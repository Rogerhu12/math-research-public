"""Lossless compressed storage for one original LocalNormalSystem tile.

The mathematical normal and its original transport are unchanged. Saving
temporarily writes one original checkpoint, then packages and verifies it,
and removes ONLY that helper-owned raw temporary directory on success.
Offline consumers read one verified logical NPZ byte string (<1 MB) at a
time. Complete loading uses the unchanged original loader in one private
temporary restore directory. No objective, matrix assembly or solve occurs.
"""
from __future__ import annotations

import io
import json
import os
from pathlib import Path
import shutil
import tempfile

import fd2d_gc_normal_checkpoint as transport
import fd2d_gc_normal_capsule as capsule_transport

SCHEMA='fd2d-compressed-original-local-normal-tile-v1'
TRANSPORT_SHA256='330fad074fcfc021279802c9b8f11e0f0f84dc6acb96e48d165360eb82dec66d'
CAPSULE_TRANSPORT_SHA256='da1f00e2936472b0a7824ebd6ea4f460eb1f5086a810e8b4c4128c9c14e73d34'
LIMIT=1_000_000
RAW_BASENAME='normal-tile'


def _sources():
    original=transport._source(transport.__file__)
    packing=transport._source(capsule_transport.__file__)
    if original['sha256']!=TRANSPORT_SHA256 or packing['sha256']!=CAPSULE_TRANSPORT_SHA256:
        raise ValueError('The original frozen numerical transport or gzip transport source changed')
    return dict(helper=transport._source(__file__),normal_transport=original,
                capsule_transport=packing)


def save_compressed_normal_tile(normal,prefix,*,binding):
    """Atomically publish a new explicit compressed-tile manifest.

    A failed pack retains its one private raw checkpoint for recovery. A
    successful publish removes that private raw directory after every gzip
    piece has been decompressed and hash-verified by the closed packer.
    Existing checkpoints, tile directories and source files are not removed.
    """
    sources=_sources();prefix=Path(prefix).absolute()
    if prefix.exists():raise FileExistsError(prefix)
    prefix.parent.mkdir(parents=True,exist_ok=True)
    raw_holder=Path(tempfile.mkdtemp(prefix='.'+prefix.name+'.raw-',dir=prefix.parent))
    pending=Path(tempfile.mkdtemp(prefix='.'+prefix.name+'.compressed-',dir=prefix.parent))
    raw_manifest=raw_holder/RAW_BASENAME/'manifest.json'
    try:
        raw_manifest=transport.save_normal_checkpoint(normal,raw_holder/RAW_BASENAME,binding=binding)
        raw_identity=capsule_transport.stream_identity(raw_manifest)
        inner=capsule_transport.create_normal_capsule(raw_manifest,pending/'payload',
            expected_manifest_sha256=raw_identity['sha256'])
        index=json.loads(inner.read_text())
        # The inner closed packer has already verified every decompressed
        # NPZ. Bind its exact index bytes, including the original manifest.
        report=dict(schema=SCHEMA,complete=True,directory_name=prefix.name,
            sources=sources,payload_index=dict(file='payload/index.json',
                                             **capsule_transport.stream_identity(inner)),
            logical_manifest=dict(file='payload/original-manifest.json',**raw_identity),
            logical_normal_schema=transport.SCHEMA,
            logical_loader='fd2d_gc_normal_checkpoint.load_normal_checkpoint',
            logical_directory_name=RAW_BASENAME,
            binding_sha256=index['original_binding_sha256'],
            mapping_sha256=index['original_mapping_sha256'],
            metadata_sha256=index['original_metadata_sha256'],
            logical_piece_count=index['piece_count'],
            logical_numerical_bytes=index['original_numerical_bytes'],
            compressed_numerical_bytes=index['compressed_numerical_bytes'],
            largest_compressed_piece_bytes=index['largest_compressed_piece_bytes'],
            original_manifest_and_pieces_lossless=True,
            raw_temporary_directory_removed_after_success=True,
            offline_piece_result='Verified original NPZ bytes, strictly below 1,000,000 bytes',
            numerical_operations_performed=False,
            mathematical_or_finite_objective_change=False)
        raw=(json.dumps(report,sort_keys=True,indent=2,allow_nan=False)+'\n').encode()
        if len(raw)>=LIMIT:raise ValueError('Compressed tile manifest exceeds its explicit limit')
        capsule_transport.write_bytes(pending/'manifest.json',raw)
        transport._fsync_directory(pending)
        if prefix.exists():raise FileExistsError(prefix)
        os.rename(pending,prefix)
        transport._fsync_directory(prefix.parent)
    except BaseException as error:
        # Never delete an existing tile. Preserve the one helper-owned raw
        # checkpoint when compression fails, so expensive progress survives.
        shutil.rmtree(pending,ignore_errors=True)
        raise RuntimeError('Compressed tile was not published; helper-owned raw data retained at '+str(raw_holder)) from error
    shutil.rmtree(raw_holder)
    return prefix/'manifest.json'


def _read(capsule):
    sources=_sources();path=Path(capsule).absolute()
    if path.name!='manifest.json':raise ValueError('Use the explicit compressed-tile manifest.json')
    raw=path.read_bytes()
    if not 0<len(raw)<LIMIT:raise ValueError('Compressed tile manifest exceeds its bound')
    outer=json.loads(raw)
    if (outer.get('schema')!=SCHEMA or outer.get('complete') is not True or
        outer.get('directory_name')!=path.parent.name or outer.get('sources')!=sources):
        raise ValueError('Incomplete, different-source or unsupported compressed tile')
    row=outer['payload_index']
    if row.get('file')!='payload/index.json':raise ValueError('Unexpected fixed payload index path')
    inner=path.parent/'payload/index.json'
    if capsule_transport.stream_identity(inner)!={k:row[k] for k in ('bytes','sha256')}:
        raise ValueError('Compressed tile inner index SHA differs')
    index=json.loads(inner.read_text())
    if (index.get('schema')!=capsule_transport.SCHEMA or index.get('complete') is not True or
            index.get('source_sha256')!=CAPSULE_TRANSPORT_SHA256):
        raise ValueError('Wrong inner gzip capsule schema or source')
    manifest_row=outer['logical_manifest']
    if manifest_row.get('file')!='payload/original-manifest.json':
        raise ValueError('Unexpected logical manifest path')
    original_path=path.parent/'payload/original-manifest.json'
    original_raw,logical=capsule_transport._read_original_manifest(original_path,
        manifest_row['sha256'])
    if len(original_raw)!=manifest_row['bytes']:
        raise ValueError('Logical manifest size differs')
    if (index['original_manifest']!={'file':'original-manifest.json',
            'bytes':manifest_row['bytes'],'sha256':manifest_row['sha256']} or
            logical['directory_name']!=RAW_BASENAME or
            outer['logical_directory_name']!=RAW_BASENAME or
            outer['logical_normal_schema']!=transport.SCHEMA):
        raise ValueError('Compressed and original manifest identities disagree')
    for key in ('binding','mapping','metadata'):
        if (outer[key+'_sha256']!=logical[key+'_sha256'] or
                index['original_'+key+'_sha256']!=logical[key+'_sha256']):
            raise ValueError('A logical '+key+' identity differs')
    rows=logical['pieces'];compressed=index['pieces']
    names=[r['original_file'] for r in compressed]
    if (len(rows)!=len(compressed) or len(rows)!=outer['logical_piece_count'] or
            len(rows)!=index['piece_count'] or len(set(names))!=len(names) or
            set(names)!={r['file'] for r in rows}):
        raise ValueError('Incomplete or duplicate compressed tile coverage')
    if (sum(r['bytes'] for r in rows)!=outer['logical_numerical_bytes'] or
            sum(r['compressed']['bytes'] for r in compressed)!=outer['compressed_numerical_bytes']):
        raise ValueError('Compressed tile numerical totals differ')
    return path,outer,index,logical


def read_logical_manifest(capsule):
    """Return the unchanged original metadata object, with its real schema."""
    return _read(capsule)[3]


def read_logical_piece(capsule,row):
    """Return one SHA-verified original NPZ byte string, never >=1 MB.

    ``row`` must be exactly one row returned by read_logical_manifest().
    Callers may use np.load(io.BytesIO(bytes), allow_pickle=False). This
    method does not manufacture a fake uncompressed path or transport schema.
    """
    path,outer,index,logical=_read(capsule)
    matches=[r for r in logical['pieces'] if r['file']==row.get('file')]
    if len(matches)!=1 or matches[0]!=row:
        raise ValueError('The requested logical piece row is not exactly bound by this capsule')
    packed=next(r for r in index['pieces'] if r['original_file']==row['file'])
    expected={k:row[k] for k in ('bytes','sha256')}
    if packed['original']!=expected or not 0<expected['bytes']<LIMIT:
        raise ValueError('The requested original piece identity or bound differs')
    compressed=packed['compressed']
    name=capsule_transport.basename(packed['compressed_file'],'.npz.gz')
    source=path.parent/'payload'/name
    if (not 0<compressed['bytes']<LIMIT or
            capsule_transport.stream_identity(source)!=compressed):
        raise ValueError('The compressed piece SHA or bound differs')
    output=io.BytesIO()
    capsule_transport.stream_inflate(source,expected,output)
    return output.getvalue()


def load_compressed_normal_tile(problem,capsule,*,expected_binding):
    """Restore one private raw checkpoint and invoke the unchanged loader.

    At most one logical piece is decompressed at a time. One complete raw
    checkpoint temporarily occupies disk only for this load, not for every
    tile. The original loader alone rebuilds and verifies the exact mapping,
    source, objective binding, shape/dtype and metadata identities.
    """
    path,outer,index,logical=_read(capsule)
    binding=transport._binding(expected_binding)
    if (transport._binding(logical['binding'])!=binding or
            logical['binding_sha256']!=transport._sha(binding.encode())):
        raise ValueError('Actual state/source/objective binding differs')
    with tempfile.TemporaryDirectory(prefix='fd2d-compressed-normal-tile-load-') as directory:
        restored=capsule_transport.restore_normal_capsule(path.parent/'payload/index.json',
            Path(directory)/RAW_BASENAME,
            expected_manifest_sha256=outer['logical_manifest']['sha256'])
        return transport.load_normal_checkpoint(problem,restored,expected_binding=expected_binding)
