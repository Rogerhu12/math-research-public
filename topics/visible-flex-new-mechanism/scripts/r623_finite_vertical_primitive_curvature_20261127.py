#!/usr/bin/env python3
"""R623 exact finite-v primitive plus the complete normalization remainder.

The actual vertical tangent is C=v/sqrt(1+v*v), NOT v.  Only its exact
linear v part is integrated mode by mode.  The odd, pi-periodic nonlinear
remainder and both radial derivatives retain a complete primitive bound.
One same-cell coefficient read supplies angular jets and this new curvature
bound.  This module neither runs a field reconstruction nor certifies an
unprovided material domain or a new global C0/C1 bound.
"""
import hashlib
import math
from pathlib import Path

BINDINGS = {
    'r582_same_field_radial_intervals_20261127.py':
        'ed167c5850ccb4e438f02a3c8d7aac051466103af2e559c0e3356001bf3ecb28',
    'r604_rotating_frame_continuous_norms_20261127.py':
        '2fa3a89f2bc2bc0e739ae69f391b06f3b44cb3033d236df632205a3c357516e0',
    'r621_normal_projected_curvature_20261127.py':
        'fa40dd40424cf6e0bea8f40b9bbfc485b32e971f3b5869359e0e59213c276b4a',
}
for filename, expected in BINDINGS.items():
    if hashlib.sha256(Path(__file__).with_name(filename).read_bytes()).hexdigest() != expected:
        raise RuntimeError('same-field primitive source changed: '+filename)
from r604_rotating_frame_continuous_norms_20261127 import (
    I, Jet, sqrt_i, absolute, norm, upper_sum, rotating_difference,
)

MODES = (2, 4, 6, 8)
# Degree-four Bernstein coefficients of T_k(2t-1), k=1,...,4.
# Each pair is an exact rational numerator/denominator, not a rounded fit.
CHEBYSHEV_BERNSTEIN = (
    ((-1,1),(-1,2),(0,1),(1,2),(1,1)),
    ((1,1),(-1,1),(-5,3),(-1,1),(1,1)),
    ((-1,1),(7,2),(0,1),(-7,2),(1,1)),
    ((1,1),(-7,1),(35,3),(-7,1),(1,1)),
)


def half_split(coefficients):
    """Outward de Casteljau split, covering both entire half intervals."""
    row = tuple(coefficients)
    left, right = [row[0]], [row[-1]]
    while len(row) > 1:
        row = tuple((a+b)/2 for a,b in zip(row[:-1],row[1:]))
        left.append(row[0]);right.append(row[-1])
    return tuple(left),tuple(reversed(right))


def linear_vertical_primitive_bounds(coefficients):
    """Whole-angle |P d_s^j v| for j=0,1,2; all four true modes retained.

    P v = -sum b_m(s)*cos(m theta)/m. With x=cos(2theta), this
    is a degree-four Chebyshev polynomial on [-1,1]. The min of
    the exact weighted coefficient norm and a four-subinterval Bernstein
    hull is still an upper bound. The subdivisions are not angle samples.
    """
    if (len(coefficients) != 4 or any(len(row) != 3 for row in coefficients)
            or any(not isinstance(x,I) for row in coefficients for x in row)):
        raise TypeError('same-cell exact m=2,4,6,8 coefficient two-jets required')
    result=[]
    for j in range(3):
        scaled=[-row[j]/mode for row,mode in zip(coefficients,MODES)]
        weighted=upper_sum(*(absolute(x) for x in scaled))
        bernstein=[]
        for i in range(5):
            value=I(0)
            for coefficient,table in zip(scaled,CHEBYSHEV_BERNSTEIN):
                numerator,denominator=table[i]
                value=value+coefficient*numerator/denominator
            bernstein.append(value)
        leaves=[tuple(bernstein)]
        for _ in range(2):
            leaves=[child for row in leaves for child in half_split(row)]
        polynomial=max(max(abs(x.lo),abs(x.hi)) for row in leaves for x in row)
        result.append(I(min(weighted.hi,polynomial)))
    return tuple(result)


def same_cell_angular_data(design,left,right,core):
    """Read the original radial coefficients ONCE for both angular consumers."""
    radial=design.coefficients(left,right)
    if tuple(radial['modes']) != MODES:
        raise ValueError('the original complete four-mode angular field changed')
    complement=radial['core_complement']
    result={}
    for name in ('u','v'):
        values={key:I(0) for key in ('value','s','ss','theta')}
        if name=='u':
            for key,j in (('value',0),('s',1),('ss',2)):
                values[key]=complement[j]*core['u']
            values['theta']=complement[0]*core['utheta']
        for mode,coefficients in zip(MODES,radial[name]):
            for key,j in (('value',0),('s',1),('ss',2)):
                values[key]=values[key]+coefficients[j]*I(-1,1)
            values['theta']=values['theta']+coefficients[0]*I(-mode,mode)
        result[name]=Jet(*(values[k] for k in ('value','s','ss','theta')))
    result['v_coefficients']=radial['v']
    result['linear_vertical_primitive_bounds']=linear_vertical_primitive_bounds(radial['v'])
    return result


def normalization_remainder_jets(v):
    """Exact stable R(v)=v*((1+v^2)^(-1/2)-1), and its two radial jets."""
    c=1/sqrt_i(1+v.value**2)
    c_minus_one=-v.value**2*c**2/(1+c)
    first=c_minus_one*(c**2+c+1)  # dR/dv = c^3-1, without near-unit subtraction.
    return (v.value*c_minus_one, first*v.s,
            first*v.ss-3*v.value*c**5*v.s**2)


def radial_curvature_with_finite_vertical_primitive(current,reference,angular,
                                                     *,difference=None,
                                                     inherited_alpha_upper=None):
    """New K only, using R621 normal blocks and the exact SAME normalized T.

    A caller may cap the local alpha enclosure by a previously complete
    same-q global alpha. That prior claim is neither rerun nor issued here.
    All current/reference jets and original u/v coefficient boxes must refer
    to this identical radial interval and full material circle.
    """
    names=('a','a_s','a_ss','z','z_s','z_ss')
    if any(not isinstance(d[k],I) for d in (current,reference) for k in names):
        raise TypeError('all six current/reference interval jets required')
    a,as_,ass,z,zs,zss=[current[k] for k in names]
    a0,a0s,a0ss,z0,z0s,z0ss=[reference[k] for k in names]
    if min(a.lo,a0.lo)<=0:
        raise ArithmeticError('positive body radius required; cap is a separate Cartesian chart')
    speed2=a0s**2+z0s**2
    if speed2.lo<=0:
        raise ArithmeticError('reference speed lower bound needs refinement')
    speed=sqrt_i(speed2)
    radial_connection=(a0s*a0ss+z0s*z0ss)/speed2
    angular_connection=a0s/a0
    second_angular_connection=a0*a0s/speed2
    if difference is None:
        da,das,dass=a-a0,as_-a0s,ass-a0ss
        dz,dzs,dzss=z-z0,zs-z0s,zss-z0ss
    else:
        if any(not isinstance(difference[k],I) for k in names):
            raise TypeError('same-field direct difference must contain all six jets')
        da,das,dass,dz,dzs,dzss=[difference[k] for k in names]
    u,v=angular['u'],angular['v']
    A,B,C=rotating_difference(u,v)
    primitive=I(11)/7
    # C and R are odd and pi-periodic, so the rescaled R504 constant is pi/4.
    vertical_primitive=I(11)/14
    horizontal=[primitive*norm(getattr(A,k),getattr(B,k)) for k in ('value','s','ss')]
    remainder=normalization_remainder_jets(v)
    remainder_bounds=[vertical_primitive*absolute(x) for x in remainder]
    linear=angular['linear_vertical_primitive_bounds']
    vertical=[I(min((x+y).hi,(vertical_primitive*absolute(getattr(C,k))).hi))
              for x,y,k in zip(linear,remainder_bounds,('value','s','ss'))]
    # Separating orthogonal ambient components is legitimate for the vector
    # primitive; the generic complete vector norm is an independent upper bound.
    generic=[primitive*norm(getattr(A,k),getattr(B,k),getattr(C,k))
             for k in ('value','s','ss')]
    p0,p1,p2=[I(min(norm(h,vv).hi,g.hi)) for h,vv,g in zip(horizontal,vertical,generic)]
    radial_difference=upper_sum(norm(das,dzs),absolute(as_)*p0,absolute(a)*p1)
    angular_difference=norm(da+a*A.value,a*B.value,a*C.value)
    local_alpha=norm(radial_difference/speed,angular_difference/a0)
    alpha_upper=local_alpha.hi
    if inherited_alpha_upper is not None:
        if (not isinstance(inherited_alpha_upper,(float,int))
                or not math.isfinite(inherited_alpha_upper)
                or not 0<=inherited_alpha_upper<1):
            raise ValueError('complete same-q inherited alpha must lie in [0,1)')
        alpha_upper=min(alpha_upper,inherited_alpha_upper)
    alpha=I(alpha_upper)
    if not 0<=alpha.lo<=alpha.hi<1:
        raise ArithmeticError('same-cell immersion enclosure unresolved')
    h11=upper_sum(
        norm(dass-radial_connection*das,dzss-radial_connection*dzs),
        absolute(ass-radial_connection*as_)*p0,
        absolute(2*as_-radial_connection*a)*p1,absolute(a)*p2)/speed2
    first_coefficient=as_-angular_connection*a
    h12=norm(das-angular_connection*da+first_coefficient*A.value+a*A.s,
        first_coefficient*B.value+a*B.s,first_coefficient*C.value+a*C.s)/(a0*speed)
    h22=upper_sum(norm(a*(A.theta+B.value),
        -da+a*(B.theta-A.value)+second_angular_connection*das,
        a*C.theta+second_angular_connection*dzs),
        absolute(second_angular_connection*as_)*p0,
        absolute(second_angular_connection*a)*p1)/(a0**2)
    nr,nz=-z0s/speed,a0s/speed
    nr=I(max(-1.,nr.lo),min(1.,nr.hi))
    nz=I(max(-1.,nz.lo),min(1.,nz.hi))
    projected_primitive=[absolute(nr)*h+absolute(nz)*vv for h,vv in zip(horizontal,vertical)]
    normal11=upper_sum(absolute(nr*(dass-radial_connection*das)
        +nz*(dzss-radial_connection*dzs)),
        absolute(ass-radial_connection*as_)*projected_primitive[0],
        absolute(2*as_-radial_connection*a)*projected_primitive[1],
        absolute(a)*projected_primitive[2])/speed2
    normal12=absolute(nr*(first_coefficient*B.value+a*B.s)
        +nz*(first_coefficient*C.value+a*C.s))/(a0*speed)
    normal22=upper_sum(absolute(nr*(-da+a*(B.theta-A.value)+second_angular_connection*das)
        +nz*(a*C.theta+second_angular_connection*dzs)),
        absolute(second_angular_connection*as_)*projected_primitive[0],
        absolute(second_angular_connection*a)*projected_primitive[1])/(a0**2)
    cosine2=1-alpha**2
    if cosine2.lo<=0:
        raise ArithmeticError('normal alignment lower bound needs refinement')
    tilt=alpha*sqrt_i(2/(1+sqrt_i(cosine2)))
    full=[I(x.hi) for x in (h11,h12,h22)]
    normal=[I(x.hi) for x in (normal11,normal12,normal22)]
    current_normal=[x+tilt*y for x,y in zip(normal,full)]
    km=absolute(a0s*z0ss-z0s*a0ss)/(speed2*speed)
    ko=absolute(z0s)/(a0*speed)
    d1,d2=I(km.hi)+current_normal[0],I(ko.hi)+current_normal[2]
    off=current_normal[1]
    curvature=(d1+d2+sqrt_i((d1-d2)**2+4*off**2))/(2*(1-alpha)**2)
    return {'R623_principal_curvature_upper':curvature.hi,
        'R623_local_C1_upper_before_inherited_cap':local_alpha.hi,
        'R623_C1_upper_used_for_curvature':alpha.hi,
        'R623_full_covariant_blocks_upper':[x.hi for x in full],
        'R623_reference_normal_blocks_upper':[x.hi for x in normal],
        'R623_current_normal_blocks_upper':[x.hi for x in current_normal],
        'R623_oriented_normal_difference_upper':tilt.hi,
        'R623_reference_principal_curvatures_upper':[km.hi,ko.hi],
        'R623_horizontal_primitive_bounds_upper':[x.hi for x in horizontal],
        'R623_linear_vertical_primitive_bounds_upper':[x.hi for x in linear],
        'R623_normalization_remainder_primitive_bounds_upper':[x.hi for x in remainder_bounds],
        'R623_complete_vertical_primitive_bounds_upper':[x.hi for x in vertical],
        'R623_v_mode_radial_jet_intervals':[[[x.lo,x.hi] for x in row]
            for row in angular['v_coefficients']],
        'four_actual_modes':[2,4,6,8],
        'linear_primitive_degree_in_cos2theta':4,
        'Bernstein_entire_polynomial_subintervals':4,
        'nonlinear_vertical_normalization_and_all_radial_jets_paid':True,
        'full_horizontal_primitive_bound_retained':True,
        'new_global_C0_C1_or_reference_certificate_claim':False,
        'complete_same_q_material_coverage_is_callers_obligation':True}
