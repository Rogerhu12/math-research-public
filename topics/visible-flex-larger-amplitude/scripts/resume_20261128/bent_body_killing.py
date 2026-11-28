#!/usr/bin/env python3
"""Whole capped-cylinder isometry search with physical freedom on every head and cap."""
import argparse
import hashlib
import importlib
import json
import os
from pathlib import Path
import sys
import time
import traceback
import numpy as np
import scipy
from scipy.optimize import least_squares
import bent_body_ambient as am
import bent_body_atlas as at

def digest(z):
    return hashlib.sha256(np.ascontiguousarray(z,dtype="<f8").tobytes()).hexdigest()

def filehash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def dump(path,obj):
    tmp=path.with_suffix(".tmp")
    tmp.write_text(json.dumps(obj,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n")
    os.replace(tmp,path)

class Frozen:
    """The selected actual material tensor, defined at every original chart point."""
    def __init__(self,b,z):
        self.degree=b.degree;self.z=z.copy();self.sha=digest(z)
    def values(self,m,p):
        f=m.f+am.Basis(m,self.degree,True,p["scale"]).values(self.z)
        u,v=f[:,1],f[:,2]
        return at.dot(u,u),at.dot(u,v),at.dot(v,v)

def row(m,r):
    # The global maximum operator residual and its actual chart location.
    K=am.opnorm(r["K"]);curv=r["bend"]
    d={"max_Killing":am.extrem(m,K),"rms_Killing":float(np.sqrt(np.average(K*K,weights=m.weight**2))),
       "max_abs_principal":am.extrem(m,curv),"min_support":am.extrem(m,r["support"],False),
       "min_area_any_regular_chart":am.extrem(m,r["area"],False)}
    cap_groups=[("cylinder",m.lab=="cylinder"),("rolled_heads",np.char.startswith(m.lab,"end")),
                ("flat_caps",np.char.startswith(m.lab,"cap"))]
    parts={}
    for tag,mask in cap_groups:
        ix=np.nonzero(mask)[0];i=ix[K[mask].argmax()]
        parts[tag]={"max_Killing":float(K[i]),"Killing_arg":m.point(i),"max_abs_principal":float(curv[mask].max())}
    d["parts"]=parts
    if "relative" in r:
        delta=am.opnorm(r["relative"])
        d.update(max_fixed_gram=am.extrem(m,delta),rms_fixed_gram=float(np.sqrt(np.average(delta**2,weights=m.weight**2))))
    return d

def measures(m,p,phys,z,vec,x,target=None):
    f=m.f+phys.values(z);ext=vec.values(x)
    ref=target.values(m,p) if target else None
    r=am.calc(f,ext,m.X0,m.sign,p,ref)
    result=row(m,r)
    velocity=am.material_velocity(f,ext,m.X0)
    result["max_material_chart_speed"]=am.extrem(m,np.linalg.norm(velocity,axis=1))
    delta=np.linalg.norm(f[:,0]-m.f[:,0],axis=1)
    result["max_displacement_from_thick_source"]=am.extrem(m,delta)
    if target:
        # This is the mesh evaluation of the continuum estimate from R741.
        # It is not an interval certificate or a trajectory integration.
        err=result["max_fixed_gram"]["value"];eps=result["max_Killing"]["value"]
        result["sampled_phase_estimate"]=[]
        for t in p["phases"]:
            lng=float(np.log1p(err)+t*eps)
            result["sampled_phase_estimate"].append({"t":t,"log_one_plus_error_bound":lng,
                   "error_bound":float(np.expm1(lng)) if lng<680 else None})
    return result

def selection(r,p):
    a=r["max_Killing"]["value"];rr=r["rms_Killing"]
    k=r["max_abs_principal"]["value"];s=r["min_support"]["value"]
    d=r["max_displacement_from_thick_source"]["value"]
    return float(np.log1p(a)+np.log1p(rr)+2.0*np.log1p(max(0.,k/p["bend_cap"]-1))+
                 12*max(0.,p["support_goal"]-s)+15*max(0.,d-p["displace_cap"]))

def moments(m,f,p):
    # Ordered chart grids with full 2pi profile and both heads. A Cartesian
    # center chart represents a single point, of zero integral weight.
    P=m.frame
    g=m.g;_,_,_,_,half,*_=g.profile_constants(32);period=2*half
    vol=0.;first=np.zeros(3);sq=0.
    pts=f[:,0]@P.T+m.center
    normals=np.cross(f[:,1],f[:,2])@P.T*m.sign[:,None]
    h=at.dot(pts,normals)
    vals=np.column_stack([h/3,pts*h[:,None]/4,at.dot(pts,pts)*h/5])
    for typ in ("cylinder","end+","end-","cap+","cap-"):
        use=m.lab==typ;uu=np.unique(m.a[use]);vv=np.unique(m.b[use])
        val=vals[use].reshape(len(uu),len(vv),5)
        # Integrate s periodically; center of the star cap is supplied with
        # area density exactly zero for this polar parametrization.
        val=np.concatenate([val,val[:1]],axis=0);us=np.r_[uu,uu[0]+period]
        if typ.startswith("cap"):
            val=np.concatenate([np.zeros_like(val[:,:1]),val],axis=1);vv=np.r_[0.,vv]
        ans=np.trapezoid(np.trapezoid(val,x=vv,axis=1),x=us,axis=0)
        vol+=ans[0];first+=ans[1:4];sq+=ans[4]
    if m.design["geometry"]=="equal":marks=g.MARKS;heights=[g.HEIGHT]*len(marks)
    else:marks=g.disk.MARKERS;heights=[1e-4*r*r for _,_,r in marks]
    masses=np.array([np.pi*h*r*r/4 for (x,y,r),h in zip(marks,heights)])
    bm=masses@np.array([[x,y] for x,y,r in marks])
    total=vol+sum(masses)
    return {"unmarked_signed_volume":float(vol),"unmarked_first_moment":first.tolist(),
           "unmarked_origin_second_moment":float(sq),"marker_first_xy":bm.tolist(),
           "marked_centered_polar_moment_halfturn_difference":float(4*first[:2]@bm/total)}

def pack(m,p,cfg):
    return am.Basis(m,cfg["shape_degree"],True,p["scale"]),am.Basis(m,cfg["field_degree"],False,p["scale"])

def main():
    ap=argparse.ArgumentParser()
    for key in ("params","geometry-source","out"):ap.add_argument("--"+key,required=True)
    arg=ap.parse_args();p=json.loads(Path(arg.params).read_text());out=Path(arg.out);out.mkdir(exist_ok=True,parents=True)
    sp=Path(arg.geometry_source).resolve();sys.path.insert(0,str(sp.parent));src=importlib.import_module(sp.stem)
    mods=[am,at,src,src.parent,src.parent.disk,importlib.import_module("r742_tilted_disk_two_jets")]
    got={Path(m.__file__).name:filehash(m.__file__) for m in mods}
    if got!=p["source_sha256"]:raise ValueError("different numerical or physical source bytes")
    start=time.monotonic()
    meta={"schema":"whole-embedded-body-Killing/v1","source_sha256":filehash(__file__),"params_sha256":filehash(arg.params),
          "imports":got,"numpy":np.__version__,"scipy":scipy.__version__,"stages":[],
          "scope":"Whole physical chart grids in both symmetry halves, full ends and caps; global material field, target, support and curvature. All extrema and finite-time bounds evaluated here are sampled, not rigorous. No success claim follows from a small training objective."}
    def save():meta["elapsed_seconds"]=time.monotonic()-start;dump(out/"summary.json",meta)
    def mesh(d,cfg,check=False):
        return at.Mesh(p,d,src,cfg["check" if check else "train"],.237 if check else 0.)
    def record(kind,d,cfg,m,b,z,v,x,extra,target=None):
        i=len(meta["stages"]);name=out/("stage-%02d.npz"%i)
        np.savez(name,physical=z,material=x)
        train=measures(m,p,b,z,v,x,target)
        ck=mesh(d,cfg,True);cb,cv=pack(ck,p,cfg)
        check=measures(ck,p,cb,z,cv,x,target);del cb,cv
        rec={"stage":i,"kind":kind,"design":d,"configuration":cfg,"physical_count":len(z),"material_count":len(x),
             "point_sha256":digest(np.r_[z,x]),"physical_sha256":digest(z),"material_sha256":digest(x),
             "npz_bytes":name.stat().st_size,"npz_sha256":filehash(name),"train":train,"check":check,
             "score":selection(check,p),**extra}
        if target:rec["fixed_target_source_physical_sha256"]=target.sha
        meta["stages"].append(rec);meta.pop("in_progress",None);save()
        print(json.dumps({"event":"stage","stage":i,"source":d["id"],"Killing":check["max_Killing"]["value"],
            "K":check["max_abs_principal"]["value"],"base_gram":check.get("max_fixed_gram",{}).get("value"),
            "point_sha256":rec["point_sha256"]}),flush=True)
        return rec
    def alternate(d,cfg,before,target):
        b0,z0,v0,x0=before
        m=mesh(d,cfg);b,v=pack(m,p,cfg)
        z=b.transfer(b0,z0);x=v.transfer(v0,x0)
        ext=v.values(x)
        ref=target.values(m,p) if target else None
        cost=am.Shape(m,b,ext,p,cfg,ref)
        zv=np.cos(.817*np.arange(len(z))+.19);zv/=np.linalg.norm(zv)
        f0=cost.fun(z);jac=cost.jac(z);jz=jac.matvec(zv)
        ww=np.sin(.3157*np.arange(len(f0))+.13);ww/=np.linalg.norm(ww)
        adj=float(abs(ww@jz-zv@jac.rmatvec(ww)));h=p["jacobian_probe"]
        fd=float(np.linalg.norm((cost.fun(z+h*zv)-cost.fun(z-h*zv))/(2*h)-jz)/max(1e-12,np.linalg.norm(jz)))
        state=[np.inf,0.,0]
        def fun(q):
            ff=cost.fun(q);val=float(ff@ff/2);state[2]+=1
            if val<state[0]:
                state[0]=val
                if time.monotonic()-state[1]>20.:
                    state[1]=time.monotonic()
                    meta["in_progress"]={"stage":len(meta["stages"]),"design":d["id"],"call":state[2],"cost":val,
                                          "physical_sha256":digest(q),"material_sha256":digest(x)}
                    with open(out/"current.tmp","wb") as stream:np.savez(stream,physical=q,material=x)
                    os.replace(out/"current.tmp",out/"current.npz");save()
            return ff
        # The actual matrix admits norm scaling without dense SVD. Use the
        # initial safeguarded scale below so every stage is reproducible.
        scale=np.array([1./(1.+sum(k[1:]))**2 for k in b.names])
        sol=least_squares(fun,z,jac=cost.jac,method="trf",tr_solver="lsmr",x_scale=scale,
                    max_nfev=cfg["nfev"],ftol=1e-10,xtol=1e-10,gtol=1e-10,
                    tr_options={"maxiter":cfg["inner"],"atol":2e-7,"btol":2e-7})
        z=sol.x
        # Refitting the field never changes the frozen material tensor.
        x,ls=am.fixed_vector(m,m.f+b.values(z),v,p,cfg["field_iterations"])
        det={"previous_physical_sha256":digest(z0),"previous_material_sha256":digest(x0),"finite_diff_relative":fd,
              "adjoint_abs":adj,"solver_status":int(sol.status),"nfev":int(sol.nfev),"njev":int(sol.njev or 0),
              "solver_cost":float(sol.cost),"optimality":float(sol.optimality),"linear_material":ls}
        rec=record("frozen_metric_actual_shape_and_vector" if target else "free_actual_shape_and_vector",
                   d,cfg,m,b,z,v,x,det,target)
        return b,z,v,x,rec
    save()
    try:
        initial=[]
        for d in p["designs"]:
            cfg=p["initial"];m=mesh(d,cfg);b,v=pack(m,p,cfg);z=np.zeros(b.n)
            before=measures(m,p,b,z,v,np.zeros(v.n))
            x,ls=am.fixed_vector(m,m.f,v,p,cfg["field_iterations"])
            rec=record("unchanged_full_physical_body",d,cfg,m,b,z,v,x,
                       {"linear_material":ls,"unextended_polar_field_Killing_max":before["max_Killing"]["value"]})
            # Only coefficient names and arrays travel to a later stage.
            initial.append((rec["score"],d,SimpleBank(b),z,SimpleBank(v),x,rec))
            del b,v,m
        chosen=[]
        for geom_id in p["continue_geometries"]:
            group=[a for a in initial if a[1]["geometry"]==geom_id]
            _,d,b,z,v,x,r=min(group,key=lambda a:a[0])
            for cfg in p["free_steps"]:
                b,z,v,x,r=alternate(d,cfg,(b,z,v,x),None)
                b,v=SimpleBank(b),SimpleBank(v)
            chosen.append((r["score"],d,b,z,v,x,r))
        _,d,b,z,v,x,r=min(chosen,key=lambda a:a[0])
        target=Frozen(b,z);kept=[(z.copy(),x.copy(),r)]
        meta["frozen_target"]={"definition":"One complete selected unmarked physical pullback tensor in the original fixed material atlas, exact chart/geometry formulas and recorded physical polynomial coefficients. Same top marker graph metric on its fixed domain; no per-radius re-fit, no Haar quadrature or target interpolation.",
               "source_stage":r["stage"],"degree":b.degree,"source_physical_sha256":target.sha,"source_design":d,
               "open_cost":"A full-group invariance of the frozen source is not presumed. Fixed refinement charges both its base tensor mismatch and the actual material Lie derivative of the candidate metric for finite-time control."}
        save()
        for cfg in p["fixed_steps"]:
            b,z,v,x,r=alternate(d,cfg,(b,z,v,x),target)
            kept.append((z.copy(),x.copy(),r));b,v=SimpleBank(b),SimpleBank(v)
        for z,x,r in kept:
            cfg=r["configuration"];m=at.Mesh(p,d,src,p["moment_grid"],0.)
            b=am.Basis(m,cfg["shape_degree"],True,p["scale"])
            r["moments"]=moments(m,m.f+b.values(z),p);del b,m
            m=at.Mesh(p,d,src,p["cloud_grid"],0.);b=am.Basis(m,cfg["shape_degree"],True,p["scale"])
            r["phases"]=m.phase_cloud(m.f+b.values(z),p);del b,m
            save()
        meta["status"]="completed_whole_closed_body_two_material_refinements";save()
    except Exception as err:
        meta["status"]="runtime_failure";meta["exception"]=type(err).__name__+": "+str(err)[:1000];save()
        traceback.print_exc();return 1
    return 0

class SimpleBank:
    def __init__(self,b):
        self.degree=b.degree;self.names=list(b.names)

if __name__=="__main__":
    raise SystemExit(main())
