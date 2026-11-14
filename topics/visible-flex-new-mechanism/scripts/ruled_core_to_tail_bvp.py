#!/usr/bin/env python3
"""Fixed-metric R44 saddle inlet to the exact R128 flat-tail port.

Nonlinear solves are intended for this public repository's GitHub Actions.
--check-only evaluates the reference, boundary jets and optional Jacobian without
calling an optimizer. This is a finite BVP candidate, not a closed-surface proof.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time
from types import SimpleNamespace

import numpy as np
from numpy.polynomial import polynomial as poly
from scipy.interpolate import BSpline
from scipy.optimize import brentq, least_squares

from core_to_tail_bvp import HCOEF, Problem, UnitMeridian
from ruled_core_geometry import RuledCore


class LocalizedRuledMeridian(UnitMeridian):
    """An exact-core metric segment, a localized join, and an open plane collar.

    The radius is the integral of cos(beta); the final constant control is chosen
    for the radius closure once, before solving for the spatial field. All
    reference data are then fixed. Quadrature is split at every formula join.
    """
    def __init__(self,core,args):
        self.core=core
        self.start=args.inlet_s
        self.length=args.length
        self.center=np.zeros(3)
        self.a0=float(core.metric(self.start)[0])
        self.exact=args.core_exact_length
        self.blend=args.core_blend_length
        self.patch_end=self.exact+self.blend
        self.flat=args.reference_flat_length
        self.active=self.length-self.flat
        self.cut_radius=args.cut_radius
        self.wiggle=args.beta_wiggle
        self.gl,self.gw=np.polynomial.legendre.leggauss(args.quadrature)
        if not (0<self.exact and 0<self.blend and self.patch_end<self.active<self.length):
            raise ValueError('Need 0 < exact, blend and exact+blend < length-flat < length')
        slope=float(core.metric(self.start+self.patch_end)[1])
        if abs(slope)>=1:
            raise ValueError('The accurate core angle must satisfy |a_prime| < 1 throughout the local patch')
        self.template=HCOEF[3]*(np.pi/2)
        self.template[0]+=np.pi/2
        self.bump=np.array([0.,0.,0.,64.,-192.,192.,-64.])
        wave=poly.polymul(self.bump,[-1.,2.])*(343*np.sqrt(7)/216)
        self.template=np.r_[self.template,0.,0.]+self.wiggle*wave
        self.bump=np.r_[self.bump,0.]
        self.control=0.
        def closure(value):
            self.control=value
            return float(self.evaluate(np.array([1.]))[0][0][0]-self.cut_radius)
        if args.reference_control is None:
            scan=np.linspace(-6,6,121)
            values=[closure(value) for value in scan]
            brackets=[(lo,hi) for lo,hi,flo,fhi in zip(scan[:-1],scan[1:],values[:-1],values[1:])
                      if flo*fhi<=0]
            if not brackets:
                raise ValueError('Localized ruled reference has no closure bracket in [-6,6]')
            lo,hi=min(brackets,key=lambda pair:abs(sum(pair)))
            self.control=brentq(closure,lo,hi,xtol=2e-14)
            self.control_bracket=[float(lo),float(hi)]
        else:
            self.control=float(args.reference_control)
            self.control_bracket=None
        self.closure_error=float(self.evaluate(np.array([1.]))[0][0][0]-self.cut_radius)
        if abs(self.closure_error)>2e-11:
            raise ValueError(f'Fixed reference control does not close the radius: {self.closure_error}')

    def core_beta(self,t,derivative=0):
        t=np.minimum(np.asarray(t),self.patch_end)
        ss=self.start+t
        aa,ap,app=self.core.metric(ss)
        appp=-3*self.core.q*self.core.scale**2*ss/(self.core.scale**2+ss*ss)**2.5
        zz=np.sqrt(1-ap*ap)
        if derivative==0:
            return np.arccos(ap)
        if derivative==1:
            return -app/zz
        if derivative==2:
            return -appp/zz-ap*app*app/zz**3
        raise ValueError('Need beta derivative 0, 1 or 2')

    def template_beta(self,t,derivative=0):
        t=np.asarray(t)
        u=np.clip(t/self.active,0.,1.)
        answer=poly.polyval(u,poly.polyder(self.template+self.control*self.bump,derivative))/self.active**derivative
        return np.where(t>=self.active,np.pi if derivative==0 else 0.,answer)

    def weight(self,t,derivative=0):
        z=(np.asarray(t)-self.exact)/self.blend
        value=poly.polyval(np.clip(z,0.,1.),poly.polyder(HCOEF[3],derivative))/self.blend**derivative
        if derivative==0:
            return np.where(z<=0.,1.,np.where(z>=1.,0.,1-value))
        return np.where((z>0.)&(z<1.),-value,0.)

    def physical_beta(self,t,derivative=0):
        core=[self.core_beta(t,d) for d in range(derivative+1)]
        base=[self.template_beta(t,d) for d in range(derivative+1)]
        ww=[self.weight(t,d) for d in range(derivative+1)]
        answer=ww[0]*core[derivative]+(1-ww[0])*base[derivative]
        if derivative>=1:
            answer+=derivative*ww[1]*(core[derivative-1]-base[derivative-1])
        if derivative==2:
            answer+=ww[2]*(core[0]-base[0])
        return answer

    def beta(self,u,derivative=0):
        return self.physical_beta(np.asarray(u)*self.length,derivative)*self.length**derivative

    def evaluate(self,u):
        t=np.asarray(u)*self.length
        ia=np.zeros_like(t,dtype=float)
        iz=np.zeros_like(t,dtype=float)
        for left,right in ((0.,self.exact),(self.exact,self.patch_end),(self.patch_end,self.active)):
            width=np.maximum(np.minimum(t,right)-left,0.)
            nodes=left+width[:,None]*(self.gl[None,:]+1)/2
            beta=self.physical_beta(nodes)
            ia+=width/2*(np.cos(beta)@self.gw)
            iz+=width/2*(np.sin(beta)@self.gw)
        ia-=np.maximum(t-self.active,0.)
        beta=self.physical_beta(t)
        bp=self.physical_beta(t,1)
        aa=[self.a0+ia,np.cos(beta),-np.sin(beta)*bp]
        zz=[iz,np.sin(beta),np.cos(beta)*bp]
        local=t<=self.exact
        exact=self.core.metric(self.start+t)
        for d in range(3):
            aa[d]=np.where(local,exact[d],aa[d])
        for d in (1,2):
            aa[d]=np.where(t>=self.active,-1. if d==1 else 0.,aa[d])
            zz[d]=np.where(t>=self.active,0.,zz[d])
        return aa,zz

    def identity(self):
        return {'family':'localized_R44_beta_with_open_flat_collar_v1',
                'ruled_scale':self.core.scale,'core_cut_s':self.start,
                'length':self.length,'core_exact_length':self.exact,
                'core_blend_length':self.blend,'reference_flat_length':self.flat,
                'cut_radius':self.cut_radius,'beta_wiggle':self.wiggle,
                'control':float(self.control),'quadrature':len(self.gl),
                'coordinate':'rotation0_tail_sin_minus_cos',
                'metric_controls':False}

    def reference_audit(self):
        report=self.diagnostics()
        aa,zz=self.evaluate(np.linspace(0,1,1001))
        for key in ('diameter_box_upper','sample_curvature_times_003_diameter_box',
                    'sample_min_normal_chord_radius_over_diameter_box'):
            report.pop(key,None)
        intrinsic=np.abs(aa[2]/aa[0])
        report.update(radius_closure_error=self.closure_error,
                      reference_control_bracket=self.control_bracket,
                      exact_core_metric_interval=[self.start,self.start+self.exact],
                      open_flat_collar_length=self.flat,
                      reference_tail_height=float(zz[0][-1]),
                      reference_mirror_ball_radius_sample=float(np.max(np.hypot(aa[0],zz[0]))),
                      fixed_metric_abs_Gauss_curvature_sample_max=float(intrinsic.max()),
                      necessary_reach_upper_from_sample_Gauss_curvature=float(1/np.sqrt(intrinsic.max())),
                      reference_does_not_certify_actual_ruled_connector=True)
        return report


class RuledTailProblem(Problem):
    def __init__(self,args):
        self.ruled_core=RuledCore(args.ruled_scale,rotation=0.)
        self.cut_s=args.inlet_s
        a0,ap0,app0=map(float,self.ruled_core.metric(self.cut_s))
        placeholder=vars(args).copy()
        placeholder.update(core_profile='ellipse',ellipse_major=a0,ellipse_minor=a0,
                           inlet_s=0.,background='hermite',design_metric=False,angular_basis='material')
        super().__init__(SimpleNamespace(**placeholder))
        self.args=args
        self.core_profile='ruled'
        self.angular_basis='material'
        self.a0,self.ap0,self.app0=a0,ap0,app0
        theta=np.arange(args.inlet_angles)*2*np.pi/args.inlet_angles
        self.inlet=self.ruled_core.inlet(theta,self.cut_s).transpose(0,2,1)
        self.inlet_solver={'method':'analytic_R44_finite_Fourier_and_elliptic_material_gauge',
                           'rotation':0.,'no_GC_integration':True}
        self.inlet_report=self.ruled_core.identity(self.cut_s)
        self.reference=LocalizedRuledMeridian(self.ruled_core,args)
        if self.J>=3:
            first=self.reference.exact/args.length
            second=self.reference.patch_end/args.length
            inside=np.r_[first,second,np.linspace(second,1.,self.J)[1:-1]]
            self.knots=np.r_[np.zeros(6),inside,np.ones(6)]
            self.spline=BSpline(self.knots,np.eye(self.J+6),5)

    def prepare(self,radial,angular):
        grid=super().prepare(radial,angular)
        # Replace the base class's unused periodic interpolant at every grid.
        grid['inlet']=[self.ruled_core.inlet(grid['theta'],self.cut_s,d) for d in range(3)]
        return grid


def warm_seed(problem,previous):
    old_identity=previous.get('fixed_metric_identity')
    if old_identity!=problem.reference.identity():
        raise ValueError('Warm candidate changes the fixed complete metric or its evaluation convention')
    if previous.get('discretization',{}).get('angular_basis')!='material':
        raise ValueError('Warm candidate has an incompatible angular basis')
    oldj=previous['discretization']['radial_free']
    oldk=2*previous['discretization']['modes']+1
    old=np.asarray(previous['coefficients'])
    oldxyz=old[:3*oldj*oldk].reshape(3,oldj,oldk)
    oldknots=np.asarray(previous['discretization']['radial_knots'])
    sample=np.linspace(0,1,max(101,8*(oldj+problem.J)))
    oldr=BSpline(oldknots,np.eye(oldj+6),5)(sample)[:,3:-3]
    transfer=np.linalg.lstsq(problem.radial(sample),oldr,rcond=None)[0]
    cc=np.zeros((3,problem.J,problem.K))
    keep=min(oldk,problem.K)
    cc[:,:,:keep]=np.einsum('ij,cjk->cik',transfer,oldxyz[:,:,:keep])
    seed=problem.seed()
    seed[:problem.np]=cc.ravel()
    seed[-4:]=old[-4:]
    return seed


def port_checks(problem,z,check_jacobian=False):
    grid=problem.prepare(np.linspace(0,1,15),64)
    geometry=problem.geometry(z,grid,True)
    tail=problem.tail(grid['theta'],z[-4:])
    errors={}
    for name,rd,td in [('x',0,0),('xs',1,0),('xt',0,1),
                       ('xss',2,0),('xst',1,1),('xtt',0,2)]:
        target=np.stack((grid['inlet'][td][rd],tail[td][rd]))
        errors[name]=float(np.max(np.abs(geometry[name][[0,-1]]-target)))
    rr=problem.reference
    starts=rr.evaluate(np.array([0.]))[0]
    ends=rr.evaluate(np.array([1.]))[0]
    start_errors=[float(starts[d][0]-problem.ruled_core.metric(problem.cut_s)[d]) for d in range(3)]
    end_errors=[float(ends[d][0]-value) for d,value in enumerate([problem.args.cut_radius,-1.,0.])]
    t=np.linspace(0,rr.exact,17)
    exact_metric=problem.ruled_core.metric(problem.cut_s+t)
    actual=rr.evaluate(t/rr.length)[0]
    core_metric_errors=[float(np.max(np.abs(actual[d]-exact_metric[d]))) for d in range(3)]
    positions=np.array([.003,.007,.013,.027,.043,.071,.19,.43,.71,.91])*rr.length
    h=2e-6*rr.length
    derivative_checks=[]
    for component in range(2):
        for order in (0,1):
            num=(rr.evaluate((positions-2*h)/rr.length)[component][order]
                 -8*rr.evaluate((positions-h)/rr.length)[component][order]
                 +8*rr.evaluate((positions+h)/rr.length)[component][order]
                 -rr.evaluate((positions+2*h)/rr.length)[component][order])/(12*h)
            exact=rr.evaluate(positions/rr.length)[component][order+1]
            derivative_checks.append({'component':'radius' if component==0 else 'height',
                'derivative':order+1,'absolute_error':float(np.max(np.abs(num-exact))),
                'relative_l2_error':float(np.linalg.norm(num-exact)/max(np.linalg.norm(exact),1e-30))})
    jac_error=None
    if check_jacobian:
        rng=np.random.default_rng(62731)
        zz=z.copy()
        zz[:problem.np]+=rng.normal(size=problem.np)*.0003
        direction=rng.normal(size=problem.size)
        direction/=np.linalg.norm(direction)
        eps=2e-6
        num=(problem.residual(zz+eps*direction,grid)-problem.residual(zz-eps*direction,grid))/(2*eps)
        jac_error=float(np.linalg.norm(num-problem.jacobian(zz,grid)@direction)/max(np.linalg.norm(num),1e-30))
    checks={'complete_position_second_jet_endpoint_errors':errors,
            'metric_start_second_jet_errors':start_errors,'metric_end_second_jet_errors':end_errors,
            'exact_core_metric_segment_errors':core_metric_errors,
            'independent_reference_derivative_checks':derivative_checks,
            'jacobian_directional_relative_error':jac_error,
            'metric_unknown_count':problem.na}
    checks['passed']=(max(errors.values())<1e-11 and max(map(abs,start_errors+end_errors))<2e-11
                      and max(core_metric_errors)<1e-12 and problem.na==0
                      and max(x['relative_l2_error'] for x in derivative_checks)<1e-7
                      and (jac_error is None or jac_error<2e-7))
    return checks


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--ruled-scale',type=float,default=.24)
    p.add_argument('--inlet-s',type=float,default=.012)
    p.add_argument('--core-exact-length',type=float,default=.01)
    p.add_argument('--core-blend-length',type=float,default=.04)
    p.add_argument('--reference-flat-length',type=float,default=.03)
    p.add_argument('--reference-control',type=float)
    p.add_argument('--length',type=float,default=1.)
    p.add_argument('--beta-wiggle',type=float,default=.8)
    p.add_argument('--cut-radius',type=float,default=.28)
    p.add_argument('--flat-start',type=float,default=.26)
    p.add_argument('--cuff-radius',type=float,default=.23)
    p.add_argument('--tail-plus',type=float,default=0.)
    p.add_argument('--tail-minus',type=float,default=0.)
    p.add_argument('--tail-angle-max',type=float,default=.1)
    p.add_argument('--tail-height',type=float)
    p.add_argument('--tail-height-min',type=float,default=.1)
    p.add_argument('--tail-height-max',type=float,default=1.2)
    p.add_argument('--radius-floor',type=float,default=.24)
    p.add_argument('--radius-ceiling',type=float,default=1.1)
    p.add_argument('--radius-weight',type=float,default=20.)
    p.add_argument('--quadrature',type=int,default=64)
    p.add_argument('--radial-free',type=int,default=5)
    p.add_argument('--modes',type=int,default=8)
    p.add_argument('--angular',type=int,default=64)
    p.add_argument('--radial-gauss',type=int,default=5)
    p.add_argument('--inlet-angles',type=int,default=192)
    p.add_argument('--max-nfev',type=int,default=150)
    p.add_argument('--warm',type=Path)
    p.add_argument('--check-only',action='store_true')
    p.add_argument('--check-jacobian',action='store_true')
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    if not 0<args.cuff_radius<args.flat_start<args.cut_radius:
        p.error('Need cuff < flat-start < cut-radius')
    if args.ruled_scale<=0 or args.inlet_s<0 or args.inlet_s>args.ruled_scale/20+1e-14:
        p.error('Use the proved R44 central strip: 0 <= inlet-s <= ruled-scale/20')
    if args.radial_free<1 or args.modes<1 or args.angular<4*args.modes+4:
        p.error('Need positive radial/mode counts and angular >= 4*modes+4')
    args.design_metric=False
    previous=json.loads(args.warm.read_text()) if args.warm else None
    if previous and args.reference_control is None:
        args.reference_control=previous['fixed_metric_identity']['control']
    start=time.perf_counter()
    problem=RuledTailProblem(args)
    identity=problem.reference.identity()
    ref=problem.reference.reference_audit()
    if ref['radius_range'][0]<=0:
        p.error('The fixed reference radius is not positive')
    seed=warm_seed(problem,previous) if previous else problem.seed()
    low=np.full(problem.size,-4.)
    high=np.full(problem.size,4.)
    low[-4:]=[-args.tail_angle_max,-args.tail_angle_max,-.6,args.tail_height_min]
    high[-4:]=[args.tail_angle_max,args.tail_angle_max,.6,args.tail_height_max]
    seed=np.clip(seed,low+1e-10,high-1e-10)
    gl,_=np.polynomial.legendre.leggauss(args.radial_gauss)
    breaks=np.unique(np.r_[problem.knots,
                          problem.reference.exact/args.length,problem.reference.patch_end/args.length,
                          problem.reference.active/args.length])
    radial=np.concatenate([lo+(hi-lo)*(gl+1)/2 for lo,hi in zip(breaks[:-1],breaks[1:])])
    grid=problem.prepare(radial,args.angular)
    checks=port_checks(problem,seed,args.check_jacobian)
    if not checks['passed']:
        raise RuntimeError(f'Port implementation checks failed: {checks}')
    initial=problem.residual(seed,grid)
    if args.check_only:
        answer=seed
        solver={'performed':False,'reason':'check_only_no_optimization'}
    else:
        progress={'last':time.perf_counter(),'calls':0}
        def fun(zz):
            value=problem.residual(zz,grid)
            progress['calls']+=1
            if time.perf_counter()-progress['last']>15:
                print(json.dumps({'event':'iterate','calls':progress['calls'],
                                  'rms':float(np.sqrt(np.mean(value*value))),
                                  'tail':zz[-4:].tolist()}),flush=True)
                progress['last']=time.perf_counter()
            return value
        fit=least_squares(fun,seed,jac=lambda zz:problem.jacobian(zz,grid),bounds=(low,high),
                          max_nfev=args.max_nfev,x_scale='jac',ftol=2e-10,xtol=2e-10,gtol=2e-10)
        answer=fit.x
        final=problem.residual(answer,grid)
        solver={'performed':True,'success':bool(fit.success),'status':fit.status,'message':fit.message,
                'nfev':fit.nfev,'njev':fit.njev,'optimality':float(fit.optimality),
                'initial_rms':float(np.sqrt(np.mean(initial*initial))),
                'final_rms':float(np.sqrt(np.mean(final*final)))}
    payload={'status':'fixed_metric_R44_core_tail_finite_BVP_not_a_closed_surface',
             'task_complete':False,'closed_surface':False,'exact_isometry_proved':False,
             'fixed_complete_metric':True,'fixed_metric_identity':identity,
             'definition':{'core_profile':'ruled','ruled_scale':args.ruled_scale,'inlet_s':args.inlet_s,
                           'central_exact_core_half_width':args.inlet_s,'rotation':0.,
                           'halfturn':'diag(-1,1,-1)','design_metric':False,
                           'tail_cut_radius':args.cut_radius,'tail_flat_start':args.flat_start,
                           'tail_cuff_radius':args.cuff_radius,'tail_height_bounds':[args.tail_height_min,args.tail_height_max],
                           'tail_final':dict(zip(('A_plus','A_minus','C_y','C_z'),answer[-4:].tolist()))},
             'discretization':{'radial_free':args.radial_free,'modes':args.modes,'angular_basis':'material',
                               'angular':args.angular,'radial_gauss':args.radial_gauss,
                               'inlet_angles':args.inlet_angles,'tail_quadrature':args.quadrature,
                               'unknowns':problem.size,'metric_unknowns':problem.na,
                               'radial_knots':problem.knots.tolist(),
                               'radial_collocation_count':len(radial),'residuals':len(initial)},
             'inlet':problem.inlet_report,'reference_geometry':ref,'port_checks':checks,
             'solver':solver,'audits':[problem.audit(answer,41,128),problem.audit(answer,81,256)],
             'coefficients':answer.tolist(),'elapsed_seconds':time.perf_counter()-start,
             'limitations':['The fixed reference control is recorded; quadrature and radius closure are numerical, not interval certificates.',
                            'The actual spatial connector is pinned only by its complete two jets; the exact reference metric segment is not a pinned R44 position segment.',
                            'A low finite residual alone does not prove a convergent isometry, embeddedness or reach.',
                            'The static R44 core has no certified task-scale Hausdorff displacement.'],
             'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'base_solver_sha256':hashlib.sha256(Path(__file__).with_name('core_to_tail_bvp.py').read_bytes()).hexdigest(),
             'core_geometry_sha256':hashlib.sha256(Path(__file__).with_name('ruled_core_geometry.py').read_bytes()).hexdigest()}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(payload,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'out':str(args.out),'performed_solve':solver['performed'],
                      'fixed_metric_identity':identity,'port_checks':checks,
                      'fine_metric':payload['audits'][-1]['relative_metric_operator_sample_max'],
                      'reference':ref,'elapsed_seconds':payload['elapsed_seconds']}),flush=True)


if __name__=='__main__':
    main()
