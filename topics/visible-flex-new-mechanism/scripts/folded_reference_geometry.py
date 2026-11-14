#!/usr/bin/env python3
"""Directed-rounding checks for a *circular reference* with interior folds.

This does not solve the nonaxisymmetric circle-port BVP. Its embedding lemma
and curvature bounds concern the reference surface of revolution, capped by
two flat disks. Decimal arithmetic is rounded outwards; sine and cosine use
alternating-series remainder bounds, not machine-libm error assumptions.
"""
from __future__ import annotations

import argparse
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, getcontext
import hashlib
import json
from pathlib import Path
import time

getcontext().prec = 60
DOWN = Context(prec=50, rounding=ROUND_FLOOR)
UP = Context(prec=50, rounding=ROUND_CEILING)


class I:
    def __init__(self, lo, hi=None):
        self.lo = lo if isinstance(lo,D) else D(str(lo))
        self.hi = self.lo if hi is None else hi if isinstance(hi,D) else D(str(hi))
        if self.lo > self.hi:
            raise ValueError('reversed interval')
    def __add__(self, other):
        other = as_i(other)
        return I(DOWN.add(self.lo,other.lo), UP.add(self.hi,other.hi))
    __radd__ = __add__
    def __neg__(self):
        return I(self.hi.copy_negate(),self.lo.copy_negate())
    def __sub__(self, other):
        return self+-as_i(other)
    def __rsub__(self, other):
        return as_i(other)+-self
    def __mul__(self, other):
        other = as_i(other)
        ends = [(x,y) for x in (self.lo,self.hi) for y in (other.lo,other.hi)]
        return I(min(DOWN.multiply(x,y) for x,y in ends),
                 max(UP.multiply(x,y) for x,y in ends))
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = as_i(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError('interval denominator meets zero')
        return self*I(DOWN.divide(D(1),other.hi), UP.divide(D(1),other.lo))
    def __rtruediv__(self, other):
        return as_i(other)/self
    def __pow__(self, n):
        if not isinstance(n,int) or n < 0:
            raise ValueError('nonnegative integer powers only')
        answer = I(1)
        for _ in range(n):
            answer *= self
        return answer
    def abs_upper(self):
        return max(self.lo.copy_abs(),self.hi.copy_abs())
    def sqrt(self):
        if self.lo < 0:
            raise ValueError('negative square root endpoint')
        # Decimal sqrt is correctly rounded; one representable step protects
        # both endpoints irrespective of its specified nearest rounding.
        return I(DOWN.next_minus(DOWN.sqrt(self.lo)),UP.next_plus(UP.sqrt(self.hi)))
    def json(self):
        return {'lower':str(self.lo),'upper':str(self.hi)}


def as_i(x):
    return x if isinstance(x,I) else I(x)


def atan_inverse_integer(denominator):
    x = I(1)/denominator
    power, total = x, x
    for k in range(1,81):
        power *= -(x*x)
        total += power/(2*k+1)
    remainder = (power*x*x/163).abs_upper()
    return total+I(-remainder,remainder)


# Machin's identity; the alternating remainders are included above.
PI = 16*atan_inverse_integer(5)-4*atan_inverse_integer(239)


def point_sincos(x):
    if abs(x) > 12:
        raise ValueError('Taylor enclosure is restricted to |x|<=12')
    xx = I(x)*I(x)
    st,ct = I(x),I(1)
    ss,cc = st,ct
    for k in range(1,41):
        st = -st*xx/((2*k)*(2*k+1))
        ct = -ct*xx/((2*k-1)*(2*k))
        ss,cc = ss+st,cc+ct
    sr = (st*xx/(82*83)).abs_upper()
    cr = (ct*xx/(81*82)).abs_upper()
    return ss+I(-sr,sr),cc+I(-cr,cr)


def sincos(x):
    x = as_i(x)
    a,b = point_sincos(x.lo),point_sincos(x.hi)
    slo,shi = min(a[0].lo,b[0].lo),max(a[0].hi,b[0].hi)
    clo,chi = min(a[1].lo,b[1].lo),max(a[1].hi,b[1].hi)
    for k in range(-8,9):
        point = PI*k/2
        if x.lo <= point.hi and x.hi >= point.lo:
            if k % 4 == 1: shi = max(shi,D(1))
            if k % 4 == 3: slo = min(slo,D(-1))
            if k % 4 == 0: chi = max(chi,D(1))
            if k % 4 == 2: clo = min(clo,D(-1))
    return I(slo,shi),I(clo,chi)


def step_point(x):
    xx=I(x)
    return xx**3*(10+xx*(-15+6*xx))


def step(x):
    # S is increasing throughout [0,1].
    x=as_i(x)
    if x.lo < 0 or x.hi > 1:
        raise ValueError('smoothstep interval outside [0,1]')
    return I(step_point(x.lo).lo,step_point(x.hi).hi)


def step_prime(x):
    x=as_i(x)
    def endpoint(v):
        v=I(v)
        return 30*v*v*(1-v)*(1-v)
    if x.lo < 0 or x.hi > D('.5'):
        raise ValueError('use the increasing half of S prime')
    return I(endpoint(x.lo).lo,endpoint(x.hi).hi)


class Reference:
    def __init__(self, wiggle, length, radius, collar='.06',plateau='0'):
        self.b,self.length,self.radius,self.collar = map(I,[wiggle,length,radius,collar])
        self.plateau=I(plateau)
        self.start = self.length*self.collar
        self.width = self.length*(1-2*self.collar-2*self.plateau)
        if (self.b.lo <= D('.5') or self.radius.lo <= 0 or self.length.lo <= 0
                or self.collar.lo <= 0 or self.collar.hi >= D('.25')
                or self.plateau.lo<0 or self.width.lo<=0):
            raise ValueError('invalid folded-reference parameters')
    def profile_step(self,x):
        return step(x) if self.plateau.lo==0 else step(2*as_i(x))/2
    def profile_prime(self,x):
        if self.plateau.lo==0:
            return step_prime(x)
        xx=2*as_i(x)
        def endpoint(v):
            v=I(v)
            return 30*v*v*(1-v)*(1-v)
        left,right=endpoint(xx.lo),endpoint(xx.hi)
        upper=max(left.hi,right.hi)
        if xx.lo<=D('.5')<=xx.hi: upper=max(upper,D('1.875'))
        return I(min(left.lo,right.lo),upper)
    def beta(self,x):
        s=self.profile_step(x)
        return PI*s+self.b*sincos(2*PI*s)[0]
    def factor(self,x):
        return PI*(1+2*self.b*sincos(2*PI*self.profile_step(x))[1])
    def beta_s(self,x):
        return self.factor(x)*self.profile_prime(x)/self.width
    def root(self,fn,lo,hi,increasing=True):
        lo,hi=D(lo),D(hi)
        left,right=fn(I(lo)),fn(I(hi))
        if increasing:
            if not (left.hi < 0 < right.lo): raise ValueError('root lacks strict endpoint signs')
        else:
            if not (right.hi < 0 < left.lo): raise ValueError('root lacks strict endpoint signs')
        for _ in range(80):
            midpoint=(lo+hi)/2
            value=fn(I(midpoint))
            if value.lo <= 0 <= value.hi:
                break
            below=value.hi < 0
            if below == increasing: lo=midpoint
            else: hi=midpoint
        return I(lo,hi)
    def events(self):
        peak=self.root(self.factor,'0','.5',False)
        height=self.beta(peak)
        if not (height.lo > PI.hi and height.hi < (3*PI/2).lo):
            raise ValueError('reference is outside the certified single-fold pattern')
        radial_max=self.root(lambda x:self.beta(x)-PI/2,'0',peak.lo)
        fold_enter=self.root(lambda x:self.beta(x)-PI,'0',peak.lo)
        fold_leave=self.root(lambda x:self.beta(x)-PI,peak.hi,'.5',False)
        return dict(radial_max=radial_max,fold_enter=fold_enter,beta_max=peak,fold_leave=fold_leave,midpoint=I('.5'))
    def integral(self,x,cells):
        # x's small uncertain tail is enclosed by |sin|,|cos|<=1.
        endpoint=x.lo
        width=I(endpoint)/cells
        cosine,sine=I(0),I(0)
        for j in range(cells):
            cell=I(endpoint*j/cells,endpoint*(j+1)/cells)
            sn,cs=sincos(self.beta(cell))
            cosine+=width*cs
            sine+=width*sn
        remainder=UP.subtract(x.hi,x.lo)
        return cosine+I(-remainder,remainder),sine+I(-remainder,remainder)
    def audit(self,cells,curvature_limit):
        events=self.events()
        values={}
        for name,event in events.items():
            if name=='beta_max': continue
            ca,sz=self.integral(event,cells)
            values[name]={'s':self.start+self.width*event,
                          'a':self.radius+self.start+self.width*ca,'z':self.width*sz}
            if name=='midpoint':
                values[name]['s']+=self.length*self.plateau
                values[name]['z']+=self.length*self.plateau
        gain=values['midpoint']['a']-self.radius
        half_simple=values['fold_leave']['z']-values['radial_max']['z']
        half_gap=values['midpoint']['z']-values['fold_enter']['z']
        amax=values['radial_max']['a']
        amin=min(self.radius.lo,values['midpoint']['a'].lo)
        height=2*values['midpoint']['z']
        kmax=D(0)
        for j in range(cells):
            value=self.beta_s(I(D(j)/(2*cells),D(j+1)/(2*cells)))
            kmax=max(kmax,value.abs_upper())
        principal_upper=max(kmax,UP.divide(D(1),amin))
        diameter_lower=2*amax
        diameter_upper=((2*amax)**2+height**2).sqrt()
        ratio=half_gap/diameter_lower
        embedded=(amin>0 and half_simple.lo>0 and half_gap.lo>0)
        return {'parameters':{'beta_wiggle':str(self.b.lo),'length':str(self.length.lo),
                              'radius':str(self.radius.lo),'collar_fraction':str(self.collar.lo)},
                'profile_family':'full_smoothstep' if self.plateau.lo==0 else 'half_smoothstep_with_central_plateau',
                'central_half_plateau_fraction':str(self.plateau.lo),
                'interval_cells_per_integral':cells,'decimal_precision':50,
                'pi_enclosure':PI.json(),
                'events':{name:{k:v.json() for k,v in value.items()} for name,value in values.items()},
                'radius_min_lower':str(amin),'midpoint_radius_gain':gain.json(),
                'half_meridian_injectivity_margin':half_simple.json(),
                'mirror_halves_separation_margin':half_gap.json(),
                'height':height.json(),'reference_diameter_lower':diameter_lower.json(),
                'reference_diameter_upper':diameter_upper.json(),
                'reference_principal_curvature_upper':str(principal_upper),
                'curvature_limit_requested':str(curvature_limit),
                'reference_curvature_ceiling_verified':principal_upper<=D(curvature_limit),
                'reference_embedding_verified_by_monotonicity_lemma':embedded,
                'reference_reach_upper_from_mirror_fold_pair':half_gap.json(),
                'reference_reach_over_D_upper_from_pair':str(ratio.hi),
                'reference_reach_target_003_ruled_out_by_pair':embedded and ratio.hi<D('.03'),
                'reference_fixed_disk_diameter_over_D_lower':str((2*self.radius/diameter_upper).lo),
                'scope':'Capped axisymmetric reference only; no nonaxisymmetric BVP or flexible family.',
                'reference_reach_lower_certified':False,'nonaxisymmetric_solution_obtained':False,
                'task_complete':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--beta-wiggle',default='2.4')
    parser.add_argument('--length',default='2.2')
    parser.add_argument('--radius',default='.45')
    parser.add_argument('--collar',default='.06')
    parser.add_argument('--plateau',default='0')
    parser.add_argument('--cells',type=int,default=512)
    parser.add_argument('--curvature-limit',default='12')
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.cells<8 or args.cells&(args.cells-1):
        parser.error('cells must be a power of two, at least 8')
    started=time.monotonic()
    result=Reference(args.beta_wiggle,args.length,args.radius,args.collar,args.plateau).audit(args.cells,args.curvature_limit)
    result.update(schema='folded-circular-reference-v1',elapsed_seconds=time.monotonic()-started,
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'out':str(args.out),'embedded':result['reference_embedding_verified_by_monotonicity_lemma'],
                      'curvature_upper':result['reference_principal_curvature_upper'],
                      'reach_pair_upper_over_D':result['reference_reach_over_D_upper_from_pair'],
                      'seconds':result['elapsed_seconds']}),flush=True)


if __name__=='__main__':
    main()
