#!/usr/bin/env python3
"""Independent exact cover and operator-constant audit of the R64 certificate.

Does not import the positive-cap generator or any geometry/collector module.
The analytic source review is separate; this checks the frozen box arithmetic.
"""
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import argparse
from flint import arb, ctx


def A(x):
    f = Fraction.from_float(x) if isinstance(x, float) else Fraction(x)
    return arb(f.numerator)/f.denominator


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def endpoint(v, upper=True):
    a, b = (v.upper() if upper else v.lower()).man_exp()
    return str(Fraction(int(a))*Fraction(2)**int(b))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--report', type=Path, default=Path('notes/2026-11-12-step4-actual-positive-cap.json'))
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    ctx.prec = 256
    d = json.loads(args.report.read_text())
    assert d['complete'] and not d['pending'] and not d['failed_cells']
    assert sha(d['object_path']) == d['object_sha256']
    assert sha('scripts/fourfold_phase_actual_positive_cap.py') == d['source_sha256']
    for n, h in d['dependency_sha256'].items():
        assert sha(Path('scripts')/n) == h
    rows = sorted(d['cells'], key=lambda r: Fraction(r['radial_interval'][0]))
    rootlo, roothi = map(Fraction, d['root_interval'])
    cut = Fraction(d['physical_regular_cut'])
    cursor = rootlo
    for row in rows:
        left, right = map(Fraction, row['radial_interval'])
        assert left == cursor and left < right <= cut
        cursor = right
        assert row['K_over_distance_input'][0] > 0
        for key in ['Fz', 'support', 'norm2', 'area2', 'minus_nraw', 'alpha', 'eta']:
            assert row['real_geometry'][key][0] > 0
    assert cursor == cut and len(rows) == 55
    lo, hi = A(cut-roothi), A(cut-rootlo)
    def lower(key): return min(A(r['real_geometry'][key][0]) for r in rows)
    def upper(key): return max(A(r['real_geometry'][key][1]) for r in rows)
    kmin = min(A(r['K_over_distance_input'][0]) for r in rows)
    kmax = max(A(r['K_over_distance_input'][1]) for r in rows)
    vr = max(A(abs(x)) for r in rows for x in r['real_geometry']['drift_theta'])
    def complex_upper(key):
        return max(arb(r['complex_geometry'][key]['upper']).upper() for r in rows)
    vc = complex_upper('drift_theta_modulus')
    jr, jc = (vr*hi).exp(), (vc*hi).exp()
    m = min(lower('alpha'), lower('eta')*kmin)/jr
    M = max(upper('alpha'), upper('eta')*kmax)*jr
    elo, ehi = lo/4, hi/4
    CE = max(1/elo+ehi/3+ehi**2/12, 1/elo+ehi/3+hi*ehi/3)
    g = (1+hi**2/arb.pi()**2)/m
    H = CE.sqrt()*(1+M*g)
    DN = CE*M
    CI = (1+max(A(3), 4/lo**2)).sqrt()
    physical = A(d['normalized_angle_strip'])/4
    rho = physical/(2*jc)
    mc = max(complex_upper('alpha_modulus'), complex_upper('eta_modulus')*kmax)*jc
    nc = 2*mc*(-rho/2).exp()/(-(-rho/2).expm1())**2
    cl = CE*(1+2*g*(M+1))**2
    s = A(Fraction(1, 2**75))
    assert s < rho/2 and s*nc < 1 and 2*g*s*nc < 1 and 2*cl*s*nc < 1
    assert m > A('0.0247') and M < A('46.05')
    assert g < A('40.389') and H < 34550 and DN < 15875
    assert CI < A('172.371') and CI*H < 5955237
    assert jr.sqrt()*upper('Yz') < A('0.299')
    values = dict(m=m, M=M, J=jr, CE=CE, g=g, poisson=H, DN=DN,
                  interior=CI, ordinary_contact=CI*H, rho=rho, Ccomplex=mc,
                  coefficient_moment=nc, DN_perturbation=cl)
    report = dict(kind='independent_positive_collar_exact_cover_and_constants', complete=True,
                  bits=256, source_sha256=sha(__file__), input_report_sha256=sha(args.report),
                  exact_radial_cover=True, cells=len(rows),
                  exact_radial_endpoints=[str(rootlo),str(cut)],
                  actual_parameter=d['exact_delta_fraction'],
                  constants={k:dict(lower=endpoint(v,False),upper=endpoint(v)) for k,v in values.items()},
                  explicit_analytic_weight='1/'+str(2**75), all_four_weight_gates=True,
                  published_safe_bounds_verified=True,
                  limitation='Arithmetic and coverage audit, combined with a separate full source/proof review; no new exterior cap or exact family.')
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(complete=True,cells=len(rows),m=str(m),M=str(M),g=str(g),
                         ordinary_contact=str(CI*H),analytic_weight='2^-75'),indent=2))


if __name__ == '__main__':
    main()
