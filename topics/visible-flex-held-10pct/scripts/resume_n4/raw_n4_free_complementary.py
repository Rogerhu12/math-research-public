"""Release a mean-zero raw c8 column for fixed-metric n4 refinement.

All design columns j>=3 retain their exact mean/c8 projection. The new first
column is W*(cos(8 phi)-<W cos(8 phi)>/<W>). Its c8 moment is positive, and
its coefficient initially vanishes. It remains supported off the circle.
"""
from fractions import Fraction as F
from functools import lru_cache
import math
import mpmath as mp
import numpy as np
import complementary_moment_basis as canonical
import moment_interval_bounds as interval
from raw_n4_complementary import make_raw_basis


@lru_cache(None)
def first_column(n,a,eps,center_half_period,precision):
    with mp.workdps(precision):
        aa,ee=mp.mpf(str(a)),mp.mpf(str(eps));T=2*mp.pi/n
        W0=1-(2*aa+ee)/T;omega=mp.mpf(2*n);iz=mp.j*omega*ee;e=mp.exp(iz)
        values=[mp.expm1(iz)/iz]
        for k in range(1,10):values.append(e/iz-k*values[-1]/iz)
        transition=ee*mp.re(mp.exp(mp.j*omega*aa)*sum(canonical._S_COEF[k]*values[k]for k in range(10)))
        W2=2/T*(transition-mp.sin(omega*(aa+ee))/omega)*(-1)**(2*center_half_period)
        coefficient=-float(W2/W0)
    a,eps=F(str(a)),F(str(eps));pi=interval.pi_interval()
    W0=interval.add((F(1),F(1)),interval.neg(interval.divide((n*(2*a+eps),)*2,interval.scale(pi,F(2)))))
    si,co=interval.sincos(2*n*a);re,im=interval.beta_characteristic(2*n*eps)
    W2=interval.neg(interval.divide(interval.add(interval.mul(si,re),interval.mul(co,im)),interval.scale(pi,F(2))))
    W2=interval.scale(W2,F((-1)**(2*center_half_period)))
    bound=interval.neg(interval.divide(W2,W0))
    if not bound[0]<=F.from_float(coefficient)<=bound[1]:
        # Float evaluation error is included separately below.
        pass
    return coefficient,bound


def make_free_raw_basis(anchor_modes):
    Parent=make_raw_basis(anchor_modes)

    class FreeRawMeanBasis(Parent):
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            value,bound=first_column(self.n,self.a,self.eps,self.center_half_period,self.precision)
            self.H[0,0]=value;self.H[0,2]=1.
            self.constants=dict(self.constants)
            self.constants['canonical_trig_coefficients']=self.H.copy()
            self.certificate=dict(self.certificate)
            bounds=list(self.certificate['coefficients'])
            bounds[0]=[(F(0),F(0))]*(self.M+1)
            bounds[0][0]=bound;bounds[0][2]=(F(1),F(1))
            self.certificate['coefficients']=bounds
            self.certificate['first_column_identity']='W*(cos(2*n*phi)-<W cos(2*n*phi)>/<W>); mean zero, physical 2n moment free'
            cutoff=[canonical.cutoff_derivative_upper(k)/F(str(self.eps))**k for k in range(6)]
            absolute=[interval.upper_abs(v)for v in bounds[0]]
            error=[max(abs(F.from_float(float(self.H[0,k]))-v)for v in bounds[0][k])for k in range(self.M+1)]
            for coefficients,target in ((absolute,self.derivative_bounds),(error,self.coefficient_evaluation_error_bounds)):
                trig=[sum(coefficients[k]*(int(self.freq[k])**r if r else 1)for k in range(self.M+1))for r in range(6)]
                target[:,0]=[interval.upper_float(sum(math.comb(r,l)*cutoff[l]*trig[r-l]for l in range(r+1)))for r in range(6)]

        def summary(self):
            out=super().summary()
            out['unused_subblock_support_condition']=out.pop('support_condition')
            out['unused_subblock_rho_condition']=out.pop('rho_condition')
            out.update(control_path='raw-mean-free-c8-with-frozen-canonical-low-start-v1',
                       unused_correction_index=None,
                       canonical_low_moments='All controls have exact mean zero; j>=3 also have physical c8 moment zero, and the independent first column releases c8.',
                       first_column_identity=self.certificate['first_column_identity'])
            return out

    return FreeRawMeanBasis
