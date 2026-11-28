#!/usr/bin/env python3
"""Resolve a genuine inner QR/full-DN return and start its first fixed-g step.

This first refinement preserves the actual M-specific native manifest, port,
baseline, source mean and complete physical metric. Only the runtime's three
declared execution fields are copied into a fresh file. The original complete
fixed-support solver owns all numerical gates, full tail responses and outer
iterations. No lambda-one input is fabricated or regenerated here.

The run action replaces this small resolver by the existing explicit process
owner. It creates no second supervisor or untracked numerical child. The
owner's process record, not this preparation summary, records the real return.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import argparse
import copy
import json
import math
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import qr_fixed_support_actual_model as model

INNER_SCHEMA = 'original-lambda-one-native4-chord3-outer8-prefix-qr-v1'
OWNER = HERE/'run_qr_fixed_support_actual_once.py'
REPO = HERE.parents[4]


def write(path, value):
    path = Path(path)
    temporary = path.with_name(path.name+'.tmp')
    with temporary.open('w') as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write('\n')
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)


def inside(work, path, description):
    path = Path(path).resolve()
    if work not in path.parents:
        raise ValueError(description+' must be an actual file below the explicit work tree')
    return path


def resolve(args, out):
    repo, origin, work = (Path(v).resolve() for v in
                          (args.repo, args.origin_repo, args.work))
    if repo != REPO or repo == work or repo in work.parents:
        raise ValueError('Use the executing source tree and one separate scientific work tree')
    summary_path = inside(work, args.coupling_summary, 'The inner actual-DN summary')
    summary_ref = model.ref(summary_path)
    summary = model.load(summary_path)
    # An outer launcher's summary or a design/linear run is not this schema.
    if (summary.get('schema') != INNER_SCHEMA
            or summary.get('status') != 'original_finite_true_dn_gates_passed'
            or summary.get('result', {}).get('accepted') is not True
            or not isinstance(summary.get('result', {}).get('run'), str)):
        raise ValueError('Require the genuine accepted inner actual-dn/summary.json, not a launcher or linear-design record')
    run = inside(work, summary['result']['run'], 'The final actual prefix run')
    context = model.accepted_input(run, repo=repo, origin_repo=origin,
                                   coupling_summary=summary_path)
    if context['role'] != 'accepted_original_support_qr_chord_design_actual_return':
        raise ValueError('This launcher performs only the first refinement of a genuine QR/full-DN anchor')
    source = context['record']
    M = source['modes']
    if type(M) is not int or not 1 <= M <= 64:
        raise ValueError('Keep the complete actual M and the existing native M<=64 scope')
    gates = dict(tol=args.tol,
        bc_tol=context['gates']['bc_tol'] if args.bc_tol is None else args.bc_tol,
        physical_bc_tol=(context['gates']['physical_bc_tol'] if args.physical_bc_tol is None
                         else args.physical_bc_tol))
    for key, ceiling in (('tol',1e-6),('bc_tol',1e-7),('physical_bc_tol',2e-9)):
        value = gates[key]
        if (type(value) not in (int,float) or not math.isfinite(value)
                or not 0 < value <= min(ceiling,context['gates'][key])):
            raise ValueError('An original finite gate cannot be loosened: '+key)
    if gates['tol'] >= context['gates']['tol']:
        raise ValueError('Explicit --tol must be strictly tighter than the actual anchor tolerance')
    if args.max_nodes < source['raw_return']['nodes']:
        raise ValueError('The complete actual source nodes exceed the explicit node ceiling')

    # These are the existing accepted source files, not re-exported lookalikes.
    port = inside(work, model.checked(context['port']), 'The M-specific original port')
    baseline_path = inside(work, model.checked(context['base_tail_settings']), 'The original baseline')
    runtime_path = inside(work, model.checked(context['tail_settings']), 'The actual old runtime')
    packet = inside(work, model.checked(context['final_packet']), 'The final physical-H packet')
    manifest = inside(work, model.checked(summary['native']['manifest']), 'The M-specific native manifest')
    if manifest.name != 'native-manifest.json':
        raise ValueError('The actual native directory has no original manifest filename')
    native = manifest.parent
    baseline, runtime, port_record = (model.load(p) for p in
                                     (baseline_path,runtime_path,port))
    keys = set(model.RUNTIME_CONFIG_KEYS)
    if (keys != {'traceFile','chordMaxCorrections','initialCheckpoint'}
            or any(key in baseline for key in keys)
            or {key:value for key,value in runtime.items() if key not in keys} != baseline
            or runtime.get('chordMaxCorrections') != 3
            or baseline['modes'] != M or runtime['modes'] != M
            or port_record['source']['config_sha256'] != model.sha(baseline_path)
            or port_record['modes'] != [3*j for j in range(1,M+1)]):
        raise ValueError('The actual port/baseline/runtime identity is not the unchanged complete M-specific problem')
    new_runtime = copy.deepcopy(runtime)
    new_runtime.update(initialCheckpoint=str(packet),
        traceFile=str(out/'fixed-actual-native-trace.jsonl'),chordMaxCorrections=3)
    if {key:value for key,value in new_runtime.items() if key not in keys} != baseline:
        raise ValueError('A physical or numerical baseline field changed during runtime preparation')
    angular = max(source['angular'],32*M)
    runtime_output = out/'fixed-actual-runtime.json'
    child_out = out/'fixed-actual'
    mode = '--inherit-owned-session' if args.inherit_owned_session else '--own-child-session'
    command = [sys.executable,'-u',str(OWNER),
        '--process-record',str(out/'actual-process.json'),
        '--console',str(out/'actual-console.log'),mode,'--',
        '--repo',str(repo),'--origin-repo',str(origin),'--work',str(work),
        '--source-run',str(run),'--coupling-summary',str(summary_path),
        '--native-source',str(native),'--base-tail-config',str(baseline_path),
        '--tail-config',str(runtime_output),'--port',str(port),
        '--outdir',str(child_out),'--modes',str(M),'--angular',str(angular),
        '--tol',str(gates['tol']),'--bc-tol',str(gates['bc_tol']),
        '--physical-bc-tol',str(gates['physical_bc_tol']),
        '--radial-refine',str(args.radial_refine),'--max-nodes',str(args.max_nodes),
        '--verbose',str(args.verbose)]
    sources = [Path(__file__),OWNER,HERE/'qr_fixed_support_actual_model.py',
        HERE/'qr_fixed_support_actual_step.py',HERE/'qr_fixed_support_actual_acceptance.py',
        HERE/'qr_fixed_support_actual_resources.py',model.checked(context['anchor_gate'])]
    result = dict(schema='first-fixed-g-from-actual-QR-inner-return-resolution-v1',
        source=model.ref(__file__),actual_inner_summary=summary_ref,
        actual_source_role=context['role'],required_anchor_source_kind=model.ANCHOR_SOURCE_KIND,
        complete_anchor_gate_provenance=context['complete_anchor_gate_provenance'],
        source_run=model.ref(run),raw=context['raw'],physical=context['physical'],
        final_physical_height_binding=context['final_height_binding'],
        final_physical_packet=context['final_packet'],source_port=model.ref(port),
        reused_baseline=model.ref(baseline_path),original_runtime=model.ref(runtime_path),
        native_manifest=model.ref(manifest),native_source=str(native),
        modes=M,source_angular=source['angular'],target_angular=angular,
        source_mean_nodes=context['mean_nodes'],source_gates=context['gates'],target_gates=gates,
        source_frozen_profile=source['frozen_profile'],source_core_settings=source['core_settings'],
        selected_gauge_q=source['gauge_q'],selected_warp_reference=source['warp_reference'],
        source_mean_or_metric_changed=False,original_baseline_bytes_reused=True,
        original_port_bytes_reused=True,original_native_manifest_reused=True,
        old_native_M24_assumed=False,old_mean_1168_assumed=False,
        runtime_execution_fields=list(model.RUNTIME_CONFIG_KEYS),
        changed_runtime_fields={key:dict(before=runtime.get(key),after=new_runtime[key])
                                for key in model.RUNTIME_CONFIG_KEYS},
        runtime_path=str(runtime_output),runtime_semantics_before_write=new_runtime,
        process_ownership_mode=mode[2:],actual_owner_argv=command,
        source_hashes={str(path.resolve()):model.sha(path) for path in sources},
        initial_guess_constructed=False,new_native_preparation_executed=False,
        numerical_child_started=False,actual_fixed_g_accepted=False,
        continuous_certificate_inherited=False,readme_completion_claimed=False)
    if model.ref(summary_path) != summary_ref:
        raise ValueError('The accepted inner summary changed while resolving its real source')
    return result,new_runtime,command


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=('resolve','run'))
    for key in ('repo','origin-repo','work','coupling-summary','outdir'):
        parser.add_argument('--'+key,type=Path,required=True)
    parser.add_argument('--tol',type=float,required=True)
    parser.add_argument('--bc-tol',type=float)
    parser.add_argument('--physical-bc-tol',type=float)
    parser.add_argument('--radial-refine',type=int,default=1)
    parser.add_argument('--max-nodes',type=int,default=6000)
    parser.add_argument('--verbose',type=int,default=2)
    owner = parser.add_mutually_exclusive_group(required=True)
    owner.add_argument('--own-child-session',action='store_true')
    owner.add_argument('--inherit-owned-session',action='store_true')
    args = parser.parse_args()
    work,out = Path(args.work).resolve(),Path(args.outdir).resolve()
    if (work not in out.parents or out == REPO or REPO in out.parents
            or args.radial_refine < 1 or args.max_nodes < 2):
        raise ValueError('Use a fresh outside-repository work output and complete positive refinement')
    if os.environ.get('GITHUB_ACTIONS') == 'true' and not args.inherit_owned_session:
        raise ValueError('In CI inherit its actual outer-owned session explicitly')
    out.mkdir(parents=True,exist_ok=False)
    summary_path = out/'summary.json'
    state = dict(schema='first-fixed-g-from-actual-QR-inner-return-entry-v1',
        source=model.ref(__file__),argv=[sys.executable,*sys.argv],action=args.action,
        status='checking_real_inner_actual_DN_anchor',numerical_child_started=False,
        delegation_attempted=False,actual_fixed_g_accepted=False,
        original_design_recomputed=False,complete_surface=False)
    write(summary_path,state)
    try:
        resolution,runtime,command = resolve(args,out)
        runtime_path = out/'fixed-actual-runtime.json'
        write(runtime_path,runtime)
        resolution['prepared_runtime'] = model.ref(runtime_path)
        write(out/'source-resolution.json',resolution)
        state.update(status='genuine_QR_anchor_and_first_fixed_g_command_resolved',
            source_resolution=model.ref(out/'source-resolution.json'),
            original_owner_argv=command,actual_process_record=str(out/'actual-process.json'),
            actual_fixed_run=str(out/'fixed-actual/run.json'))
        write(summary_path,state)
        if args.action == 'resolve':
            print(json.dumps(dict(status=state['status'],resolution=state['source_resolution'])),flush=True)
            return 0
        state.update(status='delegating_to_original_explicit_fixed_actual_process_owner',
            delegation_attempted=True,
            terminal_evidence='The actual-process.json owner record and own-KIND fixed-actual/run.json decide the real terminal and mathematical result; this is only preparation.')
        write(summary_path,state)
        # One owner process replaces this resolver; no Popen supervisor is added.
        os.execv(sys.executable,command)
        raise RuntimeError('The process-owner exec unexpectedly returned')
    except Exception as error:
        state.update(status='genuine_QR_anchor_not_resolved_or_owner_not_executed',
            error=repr(error),numerical_child_started=False,actual_fixed_g_accepted=False)
        write(summary_path,state)
        print(json.dumps(dict(status=state['status'],error=state['error'])),flush=True)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
