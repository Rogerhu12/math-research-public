#!/usr/bin/env python3
"""Frozen-metric curvature tradeoff for a public eccentric-collar trial field.

The target is the exact angular average (in the finite Fourier model) of a
specified source field's first fundamental form. It is frozen throughout.
The new residual penalizes the true shape-operator Frobenius norm, not an
unnormalized second derivative. This is a finite search, not a certificate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

from eccentric_collar_search import Meridian, TrialSpace


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class FrozenCurvatureProblem:
    def __init__(self, source, limit=12., weight=.01):
        self.source = source
        data = source
        p = data['reference_meridian']
        meridian = Meridian(p['initial_radius'], p['length'], p['collar_fraction'],
                            p['beta_wiggle'], p['quadrature_order'])
        d, b = data['discretization'], data['boundary']
        offset = b['upper_centre_offset']
        if offset[1:] != [0., 0.]:
            raise ValueError('this representation expects the prescribed x offset')
        self.space = TrialSpace(meridian, d['controls'], d['modes'], offset[0], b['upper_tilt_y'])
        if data['coefficient_shape'] != list(self.space.shape):
            raise ValueError('source coefficient shape does not match its basis')
        self.target_coeff = np.array(data['coefficients'], float)
        self.limit, self.weight = float(limit), float(weight)
        self._cache = None

    def prepare(self, s, u):
        grid = self.space.prepare(s, u)
        # Products have angular degree at most 2M: 2M+1 nodes integrate them.
        count = 2*self.space.modes+1
        target_grid = self.space.prepare(s, np.arange(count)*2*np.pi/count)
        _, fs, fu, fss, fsu, _ = self.space.geometry(self.target_coeff, target_grid,second=True)
        E, F, G = [np.mean(np.einsum('...c,...c->...', a,b), axis=1)
                   for a,b in [(fs,fs),(fs,fu),(fu,fu)]]
        schur = G-F*F/E
        if min(np.min(E),np.min(schur)) <= 0:
            raise ValueError('frozen mean metric is not positive definite')
        p = 1/np.sqrt(E)
        r = 1/np.sqrt(schur)
        q = -F/E*r
        grid['frozen_metric'] = (E,F,G)
        grid['whitener'] = (p[:,None],q[:,None],r[:,None])
        # Intrinsic K of an angular-invariant metric, evaluated without radial
        # finite differences. Only the exact Fourier angular derivative of Xss
        # is needed for G'', so no third radial derivative is introduced.
        frequencies = np.fft.fftfreq(count,d=1/count)
        fssu = np.fft.ifft(np.fft.fft(fss,axis=1)*(1j*frequencies[None,:,None]),axis=1).real
        def mean_dot(a,b):
            return np.mean(np.einsum('...c,...c->...',a,b),axis=1)
        Ep = 2*mean_dot(fs,fss)
        Fp = mean_dot(fss,fu)+mean_dot(fs,fsu)
        Gp = 2*mean_dot(fu,fsu)
        Gpp = 2*(mean_dot(fsu,fsu)+mean_dot(fu,fssu))
        meridian_E = E-F*F/G
        meridian_Ep = Ep-2*F*Fp/G+F*F*Gp/G**2
        radius = np.sqrt(G)
        radius_p = Gp/(2*radius)
        radius_pp = Gpp/(2*radius)-Gp*Gp/(4*radius**3)
        grid['target_intrinsic_K'] = -(radius_pp/meridian_E-radius_p*meridian_Ep/(2*meridian_E**2))/radius
        return grid

    def evaluate(self, coefficients, grid):
        if self._cache is not None:
            oldq, oldgrid, data = self._cache
            if oldgrid is grid and np.array_equal(oldq, coefficients):
                return data
        x,A,B,U,V,W = self.space.geometry(coefficients, grid, second=True)
        E = np.einsum('...c,...c->...',A,A)
        F = np.einsum('...c,...c->...',A,B)
        G = np.einsum('...c,...c->...',B,B)
        cross = np.cross(A,B)
        area = np.linalg.norm(cross,axis=-1)
        if np.min(area) <= 1e-11:
            raise FloatingPointError('trial loses immersion; true normal/curvature undefined')
        normal = cross/area[:,:,None]
        ell, mixed, nn = [np.einsum('...c,...c->...',normal,Z) for Z in [U,V,W]]
        determinant = area*area
        H = (G*ell+E*nn-2*F*mixed)/(2*determinant)
        K = (ell*nn-mixed*mixed)/determinant
        shape_frobenius = np.sqrt(np.maximum(4*H*H-2*K,0.))
        p,q,r = grid['whitener']
        a00 = p*p*E-1
        a01 = p*q*E+p*r*F
        a11 = q*q*E+2*q*r*F+r*r*G-1
        active = shape_frobenius > self.limit
        penalty = self.weight*np.maximum(shape_frobenius/self.limit-1,0.)
        residual = np.stack((a00,np.sqrt(2)*a01,a11,penalty),axis=-1)
        data = dict(x=x,A=A,B=B,U=U,V=V,W=W,E=E,F=F,G=G,area=area,
                    normal=normal,ell=ell,mixed=mixed,nn=nn,determinant=determinant,
                    H=H,K=K,shape_frobenius=shape_frobenius,active=active,
                    metric=np.stack((a00,a01,a11),axis=-1),residual=residual)
        self._cache = (np.array(coefficients,copy=True),grid,data)
        return data

    def residual(self, coefficients, grid):
        return self.evaluate(coefficients,grid)['residual'].ravel()

    def jacobian(self, coefficients, grid):
        d = self.evaluate(coefficients,grid)
        A,B,U,V,W = [d[k] for k in ['A','B','U','V','W']]
        E,F,G = [d[k] for k in ['E','F','G']]
        ell,mixed,nn,H,K,det = [d[k] for k in ['ell','mixed','nn','H','K','determinant']]
        normal,area,frob = [d[k] for k in ['normal','area','shape_frobenius']]
        # Differential of Q=tr((g^-1 II)^2)=4H^2-2K.
        factor = (2*K-8*H*H)
        qE = (4*H*nn+factor*G)/det
        qF = (-8*H*mixed-2*factor*F)/det
        qG = (4*H*ell+factor*E)/det
        ql = (4*H*G-2*nn)/det
        qm = (-8*H*F+4*mixed)/det
        qn = (4*H*E-2*ell)/det
        normal_gradient = ql[:,:,None]*U+qm[:,:,None]*V+qn[:,:,None]*W
        projected = normal_gradient-normal*np.einsum('...c,...c->...',normal,normal_gradient)[:,:,None]
        projected /= area[:,:,None]
        gradA = 2*qE[:,:,None]*A+qF[:,:,None]*B+np.cross(B,projected)
        gradB = qF[:,:,None]*A+2*qG[:,:,None]*B+np.cross(projected,A)
        gradU,gradV,gradW = [z[:,:,None]*normal for z in [ql,qm,qn]]
        coefficient = np.zeros_like(frob)
        coefficient[d['active']] = self.weight/(2*self.limit*frob[d['active']])
        curvature_gradients = [v*coefficient[:,:,None] for v in [gradA,gradB,gradU,gradV,gradW]]
        p,q,r = [v[:,:,None] for v in grid['whitener']]
        metric_gradients = [
            (2*p*p*A, np.zeros_like(B)),
            (np.sqrt(2)*(2*p*q*A+p*r*B), np.sqrt(2)*p*r*A),
            (2*q*q*A+2*q*r*B, 2*q*r*A+2*r*r*B),
        ]
        b0,b1,b2 = grid['radial']
        t0,t1,t2 = grid['angular']
        basis = [b1[:,None,:,None]*t0[None,:,None,:],
                 b0[:,None,:,None]*t1[None,:,None,:],
                 b2[:,None,:,None]*t0[None,:,None,:],
                 b1[:,None,:,None]*t1[None,:,None,:],
                 b0[:,None,:,None]*t2[None,:,None,:]]
        jac = np.empty((len(grid['s']),len(grid['u']),4,*self.space.shape))
        for c in range(3):
            for k,(gs,gu) in enumerate(metric_gradients):
                jac[:,:,k,:,:,c] = gs[:,:,c,None,None]*basis[0]+gu[:,:,c,None,None]*basis[1]
            jac[:,:,3,:,:,c] = sum(g[:,:,c,None,None]*bb for g,bb in zip(curvature_gradients,basis))
        return jac.reshape(-1,self.space.size)

    def audit(self, coefficients, radial=257, angular=96):
        grid = self.prepare(np.linspace(0,self.space.metric.length,radial),np.arange(angular)*2*np.pi/angular)
        d = self.evaluate(coefficients,grid)
        aa,bb,cc = [d['metric'][:,:,i] for i in range(3)]
        discriminant = np.sqrt((aa-cc)**2+4*bb*bb)
        op = np.maximum(abs(aa+cc+discriminant),abs(aa+cc-discriminant))/2
        root = np.sqrt(np.maximum(d['H']**2-d['K'],0.))
        principal = np.maximum(abs(d['H']+root),abs(d['H']-root))
        where = np.unravel_index(np.argmax(principal),principal.shape)
        coordinate_min = np.min(d['x'],axis=(0,1))
        coordinate_max = np.max(d['x'],axis=(0,1))
        diameter_lower_sample = float(np.max(coordinate_max-coordinate_min))
        return {'radial_points':radial,'angular_points':angular,
                'frozen_metric_relative_operator_sample_max':float(np.max(op)),
                'frozen_metric_relative_frobenius_rms':float(np.sqrt(np.mean(aa*aa+2*bb*bb+cc*cc))),
                'shape_operator_frobenius_sample_max':float(np.max(d['shape_frobenius'])),
                'principal_curvature_abs_sample_max':float(np.max(principal)),
                'actual_gauss_curvature_sample_range':[float(np.min(d['K'])),float(np.max(d['K']))],
                'target_intrinsic_K_sample_range':[float(np.min(grid['target_intrinsic_K'])),float(np.max(grid['target_intrinsic_K']))],
                'target_necessary_shape_frobenius_sample':float(np.sqrt(2*np.max(abs(grid['target_intrinsic_K'])))),
                'curvature_peak_s_u':[float(grid['s'][where[0]]),float(grid['u'][where[1]])],
                'curvature_constraint_excess_sample_max':float(max(np.max(d['shape_frobenius'])/self.limit-1,0)),
                'min_area_density_sample':float(np.min(d['area'])),
                'actual_schur_min_sample':float(np.min(d['E']-d['F']**2/d['G'])),
                'coordinate_min':coordinate_min.tolist(),'coordinate_max':coordinate_max.tolist(),
                'diameter_coordinate_lower_sample':diameter_lower_sample,
                'curvature_reach_necessary_scale_sample':float(1/(diameter_lower_sample*np.max(principal))),
                'continuous_bound':False,'embedding_proved':False,'reach_certified':False,
                'closed_surface':False,'task_complete':False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,required=True)
    parser.add_argument('--resume',type=Path)
    parser.add_argument('--limit',type=float,default=12.)
    parser.add_argument('--weight',type=float,default=.01)
    parser.add_argument('--radial-order',type=int,default=8)
    parser.add_argument('--angles',type=int,default=32)
    parser.add_argument('--max-nfev',type=int,default=80)
    parser.add_argument('--jacobian-check',action='store_true')
    parser.add_argument('--audit-only',action='store_true')
    parser.add_argument('--audit-radials',type=int,nargs='+',default=[257,1025])
    parser.add_argument('--out',type=Path,required=True)
    args = parser.parse_args()
    if args.limit <= 0 or args.weight < 0:
        parser.error('limit must be positive and weight nonnegative')
    started = time.monotonic()
    source = json.loads(args.source.read_text())
    problem = FrozenCurvatureProblem(source,args.limit,args.weight)
    q0 = problem.target_coeff.copy()
    if args.resume:
        resumed = json.loads(args.resume.read_text())
        if resumed['coefficient_shape'] != list(problem.space.shape):
            raise ValueError('resume shape must equal the fixed trial-space shape')
        if 'frozen_target' in resumed and resumed['frozen_target']['source_sha256'] != digest(args.source):
            raise ValueError('resume belongs to a different frozen target')
        q0 = np.array(resumed['coefficients'],float)
    grid = problem.prepare(problem.space.collocation(args.radial_order),np.arange(args.angles)*2*np.pi/args.angles)
    initial = problem.audit(q0,257,max(96,2*args.angles))
    derivative_checks = []
    if args.jacobian_check:
        for seed,epsilon in [(21,1e-7),(22,3e-8)]:
            v = np.random.default_rng(seed).normal(size=len(q0)); v /= np.linalg.norm(v)
            fd = (problem.residual(q0+epsilon*v,grid)-problem.residual(q0-epsilon*v,grid))/(2*epsilon)
            actual = problem.jacobian(q0,grid)@v
            for kind,mask in [('all',slice(None)),('curvature',slice(3,None,4))]:
                denominator = max(np.linalg.norm(fd[mask]),1e-30)
                derivative_checks.append({'kind':kind,'seed':seed,'epsilon':epsilon,
                    'relative_error':float(np.linalg.norm(fd[mask]-actual[mask])/denominator),
                    'maximum_absolute_error':float(np.max(abs(fd[mask]-actual[mask])))})
        print(json.dumps({'jacobian_checks':derivative_checks}),flush=True)
    count = [0]
    def fun(q):
        value = problem.residual(q,grid); count[0] += 1
        if count[0] % 10 == 1:
            d = problem.evaluate(q,grid)
            print(json.dumps({'evaluation':count[0],'rms':float(np.sqrt(np.mean(value**2))),
                'metric_component_max':float(np.max(abs(d['residual'][:,:,:3]))),
                'shape_frobenius_max':float(np.max(d['shape_frobenius'])),
                'seconds':time.monotonic()-started}),flush=True)
        return value
    if args.audit_only:
        rr = problem.residual(q0,grid)
        result = argparse.Namespace(x=q0,success=False,status=0,message='audit only',nfev=0,njev=0,cost=float(rr@rr)/2,optimality=None)
    else:
        result = least_squares(fun,q0,jac=lambda q:problem.jacobian(q,grid),method='lm',
                               max_nfev=args.max_nfev,ftol=1e-10,xtol=1e-10,gtol=1e-10,x_scale='jac')
    audits = [problem.audit(result.x,n,max(96,2*args.angles)) for n in args.audit_radials]
    report = {'schema':'eccentric-curvature-search-v1','status':'finite_fixed_target_tradeoff_only',
              'frozen_target':{'source_file':str(args.source),'source_sha256':digest(args.source),
                               'definition':'angular average of source-field E,F,G in the same fixed finite Fourier representation',
                               'average_quadrature_nodes':2*problem.space.modes+1,
                               'frozen_throughout_run':True,'continuous_certificate':False},
              'reference_meridian':source['reference_meridian'],'boundary':source['boundary'],
              'discretization':{'controls':problem.space.controls,'modes':problem.space.modes,
                                'radial_gauss_order':args.radial_order,'angular_points':args.angles},
              'curvature_penalty':{'quantity':'sqrt(4H^2-2K)=sqrt(kappa1^2+kappa2^2) from actual g and II',
                                   'limit':args.limit,'weight':args.weight,'constraint':'soft hinge; not a hard certificate'},
              'initial_audit':initial,'final_audits':audits,'jacobian_checks':derivative_checks,
              'solver':{'success':bool(result.success),'status':int(result.status),'message':result.message,
                         'nfev':int(result.nfev),'njev':int(result.njev or 0),'cost':float(result.cost),
                         'optimality':None if result.optimality is None else float(result.optimality)},
              'resume':str(args.resume) if args.resume else None,
              'coefficient_shape':list(problem.space.shape),'coefficients':result.x.tolist(),
              'elapsed_seconds':time.monotonic()-started,'script_sha256':digest(__file__),
              'base_script_sha256':digest(Path(__file__).with_name('eccentric_collar_search.py')),
              'claim':{'fixed_target':True,'fixed_metric_refinement_demonstrated':False,
                       'exact_isometry':False,'curvature_certified':False,'reach_certified':False,
                       'closed_family':False,'task_complete':False}}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'output':str(args.out),'final_audit':audits[-1],'seconds':report['elapsed_seconds']}),flush=True)


if __name__ == '__main__':
    main()
