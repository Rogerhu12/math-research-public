#!/usr/bin/env python3
"""Exact outward arithmetic for complete R625/R716 surface-flux moments.

This module evaluates no field, normal root, optimization direction or sampled
quadrature. Its formulas consume entire parameter-box enclosures. All actual
numeric execution is restricted to this repository's public Actions by callers.
The full closed-image, embedding, outside-tube and phase hypotheses remain
separate from a complete parametric flux integral.
"""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import json
import math
import os

SCHEMA = "complete-R716-outward-flux-moment-arithmetic-v1"
CHANNELS = ("V", "mx", "my", "mz", "Qxx", "Qxy", "Qxz", "Qyy", "Qyz", "Qzz",
            "A2_real", "A2_imag")
QUADRATIC = (("Qxx",0,0),("Qxy",0,1),("Qxz",0,2),("Qyy",1,1),
             ("Qyz",1,2),("Qzz",2,2))
ODD_UNDER_HORIZONTAL_REFLECTION = frozenset(("mz","Qxz","Qyz"))


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Actual complete moment arithmetic runs in public repository Actions")


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),
        allow_nan=False).encode()).hexdigest()


def rational(value):
    if type(value) is int:
        return F(value)
    if isinstance(value,F):
        return value
    if not isinstance(value,str) or not value:
        raise ValueError("Use exact rational strings, never rounded JSON numbers")
    result=F(value)
    if str(result) != value:
        raise ValueError("Use canonical complete rational words")
    return result


def integer(value,*,minimum=None,maximum=None):
    if type(value) is not int or (minimum is not None and value<minimum) or (
            maximum is not None and value>maximum):
        raise ValueError("Invalid exact integer parameter")
    return value


def digest(value):
    if not isinstance(value,str) or len(value)!=64 or any(
            c not in "0123456789abcdef" for c in value):
        raise ValueError("A complete SHA256 identity is required")
    return value


def _floor(q):
    return q.numerator//q.denominator


def _ceil(q):
    return -((-q.numerator)//q.denominator)


class Interval:
    """Closed exact rational bounds; every arithmetic result rounds outwards."""

    __slots__=("lo","hi","bits")
    def __init__(self,lo,hi=None,bits=192):
        self.bits=integer(bits,minimum=64,maximum=4096)
        lo=rational(lo)
        hi=lo if hi is None else rational(hi)
        if lo>hi:
            raise ValueError("An interval cannot have reversed endpoints")
        self.lo,self.hi=lo,hi

    @classmethod
    def rounded(cls,lo,hi,bits):
        scale=1<<bits
        return cls(F(_floor(lo*scale),scale),F(_ceil(hi*scale),scale),bits)

    def _other(self,value):
        if isinstance(value,Interval):
            if value.bits!=self.bits:
                raise ValueError("Use one declared complete arithmetic precision")
            return value
        return Interval(value,bits=self.bits)

    def __add__(self,value):
        other=self._other(value)
        return self.rounded(self.lo+other.lo,self.hi+other.hi,self.bits)

    __radd__=__add__

    def __neg__(self):
        return Interval(-self.hi,-self.lo,self.bits)

    def __sub__(self,value):
        return self+(-self._other(value))

    def __rsub__(self,value):
        return self._other(value)+(-self)

    def __mul__(self,value):
        other=self._other(value)
        products=(self.lo*other.lo,self.lo*other.hi,self.hi*other.lo,self.hi*other.hi)
        return self.rounded(min(products),max(products),self.bits)

    __rmul__=__mul__

    def reciprocal(self):
        if self.lo<=0<=self.hi:
            raise ArithmeticError("An actual denominator enclosure contains zero")
        return self.rounded(1/self.hi,1/self.lo,self.bits)

    def __truediv__(self,value):
        return self*self._other(value).reciprocal()

    def __rtruediv__(self,value):
        return self._other(value)*self.reciprocal()

    def square(self):
        upper=max(self.lo*self.lo,self.hi*self.hi)
        lower=F(0) if self.lo<=0<=self.hi else min(self.lo*self.lo,self.hi*self.hi)
        return self.rounded(lower,upper,self.bits)

    def __pow__(self,power):
        integer(power,minimum=0)
        if power==0:
            return Interval(1,bits=self.bits)
        if power==1:
            return self
        if power==2:
            return self.square()
        if power%2==0:
            return (self**(power//2)).square()
        return self*(self**(power-1))

    def sqrt(self):
        if self.lo<0:
            raise ArithmeticError("A real square-root enclosure requires nonnegative input")
        scale=1<<self.bits
        lower=F(math.isqrt(_floor(self.lo*scale*scale)),scale)
        upper_integer=math.isqrt(_floor(self.hi*scale*scale))
        if F(upper_integer*upper_integer,scale*scale)<self.hi:
            upper_integer+=1
        return Interval(lower,F(upper_integer,scale),self.bits)

    def intersect(self,other):
        other=self._other(other)
        lo,hi=max(self.lo,other.lo),min(self.hi,other.hi)
        if lo>hi:
            raise ArithmeticError("Two rigorous representations have disjoint enclosures")
        return Interval(lo,hi,self.bits)

    def abs_lower(self):
        return F(0) if self.lo<=0<=self.hi else min(abs(self.lo),abs(self.hi))

    def abs_upper(self):
        return max(abs(self.lo),abs(self.hi))

    def json(self):
        return [str(self.lo),str(self.hi)]


def box(value,bits=192):
    if isinstance(value,Interval):
        if value.bits!=bits:
            return Interval.rounded(value.lo,value.hi,bits)
        return value
    if not isinstance(value,list) or len(value)!=2:
        raise ValueError("A complete two-endpoint rational box is required")
    return Interval(rational(value[0]),rational(value[1]),bits)


def vector(value,bits=192):
    if not isinstance(value,list) or len(value)!=3:
        raise ValueError("A complete three-component vector is required")
    return [box(item,bits) for item in value]


def dot(a,b):
    if len(a)!=3 or len(b)!=3:
        raise ValueError("Keep every Cartesian component")
    return sum((a[i]*b[i] for i in range(3)),Interval(0,bits=a[0].bits))


def cross(a,b):
    if len(a)!=3 or len(b)!=3:
        raise ValueError("Keep every Cartesian component")
    return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]


def norm_box(a):
    return sum((v.square() for v in a),Interval(0,bits=a[0].bits)).sqrt()


def complex_product(a,b,*,conjugate_right=False):
    if len(a)!=2 or len(b)!=2:
        raise ValueError("Keep both real and imaginary components")
    br,bi=b[0],-b[1] if conjugate_right else b[1]
    return [a[0]*br-a[1]*bi,a[0]*bi+a[1]*br]


def complex_norm(a):
    return (a[0].square()+a[1].square()).sqrt()


def flux_channels(fields,bits=192):
    """Upper orientation is exactly Fphi cross Fs, with no unit normal."""
    if not isinstance(fields,dict):
        raise ValueError("Read a complete physical-sixjet dictionary")
    required=("F","Fs","Fphi","Fss","Fsphi","Fphiphi")
    jets={name:vector(fields[name],bits) for name in required}
    position=jets["F"]
    normal=cross(jets["Fphi"],jets["Fs"])
    flux=dot(position,normal)
    out={"V":flux/3}
    for name,i in (("mx",0),("my",1),("mz",2)):
        out[name]=position[i]*flux/4
    for name,i,j in QUADRATIC:
        factor=position[i].square() if i==j else position[i]*position[j]
        out[name]=factor*flux/5
    out["A2_real"]=(position[0].square()-position[1].square())*flux/5
    out["A2_imag"]=2*position[0]*position[1]*flux/5
    return out,norm_box(normal),norm_box(position)


def zero_moments(bits=192):
    return {name:Interval(0,bits=bits) for name in CHANNELS}


def add_moments(a,b):
    if set(a)!=set(CHANNELS) or set(b)!=set(CHANNELS):
        raise ValueError("All twelve complete flux channels must be retained")
    return {name:a[name]+b[name] for name in CHANNELS}


def scale_moments(a,factor):
    if set(a)!=set(CHANNELS):
        raise ValueError("All twelve complete flux channels must be retained")
    return {name:a[name]*factor for name in CHANNELS}


def reflected_upper_and_lower(upper):
    """The defined lower parametrization has reversed parameter orientation.

    With D=diag(1,1,-1), lower F=D*upper F and its outward-compatible
    cross product is Fs_lower cross Fphi_lower=D*N_upper. This identity
    is an exact formal extension. It does not certify that the image is
    embedded, nor replace its core/cap C2 and branch obligations.
    """
    bits=upper["V"].bits
    return {name:(Interval(0,bits=bits) if name in ODD_UNDER_HORIZONTAL_REFLECTION
                  else 2*upper[name]) for name in CHANNELS}


def flat_cap_moments(radius,height,pi):
    """Both unmarked, axis-centred flat discs, with normals +/-ez."""
    if radius.lo<=0:
        raise ArithmeticError("A complete positive exact cap radius is required")
    bits=radius.bits
    out=zero_moments(bits)
    out["V"]=2*pi*radius.square()*height/3
    out["Qxx"]=pi*height*(radius**4)/10
    out["Qyy"]=out["Qxx"]
    out["Qzz"]=2*pi*(height**3)*radius.square()/5
    return out


def p4_marker_moments(height,pi):
    """R716 sections 4-5: the unchanged three upper and one lower p4 caps."""
    bits=height.bits
    a,h=F(3,20),F(1,1000)
    radii=(F(1,25),F(9,200),F(1,20),F(11,200))
    centres=((a,F(0)),(F(0),a),(-a,F(0)),(F(0),F(0)))
    signs=(1,1,1,-1)
    out=zero_moments(bits)
    masses=[]
    for radius,centre,sign in zip(radii,centres,signs):
        mass=pi*h*radius*radius/5
        masses.append(mass)
        cx,cy=centre
        zbar=height+5*h/18
        out["V"]=out["V"]+mass
        out["mx"]=out["mx"]+mass*cx
        out["my"]=out["my"]+mass*cy
        out["mz"]=out["mz"]+sign*mass*zbar
        out["Qxx"]=out["Qxx"]+mass*(cx*cx+radius*radius/12)
        out["Qxy"]=out["Qxy"]+mass*cx*cy
        out["Qyy"]=out["Qyy"]+mass*(cy*cy+radius*radius/12)
        out["Qxz"]=out["Qxz"]+sign*mass*cx*zbar
        out["Qyz"]=out["Qyz"]+sign*mass*cy*zbar
        out["Qzz"]=out["Qzz"]+mass*(height.square()+5*height*h/9+5*h*h/39)
        out["A2_real"]=out["A2_real"]+mass*(cx*cx-cy*cy)
        out["A2_imag"]=out["A2_imag"]+2*mass*cx*cy
    mu=pi/F(200000000)
    explicit_b1=[a*mu*(-36),a*mu*81]
    explicit_B2=[83*a*a*mu,Interval(0,bits=bits)]
    out["mx"]=out["mx"].intersect(explicit_b1[0])
    out["my"]=out["my"].intersect(explicit_b1[1])
    out["A2_real"]=out["A2_real"].intersect(explicit_B2[0])
    out["A2_imag"]=out["A2_imag"].intersect(explicit_B2[1])
    out["V"]=out["V"].intersect(366*mu)
    return out,dict(recipe="R661 fixed p4, R716 sections 4-5",
        exact_radius_words=[str(v) for v in radii],exact_height=str(h),
        exact_centres_xy=[[str(v) for v in c] for c in centres],
        upper_lower_signs=list(signs),masses=[v.json() for v in masses],
        b1=[v.json() for v in explicit_b1],B2=[v.json() for v in explicit_B2],
        asymmetry_and_all_mixed_moments_retained=True,
        source_of_disjointness="requires the same complete unmarked external normal tube >1/1000",
        marker_disjointness_not_inferred_from_local_height=True)


def centred_tensor(moments):
    volume=moments["V"]
    if volume.lo<=0:
        raise ArithmeticError("The complete positive total volume remains unresolved")
    m=[moments[k] for k in ("mx","my","mz")]
    out={}
    for name,i,j in QUADRATIC:
        out[name]=moments[name]-m[i]*m[j]/volume
    square=(out["Qxx"].square()+out["Qyy"].square()+out["Qzz"].square()
            +2*(out["Qxy"].square()+out["Qxz"].square()+out["Qyz"].square()))
    return dict(centroid=[v/volume for v in m],tensor=out,
        frobenius_squared=square,frobenius=square.sqrt())


def r716_compensation(unmarked,markers,pi):
    volume=unmarked["V"]+markers["V"]
    if volume.lo<=0:
        return dict(available=False,reason="The total complete volume enclosure includes zero",
            total_volume=volume.json())
    bits=volume.bits
    b1=[markers["mx"],markers["my"]]
    b2=[markers["A2_real"],markers["A2_imag"]]
    b1_squared=complex_product(b1,b1)
    general=[b2[i]-b1_squared[i]/volume for i in range(2)]
    a,mu=F(3,20),pi/F(200000000)
    explicit=[a*a*mu*(83+5265*mu/volume),a*a*mu*(5832*mu/volume)]
    effective=[general[i].intersect(explicit[i]) for i in range(2)]
    A=[unmarked["A2_real"],unmarked["A2_imag"]]
    z=complex_product(A,effective,conjugate_right=True)
    half_turn=2*z[0]
    quarter_turn=z[0]+z[1]
    a_lower=complex_norm(A).lo
    b_lower=complex_norm(effective).lo
    minimum_maximum=Interval(F(2,5),bits=bits).sqrt()*a_lower*b_lower
    phase=None
    if half_turn.abs_lower()>0:
        phase="1"
    elif quarter_turn.abs_lower()>0:
        phase="1/2"
    return dict(available=True,total_volume=volume.json(),
        original_unmarked_A2=[v.json() for v in A],
        complete_fixed_b1=[v.json() for v in b1],
        complete_fixed_B2=[v.json() for v in b2],
        B_effective=[v.json() for v in effective],
        real_B_effective_structural_lower=(83*a*a*mu).json(),
        A2_conjugate_B_effective=[v.json() for v in z],
        I0_squared_minus_I1_squared=half_turn.json(),
        I0_squared_minus_Ihalf_squared=quarter_turn.json(),
        rigorous_A2_absolute_lower=str(a_lower),
        rigorous_B_effective_absolute_lower=str(b_lower),
        conditional_maximum_squared_invariant_gap_lower=str(minimum_maximum.lo),
        one_literal_phase_selected_by_nonzero_gap=phase,
        conditional_at_least_one_phase_distinct=minimum_maximum.lo>0,
        same_closed_bounded_entity_and_half_turn_hypotheses_paid_here=False,
        outside_fixed_cap_disjointness_paid_here=False,
        unconditional_noncongruence_certificate=False)



def rotate_moments(moments,phase):
    """R716(2), without assuming half-turn symmetry of the actual root branch."""
    bits=moments["V"].bits
    zero,one=Interval(0,bits=bits),Interval(1,bits=bits)
    if phase=="0":
        c,s=one,zero
    elif phase=="1/2":
        c=s=Interval(2,bits=bits).sqrt()/2
    elif phase=="1":
        c,s=zero,one
    else:
        raise ValueError("Use exactly alpha=0, pi/4 or pi/2, with t=2*alpha/pi")
    U=[[c,-s,zero],[s,c,zero],[zero,zero,one]]
    m=[moments[k] for k in ("mx","my","mz")]
    Q=[[moments["Qxx"],moments["Qxy"],moments["Qxz"]],
       [moments["Qxy"],moments["Qyy"],moments["Qyz"]],
       [moments["Qxz"],moments["Qyz"],moments["Qzz"]]]
    out=zero_moments(bits)
    out["V"]=moments["V"]
    for i,name in enumerate(("mx","my","mz")):
        out[name]=sum((U[i][j]*m[j] for j in range(3)),zero)
    for name,i,j in QUADRATIC:
        out[name]=sum((U[i][a]*Q[a][b]*U[j][b] for a in range(3) for b in range(3)),zero)
    real,imag=moments["A2_real"],moments["A2_imag"]
    if phase=="0":
        out["A2_real"],out["A2_imag"]=real,imag
    elif phase=="1/2":
        out["A2_real"],out["A2_imag"]=-imag,real
    else:
        out["A2_real"],out["A2_imag"]=-real,-imag
    out["A2_real"]=out["A2_real"].intersect(out["Qxx"]-out["Qyy"])
    out["A2_imag"]=out["A2_imag"].intersect(2*out["Qxy"])
    return out


def general_centred_phase_comparison(unmarked,markers):
    """All first, mixed and second moments are retained at all three phases."""
    total_volume=unmarked["V"]+markers["V"]
    if total_volume.lo<=0:
        return dict(available=False,total_volume=total_volume.json(),
            reason="Complete positive volume is not yet separated from zero")
    phases={}
    for phase in ("0","1/2","1"):
        moments=add_moments(rotate_moments(unmarked,phase),markers)
        phases[phase]=dict(complete_total_raw_moments=moments,
                          complete_centred_moments=centred_tensor(moments))
    differences={}
    for phase in ("1/2","1"):
        initial=phases["0"]["complete_centred_moments"]
        final=phases[phase]["complete_centred_moments"]
        square_difference=initial["frobenius_squared"]-final["frobenius_squared"]
        denominator=initial["frobenius"].hi+final["frobenius"].hi
        lower=F(0) if denominator<=0 else square_difference.abs_lower()/denominator
        differences[phase]=dict(I0_squared_minus_It_squared=square_difference,
            absolute_I0_minus_It_lower=str(lower),
            actual_first_and_mixed_moment_centre_compensation_retained=True)
    return dict(available=True,total_volume=total_volume,
        exact_physical_phase_convention="alpha=pi*t/2",
        all_three_phases=phases,phase_differences=differences,
        no_half_turn_assumption_needed_for_this_algebra=True,
        complete_outward_closed_bounded_entities_and_fixed_cap_disjointness_still_required=True,
        unconditional_noncongruence_certificate=False)

def serialize(value):
    if isinstance(value,Interval):
        return value.json()
    if isinstance(value,F):
        return str(value)
    if isinstance(value,dict):
        return {str(k):serialize(v) for k,v in value.items()}
    if isinstance(value,(tuple,list)):
        return [serialize(v) for v in value]
    if value is None or type(value) in (str,int,bool):
        return value
    raise TypeError("Do not silently round or serialize nonfinite scientific values")
