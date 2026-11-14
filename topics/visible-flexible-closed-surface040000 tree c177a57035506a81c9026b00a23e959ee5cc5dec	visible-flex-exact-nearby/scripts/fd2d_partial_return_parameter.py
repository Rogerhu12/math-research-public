#!/usr/bin/env python3
"""Physical coast-length parameter and exact piece-chart JVP for frozen v4.

T changes one shallow coast. The final deep coast compensates its radial
drop so every candidate has the SAME cut radius and first/second jets.
The parameter is for outer nonlinear design, not for a claimed isometric
family: a(s) changes with T and must be frozen after a solution is selected.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse,json,math,copy,hashlib,importlib.util
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
sp=importlib.util.spec_from_file_location('fd2d_parameter_frozen',HERE/'fd2d_frozen_ellipse_candidate.py')
fm=importlib.util.module_from_spec(sp);sp.loader.exec_module(fm)


class PartialReturnParameter:
    def __init__(self,source=ROOT/'notes/2026-11-12-fd2d-ellipse-b05-frozen-candidate-v4.json'):
        self.source=Path(source);self.original=json.loads(self.source.read_text());self.base=fm.Candidate(self.original)
        labels={p.get('label'):i for i,p in enumerate(self.base.segments)}
        self.shallow=labels['partial_return_matching_coast'];self.down=labels['redeepen_after_partial_return']
        self.deep=labels['final_deep_coast'];self.brake=labels['cut_second_jet_brake']
        self.T0=self.base.segments[self.shallow]['L']
        self.vm=math.sin(self.base.segments[self.shallow]['p0']);self.cm=math.cos(self.base.segments[self.shallow]['p0'])
        self.vd=math.sin(self.base.segments[self.deep]['p0']);self.cd=math.cos(self.base.segments[self.deep]['p0'])
        self.deep_length0=self.base.segments[self.deep]['L']
        self.deep_length_derivative=-self.vm/self.vd
        self.Tmax=self.T0-self.deep_length0/self.deep_length_derivative
        self.total_length_derivative=1+self.deep_length_derivative
        self.background_height_derivative=self.cm+self.cd*self.deep_length_derivative
        self.height0=self.base.metric_diagnostics()['background_height']
        self.tail_height=float(self.original['cut']['tail_height_span'])

    def bundle(self,T):
        T=float(T)
        if not 0<=T<self.Tmax:raise ValueError('T must satisfy 0 <= T < radial-coast Tmax')
        out=copy.deepcopy(self.original);out['segments'][self.shallow]['L']=T
        out['partial_return_design_parameters']['coast_length']=T
        out['partial_return_design_parameters']['fraction']=T/self.Tmax
        out['physical_parameter']=dict(name='partial_return_coast_length',T=T,T0=self.T0,
            source_file=self.source.name,source_sha256=fm.digest(self.source),generator=Path(__file__).name,
            generator_sha256=fm.digest(__file__),requires_new_fixed_metric_validation=True)
        for key in ('finite_linear_screen','metric_diagnostics'):out.pop(key,None)
        out['status']=dict(metric_frozen=False,nonlinear_prefix_solved=False,nonlinear_tail_matched=False,
            closed_surface=False,reach_certified=False,strong_target_complete=False)
        return out

    def candidate(self,T):return fm.Candidate(self.bundle(T))

    def piece_jets(self,index,tau,T=None):
        if T is None:T=self.T0
        candidate=self.candidate(T);p=candidate.segments[index];tau=np.asarray(tau,dtype=float)
        if np.any((tau<0)|(tau>1)):raise ValueError('Normalized piece coordinate must lie in [0,1]')
        s=p['s0']+p['L']*tau;a,v,acc=candidate.profile(s)
        length_T=1. if index==self.shallow else self.deep_length_derivative if index==self.deep else 0.
        if index<=self.shallow:s0_T=0.
        elif index<=self.deep:s0_T=1.
        else:s0_T=self.total_length_derivative
        if index<self.shallow:a_T=np.zeros_like(tau)
        elif index==self.shallow:a_T=self.vm*tau
        elif index<self.deep:a_T=np.zeros_like(tau)+self.vm
        elif index==self.deep:a_T=self.vm*(1-tau)
        else:a_T=np.zeros_like(tau)
        zero=np.zeros_like(tau)
        return dict(a=a,a_s=v,a_ss=acc,a_T=a_T,a_s_T=zero,a_ss_T=zero,
            length=p['L'],length_T=length_T,s0=p['s0'],s0_T=s0_T,
            s=s,s_T=s0_T+length_T*tau,K=-acc/a,K_T=acc*a_T/a**2,
            c=v/a,c_T=-v*a_T/a**2)

    def summary(self):
        return dict(source_file=self.source.name,source_sha256=fm.digest(self.source),T0=self.T0,
            vm=self.vm,vd=self.vd,deep_length_at_T0=self.deep_length0,
            full_radial_feasible_interval=[0.,self.Tmax],suggested_outer_design_interval=[0.,.08],
            deep_length_T=self.deep_length_derivative,total_length_T=self.total_length_derivative,
            background_height_T=self.background_height_derivative,
            background_height_with_tail_at_T0=self.height0+self.tail_height,
            background_height_with_tail_at_0=self.height0+self.tail_height-self.background_height_derivative*self.T0,
            background_height_with_tail_at_008=self.height0+self.tail_height+self.background_height_derivative*(.08-self.T0),
            variable_indices=dict(shallow=self.shallow,down=self.down,deep=self.deep,brake=self.brake),
            cut_jets_fixed=True,core_a0_fixed=True,whole_metric_fixed_across_T=False,
            actual_nonlinear_height_or_curvature_bound=False)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    model=PartialReturnParameter();tau=np.linspace(0,1,17);step=1e-6
    plus=model.candidate(model.T0+step);minus=model.candidate(model.T0-step)
    errors=dict(a=0.,a_s=0.,a_ss=0.,length=0.,s0=0.,K=0.,c=0.)
    for j in range(len(model.base.segments)):
        jets=model.piece_jets(j,tau)
        pp=plus.segments[j];pm=minus.segments[j]
        ap,vp,cp=plus.profile(pp['s0']+pp['L']*tau);am,vm,cm=minus.profile(pm['s0']+pm['L']*tau)
        for key,fp,fm_,target in (('a',ap,am,jets['a_T']),('a_s',vp,vm,jets['a_s_T']),
            ('a_ss',cp,cm,jets['a_ss_T']),('K',-cp/ap,-cm/am,jets['K_T']),('c',vp/ap,vm/am,jets['c_T'])):
            errors[key]=max(errors[key],float(np.max(abs((fp-fm_)/(2*step)-target))))
        errors['length']=max(errors['length'],abs((pp['L']-pm['L'])/(2*step)-jets['length_T']))
        errors['s0']=max(errors['s0'],abs((pp['s0']-pm['s0'])/(2*step)-jets['s0_T']))
    out=dict(scope=__doc__,source_sha256=fm.digest(__file__),summary=model.summary(),
        finite_jvp_check=dict(step=step,piece_samples=17,max_absolute_errors=errors),
        source_dependency_sha256=fm.digest(HERE/'fd2d_frozen_ellipse_candidate.py'))
    args.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))


if __name__=='__main__':main()
