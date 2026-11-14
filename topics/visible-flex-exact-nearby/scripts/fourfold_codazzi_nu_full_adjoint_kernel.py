#!/usr/bin/env python3
"""Actual ac1 full 5M nu-adjoint kernel; no scalar Schur sign is inferred.

This new producer consumes the exact replayed complete final candidate and
original full-target intervals.  It computes A_nu, B_nu, G_nu=B_nu-D A_nu
with the whole nonlocal primitive and rank-one mean.  All radial derivatives
are the actual saved PPoly derivatives.  Every real PPoly A jump is paid.
There is no adjoint candidate here; complete means kernel/source cover,
never a body inverse or a nonzero scalar Schur.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import time

from flint import arb, acb, ctx
from fourfold_codazzi_final_nu_return_derivative import (
    Finite, prepare as prepare_return, identity, extended_target, lift_state,
    exact_w_integral, exact_w_value, CONTROL_LEFT, CONTROL_RIGHT,
    maximum, interval_bounds)
from fourfold_codazzi_curvature_angle_energy_prefix import (
    read, polynomial_ranges, actual_jump)
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_bulk_box import CBox, zeros
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_metric_defect import record, save, sha

KIND='actual_final_moving_full_nu_adjoint_5M_kernel_and_all_jumps'


def add(x,y): return tuple(a+b for a,b in zip(x,y))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def scale(x,z): return tuple(a*z for a in x)
def theta(x): return tuple(a.derivative() for a in x)
def dot(x,y): return x[0]*y[0]+x[1]*y[1]
def J(x,K): return (K*x[1],-x[0])


def parts(Q,a):
    u,v=Q
    beta,K,gamma=(a[k] for k in ('beta','K','gamma'))
    m=v.mean();S=u*u+K*v*v;d=-beta*S.primitive();qp=theta(Q)
    L=((-beta*(1+3*u*u+K*v*v),-2*beta*K*u*v),
       (-2*beta*u*v,beta*(1-u*u-3*K*v*v)))
    return m,d,qp,L


def operator_action(Q,h,hr,a):
    """Full unnormalized moving D h, including both true mean terms."""
    beta,K,gamma=(a[k] for k in ('beta','K','gamma'))
    m,d,qp,L=parts(Q,a)
    hp=theta(h)
    principal=add(scale(hp,d),scale(J(hp,K),gamma*m))
    local=(L[0][0]*h[0]+L[0][1]*h[1],L[1][0]*h[0]+L[1][1]*h[1])
    nonlocal_part=add(scale(qp,-2*beta*(Q[0]*h[0]+K*Q[1]*h[1]).primitive()),
                      scale(J(qp,K),gamma*h[1].mean()))
    return sub(sub(sub(hr,principal),local),nonlocal_part)


def adjoint_action(Q,psi,psir,a):
    """Full D* psi in the actual odd/even reflection L2 space."""
    beta,K,gamma=(a[k] for k in ('beta','K','gamma'))
    m,d,qp,L=parts(Q,a)
    pp=theta(psi)
    principal=(d*pp[0]-gamma*m*pp[1],gamma*m*K*pp[0]+d*pp[1])
    local=(L[0][0]*psi[0]+L[1][0]*psi[1],
           L[0][1]*psi[0]+L[1][1]*psi[1])
    nstar=scale((Q[0],K*Q[1]),2*beta*dot(qp,psi).primitive())
    # An exact real mean, retained as a constant field.
    nstar=(nstar[0],nstar[1]+gamma*dot(J(qp,K),psi).mean())
    return sub(sub(add(add(scale(psir,-1),principal),scale(psi,d.derivative())),local),nstar)


def nu_polynomials(Q,Qr,a):
    """S.9, actual radial derivative, and S.14; no use of the PDE."""
    u,v=Q;ur,vr=Qr
    beta,K,gamma,T,T1=(a[k] for k in ('beta','K','gamma','T','T1'))
    m=v.mean();mr=vr.mean();qp=theta(Q);qpr=theta(Qr)
    v2=v*v;P=v2.primitive()
    W=add(scale(qp,P),scale(Q,v2))
    Wr=add(add(scale(qp,(2*v*vr).primitive()),scale(qpr,P)),
           add(scale(Q,2*v*vr),scale(Qr,v2)))
    A=add(scale(W,-beta*T),(gamma*m*T*qp[1],0*qp[1]))
    B=sub(scale(W,beta*K),((gamma*m*K/2)*qp[1],
                           (gamma*m/2)*qp[0]))
    Ar=add(add(scale(W,-(a['beta1']*T+beta*T1)),scale(Wr,-beta*T)),
           ((a['gamma1']*m*T+gamma*mr*T+gamma*m*T1)*qp[1]+gamma*m*T*qpr[1],
            0*qp[1]))
    G=sub(B,operator_action(Q,A,Ar,a))
    M=u.degree
    if any(z.degree>3*M for z in A+B+Ar) or any(z.degree>5*M for z in G):
        raise ValueError('complete 3M / 5M Fourier support was lost')
    return dict(A=A,B=B,Ar=Ar,G=G)


def odd_polynomial(values,alpha,m,N,fft):
    c=zeros((N,))
    for j in range(1,m+1):
        z=alpha*values[j-1]/2
        c[j]=CBox.from_acb(acb(0,-z));c[-j]=CBox.from_acb(acb(0,z))
    return Finite(c,m,fft)


def exact_delta_state(exact,alpha,m,N,fft):
    values=list(map(exact_arb,exact))
    du=odd_polynomial(values,alpha,m,N,fft)
    c=zeros((N,));c[0]=CBox.from_acb(acb(alpha*values[m]))
    for j in range(1,m+1):
        z=alpha*values[m+j]/2
        c[j]=c[-j]=CBox.from_acb(acb(z))
    return du,Finite(c,m,fft)


def lift(c,a,y,yr):
    u,v,vr,_,_=lift_state(y,yr,a,c['alpha'],c['modes'],c['grid'],c['fft'])
    ur=odd_polynomial(yr,c['alpha'],c['modes'],c['grid'],c['fft'])
    return (u,v),(ur,vr)


def exact_w_variation(left,right):
    mid=(CONTROL_LEFT+CONTROL_RIGHT)/2
    if right<=mid or left>=mid:
        return abs(exact_w_value(right)-exact_w_value(left))
    return 2*exact_w_value(mid)-exact_w_value(left)-exact_w_value(right)


def norm_pair(q):
    norms=[x.norm().upper() for x in q]
    return sum((x*x for x in norms),arb(0)).sqrt().upper()


def row_budget(c,index,args):
    left,right,j,k,row=identity(c,index)
    a=extended_target(row,left,right,c['nu'])
    y,yr=polynomial_ranges(c['saved'],c['nodes'],j,left,right)
    Q,Qr=lift(c,a,y,yr)
    vbox=Q[1].closed_cells(args.angles)
    if not Q[1].mean()<0 or not maximum(vbox)<0:
        raise ValueError('the complete actual v and mean chart must remain negative')
    polynomials=nu_polynomials(Q,Qr,a)
    return dict(common_row=index,interval=list(map(str,(left,right))),
        candidate_piece=j,original_target_row=k,actual_scalar_germ=row['actual_scalar_germ'],
        exact_bump_integral=str(exact_w_integral(left,right)),
        exact_bump_total_variation=str(exact_w_variation(left,right)),
        actual_target={name:record(a[name]) for name in
                      ('beta','beta1','gamma','gamma1','K','K1','T','T1','s','s1')},
        actual_moving_mean=record(Q[1].mean()),actual_v=record(interval_bounds(vbox)),
        complete_kernel_support={name:[z.degree for z in value] for name,value in polynomials.items()},
        kernel={name:dict(full_component_A0_upper=[record(z.norm().upper()) for z in value],
                         full_pair_A0_upper=record(norm_pair(value)),
                         complete_mean=[record(z.mean()) for z in value])
                for name,value in polynomials.items()})


def jump_budget(c,j):
    r=c['nodes'][j]
    k=min(bisect_right(c['tn'],r)-1,len(c['rows'])-1);row=c['rows'][k]
    a=extended_target(row,r,r,c['nu'])
    yl,yrl=polynomial_ranges(c['saved'],c['nodes'],j-1,r,r)
    yr,yrr=polynomial_ranges(c['saved'],c['nodes'],j,r,r)
    Ql,_=lift(c,a,yl,yrl);Qr,_=lift(c,a,yr,yrr)
    exact=actual_jump(c['saved'],c['nodes'],j)
    # Every candidate jump is an exact dyadic difference.  Coefficient
    # conversion to arb is explicit, including the complete mean.
    dQ=exact_delta_state(exact,c['alpha'],c['modes'],c['grid'],c['fft'])
    vl,vr=Ql[1],Qr[1];dv=dQ[1]
    delta_v2=(vr+vl)*dv
    delta_W=add(add(scale(theta(Qr),delta_v2.primitive()),
                   scale(theta(dQ),(vl*vl).primitive())),
                add(scale(Qr,delta_v2),scale(dQ,vl*vl)))
    delta_A=add(scale(delta_W,-a['beta']*a['T']),
       (a['gamma']*a['T']*(dv.mean()*vr.derivative()+vl.mean()*dv.derivative()),
        0*dv))
    return dict(candidate_join=j,radius=str(r),exact_bump=str(exact_w_value(r)),
        original_target_row=k,actual_scalar_germ=row['actual_scalar_germ'],
        exact_mean_jump=record(dv.mean()),
        full_A_jump_component_A0_upper=[record(z.norm().upper()) for z in delta_A],
        full_A_jump_pair_A0_upper=record(norm_pair(delta_A)),
        complete_A_jump_mean=[record(z.mean()) for z in delta_A],
        convention='right minus left; true-adjoint scalar contribution is minus w times the full pairing',
        trial_adjoint_jump_must_still_be_paid=True)


def prepare(args):
    c,doc=prepare_return(args)
    # The named final candidate is M32, so this original grid contains all
    # complete 5M products without alias.  Do not silently enlarge support.
    if 2*5*c['modes']>=c['grid']:
        raise ValueError('the actual product grid must strictly contain the complete 5M support')
    parent=Path(__file__).with_name('fourfold_codazzi_final_nu_return_derivative.py')
    doc.update(kind=KIND,source_sha256=sha(__file__),
        complete_finite_kernel_support_index=5*c['modes'],
        centre_family='fixed complete unnormalized Q at the named centre; full target parameter source',
        full_mean_rank_one_adjoint_retained=True,
        actual_adjoint_or_nu_response_not_supplied=True,
        actual_scalar_Schur_nonzero_proved=False,
        complete_native_kernel_cover_only_no_adjoint_solution=True)
    doc['dependencies'][parent.name]=sha(parent)
    return c,doc


def complete_bounds(c,doc):
    if len(doc['rows'])!=len(c['cuts'])-1:raise ValueError('a prefix is not a complete kernel cover')
    source=arb(0);kernel=arb(0);jump=arb(0)
    for row in doc['rows']:
        iw=exact_arb(Fraction(row['exact_bump_integral']))
        vw=exact_arb(Fraction(row['exact_bump_total_variation']))
        source+=vw*box_from_record(row['kernel']['A']['full_pair_A0_upper'])
        source+=iw*box_from_record(row['kernel']['B']['full_pair_A0_upper'])
        kernel+=iw*box_from_record(row['kernel']['G']['full_pair_A0_upper'])
    for j,r in enumerate(c['nodes'][1:-1],1):
        if not CONTROL_LEFT<r<CONTROL_RIGHT:continue
        row=jump_budget(c,j);doc['jumps'].append(row)
        jump+=exact_arb(Fraction(row['exact_bump']))*box_from_record(row['full_A_jump_pair_A0_upper'])
    doc.update(complete=True,whole_radial_support_and_all_finite_coefficients=True,
        all_true_PPoly_A_jumps_paid=True,
        bounds=dict(unnormalized_full_parameter_source_L1L2_upper=record(source.upper()),
                    complete_G_weighted_L1L2_upper=record(kernel.upper()),
                    all_A_jumps_weighted_l1_L2_upper=record(jump.upper()),
                    true_continuous_adjoint_scalar_absolute_coefficient=record((kernel+jump).upper())),
        bound_meaning='last coefficient multiplies an independently paid full sup-r L2-phi adjoint norm; it is not a computed Schur value',
        actual_scalar_Schur_nonzero_proved=False,complete_body_BVP_inverse_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidate',type=Path,required=True)
    p.add_argument('--target',type=Path,default=Path('notes/2026-11-13-Codazzi-true-target-r02-v1-native.json.gz'))
    p.add_argument('--type-cover',type=Path,default=Path('notes/2026-11-13-R133-compact-nu-full-type-cover-native.json.gz'))
    p.add_argument('--angles',type=int,default=1024)
    p.add_argument('--radial-subdivisions',type=int,default=1)
    p.add_argument('--resume',type=Path);p.add_argument('--max-new-rows',type=int)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve every original complete, partial or failed result')
    c,doc=prepare(args)
    if args.resume:
        old=read(args.resume)
        for key in ('kind','source_sha256','inputs','candidate_metadata','exact_parameter',
                    'exact_amplitude','exact_interval','total_radial_cells','finite_product_grid',
                    'closed_angular_cells','radial_subdivisions','dependencies'):
            if old[key]!=doc[key]:raise ValueError('complete prefix identity changed: '+key)
        if old['complete'] or old['failure'] is not None:
            raise ValueError('only a successful saved row prefix can be resumed')
        for index,row in enumerate(old['rows']):
            left,right,j,k,actual=identity(c,index)
            if (row['common_row']!=index or row['interval']!=list(map(str,(left,right)))
                or row['candidate_piece']!=j or row['original_target_row']!=k
                or row['actual_scalar_germ']!=actual['actual_scalar_germ']):
                raise ValueError('a saved complete row changed its genuine mathematical cell')
        doc['rows']=old['rows']
        doc['resume_history']=old['resume_history']+[
            dict(path=str(args.resume),sha256=sha(args.resume),saved_complete_rows=len(old['rows']),
                 original_complete=False,missing_process_exit_code_not_inferred=True)]
    first=len(doc['rows']);last=len(c['cuts'])-1
    if args.max_new_rows is not None:
        if args.max_new_rows<=0:raise ValueError('positive explicit count required')
        last=min(last,first+args.max_new_rows)
    checkpoint=time.monotonic()
    try:
        for index in range(first,last):
            doc['rows'].append(row_budget(c,index,args))
            if time.monotonic()-checkpoint>15:
                doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
                print(dict(rows=len(doc['rows']),total=len(c['cuts'])-1,
                           right=doc['rows'][-1]['interval'][1]),flush=True)
                checkpoint=time.monotonic()
        if len(doc['rows'])==len(c['cuts'])-1:complete_bounds(c,doc)
        else:doc['explicit_saved_complete_row_prefix_only']=True
    except Exception as exc:
        doc['failure']=dict(type=type(exc).__name__,message=str(exc));raise
    finally:
        doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    print(dict(complete=doc['complete'],failure=doc['failure'],rows=len(doc['rows']),
               jumps=len(doc['jumps']),out=str(args.out)),flush=True)


if __name__=='__main__':
    main()
