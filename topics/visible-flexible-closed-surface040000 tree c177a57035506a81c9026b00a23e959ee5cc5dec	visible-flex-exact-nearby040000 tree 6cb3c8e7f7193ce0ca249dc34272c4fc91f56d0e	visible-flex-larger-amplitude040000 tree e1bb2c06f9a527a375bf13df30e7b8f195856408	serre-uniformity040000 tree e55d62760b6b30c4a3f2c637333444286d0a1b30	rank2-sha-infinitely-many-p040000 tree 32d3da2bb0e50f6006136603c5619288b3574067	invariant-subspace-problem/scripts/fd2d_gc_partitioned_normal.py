"""Durable row-group partitions of the unchanged R159/v25 finite normal.

Assembly uses the frozen subset stream and independent interior rows.
Transport is deliberately delegated to fd2d_gc_normal_checkpoint. Merge
consumes an ordered iterator: one incoming normal plus one running sum,
never a list of all full-shape normal packets. Scaling/damping happens only
after the complete unscaled sum, through the original direction routine.
"""
from __future__ import annotations
from collections import Counter
import hashlib
import inspect
import json
from pathlib import Path
import time
import numpy as np

from fd2d_gc_local_normal_system import LocalNormalSystem, EliminatedFieldMap
from fd2d_gc_normal_checkpoint import _mapping_definition, _array_id, _binding, _validate_normal_layout
from fd2d_gc_positive_trace_stream_normal_consumer import stream_positive_trace_normal
from fd2d_gc_positive_trace_interior_merit import interior_gauss_curvature
from fd2d_gc_gauss_cell_frozen_operator_compatible import gauss_cell_positive_trace_frozen_operator_compatible

PLAN_SCHEMA='fd2d-R159-exact-row-partition-v1'
TILE_SCHEMA='fd2d-R159-actual-normal-tile-v1'
MERGE_SCHEMA='fd2d-R159-ordered-normal-tile-sum-v1'
ARRAYS=('Hfp','Hpp','gf','gp','field_norm_squared','parameter_norm_squared')
DESCRIPTOR_KEYS=('id','ordinal','kind','node_indices','cell_indices','include_boundary','interior_cells',
                 'mapping_sha256','mesh_identity','dimensions','partition_source_sha256')


def _json(value):
    return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False)


def _digest(value):
    return hashlib.sha256(_json(value).encode()).hexdigest()


def _source_sha():
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def _mapping_sha(mapping):
    return _digest(_mapping_definition(mapping))


def _dimensions(problem):
    return dict(nodes=int(problem.N),q=int(problem.q),parameters=int(problem.parameter_count),
                modes=int(problem.K),work=int(problem.work))


def _indices(values,limit):
    if any(type(v) is not int for v in values):
        raise TypeError('Row indices must be explicit JSON integers')
    if len(set(values))!=len(values) or any(v<0 or v>=limit for v in values):
        raise ValueError('Duplicated or out-of-range row-group indices')
    return list(values)


def _bare_descriptor(descriptor):
    if set(descriptor)!=set(DESCRIPTOR_KEYS)|{'plan_sha256'}:
        raise ValueError('Unknown or missing normal tile descriptor keys')
    return {key:descriptor[key] for key in DESCRIPTOR_KEYS}


def _plan_payload(plan):
    return {key:([{k:d[k] for k in DESCRIPTOR_KEYS} for d in value] if key=='tiles' else value)
            for key,value in plan.items() if key!='plan_sha256'}


def make_normal_partition(problem,*,node_block=16,cell_block=4,interior_cells=(),interior_block=1):
    for value,limit in ((node_block,16),(cell_block,4),(interior_block,4)):
        if type(value) is not int or not 1<=value<=limit:
            raise ValueError('Use node blocks<=16, cell blocks<=4, interior blocks<=4')
    interior=_indices(list(interior_cells),problem.N-1)
    mapping=EliminatedFieldMap(problem)
    dimensions=_dimensions(problem)
    mesh=_array_id(np.asarray(problem.x))
    mapping_sha=_mapping_sha(mapping)
    source=_source_sha()
    tiles=[]
    def add(kind,nodes=(),cells=(),boundary=False,inside=()):
        index=len(tiles)
        tile=dict(id=f'{index:04d}-{kind}',ordinal=index,kind=kind,
            node_indices=list(nodes),cell_indices=list(cells),include_boundary=bool(boundary),
            interior_cells=list(inside),mapping_sha256=mapping_sha,mesh_identity=mesh,
            dimensions=dimensions,partition_source_sha256=source)
        tiles.append(tile)
    for start in range(0,problem.N,node_block):
        add('nodes',nodes=range(start,min(start+node_block,problem.N)))
    for start in range(0,problem.N-1,cell_block):
        add('cells',cells=range(start,min(start+cell_block,problem.N-1)))
    add('boundary',boundary=True)
    for start in range(0,len(interior),interior_block):
        add('interior',inside=interior[start:start+interior_block])
    plan=dict(schema=PLAN_SCHEMA,partition_source_sha256=source,dimensions=dimensions,
        mesh_identity=mesh,mapping_sha256=mapping_sha,node_block=node_block,cell_block=cell_block,
        interior_block=interior_block,interior_cells=interior,
        row_order=['nodes','cells','boundary','interior'],tiles=tiles,
        finite_objective_changed=False,scaling_or_damping_applied=False,
        floating_bit_identity_of_regrouped_sum_claimed=False)
    sha=_digest(plan)
    plan['plan_sha256']=sha
    for tile in tiles:tile['plan_sha256']=sha
    validate_normal_partition(problem,plan)
    return plan


def _validate_descriptor(problem,descriptor):
    _bare_descriptor(descriptor)
    if descriptor['partition_source_sha256']!=_source_sha():
        raise ValueError('Different partition implementation source')
    if descriptor['dimensions']!=_dimensions(problem) or descriptor['mesh_identity']!=_array_id(np.asarray(problem.x)):
        raise ValueError('Actual problem dimensions/mesh differ from the tile')
    if type(descriptor['ordinal']) is not int or descriptor['ordinal']<0:
        raise ValueError('Invalid tile ordinal')
    if type(descriptor['id']) is not str or type(descriptor['include_boundary']) is not bool:
        raise TypeError('Invalid explicit tile id/boundary flag')
    n=_indices(descriptor['node_indices'],problem.N)
    c=_indices(descriptor['cell_indices'],problem.N-1)
    i=_indices(descriptor['interior_cells'],problem.N-1)
    flags=(bool(n),bool(c),descriptor['include_boundary'],bool(i))
    expected={'nodes':(True,False,False,False),'cells':(False,True,False,False),
              'boundary':(False,False,True,False),'interior':(False,False,False,True)}
    if descriptor['kind'] not in expected or flags!=expected[descriptor['kind']]:
        raise ValueError('A normal tile must contain exactly its one declared row-group family')


def validate_normal_partition(problem,plan):
    if plan.get('schema')!=PLAN_SCHEMA or plan.get('partition_source_sha256')!=_source_sha():
        raise ValueError('Unknown partition or changed implementation')
    if plan.get('dimensions')!=_dimensions(problem) or plan.get('mesh_identity')!=_array_id(np.asarray(problem.x)):
        raise ValueError('Different actual problem/mesh')
    if _digest(_plan_payload(plan))!=plan.get('plan_sha256'):
        raise ValueError('Partition descriptor content does not match its SHA')
    nodes=[];cells=[];interior=[];boundary=0;seen=set();last=-1
    kinds={'nodes':0,'cells':1,'boundary':2,'interior':3}
    for ordinal,tile in enumerate(plan['tiles']):
        _validate_descriptor(problem,tile)
        if (tile['ordinal']!=ordinal or tile['id'] in seen or tile['plan_sha256']!=plan['plan_sha256']
                or tile['mapping_sha256']!=plan['mapping_sha256']):
            raise ValueError('Duplicate/misordered tile or inconsistent plan/mapping binding')
        group=kinds[tile['kind']]
        if group<last:raise ValueError('Tile families must retain original node/cell/boundary/interior order')
        last=group;seen.add(tile['id']);nodes+=tile['node_indices'];cells+=tile['cell_indices']
        interior+=tile['interior_cells'];boundary+=int(tile['include_boundary'])
        if len(tile['node_indices'])>plan['node_block'] or len(tile['cell_indices'])>plan['cell_block'] or len(tile['interior_cells'])>plan['interior_block']:
            raise ValueError('A tile exceeds its explicit small-block bound')
    if nodes!=list(range(problem.N)) or cells!=list(range(problem.N-1)) or boundary!=1 or interior!=plan['interior_cells']:
        raise ValueError('Partition has omitted, duplicated or reordered original objective row groups')
    _indices(interior,problem.N-1)
    return True


def _expected_ledger(problem,descriptor):
    out=[];e=int(problem.e);d=int(problem.d)
    he=int(problem.work)//4-int(problem.K);hc=2*he-1
    window=np.asarray(problem.window())
    selected=(window!=1.)&(problem.x<problem.trace_ramp_stop);selected[-1]=False
    def add(label,nodes,rows):out.append(dict(label=label,nodes=list(nodes),rows=rows))
    for node in descriptor['node_indices']:
        if selected[node]:
            add('node_G',(node,),e);add('node_high_G',(node,),he)
        add('node_curvature',(node,),None)
    for cell in descriptor['cell_indices']:
        add('cell_C',(cell,cell+1),d);add('cell_high_C',(cell,cell+1),hc)
    if descriptor['include_boundary']:
        add('cut_l',(problem.N-1,),e);add('central_boundary',(0,),d)
        add('cut_nm',(problem.N-1,),d);add('gap',(),1)
    for cell in descriptor['interior_cells']:
        add('interior_retained',(cell,cell+1),2*e)
        add('interior_high',(cell,cell+1),2*he)
        add('interior_curvature',(cell,cell+1),None)
    return out


def _ledger_observer(problem,descriptor):
    expected=_expected_ledger(problem,descriptor);actual=[]
    def record(label,nodes,residual,jacobian):
        k=len(actual)
        if k>=len(expected):raise ValueError('Unexpected extra local row block')
        row=expected[k];count=int(np.asarray(residual).size)
        if label!=row['label'] or list(nodes)!=row['nodes'] or (row['rows'] is not None and count!=row['rows']):
            raise ValueError('Actual local row order/identity/count differs from the exact partition')
        actual.append(dict(label=label,nodes=list(map(int,nodes)),rows=count))
    return actual,expected,record


def _consumer_identity(consumer):
    path=inspect.getsourcefile(consumer)
    if path is None or not inspect.isfunction(consumer) or consumer.__closure__:
        raise TypeError('Use a frozen explicit module function as cell_consumer')
    return dict(module=consumer.__module__,qualified_name=consumer.__qualname__,
                source_sha256=hashlib.sha256(Path(path).read_bytes()).hexdigest())


def _state_binding(vector,weights,consumer,binding):
    opaque=None if binding is None else json.loads(_binding(binding))
    return dict(vector_identity=_array_id(np.asarray(vector,float)),settings=weights,
                cell_consumer=_consumer_identity(consumer),opaque_binding=opaque,
                partition_source_sha256=_source_sha())


def _finish_tile(problem,normal,descriptor,ledger,expected,state_binding,base_info):
    if len(ledger)!=len(expected):raise ValueError('Incomplete local row-group ledger')
    _validate_normal_layout(normal)
    if _mapping_sha(normal.mapping)!=descriptor['mapping_sha256']:
        raise ValueError('Actual eliminated field map differs from the frozen partition')
    groups=Counter()
    for row in ledger:groups[row['label']]+=row['rows']
    if normal.rows!=sum(r['rows'] for r in ledger) or normal.blocks!=len(ledger) or dict(normal.row_groups)!=dict(groups):
        raise ValueError('Normal counters disagree with the actual complete row ledger')
    info=dict(base_info,schema=TILE_SCHEMA,complete_tile=True,full_finite_objective=False,
        tile_descriptor=json.loads(_json(descriptor)),row_ledger=ledger,
        state_binding=state_binding,state_binding_sha256=_digest(state_binding),
        mapping_sha256=descriptor['mapping_sha256'],rows=int(normal.rows),local_blocks=int(normal.blocks),
        row_groups=dict(normal.row_groups),unscaled_normal_storage_bytes=normal.storage_bytes(),
        scaling_or_damping_applied=False,whole_tall_J_stored=False,
        finite_objective_changed_by_partition=False,complete_whole_normal_claimed=False)
    normal.info=info
    return normal,info


def assemble_normal_tile(problem,vector,descriptor,*,curvature_cap=7.2,curvature_weight=1.,
        high_gauss_weight=1.,high_codazzi_weight=1.,interior_gauss_weight=1.,
        block_cells=2,cell_consumer=gauss_cell_positive_trace_frozen_operator_compatible,
        progress=None,binding=None):
    started=time.monotonic();_validate_descriptor(problem,descriptor)
    z=np.asarray(vector,float)
    if z.shape!=(problem.size,) or not np.all(np.isfinite(z)):
        raise ValueError('Wrong/nonfinite original packed field')
    weights=dict(curvature_cap=float(curvature_cap),curvature_weight=float(curvature_weight),
        high_gauss_weight=float(high_gauss_weight),high_codazzi_weight=float(high_codazzi_weight),
        interior_gauss_weight=float(interior_gauss_weight),order=2,block_cells=int(block_cells))
    if block_cells!=int(block_cells) or not 1<=block_cells<=4 or any(not np.isfinite(v) for v in weights.values()):
        raise ValueError('Use bounded original cell assembly and finite settings')
    if any(weights[k]<0 for k in ('curvature_weight','high_gauss_weight','high_codazzi_weight','interior_gauss_weight')):
        raise ValueError('Nonnegative merit weights required')
    state=_state_binding(z,weights,cell_consumer,binding)
    ledger,expected,record=_ledger_observer(problem,descriptor)
    if descriptor['kind']!='interior':
        normal,base=stream_positive_trace_normal(problem,z,
            curvature_cap=curvature_cap,curvature_weight=curvature_weight,
            high_gauss_weight=high_gauss_weight,high_codazzi_weight=high_codazzi_weight,
            order=2,block_cells=block_cells,node_indices=descriptor['node_indices'],
            cell_indices=descriptor['cell_indices'],include_boundary=descriptor['include_boundary'],
            observer=record,progress=progress,cell_consumer=cell_consumer)
    else:
        normal=LocalNormalSystem(problem);observations=[];offset=problem.N*problem.q
        for cell in descriptor['interior_cells']:
            part=interior_gauss_curvature(problem,z,cells=(cell,),gauss_weight=interior_gauss_weight,
                curvature_cap=curvature_cap,curvature_weight=curvature_weight,jacobian=True)
            columns=np.r_[np.arange(cell*problem.q,(cell+2)*problem.q),offset+np.arange(problem.parameter_count)]
            for name in ('retained','high','curvature'):
                normal.add(part[name+'_residual'],part[name+'_jacobian'][:,columns],
                    (cell,cell+1),label='interior_'+name,observer=record)
            observations.append(part['info']);del part
            if progress is not None:progress('interior_cell',cell,normal.rows)
        base=dict(interior_constraints=observations,selected_interior_cells=descriptor['interior_cells'])
    base=dict(base,seconds=time.monotonic()-started)
    return _finish_tile(problem,normal,descriptor,ledger,expected,state,base)


def _check_tile(problem,descriptor,normal,plan):
    _validate_descriptor(problem,descriptor);_validate_normal_layout(normal)
    info=normal.info
    if (info.get('schema')!=TILE_SCHEMA or info.get('complete_tile') is not True
            or _json(info.get('tile_descriptor'))!=_json(descriptor)
            or descriptor['plan_sha256']!=plan['plan_sha256']
            or info.get('scaling_or_damping_applied') is not False):
        raise ValueError('Incomplete/mismatched actual normal tile')
    if (_mapping_sha(normal.mapping)!=plan['mapping_sha256']
            or info.get('mapping_sha256')!=plan['mapping_sha256']):
        raise ValueError('Normal tile uses different exact elimination bytes')
    if _digest(info['state_binding'])!=info['state_binding_sha256']:
        raise ValueError('Normal tile state/source/settings binding was altered')
    if info['state_binding']['partition_source_sha256']!=_source_sha():
        raise ValueError('Normal tile assembler source differs')
    expected=_expected_ledger(problem,descriptor);actual=info['row_ledger']
    if len(actual)!=len(expected):raise ValueError('Incomplete actual tile row ledger')
    totals=Counter()
    for row,want in zip(actual,expected):
        if (row['label']!=want['label'] or row['nodes']!=want['nodes']
                or type(row['rows']) is not int or row['rows']<0
                or (want['rows'] is not None and row['rows']!=want['rows'])):
            raise ValueError('Tile ledger is not its exact assigned row set')
        totals[row['label']]+=row['rows']
    if normal.rows!=sum(totals.values()) or normal.blocks!=len(actual) or dict(normal.row_groups)!=dict(totals):
        raise ValueError('Tile counters/row groups do not match its ledger')
    for a in normal.diagonal+normal.upper+[getattr(normal,k) for k in ARRAYS]:
        if not np.all(np.isfinite(a)):raise FloatingPointError('Nonfinite actual partial normal payload')
    if not np.isfinite(normal.residual_squared) or normal.residual_squared<0:
        raise FloatingPointError('Invalid actual partial residual norm')
    return info


def merge_normal_tiles(problem,tiles_iterator,plan):
    """Consume in plan order; no buffering/sorting of full normal objects."""
    started=time.monotonic();validate_normal_partition(problem,plan)
    total=LocalNormalSystem(problem)
    if _mapping_sha(total.mapping)!=plan['mapping_sha256']:
        raise ValueError('Rebuilt original elimination mapping differs from the plan')
    iterator=iter(tiles_iterator);summaries=[];state_json=None;state=None
    for expected in plan['tiles']:
        try:descriptor,part=next(iterator)
        except StopIteration as exc:raise ValueError('Missing normal tile: '+expected['id']) from exc
        if _json(descriptor)!=_json(expected):
            raise ValueError('Duplicate, out-of-order or wrong normal tile; iterator must follow plan ordinal')
        info=_check_tile(problem,descriptor,part,plan)
        current=_json(info['state_binding'])
        if state_json is None:state_json=current;state=info['state_binding']
        elif current!=state_json:raise ValueError('Partial normals bind different vectors/settings/consumer/opaque inputs')
        for target,value in zip(total.diagonal,part.diagonal):target+=value
        for target,value in zip(total.upper,part.upper):target+=value
        for key in ARRAYS:getattr(total,key)[:]+=getattr(part,key)
        total.residual_squared+=float(part.residual_squared)
        total.rows+=int(part.rows);total.blocks+=int(part.blocks)
        for label,count in part.row_groups.items():total.row_groups[label]=total.row_groups.get(label,0)+int(count)
        summaries.append(dict(id=descriptor['id'],ordinal=descriptor['ordinal'],rows=int(part.rows),
            local_blocks=int(part.blocks),residual_squared=float(part.residual_squared),row_groups=dict(part.row_groups)))
        del info,part,descriptor
    try:
        next(iterator)
    except StopIteration:
        pass
    else:
        raise ValueError('Unexpected extra normal tile after the complete partition')
    info=dict(schema=MERGE_SCHEMA,complete=True,full_finite_objective=True,
        partition_source_sha256=_source_sha(),plan_sha256=plan['plan_sha256'],
        mapping_sha256=plan['mapping_sha256'],state_binding=state,state_binding_sha256=_digest(state),
        consumed_tiles=summaries,rows=int(total.rows),local_blocks=int(total.blocks),
        row_groups=dict(total.row_groups),residual_squared=float(total.residual_squared),
        unscaled_normal_storage_bytes=total.storage_bytes(),seconds=time.monotonic()-started,
        iterator_consumed_in_original_group_order=True,all_planned_rows_covered_exactly_once=True,
        whole_tall_J_stored=False,scaling_or_damping_applied=False,
        complete_normal_created_only_after_all_tiles=True,
        floating_reduction_order_changed=True,floating_bit_identity_claimed=False,
        exact_arithmetic_finite_normal_unchanged=True)
    total.info=info
    return total,info
