#!/usr/bin/env python3
"""Simultaneous finite-phase polar coframe and physical closed shape solve."""
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

import jax
jax.config.update("jax_enable_x64",True)
import jax.numpy as j
from jax.scipy.special import logsumexp
import jaxlib
import bent_coframe_fields as field
import bent_coframe_system as rotation
import bent_shared_rim_phase as run44
import bent_end_phase as base40
import bent_body_atlas as body
import bent_end_phase_fields as fns

digest=base40.digest
save_json=base40.save_json
filehash=base40.filehash

def times(cfg):
    n=cfg["intervals"];nt=np.linspace(0,np.pi/2,n+1)
    ch=np.linspace(0,np.pi/2,2*n+1)
    if cfg["check_extra"]:
        ch=np.unique(np.r_[ch,nt[:-1]+.2113248654*nt[1],nt[:-1]+.7886751346*nt[1]])
    return nt,ch

pair_list=run44.pair_list

def config_key(d,cfg,p,z,nt):
    obj={"domain":"R757 signed-ratio central, full two rolls, two caps and true global position coframe/v1",
         "source_sha256":p["source_sha256"],"design":d,"stage":cfg,
         "coordinates_sha256":digest(z),"phase_nodes_sha256":digest(nt),
         "time_rule":"vector natural cubic spline; zero initial coefficient vector"}
    key=hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return key,obj

def main():
    ap=argparse.ArgumentParser()
    for n in ("params","geometry-source","export-source","out"):ap.add_argument("--"+n,required=True)
    a=ap.parse_args();p=json.loads(Path(a.params).read_text());out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    src=field.physical;gp=Path(a.geometry_source).resolve();export=importlib.import_module(Path(a.export_source).stem)
    orig=src.paired.base;g=src.g
    mods=[src,src.previous,src.tube,src.paired,orig,orig.delay,orig.delay.prior,orig.delay.cap,g,g.original,g.origangle,
          g.oldaxis,g.disk,importlib.import_module("r742_tilted_disk_two_jets"),field,field.legacy,field.prior,body,fns,base40,rotation,run44]
    ids={Path(z.__file__).name:filehash(z.__file__) for z in mods}
    if ids!=p["source_sha256"] or gp!=Path(src.__file__).resolve():raise ValueError("physical source identity mismatch")
    if filehash(export.__file__)!=p["export_sha256"] or filehash(export.geom.__file__)!=p["export_geometry_sha256"]:
        raise ValueError("closed export identity mismatch")
    begin=time.monotonic()
    meta={"schema":"same-closed-metric-rotation-projection/v1","stages":[],"sources":ids,
          "source_sha256":filehash(__file__),"params_sha256":filehash(a.params),
          "runtime":[np.__version__,scipy.__version__,jax.__version__,jaxlib.__version__],
          "fixed_metric":"R757 initial physical pullback on all nine material charts; phase [0,pi/2] throughout",
          "scope":"Every evaluated phase is one global C2 physical position field. Independent polar rotations are auxiliary least-squares targets. Their material exterior derivative is separately measured. R765 constant 2+2 fails the reach curvature threshold; the 2+3 bounded center passes the central curvature and strong held estimates. All optimized full fields still require whole-body verification."}
    def save():meta["elapsed_seconds"]=time.monotonic()-begin;save_json(out/"summary.json",meta)
    def tell(obj):meta["in_progress"]=obj;save()
    def stage(d,c,old=None):
        cfg=dict(p["physics"],**c,paired_space=True);idx=len(meta["stages"]);nt,ck=times(cfg)
        M=field.Model(cfg["mesh"],cfg,0);ref=rotation.Reference(M.mesh.f0)
        Z=np.zeros((len(nt),M.n));history=[]
        if old:
            spl=CubicSpline(old[1],old[2],axis=0,bc_type="natural")
            for i,t in enumerate(nt[1:],1):Z[i]=M.project(old[0],spl(t))
        train=np.linspace(0,np.pi/2,2*cfg["intervals"]+1)
        A=CubicSpline(nt,np.eye(len(nt)),axis=0,bc_type="natural")(train[1:])[:,1:]
        fields=[]
        for k,t in enumerate(train[1:]):
            tell({"stage":idx,"design":d["id"],"material_base_phase":float(t),"index":k,"total":len(A)})
            fields.append(M.base(d,float(t)))
        focus=None
        for block in range(cfg["reweight_blocks"]):
            tell({"stage":idx,"block":block,"action":"assemble_actual_global_shape_operator"})
            op=rotation.System(M,ref,cfg,focus);focus=np.zeros(len(ref.F))
            for step in range(cfg["polar_steps"]):
                az=A@Z[1:];rhs=[];actual=[];before=0.
                for k,f0 in enumerate(fields):
                    F=f0+M.val(az[k]);r,dist,atoms,pr=rotation.targets(F,ref,cfg,op.locked)
                    rhs.append(op.rhs(r));actual.append(pr);focus=np.maximum(focus,dist)
                    before+=(.5 if k==len(A)-1 else 1.)*op.score(atoms)
                dx=op.change(A,np.asarray(rhs))
                if not np.all(np.isfinite(dx)):raise ArithmeticError("nonfinite actual full-shape solve")
                # Recompute rotations, true chords, Hessian targets, and full
                # merit after each trial. Zero is the physical incumbent.
                scales=cfg["step_factors"];win=0.;best=before;trials=[]
                for alpha in scales:
                    cur=A@(Z[1:]+alpha*dx);val=0.
                    for k,f0 in enumerate(fields):
                        F=f0+M.val(cur[k]);_,_,atoms,_=rotation.targets(F,ref,cfg,op.locked)
                        val+=(.5 if k==len(A)-1 else 1.)*op.score(atoms)
                    trials.append([float(alpha),float(val)])
                    if np.isfinite(val) and val<best:best=val;win=alpha
                    # A successful full or half step need not try smaller steps.
                    if win and val<=before*(1-1.e-5):break
                Z[1:]+=win*dx
                rec={"block":block,"iteration":step,"pre_merit":before,"post_merit":best,
                     "accepted_factor":win,"trials":trials,"step_l2":float(np.linalg.norm(dx)),
                     "before_polar_max":max(v["polar_peak"] for v in actual),
                     "before_stretch_min":min(v["minimum_stretch"] for v in actual),
                     "before_pair_inverse_max":max(v["maximum_scanned_inverse"] for v in actual),
                     "before_covariant_peak":max(v["fixed_covariant_bending_peak"] for v in actual),
                     "active_ordered_pair_count":sum(v["sample_ball_halfspaces_active"] for v in actual)}
                history.append(rec);tell({"stage":idx,"design":d["id"],"nonlinear_global_shape_step":rec})
            del op
        names=M.names;del fields,ref,M
        M=field.Model(cfg["check"],cfg,.237);spl=CubicSpline(nt,Z,axis=0,bc_type="natural")
        ref=rotation.Reference(M.mesh.f0);projected=[];rot_seams=np.zeros(2);body_rot_seams=np.zeros((2,2));grip_rot=0.
        col=["phase","Gram_inf","Gram_rms","K_abs","area_ratio_min","support","ordered_inverse","four_seams_max"]
        rows=[];charts={};peaks={};seam=np.zeros((2,2));overlap=np.zeros(2)
        for it,t in enumerate(ck):
            base=M.base(d,float(t));F=base+M.val(spl(t));obs=base40.measured(M.mesh,F,base)
            err,curl,R,valid,svals=rotation.projection_report(F,ref)
            ix=int(err.argmax());ic=int(curl.argmax());bad=int((~valid).sum())
            projected.append({"phase":float(t),"polar_max":float(err[ix]),"polar_at":M.mesh.name(ix),
                "exterior_derivative_per_area_max_on_regular":float(curl[ic]),"curl_at":M.mesh.name(ic),
                "rank_below_1e_12":bad,"sigma_min":float(svals[:,-1].min()),"sigma_max":float(svals[:,0].max())})
            gg=M.mesh.g.grip_arclength(np.array([.10,1.05]));sv=M.mesh.xy
            fixed=(M.mesh.lab=="cylinder")&(sv[:,0]>=gg[0])&(sv[:,0]<=gg[1])&(np.abs(sv[:,1])<=.36)
            if np.any(fixed):grip_rot=max(grip_rot,float(abs(R[fixed]-np.eye(3)).max()))
            by={nm:R[sl].reshape(len(M.mesh.polar),-1,3,3) for nm,uu,vv,sl in M.mesh.cases if "cartesian" not in nm}
            for jx,sfx in enumerate(("+","-")):
                rc=by["cylinder"][:,-1 if jx==0 else 0];re=by["end"+sfx];cp=by["cap"+sfx]
                body_rot_seams[jx]=np.maximum(body_rot_seams[jx],
                    [float(abs(rc-re[:,0]).max()),float(abs(re[:,-1]-cp[:,-1]).max())])
            _,pr=pair_list(F,M.mesh.sign,cfg["pair_count"])
            ss=np.asarray(field.prior.seams(M.mesh,F));seam=np.maximum(seam,ss)
            # The ninth-chart overlap is tested by actual independent material calls.
            lab=M.mesh.polar[::max(1,len(M.mesh.polar)//9)]
            uw=np.tile(lab,2);vw=np.repeat([0.,.000125],len(lab))
            for jx,suffix in enumerate(("+","-")):
                fn=field.evaluate(d,cfg,spl(t),"cap-normal"+suffix,uw,vw,float(t))
                fp=field.evaluate(d,cfg,spl(t),"cap"+suffix,uw,1-vw,float(t))
                fn0=src.delay.chart_jet("cap-normal"+suffix,uw,vw,0.,bend=0.,rotate=False)
                fp0=src.delay.chart_jet("cap"+suffix,uw,1-vw,0.,bend=0.,rotate=False)
                rn=rotation.projection_report(fn,rotation.Reference(fn0))[2]
                rp=rotation.projection_report(fp,rotation.Reference(fp0))[2]
                rot_seams[jx]=max(rot_seams[jx],float(abs(rn-rp).max()))
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
        rec={"stage":idx,"design":d,"configuration":cfg,"closed_point_sha256":ckid,"identity":ident,
             "coordinates_shape":list(Z.shape),"phase_sha256":digest(nt),"point_sha256":digest(Z),
             "input_closed_point_sha256":old[-1]["closed_point_sha256"] if old else None,
             "npz_bytes":fn.stat().st_size,"npz_sha256":filehash(fn),
             "true_joint_training_phases":train.tolist(),"global_shape_history":history,"projected_rotation_checks":projected,
             "right_grip_rotation_max":grip_rot,"rotation_overlap_max":rot_seams.tolist(),"four_rotation_seams_max":body_rot_seams.tolist(),
             "validation_columns":col,"validation":rows,"extrema":peaks,"charts_Gram":charts,"score":score,
             "max_projected_curl_at_regular_samples":max(z["exterior_derivative_per_area_max_on_regular"] for z in projected),
             "max_polar_distance":max(z["polar_max"] for z in projected),
             "seam_two_jet_maxima":seam.tolist(),"normal_to_cap_overlap_sixjet_maxima":overlap.tolist(),"per_side_basis_dimensions":list(field.layout(cfg))}
        fr=out/("stage-%02d-return.json"%idx);save_json(fr,rec)
        light={k:rec[k] for k in ("stage","design","score","closed_point_sha256","point_sha256","phase_sha256","max_polar_distance","max_projected_curl_at_regular_samples","right_grip_rotation_max","rotation_overlap_max","four_rotation_seams_max",
                     "npz_sha256","coordinates_shape","extrema","charts_Gram","seam_two_jet_maxima","normal_to_cap_overlap_sixjet_maxima")}
        light.update(return_file=fr.name,return_bytes=fr.stat().st_size,return_sha256=filehash(fr))
        meta["stages"].append(light);meta.pop("in_progress",None);save()
        print(json.dumps({"event":"rotation_shape_stage","stage":idx,"design":d["id"],"score":score,
                          "peak_Gram":peaks["gram"],"closed_point_sha256":ckid}),flush=True)
        return names,nt,Z,rec
    def export_stage(result,folder):
        folder.mkdir(exist_ok=True,parents=True);names,nt,Z,rec=result;d=rec["design"];cfg=rec["configuration"]
        sp=CubicSpline(nt,Z,axis=0,bc_type="natural")
        def f(chart,u,v,t):return field.evaluate(d,cfg,sp(t),chart,u,v,t)
        def f0(chart,u,v):return src.delay.chart_jet(chart,u,v,0.,bend=0.,rotate=False)
        _,xx,active=g.atlas(32);P=2*g.profile_constants(32)[4];m0=g.original.profile_constants(32)[1]
        po=2*g.original.profile_constants(32)[4]
        cuts=np.unique(np.r_[field.physical.cuts(1,"bounded"),field.physical.cuts(-1,"bounded"),field.physical.cuts(1),field.physical.cuts(-1),[0.,.025,1/3-.025,1/3,2/3,2/3+.025,1-.025,1.]])
        b=((np.arange(11)[:,None]+cuts)*(1.3/11)).ravel()
        extra=np.unique(np.r_[xx,g.forward(np.r_[m0+b,po-m0-1.3+b]),g.grip_arclength(np.array([.10,1.05]))])
        vend=src.delay.clock_at(np.array([0.,.00005,.0001,.000175,.0002,.00025,.00035,.0005,.001,g.END_LENGTH-.0005,g.END_LENGTH]))
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
        for group in ("ratio","reference"):
            pool=[u for u in starts if u[-1]["design"]["group"]==group];best=min(pool,key=lambda z:z[-1]["score"])
            for c in p["refinements"]:best=stage(best[-1]["design"],c,best)
            winners[group]=best
        meta["final_closed_export"]=export_stage(winners["ratio"],out);save()
        meta["reference_closed_export"]=export_stage(winners["reference"],out/"reference");save()
        meta["status"]="completed_both_full_coframe_shape_refinements";meta.pop("in_progress",None);save()
    except Exception as exc:
        meta["status"]="runtime_failure";meta["error"]=type(exc).__name__+": "+str(exc)[:1600]
        save();traceback.print_exc();return 1
    return 0

if __name__=="__main__":raise SystemExit(main())
