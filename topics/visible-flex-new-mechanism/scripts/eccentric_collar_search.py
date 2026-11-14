#!/usr/bin/env python3
"""Finite Cartesian search for a warped-metric annulus with eccentric collars.

This is a design/search diagnostic, not an existence or reach certificate.
All geometry and equations are defined here independently; no private data.

In fixed mode the target g=ds^2+a(s)^2 du^2 is fixed during each solve.
In angular-design mode only angular dependence of E,F,G is minimized;
their radial means remain free and this changes the designed metric.
The reference
meridian has tangent angle beta(s)=pi*S(x)+b*sin(2*pi*S(x)), where x runs
between two open flat collars and S is the quintic smoothstep.  Its radius
and height are defined by quadratures a'=cos(beta), z'=sin(beta).

The unknown is a Cartesian Fourier expansion times quintic B-splines.
Its full two-jet is zero on both collars.  A prescribed, exactly clamped
translation/tilt places the upper collar at an eccentric centre.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path

import numpy as np
from scipy.interpolate import BSpline
from scipy.optimize import least_squares


def smoothstep(x):
    x = np.asarray(x)
    y = np.clip(x, 0.0, 1.0)
    value = y**3 * (10.0 + y * (-15.0 + 6.0 * y))
    d1 = 30.0 * y**2 * (1.0 - y)**2
    d2 = 60.0 * y * (1.0 - y) * (1.0 - 2.0*y)
    return value, d1, d2


class Meridian:
    def __init__(self, radius=.45, length=2.0, collar=.06, wiggle=.9, quad=96):
        if not (radius > 0 and length > 0 and 0 < collar < .25):
            raise ValueError("invalid meridian parameters")
        self.radius, self.length = float(radius), float(length)
        self.collar, self.wiggle = float(collar), float(wiggle)
        self.start, self.end = length*collar, length*(1-collar)
        self.nodes, self.weights = np.polynomial.legendre.leggauss(quad)
        self.height = 2*self._integrals(np.array([length/2]))[0, 1]

    def beta(self, s):
        value, d1, d2 = smoothstep((np.asarray(s)-self.start)/(self.end-self.start))
        beta = np.pi*value + self.wiggle*np.sin(2*np.pi*value)
        factor = np.pi + 2*np.pi*self.wiggle*np.cos(2*np.pi*value)
        beta1 = factor*d1/(self.end-self.start)
        beta2 = (factor*d2 - 4*np.pi**2*self.wiggle*np.sin(2*np.pi*value)*d1**2)/(self.end-self.start)**2
        return beta, beta1, beta2

    def _integrals(self, s):
        s = np.asarray(s, float).reshape(-1)
        stop = np.maximum(s, self.start)
        half = (stop-self.start)/2
        points = self.start+half[:, None]*(1+self.nodes[None, :])
        beta, _, _ = self.beta(points)
        cosint = half*(np.cos(beta)@self.weights)+np.minimum(s, self.start)
        sinint = half*(np.sin(beta)@self.weights)
        return np.column_stack((cosint, sinint))

    def evaluate(self, s):
        s = np.asarray(s, float)
        reflected = np.minimum(s, self.length-s)
        integ = self._integrals(reflected)
        a = self.radius+integ[:, 0]
        z = np.where(s <= self.length/2, integ[:, 1], self.height-integ[:, 1])
        beta, beta1, _ = self.beta(s)
        return a, z, np.cos(beta), np.sin(beta), -np.sin(beta)*beta1, np.cos(beta)*beta1

    def identity(self):
        return {"formula": "a'=cos(pi*S+b*sin(2*pi*S)); z'=sin(pi*S+b*sin(2*pi*S)); S=quintic smoothstep on [collar*L,(1-collar)*L]",
                "initial_radius": self.radius, "length": self.length,
                "collar_fraction": self.collar, "beta_wiggle": self.wiggle,
                "quadrature_order": len(self.nodes), "reference_height": float(self.height)}


def fourier(u, modes):
    u = np.asarray(u)
    values = [np.ones_like(u)]
    d1 = [np.zeros_like(u)]
    d2 = [np.zeros_like(u)]
    for m in range(1, modes+1):
        values.extend((np.cos(m*u), np.sin(m*u)))
        d1.extend((-m*np.sin(m*u), m*np.cos(m*u)))
        d2.extend((-m*m*np.cos(m*u), -m*m*np.sin(m*u)))
    return tuple(np.column_stack(x) for x in (values, d1, d2))


class TrialSpace:
    def __init__(self, meridian, controls, modes, offset, tilt, metric_mode='fixed',
                 design_floor=.1, barrier_weight=10., design_ceiling=4., design_objective='relative'):
        if controls < 9 or modes < 1:
            raise ValueError("use controls>=9, modes>=1")
        self.metric = meridian
        self.controls, self.modes = controls, modes
        self.offset, self.tilt = float(offset), float(tilt)
        self.metric_mode = metric_mode
        self.design_floor, self.barrier_weight = float(design_floor),float(barrier_weight)
        self.design_ceiling=float(design_ceiling)
        self.design_objective=design_objective
        interior = np.linspace(meridian.start, meridian.end, controls-4)[1:-1]
        self.knots = np.r_[np.repeat(meridian.start, 6), interior, np.repeat(meridian.end, 6)]
        self.basis = BSpline(self.knots, np.eye(controls), 5, extrapolate=False)
        self.free = slice(3, controls-3)
        self.shape = (controls-6, 2*modes+1, 3)
        self.size = math.prod(self.shape)
        ct, st = np.cos(tilt), np.sin(tilt)
        self.rotation = np.array([[ct, 0., st], [0., 1., 0.], [-st, 0., ct]])

    def radial_basis(self, s):
        s = np.asarray(s)
        inside = (s >= self.metric.start) & (s <= self.metric.end)
        result = []
        for order in range(3):
            values = np.zeros((len(s), self.shape[0]))
            values[inside] = self.basis.derivative(order)(s[inside])[:, self.free]
            result.append(values)
        return result

    def collocation(self, order=3):
        points, weights = np.polynomial.legendre.leggauss(order)
        unique = np.unique(self.knots)
        ss = []
        for left, right in zip(unique[:-1], unique[1:]):
            ss.extend((left+(right-left)*(1+points)/2).tolist())
        return np.array(ss)

    def prepare(self, s, u):
        s, u = np.asarray(s), np.asarray(u)
        aa, zz, ap, zp, app, zpp = self.metric.evaluate(s)
        if np.min(aa) <= 0:
            raise ValueError("target radius is nonpositive")
        co, si = np.cos(u), np.sin(u)
        ones = np.ones_like(u)
        def xyz(x, y, z):
            return np.stack((x, y, z), axis=-1)
        base = xyz(aa[:,None]*co, aa[:,None]*si, zz[:,None]*ones)
        bs = xyz(ap[:,None]*co, ap[:,None]*si, zp[:,None]*ones)
        bu = xyz(-aa[:,None]*si, aa[:,None]*co, np.zeros((len(s),len(u))))
        bss = xyz(app[:,None]*co, app[:,None]*si, zpp[:,None]*ones)
        bsu = xyz(-ap[:,None]*si, ap[:,None]*co, np.zeros((len(s),len(u))))
        buu = xyz(-aa[:,None]*co, -aa[:,None]*si, np.zeros((len(s),len(u))))
        f, fp, fpp = smoothstep((s-self.metric.start)/(self.metric.end-self.metric.start))
        fp = fp/(self.metric.end-self.metric.start)
        fpp = fpp/(self.metric.end-self.metric.start)**2
        delta = self.rotation-np.eye(3)
        rel = base-np.array([0., 0., self.metric.height])
        change = rel@delta.T+np.array([self.offset, 0., 0.])
        cs, cu = bs@delta.T, bu@delta.T
        transformed = [base+f[:,None,None]*change,
                       bs+fp[:,None,None]*change+f[:,None,None]*cs,
                       bu+f[:,None,None]*cu,
                       bss+fpp[:,None,None]*change+2*fp[:,None,None]*cs+f[:,None,None]*(bss@delta.T),
                       bsu+fp[:,None,None]*cu+f[:,None,None]*(bsu@delta.T),
                       buu+f[:,None,None]*(buu@delta.T)]
        return {"s":s, "u":u, "a":aa, "base":transformed,
                "radial":self.radial_basis(s), "angular":fourier(u,self.modes)}

    def geometry(self, q, grid, second=False):
        coeff = np.asarray(q).reshape(self.shape)
        r, a = grid["radial"], grid["angular"]
        orders = [(0,0),(1,0),(0,1)]
        if second:
            orders += [(2,0),(1,1),(0,2)]
        return [grid["base"][i]+np.einsum('rj,uk,jkc->ruc', r[ri],a[ai],coeff,optimize=True)
                for i,(ri,ai) in enumerate(orders)]

    def residual(self, q, grid):
        _, fs, fu = self.geometry(q,grid)
        a = grid["a"][:,None]
        e = np.einsum('...c,...c->...',fs,fs)-1
        f = np.einsum('...c,...c->...',fs,fu)/a
        g = np.einsum('...c,...c->...',fu,fu)/a**2-1
        value=np.stack((e,np.sqrt(2)*f,g),axis=-1)
        if self.metric_mode == 'angular-design':
            mu=np.mean(value,axis=1,keepdims=True)
            if self.design_objective == 'absolute':
                return (value-mu).ravel()
            me,mg=np.maximum(mu[:,:,0]+1,1e-14),np.maximum(mu[:,:,2]+1,1e-14)
            mc=mu[:,:,1]/np.sqrt(2)
            value -= mu
            value[:,:,0] /= me
            value[:,:,1] /= np.sqrt(me*mg)
            value[:,:,2] /= mg
            schur=me-mc*mc/mg
            barriers=self.barrier_weight*np.sqrt(len(grid['u']))*np.stack(
                (np.maximum(self.design_floor-schur[:,0],0),
                 np.maximum(self.design_floor-mg[:,0],0),
                 np.maximum(me[:,0]-self.design_ceiling,0),
                 np.maximum(mg[:,0]-self.design_ceiling,0)),axis=1)
            return np.r_[value.ravel(),barriers.ravel()]
        return value.ravel()

    def jacobian(self, q, grid):
        _, fs, fu = self.geometry(q,grid)
        r0,r1,_ = grid["radial"]
        a0,a1,_ = grid["angular"]
        ar = grid["a"][:,None,None,None]
        b_s = r1[:,None,:,None]*a0[None,:,None,:]
        b_u = r0[:,None,:,None]*a1[None,:,None,:]
        jac = np.empty((len(grid["s"]),len(grid["u"]),3,*self.shape))
        for c in range(3):
            x,y = fs[:,:,c,None,None],fu[:,:,c,None,None]
            jac[:,:,0,:,:,c] = 2*x*b_s
            jac[:,:,1,:,:,c] = np.sqrt(2)*(y*b_s+x*b_u)/ar
            jac[:,:,2,:,:,c] = 2*y*b_u/ar**2
        if self.metric_mode == 'angular-design':
            if self.design_objective == 'absolute':
                return (jac-np.mean(jac,axis=1,keepdims=True)).reshape(-1,self.size)
            raw=np.stack((np.einsum('...c,...c->...',fs,fs),
                          np.sqrt(2)*np.einsum('...c,...c->...',fs,fu)/grid['a'][:,None],
                          np.einsum('...c,...c->...',fu,fu)/grid['a'][:,None]**2),axis=2)
            mu=np.mean(raw,axis=1,keepdims=True)
            me,mg=np.maximum(mu[:,:,0],1e-14),np.maximum(mu[:,:,2],1e-14)
            mc=mu[:,:,1]/np.sqrt(2)
            dmu=np.mean(jac,axis=1,keepdims=True)
            raw-=mu
            me5,mg5=me[:,:,None,None,None],mg[:,:,None,None,None]
            mc5=mc[:,:,None,None,None]
            jac[:,:,0]=(jac[:,:,0]-dmu[:,:,0])/me5-raw[:,:,0,None,None,None]*dmu[:,:,0]/me5**2
            jac[:,:,1]=(jac[:,:,1]-dmu[:,:,1])/np.sqrt(me5*mg5)-raw[:,:,1,None,None,None]/np.sqrt(me5*mg5)*.5*(dmu[:,:,0]/me5+dmu[:,:,2]/mg5)
            jac[:,:,2]=(jac[:,:,2]-dmu[:,:,2])/mg5-raw[:,:,2,None,None,None]*dmu[:,:,2]/mg5**2
            schur=me-mc*mc/mg
            ds=dmu[:,:,0]-2*mc5/mg5*dmu[:,:,1]/np.sqrt(2)+mc5**2/mg5**2*dmu[:,:,2]
            db=np.stack((-ds[:,0]*(schur[:,0]<self.design_floor)[:,None,None,None],
                         -dmu[:,0,2]*(mg[:,0]<self.design_floor)[:,None,None,None],
                         dmu[:,0,0]*(me[:,0]>self.design_ceiling)[:,None,None,None],
                         dmu[:,0,2]*(mg[:,0]>self.design_ceiling)[:,None,None,None]),axis=1)
            db*=self.barrier_weight*np.sqrt(len(grid['u']))
            return np.concatenate((jac.reshape(-1,self.size),db.reshape(-1,self.size)),axis=0)
        return jac.reshape(-1,self.size)

    def seed(self, amplitude2, amplitude3):
        q=np.zeros(self.shape)
        for m,amp in [(2,amplitude2),(3,amplitude3)]:
            if amp == 0:
                continue
            if m+1 > self.modes:
                raise ValueError("radial mixed seed requires modes>=4")
            # cos(m*u)*(cos(u),sin(u),0), represented exactly.
            q[:,2*(m+1)-1,0] += amp/2
            q[:,2*(m-1)-1,0] += amp/2
            q[:,2*(m+1),1] += amp/2
            q[:,2*(m-1),1] -= amp/2
            q[:,2*m-1,2] += .3*amp
        return q.ravel()

    def curvature_seed(self, amplitude2, amplitude3, asymmetry=.3):
        """Project exact constant-speed convex cross sections into the trial space.

        rho=a*(1+A*cos(2phi)+B*cos(3phi)), theta=phi+A/2*sin(2phi)+B/3*sin(3phi).
        Support h=a*(1-A/3*cos(2phi)-B/8*cos(3phi)) gives rho=h+h''.
        This seed fixes each cross-section perimeter, not its meridional metric.
        Its material means are retained; no individual section is recentered.
        """
        if abs(amplitude2)+abs(amplitude3)*(1+abs(asymmetry)) >= .95:
            raise ValueError('curvature seed must keep rho strictly positive')
        s=self.collocation(6)
        u=np.arange(max(64,4*self.modes+2))*2*np.pi/max(64,4*self.modes+2)
        x=(s-self.metric.start)/(self.metric.end-self.metric.start)
        bump=64*x**3*(1-x)**3
        A=amplitude2*bump[:,None]
        B=amplitude3*(bump*(1+asymmetry*(2*x-1)))[:,None]
        phi=np.broadcast_to(u,(len(s),len(u))).copy()
        for _ in range(15):
            phi -= (phi+A*np.sin(2*phi)/2+B*np.sin(3*phi)/3-u)/(1+A*np.cos(2*phi)+B*np.cos(3*phi))
        a=self.metric.evaluate(s)[0][:,None]
        h=a*(1-A*np.cos(2*phi)/3-B*np.cos(3*phi)/8)
        hp=a*(2*A*np.sin(2*phi)/3+3*B*np.sin(3*phi)/8)
        dx=h*np.cos(phi)-hp*np.sin(phi)-a*np.cos(u)
        dy=h*np.sin(phi)+hp*np.cos(phi)-a*np.sin(u)
        displacement=np.stack((dx,dy,np.zeros_like(dx)),axis=2)
        angular=fourier(u,self.modes)[0]
        weight=np.r_[1.,np.full(2*self.modes,2.)]/len(u)
        target=np.einsum('ruc,uk,k->rkc',displacement,angular,weight)
        radial=self.radial_basis(s)[0]
        coeff=np.linalg.lstsq(radial,target.reshape(len(s),-1),rcond=None)[0]
        return coeff.reshape(-1)

    def audit(self,q,radial,angular):
        grid=self.prepare(np.linspace(0,self.metric.length,radial),np.arange(angular)*2*np.pi/angular)
        f,fs,fu,fss,fsu,fuu=self.geometry(q,grid,second=True)
        a=grid['a'][:,None]
        e=np.einsum('...c,...c->...',fs,fs)
        mixed=np.einsum('...c,...c->...',fs,fu)
        g=np.einsum('...c,...c->...',fu,fu)
        if self.metric_mode == 'angular-design':
            eb,fb,gb=[np.mean(x,axis=1,keepdims=True) for x in [e,mixed,g]]
        else:
            eb,fb,gb=np.ones_like(a),np.zeros_like(a),a*a
        de,df,dg=e-eb,mixed-fb,g-gb
        ee,gg,ff=de,dg/a**2,df/a
        determinant=eb*gb-fb*fb
        trace=(gb*de+eb*dg-2*fb*df)/determinant
        determinant_delta=(de*dg-df*df)/determinant
        discriminant=np.sqrt(np.maximum(trace*trace-4*determinant_delta,0.))
        op=np.maximum(np.abs((trace+discriminant)/2),np.abs((trace-discriminant)/2))
        cross=np.cross(fs,fu)
        area=np.linalg.norm(cross,axis=-1)
        normal=cross/np.maximum(area[:,:,None],1e-300)
        l=np.einsum('...c,...c->...',normal,fss)
        m=np.einsum('...c,...c->...',normal,fsu)
        n=np.einsum('...c,...c->...',normal,fuu)
        det=e*g-mixed**2
        H=(g*l+e*n-2*mixed*m)/(2*np.maximum(det,1e-300))
        K=(l*n-m*m)/np.maximum(det,1e-300)
        root=np.sqrt(np.maximum(H*H-K,0))
        curvature=np.maximum(np.abs(H+root),np.abs(H-root))
        return {"radial_points":radial,"angular_points":angular,
                "metric_relative_operator_sample_max":float(np.max(op)),
                "metric_components_sample_max":[float(np.max(np.abs(x))) for x in [ee,ff,gg]],
                "metric_relative_rms":float(np.sqrt(np.mean(np.maximum(trace*trace-2*determinant_delta,0)))),
                "audit_target":"angular mean of this candidate" if self.metric_mode=='angular-design' else "fixed reference metric",
                "target_mean_E_range":[float(np.min(eb)),float(np.max(eb))],
                "target_mean_G_range":[float(np.min(gb)),float(np.max(gb))],
                "target_schur_min":float(np.min(eb-fb*fb/gb)),
                "min_area_density_sample":float(np.min(area)),
                "max_principal_curvature_sample":float(np.max(curvature)),
                "coordinate_min":np.min(f,axis=(0,1)).tolist(),
                "coordinate_max":np.max(f,axis=(0,1)).tolist(),
                "closed_surface":False,"continuous_error_bound":False,
                "embedding_proved":False,"reach_proved":False}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--radius',type=float,default=.45)
    ap.add_argument('--length',type=float,default=2.)
    ap.add_argument('--collar',type=float,default=.06)
    ap.add_argument('--beta-wiggle',type=float,default=.9)
    ap.add_argument('--quadrature',type=int,default=96)
    ap.add_argument('--controls',type=int,default=12)
    ap.add_argument('--modes',type=int,default=4)
    ap.add_argument('--offset',type=float,default=.02)
    ap.add_argument('--tilt',type=float,default=0.)
    ap.add_argument('--seed2',type=float,default=.08)
    ap.add_argument('--seed3',type=float,default=.08)
    ap.add_argument('--seed-kind',choices=['radial','curvature'],default='radial')
    ap.add_argument('--seed-asymmetry',type=float,default=.3)
    ap.add_argument('--radial-order',type=int,default=3)
    ap.add_argument('--angles',type=int,default=24)
    ap.add_argument('--max-nfev',type=int,default=80)
    ap.add_argument('--method',choices=['lm','trf'],default='lm')
    ap.add_argument('--metric-mode',choices=['fixed','angular-design'],default='fixed')
    ap.add_argument('--design-floor',type=float,default=.1)
    ap.add_argument('--barrier-weight',type=float,default=10.)
    ap.add_argument('--design-ceiling',type=float,default=4.)
    ap.add_argument('--design-objective',choices=['absolute','relative'],default='relative')
    ap.add_argument('--resume',type=Path)
    ap.add_argument('--audit-only',action='store_true')
    ap.add_argument('--audit-radials',type=int,nargs='+',default=[65,129,257])
    ap.add_argument('--linear-spectrum',action='store_true')
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    start=time.monotonic()
    metric=Meridian(args.radius,args.length,args.collar,args.beta_wiggle,args.quadrature)
    space=TrialSpace(metric,args.controls,args.modes,args.offset,args.tilt,args.metric_mode,args.design_floor,args.barrier_weight,args.design_ceiling,args.design_objective)
    radial=space.collocation(args.radial_order)
    angular=np.arange(args.angles)*2*np.pi/args.angles
    grid=space.prepare(radial,angular)
    q0=space.seed(args.seed2,args.seed3) if args.seed_kind=='radial' else space.curvature_seed(args.seed2,args.seed3,args.seed_asymmetry)
    if args.resume:
        data=json.loads(args.resume.read_text())
        if data['coefficient_shape'] != list(space.shape):
            raise ValueError('resume basis shape does not match')
        q0=np.array(data['coefficients'],float).reshape(-1)
    counter=[0]
    def fun(q):
        value=space.residual(q,grid)
        counter[0]+=1
        if counter[0] % 10 == 1:
            print(json.dumps({'evaluation':counter[0],'rms':float(np.sqrt(np.mean(value**2))),
                              'max':float(np.max(np.abs(value))),'seconds':time.monotonic()-start}),flush=True)
        return value
    initial=space.audit(q0,65,max(64,args.angles*2))
    spectrum=None
    if args.linear_spectrum:
        singular=np.linalg.svd(space.jacobian(np.zeros(space.size),grid),compute_uv=False)
        spectrum={'smallest_12':singular[-12:].tolist(),'largest':float(singular[0]),
                  'scope':'finite Jacobian at prescribed-offset clamped reference; not a continuous inverse'}
    if args.audit_only:
        r0=space.residual(q0,grid)
        result=argparse.Namespace(x=q0,success=False,status=0,message='audit only; no optimization',
                                 nfev=0,njev=0,cost=float(r0@r0)/2,optimality=None)
    else:
        result=least_squares(fun,q0,jac=lambda q:space.jacobian(q,grid),method=args.method,
                             ftol=1e-11,xtol=1e-11,gtol=1e-11,max_nfev=args.max_nfev,
                             x_scale='jac')
    audits=[space.audit(result.x,n,max(64,args.angles*2)) for n in args.audit_radials]
    report={'schema':'eccentric-collar-search-v1','status':'audit_only' if args.audit_only else 'finite_search_only',
            'metric_mode':args.metric_mode,
            'design_nondegeneracy':{'reference_scaled_schur_floor':args.design_floor,
                                    'reference_scaled_G_floor':args.design_floor,
                                    'reference_scaled_E_G_ceiling':args.design_ceiling,
                                    'soft_barrier_weight':args.barrier_weight},
            'design_objective':args.design_objective,
            'fixed_metric':metric.identity() if args.metric_mode=='fixed' else None,
            'reference_meridian':metric.identity(),
            'boundary':{'upper_centre_offset':[args.offset,0.,0.],
                        'upper_tilt_y':args.tilt,'upper_rotation':space.rotation.tolist(),
                        'open_collar_two_jets_exact_by_representation':True},
            'discretization':{'controls':args.controls,'modes':args.modes,
                              'radial_collocation':len(radial),'angular_collocation':args.angles,
                              'radial_gauss_order':args.radial_order},
            'initial_seed':{'radial_mode2':args.seed2,'radial_mode3':args.seed3,
                            'kind':args.seed_kind,'asymmetry':args.seed_asymmetry,
                            'resume':str(args.resume) if args.resume else None},
            'solver':{'method':args.method,'success':bool(result.success),'status':int(result.status),
                      'message':result.message,'nfev':int(result.nfev),'njev':int(result.njev or 0),
                      'cost':float(result.cost),'optimality':None if result.optimality is None else float(result.optimality)},
            'initial_audit':initial,'final_audits':audits,'linear_spectrum':spectrum,
            'coefficient_shape':list(space.shape),'coefficients':result.x.tolist(),
            'elapsed_seconds':time.monotonic()-start,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'claim':{'closed_family':False,'exact_isometry':False,'reach_certified':False,
                     'task_complete':False,'fixed_metric_refinement_demonstrated':False}}
    if args.metric_mode=='angular-design':
        sample_s=np.linspace(0,metric.length,33)
        mean_grid=space.prepare(sample_s,np.arange(2*args.modes+1)*2*np.pi/(2*args.modes+1))
        _,fs,fu=space.geometry(result.x,mean_grid)
        mean_components=[np.mean(np.einsum('...c,...c->...',x,y),axis=1)
                         for x,y in [(fs,fs),(fs,fu),(fu,fu)]]
        report['designed_metric_samples']={'s':sample_s.tolist(),
            **dict(zip(['E','F','G'],[x.tolist() for x in mean_components])),
            'not_a_frozen_target_certificate':True}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'out':str(args.out),'solver_success':bool(result.success),
                      'metric_sample_max':audits[-1]['metric_relative_operator_sample_max'],
                      'seconds':report['elapsed_seconds']}),flush=True)


if __name__=='__main__':
    main()
