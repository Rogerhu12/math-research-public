"""R786 whole physical surface and simultaneous time/space Gauss-Newton and compressive Gram trials."""
import argparse,hashlib,importlib.util,json,os,sys,time
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"resume_20261126"))
import bent_mild_cap_pullback_fields as fld
import bent_mild_cap_stress_system as sysfit
import r786_delayed_two_cap_roll_collars as ref
import r781_round_three_lobe_spatial_rings as intrinsic
from scipy.spatial import cKDTree

def put(path,obj):
    s=(json.dumps(obj,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode()
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    tmp=p.with_suffix(p.suffix+".tmp");tmp.write_bytes(s);os.replace(tmp,p)
    return {"path":str(p.name),"bytes":len(s),"sha256":hashlib.sha256(s).hexdigest()}

def ah(a):return hashlib.sha256(np.ascontiguousarray(a,dtype="<f8").tobytes()).hexdigest()

def log(d):print(json.dumps(d,sort_keys=True,separators=(",",":"),allow_nan=False),flush=True)

def charts(conf,order,ind,d):
    grid=fld.grid(conf["ns"],conf["nv"],order,ind);ns=fld.names(conf["level"])
    out=[]
    for key,u,v in grid:
        z=fld.target(key,u,v,order)
        anchor=fld.target(key,u,v,20) if order!=20 else z
        B=fld.basis(key,u,v,anchor,ns,d,20)
        zh,Bh,C=sysfit.fixed(z,B);out.append((key,u,v,z,zh,Bh,C))
    return out

def base_fields(table,d,ts,order):
    tables=[];values=[]
    for key,u,v,z,zh,Bh,C in table:
        weight=(1. if key=="cylinder" else .52)/np.sqrt(len(u))
        tables.append((Bh,np.full(len(u),weight),z[:,0]))
    for t in ts:
        part=[]
        for key,u,v,z,zh,Bh,C in table:
            vv=fld.base(key,u,v,float(t),order,d) if t else z
            part.append(sysfit.transformed(vv,C))
        values.append((float(t),part,fld.floor(t,order)))
    return tables,values

def transfer(old,nodes,ns):
    out=np.zeros((len(nodes)-1,len(ns),3))
    if old is None:return out
    prev,oldnodes,keys=old;W=sysfit.clock(oldnodes,nodes[1:]);new=np.einsum("tn,nkd->tkd",W,prev)
    ids={key:i for i,key in enumerate(ns)}
    for k,j in enumerate(keys):out[:,ids[j]]=new[:,k]
    return out

def stage_fit(conf,par,d,old,progress):
    order=conf["order"];table=charts(conf,order,False,d);ns=fld.names(conf["level"])
    T=conf["time_intervals"];nodes=np.linspace(0.,np.pi/2,T+1)
    # Half-knot phases enter the actual normal equations, not just reporting.
    ts=np.unique(np.r_[np.linspace(0.,np.pi/2,2*T+1)[1:],.003,.006,np.pi/4,np.pi/3]);W=sysfit.clock(nodes,ts)
    Z=transfer(old,nodes,ns)
    if old is None:
        for key,dim,value in d["seed"]:
            j=ns.index(tuple(key));Z[:,j,dim]=value*np.sin(nodes[1:])
    tabs,vals=base_fields(table,d,ts,order);hist=[]
    for it in range(conf["iterations"]):
        steps,read=sysfit.shape_step(tabs,vals,W,Z,par)
        original=Z;best=read["current_objective"];newpeak=read["raw_max_gram"]
        chosen="stationary";picked=0.;actual_trials=[]
        # Keep the full original GN backtracking. Test both signs of each physical second-order
        # direction from the same incumbent and retain the lowest true full-domain objective.
        for tag,step in steps:
            factors=([2.**(-j) for j in range(par["line_trials"])] if tag=="gauss-newton"
                     else [sg*f for f in par["stress_line_scales"] for sg in (1.,-1.)])
            for f in factors:
                v,p=sysfit.objective(tabs,vals,W,original+f*step,par)
                actual_trials.append([tag,float(f),float(v),float(p)])
                if v<best:
                    best,picked,newpeak=v,f,p;Z=original+f*step;chosen=tag
                    if tag=="gauss-newton":break
        read.update(accepted_direction=chosen,accepted_line_scale=picked,actual_new_objective=best,
                    actual_new_peak=newpeak,signed_trial_count=len(actual_trials),
                    best_trial_by_direction={label:min([a for a in actual_trials if a[0]==label],key=lambda a:a[2])
                                             for label,_ in steps})
        hist.append(read);progress({"iteration":it,"objective":best,"accepted_direction":chosen,
                                     "accepted_scale":picked,"training_gram":newpeak})
    return Z,nodes,ns,hist

def true_eval(conf,d,Z,nodes,ns,solver):
    other=dict(conf,ns=conf["check_ns"],nv=conf["check_nv"])
    table=charts(other,conf["check_order"],True,d);times=np.unique(np.r_[np.linspace(0.,np.pi/2,conf["check_phases"]),.003,.006,np.pi/4,np.pi/3])
    W=sysfit.clock(nodes,times);by={};peaks={};phase_rows=[];initial=None;held=[];support=[];far=[]
    material=np.concatenate([row[3][:,0] for row in table]);starts=np.cumsum([0]+[len(row[1]) for row in table])
    def material_label(i):
        j=int(np.searchsorted(starts[1:],i,side="right"));row=table[j];k=i-starts[j]
        return {"chart":row[0],"u":float(row[1][k]),"v":float(row[2][k])}
    for i,t in enumerate(times):
        co=np.tensordot(W[i],Z,axes=1);gmx=0.;kmx=0.;amin=float("inf");cloud=[]
        for key,u,v,z,zh,Bh,C in table:
            vv=fld.base(key,u,v,float(t),conf["check_order"],d) if t else z
            F=sysfit.transformed(vv,C)
            F=fld.apply(F,Bh,co,fld.floor(float(t),conf["check_order"]),False)[0]
            op,pk,ar=sysfit.stats(F);cloud.append(F[:,0])
            m0=np.einsum("nid,njd->nij",z[:,1:3],z[:,1:3])
            ab=np.einsum("nij,njd->nid",np.linalg.inv(np.swapaxes(C,1,2)),F[:,1:3])
            gm=np.einsum("nid,njd->nij",ab,ab);err=gm-m0
            den=np.sqrt(np.maximum(m0[:,0,0]*m0[:,1,1],1.e-30))
            for met,arr,sg in (("gram",op,1),("curvature",pk,1),("area",ar,-1),
                   ("covariant_ee",abs(err[:,0,0])/m0[:,0,0],1),
                   ("covariant_mixed",abs(err[:,0,1])/den,1),("covariant_vv",abs(err[:,1,1])/m0[:,1,1],1)):
                j=int(np.argmax(sg*arr));val=float(arr[j]);rec={"value":val,"phase":float(t),
                        "chart":key,"u":float(u[j]),"v":float(v[j])}
                cp=by.setdefault(key,{})
                if met not in cp or val*sg>sg*cp[met]["value"]:cp[met]=rec
                if met not in peaks or val*sg>sg*peaks[met]["value"]:peaks[met]=rec
            gmx=max(gmx,float(op.max()));kmx=max(kmx,float(pk.max()));amin=min(amin,float(ar.min()))
        pts=np.concatenate(cloud);yf=fld.floor(float(t),conf["check_order"]);support.append([float(t),yf,float(pts[:,1].min()),float(pts[:,1].min()-yf)])
        fi,fj,vs,count,radius=sysfit.far_constraints(pts,material,solver)
        detail={"phase":float(t),"all_active_pairs":count,"initial_radius":float(radius),"residual":0.}
        if len(vs):
            k=int(np.argmax(vs));i1,i2=int(fi[k]),int(fj[k])
            detail.update(residual=float(vs[k]),material=[material_label(i1),material_label(i2)],
                 initial_chord=float(np.linalg.norm(material[i1]-material[i2])),actual_chord=float(np.linalg.norm(pts[i1]-pts[i2])))
        far.append(detail)
        phase_rows.append([float(t),gmx,kmx,amin])
        if initial is None:initial=pts;c0=cKDTree(pts)
        if any(abs(float(t)-s)<1.e-13 for s in (0.,np.pi/4,np.pi/2)):
            ct=cKDTree(pts)
            held.append([float(t),float(c0.query(pts)[0].max()),float(ct.query(initial)[0].max())])
    return dict(peaks=peaks,charts=by,phase_gram_curvature_area=phase_rows,finite_two_directed_held=held,
                evaluation_order=conf["check_order"],station_count=other["ns"],bridge_subdivisions=other["nv"],
                fixed_chart_order=20,actual_phase_count=len(times),finite_points_per_phase=sum(len(x[1]) for x in table),phase_axis_floor_minimum_margin=support,phase_metric_reach_chord=far)

def identity(d,ns,Z,nodes,files,par,path):
    docs={"schema":"r786-two-cap-closed-stress-v1","design":d,"column_names":ns,"actual_coefficient_le_f64":ah(Z),
          "actual_coefficient_shape":list(Z.shape),"time_nodes_le_f64":ah(nodes),"fixed_sources":files,
          "fixed_metric":par["fixed_metric"],"world_motion":"R786 cap delay and R785 four MILD bends on both caps. The axial floor is the R781 left extremal plane less .008 sin(t). Hard caps keep the two actual prescribed cap poses and lip, with both central rims released; other branches keep one or two inner pads. The R784 finite spatial Taylor is part of the physical collar.",
          "temporal_basis":"CubicSpline natural left, zero right derivative at pi/2; zero coefficient at t0",
          "continuum_integrals":"R781 exact initial integrals and R786 true reflected roll clock. All spatial columns and their original ring companions use defining order 20; current base and metric use the recorded stage quadrature. Final field uses order 20 throughout. The ninth-degree R784 field is finite, distinct from its local exact Cauchy limit.",
          "physical_order":par["defining_order"]}
    raw=json.dumps(docs,sort_keys=True,separators=(",",":")).encode()
    with path.open("wb") as h:np.savez_compressed(h,coefficients=Z,time_nodes=nodes)
    return hashlib.sha256(raw).hexdigest(),docs,dict(path=path.name,bytes=path.stat().st_size,sha256=hashlib.sha256(path.read_bytes()).hexdigest())

def run():
    p=argparse.ArgumentParser()
    for a in ("params","geometry-source","export-source","out"):p.add_argument("--"+a,required=True)
    a=p.parse_args();out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    par=json.loads(Path(a.params).read_text())
    if Path(a.geometry_source).resolve()!=Path(ref.__file__).resolve():raise ValueError("wrong actual R786 geometry module")
    ep=Path(a.export_source);spec=importlib.util.spec_from_file_location("r772_mesh_terminal",ep)
    ex=importlib.util.module_from_spec(spec);spec.loader.exec_module(ex)
    files={"params":hashlib.sha256(Path(a.params).read_bytes()).hexdigest()}
    for p in [Path(__file__),Path(fld.__file__),Path(sysfit.__file__),Path(ref.__file__),Path(intrinsic.__file__),Path(fld.cauchy.__file__),
              Path(sysfit.old.__file__),Path(fld.previous.__file__),Path(fld.previous.cap.__file__),
              Path(ref.shear.__file__),Path(ref.shear.flaps.__file__),
              Path(sys.modules["r740_rolled_disk_seed"].__file__),Path(sys.modules["r742_tilted_disk_two_jets"].__file__),
              Path(sys.modules["r767_negative_track_profile"].__file__),Path(sys.modules["r767_preloaded_cap_atlas"].__file__),
              Path(sys.modules["bent_spatial_ring_fields"].__file__),Path(sys.modules["bent_coherent_shear_fields"].__file__),
              Path(sys.modules["r775_nonplanar_compensated_section_two_jets"].__file__),
              Path(sys.modules["r772_coherent_developing_tube"].__file__),Path(sysfit.ref.__file__),ep,
              ep.with_name("closed_body_mesh_terminal.py"),ep.with_name("closed_body_mesh_geometry.py")]:
        files[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
    assert par["defining_order"]==par["refine"][-1]["check_order"]
    report={"schema":"r786-two-cap-full-domain-gram-stress-run-v1","sources":files,"fixed_metric":par["fixed_metric"],
            "fixed_initial_D":float(intrinsic.diameter(0.,20)),"fixed_required_radius":float(.03*intrinsic.diameter(0.,20)),
            "stages":[],"closed_exports":{},"field_families":par["families"],"notes":par["limits"]}
    put(out/"summary.json",report);allstates={};idx=0
    def save_stage(d,conf,old,desc):
        nonlocal idx
        n=idx;idx+=1;start=time.monotonic();log({"stage":n,"start":desc,"budget":conf})
        Z,nodes,ns,hist=stage_fit(conf,par["solver"],d,old,lambda rec:log({"stage":n,**rec}))
        baseline=None
        if old is None:
            raw=true_eval(conf,d,np.zeros_like(Z),nodes,ns,par["solver"])
            baseline={k:raw[k] for k in ("peaks","charts","finite_two_directed_held","phase_axis_floor_minimum_margin","phase_metric_reach_chord")}
        val=true_eval(conf,d,Z,nodes,ns,par["solver"]);sha,doc,npz=identity(d,ns,Z,nodes,files,par,out/("stage-%02d-field.npz"%n))
        score=val["peaks"]["gram"]["value"]+.02*max(0.,val["peaks"]["curvature"]["value"]-par["solver"]["curvature_bound"])+.20*max(0.,par["solver"]["area_floor"]-val["peaks"]["area"]["value"])
        st=dict(stage=n,name=desc,design=d,budget=conf,point_sha256=sha,point_identity=doc,field_npz=npz,score=score,
                bare_coarse_candidate=baseline,working_integration_order=conf["order"],training_history=hist,independent=val,
                elapsed_seconds=time.monotonic()-start)
        ret=put(out/("stage-%02d-return.json"%n),st)
        report["stages"].append(dict(stage=n,name=desc,point_sha256=sha,score=score,
               gram=val["peaks"]["gram"],curvature=val["peaks"]["curvature"],area=val["peaks"]["area"],
               complete_stage_file=ret,field_shape=list(Z.shape),field_le_f64_sha256=ah(Z)))
        put(out/"summary.json",report);log({"phase":"stage_complete","stage":n,"point":sha,"score":score,
               "gram":val["peaks"]["gram"],"curvature":val["peaks"]["curvature"]})
        return score,(Z,nodes,ns),sha
    # All three independent design families receive their own complete same-target refinements and final geometry.
    for family,starts in par["families"].items():
        best=None
        for label,d in starts:
            score,state,sha=save_stage(d,par["coarse"],None,family+"-"+label)
            if best is None or score<best[0]:best=(score,state,sha,label,d)
        allstates[family]=best
    for j,conf in enumerate(par["refine"]):
        for family,old in list(allstates.items()):
            _,state,_,label,d=old
            score,new,sha=save_stage(d,conf,state,family+"-"+label+"-refinement-"+str(j+1))
            allstates[family]=(score,new,sha,label,d)
    for family,(_,state,sha,label,d) in allstates.items():
        Z,nodes,ns=state;O=par["defining_order"]
        def f(chart,u,v,t):
            coeff=np.tensordot(sysfit.clock(nodes,[t])[0],Z,axes=1)
            return fld.image(chart,np.asarray(u),np.asarray(v),t,d,O,ns,coeff)
        def target(chart,u,v):return fld.target(chart,np.asarray(u),np.asarray(v),O)
        dest=out if family=="hard_heads" else out/("inner-grip" if family=="inner_grip" else "spatial-rings");dest.mkdir(exist_ok=True)
        result=ex.export_final(dest,sha,np.unique(np.r_[np.linspace(0.,np.pi/2,65),.003,.006,np.pi/3]),ref.P,ref.HALF_WIDTH,ref.L,f,
                 target_evaluator=target,mesh_times=np.linspace(0.,np.pi/2,7),cap_atlas=ref,material_order=O,
                 profile_extra=np.unique(np.r_[ref.profile_marks(),ref.P*np.arange(48)/48,ref.angular_breaks(O),[ref.R*((j*np.pi/2+sg*x)%(2*np.pi)) for j in range(4) for sg in (-1.,1.) for x in (.46,.48,.57,.67,.69)]]),end_extra=np.unique(np.r_[0.,ref.SM/2,ref.SM,ref.L-ref.SM,ref.L-ref.SM/2,ref.L,ref.terminal_stations(np.pi/2),ref.L-fld.cauchy.HALF_BAND,ref.L-1.5*fld.cauchy.HALF_BAND]),central_extra=np.unique(np.r_[ref.axial_marks(),(np.arange(12)+.5)/12-.5]),
                 progress=lambda rec:log({"phase":"closed_mesh","family":family,"measurement":rec}))
        doc=put(dest/"closed-geometry-index.json",result)
        report["closed_exports"][family]={"point_sha256":sha,"directory":str(dest.relative_to(out)),
               "index":doc,"finite_extrema":result["finite_extrema"],"complete_requested_meshes":result["complete_requested_meshes"],
               "all_phase_measurements_returned":result["all_phase_measurements_returned"],"errors":result["errors"]}
        put(out/"summary.json",report)
    report["complete"]=True;put(out/"summary.json",report);log({"phase":"terminal","stages":idx})

if __name__=="__main__":run()
