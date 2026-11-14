#!/usr/bin/env python3
"""Exact-parameter sufficient budget for R112's shifted linear residual.

This proves a conditional box, not that an actual field lies in the box.
No sampled projection, solver flag, or unfinished field is accepted here.
The original fixed target is retained through its explicit bridge budget.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'OMP_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location('fd2d_pullback_target_supplier',
                                            HERE/'78718-prefix-metric-supplier-storage-v1.py')
supplier = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = supplier
spec.loader.exec_module(supplier)
I, qbounds = supplier.I, supplier.qbounds


def identity(path):
    path = Path(path)
    return {'file': str(path.resolve()), 'bytes': path.stat().st_size,
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


def bernstein_exact(coefficients):
    degree = len(coefficients)-1
    return [sum((coefficients[j]*Q(math.comb(k,j), math.comb(degree,j))
                 for j in range(k+1)), Q(0)) for k in range(degree+1)]


def upper(value):
    return float(value.hi)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--geometry', type=Path,
                    default=BASE/'notes/2026-11-09-db6f-root-flat17-coupled-m12f24.json')
    ap.add_argument('--target', type=Path,
                    default=BASE/'notes/2026-11-09-db6f-root-flat17-m12-target.json')
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    geometry = json.loads(args.geometry.read_text())
    target = json.loads(args.target.read_text())
    if target['geometry_sha256'] != identity(args.geometry)['sha256']:
        raise ValueError('Wrong frozen target')
    cfg = geometry['frozen_profile']
    if cfg['ramp_law'] != 'flat' or cfg['direction'] != 'outward' or cfg['cycles'] != 1:
        raise ValueError('This explicit budget is for the recorded flat17 target')
    delta, vu, vd, eps, eta = (Q(float(cfg[k])) for k in ('delta','vu','vd','ramp','ramp_eta'))
    profile = SimpleNamespace(delta=delta, eps=eps, eta=eta, sign=1)
    tu, td = delta/(vu*(1-eps)), delta/(vd*(1-eps))
    cuts = [Q(0), eps*eta, eps*(1-eta), eps, 1-eps,
            1-eps+eps*eta, 1-eps*eta, Q(1)]
    prefix_first, prefix_second = Q(0), Q(0)
    for phase, length, start in ((0,tu,Q(0)), (1,td,tu)):
        for k, (u0,u1) in enumerate(zip(cuts,cuts[1:])):
            left, right = start+length*u0, start+length*u1
            coefficients = supplier.Target.a_prefix_poly(profile,left,right,(phase,length,start,k))
            first = supplier.scale(supplier.der(coefficients), 1/(right-left))
            second = supplier.scale(supplier.der(first), 1/(right-left))
            prefix_first = max(prefix_first, *map(abs,bernstein_exact(first)))
            prefix_second = max(prefix_second, *map(abs,bernstein_exact(second)))
    length, pt, ps = (Q(target['bridge_constants'][k]) for k in ('L','pt','ps'))
    c2, c3 = 3*pt-length*ps, -2*pt+length*ps
    phi_bernstein = bernstein_exact([Q(0),Q(0),c2,c3])
    if min(phi_bernstein)<0 or max(phi_bernstein)>=3:
        raise ValueError('Bridge monotonic-radius proof window failed')
    # 0 <= phi < 3 < pi: the inward bridge radius never exceeds its value 1.
    bridge_second = (2*abs(c2)+3*abs(c3))/length
    # For the exact tail, |f_ss|=|kappa_meridian| |w|/sqrt(1+w^2) <= 6.
    second_bound = max(prefix_second, bridge_second, Q(6))
    if prefix_first>1 or 1+delta>=Q(11,10):
        raise ValueError('Global first-derivative/radius window failed')
    G0, G1 = Q(121,100), Q(11,5)
    exact_G2 = 2+Q(11,5)*second_bound
    G2 = Q(1000)
    if exact_G2>G2:
        raise ValueError('Conservative second metric derivative budget failed')
    # The field is zero in the deep tail. f>=.4 on its activity and its
    # image, after the actual global diffeomorphism has been established.
    fmin = Q(2,5)
    A, B, kappa, H = Q(1,10**10), Q(1,10**10), Q(1,10**6), Q(1,100)
    old_delta, linear, transfer = Q(3,10**8), Q(19,10**10), Q(1,10**12)
    Ai, Bi, ki, Hi = map(qbounds,(A,B,kappa,H))
    d = (Ai.square()+Bi.square()).sqrt()
    rem = (qbounds(G2)*Ai.square()/2+qbounds(G1)*ki*d
           +2*qbounds(G0)*Hi*d+2*ki*qbounds(old_delta*G0)
           +ki.square()*qbounds((1+old_delta)*G0))
    gamma = 1+qbounds(G1)*Ai/qbounds(fmin).square()
    frozen_upper = gamma*qbounds(linear)+rem/qbounds(fmin).square()
    original_upper = qbounds(transfer)+(1+qbounds(transfer))*frozen_upper
    if not upper(original_upper)<2e-9:
        raise ValueError('The sufficient box does not meet the original tolerance')
    out = {'status': 'PROVED_CONDITIONAL_NONCIRCLE_PULLBACK_BOX',
           'geometry': identity(args.geometry), 'target': identity(args.target),
           'script': identity(__file__),
           'prefix_first_derivative_upper_exact': str(prefix_first),
           'prefix_second_derivative_upper_exact': str(prefix_second),
           'bridge_phase_bernstein_exact': list(map(str,phi_bernstein)),
           'bridge_second_derivative_upper_exact': str(bridge_second),
           'metric_G2_analytic_upper_exact': str(exact_G2),
           'target_bounds_exact': {k:str(v) for k,v in
                                   [('fmin_on_activity',fmin),('G0',G0),('G1',G1),('G2',G2)]},
           'required_field_box_exact': {k:str(v) for k,v in
              [('p',A),('q',B),('Dv_operator',kappa),('D2v_bilinear',H),
               ('old_relative_error',old_delta),('continuous_linear_relative_error',linear),
               ('fixed_target_transfer',transfer)]},
           'coordinate_displacement_upper':upper(d),
           'nonlinear_coordinate_remainder_upper':upper(rem),
           'target_frame_factor_upper':upper(gamma),
           'frozen_target_metric_upper':upper(frozen_upper),
           'original_fixed_target_metric_upper':upper(original_upper),
           'below_original_2e9_tolerance':True,
           'actual_field_verified':False, 'actual_continuous_linear_error_verified':False,
           'new_complete_surface':False,
           'additional_hypotheses':['Actual C2 periodic field with interface two jets',
               'Global diffeomorphism; zero deep-tail field and f>=.4 on activity/image',
               'Own complete continuous field and linear residual certificates',
               'R21 same-background curvature and exact-bridge transfer evidence'],
           'proof':'R112 section 4.1; exact rational flat-ramp derivatives, frozen bridge phi Bernstein bound, analytic tail curvature <=6'}
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('prefix_first_derivative_upper_exact',
          'prefix_second_derivative_upper_exact','metric_G2_analytic_upper_exact',
          'nonlinear_coordinate_remainder_upper','original_fixed_target_metric_upper')},indent=2))


if __name__ == '__main__':
    main()
