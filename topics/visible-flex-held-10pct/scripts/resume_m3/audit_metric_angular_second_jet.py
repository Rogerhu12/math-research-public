#!/usr/bin/env python3
"""Finite analytic angular second-jet diagnostic of the complete m3 metric.

The core, exact lift, original s-dependent chart and physical quintic are
retained.  The declared finite mean is fixed as the evaluation N changes.
All maxima and Fourier sums here are finite diagnostics, NOT continuous
bounds, interval arithmetic, or a replacement for original acceptance gates.
"""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key]="1"
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec)
    sys.modules[name]=out
    spec.loader.exec_module(out)
    return out


def xyz(z):
    return np.stack((z.real,z.imag,np.zeros_like(z.real)),axis=-1)


def op(c):
    return .5*(np.abs(c[...,0]+c[...,2])+
               np.sqrt((c[...,0]-c[...,2])**2+4*c[...,1]**2))


def third_basis(flow,N):
    """Third derivative of the original three-block rotating Fourier basis."""
    M=int(flow.M)
    if flow.n!=3*M+1:
        raise ValueError("Require the original complete rotating basis")
    psi=2*np.pi*np.arange(N)/N
    er=np.c_[np.cos(psi),np.sin(psi),np.zeros(N)]
    et=np.c_[-np.sin(psi),np.cos(psi),np.zeros(N)]
    ez=np.c_[np.zeros(N),np.zeros(N),np.ones(N)]
    result=np.zeros((flow.n,N,3))
    result[0]=-et
    for j,m in enumerate(np.asarray(flow.even,dtype=int)):
        co=np.cos(m*psi)[:,None];si=np.sin(m*psi)[:,None]
        result[1+j]=m*(m*m+3)*si*er-(3*m*m+1)*co*et
        result[M+1+j]=(3*m*m+1)*si*er-m*(m*m+3)*co*et
        result[2*M+1+j]=m**3*si*ez
    return result


def static_lift_third(flow,N,B3):
    core=getattr(flow,"exact_lift_core",None)
    if core is None:
        raise ValueError("This diagnostic requires the complete exact core lift")
    angular=flow.angular(N)
    theta,rho,rhop=angular[1:4]
    rhopp=9*(1-rho)
    g=core.evaluate(theta)
    if "kappa_u" not in g:
        raise ValueError("Analytic true material curvature derivative required")
    nu=np.exp(1j*g["phi"])
    gamma3=xyz(-(g["kappa_u"]+1j*g["kappa"]**2)*nu)
    core3=(gamma3*rho[:,None]**3+
           3*g["Ftt"]*(rho*rhop)[:,None]+g["Ft"]*rhopp[:,None])
    base3=xyz(np.exp(1j*theta)*(-3*rho*rhop+1j*(rhopp-rho**3)))
    projected=flow.values((flow.q*flow.exact_lift_initial)[:,None],B3)[0]
    return core3-base3-projected


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-run",type=Path,required=True)
    parser.add_argument("--physical",type=Path,required=True)
    parser.add_argument("--mean-nodes",type=int,required=True)
    parser.add_argument("--angular",type=int,nargs="+",default=[1168,2336])
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--batch",type=int,default=8)
    args=parser.parse_args()
    own=Path(__file__).parent
    adapter=module("_metric_twojet_adapter",own/"actual_m3_metric_model.py")
    audit=module("_metric_twojet_tools",own/"audit_full_relative_metric.py")
    record=json.loads(args.source_run.read_text())
    obj=adapter.load_model(record)
    physical=audit.load_physical(args.physical)
    obj.initial(physical.p)
    flow=obj.flow(physical.p[0])
    ss=np.unique(np.r_[np.linspace(0.,flow.end,151),physical.x,
                       (physical.x[:-1]+physical.x[1:])/2])
    Ns=sorted(set(args.angular))
    if min(Ns)<=2*(3*obj.M+1):
        raise ValueError("Evaluation grid does not resolve the finite field basis")
    _,B1m,B2m=flow.basis(args.mean_nodes)
    bases={N:flow.basis(N) for N in Ns}
    basis3={N:third_basis(flow,N) for N in Ns}
    lift3={N:static_lift_third(flow,N,basis3[N]) for N in Ns}
    rows={N:dict(angular=N,sample_operator_max=0.,sample_second_operator_max=0.,
                 second_peak=None,second_component_fft_l1=np.zeros(3),
                 second_vs_dft_second_max=0.) for N in Ns}
    for first in range(0,len(ss),args.batch):
        s=ss[first:first+args.batch];Y=physical.sol(s);Yp=physical.sol(s,1)
        mean=np.mean(flow.frame(s,obj.q*Y,B1m,B2m)["V"][:,:,2],axis=1)
        a=flow.profile(s)[0]
        # The installed exact_core_lift uses this unchanged default window.
        x=np.clip((s-.5*flow.prefix_end)/(.4*flow.prefix_end),0.,1.)
        chi=1-x**3*(10-15*x+6*x*x)
        for N in Ns:
            B,B1,B2=bases[N];g=flow.geo(s,N)
            rho,rhop,v,vp=g["rho"],g["rhop"],g["v"],g["vp"]
            rhopp=9*(1-rho)
            p3=xyz(a[:,None]*np.exp(1j*g["theta"])*
                   (-3*rho*rhop+1j*(rhopp-rho**3)))
            p3+=(a*chi)[:,None,None]*lift3[N][None,:,:]
            d=g["p1"]+obj.q*flow.values(Y,B1)
            dd=g["p2"]+obj.q*flow.values(Y,B2)
            ddd=p3+obj.q*flow.values(Y,basis3[N])
            Fsc=g["s1"]+obj.q*flow.values(Yp,B)
            Fsc[:,:,2]+=mean[:,None]
            Fsc1=g["sp"]+obj.q*flow.values(Yp,B1)
            Fsc2=g["spp"]+obj.q*flow.values(Yp,B2)
            vpp=-9*v-2*rhop*vp/rho-rhopp*v/rho
            U=Fsc-v[:,:,None]*d
            U1=Fsc1-vp[:,:,None]*d-v[:,:,None]*dd
            U2=Fsc2-vpp[:,:,None]*d-2*vp[:,:,None]*dd-v[:,:,None]*ddd
            V=d/(rho*a[:,None])[:,:,None]
            V1=(dd/rho[:,:,None]-d*(rhop/rho**2)[:,:,None])/a[:,None,None]
            V2=(ddd/rho[:,:,None]-2*dd*(rhop/rho**2)[:,:,None]+
                d*(2*rhop**2/rho**3-rhopp/rho**2)[:,:,None])/a[:,None,None]
            dot=lambda x,y:np.sum(x*y,axis=-1)
            E=np.stack((dot(U,U)-1,dot(U,V),dot(V,V)-1),axis=-1)
            E2=np.stack((2*(dot(U1,U1)+dot(U,U2)),
                         dot(U2,V)+2*dot(U1,V1)+dot(U,V2),
                         2*(dot(V1,V1)+dot(V,V2))),axis=-1)
            row=rows[N]
            row["sample_operator_max"]=max(row["sample_operator_max"],float(op(E).max()))
            values=op(E2);i,j=np.unravel_index(int(np.argmax(values)),values.shape)
            if float(values[i,j])>row["sample_second_operator_max"]:
                row["sample_second_operator_max"]=float(values[i,j])
                row["second_peak"]=dict(s=float(s[i]),psi=float(2*np.pi*j/N),
                    theta=float(g["theta"][i,j]),components=E2[i,j].tolist())
            coefficients=np.fft.fft(E2,axis=1)/N
            row["second_component_fft_l1"]=np.maximum(
                row["second_component_fft_l1"],np.sum(abs(coefficients),axis=1).max(axis=0))
            k=np.fft.fftfreq(N,d=1/N)
            spectral=np.fft.ifft(-(k*k)[None,:,None]*np.fft.fft(E,axis=1),axis=1).real
            row["second_vs_dft_second_max"]=max(row["second_vs_dft_second_max"],
                                               float(abs(E2-spectral).max()))
    for row in rows.values():
        row["second_component_fft_l1"]=row["second_component_fft_l1"].tolist()
    sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    report=dict(scope=__doc__,source_run=str(args.source_run.resolve()),
        source_run_sha256=sha(args.source_run),physical_sha256=sha(args.physical),
        source_sha256=sha(__file__),modes=int(obj.M),mean_nodes=args.mean_nodes,
        mean_scope="fixed finite periodic mean; no true-mean remainder supplied",
        radial_samples=len(ss),reference_lift_coefficient=1.,
        exact_lift_window=[.5,.9],analytic_gamma3_used=True,
        rows=list(rows.values()),continuous_angular_bound=False,
        continuous_radial_bound=False,original_acceptance_gates_changed=False,
        bvp_or_tail_solve_invoked=False)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()

