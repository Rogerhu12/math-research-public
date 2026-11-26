#!/usr/bin/env python3
"""Complete finite geometry and all original selected rows for the SO3 field.

The physical field is the NEW R696 centered angular-unit representation, evaluated
through its actual world six-jet and full-variable transpose.  Only the
coordinate-independent curvature differential and the unchanged e783 working
set selector are reused.  No R671 point pullback or old-field certificate is
relabelled.  All scientific entry points require the public Actions runner.
"""
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
import mmap
import os
from pathlib import Path
import sys
from types import SimpleNamespace

import numpy as np


SCHEMA = 'complete-R696-angular-unit-world-geometry-and-original-192-amplitude-rows-v1'
OPERATOR_SCHEMA = 'complete-R696-angular-unit-centered-field-v1'
ANGULAR_OPERATOR_SHA256 = 'd2f8a93c3356fc172e5c6ac365b0bff65660fea2bb3bf8350ab124537a0f4a14'
PURE_GEOMETRY_SHA256 = 'a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854'
SELECTOR_SHA256 = 'e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8'
REFERENCE_JET_SHA256 = '4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3'
KEYS = ('F', 'Fs', 'Fphi', 'Fss', 'Fsphi', 'Fphiphi')
MARKER_HEIGHT_EXACT = Fraction(1, 1000)


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific SO3 geometry requires the public repository Actions')


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def array_sha(value):
    value = np.ascontiguousarray(value)
    h = hashlib.sha256(str(value.dtype).encode())
    h.update(json.dumps(list(value.shape)).encode())
    h.update(value.tobytes())
    return h.hexdigest()


def load_source(path, expected):
    path = Path(path).resolve()
    if sha(path) != expected:
        raise ValueError('The complete reused source differs: '+str(path))
    name = 'so3_geometry_dependency_'+expected
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _round_fraction(value, *, upward):
    rounded = float(value)
    exact = Fraction.from_float(rounded)
    if (upward and exact < value) or (not upward and exact > value):
        rounded = math.nextafter(rounded, math.inf if upward else -math.inf)
    return rounded


@dataclass(frozen=True)
class Budgets:
    """Immutable marked/body/held budgets for the actual NEW physical field.

    Scalar roundings are directed, but field evaluations remain numerical.
    R is this same frozen deep scalar profile's terminal radius carrier.
    """
    marked_diameter_budget: float
    witness_lower_budget: float
    cap_radius: float
    height_floor: float

    def __post_init__(self):
        for name in ('marked_diameter_budget', 'witness_lower_budget',
                     'cap_radius', 'height_floor'):
            value = float(getattr(self, name))
            if not math.isfinite(value):
                raise ValueError('All fixed amplitude budgets must be finite')
            object.__setattr__(self, name, value)
        D, L, R, H = (Fraction.from_float(getattr(self, name)) for name in
            ('marked_diameter_budget', 'witness_lower_budget', 'cap_radius', 'height_floor'))
        if not 2*MARKER_HEIGHT_EXACT < D <= Fraction(9, 2):
            raise ValueError('Need 2h < marked D <= 4.5 for the fixed diameter-0.9 grip')
        if L <= 0 or 5*L < D:
            raise ValueError('The held-witness lower budget must be at least marked D/5')
        if R <= Fraction(9, 20):
            raise ValueError('The fixed same-profile cap must contain the radius-0.45 grip')
        if H <= 1:
            raise ValueError('An explicit fixed height floor greater than 1 is required')

    @property
    def body_diameter_budget(self):
        return _round_fraction(Fraction.from_float(self.marked_diameter_budget)
                               - 2*MARKER_HEIGHT_EXACT, upward=False)

    @property
    def amplitude_height_floor(self):
        return _round_fraction(Fraction.from_float(self.witness_lower_budget)
                               + MARKER_HEIGHT_EXACT, upward=True)

    @property
    def effective_height_floor(self):
        return max(self.height_floor, self.amplitude_height_floor)

    def metadata(self):
        return dict(marked_diameter_budget=self.marked_diameter_budget,
            body_diameter_budget=self.body_diameter_budget,
            witness_lower_budget=self.witness_lower_budget,
            cap_radius=self.cap_radius, cap_radius_carrier_hex=self.cap_radius.hex(),
            height_floor=self.height_floor,
            amplitude_height_floor=self.amplitude_height_floor,
            effective_height_floor=self.effective_height_floor,
            marker_height_exact='1/1000', fixed_grip_diameter=0.9,
            body_budget_rounding='downward from exact binary64 marked D minus 2/1000',
            amplitude_height_rounding='upward from exact binary64 L plus 1/1000',
            fixed_during_direction_and_all_trial_reads=True,
            cap_radius_scope='same frozen deep-profile terminal radius; no free R variable',
            scope='Design constraints for the chosen whole-image witness; finite values are not continuous certificates')


def _key(location):
    return (int(location['cell']), float(location['u']).hex(), float(location['phi']).hex())


def _discard(matrix):
    if (isinstance(matrix, np.memmap) and hasattr(matrix._mmap, 'madvise')
            and hasattr(mmap, 'MADV_DONTNEED')):
        matrix._mmap.madvise(mmap.MADV_DONTNEED)


class GeometryScreen:
    def __init__(self, problem, repo, budgets, *, reach_ratio=.03,
                 reach_safety_factor=.992, amplitude_top_radius=2,
                 amplitude_top_distance=4):
        require_actions()
        self.q = problem
        self.repo = Path(repo).resolve()
        self.budgets = budgets
        if not isinstance(budgets, Budgets):
            raise TypeError('Use one immutable Budgets instance for the whole continuation')
        if float(problem.R).hex() != budgets.cap_radius.hex():
            raise ValueError('Amplitude R must be the actual unchanged scalar-profile R')
        self.reach_ratio = float(reach_ratio)
        self.safety = float(reach_safety_factor)
        if not (0 < self.reach_ratio < 1 and 0 < self.safety < 1):
            raise ValueError('Use explicit positive reach ratio and numerical safety below one')
        self.amplitude_top_radius = int(amplitude_top_radius)
        self.amplitude_top_distance = int(amplitude_top_distance)
        if (self.amplitude_top_radius != amplitude_top_radius
                or self.amplitude_top_distance != amplitude_top_distance
                or not 1 <= self.amplitude_top_radius <= 2
                or not 1 <= self.amplitude_top_distance <= 4):
            raise ValueError('Use at most two radius and four paired-distance working locations')
        model = problem.model
        if (model.get('schema') != OPERATOR_SCHEMA
                or model.get('source_sha256') != ANGULAR_OPERATOR_SHA256
                or model.get('reference_meridian_kernel_sha256') != REFERENCE_JET_SHA256
                or model.get('all_current_free_core_coefficients_retained') is not True
                or model.get('current_height_free') is not True
                or model.get('radial_Gram_error_identically_zero') is not False
                or model.get('angular_Gram_error_identically_zero') is not True
                or model.get('closed_angular_sections_identically') is not True
                or model.get('all_free_radial_profile_jets_retained') is not True
                or model.get('vertical_profile', {}).get('r_independent_of_angle') is not True):
            raise ValueError('Use the complete R696 centered angular field and its independent radial profile')
        self.operator_sha256 = model['source_sha256']
        for name in ('grid_fields', 'point_fields', 'point_vjp', 'prepare', 'domain'):
            method = getattr(problem, name)
            path = Path(method.__code__.co_filename).resolve()
            if sha(path) != self.operator_sha256:
                raise ValueError('Actual new-field entry differs from its bound model: '+name)
        if canonical(model) != problem.identity:
            raise ValueError('The actual complete SO3 model identity differs')
        if (int(problem.K) != 3 or int(problem.core_size) != int(problem.M)-3
                or int(problem.profile_size) != 3*int(problem.J)-6
                or int(problem.rotation_size) != (2*(int(problem.M)+1)*(3*int(problem.J)-6)
                                                  +int(problem.M)*(3*int(problem.J)-5))
                or int(problem.free_size) != (int(problem.core_size)+int(problem.rotation_size)
                                              +int(problem.profile_size)+1)):
            raise ValueError('Keep every free core, rotation, radial-profile coordinate and final H')
        scripts = self.repo/'topics/visible-flex-larger-amplitude/scripts'
        self.pure = load_source(scripts/'resume_20261120_curvature_qp.py',
                                PURE_GEOMETRY_SHA256)
        self.selector = load_source(scripts/'resume_20261120/fullclosed_point_inequalities_v2.py',
                                    SELECTOR_SHA256)
        # The old selector's observed_module is passed only to our new point
        # shim. Its original physical field/point functions are never called.
        self.observed_marker = SimpleNamespace(
            schema='actual-R696-angular-unit-world-point-shim-v1',
            operator_source_sha256=self.operator_sha256)
        self._curvature_memory = {}
        self._radius_memory = {}
        self._x = None
        self._prepared = None
        self._token = None
        self._field_cache = {}
        self._grid = None
        self._last_scan = None
        self._radial_index = {}
        for i, (cell, u) in enumerate(zip(problem.observation_cells, problem.observation_u)):
            self._radial_index.setdefault((int(cell), float(u).hex()), int(i))
        self._angle_index = {float(phi).hex(): int(i) for i, phi in enumerate(problem.phi)}
        if len(self._angle_index) != int(problem.N):
            raise ValueError('The actual angular observation carrier has duplicate literal angles')
        self.binding = dict(schema=SCHEMA, source_sha256=sha(__file__),
            operator_source_sha256=self.operator_sha256,
            actual_model_identity_sha256=problem.identity,
            pure_curvature_source_sha256=PURE_GEOMETRY_SHA256,
            unchanged_original_selector_sha256=SELECTOR_SHA256,
            physical_pullback='actual complete R696 point_vjp in world coordinates, including every radial-profile slot',
            old_R671_point_pullback_used=False, old_geometry_certificate_inherited=False,
            budgets=budgets.metadata(), reach_ratio=self.reach_ratio,
            numerical_reach_safety_factor=self.safety,
            quarter_completion='exact x/y reflection parity of the new omega and frozen chart; both witness signs are read',
            lower_half_completion='z reflection; absolute curvature, radius and distances to the equatorial witness are invariant',
            scientific_evaluation_environment='public repository Actions',
            coordinate_semantics='cell/u on the unchanged symbolic radial mesh; phi is the NEW fixed-parent chart coordinate phi0',
            historical_angle_reinterpretation='every literal legacy normal-angle value is read as new phi0; no claim of the same physical point across representations',
            historical_physical_values_or_certificates_transferred=False,
            current_normal_angle='operator solves Theta_current(phi_c)=Theta_frozen_parent(phi0); all free core derivatives retained, root errors not certified')

    def _set_x(self, x):
        require_actions()
        x = np.asarray(x, dtype=float)
        if x.shape != (self.q.free_size,) or not np.isfinite(x).all():
            raise ValueError('Use the actual finite complete new-field point')
        if self._x is not None and np.array_equal(x, self._x):
            return
        prepared = self.q.prepare(x)
        if (np.asarray(prepared.core).shape != (self.q.M,)
                or not np.array_equal(prepared.core[self.q.K:], x[:self.q.core_size])
                or float(prepared.height) != float(x[-1])):
            raise ValueError('Current core and H do not match the complete new-field point')
        self._x = x.copy()
        self._prepared = prepared
        self._token = array_sha(x)
        self._field_cache = {}
        self._grid = None
        self._last_scan = None

    def _location(self, value):
        if 'cell' in value:
            cell, u, phi = int(value['cell']), float(value['u']), float(value['phi'])
        else:
            stage, angle = int(value['stage']), int(value['angle'])
            if not 0 <= stage < self.q.P or not 0 <= angle < self.q.N:
                raise ValueError('A requested grid location is outside the actual observation carrier')
            cell, u = int(self.q.observation_cells[stage]), float(self.q.observation_u[stage])
            phi = float(self.q.phi[angle])
        if (not 0 <= cell < self.q.J-1 or not 0 <= u <= 1
                or not math.isfinite(u) or not math.isfinite(phi)):
            raise ValueError('Use an actual same-mesh literal binary64 location')
        return dict(cell=cell, u=u, phi=phi, protected=bool(value.get('protected', False)))

    def _remember(self, values, memory):
        for value in values:
            item = self._location(value)
            key = _key(item)
            if key in memory:
                memory[key]['protected'] = bool(memory[key].get('protected', False)
                                                or item.get('protected', False))
            else:
                memory[key] = item

    def _grid_location(self, stage, angle, **metadata):
        result = self._location(dict(stage=int(stage), angle=int(angle)))
        result.update(stage=int(stage), angle=int(angle),
                      s=float(self.q.times[int(stage)]))
        result.update(metadata)
        return result

    def _validate_fields(self, fields, shape):
        if (not set(KEYS).issubset(fields)
                or set(fields)-set(KEYS)-{'rho0', 'closure_delta'}):
            raise ValueError('Every new world field query must return the complete six jets')
        # grid_fields also reports its true chart and closure diagnostics.
        # They are checked, but are not mistaken for physical six-jet slots.
        for name in set(fields)-set(KEYS):
            extra = np.asarray(fields[name], dtype=float)
            expected = ((shape[-2],) if name == 'rho0' else (shape[-2], 3))
            if len(shape) != 3 or extra.shape != expected or not np.isfinite(extra).all():
                raise FloatingPointError('Invalid complete-field diagnostic: '+name)
        result = {}
        for name in KEYS:
            value = np.asarray(fields[name], dtype=float)
            if value.shape != shape or not np.isfinite(value).all():
                raise FloatingPointError('Nonfinite or incomplete actual world six-jet: '+name)
            result[name] = value
        return result

    def _point(self, location):
        item = self._location(location)
        key = _key(item)
        if key not in self._field_cache:
            fields = self.q.point_fields(self._x, item['cell'], item['u'], item['phi'])
            fields = self._validate_fields(fields, (3,))
            self._field_cache[key] = {name: value.copy() for name, value in fields.items()}
        return self._field_cache[key]

    def _point_geometry(self, fields):
        V, W = fields['Fs'], fields['Fphi']
        area = float(np.linalg.norm(np.cross(V, W)))
        if not math.isfinite(area) or area <= 0:
            raise FloatingPointError('An actually requested point has nonpositive tangent area')
        values = [self.pure.curvature_cotangent(fields, branch)[0] for branch in (0, 1)]
        radius = float(np.linalg.norm(fields['F']))
        if not np.isfinite(values).all() or not math.isfinite(radius):
            raise FloatingPointError('Nonfinite actual point curvature or radius')
        return values, radius, area

    def _amplitude_values(self, fields):
        F = fields['F']
        B, L = self.budgets.body_diameter_budget, self.budgets.witness_lower_budget
        r0 = 1.+np.sum(self._prepared.core)
        if not np.isfinite(r0):
            raise FloatingPointError('The complete current witness radius is not finite')
        squared = np.sum(F*F, axis=-1)
        result = {'body_diameter': 4*squared/(B*B)-1}
        for sign, name in ((1, 'distance_plus'), (-1, 'distance_minus')):
            delta = np.array(F, copy=True)
            delta[..., 1] -= sign*r0
            result[name] = 1-np.sum(delta*delta, axis=-1)/(L*L)
        if any(not np.isfinite(value).all() for value in result.values()):
            raise FloatingPointError('Nonfinite true same-field amplitude values')
        return result

    def _scalar_values(self):
        H = float(self._prepared.height)
        B, L = self.budgets.body_diameter_budget, self.budgets.witness_lower_budget
        result = dict(cap_diameter=4*(self.q.R*self.q.R+H*H)/(B*B)-1,
                      height_floor=(self.budgets.effective_height_floor-H)/L)
        if not np.isfinite(list(result.values())).all():
            raise FloatingPointError('Nonfinite same-field scalar amplitude values')
        return result

    @staticmethod
    def _offer(pool, location, score, count, **data):
        key = _key(location)
        item = dict(location=location, score=float(score), **data)
        if key not in pool or item['score'] > pool[key]['score']:
            pool[key] = item
        if len(pool) > count:
            kept = sorted(pool, key=lambda k: pool[k]['score'], reverse=True)[:count]
            for old in tuple(pool):
                if old not in kept:
                    del pool[old]

    def _block_candidates(self, values, begin, count):
        # All values have already participated in the full finite maximum.
        # Adaptive top selection affects only the bounded linear working set.
        flat = np.asarray(values).ravel()
        take = min(len(flat), max(64, 8*count))
        while True:
            indices = np.argpartition(flat, len(flat)-take)[-take:]
            indices = indices[np.argsort(flat[indices])[::-1]]
            output, keys = [], set()
            for index in indices:
                stage, local_angle = np.unravel_index(int(index), values.shape)
                location = self._grid_location(stage, begin+local_angle)
                key = _key(location)
                if key not in keys:
                    keys.add(key)
                    output.append((location, float(flat[index]), int(stage), int(local_angle)))
                    if len(output) == count:
                        return output
            if take == len(flat):
                return output
            take = min(len(flat), 2*take)

    def _ensure_grid(self):
        if self._grid is not None:
            return
        domain = self.q.domain(self._x)
        q = self.q
        kappas = np.empty((q.P, q.N, 2))
        radii = np.empty((q.P, q.N))
        covered = np.zeros(q.N, dtype=bool)
        minimum_area = math.inf
        max_body = max_plus = max_minus = -math.inf
        radius_pool, distance_pool = {}, {}
        # Every inherited literal grid address is read directly from its
        # already required full block, avoiding repeated meridian integrals.
        needed = {}
        for item in list(self._curvature_memory.values())+list(self._radius_memory.values()):
            stage = self._radial_index.get((item['cell'], float(item['u']).hex()))
            angle = self._angle_index.get(float(item['phi']).hex())
            if stage is not None and angle is not None:
                needed.setdefault(angle, []).append((stage, _key(item)))
        blocks = 0
        for begin, end, supplied in q.grid_fields(self._x):
            begin, end = int(begin), int(end)
            if not 0 <= begin < end <= q.N or np.any(covered[begin:end]):
                raise ValueError('The complete new-field angular blocks overlap or leave their domain')
            z = self._validate_fields(supplied, (q.P, end-begin, 3))
            V, W = z['Fs'], z['Fphi']
            cross = np.cross(V, W)
            area = np.sqrt(np.sum(cross*cross, axis=-1))
            if not np.isfinite(area).all() or np.any(area <= 0):
                raise FloatingPointError('A full-grid world tangent area is nonpositive or nonfinite')
            minimum_area = min(minimum_area, float(np.min(area)))
            normal = cross/area[..., None]
            E, F, G = np.sum(V*V, axis=-1), np.sum(V*W, axis=-1), np.sum(W*W, axis=-1)
            e = np.sum(normal*z['Fss'], axis=-1)
            f = np.sum(normal*z['Fsphi'], axis=-1)
            g = np.sum(normal*z['Fphiphi'], axis=-1)
            determinant = area*area
            trace = (e*G+g*E-2*f*F)/determinant
            gauss = (e*g-f*f)/determinant
            gap = np.sqrt(np.maximum(0., trace*trace-4*gauss))
            block_k = np.stack(((trace-gap)/2, (trace+gap)/2), axis=-1)
            block_r = np.sqrt(np.sum(z['F']*z['F'], axis=-1))
            if not np.isfinite(block_k).all() or not np.isfinite(block_r).all():
                raise FloatingPointError('A full-grid curvature or radius is nonfinite')
            kappas[:, begin:end] = block_k
            radii[:, begin:end] = block_r
            av = self._amplitude_values(z)
            max_body = max(max_body, float(np.max(av['body_diameter'])))
            max_plus = max(max_plus, float(np.max(av['distance_plus'])))
            max_minus = max(max_minus, float(np.max(av['distance_minus'])))
            paired = np.maximum(av['distance_plus'], av['distance_minus'])
            for family, values, count, pool in (
                ('body_diameter', av['body_diameter'], self.amplitude_top_radius, radius_pool),
                ('witness_distance', paired, self.amplitude_top_distance, distance_pool)):
                for loc, score, stage, local_angle in self._block_candidates(values, begin, count):
                    self._offer(pool, loc, score, count, kind=family)
                    self._field_cache[_key(loc)] = {
                        name: value[stage, local_angle].copy() for name, value in z.items()}
            for angle in range(begin, end):
                for stage, key in needed.get(angle, ()):
                    self._field_cache[key] = {name: value[stage, angle-begin].copy()
                                              for name, value in z.items()}
            covered[begin:end] = True
            blocks += 1
        if not covered.all():
            raise ValueError('The actual full-grid angular coverage is incomplete')
        worst = tuple(int(v) for v in np.unravel_index(np.argmax(np.abs(kappas)), kappas.shape))
        farthest = tuple(int(v) for v in np.unravel_index(np.argmax(radii), radii.shape))
        K = float(abs(kappas[worst]))
        radius = float(radii[farthest])
        diameter = max(2., 2*abs(float(self._prepared.height)), 2*radius)
        scan = dict(complete=True, maximum_absolute_principal_curvature=K,
            maximum_radius=radius, diameter_point_lower=diameter,
            necessary_reach_product=self.reach_ratio*diameter*K,
            min_area=minimum_area, worst=self._grid_location(*worst[:2], branch=worst[2]),
            farthest=self._grid_location(*farthest), point_count=int(q.P*q.N),
            observed_stages=int(q.P), angular_orbits=int(q.N), angular_blocks=blocks,
            every_requested_grid_point_read=True, angular_coverage_complete=True,
            continuous_geometry_certified=False, domain=domain)
        self._grid = dict(kappas=kappas, radii=radii, summary=scan,
            radius_pool=radius_pool, distance_pool=distance_pool,
            maximum_body_g=max_body, maximum_plus_g=max_plus, maximum_minus_g=max_minus)

    def _new_locations(self, supplied, memory):
        keys = {_key(self._location(value)) for value in supplied}
        # Also return protected upgrades, with no rounding or memory eviction.
        old_protected = {_key(self._location(value)) for value in supplied if value.get('protected', False)}
        return [dict(value) for key, value in memory.items()
                if key not in keys or (value.get('protected', False) and key not in old_protected)]

    def scan(self, x, witnesses=(), radius_witnesses=()):
        require_actions()
        witnesses, radius_witnesses = list(witnesses), list(radius_witnesses)
        self._remember(witnesses, self._curvature_memory)
        self._remember(radius_witnesses, self._radius_memory)
        try:
            self._set_x(x)
            self._ensure_grid()
            grid = self._grid
            curvature_locations = self.pure.pick_extremes(grid['kappas'], 16, branches=True)
            radius_locations = self.pure.pick_extremes(grid['radii'], 2)
            new_curv = [self._grid_location(s, a) for s, a, _ in curvature_locations]
            new_curv.append(grid['summary']['worst'])
            new_rad = [self._grid_location(s, a) for s, a in radius_locations]
            new_rad.append(grid['summary']['farthest'])
            new_rad.extend(item['location'] for item in grid['radius_pool'].values())
            new_rad.extend(item['location'] for item in grid['distance_pool'].values())
            self._remember(new_curv, self._curvature_memory)
            self._remember(new_rad, self._radius_memory)
            union = dict(self._curvature_memory)
            union.update(self._radius_memory)
            K = float(grid['summary']['maximum_absolute_principal_curvature'])
            radius = float(grid['summary']['maximum_radius'])
            minimum_area = float(grid['summary']['min_area'])
            worst, farthest = grid['summary']['worst'], grid['summary']['farthest']
            max_body = float(grid['maximum_body_g'])
            max_plus, max_minus = float(grid['maximum_plus_g']), float(grid['maximum_minus_g'])
            radius_pool = dict(grid['radius_pool'])
            distance_pool = dict(grid['distance_pool'])
            point_records = []
            for location in union.values():
                fields = self._point(location)
                values, point_radius, area = self._point_geometry(fields)
                branch = int(np.argmax(np.abs(values)))
                value = abs(float(values[branch]))
                if value > K:
                    K, worst = value, dict(location, branch=branch)
                if point_radius > radius:
                    radius, farthest = point_radius, dict(location)
                minimum_area = min(minimum_area, area)
                av = self._amplitude_values(fields)
                max_body = max(max_body, float(av['body_diameter']))
                max_plus = max(max_plus, float(av['distance_plus']))
                max_minus = max(max_minus, float(av['distance_minus']))
                self._offer(radius_pool, location, av['body_diameter'],
                            self.amplitude_top_radius, kind='body_diameter')
                self._offer(distance_pool, location, max(av['distance_plus'], av['distance_minus']),
                            self.amplitude_top_distance, kind='witness_distance')
                point_records.append(dict(location=location,
                    signed_principal_curvatures=[float(v) for v in values],
                    radius=point_radius, area=area,
                    amplitude={key: float(value) for key, value in av.items()}))
            self._remember([worst], self._curvature_memory)
            self._remember([farthest], self._radius_memory)
            self._remember([item['location'] for item in radius_pool.values()], self._radius_memory)
            self._remember([item['location'] for item in distance_pool.values()], self._radius_memory)
            diameter = max(2., 2*abs(float(self._prepared.height)), 2*radius)
            product = self.reach_ratio*diameter*K
            scalar = self._scalar_values()
            maximum_g = max(product-self.safety, max_body, max_plus, max_minus, *scalar.values())
            if not math.isfinite(maximum_g):
                raise FloatingPointError('Nonfinite complete actual physical inequality maximum')
            result = dict(schema=SCHEMA, complete=True, passed=bool(maximum_g <= 0),
                current_full_point_sha256=self._token,
                actual_model_identity_sha256=self.q.identity,
                maximum_physical_g=float(maximum_g),
                maximum_absolute_principal_curvature=K, maximum_radius=radius,
                diameter_point_lower=diameter, necessary_reach_product=product,
                reach_physical_g=product-self.safety, min_area=minimum_area,
                worst=worst, farthest=farthest, current_height=float(self._prepared.height),
                current_witness_radius=float(1.+np.sum(self._prepared.core)),
                grid=grid['summary'], permanent_unique_locations_read=len(union),
                permanent_curvature_locations=len(self._curvature_memory),
                permanent_radius_locations=len(self._radius_memory),
                all_permanent_curvature_and_radius_locations_read=True,
                all_six_world_jets_read=True, both_witness_signs_read_at_every_point=True,
                amplitude=dict(complete=True, body_diameter=max_body,
                    distance_plus=max_plus, distance_minus=max_minus, **scalar,
                    radius_working_candidates=sorted(radius_pool.values(), key=lambda v: -v['score']),
                    distance_working_candidates=sorted(distance_pool.values(), key=lambda v: -v['score']),
                    budgets=self.budgets.metadata()),
                new_curvature_locations=self._new_locations(witnesses, self._curvature_memory),
                new_radius_locations=self._new_locations(radius_witnesses, self._radius_memory),
                continuous_geometry_certified=False, continuous_metric_certified=False,
                rigorous_quadrature_or_root_errors_paid=False,
                old_continuous_certificates_inherited=False,
                source_binding=self.binding)
            # Detailed same-field witness values remain a small runner report,
            # not scientific raw arrays. Every exact address is preserved.
            result['permanent_point_records'] = point_records
            self._last_scan = result
            return result
        except (ValueError, FloatingPointError, OverflowError, np.linalg.LinAlgError) as error:
            self._grid = None
            self._last_scan = None
            return dict(schema=SCHEMA, complete=False, passed=False,
                current_full_point_sha256=None,
                actual_model_identity_sha256=self.q.identity,
                maximum_physical_g=None, error_type=type(error).__name__, error=str(error),
                new_curvature_locations=self._new_locations(witnesses, self._curvature_memory),
                new_radius_locations=self._new_locations(radius_witnesses, self._radius_memory),
                all_permanent_curvature_and_radius_locations_read=False,
                continuous_geometry_certified=False, old_continuous_certificates_inherited=False)

    # ----- Explicit NEW physical shims for the unchanged original selector.
    def scan_geometry(self, problem, x, *, top_curvature=16, top_radius=2):
        if problem is not self.q:
            raise ValueError('Original selector received a different physical problem')
        self._set_x(x)
        self._ensure_grid()
        return (dict(self._grid['summary']),
            self.pure.pick_extremes(self._grid['kappas'], top_curvature, branches=True),
            self.pure.pick_extremes(self._grid['radii'], top_radius))

    def single_fields(self, problem, prepared, stage, angle):
        self._check_prepared(problem, prepared)
        return self._point(self._grid_location(stage, angle))

    def curvature_cotangent(self, fields, branch):
        return self.pure.curvature_cotangent(fields, branch)

    def _check_prepared(self, problem, prepared):
        if problem is not self.q or not np.array_equal(prepared.x, self._x):
            raise ValueError('A point query or covector crossed the actual same-parent boundary')

    def fields_at(self, problem, prepared, cell, u, phi, observed_module):
        self._check_prepared(problem, prepared)
        if observed_module is not self.observed_marker:
            raise ValueError('Use the explicit new world-point shim')
        return self._point(dict(cell=cell, u=u, phi=phi))

    def pullback(self, problem, prepared, stage, angle, cotangent):
        self._check_prepared(problem, prepared)
        location = self._grid_location(stage, angle)
        return self._pullback(location, cotangent)

    def pullback_at(self, problem, prepared, cell, u, phi, cotangent, observed_module):
        self._check_prepared(problem, prepared)
        if observed_module is not self.observed_marker:
            raise ValueError('Use the explicit new world-point shim')
        return self._pullback(dict(cell=cell, u=u, phi=phi), cotangent)

    def _pullback(self, location, cotangent):
        item = self._location(location)
        cotangent = self._validate_fields(cotangent, (3,))
        gradient = np.asarray(self.q.point_vjp(self._x, item['cell'], item['u'], item['phi'],
                                             cotangent), dtype=float)
        if gradient.shape != (self.q.free_size,) or not np.isfinite(gradient).all():
            raise FloatingPointError('The new world pullback omitted a free variable or is nonfinite')
        return gradient

    def _amplitude_row(self, kind, location=None, sign=None):
        gradient = np.zeros(self.q.free_size)
        B, L = self.budgets.body_diameter_budget, self.budgets.witness_lower_budget
        if kind in ('cap_diameter', 'height_floor'):
            value = self._scalar_values()[kind]
            gradient[-1] = (8*self._prepared.height/(B*B) if kind == 'cap_diameter' else -1/L)
            return float(value), gradient, dict(kind=kind, only_final_height_coordinate=True,
                fixed_cap_radius_has_no_free_derivative=True)
        location = self._location(location)
        fields = self._point(location)
        F = fields['F']
        cot = {name: np.zeros(3) for name in KEYS}
        values = self._amplitude_values(fields)
        if kind == 'body_diameter':
            value = float(values[kind])
            cot['F'] = 8*F/(B*B)
            gradient = self._pullback(location, cot)
        elif kind == 'witness_distance':
            if sign not in (-1, 1):
                raise ValueError('A distance derivative must keep its actual witness sign')
            w = F.copy()
            w[1] -= sign*(1.+np.sum(self._prepared.core))
            value = float(values['distance_plus' if sign == 1 else 'distance_minus'])
            cot['F'] = -2*w/(L*L)
            gradient = self._pullback(location, cot)
            # p=(0,1+sum ALL current core coefficients,0) in WORLD coordinates.
            # Every original FREE core entry changes p_y by one. This term is
            # added before the full H2 coordinate transpose, never after it.
            gradient[:self.q.core_size] += 2*sign*w[1]/(L*L)
        else:
            raise ValueError('Unknown actual amplitude inequality')
        return value, gradient, dict(kind=kind, location=location, sign=sign,
            witness_formula='p=(0,1+sum_all_current_core,0)',
            full_free_core_witness_derivative_added=(kind == 'witness_distance'),
            witness_derivative_added_before_coordinate_transpose=True)

    def build_rows(self, x, transpose, coordinate_size, *, witnesses=(),
                   radius_witnesses=(), current_geometry=None, matrix_workdir=None,
                   max_rows=192, active_band=.025, block_columns=32768):
        require_actions()
        if int(coordinate_size) != coordinate_size or coordinate_size != self.q.free_size:
            raise ValueError('Retain all full SO3 H2 coordinates in every selected row')
        if int(max_rows) != 192:
            raise ValueError('The complete original selector must keep its declared 192-row cap')
        if not math.isfinite(float(active_band)) or active_band <= 0:
            raise ValueError('Use a positive declared linear working-set activity band')
        if int(block_columns) != block_columns or block_columns <= 0:
            raise ValueError('Use a positive streamed column block size')
        self._set_x(x)
        if current_geometry is not None:
            if (current_geometry.get('current_full_point_sha256') != self._token
                    or current_geometry.get('actual_model_identity_sha256') != self.q.identity):
                raise ValueError('The supplied true scan belongs to a different complete parent')
        actual = self.scan(x, witnesses, radius_witnesses)
        if not actual['complete']:
            raise ValueError('A singular or incomplete current world field cannot define rows: '
                             +actual.get('error', 'unknown actual failure'))
        if matrix_workdir is None:
            raise ValueError('An explicit outside-repository runner scratch cache is required')
        directory = Path(matrix_workdir).resolve()
        if directory == self.repo or self.repo in directory.parents:
            raise ValueError('Scientific row caches must stay outside the repository')
        directory.mkdir(parents=True, exist_ok=False)
        original, bounds, prefix = self.selector.build_inequality_rows(
            self.q, self._x, self, self, transpose, coordinate_size,
            reach_ratio=self.reach_ratio, safety=self.safety, active_band=active_band,
            max_rows=192, top_curvature=16, top_radius=2,
            witnesses=list(self._curvature_memory.values()),
            radius_witnesses=list(self._radius_memory.values()),
            observed_module=self.observed_marker,
            matrix_workdir=directory/'original-192', block_columns=block_columns)
        prefix_rows = int(original.shape[0])
        selections = []
        for kind, key in (('body_diameter', 'radius_working_candidates'),
                          ('witness_distance', 'distance_working_candidates')):
            for index, item in enumerate(actual['amplitude'][key]):
                if index and item['score'] < -active_band:
                    continue
                if kind == 'body_diameter':
                    selections.append((kind, item['location'], None))
                else:
                    # The selected physical location always carries BOTH
                    # reflection branches, irrespective of which is active.
                    selections.extend((kind, item['location'], sign) for sign in (-1, 1))
        selections.extend((kind, None, None) for kind in ('cap_diameter', 'height_floor'))
        if len(selections) > 12:
            raise ValueError('The declared bounded amplitude working set unexpectedly expanded')
        total = prefix_rows+len(selections)
        path = Path(prefix['row_cache'])
        prefix_bytes = prefix_rows*coordinate_size*np.dtype(np.float64).itemsize
        if isinstance(original, np.memmap):
            original.flush()
            original._mmap.close()
        del original
        if prefix_rows and (not path.exists() or path.stat().st_size != prefix_bytes):
            raise ValueError('The complete original selected-row prefix byte length changed')
        # Extend the SAME cache. No prefix row is rewritten, no second 2GB
        # cache is created, and no scientific row is moved into git.
        with path.open('r+b' if path.exists() else 'w+b') as stream:
            stream.truncate(total*coordinate_size*np.dtype(np.float64).itemsize)
        matrix = np.memmap(path, dtype=np.float64, mode='r+', shape=(total, coordinate_size))
        result_bounds = np.empty(total)
        result_bounds[:prefix_rows] = bounds
        row_metadata = []
        for old in prefix['rows']:
            row = dict(old)
            row.update(kind='necessary_reach_product',
                physical_g=float(old['current_product'])-self.safety,
                upper_bound=self.safety,
                physical_current_value=float(old['current_product']),
                row_normalization_scale=float(old['gradient_coordinate_norm']),
                original_prefix_row=True)
            row_metadata.append(row)
        for offset, (kind, location, sign) in enumerate(selections):
            value, free_gradient, extra = self._amplitude_row(kind, location, sign)
            coordinate_gradient = np.asarray(transpose(free_gradient), dtype=float)
            if coordinate_gradient.shape != (coordinate_size,) or not np.isfinite(coordinate_gradient).all():
                raise FloatingPointError('The full H2 coordinate transpose is incomplete or nonfinite')
            norm = float(np.linalg.norm(coordinate_gradient))
            if not math.isfinite(norm):
                raise FloatingPointError('Nonfinite full-coordinate amplitude gradient norm')
            scale = norm if norm > 0 else 1.
            index = prefix_rows+offset
            matrix[index] = coordinate_gradient/scale
            result_bounds[index] = -value/scale
            row_metadata.append(dict(index=index, **extra, physical_g=value,
                physical_current_value=value, upper_bound=0.,
                current_product=None, gradient_coordinate_norm=norm,
                row_normalization_scale=scale, zero_gradient_row_retained=bool(norm == 0),
                normalized_bound=float(result_bounds[index]), original_prefix_row=False))
            matrix.flush()
            _discard(matrix)
        if len(row_metadata) != total or not np.isfinite(result_bounds).all():
            raise FloatingPointError('The complete typed selected-row metadata is inconsistent')
        matrix.flush()
        _discard(matrix)
        metadata = dict(schema=SCHEMA, source_binding=self.binding,
            selected_rows=total, original_prefix_rows=prefix_rows,
            appended_amplitude_rows=len(selections), no_original_row_removed=True,
            original_prefix_rewritten=False, original_selector_source_sha256=SELECTOR_SHA256,
            original_selection_metadata=prefix, rows=row_metadata,
            row_cache=str(path), row_cache_bytes=total*coordinate_size*8,
            row_cache_allocated_bytes=int(path.stat().st_blocks*512),
            original_prefix_bytes=prefix_bytes, duplicate_prefix_cache_bytes=0,
            shared_cache_extended_in_place=True, block_columns=int(block_columns),
            original_variables=int(self.q.free_size), coordinate_size=int(coordinate_size),
            physical_g_formula='current physical value minus its own upper bound',
            normalized_row_formula='C=dg[T]/positive_scale; b=-physical_g/positive_scale',
            common_slack_formula='dg[Tz]-delta_tau <= tau0-physical_g for EVERY typed row',
            zero_gradient_amplitude_rows_retained=True,
            all_original_field_variables_retained=True,
            current_full_point_sha256=self._token,
            current_geometry=actual, numerical_reach_safety_factor=self.safety,
            permanent_curvature_locations=len(self._curvature_memory),
            permanent_radius_locations=len(self._radius_memory),
            nonlinear_memory_has_no_eviction_or_working_row_cap=True,
            no_feasibility_inferred_from_linear_model=True,
            continuous_geometry_certified=False,
            scope='Full finite NEW-field world geometry, unchanged original 192 selection, plus bounded actual amplitude rows; true whole-grid/permanent-point scans decide nonlinear acceptance')
        return matrix, result_bounds, metadata
