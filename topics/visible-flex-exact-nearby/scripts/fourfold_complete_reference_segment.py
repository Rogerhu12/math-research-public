#!/usr/bin/env python3
"""Complete exact retarget-reference segments and real-time angular images.

All eight time coefficients and every Laurent product frequency are kept.
The real-time image is bounded from the original degree-seven Bernstein
controls, not from the absolute values of a complex-time power expansion.
An exact subsegment may inherit the stronger original whole-segment bound.
No true-flow approximation or q lower bound is inferred by this module.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import json
import math
from pathlib import Path
import time

from flint import arb, acb, acb_poly, ctx

from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_retarget_reference_jets import RetargetReference, segment_arrays
from fourfold_retarget_reference_native_grid import NativeRetargetSegment
from fourfold_packaged_reference_bidisk import PackageReference, laurent


class CompleteReferenceSegment(NativeRetargetSegment):
    """Native symbolic reference with full periodic-product materialization."""
    def __init__(self, reference, leg, segment, left=Fraction(0), right=Fraction(1)):
        left, right = Fraction(left), Fraction(right)
        super().__init__(reference, leg, segment, left, right)
        self._full = None
        self._bernstein = None
        self._image_cache = {}

    def complete_periodic(self):
        """All coefficients of the exact subsegment U+Q*a or U+Q*Qend*a."""
        # This frozen method only uses the NativeRetargetSegment fields; it
        # neither accesses nor creates a package attribute.
        return PackageReference.complete_periodic(self)

    def complete_bernstein(self):
        """All eight ORIGINAL whole-segment Bernstein control polynomials."""
        if self._bernstein is not None:
            return self._bernstein
        bp, base = self.reference.base[self.leg]
        qp, q = self.reference.Q[self.leg]
        real, imag, brow = segment_arrays(bp, base, self.segment, ['U', 'L'])
        qr, qi, qrow = segment_arrays(qp, q, self.segment, ['Qtilde'])
        if brow != self.identity['base_shard'] or qrow != self.identity['Q_shard']:
            raise ValueError('Bernstein and Native reference shard identities differ')
        U = [[acb(arb(float(re)), arb(float(im)))
              for re, im in zip(real[j, 0], imag[j, 0])] for j in range(8)]
        Q = [[acb(arb(float(re)), arb(float(im)))
              for re, im in zip(qr[j], qi[j])] for j in range(8)]
        static = acb_poly(laurent(self.a.coefficients[0]))
        KB = self.a.K
        if self.end is not None:
            static *= acb_poly(laurent(self.end.coefficients[0]))
            KB += self.end.K
        KU, KQ = len(U[0])-1, len(Q[0])-1
        K = max(KU, KQ+KB)
        controls = []
        for j in range(8):
            product = acb_poly(laurent(Q[j]))*static
            row = [acb(0) for _ in range(2*K+1)]
            offset = K-KQ-KB
            for k in range(2*(KQ+KB)+1):
                row[offset+k] += product[k]
            offset = K-KU
            for k, value in enumerate(laurent(U[j])):
                row[offset+k] += value
            if not row[K].imag.contains(0):
                raise ValueError('complete real Bernstein mean lost reality')
            # The exact product is real on the real label axis. These are
            # coefficient enclosures, not newly selected dyadic midpoints.
            controls.append([acb(row[K].real)]+row[K+1:])
        self._bernstein = controls
        return self._bernstein

    def real_time_image(self, S, nodes=512, p=8):
        return real_time_image(self, S, nodes=nodes, p=p)


def real_time_image(reference, S, nodes=512, p=8):
    """Full |Im Y| on real local time and the entire normalized-label strip."""
    if not isinstance(reference, CompleteReferenceSegment):
        raise ValueError('validated complete symbolic reference segment required')
    S = Fraction(S)
    nodes, p = int(nodes), int(p)
    if S < 0 or nodes < 2 or nodes & (nodes-1) or p < 1:
        raise ValueError('nonnegative strip, power-of-two nodes and positive Taylor order required')
    key = (S, nodes, p, ctx.prec)
    if key in reference._image_cache:
        return reference._image_cache[key]
    start, cpu = time.monotonic(), time.process_time()
    controls = reference.complete_bernstein()
    K = len(controls[0])-1
    if len(controls) != 8 or any(len(row) != K+1 for row in controls):
        raise ValueError('complete degree-seven control polynomial expected')
    width, hx = exact_arb(S), arb.pi()/nodes
    sinh = [(k*width).sinh() for k in range(K+1)]
    cells, maximum = [], arb(0)
    for control_index, row in enumerate(controls):
        # If C(x) is real on R with positive coefficient c_k, then
        # Im C(x+iS) has positive coefficient i*c_k*sinh(kS).  Its
        # zero coefficient is zero; Im(x+iS)/4 contributes exactly S/4.
        positive = [acb(width/4)]+[acb(0, 1)*row[k]*sinh[k] for k in range(1, K+1)]
        frequencies = list(range(-K, K+1))
        coefficients = laurent(positive)
        current = list(coefficients)
        tables = []
        for order in range(p+1):
            folded = [acb(0) for _ in range(nodes)]
            for k, value in zip(frequencies, current):
                folded[k % nodes] += value
            values = [nodes*v for v in acb.dft(folded, inverse=True)]
            if any(not value.imag.contains(0) for value in values):
                raise ValueError('a real boundary-Imag polynomial lost exact reality')
            tables.append([value.real for value in values])
            if order < p:
                current = [value*acb(0, k)*hx/(order+1)
                           for k, value in zip(frequencies, current)]
        # Real angular offsets do not add an exp(|k|hx) factor: the integral
        # Taylor remainder of exp(i*k*x) has derivative modulus |k|^(p+1).
        remainder = (2*sum((abs(positive[k])*(k*hx)**(p+1)/math.factorial(p+1)
                            for k in range(1, K+1)), arb(0))).upper()
        bounds = [(sum((abs(tables[order][j]) for order in range(p+1)), arb(0))
                   +remainder).upper() for j in range(nodes)]
        index = max(range(nodes), key=lambda j: bounds[j])
        control_upper = max(bounds).upper()
        maximum = max(maximum, control_upper).upper()
        cells.append(dict(bernstein_control=control_index,
            complete_closed_angular_cell_cover=True,
            all_retained_Laurent_frequencies=list((-K, K)),
            complete_angular_Taylor_remainder=ball_record(remainder),
            maximum_boundary_Imag_modulus=ball_record(control_upper),
            maximum_node_Imag_modulus=ball_record(max(abs(v) for v in tables[0]).upper()),
            worst_cell_index=index,
            worst_cell_center_pi_multiple=str(Fraction(2*index, nodes)),
            exact_cell_halfwidth_pi_multiple=str(Fraction(1, nodes))))
    result = dict(physical_theta_image_strip=ball_record(maximum),
        complete_real_time_image_proved=True,
        scope='All real time in the ORIGINAL whole segment, hence also the specified exact subsegment; all labels |Im x|<=S.',
        initial_label_strip=str(S), angular_nodes=nodes, taylor_order=p,
        Fourier_degree=K, time_Bernstein_degree=7, control_count=8,
        original_whole_segment_controls=True,
        all_symbolic_products_retained=True,
        both_label_boundaries_by_exact_reality=True,
        interior_label_strip_by_harmonic_maximum=True,
        real_time_by_nonnegative_Bernstein_convexity=True,
        identity=reference.identity,
        source_sha256=sha(__file__),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in [
            'fourfold_retarget_reference_jets.py', 'fourfold_retarget_reference_native_grid.py',
            'fourfold_packaged_reference_bidisk.py']},
        exact_reference_document_provenance=dict(reference.reference.provenance),
        controls=cells, seconds=time.monotonic()-start, cpu_seconds=time.process_time()-cpu,
        limitations=['This is an exact finite-reference image gate, not a true flow error.',
            'No q lower bound or full complex-time image is inferred.',
            'Compare this physical image bound with the SAME actual field domain before composition.'])
    reference._image_cache[key] = result
    return result


def write_report(path, report):
    path = Path(path)
    raw = (json.dumps(report, indent=2)+'\n').encode()
    if len(raw) > 1_000_000 and path.suffix != '.gz':
        raise ValueError('a report larger than 1MB requires gzip')
    data = gzip.compress(raw, mtime=0) if path.suffix == '.gz' else raw
    if len(data) > 5_000_000:
        raise ValueError('split this report below 5MB')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def check_materialization(reference):
    """Independent finite symbolic products versus the complete polynomial."""
    full = reference.complete_periodic()
    checks = []
    for u in (acb(arb(1)/2, arb(1)/8), acb(0, arb(5)/4)):
        Y, Yu, Yx = reference.grid(u, 16, Fraction(1, 512))
        U, Uu, Ux = full.grid(u, 16, Fraction(1, 512))
        for j in range(16):
            label = acb(2*arb.pi()*j/16, arb(1)/512)
            actual, expected = (Y[j], Yu[j], Yx[j]), (label/4+U[j], Uu[j], arb(1)/4+Ux[j])
            if not all(a.real.overlaps(b.real) and a.imag.overlaps(b.imag)
                       for a, b in zip(actual, expected)):
                raise ValueError('complete materialization differs from the original symbolic products')
        checks.append(dict(time_real=ball_record(u.real), time_imaginary=ball_record(u.imag),
                           all_16_Y_Yu_Yx_checks_passed=True))
    # Real original Bernstein controls and the restricted full monomial
    # representation are also compared, with all frequencies retained.
    controls = reference.complete_bernstein()
    for local_u in (Fraction(-1), Fraction(1, 4), Fraction(1)):
        s = reference.left+(reference.right-reference.left)*(local_u+1)/2
        weights = [exact_arb(Fraction(math.comb(7, j))*s**j*(1-s)**(7-j)) for j in range(8)]
        u = acb(exact_arb(local_u))
        for k in range(full.K+1):
            expected = sum((weights[j]*controls[j][k] for j in range(8)), acb(0))
            actual = full.polynomials[full.K+k](u)
            if not (actual.real.overlaps(expected.real) and actual.imag.overlaps(expected.imag)):
                raise ValueError('original Bernstein and restricted full time coefficients disagree')
    return dict(complete_symbolic_product_checks=checks,
        all_original_Bernstein_coefficients_match_restricted_monomial_at_three_real_times=True,
        complete_Fourier_degree=full.K, complete_time_terms=full.terms)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--descriptor', type=Path, default=Path('data/phase_ring_continuation/step5_retargeted_reference/descriptor.json'))
    p.add_argument('--leg', choices=('forward', 'backward'), default='forward')
    p.add_argument('--segments', default='0,419,549')
    p.add_argument('--left', default='0'); p.add_argument('--right', default='1')
    p.add_argument('--label-widths', default='1/512,1/128')
    p.add_argument('--nodes', type=int, default=512); p.add_argument('--taylor-order', type=int, default=8)
    p.add_argument('--bits', type=int, default=256); p.add_argument('--out', type=Path, required=True)
    args = p.parse_args(); ctx.prec = args.bits
    start, cpu = time.monotonic(), time.process_time()
    ref = RetargetReference(args.descriptor)
    report = dict(kind='complete_symbolic_reference_and_real_time_full_label_image', complete=False,
        source_sha256=sha(__file__), descriptor_sha256=sha(args.descriptor), bits=args.bits, cases=[])
    write_report(args.out, report)
    for segment in map(int, args.segments.split(',')):
        model = CompleteReferenceSegment(ref, args.leg, segment, Fraction(args.left), Fraction(args.right))
        check = check_materialization(model)
        for S in map(Fraction, args.label_widths.split(',')):
            result = model.real_time_image(S, nodes=args.nodes, p=args.taylor_order)
            report['cases'].append(dict(segment=segment, leg=args.leg, materialization_checks=check, **result))
            write_report(args.out, report)
            print(json.dumps(dict(segment=segment, label_width=str(S),
                physical_theta_image_strip=result['physical_theta_image_strip'],
                cpu_seconds=result['cpu_seconds'])), flush=True)
    report.update(complete=True, seconds=time.monotonic()-start, cpu_seconds=time.process_time()-cpu)
    write_report(args.out, report)


if __name__ == '__main__':
    main()
