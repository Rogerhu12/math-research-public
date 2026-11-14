#!/usr/bin/env python3
"""Pinned noncircular coaxial collars through folded, optionally plateau, bands.

Actual optimization runs only in this public repository's GitHub Actions.
--smoke-only performs a small development audit and optional Jacobian check.
The circular reference audit is recorded separately and never inherited as a
geometry certificate for the nonaxisymmetric BVP output.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np
from scipy.optimize import least_squares
from scipy.special import ellipe, ellipeinc
from scipy.interpolate import BSpline

from eccentric_collar_search import Meridian, TrialSpace, fourier, smoothstep
from eccentric_curvature_search import FrozenCurvatureProblem
from unit_tangent_collar_search import UnitTangentSpace, SignedFrenetSpace


class PlateauMeridian(Meridian):
    """Two C2 folded transitions and an exact open vertical cylindrical core."""
    def __init__(self,radius=.8,length=3.,collar=.06,wiggle=2.4,quad=96,plateau=.15):
        if not (radius>0 and length>0 and 0<collar<.25 and 0<plateau<.5-collar):
            raise ValueError('invalid plateau meridian')
        self.radius,self.length,self.collar,self.wiggle=map(float,[radius,length,collar,wiggle])
        self.plateau=float(plateau)
        self.start,self.end=length*collar,length*(1-collar)
        self.core_left,self.core_right=length*(.5-plateau),length*(.5+plateau)
        self.transition_width=self.core_left-self.start
        self.nodes,self.weights=np.polynomial.legendre.leggauss(quad)
        self.height=2*self._integrals(np.array([length/2]))[0,1]
    def beta(self,s):
        s=np.asarray(s)
        reflected=np.minimum(s,self.length-s)
        value,d1,d2=smoothstep((reflected-self.start)/self.transition_width)
        v,vp,vpp=value/2,d1/(2*self.transition_width),d2/(2*self.transition_width**2)
        half=np.pi*v+self.wiggle*np.sin(2*np.pi*v)
        factor=np.pi+2*np.pi*self.wiggle*np.cos(2*np.pi*v)
        first=factor*vp
        second=factor*vpp-4*np.pi**2*self.wiggle*np.sin(2*np.pi*v)*vp*vp
        return np.where(s<=self.length/2,half,np.pi-half),first,np.where(s<=self.length/2,second,-second)
    def _integrals(self,s):
        s=np.asarray(s,float).reshape(-1)
        stop=np.clip(s,self.start,self.core_left)
        half=(stop-self.start)/2
        points=self.start+half[:,None]*(1+self.nodes[None,:])
        beta=self.beta(points)[0]
        radial=np.minimum(s,self.start)+half*(np.cos(beta)@self.weights)
        height=half*(np.sin(beta)@self.weights)+np.maximum(s-self.core_left,0.)
        return np.column_stack((radial,height))
    def identity(self):
        return {'formula':'left beta=pi*v+b*sin(2*pi*v), v=S5((s-cL)/(L*(.5-p-c)))/2; central beta=pi/2; right beta(s)=pi-beta(L-s)',
                'profile_family':'half_smoothstep_with_central_plateau',
                'initial_radius':self.radius,'length':self.length,'collar_fraction':self.collar,
                'beta_wiggle':self.wiggle,'central_half_plateau_fraction':self.plateau,
                'quadrature_order':len(self.nodes),'reference_height':float(self.height)}


def make_meridian(args):
    if args.plateau:
        return PlateauMeridian(args.radius,args.length,args.collar,args.beta_wiggle,args.quadrature,args.plateau)
    return Meridian(args.radius,args.length,args.collar,args.beta_wiggle,args.quadrature)


def core_curve(u,args):
    """One fixed closed unit-mean-radius curve, with exact material jets.

    The mixed support curve is translated once by its analytical material
    centroid. No evolving section is recentered; all center modes stay free.
    """
    u=np.asarray(u)
    phi=u.copy()
    if args.core_shape=='curvature':
        A,B=args.seed2,args.seed3
        for _ in range(35):
            rho=1+A*np.cos(2*phi)+B*np.cos(3*phi)
            correction=(phi+A*np.sin(2*phi)/2+B*np.sin(3*phi)/3-u)/rho
            phi-=correction
            if np.max(abs(correction))<2e-15: break
        rho=1+A*np.cos(2*phi)+B*np.cos(3*phi)
        h=1-A*np.cos(2*phi)/3-B*np.cos(3*phi)/8
        hp=2*A*np.sin(2*phi)/3+3*B*np.sin(3*phi)/8
        x=h*np.cos(phi)-hp*np.sin(phi)+A*B/24
        y=h*np.sin(phi)+hp*np.cos(phi)
        tangent=np.stack((-np.sin(phi),np.cos(phi),np.zeros_like(phi)),axis=-1)
        normal=np.stack((-np.cos(phi),-np.sin(phi),np.zeros_like(phi)),axis=-1)
        angle_delta=phi-u
        kappa=1/rho
    else:
        A,B=args.ellipse_major,args.ellipse_minor
        modulus=1-(B/A)**2
        complete=ellipe(modulus)
        mean_radius=2*A*complete/np.pi
        for _ in range(35):
            speed=np.sqrt(A*A*np.sin(phi)**2+B*B*np.cos(phi)**2)
            length=A*(ellipeinc(phi-np.pi/2,modulus)+complete)
            correction=(length-mean_radius*u)/speed
            phi-=correction
            if np.max(abs(correction))<2e-15: break
        speed=np.sqrt(A*A*np.sin(phi)**2+B*B*np.cos(phi)**2)
        x,y=A*np.cos(phi)/mean_radius,B*np.sin(phi)/mean_radius
        tangent=np.stack((-A*np.sin(phi)/speed,B*np.cos(phi)/speed,np.zeros_like(phi)),axis=-1)
        normal=np.stack((-B*np.cos(phi)/speed,-A*np.sin(phi)/speed,np.zeros_like(phi)),axis=-1)
        kappa=A*B*mean_radius/speed**3
        theta=np.arctan2(-tangent[:,0],tangent[:,1])
        angle_delta=np.arctan2(np.sin(theta-u),np.cos(theta-u))
    gamma=np.stack((x,y,np.zeros_like(phi)),axis=-1)
    return {'gamma':gamma,'du':tangent,'duu':kappa[:,None]*normal,
            'angle_delta':angle_delta,'angle_u':kappa,'curvature':kappa}


def core_bridge_and_mask(s,meridian):
    s=np.asarray(s)
    mid=meridian.length/2
    if hasattr(meridian,'plateau'):
        left,right=meridian.core_left,meridian.core_right
        reflected=np.minimum(s,meridian.length-s)
        B,Bp,Bpp=smoothstep((reflected-meridian.start)/meridian.transition_width)
        Bp*=np.where(s<=mid,1.,-1.)/meridian.transition_width
        Bpp/=meridian.transition_width**2
        v=np.where(s<left,(s-left)/mid,np.where(s>right,(s-right)/mid,0.))
        eta=v**3
        etap=np.where((s<left)|(s>right),3*v*v/mid,0.)
        etapp=np.where((s<left)|(s>right),6*v/mid**2,0.)
    else:
        width=meridian.end-meridian.start
        x=np.clip((s-meridian.start)/width,0,1)
        B=64*x**3*(1-x)**3
        Bp=192*x*x*(1-x)**2*(1-2*x)/width
        Bpp=384*x*(1-x)*(1-5*x+5*x*x)/width**2
        v=(s-mid)/mid
        eta,etap,etapp=v*v,2*v/mid,np.full_like(v,2/mid**2)
    return (B,Bp,Bpp),(eta,etap,etapp)


def mask_radial(radial,mask):
    b,bp,bpp=radial
    eta,etap,etapp=[x[:,None] for x in mask]
    return [eta*b,eta*bp+etap*b,eta*bpp+2*etap*bp+etapp*b]


class SplitRadialSpace:
    """Keep the same number of unknowns, localized to the two transitions."""
    def __init__(self,meridian,free_count):
        self.free_count=free_count
        self.blocks=[]
        counts=[free_count//2,free_count-free_count//2]
        offset=0
        for (left,right),count in zip([(meridian.start,meridian.core_left),
                                       (meridian.core_right,meridian.end)],counts):
            controls=count+6
            interior=np.linspace(left,right,controls-4)[1:-1]
            knots=np.r_[np.repeat(left,6),interior,np.repeat(right,6)]
            self.blocks.append((left,right,count,offset,knots,BSpline(knots,np.eye(controls),5,extrapolate=False)))
            offset+=count
    def basis(self,s):
        s=np.asarray(s)
        output=[np.zeros((len(s),self.free_count)) for _ in range(3)]
        for left,right,count,offset,_,basis in self.blocks:
            inside=(s>=left)&(s<=right)
            for order in range(3):
                output[order][inside,offset:offset+count]=basis.derivative(order)(s[inside])[:,3:count+3]
        return output
    def collocation(self,order):
        nodes,_=np.polynomial.legendre.leggauss(order)
        values=[]
        for _,_,_,_,knots,_ in self.blocks:
            unique=np.unique(knots)
            for left,right in zip(unique[:-1],unique[1:]):
                values.extend(left+(right-left)*(nodes+1)/2)
        return np.array(values)


class PinnedCartesianSpace(TrialSpace):
    def __init__(self,args):
        if args.offset!=0:
            raise ValueError('first folded branch is explicitly coaxial; use offset=0')
        self.args=args
        super().__init__(make_meridian(args),args.controls,args.modes,0.,0.,'fixed')
        self.split=SplitRadialSpace(self.metric,self.shape[0]) if args.plateau else None
    def radial_basis(self,s):
        return self.split.basis(s) if getattr(self,'split',None) else super().radial_basis(s)
    def collocation(self,order=8):
        return self.split.collocation(order) if self.split else super().collocation(order)
    def prepare(self,s,u):
        grid=super().prepare(s,u)
        bridge,mask=core_bridge_and_mask(s,self.metric)
        if not self.split:
            grid['radial']=mask_radial(grid['radial'],mask)
        a,_,ap,_,app,_=self.metric.evaluate(np.asarray(s))
        B,Bp,Bpp=bridge
        f0,f1,f2=a*B,ap*B+a*Bp,app*B+2*ap*Bp+a*Bpp
        core=core_curve(u,self.args)
        er=np.stack((np.cos(u),np.sin(u),np.zeros_like(u)),axis=-1)
        et=np.stack((-np.sin(u),np.cos(u),np.zeros_like(u)),axis=-1)
        difference=[core['gamma']-er,core['du']-et,core['duu']+er]
        for index,(factor,angular_order) in enumerate([(f0,0),(f1,0),(f0,1),(f2,0),(f1,1),(f0,2)]):
            grid['base'][index]+=factor[:,None,None]*difference[angular_order][None,:,:]
        return grid


class ReferenceMetricProblem(FrozenCurvatureProblem):
    def __init__(self,space,limit,weight):
        self.space,self.limit,self.weight,self._cache=space,limit,weight,None
    def prepare(self,s,u):
        grid=self.space.prepare(s,u)
        a,_,_,_,app,_=self.space.metric.evaluate(np.asarray(s))
        grid['frozen_metric']=(np.ones_like(a),np.zeros_like(a),a*a)
        grid['whitener']=(np.ones_like(a[:,None]),np.zeros_like(a[:,None]),1/a[:,None])
        grid['target_intrinsic_K']=-app/a
        return grid


class PinnedUnitSpace(UnitTangentSpace):
    def __init__(self,args):
        UnitTangentSpace.__init__(self,args)
        self.meridian=make_meridian(args)
        self.radial=TrialSpace(self.meridian,args.controls,args.modes,0.,0.)
        self.split=SplitRadialSpace(self.meridian,self.j) if args.plateau else None
    def prepare(self,s,n):
        s=np.asarray(s); u=np.arange(n)*2*np.pi/n
        a,z,ap,zp,app,zpp=self.meridian.evaluate(s)
        bridge,mask=core_bridge_and_mask(s,self.meridian)
        B,Bp,Bpp=bridge
        core=core_curve(u,self.args)
        radial=self.split.basis(s) if self.split else mask_radial(self.radial.radial_basis(s),mask)
        center=np.column_stack((np.zeros_like(s),np.zeros_like(s),z))
        cp=np.column_stack((np.zeros_like(s),np.zeros_like(s),zp))
        cpp=np.column_stack((np.zeros_like(s),np.zeros_like(s),zpp))
        return {'s':s,'u':u,'radial':radial,'psi_radial':radial,
                'fourier':fourier(u,self.args.modes),'a':a,'ap':ap,'app':app,
                'c':center,'cp':cp,'cpp':cpp,
                'delta_base':B[:,None]*core['angle_delta'],
                'delta_s':Bp[:,None]*core['angle_delta'],
                'delta_ss':Bpp[:,None]*core['angle_delta'],
                'delta_u':B[:,None]*(core['angle_u']-1)}


class PinnedSignedSpace(SignedFrenetSpace,PinnedUnitSpace):
    pass


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--engine',choices=['cartesian','unit','signed'],default='cartesian')
    parser.add_argument('--radius',type=float,default=.8)
    parser.add_argument('--length',type=float,default=3.)
    parser.add_argument('--collar',type=float,default=.06)
    parser.add_argument('--beta-wiggle',type=float,default=2.4)
    parser.add_argument('--plateau',type=float,default=.15)
    parser.add_argument('--quadrature',type=int,default=96)
    parser.add_argument('--offset',type=float,default=0.)
    parser.add_argument('--controls',type=int,default=14)
    parser.add_argument('--modes',type=int,default=6)
    parser.add_argument('--radial-order',type=int,default=8)
    parser.add_argument('--angles',type=int,default=64)
    parser.add_argument('--core-shape',choices=['curvature','ellipse'],default='curvature')
    parser.add_argument('--seed2',type=float,default=.25)
    parser.add_argument('--seed3',type=float,default=.2)
    parser.add_argument('--ellipse-major',type=float,default=1.4)
    parser.add_argument('--ellipse-minor',type=float,default=.5)
    parser.add_argument('--curvature-limit',type=float,default=13.)
    parser.add_argument('--curvature-weight',type=float,default=0.)
    parser.add_argument('--closure-weight',type=float,default=2.)
    parser.add_argument('--max-nfev',type=int,default=180)
    parser.add_argument('--reference-audit',type=Path)
    parser.add_argument('--resume',type=Path)
    parser.add_argument('--check-jacobian',action='store_true')
    parser.add_argument('--smoke-only',action='store_true')
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.offset!=0 or args.plateau<0 or abs(args.seed2)+abs(args.seed3)>=.95:
        parser.error('require offset=0, plateau>=0 and |seed2|+|seed3|<.95')
    if not (args.ellipse_major>=args.ellipse_minor>0):
        parser.error('require ellipse major>=minor>0')
    if not args.smoke_only and (os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        parser.error('optimization belongs in the public repository Actions; --smoke-only is for cheap development checks')
    # Existing unit/signed code expects these explicit, fixed-radius settings.
    args.fixed_radius=True; args.pin_core=True; args.seed_asymmetry=0.
    args.radius_floor=.7; args.radius_ceiling=1.3; args.radius_weight=10.
    args.signed_flow=args.engine=='signed'
    started=time.monotonic()
    if args.engine=='cartesian':
        space=PinnedCartesianSpace(args)
        problem=ReferenceMetricProblem(space,args.curvature_limit,args.curvature_weight)
        s=space.collocation(args.radial_order)
        grid=problem.prepare(s,np.arange(args.angles)*2*np.pi/args.angles)
        audit=lambda q,n:problem.audit(q,n,max(128,2*args.angles))
        residual=lambda q:problem.residual(q,grid)
        jacobian=lambda q:problem.jacobian(q,grid)
        meridian=space.metric
    else:
        space=(PinnedSignedSpace if args.engine=='signed' else PinnedUnitSpace)(args)
        radial=space.split.collocation(args.radial_order) if space.split else space.radial.collocation(args.radial_order)
        grid=space.prepare(radial,args.angles)
        audit=lambda q,n:space.audit(q,n,max(128,2*args.angles))
        residual=lambda q:space.residual(q,grid)
        jacobian=lambda q:space.jacobian(q,grid)
        meridian=space.meridian
    q0=np.zeros(space.size)
    if args.resume:
        saved=json.loads(args.resume.read_text())
        if saved['definition']['engine']!=args.engine or len(saved['coefficients'])!=space.size:
            raise ValueError('resume basis or engine mismatch; project explicitly')
        for key in ['radius','length','collar','beta_wiggle','plateau','core_shape','seed2','seed3','ellipse_major','ellipse_minor']:
            if saved['definition'][key]!=getattr(args,key):
                raise ValueError('resume changes the fixed geometry/core; use a separate design run')
        q0=np.asarray(saved['coefficients'],float)
    reference=None
    if args.reference_audit:
        reference=json.loads(args.reference_audit.read_text())
        expected={'beta_wiggle':args.beta_wiggle,'length':args.length,'radius':args.radius,'collar_fraction':args.collar}
        if any(float(reference['parameters'][k])!=v for k,v in expected.items()) or float(reference['central_half_plateau_fraction'])!=args.plateau:
            raise ValueError('circular reference audit parameters do not match this BVP')
    derivative=None
    if args.check_jacobian:
        direction=np.random.default_rng(20261114).normal(size=space.size)
        direction/=np.linalg.norm(direction); eps=2e-7
        numeric=(residual(q0+eps*direction)-residual(q0-eps*direction))/(2*eps)
        analytic=jacobian(q0)@direction
        derivative=float(np.linalg.norm(numeric-analytic)/max(np.linalg.norm(numeric),1e-30))
        print(json.dumps({'jacobian_relative_error':derivative}),flush=True)
    initial=audit(q0,65 if args.smoke_only else 257)
    evaluations=[0]
    def fun(q):
        value=residual(q); evaluations[0]+=1
        if evaluations[0]%10==1:
            print(json.dumps({'evaluation':evaluations[0],'rms':float(np.sqrt(np.mean(value*value))),
                              'maximum':float(np.max(abs(value))),'seconds':time.monotonic()-started}),flush=True)
        return value
    if args.smoke_only:
        rr=residual(q0)
        result=argparse.Namespace(x=q0,success=False,message='development smoke only; no optimization',nfev=0,cost=float(rr@rr)/2,optimality=None)
    else:
        result=least_squares(fun,q0,jac=jacobian,method='lm',x_scale='jac',
                             max_nfev=args.max_nfev,ftol=1e-11,gtol=1e-11,xtol=1e-11)
    audits=[audit(result.x,n) for n in ([65] if args.smoke_only else [257,1025])]
    source_names=['folded_collar_search.py','eccentric_collar_search.py','eccentric_curvature_search.py','unit_tangent_collar_search.py']
    report={'schema':'folded-pinned-collar-v1','status':'development_smoke_only' if args.smoke_only else 'finite_fixed_metric_search',
            'definition':{k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},
            'target_metric':'ds^2+a_reference(s)^2 du^2; fixed throughout this run',
            'reference_meridian':meridian.identity(),'open_core_pinned':bool(args.plateau),
            'radial_representation':'separate clamped quintic transitions with the same total free count' if args.plateau else 'whole-band quintics with central first-jet zero mask',
            'central_value_and_first_jet_pinned':True,'e0_coaxial_branch':True,
            'circular_reference_audit':reference,'reference_proof_does_not_certify_this_nonaxisymmetric_field':True,
            'core_material_centroid_fixed_once':True,'noncentral_center_modes_retained':True,
            'initial_audit':initial,'final_audits':audits,'jacobian_relative_error':derivative,
            'solver':{'success':bool(result.success),'message':result.message,'nfev':int(result.nfev),
                      'cost':float(result.cost),'optimality':None if result.optimality is None else float(result.optimality)},
            'coefficients':result.x.tolist(),'elapsed_seconds':time.monotonic()-started,
            'source_sha256':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in source_names},
            'claim':{'exact_isometry':False,'fixed_metric_refinement_demonstrated':False,
                     'closed_embedded_family':False,'held_displacement_certified':False,
                     'reach_certified':False,'task_complete':False}}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'out':str(args.out),'engine':args.engine,'final_audit':audits[-1]}),flush=True)


if __name__=='__main__':
    main()
