#!/usr/bin/env python3
"""R646 verified comparison of the SAME actual R631 macro core.

No new Fourier projection, fitting, connection solve or private computation.
This consumer is called only after an actual completed mu=1 checkpoint is
available. A partial result contains its paid constants, angular primitives
and exact remaining interval stack; it is not a completed certificate.

API: compare_actual_core(checkpoint, origin, ...). The caller binds the
completed source checkpoint and, for a resume, the exact returned state hash.
All scientific arithmetic is restricted to public repository Actions.
"""
from collections import defaultdict
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import time


SCHEMA = 'r646-same-actual-R631-macro-core-composition-ball-v1'
THRESHOLD = Fraction(1, 50000)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def sha(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def public_only():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY', '').lower() != 'rogerhu12/math-research-public'
            or not os.environ.get('GITHUB_RUN_ID')):
        raise RuntimeError('verified scientific arithmetic belongs to the declared public Actions')


class UnclosedCell(Exception):
    pass


class ClockCheckpoint(Exception):
    pass


class ActualCoreComparison:
    def __init__(self, checkpoint, origin, *, precision_bits, order, maximum_depth,
                 budget_seconds, resume, resume_sha256):
        public_only()
        import flint
        self.arb, self.acb, self.ctx = flint.arb, flint.acb, flint.ctx
        if (type(precision_bits) is not int or not 128 <= precision_bits <= 4096
                or type(order) is not int or not 2 <= order <= 16
                or type(maximum_depth) is not int or not 1 <= maximum_depth <= 60
                or not 0 < budget_seconds <= 3300):
            raise ValueError('finite declared verification range required')
        self.ctx.prec = precision_bits
        self.precision, self.N, self.maximum_depth = precision_bits, order, maximum_depth
        self.started = time.monotonic()
        self.deadline = self.started + float(budget_seconds)
        self.counts = defaultdict(int)
        self.prior_costs = None
        self.source_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        if (origin.get('source_run_naturally_completed') is not True
                or type(origin.get('run_id')) is not int
                or origin.get('checkpoint_sha256') != sha(checkpoint)
                or len(origin.get('source_commit', '')) != 40
                or len(origin.get('FINAL_JSON_sha256', '')) != 64
                or Fraction(checkpoint['mu_literal']) != 1):
            raise ValueError('one actual completed mu=1 source and unchanged checkpoint required')
        j = checkpoint['maximum_independent_mode']
        coefficients = checkpoint['actual_prescribed_total_P0']
        if (type(j) is not int or j < 2 or j % 2
                or len(coefficients) != j // 2
                or not all(type(c) is float and math.isfinite(c) for c in coefficients)
                or len(checkpoint['actual_q_sha256']) != 64):
            raise ValueError('every actual binary64 positive even-mode coefficient required')
        core = checkpoint['actual_core_input']
        if (core.get('schema') != 'actual-new-R080-to-R631-canonical-convex-core-input-v1'
                or Fraction(core['mu_literal']) != 1
                or core.get('mu_rational') != [1, 1]
                or core.get('maximum_independent_mode') != j
                or core.get('retained_modes') != list(range(2, j+1, 2))
                or core.get('P0_coefficients') != coefficients):
            raise ValueError('the actual coefficients must belong to this same R631 macro input')
        self.input = {'schema': SCHEMA, 'origin': origin,
            'same_actual_q_sha256': checkpoint['actual_q_sha256'],
            'same_actual_P0': coefficients, 'maximum_independent_mode': j,
            'fixed_exact_R_epsilon_A_B': ['4/5', '1/20', '1', '37/100'],
            'exact_threshold': str(THRESHOLD)}
        self.input_sha = sha(self.input)
        self.coefficients = [self.ball(Fraction.from_float(c)) for c in coefficients]
        self.L, self.R, self.eps = self.arb.pi() / 2, self.ball(Fraction(4, 5)), self.ball(Fraction(1, 20))
        self.closed = Fraction(0)
        self.closed_bound = Fraction(0)
        self.closed_count = 0
        self.frontier = []
        self.constants_ready = False
        self.witness = None
        self.last_failure = None
        self.flint_version = flint.__version__
        if resume is not None:
            if (resume_sha256 != sha(resume) or resume.get('input_sha256') != self.input_sha
                    or resume.get('source_sha256') != self.source_sha
                    or resume.get('precision_bits') != self.precision
                    or resume.get('Taylor_order') != self.N
                    or resume.get('maximum_depth') != self.maximum_depth
                    or type(resume.get('constants_ready')) is not bool):
                raise ValueError('only an exact same-source paid partial state can be resumed')
            self.prior_costs = resume['costs']
            self.closed = Fraction(resume['closed_prefix_endpoint'])
            self.closed_bound = Fraction(resume['closed_prefix_maximum_bound'])
            self.closed_count = resume['closed_leaf_count']
            self.frontier = json.loads(json.dumps(resume['remaining_actual_interval_stack']))
            for name, value in resume['paid_constant_balls'].items():
                if name not in ('Leps', 'r0', 'p', 'q', 'e_star'):
                    raise ValueError('unexpected paid constant in the same-source partial state')
                setattr(self, name, self.unpack(value))
            self.constants_ready = resume['constants_ready']
            if self.constants_ready:
                if not all(hasattr(self, name) for name in ('Leps', 'r0', 'p', 'q', 'e_star')):
                    raise ValueError('a ready state must retain every completed constant enclosure')
                self.validate_partition()
            elif self.frontier or self.closed or self.closed_count or self.closed_bound:
                raise ValueError('no interval can be paid before the fixed constants are ready')

    def check(self):
        public_only()
        if time.monotonic() >= self.deadline:
            raise ClockCheckpoint('save actual remaining verification work')

    def ball(self, value):
        value = Fraction(value)
        return self.arb(str(value))

    def interval(self, lo, hi):
        lo, hi = Fraction(lo), Fraction(hi)
        if lo > hi:
            raise ValueError('invalid exact interval')
        return self.arb(str((lo + hi) / 2), str((hi - lo) / 2))

    def pack(self, value):
        if not value.is_finite():
            raise UnclosedCell('a non-finite ball has no paid enclosure')
        return [str(value.lower().fmpq()), str(value.upper().fmpq())]

    def unpack(self, value):
        return self.interval(*value)

    @staticmethod
    def rational_upper(value):
        if not value.is_finite():
            raise UnclosedCell('finite absolute derivative enclosure not obtained')
        return Fraction(str(value.abs_upper().fmpq()))

    def multiply(self, a, b):
        self.check()
        self.counts['jet_convolutions'] += 1
        return [sum((a[k] * b[n-k] for k in range(n+1)), self.arb(0))
                for n in range(self.N+1)]

    def reciprocal(self, a):
        if a[0].contains(0):
            raise UnclosedCell('jet denominator is not separated from zero')
        out = [1 / a[0]]
        for n in range(1, self.N+1):
            self.check()
            out.append(-sum((a[k]*out[n-k] for k in range(1, n+1)), self.arb(0))/a[0])
        self.counts['jet_reciprocals'] += 1
        return out

    def square_root(self, a):
        if not a[0].is_finite() or not a[0].lower().fmpq() > 0:
            raise UnclosedCell('positive real square-root jet not enclosed on this cell')
        out = [a[0].sqrt()]
        for n in range(1, self.N+1):
            self.check()
            out.append((a[n]-sum((out[k]*out[n-k] for k in range(1, n)),
                                 self.arb(0)))/(2*out[0]))
        self.counts['jet_positive_square_roots'] += 1
        return out

    def sin_cos(self, a):
        sine, cosine = [a[0].sin()], [a[0].cos()]
        for n in range(1, self.N+1):
            self.check()
            sine.append(sum((k*a[k]*cosine[n-k] for k in range(1, n+1)), self.arb(0))/n)
            cosine.append(-sum((k*a[k]*sine[n-k] for k in range(1, n+1)), self.arb(0))/n)
        self.counts['jet_trigonometric_pairs'] += 1
        return sine, cosine

    def rho_jet(self, x):
        phase = [self.L*x, self.L] + [self.arb(0) for _ in range(self.N-1)]
        sine, cosine = self.sin_cos(phase)
        ss, cc = self.multiply(sine, sine), self.multiply(cosine, cosine)
        v = [c+self.eps**2*s for c, s in zip(cc, ss)]
        w = [-v0 for v0 in v]
        w[0] += 1+self.eps**2
        iv = self.reciprocal(self.square_root(v))
        iw = self.reciprocal(self.square_root(w))
        iv3 = self.multiply(self.multiply(iv, iv), iv)
        iw3 = self.multiply(self.multiply(iw, iw), iw)
        result = [self.eps**2*(self.p*a+self.q*b) for a, b in zip(iv3, iw3)]
        result[0] += self.r0
        self.counts['complete_rho_jets'] += 1
        return result

    def rho_complex(self, x, analytic):
        phase = self.L*x
        sine, cosine = phase.sin_cos()
        v = cosine*cosine+self.eps**2*sine*sine
        w = 1+self.eps**2-v
        # The requested analytic check applies to BOTH square-root branches.
        sv, sw = v.sqrt(analytic=analytic), w.sqrt(analytic=analytic)
        return self.eps**2*(self.p/(sv**3)+self.q/(sw**3))+self.r0

    def integral(self, kind, a, b):
        self.check()
        def callback(x, analytic):
            self.check()
            self.counts['verified_quadrature_callbacks'] += 1
            if kind == 'support':
                phase = self.L*x
                sine, cosine = phase.sin_cos()
                value = (cosine*cosine+self.eps**2*sine*sine).sqrt(analytic=analytic)
            else:
                value = self.rho_complex(x, analytic)
                if kind == 'rho_cube':
                    value = value**3
            if not value.is_finite():
                self.counts['quadrature_nonfinite_analytic_or_denominator_balls'] += 1
            return value
        self.counts['verified_integrals_attempted'] += 1
        result = self.acb.integral(callback, self.acb(self.ball(a)), self.acb(self.ball(b)),
            abs_tol=1e-30, rel_tol=1e-30, eval_limit=100000, depth_limit=100)
        if not result.is_finite() or not result.imag.contains(0):
            raise UnclosedCell('this actual real-path integral was not enclosed')
        self.counts['verified_integrals_completed'] += 1
        return result.real

    def initialize(self):
        if not hasattr(self, 'Leps'):
            self.Leps = 4*self.L*self.integral('support', Fraction(0), Fraction(1))
        else:
            self.counts['paid_support_integral_reused'] += 1
        c = self.Leps/(1+self.eps)
        if not hasattr(self, 'r0'):
            self.r0 = (c*self.ball(Fraction(137, 100))-4*self.L*self.R)/(2*c-4*self.L)
        if not hasattr(self, 'p'):
            self.p = (1-self.r0-self.eps*(self.ball(Fraction(37, 100))-self.r0))/(1-self.eps**2)
        if not hasattr(self, 'q'):
            self.q = (self.ball(Fraction(37, 100))-self.r0-self.eps*(1-self.r0))/(1-self.eps**2)
        if (not Fraction(str(self.r0.lower().fmpq())) > Fraction(7, 50)
                or not Fraction(str(self.r0.upper().fmpq())) < Fraction(27, 100)
                or not self.p.lower().fmpq() > 0 or not self.q.lower().fmpq() > 0):
            raise UnclosedCell('the fixed positive R631 constants were not enclosed sharply enough')
        if not hasattr(self, 'e_star'):
            self.e_star = self.integral('rho_cube', Fraction(0), Fraction(1))/self.R**3
        else:
            self.counts['paid_cubic_rho_integral_reused'] += 1
        self.constants_ready = True
        self.frontier = [self.cell(Fraction(0), Fraction(1), self.arb(0), self.L, 0)]

    def cell(self, a, b, theta_a, theta_b, depth):
        return {'a': str(a), 'b': str(b), 'Theta_a': self.pack(theta_a),
                'Theta_b': self.pack(theta_b), 'depth': depth}

    def composition_jet(self, x, theta):
        rho = self.rho_jet(x)
        angle = [theta] + [self.L*rho[k-1]/(self.R*k) for k in range(1, self.N+1)]
        result = [self.arb(0) for _ in range(self.N+1)]
        for index, coefficient in enumerate(self.coefficients):
            self.check()
            mode = 2*(index+1)
            _, cosjet = self.sin_cos([mode*v for v in angle])
            for k in range(self.N+1):
                result[k] += coefficient*cosjet[k]
        rho2 = self.multiply(rho, rho)
        result = [a-b/(2*self.R**2) for a, b in zip(result, rho2)]
        result[0] += self.e_star/2
        self.counts['whole_difference_jets_completed'] += 1
        return result

    def validate_partition(self):
        if (not 0 <= self.closed <= 1 or not 0 <= self.closed_bound <= THRESHOLD
                or type(self.closed_count) is not int or self.closed_count < 0):
            raise ValueError('the actual paid prefix is invalid')
        last = self.closed
        for item in reversed(self.frontier):
            a, b = Fraction(item['a']), Fraction(item['b'])
            if a != last or not a < b <= 1:
                raise ValueError('the exact remaining stack does not partition the unpaid suffix')
            last = b
        if last != 1:
            raise ValueError('part of the real interval was omitted')

    def run(self):
        active = None
        status = 'unresolved_actual_intervals'
        try:
            if not self.constants_ready:
                self.initialize()
            self.validate_partition()
            while self.frontier:
                self.check()
                active = self.frontier.pop()
                a, b = Fraction(active['a']), Fraction(active['b'])
                if a != self.closed:
                    raise ValueError('only the leftmost unpaid interval may be processed')
                m, h = (a+b)/2, (b-a)/2
                if 'Theta_mid' not in active:
                    theta_m = self.unpack(active['Theta_a'])+self.L/self.R*self.integral('rho', a, m)
                    active['Theta_mid'] = self.pack(theta_m)
                else:
                    theta_m = self.unpack(active['Theta_mid'])
                    self.counts['paid_actual_midpoint_primitives_reused'] += 1
                if 'point_difference_jet' not in active:
                    center = self.composition_jet(self.ball(m), theta_m)
                    active['point_difference_jet'] = [self.pack(v) for v in center]
                else:
                    center = [self.unpack(v) for v in active['point_difference_jet']]
                    if len(center) != self.N+1:
                        raise ValueError('the retained whole point jet has a different order')
                    self.counts['paid_actual_point_difference_jets_reused'] += 1
                if (center[0].is_finite()
                        and Fraction(str(center[0].abs_lower().fmpq())) > THRESHOLD):
                    self.witness = {'normal_angle_over_pi_half': str(m),
                        'actual_difference_ball': self.pack(center[0]),
                        'comparison_threshold_violated_not_geometric_impossibility': True}
                    status = 'actual_core_comparison_threshold_violated'
                    break
                bound = None
                try:
                    theta_I = self.interval(active['Theta_a'][0], active['Theta_b'][1])
                    whole = self.composition_jet(self.interval(a, b), theta_I)
                    bound = sum((self.rational_upper(center[k])*h**k for k in range(self.N)), Fraction(0))
                    bound += self.rational_upper(whole[self.N])*h**self.N
                except UnclosedCell:
                    self.counts['interval_jet_domains_requiring_subdivision'] += 1
                self.counts['actual_cells_attempted'] += 1
                if bound is not None and bound <= THRESHOLD:
                    self.closed, self.closed_bound = b, max(self.closed_bound, bound)
                    self.closed_count += 1
                    self.counts['new_whole_closed_cells'] += 1
                    active = None
                    continue
                if active['depth'] >= self.maximum_depth:
                    status = 'declared_depth_with_actual_interval_unresolved'
                    break
                depth = active['depth']+1
                right = self.cell(m, b, theta_m, self.unpack(active['Theta_b']), depth)
                left = self.cell(a, m, self.unpack(active['Theta_a']), theta_m, depth)
                self.frontier.extend([right, left])
                self.counts['actual_bisections'] += 1
                active = None
            else:
                status = 'whole_actual_P_error_at_most_one_over_50000'
        except ClockCheckpoint as exc:
            status = 'actual_public_clock_checkpoint_not_a_certificate'
            self.last_failure = {'type': type(exc).__name__, 'message': str(exc)}
        except Exception as exc:
            status = 'actual_unclosed_arithmetic_or_source_failure'
            self.last_failure = {'type': type(exc).__name__, 'message': str(exc)}
        finally:
            if active is not None:
                self.frontier.append(active)
        if self.constants_ready:
            self.validate_partition()
        passed = status == 'whole_actual_P_error_at_most_one_over_50000'
        if passed and (self.frontier or self.closed != 1):
            raise RuntimeError('no whole comparison without exact complete coverage')
        constants = {key: self.pack(getattr(self, key)) for key in ('Leps', 'r0', 'p', 'q', 'e_star')
                     if hasattr(self, key) and getattr(self, key).is_finite()}
        state = {'schema': SCHEMA, 'input_sha256': self.input_sha,
            'source_sha256': self.source_sha, 'precision_bits': self.precision,
            'Taylor_order': self.N, 'maximum_depth': self.maximum_depth,
            'constants_ready': self.constants_ready, 'paid_constant_balls': constants,
            'closed_prefix_endpoint': str(self.closed),
            'closed_prefix_maximum_bound': str(self.closed_bound),
            'closed_leaf_count': self.closed_count,
            'remaining_actual_interval_stack': self.frontier,
            'costs': {'new_elapsed_seconds': time.monotonic()-self.started,
                      'new_actual_counts': dict(self.counts), 'prior_costs_not_counted_as_new': self.prior_costs}}
        return {'status': status, 'same_actual_input': self.input,
            'python_flint_version': self.flint_version, 'proof_state': state,
            'proof_state_sha256': sha(state), 'actual_point_witness': self.witness,
            'failure': self.last_failure, 'whole_continuous_actual_P_error_certified': passed,
            'actual_P_error_upper_exact_rational': str(self.closed_bound) if passed else None,
            'no_projection_refitting_or_actual_coefficient_change': True,
            'full_connection_metric_reach_or_README_certified': False}


def compare_actual_core(checkpoint, origin, *, precision_bits=192, order=6,
                        maximum_depth=30, budget_seconds=1800.,
                        resume=None, resume_sha256=None):
    public_only()
    return ActualCoreComparison(checkpoint, origin, precision_bits=precision_bits,
        order=order, maximum_depth=maximum_depth, budget_seconds=budget_seconds,
        resume=resume, resume_sha256=resume_sha256).run()
