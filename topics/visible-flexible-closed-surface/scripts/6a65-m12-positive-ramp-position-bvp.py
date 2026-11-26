#!/usr/bin/env python3
"""Free two-port actual Cartesian full-Gram BVP on the original M12 K>0 ramp.

The unknown is a C4 quintic B-spline times a complete selected C3/reflection
Cartesian Fourier expansion, added to the actual old position map. Neither
port is frozen. A matrix-free analytic J/JT differentiates that own map.
The intrinsic profile and fixed central material chart never change.

This is a finite BVP consumer, not an infinite-dimensional existence proof.
Its moved ports need exact-coast consumption and actual neighboring seams.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import importlib.util
import json
from pathlib import Path
import time
import numpy as np
from scipy import fft
from scipy.interpolate import BSpline
from scipy.linalg import cholesky, solve_triangular
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import LinearOperator, lsmr

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('positive_ramp_glue',HERE/'6a65-m12-ramp-exact-coast-c2-glue.py')
glue=importlib.util.module_from_spec(spec);spec.loader.exec_module(glue)
ramp=glue.ramp;ad=ramp.ad;LD=np.longdouble


class PositiveRamp(ramp.OriginalRamp):
    def __init__(self,meta):
        super().__init__(meta)
        self.left=self.Tu-self.R
        self.right=self.Tu
        self.positive_breaks=[self.left,self.left+self.R*self.etaq,self.right-self.R*self.etaq,self.right]

    def profile(self,s):
        z=ad.base.ld(self.Tu)-np.asarray(s,dtype=LD)
        a,ap,app=super().profile(z)
        return 2+ad.base.ld(self.delta)-a,ap,-app


def radial_grid(candidate,elements,gauss):
    mesh=[]
    for left,right in zip(candidate.positive_breaks[:-1],candidate.positive_breaks[1:]):
        count=max(1,round(elements*float((right-left)/candidate.R)))
        mesh.extend([float(left+(right-left)*Q(j,count)) for j in range(count)])
    mesh.append(float(candidate.right));mesh=np.asarray(mesh)
    gx,gw=np.polynomial.legendre.leggauss(gauss)
    s=((mesh[:-1]+mesh[1:])[:,None]/2+(mesh[1:]-mesh[:-1])[:,None]*gx/2).ravel()
    weights=((mesh[1:]-mesh[:-1])[:,None]*gw/2).ravel()
    return mesh,s,weights


class Basis:
    def __init__(self,mesh,order):
        self.knots=np.r_[np.repeat(mesh[0],6),mesh[1:-1],np.repeat(mesh[-1],6)]
        self.nb=len(self.knots)-6
        self.spline=BSpline(self.knots,np.eye(self.nb),5,axis=0)
        self.pm=np.arange(-order,order+1)*3+1
        self.zm=np.arange(order+1)*3
        self.modes=np.r_[self.pm,self.zm]
        self.na=len(self.modes)
        self.order=order

    def matrices(self,s):
        return [csr_matrix(self.spline(s,nu=j)) for j in range(3)]

    def angular(self,amplitude,N,derivative=0):
        nr=len(amplitude)
        q=np.zeros((nr,N),dtype=complex)
        z=np.zeros((nr,N),dtype=complex)
        q[:,self.pm%N]=amplitude[:,:len(self.pm)]*(1j*self.pm)**derivative
        zz=amplitude[:,len(self.pm):]
        z[:,0]=zz[:,0] if derivative==0 else 0
        if len(self.zm)>1:
            k=self.zm[1:]
            z[:,k]=zz[:,1:]*(1j*k)**derivative/2
            z[:,-k]=zz[:,1:]*(-1j*k)**derivative/2
        q=fft.ifft(q,axis=1,norm='forward')
        z=fft.ifft(z,axis=1,norm='forward').real
        return np.stack((q.real,q.imag,z),axis=-1)

    def angular_adjoint(self,values,derivative=0):
        q=fft.fft(values[...,0]+1j*values[...,1],axis=1)
        z=fft.fft(values[...,2],axis=1)
        if derivative==0:
            return np.c_[q[:,self.pm%values.shape[1]].real,z[:,self.zm].real]
        if derivative==1:
            return np.c_[q[:,self.pm%values.shape[1]].imag*self.pm,z[:,self.zm].imag*self.zm]
        raise ValueError('Only first derivative adjoint is used')


def central_chart(central,N):
    theta=np.arange(N)*2*np.pi/N
    p=central.derivative(theta,1);q=central.derivative(theta,2)
    J=np.linalg.norm(p,axis=-1)
    u=np.concatenate([glue.material_angle(central,theta[j:j+64]) for j in range(0,N,64)])
    return u,J/central.a,np.sum(p*q,axis=-1)/(J*central.a)


def background(src,candidate,central,s,N,lam):
    u,rho,rhop=central_chart(central,N)
    data=[]
    for value in s:
        p=ad.old_packet(src,LD(lam)*LD(value),u,LD(lam))
        data.append(np.stack((p['X'],p['X_s'],p['X_u']*rho[:,None],p['X_ss'],
                              p['X_su']*rho[:,None],p['X_uu']*rho[:,None]**2+p['X_u']*rhop[:,None])))
    return np.asarray(data),np.asarray(candidate.profile(s)[0],float)[:,None]*rho[None,:]


def gram(Xs,Xt,bb):
    e=np.sum(Xs*Xs,axis=-1)-1
    f=np.sum(Xs*Xt,axis=-1)/bb
    g=np.sum(Xt*Xt,axis=-1)/(bb*bb)-1
    return np.stack((e,np.sqrt(2)*f,g),axis=-1)


def statistics(p,bb,weights):
    X,Xs,Xt,Xss,Xst,Xtt=[p[:,j] for j in range(6)]
    res=gram(Xs,Xt,bb);e,f,g=res[...,0],res[...,1]/np.sqrt(2),res[...,2]
    op=np.abs(e+g)/2+np.sqrt(((e-g)/2)**2+f*f)
    normal=np.cross(Xs,Xt);normal/=np.linalg.norm(normal,axis=-1)[...,None]
    E=e+1;F=f*bb;G=(g+1)*bb*bb
    L,M,N=[np.sum(normal*z,axis=-1) for z in (Xss,Xst,Xtt)]
    det=E*G-F*F;trace=(G*L-2*F*M+E*N)/det;kg=(L*N-M*M)/det
    curvature=np.abs(trace)/2+np.sqrt(np.maximum(0,trace*trace/4-kg))
    where=np.unravel_index(np.argmax(op),op.shape)
    return dict(metric_peak=float(np.max(op)),weighted_energy=float(np.sum(weights[:,None]*bb*np.sum(res*res,axis=-1))/bb.shape[1]),
                curvature_peak=float(np.max(curvature)),support_lower=float(np.min(-np.sum(X*normal,axis=-1))),
                peak_radial_index=int(where[0]),peak_angle_index=int(where[1]))


class Linearized:
    def __init__(self,basis,s,weights,p,bb,N,precondition=True):
        self.basis=basis;self.B0,self.B1,self.B2=basis.matrices(s)
        self.N=N;self.Xs=p[:,1];self.Xt=p[:,2];self.bb=bb
        self.weight=np.sqrt(weights[:,None]*bb/N)
        if not precondition:return
        mass=np.asarray((self.B0.T@self.B0.multiply(weights[:,None])).todense())
        stiff=np.asarray((self.B1.T@self.B1.multiply(weights[:,None])).todense())
        self.S=[]
        for k in basis.modes:
            H=stiff+(float(k*k)+.01)*mass
            L=cholesky(H,lower=True)
            self.S.append(solve_triangular(L.T,np.eye(basis.nb),lower=False))
        self.S=np.asarray(self.S)
        self.shape=(p.shape[0]*N*3,basis.nb*basis.na)
        self.operator=LinearOperator(self.shape,matvec=self.matvec,rmatvec=self.rmatvec,dtype=float)

    def unpack(self,x):
        return np.einsum('aij,aj->ia',self.S,np.asarray(x).reshape(self.basis.na,self.basis.nb),optimize=True)

    def matvec(self,x):
        coeff=self.unpack(x)
        Ws=self.basis.angular(self.B1@coeff,self.N)
        Wt=self.basis.angular(self.B0@coeff,self.N,1)
        e=2*np.sum(self.Xs*Ws,axis=-1)
        f=np.sqrt(2)*np.sum(self.Xs*Wt+self.Xt*Ws,axis=-1)/self.bb
        g=2*np.sum(self.Xt*Wt,axis=-1)/(self.bb*self.bb)
        return (np.stack((e,f,g),axis=-1)*self.weight[...,None]).ravel()

    def rmatvec(self,x):
        z=np.asarray(x).reshape(*self.bb.shape,3)*self.weight[...,None]
        e,f,g=z[...,0],z[...,1],z[...,2]
        V=2*e[...,None]*self.Xs+(np.sqrt(2)*f/self.bb)[...,None]*self.Xt
        W=(np.sqrt(2)*f/self.bb)[...,None]*self.Xs+(2*g/(self.bb*self.bb))[...,None]*self.Xt
        grad=self.B1.T@self.basis.angular_adjoint(V)+self.B0.T@self.basis.angular_adjoint(W,1)
        return np.einsum('aij,ia->aj',self.S,grad,optimize=True).ravel()

    def packet(self,coeff):
        a0,a1,a2=self.B0@coeff,self.B1@coeff,self.B2@coeff
        return np.stack((self.basis.angular(a0,self.N),self.basis.angular(a1,self.N),self.basis.angular(a0,self.N,1),
                         self.basis.angular(a2,self.N),self.basis.angular(a1,self.N,1),self.basis.angular(a0,self.N,2)),axis=1)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--data',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--elements',type=int,default=48);ap.add_argument('--order',type=int,default=24)
    ap.add_argument('--angular',type=int,default=384);ap.add_argument('--gauss',type=int,default=4)
    ap.add_argument('--iterations',type=int,default=500);ap.add_argument('--newton',type=int,default=2)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Fresh report path required')
    if args.angular<=2*(3*args.order+1):raise ValueError('Angular grid aliases selected Fourier modes')
    start=time.monotonic();meta=HERE.parent/'notes'/ad.base.META_NAME
    if ad.sha(args.data)!=ad.base.DATA_SHA:raise ValueError('Wrong original M12 data')
    src=ad.base.Source(args.data,meta);candidate=PositiveRamp(json.loads(meta.read_text()))
    unused,central_c=ad.exact_section(args.data,Q(0));central=ad.NativeCurve(central_c,512,32)
    bridge=json.loads((HERE.parent/'notes/2026-11-09-db6f-root-exact-bridge-m12.json').read_text())['arclength_rescale']
    lam=(Q(bridge['lo'])+Q(bridge['hi']))/2
    mesh,s,weights=radial_grid(candidate,args.elements,args.gauss);basis=Basis(mesh,args.order)
    p0,bb=background(src,candidate,central,s,args.angular,ad.base.ld(lam));p=p0.copy()
    coeff=np.zeros((basis.nb,basis.na));rows=[];initial=statistics(p,bb,weights)
    print(json.dumps({'initial':initial,'unknowns':coeff.size,'residuals':len(s)*args.angular*3}),flush=True)
    for step in range(args.newton):
        op=Linearized(basis,s,weights,p,bb,args.angular)
        if step==0:
            rng=np.random.default_rng(1729);x=rng.normal(size=op.shape[1]);y=rng.normal(size=op.shape[0])
            lhs=np.dot(op.matvec(x),y);rhs=np.dot(x,op.rmatvec(y))
            adjoint_error=abs(lhs-rhs)/max(1,abs(lhs),abs(rhs))
            if adjoint_error>1e-11:raise ArithmeticError('Analytic J/JT mismatch')
        residual=(gram(p[:,1],p[:,2],bb)*op.weight[...,None]).ravel()
        scale=1e10
        solution=lsmr(op.operator,-residual*scale,atol=1e-11,btol=1e-11,conlim=1e12,maxiter=args.iterations)
        correction=op.unpack(solution[0])/scale;delta=op.packet(correction)
        before=statistics(p,bb,weights);accepted=None;attempts=[]
        for alpha in (1.,.5,.25,.125,.0625):
            trial=p+alpha*delta;stat=statistics(trial,bb,weights);attempts.append({'alpha':alpha,**stat})
            if stat['weighted_energy']<before['weighted_energy'] and stat['metric_peak']<=1.05*before['metric_peak']:
                accepted=alpha;p=trial;coeff+=alpha*correction;break
        row={'step':step,'lsmr_stop':int(solution[1]),'lsmr_iterations':int(solution[2]),'lsmr_residual':float(solution[3])/scale,
             'estimated_condition':float(solution[6]),'accepted_alpha':accepted,'attempts':attempts}
        rows.append(row);print(json.dumps(row),flush=True)
        if accepted is None:break
    # Different radial Gauss points and doubled angular grid, same actual map.
    omesh,os,ow=radial_grid(candidate,args.elements,args.gauss+2)
    po,bo=background(src,candidate,central,os,2*args.angular,ad.base.ld(lam))
    oo=Linearized(basis,os,ow,po,bo,2*args.angular,precondition=False)
    before_obs=statistics(po,bo,ow);after_obs=statistics(po+oo.packet(coeff),bo,ow)
    endp,endbb=background(src,candidate,central,[float(candidate.left),float(candidate.right)],2*args.angular,ad.base.ld(lam))
    eop=Linearized(basis,[float(candidate.left),float(candidate.right)],np.ones(2),endp,endbb,2*args.angular,precondition=False)
    # No two-point preconditioner is used; packet depends only on evaluation matrices.
    enddelta=eop.packet(coeff)
    np.savez_compressed(str(args.out)+'.field.npz',coefficients=coeff,knots=basis.knots,planar_modes=basis.pm,vertical_modes=basis.zm,
                        central_c_numerator=np.asarray([str(q.numerator) for q in central_c]),central_c_denominator=np.asarray([str(q.denominator) for q in central_c]))
    out={'schema':'6a65-original-M12-positive-K-free-two-port-Cartesian-BVP-v1','script_sha256':ad.sha(__file__),
         'data_sha256':ad.base.DATA_SHA,'original_geometry_sha256':ad.sha(meta),'field_sha256':ad.sha(str(args.out)+'.field.npz'),
         's_left_exact':str(candidate.left),'s_right_exact':str(candidate.right),'original_metric_unchanged':True,
         'unknown_count':int(coeff.size),'elements':len(mesh)-1,'angular':args.angular,'gauss':args.gauss,'order':args.order,
         'analytic_adjoint_relative_error':float(adjoint_error),'initial_training':initial,'rows':rows,
         'independent_observer_before':before_obs,'independent_observer_after':after_obs,
         'left_port_twojet_changes':{name:float(np.max(np.linalg.norm(enddelta[0,j],axis=-1))) for j,name in enumerate(('X','Xs','Xtheta','Xss','Xstheta','Xthetatheta'))},
         'right_port_twojet_changes':{name:float(np.max(np.linalg.norm(enddelta[1,j],axis=-1))) for j,name in enumerate(('X','Xs','Xtheta','Xss','Xstheta','Xthetatheta'))},
         'both_ports_free':True,'neighboring_exact_coast_consumed':False,'whole_closed_surface_constructed':False,
         'continuous_metric_certificate':False,'seconds':time.monotonic()-start}
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps(out,indent=2,allow_nan=False))


if __name__=='__main__':main()
