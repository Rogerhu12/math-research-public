"""R757 true unit-speed closed section: every former open straight segment is bowed."""
from functools import lru_cache
import numpy as np
from numpy.polynomial import Polynomial
import r744_extruded_closed_two_jets as original
import r747_offset_arclength_closed_two_jets as origangle
import r746_axial_translation_closed_two_jets as oldaxis
from r742_tilted_disk_two_jets import J,unary

disk=original.disk;turn=original.turn;END_LENGTH=original.END_LENGTH
END_TURN=original.END_TURN;END_BLEND=original.END_BLEND
CENTER_X=original.CENTER_X;PLANAR_TURN=original.PLANAR_TURN;PLANAR_BLEND=original.PLANAR_BLEND
CELL_MAX=.12
BOW=.04
profile_polynomial=Polynomial((0.,4.,-4.))**5
DER=tuple(profile_polynomial.deriv(j) for j in range(5))

def shape(t,j):
    # Endpoint-stable product form via symmetry; use the polynomial only on half the interval.
    u=np.minimum(t,1.-t)
    return DER[j](u)*np.where(t<=.5,1.,(-1.)**j)

def arc_extra(t,ell,order):
    nodes,wt=disk.rule(order)
    # Split at 1/2 for the reflected polynomial representation.
    out=np.zeros_like(t)
    for lo,hi in ((0.,.5),(.5,1.)):
        w=np.clip(t-lo,0.,hi-lo)
        a=BOW*ell[:,None]*shape(lo+w[:,None]*nodes,1)
        out+=ell*w*((a*a/(np.sqrt(1+a*a)+1))@wt)
    return out

@lru_cache(maxsize=None)
def atlas(order=32):
    lh,m0,m1,rtop,half,*_=original.profile_constants(order)
    P=2*half
    top=[(0.,lh),(m0,m0+1+disk.HOLD),(m0+1+disk.HOLD+disk.BEND,m1),(rtop,half)]
    spans=sorted([*top,*[(P-b,P-a) for a,b in top]])
    all_knots=[0.,P]
    for a,b in spans:
        all_knots.extend(np.linspace(a,b,int(np.ceil((b-a)/CELL_MAX))+1))
    knots=np.unique(all_knots);ell=np.diff(knots);mid=.5*(knots[1:]+knots[:-1])
    live=np.array([any(a<t<b for a,b in spans) for t in mid])
    ds=ell.copy();ds[live]+=arc_extra(np.ones(live.sum()),ell[live],order)
    new=np.r_[0.,np.cumsum(ds)];mid=int(np.searchsorted(knots,half))
    if len(knots)==2*mid+1 and knots[mid]==half:
        new[mid:]=2*new[mid]-new[:mid+1][::-1]
    return knots,new,live

def forward(a,order=32):
    old,new,active=atlas(order);q=np.asarray(a,float);sh=q.shape;q=q.ravel()
    lap=np.floor(q/old[-1]);u=q-lap*old[-1]
    i=np.clip(np.searchsorted(old,u,side="right")-1,0,len(active)-1)
    l=old[i+1]-old[i];t=np.clip((u-old[i])/l,0,1);f=active[i]
    value=new[i]+l*t
    if np.any(f):value[f]+=arc_extra(t[f],l[f],order)
    return (value+lap*new[-1]).reshape(sh)

def local(s,order):
    old,new,active=atlas(order);ss=np.asarray(s,float);sh=ss.shape;ss=ss.ravel()
    lap=np.floor(ss/new[-1]);a=ss-lap*new[-1]
    i=np.clip(np.searchsorted(new,a,side="right")-1,0,len(active)-1)
    l=old[i+1]-old[i];off=a-new[i];t=np.clip(off/l,0.,1.);f=active[i]
    if np.any(f):
        tt=t[f];le=l[f]
        for _ in range(5):
            err=le*tt+arc_extra(tt,le,order)-off[f]
            sp=np.sqrt(1+(BOW*le*shape(tt,1))**2)
            tt=np.clip(tt-err/(le*sp),0.,1.)
        t[f]=tt
    a0=lap*old[-1]+old[i]+t*l
    vals=[np.where(f,BOW*l**(2-j)*shape(t,j),0.) for j in range(5)]
    return sh,a0,f,l,vals

def profile_coordinates(s,order=32):
    sh,a0,live,l,(f,fp,fpp,f3,f4)=local(s,order)
    q,T,N,ko,kpo=original.profile_coordinates(a0,order)
    v=1+fp*fp
    point=q+f[:,None]*N;tang=(T+fp[:,None]*N)/np.sqrt(v)[:,None]
    n=np.stack((-tang[:,1],tang[:,0]),axis=1)
    k=np.where(live,-fpp/v**1.5,ko)
    kp=np.where(live,-f3/v**2+3*fp*fpp*fpp/v**3,kpo)
    return point.reshape(sh+(2,)),tang.reshape(sh+(2,)),n.reshape(sh+(2,)),k.reshape(sh),kp.reshape(sh)

def angular_data(s,order):
    sh,a0,live,l,(f,fp,fpp,f3,f4)=local(s,order)
    theta,k,kp=origangle.angular_data(a0,order);v=1+fp*fp
    return ((theta-np.arctan(fp)).reshape(sh),np.where(live,-fpp/v**1.5,k).reshape(sh),
          np.where(live,-f3/v**2+3*fp*fpp*fpp/v**3,kp).reshape(sh))

def curvature_atoms(s,order=32):
    sh,a0,live,l,(f,p,q,r,h)=local(s,order);v=1+p*p
    k=-q/v**1.5
    k1=-r/v**2+3*p*q*q/v**3
    k2=-h/v**2.5+(10*p*q*r+3*q**3)/v**3.5-18*p*p*q**3/v**4.5
    return [z.reshape(sh) for z in (l*l*k,l*l*k1,l*l*k2)]

def profile(u,order):
    q,T,n,k,kp=profile_coordinates(u.v,order)
    return ([unary(u,q[:,i],T[:,i],-k*n[:,i]) for i in range(2)],
            [unary(u,n[:,i],k*T[:,i],kp*T[:,i]-k*k*n[:,i]) for i in range(2)])

@lru_cache(maxsize=None)
def profile_constants(order=32):
    p=list(original.profile_constants(order))
    p[:5]=forward(np.array(p[:5]),order).tolist()
    return tuple(p)

def axis(order=32):return oldaxis.axis(order)
def grip_arclength(a,order=32):return forward(oldaxis.grip_arclength(a,order),order)
slice_j=original.slice_j

def profile_nodes(g,n,off):
    # Complete moving curvature cells in their true new material arclength.
    from bent_body_atlas import profile_nodes as parent_nodes
    base=np.asarray(parent_nodes(original,n,off));o,x,active=atlas(32)
    sub=max(2,min(12,int(np.ceil(n/18))))
    t=(np.arange(sub)+(.37 if off else 0))/sub
    old_grid=np.r_[base,o[:-1],(o[:-1][active,None]+np.diff(o)[active,None]*t).ravel()]
    xx=np.mod(forward(old_grid),x[-1])
    xx[(xx<3.e-12)|(x[-1]-xx<3.e-12)]=0.
    nodes=np.unique(np.round(xx,12))
    return nodes[np.r_[True,np.diff(nodes)>3.e-12]]
