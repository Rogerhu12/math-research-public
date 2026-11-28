"""Compensated Gauss--Codazzi and position on the actual R732 positive-v Cauchy pulses."""

import numpy as np
from scipy.interpolate import RectBivariateSpline

from r688_actual_r664_window_collars import mollifier_cdf, quadrature, require_public

H = 1.e-8
B0 = .100/(.102*.998)
C_AXIS = np.array([1.,0.,0.])
PHASE_HEIGHT = .920

def spectral_derivative(values, wave):
    return np.fft.ifft(1j*wave*np.fft.fft(values)).real


class Pulse:
    """Positive-v material window on the right side. Lower primary uses the same curvature sign."""
    def __init__(self,phase,c,sense,angles,modes,steps):
        require_public()
        self.phase,self.c,self.sense=phase,c,sense
        self.lo,self.hi=c-.0005,c+.1005
        self.modes,self.steps=modes,steps
        v=self.lo+(self.hi-self.lo)*np.arange(modes)/modes
        dz=(self.hi-self.lo)/modes
        wave=2*np.pi*np.fft.fftfreq(modes,dz)
        self.wave=wave
        y=(v-c)/.100
        beta=(mollifier_cdf((y-.001)/.0005)-mollifier_cdf((y-.999)/.0005))/(.100*.998)
        n0=sense*(B0+PHASE_HEIGHT*phase*beta)
        alpha=angles(v,phase)
        cT=np.column_stack((np.zeros(modes),np.cos(alpha),np.sin(alpha)))
        nT=np.cross(C_AXIS,cT)
        # m=h^3*M; n=n0+h^4*G. The remaining columns are E1,E2,N correction,Q.
        # Q supplies an actual single interpolated position delta h^4 Q.
        Y=np.zeros((modes,14))
        self.min_n=float('inf')
        times=np.linspace(0.,2.,steps+1)
        stored=[Y[:,11:14].copy()]
        self.count=0
        def rhs(q,Z):
            self.count+=1
            M,G=Z[:,0],Z[:,1]
            E,J,V=Z[:,2:5],Z[:,5:8],Z[:,8:11]
            A=1.+H**4*q**4
            n=n0+H**4*G
            self.min_n=min(self.min_n,float(np.min(sense*n)))
            if self.min_n<=.04:
                raise ArithmeticError('r724 signed curvature denominator')
            L=(H**4*M*M-12*q*q/A)/n
            e1=C_AXIS+H**3*E;e2=cT+H**4*J;N=nT+H**3*V
            return np.column_stack((spectral_derivative(L,wave)/A-8*H**4*q**3*M/A,
                                    spectral_derivative(M,wave)/A+4*q**3*(H*H*L-n)/A,
                                    L[:,None]*N,M[:,None]*N,-L[:,None]*e1-H*M[:,None]*e2,E))
        for a,b in zip(times,times[1:]):
            d=b-a
            k1=rhs(a,Y);k2=rhs(a+d/2,Y+d*k1/2)
            k3=rhs(a+d/2,Y+d*k2/2);k4=rhs(b,Y+d*k3)
            Y=Y+d*(k1+2*k2+2*k3+k4)/6
            stored.append(Y[:,11:14].copy())
        arr=np.asarray(stored)
        da=float(angles(np.asarray(self.hi),phase)-angles(np.asarray(self.lo),phase))
        co,si=np.cos(da),np.sin(da)
        rot=np.array([[1.,0.,0.],[0.,co,-si],[0.,si,co]])
        arr=np.concatenate((arr,arr[:,:1,:]@rot.T),axis=1)
        self.spl=[RectBivariateSpline(times,np.r_[v,self.hi],arr[:,:,j],kx=5,ky=5,s=0) for j in range(3)]
        self.highest_correction=float(np.max(abs(arr)))

    def raw_delta(self,distance,v,dt,dv):
        if not (0<=dt<=2 and 0<=dv<=2):
            raise ValueError('position derivative order')
        q=distance/H
        t,v=np.broadcast_arrays(q,v)
        zero=np.zeros(t.size)
        def ev(o,x):
            return np.column_stack([p.ev(x,v.ravel(),dx=o,dy=dv) for p in self.spl])
        # Subtract the three displacement jets at q=0 from the SAME position interpolant.
        # These vanish in the exact Cauchy problem and make our computed position C2 at t=0.
        flat=t.ravel()
        E=ev(dt,flat)
        if dt==0:
            E-=ev(0,zero)+flat[:,None]*ev(1,zero)+.5*flat[:,None]**2*ev(2,zero)
        elif dt==1:
            E-=ev(1,zero)+flat[:,None]*ev(2,zero)
        else:
            E-=ev(2,zero)
        return H**(4-dt)*E.reshape(t.shape+(3,))


def gate(x,order=0):
    """Even smooth probability convolution of the actual R724 compressed quintic."""
    x=np.asarray(x,float)
    flat=x.ravel(); out=np.zeros_like(flat)
    if order==0:out[flat>=.998]=1.
    active=(flat>.002)&(flat<.998)
    y=flat[active]
    if not len(y):return out.reshape(x.shape)
    q,w=quadrature(32)
    norm=np.exp(-1/(1-q*q))@w
    span=.992; eps=.002
    lo=np.clip((y-.996)/eps,-1.,1.); hi=np.clip((y-.004)/eps,-1.,1.)
    half=(hi-lo)/2; z=lo[:,None]+half[:,None]*(1+q)
    u=np.clip((y[:,None]-.004-eps*z)/span,0,1)
    if order==0:power=u**3*(10-15*u+6*u*u)
    elif order==1:power=30*u**2*(1-u)**2/span
    elif order==2:power=60*u*(1-u)*(1-2*u)/span**2
    else:raise ValueError('gate order')
    values=half*((np.exp(-1/np.maximum(1-z*z,1.e-300))*power)@w)/norm
    if order==0:values+=mollifier_cdf(lo,order=32)
    out[active]=values
    return out.reshape(x.shape)


