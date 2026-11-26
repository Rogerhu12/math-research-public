#!/usr/bin/env python3
"""Geometry contract for refinements of an actual warm nonlinear-DN field.

The accepted input remains an actual nonlinear boundary problem. A small
geometry specification is passed to the declared v2/v3 factory; it carries
no finite-linear acceptance claim and no linear BVP is invoked.
"""
import copy
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
BASE_KIND = 'warm-supported-material-phase-fixed-metric-actual-dn'
KIND = BASE_KIND+'-refinement-v1'
VERSIONS = {
    'warm-supported-material-phase-fixed-metric-v2': 'warm_fixed_m3_model_v2.py',
    'warm-supported-material-phase-fixed-metric-v3': 'warm_fixed_m3_model_v3.py',
}
FROZEN_KEYS = (
    'frozen_profile', 'warm_definition', 'angular_chart', 'gauge_q', 'warp_reference',
    'mean_nodes', 'bc_normalization', 'frozen_radial_chart', 'frozen_source_signature',
    'origin_design_run', 'origin_design_sha256', 'physical_tail_parameters',
    'physical_tail_cut', 'linear_source_run', 'linear_source_run_sha256',
    'linear_source_model_kind', 'linear_source_acceptance_kind',
    'linear_source_solver_invoked', 'source_raw_sha256', 'source_physical_sha256',
)
OPTIONAL_FROZEN_KEYS = ('basis_anchor_v2_run', 'basis_anchor_v2_sha256')
RUNTIME_CONFIG_KEYS = ('traceFile', 'chordMaxCorrections', 'initialCheckpoint')


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def api(repo):
    return module('_actual_refine_original_api', Path(repo)/
        'topics/visible-flex-held-10pct/scripts/resume_20261126/warm_true_dn_solve.py')


def accepted_input(path, *, repo=None):
    path = Path(path).resolve()
    record = json.loads(path.read_text())
    repo = Path(repo if repo is not None else record['repository']).resolve()
    current = repo/'topics/visible-flex-held-10pct/scripts/resume_20261126'
    if record.get('model_kind') == BASE_KIND:
        gate = module('_actual_refine_base_acceptance', current/'warm_actual_dn_acceptance.py')
        return gate.accepted_actual_input(path, repo=repo)
    if record.get('model_kind') == KIND:
        gate = module('_actual_refine_versioned_acceptance', current/'warm_actual_dn_refine_acceptance.py')
        return gate.accepted_actual_input(path, repo=repo)
    raise ValueError('A real accepted original nonlinear-DN field is required')


def provider(repo, record):
    name = VERSIONS.get(record.get('linear_source_model_kind'))
    if name is None:
        raise ValueError('This refinement requires an explicit frozen-radial v2/v3 phase family')
    return module('_actual_refine_geometry_provider', Path(repo)/
        'topics/visible-flex-held-10pct/scripts/resume_20261126'/name)


def geometry_spec(repo, record):
    """Factory parameters only: never an accepted linear source record."""
    model = provider(repo, record)
    value = {key: copy.deepcopy(record[key]) for key in model.CONTRACT_KEYS}
    value.update(model_kind=record['linear_source_model_kind'], fixed_metric=True,
        homotopy=record['warm_definition']['homotopy'], modes=record['modes'],
        angular=record['angular'], linear_port_path=record['linear_port_path'],
        linear_port_sha256=record['linear_port_sha256'])
    for key, expected in model.provider_bindings().items():
        if record.get(key) != expected:
            raise ValueError('The actual finite phase family implementation changed: '+key)
        value[key] = expected
    if value['homotopy'] != 1. or value['mean_nodes'] != 1168:
        raise ValueError('Refinement retains the actual lambda-one finite-mean problem')
    return value


def require_same_problem(repo, left, right):
    for key in FROZEN_KEYS + OPTIONAL_FROZEN_KEYS:
        if left.get(key) != right.get(key):
            raise ValueError('The complete actual nonlinear problem changed: '+key)
    for record in (left, right):
        if (record.get('terminal_kind') != 'original_actual_nonlinear_dn'
                or record.get('parameter_zero_meaning') != 'log(q_aux/gauge_q)'
                or record.get('fixed_metric') is not True
                or record.get('fixed_core') is not False
                or record['warm_definition']['homotopy'] != 1.
                or record['mean_nodes'] != 1168 or record['bc_normalization'] != .02):
            raise ValueError('The original fixed metric, phase, mean or nonlinear terminal changed')
        geometry_spec(repo, record)
    lp = provider(repo, left).provider_bindings()
    rp = provider(repo, right).provider_bindings()
    if lp != rp or any(left.get(key) != right.get(key) for key in lp):
        raise ValueError('The finite family source contract changed')
    return {key: copy.deepcopy(left.get(key)) for key in FROZEN_KEYS+OPTIONAL_FROZEN_KEYS}


def validate_refinement_definition(repo, record, parent):
    require_same_problem(repo, parent, record)
    if (record.get('model_kind') != KIND
            or record.get('fixed_metric_refinement') is not True
            or record.get('fixed_metric_design_continuation') is not False
            or record.get('same_complete_problem_as_source') is not True
            or record.get('boundary_problem_changed') is not False
            or record.get('linear_bvp_invoked') is not False
            or record.get('initializer_is_accepted_solution') is not False
            or record.get('exact_lift_coefficient') != 1):
        raise ValueError('The actual nonlinear refinement provenance is incomplete')
    if (record['modes'] < parent['modes'] or record['angular'] < parent['angular']
            or record['gates']['tol'] >= parent['gates']['tol']
            or any(record['gates'][key] > parent['gates'][key]
                   for key in ('bc_tol', 'physical_bc_tol'))):
        raise ValueError('A refinement cannot truncate modes or loosen a recorded residual gate')
    if record['actual_source_raw_sha256'] != parent['raw_return']['sha256']:
        raise ValueError('The actual input raw identity changed')
    if record['actual_source_physical_sha256'] != parent['physical_sha256']:
        raise ValueError('The actual input physical identity changed')
    original = json.loads(Path(parent['tail_settings']).read_text())
    target = json.loads(Path(record['tail_settings']).read_text())
    skip = set(RUNTIME_CONFIG_KEYS) | {'modes', 'quadrature'}
    if ({k: v for k, v in original.items() if k not in skip} !=
            {k: v for k, v in target.items() if k not in skip}):
        raise ValueError('The original finite-depth/shooting problem changed')
    if (target['modes'] != record['modes'] or target['quadrature'] < original['quadrature']
            or target['quadrature'] <= 4*3*record['modes']
            or target.get('initialCheckpoint') != parent['result']['full_height_record']):
        raise ValueError('The new native resolution or actual complete-state initializer changed')
    base = {k: v for k, v in target.items() if k not in RUNTIME_CONFIG_KEYS}
    implementation = api(repo)
    base_path = Path(record['base_tail_settings'])
    if implementation.sha(base_path) != record['base_tail_settings_sha256'] or implementation.load(base_path) != base:
        raise ValueError('The literal new original port configuration changed')
    port = implementation.load(record['linear_port_path'])
    if (implementation.sha(record['linear_port_path']) != record['linear_port_sha256']
            or port['source']['config_sha256'] != implementation.sha(base_path)
            or port['parameters'] != record['physical_tail_parameters']
            or port['modes'] != [3*j for j in range(1, record['modes']+1)]):
        raise ValueError('The original startup port is not bound to this resolution and metric')
    cut = dict(port['cut'], _prefix_bridge=record['frozen_profile']['prefix_bridge'])
    if cut != record['physical_tail_cut']:
        raise ValueError('The actual original physical cut changed')


def build_models(repo, records):
    """Bootstrap once, then construct each requested honest geometry spec."""
    if not records:
        raise ValueError('No actual geometry supplied')
    model = provider(repo, records[0])
    design, origin, signature, _ = model.bootstrap(records[0]['origin_design_run'])
    result = []
    for record in records:
        if signature != record['frozen_source_signature']:
            raise ValueError('The original complete geometry source changed')
        spec = geometry_spec(repo, record)
        result.append(model.build_model(design, origin, spec))
    return result


def load_model(config):
    path = Path(config['source_run']).resolve()
    provisional = json.loads(path.read_text())
    repo = Path(config.get('repo', provisional['repository'])).resolve()
    record = accepted_input(path, repo=repo)
    obj, = build_models(repo, [record])
    obj.relative_metric_loader_record = dict(model_kind=record['model_kind'],
        fixed_metric=True, fixed_core=False, mean_nodes=1168,
        parameter_zero_meaning='log(q_aux/gauge_q)', source_run=str(path),
        source_run_sha256=api(repo).sha(path), bvp_or_tail_solver_invoked=False,
        actual_terminal_not_replaced_by_linear=True, complete_surface=False)
    return obj


def transfer(repo, source_path, source, target, *, radial_refine=1):
    if not isinstance(radial_refine, int) or radial_refine < 1:
        raise ValueError('Use a positive integral radial subdivision')
    model = provider(repo, source)
    old, new = build_models(repo, [source, target])
    path = Path(source_path).resolve()
    with np.load(path.parent/source['raw_return']['file'], allow_pickle=False) as raw:
        x0, y0, p0, scales = (raw[k].copy() for k in ('x', 'y', 'p', 'pscale'))
    if not np.array_equal(scales, old.pscale) or new.M < old.M:
        raise ValueError('The accepted actual raw scale or mode count changed')
    par = np.zeros(new.M)
    par[:old.M] = p0
    old_initial, new_initial = old.initial(p0).copy(), new.initial(par).copy()
    old_flow, flow = old.flow(p0[0]), new.flow(par[0])
    old_s = old.chart(x0, p0[0])[0]
    if (old_flow.end != flow.end or not np.array_equal(new.chart(x0, par[0])[0], old_s)
            or not np.array_equal(new.pscale[:old.M-1], old.pscale)
            or not np.array_equal(new._core.controls[:old.M], old._core.controls)
            or np.any(new._core.controls[old.M:] != 0)):
        raise ValueError('Mode embedding changed the fixed chart or retained physical phase controls')
    if radial_refine == 1:
        x, old_values = x0.copy(), y0
    else:
        from fixed_metric_mode3_bvp import merge_profile_mesh
        extra = np.concatenate([np.linspace(lo, hi, radial_refine+1)
                                for lo, hi in zip(x0[:-1], x0[1:])])
        x = merge_profile_mesh(np.r_[x0, extra], new.chart_breaks)
        audit = module('_actual_refine_transfer_physical', Path(repo)/
            'topics/visible-flex-held-10pct/scripts/resume_m3/audit_full_relative_metric.py')
        field = audit.load_physical(path.parent/'physical.npz')
        if field.source_sha256 != source['physical_sha256'] or not np.array_equal(field.p, p0):
            raise ValueError('The actual accepted physical field changed')
        old_values = field.sol(new.chart(x, par[0])[0])
        for index, node in enumerate(x0):
            matches = np.flatnonzero(x == node)
            if len(matches) != 1:
                raise ValueError('A radial refinement lost an original accepted raw node')
            old_values[:, matches[0]] = y0[:, index]
    s = new.chart(x, par[0])[0]
    difference = new_initial-model.embed(old_initial, old.M, new.M)
    y = model.embed(old_values, old.M, new.M)+model.lift_weight(flow, s)[None, :]*difference[:, None]
    if not np.all(np.isfinite(y)):
        raise FloatingPointError('The complete original physical lift is nonfinite')
    details = dict(source_modes=old.M, target_modes=new.M, source_nodes=len(x0),
        initial_nodes=len(x), radial_refine=radial_refine,
        preserved_original_raw_nodes=True, original_raw_coordinate_frozen=True,
        complete_phase_controls_zero_extended=True, exact_lift_coefficient=1,
        initial_projection_transfer_max=float(abs(difference).max()),
        initial_parameters=par.tolist(), initial_phase_controls=new._core.controls.tolist(),
        initializer_is_accepted_solution=False)
    return new, x, y, par, details
