"""An explicit new finite objective: whole actual coast RHS at split G8.

The saved physical field, boundary projection and variable interpretation are
inherited unchanged.  Only the coast cell residual rule is replaced by the
frozen R165 consumer; this is never labelled the old v25 finite objective.
"""
from pathlib import Path
import time
import json
import numpy as np
import fd2d_gc_staged_search_context as previous
from fd2d_gc_staged_search_context import NumericalContext as PreviousContext, array_identity
from fd2d_gc_grouped_coast_codazzi import gauss_cell_positive_trace_grouped_coast
from fd2d_gc_gauss_cell_codazzi_chunked import gauss_cell_codazzi
from fd2d_gc_positive_trace_value_nodes import value_node_packet
from fd2d_gc_positive_trace_merit import curvature_merit,high_gauss_merit
from fd2d_gc_positive_trace_interior_merit import interior_gauss_curvature
from fd2d_gc_archive_arrays import identity


FINITE_RULE=('R165 coast: exact complete n/m endpoint difference minus window-split Gauss8 '
    'of the whole actual R153 physical PDE at common points; outside coast: frozen original '
    'R152/R153/R155 consumer; node and declared two-point interior Gauss/curvature rows unchanged')


class NumericalContext(PreviousContext):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        here=Path(__file__).resolve().parent
        source=identity(__file__);consumer=identity(here/'fd2d_gc_grouped_coast_codazzi.py')
        self.report['base_context_source']=self.report['source']
        self.report['source']=source
        self.report['providers']['fd2d_gc_grouped_coast_codazzi.py']=consumer
        self.report['finite_radial_scheme']=FINITE_RULE
        self.report['physical_field_and_objective_unchanged_from24']=False
        self.report['physical_field_definition_unchanged_by_cell_rule']=True
        self.report['finite_objective_changed_from25']=True
        self.report['grouped_rule_definition']=dict(schema='fd2d-R165-whole-actual-coast-G8-v1',
            consumer_source=dict(name='fd2d_gc_grouped_coast_codazzi.py',sha256=consumer['sha256'],bytes=consumer['bytes']),
            fine_order=8,point_batch=2,old_point_gauss_diagnostic_order=2,
            support=list(self.problem.gauss_l_definition['support']),
            complete_raw_and_nonlinear_l_terms_evaluated_at_same_points=True,
            known_lifting_change_not_separately_evaluated=True,
            outside_coast_consumer_unchanged=True,finite_rule=FINITE_RULE)
        self.binding=dict(self.binding,schema='fd2d-grouped-actual-coast-value-and-normal-binding-v1',
            context_source_sha256=source['sha256'],base_context_source_sha256=identity(previous.__file__)['sha256'],
            finite_rule=FINITE_RULE,grouped_rule_definition=self.report['grouped_rule_definition'])
        self.binding['implementation_sources']=dict(self.binding['implementation_sources'],
            fd2d_gc_grouped_coast_codazzi_py=consumer['sha256'])

    def objective(self,v,jacobian=False):
        if jacobian:raise ValueError('Use the matching grouped row-partition normal assembler')
        self.objective_evaluations+=1;began=time.monotonic()
        self.report['actual_value_objective_evaluations']=self.objective_evaluations
        bottom,data=value_node_packet(self.problem,v)
        curvature=curvature_merit(self.problem,v,cap=self.args.curvature_cap,
            weight=self.args.curvature_weight,data=data,jacobian=False)
        high=high_gauss_merit(self.problem,v,weight=self.args.high_gauss_weight,data=data,jacobian=False)
        grouped_rules=[];block_records=[]
        def consume(block,local,**settings):
            answer=gauss_cell_positive_trace_grouped_coast(block,local,**settings)
            info=answer['info'];start=int(np.searchsorted(self.problem.x,block.x[0]))
            if self.problem.x[start]!=block.x[0]:raise ValueError('Chunk origin is not an actual saved node')
            rows=[]
            for rule in info.get('grouped_coast_rules',[]):
                rows.append(dict(rule,global_cell=start+int(rule['local_cell'])))
            grouped_rules.extend(rows)
            block_records.append(dict(node_start=start,node_stop=start+block.N-1,
                grouped_coast_local_cells=list(info.get('grouped_coast_local_cells',[])),
                grouped_coast_applied=bool(rows),old_G2_point_gauss_kept=True))
            return answer
        quadrature=gauss_cell_codazzi(self.problem,v,order=2,
            high_weight=self.args.high_codazzi_weight,jacobian=False,
            block_cells=self.args.block_cells,consumer=consume)
        global_cells=[r['global_cell'] for r in grouped_rules]
        if len(set(global_cells))!=len(global_cells):raise ArithmeticError('A coast cell was reported twice')
        e,f=self.problem.gauss_l_definition['support']
        expected=np.flatnonzero((self.problem.x[:-1]<f)&(self.problem.x[1:]>e)).tolist()
        if global_cells!=expected:raise ArithmeticError('Whole grouped-coast diagnostics omit or duplicate a cell')
        first_chunk_info = {k: quadrature['info'].get(k) for k in (
            'known_lifting_full_change_maximum', 'selected_coast_local_cells',
            'known_rule', 'symmetry', 'grouped_coast_rules', 'grouped_coast_local_cells')
            if k in quadrature['info']}
        quadrature['info'].update(legacy_first_chunk_info=first_chunk_info,
            known_lifting_full_change_maximum=None,
            known_lifting_change_maximum_not_separately_evaluated=True,
            selected_coast_local_cells_scope='Legacy first chunk only; use whole_grouped_coast_cells',
            whole_grouped_coast_rules=grouped_rules,
            whole_grouped_coast_cells=global_cells,whole_grouped_coast_cell_count=len(global_cells),
            grouped_block_records=block_records,known_lifting_change_not_separately_evaluated=True,
            whole_known_lifting_change_maximum=None,
            fine_sampled_interior_Gauss_maximum=(max(r['fine_sampled_Gauss_maximum'] for r in grouped_rules)
                                               if grouped_rules else None),
            grouped_rule_diagnostic_scope='All grouped coast cells with global saved-mesh indices',
            nested_symmetry_diagnostic_scope='Original chunk sub-diagnostics may refer to first block only',
            finite_radial_scheme=FINITE_RULE)
        raw=np.r_[quadrature['retained_residual'],bottom]
        interior=interior_gauss_curvature(self.problem,v,cells=self.args.interior_cells,
            gauss_weight=self.args.interior_gauss_weight,curvature_cap=self.args.curvature_cap,
            curvature_weight=self.args.curvature_weight,jacobian=False)
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
        self.event('actual_grouped_value_evaluation_complete',number=self.objective_evaluations,
            evaluation_seconds=time.monotonic()-began,grouped_coast_cells=len(grouped_rules),
            actual_old_G2_diagnostic_Gauss=quadrature['info']['sampled_interior_Gauss_maximum'],
            actual_fine_diagnostic_Gauss=quadrature['info']['fine_sampled_interior_Gauss_maximum'])
        return residual,data

    def diag(self,v,data):
        answer=super().diag(v,data);answer['finite_radial_scheme']=FINITE_RULE
        answer['finite_objective_changed_from25']=True
        return answer

    def checkpoint(self,v,suffix,extra=None):
        additions=dict(finite_radial_scheme=np.array(FINITE_RULE),
            finite_grouped_coast_rule_definition=np.array(json.dumps(self.report['grouped_rule_definition'],sort_keys=True)))
        if extra:additions.update(extra)
        return super().checkpoint(v,suffix,extra=additions)
