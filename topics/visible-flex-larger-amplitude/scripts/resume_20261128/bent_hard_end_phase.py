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
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"resume_20261126"))
import bent_end_phase_fields as fns
import bent_end_phase as base40
import bent_hard_end_fields as hf
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
    raw=base40.residual(f,m,p,base,n0)
    g=metric_rows(f,m);a,b,c=g.T
    least=1+.5*(a+c)-np.sqrt(.25*(a-c)**2+.5*b*b+1.e-20)
    return np.column_stack((raw,p["immersion_weight"]*base40.plus(p["minimum_eigenvalue"]-least)))

def metric_rows(f,m):
    g=fns.metric(f)
    return fns.whiten(tuple(x-y for x,y in zip(g,m.g0)),m.g0)

class Objective:
    def __init__(self,m,b,d,t,p,reg,z):
        self.m,self.b,self.d,self.t,self.p,self.reg=m,b,d,t,p,reg
        self.nominal=m.at(d,t);self.n0=fns.support_norm(self.nominal,m.sign,m.center)[0]
        initial=m.at(d,t,z[:hf.HARD])+b.val(z)
        err=fns.opnorm(metric_rows(initial,m))
        self.weight=m.weight*np.sqrt(1+np.minimum(16.,err/max(float(np.quantile(err,.82)),.01)))
        self.last=None
    def prep(self,z):
        if self.last is not None and np.array_equal(self.last,z):return
        self.last=z.copy();self.f=self.m.at(self.d,self.t,z[:hf.HARD])+self.b.val(z)
        self.r=residual(self.f,self.m,self.p,self.nominal,self.n0)
    def fun(self,z):
        self.prep(z)
        return np.r_[(self.r*self.weight[:,None]).ravel(),self.reg*z]
    def jac(self,z):
        self.prep(z);m,b=self.m,self.b;npnt,nr=self.r.shape
        g=np.empty((npnt,nr,6,3));cf=self.f.astype(complex);tiny=1.e-27
        for j in range(6):
            for i in range(3):
                cf[:,j,i]+=1j*tiny
                g[:,:,j,i]=residual(cf,m,self.p,self.nominal,self.n0).imag/tiny
                cf[:,j,i]-=1j*tiny
        g*=self.weight[:,None,None,None]
        h=np.empty((npnt*nr,hf.HARD));delta=self.p["hard_parameter_difference"]
        for j in range(hf.HARD):
            group="central" if j==0 else (1 if j in (1,2,3) or 7<=j<13 else -1)
            zp=z[:hf.HARD].copy();zm=zp.copy();zp[j]+=delta;zm[j]-=delta
            df=(m.part(self.d,self.t,zp,group)-m.part(self.d,self.t,zm,group))/(2*delta)
            h[:,j]=np.einsum("nrji,nji->nr",g,df,optimize=False).ravel()
        reg=self.reg
        # No columns are dropped. The two independent annular blocks have disjoint
        # support; use dense products when small, matrix-free full contractions otherwise.
        blocks=[]
        for sl in m.roll:
            a=g[sl]
            if nr*len(a)*3*b.m<=self.p["dense_jacobian_entries"]:
                mm=np.empty((nr*len(a),3*b.m))
                for i in range(3):
                    mm[:,i::3]=np.einsum("nrj,jnk->nrk",a[:,:,:,i],b.B,optimize=True).reshape(-1,b.m)
            else:mm=None
            blocks.append((sl,a,mm))
        def mv(q):
            q=q.ravel();v=(h@q[:hf.HARD]).reshape(npnt,nr)
            for (sl,a,mm),zz in zip(blocks,q[hf.HARD:].reshape(2,b.m,3)):
                if mm is not None:v[sl]+=(mm@zz.ravel()).reshape(-1,nr)
                else:v[sl]+=np.einsum("nrji,nji->nr",a,(b.B@zz).transpose(1,0,2),optimize=False)
            return np.r_[v.ravel(),reg*q]
        def rm(q):
            q=q.ravel();v=q[:-b.n].reshape(npnt,nr);result=[h.T@v.ravel()]
            for sl,a,mm in blocks:
                if mm is not None:result.append(mm.T@v[sl].ravel())
                else:
                    w=np.einsum("nrji,nr->nji",a,v[sl],optimize=False)
                    result.append((b.B.reshape(-1,b.m).T@np.ascontiguousarray(w.transpose(1,0,2)).reshape(-1,3)).ravel())
            return np.concatenate(result)+reg*q[-b.n:]
        return LinearOperator((npnt*nr+b.n,b.n),matvec=mv,rmatvec=rm,dtype=float)

def snapshot(m,b,d,t,z):
    base=m.at(d,t);f=m.at(d,t,z[:hf.HARD])+b.val(z)
    return base40.measured(m,f,base),f
def cloud(m,b,d,spline,times):
    O=np.array(m.ar.axial.axis());first=None;rows=[]
    for t in times:
        z=np.asarray(spline(t));f=m.at(d,float(t),z[:hf.HARD])+b.val(z)
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
    mods=[src,src.delay,src.delay.cap,src.ar,src.ar.axial,src.ar.old,src.ar.old.disk,
          importlib.import_module("r742_tilted_disk_two_jets"),fns,base40,hf,atlas39]
    hs={Path(m.__file__).name:filehash(m.__file__) for m in mods}
    if hs!=p["source_sha256"]:raise ValueError("source chain differs")
    meta={"schema":"hard-central-caps-delayed-end/v1","source_sha256":filehash(__file__),"params_sha256":filehash(a.params),
         "sources":hs,"numpy":np.__version__,"scipy":scipy.__version__,"stages":[],
         "target":"One R752 phase-zero unmarked physical pullback, Y=.37/e=.81/angular cutoff 1/1024, on every point with t in [0,pi/2]. Fixed across all designs/refinements.",
         "scope":"Actual finite phase geometry and Gram estimates on complete spatial chart grids and independent time refinements. Continuous exact isometry, tube bounds for corrected fields, and convergence require separate evidence."}
    begin=time.monotonic()
    def save():meta["elapsed_seconds"]=time.monotonic()-begin;save_json(out/"summary.json",meta)
    def solve(m,b,d,t,z,cfg,stage,ti):
        base=m.at(d,t);obj=Objective(m,b,d,t,p,cfg["regularizer"],z)
        ff=obj.fun(z);J=obj.jac(z)
        q=np.cos(np.arange(b.n)*.939+.07);q/=np.linalg.norm(q)
        w=np.sin(np.arange(len(ff))*.613+.21);w/=np.linalg.norm(w)
        jv=J.matvec(q);adj=abs(float(jv@w-q@J.rmatvec(w)))
        hp=p["jacobian_probe"]
        fd=float(np.linalg.norm((obj.fun(z+hp*q)-obj.fun(z-hp*q))/(2*hp)-jv)/max(np.linalg.norm(jv),1e-15))
        # Actual column jet magnitudes, sampled once instead of doing b.n separate products.
        B=b.B
        mag=np.sqrt(np.sum(np.mean(B**2,axis=1)*np.array([.01,1.,1.,.0008,.0016,.0008])[:,None],axis=0))
        scale=np.r_[np.full(hf.HARD,.60),np.tile(np.repeat(1./np.maximum(mag,.0001),3),2)]
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
        g,_,_,_,_=fns.properties(m.at(d,t,z[:hf.HARD])+b.val(z),m)
        report={"index":ti,"phase":float(t),"point_sha256":digest(z),"nfev":int(res.nfev),"njev":int(res.njev or 0),
                "status":int(res.status),"cost":float(res.cost),"optimality":float(res.optimality),
                "adjoint_abs":adj,"directional_fd_relative":fd,"train_gram":float(fns.opnorm(g).max())}
        return z,report
    def run(d,cfg,prior=None):
        idx=len(meta["stages"]);m=hf.Mesh(src,cfg["mesh"],0.);b=hf.Basis(m,cfg)
        knots=np.linspace(0.,np.pi/2,cfg["intervals"]+1);Z=[np.zeros(b.n)];rr=[]
        pred=None
        if prior:
            oldnames,nt,zz,_=prior
            pred=CubicSpline(nt,zz,axis=0,bc_type="natural")
        for k,t in enumerate(knots[1:],1):
            z=b.project(oldnames,pred(t)) if pred else Z[-1].copy()
            # Continue the deformation amplitude from the actual, preceding phase.
            if pred is None and k>1:z[hf.HARD:]*=np.sin(t)/np.sin(knots[k-1])
            z,r=solve(m,b,d,t,z,cfg,idx,k);Z.append(z);rr.append(r)
            meta["in_progress"]={"stage":idx,"design":d["id"],"complete_knots":k,"last_knot":r};save()
            print(json.dumps({"event":"solved_knot","stage":idx,**r}),flush=True)
        Z=np.array(Z);spline=CubicSpline(knots,Z,axis=0,bc_type="natural")
        names=b.names;b=None;m=None
        ck=hf.Mesh(src,cfg["check"],.237);cb=hf.Basis(ck,cfg)
        raw0=ck.at(d,0.)
        same0=float(abs(raw0-ck.f0).max())
        ts=np.linspace(0,np.pi/2,2*cfg["intervals"]+1)
        if cfg["extra_check"]:
            h=(np.pi/2)/cfg["intervals"];ts=np.unique(np.r_[ts,knots[:-1]+.2113248654*h,knots[:-1]+.7886751346*h])
        worsts={};stats=[];perchart={};jumps=np.zeros((2,2))
        for t in ts:
            val,f=snapshot(ck,cb,d,float(t),np.asarray(spline(t)))
            jumps=np.maximum(jumps,hf.seams(ck,f))
            for name in ["gram","K","support","area_min","max_physical_correction"]:
                v=val[name];prev=worsts.get(name);lo=name in ["support","area_min"]
                if prev is None or (v["value"]<prev["value"] if lo else v["value"]>prev["value"]):
                    worsts[name]={"phase":float(t),**v}
            for name,gval in val["charts_gram_K_support_arg_uv"].items():
                if name not in perchart or gval[0]>perchart[name][0]:
                    perchart[name]=[gval[0],float(t),gval[3],gval[4]]
            stats.append([float(t),val["gram"]["value"],val["gram_rms"],val["K"]["value"],val["support"]["value"]])
        direct=[]
        target_t=float(knots[-1]);hard=Z[-1,:hf.HARD]
        cached=ck.at(d,target_t,hard);shape=hf.hshape(src,d,hard)
        for label,u,v,sl in ck.cases:
            jj=np.unique(np.linspace(0,len(u)-1,min(11,len(u)),dtype=int))
            exact=src.chart_jet(label,u[jj],v[jj],target_t,shape=shape,method=d["method"],rotate=False)
            direct.append([label,float(abs(cached[sl][jj]-exact).max())])
        fname=out/("stage-%02d.npz"%idx);np.savez(fname,phases=knots,coefficients=Z)
        g=worsts["gram"]["value"];k=worsts["K"]["value"];su=worsts["support"]["value"]
        score=float(g+.70*max(0.,k/p["curvature_cap"]-1)+3*max(0.,p["support_goal"]-su))
        rec={"stage":idx,"design":d,"configuration":cfg,"coefficient_count_per_phase":int(Z.shape[1]),
                "shape":list(Z.shape),"point_sha256":digest(Z),"time_data_sha256":digest(knots),
                "previous_point_sha256":digest(prior[2]) if prior else None,
                "npz_sha256":filehash(fname),"npz_bytes":fname.stat().st_size,
                "direct_source_sixjet_comparison_at_last_phase":direct,"zero_phase_sixjet_difference":same0,"knots":rr,"all_time_check":worsts,"worst_gram_by_chart":perchart,
                "check_phase_columns":["phase","max_gram","rms_gram","max_abs_principal","min_support"],
                "check_phases":stats,"score":score,"maximum_seam_sixjet_jumps":jumps.tolist(),
                "terminal_hard_coordinates":Z[-1,:hf.HARD].tolist(),
                "terminal_physical_control":hf.hshape(src,d,Z[-1,:hf.HARD]).__dict__}
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
        meta["selected_design"]=d
        # The following levels all use the unchanged analytic g from the first stage.
        levels=[prev]
        for cfg in p["refinements"]:
            prev=run(d,cfg,prev);levels.append(prev)
        for names,nt,Z,rec in levels:
            cfg=rec["configuration"];spline=CubicSpline(nt,Z,axis=0,bc_type="natural")
            active=rec["design"]
            m=hf.Mesh(src,p["cloud_grid"],0.);b=hf.Basis(m,cfg)
            rec["whole_phase_clouds"]=cloud(m,b,active,spline,p["geometry_phases"]);del b,m
            m=hf.Mesh(src,p["moment_grid"],0.);b=hf.Basis(m,cfg)
            moments=[]
            for t in p["geometry_phases"]:
                z=spline(t);f=m.at(active,t,z[:hf.HARD])+b.val(z);moments.append({"phase":t,**base40.surface_integrals(m,f)})
            rec["moments"]=moments;del b,m;save()
        meta["status"]="completed_full_finite_time_and_fixed_metric_refinements";save()
    except Exception as e:
        meta["status"]="runtime_failure";meta["exception"]=type(e).__name__+": "+str(e)[:1200];save()
        traceback.print_exc();return 1
    return 0
if __name__=="__main__":
    raise SystemExit(main())
