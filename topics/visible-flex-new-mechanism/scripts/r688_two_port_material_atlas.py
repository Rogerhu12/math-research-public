"""Real crown-to-primary annular material chart and phase-dependent port data."""
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.sparse import csr_matrix
from scipy.optimize import brentq
from scipy.spatial.transform import Rotation

from r688_actual_r664_window_collars import active_width, band, smooth
from r688_true_caps_and_reference_sections import D, EPS_CAP, HOLE, W


def differentiate(nodes, order, periodic=False):
    n=len(nodes)
    A=np.zeros((n,n))
    for j in range(n):
        if periodic:
            idx=np.arange(j-2,j+3)%n
            x=(nodes[idx]-nodes[j]+np.pi)%(2*np.pi)-np.pi
        else:
            i=np.clip(j-2,0,n-5)
            idx=np.arange(i,i+5); x=nodes[idx]-nodes[j]
        scale=np.max(abs(x))
        rhs=np.zeros(5); rhs[order]=1 if order==1 else 2
        A[j,idx]=np.linalg.solve((x/scale)[None,:]**np.arange(5)[:,None],rhs)/scale**order
    return A


def separated(points, tol):
    ans=[]
    for u in sorted(points):
        if not ans or u-ans[-1]>tol:
            ans.append(u)
    return np.array(ans)


def frame(a,b):
    e=a/np.linalg.norm(a,axis=-1)[...,None]
    n=np.cross(e,b)
    n/=np.linalg.norm(n,axis=-1)[...,None]
    return np.stack((e,np.cross(n,e),n),axis=-1)


def rotation(vectors):
    return Rotation.from_rotvec(vectors.reshape(-1,3)).as_matrix().reshape(vectors.shape[:-1]+(3,3))


def step_vec(M):
    return Rotation.from_matrix(M.reshape(-1,3,3)).as_rotvec().reshape(M.shape[:-2]+(3,))


def softmax2(a,b,eps):
    diff=abs(a-b); v=np.minimum(diff/eps,1.)
    soft=np.where(diff>=eps,diff,eps*(3+6*v*v-v**4)/8)
    return (a+b+soft)/2


class MaterialAtlas:
    def __init__(self, ref, source, angular, rings, h, shift):
        self.ref,self.h,self.source=ref,h,source
        self.L=.22
        self.end=ref.meridian_end+self.L
        material=np.linspace(-1.,1.,16001)
        _,yy,zz=source.fields(material)
        self.inv=CubicSpline(yy,material,extrapolate=False)
        self.vstar=brentq(lambda v:float(source.fields(np.asarray(v))[1]),0.,.001,xtol=5e-16)
        self.Ylo,self.Yhi=yy[0],yy[-1]
        self.Zlo,self.Zhi=zz[0],zz[-1]
        def ysz(v):
            _,y,z=source.fields(np.atleast_1d(v))
            return y,z
        angles=list(2*np.pi*(np.arange(angular)+shift)/angular)
        outer_arc=ref.S+.00025
        for v in [-1+EPS_CAP/2,-.93,-.90,-.89,-.88,-.64,-.63,-.62,-.59,0,
                  .59,.62,.63,.64,.88,.89,.90,.93,1-EPS_CAP/2]:
            y,z=ysz(v)
            for side in (-1,1):
                angle=float(np.arctan2(z[0]+side*outer_arc,y[0])%(2*np.pi))
                angles.append(angle)
                if abs(v)> .99:
                    angles.extend((angle+j for j in (-.00008,-.000035,-.000012,.000012,.000035,.00008)))
        self.theta=separated([a%(2*np.pi) for a in angles],1.e-7)
        t1=.00025
        t2=t1+ref.sphere_turn; t3=t2+ref.tube_length; t4=ref.meridian_end
        sections=[(0,t1,4),(t1,t2,rings),(t2,t3,rings),(t3,t4,2*rings),(t4,self.end,3*rings)]
        coords=[]
        for a,b,k in sections:
            frac=np.arange(1,k)/k
            coords.extend([a,b,*list(a+(b-a)*(frac+shift/k))])
        coords.extend(self.end-i for i in [.00005,.00012,.0002,.00035,.0005,.00075,.0011,.0016,.0024,.0035,.006,.012,.022,.037])
        self.t=separated(coords,1e-7)
        self.T,self.A=np.meshgrid(self.t,self.theta,indexing='ij')
        co,si=np.cos(self.A),np.sin(self.A)
        def coords(r,cc,ss):
            y=r*cc; z=r*ss
            yc=np.clip(y,self.Ylo,self.Yhi)
            v=self.inv(yc)
            for _ in range(4):
                alpha,yy0,zz0=source.fields(v)
                if np.max(abs(yy0-yc))<4e-15:
                    break
                v=np.clip(v-(yy0-yc)/source.cartesian(v,1)[...,0],-1.,1.)
            alpha,yy0,zz0=source.fields(v)
            if np.max(abs(yy0-yc))>3e-14:
                raise ArithmeticError("Original material inverse failed on the true stored source line")
            return v+(y-yc),z-zz0,yy0+(y-yc),zz0
        # The perimeter intersection depends only on angle, once per actual ray.
        cc,ss=co[0],si[0]
        lo=np.full_like(cc,.198); hi=np.full_like(cc,2.)
        for _ in range(52):
            mid=(lo+hi)/2; v,s,y,zbase=coords(mid,cc,ss)
            val=softmax2(abs(v)/(1-EPS_CAP/2),abs(s)/outer_arc,.00002)
            hi=np.where(val>=1,mid,hi); lo=np.where(val<1,mid,lo)
        rr=(lo+hi)/2
        w=np.maximum(0,self.T-ref.meridian_end)
        r=HOLE+w+(rr[None,:]-HOLE-self.L)*smooth(w/self.L)
        self.v,self.s,self.y,self.z0=coords(r,co,si)
        self.outer=self.T>=ref.meridian_end
        self.wing=ref.S-abs(self.s)
        self.side=np.sign(self.s)
        self.gap=1-abs(self.v)
        self.width=active_width(self.v,h)
        self.cap_allow=smooth((self.gap-EPS_CAP)/.07)
        self.wing_allow=smooth((self.wing-self.width)/.07)
        self.bridge=(~self.outer)|(r<=.2005)
        self.free=np.where(self.outer,smooth((r-.2005)/.055)*self.cap_allow*self.wing_allow,0.)
        self.paid=self.bridge|(self.outer&((self.wing<=self.width)|(self.gap<=EPS_CAP)))
        self.outer_weight=np.where(self.outer,smooth((r-.2005)/.12),0.)
        self.tie=smooth((w/self.L-.18)/.54)
        outside=self.paid&~self.bridge
        if (np.any(self.tie[self.bridge]!=0) or np.any(self.tie[outside]!=1)
                or np.any(np.diff(outside.astype(int),axis=0)<0)):
            raise ArithmeticError("Actual crown/primary paid intervals and two-sided integration bands differ")
        self.Dt=differentiate(self.t,1); self.Dtt=differentiate(self.t,2)
        self.Da=differentiate(self.theta,1,True); self.Daa=differentiate(self.theta,2,True)
        self.Dt,self.Dtt,self.Da,self.Daa=map(csr_matrix,(self.Dt,self.Dtt,self.Da,self.Daa))
        # Piecewise linear integral is monotone on this deliberately nonuniform grid.
        self.I=np.zeros((len(self.t),len(self.t)))
        for i,dt in enumerate(np.diff(self.t),1):
            self.I[i]=self.I[i-1]; self.I[i,i-1:i+1]+=dt/2
        widths=(np.roll(self.theta,-1)-self.theta)%(2*np.pi)
        self.angular_weights=(widths+np.roll(widths,1))/2
        self.quad=(self.I[-1,:,None]*self.angular_weights[None,:])/(self.end*2*np.pi)
        self.geometry={}
        base=np.empty(self.T.shape+(3,))
        inner=~self.outer
        x,rad=ref.meridian(self.T[inner])
        base[inner]=np.stack((x,rad*co[inner],rad*si[inner]),axis=-1)
        s,v,y=self.s[self.outer],self.v[self.outer],self.y[self.outer]
        x,z=ref.section(s,v,y)
        base[self.outer]=np.stack((x,y,self.z0[self.outer]+z),axis=-1)
        self.base=base

    def dt(self,X,order=1):
        A=self.Dt if order==1 else self.Dtt
        return (A@X.reshape(X.shape[0],-1)).reshape(X.shape)

    def da(self,X,order=1):
        A=self.Da if order==1 else self.Daa
        Y=np.swapaxes(X,0,1)
        return np.swapaxes((A@Y.reshape(Y.shape[0],-1)).reshape(Y.shape),0,1)

    def integrate(self,X):
        out=np.zeros_like(X)
        widths=np.diff(self.t).reshape((-1,)+(1,)*(X.ndim-1))
        out[1:]=np.cumsum(widths*(X[1:]+X[:-1])/2,axis=0)
        return out

    def prepare(self,line,collars,source_collars):
        if line.phase in self.geometry:
            return self.geometry[line.phase]
        self.geometry[line.phase]=self._lifting(line,collars,source_collars)
        return self.geometry[line.phase]

    def _lifting(self,line,collars,source_collars):
        src=self.source
        alpha,y,z=line.fields(self.v)
        a0,y0,z0=src.fields(self.v)
        disp=np.stack((np.zeros_like(y),y-y0,z-z0),axis=-1)
        _,ys,zs=src.fields(np.array([self.vstar]))
        _,yf,zf=line.fields(np.array([self.vstar]))
        shift=np.array([0.,(yf-ys).item(),(zf-zs).item()])
        P=self.base+shift+self.outer_weight[...,None]*(disp-shift)
        rv=np.zeros_like(P); rv[...,0]=self.outer_weight*(alpha-a0)
        for coll,orig in zip(collars,source_collars):
            pulse_v=self.v if coll.sign==1 else -self.v
            vw=band(pulse_v,-.907,-.90,-.62,-.613)
            mask=self.outer&(self.wing>=0)&(self.wing<=2.3*self.h)&(vw>0)
            if not np.any(mask):
                continue
            t,v=self.wing[mask],self.v[mask]
            pc,pt,pv,*_=coll.position_jets(t,v)
            _,ot,ov,*_=orig.position_jets(t,v)
            linept=np.stack((W+t,y[mask],z[mask]),axis=-1)
            wt=vw[mask]*(1-smooth((t/self.h-1)/1.3))
            P[mask]+=wt[:,None]*(pc-linept)
            rel=frame(pt,pv)@np.swapaxes(frame(ot,ov),-1,-2)
            old=rotation(rv[mask])
            rv[mask]=step_vec(rotation(wt[:,None]*step_vec(rel@np.swapaxes(old,-1,-2)))@old)
        return P,rotation(rv)
