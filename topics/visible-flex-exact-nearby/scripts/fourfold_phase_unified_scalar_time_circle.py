#!/usr/bin/env python3
"""True scalar samples on ordinary and root-deflated complex time circles.

The exact time endpoints are rational-plus-pi objects.  Every sample is tied
to one passed whole-angle/time germ, the exact target and the old reference
time grid.  A selected analytic germ is not silently declared to represent
other real spline spans.  The turn wave is sin(eta)*sqrt(Q), never sqrt(-K).
The retained scalar samples can be passed to the frozen circle_coefficients
and time_alias_bounds functions; no reference/flow error is asserted here.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, ctx

from fourfold_phase_beta_affine import AffineBulkTarget, sha
from fourfold_phase_beta_bulk_interval import exact_arb, complex_pad
from fourfold_phase_beta_interval import (
    array_derivative, ball_record, primitive_fourier_budget,
    series_constant, vector_dot,
)
from fourfold_phase_field_time_refined_root import prepare_refined_root
from fourfold_phase_field_time_turn_collar import PiTime, TurnCollarTimeModel
from fourfold_phase_uniform_field_time_grid_fast import f_invariants
from fourfold_native_series_fft import NativeSeriesFFT


def document(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def exact_time(value):
    if isinstance(value, PiTime):
        return value
    if isinstance(value, str):
        return PiTime(Fraction(value))
    if 'kind' in value:
        return PiTime.from_record(value)
    return PiTime(Fraction(value['rational']), Fraction(value['pi_coefficient']))


def complex_record(value):
    return dict(real=ball_record(value.real), imag=ball_record(value.imag))


def write_report(path, report):
    path = Path(path)
    raw = (json.dumps(report, indent=2)+'\n').encode()
    if len(raw) > 1_000_000 and path.suffix != '.gz':
        raise ValueError('reports larger than 1MB require gzip')
    data = gzip.compress(raw, mtime=0) if path.suffix == '.gz' else raw
    if len(data) > 5_000_000:
        raise ValueError('split this report below 5MB')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


_DEFLATION_CACHE = {}


class RootDeflatedCurvature:
    """A true J(rho)=-K(t-rho)/rho with a paid full radial remainder."""
    def __init__(self, object_path, root_package, nodes, R0, RE, sigma,
                 *, radius=Fraction(3, 1250), degree=64):
        if degree < 4:
            raise ValueError('at least four radial coefficients are required')
        self.root_package, self.root = root_package, root_package.root
        self.degree, self.RK = int(degree), exact_arb(radius)
        self.radius_fraction = Fraction(radius)
        if not R0 > RE > self.RK > 0:
            raise ValueError('nested positive curvature/metric/primitive radii required')
        self.positive_cell = tuple(map(Fraction, root_package.provenance['root_common_span']))
        positive = AffineBulkTarget(object_path, nodes, nodes, R0, RE, sigma)
        positive.set_cell(*self.positive_cell)
        positive.fourier = NativeSeriesFFT()
        oldcap = ctx.cap
        try:
            ctx.cap = max(21, degree+4)
            budget = positive.analytic_input_budget(acb(self.root), R0, sigma, RE)
            root_K = positive.target(self.root, self.RK, budget)[4]
            if root_K.prec <= degree or not root_K[0].real.contains(0):
                raise ValueError('inconsistent actual root or insufficient radial jet')
            # The existing true-root certificate makes K(t) exactly zero.
            # All derivatives are real at the true real root, even though the
            # arithmetic FFT enclosure can have a small imaginary component.
            self.coefficient = [acb((-root_K[j+1]/self.RK).real) for j in range(degree)]
            ctx.cap = 4
            disk = complex_pad(acb(self.root), self.RK)
            coefficient, Kdisk, _, disk_budget = positive.complete_data(disk)
            first = array_derivative(coefficient)
            Efinite = sum((vector_dot(first[k], first[(-k) % nodes])
                           for k in range(nodes)), series_constant(0))[0]
            Etrue = complex_pad(Efinite, disk_budget['E_error'])
            a = positive.scalars(disk, 1)[2][0]
            if not (a.abs_lower() > 0 and Etrue.abs_lower() > 0 and Kdisk.is_finite()):
                raise ValueError('full curvature disk has no holomorphic denominator gate')
            self.K_bound = abs(Kdisk).upper()
            self.domain = dict(radius_modulus_lower=ball_record(a.abs_lower()),
                E_modulus_lower=ball_record(Etrue.abs_lower()),
                K_modulus_upper=ball_record(self.K_bound))
        finally:
            ctx.cap = oldcap

    def evaluate(self, eta):
        cosine, sine = eta.cos(), eta.sin()
        rho = self.root*(1-cosine)
        ratio = (abs(rho)/self.RK).upper()
        if not ratio < 1 or not (1+cosine).abs_lower() > 0:
            raise ValueError('turn sample leaves the paid deflation disk')
        z = rho/self.RK
        J = self.coefficient[-1]
        for coefficient in self.coefficient[-2::-1]:
            J = coefficient+z*J
        tail = (self.K_bound/self.RK*ratio**self.degree/(1-ratio)).upper()
        Jtrue = complex_pad(J, tail)
        Q = self.root*Jtrue/(1+cosine)
        if not Q.real > 0:
            raise ValueError('true Q square-root branch is not separated')
        return sine*Q.sqrt(analytic=True), dict(
            Q=complex_record(Q), full_J_radial_tail=ball_record(tail),
            normalized_radial_modulus=ball_record(ratio))


def cached_deflation(object_path, root_package, nodes, R0, RE, sigma, radius, degree):
    key = (root_package.object_sha256, root_package.certificate_sha256,
           ctx.prec, int(nodes), tuple(map(str, (R0, RE, sigma))),
           Fraction(radius), int(degree), root_package.root.str(ctx.dps+8))
    if key not in _DEFLATION_CACHE:
        _DEFLATION_CACHE[key] = RootDeflatedCurvature(
            object_path, root_package, nodes, R0, RE, sigma, radius=radius, degree=degree)
    return _DEFLATION_CACHE[key]


class UnifiedScalarTimeCircleField:
    """Same scalar sampling contract on ordinary and genuine turn germs."""
    def __init__(self, descriptor_path, domain_path, *, germ=-1, nodes=1024,
                 root_nodes=None, radial_degree=64, curvature_radius=Fraction(3, 1250)):
        self.descriptor_path, self.domain_path = Path(descriptor_path), Path(domain_path)
        descriptor, domain = document(descriptor_path), document(domain_path)
        if not (descriptor.get('complete') and domain.get('complete')
                and domain.get('proved_full_physical_angle_and_complex_time_domain')
                and domain.get('complete_common_span_coverage')):
            raise ValueError('a passed complete whole-angle/time germ-union domain is required')
        if domain['retarget_descriptor_sha256'] != sha(descriptor_path):
            raise ValueError('domain and retarget descriptor identities differ')
        self.object_path, self.root_path = [Path(descriptor[k]['path'])
                                          for k in ('target_object', 'target_root')]
        for key, path, hash_key in [('target_object', self.object_path, 'target_object_sha256'),
                                    ('target_root', self.root_path, 'target_root_sha256')]:
            if sha(path) != descriptor[key]['sha256'] or sha(path) != domain[hash_key]:
                raise ValueError('domain and exact object/root identities differ')
        if domain['exact_delta_fraction'] != descriptor['target_exact_delta_fraction']:
            raise ValueError('exact affine parameter differs')
        self.selected, self.domain = domain['germs'][germ], domain
        if not self.selected['passed']:
            raise ValueError('the selected actual germ did not pass its domain gate')
        self.cell = tuple(map(Fraction, self.selected['common_span']))
        self.time_endpoints = tuple(map(exact_time, domain['exact_time_endpoints']))
        self.exact_tau0 = sum(self.time_endpoints, PiTime())/2
        self.exact_h = (self.time_endpoints[1]-self.time_endpoints[0])/2
        self.tau0, self.h = self.exact_tau0.ball(), self.exact_h.ball()
        self.outer = exact_arb(Fraction(domain['time_radius']))
        self.strip = exact_arb(Fraction(domain['physical_theta_strip']))
        self.modulus = arb(self.selected['true_field_moduli']['f']['upper']).upper()
        grid_row = descriptor['old_'+domain['leg']+'_reference']
        if sha(grid_row['path']) != grid_row['sha256']:
            raise ValueError('saved reference time-grid manifest identity differs')
        if domain.get('time_grid_manifest_sha256', grid_row['sha256']) != grid_row['sha256']:
            raise ValueError('domain was computed on a different reference time grid')
        grid = document(grid_row['path'])
        segment = int(domain['segment'])
        if not 0 <= segment < grid['segment_count']:
            raise ValueError('segment leaves the saved reference time grid')
        a, b = map(exact_time, grid['exact_time_endpoints'][segment:segment+2])
        sl, sr = map(Fraction, domain['normalized_subspan'])
        if not (0 <= sl < sr <= 1) or self.time_endpoints != (a+(b-a)*sl, a+(b-a)*sr):
            raise ValueError('actual rational/pi endpoint or exact subspan mismatch')
        self.sign = int(grid['trace_identity']['sign'])
        if self.sign not in (-1, 1) or domain.get('branch_sign', self.sign) != self.sign:
            raise ValueError('actual physical branch sign differs')
        self.nodes = int(nodes)
        self.R0, self.RE, self.sigma = map(exact_arb,
            (Fraction(3, 1000), Fraction(1, 400), Fraction(8, 25)))
        self.root_package = prepare_refined_root(self.object_path, self.root_path,
                                                nodes=nodes if root_nodes is None else root_nodes)
        self.root = self.root_package.root
        self.target = AffineBulkTarget(self.object_path, nodes, nodes, self.R0, self.RE, self.sigma)
        self.target.set_cell(*self.cell)
        self.target.fourier = NativeSeriesFFT()
        curvature = self.selected.get('curvature', {})
        self.turn = curvature.get('kind') == 'root_deflated_Q'
        self.mode = 'root_deflated_Q' if self.turn else 'ordinary_negative_K'
        self.endpoint_locations = []
        if self.turn:
            self.deflation = cached_deflation(self.object_path, self.root_package, nodes,
                self.R0, self.RE, self.sigma, curvature_radius, radial_degree)
            positive = self.deflation.positive_cell
            if self.cell == positive:
                self.side = 1
            elif self.cell == (-positive[1], -positive[0]):
                self.side = -1
            else:
                raise ValueError('turn curvature was applied to a non-root analytic germ')
            halfpi = PiTime(Fraction(0), Fraction(1, 2))
            eta_left, eta_right = [halfpi-self.side*x for x in self.time_endpoints]
            if not eta_left.nonnegative() or not eta_right.nonnegative():
                raise ValueError('the actual real time interval leaves the inner turn side')
            self.endpoint_locations = [u for u, eta in ((-1, eta_left), (1, eta_right)) if eta.is_zero()]
            self.exact_eta0, self.exact_eta1 = halfpi-self.side*self.exact_tau0, -self.side*self.exact_h
            self.eta0, self.eta1 = self.exact_eta0.ball(), self.exact_eta1.ball()
            self.budget_center = self.side*self.root*self.eta0.cos()
            H = abs(self.eta1)*self.outer
            self.radial_enlargement = (abs(self.root)*(abs(self.eta0.cos())*(H.cosh()-1)
                                                       +abs(self.eta0.sin())*H.sinh())).upper()
        else:
            if curvature.get('kind') not in (None, 'ordinary_negative_K', 'ordinary_negative_curvature'):
                raise ValueError('unknown curvature branch certificate')
            if not curvature and 'minus_K_real_lower' not in self.selected:
                raise ValueError('ordinary germ lacks its curvature branch certificate')
            self.budget_center = self.root*self.tau0.sin()
            H = abs(self.h)*self.outer
            self.radial_enlargement = (abs(self.root)*(abs(self.tau0.sin())*(H.cosh()-1)
                                                       +abs(self.tau0.cos())*H.sinh())).upper()
        self.center = self.budget_center
        self.common_budget = self.target.analytic_input_budget(acb(self.budget_center),
            self.R0+self.radial_enlargement, self.sigma, self.RE+self.radial_enlargement)
        def common_budget(radial, radial_radius, sigma, E_radius):
            if not (radial_radius is self.R0 and sigma is self.sigma and E_radius is self.RE):
                raise ValueError('the shared analytic majorant was requested at different radii')
            return dict(self.common_budget)
        self.target.analytic_input_budget = common_budget
        required = domain.get('required_common_spans', [row['common_span'] for row in domain['germs']])
        self.whole_real_interval_in_selected_germ = len(required) == 1 and tuple(map(Fraction, required[0])) == self.cell

    def sample(self, u, angles):
        """Enclose true physical f(c+h*u, pi*j/(2N)) of this one germ."""
        u = acb(u)
        if not abs(u).upper() < self.outer:
            raise ValueError('scalar time sample leaves the certified complex time disk')
        angles = int(angles)
        if angles < self.nodes or angles & (angles-1):
            raise ValueError('a power-of-two angle grid at least Q long is required')
        if self.turn and u.imag == 0 and u.real.is_exact():
            exact_u = Fraction(str(u.real.fmpq()))
            if (self.exact_eta0+self.exact_eta1*exact_u).is_zero():
                return [acb(0) for _ in range(angles)], dict(exact_turn_zero=True,
                    exact_time_endpoint=exact_u in self.endpoint_locations,
                    geometry_seconds=0.0, grid_seconds=0.0,
                    maximum_component_radius=ball_record(arb(0)))
        oldcap, ctx.cap = ctx.cap, 4
        before = time.monotonic()
        try:
            wave_report = None
            if self.turn:
                eta = acb(self.eta0)+self.eta1*u
                radial, r_tau = self.side*self.root*eta.cos(), self.root*eta.sin()
                wave, wave_report = self.deflation.evaluate(eta)
            else:
                tau = acb(self.tau0)+self.h*u
                radial, r_tau = self.root*tau.sin(), self.root*tau.cos()
            coefficient, K, _, budget = self.target.complete_data(radial)
            if not self.turn:
                if not (-K).real > 0:
                    raise ValueError('ordinary right-half-plane curvature branch is not separated')
                wave = (-K).sqrt(analytic=True)
            beta, gamma, _, _ = self.target.scalars(radial, 1)
            geometry_seconds = time.monotonic()-before
            before = time.monotonic()
            frequency_data = np.empty((angles, 9), object)
            frequency_data.fill(acb(0))
            for k, frequency in enumerate(self.target.frequency):
                if frequency % 4:
                    raise ValueError('unexpected physical primitive frequency')
                for c in range(3):
                    frequency_data[(frequency//4) % angles, c] = coefficient[k, c][1]
            for k, (b, g) in enumerate(zip(beta, gamma), 1):
                if k >= angles//2:
                    raise ValueError('finite phase modes exceed this grid')
                for sign in (-1, 1):
                    factor, row = acb(0, -sign)/2, (sign*k) % angles
                    frequency_data[row, 3:7] = [b[0]*factor, g[0]*factor, b[1]*factor, g[1]*factor]
                    frequency_data[row, 7] = b[0]*factor*acb(0, 4*sign*k)
                    frequency_data[row, 8] = g[0]*factor*acb(0, 4*sign*k)
            samples = self.target.fourier.fft(frequency_data, inverse=True)*angles
            errors, _ = primitive_fourier_budget(self.nodes, self.sigma, arb(0), self.R0,
                budget['radius_bound'], budget['height_bound'], budget['tangent_bound'])
            Xerror = (errors[0]/self.R0).upper()
            result, Dlower, maximum_radius = [], None, arb(0)
            for j in range(angles):
                X = [complex_pad(samples[j, c], Xerror) for c in range(3)]
                D, M, W = f_invariants(X, samples[j, 3:])
                lower = D.abs_lower()
                if not lower > 0:
                    raise ValueError('pointwise denominator enclosure contains zero')
                Dlower = lower if Dlower is None else min(Dlower, lower)
                value = -r_tau*(M+self.sign*wave*W)/D
                if not value.is_finite():
                    raise ValueError('nonfinite true scalar field sample')
                result.append(value)
                maximum_radius = max(maximum_radius, value.real.rad().upper(), value.imag.rad().upper())
            return result, dict(geometry_seconds=geometry_seconds, grid_seconds=time.monotonic()-before,
                sample_D_lower=ball_record(Dlower), primitive_derivative_fee=ball_record(Xerror),
                maximum_component_radius=ball_record(maximum_radius), turn_wave=wave_report)
        finally:
            ctx.cap = oldcap

    def identity(self):
        return dict(domain_path=str(self.domain_path), domain_sha256=sha(self.domain_path),
            descriptor_sha256=sha(self.descriptor_path), target_object_sha256=sha(self.object_path),
            target_root_sha256=sha(self.root_path), exact_delta_fraction=str(self.target.affine_delta),
            common_span=list(map(str, self.cell)), mode=self.mode, branch_sign=self.sign,
            exact_time_endpoints=[x.record() for x in self.time_endpoints],
            actual_time_outer_radius=self.domain['time_radius'],
            actual_physical_outer_strip=self.domain['physical_theta_strip'],
            actual_outer_modulus=ball_record(self.modulus),
            whole_real_interval_in_selected_germ=self.whole_real_interval_in_selected_germ,
            endpoint_locations=self.endpoint_locations, refined_root=self.root_package.provenance,
            radial_enlargement=ball_record(self.radial_enlargement),
            common_E_infinite_error=ball_record(self.common_budget['E_error']))


def run_pilot(args):
    ctx.prec, ctx.cap = args.bits, max(21, args.check_order+4)
    started, cpu = time.monotonic(), time.process_time()
    rows = []
    for domain_path in args.domain:
        before = time.monotonic()
        model = UnifiedScalarTimeCircleField(args.descriptor, domain_path,
            nodes=args.primitive_nodes, radial_degree=args.radial_degree)
        init_seconds = time.monotonic()-before
        if not model.turn:
            raise ValueError('the first pilot requires actual root-deflated domains')
        check = TurnCollarTimeModel(model.object_path, model.root_path, *model.time_endpoints,
            side=model.side, nodes=args.primitive_nodes, order=args.check_order,
            radial_degree=args.radial_degree, outer_radius=Fraction(model.domain['time_radius']),
            curvature_radius=Fraction(3, 1250), branch_sign=model.sign)
        indices = sorted({0, args.angles//7, args.angles//3, args.angles-1})
        checks = {}
        for j in indices:
            value, _ = check.time_field([acb(arb.pi()*j/(2*args.angles))])
            checks[j] = [value[0][i] for i in range(check.precision)]
        rho = exact_arb(Fraction(args.radius))
        time_points = [acb(rho), acb(0, rho),
                       rho*acb(0, arb.pi()/4).exp(), acb(-rho), acb(0, -rho)]
        samples = []
        for u in time_points:
            actual, timing = model.sample(u, args.angles)
            ratio = (abs(u)/model.outer).upper()
            tail = (model.modulus*ratio**check.precision/(1-ratio)).upper()
            comparisons = []
            for j in indices:
                expected = acb(0)
                for coefficient in checks[j][::-1]:
                    expected = coefficient+u*expected
                expected = complex_pad(expected, tail)
                passed = (actual[j].real.overlaps(expected.real)
                          and actual[j].imag.overlaps(expected.imag))
                if not passed:
                    raise ValueError('true scalar/Q sample disagrees with independent time jets')
                comparisons.append(dict(angle_node=j, overlap_after_true_time_tail=True,
                    scalar=complex_record(actual[j]), independent_time_jet=complex_record(expected)))
            samples.append(dict(u=complex_record(u), true_time_jet_tail=ball_record(tail),
                                checks=comparisons, **timing))
        endpoints = []
        for u in model.endpoint_locations:
            values, timing = model.sample(acb(u), args.angles)
            if any(value != 0 for value in values):
                raise ValueError('the exact physical turning endpoint failed exact zero')
            endpoints.append(dict(normalized_time=u, every_angle_exactly_zero=True, **timing))
        rows.append(dict(**model.identity(), init_seconds=init_seconds,
            samples=samples, exact_endpoint_checks=endpoints,
            radial_deflation_domain=model.deflation.domain))
        print(json.dumps(dict(domain=str(domain_path), mode=model.mode, passed=True,
                              elapsed_seconds=time.monotonic()-started)), flush=True)
    report = dict(kind='actual_turn_scalar_time_circle_independent_jet_checks', complete=True,
        source_sha256=sha(__file__), bits=args.bits, primitive_nodes=args.primitive_nodes,
        angles=args.angles, radial_degree=args.radial_degree,
        independent_time_order=args.check_order, time_circle_radius=args.radius,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in
            ['fourfold_phase_field_time_turn_collar.py', 'fourfold_phase_field_time_refined_root.py',
             'fourfold_phase_beta_affine.py', 'fourfold_phase_beta_bulk_interval.py',
             'fourfold_phase_beta_interval.py', 'fourfold_phase_uniform_field_time_grid_fast.py',
             'fourfold_native_series_fft.py']},
        domains=rows, total_seconds=time.monotonic()-started, total_cpu_seconds=time.process_time()-cpu,
        limitations=['True samples and independent node comparisons only; no finite P package or full residual is asserted.',
            'A selected analytic germ remains distinct from any neighboring true spline germ.',
            'No actual return/conjugacy/parameter derivative certificate is inferred from this pilot.'])
    write_report(args.out, report)
    print(json.dumps(dict(complete=True, total_seconds=report['total_seconds'],
                         total_cpu_seconds=report['total_cpu_seconds'])), flush=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--descriptor', type=Path, default=Path('data/phase_ring_continuation/step5_retargeted_reference/descriptor.json'))
    p.add_argument('--domain', type=Path, action='append', required=True)
    p.add_argument('--primitive-nodes', type=int, default=512)
    p.add_argument('--angles', type=int, default=512)
    p.add_argument('--radial-degree', type=int, default=64)
    p.add_argument('--check-order', type=int, default=64)
    p.add_argument('--radius', default='5/4')
    p.add_argument('--bits', type=int, default=256)
    p.add_argument('--out', type=Path, required=True)
    run_pilot(p.parse_args())


if __name__ == '__main__':
    main()
