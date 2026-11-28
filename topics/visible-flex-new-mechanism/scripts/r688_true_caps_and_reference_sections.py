"""Physical R681 parallel convex caps and R686 wide, two-jet-matched source sections."""
from functools import lru_cache
from numpy.polynomial import Polynomial

import numpy as np
from scipy.integrate import cumulative_simpson, solve_ivp
from scipy.interpolate import make_interp_spline, RectBivariateSpline

from r688_actual_r664_window_collars import mollifier_cdf, quadrature, require_public, smooth

W, D = .38, .20
EPS_CAP = .05
HOLE, TUBE = .198, .10
TOP_ANGLE = np.arctan2(D,W)


def sym_step(t):
    """Integral of uniform [.001,.999] convolved with the even .0005 bump."""
    u = np.asarray(t,float)
    eps = .0005
    # E[(u-a-Z)_+-(u-b-Z)_+]/(b-a). Integrate only up to the moving kink.
    q,weight = quadrature(48)
    norm = np.exp(-1/(1-q*q))@weight
    def primitive(s):
        bound = np.clip(s/eps,-1.,1.)
        half = (bound+1)/2
        z = -1+half[...,None]*(1+q)
        value = half*((np.exp(-1/np.maximum(1-z*z,1.e-300))*(s[...,None]-eps*z))@weight)
        return np.where(s<=-eps,0.,np.where(s>=eps,s,value/norm))
    return np.clip((primitive(u-.001)-primitive(u-.999))/.998,0.,1.)


@lru_cache(maxsize=1)
def shoulder_polynomials():
    # Local unit coordinates avoid cancellation at the right end of the narrow ramp.
    delta=.01; u=Polynomial([0.,1.]); v=1-u
    function=[delta*(u**3-u**4/2)/(1-delta),
              (delta/2+(1-2*delta)*u)/(1-delta),
              1-delta*(v**3-v**4/2)/(1-delta)]
    return [(width,(1-f)**2,((1-f)**2).integ()) for width,f in
            zip((delta,1-2*delta,delta),function)]


def shoulder_parameter(g):
    """Return true section w, dw/dg and d2w/dg2 on the rigid cap shoulder."""
    g=np.asarray(g,float)
    g0=.00001; length=.023
    mass=np.clip(g,0,g0).copy()
    speed=np.where(g<=g0,1.,0.); accel=np.zeros_like(g)
    begin=g0
    for fraction,q,I in shoulder_polynomials():
        width=length*fraction
        v=np.clip((g-begin)/width,0.,1.)
        mask=(g>=begin)&(g<begin+width)
        mass+=width*I(v)
        speed=np.where(mask,q(v),speed)
        accel=np.where(mask,q.deriv()(v)/width,accel)
        begin+=width
    return -mass,-speed,-accel


def seat_weight(s,S):
    sign=np.sign(s); dist=S-abs(s)
    u=np.clip((dist-.001)/.0015,0.,1.)
    w=1-u**3*(10-15*u+6*u*u)
    ws=sign*30*u*u*(1-u)**2/.0015
    wss=-60*u*(1-u)*(1-2*u)/.0015**2
    return w,ws,wss


def implicit(p):
    x,w,z = np.moveaxis(p,-1,0)
    sig = (x/.42)**2+((w-.02)/.07)**2
    base = np.maximum(sig-1,0.)
    H = (base/.44)**4
    hp = 4*base**3/.44**4
    hpp = 12*base**2/.44**4
    dsig = np.stack((2*x/.42**2,2*(w-.02)/.07**2,np.zeros_like(x)),axis=-1)
    grad = hp[...,None]*dsig
    grad[...,2] = 2*z/.08**2
    hess = hpp[...,None,None]*dsig[...,None]*dsig[...,None,:]
    hess[...,0,0] += 2*hp/.42**2
    hess[...,1,1] += 2*hp/.07**2
    hess[...,2,2] += 2/.08**2
    return H+(z/.08)**2-1, grad, hess


def radial_zero(direction, center):
    lo = np.zeros(direction.shape[:-1])
    hi = np.full_like(lo,.8)
    for _ in range(56):
        mid = (lo+hi)/2
        val = implicit(center+direction*mid[...,None])[0]
        hi = np.where(val>=0,mid,hi)
        lo = np.where(val<0,mid,lo)
    return center+direction*((lo+hi)/2)[...,None]


def cap_sections(w, phi, initial=None, jets=False):
    w,phi = np.broadcast_arrays(w,phi)
    c,s=np.cos(phi),np.sin(phi)
    axis = np.stack((-s,np.zeros_like(s),c),axis=-1)
    direction = np.stack((c,np.zeros_like(s),s),axis=-1)
    center = np.stack((np.zeros_like(w),w,np.zeros_like(w)),axis=-1)
    p=radial_zero(direction,center) if initial is None else initial
    eye=np.eye(3)
    for offset in (np.linspace(.12/16,.12,16) if initial is None else (.12,)):
        def system(z):
            value,grad,H=implicit(z)
            size=np.linalg.norm(grad,axis=-1)
            n=grad/size[...,None]
            dn=(eye-n[...,None]*n[...,None,:])@H/size[...,None,None]
            surf=z+offset*n
            F=np.stack((value,surf[...,1]-w,np.sum(surf*axis,axis=-1)),axis=-1)
            J=eye+offset*dn
            A=np.stack((grad,J[...,1,:],np.einsum('...i,...ij->...j',axis,J)),axis=-2)
            return F,A,surf,n
        for _ in range(24):
            F,A,surf,n=system(p)
            err=np.max(abs(F),axis=-1)
            if np.max(err)<3e-12:
                break
            delta=np.linalg.solve(A,F[...,None])[...,0]
            # Separate step for each real section point.
            q=p-delta
            for _ in range(10):
                bad=(np.max(abs(system(q)[0]),axis=-1)>err)&(err>3e-12)
                if not np.any(bad):
                    break
                q=np.where(bad[...,None],(p+q)/2,q)
            p=q
        if np.max(abs(system(p)[0]))>2e-10:
            raise ArithmeticError("Actual R681 parallel cap section root is unresolved")
    P,N=system(p)[2:]
    if not jets:
        return P,N
    # Implicit two-jet on the actual parallel surface. Only the original
    # shape operator and its parallel transform are needed for these rows.
    _,grad,H=implicit(p); T=eye-N[...,None]*N[...,None,:]
    S0=T@H@T/np.linalg.norm(grad,axis=-1)[...,None,None]
    S=np.linalg.solve(eye+.12*S0,S0)
    def dot(a,b):
        return np.sum(a*b,axis=-1)
    c=direction; k=axis
    rn=dot(N,c)
    if np.any(rn<=0):
        raise ArithmeticError("True cap polar section lost radial transversality")
    rho=dot(P,c); rw=-N[...,1]/rn; ra=-rho*dot(N,k)/rn
    Pw=np.array([0.,1.,0.])+rw[...,None]*c
    Pa=ra[...,None]*c+rho[...,None]*k
    def second(a,b,rem):
        dN=np.einsum('...ij,...j->...i',S,a)
        rho_ij=(-dot(dN,b)-dot(N,rem))/rn
        return rho_ij[...,None]*c+rem
    Pww=second(Pw,Pw,np.zeros_like(P))
    Pwa=second(Pw,Pa,rw[...,None]*k)
    Paa=second(Pa,Pa,2*ra[...,None]*k-rho[...,None]*c)
    return tuple(a[...,[0,2]] for a in (P,Pw,Pa,Pww,Pwa,Paa))


def soft_angle(length,start,end):
    def rhs(t,_):
        a=start+(end-start)*float(sym_step(t/length))
        return [np.cos(a),np.sin(a)]
    sol=solve_ivp(rhs,(0,length),[0.,0.],rtol=4e-13,atol=2e-15,method="DOP853",
                  max_step=length/24,dense_output=True)
    if not sol.success:
        raise ArithmeticError(sol.message)
    return sol.sol


class ReferenceSections:
    def __init__(self, angular_table=801, cap_rows=33):
        require_public()
        self.phi=np.pi/3
        self.arc_lengths=np.array([.001,.125*self.phi,.125*self.phi,.101*np.pi/2])
        self.cuts=np.r_[0.,np.cumsum(self.arc_lengths)]
        self.turns=[None,soft_angle(self.arc_lengths[1],0.,self.phi),
                    soft_angle(self.arc_lengths[2],self.phi,0.),
                    soft_angle(self.arc_lengths[3],0.,-np.pi/2)]
        starts=[[W,D],[W+.001,D]]
        for i in range(1,4):
            starts.append(starts[-1]+self.turns[i](self.arc_lengths[i]))
        self.starts=np.asarray(starts)
        self.xf,self.height=self.starts[-1]
        self.S=self.height+self.cuts[-1]
        # Input s is signed material arclength on the new central arc. On both
        # real horizontal seats it is exactly the physical horizontal distance.
        d=np.linspace(0,self.S,2049)
        cap=1-smooth((d-.008)/.008)
        partial=cap*D/(D*D+(W+d)**2)
        tails=1-cap
        c=(TOP_ANGLE-cumulative_simpson(partial,x=d,initial=0)[-1])/cumulative_simpson(tails,x=d,initial=0)[-1]
        deriv=partial+c*tails
        phi_grid=TOP_ANGLE-cumulative_simpson(deriv,x=d,initial=0)
        phi_grid[-1]=0.
        self.angle=make_interp_spline(d,phi_grid,k=5)
        w=np.linspace(-.0083,0.,cap_rows)
        phi=np.linspace(-TOP_ANGLE,TOP_ANGLE,angular_table)
        ww,pp=np.meshgrid(w,phi,indexing='ij')
        pts,norm=cap_sections(ww,pp)
        self.tables=[RectBivariateSpline(w,phi,pts[...,i],kx=5,ky=5) for i in (0,2)]
        self.cap_normals=[RectBivariateSpline(w,phi,norm[...,i],kx=5,ky=5) for i in range(3)]
        self.sphere_r=.11
        theta0=np.arccos(.25)
        eps=.0005
        def crown_rhs(s,y):
            k=(1-smooth((s/eps-.12)/.76))/self.sphere_r
            return [-k,np.sin(y[0]),-np.cos(y[0])]
        crown=solve_ivp(crown_rhs,(0,2*eps),[theta0,.11/4,.11*np.sqrt(15)/4],
                        dense_output=True,max_step=eps/20,rtol=4e-13,atol=2e-15)
        if not crown.success:
            raise ArithmeticError(crown.message)
        self.crown=crown.sol
        self.theta_b,zb,rb=self.crown(.001)
        self.xb=.96-zb
        self.rb=rb
        q,weight=quadrature(64)
        t=(q+1)/2
        def mean(f):
            return float(weight@f(t)/2)
        self.sphere_turn=(rb-TUBE)/mean(lambda z: np.cos(self.theta_b+(np.pi/2-self.theta_b)*sym_step(z)))
        self.source_turn=(HOLE-TUBE)/mean(lambda z: np.cos(np.pi/2*sym_step(z)))
        self.sphere_arc=soft_angle(self.sphere_turn,np.pi/2-self.theta_b,0.)
        self.source_arc=soft_angle(self.source_turn,0.,np.pi/2)
        # For sphere_arc, x advances by cos(delta), radius falls by sin(delta).
        self.crown_end_x=self.xb-self.sphere_arc(self.sphere_turn)[0]
        self.tube_length=self.crown_end_x-(self.xf+HOLE-TUBE)
        if not (.2229<self.height and self.xf<.701 and self.tube_length>0):
            raise ArithmeticError("Actual wide join failed the R686 compatibility margins")
        self.meridian_end=.00025+self.sphere_turn+self.tube_length+self.source_turn

    def central(self, s):
        s=np.asarray(s)
        d=self.S-abs(s)
        x=np.full(s.shape,self.xf); z=abs(s).copy()
        seat=d<=self.cuts[1]
        x[seat]=W+d[seat]; z[seat]=D
        for i in range(1,4):
            mask=(d>self.cuts[i])&(d<=self.cuts[i+1])
            if np.any(mask):
                point=self.starts[i,:,None]+self.turns[i](d[mask]-self.cuts[i])
                x[mask],z[mask]=point
        return x,np.sign(s)*z

    def actual_section(self,w,phi,jets=False):
        def evaluate(spl):
            return spl.ev(w.ravel(),phi.ravel()).reshape(w.shape)
        guess=np.stack((evaluate(self.tables[0]),w,evaluate(self.tables[1])),axis=-1)
        normals=np.stack([evaluate(spl) for spl in self.cap_normals],axis=-1)
        return cap_sections(w,phi,initial=guess-.12*normals,jets=jets)

    def old(self,s,w):
        s,w=np.broadcast_arrays(s,w)
        dist=self.S-abs(s)
        phi=np.sign(s)*self.angle(np.clip(dist,0,self.S))
        P,_=self.actual_section(w,phi)
        x,z=P[...,0].copy(),P[...,2].copy()
        # Flat plate is analytically present on this actual cap (strict .40 > .38).
        seat=seat_weight(s,self.S)[0]
        x+=seat*(W+dist-x)
        z+=seat*(np.sign(s)*D-z)
        return x,z

    def shoulder_jets(self,g,s):
        """The physical two-jet of (old_x(eta(g),s),-g,old_z(eta(g),s))."""
        g,s=np.broadcast_arrays(g,s)
        w,wp,wpp=shoulder_parameter(g)
        dist=np.clip(self.S-abs(s),0.,self.S); sign=np.sign(s)
        phi=sign*self.angle(dist)
        ps=-self.angle(dist,1)
        pss=sign*self.angle(dist,2)
        raw,fw,fp,fww, fwp, fpp=self.actual_section(w,phi,jets=True)
        def col(x):
            return x[...,None]
        seat=np.stack((W+self.S-abs(s),sign*D),axis=-1)
        seats=np.stack((-sign,np.zeros_like(sign)),axis=-1)
        k,ks,kss=[col(t) for t in seat_weight(s,self.S)]
        fs=fp*col(ps)
        fs2=fpp*col(ps**2)+fp*col(pss)
        X=raw+k*(seat-raw)
        Xs=fs+k*(seats-fs)+ks*(seat-raw)
        Xss=(1-k)*fs2+2*ks*(seats-fs)+kss*(seat-raw)
        Xg=(1-k)*fw*col(wp)
        Xgg=(1-k)*(fww*col(wp**2)+fw*col(wpp))
        Xgs=((1-k)*fwp*col(ps)-ks*fw)*col(wp)
        def xyz(xz,y):
            return np.stack((xz[...,0],np.full_like(g,y) if np.isscalar(y) else y,xz[...,1]),axis=-1)
        return (xyz(X,-g),xyz(Xg,-1.),xyz(Xs,0.),xyz(Xgg,0.),xyz(Xgs,0.),xyz(Xss,0.))

    def section(self,s,v,y0):
        gap=1-abs(v)
        w=shoulder_parameter(np.maximum(0,gap))[0]
        w*=1-smooth((gap-1.12*EPS_CAP)/.055)
        x,z=self.old(s,w)
        xc,zc=self.central(s)
        mix=1-smooth((abs(y0)-.215)/.54)
        return x+mix*(xc-x),z+mix*(zc-z)

    def meridian(self,d):
        """Increasing d goes from inside the retained crown toward the window."""
        d=np.asarray(d)
        x=np.empty_like(d); r=np.empty_like(d)
        first=d<=.00025
        if np.any(first):
            _,axis,rad=self.crown(.00075+d[first]); x[first],r[first]=.96-axis,rad
        d=d-.00025
        mask=(~first)&(d<=self.sphere_turn)
        if np.any(mask):
            step=self.sphere_arc(d[mask]); x[mask],r[mask]=self.xb-step[0],self.rb-step[1]
        d=d-self.sphere_turn
        mask=(d>0)&(d<=self.tube_length)
        x[mask],r[mask]=self.crown_end_x-d[mask],TUBE
        d=d-self.tube_length
        mask=d>0
        if np.any(mask):
            step=self.source_arc(self.source_turn-d[mask])
            x[mask],r[mask]=self.xf+step[1],HOLE-step[0]
        return x,r
