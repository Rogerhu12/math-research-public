#!/usr/bin/env python3
"""R150 full angular-function prototype; finite radial quadrature only.

No angular FFT, projection, or boundary truncation is used. The prototype
reports its Gauss and formal curvature defects and is not a nonlinear solve.
Radial checks use a second rule on exactly the first rule's controls.
"""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse,json,pathlib,time,resource,hashlib
from math import comb
import numpy as np
from scipy.special import betainc
from fd2d_codazzi_moment_lifting_probe import identity,s5,rule_tables,primitive
from fd2d_gc_radial_bump_profile import RadialBumpProfile
from fd2d_balanced_curvature_core import FixedBalancedGeometry,BalancedCurvatureCore
from fd2d_positive_flat_developable_family import PositiveFlatDevelopableFamily,primitive_weights


class FullFunctionMomentProbe:
    def __init__(self,candidate,state,*,max_step=.0125):
        with np.load(state,allow_pickle=False) as z:
            p=z['parameters'].copy();K=int(z['modes']);supports=z['profile_supports'].copy()
        self.parameters=p;self.K=K
        self.profile=RadialBumpProfile(candidate,supports=supports,coefficients=p[2*K+1:])
        self.geometry=FixedBalancedGeometry();self.core=BalancedCurvatureCore(p[:K],geometry=self.geometry)
        self.tail=PositiveFlatDevelopableFamily(coefficients=p[K:2*K+1],
            cut_radius=.8,cuff_radius=.32,flat_radius=.34,plane_height=1.25)
        self.C,self.L=float(self.profile.central_end),float(self.profile.end)
        self.aC,self.aL=[float(self.profile.jet([x])['a'][0]) for x in (self.C,self.L)]
        self.control_left=self.C+.001;self.control_right=self.L-.001;self.ramp=.01
        self.tail_start=.42*self.L
        br=np.unique(np.r_[self.profile.breaks,self.control_left,self.control_left+self.ramp,
            self.control_right-self.ramp,self.control_right,self.tail_start,self.C,self.L])
        br=br[(br>=self.C)&(br<=self.L)]
        self.breaks=np.unique(np.concatenate([np.linspace(l,r,max(1,int(np.ceil((r-l)/max_step)))+1)
            for l,r in zip(br[:-1],br[1:])]))

    def angular(self,u):
        u=np.asarray(u,float);geom=self.geometry;phi=geom.normal_angle(u)
        rho=geom.radius(phi);rp=geom.radius_derivative(phi)
        th=np.tanh(geom.k*(np.cos(2*phi)-geom.c))
        rpp=(2*geom.D*geom.k*np.cos(2*phi)*(1-th*th)
            +4*geom.D*geom.k**2*np.sin(2*phi)**2*th*(1-th*th)
            -4*geom.u2*np.cos(2*phi)-16*geom.u4*np.cos(4*phi))
        core=self.core.curvature(phi);nc=core['n'];nphi=core['n_phi']
        npp=2*rp**2/rho**3-rpp/rho**2-np.cos(phi[:,None]*self.core.modes)@(self.core.modes**2*self.core.d)
        ncu=geom.a0/rho*nphi
        ncuu=(geom.a0/rho)**2*(npp-rp/rho*nphi)
        nc,ncu,ncuu=(np.asarray(x,float) for x in (nc,ncu,ncuu))
        sn,cs=np.sin(u),np.cos(u);r=self.aL;y=r*sn
        jets=self.tail.angle_jets(y);kap,ky=jets['kappa'],jets['kappa_y']
        q=np.clip((abs(y)-self.tail.flat_radius)/self.tail.width,0.,1.)
        inside=(abs(y)>self.tail.flat_radius)&(abs(y)<self.tail.cut_radius)
        degree=self.tail.parameter_count-1;weights,_=primitive_weights(degree)
        kyy=np.zeros_like(u);anti=np.zeros_like(u)
        for i,p in enumerate(self.tail.coefficients):
            aa,bb=i+4,degree-i+4;scale=630*comb(degree,i)
            second=scale*(aa*(aa-1)*q**(aa-2)*(1-q)**bb
                -2*aa*bb*q**(aa-1)*(1-q)**(bb-1)+bb*(bb-1)*q**aa*(1-q)**(bb-2))
            kyy+=p*np.where(inside,second/self.tail.width**3,0.)
            anti+=p*weights[i]*(self.tail.flat_radius*betainc(i+5,degree-i+5,q)
                +self.tail.width*(i+5)/(degree+10)*betainc(i+6,degree-i+5,q))
        nl=kap*cs*cs;ml=-kap*sn*cs;ll=kap*sn*sn
        nlu=r*ky*cs**3-2*kap*sn*cs
        mlu=-r*ky*sn*cs**2-kap*(cs**2-sn**2)
        llu=r*ky*cs*sn**2+2*kap*sn*cs
        nluu=r*r*kyy*cs**4-5*r*ky*sn*cs**2-2*kap*(cs**2-sn**2)
        lluu=r*r*kyy*cs**2*sn**2+r*ky*(-sn**3+4*sn*cs**2)+2*kap*(cs**2-sn**2)
        Phi=np.stack((-anti,r*nl-self.aC*nc,ll),axis=-1)
        Phiu=np.stack((r*r*ml,r*nlu-self.aC*ncu,llu),axis=-1)
        Phiuu=np.stack((r*r*mlu,r*nluu-self.aC*ncuu,lluu),axis=-1)
        return dict(Phi=Phi,Phiu=Phiu,Phiuu=Phiuu,nC=nc,
            right=np.stack((nl,ml,ll),axis=-1))

    def grid(self,order):
        x,w,anti=rule_tables(order);widths=np.diff(self.breaks)
        points=(self.breaks[:-1,None]+widths[:,None]*(x+1)/2).ravel()
        jet=self.profile.jet(points);a,ap=jet['a'],jet['a_s'];first,I=primitive(a**-2,widths,w,anti)
        J=I-first;c=ap/a;b=s5((points-self.control_left)/self.ramp)*s5((self.control_right-points)/self.ramp)
        chi=s5((points-self.tail_start)/(self.L-self.tail_start));f=np.stack((np.ones_like(a),J,c),axis=-1)
        W=(widths[:,None]*w[None,:]/2).ravel()
        return dict(order=order,x=points,a=a,ap=ap,K=jet['K'],J=J,I=I,b=b,chi=chi,f=f,
            weights=W,widths=widths,gauss_weights=w,anti=anti)

    def controls(self,g):
        W,a,b,f,chi=(g[k] for k in ('weights','a','b','f','chi'))
        H=f.T@((W*a*b)[:,None]*f);d=(W*a*chi)@f
        targets=np.stack((np.array([1.,0.,0.]),np.array([0.,0.,1.]),-d),axis=-1)
        coeff=np.linalg.solve(H,targets)
        return dict(H=H,baseline_moments=d,coefficients=coeff)

    def consume(self,g,p,ang):
        a,ap=g['a'],g['ap'];ell=g['b'][:,None]*(g['f']@p['coefficients']);ell[:,2]+=g['chi']
        prim,totalAl=primitive(a[:,None]*ell,g['widths'],g['gauss_weights'],g['anti'])
        M=prim/a[:,None]**2
        intap,totalap=primitive(ap[:,None]*ell,g['widths'],g['gauss_weights'],g['anti'])
        intM,totalM=primitive(M,g['widths'],g['gauss_weights'],g['anti'])
        R=intap/a[:,None];S=intM/a[:,None]
        rightm=(totalAl/self.aL**2)@ang['Phiu'].T
        rightn=self.aC/self.aL*ang['nC']+(totalap/self.aL)@ang['Phi'].T+(totalM/self.aL)@ang['Phiuu'].T
        boundary=float(max(abs(rightm-ang['right'][:,1]).max(),abs(rightn-ang['right'][:,0]).max()))
        maxG=0.;maxcap=0.;minn=np.inf;maxn=-np.inf;maxell=0.;location=None
        for start in range(0,len(a),64):
            sl=slice(start,min(start+64,len(a)))
            nf=self.aC/a[sl,None]*ang['nC'][None,:]+R[sl]@ang['Phi'].T+S[sl]@ang['Phiuu'].T
            mf=M[sl]@ang['Phiu'].T;lf=ell[sl]@ang['Phi'].T
            G=nf*lf-mf*mf-g['K'][sl,None]
            eig=np.sqrt((nf-lf)**2+4*mf*mf);cap=np.maximum(abs((nf+lf+eig)/2),abs((nf+lf-eig)/2))
            loc=np.unravel_index(np.argmax(abs(G)),G.shape);value=float(abs(G[loc]))
            if value>maxG:maxG=value;location=dict(s=float(g['x'][start+loc[0]]),angular_index=int(loc[1]))
            maxcap=max(maxcap,float(cap.max()));minn=min(minn,float(nf.min()));maxn=max(maxn,float(nf.max()));maxell=max(maxell,float(abs(lf).max()))
        return dict(order=g['order'],nodes=len(a),sampled_full_boundary_defect=boundary,
            sampled_full_Gauss_maximum=maxG,sampled_formal_curvature_maximum=maxcap,
            minimum_n=minn,maximum_n=maxn,maximum_abs_l=maxell,Gauss_maximum_location=location,
            no_angular_truncation=True,continuous_certificate=False,nonlinear_success=False)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--candidate',required=True);parser.add_argument('--state',required=True)
    parser.add_argument('--output-stem',required=True);parser.add_argument('--angles',type=int,default=512)
    parser.add_argument('--order',type=int,default=16);parser.add_argument('--check-order',type=int,default=24)
    args=parser.parse_args();start=time.monotonic();stem=pathlib.Path(args.output_stem)
    report_path=stem.with_name(stem.name+'-report.json');controls_path=stem.with_name(stem.name+'-controls.npz')
    if report_path.exists() or controls_path.exists():raise FileExistsError('Use an unused output stem')
    p=FullFunctionMomentProbe(args.candidate,args.state);u=2*np.pi*np.arange(args.angles)/args.angles;ang=p.angular(u)
    tiny=np.array([.2,.48,.9,1.1,1.4,1.7]);h=1e-6;center=p.angular(tiny);plus=p.angular(tiny+h);minus=p.angular(tiny-h)
    errors={}
    for name,previous in [('Phiu','Phi'),('Phiuu','Phiu')]:
        fd=(plus[previous]-minus[previous])/(2*h);exact=center[name]
        errors[name]=float(np.max(abs(fd-exact)/(1+abs(exact))))
    g=p.grid(args.order);controls=p.controls(g);coarse=p.consume(g,controls,ang)
    refined=p.consume(p.grid(args.check_order),controls,ang)
    np.savez_compressed(controls_path,**controls,parameters=p.parameters,breaks=p.breaks,
        actual_angular_definition=np.array('R150: full A,N,l_L and exact analytic material first/second jets; no Fourier truncation'))
    eigen=np.linalg.eigvalsh(controls['H'])
    report=dict(schema='fd2d-full-angular-function-three-moment-probe-v1',source=identity(__file__),
        radial_primitive_source=identity(pathlib.Path(__file__).with_name('fd2d_codazzi_moment_lifting_probe.py')),
        candidate=identity(args.candidate),input_state=identity(args.state),controls=identity(controls_path),
        angular_samples=args.angles,no_angular_Fourier_or_projection=True,full_boundary_functions='original exact defined balanced seed and positive Bernstein tail',
        unchanged_parameters=True,unchanged_physical_metric=True,
        angular_derivative_small_check=dict(points=tiny.tolist(),step=h,scaled_errors=errors),
        Gram=dict(eigenvalues=eigen.tolist(),condition=float(eigen[-1]/eigen[0])),
        coarse=coarse,independent_radial_consumption=refined,
        seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        nonlinear_success=False,continuous_surface_claim=False)
    report_path.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(report=str(report_path),Gram=report['Gram'],jets=errors,coarse=coarse,independent=refined,
        seconds=report['seconds'],peak_rss_kib=report['peak_rss_kib'])),flush=True)

if __name__=='__main__':main()
