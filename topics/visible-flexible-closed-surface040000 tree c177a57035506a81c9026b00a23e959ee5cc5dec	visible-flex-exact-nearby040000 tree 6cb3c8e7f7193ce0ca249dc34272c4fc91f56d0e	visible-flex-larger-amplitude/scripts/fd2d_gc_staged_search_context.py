"""Frozen finite v24 objective in a process-independent numerical context.

The objective, diagnostics, boundary projection and field checkpoint methods
below are AST copies of the actual v24 driver, with only closure variables
replaced by explicit context attributes. No finite equation is changed.
This context enables durable value/normal/direction/trial stages.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import os
import argparse, json, time, resource, traceback, datetime, platform, gc
from pathlib import Path
import numpy as np
import scipy
from scipy import sparse
from fd2d_gc_midpoint_refined_positive_trace_v3 import create_midpoint_refined_problem, checkpoint_arrays
from fd2d_gc_search_domain_roundoff import checked_search_domain
from fd2d_gc_positive_trace_value_nodes import value_node_packet
from fd2d_gc_gauss_cell_codazzi_chunked import gauss_cell_codazzi
from fd2d_gc_gauss_cell_frozen_operator_compatible import gauss_cell_positive_trace_frozen_operator_compatible as gauss_cell_positive_trace
from fd2d_gc_prepared_geometry_cache import install_prepared_geometry_cache
from fd2d_gc_frozen_operator_projections import install_frozen_operator_projection_cache
from fd2d_gc_positive_trace_merit import curvature_merit, high_gauss_merit
from fd2d_gc_positive_trace_interior_merit import interior_gauss_curvature
from fd2d_gc_codazzi_complement import codazzi_complement
from fd2d_gc_bump_residual_locations import residual_locations
from fd2d_gc_local_normal_system import bounded_normal_direction
from fd2d_gc_positive_trace_interior_stream_normal_consumer import stream_positive_trace_interior_normal
from fd2d_gc_archive_arrays import identity, load_npz, save_npz
import hashlib
from types import SimpleNamespace

def frozen_reference_identity(definition):
    """Compare frozen functions independently of path and operational cache counts.

    The reference binding SHA already covers exact input/source content and
    numeric precision. All remaining mathematical window/lifting fields are
    compared. Full unmodified metadata is retained in every checkpoint.
    """

    def clean(value):
        if isinstance(value, dict):
            identity_record = 'sha256' in value and 'bytes' in value
            return {k: clean(v) for k, v in value.items() if k != 'cache_statistics' and (not (identity_record and k == 'path'))}
        if isinstance(value, list):
            return [clean(v) for v in value]
        return value
    return clean(definition)

PARENT_SOURCE='fd2d-gc-raw-bump-refined-angular-prepared-cache-damping-run.py'
DEPENDENCIES=('fd2d_gc_prepared_geometry_cache.py', 'fd2d_gc_frozen_operator_projections.py', 'fd2d_gc_gauss_cell_frozen_operator_compatible.py', 'fd2d_gc_positive_trace_stream_normal_consumer.py', 'fd2d_gc_positive_trace_interior_stream_normal_consumer.py', 'fd2d-gc-raw-bump-refined-angular-prepared-cache-run.py', 'fd2d_gc_positive_trace_value_nodes.py', 'fd2d_gc_midpoint_refined_positive_trace_v3.py', 'fd2d_gc_midpoint_refined_positive_trace.py', 'fd2d_gc_nested_angular_positive_trace.py', 'fd2d_gc_search_domain_roundoff.py', 'fd2d_gc_positive_trace_interior_stream_normal.py', 'fd2d_gc_positive_trace_stream_normal.py', 'fd2d_gc_local_normal_system.py', 'fd2d_gc_positive_trace_interior_merit.py', 'fd2d_gc_raw_bump_positive_trace.py', 'fd2d_gc_positive_trace_branch.py', 'fd2d_gc_gauss_cell_positive_trace.py', 'fd2d_gc_positive_trace_merit.py', 'fd2d_gc_positive_trace_bounded_schur.py', 'fd2d_gc_positive_gauss_coast_hybrid.py', 'fd2d_gc_positive_gauss_hybrid.py', 'fd2d_gc_hybrid_lifting_codazzi_d2.py', 'fd2d_gc_raw_bump_positive_gauss.py', 'fd2d_gc_positive_gauss_l.py', 'fd2d_gc_gauss_cell_positive_gauss.py', 'fd2d_gc_positive_gauss_merit.py', 'fd2d_gc_positive_gauss_bounded_schur.py', 'fd2d_gc_frozen_ruling_atlas.py', 'fd2d_gc_raw_bump_ruling_atlas.py', 'fd2d_gc_gauss_cell_codazzi_endpoint_d2.py', 'fd2d_gc_raw_bump_coast_reference.py', 'fd2d_gc_frozen_coast_reference.py', 'fd2d_k0_native_gc.py', 'fd2d_gc_raw_bump_turn_mesh.py', 'fd2d_gc_gauss_cell_codazzi.py', 'fd2d_gc_gauss_cell_codazzi_chunked.py', 'fd2d_gc_gauss_cell_codazzi_d2.py', 'fd2d_gc_d2_complements.py', 'fd2d_gc_raw_bump_cylinder.py', 'fd2d_gc_bump_cylinder_bounded_schur_v2.py', 'fd2d_gc_raw_bump_clean.py', 'fd2d_gc_raw_bump_dae.py', 'fd2d_gc_codazzi_complement.py', 'fd2d_gc_bump_residual_locations.py', 'fd2d_gc_radial_bump_profile.py', 'fd2d_gc_bump_bounded_schur.py', 'fd2d_gc_bump_merit.py', 'fd2d_gc_curvature_penalty.py', 'fd2d_gc_packet_checkpoint.py', 'fd2d_gc_normal_checkpoint.py')


def array_identity(value):
    value=np.asarray(value)
    return dict(shape=list(value.shape),dtype=value.dtype.str,
        sha256=hashlib.sha256(np.ascontiguousarray(value).tobytes()).hexdigest())


class NumericalContext:
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
        self.problem=create_midpoint_refined_problem(self.args.candidate,saved_field=self.a,split_cells=(),
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

    def save_report(self, **updates):
        self.report.update(updates)
        self.report['seconds']=time.monotonic()-self.started
        self.report['peak_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if self.prepared_handle is not None:self.report['prepared_geometry_cache_statistics']=self.prepared_handle.statistics()
        if self.operator_handle is not None:self.report['frozen_operator_cache_statistics']=self.operator_handle.statistics()
        target=self.stem.with_name(self.stem.name+'-report.json')
        target.parent.mkdir(parents=True,exist_ok=True)
        temporary=target.with_suffix('.json.writing')
        temporary.write_text(json.dumps(self.report,indent=2,allow_nan=False)+'\n')
        os.replace(temporary,target)
        return target

    def event(self, kind, **values):
        row=dict(event=kind,seconds=time.monotonic()-self.started,**values)
        target=self.stem.with_name(self.stem.name+'-progress.jsonl')
        target.parent.mkdir(parents=True,exist_ok=True)
        with target.open('a') as out:out.write(json.dumps(row,allow_nan=False)+'\n')
        print(json.dumps(row,allow_nan=False),flush=True)


    def project(self, v):
        z = np.array(v, float, copy=True)
        _, p = self.problem.unpack(z)
        p[self.problem.tail_parameter_slice] = np.clip(p[self.problem.tail_parameter_slice], 0.0, 1.2)
        p[self.problem.profile_parameter_slice] = np.clip(p[self.problem.profile_parameter_slice], -self.args.profile_box, self.args.profile_box)
        return self.problem.impose_linear_boundary_values(z)

    def domain_diagnostics(self, v):
        _, pp = self.problem.unpack(v)
        nc = self.problem.seed + self.problem.core_basis @ pp[:self.problem.K]
        ts = pp[self.problem.tail_parameter_slice]
        delta = pp[self.problem.profile_parameter_slice]
        margin = self.problem.profile_domain['matrix'] @ delta - self.problem.profile_domain['lower']
        bound = 8 * np.finfo(float).eps * (float(np.max(abs(self.problem.seed))) + float(np.max(abs(self.problem.core_basis) @ abs(pp[:self.problem.K]))))
        return dict(minimum_central=float(nc.min()), maximum_central=float(nc.max()), central_floor_difference=float(nc.min() - self.args.central_floor), central_cap_difference=float(self.args.central_cap - nc.max()), illustrative_floating_sum_error_scale=bound, tail_minimum=float(ts.min()), tail_maximum=float(ts.max()), profile_linear_minimum_margin=float(margin.min()))

    def objective(self, v, jacobian=False):
        self.objective_evaluations += 1
        objective_start = time.monotonic()
        self.report['actual_value_objective_evaluations'] = self.objective_evaluations
        if jacobian:
            raise ValueError('Use the actual streamed normal assembler; this objective is value-only')
        bottom, data = value_node_packet(self.problem, v)
        curv = curvature_merit(self.problem, v, cap=self.args.curvature_cap, weight=self.args.curvature_weight, data=data, jacobian=False)
        high = high_gauss_merit(self.problem, v, weight=self.args.high_gauss_weight, data=data, jacobian=False)
        known_block_diagnostics = []

        def actual_cell_consumer(block, local, **settings):
            answer = gauss_cell_positive_trace(block, local, **settings)
            known_block_diagnostics.append(dict(endpoints=[float(block.x[0]), float(block.x[-1])], maximum=answer['info']['known_lifting_full_change_maximum'], selected_cells=len(answer['info']['selected_coast_local_cells'])))
            return answer
        quadrature = gauss_cell_codazzi(self.problem, v, order=2, high_weight=self.args.high_codazzi_weight, jacobian=False, block_cells=self.args.block_cells, consumer=actual_cell_consumer)
        quadrature['info']['whole_known_lifting_change_maximum'] = max((q['maximum'] for q in known_block_diagnostics))
        quadrature['info']['whole_fine_known_cell_count'] = sum((q['selected_cells'] for q in known_block_diagnostics))
        quadrature['info']['known_rule_diagnostic_scope'] = 'Fine physical support is global; nested cell rules and symmetry are first block only. Whole maxima/count explicitly aggregated.'
        quadrature['info']['nested_symmetry_diagnostic_scope'] = 'First block; full point maxima and matrices aggregated over all blocks'
        raw = np.r_[quadrature['retained_residual'], bottom]
        interior = interior_gauss_curvature(self.problem, v, cells=self.args.interior_cells, gauss_weight=self.args.interior_gauss_weight, curvature_cap=self.args.curvature_cap, curvature_weight=self.args.curvature_weight, jacobian=False)
        data['previous_node_cell_residual_maximum'] = float(np.max(abs(raw)))
        raw = np.r_[raw, interior['retained_residual']]
        residual = np.r_[raw, curv['residual'], high['residual'], quadrature['high_residual'], interior['high_residual'], interior['curvature_residual']]
        data['interior_actual_constraints'] = interior['info']
        data['original_residual'] = raw
        data['codazzi_cells'] = quadrature['retained_cells']
        data['curvature_merit'] = curv['info']
        data['high_gauss_merit'] = high['info']
        data['high_codazzi_merit'] = dict(quadrature['info'], residual_l2=float(np.linalg.norm(quadrature['high_residual'])), sampled_omitted_codazzi_maximum=quadrature['info']['sampled_omitted_average_codazzi_maximum'])
        data['codazzi_complement_result'] = {'omitted_codazzi_cells': quadrature['omitted_codazzi_cells']}
        self.event('actual_value_evaluation_complete', number=self.objective_evaluations, evaluation_seconds=time.monotonic() - objective_start, prepared_geometry_cache=self.prepared_handle.statistics(), frozen_operator_cache=self.operator_handle.statistics())
        return (residual, data)

    def diag(self, v, data):
        raw = data['original_residual']
        fields = data['fields']
        p = data['parameters']
        n, m, l = (fields[:, :, i] for i in range(3))
        disc = np.hypot(l - n, 2 * m)
        axes = data['axes']
        d = dict(residual_maximum=float(np.max(abs(raw))), previous_node_cell_residual_maximum=data['previous_node_cell_residual_maximum'], interior_actual_constraints=data['interior_actual_constraints'], residual_rms=float(np.linalg.norm(raw) / np.sqrt(len(raw))), legacy_trapezoid_residual_maximum=None, legacy_trapezoid_not_evaluated=True, full_gauss_node_maximum=float(np.max(abs(data['full_gauss']))), formal_curvature_node_maximum=float(np.max(np.maximum(abs(l + n + disc), abs(l + n - disc))) / 2), A=float(axes['A']), B=float(axes['B']), gap=float(axes['gap']), base_coast_T_fixed=self.problem.base_reference_T, tail_coefficients=p[self.problem.tail_parameter_slice].tolist(), profile_deltas=p[self.problem.profile_parameter_slice].tolist(), minimum_n=float(n.min()), maximum_n=float(n.max()), minimum_active_coast_n_at_nodes=data['gauss_l_delta']['sampled_minimum_active_n'], gauss_l_field=True, continuous_positive_domain_certified=False, removed_actual_zero_Gauss_nodes=data['affine_node_gauss_rows_removed'], removed_terminal_positive_trace_Gauss_nodes=data['removed_actual_positive_trace_gauss_nodes'], minimum_sampled_positive_trace_h=data['positive_trace_delta']['minimum_active_h'], minimum_central_curvature=float((self.problem.seed + self.problem.core_basis @ p[:self.problem.K]).min()), minimum_radius_at_nodes=float(data['profile_jet']['a'].min()), exact_cut_lifting=True, cut_n_mean_omitted=False, cut_correction_maximum=float(np.max(abs(self.problem.unpack(v)[0][-1]))), nonlinear_finite_solution=False, continuous_certificate=False, finite_radial_scheme='R153 nonlinear Gauss2 plus declared R152 fine original affine coast lifting', curvature_merit=data['curvature_merit'], high_gauss_merit=data['high_gauss_merit'], high_codazzi_merit=data['high_codazzi_merit'])
        return d

    def checkpoint(self, v, suffix, extra=None):
        arrays = checkpoint_arrays(self.problem, v, self.report['candidate']['sha256'], refinement_definition=self.problem.radial_refinement_definition)
        for key in ('radial_refinement_definition', 'angular_embedding_definition', 'parent_finite_interior_rows_definition'):
            if key in self.a:
                arrays[key] = np.array(self.a[key], copy=True)
        arrays['finite_radial_scheme'] = np.array('R153 nonlinear Gauss2 + split Gauss8 affine known coast + R155 exact nonlinear n endpoints and complete terminal angular-drift Gauss2')
        arrays['finite_interior_rows_definition'] = np.array(json.dumps(self.report['finite_interior_rows_definition'], sort_keys=True))
        if extra:
            arrays.update(extra)
        return save_npz(self.stem.with_name(self.stem.name + suffix), **arrays)
