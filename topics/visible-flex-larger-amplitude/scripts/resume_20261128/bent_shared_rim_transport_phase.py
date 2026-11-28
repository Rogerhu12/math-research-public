#!/usr/bin/env python3
"""Run53 complete Run44 search with the R790 multiphase physical cap transport."""
import argparse
import hashlib
import importlib
import json
import os
import sys
import time
import traceback
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"resume_20261126"))
import numpy as np
import scipy
from scipy.spatial import cKDTree
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize
import jax
jax.config.update("jax_enable_x64",True)
import jax.numpy as j
from jax.scipy.special import logsumexp
import jaxlib
import bent_shared_rim_phase as original44
import bent_shared_rim_transport_fields as field
import bent_end_phase as base40
import bent_body_atlas as body
import bent_end_phase_fields as fns

digest=base40.digest
save_json=base40.save_json
filehash=base40.filehash

times = original44.times
pair_list = original44.pair_list
Objective = original44.Objective

def config_key(d,cfg,p,z,nt):
    obj={"domain":"R757 closed material field with two complete R763 shared rim jets, R790 twelve-component physical transport/v1",
         "source_sha256":p["source_sha256"],"design":d,"stage":cfg,
         "coordinates_sha256":digest(z),"phase_nodes_sha256":digest(nt),
         "time_rule":"vector natural cubic spline; zero initial coefficient vector"}
    key=hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return key,obj

def main():
    ap=argparse.ArgumentParser()
    for n in ("params","geometry-source","export-source","out"):ap.add_argument("--"+n,required=True)
    a=ap.parse_args();p=json.loads(Path(a.params).read_text());out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    parent_path=Path(a.params).with_name(p["original_scientific_parameters"]["name"])
    parent_params=json.loads(parent_path.read_text())
    for key in ("designs","physics","mesh_times","coarse","refinements","runtime","export_sha256","export_geometry_sha256"):
        if p[key]!=parent_params[key]:
            raise ValueError("inconsistent inherited Run44 scientific parameter "+key)
        p[key]=parent_params[key]
    src=field.physical;gp=Path(a.geometry_source).resolve();export=importlib.import_module(Path(a.export_source).stem)
    orig=src.paired.base;g=src.g
    mods=[src,src.tube,src.paired,orig,orig.delay,orig.delay.prior,orig.delay.cap,g,g.original,g.origangle,
          g.oldaxis,g.disk,importlib.import_module("r742_tilted_disk_two_jets"),field,field.prior,body,fns,base40,src.original,src.flow,field.original,original44]
    ids={Path(z.__file__).name:filehash(z.__file__) for z in mods}
    ids[parent_path.name]=filehash(parent_path)
    if ids!=p["source_sha256"] or gp!=Path(src.__file__).resolve():raise ValueError("physical source identity mismatch")
    if filehash(export.__file__)!=p["export_sha256"] or filehash(export.geom.__file__)!=p["export_geometry_sha256"]:
        raise ValueError("closed export identity mismatch")
    begin=time.monotonic()
    meta={"schema":"r790-complete-shared-rim-transport/v1","stages":[],"sources":ids,
          "source_sha256":filehash(__file__),"params_sha256":filehash(a.params),
          "runtime":[np.__version__,scipy.__version__,jax.__version__,jaxlib.__version__],
          "fixed_metric":"R757 initial physical pullback on all nine material charts; phase [0,pi/2] throughout",
          "scope":"All reported optimized extrema are finite samples. R761 verifies the uncorrected named field. Shared rim corrections and the R763 starts require their own reach, immersion, quotient and same-metric verification."}
    def save():meta["elapsed_seconds"]=time.monotonic()-begin;save_json(out/"summary.json",meta)
    def tell(obj):meta["in_progress"]=obj;save()
    def stage(d,c,old=None):
        cfg=dict(p["physics"],**c,paired_space=True);idx=len(meta["stages"]);nt,ck=times(cfg)
        M=field.Model(cfg["mesh"],cfg,0);sc=M.scale();obj=Objective(M,cfg)
        Z=np.zeros((len(nt),M.n));history=[];probes=[]
        if old:
            pred=CubicSpline(old[1],old[2],axis=0,bc_type="natural")
            for i,t in enumerate(nt[1:],1):Z[i]=M.project(old[0],pred(t))
        train=np.linspace(0,np.pi/2,2*cfg["intervals"]+1)
        A=CubicSpline(nt,np.eye(len(nt)),axis=0,bc_type="natural")(train)[:,1:]
        fields=[];pairs=[]
        amplitudes=([item["angle"] for item in p["designs"] if item["cap"]=="tube"]
                    if old is None else [d["angle"]])
        src.set_phase_grid(train,amplitudes,"stage-%02d training %s"%(idx,d["id"]),tell)
        for l,t in enumerate(train):
            tell({"stage":idx,"design":d["id"],"prepare_true_phase":float(t),"index":l,"total":len(train)})
            F=M.base(d,float(t));fields.append(F)
            Q=F+M.val(A[l]@Z[1:])
            pairs.append(pair_list(Q,M.mesh.sign,cfg["pair_count"])[0])
        for outer in range(2):
            start=Z[1:].copy();calls=0;best=float("inf");stamp=0.
            def fun(y,publish=True):
                nonlocal calls,best,stamp
                yy=y.reshape(len(nt)-1,M.n)
                co=start+yy*sc;az=A@co
                grad=np.zeros_like(co);loss=0.
                for k in range(1,len(train)):
                    F=fields[k]+M.val(az[k]);val,gf=obj.eval(F,pairs[k])
                    weight=(.5 if k==len(train)-1 else 1.)/(len(train)-1)
                    loss+=weight*float(val);gg=M.adj(np.asarray(gf));grad+=weight*A[k,:,None]*gg
                reg=cfg["regularizer"]
                loss+=reg*np.mean(co*co);grad+=2*reg*co/co.size;calls+=1
                if not np.isfinite(loss) or not np.all(np.isfinite(grad)):return 1.e10+.1*np.sum(yy*yy),(.2*yy).ravel()
                if publish and loss<best:
                    best=loss
                    if time.monotonic()-stamp>40:
                        stamp=time.monotonic();tell({"stage":idx,"design":d["id"],"block":outer,"call":calls,
                               "true_joint_phase_loss":loss,"phase_count":len(train),"point_sha256":digest(co)})
                return loss,(grad*sc).ravel()
            init=np.zeros_like(start).ravel();basev,slope=fun(init)
            if not outer:
                direction=np.cos(np.arange(len(init))*.479+.19);direction/=np.linalg.norm(direction);eps=5.e-6
                fd=(fun(eps*direction,False)[0]-fun(-eps*direction,False)[0])/(2*eps)
                exact=float(slope@direction)
                probes.append({"actual":float(fd),"predicted":exact,
                               "relative":float(abs(fd-exact)/max(1.e-8,abs(fd),abs(exact)))})
            res=minimize(fun,init,jac=True,method="L-BFGS-B",options={"maxiter":cfg["maxiter_per_block"],
                     "maxcor":13,"maxls":22,"ftol":2.e-12,"gtol":2.e-8})
            Z[1:]=start+sc*res.x.reshape(start.shape);az=A@Z[1:]
            pq=[]
            for l in range(1,len(train)):
                fp=fields[l]+M.val(az[l]);pairs[l],pr=pair_list(fp,M.mesh.sign,cfg["pair_count"]);pq.append(pr["max_inverse"])
            history.append({"block":outer,"loss_at_start":float(basev),"loss":float(res.fun),"exit":int(res.status),
                            "nfev":int(res.nfev),"iterations":int(res.nit),"gradient_inf":float(abs(res.jac).max()),
                            "newly_scanned_max_inverse_by_training_phase":pq})
            tell({"stage":idx,"completed_joint_block":outer,"result":history[-1]})
        names=M.names;del fields,pairs,obj,M
        M=field.Model(cfg["check"],cfg,.237);spl=CubicSpline(nt,Z,axis=0,bc_type="natural")
        col=["phase","Gram_inf","Gram_rms","K_abs","area_ratio_min","support","ordered_inverse","four_seams_max"]
        rows=[];charts={};peaks={};seam=np.zeros((2,2));overlap=np.zeros(2)
        src.set_phase_grid(ck,amplitudes,"stage-%02d validation %s"%(idx,d["id"]),tell)
        for it,t in enumerate(ck):
            base=M.base(d,float(t));F=base+M.val(spl(t));obs=base40.measured(M.mesh,F,base)
            _,pr=pair_list(F,M.mesh.sign,cfg["pair_count"])
            ss=np.asarray(field.prior.seams(M.mesh,F));seam=np.maximum(seam,ss)
            # The ninth-chart overlap is tested by actual independent material calls.
            lab=M.mesh.polar[::max(1,len(M.mesh.polar)//9)]
            uw=np.tile(lab,2);vw=np.repeat([0.,.000125],len(lab))
            for jx,suffix in enumerate(("+","-")):
                fn=field.evaluate(d,cfg,spl(t),"cap-normal"+suffix,uw,vw,float(t))
                fp=field.evaluate(d,cfg,spl(t),"cap"+suffix,uw,1-vw,float(t))
                fp=fp*np.array([1,1,-1,1,-1,1])[None,:,None]
                overlap[jx]=max(overlap[jx],float(abs(fn-fp).max()))
            row=[float(t),obs["gram"]["value"],obs["gram_rms"],obs["K"]["value"],
                 obs["area_min"]["value"],obs["support"]["value"],pr["max_inverse"],float(ss.max())];rows.append(row)
            for nm,val in obs["charts_gram_K_support_arg_uv"].items():
                if nm not in charts or val[0]>charts[nm][0]:charts[nm]=[val[0],float(t),val[3],val[4]]
            for nm,jj,ww in (("gram",1,obs["gram"]),("curvature",3,obs["K"]),("ordered_inverse",6,
                  {**pr,"material_pair":[M.mesh.name(xx) for xx in pr["pair"]]})):
                if nm not in peaks or row[jj]>peaks[nm]["value"]:peaks[nm]={"value":row[jj],"phase":float(t),"at":ww}
            tell({"stage":idx,"checked_phase":float(t),"index":it,"total":len(ck),"actual":row})
        rr=np.asarray(rows);score=float(rr[:,1].max()+.45*max(0.,rr[:,3].max()/9.5-1)+
                                         .65*max(0.,cfg["tube_radius"]*rr[:,6].max()-1))
        ckid,ident=config_key(d,cfg,p,Z,nt)
        fn=out/("stage-%02d.npz"%idx);np.savez(fn,phases=nt,coordinates=Z)
        rec={"transport_to_this_stage":src.counters(),"stage":idx,"design":d,"configuration":cfg,"closed_point_sha256":ckid,"identity":ident,
             "coordinates_shape":list(Z.shape),"phase_sha256":digest(nt),"point_sha256":digest(Z),
             "input_closed_point_sha256":old[-1]["closed_point_sha256"] if old else None,
             "npz_bytes":fn.stat().st_size,"npz_sha256":filehash(fn),
             "true_joint_training_phases":train.tolist(),"directional_check":probes,"joint_history":history,
             "validation_columns":col,"validation":rows,"extrema":peaks,"charts_Gram":charts,"score":score,
             "seam_two_jet_maxima":seam.tolist(),"normal_to_cap_overlap_sixjet_maxima":overlap.tolist(),"per_side_basis_dimensions":list(field.layout(cfg))}
        fr=out/("stage-%02d-return.json"%idx);save_json(fr,rec)
        light={k:rec[k] for k in ("stage","design","score","closed_point_sha256","point_sha256","phase_sha256",
                     "npz_sha256","coordinates_shape","extrema","charts_Gram","seam_two_jet_maxima","normal_to_cap_overlap_sixjet_maxima")}
        light["transport_to_this_stage"]=rec["transport_to_this_stage"]
        light.update(return_file=fr.name,return_bytes=fr.stat().st_size,return_sha256=filehash(fr))
        meta["stages"].append(light);meta.pop("in_progress",None);save()
        print(json.dumps({"event":"shared_rim_stage","stage":idx,"design":d["id"],"score":score,
                          "peak_Gram":peaks["gram"],"closed_point_sha256":ckid}),flush=True)
        return names,nt,Z,rec
    def export_stage(result,folder):
        folder.mkdir(exist_ok=True,parents=True);names,nt,Z,rec=result;d=rec["design"];cfg=rec["configuration"]
        sp=CubicSpline(nt,Z,axis=0,bc_type="natural")
        def f(chart,u,v,t):return field.evaluate(d,cfg,sp(t),chart,u,v,t)
        def f0(chart,u,v):return src.delay.chart_jet(chart,u,v,0.,bend=0.,rotate=False)
        _,xx,active=g.atlas(32);P=2*g.profile_constants(32)[4];m0=g.original.profile_constants(32)[1]
        po=2*g.original.profile_constants(32)[4]
        cuts=np.array([0.,.025,1/3-.025,1/3,2/3,2/3+.025,1-.025,1.])
        b=((np.arange(11)[:,None]+cuts)*(1.3/11)).ravel()
        extra=np.unique(np.r_[xx,g.forward(np.r_[m0+b,po-m0-1.3+b]),g.grip_arclength(np.array([.10,1.05]))])
        vend=src.delay.clock_at(np.array([0.,.00005,.0001,.000175,.0002,.00025,.00035,.0005,.001,g.END_LENGTH-.0005,g.END_LENGTH]))
        terminal_times=np.unique(np.r_[times(cfg)[1],p["mesh_times"]])
        src.set_phase_grid(terminal_times,[d["angle"]],"complete terminal "+d["id"],tell)
        ind=export.export_final(folder,rec["closed_point_sha256"],list(times(cfg)[1]),P,src.delay.HALF_WIDTH,src.delay.END_LENGTH,
             f,target_evaluator=f0,mesh_times=p["mesh_times"],profile_extra=extra,end_extra=vend,
             central_extra=[-.36,.36,0.],cap_center=(g.CENTER_X,0.),progress=lambda z:tell({"terminal":d["id"],"measurement":z}))
        ip=folder/"closed-geometry-index.json";save_json(ip,ind)
        ret={k:ind.get(k) for k in ("point_sha256","topology","grid","phase_count","completed_phases","finite_extrema","errors",
                  "meshes","complete_requested_meshes","all_phase_measurements_returned")}
        ret.update(index_file=str(ip.relative_to(out)),index_bytes=ip.stat().st_size,index_sha256=filehash(ip))
        return ret
    save()
    try:
        starts=[stage(d,p["coarse"]) for d in p["designs"]];winners={}
        for group in ("released","tube"):
            pool=[u for u in starts if u[-1]["design"]["group"]==group];best=min(pool,key=lambda z:z[-1]["score"])
            for c in p["refinements"]:best=stage(best[-1]["design"],c,best)
            winners[group]=best
        meta["final_closed_export"]=export_stage(winners["released"],out);save()
        meta["tube_closed_export"]=export_stage(winners["tube"],out/"tube-reference");save()
        meta["transport_final"]=src.counters();meta["status"]="completed_joint_shared_rim_refinements";meta.pop("in_progress",None);save()
    except Exception as exc:
        meta["transport_at_failure"]=src.counters();meta["status"]="runtime_failure";meta["error"]=type(exc).__name__+": "+str(exc)[:1600]
        save();traceback.print_exc();return 1
    return 0

if __name__=="__main__":raise SystemExit(main())
