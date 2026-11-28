"""R681 double pulse, R664 physical Gauss--Codazzi collars and their Cartesian jets."""
from functools import lru_cache
import os

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import BPoly, RectBivariateSpline
from scipy.special import expit


def require_public():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY", "").lower() != "rogerhu12/math-research-public" or
            not os.environ.get("GITHUB_RUN_ID", "").isdigit()):
        raise RuntimeError("R688 science requires the public repository Actions runner")


def smooth(x):
    """C-infinity step supported in the unit transition interval."""
    x = np.asarray(x, float)
    y = np.clip(x, 1.e-14, 1-1.e-14)
    return np.where(x <= 0, 0., np.where(x >= 1, 1., expit(1/(1-y)-1/y)))


def band(v, outer_left, inner_left, inner_right, outer_right):
    return smooth((v-outer_left)/(inner_left-outer_left))*smooth((outer_right-v)/(outer_right-inner_right))


@lru_cache(maxsize=4)
def quadrature(order):
    return np.polynomial.legendre.leggauss(order)


def mollifier_cdf(x, order=48):
    x = np.asarray(x, float)
    q, w = quadrature(order)
    r = np.clip(x, -1., 1.)
    half = (r+1)/2
    t = -1 + half[..., None]*(q+1)
    norm = np.exp(-1/(1-q*q)) @ w
    integ = half*(np.exp(-1/np.maximum(1-t*t, 1.e-300)) @ w)/norm
    return np.where(x <= -1, 0., np.where(x >= 1, 1., integ))


def beta(v):
    return (mollifier_cdf((v+.88)/.01)-mollifier_cdf((v+.64)/.01))/.24


def pulse(v):
    return .05*band(v, -.93, -.91, -.61, -.59)


def true_curvature(v, phase):
    return pulse(v)-pulse(-v)+phase*(beta(v)-beta(-v))


class Centerline:
    def __init__(self, phase):
        require_public()
        self.phase = float(phase)

        def rhs(v, data):
            return [float(true_curvature(np.asarray(v), self.phase)), np.cos(data[0]), np.sin(data[0])]

        self.solution = solve_ivp(rhs, (-1., 1.), [0., -1., 0.], method="DOP853",
                                  rtol=3e-13, atol=2e-15, max_step=.006, dense_output=True)
        if not self.solution.success:
            raise RuntimeError(self.solution.message)
        self.calls = self.solution.nfev
        self.far=self.solution.sol(1.)[1:]

        # A single C4 physical centerline with the exact analytic straight caps.
        # Endpoint derivative data come from this same DOP solution and prescribed curvature.
        v=np.linspace(-.93,.93,1861)
        alpha,y,z=self.solution.sol(v)
        y[0],z[0]=-0.93,0.
        y[-1],z[-1]=self.far[0]-.07,self.far[1]
        alpha[[0,-1]]=0.
        pos=np.column_stack((y,z))
        first=np.column_stack((np.cos(alpha),np.sin(alpha)))
        normal=np.column_stack((-np.sin(alpha),np.cos(alpha)))
        k=true_curvature(v,self.phase); delta=2e-5
        km=true_curvature(v-delta,self.phase); kp=true_curvature(v+delta,self.phase)
        kd=(kp-km)/(2*delta); kdd=(kp-2*k+km)/delta**2
        kd[[0,-1]]=0.; kdd[[0,-1]]=0.
        second=k[:,None]*normal
        third=kd[:,None]*normal-(k*k)[:,None]*first
        fourth=(kdd-k**3)[:,None]*normal-(3*k*kd)[:,None]*first
        self.curve=BPoly.from_derivatives(v,np.stack((pos,first,second,third,fourth),axis=1))
        checks=v[:-1]+.0005
        raw=self.solution.sol(checks)
        dp=self.curve(checks,1); ddp=self.curve(checks,2)
        analytic=np.column_stack((np.cos(raw[0]),np.sin(raw[0])))
        accel=true_curvature(checks,self.phase)[:,None]*np.column_stack((-analytic[:,1],analytic[:,0]))
        self.curve_errors=[float(np.max(np.linalg.norm(x,axis=-1))) for x in
            (self.curve(checks)-raw[1:].T,dp-analytic,ddp-accel)]

    def cartesian(self,v,order=0):
        v=np.asarray(v,float)
        pos=self.curve(np.clip(v,-.93,.93),order)
        if order==0:
            low=np.stack((v,np.zeros_like(v)),axis=-1)
            high=np.stack((self.far[0]+v-1,np.full_like(v,self.far[1])),axis=-1)
        else:
            low=np.broadcast_to([1. if order==1 else 0.,0.],v.shape+(2,))
            high=low
        return np.where((v<=-.93)[...,None],low,np.where((v>=.93)[...,None],high,pos))

    def fields(self, v):
        p=self.cartesian(v); d=self.cartesian(v,1)
        return np.arctan2(d[...,1],d[...,0]),p[...,0],p[...,1]


class Collar:
    """One signed pulse on an enlarged material interval, before the physical cut."""
    def __init__(self, line, sign, h, modes, steps):
        require_public()
        self.h, self.sign, self.line = h, sign, line
        lo, hi = (-.95, -.57) if sign == 1 else (.57, .95)
        self.lo, self.hi = lo, hi
        width = hi-lo
        # Only m,n are differentiated periodically. Their initial extension is
        # constant at both artificial ends and agrees with the actual pulse inside.
        v = lo+width*np.arange(modes)/modes
        k = 2*np.pi*np.fft.fftfreq(modes, d=width/modes)
        ext = sign*(.05 + line.phase*beta(v if sign == 1 else -v))
        alpha, y, z = line.fields(v)
        P = np.column_stack((np.full(modes, .38), y, z))
        first = np.broadcast_to([1., 0., 0.], P.shape).copy()
        second = np.column_stack((np.zeros(modes), np.cos(alpha), np.sin(alpha)))
        normal = np.cross(first, second)
        Y = np.column_stack((np.zeros(modes), ext, P, first, second, normal))

        def dv(a):
            return np.fft.ifft(1j*k*np.fft.fft(a)).real

        def unpack(Y):
            return Y[:, 0], Y[:, 1], Y[:, 2:5], Y[:, 5:8], Y[:, 8:11], Y[:, 11:14]

        self.maximum_speed = 0.
        self.minimum_signed_n = np.inf

        def rhs(t, Y):
            m, n, _, e1, e2, N = unpack(Y)
            if np.min(sign*n) <= .02 or not np.isfinite(Y).all():
                raise ArithmeticError("The actual signed collar denominator lost its guarded branch")
            A = 1+t**4
            J = 4*t**3/A
            K = -12*t*t/A
            l = (K+m*m)/n
            self.minimum_signed_n = min(self.minimum_signed_n, float(np.min(sign*n)))
            speed = np.max((abs(m)+np.sqrt(-K))/(A*abs(n)))
            self.maximum_speed = max(self.maximum_speed, float(speed))
            return np.column_stack((dv(l)/A-2*J*m, dv(m)/A+J*(l-n), e1,
                                   l[:, None]*N, m[:, None]*N, -l[:, None]*e1-m[:, None]*e2))

        times = np.linspace(0., 3*h, steps+1)
        history = [Y.copy()]
        for t, dt in zip(times[:-1], np.diff(times)):
            p1 = rhs(t, Y)
            p2 = rhs(t+dt/2, Y+dt*p1/2)
            p3 = rhs(t+dt/2, Y+dt*p2/2)
            p4 = rhs(t+dt, Y+dt*p3)
            Y = Y+dt*(p1+2*p2+2*p3+p4)/6
            history.append(Y.copy())
        self.splines = [RectBivariateSpline(times, v, values, kx=5, ky=5, s=0)
                        for values in np.moveaxis(np.asarray(history), -1, 0)]
        self.rhs_calls = 4*steps
        self.checked = 3*h*self.maximum_speed < .003
        if not self.checked:
            raise ArithmeticError("The measured speed exhausts the proper physical pulse buffer")

    def jets(self, t, v):
        t, v = np.broadcast_arrays(t, v)
        vals = np.stack([spl.ev(t.ravel(), v.ravel()).reshape(t.shape)
                         for spl in self.splines], axis=-1)
        m,n = vals[..., 0], vals[..., 1]
        P,e1,e2,N = [vals[..., i:i+3] for i in (2,5,8,11)]
        A, Ap = 1+t**4, 4*t**3
        l = (m*m-12*t*t/A)/n
        return (P, e1, A[..., None]*e2, l[..., None]*N,
                Ap[..., None]*e2+(A*m)[..., None]*N,
                -(A*Ap)[..., None]*e1+(A*A*n)[..., None]*N)

    def raw_position_jets(self,t,v):
        """Independent Cartesian two-jet of the one actual position interpolant."""
        t,v=np.broadcast_arrays(t,v)
        def value(dt,dv):
            return np.stack([spl.ev(t.ravel(),v.ravel(),dx=dt,dy=dv).reshape(t.shape)
                             for spl in self.splines[2:5]],axis=-1)
        return tuple(value(dt,dv) for dt,dv in ((0,0),(1,0),(0,1),(2,0),(1,1),(0,2)))

    def position_jets(self,t,v):
        """Physical C2 position and five derivatives with exact sheet Cauchy jets."""
        t,v=np.broadcast_arrays(t,v)
        eq=np.zeros_like(t)
        def at0(dt,dv):
            return np.stack([spl.ev(eq.ravel(),v.ravel(),dx=dt,dy=dv).reshape(t.shape)
                             for spl in self.splines[2:5]],axis=-1)
        b00,b10,b01,b20,b11,b02=self.raw_position_jets(eq,v)
        b21,b12,b22=at0(2,1),at0(1,2),at0(2,2)
        p,pt,pv,ptt,ptv,pvv=self.raw_position_jets(t,v)
        t=t[...,None]
        line=[self.line.cartesian(v,j) for j in range(3)]
        def xyz(x,yz):
            return np.concatenate((np.broadcast_to(x,yz.shape[:-1])[...,None],yz),axis=-1)
        return (xyz(.38,line[0])+t*np.array([1.,0.,0.])+(p-b00)-t*b10-.5*t*t*b20,
                np.array([1.,0.,0.])+(pt-b10)-t*b20,
                xyz(0.,line[1])+(pv-b01)-t*b11-.5*t*t*b21,
                ptt-b20,(ptv-b11)-t*b21,
                xyz(0.,line[2])+(pvv-b02)-t*b12-.5*t*t*b22)


def active_width(v, h):
    v = np.asarray(v)
    return h*band(-abs(v), -.90, -.89, -.63, -.62)


def verify_collars(coarse, fine):
    output = []
    for a,b in zip(coarse, fine):
        v = np.linspace(-.90, -.62, 247)
        if a.sign < 0:
            v = -v
        fraction,v=np.meshgrid(np.linspace(0.,1.,13),v,indexing="ij")
        t = (fraction*active_width(v, a.h)).ravel()
        v=v.ravel()
        # Independent radial and azimuthal resolutions. These are readouts,
        # never a certified continuous PDE or Cauchy error estimate.
        x, y = a.jets(t,v), b.jets(t,v)
        P, first, sec, rr, rs, ss = y
        n = np.cross(first,sec)
        n /= np.linalg.norm(n,axis=1)[:,None]
        A = 1+t**4
        l = np.sum(rr*n,axis=1)
        m = np.sum(rs*n,axis=1)/A
        nn = np.sum(ss*n,axis=1)/A**2
        orth = np.stack((np.sum(first**2,axis=1)-1, np.sum(first*sec,axis=1)/A,
                         np.sum(sec**2,axis=1)/A**2-1))
        xp,yp=a.position_jets(t,v),b.position_jets(t,v)
        derivative_defect=[float(np.max(np.linalg.norm(j-k,axis=-1))) for j,k in zip(yp[1:],y[1:])]
        rawp=b.raw_position_jets(t,v)
        raw_correction=[float(np.max(np.linalg.norm(z-w,axis=-1))) for z,w in zip(rawp,yp)]
        coarse_derivative_defect=[float(np.max(np.linalg.norm(j-k,axis=-1))) for j,k in zip(xp[1:],x[1:])]
        output.append(dict(sign=a.sign, position_spline_five_differential_defects=derivative_defect,
                           coarse_position_five_differential_defects=coarse_derivative_defect,
                           physical_strip_material_samples=len(t),raw_position_to_cauchy_matched_six=raw_correction,
                           position_spline_six_grid_jet_changes=[float(np.max(np.linalg.norm(z-w,axis=-1))) for z,w in zip(xp,yp)], max_grid_jet_changes=[float(np.max(np.linalg.norm(z-w,axis=-1))) for z,w in zip(x,y)],
                           frame_gram_max=float(np.max(abs(orth))),
                           gauss_max=float(np.max(abs(l*nn-m*m+12*t*t/A))),
                           min_signed_n=b.minimum_signed_n, maximum_propagation_speed=b.maximum_speed,
                           rhs_calls=a.rhs_calls+b.rhs_calls))
    return output
