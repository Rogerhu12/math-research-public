#!/usr/bin/env python3
"""Raise M without dropping the exact lift's M-dependent inlet projection.

This creates a nodal Newton initial guess, not an accepted BVP or surface.
At fixed q, profile, chart and physical core, the continuous reference transfer
is Y_new(s)=embed(Y_old(s))+a(s)*chi(s)*(I_new-embed(I_old)).
The lift coefficient is one; material-core homotopy lambda is NOT a factor.
"""
import argparse, hashlib, importlib.util, json, sys
from pathlib import Path
import numpy as np
from scipy.interpolate import PPoly

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec)
    sys.modules[name]=out
    spec.loader.exec_module(out)
    return out

def embed(value,old_m,new_m):
    value=np.asarray(value)
    if value.shape[0] != 3*old_m+1:
        raise ValueError("Unexpected physical Fourier layout")
    result=np.zeros((3*new_m+1,)+value.shape[1:],dtype=value.dtype)
    result[0]=value[0]
    for old_start,new_start in ((1,1),(old_m+1,new_m+1),
                                (2*old_m+1,2*new_m+1)):
        result[new_start:new_start+old_m]=value[old_start:old_start+old_m]
    return result

def lift_weights(flow,s):
    s=np.atleast_1d(s)
    aa,av,acc=flow.profile(s)
    span=.4*flow.prefix_end
    x=np.clip((s-.5*flow.prefix_end)/span,0.,1.)
    chi=1-x**3*(10-15*x+6*x*x)
    chip=-30*x*x*(1-x)**2/span
    chipp=-60*x*(1-x)*(1-2*x)/span**2
    return (aa*chi,av*chi+aa*chip,acc*chi+2*av*chip+aa*chipp)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source-run",type=Path,required=True)
    ap.add_argument("--raw",type=Path)
    ap.add_argument("--modes",type=int,required=True)
    ap.add_argument("--angular",type=int)
    ap.add_argument("--check-angular",type=int,default=2048)
    ap.add_argument("--outdir",type=Path,required=True)
    a=ap.parse_args()
    rec=json.loads(a.source_run.read_text())
    command=rec["command"]
    def option(name):
        return command[command.index(name)+1]
    if "--core-module" not in command:
        raise ValueError("This entry requires the original exact-lift provider")
    if not rec.get("solver_success"):
        raise ValueError("Source BVP did not converge; no accepted field was supplied")
    raw=a.raw or a.source_run.parent/rec["raw_return"]["file"]
    if sha(raw)!=rec["raw_return"]["sha256"]:
        raise ValueError("Raw source hash differs from recorded return")
    old_m=int(rec["modes"]); new_m=a.modes
    if new_m<=old_m:
        raise ValueError("This operation only raises M")
    q=float(rec["gauge_q"]); warp=float(rec["warp_reference"])
    source=Path(option("--source-topic")); short=Path(option("--short-bridge"))
    cfg=json.loads(Path(option("--profile")).read_text())
    chart=json.loads(Path(option("--chart")).read_text())
    port_path=Path(option("--port"))
    port=json.loads(port_path.read_text())
    port["cut"]["_prefix_bridge"]=cfg["prefix_bridge"]
    port["_sha256"]=sha(port_path)
    if (cfg!=rec["physical_profile"] or chart!=rec["angular_chart"]
        or port["parameters"]!=rec["physical_tail_parameters"]
        or port["cut"]!=rec["physical_tail_cut"]):
        raise ValueError("Physical profile, chart or tail metric changed")
    if new_m>len(port["linearSlope"]):
        raise ValueError("Regenerate the same original port with enough linear modes")
    core_path=Path(option("--core-module"))
    core_cfg=Path(option("--core-config")) if "--core-config" in command else None
    settings=json.loads(core_cfg.read_text()) if core_cfg else {}
    if settings!=rec["core_settings"]:
        raise ValueError("Core settings changed")
    for file in (core_path, core_cfg):
        if file is not None:
            expected=rec["inputs"].get(str(file.resolve()))
            if expected is None or sha(file)!=expected:
                raise ValueError("Source core provider or settings hash changed")
    scripts=source/"scripts"
    c=module("resize_coupler",scripts/"db6f-prefix-coupled.py")
    module("resize_flat",scripts/"db6f-prefix-flat-profile.py").install(c.adaptive)
    c.adaptive.old.install_source(source/"repro/source-root")
    module("resize_short",short).install()
    module("resize_jac",scripts/"78718-prefix-fourier-jacobian.py").install(c.adaptive)
    factory=module("resize_core",core_path).make_factory(settings)
    __import__("fixed_metric_mode3_core").PlanarSupportCore=factory
    __import__("fixed_metric_mode3_bvp").PlanarSupportCore=factory
    Flow,Base=c.adaptive.build_classes(chart)
    sys.path.insert(0,str(Path(__file__).with_name("round_raw_lib")))
    from exact_core_lift import install_core_lift
    Base=install_core_lift(Flow,Base)
    if hasattr(factory,"jet_parameter_derivatives"):
        import analytic_adaptive_core_jac as analytic
        analytic.parameter_jets=lambda core,theta:core.jet_parameter_derivatives(theta)
        analytic.install(Base)
    old=Base(cfg,port,q,old_m,int(rec["angular"]),False,warp)
    nt=a.angular or max(int(rec["angular"]),32*new_m)
    new=Base(cfg,port,q,new_m,nt,False,warp)
    r=np.load(raw)
    x,y0,p0=r["x"].copy(),r["y"].copy(),r["p"].copy()
    if (y0.shape!=(old.n,len(x)) or p0.shape!=(old_m,)
        or not np.array_equal(r["pscale"],old.pscale)):
        raise ValueError("Raw dimensions or old physical parameter scales differ")
    p1=np.zeros(new_m)
    p1[0]=p0[0]
    p1[1:old_m]=p0[1:]*old.pscale/new.pscale[:old_m-1]
    i0=old.initial(p0).copy()
    i1=new.initial(p1).copy()
    f0,f1=old.flow(p0[0]),new.flow(p1[0])
    s,ds=old.chart(x,p0[0])
    sn,dsn=new.chart(x,p1[0])
    if not np.array_equal(s,sn) or not np.array_equal(ds,dsn):
        raise ValueError("Meridian chart changed")
    di=i1-embed(i0,old_m,new_m)
    h,hp,hpp=lift_weights(f1,s)
    y1=embed(y0,old_m,new_m)+h[None,:]*di[:,None]
    # Finite reconstruction check of the continuous reference, including
    # all computational two-jets when the saved physical C2 source exists.
    physical=a.source_run.parent/"physical.npz"
    pp=None
    if physical.exists():
        if sha(physical)!=rec.get("physical_sha256"):
            raise ValueError("Physical C2 source hash differs")
        rphys=np.load(physical)
        if not np.array_equal(rphys["p"],p0):
            raise ValueError("Raw and physical parameter vectors differ")
        pp=PPoly.construct_fast(rphys["c"],rphys["x"],axis=1,extrapolate=False)
    checks={name:0. for name in
            ("position","psi","psi_psi","s","s_psi","s_s","rho")}
    sample=np.unique(np.r_[np.linspace(0,f0.end,65),
                           f0.prefix_end*np.array([.5,.6,.7,.8,.9]),s[::max(1,len(s)//32)]])
    N=max(a.check_angular,32*(new_m*3+1))
    B0,D0,DD0=f0.basis(N);B1,D1,DD1=f1.basis(N)
    if pp is None:
        # No assertion on meridian two-jets without the saved physical source.
        sample=s
    for start in range(0,len(sample),16):
        z=sample[start:start+16]
        if pp is None:
            v0=y0[:,start:start+len(z)]
        else:
            v0=pp(z)
        w,w1,w2=lift_weights(f1,z)
        v1=embed(v0,old_m,new_m)+w[None,:]*di[:,None]
        g0,g1=f0.geo(z,N),f1.geo(z,N)
        checks["rho"]=max(checks["rho"],float(abs(g0["rho"]-g1["rho"]).max()))
        pairs=[("position","pos",v0,v1,B0,B1),
               ("psi","p1",v0,v1,D0,D1),
               ("psi_psi","p2",v0,v1,DD0,DD1)]
        if pp is not None:
            u0,uu0=pp(z,1),pp(z,2)
            u1=embed(u0,old_m,new_m)+w1[None,:]*di[:,None]
            uu1=embed(uu0,old_m,new_m)+w2[None,:]*di[:,None]
            pairs.extend([("s","s1",u0,u1,B0,B1),
                          ("s_psi","sp",u0,u1,D0,D1),
                          ("s_s","s2",uu0,uu1,B0,B1)])
        for name,geo_key,c0,c1,b0,b1 in pairs:
            delta=g1[geo_key]+q*f1.values(c1,b1)-g0[geo_key]-q*f0.values(c0,b0)
            checks[name]=max(checks[name],float(np.max(np.linalg.norm(delta,axis=2))))
    if max(checks.values())>1e-7:
        raise FloatingPointError("Physical reference transfer failed: "+str(checks))
    a.outdir.mkdir(parents=True,exist_ok=False)
    dest=a.outdir/"initial.npz"
    np.savez_compressed(dest,x=x,y=y1,p=p1,pscale=new.pscale)
    result=dict(scope=__doc__,status="nodal_initial_guess_ready",
        source_run=str(a.source_run.resolve()),source_run_sha256=sha(a.source_run),
        raw_source_sha256=sha(raw),initial_raw=str(dest.resolve()),
        initial_raw_sha256=sha(dest),modes=[old_m,new_m],gauge_q=q,
        warp_reference=warp,delta_increment=float(p0[0]),
        physical_controls_old=(p0[1:]*old.pscale).tolist(),
        physical_controls_new=(p1[1:]*new.pscale).tolist(),
        exact_lift_coefficient=1,core_homotopy=settings.get("homotopy"),
        inlet_projection_change_max=float(abs(di).max()),
        reference_two_jet_checks=checks,check_angular=N,check_s=len(sample),
        meridian_two_jets_checked=pp is not None,
        diagnostics=dict(reference_two_jet_checks=checks,check_angular=N,
                         check_s=len(sample),meridian_two_jets_checked=pp is not None,
                         inlet_projection_change_max=float(abs(di).max()),
                         exact_lift_coefficient=1,core_homotopy=settings.get("homotopy")),
        result=dict(initial_raw=str(dest.resolve()),initial_raw_sha256=sha(dest)),
        common_mean_height_scope="The identical angular frame and s jet preserve its original mean-height reconstruction; the reported raw jets omit that common term.",
        stored_representation="Only nodal Y is stored. The continuous transferred reference has the stated identity; a new BVP interpolant is not claimed identical.",
        accepted_bvp=False,metric_gate_paid=False,true_tail_paid=False,
        complete_surface=False)
    (a.outdir/"transfer.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,allow_nan=False))

if __name__=="__main__":
    main()
