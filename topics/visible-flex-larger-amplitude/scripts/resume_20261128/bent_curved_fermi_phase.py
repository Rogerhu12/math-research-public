#!/usr/bin/env python3
"""Finite-time physical Fermi/Jacobi shape optimization on one fixed R757 curved-wall, nonflat-cap closed metric."""
import argparse
import hashlib
import importlib
import importlib.util
import json
import os
import sys
import time
import traceback
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"resume_20261126"))
import numpy as np
import scipy
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize
import jax
import jaxlib
import bent_body_atlas as atlas
import bent_end_phase_fields as fns
import bent_end_phase as base40
import bent_curved_hard_end_fields as hf
import bent_curved_fermi_shoot as fs
import bent_curved_fermi_reconstruct as material

def digest(x):return base40.digest(x)
def filehash(path):return base40.filehash(path)
def save_json(path,obj):return base40.save_json(path,obj)
def join(m,b,d,t,z):return m.at(d,t,z[:hf.HARD])+b.val(z)
def times_for(cfg):
    times=np.linspace(0,np.pi/2,2*cfg["intervals"]+1)
    if cfg["extra_check"]:
        knots=np.linspace(0,np.pi/2,cfg["intervals"]+1);h=knots[1]
        times=np.unique(np.r_[times,knots[:-1]+h*.2113248654,knots[:-1]+h*.7886751346])
    return times

class ShapeLoss:
    def __init__(self,m,b,shoot,d,t,cfg,stage,knot,notify):
        self.m,self.b,self.shoot,self.d,self.t,self.cfg=m,b,shoot,d,t,cfg
        self.stage,self.knot,self.notify=stage,knot,notify;self.calls=0
        shoot.bind(d,t)
        self.best=np.inf;self.last_time=0.;self.rejects=0
    def loss_grad(self,z,publish=True):
        m,b,d,t=self.m,self.b,self.d,self.t
        F=join(m,b,d,t,z)
        val,G=self.shoot.value_grad(F);val=float(val);G=np.asarray(G)
        self.calls+=1
        if not np.isfinite(val) or not np.all(np.isfinite(G)):
            self.rejects+=1
            return 1.e8+.1*float(z@z),.2*z
        h=z[:hf.HARD];delta=self.cfg["hard_difference"];grad=np.empty(b.n);grad[hf.HARD:]=b.adj(G)
        for j in range(hf.HARD):
            which="central" if j==0 else (1 if j in (1,2,3) or 7<=j<13 else -1)
            hp=h.copy();hm=h.copy();hp[j]+=delta;hm[j]-=delta
            df=m.part(d,t,hp,which)-m.part(d,t,hm,which)
            grad[j]=np.sum(df*G)/(2*delta)
        reg=self.cfg["regularizer"]
        val+=reg*(z@z)/b.n;grad+=2*reg*z/b.n
        if publish and val<self.best:
            self.best=val
            if time.monotonic()-self.last_time>35:
                self.last_time=time.monotonic()
                self.notify({"stage":self.stage,"knot":self.knot,"phase":float(t),"design":d["id"],
                       "call":self.calls,"physical_fermi_loss":val,"point_sha256":digest(z)},z,t)
        return val,grad

def solve(loss,z0,b,cfg,probe):
    # Include physical second derivatives in the preconditioner of every roll mode.
    norm=b.norm()
    scale=np.r_[np.full(hf.HARD,.5),np.tile(np.repeat(np.clip(.22/np.maximum(norm,.035),.002,1.5),3),2)]
    def fun(y):
        f,g=loss.loss_grad(z0+scale*y);return f,g*scale
    y=np.zeros_like(z0);val,g=fun(y);fd=None
    if probe:
        dr=np.cos(np.arange(len(y))*.917+.31);dr/=np.linalg.norm(dr);eps=4.e-6
        vp=loss.loss_grad(z0+eps*scale*dr,False)[0];vm=loss.loss_grad(z0-eps*scale*dr,False)[0]
        slope=(vp-vm)/(2*eps);expected=float(g@dr)
        fd={"actual":float(slope),"predicted":expected,
            "relative":float(abs(slope-expected)/max(abs(slope),abs(expected),1.e-8))}
    res=minimize(fun,y,jac=True,method="L-BFGS-B",options={"maxiter":cfg["maxiter"],"maxls":24,
          "maxcor":15,"ftol":2.e-12,"gtol":2.e-8})
    z=z0+scale*res.x
    return z,{"knot":loss.knot,"phase":float(loss.t),"point_sha256":digest(z),"start_loss":val,
              "loss":float(res.fun),"iterations":int(res.nit),"evaluations":int(res.nfev),
              "exit":int(res.status),"gradient_inf":float(np.max(abs(res.jac))),
              "nonfinite_proposals":loss.rejects,"directional_difference":fd}

def main():
    ap=argparse.ArgumentParser()
    for k in ("params","geometry-source","export-source","out"):ap.add_argument("--"+k,required=True)
    a=ap.parse_args();p=json.loads(Path(a.params).read_text());out=Path(a.out);out.mkdir(exist_ok=True,parents=True)
    gp=Path(a.geometry_source).resolve();sys.path.insert(0,str(gp.parent));src=importlib.import_module(gp.stem)
    ep=Path(a.export_source).resolve();spec=importlib.util.spec_from_file_location("fermi_final_export",ep)
    ex=importlib.util.module_from_spec(spec);sys.modules[spec.name]=ex;spec.loader.exec_module(ex)
    mods=[src,src.delay,src.delay.prior,src.delay.cap,src.ar.old,src.ar.old.original,src.ar.old.oldaxis,src.ar.old.origangle,src.ar.old.disk,hf.track,
        importlib.import_module("r742_tilted_disk_two_jets"),fns,base40,hf,fs,material,atlas]
    ids={Path(m.__file__).name:filehash(m.__file__) for m in mods}
    if ids!=p["source_sha256"]:raise ValueError("runnable source identity mismatch")
    if filehash(ep)!=p["export_sha256"]:raise ValueError("closed export source identity mismatch")
    eh=filehash(ep.with_name("closed_body_mesh_geometry.py"))
    if eh!=p["export_geometry_sha256"]:raise ValueError("mesh geometry source identity mismatch")
    begin=time.monotonic()
    meta={"schema":"finite-shape-fermi-jacobi/v1","source_sha256":filehash(__file__),"params_sha256":filehash(a.params),
          "sources":ids,"export_sha256":filehash(ep),"export_geometry_sha256":eh,"numpy":np.__version__,"scipy":scipy.__version__,
          "jax":jax.__version__,"jaxlib":jaxlib.__version__,"stages":[],
          "fixed_metric":"R757 independent curved-section + nonflat two-cap continuum initial pullback on the complete nine-chart atlas, all phases [0,pi/2].",
          "scope":"Finite samples of physical curvature, landing, Jacobi length and actual reconstructed full Gram. Accepted interval rays, diffeomorphism, nonfocal coverage, global tube and exact isometry require separate bounds."}
    def save():meta["elapsed_seconds"]=time.monotonic()-begin;save_json(out/"summary.json",meta)
    def notify(rec,z=None,t=None):
        meta["in_progress"]=rec
        if z is not None:
            with open(out/"current.tmp","wb") as st:np.savez(st,point=z,phase=t)
            os.replace(out/"current.tmp",out/"current.npz")
        save()
    def run(d,cfg,prior=None):
        idx=len(meta["stages"]);cfg=dict(p["physics"],**cfg,paired_space=hf.paired(d));m=hf.Mesh(src,cfg["mesh"],0);b=hf.Basis(m,cfg)
        shoot=fs.Shoot(m,cfg,False);nt=np.linspace(0,np.pi/2,cfg["intervals"]+1)
        ZZ=[np.zeros(b.n)];logs=[]
        pred=None if prior is None else CubicSpline(prior[1],prior[2],axis=0,bc_type="natural")
        for k,t in enumerate(nt[1:],1):
            z=b.project(prior[0],pred(t)) if pred is not None else ZZ[-1].copy()
            if pred is None and k>1:z[hf.HARD:]*=np.sin(t)/np.sin(nt[k-1])
            act=ShapeLoss(m,b,shoot,d,t,cfg,idx,k,notify);z,log=solve(act,z,b,cfg,k==1)
            ZZ.append(z);logs.append(log);notify({"stage":idx,"complete_knots":k,"last":log})
            print(json.dumps({"event":"fermi_physical_knot","stage":idx,**log}),flush=True)
        ZZ=np.array(ZZ);names=b.names;ship=(names,nt,ZZ);del shoot,b,m
        ck=hf.Mesh(src,cfg["check"],.237);cb=hf.Basis(ck,cfg);check=fs.Shoot(ck,cfg,True)
        maps=[];fitread=[];knots_worst=[]
        calibration=[check.baseline_test(d,phi) for phi in (0.,np.pi/2)]
        for k,t in enumerate(nt):
            check.bind(d,t);F=join(ck,cb,d,t,ZZ[k]);r,tr=check.read(F,True)
            qq,rep=material.fit(check,tr,cfg)
            if k==0:qq[:]=0.
            maps.append(qq);fitread.append(rep)
            knots_worst.append([r["max_relative_J"]["value"],r["max_abs_T_minus_L"],r["max_rim_arclength_mismatch"]])
        maps=np.array(maps)
        spl=CubicSpline(nt,ZZ,axis=0,bc_type="natural");ssp=CubicSpline(nt,maps,axis=0,bc_type="natural")
        fname=out/("stage-%02d.npz"%idx);np.savez(fname,phases=nt,physical=ZZ,coordinate_maps=maps)
        cols=["phase","J_rel","T_abs","rim_arclength","minimum_J","guard_max","angular_increment_min",
              "actual_Gram","actual_K","actual_support","map_det_min"]
        rows=[];peak={};worstchart={};seam=np.zeros((2,2))
        for t in times_for(cfg):
            check.bind(d,t);z=spl(t);F=join(ck,cb,d,t,z);r=check.read(F)
            actual,det=material.whole(ck,d,cfg,z,ssp(t),float(t))
            wm=base40.measured(ck,actual,ck.at(d,t))
            seam=np.maximum(seam,hf.seams(ck,actual))
            for key,x in wm["charts_gram_K_support_arg_uv"].items():
                if key not in worstchart or x[0]>worstchart[key][0]:worstchart[key]=[x[0],float(t),x[3],x[4]]
            row=[float(t),r["max_relative_J"]["value"],r["max_abs_T_minus_L"],r["max_rim_arclength_mismatch"],
               r["minimum_J"]["value"],r["guard_ratio_max"],r["minimum_angular_increment_ratio"]["value"],
               wm["gram"]["value"],wm["K"]["value"],wm["support"]["value"],float(det.min())]
            rows.append(row)
            if not peak or row[7]>peak["actual"]["value"]:
                peak={"phase":float(t),"actual":wm["gram"],"shooting":r,"max_K":wm["K"],
                      "min_support":wm["support"],"min_map_det":float(det.min())}
        R=np.array(rows);score=float(R[:,7].max()+.55*max(0.,R[:,8].max()/9.5-1)+
           2*max(0.,.105-R[:,9].min())+2*max(0.,-R[:,10].min())+2*max(0.,R[:,5].max()-1))
        rec={"stage":idx,"design":d,"configuration":cfg,"physical_shape":list(ZZ.shape),"map_shape":list(maps.shape),
          "point_sha256":digest(ZZ),"map_sha256":digest(maps),"phase_sha256":digest(nt),
          "previous_point_sha256":digest(prior[2]) if prior else None,"npz_sha256":filehash(fname),"npz_bytes":fname.stat().st_size,
          "analytic_unbent_calibration":calibration,"knots":logs,"map_fit_at_knots":fitread,"shooting_at_knots_J_T_rim":knots_worst,
          "check_columns":cols,"all_checked_times":rows,"worst_actual_Gram":peak,"worst_Gram_by_chart":worstchart,
          "all_checked_seam_twojet_jumps":seam.tolist(),"score":score}
        identity={"domain":"R757 curved-profile nonflat-cap closed physical+material field v1",
                  "fixed_geometry_sha256":ids["r757_delayed_metric.py"],
                  "profile_sha256":ids["r757_curved_profile_two_jets.py"],
                  "paired_source_sha256":ids["r759_paired_curvature_tracks.py"],
                  "physical_source_sha256":ids["r757_curved_rectifying_closed_two_jets.py"],
                  "material_reconstruction_sha256":ids["bent_curved_fermi_reconstruct.py"],
                  "canonical_physical_basis_sha256":ids["bent_curved_hard_end_fields.py"],
                  "design":d,"configuration":cfg,"physical_sha256":rec["point_sha256"],
                  "map_sha256":rec["map_sha256"],"phase_sha256":rec["phase_sha256"]}
        rec["closed_point_identity"]=identity
        rec["closed_point_sha256"]=hashlib.sha256(json.dumps(identity,sort_keys=True,separators=(",",":"),
                 ensure_ascii=True,allow_nan=False).encode("ascii")).hexdigest()
        stagefile=out/("stage-%02d-return.json"%idx);save_json(stagefile,rec)
        light={key:rec[key] for key in ("stage","design","physical_shape","map_shape","point_sha256","map_sha256",
            "phase_sha256","closed_point_sha256","npz_sha256","npz_bytes","score","worst_actual_Gram","worst_Gram_by_chart",
            "analytic_unbent_calibration","all_checked_seam_twojet_jumps")}
        light.update(return_file=stagefile.name,return_bytes=stagefile.stat().st_size,return_sha256=filehash(stagefile))
        meta["stages"].append(light);meta.pop("in_progress",None);save()
        print(json.dumps({"event":"complete_stage","stage":idx,"score":score,"actual_Gram":float(R[:,7].max()),
               "point":rec["point_sha256"],"map":rec["map_sha256"]}),flush=True)
        return (*ship,maps,rec)
    def export_level(result,export_dir):
        export_dir.mkdir(exist_ok=True,parents=True)
        names,nt,Z,maps,rec=result;d=rec["design"];cfg=rec["configuration"]
        spl=CubicSpline(nt,Z,axis=0,bc_type="natural");msp=CubicSpline(nt,maps,axis=0,bc_type="natural")
        def evaluator(chart,u,v,t):return material.evaluate(src,d,cfg,spl(t),msp(t),chart,u,v,t,True)
        def target(chart,u,v):return src.delay.chart_jet(chart,u,v,0.,bend=0.,rotate=True)
        def step(measurement):
            notify({"phase":"final_closed_mesh","measurement":measurement})
        lh,m0,m1,rtop,half,*_=src.OLD.profile_constants(32)
        h=src.OLD.disk.HOLD;w=src.OLD.disk.BEND;edge=src.OLD.disk.EDGE
        upper=[0.,lh,lh+.001,m0-.001,m0,m1,m1+.001,rtop-.001,rtop,half,
               *[m0+1+x for x in (h,h+w*edge,h+w*(1-edge),h+w)],
               *src.AX.grip_arclength(np.array([.10,1.05]),32)]
        for xmark in (src.LEFT,src.RIGHT):
            lo,hi=lh,m0
            for _ in range(51):
                mid=.5*(lo+hi)
                if src.OLD.profile_coordinates(np.array([mid]))[0][0,0]<xmark:lo=mid
                else:hi=mid
            upper.append(.5*(lo+hi))
        # Include all new bowed cell joins and their true arclength interior extrema.
        # Transition points inherited from the old sections need true arclength conversion.
        o,x,live=src.OLD.atlas(32);oldg=src.OLD.original
        ll,mo,mn,rt,hh,*_=oldg.profile_constants(32)
        old_extra=np.array([ll,ll+.001,mo-.001,mo,mn,mn+.001,rt-.001,rt,
                           *[mo+1+xv for xv in (h,h+w*edge,h+w*(1-edge),h+w)]])
        extra=np.unique(np.r_[upper,2*half-np.asarray(upper),x,src.OLD.forward(np.r_[old_extra,2*hh-old_extra]),
                       src.OLD.forward((o[:-1][live,None]+np.diff(o)[live,None]*np.array([.25,.5,.75])).ravel())])
        breaks=[0.,.00005,.0001,.0002,.00035,.0005,.001,src.OLD.END_LENGTH-.0005,src.OLD.END_LENGTH]
        for bound in (.60*src.delay.SMALL_ANGLE,src.delay.SMALL_ANGLE):
            lo,hi=0.,.002
            for _ in range(50):
                mid=.5*(lo+hi);alpha=src.OLD.disk.softened_angle(np.array([mid]),src.OLD.END_LENGTH,src.OLD.END_BLEND,1/src.OLD.END_TURN)[0]
                if alpha<bound:lo=mid
                else:hi=mid
            breaks.append(.5*(lo+hi))
        vend=src.delay.clock_at(np.unique(breaks))
        index=ex.export_final(export_dir,rec["closed_point_sha256"],list(times_for(cfg)),2*src.OLD.profile_constants(32)[4],
                  src.delay.HALF_WIDTH,src.delay.END_LENGTH,evaluator,target_evaluator=target,
                  mesh_times=p["mesh_times"],profile_extra=extra,end_extra=vend,central_extra=[-.36,.36,0.],cap_center=(src.OLD.CENTER_X,0.),progress=step)
        ip=export_dir/"closed-geometry-index.json";save_json(ip,index)
        ret={k:index.get(k) for k in ("point_sha256","topology","grid","phase_count",
            "completed_phases","finite_extrema","errors","meshes","complete_requested_meshes","all_phase_measurements_returned")}
        ret.update(index_file=str(ip.relative_to(out)),index_bytes=ip.stat().st_size,index_sha256=filehash(ip))
        return ret
    save()
    try:
        starts=[run(d,p["coarse"]) for d in p["designs"]]
        finalists={}
        for key,mask in (("paired",True),("shift",False)):
            pool=[v for v in starts if hf.paired(v[-1]["design"])==mask]
            best=min(pool,key=lambda x:x[-1]["score"]);design=best[-1]["design"]
            meta.setdefault("selected_designs",{})[key]=design
            last=best
            for cfg in p["refinements"]:
                last=run(design,cfg,last)
            finalists[key]=last
        meta["final_closed_export"]=export_level(finalists["paired"],out)
        save()
        meta["shift_closed_export"]=export_level(finalists["shift"],out/"original-shift")
        save()
        meta["status"]="completed_full_closed_fermi_refinements"
        meta.pop("in_progress",None);save()
    except Exception as exc:
        meta["status"]="runtime_failure";meta["error"]=type(exc).__name__+": "+str(exc)[:1400]
        save();traceback.print_exc();return 1
    return 0
if __name__=="__main__":
    raise SystemExit(main())
