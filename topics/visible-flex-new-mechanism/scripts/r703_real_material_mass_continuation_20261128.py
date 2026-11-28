#!/usr/bin/env python3
"""Actual 1604-coordinate R687 successor with two auxiliary gauges and true material derivatives."""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import time
from types import SimpleNamespace
import numpy as np
from scipy.linalg import qr,svd
from r669_true_finite_tilt_reach_continuation_20261128 import trust_step
from r703_transported_lattice_anchor import CalibratedGrid,transported
from r703_weighted_material_field import Space,Field,frozen_for
from r703_material_geometry_observer import objective,read,transport_cost


def public():
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public' or not os.environ.get('GITHUB_RUN_ID','').isdigit():
        raise SystemExit('Public scientific runner required.')


def emit(kind,**d):
    print(json.dumps(dict(kind=kind,**d),sort_keys=True,allow_nan=False),flush=True)


def main():
    public();ap=argparse.ArgumentParser();ap.add_argument('--geometry',required=True);ap.add_argument('--max-seconds',type=int,required=True);args=ap.parse_args()
    opt=json.loads(Path(args.geometry).read_text());raw=Path(opt['input_state']).read_bytes();src=json.loads(raw)
    if (hashlib.sha256(raw).hexdigest()!=opt['input_state_sha256'] or src['run']!=46146623642 or src['fixed_metric'] is not None
            or len(src['all_parameters'])!=1604 or src['packed_le_float64_sha256']!=hashlib.sha256(np.asarray(src['all_parameters'],dtype='<f8').tobytes()).hexdigest()):
        raise ValueError('Missing full R687 natural terminal.')
    start=time.perf_counter();elapsed=lambda:time.perf_counter()-start;count=Counter();frozen=None;history=[];accepted=0;trust=opt['trust']
    schedules=list(opt['stages']);sp=Space(schedules[0]['spans'],schedules[0]['K']);x=np.zeros(sp.size);phase=0.;last=None;mu0=0.
    grids={};targets={}
    def grid(spans,order,N):
        key=(spans,order,N)
        if key not in grids:grids[key]=CalibratedGrid(src,order,N,spans,count)
        return grids[key]
    def target(g,binding=None):
        f=frozen if binding is None else binding
        if f is None:return None
        old,fx,refN=f;key=(g.r.tobytes(),old.spans,old.K,refN,fx.tobytes())
        if key not in targets:
            psi=2*np.pi*np.arange(refN)/refN
            support=SimpleNamespace(r=g.r,phi=psi,anchor=transported(src,g.r,psi,count))
            targets[key]=frozen_for(Field(old,support),fx);count['independent_fixed_E_evaluators']+=1
        return targets[key]
    def field(g):return Field(sp,g)
    def observe(g,y,lev,detail=False,binding=None):
        st=field(g).state(y,lev,target(g,binding));count['physical_readouts']+=1
        val=read(g,st,opt['fine_betas']);mer=objective(g,st,lev,opt)
        if detail: return val,float(np.linalg.norm(mer)),st
        return val,float(np.linalg.norm(mer))
    def gate(d):
        return d['sampled_whole_shell_pass'] and d['sampled_rotational_eta']<=opt['freeze_eta'] and d['true_ring_closure']<=opt['freeze_eta'] and d['true_angular_length_margin']>=0
    def candidate_acceptable(w,c,w0,c0):
        if w0['sampled_whole_shell_pass'] and c0['sampled_whole_shell_pass']:
            return w['sampled_whole_shell_pass'] and c['sampled_whole_shell_pass']
        return all(y['sampled_whole_shell_pass'] or y['sampled_shell_violation']<o['sampled_shell_violation'] for y,o in ((w,w0),(c,c0)))
    def clean_grids():
        # A complete readout is already emitted on each new grid; cached source reconstructions are stage-local.
        grids.clear();targets.clear()
    try:
        g0=grid(sp.spans,opt['check_order'],opt['check_angles']);forward=field(g0)
        original=forward.state(x,0.,old_slope=True);soft=forward.state(x,0.)
        emit('transported_actual_source',original_run=src['run'],original_seconds=src['elapsed_seconds'],original_counts=src['counts'],
             original_parameter_sha=src['packed_le_float64_sha256'],transport=transport_cost(g0,original,soft),
             raw_projected=read(g0,original,opt['fine_betas']),C2_softened=read(g0,soft,opt['fine_betas']),elapsed_seconds=elapsed())
        del original,soft;last=None;done=0
        while done<len(schedules):
            stage=schedules[done]
            if elapsed()>args.max_seconds-opt['reserve_seconds']:break
            old=sp;new=Space(stage['spans'],stage['K'])
            if (old.spans,old.K)!=(new.spans,new.K):
                x=new.prolong(old,x);count['exact_new_coordinate_prolongations']+=1;clean_grids()
            sp=new;phase=stage['level']
            g=grid(sp.spans,stage['order'],stage['angles']);fine=grid(sp.spans,opt['check_order'],opt['check_angles'])
            work=field(g);ref=target(g);free=np.arange(sp.size) if frozen is None else sp.frozen_columns()
            if frozen is not None and (np.min(abs(ref['slope_mean']))<1e-7 or np.any(ref['slope_mean']*ref['slope_mean'][0]<=0)):
                raise ArithmeticError('Frozen mean slope chart lost its nonzero moment; a different exact scale gauge is needed.')
            checked,indnorm=observe(fine,x,phase);nacc=0;why='iteration_limit';start_eta=checked['sampled_rotational_eta']
            st=work.state(x,phase,ref);wk=read(g,st,opt['work_betas'])
            emit('new_material_phase',i=done,level=phase,space=[sp.spans,sp.K],original_columns=sp.size,all_independent_columns=len(free),
                 is_frozen=frozen is not None,initial=checked,actual_parameters=x.tolist(),seconds=elapsed())
            for it in range(stage['iterations']):
                if elapsed()>args.max_seconds-opt['reserve_seconds']:why='scientific_budget';break
                st=work.state(x,phase,ref);vec,keep=objective(g,st,phase,opt,True);loss=float(vec@vec);root=st['root']
                h=2.e-24;mat=np.empty((int(keep.sum()),len(free)),order='F')
                for j,idx in enumerate(free):
                    y=x.astype(complex);y[idx]+=1j*h
                    val=objective(g,work.state(y,phase,ref,root),phase,opt)
                    mat[:,j]=val.imag[keep]/h
                count['complete_new_material_J']+=1;count['all_independent_complex_columns']+=len(free)
                if it==0:
                    direction=np.cos(np.arange(1,len(free)+1)*.731);direction/=np.linalg.norm(direction);dvec=np.zeros_like(x);dvec[free]=direction
                    predicted=mat@direction;errs=[]
                    for step in (2.e-6,4.e-7):
                        hi=objective(g,work.state(x+step*dvec,phase,ref),phase,opt);lo=objective(g,work.state(x-step*dvec,phase,ref),phase,opt)
                        errs.append(float(np.linalg.norm((hi-lo)[keep]/(2*step)-predicted)/max(np.linalg.norm(predicted),1.e-15)))
                    emit('all_column_physical_derivative',stage=done,relative=errs,rows=mat.shape[0],columns=len(free))
                    if min(errs)>.0002:raise ArithmeticError('New full material derivative fails its independent directional comparison.')
                Q,R=qr(mat,mode='economic',check_finite=False,overwrite_a=True);rhs=Q.T@vec[keep];del Q,mat
                u,s,v=svd(R,full_matrices=False,check_finite=False);force=-(u.T@rhs);count['complete_new_QR_SVD']+=1
                if it==0:emit('all_singular_values',stage=done,values=s.tolist())
                ok=False;least=max(1.e-17,(float(s[0])**2)*2.e-13)
                for _ in range(15):
                    dx,pred,mu=trust_step(s,v,force,trust,least);y=x.copy();y[free]+=dx;count['actual_new_trials']+=1
                    try:
                        trial=work.state(y,phase,ref);vv=objective(g,trial,phase,opt);newloss=float(vv@vv)
                        if pred>0 and newloss<loss:
                            rw=read(g,trial,opt['work_betas']);rr,en=observe(fine,y,phase)
                            if en<indnorm and candidate_acceptable(rw,rr,wk,checked):
                                ratio=(loss-newloss)/pred;x=y;wk,checked,indnorm=rw,rr,en;nacc+=1;accepted+=1;ok=True;mu0=mu
                                if ratio>.75:trust=min(opt['max_trust'],trust*1.45)
                                elif ratio<.2:trust*=.65
                                emit('accepted_new_material_parameters',stage=done,iteration=it,total_accepted=accepted,level=phase,
                                     work_norm=newloss**.5,independent_norm=en,independent=rr,actual_parameters=x.tolist(),
                                     damping=mu,trust=trust,counts=dict(count),seconds=elapsed());break
                    except FloatingPointError as exc:count['unaccepted_domain_trials']+=1
                    trust*=.43
                    if trust<1.e-12:break
                if not ok:
                    why='unaccepted_trust_region';break
                if gate(checked) and indnorm<opt['goal']:
                    why='numerical_goal';break
            endg=grid(sp.spans,opt['stage_order'],opt['stage_angles']);last,stage_norm=observe(endg,x,phase)
            info=dict(stage=done,level=phase,columns=sp.size,independent_columns=len(free),accepted=nacc,reason=why,start_eta=start_eta,
                      fixed=frozen is not None,full=last,norm=stage_norm)
            history.append(info);emit('material_stage_terminal',**info,parameters=x.tolist(),counts=dict(count),seconds=elapsed())
            if phase==1. and frozen is None and gate(last) and gate(checked):
                proposal=(sp,x.copy(),opt['reference_angles'])
                try:
                    # Check precisely the proposed immutable quadrature-defined E on both independent grids.
                    a1,_=observe(endg,x,1.,binding=proposal);a2,_=observe(fine,x,1.,binding=proposal)
                    gauge=target(endg,proposal)['slope_mean']
                    good=np.min(abs(gauge))>1e-7 and np.all(gauge*gauge[0]>0)
                    if gate(a1) and gate(a2) and good:
                        frozen=proposal;future=dict(opt['fixed_stage'],K=sp.K+2,spans=2*sp.spans)
                        schedules=schedules[:done+1]+[future]
                        emit('actual_E_frozen',space=[sp.spans,sp.K],parameters=x.tolist(),reference_angles=opt['reference_angles'],fixed_read=a1)
                except FloatingPointError as exc:emit('proposed_E_unavailable',reason=str(exc))
            done+=1
            if done<len(schedules):trust=max(trust,opt['retarget_trust'])
            if why=='scientific_budget':break
        crossed={}
        for name,order,M in [('radial_only',opt['final_order'],opt['stage_angles']),('angle_only',opt['stage_order'],opt['final_angles']),
                             ('both',opt['final_order'],opt['final_angles'])]:
            gg=grid(sp.spans,order,M);crossed[name]=observe(gg,x,phase)[0]
            emit('actual_crossed_read',name=name,data=crossed[name],seconds=elapsed())
        emit('terminal',original_source=src['literal_final_sha256'],actual_space=[sp.spans,sp.K],all_parameters=x.tolist(),attempted_level=phase,
             frozen=None if frozen is None else dict(space=[frozen[0].spans,frozen[0].K],reference_parameters=frozen[1].tolist(),reference_angles=frozen[2]),
             stages=history,actual_accepted=accepted,trust=trust,last_accepted_mu=mu0,independent_crossed=crossed,counts=dict(count),
             elapsed_seconds=elapsed(),continuous_metric_certified=False,README_completion_claim=False)
    except Exception as exc:
        emit('incomplete',reason=str(exc),actual_space=[sp.spans,sp.K],all_parameters=x.tolist(),attempted_level=phase,counts=dict(count),
             last=last,elapsed_seconds=elapsed(),README_completion_claim=False);raise


if __name__=='__main__':main()
