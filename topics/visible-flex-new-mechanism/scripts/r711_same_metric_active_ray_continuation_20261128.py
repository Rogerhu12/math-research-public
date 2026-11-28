#!/usr/bin/env python3
"""Continue the natural R691 state with all-column material eigenvalue cuts."""
import argparse
from collections import Counter
import hashlib
import json
import math
import os
from pathlib import Path
import time

import numpy as np

from r675_bowed_endpoint_pose_response_20261128 import Endpoint,emit
from r685_hard_moment_physical_pose_20261128 import import_field,physical,reordered
from r691_same_metric_bowed_pose_continuation_20261128 import LocalSpace
from r711_relative_peak_correction import CompletePencil,RelativeProblem,ray_rows,rays,true_l2_row


def main():
    if (os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'
            or not os.environ.get('GITHUB_RUN_ID','').isdigit()):raise SystemExit('Public Actions required.')
    ap=argparse.ArgumentParser();ap.add_argument('--geometry',required=True);ap.add_argument('--max-seconds',required=True,type=float)
    args=ap.parse_args();opt=json.loads(Path(args.geometry).read_text());buf=Path(opt['input_state']).read_bytes();prior=json.loads(buf)
    if (hashlib.sha256(buf).hexdigest()!=opt['input_sha256'] or prior['kind']!='terminal' or prior['actual_q']!=-.004
            or prior['counts']['complete_new_nonlinear_matrices']!=62 or prior['accepted']!=58):
        raise ValueError('Incorrect R691 natural terminal.')
    start=time.monotonic();elapsed=lambda:time.monotonic()-start;count=Counter();end=Endpoint(opt,count)
    sp=LocalSpace(end,prior['actual_space']);x=np.array(prior['actual_parameters']);xp=np.array(prior['previous_secant_parameters'])
    if x.size!=4874 or xp.shape!=x.shape or not np.array_equal(sp.spl.t,prior['actual_knots']):raise ValueError('Different actual source basis.')
    q,qp,mu=prior['actual_q'],prior['previous_secant_q'],prior['next_mu']
    all_accepted=0;stages=[];current=None;old_paid=prior['independent_crossed']['both'];critical=old_paid['metric_attainer']
    emit('transport',run=46146638022,job=140984024664,source='ab93783f59cfed440fda2c25b68ef3d362d5bf32',
         literal_sha=hashlib.sha256(buf.rstrip(b'\n')).hexdigest(),old_fees=prior['counts'],old_seconds=prior['elapsed_seconds'],
         old_last_independent=old_paid,previous_mu=mu,starting_columns=sp.size,old_J_replayed=False)
    def limit():return elapsed()>args.max_seconds-opt['reserve_seconds']
    def snapshot():
        return dict(actual_q=q,previous_secant_q=qp,actual_space=sp.spec,
                    actual_knots=sp.spl.t.tolist(),actual_parameters=x.tolist(),previous_secant_parameters=xp.tolist(),
                    next_mu=mu,accepted=all_accepted,counts=dict(count),elapsed_seconds=elapsed(),continuous_t_verified=False,README_completion_claim=False)
    try:
        for stage_num,stage in enumerate(opt['stages']):
            if limit():break
            new=LocalSpace(end,stage)
            if sp.K!=new.K or not np.array_equal(sp.edges,new.edges):
                x=import_field(sp,x,new);xp=import_field(sp,xp,new);count['exact_local_space_prolongations']+=1
            sp=new
            order=reordered(sp);inv=np.argsort(order)
            phi=2*np.pi*np.arange(stage['angles'])/stage['angles'];work=sp.grid(stage['order'],len(phi),False,phi)
            # Even uniform angular quadrature includes both axes. The inherited off-grid ray is evaluated directly below.
            fp=2*np.pi*np.arange(opt['fine_angles'])/opt['fine_angles']
            fine=sp.grid(opt['fine_order'],len(fp),True,fp)
            current=physical(sp,x,fine,q);wk=physical(sp,x,work,q)
            if not(current['sampled_whole_shell_pass'] and wk['sampled_whole_shell_pass']):raise ArithmeticError('Accepted field fails a new whole-shell grid.')
            prob=RelativeProblem(sp,x,q,opt,stage,count);reason='iteration_limit';acc=0;begin=current['finite_fixed_g_eta']
            emit('begin_new_relative_problem',stage=stage_num,q=q,columns=sp.size,bulk_grid=[stage['order'],stage['angles']],
                 independent=current,mu=mu,source_cut_coordinates=critical,counts=dict(count),seconds=elapsed())
            for it in range(stage['iterations']):
                if limit():reason='budget';break
                peak=current['finite_fixed_g_eta']
                wlist=rays(sp,x,fine,q,opt);vs,cs=ray_rows(sp,x,q,wlist)
                # The independent inherited extremum was on the old 277 angular grid, not necessarily a current Gauss radius.
                if stage_num==0 and it==0:
                    from r685_hard_moment_physical_pose_20261128 import as_grid
                    og=as_grid(sp,np.array([critical[0]]),np.array([critical[1]]),np.ones(1))
                    wr=rays(sp,x,og,q,opt,True);v0,c0=ray_rows(sp,x,q,wr)
                    wlist.extend(wr);vs=np.r_[vs,v0];cs=np.vstack((cs,c0))
                l2,lJ=true_l2_row(sp,x,fine,q);w2,wJ=true_l2_row(sp,x,work,q)
                if max(abs(l2-current['finite_metric_L2']),abs(w2-wk['finite_metric_L2']))>1e-12:raise ArithmeticError('The material L2 adjoints must match both actual values.')
                A,B,check=prob.matrices(x,it==0);loss=float(A[:,-1]@A[:,-1]);improved=False
                if it==0:
                    d=np.sin(np.arange(1,sp.size+1)*.71);d/=np.linalg.norm(d);dx=d[inv];sweep=[]
                    for h in (2e-9,5e-10):
                        hi=ray_rows(sp,x+h*dx,q,wlist)[0];lo=ray_rows(sp,x-h*dx,q,wlist)[0]
                        pr=cs@d;err=np.linalg.norm((hi-lo)/(2*h)-pr)/max(np.linalg.norm(pr),1e-16)
                        lf=physical(sp,x+h*dx,fine,q)['finite_metric_L2'];rf=physical(sp,x-h*dx,fine,q)['finite_metric_L2']
                        lw=physical(sp,x+h*dx,work,q)['finite_metric_L2'];rw=physical(sp,x-h*dx,work,q)['finite_metric_L2']
                        dL=np.array([lJ@d,wJ@d]);e2=np.linalg.norm((np.array([lf-rf,lw-rw]))/(2*h)-dL)/max(np.linalg.norm(dL),1e-14)
                        sweep.append([float(err),float(e2)])
                    emit('new_relative_and_ray_differential',stage=stage_num,bulk_check=check,ray_and_l2=sweep,
                         physical_rays=wlist,start_actual_ray_values=vs.tolist())
                    if min(check)>1e-3 or np.max(np.min(sweep,axis=0))>1.e-3:raise ArithmeticError('Actual relative operator directional test failed.')
                attempts=[]
                for lam in (mu,min(opt['mu_max'],mu*4.),max(opt['mu_min'],mu*.25)):
                    if limit():break
                    pencil=CompletePencil(A,B,lam,opt['ridge']);count['new_complete_QR_SVD']+=1
                    emit('ray_pencil',stage=stage_num,iteration=it,mu=lam,ridge=pencil.ridge,
                         all_singular_values=pencil.s.tolist(),singular_extrema=[pencil.s[-1],pencil.s[0]])
                    for gain in opt['peak_reductions']:
                        if limit():break
                        ceiling=(1-gain)*peak
                        C=np.vstack((cs,lJ,wJ));h=np.r_[ceiling-vs,-gain*.015*l2,-gain*.015*w2]
                        for exchange in range(opt['exchanges']+1):
                            count['all_column_cut_models']+=1
                            step,info=pencil.direction(C,h)
                            if step is None:break
                            actual=step[inv];challenger=None
                            for fraction in opt['fractions']:
                                if limit():break
                                y=x+fraction*actual;count['new_actual_trials']+=1
                                try:
                                    ww=physical(sp,y,work,q)
                                    if not ww['sampled_whole_shell_pass']:continue
                                    dd=physical(sp,y,fine,q)
                                    if not dd['sampled_whole_shell_pass']:continue
                                    if challenger is None or dd['finite_fixed_g_eta']<challenger[0]:
                                        challenger=(dd['finite_fixed_g_eta'],y,fraction)
                                    if (ww['finite_metric_L2']>=wk['finite_metric_L2'] or ww['finite_fixed_g_eta']>=wk['finite_fixed_g_eta']
                                            or dd['finite_metric_L2']>=current['finite_metric_L2']
                                            or dd['finite_fixed_g_eta']>=peak):continue
                                    newloss=prob.merit(y)
                                    if newloss>=loss:continue
                                except FloatingPointError:continue
                                x,wk,current=y,ww,dd;mu=max(opt['mu_min'],min(opt['mu_max'],lam*(.84 if fraction>=.5 else 1.4)))
                                improved=True;all_accepted+=1;acc+=1
                                emit('accepted_actual_ray_update',stage=stage_num,iteration=it,gain=gain,exchange=exchange,
                                     dual=info,fraction=fraction,mu_used=lam,next_mu=mu,q=q,independent=current,work=wk,
                                     weighted_merit=math.sqrt(newloss),actual_parameters=x.tolist(),counts=dict(count),seconds=elapsed())
                                break
                            attempts.append(dict(mu=lam,gain=gain,exchange=exchange,dual=info,
                                                 best_feasible_peak=None if challenger is None else challenger[0]))
                            if improved or challenger is None or exchange==opt['exchanges'] or limit():break
                            _,y,fraction=challenger
                            wr=rays(sp,y,fine,q,opt,True);vplus,Jplus=ray_rows(sp,y,q,wr)
                            # The trial-selected Rayleigh direction is differentiated on that actual trial.
                            C=np.vstack((C,Jplus));h=np.r_[h,ceiling-vplus+Jplus@(fraction*step)]
                            count['actual_trial_ray_exchanges']+=1
                        if improved:break
                    del pencil
                    if improved:break
                del A,B
                if not improved:
                    reason='budget' if limit() else 'no_admissible_exchanged_cut_step'
                    emit('actual_cut_search_terminal',stage=stage_num,iteration=it,attempts=attempts,reason=reason,seconds=elapsed());break
                if current['finite_fixed_g_eta']<=opt['numerical_goal']:reason='fixed_g_numerical_goal';break
            stages.append(dict(stage=stage_num,q=q,accepted=acc,reason=reason,start_eta=begin,independent=current,columns=sp.size))
            emit('stage_terminal',stage=stages[-1],**snapshot())
            if limit():break
        crossed={}
        for k,ro,na in [('radius_only',opt['final_order'],opt['fine_angles']),('angle_only',opt['fine_order'],opt['final_angles']),('both',opt['final_order'],opt['final_angles'])]:
            crossed[k]=physical(sp,x,sp.grid(ro,na,True),q)
        emit('terminal',stages=stages,independent_crossed=crossed,**snapshot())
    except Exception as exc:
        emit('incomplete',reason=str(exc),last_physical=current,stages=stages,**snapshot());raise


if __name__=='__main__':main()
