"""Add one closed tile while retaining only the total and one <1MB piece.

The original transport and partition checkers still verify exact sources,
binding, map, typed metadata, row ledger, piece bytes, and array bytes.
No second full LocalNormalSystem is allocated. All array additions follow
the original TILE order, hence each scalar receives the same float64 sum.
A failed read mutates only the caller's uncommitted in-memory total.
"""
import copy
import json
from pathlib import Path
import numpy as np
import fd2d_gc_normal_checkpoint as transport
import fd2d_gc_grouped_coast_partitioned_normal as partition


def add_closed_normal_tile(total,manifest,*,expected_binding,problem,descriptor,plan):
    manifest=Path(manifest).absolute();report=json.loads(manifest.read_text())
    if (manifest.name!='manifest.json' or report.get('schema')!=transport.SCHEMA
            or report.get('complete') is not True or report.get('directory_name')!=manifest.parent.name):
        raise ValueError('Incomplete or incorrectly named tile checkpoint')
    binding=transport._binding(expected_binding)
    if (transport._binding(report['binding'])!=binding
            or report['binding_sha256']!=transport._sha(binding.encode('utf-8'))):
        raise ValueError('Actual tile state/source/objective binding differs')
    if (report['source']!=transport._source(transport.__file__)
            or report['original_normal_source']!=transport._source(transport.original_module.__file__)
            or report.get('piece_limit_exclusive')!=transport.PIECE_LIMIT
            or report.get('max_nodes_per_piece')!=transport.MAX_NODES_PER_PIECE):
        raise ValueError('Original transport/normal implementation differs')
    mapping=transport._mapping_definition(total.mapping)
    if report['mapping']!=mapping or report['mapping_sha256']!=transport._sha(transport._json(mapping).encode('utf-8')):
        raise ValueError('Exact elimination map differs')
    pieces=report['pieces']
    if (len(pieces)!=report['numerical_piece_count'] or len({p['file'] for p in pieces})!=len(pieces)
            or sum(p['bytes'] for p in pieces)!=report['numerical_piece_bytes']):
        raise ValueError('Missing, repeated, or incorrectly sized transport pieces')
    kinds=[p['kind'] for p in pieces]
    if kinds[:2]!=['mapping','global'] or any(k!='nodes' for k in kinds[2:]):
        raise ValueError('Tile pieces do not have the original complete order')
    metadata=report['metadata']
    if set(metadata)!=set(transport._METADATA) or report['metadata_sha256']!=transport._sha(transport._json(metadata).encode('utf-8')):
        raise ValueError('Typed diagnostic metadata differs')
    # Shallow copy shares the already validated TOTAL arrays only for layout
    # checks. Every incoming array is checked for finiteness below, before add.
    view=copy.copy(total)
    for key in transport._METADATA:setattr(view,key,transport._unpack_metadata(metadata[key]))
    if transport._json({key:transport._pack_metadata(getattr(view,key)) for key in transport._METADATA})!=transport._json(metadata):
        raise ValueError('Tile typed metadata failed exact roundtrip')
    info=partition._check_tile(problem,descriptor,view,plan)
    if view.storage_bytes()!=report['normal_storage_bytes']:
        raise ValueError('Actual tile storage layout differs')
    wanted={key:np.asarray(getattr(total.mapping,key)) for key in transport._MAPPING_ARRAYS}
    for key,value in transport._read_piece(manifest.parent,pieces[0],wanted):
        if transport._array_id(value)!=transport._array_id(wanted[key]):
            raise ValueError('Stored mapping bytes differ')
    wanted={key:getattr(total,key) for key in transport._GLOBAL_ARRAYS}
    for key,value in transport._read_piece(manifest.parent,pieces[1],wanted):
        if not np.all(np.isfinite(value)):raise FloatingPointError('Nonfinite actual tile array')
        wanted[key][...]+=value
    next_node=0
    for row in pieces[2:]:
        pair=row.get('node_range',[])
        if (len(pair)!=2 or any(type(x) is not int for x in pair) or pair[0]!=next_node
                or not pair[0]<pair[1]<=total.mapping.N or pair[1]-pair[0]>transport.MAX_NODES_PER_PIECE):
            raise ValueError('Tile node ranges have gaps or overlaps')
        wanted=transport._node_arrays(total,*pair)
        for key,value in transport._read_piece(manifest.parent,row,wanted):
            if not np.all(np.isfinite(value)):raise FloatingPointError('Nonfinite actual tile array')
            wanted[key][...]+=value
        next_node=pair[1]
    if next_node!=total.mapping.N:raise ValueError('Tile lacks final node blocks')
    total.residual_squared+=float(view.residual_squared)
    total.rows+=int(view.rows);total.blocks+=int(view.blocks)
    for label,count in view.row_groups.items():total.row_groups[label]=total.row_groups.get(label,0)+int(count)
    return dict(state_binding=info['state_binding'],
        summary=dict(id=descriptor['id'],ordinal=descriptor['ordinal'],rows=int(view.rows),
            local_blocks=int(view.blocks),residual_squared=float(view.residual_squared),row_groups=dict(view.row_groups)))
