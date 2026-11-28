#!/usr/bin/env python3
"""Finite Killing-field design on the actual tilted disk, two fixed Haar refinements."""
import argparse
import hashlib
import importlib
import json
import os
import sys
import time
import traceback
from pathlib import Path
from types import SimpleNamespace
import numpy as np
import scipy
from scipy.optimize import least_squares
from scipy.sparse.linalg import LinearOperator
from scipy.spatial import cKDTree
import bent_disk_shoulder as old
import bent_disk_arclength as arc
import bent_disk_killing_fields as kf
from bent_disk_killing_fields import PAIRS,DT,row,scalar,apply,pull,forms,ortho,geom,normop
import bent_disk_killing_target as kt

class Native:
    """Same actual run-37 nonpolynomial seed with its original six jets."""
    base=SimpleNamespace(A_LENGTH=.25)
    def __init__(self,params,d):
        self.disk=old.Disk(dict(params,angle=d.gamma,height=d.height))
    def shoulder_jet(self,s,theta,design,normalized):
        s,theta=np.broadcast_arrays(s,theta);sh=s.shape
        if s.ndim==2 and np.all(s==s[:,:1]) and np.all(theta==theta[:1,:]):
            b=arc.Native(self.disk,design.length,.98,3,2,s[:,0]/design.length,theta[0])
            return np.stack([b.base[j,k]@self.disk.frame.T for j,k in PAIRS],axis=-2)
        out=np.empty((s.size,6,3));s=s.ravel();theta=theta.ravel()
        for a in np.unique(theta):
            ind=theta==a
            b=arc.Native(self.disk,design.length,.98,3,2,s[ind]/design.length,[a])
            for i,p in enumerate(PAIRS):
                out[ind,i,:]=b.base[p][:,0]@self.disk.frame.T
        return out.reshape(sh+(6,3))

def transfer(oldbank,cf,newbank):
    out=np.zeros(newbank.n)
    for oldsp,osl,nsp,nsl in zip(oldbank.spaces,oldbank.sl,newbank.spaces,newbank.sl):
        if oldsp.shape==nsp.shape and np.array_equal(oldsp.spl.t,nsp.spl.t):
            out[nsl]=cf[osl]
            continue
        allknots=np.unique(np.r_[nsp.spl.t,oldsp.spl.t])
        s=np.concatenate([np.linspace(l,h,9,endpoint=False) for l,h in zip(allknots,allknots[1:])]+[allknots[-1:]])
        vals=oldsp.spl(s)@cf[osl].reshape(oldsp.shape)
        dest=out[nsl].reshape(nsp.shape);m=min(dest.shape[1],vals.shape[1])
        dest[:,:m]=np.linalg.lstsq(nsp.spl(s),vals[:,:m],rcond=1e-14)[0]
    return out

class Adapter:
    def __init__(self,b,p):
        self.b=b;self.disk=old.Disk(dict(p["disk"],angle=b.d.gamma,height=b.d.height))
        self.n=b.F.n;self.t=b.s;self.theta=b.a
    def field(self,c,j,k):
        return self.b.base[...,PAIRS.index((j,k)),:]+self.b.F.values(c,j,k)
    def delta(self,c,j,k):
        return self.b.F.values(c,j,k)
    def adjoint(self,v,j,k):
        return self.b.F.adj(v,j,k)

def support(b,f,p):
    center=np.array([p["support_center_world_x"]/np.cos(b.d.gamma),0.,0.])
    pos,u,v=f[:3];nu=np.cross(u,v); area=np.maximum(np.linalg.norm(nu,axis=-1),1e-12)
    n=nu/row(area);rel=pos-center
    h=scalar(rel,n)
    ngrad=(rel-row(h)*n)/row(area)
    return h,(n,np.cross(v,ngrad),np.cross(ngrad,u))

def shapeadj(f,x,v,b):
    _,u,w,uu,uw,ww=f
    a,ds,dt=x
    ys=row(a[...,0])*uu+row(a[...,1])*uw+row(ds[...,0])*u+row(ds[...,1])*w
    yt=row(a[...,0])*uw+row(a[...,1])*ww+row(dt[...,0])*u+row(dt[...,1])*w
    gs=2*row(v[...,0])*u+row(v[...,1])*w
    gt=row(v[...,1])*u+2*row(v[...,2])*w
    gu=2*row(v[...,0])*ys+row(v[...,1])*yt+row(ds[...,0])*gs+row(dt[...,0])*gt
    gw=row(v[...,1])*ys+2*row(v[...,2])*yt+row(ds[...,1])*gs+row(dt[...,1])*gt
    return (b.adj(gu,1,0)+b.adj(gw,0,1)+b.adj(row(a[...,0])*gs,2,0)
           +b.adj(row(a[...,1])*gs+row(a[...,0])*gt,1,1)+b.adj(row(a[...,1])*gt,0,2))

class Shape:
    def __init__(self,b,p,cf,cx,reg,target):
        self.b,self.p,self.cx,self.target=b,p,cx,target
        self.x=b.vect(cx);self.ad=Adapter(b,p);self.geom=old.Objective(self.ad,p,reg,None)
        self.mass=np.sqrt(len(b.s)*len(b.a));self.reg=reg
        self.f0=b.fields(cf)
        ref=geom(self.f0)[:3] if target is None else target.values(b.s,b.a)
        self.ref=np.stack(ref,axis=-1);self.M=ortho(*ref)
        self.last=None
    def prep(self,c):
        if self.last is not None and np.array_equal(c,self.last):return
        self.last=c.copy();self.f=self.b.fields(c);self.geom.prepare(c)
        self.su,self.sg=support(self.b,self.f,self.p)
        self.slope=-self.p["support_weight"]*(self.su<self.p["support_goal"])
        if self.target is None:
            v=forms(self.f,self.x)
        else:
            v=np.stack(geom(self.f)[:3],axis=-1)-self.ref
        d=apply(self.M,v)
        # The smooth large-residual loss preserves the same zero tensor.
        tau=self.p["tensor_softness"]
        self.res=tau*np.arcsinh(d/tau);self.grad=1./np.sqrt(1+(d/tau)**2)
    def fun(self,c):
        self.prep(c)
        return np.r_[self.res.ravel()/self.mass,
            self.p["support_weight"]*np.maximum(self.p["support_goal"]-self.su,0.).ravel()/self.mass,
            self.geom.res[3:].ravel()/self.mass,self.reg*c]
    def jac(self,c):
        self.prep(c)
        b=self.b;f=self.f;_,u,v,*_=f;x=self.x
        oldj=self.geom.jac(c);n=self.res[...,0].size
        # forms is quadratic in the physical field, so its directional
        # derivative is the symmetric polarization without any perturbation size.
        def mv(z):
            z=z.ravel()
            df=[b.F.values(z,j,k) for j,k in PAIRS]
            _,du,dv,*_=df
            if self.target is None:
                a,ds,dt=x
                def dy(t):
                    _,i,j,k,l,m=t
                    return (row(a[...,0])*k+row(a[...,1])*l+row(ds[...,0])*i+row(ds[...,1])*j,
                            row(a[...,0])*l+row(a[...,1])*m+row(dt[...,0])*i+row(dt[...,1])*j)
                ys,yt=dy(f);dys,dyt=dy(df)
                gr=np.stack([2*(scalar(du,ys)+scalar(u,dys)),
                             scalar(dv,ys)+scalar(v,dys)+scalar(du,yt)+scalar(u,dyt),
                             2*(scalar(dv,yt)+scalar(v,dyt))],axis=-1)
            else:
                gr=np.stack([2*scalar(u,du),scalar(u,dv)+scalar(v,du),2*scalar(v,dv)],axis=-1)
            h=self.slope*sum(scalar(g,d) for g,d in zip(self.sg,df[:3]))
            return np.r_[(self.grad*apply(self.M,gr)).ravel()/self.mass,h.ravel()/self.mass,oldj.matvec(z)[3*n:]]
        def rm(z):
            z=z.ravel();g=pull(self.M,self.grad*z[:3*n].reshape(self.grad.shape)/self.mass)
            if self.target is None:
                val=shapeadj(f,x,g,b.F)
            else:
                val=b.F.adj(2*row(g[...,0])*u+row(g[...,1])*v,1,0)
                val+=b.F.adj(row(g[...,1])*u+2*row(g[...,2])*v,0,1)
            h=row(z[3*n:4*n].reshape(self.su.shape)*self.slope/self.mass)
            val+=sum(b.F.adj(h*a,j,k) for a,(j,k) in zip(self.sg,PAIRS[:3]))
            return val+oldj.rmatvec(np.r_[np.zeros(3*n),z[4*n:]])
        return LinearOperator((oldj.shape[0]+n,b.F.n),matvec=mv,rmatvec=rm,dtype=float)

def metrics(b,cf,cx,p,target=None):
    f=b.fields(cf);x=b.vect(cx)
    e,ff,g,n,area,K=geom(f);M=ortho(e,ff,g)
    k=normop(apply(M,forms(f,x)))
    su=support(b,f,p)[0]
    xi=old.Disk(dict(p["disk"],angle=b.d.gamma,height=b.d.height)).point(p["witness_x"],0.)
    xh=np.array([-xi[0],0.,xi[2]])@b.frame
    gap=np.linalg.norm(f[0]-xh,axis=-1)
    rec={"Killing_op_max":float(k.max()),"Killing_rms":float(np.sqrt(np.mean(k*k))),
       "clock_min_sample":float(x[0][...,1].min()),"area_min":float(area.min()),"support_min":float(su.min()),
       "max_abs_principal":float(K.max()),"origin_radius":float(np.linalg.norm(f[0],axis=-1).max()),
       "upper_height_min":float(f[0][...,2].min()),"opposite_witness_to_upper":float(gap.min()),
       "check_shape":list(k.shape)}
    if target is not None:
        ref=target.values(b.s,b.a);dv=apply(ortho(*ref),np.stack([e-ref[0],ff-ref[1],g-ref[2]],axis=-1))
        ev=normop(dv)
        rec.update(frozen_gram_max=float(ev.max()),frozen_gram_rms=float(np.sqrt(np.mean(ev**2))))
    return rec

def score(rec,p):
    return (np.log1p(rec["Killing_op_max"])+np.log1p(rec["Killing_rms"])+
         p["select_bending"]*np.log1p(max(0.,rec["max_abs_principal"]/p["curvature_price"]-1))+
         4*max(0.,p["support_goal"]-rec["support_min"])+3*max(0.,p["witness_ball"]-rec["opposite_witness_to_upper"])+
         2*max(0.,rec["origin_radius"]-p["body_radius"]))

def moments(b,cf,p):
    f=b.fields(cf)
    tt=b.a; a=np.linspace(0.,1.,p["moment_disk_radial"])
    dd=b.jet.disk_jet(a[:,None],tt[None,:],design=b.d,markers=False) if hasattr(b.jet,"disk_jet") else None
    if dd is None:
        d=old.Disk(dict(p["disk"],angle=b.d.gamma,height=b.d.height))
        xx=a[:,None]*np.cos(tt); yy=a[:,None]*np.sin(tt);ff=d.point(xx,yy)
        T=d.curve(xx)[1];ey=np.array([0.,1.,0.])
        du=row(np.cos(tt))*T+row(np.sin(tt))*ey
        dv=row(-yy)*T+row(xx)*ey
    else:
        ff,du,dv=dd[...,0,:],dd[...,1,:],dd[...,2,:]
    def sumhalf(s,p0,ds,da):
        pt=p0@b.frame.T;nu=np.cross(ds,da)@b.frame.T
        r=p0.copy();r[...,2]*=-1
        n=np.cross(ds,da);n[...,2]*=-1
        pt2=r@b.frame.T;nu2=n@b.frame.T
        d1=scalar(pt,nu);d2=scalar(pt2,nu2)
        v=DT*np.trapezoid(np.mean(d1+d2,axis=1),s)/3
        c=DT*np.trapezoid(np.mean(pt[...,0]*d1+pt2[...,0]*d2,axis=1),s)/4
        return np.array([v,c])
    vol,cx=sumhalf(b.s,*f[:3])+sumhalf(a,ff@b.frame,du@b.frame,dv@b.frame)
    B=sum(np.pi*h*r*r*x/5. for x,y,r,h in p["markers"])
    vm=sum(np.pi*h*r*r/5. for x,y,r,h in p["markers"])
    return {"signed_unmarked_volume":float(vol),"signed_unmarked_first_moment_x":float(cx),
            "fixed_marker_first_moment_x":float(B),"marked_central_second_moment_pi_difference":float(4*cx*B/(vol+vm))}

def cloud(b,cf,p):
    a=b.a;disk=old.Disk(dict(p["disk"],angle=b.d.gamma,height=b.d.height));d=p["cloud_nr"]
    rr=np.linspace(0.,1.,d)[1:,None]
    xx=np.r_[0.,(rr*np.cos(a)).ravel()];yy=np.r_[0.,(rr*np.sin(a)).ravel()]
    f=disk.point(xx,yy)@b.frame;be=disk.angles(xx)[0]
    no=np.stack([-np.sin(be),np.zeros_like(be),np.cos(be)],axis=-1)@b.frame
    fj=b.fields(cf);nu=geom(fj)[3];nring=len(a)
    up=np.vstack([f,fj[0][1:].reshape(-1,3)]);upn=np.vstack([no,nu[1:].reshape(-1,3)])
    lo=up[:-nring].copy();lo[:,2]*=-1
    lon=upn[:-nring].copy();lon[:,2]*=-1
    body=np.vstack([up,lo])@b.frame.T;normal=np.vstack([upn,lon])@b.frame.T
    edge=disk.point(p["witness_x"],0.)
    markers=[]
    for cx,cy,r,h in p["markers"]:
        radii=np.linspace(0.,r,5)[:,None]
        aa=np.arange(12)*DT/12
        x=(cx+radii*np.cos(aa)).ravel();y=(cy+radii*np.sin(aa)).ravel()
        markers.append(np.stack([x,y,np.full_like(x,disk.H)],axis=-1))
    extra=np.vstack(markers); vals=[]; rows=[]
    for ph in [0.,np.pi/2,np.pi]:
        co,si=np.cos(ph),np.sin(ph);rot=np.array([[co,si,0],[-si,co,0],[0,0,1.]])
        pts=np.vstack([body@rot,extra]);norm=np.vstack([normal@rot,np.tile([0.,0.,1.],(len(extra),1))])
        ids=np.r_[np.arange(len(f)),np.arange(len(body),len(pts))]
        for cx,cy,r,h in p["markers"]:
            dx=pts[ids,0]-cx;dy=pts[ids,1]-cy;z=1-(dx*dx+dy*dy)/r**2
            active=z>0.;ii=ids[active];z=z[active]
            pts[ii,2]+=h*z**4
            nn=np.stack([8*h*dx[active]*z**3/r**2,8*h*dy[active]*z**3/r**2,np.ones_like(z)],axis=-1)
            norm[ii]=nn/row(np.linalg.norm(nn,axis=-1))
        tree=cKDTree(pts);vals.append((pts,tree));first,t0=vals[0]
        dmax=0.;chord=0.
        for start in range(0,len(pts),80):
            sl=slice(start,start+80)
            dv=pts[None,:,:]-pts[sl,None,:];d2=scalar(dv,dv)
            dmax=max(dmax,float(d2.max()))
            top=2*abs(np.einsum("bij,bj->bi",dv,norm[sl]))
            chord=max(chord,float(np.max(top/np.where(d2>1e-20,d2,np.inf))))
        rows.append(dict(phase=ph,point_count=len(pts),diameter=float(np.sqrt(dmax)),
                         held=float(max(tree.query(first)[0].max(),t0.query(pts)[0].max())),
                         center_witness=float(tree.query(edge)[0]),ordered_inverse_ball=chord))
    return rows

def main():
    ap=argparse.ArgumentParser()
    for key in ["params","jet-source","out"]:ap.add_argument("--"+key,required=True)
    args=ap.parse_args()
    p=json.loads(Path(args.params).read_text());out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    jp=Path(args.jet_source).resolve();sys.path.insert(0,str(jp.parent));jet=importlib.import_module(jp.stem)
    def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
    modules=[old,arc,kf,kt,jet,jet.base]
    hashes={Path(m.__file__).name:sha(m.__file__) for m in modules}
    for name,h in p["fixed_source_hashes"].items():
        if hashes[name]!=h:raise ValueError("scientific source bytes differ: "+name)
    start=time.monotonic()
    meta={"schema":"finite-disk-killing-haar/v1","science_sha256":sha(__file__),"params_sha256":sha(args.params),
        "sources":hashes,"numpy":np.__version__,"scipy":scipy.__version__,"stages":[],
        "scope":"Actual full-circle shape and material field solve. Haar cache, independent integration, principal curvatures, ordered chord and volume moments are numerical. Exact symmetry, same-g path, reach and geometry certificates require continuum estimates."}
    def save():
        meta["elapsed_seconds"]=time.monotonic()-start;old.put_json(out/"summary.json",meta)
    def design(spec):
        if spec["id"]=="native":
            d=SimpleNamespace(gamma=.38,height=.37,length=1.02,join=.5)
            return Native(p["disk"],d),d,0.
        d=jet.Design(**spec["parameters"])
        return (kf.Handles(jet,spec["right_handle"]) if "right_handle" in spec else jet),d,spec["extra"]
    def grid(spec,cfg,check=False,custom=None):
        j,d,extra=design(spec);edges=kf.span_edges(d,j.base,extra)
        rr=cfg["check_radial" if check else "radial"];n=cfg["check_angular" if check else "angular"]
        s=kf.radial_nodes(edges,rr);a=DT*(np.arange(n)+(.217 if check else 0.))/n
        if custom is not None:s,a=custom
        return kf.Field(j,d,extra,cfg["spans"],cfg["mode"],s,a)
    def record(kind,spec,cfg,b,cf,cx,other=None,target=None):
        i=len(meta["stages"])
        fname=out/("stage-%02d.npz"%i);np.savez(fname,shape_coefficients=cf,field_coefficients=cx)
        ck=grid(spec,cfg,True)
        rr=metrics(ck,cf,cx,p,target)
        q={"stage":i,"kind":kind,"design":spec,"configuration":cfg,"shape_count":len(cf),"field_count":len(cx),
           "shape_sha256":old.array_digest(cf),"field_sha256":old.array_digest(cx),"point_sha256":old.array_digest(np.r_[cf,cx]),
           "npz_bytes":fname.stat().st_size,"npz_sha256":sha(fname),"train":metrics(b,cf,cx,p,target),"check":rr,
           "score":float(score(rr,p))}
        if other:q.update(other)
        meta["stages"].append(q);meta.pop("in_progress",None);save()
        print(json.dumps({"event":"stage","stage":i,"kind":kind,"design":spec["id"],
             "relative_Killing":rr["Killing_op_max"],"frozen_gram":rr.get("frozen_gram_max"),
             "curvature":rr["max_abs_principal"],"support":rr["support_min"]}),flush=True)
        return q
    def physically_solve(b,cf,cx,cfg,target,tag):
        obj=Shape(b,p,cf,cx,cfg["regularizer"],target)
        z=np.cos(.291*np.arange(b.F.n)+.1);z/=np.linalg.norm(z)
        f0=obj.fun(cf);jac=obj.jac(cf);jz=jac.matvec(z);w=np.sin(.738*np.arange(len(f0))+.5);w/=np.linalg.norm(w)
        adj=abs(float(w@jz-z@jac.rmatvec(w)));h=p["jacobian_probe"]
        fd=np.linalg.norm((obj.fun(cf+h*z)-obj.fun(cf-h*z))/(2*h)-jz)/max(np.linalg.norm(jz),1e-15)
        best=[np.inf,0.,0]
        def fun(x):
            ff=obj.fun(x);v=float(ff@ff/2);best[2]+=1
            if v<best[0]:
                best[0]=v
                if time.monotonic()-best[1]>20.:
                    best[1]=time.monotonic()
                    meta["in_progress"]={"stage":len(meta["stages"]),"kind":tag,"call":best[2],"cost":v,
                                         "shape_sha256":old.array_digest(x)}
                    with open(out/"current.tmp","wb") as handle:np.savez(handle,shape_coefficients=x,field_coefficients=cx)
                    os.replace(out/"current.tmp",out/"current.npz");save()
            return ff
        scale=b.F.scale(.02)
        sol=least_squares(fun,cf,jac=obj.jac,method="trf",tr_solver="lsmr",x_scale=scale,
            max_nfev=cfg["max_feval"],ftol=1e-10,xtol=1e-10,gtol=1e-10,
            tr_options={"maxiter":cfg["lsmr"],"atol":3e-7,"btol":3e-7})
        return sol.x,{"solver_status":int(sol.status),"nfev":int(sol.nfev),"njev":int(sol.njev or 0),
                 "cost":float(sol.cost),"optimality":float(sol.optimality),"directional_fd_relative":float(fd),"adjoint_abs":adj}
    save()
    try:
        results=[]
        cfg=p["field_stage"]
        for spec in p["designs"]:
            b=grid(spec,cfg);cf=np.zeros(b.F.n);c0=np.zeros(b.X.n)
            raw=metrics(grid(spec,cfg,True),cf,c0,p)
            cx,ls=kf.fixed_x(b,cf,p["field_regularizer"],cfg["field_iterations"])
            cx,a,lower=kf.positive_field(b,cx,p["clock_margin"])
            q=record("fixed_actual_shape_killing",spec,cfg,b,cf,cx,
                 dict(raw_polar_field=raw,linear_solve=ls,field_rescale=float(a),angular_speed_control_lower=float(lower)))
            results.append((q["score"],spec,b,cf,cx,q))
        bank=[]
        for _,spec,b,cf,cx,r in sorted(results,key=lambda x:x[0])[:p["continue_count"]]:
            for cfg in p["coupled"]:
                b0=b;b=grid(spec,cfg);cf=transfer(b0.F,cf,b.F);cx=transfer(b0.X,cx,b.X)
                cf,other=physically_solve(b,cf,cx,cfg,None,"physical_Killing")
                cx,ls=kf.fixed_x(b,cf,p["field_regularizer"],cfg["field_iterations"])
                cx,scale,lower=kf.positive_field(b,cx,p["clock_margin"])
                other.update(linear_solve=ls,field_rescale=float(scale),angular_speed_control_lower=float(lower))
                r=record("alternate_shape_and_material",spec,cfg,b,cf,cx,other)
            bank.append((r["score"],spec,b,cf,cx,r))
        _,spec,b,cf,cx,r=min(bank,key=lambda z:z[0])
        fcfg=r["configuration"];meta["selected_source_stage"]=r["stage"];save()
        inherited=cx.copy()
        attempts=[]
        for factor in p["orbit_radial_scales"]:
            cx=inherited.copy();cx[b.X.sl[0]]*=factor
            try:
                fixed=kt.Target(b,cf,cx,**p["haar_cache"],margin=p["clock_margin"])
                independent=kt.Target(b,cf,cx,**p["haar_independent"],margin=p["clock_margin"])
                attempts.append({"radial_scale":factor,"status":"complete"})
                break
            except (ValueError,FloatingPointError) as err:
                attempts.append({"radial_scale":factor,"status":"unresolved","reason":str(err)[:180]})
        else:
            raise ValueError("all full-circle orbit integrations failed: "+str(attempts))
        input_field_sha=old.array_digest(cx)
        cx=fixed.cx.copy()
        frozen_field_sha=old.array_digest(cx)
        independent_field_sha=old.array_digest(independent.cx)
        np.savez(out/"frozen-source.npz",shape_coefficients=cf,field_coefficients=cx)
        meta["orbit_integration_attempts"]=attempts
        meta["frozen_source_npz_sha256"]=sha(out/"frozen-source.npz")
        # Compare the two integrations on a grid independent of their caches.
        ss=kf.radial_nodes(b.edges,p["haar_compare_radial"]);aa=DT*(np.arange(194)+.321)/194
        v0=fixed.values(ss,aa);v1=independent.values(ss,aa)
        dv=normop(apply(ortho(*v1),np.stack(v0,axis=-1)-np.stack(v1,axis=-1)))
        meta["frozen_target"]={"definition":"R741 (12)-(13) of the selected source shape and normalized material vector field, unchanged through both fixed steps. One cached rounded evaluator and one independent denser quadrature are retained.",
             "source_shape_sha256":old.array_digest(cf),"source_field_sha256":frozen_field_sha,
             "source_field_before_cache_rescale_sha256":input_field_sha,"independent_source_field_sha256":independent_field_sha,
             "identical_frozen_preperiod_vector":frozen_field_sha==independent_field_sha,
             "action":"Both fixed stages use the circle action of this same original shape basis and recorded preperiod vector. A transferred stage vector is used only for reporting the material Killing residual.",
             "cache_table_sha256":old.array_digest(fixed.table),"denser_table_sha256":old.array_digest(independent.table),
             "cache":fixed.report,"independent":independent.report,"relative_cache_discrepancy_max":float(dv.max()),
             "relative_cache_discrepancy_rms":float(np.sqrt(np.mean(dv*dv)))}
        save();keep=[(b,cf,cx,r)]
        for cfg in p["fixed_refinements"]:
            b0=b;b=grid(spec,cfg);cf=transfer(b0.F,cf,b.F);cx=transfer(b0.X,cx,b.X)
            cf,other=physically_solve(b,cf,cx,cfg,fixed,"frozen_Haar")
            ck=grid(spec,cfg,True)
            other["frozen_action_source_field_sha256"]=frozen_field_sha
            other["transferred_diagnostic_field_sha256"]=old.array_digest(cx)
            other["independent_same_target"]=metrics(ck,cf,cx,p,independent)
            r=record("same_frozen_Haar_shape",spec,cfg,b,cf,cx,other,fixed)
            keep.append((b,cf,cx,r))
        for b,cf,cx,r in keep:
            cfg=r["configuration"]
            ss=kf.radial_nodes(b.edges,p["moment_radial"]);aa=DT*np.arange(p["moment_angular"])/p["moment_angular"]
            r["volume_moments"]=moments(grid(spec,cfg,custom=(ss,aa)),cf,p)
            ss=kf.radial_nodes(b.edges,p["cloud_shoulder"]);aa=DT*np.arange(p["cloud_angular"])/p["cloud_angular"]
            r["sampled_entire_phases"]=cloud(grid(spec,cfg,custom=(ss,aa)),cf,p)
            save()
        meta["status"]="completed_full_finite_Killing_Haar_and_two_fixed_refinements";save()
    except Exception as exc:
        meta["status"]="runtime_failure";meta["exception"]=type(exc).__name__+": "+str(exc)[:1600];save()
        traceback.print_exc();return 1
    return 0

if __name__=="__main__":
    raise SystemExit(main())
