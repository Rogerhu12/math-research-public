#!/usr/bin/env python3
"""Actual nonlinear q=-.004 continuation on the unchanged R673 metric."""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
import math
import os
from pathlib import Path
import time
import numpy as np
from scipy.interpolate import BSpline
from scipy.linalg import qr,svd
from r675_bowed_endpoint_pose_response_20261128 import Endpoint, ResponseSpace, dot, emit, pack, plus
from r685_hard_moment_physical_pose_20261128 import (RadialQR,as_grid,import_field,metric_defect,operators,
                                                       physical,relative_curvature_map,reordered)


def positive(x,width):
    y=np.maximum(0.,x); v=width/np.maximum(y,1e-100); z=np.exp(-v)
    return y*z,(1+v)*z


class LocalSpace(ResponseSpace):
    def __init__(self,end,spec):
        super().__init__(end,[16,32,16],spec['K']);self.spec=spec
        pts=list(self.edges)
        for i,fan in enumerate(spec['inner_subdivisions']):
            pts.extend(np.linspace(self.edges[i],self.edges[i+1],fan+1)[1:-1])
        self.edges=np.asarray(sorted(pts)); knots=np.r_[[end.a]*5,self.edges,[end.b]*5]
        full=len(knots)-6;self.spl=BSpline(knots,np.eye(full),5);self.nb=full-6;self.size=self.nb*len(self.blocks)+2


def tensors(raw,r,T0):
    D,Y,n,_=relative_curvature_map(raw,r); rd=r[:,None,None]
    e,f,g=dot(D,D),dot(D,Y),dot(Y,Y); L,M,N=dot(n,raw[3]),dot(n,raw[4]/rd),dot(n,raw[5]/rd**2)
    area=dot(np.cross(D,Y),np.cross(D,Y)); tr=(g*L-2*f*M+e*N)/area
    result=[]; deriv=[]
    for sign in (1,-1):
        t=sign*T0; aa,ab,bb=e+t*L,f+t*M,g+t*N; det=(aa*bb-ab*ab)/area
        result.extend((1+t*tr/2,det))
        deriv.append(([t*(N-tr*g)/(2*area),t*(-M+tr*f)/area,t*(L-tr*e)/(2*area)],
                      [t*g/(2*area),-t*f/area,t*e/(2*area)]))
        deriv.append(([(bb-det*g)/area,(-2*ab+2*det*f)/area,(aa-det*e)/area],
                      [t*bb/area,-2*t*ab/area,t*aa/area]))
    return result,deriv


def physical_state(sp,x,g,q):return plus(g['state'](q),sp.fields(x,g))


def weights_grid(g):
    n=len(g['phi']); w=np.sqrt(g['weights'][:,None]/n)*np.ones((1,n));return w,np.stack((w,math.sqrt(2)*w,w))


def rows(sp,x,g,q,base,opts,scale,J=False,indices=None,force_masks=None,vector=False):
    raw=physical_state(sp,x,g,q);metric=np.asarray(metric_defect(raw,g['raw'],g['r']));w,ww=weights_grid(g)
    vals,der=tensors(raw,g['r'],opts['T']); squared=metric[0]**2+2*metric[1]**2+metric[2]**2
    peak=opts['peak_weight']/scale; costs=[(metric*ww).ravel(),(w*peak*squared).ravel()]
    if J:
        ids,A,B=operators(sp,g,raw,indices); ncol=len(ids); parts=[(A*ww[...,None]).reshape(-1,ncol)]
        p=2*peak*(metric[0,...,None]*A[0]+2*metric[1,...,None]*A[1]+metric[2,...,None]*A[2]);parts.append((w[...,None]*p).reshape(-1,ncol))
    masks=[]
    for i,(guard,v,(ag,bg)) in enumerate(zip(base,vals,der)):
        loss,dc=positive(guard-v,opts['smooth_width']); need=dc>0 if force_masks is None else force_masks[i];masks.append(need)
        # At every omitted row BOTH its residual and derivative are identically (or machine) zero.
        if need.any():
            costs.append((w*opts['cone_weight']*loss)[need])
            if J:
                dv=sum(a[need,None]*A[j][need]+b[need,None]*B[j][need] for j,(a,b) in enumerate(zip(ag,bg)))
                parts.append(-(w*opts['cone_weight']*dc)[need,None]*dv)
    rhs=np.concatenate(costs)
    if not J:return rhs if vector else float(rhs@rhs)
    return ids,np.column_stack((np.vstack(parts),rhs)),np.column_stack(((B*ww[...,None]).reshape(-1,ncol),np.zeros(B.shape[0]*B.shape[1]*B.shape[2]))),masks


class Problem:
    def __init__(self,sp,xanchor,q,opts,stage,count):
        self.sp,self.q,self.opts,self.count=sp,q,opts,count;self.data=[]
        z,w=np.polynomial.legendre.leggauss(stage['order']);ph=2*np.pi*np.arange(stage['angles'])/stage['angles']
        exp=sp.spl.t[np.arange(sp.nb)+9]
        for i,(lo,hi) in enumerate(zip(sp.edges[:-1],sp.edges[1:])):
            r=(lo+hi+(hi-lo)*z)/2;g=as_grid(sp,r,ph,(hi-lo)*w/(2*sp.scale))
            ref,_=tensors(physical_state(sp,xanchor,g,q),r,opts['T'])
            guards=[np.minimum(cap,opts['guard_fraction']*val) for cap,val in zip((.32,.24,.32,.24),ref)]
            active=np.nonzero(np.max(abs(g['b'][0]),axis=0)>0)[0]; dead=np.flatnonzero(exp<=hi+1e-14)
            stop=sp.size if i==len(sp.edges)-2 else ((dead[-1]+1)*len(sp.blocks)-1 if len(dead) else -1)
            self.data.append((g,guards,active,stop))

    def matrices(self,x,scale,check=False):
        sp=self.sp; left,right=RadialQR(sp.size,self.count),RadialQR(sp.size,self.count)
        if check:
            v=np.sin(np.arange(1,sp.size+1)*.479);v/=np.linalg.norm(v);phys=v[np.argsort(reordered(sp))]
            sizes=[min(3e-9,max(5e-12,scale*.0002)),min(8e-10,max(2e-12,scale*.00005))]
            num=np.zeros(2);den=np.zeros(2)
        for g,guards,active,stop in self.data:
            ids,A,B,masks=rows(sp,x,g,self.q,guards,self.opts,scale,True,active)
            if check:
                exact=A[:,:-1]@v[ids]
                for j,h in enumerate(sizes):
                    fp=rows(sp,x+h*phys,g,self.q,guards,self.opts,scale,force_masks=masks,vector=True)
                    fm=rows(sp,x-h*phys,g,self.q,guards,self.opts,scale,force_masks=masks,vector=True)
                    fd=(fp-fm)/(2*h);num[j]+=np.sum((fd-exact)**2);den[j]+=np.sum(exact**2)
            ids=np.r_[ids,sp.size]
            left.add(ids,A,stop);right.add(ids,B,stop)
        if left.carry.size or right.carry.size:raise ArithmeticError('Unfinished complete physical span QR.')
        self.count['complete_new_nonlinear_matrices']+=1;self.count['original_columns']+=sp.size
        return left.square,right.square,(np.sqrt(num/np.maximum(den,1e-25)).tolist() if check else [])

    def merit(self,x,scale):
        return sum(rows(self.sp,x,g,self.q,base,self.opts,scale) for g,base,_,_ in self.data)


def direction(A,B,mu):
    both=np.asfortranarray(np.vstack((A[:,:-1],mu*B[:,:-1])));rhs=np.r_[A[:,-1],mu*B[:,-1]]
    ss=np.linalg.norm(both,axis=0);ss=np.where(ss>0,ss,1.);both/=ss
    Q,R=qr(both,mode='economic',overwrite_a=True,check_finite=False);force=Q.T@rhs;del Q,both
    U,sv,vt=svd(R,full_matrices=False,check_finite=False);f=U.T@force
    y=-(vt.T@np.divide(f,sv,where=sv!=0,out=np.zeros_like(f)))/ss
    return y,sv


def main():
    if (os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'
            or not os.environ.get('GITHUB_RUN_ID','').isdigit()):raise SystemExit('Scientific execution requires public Actions.')
    ap=argparse.ArgumentParser();ap.add_argument('--geometry',required=True);ap.add_argument('--max-seconds',required=True,type=float)
    args=ap.parse_args();opt=json.loads(Path(args.geometry).read_text());prior=json.loads(Path(opt['input_state']).read_text())
    if prior['run']!=46144003761 or prior['q']!=-.004 or len(prior['parameters'])!=3152:raise ValueError('Incorrect actual fixed-g source.')
    start=time.perf_counter(); elapsed=lambda:time.perf_counter()-start;count=Counter();end=Endpoint(opt,count)
    sp=LocalSpace(end,opt['stages'][0]);x=np.asarray(prior['parameters']);xref=x.copy();xp=np.asarray(prior['previous_parameters']);q=prior['q'];qp=prior['previous_q'];nacc=0
    eps=opt['numerical_goal'];strict_refined=False;eta_seen=False;refinement_paid=False;history=[];last=None;mu=prior['last_step_mu']
    emit('provenance',actual_source_run=prior['run'],source_costs=prior['counts'],source_scientific_seconds=prior['seconds'],
         prior_accepted=12,initial_original_columns=sp.size,fixed_metric='unchanged complete R673 positive endpoint g+',
         source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    try:
        program=list(opt['stages'])
        for i,s in enumerate(program):
            if elapsed()>args.max_seconds-opt['reserve_seconds']:break
            proposed=s.get('new_q',q)
            if proposed!=q and not strict_refined:
                emit('expansion_not_attempted',stage=i,strict_same_metric_refinement=False);break
            oldsp=sp;newsp=LocalSpace(end,s)
            if newsp.size!=sp.size or not np.array_equal(newsp.edges,sp.edges):
                x=import_field(sp,x,newsp);xref=import_field(sp,xref,newsp);xp=import_field(sp,xp,newsp);sp=newsp;count['exact_local_space_prolongations']+=1
            fine=sp.grid(opt['fine_order'],opt['fine_angles'],True);work=sp.grid(s['order'],s['angles'])
            if proposed!=q:
                choices=[]
                for t in (0.,.5,1.):
                    y=x+t*(proposed-q)/(q-qp)*(x-xp)
                    try: ck=physical(sp,y,fine,proposed);wk=physical(sp,y,work,proposed)
                    except FloatingPointError:continue
                    if ck['sampled_whole_shell_pass'] and wk['sampled_whole_shell_pass']:choices.append((ck['finite_metric_L2'],t,y))
                if not choices:emit('no_feasible_expansion_predictor',stage=i,q=proposed);break
                old=x.copy(); _,t,x=min(choices,key=lambda z:z[0]);qp,q=q,proposed;xp=old;xref=x.copy();strict_refined=False;eta_seen=False;refinement_paid=False
            check=physical(sp,x,fine,q); wk0=physical(sp,x,work,q)
            if not(check['sampled_whole_shell_pass'] and wk0['sampled_whole_shell_pass']):
                raise ArithmeticError('Actual continued state failed its independent whole geometry gate.')
            # Reconstruct the SAME source shell to define a real safety reserve, not a moving active-peak index.
            prob=Problem(sp,xref,q,opt,s,count);order=reordered(sp);count_stage=0;why='iteration_limit';beg=check['finite_fixed_g_eta']
            emit('actual_continuation_stage',stage=i,q=q,original_columns=sp.size,radial_intervals=len(sp.edges)-1,modes=sp.K,
                 actual_parameters=x.tolist(),independent=check,previous_mu=mu,source_is_unchanged=(i==0))
            for it in range(s['iterations']):
                if elapsed()>args.max_seconds-opt['reserve_seconds']:why='scientific_budget';break
                scale=max(check['finite_fixed_g_eta'],1e-13); A,B,checks=prob.matrices(x,scale,check=(it==0));loss=float(A[:,-1]@A[:,-1])
                if it==0:
                    emit('complete_physical_residual_differential',stage=i,columns=sp.size,relative_errors=checks)
                    if min(checks)>8e-4:raise ArithmeticError('New all-column cone and quartic residual differential mismatch.')
                improved=False
                trials_mu=list(dict.fromkeys([mu,max(opt['mu_min'],mu*.32),min(opt['mu_max'],mu*3.5)]))
                for trialmu in trials_mu:
                    if elapsed()>args.max_seconds-opt['reserve_seconds']:break
                    p,sv=direction(A,B,trialmu);count['full_original_QR_SVD']+=1;dx=p[np.argsort(order)]
                    if it==0:emit('new_stage_singular_values',stage=i,q=q,mu=trialmu,values=sv.tolist())
                    for f in (1.,.6,.35,.18,.09,.045,.02,.009,.004,.0015):
                        y=x+f*dx;count['actual_fixed_metric_trials']+=1
                        try:
                            ww=physical(sp,y,work,q)
                            if not ww['sampled_whole_shell_pass'] or ww['finite_metric_L2']>=wk0['finite_metric_L2']:continue
                            cc=physical(sp,y,fine,q)
                            if not(cc['sampled_whole_shell_pass'] and cc['finite_metric_L2']<check['finite_metric_L2'] and cc['finite_fixed_g_eta']<check['finite_fixed_g_eta']):continue
                            ml=prob.merit(y,scale)
                        except FloatingPointError:continue
                        if not ml<loss:continue
                        oldeta=check['finite_fixed_g_eta'];x,wk0,check=y,ww,cc;count_stage+=1;nacc+=1;improved=True
                        if f>=.6 and cc['sampled_whole_shell_margins']['curvature']>2.4 and cc['finite_fixed_g_eta']>.90*oldeta:
                            mu=max(opt['mu_min'],trialmu*.67)
                        elif f<.18 or cc['sampled_whole_shell_margins']['curvature']<1.2:
                            mu=min(opt['mu_max'],trialmu*1.5)
                        else:mu=trialmu
                        emit('actual_same_g_accepted',stage=i,iteration=it,q=q,accepted=nacc,mu_used=trialmu,next_mu=mu,
                             fraction=f,actual_parameters=x.tolist(),independent=check,weighted_merit=math.sqrt(ml),
                             singular_extrema=[float(sv[-1]),float(sv[0])],elapsed_seconds=elapsed());break
                    if improved:break
                if not improved:why='no_improving_admissible_step';break
                if check['finite_fixed_g_eta']<=eps:why='solver_tolerance';break
            cross=physical(sp,x,sp.grid(opt['final_order'],opt['final_angles'],True),q)
            eta_seen|=(check['finite_fixed_g_eta']<=1e-6 and cross['finite_fixed_g_eta']<=1e-6 and cross['sampled_whole_shell_pass'])
            refinement_paid|=(eta_seen and i>0 and sp.size>3152 and count_stage>0 and cross['finite_fixed_g_eta']<=eps
                               and check['finite_fixed_g_eta']<=eps and cross['sampled_whole_shell_pass'] and check['finite_fixed_g_eta']<beg)
            # A historical pass never qualifies a different current field for angle expansion.
            strict_refined=(refinement_paid and cross['finite_fixed_g_eta']<=eps and check['finite_fixed_g_eta']<=eps
                            and cross['sampled_whole_shell_pass'] and check['sampled_whole_shell_pass'])
            last=cross;history.append(dict(stage=i,q=q,accepted=count_stage,reason=why,start_eta=beg,independent=cross,original_columns=sp.size,
                                           one_ppm_seen=eta_seen,paid_same_g_refinement=refinement_paid,strict_same_g_refinement=strict_refined));emit('actual_stage_terminal',**history[-1],
                                 actual_parameters=x.tolist(),counts=dict(count),mu=mu,elapsed_seconds=elapsed())
        grids={}
        for label,no,na in [('radius_only',opt['final_order'],opt['fine_angles']),('angle_only',opt['fine_order'],opt['final_angles']),('both',opt['final_order'],opt['final_angles'])]:
            grids[label]=physical(sp,x,sp.grid(no,na,True),q)
        emit('terminal',actual_q=q,previous_secant_q=qp,actual_parameters=x.tolist(),previous_secant_parameters=xp.tolist(),
             actual_space=sp.spec,actual_knots=sp.spl.t.tolist(),accepted=nacc,next_mu=mu,stages=history,independent_crossed=grids,
             counts=dict(count),elapsed_seconds=elapsed(),continuous_t_verified=False,README_completion_claim=False)
    except Exception as exc:
        emit('incomplete',reason=str(exc),q=q,actual_parameters=x.tolist(),actual_space=sp.spec,counts=dict(count),elapsed_seconds=elapsed());raise


if __name__=='__main__':main()
