"""Full-shell finite readout including actual rigid hats, prescribed bands and annuli."""
import numpy as np
from scipy.spatial import cKDTree

from r688_actual_r664_window_collars import active_width
from r688_true_caps_and_reference_sections import D, EPS_CAP, W, implicit, radial_zero

SUPPORT=np.array([.003,.003,np.sqrt(1-2*.003**2)])
REFLECT=np.array([-1.,1.,1.])


def unit(v):
    return v/np.maximum(1e-140,np.linalg.norm(v,axis=-1))[...,None]


def normal_and_curvature(a,b,aa,ab,bb):
    N=unit(np.cross(a,b))
    G=np.stack((np.sum(a*a,axis=-1),np.sum(a*b,axis=-1),np.sum(b*b,axis=-1)),axis=-1)
    g,f,h=np.moveaxis(G,-1,0)
    det=g*h-f*f
    d,e,k=[np.sum(v*N,axis=-1) for v in (aa,ab,bb)]
    H=(d*h+k*g-2*e*f)/(2*np.maximum(det,1e-30))
    K=(d*k-e*e)/np.maximum(det,1e-30)
    maximum=abs(H)+np.sqrt(np.maximum(0,H*H-K))
    scale=np.maximum(g*h,1e-30)
    return N,maximum,np.maximum(det,0)/scale,G


def vec3(x,y,z):
    return np.stack(np.broadcast_arrays(x,y,z),axis=-1)


class KnownBody:
    def __init__(self,ref,res):
        nphi,resv=res,2*res+1
        phi=2*np.pi*np.arange(nphi)/nphi
        theta=np.linspace(0,np.pi,resv)
        th,ph=np.meshgrid(theta,phi,indexing='ij')
        rays=vec3(np.sin(th)*np.cos(ph),np.cos(th),np.sin(th)*np.sin(ph))
        p=radial_zero(rays,np.array([0,.02,0]))
        norm=unit(implicit(p)[1]); cap=p+.12*norm
        inside=cap[...,1]>=0
        self.cap=cap[inside]; self.cap_n=norm[inside]
        th,ph=np.meshgrid(np.linspace(np.arccos(.25),np.pi,resv),phi,indexing='ij')
        crown_n=vec3(-np.cos(th),np.sin(th)*np.cos(ph),np.sin(th)*np.sin(ph))
        self.crown=(np.array([.96,0,0])+.11*crown_n).reshape(-1,3)
        self.crown_n=crown_n.reshape(-1,3)
        w,ph=np.meshgrid(np.linspace(0,.001,15),phi,indexing='ij')
        th,ax,rad=ref.crown(w.ravel()).reshape((3,)+w.shape)
        sh=vec3(.96-ax,rad*np.cos(ph),rad*np.sin(ph))
        sn=vec3(-np.cos(th),np.sin(th)*np.cos(ph),np.sin(th)*np.sin(ph))
        self.crown=np.vstack((self.crown,sh.reshape(-1,3)))
        self.crown_n=np.vstack((self.crown_n,sn.reshape(-1,3)))
        vs=np.r_[np.linspace(-1,1,2*res+1),np.linspace(-.925,-.60,res),np.linspace(.60,.925,res)]
        self.v=np.unique(vs)
        self.u=np.linspace(-W,W,2*res//3+1)
        self.ref=ref
        # Both curved fixed shoulders; sample all around the cap by reflecting
        # its right half, plus the flat seats (provided by the wide sheets).
        g_knots=np.unique(np.r_[np.linspace(0,EPS_CAP,31),.00001,.00024,.02278,.02301])
        arc_knots=np.unique(np.r_[np.linspace(-ref.S,ref.S,res*4+1),
                                   ref.S-np.linspace(0,.003,11),-ref.S+np.linspace(0,.003,11)])
        w,sa=np.meshgrid(g_knots,arc_knots,indexing='ij')
        X,dw,ds,dww,dws,dss=ref.shoulder_jets(w,sa)
        self.primary_shoulder=X.reshape(-1,3)
        _,shoulder_k,shoulder_sine,_=normal_and_curvature(dw,ds,dww,dws,dss)
        self.primary_shoulder_max_abs_principal=float(np.max(shoulder_k))
        self.primary_shoulder_min_sine=float(np.min(shoulder_sine))
        self.primary_shoulder_n=unit(np.cross(dw,ds)).reshape(-1,3)

    def cloud(self,line,collars,h,crown_shift):
        p=[]; n=[]
        def add(X,N,mirror=False):
            X=X.reshape(-1,3); N=N.reshape(-1,3)
            p.append(X); n.append(N)
            if mirror:
                p.append(X*REFLECT); n.append(N*REFLECT)
        for side in (-1,1):
            _,y,z=line.fields(np.array([side]))
            orient=np.array([1.,side,1.])
            shift=np.array([0.,y.item(),z.item()])
            add(self.cap*orient+shift,self.cap_n*orient)
            add(self.primary_shoulder*orient+shift,self.primary_shoulder_n*orient,True)
        add(self.crown+crown_shift,self.crown_n,True)
        v,u=np.meshgrid(self.v,self.u,indexing='ij')
        al,y,z=line.fields(v)
        for side in (-1,1):
            add(vec3(u,y,z+side*D),vec3(0,-np.sin(al),np.cos(al))*side)
            for coll in collars:
                vs=np.linspace(-.90,-.62,len(self.v))
                if coll.sign<0:
                    vs=-vs
                t,v=np.meshgrid(np.linspace(0,1,5),vs,indexing='ij')
                t=t*active_width(v,h)
                X,a,b,*_=coll.position_jets(t,v)
                X[...,2]+=side*D
                add(X,unit(np.cross(a,b))*side,True)
            # Restore local variable overwritten by collar-grid construction.
            v,u=np.meshgrid(self.v,self.u,indexing='ij')
        return np.concatenate(p),np.concatenate(n)


def normal_chords(P,N,tau,source,labels):
    # Stream all unordered pairs in range and both normal directions. At a
    # duplicated geometry node preserve both normals and record multiplicity.
    tree=cKDTree(P)
    worst=0.; coincident=0; distinct=0; worst_pair=None; intrinsic=0.; intrinsic_pair=None
    for first in range(0,len(P),128):
        rows=tree.query_ball_point(P[first:first+128],2*tau)
        for i,idx in enumerate(rows,first):
            idx=np.asarray(idx,int); idx=idx[idx>i]
            if not len(idx):
                continue
            d=P[idx]-P[i]; dd=np.sum(d*d,axis=1)
            good=dd>1e-24
            coincident+=int(np.sum(~good))
            if np.any(~good):
                distinct+=int(np.sum(np.linalg.norm(labels[idx[~good]]-labels[i],axis=1)>1e-7))
            length=np.sqrt(dd)
            d0=np.linalg.norm(source[idx]-source[i],axis=1)
            projection=(np.sqrt(1-1e-6)*d0*(1-length/(2*tau))-length)/tau
            top=np.argmax(projection)
            if projection[top]>intrinsic:
                intrinsic=float(projection[top]); intrinsic_pair=[i,int(idx[top])]
            if not np.any(good):
                continue
            d,dd,idx=d[good],dd[good],idx[good]
            ratio=2*tau*np.maximum(abs(d@N[i]),abs(np.sum(d*N[idx],axis=1)))/dd
            j=np.argmax(ratio)
            if ratio[j]>worst:
                worst=float(ratio[j]); worst_pair=[i,int(idx[j])]
    return dict(max_two_sided_normal_chord_ratio=worst,attaining_pair=worst_pair,
                sampled_projected_chord_excess=intrinsic,projected_chord_pair=intrinsic_pair,
                coincidences_at_geometry_tolerance=coincident,coincidences_with_distinct_undeformed_reference_positions=distinct)
