"""R170 actual grouped finite field with a larger, exact tail search domain.

The initializer below is the previous staged initializer with only the
factory changed to the genuine DyadicTailRefinedDAE, followed by the same
R165 metadata setup. Actual objective and diagnostics inherit the frozen
R165 methods. This is a new explicit domain, never an old-class alias.
"""
import json,time,datetime,platform,resource,os
from pathlib import Path
from types import SimpleNamespace
import numpy as np
import scipy
import fd2d_gc_staged_search_context as previous
import fd2d_gc_grouped_search_context as grouped
from fd2d_gc_staged_search_context import (DEPENDENCIES,PARENT_SOURCE,
    array_identity,frozen_reference_identity)
from fd2d_gc_grouped_search_context import NumericalContext as GroupedContext,FINITE_RULE
from fd2d_gc_dyadic_tail_problem import create_dyadic_tail_problem,checkpoint_arrays
from fd2d_gc_archive_arrays import identity,load_npz,save_npz
from fd2d_gc_search_domain_roundoff import checked_search_domain
from fd2d_gc_prepared_geometry_cache import install_prepared_geometry_cache
from fd2d_gc_frozen_operator_projections import install_frozen_operator_projection_cache


class NumericalContext(GroupedContext):
    def __init__(self, request, stage_prefix, *, install_caches=True, central_floor=None):
        self.started=time.monotonic();self.stem=Path(stage_prefix)
        self.prepared_handle=self.operator_handle=None
        self.objective_evaluations=0
        self.request=json.loads(Path(request).read_text())
        settings=dict(self.request['settings'])
        settings['out_prefix']=str(self.stem)
        if central_floor is not None:settings['central_floor']=float(central_floor)
        self.args=SimpleNamespace(**settings)
        for key in ('candidate','warm_start','radius_packet','reference_inlet','reference_cache','owner_stop_file'):
            value=getattr(self.args,key)
            if value is not None:setattr(self.args,key,Path(value))
        self.args.out_prefix=self.stem
        here=Path(__file__).resolve().parent
        self.report=dict(schema='fd2d-process-independent-same-finite-context-v1',
            source=identity(__file__),parent_objective_source=identity(here/PARENT_SOURCE),
            providers={name:identity(here/name) for name in DEPENDENCIES},
            request=identity(request),candidate=identity(self.args.candidate),
            warm_input=identity(self.args.warm_start),reference_inlet=identity(self.args.reference_inlet),
            settings={k:str(v) if isinstance(v,Path) else v for k,v in vars(self.args).items()},
            versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
            started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            completed=False,accepted_steps=0,finite_success=False,strong_target_complete=False)
        if self.report['warm_input']['sha256']!=self.request['input_sha256']:
            raise ValueError('The immutable requested input SHA changed')
        self.a=load_npz(self.args.warm_start)
        if int(self.a['modes'])!=self.args.modes:
            raise ValueError('The explicit saved angular layout differs')
        self.args.interior_cells=tuple(json.loads(str(self.a['finite_interior_rows_definition']))['cells'])
        self.report['finite_interior_rows_definition']=json.loads(str(self.a['finite_interior_rows_definition']))
        proof=json.loads(self.args.radius_packet.read_text())
        if not proof['passed'] or proof['candidate_sha256']!=self.report['candidate']['sha256']:
            raise ValueError('Radius proof does not bind this actual candidate')
        witness=dict(**identity(self.args.radius_packet),candidate_sha256=proof['candidate_sha256'])
        self.problem=create_dyadic_tail_problem(self.args.candidate,saved_field=self.a,split_cells=(),
            modes=self.args.modes,max_step=self.args.mesh_step,gap=self.args.gap,
            reference_inlet=self.args.reference_inlet,reference_cache=self.args.reference_cache,
            reference_rim_fraction=self.args.reference_rim_fraction,minimum_active_n=self.args.minimum_active_n,
            mesh_relative_tolerance=self.args.mesh_relative_tolerance,
            base_lower_bound='4/5',base_lower_provenance=witness,radius_floor=self.args.radius_floor)
        problem=self.problem
        if str(self.a['candidate_sha256'])!=self.report['candidate']['sha256'] or str(self.a['profile_kind'])!='physical_bumps':
            raise ValueError('Wrong physical initializer identity')
        if not np.array_equal(self.a['mesh'],problem.x) or not np.array_equal(self.a['profile_supports'],problem.profile.supports):
            raise ValueError('Restore the declared saved mesh and supports exactly')
        if self.a['corrections'].shape!=(problem.N,problem.q) or len(self.a['parameters'])!=problem.parameter_count:
            raise ValueError('Explicit field dimensions differ')
        for key,expected in (('seed_weight_definition',problem.seed_weight_definition),
                ('angular_atlas_definition',problem.angular_atlas_definition),
                ('coast_reference_definition',problem.coast_reference_definition),
                ('reference_evaluation_definition',problem.reference_evaluation_definition),
                ('gauss_l_definition',problem.gauss_l_definition),
                ('positive_trace_definition',problem.positive_trace_definition)):
            if key not in self.a or frozen_reference_identity(json.loads(str(self.a[key])))!=frozen_reference_identity(expected):
                raise ValueError('Saved actual field definition differs: '+key)
        old=np.r_[self.a['corrections'].ravel(),self.a['parameters']]
        self.vector=self.project(old)
        self.report['initial_projection_change']=float(np.max(abs(self.vector-old)))
        self.report['parameter_layout']=problem.parameter_layout()
        self.report['finite_radial_scheme']='Original R152 split G8 affine coast lifting + original R153/R155 complete nonlinear G2; original actual n/m endpoint differences'
        self.report['physical_field_and_objective_unchanged_from24']=True
        self.report['interior_cells']=list(self.args.interior_cells)
        self.report['source_finite_input']=dict(mesh=array_identity(problem.x),vector=array_identity(self.vector))
        permitted,domain=checked_search_domain(problem,self.vector,self.args.central_cap,self.args.central_floor)
        self.report['initial_domain']=domain
        if not permitted:raise ValueError('Requested initial state is outside the declared search domain')
        mathematical_settings={key:getattr(self.args,key) for key in (
            'gap','modes','curvature_cap','curvature_weight','high_gauss_weight','high_codazzi_weight',
            'minimum_active_n','interior_gauss_weight','reference_rim_fraction','radius_floor')}
        mathematical_settings['interior_cells']=list(self.args.interior_cells)
        self.binding=dict(schema='fd2d-same-state-finite-value-and-normal-binding-v1',
            input_npz_sha256=self.report['warm_input']['sha256'],input_npz_bytes=self.report['warm_input']['bytes'],
            packed_vector=array_identity(self.vector),candidate_sha256=self.report['candidate']['sha256'],
            reference_inlet_sha256=self.report['reference_inlet']['sha256'],
            mathematical_settings=mathematical_settings,
            actual_saved_definition_arrays={k:array_identity(v) for k,v in self.a.items()
                if k not in ('corrections','parameters','full_gauss_nodes','codazzi_cells','omitted_codazzi_cells')},
            implementation_sources={name:r['sha256'] for name,r in self.report['providers'].items()},
            context_source_sha256=self.report['source']['sha256'],
            parent_objective_source_sha256=self.report['parent_objective_source']['sha256'],
            finite_rule=self.report['finite_radial_scheme'],damping_and_search_floor_not_part_of_normal_identity=True)
        if install_caches:
            self.prepared_handle=install_prepared_geometry_cache(problem,byte_limit=self.args.prepared_cache_mib*1024*1024)
            self.operator_handle=install_frozen_operator_projection_cache(problem,byte_limit=self.args.operator_cache_mib*1024*1024)
            self.report['prepared_geometry_cache_definition']=self.prepared_handle.definition()
            self.report['frozen_operator_cache_binding']=self.operator_handle.binding
        self.report['cache_instances_are_process_local']=True
        here=Path(__file__).resolve().parent
        source=identity(__file__);consumer=identity(here/'fd2d_gc_grouped_coast_codazzi.py')
        self.report['base_context_source']=identity(previous.__file__)
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
        domain=self.problem.tail_search_domain_definition
        self.report.update(tail_search_domain_definition=domain,
            global_tail_coefficient_box_required=False,
            actual_finite_functions_changed_by_domain=False,
            original_grouped_objective_source=identity(grouped.__file__))
        self.binding=dict(self.binding,schema='fd2d-R170-grouped-same-field-new-tail-domain-v1',
            original_grouped_context_source_sha256=identity(grouped.__file__)['sha256'],
            tail_search_domain_definition=domain,
            domain_provider_source_sha256=identity(here/'fd2d_gc_dyadic_tail_problem.py')['sha256'],
            finite_objective_unchanged_by_selected_domain=True)

    def project(self,v):
        z=np.array(v,float,copy=True);_,p=self.problem.unpack(z)
        tail=p[self.problem.tail_parameter_slice]
        certificate=self.problem.tail_control_box.certificate(tail)
        repair=None
        if not certificate['passed']:
            repaired=self.problem.tail_control_box.repair_toward_constant(tail)
            p[self.problem.tail_parameter_slice]=repaired['controls']
            repair=repaired['info']
            certificate=repair['output_certificate']
        before_profile=p[self.problem.profile_parameter_slice].copy()
        p[self.problem.profile_parameter_slice]=np.clip(before_profile,
            -self.args.profile_box,self.args.profile_box)
        answer=self.problem.impose_linear_boundary_values(z)
        self.last_projection_information=dict(
            new_domain='R170 eight dyadic Bernstein boxes',
            global_control_clipping_applied=False,
            exact_tail_certificate=certificate,explicit_tail_repair=repair,
            profile_clip_maximum_change=float(np.max(abs(before_profile-p[self.problem.profile_parameter_slice]))),
            maximum_full_vector_change=float(np.max(abs(answer-np.asarray(v,float)))))
        return answer

    def domain_diagnostics(self,v):
        answer=super().domain_diagnostics(v)
        _,p=self.problem.unpack(v)
        answer['tail_global_range_is_not_the_search_box']=True
        answer['exact_dyadic_tail_certificate']=self.problem.tail_control_box.certificate(
            p[self.problem.tail_parameter_slice])
        return answer

    def checkpoint(self,v,suffix,extra=None):
        arrays=checkpoint_arrays(self.problem,v,self.report['candidate']['sha256'],
            refinement_definition=self.problem.radial_refinement_definition)
        for key in ('radial_refinement_definition','angular_embedding_definition','parent_finite_interior_rows_definition'):
            if key in self.a:arrays[key]=np.array(self.a[key],copy=True)
        arrays['finite_radial_scheme']=np.array(FINITE_RULE)
        arrays['finite_interior_rows_definition']=np.array(json.dumps(self.report['finite_interior_rows_definition'],sort_keys=True))
        arrays['finite_grouped_coast_rule_definition']=np.array(json.dumps(self.report['grouped_rule_definition'],sort_keys=True))
        if extra:arrays.update(extra)
        return save_npz(self.stem.with_name(self.stem.name+suffix),**arrays)
