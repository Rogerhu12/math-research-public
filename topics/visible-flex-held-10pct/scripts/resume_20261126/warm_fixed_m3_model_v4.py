#!/usr/bin/env python3
"""Versioned fixed-metric warm model with literal original radial chart.

Two accepted data provenances are explicit: a real successful warm BVP, or
a verified same-Cartesian-map reexpression of an actual accepted original
raw return. A reexpression never advertises a newly invoked solver.
"""
import copy
import math
from pathlib import Path
import sys
import numpy as np

HERE=Path(__file__).resolve().parent
SCRIPTS=HERE.parent
sys.path.insert(0,str(HERE))
import warm_fixed_m3_model as original
from warm_fixed_m3_model import sha,load,module,option,bootstrap,embed,lift_weight
from warm_homotopy_core_factory_v4 import BASIS_RULE

KIND='warm-supported-material-phase-fixed-metric-v4'
SCALE_RULE=dict(legacy_power_start=2,legacy_floor=1e-9,
                physical_control='phase_scale_times_p',first='log(q_aux/gauge_q)')
CONTRACT_KEYS=('origin_design_run','origin_design_sha256','frozen_source_signature',
    'frozen_profile','physical_tail_parameters','physical_tail_cut','angular_chart',
    'gauge_q','warp_reference','warm_definition','warm_provider_sha256',
    'warm_geometry_base_sha256','frozen_radial_chart','mean_nodes','bc_normalization',
    'basis_anchor_v3_run','basis_anchor_v3_sha256',
    'basis_anchor_v2_run','basis_anchor_v2_sha256')


def checked_basis_anchor(record):
    definition=record['warm_definition']
    if record.get('homotopy')!=definition.get('homotopy'):
        raise ValueError('The top-level and full mathematical lambda definitions differ')
    if definition.get('phase_basis')!=BASIS_RULE:
        raise ValueError('The declared full-to-complementary homotopy differs from this v4 model')
    path=Path(record['basis_anchor_v3_run']).resolve()
    if (definition.get('basis_anchor_v3_run')!=str(path) or
            definition.get('basis_anchor_v3_sha256')!=record['basis_anchor_v3_sha256'] or
            sha(path)!=record['basis_anchor_v3_sha256']):
        raise ValueError('The accepted zero-control v3 anchor changed')
    validator=module('_warm_v4_actual_v3_anchor',HERE/'warm_fixed_m3_model_v3.py')
    source=validator.accepted_input(path)
    if source['homotopy']!=source['warm_definition']['anchor_core_settings']['homotopy']:
        raise ValueError('A changed-lambda/nonzero-phase v3 solution is not a zero-control R53 anchor')
    with np.load(path.parent/source['raw_return']['file'],allow_pickle=False) as raw:
        if np.any(raw['p']!=0):
            raise ValueError('The v3 anchor has nonzero physical phase controls')
    for key in ('frozen_profile','physical_tail_parameters','physical_tail_cut','angular_chart',
                'gauge_q','warp_reference','frozen_radial_chart','mean_nodes','bc_normalization',
                'origin_design_run','origin_design_sha256',
                'basis_anchor_v2_run','basis_anchor_v2_sha256'):
        if record[key]!=source[key]:
            raise ValueError('The zero-control anchor metric/chart/normalization changed: '+key)
    for key in ('anchor_support_coefficients','anchor_core_settings','anchor_run','anchor_run_sha256',
                'gauge_q','phase_control_scale','phase_parameter_scale_rule',
                'basis_anchor_v2_run','basis_anchor_v2_sha256'):
        if definition[key]!=source['warm_definition'][key]:
            raise ValueError('The complete zero-control R53 anchor changed: '+key)
    return source


def provider_bindings():
    return dict(warm_provider_sha256=sha(HERE/'warm_homotopy_core_factory_v4.py'),
                warm_geometry_base_sha256=sha(HERE/'warm_supported_core_factory.py'),
                warm_model_sha256=sha(HERE/'warm_fixed_m3_model_v4.py'),
                warm_v3_validator_sha256=sha(HERE/'warm_fixed_m3_model_v3.py'),
                warm_v2_validator_sha256=sha(HERE/'warm_fixed_m3_model_v2.py'),
                warm_common_model_sha256=sha(HERE/'warm_fixed_m3_model.py'),
                auxiliary_domain_guard_sha256=sha(HERE/'warm_auxiliary_domain_guard.py'))


def artifact_checks(path,record):
    path=Path(path).resolve()
    raw=path.parent/record['raw_return']['file']
    if sha(raw)!=record['raw_return']['sha256']:
        raise ValueError('The actual raw representation changed')
    physical=path.parent/'physical.npz'
    if sha(physical)!=record['physical_sha256']:
        raise ValueError('The physical C2 representation changed')
    report=path.parent/'relative-metric.json'
    if sha(report)!=record['relative_metric_sha256']:
        raise ValueError('The finite full metric audit changed')
    with np.load(raw,allow_pickle=False) as values, np.load(physical,allow_pickle=False) as phys:
        if not np.array_equal(values['p'],phys['p']):
            raise ValueError('Raw and physical parameter vectors differ')
        if not (values['y'].shape==(3*record['modes']+1,len(values['x'])) and
                values['p'].shape==(record['modes'],)):
            raise ValueError('The actual raw dimensions differ from the model')
        if not all(np.all(np.isfinite(values[key])) for key in
                   ('x','y','p','pscale','rms','cubic_x','cubic_c')):
            raise ValueError('The actual raw field contains nonfinite entries')
        if not all(np.all(np.isfinite(phys[key])) for key in ('x','c','p')):
            raise ValueError('The actual physical C2 field contains nonfinite entries')
        if (not np.all(np.diff(values['x'])>0) or not np.all(np.diff(phys['x'])>0) or
                np.any(values['rms']<0) or
                float(np.max(values['rms']))!=record['raw_return']['rms']):
            raise ValueError('The actual raw mesh/RMS does not match its record')
        if not np.array_equal(values['pscale'],
                              np.maximum(record['gauge_q']**np.arange(2,record['modes']+1),1e-9)):
            raise ValueError('The raw scale array violates the true phase parameter contract')


def accepted_input(path,*,require_lambda_one=False):
    """Validate accepted v4 provenance and finite gates without solving."""
    path=Path(path).resolve()
    record=load(path)
    if record.get('model_kind')!=KIND or not record.get('fixed_metric'):
        raise ValueError('Expected the versioned fixed-metric warm model')
    checked_basis_anchor(record)
    if (record.get('terminal_kind')!='original_linear_dn' or
            record.get('actual_tail_requested') or record.get('original_actual_nonlinear_tail')):
        raise ValueError('This finite linear-DN input check cannot replace an actual nonlinear boundary')
    if record.get('error') or not record.get('finite_linear_candidate_pass'):
        raise ValueError('The warm representation has not passed all actual finite gates')
    if record.get('mean_nodes')!=1168 or record.get('bc_normalization')!=.02:
        raise ValueError('The fixed mean/BC convention changed')
    if require_lambda_one and not (record['homotopy']==1. and
                                   record['warm_definition']['homotopy']==1.):
        raise ValueError('An actual accepted lambda-one field is required')
    if record['warm_definition']['phase_parameter_scale_rule']!=SCALE_RULE:
        raise ValueError('The true parameter/control scale rule changed')
    if record.get('parameter_zero_meaning')!='log(q_aux/gauge_q)':
        raise ValueError('Ambiguous first auxiliary coordinate')
    kind=record.get('acceptance_kind')
    raw=record.get('raw_return',{})
    if kind=='actual_warm_bvp_return':
        if (not record.get('solver_invoked') or not record.get('solver_success') or
                not raw.get('success') or raw.get('status')!=0):
            raise ValueError('A claimed actual warm solve lacks its successful return')
    elif kind=='same_cartesian_map_verified_reexpression':
        source=record.get('source_solver_provenance',{})
        identity=record.get('zero_control_identity',{})
        if (record.get('solver_invoked') is not False or record.get('solver_success') is not None or
                raw.get('success') is not None or not raw.get('accepted_representation') or
                not source.get('solver_success') or not source.get('raw_success') or
                not identity.get('all_required_exact_equalities')):
            raise ValueError('A reexpression must retain honest original solver provenance and real identity checks')
        original_run=Path(source['run'])
        if sha(original_run)!=source['run_sha256']:
            raise ValueError('Original successful solver provenance changed')
        original_record=load(original_run)
        original_raw=original_run.parent/original_record['raw_return']['file']
        if (sha(original_raw)!=source['raw_sha256'] or
                not original_record.get('solver_success') or
                not original_record['raw_return'].get('success')):
            raise ValueError('The bound original raw success changed')
    else:
        raise ValueError('Unknown accepted field provenance')
    gates=record['gates']
    for name,ceiling in (('tol',1e-6),('bc_tol',1e-7),('physical_bc_tol',2e-9)):
        if not math.isfinite(gates[name]) or not 0<gates[name]<=ceiling:
            raise ValueError('An original finite gate was loosened or is invalid')
    for value,limit in ((raw.get('rms',math.inf),gates['tol']),
                        (record.get('original_scaled_bc_max',math.inf),gates['bc_tol']),
                        (record.get('linear_dn_physical_bc_max',math.inf),gates['physical_bc_tol'])):
        if not math.isfinite(value) or value<0 or value>limit:
            raise ValueError('The actual raw RMS or boundary gate failed')
    rows=record.get('metric_diagnostics',[])
    if not rows or any(not math.isfinite(row[key]) or not 0<=row[key]<=1e-6
                       for row in rows for key in
                       ('legacy_max_component_fft_l1','sample_operator_max')):
        raise ValueError('The actual complete finite metric audit failed')
    floor=16*(3*record['modes']+1)
    if (any(row['angular']<floor for row in rows) or
            sorted(row['angular'] for row in rows)!=sorted(record['actual_audit_angular'])):
        raise ValueError('The complete metric audit omitted the original angular floor or changed grids')
    if any(record.get(key)!=value for key,value in provider_bindings().items()):
        raise ValueError('The versioned core source changed')
    artifact_checks(path,record)
    return record


def build_model(design,origin,record,*,anchor_baseline=None):
    definition=record['warm_definition']
    if record.get('model_kind')!=KIND or not record.get('fixed_metric'):
        raise ValueError('This loader does not silently reinterpret a v1 record')
    checked_basis_anchor(record)
    if (definition['anchor_core_settings']!=origin['core_settings'] or
            not np.array_equal(definition['anchor_support_coefficients'],
                               design._core.original.coefficients)):
        raise ValueError('The complete actual anchor changed')
    if definition['phase_parameter_scale_rule']!=SCALE_RULE:
        raise ValueError('The actual warped-BVP parameter scales are not declared')
    if record['frozen_profile']!=origin['frozen_profile']:
        raise ValueError('The original actual intrinsic metric changed')
    if (record['mean_nodes']!=1168 or record['bc_normalization']!=.02 or
            definition['gauge_q']!=record['gauge_q'] or
            origin['gauge_q']!=record['gauge_q'] or
            origin['angular_chart']!=record['angular_chart']):
        raise ValueError('The common gauge, material chart, mean or BC convention changed')
    if (definition['anchor_run_sha256']!=record['origin_design_sha256'] or
            Path(definition['anchor_run']).resolve()!=Path(record['origin_design_run']).resolve()):
        raise ValueError('The anchor identity changed')
    if any(record.get(key)!=value for key,value in provider_bindings().items()):
        raise ValueError('The versioned provider or its geometry implementation changed')
    radial=record['frozen_radial_chart']
    expected=dict(chart_join=float(design.chart_join),
        chart_reference_prefix=float(design.chart_reference_prefix),
        chart_breaks=np.asarray(design.chart_breaks).tolist(),
        meaning='literal original design numerical radial coordinate frozen at the accepted actual delta')
    if radial!=expected:
        raise ValueError('The literal original numerical radial coordinate changed')
    provider=module('_warm_v4_provider',HERE/'warm_homotopy_core_factory_v4.py')
    factory=provider.make_factory(definition,reference_class=type(design._core.original),
                                  anchor_baseline=anchor_baseline)
    __import__('fixed_metric_mode3_core').PlanarSupportCore=factory
    __import__('fixed_metric_mode3_bvp').PlanarSupportCore=factory
    coupler=sys.modules['_metric_coupler']
    Flow,Base=coupler.adaptive.build_classes(record['angular_chart'])
    sys.path.insert(0,str(SCRIPTS/'resume_m3/round_raw_lib'))
    from exact_core_lift import install_core_lift
    import analytic_adaptive_core_jac as analytic
    Base=install_core_lift(Flow,Base)
    analytic.parameter_jets=lambda core,theta:core.jet_parameter_derivatives(theta)
    analytic.install(Base)
    port_path=Path(record['linear_port_path'])
    port=load(port_path)
    if sha(port_path)!=record['linear_port_sha256']:
        raise ValueError('The numerical linear port changed')
    port['cut']['_prefix_bridge']=record['frozen_profile']['prefix_bridge']
    port['_sha256']=sha(port_path)
    if (port['parameters']!=record['physical_tail_parameters'] or
            port['cut']!=record['physical_tail_cut']):
        raise ValueError('The physical tail metric changed')
    obj=Base(copy.deepcopy(record['frozen_profile']),port,float(record['gauge_q']),
             int(record['modes']),int(record['angular']),True,float(record['warp_reference']))
    obj.bcweights=np.full(obj.M,.02)
    obj.chart_join=radial['chart_join']
    obj.chart_reference_prefix=radial['chart_reference_prefix']
    obj.chart_breaks=np.asarray(radial['chart_breaks']).copy()
    expected_scales=np.maximum(obj.q**np.arange(2,obj.M+1),1e-9)
    if not np.array_equal(obj.pscale,expected_scales):
        raise ValueError('The actual inherited BVP scale array differs from the provider contract')
    guard=module('_warm_v4_exp_guard',HERE/'warm_auxiliary_domain_guard.py')
    guard.install(obj)
    obj.relative_metric_loader_record=dict(model_kind=KIND,fixed_metric=True,
        fixed_core=False,parameter_zero_meaning='log(q_aux/gauge_q)',mean_nodes=1168,
        frozen_original_radial_chart=True,bvp_or_tail_solver_invoked=False,complete_surface=False)
    return obj


def load_model(config):
    path=Path(config['source_run']).resolve()
    record=load(path)
    if record.get('model_kind')!=KIND:
        raise ValueError('Use the explicit v4 loader for the v4 phase contract')
    if record.get('terminal_kind')!='original_linear_dn':
        raise ValueError('This model has no nonlinear DN attached')
    origin=Path(record['origin_design_run'])
    if sha(origin)!=record['origin_design_sha256']:
        raise ValueError('The accepted original run changed')
    design,source,signature,_=bootstrap(origin)
    if signature!=record['frozen_source_signature']:
        raise ValueError('The original numerical source changed')
    return build_model(design,source,record)
