"""Two exact defining circle-trace controls, beyond supported raw controls.

The mathematical definition uses explicit integrals and a positive 2x2 moment
matrix inverse.  mpmath and binary64 evaluations below are numerical evaluations
of that definition, not interval certificates.  No BVP or running core imports
this prototype.  The two columns are ordered (radius trace, centre trace).

The locally defined cos(d) is repeated with period 2*pi/3 only after it has
been multiplied by chi.  It is not the global harmonic cos(3*phi).
"""
from __future__ import annotations
import math
import numpy as np
from numpy.polynomial import Polynomial
import mpmath as mp


SMOOTH_COEFFICIENTS=(0,0,0,0,0,126,-420,540,-315,70)


def defining_moments(halfwidth,transition,precision=80):
    """Normalised full-circle moments; centre is exactly pi/3 in the definition.

    I(w)=(2/T)*integral_0^(a+b) chi(d)*cos(w*d) dd.
    G rows/columns are the weighted {1,cos(3*phi)} moments with weight W=1-chi.
    V columns are chi and chi*cos(d); D=G^-1 V gives low subtraction columns.
    """
    with mp.workdps(precision):
        a,b=mp.mpf(str(halfwidth)),mp.mpf(str(transition))
        T=2*mp.pi/3
        if not 0<a<a+b<T/2:
            raise ValueError('Require 0<a<a+b<pi/3')
        def moment(omega):
            omega=mp.mpf(omega)
            if not omega:return (2*a+b)/T
            iz=mp.j*omega*b;e=mp.exp(iz)
            powers=[mp.expm1(iz)/iz]
            for k in range(1,10):powers.append(e/iz-k*powers[-1]/iz)
            cut=powers[0]-sum(SMOOTH_COEFFICIENTS[k]*powers[k] for k in range(10))
            return 2/T*(mp.sin(omega*a)/omega+b*mp.re(mp.exp(mp.j*omega*a)*cut))
        I={k:moment(k) for k in (0,1,2,3,4,6)}
        # cos(3*phi)=-cos(3*d) on the sector centred at pi/3.
        G=mp.matrix([[1-I[0],I[3]],[I[3],(1-I[0]-I[6])/2]])
        V=mp.matrix([[I[0],I[1]],[-I[3],-(I[2]+I[4])/2]])
        D=G**-1*V
        determinant=mp.det(G)
        if determinant<=0:raise ArithmeticError('Positive moment matrix evaluation failed')
        residual=max(abs((G*D-V)[i,j]) for i in range(2) for j in range(2))
        floats=lambda x:np.array([[float(x[i,j]) for j in range(x.cols)] for i in range(x.rows)])
        decimals=lambda x:[[mp.nstr(x[i,j],precision-10) for j in range(x.cols)] for i in range(x.rows)]
        return dict(low_gram=floats(G),moment_rhs=floats(V),low_projection=floats(D),
            low_gram_decimal=decimals(G),moment_rhs_decimal=decimals(V),
            low_projection_decimal=decimals(D),determinant_decimal=mp.nstr(determinant,precision-10),
            high_precision_constraint_residual=mp.nstr(residual,12),
            cosine_moments={str(k):mp.nstr(v,precision-10) for k,v in I.items()})


class CircleTraceControls:
    """C4, even/C3, zero-mean/primary controls with traces 1 and cos(d)."""
    def __init__(self,halfwidth=.21,transition=.4,precision=80):
        self.a=float(halfwidth);self.b=float(transition);self.precision=int(precision)
        self.T=2*math.pi/3;self.L=self.T/2;self.center=math.pi/3
        if not 0<self.a<self.a+self.b<self.L:raise ValueError('Require 0<a<a+b<pi/3')
        self.constants=defining_moments(halfwidth,transition,self.precision)
        self.low_projection=self.constants['low_projection'].copy()
        smooth=Polynomial(SMOOTH_COEFFICIENTS)
        self.smooth_derivatives=[smooth.deriv(k) for k in range(5)]

    def local(self,phi):
        x=np.asarray(phi,float)-self.center
        return x-np.floor((x+self.L)/self.T)*self.T

    def cutoff_jets(self,phi,order=4):
        if not 0<=order<=4:raise ValueError('This interface exposes the global C4 jets only')
        d=self.local(phi);distance=abs(d);t=np.clip((distance-self.a)/self.b,0.,1.)
        interior=(distance>self.a)&(distance<self.a+self.b)
        jets=[np.where(distance<=self.a,1.,np.where(distance>=self.a+self.b,0.,
            1-self.smooth_derivatives[0](t)))]
        for k in range(1,order+1):
            jets.append(np.where(interior,-self.smooth_derivatives[k](t)*np.sign(d)**k/self.b**k,0.))
        return d,tuple(jets)

    def support_jets(self,phi,order=4):
        phi=np.asarray(phi,float);shape=phi.shape;flat=phi.ravel()
        d,chi=self.cutoff_jets(flat,order)
        W=(1-chi[0],)+tuple(-x for x in chi[1:])
        output=[]
        for r in range(order+1):
            # Leibniz rule for the locally repeated chi*cos(d).
            centre_seed=sum(math.comb(r,k)*chi[k]*np.cos(d+(r-k)*math.pi/2)
                            for k in range(r+1))
            seeds=np.stack((chi[r],centre_seed))
            low0=W[r]
            low1=sum(math.comb(r,k)*W[k]*3**(r-k)*
                np.cos(3*flat+(r-k)*math.pi/2) for k in range(r+1))
            value=seeds-self.low_projection.T@np.stack((low0,low1))
            output.append(value.reshape((2,)+shape))
        return tuple(output)

    def rho_jets(self,phi):
        b=self.support_jets(phi,4)
        return b[0]+b[2],b[1]+b[3],b[2]+b[4]

    def position_increment(self,phi,coefficients):
        """Actual project normal convention: delta Gamma=b*e_r+b'*e_theta."""
        phi=np.asarray(phi,float);coefficients=np.asarray(coefficients,float)
        if coefficients.shape!=(2,):raise ValueError('Use (radius trace A, centre trace B)')
        jets=self.support_jets(phi,1)
        b=np.tensordot(coefficients,jets[0],axes=(0,0))
        bp=np.tensordot(coefficients,jets[1],axes=(0,0))
        er=np.stack((np.cos(phi),np.sin(phi)),axis=-1)
        et=np.stack((-np.sin(phi),np.cos(phi)),axis=-1)
        return b[...,None]*er+bp[...,None]*et

    def summary(self):
        return dict(base_mode=3,halfwidth=self.a,transition=self.b,center='pi/3',
            precision=self.precision,column_order=['radius trace','centre trace'],
            normalized_inner_product='(2*pi)^(-1) integral_0^(2*pi)',
            defining_local_cosine='cos(d), with d in [-pi/3,pi/3), multiplied by chi before C3 repetition',
            low_basis=['1','cos(3*phi)'],projection_order='rows: low basis; columns: radius and centre seeds',
            low_gram_decimal=self.constants['low_gram_decimal'],
            moment_rhs_decimal=self.constants['moment_rhs_decimal'],
            low_projection_decimal=self.constants['low_projection_decimal'],
            determinant_decimal=self.constants['determinant_decimal'],
            high_precision_constraint_residual=self.constants['high_precision_constraint_residual'],
            scope='Explicit defining-integral prototype. Floating evaluations are not interval certificates, '
                'and these two new columns have not been installed in a production BVP.')
