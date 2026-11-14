#!/usr/bin/env python3
"""Directed true Fourier coefficients of the two-channel R37 core block.

Finite angular projections of the genuine infinite phase graph are enclosed
with the native primitive tail, all angular trapezoidal aliases, and directed
arithmetic. This certifies individual physical radial points or closed cells;
it does not certify the separate floating radial propagation runner.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, acb_mat, ctx

from fourfold_phase_beta_affine import AffineFastBulkTarget, provenance
from fourfold_phase_beta_bulk_interval import exact_arb, real_interval
from fourfold_phase_beta_bulk_box import CBox, Box, cdot, ccross
from fourfold_phase_beta_interval import ball_record


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def complex_record(value):
    return dict(real=ball_record(value.real), imag=ball_record(value.imag))


def matrix_record(value):
    return [[complex_record(value[i, j]) for j in range(value.ncols())]
            for i in range(value.nrows())]


def extend_half(value, parity):
    """Exact angular parity of the explicitly symmetric phase object."""
    reverse = parity*value[-2:0:-1]
    return CBox(Box(np.concatenate((value.real.lo, reverse.real.lo)),
                    np.concatenate((value.real.hi, reverse.real.hi))),
                Box(np.concatenate((value.imag.lo, reverse.imag.lo)),
                    np.concatenate((value.imag.hi, reverse.imag.hi))))


class TrueCoreCoefficientTarget(AffineFastBulkTarget):
    def bind_complex_chart(self, path):
        path = Path(path)
        saved = json.loads(path.read_text())
        if (not saved.get('proved') or not saved.get('exact_closed_radial_coverage_rechecked')
            or saved['origin_inputs_sha256'] != self.affine_definition['origin_inputs']['sha256']
            or saved['frozen_direction_sha256'] != self.affine_definition['direction']['sha256']):
            raise ValueError('the complete complex chart belongs to another actual object')
        left, right = map(Fraction, saved['exact_parameter_fractions'])
        if not left <= self.affine_delta <= right:
            raise ValueError('actual parameter exceeds the complete complex chart')
        source = Path(__file__).with_name('fourfold_phase_affine_complex_chart.py')
        if sha(source) != saved['source_sha256']:
            raise ValueError('complex chart source identity changed')
        topic = Path(__file__).resolve().parents[1]
        prefix = 'topics/visible-flex-exact-nearby/'
        for name, digest in saved['certificate_sha256'].items():
            actual = topic/name.removeprefix(prefix)
            if sha(actual) != digest:
                raise ValueError('complex chart input identity changed: '+name)
        self.chart, self.chart_path = saved, path

    def coefficient_moduli(self, radial, coefficient, K0, errors, strip):
        if not hasattr(self, 'chart'):
            raise ValueError('bind the actual complete complex denominator chart first')
        chart = self.chart
        radial_domain = list(map(lambda x:Fraction(float(x)), chart['radial_core']))
        if (not exact_arb(radial_domain[0]) <= radial.real.lower()
            or not radial.real.upper() <= exact_arb(radial_domain[1])
            or not strip/4 <= arb(float(chart['angular_strip_width']))):
            raise ValueError('requested low-block coefficient domain exceeds the actual chart')
        fields = self.fast_fields(radial, coefficient, errors, True, strip)
        F, X, Y, Frr, Frt, Ftt = [fields[key] for key in
            ((0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2))]
        cross = ccross(Y, X)
        upper = lambda value:arb(float(np.max(value.magnitude_upper())))
        G, R2 = upper(cdot(cross, cross)), upper(cdot(F, F))
        L, M, N = [upper(cdot(cross, value)) for value in (Frr, Frt, Ftt)]
        Slo = arb(float(chart['right_half_plane_lower']['support_numerator']))
        Rlo = arb(float(chart['right_half_plane_lower']['F_dot_F']))
        Nlo = arb(float(chart['Nraw_modulus_lower']))
        ell = arb(float(chart['ell_modulus_upper']))
        if not min(Slo, Rlo, Nlo) > 0:
            raise ValueError('complex chart lacks a positive denominator bound')
        factor = R2/Slo**2
        A, B, C0 = N*factor, M*factor, L*factor
        C = (M*M+upper(K0)*G*G)*factor/Nlo
        omega = C0+C
        FX, FY = upper(cdot(F, X)), upper(cdot(F, Y))
        d0 = (A*(upper(cdot(X, X))+FX*FX/Rlo)
              +2*B*(upper(cdot(X, Y))+FX*FY/Rlo)
              +C0*(upper(cdot(Y, Y))+FY*FY/Rlo))/Rlo
        # True quotient moduli use the paid chart. No broad rectangular
        # reciprocal is mistaken for a real loss of analytic nonvanishing.
        return {name:value.upper() for name, value in
            dict(a=A, b=B, c=C, tau=d0+omega*ell*ell, sigma=omega*ell).items()}

    def coefficient_values(self, radial, coefficient, K0, errors, sigma=None):
        fields = self.fast_fields(radial, coefficient, errors, True, sigma)
        if sigma is None or sigma == 0:
            for value in fields.values():
                if np.any(value.imag.lo > 0) or np.any(value.imag.hi < 0):
                    raise ValueError('mathematically real field lost its real axis')
            fields = {key:CBox(value.real) for key, value in fields.items()}
        F, X, Y, Frr, Frt, Ftt = [fields[key] for key in
            ((0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2))]
        cross = ccross(Y, X)
        G, R2, support = cdot(cross, cross), cdot(F, F), cdot(cross, F)
        l, m, n = [cdot(cross, value) for value in (Frr, Frt, Ftt)]
        factor = R2/(support*support)
        a, b, c0 = -n*factor, m*factor, -l*factor
        chat = -(m*m+K0*G*G)*factor/n
        omega = c0-chat
        FX, FY = cdot(F, X), cdot(F, Y)
        d0 = (a*(cdot(X, X)-FX*FX/R2)
              +2*b*(cdot(X, Y)-FX*FY/R2)
              +c0*(cdot(Y, Y)-FY*FY/R2))/R2
        if radial == acb(0):
            ell = Frt[:, 2]/X[:, 2]-FY/R2
        else:
            if radial.real.contains(0):
                raise ValueError('a nontrivial radial waist interval needs a paid F_z/r quotient')
            ell = Y[:, 2]/F[:, 2]-FY/R2
        values = dict(a=a, b=b, c=chat, tau=d0+omega*ell*ell, sigma=omega*ell)
        if any(not np.all(np.isfinite(value.magnitude_upper())) for value in values.values()):
            raise ValueError('a true core coefficient domain is nonfinite')
        return values

    def common_cells(self):
        domain = Fraction(3)
        cuts = {-domain, domain}
        for key, values in self.frozen.items():
            if key.endswith('_knots'):
                for x in values:
                    q = Fraction(float(x))
                    for r in (q, -q):
                        if -domain < r < domain:
                            cuts.add(r)
        return sorted(cuts)

    def point_or_cell(self, left, right, modes, normalized_strip):
        left, right = Fraction(left), Fraction(right)
        cuts = self.common_cells()
        selector = (left+right)/2
        position = bisect_right(cuts, selector)-1
        if position == len(cuts)-1:
            position -= 1
        a, b = cuts[position:position+2]
        if not a <= left <= right <= b:
            raise ValueError('requested radial interval crosses a true common polynomial span')
        self.set_cell(a, b)
        radial = acb(real_interval(left, right))
        coefficient, K0, _, errors, real = self.complete_fast_data(radial)
        if not real:
            raise ValueError('this finite core block uses the real material radius')
        values = self.coefficient_values(radial, coefficient, K0, errors)
        real_cover = self.coefficient_values(radial, coefficient, K0, errors, arb(0))
        a_lower = arb(float(np.min(real_cover['a'].real.lo)))
        if not a_lower > 0:
            raise ValueError('complete real angular radial-principal positivity failed')
        strip = exact_arb(normalized_strip)
        if not strip > 0:
            raise ValueError('positive normalized angular strip required')
        moduli = self.coefficient_moduli(radial, coefficient, K0, errors, strip)
        coefficients = {}
        raw = {}
        for name, value in values.items():
            parity = -1 if name in ('b', 'sigma') else 1
            full = extend_half(value, parity)
            transformed = self.fast_fourier.fft(full)/self.angles
            rows = {}
            for lag in range(-2*modes, 2*modes+1):
                alias = moduli[name]*((-(self.angles-abs(lag))*strip).exp()
                    +(-(self.angles+abs(lag))*strip).exp())/(1-(-self.angles*strip).exp())
                fee = arb(0, alias.upper())
                z = transformed[lag % self.angles].to_acb()+acb(fee, fee)
                rows[lag] = z
            coefficients[name] = rows
            raw[name] = dict(whole_angular_strip_modulus=ball_record(moduli[name]),
                finite_Fourier={str(lag):complex_record(z) for lag, z in rows.items()})
        indices = list(range(-modes, modes+1))
        n = len(indices)
        matrices = {name:acb_mat([[rows[i-j] for j in indices] for i in indices])
                    for name, rows in coefficients.items()}
        H = acb_mat([[coefficients['tau'][i-j]+acb(0, 4*(i-j))*coefficients['sigma'][i-j]
                     for j in indices] for i in indices])
        A, B, C = [matrices[name] for name in ('a', 'b', 'c')]
        D = acb_mat([[acb(0, 4*i) if i == j else 0 for j in indices] for i in indices])
        inverse = A.inv()
        F11, F12 = -inverse*B*D, inverse
        F21, F22 = D*B*inverse*B*D-D*C*D-H, -D*B*inverse
        generator = acb_mat([[([F11, F12] if i < n else [F21, F22])[j//n][i % n, j % n]
                              for j in range(2*n)] for i in range(2*n)])
        return dict(radial_interval=[str(left), str(right)], selected_common_span=[str(a), str(b)],
            true_target_curvature=complex_record(K0.to_acb()),
            normalized_angular_strip=str(normalized_strip),
            physical_angular_strip=str(Fraction(normalized_strip)/4),
            full_real_angular_a_lower=ball_record(a_lower),
            primitive_errors=[ball_record(error) for error in errors],
            true_coefficient_projection=raw,
            true_zero_order_matrix=matrix_record(H),
            true_two_channel_generator=matrix_record(generator),
            generator_definition='Galerkin A inverse after projection; all k=-N..N in both w and p slots',
            mean_index=modes, mean_is_retained=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--object', type=Path, default=Path(
        'data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    parser.add_argument('--modes', type=int, default=4)
    parser.add_argument('--primitive-nodes', type=int, default=512)
    parser.add_argument('--angles', type=int, default=1024)
    parser.add_argument('--bits', type=int, default=160)
    parser.add_argument('--chart', type=Path, default=Path(
        'data/phase_ring_continuation/type_fixed_step02_d5_affine_complex_chart_1over64.json'))
    parser.add_argument('--normalized-strip', type=Fraction, default=Fraction(1, 16))
    parser.add_argument('--points', type=Fraction, nargs='+', default=[Fraction(0), Fraction(1, 8), Fraction(61, 256)])
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.modes < 0 or args.angles <= 4*args.modes:
        raise ValueError('invalid low block and angular sampling')
    ctx.prec, ctx.cap = args.bits, 4
    wall, cpu = time.monotonic(), time.process_time()
    target = TrueCoreCoefficientTarget(args.object, args.primitive_nodes, args.angles,
                                       arb('.003'), arb('.0025'), arb('.32'))
    target.bind_complex_chart(args.chart)
    rows = []
    identity = provenance(target, args.object)
    identity['source_sha256'] = sha(__file__)
    report = dict(kind='directed_actual_R37_low_Fourier_coefficient_and_generator_inputs',
        complete=False, **identity,
        modes=args.modes, frequencies=list(range(-4*args.modes, 4*args.modes+1, 4)),
        quarter_primitive_nodes=args.primitive_nodes, angles=args.angles, bits=args.bits,
        complete_complex_chart_path=str(args.chart), complete_complex_chart_sha256=sha(args.chart),
        all_true_infinite_primitive_and_angular_alias_errors_included=True,
        radial_generator_inputs=rows,
        limitation='Only listed radial points/cells are certified; no radial ODE propagation or infinite high-frequency Schur complement is asserted.')
    args.out.parent.mkdir(parents=True, exist_ok=True)
    for point in args.points:
        rows.append(target.point_or_cell(point, point, args.modes, args.normalized_strip))
        args.out.write_text(json.dumps(report, indent=2)+'\n')
        print(json.dumps(dict(point=str(point), passed=True,
            a_lower=rows[-1]['full_real_angular_a_lower']['ball'])), flush=True)
    report.update(complete=True, CPU_seconds=time.process_time()-cpu,
                  wall_seconds=time.monotonic()-wall)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(complete=True, CPU_seconds=report['CPU_seconds'],
        wall_seconds=report['wall_seconds'], sha256=sha(args.out))), flush=True)


if __name__ == '__main__':
    main()
