#!/usr/bin/env python3
"""Independent whole-R690 axisymmetric unit-meridian input for full SO3.

The documented warm supplies only its exact scalar/nodes and complete core.
No optimized old q field, d3 parent, old direction, metric or geometry
certificate is required. All original positive observations are regenerated.
The true T0 includes the full quintic prefix, analytic continuation, Hold
and entire deep flat tail. Actual computation belongs in public Actions.
"""
import argparse
import bisect
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time
from types import SimpleNamespace
import numpy as np

SCHEMA = 'R690-independent-axisymmetric-SO3-reference-input-v1'
PREPARATION_SCHEMA = 'R690-independent-axisymmetric-SO3-preparation-v1'
SOURCE_PINS = {
    'warm_producer': ('notes/2026-11-17-parallel-model-fullclosed-hold-warm.py', 'bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3'),
    'observed': ('scripts/resume_20261120/gauss_observed_closed_gram.py', '26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d'),
    'scalar': ('notes/2026-11-17-parallel-model-full-hold-oracle.py', 'a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670'),
    'integer': ('notes/2026-11-17-parallel-inward-integral-enclosure.py', 'babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0'),
    'hold': ('scripts/parallel_20261117_negative_hold_profile_ivp.py', 'ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1'),
    'deep_scalar': ('scripts/resume_20261126/deep_valley_tail_input.py', 'e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2'),
    'history': ('scripts/resume_20261120/launch_refinement_from_full_report.py', '4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'),
}

def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific independent SO3 input requires public repository Actions')

def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def file_record(path, repo=None):
    path = Path(path).resolve()
    result = dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)
    if repo is not None:
        try:
            result['repo_relative_path'] = str(path.relative_to(repo))
        except ValueError:
            pass
    return result


def load(name, path, expected=None):
    if expected is not None and sha(path) != expected:
        raise ValueError('Changed complete source '+str(path))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def event(**values):
    print(json.dumps(values, separators=(',', ':'), allow_nan=False), flush=True)


def write_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name+'.partial')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)



def array_sha(value):
    value = np.ascontiguousarray(value)
    h = hashlib.sha256(str(value.dtype).encode())
    h.update(json.dumps(list(value.shape)).encode())
    h.update(value.tobytes())
    return h.hexdigest()

def paths_and_modules(repo):
    topic = Path(repo).resolve()/'topics/visible-flex-larger-amplitude'
    paths, modules = {}, {}
    for role, (relative, expected) in SOURCE_PINS.items():
        paths[role] = topic/relative
        if sha(paths[role]) != expected:
            raise ValueError('Changed complete independent-input dependency: '+role)
        if role != 'warm_producer':
            modules[role] = load('_independent_axis_'+role, paths[role], expected)
    return paths, modules

def read_scalar(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)

def scalar_parameters(data):
    return dict(analytic_extension_origin=data['analytic_extension_origin'],
        geometry=data['fixed_scalar_profile']['geometry'])

def upper_float(value):
    value = F(value)
    result = float(value)
    if F(result) < value:
        result = np.nextafter(result, np.inf)
    return float(result)

def midpoint_and_error(box, scale):
    value = float(F(box[0]+box[1], 2*scale))
    error = max(abs(F(value)-F(box[0], scale)), abs(F(value)-F(box[1], scale)))
    return value, upper_float(error)

def point_definition(nodes, cell, u):
    cell, u = int(cell), float(u)
    if not 0 <= cell < len(nodes)-1 or not math.isfinite(u) or not 0 <= u <= 1:
        raise ValueError('Use a literal local point on the complete symbolic mesh')
    q = F(u)
    return tuple((1-q)*left+q*right for left, right in zip(nodes[cell], nodes[cell+1]))

class WholeAxisymmetricLaw:
    """Full b=a_s,c>=0,b_s,c_s; no repeated tail height-integral table.

    The e091 derivative-only methods are composed with exact parameters in
    a separate object. It is not a fabricated complete DeepValleyTail.
    """
    def __init__(self, full, deep_module, *, tail_cutoff='1/8'):
        require_actions()
        self.full, self.d = full, deep_module
        epsilon = F(tail_cutoff)
        if not 0 < epsilon <= F(1, 8):
            raise ValueError('Use a complete declared infinite-tail cutoff')
        class TailDerivativeLaw:
            _beta_jets = deep_module.DeepValleyTail._beta_jets
            beta_and_curvature = deep_module.DeepValleyTail.beta_and_curvature
        self.tail = TailDerivativeLaw()
        t = self.tail
        t.width, t.kappa = F(full.out), F(full.kp)
        t.amplitude, t.epsilon = t.width*t.kappa, epsilon
        t.tail_bounds = deep_module.tail_derivative_envelopes(epsilon, t.amplitude, t.width, orders=4)
        self.cache, self.maximum_errors, self.evaluations = {}, np.zeros(4), 0

    def _polynomial(self, coefficients, ubox):
        h = self.full.h
        result = h.interval(F(0))
        for coefficient in reversed(coefficients):
            result = h.add(h.multiply(result, ubox), h.interval(F(coefficient)))
        return result

    def _prefix_boxes(self, low, high):
        p, h, o = self.full, self.full.h, self.full.o
        pieces = []
        first = min(len(p.x)-2,max(0,bisect.bisect_right(p.x,low)-1))
        last = min(len(p.x)-2,bisect.bisect_left(p.x,high))
        for j in range(first,last+1):
            left,right = p.x[j:j+2]
            lo, hi = max(low, left), min(high, right)
            if lo > hi:
                continue
            width = right-left
            u = o.box((lo-left)/width, (hi-left)/width)
            co = p.coefficients[j]
            first = [F(k+1)*co[k+1]/width for k in range(5)]
            second = [F((k+1)*(k+2))*co[k+2]/width**2 for k in range(4)]
            b, bs = self._polynomial(first, u), self._polynomial(second, u)
            limit = o.box(-p.old_ap_bound, p.old_ap_bound)
            b = max(b[0], limit[0]), min(b[1], limit[1])
            if b[0] > b[1]:
                raise ArithmeticError('Prefix derivative missed its proved complete bound')
            c = o.square_root(o.subtract(h.interval(F(1)), h.multiply(b, b)))
            if c[0] <= 0:
                raise ArithmeticError('The original quintic branch has proved c>0')
            cs = h.neg(o.divide(h.multiply(b, bs), c))
            pieces.append((b, c, bs, cs))
        if not pieces:
            raise ValueError('The complete original scalar knots missed the query')
        return tuple((min(v[k][0] for v in pieces), max(v[k][1] for v in pieces)) for k in range(4))

    def _analytic_boxes(self, low, high):
        p, h, o = self.full, self.full.h, self.full.o
        angle = o.subtract(p.alpha_origin, h.multiply(p.K,
            o.subtract(o.box(low, high), h.interval(p.origin))))
        b, c = h.sine_cosine(angle)
        return b, c, h.neg(h.multiply(p.K, c)), h.multiply(p.K, b)

    def _hold_boxes(self, definition):
        p, h = self.full, self.full.h
        angle, curvature = self.d.DeepValleyTail._old_angle_curvature(
            SimpleNamespace(old=p), p.affine_time(*definition))
        b, c = h.sine_cosine(angle)
        return b, c, h.neg(h.multiply(curvature, c)), h.multiply(curvature, b)

    def boxes(self, definition):
        require_actions()
        definition = tuple(F(v) for v in definition)
        p, h, d = self.full, self.full.h, self.d
        sbox = p.affine_time(*definition)
        low, high = F(sbox[0], h.S), F(sbox[1], h.S)
        if low < 0 or high > F(p.S[1], h.S):
            raise ValueError('Point outside the same exact scalar domain')
        if definition == (F(1), F(0)):
            return tuple(d.box(v) for v in (-1, 0, 0, 0))
        if definition == (F(0), F(0)):
            v = self._prefix_boxes(F(0), F(0))
            return d.ZERO, d.ONE, d.box(F(v[2][0], h.S), F(v[2][1], h.S)), d.ZERO
        old = []
        if low <= p.origin:
            old.append(self._prefix_boxes(low, min(high, p.origin)))
        if high >= p.origin and low <= p.cut:
            old.append(self._analytic_boxes(max(low, p.origin), min(high, p.cut)))
        if old and high <= p.cut:
            joined = tuple((min(v[k][0] for v in old), max(v[k][1] for v in old)) for k in range(4))
            return tuple(d.box(F(v[0], h.S), F(v[1], h.S)) for v in joined)
        alpha, beta = definition
        t = d.box(-beta) if alpha == 1 else d.sub(
            d.scale(d.box(F(p.S[0], h.S), F(p.S[1], h.S)), 1-alpha), d.box(beta))
        tl, th = F(t[0], d.SCALE), F(t[1], d.SCALE)
        if tl >= self.tail.width/4:
            old.append(self._hold_boxes(definition))
            joined = tuple((min(v[k][0] for v in old), max(v[k][1] for v in old)) for k in range(4))
            return tuple(d.box(F(v[0], h.S), F(v[1], h.S)) for v in joined)
        if tl < 0:
            raise ValueError('Exact symbolic point box extends past the cap')
        if th > self.tail.width/4:
            if th > self.tail.width:
                raise ValueError('Replacement-anchor point spans outside the out ramp')
            left = self.tail.beta_and_curvature(tl/self.tail.width, F(1, 4))
            right = self.tail._beta_jets(F(1, 4), th/self.tail.width)
            angle = d.hull((left[0], right[0]))
            curvature = d.hull((left[1], d.scale(right[1], 1/self.tail.width)))
        else:
            angle, curvature = self.tail.beta_and_curvature(tl/self.tail.width, th/self.tail.width)
        sine, cosine = d.sine_cosine(angle)
        return d.neg(cosine), sine, d.neg(d.mul(curvature, sine)), d.neg(d.mul(curvature, cosine))

    def at(self, definition):
        key = tuple(F(v) for v in definition)
        if key not in self.cache:
            pairs = [midpoint_and_error(v, self.d.SCALE) for v in self.boxes(key)]
            values, errors = np.array([v for v,e in pairs]), np.array([e for v,e in pairs])
            if not np.isfinite(values).all() or not np.isfinite(errors).all():
                raise ArithmeticError('Nonfinite complete scalar meridian jet')
            self.maximum_errors = np.maximum(self.maximum_errors, errors)
            values.setflags(write=False); errors.setflags(write=False)
            self.cache[key] = values, errors
            self.evaluations += 1
        return self.cache[key]

    def metadata(self):
        return dict(source_sha256=sha(__file__), deep_derivative_source_sha256=SOURCE_PINS['deep_scalar'][1],
            exact_scalar_law='True quintics, analytic continuation, all Hold and complete R690 deep tail',
            positive_vertical_branch=True, original_prefix_a_s_bound_exact=str(self.full.old_ap_bound),
            tail_cutoff_exact=str(self.tail.epsilon), complete_infinite_tail_included=True,
            reference_height_integrals_recomputed=False, actual_new_scalar_queries=self.evaluations,
            maximum_four_scalar_carrier_errors=self.maximum_errors.tolist(),
            full_T0_trigonometry_and_normalization_rounding_certified=False)

def target_a_box(full, deep, d, definition):
    alpha, beta = definition
    t = d.box(-beta) if alpha == 1 else d.sub(d.scale(deep._from_old(full.S), 1-alpha), d.box(beta))
    low, high = F(t[0], d.SCALE), F(t[1], d.SCALE)
    anchor = deep.width/4
    if high <= anchor:
        return deep.reference_at_affine(alpha, beta)[0]
    if low >= anchor:
        return deep._from_old(full.at_box(full.affine_time(alpha, beta))[0])
    fee = max(anchor-low, high-anchor)
    return d.add(deep.anchor_radius, d.box(-fee, fee))


class AxisymmetricReferenceContext:
    """Prepared input, without reconstructing an old physical q field as T0."""
    @classmethod
    def from_files(cls, *, repo, reference_bundle, carrier, node_report, scalar_input,
                   preparation_report, panels=128):
        require_actions()
        paths, modules = paths_and_modules(repo)
        report = json.loads(Path(preparation_report).read_text())
        actual = dict(reference_bundle=reference_bundle, carrier=carrier,
            node_report=node_report, scalar_input=scalar_input)
        if (report.get('schema') != PREPARATION_SCHEMA or report.get('source_sha256') != sha(__file__)
                or report.get('complete') is not True):
            raise ValueError('Use the actual complete independent reference preparation')
        for role, value in actual.items():
            if report['input_for_solver'][role]['sha256'] != sha(value):
                raise ValueError('Changed independent input bytes: '+role)
        for role, (_, expected) in SOURCE_PINS.items():
            if report['source_sha256_by_role'].get(role) != expected:
                raise ValueError('Actual preparation omitted a complete source: '+role)
        with np.load(reference_bundle, allow_pickle=False) as data:
            saved = {key: np.array(data[key], copy=True) for key in data.files}
        with np.load(carrier, allow_pickle=False) as data:
            obs = {key: np.array(data[key], copy=True) for key in data.files}
        model = json.loads(str(saved['reference_model_json'].item()))
        identity = canonical(model)
        if (str(saved['schema'].item()) != SCHEMA or model.get('schema') != SCHEMA
                or model.get('source_sha256') != sha(__file__)
                or str(saved['reference_model_identity_sha256'].item()) != identity
                or report.get('reference_model_identity_sha256') != identity
                or model.get('scalar_input_sha256') != sha(scalar_input)
                or model.get('symbolic_node_report_sha256') != sha(node_report)
                or model.get('observation_carrier_sha256') != sha(carrier)
                or canonical(model['fixed_scalar_profile_definition']) != model['fixed_scalar_metric_identity_sha256']):
            raise ValueError('The complete new reference/model/source identity differs')
        self = cls()
        self.repo, self.paths, self.modules = Path(repo).resolve(), paths, modules
        self.input_records = {role: file_record(value) for role, value in actual.items()}
        self.input_records['preparation_report'] = file_record(preparation_report)
        self.model, self.identity, self.preparation, self.data = model, identity, report, saved
        self.mesh, self.core = np.array(saved['mesh'], copy=True), np.array(saved['initial_core'], copy=True)
        self.height, self.radius, self.width = (float(saved[k]) for k in ('initial_height','radius','width'))
        self.M, self.J = len(self.core), len(self.mesh)
        nodes = json.loads(Path(node_report).read_text())
        self.nodes = [(F(row['S_coefficient']),F(row['constant'])) for row in nodes['true_scalar_nodes']]
        if (self.M != 160 or self.J != 923 or self.core.shape != (160,)
                or len(self.nodes) != self.J or self.nodes[0] != (F(0),F(0)) or self.nodes[-1] != (F(1),F(0))
                or self.mesh[0] != 0 or not np.isfinite(self.mesh).all() or not np.all(np.diff(self.mesh)>0)
                or not np.isfinite(self.core).all() or not math.isfinite(self.height)
                or model['mesh_sha256'] != array_sha(self.mesh)
                or model['fixed_chart_core_sha256'] != array_sha(self.core)
                or model['fixed_core_first3'] != [float(v).hex() for v in self.core[:3]]
                or model['radius_carrier_hex'] != self.radius.hex()
                or not np.array_equal(saved['fixed_core_first3'], self.core[:3])):
            raise ValueError('Keep the actual full domain and complete core/H parameters')
        for key in ('mesh','radius','width','fixed_core_first3'):
            if not np.array_equal(saved[key],obs[key]):
                raise ValueError('Reference and observation carrier disagree: '+key)
        self.observed = modules['observed']
        self.plan = self.observed.ObservationPlan.from_arrays(obs)
        self.a_observations = np.array(obs['a_observations'],copy=True)
        if (len(self.plan.cells) != 7377 or self.plan.legacy_count != 1845 or self.plan.order != 6
                or self.a_observations.shape != (7377,) or not np.isfinite(self.a_observations).all()
                or np.any(self.a_observations <= 0) or model['a_observations_sha256'] != array_sha(self.a_observations)):
            raise ValueError('Retain all original positive legacy and Gauss observations')
        parameters = read_scalar(scalar_input)
        if canonical(scalar_parameters(parameters)) != model['original_scalar_parameters_identity_sha256']:
            raise ValueError('The true original scalar law changed')
        self.full = modules['scalar'].FullHold(parameters,paths['integer'],paths['hold'],panels=int(panels))
        if self.full.carrier(self.full.S) != float(self.mesh[-1]):
            raise ValueError('Keep the same exact S and its carrier')
        self.scalar_identity = model['fixed_scalar_metric_identity_sha256']
        self.scalar_definition = model['fixed_scalar_profile_definition']
        self.law = WholeAxisymmetricLaw(self.full,modules['deep_scalar'],tail_cutoff=model['working_scalar_tail_cutoff'])
        self.reference_cache = {}
        cells,local,values,errors = (saved[k] for k in
            ('cached_scalar_cells','cached_scalar_local','cached_scalar_values','cached_scalar_errors'))
        if (cells.ndim != 1 or local.shape != cells.shape or values.shape != (len(cells),4)
                or errors.shape != values.shape or not np.isfinite(values).all()
                or not np.isfinite(errors).all() or np.any(errors < 0)):
            raise ValueError('Keep the complete scalar jet/error carrier')
        for cell,u,value,error in zip(cells,local,values,errors):
            if int(cell) != cell:
                raise ValueError('Cached cell must be an exact integer')
            point_definition(self.nodes,int(cell),float(u))
            key = (int(cell),float(u).hex())
            if key in self.reference_cache:
                raise ValueError('Duplicate cached scalar address')
            value.setflags(write=False); error.setflags(write=False)
            self.reference_cache[key] = value,error
        self.maximum_reference_errors = np.zeros(4)
        self.actual_cached_queries = self.actual_new_queries = 0
        return self

    def reference_at(self,cell,u):
        key = (int(cell),float(u).hex())
        definition = point_definition(self.nodes,cell,u)
        if key in self.reference_cache:
            value = self.reference_cache[key]
            self.actual_cached_queries += 1
        else:
            value = self.law.at(definition)
            self.reference_cache[key] = value
            self.actual_new_queries += 1
        self.maximum_reference_errors = np.maximum(self.maximum_reference_errors,value[1])
        return value

    def create_problem(self,*,N=2048,stage_block=64):
        require_actions()
        if N != 2048 or stage_block < 1:
            raise ValueError('This first independent entry retains the full original 2048 grid')
        context = self
        class CompleteReferenceObservations:
            def mixed_stage_weights(self,legacy_fraction=.5):
                return context.observed.ObservationMixin.mixed_stage_weights(self,legacy_fraction)
        q = CompleteReferenceObservations()
        q.axisymmetric_reference_context = self
        q.M,q.K,q.J = self.M,3,self.J
        q.mesh,q.R = self.mesh.copy(),self.radius
        q.P,q.legacy_P,q.full_N = len(self.plan.cells),self.plan.legacy_count,int(N)
        L = N//4
        q.N,q.phi = L+1,np.pi*np.arange(L+1)/(2*L)
        q.multiplicity = np.full(q.N,4.)
        q.multiplicity[[0,-1]] = 2.
        q.times,q.observation_cells,q.observation_u = self.plan.times.copy(),self.plan.cells.copy(),self.plan.local_u.copy()
        q.a,q.stage_block = self.a_observations.copy(),int(stage_block)
        q.stage_legacy_simpson_weights = self.plan.legacy_simpson_weights.copy()
        q.stage_quadrature_weights = self.plan.quadrature_weights.copy()
        return q,SimpleNamespace(core=self.core.copy(),height=self.height)

    def metadata(self):
        return dict(schema=SCHEMA,source_sha256=sha(__file__),definition=self.model,
            model_identity_sha256=self.identity,fixed_scalar_metric_identity_sha256=self.scalar_identity,
            input_records=self.input_records,full_scalar=self.full.metadata(),derivative_law=self.law.metadata(),
            actual_cached_scalar_queries=self.actual_cached_queries,actual_new_scalar_queries=self.actual_new_queries,
            maximum_reference_scalar_carrier_errors=self.maximum_reference_errors.tolist(),
            optimized_old_parent_required=False,historical_directions_replayed=False,
            complete_old_field_certificates_inherited=False,initial_height_is_free_variable=True)

class AxisymmetricMeridianJet:
    """True world T0,T0_s,T0_phi,T0_phiphi for the complete fixed scalar."""
    def __init__(self,problem,prepared,*,expected_bundle_sha256=None):
        require_actions()
        self.context = c = problem.axisymmetric_reference_context
        if (c.model.get('schema') != SCHEMA or c.model.get('source_sha256') != sha(__file__)
                or expected_bundle_sha256 != c.input_records['reference_bundle']['sha256']
                or not np.array_equal(prepared.core,c.core)):
            raise ValueError('Bind the independent whole-scalar reference and complete fixed chart')
        self.model,self.model_identity = c.model,c.identity
        self.core,self.height = c.core.copy(),c.height
        self.freq = 2*np.arange(1,c.M+1,dtype=float)
        self.binding = dict(schema=SCHEMA,source_sha256=sha(__file__),
            reference_bundle=c.input_records['reference_bundle'],
            reference_model_identity_sha256=c.identity,fixed_scalar_metric_identity_sha256=c.scalar_identity,
            source_binding={role:file_record(path,c.repo) for role,path in c.paths.items()},
            T0='a_s er(theta0)+c ez, c>=0, a_s^2+c^2=1',
            T0_s='a_ss er(theta0)+c_s ez; full original-prefix and R690 law',old_physical_q_field_used=False)

    def evaluate(self,cells,local,phi):
        require_actions()
        raw_cells,local,phi = np.asarray(cells),np.asarray(local),np.asarray(phi)
        if (raw_cells.ndim != 1 or local.shape != raw_cells.shape or phi.ndim != 1
                or not len(local) or not len(phi) or np.iscomplexobj(local) or np.iscomplexobj(phi)
                or not np.isfinite(raw_cells).all() or not np.isfinite(local).all() or not np.isfinite(phi).all()):
            raise ValueError('Use complete finite radial rows and independent angle vector')
        cells = raw_cells.astype(np.int64)
        if not np.array_equal(raw_cells,cells):
            raise ValueError('Cell addresses must be exact integers')
        values = np.array([self.context.reference_at(int(cell),float(u))[0] for cell,u in zip(cells,local)])
        b,c,bs,cs = values.T
        norm = np.sqrt(b*b+c*c)
        if not np.isfinite(norm).all() or np.any(norm <= 0):
            raise ArithmeticError('Complete meridian carrier must be nonzero')
        B,C = b/norm,c/norm
        ns = B*bs+C*cs
        Bs,Cs = (bs-B*ns)/norm,(cs-C*ns)/norm
        phi = np.asarray(phi,dtype=float)
        phase = phi[:,None]*self.freq[None]
        qfreq = 1-self.freq*self.freq
        theta = phi+np.sin(phase)@((qfreq/self.freq)*self.core)
        rho = 1+np.cos(phase)@(qfreq*self.core)
        rhop = -np.sin(phase)@(self.freq*qfreq*self.core)
        if not np.isfinite(rho).all() or np.any(rho <= 0):
            raise ValueError('Frozen warm-core chart fails positivity at requested angles')
        zero = np.zeros_like(theta)
        er = np.column_stack((np.cos(theta),np.sin(theta),zero))
        et = np.column_stack((-np.sin(theta),np.cos(theta),zero))
        ez = np.array([0.,0.,1.])
        result = dict(T0=B[:,None,None]*er[None]+C[:,None,None]*ez,
            T0_s=Bs[:,None,None]*er[None]+Cs[:,None,None]*ez,
            T0_phi=B[:,None,None]*(rho[:,None]*et)[None],
            T0_phiphi=B[:,None,None]*(rhop[:,None]*et-rho[:,None]**2*er)[None],
            norm=np.broadcast_to(norm[:,None],(len(cells),len(phi))),
            theta_parent=theta,rho_parent=rho,rho_phi_parent=rhop,
            metadata=dict(schema=SCHEMA,source_sha256=sha(__file__),reference_model_identity_sha256=self.model_identity,
                complete_true_scalar_used=True,independent_world_meridian=True,exact_definition_has_unit_speed=True,
                actual_carriers_normalized=True,numerical_normalization_and_trigonometric_errors_certified=False,
                old_physical_q_field_used=False))
        for value in result.values():
            if isinstance(value,np.ndarray):
                if not np.isfinite(value).all():
                    raise ArithmeticError('Nonfinite complete independent world meridian jet')
                value.setflags(write=False)
        return result


def indexed_grid(value):
    if isinstance(value,dict):
        if 'stage' in value and 'angle' in value and 'phi' not in value:
            return True
        return any(indexed_grid(v) for v in value.values())
    if isinstance(value,list):
        if value and isinstance(value[0],str) and value[0] in ('grid','grid_radius'):
            return True
        return any(indexed_grid(v) for v in value)
    return False

def historical_scalar_definition(data):
    profile = data['inward_scalar_profile']
    return dict(fixed_scalar_profile=data['fixed_scalar_profile'],
        analytic_extension_origin=data['analytic_extension_origin'],
        inward_parameters={key:profile[key] for key in
            ('cut','curvature','ramp_in','ramp_out','quadrature')},
        compact_curvature_pulse=profile['compact_curvature_pulse'])

def add_supplied_locations(locations,payload,*,path,node,scalar,angles):
    """Retain every supplied literal address, order/capacity metadata separately.

    The old capacities describe old selection policy, never a cap on new
    permanent storage. Historical indexed points bind the exact symbolic
    domain and the original scalar definition before chart reinterpretation.
    """
    origin = ('independent_reference_input',path.name)
    package = payload.get('schema') == 'a04-historical-location-parameters-v1'
    if package:
        topology = payload['topology']
        expected = dict(nodes=923,M=160,legacy_stages=1845,observed_stages=7377,full_angles=angles)
        if (any(topology.get(key)!=value for key,value in expected.items())
                or canonical(node['true_scalar_nodes']) != topology['symbolic_node_definitions_sha256']
                or canonical(historical_scalar_definition(scalar)) != topology['scalar_definition_sha256']):
            raise ValueError('Historical package requires the same exact original nodes, scalar, and angle/observation grids')
        records = payload['seeds']
        expected_names = ('legacy_memory','restore_grid','restore_local','witness_positive','witness_lowphi',
            'full13_curvature','full13_radius','r17_grid','r17_local','r17_fixed','continue_union')
        if tuple(records) != expected_names:
            raise ValueError('Retain the complete published ordered historical seed package')
        before = locations.occurrences
        summaries = []
        for name,record in records.items():
            value = record['payload']
            declared = value.get('full_angles',value.get('optimization_full_angles',angles))
            if int(declared) != angles:
                raise ValueError('Historical indexed angle grid differs: '+name)
            for key,expected_value in (('legacy_stages',1845),('total_stages',7377)):
                if key in value and int(value[key]) != expected_value:
                    raise ValueError('Historical observation plan differs: '+name)
            initial_occurrences = locations.occurrences
            for key,role in (('curvature_locations','curvature'),('radius_locations','radius'),
                             ('grid_curvature_locations','curvature'),('grid_radius_locations','radius')):
                for pair in value.get(key,[]):
                    if not isinstance(pair,list) or len(pair)!=2:
                        raise ValueError('Malformed ordered indexed position: '+name+'.'+key)
                    stage,angle = pair
                    if name == 'legacy_memory' and not 0 <= int(stage) < 1845:
                        raise ValueError('Historical legacy point must remain in the original retained prefix')
                    locations.grid(stage,locations.angle(angle),role,False,'.'.join(origin+(name,key)))
            role = 'radius' if name=='full13_radius' else ('curvature' if name in
                ('full13_curvature','witness_positive','witness_lowphi') else None)
            locations.walk(value,path=origin+(name,'payload'),role=role)
            summaries.append(dict(name=name,payload_schema=value.get('schema'),
                historical_source_sha256=record['historical_source_sha256'],
                original_payload_identity_sha256=canonical(value),
                original_record_identity_sha256=canonical(record),
                source_position_occurrences=locations.occurrences-initial_occurrences,
                curvature_capacity=value.get('curvature_capacity'),radius_capacity=value.get('radius_capacity'),
                protected_positions=len(value.get('protected_curvature_points',[])),
                full_payload_and_order_retained=True,capacity_used_to_drop_positions=False))
        return dict(kind='complete-published-a04-historical-package',input=file_record(path),
            original_topology=topology,actual_symbolic_nodes_sha256=canonical(node['true_scalar_nodes']),
            actual_original_scalar_definition_sha256=canonical(historical_scalar_definition(scalar)),
            exact_original_node_scalar_grid_binding=True,ordered_records=summaries,
            source_position_occurrences=locations.occurrences-before,
            original_payload=payload,
            later_runner_only_positions_included=False,
            scope='All 11 supplied payloads; no unavailable run1/run2 continuation report or raw position was inferred from its hash')
    declared_N = payload.get('N',payload.get('full_angles',payload.get('full_N')))
    if indexed_grid(payload) and (declared_N is None or int(declared_N)!=angles):
        raise ValueError('An indexed source must explicitly bind the unchanged full angle grid')
    if any(key in payload for key in ('curvature_locations','radius_locations','grid_curvature_locations','grid_radius_locations')):
        raise ValueError('Standalone old ordered-index memories require their complete bound historical package')
    before = locations.occurrences
    locations.walk(payload,path=origin)
    return dict(kind='explicit-supplied-full-report-or-literal-manifest',input=file_record(path),
        source_position_occurrences=locations.occurrences-before,original_payload=payload,
        all_original_payload_metadata_retained=True)

def prepare(args):
    require_actions()
    start = time.monotonic()
    repo,outdir = args.repo.resolve(),args.outdir.resolve()
    if outdir.exists() or outdir == repo or repo in outdir.parents:
        raise ValueError('Use fresh scientific output outside the repository')
    outdir.mkdir(parents=True)
    paths,modules = paths_and_modules(repo)
    node = json.loads(args.node_report.read_text())
    if (node.get('schema') != 'fullclosed-hold-real-pulse-warm-v1'
            or node.get('source_sha256') != SOURCE_PINS['warm_producer'][1]
            or node.get('bundle_sha256') != sha(args.warm_bundle)
            or node.get('input_sha256') != sha(args.scalar_input)
            or node.get('M') != 160 or node.get('J') != 923 or node.get('exact_core_affine') is not True):
        raise ValueError('Use the actual complete warm and its own exact scalar/node report')
    with np.load(args.warm_bundle,allow_pickle=False) as data:
        warm = {key:np.array(data[key],copy=True) for key in data.files}
    mesh = np.array(warm['mesh'],copy=True)
    if (mesh.shape != (923,) or warm['qjets'].shape != (923,3,482)
            or not np.isfinite(mesh).all() or not np.all(np.diff(mesh)>0)):
        raise ValueError('Keep every original node and its complete core')
    core = np.array(warm['qjets'][0,0,1:161],copy=True)
    if not np.array_equal(core[:3],warm['fixed_core_first3']):
        raise ValueError('The original fixed first three core words changed')
    raw = read_scalar(args.scalar_input)
    full = modules['scalar'].FullHold(raw,paths['integer'],paths['hold'],panels=args.panels)
    if full.carrier(full.S) != float(mesh[-1]) or full.carrier(full.R) != float(warm['radius']):
        raise ValueError('The actual warm endpoints differ from its own exact scalar')
    definitions = [(F(v['S_coefficient']),F(v['constant'])) for v in node['true_scalar_nodes']]
    width = float(warm['width'])
    if len(definitions) != 923 or definitions[0] != (F(0),F(0)) or definitions[-1] != (F(1),F(0)):
        raise ValueError('Keep every exact original affine symbolic node')
    breaks = [j for j,v in enumerate(definitions) if v == (F(1),-F(width))]
    if len(breaks) != 1:
        raise ValueError('The exact S-width observation breakpoint must remain unique')
    plan = modules['observed'].make_plan(mesh,width,order=6,lift_break_node=breaks[0])
    if len(plan.cells) != 7377 or plan.legacy_count != 1845:
        raise ValueError('Keep all 1845 legacy and 5532 Gauss observations')
    inputs = dict(scalar_input=sha(args.scalar_input),scalar_source=SOURCE_PINS['scalar'][1],
        integer_source=SOURCE_PINS['integer'][1],hold_source=SOURCE_PINS['hold'][1])
    deep = modules['deep_scalar'].DeepValleyTail(full,input_identity=inputs,
        epsilon=F(args.scalar_tail_cutoff),integral_tolerance=F(args.scalar_integral_tolerance),
        admission_seconds=args.scalar_admission_seconds)
    law = WholeAxisymmetricLaw(full,modules['deep_scalar'],tail_cutoff=args.scalar_tail_cutoff)
    a,ae,te = [],[],[]
    for index,(cell,u,tc) in enumerate(zip(plan.cells,plan.local_u,plan.times)):
        definition = point_definition(definitions,int(cell),float(u))
        value,error = midpoint_and_error(target_a_box(full,deep,modules['deep_scalar'],definition),modules['deep_scalar'].SCALE)
        a.append(value); ae.append(error)
        sb = full.affine_time(*definition)
        te.append(upper_float(max(abs(F(float(tc))-F(sb[0],full.h.S)),abs(F(float(tc))-F(sb[1],full.h.S)))))
        if (index+1)%1024 == 0:
            event(event='independent_axisymmetric_target_observations',completed=index+1,total=7377)
    a,ae,te = np.asarray(a),np.asarray(ae),np.asarray(te)
    if not np.isfinite(a).all() or np.any(a<=0):
        raise ArithmeticError('Each true fixed scalar observation needs a positive finite carrier')
    radius,radius_error = midpoint_and_error(deep.R,modules['deep_scalar'].SCALE)
    gx,gw = np.polynomial.legendre.leggauss(args.seed_integration_order)
    gu,gw = (gx+1)/2,gw/2
    cells,local = np.repeat(np.arange(922),args.seed_integration_order),np.tile(gu,922)
    addresses,cv,ce,seen = [],[],[],set()
    for cell,u in zip(np.r_[cells,plan.cells],np.r_[local,plan.local_u]):
        key = (int(cell),float(u).hex())
        if key in seen:
            continue
        seen.add(key)
        value,error = law.at(point_definition(definitions,int(cell),float(u)))
        addresses.append((int(cell),float(u))); cv.append(value); ce.append(error)
        if len(addresses)%1024 == 0:
            event(event='independent_axisymmetric_complete_meridian_scalars',completed=len(addresses))
    lookup = {(cell,u.hex()):v for (cell,u),v in zip(addresses,cv)}
    iv = np.array([lookup[(int(cell),float(u).hex())] for cell,u in zip(cells,local)])
    b,c = iv[:,0],iv[:,1]
    normalized_c = c/np.sqrt(b*b+c*c)
    height = float(np.sum(np.sum(normalized_c.reshape(922,args.seed_integration_order)*gw[None],axis=1)*np.diff(mesh)))
    if not math.isfinite(height):
        raise ArithmeticError('The explicit free-height seed is nonfinite')
    carrier_path = outdir/'observations.npz'
    np.savez_compressed(carrier_path,**plan.arrays(),mesh=mesh,a_stages=a[:1845],
        a_observations=a,a_observation_absolute_error=ae,observation_time_absolute_error=te,
        radius=np.array(radius),width=np.array(width),fixed_core_first3=core[:3],
        fixed_scalar_metric_identity_sha256=np.array(deep.model_identity_sha256))
    model = dict(schema=SCHEMA,source_sha256=sha(__file__),
        fixed_scalar_metric_identity_sha256=deep.model_identity_sha256,fixed_scalar_profile_definition=deep.definition,
        scalar_input_sha256=sha(args.scalar_input),original_scalar_parameters_identity_sha256=canonical(scalar_parameters(raw)),
        symbolic_node_report_sha256=sha(args.node_report),original_warm_bundle_sha256=sha(args.warm_bundle),
        observation_carrier_sha256=sha(carrier_path),mesh_sha256=array_sha(mesh),M=160,J=923,
        fixed_chart_core_sha256=array_sha(core),fixed_core_first3=[float(v).hex() for v in core[:3]],
        radius_carrier_hex=radius.hex(),radius_error_upper=radius_error,
        radius_definition='Exact R690 terminal radius, with a bound working carrier',
        radius_complete_enclosure=modules['deep_scalar'].enclosure(deep.R),
        a_observations_sha256=array_sha(a),working_scalar_tail_cutoff=str(F(args.scalar_tail_cutoff)),
        exact_domain='Original complete affine-in-S 923-node mesh and exact original S',
        frozen_chart='theta0(phi)=Theta_initial_warm_core(phi); every current free core may change',
        T0='a_s er(theta0)+c ez; c>=0,a_s^2+c^2=1; complete prefix/Hold/R690 law',
        T0_ports='T0(0)=ez; T0_s,z(0)=0; T0(S)=-er(theta0); T0_s(S)=0',
        fixed_metric='ds^2+a_deep(s)^2*dtheta0^2',
        old_optimized_q_field_required=False,old_nonlinear_directions_required=False,
        initial_height_rule='Working whole-cell Gauss integral of normalized c; free H, not an exact integral claim',
        seed_integration_order=int(args.seed_integration_order),all_original_free_core_coefficients_retained=True)
    reference_path = outdir/'reference.npz'
    np.savez_compressed(reference_path,schema=np.array(SCHEMA),mesh=mesh,initial_core=core,
        initial_height=np.array(height),original_warm_height=np.array(float(warm['Hcap'])),
        radius=np.array(radius),width=np.array(width),fixed_core_first3=core[:3],
        cached_scalar_cells=np.array([cell for cell,u in addresses],dtype=np.int64),
        cached_scalar_local=np.array([u for cell,u in addresses]),cached_scalar_values=np.asarray(cv),
        cached_scalar_errors=np.asarray(ce),
        reference_model_json=np.array(json.dumps(model,sort_keys=True,separators=(',',':'))),
        reference_model_identity_sha256=np.array(canonical(model)))
    locations = modules['history'].Locations(923,7377,args.angles)
    location_sources,location_provenance = [],[]
    for path in args.manifest:
        payload = json.loads(path.read_text())
        binding = add_supplied_locations(locations,payload,path=path,node=node,scalar=raw,angles=args.angles)
        location_provenance.append(binding)
        location_sources.append({key:value for key,value in binding.items() if key!='original_payload'})
    indexed = locations.resolve_grid(carrier_path)
    arrays = locations.arrays()
    provenance_path = outdir/'supplied-location-provenance.json'
    write_json(provenance_path,dict(schema='independent-axisymmetric-SO3-complete-supplied-history-v1',
        ordered_inputs=location_provenance,historical_capacities_are_not_new_storage_limits=True,
        actual_carrier_sha256=sha(carrier_path),actual_reference_bundle_sha256=sha(reference_path),
        legacy_angle_reinterpretation='literal old normal-angle value used as new frozen-chart phi0; not same physical point',
        inherited_geometric_values=False,unprovided_later_runner_reports_reconstructed=False))
    location_path = outdir/'locations.json'
    location_payload = dict(schema='independent-axisymmetric-SO3-literal-position-input-v1',
        carrier_sha256=sha(carrier_path),reference_bundle_sha256=sha(reference_path),
        N=args.angles,J=923,P=7377,source_inputs=location_sources,complete_supplied_provenance=file_record(provenance_path),
        curvature_points=arrays['curvature_points'],radius_points=arrays['radius_points'],
        protected_curvature_points=arrays['protected_curvature_points'],
        exact_location_summary=locations.summary(),resolved_grid_positions=indexed,
        legacy_angle_reinterpretation='literal old normal-angle value used as new frozen-chart phi0; not same physical point',
        only_supplied_positions_claimed_complete=True,old_geometry_values_transferred=False)
    write_json(location_path,location_payload)
    report = dict(schema=PREPARATION_SCHEMA,source_sha256=sha(__file__),
        source_commit=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip(),
        source_paths={role:str(path) for role,path in paths.items()},
        source_sha256_by_role={role:sha(path) for role,path in paths.items()},
        complete=True,N=args.angles,M=160,J=923,P=7377,
        old_warm_bundle=file_record(args.warm_bundle),old_warm_node_report=file_record(args.node_report),
        input_for_solver={role:file_record(path) for role,path in dict(reference_bundle=reference_path,
            carrier=carrier_path,node_report=args.node_report,scalar_input=args.scalar_input).items()},
        new_locations=file_record(location_path),complete_supplied_location_provenance=file_record(provenance_path),
        supplied_location_sources=location_sources,reference_model_identity_sha256=canonical(model),
        reference_definition=model,fixed_scalar_metric_identity_sha256=deep.model_identity_sha256,
        original_scalar_parameters_identity_sha256=model['original_scalar_parameters_identity_sha256'],
        true_scalar=deep.metadata(),whole_unit_meridian_law=law.metadata(),
        new_height=height,original_warm_height=float(warm['Hcap']),
        all_original_free_core_and_height_retained=True,initial_height_is_only_a_free_variable_seed=True,
        optimized_old_q_field_read_as_T0=False,original_positive_observations_and_angle_orbits_retained=True,
        historical_nonlinear_directions_replayed=False,old_certificates_inherited=False,
        exact_location_summary=locations.summary(),complete_same_field_metric_or_geometry_read=False,
        physical_new_field_still_requires_full_initial_read=True,complete_scalar_tail_included=True,
        seconds=time.monotonic()-start,
        execution=dict(repository=os.environ['GITHUB_REPOSITORY'],run_id=os.environ.get('GITHUB_RUN_ID'),
            run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'),workflow_trigger_commit=os.environ.get('GITHUB_SHA')))
    write_json(outdir/'report.json',report)
    event(event='independent_axisymmetric_reference_prepared',reference_sha256=sha(reference_path),
        carrier_sha256=sha(carrier_path),fixed_scalar_identity=deep.model_identity_sha256,
        reference_identity=canonical(model),original_scalar_parameters_identity=report['original_scalar_parameters_identity_sha256'],
        M=160,J=923,P=7377,N=args.angles,height=height,curvature_positions=len(arrays['curvature_points']),
        radius_positions=len(arrays['radius_points']),report_sha256=sha(outdir/'report.json'),seconds=report['seconds'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo','warm-bundle','node-report','scalar-input','outdir'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--manifest',type=Path,action='append',default=[])
    parser.add_argument('--angles',type=int,default=2048)
    parser.add_argument('--seed-integration-order',type=int,default=8)
    parser.add_argument('--panels',type=int,default=128)
    parser.add_argument('--scalar-admission-seconds',type=float,default=300.)
    parser.add_argument('--scalar-integral-tolerance',default='1e-18')
    parser.add_argument('--scalar-tail-cutoff',default='1/8')
    args = parser.parse_args()
    if args.angles!=2048 or args.seed_integration_order<4 or args.panels<1 or args.scalar_admission_seconds<=0:
        raise ValueError('Use the full original grid and positive declared scalar/integration budgets')
    prepare(args)
