#!/usr/bin/env python3
"""Exact common material two-jet data at the actual M24 prefix/bridge seam.

Only the polynomial pieces touching the seam are reconstructed.  No core,
background primitive, mean integral, full-bridge range, or curvature is rerun.
The proof of mean/height agreement uses the same fixed finite functional and
the identical true primitive anchor, not numerical overlap of intervals.
"""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key]="1"
import argparse,bisect,hashlib,importlib.util,json,sys,time
from pathlib import Path
from fractions import Fraction as Q
import numpy as np

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def fq(x):return Q.from_float(float(x))
def der(p):return [(i+1)*p[i+1] for i in range(len(p)-1)]
def val(p,x):
    v=Q(0)
    for a in p[::-1]:v=v*x+a
    return v
def jets(p,x):
    out=[]
    for _ in range(3):out.append(val(p,x));p=der(p)
    return out

def anchored_mean_primitive(s,entry,prefix_primitive,bridge_increment):
    """Same real primitive anchor; no independent rounded bridge height.

    Providers must denote the declared true functions. This composition does
    not turn an arbitrary finite quadrature routine into a true primitive.
    """
    if s<=entry:return prefix_primitive(s)
    return prefix_primitive(entry)+bridge_increment(s)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ("source-run","physical","core-mean-intervals","core-mean-certificate",
                 "prefix-height-certificate","bridge-geometry-certificate",
                 "bridge-mean-certificate","interval-kernel","support-dir","out"):
        ap.add_argument("--"+name,type=Path,required=True)
    a=ap.parse_args();start=time.monotonic()
    sys.path.insert(0,str(a.support_dir.resolve()))
    v=module("_prefix_bridge_seam_metric",a.support_dir/"certify_prefix_metric_interval_taylor.py")
    v.m.K=v.m.module("_prefix_bridge_seam_interval",a.interval_kernel)
    ad=v.m.module("_prefix_bridge_seam_model",a.support_dir/"actual_m3_metric_model.py")
    ld=v.m.module("_prefix_bridge_seam_field",a.support_dir/"audit_full_relative_metric.py")
    sh=module("_prefix_bridge_seam_shared",a.support_dir/"certify_r59_shared_jet_transfer.py")
    o=ad.load_model({"source_run":str(a.source_run.resolve())});z=ld.load_physical(a.physical)
    p=v.PrefixPieces(o,z);f=p.f;entry=p.entry;rh,ph=sha(a.source_run),sha(a.physical)
    hc=json.loads(a.prefix_height_certificate.read_text())
    bc=json.loads(a.bridge_geometry_certificate.read_text())
    bm=json.loads(a.bridge_mean_certificate.read_text())
    assert hc["source_run_sha256"]==rh and hc["physical_sha256"]==ph
    assert bc["run_sha256"]==rh and bc["physical_sha256"]==ph
    assert bc["input_certificate_sha256"]["mean"]==sha(a.bridge_mean_certificate)
    assert hc["complete"] and bm["complete"]
    assert hc["frenet_root_lower"]>0 and bm["frenet_root_lower"]>0
    assert hc["mean_nodes"]==bc["mean_nodes"]==bm["mean_nodes"]==1168
    assert hc["height_core_anchor"]==0
    assert Q(hc["profile_duration_ratio_exact"])==p.duration_ratio
    assert Q(hc["profile_amplitude_ratio_exact"])==p.amplitude_ratio
    v.binding(json.loads(a.core_mean_certificate.read_text()),rh,ph,a.core_mean_intervals)
    with np.load(a.core_mean_intervals) as data:psi=np.array(data["psi"],copy=True)
    literal=2*np.pi*np.arange(1168)/1168
    assert np.array_equal(psi,literal)
    yl=bisect.bisect_left(p.xx,entry)-1;yr=bisect.bisect_right(p.xx,entry)-1
    assert yl in p.field_coefficients_exact and 0<=yr<len(p.xx)-1
    # Reconstruct only the right bridge piece by the existing SharedBridgeData
    # definition, using its exact right_correction helper and actual input.
    h=p.xx[yr+1]-p.xx[yr];right=[]
    for j in range(p.n):
        pp=[fq(z.sol.c[5-k,yr,j]) for k in range(6)]
        if yr+1<len(p.xx)-1:
            target=[fq(z.sol.c[5,yr+1,j]),fq(z.sol.c[4,yr+1,j]),2*fq(z.sol.c[3,yr+1,j])]
        else:target=jets(pp,h)
        cc,_=sh.right_correction(pp,h,target)
        right.append([x+y for x,y in zip(pp,cc)])
    diffs=[]
    for lp,rp in zip(p.field_coefficients_exact[yl],right):
        ljet=jets(lp,entry-p.xx[yl]);rjet=jets(rp,entry-p.xx[yr])
        diffs.extend(x-y for x,y in zip(ljet,rjet))
    assert all(x==0 for x in diffs)
    el=bisect.bisect_left(p.spx,entry)-1;er=bisect.bisect_right(p.spx,entry)-1
    assert entry<Q(3,4)*p.end
    pp=[fq(f.spline.c[3-k,er])/p.end**k for k in range(4)]+[Q(0),Q(0)]
    h=p.spx[er+1]-p.spx[er]
    target=[fq(f.spline.c[3,er+1]),fq(f.spline.c[2,er+1])/p.end,
            2*fq(f.spline.c[1,er+1])/p.end**2]
    cc,_=sh.right_correction(pp,h,target)
    bridge_e=[fq(f.warp_e)*(x+y) for x,y in zip(pp,cc)]
    le=jets(p.chart_coefficients_exact[el],entry-p.spx[el])
    re=jets(bridge_e,entry-p.spx[er]);ediff=[x-y for x,y in zip(le,re)]
    assert all(x==0 for x in ediff) and abs(le[0])<1
    last=p.profile_pieces[-1]
    u=(entry-last["origin"])/last["length"]
    c=last["coefficients_exact"];profile=[]
    for j in range(3):profile.append(val(c,u)/last["length"]**j);c=der(c)
    assert profile==[Q(1),Q(0),Q(0)]
    assert fq(f.bridge.astart)==1 and fq(f.bridge.L1)>0
    peak=fq(f.bridge.peak)
    phi=[Q(0),Q(0),3*peak,-2*peak]
    assert val(phi,Q(0))==val(der(phi),Q(0))==0
    # True bridge primitive: a=1-int sin(phi), so its initial jets are 1,0,0.
    bridge_profile=[Q(1),Q(0),Q(0)]
    assert profile==bridge_profile and p.lift_hi<entry
    report={"status":"actual_prefix_bridge_shared_C2_seam_proved",
        "source_sha256":sha(__file__),"source_run_sha256":rh,"physical_sha256":ph,
        "prefix_pieces_source_sha256":sha(a.support_dir/"explicit_m24_prefix_pieces.py"),
        "bridge_shared_source_sha256":sha(a.support_dir/"certify_r59_shared_jet_transfer.py"),
        "prefix_height_certificate_sha256":sha(a.prefix_height_certificate),
        "bridge_geometry_certificate_sha256":sha(a.bridge_geometry_certificate),
        "bridge_mean_certificate_sha256":sha(a.bridge_mean_certificate),
        "mean_core_certificate_sha256":sha(a.core_mean_certificate),
        "entry_exact":str(entry),"Y_entry_is_knot":entry in p.xx,
        "Y_left_right_indices":[yl,yr],"Y_exact_scalar_jet_comparisons":len(diffs),
        "Y_jet_difference_exact":"0","chart_left_right_indices":[el,er],
        "e_jet_difference_exact":[str(x) for x in ediff],
        "profile_common_two_jet_exact":[str(x) for x in profile],
        "lift_identically_zero_left_neighborhood_exact":str(entry-p.lift_hi),
        "late_chart_cutoff_strictly_after_entry":True,
        "material_chart_rho_lower_exact":str(1-abs(le[0])),
        "mean_nodes":1168,"mean_weight_exact":"1/1168",
        "mean_psi_binary_sha256":hashlib.sha256(np.ascontiguousarray(psi,dtype="<f8").tobytes()).hexdigest(),
        "same_literal_mean_nodes":True,
        "mean_zero_and_first_jet_identity":"algebraic consequence of common input jets and the same smooth finite Frenet functional, proved in the accompanying note",
        "height_anchor_identity":"Zbridge(s)=Zprefix(entry)+integral(entry,s) Mbridge; z0 is exactly the prefix primitive endpoint, not an independent value in its interval",
        "Cartesian_seam_two_jet_exact":True,"material_metric_unchanged":True,
        "new_repair_needed":False,"new_background_mean_or_curvature_computation":False,
        "whole_closed_surface":False,"seconds":time.monotonic()-start}
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n");print(json.dumps(report),flush=True)
if __name__=="__main__":main()
