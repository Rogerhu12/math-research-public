#!/usr/bin/env python3
"""One fixed complete metric inside the original R53 actual-DN family.

The first anchor must be a genuine accepted lambda-one complete-prefix-QR chord return. Its
actual delta, full profile, literal radial chart, angular chart, gauge,
warp-reference and finite mean rule are frozen. The original support core,
complete exact lift and fixed=True constructor are retained. Parameter zero
becomes log(q_actual/q_seed); no phase-family model or linear solve is used.
Accepted-source records are never rewritten or relabelled by this module.
"""
import copy
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np
from scipy.interpolate import PPoly

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
KIND = 'original_r53_literal_fixed_metric_qr_anchor_actual_dn_v1'
PARAMETER_ZERO = 'log(q_actual/q_seed)'
RUNTIME_CONFIG_KEYS = ('traceFile', 'chordMaxCorrections', 'initialCheckpoint')
ANCHOR_SOURCE_KIND = 'actual_lambda_one_qr_chord_final_physical_height'
REVIEWED_NUMERICAL_SOURCES = {'chord_fixed_support_actual_model.py': '5f5fde082660b02f164a0b8932bed09ca6fa9ecb212d4928768fc8210d8d82a0', 'chord_fixed_support_actual_step.py': 'a4b21f9fb08c1756b274ceeaa2c89b877ecebfa3bcd64627ebd7940cb5025359', 'chord_fixed_support_actual_acceptance.py': '23501290001a0a01f5aefc0a32772a0a357f87cb86e27f8b1143fd2592e7c93f', 'chord_fixed_support_actual_resources.py': 'c19093a00ddff270337dff47cfcd2c5c1ed426eed79d65eb083dfbc66651db15', 'run_chord_fixed_support_actual_once.py': '23b7ded6ad7791cb032ab0363c4b2e4bceb2be8beb3670cfc4c59289ef641374'}


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1048576), b''):
            digest.update(chunk)
    return digest.hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def checked(reference):
    path = Path(reference['path']).resolve()
    if sha(path) != reference['sha256']:
        raise ValueError('A bound complete source changed: '+str(path))
    return path


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def option(record, flag):
    command = record['command']
    if command.count(flag) != 1:
        raise ValueError('Require one original argument '+flag)
    return command[command.index(flag)+1]


def finite(value, upper):
    return (isinstance(value, (int, float)) and not isinstance(value, bool)
            and math.isfinite(value) and 0 <= value <= upper)


def reviewed_source_paths():
    paths = []
    for name, expected in REVIEWED_NUMERICAL_SOURCES.items():
        path = HERE/name
        if sha(path) != expected:
            raise ValueError('The reviewed fixed-support numerical source changed: '+name)
        paths.append(path)
    return paths


def original_gate(origin_repo):
    """Load the old frozen tree's gate, never reinterpret its absolute paths."""
    origin_repo = Path(origin_repo).resolve()
    path = origin_repo/'topics/visible-flex-held-10pct/scripts/resume_20261128/tail/qr_actual_coupled_prefix.py'
    if sha(path) != sha(HERE.parent/'tail/qr_actual_coupled_prefix.py'):
        raise ValueError('The explicitly selected original-tree complete-prefix-QR gate needs a separate review')
    gate = module('_qr_fixed_support_actual_anchor_gate', path)
    if Path(gate.SCRIPTS).resolve() != origin_repo/'topics/visible-flex-held-10pct/scripts':
        raise ValueError('The original-tree gate imported geometry from another source tree; use a fresh process')
    return gate, path


def accepted_input(path, *, repo, origin_repo=None, coupling_summary=None, seen=None):
    """An explicit view of an unchanged genuine anchor or own actual return."""
    reviewed_source_paths()
    path, repo = Path(path).resolve(), Path(repo).resolve()
    record = load(path)
    seen = set() if seen is None else set(seen)
    if str(path) in seen:
        raise ValueError('Cyclic actual-refinement predecessor chain')
    seen.add(str(path))
    if record.get('model_kind') == KIND:
        if coupling_summary is not None:
            raise ValueError('An own fixed-metric return has its bound anchor; do not supply another coupling summary')
        gate = module('_qr_fixed_support_actual_return_gate', HERE/'qr_fixed_support_actual_acceptance.py')
        record = gate.accepted_actual_input(path, repo=repo, seen=seen)
        return dict(role='accepted_original_support_qr_anchor_fixed_metric_actual_return', path=str(path),
            record=record, raw=ref(path.parent/record['raw_return']['file']),
            physical=ref(path.parent/'physical.npz'),
            final_packet=ref(record['result']['full_height_record']),
            final_height_binding=ref(record['result']['height_reference']),
            tail_settings=ref(record['tail_settings']),
            base_tail_settings=ref(record['base_tail_settings']),
            port=ref(record['linear_port_path']), mean_nodes=record['mean_nodes'],
            original_repository=record['fixed_problem']['original_repository'],
            gates=copy.deepcopy(record['gates']))
    if record.get('model_kind') is not None or origin_repo is None or coupling_summary is None:
        raise ValueError('The first source requires explicit old frozen --origin-repo and actual --coupling-summary')
    gate, gate_path = original_gate(origin_repo)
    accepted, physical, binding, provenance = gate.accepted_coupled(path, coupling_summary)
    if provenance.get('source_kind') != ANCHOR_SOURCE_KIND:
        raise ValueError('The actual anchor must retain its independent complete-prefix-QR provenance')
    del physical
    summary = load(coupling_summary)
    physical_path = path.parent/'physical.npz'
    # In particular this hash comes from the currently checked actual file,
    # not an assumed optional physical_sha256 field in the portable record.
    return dict(role='accepted_original_support_qr_chord_design_actual_return', path=str(path),
        record=accepted, raw=ref(path.parent/accepted['raw_return']['file']),
        physical=ref(physical_path), final_packet=copy.deepcopy(binding['packet']),
        final_height_binding=copy.deepcopy(summary['result']['full_height_binding']),
        tail_settings=copy.deepcopy(summary['tail_configuration']['runtime']),
        base_tail_settings=copy.deepcopy(summary['tail_configuration']['baseline']),
        port=copy.deepcopy(summary['input']['port']),
        mean_nodes=binding['source_mean_nodes'], original_repository=str(Path(origin_repo).resolve()),
        coupling_summary=ref(coupling_summary), anchor_gate=ref(gate_path),
        complete_anchor_gate_provenance=provenance, gates=copy.deepcopy(accepted['gates']))


def chart_record(obj):
    return dict(chart_join=float(obj.chart_join),
        chart_reference_prefix=float(obj.chart_reference_prefix),
        chart_breaks=np.asarray(obj.chart_breaks).tolist())


def restore_chart(obj, chart):
    if (not 0 < chart['chart_join'] < 1 or chart['chart_reference_prefix'] <= 0
            or not np.all(np.isfinite(chart['chart_breaks']))):
        raise ValueError('Invalid actual literal radial chart')
    obj.chart_join = float(chart['chart_join'])
    obj.chart_reference_prefix = float(chart['chart_reference_prefix'])
    obj.chart_breaks = np.asarray(chart['chart_breaks'], dtype=float)


def raw_arrays(context):
    with np.load(checked(context['raw']), allow_pickle=False) as data:
        return {key:data[key].copy() for key in
                ('x', 'y', 'p', 'pscale', 'cubic_x', 'cubic_c', 'rms')}


def bootstrap(context):
    """Install the real original source classes once in this fresh process."""
    source = context['record']
    if context['role'] == 'accepted_original_support_qr_chord_design_actual_return':
        anchor_path = Path(context['path'])
    else:
        anchor_path = checked(source['fixed_problem']['actual_anchor'])
    origin_repo = Path(context['original_repository']).resolve()
    scripts = origin_repo/'topics/visible-flex-held-10pct/scripts'
    loader = module('_qr_fixed_support_original_geometry_loader', scripts/'resume_m3/actual_m3_metric_model.py')
    anchor = load(anchor_path)
    design = loader.load_model(dict(source_run=str(anchor_path)))
    signature_api = module('_qr_fixed_support_original_signature', scripts/'resume_20261126/fixed_m3_branch_model.py')
    signature = signature_api.original_source_signature(anchor)
    if anchor['core_settings']['homotopy'] != 1 or anchor['core_settings']['curvature_blend'] != 1:
        raise ValueError('The original support lambda-one family changed')
    return design, anchor, signature


def first_fixed_problem(context, design, anchor, signature, raw):
    design.initial(raw['p'])
    frozen = {**copy.deepcopy(design.cfg), 'delta':float(design.cfg['delta']+raw['p'][0])}
    if frozen != anchor['frozen_profile']:
        raise ValueError('The actual returned delta is not the saved physical frozen metric')
    norm = anchor['gates']['physical_bc_tol']/anchor['gates']['bc_tol']
    if not np.all(design.bcweights == norm):
        raise ValueError('The original boundary normalization changed')
    return dict(original_repository=context['original_repository'],
        anchor_source_kind=ANCHOR_SOURCE_KIND,
        complete_anchor_gate_provenance=copy.deepcopy(context['complete_anchor_gate_provenance']),
        actual_anchor=ref(context['path']), coupling_summary=context['coupling_summary'],
        original_anchor_gate=context['anchor_gate'],
        anchor_raw=context['raw'], anchor_physical=context['physical'],
        anchor_final_physical_height_binding=context['final_height_binding'],
        anchor_final_physical_packet=context['final_packet'],
        anchor_port=context['port'],
        frozen_source_signature=signature, frozen_profile=frozen,
        frozen_literal_radial_chart=chart_record(design),
        angular_chart=copy.deepcopy(anchor['angular_chart']),
        core_settings=copy.deepcopy(anchor['core_settings']),
        gauge_q=float(design.q), warp_reference_q=float(design.warp_q),
        q_seed=float(design.seed_support_amplitude), mean_nodes=context['mean_nodes'],
        bc_normalization=float(norm), bridge_sigma=float(design.bridge.sigma),
        physical_tail_parameters=copy.deepcopy(anchor['physical_tail_parameters']),
        physical_tail_cut=copy.deepcopy(anchor['physical_tail_cut']),
        parameter_zero_meaning=PARAMETER_ZERO,
        original_support_family_and_exact_lift_retained=True,
        physical_delta_is_solution_unknown=False)


def construct(design, problem, port_path, modes, angular):
    port = load(port_path)
    port['cut']['_prefix_bridge'] = copy.deepcopy(problem['frozen_profile']['prefix_bridge'])
    port['_sha256'] = sha(port_path)
    if (port['parameters'] != problem['physical_tail_parameters']
            or port['cut'] != problem['physical_tail_cut']
            or port['modes'] != [3*j for j in range(1, modes+1)]):
        raise ValueError('The target port changed the actual complete physical metric or modes')
    obj = type(design)(copy.deepcopy(problem['frozen_profile']), port,
        problem['gauge_q'], modes, angular, True, problem['warp_reference_q'])
    restore_chart(obj, problem['frozen_literal_radial_chart'])
    obj.bcweights = np.full(modes, problem['bc_normalization'])
    if (obj.seed_support_amplitude != problem['q_seed'] or not obj.fixed
            or obj.cfg != problem['frozen_profile'] or obj.q != problem['gauge_q']
            or obj.warp_q != problem['warp_reference_q']
            or obj.bridge.sigma != problem['bridge_sigma']):
        raise ValueError('The original fixed=True construction changed a frozen quantity')
    return obj


def embed(values, old_m, new_m):
    values = np.asarray(values)
    if new_m < old_m or values.shape[0] != 3*old_m+1:
        raise ValueError('A complete Fourier embedding cannot drop modes')
    result = np.zeros((3*new_m+1,)+values.shape[1:], dtype=values.dtype)
    result[0] = values[0]
    for source, target in ((1,1), (old_m+1,new_m+1), (2*old_m+1,2*new_m+1)):
        result[target:target+old_m] = values[source:source+old_m]
    return result


def lift_weight(flow, s):
    a = flow.profile(s)[0]
    z = np.clip((s-.5*flow.prefix_end)/(.4*flow.prefix_end), 0., 1.)
    return a*(1-z**3*(10-15*z+6*z*z))


def prepare(context, target, *, radial_refine=1):
    """Preserve all source knots and complete physical controls in an initial guess."""
    if type(radial_refine) is not int or radial_refine < 1:
        raise ValueError('Use a positive integral radial subdivision')
    design, anchor, signature = bootstrap(context)
    raw = raw_arrays(context)
    source = context['record']
    first = context['role'] == 'accepted_original_support_qr_chord_design_actual_return'
    if first:
        old = design
        problem = first_fixed_problem(context, design, anchor, signature, raw)
    else:
        problem = copy.deepcopy(source['fixed_problem'])
        if signature != problem['frozen_source_signature']:
            raise ValueError('The anchored original source implementation changed')
        old = construct(design, problem, checked(context['port']), source['modes'], source['angular'])
    new = construct(design, problem, target['linear_port_path'], target['modes'], target['angular'])
    old_m = int(source['modes'])
    x0, y0, p0 = raw['x'], raw['y'], raw['p']
    if (new.M < old_m or new.nt < old.nt or not np.array_equal(raw['pscale'], old.pscale)
            or not np.array_equal(new.pscale[:old_m-1], old.pscale)):
        raise ValueError('Retained mode count, angular resolution or physical parameter scales changed')
    old_initial = old.initial(p0).copy()
    old_coefficients = np.asarray(old._core.coefficients).copy()
    q_actual = float(old.support_amplitude)
    parameters = np.zeros(new.M)
    parameters[0] = math.log(q_actual/problem['q_seed']) if first else p0[0]
    parameters[1:old_m] = p0[1:]
    new_initial = new.initial(parameters).copy()
    new_coefficients = np.asarray(new._core.coefficients)
    if (not np.array_equal(new_coefficients[:old_m], old_coefficients)
            or np.any(new_coefficients[old_m:] != 0)):
        raise ValueError('The complete original support coefficients were not retained literally')
    old_flow, flow = old.flow(p0[0]), new.flow(parameters[0])
    old_chart, new_chart = old.chart(x0, p0[0]), new.chart(x0, parameters[0])
    if (old_flow.end != flow.end
            or any(not np.array_equal(left,right) for left,right in zip(old_chart,new_chart))):
        raise ValueError('The actual literal radial chart or physical domain changed')
    grids = [x0, np.asarray(problem['frozen_literal_radial_chart']['chart_breaks'])]
    if radial_refine > 1:
        grids.append(np.concatenate([np.linspace(lo,hi,radial_refine+1)
                                     for lo,hi in zip(x0[:-1],x0[1:])]))
    # np.unique retains every distinct literal source knot. There is no
    # tolerance merge which could silently replace an accepted old node.
    x = np.unique(np.concatenate(grids))
    if x[0] != 0 or x[-1] != 1 or not np.all(np.isin(x0,x)):
        raise ValueError('The complete accepted computational grid changed')
    if np.array_equal(x,x0):
        old_values = y0.copy()
    else:
        with np.load(checked(context['physical']), allow_pickle=False) as saved:
            physical = PPoly.construct_fast(saved['c'].copy(),saved['x'].copy(),axis=1,extrapolate=False)
            if not np.array_equal(saved['p'],p0):
                raise ValueError('The actual source physical field has different parameters')
        old_values = physical(new.chart(x,parameters[0])[0])
        matches = np.searchsorted(x,x0)
        if not np.array_equal(x[matches],x0):
            raise ValueError('A source node was lost in the refined grid')
        old_values[:,matches] = y0
    difference = new_initial-embed(old_initial,old_m,new.M)
    y = embed(old_values,old_m,new.M)
    if np.any(difference != 0):
        y += lift_weight(flow,new.chart(x,parameters[0])[0])[None,:]*difference[:,None]
    if not np.all(np.isfinite(y)):
        raise FloatingPointError('The complete physical support lift is nonfinite')
    target.update(fixed_problem=problem, frozen_profile=copy.deepcopy(problem['frozen_profile']),
        mean_nodes=problem['mean_nodes'], gauge_q=problem['gauge_q'],
        warp_reference=problem['warp_reference_q'], bc_normalization=problem['bc_normalization'],
        physical_tail_parameters=copy.deepcopy(problem['physical_tail_parameters']),
        physical_tail_cut=copy.deepcopy(problem['physical_tail_cut']),
        angular_chart=copy.deepcopy(problem['angular_chart']), core_settings=copy.deepcopy(problem['core_settings']),
        parameter_scales=new.pscale.tolist())
    transfer = dict(source_role=context['role'], source_nodes=len(x0), initial_nodes=len(x),
        source_modes=old_m,target_modes=new.M,radial_refine=radial_refine,
        complete_source_knots_retained=True, literal_chart_values_and_derivatives_bitwise_retained=True,
        complete_original_support_coefficients_retained=True, new_support_coefficients_are_zero=True,
        initial_parameters=parameters.tolist(), initial_support_coefficients=new_coefficients.tolist(),
        exact_lift_coefficient=1, initial_projection_transfer_max=float(np.max(np.abs(difference))),
        initial_q_actual=q_actual, initializer_is_accepted_solution=False,
        design_delta_is_no_longer_an_unknown=True, linear_bvp_invoked=False)
    return new,x,y,parameters,transfer


def validate_refinement_definition(record, context):
    problem = record['fixed_problem']
    if (problem.get('anchor_source_kind') != ANCHOR_SOURCE_KIND
            or problem.get('complete_anchor_gate_provenance', {}).get('source_kind') != ANCHOR_SOURCE_KIND):
        raise ValueError('The fixed complete problem lost its real QR anchor identity')
    parent = context['record']
    if (record.get('model_kind') != KIND or record.get('fixed_metric') is not True
            or record.get('fixed_core') is not False or record.get('fixed_metric_refinement') is not True
            or record.get('parameter_zero_meaning') != PARAMETER_ZERO
            or record.get('terminal_kind') != 'original_actual_nonlinear_dn'
            or record.get('linear_bvp_invoked') is not False
            or record.get('exact_lift_coefficient') != 1):
        raise ValueError('The honest original-support fixed actual-DN declaration is incomplete')
    if context['role'] == 'accepted_original_support_qr_anchor_fixed_metric_actual_return':
        if record['fixed_problem'] != parent['fixed_problem']:
            raise ValueError('A fixed complete problem changed during refinement')
    else:
        problem = record['fixed_problem']
        for key, wanted in (('actual_anchor',ref(context['path'])),
                            ('coupling_summary',context['coupling_summary']),
                            ('anchor_raw',context['raw']),('anchor_physical',context['physical']),
                            ('anchor_final_physical_packet',context['final_packet'])):
            if problem[key] != wanted:
                raise ValueError('The actual first anchor identity changed: '+key)
    if (record['mean_nodes'] != context['mean_nodes'] or record['modes'] < parent['modes']
            or record['angular'] < parent['angular'] or record['gates']['tol'] >= context['gates']['tol']):
        raise ValueError('A refinement changed its finite mean, dropped modes or failed to tighten radial tolerance')
    for key, upper in (('tol',1e-6),('bc_tol',1e-7),('physical_bc_tol',2e-9)):
        if not 0 < record['gates'][key] <= min(upper,context['gates'][key]):
            raise ValueError('An original residual gate was loosened: '+key)
    if (record['gates']['tail_solve_tolerance'] != 2e-9
            or record['gates']['original_outer_budget'] != 8):
        raise ValueError('The full nonlinear-tail or outer budget changed')
    original = load(checked(context['tail_settings']))
    target = load(record['tail_settings'])
    skip = set(RUNTIME_CONFIG_KEYS)|{'modes','quadrature','steps'}
    if ({k:v for k,v in original.items() if k not in skip}
            != {k:v for k,v in target.items() if k not in skip}):
        raise ValueError('The complete actual tail background, depth or subdivision changed')
    if (type(target['steps']) is not int or target['steps'] < original['steps']
            or target['steps'] % original['steps'] or target['modes'] != record['modes']
            or not 1 <= target['modes'] <= 64 or target['quadrature'] < original['quadrature']
            or target['quadrature'] <= 12*target['modes']
            or target.get('chordMaxCorrections') != 3
            or Path(target.get('initialCheckpoint','')).resolve() != checked(context['final_packet'])):
        raise ValueError('The complete original native scope/state initializer changed')
    base = {k:v for k,v in target.items() if k not in RUNTIME_CONFIG_KEYS}
    if load(record['base_tail_settings']) != base:
        raise ValueError('The explicit baseline settings do not bind the actual runtime')
    port = load(record['linear_port_path'])
    if (port['source']['config_sha256'] != sha(record['base_tail_settings'])
            or port['parameters'] != record['fixed_problem']['physical_tail_parameters']
            or dict(port['cut'],_prefix_bridge=record['frozen_profile']['prefix_bridge'])
               != record['fixed_problem']['physical_tail_cut']):
        raise ValueError('The complete startup port changes the frozen metric')


def load_model(config):
    path = Path(config['source_run']).resolve()
    context = accepted_input(path,repo=config['repo'])
    if context['role'] != 'accepted_original_support_qr_anchor_fixed_metric_actual_return':
        raise ValueError('This loader requires its own genuine fixed actual-DN return')
    record = context['record']
    design,anchor,signature = bootstrap(context)
    if signature != record['fixed_problem']['frozen_source_signature']:
        raise ValueError('The original full geometry provider changed')
    obj = construct(design,record['fixed_problem'],record['linear_port_path'],record['modes'],record['angular'])
    obj.relative_metric_loader_record = dict(model_kind=KIND,source_run=ref(path),
        fixed_metric=True,fixed_core=False,mean_nodes=record['mean_nodes'],
        parameter_zero_meaning=PARAMETER_ZERO, original_support_and_exact_lift=True,
        terminal_kind='original_actual_nonlinear_dn',bvp_or_tail_solver_invoked=False,
        original_repository=record['fixed_problem']['original_repository'])
    return obj
