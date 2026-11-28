#!/usr/bin/env python3
"""R760 full-phase physical Gauss-Newton fit on both complete curved ends and crowns."""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import sys
import numpy as np
from scipy.optimize import least_squares
from scipy.sparse.linalg import LinearOperator
import r760_cartesian_curved_crown_and_lower_rate_walls as geom
import r758_curved_outer_collars_and_fixed_elliptical_crowns as earlier
from functools import lru_cache
from scipy.spatial.transform import Rotation
from r742_tilted_disk_two_jets import J,cap_s7,trig

p=geom
m=geom.m
WC=1-(1-geom.JOIN)*geom.RHO_CORE
KMAX=8.
RMIN=.125
PHASES=(0.,.15,.30,.45,.60,.75,.90)
# Angular nodes, transverse intervals, quadrature, Fourier order, radial order,
# full nonlinear evaluations, inner LSMR iterations, independent audit grid.
LEVELS=((24,6,16,2,2,12,12,64,12),
        (40,9,24,3,3,20,16,96,18),
        (64,12,32,5,4,30,20,144,26))
CHARTS=("cylinder","end","cap","cap-normal","cap-cartesian")


def grid(n,k,order,ph,side,rich):
    cut,length,half=p.material(order,True)
    time=m.old.PLANAR_TURN*ph
    elbows=np.asarray(p.clock_spec(True)[1])
    main=m.flat_material_s(np.array([-.5,.30,.30+.26*.125,.56-.26*.125,.56,1.]),order=order)
    pts=np.r_[m.LEFT_LENGTH/2,cut+elbows,cut-.30,cut-.20,cut-.10,half,main,main-time]
    if rich:
        pts=np.r_[pts,cut+(elbows[1:]+elbows[:-1])/2,
                  [m.grip_s(x,order)+a*r for x,y,r in m.MARKS for a in (-1.,-.70,0.,.70,1.)]]
    s=np.unique(np.r_[np.arange(n)*2*half/n,pts,2*half-pts])
    # Each true cap includes the regular Cartesian ellipse at and across its polar pole.
    vc=np.unique(np.r_[np.linspace(.02,1,k+1), .82*(1-geom.JOIN),.84*(1-geom.JOIN),.86*(1-geom.JOIN),
        .87*(1-geom.JOIN),.92*(1-geom.JOIN),.97*(1-geom.JOIN),.98*(1-geom.JOIN),
        1-geom.WIDTH,1-geom.WIDTH-geom.ROUND])
    near=np.unique(np.r_[np.linspace(0,geom.WIDTH,k+1),geom.WIDTH/2])
    yv=side*np.unique(np.r_[np.linspace(0,1,k+1),.33,.70,.75,.85])
    phi=np.arange(n)*2*np.pi/n
    ang,r=np.meshgrid(phi,np.linspace(0,.999999,max(3,k//2)),indexing="ij")
    cs=m.section_center(order)
    xy=(cs-geom.OFFSET+geom.EX*r*np.cos(ang),geom.EZ*r*np.sin(ang))
    return [np.meshgrid(s,yv,indexing="ij"),np.meshgrid(s,np.unique(np.r_[np.linspace(0,m.END_L,k+1),
        m.END_E,m.END_L-m.END_E]),indexing="ij"),np.meshgrid(s,vc,indexing="ij"),
        np.meshgrid(s,near,indexing="ij"),xy]


@lru_cache(maxsize=None)
def initial_paths(order,side):
    half=p.material(order,True)[-1]
    s=np.arange(24)*2*half/24
    cap="cap"+("+" if side>0 else "-")
    inner=geom.RHO_CORE*(1-geom.JOIN)
    marks=np.unique(np.r_[inner,1.,(1-geom.JOIN)*np.array([.84,.86,.87,.92,.97,.98]),
        1-geom.WIDTH,1-geom.WIDTH-geom.ROUND])
    nodes,weights=m.old.disk.rule(order);length=np.zeros_like(s)
    for lo,hi in zip(marks[:-1],marks[1:]):
        ss,vv=np.meshgrid(s,lo+(hi-lo)*nodes,indexing="ij")
        j=geom.chart_jet(cap,ss,vv,0.,order,rotate=False)
        length+=(hi-lo)*(np.linalg.norm(j[...,2,:],axis=-1)@weights)
    core=geom.chart_jet(cap,s,np.full_like(s,inner),0.,order,rotate=False)[:,0]
    delta=core[None,:,:]-core[:,None,:]
    flat=delta[...,[0,2]]
    # The complete Cartesian quadratic ellipse is convex. Follow its actual
    # straight projected chord between each pair, using its true graph speed.
    xz=(core[:,[0,2]]-np.array([m.section_center(order)-geom.OFFSET,0.]))[:,None,:]
    inside=np.zeros((len(s),len(s)))
    for t,w in zip(nodes,weights):
        body=xz+t*flat
        dy=2*geom.BOWL*(body[...,0]*flat[...,0]/geom.EX**2+body[...,1]*flat[...,1]/geom.EZ**2)
        inside+=w*np.sqrt(np.sum(flat*flat,axis=-1)+dy*dy)
    return s,length[:,None]+inside,cap,inner


@lru_cache(maxsize=None)
def knot_pose(order,side,ph):
    s,paths,cap,inner=initial_paths(order,side)
    rim=geom.chart_jet(cap,s,np.ones_like(s),ph,order,rotate=False)[:,0]
    core=geom.chart_jet(cap,s,np.full_like(s,inner),ph,order,rotate=False)[:,0]
    center=np.mean(core,axis=0)
    def prices(v):
        moved=Rotation.from_rotvec(v[:3]).apply(core-center)+center+v[3:]
        return np.linalg.norm(rim[:,None,:]-moved[None,:,:],axis=-1)-paths
    reg=np.array([.006,.006,.006,.003,.003,.003])
    def residual(v):
        return np.r_[np.maximum(0.,prices(v)).ravel(),reg*v]
    z=np.zeros(6)
    v=z if ph==0. else least_squares(residual,z,max_nfev=96,xtol=1e-11,ftol=1e-11,gtol=1e-11,
            bounds=([-1.2]*3+[-.7]*3,[1.2]*3+[.7]*3)).x
    return v,center,[float(np.max(prices(z))),float(np.max(prices(v)))]


def posed(name,u,v,ph,order,side):
    j=geom.chart_jet(name,u,v,ph,order,rotate=False)
    ip=max(0,min(len(PHASES)-2,np.searchsorted(PHASES,ph,side="right")-1))
    t=(ph-PHASES[ip])/(PHASES[ip+1]-PHASES[ip]);b=t**3*(10+t*(-15+6*t))
    va,ca,_=knot_pose(order,side,PHASES[ip]);vb,cb,_=knot_pose(order,side,PHASES[ip+1])
    pose=(1-b)*va+b*vb;center=(1-b)*ca+b*cb
    if name in ("cylinder","end+","end-") or name.startswith("cap-normal"):
        return j
    vv=J(v,a=1.)
    wt=J(np.ones_like(v)) if name.startswith("cap-cartesian") else cap_s7((1-vv-.025)/(WC-.025))
    rotation=Rotation.from_rotvec(pose[:3]).as_matrix()
    norm=j.copy();norm[:,0]-=center
    delta=norm@(rotation-np.eye(3)).T;delta[:,0]+=pose[3:]
    for c in range(3):
        q=wt*J(*delta[:,:,c].T)
        j[:,:,c]+=np.stack(np.broadcast_arrays(*(e+np.zeros_like(v) for e in q.parts())),axis=1)
    return j


def tip_audit(order,side):
    ch="cap"+("+" if side>0 else "-")
    rows=[]
    for key,g,pp in (("R758",earlier,earlier.pre),("R760",geom,p)):
        for ph in PHASES:
            s=pp.material(order,True)[-1];v=.84*(1-g.JOIN)
            jets=g.chart_jet(ch,s,v,ph,order,rotate=False)
            tang=jets[1:3][:,[0,2]]
            grad=np.linalg.solve(tang,jets[1:3,1])
            h=jets[3:,1]-jets[3:][:,[0,2]]@grad
            inverse=np.linalg.inv(tang)
            hh=inverse@h[[0,1,1,2]].reshape(2,2)@inverse.T
            gauss=np.linalg.det(hh)/(1+grad@grad)**2
            rows.append([key,ph,float(s),float(v),grad.tolist(),hh.tolist(),float(gauss)])
    return rows


CART_CENTERS=tuple((x,z) for x in (-.90,-.45,0.,.40,.72) for z in (-.55,0.,.55))


def columns(kind,u,v,side,order,mode,M,N,ref=None):
    zero=J(np.zeros_like(u.v));one=zero+1.
    if kind=="cap-cartesian":
        return [zero]*((2*M+1)*N*2+2*len(CART_CENTERS))+[one]
    if kind=="cylinder":
        tau=side*v-1.
    elif kind=="end":
        tau=v
    elif kind=="cap":
        tau=m.END_L+1-v
    else:
        tau=m.END_L+v
    cut,extent,half=p.material(order,True)
    angle=u*(np.pi/half)
    az=[one]
    for j in range(1,M+1):
        az.extend(trig(j*angle))
    def packet(left,right,active):
        x=(tau-left)/(right-left)
        envelope=active*cap_s7(x/.19)*cap_s7((1-x)/.19)
        radial=[envelope]
        for j in range(1,N):
            radial.append(envelope*trig(np.pi*j*x)[0])
        return [f*b for f in az for b in radial]
    main=packet(m.END_L+geom.WIDTH,m.END_L+WC,one)
    if mode=="outer_locked":
        extra=packet(0.,m.END_L+.12,1-geom.right_weight(u,order))
    else:
        extra=packet(-.30,m.END_L+.12,one)
    shift=cap_s7((tau-m.END_L-.025)/(WC-.025))
    if ref is None:
        name=kind if kind=="cylinder" else kind+("+" if side>0 else "-")
        ref=geom.chart_jet(name,u.v,v.v,0.,order,rotate=False)
    xx=J(*ref[:,:,0].T);zz=J(*ref[:,:,2].T)
    middle=main[0];sleeve=extra[0]
    bumps=[]
    for cx,cz in CART_CENTERS:
        dx=(xx-cx)/.36;dz=(zz-cz)/.39
        bumps.append(geom.expj(-(dx*dx+dz*dz)))
    return main+extra+[middle*b for b in bumps]+[sleeve*b for b in bumps]+[shift]


def linjet(mat,pa,pb,pc):
    # Initial orthonormal frame: e1=pa*u, e2=pb*u+pc*v, with positive determinant.
    # The Hessian terms from spatial differentiation of frame coefficients are
    # tangent and vanish against the normal, so the same transform applies to II.
    a,b=mat[:,1],mat[:,2]
    aa,ab,bb=mat[:,3],mat[:,4],mat[:,5]
    return np.stack((mat[:,0],pa*a,pb*a+pc*b,pa*pa*aa,pa*pb*aa+pa*pc*ab,
                     pb*pb*aa+2*pb*pc*ab+pc*pc*bb),axis=1)


class Data:
    def __init__(self,level,ph,side,mode,audit=False):
        n,k,order,M,N,_,_,an,ak=level
        self.M,self.N=M,N
        raw=[];bases=[];refs=[];weights=[];orient=[];blocks=[]
        nx=0
        gg=grid(an if audit else n,ak if audit else k,order,ph,side,audit)
        for kind,(s,v) in zip(CHARTS,gg):
            name=kind if kind=="cylinder" else kind+("+" if side>0 else "-")
            s,v=s.ravel(),v.ravel()
            cur=posed(name,s,v,ph,order,side)
            ref=geom.chart_jet(name,s,v,0.,order,rotate=False)
            cols=columns(kind,J(s,s=1.),J(v,a=1.),side,order,mode,M,N,ref)
            h=np.stack([np.stack(np.broadcast_arrays(*(entry+np.zeros_like(s) for entry in c.parts())),axis=1)
                        for c in cols],axis=-1)
            a,b=ref[:,1],ref[:,2];l=np.linalg.norm(a,axis=1)
            e1=a/l[:,None];proj=np.einsum("ni,ni->n",b,e1)
            perp=b-proj[:,None]*e1;perpl=np.linalg.norm(perp,axis=1)
            if np.any((l<=0)|(perpl<=0)):
                raise ArithmeticError("singular input reference chart; regular Cartesian core is evaluated separately")
            pa=(1/l)[:,None];pc=(1/perpl)[:,None];pb=-proj[:,None]*pa*pc
            raw.append(linjet(cur,pa,pb,pc));bases.append(linjet(h,pa,pb,pc));refs.append(linjet(ref,pa,pb,pc))
            sign=1 if kind=="cylinder" else side*(-1 if kind in ("cap","cap-cartesian") else 1)
            orient.append(np.full(len(s),sign));weights.append(np.full(len(s),1/np.sqrt(len(s))))
            blocks.append((name,nx,nx+len(s)));nx+=len(s)
        self.base=np.concatenate(raw);self.h=np.concatenate(bases);self.ref=np.concatenate(refs)
        self.w=np.concatenate(weights);self.ori=np.concatenate(orient);self.blocks=blocks
        self.center=np.array([m.section_center(order),0.,0.])
        self.p=self.h.shape[-1]
        self.cache_key=None;self.saved=None

    def state(self,x):
        key=x.tobytes()
        if key==self.cache_key:
            return self.saved
        field=self.base+self.h@x.reshape(self.p,3)
        f,a,b,h11,h12,h22=np.moveaxis(field,1,0)
        dot=lambda x,y:np.einsum("ni,ni->n",x,y)
        cr=np.cross(a,b);area=np.linalg.norm(cr,axis=1)
        normal=self.ori[:,None]*cr/np.maximum(area,1e-14)[:,None]
        aa,ab,bb=dot(a,a),dot(a,b),dot(b,b)
        g=np.stack((aa,ab,ab,bb),axis=-1).reshape(-1,2,2)
        n11,n12,n22=(dot(z,normal) for z in (h11,h12,h22))
        ii=np.stack((n11,n12,n12,n22),axis=-1).reshape(-1,2,2)
        middle=f-self.center;support=dot(middle,normal)
        res=np.zeros((len(f),6));der=np.zeros((len(f),6,6,3))
        res[:,:3]=np.stack((aa-1,np.sqrt(2)*ab,bb-1),axis=-1)
        der[:,0,1]=2*a;der[:,1,1]=np.sqrt(2)*b;der[:,1,2]=np.sqrt(2)*a;der[:,2,2]=2*b
        def normder(val):
            tang=(val-dot(val,normal)[:,None]*normal)*(self.ori/np.maximum(area,1e-14))[:,None]
            return np.cross(b,tang),np.cross(tang,a)
        for ix,sgn in ((3,1.),(4,-1.)):
            values,vec=np.linalg.eigh(KMAX*g+sgn*ii)
            u=vec[:,0,0];v=vec[:,1,0]
            active=(values[:,0]<0)*(.18/KMAX)
            res[:,ix]=np.maximum(0.,-values[:,0])*(.18/KMAX)
            u,v=u[:,None],v[:,None]
            tangent=u*a+v*b;curv=u*u*h11+2*u*v*h12+v*v*h22
            na,nb=normder(curv);mult=-active[:,None]
            der[:,ix,1]=mult*(2*KMAX*u*tangent+sgn*na)
            der[:,ix,2]=mult*(2*KMAX*v*tangent+sgn*nb)
            der[:,ix,3]=mult*sgn*u*u*normal;der[:,ix,4]=mult*sgn*2*u*v*normal
            der[:,ix,5]=mult*sgn*v*v*normal
        active=(support<RMIN)*.30
        res[:,5]=.30*np.maximum(0.,RMIN-support);na,nb=normder(middle)
        der[:,5,0]=-active[:,None]*normal;der[:,5,1]=-active[:,None]*na;der[:,5,2]=-active[:,None]*nb
        self.cache_key=key;self.saved=(field,g,ii,support,area,res,der)
        return self.saved

    def fun(self,x):
        res=self.state(x)[-2]
        return np.r_[(self.w[:,None]*res).ravel(),.0002*x]

    def jac(self,x):
        der=self.state(x)[-1]*self.w[:,None,None,None]
        p=self.p;h=self.h
        def mv(y):
            col=np.asarray(y).ravel()
            df=h@col.reshape(p,3)
            return np.r_[np.einsum("nkac,nac->nk",der,df).ravel(),.0002*col]
        def rv(y):
            row=np.asarray(y).ravel();body=row[:-3*p].reshape(-1,6)
            normal=np.einsum("nk,nkac->nac",body,der)
            force=np.einsum("nap,nac->pc",h,normal,optimize=True)
            return force.ravel()+.0002*row[-3*p:]
        return LinearOperator((len(self.base)*6+3*p,3*p),matvec=mv,rmatvec=rv,dtype=np.float64)

    def result(self,x):
        field,g,ii,support,area,_,_=self.state(x)
        sig=np.linalg.svd(field[:,1:3,:],compute_uv=False)
        _,s,vt=np.linalg.svd(np.swapaxes(field[:,1:3],1,2),full_matrices=False)
        den=s[:,:,None]*s[:,None,:]
        cost=np.linalg.eigvalsh((vt@ii@np.swapaxes(vt,1,2))/np.maximum(den,1e-24))
        metric=np.max(np.abs(np.linalg.eigvalsh(g-np.eye(2))),axis=1)
        kk=np.max(np.abs(cost),axis=1)
        values={}
        for key,i,j in self.blocks:
            values[key]=[j-i,int(np.count_nonzero(sig[i:j,1]<=1e-12*sig[i:j,0])),
                float(np.max(metric[i:j])),float(np.max(kk[i:j])),float(np.min(support[i:j])),
                float(np.min(area[i:j]))]
        return values


def resize(x,prev,now):
    tail=2*len(CART_CENTERS)+1
    if x is None:
        return np.zeros((2*(2*now[0]+1)*now[1]+tail,3))
    mo,no=prev;mn,nn=now
    ans=np.zeros((2*(2*mn+1)*nn+tail,3))
    for r in range(2):
        a=x[:-tail].reshape(2,2*mo+1,no,3)
        b=ans[:-tail].reshape(2,2*mn+1,nn,3)
        b[r,:2*mo+1,:no]=a[r]
    ans[-tail:]=x[-tail:]
    return ans


def solve(mode,side,folder):
    rows=[];coeff={}
    for idx,level in enumerate(LEVELS):
        n,k,order,M,N,nfev,maxit,_,_=level
        prior=None
        for ip,ph in enumerate(PHASES):
            data=Data(level,ph,side,mode)
            prev=(LEVELS[idx-1][3],LEVELS[idx-1][4]) if idx else None
            seed=resize(coeff.get((idx-1,ip)),prev,(M,N)) if idx else resize(None,None,(M,N))
            if prior is not None and ip>1:
                # Pick the better full residual of the prior-phase solution and
                # the prolongated same-phase solution; neither changes the target.
                if np.linalg.norm(data.fun(prior.ravel()))<np.linalg.norm(data.fun(seed.ravel())):
                    seed=prior.copy()
            before=data.result(seed.ravel())
            if ph:
                opt=least_squares(data.fun,seed.ravel(),jac=data.jac,method="trf",tr_solver="lsmr",
                    tr_options={"maxiter":maxit,"atol":.0002,"btol":.0002},max_nfev=nfev,x_scale=1.,
                    ftol=1e-9,xtol=1e-9,gtol=1e-9)
                x=opt.x.reshape(-1,3);status=[int(opt.status),int(opt.nfev),float(opt.cost),float(opt.optimality)]
            else:
                x=seed;status=[0,0,float(np.linalg.norm(data.fun(x.ravel()))**2/2),0.]
            after=data.result(x.ravel());del data
            audit=Data(level,ph,side,mode,audit=True)
            checked=audit.result(x.ravel())
            packed=np.asarray(x,dtype="<f8").tobytes();coeff[idx,ip]=x;prior=x
            filename=f"{mode}_{side}_{idx}_{ip}.f64"
            (folder/filename).write_bytes(packed)
            rows.append({"level":idx,"phase":ph,"status_nfev_cost_optimality":status,
                "seed":before,"fit":after,"independent_grid":checked,
                "coeff":[len(packed),sha256(packed).hexdigest()]})
            del audit
            print("R760 finished",mode,side,idx,ip,status,flush=True)
    intermediate=[]
    for idx,level in enumerate(LEVELS):
        for ip,(lo,hi) in enumerate(zip(PHASES,PHASES[1:])):
            ph=(lo+hi)/2
            mid=(coeff[idx,ip]+coeff[idx,ip+1])/2
            audit=Data(level,ph,side,mode,audit=True)
            intermediate.append([idx,ph,audit.result(mid.ravel())])
            del audit
    return rows,intermediate


def fitted_chart_jet(chart,u,v,phase,mode,side,level,folder,rotate=True):
    """Reconstruct every phase from the complete runner coefficient words or command replay.

    Central y and the chosen signed half are explicit. C2 quintic interpolation
    in the same time-zero material frame joins the registered phase solutions.
    """
    idx=int(level)
    n,k,order,M,N,*_=LEVELS[idx]
    ph=float(phase)
    ip=max(0,min(len(PHASES)-2,np.searchsorted(PHASES,ph,side="right")-1))
    t=(ph-PHASES[ip])/(PHASES[ip+1]-PHASES[ip]);b=t*t*t*(10+t*(-15+6*t))
    path=lambda k:Path(folder)/f"{mode}_{side}_{idx}_{k}.f64"
    l=np.fromfile(path(ip),dtype="<f8").reshape(-1,3);r=np.fromfile(path(ip+1),dtype="<f8").reshape(-1,3)
    c=(1-b)*l+b*r
    def physical(name,uu,vv,_ph,x,y,z):
        kind=name if name=="cylinder" else name[:-1]
        terms=columns(kind,uu,vv,side,order,mode,M,N)
        return tuple(sum((term*row[i] for term,row in zip(terms,c)),J(np.zeros_like(uu.v))) for i in range(3))
    sa,sb=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float));shape=sa.shape
    sa,sb=sa.ravel(),sb.ravel();j=posed(chart,sa,sb,ph,order,side)
    delta=physical(chart,J(sa,s=1.),J(sb,a=1.),ph,None,None,None)
    for i,d in enumerate(delta):
        j[:,:,i]+=np.stack(np.broadcast_arrays(*(z+np.zeros_like(sa) for z in d.parts())),axis=1)
    if rotate:
        ox,oz=m.axis(order);c,h=np.cos(ph),np.sin(ph)
        x=j[:,:,0].copy();z=j[:,:,2].copy();x[:,0]-=ox;z[:,0]-=oz
        j[:,:,0]=c*x-h*z;j[:,:,2]=h*x+c*z;j[:,0,0]+=ox;j[:,0,2]+=oz
    return j.reshape(shape+(6,3))


def opposite_end_prices(level,mode,side,folder):
    """Original cap radial path from true rim to common bowl; each altered chord uses identical labels."""
    order=LEVELS[level][2];half=p.material(order,True)[-1];s=np.arange(16)*2*half/16
    inner=geom.RHO_CORE*(1-geom.JOIN)
    marks=np.unique(np.r_[inner,1.,(1-geom.JOIN)*np.array([.86,.87,.92,.97,.98]),
                           1-geom.WIDTH,1-geom.WIDTH-geom.ROUND])
    path=np.zeros_like(s);nodes,weights=m.old.disk.rule(order)
    chart="cap"+("+" if side>0 else "-")
    for v0,v1 in zip(marks[:-1],marks[1:]):
        xx,vv=np.meshgrid(s,v0+(v1-v0)*nodes,indexing="ij")
        jj=geom.chart_jet(chart,xx,vv,0.,order,rotate=False)
        path+=(v1-v0)*(np.linalg.norm(jj[...,2,:],axis=-1)@weights)
    rows=[];blob=bytearray()
    for ph in sorted(set(PHASES)|{(a+b)/2 for a,b in zip(PHASES[:-1],PHASES[1:])}):
        end=fitted_chart_jet(chart,s,np.ones_like(s),ph,mode,side,level,folder,False)[:,0]
        core=fitted_chart_jet(chart,s,np.full_like(s,inner),ph,mode,side,level,folder,False)[:,0]
        chord=np.linalg.norm(end-core,axis=-1)
        i=int(np.argmax(chord-path))
        blob.extend(np.asarray(np.stack((s,path,chord),axis=1),dtype="<f8").tobytes())
        rows.append([ph,float(s[i]),float(path[i]),float(chord[i]),float(chord[i]-path[i])])
    return [rows,len(blob),sha256(blob).hexdigest()]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mode",choices=("outer_locked","free_end"),required=True)
    ap.add_argument("--side",choices=(-1,1),type=int,required=True)
    ap.add_argument("--folder",type=Path,required=True);ap.add_argument("--report",type=Path,required=True)
    arg=ap.parse_args();m.old.disk._public();arg.folder.mkdir(exist_ok=True,parents=True)
    rows,between=solve(arg.mode,arg.side,arg.folder)
    rec={"schema":"R760-curved-crown-physical-fit-branch-v1","mode":arg.mode,"side":arg.side,
         "run":os.environ["GITHUB_RUN_ID"],"attempt":os.environ["GITHUB_RUN_ATTEMPT"],
         "source_commit":os.environ["R760_SOURCE_COMMIT"],"rules_read_commit":os.environ["R760_RULES_COMMIT"],
         "levels":LEVELS,"phases":PHASES,"rows":rows,"intermediate_phases":between,
         "whole_crown_SE3_knots":[[l[2],ph,knot_pose(l[2],arg.side,ph)[0].tolist(),knot_pose(l[2],arg.side,ph)[2]] for l in LEVELS for ph in PHASES],
         "original_actual_758_and_760_cartesian_tip":tip_audit(32,arg.side),
         "cap_radial_path_prices":[opposite_end_prices(i,arg.mode,arg.side,arg.folder) for i in range(len(LEVELS))],
         "chart_columns":["points","nearly_singular","relative_metric_max","max_abs_principal","min_support","min_relative_area"],
         "scope":"All five charts of this entire half-sphere, including the shared central half and the true regular Cartesian ellipse. All derivatives refer to the one curved R760 zero-phase target."}
    arg.report.write_text(json.dumps(rec,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n")


if __name__=="__main__":
    main()
