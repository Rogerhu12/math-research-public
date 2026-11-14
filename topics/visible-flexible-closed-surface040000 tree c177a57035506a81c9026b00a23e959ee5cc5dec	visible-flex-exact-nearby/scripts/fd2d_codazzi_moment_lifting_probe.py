#!/usr/bin/env python3
"""Finite quadrature probe of the exact R148 definition, not a GC solution.

The angular input is explicitly the even Fourier polynomial obtained from
fixed uniform material samples. Its omitted boundary function is measured.
The second radial rule consumes the first rule's actual control coefficients
and independently checks their endpoint defects. No current solver is edited.
"""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse,hashlib,json,pathlib,time,resource
import numpy as np
from fd2d_gc_radial_bump_profile import RadialBumpProfile
from fd2d_balanced_curvature_core import FixedBalancedGeometry,BalancedCurvatureCore
from fd2d_positive_flat_developable_family import PositiveFlatDevelopableFamily


def identity(path):
    p=pathlib.Path(path);b=p.read_bytes()
    return dict(path=str(p.resolve()),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())


def s5(q):
    q=np.clip(q,0.,1.);return q**3*(10-15*q+6*q*q)


def rule_tables(order):
    x,w=np.polynomial.legendre.leggauss(order)
    v=np.polynomial.legendre.legvander(x,order)
    integrals=np.empty((order,order));integrals[:,0]=x+1
    for j in range(1,order):
        integrals[:,j]=(v[:,j+1]-v[:,j-1])/(2*j+1)
    coefficient=((2*np.arange(order)+1)/2)[:,None]*v[:,:order].T*w
    return x,w,integrals@coefficient


def primitive(values,widths,w,integral_matrix):
    pieces,order=len(widths),len(w)
    shape=values.shape[1:];z=values.reshape((pieces,order)+shape)
    total=np.einsum('q,cq...->c...',w,z)*(widths/2).reshape((pieces,)+(1,)*len(shape))
    prefix=np.concatenate((np.zeros_like(total[:1]),np.cumsum(total,axis=0)[:-1]),axis=0)
    partial=np.einsum('iq,cq...->ci...',integral_matrix,z)*(widths/2).reshape((pieces,1)+(1,)*len(shape))
    return (partial+prefix[:,None]).reshape(values.shape),np.sum(total,axis=0)


class Probe:
    def __init__(self,candidate,state,modes,angles,max_step):
        with np.load(state,allow_pickle=False) as z:
            p=z['parameters'].copy();oldK=int(z['modes']);supports=z['profile_supports'].copy()
        self.profile=RadialBumpProfile(candidate,supports=supports,coefficients=p[2*oldK+1:])
        self.tail=PositiveFlatDevelopableFamily(coefficients=p[oldK:2*oldK+1],
            cut_radius=.8,cuff_radius=.32,flat_radius=.34,plane_height=1.25)
        geom=FixedBalancedGeometry();core=BalancedCurvatureCore(p[:oldK],geometry=geom)
        self.C,self.L=float(self.profile.central_end),float(self.profile.end)
        self.angles=angles;self.modes=modes;self.k=2*np.arange(modes+1)
        self.u=2*np.pi*np.arange(angles)/angles
        self.phase=np.asarray(geom.normal_angle(self.u),float)
        self.left_samples=np.stack((np.asarray(core.curvature(self.phase)['n'],float),
            np.zeros(angles),np.zeros(angles)),axis=-1)
        aL=float(self.profile.jet([self.L])['a'][0]);sn,cs=np.sin(self.u),np.cos(self.u)
        kap=self.tail.angle_jets(aL*sn)['kappa']
        self.right_samples=kap[:,None]*np.stack((cs*cs,-sn*cs,sn*sn),axis=-1)
        self.left=np.fft.rfft(self.left_samples,axis=0)[self.k]/angles
        self.right=np.fft.rfft(self.right_samples,axis=0)[self.k]/angles
        self.aC=float(self.profile.jet([self.C])['a'][0]);self.aL=aL
        self.control_left=self.C+.001;self.control_right=self.L-.001;self.ramp=.01
        self.tail_start=.42*self.L
        br=np.unique(np.r_[self.profile.breaks,self.control_left,self.control_left+self.ramp,
            self.control_right-self.ramp,self.control_right,self.tail_start,self.C,self.L])
        br=br[(br>=self.C)&(br<=self.L)]
        self.breaks=np.unique(np.concatenate([np.linspace(l,r,max(1,int(np.ceil((r-l)/max_step)))+1)
            for l,r in zip(br[:-1],br[1:])]))
        self.parameters=p;self.input_modes=oldK

    def material(self,coefficients):
        spec=np.zeros((len(coefficients),self.angles//2+1),complex)
        spec[:,self.k]=coefficients*self.angles
        return np.fft.irfft(spec,n=self.angles,axis=1)

    def grid(self,order):
        x,w,anti=rule_tables(order);width=np.diff(self.breaks)
        points=(self.breaks[:-1,None]+width[:,None]*(x+1)/2).ravel()
        jet=self.profile.jet(points);a,ap=jet['a'],jet['a_s']
        first,I=primitive(a**-2,width,w,anti);J=I-first
        b=s5((points-self.control_left)/self.ramp)*s5((self.control_right-points)/self.ramp)
        weight=(width[:,None]*w[None,:]/2).ravel()
        base=[];sn=np.sin(self.u)
        for start in range(0,len(points),order):
            aa=a[start:start+order,None];ss=points[start:start+order,None]
            values=self.tail.angle_jets(aa*sn[None,:])['kappa']*sn[None,:]**2
            values*=s5((ss-self.tail_start)/(self.L-self.tail_start))
            base.append(np.fft.rfft(values,axis=1)[:,self.k]/self.angles)
        return dict(order=order,x=points,a=a,ap=ap,K=jet['K'],J=J,I=I,b=b,
            weights=weight,widths=width,gauss_weights=w,anti=anti,base=np.concatenate(base))

    def controls(self,g):
        a,ap,b,J,W,B=(g[key] for key in ('a','ap','b','J','weights','base'))
        k=self.k[1:];mu=a*b;A=float(W@mu)
        q=(ap/a)[:,None]/k[None,:]**2-J[:,None]
        qbar=(W*mu)@q/A;V=(W*mu)@((q-qbar)**2)
        nC,mC=self.left[:,0],self.left[:,1];nL,mL=self.right[:,0],self.right[:,1]
        t1=(self.aL**2*mL[1:]-self.aC**2*mC[1:])/(1j*k)-(W*a)@B[:,1:]
        t2=(self.aL*nL[1:]-self.aC*nC[1:])/k**2-1j*self.aC**2*mC[1:]*g['I']/k-(W*a)@(q*B[:,1:])
        xx=t1/A;yy=(t2-qbar*t1)/V
        M0=float(W@(ap*ap*b));T0=self.aL*nL[0]-self.aC*nC[0]-(W*ap)@B[:,0]
        if min(A,M0,float(V.min()))<=0:raise ArithmeticError('Actual finite Gram screen is not positive')
        return dict(A=A,V=V,qbar=qbar,x=xx,y=yy,M0=M0,r=T0/M0)

    def consume(self,g,p):
        k=self.k;a,ap,b,J,W,B=(g[key] for key in ('a','ap','b','J','weights','base'))
        ell=B.copy();ell[:,0]+=p['r']*ap*b
        q=(ap/a)[:,None]/k[None,1:]**2-J[:,None]
        ell[:,1:]+=b[:,None]*(p['x']+p['y']*(q-p['qbar']))
        integ,totalAl=primitive(a[:,None]*ell,g['widths'],g['gauss_weights'],g['anti'])
        m=(self.aC**2*self.left[None,:,1]+1j*k[None,:]*integ)/a[:,None]**2
        intm,totalm=primitive(m,g['widths'],g['gauss_weights'],g['anti'])
        intell,totalell=primitive(ap[:,None]*ell,g['widths'],g['gauss_weights'],g['anti'])
        n=(self.aC*self.left[None,:,0]+1j*k[None,:]*intm+intell)/a[:,None]
        rightm=(self.aC**2*self.left[:,1]+1j*k*totalAl)/self.aL**2
        rightn=(self.aC*self.left[:,0]+1j*k*totalm+totalell)/self.aL
        defects=np.stack((rightn-self.right[:,0],rightm-self.right[:,1]))
        nf,mf,lf=map(self.material,(n,m,ell))
        G=nf*lf-mf*mf-g['K'][:,None]
        eig=np.sqrt((nf-lf)**2+4*mf**2)
        cap=np.maximum(abs((nf+lf+eig)/2),abs((nf+lf-eig)/2))
        loc=np.unravel_index(np.argmax(abs(G)),G.shape)
        return dict(order=g['order'],nodes=len(a),minimum_a=float(a.min()),
            endpoint_coefficient_maximum=float(np.max(abs(defects))),
            endpoint_material_maximum=float(np.max(abs(self.material(defects)))),
            sampled_full_Gauss_maximum=float(np.max(abs(G))),sampled_formal_curvature_maximum=float(cap.max()),
            gauss_maximum_location=dict(s=float(g['x'][loc[0]]),u=float(self.u[loc[1]])),
            minimum_n=float(nf.min()),maximum_n=float(nf.max()),maximum_abs_l=float(abs(lf).max()),
            exact_Codazzi_claimed_for_numerical_quadrature=False,
            continuous_certificate=False,nonlinear_success=False)


def main():
    pa=argparse.ArgumentParser();pa.add_argument('--candidate',required=True);pa.add_argument('--state',required=True)
    pa.add_argument('--output-stem',required=True);pa.add_argument('--modes',type=int,default=63)
    pa.add_argument('--angles',type=int,default=1024);pa.add_argument('--order',type=int,default=16)
    pa.add_argument('--check-order',type=int,default=24);pa.add_argument('--max-step',type=float,default=.0125)
    args=pa.parse_args();start=time.monotonic();stem=pathlib.Path(args.output_stem)
    report_path=stem.with_name(stem.name+'-report.json');state_path=stem.with_name(stem.name+'-controls.npz')
    if report_path.exists() or state_path.exists():raise FileExistsError('Use a new output stem')
    if args.angles%2 or 2*args.modes>=args.angles//2:raise ValueError('Keep highest even wave below Nyquist')
    p=Probe(args.candidate,args.state,args.modes,args.angles,args.max_step)
    g=p.grid(args.order);control=p.controls(g);coarse=p.consume(g,control)
    check=p.consume(p.grid(args.check_order),control)
    boundary={}
    for label,coef,actual in [('left',p.left,p.left_samples),('right',p.right,p.right_samples)]:
        finite=p.material(coef.T).T;boundary[label]=float(np.max(abs(finite-actual)))
    np.savez_compressed(state_path,**control,parameters=p.parameters,breaks=p.breaks,
        input_modes=p.input_modes,modes=p.modes,angular_samples=p.angles,
        left_boundary_coefficients=p.left,right_boundary_coefficients=p.right,
        formula=np.array('R148 exact two-moment definition, evaluated by explicit finite radial and angular quadrature'))
    report=dict(schema='fd2d-Codazzi-two-moment-finite-probe-v1',source=identity(__file__),
        candidate=identity(args.candidate),input_state=identity(args.state),controls=identity(state_path),
        parameters_unchanged=True,physical_metric_unchanged=True,angular_basis='fixed physical material u',
        angular_polynomial_definition=dict(modes=args.modes,highest_integer_wave=2*args.modes,uniform_samples=args.angles),
        actual_boundary_truncation_maximum=boundary,
        weight_definition=dict(left=p.control_left,right=p.control_right,ramp=p.ramp,formula='S5((s-left)/ramp)*S5((right-s)/ramp)'),
        Gram_screen=dict(A=control['A'],M0=control['M0'],minimum_V=float(control['V'].min()),maximum_V=float(control['V'].max())),
        coarse=coarse,independent_radial_consumption=check,
        seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        scope='A finite initializer probe; full boundary truncation and radial moment defects are reported, not called an exact nonlinear GC field')
    report_path.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(report=str(report_path),coarse=coarse,independent=check,boundary=boundary,
        Gram=report['Gram_screen'],seconds=report['seconds'],peak_rss_kib=report['peak_rss_kib'])),flush=True)

if __name__=='__main__':main()
