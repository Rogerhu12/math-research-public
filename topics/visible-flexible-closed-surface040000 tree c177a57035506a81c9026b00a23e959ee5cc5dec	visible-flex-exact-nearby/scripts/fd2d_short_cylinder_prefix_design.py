#!/usr/bin/env python3
"""A new fixed-g prefix with a shortened exact central cylinder.
The later radial profile and its jets are translated in meridian arclength.
The actual fixed-tail direction is matched by the physical coast parameter T.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,importlib.util,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
spec=importlib.util.spec_from_file_location('fd2d_wider_parent_family',HERE/'fd2d-wider-cut-prefix-screen.py')
wide=importlib.util.module_from_spec(spec);spec.loader.exec_module(wide);fm=wide.fm;lin=wide.lin;moderate=wide.moderate


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source',type=Path,default=ROOT/'notes/2026-11-12-fd2d-moderate-deep-p148-frozen-01.json')
    p.add_argument('--tail-config',type=Path,required=True);p.add_argument('--tail-port',type=Path,required=True)
    p.add_argument('--vmid',type=float,required=True);p.add_argument('--pdeep',type=float,required=True)
    p.add_argument('--central-cylinder',type=float,default=.001)
    p.add_argument('--out-prefix',type=Path,required=True);args=p.parse_args();started=time.monotonic()
    cfg=json.loads(args.tail_config.read_text());port=json.loads(args.tail_port.read_text());source=json.loads(args.source.read_text())
    if not port.get('completed') or port['config_sha256']!=fm.digest(args.tail_config) or port['far']<cfg['protectCell']:
        raise ValueError('Actual full-changed-depth fixed-tail port required')
    initial=wide.provisional_bundle(source,args.vmid,cfg['rCut'],cfg['wCut'],port['linear_slopes']['2'],args.pdeep)
    initial.pop('provisional_tail_target',None)
    cylinder=initial['segments'][0]
    if cylinder.get('label')!='central_cylinder' or cylinder['kind']!='coast' or cylinder['p0']!=0 or cylinder['p1']!=0:
        raise ValueError('An exact leading cylinder is required')
    old_length=cylinder['L'];new_length=float(args.central_cylinder)
    if not 0<new_length<=old_length:raise ValueError('Positive shortening only')
    cylinder['L']=new_length
    initial['central_cylinder_shortening']=dict(original_length=old_length,new_length=new_length,
        exact_height_reduction=old_length-new_length,
        later_radial_profile='Same segment formulas, translated in meridian arclength',
        linear_invariance='For the central data f=1,g=0 the exact cylinder transfer leaves f,g unchanged',
        nonlinear_invariance='For l=m=0, the cylinder extrudes the same central curve vertically; no nonround reach claim follows',
        new_physical_metric=True)
    cut=initial['cut'];cut.update(tail_height_span=port['stats']['heightSpan'],tail_height_span_known=True,
        linear_slopes=port['linear_slopes'],linear_tail_port_computed=True,nonlinear_tail_matched=False)
    for key in ('zero_tail_height_is_unused_placeholder','solved_tail_port'):cut.pop(key,None)
    initial['inputs'].update(tail_config=args.tail_config.name,tail_config_sha256=fm.digest(args.tail_config),
        tail_port=args.tail_port.name,tail_port_sha256=fm.digest(args.tail_port))
    initial['finite_linear_screen']['scope']='Actual full changed-prefix m2 tail direction; shallow coast T not yet matched.'
    initial['fixed_tail_design']=dict(vmid=args.vmid,pdeep=args.pdeep,new_physical_metric=True,
        source_candidate=args.source.name,source_candidate_sha256=fm.digest(args.source),
        prefix_family_source='fd2d-wider-cut-prefix-screen.py',prefix_family_sha256=fm.digest(HERE/'fd2d-wider-cut-prefix-screen.py'),
        generator=Path(__file__).name,generator_sha256=fm.digest(__file__),tail_depth=port['far'])
    stem=args.out_prefix;seed=stem.with_name(stem.name+'-initial.json');report_file=stem.with_name(stem.name+'-report.json')
    if seed.exists() or report_file.exists():raise ValueError('Unused output stem required')
    seed.write_text(json.dumps(initial,indent=2)+'\n');family=moderate.ModerateFamily(seed)
    report=dict(schema='fd2d-short-cylinder-fixed-tail-prefix-design-v1',source_sha256=fm.digest(__file__),initial_file=seed.name,
        initial_sha256=fm.digest(seed),tail_config_sha256=fm.digest(args.tail_config),tail_port_sha256=fm.digest(args.tail_port),
        vmid=args.vmid,pdeep=args.pdeep,central_cylinder=new_length,evaluations=[],completed=False,nonlinear_solution=False,continuous_certificate=False)
    def shoot(T):
        r,y=family.shoot(args.pdeep,float(T));row=dict(T=float(T),residual=r,terminal_fg=y.tolist());report['evaluations'].append(row)
        report_file.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(dict(event='shoot',**row)),flush=True);return r
    upper=family.Tmax(args.pdeep);lo=0.;flo=shoot(lo);hi=min(.2,.95*upper);fhi=shoot(hi)
    while flo*fhi>0 and hi<.95*upper:hi=min(2*hi,.95*upper);fhi=shoot(hi)
    if flo*fhi>0:
        report.update(completed=True,root_found=False,Tmax=upper,seconds=time.monotonic()-started)
        report_file.write_text(json.dumps(report,indent=2)+'\n');raise RuntimeError('No T bracket within the positive-coast range')
    T=brentq(shoot,lo,hi,xtol=5e-13,rtol=1e-14);row,bundle,_=family.root_record(args.pdeep,T)
    trace,analysis=lin.analyse(fm.Candidate(bundle),family.target,full_checks=True)
    bundle['status']['metric_frozen']=True;bundle['selection_reason']='Shortened exact cylinder, moderate middle speed, actual full-depth fixed-tail m2 direction, and measured height/amplification. New BVP input only.'
    candidate=stem.with_name(stem.name+'-candidate.json');trajectory=stem.with_name(stem.name+'-trajectory.npz')
    candidate.write_text(json.dumps(bundle,indent=2)+'\n');np.savez_compressed(trajectory,**trace.sample())
    report.update(completed=True,root_found=True,root=row,full_linear_analysis=analysis,Tmax=upper,
        candidate_file=candidate.name,candidate_sha256=fm.digest(candidate),trajectory_file=trajectory.name,
        trajectory_sha256=fm.digest(trajectory),trajectory_bytes=trajectory.stat().st_size,seconds=time.monotonic()-started)
    report_file.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(dict(event='complete',root=row,candidate=candidate.name,sha256=fm.digest(candidate),seconds=report['seconds'])),flush=True)


if __name__=='__main__':main()
