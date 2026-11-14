"""Lossless, atomic, bounded-piece transport of an actual LocalNormalSystem.

No objective/Jacobian/normal assembly, scaling, factorization, or nonlinear
step occurs here. The caller supplies the complete mathematical binding;
it is opaque JSON, not guessed from cache counters, timestamps, or paths.

save_normal_checkpoint(normal, prefix, *, binding) -> Path to manifest.json
load_normal_checkpoint(problem, manifest, *, expected_binding) -> original
LocalNormalSystem, whose exact elimination map is rebuilt and verified.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import struct
import tempfile
import numpy as np
from fd2d_gc_local_normal_system import LocalNormalSystem
import fd2d_gc_local_normal_system as original_module


SCHEMA='fd2d-lossless-local-normal-checkpoint-v1'
PIECE_LIMIT=1_000_000
MAX_NODES_PER_PIECE=4
_MAPPING_ARRAYS=('central_nodes','extra','pairs','fixed','free','widths','offsets')
_MAPPING_LISTS=('node_free','field_maps','parameter_maps')
_MAPPING_SCALARS=('N','q','P','total','count')
_GLOBAL_ARRAYS=('Hpp','gp','parameter_norm_squared')
_METADATA=('residual_squared','rows','blocks','row_groups','info')


def _sha(data):return hashlib.sha256(data).hexdigest()


def _source(path):
    path=Path(path);raw=path.read_bytes()
    return dict(name=path.name,bytes=len(raw),sha256=_sha(raw))


def _json(value):
    return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False)


def _binding(value):
    # JSON type identity is explicit: 1 and 1.0 remain distinct, object
    # member order is immaterial, and no NumPy/tuple coercion is hidden.
    def visit(x):
        if x is None or type(x) in (bool,str,int):return
        if type(x) is float:
            if not np.isfinite(x):raise ValueError('Binding JSON numbers must be finite')
            return
        if type(x) is list:
            for item in x:visit(item)
            return
        if type(x) is dict:
            if not all(type(k) is str for k in x):raise TypeError('Binding object keys must be strings')
            for item in x.values():visit(item)
            return
        raise TypeError('Binding must already be explicit JSON; unsupported '+type(x).__name__)
    visit(value)
    if type(value) is not dict:raise TypeError('Binding must be an explicit JSON object')
    return _json(value)


def _array_id(value):
    a=np.asarray(value)
    if a.dtype.hasobject or a.dtype.fields is not None or a.dtype.subdtype is not None:
        raise TypeError('Only ordinary non-object numerical arrays can enter the checkpoint')
    data=np.ascontiguousarray(a).tobytes(order='C')
    return dict(shape=list(a.shape),dtype=a.dtype.str,bytes=len(data),sha256=_sha(data))


def _mapping_definition(mapping):
    return dict(scalars={key:int(getattr(mapping,key)) for key in _MAPPING_SCALARS},
        arrays={key:_array_id(getattr(mapping,key)) for key in _MAPPING_ARRAYS},
        node_arrays={key:[_array_id(a) for a in getattr(mapping,key)] for key in _MAPPING_LISTS})


def _pack_metadata(value):
    """Typed JSON, including binary floating scalars, without pickle.

    The normal's actual diagnostics are small. An unexpected large array
    in info is rejected rather than silently dumped into JSON metadata.
    """
    if value is None:return ['none']
    if type(value) is bool:return ['bool',value]
    if type(value) is int:return ['int',str(value)]
    if type(value) is float:return ['float64-bits',struct.pack('>d',value).hex()]
    if type(value) is str:return ['str',value]
    if type(value) is list:return ['list',[_pack_metadata(x) for x in value]]
    if type(value) is tuple:return ['tuple',[_pack_metadata(x) for x in value]]
    if type(value) is dict:
        if not all(type(k) is str for k in value):raise TypeError('Diagnostic keys must be strings')
        return ['dict',[[k,_pack_metadata(v)] for k,v in value.items()]]
    if isinstance(value,np.generic):
        a=np.asarray(value);identity=_array_id(a)
        return ['numpy-scalar',identity,a.tobytes().hex()]
    if isinstance(value,np.ndarray):
        identity=_array_id(value)
        if value.nbytes>65536:raise ValueError('Unexpected large array in normal.info; keep numerical payloads in explicit array blocks')
        return ['small-numpy-array',identity,np.ascontiguousarray(value).tobytes().hex()]
    raise TypeError('Unsupported non-JSON diagnostic value '+type(value).__name__)


def _unpack_metadata(packet):
    tag=packet[0]
    if tag=='none':return None
    if tag=='bool':return bool(packet[1])
    if tag=='int':return int(packet[1])
    if tag=='float64-bits':return struct.unpack('>d',bytes.fromhex(packet[1]))[0]
    if tag=='str':return packet[1]
    if tag in ('list','tuple'):
        out=[_unpack_metadata(x) for x in packet[1]]
        return tuple(out) if tag=='tuple' else out
    if tag=='dict':return {key:_unpack_metadata(v) for key,v in packet[1]}
    if tag in ('numpy-scalar','small-numpy-array'):
        desc=packet[1];dtype=np.dtype(desc['dtype'])
        if dtype.hasobject or dtype.fields is not None or dtype.subdtype is not None:
            raise ValueError('Unsafe diagnostic array dtype')
        raw=bytes.fromhex(packet[2])
        a=np.frombuffer(raw,dtype=dtype).copy().reshape(tuple(desc['shape']))
        if _array_id(a)!=desc:raise ValueError('Diagnostic binary payload identity mismatch')
        return a[()] if tag=='numpy-scalar' else a
    raise ValueError('Unsupported typed diagnostic tag')


def _node_arrays(normal,start,stop):
    m=normal.mapping;out={}
    for node in range(start,stop):
        label=f'{node:06d}';a,b=map(int,m.offsets[node:node+2])
        out['diagonal_'+label]=normal.diagonal[node]
        if node<m.N-1:out['upper_'+label]=normal.upper[node]
        out['Hfp_'+label]=normal.Hfp[a:b]
        out['gf_'+label]=normal.gf[a:b]
        out['field_norm_squared_'+label]=normal.field_norm_squared[a:b]
    return out


def _validate_normal_layout(normal):
    if type(normal) is not LocalNormalSystem:
        raise TypeError('This transport stores the original LocalNormalSystem, not a serialized subclass')
    m=normal.mapping
    expected={'Hfp':(m.count,m.P),'Hpp':(m.P,m.P),'gf':(m.count,),
              'gp':(m.P,),'field_norm_squared':(m.count,),'parameter_norm_squared':(m.P,)}
    if len(normal.diagonal)!=m.N or len(normal.upper)!=m.N-1:
        raise ValueError('Normal block list lengths differ from its elimination map')
    for key,shape in expected.items():
        a=getattr(normal,key)
        if not isinstance(a,np.ndarray) or a.shape!=shape or a.dtype!=np.dtype('float64'):
            raise ValueError('Wrong original normal array layout: '+key)
    for j,a in enumerate(normal.diagonal):
        if a.shape!=(m.widths[j],m.widths[j]) or a.dtype!=np.dtype('float64'):
            raise ValueError('Wrong node diagonal layout')
    for j,a in enumerate(normal.upper):
        if a.shape!=(m.widths[j],m.widths[j+1]) or a.dtype!=np.dtype('float64'):
            raise ValueError('Wrong adjacent-node upper layout')


def _estimate(arrays):
    # A conservative allowance for numerical .npy headers and ZIP entries.
    # The actual final file length is checked independently before commit.
    return sum(np.asarray(a).nbytes+1024 for a in arrays.values())+1024


def _fsync_directory(path):
    fd=os.open(path,os.O_RDONLY|os.O_DIRECTORY)
    try:os.fsync(fd)
    finally:os.close(fd)


def _write_piece(directory,name,kind,arrays,*,node_range=None):
    if _estimate(arrays)>=PIECE_LIMIT:
        raise ValueError('A single requested block packet exceeds the explicit <1MB transport size; it was not committed')
    tmp=directory/(name+'.tmp');dest=directory/name
    with tmp.open('xb') as stream:
        np.savez(stream,**arrays)
        stream.flush();os.fsync(stream.fileno())
    raw=tmp.read_bytes()
    if len(raw)>=PIECE_LIMIT:
        raise ValueError('An actual NPZ piece is not strictly below 1,000,000 bytes')
    os.rename(tmp,dest)
    out=dict(file=name,kind=kind,bytes=len(raw),sha256=_sha(raw),
             arrays={key:_array_id(value) for key,value in arrays.items()})
    if node_range is not None:out['node_range']=list(node_range)
    return out


def save_normal_checkpoint(normal,prefix,*,binding):
    """Write a NEW directory atomically, returning its final manifest Path.

    Each numerical NPZ piece is <1,000,000 bytes; a node piece contains
    at most four nodes. The current K31/129-node layout is well inside
    these limits. No existing checkpoint is overwritten. On interrupted
    writes the uniquely named temporary directory is not loadable.
    """
    _validate_normal_layout(normal)
    encoded_binding=_binding(binding)
    prefix=Path(prefix).absolute()
    if prefix.exists():raise FileExistsError(prefix)
    prefix.parent.mkdir(parents=True,exist_ok=True)
    temp=Path(tempfile.mkdtemp(prefix='.'+prefix.name+'.incomplete-',dir=prefix.parent))
    mapping=_mapping_definition(normal.mapping)
    metadata={key:_pack_metadata(getattr(normal,key)) for key in _METADATA}
    pieces=[]
    pieces.append(_write_piece(temp,'mapping.npz','mapping',
        {key:np.asarray(getattr(normal.mapping,key)) for key in _MAPPING_ARRAYS}))
    pieces.append(_write_piece(temp,'global.npz','global',
        {key:getattr(normal,key) for key in _GLOBAL_ARRAYS}))
    start=0
    while start<normal.mapping.N:
        stop=start+1
        if _estimate(_node_arrays(normal,start,stop))>=PIECE_LIMIT:
            raise ValueError('A single node exceeds the declared bounded transport piece; no checkpoint was committed')
        while stop<normal.mapping.N and stop-start<MAX_NODES_PER_PIECE:
            if _estimate(_node_arrays(normal,start,stop+1))>=PIECE_LIMIT:break
            stop+=1
        pieces.append(_write_piece(temp,f'nodes-{start:06d}-{stop:06d}.npz','nodes',
            _node_arrays(normal,start,stop),node_range=(start,stop)))
        start=stop
    report=dict(schema=SCHEMA,complete=True,directory_name=prefix.name,
        storage='Uncompressed NPZ; exact ordinary numerical dtypes; no pickle; C-order logical-byte SHA256',
        piece_limit_exclusive=PIECE_LIMIT,max_nodes_per_piece=MAX_NODES_PER_PIECE,
        source=_source(__file__),original_normal_source=_source(original_module.__file__),
        binding=json.loads(encoded_binding),binding_sha256=_sha(encoded_binding.encode('utf-8')),
        mapping=mapping,mapping_sha256=_sha(_json(mapping).encode('utf-8')),
        metadata=metadata,metadata_sha256=_sha(_json(metadata).encode('utf-8')),
        pieces=pieces,normal_storage_bytes=int(normal.storage_bytes()),
        numerical_piece_count=len(pieces),numerical_piece_bytes=sum(p['bytes'] for p in pieces),
        numerical_operations_performed=False,mathematical_or_finite_objective_change=False)
    raw=(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2,allow_nan=False)+'\n').encode('utf-8')
    # The manifest is the last file, and the whole directory is only then
    # renamed to the caller's unique final name. A temp-name manifest is
    # explicitly rejected by load through directory_name.
    with (temp/'manifest.json.tmp').open('xb') as stream:
        stream.write(raw);stream.flush();os.fsync(stream.fileno())
    os.rename(temp/'manifest.json.tmp',temp/'manifest.json')
    _fsync_directory(temp)
    if prefix.exists():raise FileExistsError(prefix)
    os.rename(temp,prefix);_fsync_directory(prefix.parent)
    return prefix/'manifest.json'


def _read_piece(directory,row,expected):
    name=row['file']
    if type(name) is not str or Path(name).name!=name or not name.endswith('.npz'):
        raise ValueError('Piece names must be relative NPZ basenames')
    path=directory/name
    if not 0<row['bytes']<PIECE_LIMIT or path.stat().st_size!=row['bytes']:
        raise ValueError('Checkpoint piece byte count differs or exceeds limit')
    raw=path.read_bytes()
    if _sha(raw)!=row['sha256']:raise ValueError('Checkpoint piece SHA256 mismatch: '+name)
    # Bound a read to one actual piece. np.load receives allow_pickle=False
    # and every array is checked against both its saved identity and the
    # shape/dtype allocated by the original LocalNormalSystem.
    import io
    with np.load(io.BytesIO(raw),allow_pickle=False) as packet:
        if set(packet.files)!=set(expected) or set(row['arrays'])!=set(expected):
            raise ValueError('Checkpoint piece array keys differ from the declared original layout')
        for key,target in expected.items():
            value=packet[key]
            if value.shape!=target.shape or value.dtype.str!=target.dtype.str:
                raise ValueError('Checkpoint array shape/dtype mismatch: '+key)
            if _array_id(value)!=row['arrays'][key]:
                raise ValueError('Checkpoint array SHA256 mismatch: '+key)
            yield key,value


def load_normal_checkpoint(problem,manifest,*,expected_binding):
    """Rebuild the ORIGINAL elimination map, verify all identities, and load.

    A partially written/mismatched checkpoint is never returned. This
    function does not recompute a residual, a Jacobian, or a normal block.
    """
    manifest=Path(manifest).absolute()
    if manifest.name!='manifest.json':raise ValueError('Load the completed manifest.json')
    report=json.loads(manifest.read_text())
    if (report.get('schema')!=SCHEMA or report.get('complete') is not True
            or report.get('directory_name')!=manifest.parent.name):
        raise ValueError('Incomplete, temporary, or unsupported normal checkpoint')
    binding=_binding(expected_binding)
    if (_binding(report['binding'])!=binding
            or report['binding_sha256']!=_sha(binding.encode('utf-8'))):
        raise ValueError('Actual state/source/objective binding differs')
    if (report['source']!=_source(__file__)
            or report['original_normal_source']!=_source(original_module.__file__)):
        raise ValueError('Original normal or checkpoint implementation source identity differs')
    if (report.get('piece_limit_exclusive')!=PIECE_LIMIT
            or report.get('max_nodes_per_piece')!=MAX_NODES_PER_PIECE):
        raise ValueError('Different bounded-piece schema')
    # No serialized class or mapping is trusted. All matrices below are
    # allocated by the unchanged source class using the caller's problem.
    normal=LocalNormalSystem(problem)
    mapping=_mapping_definition(normal.mapping)
    if (report['mapping']!=mapping
            or report['mapping_sha256']!=_sha(_json(mapping).encode('utf-8'))):
        raise ValueError('Rebuilt exact elimination map differs from the saved mapping')
    pieces=report['pieces']
    if len(pieces)!=report['numerical_piece_count'] or len({p['file'] for p in pieces})!=len(pieces):
        raise ValueError('Missing or duplicate checkpoint pieces')
    if sum(p['bytes'] for p in pieces)!=report['numerical_piece_bytes']:
        raise ValueError('Numerical piece total differs')
    kinds=[p['kind'] for p in pieces]
    if kinds[:2]!=['mapping','global'] or any(k!='nodes' for k in kinds[2:]):
        raise ValueError('Checkpoint pieces must be mapping, globals, then complete ordered node ranges')
    expected={key:np.asarray(getattr(normal.mapping,key)) for key in _MAPPING_ARRAYS}
    for key,value in _read_piece(manifest.parent,pieces[0],expected):
        if _array_id(value)!=_array_id(expected[key]):
            raise ValueError('Stored actual mapping bytes differ from the rebuilt mapping')
    globals_={key:getattr(normal,key) for key in _GLOBAL_ARRAYS}
    for key,value in _read_piece(manifest.parent,pieces[1],globals_):globals_[key][...]=value
    next_node=0
    for row in pieces[2:]:
        pair=row.get('node_range',[])
        if (len(pair)!=2 or any(type(x) is not int for x in pair)
                or pair[0]!=next_node or not pair[0]<pair[1]<=normal.mapping.N
                or pair[1]-pair[0]>MAX_NODES_PER_PIECE):
            raise ValueError('Node ranges have gaps, overlaps, or exceed four nodes')
        expected=_node_arrays(normal,*pair)
        for key,value in _read_piece(manifest.parent,row,expected):expected[key][...]=value
        next_node=pair[1]
    if next_node!=normal.mapping.N:raise ValueError('Normal checkpoint lacks final node blocks')
    metadata=report['metadata']
    if set(metadata)!=set(_METADATA) or report['metadata_sha256']!=_sha(_json(metadata).encode('utf-8')):
        raise ValueError('Normal diagnostic metadata identity differs')
    for key in _METADATA:setattr(normal,key,_unpack_metadata(metadata[key]))
    if _json({key:_pack_metadata(getattr(normal,key)) for key in _METADATA})!=_json(metadata):
        raise ValueError('Normal metadata failed exact typed roundtrip')
    _validate_normal_layout(normal)
    if normal.storage_bytes()!=report['normal_storage_bytes']:
        raise ValueError('Restored normal numerical layout storage differs')
    return normal
