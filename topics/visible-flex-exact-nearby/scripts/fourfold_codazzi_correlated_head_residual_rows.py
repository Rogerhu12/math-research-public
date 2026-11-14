#!/usr/bin/env python3
"""Joint radial-polynomial residuals for the actual full regular q/psi.

Each original full Hermite trial supplies its mean as an approximation.
The two scalar residuals then drive exact mean-error equations.  No mean
is discarded and no independent interval enclosure of h' minus A h is
substituted for the correlated polynomial.  All angular outputs through
N+2M are retained, as are complete original target tails and whole eta.

This row producer alone does not solve the two mean-error equations or
certify a body inverse.  Its signed means and coupling columns are the
complete inputs of that subsequent scalar consumer.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json,math,time
from pathlib import Path
import numpy as np
from flint import arb,arb_series,ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_mean_completed_head_body_residual_v3 import (
    prepare,identity,read,actual_jump)
from fourfold_codazzi_full_body_graft_target_jets import ReciprocalFullTargetJets
from fourfold_codazzi_nu_full_adjoint_kernel import operator_action,adjoint_action
from fourfold_codazzi_reciprocal_continuous_residual_v3 import target_model
from fourfold_codazzi_correlated_radial_Fourier import (
    RadialFourier,candidate_fields,norms,circle_pair)
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_bulk_box import arb_box
from fourfold_phase_metric_defect import record,save,sha

KIND='actual_full_regular_joint_radial_polynomial_residual_rows_v1'
RIGHT=Fraction(25,8)
CONTROL_LEFT=Fraction(1,20)
CONTROL_RIGHT=Fraction(9,50)


def T_jets(values):
    """T=beta/(2 E), E=gamma^2*a^2, through its real third jet."""
    b=[values['beta'+(str(j) if j else '')]/math.factorial(j) for j in range(4)]
    g=[values['gamma'+(str(j) if j else '')]/math.factorial(j) for j in range(4)]
    a=values['a'];b0,b1,b2=values['beta'],values['beta1'],values['beta2']
    aa=[a,a*b0,a*(b1+b0*b0)/2,a*(b2+3*b0*b1+b0**3)/6]
    out=arb_series(b,prec=4)/(2*arb_series(g,prec=4)**2*arb_series(aa,prec=4)**2)
    return {('T'+(str(j) if j else '')):out[j]*math.factorial(j) for j in range(4)}


def scalar_models(c,left,right,whole,midpoint):
    half=(right-left)/2;models={}
    for name in ('gamma','beta','K','s'):
        models[name]=RadialFourier.scalar(target_model(midpoint,whole,name,half),c['grid'],c['fft'])
    if left>=CONTROL_LEFT and right<=CONTROL_RIGHT:
        tw=T_jets(whole);tm=T_jets(midpoint)
        models['T']=RadialFourier.scalar(target_model(tm,tw,'T',half),c['grid'],c['fft'])
    return models


def parameter_source(Q,a,left,right):
    u,v=Q;zero=u.coerce(0)
    if right<=CONTROL_LEFT or left>=CONTROL_RIGHT:return (zero,zero)
    if left<CONTROL_LEFT or right>CONTROL_RIGHT:raise ValueError('compact-source seam crossed')
    beta,K,gamma,T=(a[n] for n in ('beta','K','gamma','T'))
    midpoint=(left+right)/2;half=(right-left)/2;width=CONTROL_RIGHT-CONTROL_LEFT
    t=RadialFourier.scalar([exact_arb((midpoint-CONTROL_LEFT)/width),exact_arb(half/width)],c_grid:=u.grid,u.fft)
    p=t*(1-t);w=4096*p**6
    wr=(24576*exact_arb(1/width))*p**5*(1-2*t)
    Knu=-K*w+T*wr;m=v.mean();v2=v*v;I=v2.primitive();up=u.derivative();vp=v.derivative()
    return (-beta*Knu*(I*up+v2*u)+gamma*m*(K*w*.5+Knu)*vp,
            -beta*Knu*(I*vp+v2*v)-(gamma*m*w*.5)*up)


def attach_full_trials(c):
    actual={}
    for role in ('response','adjoint'):
        t=c[role];p=Path(t['meta']['original_full_trial_path'])
        if sha(p)!=t['meta']['original_full_trial_sha256']:
            raise ValueError('the original complete full trial identity changed')
        saved=load_candidate(p)
        if (not np.array_equal(saved['radial_nodes'],t['saved']['radial_nodes'])
            or saved['piece_coefficients'].shape!=t['saved']['piece_coefficients'].shape):
            raise ValueError('full trial and exact nonmean projection have different partitions')
        m=t['m'];full=saved['piece_coefficients'];non=t['saved']['piece_coefficients']
        if not np.array_equal(full[:,:,:m],non[:,:,:m]) or not np.array_equal(full[:,:,m+1:],non[:,:,m+1:]):
            raise ValueError('the original full trial differs in a nonmean coefficient')
        t['full_saved']=saved;actual[role]=dict(path=str(p),sha256=sha(p),metadata=json.loads(str(saved['metadata'])))
    return actual


def row_budget(c,target,i):
    left,right,k,old,indices=identity(c,i);mid=(left+right)/2
    whole,germ=target.coefficients(left,right,c['nu'])
    centre,cg=target.coefficients(mid,mid,c['nu'])
    if germ!=cg or not germ[0]<=left<right<=germ[1]:
        raise ValueError('midpoint and complete interval must use one actual target germ')
    a=scalar_models(c,left,right,whole,centre)
    bg=candidate_fields(c['saved']['piece_coefficients'][:,indices['background']],
        c['nodes'][indices['background']],left,right,c['m'],c['grid'],c['fft'],c['alpha'],a['s'])
    Q=(bg[0],bg[1]);u,v=Q;m=v.mean()
    trials={}
    for role in ('response','adjoint'):
        t=c[role];f=candidate_fields(t['full_saved']['piece_coefficients'][:,indices[role]],
            t['nodes'][indices[role]],left,right,t['m'],c['grid'],c['fft'])
        trials[role]=((f[0],f[1]),(f[4],f[5]))
    h,hr=trials['response'];psi,psir=trials['adjoint']
    D=operator_action(Q,h,hr,a);F=parameter_source(Q,a,left,right)
    R=(D[0]-F[0],D[1]-F[1]);Rd=adjoint_action(Q,psi,psir,a)
    maxdegree=max(t['m'] for t in (c['response'],c['adjoint']))+2*c['m']
    if any(z.degree>maxdegree for z in R+Rd):raise ValueError('an actual full output mode was lost')
    Rmean=R[1].mean();Dmean=Rd[1].mean()
    Rnon=(R[0],R[1].nonmean());Dnon=(Rd[0],Rd[1].nonmean())
    Smean=(u*u+a['K']*v*v).mean();cm=a['beta']*(1-Smean-2*a['K']*m*m)
    z=u.coerce(0);one=u.coerce(1)
    negative_column=operator_action(Q,(z,one),(z,z),a)
    column=tuple(-f for f in negative_column)
    dualcolumn=(-2*a['beta']*m*u,a['beta']*(1-Smean)-2*a['beta']*a['K']*m*v)
    column_non=(column[0],column[1].nonmean())
    dualcolumn_non=(dualcolumn[0],dualcolumn[1].nonmean())
    lambd=(psi[0],psi[1].nonmean())
    pair=circle_pair(lambd,Rnon);g=circle_pair(lambd,column_non)
    length=right-left
    names=('gamma','beta','K','s')
    def jets(values):
        return {n:record(values[n]) for n in ['a']+[name+(str(j) if j else '') for name in names for j in range(4)]}
    def budgets(pair):return {n:record(v) for n,v in norms(pair,length,c['width']).items()}
    return dict(common_row=i,interval=list(map(str,(left,right))),source_mean_row=k,
        pieces=indices,actual_scalar_germ=list(map(str,germ)),
        actual_original_scalar_germ=old['actual_scalar_germ'],
        full_output_support=maxdegree,complete_angular_grid=c['grid'],
        exact_shared_radial_variable='t=(r-midpoint)/halfwidth in [-1,1]',
        intrinsic_midpoint_jets=jets(centre),intrinsic_whole_third_jets=jets(whole),
        scalar_cm=record(cm.scalar_range()),
        response_mean_residual=record(Rmean.scalar_range()),
        adjoint_mean_residual=record(Dmean.scalar_range()),
        response_full_trial_mean=record(h[1].mean().scalar_range()),
        adjoint_full_trial_mean=record(psi[1].mean().scalar_range()),
        uncorrected_response_nonmean=budgets(Rnon),
        uncorrected_adjoint_nonmean=budgets(Dnon),
        actual_A_e2_nonmean=budgets(column_non),
        actual_Astar_e2_nonmean=budgets(dualcolumn_non),
        signed_full_trial_dual_response_nonmean_integral=record(pair.scalar_integral(length)),
        signed_adjoint_nonmean_Ae2_range=record(g.scalar_range()),
        exact_mean_error_equations=dict(
            response="e_z'=cm*e_z - response_mean_residual; solved backward from true outer mean minus full trial mean",
            adjoint="e_mu'=-cm*e_mu + adjoint_mean_residual; solved forward from exact waist dual mean minus full trial mean"),
        nonmean_mean_error_corrections='R_non - (A e2)_non e_z; Rd_non - (Astar e2)_non e_mu',
        all_unknown_scalar_tail_errors_have_complete_finite_angular_support=True,
        no_complete_scalar_error_flow_or_body_inverse_claimed=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('candidate','mean','response','adjoint'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--waist',type=Path,default=Path('notes/2026-11-14-R133-final-waist-mean-adjoint-column-rational.json'))
    p.add_argument('--amp-multiplier',type=Fraction,default=Fraction(-1))
    p.add_argument('--analytic-width',type=Fraction,default=Fraction(1,2048))
    p.add_argument('--radial-subdivisions',type=int,default=1)
    p.add_argument('--half-width',type=Fraction,default=Fraction(1,10**9))
    p.add_argument('--first',type=int,default=0);p.add_argument('--count',type=int)
    p.add_argument('--resume',type=Path);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();started=time.monotonic();ctx.prec=256;ctx.cap=6
    if args.out.exists():raise FileExistsError('preserve every actual polynomial outcome')
    if args.half_width!=Fraction(1,10**9):raise ValueError('this contract keeps the entire original eta box')
    c,old=prepare(args)
    if sha(args.object)!=c['meta']['object_sha256']:raise ValueError('the exact intrinsic object changed')
    full=attach_full_trials(c);c['nu']=Fraction(c['meta']['exact_float_nu'])
    target=ReciprocalFullTargetJets(args.object,args.half_width,512)
    n=len(c['cuts'])-1;end=n if args.count is None else min(n,args.first+args.count)
    if not 0<=args.first<end:raise ValueError('nonempty exact original row range required')
    dependencies={name:sha(Path(__file__).with_name(name)) for name in (
        'fourfold_codazzi_correlated_radial_Fourier.py',
        'fourfold_codazzi_mean_completed_head_body_residual_v3.py',
        'fourfold_codazzi_nu_full_adjoint_kernel.py',
        'fourfold_codazzi_full_body_graft_target_jets.py',
        'fourfold_codazzi_reciprocal_continuous_residual_v3.py')}
    ident=dict(candidate_sha256=sha(args.candidate),object_sha256=sha(args.object),
        original_inputs=old['inputs'],full_trials=full,dependencies=dependencies,
        exact_alpha=c['meta']['exact_float_amplitude'],exact_nu=c['meta']['exact_float_nu'],
        original_parameter_half_width=str(args.half_width),radial_subdivisions=args.radial_subdivisions,
        total_common_cells=n,complete_finite_grid=c['grid'],analytic_width=str(args.analytic_width),
        source_sha256=sha(__file__))
    doc=dict(kind=KIND,identity=ident,complete=False,selected_cells_complete=False,failure=None,
        candidate_sha256=sha(args.candidate),source_sha256=sha(__file__),
        exact_interval=['0','25/8'],selected_indices=[args.first,end],rows=[],
        actual_outer_response_mean=old['outer_response_mean'],actual_adjoint_initial_mean=old['adjoint_initial_mean'],
        original_ac1_operator_not_relabelled_as_continuous_repair=True,
        complete_scalar_error_flows_still_required=True,complete_body_inverse_proved=False)
    if args.resume:
        prior=read(args.resume)
        if prior['kind']!=KIND or prior['identity']!=ident or prior['failure'] is not None:
            raise ValueError('only the actual same-input successful polynomial prefix may resume')
        if prior['selected_indices'][0]!=args.first or prior['selected_indices'][1]>end:
            raise ValueError('resume cannot change the original first row or delete requested cells')
        for j,row in enumerate(prior['rows'],args.first):
            if row['common_row']!=j or row['interval']!=list(map(str,c['cuts'][j:j+2])):
                raise ValueError('an actual completed joint polynomial row changed')
        doc['rows']=prior['rows'];doc['resume_source_sha256']=sha(args.resume)
    try:
        for i in range(args.first+len(doc['rows']),end):
            tick=time.monotonic();row=row_budget(c,target,i);row['wall_seconds']=time.monotonic()-tick
            doc['rows'].append(row);doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
            print(dict(row=i,interval=row['interval'],seconds=row['wall_seconds'],
                primal_L2=row['uncorrected_response_nonmean']['L2_sup'],
                dual_L2=row['uncorrected_adjoint_nonmean']['L2_sup']),flush=True)
        doc['selected_cells_complete']=True
        doc['complete']=args.first==0 and end==n
        doc['complete_scope']='joint polynomial row cover only; scalar mean-error propagation and global inverse remain separate'
    except Exception as e:
        doc['failure']=dict(type=type(e).__name__,message=str(e));raise
    finally:
        doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    print(dict(complete=doc['complete'],selected_cells_complete=doc['selected_cells_complete'],rows=len(doc['rows'])),flush=True)


if __name__=='__main__':main()
