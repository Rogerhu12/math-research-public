#!/usr/bin/env python3
"""Finite Fourier conjugacy/actual-parameter exploration for two sampled maps.

The p-family used here is the affine interpolation of two independently
computed principal maps, not the exact geometric p-family. Its solution is
an initializer that must be checked on a newly saved geometry and actual
ray nodes. Intermediate translation continuation is only an initializer.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.interpolate import CubicHermiteSpline


TWOPI = 2*np.pi


def target_value(name):
    if name == "D5":
        return (15121+np.sqrt(5))/27422
    if name == "D8":
        return (4852+np.sqrt(8))/8804
    raise ValueError(name)


class MapFamily:
    def __init__(self, first, second):
        self.first, self.second = first, second
        self.length = float(first["angular_period"])
        self.scale = TWOPI/self.length
        if (second["angular_period"] != self.length or
                first["initial_angles"] != second["initial_angles"]):
            raise ValueError("two maps need exactly the same angular grid")
        self.splines = []
        for saved in (first, second):
            xx = np.r_[saved["initial_angles"], self.length]
            yy = np.r_[saved["returned_angles"], saved["returned_angles"][0]+self.length]
            dd = np.r_[saved["angular_derivative"], saved["angular_derivative"][0]]
            self.splines.append(CubicHermiteSpline(xx, yy, dd))

    def each(self, x, derivative=0):
        x = np.asarray(x)
        winding = np.floor(x/TWOPI)
        theta = (x-winding*TWOPI)/self.scale
        values = np.stack([s(theta, nu=derivative) for s in self.splines])
        if derivative == 0:
            values = self.scale*values+winding*TWOPI
        else:
            values = values*self.scale**(1-derivative)
        return values

    def map(self, parameter, x, derivative=0):
        first, second = self.each(x, derivative)
        return first+parameter*(second-first)

    def column(self, x, derivative=0):
        first, second = self.each(x, derivative)
        return second-first


def frequencies(size):
    return np.fft.fftfreq(size)*size


def coefficients(values):
    return np.fft.fft(values)/len(values)


def evaluate(values, x, derivative=0):
    k = frequencies(len(values))
    return np.real(np.exp(1j*np.outer(np.asarray(x), k))
                   @ (coefficients(values)*(1j*k)**derivative))


def dense_checks(values, count=None):
    size = count or 8*len(values)
    x = np.arange(size)*TWOPI/size
    h = evaluate(values, x)
    hp = 1+evaluate(values, x, 1)
    return x, h, hp


def newton(family, rho, h, parameter, *, homotopy=None,
           guess_parameter=.4, maximum_steps=30):
    size = len(h)
    x = np.arange(size)*TWOPI/size
    k = frequencies(size)
    identity = np.eye(size)
    shift = np.fft.ifft(np.exp(1j*k*TWOPI*rho)[:,None]
                        *np.fft.fft(identity,axis=0),axis=0).real
    history=[]
    alpha=TWOPI*rho
    def quantities(values, p):
        H=x+values
        if homotopy is None:
            mapped=family.map(p,H)
            space=family.map(p,H,1)
            column=family.column(H)
        else:
            mapped=H+alpha+homotopy*(family.map(guess_parameter,H)-H-alpha)+p
            space=1+homotopy*(family.map(guess_parameter,H,1)-1)
            column=np.ones_like(H)
        error=mapped-x-alpha-shift@values
        return error,space,column
    for step in range(maximum_steps):
        error,space,column=quantities(h,parameter)
        residual=float(np.max(np.abs(error)))
        _,_,hp=dense_checks(h,4*size)
        entry=dict(step=step,parameter=float(parameter),collocation_residual=residual,
                   sampled_minimum_Hprime=float(hp.min()))
        history.append(entry)
        if residual < 2e-12:
            return h,parameter,history
        matrix=np.empty((size+1,size+1))
        matrix[:-1,:-1]=np.diag(space)-shift
        matrix[:-1,-1]=column
        matrix[-1,:-1]=1/size
        matrix[-1,-1]=0.
        rhs=np.r_[-error,-np.mean(h)]
        correction=np.linalg.solve(matrix,rhs)
        accepted=False
        for exponent in range(18):
            damping=2.**(-exponent)
            hh=h+damping*correction[:-1]
            pp=parameter+damping*correction[-1]
            if homotopy is None and not -.25 < pp < 1.25:
                continue
            _,_,hpp=dense_checks(hh,4*size)
            if hpp.min() <= 1e-5:
                continue
            ee,_,_=quantities(hh,pp)
            if np.max(np.abs(ee)) < residual*(1-1e-4*damping):
                h,parameter,accepted=hh,pp,True
                entry["damping"]=damping
                break
        if not accepted:
            entry["stopped"]="line search could not reduce residual with positive sampled Hprime"
            return h,parameter,history
    return h,parameter,history


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-map",type=Path,required=True)
    parser.add_argument("--probe-map",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--checkpoint",type=Path,required=True)
    parser.add_argument("--target",choices=["D5","D8"],default="D5")
    parser.add_argument("--sizes",type=int,nargs="+",default=[65,129,257])
    parser.add_argument("--initial-conjugacy",type=Path)
    parser.add_argument("--initial-parameter",type=float,default=.4)
    args=parser.parse_args()
    base=json.loads(args.base_map.read_text())
    probe=json.loads(args.probe_map.read_text())
    family=MapFamily(base,probe)
    rho=target_value(args.target)
    h=np.zeros(args.sizes[0]);counterterm=0.;history=[]
    if args.initial_conjugacy:
        with np.load(args.initial_conjugacy,allow_pickle=False) as saved:
            h=evaluate(saved["h_values"],np.arange(args.sizes[0])*TWOPI/args.sizes[0])
    else:
        for lam in np.arange(.1,1.01,.1):
            h,counterterm,steps=newton(family,rho,h,counterterm,homotopy=lam)
            history.append(dict(stage="translation initializer",lambda_value=float(lam),steps=steps))
            print(json.dumps(dict(stage="translation initializer",lambda_value=float(lam),
                                  last=steps[-1])),flush=True)
    parameter=args.initial_parameter
    levels=[]
    for size in args.sizes:
        if len(h)!=size:
            h=evaluate(h,np.arange(size)*TWOPI/size)
        h,parameter,steps=newton(family,rho,h,parameter)
        x,hh,hp=dense_checks(h,16*size)
        error=family.map(parameter,x+hh)-x-TWOPI*rho-evaluate(h,x+TWOPI*rho)
        column=family.column(x+hh)
        shifted_hp=1+evaluate(h,x+TWOPI*rho,1)
        level=dict(size=size,parameter=float(parameter),steps=steps,
                   sampled_residual_max=float(np.max(np.abs(error))),
                   sampled_Hprime_range=[float(hp.min()),float(hp.max())],
                   sampled_weighted_twist=float(np.mean(column/shifted_hp)),
                   sampled_twist_integrand_range=[float(np.min(column/shifted_hp)),
                                                  float(np.max(column/shifted_hp))])
        levels.append(level)
        print(json.dumps({key:value for key,value in level.items() if key!="steps"}),flush=True)
    metadata=dict(kind="floating_affine_map_initializer_not_actual_geometric_conjugacy",
                  base_map_sha256=hashlib.sha256(args.base_map.read_bytes()).hexdigest(),
                  probe_map_sha256=hashlib.sha256(args.probe_map.read_bytes()).hexdigest(),
                  base_source_sha256=base["source_sha256"],
                  probe_source_sha256=probe["source_sha256"],target=args.target,
                  rotation_number=rho,parameter=float(parameter),angular_scale=family.scale)
    if args.initial_conjugacy:
        metadata["initial_conjugacy_sha256"]=hashlib.sha256(args.initial_conjugacy.read_bytes()).hexdigest()
    np.savez_compressed(args.checkpoint,h_values=h,metadata=np.array(json.dumps(metadata)))
    report=dict(**metadata,initializer_history=history,levels=levels,
                checkpoint_sha256=hashlib.sha256(args.checkpoint.read_bytes()).hexdigest(),
                limitations=["affine combination of sampled maps, not exact geometry family",
                             "finite Fourier and angular sampling; no norm or roundoff certificate",
                             "intermediate translation is only a numerical initializer",
                             "tiny binary reflection defect remains unpaid",
                             "real-node estimates are not R31 Wiener inputs or a KAM theorem application"])
    args.out.write_text(json.dumps(report,indent=2)+"\n")


if __name__=="__main__":
    main()
