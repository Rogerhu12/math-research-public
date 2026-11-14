#!/usr/bin/env python3
"""R86: ordered parameter tails from actual integrated spatial derivatives.

This module never reconstructs a flow from node samples.  Its main helper
uses proved common integral bounds for the true and finite sources.  The
optional density reader pays every finite Fourier coefficient and uses the
saved continuous error only through a strictly positive Cauchy loss.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path

from flint import arb, acb, ctx


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def exact(value):
    value = Fraction(value)
    return arb(value.numerator) / value.denominator


def nonnegative(value):
    value = arb(value)
    if not value.is_finite() or not value >= 0:
        raise ValueError('a finite nonnegative directed bound is required')
    return value.upper()


def upper(record):
    return nonnegative(arb(record['upper']).upper())


def record(value):
    value = nonnegative(value)
    return dict(upper=str(value), mid_float=float(value))


def spatial_ordered_tails(A, B, C):
    """Return sup-strip tails for V0,V1,V2, each retained through order two.

    A[j], B[j], C[j] are integral bounds for spatial derivative j of g0,
    g1, g2, respectively, on the whole trajectory tube.  The caller must
    separately check the tube inclusion and that g1,g2 are actual parameter
    derivatives of g0.  All derivatives are ordinary derivatives, not
    normalized Taylor coefficients.
    """
    if any(len(row) != 3 for row in (A, B, C)):
        raise ValueError('three spatial derivatives are required per source')
    A, B, C = [list(map(nonnegative, row)) for row in (A, B, C)]
    a0, a1, a2 = A
    b0, b1, b2 = B
    c0, c1, c2 = C
    growth = a1.exp().upper()
    zstar = (growth*b0).upper()
    du = (a1*a0).upper()
    dz = (a1*zstar+b1*a0).upper()
    d2 = (a1*c0+2*b1*b0+c1*a0).upper()
    tail0 = (a1*du+a2*a0*a0/2).upper()
    tail1 = (a1*dz+a2*a0*b0+b1*du+b2*a0*a0/2).upper()
    terms2 = dict(
        propagated_quadratic_approximation=a1*d2,
        shifted_g0_derivative_on_G2=a2*a0*c0,
        actual_quadratic_variation=a2*zstar*zstar,
        source1_times_variation_defect=2*b1*dz,
        shifted_source1_derivative=2*b2*a0*b0,
        source2_times_position_defect=c1*du,
        source2_spatial_Taylor_remainder=c2*a0*a0/2)
    tail2 = (growth*sum(terms2.values(), arb(0))).upper()
    return dict(tails=[tail0, tail1, tail2], exponential_growth=growth,
        parameter_first_variation_bound=zstar,
        position_minus_first_integral_bound=du,
        parameter_variation_minus_first_integral_bound=dz,
        quadratic_parameter_approximation_minus_first_integral_bound=d2,
        unpropagated_second_parameter_terms={k:v.upper() for k,v in terms2.items()})


def ordered_source_error_fees(A, B, C, errors):
    """Pay V(g)-V(ghat) without treating the three approximants as a family.

    errors[k][j] bounds integral sup |partial_x^j(g_k-ghat_k)| for j=0,1.
    A/B/C are common bounds for true and approximate sources.  They may be
    obtained by adding the continuous errors to the finite derivative norms.
    """
    if len(errors) != 3 or any(len(row) != 2 for row in errors):
        raise ValueError('three rows of zeroth/first derivative errors required')
    A, B, C = [list(map(nonnegative, row)) for row in (A, B, C)]
    E = [list(map(nonnegative, row)) for row in errors]
    a0, a1 = A[:2]
    b0, b1 = B[:2]
    c0, c1 = C[:2]
    e00,e01 = E[0]
    e10,e11 = E[1]
    e20,e21 = E[2]
    return [(e00*(1+a1)+a0*e01).upper(),
        ((1+a1)*e10+b1*e00+b0*e01+a0*e11).upper(),
        ((1+a1)*e20+c1*e00+c0*e01+2*b1*e10+2*b0*e11+a0*e21).upper()]


def certify(A, B, C, errors, *, trajectory_strip_gap, finite_output_fees=None):
    """Combine the actual tails, continuous source fees, and finite fees.

    This is an arithmetic conditional certificate.  It does not assert that
    supplied bounds have already been proved for a particular geometric map.
    """
    A, B, C = [list(map(nonnegative, row)) for row in (A, B, C)]
    gap = nonnegative(trajectory_strip_gap)
    if not A[0] < gap:
        raise ValueError('the complete trajectory tube has not been contained')
    tails = spatial_ordered_tails(A, B, C)
    source = ordered_source_error_fees(A, B, C, errors)
    finite = [arb(0)]*3 if finite_output_fees is None else list(map(nonnegative, finite_output_fees))
    if len(finite) != 3:
        raise ValueError('one finite integration/projection fee per output required')
    return dict(**tails, source_error_fees=source, finite_output_fees=finite,
        total_errors=[(t+e+f).upper() for t,e,f in zip(tails['tails'],source,finite)],
        trajectory_strip_gap=gap, trajectory_tube_included=True)


def _decode(row):
    if len(row) != 4:
        raise ValueError('wrong exact complex dyadic encoding')
    return acb(arb((int(row[0]), int(row[1]))), arb((int(row[2]), int(row[3]))))


def _integer_derivative_factor(degree, loss, derivative):
    """Exact finite-frequency max k^j exp(-loss*k); no float selector."""
    if derivative == 0:
        return arb(1)
    if degree == 0:
        return arb(0)
    peak = Fraction(derivative)/loss
    lo = peak.numerator//peak.denominator
    candidates = {1, degree, min(degree,max(1,lo)), min(degree,max(1,lo+1))}
    return max(((arb(k)**derivative*(-exact(loss)*k).exp()).upper()
                for k in candidates), key=lambda z:z).upper()


def density_spatial_budget(report_path, derivative_strip=Fraction(7,2048), *, exact_rectangle=False):
    """Recover one completed g0 leaf's true integrated derivatives j=0,1,2.

    exact_rectangle=True streams its saved exact full Fourier polynomial.
    Otherwise only already proved row A_S norms and the retained degree are
    used, with an exact finite-frequency Cauchy factor.  No new field samples
    or temporal reconstruction are performed.
    """
    report_path = Path(report_path)
    report = read(report_path)
    if not report.get('complete') or not report.get('complete_continuous_true_density_proved'):
        raise ValueError('a completed continuous true-density certificate is required')
    S, d = Fraction(report['label_strip']), Fraction(derivative_strip)
    if not 0 <= d < S:
        raise ValueError('strict derivative strip loss required')
    E = upper(report['R72_inputs']['integrated_approximation_error_E'])
    loss = S-d
    finite = [arb(0)]*3
    row_norms = []
    rectangle = None
    if exact_rectangle:
        link = report.get('density_exact_rectangle')
        if link is None:
            raise ValueError('this leaf did not preserve its exact density rectangle')
        path = Path(link['path'])
        if sha(path) != link['sha256']:
            raise ValueError('exact density manifest hash changed')
        manifest = read(path)
        if (not manifest.get('complete') or not manifest.get('exactly_reloaded')
            or manifest['frequency_scale'] != 1
            or manifest['identity']['identity'] != report['identity']):
            raise ValueError('exact rectangle identity or normalization differs')
        degree = int(manifest['Fourier_degree'])
        if report.get('density_coefficient_sha256',manifest['coefficient_sha256']) != manifest['coefficient_sha256']:
            raise ValueError('saved finite density coefficient identity differs')
        weights = [(exact(d)*k).exp() for k in range(degree+1)]
        running = 0
        digest = hashlib.sha256()
        digest.update(b'exact-positive-time-Fourier-v1;frequency=1\n')
        for item in manifest['shards']:
            shard = path.parent/item['path']
            if (sha(shard) != item['sha256'] or shard.stat().st_size != item['bytes']
                or item['time_start'] != running):
                raise ValueError('exact density shard identity or time cover changed')
            payload = read(shard)
            if (payload['identity'] != manifest['identity']
                or payload['time_start'] != running
                or payload['time_stop'] != item['time_stop']):
                raise ValueError('shard payload identity or time range differs')
            if len(payload['coefficients']) != item['time_stop']-running:
                raise ValueError('wrong exact density shard row count')
            for encoded in payload['coefficients']:
                if len(encoded) != degree+1:
                    raise ValueError('exact density row degree differs')
                digest.update((json.dumps(encoded,separators=(',',':'))+'\n').encode())
                row = list(map(_decode,encoded))
                if not row[0].imag.is_zero():
                    raise ValueError('constant coefficient must be exactly real')
                norms = [arb(0)]*3
                for k,z in enumerate(row):
                    magnitude = abs(z)*(1 if k==0 else 2)*weights[k]
                    for j in range(3):
                        if j==0 or k:
                            norms[j] += magnitude*(k**j)
                norms = [v.upper() for v in norms]
                row_norms.append(list(map(record,norms)))
                for j in range(3):
                    finite[j] += 2*norms[j]/(running+1)
                running += 1
        if running != manifest['time_terms'] or digest.hexdigest() != manifest['coefficient_sha256']:
            raise ValueError('complete finite density coefficient digest differs')
        rectangle = dict(path=str(path),sha256=sha(path),shards=len(manifest['shards']),
            finite_coefficient_sha256=manifest['coefficient_sha256'])
        method = 'all_exact_finite_coefficients'
    else:
        degree = int(report.get('density_compression',{}).get('selected_Fourier_degree',report['density_layout']['degree']))
        factors = [_integer_derivative_factor(degree,loss,j) for j in range(3)]
        for i,row in enumerate(report['R72_inputs']['finite_time_coefficient_A_norms']):
            norm = upper(row)
            for j in range(3):
                finite[j] += 2*norm*factors[j]/(i+1)
        method = 'saved_complete_A_S_row_norms_and_finite_degree'
    finite = [v.upper() for v in finite]
    errors = [(E*(1 if j<2 else 2)/exact(loss)**j).upper() for j in range(3)]
    true = [(v+e).upper() for v,e in zip(finite,errors)]
    return dict(kind='R86_completed_density_spatial_derivative_budget',complete=True,
        source_sha256=sha(__file__),report_path=str(report_path),report_sha256=sha(report_path),
        exact_reference_identity=report['identity']['reference'],
        spatial_derivative_coordinate='normalized initial label x; frequency k, not 4k',
        input_strip=str(S),derivative_strip=str(d),strict_error_Cauchy_loss=str(loss),
        method=method,retained_Fourier_degree=degree,exact_rectangle=rectangle,
        finite_integrated_derivative_norms=list(map(record,finite)),
        integrated_continuous_derivative_errors=list(map(record,errors)),
        common_true_and_finite_integrated_derivative_bounds=list(map(record,true)),
        exact_time_row_derivative_norms=row_norms,
        signed_time_halfwidth_already_in_source=True,
        new_field_or_reference_samples_used=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--density-report',type=Path,required=True)
    parser.add_argument('--derivative-strip',default='7/2048')
    parser.add_argument('--exact-rectangle',action='store_true')
    parser.add_argument('--bits',type=int,default=192)
    parser.add_argument('--out',type=Path,required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    result = density_spatial_budget(args.density_report,Fraction(args.derivative_strip),
                                    exact_rectangle=args.exact_rectangle)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(method=result['method'],
        bounds=result['common_true_and_finite_integrated_derivative_bounds'],
        source_sha256=result['source_sha256'],report_sha256=sha(args.out))),flush=True)


if __name__ == '__main__':
    main()
