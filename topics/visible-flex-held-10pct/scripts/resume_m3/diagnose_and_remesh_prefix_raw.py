#!/usr/bin/env python3
"""Diagnose an actual returned prefix cubic and prepare a full-field remesh seed.

No Newton step, relaxed tolerance, increased node budget or acceptance claim is
made. All state components and actual parameters come from the returned cubic.
"""
import argparse, hashlib, importlib.util, json, sys
from pathlib import Path
import numpy as np
from scipy.interpolate import PPoly
from scipy.integrate import _bvp

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source-run",type=Path,required=True)
    ap.add_argument("--raw",type=Path)
    ap.add_argument("--nodes",type=int,default=401)
    ap.add_argument("--outdir",type=Path,required=True)
    a=ap.parse_args()
    a.outdir.mkdir(parents=True,exist_ok=False)
    report=a.outdir/"diagnostic.json"
    result=dict(status="loading",scope=__doc__,complete_surface=False,
                accepted_bvp=False,metric_gate_paid=False)
    def save():
        tmp=report.with_suffix(".tmp")
        tmp.write_text(json.dumps(result,indent=2,allow_nan=False)+"\n")
        tmp.replace(report)
    save()
    record=json.loads(a.source_run.read_text())
    raw=a.raw or a.source_run.parent/record["raw_return"]["file"]
    if sha(raw)!=record["raw_return"]["sha256"]:
        raise ValueError("Actual raw hash differs from run.json")
    source=Path(__file__).with_name("actual_m3_metric_model.py")
    spec=importlib.util.spec_from_file_location("_rms_model",source)
    model=importlib.util.module_from_spec(spec);spec.loader.exec_module(model)
    obj=model.load_model({"source_run":str(a.source_run)})
    r=np.load(raw)
    x,y,p=r["x"].copy(),r["y"].copy(),r["p"].copy()
    if (y.shape!=(obj.n,len(x)) or p.shape!=(obj.M,)
            or not np.array_equal(r["pscale"],obj.pscale)):
        raise ValueError("Raw state or actual parameter scales differ")
    pp=PPoly.construct_fast(r["cubic_c"],r["cubic_x"],axis=1,extrapolate=False)
    if not np.array_equal(x,r["cubic_x"]):
        raise ValueError("Returned mesh and saved cubic knots differ")
    obj.initial(p)
    h=np.diff(x)
    if np.min(h)<=0:
        raise ValueError("Non-increasing raw mesh")
    stored=np.asarray(r["rms"],float)
    if stored.shape!=h.shape:
        raise ValueError("RMS interval layout differs")
    tol=float(record["gates"]["tol"])
    eps=np.finfo(float).eps
    result.update(status="diagnosing_original_cubic",source_run_sha256=sha(a.source_run),
                  raw_source_sha256=sha(raw),
                  diagnostics=dict(nodes=len(x),max_stored_rms=float(stored.max()),
                      tol=tol,over_tol_intervals=int(np.sum(stored>tol)),
                      mesh_h_min=float(h.min()),mesh_h_median=float(np.median(h)),
                      mesh_h_max=float(h.max()),parameters=p.tolist(),
                      physical_controls=(p[1:]*obj.pscale).tolist()))
    save()
    # Reproduce the actual SciPy residual definition without modifying it.
    col,ymid,f,fmid=_bvp.collocation_fun(obj.fun,y,p,x,h)
    rms_col=_bvp.estimate_rms_residuals(
        obj.fun,pp,x,h,p,1.5*col/h[None,:],fmid)
    middle=x[:-1]+h/2
    direct_fmid=obj.fun(middle,pp(middle),p)
    direct_mid=pp(middle,1)-direct_fmid
    rms_direct=_bvp.estimate_rms_residuals(
        obj.fun,pp,x,h,p,direct_mid,direct_fmid)
    rounding_rate=eps*(abs(y[:,:-1])+abs(y[:,1:]))/h[None,:]/(1+abs(fmid))
    rounding_l2=np.linalg.norm(rounding_rate,axis=0)
    worst=np.argsort(stored)[-16:][::-1]
    flow=obj.flow(p[0])
    physical_mid,_=obj.chart(middle,p[0])
    aa,av,acc=flow.profile(physical_mid[worst])
    entries=[]
    for k,j in enumerate(worst):
        entries.append(dict(interval=int(j),t_left=float(x[j]),t_right=float(x[j+1]),
            h=float(h[j]),s_mid=float(physical_mid[j]),
            stored_rms=float(stored[j]),recomputed_collocation_rms=float(rms_col[j]),
            saved_cubic_direct_rms=float(rms_direct[j]),
            raw_midpoint_value_gap=float(abs(pp(middle[j])-ymid[:,j]).max()),
            heuristic_rounding_rate_l2=float(rounding_l2[j]),
            normalized_collocation_defect=float(np.linalg.norm(
                (1.5*col[:,j]/h[j])/(1+abs(fmid[:,j])))),
            profile_a=float(aa[k]),profile_a_prime=float(av[k]),
            profile_a_second=float(acc[k])))
    point_error=float(abs(pp(x)-y).max())
    top=worst[0]
    result["diagnostics"].update(
        recomputed_collocation_rms_max=float(rms_col.max()),
        saved_cubic_direct_rms_max=float(rms_direct.max()),
        stored_recomputed_rms_max_difference=float(abs(stored-rms_col).max()),
        cubic_node_reconstruction_error=point_error,worst_intervals=entries,
        heuristic_rounding_scope="eps*(|Y_left|+|Y_right|)/h normalized by 1+|F_mid| is a scale estimate, not an error bound or a proven cause",
        worst_h_over_median=float(h[top]/np.median(h)),
        rounding_floor_plausible=bool(
            h[top]<1e-3*np.median(h) and rounding_l2[top]>.1*stored[top]))
    result["status"]="original_rms_diagnosed"
    save()
    # Reuse the original mesh constructor, with no cold field seed.
    from fixed_metric_mode3_bvp import merge_profile_mesh
    xn=merge_profile_mesh(np.linspace(0,1,a.nodes),obj.chart_breaks)
    yn=pp(xn)
    hn=np.diff(xn)
    if not np.isfinite(yn).all():
        raise FloatingPointError("Original cubic cannot be evaluated on target mesh")
    new_col,new_mid,new_f,new_fmid=_bvp.collocation_fun(obj.fun,yn,p,xn,hn)
    candidate=_bvp.create_spline(yn,new_f,xn,hn)
    candidate_rms=_bvp.estimate_rms_residuals(
        obj.fun,candidate,xn,hn,p,1.5*new_col/hn[None,:],new_fmid)
    test=np.unique(np.r_[xn,xn[:-1]+hn/2,
                         xn[:-1]+hn*(.5-.5*np.sqrt(3/7)),
                         xn[:-1]+hn*(.5+.5*np.sqrt(3/7))])
    # This compares the prospective original solver cubic with the full
    # retained source cubic; nodal identity alone is not called C2 identity.
    mismatch=float(abs(candidate(test)-pp(test)).max())
    derivative_mismatch=float(abs(candidate(test,1)-pp(test,1)).max())
    first_inlet=float(abs(yn[:,0]-obj.initial(p)).max())
    physical_s,_=obj.chart(xn,p[0])
    full_domain_min=1.
    for k in range(0,len(xn),32):
        sl=slice(k,k+32)
        full_domain_min=min(full_domain_min,float(flow.frame(
            physical_s[sl],obj.q*yn[:,sl])["margin"].min()))
    dest=a.outdir/"initial.npz"
    np.savez_compressed(dest,x=xn,y=yn,p=p,pscale=obj.pscale)
    result["diagnostics"].update(
        remesh_nodes=len(xn),remesh_h_min=float(hn.min()),
        remesh_h_median=float(np.median(hn)),
        prospective_solver_cubic_rms_max=float(candidate_rms.max()),
        prospective_cubic_value_difference=mismatch,
        prospective_cubic_t_derivative_difference=derivative_mismatch,
        remesh_inlet_coefficient_residual=first_inlet,
        remesh_original_frame_margin_min=full_domain_min,
        exact_parameters_retained=bool(np.array_equal(p,r["p"])),
        nodal_seed_scope="Every state component is sampled from the original whole cubic. The next solver cubic may differ between these nodes and must pass all original gates.")
    result.update(status="diagnosed_and_remesh_initial_guess_ready",
        result=dict(initial_raw=str(dest.resolve()),initial_raw_sha256=sha(dest),
                    source_raw=str(raw.resolve()),source_run=str(a.source_run.resolve()),
                    nodes=len(xn),gauge_q=obj.q,warp_reference=record["warp_reference"]))
    save()
    print(json.dumps(result,allow_nan=False))

if __name__=="__main__":
    try:
        main()
    except Exception as exc:
        if "--outdir" in sys.argv:
            directory=Path(sys.argv[sys.argv.index("--outdir")+1])
            directory.mkdir(parents=True,exist_ok=True)
            file=directory/"diagnostic.json"
            report=json.loads(file.read_text()) if file.exists() else {}
            report.update(status="error",error=repr(exc),complete_surface=False)
            file.write_text(json.dumps(report,indent=2)+"\n")
        raise
