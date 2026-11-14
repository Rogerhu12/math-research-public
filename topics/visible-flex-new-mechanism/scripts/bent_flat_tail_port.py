#!/usr/bin/env python3
"""Exact developable S11 bent-flat ports, with a globally fixed angle lift.

The mathematical functions Y and H are integrals, not fitted polynomials.
Floating quadrature below evaluates those definitions without certifying its
error. Scalar jets use finite Taylor algebra and no angular differencing.
The CLI only checks artificial interfaces; research evaluation is by Actions.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

from cosine_connector_radial_seed import s11


def exact(value):
    return Q.from_float(float(value)) if isinstance(value,(float,np.floating)) else Q(value)


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


class Jet22:
    """Taylor coefficients in (core-to-cap t, theta), degree <=2 in each variable.

    Coefficients include 1/(i!j!). Truncation is the quotient by (t^3,theta^3),
    so elementary compositions through total degree four give every stored jet.
    """
    def __init__(self,coefficients):
        self.c=np.asarray(coefficients,float)
        if self.c.shape[:2]!=(3,3):raise ValueError('a 3 by 3 coefficient prefix is required')

    @classmethod
    def constant(cls,value):
        value=np.asarray(value,float);out=np.zeros((3,3)+value.shape);out[0,0]=value
        return cls(out)

    @classmethod
    def variable(cls,value,axis,derivative=1.):
        result=cls.constant(value);result.c[1,0] = derivative if axis==0 else 0.
        result.c[0,1] = derivative if axis==1 else 0.
        return result

    def _other(self,value):
        return value if isinstance(value,Jet22) else Jet22.constant(np.broadcast_to(value,self.c.shape[2:]))

    def __add__(self,other):return Jet22(self.c+self._other(other).c)
    __radd__=__add__
    def __neg__(self):return Jet22(-self.c)
    def __sub__(self,other):return self+-self._other(other)
    def __rsub__(self,other):return self._other(other)+-self
    def __mul__(self,other):
        other=self._other(other);out=np.zeros_like(self.c)
        for i in range(3):
            for j in range(3):
                for k in range(i+1):
                    for l in range(j+1):out[i,j]+=self.c[k,l]*other.c[i-k,j-l]
        return Jet22(out)
    __rmul__=__mul__
    def __truediv__(self,other):return self*self._other(other).reciprocal()
    def __rtruediv__(self,other):return self._other(other)*self.reciprocal()

    def compose(self,derivatives):
        if len(derivatives)!=5:raise ValueError('derivatives zero through four are required')
        difference=Jet22(self.c.copy());difference.c[0,0]=0.
        result=Jet22.constant(np.broadcast_to(derivatives[0],self.c.shape[2:]))
        power=Jet22.constant(np.ones(self.c.shape[2:]))
        for k in range(1,5):
            power=power*difference
            result=result+power*(np.asarray(derivatives[k])/math.factorial(k))
        return result

    def reciprocal(self):
        value=self.c[0,0]
        if np.any(value==0):raise ValueError('zero denominator in a scalar chart')
        return self.compose([(-1)**k*math.factorial(k)*value**(-k-1) for k in range(5)])

    def sin(self):
        x=self.c[0,0];s,c=np.sin(x),np.cos(x)
        return self.compose([s,c,-s,-c,s])

    def cos(self):
        x=self.c[0,0];s,c=np.sin(x),np.cos(x)
        return self.compose([c,-s,-c,s,c])

    def atan(self):
        x=self.c[0,0];d=1+x*x
        return self.compose([np.arctan(x),1/d,-2*x/d**2,(6*x*x-2)/d**3,
                             24*x*(1-x*x)/d**4])

    def sqrt(self):
        x=self.c[0,0]
        if np.any(x<=0):raise ValueError('positive square root chart required')
        return self.compose([np.sqrt(x),.5*x**(-.5),-.25*x**(-1.5),
                             .375*x**(-2.5),-.9375*x**(-3.5)])

    def result(self):
        return {'value':self.c[0,0],'s':self.c[1,0],'ss':2*self.c[2,0],
                'theta':self.c[0,1],'st':self.c[1,1],'tt':2*self.c[0,2],
                'ss_theta':2*self.c[2,1],'ss_thetatheta':4*self.c[2,2]}


def smoothstep_derivative(x,order):
    """Clamped S11 and its first five derivatives, stable at either endpoint."""
    x=np.asarray(x,float)
    if order==0:return s11(np.clip(x,0.,1.))
    if not 1<=order<=5:raise ValueError('S11 derivatives zero through five only')
    y=np.clip(x,0.,1.);n=order-1;result=np.zeros_like(y)
    for k in range(n+1):
        if k<=5 and n-k<=5:
            coefficient=(2772*math.comb(n,k)*math.factorial(5)//math.factorial(5-k)*
                         math.factorial(5)//math.factorial(5-(n-k))*(-1)**(n-k))
            result+=coefficient*y**(5-k)*(1-y)**(5-(n-k))
    return np.where((x>0)&(x<1),result,0.)


class BentFlatTail:
    """P_sigma=(r cos theta,Y(r sin theta),sigma*(h-H(r sin theta))).

    Derivatives labelled s are along core-to-cap t, with dr/dt=-1.
    The additive height h is a single cap constant. It is not a shape parameter
    in the connector: reconstruction determines it from the common center.
    """
    def __init__(self,cut_radius='11/50',bend_width='27/500',amplitude='1/4',side=1):
        self.cut_exact,self.width_exact,self.amplitude_exact=map(exact,(cut_radius,bend_width,amplitude))
        if not self.cut_exact>0 or not self.width_exact>0 or not 0<self.amplitude_exact<Q('3/4') or side not in [-1,1]:
            raise ValueError('positive radii, 0<amplitude<3/4 and side +/-1 required')
        self.cut=float(self.cut_exact);self.width=float(self.width_exact)
        self.amplitude=float(self.amplitude_exact);self.side=int(side)
        self.outer_exact=self.cut_exact+self.width_exact;self.outer=float(self.outer_exact)
        self.curvature_upper_exact=self.amplitude_exact/self.width_exact*Q(693,256)
        self.height_drop_upper_exact=self.amplitude_exact*self.width_exact/2
        self.identity={'schema':'S11-saturated-bent-flat-tail-v1',
            'cut_radius':str(self.cut_exact),'bend_width':str(self.width_exact),
            'outer_radius':str(self.outer_exact),'bend_amplitude':str(self.amplitude_exact),
            'side':self.side,'radial_derivative_dr_dt':-1,
            'alpha_definition':'sign(y)*bend_amplitude*S11((abs(y)-cut_radius)/bend_width)',
            'smoothstep_polynomial_coefficients':['0']*6+['462','-1980','3465','-3080','1386','-252'],
            'smoothstep_extension':'0 on x<=0; 1 on x>=1',
            'Y_definition':'integral_0^y cos(alpha(v)) dv',
            'H_definition':'integral_0^y sin(alpha(v)) dv',
            'position_definition':'(r*cos(theta),Y(r*sin(theta)),side*(h-H(r*sin(theta))))',
            'height_definition':'one h=side*z_center_at_inner_circle from the common anchored reconstruction',
            'beta_lift':'-side*pi+side*atan(sin(theta)*tan(alpha(r*sin(theta))))',
            'held_closed_disk':'r<=cut_radius; fixed for every phase, with nonempty interior',
            'regularity':'alpha C5, P C6; no jointly analytic extension across onset curves',
            'quadrature_is_evaluation_not_part_of_the_physical_definition':True}
        self.identity_sha256=digest(self.identity)
        self._full_integrals={}

    def alpha_jets(self,y,maximum=4):
        y=np.asarray(y,float);z=(abs(y)-self.cut)/self.width;sign=np.sign(y)
        if not 0<=maximum<=5:raise ValueError('alpha derivatives through order five only')
        return [self.amplitude*sign**(k+1)*smoothstep_derivative(z,k)/self.width**k
                for k in range(maximum+1)]

    def scalar_jets(self,radius,theta):
        radius,theta=np.broadcast_arrays(np.asarray(radius,float),np.asarray(theta,float))
        if np.any(radius<0):raise ValueError('nonnegative radius required')
        r=Jet22.variable(radius,0,-1.);angle=Jet22.variable(theta,1)
        sine,cosine=angle.sin(),angle.cos();y=r*sine
        alpha=y.compose(self.alpha_jets(y.c[0,0],4));C,S=alpha.cos(),alpha.sin()
        u=(sine*cosine*(1-C)/(sine*sine+cosine*cosine*C)).atan()
        horizontal=(1-cosine*cosine*S*S).sqrt()
        v=-self.side*cosine*S/horizontal
        beta=-self.side*np.pi+self.side*(sine*S/C).atan()
        return {'u':u.result(),'v':v.result(),'beta':beta.result(),
            'tail_physical_identity_sha256':self.identity_sha256,
            'radial_derivative_convention':'dr/ds=-1',
            'floating_jets_are_not_interval_bounds':True}

    def integrals(self,y,quadrature_order=32):
        y=np.asarray(y,float);absolute=abs(y);distance=np.maximum(absolute-self.cut,0)
        span=np.minimum(distance,self.width);nodes,weights=leggauss(int(quadrature_order))
        local=span[...,None]*(nodes+1)/2
        angle=self.amplitude*smoothstep_derivative(local/self.width,0)
        integral_cos=np.sum(np.cos(angle)*weights,axis=-1)*span/2
        integral_sin=np.sum(np.sin(angle)*weights,axis=-1)*span/2
        extra=np.maximum(distance-self.width,0)
        Y=np.sign(y)*(np.minimum(absolute,self.cut)+integral_cos+extra*np.cos(self.amplitude))
        H=integral_sin+extra*np.sin(self.amplitude)
        return Y,H

    def position_jets(self,radius,theta,height=0.,quadrature_order=32):
        r,theta=np.broadcast_arrays(np.asarray(radius,float),np.asarray(theta,float))
        if np.any(r<0):raise ValueError('nonnegative radius required')
        s,c=np.sin(theta),np.cos(theta);y=r*s
        alpha,ap=self.alpha_jets(y,1);C,S=np.cos(alpha),np.sin(alpha);sigma=self.side
        Y,H=self.integrals(y,quadrature_order);zero=np.zeros_like(r)
        X=np.stack((r*c,Y,sigma*(np.broadcast_to(height,r.shape)-H)),axis=-1)
        Xs=np.stack((-c,-s*C,sigma*s*S),axis=-1)
        Xt=np.stack((-r*s,r*c*C,-sigma*r*c*S),axis=-1)
        Xss=np.stack((zero,-s*s*S*ap,-sigma*s*s*C*ap),axis=-1)
        Xst=np.stack((s,-c*C+r*s*c*S*ap,sigma*c*S+sigma*r*s*c*C*ap),axis=-1)
        Xtt=np.stack((-r*c,-r*s*C-r*r*c*c*S*ap,
                      sigma*r*s*S-sigma*r*r*c*c*C*ap),axis=-1)
        return {'X':X,'Xs':Xs,'Xtheta':Xt,'Xss':Xss,'Xst':Xst,'Xtt':Xtt,
            'normal':np.stack((zero,sigma*S,C),axis=-1),
            'principal_curvature_absolute':abs(ap),'integral_quadrature_order':int(quadrature_order),
            'tail_physical_identity_sha256':self.identity_sha256,
            'quadrature_and_floating_jets_are_not_interval_bounds':True}

    def analytic_budget(self):
        return {'curvature_upper_exact':str(self.curvature_upper_exact),
            'tail_pair_normal_chord_radius_lower_exact':str(1/self.curvature_upper_exact),
            'physical_cap_height_drop_upper_exact':str(self.height_drop_upper_exact),
            'horizontal_radius_upper_exact':str(self.outer_exact),
            'whole_surface_reach_not_implied_by_tail_pair_bound':True,
            'continuous_tail_bound_source':'results/R40-bent-flat-tail-normal-chord-and-ball-budget.md'}


def developer_check():
    from frame_collar_bvp import target_frame
    checks=[];h=1e-6
    # A mild artificial cap with a wider onset interval, not the selected model.
    theta=np.array([.21,.83,1.17,1.72,2.36,3.69,5.12]);r=np.array([.39,.42,.34,.44,.41,.43,.35])
    for side in [1,-1]:
        tail=BentFlatTail('1/5','1/4','1/5',side)
        fields=tail.scalar_jets(r,theta);fields['_theta']=theta
        frame=target_frame(fields);position=tail.position_jets(r,theta,.3)
        fp=tail.scalar_jets(r-h,theta);fm=tail.scalar_jets(r+h,theta)
        gp=tail.scalar_jets(r,theta+h);gm=tail.scalar_jets(r,theta-h)
        scalar_error={}
        for name in ['u','v','beta']:
            for key,fd in [('s',(fp[name]['value']-fm[name]['value'])/(2*h)),
                           ('ss',(fp[name]['s']-fm[name]['s'])/(2*h)),
                           ('theta',(gp[name]['value']-gm[name]['value'])/(2*h)),
                           ('st',(gp[name]['s']-gm[name]['s'])/(2*h)),
                           ('tt',(gp[name]['theta']-gm[name]['theta'])/(2*h)),
                           ('ss_theta',(gp[name]['ss']-gm[name]['ss'])/(2*h))]:
                scalar_error[name+'_'+key]=float(np.max(abs(fields[name][key]-fd))/max(1.,np.max(abs(fields[name][key]))))
        xp=tail.position_jets(r-h,theta,.3);xm=tail.position_jets(r+h,theta,.3)
        tp=tail.position_jets(r,theta+h,.3);tm=tail.position_jets(r,theta-h,.3)
        position_error={}
        for key,fd in [('Xs',(xp['X']-xm['X'])/(2*h)),('Xss',(xp['Xs']-xm['Xs'])/(2*h)),
                       ('Xtheta',(tp['X']-tm['X'])/(2*h)),('Xst',(tp['Xs']-tm['Xs'])/(2*h)),
                       ('Xtt',(tp['Xtheta']-tm['Xtheta'])/(2*h))]:
            position_error[key]=float(np.max(abs(position[key]-fd))/max(1.,np.max(abs(position[key]))))
        target_error=max(float(np.max(abs(frame['T']-position['Xtheta']/r[:,None]))),
                         float(np.max(abs(frame['V']-position['Xs']))))
        R=frame['Vtheta']+frame['T']-r[:,None]*frame['Ts']
        reflection=tail.scalar_jets(r,-theta);periodic=tail.scalar_jets(r,theta+np.pi)
        symmetry=max(float(np.max(abs(reflection[name]['value']-(-1 if name!='beta' else 1)*fields[name]['value'])))
                     for name in ['u','v','beta'])
        symmetry=max(symmetry,max(float(np.max(abs(periodic[name]['value']-fields[name]['value']))) for name in ['u','v','beta']))
        Y0,H0=tail.integrals(r*np.sin(theta),24);Y1,H1=tail.integrals(r*np.sin(theta),48)
        checks.append({'side':side,'scalar_jet_relative_errors':scalar_error,
            'position_jet_relative_errors':position_error,'target_frame_error':target_error,
            'integrability_error':float(np.max(abs(R))),'symmetry_error':symmetry,
            'quadrature_doubling_difference':float(max(np.max(abs(Y1-Y0)),np.max(abs(H1-H0))))})
    # Exact endpoint identities of the chosen polynomial; no physical sampling.
    p=[Q(0)]*6+[Q(x) for x in [462,-1980,3465,-3080,1386,-252]]
    endpoints=[]
    for order in range(6):
        endpoints.append([str(p[0]),str(sum(p,Q(0)))])
        p=[(i+1)*p[i+1] for i in range(len(p)-1)]
    endpoint_pass=endpoints[0]==['0','1'] and all(row==['0','0'] for row in endpoints[1:])
    passed=endpoint_pass and all(max(row['scalar_jet_relative_errors'].values())<3e-6 and
        max(row['position_jet_relative_errors'].values())<3e-6 and
        max(row['target_frame_error'],row['integrability_error'],row['symmetry_error'],row['quadrature_doubling_difference'])<1e-10
        for row in checks)
    return {'schema':'bent-flat-port-development-v1','checks':checks,
        'exact_S11_endpoint_jets':endpoints,'passed':bool(passed),
        'artificial_inputs_only':True,'research_geometry_evaluated':False,'optimization_performed':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    result=developer_check();result['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
    if not result['passed']:raise SystemExit(1)


if __name__=='__main__':main()
