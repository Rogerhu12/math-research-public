#!/usr/bin/env python3
"""Consume the actual M12 Fourier inlet using the existing R137 supplier.

The raw inlet curve is the exact-rational Hermite cross-section at the fixed
native coordinate.  Its constant-speed normalized image is defined by an
exact arclength integral, not by identifying a quadrature value as exact.
The target affine metric is the ORIGINAL frozen physical profile; the exact
bridge determines native s = lambda * physical sigma.  Rounded evaluation
and angle/quadrature observations are reported separately from that definition.
Old full Cartesian ports are compared; no gluing or closed-map claim is made.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import io
import json
import math
from pathlib import Path
import sys
import time
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec);spec.loader.exec_module(value)
    return value


base=module("m12_r137_source",HERE/"6a65-m12-weak-stress-recovered-v2.py")
supplier=module("m12_r137_supplier",HERE/"6a65-geometry-r137-exact-inlet-consumer.py")
LD=base.LD


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def normmax(x):return float(np.max(np.linalg.norm(x,axis=-1)))
def qfloat(x):return F.from_float(float(x))


def exact_section(data,s):
    """Exact nodal binary rational Hermite, including exact mean increments."""
    with np.load(io.BytesIO(gzip.decompress(Path(data).read_bytes())),allow_pickle=False) as a:
        mesh=a['mesh'];jets=a['jets'];increments=a['mean_increments']
        cell=min(len(mesh)-2,max(0,int(np.searchsorted(mesh,float(s),side='right')-1)))
        left=qfloat(mesh[cell]);h=qfloat(mesh[cell+1])-left;t=(s-left)/h
        if not 0<=t<=1:raise ValueError('Exact source cell lookup failed')
        mean=sum((qfloat(z) for z in increments[:cell]),F(0))
        coeff=[]
        for j in range(jets.shape[2]):
            y0=mean if j==jets.shape[2]-1 else qfloat(jets[0,cell,j])
            y1=mean+qfloat(increments[cell]) if j==jets.shape[2]-1 else qfloat(jets[0,cell+1,j])
            d0,d1=qfloat(jets[1,cell,j]),qfloat(jets[1,cell+1,j])
            d20,d21=qfloat(jets[2,cell,j]),qfloat(jets[2,cell+1,j])
            p0,p1,p2=y0,h*d0,h*h*d20/2
            r0=y1-y0-p1-p2;r1=h*(d1-d0)-h*h*d20;r2=h*h*(d21-d20)
            poly=[p0,p1,p2,10*r0-4*r1+r2/2,-15*r0+7*r1-r2,6*r0-3*r1+r2/2]
            val=poly[-1]
            for z in reversed(poly[:-1]):val=val*t+z
            coeff.append(val)
    return cell,coeff


class NativeCurve(supplier.Curve):
    """Analytic cylindrical-to-Cartesian Fourier conversion, with no DFT."""
    def __init__(self,exact_coeff,panels=128,gauss=16):
        c=exact_coeff;M=(len(c)-2)//3;degree=3*M+1
        self.degree=degree;self.modes=np.arange(-degree,degree+1)
        self.coeff=np.zeros((2*degree+1,3),dtype=complex)
        def xy(m,amplitude):
            z=float(amplitude/2)
            self.coeff[degree+m,0]+=z;self.coeff[degree-m,0]+=z
            self.coeff[degree+m,1]-=1j*z;self.coeff[degree-m,1]+=1j*z
        xy(1,c[0])
        for j in range(1,M+1):
            xy(1+3*j,(c[j]+c[M+j])/2)
            xy(1-3*j,(c[j]-c[M+j])/2)
            self.coeff[degree+3*j,2]=float(c[2*M+j]/2)
            self.coeff[degree-3*j,2]=float(c[2*M+j]/2)
        self.coeff[degree,2]=float(c[-1])
        self.exact_coeff=c;self.planar=False;self.panels=panels;self.gauss=gauss
        x,w=np.polynomial.legendre.leggauss(gauss)
        self.gx,self.gw=(x+1)/2,w/2
        self.cuts=np.linspace(0,2*np.pi,panels+1)
        lo=self.cuts[:-1];length=np.diff(self.cuts)
        q=lo[:,None]+length[:,None]*self.gx
        speed=np.linalg.norm(self.derivative(q.ravel(),1),axis=-1).reshape(q.shape)
        lengths=length*np.sum(speed*self.gw,axis=-1)
        self.cumulative=np.r_[0,np.cumsum(lengths)]
        self.perimeter=self.cumulative[-1];self.a=self.perimeter/(2*np.pi)


class FixedRadiusCurve(supplier.Curve):
    def __init__(self,raw,target):
        self.raw=raw;self.a=float(target)
        self.normalization=self.a/raw.a
        self.center=raw.coeff[raw.degree].real.copy()
        self.degree=raw.degree;self.panels=raw.panels;self.gauss=raw.gauss

    def theta(self,u):return self.raw.theta(u)

    def derivative(self,theta,order=0):
        value=self.raw.derivative(theta,order)
        return self.center+self.normalization*(value-self.center) if order==0 else self.normalization*value


def old_packet(src,s,u,lam):
    """Own full Cartesian two-jet, in physical sigma and original material u."""
    s=LD(s);u=np.asarray(u,dtype=LD)
    e,ep=src.chart(s)
    j=min(np.searchsorted(src.sx,s/src.end,side='right')-1,len(src.sc)-1)
    xx=s/src.end-src.sx[j]
    epp=src.warp*(2*src.sc[j,2]+6*src.sc[j,3]*xx)/(src.end*src.end)
    psi=u.copy()
    for unused in range(20):
        residual=psi-e*np.sin(3*psi)/3-u
        psi-=residual/(1-e*np.cos(3*psi))
        if np.max(np.abs(residual))<LD('1e-18'):break
    if np.max(np.abs(residual))>LD('1e-15'):raise ArithmeticError('Old material inverse failed')
    cell=max(0,min(len(src.mesh)-2,np.searchsorted(src.mesh,s,side='right')-1))
    c,d=src.coefficients(cell,s);t=(s-src.mesh[cell])/src.h[cell];p=src.power[cell]
    dd=20*p[5]
    for k in range(4,1,-1):dd=dd*t+k*(k-1)*p[k]
    dd/=src.h[cell]**2
    M=src.M;k=np.arange(3,3*M+1,3,dtype=LD)
    co,si=np.cos(k[:,None]*psi),np.sin(k[:,None]*psi)
    def terms(a):
        R=a[0]+a[1:M+1]@co;T=a[M+1:2*M+1]@si;Z=a[-1]+a[2*M+1:3*M+1]@co
        Rp=-(k*a[1:M+1])@si;Tp=(k*a[M+1:2*M+1])@co;Zp=-(k*a[2*M+1:3*M+1])@si
        Rpp=-(k*k*a[1:M+1])@co;Tpp=-(k*k*a[M+1:2*M+1])@si;Zpp=-(k*k*a[2*M+1:3*M+1])@co
        return np.stack([R,T,Z],axis=-1),np.stack([Rp-T,Tp+R,Zp],axis=-1),np.stack([Rpp-2*Tp-R,Tpp+2*Rp-T,Zpp],axis=-1)
    X,Xp,Xpp=terms(c);Xs,Xsp,_=terms(d);Xss,_,_=terms(dd)
    rho=1-e*np.cos(3*psi);nu=-ep*np.sin(3*psi)/3
    uss=-epp*np.sin(3*psi)/3;usp=-ep*np.cos(3*psi);upp=3*e*np.sin(3*psi)
    ps=-nu/rho;pu=1/rho
    pss=-(uss+2*usp*ps+upp*ps*ps)/rho
    psu=-(usp+upp*ps)/(rho*rho);puu=-upp/(rho*rho*rho)
    col=lambda x:x[:,None]
    value={'X':X,'X_s':LD(lam)*(Xs+col(ps)*Xp),'X_u':col(pu)*Xp,
           'X_ss':LD(lam)**2*(Xss+2*col(ps)*Xsp+col(ps*ps)*Xpp+col(pss)*Xp),
           'X_su':LD(lam)*(col(pu)*Xsp+col(ps*pu)*Xpp+col(psu)*Xp),
           'X_uu':col(pu*pu)*Xpp+col(puu)*Xp}
    cp,sp=np.cos(psi),np.sin(psi)
    def cart(v):return np.stack([cp*v[:,0]-sp*v[:,1],sp*v[:,0]+cp*v[:,1],v[:,2]],axis=-1).astype(float)
    return {key:cart(v) for key,v in value.items()}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--data',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--angles',type=int,default=256)
    ap.add_argument('--panels',type=int,default=128)
    ap.add_argument('--gauss',type=int,default=16)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Fresh output required')
    start=time.monotonic()
    src=base.Source(args.data,HERE.parent/'notes'/base.META_NAME)
    rg=base.regions(src.meta)[0];left,right=rg['left'],rg['right'];slope=rg['slope']
    bridgepath=HERE.parent/'notes/2026-11-09-db6f-root-exact-bridge-m12.json'
    bridge=json.loads(bridgepath.read_text());lamlo=F(bridge['arclength_rescale']['lo']);lamhi=F(bridge['arclength_rescale']['hi'])
    lam=(lamlo+lamhi)/2
    # Evaluation midpoint; the mathematical lambda is the unique exact bridge.
    sigma0=left/lam;length=(right-left)/lam
    f0=rg['intercept']+slope*sigma0
    cell,c=exact_section(args.data,left)
    raw=NativeCurve(c,args.panels,args.gauss);curve=FixedRadiusCurve(raw,float(f0))
    u=2*np.pi*np.arange(args.angles)/args.angles
    inlet=curve.inlet(u,float(slope))
    n,m=inlet['n'],inlet['m'];k=m/n;ku=inlet['m_u']/n-m*inlet['n_u']/(n*n)
    B=float(slope)*(1+k*k)-ku
    focus=np.full_like(B,np.inf);negative=B<0
    wf=float(f0)/(-B[negative])
    focus[negative]=np.hypot(float(f0/slope)+wf,k[negative]*wf)-float(f0/slope)
    zero=supplier.propagate(float(f0),float(slope),0.,inlet)
    oldleft=old_packet(src,base.ld(left),u,base.ld(lam))
    result={
        'schema':'6a65-M12-original-affine-metric-exact-form-R137-v1',
        'script_sha256':sha(__file__),'supplier_sha256':sha(HERE/'6a65-geometry-r137-exact-inlet-consumer.py'),
        'ruling_sha256':sha(HERE/'fd2d_k0_ruling_coast.py'),'data_sha256':base.DATA_SHA,
        'geometry_sha256':sha(HERE.parent/'notes'/base.META_NAME),'exact_bridge_sha256':sha(bridgepath),
        'native_left_exact':str(left),'native_right_exact':str(right),'source_cell':int(cell),
        'fixed_metric_definition':'Original physical affine g=d_sigma^2+(intercept+v*sigma)^2 du^2; native s=lambda*sigma, lambda is the unique original exact bridge ratio',
        'physical_entry_numerical':float(sigma0),'physical_length_numerical':float(length),
        'fixed_f_entry_numerical':float(f0),'v_exact_binary':str(slope),
        'raw_gamma_definition':'Exact rational Hermite cylindrical coefficients at native left; algebraic Cartesian conversion, no DFT or truncation',
        'new_gamma_definition':'center+(f(entry)/a_raw)*(gamma_raw-center); a_raw=(1/(2*pi))*integral_0^(2*pi)|gamma_raw_prime|; u=arc/a_raw',
        'fourier_degree':raw.degree,'arclength_raw_numerical':raw.a,'normalization_numerical':curve.normalization,
        'arc_quadrature':{'panels':args.panels,'gauss':args.gauss,'continuous_remainder_certified':False},
        'angles':args.angles,'continuous_angle_certificate':False,
        'minimum_sampled_Tu_norm':float(np.min(inlet['tangentDerivativeNorm'])),
        'minimum_sampled_n':float(np.min(n)),'maximum_sampled_abs_m_over_n':float(np.max(np.abs(k))),
        'minimum_sampled_B':float(np.min(B)),
        'minimum_sampled_focus':None if np.all(np.isinf(focus)) else float(np.min(focus)),
        'left_port_metric_sampled':float(np.max(zero['metric'])),
        'left_port_old_twojet_difference':{key:normmax(zero[key]-oldleft[key]) for key in oldleft},
        'inlet_frame_defects':{key:float(np.max(np.abs(v))) for key,v in supplier.inlet_defects(float(f0),float(slope),inlet).items()},
        'old_neighbor_ports_matched':False,'whole_closed_map_constructed':False,
        'exact_math_definition_not_rounded_quadrature_identification':True}
    try:
        end=supplier.at_material(float(f0),float(slope),float(length),u,lambda t:curve.inlet(t,float(slope)))
        oldright=old_packet(src,base.ld(right),u,base.ld(lam))
        result.update(right_port_success=True,right_port_metric_sampled=float(np.max(end['metric'])),
            right_port_old_twojet_difference={key:normmax(end[key]-oldright[key]) for key in oldright},
            minimum_sampled_D=float(min(float(f0),np.min(end['D']))),
            minimum_sampled_material_derivative=float(np.min(end['U_t'])),
            maximum_sampled_endpoint_curvature=float(max(np.max(zero['actual_curvature']),np.max(end['actual_curvature']))),
            maximum_sampled_endpoint_abs_K=float(max(np.max(np.abs(zero['actual_K'])),np.max(np.abs(end['actual_K'])))))
        np.savez_compressed(str(args.out)+'.ports.npz',u=u,**{'left_'+key:zero[key] for key in oldleft},
                           **{'right_'+key:end[key] for key in oldright},raw_modes=raw.modes,raw_coefficients=raw.coeff)
    except (ValueError,RuntimeError) as exc:
        result.update(right_port_success=False,right_port_error=str(exc))
    result['seconds']=time.monotonic()-start
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result,indent=2,allow_nan=False))


if __name__=='__main__':main()
