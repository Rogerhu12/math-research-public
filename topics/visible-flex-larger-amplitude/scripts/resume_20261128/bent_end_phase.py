#!/usr/bin/env python3
"""Direct finite-time search with one fixed complete metric and both moving physical ends."""
import argparse
import hashlib
import importlib
import json
import os
import sys
import time
import traceback
from pathlib import Path
import numpy as np
import scipy
from scipy.interpolate import CubicSpline
from scipy.optimize import least_squares
from scipy.sparse.linalg import LinearOperator
from scipy.spatial import cKDTree
import bent_end_phase_fields as fns
import bent_body_atlas as atlas39

def digest(x):return hashlib.sha256(np.ascontiguousarray(x,dtype="<f8").tobytes()).hexdigest()
def filehash(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def save_json(path,obj):
    tmp=path.with_suffix(".tmp");tmp.write_text(json.dumps(obj,separators=(",",":"),sort_keys=True,allow_nan=False)+"\n")
    os.replace(tmp,path)
def extrem(m,a,high=True):
    i=int(a.argmax() if high else a.argmin())
    return {"value":float(a[i]),**m.name(i)}
def plus(x):return np.where(x.real>0,x,0.)

def residual(f,m,p,base,n0):
    gram,bend,sup,area,n=fns.properties(f,m)
    z=f[:,0]-base[:,0];dn=fns.dot(z,n0)
    length=np.sqrt(fns.dot(z,z)+1.e-20)
    near=np.sqrt(dn*dn+1e-20)
    # Metric uses the full tensor in the fixed initial metric, including
    # both off-diagonal slots with their Frobenius weight.
    h=p["metric_loss_scale"]
    return np.column_stack([h*np.arcsinh(gram/h),p["bend_weight"]*plus(bend/p["curvature_cap"]-1.),
           p["support_weight"]*plus(p["support_goal"]-sup),p["normal_displace_weight"]*plus(near-p["normal_displace_goal"]),
           p["travel_weight"]*plus(length-p["travel_goal"])])

class Objective:
    def __init__(self,m,b,base,p,reg,z):
        self.m,self.b,self.base,self.p,self.reg=m,b,base,p,reg
        self.n0=fns.support_norm(base,m.sign,m.center)[0]
        g=fns.properties(base+b.val(z),m)[0];w=fns.opnorm(g)
        self.weight=m.weight*np.sqrt(1+np.minimum(9.,w/max(float(np.quantile(w,.80)),.01)))
        self.last=None
    def prep(self,z):
        if self.last is not None and np.array_equal(z,self.last):return
        self.last=z.copy();self.f=self.base+self.b.val(z)
        self.r=residual(self.f,self.m,self.p,self.base,self.n0)
    def fun(self,z):
        self.prep(z);return np.r_[(self.r*self.weight[:,None]).ravel(),self.reg*z]
    def jac(self,z):
        self.prep(z);ns,cols=self.r.shape
        g=np.empty((ns,cols,6,3))
        cf=self.f.astype(complex);h=1.e-27
        for j in range(6):
            for i in range(3):
                cf[:,j,i]+=1j*h
                g[:,:,j,i]=residual(cf,self.m,self.p,self.base,self.n0).imag/h
                cf[:,j,i]-=1j*h
        g*=self.weight[:,None,None,None]
        b,reg=self.b,self.reg
        if ns*cols*b.n<=self.p["dense_jacobian_entries"]:
            M=np.empty((ns*cols,b.n))
            for i in range(3):
                block=np.einsum("nrj,jnk->nrk",g[:,:,:,i],b.B,optimize=True)
                M[:,i::3]=block.reshape(ns*cols,b.m)
            def dense_mv(q):q=q.ravel();return np.r_[M@q,reg*q]
            def dense_rm(q):q=q.ravel();return M.T@q[:-b.n]+reg*q[-b.n:]
            return LinearOperator((ns*cols+b.n,b.n),matvec=dense_mv,rmatvec=dense_rm,dtype=float)
        def mv(q):
            q=q.ravel();v=np.einsum("nrji,nji->nr",g,b.val(q),optimize=False)
            return np.r_[v.ravel(),reg*q]
        def rm(q):
            q=q.ravel();v=np.einsum("nrji,nr->nji",g,q[:-b.n].reshape(ns,cols),optimize=False)
            return b.adj(v)+reg*q[-b.n:]
        return LinearOperator((ns*cols+b.n,b.n),matvec=mv,rmatvec=rm,dtype=float)

def measured(m,f,base):
    gram,bend,sup,area,n=fns.properties(f,m);e=fns.opnorm(gram)
    out={"gram":extrem(m,e),"gram_rms":float(np.sqrt(np.average(e*e,weights=m.weight**2))),
         "K":extrem(m,bend),"support":extrem(m,sup,False),"area_min":extrem(m,area,False),
         "max_physical_correction":extrem(m,np.linalg.norm(f[:,0]-base[:,0],axis=1))}
    charts={}
    for name in ("cylinder","end+","end-","cap+","cap-","cap-cartesian+","cap-cartesian-"):
        use=m.lab==name;ix=np.nonzero(use)[0];i=ix[e[use].argmax()]
        charts[name]=[float(e[i]),float(bend[use].max()),float(sup[use].min()),float(m.xy[i,0]),float(m.xy[i,1])]
    out["charts_gram_K_support_arg_uv"]=charts
    return out

def snapshot(m,b,d,t,z):
    base=m.at(d,t);f=base+b.val(z)
    return measured(m,f,base),f

def surface_integrals(m,f):
    y=f[:,0];n=np.cross(f[:,1],f[:,2])*m.sign[:,None]
    h=fns.dot(y,n);val=np.column_stack([h/3,y*h[:,None]/4,fns.dot(y,y)*h/5])
    total=np.zeros(5)
    P=2*m.g.profile_constants(32)[4]
    for name in ("cylinder","end+","end-","cap+","cap-"):
        ii=m.lab==name;u=np.unique(m.xy[ii,0]);v=np.unique(m.xy[ii,1]);a=val[ii].reshape(len(u),len(v),5)
        a=np.r_[a,a[:1]]
        if name.startswith("cap"):
            a=np.concatenate([np.zeros_like(a[:,:1]),a],axis=1);v=np.r_[0.,v]
        total+=np.trapezoid(np.trapezoid(a,v,axis=1),np.r_[u,u[0]+P],axis=0)
    return {"signed_volume":float(total[0]),"first_moment":total[1:4].tolist(),
          "centered_second_moment":float(total[4]-total[1:4]@total[1:4]/total[0])}

def cloud(m,b,d,spline,times):
    O=np.array(m.ar.axial.axis());first=None;rows=[]
    for t in times:
        base=m.at(d,float(t));f=base+b.val(np.asarray(spline(t)))
        pts=f[:,0].copy();n=fns.support_norm(f,m.sign,m.center)[0]
        xx,zz=pts[:,0]-O[0],pts[:,2]-O[1];co,si=np.cos(t),np.sin(t)
        pts[:,0]=O[0]+co*xx-si*zz;pts[:,2]=O[1]+si*xx+co*zz
        nx=n[:,0].copy();nz=n[:,2].copy();n[:,0]=co*nx-si*nz;n[:,2]=si*nx+co*nz
        tree=cKDTree(pts)
        if first is None:first=(pts.copy(),tree)
        inv=0.;dm=0.;ij=(0,0)
        for j in range(0,len(pts),32):
            v=pts[None,:,:]-pts[j:j+32,None,:];dd=np.einsum("bni,bni->bn",v,v)
            z=2*abs(np.einsum("bni,bi->bn",v,n[j:j+32]))/np.where(dd>1e-16,dd,np.inf)
            dm=max(dm,float(dd.max()))
            if z.max()>inv:
                r,c=np.unravel_index(z.argmax(),z.shape);inv=float(z[r,c]);ij=(int(j+r),int(c))
        rows.append({"phase":float(t),"point_count":len(pts),"sample_held":float(max(tree.query(first[0])[0].max(),first[1].query(pts)[0].max())),
              "diameter":float(np.sqrt(dm)),"ordered_inverse_reach":inv,"ordered_arg":[m.name(ij[0]),m.name(ij[1])]})
    return rows

def main():
    ap=argparse.ArgumentParser()
    for k in ("params","geometry-source","out"):ap.add_argument("--"+k,required=True)
    a=ap.parse_args();p=json.loads(Path(a.params).read_text());out=Path(a.out);out.mkdir(exist_ok=True,parents=True)
    srcpath=Path(a.geometry_source).resolve();sys.path.insert(0,str(srcpath.parent));src=importlib.import_module(srcpath.stem)
    mods=[src,src.ar,src.ar.axial,src.ar.old,src.ar.old.disk,importlib.import_module("r742_tilted_disk_two_jets"),fns,atlas39]
    hs={Path(m.__file__).name:filehash(m.__file__) for m in mods}
    if hs!=p["source_sha256"]:raise ValueError("source chain differs")
    meta={"schema":"direct-finite-axial-flex/v1","source_sha256":filehash(__file__),"params_sha256":filehash(a.params),
         "sources":hs,"numpy":np.__version__,"scipy":scipy.__version__,"stages":[],
         "target":"The R747 common initial physical pullback on every original material point, no masks omitted in verification. This g, material chart and [0,pi/2] are identical in every design and refinement.",
         "scope":"Actual finite phase geometry and Gram estimates on complete spatial chart grids and independent time refinements. Continuous exact isometry, tube bounds for corrected fields, and convergence require separate evidence."}
    begin=time.monotonic()
    def save():meta["elapsed_seconds"]=time.monotonic()-begin;save_json(out/"summary.json",meta)
    def solve(m,b,d,t,z,cfg,stage,ti):
        base=m.at(d,t);obj=Objective(m,b,base,p,cfg["regularizer"],z)
        ff=obj.fun(z);J=obj.jac(z)
        q=np.cos(np.arange(b.n)*.939+.07);q/=np.linalg.norm(q)
        w=np.sin(np.arange(len(ff))*.613+.21);w/=np.linalg.norm(w)
        jv=J.matvec(q);adj=abs(float(jv@w-q@J.rmatvec(w)))
        hp=p["jacobian_probe"]
        fd=float(np.linalg.norm((obj.fun(z+hp*q)-obj.fun(z-hp*q))/(2*hp)-jv)/max(np.linalg.norm(jv),1e-15))
        # Actual column jet magnitudes, sampled once instead of doing b.n separate products.
        B=b.B
        mag=np.sqrt(np.sum(np.mean(B**2,axis=1)*np.array([.01,1.,1.,.0008,.0016,.0008])[:,None],axis=0))
        scale=np.repeat(1./np.maximum(mag,1e-4),3)
        state=[np.inf,0.,0]
        def fun(q):
            r=obj.fun(q);v=float(r@r/2);state[2]+=1
            if v<state[0]:
                state[0]=v
                if time.monotonic()-state[1]>35.:
                    state[1]=time.monotonic()
                    meta["in_progress"]={"stage":stage,"knot_index":ti,"phase":float(t),"design":d["id"],
                         "call":state[2],"cost":v,"point_sha256":digest(q)}
                    with open(out/"current.tmp","wb") as st:np.savez(st,point=q,phase=t)
                    os.replace(out/"current.tmp",out/"current.npz");save()
            return r
        res=least_squares(fun,z,jac=obj.jac,method="trf",tr_solver="lsmr",x_scale=scale,
                max_nfev=cfg["max_nfev"],ftol=1e-10,xtol=1e-10,gtol=1e-10,
                tr_options={"maxiter":cfg["inner"],"atol":4e-7,"btol":4e-7})
        z=res.x
        g,_,_,_,_=fns.properties(base+b.val(z),m)
        report={"index":ti,"phase":float(t),"point_sha256":digest(z),"nfev":int(res.nfev),"njev":int(res.njev or 0),
                "status":int(res.status),"cost":float(res.cost),"optimality":float(res.optimality),
                "adjoint_abs":adj,"directional_fd_relative":fd,"train_gram":float(fns.opnorm(g).max())}
        return z,report
    def run(d,cfg,prior=None):
        idx=len(meta["stages"]);m=fns.Mesh(src,cfg["mesh"],0.);b=fns.Basis(m,d,cfg)
        knots=np.linspace(0.,np.pi/2,cfg["intervals"]+1);Z=[np.zeros(b.n)];rr=[]
        pred=None
        if prior:
            oldnames,nt,zz,_=prior
            pred=CubicSpline(nt,zz,axis=0,bc_type="natural")
        for k,t in enumerate(knots[1:],1):
            z=b.project(oldnames,pred(t)) if pred else Z[-1].copy()
            # Continue the deformation amplitude from the actual, preceding phase.
            if pred is None and k>1:z*=np.sin(t)/np.sin(knots[k-1])
            z,r=solve(m,b,d,t,z,cfg,idx,k);Z.append(z);rr.append(r)
            meta["in_progress"]={"stage":idx,"design":d["id"],"complete_knots":k,"last_knot":r};save()
            print(json.dumps({"event":"solved_knot","stage":idx,**r}),flush=True)
        Z=np.array(Z);spline=CubicSpline(knots,Z,axis=0,bc_type="natural")
        names=b.names;b=None;m=None
        ck=fns.Mesh(src,cfg["check"],.237);cb=fns.Basis(ck,d,cfg)
        raw0=ck.at(d,0.)
        same0=float(abs(raw0-ck.f0).max())
        ts=np.linspace(0,np.pi/2,2*cfg["intervals"]+1)
        if cfg["extra_check"]:
            h=(np.pi/2)/cfg["intervals"];ts=np.unique(np.r_[ts,knots[:-1]+.2113248654*h,knots[:-1]+.7886751346*h])
        worsts={};stats=[];perchart={}
        for t in ts:
            val,f=snapshot(ck,cb,d,float(t),np.asarray(spline(t)))
            for name in ["gram","K","support","area_min","max_physical_correction"]:
                v=val[name];prev=worsts.get(name);lo=name in ["support","area_min"]
                if prev is None or (v["value"]<prev["value"] if lo else v["value"]>prev["value"]):
                    worsts[name]={"phase":float(t),**v}
            for name,gval in val["charts_gram_K_support_arg_uv"].items():
                if name not in perchart or gval[0]>perchart[name][0]:
                    perchart[name]=[gval[0],float(t),gval[3],gval[4]]
            stats.append([float(t),val["gram"]["value"],val["gram_rms"],val["K"]["value"],val["support"]["value"]])
        fname=out/("stage-%02d.npz"%idx);np.savez(fname,phases=knots,coefficients=Z)
        g=worsts["gram"]["value"];k=worsts["K"]["value"];su=worsts["support"]["value"]
        score=float(g+.70*max(0.,k/p["curvature_cap"]-1)+3*max(0.,p["support_goal"]-su))
        rec={"stage":idx,"design":d,"configuration":cfg,"coefficient_count_per_phase":int(Z.shape[1]),
                "shape":list(Z.shape),"point_sha256":digest(Z),"time_data_sha256":digest(knots),
                "previous_point_sha256":digest(prior[2]) if prior else None,
                "npz_sha256":filehash(fname),"npz_bytes":fname.stat().st_size,
                "zero_phase_sixjet_difference":same0,"knots":rr,"all_time_check":worsts,"worst_gram_by_chart":perchart,
                "check_phase_columns":["phase","max_gram","rms_gram","max_abs_principal","min_support"],
                "check_phases":stats,"score":score}
        meta["stages"].append(rec);meta.pop("in_progress",None);save()
        print(json.dumps({"event":"stage","stage":idx,"point":rec["point_sha256"],"score":score,
                        "gram":g,"K":k,"support":su}),flush=True)
        return names,knots,Z,rec
    save()
    try:
        start=[]
        for d in p["designs"]:
            res=run(d,p["coarse"]);start.append((res[-1]["score"],d,res))
        _,d,prev=min(start,key=lambda q:q[0])
        meta["selected_coarse_design"]=d
        if d["central"]=="locked":
            d=dict(d,id=d["id"]+"-expanded",central="expanded")
            meta["continuation"]="The complete locked coarse field is embedded by name in a strict superset; new central directions vanish only on the actual grip and at the protected positive cap-center first jet."
        meta["selected_design"]=d
        # The following levels all use the unchanged analytic g from the first stage.
        levels=[prev]
        for cfg in p["refinements"]:
            prev=run(d,cfg,prev);levels.append(prev)
        for names,nt,Z,rec in levels:
            cfg=rec["configuration"];spline=CubicSpline(nt,Z,axis=0,bc_type="natural")
            active=rec["design"]
            m=fns.Mesh(src,p["cloud_grid"],0.);b=fns.Basis(m,active,cfg)
            rec["whole_phase_clouds"]=cloud(m,b,active,spline,p["geometry_phases"]);del b,m
            m=fns.Mesh(src,p["moment_grid"],0.);b=fns.Basis(m,active,cfg)
            moments=[]
            for t in p["geometry_phases"]:
                f=m.at(active,t)+b.val(spline(t));moments.append({"phase":t,**surface_integrals(m,f)})
            rec["moments"]=moments;del b,m;save()
        meta["status"]="completed_full_finite_time_and_fixed_metric_refinements";save()
    except Exception as e:
        meta["status"]="runtime_failure";meta["exception"]=type(e).__name__+": "+str(e)[:1200];save()
        traceback.print_exc();return 1
    return 0
if __name__=="__main__":
    raise SystemExit(main())
