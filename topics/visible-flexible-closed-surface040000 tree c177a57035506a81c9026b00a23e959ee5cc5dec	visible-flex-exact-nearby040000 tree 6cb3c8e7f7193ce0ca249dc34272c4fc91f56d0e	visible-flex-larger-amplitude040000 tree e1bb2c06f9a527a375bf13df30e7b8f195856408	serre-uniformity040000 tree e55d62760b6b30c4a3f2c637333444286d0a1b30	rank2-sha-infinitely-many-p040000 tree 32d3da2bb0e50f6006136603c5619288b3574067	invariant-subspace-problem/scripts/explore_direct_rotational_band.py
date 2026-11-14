#!/usr/bin/env python3
"""Exploratory direct-coordinate rotational-metric solver, never an acceptance certificate.

The map is F=(r+u)e_r+v e_theta+(H+w)e_z. Even angular modes and
open-knot quintic radial B-splines enforce reflection symmetry and exact C2
zero nonradial jets at both ends. The mode-two central height is fixed by
linear elimination, not a soft penalty. The radial target coefficient is
allowed to vary in this exploratory search; a candidate must subsequently
freeze its entire metric before any convergence claim.
"""
import argparse
import json
import os
from pathlib import Path
import time

os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('OMP_NUM_THREADS', '1')
import numpy as np
from scipy.interpolate import BSpline
from scipy.optimize import least_squares
from scipy.sparse import csr_matrix, diags, eye, hstack, kron, vstack


def profile(r, a, b, height, ripple):
    x = (r-a)/(b-a)
    L = b-a
    s = 10*x**3-15*x**4+6*x**5
    sp = 30*x**2-60*x**3+30*x**4
    spp = 60*x-180*x**2+120*x**3
    p = np.pi*x
    f = np.sin(p)**4
    fp = 4*np.pi*np.sin(p)**3*np.cos(p)
    fpp = 4*np.pi**2*(3*np.sin(p)**2*np.cos(p)**2-np.sin(p)**4)
    q, qp, qpp = np.sin(4*p), 4*np.pi*np.cos(4*p), -16*np.pi**2*np.sin(4*p)
    return (height*s+ripple*f*q,
            (height*sp+ripple*(fp*q+f*qp))/L,
            (height*spp+ripple*(fpp*q+2*fp*qp+f*qpp))/L**2)


class Band:
    def __init__(self, cells=14, modes=4, a=.25, b=.95, amplitude=.10,
                 height=.25, ripple=.025, radial_order=4, angular=None,
                 vary_mean=False, hessian_limit=0., hessian_weight=10.):
        self.cells, self.modes = cells, modes
        self.a, self.b, self.amplitude = a, b, amplitude
        self.height, self.ripple, self.vary_mean = height, ripple, vary_mean
        self.hessian_limit,self.hessian_weight=hessian_limit,hessian_weight
        self.degree = 5
        self.knots = np.r_[np.repeat(a,6),np.linspace(a,b,cells+1)[1:-1],np.repeat(b,6)]
        self.nall = len(self.knots)-6
        self.keep = np.arange(3,self.nall-3)
        self.n = len(self.keep)
        self.blocks = [('u',m) for m in range(0,2*modes+1,2)]
        self.blocks += [('v',m) for m in range(2,2*modes+1,2)]
        self.blocks += [('w',m) for m in range(2,2*modes+1,2)]
        if vary_mean:
            self.blocks += [('h',0)]
        self.nfull = self.n*len(self.blocks)
        self.pivot_block = self.blocks.index(('w',2))
        bc = self.basis(np.array([(a+b)/2]))[0][0]
        p = int(np.argmax(bc))
        self.pivot = self.pivot_block*self.n+p
        self.free = np.delete(np.arange(self.nfull),self.pivot)
        rows,cols,vals = list(self.free),list(range(self.nfull-1)),[1.]*(self.nfull-1)
        for j,c in enumerate(self.free):
            if c//self.n==self.pivot_block:
                rows.append(self.pivot);cols.append(j);vals.append(-bc[c%self.n]/bc[p])
        self.T=csr_matrix((vals,(rows,cols)),shape=(self.nfull,self.nfull-1))
        self.c0=np.zeros(self.nfull);self.c0[self.pivot]=amplitude/bc[p]
        gx,gw=np.polynomial.legendre.leggauss(radial_order)
        edges=np.linspace(a,b,cells+1)
        self.r=np.concatenate([(x+y)/2+(y-x)*gx/2 for x,y in zip(edges[:-1],edges[1:])])
        self.theta=np.linspace(0,2*np.pi,angular or max(32,8*modes+8),endpoint=False)
        self.ops=self.operators(self.r,self.theta)
        self.nr,self.nt=len(self.r),len(self.theta)
        self.sz=self.nr*self.nt
        self.project=kron(eye(self.nr,format='csr'),eye(self.nt,format='csr')-csr_matrix(np.full((self.nt,self.nt),1/self.nt)),format='csr')
        hp=profile(self.r,a,b,height,ripple)[1]
        self.scaleE=np.repeat(1/(1+hp**2),self.nt)
        self.scaleF=np.repeat(1/(self.r*np.sqrt(1+hp**2)),self.nt)
        self.scaleG=np.repeat(1/self.r**2,self.nt)
        self.jac_checks={}

    def basis(self,r):
        bs=BSpline(self.knots,np.eye(self.nall),5,extrapolate=False)
        return [bs.derivative(k)(r)[:,self.keep] for k in (0,1,2)]

    def operators(self,r,theta):
        B,B1,B2=self.basis(r)
        z=csr_matrix((len(r)*len(theta),self.n))
        out={k:[] for k in ['p0','p1','p2','r0','r1','r2','t0','t1','t2','rr0','rr1','rr2','rt0','rt1','rt2','tt0','tt1','tt2']}
        for kind,m in self.blocks:
            c,s=np.cos(m*theta),np.sin(m*theta)
            def K(b,t):return kron(csr_matrix(b),csr_matrix(t[:,None]),format='csr')
            p=[z,z,z];dr=[z,z,z];dt=[z,z,z];drr=[z,z,z];drt=[z,z,z];dtt=[z,z,z]
            if kind=='u':
                p[0]=K(B,c);dr[0]=K(B1,c);dt[0]=K(B,-m*s);dt[1]=K(B,c)
                drr[0]=K(B2,c);drt[0]=K(B1,-m*s);drt[1]=K(B1,c)
                dtt[0]=K(B,-(m*m+1)*c);dtt[1]=K(B,-2*m*s)
            elif kind=='v':
                p[1]=K(B,s);dr[1]=K(B1,s);dt[0]=K(B,-s);dt[1]=K(B,m*c)
                drr[1]=K(B2,s);drt[0]=K(B1,-s);drt[1]=K(B1,m*c)
                dtt[0]=K(B,-2*m*c);dtt[1]=K(B,-(m*m+1)*s)
            else:
                p[2]=K(B,c);dr[2]=K(B1,c);dt[2]=K(B,-m*s)
                drr[2]=K(B2,c);drt[2]=K(B1,-m*s);dtt[2]=K(B,-m*m*c)
            for pre,arr in [('p',p),('r',dr),('t',dt),('rr',drr),('rt',drt),('tt',dtt)]:
                for k in range(3):out[pre+str(k)].append(arr[k])
        mats={k:hstack(v,format='csr') for k,v in out.items()}
        H,Hp,Hpp=profile(np.array(r),self.a,self.b,self.height,self.ripple)
        R=np.repeat(r,len(theta));Z=np.repeat(H,len(theta));Zr=np.repeat(Hp,len(theta));Zrr=np.repeat(Hpp,len(theta))
        zero=np.zeros_like(R);one=np.ones_like(R)
        bases={'p':[R,zero,Z],'r':[one,zero,Zr],'t':[zero,R,zero],
               'rr':[zero,zero,Zrr],'rt':[zero,one,zero],'tt':[-R,zero,zero]}
        return mats,bases

    def full(self,x):return self.c0+self.T@x

    def evaluate(self,c,ops=None):
        mats,bases=ops or self.ops
        return {pre:np.stack([bases[pre][i]+mats[pre+str(i)]@c for i in range(3)],axis=1)
                for pre in ['p','r','t','rr','rt','tt']}

    def initial(self):
        rr=np.linspace(self.a,self.b,300)
        B=self.basis(rr)[0]
        f=np.sin(np.pi*(rr-self.a)/(self.b-self.a))**4
        wc=np.linalg.lstsq(B,self.amplitude*f,rcond=None)[0]
        c=np.zeros(self.nfull);c[self.pivot_block*self.n:(self.pivot_block+1)*self.n]=wc
        return c[self.free]

    def residual(self,x):
        e=self.evaluate(self.full(x))
        R,T=e['r'],e['t']
        E=np.einsum('ij,ij->i',R,R);F=np.einsum('ij,ij->i',R,T);G=np.einsum('ij,ij->i',T,T)
        residual=np.r_[self.scaleE*(self.project@E),self.scaleF*F,self.scaleG*(G-np.repeat(self.r**2,self.nt))]
        if self.hessian_limit>0:
            rr=np.repeat(self.r,self.nt)[:,None]
            hs=[e['rr'],e['rt']/rr-e['t']/rr**2,e['tt']/rr**2+e['r']/rr]
            residual=np.r_[residual,*[self.hessian_weight*np.maximum(0,np.sum(h*h,axis=1)/self.hessian_limit**2-1) for h in hs]]
        return residual

    def jacobian(self,x):
        mats,_=self.ops
        e=self.evaluate(self.full(x));R,T=e['r'],e['t']
        ER=sum((diags(2*R[:,i])@mats['r'+str(i)] for i in range(3)))
        FR=sum((diags(T[:,i])@mats['r'+str(i)]+diags(R[:,i])@mats['t'+str(i)] for i in range(3)))
        GR=sum((diags(2*T[:,i])@mats['t'+str(i)] for i in range(3)))
        rows=[diags(self.scaleE)@self.project@ER,diags(self.scaleF)@FR,diags(self.scaleG)@GR]
        if self.hessian_limit>0:
            rr=np.repeat(self.r,self.nt)
            hs=[e['rr'],e['rt']/rr[:,None]-e['t']/rr[:,None]**2,e['tt']/rr[:,None]**2+e['r']/rr[:,None]]
            hmat=[[mats['rr'+str(i)] for i in range(3)],
                  [diags(1/rr)@mats['rt'+str(i)]-diags(1/rr**2)@mats['t'+str(i)] for i in range(3)],
                  [diags(1/rr**2)@mats['tt'+str(i)]+diags(1/rr)@mats['r'+str(i)] for i in range(3)]]
            for h,hm in zip(hs,hmat):
                active=(np.sum(h*h,axis=1)>self.hessian_limit**2).astype(float)
                rows.append(diags(2*self.hessian_weight*active/self.hessian_limit**2)@sum(diags(h[:,i])@hm[i] for i in range(3)))
        return vstack(rows,format='csr')@self.T

    def check_jacobian(self,x):
        rng=np.random.default_rng(20261108);v=rng.normal(size=len(x));v/=np.linalg.norm(v)
        jv=self.jacobian(x)@v
        self.jac_checks={str(h):float(np.linalg.norm((self.residual(x+h*v)-self.residual(x-h*v))/(2*h)-jv)/max(np.linalg.norm(jv),1e-15)) for h in [1e-4,1e-5,1e-6]}
        return self.jac_checks

    def diagnostic(self,x,dense_factor=3):
        rr=np.linspace(self.a,self.b,self.cells*8*dense_factor+1)
        th=np.linspace(0,2*np.pi,len(self.theta)*dense_factor,endpoint=False)
        e=self.evaluate(self.full(x),self.operators(rr,th))
        R,T=e['r'],e['t'];E=np.sum(R*R,axis=1);F=np.sum(R*T,axis=1);G=np.sum(T*T,axis=1)
        em=E.reshape(len(rr),len(th)).mean(axis=1);es=np.repeat(em,len(th));gs=np.repeat(rr**2,len(th))
        z11=(E-es)/es;z12=F/np.sqrt(es*gs);z22=(G-gs)/gs
        eig=np.maximum(np.abs((z11+z22)/2+np.sqrt(((z11-z22)/2)**2+z12*z12)),np.abs((z11+z22)/2-np.sqrt(((z11-z22)/2)**2+z12*z12)))
        cross=np.cross(R,T);area=np.linalg.norm(cross,axis=1);N=cross/area[:,None]
        l=np.sum(e['rr']*N,axis=1);m=np.sum(e['rt']*N,axis=1);n=np.sum(e['tt']*N,axis=1)
        det=E*G-F*F;H=(G*l-2*F*m+E*n)/(2*det);K=(l*n-m*m)/det
        kmax=np.max(np.abs(H)+np.sqrt(np.maximum(0,H*H-K)))
        p=e['p'];rho=np.sqrt(p[:,0]**2+p[:,1]**2)
        polarJ=p[:,0]*T[:,1]-p[:,1]*T[:,0]
        rrvec=np.repeat(rr,len(th))[:,None]
        hs=[e['rr'],e['rt']/rrvec-e['t']/rrvec**2,e['tt']/rrvec**2+e['r']/rrvec]
        return {'max_relative_metric_spectral_defect':float(eig.max()),'max_E_nonmean_relative':float(np.max(np.abs(z11))),
                'max_F_relative':float(np.max(np.abs(z12))),'max_G_relative':float(np.max(np.abs(z22))),
                'max_abs_principal_curvature_sampled':float(kmax),'minimum_curvature_radius_sampled':float(1/kmax),
                'min_gram_determinant_sampled':float(det.min()),'min_polar_angular_jacobian_sampled':float(polarJ.min()),
                'radial_range_sampled':[float(rho.min()),float(rho.max())],
                'height_range_sampled':[float(p[:,2].min()),float(p[:,2].max())],
                'max_cartesian_domain_hessian_components_sampled':[float(np.linalg.norm(h,axis=1).max()) for h in hs],
                'dense_grid':[len(rr),len(th)],'amplitude_fixed':self.amplitude,
                'reach_certified':False,'closed_surface':False,'fixed_metric_refinement':False}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--cells',type=int,default=12);ap.add_argument('--modes',type=int,default=3)
    ap.add_argument('--amplitude',type=float,default=.06);ap.add_argument('--height',type=float,default=.25)
    ap.add_argument('--ripple',type=float,default=.025);ap.add_argument('--vary-mean',action='store_true')
    ap.add_argument('--hessian-limit',type=float,default=0.);ap.add_argument('--hessian-weight',type=float,default=10.)
    ap.add_argument('--max-nfev',type=int,default=100);ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    band=Band(cells=args.cells,modes=args.modes,amplitude=args.amplitude,height=args.height,ripple=args.ripple,vary_mean=args.vary_mean,hessian_limit=args.hessian_limit,hessian_weight=args.hessian_weight)
    x=band.initial();check=band.check_jacobian(x)
    before=band.diagnostic(x,1)
    start=time.monotonic()
    result=least_squares(band.residual,x,jac=band.jacobian,method='trf',tr_solver='lsmr',
                         tr_options={'atol':1e-11,'btol':1e-11,'maxiter':250},
                         ftol=1e-12,xtol=1e-12,gtol=1e-10,max_nfev=args.max_nfev,x_scale='jac',verbose=0)
    after=band.diagnostic(result.x,2)
    report={'purpose':'exploration only; not an exact-isometry or reach certificate',
            'arguments':{k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},
            'unknowns':len(x),'residuals':len(band.residual(x)),'jacobian_directional_checks':check,
            'initial':before,'final':after,'solver':{'success':bool(result.success),'message':result.message,'nfev':result.nfev,'cost':float(result.cost),'optimality':float(result.optimality)},
            'elapsed_seconds':time.monotonic()-start,'numpy':np.__version__}
    np.savez_compressed(args.out/'checkpoint.npz',coefficients=band.full(result.x),free_variables=result.x,knots=band.knots,blocks=np.array(band.blocks,dtype=str),radial_grid=band.r,theta=band.theta)
    (args.out/'summary.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
