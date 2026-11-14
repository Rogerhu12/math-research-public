#!/usr/bin/env python3
"""Finite same-port screen with a shallow return BEFORE full contraction.

The input prefix and a0 are unchanged. The suffix first reaches a moderate
negative a', returns to a shallower negative phase, and only then deepens to
the fixed cut brake. A variable shallow coast supplies one finite linear
m2 matching parameter. This is a NEW metric choice, not a nonlinear solution.
Every tried candidate and rejection is saved; only a small-gain matched seed
can be selected for subsequent fixed-g BVP use.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse,json,math,copy,importlib.util,time
from pathlib import Path
import numpy as np
from scipy.optimize import brentq

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
spec=importlib.util.spec_from_file_location('fd2d_partial_monotone',HERE/'fd2d_monotone_ellipse_screen.py')
mono=importlib.util.module_from_spec(spec);spec.loader.exec_module(mono);fm=mono.fm


class PartialReturnScreen(mono.Screen):
    def build(self,vmid,return_phase,fraction,acceleration=2.1,epsilon=.001,K=6.8,transition=.04):
        if not 0<=fraction<1:raise ValueError('Coast fraction must lie in [0,1)')
        if not 0<return_phase<math.asin(vmid):raise ValueError('Return must be shallower than the moderate contraction')
        bundle=copy.deepcopy(self.base);pieces=bundle['segments'];jet=list(pieces[-1]['jet1'])
        piece,jet=mono.acceleration_piece(jet,transition,-acceleration,'partial_return_acceleration_entry');pieces.append(piece)
        plateau_speed=-vmid+acceleration*transition/2
        duration=(plateau_speed-jet[1])/(-acceleration)
        if duration<=0:raise ValueError('Nonpositive acceleration plateau')
        piece,jet=mono.acceleration_piece(jet,duration,-acceleration,'partial_return_acceleration_plateau');pieces.append(piece)
        piece,jet=mono.acceleration_piece(jet,transition,0.,'partial_return_acceleration_exit');pieces.append(piece)
        phase0=math.asin(jet[1]);deep=-math.pi/2+epsilon
        first=fm.turn(phase0,-return_phase,K)
        first.update(start_from_previous=True,length_from_turn_rate=True,label='early_shallow_return')
        second=fm.turn(-return_phase,deep,K)
        second.update(start_from_previous=True,length_from_turn_rate=True,label='redeepen_after_partial_return')
        w=self.tail['w'];wr=self.tail['wr'];pt=-math.atan2(1.,w);ps=-wr/(1+w*w)**1.5
        brake=dict(kind='brake',p0=deep,p1=pt,L=2*(pt-deep)/ps,start_from_previous=True,
                   end_from_cut=True,label='cut_second_jet_brake')
        start_radius=fm.Candidate(bundle).segments[-1]['a_end']
        free=start_radius+sum(fm.phase_integral(p,1.) for p in (first,second,brake))-self.tail['r']
        if free<=0:raise ValueError('No radial room for the early partial return')
        coast_length=fraction*free/math.sin(return_phase)
        pieces.append(first)
        pieces.append(dict(kind='coast',p0=-return_phase,p1=-return_phase,L=coast_length,
                           start_from_previous=True,label='partial_return_matching_coast'))
        pieces.append(second)
        pieces.append(dict(kind='coast_to',p0=deep,p1=deep,start_from_previous=True,
                           radius_after_next=self.tail['r'],label='final_deep_coast'))
        pieces.append(brake)
        for name in ('linear_m2_seed','metric_diagnostics','design_parameters'):bundle.pop(name,None)
        bundle.update(generated_by=Path(__file__).name,generator_sha256=fm.digest(__file__),
            partial_return_design_parameters=dict(vmid=vmid,return_phase=return_phase,fraction=fraction,
                coast_length=coast_length,acceleration=acceleration,epsilon=epsilon,K=K,transition=transition),
            source_frozen_candidate=self.source_path.name,source_frozen_candidate_sha256=fm.digest(self.source_path),
            status=dict(metric_frozen=True,nonlinear_prefix_solved=False,nonlinear_tail_matched=False,
                        closed_surface=False,reach_certified=False,strong_target_complete=False))
        candidate=fm.Candidate(bundle);suffix=candidate.segments[self.count:]
        back=candidate.linear(self.terminal,backward=True,segments=suffix)
        determinant=self.initial_line[0]*back[1]-self.initial_line[1]*back[0]
        residual=float(determinant/(np.linalg.norm(self.initial_line)*np.linalg.norm(back)))
        gain=float(np.dot(self.initial_line,back)/np.dot(back,back))
        bundle['finite_linear_screen']=dict(normalized_direction_residual=residual,
            terminal_height_gain_at_exact_direction_match=gain,prefix_line=self.initial_line.tolist(),
            backward_at_prefix=back.tolist(),terminal_direction=self.terminal.tolist(),
            scope='Finite m2 direction only; gain applies at a matching root. No nonlinear closure or geometric bound.')
        bundle['metric_diagnostics']=candidate.metric_diagnostics()
        bundle['metric_diagnostics']['background_height_with_tail']=bundle['metric_diagnostics']['background_height']+self.port['stats']['heightSpan']
        s=np.unique(np.concatenate([np.linspace(p['s0'],p['s0']+p['L'],max(3,math.ceil(p['L']/.002))) for p in candidate.segments]))
        a,v,acc=candidate.profile(s)
        bundle['metric_diagnostics']['sample_rotational_meridian_curvature']=float(np.max(abs(acc)/np.sqrt(1-v*v)))
        bundle['radial_coast_budget']=free
        return bundle


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source',type=Path,default=ROOT/'notes/2026-11-12-fd2d-ellipse-b05-frozen-candidate-v2.json')
    p.add_argument('--port',type=Path,default=ROOT/'notes/2026-11-12-fd2d-ellipse-cuff032-cut04-port.json')
    p.add_argument('--out',type=Path,required=True);p.add_argument('--selected-out',type=Path)
    p.add_argument('--acceleration',type=float,default=2.1);p.add_argument('--epsilon',type=float,default=.001)
    p.add_argument('--vmid',type=float,nargs='+',default=[.85,.95]);p.add_argument('--return-phase',type=float,nargs='+',default=[.2,.5])
    p.add_argument('--fraction',type=float,nargs='+',default=[0.,.33,.67,.95]);args=p.parse_args()
    screen=PartialReturnScreen(args.source,args.port);start=time.monotonic()
    report=dict(scope=__doc__,source_sha256=fm.digest(__file__),source_candidate_sha256=fm.digest(args.source),
        parameters=dict(acceleration=args.acceleration,epsilon=args.epsilon),rows=[],roots=[])
    for vmid in args.vmid:
        for ret in args.return_phase:
            previous=None
            for fraction in args.fraction:
                try:
                    b=screen.build(vmid,ret,fraction,args.acceleration,args.epsilon)
                    r=b['finite_linear_screen']['normalized_direction_residual']
                    row=dict(vmid=vmid,return_phase=ret,fraction=fraction,residual=r,
                        gain_diagnostic=b['finite_linear_screen']['terminal_height_gain_at_exact_direction_match'],
                        radial_coast_budget=b['radial_coast_budget'],metric=b['metric_diagnostics'])
                    if previous is not None and previous[1]*r<0:
                        root=brentq(lambda f:screen.build(vmid,ret,f,args.acceleration,args.epsilon)['finite_linear_screen']['normalized_direction_residual'],previous[0],fraction,xtol=2e-11)
                        candidate=screen.build(vmid,ret,root,args.acceleration,args.epsilon)
                        report['roots'].append(candidate)
                        print(json.dumps(dict(event='root',parameters=candidate['partial_return_design_parameters'],linear=candidate['finite_linear_screen'],metric=candidate['metric_diagnostics'])),flush=True)
                    previous=fraction,r
                except Exception as exc:row=dict(vmid=vmid,return_phase=ret,fraction=fraction,error=str(exc));previous=None
                report['rows'].append(row);args.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(row),flush=True)
    accepted=[r for r in report['roots'] if abs(r['finite_linear_screen']['normalized_direction_residual'])<1e-5
              and abs(r['finite_linear_screen']['terminal_height_gain_at_exact_direction_match'])<.1
              and r['metric_diagnostics']['background_height_with_tail']<1.25
              and r['metric_diagnostics']['sample_rotational_meridian_curvature']<1/.136]
    if accepted and args.selected_out:
        chosen=min(accepted,key=lambda r:abs(r['finite_linear_screen']['terminal_height_gain_at_exact_direction_match']))
        args.selected_out.write_text(json.dumps(chosen,indent=2)+'\n')
        report['selected_output']=args.selected_out.name;report['selected_sha256']=fm.digest(args.selected_out)
    report.update(accepted_finite_seed_count=len(accepted),seconds=time.monotonic()-start)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(event='complete',trials=len(report['rows']),roots=len(report['roots']),accepted_finite_seeds=len(accepted),seconds=report['seconds'])),flush=True)


if __name__=='__main__':main()
