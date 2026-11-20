#!/usr/bin/env python3
"""R679 N-only preparation, genuine even/odd readout and full continuation.

No M padding, radial restriction, new node/carrier, lambda migration or
changed mother norm.  Preparation is stdlib/report/source work only.
Every array, operator, oracle and solve entry requires public Actions.
The original input bundle/node/observation files are reused unchanged.
"""
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import shlex
import subprocess
import sys
import time


SCHEMA = 'same-g-N-only-complete-Phi-continuation-v1'
M_HELPER_SHA = 'eea174b983d20543a154df6fdb308bb5742c7f3bde04936c960fd572de267677'
HISTORY_SHA = '4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'
TRANSFER_SHA = '2e8ae99813c105982b10b896606538c1c42baf0abf089457412b32e265d4411a'
MANIFEST_SHA = '100e57c66e1f5b592fe22570c6c7894a6ab75e082b714edfff42514098d5c622'
SOC_DERIVER_SHA = '805823e49970246bf532b65a0caefd88244b414ee52f8f555ff28b745d2fd30a'
SOC_LAUNCHER_SHA = '9b7d50fd7d1a0332fc493f848688b792dff39fd2a1af4914349d048abe080d0a'
COMPOSITE_SHA = '40e8c42b8c66424d06ff08af8dff8d1505eff2b4f48ba905c9ae405000d2357e'
POSITION_SCHEMA = 'immutable-curvature-history-locations-v1'


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            digest.update(block)
    return digest.hexdigest()


def load(name, path, expected=None):
    if expected is not None and sha(path) != expected:
        raise ValueError('Changed declared dependency: '+name)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def bind_parent(report, supplied, folder, history):
    """Whole-body identities, never a new permissive parent-source branch."""
    if 'pcg_soc_derivation' in report:
        binder = load('N_only_complete_PCG_SOC_binder',
            folder/'derive_full_phi_coarse_pcg_soc.py', COMPOSITE_SHA)
        binding = binder.bind_soc_parent(report, supplied, folder,
            folder/'launch_fixed_g_refinement_qp.py')
        family = 'PCG_SOC'
    elif 'soc_derivation' in report:
        if supplied is None:
            raise ValueError('A SOC parent requires its actual complete source')
        binder = load('N_only_complete_SOC_binder',
            folder/'derive_full_phi_parent_row_soc.py', SOC_DERIVER_SHA)
        binding = binder.bind_soc_parent(report, supplied, folder,
            folder/'launch_fixed_g_refinement_qp.py')
        family = 'SOC'
    else:
        binding = history.bound_parent_source(report, folder, supplied)
        family = 'frozen_or_manifest'
    if family == 'frozen_or_manifest':
        damping = history.terminal_damping(report)
    else:
        checks = load('N_only_frozen_SOC_terminal_rule',
            folder/'launch_full_phi_parent_row_soc.py', SOC_LAUNCHER_SHA)
        damping = checks.check_SOC_terminal(history, report)
    base = binding.get('declared_derivation', {}).get('frozen_driver_sha256',
                                                    binding['sha256'])
    return dict(binding=binding, family=family, base_sha256=base, damping=damping)


def dimensions(report, new_angles=None):
    J, M, N = [int(report[key]) for key in ('J', 'M', 'N')]
    if any(report[key] != value for key, value in (('J',J),('M',M),('N',N))):
        raise ValueError('Nonintegral completed-report field dimensions')
    target = 2*N if new_angles is None else int(new_angles)
    rows = int(report['all_full_rows'])
    if (J < 2 or M < 3 or N % 4 or N <= 4*M or target != 2*N
            or rows != report['all_full_rows'] or rows % (3*N)):
        raise ValueError('Need the declared same-M dyadic N -> 2N refinement with old N>4M')
    P = rows//(3*N)
    if P < 2*J-1 or report['original_full_rows'] != 3*(2*J-1)*N:
        raise ValueError('Retain the complete original and added radial rows')
    free, integrated = int(report['original_variables']), int(report['integrated_variables'])
    if integrated-free != 2*(3*M+2):
        raise ValueError('The parent is not the declared complete integrated-coordinate layout')
    return dict(J=J, M=M, old_full_N=N, new_full_N=target,
        old_quarter_N=N//4+1, new_quarter_N=target//4+1,
        radial_observations=P, original_variables=free,
        integrated_variables=integrated, coarse_variables=int(report['coarse_variables']),
        old_full_rows=rows, new_full_rows=2*rows,
        one_new_quarter_residual_bytes=8*3*P*(target//4+1),
        added_original_variables=0, radial_rows_added=0,
        scope='Algebraic layout counts only; no actual field or memory experiment')


def contains_grid(value):
    if isinstance(value, dict):
        if ('stage' in value and 'angle' in value and 'phi' not in value):
            return True
        if any(key in value for key in ('grid_curvature_locations','grid_radius_locations')):
            return True
        return any(contains_grid(item) for item in value.values())
    if isinstance(value, list):
        if value and isinstance(value[0], str) and value[0] in ('grid','grid_radius'):
            return True
        return any(contains_grid(item) for item in value)
    return False


def extract_locations(history, payload, shape, *, source, explicit_N=None,
                      parent_report=False):
    """Resolve angle indices under their own declared old N, before union."""
    candidates = []
    for key in ('N','optimization_full_angles','full_angles'):
        if key in payload:
            n = int(payload[key])
            if n != payload[key]:
                raise ValueError('A manifest angular identity is not an integer')
            candidates.append(n)
    if explicit_N is not None:
        candidates.append(int(explicit_N))
    if candidates and len(set(candidates)) != 1:
        raise ValueError('Conflicting full-N identities in one supplied position payload')
    has_grid = contains_grid(payload)
    if candidates:
        N = candidates[0]
    elif parent_report:
        N = shape['old_full_N']
    elif has_grid:
        raise ValueError('A grid-bearing manifest needs its actual old N; use --grid-manifest N PATH')
    else:
        N = shape['old_full_N']  # Numeric cell/u/phi tuples do not use this N.
    if N <= 0 or N % 4:
        raise ValueError('A recorded quarter-grid full N must be positive and divisible by four')
    if parent_report and N != shape['old_full_N']:
        raise ValueError('Parent angle identity changed before extraction')
    if 'J' in payload and int(payload['J']) != shape['J']:
        raise ValueError('A supplied report belongs to another radial mesh')
    if 'all_full_rows' in payload and payload['all_full_rows'] != 3*shape['radial_observations']*N:
        raise ValueError('A supplied grid report belongs to another radial observation plan')
    # Nested complete reports with another N need their own extraction scope.
    # Ordinary scalar metadata containing N is not treated as a report.
    def check_nested(item, top=True):
        if isinstance(item, dict):
            if (not top and {'N','J','all_full_rows'} <= set(item)
                    and int(item['N']) != N and contains_grid(item)):
                raise ValueError('Split nested grid reports with different N into separately declared inputs')
            for child in item.values():
                check_nested(child, False)
        elif isinstance(item, list):
            for child in item:
                check_nested(child, False)
    check_nested(payload)
    points = history.Locations(shape['J'], shape['radial_observations'], N)
    points.walk(payload, path=(source,))
    # R676 also publishes these two compact stage/angle formats; the old
    # generic walker intentionally does not guess their interpretation.
    for key, role in (('grid_curvature_locations','curvature'),('grid_radius_locations','radius')):
        for pair in payload.get(key, []):
            if not isinstance(pair, list) or len(pair) != 2:
                raise ValueError('Malformed compact recorded grid location')
            points.grid(pair[0], points.angle(pair[1]), role, False, source+'.'+key)
    return points, dict(source=source, original_full_N=N,
        explicit_full_N=explicit_N, indexed_grid_present=has_grid,
        literal_quarter_angle_formula='pi*old_index/(old_full_N/2)',
        decimal_rounding=False, extraction=points.summary())


def same_source(role, path, report, history):
    record = history.file_record(path)
    if record['sha256'] != report.get('source_sha256_by_role', {}).get(role):
        raise ValueError('Changed actual parent field/objective/norm/solver source: '+role)
    return record


def prepare(args):
    folder = args.repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261120'
    m = load('N_only_frozen_M_interface_helpers', folder/'launch_frequency_only_fullclosed.py', M_HELPER_SHA)
    paths = m.source_inputs(folder)
    pins = dict(history=HISTORY_SHA, derivation=MANIFEST_SHA,
        transfer_helper=TRANSFER_SHA, original_launcher=m.ORIGINAL_LAUNCHER_SHA,
        tail_launcher=m.TAIL_LAUNCHER_SHA,
        original_driver=m.ORIGINAL_DRIVER_SHA, tail_driver=m.TAIL_DRIVER_SHA)
    for key, digest in pins.items():
        if sha(paths[key]) != digest:
            raise ValueError('Changed frozen N-only preparation dependency: '+key)
    history = load('N_only_complete_history', paths['history'], HISTORY_SHA)
    derivation = load('N_only_exact_position_transform', paths['derivation'], MANIFEST_SHA)
    report = json.loads(args.parent_report.read_text())
    parent = bind_parent(report, args.parent_source, folder, history)
    shape = dimensions(report, args.new_angles)
    if report.get('final_bundle_sha256') != sha(args.bundle):
        raise ValueError('Need the exact naturally completed parent final bundle')
    if report.get('observation_carrier_sha256') != sha(args.carrier):
        raise ValueError('Retain this actual parent radial observation file')
    objective = m.bound_objective(report)
    objective.pop('old_and_new_M_functionals_identical_on_the_included_subspace', None)
    objective.update(old_N=shape['old_full_N'], new_N=shape['new_full_N'],
        same_finite_functional=False, same_fixed_g=True,
        target_new_normalization=2*objective['normalization'],
        exact_relation='Phi_2N=.5*Phi_even_old_N+.5*Phi_new_odd_N')
    if parent['base_sha256'] not in (m.ORIGINAL_DRIVER_SHA,m.TAIL_DRIVER_SHA):
        raise ValueError('Unsupported complete original/R671 parent')
    tail = parent['base_sha256'] == m.TAIL_DRIVER_SHA
    lam, eta = 0., None
    if tail:
        if (report.get('exact_tail_node_report_sha256') != sha(args.node_report)
                or report.get('exact_tail_scalar_input_sha256') != sha(args.scalar_input)):
            raise ValueError('Use the current actual R671 node/scalar files')
        lam, eta = float(report['exact_tail_lambda']), int(report['exact_tail_eta_start_node'])
        if not math.isfinite(lam) or not 0 <= lam <= 1 or eta != report['exact_tail_eta_start_node']:
            raise ValueError('Invalid completed parent R671 model parameters')
    collections, records = [], []
    pts, info = extract_locations(history, report, shape, source='actual_parent', parent_report=True)
    collections.append(pts)
    records.append(dict(**history.file_record(args.parent_report), **info))
    entries = [(path, None) for path in args.manifest]
    entries += [(Path(path).resolve(), int(n)) for n, path in args.grid_manifest]
    for index, (path, explicit) in enumerate(entries):
        payload = json.loads(path.read_text())
        declared = payload.get('carrier_sha256', payload.get('observation_carrier_sha256'))
        if declared is not None and declared != sha(args.carrier):
            raise ValueError('A supplied permanent position payload names another radial carrier')
        pts, info = extract_locations(history, payload, shape,
            source='caller_'+str(index), explicit_N=explicit)
        collections.append(pts)
        records.append(dict(**history.file_record(path), **info))
    if args.outdir.is_relative_to(args.repo):
        raise ValueError('Keep actual scientific outputs and raw reports outside the Git checkout')
    prior_plan=None
    if args.outdir.exists() and any(args.outdir.iterdir()):
        prior_path=args.outdir/'angle-plan.json'
        if not prior_path.is_file():
            raise FileExistsError('The output directory belongs to another task')
        prior_plan=json.loads(prior_path.read_text())
        if (prior_plan.get('scientific_execution_started')
                or any((args.outdir/name).exists() for name in
                       ('solve','complete-permanent-locations.json','common-even-odd-readout.json'))):
            raise FileExistsError('An actual N-only attempt already owns this directory; use a new one')
    args.outdir.mkdir(parents=True, exist_ok=True)
    union = args.outdir/'complete-permanent-locations.json'
    if parent['family'] == 'frozen_or_manifest':
        driver = derivation.derive_driver(paths['tail_driver' if tail else 'original_driver'],
            args.outdir/'derived-full-phi-exact-positions.py')
    else:
        # The entire actual SOC or PCG+SOC body is already bound above.
        # Preserve it literally; changing --angles does not change its source.
        driver = dict(**history.file_record(parent['binding']['path']),
            reused_bound_parent_body=True, complete_body_binding=parent['binding'])
    maxiter = int(report['max_qp_hessian_advances']) if args.maxiter is None else args.maxiter
    if maxiter < 1:
        raise ValueError('Need a positive explicitly recorded complete-QP budget')
    launcher = paths['tail_launcher' if tail else 'original_launcher']
    invocation = [sys.executable, str(launcher), '--repo',str(args.repo),'--work',str(args.work),
        '--bundle',str(args.bundle),'--carrier',str(args.carrier),'--outdir',str(args.outdir/'solve'),
        '--damping',repr(parent['damping']['terminal_damping']), '--directions',str(args.directions),
        '--maxiter',str(maxiter),'--active-rows',str(report['active_max_rows']),
        '--qp-atol',repr(report['qp_atol']),'--qp-rtol',repr(report['qp_rtol']),
        '--manifest',str(union)]
    centers = report.get('requested_coarse_centers')
    if centers is not None:
        invocation.extend(['--coarse-centers',','.join(repr(float(v)) for v in centers)])
    if tail:
        invocation.extend(['--node-report',str(args.node_report),'--scalar-input',str(args.scalar_input),
            '--eta-start-node',str(eta),'--lambda-value',repr(lam),
            '--source-lambda',repr(lam),'--migration','keep-q'])
    returned = subprocess.run([*invocation,'--print-command'],check=True,capture_output=True,text=True)
    command = shlex.split(returned.stdout.strip())
    command[2] = driver['path']
    qp_wanted = report['source_sha256_by_role']['qp']
    qp_candidates = [folder/'fullspace_feasible_active_pcg_v4.py',
        folder/'fullspace_feasible_active_cg_v3.py',folder/'fullspace_feasible_active_cg_v2.py']
    if report.get('source_paths',{}).get('qp'):
        qp_candidates.append(Path(report['source_paths']['qp']))
    qp = next((p.resolve() for p in qp_candidates if p.is_file() and sha(p)==qp_wanted),None)
    if qp is None:
        raise ValueError('Need the actual same parent QP implementation')
    overrides = {'--qp-source':qp, '--angles':shape['new_full_N'],
        '--low-modes':report['coarse_low_modes'],'--stage-block':args.stage_block,
        '--target':report['target'],'--active-block-columns':report['active_block_columns'],
        '--active-top-curvature':report['active_top_curvature'],'--active-top-radius':report['active_top_radius'],
        '--line-trials':report['max_line_trials'],'--qp-feasibility-tolerance':report['qp_feasibility_tolerance'],
        '--qp-row-rank-tolerance':report['qp_row_rank_tolerance']}
    for flag,value in overrides.items():
        derivation.replace(command,flag,value)
    command.extend(['--active-rank-tolerance',repr(report['active_rank_tolerance'])])
    if report.get('sampled_curvature_cap') is not None:
        command.extend(['--curvature-cap',repr(report['sampled_curvature_cap'])])
    if centers is None:
        at=command.index('--coarse-centers')
        del command[at:at+2]
    roles = dict(operator='--operator',implementation='--implementation',basis='--basis-source',
        coarse='--coarse-source',helpers='--helpers',coordinates='--coordinate-source',
        scale='--scale-source',geometry='--geometry-source',point='--point-source',
        observed_geometry='--geometry-observed-source',base_batch='--base-batch-source',
        height='--height-source',angular='--angular-source',inequalities='--inequality-source',
        spectral='--spectral-source',spectral_hessian='--spectral-hessian-source',qp='--qp-source')
    if tail:
        roles.update(exact_tail='--exact-tail-source',tail_scalar='--tail-scalar-source',
            tail_integer='--tail-integer-source',tail_hold='--tail-hold-source')
    if parent['family'] in ('SOC','PCG_SOC'):
        tau = float(report['parent_row_soc']['tau'])
        if not math.isfinite(tau) or tau < 0:
            raise ValueError('Retain the actual declared parent SOC tau')
        command.extend(['--soc-source',str(folder/'full_phi_parent_row_soc.py'),'--soc-tau',repr(tau)])
        roles['soc']='--soc-source'
    if parent['family']=='PCG_SOC':
        command.extend(['--enable-coarse-preconditioner',
            '--coarse-frame-source',str(folder/'full_phi_coarse_frame.py'),
            '--coarse-moments-source',str(folder/'full_phi_coarse_moments.py')])
        roles.update(coarse_frame='--coarse-frame-source',coarse_moments='--coarse-moments-source')
    dependencies = {role:same_source(role,Path(m.argument(command,flag)).resolve(),report,history)
                    for role,flag in roles.items()}
    if parent['family']=='PCG_SOC':
        dependencies['coarse_qp_v3']=same_source('coarse_qp_v3',
            qp.with_name('fullspace_feasible_active_cg_v3.py'),report,history)
    inputs = {key:history.file_record(getattr(args,key)) for key in
              ('parent_report','bundle','carrier','node_report','scalar_input')}
    external = None
    if args.final_report is not None:
        final_report=json.loads(args.final_report.read_text())
        final_parent=bind_parent(final_report,args.final_source,folder,history)
        external=dict(report=history.file_record(args.final_report),
            bundle=history.file_record(args.final_bundle), parent_binding=final_parent)
    plan=dict(schema=SCHEMA,source_sha256=sha(__file__),inputs=inputs,
        M_only_helper=history.file_record(folder/'launch_frequency_only_fullclosed.py'),
        parent=parent,dimensions=shape,objective=objective,
        is_R671=tail,unchanged_lambda=lam,unchanged_eta_start_node=eta,
        input_position_scopes=records, source_preparation_launcher_argv=invocation,
        scientific_command=command,driver=driver,dependencies=dependencies,
        maxiter=maxiter,requested_directions=args.directions,
        readout_only=args.readout_only,external_completed_candidate=external,
        outputs=dict(permanent_locations=str(union),solver_directory=str(args.outdir/'solve'),
            angular_readout=str(args.outdir/'common-even-odd-readout.json')),
        original_bundle_file_reused=True,original_node_file_reused=True,
        original_observation_carrier_file_reused=True,
        M_radial_rows_g_and_mother_norm_unchanged=True,
        finite_mean_Phi_changed=True,new_grid_geometry_inherited=False,
        old_grid_decoded_before_new_N=True,scientific_arrays_read=False,
        scientific_execution_started=False,angular_or_frequency_convergence_demonstrated=False,
        continuous_metric_certified=False,topic_completion_certified=False)
    path=args.outdir/'angle-plan.json'
    if prior_plan is not None:
        for key in ('schema','source_sha256','inputs','parent','dimensions','objective',
                    'input_position_scopes','scientific_command','driver','dependencies',
                    'maxiter','requested_directions','readout_only','external_completed_candidate'):
            if prior_plan.get(key)!=plan[key]:
                raise FileExistsError('The prepared N-only inputs/parameters changed; use a fresh directory')
    history.write_json(path,plan)
    return dict(m=m,history=history,paths=paths,folder=folder,report=report,parent=parent,
        plan=plan,plan_path=path,collections=collections,union=union,command=command)


def validate_arrays(args,state):
    h,p=state['history'],state['plan']
    h.require_actions()
    import numpy as np
    helper=load('N_only_R676_model_helpers',state['paths']['transfer_helper'],TRANSFER_SHA)
    paths=helper.sources(args.repo)
    for key in ('observed','batch','dense','factory','scalar','integer','hold','spectral'):
        if sha(paths[key])!=helper.EXPECTED[key]:
            raise ValueError('Changed frozen finite-field/readout dependency: '+key)
    observed=helper.load('N_only_complete_observed',paths['observed'])
    factory=helper.load('N_only_reference_factory',paths['factory'])
    with np.load(args.bundle,allow_pickle=False) as raw:
        data={key:np.array(raw[key],copy=True) for key in raw.files}
    with np.load(args.carrier,allow_pickle=False) as raw:
        carrier={key:np.array(raw[key],copy=True) for key in raw.files}
    shape=p['dimensions'];J=shape['J'];M=shape['M'];P=shape['radial_observations']
    if data['qjets'].shape!=(J,3,3*M+2) or data['mesh'].shape!=(J,):
        raise ValueError('Actual parent field differs from the completed report layout')
    for key in ('mesh','a_stages','radius','width','fixed_core_first3'):
        if not state['m'].array_identity(np,data[key],carrier[key]):
            raise ValueError('Parent and original carrier differ: '+key)
    plan=observed.ObservationPlan.from_arrays(carrier)
    if len(plan.cells)!=P or plan.legacy_count!=2*J-1 or carrier['a_observations'].shape!=(P,):
        raise ValueError('The actual full observation carrier differs from the parent report')
    node=json.loads(args.node_report.read_text())
    nodes=[(Fraction(v['S_coefficient']),Fraction(v['constant'])) for v in node['true_scalar_nodes']]
    anchors=node['true_a_stage_boxes']
    if (node['input_sha256']!=sha(args.scalar_input) or len(nodes)!=J or len(anchors)!=2*J-1
            or nodes[0]!=(Fraction(0),Fraction(0)) or nodes[-1]!=(Fraction(1),Fraction(0))
            or float(node['S_carrier'])!=float(data['mesh'][-1])
            or float(node['radius_carrier'])!=float(data['radius'])
            or ('M' in node and int(node['M'])!=M)):
        raise ValueError('Actual symbolic nodes/scalar definition differ from the unchanged field')
    if any(Fraction(v['lower_exact'])<=0 or Fraction(v['upper_exact'])<Fraction(v['lower_exact']) for v in anchors):
        raise ValueError('Retain the complete positive original node/midpoint a enclosures')
    state['m'].affine_input(np,data['qjets'],data['fixed_core_first3'])
    model=helper.model_definition(data,nodes,paths,args.node_report,args.carrier,args.scalar_input,factory)
    if (model['definition'] is not None)!=p['is_R671'] or model['lambda_value']!=p['unchanged_lambda']:
        raise ValueError('Actual field representation differs from its completed report')
    if p['is_R671'] and int(model['definition']['eta_start_node'])!=p['unchanged_eta_start_node']:
        raise ValueError('Actual R671 eta identity differs')
    return dict(np=np,helper=helper,paths=paths,observed=observed,factory=factory,
                data=data,carrier=carrier,observation_plan=plan,node=node,nodes=nodes,model=model)


def materialize_positions(args,state):
    h=state['history'];h.require_actions()
    shape=state['plan']['dimensions']
    union=h.Locations(shape['J'],shape['radial_observations'],shape['old_full_N'])
    returned=[]
    for points,scope in zip(state['collections'],state['plan']['input_position_scopes']):
        count=points.resolve_grid(args.carrier)
        union.walk(points.arrays())
        returned.append(dict(**scope,resolved_grid_count=count,final_extraction=points.summary()))
    arrays=union.arrays()
    if not arrays['curvature_points'] or not arrays['radius_points']:
        raise ValueError('Retain both complete permanent curvature and radius location unions')
    payload=dict(schema=POSITION_SCHEMA,bundle_sha256=sha(args.bundle),
        carrier_sha256=sha(args.carrier),source_sha256=sha(__file__),
        parent_report=h.file_record(args.parent_report),history_helper_sha256=HISTORY_SHA,
        extraction_sources=returned,**arrays,extraction=union.summary(),
        old_to_new_ideal_quarter_index='k -> 2*k',
        physical_positions_are_original_literal_binary_tuples=True,
        phi_projected_to_new_grid=False,decimal_position_rounding=False,
        original_cells_and_binary_u_unchanged=True,values_inherited=False)
    h.write_json(state['union'],payload,compact=True)
    return dict(file=h.file_record(state['union']),extraction=union.summary(),
                source_grid_scopes=returned)


def materialize_final_positions(args,state,report,bundle):
    """New returned grid indices use new N; old tuples stay literal."""
    h=state['history'];h.require_actions();shape=state['plan']['dimensions']
    points,scope=extract_locations(h,report,shape,source='actual_new_N_final')
    count=points.resolve_grid(args.carrier)
    union=h.Locations(shape['J'],shape['radial_observations'],shape['new_full_N'])
    union.walk(json.loads(state['union'].read_text()))
    union.walk(points.arrays())
    path=args.outdir/'complete-permanent-locations-final.json'
    payload=dict(schema=POSITION_SCHEMA,source_sha256=sha(__file__),
        bundle_sha256=sha(bundle),carrier_sha256=sha(args.carrier),
        input_union=h.file_record(state['union']),new_report_scope=scope,
        new_grid_points_resolved=count,**union.arrays(),extraction=union.summary(),
        old_positions_reinterpreted_under_new_N=False,decimal_position_rounding=False,
        all_recognized_old_and_new_positions_retained=True,values_inherited=False)
    h.write_json(path,payload,compact=True)
    return dict(file=h.file_record(path),extraction=union.summary())


def make_readout_operator(args,state,arrays):
    np=arrays['np'];data=arrays['data'];paths=arrays['paths']
    dim=state['plan']['dimensions'];context=None
    if state['plan']['is_R671']:
        panels=int(arrays['node']['scalar']['simpson_panels_per_ramp'])
        if panels!=128:
            raise ValueError('Keep the frozen full-driver 128-panel profile convention')
        context=arrays['factory'].TailLiftContext.from_files(bundle=args.bundle,carrier=args.carrier,
            node_report=args.node_report,scalar_input=args.scalar_input,
            scalar_source=paths['scalar'],integer_source=paths['integer'],hold_source=paths['hold'],
            observed_source=paths['observed'],eta_start_node=state['plan']['unchanged_eta_start_node'],
            lambda_value=state['plan']['unchanged_lambda'],panels=panels)
        op,native=context.create_pair(paths['dense'],paths['batch'],
            N=dim['new_full_N'],stage_block=args.stage_block,quarter=True)
        del native
        if context.definition()!=arrays['model']['definition']:
            raise ValueError('N-only must retain the entire canonical reference-tail definition')
    else:
        op=arrays['observed'].create(paths['dense'],data['mesh'],data['a_stages'],
            float(data['radius']),data['fixed_core_first3'],M=dim['M'],N=dim['new_full_N'],
            width=float(data['width']),quarter=True,stage_block=args.stage_block,
            batch_source=paths['batch'],observation_plan=arrays['observation_plan'],
            a_observations=arrays['carrier']['a_observations'])
    old_phi=np.pi*np.arange(dim['old_full_N']//4+1)/(dim['old_full_N']//2)
    if not np.array_equal(op.phi[::2],old_phi):
        raise ValueError('New even angle carriers differ literally from the old formula; a distinct old-angle reader is required')
    if not state['m'].array_identity(np,op.a,arrays['carrier']['a_observations']):
        raise ValueError('The shared readout operator changed actual target a carriers')
    spectral=arrays['helper'].load('N_only_original_positive_spectral_loss',paths['spectral'])
    return op,context,spectral


def read_field(op,data,np,spectral,old_N,*,name,progress=None):
    """All/even/odd use exactly one actual new-grid first-jet block buffer."""
    started=time.monotonic()
    x,affine=op.pack(data['qjets'],float(data['Hcap']),require_affine=True)
    prepared=op.prepare(x)
    radial=op.mixed_stage_weights(.5)
    mass=float(radial.sum())
    if np.any(radial<=0) or op.full_N!=2*old_N:
        raise ValueError('Retain all positive radial weights and the exact declared dyadic full grid')
    selectors=dict(even=np.arange(0,op.N,2,dtype=int),
                   odd=np.arange(1,op.N,2,dtype=int),all=np.arange(op.N,dtype=int))
    sums={key:dict(loss=0.,sse=0.,maximum=-1.,worst=None,min_det=float('inf'),min_E=float('inf')) for key in selectors}
    orbits={key:op.multiplicity[index] for key,index in selectors.items()}
    for key in selectors:
        expected=2*old_N if key=='all' else old_N
        if float(orbits[key].sum())!=expected or np.any(orbits[key]<=0):
            raise ValueError('Quarter endpoint/interior weights do not give the declared even/odd mass')
    parameters=spectral.Parameters(p=8,epsilon=.001,scale=.05)
    completed=0;failure=None;batches=0
    for start in range(0,op.P,op.stage_block):
        stop=min(start+op.stage_block,op.P)
        try:
            v,d=op._first_batch(prepared,start,stop)
            ar=op.a[start:stop,None]*prepared.rho[None]
            if not np.isfinite(ar).all() or np.any(ar==0):
                raise ArithmeticError('Invalid target angular denominator in the actual current field')
            raw=np.stack((np.einsum('bni,bni->bn',v,v)-1,
                np.einsum('bni,bni->bn',v,d)/ar,
                np.einsum('bni,bni->bn',d,d)/(ar*ar)-1),axis=-1)
            if not np.isfinite(raw).all():
                raise ArithmeticError('Nonfinite actual new-grid Gram block')
            plus,minus,_=spectral.eigenvalues(raw)
            loss=spectral.point_loss(raw,parameters)
            magnitude=np.maximum(abs(plus),abs(minus))
            square=raw[...,0]**2+2*raw[...,1]**2+raw[...,2]**2
            det=(1+raw[...,0])*(1+raw[...,2])-raw[...,1]**2
            if not np.isfinite(loss).all():
                raise ArithmeticError('Nonfinite actual spectral loss')
            updates={}
            for key,index in selectors.items():
                values=magnitude[:,index]
                at=np.unravel_index(int(np.argmax(values)),values.shape)
                row=start+int(at[0]);angle=int(index[int(at[1])])
                location=dict(stage=row,cell=int(op.observation_cells[row]),u=float(op.observation_u[row]),
                    s_carrier=float(op.times[row]),new_quarter_angle_index=angle,
                    old_quarter_angle_index=(angle//2 if angle%2==0 else None),
                    old_halfstep_interval_index=(angle//2 if angle%2 else None),
                    phi=float(op.phi[angle]),phi_binary_hex=float(op.phi[angle]).hex(),
                    ideal_phi_over_pi=str(Fraction(2*angle,op.full_N)),
                    angular_subset=('even_old' if angle%2==0 else 'new_odd'))
                updates[key]=dict(loss=float(radial[start:stop]@(loss[:,index]@orbits[key])),
                    sse=float(radial[start:stop]@(square[:,index]@orbits[key])),
                    maximum=float(values[at]),worst=location,
                    min_det=float(np.min(det[:,index])),min_E=float(np.min(1+raw[:,index,0])))
            if any(not math.isfinite(value['loss']) or not math.isfinite(value['sse'])
                    or not math.isfinite(sums[key]['loss']+value['loss'])
                    or not math.isfinite(sums[key]['sse']+value['sse'])
                    for key,value in updates.items()):
                raise ArithmeticError('Nonfinite actual partition reduction')
            for key,value in updates.items():
                target=sums[key]
                target['loss']+=value['loss'];target['sse']+=value['sse']
                target['min_det']=min(target['min_det'],value['min_det'])
                target['min_E']=min(target['min_E'],value['min_E'])
                if value['maximum']>target['maximum']:
                    target['maximum']=value['maximum'];target['worst']=value['worst']
            completed=stop;batches+=1
            if progress is not None:
                progress(dict(field=name,radial_rows_returned=completed,radial_rows_total=op.P))
        except (ArithmeticError,MemoryError) as error:
            failure=dict(type=type(error).__name__,reason=str(error),first_unreturned_stage=start)
            break
    complete=completed==op.P
    scopes={}
    for key,acc in sums.items():
        denominator=mass*float(orbits[key].sum())
        scopes[key]=dict(radial_rows=op.P,radial_rows_returned=completed,
            complete_scope=complete,orbit_mass=float(orbits[key].sum()),quarter_columns=len(selectors[key]),
            normalization=denominator,
            mean_Phi=(acc['loss']/denominator if complete else None),
            weighted_frobenius_sse=(acc['sse'] if complete else None),
            mean_weighted_frobenius_sse=(acc['sse']/denominator if complete else None),
            maximum_relative_Gram=(acc['maximum'] if complete else None),
            worst_Gram=acc['worst'],minimum_relative_determinant=(acc['min_det'] if complete else None),
            minimum_relative_E=(acc['min_E'] if complete else None),
            minimum_normalized_orbit_weight=float(radial.min()*orbits[key].min()/denominator),
            returned_only_unnormalized_loss=acc['loss'],returned_only_unnormalized_sse=acc['sse'],
            returned_only_maximum=(acc['maximum'] if completed else None),
            missing_rows_treated_as_zero=False)
    relation=None
    if complete:
        relation=dict(Phi_all_minus_half_even_minus_half_odd=scopes['all']['mean_Phi']-
            .5*scopes['even']['mean_Phi']-.5*scopes['odd']['mean_Phi'],
            max_all_minus_max_parts=scopes['all']['maximum_relative_Gram']-
                max(scopes['even']['maximum_relative_Gram'],scopes['odd']['maximum_relative_Gram']),
            scope='Same returned block values; ordinary floating reduction differences, not outward certificates')
    return dict(name=name,complete=complete,affine=affine,partitions=scopes,
        decomposition_readout=relation,failure=failure,seconds=time.monotonic()-started,
        rho_sample_minimum=(float(np.min(prepared.rho)) if np.isfinite(prepared.rho).all() else None),
        rho_sample_positive=bool(np.isfinite(prepared.rho).all() and np.all(prepared.rho>0)),
        actual_free_vector_sha256=hashlib.sha256(np.ascontiguousarray(x).tobytes()).hexdigest(),
        first_jet_batches_returned=batches,new_grid_evaluated_once=True,
        exact_even_angle_carriers_equal_old=True,parameters=parameters.as_dict(),
        curvature_or_permanent_geometry_read=False,continuous_metric_certified=False,
        old_finite_geometry_flags_inherited=False)


def check_final(args,state,report,bundle,source):
    h=state['history'];plan=state['plan'];dim=plan['dimensions']
    binding=bind_parent(report,source,state['folder'],h)
    if (report.get('complete') is not True or report.get('final_bundle_sha256')!=sha(bundle)
            or report.get('observation_carrier_sha256')!=plan['inputs']['carrier']['sha256']
            or any(report.get(key)!=value for key,value in dict(J=dim['J'],M=dim['M'],N=dim['new_full_N'],
                all_full_rows=dim['new_full_rows'],original_variables=dim['original_variables'],
                integrated_variables=dim['integrated_variables'],coarse_variables=dim['coarse_variables']).items())
            or binding['base_sha256']!=state['parent']['base_sha256']):
        raise ValueError('Returned new-N candidate is not the declared complete same-space field')
    final_objective=state['m'].bound_objective(report)
    if final_objective['normalization']!=plan['objective']['target_new_normalization']:
        raise ValueError('The same radial weights with doubled N need exactly the declared doubled normalization')
    for role,record in plan['dependencies'].items():
        if report.get('source_sha256_by_role',{}).get(role)!=record['sha256']:
            raise ValueError('The actual new-N solve changed a declared dependency: '+role)
    if report['bundle_sha256']!=plan['inputs']['bundle']['sha256']:
        raise ValueError('The actual new-N solve did not start from this exact parent bundle')
    if plan['is_R671'] and (report['exact_tail_lambda']!=plan['unchanged_lambda']
            or report['exact_tail_eta_start_node']!=plan['unchanged_eta_start_node']
            or report['exact_tail_node_report_sha256']!=plan['inputs']['node_report']['sha256']
            or report['exact_tail_scalar_input_sha256']!=plan['inputs']['scalar_input']['sha256']):
        raise ValueError('Returned R671 solve changed the physical reference-tail definition')
    if report.get('initial_damping')!=state['parent']['damping']['terminal_damping']:
        raise ValueError('New-N solve changed the inherited same-unit initial damping')
    coarse_layout=('coarse_low_modes','requested_coarse_centers','actual_coarse_center_nodes')
    strategy=('qp_atol','qp_rtol','qp_feasibility_tolerance','qp_row_rank_tolerance',
        'active_max_rows','active_block_columns','active_rank_tolerance',
        'active_top_curvature','active_top_radius','max_line_trials','target','sampled_curvature_cap')
    for key in coarse_layout+strategy:
        if key not in state['report'] or key not in report or report[key]!=state['report'][key]:
            raise ValueError('N-only final changed the actual coarse layout or continuation strategy: '+key)
    if binding['family']!=state['parent']['family']:
        raise ValueError('N-only final changed the bound original/SOC/PCG continuation family')
    if state['parent']['family'] in ('SOC','PCG_SOC'):
        if report['parent_row_soc']!=state['report']['parent_row_soc']:
            raise ValueError('N-only continuation changed the declared SOC/PCG policy')
    return dict(binding,matched_coarse_layout_fields=list(coarse_layout),
                matched_continuation_strategy_fields=list(strategy))


def paired_readout(args,state,arrays,final_bundle=None,final_report=None):
    h=state['history'];h.require_actions();np=arrays['np']
    started=time.monotonic()
    op,context,spectral=make_readout_operator(args,state,arrays)
    out=Path(state['plan']['outputs']['angular_readout'])
    result=dict(schema=SCHEMA+'-actual-even-odd-readout',source_sha256=sha(__file__),
        inputs=state['plan']['inputs'],dimensions=state['plan']['dimensions'],
        same_operator_and_radial_profile_for_both_fields=True,
        original_reference_definition=arrays['model']['definition'],
        actual_reference_context=None if context is None else context.metadata(),
        helper_sources={key:h.file_record(arrays['paths'][key]) for key in
            ('observed','batch','dense','factory','scalar','integer','hold','spectral')},
        exact_even_angle_carriers_equal_old=True,radial_file_sha256=sha(args.carrier),
        old_parent_report_statistics=state['m'].statistics_snapshot(
            state['report'].get('current',state['report']['initial'])),
        final=None,complete_pair=False,new_continuous_or_finite_geometry_certificate=False)
    def progress(value):
        if value['radial_rows_returned']==op.P or value['radial_rows_returned']%(16*op.stage_block)==0:
            print(json.dumps(dict(event='N_only_angular_partition_readout',**value)),flush=True)
    result['parent']=read_field(op,arrays['data'],np,spectral,
        state['plan']['dimensions']['old_full_N'],name='actual_parent',progress=progress)
    h.write_json(out,result)
    if final_bundle is not None:
        with np.load(final_bundle,allow_pickle=False) as raw:
            final={key:np.array(raw[key],copy=True) for key in raw.files}
        for key in ('mesh','a_stages','radius','width','fixed_core_first3'):
            if not state['m'].array_identity(np,final[key],arrays['data'][key]):
                raise ValueError('Actual final candidate changed a radial/port carrier: '+key)
        model=arrays['helper'].model_definition(final,arrays['nodes'],arrays['paths'],
            args.node_report,args.carrier,args.scalar_input,arrays['factory'])
        if model!=arrays['model']:
            raise ValueError('Final candidate changed the exact same-M reference model')
        state['m'].affine_input(np,final['qjets'],final['fixed_core_first3'])
        same=all(state['m'].array_identity(np,final[key],arrays['data'][key]) for key in ('qjets','Hcap'))
        result['final_bundle']=h.file_record(final_bundle)
        result['identical_parent_and_final_physical_coefficients']=same
        if same:
            result['final']=dict(result['parent'],name='actual_final_same_field',
                actual_readout_reused_from='actual_parent',additional_first_jet_batches=0)
        else:
            result['final']=read_field(op,final,np,spectral,
                state['plan']['dimensions']['old_full_N'],name='actual_final',progress=progress)
        result['final_report_statistics']=state['m'].statistics_snapshot(
            final_report.get('current',final_report['initial']))
        result['new_N_initial_driver_statistics']=state['m'].statistics_snapshot(final_report['initial'])
    if result['parent']['complete']:
        p=result['parent']['partitions'];old=result['old_parent_report_statistics']
        result['parent_grid_change_attribution']=dict(
            old_report_to_reader_even=(p['even']['mean_Phi']-old['mean_Phi'] if old['mean_Phi'] is not None else None),
            reader_parent_all_minus_even=p['all']['mean_Phi']-p['even']['mean_Phi'],
            reader_parent_odd_minus_even=p['odd']['mean_Phi']-p['even']['mean_Phi'],
            same_field_grid_rule_change_not_optimization=True,
            old_driver_vs_new_reader_synthesis_and_reduction_may_differ=True)
    if result['final'] is not None and result['parent']['complete'] and result['final']['complete']:
        result['complete_pair']=True
        result['same_functional_changes']={key:dict(
            final_minus_parent_Phi=result['final']['partitions'][key]['mean_Phi']-result['parent']['partitions'][key]['mean_Phi'],
            final_minus_parent_maximum=result['final']['partitions'][key]['maximum_relative_Gram']-result['parent']['partitions'][key]['maximum_relative_Gram'])
            for key in ('even','odd','all')}
        result['cross_N_final_minus_old_parent_as_optimization_used']=False
    result.update(seconds=time.monotonic()-started,
        newly_paid_scope='Finite same-carrier first-jet Gram/loss partitions only; no curvature/reach or continuous peak read',
        profile_N_independent=True,reference_profile_cache_loaded=False,
        old_input_profile_files_rewritten=False,reference_oracle_requery_by_frozen_factory=context is not None,
        angular_convergence_demonstrated=False,frequency_bottleneck_claimed=False,
        topic_completion_certified=False)
    h.write_json(out,result)
    return out,result


def execute(args,state):
    h=state['history'];p=state['plan'];h.require_actions()
    p.update(scientific_execution_started=True,stage='validating_unchanged_inputs',
        execution={key:os.environ.get(key) for key in ('GITHUB_REPOSITORY','GITHUB_RUN_ID','GITHUB_RUN_ATTEMPT','GITHUB_SHA')})
    h.write_json(state['plan_path'],p)
    arrays=validate_arrays(args,state)
    p.update(scientific_arrays_read=True,positions=materialize_positions(args,state))
    final_bundle=final_report=None
    solver_return=None
    if args.readout_only:
        if args.final_report is not None:
            final_report=json.loads(args.final_report.read_text());final_bundle=args.final_bundle
            p['actual_final_binding']=check_final(args,state,final_report,final_bundle,args.final_source)
    else:
        p['stage']='same_space_new_N_full_QP_started';h.write_json(state['plan_path'],p)
        environment=os.environ.copy()
        for key in ('GITHUB_TOKEN','GH_TOKEN','TASK_GITHUB_TOKEN'):
            environment.pop(key,None)
        environment.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
        started=time.monotonic()
        returned=subprocess.run(state['command'],env=environment,cwd=args.repo)
        solver_return=dict(returncode=returned.returncode,seconds=time.monotonic()-started,
            naturally_complete=False)
        report_path=args.outdir/'solve/report.json'
        if report_path.is_file():
            solver_return['report']=h.file_record(report_path)
        if returned.returncode==0:
            final_report=json.loads(report_path.read_text());final_bundle=args.outdir/'solve/final.npz'
            p['actual_final_binding']=check_final(args,state,final_report,final_bundle,Path(p['driver']['path']))
            solver_return.update(naturally_complete=True,final_bundle=h.file_record(final_bundle),
                actual_direction_count=len(final_report['directions']),
                accepted_direction_count=sum(bool(row['accepted']) for row in final_report['directions']),
                terminal_damping=p['actual_final_binding']['damping'],
                final_new_grid_geometry_filter=final_report.get('final_curvature_filter'))
        p['solver_return']=solver_return
    if final_report is not None:
        p['final_positions']=materialize_final_positions(args,state,final_report,final_bundle)
    p['stage']='actual_common_even_odd_readout';h.write_json(state['plan_path'],p)
    path,readout=paired_readout(args,state,arrays,final_bundle,final_report)
    for key,record in p['inputs'].items():
        if sha(record['path'])!=record['sha256']:
            raise ValueError('An original N-only input changed during execution: '+key)
    p.update(stage='readout_returned',angular_readout=h.file_record(path),
        actual_parent_partition_complete=readout['parent']['complete'],
        actual_complete_pair=readout['complete_pair'],scientific_execution_returned=True,
        complete_same_space_solve=(solver_return or {}).get('naturally_complete',False),
        continuous_metric_certified=False,topic_completion_certified=False)
    h.write_json(state['plan_path'],p)
    print(json.dumps(dict(event='N_only_returned',plan=h.file_record(state['plan_path']),
        readout=h.file_record(path),solver_return=solver_return,
        complete_pair=readout['complete_pair'],topic_completion_certified=False),allow_nan=False),flush=True)
    if solver_return is not None and solver_return['returncode']:
        raise SystemExit(solver_return['returncode'])


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ('repo','work','parent-report','bundle','carrier','node-report','scalar-input','outdir'):
        parser.add_argument('--'+key,type=Path,required=True)
    parser.add_argument('--manifest',type=Path,action='append',default=[])
    parser.add_argument('--grid-manifest',nargs=2,action='append',default=[],metavar=('OLD_FULL_N','PATH'))
    for key in ('parent-source','final-report','final-bundle','final-source'):
        parser.add_argument('--'+key,type=Path)
    parser.add_argument('--new-angles',type=int)
    parser.add_argument('--directions',type=int,default=1)
    parser.add_argument('--maxiter',type=int)
    parser.add_argument('--stage-block',type=int,default=64)
    parser.add_argument('--readout-only',action='store_true')
    parser.add_argument('--execute',action='store_true')
    args=parser.parse_args()
    if args.directions<1 or args.stage_block<1 or (args.maxiter is not None and args.maxiter<1):
        raise ValueError('Need positive declared direction/iteration/block counts')
    if bool(args.final_report)!=bool(args.final_bundle) or (args.final_source is not None and args.final_report is None):
        raise ValueError('An external actual final needs both its completed report and bundle')
    if args.final_report is not None and not args.readout_only:
        raise ValueError('External final inputs belong only to explicit readout-only mode')
    for key in ('repo','work','parent_report','bundle','carrier','node_report','scalar_input','outdir',
                'parent_source','final_report','final_bundle','final_source'):
        value=getattr(args,key)
        if value is not None:
            setattr(args,key,value.resolve())
    args.manifest=[path.resolve() for path in args.manifest]
    state=prepare(args)
    if not args.execute:
        print(json.dumps(dict(event='N_only_prepared_no_science',plan=state['history'].file_record(state['plan_path']),
            dimensions=state['plan']['dimensions'],command=state['command'],
            scientific_arrays_read=False,scientific_execution_started=False),allow_nan=False),flush=True)
        return
    try:
        execute(args,state)
    except Exception as error:
        state['plan'].update(stage='exception_no_completion_claim',
            exception=dict(type=type(error).__name__,message=str(error)),
            topic_completion_certified=False)
        state['history'].write_json(state['plan_path'],state['plan'])
        raise


if __name__=='__main__':
    main()
