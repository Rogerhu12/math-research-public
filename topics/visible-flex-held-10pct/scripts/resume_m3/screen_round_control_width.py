#!/usr/bin/env python3
"""Sample the complete physical compact control for several transition widths.

The defining high-precision low-moment Gram inverse is unchanged.  This is a
read-only design screen, not a rho certificate, BVP, or accepted continuation.
Only coefficients and scalar diagnostics are saved, never sampled arrays.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import numpy as np


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--prefix',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--widths',type=float,nargs='+',default=[.03,.04,.06,.08,.10,.12,.16,.20])
    p.add_argument('--halfwidth',type=float,default=.21)
    p.add_argument('--flatten-transition',type=float,default=.08)
    p.add_argument('--samples',type=int,default=32768)
    p.add_argument('--precision',type=int,default=80)
    a=p.parse_args()
    lib=Path(__file__).with_name('round_core_lib');sys.path.insert(0,str(lib))
    from complementary_moment_basis import ComplementaryMomentBasis,_constants
    from couple_m3_smallcut_secant import accepted_anchor
    r=json.load(gzip.open(a.prefix,'rt'));accepted_anchor(r,a.prefix)
    q=r['actual_primary_amplitude'];n=r['config']['base_mode'];M=r['config']['modes']
    c=np.asarray(r['parameters'][1:])*np.asarray(r['central_correction_scales'])
    T=2*np.pi/n;center=T/2;x=T*np.arange(a.samples)/a.samples
    d=abs((x-center+T/2)%T-T/2);t=np.clip((d-a.halfwidth)/a.flatten_transition,0,1)
    chi=1-t**5*(126+t*(-420+t*(540+t*(-315+70*t))))
    f=n*n-1;smooth=-f*np.cos(n*x);C=f
    gx,gw=np.polynomial.legendre.leggauss(128);integral=0.
    for lo,hi in [(0,a.halfwidth),(a.halfwidth,a.halfwidth+a.flatten_transition)]:
        u=(lo+hi)/2+(hi-lo)/2*gx;tt=np.clip((u-a.halfwidth)/a.flatten_transition,0,1)
        cc=1-tt**5*(126+tt*(-420+tt*(540+tt*(-315+70*tt))))
        integral+=(hi-lo)/2*float(gw@(cc*(C-f*np.cos(n*u))))
    beta=-(2/T)*integral/(1-(2*a.halfwidth+a.flatten_transition)/T)
    target=smooth+chi*(C-smooth)+beta*(1-chi)
    lowrho=c@((1-(n*np.arange(2,M+1))**2)[:,None]*np.cos(n*np.arange(2,M+1)[:,None]*x))
    rho0=1+q*smooth+lowrho
    rows=[]
    for width in a.widths:
        # Use the exact defining formula without constructing positivity
        # certificates for every rejected design.  No physical solver imports
        # or uses this lightweight object.
        b=object.__new__(ComplementaryMomentBasis)
        b.n=n;b.M=M;b.a=a.halfwidth;b.eps=width;b.T=T;b.center=center;b.center_half_period=1
        k=_constants(n,M,a.halfwidth,width,1,a.precision,True)
        b.H=k['canonical_trig_coefficients'];b.fundamental_leakage=np.zeros(M-1)
        b.freq=n*np.arange(M+1);b.target_freq=b.freq[2:]
        jets=b.support_jets(x,4,1.)
        support=c@jets[0];control=c@(jets[0]+jets[2]);controlprime=c@(jets[1]+jets[3]);controlsecond=c@(jets[2]+jets[4])
        rho1=1+q*target+control;delta=rho1-rho0;negative=delta<0
        ratios=np.where(negative,(rho0-1e-5)/np.where(negative,-delta,1),np.inf)
        at=int(np.argmin(ratios));im=int(np.argmin(control));ip=int(np.argmax(control))
        row=dict(control_transition=width,support_gram_condition=k['support_condition'],
          high_precision_moment_residual=k['high_precision_moment_residual'],
          complete_control_support_linf=float(max(abs(support))),
          complete_control_rho_min=float(control[im]),complete_control_rho_min_phi=float(x[im]),
          complete_control_rho_max=float(control[ip]),complete_control_rho_max_phi=float(x[ip]),
          complete_control_rho_phi_linf=float(max(abs(controlprime))),
          complete_control_rho_phiphi_linf=float(max(abs(controlsecond))),
          full_rho_lambda_one_min=float(min(rho1)),full_rho_lambda_one_max=float(max(rho1)),
          first_sampled_positivity_failure_lambda=float(min(ratios)),
          first_sampled_positivity_failure_phi=float(x[at]))
        rows.append(row);print(json.dumps(row),flush=True)
    result=dict(scope=__doc__,input=str(a.prefix.resolve()),input_sha256=hashlib.sha256(a.prefix.read_bytes()).hexdigest(),
      source_sha256={str(z.resolve()):hashlib.sha256(z.read_bytes()).hexdigest() for z in
      [Path(__file__),lib/'complementary_moment_basis.py']},q=q,base_mode=n,modes=M,
      halfwidth=a.halfwidth,flatten_transition=a.flatten_transition,flatten_beta=beta,
      lock_fundamental=True,physical_corrections=c.tolist(),samples_per_sector=a.samples,
      old_complete_rho_min=float(min(rho0)),rows=rows,
      warning='Sampled suprema are lower bounds on actual suprema. The first sampled positivity failure is an upper bound on the positive initial homotopy interval, not an existence obstruction.')
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
