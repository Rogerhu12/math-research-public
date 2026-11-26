#!/usr/bin/env python3
"""Same-actual-batch accurate total mean residuals for the full R711 seed.

This independently encloses the complete boundary and complement integrals.
All actual v/v_phi/v_phiphi words, exact scalar/chart/core/H definitions and
all radial pieces are retained. It produces the previously external R713
mean-equation inputs; it does not compute an outer normal root or certify
the complete embedded surface. Scientific execution is public Actions only.
"""
import argparse
from fractions import Fraction as F
from functools import cmp_to_key
import hashlib
import heapq
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time
from types import SimpleNamespace

SCHEMA = 'complete-reference-centred-c1-smooth-triangle-accurate-total-mean-residuals-v1'
JOURNAL_SCHEMA = 'same-reference-centred-c1-smooth-triangle-actual-batch-complete-integral-journal-v1'
TOPIC = 'topics/visible-flex-larger-amplitude'
PINS = {'fees': ('scripts/resume_20261126/reference_centred_c1_smooth_triangle_seed_angular_jet_error_bounds.py',
          'a7f1862362d729f29fba2b41ad040a5961b8cedb5eb729d8d6bbdc5bc36120c9'),
 'reference': ('scripts/resume_20261126/so3_axisymmetric_reference.py',
               '4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3'),
 'whole_scalar': ('scripts/resume_20261126/so3_axisymmetric_continuous_integrand.py',
                  'a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6')}
DERIVED_FROM_COMPLETE_MEAN_PRODUCER_SHA256 = '581fbcc397d379b64ee4a1d36b864b9a9e3b537f7b1be962ae03e22920c72202'
REFERENCE_UNIT_LAW = 'a_s er(theta0)+c ez; c>=0,a_s^2+c^2=1; complete prefix/Hold/R690 law'
SOURCE_SCOPE = ('complete accurate fixed-seed candidate mean residuals for this exact centred/cached outer report and whole '
 'actual batch; not its raw calibration defect, current normal root, whole-angle cover, physical lift, '
 'metric, reach or embedding certificate')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Accurate seed mean integration requires public repository Actions')


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def source_commit(repo):
    return subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'],
        text=True).strip()


def load(name, path, digest):
    if sha(path) != digest:
        raise ValueError('Changed complete accurate integration dependency: '+str(path))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def read_captured(path):
    raw = Path(path).read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def file_record(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)


def exact_affine(value):
    if (not isinstance(value, (list, tuple)) or len(value) != 2
            or any(isinstance(v, bool) for v in value)):
        raise ValueError('An exact affine point has two rational coefficients')
    return tuple(F(v) for v in value)


def affine_record(value):
    return [str(v) for v in value]


def average(left, right):
    return tuple((a+b)/2 for a, b in zip(left, right))


def encode(value):
    if isinstance(value, F):
        return str(value)
    if hasattr(value, 'json') and callable(value.json):
        return value.json()
    if isinstance(value, dict):
        return {str(key): encode(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(item) for item in value]
    return value


def write_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name+'.partial')
    temporary.write_text(json.dumps(encode(value), sort_keys=True, indent=2,
        allow_nan=False)+'\n')
    temporary.replace(path)


def event(**value):
    print(json.dumps(encode(value), separators=(',', ':'), allow_nan=False), flush=True)


class ActualMeanBatch:
    """Independent accurate reference binder; never constructs an outer field."""
    def __init__(self, args):
        require_actions()
        self.repo = Path(args.repo).resolve()
        topic = self.repo/TOPIC
        self.paths = {role: topic/relative for role, (relative, digest) in PINS.items()}
        self.modules = {role: load('_accurate_mean_'+role, self.paths[role], digest)
            for role, (relative, digest) in PINS.items()}
        self.k = self.modules['fees']
        self.seed, self.working, self.actual_binding = self.k.bind_actual_batch(
            self.repo, args.report, args.batch_index, args.batch_arrays)
        raw, digest = read_captured(args.report)
        if digest != self.actual_binding['report_sha256']:
            raise ValueError('The captured scientific report changed after the actual-batch binder')
        input_paths = {name: Path(getattr(args, name)).resolve() for name in
            ('reference_bundle', 'carrier', 'node_report', 'scalar_input', 'preparation_report')}
        required = dict(reference_bundle=raw['bundle_sha256'],
            carrier=raw['observation_carrier_sha256'],
            node_report=raw['exact_tail_node_report_sha256'],
            scalar_input=raw['exact_tail_scalar_input_sha256'],
            preparation_report=raw['independent_preparation_report']['sha256'])
        for name, path in input_paths.items():
            if sha(path) != required[name]:
                raise ValueError('The accurate scalar/chart input is not this seed: '+name)
        self.context = self.modules['reference'].AxisymmetricReferenceContext.from_files(
            repo=self.repo, **input_paths, panels=args.panels)
        self.report_path = Path(args.report).resolve()
        self.input_paths, self.input_sha256 = input_paths, required
        c, seed = self.context, self.seed
        if (seed['complete_axisymmetric_reference_model'] != c.model
                or seed['initial_reference_model_identity_sha256'] != c.identity
                or seed['initial_reference_bundle_sha256'] != required['reference_bundle']
                or seed['fixed_scalar_metric_identity_sha256'] != c.scalar_identity
                or seed['fixed_scalar_profile_definition'] != c.scalar_definition
                or seed['fixed_chart_core_sha256'] != c.model['fixed_chart_core_sha256']
                or seed['initial_height_hex'] != float(c.height).hex()
                or c.model['T0'] != REFERENCE_UNIT_LAW):
            raise ValueError('The exact complete reference, fixed chart or frozen height differs')
        if (not 0 <= F(c.full.old_ap_bound) < 1 or not 0 < F(c.full.out) < F(1, 40)
                or F(c.full.kp) != F(3, 2)):
            raise ValueError('The proved original positive-sqrt and R690 nonnegative-tail branch changed')
        for name, path in input_paths.items():
            if sha(path) != required[name]:
                raise ValueError('An accurate reference input changed while being bound: '+name)
        if sha(args.report) != digest:
            raise ValueError('The actual source report changed while its reference was bound')
        self.scalar = self.modules['whole_scalar'].ScalarWholeInterval(
            SimpleNamespace(context=c))
        self.d = self.scalar.d
        self.bits = int(args.precision_bits)
        self.I = self.k.Interval
        self.S = self.from_deep(self.scalar.exact_affine_box((F(1), F(0))))
        if self.S.lo <= 0:
            raise ValueError('The same exact scalar domain must have positive length')
        radius = c.model['radius_complete_enclosure']
        self.R = self.I(F(radius['lower_exact']), F(radius['upper_exact']), self.bits)
        if self.R.lo <= 0:
            raise ValueError('Keep the complete positive true terminal-radius enclosure')
        self.H = self.k.word(seed['initial_height_hex'])
        self.core = tuple(F(float(value)) for value in c.core)
        self.support = tuple(tuple(F(v) for v in pair)
            for pair in seed['exact_relative_support_intervals'])
        self.central = tuple(tuple(F(v) for v in pair)
            for pair in seed['exact_relative_central_intervals'])
        self.delta = F(seed['exact_relative_boundary_each_end_length'])
        self.beta = F(seed['exact_relative_boundary_total_length'])
        if (len(self.support) != 2 or len(self.central) != 2 or self.delta <= 0
                or self.beta != 4*self.delta):
            raise ValueError('Use both exact supported intervals and all four boundary layers')
        for i, ((a, b), (ca, cb)) in enumerate(zip(self.support, self.central)):
            if (not 0 < a < ca < cb < b < 1
                    or ca-a != self.delta or b-cb != self.delta
                    or (i and self.support[i-1][1] >= a)):
                raise ValueError('Complete exact support/central/boundary definitions disagree')
        self.Lc = self.S*sum((b-a for a, b in self.central), F(0))
        self.angles = [self.chart(row['literal_phi_hex']) for row in self.working]
        self.candidates = []
        for row in self.working:
            v = [self.k.point_vector(row[key]) for key in ('v', 'v_phi', 'v_phiphi')]
            lower, upper = self.k.point_norm(v[0], self.bits)
            if lower <= 0 or v[0][2] <= 0:
                raise ValueError('The actual working mean direction is not in the paid positive hemisphere')
            intervals = [[self.I(q, q, self.bits) for q in part] for part in v]
            direction, radius = self.k.normalized_jets(*intervals,
                norm_lower=lower, norm_upper=upper)
            zeta = v[0][2]/upper
            self.candidates.append(dict(v=intervals, d=direction,
                radius=radius, direction_vertical_lower=zeta,
                boundary_normalization_lower=self.k.cap_floor(zeta, self.bits)))
        self.plan = self.make_plan()
        self.binding = dict(schema=SCHEMA, source_sha256=sha(__file__),
            complete_source_sha256_by_role={role: digest for role, (path, digest) in PINS.items()},
            actual_batch=self.actual_binding, complete_seed_model=seed,
            reference_model_identity_sha256=c.identity,
            fixed_scalar_metric_identity_sha256=c.scalar_identity,
            complete_exact_scalar_definition=c.scalar_definition,
            exact_symbolic_nodes=[affine_record(value) for value in c.nodes],
            exact_partition=self.plan,
            exact_partition_identity_sha256=canonical(self.plan),
            complete_input_records={name: file_record(path) for name, path in input_paths.items()},
            precision_bits=self.bits, panels=int(args.panels),
            boundary_unit_and_nonnegative_vertical_provenance=dict(
                complete_reference_source_sha256=PINS['reference'][1],
                actual_complete_model_T0=c.model['T0'],
                original_prefix_Bernstein_ap_bound_exact=str(c.full.old_ap_bound),
                R690_exact_tail_width=str(c.full.out), R690_tail_kappa=str(c.full.kp),
                proved_references=['R669 section 2', 'R690 sections 2, 2.1, 2.3'],
                accurate_law='prefix positive sqrt; analytic/Hold sin-cos; R690 complete nonnegative-beta sine',
                exact_unit_property_is_structural_not_a_sampled_norm=True),
            scientific_field_F_J_root_evaluations=0,
            accurate_reference_only=True,
            old_hDelta_actual_input_constructor_used=False,
            scope=SOURCE_SCOPE)
        self.identity = canonical(self.binding)
        self.counts = dict(scalar_whole_interval_calls=0,
            complete_leaf_enclosures=0, complete_boundary_leaf_enclosures=0,
            complete_complement_leaf_enclosures=0, literal_angle_count=len(self.angles))

    def from_deep(self, value):
        return self.I(F(value[0], self.d.SCALE), F(value[1], self.d.SCALE), self.bits)

    def recheck_actual_bytes(self):
        if sha(self.report_path) != self.actual_binding['report_sha256']:
            raise ValueError('The bound scientific report changed during accurate integration')
        if sha(self.actual_binding['actual_raw_batch_path']) != self.actual_binding['actual_raw_batch_sha256']:
            raise ValueError('The bound full mean batch changed during accurate integration')
        for name, path in self.input_paths.items():
            if sha(path) != self.input_sha256[name]:
                raise ValueError('An exact same-seed input changed during integration: '+name)

    def compare(self, left, right):
        if left == right:
            return 0
        box = self.scalar.exact_affine_box(tuple(b-a for a, b in zip(left, right)))
        if box[0] > 0:
            return -1
        if box[1] < 0:
            return 1
        raise ValueError('The current exact S enclosure does not order distinct affine partition points')

    def region(self, point):
        for index, ((a, b), (ca, cb)) in enumerate(zip(self.support, self.central)):
            if self.compare((a, F(0)), point) < 0 and self.compare(point, (b, F(0))) < 0:
                if self.compare(point, (ca, F(0))) < 0:
                    return 'boundary_left', index
                if self.compare((cb, F(0)), point) < 0:
                    return 'boundary_right', index
                return 'central', index
        return 'outside', None

    def make_plan(self):
        cuts = set(self.context.nodes)
        for support, central in zip(self.support, self.central):
            cuts.update((v, F(0)) for v in support+central)
        ordered = sorted(cuts, key=cmp_to_key(self.compare))
        if ordered[0] != (F(0), F(0)) or ordered[-1] != (F(1), F(0)):
            raise ValueError('The complete exact original scalar domain changed')
        pieces = []
        for index, (left, right) in enumerate(zip(ordered, ordered[1:])):
            if self.compare(left, right) >= 0:
                raise ValueError('Every complete radial piece needs positive exact width')
            kind, support = self.region(average(left, right))
            pieces.append(dict(id='r'+str(index), left=affine_record(left),
                right=affine_record(right), kind=kind, support_index=support,
                depth=0, centrally_integrated_by_exact_Lc_v=(kind == 'central')))
        return pieces

    def chart(self, phi_word):
        phi = self.k.word(phi_word)
        d = self.d
        pbox = d.box(phi)
        theta, rho, rhop = pbox, d.ONE, d.ZERO
        support, supportp = d.ONE, d.ZERO
        for m, coefficient in enumerate(self.core, 1):
            if coefficient == 0:
                continue
            nu = 2*m
            sine, cosine = d.sine_cosine(d.scale(pbox, nu))
            q = 1-nu*nu
            theta = d.add(theta, d.scale(sine, F(q, nu)*coefficient))
            rho = d.add(rho, d.scale(cosine, q*coefficient))
            rhop = d.add(rhop, d.scale(sine, -nu*q*coefficient))
            support = d.add(support, d.scale(cosine, coefficient))
            supportp = d.sub(supportp, d.scale(sine, nu*coefficient))
        rho, rhop = self.from_deep(rho), self.from_deep(rhop)
        if rho.lo <= 0:
            raise ValueError('The actual literal fixed-chart angle has no positive accurate rho bound')
        st, ct = (self.from_deep(value) for value in d.sine_cosine(theta))
        sn, cn = (self.from_deep(value) for value in d.sine_cosine(pbox))
        zero = self.I(0, 0, self.bits)
        e, tangent = [ct, st, zero], [-st, ct, zero]
        normal, normal_tangent = [cn, sn, zero], [-sn, cn, zero]
        e1 = self.k.vscale(tangent, rho)
        e2 = self.k.vsub(self.k.vscale(tangent, rhop), self.k.vscale(e, rho**2))
        pp, ps = self.from_deep(support), self.from_deep(supportp)
        Gamma = self.k.vadd(self.k.vscale(normal, pp), self.k.vscale(normal_tangent, ps))
        Gamma1 = self.k.vscale(normal_tangent, rho)
        Gamma2 = self.k.vsub(self.k.vscale(normal_tangent, rhop), self.k.vscale(normal, rho))
        return dict(literal_phi_hex=phi_word, e=[e, e1, e2],
            Gamma=[Gamma, Gamma1, Gamma2], rho=rho, rho_phi=rhop,
            boundary_Tphi_norm_upper=self.k.norm_box(e1).hi,
            boundary_Tphiphi_norm_upper=self.k.norm_box(e2).hi)

    def relative_box(self, left, right):
        lo = self.I(left[0], left[0], self.bits)+left[1]/self.S
        hi = self.I(right[0], right[0], self.bits)+right[1]/self.S
        return self.I(lo.lo, hi.hi, self.bits)

    def cutoff(self, left, right, kind, index):
        a, b = self.support[index]
        ca, cb = self.central[index]
        relative = self.relative_box(left, right)
        if kind == 'boundary_left':
            u = ((relative-a)/self.delta).intersect(0, 1)
        elif kind == 'boundary_right':
            u = ((b-relative)/self.delta).intersect(0, 1)
        else:
            raise ValueError('A boundary cutoff needs its exact declared boundary piece')
        # S5 is increasing on [0,1]; endpoint evaluation avoids dependency inflation.
        def value(v):
            return v**3*(10-15*v+6*v*v)
        return self.I(value(u.lo), value(u.hi), self.bits).intersect(0, 1)

    def leaf(self, description):
        require_actions()
        left, right = exact_affine(description['left']), exact_affine(description['right'])
        kind, support = self.region(average(left, right))
        if kind != description['kind'] or support != description['support_index']:
            raise ValueError('A journal leaf changed its exact support region')
        if kind == 'central':
            raise ValueError('Central total mean is exact Lc*v, not a substituted sampling rule')
        width = self.from_deep(self.scalar.width_box(left, right))
        boxes, scalar_pieces = self.scalar.enclose(left, right)
        self.counts['scalar_whole_interval_calls'] += 1
        b, c = self.from_deep(boxes[0]), self.from_deep(boxes[1])
        # Exact formula property of the bound canonical R690 reference:
        # clipping is an intersection of two proved bounds, not a norm repair.
        b, c = b.intersect(-1, 1), c.intersect(0, 1)
        if kind == 'outside':
            scalar_integral = [width*b, width*c]
            result = dict(description=description, contribution='complement_scalar_b_c',
                integral=scalar_integral, scalar_piece_scope=scalar_pieces)
            self.counts['complete_complement_leaf_enclosures'] += 1
        else:
            chi = self.cutoff(left, right, kind, support)
            result_angles = []
            for chart, candidate in zip(self.angles, self.candidates):
                zero = self.I(0, 0, self.bits)
                e0, e1, e2 = chart['e']
                T = [self.k.vadd(self.k.vscale(e0, b), [zero, zero, c]),
                     self.k.vscale(e1, b), self.k.vscale(e2, b)]
                Y = [self.k.vadd(self.k.vscale(t, 1-chi), self.k.vscale(direction, chi))
                    for t, direction in zip(T, candidate['d'])]
                normalized, radius = self.k.normalized_jets(*Y,
                    norm_lower=candidate['boundary_normalization_lower'], norm_upper=1)
                result_angles.append([self.k.vscale(value, width) for value in normalized])
            result = dict(description=description, contribution='complete_boundary_three_angular_jets',
                integral=result_angles, scalar_piece_scope=scalar_pieces)
            self.counts['complete_boundary_leaf_enclosures'] += 1
        self.counts['complete_leaf_enclosures'] += 1
        return encode(result)

    def children(self, description):
        left, right = exact_affine(description['left']), exact_affine(description['right'])
        middle = average(left, right)
        return [dict(description, id=description['id']+'/'+str(i), depth=description['depth']+1,
            left=affine_record(a), right=affine_record(b))
            for i, (a, b) in enumerate(((left, middle), (middle, right)))]

    def decode_integral(self, leaf):
        if leaf['contribution'] == 'complement_scalar_b_c':
            if leaf['description']['kind'] != 'outside' or len(leaf['integral']) != 2:
                raise ValueError('Invalid complete complement journal contribution')
            return [self.k.box(value, self.bits) for value in leaf['integral']]
        if (leaf['contribution'] != 'complete_boundary_three_angular_jets'
                or not leaf['description']['kind'].startswith('boundary')
                or len(leaf['integral']) != len(self.angles)):
            raise ValueError('Invalid complete boundary journal contribution')
        answer = []
        for angle in leaf['integral']:
            if len(angle) != 3:
                raise ValueError('All three accurate total-equation angular jets are required')
            answer.append([self.k.vector_box(value, self.bits) for value in angle])
        return answer

    def leaf_score(self, leaf):
        value = self.decode_integral(leaf)
        if leaf['contribution'] == 'complement_scalar_b_c':
            h = value[0].hi-value[0].lo
            z = value[1].hi-value[1].lo
            return max(sum(component.abs_upper() for component in chart['e'][j])*h
                +(z if j == 0 else 0) for chart in self.angles for j in range(3))
        return max(sum(q.hi-q.lo for q in jet) for angle in value for jet in angle)

    def assemble_sums(self, complement_sums, boundary_sums):
        """Exact endpoint sums of complete active leaves; not interval subtraction."""
        zero = self.I(0, 0, self.bits)
        complement = [self.I(*value, self.bits) for value in complement_sums]
        boundary = [[[self.I(*value, self.bits) for value in jet]
            for jet in angle] for angle in boundary_sums]
        rows, widths = [], []
        for index, (chart, candidate) in enumerate(zip(self.angles, self.candidates)):
            horizontal = self.R-complement[0]
            vertical = self.H-complement[1]
            K = []
            for j in range(3):
                cap = self.k.vscale(chart['e'][j], horizontal)
                if j == 0:
                    cap = self.k.vadd(cap, [zero, zero, vertical])
                K.append(self.k.vsub(cap, chart['Gamma'][j]))
            residual = [self.k.vsub(self.k.vadd(self.k.vscale(candidate['v'][j], self.Lc),
                boundary[index][j]), K[j]) for j in range(3)]
            norms = [self.k.norm_box(value).hi for value in residual]
            km, kp = self.k.norm_box(K[0]).lo, self.k.norm_box(K[0]).hi
            kz = K[0][2].lo
            bup = (self.S*self.beta).hi
            hypotheses = bool(0 < km <= kp and bup < km and bup < kz and kp+bup < self.Lc.lo)
            fees = dict(accurate_S_enclosure=self.S,
                K_norm_lower=km, K_norm_upper=kp, K_vertical_lower=kz,
                accurate_reference_unit_and_nonnegative_vertical_on_complete_boundary=True,
                accurate_centered_total_equation_residual_norms=norms,
                boundary_reference_phi_norm_upper=chart['boundary_Tphi_norm_upper'],
                boundary_reference_phiphi_norm_upper=chart['boundary_Tphiphi_norm_upper'],
                accurate_fixed_chart_radial_jets=dict(zip(('e', 'ep', 'epp'), chart['e'])),
                fixed_chart_e_is_the_accurate_horizontal_unit_radial_vector=True)
            rows.append(dict(literal_phi_hex=chart['literal_phi_hex'], fees=fees, nodes=[],
                accurate_total_equation_vector_enclosures=residual,
                accurate_K_angular_jets=K,
                all_pointwise_R709_sufficient_inequalities_proved=hypotheses,
                full_angle_R709_hypotheses_certified=False))
            widths.extend(sum(component.hi-component.lo for component in jet) for jet in residual)
        return encode(dict(angles=rows, complement_scalar_integral=complement,
            complete_boundary_angular_integrals=boundary,
            maximum_total_equation_component_L1_width=max(widths),
            all_literal_angle_R709_hypotheses_proved=all(
                row['all_pointwise_R709_sufficient_inequalities_proved'] for row in rows)))


class CompleteLeafJournal:
    """Atomic complete-leaf transitions; partial new children never replace a parent."""
    def __init__(self, actual, directory, *, width_goal):
        self.actual = actual
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.path = self.directory/'journal.jsonl'
        self.header_path = self.directory/'binding.json'
        self.width_goal = F(width_goal)
        if self.width_goal <= 0:
            raise ValueError('Use an explicit positive accurate integral width goal')
        self.binding = dict(schema=JOURNAL_SCHEMA, actual_binding=actual.binding,
            actual_binding_identity_sha256=actual.identity,
            width_goal=str(self.width_goal),
            leaf_rule='outward whole-piece range times complete exact positive affine width',
            initial_plan_order='exact radial order; central pieces paid by exact Lc*v',
            refinement_rule='largest current interval-contribution L1 width; exact affine midpoint',
            complete_infinite_tail_never_truncated=True)
        self.identity = canonical(self.binding)
        self.expected = [value for value in actual.plan if value['kind'] != 'central']
        self.leaves, self.heap = {}, []
        self.complement_sums = [[F(0), F(0)] for _ in range(2)]
        self.boundary_sums = [[[[F(0), F(0)] for _ in range(3)] for _ in range(3)]
            for _ in actual.angles]
        self.next_initial, self.seq, self.previous = 0, 0, '0'*64
        self.restored_transitions = 0
        if self.header_path.exists():
            header, digest = read_captured(self.header_path)
            if header != dict(binding=self.binding, identity_sha256=self.identity):
                raise ValueError('A journal must retain the identical actual batch/source/precise plan')
            if not self.path.exists():
                # A process may have stopped after its atomic empty binding.
                # This recovers no claimed scientific contribution.
                self.path.touch()
            self.restore()
        else:
            if self.path.exists() or any(self.directory.iterdir()):
                raise ValueError('A fresh journal directory must not contain unbound existing data')
            write_json(self.header_path, dict(binding=self.binding, identity_sha256=self.identity))
            self.path.touch()

    @property
    def complete(self):
        return self.next_initial == len(self.expected)

    def add(self, leaf):
        identity = leaf['description']['id']
        if identity in self.leaves:
            raise ValueError('A complete active leaf is duplicated')
        score = self.actual.leaf_score(leaf)
        self.leaves[identity] = leaf
        self.accumulate(leaf, 1)
        heapq.heappush(self.heap, (-score, identity))

    def accumulate(self, leaf, sign):
        values = self.actual.decode_integral(leaf)
        if leaf['contribution'] == 'complement_scalar_b_c':
            pairs = zip(self.complement_sums, values)
            for target, value in pairs:
                target[0] += sign*value.lo
                target[1] += sign*value.hi
        else:
            for target_angle, angle in zip(self.boundary_sums, values):
                for target_jet, jet in zip(target_angle, angle):
                    for target, value in zip(target_jet, jet):
                        target[0] += sign*value.lo
                        target[1] += sign*value.hi

    def complete_result(self):
        if not self.complete:
            raise ValueError('A partial cover has no complete total equation residual')
        return self.actual.assemble_sums(self.complement_sums, self.boundary_sums)

    def transition(self, payload):
        kind = payload.get('kind')
        if kind == 'initial':
            if self.complete:
                raise ValueError('The complete initial cover was already supplied')
            leaf = payload['leaf']
            if leaf['description'] != self.expected[self.next_initial]:
                raise ValueError('Every initial exact piece must be read once in complete radial order')
            self.add(leaf)
            self.next_initial += 1
        elif kind == 'split':
            if not self.complete:
                raise ValueError('Refinement may not hide any unread initial complete piece')
            parent = payload['parent_id']
            if parent not in self.leaves:
                raise ValueError('A split requires its active whole parent')
            description = self.leaves[parent]['description']
            expected = self.actual.children(description)
            children = payload['children']
            if len(children) != 2 or [value['description'] for value in children] != expected:
                raise ValueError('Two complete children must partition their exact parent')
            self.accumulate(self.leaves[parent], -1)
            del self.leaves[parent]
            for leaf in children:
                self.add(leaf)
        else:
            raise ValueError('Unknown complete-leaf journal transition')

    def restore(self):
        with self.path.open('rb') as stream:
            for line in stream:
                if not line.endswith(b'\n'):
                    raise ValueError('A journal has a partial record; do not invent its paid contribution')
                entry = json.loads(line)
                payload = entry['payload']
                body = dict(schema=JOURNAL_SCHEMA, binding_identity_sha256=self.identity,
                    sequence=self.seq, previous_sha256=self.previous, payload=payload)
                if any(entry.get(key) != value for key, value in body.items()):
                    raise ValueError('The actual journal chain, source, plan or sequence changed')
                digest = canonical(body)
                if entry.get('entry_sha256') != digest:
                    raise ValueError('A complete scientific journal record changed')
                self.transition(payload)
                self.previous, self.seq = digest, self.seq+1
                self.restored_transitions += 1

    def append(self, payload):
        body = dict(schema=JOURNAL_SCHEMA, binding_identity_sha256=self.identity,
            sequence=self.seq, previous_sha256=self.previous, payload=payload)
        digest = canonical(body)
        data = json.dumps(dict(body, entry_sha256=digest), sort_keys=True,
            separators=(',', ':'), allow_nan=False)+'\n'
        with self.path.open('a') as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        self.transition(payload)
        self.previous, self.seq = digest, self.seq+1

    def largest(self):
        while self.heap and self.heap[0][1] not in self.leaves:
            heapq.heappop(self.heap)
        if not self.heap:
            raise ValueError('A complete noncentral domain cannot have an empty integral cover')
        return self.leaves[self.heap[0][1]]

    def run(self, *, seconds, maximum_transitions=None, progress=None):
        start = time.monotonic()
        transitions = 0
        result = self.complete_result() if self.complete else None
        while True:
            reached = (self.complete and F(result['maximum_total_equation_component_L1_width']) <= self.width_goal)
            if reached or time.monotonic()-start >= seconds:
                break
            if maximum_transitions is not None and transitions >= maximum_transitions:
                break
            if not self.complete:
                leaf = self.actual.leaf(self.expected[self.next_initial])
                payload = dict(kind='initial', leaf=leaf)
            else:
                parent = self.largest()
                children = [self.actual.leaf(description)
                    for description in self.actual.children(parent['description'])]
                payload = dict(kind='split', parent_id=parent['description']['id'], children=children)
            self.append(payload)
            transitions += 1
            if self.complete:
                result = self.complete_result()
            if progress is not None:
                progress(self, transitions, time.monotonic()-start, result)
        return dict(complete=self.complete, tolerance_reached=bool(reached),
            completed_initial_pieces=self.next_initial, required_initial_pieces=len(self.expected),
            active_complete_leaves=len(self.leaves), new_complete_transitions=transitions,
            restored_complete_transitions=self.restored_transitions,
            total_complete_transitions=self.seq, seconds=time.monotonic()-start,
            journal_chain_sha256=self.previous,
            complete_result=result if self.complete else None,
            partial_integrals_not_published_as_full_residuals=not self.complete)


def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, required=True)
    p.add_argument('--report', type=Path, required=True)
    p.add_argument('--batch-index', type=int, required=True)
    p.add_argument('--batch-arrays', type=Path)
    for name in ('reference-bundle', 'carrier', 'node-report', 'scalar-input', 'preparation-report'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--outdir', type=Path, required=True)
    p.add_argument('--panels', type=int, default=128)
    p.add_argument('--precision-bits', type=int, default=160)
    p.add_argument('--width-goal', default='1/100000000')
    p.add_argument('--seconds', type=float, default=600.)
    p.add_argument('--maximum-transitions', type=int)
    a = p.parse_args()
    if (a.batch_index < 0 or a.panels < 1 or not 64 <= a.precision_bits <= 1024
            or not math.isfinite(a.seconds) or a.seconds <= 0
            or F(a.width_goal) <= 0
            or (a.maximum_transitions is not None and a.maximum_transitions < 1)):
        p.error('Use positive complete arithmetic/budget parameters and a real batch index')
    return a


def main():
    require_actions()
    args = parse_args()
    args.repo, args.outdir = args.repo.resolve(), args.outdir.resolve()
    if args.outdir == args.repo or args.repo in args.outdir.parents:
        raise ValueError('All actual raw integration journals stay outside the repository')
    args.outdir.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    actual = ActualMeanBatch(args)
    journal = CompleteLeafJournal(actual, args.outdir/'complete-leaves', width_goal=args.width_goal)
    report_path, request_path = args.outdir/'report.json', args.outdir/'fee-request.json'
    report = dict(schema=SCHEMA, source_sha256=sha(__file__), source_commit=source_commit(args.repo),
        github_run_id=os.environ.get('GITHUB_RUN_ID'),
        binding=actual.binding, binding_identity_sha256=actual.identity,
        complete=False, tolerance_reached=False, exact_or_uniform_geometry_certificate=False,
        full_outer_normal_certificate=False,
        accurate_total_equation_inputs_computed_here=True,
        profile_moments_computed_here=False,
        profile_moments_require_independent_R713_consumer=True,
        previous_mean_working_residual_used_as_accurate_error=False,
        current_F_J_or_endpoint_roots_recomputed=False,
        complete_outer_source_attribution=actual.actual_binding['complete_outer_attribution'],
        fixed_reference_mean_equation_is_not_actual_outer_Q_total=True,
        raw_reference_calibration_and_current_normal_fees_paid=False,
        complete_R715_physical_lift_and_sixjet_fees_paid=False,
        scope=SOURCE_SCOPE)
    if report_path.exists():
        previous, digest = read_captured(report_path)
        if previous.get('binding_identity_sha256') != actual.identity:
            raise ValueError('The output directory belongs to another complete mean batch')
    write_json(report_path, report)
    last_progress = [time.monotonic()]

    def progress(state, count, seconds, result):
        if time.monotonic()-last_progress[0] >= 20:
            event(event='complete_accurate_mean_integral_piece', elapsed_seconds=seconds,
                complete_cover=state.complete, active_leaves=len(state.leaves),
                initial_pieces_completed=state.next_initial, full_initial_pieces=len(state.expected),
                committed_transitions=state.seq,
                maximum_complete_residual_width=None if result is None else
                    result['maximum_total_equation_component_L1_width'])
            last_progress[0] = time.monotonic()

    state = journal.run(seconds=args.seconds, maximum_transitions=args.maximum_transitions,
        progress=progress)
    actual.recheck_actual_bytes()
    report.update({key: value for key, value in state.items() if key != 'complete_result'})
    report['counts_this_invocation'] = actual.counts
    report['journal'] = file_record(journal.path)
    report['journal_binding'] = file_record(journal.header_path)
    report['total_invocation_seconds'] = time.monotonic()-started
    if state['complete']:
        result = state['complete_result']
        request = dict(schema=actual.k.REQUEST_SCHEMA, binding=actual.actual_binding,
            external_fee_provenance=dict(
                source_sha256=sha(__file__), report_source_schema=SCHEMA,
                accurate_mean_binding_identity_sha256=actual.identity,
                complete_journal_sha256=report['journal']['sha256'],
                complete_journal_chain_sha256=journal.previous,
                complete_reference_identity_sha256=actual.context.identity,
                exact_reference_unit_and_nonnegative_vertical_law=REFERENCE_UNIT_LAW,
                exact_all_radial_pieces_and_infinite_tail_retained=True,
                actual_batch_angles_only=True, continuous_phi_cover_certified=False,
                actual_working_scalar_quadrature_or_libm_errors_assumed_zero=False,
                current_outer_field_or_geometry_certified=False,
                complete_outer_source_attribution=actual.actual_binding['complete_outer_attribution'],
                raw_reference_calibration_or_current_normal_error_certified=False,
                complete_R715_physical_lift_error_certified=False),
            angles=result['angles'])
        write_json(request_path, request)
        report['fee_request'] = file_record(request_path)
        report['maximum_total_equation_component_L1_width'] = result['maximum_total_equation_component_L1_width']
        report['all_literal_angle_R709_hypotheses_proved'] = result['all_literal_angle_R709_hypotheses_proved']
        report['literal_angle_count'] = len(result['angles'])
        report['accurate_residual_norm_upper_by_angle'] = [
            row['fees']['accurate_centered_total_equation_residual_norms'] for row in result['angles']]
        report['maximum_accurate_residual_norm_upper'] = [str(max(
            F(row[j]) for row in report['accurate_residual_norm_upper_by_angle'])) for j in range(3)]
    else:
        report['fee_request'] = None
        report['maximum_total_equation_component_L1_width'] = None
        report['all_literal_angle_R709_hypotheses_proved'] = None
        report['literal_angle_count'] = len(actual.angles)
        report['accurate_residual_norm_upper_by_angle'] = None
        report['maximum_accurate_residual_norm_upper'] = None
    write_json(report_path, report)
    event(event='actual_accurate_mean_fee_report', complete=report['complete'],
        tolerance_reached=report['tolerance_reached'], active_complete_leaves=report['active_complete_leaves'],
        total_invocation_seconds=report['total_invocation_seconds'], report=file_record(report_path))


if __name__ == '__main__':
    main()
