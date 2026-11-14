#!/usr/bin/env python3
"""New fixed tail/cut, old p=1.48 phase rules, and an actual finite T root.
The resulting g is new. No nonlinear isometry or reach is asserted.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,copy,importlib.util,json,math,time
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.optimize import brentq
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
spec=importlib.util.spec_from_file_location('fd2d_retarget_moderate',HERE/'fd2d_moderate_deep_screen.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);fm=mod.fm;lin=mod.lin


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source',type=Path,default=ROOT/'notes/2026-11-12-fd2d-moderate-deep-p148-frozen-01.json')
    p.add_argument('--tail-config',type=Path,required=True);p.add_argument('--tail-port',type=Path,required=True)
    p.add_argument('--out-prefix',type=Path,required=True);args=p.parse_args();started=time.monotonic()
    source=json.loads(args.source.read_text());cfg=json.loads(args.tail_config.read_text());port=json.loads(args.tail_port.read_text())
    if not port.get('completed') or port['config_sha256']!=fm.digest(args.tail_config) or port['far']<cfg['protectCell']:
        raise ValueError('Complete port report for this config and all changed cells required')
    if abs(source['moderate_deep_design']['pdeep']-1.48)>1e-13:raise ValueError('pdeep=1.48 source required')
    rc,wc,K=cfg['rCut'],cfg['wCut'],cfg['curvatureBound'];wr=float(-Fraction(str(K))*Fraction(str(wc))/Fraction(str(rc)))
    D=port['linear_slopes']['2'];target=[wc*(4-rc*D)/3,1.]
    initial=copy.deepcopy(source);initial['cut_reference']=dict(r=rc,w=wc,wr=wr)
    initial['cut']=dict(r=rc,w=wc,wr=wr,a_prime=-1/math.sqrt(1+wc*wc),a_second=-wc*wr/(1+wc*wc)**2,
        z_prime=wc/math.sqrt(1+wc*wc),physical_upper_background_height_r_sign=-1,
        linear_slopes=port['linear_slopes'],cuff_radius=port['stats']['rCuff'],tail_height_span=port['stats']['heightSpan'])
    initial['inputs'].update(tail_port=args.tail_port.name,tail_port_sha256=fm.digest(args.tail_port),
        tail_config=args.tail_config.name,tail_config_sha256=fm.digest(args.tail_config))
    for piece in initial['segments']:
        if piece.get('label')=='final_deep_coast':piece['radius_after_next']=rc
    for key in ('metric_diagnostics','full_m2_amplification','selection_reason'):initial.pop(key,None)
    initial['finite_linear_screen']=dict(terminal_direction=target,scope='New tail direction; initial T is not yet recalibrated.')
    initial['status'].update(metric_frozen=False)
    initial['tail_retarget_provenance']=dict(source_candidate=args.source.name,source_sha256=fm.digest(args.source),
        generator=Path(__file__).name,generator_sha256=fm.digest(__file__),tail_config_sha256=fm.digest(args.tail_config),
        actual_tail_port_sha256=fm.digest(args.tail_port),far=port['far'],new_physical_metric=True,
        direction_formula='f/g=(b/v)(r D2-4)/3=w(4-r D2)/3')
    seed=args.out_prefix.with_name(args.out_prefix.name+'-initial.json');report_file=args.out_prefix.with_name(args.out_prefix.name+'-report.json')
    if seed.exists() or report_file.exists():raise ValueError('Unused output stem required')
    seed.write_text(json.dumps(initial,indent=2)+'\n');family=mod.ModerateFamily(seed)
    report=dict(schema='fd2d-p148-new-tail-retarget-v1',source_sha256=fm.digest(__file__),initial_file=seed.name,initial_sha256=fm.digest(seed),
        tail_config_sha256=fm.digest(args.tail_config),tail_port_sha256=fm.digest(args.tail_port),terminal_direction=target,
        evaluations=[],completed=False,nonlinear_solution=False,continuous_certificate=False)
    def shoot(T):
        r,y=family.shoot(1.48,float(T));row=dict(T=float(T),residual=r,terminal_fg=y.tolist());report['evaluations'].append(row)
        report_file.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(dict(event='shoot',**row)),flush=True);return r
    Tmax=family.Tmax(1.48);lo=0.;flo=shoot(lo);hi=min(.03,.95*Tmax);fhi=shoot(hi)
    while flo*fhi>0 and hi<.95*Tmax:hi=min(2*hi,.95*Tmax);fhi=shoot(hi)
    if flo*fhi>0:
        report.update(completed=True,root_found=False,Tmax=Tmax,seconds=time.monotonic()-started)
        report_file.write_text(json.dumps(report,indent=2)+'\n');raise RuntimeError('No sign bracket in physical coast interval')
    root=brentq(shoot,lo,hi,xtol=5e-13,rtol=1e-14);row,bundle,_=family.root_record(1.48,root)
    trace,analysis=lin.analyse(fm.Candidate(bundle),target,full_checks=True)
    bundle['status']['metric_frozen']=True
    bundle['selection_reason']='Existing pdeep=1.48 phase rules with new fixed tail/cut and T matched to its actual full-depth finite m2 direction. Small-branch initializer only.'
    candidate=args.out_prefix.with_name(args.out_prefix.name+'-candidate.json');trajectory=args.out_prefix.with_name(args.out_prefix.name+'-trajectory.npz')
    candidate.write_text(json.dumps(bundle,indent=2)+'\n');np.savez_compressed(trajectory,**trace.sample())
    report.update(completed=True,root_found=True,root=row,full_linear_analysis=analysis,candidate_file=candidate.name,candidate_sha256=fm.digest(candidate),
        trajectory_file=trajectory.name,trajectory_sha256=fm.digest(trajectory),trajectory_bytes=trajectory.stat().st_size,Tmax=Tmax,seconds=time.monotonic()-started)
    report_file.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(dict(event='complete',T=root,root=row,candidate_file=candidate.name,candidate_sha256=fm.digest(candidate),seconds=report['seconds'])),flush=True)


if __name__=='__main__':main()
