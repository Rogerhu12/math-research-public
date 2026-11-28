#!/usr/bin/env python3
"""Independent exact cross-check of the complete unit-marker PSD certificate.

This check uses symbolic rational differentiation for the three Hessian
numerators and direct affine power-to-Bernstein conversion for every actual
positive rectangle. The production proof uses polynomial arithmetic and
integer midpoint subdivision instead. No sampled point proves positivity.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path
import time

import sympy as sp

HERE = Path(__file__).resolve().parent
PROOF = HERE/'unit_marker_full_hessian_psd.py'
PROOF_SHA = '18160306c11257d3a1a989192e6ed160e3122b6206ea708dde268c47b9e8e5ef'


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def direct_coefficients(poly,rlo,rhi,clo,chi):
    """Exact full affine substitution, without midpoint subdivision."""
    n,m = max(i for i,j in poly),max(j for i,j in poly)
    monomial = {}
    dr,dc = rhi-rlo,chi-clo
    for (i,j),a in poly.items():
        for k in range(i+1):
            x = a*comb(i,k)*rlo**(i-k)*dr**k
            for l in range(j+1):
                key = k,l
                monomial[key] = monomial.get(key,Q(0))+x*comb(j,l)*clo**(j-l)*dc**l
    out = []
    for i in range(n+1):
        row = []
        for j in range(m+1):
            row.append(sum((a*Q(comb(i,k),comb(n,k))*Q(comb(j,l),comb(m,l))
                            for (k,l),a in monomial.items() if k<=i and l<=j),Q(0)))
        out.append(row)
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--certificate',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args = parser.parse_args()
    started = time.monotonic()
    if ref(PROOF)['sha256'] != PROOF_SHA:
        raise ValueError('The exact proof source changed')
    summary = json.loads(args.certificate.read_text())
    if (summary['status'] != 'complete_unit_marker_Cartesian_Hessian_operator_bound_certified'
            or summary['source'] != ref(PROOF) or not summary['complete_exact_single_cover']):
        raise ValueError('Use the actual complete source-bound proof')
    spec = importlib.util.spec_from_file_location('_actual_unit_marker_psd_proof',PROOF)
    proof = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(proof)
    D,P,A,C,T = proof.hessian_numerators()
    r,c = sp.symbols('r c',real=True)
    denominator = 4-4*r**3*c+r**6
    phi = 2*r**3*(1-r*r)**3*(2*c-r**3)/denominator
    fr,fc = sp.diff(phi,r),sp.diff(phi,c)
    expressions = {
        'A':sp.diff(fr,r)*denominator**3,
        'C':(fr/r+(9*(1-c*c)*sp.diff(fc,c)-9*c*fc)/r**2)*denominator**3,
        'T':(-3*(r*sp.diff(fc,r)-fc)/r**2)*denominator**3,
    }
    original = {'A':A,'C':C,'T':T}
    for name,expression in expressions.items():
        symbolic = sp.Poly(sp.cancel(expression),r,c)
        value = {tuple(power):Q(int(coef.p),int(coef.q)) for power,coef in symbolic.terms()}
        if value != original[name]:
            raise ArithmeticError('The complete independently differentiated Hessian differs: '+name)
    K = Q(summary['unit_Hessian_operator_upper_exact'])
    polynomials,_ = proof.principal_minor_polynomials(K)
    initial = {name:proof.bernstein_on_initial_rectangle(poly) for name,poly in polynomials.items()}
    leaf_ref = summary['full_leaf_record']
    if ref(leaf_ref['path']) != leaf_ref:
        raise ValueError('The actual positive rectangle file changed')
    leaves = [json.loads(line) for line in Path(leaf_ref['path']).read_text().splitlines()]
    total_coefficients = 0
    exact_rectangles = []
    for leaf in leaves:
        rlo,rhi = map(Q,leaf['r_exact']);clo,chi = map(Q,leaf['cos3theta_exact'])
        if not 0<=rlo<rhi<=1 or not -1<=clo<chi<=1:
            raise ArithmeticError('An actual proof rectangle lies outside the complete domain')
        exact_rectangles.append((rlo,rhi,clo,chi))
        for name,poly in polynomials.items():
            matrix,den = initial[name]
            for depth,bit in enumerate(leaf['path']):
                matrix,den = proof.split((matrix,den),depth%2)[int(bit)]
            direct = direct_coefficients(poly,rlo,rhi,clo,chi)
            exact = [[Q(value,den) for value in row] for row in matrix]
            if direct != exact or min(map(min,direct))<=0:
                raise ArithmeticError('Direct exact affine Bernstein conversion differs on a full box')
            recorded = leaf['proofs'][name]
            if (str(min(map(min,direct))) != recorded['minimum_coefficient_exact']
                    or proof.digest(dict(values=matrix,denominator=den))
                       != recorded['complete_integer_coefficient_matrix_sha256']):
                raise ArithmeticError('An actual durable positivity receipt changed')
            total_coefficients += sum(map(len,direct))
    # Independent rectangle sweep; it does not use the production binary-tree
    # collapse or its reported area sum.
    breaks = sorted({value for row in exact_rectangles for value in row[:2]})
    if breaks[0]!=0 or breaks[-1]!=1:
        raise ArithmeticError('The full radial interval is missing')
    for lo,hi in zip(breaks,breaks[1:]):
        mid = (lo+hi)/2
        intervals = sorted((a,b) for x,y,a,b in exact_rectangles if x<mid<y)
        cursor = Q(-1)
        for a,b in intervals:
            if a!=cursor:
                raise ArithmeticError('The complete angular cover has a gap or overlap')
            cursor = b
        if cursor!=1:
            raise ArithmeticError('The complete angular interval is missing')
    result = dict(status='independent_exact_unit_marker_PSD_check_passed',source=ref(__file__),
        certificate=ref(args.certificate),proof_source=ref(PROOF),sympy_version=sp.__version__,
        symbolic_rational_Hessian_numerators_identical=True,
        direct_affine_Bernstein_all_coefficients_identical=True,
        full_exact_rectangle_sweep_without_gap_or_overlap=True,
        actual_rectangles=len(leaves),polynomials_per_rectangle=len(polynomials),
        exact_coefficients_checked=total_coefficients,unit_Hessian_operator_upper_exact=str(K),
        finite_sampling_used_as_a_proof=False,new_field_or_metric_selected=False,
        seconds=time.monotonic()-started)
    if args.out.exists():
        raise ValueError('Preserve existing verification records')
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result),flush=True)


if __name__=='__main__':
    main()
