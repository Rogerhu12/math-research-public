#!/usr/bin/env python3
"""One actual fixed-polar-radius/positive Bernstein-height point budget.

The conditional algebra is exact. This executable evaluates its constants
in binary64; its output is not a continuous interval certificate.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, sys, time
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
from scipy.special import comb

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m
    spec.loader.exec_module(m);return m

def main():
    ap=argparse.ArgumentParser()
    for name in ("scripts","polar-source","ramp-master","coast-master","output"):
        ap.add_argument("--"+name,type=Path,required=True)
    ap.add_argument("--theta",type=float,default=np.pi/2)
    ap.add_argument("--reach-radius",type=float,default=.097)
    ap.add_argument("--bracket",type=float,nargs=2,default=[.75,.85])
    args=ap.parse_args()
    if args.output.exists(): raise FileExistsError("Fresh numerical point budget required")
    started=time.monotonic()
    m=module(args.polar_source,"nonfold_actual_point_budget")
    field=m.NonfoldPolarConnector(args.scripts,args.ramp_master,args.coast_master)
    theta=np.asarray([args.theta])
    left,left_error=field.inverse(0,theta);right,right_error=field.inverse(1,theta)
    data=np.concatenate((left["logrho"],right["logrho"]),axis=0)
    def profile(t):
        q=np.stack([np.einsum("i,ijk->jk",
            field.warm.ports.hermite_weights(t,field.L,j),data) for j in range(3)])
        rho=float(np.exp(q[0,0,0]))
        return dict(rho=rho,rho_s=rho*float(q[1,0,0]),
            rho_ss=rho*float(q[2,0,0]+q[1,0,0]**2),
            rho_theta=rho*float(q[0,1,0]))
    t=float(brentq(lambda x:profile(x)["rho_s"],*args.bracket,xtol=5e-15))
    radial=profile(t)
    n,L=field.degree,field.L
    lz,rz=left["z"],right["z"]
    controls=np.array([lz[1,0,0],lz[1,0,0]+L*lz[2,0,0]/n,
        rz[1,0,0]-L*rz[2,0,0]/n,rz[1,0,0]],float)
    total=(n+1)*float(rz[0,0,0]-lz[0,0,0])/L-np.sum(controls)
    k=np.arange(n+1);bern=comb(n,k)*t**k*(1-t)**(n-k)
    endpoint=float(controls@bern[[0,1,n-1,n]])
    j=int(np.argmax(bern[2:-2]))+2
    upper=endpoint+total*float(bern[j])
    # At rho_s=0, normal curvature in the vertical tangent direction is
    # |rho*rho_ss|/(z_s^2*sqrt(rho^2+rho_theta^2)). No reflection is assumed.
    normal_factor=radial["rho"]/np.hypot(radial["rho"],radial["rho_theta"])
    required=float(np.sqrt(args.reach_radius*abs(radial["rho_ss"])*normal_factor))
    out=dict(schema="6a65-fixed-polar-radius-positive-height-point-budget-v2",
        sourceSHA256=sha(__file__),polarSourceSHA256=sha(args.polar_source),
        rampMasterSHA256=sha(args.ramp_master),coastMasterSHA256=sha(args.coast_master),
        parameters=dict(theta=args.theta,reachRadius=args.reach_radius,bracket=args.bracket,
            degree=n,L=L,b=field.b,amplitude=field.master.amplitude,Z=field.master.Z),
        point=dict(s=field.b+L*t,t=t,**radial,normalProjectionFactor=float(normal_factor)),
        inverseResidual=max(left_error,right_error),
        endpointVelocityControls=controls.tolist(),interiorControlMass=float(total),
        maximizingInteriorIndex=j,maximizingBernsteinValue=float(bern[j]),
        endpointContribution=endpoint,sharpNonnegativeControlHeightUpperBound=float(upper),
        necessaryHeightSpeedForOwnPrincipalCurvatureLimit=required,
        deficit=required-upper,
        conditionalFormulaExact=True,numericalInstantiationOnly=True,
        reflectionAssumptionUsed=False,continuousCertificate=False,
        actualOptimizationAttempts=0,seconds=time.monotonic()-started)
    if total<=0 or np.min(controls)<0: raise ValueError("Positive-control hypothesis failed")
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2,allow_nan=False)+"\n")
    print(json.dumps(dict(reportSHA256=sha(args.output),**out),allow_nan=False),flush=True)

if __name__=="__main__": main()
