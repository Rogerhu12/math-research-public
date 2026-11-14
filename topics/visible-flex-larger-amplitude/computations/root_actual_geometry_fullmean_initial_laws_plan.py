#!/usr/bin/env python3
"""Prepare complete-mean finite geometry fields from one accepted actual state.

Baseline-only preparation is allowed before the new response has finished.
Afterward the same prefix/grid can receive a complete two-sided variable-control plan; baseline
has no response-data dependency and is never recomputed merely to fill a plan.
The reviewed neutral list is explicit; default controls are vu, first-turn K, k0, and degree22 inlet frontload, each from the same newly computed actual core-held response.
No column from a different accepted baseline may be imported.
Every case is an unsolved actual-J warm diagnostic, not a new accepted BVP.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys

for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'

import numpy as np
from root_neck_chart import NeckChart
from strong_actual_fixed_control_response import raw_flat


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)



REVIEWED_NEUTRALS=('vu','vd','start_acceleration','descending_turn_curvature',
                  'descending_sync_curvature','coast_outward','loop_ratio','initial_speed_frontload')
DEFAULT_NEUTRALS=('vu','descending_turn_curvature','start_acceleration','initial_speed_frontload')
def valid_controls(names):
    return (names[:3]==['actual_q1','actual_q4','actual_c6'] and
            3<=len(names)<=11 and len(set(names))==len(names) and
            all(n in REVIEWED_NEUTRALS for n in names[3:]))
def add_profile(profile,key,value):
    if key in ('initial_speed_pulse','initial_speed_frontload') and key not in profile:
        if value==0.:return
        profile[key]=value
    else:profile[key]+=value

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for key in ('actual-reference','actual-reference-raw','actual-reference-tail',
                'source-topic','frozen-reference-ready','frozen-calibration-ledger',
                'port','tail-config','out-prefix'):
        ap.add_argument('--'+key, type=Path, required=True)
    ap.add_argument('--response-data', type=Path)
    ap.add_argument('--baseline-only', action='store_true')
    ap.add_argument('--known-grid', type=Path)
    ap.add_argument('--interior-audit', type=Path, help='Optional accepted physical-polynomial curvature witness; exact baseline SHA required.')
    ap.add_argument('--angular', type=int, default=768)
    ap.add_argument('--geometry-batch', type=int, default=8)
    ap.add_argument('--rss-limit-mib', type=float, default=192.)
    ap.add_argument('--neutral-controls',nargs='+',default=list(DEFAULT_NEUTRALS))
    ap.add_argument('--steps',type=float,nargs='+',required=True,help='Positive steps for all three original core controls followed by the declared reviewed neutral controls.')
    args = ap.parse_args()
    if not args.baseline_only and not args.response_data:
        raise ValueError('A full plan requires its newly completed actual response')
    control_names=['actual_q1','actual_q4','actual_c6',*args.neutral_controls]
    if not valid_controls(control_names) or len(args.steps)!=len(control_names):
        raise ValueError('Require three original core controls and distinct explicitly reviewed neutrals with one step each')
    if args.angular < 768 or args.angular % 768 or any(not np.isfinite(x) or x<=0 for x in args.steps):
        raise ValueError('Positive finite control steps and a full fourfold angular grid are required')
    actual, raw, tail = [read(p) for p in (args.actual_reference,args.actual_reference_raw,args.actual_reference_tail)]
    if (not actual['solver_success'] or actual.get('audit_pending',True)
            or not actual['config'].get('actual_nonlinear_tail') or not raw['solver_success']
            or sha(args.actual_reference_raw) != actual['raw_collocation_checkpoint']['sha256']
            or not tail['response']['converged']):
        raise ValueError('A fully processed accepted actual/raw/tail baseline is required')
    chart_record = actual['numerical_meridian_chart']
    if (chart_record['kind'] != 'C2-all-physical-knots-v1'
            or raw['identity']['numerical_reference_knots'] != chart_record['reference_t']
            or raw['identity']['profile'] != actual['frozen_profile']):
        raise ValueError('The saved material chart or physical profile differs')
    hashes = {}
    x = np.asarray(raw_flat(args.actual_reference_raw,raw,'x',hashes)).reshape(raw['arrays']['x']['shape'])
    if x[0] != 0 or x[-1] != 1 or not np.all(np.diff(x)>0):
        raise ValueError('Complete accepted raw knots must cover [0,1] in order')
    chart = NeckChart(chart_record['reference_t'],chart_record['physical_s'])
    physical = np.unique(np.r_[np.linspace(chart.s[0],chart.s[-1],241),
                      *[np.linspace(a,b,33) for a,b in zip(chart.s[:-1],chart.s[1:])]])
    mapped = chart.inverse(physical)
    roundtrip = float(abs(chart.evaluate(mapped)[0]-physical).max())
    if roundtrip>1e-12:
        raise ValueError('The recorded physical anchors did not survive chart inversion')
    inherited = []
    if args.known_grid:
        old = read(args.known_grid)
        for witness in old.get('known_reference_witnesses',[]):
            eta = witness.get('eta',witness['angular_index']*2*np.pi/old['angular'])
            angle_index = int(round(eta*args.angular/(2*np.pi))) % args.angular
            if abs(angle_index*2*np.pi/args.angular-eta)>1e-13:
                raise ValueError('The requested geometry grid omits a saved angular witness')
            inherited.append(dict(numerical_t=old['numerical_t'][witness['radial_index']],
                                  angular_index=angle_index, eta=eta,
                                  source_grid=str(args.known_grid), old_witness_only=True))
    interior_record = None
    if args.interior_audit:
        interior_record = read(args.interior_audit)
        if (interior_record.get('input_sha256') != sha(args.actual_reference)
                or interior_record.get('modes') != actual['modes']):
            raise ValueError('The accepted physical-interior witness belongs to another baseline')
        witness = interior_record['top']['kappa']
        physical_s, eta = float(witness['s']), float(witness['psi'])
        if not chart.s[0] <= physical_s <= chart.s[-1]:
            raise ValueError('The actual physical curvature witness is outside the saved chart')
        angle_index = int(round(eta*args.angular/(2*np.pi))) % args.angular
        mismatch = abs(np.angle(np.exp(1j*(angle_index*2*np.pi/args.angular-eta))))
        if mismatch > 1e-13:
            raise ValueError('The requested angular grid omits the accepted physical curvature witness; increase angular explicitly')
        numerical_t = float(chart.inverse(np.array([physical_s]))[0])
        inherited.append(dict(numerical_t=numerical_t, physical_s=physical_s,
            angular_index=angle_index, eta=eta, source_audit=str(args.interior_audit),
            source_audit_sha256=sha(args.interior_audit),
            source_polynomial_sample=witness['value'],
            same_accepted_baseline_physical_polynomial_witness=True,
            raw_cubic_evaluation_does_not_replace_physical_quintic_audit=True))
    grid = np.unique(np.r_[x,mapped,chart.t,np.linspace(0,1,257),
                           [w['numerical_t'] for w in inherited]])
    for witness in inherited:
        witness['radial_index'] = int(np.argmin(abs(grid-witness['numerical_t'])))
        if grid[witness['radial_index']] != witness['numerical_t']:
            raise ValueError('A saved witness was lost from the complete grid')
    prefix=args.out_prefix
    prefix.parent.mkdir(parents=True,exist_ok=True)
    grid_path=Path(str(prefix)+'-grid.json')
    grid_record=dict(numerical_t=grid.tolist(),angular=args.angular,grid_only=True,
        all_original_raw_nodes_used_in_cubic=True,all_original_raw_nodes_evaluated=True,
        raw_sha256=sha(args.actual_reference_raw),original_raw_nodes=len(x),
        saved_physical_knots=len(chart.s),mapped_physical_anchors=len(physical),
        chart_roundtrip_max=roundtrip,
        rule='Every accepted raw knot, uniform257 t, uniform241 physical s, 33 per physical knot interval, saved comparison witnesses and optional accepted-polynomial curvature witness.',
        known_reference_witnesses=inherited,
        inherited_witnesses_are_not_claimed_to_be_new_extrema=True)
    if grid_path.exists():
        if read(grid_path)!=grid_record:
            raise ValueError('The existing common grid belongs to a different state or sampling rule')
    else:
        grid_path.write_text(json.dumps(grid_record,indent=2)+'\n')
    core=actual['core']['coefficients'][:3]
    directions=list(zip(control_names,args.steps))
    cases=[('baseline',None,0.)]
    response_rows={}
    if not args.baseline_only:
        response=read(args.response_data)
        if (response.get('schema')!='fixed-actual-to-three-control-response-v1'
                or not response.get('finished') or response.get('new_solution')
                or response['baseline']['core']!=actual['core']['coefficients']
                or response['baseline']['profile']!=actual['frozen_profile']
                or response['modes']!=actual['modes'] or response['nodes']!=len(x)
                or response['angular']!=actual['config']['angular']):
            raise ValueError('The completed response belongs to another accepted state')
        for path in (args.actual_reference,args.actual_reference_raw,args.actual_reference_tail):
            if response['source_sha256'].get(str(path))!=sha(path):
                raise ValueError('Preserve exact response input path spelling and hash: '+str(path))
        response_rows={r['direction']:r for r in response['prescribed_low_core_responses']}
        response_rows.update({r['external_field']:r for r in response['additional_core_held_directions']})
        for name,step in directions:
            if name not in response_rows:
                raise ValueError('A complete actual control response is missing: '+name)
            cases.extend([(name+'-plus',name,step),(name+'-minus',name,-step)])
    wrapper=Path(__file__).with_name('root_actual_geometry_field_initial_laws.py')
    base_command=[sys.executable,str(wrapper)]
    for key in ('actual_reference','actual_reference_raw','actual_reference_tail',
                'source_topic','frozen_reference_ready','frozen_calibration_ledger','port','tail_config'):
        base_command+=['--'+key.replace('_','-'),str(getattr(args,key))]
    base_command+=['--target-core',*map(repr,core),'--max-nodes',str(max(2400,len(x)+400)),
                  '--radial-batch-size','8','--collocation-batch-size','12',
                  '--geometry-grid',str(grid_path),'--mean-angular',str(max(512,16*(3*actual['modes']+1))),
                  '--geometry-batch',str(args.geometry_batch),'--resident-rss-guard-mib',str(args.rss_limit_mib)]
    planned=[]
    for name,direction,step in cases:
        case=Path(str(prefix)+'-'+name)
        report,field,formal,log=[Path(str(case)+suffix) for suffix in
                               ('-screen.json','-field.json','-resource.json','-log.txt')]
        command=base_command.copy()
        target,profile=core.copy(),dict(actual['frozen_profile'])
        if direction:
            command+=['--response-data',str(args.response_data)]
            if direction in ('actual_q1','actual_q4','actual_c6'):
                target[('actual_q1','actual_q4','actual_c6').index(direction)]+=step
            else:
                command+=['--neutral-control-step',direction+'='+repr(step)]
            for key,value in response_rows[direction]['physical_profile_derivative'].items():
                add_profile(profile,key,step*value)
        at=command.index('--target-core')
        command[at+1:at+4]=list(map(repr,target))
        command+=['--out-prefix',str(case),'--inspect-warm-output',str(report),'--geometry-array',str(field)]
        command=[sys.executable,str(Path(__file__).with_name('strong_resource_run.py')),
                 '--out',str(formal),'--',*command]
        planned.append(dict(name=name,direction=direction,step=step,command=command,
            expected_core=target,expected_profile=profile,report=str(report),field=str(field),
            resource=str(formal),log=str(log),complete_mean_angular=max(512,16*(3*actual['modes']+1))))
    inputs=[Path(__file__),wrapper,Path(__file__).with_name('root_geometry_array_io_resident.py'),
            Path(__file__).with_name('root_neck_chart.py'),args.actual_reference,args.actual_reference_raw,
            args.actual_reference_tail,args.frozen_reference_ready,args.frozen_calibration_ledger,
            args.port,args.tail_config,grid_path]
    inputs.extend(Path(__file__).with_name(name) for name in ('root_actual_geometry_field_complete_mean.py','strong_initial_laws_augmented_core.py','strong_pulse_augmented_core.py','strong_initial_speed_pulse.py','strong_monotone_initial_speed.py'))
    if args.known_grid:inputs.append(args.known_grid)
    if args.interior_audit:inputs.append(args.interior_audit)
    if not args.baseline_only:inputs.append(args.response_data)
    hashes.update({str(p):sha(p) for p in inputs})
    path=Path(str(prefix)+('-baseline-plan.json' if args.baseline_only else '-plan.json'))
    if path.exists():raise FileExistsError('Use a fresh plan file')
    path.write_text(json.dumps(dict(scope=__doc__,prepared_only=True,executed=False,
        baseline_only=args.baseline_only,nonlinear_solution=False,new_tail_evaluation=False,
        cwd=str(Path.cwd()),grid=str(grid_path),geometry_wrapper=str(wrapper),
        source_and_input_sha256=hashes,baseline_core=core,modes=actual['modes'],
        directions=[dict(name=name,step=step) for name,step in directions],candidates=planned,
        all_original_fields_and_core_modes_retained=True,
        mean_rule='Original full physical postprocessor angular rule for height and both radial mean derivatives.',
        limitations=['Warm numerical samples, with no new true nonlinear-tail solve.',
                     'No continuous curvature, reach, closed-surface diameter or amplitude certificate.']),indent=2)+'\n')
    print(json.dumps(dict(plan=str(path),sha256=sha(path),cases=len(planned),radial=len(grid),angular=args.angular)),flush=True)


if __name__=='__main__':
    main()
