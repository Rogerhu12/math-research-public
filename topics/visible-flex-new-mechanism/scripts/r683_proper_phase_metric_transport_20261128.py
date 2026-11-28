#!/usr/bin/env python3
"""Continue actual R680 geometry to a rotational metric using the whole material annulus."""
from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
import hashlib
import json
import math
import os
from pathlib import Path
import time

import numpy as np
from scipy.linalg import qr, svd
from r659_finite_tilt_latitude_system_20261128 import (
    dot, emit, extend_exactly, jy, peg_readout, rz_frame)
from r669_true_finite_tilt_reach_continuation_20261128 import ReachSystem, trust_step


class TrialDomainError(ArithmeticError):
    pass


def positive_part(z, width):
    """C-infinity vanishing residual and its derivative."""
    pos=np.maximum(z,0.)
    ratio=width/np.maximum(pos,1.e-100)
    factor=np.exp(-ratio)
    return pos*factor, factor*(1+ratio)


class ProperPhase(ReachSystem):
    def __init__(self,spec,counter):
        super().__init__(spec,counter)
        self.d=.05
        self.left=self.a+self.d
        self.right=self.b-self.d
        self.total=self.tail(np.array([self.a]))[0]
        self.scale=self.ang/self.total
        self.cbase=lru_cache(maxsize=20)(self.center_anchor)
        self.intc=(self.spl.antiderivative()(self.a)-self.spl.antiderivative()(self.b))[2:-2]

    def ramp_integral(self,u,endpoint,orientation):
        # Integral d H(t)/(endpoint+orientation*d*t) from zero to u.
        y=-(orientation*self.d/endpoint)*u
        value=np.zeros_like(u)
        for n in range(108,-1,-1):
            value=value*y+3/(n+3)-2*u/(n+4)
        return (self.d/endpoint)*u**3*value

    def tail(self,r):
        l=np.clip((r-self.a)/self.d,0,1)
        h=np.clip((self.b-r)/self.d,0,1)
        return (self.ramp_integral(np.ones_like(l),self.a,1)-self.ramp_integral(l,self.a,1)
                +np.log(self.right/np.clip(r,self.left,self.right))+self.ramp_integral(h,self.b,-1))

    def profile(self,r):
        u=np.minimum.reduce(((r-self.a)/self.d,(self.b-r)/self.d,np.ones_like(r)))
        k=u*u*(3-2*u)
        sign=np.where(r<self.left,1.,np.where(r>self.right,-1.,0.))
        p=-self.scale*k
        dp=-self.scale*6*u*(1-u)*sign/self.d
        return p,dp,self.scale*self.tail(r)

    def center_anchor(self,raw):
        r=np.frombuffer(raw,dtype=np.float64)
        nodes,weights=np.polynomial.legendre.leggauss(24)
        out=np.zeros((len(r),3))
        for lo,hi in ((self.a,self.left),(self.left,self.right),(self.right,self.b)):
            low=np.clip(r,lo,hi)
            half=(hi-low)/2
            sample=(hi+low[:,None])/2+half[:,None]*nodes
            p,_,q=self.profile(sample)
            out[:,0]-=half*((-1.01*p*np.sin(q))@weights)
            out[:,2]-=half*((-1.01*p*np.cos(q))@weights)
        return out

    def center(self,x,r):
        return super().center(x,r)+self.cbase(np.ascontiguousarray(r,dtype=np.float64).tobytes())

    def grid(self,order,azimuths,endpoints=False):
        # Include both real ramp joins as integration breakpoints even where they are not knots.
        z,w=np.polynomial.legendre.leggauss(order)
        cuts=np.unique(np.r_[np.linspace(self.a,self.b,self.nsp+1),self.left,self.right])
        half=np.diff(cuts)/2
        r=((cuts[:-1]+half)[:,None]+half[:,None]*z).ravel()
        weights=(half[:,None]*w/(self.b-self.a)).ravel()
        if endpoints:
            r=np.unique(np.r_[cuts,r]); diff=np.diff(r)
            weights=(np.r_[0,diff]+np.r_[diff,0])/(2*(self.b-self.a))
        return self.at(r,azimuths,weights)

    def at(self,r,azimuths,weights=None):
        g=super().at(r,azimuths,weights)
        p,dp,q=self.profile(r)
        c=np.cos(g['phi'])
        g.update(q=q,qx=p/r,qxx=dp/r-p/r**2,w=-1.01*p,dw=-1.01*dp,
                 anis=p[:,None]**2*(2.02*c+c*c-.5),anchor_E=1+p*p*(1.01**2+.5))
        return g

    def state(self,x,g,second=False):
        st=super().state(x,g,second)
        body=g['w'][:,None]*g['ez']
        st['D']+=body[:,None,:]
        st['Cp']+=rz_frame(body,g['q'])
        st['E']=dot(st['D'],st['D']).mean(axis=1)
        if second:
            st['Drr']+=(g['dw'][:,None]*g['ez']+g['qx'][:,None]*jy(body))[:,None,:]
        return st


def cone_data(sh,T):
    # Both trace/2 and determinant must be positive for each physical quadratic form.
    h=T*sh['eigen'][0][1]
    l=T*sh['eigen'][1][1]
    # Gradients below are w.r.t. the signed R669 rows dh and -dl.
    vals=[]; deriv=[]
    for s in (1,-1):
        vals.extend((1+s*(h+l)/2,(1+s*h)*(1+s*l)))
        deriv.extend(((s/2,-s/2),(s*(1+s*l),-s*(1+s*h))))
    vals.extend(dot(sh['n'],axis) for axis in sh['axes'])
    return vals,deriv


def directional_length(sys,grid,sh,anchor,level,opts):
    # Full xz circle, two opposite meridians, including overlapping tangent cones.
    beta=grid['beta']; direction=grid['directions']; sign=grid['sign']
    A=np.abs(np.angle(np.exp(1j*(beta+sys.ang)))); B=np.abs(beta)
    length=sh['length']; T=opts['T']; span=sys.b-sys.a
    def ceiling(S):
        if S<T*max(abs(A-B)):
            raise TrialDomainError('End tangent cones could not meet at the actual length.')
        m=np.maximum(0.,(A+B-S/T)/2)
        non=S-T*(A-np.sin(A)+B-np.sin(B))
        over=T*(np.sin(A)+np.sin(B)-2*np.sin(m))
        return np.where(m>0,over,non),np.cos(m)
    d=np.array([sys.b-sys.a*math.cos(sys.ang),sys.a*math.sin(sys.ang)])
    def chords(c):
        return (direction@d)[None,:]+sign*(direction@c)[None,:]
    old=np.maximum(0.,chords(anchor['C'])-ceiling(anchor['S'])[0][None,:])
    latest,du=ceiling(length)
    raw=chords(sh['actual_center'])-latest[None,:]
    z=(raw-(1-level)*(old+1e-12)+level*opts['length_buffer'])/span
    return z,du,float(-raw.max())


def angular_grid(n):
    beta=np.linspace(-np.pi,np.pi,n,endpoint=False)
    return dict(beta=beta,directions=np.stack((np.cos(beta),np.sin(beta)),axis=1),sign=np.array([[1.],[-1.]]))


def prepare(sys,g,opts,nbeta):
    x=np.zeros(sys.size); st=sys.state(x,g,True)
    sh=sys.shape(x,g,st,opts,g['weights']); cone,_=cone_data(sh,opts['T'])
    guards=[np.minimum(cap,.8*value) for value,cap in zip(cone,(.28,.20,.28,.20,.38,.38))]
    return dict(guards=guards,C=sh['actual_center'],S=sh['length'],angles=angular_grid(nbeta))


def evaluate(sys,x,g,level,opts,anchor,fixed=None):
    sys.count['actual_design_evaluations']+=1
    st=sys.state(x,g,True); D,H=st['D'],st['H']; E=st['E'] if fixed is None else fixed
    mr=sys.pack(dot(D,D)-E[:,None]-(1-level)*g['anis'],dot(D,H),dot(H,H)-1,
                st['T'][...,1].mean(axis=1),g)
    sh=sys.shape(x,g,st,opts,g['weights'])
    if fixed is not None:
        sh['length']=(sys.b-sys.a)*float(g['weights']@np.sqrt(fixed))
    vals,derivatives=cone_data(sh,opts['T'])
    weights=np.sqrt(g['weights'][:,None]/len(g['phi']))
    data=[]; blocks=[]
    for val,guard in zip(vals,anchor['guards']):
        cost,der=positive_part(guard-val,opts['smooth_width'])
        blocks.append((opts['physical_weight']*weights*cost).ravel())
        data.append(-opts['physical_weight']*der)
    z,du,margin=directional_length(sys,anchor['angles'],sh,anchor,level,opts)
    cost,der=positive_part(z,opts['smooth_width'])
    # Normalize each equally weighted directional budget; hard curvature is separate.
    factor=opts['length_weight']/math.sqrt(cost.size)
    res=np.r_[mr,*blocks,(factor*cost).ravel()]
    sh.update(cone_grad=derivatives,chain=data,zder=factor*der,du=du,
              reference=anchor,physical_margin=min(float(np.min(v)) for v in vals),
              directional_margin=margin,metric_norm=float(np.linalg.norm(mr)))
    return res,st,sh


def full_matrix(sys,x,g,st,sh,opts,fixed):
    # Request R669's analytical original columns only where at least one smooth row needs them.
    # Any removed row has exactly zero derivative AND zero residual. Metric rows stay complete.
    cha=sh['chain']; shape=cha[0].shape
    active=[v!=0 for v in cha]; common=np.logical_or.reduce(active[:4])
    raw_masks=[common,common,active[4],active[5]]
    old=dict(sh,constraints=[np.where(m,1.,-1.) for m in raw_masks],cgrad=np.zeros(2),excess=1.)
    raw,unused=sys.full_jacobian(x,g,st,old,opts,fixed)
    nmetric=3*shape[0]*shape[1]+shape[0]; offset=nmetric; channels=[]
    for mask in raw_masks:
        nn=int(mask.sum()); channels.append(raw[offset:offset+nn]); offset+=nn
    minus_dS=raw[offset]; gathered=[raw[:nmetric]]
    masks=[np.ones(nmetric,dtype=bool)]
    for i,mask in enumerate(active):
        masks.append(mask.ravel())
        if not mask.any():
            continue
        if i<4:
            h,l=sh['cone_grad'][i]
            hs=np.broadcast_to(h,shape)[mask,None]; ls=np.broadcast_to(l,shape)[mask,None]
            piece=hs*channels[0][mask[common]]+ls*channels[1][mask[common]]
        else:
            piece=-channels[i-2]
        gathered.append(cha[i][mask,None]*piece)
    ang=sh['reference']['angles']; zg=sh['zder']; lmask=zg!=0
    masks.append(lmask.ravel())
    if lmask.any():
        ii,jj=np.nonzero(lmask)
        lrows=sh['du'][jj,None]*minus_dS[None,:]
        coeff=ang['sign'][ii]*ang['directions'][jj]/(sys.b-sys.a)
        for k in range(2):
            start=2*sys.K*sys.na+k*sys.nc
            lrows[:,start:start+sys.nc]+=coeff[:,k,None]*sys.intc
        gathered.append(zg[lmask,None]*lrows)
    sys.count['complete_new_cone_matrices']+=1
    return np.asfortranarray(np.vstack(gathered)),np.concatenate(masks)


def shell(sys,x,g,st,sh):
    """Pointwise finiteness checks on this grid and rigorous peg envelopes conditional on C."""
    s=math.sin(sys.ang); co=math.cos(sys.ang); T=.03
    center=sys.center(x,g['r'])
    F=center[:,None,:]+g['r'][:,None,None]*rz_frame(st['U'],g['q'][:,None])
    rho=np.linalg.norm(F[...,:2],axis=-1); z=F[...,2]
    d,h=sh['actual_center']; lam=.845/.29
    side=.285+.02+.04*lam; border=2*T*math.hypot(1,lam)
    ra=float(rho.max()); za=float(z.min()); zb=float(z.max())
    # Two real R655 peg pieces. Overestimate radius and height jointly for each piece.
    pieces=[(abs(d)+.075+.0336*s,h-.075*s,h+.0336*co+.075*s),
            (abs(d)+.043+.28*s,h-.043*s,h+.28*co+.043*s)]
    maxradius=max(ra,*(t[0] for t in pieces)); zmin=min(za,*(t[1] for t in pieces))
    zmax=max(zb,*(t[2] for t in pieces))
    def from_outer(radius,lo,hi):
        def mixed(c,origin):
            return .04501+math.hypot(radius+c,max(abs(lo-origin),abs(hi-origin)))
        return max(mixed(.285,-.045),mixed(.56,-.335))
    diam=max(max(.57,math.hypot(.845,.29))+.09002,math.hypot(2*maxradius,zmax-zmin),
             from_outer(ra,za,zb),*(from_outer(*piece) for piece in pieces))
    weak_support=.335*co-.56*s+.04499
    disk_support=max(float(np.max(s*rho-co*z)),*(s*rp-co*z0 for rp,z0,_ in pieces))
    side_needed=max(float(np.max(rho+lam*(-z-.045))),*(rp+lam*(-z0-.045) for rp,z0,_ in pieces))+border
    return dict(sampled_curvature_margin=1/T-sh['max_abs_curvature'],
                sampled_outer_normal_min=sh['min_outer_normal'],sampled_inner_normal_min=sh['min_inner_normal'],
                sampled_side_margin=side-side_needed,sampled_cylinder_margin=.285-.00001-maxradius-2*T,
                peg_outer_tube_cylinder_margin=sys.b-(abs(d)+.075+(.28+T)*s),
                sampled_whole_support_dominance=weak_support-disk_support,sampled_whole_D_upper_estimate=diam,
                conditional_hold_support_difference=2*.56*s,actual_inner_center_xz=[float(d),float(h)])


def shell_ok(d):
    return (min(d[k] for k in ('sampled_curvature_margin','sampled_outer_normal_min',
                'sampled_inner_normal_min','sampled_side_margin','sampled_cylinder_margin',
                'peg_outer_tube_cylinder_margin','sampled_whole_support_dominance'))>0
            and d['sampled_whole_D_upper_estimate']<1)


def fixed_port(sys,x,g,st,E,Eprime):
    inside=(g['t']>=.15)&(g['t']<=.85)
    if inside.sum()<3 or np.min(E[inside])<=1+1e-12:
        return dict(available=False,reason='positive frozen reference slope unavailable on the tested compact interval')
    r=g['r']; phi=g['phi']; rad=r[inside]
    amplitude=np.sqrt(E[inside]-1); rate=Eprime[inside]/(2*amplitude)
    D,H=st['D'],st['H']; q=g['q'][:,None]
    er=g['er']; et=g['et']; F=sys.center(x,r)[:,None,:]+r[:,None,None]*rz_frame(st['U'],q)
    vr=(rz_frame(D,q)-er)[inside].copy(); vr[...,2]+=amplitude[:,None]
    vp=(r[:,None,None]*(rz_frame(H,q)-et))[inside]
    def harmonic(z,j):
        return 2*np.mean(z*j[None,:],axis=1)
    co=np.cos(phi); si=np.sin(phi)
    p=-harmonic(dot(vr,vr),co)/2; qv=-harmonic(dot(vp,vp),co)/(2*rad); mix=-harmonic(dot(vr,vp),si)
    pe=harmonic((dot(D,D)-E[:,None])[inside],co)/2
    qe=rad*harmonic((dot(H,H)-1)[inside],co)/2
    se=rad*harmonic(dot(D,H)[inside],si)
    def integral(pp,qq,ss):
        boundary=qq/(amplitude*rad)
        return float(boundary[-1]-boundary[0]+np.trapezoid(qq*rate/(amplitude**2*rad)-ss/(amplitude*rad**2)-pp/(amplitude*rad),rad))
    u=harmonic(F[inside,:,2],co)/rad
    prediction,correction=integral(p,qv,mix),integral(pe,qe,se)
    return dict(available=True,interval=[float(rad[0]),float(rad[-1])],sampled_measured_change=float(u[-1]-u[0]),
                full_displacement_quadratic_port=prediction,full_metric_defect_correction=correction,
                sampled_quadrature_difference=float(u[-1]-u[0]-prediction-correction),using_fixed_reference_derivative=True)


def read(sys,x,g,target,opts,anchor,fixed=None,fixed_prime=None):
    res,st,sh=evaluate(sys,x,g,target,opts,anchor,fixed)
    d=sys.readout(x,g,fixed)
    if fixed is not None:
        d['full_finite_tilt_port']=fixed_port(sys,x,g,st,fixed,fixed_prime)
    d.pop('exact_R655_spherical_support_difference'); d.pop('sampled_R655_spherical_dominance_margin_min')
    d.update(shell(sys,x,g,st,sh)); d['sampled_actual_whole_geometry_gate']=shell_ok(d)
    E=st['E'] if fixed is None else fixed
    desired=E[:,None]+(1-target)*g['anis']
    if desired.min()<=0:
        raise ArithmeticError('Nonpositive designed metric at the finite candidate.')
    rr=dot(st['D'],st['D'])/desired-1; ff=dot(st['D'],st['H'])/np.sqrt(desired); tt=dot(st['H'],st['H'])-1
    residual=np.abs((rr+tt)/2)+np.sqrt(((rr-tt)/2)**2+ff**2)
    ix=np.unravel_index(residual.argmax(),residual.shape)
    d.update(sampled_actual_design_eta=float(residual[ix]),sampled_design_eta_attainer=[float(g['r'][ix[0]]),float(g['phi'][ix[1]])],
             sampled_two_meridian_length_margin=sh['directional_margin'],smooth_cone_metric_norm=float(np.linalg.norm(res)),
             sampled_min_trace_det_or_axis=sh['physical_margin'],design_fraction=target,angular_budgets=len(anchor['angles']['beta']))
    return d


def center_predictor(sys):
    vec=np.zeros(sys.size); _,_,cc=sys.split(vec)
    rr=np.array([np.mean(sys.knots[i+1:i+sys.degree+1]) for i in range(sys.nb)])[2:-2]
    p,_,q=sys.profile(rr)
    wanted=np.stack((1.01*p*np.sin(q),1.01*p*np.cos(q)),axis=1)
    cc[:]=np.linalg.solve(sys.spl(rr)[:,2:-2],wanted).T
    return vec


def old_predictor(sys,record):
    # Actual paid body and centre correction, including its old signed quintic base derivative.
    vec=np.array(record['parameters'])
    if vec.size!=sys.size or sys.size!=934 or record['run']!=46138497837:
        raise ValueError('Wrong R669 source from natural completion.')
    _,_,cc=sys.split(vec)
    rr=np.array([np.mean(sys.knots[i+1:i+sys.degree+1]) for i in range(sys.nb)])[2:-2]
    t=(rr-sys.a)/(sys.b-sys.a); z=2*t-1
    cc[1]+=np.linalg.solve(sys.spl(rr)[:,2:-2],-3*.72*z*(1-z*z)**2)
    return vec


def main():
    if (os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'
            or not os.environ.get('GITHUB_RUN_ID','').isdigit()):
        raise SystemExit('Scientific execution requires public math-research-public Actions.')
    parser=argparse.ArgumentParser(); parser.add_argument('--geometry',required=True)
    parser.add_argument('--max-seconds',type=float,required=True); args=parser.parse_args()
    opts=json.loads(Path(args.geometry).read_text()); prior=json.loads(Path(opts['input_state']).read_text())
    start=time.perf_counter(); elapsed=lambda:time.perf_counter()-start
    count=Counter(); sys=ProperPhase(opts['base'],count)
    x=np.zeros(sys.size); predictor=old_predictor(sys,prior); slope=center_predictor(sys); trust=opts['initial_trust']
    frozen=None; stages=[]; accepted=0; last_level=0.; fixed_steps=0; last_guard=None
    emit('provenance',source_run=prior['run'],all_old_costs=prior['counts'],old_seconds=prior['seconds'],
         old_terminal_trust=prior['trust'],new_initial_trust=trust,old_science_replayed=False,
         old_all_parameters=prior['parameters'],new_exact_anchor_state=x.tolist(),true_tilt_sine=math.sin(sys.ang),
         source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    def fixed_on(g):
        if frozen is None:
            return None
        prior_sys,prior_x=frozen
        return prior_sys.state(prior_x,prior_sys.at(g['r'],opts['reference_azimuths']))['E']
    def obs(order,angles,level):
        gd=sys.grid(order,angles,True); f=fixed_on(gd)
        fp=None
        if frozen is not None:
            fs,fx=frozen; fst=fs.state(fx,fs.at(gd['r'],opts['reference_azimuths']),True)
            fp=2*dot(fst['D'],fst['Drr']).mean(axis=1)
        ans=read(sys,x,gd,level,opts,prepare(sys,gd,opts,opts['independent_betas']),f,fp)
        if frozen is not None:
            fs,fx=frozen; finer=fs.state(fx,fs.at(gd['r'],opts['check_reference_azimuths']))['E']
            ans['sampled_frozen_E_reference_difference']=float(np.max(abs(finer/f-1)))
        return ans
    try:
        first=obs(opts['check_order'],opts['check_angles'],0.)
        if not (first['sampled_actual_whole_geometry_gate'] and first['sampled_actual_design_eta']<1e-10):
            raise ArithmeticError('Zero R680 discrepancy or known whole geometric anchor failed independent check.')
        emit('exact_thick_anchor',actual=first,analytic_reference='R680')
        schedule=list(opts['levels'])
        for stage,level in enumerate(schedule):
            if elapsed()>args.max_seconds-opts['reserve_seconds']:
                break
            is_fixed=frozen is not None
            promoting=(stage==opts['promote_at'] or is_fixed)
            if promoting and sys.K<opts['promoted_modes']+(2 if is_fixed else 0):
                old=sys; sys=ProperPhase(dict(sys.spec,body_modes=opts['promoted_modes']+(2 if is_fixed else 0),
                                               radial_spans=2*sys.nsp if is_fixed else sys.nsp),count)
                x=extend_exactly(old,x,sys); predictor=extend_exactly(old,predictor,sys)
                slope=extend_exactly(old,slope,sys); count['exact_space_promotions']+=1
            order=opts['work_order']+(1 if promoting or sys.K>14 else 0)
            nphi=opts['work_angles']+(16 if sys.K>14 else 0)
            g=sys.grid(order,nphi); ac=prepare(sys,g,opts,opts['work_betas']); fixed=fixed_on(g)
            gg=sys.grid(opts['check_order'],opts['check_angles'],True)
            sec=prepare(sys,gg,opts,opts['work_betas']); fixed2=fixed_on(gg)
            def calc(y):
                return evaluate(sys,y,g,level,opts,ac,fixed)
            def actual_guard(y,work_st,work_sh):
                count['new_physical_guard_evaluations']+=1
                a=shell(sys,y,g,work_st,work_sh)
                if not shell_ok(a):
                    return False,a
                _,v,h=evaluate(sys,y,gg,level,opts,sec,fixed2)
                b=shell(sys,y,gg,v,h)
                return shell_ok(b),b
            res,st,sh=calc(x); delta=level-last_level
            initial_norm=float(np.linalg.norm(res)); trial_predictors=[]
            # Preserve the old scientific direction; its coefficients never replace the feasible anchor by fiat.
            if delta>0:
                for old_scale,slope_scale in opts['predictor_scales']:
                    y=x+delta*(old_scale*predictor+slope_scale*slope)
                    count['two_source_new_anchor_predictor_trials']+=1
                    try:
                        rn,sn,hn=calc(y); norm=float(np.linalg.norm(rn)); ok,gd=actual_guard(y,sn,hn)
                    except (FloatingPointError,TrialDomainError) as err:
                        count['inadmissible_predictor_domain']+=1
                        trial_predictors.append(dict(old_scale=old_scale,slope_scale=slope_scale,admissible=False,reason=str(err)))
                        continue
                    trial_predictors.append(dict(old_scale=old_scale,slope_scale=slope_scale,norm=norm,geometry=gd,admissible=ok))
                good=[d for d in trial_predictors if d['admissible'] and d['norm']<initial_norm]
                if good:
                    best=min(good,key=lambda d:d['norm']); x=x+delta*(best['old_scale']*predictor+best['slope_scale']*slope)
                    res,st,sh=calc(x); count['accepted_transported_predictors']+=1
            emit('new_design_target',stage=stage,level=level,full_columns=sys.size,initial_norm=initial_norm,
                 predictor_trials=trial_predictors,all_parameters=x.tolist(),fixed_E=is_fixed)
            trust=max(trust,opts['retarget_trust'] if delta>0 or promoting else 1.e-9)
            steps=0; outcome='iteration_limit'
            for i in range(opts['fixed_iterations'] if is_fixed else opts['iterations'][min(stage,len(opts['iterations'])-1)]):
                if elapsed()>args.max_seconds-opts['reserve_seconds']:
                    outcome='scientific_budget'; break
                J,mask=full_matrix(sys,x,g,st,sh,opts,is_fixed)
                if i==0:
                    d=np.sin(np.arange(1,sys.size+1)*.537); d/=np.linalg.norm(d)
                    val=J@d; errors=[]
                    for eps in (2e-7,5e-8):
                        fd=(calc(x+eps*d)[0]-calc(x-eps*d)[0])/(2*eps)
                        errors.append(float(np.linalg.norm(fd[mask]-val)/max(np.linalg.norm(val),1e-14)))
                    emit('new_full_derivative_check',stage=stage,columns=sys.size,relative_errors=errors)
                    if min(errors)>3e-5:
                        raise ArithmeticError('Complete R683 Jacobian disagrees with the actual residual.')
                Q,R=qr(J,mode='economic',check_finite=False,overwrite_a=True); rhs=Q.T@res[mask]
                del Q,J
                U,sv,vt=svd(R,full_matrices=False,check_finite=False); force=-(U.T@rhs)
                least=max(1e-19,5e-14*float(sv[0])**2); loss=float(res@res)
                count['full_new_QR_SVD']+=1; improved=False
                if i==0:
                    emit('complete_stage_singular_values',stage=stage,values=sv.tolist(),columns=sys.size)
                for j in range(16):
                    dx,pred,damp=trust_step(sv,vt,force,trust,least); y=x+dx
                    count['new_full_trials']+=1
                    try:
                        rn,sn,hn=calc(y); newloss=float(rn@rn); gain=(loss-newloss)/pred if pred>0 else -math.inf
                    except (FloatingPointError,TrialDomainError) as err:
                        count['inadmissible_trial_domain']+=1
                        emit('rejected_trial_domain',stage=stage,iteration=i,trial=j,trust=trust,reason=str(err))
                        trust*=.4
                        if trust<1e-10:
                            break
                        continue
                    if newloss<loss and gain>.015:
                        try:
                            ok,gate=actual_guard(y,sn,hn)
                        except (FloatingPointError,TrialDomainError) as err:
                            ok=False; count['inadmissible_independent_domain']+=1
                            emit('rejected_independent_domain',stage=stage,iteration=i,trial=j,trust=trust,reason=str(err))
                        if ok:
                            x,res,st,sh=y,rn,sn,hn; steps+=1; accepted+=1; fixed_steps+=int(is_fixed)
                            if gain>.7 and np.linalg.norm(dx)>.8*trust:
                                trust=min(1.75*trust,opts['max_trust'])
                            elif gain<.18:
                                trust*=.65
                            last_guard=gate; improved=True
                            emit('new_accepted',stage=stage,level=level,iteration=i,accepted=accepted,
                                 norm=math.sqrt(newloss),metric_norm=sh['metric_norm'],working_directional_margin=sh['directional_margin'],
                                 all_singular_extrema=[float(sv[-1]),float(sv[0])],damping=damp,gain=gain,
                                 trust=trust,geometry_independent=gate,all_parameters=x.tolist(),seconds=elapsed())
                            break
                        count['loss_reducing_steps_rejected_by_true_shell']+=1
                    trust*=.4
                    if trust<1e-10:
                        break
                if not improved:
                    outcome='no_admissible_reducing_trust_step'; break
                if np.linalg.norm(res)<opts['work_goal']:
                    outcome='work_tolerance'; break
            report=obs(opts['stage_order'],opts['stage_angles'],level)
            record=dict(stage=stage,target_fraction=level,accepted=steps,trust=trust,work_norm=float(np.linalg.norm(res)),
                        reason=outcome,fixed_E=is_fixed,independent=report)
            stages.append(record); last_level=level
            emit('new_stage_terminal',**record,all_parameters=x.tolist(),space=sys.spec,seconds=elapsed())
            if (level==1 and frozen is None and report['sampled_actual_design_eta']<=opts['freeze_metric']
                    and report['ring_closure_max']<=opts['freeze_metric'] and report['sampled_actual_whole_geometry_gate']
                    and report['sampled_two_meridian_length_margin']>=0):
                # Freeze only the actual fixed reference used by all subsequent solves and tests.
                gc=sys.grid(opts['stage_order'],opts['stage_angles'],True)
                cst=sys.state(x,sys.at(gc['r'],opts['reference_azimuths']),True)
                ec=cst['E']; ecprime=2*dot(cst['D'],cst['Drr']).mean(axis=1)
                ec2=sys.state(x,sys.at(gc['r'],opts['check_reference_azimuths']))['E']
                verify=read(sys,x,gc,1.,opts,prepare(sys,gc,opts,opts['independent_betas']),fixed=ec,fixed_prime=ecprime)
                alias=float(np.max(abs(ec2/ec-1)))
                passed=(verify['sampled_actual_design_eta']<=opts['freeze_metric'] and
                        verify['ring_closure_max']<=opts['freeze_metric'] and
                        verify['sampled_actual_whole_geometry_gate'] and verify['sampled_two_meridian_length_margin']>=0)
                emit('same_reference_gate',stage=stage,passed=passed,actual_fixed_readout=verify,
                     independent_reference_angular_difference=alias,reference_azimuths=opts['reference_azimuths'])
                if passed:
                    frozen=(sys,x.copy()); schedule[:]=schedule[:stage+1]+[1.]
                    emit('actual_reference_frozen',space=sys.spec,parameters=x.tolist(),azimuths=opts['reference_azimuths'])
        crossed={}
        for key,order,angles in [('radius_only',opts['final_order'],opts['stage_angles']),
                                 ('angle_only',opts['stage_order'],opts['final_angles']),
                                 ('both',opts['final_order'],opts['final_angles'])]:
            crossed[key]=obs(order,angles,last_level)
        emit('terminal',target_fraction_last_attempted=last_level,independent_crossed=crossed,stages=stages,
             frozen_reference=None if frozen is None else dict(space=frozen[0].spec,params=frozen[1].tolist(),
                                                           azimuths=opts['reference_azimuths']),
             all_parameters=x.tolist(),space=sys.spec,fixed_parameter_steps=fixed_steps,trust=trust,accepted=accepted,
             counts=dict(count),elapsed_seconds=elapsed(),certified_all_points=False,README_completion_claim=False)
    except Exception as exc:
        emit('incomplete',reason=str(exc),space=sys.spec,all_parameters=x.tolist(),last_level=last_level,
             last_guard=last_guard,counts=dict(count),elapsed_seconds=elapsed()); raise


if __name__=='__main__':
    main()
