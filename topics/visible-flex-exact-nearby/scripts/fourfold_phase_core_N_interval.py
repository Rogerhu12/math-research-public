#!/usr/bin/env python3
"""Directed continuous N<0 gate for one explicitly symmetric R33 phase graph.

Uses the exact identity n=-a^2[(1+beta_theta)cos(gamma)<Fx,e_gamma>
                            -gamma_theta<Fx,e_phi>].
Radial spline intervals, finite-angle Lipschitz bounds, direct interval DFT,
and the infinite primitive tail are all retained. This is not a ray map or
an isometric-surface certificate. No Gaussian smoothing is applied.
"""
from __future__ import annotations

import argparse
from collections import deque
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np

from fourfold_phase_compare import load
from fourfold_phase_root_interval import (
    Box, SplineBox, SymmetricTarget, stack, sum_box, interval_dot,
    angular_grid, machin_pi,
)
from fourfold_phase_uniform_tail import up,down,mul_up,add_up


class ClosedSpanSplineBox(SplineBox):
    """The same interval polynomial evaluator, including both span endpoints.

All requested derivatives are <=3, and the stored splines are C4 on the
core. On a closed knot span they equal that span's polynomial limits.
The fifth Taylor coefficient can use its one-sided polynomial value.
"""
    def jets(self,x,order=3):
        center=float((float(x.lo)+float(x.hi))/2)
        point=Box(center);coefficients=[]
        for t,k,low,high in self.states:
            left=int(np.searchsorted(t,float(x.lo),side="right")-1)
            right=int(np.searchsorted(t,float(x.hi),side="left")-1)
            if float(x.lo)==float(x.hi):right=left
            if left!=right:
                raise ValueError("closed radial interval crosses an interior input knot")
            span=left
            d=[Box(low[span-k+j],high[span-k+j]) for j in range(k+1)]
            for level in range(1,k+1):
                for j in range(k,level-1,-1):
                    index=span-k+j
                    weight=(point-t[index])/(Box(t[index+k-level+1])-t[index])
                    d[j]=(1-weight)*d[j-1]+weight*d[j]
            coefficients.append(d[k])
        displacement=x-center;answer=[]
        for derivative in range(order+1):
            last=len(coefficients)-1-derivative
            value=coefficients[-1]/math.factorial(last)
            for power in range(last-1,-1,-1):
                value=value*displacement+coefficients[derivative+power]/math.factorial(power)
            answer.append(value)
        return stack(answer)


def materialize(checkpoint,output):
    solver,vector,metadata=load(checkpoint)
    coeff,alpha=solver.unpack(vector)
    positive=coeff.transpose(2,0,1)
    raw=np.concatenate((positive[::-1]*np.array([1.,-1.]),positive))
    base=solver.base_spline.component_spline
    result=dict(phase_knots=solver.knots,phase_coefficients=raw,
                base_knots=base.t,base_degree=base.k,base_radius_coefficients=base.c[:,0],
                alpha=alpha,shift_knots=solver.radius_shift.t,
                shift_degree=solver.radius_shift.k,shift_coefficients=solver.radius_shift.c,
                metadata=np.array(json.dumps(dict(
                    checkpoint_sha256=hashlib.sha256(checkpoint.read_bytes()).hexdigest(),
                    input_semantics="binary64 coefficients and knots define exact reals; explicit reflection is applied by SymmetricTarget",
                    parameters=metadata["parameters"]))))
    for j,w in enumerate(solver.mean_splines):
        sp=w.component_spline
        result.update({f"mean{j}_knots":sp.t,f"mean{j}_degree":sp.k,
                       f"mean{j}_radius_coefficients":sp.c[:,0]})
    for j,w in enumerate([solver.base_spline]+solver.mean_splines):
        result.update({f"height{j}_slope_knots":w.slope_spline.t,
                       f"height{j}_slope_coefficients":w.slope_spline.c,
                       f"height{j}_slope_degree":w.slope_spline.k,
                       f"height{j}_primitive_knots":w.primitive.t,
                       f"height{j}_primitive_coefficients":w.primitive.c,
                       f"height{j}_primitive_degree":w.primitive.k,
                       f"height{j}_floating_origin":w.origin})
    output.parent.mkdir(parents=True,exist_ok=True)
    np.savez_compressed(output,**result)


class CoreNGate:
    def __init__(self,frozen,quarter_nodes,angular_nodes):
        self.target=SymmetricTarget(frozen,quarter_nodes)
        for name in ("phase","base","shift"):
            old=getattr(self.target,name)
            replacement=ClosedSpanSplineBox.__new__(ClosedSpanSplineBox)
            replacement.states=old.states
            setattr(self.target,name,replacement)
        for name in ("means","slopes"):
            replacements=[]
            for old in getattr(self.target,name):
                replacement=ClosedSpanSplineBox.__new__(ClosedSpanSplineBox)
                replacement.states=old.states;replacements.append(replacement)
            setattr(self.target,name,replacements)
        sine,cosine=angular_grid(angular_nodes)
        modes=np.arange(1,self.target.modes+1)
        index=(np.arange(angular_nodes)[:,None]*modes[None,:])%angular_nodes
        self.cosine=Box(cosine.lo[index],cosine.hi[index])
        self.frequency=4*modes
        self.half_gap=(machin_pi()/(4*angular_nodes)).hi

    def evaluate(self,left,right):
        beta,gamma,radius,slope=self.target.scalars(Box(left,right))
        primitive=self.target.primitive(self.target.tangent(beta,gamma))
        fx=radius[1]*primitive[0]+radius[0]*primitive[1]
        lo,hi=fx.lo.copy(),fx.hi.copy()
        zz=Box(lo[0,2],hi[0,2])+slope[0]
        lo[0,2],hi[0,2]=zz.lo,zz.hi
        fx=Box(lo,hi)
        sigma,errors=self.target.tail_errors(beta,gamma,radius)
        tail=float(errors[0])
        beta_theta=interval_dot(self.cosine,(beta[0]*self.frequency).reshape(-1,1))
        gamma_theta=interval_dot(self.cosine,(gamma[0]*self.frequency).reshape(-1,1))
        beta_second=float(sum_box(Box(mul_up(beta[0].abs_upper(),self.frequency**2))).hi)
        gamma_second=float(sum_box(Box(mul_up(gamma[0].abs_upper(),self.frequency**2))).hi)
        p_lower=float((Box(1)+Box(float(beta_theta.lo.min()))
                       -Box(mul_up(self.half_gap,beta_second))).lo)
        gamma_first=float(add_up(float(gamma_theta.abs_upper().max()),
                                 mul_up(self.half_gap,gamma_second)))
        gamma_size=float(sum_box(Box(gamma[0].abs_upper())).hi)
        vertical_tail=float(sum_box(Box(fx[1:,2].abs_upper())).hi)
        z_lower=float((Box(float(fx.lo[0,2]))-vertical_tail-tail).lo)
        z_abs=float(add_up(float(sum_box(Box(fx[:,2].abs_upper())).hi),tail))
        # One real mode is (U cos(n theta), V sin(n theta)); its horizontal
        # Euclidean norm is bounded by max(|U|,|V|), including the mean mode.
        horizontal=float(add_up(float(sum_box(Box(np.maximum(
            fx[:,0].abs_upper(),fx[:,1].abs_upper()))).hi),tail))
        c_lower=float((Box(1)-Box(gamma_size)*gamma_size/2).lo)
        inner=float((Box(c_lower)*z_lower-Box(gamma_size)*horizontal).lo)
        valid=(p_lower>0 and c_lower>0 and inner>0 and radius.lo[0]>0)
        phi=float((Box(p_lower)*c_lower*inner-Box(gamma_first)*horizontal).lo)
        gate=bool(valid and phi>0)
        row=dict(interval=[left,right],passed=gate,positive_multiplier_conditions=bool(valid),
                 P_lower=p_lower,gamma_abs_upper=gamma_size,
                 gamma_theta_abs_upper=gamma_first,Fx_z_lower=z_lower,
                 Fx_z_abs_upper=z_abs,Fx_horizontal_upper=horizontal,
                 cos_gamma_lower=c_lower,normal_component_lower=inner,
                 N_factor_lower=phi,actual_a=radius[0].pair(),
                 primitive_Fx_tail_alias_upper=tail,tail_sigma=sigma)
        if gate:
            raw_lower=float((Box(float(radius.lo[0]))*float(radius.lo[0])*phi).lo)
            area_upper=float((Box(float(radius.hi[0]))*(Box(horizontal)+z_abs)).hi)
            normalized_upper=float((-Box(raw_lower)/area_upper).hi)
            row.update(raw_minus_n_lower=raw_lower,area_upper=area_upper,
                       actual_unit_normal_N_upper=normalized_upper)
        return row


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint",type=Path,required=True)
    parser.add_argument("--inputs",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--right",type=float,default=.24)
    parser.add_argument("--max-radial-step",type=float,default=.0005)
    parser.add_argument("--quarter-nodes",type=int,default=256)
    parser.add_argument("--angular-nodes",type=int,default=4096)
    parser.add_argument("--max-depth",type=int,default=12)
    parser.add_argument("--resume",action="store_true")
    args=parser.parse_args();started=time.monotonic()
    source_sha=hashlib.sha256(args.checkpoint.read_bytes()).hexdigest()
    if not args.inputs.exists():materialize(args.checkpoint,args.inputs)
    with np.load(args.inputs,allow_pickle=False) as stored:
        frozen={k:stored[k].copy() for k in stored.files}
    if json.loads(str(frozen["metadata"]))["checkpoint_sha256"]!=source_sha:
        raise ValueError("frozen input belongs to another geometry")
    inputs_sha=hashlib.sha256(args.inputs.read_bytes()).hexdigest()
    cuts=[0.,args.right]
    for name,value in frozen.items():
        if name.endswith("_knots"):
            cuts.extend(value.tolist());cuts.extend((-value).tolist())
    cuts=np.unique(cuts);cuts=cuts[(cuts>=0)&(cuts<=args.right)]
    pending=[]
    for left,right in zip(cuts[:-1],cuts[1:]):
        count=max(1,int(np.ceil((right-left)/args.max_radial_step)))
        split=np.linspace(left,right,count+1)
        pending.extend((float(a),float(b),0) for a,b in zip(split[:-1],split[1:]) if b>a)
    rows=[];failures=[]
    common=dict(kind="directed_continuous_core_N_gate_for_explicitly_symmetric_infinite_R33",
                source_checkpoint=str(args.checkpoint),source_sha256=source_sha,
                inputs=str(args.inputs),inputs_sha256=inputs_sha,
                core=[-args.right,args.right],quarter_nodes=args.quarter_nodes,
                angular_nodes=args.angular_nodes,max_radial_step=args.max_radial_step,
                run_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                dependency_sha256={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                                   for name in ("fourfold_phase_root_interval.py","fourfold_phase_uniform_tail.py",
                                                "fourfold_interval_scalar.py")},
                geometry="a,beta explicitly even; exact-integral Z,gamma explicitly odd; infinite R33 primitive; no Gaussian")
    if args.resume and args.out.exists():
        previous=json.loads(args.out.read_text())
        for key in ("inputs_sha256","run_source_sha256","quarter_nodes","angular_nodes","max_radial_step","core"):
            if previous[key]!=common[key]:raise ValueError("resume input changed: "+key)
        if previous["status"]=="complete":
            print(json.dumps({"progress":"matching complete N certificate already saved"}),flush=True);return
        rows=previous["rows"];failures=previous["failures"];pending=previous["pending"]
    gate=CoreNGate(frozen,args.quarter_nodes,args.angular_nodes)
    queue=deque(pending);attempts=0
    def save(status):
        report=dict(**common,status=status,rows=rows,failures=failures,pending=list(queue),
                    proved_continuous_N_negative=bool(status=="complete" and not failures),
                    limitations=["applies to this explicitly symmetric infinite R33 graph, not old approximate-mirror ray outputs",
                                 "IEEE correctly rounded elementary operations and outward nextafter interval kernel",
                                 "no complex theta tube or parameter-interval certificate supplied",
                                 "no exact isometric PDE solution or closed-surface claim"])
        if rows:
            report.update(minimum_N_factor_lower=min(r["N_factor_lower"] for r in rows),
                          minimum_raw_minus_n_lower=min(r["raw_minus_n_lower"] for r in rows),
                          maximum_unit_normal_N_upper=max(r["actual_unit_normal_N_upper"] for r in rows))
        args.out.write_text(json.dumps(report,indent=2)+"\n")
        return report
    while queue:
        left,right,depth=queue.popleft();attempts+=1
        row=gate.evaluate(left,right)
        if row["passed"]:rows.append(row)
        else:
            mid=float((left+right)/2)
            if depth<args.max_depth and left<mid<right:
                queue.appendleft((mid,right,depth+1));queue.appendleft((left,mid,depth+1))
            else:failures.append(row)
        if attempts%10==0:
            save("partial")
            print(json.dumps(dict(progress="interval N cells saved",passed=len(rows),
                                  failed=len(failures),pending=len(queue),
                                  elapsed_seconds=time.monotonic()-started)),flush=True)
    report=save("complete")
    print(json.dumps({k:v for k,v in report.items() if k not in ("rows","failures","pending")}),flush=True)
    if failures:raise SystemExit("N certificate failed on retained cells")


if __name__=="__main__":
    main()
