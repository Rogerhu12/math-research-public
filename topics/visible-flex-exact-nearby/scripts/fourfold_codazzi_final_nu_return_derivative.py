#!/usr/bin/env python3
"""Whole-circle compact-metric ray-return derivative of the actual final centre.

This producer differentiates the explicit frozen U,V family, not an
uncomputed true nonlinear solution family.  It keeps the complete actual
nu mean, original full-primitive target intervals, all finite products
through 4M, and every actual dyadic PPoly jump in the integration-by-parts
identity.  No characteristic sample or finite difference is a proof.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction
import json
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, ctx

from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_curvature_angle_energy_prefix import (
    read, dyadic, target_bounds, polynomial_ranges, actual_jump, bump_jets)
from fourfold_codazzi_moving_actual_R_boundary import COORDINATES
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_bulk_box import (
    Box, CBox, zeros, arb_box, DirectedFFT)
from fourfold_phase_correlated_curvature import Polynomial
from fourfold_phase_metric_defect import record, save, sha

KIND='actual_frozen_moving_centre_complete_compact_nu_ray_return_derivative'
EXPECTED_CANDIDATE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
CONTROL_LEFT=Fraction(1,20)
CONTROL_RIGHT=Fraction(9,50)


class Finite(Polynomial):
    """Exact finite-support Fourier polynomial in interval coefficients.

    Only coefficient and interval arithmetic errors occur here.  There is
    no unknown infinite angular remainder, so differentiating the actual
    coefficient intervals is legitimate.  The original intrinsic tail is
    already enclosed in the radial interval coefficients.
    """
    def __init__(self,coefficient,degree,fft):
        degree=int(degree)
        c=CBox(Box(coefficient.real.lo.copy(),coefficient.real.hi.copy()),
               Box(coefficient.imag.lo.copy(),coefficient.imag.hi.copy()))
        N=len(c.real.lo)
        modes=np.asarray([j if j<N//2 else j-N for j in range(N)])
        outside=abs(modes)>degree
        if (np.any(c.real.lo[outside]>0) or np.any(c.real.hi[outside]<0)
            or np.any(c.imag.lo[outside]>0) or np.any(c.imag.hi[outside]<0)):
            raise ValueError('a true finite-support zero was not enclosed')
        c[outside]=0
        super().__init__(c,arb(0),degree,fft)

    @classmethod
    def constant(cls,value,N,fft):
        c=zeros((N,));c[0]=CBox.from_acb(acb(value))
        return cls(c,0,fft)

    def coerce(self,value):
        if isinstance(value,Finite):
            if value.grid!=self.grid or value.fft is not self.fft:
                raise ValueError('incompatible actual finite Fourier algebras')
            return value
        return self.constant(value,self.grid,self.fft)

    def __add__(self,value):
        value=self.coerce(value)
        return Finite(self.c+value.c,max(self.degree,value.degree),self.fft)
    __radd__=__add__

    def __neg__(self):return Finite(-self.c,self.degree,self.fft)
    def __sub__(self,value):return self+(-self.coerce(value))
    def __rsub__(self,value):return self.coerce(value)+(-self)

    def __mul__(self,value):
        value=self.coerce(value)
        answer=super().__mul__(value)
        if not answer.error==0:
            raise ValueError('this finite centre must not acquire an unspecified infinite tail')
        return Finite(answer.c,answer.degree,self.fft)
    __rmul__=__mul__

    def derivative(self,order=1):
        N=self.grid
        frequency=np.asarray([j if j<N//2 else j-N for j in range(N)])*4
        out=self.c
        for _ in range(order):out=out*CBox(0.,Box(frequency.astype(float)))
        return Finite(out,self.degree,self.fft)

    def primitive(self):
        c=zeros((self.grid,))
        for j in range(-self.degree,self.degree+1):
            if j:c[j%self.grid]=self.c[j%self.grid]*CBox.from_acb(acb(0,-arb(1)/(4*j)))
        return Finite(c,self.degree,self.fft)

    def closed_cells(self,angles):
        if angles<self.grid or angles&(angles-1):
            raise ValueError('the complete closed angular grid must contain full support')
        coefficients=zeros((angles,))
        frequency=np.asarray([j if j<self.grid//2 else j-self.grid
                              for j in range(self.grid)])
        coefficients[frequency%angles]=self.c
        f=self.fft.fft(coefficients,inverse=True)*angles
        derivative=self.derivative()
        dc=zeros((angles,));dc[frequency%angles]=derivative.c
        fp=self.fft.fft(dc,inverse=True)*angles
        if (np.any(f.imag.lo>0) or np.any(f.imag.hi<0)
            or np.any(fp.imag.lo>0) or np.any(fp.imag.hi<0)):
            raise ValueError('a real finite Fourier field lost its reality enclosure')
        # Nearest-node cells have exact physical half-width pi/(4N).
        h=arb.pi()/(4*angles)
        absolute_fp=Box(np.maximum(abs(fp.real.lo),abs(fp.real.hi)))
        fee=absolute_fp*arb_box(h)+arb_box((h*h*self.norm(2)/2).upper())
        result=Box(f.real.lo-fee.hi,f.real.hi+fee.hi)
        # The two binary64 endpoint subtractions themselves are rounded out.
        result=Box(np.nextafter(result.lo,-np.inf),np.nextafter(result.hi,np.inf))
        win=arb_box(self.norm().upper()).hi
        lo=np.maximum(result.lo,-win);hi=np.minimum(result.hi,win)
        if np.any(lo>hi):raise ValueError('two valid full angular bounds became disjoint')
        return Box(lo,hi)


def minimum(box):return arb(float(np.min(box.lo))).lower()
def maximum(box):return arb(float(np.max(box.hi))).upper()
def absmax(box):return arb(float(np.max(np.maximum(abs(box.lo),abs(box.hi))))).upper()
def interval_bounds(box):return minimum(box).union(maximum(box))


def lift_state(y,yr,a,alpha,m,N,fft):
    cu=zeros((N,));cv=zeros((N,));cvr=zeros((N,))
    mean=a['s']+alpha*y[m];meanr=a['s1']+alpha*yr[m]
    cv[0]=CBox.from_acb(acb(mean));cvr[0]=CBox.from_acb(acb(meanr))
    for j in range(1,m+1):
        U=alpha*y[j-1]/2;V=alpha*y[m+j]/2;Vr=alpha*yr[m+j]/2
        cu[j]=CBox.from_acb(acb(0,-U));cu[-j]=CBox.from_acb(acb(0,U))
        cv[j]=cv[-j]=CBox.from_acb(acb(V))
        cvr[j]=cvr[-j]=CBox.from_acb(acb(Vr))
    return Finite(cu,m,fft),Finite(cv,m,fft),Finite(cvr,m,fft),mean,meanr


def extended_target(row,left,right,nu):
    a=target_bounds(row,left,right,nu)
    old={k:box_from_record(row['true_target_coefficients'][k])
         for k in ('a','a1','a2','E','E1')}
    w,w1,_=bump_jets(left,right)
    E=old['E']*(nu*w).exp()
    E1=(old['E1']+nu*w1*old['E'])*(nu*w).exp()
    gap=E-old['a1']**2
    if not E>0 or not gap>0:raise ValueError('the exact controlled rotational gap is unresolved')
    bp=old['a2']/old['a']-a['beta']**2
    T=a['beta']/(2*E)
    Tp=bp/(2*E)-T*E1/E
    q=(-a['K']).sqrt()
    qp=-a['K1']/(2*q)
    gp=a['gamma']*(E1/(2*E)-a['beta'])
    sigma=-a['s']*old['a1']**2/(2*gap)
    return dict(a,En=E,En1=E1,beta1=bp,T=T,T1=Tp,q=q,q1=qp,
                gamma1=gp,sigma_s=sigma,w=w,w1=w1)


def kernel_polynomials(u,v,vr,mean,meanr,a):
    beta,K,gamma,q,T,Tp,sigma=(a[k] for k in
        ('beta','K','gamma','q','T','T1','sigma_s'))
    v2=v*v;Iv2=v2.primitive()
    S=u*u+K*v2
    Fphi=beta*(S-S.mean())
    speed=-gamma*mean*q
    drift_negative=beta*S.primitive()
    Aosc=beta*T*Iv2
    Ar_osc=(a['beta1']*T+beta*Tp)*Iv2+2*beta*T*(v*vr).primitive()
    Ar_const=(a['gamma1']*mean*T+gamma*meanr*T+gamma*mean*Tp
              -gamma*mean*T*a['q1']/q)/(2*q)
    Bosc=beta*K*(2*sigma*v-v2).primitive()
    out={}
    for epsilon in (-1,1):
        F=drift_negative+epsilon*speed
        A=Aosc+epsilon*gamma*mean*T/(2*q)
        Ar=Ar_osc+epsilon*Ar_const
        B=Bosc-epsilon*gamma*sigma*q
        G=B-Ar-F*A.derivative()+Fphi*A
        if G.degree>4*u.degree:
            raise ValueError('the complete 4M support identity was lost')
        out[str(epsilon)]=dict(F=F,A=A,G=G)
    return out,Fphi


def exact_w_integral(left,right):
    width=CONTROL_RIGHT-CONTROL_LEFT
    t0=(left-CONTROL_LEFT)/width;t1=(right-CONTROL_LEFT)/width
    # 4096 t^6(1-t)^6, integrated exactly as a rational.
    import math
    value=Fraction(0)
    for j in range(7):
        value+=Fraction((-1)**j*math.comb(6,j),7+j)*(t1**(7+j)-t0**(7+j))
    value*=4096*width
    if value<=0:raise ValueError('the actual nonnegative bump integral must be positive')
    return value


def exact_w_value(r):
    t=(r-CONTROL_LEFT)/(CONTROL_RIGHT-CONTROL_LEFT)
    return 4096*t**6*(1-t)**6


def prepare(args):
    if sha(args.candidate)!=EXPECTED_CANDIDATE:
        raise ValueError('replay must recover the complete exact ac1 final candidate; a different state needs a new explicit input contract')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']))
    native=read(args.target);types=read(args.type_cover)
    if (meta['coordinates']!=COORDINATES or meta['object_sha256']!=native['object_sha256']
        or not native['complete'] or native['exact_requested_interval']!=['0','1/5']
        or not types['complete'] or not types['exactly_one_real_K_root']
        or types['inputs'].get(str(args.target))!=sha(args.target)):
        raise ValueError('the complete same-object target and type cover are required')
    nuq=Fraction(meta['exact_float_nu']);alphaq=Fraction(meta['exact_float_amplitude'])
    nulo,nuhi=map(Fraction,types['exact_nu_interval'])
    if nuq!=dyadic(meta['nu']) or alphaq!=dyadic(meta['amplitude']) or not nulo<nuq<nuhi:
        raise ValueError('the actual exact parameter is not an interior point of its proved type cover')
    nodes=list(map(dyadic,saved['radial_nodes']))
    if nodes[0]!=0 or nodes[-1]!=Fraction(25,8):
        raise ValueError('the complete actual full-R centre is required')
    rows=native['rows']
    tn=[Fraction(row['interval'][0]) for row in rows]+[Fraction(rows[-1]['interval'][1])]
    if any(Fraction(x['interval'][1])!=Fraction(y['interval'][0]) for x,y in zip(rows,rows[1:])):
        raise ValueError('the complete original target cover has a gap')
    original=sorted({CONTROL_LEFT,CONTROL_RIGHT}
        |{r for r in nodes+tn if CONTROL_LEFT<r<CONTROL_RIGHT})
    if args.radial_subdivisions<1:raise ValueError('positive explicit radial refinement required')
    cuts=[]
    for left,right in zip(original,original[1:]):
        cuts.extend(left+(right-left)*j/args.radial_subdivisions for j in range(args.radial_subdivisions))
    cuts.append(CONTROL_RIGHT)
    modes=int(meta['modes']);grid=1
    while grid<=8*modes:grid*=2
    if args.angles<grid or args.angles&(args.angles-1):
        raise ValueError('full 4M finite products and a power-of-two closed angle grid required')
    c=dict(saved=saved,meta=meta,nodes=nodes,rows=rows,tn=tn,cuts=cuts,modes=modes,
           grid=grid,fft=DirectedFFT(),alpha=exact_arb(alphaq),nu=exact_arb(nuq))
    dependencies=(
        'fourfold_codazzi_candidate_shards.py','fourfold_codazzi_curvature_angle_energy_prefix.py',
        'fourfold_codazzi_moving_actual_R_boundary.py','fourfold_codazzi_rotational_cap_jacobi.py',
        'fourfold_phase_beta_bulk_interval.py','fourfold_phase_beta_bulk_box.py',
        'fourfold_phase_correlated_curvature.py','fourfold_phase_metric_defect.py')
    doc=dict(kind=KIND,source_sha256=sha(__file__),complete=False,failure=None,
        inputs={str(p):sha(p) for p in (args.candidate,args.target,args.type_cover)},
        candidate_metadata=meta,actual_candidate_sha256=EXPECTED_CANDIDATE,
        exact_parameter=str(nuq),exact_amplitude=str(alphaq),
        exact_interval=[str(CONTROL_LEFT),str(CONTROL_RIGHT)],
        original_object_sha256=native['object_sha256'],
        original_affine_parameter_half_width=native['parameter_half_width'],
        original_exact_center_parameter=native['exact_center_parameter'],
        whole_affine_parameter_interval=True,complete_original_primitive_tail=True,
        centre_family='fixed complete U,V,alpha and dyadic radial nodes; only actual s,K,gamma depend on nu',
        actual_nonlinear_solution_family_derivative=False,
        complete_finite_kernel_support_index=4*modes,finite_product_grid=grid,
        closed_angular_cells=args.angles,radial_subdivisions=args.radial_subdivisions,
        total_radial_cells=len(cuts)-1,rows=[],jumps=[],resume_history=[],
        dependencies={name:sha(Path(__file__).with_name(name)) for name in dependencies},
        all_mean_rows_retained=True,
        complete_body_BVP_inverse_proved=False,
        actual_rotation_number_twist_proved=False)
    return c,doc


def identity(c,index):
    left,right=c['cuts'][index:index+2]
    j=min(bisect_right(c['nodes'],left)-1,len(c['nodes'])-2)
    k=bisect_right(c['tn'],left)-1;row=c['rows'][k]
    tl,tr=map(Fraction,row['interval'])
    if not c['nodes'][j]<=left<right<=c['nodes'][j+1] or not tl<=left<right<=tr:
        raise ValueError('a whole closed target/candidate/refinement identity is incomplete')
    return left,right,j,k,row


def row_budget(c,index,args):
    left,right,j,k,row=identity(c,index)
    a=extended_target(row,left,right,c['nu'])
    y,yr=polynomial_ranges(c['saved'],c['nodes'],j,left,right)
    u,v,vr,mean,meanr=lift_state(y,yr,a,c['alpha'],c['modes'],c['grid'],c['fft'])
    vbox=v.closed_cells(args.angles)
    if not mean<0 or not maximum(vbox)<0:
        raise ValueError('the complete actual negative v/mean chart is unresolved')
    polynomials,Fphi=kernel_polynomials(u,v,vr,mean,meanr,a)
    out=dict(common_row=index,interval=list(map(str,(left,right))),
        candidate_piece=j,original_target_row=k,actual_scalar_germ=row['actual_scalar_germ'],
        exact_bump_integral=str(exact_w_integral(left,right)),
        v=record(interval_bounds(vbox)),mean_v=record(mean),
        F_phi=record(interval_bounds(Fphi.closed_cells(args.angles))),
        actual_target={name:record(a[name]) for name in
            ('gamma','beta','K','K1','s','s1','T','T1','sigma_s','q')},
        kernel={})
    for epsilon,p in polynomials.items():
        out['kernel'][epsilon]={name:record(interval_bounds(p[name].closed_cells(args.angles)))
            for name in ('F','A','G')}
    return out


def jump_budget(c,j,args):
    r=c['nodes'][j]
    k=min(bisect_right(c['tn'],r)-1,len(c['rows'])-1)
    a=extended_target(c['rows'][k],r,r,c['nu'])
    yl,yrl=polynomial_ranges(c['saved'],c['nodes'],j-1,r,r)
    yr,yrr=polynomial_ranges(c['saved'],c['nodes'],j,r,r)
    _,vl,_,ml,_=lift_state(yl,yrl,a,c['alpha'],c['modes'],c['grid'],c['fft'])
    _,vr,_,mr,_=lift_state(yr,yrr,a,c['alpha'],c['modes'],c['grid'],c['fft'])
    exact=actual_jump(c['saved'],c['nodes'],j);m=c['modes']
    cv=zeros((c['grid'],))
    dm=c['alpha']*exact_arb(exact[m]);cv[0]=CBox.from_acb(acb(dm))
    for h in range(1,m+1):
        x=c['alpha']*exact_arb(exact[m+h])/2
        cv[h]=cv[-h]=CBox.from_acb(acb(x))
    dv=Finite(cv,m,c['fft'])
    # Accurate right-minus-left identity avoids subtracting large A enclosures.
    Josc=a['beta']*a['T']*((vr+vl)*dv).primitive()
    jc=a['gamma']*a['T']*dm/(2*a['q'])
    budgets={str(eps):record((Josc+eps*jc).norm().upper()) for eps in (-1,1)}
    return dict(candidate_join=j,radius=str(r),exact_bump=str(exact_w_value(r)),
        original_target_row=k,actual_scalar_germ=c['rows'][k]['actual_scalar_germ'],
        exact_mean_v_jump=record(dm),full_A_jump_A0=budgets,
        jump_convention='right minus left; its contribution in the derivative formula has negative sign')


def complete_bounds(c,doc,args):
    rows=doc['rows'];n=len(rows)
    if n!=len(c['cuts'])-1:
        raise ValueError('a saved prefix is not a complete return-derivative certificate')
    lengths=[exact_arb(c['cuts'][i+1]-c['cuts'][i]) for i in range(n)]
    rates=[box_from_record(row['F_phi']) for row in rows]
    # suffix[i] encloses the whole actual integral from the i-th radial cut to b.
    suffix=[arb(0) for _ in range(n+1)]
    for i in range(n-1,-1,-1):suffix[i]=suffix[i+1]+lengths[i]*rates[i]
    derivative={str(eps):[arb(0),arb(0)] for eps in (-1,1)}
    spatial=suffix[0].exp()
    doc['jumps']=[]
    jumps_at={}
    for j,r in enumerate(c['nodes']):
        if j>0 and CONTROL_LEFT<r<CONTROL_RIGHT:
            item=jump_budget(c,j,args);doc['jumps'].append(item)
            i=bisect_right(c['cuts'],r)-1
            if c['cuts'][i]!=r:raise ValueError('a true centre interface was not in the common partition')
            jumps_at[i]=item
    for i,row in enumerate(rows):
        # A point inside this cell sees only part of the current rate interval.
        exponent_lo=(suffix[i+1].lower()+min(arb(0),lengths[i]*rates[i].lower())).lower()
        exponent_hi=(suffix[i+1].upper()+max(arb(0),lengths[i]*rates[i].upper())).upper()
        Wlo=exponent_lo.exp().lower();Whi=exponent_hi.exp().upper()
        weight=exact_arb(Fraction(row['exact_bump_integral']))
        row['remaining_characteristic_weight_lower']=record(Wlo)
        row['remaining_characteristic_weight_upper']=record(Whi)
        for eps in ('-1','1'):
            G=box_from_record(row['kernel'][eps]['G']);lo=G.lower();hi=G.upper()
            lower_term=weight*(Wlo*max(arb(0),lo)+Whi*min(arb(0),lo))
            upper_term=weight*(Whi*max(arb(0),hi)+Wlo*min(arb(0),hi))
            derivative[eps][0]=(derivative[eps][0]+lower_term).lower()
            derivative[eps][1]=(derivative[eps][1]+upper_term).upper()
        if i in jumps_at:
            item=jumps_at[i];Wi=suffix[i].upper().exp().upper()
            weighti=exact_arb(Fraction(item['exact_bump']))
            item['remaining_characteristic_weight_upper']=record(Wi)
            for eps in ('-1','1'):
                fee=(Wi*weighti*box_from_record(item['full_A_jump_A0'][eps])).upper()
                derivative[eps][0]=(derivative[eps][0]-fee).lower()
                derivative[eps][1]=(derivative[eps][1]+fee).upper()
    minus=derivative['-1'][0].union(derivative['-1'][1])
    plus=derivative['1'][0].union(derivative['1'][1])
    numerator=plus-minus
    if not spatial>0:raise ValueError('the complete flow ceased to be orientation preserving')
    returned=numerator/spatial
    positive=bool(returned>0);negative=bool(returned<0)
    doc.update(complete=True,whole_closed_circle_and_radial_support=True,
        all_exact_PPoly_A_jumps_paid=True,all_mean_and_original_target_fees_retained=True,
        bounds=dict(plus_flow_nu_derivative=record(plus),
            minus_flow_nu_derivative=record(minus),
            complete_flow_spatial_derivative=record(spatial),
            complete_return_nu_derivative=record(returned)),
        strict_frozen_centre_return_positive=positive,
        strict_frozen_centre_return_negative=negative,
        strict_frozen_centre_sign_resolved=positive or negative,
        sign_failure_is_preserved_not_replaced_by_a_finite_sample=True,
        endpoint_formula='Phi_minus^{-1} composed with Phi_plus on the complete bump support',
        no_claim_of_rotation_number_strict_monotonicity_without_actual_conjugacy=True)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--target',type=Path,default=Path('notes/2026-11-13-Codazzi-true-target-r02-v1-native.json.gz'))
    ap.add_argument('--type-cover',type=Path,default=Path('notes/2026-11-13-R133-compact-nu-full-type-cover-native.json.gz'))
    ap.add_argument('--angles',type=int,default=1024)
    ap.add_argument('--radial-subdivisions',type=int,default=1)
    ap.add_argument('--resume',type=Path)
    ap.add_argument('--max-new-rows',type=int)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=320;ctx.cap=6;start=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve every actual mathematical outcome')
    c,doc=prepare(args)
    if args.resume:
        old=read(args.resume)
        for key in ('kind','source_sha256','inputs','candidate_metadata','exact_parameter',
            'exact_amplitude','exact_interval','total_radial_cells','finite_product_grid',
            'closed_angular_cells','radial_subdivisions','dependencies'):
            if old[key]!=doc[key]:raise ValueError('saved complete-prefix identity changed: '+key)
        if old['complete'] or old['failure'] is not None:
            raise ValueError('only an explicitly successful saved row prefix may be resumed')
        for index,row in enumerate(old['rows']):
            left,right,j,k,actual=identity(c,index)
            if (row['common_row']!=index or row['interval']!=list(map(str,(left,right)))
                or row['candidate_piece']!=j or row['original_target_row']!=k
                or row['actual_scalar_germ']!=actual['actual_scalar_germ']):
                raise ValueError('a saved actual row lost its exact closed interval')
        doc['rows']=old['rows'];doc['resume_history']=old['resume_history']+[
            dict(path=str(args.resume),sha256=sha(args.resume),saved_rows=len(old['rows']),
                original_complete=False,missing_process_exit_status_not_inferred=True)]
    first=len(doc['rows']);last=len(c['cuts'])-1
    if args.max_new_rows is not None:
        if args.max_new_rows<=0:raise ValueError('explicit positive new-row count required')
        last=min(last,first+args.max_new_rows)
    checkpoint=time.monotonic()
    try:
        for index in range(first,last):
            doc['rows'].append(row_budget(c,index,args))
            if time.monotonic()-checkpoint>15:
                doc['wall_seconds']=time.monotonic()-start;save(args.out,doc)
                print(dict(saved_rows=len(doc['rows']),total=len(c['cuts'])-1,
                    right=doc['rows'][-1]['interval'][1]),flush=True)
                checkpoint=time.monotonic()
        if len(doc['rows'])==len(c['cuts'])-1:complete_bounds(c,doc,args)
        else:doc['explicit_complete_row_prefix_only']=True
    except Exception as exc:
        doc['failure']=dict(type=type(exc).__name__,message=str(exc))
        raise
    finally:
        doc['wall_seconds']=time.monotonic()-start;save(args.out,doc)
    print(dict(complete=doc['complete'],failure=doc['failure'],
        rows=len(doc['rows']),jumps=len(doc['jumps']),
        actual_frozen_centre_sign_resolved=doc.get('strict_frozen_centre_sign_resolved'),
        out=str(args.out)),flush=True)


if __name__=='__main__':
    main()
