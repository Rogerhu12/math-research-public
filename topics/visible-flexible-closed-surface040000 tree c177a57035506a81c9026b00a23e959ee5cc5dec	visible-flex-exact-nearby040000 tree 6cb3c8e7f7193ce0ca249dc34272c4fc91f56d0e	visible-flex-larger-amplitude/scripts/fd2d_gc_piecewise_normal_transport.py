"""Explicit new transport for exact-order, independently merged small pieces.

Offline reduction does not reconstruct a geometry or pretend to call the
original saver. This CONSUMER reconstructs the original LocalNormalSystem
and verifies its full elimination map before any factorization or use.
"""
import json
from pathlib import Path

SCHEMA='fd2d-offline-piecewise-ordered-normal-v1'


def load_piecewise_normal(problem,manifest,*,expected_binding):
    import numpy as np
    import fd2d_gc_normal_checkpoint as t
    from fd2d_gc_local_normal_system import LocalNormalSystem
    manifest=Path(manifest).absolute();r=json.loads(manifest.read_text())
    if r.get('schema')!=SCHEMA or r.get('complete') is not True or r['directory_name']!=manifest.parent.name:
        raise ValueError('Incomplete piecewise sum')
    if t._binding(r['binding'])!=t._binding(expected_binding):raise ValueError('Different actual finite goal')
    if r['binding_sha256']!=t._sha(t._binding(expected_binding).encode()):raise ValueError('Binding bytes changed')
    if r['original_normal_source']!=t._source(t.original_module.__file__):raise ValueError('Original normal implementation changed')
    if r['piece_consumer_source']!=t._source(__file__):raise ValueError('Piece consumer implementation changed')
    normal=LocalNormalSystem(problem);mapping=t._mapping_definition(normal.mapping)
    if mapping!=r['mapping'] or r['mapping_sha256']!=t._sha(t._json(mapping).encode()):
        raise ValueError('Actual full elimination mapping differs from saved input tiles')
    pieces=r['pieces']
    if len(pieces)!=r['numerical_piece_count'] or len({p['file'] for p in pieces})!=len(pieces):
        raise ValueError('Missing or duplicate final pieces')
    if sum(p['bytes'] for p in pieces)!=r['numerical_piece_bytes']:raise ValueError('Piece byte count changed')
    if [p['kind'] for p in pieces[:2]]!=['mapping','global'] or any(p['kind']!='nodes' for p in pieces[2:]):
        raise ValueError('Final piece order changed')
    expected={key:np.asarray(getattr(normal.mapping,key)) for key in t._MAPPING_ARRAYS}
    for key,value in t._read_piece(manifest.parent,pieces[0],expected):
        if t._array_id(value)!=t._array_id(expected[key]):raise ValueError('Actual mapping arrays differ')
    expected={key:getattr(normal,key) for key in t._GLOBAL_ARRAYS}
    for key,value in t._read_piece(manifest.parent,pieces[1],expected):expected[key][...]=value
    stop=0
    for row in pieces[2:]:
        pair=row['node_range']
        if len(pair)!=2 or pair[0]!=stop or not stop<pair[1]<=normal.mapping.N or pair[1]-stop>4:
            raise ValueError('Incomplete or overlapping node ranges')
        expected=t._node_arrays(normal,*pair)
        for key,value in t._read_piece(manifest.parent,row,expected):expected[key][...]=value
        stop=pair[1]
    if stop!=normal.mapping.N:raise ValueError('Missing final normal nodes')
    md=r['metadata']
    if set(md)!=set(t._METADATA) or r['metadata_sha256']!=t._sha(t._json(md).encode()):raise ValueError('Typed metadata changed')
    for key in t._METADATA:setattr(normal,key,t._unpack_metadata(md[key]))
    if t._json({key:t._pack_metadata(getattr(normal,key)) for key in t._METADATA})!=t._json(md):
        raise ValueError('Typed metadata roundtrip changed')
    t._validate_normal_layout(normal)
    if normal.storage_bytes()!=r['normal_storage_bytes']:raise ValueError('Different numerical normal layout')
    return normal
