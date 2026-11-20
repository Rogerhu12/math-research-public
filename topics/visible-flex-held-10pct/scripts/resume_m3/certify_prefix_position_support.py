#!/usr/bin/env python3
"""Continuous position/support of the same explicit true-core M24 prefix.

Reuses the completed true-core angular boxes, exact shared-Hermite pieces and
normalized profile. The already-certified fixed-1168 mean range pays both M(s)
and its height primitive. No mean integral, BVP, core, or curvature is rerun.
"""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key]="1"
import argparse,hashlib,importlib.util,json,sys,time
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
import mpmath as mp

def module(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s)
    sys.modules[name]=m;s.loader.exec_module(m);return m
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def fq(x):return Q.from_float(float(x))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("source-run","physical","core-angle-intervals","core-angle-certificate",
                "mean-range-certificate","interval-kernel","support-dir","out"):
        p.add_argument("--"+key,type=Path,required=True)
    p.add_argument("--max-cells",type=int,default=20000)
    a=p.parse_args();started=time.monotonic()
    sys.path.insert(0,str(a.support_dir.resolve()))
    v=module("_held10_position_support_kernel",a.support_dir/"certify_prefix_metric_interval_taylor.py")
    v.m.K=v.m.module("_held10_position_interval_kernel",a.interval_kernel)
    I,D=v.I,v.D
    ad=v.m.module("_held10_position_model",a.support_dir/"actual_m3_metric_model.py")
    ld=v.m.module("_held10_position_field",a.support_dir/"audit_full_relative_metric.py")
    o=ad.load_model({"source_run":str(a.source_run.resolve())});z=ld.load_physical(a.physical)
    pieces=v.PrefixPieces(o,z);rh,ph=sha(a.source_run),sha(a.physical)
    ac=json.loads(a.core_angle_certificate.read_text())
    v.binding(ac,rh,ph,a.core_angle_intervals)
    mc=json.loads(a.mean_range_certificate.read_text())
    assert mc["source_run_sha256"]==rh and mc["physical_sha256"]==ph
    assert mc["complete"] and mc["height_window_passed"] and mc["height_core_anchor"]==0
    assert mc["mean_nodes"]==1168
    assert Q(mc["profile_amplitude_ratio_exact"])==pieces.amplitude_ratio
    assert Q(mc["profile_duration_ratio_exact"])==pieces.duration_ratio
    lower,upper=Q(805,1000),Q(1000001,1000000)
    assert fq(mc["finite_mean_value_range"][0])>lower
    assert fq(mc["finite_mean_value_range"][1])<upper
    mi=I(I.rational(lower).x[0],I.rational(upper).x[1])
    # Only the .v components are used. Zero auxiliary derivative slots do not
    # assert that the true varying M has zero radial derivatives.
    mean=v.constant(mi)
    with np.load(a.core_angle_intervals) as data:
        bt=v.AngleTable(data["psi_lo"],data["psi_hi"],pieces.f.even)
        bt.build_lift(data,pieces.f,"box",pieces.q)
        assert np.array_equal(bt.hi[:-1],bt.lo[1:]) and bt.lo[0]==0
        mp.iv.dps=70
        assert bt.hi[-1]>=v.m.K.up(float((2*mp.iv.pi).b))
        step=float(np.max((I(bt.hi)-I(bt.lo)).x[1]))
    obj=v.PrefixMetric(pieces,None,None,bt,step)
    report={"status":"running","source_sha256":sha(__file__),
        "source_run_sha256":rh,"physical_sha256":ph,
        "core_angle_certificate_sha256":sha(a.core_angle_certificate),
        "core_angle_intervals_sha256":sha(a.core_angle_intervals),
        "mean_range_certificate_sha256":sha(a.mean_range_certificate),
        "metric_kernel_source_sha256":sha(a.support_dir/"certify_prefix_metric_interval_taylor.py"),
        "pieces_source_sha256":sha(a.support_dir/"explicit_m24_prefix_pieces.py"),
        "derivative_kernel_source_sha256":sha(a.support_dir/"certify_bridge_metric_fourier_taylor.py"),
        "interval_wrapper_source_sha256":sha(a.support_dir/"certify_r59_fixed_mean_ranges.py"),
        "interval_kernel_sha256":sha(a.interval_kernel),
        "frozen_projection_binary_sha256":hashlib.sha256(np.ascontiguousarray(
            pieces.f.exact_lift_initial,dtype="<f8").tobytes()).hexdigest(),
        "mean_nodes":1168,"angular_boxes":bt.N,
        "mean_value_range_exact":[str(lower),str(upper)],
        "height_primitive_contract":"Z(0)=0; .805*s <= Z(s) <= 1.000001*s from the same true fixed mean",
        "normal_orientation":"-U cross V / |U cross V|, with U=F_s and V=F_theta/a",
        "radius_target_exact":"67/50","support_target_exact":"87/1000",
        "accepted":0,"attempted":0,"splits":0,
        "radius_upper":0.,"support_lower":None,"normal_cross_length_lower":None,
        "complete_surface":False,"curvature_computed":False,
        "source_field_modified":False,"mean_or_core_recomputed":False}
    a.out.parent.mkdir(parents=True,exist_ok=True)
    def save():
        report["seconds"]=time.monotonic()-started
        a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    def enclose(left,right):
        data=obj.data(left,right,"radial")
        aa,chi=data[2],data[6]
        er,_,_,_,_=obj.frame(bt,data,"radial")
        basis=bt.basis(data[0],"radial",0)[0]
        h0=bt.lift(0,"radial")
        zz=I(I.rational(lower*left).x[0],I.rational(upper*right).x[1])
        F=[aa.v*er[k].v+basis[k].v+(aa*chi).v*h0[k].v+(zz if k==2 else I(0))
           for k in range(3)]
        _,U,V,_,_=obj.metric(bt,data,mean,"radial",True)
        u,w=[x.v for x in U],[x.v for x in V]
        cross=[u[1]*w[2]-u[2]*w[1],u[2]*w[0]-u[0]*w[2],u[0]*w[1]-u[1]*w[0]]
        length=sum((x.sq() for x in cross),I(0)).sqrt()
        if np.any(length.x[0]<=0):raise ArithmeticError("Normal length not separated from zero")
        normal=[-x/length for x in cross]
        radius=sum((x.sq() for x in F),I(0)).sqrt()
        support=sum((x*y for x,y in zip(F,normal)),I(0))
        ri=int(np.argmax(radius.x[1]));si=int(np.argmin(support.x[0]))
        return (float(radius.x[1][ri]),float(support.x[0][si]),float(np.min(length.x[0])),
            [float(bt.lo[ri]),float(bt.hi[ri])],[float(bt.lo[si]),float(bt.hi[si])])
    todo=[(l,r,0) for l,r in zip(pieces.grid[:-1],pieces.grid[1:])][::-1]
    while todo:
        left,right,depth=todo.pop();report["attempted"]+=1
        try:
            radius,support,normlo,ra,sa=enclose(left,right)
            passed=fq(radius)<Q(67,50) and fq(support)>Q(87,1000)
            reason="position or support interval target not paid"
        except (ValueError,ArithmeticError,FloatingPointError) as exc:
            passed=False;radius=None;support=None;reason=str(exc)
        if passed:
            report["accepted"]+=1
            if radius>report["radius_upper"]:
                report.update(radius_upper=radius,radius_peak_s=[float(left),float(right)],radius_peak_psi=ra)
            if report["support_lower"] is None or support<report["support_lower"]:
                report.update(support_lower=support,support_peak_s=[float(left),float(right)],support_peak_psi=sa)
            report["normal_cross_length_lower"]=normlo if report["normal_cross_length_lower"] is None else min(
                normlo,report["normal_cross_length_lower"])
        else:
            if depth>=24 or report["accepted"]+len(todo)>=a.max_cells:
                report.update(status="position_support_not_resolved",unresolved_s=[float(left),float(right)],
                    unresolved_reason=reason,last_radius=radius,last_support=support,remaining=len(todo)+1)
                save();print(json.dumps(report),flush=True);return
            middle=(left+right)/2
            todo.extend([(middle,right,depth+1),(left,middle,depth+1)]);report["splits"]+=1
        if report["attempted"]%25==0:
            save();print(json.dumps({k:report[k] for k in ("status","accepted","attempted","splits",
                "radius_upper","support_lower","seconds")}),flush=True)
    report.update(status="continuous_prefix_position_and_support_certified",
        scope=["All radial pieces and all angular closed boxes are covered, including one-sided joins",
            "Same true R53 core, shared Hermite Y/e, endpoint-normalized profile and frozen finite 1168 mean",
            "The mean/height are range enclosures; no mean derivative, core integral or curvature was recomputed",
            "No whole closed surface, exact inlet-cylinder seam or true nonlinear tail is asserted"])
    save();print(json.dumps(report),flush=True)
if __name__=="__main__":main()
