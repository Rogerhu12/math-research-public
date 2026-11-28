#!/usr/bin/env python3
"""Physical arclength normalization of both entire R780 rolls, including its true two transverse derivatives."""
from functools import lru_cache
import numpy as np
import r780_exact_bent_caps_and_closed_spatially_shifted_center as geom
from r742_tilted_disk_two_jets import J,gather,unary

old,m=geom.old,geom.m;E,OLD_L,L,T,B=geom.E,geom.OLD_L,geom.L,geom.T,geom.B
ACTIVE=E+OLD_L
SHAPES=((2,2),(3,3),(5,4))
TENS=(32,48,72)
GAUSS=(4,6,8)
def period(order):return 2*old.material(order,True)[-1]

def radial(v,order):
    # Scalar original p,d and true first two derivatives even at the old/new material joins.
    q=J(np.asarray(v),a=1.)
    a=unary(q,np.minimum(q.v,E),(q.v<=E).astype(float),0.)
    b=unary(q,np.maximum(0.,q.v-E),(q.v>E).astype(float),0.)
    pe,de=geom.base.initial_turn(a,order);pr,dr=geom.roll_offsets("round+",b,order)
    return pe+pr-geom.base.axial(order),de+dr

def basis(s,u,P,shape):
    f=2*np.pi*s/P;t=u/ACTIVE
    win=np.where((t>0)&(t<1),1.,0.)
    t=np.clip(t,0.,1.);v=t*(1-t);vp=1-2*t
    env=64*v**3
    d1=192*v*v*vp/ACTIVE
    d2=384*v*(vp*vp-v)/(ACTIVE**2)
    angular=[(np.ones_like(s),np.zeros_like(s),np.zeros_like(s))]
    for k in range(1,shape[0]+1):
        h=2*np.pi*k/P;cs=np.cos(k*f);sn=np.sin(k*f)
        angular.extend(((cs,-h*sn,-h*h*cs),(sn,h*cs,-h*h*sn)))
    radial=[]
    for k in range(shape[1]):
        h=np.pi*k/ACTIVE;cs=np.cos(np.pi*k*t);sn=np.sin(np.pi*k*t)
        radial.append((win*env*cs,win*(d1*cs-h*env*sn),win*(d2*cs-2*h*d1*sn-h*h*env*cs)))
    vals=[]
    for a,ap,app in angular:
        for b,bp,bpp in radial:vals.append(np.stack((a*b,ap*b,a*bp,app*b,ap*bp,a*bpp),axis=-1))
    return np.stack(vals,axis=-1)

def native(s,u,ph,order,mode,side,shape,coef):
    s,u=np.broadcast_arrays(s,u);sh=s.shape;s,u=s.ravel(),u.ravel()
    j=np.empty((len(s),6,3))
    sg="+" if side==1 else "-"
    for mask,ch,v in ((u<E,"preband",u),(u>=E,"round",u-E)):
        if np.any(mask):j[mask]=geom.chart_jet(ch+sg,s[mask],v[mask],ph,order,mode,False)
    if coef is not None:j+=basis(s,u,period(order),shape)@coef
    return j.reshape(sh+(6,3))

def scalar_speed(j):
    g,gu,gua,gaa,gvv=j[...,1,:],j[...,2,:],j[...,4,:],j[...,3,:],j[...,5,:]
    v=np.linalg.norm(g,axis=-1);safe=np.maximum(v,1e-14);t=g/safe[...,None]
    dot=lambda a,b:np.einsum("...i,...i->...",a,b)
    va=dot(t,gaa);vu=dot(t,gua)
    t_a=(gaa-va[...,None]*t)/safe[...,None]
    bulk=(dot(gua,gua)-vu*vu)/safe-dot(t_a,gvv)
    boundary=dot(t,gvv)
    return np.stack((v,vu,bulk),axis=-1),boundary,va

def original_angle(s,order):
    P=period(order);g=geom.c.stations(order)
    full,iv=np.unique(np.r_[g,P-g,np.mod(s,P),0.,P],return_inverse=True)
    _,tt,_,k,kp=old.data(full,0.,order,True)
    angle=np.unwrap(np.arctan2(tt[:,1],tt[:,0]))
    ix=np.searchsorted(full,np.mod(s,P));v=angle[0]-angle[ix]
    return J(v,k[ix],0.,kp[ix],0.,0.)

class Ring:
    def __init__(self,u,ph,order,mode,side,index,coef):
        self.u,self.ph,self.order,self.mode,self.side,self.shape,self.coef=u,ph,order,mode,side,SHAPES[index],coef
        st=geom.c.stations(order);self.P=period(order)
        knots=np.unique(np.r_[st,self.P-st,np.linspace(0,self.P,TENS[index]+1)])
        self.grid=knots[np.r_[True,np.diff(knots)>1e-13]]
        self.nodes,self.weights=m.old.disk.rule(GAUSS[index])
        self.width=np.diff(self.grid)
        av=self.grid[:-1,None]+self.width[:,None]*self.nodes
        jet=self.field(av);vv,_,_=scalar_speed(jet)
        edge=self.field(self.grid);ev,bd,_=scalar_speed(edge)
        sums=self.width[:,None]*np.einsum("q,iqk->ik",self.weights,vv)
        self.pre=np.vstack((np.zeros(3),np.cumsum(sums,axis=0)))
        self.bound0=bd[0];self.length=self.pre[-1].copy();self.length[2]+=bd[-1]-bd[0]
        self.min_sampled_speed=float(min(vv[...,0].min(),ev[...,0].min()))
    def field(self,s):
        return native(s,np.full(np.shape(s),self.u),self.ph,self.order,self.mode,self.side,self.shape,self.coef)
    def integrals(self,a):
        ix=np.clip(np.searchsorted(self.grid,a,side="right")-1,0,len(self.grid)-2)
        h=a-self.grid[ix];v=self.grid[ix,None]+h[:,None]*self.nodes
        quad=self.field(v);data,_,_=scalar_speed(quad)
        parts=self.pre[ix]+h[:,None]*np.einsum("q,iqk->ik",self.weights,data)
        f=self.field(a);vel,bd,va=scalar_speed(f);parts[:,2]+=bd-self.bound0
        return parts,f,vel,va
    def evaluate(self,s):
        P=self.P;raws=np.mod(s,P);p,d=radial(np.asarray(self.u),self.order)
        # d depends only on the transverse variable; K0 is the true unwrapped turning primitive.
        ell0=P-2*np.pi*d;ell=J(self.length[0],a=self.length[1],aa=self.length[2])
        I0=J(raws,s=np.ones_like(raws))-d*original_angle(raws,self.order)
        right=I0*ell/ell0
        target=right.v;a=np.interp(target,self.pre[:,0],self.grid)
        lo=np.zeros_like(a);hi=np.full_like(a,P)
        for _ in range(9):
            parts,f,vel,va=self.integrals(a);err=parts[:,0]-target
            if np.max(abs(err))<2e-13:break
            hi=np.where(err>0,a,hi);lo=np.where(err<0,a,lo)
            upd=a-err/np.maximum(vel[:,0],1e-14)
            a=np.where((upd>=lo)&(upd<=hi),upd,.5*(lo+hi))
        parts,f,vel,va=self.integrals(a)
        speed=np.maximum(vel[:,0],1e-14);vu=vel[:,1]
        ss=right.s/speed;su=(right.a-parts[:,1])/speed
        sss=(right.ss-va*ss**2)/speed
        ssu=(right.sa-va*ss*su-vu*ss)/speed
        suu=(right.aa-parts[:,2]-2*vu*su-va*su*su)/speed
        rat=ell0/ell
        C=(J(m.section_center(self.order)),self.side*(B+p),J(0.))
        out=[]
        for i in range(3):
            val,fa,fu,faa,fau,fuu=f[:,:,i].T
            v=J(val,fa*ss,fa*su+fu,faa*ss*ss+fa*sss,
                faa*ss*su+fau*ss+fa*ssu,faa*su*su+2*fau*su+fuu+fa*suu)
            out.append(C[i]+rat*(v-C[i]))
        return gather(out,len(s)),[float(np.max(abs(parts[:,0]-target))),self.min_sampled_speed,
                                   float(ell.v),float(ell0.v),float(rat.v)]

class PhysicalRoll:
    def __init__(self,ph,order,mode,index,coeff):
        self.ph,self.order,self.mode,self.index,self.coeff=ph,order,mode,index,coeff
        self.cache={};self.diagnostics={}
    def jet(self,ch,s,v,rotate=False):
        if not self.ph or ch=="cylinder" or ch.startswith("cap"):
            return geom.chart_jet(ch,s,v,self.ph,self.order,self.mode,rotate)
        s,v=np.broadcast_arrays(s,v);sh=s.shape;s,v=s.ravel(),v.ravel()
        u=v+(E if ch.startswith("round") else 0.)
        sign=1 if ch.endswith("+") else -1;j=np.empty((len(s),6,3))
        edge=(u==0)|(u>=ACTIVE-1e-14)
        if np.any(edge):
            j[edge]=geom.chart_jet(ch,s[edge],v[edge],self.ph,self.order,self.mode,False)
        for t in np.unique(u[~edge]):
            k=(sign,float(t));mask=u==t
            if k not in self.cache:self.cache[k]=Ring(float(t),self.ph,self.order,self.mode,sign,self.index,self.coeff[sign])
            j[mask],diag=self.cache[k].evaluate(s[mask]);self.diagnostics[k]=diag
        if rotate:
            ax=np.asarray(m.axis(self.order));p=j[:,:,[0,2]].copy();p[:,0]-=ax
            p=geom.c.oldgeom.parent.rot(p,self.ph);p[:,0]+=ax;j[:,:,0]=p[:,:,0];j[:,:,2]=p[:,:,1]
        return j.reshape(sh+(6,3))
