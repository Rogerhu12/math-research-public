#!/usr/bin/env python3
"""New full fixed-g+ response with an exact moment, physical cost, and actual finite-angle corrections."""
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
from scipy.linalg import qr, svd
from r675_bowed_endpoint_pose_response_20261128 import (
    Endpoint, ResponseSpace, bdelta, dot, emit, pack, plus, read, relative, strains)


def scaled(v,c):
    return [a*c for a in v]


def as_grid(sp,r,phi,weights):
    g=sp.end.evaluate(r,phi)
    g.update(r=r,phi=phi,weights=weights,b=[sp.scale*sp.spl(r,k)[:,3:-3] for k in range(3)])
    return g


def import_field(old,x,sp):
    source={pair:row for row,pair in enumerate(old.blocks)}
    y=np.zeros(sp.size); y[-2:]=x[-2:]
    knots=[r for r in sp.edges[1:-1] if not np.any(np.isclose(r,old.edges,atol=1.e-14,rtol=0.))]
    for row,pair in enumerate(sp.blocks):
        if pair not in source:
            continue
        i=source[pair]; c=np.r_[np.zeros(3),x[i*old.nb:(i+1)*old.nb],np.zeros(3)]
        f=BSpline(old.spl.t,c,5)
        for r in knots:
            f=f.insert_knot(float(r))
        if len(f.c)-6!=sp.nb:
            raise ValueError('Paid field was not transported into its nested space.')
        y[row*sp.nb:(row+1)*sp.nb]=f.c[3:-3]
    return y


def relative_curvature_map(raw,r):
    D,Y=raw[1],raw[2]/r[:,None,None]
    area=np.cross(D,Y); norm=np.linalg.norm(area,axis=-1)
    if norm.min()<1.e-10:
        raise FloatingPointError('Singular finite actual frame.')
    n=area/norm[...,None]
    e,f,k=dot(D,D),dot(D,Y),dot(Y,Y); det=norm**2
    second=[raw[3],raw[4]/r[:,None,None],raw[5]/r[:,None,None]**2]
    gam=[]
    for h in second:
        d,p=dot(h,D),dot(h,Y)
        gam.append(((k*d-f*p)/det,(e*p-f*d)/det))
    return D,Y,n,gam


def operators(sp,g,raw,indices):
    """All currently supported original columns, in radial-major order, and real material b'."""
    r=g['r'][:,None]; D,Y,n,gamma=relative_curvature_map(raw,g['r']); nphi=len(g['phi'])
    ord_ids=[]; cols=[]; blocks=len(sp.blocks)
    for i in indices:
        for j,(coord,harmonic) in enumerate(sp.blocks):
            ord_ids.append(i*blocks+j)
            sf,df,ddf=sp.angular(coord,harmonic,g['phi'])
            B,Br,Brr=[m[:,i,None] for m in g['b']]
            cols.append((coord,Br*sf,B*df/r,(Brr*sf,Br*df/r,B*ddf/r**2)))
    for j,coord in enumerate((0,2)):
        ord_ids.append(sp.size-2+j); c,c1,c2=g['chi']; zeros=np.zeros_like(D[...,0])
        cols.append((coord,np.broadcast_to(sp.scale*c1[:,None],zeros.shape),zeros,
                     (np.broadcast_to(sp.scale*c2[:,None],zeros.shape),zeros,zeros)))
    nr=len(r); nc=len(cols); A=np.empty((3,nr,nphi,nc)); B=np.empty_like(A)
    for i,(coord,vr,vp,second) in enumerate(cols):
        A[0,...,i]=2*D[...,coord]*vr; A[2,...,i]=2*Y[...,coord]*vp
        A[1,...,i]=D[...,coord]*vp+Y[...,coord]*vr
        for j,(s,(gr,gp)) in enumerate(zip(second,gamma)):
            B[j,...,i]=n[...,coord]*(s-gr*vr-gp*vp)
    return np.array(ord_ids),A,B


class RadialQR:
    """Exact row-orthogonal span elimination; all original columns and the affine residual survive."""
    def __init__(self,cols,count):
        self.square=np.zeros((cols+1,cols+1)); self.ids=np.empty(0,dtype=int)
        self.carry=np.empty((0,0)); self.count=count

    def add(self,ids,local,finish):
        together=np.union1d(ids,self.ids); c=len(together)
        work=np.zeros((len(self.carry)+len(local),c),order='F')
        work[:len(self.carry),np.searchsorted(together,self.ids)]=self.carry
        work[len(self.carry):,np.searchsorted(together,ids)]=local
        r=qr(work,mode='r',overwrite_a=True,check_finite=False)[0][:c]
        if len(r)!=c:
            raise ArithmeticError('Span QR did not have sufficient full rows.')
        done=int(np.searchsorted(together,finish,side='right'))
        self.square[np.ix_(together[:done],together)]=r[:done]
        self.ids=together[done:]; self.carry=r[done:,done:].copy()
        self.count['full_supported_span_QR']+=1


def reordered(sp):
    return np.r_[np.arange(sp.nb*len(sp.blocks)).reshape(len(sp.blocks),sp.nb).T.ravel(),sp.size-2,sp.size-1]


def assemble(sp,order,angles,params,q,linear,count):
    zl,wb=np.polynomial.legendre.leggauss(order); phi=2*np.pi*np.arange(angles)/angles
    left,right=RadialQR(sp.size,count),RadialQR(sp.size,count)
    expiry=sp.spl.t[np.arange(sp.nb)+3+6]; blocks=len(sp.blocks)
    for i,(lo,hi) in enumerate(zip(sp.edges[:-1],sp.edges[1:])):
        r=(lo+hi+(hi-lo)*zl)/2; w=(hi-lo)*wb/(2*sp.scale); g=as_grid(sp,r,phi,w)
        correction=sp.fields(params,g)
        if linear:
            raw=g['raw']; v=plus(g['pose'],correction); metric=strains(raw,v,r); second=bdelta(raw,v,r)
        else:
            raw=plus(g['state'](q),correction)
            metric=metric_defect(raw,g['raw'],r); second=[np.zeros_like(metric[0])]*3
        active=np.where(np.max(abs(g['b'][0]),axis=0)>0)[0]
        ids,A,B=operators(sp,g,raw,active)
        W=np.sqrt(w[:,None]/angles)*np.ones((1,angles)); ww=np.stack((W,math.sqrt(2)*W,W))
        ab=np.column_stack(((A*ww[...,None]).reshape(-1,len(ids)),pack(metric,g)))
        bb=np.column_stack(((B*ww[...,None]).reshape(-1,len(ids)),pack(second,g)))
        full_ids=np.r_[ids,sp.size]
        expired=np.flatnonzero(expiry<=hi+1e-14)
        finish=sp.size if i==len(sp.edges)-2 else (int(expired[-1]+1)*blocks-1 if len(expired) else -1)
        left.add(full_ids,ab,finish); right.add(full_ids,bb,finish)
    if left.carry.size or right.carry.size:
        raise ArithmeticError('Unfinished full-column radial elimination.')
    count['all_original_physical_matrices']+=1; count['all_original_columns']+=sp.size
    return left.square,right.square


def metric_defect(raw,base,r):
    rd=r[:,None,None]; D,Y=raw[1],raw[2]/rd; d,y=base[1],base[2]/rd
    return [dot(D,D)-dot(d,d),dot(D,Y)-dot(d,y),dot(Y,Y)-dot(y,y)]


def moment(sp,params,order):
    # Reference moment is linear in the complete Cartesian field, with actual variation of the normal.
    nodes,weights=np.polynomial.legendre.leggauss(order); end=sp.end
    m=np.zeros(sp.size); value=0.; phi=np.array([np.pi/2])
    for lo,hi in zip(sp.edges[:-1],sp.edges[1:]):
        if lo<end.l-1.e-14 or hi>end.u+1.e-14:
            continue
        r=(lo+hi+(hi-lo)*nodes)/2; w=(hi-lo)*weights/2; g=as_grid(sp,r,phi,w/sp.scale)
        active=np.where(np.max(abs(g['b'][0]),axis=0)>0)[0]
        ids,_,B=operators(sp,g,g['raw'],active); v=plus(g['pose'],sp.fields(params,g))
        b0=bdelta(g['raw'],v,r); c=np.cos(g['angle']); h=g['Hr']; N=np.sqrt(1+(h*c)**2)
        f=w*c/(2*g['wr']*N); j=f*h/r; k=f*g['Hrr']
        m[ids]+=j@B[0,:,0,:]+k@B[2,:,0,:]; value+=j@b0[0][:,0]+k@b0[2][:,0]
    return m,float(value)


def constrained_pencil(A,B,m,value,scales,count):
    # Householder imposes the one physical equality. Every orthogonal free direction is retained.
    unit=m/np.linalg.norm(m); sign=1. if unit[-1]>=0 else -1.
    house=unit.copy(); house[-1]+=sign; house/=np.linalg.norm(house)
    last=(-1-value)/(-sign*np.linalg.norm(m))
    def transform(F):
        G=F[:,:-1]-2*(F[:,:-1]@house)[:,None]*house[None,:]
        return G[:,:-1],F[:,-1]+last*G[:,-1]
    L,l0=transform(A); K,k0=transform(B)
    def recover(y):
        z=np.r_[y,last]; return z-2*(house@z)*house
    for scale in scales:
        J=np.asfortranarray(np.vstack((L,scale*K))); b=np.r_[l0,scale*k0]
        Q,R=qr(J,mode='economic',overwrite_a=True,check_finite=False); rhs=Q.T@b
        del Q,J
        U,s,vt=svd(R,full_matrices=False,check_finite=False); f=U.T@rhs
        sol=recover(-vt.T@np.divide(f,s,out=np.zeros_like(f),where=s!=0))
        count['complete_hard_moment_QR_SVD']+=1
        yield scale,sol,s


def physical(sp,params,g,q):
    r=g['r']; rd=r[:,None,None]; raw=plus(g['state'](q),sp.fields(params,g))
    D,Y,n,_=relative_curvature_map(raw,r); area=dot(np.cross(D,Y),np.cross(D,Y))
    e,f,k=dot(D,D),dot(D,Y),dot(Y,Y)
    b11,b12,b22=dot(n,raw[3]),dot(n,raw[4]/rd),dot(n,raw[5]/rd**2)
    mean=(b11*k-2*b12*f+b22*e)/(2*area); gauss=(b11*b22-b12*b12)/area
    curve=np.abs(mean)+np.sqrt(np.maximum(mean**2-gauss,0))
    errs=metric_defect(raw,g['raw'],r); eta=relative(g['raw'],errs,r)
    F=raw[0]; rho=np.linalg.norm(F[...,:2],axis=-1); z=F[...,2]
    angle=sp.end.theta+q; co,s=math.cos(angle),math.sin(angle); d,h=sp.scale*params[-2:]
    T=.03; B=1/3; c=5/12; H=.35; lam=(B+c)/H
    peg=[(abs(d)+.075+.0336*abs(s),h-.075*abs(s),h+.0336*co+.075*abs(s)),
         (abs(d)+.043+.28*abs(s),h-.043*abs(s),h+.28*co+.043*abs(s))]
    ring=(float(rho.max()),float(z.min()),float(z.max())); allparts=[ring]+peg
    maxrad=max(v[0] for v in allparts); zmin=min(v[1] for v in allparts); zmax=max(v[2] for v in allparts)
    diameter=max(max(2*B,math.hypot(B+c,H))+.09002,math.hypot(2*maxrad,zmax-zmin))
    for rad,lo,hi in allparts:
        for cc,zz in ((B,-.045),(c,-H-.045)):
            diameter=max(diameter,.04501+math.hypot(rad+cc,max(abs(lo-zz),abs(hi-zz))))
    side=max(float(np.max(rho+lam*(-z-.045))),*(rad+lam*(-lo-.045) for rad,lo,_ in peg))
    cover=B+.02+.04*lam-side-2*T*math.hypot(1,lam)
    sup=min((H+.045)*co-c*abs(s)+.04499-float(np.max(abs(s)*rho-co*z)),
            *((H+.045)*co-c*abs(s)+.04499-(abs(s)*rr-co*lo) for rr,lo,_ in peg))
    guard=dict(curvature=1/T-float(curve.max()),outer_normal=float(n[...,2].min()),
               inner_normal=float((s*n[...,0]+co*n[...,2]).min()),outer_side=cover,
               outer_cylinder=B-.00001-maxrad-2*T,peg_cylinder=sp.end.b-(abs(d)+.075+(.28+T)*abs(s)),
               diameter=1-diameter,sphere_dominance=sup)
    ix=np.unravel_index(np.argmax(eta),eta.shape); ic=np.unravel_index(np.argmax(curve),curve.shape)
    def loc(i): return [float(r[i[0]]),float(g['phi'][i[1]])]
    return dict(actual_angle_increment=q,actual_inner_angle=angle,inner_translation_xz=[float(d),float(h)],
                finite_fixed_g_eta=float(eta[ix]),metric_attainer=loc(ix),finite_metric_L2=float(np.linalg.norm(pack(errs,g))),
                sampled_max_abs_actual_curvature=float(curve[ic]),curvature_attainer=loc(ic),
                sampled_whole_shell_margins=guard,sampled_whole_shell_pass=bool(min(guard.values())>0),
                sampled_D_upper_estimate=diameter,all_caps=2)


def samples(sp,n,opts):
    return sp.grid(opts['independent_order'],max(n,opts['independent_angles']),True)


def checkpoint(particle,sp):
    row=particle['row']; old=ResponseSpace(sp.end,row['bands'],row['K'])
    x=import_field(old,np.asarray(particle['coefficients']),sp)
    weak=import_field(old,np.asarray(particle['weakest']),sp)
    return x,weak


def unique_poses(sp,params,opts):
    return [(q,q*params) for q in opts['angles']]


def main():
    if (os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'
        or not os.environ.get('GITHUB_RUN_ID','').isdigit()):
        raise SystemExit('Scientific execution requires public math-research-public Actions.')
    ap=argparse.ArgumentParser(); ap.add_argument('--geometry',required=True); ap.add_argument('--max-seconds',required=True,type=float)
    args=ap.parse_args(); opts=json.loads(Path(args.geometry).read_text()); prior=json.loads(Path(opts['previous']).read_text())
    if prior['run']!=46141399411 or len(prior['states'])!=5:
        raise ValueError('Wrong naturally completed R675 transport.')
    start=time.perf_counter(); elapsed=lambda:time.perf_counter()-start; count=Counter()
    end=Endpoint(opts,count); sp=ResponseSpace(end,opts['bands'],opts['K']); order=reordered(sp)
    orig=lambda v: v[np.argsort(order)]; fine=samples(sp,2*sp.K+5,opts)
    qgoal=opts['angles'][-1]; x0=None; y=None; rec=[]; accepted=0; current_q=0.
    emit('provenance',prior_run=prior['run'],prior_seconds=prior['seconds'],prior_costs=prior['counts'],
         all_original_columns=sp.size,old_matrices_replayed=False,fixed_metric='actual R673 positive endpoint',
         source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    try:
        bank=[]
        for entry in prior['states']:
            x,w=checkpoint(entry,sp); bank.append((x,w))
        x0=bank[-1][0].copy(); z0=np.zeros(sp.size)
        # Every transported weak direction has its actual central moment charged in this new space.
        m,mzero=moment(sp,z0,opts['moment_order']); value=mzero+m@x0[order]
        audit=[]
        for entry,(x,w) in zip(prior['states'],bank):
            coeff=float(m@w[order]); oldval=float(mzero+m@x[order]); tw=None
            if abs(coeff)>1.e-12:
                amp=(-1-oldval)/coeff; trial=x+amp*w
                try:
                    weak_finite=physical(sp,qgoal*trial,fine,qgoal)
                except FloatingPointError as exc:
                    weak_finite=dict(sampled_whole_shell_pass=False,reason=str(exc))
                tw=dict(amplitude=float(amp),actual=read(sp,trial,fine),finite=weak_finite)
            audit.append(dict(space=entry['row']['space'],actual_moment=oldval,weak_unit_moment=coeff,
                              finite_weak_moment_correction=tw,paid_minimum_sigma=entry['row']['minimum_sigma']))
        emit('transported_five_actual_states',new_measurements=audit,complete_initial=x0.tolist(),seconds=elapsed())
        A,B=assemble(sp,opts['work_order'],opts['work_angles'],x0,0.,True,count)
        grid=sp.grid(opts['work_order'],opts['work_angles']); d=np.sin(np.arange(1,sp.size+1)*.417);d/=np.linalg.norm(d)
        perturb=x0+orig(d); v=plus(grid['pose'],sp.fields(perturb,grid)); err=[]
        for mat,expected in [(A,pack(strains(grid['raw'],v,grid['r']),grid)),(B,pack(bdelta(grid['raw'],v,grid['r']),grid))]:
            err.append(float(abs(np.linalg.norm(mat@np.r_[d,1])-np.linalg.norm(expected))/max(1e-16,np.linalg.norm(expected))))
        ma,mv=moment(sp,perturb,opts['moment_order']+3); merr=abs(value+m@d-mv)
        emit('orthogonal_full_rows_check',norm_errors=err,independent_moment_error=float(merr),all_columns=sp.size)
        if max(err)>2e-10 or merr>2e-8:
            raise ArithmeticError('Complete physical factor or moment did not reconstruct the actual field.')
        candidates=[]
        for weight,delta,sv in constrained_pencil(A,B,m,value,opts['bending_scales'],count):
            if elapsed()>args.max_seconds-opts['reserve_seconds'] and candidates:
                break
            x=x0+orig(delta); mr,mv=moment(sp,x,opts['moment_order']+4)
            if abs(mv+1)>2e-7:
                raise ArithmeticError('Exact scalar moment missing in independent quadrature.')
            rd=read(sp,x,fine); results=[]
            for q,yy in unique_poses(sp,x,opts):
                try:
                    results.append(physical(sp,yy,fine,q))
                except FloatingPointError as exc:
                    results.append(dict(actual_angle_increment=q,sampled_whole_shell_pass=False,reason=str(exc)))
            errL=float(np.linalg.norm(A@np.r_[delta,1])); bL=float(np.linalg.norm(B@np.r_[delta,1]))
            row=dict(weight=weight,complete_hard_moment=mv,work_strain_L2=errL,work_bending_L2=bL,
                     independent_unit_response=rd,finite_poses=results,all_singular_values=sv.tolist())
            emit('hard_moment_full_solution',**row,all_actual_unit_coefficients=x.tolist(),seconds=elapsed())
            rec.append({k:v for k,v in row.items() if k!='all_singular_values'}); candidates.append((x,results))
        if not candidates: raise ArithmeticError('No complete hard moment solution.')
        # Local continuation follows genuine fixed-g states in consecutive finite angle stations.
        # The zero reference and exact rigid pose are always independent fallback predictors.
        previous=z0.copy(); reports=[]; last_direction=candidates[0][0]
        for station,q in enumerate(opts['angles']):
            if elapsed()>args.max_seconds-opts['reserve_seconds']: break
            proposals=[('secant',previous+(q-current_q)*last_direction),('rigid_lift',previous.copy())]
            proposals.extend((f'paid_hard_moment_{i}',q*x) for i,(x,_) in enumerate(candidates))
            allowed=[]
            for name,test in proposals:
                try: ob=physical(sp,test,fine,q)
                except FloatingPointError: continue
                if ob['sampled_whole_shell_pass']: allowed.append((ob['finite_metric_L2'],name,test,ob))
            if not allowed:
                emit('no_admissible_station',station=station,increment=q); break
            _,name,y,detail=min(allowed,key=lambda v:v[0]); y=y.copy(); new_steps=0
            emit('actual_station_started',station=station,increment=q,predictor=name,independent=detail,all_parameters=y.tolist())
            for i in range(opts['nonlinear_iterations']):
                if elapsed()>args.max_seconds-opts['reserve_seconds']:break
                Anew,Bnew=assemble(sp,opts['work_order'],opts['work_angles'],y,q,False,count)
                # A genuine fixed-g Gauss-Newton step; bending cost regularizes the update, not the fixed reference.
                lastloss=float(np.linalg.norm(Anew[:,-1])); improved=False
                for mu in opts['step_scales']:
                    J=np.asfortranarray(np.vstack((Anew[:,:-1],mu*Bnew[:,:-1])))
                    Q,R=qr(J,mode='economic',overwrite_a=True,check_finite=False)
                    force=Q[:len(Anew)].T@Anew[:,-1]; del Q,J
                    U,sv,vt=svd(R,full_matrices=False,check_finite=False); force=U.T@force
                    dx=orig(-vt.T@np.divide(force,sv,out=np.zeros_like(force),where=sv!=0))
                    count['nonlinear_all_column_QR_SVD']+=1
                    for fraction in (1.,.5,.25,.125,.0625,.03125):
                        trial=y+fraction*dx; count['nonlinear_actual_trials']+=1
                        try:
                            wk=physical(sp,trial,grid,q); ck=physical(sp,trial,fine,q)
                        except FloatingPointError:
                            continue
                        if (wk['sampled_whole_shell_pass'] and ck['sampled_whole_shell_pass'] and wk['finite_metric_L2']<lastloss
                                and ck['finite_metric_L2']<detail['finite_metric_L2'] and ck['finite_fixed_g_eta']<detail['finite_fixed_g_eta']):
                            y,detail=trial,ck; improved=True; accepted+=1; new_steps+=1
                            emit('actual_fixed_g_update',station=station,iteration=i,mu=mu,fraction=fraction,
                                 independent=detail,all_parameters=y.tolist(),sigma_extrema=[float(sv[-1]),float(sv[0])],seconds=elapsed());break
                    if improved:break
                if not improved or detail['finite_fixed_g_eta']<opts['actual_goal']:break
            slope=(y-previous)/(q-current_q); last_direction=slope; previous=y.copy(); current_q=q
            reports.append(dict(q=q,actual_accepted=new_steps,independent=detail))
        if y is None: y=np.zeros(sp.size)
        if not current_q: y=np.zeros(sp.size)
        crossed={}
        for label,oo,na in [('radius_only',opts['final_order'],opts['independent_angles']),('angle_only',opts['independent_order'],opts['final_angles']),
                            ('both',opts['final_order'],opts['final_angles'])]:
            crossed[label]=physical(sp,y,sp.grid(oo,na,True),current_q)
        emit('terminal',linear_candidates=rec,nonlinear_stations=reports,actual_last_increment=current_q,
             final_actual_correction=y.tolist(),all_columns=sp.size,accepted_nonlinear=accepted,independent_crossed=crossed,
             counts=dict(count),elapsed_seconds=elapsed(),continuous_t_verified=False,README_completion_claim=False)
    except Exception as exc:
        emit('incomplete',reason=str(exc),last_increment=current_q,last_actual_coefficients=None if y is None else y.tolist(),
             counts=dict(count),elapsed_seconds=elapsed()); raise


if __name__=='__main__': main()
