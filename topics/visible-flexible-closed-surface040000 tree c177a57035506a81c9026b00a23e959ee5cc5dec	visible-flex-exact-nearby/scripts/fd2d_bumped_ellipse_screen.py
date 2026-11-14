#!/usr/bin/env python3
"""Finite linear design with one shallow phase return while a' stays negative.

The return creates a negative-Gaussian-curvature section without an axial
pause. A curvature-bounded phase brake joins the main acceleration to the
near-horizontal coast. Whole-prefix nonlinear geometry remains unverified.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse,json,math,copy,importlib.util
from pathlib import Path
import numpy as np
from scipy.optimize import brentq

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
sp=importlib.util.spec_from_file_location('fd2d_monotone_bump',HERE/'fd2d_monotone_ellipse_screen.py')
mono=importlib.util.module_from_spec(sp);sp.loader.exec_module(mono);fm=mono.fm


class BumpScreen(mono.Screen):
    def build(self,mid_phase,fraction,position=.5,acceleration=1.9,epsilon=.001,K=6.8,transition=.04):
        bundle=copy.deepcopy(self.base);pieces=bundle['segments'];jet=list(pieces[-1]['jet1'])
        piece,jet=mono.acceleration_piece(jet,transition,-acceleration,'bump_acceleration_entry');pieces.append(piece)
        end_speed=-math.sqrt(1-(acceleration/K)**2)
        length=(end_speed-jet[1])/(-acceleration)
        if length<=0:raise ValueError('Nonpositive plateau length')
        piece,jet=mono.acceleration_piece(jet,length,-acceleration,'bump_acceleration_plateau');pieces.append(piece)
        phase0=math.asin(jet[1]);deep=-math.pi/2+epsilon
        piece=dict(kind='phase_bridge',p0=phase0,p1=deep,ps0=-K,ps1=0.,
                   L=2*(phase0-deep)/K,start_from_previous=True,start_second_from_previous=True,
                   label='curvature_bounded_deepening')
        pieces.append(piece);base=fm.Candidate(bundle);start_radius=base.segments[-1]['a_end']
        first=fm.turn(deep,-mid_phase,K);first.update(start_from_previous=True,length_from_turn_rate=True,label='shallow_phase_return')
        second=fm.turn(-mid_phase,deep,K);second.update(start_from_previous=True,length_from_turn_rate=True,label='shallow_phase_redeepen')
        w=self.tail['w'];wr=self.tail['wr'];pt=-math.atan2(1.,w);ps=-wr/(1+w*w)**1.5
        brake=dict(kind='brake',p0=deep,p1=pt,L=2*(pt-deep)/ps,
                   start_from_previous=True,end_from_cut=True,label='cut_second_jet_brake')
        free=start_radius+self._radial(first)+self._radial(second)+self._radial(brake)-self.tail['r']
        if free<=0:raise ValueError('No radial room for this shallow return')
        middle_drop=fraction*free;before_drop=position*(1-fraction)*free
        pieces.append(dict(kind='coast_to',p0=deep,p1=deep,start_from_previous=True,
                           radius_end=start_radius-before_drop,label='deep_coast_before_return'))
        pieces.append(first)
        pieces.append(dict(kind='coast',p0=-mid_phase,p1=-mid_phase,start_from_previous=True,
                           L=middle_drop/math.sin(mid_phase),label='shallow_coast'))
        pieces.append(second)
        pieces.append(dict(kind='coast_to',p0=deep,p1=deep,start_from_previous=True,
                           radius_after_next=self.tail['r'],label='deep_coast_after_return'))
        pieces.append(brake)
        for name in ('linear_m2_seed','metric_diagnostics','design_parameters'):bundle.pop(name,None)
        bundle.update(generated_by=Path(__file__).name,generator_sha256=fm.digest(__file__),
            bump_design_parameters=dict(mid_phase=mid_phase,fraction=fraction,position=position,
                acceleration=acceleration,epsilon=epsilon,K=K,transition=transition),
            source_frozen_candidate=self.source_path.name,source_frozen_candidate_sha256=fm.digest(self.source_path),
            status=dict(metric_frozen=True,nonlinear_prefix_solved=False,nonlinear_tail_matched=False,
                        closed_surface=False,reach_certified=False,strong_target_complete=False))
        candidate=fm.Candidate(bundle);suffix=candidate.segments[self.count:]
        back=candidate.linear(self.terminal,backward=True,segments=suffix)
        determinant=self.initial_line[0]*back[1]-self.initial_line[1]*back[0]
        residual=float(determinant/(np.linalg.norm(self.initial_line)*np.linalg.norm(back)))
        gain=float(np.dot(self.initial_line,back)/np.dot(back,back))
        bundle['finite_linear_screen']=dict(normalized_direction_residual=residual,
            terminal_height_gain_at_exact_direction_match=gain,
            prefix_line=self.initial_line.tolist(),backward_at_prefix=back.tolist(),terminal_direction=self.terminal.tolist(),
            scope='Finite m2 line only; the reported gain is meaningful at a matched direction, not at an arbitrary row.')
        bundle['metric_diagnostics']=candidate.metric_diagnostics()
        bundle['metric_diagnostics']['background_height_with_tail']=bundle['metric_diagnostics']['background_height']+self.port['stats']['heightSpan']
        bundle['radial_coast_budget']=free
        return bundle

    @staticmethod
    def _radial(piece):return fm.phase_integral(piece,1.)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source',type=Path,default=ROOT/'notes/2026-11-12-fd2d-ellipse-b05-frozen-candidate-v2.json')
    p.add_argument('--port',type=Path,default=ROOT/'notes/2026-11-12-fd2d-ellipse-cuff032-cut04-port.json')
    p.add_argument('--out',type=Path,required=True);p.add_argument('--selected-out',type=Path)
    p.add_argument('--epsilon',type=float,default=.001);p.add_argument('--position',type=float,default=.5)
    args=p.parse_args();screen=BumpScreen(args.source,args.port)
    report=dict(scope=__doc__,source_sha256=fm.digest(__file__),source_candidate_sha256=fm.digest(args.source),
                epsilon=args.epsilon,position=args.position,rows=[],roots=[])
    for mid in (1.0,1.2,1.35):
        previous=None
        for fraction in (0.,.3,.6,.9):
            try:
                b=screen.build(mid,fraction,args.position,epsilon=args.epsilon)
                r=b['finite_linear_screen']['normalized_direction_residual']
                row=dict(mid_phase=mid,fraction=fraction,residual=r,metric=b['metric_diagnostics'],
                         radial_coast_budget=b['radial_coast_budget'])
                if previous is not None and previous[1]*r<0:
                    rt=brentq(lambda t:screen.build(mid,t,args.position,epsilon=args.epsilon)['finite_linear_screen']['normalized_direction_residual'],previous[0],fraction,xtol=2e-11)
                    root=screen.build(mid,rt,args.position,epsilon=args.epsilon)
                    report['roots'].append(root)
                previous=fraction,r
            except Exception as exc:row=dict(mid_phase=mid,fraction=fraction,error=str(exc));previous=None
            report['rows'].append(row);args.out.write_text(json.dumps(report,indent=2)+'\n')
            print(json.dumps(row),flush=True)
    accepted=[r for r in report['roots'] if abs(r['finite_linear_screen']['normalized_direction_residual'])<1e-5
              and abs(r['finite_linear_screen']['terminal_height_gain_at_exact_direction_match'])<.1
              and r['metric_diagnostics']['background_height_with_tail']<1.2]
    if accepted and args.selected_out:
        best=min(accepted,key=lambda r:abs(r['finite_linear_screen']['terminal_height_gain_at_exact_direction_match']))
        args.selected_out.write_text(json.dumps(best,indent=2)+'\n');report['selected_sha256']=fm.digest(args.selected_out)
        report['selected_output']=args.selected_out.name
    report['accepted_finite_seed_count']=len(accepted);args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(event='complete',trials=len(report['rows']),roots=len(report['roots']),accepted_finite_seeds=len(accepted))),flush=True)


if __name__=='__main__':main()
