#!/usr/bin/env python3
"""Exact R53 core bounds around an actual support-parameter vector.

All arithmetic for bounds/membership is Fraction. This certifies the
integral-defined mathematical core, not the floating GL position oracle,
the full Frenet domain, a BVP, a complete metric, or a closed surface.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ratio(x):
    return [x.numerator, x.denominator]


def binary(x):
    return F.from_float(float(x))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--center', type=Path, required=True)
    p.add_argument('--candidate-run', type=Path)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    spec = json.loads(a.center.read_text())
    if spec['base_mode'] != 3:
        raise ValueError('This declared neighborhood uses mode three')
    center = [F.from_float(float.fromhex(x)) for x in spec['center_control_hex']]
    qlo, qhi = F(spec['q_interval'][0]), F(spec['q_interval'][1])
    budget = F(spec['weighted_control_radius'])
    S, b, k = [F.from_float(float.fromhex(spec[name]))
               for name in ('halfwidth_hex', 'transition_hex', 'target_curvature_hex')]
    if not (0 < qlo <= qhi and budget > 0 and 0 < S and 0 < b and S+b < 1):
        raise ValueError('Declared parameter window is invalid')
    norm = sum(((3*j)**2-1)*abs(c) for j, c in enumerate(center, 2))
    deviation = 8*max(abs(qlo), abs(qhi)) + norm + budget
    rho_lo, rho_hi = 1-deviation, 1+deviation
    assert rho_lo > F(97, 200) and rho_hi < F(303, 200)
    old_lo, old_hi = 1/rho_hi, 1/rho_lo
    assert F(1, 5) <= k < old_lo
    # T=2*pi/3>2. The exact ninth-order symmetric step has J=2*S+b.
    J = 2*S+b
    assert 0 < J < 2
    beta_hi = (old_hi-k)*J/(2-J)
    new_hi = old_hi+beta_hi
    assert new_hi < F(243, 50)
    membership = None
    if a.candidate_run:
        run = json.loads(a.candidate_run.read_text())
        core = run['raw_return']['core_summary']
        params = list(core['physical_parameters'])
        if core['base_mode'] != 3 or core['core_kind'] != 'material-curvature-flattening':
            raise ValueError('Candidate uses another physical parameter convention')
        for name, val in [('halfwidth', S), ('transition', b), ('target_curvature', k)]:
            if binary(core[name]) != val:
                raise ValueError('Candidate has another core design: ' + name)
        if binary(core['curvature_blend']) != 1 or not 0 <= binary(core['homotopy']) <= 1:
            raise ValueError('Candidate is not on the declared tau=1 homotopy')
        q, candidate = binary(params[0]), [binary(x) for x in params[1:]]
        distance = sum(((3*j)**2-1)*abs(
            (candidate[j-2] if j-2 < len(candidate) else 0) -
            (center[j-2] if j-2 < len(center) else 0))
            for j in range(2, max(len(center), len(candidate))+2))
        member = qlo <= q <= qhi and distance <= budget
        membership = dict(run_sha256=sha(a.candidate_run), modes=len(candidate)+1,
            q=ratio(q), weighted_distance=ratio(distance), belongs=member,
            center_extended_by_zero=True)
        if not member:
            raise ValueError('Actual controls leave the proved neighborhood')
    result = dict(scope=__doc__, source_sha256=sha(__file__), center_sha256=sha(a.center),
        center_control_count=len(center), center_weighted_norm=ratio(norm),
        q_interval=[ratio(qlo), ratio(qhi)], weighted_radius=ratio(budget),
        rho_lower=ratio(rho_lo), rho_upper=ratio(rho_hi),
        old_curvature_lower=ratio(old_lo), old_curvature_upper=ratio(old_hi),
        window_mass=ratio(J), beta_upper=ratio(beta_hi),
        whole_homotopy_curvature_lower=ratio(k), whole_homotopy_curvature_upper=ratio(new_hi),
        rational_display_gates=dict(rho_lower_gt='97/200', rho_upper_lt='303/200',
                                   curvature_lower_ge='1/5', curvature_upper_lt='243/50'),
        finite_additional_modes_allowed=True, candidate_membership=membership,
        full_surface_claim=False)
    a.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(event='exact_core_neighborhood_proved',
        center_norm_display=float(norm), rho_lower_display=float(rho_lo),
        curvature_upper_display=float(new_hi), candidate_member=(membership or {}).get('belongs'))))


if __name__ == '__main__':
    main()
