"""A genuine isometric bending of the entire R781 right disk, fixed on its central open grip."""
from functools import lru_cache
import numpy as np
import r781_round_three_lobe_spatial_rings as ref
from r742_tilted_disk_two_jets import J,unary,trig,cap_s7,gather

START=.18
WIDTH=.14

def heading(x,b):
    p,dp,ddp=ref.clock((x-START)/WIDTH)
    return b*p,b*dp/WIDTH,b*ddp/WIDTH**2

@lru_cache(maxsize=160)
def table(b,order):
    cuts=START+WIDTH*np.array([0.,ref.ROUND,1-ref.ROUND,1.])
    n,w=ref.rule(order);d=np.diff(cuts);h=heading(cuts[:-1,None]+d[:,None]*n,b)[0]
    return cuts,np.vstack((np.zeros(2),np.cumsum(d[:,None]*np.c_[(-2*np.sin(h/2)**2)@w,np.sin(h)@w],axis=0)))

def displacements(x,b,order):
    cuts,tab=table(b,order);q=np.clip(x.v,cuts[0],cuts[-1])
    ix=np.clip(np.searchsorted(cuts,q,side="right")-1,0,len(cuts)-2)
    h=q-cuts[ix];n,w=ref.rule(order);a=heading(cuts[ix,None]+h[:,None]*n,b)[0]
    zz=tab[ix]+h[:,None]*np.c_[(-2*np.sin(a/2)**2)@w,np.sin(a)@w]
    ext=np.maximum(x.v-cuts[-1],0.)
    zz[:,0]-=ext*2*np.sin(b/2)**2;zz[:,1]+=ext*np.sin(b)
    ang,k,kp=heading(x.v,b);c,s=trig(unary(x,ang,k,kp))
    dx=unary(x,zz[:,0],-2*np.sin(ang/2)**2,-k*s.v)
    dy=unary(x,zz[:,1],s.v,k*c.v)
    return dx,dy,c,s

def transform(F,t,amplitude,order):
    if not amplitude or not t:return F
    shape=F.shape;a=F.reshape(-1,6,3);X,Y,Z=[J(*a[:,:,j].T) for j in range(3)]
    ytop=.5+ref.end_limits(order)[0]
    h=Y-ytop
    dx,dy,c,s=displacements(X,float(amplitude)*np.sin(t)**2,order)
    gate=cap_s7((Y-.36)/.165)
    out=gather([X+gate*(dx-h*s),Y+gate*(dy+h*(c-1)),Z],len(a))
    return out.reshape(shape)
