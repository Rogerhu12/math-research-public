#!/usr/bin/env python3
"""Own C2 position map: actual central ramp + exact-form full R137 coast.

The last polynomial ramp piece carries a full value/first/second radial jet
Hermite correction to the NEW exact-arc R137 inlet. Angular derivatives of
all three correction traces are computed from that same inlet. The metric
screen differentiates this actual composite map, not its intended frame.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import json
from pathlib import Path
import time
import numpy as np

import importlib.util
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('ramp_c2_source',HERE/'6a65-m12-central-ramp-hermite-flow.py')
ramp=importlib.util.module_from_spec(spec);spec.loader.exec_module(ramp)
ad=ramp.ad;LD=ramp.LD;CLD=ramp.CLD


class EndpointCurve(ad.supplier.Curve):
    def __init__(self,half,degree,panels=256,gauss=16):
        self.degree=degree;self.modes=np.arange(-degree,degree+1)
        self.coeff=np.stack([half[k] if k>=0 else np.conj(half[-k]) for k in self.modes]).astype(complex)
        self.panels,self.gauss,self.planar=panels,gauss,False
        x,w=np.polynomial.legendre.leggauss(gauss);self.gx,self.gw=(x+1)/2,w/2
        self.cuts=np.linspace(0,2*np.pi,panels+1);lo=self.cuts[:-1];width=np.diff(self.cuts)
        q=lo[:,None]+width[:,None]*self.gx
        speed=[]
        for j in range(0,q.size,512):speed.extend(np.linalg.norm(self.derivative(q.ravel()[j:j+512],1),axis=-1))
        lengths=width*np.sum(np.asarray(speed).reshape(q.shape)*self.gw,axis=-1)
        self.cumulative=np.r_[0,np.cumsum(lengths)];self.perimeter=self.cumulative[-1];self.a=self.perimeter/(2*np.pi)


def material_angle(raw,theta):
    theta=np.asarray(theta,float);cell=np.minimum(raw.panels-1,np.floor(theta/(2*np.pi)*raw.panels).astype(int))
    lo=raw.cuts[cell];q=lo[:,None]+(theta-lo)[:,None]*raw.gx
    speed=np.linalg.norm(raw.derivative(q.ravel(),1),axis=-1).reshape(q.shape)
    return (raw.cumulative[cell]+(theta-lo)*np.sum(speed*raw.gw,axis=1))/raw.a


def inlet_batched(curve,u,v):
    parts=[curve.inlet(u[j:j+64],v) for j in range(0,len(u),64)]
    return {k:np.concatenate([p[k] for p in parts]) for k in parts[0]}


def material_batched(curve,f0,v,x,u):
    parts=[ad.supplier.at_material(f0,v,x,u[j:j+64],lambda t:curve.inlet(t,v)) for j in range(0,len(u),64)]
    return {k:np.concatenate([p[k] for p in parts]) for k in parts[0] if isinstance(parts[0][k],np.ndarray) and parts[0][k].ndim>0}


def correction_traces(inlet,f0,density,density_t,old):
    n,m,nu,mu,nuu,muu=[np.asarray(inlet[k],dtype=LD) for k in ('n','m','n_u','m_u','n_uu','m_uu')]
    X,d,T,Tu,N,du,duu,Nu=[np.asarray(inlet[k],dtype=LD) for k in ('X','e1','e2','e2_u','N','e1_u','e1_uu','N_u')]
    col=lambda x:x[:,None]
    Nuu=-f0*(col(mu)*d+col(m)*du+col(nu)*T+col(n)*Tu)
    ell=m*m/n;ell_u=2*m*mu/n-m*m*nu/(n*n)
    ell_uu=2*(mu*mu+m*muu)/n-4*m*mu*nu/(n*n)-m*m*nuu/(n*n)+2*m*m*nu*nu/(n*n*n)
    values=np.stack((X,d,col(ell)*N))
    first=np.stack((f0*T,du,col(ell_u)*N+col(ell)*Nu))
    second=np.stack((f0*Tu,duu,col(ell_uu)*N+2*col(ell_u)*Nu+col(ell)*Nuu))
    new=np.stack((values,first*col(density),second*col(density*density)+first*col(density_t)),axis=1)
    return new-old


def observe(mesh,coeff,delta,density,candidate,N,gauss,patch_start):
    gx,gw=np.polynomial.legendre.leggauss(gauss);patch_end=ad.base.ld(candidate.R)
    ph=patch_end-patch_start
    pol=np.array([[0,0,0,10,-15,6],[0,0,0,-4*ph,7*ph,-3*ph],[0,0,0,ph*ph/2,-ph*ph,ph*ph/2]],dtype=LD)
    pd=pol[:,1:]*np.arange(1,6,dtype=LD)/ph
    pdd=pd[:,1:]*np.arange(1,5,dtype=LD)/ph
    coeff=np.asarray(coeff,dtype=CLD);peak=LD(0);curv=LD(0);support=LD('inf');energy=LD(0);where=None
    for j in range(len(mesh)-1):
        a,b=ad.base.ld(mesh[j]),ad.base.ld(mesh[j+1]);h=b-a
        c0,c1,c2=coeff[j,0],h*coeff[j,1],h*h*coeff[j,2]/2
        r0=coeff[j+1,0]-c0-c1-c2;r1=h*(coeff[j+1,1]-coeff[j,1])-2*c2;r2=h*h*(coeff[j+1,2]-coeff[j,2])
        p=np.stack((c0,c1,c2,10*r0-4*r1+r2/2,-15*r0+7*r1-r2,6*r0-3*r1+r2/2))
        for x,w in zip(gx,gw):
            t=(LD(x)+1)/2;s=a+h*t
            val=p[-1].copy();ds=5*p[-1];dss=20*p[-1]
            for k in range(4,-1,-1):val=val*t+p[k]
            for k in range(4,0,-1):ds=ds*t+k*p[k]
            for k in range(4,1,-1):dss=dss*t+k*(k-1)*p[k]
            X=ramp.evaluate_coeff(val,N);Xs=ramp.evaluate_coeff(ds/h,N);Xss=ramp.evaluate_coeff(dss/(h*h),N)
            Xt=ramp.evaluate_coeff(val,N,1);Xtt=ramp.evaluate_coeff(val,N,2);Xst=ramp.evaluate_coeff(ds/h,N,1)
            if s>=patch_start:
                q=(s-patch_start)/ph
                v=np.polynomial.polynomial.polyval(q,pol.T);dv=np.polynomial.polynomial.polyval(q,pd.T);ddv=np.polynomial.polynomial.polyval(q,pdd.T)
                X+=np.einsum('j,jnd->nd',v,delta[:,0]);Xs+=np.einsum('j,jnd->nd',dv,delta[:,0]);Xss+=np.einsum('j,jnd->nd',ddv,delta[:,0])
                Xt+=np.einsum('j,jnd->nd',v,delta[:,1]);Xtt+=np.einsum('j,jnd->nd',v,delta[:,2]);Xst+=np.einsum('j,jnd->nd',dv,delta[:,1])
            f=candidate.profile([s])[0][0];bb=f*density
            E=np.sum(Xs*Xs,axis=-1);F=np.sum(Xs*Xt,axis=-1);G=np.sum(Xt*Xt,axis=-1)
            ee,ff,gg=E-1,F/bb,G/(bb*bb)-1
            op=np.abs(ee+gg)/2+np.sqrt(((ee-gg)/2)**2+ff*ff);v=np.max(op)
            if v>peak:peak=v;where={'s':float(s),'cell':j,'angle_index':int(np.argmax(op))}
            normal=np.cross(Xs,Xt);normal/=np.sqrt(np.sum(normal*normal,axis=-1))[:,None]
            L,M,Nc=(np.sum(normal*z,axis=-1) for z in (Xss,Xst,Xtt));det=E*G-F*F
            tr=(G*L-2*F*M+E*Nc)/det;kg=(L*Nc-M*M)/det
            curv=max(curv,np.max(np.abs(tr)/2+np.sqrt(np.maximum(0,tr*tr/4-kg))))
            support=min(support,np.min(-np.sum(X*normal,axis=-1)))
            energy+=h*LD(w)/2*np.mean((ee*ee+2*ff*ff+gg*gg)*bb)
    return {'sampled_metric':float(peak),'sampled_curvature':float(curv),'sampled_support':float(support),
            'sampled_energy':float(energy),'peak_at':where,'radial_cells':len(mesh)-1,'gauss':gauss,'angular_nodes':N}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--field',type=Path,required=True);ap.add_argument('--report',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--coast-degree',type=int,required=True);ap.add_argument('--angular',type=int,default=1536);ap.add_argument('--gauss',type=int,default=8)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Fresh output required')
    start=time.monotonic();report=json.loads(args.report.read_text())
    if report['field_sha256']!=ad.sha(args.field):raise ValueError('Ramp field hash mismatch')
    with np.load(args.field,allow_pickle=False) as d:
        coeff=d['coefficients'].copy();mesh=[Q(int(a),int(b)) for a,b in zip(d['mesh_numerator'],d['mesh_denominator'])]
        central_c=[Q(int(a),int(b)) for a,b in zip(d['central_c_numerator'],d['central_c_denominator'])]
    meta=HERE.parent/'notes'/ad.base.META_NAME;candidate=ramp.OriginalRamp(json.loads(meta.read_text()))
    if mesh[-1]!=candidate.R:raise ValueError('Ramp field does not reach complete original ramp')
    N=args.angular;theta=np.arange(N,dtype=LD)*2*ad.base.PI/N
    central=ad.NativeCurve(central_c,512,32)
    gp=np.asarray(central.derivative(theta,1),dtype=LD);gpp=np.asarray(central.derivative(theta,2),dtype=LD)
    J=np.sqrt(np.sum(gp*gp,axis=-1));density=J/LD(central.a);density_t=np.sum(gp*gpp,axis=-1)/(J*LD(central.a))
    u=np.concatenate([material_angle(central,theta[j:j+64]) for j in range(0,N,64)])
    degree=min(args.coast_degree,coeff.shape[-2]-2)
    endpoint=EndpointCurve(coeff[-1,0],degree)
    f0q=1+candidate.vq*candidate.R/2;f0=LD(ad.base.ld(f0q));v=LD(candidate.v)
    curve=ad.FixedRadiusCurve(endpoint,float(f0));inlet=inlet_batched(curve,u,float(v))
    old=np.stack([np.stack([ramp.evaluate_coeff(coeff[-1,j],N,k) for k in range(3)]) for j in range(3)])
    delta=correction_traces(inlet,f0,density,density_t,old)
    patch_start=ad.base.ld(candidate.breaks[-2])
    observed=observe(mesh,coeff,delta,density,candidate,N,args.gauss,patch_start)
    length=candidate.Tu*(1-2*candidate.eps)
    coast=[]
    for q in (Q(0),Q(1,2),Q(1)):
        data=material_batched(curve,float(f0),float(v),float(length*q),u)
        coast.append({'fraction':str(q),'sampled_metric':float(np.max(data['metric'])),
                      'sampled_curvature':float(np.max(data['actual_curvature'])),'minimum_D':float(np.min(data['D'])),
                      'minimum_Ut':float(np.min(data['U_t'])),'sampled_support':float(np.min(-np.sum(data['X']*data['N'],axis=-1)))})
    out={'schema':'6a65-M12-actual-C2-ramp-to-exact-form-coast-v1','script_sha256':ad.sha(__file__),
         'ramp_report_sha256':ad.sha(args.report),'ramp_field_sha256':ad.sha(args.field),
         'dependencies':{name:ad.sha(HERE/name) for name in ('6a65-m12-central-ramp-hermite-flow.py','6a65-m12-r137-fixed-metric-adapter.py','6a65-geometry-r137-exact-inlet-consumer.py','fd2d_k0_ruling_coast.py')},
         'original_metric_unchanged':True,'coast_raw_curve_degree':degree,'coast_raw_arc_numerical':endpoint.a,
         'coast_radius_exact':str(f0q),'coast_length_exact':str(length),
         'patch_start_exact':str(candidate.breaks[-2]),'patch_end_exact':str(candidate.R),
         'correction_trace_norms':[[float(np.max(np.linalg.norm(delta[j,k],axis=-1))) for k in range(3)] for j in range(3)],
         'correction_definition':'Three right-end quintic Hermite traces on the complete last ramp polynomial piece, zero 0..2 radial jets at its left. Each trace is exact R137 inlet jet in the fixed central material chart minus the actual finite ramp endpoint jet. No angular reinterpolation of the correction.',
         'C2_gluing_is_an_exact_function_identity':True,'central_exact_reflection_jets_preserved':True,
         'actual_corrected_ramp_observer':observed,'coast_observations':coast,
         'continuous_nonfocal_domain_proof_for_this_new_curve':False,'whole_closed_surface_constructed':False,
         'seconds':time.monotonic()-start}
    np.savez_compressed(str(args.out)+'.coast-definition.npz',positive_cartesian_coefficients=coeff[-1,0,:degree+1],
                        central_c_numerator=np.asarray([str(x.numerator) for x in central_c]),
                        central_c_denominator=np.asarray([str(x.denominator) for x in central_c]))
    out['coast_definition_sha256']=ad.sha(str(args.out)+'.coast-definition.npz')
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps(out,indent=2,allow_nan=False))


if __name__=='__main__':main()
