#!/usr/bin/env python3
"""Finite linear design of a single contraction after the frozen elliptic prefix.

The new suffix avoids returning a' to zero and avoids an axial pause. Smooth
acceleration ramps and one constant-acceleration section deepen the radial
speed directly to the tail brake. This selects a NEW g; only a written selected
bundle is subsequently held fixed. No nonlinear geometry is asserted.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse,json,math,importlib.util,copy
from pathlib import Path
import numpy as np
from scipy.optimize import brentq

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
sp=importlib.util.spec_from_file_location('fd2d_frozen_monotone',HERE/'fd2d_frozen_ellipse_candidate.py')
fm=importlib.util.module_from_spec(sp);sp.loader.exec_module(fm)


def acceleration_piece(jet0,length,acc1,label):
    d0,v0,c0=jet0;delta=acc1-c0
    # a''=c0+(c1-c0)*(3*u^2-2*u^3); integrate twice exactly.
    v1=v0+length*(c0+acc1)/2
    d1=d0+length*v0+length*length*(c0/2+3*delta/20)
    jet1=[float(d1),float(v1),float(acc1)]
    return dict(kind='hermite',L=float(length),jet0=list(jet0),jet1=jet1,label=label),jet1


class Screen:
    def __init__(self,source,port):
        self.source_path=Path(source);self.port_path=Path(port)
        self.source=json.loads(self.source_path.read_text());self.port=json.loads(self.port_path.read_text())
        pieces=[]
        for p in self.source['segments']:
            if p.get('label')=='frozen_feedback_prefix' or p.get('label')=='central_cylinder':pieces.append(copy.deepcopy(p))
            else:break
        self.base=dict(self.source);self.base['segments']=pieces
        self.prefix=fm.Candidate(self.base);self.count=len(self.prefix.segments)
        self.initial_line=self.prefix.linear([1.,0.])
        self.tail=self.source['cut_reference'];r=self.tail['r'];w=self.tail['w']
        D=next(row['slope'] for row in self.port['rows'] if row['mode']==2)
        self.terminal=np.array([-w*(r*D-4)/3,1.])

    def build(self,acceleration,pdeep,transition=.04):
        bundle=copy.deepcopy(self.base);pieces=bundle['segments'];jet=list(pieces[-1]['jet1'])
        p,jet=acceleration_piece(jet,transition,-acceleration,'monotone_acceleration_entry');pieces.append(p)
        end_speed=-math.sin(pdeep);end_delta_v=-acceleration*transition/2
        plateau_speed=end_speed-end_delta_v
        duration=(plateau_speed-jet[1])/(-acceleration)
        if duration<=0:raise ValueError('Nonpositive constant-acceleration interval')
        p,jet=acceleration_piece(jet,duration,-acceleration,'monotone_acceleration_plateau');pieces.append(p)
        p,jet=acceleration_piece(jet,transition,0.,'monotone_acceleration_exit');pieces.append(p)
        phase0=math.asin(jet[1]);w=self.tail['w'];wr=self.tail['wr'];phase1=-math.atan2(1.,w)
        ps=-wr/(1+w*w)**1.5
        if phase0>=phase1:raise ValueError('The terminal brake requires a deeper initial phase')
        pieces.append(dict(kind='coast_to',p0=phase0,p1=phase0,start_from_previous=True,
                           radius_after_next=self.tail['r'],label='monotone_flat_coast'))
        pieces.append(dict(kind='brake',p0=phase0,p1=phase1,L=2*(phase1-phase0)/ps,
                           start_from_previous=True,end_from_cut=True,label='cut_second_jet_brake'))
        for name in ('linear_m2_seed','metric_diagnostics','design_parameters'):bundle.pop(name,None)
        bundle.update(schema='fd2d-frozen-ellipse-metric-v2-shared-jets',
            generated_by=Path(__file__).name,generator_sha256=fm.digest(__file__),
            monotone_design_parameters=dict(acceleration=acceleration,pdeep=pdeep,transition=transition),
            source_frozen_candidate=self.source_path.name,source_frozen_candidate_sha256=fm.digest(self.source_path),
            status=dict(metric_frozen=True,nonlinear_prefix_solved=False,nonlinear_tail_matched=False,
                        closed_surface=False,reach_certified=False,strong_target_complete=False))
        candidate=fm.Candidate(bundle);suffix=candidate.segments[self.count:]
        back=candidate.linear(self.terminal,backward=True,segments=suffix)
        determinant=self.initial_line[0]*back[1]-self.initial_line[1]*back[0]
        residual=determinant/(np.linalg.norm(self.initial_line)*np.linalg.norm(back))
        bundle['finite_linear_screen']=dict(normalized_direction_residual=float(residual),
            prefix_line=self.initial_line.tolist(),backward_at_prefix=back.tolist(),
            terminal_direction=self.terminal.tolist(),modes_matched=[2],
            scope='One finite linear mode only; not a nonlinear boundary-value solution.')
        bundle['metric_diagnostics']=candidate.metric_diagnostics()
        bundle['metric_diagnostics']['background_height_with_tail']=bundle['metric_diagnostics']['background_height']+self.port['stats']['heightSpan']
        return bundle


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source',type=Path,default=ROOT/'notes/2026-11-12-fd2d-ellipse-b05-frozen-candidate-v2.json')
    p.add_argument('--port',type=Path,default=ROOT/'notes/2026-11-12-fd2d-ellipse-cuff032-cut04-port.json')
    p.add_argument('--out',type=Path,required=True);p.add_argument('--selected-out',type=Path)
    args=p.parse_args();screen=Screen(args.source,args.port)
    report=dict(scope=__doc__,source_sha256=fm.digest(__file__),source_candidate_sha256=fm.digest(args.source),rows=[],roots=[])
    for acc in (1.6,1.9,2.1,2.25):
        previous=None
        for phase in (1.475,1.50,1.54,1.568):
            try:
                b=screen.build(acc,phase);res=b['finite_linear_screen']['normalized_direction_residual']
                row=dict(acceleration=acc,pdeep=phase,residual=res,metric=b['metric_diagnostics'])
                if previous is not None and previous[1]*res<0:
                    root=brentq(lambda x:screen.build(acc,x)['finite_linear_screen']['normalized_direction_residual'],
                                previous[0],phase,xtol=2e-10)
                    good=screen.build(acc,root);report['roots'].append(good)
                previous=phase,res
            except Exception as exc:
                row=dict(acceleration=acc,pdeep=phase,error=str(exc));previous=None
            report['rows'].append(row);args.out.write_text(json.dumps(report,indent=2)+'\n')
            print(json.dumps(row),flush=True)
    if report['roots'] and args.selected_out:
        chosen=min(report['roots'],key=lambda r:r['metric_diagnostics']['background_height_with_tail'])
        args.selected_out.write_text(json.dumps(chosen,indent=2)+'\n')
        report['selected_output']=args.selected_out.name;report['selected_sha256']=fm.digest(args.selected_out)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(event='complete',trials=len(report['rows']),finite_linear_roots=len(report['roots']))),flush=True)


if __name__=='__main__':main()
