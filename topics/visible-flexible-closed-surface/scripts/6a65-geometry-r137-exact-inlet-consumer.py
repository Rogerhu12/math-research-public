#!/usr/bin/env python3
"""Construct a NEW exact-form R137 inlet from an actual sampled cross-section.

The periodic Fourier curve is explicitly new data. Its exact arclength is
defined by an integral and numerical quadrature remains identified separately.
Frames and all derivatives are constructed from this one curve, not projected
independently. Existing R137 propagation/material inverse is reused unchanged.
No old non-flat neighbor is asserted to match the newly constructed two-jets.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import hashlib
import json
import math
import sys
import time
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fd2d_k0_ruling_coast import propagate, at_material, inlet_defects

ORDER = 6


def mul(a, b):
    shape = np.broadcast_shapes(a.shape[1:], b.shape[1:])
    out = np.zeros((ORDER+1,)+shape)
    for k in range(ORDER+1):
        for j in range(k+1):
            out[k] += a[j]*b[k-j]
    return out


def inv(a):
    out = np.zeros_like(a);out[0] = 1/a[0]
    for k in range(1, ORDER+1):
        out[k] = -sum(a[j]*out[k-j] for j in range(1, k+1))/a[0]
    return out


def sqrt(a):
    out = np.zeros_like(a);out[0] = np.sqrt(a[0])
    for k in range(1, ORDER+1):
        out[k] = (a[k]-sum((out[j]*out[k-j] for j in range(1, k)), np.zeros_like(a[0])))/(2*out[0])
    return out


def diff(a):
    out = np.zeros_like(a)
    for k in range(ORDER):
        out[k] = (k+1)*a[k+1]
    return out


def dot(a, b):
    return sum(mul(a[..., j], b[..., j]) for j in range(3))


def cross(a, b):
    return np.stack((mul(a[..., 1], b[..., 2])-mul(a[..., 2], b[..., 1]),
                     mul(a[..., 2], b[..., 0])-mul(a[..., 0], b[..., 2]),
                     mul(a[..., 0], b[..., 1])-mul(a[..., 1], b[..., 0])), axis=-1)


def scale(a, v):
    return mul(a[..., None], v)


class Curve:
    def __init__(self, points, degree, panels=128, gauss=16, planar=False):
        self.points = np.asarray(points)
        N = len(points)
        if degree < 3 or 2*degree >= N:
            raise ValueError('Need a strict Fourier truncation with degree >= 3')
        full = np.fft.fft(self.points, axis=0)/N
        self.modes = np.arange(-degree, degree+1)
        self.coeff = np.stack([full[k % N] for k in self.modes])
        for k in range(1, degree+1):
            c = (self.coeff[degree+k]+np.conj(self.coeff[degree-k]))/2
            self.coeff[degree+k] = c;self.coeff[degree-k] = np.conj(c)
        self.coeff[degree] = self.coeff[degree].real
        self.planar = bool(planar)
        if self.planar:
            self.coeff[self.modes != 0, 2] = 0
        self.degree, self.panels, self.gauss = degree, panels, gauss
        x, w = np.polynomial.legendre.leggauss(gauss)
        self.gx, self.gw = (x+1)/2, w/2
        self.cuts = np.linspace(0, 2*np.pi, panels+1)
        lo = self.cuts[:-1];length = np.diff(self.cuts)
        q = lo[:, None]+length[:, None]*self.gx
        speed = np.linalg.norm(self.derivative(q.ravel(), 1), axis=-1).reshape(q.shape)
        lengths = length*np.sum(speed*self.gw, axis=-1)
        self.cumulative = np.r_[0, np.cumsum(lengths)]
        self.perimeter = self.cumulative[-1];self.a = self.perimeter/(2*np.pi)

    def derivative(self, theta, order=0):
        theta = np.asarray(theta).reshape(-1)
        return (np.exp(1j*theta[:, None]*self.modes) @
                (self.coeff*(1j*self.modes[:, None])**order)).real

    def theta(self, u):
        u = np.asarray(u).reshape(-1)
        target = np.mod(u, 2*np.pi)*self.a
        cell = np.clip(np.searchsorted(self.cumulative, target, side='right')-1, 0, self.panels-1)
        lo, hi = self.cuts[cell], self.cuts[cell+1]
        t = lo+(target-self.cumulative[cell])/(self.cumulative[cell+1]-self.cumulative[cell])*(hi-lo)
        for _ in range(7):
            q = lo[:, None]+(t-lo)[:, None]*self.gx
            speed = np.linalg.norm(self.derivative(q.ravel(), 1), axis=-1).reshape(q.shape)
            arc = self.cumulative[cell]+(t-lo)*np.sum(speed*self.gw, axis=-1)
            residual = arc-target
            if np.max(np.abs(residual)) <= 2e-14:
                return t
            t -= residual/np.linalg.norm(self.derivative(t, 1), axis=-1)
            t = np.minimum(hi, np.maximum(lo, t))
        if np.max(np.abs(residual)) > 2e-12:
            raise RuntimeError('New arclength inverse did not converge')
        return t

    def inlet(self, u, v):
        u = np.asarray(u).reshape(-1);theta = self.theta(u)
        gamma = np.stack([self.derivative(theta, j)/math.factorial(j) for j in range(ORDER+1)])
        gp = diff(gamma);speed = sqrt(dot(gp, gp));recip = inv(speed)
        T = scale(recip, gp);lam = self.a*recip
        def Du(field):
            return scale(lam, diff(field)) if field.ndim == 3 else mul(lam, diff(field))
        Tu = Du(T);TuNorm = sqrt(dot(Tu, Tu));invTu = inv(TuNorm)
        U = scale(invTu, Tu);V = cross(T, U)
        ratio = v*invTu;one = np.zeros_like(ratio);one[0] = 1
        radicand = one-mul(ratio, ratio)
        if np.any(radicand[0] <= 0):
            raise ValueError('This new inlet fails the actual |T_u| > v condition')
        d = -scale(ratio, U)+scale(sqrt(radicand), V)
        N = cross(d, T);du = Du(d);duu = Du(du);Tuu = Du(Tu);Nu = Du(N)
        n = dot(Tu, N)/self.a;m = dot(du, N)/self.a
        nu, mu = Du(n), Du(m);nuu, muu = Du(nu), Du(mu)
        return dict(u=u,theta=theta,X=gamma[0],X_u=self.a*T[0],X_uu=self.a*Tu[0],
                    e1=d[0],e1_u=du[0],e1_uu=duu[0],e2=T[0],e2_u=Tu[0],e2_uu=Tuu[0],
                    N=N[0],N_u=Nu[0],n=n[0],m=m[0],n_u=nu[0],m_u=mu[0],n_uu=nuu[0],m_uu=muu[0],
                    tangentDerivativeNorm=TuNorm[0],curveSpeedBeforeNormalization=speed[0])


def normmax(a):
    return float(np.max(np.linalg.norm(a, axis=-1)))


def jsonable(x):
    if isinstance(x, np.ndarray):return x.tolist()
    if isinstance(x, np.generic):return x.item()
    raise TypeError(type(x).__name__)


def main():
    ap = argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('output_prefix')
    ap.add_argument('--degree', type=int, default=32);ap.add_argument('--v', type=float, default=.05)
    ap.add_argument('--planar', action='store_true', help='Explicit new curve: replace its z coordinate by the original average height')
    ap.add_argument('--angles', type=int, default=1024);ap.add_argument('--lengths', type=float, nargs='+', default=[.02,.05,.1,.2])
    args = ap.parse_args();start = time.time();prefix = Path(args.output_prefix)
    if Path(str(prefix)+'-report.json').exists():raise ValueError('Fresh output required')
    raw = json.loads(Path(args.input).read_text());old = raw['points']
    positions = np.asarray([p['X'] for p in old]);curve = Curve(positions,args.degree,planar=args.planar)
    old_u = np.asarray([p['u'] for p in old]);old_Xu = np.asarray([p['Xu'] for p in old]);old_Xuu = np.asarray([p['Xuu'] for p in old])
    data_old = curve.inlet(old_u,args.v);data = curve.inlet(2*np.pi*np.arange(args.angles)/args.angles,args.v)
    a,v = curve.a,args.v;n,m = data['n'],data['m'];k=m/n;ku=data['m_u']/n-m*data['n_u']/n**2
    B=v*(1+k*k)-ku;negative=B<0;wfocus=np.where(negative,a/np.maximum(-B,1e-300),np.inf)
    focus=np.where(negative,np.hypot(a/v+wfocus,wfocus*k)-a/v,np.inf)
    zero=propagate(a,v,0,data);oldzero=propagate(a,v,0,data_old)
    defects=inlet_defects(a,v,data)
    old_jets={'X':positions,'X_s':np.asarray([p['Xs'] for p in old]),'X_u':old_Xu,
              'X_ss':np.asarray([p['Xss'] for p in old]),'X_su':np.asarray([p['Xsu'] for p in old]),'X_uu':old_Xuu}
    mismatch={key:normmax(oldzero[key]-value) for key,value in old_jets.items()}
    reports=[];accepted=[];held=raw['actualCentralSupport'];marker=np.array([0,held,0]);G=data['e1']-k[:,None]*data['e2']
    for length in args.lengths:
        try:end=propagate(a,v,length,data)
        except ValueError as exc:reports.append({'length':length,'validFiniteDomain':False,'error':str(exc)});continue
        accepted.append(length);W=end['w'];D=end['D'];ideal0=n*(1+k*k);ideal1=a*n*(1+k*k)/D
        wheld=np.clip(-np.einsum('ij,ij->i',data['X']-marker,G)/np.einsum('ij,ij->i',G,G),0,W)
        nearest=data['X']+wheld[:,None]*G;both=np.concatenate((data['X'],end['X']))
        item={'length':length,'validFiniteDomain':True,'minimumD':float(min(a,np.min(D))),
              'maximumIdealRankOneCurvature':float(max(np.max(ideal0),np.max(ideal1))),
              'maximumActualEndpointCurvature':float(np.max(end['actual_curvature'])),
              'maximumActualEndpointMetricDefect':float(np.max(end['metric'])),
              'maximumRadiusWholeRulingsAtSampledAngles':float(np.max(np.linalg.norm(both,axis=-1))),
              'maximumAbsoluteYWholeRulingsAtSampledAngles':float(np.max(np.abs(both[:,1]))),
              'maximumAbsoluteZWholeRulingsAtSampledAngles':float(np.max(np.abs(both[:,2]))),
              'minimumHeldDistanceWholeRulingsAtSampledAngles':float(np.min(np.linalg.norm(nearest-marker,axis=-1))),
              'minimumOutwardSupportAtSampledAngles':float(np.min(-np.einsum('ij,ij->i',data['X'],data['N']))),
              'minimumMaterialDerivative':float(np.min(end['U_t']))}
        reports.append(item)
    selected=None;inverse_failures=[]
    for length in sorted(accepted,reverse=True):
        try:
            endpoint=at_material(a,v,length,data['u'],lambda u:curve.inlet(u,v))
        except (ValueError,RuntimeError) as exc:
            inverse_failures.append({'length':length,'error':str(exc)})
            continue
        selected=length
        np.savez_compressed(str(prefix)+'-endpoint.npz',**{key:value for key,value in endpoint.items() if isinstance(value,(np.ndarray,float,int,bool))})
        break
    np.savez_compressed(str(prefix)+'-inlet.npz',**{key:value for key,value in data.items() if isinstance(value,np.ndarray)},
                        curve_modes=curve.modes,curve_coefficients=curve.coeff,a=a,v=v)
    report={'schema':'6a65-R137-new-exact-form-arc-inlet-and-ruling-consumer-v1',
            'source':{'input':args.input,'inputSHA256':hashlib.sha256(Path(args.input).read_bytes()).hexdigest(),
                      'scriptSHA256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'parentStrongState':raw['source']},
            'newInputDefinition':'Finite real Fourier gamma; exact arclength u=2*pi*int|gamma_theta|/P; d=-v*Tu/|Tu|^2+sqrt(1-v^2/|Tu|^2)*(T cross Tu)/|Tu|',
            'oldParameterEntry':raw['oldEntry'],'physicalEntry':raw['s'],'degree':args.degree,'angles':args.angles,
            'explicitPlanarProjection':args.planar,'planarHeight':float(np.mean(positions[:,2])) if args.planar else None,
            'aNumerical':a,'v':v,'arcQuadrature':{'panels':curve.panels,'gauss':curve.gauss,'continuousRemainderCertified':False},
            'gammaProjectionPositionErrorAtOriginalSamples':normmax(curve.derivative(old_u)-positions),
            'gammaProjectionFirstDerivativeErrorAtOriginalSamples':normmax(curve.derivative(old_u,1)-old_Xu),
            'gammaProjectionSecondDerivativeErrorAtOriginalSamples':normmax(curve.derivative(old_u,2)-old_Xuu),
            'completeNewInletTwoJetDifferenceFromOld':mismatch,
            'minimumTangentDerivativeNorm':float(np.min(data['tangentDerivativeNorm'])),
            'minimumN':float(np.min(n)),'maximumAbsM':float(np.max(np.abs(m))),
            'maximumAbsKratio':float(np.max(np.abs(k))),'maximumAbsKratioDerivative':float(np.max(np.abs(ku))),
            'minimumB':float(np.min(B)),'minimumSampledPhysicalFocusDistance':float(np.min(focus)),
            'newExactFormInletDefectsNumerical':{key:float(np.max(np.abs(value))) for key,value in defects.items()},
            'newExactFormInletMetricDefectNumerical':float(np.max(zero['metric'])),
            'newInletMaximumCurvature':float(np.max(zero['actual_curvature'])),
            'coasts':reports,'savedEndpointLength':selected,'materialInverseFailures':inverse_failures,'seconds':time.time()-start,
            'newFlatMetric':'d_sigma^2+(a+v*sigma)^2 du^2; rho exactly zero on this new segment; clock supported outside',
            'oldNeighborTwoJetsNotMatched':True,'wholeClosedSurfaceNotConstructed':True,
            'continuousAngleDomainCertificate':False,'nonlocalReachNotCertified':True}
    prefix.parent.mkdir(parents=True,exist_ok=True)
    Path(str(prefix)+'-report.json').write_text(json.dumps(report,indent=2,default=jsonable)+'\n')
    print(json.dumps(report,default=jsonable))


if __name__=='__main__':main()
