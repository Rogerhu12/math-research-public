#!/usr/bin/env python3
"""Angle-arclength design of a strong bent disk and one reflected shoulder."""
import argparse
import json
import os
import time
import traceback
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import least_squares
from scipy.sparse.linalg import LinearOperator

import bent_disk_shoulder as old


class Native(old.Shoulder):
    """Use the actual curved disk away from its rim, with bounded added radius."""
    def __init__(self,disk,length,equator,spans,mode,t,theta,pad=.15):
        super().__init__(disk,length,equator,spans,mode,t,theta)
        s=(self.t*length)[:,None]
        v=np.tanh(s/pad)
        r=1.+pad*v
        rs=1.-v*v
        rss=-2.*v*rs/pad
        c=np.cos(self.theta)[None,:]
        y=np.sin(self.theta)[None,:]
        x=r*c
        ey=np.array([0.,1.,0.])
        ez=np.array([0.,0.,1.])
        p,p1,p2,_,_=disk.curve(x)
        def v3(x):
            return x[...,None]
        clock=v3(rs)
        ray=v3(c)*p1+v3(y)*ey
        d00=p+v3(r*y)*ey+disk.H*ez
        d10=clock*ray
        d20=v3(rs*rs*c*c)*p2+v3(rss)*ray
        d01=v3(-r*y)*p1+v3(r*c)*ey
        d02=v3((r*y)**2)*p2-v3(r*c)*p1-v3(r*y)*ey
        d11=clock*(v3(-r*y*c)*p2-v3(y)*p1+v3(c)*ey)
        diskjets={(0,0):d00,(1,0):d10,(2,0):d20,(0,1):d01,(0,2):d02,(1,1):d11}
        h0=[1.,0.,0.,-10.,15.,-6.]
        h1=[0.,0.,0.,-4.,7.,-3.]
        chi=[old.polynomial(h0,self.t,j)[:,None,None]/length**j for j in range(3)]
        end=[old.polynomial(h1,self.t,j)[:,None,None]*length**(1-j) for j in range(3)]
        for j,k in self.base:
            E=np.stack([equator*np.cos(self.theta+k*np.pi/2),
                        equator*np.sin(self.theta+k*np.pi/2),np.zeros_like(self.theta)],axis=-1)
            D=diskjets[0,k] @ disk.frame
            if j==0:
                q=chi[0]*(D-E)+E
            elif j==1:
                q=chi[1]*(D-E)+chi[0]*(diskjets[1,k] @ disk.frame)
            else:
                q=chi[2]*(D-E)+2*chi[1]*(diskjets[1,k] @ disk.frame)+chi[0]*(diskjets[2,k] @ disk.frame)
            self.base[j,k]=q if k else q-end[j]*ez


def grid(cls,disk,design,stage,verify=False):
    nr=stage["check_radial" if verify else "radial"]
    na=stage["check_angular" if verify else "angular"]
    t=(1.-np.cos(np.pi*np.arange(nr)/(nr-1)))/2.
    return cls(disk,design["length"],design["equator_radius"],stage["spans"],stage["mode"],
               t,old.angular_grid(na,.173 if verify else 0.))


def same_grid(cls,b,t,a):
    return cls(b.disk,b.L,b.eq,b.spans,b.mode,t,a)


def project(b,source):
    if source is None:
        return np.zeros(b.n)
    src,x=source
    a=old.angular_grid(max(6*max(b.mode,src.mode)+8,112))
    t=np.linspace(0.,1.,max(8*max(b.spans,src.spans)+17,81))
    A=same_grid(type(src),src,t,a)
    B=same_grid(type(b),b,t,a)
    # Preserve the source physical geometry when its equator plane or grip
    # height changes only up to the exact, newly imposed boundary jets.
    goal=(A.field(x,0,0) @ src.disk.frame.T) @ b.disk.frame
    d=goal-B.base[0,0]
    result=np.empty(b.n)
    for k,sl in enumerate(b.slices):
        c1=np.linalg.lstsq(B.bs[k][0],d[...,k],rcond=1.e-13)[0]
        result[sl]=np.linalg.lstsq(B.ph[k][0],c1.T,rcond=1.e-13)[0].T.ravel()
    return result


def avg(a):
    return np.mean(a,axis=1,keepdims=True)


def primitive(a):
    """Mean-zero periodic primitive on a uniform full circle (odd result for even input)."""
    w=np.fft.rfft(a,axis=1)
    z=np.zeros(w.shape[1],dtype=complex)
    z[1:]=1./(1j*np.arange(1,len(z)))
    if a.shape[1]%2==0:
        z[-1]=0.
    return np.fft.irfft(w*z[None,:],n=a.shape[1],axis=1)


def gauge(b,x):
    u,v,m=[b.field(x,*jk) for jk in ((1,0),(0,1),(1,1))]
    w0=np.linalg.norm(v,axis=-1)
    w=np.maximum(w0,1.e-10)
    T=v/w[...,None]
    q=old.dot(u,T)
    V=u-q[...,None]*T
    ws=old.dot(T,m)
    P=avg(w)
    H=avg(ws)/P
    B=q-primitive(ws-w*H)
    E=old.dot(V,V)
    return u,v,m,w,T,q,V,ws,P,H,B,E


class Fixed:
    def __init__(self,b,x,count):
        self.b,self.x,self.count=b,x.copy(),count
        self.memo={}
    def values(self,t):
        key=np.ascontiguousarray(t,dtype="<f8").tobytes()
        if key not in self.memo:
            k=same_grid(type(self.b),self.b,np.asarray(t),old.angular_grid(self.count))
            *_,P,H,B,E=gauge(k,self.x)
            self.memo[key]=(avg(E),P)
        return self.memo[key]


def diagnostics(b,x,target):
    *_,P,H,B,E=gauge(b,x)
    Ee,Pt=(avg(E),P) if target is None else target.values(b.t)
    if np.any(Ee<=0.) or np.any(Pt<=0.):
        raise ValueError("nonpositive actual angular-gauge metric")
    a=(E+B*B)/Ee
    f=P*B/(Pt*np.sqrt(Ee))
    g=(P/Pt)**2
    h=.5*(a+g)
    r=np.sqrt((.5*(a-g))**2+f*f)
    error=np.maximum(np.abs(h+r-1.),np.abs(h-r-1.))
    old_metric,pos,n=old.field_metrics(b,x,None)
    out={"gauged_max_relative":float(error.max()),"gauged_rms":float(np.sqrt(np.mean(error**2))),
         "normal_speed_angular_scatter_max":float(np.max(np.abs(E-avg(E)))),
         "arclength_cross_speed_max":float(np.max(np.abs(B))),
         "p0_relative_max":float(np.max(np.abs(g-1.))),
         "min_projected_speed_squared":float(E.min()),"min_angular_speed":float(np.linalg.norm(b.field(x,0,1),axis=2).min()),
         "original_coordinate_gram_max":old_metric["gram_max"],"K_sample_max":old_metric["shoulder_K_abs_sample_max"],
         "origin_radius_sample_max":old_metric["origin_radius_sample_max"],"min_signed_equator_height":float(pos[...,2].min())}
    return out,pos,n


class Objective:
    def __init__(self,b,p,stage,target):
        self.b,self.p,self.stage,self.target=b,p,stage,target
        self.reg=stage["regularizer"]
        self.old=old.Objective(b,p,self.reg,None)
        self.mass=np.sqrt(len(b.t)*len(b.theta))
        self.start=None
        self.count=0
        self.center=np.array([p["support_center_world_x"]/np.cos(b.disk.angle),0.,0.])

    def prep(self,x):
        if self.start is not None and np.array_equal(x,self.start):
            return
        self.start=x.copy();self.count+=1
        self.old.prepare(x)
        self.u,self.v,self.uv,self.w,self.T,self.q,self.V,self.ws,self.P,self.H,self.B,self.E=gauge(self.b,x)
        self.A,self.pt=(np.maximum(avg(self.E),1.e-10),self.P) if self.target is None else self.target.values(self.b.t)
        f=self.b.field(x,0,0)
        q=f-self.center
        cr=np.cross(self.u,self.v)
        area=np.maximum(np.linalg.norm(cr,axis=2),1.e-10)
        n=cr/area[...,None]
        sop=old.dot(q,n)
        h=(q-sop[...,None]*n)/area[...,None]
        self.support=sop
        self.sgrads=(n,np.cross(self.v,h),np.cross(h,self.u))
        e=self.E; a=self.A; p=self.p
        self.rows=np.zeros((5,)+e.shape)
        self.rows[0]=e/a-1.
        self.rows[1]=self.B/np.sqrt(a)
        if self.target is not None:
            self.rows[2]=self.P/self.pt-1.
        self.eslope=-p["speed_weight"]*(e<p["normal_speed_floor"])
        self.sslope=-p["support_weight"]*(sop<p["support_goal"])
        self.rows[3]=p["speed_weight"]*np.maximum(p["normal_speed_floor"]-e,0.)
        self.rows[4]=p["support_weight"]*np.maximum(p["support_goal"]-sop,0.)

    def fun(self,x):
        self.prep(x)
        value=np.r_[self.rows.ravel()/self.mass,self.old.res[3:].ravel()/self.mass,self.reg*x]
        if self.count%15==1:
            print(json.dumps({"event":"arc_objective","call":self.count,"norm":float(np.linalg.norm(value)),
                              "angle_residual":float(np.max(np.abs(self.rows[:3])))}),flush=True)
        return value

    def jac(self,x):
        self.prep(x)
        b=self.b
        oldj=self.old.jac(x)
        no=np.prod(self.old.shape[1:])
        old_size=int(np.prod(self.old.shape))
        n0=self.rows.size
        rows_shape=self.rows.shape
        norm=self.mass
        u,v,m,w,T,q,V,ws,P,H,B,E=self.u,self.v,self.uv,self.w,self.T,self.q,self.V,self.ws,self.P,self.H,self.B,self.E
        a,pt,es,ss,sg=self.A,self.pt,self.eslope,self.sslope,self.sgrads
        design=self.target is None
        def mv(z):
            z=z.ravel()
            df,du,dv,dm=[b.delta(z,*jk) for jk in ((0,0),(1,0),(0,1),(1,1))]
            dw=old.dot(T,dv)
            dT=(dv-dw[...,None]*T)/w[...,None]
            dq=old.dot(du,T)+old.dot(u,dT)
            de=2*old.dot(u,du)-2*q*dq
            dws=old.dot(dT,m)+old.dot(T,dm)
            dh=dws-H*dw-w*(avg(dws)-H*avg(dw))/P
            db=dq-primitive(dh)
            da=avg(de) if design else 0.
            rr=np.zeros(rows_shape)
            rr[0]=(de-(E/a)*da)/a
            rr[1]=db/np.sqrt(a)-.5*B*da/(a**1.5)
            if not design:
                rr[2]=avg(dw)/pt
            rr[3]=es*de
            rr[4]=ss*(old.dot(sg[0],df)+old.dot(sg[1],du)+old.dot(sg[2],dv))
            return np.r_[rr.ravel()/norm,oldj.matvec(z)[3*no:]]
        def rmv(z):
            z=z.ravel()
            zz=z[:n0].reshape(rows_shape)/norm
            ge=zz[0]/a+es*zz[3]
            gb=zz[1]/np.sqrt(a)
            if design:
                ge+=avg(-zz[0]*E/a**2-.5*zz[1]*B/a**1.5)
            gq=gb-2*q*ge
            gh=primitive(gb)
            gs=gh-avg(gh*w)/P
            gw=-H*gs
            if not design:
                gw+=avg(zz[2])/pt
            gt=gq[...,None]*u+gs[...,None]*m
            gu=2*ge[...,None]*u+gq[...,None]*T
            gv=gw[...,None]*T+(gt-old.dot(gt,T)[...,None]*T)/w[...,None]
            gm=gs[...,None]*T
            gp=(ss*zz[4])[...,None]
            result=b.adjoint(gp*sg[0],0,0)+b.adjoint(gu+gp*sg[1],1,0)
            result+=b.adjoint(gv+gp*sg[2],0,1)+b.adjoint(gm,1,1)
            return result+oldj.rmatvec(np.r_[np.zeros(3*no),z[n0:]])
        return LinearOperator((n0+old_size-3*no+b.n,b.n),matvec=mv,rmatvec=rmv,dtype=float)


def ellipse_start(b,ell):
    a=old.angular_grid(max(144,6*b.mode))
    t=np.linspace(0.,1.,max(121,9*b.spans))
    k=same_grid(type(b),b,t,a)
    s=t[:,None]*ell.ELL_SHOULDER_LENGTH
    data=ell.ellipse_shoulder(s,a[None,:],32)
    data[...,2]+=b.disk.H-ell.H
    d=data @ b.disk.frame-k.base[0,0]
    out=np.empty(b.n)
    for i,sl in enumerate(k.slices):
        a1=np.linalg.lstsq(k.bs[i][0],d[...,i],rcond=1.e-13)[0]
        out[sl]=np.linalg.lstsq(k.ph[i][0],a1.T,rcond=1.e-13)[0].T.ravel()
    return out


def phase_values(b,x,p):
    # The existing cloud/phase routine evaluates the original base explicitly.
    # Rebuild only its shoulder section with the correct non-polynomial base.
    nr,na=p["cloud_radial"],p["cloud_angular"]
    raw,norm,ndisk,extra=old.cloud(b,x,nr,na,p)
    a=old.angular_grid(na)
    k=same_grid(type(b),b,np.linspace(0.,1.,nr)[1:],a)
    f=k.field(x,0,0)
    nn=np.cross(k.field(x,1,0),k.field(x,0,1))
    nn/=np.maximum(np.linalg.norm(nn,axis=-1,keepdims=True),1.e-15)
    n=(nr-1)*na
    raw[ndisk:ndisk+n]=f.reshape(-1,3) @ b.disk.frame.T
    norm[ndisk:ndisk+n]=nn.reshape(-1,3) @ b.disk.frame.T
    for field,surface in ((raw,f),(norm,nn)):
        rev=surface[:-1].reshape(-1,3).copy()
        rev[:,2]*=-1.
        field[2*ndisk+n:]=rev @ b.disk.frame.T
    groups=[]; trees=[]; half=old.cKDTree
    witness=b.disk.point(p["witness_x"],0.)
    for ph in p["phases"]:
        c,s=np.cos(ph),np.sin(ph)
        rot=np.array([[c,s,0.],[-s,c,0.],[0.,0.,1.]])
        pts=np.vstack([raw@rot,extra.copy()]); ns=np.vstack([norm@rot,np.tile([0.,0.,1.],(len(extra),1))])
        idx=np.r_[np.arange(ndisk),np.arange(len(raw),len(pts))]
        for cx,cy,br,height in p["markers"]:
            dx,dy=pts[idx,0]-cx,pts[idx,1]-cy
            z=1.-(dx**2+dy**2)/br**2
            pick=z>0.; ii=idx[pick];z=z[pick]
            pts[ii,2]+=height*z**4
            ns[ii]=np.stack([8*height*dx[pick]*z**3/br**2,8*height*dy[pick]*z**3/br**2,np.ones_like(z)],axis=-1)
            ns[ii]/=np.linalg.norm(ns[ii],axis=-1,keepdims=True)
        groups.append((pts,ns));trees.append(half(pts))
    result=[]
    for i,(pts,ns) in enumerate(groups):
        d2max=0.;inv=0.
        for start in range(0,len(pts),96):
            sl=slice(start,start+96)
            d=pts[None,:,:]-pts[sl,None,:]
            d2=old.dot(d,d)
            d2max=max(d2max,float(d2.max()))
            pn=np.abs(np.einsum("bij,bj->bi",d,ns[sl]))
            inv=max(inv,float(np.max(2*pn/np.where(d2>1.e-20,d2,np.inf))))
        result.append({"phase":p["phases"][i],"sample_diameter":float(np.sqrt(d2max)),
                       "sample_Hausdorff":float(max(trees[0].query(pts)[0].max(),trees[i].query(groups[0][0])[0].max())),
                       "sample_chord_inverse_reach_max":inv,"sample_witness_distance":float(trees[i].query(witness)[0]),
                       "point_count":len(pts)})
    return result


def main():
    import importlib.util
    ap=argparse.ArgumentParser()
    for key in ("params","parent-params","parent-dir","ellipse-source","out"):
        ap.add_argument("--"+key,required=True)
    args=ap.parse_args()
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    parent=Path(args.parent_dir)
    pp=json.loads(Path(args.parent_params).read_text())
    p=json.loads(Path(args.params).read_text())
    def sh(path):
        return old.digest_bytes(Path(path).read_bytes())
    if sh(args.parent_params)!=p["parent_params_sha256"] or sh(old.__file__)!=p["parent_source_sha256"] or sh(args.ellipse_source)!=p["ellipse_source_sha256"]:
        raise ValueError("actual source/scientific input identity mismatch")
    spec=importlib.util.spec_from_file_location("r740_scientific_seed",args.ellipse_source)
    ell=importlib.util.module_from_spec(spec);spec.loader.exec_module(ell)
    parent_summary=json.loads((parent/"summary.json").read_text())
    summary={"schema":"bent-disk-canonical-angle/v1","source_sha256":sh(__file__),"params_sha256":sh(args.params),
             "parent_source_sha256":sh(old.__file__),"parent_summary_sha256":sh(parent/"summary.json"),
             "ellipse_source_sha256":sh(args.ellipse_source),"numpy":np.__version__,"scipy":scipy.__version__,
             "parent_reads":[],"stages":[],"scope":"Approximate full-shoulder solutions. Canonical angle primitive uses sampled Fourier integration. Only the exact central disk and algebraic reflection framework are prescribed; no continuum embedding, reach, exact solution, or refinement convergence is presumed."}
    begin=time.monotonic()
    def save():
        summary["elapsed_seconds"]=time.monotonic()-begin
        old.put_json(out/"summary.json",summary)
    def diskof(d):
        opts=dict(pp["disk"]);opts.update(height=d["height"],angle=d["angle"])
        return old.Disk(opts)
    save()
    parents={}
    try:
        if sh(parent/"summary.json")!=p["parent_summary_sha256"]:
            raise ValueError("not the complete original 36 summary")
        for entry in p["parent_stages"]:
            i=entry["stage"];r=parent_summary["stages"][i]
            filename=parent/("stage-%02d.npz"%i)
            if sh(filename)!=entry["npz_sha256"]:
                raise ValueError("wrong complete parent stage container")
            with np.load(filename,allow_pickle=False) as data:
                x=data["coefficients"].copy()
            if old.array_digest(x)!=entry["x_sha256"] or old.array_digest(x)!=r["x_sha256"]:
                raise ValueError("wrong actual parent coefficients")
            d=r["design"];stage=r["configuration"]
            ba=grid(old.Shoulder,diskof(d),d,stage)
            chk=grid(old.Shoulder,ba.disk,d,p["parent_check"]|{"spans":ba.spans,"mode":ba.mode},True)
            if len(x)!=ba.n:
                raise ValueError("parent stage dimension mismatch")
            met,_,_=diagnostics(chk,x,None)
            summary["parent_reads"].append({"stage":i,"npz_sha256":sh(filename),"x_sha256":old.array_digest(x),
                        "same_geometric_image_gauged_measure":met})
            parents[i]=(ba,x)
        save()
        def solve(d,stage,src=None,target=None):
            b=grid(Native,diskof(d),d,stage)
            if src is None and d["seed"]=="ellipse":
                x0=ellipse_start(b,ell)
            else:
                x0=project(b,src)
            obj=Objective(b,p,stage,target)
            t0=time.monotonic();vv=np.cos(.947*np.arange(b.n)+.05);vv/=np.linalg.norm(vv)
            f0=obj.fun(x0);jj=obj.jac(x0);jv=jj.matvec(vv)
            ww=np.sin(.243*np.arange(len(f0))+.38);ww/=np.linalg.norm(ww)
            adj=abs(float(jv@ww-vv@jj.rmatvec(ww)))
            h=p["jacobian_probe"]
            diff=(obj.fun(x0+h*vv)-obj.fun(x0-h*vv))/(2*h)
            fd=float(np.linalg.norm(diff-jv)/max(np.linalg.norm(jv),1.e-20))
            scale=np.empty(b.n)
            for i,sl in enumerate(b.slices):
                m=np.arange(1 if i==1 else 0,b.mode+1)
                r0=np.mean(b.bs[i][0]**2,axis=0)[:,None]
                r1=np.mean((b.bs[i][1]/b.L)**2,axis=0)[:,None]
                r2=np.mean((b.bs[i][2]/b.L**2)**2,axis=0)[:,None]
                hess=(p["bending_weight"]/p["curvature_price"])**2
                scale[sl]=1./np.sqrt(np.maximum(1.e-6,r1+r0*m**2+hess*(r2+2*r1*m*m+r0*m**4))).ravel()
            state=[float("inf"),0.,0]
            def fun(z):
                f=obj.fun(z);value=float(.5*(f@f));state[2]+=1
                if value<state[0]:
                    state[0]=value
                    if time.monotonic()-state[1]>15. or state[2]==1:
                        state[1]=time.monotonic()
                        with open(out/"current-field.tmp","wb") as fhandle:
                            np.savez(fhandle,coefficients=z)
                        os.replace(out/"current-field.tmp",out/"current-field.npz")
                        summary["in_progress"]={"stage":len(summary["stages"]),"design":d["id"],"layer":stage["id"],
                           "call":state[2],"cost":value,"x_sha256":old.array_digest(z)}
                        save()
                return f
            result=least_squares(fun,x0,jac=obj.jac,method="trf",tr_solver="lsmr",x_scale=scale,
                         tr_options={"maxiter":stage["lsmr_iterations"],"atol":1.e-7,"btol":1.e-7},
                         max_nfev=stage["max_evaluations"],ftol=1.e-10,xtol=1.e-10,gtol=1.e-10)
            x=result.x
            chk=grid(Native,b.disk,d,stage,True)
            met,f,n=diagnostics(chk,x,target)
            train,_,_=diagnostics(b,x,target)
            c=np.array([p["support_center_world_x"]/np.cos(b.disk.angle),0.,0.])
            sup=float(old.dot(f-c,n).min())
            pt=b.disk.point(p["witness_x"],0.);cmp=np.array([-pt[0],0.,pt[2]]) @ b.disk.frame
            gap=float(np.linalg.norm(f-cmp,axis=-1).min())
            score=met["gauged_max_relative"]+.28*max(0.,met["K_sample_max"]/p["curvature_price"]-1.)+\
                  3*max(0.,p["support_goal"]-sup)+2*max(0.,p["witness_ball"]-gap)+\
                  2*max(0.,met["origin_radius_sample_max"]-p["body_radius"])
            # Analytic whole bent disk support including the fixed p4 markers.
            # Shoulder sampled support/curvature are separate from these formulas.
            cx=p["support_center_world_x"];cz=cx*np.tan(b.disk.angle)
            slope=max(8*hh/br for _,_,br,hh in p["markers"])
            mr=max(np.hypot(mx,my)+br for mx,my,br,_ in p["markers"])
            disk_support=min(cx-(b.disk.h+b.disk.b/np.sqrt(2.)),b.disk.H-cz,
                             (b.disk.H-cz-slope*(mr+cx))/np.sqrt(1.+slope*slope))
            i=len(summary["stages"]);np.savez(out/("stage-%02d.npz"%i),coefficients=x)
            rec={"stage":i,"design":d,"configuration":stage,"nfev":int(result.nfev),"njev":int(result.njev or 0),
                 "cost":float(result.cost),"solver_status":int(result.status),"optimality":float(result.optimality),
                 "start_x_sha256":old.array_digest(x0),"source_x_sha256":old.array_digest(src[1]) if src else None,
                 "x_sha256":old.array_digest(x),"coefficient_count":b.n,"train":train,"check":met,
                 "frozen_target_source_x_sha256":old.array_digest(target.x) if target else None,
                 "finite_difference_relative":fd,"adjoint_abs":adj,"minimum_support":sup,"exact_disk_support_formula_float":float(disk_support),
                 "exact_unmarked_disk_K_bound_formula_float":float(np.pi/(2*b.disk.b*(1-b.disk.e))),
                 "sample_witness_to_upper_shoulder":gap,
                 "score":float(score),"elapsed":time.monotonic()-t0}
            summary.pop("in_progress",None);summary["stages"].append(rec);save()
            print(json.dumps({"event":"stage","stage":i,"design":d["id"],"score":score,
                         "gauged_max":met["gauged_max_relative"],"curvature":met["K_sample_max"],"x":rec["x_sha256"]}),flush=True)
            return b,x,rec
        bank=[]
        for d in p["designs"]:
            src=parents.get(d.get("parent_stage"))
            b,x,r=solve(d,p["coarse"],src)
            bank.append((r["score"],d,b,x,r))
        _,d,b,x,r=min(bank,key=lambda v:v[0]);summary["selected_coarse_stage"]=r["stage"]
        for stage in p["design_refinements"]:
            b,x,r=solve(d,stage,(b,x))
        target=Fixed(b,x,p["freeze_angular"])
        nodes=np.linspace(0.,1.,257)
        ee,po=target.values(nodes)
        summary["frozen_target"]={"source_stage":r["stage"],"source_x_sha256":old.array_digest(x),
               "angular_count":target.count,"check_257x2_sha256":old.array_digest(np.stack([ee[:,0],po[:,0]],axis=1)),
               "definition":"The same source field's fixed uniform-angle mean normal-speed-squared and mean angular speed at every requested physical radius. No radial interpolation. Target diag(E,P^2); physical s=L t."}
        save();full=[(b,x,r)]
        for stage in p["fixed_refinements"]:
            b,x,r=solve(d,stage,(b,x),target);full.append((b,x,r))
        for b,x,r in full:
            r["whole_sampled_phases"]=phase_values(b,x,p);save()
        summary["status"]="completed_parent_comparison_design_and_two_frozen_resolutions";save()
    except Exception as exc:
        summary["status"]="runtime_failure";summary["exception"]=type(exc).__name__+": "+str(exc)[:1200];save()
        traceback.print_exc()
        return 1
    return 0


if __name__=="__main__":
    raise SystemExit(main())
