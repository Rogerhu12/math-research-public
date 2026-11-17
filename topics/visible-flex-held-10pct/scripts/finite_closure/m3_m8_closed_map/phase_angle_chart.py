"""A literal C2 material-angle chart for the finite closed-map phase action.

The geometry coefficients are unchanged. Frozen source chart values and jets
are converted to one shared two-jet per radial knot, so C2 regularity does not
depend on separately rounded CubicSpline polynomial endpoint identities.
Every Bernstein bound below is computed with exact Fraction arithmetic.
"""
from fractions import Fraction as Q
import math
import numpy as np
from shared_jet import SharedJetQuintic

class PhaseAngleChart:
    def __init__(self,prefix):
        self.prefix=prefix;s=prefix.rep.x;flow=prefix.flow
        e=self.source_e(s)
        e[:,0]=[prefix.E0,0.,prefix.Epp];e[:,-1]=0.
        self.rep=SharedJetQuintic(s,e[:,None,:])
        self.absolute_e_bound=self.bernstein_bound(s,e)
        if not self.absolute_e_bound<1:raise ValueError('Phase angle is not certified invertible')
        self.rho_lower=1-self.absolute_e_bound
        ss=np.unique(np.r_[s,(s[:-1]+s[1:])/2])
        self.numeric_difference=np.max(abs(np.stack([self.rep(ss,j)[0]for j in range(3)])-self.source_e(ss)),axis=1)

    def source_e(self,s):
        flow=self.prefix.flow;s=np.asarray(s,float);x=s/flow.end
        t=np.clip(4*x-3,0,1);fac=4/flow.end
        cut=1-t**3*(10+t*(-15+6*t));cp=-30*t*t*(1-t)**2*fac;cpp=-60*t*(1-t)*(1-2*t)*fac**2
        h=flow.spline(x);hp=flow.spline(x,1)/flow.end;hpp=flow.spline(x,2)/flow.end**2
        return np.stack([flow.warp_e*h*cut,flow.warp_e*(hp*cut+h*cp),
            flow.warp_e*(hpp*cut+2*hp*cp+h*cpp)])

    @staticmethod
    def bernstein_bound(knots,jets):
        bound=Q(0)
        for i in range(len(knots)-1):
            h=Q.from_float(float(knots[i+1]))-Q.from_float(float(knots[i]))
            y0,d0,q0=[Q.from_float(float(jets[j,i]))for j in range(3)]
            y1,d1,q1=[Q.from_float(float(jets[j,i+1]))for j in range(3)]
            e0=y1-y0-h*d0-h*h*q0/2;e1=d1-d0-h*q0;e2=q1-q0
            c=[y0,h*d0,h*h*q0/2,10*e0-4*h*e1+h*h*e2/2,
                -15*e0+7*h*e1-h*h*e2,6*e0-3*h*e1+h*h*e2/2]
            for k in range(6):
                b=sum((c[j]*Q(math.comb(k,j),math.comb(5,j))for j in range(k+1)),Q(0))
                bound=max(bound,abs(b))
        return bound

    def angular(self,s,psi):
        s,psi=np.broadcast_arrays(np.asarray(s,float),np.asarray(psi,float))
        e,ep,epp=[self.rep(s,j)[0]for j in range(3)]
        sn=np.sin(3*psi);co=np.cos(3*psi)
        return psi-e*sn/3,1-e*co,3*e*sn,-ep*sn/3,-epp*sn/3,-ep*co

    def inverse(self,s,theta):
        s,theta=np.broadcast_arrays(np.asarray(s,float),np.asarray(theta,float));psi=theta.copy()
        for _ in range(30):
            value,rho,*_=self.angular(s,psi);change=(value-theta)/rho;psi-=change
            if np.max(abs(change))<2e-15:break
        if np.max(abs(self.angular(s,psi)[0]-theta))>2e-13:raise ValueError('Material angle inversion failed')
        return psi

    def report(self):
        def q(x):return dict(numerator=str(x.numerator),denominator=str(x.denominator),display_only=float(x))
        return dict(definition='Shared radial two-jet quintic e(s); theta=psi-e(s)sin(3psi)/3.',
            exact_absolute_e_upper=q(self.absolute_e_bound),exact_rho_lower=q(self.rho_lower),
            radial_spans=len(self.rep.x)-1,exact_center_two_jet=True,exact_zero_cut_two_jet=True,
            numerical_source_chart_difference_orders_0_1_2=self.numeric_difference.tolist(),
            geometry_coefficients_changed=False,metric_reaudited_in_this_query=False)
