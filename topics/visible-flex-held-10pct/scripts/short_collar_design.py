#!/usr/bin/env python3
"""Design a new C2 circular collar for an existing noncircular prefix.

This is a finite nonlinear experiment. It designs a new meridian metric;
it is not a fixed-metric refinement, an existence proof, or a reach proof.
The input contains the original endpoint's actual Cartesian two-jet.
All endpoint Fourier coefficients are retained (also above correction m).
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import hashlib
import json
import time
from pathlib import Path
import numpy as np
from scipy.interpolate import BSpline
from scipy.optimize import least_squares


class Collar:
    def __init__(self, trace, length=.65, rise=.25, radius=.15, nc=16, m=8,
                 free_E=False):
        self.length, self.rise, self.radius = length, rise, radius
        self.nc, self.m, self.free_E = nc, m, free_E
        self.shape = (nc - 6, 3*m)
        self.size = (nc - 6)*3*m
        self.odd = np.arange(1, 2*m, 2)
        self.even = np.arange(0, 2*m, 2)
        self.trace = trace
        self.z0 = float(trace['X'][:, 2].mean())
        self.z1 = self.z0 + rise
        self.coeff = [np.fft.fft(trace[k], axis=0)/len(trace[k])
                      for k in ('X', 'Xs', 'Xss')]
        self.freq = np.fft.fftfreq(len(trace['X']), 1/len(trace['X']))
        knots = np.r_[np.zeros(6), np.linspace(0, 1, nc-4)[1:-1], np.ones(6)]
        self.spline = BSpline(knots, np.eye(nc), 5, extrapolate=False)
        self.intervals = np.unique(knots)

    def angles(self, u):
        base = np.zeros((len(u), 3*self.m, 3)); first = base.copy(); second = base.copy()
        for part, component, modes, trig in ((0, 0, self.odd, 'cos'),
                                            (1, 1, self.odd, 'sin'),
                                            (2, 2, self.even, 'cos')):
            sl = slice(part*self.m, (part+1)*self.m)
            v = u[:, None]*modes
            if trig == 'cos':
                base[:, sl, component] = np.cos(v)
                first[:, sl, component] = -modes*np.sin(v)
                second[:, sl, component] = -modes**2*np.cos(v)
            else:
                base[:, sl, component] = np.sin(v)
                first[:, sl, component] = modes*np.cos(v)
                second[:, sl, component] = -modes**2*np.sin(v)
        return base, first, second

    def prepare(self, s, u):
        s, u = np.asarray(s), np.asarray(u)
        # Six quintic endpoint jets: start/end value, first and second derivative.
        polynomials = [
            [1,0,0,-10,15,-6], [0,1,0,-6,8,-3], [0,0,.5,-1.5,1.5,-.5],
            [0,0,0,10,-15,6], [0,0,0,-4,7,-3], [0,0,0,.5,-1,.5]]
        H = [[np.polynomial.polynomial.polyval(s, np.polynomial.polynomial.polyder(p,d))
              for p in polynomials] for d in range(3)]
        start = [[np.real(np.exp(1j*u[:,None]*self.freq) @
                          (c*(1j*self.freq[:,None])**du))
                  for du in range(3)] for c in self.coeff]
        er = np.stack((np.cos(u),np.sin(u),np.zeros_like(u)), axis=-1)
        et = np.stack((-np.sin(u),np.cos(u),np.zeros_like(u)), axis=-1)
        circ = (er, et, -er)
        orders = [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]
        base = []
        for ds,du in orders:
            endpoint = self.radius*circ[du]
            if du == 0:
                endpoint = endpoint + np.array([0.,0.,self.z1])
            value = sum(H[ds][j][:,None,None] * self.length**j * start[j][du]
                        for j in range(3))
            value += H[ds][3][:,None,None]*endpoint
            value -= H[ds][4][:,None,None]*self.length*circ[du]
            base.append(value)
        return dict(s=s,u=u,base=base,
                    radial=[self.spline.derivative(d)(s)[:,3:-3] for d in range(3)],
                    angle=self.angles(u))

    def geometry(self, q, g, second=False):
        coeff = np.asarray(q).reshape(self.shape)
        orders = [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]
        return [g['base'][i] + np.einsum('sj,ucd,jc->sud',g['radial'][a],
                                       g['angle'][b],coeff,optimize=True)
                for i,(a,b) in enumerate(orders[:6 if second else 3])]

    def residual(self, q, g, jac=False):
        x,fs,fu = self.geometry(q,g)
        e = np.sum(fs*fs,-1); f = np.sum(fs*fu,-1); gg = np.sum(fu*fu,-1)
        me = e.mean(1,keepdims=True) if self.free_E else np.full((len(e),1),self.length**2)
        mg = np.maximum(gg.mean(1,keepdims=True),1e-20)
        r = np.stack((e/me-1, np.sqrt(2)*f/np.sqrt(me*mg), gg/mg-1),axis=-1)
        rho = np.sqrt(np.sum(x[:,:,:2]**2,-1))
        # Shape bounds are design aids. Dense post-evaluation reports violations.
        br = np.maximum(rho-.8,0)
        bz_hi = np.maximum(x[:,:,2]-(self.z1+.05),0)
        bz_lo = np.maximum(self.z0-.1-x[:,:,2],0)
        floor = np.maximum(.005-mg[:,0],0)
        if not jac:
            return np.r_[r.ravel(), br.ravel(), bz_hi.ravel(), bz_lo.ravel(), 10*floor]
        B = [g['radial'][a][:,None,:,None,None]*g['angle'][b][None,:,None,:,:]
             for a,b in ((0,0),(1,0),(0,1))]
        Bx,Bs,Bu = B
        de = 2*np.sum(fs[:,:,None,None,:]*Bs,-1)
        df = np.sum(fu[:,:,None,None,:]*Bs+fs[:,:,None,None,:]*Bu,-1)
        dg = 2*np.sum(fu[:,:,None,None,:]*Bu,-1)
        dme = de.mean(1,keepdims=True) if self.free_E else np.zeros_like(de[:,:1])
        dmg = dg.mean(1,keepdims=True)
        ME,MG = me[:,:,None,None],mg[:,:,None,None]
        je = de/ME-e[:,:,None,None]*dme/ME**2
        jf = np.sqrt(2)*df/np.sqrt(ME*MG)-r[:,:,1,None,None]*.5*(dme/ME+dmg/MG)
        jg = dg/MG-gg[:,:,None,None]*dmg/MG**2
        j = np.stack((je,jf,jg),axis=2).reshape(-1,self.size)
        drho = np.sum(x[:,:,None,None,:2]*Bx[:,:,:,:,:2],-1)/np.maximum(rho,1e-20)[:,:,None,None]
        jr = drho*(br>0)[:,:,None,None]
        jhi = Bx[:,:,:,:,2]*(bz_hi>0)[:,:,None,None]
        jlo = -Bx[:,:,:,:,2]*(bz_lo>0)[:,:,None,None]
        jfloor = -10*dmg[:,0]*(floor>0)[:,None,None]
        return np.r_[j,jr.reshape(-1,self.size),jhi.reshape(-1,self.size),
                     jlo.reshape(-1,self.size),jfloor.reshape(-1,self.size)]

    def audit(self,q,n=201,nu=256):
        g = self.prepare(np.linspace(0,1,n),2*np.pi*np.arange(nu)/nu)
        x,fs,fu,fss,fsu,fuu = self.geometry(q,g,True)
        e=np.sum(fs*fs,-1);f=np.sum(fs*fu,-1);gg=np.sum(fu*fu,-1)
        me=e.mean(1,keepdims=True) if self.free_E else self.length**2
        mg=gg.mean(1,keepdims=True)
        a=e/me-1;b=f/np.sqrt(me*mg);d=gg/mg-1
        metric=np.abs((a+d)/2)+np.sqrt((a-d)**2/4+b*b)
        cross=np.cross(fu,fs);area=np.linalg.norm(cross,axis=-1)
        normal=cross/np.maximum(area,1e-30)[:,:,None]
        l=np.sum(fss*normal,-1);m=np.sum(fsu*normal,-1);nn=np.sum(fuu*normal,-1)
        det=e*gg-f*f;H=(l*gg-2*m*f+nn*e)/(2*det);K=(l*nn-m*m)/det
        kappa=np.abs(H)+np.sqrt(np.maximum(H*H-K,0))
        support=np.sum(x*normal,-1)
        return dict(scope='finite samples of a designed new metric, not a proof',grid=[n,nu],
                    metric_max=float(metric.max()),curvature_max=float(kappa.max()),
                    support_min=float(support.min()),area_min=float(area.min()),
                    E_range=[float(e.min()),float(e.max())],G_range=[float(gg.min()),float(gg.max())],
                    z_range=[float(x[:,:,2].min()),float(x[:,:,2].max())],
                    radius_max=float(np.linalg.norm(x[:,:,:2],axis=-1).max()),
                    ball_radius_max=float(np.linalg.norm(x,axis=-1).max()))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--trace',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--length',type=float,default=.65);ap.add_argument('--rise',type=float,default=.25)
    ap.add_argument('--radius',type=float,default=.15);ap.add_argument('--nc',type=int,default=16)
    ap.add_argument('--m',type=int,default=8);ap.add_argument('--nfev',type=int,default=120)
    ap.add_argument('--free-E',action='store_true');ap.add_argument('--seed',type=Path)
    args=ap.parse_args();trace=dict(np.load(args.trace))
    obj=Collar(trace,length=args.length,rise=args.rise,radius=args.radius,nc=args.nc,m=args.m,free_E=args.free_E)
    nodes,_=np.polynomial.legendre.leggauss(5)
    s=np.concatenate([a+(b-a)*(nodes+1)/2 for a,b in zip(obj.intervals[:-1],obj.intervals[1:])])
    g=obj.prepare(s,2*np.pi*np.arange(max(64,8*args.m))/max(64,8*args.m))
    q=np.zeros(obj.size) if args.seed is None else np.array(json.loads(args.seed.read_text())['q'])
    start=time.monotonic();count=0
    def fun(q):
        nonlocal count
        r=obj.residual(q,g);count+=1
        if count%10==1:
            print(json.dumps(dict(eval=count,rms=float(np.sqrt(np.mean(r*r))),
                                  maximum=float(abs(r).max()),seconds=time.monotonic()-start)),flush=True)
        return r
    res=least_squares(fun,q,jac=lambda v:obj.residual(v,g,True),method='lm',max_nfev=args.nfev,
                      ftol=1e-11,xtol=1e-11,gtol=1e-11,x_scale='jac')
    data=dict(parameters={k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},
              trace_sha256=hashlib.sha256(args.trace.read_bytes()).hexdigest(),q=res.x.tolist(),
              success=bool(res.success),message=res.message,nfev=res.nfev,cost=res.cost,
              seconds=time.monotonic()-start,audit=obj.audit(res.x))
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k!='q'}),flush=True)

if __name__=='__main__':
    main()
