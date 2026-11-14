#!/usr/bin/env python3
"""Same true cap form with the scalar axis curvature cancellation paid first.

The identity C^2(L^2-L')+L C C'=Z'(a' Z''-a'' Z')/a^5 is formed in full
scalar polynomial coefficients.  An exact dyadic constant is subtracted
before evaluation, so the common complex a^5 factor is not independently
wrapped.  Complete nonaxis mean-energy and infinite-primitive errors remain.
"""
import math
import numpy as np
from flint import acb
from fourfold_phase_beta_bulk_box import CBox,Box,cdot,arb_box,reduce_box
from fourfold_phase_cap_scaled_body import poly_eval,magnitude
from fourfold_phase_cap_vector_germs import VectorScaledBodyForm,derivative,multiply,subtract


class CorrelatedCurvatureBodyForm(VectorScaledBodyForm):
    def set_cell(self,left,right):
        previous=self.cell
        super().set_cell(left,right)
        if previous==self.cell and hasattr(self,'axis_remainder'):
            return
        a,z=self.scalar_poly[:,-2],self.scalar_poly[:,-1]
        ar,zr=derivative(a),derivative(z)
        arr,zrr=derivative(ar),derivative(zr)
        numerator=multiply(zr,subtract(multiply(ar,zrr),multiply(arr,zr)))
        a2=multiply(a,a)
        a5=multiply(multiply(a2,a2),a)
        self.axis_constant=float((numerator[0]/(a[0]**5)).to_acb().real.mid())
        self.axis_remainder=subtract(numerator,self.axis_constant*a5)

    def normalized_data(self,radial):
        primitive,radius=self.unit_finite_data(radial)
        errors=self.unit_tail_errors(radial)
        L,Lp,C,Cp,ia=self.scalar_ratios(radial,radius)
        reverse=(-np.arange(self.nodes))%self.nodes
        u=L*primitive[0]+primitive[1]
        ur=Lp*primitive[0]+L*primitive[1]+primitive[2]
        ebar=2*L*u[0,0]+cdot(u,u[reverse]).sum()
        ebar_r=2*Lp*u[0,0]+2*L*ur[0,0]+2*cdot(u,ur[reverse]).sum()
        eps=[arb_box(math.factorial(j)*errors[0]/self.tail_radius**j) for j in range(3)]
        Labs,Lpabs=magnitude(L),magnitude(Lp)
        eu=Labs*eps[0]+eps[1]
        eur=Lpabs*eps[0]+Labs*eps[1]+eps[2]
        Mu=Box(np.max(reduce_box(Box(u.magnitude_upper())).hi))
        Mur=Box(np.max(reduce_box(Box(ur.magnitude_upper())).hi))
        fee0=2*Labs*eu+3*(2*Mu*eu+eu*eu)
        fee1=2*Lpabs*eu+2*Labs*eur+6*(Mu*eur+Mur*eu+eu*eur)
        real=radial.imag==0
        ebar,ebar_r=ebar.pad(fee0,real),ebar_r.pad(fee1,real)
        a=radius[0]
        Ebar=L*L+a*a*C*C+ebar
        delta=CBox.from_acb(radial-acb(self.anchor))
        axis=self.axis_constant+poly_eval(self.axis_remainder,delta)*ia**5
        K=(axis+(L*ebar_r-2*Lp*ebar)*ia*ia/2)/(Ebar*Ebar)
        if real:K=CBox(K.real)
        self.last_scaled_diagnostics=dict(Ebar=Ebar.to_acb(),L=L.to_acb(),
            Lprime=Lp.to_acb(),C=C.to_acb(),Cprime=Cp.to_acb(),
            correlated_axis=axis.to_acb(),
            normalized_E_errors=[float(fee0.hi),float(fee1.hi)])
        return primitive,K,errors,real,(L,Lp,C,Cp,ia)
