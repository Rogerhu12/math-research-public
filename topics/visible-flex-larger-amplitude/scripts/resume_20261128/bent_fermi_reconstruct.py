"""Reconstruct an actual seam-clamped periodic map of the fixed R752 domain."""
from types import SimpleNamespace
import numpy as np
import bent_hard_end_fields as hf
import bent_end_phase_fields as base
from r742_tilted_disk_two_jets import J,gather

def angular(s,P,n):
    a=base.scalar(s);a[:,1]=1.;out=[base.scalar(np.ones(len(s)))]
    for k in range(1,n+1):
        f=2*np.pi*k/P;c=np.cos(f*s);ss=np.sin(f*s)
        out.extend((base.unary(a,c,-f*ss,-f*f*c),base.unary(a,ss,f*c,-f*f*ss)))
    return out

def mat(s,v,P,L,na,nr,jet=False):
    s=np.asarray(s);v=np.asarray(v);w=base.scalar(v/L);w[:,2]=1./L
    one=base.scalar(np.ones(len(s)));t=base.mul(w,one-w)
    e2=16*base.mul(t,t);e3=4*base.mul(t,e2)
    r=base.cheb(2*w-one,nr);a=angular(s,P,na)
    if jet:return r,a,e2,e3,t
    R=np.stack([z[:,0] for z in r],axis=1);A=np.stack([z[:,0] for z in a],axis=1)
    B=(R[:,:,None]*A[:,None,:]).reshape(len(s),-1)
    return B,e2[:,0],e3[:,0],t[:,0]

def fit(shoot,tr,cfg):
    times=tr[:,:,:,2];T=times[-1];L=shoot.L;P=shoot.P
    alpha=np.broadcast_to(shoot.launch,(len(shoot.clock),len(shoot.launch)))
    b=np.broadcast_to(shoot.clock[:,None],alpha.shape)
    weights=np.sqrt(np.r_[np.diff(shoot.clock)/2,0]+np.r_[0,np.diff(shoot.clock)/2])
    vals=[];read=[];na=cfg["map_fourier"];nr=cfg["map_radial"]
    for side in range(2):
        v=L*times[:,side]/np.maximum(T[side],1.e-12);v=np.clip(v,0,L)
        aa=tr[:,side,:,0]
        B,e2,e3,tt=mat(alpha.ravel(),v.ravel(),P,L,na,nr)
        W=np.broadcast_to(weights[:,None],v.shape).ravel()
        raw=(b-v).ravel()/(L*np.maximum(tt,1.e-12))
        target=np.arctanh(np.clip(raw,-.99,.99));qs=[];cost=[]
        for gate,y in [(e3,(aa-alpha).ravel()),(e2,target)]:
            M=B*(gate*W)[:,None];rhs=y*W
            # Ridge regularizes the numerical fit, never alters the independent target metric.
            rhs=M.T@rhs;G=M.T@M
            scale=cfg["map_ridge"]*max(1.,float(np.trace(G)/len(G)))
            q=np.linalg.solve(G+scale*np.eye(len(G)),rhs);qs.append(q)
            cost.append(float(abs((B@q)*gate-y).max()))
        vals.append(qs);read.append({"max_fit_coordinate_error":cost,"radial_inverse_tanh_clips":int((abs(raw)>.99).sum())})
    return np.array(vals),read

def mapjet(s,v,P,L,na,nr,coeff):
    r,a,e2,e3,t=mat(s,v,P,L,na,nr,True)
    # Separable contraction of two scalar jets for both displacement channels.
    R=np.stack(r,axis=-1);A=np.stack(a,axis=-1)
    C=coeff.reshape(2,len(r),len(a))
    def contracted(i,j):
        return np.einsum("nr,cra,na->cn",R[:,i],C,A[:,j],optimize=True)
    out=np.stack([contracted(0,0),contracted(0,1),contracted(2,0),
                  contracted(0,3),contracted(2,1),contracted(5,0)],axis=-1)
    aa=base.scalar(s);aa[:,1]=1.;aa+=base.mul(e3,out[0])
    rho=base.mul(e2,out[1]);z=np.tanh(rho[:,0]);D=1-z*z
    bb=base.scalar(v);bb[:,2]=1.;bb+=L*base.mul(t,base.unary(rho,z,D,-2*z*D))
    return J(*aa.T),J(*bb.T)

def evaluate(src,d,cfg,z,q,chart,u,v,phase,world=True,read_det=False):
    aa,bb=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float));sh=aa.shape
    s,v=aa.ravel(),bb.ravel();D=src.delay;P=2*src.OLD.profile_constants(32)[4]
    shape=hf.hshape(src,d,z[:hf.HARD]);res=[];det=[]
    if not chart.startswith("end"):
        f=src.chart_jet(chart,s,v,phase,shape=shape,method=d["method"],rotate=world)
        rr=f.reshape(sh+(6,3))
        return (rr,np.ones(sh)) if read_det else rr
    side=0 if chart=="end+" else 1
    for first in range(0,len(s),1000):
        ii=slice(first,first+1000)
        a,b=mapjet(s[ii],v[ii],P,D.END_LENGTH,cfg["map_fourier"],cfg["map_radial"],q[side])
        det.append(a.s*b.a-a.a*b.s)
        f=src.chart_jet(chart,a.v,b.v,phase,shape=shape,method=d["method"],rotate=False)
        fake=SimpleNamespace(xy=np.column_stack((a.v,b.v)),delay=D,g=src.OLD,roll=[slice(None)])
        B=hf.Basis(fake,cfg)
        c=z[hf.HARD:].reshape(2,B.m,3)[side]
        f=f+(B.B@c).transpose(1,0,2)
        jets=src.compose2(a,b,*[f[:,j] for j in range(6)])
        x,y,zz=jets
        if world:
            ox,oz=src.AX.axis(32);co,si=np.cos(phase),np.sin(phase);X=x-ox;Z=zz-oz
            x,zz=ox+co*X-si*Z,oz+si*X+co*Z
        res.append(gather((x,y,zz),len(a.v)))
    rr=np.concatenate(res).reshape(sh+(6,3))
    return (rr,np.concatenate(det).reshape(sh)) if read_det else rr

def whole(m,d,cfg,z,q,t):
    f=[];det=[]
    for chart,u,v,sl in m.cases:
        a,b=evaluate(m.src,d,cfg,z,q,chart,u,v,t,False,True)
        f.append(a);det.append(b)
    return np.concatenate(f),np.concatenate(det)
