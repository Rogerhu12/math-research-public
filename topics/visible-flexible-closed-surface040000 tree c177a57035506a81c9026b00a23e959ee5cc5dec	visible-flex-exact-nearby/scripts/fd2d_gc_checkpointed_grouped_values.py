"""Durable value-only execution of the unchanged complete R165 objective.

The engine is separate from the frozen NumericalContext and trial entry.
Every actual node packet, original two-cell consumer result and interior
packet is atomically saved with exact full-state/source bindings. A retry
reuses only complete matching packets. No Armijo or acceptance decision is
made here, and no partially evaluated residual is returned as complete.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import time

import numpy as np

import fd2d_gc_grouped_search_context as grouped
from fd2d_gc_grouped_search_context import FINITE_RULE,array_identity
from fd2d_gc_grouped_coast_codazzi import gauss_cell_positive_trace_grouped_coast
from fd2d_gc_gauss_cell_codazzi_chunked import gauss_cell_codazzi
from fd2d_gc_positive_trace_stream_normal import radial_view
from fd2d_gc_positive_trace_merit import curvature_merit,high_gauss_merit
from fd2d_gc_positive_trace_interior_merit import interior_gauss_curvature
from fd2d_gc_packet_checkpoint import save_actual_packet,load_actual_packet
from fd2d_gc_archive_arrays import identity

SCHEMA='fd2d-complete-R165-value-block-replay-v1'
HERE=Path(__file__).resolve().parent


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False)


class ActualValueBlockCache:
    """Lossless subpacket transport; complete binding before every reuse."""
    def __init__(self,directory,*,context_binding,vector,source_bindings=None):
        self.directory=Path(directory)
        self.binding=dict(schema=SCHEMA,context_binding=context_binding,
            full_actual_vector=array_identity(vector),engine_source=identity(__file__),
            exact_dependencies=source_bindings or {})
        self.records=[];self.hits=0;self.evaluations=0

    def get(self,kind,descriptor,compute):
        if not kind or any(c not in 'abcdefghijklmnopqrstuvwxyz_0123456789' for c in kind):
            raise ValueError('A plain local phase identifier is required')
        expected=dict(common=self.binding,phase=kind,descriptor=descriptor)
        digest=hashlib.sha256(canonical(expected).encode()).hexdigest()
        directory=self.directory/(kind+'-'+digest)
        manifest=directory/'manifest.json'
        if directory.exists():
            # A directory without its final atomic manifest is not a hit.
            if not manifest.exists():raise ValueError('Unexpected incomplete final packet directory')
            result=load_actual_packet(manifest,expected_binding=expected)
            self.hits+=1;reused=True
        else:
            result=compute()
            manifest=save_actual_packet(result,directory,binding=expected)
            self.evaluations+=1;reused=False
        self.records.append(dict(phase=kind,descriptor=descriptor,manifest=identity(manifest),
                                 reused_complete_packet=reused))
        return result


def _source_bindings():
    names=('fd2d_gc_grouped_search_context.py','fd2d_gc_grouped_coast_codazzi.py',
        'fd2d_gc_gauss_cell_codazzi_chunked.py','fd2d_gc_positive_trace_value_nodes.py',
        'fd2d_gc_positive_trace_stream_normal.py','fd2d_gc_positive_trace_merit.py',
        'fd2d_gc_positive_trace_interior_merit.py','fd2d_gc_packet_checkpoint.py')
    return {name:identity(HERE/name) for name in names}


def checkpointed_value_node_packet(problem,vector,cache):
    """Same node arithmetic, projections and boundary order as the frozen helper."""
    y,p=problem.unpack(vector)
    _,axes=problem.core(p[:problem.K])
    fields=np.empty((problem.work,problem.N,3));gauss=np.empty((problem.work,problem.N))
    active_n=[];active_h=[]
    for j in range(problem.N):
        local=np.r_[y[j],p]
        descriptor=dict(node=j,physical_label=float(problem.x[j]),local_vector=array_identity(local))
        def evaluate():
            view=radial_view(problem,[j])
            _,data=view.evaluate(local)
            return dict(fields=np.array(data['fields'][:,0],copy=True),
                full_gauss=np.array(data['full_gauss'][:,0],copy=True),
                minimum_active_n=data['gauss_l_delta']['sampled_minimum_active_n'],
                minimum_active_h=data['positive_trace_delta']['minimum_active_h'])
        row=cache.get('node',descriptor,evaluate)
        fields[:,j]=row['fields'];gauss[:,j]=row['full_gauss']
        if row['minimum_active_n'] is not None:active_n.append(float(row['minimum_active_n']))
        if row['minimum_active_h'] is not None:active_h.append(float(row['minimum_active_h']))
    problem.profile.set_parameters(p[problem.profile_parameter_slice])
    jet=problem.profile.jet(problem.x)
    selected=np.asarray(problem.retained_actual_gauss_nodes,int)
    projected=(problem.PE@gauss[:,selected]).T
    central=y[0,:problem.d].copy();central[:problem.e]-=problem.core_coefficients@p[:problem.K]
    bottom=np.r_[projected.ravel(),y[-1,problem.d:],central,y[-1,:problem.d],
                 (float(axes['gap'])-problem.gap)/problem.gap]
    data=dict(fields=fields,full_gauss=gauss,projected_gauss=projected,
        axes=axes,parameters=p,physical_profile_parameters=p[problem.profile_parameter_slice].copy(),
        profile_jet=jet,gauss_l_delta=dict(sampled_minimum_active_n=min(active_n) if active_n else None),
        positive_trace_delta=dict(minimum_active_h=min(active_h) if active_h else None),
        affine_node_gauss_rows_removed=np.flatnonzero(problem.window()[:-1]==1).tolist(),
        removed_actual_positive_trace_gauss_nodes=np.flatnonzero(problem.x[:-1]>=problem.trace_ramp_stop).tolist(),
        value_only_node_assembly=dict(one_radial_packet_at_a_time=True,
            whole_parameter_packet_retained=False,full_field_definition_unchanged=True,
            finite_rows_unchanged=True,legacy_trapezoid_diagnostic_not_assembled=True))
    return bottom,data


def checkpointed_grouped_objective(ctx,vector,cache_directory):
    """Return a complete (residual,data) or propagate the actual exception.

    Same existing context/physical definition and finite rule are required.
    Provenance says which engine actually executed. The caller retains the
    original projection, actual search-domain and Armijo procedures.
    """
    v=np.asarray(vector,float)
    if v.shape!=(ctx.problem.size,) or not np.all(np.isfinite(v)):
        raise ValueError('Actual finite vector has wrong shape or nonfinite values')
    if ctx.report.get('finite_radial_scheme')!=FINITE_RULE:
        raise ValueError('This engine evaluates only the explicit R165 complete finite objective')
    began=time.monotonic();ctx.objective_evaluations+=1
    ctx.report['actual_value_objective_evaluations']=ctx.objective_evaluations
    cache=ActualValueBlockCache(cache_directory,context_binding=ctx.binding,vector=v,
                                source_bindings=_source_bindings())
    bottom,data=checkpointed_value_node_packet(ctx.problem,v,cache)
    ctx.event('checkpointed_value_nodes_complete',node_count=ctx.problem.N,
              reused=cache.hits,evaluated=cache.evaluations)
    curvature=curvature_merit(ctx.problem,v,cap=ctx.args.curvature_cap,
        weight=ctx.args.curvature_weight,data=data,jacobian=False)
    high=high_gauss_merit(ctx.problem,v,weight=ctx.args.high_gauss_weight,data=data,jacobian=False)
    grouped_rules=[];block_records=[]
    def consume(block,local,**settings):
        start=int(np.searchsorted(ctx.problem.x,block.x[0]))
        if ctx.problem.x[start]!=block.x[0]:raise ValueError('Cell origin is not an actual saved node')
        if settings.get('jacobian') is not False:raise ValueError('This cache contains actual values only')
        descriptor=dict(node_start=start,node_stop=start+block.N-1,
            local_mesh=array_identity(block.x),local_vector=array_identity(local),settings=settings)
        answer=cache.get('cells',descriptor,
            lambda:gauss_cell_positive_trace_grouped_coast(block,local,**settings))
        info=answer['info'];rows=[]
        for rule in info.get('grouped_coast_rules',[]):
            rows.append(dict(rule,global_cell=start+int(rule['local_cell'])))
        grouped_rules.extend(rows)
        block_records.append(dict(node_start=start,node_stop=start+block.N-1,
            grouped_coast_local_cells=list(info.get('grouped_coast_local_cells',[])),
            grouped_coast_applied=bool(rows),old_G2_point_gauss_kept=True))
        if len(block_records)%8==0:
            ctx.event('checkpointed_value_cell_prefix',block_count=len(block_records),
                      completed_cells=start+block.N-1,reused=cache.hits,evaluated=cache.evaluations)
        return answer
    quadrature=gauss_cell_codazzi(ctx.problem,v,order=2,
        high_weight=ctx.args.high_codazzi_weight,jacobian=False,
        block_cells=ctx.args.block_cells,consumer=consume)
    global_cells=[r['global_cell'] for r in grouped_rules]
    if len(set(global_cells))!=len(global_cells):raise ArithmeticError('Coast cell reported twice')
    e,f=ctx.problem.gauss_l_definition['support']
    expected=np.flatnonzero((ctx.problem.x[:-1]<f)&(ctx.problem.x[1:]>e)).tolist()
    if global_cells!=expected:raise ArithmeticError('Grouped diagnostics omit or duplicate cells')
    first_chunk_info={k:quadrature['info'].get(k) for k in (
        'known_lifting_full_change_maximum','selected_coast_local_cells','known_rule',
        'symmetry','grouped_coast_rules','grouped_coast_local_cells') if k in quadrature['info']}
    quadrature['info'].update(legacy_first_chunk_info=first_chunk_info,
        known_lifting_full_change_maximum=None,known_lifting_change_maximum_not_separately_evaluated=True,
        selected_coast_local_cells_scope='Legacy first chunk only; use whole_grouped_coast_cells',
        whole_grouped_coast_rules=grouped_rules,whole_grouped_coast_cells=global_cells,
        whole_grouped_coast_cell_count=len(global_cells),grouped_block_records=block_records,
        known_lifting_change_not_separately_evaluated=True,whole_known_lifting_change_maximum=None,
        fine_sampled_interior_Gauss_maximum=(max(r['fine_sampled_Gauss_maximum'] for r in grouped_rules)
                                           if grouped_rules else None),
        grouped_rule_diagnostic_scope='All grouped coast cells with global saved-mesh indices',
        nested_symmetry_diagnostic_scope='Original chunk sub-diagnostics may refer to first block only',
        finite_radial_scheme=FINITE_RULE)
    raw=np.r_[quadrature['retained_residual'],bottom]
    interior_settings=dict(cells=ctx.args.interior_cells,gauss_weight=ctx.args.interior_gauss_weight,
        curvature_cap=ctx.args.curvature_cap,curvature_weight=ctx.args.curvature_weight,jacobian=False)
    interior=cache.get('interior',interior_settings,
                      lambda:interior_gauss_curvature(ctx.problem,v,**interior_settings))
    data['previous_node_cell_residual_maximum']=float(np.max(abs(raw)))
    raw=np.r_[raw,interior['retained_residual']]
    residual=np.r_[raw,curvature['residual'],high['residual'],quadrature['high_residual'],
                   interior['high_residual'],interior['curvature_residual']]
    data.update(interior_actual_constraints=interior['info'],original_residual=raw,
        codazzi_cells=quadrature['retained_cells'],curvature_merit=curvature['info'],
        high_gauss_merit=high['info'],
        high_codazzi_merit=dict(quadrature['info'],residual_l2=float(np.linalg.norm(quadrature['high_residual'])),
            sampled_omitted_codazzi_maximum=quadrature['info']['sampled_omitted_average_codazzi_maximum']),
        codazzi_complement_result=dict(omitted_codazzi_cells=quadrature['omitted_codazzi_cells']))
    data['checkpointed_value_execution']=dict(schema=SCHEMA,engine_source=identity(__file__),
        complete=True,full_actual_vector=array_identity(v),original_context_binding=ctx.binding,
        node_packets=ctx.problem.N,cell_packets=len(block_records),interior_packets=1,
        newly_evaluated_packets=cache.evaluations,reused_complete_packets=cache.hits,
        ordered_packets=cache.records,row_order_unchanged=True,
        original_context_objective_called=False,physical_field_and_finite_objective_changed=False)
    ctx.event('checkpointed_actual_grouped_value_evaluation_complete',number=ctx.objective_evaluations,
        evaluation_seconds=time.monotonic()-began,reused=cache.hits,evaluated=cache.evaluations,
        grouped_coast_cells=len(grouped_rules),actual_fine_diagnostic_Gauss=quadrature['info']['fine_sampled_interior_Gauss_maximum'])
    return residual,data
