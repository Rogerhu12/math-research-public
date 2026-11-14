#!/usr/bin/env python3
"""Same-g true-tail BVP with explicit small-height continuation scheduling.

Select M on the command line. Keep flat17 geometry, original physical BC,
true nonlinear DN, original power2_weights(M), release-LU and direct CSC.
After a real success, small external H changes first try the complete target;
recognized failures still use the original halving and final validation.
All resulting arrays remain on disk. Finite success is not a closed-surface
or all-time metric/reach certificate.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import copy
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC/'notes'
PROFILE = NOTES/'2026-11-09-db6f-prefix-flat-v17v18-fixed-m14-d12-p8-s32-q512-outer-from14-frozen-profile.json'
CHART = NOTES/'2026-11-09-950f-prefix-adaptive-chart.json'
PORT = NOTES/'2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json'


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def require(ok, message):
    if not ok:
        raise ValueError(message)


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def identity(path):
    path = Path(path).resolve()
    return {'path':str(path),'bytes':path.stat().st_size,
            'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}


def write(path, value, exclusive=False):
    data = (json.dumps(value,indent=2,allow_nan=False)+'\n').encode()
    require(len(data) < 1_000_000, 'Run metadata unexpectedly large')
    with Path(path).open('xb' if exclusive else 'wb') as stream:
        stream.write(data)


def retain_worker_warm(path, out):
    """Read one recovery snapshot once, without relabelling it as a good DN."""
    path = path.resolve()
    raw = path.read_bytes()
    payload = gzip.decompress(raw) if path.suffix == '.gz' else raw
    record = json.loads(payload)
    response = record.get('response') or {}
    seam = record.get('seam') or {}
    checkpoint = (response.get('checkpoint') or seam.get('tail_checkpoint')
                  or record.get('checkpoint') or record)
    require(isinstance(checkpoint, dict) and isinstance(checkpoint.get('parameters'), dict)
            and isinstance(checkpoint.get('states'), list)
            and isinstance(checkpoint.get('cutHeight'), list),
            'Worker warm input has no complete shooting state and physical height label')
    # Iteration producers replace their source atomically. Retaining these
    # observed bytes makes the later worker read the same actual snapshot.
    retained = Path(str(out)+'-tail-warm-input.json.gz')
    packed = raw if path.suffix == '.gz' else gzip.compress(payload, mtime=0)
    require(len(packed) < 5_000_000, 'Worker warm snapshot exceeds file limit')
    with retained.open('xb') as stream:
        stream.write(packed)
    return retained, {
        'observed_source': {'path': str(path), 'bytes': len(raw),
                            'sha256': hashlib.sha256(raw).hexdigest()},
        'retained_input': identity(retained),
        'input_status': record.get('status'),
        'input_converged_flag': response.get('converged'),
        'input_failure': response.get('failed'),
        'input_scope': checkpoint.get('scope'),
        'input_modes': checkpoint['parameters'].get('modes'),
        'input_quadrature': checkpoint['parameters'].get('quadrature'),
        'input_nodes': len(checkpoint['states']),
        'input_cut_height': list(checkpoint['cutHeight']),
        'role': 'Worker initial guess only; any unconverged status is retained.',
        'used_as_known_successful_seed': False,
        'changes_bootstrap_or_final_height': False}


def make_progress(path):
    """Scalar run observations only; no added numerical acceptance condition."""
    started = time.monotonic()
    Path(path).open('x').close()
    def emit(event, **values):
        memory = {}
        for filename, wanted in (('/proc/self/status', ('VmRSS:', 'VmHWM:')),
                                 ('/proc/meminfo', ('MemAvailable:',))):
            try:
                for line in Path(filename).read_text().splitlines():
                    if line.startswith(wanted):
                        key, value, *_ = line.split()
                        memory[key.rstrip(':')+'_kB'] = int(value)
            except OSError:
                pass
        row = {'event': event, 'elapsed_seconds': time.monotonic()-started,
               'unix_time': time.time(), **memory, **values}
        with Path(path).open('a') as stream:
            stream.write(json.dumps(row, allow_nan=False)+'\n')
    return emit


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--modes',type=int,required=True)
    parser.add_argument('--restart',type=Path,required=True)
    parser.add_argument('--tail-seed',type=Path)
    tail_initial = parser.add_mutually_exclusive_group()
    tail_initial.add_argument('--tail-initial-checkpoint',type=Path,
                        help='Actual failure/iteration/success packet used only as worker warm; the known tail seed and requested heights stay unchanged')
    tail_initial.add_argument('--tail-cold-start',action='store_true',
                        help='Use the original rotational linear shooting initial state; the known tail packet supplies only parameters and height')
    parser.add_argument('--out-prefix',type=Path,required=True)
    parser.add_argument('--angular',type=int)
    parser.add_argument('--tail-modes',type=int,
                        help='True tail order W >= prefix M; default M')
    parser.add_argument('--tail-angular',type=int,
                        help='True tail quadrature; default next power of two covering W')
    parser.add_argument('--tail-shooting-parts', type=int,
                        help='Explicit numerical stages per raw profile; physical geometry is unchanged')
    parser.add_argument('--tail-steps', type=int,
                        help='RK steps per shooting stage; paired P16/S16 retains the old P8/S32 raw density')
    parser.add_argument('--tail-audit-steps', type=int,
                        help='Explicit final point audit samples per new stage; default rescales with P to retain the original raw density')
    parser.add_argument('--jacobian', choices=('fourier', 'original'), default='original',
                        help='Prefix state Jacobian assembly; equations and tolerances are unchanged')
    parser.add_argument('--transforms', choices=('fourier', 'original'), default='original',
                        help='Long-precision cylindrical values/project evaluation')
    parser.add_argument('--tail-jacobian', choices=('fourier', 'fourier-root', 'original'), default='original',
                        help='Actual tail variational-flow assembly; state RHS is unchanged')
    parser.add_argument('--tail-stage-workers', type=int, choices=(0, 2, 4), default=0,
                        help='Optional independent stage evaluation threads; zero preserves serial stage maps')
    parser.add_argument('--tail-predictor', choices=('tangent', 'linear'), default='linear',
                        help='Initial shooting guess only; original nonlinear acceptance remains')
    parser.add_argument('--tail-trial', choices=('momentum', 'geometric', 'geometric-centered'), default='momentum',
                        help='Newton trial curve only; the original correction, residual and acceptance remain')
    parser.add_argument('--tail-root-precision', choices=('original', 'tight'), default='original',
                        help='Implicit root/mean accuracy only; tight uses 4e-15 with 2e-14 fallback and retains the original 2e-9 shooting target')
    parser.add_argument('--bootstrap-height-scale', type=float, default=1.,
                        help='First actual DN target is this times the original warm height; continue to the unchanged requested target')
    parser.add_argument('--bootstrap-from-initial-checkpoint', action='store_true',
                        help='Use the actual retained warm cutHeight as the first true DN target, preserving its binary components; the known successful seed still supplies physical parameters and the final prefix target is unchanged')
    parser.add_argument('--direct-relative-limit', type=float, default=0.01,
                        help='After actual finite success, try the complete new H target first when its relative infinity change is at most this value')
    parser.add_argument('--max-nodes',type=int,default=8000)
    parser.add_argument('--source-root',type=Path,default=TOPIC/'repro/source-root')
    parser.add_argument('--data-gib',type=float,default=6.)
    parser.add_argument('--node-heap',type=int,default=1536)
    parser.add_argument('--prepare-only',action='store_true',
                        help='Construct the actual padded initial guess and print scalar diagnostics; no DN/BVP')
    parser.add_argument('--tail-only',action='store_true',
                        help='Solve the actual wider-DN bootstrap once and exit before any prefix BVP')
    args = parser.parse_args()
    require(args.tail_seed is not None, 'This continuation entry needs an explicit actual successful --tail-seed, also when restarting an outer-UNSOLVED inner snapshot')
    require(not args.bootstrap_from_initial_checkpoint or args.tail_initial_checkpoint is not None,
            'Exact warm-height bootstrap requires an actual --tail-initial-checkpoint')
    require(0 < args.direct_relative_limit <= 1., 'direct-relative-limit must be finite in (0,1]')
    args.restart = args.restart.resolve()
    args.out_prefix = args.out_prefix.resolve()
    args.source_root = args.source_root.resolve()
    require(args.modes > 0 and args.max_nodes >= 3 and args.data_gib > 0, 'Invalid numerical/resource setting')
    require(0 < args.bootstrap_height_scale <= 1., 'Bootstrap height scale must lie in (0,1]')
    require(not (args.prepare_only and args.tail_only), 'Choose only one partial execution mode')
    os.environ['VISIBLE_FLEX_TAIL_STAGE_WORKERS'] = str(args.tail_stage_workers)
    os.environ['VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND'] = args.tail_jacobian
    os.environ['VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND'] = args.tail_predictor
    os.environ['VISIBLE_FLEX_TAIL_TRIAL_BACKEND'] = args.tail_trial
    os.environ['VISIBLE_FLEX_TAIL_ROOT_PRECISION'] = args.tail_root_precision
    need = max(512,8*(3*args.modes+1))
    N = args.angular if args.angular is not None else 1 << (need-1).bit_length()
    require(N >= need, 'Use angular >= max(512, 8*(3*M+1))')
    W = args.tail_modes if args.tail_modes is not None else args.modes
    tail_need = max(512, 8*(3*W+1))
    NT = args.tail_angular if args.tail_angular is not None else 1 << (tail_need-1).bit_length()
    # The tail engine needs N > 4*spacing*W. The former 8*(3W+1)
    # heuristic remains the automatic default, not a restriction on an
    # explicitly chosen N512 at W22. Prefix basis requirements are separate.
    require(W >= args.modes and NT >= 512 and NT > 4*3*W,
            'W must cover M and have sufficient true-tail quadrature')
    limit = int(args.data_gib*1024**3)
    resource.setrlimit(resource.RLIMIT_DATA,(limit,limit))
    resource.setrlimit(resource.RLIMIT_FSIZE,(4_999_999,4_999_999))
    out = args.out_prefix
    require(out.parent.is_dir(), 'Output directory does not exist')
    require(not list(out.parent.glob(out.name+'*')), 'Output prefix has already been used')
    seed = read(args.restart)
    profile, chart, port = read(PROFILE), read(CHART), read(PORT)
    require(seed['frozen_profile'] == profile and seed['chart'] == chart
            and seed['gauge_amplitude'] == .1 and seed['warp_reference_q'] == .1
            and seed['physical_tail_parameters'] == port['parameters']
            and seed['physical_tail_cut'] == port['cut'], 'Input changes the fixed physical geometry')
    require(seed['config']['modes'] <= args.modes <= W <= len(port['linearSlope']), 'Unsupported refinement order')
    if args.tail_seed is None:
        args.tail_seed = args.restart.parent/seed['tail_seam']['tail_record']
    args.tail_seed = args.tail_seed.resolve()
    prior = read(args.tail_seed)
    require(prior['response'].get('converged') is True, 'Initial tail packet is not a real successful finite DN')
    require(prior['response']['checkpoint']['parameters']['modes'] <= W,
            'Tail seed has a higher Fourier order than requested')
    worker_warm, warm_metadata = args.tail_seed, None
    if args.tail_cold_start:
        worker_warm = None
        warm_metadata = {
            'cold_start': True,
            'initial_state_constructor': 'original dn.tail.initial at the actual first requested height',
            'known_packet_role': 'Physical parameters and original height only; no saved shooting state is loaded.',
            'used_as_known_successful_seed': False,
            'changes_bootstrap_or_final_height': False}
    elif args.tail_initial_checkpoint is not None:
        worker_warm, warm_metadata = retain_worker_warm(args.tail_initial_checkpoint, out)
    config = copy.deepcopy(prior['config'])
    config.update(modes=W,quadrature=NT,
        traceFile=str(out)+'_tail-trace.jsonl',
        iterationCheckpointFile=str(out)+'_tail-iteration.json.gz',
        trialDiagnosticFile=str(out)+'_tail-trials.jsonl',
        trialStatePrefix=str(out)+'_tail-trial')
    old_parts, old_steps = prior['config']['shootingParts'], prior['config']['steps']
    parts = old_parts if args.tail_shooting_parts is None else args.tail_shooting_parts
    steps = old_steps if args.tail_steps is None else args.tail_steps
    old_audit = prior['config'].get('auditSteps', old_steps)
    require(parts > 0 and steps > 0, 'Tail partition and RK steps must be positive')
    if args.tail_audit_steps is None:
        require(old_parts*old_audit % parts == 0,
                'Specify integral --tail-audit-steps for this numerical partition')
        audit_steps = old_parts*old_audit//parts
    else:
        audit_steps = args.tail_audit_steps
    require(audit_steps > 0, 'Tail audit steps must be positive')
    partition_refinement = parts != old_parts
    if partition_refinement:
        require(parts > old_parts and parts % old_parts == 0 and parts*steps == old_parts*old_steps,
                'This explicit partition route retains the old raw RK density under integral refinement')
    config.update(shootingParts=parts, steps=steps, auditSteps=audit_steps)
    tail_grid = {'shootingParts': parts, 'steps': steps, 'auditSteps': audit_steps,
                 'oldShootingParts': old_parts, 'oldSteps': old_steps, 'oldAuditSteps': old_audit,
                 'nominalRKStepsPerRawProfile': parts*steps,
                 'nominalAuditStepsPerRawProfile': parts*audit_steps,
                 'partition_refinement': partition_refinement,
                 'scope': 'Numerical shooting partition, RK and audit grid only; same physical metric and final target.'}
    os.environ['VISIBLE_FLEX_TAIL_PARTITION_REFINEMENT'] = '1' if partition_refinement else '0'
    if args.tail_cold_start:
        config.pop('initialCheckpoint', None)
    else:
        config['initialCheckpoint'] = str(worker_warm)
    require(config['solveTolerance'] == 2e-9 and config['maxIterations'] == 36
            and config['sharedEngines'] is True, 'Unexpected original finite DN policy')
    for key,value in port['parameters'].items():
        require(config.get(key) == value, 'Tail changes the fixed physical parameter: '+key)
    import numpy as np
    client_selection = module('generic_mode_client_selection', HERE/'fd2d-prefix-tail-parallel-client.py')
    tail_implementation = client_selection.implementation(args.tail_jacobian, args.tail_predictor,
                                                          args.tail_trial, args.tail_root_precision,
                                                          partition_refinement, args.tail_stage_workers)
    flat = module('generic_mode_flat_runner', HERE/'db6f-prefix-flat-coupled.py')
    runner = flat.m
    pre_backend_builder = runner.adaptive.build_classes
    jacobian_source = HERE/'950f-prefix-adaptive-chart-bvp-v2.py'
    if args.jacobian == 'fourier':
        jacobian_source = HERE/'78718-prefix-fourier-jacobian.py'
        fourier_jacobian = module('generic_mode_fourier_jacobian', jacobian_source)
        fourier_jacobian.install(runner.adaptive)
    transform_source = HERE/'950f-prefix-adaptive-chart-bvp-v2.py'
    if args.transforms == 'fourier':
        transform_source = HERE/'78718-prefix-long-fourier-transforms.py'
        fourier_transforms = module('generic_mode_long_fourier_transforms', transform_source)
        fourier_transforms.install(runner.adaptive)
    runner.adaptive.old.install_source(args.source_root)
    from curve_stable_prefix_bvp import load_checkpoint
    _, Base = runner.adaptive.build_classes(chart)
    class BVP(runner.TailMixin,Base):
        pass
    port_with_sha = dict(port,_sha256=identity(PORT)['sha256'])
    obj = BVP(profile,port_with_sha,.1,args.modes,N,True,.1)
    obj.bcweights = np.full(args.modes,2e-11/1e-8)
    restart = module('generic_mode_saved_mesh_restart',HERE/'db6f-prefix-preserve-restart.py')
    x,y,p,info = restart.restart(obj,args.restart,chart)
    require(len(x) <= args.max_nodes, 'Initial saved mesh exceeds requested max_nodes')
    target = np.zeros(W)
    target[:args.modes] = obj.bridge.sigma*obj.q*y[obj.iz:,-1]
    old_target = np.zeros(W)
    old_values = prior['response']['checkpoint']['cutHeight']
    old_target[:len(old_values)] = old_values
    bootstrap_height_override = None
    if args.bootstrap_from_initial_checkpoint:
        bootstrap_height_override = list(warm_metadata['input_cut_height'])
        require(len(bootstrap_height_override) == W
                and np.all(np.isfinite(np.asarray(bootstrap_height_override, dtype=float))),
                'Actual warm-height override must have the complete requested tail order')
    first_bootstrap_target = (np.asarray(bootstrap_height_override, dtype=float)
                              if bootstrap_height_override is not None
                              else args.bootstrap_height_scale*old_target)
    spectral = module('generic_mode_power2_solver',HERE/'db6f-root-spectral-collocation-v2.py')
    weights = spectral.power2_weights(args.modes)
    preparation = {'status':'ACTUAL_INITIAL_GUESS_PREPARED_ONLY','modes':args.modes,
        'angular':N,'tail_modes':W,'tail_angular':NT,
        'state_components':len(weights),'maximum_weight':float(weights.max()),
        'initial_nodes':len(x),'maximum_nodes':args.max_nodes,
        'initial_height_max':float(np.max(np.abs(target))),
        'height_difference_from_padded_tail_seed_max':float(np.max(np.abs(target-old_target))),
        'bootstrap_height_scale': args.bootstrap_height_scale,
        'first_actual_bootstrap_height_max': float(np.max(np.abs(first_bootstrap_target))),
        'bootstrap_height_source': ('actual-retained-initial-checkpoint-cutHeight'
                                    if bootstrap_height_override is not None else 'scaled-known-successful-seed'),
        'bootstrap_height_scale_applied': bootstrap_height_override is None,
        'bootstrap_changes_final_requested_height': False,
        'small_height_continuation': {'direct_relative_limit': args.direct_relative_limit,
            'selection_requires_actual_successful_origin': True,
            'bootstrap_is_actually_solved': True, 'direct_initial_step': '1',
            'ordinary_initial_step': '1/8', 'minimum_step': '1/1024',
            'scope': 'Only target scheduling changes; all original residual, floor, physical and final validation conditions remain.'},
        'worker_warm_input': warm_metadata,
        'tail_cold_start': args.tail_cold_start,
        'tail_shooting_grid': tail_grid,
        'restart_diagnostics':info,'source_prefix_was_successful':seed.get('solver_success') is True,
        'scope':'Mode padding, original inlet correction and initial guess only; no new DN or BVP.'}
    # Do not retain a duplicate large initial state while original main loads it.
    del obj,x,y,p,Base,BVP
    config_path = Path(str(out)+'-tail-config.json')
    argv = [str(HERE/'db6f-prefix-flat-coupled.py'),
        '--source-root',str(args.source_root),'--profile',str(PROFILE),
        '--chart',str(CHART),'--linear-port',str(PORT),
        '--tail-config',str(config_path),'--out-prefix',str(out),'--restart',str(args.restart),
        '--amplitude','0.1','--warp-reference','0.1','--modes',str(args.modes),
        '--angular',str(N),'--audit-angular',str(max(1024,16*(3*args.modes+1))),
        '--nodes','1601','--max-nodes',str(args.max_nodes),'--tol','2e-9',
        '--bc-tol','1e-8','--physical-bc-tol','2e-11','--node-heap',str(args.node_heap),
        '--fixed','--warmup-scales','--lagged-tail','--preserve-restart-mesh']
    run = {'scope':__doc__,'argv':sys.argv[:],'delegated_original_argv':argv,
        'preparation':preparation,'fixed_inputs':[identity(p) for p in
            dict.fromkeys((PROFILE,CHART,PORT,args.restart,args.tail_seed,worker_warm)) if p is not None],
        'script':identity(__file__),'source_files':[identity(HERE/name) for name in
            ('fd2d-tail-parallel-continuation.py','78718-small-height-continuation.py',
             '78718-prefix-tail-linear-m15q512-v1.py',
             'fd2d-prefix-tail-parallel-client.py','78718-prefix-tail-geometric-worker.mjs',
             '78718-tail-geometric-warm-remesh.mjs','78718-prefix-projected-tail.py',
             '78718-prefix-inner-snapshot.py',
             'db6f-prefix-flat-coupled.py','db6f-prefix-coupled.py',
             'db6f-prefix-preserve-restart.py','db6f-root-spectral-collocation-v2.py',
             'db6f-prefix-domain-newton-release-lu.py','db6f-prefix-direct-csc-foundation-v2.py')],
        'settings':{'M':args.modes,'N':N,'tail_modes':W,'tail_angular':NT,'tol':2e-9,'bc_tol':1e-8,
                    'physical_bc_tol':2e-11,'max_nodes':args.max_nodes,
                    'tail_stage_workers':args.tail_stage_workers,
                    'tail_shooting_parts':parts,'tail_steps_per_stage':steps,
                    'tail_audit_steps_per_stage':audit_steps,
                    'data_bytes_per_process':limit,'node_heap_mib':args.node_heap},
        'jacobian_backend': {'name': args.jacobian, 'source': identity(jacobian_source),
            'scope': 'Prefix Jacobian assembly only; the original RHS, BC, physical metric and tolerances remain.'},
        'transform_backend': {'name': args.transforms, 'source': identity(transform_source),
            'scope': 'Same finite cylindrical synthesis/projection; long precision and separate complex parts.'},
        'tail_stage_evaluation': {'workers': args.tail_stage_workers,
            'backend': 'visible-flex-independent-stage-pool-v2-multi' if args.tail_stage_workers else 'original-serial',
            'policy': 'ascending dynamic claims; stop above observed failure; minimum failure; original ordered reduction',
            'threads_released_before_each_DN_response': True,
            'within_stage_root_RK_equations_unchanged': True},
        'tail_jacobian_backend': {'name': args.tail_jacobian,
            'worker': identity(HERE/tail_implementation['worker']),
            'additional_sources': [identity(HERE/name) for name in
                tail_implementation['additional_sources']]},
        'tail_predictor': {'name': args.tail_predictor,
            'expected_ready_label': tail_implementation['predictor_label'],
            'scope': 'Warm initial guess only; no changed shooting residual, guard or tolerance.'},
        'tail_trial': {'name': args.tail_trial,
            'expected_ready_label': tail_implementation['trial_label'],
            'scope': 'Same Newton direction with an optional Q/L trial curve; the original residual and acceptance decide.'},
        'tail_root_precision': {'name': args.tail_root_precision,
            'expected_ready_label': tail_implementation['root_precision_label'],
            'nominal_relative_tolerance': 4e-15 if args.tail_root_precision == 'tight' else 8e-14,
            'fallback_relative_tolerance': 2e-14 if args.tail_root_precision == 'tight' else 5e-12,
            'mean_relative_tolerance': 4e-15 if args.tail_root_precision == 'tight' else 8e-14,
            'scope': 'More accurate implicit arithmetic solve only; no changed physical equation, projection floor or shooting success criterion.'},
        'small_height_continuation': {'direct_relative_limit': args.direct_relative_limit,
            'selection_requires_actual_successful_origin': True,
            'bootstrap_is_actually_solved': True, 'direct_initial_step': '1',
            'ordinary_initial_step': '1/8', 'minimum_step': '1/1024',
            'scope': 'Only target scheduling changes; all original residual, floor, physical and final validation conditions remain.'},
        'worker_warm_input': warm_metadata,
        'tail_cold_start': args.tail_cold_start,
        'tail_shooting_grid': tail_grid,
        'bootstrap': {'height_scale': args.bootstrap_height_scale,
            'height_override': bootstrap_height_override,
            'height_scale_applied': bootstrap_height_override is None,
            'scope': 'Only the first actual DN request target may use the explicitly selected retained warm cutHeight; otherwise it uses the scaled known seed. The old successful packet remains an unchanged parameter source, and original continuation must return the unchanged prefix target.',
            'physical_metric_or_final_height_changed': False,
            'old_response_is_not_relabelled': True},
        'finite_success':False,'closed_surface_success':False}
    run_path = Path(str(out)+'-mode-run.json')
    if args.prepare_only:
        run['status'] = 'PREPARED_WITHOUT_SOLVER'
        write(run_path,run,exclusive=True)
        print(json.dumps({'status':run['status'],'report':identity(run_path),
            **{k:preparation[k] for k in ('modes','angular','tail_modes','tail_angular','initial_nodes',
                 'height_difference_from_padded_tail_seed_max','maximum_weight')},
            'solver_calls':0}),flush=True)
        return 0
    adapter = module('generic_mode_actual_tail',HERE/'fd2d-tail-parallel-continuation.py')
    policy = {'record_prefix':str(out)+'_tail','journal_file':str(out)+'_tail-control.jsonl',
              'last_good_file':str(out)+'_tail-last-good.json',
              'bootstrap_height_scale': args.bootstrap_height_scale,
              'bootstrap_height_override': bootstrap_height_override,
              'known_seed_packet': str(args.tail_seed),
              'worker_warm_input': warm_metadata,
              'tail_cold_start': args.tail_cold_start,
              'tail_trial': args.tail_trial,
              'tail_stage_workers': args.tail_stage_workers,
              'small_height_continuation': dict(run['small_height_continuation']),
              'tail_shooting_grid': tail_grid,
              'control':dict(adapter.c.CONTROL),
              'scope':'Actual same-g Fourier continuation; all added modes are initial guesses until solved.'}
    write(config_path,config,exclusive=True)
    write(Path(str(out)+'_tail-continuation.json'),policy,exclusive=True)
    emit = make_progress(Path(str(out)+'-progress.jsonl'))
    emit('prepared', prefix_modes=args.modes, tail_modes=W, prefix_angular=N,
         tail_angular=NT, initial_nodes=preparation['initial_nodes'], jacobian=args.jacobian,
         transforms=args.transforms, tail_jacobian=args.tail_jacobian,
         tail_stage_workers=args.tail_stage_workers,
         tail_predictor=args.tail_predictor, tail_trial=args.tail_trial,
         tail_root_precision=args.tail_root_precision,
         tail_shooting_parts=parts, tail_steps_per_stage=steps,
         tail_audit_steps_per_stage=audit_steps)
    class ObservedPort(adapter.WeightedTailPort):
        def __init__(self, *values, **kwargs):
            emit('tail-initialize-start', tail_modes=W, angular=NT)
            super().__init__(*values, **kwargs)
            warm = self.ready.get('warmEmbedding')
            run['actual_warm_embedding'] = warm
            run['actual_tail_jacobian_backend'] = self.ready.get('tailJacobian', 'original')
            run['actual_tail_predictor'] = self.ready.get('tailPredictor', 'linear-amplitude-and-boundary-v1')
            run['actual_amplitude_warm'] = self.ready.get('amplitudeWarm', 'legacy-momentum-scaling')
            run['actual_tail_stage_workers'] = self.ready.get('tailStageWorkers', 0)
            run['actual_tail_stage_evaluation'] = self.ready.get('tailStageEvaluation', 'original-serial')
            run['actual_tail_trial'] = self.ready.get('tailTrial', 'linear-momentum-trial-v1')
            run['actual_tail_root_precision'] = self.ready.get('tailRootPrecision', 'original-8e-14-fallback-5e-12')
            write(run_path, run)
            emit('tail-initialize-end', tail_modes=self.M, warm_embedding=warm,
                 tail_jacobian=self.ready.get('tailJacobian', 'original'),
                 tail_predictor=run['actual_tail_predictor'],
                 amplitude_warm=run['actual_amplitude_warm'],
                 tail_trial=run['actual_tail_trial'],
                 tail_root_precision=run['actual_tail_root_precision'])
        def solve(self, height, jacobian=True, audit=False):
            emit('tail-request-start', physical_calls=self.calls,
                 jacobian=jacobian, audit=audit)
            start = time.monotonic()
            try:
                result = super().solve(height, jacobian=jacobian, audit=audit)
            except Exception as error:
                emit('tail-request-failed', seconds=time.monotonic()-start,
                     physical_calls=self.calls, error=repr(error))
                raise
            emit('tail-request-end', seconds=time.monotonic()-start,
                 physical_calls=self.calls, residual=result['residual'])
            packet_path = Path(str(out)+f'_tail_{self.calls:04d}.json.gz')
            if packet_path.is_file():
                run['last_actual_tail_packet'] = identity(packet_path)
            return result
    if args.tail_only:
        port, code = None, 2
        run.update(status='ACTUAL_TRUE_DN_BOOTSTRAP_RUNNING', tail_only=True, solver_calls=0)
        write(run_path, run, exclusive=True)
        start = time.monotonic()
        try:
            port = ObservedPort(config_path, args.source_root,
                                Path(str(out)+'_tail'), node_heap=args.node_heap)
            response = port.solve(target, jacobian=False, audit=False)
            adapter.c.validate_response(response, W, port.parameters, 2e-9, False, False)
            require(response['converged'] is True, 'Actual warm bootstrap did not converge')
            packet_path = Path(str(out)+f'_tail_{port.calls:04d}.json.gz')
            run.update(status='ACTUAL_TRUE_DN_BOOTSTRAP_SUCCESS_ONLY',
                actual_tail_residual=response['residual'], tail_calls=port.calls,
                warm_packet=identity(packet_path), prefix_solver_calls=0,
                scope='Real finite DN warm state only; no new prefix solution or final audited seam.')
            code = 0
        except Exception as error:
            run.update(status='ACTUAL_TRUE_DN_BOOTSTRAP_NOT_COMPLETED', error=repr(error))
        finally:
            if port is not None:
                port.close()
            run['seconds'] = time.monotonic()-start
            run['child_peak_rss_kB'] = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
            run['requested_process_exit_code'] = code
            write(run_path, run)
            emit('tail-only-completed', requested_exit_code=code, seconds=run['seconds'])
        print(json.dumps({'status': run['status'], 'report': identity(run_path),
                          'requested_exit_code': code, 'prefix_solver_calls': 0,
                          'finite_coupled_success': False}), flush=True)
        return code
    original_module = runner.module
    def select_client(name,file):
        if Path(file).resolve() == (HERE/'db6f-prefix-tail-shared-client.py').resolve():
            return SimpleNamespace(WeightedTailPort=ObservedPort)
        return original_module(name,file)
    runner.module = select_client
    original_build_classes = runner.adaptive.build_classes
    def observed_build_classes(chart):
        Flow, Base = original_build_classes(chart)
        class ObservedBase(Base):
            def fun_jac(self, s, y, p):
                emit('rhs-jacobian-start', nodes=len(s), state_components=len(y))
                start = time.monotonic()
                result = super().fun_jac(s, y, p)
                emit('rhs-jacobian-end', nodes=len(s), seconds=time.monotonic()-start)
                return result
        return Flow, ObservedBase
    runner.adaptive.build_classes = observed_build_classes
    import scipy.integrate._bvp as backend
    import f6curve_domain_newton as original_newton
    selected_newton = module('generic_mode_release_lu',HERE/'db6f-prefix-domain-newton-release-lu.py')
    old_stats = original_newton.STATS
    class ObservedStats(dict):
        def __setitem__(self, key, value):
            super().__setitem__(key, value)
            if key in ('calls', 'accepted_steps', 'no_step'):
                emit('newton-counter', counter=key, value=value,
                     newton_calls=self.get('calls', 0), accepted_steps=self.get('accepted_steps', 0))
    original_newton.STATS = selected_newton.STATS = ObservedStats(old_stats)
    original_splu = selected_newton.splu
    def observed_splu(matrix, *values, **kwargs):
        emit('lu-factor-start', dimension=matrix.shape[0], explicit_nnz=matrix.nnz)
        start = time.monotonic()
        result = original_splu(matrix, *values, **kwargs)
        emit('lu-factor-end', seconds=time.monotonic()-start,
             factor_nnz=result.nnz)
        return result
    selected_newton.splu = observed_splu
    foundation = module('generic_mode_csc_foundation',HERE/'db6f-prefix-direct-csc-foundation-v2.py')
    csc = foundation.make_functions(backend)
    old_prepare, old_newton = backend.prepare_sys, backend.solve_newton
    backend.prepare_sys = csc.prepare_sys
    selected_solver, records = spectral.make_solver(weights)
    snapshots = module('generic_mode_inner_snapshot', HERE/'78718-prefix-inner-snapshot.py')
    def solve(fun,bc,x,y,p,**kwargs):
        backend.solve_newton = selected_newton.solve_newton
        run['status'] = 'ACTUAL_INNER_BVP_RUNNING'
        run['inner_calls'] = records
        write(run_path,run)
        emit('inner-bvp-start', nodes=len(x), state_components=len(y), parameters=len(p))
        result = selected_solver(fun,bc,x,y,p,**kwargs)
        run['inner_calls'] = records
        write(run_path,run)
        emit('inner-bvp-end', success=bool(result.success), nodes=len(result.x),
             rms_max=float(np.max(result.rms_residuals)))
        emit('inner-snapshot-start', inner_call=len(records), nodes=len(result.x))
        try:
            snapshot = snapshots.save_inner_candidate(fun.__self__, result,
                prefix=out, number=len(records), chart=chart, tail_config=config,
                tail_modes=W, input_restart=identity(args.restart),
                preceding_tail=run.get('last_actual_tail_packet'),
                solver_record=records[-1])
            run.setdefault('inner_snapshots', []).append(snapshot)
            emit('inner-snapshot-saved', inner_call=len(records),
                 physical_candidate=snapshot['physical_candidate'],
                 seconds=snapshot['seconds'], outer_status='UNSOLVED')
        except Exception as error:
            # A diagnostic save must not change the original outer algorithm.
            snapshot = {'status': 'INNER_SNAPSHOT_NOT_COMPLETED',
                        'inner_call': len(records), 'error': repr(error),
                        'does_not_change_inner_or_outer_result': True}
            run.setdefault('inner_snapshots', []).append(snapshot)
            emit('inner-snapshot-failed', **snapshot)
        write(run_path,run)
        return result
    runner.solve_bvp = solve
    previous_argv = sys.argv[:]
    start = time.monotonic()
    run['status'] = 'ACTUAL_TRUE_DN_AND_BVP_RUNNING'
    write(run_path,run,exclusive=True)
    code = 2
    try:
        sys.argv = argv
        if W == args.modes:
            runner.main()
        else:
            mixed = module('generic_projected_tail_main', HERE/'78718-prefix-projected-tail.py')
            mixed.main(runner)
        cp_path = Path(str(out)+'.json.gz')
        summary = read(Path(str(out)+'-summary.json'))
        require(summary.get('error') is None and summary.get('solver_success') is True,
                'Original coupled solver did not succeed')
        cp = load_checkpoint(cp_path)
        require(cp['frozen_profile'] == profile and cp['chart'] == chart
                and cp['config']['modes'] == args.modes, 'Output changed the physical geometry or mode order')
        require(records and all(r.get('success') and r.get('original_physical_residual_gate_passed')
                                for r in records), 'Original physical inner residual did not pass')
        require(0 <= cp['max_rms_collocation_residual'] <= 2e-9, 'Original RMS tolerance did not pass')
        outer = cp['actual_outer_checks']
        require(outer and outer[-1]['inner_success'] is True
                and 0 <= outer[-1]['actual_boundary_residual'] <= 1e-8
                and 0 <= outer[-1]['actual_tail_residual'] < 2e-9,
                'Original actual nonlinear outer BC did not pass')
        require(0 <= cp['summary']['physical_bc_max'] <= 2e-11,
                'Physical terminal BC did not pass')
        final_path = out.parent/cp['tail_seam']['tail_record']
        require(final_path == Path(str(out)+f"_tail_{cp['tail_calls']:04d}.json.gz"),
                'Final seam refers to a different run')
        packet = read(final_path)
        require(packet['request']['jacobian'] is True and packet['request']['audit'] is True,
                'Final actual tail lacks the original requested Jacobian or audit')
        params = packet['response']['checkpoint']['parameters']
        adapter.c.validate_response(packet['response'],W,params,2e-9,True,True)
        require(packet['response']['converged'] is True
                and cp['tail_seam'].get('full_tail_jets',cp['tail_seam']['tail_jets']) == packet['response']['jets'],
                'Saved seam differs from the actual final tail')
        run.update(status='ACTUAL_FINITE_COUPLED_SUCCESS',finite_success=True,
            checkpoint=identity(cp_path),own_final_tail=identity(final_path),
            physical_rms=cp['max_rms_collocation_residual'],
            physical_bc=cp['summary']['physical_bc_max'],
            sampled_metric_diagnostic=cp['summary']['metric_l1'],
            actual_tail_residual=packet['response']['residual'],
            tail_calls=cp['tail_calls'],final_nodes=cp['nodes'])
        code = 0
    except Exception as error:
        run.update(status='ACTUAL_FINITE_COUPLED_NOT_COMPLETED',error=repr(error))
    finally:
        sys.argv = previous_argv
        backend.prepare_sys, backend.solve_newton = old_prepare,old_newton
        runner.module = original_module
        runner.adaptive.build_classes = pre_backend_builder
        original_newton.STATS = old_stats
        run['seconds'] = time.monotonic()-start
        run['inner_calls'] = records
        run['requested_process_exit_code'] = code
        write(run_path,run)
        emit('coupled-run-completed', requested_exit_code=code, seconds=run['seconds'])
    print(json.dumps({k:run[k] for k in ('status','finite_success','seconds')}
        | {'report':identity(run_path),'requested_exit_code':code,
           'closed_surface_success':False}),flush=True)
    return code


if __name__ == '__main__':
    sys.exit(main())
