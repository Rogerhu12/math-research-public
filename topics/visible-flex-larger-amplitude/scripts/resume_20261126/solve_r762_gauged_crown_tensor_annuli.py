#!/usr/bin/env python3
"""Fit the true R760 curved caps using positive meridian coordinates and independent compact C2 tensor fields."""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import sys
import numpy as np
from scipy.optimize import least_squares
from scipy.sparse.linalg import LinearOperator
from scipy.sparse import csr_matrix,vstack
from r742_tilted_disk_two_jets import unary
import r762_positive_meridian_arclength_and_full_jets as transport
import solve_r760_curved_crown_middle_annuli as original
import r760_cartesian_curved_crown_and_lower_rate_walls as geom
import r758_curved_outer_collars_and_fixed_elliptical_crowns as earlier
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


posed=transport.posed
knot_pose=original.knot_pose


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


LOCAL={2:(6,3),3:(12,6),5:(24,12)}


def cardinal(x):
    a=np.abs(x.v);q=np.maximum(2-a,0.);sig=np.sign(x.v);inner=a<1
    val=np.where(inner,(4-6*a*a+3*a**3)/6,q**3/6)
    der=np.where(inner,(-12*a+9*a*a)/6,-q*q/2)*sig
    sec=np.where(inner,-2+3*a,q)
    return unary(x,val,der,sec)


def tensor_coords(x,y,period,na,nr):
    ax=x*(na/period)
    av=np.mod(ax.v[:,None]-np.arange(na)[None,:]+na/2,na)-na/2
    def shaped(j):
        return [np.broadcast_to(t,j.v.shape)[:,None] for t in j.parts()[1:]]
    aa=cardinal(J(av,*shaped(ax)))
    ry=y*nr;rv=ry.v[:,None]-np.arange(-1,nr+2)[None,:]
    rr=cardinal(J(rv,*shaped(ry)))
    a=J(*(t[:,:,None] for t in np.broadcast_arrays(*aa.parts())))
    b=J(*(t[:,None,:] for t in np.broadcast_arrays(*rr.parts())))
    return a*b


def layout(M,N):
    na,nr=LOCAL[M];global_count=2*(2*M+1)*N+2*len(CART_CENTERS)
    return global_count,na,nr,global_count+2*na*(nr+3)


def physical_basis(kind,s,v,side,order,mode,M,N,ref=None):
    """Return true physical scalar two-jets, points by derivatives by coefficient."""
    gcount,na,nr,count=layout(M,N);n=len(s)
    if kind=="cap-cartesian":
        return np.zeros((n,6,count))
    u=J(s,s=1.);vv=J(v,a=1.);one=J(np.ones(n))
    if kind=="cylinder":
        tau=side*vv-1
    elif kind=="end":
        tau=vv
    elif kind=="cap":
        tau=m.END_L+1-vv
    else:
        tau=m.END_L+vv
    cut,extent,half=p.material(order,True);period=2*half
    angle=u*(2*np.pi/period);az=[one]
    for j in range(1,M+1):
        az.extend(trig(j*angle))
    # The three-dimensional displacement is zero on both open cap guards.
    # A sleeve may change the whole roll in free_end, and closes before the rim guard.
    if mode=="outer_locked":
        start=0.;active=1-geom.right_weight(u,order)
    else:
        start=-.30;active=one
    def packet(left,right,active):
        t=(tau-left)/(right-left)
        env=active*cap_s7(t/.19)*cap_s7((1-t)/.19)
        radial=[env]+[env*trig(np.pi*j*t)[0] for j in range(1,N)]
        return [a*b for a in az for b in radial],t,env
    margin=.04*(WC-geom.WIDTH)
    main,x,em=packet(m.END_L+geom.WIDTH+margin,m.END_L+WC-margin,one)
    extra,y,ee=packet(start,m.END_L+geom.WIDTH-.0008,active)
    if ref is None:
        name=kind if kind=="cylinder" else kind+("+" if side>0 else "-")
        ref=geom.chart_jet(name,s,v,0.,order,rotate=False)
    xx=J(*ref[:,:,0].T);zz=J(*ref[:,:,2].T)
    bumps=[geom.expj(-(((xx-cx)/.36)*((xx-cx)/.36)+((zz-cz)/.39)*((zz-cz)/.39))) for cx,cz in CART_CENTERS]
    terms=main+extra+[em*b for b in bumps]+[ee*b for b in bumps]
    block=np.zeros((n,6,count))
    for i,j in enumerate(terms):
        for k,q in enumerate(j.parts()):
            block[:,k,i]=q
    span=na*(nr+3)
    for i,(t,env) in enumerate(((x,em),(y,ee))):
        sel=np.flatnonzero(env.v!=0.)
        if not len(sel):
            continue
        def take(j):
            return J(*(np.broadcast_to(v,(n,))[sel] for v in j.parts()))
        tens=tensor_coords(take(u),take(t),period,na,nr)
        gate=J(*(v[:,None,None] for v in take(env).parts()))
        col=gcount+i*span
        for k,b in enumerate((gate*tens).parts()):
            block[sel,k,col:col+span]=b.reshape(len(sel),span)
    return block


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
            a,b=ref[:,1],ref[:,2];l=np.linalg.norm(a,axis=1)
            e1=a/l[:,None];proj=np.einsum("ni,ni->n",b,e1)
            perp=b-proj[:,None]*e1;perpl=np.linalg.norm(perp,axis=1)
            if np.any((l<=0)|(perpl<=0)):
                raise ArithmeticError("singular input reference chart; regular Cartesian core is evaluated separately")
            pa=(1/l)[:,None];pc=(1/perpl)[:,None];pb=-proj[:,None]*pa*pc
            raw.append(linjet(cur,pa,pb,pc));refs.append(linjet(ref,pa,pb,pc))
            for lo in range(0,len(s),160):
                sl=slice(lo,lo+160)
                h=physical_basis(kind,s[sl],v[sl],side,order,mode,M,N,ref[sl])
                h=linjet(h,pa[sl],pb[sl],pc[sl])
                bases.append(csr_matrix(h.reshape(-1,h.shape[-1])))
            sign=1 if kind=="cylinder" else side*(-1 if kind in ("cap","cap-cartesian") else 1)
            orient.append(np.full(len(s),sign));weights.append(np.full(len(s),1/np.sqrt(len(s))))
            blocks.append((name,nx,nx+len(s)));nx+=len(s)
        self.base=np.concatenate(raw);self.h=vstack(bases,format="csr");self.ref=np.concatenate(refs)
        self.w=np.concatenate(weights);self.ori=np.concatenate(orient);self.blocks=blocks
        self.center=np.array([m.section_center(order),0.,0.])
        self.p=self.h.shape[-1]
        self.cache_key=None;self.saved=None

    def state(self,x):
        key=x.tobytes()
        if key==self.cache_key:
            return self.saved
        field=self.base+(self.h@x.reshape(self.p,3)).reshape(-1,6,3)
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
            df=(h@col.reshape(p,3)).reshape(-1,6,3)
            return np.r_[np.einsum("nkac,nac->nk",der,df).ravel(),.0002*col]
        def rv(y):
            row=np.asarray(y).ravel();body=row[:-3*p].reshape(-1,6)
            normal=np.einsum("nk,nkac->nac",body,der)
            force=h.T@normal.reshape(-1,3)
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
                float(np.min(area[i:j])),*[float(np.max(np.abs(v[i:j]))) for v in (g[:,0,0]-1,g[:,0,1],g[:,1,1]-1)]]
        return values


def resize(x,prev,now):
    mn,nn=now;g,an,rn,count=layout(mn,nn);out=np.zeros((count,3))
    if x is None:
        return out
    mo,no=prev;go,ao,ro,_=layout(mo,no)
    a=x[:go-2*len(CART_CENTERS)].reshape(2,2*mo+1,no,3)
    b=out[:g-2*len(CART_CENTERS)].reshape(2,2*mn+1,nn,3)
    b[:,:2*mo+1,:no]=a
    out[g-2*len(CART_CENTERS):g]=x[go-2*len(CART_CENTERS):go]
    # Exact full-line cardinal-cubic refinement; discarded outer centers are
    # identically zero with their first two derivatives on the active interval.
    a=x[go:].reshape(2,ao,ro+3,3);b=out[g:].reshape(2,an,rn+3,3)
    mask=[1/8,4/8,6/8,4/8,1/8]
    for i in range(ao):
        for j in range(-1,ro+2):
            for dx,wx in zip(range(-2,3),mask):
                for dy,wy in zip(range(-2,3),mask):
                    jy=2*j+dy
                    if -1<=jy<=rn+1:
                        b[:,(2*i+dx)%an,jy+1]+=wx*wy*a[:,i,j+1]
    return out


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
            print("R762 finished",mode,side,idx,ip,status,flush=True)
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
    sa,sb=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float));shape=sa.shape
    sa,sb=sa.ravel(),sb.ravel();j=posed(chart,sa,sb,ph,order,side)
    kind=chart if chart=="cylinder" else chart[:-1]
    for lo in range(0,len(sa),160):
        sl=slice(lo,lo+160)
        h=physical_basis(kind,sa[sl],sb[sl],side,order,mode,M,N)
        j[sl]+=h@c
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


def transport_audit(side):
    """Independent gauge-only experiment; compares the same original labelled cap before either shape fit."""
    records=[];chart="cap"+("+" if side>0 else "-")
    phases=sorted(set(PHASES)|{(a+b)/2 for a,b in zip(PHASES[:-1],PHASES[1:])})
    for level in LEVELS:
        n,k,order,_,_,_,_,an,ak=level
        half=p.material(order,True)[-1]
        # Include end guards, four full transition edges and independently shifted interiors.
        s=2*half*(np.arange(an)+.37)/an
        z=np.unique(np.r_[0.,1.,transport.GUARDS,(np.arange(ak+1)+.43)/(ak+1)])
        ss,zz=np.meshgrid(s,z,indexing="ij");ss=ss.ravel();zz=zz.ravel()
        vv=transport.LEFT+transport.SPAN*zz
        target=geom.chart_jet(chart,ss,vv,0.,order,rotate=False)
        a,b=target[:,1],target[:,2]
        pa=1/np.linalg.norm(a,axis=1);e1=pa[:,None]*a
        proj=np.einsum("ni,ni->n",b,e1);perp=b-proj[:,None]*e1;pc=1/np.linalg.norm(perp,axis=1);pb=-proj*pa*pc
        def met(cur):
            ta=pa[:,None]*cur[:,1];tb=pb[:,None]*cur[:,1]+pc[:,None]*cur[:,2]
            d11=np.einsum("ij,ij->i",ta,ta)-1
            d12=np.einsum("ij,ij->i",ta,tb)
            d22=np.einsum("ij,ij->i",tb,tb)-1
            gvv=np.sum(cur[:,2]**2,axis=1)/np.sum(b*b,axis=1)-1
            return [float(np.max(np.abs(q))) for q in (d11,d12,d22,gvv)]
        for ph in phases:
            before=original.posed(chart,ss,vv,ph,order,side)
            after=transport.posed(chart,ss,vv,ph,order,side)
            mapj=transport.map_jet(ss,vv,ph,order,side)
            # Stay strictly inside the true open guards, away from rounded endpoint comparisons.
            guards=(zz<transport.GUARDS[0])|(zz>transport.GUARDS[-1])
            base=np.zeros_like(mapj);base[:,0]=vv;base[:,2]=1.
            ids=np.max(np.abs(mapj[guards]-base[guards]))
            gs=np.max(np.abs(after[guards]-before[guards]))
            A,G,AI,GI,scale=transport.coefficients(s,ph,side,order)
            proxy_ratio=AI[0,:,-1]/transport.coefficients(s,0.,side,order)[2][0,:,-1]
            rec=[order,ph,len(vv),met(before),met(after),float(np.min(mapj[:,2])),float(np.max(mapj[:,2])),
                float(ids),float(gs),float(np.max(np.abs(AI[0,:,-1]-GI[0,:,-1]))),
                float(np.min(scale)),float(np.max(scale)),float(np.max(np.abs(proxy_ratio**2-1)))]
            records.append(rec)
            print("R762 gauge alone",side,order,ph,rec[3:8],flush=True)
    return {"schema":"R762-independent-transport-alone-before-shape-fit-v1","run":os.environ["GITHUB_RUN_ID"],
        "attempt":os.environ["GITHUB_RUN_ATTEMPT"],"source_commit":os.environ["R762_SOURCE_COMMIT"],"side":side,
        "metrics":["max_abs_frame11","max_abs_frame12","max_abs_frame22","max_abs_material_vv_relative"],
        "columns":["order","phase","points","before","after","min_phi_v","max_phi_v","guard_identity_max_sixjet",
        "guard_geometry_max_sixjet","primitive_total_gap","min_b","max_b","proxy_slicelength_obstruction_max"],
        "rows":records}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mode",choices=("outer_locked","free_end"),required=True)
    ap.add_argument("--side",choices=(-1,1),type=int,required=True)
    ap.add_argument("--folder",type=Path,required=True);ap.add_argument("--report",type=Path,required=True)
    arg=ap.parse_args();m.old.disk._public();arg.folder.mkdir(exist_ok=True,parents=True)
    if arg.mode=="outer_locked":
        obj=transport_audit(arg.side)
        arg.report.with_name(f"gauge-{arg.side}.json").write_text(json.dumps(obj,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n")
    rows,between=solve(arg.mode,arg.side,arg.folder)
    rec={"schema":"R762-positive-meridian-gauge-and-physical-tensor-fit-v1","mode":arg.mode,"side":arg.side,
         "run":os.environ["GITHUB_RUN_ID"],"attempt":os.environ["GITHUB_RUN_ATTEMPT"],
         "source_commit":os.environ["R762_SOURCE_COMMIT"],"rules_read_commit":os.environ["R762_RULES_COMMIT"],
         "levels":LEVELS,"local_tensor_sizes":LOCAL,"phases":PHASES,"rows":rows,"intermediate_phases":between,
         "whole_crown_SE3_knots":[[l[2],ph,knot_pose(l[2],arg.side,ph)[0].tolist(),knot_pose(l[2],arg.side,ph)[2]] for l in LEVELS for ph in PHASES],
         "original_actual_758_and_760_cartesian_tip":tip_audit(32,arg.side),
         "cap_radial_path_prices":[opposite_end_prices(i,arg.mode,arg.side,arg.folder) for i in range(len(LEVELS))],
         "chart_columns":["points","nearly_singular","relative_metric_max","max_abs_principal","min_support","min_relative_area","max_abs_relative_11","max_abs_relative_12","max_abs_relative_22"],
         "scope":"All five charts of this entire half-sphere, including the shared central half and the true regular Cartesian ellipse. All derivatives refer to the one curved R760 zero-phase target."}
    arg.report.write_text(json.dumps(rec,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n")


if __name__=="__main__":
    main()
