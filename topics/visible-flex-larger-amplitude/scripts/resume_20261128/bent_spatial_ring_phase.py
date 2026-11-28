"""Public full-domain R775 spatial physical fit, with two separately continued same-metric chains."""
import argparse,hashlib,importlib.util,json,os,sys,time
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"resume_20261126"))
import bent_spatial_ring_fields as fld
import bent_spatial_ring_system as sysfit
import r775_nonplanar_compensated_section_two_jets as ref
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
        z=fld.target(key,u,v,order);B=fld.basis(key,u,v,z,ns,d)
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
    ts=np.linspace(0.,np.pi/2,2*T+1)[1:];W=sysfit.clock(nodes,ts)
    Z=transfer(old,nodes,ns)
    if old is None:
        for key,dim,value in d["seed"]:
            j=ns.index(tuple(key));Z[:,j,dim]=value*np.sin(nodes[1:])
    tabs,vals=base_fields(table,d,ts,order);hist=[]
    for it in range(conf["iterations"]):
        step,read=sysfit.shape_step(tabs,vals,W,Z,par)
        best=read["current_objective"];picked=0.;newpeak=read["raw_max_gram"]
        for k in range(par["line_trials"]):
            f=2.**(-k);v,p=sysfit.objective(tabs,vals,W,Z+f*step,par)
            if v<best:
                best,picked,newpeak=v,f,p;Z=Z+f*step;break
        read.update(accepted_line_scale=picked,actual_new_objective=best,actual_new_peak=newpeak)
        hist.append(read);progress({"iteration":it,"objective":best,"accepted_scale":picked,"training_gram":newpeak})
    return Z,nodes,ns,hist

def true_eval(conf,d,Z,nodes,ns):
    other=dict(conf,ns=conf["check_ns"],nv=conf["check_nv"])
    table=charts(other,conf["check_order"],True,d);times=np.linspace(0.,np.pi/2,conf["check_phases"])
    W=sysfit.clock(nodes,times);by={};peaks={};phase_rows=[];initial=None;held=[];mark=[];support=[]
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
        phase_rows.append([float(t),gmx,kmx,amin])
        if initial is None:initial=pts;c0=cKDTree(pts)
        if i in (0,len(times)//2,len(times)-1):
            ct=cKDTree(pts)
            held.append([float(t),float(c0.query(pts)[0].max()),float(ct.query(initial)[0].max())])
    return dict(peaks=peaks,charts=by,phase_gram_curvature_area=phase_rows,finite_two_directed_held=held,
                evaluation_order=conf["check_order"],station_count=other["ns"],bridge_subdivisions=other["nv"],
                finite_points_per_phase=sum(len(x[1]) for x in table),phase_axis_floor_minimum_margin=support)

def identity(d,ns,Z,nodes,files,par,path):
    docs={"schema":"r775-spatial-ring-signed-support-identity-v1","design":d,"column_names":ns,"actual_coefficient_le_f64":ah(Z),
          "actual_coefficient_shape":list(Z.shape),"time_nodes_le_f64":ah(nodes),"fixed_sources":files,
          "fixed_metric":par["fixed_metric"],"world_motion":"R775 axial support floor times a positive scalar, R772 fixed right head; selected design fixes or releases the left head",
          "temporal_basis":"CubicSpline natural left, zero right derivative at pi/2; zero coefficient at t0",
          "continuum_integrals":"R775 + R772 exact material integrals; recorded working quadrature fixes array interpretation",
          "physical_order":par["defining_order"]}
    raw=json.dumps(docs,sort_keys=True,separators=(",",":")).encode()
    with path.open("wb") as h:np.savez_compressed(h,coefficients=Z,time_nodes=nodes)
    return hashlib.sha256(raw).hexdigest(),docs,dict(path=path.name,bytes=path.stat().st_size,sha256=hashlib.sha256(path.read_bytes()).hexdigest())

def run():
    p=argparse.ArgumentParser()
    for a in ("params","geometry-source","export-source","out"):p.add_argument("--"+a,required=True)
    a=p.parse_args();out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    par=json.loads(Path(a.params).read_text())
    if Path(a.geometry_source).resolve()!=Path(ref.__file__).resolve():raise ValueError("wrong actual R775 geometry module")
    ep=Path(a.export_source);spec=importlib.util.spec_from_file_location("r772_mesh_terminal",ep)
    ex=importlib.util.module_from_spec(spec);spec.loader.exec_module(ex)
    files={"params":hashlib.sha256(Path(a.params).read_bytes()).hexdigest()}
    for p in [Path(__file__),Path(fld.__file__),Path(sysfit.__file__),Path(ref.__file__),Path(ref.g.__file__),Path(ref.g.guard.__file__),Path(ref.g.guard.old.__file__),
              Path(fld.richer.__file__),Path(sysfit.ref.__file__),Path(sys.modules["r767_preloaded_cap_atlas"].__file__),Path(sys.modules["r742_tilted_disk_two_jets"].__file__),ep,
              ep.with_name("closed_body_mesh_terminal.py"),ep.with_name("closed_body_mesh_geometry.py")]:
        files[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
    assert par["defining_order"]==par["refine"][-1]["check_order"]
    report={"schema":"r775-spatial-ring-closed-body-phase-run-v1","sources":files,"fixed_metric":par["fixed_metric"],
            "stages":[],"closed_exports":{},"field_families":par["families"],"notes":par["limits"]}
    put(out/"summary.json",report);allstates={};idx=0
    def save_stage(d,conf,old,desc):
        nonlocal idx
        n=idx;idx+=1;start=time.monotonic();log({"stage":n,"start":desc,"budget":conf})
        Z,nodes,ns,hist=stage_fit(conf,par["solver"],d,old,lambda rec:log({"stage":n,**rec}))
        val=true_eval(conf,d,Z,nodes,ns);sha,doc,npz=identity(d,ns,Z,nodes,files,par,out/("stage-%02d-field.npz"%n))
        score=val["peaks"]["gram"]["value"]+.02*max(0.,val["peaks"]["curvature"]["value"]-par["solver"]["curvature_bound"])+.20*max(0.,par["solver"]["area_floor"]-val["peaks"]["area"]["value"])
        st=dict(stage=n,name=desc,design=d,budget=conf,point_sha256=sha,point_identity=doc,field_npz=npz,score=score,
                working_integration_order=conf["order"],training_history=hist,independent=val,
                elapsed_seconds=time.monotonic()-start)
        ret=put(out/("stage-%02d-return.json"%n),st)
        report["stages"].append(dict(stage=n,name=desc,point_sha256=sha,score=score,
               gram=val["peaks"]["gram"],curvature=val["peaks"]["curvature"],area=val["peaks"]["area"],
               complete_stage_file=ret,field_shape=list(Z.shape),field_le_f64_sha256=ah(Z)))
        put(out/"summary.json",report);log({"phase":"stage_complete","stage":n,"point":sha,"score":score,
               "gram":val["peaks"]["gram"],"curvature":val["peaks"]["curvature"]})
        return score,(Z,nodes,ns),sha
    # Both independent design families receive their own complete same-target refinements and final geometry.
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
        dest=out if family=="hard_heads" else out/"free-left";dest.mkdir(exist_ok=True)
        result=ex.export_final(dest,sha,np.linspace(0.,np.pi/2,65),ref.P,ref.HALF_WIDTH,ref.L,f,
                 target_evaluator=target,mesh_times=np.linspace(0.,np.pi/2,7),cap_atlas=ref.g,material_order=O,
                 profile_extra=np.unique(np.r_[ref.profile_marks(),ref.cuts(O)]),end_extra=[0.,ref.g.SM,ref.L-ref.g.SM,ref.L],central_extra=np.unique(np.r_[ref.axial_marks(),-.485,-.47,-.455,.455,.47,.485]),
                 progress=lambda rec:log({"phase":"closed_mesh","family":family,"measurement":rec}))
        doc=put(dest/"closed-geometry-index.json",result)
        report["closed_exports"][family]={"point_sha256":sha,"directory":str(dest.relative_to(out)),
               "index":doc,"finite_extrema":result["finite_extrema"],"complete_requested_meshes":result["complete_requested_meshes"],
               "all_phase_measurements_returned":result["all_phase_measurements_returned"],"errors":result["errors"]}
        put(out/"summary.json",report)
    report["complete"]=True;put(out/"summary.json",report);log({"phase":"terminal","stages":idx})

if __name__=="__main__":run()
