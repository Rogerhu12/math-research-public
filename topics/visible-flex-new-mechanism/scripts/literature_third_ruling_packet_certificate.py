#!/usr/bin/env python3
"""Exact algebra for the eight-packet third-order ruling cancellation.

This is a symbolic identity certificate, not geometric evaluation or a search.
It verifies the pointwise characteristic RHS, the local eta0 formula, and the
integer seventh-difference weights.  The accompanying proof pays the support,
translation-degree, boundary, and range arguments separately.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as S


def certificate():
    x, k, h, omega, hs, oms = S.symbols('x k h omega hs omega_s', nonzero=True)
    f0, f1, f2, J0, J1, J2 = S.symbols('f0 f1 f2 J0 J1 J2star')
    z, d = x+omega, h*omega-k
    e = h*z-k
    Q = 1+e*e
    u, ux = h/z, -h/z**2
    c = hs/z-h*oms/z**2
    lam = (hs*z-h*oms)/h**2
    Ds = lambda F: S.diff(F, h)*hs+S.diff(F, k)*2*h*oms+S.diff(F, omega)*oms
    Dx = lambda F: S.diff(F, x)+S.diff(F, f0)*f1+S.diff(F, f1)*f2
    YT, YB = -f1/(2*z), h*f0/z-e*f1/(2*z)
    YN_s = h*f0/z-h*f1/2
    r = [(d*d+1)/(8*h), d/4, h/8]
    local = [h/(2*z), -e/(2*z), h*z/4-3*k/8+(k*k+1)/(8*h*z)]
    rho = (sum(rr*J for rr, J in zip(r, [J0, J1, J2]))
           +local[0]*f0*f0+local[1]*f0*f1+local[2]*f1*f1)
    K0 = k*z*z-(k*k+1)*z/h
    rhs = ((Ds(YT)**2+Ds(YB)**2+YN_s**2)/(2*u*u)
           +K0*rho-lam*Ds(rho))
    a0 = k*e/2
    a1 = -k*Q/(2*h)
    a2 = (k*h*z**3/4-(5*k*k+1+hs*hs/h**2)*z*z/8
          +k*(k*k+1)*z/(2*h)-(k*k+1)**2/(8*h*h)
          +hs*z*oms/(4*h)-k*hs*oms/(4*h*h)+(k*k+1)*hs*hs/(8*h**4))
    expected_rhs = (a0*f0*f0+a1*f0*f1+a2*f1*f1
                    +sum((K0*rr-lam*Ds(rr))*J for rr, J in zip(r, [J0, J1, J2])))
    Hsx = Ds(YT)*Dx(YT)+Ds(YB)*Dx(YB)
    Hxx = Dx(YT)**2+Dx(YB)**2
    eta0 = Hsx/(2*ux)-c*Hxx/(4*ux*ux)-Ds(rho)/2
    expected_eta0 = (-hs*e*f1*f1/(8*h)+hs*Q*f1*f2/(8*h*h)
        -(hs*z-h*oms)*Q*f2*f2/(16*h*h)
        -sum(Ds(rr)*J for rr, J in zip(r, [J0, J1, J2]))/2)
    first, second = S.factor(rhs-expected_rhs), S.factor(eta0-expected_eta0)
    weights = [(-1)**j*int(S.binomial(7, j)) for j in range(8)]
    moments = [sum(weights[j]*j**m for j in range(8)) for m in range(7)]
    # The normal component of the restored field supplies the ruling formula.
    W, Wx, eta = S.symbols('W W_x eta0')
    w = h*h-k*u
    full_eta = eta-u*W+h*Wx/2
    p = (u*u*W+u*full_eta)/(h*h)
    q = full_eta-k*p
    normal_component = -(u*p+w*q)/(2*h)
    third = S.factor(2*z*z/h*normal_component-(e*W-Q*Wx/(2*h)-Q*eta/(h*h)))
    assert first == 0 and second == 0 and third == 0 and moments == [0]*7
    return dict(exact_symbolic_certificate=True, no_research_geometry_evaluation=True,
        identities=dict(characteristic_rhs_difference=str(first), eta0_difference=str(second),
                        third_ruling_normal_component_difference=str(third)),
        seventh_difference_weights=weights, integer_moments_degrees_0_through_6=moments,
        packet_amplitude_definition='a_j = real_cube_root((-1)^j * binomial(7,j))',
        translation_degree_bounds=dict(characteristic_rhs=4, anchored_W=4, eta0=3, ruling_integral=6),
        support_localization_is_proved_in_note=True,
        profile_circle_third_order_certificate_scope='formal metric coefficients through order three',
        exact_finite_isometric_family=False, embedded_closed_surface=False, task_complete=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    result = certificate()
    result['source_script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    encoded = json.dumps(result, indent=2)+'\n'
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(encoded)
        print(json.dumps(dict(output=str(args.out), bytes=len(encoded.encode()),
                              sha256=hashlib.sha256(encoded.encode()).hexdigest())))
    else:
        print(encoded)


if __name__ == '__main__':
    main()
