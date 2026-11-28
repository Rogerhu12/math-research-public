#!/usr/bin/env python3
"""Exact symbolic identities for the conditional linear-time C2 lemma.

No geometry input, sampled field, BVP, native worker or numerical time probe
is constructed. This checks polynomial/rational identities only. Inequality
directions, complete-field hypotheses and still-unpaid actual constants are
stated in the accompanying proof. SymPy is used with exact integers/rationals.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

import sympy as sp


def check():
    checks = {}

    def zero(name, value):
        entries = list(value) if isinstance(value, sp.MatrixBase) else [value]
        if not all(sp.cancel(sp.expand(item)) == 0 for item in entries):
            raise AssertionError(name)
        checks[name] = True

    # All identities hold over the indicated rational function fields; the
    # accompanying proof supplies h>0, 0<=t<=h and rho_0>0 where required.
    t, h, s = sp.symbols('t h s')
    kernel_integral = (sp.integrate(s*(h-t)/h, (s, 0, t))
                       + sp.integrate(t*(h-s)/h, (s, t, h)))
    zero('Peano_kernel_integral', kernel_integral-t*(h-t)/2)
    zero('Peano_maximum_one_eighth', h*h/8-t*(h-t)/2-(t-h/2)**2/2)

    u = sp.symbols('u')
    a = sp.Matrix(3, 2, sp.symbols('a0:6'))
    b = sp.Matrix(3, 2, sp.symbols('b0:6'))
    mixed = (1-u)*a+u*b
    zero('full_Gram_convex_combination_identity',
         mixed.T*mixed-((1-u)*a.T*a+u*b.T*b-u*(1-u)*(b-a).T*(b-a)))
    zero('full_Gram_perturbation_identity',
         (a+b).T*(a+b)-a.T*a-a.T*b-b.T*a-b.T*b)

    rho = sp.symbols('rho0:4')

    def material_derivative(value):
        return sp.cancel(sum(sp.diff(value, rho[j])*rho[j+1]
                             for j in range(3))/rho[0])

    q1 = material_derivative(1/rho[0])
    q2 = material_derivative(q1)
    q3 = material_derivative(q2)
    zero('support_curvature_material_first', q1+rho[1]/rho[0]**3)
    zero('support_curvature_material_second',
         q2+rho[2]/rho[0]**4-3*rho[1]**2/rho[0]**5)
    zero('support_curvature_material_third',
         q3+rho[3]/rho[0]**5-10*rho[1]*rho[2]/rho[0]**6
         +15*rho[1]**3/rho[0]**7)

    w = 126*t**5-420*t**6+540*t**7-315*t**8+70*t**9
    zero('nonic_window_first', sp.diff(w,t)-630*t**4*(1-t)**4)
    zero('nonic_window_second', sp.diff(w,t,2)-2520*t**3*(1-t)**3*(1-2*t))
    zero('nonic_window_third', sp.diff(w,t,3)
         -(7560*t**2*(1-t)**2*(1-2*t)**2-5040*t**3*(1-t)**3))
    zero('nonic_window_reflection', w+w.subs(t,1-t)-1)
    zero('nonic_window_half_integral', sp.integrate(1-w,(t,0,1))-sp.Rational(1,2))
    zero('window_third_derivative_coarse_constant',
         sp.Rational(7560,16)+sp.Rational(5040,64)-sp.Rational(2205,4))
    zero('window_endpoint_two_sided_four_jets', sp.Matrix([
        sp.diff(w,t,j).subs(t,0) for j in range(1,5)]
        +[sp.diff(w,t,j).subs(t,1) for j in range(1,5)]))

    q = sp.symbols('q0:4')
    window = sp.symbols('w0:4')
    lam, target, beta = sp.symbols('lambda k beta')

    def derivative(value):
        return sp.expand(sum(sp.diff(value, q[j])*q[j+1]
                             +sp.diff(value, window[j])*window[j+1]
                             for j in range(3)))

    coefficient = 1-lam*(1-window[0])
    gap = q[0]-target+beta
    curvature = coefficient*q[0]+lam*(1-window[0])*target+lam*beta*window[0]
    d1 = derivative(curvature)
    d2 = derivative(d1)
    d3 = derivative(d2)
    zero('complete_blended_curvature_first', d1-coefficient*q[1]-lam*window[1]*gap)
    zero('complete_blended_curvature_second',
         d2-coefficient*q[2]-2*lam*window[1]*q[1]-lam*window[2]*gap)
    zero('complete_blended_curvature_third',
         d3-coefficient*q[3]-3*lam*window[1]*q[2]
         -3*lam*window[2]*q[1]-lam*window[3]*gap)

    kappa = sp.symbols('kappa0:4')

    def curve_derivative(pair):
        scalar = [sum(sp.diff(value, kappa[j])*kappa[j+1]
                      for j in range(3)) for value in pair]
        # n'=kappa*T, T'=-kappa*n.
        return sp.Matrix([sp.expand(scalar[0]-kappa[0]*pair[1]),
                          sp.expand(scalar[1]+kappa[0]*pair[0])])

    gamma = sp.Matrix([0,1])
    for order in range(2,6):
        gamma = curve_derivative(gamma)
        if order == 4:
            zero('complete_curve_fourth_derivative', gamma-sp.Matrix([
                kappa[0]**3-kappa[2],-3*kappa[0]*kappa[1]]))
    zero('complete_curve_fifth_derivative', gamma-sp.Matrix([
        6*kappa[0]**2*kappa[1]-kappa[3],
        kappa[0]**4-4*kappa[0]*kappa[2]-3*kappa[1]**2]))

    x, y, z = sp.symbols('x y z')
    f = sp.Function('f')(x,y)
    generator = sp.Matrix([[0,-1,0],[1,0,0],[0,0,0]])
    disk = sp.Matrix([x,y,z+f])
    zero('Cartesian_disk_generator_is_affine', generator**2*disk-sp.Matrix([-x,-y,0]))
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True,
                        help='A new small algebra receipt outside the repository')
    args = parser.parse_args()
    source = Path(__file__).resolve()
    repo = source.parents[5]
    out = args.out.resolve()
    if out == repo or repo in out.parents:
        raise ValueError('The actual execution receipt belongs outside the source tree')
    checks = check()
    result = dict(schema='exact-linear-time-C2-algebra-only-v1',
        source=dict(path=str(source),sha256=hashlib.sha256(source.read_bytes()).hexdigest()),
        actual_argv=[sys.executable,*sys.argv],sympy_version=sp.__version__,
        checks=checks,passed=all(checks.values()),
        uses_exact_integer_rational_symbolic_arithmetic=True,
        actual_field_loaded=False,new_numerical_or_native_solve=False,
        actual_time_constants_paid=False,global_metric_certified=False,
        global_embedding_or_reach_certified=False,complete_surface=False)
    out.parent.mkdir(parents=True,exist_ok=True)
    with out.open('x') as stream:
        stream.write(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(passed=result['passed'],exact_identities=len(checks),
        out=str(out),sha256=hashlib.sha256(out.read_bytes()).hexdigest()),allow_nan=False),flush=True)


if __name__ == '__main__':
    main()
