"""A new finite endpoint space: retain raw B2..B(M-2), then T=SA-SB and U=SB.

The number of controls remains M-1, but this is not the original raw span or
a coordinate change.  Only lambda=1 is defined.  The exact mean/primary
constraints follow from the defining integrals in R44.  Rational enclosures
below control the two new projection coefficients; floating evaluation and
the inherited numerical positivity guard are not a surface certificate.
"""
from fractions import Fraction as F
from functools import lru_cache
import math
from pathlib import Path
import sys
import numpy as np

LIBRARY=Path(__file__).with_name('round_raw_lib')
if str(LIBRARY) not in sys.path:sys.path.insert(0,str(LIBRARY))
from complementary_moment_basis import ComplementaryMomentBasis,cutoff_derivative_upper
from moment_interval_bounds import add,neg,scale,mul,divide,upper_abs,upper_float,pi_interval,sincos,beta_characteristic
from circle_trace_controls import CircleTraceControls


@lru_cache(None)
def trace_projection_enclosures(a_text,b_text):
    """Exact rational bounds on D=G^-1 V, with local cosine frequencies 1..6.

    Integration by parts gives I(w)=3/(pi*w) E[sin(w*(a+b*t))],
    where the probability density is P'(t)=630*t^4*(1-t)^4.
    All inequalities below use Fraction arithmetic and the existing exact
    Taylor remainder enclosures.  No floating inverse is treated as exact.
    """
    a,b=F(a_text),F(b_text);pi=pi_interval();one=(F(1),F(1))
    I={0:divide((3*(2*a+b),)*2,scale(pi,F(2)))}
    for w in [1,2,3,4,6]:
        si,co=sincos(w*a);re,im=beta_characteristic(w*b)
        I[w]=scale(divide(add(mul(si,re),mul(co,im)),pi),F(3,w))
    G=[[add(one,neg(I[0])),I[3]],
       [I[3],scale(add(add(one,neg(I[0])),neg(I[6])),F(1,2))]]
    V=[[I[0],I[1]],[neg(I[3]),scale(neg(add(I[2],I[4])),F(1,2))]]
    det=add(mul(G[0][0],G[1][1]),neg(mul(G[0][1],G[1][0])))
    if det[0]<=0:raise ArithmeticError('Exact interval determinant does not prove positivity')
    inv=[[divide(G[1][1],det),divide(neg(G[0][1]),det)],
         [divide(neg(G[1][0]),det),divide(G[0][0],det)]]
    D=[[add(mul(inv[i][0],V[0][j]),mul(inv[i][1],V[1][j])) for j in range(2)] for i in range(2)]
    return dict(projection=D,determinant=det,gram=G,moment_rhs=V)


class CircleTraceReplacementBasis:
    def __init__(self,base_mode=3,modes=16,halfwidth=.21,transition=.4,
                 center=math.pi/3,precision=80,quadrature_order=64,lock_fundamental=True):
        self.n=int(base_mode);self.M=int(modes)
        self.a=float(halfwidth);self.eps=float(transition);self.center=float(center)
        self.T=2*math.pi/3;self.keep=self.M-3
        if self.n!=3 or self.M<4 or not lock_fundamental or abs(self.center-math.pi/3)>1e-12:
            raise ValueError('This new finite space requires n3, M>=4, centre pi/3 and mean/primary locking')
        self.precision=int(precision);self.lock_fundamental=True
        # Keep the original full-M implementation before slicing: no alternative
        # formula is introduced for any of the retained raw columns.
        self.raw=ComplementaryMomentBasis(base_mode=3,modes=self.M,halfwidth=self.a,
            transition=self.eps,center=self.center,precision=self.precision,
            quadrature_order=quadrature_order,lock_fundamental=True)
        self.trace=CircleTraceControls(self.a,self.eps,self.precision)
        self.trace_certificate=trace_projection_enclosures(str(self.a),str(self.eps))
        original_interval=self.trace_certificate['projection']
        interval=[[add(row[0],neg(row[1])),row[1]] for row in original_interval]
        self.projection_intervals=interval
        D=self.trace.constants['low_projection']@np.array([[1.,0.],[-1.,1.]])
        self.trace_projection=D
        absolute=[[upper_abs(interval[i][j]) for j in range(2)] for i in range(2)]
        error=[[max(abs(F.from_float(float(D[i,j]))-v) for v in interval[i][j]) for j in range(2)] for i in range(2)]
        cut=[cutoff_derivative_upper(k)/F(str(self.eps))**k for k in range(5)]
        self.cutoff_rational_bounds=cut
        extent=F(str(self.a))+F(str(self.eps))
        difference_jet_bounds=[min(F(2),extent**2/2),min(F(1),extent),F(1),min(F(1),extent),F(1)]
        bound=[];err=[]
        for k in range(5):
            low0=cut[k]
            low1=sum(F(math.comb(k,l))*cut[l]*3**(k-l) for l in range(k+1))
            seeds=[sum(F(math.comb(k,l))*cut[l]*difference_jet_bounds[k-l] for l in range(k+1)),
                   sum(F(math.comb(k,l))*cut[l] for l in range(k+1))]
            bound.append([upper_float(seeds[j]+absolute[0][j]*low0+absolute[1][j]*low1) for j in range(2)])
            err.append([upper_float(error[0][j]*low0+error[1][j]*low1) for j in range(2)])
        self.derivative_bounds=np.concatenate((self.raw.derivative_bounds[:5,:self.keep],np.asarray(bound)),axis=1)
        self.coefficient_evaluation_error_bounds=np.concatenate((
            self.raw.coefficient_evaluation_error_bounds[:5,:self.keep],np.asarray(err)),axis=1)
        self.fundamental_evaluation_error=np.zeros(self.M-1)
        self.fundamental_absolute_upper=np.zeros(self.M-1)
        self.fundamental_leakage=np.zeros(self.M-1)
        self.gx,self.gw=np.polynomial.legendre.leggauss(32)

    @staticmethod
    def _endpoint(homotopy):
        if homotopy!=1.:raise ValueError('The circle-trace replacement defines only the lambda-one endpoint')

    def support_jets(self,phi,order=4,homotopy=1.):
        self._endpoint(homotopy)
        raw=self.raw.support_jets(phi,order,1.)
        flat=np.asarray(phi,float).ravel();d,chi=self.trace.cutoff_jets(flat,order)
        W=(1-chi[0],)+tuple(-v for v in chi[1:])
        difference=[2*np.sin(d/2)**2,np.sin(d),np.cos(d),-np.sin(d),-np.cos(d)]
        trace=[]
        for r in range(order+1):
            first=sum(math.comb(r,k)*chi[k]*difference[r-k] for k in range(r+1))
            second=sum(math.comb(r,k)*chi[k]*np.cos(d+(r-k)*np.pi/2) for k in range(r+1))
            low0=W[r]
            low1=sum(math.comb(r,k)*W[k]*3**(r-k)*np.cos(3*flat+(r-k)*np.pi/2) for k in range(r+1))
            trace.append(np.stack((first,second))-self.trace_projection.T@np.stack((low0,low1)))
        return tuple(np.concatenate((r[:self.keep],t),axis=0) for r,t in zip(raw,trace))

    def trace_primitive(self,phi):
        """The defining odd primitive int_0^d S(center+t)dt, evaluated piecewise.

        On the protected arc it is (d-sin d,sin d).  On the far complement mean
        zero permits integration backwards from the reflection axis.  Only
        the transition uses a 32-point Gauss evaluation of the explicit
        degree-nine polynomial times frequencies at most three.
        """
        d=self.trace.local(np.asarray(phi,float).ravel());x=abs(d)
        out=np.zeros((2,len(x)))
        inner=x<=self.a
        out[0,inner]=x[inner]-np.sin(x[inner]);out[1,inner]=np.sin(x[inner])
        transition=(x>self.a)&(x<self.a+self.eps)
        if np.any(transition):
            length=x[transition]-self.a
            points=self.a+length[:,None]*(self.gx+1)/2
            values=self.support_jets(self.center+points.ravel(),0)[0][-2:].reshape(2,len(length),len(self.gx))
            integral=length[None,:]/2*np.einsum('jkq,q->jk',values,self.gw)
            out[:,transition]=np.array([self.a-math.sin(self.a),math.sin(self.a)])[:,None]+integral
        far=x>=self.a+self.eps
        if np.any(far):
            length=self.T/2-x[far];D=self.trace_projection
            out[:,far]=length[None,:]*(D[0,:,None]+D[1,:,None]*np.sinc(3*length[None,:]/np.pi))
        return out*np.sign(d)[None,:]

    def primitive_jets(self,phi,order=5,homotopy=1.):
        self._endpoint(homotopy)
        if not 0<=order<=5:raise ValueError('Primitive orders zero through five only')
        raw=self.raw.primitive(phi,1.)[:self.keep]
        primitive=np.concatenate((raw,self.trace_primitive(phi)),axis=0)
        return (primitive,) if order==0 else (primitive,)+self.support_jets(phi,order-1,1.)

    def homotopy_rho_bounds(self,homotopy=1.):
        self._endpoint(homotopy)
        return tuple(self.derivative_bounds[k]+self.derivative_bounds[k+2] for k in range(3))

    def combined_control_rho_bounds(self,coefficients,homotopy=1.):
        """Whole-domain rho/rho'/rho'' bounds after combining both trace columns.

        Physical trace coordinates are (t,u), with A=t and B=u-t.  On the
        protected arc the support trace is t+(u-t)*cos(d), and rho trace t.
        Combine this seed and both low projection coefficients before taking
        absolute values.  In particular u=0 retains the SA-SB cancellation.
        No sampled derivative maximum enters this budget.
        """
        self._endpoint(homotopy)
        c=np.asarray(coefficients,float)
        if c.shape!=(self.M-1,) or not np.all(np.isfinite(c)):raise ValueError('Complete finite physical controls required')
        t,u=map(lambda v:F.from_float(float(v)),c[-2:]);delta=t-u
        extent=F(str(self.a))+F(str(self.eps));cut=self.cutoff_rational_bounds
        g0=min(abs(t)+abs(u-t),abs(u)+abs(delta)*min(F(2),extent**2/2))
        g1=abs(delta)*min(F(1),extent);g2=abs(delta)
        seed=[abs(t)+2*cut[1]*g1+cut[2]*g0,
              cut[1]*abs(t)+3*cut[2]*g1+2*cut[1]*g2+cut[3]*g0,
              cut[2]*abs(t)+4*cut[3]*g1+5*cut[2]*g2+2*cut[1]*g1+cut[4]*g0]
        low=[upper_abs(add(scale(row[0],t),scale(row[1],u))) for row in self.projection_intervals]
        raw=self.raw.homotopy_rho_bounds(1.)
        result=[]
        for k in range(3):
            low0=cut[k]+cut[k+2]
            low1=sum(F(math.comb(k,l))*3**(k-l)*(8*cut[l]+6*cut[l+1]+cut[l+2]) for l in range(k+1))
            remaining=sum(abs(F.from_float(float(c[j])))*F.from_float(float(raw[k][j])) for j in range(self.keep))
            result.append(upper_float(remaining+seed[k]+low[0]*low0+low[1]*low1))
        return tuple(result)

    def summary(self):
        det=self.trace_certificate['determinant']
        return dict(base_mode=3,modes=self.M,halfwidth=self.a,transition=self.eps,center=self.center,
            controls=self.M-1,retained_raw_indices=list(range(2,self.M-1)),
            replacement_indices=[self.M-1,self.M],replacement_columns=['T=SA-SB','U=SB'],
            physical_trace_coordinates='(t,u) map to (A,B)=(t,u-t); d/dt=T, d/du=U',
            finite_span='span(B2,...,B(M-2),T,U)=span(B2,...,B(M-2),SA,SB); a new space, not the old raw span',
            low_constraints='Defining mean and cos(3 phi) support moments both zero',
            control_path='circle-trace-replace-last-two-v1',homotopy='lambda=1 only',
            trace_projection_float=self.trace_projection.tolist(),
            exact_rational_determinant_lower=float(det[0]),
            projection_float_value_error_upper=float(np.max(self.coefficient_evaluation_error_bounds[0,-2:])),
            trace_support_derivative_upper_bounds=self.derivative_bounds[:5,-2:].T.tolist(),
            primitive_definition='Odd primitive about pi/3; zero again at the opposite reflection axis by the exact mean constraint',
            numerical_transition_quadrature_order=32,
            positivity_budget='Raw retained columns plus a combined trace seed and combined low projection; no sampled maxima',
            scope='Exact defining-integral finite space with rational coefficient enclosures. '
                'Floating evaluation and the inherited source positivity guard are not a complete geometry certificate.')
