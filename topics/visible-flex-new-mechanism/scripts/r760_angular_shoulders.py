"""Three-axis angular controls on the actual native w transitions missed by the R750 work mesh."""
import numpy as np
from scipy.sparse import csr_matrix

import r750_rigid_annulus as parent

PANELS=((.206,'rise'),(.206,'fall'),(.847,'rise'),(.847,'fall'))


def interval(c,edge):
    return (c-.0005,c-.0003) if edge=='rise' else (c+.1003,c+.1005)


def extra_tags(degree):
    radial=(0,) if degree==3 else (0,1,2,3)
    return [('actual_native_w_flank',i,side,sign,c,edge,parity)
            for i in radial for side in (0,2) for sign in (-1,1)
            for c,edge in PANELS for parity in (0,1)]


def tags(degree):return parent.tags(degree)+extra_tags(degree)


def padded(q,old,new):
    oldq=dict(zip(tags(old),np.asarray(q).reshape(-1,3),strict=True))
    return np.asarray([oldq.get(t,np.zeros(3)) for t in tags(new)]).ravel()


def radial_shapes(ell,er):
    a=parent.early.FORCED_END
    b=parent.FREE_END
    up,du=parent.flat_step((ell-a)/.01)
    down,dd=parent.flat_step((b-ell)/.032)
    env=up*down
    dev=du*down/.01-up*dd/.032
    ans=[(env,er*dev)]
    for center,half in ((.188,.14),(.326,.14),(.464,.14)):
        t=(ell-center)/half
        mid=abs(t)<1
        val=np.where(mid,(1-t*t)**3,0.)
        d=np.where(mid,-6*t*(1-t*t)**2/half,0.)
        ans.append((env*val,er*(dev*val+env*d)))
    return ans


def appended(build,degree,r,s,derivatives=True):
    flat_s=np.asarray(s).ravel();n=len(flat_s)
    ell,er,_=parent.space.ell_data(np.asarray(r).ravel())
    _,kind,v=build.ring.label(flat_s)
    v_sigma=np.where(kind==0,build.ring.length,np.where(kind==2,-build.ring.length,0.))
    rad=radial_shapes(ell,er)
    m=extra_tags(degree);B=np.zeros((n,len(m)))
    if derivatives:Br=np.zeros_like(B);Bs=np.zeros_like(B)
    for col,(_,i,side,sign,c,edge,odd) in enumerate(m):
        a,b=interval(c,edge)
        raw=(sign*v-a)/(b-a);active=(kind==side)&(raw>0)&(raw<1)
        if not np.any(active):continue
        t=raw[active];v0=64*(t*(1-t))**3
        v1=192*(t*(1-t))**2*(1-2*t)
        g=v0*(2*t-1) if odd else v0
        B[active,col]=rad[i][0][active]*g
        if derivatives:
            dg=(v1*(2*t-1)+2*v0) if odd else v1
            Br[active,col]=rad[i][1][active]*g
            Bs[active,col]=rad[i][0][active]*dg*sign*v_sigma[active]/(b-a)
    return (B,Br,Bs) if derivatives else csr_matrix(B)


def install(frame,build):
    B,Br,Bs=appended(build,frame.degree,frame.r,frame.s)
    frame.B=np.column_stack((frame.B,B));frame.Br=np.column_stack((frame.Br,Br))
    frame.Bs=np.column_stack((frame.Bs,Bs));frame.ncols=3*frame.B.shape[1]
    frame.q0=np.zeros(frame.ncols)


def true_angles(build,purpose):
    f={'train':.5,'validation':.319,'qualification':.173}[purpose]
    cells=np.array([0.,.25,.5,.75,1.])
    t=np.unique(np.r_[cells,cells[:-1]+f*np.diff(cells)])
    pos=np.concatenate([a+(b-a)*t for a,b in (interval(c,side) for c,side in PANELS)])
    v=np.r_[pos,-pos];r=build.ring
    return np.unique(np.mod(np.r_[(v+1)/r.length,(3+r.LU-v)/r.length],1.))
