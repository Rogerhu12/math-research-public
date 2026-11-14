#!/usr/bin/env python3
"""Frozen C2 metric and exact arclength ellipse for a NEW strong-target BVP.

This is an input provider, not a nonlinear solution or a reach certificate.
The selected feedback-generated prefix is frozen as quintic Hermite data.
All subsequent evaluations, including angular refinement, use that same data.
The one-pause extension matches only a finite linear m2 tail direction.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import hashlib
import json
import math
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.special import ellipe,ellipeinc

ROOT=Path(__file__).resolve().parent.parent
GX,GW=np.polynomial.legendre.leggauss(40)
GX=(GX+1)/2;GW=GW/2


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class ExactEllipse:
    """sigma has period 2*pi and |d gamma / d sigma| equals a0."""
    def __init__(self,A=1.4,B=.5):
        self.A=float(A);self.B=float(B);self.m=1-(self.B/self.A)**2
        self.E=float(ellipe(self.m));self.a0=2*self.A*self.E/math.pi

    def arc(self,theta):
        return self.A*(ellipeinc(np.asarray(theta)-math.pi/2,self.m)+self.E)

    def eccentric_angle(self,sigma):
        sigma=np.asarray(sigma,dtype=float);wrapped=np.mod(sigma,2*math.pi)
        target=self.a0*wrapped
        out=np.array([0. if t==0 else brentq(lambda x:float(self.arc(x))-t,0.,2*math.pi,
                     xtol=5e-15,rtol=9e-16) for t in target.ravel()])
        return out.reshape(sigma.shape)

    def core(self,sigma):
        theta=self.eccentric_angle(sigma);ct=np.cos(theta);st=np.sin(theta)
        z=np.zeros_like(theta)
        X=np.stack((self.A*ct,self.B*st,z),axis=-1)
        Xt=np.stack((-self.A*st,self.B*ct,z),axis=-1)
        Xtt=np.stack((-self.A*ct,-self.B*st,z),axis=-1)
        ell=np.sqrt(self.A**2*st**2+self.B**2*ct**2)
        ellt=(self.A**2-self.B**2)*st*ct/ell
        Xsig=(self.a0/ell)[...,None]*Xt
        Xsigsig=(self.a0/ell)[...,None]**2*Xtt-(self.a0**2*ellt/ell**3)[...,None]*Xt
        Xs=np.zeros_like(X);Xs[...,2]=1
        return dict(X=X,X_sigma=Xsig,X_sigma_sigma=Xsigsig,X_s=Xs,
                    X_s_sigma=np.zeros_like(X),X_ss=np.zeros_like(X),theta=theta)


def ramp(u):
    u=np.asarray(u);t=np.clip(np.minimum(u,1-u)/.08,0,1)
    velocity=3*t*t-2*t*t*t
    x=np.clip(u/.08,0,1);left=.08*(x**3-x**4/2)
    x=np.clip((1-u)/.08,0,1);right=.92-.08*(x**3-x**4/2)
    return velocity,np.where(u<.08,left,np.where(u>.92,right,u-.04))


def phase(piece,u):
    u=np.asarray(u);kind=piece['kind'];p0=piece['p0'];d=piece['p1']-p0
    if kind=='turn':
        v,I=ramp(u);return p0+d*I/.92,d*v/(.92*piece['L'])
    if kind=='brake':
        return p0+d*u*u,2*d*u/piece['L']
    if kind=='phase_bridge':
        L=piece['L'];q0=L*piece['ps0'];q1=L*piece['ps1']
        c2=3*d-2*q0-q1;c3=-2*d+q0+q1
        return p0+u*(q0+u*(c2+u*c3)),(q0+u*(2*c2+3*u*c3))/L
    return 0*u+p0,0*u


def phase_integral(piece,u,function=np.sin):
    u=float(u);cuts=[0.]
    if piece['kind']=='turn':cuts.extend(v for v in (.08,.92) if v<u)
    cuts.append(u);ans=0.
    for lo,hi in zip(cuts[:-1],cuts[1:]):
        phi,_=phase(piece,lo+(hi-lo)*GX)
        ans+=(hi-lo)*float(np.dot(function(phi),GW))
    return piece['L']*ans


def turn(p0,p1,K=7.):
    return dict(kind='turn',p0=float(p0),p1=float(p1),L=abs(p1-p0)/(K*.92),K=K)


def quintic(row0,row1,a0):
    h=row1['s']-row0['s'];y0=row0['radius']-a0;y1=row1['radius']-a0
    c0=y0;c1=h*row0['radial_speed'];c2=.5*h*h*row0['radial_acceleration']
    d=y1-c0-c1-c2;v=h*row1['radial_speed']-c1-2*c2
    acc=h*h*row1['radial_acceleration']-2*c2
    return [c0,c1,c2,10*d-4*v+acc/2,-15*d+7*v-acc,6*d-3*v+acc/2]


class Candidate:
    def __init__(self,bundle):
        self.bundle=bundle;self.ellipse=ExactEllipse(**bundle['ellipse'])
        self.a0=self.ellipse.a0;self.segments=[];s=0.;a=self.a0
        for raw in bundle['segments']:
            p=dict(raw);p['s0']=s;p['a_start']=a
            if p['kind']=='coast_to':
                p['L']=(p['radius_end']-a)/math.sin(p['p0'])
                if p['L'] < -2e-12:raise ValueError('Negative coast length')
                p['L']=max(0.,p['L'])
            if p['kind']=='hermite':a=self.a0+sum(p['coefficients'])
            else:a+=phase_integral(p,1.)
            p['s1']=s+p['L'];p['a_end']=a;s=p['s1']
            if p['L']>0:self.segments.append(p)
        self.end=s;self.breaks=np.array([0.]+[p['s1'] for p in self.segments])

    def _jet(self,p,u):
        if p['kind']=='hermite':
            c=np.array(p['coefficients']);h=p['L']
            aa=self.a0+np.polynomial.polynomial.polyval(u,c)
            v=np.polynomial.polynomial.polyval(u,np.polynomial.polynomial.polyder(c))/h
            acc=np.polynomial.polynomial.polyval(u,np.polynomial.polynomial.polyder(c,2))/(h*h)
            return aa,v,acc
        phi,ps=phase(p,u);u=np.asarray(u)
        aa=p['a_start']+np.array([phase_integral(p,t) for t in u.ravel()]).reshape(u.shape)
        return aa,np.sin(phi),np.cos(phi)*ps

    def profile(self,s):
        s=np.atleast_1d(np.asarray(s,dtype=float))
        if np.any(s < -2e-12) or np.any(s > self.end+2e-12):
            raise ValueError('Outside frozen prefix interval')
        ids=np.minimum(np.searchsorted(self.breaks,s,side='right')-1,len(self.segments)-1)
        ids=np.maximum(ids,0);out=[np.empty_like(s) for _ in range(3)]
        for j in np.unique(ids):
            mask=ids==j;p=self.segments[j];u=np.clip((s[mask]-p['s0'])/p['L'],0,1)
            vals=self._jet(p,u)
            for k in range(3):out[k][mask]=vals[k]
        return tuple(out)

    def linear_piece(self,p,y,m=2,backward=False):
        if p['kind'] in ('coast','coast_to'):
            v=math.sin(p['p0']);b=math.cos(p['p0']);a0=p['a_start'];a1=p['a_end']
            if backward:a0,a1=a1,a0
            if abs(v)<1e-14:
                t=-p['L'] if backward else p['L']
                return np.array([y[0]-m*m*t*y[1]/a0,y[1]])
            C=np.array([[-(m*m-1),-m*m*b/v],[(m*m-1)*v/b,m*m]])
            return (np.eye(2)+(a1/a0-1)*C)@y
        def rhs(u,y):
            aa,v,_=self._jet(p,np.array([u]));aa=float(aa[0]);v=float(v[0]);b=math.sqrt(1-v*v)
            return p['L']/aa*np.array([-(m*m-1)*v*y[0]-m*m*b*y[1],
                                     (m*m-1)*v*v*y[0]/b+m*m*v*y[1]])
        interval=(1,0) if backward else (0,1)
        sol=solve_ivp(rhs,interval,y,method='DOP853',rtol=2e-11,atol=2e-13,max_step=.08)
        if not sol.success:raise RuntimeError(sol.message)
        return sol.y[:,-1]

    def linear(self,y,m=2,backward=False,segments=None):
        pieces=self.segments if segments is None else segments
        for p in (reversed(pieces) if backward else pieces):y=self.linear_piece(p,np.asarray(y),m,backward)
        return y

    def metric_diagnostics(self):
        amin=math.inf;vmax=0.;accmax=0.;height=0.;jump=0.
        for j,p in enumerate(self.segments):
            u=np.linspace(0,1,81);aa,v,acc=self._jet(p,u)
            amin=min(amin,float(aa.min()));vmax=max(vmax,float(abs(v).max()));accmax=max(accmax,float(abs(acc).max()))
            if p['kind']=='hermite':
                _,vv,_=self._jet(p,GX);height+=p['L']*float(np.dot(np.sqrt(1-vv*vv),GW))
            else:height+=phase_integral(p,1.,np.cos)
            if j:
                old=self.segments[j-1]
                left=np.array([a[0] for a in self._jet(old,np.array([1.]))])
                right=np.array([a[0] for a in self._jet(p,np.array([0.]))])
                jump=max(jump,float(abs(left-right).max()))
        return dict(end=self.end,minimum_radius_sample=amin,maximum_abs_a_prime_sample=vmax,
                    maximum_abs_a_second_sample=accmax,background_height=height,maximum_jet_join_roundoff=jump,
                    cut_jet=[float(x[0]) for x in self.profile([self.end])])


def build(prefix_report,port,prefix_length=.15,lead=.05,vmid=.8,rpause=.7,K=7.,pdeep=1.568,
          bridge_length=.04,bridge_phase_add=.025):
    source=json.loads(Path(prefix_report).read_text());tail=json.loads(Path(port).read_text())
    knots=[r for r in source['metric_knots'] if r['s']<=prefix_length+1e-13]
    knots=list({r['s']:r for r in knots}.values());knots.sort(key=lambda r:r['s'])
    if abs(knots[-1]['s']-prefix_length)>1e-12:raise ValueError('Prefix length is not a saved knot')
    a0=source['metric_a0'];segments=[]
    if lead:segments.append(dict(kind='coast',p0=0.,p1=0.,L=lead,label='central_cylinder'))
    for k0,k1 in zip(knots[:-1],knots[1:]):
        segments.append(dict(kind='hermite',L=k1['s']-k0['s'],coefficients=quintic(k0,k1,a0),
                             label='frozen_feedback_prefix'))
    end=knots[-1];p0=math.asin(end['radial_speed']);ps0=end['radial_acceleration']/math.cos(p0)
    pp=p0+bridge_phase_add
    segments.append(dict(kind='phase_bridge',p0=p0,p1=pp,ps0=ps0,ps1=0.,L=bridge_length,label='freeze_to_turn'))
    pm=-math.asin(vmid);segments.append(turn(pp,pm,K))
    prebrake=turn(pm,0.,K)
    segments.append(dict(kind='coast_to',p0=pm,p1=pm,radius_end=rpause-phase_integral(prebrake,1.)))
    segments.append(prebrake)
    pause_index=len(segments)
    segments.append(dict(kind='coast',p0=0.,p1=0.,L=0.,label='linear_m2_pause'))
    segments.append(turn(0.,-pdeep,K))
    rc=tail['cut']['r'];wc=tail['cut']['w'];wr=tail['cut']['wr']
    pt=-math.atan2(1.,wc);ps=-wr/(1+wc*wc)**1.5
    brake=dict(kind='brake',p0=-pdeep,p1=pt,L=2*(pt+pdeep)/ps,label='cut_second_jet_brake')
    segments.append(dict(kind='coast_to',p0=-pdeep,p1=-pdeep,radius_end=rc-phase_integral(brake,1.)))
    segments.append(brake)
    bundle=dict(schema='fd2d-frozen-ellipse-metric-v1',ellipse=dict(A=1.4,B=.5),
        exact_a0_definition='2*A*complete_elliptic_E(1-(B/A)^2)/pi',segments=segments,
        generated_by=Path(__file__).name,generator_sha256=digest(__file__),
        inputs=dict(prefix_report=Path(prefix_report).name,prefix_report_sha256=digest(prefix_report),
                    tail_port=Path(port).name,tail_port_sha256=digest(port),tail_config_sha256=tail['config_sha256']),
        design_parameters=dict(prefix_length=prefix_length,lead=lead,vmid=vmid,rpause=rpause,K=K,
                               pdeep=pdeep,bridge_length=bridge_length,bridge_phase_add=bridge_phase_add),
        status=dict(metric_frozen=True,nonlinear_prefix_solved=False,nonlinear_tail_matched=False,
                    closed_surface=False,reach_certified=False,strong_target_complete=False))
    trial=Candidate(bundle)
    # Locate the pause interface by its preceding segment label-independent
    # construction index; the zero-length pause itself is omitted by Candidate.
    pre_count=pause_index;before=trial.segments[:pre_count];after=trial.segments[pre_count:]
    y0=trial.linear([1.,0.],segments=before)
    D=next(r['slope'] for r in tail['rows'] if r['mode']==2)
    terminal=np.array([-wc*(rc*D-4)/3,1.]);target=trial.linear(terminal,backward=True,segments=after)
    denom=(4/rpause)*y0[1]*target[1]
    pause=float((y0[0]*target[1]-y0[1]*target[0])/denom)
    if not math.isfinite(pause) or pause<0:raise ValueError(f'Nonpositive finite m2 pause: {pause}')
    bundle['segments'][pause_index]['L']=pause
    bundle['linear_m2_seed']=dict(pause=pause,before_pause=y0.tolist(),backward_at_pause=target.tolist(),
        terminal_direction=terminal.tolist(),terminal_height_gain=float(y0[1]/target[1]),
        matching_definition='T=(f0*G-g0*F)/((4/a_pause)*g0*G)',
        scope='Finite m2 linear direction only; higher modes and exact ellipse nonlinear closure remain unsolved.')
    obj=Candidate(bundle);bundle['metric_diagnostics']=obj.metric_diagnostics()
    bundle['metric_diagnostics']['background_height_with_tail']=bundle['metric_diagnostics']['background_height']+tail['stats']['heightSpan']
    forward=obj.linear([1.,0.]);backward=obj.linear(terminal,backward=True)
    bundle['linear_m2_seed']['forward_terminal']=forward.tolist()
    bundle['linear_m2_seed']['backward_core']=backward.tolist()
    bundle['linear_m2_seed']['normalized_forward_direction_residual']=float((forward[0]*terminal[1]-forward[1]*terminal[0])/(np.linalg.norm(forward)*np.linalg.norm(terminal)))
    bundle['linear_m2_seed']['normalized_backward_core_residual']=float(backward[1]/np.linalg.norm(backward))
    bundle['cut']=dict(r=rc,w=wc,wr=wr,a_prime=-1/math.sqrt(1+wc*wc),
        a_second=-wc*wr/(1+wc*wc)**2,z_prime=wc/math.sqrt(1+wc*wc),
        physical_upper_background_height_r_sign=-1,
        linear_slopes={str(r['mode']):r['slope'] for r in tail['rows']},
        cuff_radius=tail['stats']['rCuff'],tail_height_span=tail['stats']['heightSpan'])
    return bundle


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--prefix-report',type=Path,default=ROOT/'notes/2026-11-12-fd2d-ellipse-b05-filtered-n256.json')
    p.add_argument('--port',type=Path,default=ROOT/'notes/2026-11-12-fd2d-ellipse-cuff032-cut04-port.json')
    p.add_argument('--out',type=Path,required=True);p.add_argument('--scan',action='store_true')
    p.add_argument('--prefix-length',type=float,default=.15);p.add_argument('--lead',type=float,default=.05)
    p.add_argument('--v-mid',type=float,default=.8);p.add_argument('--pause-radius',type=float,default=.7)
    p.add_argument('--deep-phase',type=float,default=1.568)
    args=p.parse_args()
    if args.scan:
        report=dict(scope=__doc__,rows=[])
        for prefix_length,lead in [(.15,.05),(.2,.08),(.25,.125)]:
            for vmid in [.65,.8,.9]:
                for rpause in [.65,.7,.75]:
                    pars=dict(prefix_length=prefix_length,lead=lead,vmid=vmid,rpause=rpause)
                    try:
                        b=build(args.prefix_report,args.port,**pars)
                        row=dict(parameters=pars,metric=b['metric_diagnostics'],linear=b['linear_m2_seed'])
                    except Exception as exc:row=dict(parameters=pars,error=str(exc))
                    report['rows'].append(row);args.out.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(dict(event='complete',trials=len(report['rows']),successful=sum('error' not in r for r in report['rows']))))
    else:
        b=build(args.prefix_report,args.port,prefix_length=args.prefix_length,lead=args.lead,
                vmid=args.v_mid,rpause=args.pause_radius,pdeep=args.deep_phase)
        args.out.write_text(json.dumps(b,indent=2)+'\n')
        print(json.dumps(dict(event='frozen_candidate_written',path=str(args.out),metric=b['metric_diagnostics'],linear=b['linear_m2_seed'])))


if __name__=='__main__':main()
