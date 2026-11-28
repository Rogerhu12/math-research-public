"""Whole finite-input negative-Sobolev receiver for shifted columns and physical rank blocks.

Input units are n^(1/6) H^(-4/3), n=4j. Any additional original n
power must already be present in the signed supplied amplitudes.
"""
from fractions import Fraction as Q
from flint import arb
from fourfold_codazzi_signed_density_transport_arithmetic import exact
from fourfold_codazzi_collar_signed_laurent_enclosure import DEGREE,WIDTH
from fourfold_codazzi_true_phase_original_inputs import check

SPLITS=(Q(1,8),Q(1,4),Q(1,2),Q(3,4))


def power(x,p):return (x.log()*exact(p)).exp()


def rownorm(values):
    return sum((abs(v).upper()**2 for v in values),arb(0)).sqrt().upper()


def max_physical_weight(lo,hi,h,eps,p):
    # This keeps the true physical output label. Numerator and denominator
    # may be bounded separately only after restricting this same input band.
    left,right=sorted((eps*lo+h,eps*hi+h))
    if left==right==0:return arb(0)
    smallest=1 if left<=0<=right else min(abs(left),abs(right))
    numerator=power(arb(4*hi),Q(1,6))*power(arb(1+16*hi*hi),Q(2,3))
    return (numerator/power(arb(1+16*smallest*smallest),p/2)).upper()


def weighted_input_square(lo,hi):
    total=(hi*(hi+1)//2)**2-((lo-1)*lo//2)**2
    correction=power(arb(1)+exact(Q(1,16*lo*lo)),Q(4,3))
    return (64*correction*total).upper()


def near_far(lo,hi,a,p):
    check(p>Q(1,2),"entire infinite physical output square is summable")
    exponent=Q(3,2)-p
    endpoint=hi if exponent>=0 else lo
    correction=power(arb(1)+exact(Q(1,16*lo*lo)),Q(2,3))
    far=power(arb(4*endpoint),exponent)*correction/power(exact(a),p)
    z=(-8*exact(WIDTH*(1-a))).exp();den=1-z
    tail=z**lo*(lo**3/den+3*lo**2*z/den**2+3*lo*z*(1+z)/den**3+
                z*(1+4*z+z*z)/den**4)
    critical=Q(3)/(8*WIDTH*(1-a))
    peak=exact(min(max(critical,Q(lo)),Q(hi)))
    finite=(hi-lo+1)*peak**3*(-8*exact(WIDTH*(1-a))*peak).exp()
    geometric=min(tail.upper(),finite.upper())
    # Two input signs and all nonzero output integers. This is a true
    # Hilbert--Schmidt tail, not an assumed orthogonality of the output.
    near=2*64*correction**2*geometric*(2*power(arb(4),-2*p)*(1+exact(1/(2*p-1))))
    return far.upper(),near.upper()


def band(columns,lo,hi,p):
    """columns[sign_index][original_reference_column], each a full Column.

    The bound is for the projected physical output. Its use for a source
    row requires that original row's exact nonmean/reflection identity.
    """
    p=Q(p)
    check(len(columns)==2 and len(columns[0])==len(columns[1]) and len(columns[0]) in (1,2),
          "both complete signs and the stated independent original reference columns")
    heads=[]
    for h in range(-DEGREE,DEGREE+1):
        heads.append(max((rownorm([x.oscillatory.coeff(h) for x in row])*
                         max_physical_weight(lo,hi,h,eps,p)).upper()
                         for eps,row in zip((1,-1),columns)))
    error=max(rownorm([x.oscillatory.error for x in row]) for row in columns)
    splits=[]
    for a in SPLITS:
        far,near=near_far(lo,hi,a,p)
        splits.append([(far*error).upper(),(near*error**2).upper()])
    physical_square=arb(0)
    for row in columns:
        head=arb(0)
        for h in range(-DEGREE,DEGREE+1):
            if h:
                head+=rownorm([x.physical.coeff(h) for x in row])**2/power(arb(1+16*h*h),p)
        rem=rownorm([x.physical.error for x in row])/power(arb(17),p/2)
        physical_square+=(head.sqrt()+rem)**2
    rank=(weighted_input_square(lo,hi)*physical_square).upper()
    return dict(head=heads,splits=splits,physical_rank_squared=rank)


def scalar_band(values,lo,hi):
    check(len(values)==2 and len(values[0])==len(values[1]),"both full physical mean functionals")
    return (weighted_input_square(lo,hi)*sum((rownorm(row)**2 for row in values),arb(0))).upper()


def zero():
    return dict(head=[arb(0)]*(2*DEGREE+1),splits=[[arb(0),arb(0)] for _ in SPLITS],
                physical_rank_squared=arb(0))


def merge(a,b):
    return dict(head=[max(x,y) for x,y in zip(a['head'],b['head'])],
        splits=[[max(x[0],y[0]),(x[1]+y[1]).upper()] for x,y in zip(a['splits'],b['splits'])],
        physical_rank_squared=(a['physical_rank_squared']+b['physical_rank_squared']).upper())


def full_cost(record):
    z=(-4*exact(WIDTH)).exp()
    remainder=min((far*(1+z)/(1-z)+near.sqrt()).upper() for far,near in record['splits'])
    return (sum(record['head'],arb(0))+remainder+record['physical_rank_squared'].sqrt()).upper()
