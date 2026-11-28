#!/usr/bin/env python3
"""R766 actual cyclic triangle-distance propagation across both complete R764 pre-rolls."""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import numpy as np
from scipy.interpolate import BSpline,CubicSpline,make_interp_spline
from scipy.optimize import least_squares
from scipy.sparse import coo_matrix,eye,vstack
from r742_tilted_disk_two_jets import J,cap_s7,gather
import r766_positive_boundary_curvature_and_exact_signed_ribbons as geom
import solve_r764_corrugated_whole_sphere as prior

base=geom.base;old=geom.old;m=geom.m
B=base.HALF;E=base.E;L=base.L
PHASES=(0.,.075,.15,.225,.30,.375,.45,.525,.60,.675,.75,.825,.90)
LEVELS=((96,12,16,16),(192,24,24,24),(384,48,32,32))
MET=["relative_gram_op","max_abs_frame11","max_abs_frame12","max_abs_frame22","max_abs_principal","min_support","min_relative_area"]


def nodes(n,order):
    half=old.material(order,True)[-1]
    core=m.grip_s(.55,order);u=np.unique(np.r_[np.arange(n//2+1)*2*half/n,core])
    return np.r_[u,2*half-u[-2:0:-1]],len(u),2*half


def input_ring(s,nu,ph,order):
    q,t,n,k,kp=geom.curve(s,ph,order)
    q0=old.data(s,0.,order,True)[0]
    if not ph:
        return q0,[0.,0.,0.]
    z=geom.curve(s[:nu],ph,order,aligned=False)[0];edge=np.diff(z,axis=0)
    raw=np.linalg.norm(edge,axis=1);target=np.linalg.norm(np.diff(q0[:nu],axis=0),axis=1)
    unit=edge/raw[:,None];bell=geom.knob((s[1:nu]+s[:nu-1])/2,order)[0]
    def integral(b):
        return np.sum(target*geom.rot(unit,b*bell)[:,1])
    lo,hi=-.45,.45
    if integral(lo)>0 or integral(hi)<0:
        raise ValueError("input polygon fails the complete signed closure bracket")
    for _ in range(56):
        mid=(lo+hi)/2
        if integral(mid)>0:hi=mid
        else:lo=mid
    b=(lo+hi)/2;up=z[0]+np.vstack((np.zeros(2),np.cumsum(target[:,None]*geom.rot(unit,b*bell),axis=0)))
    # Both extreme points lie on the true reflecting line.
    up[0,1]=0.;up[-1,1]=0.
    low=up[-2:0:-1].copy();low[:,1]*=-1
    _,_,_,angle,_,_=geom.state(order,ph);qp=geom.rot(np.vstack((up,low)),angle)
    anchor=np.argmin(np.abs(s-m.grip_s(.55,order)));qp+=q[anchor]-qp[anchor]
    dst=np.linalg.norm(np.roll(qp,-1,axis=0)-qp,axis=1)
    original=np.linalg.norm(np.roll(q0,-1,axis=0)-q0,axis=1)
    return qp,[float(b),float(np.max(np.abs(dst/original-1))),float(np.max(np.linalg.norm(qp-q,axis=1)))]


def original_grid(s,v,order,side):
    q,_,n,_,_=old.data(s,0.,order,True);p,d=base.initial_turn(J(v),order)
    x=q[:,None,:]-n[:,None,:]*d.v[None,:,None]
    out=np.zeros((len(s),len(v),3));out[:,:,0]=x[:,:,0];out[:,:,2]=x[:,:,1]
    out[:,:,1]=side*(B+p.v);return out


def guide(chart,s,v,ph,order,e):
    if chart=="cylinder":
        return geom.central(s,v,ph,order)
    side=1 if chart.endswith("+") else -1
    if not chart.startswith("preband"):
        j=geom.moved_whole(chart,s,v,ph,order)
        if chart.startswith("round"):
            a,b=np.broadcast_arrays(np.asarray(s,float),np.asarray(v,float));sh=a.shape
            u,w=J(a.ravel(),s=1.),J(b.ravel(),a=1.)
            dh=-side*(e*ph/.90)*(1-geom.rigid_weight(u,order))*(1-cap_s7(w/L))
            j.reshape(-1,6,3)[:,:,1]+=np.stack(np.broadcast_arrays(*(x+np.zeros_like(u.v) for x in dh.parts())),axis=1)
        return j
    a,b=np.broadcast_arrays(np.asarray(s,float),np.asarray(v,float));shape=a.shape;a,b=a.ravel(),b.ravel()
    u,w=J(a,s=1.),J(b,a=1.);q,n=geom.curve_jet(u,ph,order);q0,n0=old.profile(u,0.,order,True)
    angle,tr=geom.right_motion(order,ph);co,si=np.cos(angle),np.sin(angle)
    q0=[co*q0[0]-si*q0[1]+tr[0],si*q0[0]+co*q0[1]+tr[1]]
    n0=[co*n0[0]-si*n0[1],si*n0[0]+co*n0[1]]
    p,d=base.initial_turn(w,order);h=base.smooth5(w/E);eta=(e*ph/.90)*(1-geom.rigid_weight(u,order))
    plane=[(1-h)*(q[i]-d*n[i])+h*(q0[i]-d*n0[i]) for i in range(2)]
    return gather((plane[0],side*(B+p-eta*h),plane[1]),len(a)).reshape(shape+(6,3))


def lengths(x):
    return np.linalg.norm(x,axis=-1)


def cartesian_row(P,guess,targets,sgn,maxev,fixed,anchor):
    n=len(P);i=np.arange(n);j=(i+1)%n;di=(i+sgn)%n
    a,b,c=targets
    def fun(x):
        q=x.reshape(-1,3).copy();q[fixed]=anchor[fixed];d=(q-P,q-P[di],q[j]-q)
        return np.concatenate([(np.einsum("ij,ij->i",z,z)/ell**2-1)/2 for z,ell in zip(d,(a,b,c))])
    def jac(x):
        q=x.reshape(-1,3).copy();q[fixed]=anchor[fixed];d=(q-P,q-P[di],q[j]-q)
        rows=np.tile(i[:,None],(1,3));xyz=np.arange(3)
        rr=[];cc=[];vv=[]
        for k,(z,ell) in enumerate(zip(d,(a,b,c))):
            z=z/ell[:,None]**2
            if k<2:
                rr.append((rows+k*n).ravel());cc.append((3*i[:,None]+xyz).ravel());vv.append(z.ravel())
            else:
                for col,sign in ((i,-1),(j,1)):
                    rr.append((rows+k*n).ravel());cc.append((3*col[:,None]+xyz).ravel());vv.append(sign*z.ravel())
        mat=coo_matrix((np.concatenate(vv),(np.concatenate(rr),np.concatenate(cc))),shape=(3*n,3*n)).tocsr()
        return mat.multiply(np.repeat(~fixed,3)[None,:]).tocsr()
    opt=least_squares(fun,guess.ravel(),jac=jac,method="trf",tr_solver="lsmr",
        max_nfev=2*maxev,tr_options={"maxiter":180,"atol":1e-11,"btol":1e-11},
        ftol=1e-12,xtol=1e-12,gtol=1e-12)
    q=opt.x.reshape(-1,3).copy();q[fixed]=anchor[fixed]
    return q,int(opt.nfev)


def advance(P,guess,targets,side,sgn,maxev,fixed,anchor):
    n=len(P);i=np.arange(n);j=(i+1)%n;di=(i+sgn)%n
    a,b,c=targets;edge=P[di]-P;ell=lengths(edge);ev=0
    good=np.all(ell>0)
    if good:
        t=edge/ell[:,None];xi=(ell*ell+(a-b)*(a+b))/(2*ell);rr=(a-xi)*(a+xi)
        good=np.all(rr>0)
    else:
        rr=np.zeros_like(ell)
    if good:
        origin=P+xi[:,None]*t
        trial=np.zeros_like(t);trial[:,1]=side
        vy=trial-t*np.einsum("ij,ij->i",trial,t)[:,None]
        bad=lengths(vy)<1e-4
        if np.any(bad):
            replacement_axis=np.eye(3)[np.argmin(np.abs(t[bad]),axis=1)]
            vy[bad]=replacement_axis-t[bad]*np.einsum("ij,ij->i",replacement_axis,t[bad])[:,None]
        vy/=lengths(vy)[:,None];nr=np.cross(t,vy);rad=np.sqrt(rr)
        delta=guess-origin
        wanted=np.arctan2(np.einsum("ij,ij->i",delta,nr),np.einsum("ij,ij->i",delta,vy))
        def positions(h):
            co=np.cos(h)[:,None];si=np.sin(h)[:,None]
            q=origin+rad[:,None]*(co*vy+si*nr);d=rad[:,None]*(-si*vy+co*nr)
            q[fixed]=anchor[fixed];d[fixed]=0.
            return q,d
        def residual(h):
            q,_=positions(h);z=q[j]-q
            return (np.einsum("ij,ij->i",z,z)/c**2-1)/2
        def derivative(h):
            q,d=positions(h);z=(q[j]-q)/c[:,None]**2
            aa=-np.einsum("ij,ij->i",z,d);bb=np.einsum("ij,ij->i",z,d[j])
            return coo_matrix((np.r_[aa,bb],(np.r_[i,i],np.r_[i,j])),shape=(n,n)).tocsr()
        h=wanted.copy()
        for reg in (.001,0.):
            def fun(x):
                f=residual(x)
                return np.r_[f,reg*(x-wanted)] if reg else f
            def jac(x):
                J0=derivative(x)
                return vstack((J0,reg*eye(n)),format="csr") if reg else J0
            opt=least_squares(fun,h,jac=jac,method="trf",tr_solver="lsmr",max_nfev=maxev,
                tr_options={"maxiter":180,"atol":1e-11,"btol":1e-11},ftol=1e-13,xtol=1e-13,gtol=1e-13)
            h=opt.x;ev+=int(opt.nfev)
        Q=positions(h)[0]
    else:
        Q,ev=cartesian_row(P,guess,targets,sgn,maxev,fixed,anchor)
    got=(lengths(Q-P),lengths(Q-P[di]),lengths(Q[j]-Q))
    err=[float(np.max(np.abs((val/tar)**2-1))) for val,tar in zip(got,targets)]
    return Q,[int(good),ev,float(np.min(rr)),*err]


def integrate(level,ph,e,pattern,side):
    n,nv,order,maxev=level;s,nu,period=nodes(n,order);v=np.linspace(0,E,nv+1);ix=np.arange(len(s))
    ref=original_grid(s,v,order,side);qp,pen=input_ring(s,nu,ph,order)
    ss,vv=np.meshgrid(s,v,indexing="ij")
    pre=guide("preband"+("+" if side==1 else "-"),ss,vv,ph,order,e)[:,:,0,:]
    q=np.empty_like(ref);q[:,0,0]=qp[:,0];q[:,0,2]=qp[:,1];q[:,0,1]=side*B;rows=[]
    fixed=geom.rigid_weight(J(s),order).v==1.;angle,tr=geom.right_motion(order,ph)
    equator=nu-1;offset=qp[equator]-geom.rot(ref[equator,0,[0,2]],angle)
    for k in range(nv):
        step=1 if pattern=="forward" or k%2==0 else -1
        di=(ix+step)%len(s);j=(ix+1)%len(s)
        a=lengths(ref[:,k+1]-ref[:,k]);b=lengths(ref[:,k+1]-ref[di,k])
        c=lengths(ref[j,k+1]-ref[:,k+1])
        if ph==0.:
            q[:,k+1]=ref[:,k+1]
            ell=lengths(ref[di,k]-ref[:,k]);xi=(ell*ell+(a-b)*(a+b))/(2*ell)
            rows.append([1,0,float(np.min((a-xi)*(a+xi))),0.,0.,0.]);continue
        guide_step=pre[:,k+1]-pre[:,k]
        if k:
            previous=q[:,k]-q[:,k-1]
            guide_step=.65*guide_step+.35*previous
        anchor=ref[:,k+1,:].copy();xz=geom.rot(anchor[:,[0,2]],angle)+offset
        anchor[:,0]=xz[:,0];anchor[:,2]=xz[:,1]
        q[:,k+1],cost=advance(q[:,k],q[:,k]+guide_step,(a,b,c),side,step,maxev,fixed,anchor)
        rows.append(cost)
    # Preserve the analytic entire central seam of the reconstructed C2 image.
    # The input polygon differs from its true unit curve by a measured small price.
    delta=q-pre;dv=delta[:,0].copy();smooth=base.smooth5(J(v/E)).v
    delta-=dv[:,None,:]*(1-smooth)[None,:,None];delta[:,0]=0.;delta[fixed]=0.
    if ph==0.:delta.fill(0.)
    stats=np.asarray(rows,dtype="<f8");raw=stats.tobytes()
    return delta,{"input_boundary":pen,"rows":len(rows),"cartesian_fallback":int(np.count_nonzero(stats[:,0]==0)),
        "nfev":int(np.sum(stats[:,1])),"minimum_circle_radius_squared":float(np.min(stats[:,2])),
        "maximum_squared_edge_prices":np.max(stats[:,3:],axis=0).tolist(),
        "peak_rows":np.argmax(stats[:,3:],axis=0).tolist(),"row_record":[len(raw),sha256(raw).hexdigest()]},raw


class RingField:
    def __init__(self,s,v,period,delta):
        h=v[1]-v[0];D=np.swapaxes(delta,0,1);zero=np.zeros_like(D[0])
        d1=(25*D[-1]-48*D[-2]+36*D[-3]-16*D[-4]+3*D[-5])/(12*h)
        d2=(35*D[-1]-104*D[-2]+114*D[-3]-56*D[-4]+11*D[-5])/(12*h*h)
        spl=make_interp_spline(v,D,k=5,bc_type=([(1,zero),(2,zero)],[(1,d1),(2,d2)]))
        c=np.swapaxes(spl.c,0,1);self.rad=BSpline(spl.t,np.eye(c.shape[1]),5)
        self.ang=CubicSpline(np.r_[s,period],np.concatenate((c,c[:1]),axis=0),axis=0,bc_type="periodic")
        self.P=period

    def component(self,u,v,i,j):
        S=self.ang(np.mod(u,self.P),nu=i);V=self.rad(v,nu=j)
        return np.einsum("nrc,nr->nc",S,V)

    def jet(self,chart,s,v,ph,order,e):
        a,w=np.broadcast_arrays(np.asarray(s,float),np.asarray(v,float));shape=a.shape
        a,w=a.ravel(),w.ravel();out=guide(chart,a,w,ph,order,e)
        if not (chart.startswith("preband") or chart.startswith("round")):
            return out.reshape(shape+(6,3))
        # The angular weight protects the entire connected exact right sector.
        mask=1-geom.rigid_weight(J(a,s=1.),order)
        if chart.startswith("preband"):
            cols=[self.component(a,w,i,j) for i,j in ((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))]
            for k in range(3):
                d=mask*J(*(x[:,k] for x in cols))
                out[:,:,k]+=np.stack(np.broadcast_arrays(*(z+np.zeros_like(w) for z in d.parts())),axis=1)
        else:
            vr=J(w,a=1.);fade=1-cap_s7(vr/L);end=np.full(len(a),E)
            order2=[[self.component(a,end,i,j) for i in range(3)] for j in range(3)]
            for k in range(3):
                terms=[J(z[0][:,k],s=z[1][:,k],ss=z[2][:,k]) for z in order2]
                d=mask*fade*(terms[0]+vr*terms[1]+.5*vr*vr*terms[2])
                out[:,:,k]+=np.stack(np.broadcast_arrays(*(z+np.zeros_like(w) for z in d.parts())),axis=1)
        return out.reshape(shape+(6,3))


def relative(cur,ref,sign,center):
    a,b=ref[:,1],ref[:,2];l=lengths(a);e1=a/l[:,None]
    proj=np.einsum("ij,ij->i",b,e1);perp=lengths(b-proj[:,None]*e1)
    pa=1/l[:,None];pc=1/perp[:,None];pb=-proj[:,None]*pa*pc
    ff=prior.linjet(cur,pa,pb,pc);f,ta,tb,aa,ab,bb=np.moveaxis(ff,1,0)
    cr=np.cross(ta,tb);area=lengths(cr);nor=sign*cr/np.maximum(area[:,None],1e-18)
    dot=lambda p,q:np.einsum("ni,ni->n",p,q)
    g11,g12,g22=dot(ta,ta),dot(ta,tb),dot(tb,tb)
    gram=np.stack((g11-1,g12,g12,g22-1),axis=1).reshape(-1,2,2)
    l,mix,n=dot(nor,aa),dot(nor,ab),dot(nor,bb)
    ii=np.stack((l,mix,mix,n),axis=1).reshape(-1,2,2)
    _,sv,vt=np.linalg.svd(np.swapaxes(ff[:,1:3],1,2),full_matrices=False)
    ks=np.linalg.eigvalsh((vt@ii@np.swapaxes(vt,1,2))/np.maximum(sv[:,:,None]*sv[:,None,:],1e-24))
    return [float(np.max(np.abs(np.linalg.eigvalsh(gram)))),float(np.max(np.abs(g11-1))),
            float(np.max(np.abs(g12))),float(np.max(np.abs(g22-1))),float(np.max(np.abs(ks))),
            float(np.min(dot(f-center,nor))),float(np.min(area))]


def audit(idx,ph,e,fields):
    lev=prior.LEVELS[idx];order=lev[2];out={};minhold=np.inf
    witness=base.chart_jet("cylinder",0.,0.,0.,order,e,False)[0]
    ox,oz=m.axis(order);w=witness.copy();w[[0,2]]=geom.rot(w[[0,2]]-np.array([ox,oz]),-ph)+np.array([ox,oz])
    center=np.array([m.section_center(order),0.,0.])
    for chart,(ss,vv) in zip(prior.CHARTS,prior.axes(lev,ph,True)):
        s,v=ss.ravel(),vv.ravel();side=1 if chart.endswith("+") else -1
        sign=1 if chart=="cylinder" else side*(-1 if chart.startswith("cap") and not chart.startswith("cap-normal") else 1)
        chunk=[]
        for lo in range(0,len(s),384):
            sl=slice(lo,lo+384);x=s[sl];y=v[sl]
            cur=fields[side].jet(chart,x,y,ph,order,e);ref=base.chart_jet(chart,x,y,0.,order,e,False)
            chunk.append(relative(cur,ref,sign,center));minhold=min(minhold,float(np.min(lengths(cur[:,0]-w))))
        cc=np.asarray(chunk)
        out[chart]=[len(s),*cc[:,:5].max(axis=0).tolist(),*cc[:,5:].min(axis=0).tolist()]
    # True seam through old tail, its zero curvature, complete straight continuation, and the new wall.
    _,edge=geom.right_data(order);cut,_,half=old.material(order,True)
    ss,vr=np.meshgrid(np.r_[edge-.05,edge-.0005,edge,edge+.05,cut+.002,half],np.linspace(0,E,33),indexing="ij")
    old_address={}
    for side,name in ((1,"preband+"),(-1,"preband-")):
        actual=fields[side].jet(name,ss,vr,ph,order,e)
        rig=geom.moved_whole(name,ss,vr,ph,order)
        old_address[name]=float(np.max(np.abs(actual-rig)))
    return {"charts":out,"minimum_sampled_held_witness":minhold,"right_sector_rigid_sixjet":old_address}


def make_fields(level,arr):
    n,nv,order,_=level;s,_,period=nodes(n,order);v=np.linspace(0,E,nv+1)
    return {side:RingField(s,v,period,D) for side,D in arr.items()}


def fitted_chart_jet(chart,s,v,ph,idx,e,folder,rotate=True):
    level=LEVELS[idx];n,nv,order,_=level;sn,_,_=nodes(n,order)
    ip=max(0,min(len(PHASES)-2,np.searchsorted(PHASES,ph,side="right")-1))
    q=(ph-PHASES[ip])/(PHASES[ip+1]-PHASES[ip]);w=q**3*(10+q*(-15+6*q))
    side=1 if chart.endswith("+") else -1
    def read(j):
        return np.fromfile(Path(folder)/f"level{idx}-phase{j}-side{side}.f64",dtype="<f8").reshape(len(sn),nv+1,3)
    obj=make_fields(level,{side:(1-w)*read(ip)+w*read(ip+1)})[side]
    out=obj.jet(chart,s,v,ph,order,e)
    if rotate:
        ox,oz=m.axis(order);xz=out[...,[0,2]].copy();xz[...,0,:]-=[ox,oz]
        xz=geom.rot(xz,ph);xz[...,0,:]+=[ox,oz];out[...,0]=xz[...,0];out[...,2]=xz[...,1]
    return out


def solve(folder,e,pattern):
    for idx,level in enumerate(LEVELS):
        rings=[];smooth=[];prev=None
        for ip,ph in enumerate(PHASES):
            coef={};prices={}
            for side in (-1,1):
                D,c,raw=integrate(level,ph,e,pattern,side)
                b=np.asarray(D,dtype="<f8").tobytes();coef[side]=D
                (folder/f"level{idx}-phase{ip}-side{side}.f64").write_bytes(b)
                (folder/f"level{idx}-phase{ip}-side{side}-rows.f64").write_bytes(raw)
                prices[str(side)]={**c,"coefficient_words":[len(b),sha256(b).hexdigest()]}
            rings.append([ph,geom.state(level[2],ph)[-1],prices])
            fitted=audit(idx,ph,e,make_fields(level,coef));smooth.append([ph,"integrated",fitted])
            if prev is not None:
                between=(PHASES[ip-1]+ph)/2;mid={k:(prev[k]+coef[k])/2 for k in coef}
                smooth.append([between,"independent_interpolation",audit(idx,between,e,make_fields(level,mid))])
            print("R766 complete cyclic propagation",idx,ph,e,pattern,prices,
                "metric",max(x[1] for x in fitted["charts"].values()),flush=True)
            prev=coef
        header={"schema":"R766-two-whole-preband-circle-propagation-and-closed-cap-audit-v1","pattern":pattern,
             "e":e,"level":idx,"grid":level,"run":os.environ["GITHUB_RUN_ID"],"attempt":os.environ["GITHUB_RUN_ATTEMPT"],
             "source_commit":os.environ["R766_SOURCE_COMMIT"],"rules_read_commit":os.environ["R766_RULES_COMMIT"]}
        for suffix,data in (("rings",{"edge_price_order":["meridian","diagonal","upper_ring"],"rows":rings}),
                            ("surface",{"columns":["points",*MET],"rows":sorted(smooth)})):
            prior.write(folder/f"stage-{idx}-{suffix}.json",{**header,"experiment":suffix,**data})


if __name__=="__main__":
    arg=argparse.ArgumentParser(description=__doc__)
    arg.add_argument("--pattern",choices=("forward","alternating"),required=True)
    arg.add_argument("--retreat",type=float,choices=base.ENDS,required=True)
    arg.add_argument("--folder",type=Path,required=True);v=arg.parse_args();m.old.disk._public()
    v.folder.mkdir(exist_ok=True,parents=True);solve(v.folder,v.retreat,v.pattern)
