#!/usr/bin/env python3
"""R164: continuous positive-n lower bounds for an immutable saved coast.

The complete defining field is raw P1 + (1-w)*plain tail + w*R139.
On this coast the seed and disjoint terminal trace weight vanish. The
positive Bernstein plain-tail n is nonnegative, so it can be discarded.
Only saved binary Fourier coefficients, the original R139 inlet/chart,
and the frozen coast window enter the interval arithmetic. No profile
ODE, angular inverse, BVP, full residual, or Jacobian is evaluated.

The output includes every covering box and unresolved box. A successful
report certifies this saved input only; a nonpositive lower enclosure is
not a negative-value witness. Binary endpoints, not short displays, carry
the inequalities. The defining original providers are never modified.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
import numpy as np
import flint
from flint import arb, ctx
from fd2d_gc_archive_arrays import identity, load_npz
from fd2d_gc_positive_trace_native_field_v2 import PositiveTraceNativeField
from fd2d_k0_ruling_angular_certificate import moment, bounds

HERE = Path(__file__).resolve().parent
NOTES = HERE.parent/'notes'
SCHEMA = 'fd2d-fixed-raw-P1-ruling-coast-positive-n-Arb-v1'


def aq(value):
    q = F(value)
    return arb(q.numerator)/q.denominator


def fraction_row(value):
    q = F(value)
    return [str(q.numerator), str(q.denominator)]


def square(x):
    # Explicit nonnegative square; never use generic real powers on a
    # ball that contains zero.
    if x >= 0 or x <= 0:
        return x*x
    end = abs(x).upper()
    return arb(0).union(end*end)


def step5_exact(t):
    t = min(F(1), max(F(0), F(t)))
    return t*t*t*(10-15*t+6*t*t)


class CoastPositiveNConsumer:
    """Reusable exact-function consumer; fields may use either K layout.

    Native construction checks saved provider/schema/source identities;
    it is not used to infer positivity from numerical point evaluation.
    """
    def __init__(self, field, candidate, inlet, ruling_proof):
        self.paths = dict(field=Path(field), candidate=Path(candidate),
                          inlet=Path(inlet), ruling_proof=Path(ruling_proof))
        saved = load_npz(field)
        kind = str(saved['representation_kind'])
        if kind == 'ruling_atlas_coast_Gauss_l_terminal_positive_trace_fixed_tail_degree_v1':
            from fd2d_gc_independent_tail_native_field import IndependentTailPositiveTraceNativeField
            cls = IndependentTailPositiveTraceNativeField
        else:
            cls = PositiveTraceNativeField
        reader = cls(field, candidate, reference_inlet=inlet)
        self.reader = reader
        self.saved = saved
        self.mesh = [F(float(v)) for v in saved['mesh']]
        self.K = int(reader.K)
        self.raw = [[arb(float(v)) for v in row[:self.K+1]] for row in saved['corrections']]
        if self.K < 1 or not np.array_equal(reader.frequencies, 2*np.arange(self.K+1)):
            raise ValueError('Expected the saved real cos(2*j*xi) n basis')
        ref = reader.coast_reference
        self.entry, self.exit = F(ref.entry_s), F(ref.exit_s)
        self.length = F(ref.length)
        # This rounded scalar is the actual original provider constant.
        self.rim = F(float(ref.length*reader.reference_rim_fraction))
        if not self.entry < self.exit or not 0 < self.rim < (self.exit-self.entry)/2:
            raise ValueError('No positive coast plateau')
        if reader.seed_weight_definition['end'] > float(self.entry):
            raise ValueError('The omitted seed has not vanished on the whole coast')
        terminal = json.loads(str(saved['positive_trace_definition']))
        if F(terminal['start']) < self.exit:
            raise ValueError('The terminal trace changes n on this coast')
        if reader.tail_kind != 'positive_bernstein':
            raise ValueError('The omitted tail must use the declared positive Bernstein family')
        tail = np.asarray(reader.parameters[reader.tail_parameter_slice], float)
        if np.any(tail < 0) or not np.all(np.isfinite(tail)):
            raise ValueError('A negative tail control invalidates the nonnegative-tail omission')
        self.tail_minimum = F(float(np.min(tail)))
        atlas = reader.angular_atlas_definition
        if atlas.get('coast_formula') != 'Frozen R139 ruling map, label xi is fixed inlet seed-normal angle':
            raise ValueError('Only the declared ruling-label coast chart is supported')
        if atlas.get('coast') != [float(self.entry), float(self.exit)]:
            raise ValueError('Coast support and chart disagree')
        data = np.load(inlet, allow_pickle=False)
        self.a, self.v = (arb(float(data[k])) for k in ('a', 'v'))
        self.rho0 = self.a/self.v
        self.nc = [arb(float(v)) for v in data['n_phi_cos']]
        self.mc = [arb(float(v)) for v in data['m_phi_sin']]
        self.freq = [int(v) for v in data['frequencies']]
        if self.freq != list(range(0, 2*len(self.nc), 2)) or len(self.mc) != len(self.nc)-1:
            raise ValueError('The immutable inlet must have the exact D2 real basis')
        proof = json.loads(Path(ruling_proof).read_text())
        mompath = ref.geometry.moments_path
        if (not proof.get('passed') or proof.get('unresolved')
                or proof['inlet_sha256'] != identity(inlet)['sha256']
                or proof['candidate_sha256'] != identity(candidate)['sha256']
                or proof['moments_sha256'] != identity(mompath)['sha256']):
            raise ValueError('The old full-ruling certificate is not for these functions')
        self.paths.update(moments=Path(mompath))
        self.old_boxes = proof['boxes']
        mom = json.loads(Path(mompath).read_text())
        par = mom['parameters']
        self.a0 = moment(mom['enclosures']['a0'])
        self.adjust = {k: moment(mom['enclosures'][k]) for k in ('u0', 'u2', 'u4')}
        self.seed_r, self.seed_D, self.seed_c, self.seed_k = (arb(par[k]) for k in ('r', 'D', 'c', 'k'))
        self._angular_cache = {}
        self._radial_cache = {}
        self.proof = proof
        self.definition = dict(
            exact_input_coefficient_semantics='Each saved binary64 is its exact dyadic rational; no fitting or field reset.',
            complete_field_identity='n = raw_P1 + (1-w)*eta*kappa(a_delta(s)*sin(U))*cos(U)^2 + w*n_ref',
            lower_function='raw_P1 + w*n_ref',
            seed_zero_on_closed_coast=True, terminal_trace_zero_on_closed_coast=True,
            tail_parameter_minimum_exact=fraction_row(self.tail_minimum),
            tail_nonnegative_reason='eta>=0, nonnegative Bernstein controls, clipped kappa>=0, and cos(U)^2>=0',
            physical_profile_and_material_inverse_not_evaluated=True,
            physical_target_GC_solution_inferred=False,
            original_coast_definition=reader.coast_reference_definition,
            actual_rim_exact=fraction_row(self.rim),
            endpoint_minus_entry_minus_stored_length_exact=fraction_row(self.exit-self.entry-self.length),
            endpoint_rounding_handling='Enclose the union of sigma=s-entry over the whole stored support and the stored endpoint sigma=L. At exit the multiplying coast weight is exactly zero.',
            angular_symmetry='Both n_raw and n_ref are even and pi-periodic; [0,pi/2] covers the complete circle by exact D2 reflection.',
            original_atlas_source_sha256=atlas['source_sha256'],
            original_reference_binding_sha256=ref.binding_sha256,
            frozen_full_physical_parameter_sha256=hashlib.sha256(np.ascontiguousarray(saved['parameters']).tobytes()).hexdigest(),
            original_schema=kind, angular_modes=self.K,
            no_inference_for_later_accepted_fields=True)

    def radial_segments(self):
        result = []
        breakpoints = (self.entry, self.entry+self.rim, self.exit-self.rim, self.exit)
        for j, (left, right) in enumerate(zip(self.mesh, self.mesh[1:])):
            a, b = max(left, self.entry), min(right, self.exit)
            if a >= b:
                continue
            points = sorted(set([a, b]+[p for p in breakpoints if a < p < b]))
            result.extend((j, u, v) for u, v in zip(points, points[1:]))
        if (not result or result[0][1] != self.entry or result[-1][2] != self.exit
                or any(a[2] != b[1] for a, b in zip(result, result[1:]))):
            raise ValueError('The actual P1 mesh does not cover the complete reference support')
        return result

    def angular(self, lo, hi):
        key = (lo, hi)
        if key in self._angular_cache:
            return self._angular_cache[key]
        phi = (arb.pi()*aq(lo)/2).union(arb.pi()*aq(hi)/2)
        trig = [(arb(0), arb(1))]+[(phi*f).sin_cos() for f in self.freq[1:]]
        nc, mc, np1, mp1 = self.nc[0], arb(0), arb(0), arb(0)
        for j, f in enumerate(self.freq[1:], 1):
            sn, cs = trig[j]
            nc += self.nc[j]*cs; mc += self.mc[j-1]*sn
            np1 -= f*self.nc[j]*sn; mp1 += f*self.mc[j-1]*cs
        c2, c4 = (2*phi).cos(), (4*phi).cos()
        rho = (self.seed_r+self.seed_D*(1-(self.seed_k*(c2-self.seed_c)).tanh())/2
               +self.adjust['u0']+self.adjust['u2']*c2+self.adjust['u4']*c4)
        h = rho/self.a0
        if not (nc > 0 and h > 0):
            answer = dict(valid=False, reason='inlet n or chart h interval contains zero')
        else:
            k = mc/nc; k2 = square(k)
            ku = (mp1*nc-mc*np1)/(h*nc*nc)
            answer = dict(valid=True, nc=nc, k2=k2, B=self.v*(1+k2)-ku,
                          cos=[(phi*(2*j)).cos() for j in range(self.K+1)])
        # A small bounded cache, not a sample-derived function definition.
        if len(self._angular_cache) >= 8192:
            self._angular_cache.clear()
        self._angular_cache[key] = answer
        return answer

    def _raw_endpoint(self, cell, s, cosine):
        left, right = self.mesh[cell], self.mesh[cell+1]
        theta = aq((s-left)/(right-left))
        return sum(((self.raw[cell][j]+theta*(self.raw[cell+1][j]-self.raw[cell][j]))*c
                    for j, c in enumerate(cosine)), arb(0))

    def _weight(self, s):
        return step5_exact((s-self.entry)/self.rim)*step5_exact((self.exit-s)/self.rim)

    def evaluate(self, cell, s0, s1, phi0, phi1):
        angular = self.angular(phi0, phi1)
        if not angular['valid']:
            return dict(valid=False, reason=angular['reason'])
        raw = self._raw_endpoint(cell, s0, angular['cos']).union(
            self._raw_endpoint(cell, s1, angular['cos']))
        weights = (self._weight(s0), self._weight(s1))
        weight = aq(min(weights)).union(aq(max(weights)))
        sigma0, sigma1 = s0-self.entry, s1-self.entry
        if s1 == self.exit:
            sigma1 = max(sigma1, self.length)
        k2, B = angular['k2'], angular['B']
        def endpoint(sigma):
            ss = aq(sigma)
            A = ss*(2*self.rho0+ss)
            Q = (self.rho0*self.rho0+(1+k2)*A).sqrt()
            ruling_w = A/(self.rho0+Q)
            D = self.a+ruling_w*B
            factor = 1+k2*A/((self.rho0+ss)*(self.rho0+ss))
            return D, factor
        d0, f0 = endpoint(sigma0); d1, f1 = endpoint(sigma1)
        # For every fixed angle, ruling_w and A/rho^2 increase in sigma;
        # D is affine in ruling_w. Endpoint hulls cover all radial values.
        D = d0.union(d1); factor = f0.union(f1)
        if not (D > 0 and factor > 0):
            return dict(valid=False, reason='local reference denominator enclosure contains zero',
                        raw=raw, weight=weight, D=D)
        reference = self.a*angular['nc']*factor/D
        lower_function = raw+weight*reference
        if not all(q.is_finite() for q in (raw, weight, D, reference, lower_function)):
            return dict(valid=False, reason='nonfinite Arb interval')
        return dict(valid=True, lower_function=lower_function, raw=raw,
                    weight=weight, reference=reference, D=D)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--field', type=Path, required=True)
    p.add_argument('--candidate', type=Path, required=True)
    p.add_argument('--inlet', type=Path, default=NOTES/'2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz')
    p.add_argument('--ruling-proof', type=Path, default=NOTES/'2026-11-12-fd2d-k0-ruling-angular-certificate-01.json')
    p.add_argument('--out-stem', type=Path, required=True)
    p.add_argument('--precision', type=int, default=160)
    p.add_argument('--maximum-angle-depth', type=int, default=3)
    p.add_argument('--maximum-radial-depth', type=int, default=3)
    p.add_argument('--maximum-evaluations', type=int, default=16000)
    a = p.parse_args()
    report_path = a.out_stem.with_name(a.out_stem.name+'-report.json')
    boxes_path = a.out_stem.with_name(a.out_stem.name+'-boxes.json.gz')
    if report_path.exists() or boxes_path.exists():
        raise FileExistsError('Use a new immutable report stem')
    ctx.prec = a.precision
    begun = time.perf_counter()
    consumer = CoastPositiveNConsumer(a.field, a.candidate, a.inlet, a.ruling_proof)
    accepted, unresolved = [], []
    evaluations = 0
    def visit(cell, s0, s1, p0, p1, sd, ad):
        nonlocal evaluations
        record = dict(old_cell=cell, s_left_exact=fraction_row(s0), s_right_exact=fraction_row(s1),
                      angle_left_pi_over_two=fraction_row(p0), angle_right_pi_over_two=fraction_row(p1),
                      radial_depth=sd, angular_depth=ad)
        if evaluations >= a.maximum_evaluations:
            record['reason'] = 'declared finite interval-evaluation budget exhausted'
            unresolved.append(record); return
        evaluations += 1
        value = consumer.evaluate(cell, s0, s1, p0, p1)
        for name in ('lower_function', 'raw', 'weight', 'reference', 'D'):
            if name in value:
                record[name] = bounds(value[name])
        if value['valid'] and value['lower_function'] > 0:
            accepted.append(record); return
        record['reason'] = value.get('reason', 'strict positivity not proved by this box')
        can_s = sd < a.maximum_radial_depth
        can_a = ad < a.maximum_angle_depth
        if not can_s and not can_a:
            unresolved.append(record); return
        # The original 209 angular boxes are already small. Start with
        # radial splitting, then alternate; both limits are explicit.
        if can_s and (not can_a or sd <= ad):
            middle = (s0+s1)/2
            visit(cell, s0, middle, p0, p1, sd+1, ad)
            visit(cell, middle, s1, p0, p1, sd+1, ad)
        else:
            middle = (p0+p1)/2
            visit(cell, s0, s1, p0, middle, sd, ad+1)
            visit(cell, s0, s1, middle, p1, sd, ad+1)
    radial = consumer.radial_segments()
    angles = []
    for box in consumer.old_boxes:
        lo = F(*map(int, box['left_pi_over_two']))
        hi = F(*map(int, box['right_pi_over_two']))
        angles.append((lo, hi))
    angles.sort()
    if (angles[0][0] != 0 or angles[-1][1] != 1
            or any(left[1] != right[0] for left, right in zip(angles, angles[1:]))):
        raise ValueError('Original angular certificate does not form the declared complete partition')
    for cell, s0, s1 in radial:
        for p0, p1 in angles:
            visit(cell, s0, s1, p0, p1, 0, 0)
    payload = dict(schema=SCHEMA, accepted=accepted, unresolved=unresolved)
    with gzip.open(boxes_path, 'wt', encoding='utf-8') as handle:
        json.dump(payload, handle, separators=(',', ':'), allow_nan=False)
        handle.write('\n')
    minimum = None
    if accepted:
        def lower(row):
            m, e = row['lower_function']['lower_binary']
            return F(int(m))*F(2)**int(e)
        minimum = min(accepted, key=lower)
    sources = ['fd2d_coast_positive_n_certificate.py', 'fd2d_k0_ruling_angular_certificate.py',
               'fd2d_gc_positive_trace_native_field_v2.py', 'fd2d_gc_ruling_atlas_native_field.py',
               'fd2d_gc_frozen_ruling_atlas.py', 'fd2d_gc_frozen_coast_reference.py',
               'fd2d_k0_native_gc.py', 'fd2d_gc_raw_bump_coast_reference.py',
               'fd2d_gc_archive_arrays.py']
    report = dict(schema=SCHEMA, actual_execution=True, inputs={k: identity(v) for k, v in consumer.paths.items()},
                  sources={name: identity(HERE/name) for name in sources},
                  precision_bits=ctx.prec, flint_version=flint.__version__, definition=consumer.definition,
                  radial_support_exact=[fraction_row(consumer.entry), fraction_row(consumer.exit)],
                  initial_radial_segments=len(radial), original_angular_boxes=len(angles),
                  interval_evaluations=evaluations, accepted_boxes=len(accepted), unresolved_boxes=len(unresolved),
                  maximum_radial_depth=a.maximum_radial_depth, maximum_angle_depth=a.maximum_angle_depth,
                  maximum_evaluations=a.maximum_evaluations,
                  passed=not unresolved, minimum_accepted_box=minimum,
                  accepted_only_lower_is_not_global_if_unresolved=True,
                  unresolved_old_cells=sorted(set(r['old_cell'] for r in unresolved)),
                  unresolved_examples=unresolved[:12], boxes=identity(boxes_path),
                  coverage='The full stored closed coast times [0,pi/2], and the complete angle circle by exact D2 symmetry.',
                  exact_unmodified_input_only=True, samples_used_for_certificate=False,
                  no_BVP=True, no_whole_residual=True, no_Jacobian=True, no_body=True,
                  no_frozen_reference_GC_transfer_to_modified_target_metric=True,
                  strict_bounds_in_binary_fields=True, short_displays_not_outward_rounded=True,
                  seconds=time.perf_counter()-begun,
                  peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    report_path.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps({k: report[k] for k in ('passed', 'accepted_boxes', 'unresolved_boxes',
                     'unresolved_old_cells', 'interval_evaluations', 'seconds', 'peak_rss_kib')}))
    if minimum is not None:
        print(json.dumps(dict(minimum_accepted_lower_display=minimum['lower_function']['lower_display'],
                              minimum_accepted_cell=minimum['old_cell'])))


if __name__ == '__main__':
    main()
