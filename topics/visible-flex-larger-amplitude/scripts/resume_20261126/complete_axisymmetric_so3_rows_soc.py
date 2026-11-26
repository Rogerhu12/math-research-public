#!/usr/bin/env python3
"""Full-current-SO3 typed separation/SOC at one immutable parent and ray anchor.

The actual complete QP prefix is never selected again or replaced.  New
violated addresses generate full original-variable world pullbacks at that
same parent, followed by the same declared coordinate transpose.  Every
row remains in the R683 all-halfspace correction.  Only the outer driver
may accept a corrected point, after same-Phi, domain and complete geometry
reads.  Numerical correction failure is not geometric infeasibility.
"""
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys

import numpy as np


SCHEMA = 'complete-axisymmetric-SO3-fixed-parent-ray-separated-all-rows-SOC-v1'
OPERATOR_SHA = '7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf'
GEOMETRY_SHA = '2240a1f68021991a85c502ed3cf67c82f6bac6e1e4e10b3b3286eab120d4f229'
PROJECTION_SHA = 'a2c6d334d40be88ac7edb2dd2e525da5583d9f723e33d5bae9d910c0adfe745e'
SELECTOR_SHA = 'e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8'
KEYS = ('F', 'Fs', 'Fphi', 'Fss', 'Fsphi', 'Fphiphi')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Complete scientific SO3 correction belongs in public repository Actions')


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def finite(value, name, *, nonnegative=False):
    if isinstance(value, bool):
        raise ValueError('Use an actual finite scalar: '+name)
    result = float(value)
    if not math.isfinite(result) or (nonnegative and result < 0):
        raise ValueError('Invalid actual finite scalar: '+name)
    return result


def source_module(obj):
    module = sys.modules.get(obj.__class__.__module__)
    if module is None:
        raise ValueError('The actual complete source module is unavailable')
    return module


def prefix_sha(path, size):
    h = hashlib.sha256()
    remaining = int(size)
    with Path(path).open('rb') as stream:
        while remaining:
            block = stream.read(min(remaining, 1 << 20))
            if not block:
                raise ValueError('The actual original QP row prefix was truncated')
            h.update(block)
            remaining -= len(block)
    return h.hexdigest()


def load_projection(path):
    path = Path(path).resolve()
    if sha(path) != PROJECTION_SHA:
        raise ValueError('Use the complete unchanged published R683 projection kernel')
    spec = importlib.util.spec_from_file_location('_actual_SO3_R683_all_halfspaces', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class CompleteSO3RowsSOC:
    def __init__(self, q, parent_x, coordinates, screen, matrix, bounds, metadata,
                 *, projection_source, parent_identity, max_rounds=8,
                 block_columns=32768):
        require_actions()
        self.q, self.coordinates, self.screen = q, coordinates, screen
        self.base = load_projection(projection_source)
        self.x = np.array(parent_x, dtype=np.float64, copy=True)
        self.x.setflags(write=False)
        if self.x.shape != (q.free_size,) or not np.isfinite(self.x).all():
            raise ValueError('Bind every current free core, rotation jet and height coordinate')
        if (sha(source_module(q).__file__) != OPERATOR_SHA
                or sha(source_module(coordinates).__file__) != OPERATOR_SHA
                or sha(source_module(screen).__file__) != GEOMETRY_SHA
                or coordinates.problem is not q or screen.q is not q
                or q.model.get('source_sha256') != OPERATOR_SHA
                or canonical(q.model) != q.identity):
            raise ValueError('Bind the actual complete 7f SO3 field, its norm and 2240 world screen')
        for name in ('point_fields', 'point_vjp', 'prepare', 'fields_torch'):
            if sha(getattr(q, name).__code__.co_filename) != OPERATOR_SHA:
                raise ValueError('A complete original SO3 physical entry changed: '+name)
        if (metadata.get('schema') != source_module(screen).SCHEMA
                or metadata.get('source_binding') != screen.binding
                or metadata.get('no_original_row_removed') is not True
                or metadata.get('original_selector_source_sha256') != SELECTOR_SHA
                or metadata.get('current_full_point_sha256') != source_module(screen).array_sha(self.x)):
            raise ValueError('The supplied C is not the complete actual same-parent typed QP prefix')
        norm = coordinates.record
        if canonical({k: v for k, v in norm.items() if k != 'norm_identity_sha256'}) != norm['norm_identity_sha256']:
            raise ValueError('The complete physical coordinate norm identity changed')
        if (not isinstance(matrix, np.memmap) or matrix.dtype != np.dtype('float64')
                or matrix.ndim != 2 or matrix.shape[1] != q.free_size
                or matrix.offset != 0
                or Path(matrix.filename).resolve() != Path(metadata['row_cache']).resolve()):
            raise ValueError('Keep the real full-coordinate row-major original QP mmap')
        self.C = matrix
        self.b = np.array(bounds, dtype=np.float64, copy=True)
        self.rows = json.loads(json.dumps(metadata['rows'], allow_nan=False))
        if (self.b.shape != (len(matrix),) or not np.isfinite(self.b).all()
                or len(self.rows) != len(matrix) or metadata['selected_rows'] != len(matrix)):
            raise ValueError('Every actual original row needs its unchanged bound and metadata')
        self.original_count = len(matrix)
        self.original_curvature_count = int(metadata['original_prefix_rows'])
        if (self.original_curvature_count+metadata['appended_amplitude_rows'] != len(matrix)
                or not 0 <= self.original_curvature_count <= len(matrix)):
            raise ValueError('Keep both the whole original selected prefix and all amplitude rows')
        self.round_limit = int(max_rounds)
        self.block_columns = int(block_columns)
        if (isinstance(max_rounds, bool) or self.round_limit != max_rounds
                or not 1 <= self.round_limit <= 8 or self.block_columns != block_columns
                or self.block_columns < 1):
            raise ValueError('Declare a finite one-to-eight separation budget and positive column block')
        self.reach_ratio, self.safety = screen.reach_ratio, screen.safety
        self.path = Path(matrix.filename).resolve()
        self.original_bytes = self.original_count*q.free_size*8
        matrix.flush()
        if self.path.stat().st_size != self.original_bytes:
            raise ValueError('Bind the original unextended complete QP cache before SOC')
        self.original_prefix_sha256 = prefix_sha(self.path, self.original_bytes)
        self.descriptors = [self._descriptor(row, i, self.b[i]) for i, row in enumerate(self.rows)]
        if ([v['kind'] for v in self.descriptors].count('cap_diameter') != 1
                or [v['kind'] for v in self.descriptors].count('height_floor') != 1):
            raise ValueError('The complete cap and free-H scalar rows are mandatory')
        self.keys = {self._key(row) for row in self.descriptors}
        self.max_additions = 2+screen.amplitude_top_radius+2*screen.amplitude_top_distance
        self.capacity_rows = self.original_count+self.round_limit*self.max_additions
        self.capacity = None
        self.rounds = 0
        self.qp_frozen = False
        self.qp_count = None
        self.qp_prefix_bytes = None
        self.qp_prefix_sha256 = None
        self.seed_records = []
        self.anchor_step = None
        self.anchor_point = None
        self.anchor_alpha = None
        self.new_curvature_locations = []
        self.new_radius_locations = []
        self.identity = dict(schema=SCHEMA, source_sha256=sha(__file__),
            parent_identity=parent_identity, parent_coordinate_sha256=self.base.array_sha(self.x),
            model_identity_sha256=q.identity, actual_complete_model=q.model,
            coordinate_norm=norm, original_rows_metadata_sha256=canonical(metadata),
            original_prefix_bytes=self.original_bytes,
            original_prefix_sha256=self.original_prefix_sha256,
            original_QP_rows=self.original_count, original_curvature_rows=self.original_curvature_count,
            original_amplitude_rows=len(matrix)-self.original_curvature_count,
            ambient_coordinates=q.free_size, world_geometry_source_sha256=GEOMETRY_SHA,
            physical_operator_source_sha256=OPERATOR_SHA, projection_source_sha256=PROJECTION_SHA,
            reach_ratio=self.reach_ratio, numerical_reach_safety_factor=self.safety,
            budgets=screen.budgets.metadata(), maximum_rounds=self.round_limit,
            no_old_physical_source_or_schema_relabeling=True,
            QP_prefix_never_reselected=True, fixed_parent_and_ray_anchor_every_round=True)

    def prior_rejection_requests(self, reports):
        """Retain exact addresses from actual same-model rejected reports, not values."""
        require_actions()
        requests, seen, provenance = [], set(), []
        def offer(row, source_path):
            key = (row['kind'], self._location_key(row['location']), row.get('sign'))
            if key not in seen:
                seen.add(key)
                requests.append(row)
                provenance.append(dict(request=row, first_actual_report_address=source_path))
        def walk(value, path):
            if isinstance(value, dict):
                if value.get('schema') == source_module(self.screen).SCHEMA:
                    if value.get('complete') is not True or value.get('passed') is not False:
                        return
                    if value.get('actual_model_identity_sha256') != self.q.identity:
                        raise ValueError('A prior separated address has another mathematical field model')
                    if finite(value['reach_physical_g'], 'prior actual reach g') > 0:
                        offer(dict(kind='necessary_reach_product', location=self._point(value['worst'])), path)
                    amplitude = value['amplitude']
                    if amplitude.get('complete') is not True:
                        raise ValueError('A prior complete geometry rejection lacks its full amplitude record')
                    if finite(amplitude['body_diameter'], 'prior actual body g') > 0:
                        for item in amplitude['radius_working_candidates']:
                            offer(dict(kind='body_diameter', location=self._point(item['location']), sign=None), path)
                    if max(finite(amplitude['distance_plus'], 'prior actual plus g'),
                           finite(amplitude['distance_minus'], 'prior actual minus g')) > 0:
                        for item in amplitude['distance_working_candidates']:
                            for sign in (-1, 1):
                                offer(dict(kind='witness_distance', location=self._point(item['location']), sign=sign), path)
                    return
                for key, item in value.items():
                    if isinstance(item, (dict, list)):
                        walk(item, path+[str(key)])
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if isinstance(item, (dict, list)):
                        walk(item, path+[str(i)])
        for i, report in enumerate(reports):
            if report is not None:
                walk(report, ['bound_actual_report', str(i)])
        return requests, provenance

    def _actual_diameter_partner(self, geometry):
        H = abs(finite(geometry['current_height'], 'actual H'))
        R = finite(geometry['maximum_radius'], 'actual radius', nonnegative=True)
        D = finite(geometry['diameter_point_lower'], 'actual diameter')
        if D != max(2., 2*H, 2*R):
            raise ValueError('Use the unchanged complete true-field diameter maximum')
        if 2*R >= max(2., 2*H):
            return dict(kind='point_radius', location=self._point(geometry['farthest']))
        if 2*H >= 2.:
            return dict(kind='cap_height')
        return dict(kind='fixed_core')

    def seed_before_qp(self, reports, current_geometry):
        """Append all actual prior rejection locations before this NEW parent's QP."""
        require_actions()
        if self.qp_frozen or self.capacity is not None or self.rounds or self.anchor_step is not None:
            raise ValueError('Prior separation is a single explicit pre-QP operation')
        if (current_geometry.get('complete') is not True or current_geometry.get('passed') is not True
                or current_geometry.get('actual_model_identity_sha256') != self.q.identity
                or current_geometry.get('current_full_point_sha256') != source_module(self.screen).array_sha(self.x)):
            raise ValueError('Pre-QP seeding needs this freshly screened feasible current parent')
        requests, provenance = self.prior_rejection_requests(reports)
        partner = self._actual_diameter_partner(current_geometry)
        candidates = []
        for row in requests:
            if row['kind'] == 'necessary_reach_product':
                candidates.extend(dict(row, branch=branch, partner=partner) for branch in (0, 1))
            else:
                candidates.append(row)
        self.capacity_rows += len(candidates)
        result = self._append_descriptors(candidates, origin='prior_actual_rejection_before_NEW_QP')
        result.update(actual_prior_unique_requests=len(requests), prior_address_provenance=provenance,
            prior_physical_values_or_covectors_inherited=False,
            current_full_diameter_partner_used_for_both_principal_branches=True,
            original_selector_and_amplitude_prefix_unchanged=True)
        self.seed_records = result.get('rows', [])
        return result

    def freeze_qp_prefix(self):
        require_actions()
        if self.qp_frozen or self.rounds or self.anchor_step is not None:
            raise ValueError('Freeze the complete QP prefix exactly once before solving it')
        self.C.flush()
        self.qp_count = len(self.C)
        self.qp_prefix_bytes = self.qp_count*self.q.free_size*8
        self.qp_prefix_sha256 = prefix_sha(self.path, self.qp_prefix_bytes)
        self.qp_frozen = True
        self.identity.update(original_selector_and_amplitude_rows=self.original_count,
            pre_QP_separation_rows=self.qp_count-self.original_count,
            original_QP_rows=self.qp_count, complete_QP_prefix_bytes=self.qp_prefix_bytes,
            complete_QP_prefix_sha256=self.qp_prefix_sha256,
            whole_prefix_frozen_before_actual_QP=True)
        return dict(self.identity)

    def qp_metadata(self, original_metadata):
        if not self.qp_frozen:
            raise ValueError('First freeze the complete actual QP prefix')
        result = json.loads(json.dumps(original_metadata, allow_nan=False))
        result.update(schema='complete-SO3-selected-amplitude-and-prior-rejection-QP-rows-v1',
            original_selected_prefix_schema=original_metadata['schema'],
            original_selected_prefix_metadata_sha256=canonical(original_metadata),
            source_of_prior_separation_rows_sha256=sha(__file__),
            selected_rows=self.qp_count, rows=json.loads(json.dumps(self.rows, allow_nan=False)),
            appended_pre_QP_separation_rows=self.qp_count-self.original_count,
            row_cache_bytes=self.qp_prefix_bytes, row_cache_capacity_bytes=self.path.stat().st_size,
            literal_original_prefix_sha256=self.original_prefix_sha256,
            frozen_complete_QP_prefix_sha256=self.qp_prefix_sha256,
            original_prefix_rewritten=False, no_original_row_removed=True)
        return result

    def _point(self, value):
        return self.screen._location(value)

    def _legacy_curvature(self, value):
        if value[0] == 'grid' and len(value) == 4:
            location = self._point(dict(stage=int(value[1]), angle=int(value[2])))
            branch = int(value[3])
        elif value[0] == 'arbitrary' and len(value) == 5:
            location = self._point(dict(cell=int(value[1]), u=float(value[2]), phi=float(value[3])))
            branch = int(value[4])
        else:
            raise ValueError('Unknown complete original curvature address')
        if branch not in (0, 1):
            raise ValueError('Keep the actual principal branch')
        return location, branch

    def _legacy_radius(self, value):
        if value in (['fixed_core'], ('fixed_core',)):
            return dict(kind='fixed_core')
        if value in (['cap_height'], ('cap_height',)):
            return dict(kind='cap_height')
        if value[0] == 'grid_radius' and len(value) == 3:
            point = self._point(dict(stage=int(value[1]), angle=int(value[2])))
        elif value[0] == 'arbitrary_radius' and len(value) == 4:
            point = self._point(dict(cell=int(value[1]), u=float(value[2]), phi=float(value[3])))
        else:
            raise ValueError('Unknown complete original diameter partner')
        return dict(kind='point_radius', location=point)

    def _descriptor(self, row, index, bound):
        if row['index'] != index or float(row['normalized_bound']) != float(bound):
            raise ValueError('The literal original row order or normalized bound changed')
        scale = finite(row['row_normalization_scale'], 'parent row scale')
        g = finite(row['physical_g'], 'parent physical g')
        if scale <= 0 or -g/scale != float(bound):
            raise ValueError('The typed physical row and its exact stored normalization differ')
        kind = row['kind']
        result = dict(kind=kind, scale=scale, parent_g=g)
        if kind == 'necessary_reach_product':
            point, branch = self._legacy_curvature(row['curvature_point'])
            result.update(location=point, branch=branch, partner=self._legacy_radius(row['radius_point']))
        elif kind in ('body_diameter', 'witness_distance'):
            result.update(location=self._point(row['location']), sign=row.get('sign'))
            if kind == 'witness_distance' and result['sign'] not in (-1, 1):
                raise ValueError('Keep the actual free-core witness sign')
        elif kind not in ('cap_diameter', 'height_floor'):
            raise ValueError('Unknown complete actual SO3 inequality family')
        return result

    @staticmethod
    def _location_key(value):
        return (int(value['cell']), float(value['u']).hex(), float(value['phi']).hex())

    def _key(self, row):
        kind = row['kind']
        if kind == 'necessary_reach_product':
            partner = row['partner']
            pkey = (partner['kind'],) if partner['kind'] != 'point_radius' else (
                partner['kind'], *self._location_key(partner['location']))
            return (kind, self._location_key(row['location']), int(row['branch']), pkey)
        if kind in ('body_diameter', 'witness_distance'):
            return kind, self._location_key(row['location']), row.get('sign')
        return (kind,)

    def _diameter(self, partner, *, derivative=False):
        q, screen = self.q, self.screen
        kind = partner['kind']
        gradient = np.zeros(q.free_size) if derivative else None
        if kind == 'fixed_core':
            D = 2.
        elif kind == 'cap_height':
            H = float(screen._prepared.height)
            D = 2*abs(H)
            if derivative:
                gradient[-1] = 2*np.sign(H)
        elif kind == 'point_radius':
            f = screen._point(partner['location'])
            D = 2*float(np.linalg.norm(f['F']))
            if not math.isfinite(D) or D <= 0:
                raise FloatingPointError('An actual diameter partner has no positive finite radius')
            if derivative:
                cot = {key: np.zeros(3) for key in KEYS}
                cot['F'] = 4*f['F']/D
                gradient = screen._pullback(partner['location'], cot)
        else:
            raise ValueError('Unknown same-parent diameter branch')
        if not math.isfinite(D) or D <= 0:
            raise FloatingPointError('Every declared diameter partner is positive and finite')
        return D, gradient

    def _parent_row(self, descriptor):
        screen = self.screen
        screen._set_x(self.x)
        kind = descriptor['kind']
        if kind == 'necessary_reach_product':
            f = screen._point(descriptor['location'])
            value, cot, principal = screen.curvature_cotangent(f, descriptor['branch'])
            if (not math.isfinite(value) or value == 0
                    or not math.isfinite(principal['principal_gap']) or principal['principal_gap'] <= 0):
                raise FloatingPointError('A new absolute-curvature row needs a finite nonzero simple parent branch; no full derivative is declared at a zero value or repeated eigenvalue')
            dk = screen._pullback(descriptor['location'], cot)
            D, dD = self._diameter(descriptor['partner'], derivative=True)
            g = self.reach_ratio*D*abs(value)-self.safety
            gradient = self.reach_ratio*(D*np.sign(value)*dk+abs(value)*dD)
            details = dict(signed_curvature=float(value), diameter=D,
                current_product=g+self.safety, principal_metadata=principal)
        else:
            g, gradient, details = screen._amplitude_row(kind,
                descriptor.get('location'), descriptor.get('sign'))
        row = np.asarray(self.coordinates.transpose(gradient), dtype=np.float64)
        if row.shape != (self.q.free_size,) or not np.isfinite(row).all():
            raise FloatingPointError('A separated covector omitted full core/omega/H or the complete norm transpose')
        norm = float(np.linalg.norm(row))
        if not math.isfinite(norm):
            raise FloatingPointError('A separated full-coordinate norm is nonfinite')
        scale = norm if norm > 0 else 1.
        g = finite(g, 'actual separated parent inequality')
        desc = dict(descriptor, scale=scale, parent_g=g)
        record = dict(kind=kind, physical_g=g, row_normalization_scale=scale,
            gradient_coordinate_norm=norm, normalized_bound=-g/scale,
            descriptor=desc, actual_parent_details=details,
            same_original_parent_covector=True,
            complete_world_point_vjp_and_coordinate_transpose=True,
            free_core_witness_derivative_paid=(kind == 'witness_distance'),
            zero_gradient_row_retained=(norm == 0), original_prefix_row=False)
        return row/scale, -g/scale, desc, record

    def cache_state(self):
        stat = self.path.stat()
        return dict(path=str(self.path), original_QP_rows=self.qp_count,
            original_selector_amplitude_rows=self.original_count,
            current_rows=len(self.C), capacity_rows=(self.capacity_rows if self.capacity is not None else self.original_count),
            used_bytes=int(self.C.size*8), capacity_bytes=int(stat.st_size),
            actual_allocated_bytes=int(stat.st_blocks*512) if hasattr(stat, 'st_blocks') else None,
            original_prefix_bytes=self.original_bytes,
            original_prefix_sha256=self.original_prefix_sha256,
            original_QP_prefix_unchanged=True, all_earlier_separation_rows_retained=True,
            only_new_row_indices_written=True, unused_capacity_not_a_constraint=True,
            capacity_is_not_a_RAM_bound=True)

    def extend_from_rejected_geometry(self, geometry):
        require_actions()
        if not self.qp_frozen:
            raise ValueError('All subsequent separation is after the whole QP prefix was frozen')
        if self.rounds >= self.round_limit:
            raise ValueError('The finite same-parent separation budget is exhausted')
        if geometry.get('complete') is not True or geometry.get('actual_model_identity_sha256') != self.q.identity:
            return dict(complete=False, extension_available=False, reason='No complete actual same-model rejected geometry')
        requested = []
        if finite(geometry['reach_physical_g'], 'actual rejected reach g') > 0:
            point = self._point(geometry['worst'])
            partner = self._actual_diameter_partner(geometry)
            for branch in (0, 1):
                requested.append(dict(kind='necessary_reach_product', location=point,
                    branch=branch, partner=partner))
        amplitude = geometry['amplitude']
        if amplitude.get('complete') is not True or amplitude['budgets'] != self.screen.budgets.metadata():
            raise ValueError('The rejected complete amplitude screen changed its held budgets')
        if finite(amplitude['body_diameter'], 'actual body g') > 0:
            for item in amplitude['radius_working_candidates']:
                requested.append(dict(kind='body_diameter', location=self._point(item['location']), sign=None))
        if max(finite(amplitude['distance_plus'], 'actual plus g'),
               finite(amplitude['distance_minus'], 'actual minus g')) > 0:
            for item in amplitude['distance_working_candidates']:
                for sign in (-1, 1):
                    requested.append(dict(kind='witness_distance', location=self._point(item['location']), sign=sign))
        return self._append_descriptors(requested, origin='same_parent_post_QP_separation')

    def _append_descriptors(self, requested, *, origin):
        require_actions()
        candidates, seen = [], set(self.keys)
        for row in requested:
            key = self._key(row)
            if key not in seen:
                candidates.append(row)
                seen.add(key)
        if self.qp_frozen and len(candidates) > self.max_additions:
            raise ValueError('The actual separation set exceeds its explicitly reserved capacity')
        additions = [self._parent_row(row) for row in candidates]
        negative = [dict(row=record, normalized_bound=float(b))
            for _, b, _, record in additions if b < 0]
        if negative:
            return dict(complete=True, extension_available=False,
                reason='A newly separated location is infeasible at the fixed parent; real restoration or another parent is required',
                actual_new_parent_violations=negative, negative_bound_used_as_feasible_zero=False,
                original_rows_removed=False, geometric_infeasibility_proved=False)
        if not additions:
            return dict(complete=True, extension_available=True, added_rows=0,
                reason='Every chosen true rejected family already has its same row and partner',
                all_existing_rows_retained=True)
        old_count, new_count = len(self.C), len(self.C)+len(additions)
        if new_count > self.capacity_rows:
            raise ValueError('No original row may be evicted to create more separation capacity')
        if self.capacity is None:
            self.C.flush()
            with self.path.open('r+b') as stream:
                stream.truncate(self.capacity_rows*self.q.free_size*8)
            self.capacity = np.memmap(self.path, dtype=np.float64, mode='r+',
                shape=(self.capacity_rows, self.q.free_size))
        records = []
        for j, (row, bound, desc, record) in enumerate(additions):
            index = old_count+j
            self.capacity[index] = row
            record.update(index=index, origin=origin,
                introduced_for_correction_round=self.rounds+1 if self.qp_frozen else None)
            self.rows.append(record)
            self.descriptors.append(desc)
            self.keys.add(self._key(desc))
            records.append(record)
            if desc['kind'] == 'necessary_reach_product':
                self.new_curvature_locations.append(dict(desc['location'], protected=True))
                if desc['partner']['kind'] == 'point_radius':
                    self.new_radius_locations.append(dict(desc['partner']['location']))
            elif 'location' in desc:
                self.new_radius_locations.append(dict(desc['location']))
        self.capacity.flush()
        self.base._discard(self.capacity)
        if prefix_sha(self.path, self.original_bytes) != self.original_prefix_sha256:
            raise ValueError('Appending separated rows changed the literal original QP bytes')
        if self.qp_frozen and prefix_sha(self.path, self.qp_prefix_bytes) != self.qp_prefix_sha256:
            raise ValueError('Appending a correction row changed the complete frozen QP prefix')
        self.C = self.capacity[:new_count]
        self.b = np.r_[self.b, [item[1] for item in additions]]
        return dict(complete=True, extension_available=True, added_rows=len(additions),
            rows=records, origin=origin,
            correction_round=self.rounds+1 if self.qp_frozen else None, previous_rows=old_count,
            current_rows=new_count, cache=self.cache_state(),
            original_prefix_bytes_directly_checked=True,
            no_QP_reselection_or_original_row_rewrite=True,
            new_curvature_locations=self.new_curvature_locations,
            new_radius_locations=self.new_radius_locations,
            amplitude_candidate_scope='Complete reported top paired-distance pool, with both signs retained; a later full screen still decides every point')

    def read_fixed_values(self, point):
        require_actions()
        point = np.asarray(point, dtype=float)
        if point.shape != self.x.shape or not np.isfinite(point).all():
            raise ValueError('Use the complete finite actual trial point')
        values, records = [], []
        try:
            self.screen._set_x(point)
            for i, row in enumerate(self.descriptors):
                kind = row['kind']
                if kind == 'necessary_reach_product':
                    f = self.screen._point(row['location'])
                    principal, _, area = self.screen._point_geometry(f)
                    if not math.isfinite(area) or area <= 0:
                        raise FloatingPointError('The actual typed curvature point has no positive area')
                    value = float(principal[row['branch']])
                    D, _ = self._diameter(row['partner'])
                    g = self.reach_ratio*D*abs(value)-self.safety
                    detail = dict(signed_curvature=value, diameter=D, area=area)
                elif kind in ('cap_diameter', 'height_floor'):
                    g = self.screen._scalar_values()[kind]
                    detail = dict(height=float(self.screen._prepared.height))
                else:
                    f = self.screen._point(row['location'])
                    av = self.screen._amplitude_values(f)
                    key = (kind if kind == 'body_diameter' else
                        'distance_plus' if row['sign'] == 1 else 'distance_minus')
                    g = float(av[key])
                    detail = dict(current_witness_radius=float(1+np.sum(self.screen._prepared.core)), sign=row.get('sign'))
                g = finite(g, 'true typed nonlinear row')
                normalized = g/row['scale']
                if not math.isfinite(normalized):
                    raise FloatingPointError('A true typed row is nonfinite in its original parent units')
                values.append(normalized)
                records.append(dict(index=i, kind=kind, physical_g=g,
                    parent_normalization_scale=row['scale'], normalized_g=normalized, **detail))
        except (FloatingPointError, OverflowError, ValueError, RuntimeError, np.linalg.LinAlgError) as exc:
            return dict(complete=False, actual_error=repr(exc), failed_row=len(records), rows=records,
                original_parent_scales_retained=True, geometric_infeasibility_proved=False)
        return dict(complete=True, coordinate_sha256=self.base.array_sha(point),
            normalized_constraints=values, rows=records,
            maximum_normalized_constraint=max(values, default=None),
            all_original_and_separated_rows_read=True,
            fixed_parent_scales_and_same_original_partner_addresses=True)

    def bind_anchor(self, coordinate_step, anchor_alpha, anchor_point):
        require_actions()
        if not self.qp_frozen:
            raise ValueError('The actual QP must already have its complete frozen prefix')
        d = np.asarray(coordinate_step, dtype=np.float64)
        alpha = finite(anchor_alpha, 'actual ray anchor alpha')
        if d.shape != (self.q.free_size,) or not np.isfinite(d).all() or not 0 < alpha <= 1:
            raise ValueError('Keep the finite full ray anchor in the original coordinate norm')
        point = np.asarray(anchor_point, dtype=np.float64)
        if not np.array_equal(point, self.x+self.coordinates.lift(d)):
            raise ValueError('The actual anchor is not this same parent plus its declared full coordinate step')
        if self.anchor_step is None:
            self.anchor_step = d.copy()
            self.anchor_step.setflags(write=False)
            self.anchor_point = point.copy()
            self.anchor_point.setflags(write=False)
            self.anchor_alpha = alpha
        elif (not np.array_equal(d, self.anchor_step)
                or not np.array_equal(point, self.anchor_point) or alpha != self.anchor_alpha):
            raise ValueError('No correction round may change its original parent or ray anchor')

    def propose(self, *, tau=0., inward_fraction=.125, feasibility_tolerance=2e-11):
        require_actions()
        if self.anchor_step is None:
            raise ValueError('Bind one actual Phi/domain-passing geometry-rejected ray first')
        if self.rounds >= self.round_limit:
            raise ValueError('The finite correction budget is exhausted')
        self.rounds += 1
        tolerance = finite(feasibility_tolerance, 'all-row tolerance', nonnegative=True)
        tau = finite(tau, 'cubic inward coefficient', nonnegative=True)
        fraction = finite(inward_fraction, 'observed violation fraction', nonnegative=True)
        d = self.anchor_step
        report = dict(schema=SCHEMA, source_sha256=sha(__file__), identity=self.identity,
            complete=False, proposal_available=False, correction_round=self.rounds,
            original_QP_rows=self.qp_count, original_selector_amplitude_rows=self.original_count,
            current_rows=len(self.C),
            cache=self.cache_state(), anchor_alpha=self.anchor_alpha,
            original_anchor_step_sha256=self.base.array_sha(d),
            original_anchor_point_sha256=self.base.array_sha(self.anchor_point),
            same_parent_and_anchor_every_round=True, original_QP_prefix_reselected=False,
            all_current_rows_reread_at_original_anchor=True,
            full_true_Phi_domain_geometry_acceptance_owned_by_driver=True,
            minimum_norm_convergence_not_assumed=True, continuous_geometry_certified=False)
        cd = self.base._dot(self.C, d, self.block_columns)
        slack = self.b-cd
        violation = float(np.max(-slack[:self.qp_count], initial=0.))
        report['original_prefix_linear_violation'] = violation
        report['all_current_anchor_linear_violation'] = float(np.max(-slack, initial=0.))
        if violation > tolerance:
            report.update(complete=True, reason='The scaled original QP direction violates an original literal QP row')
            return None, None, report
        actual = self.read_fixed_values(self.anchor_point)
        report['actual_anchor_fixed_rows'] = actual
        if not actual['complete']:
            report.update(complete=True, reason='No complete actual anchor read for all fixed-parent row functions')
            return None, None, report
        r = np.asarray(actual['normalized_constraints'], dtype=float)
        maximum = float(np.max(r, initial=0.))
        length = float(np.linalg.norm(d))
        if maximum <= 0 or not math.isfinite(length) or length <= 0:
            report.update(complete=True, reason='No positive represented anchor violation or no finite nonzero anchor')
            return None, None, report
        try:
            inward = tau*length**3+fraction*maximum
        except OverflowError:
            inward = float('inf')
        if not math.isfinite(inward):
            report.update(complete=True, reason='The explicit inward budget is nonfinite')
            return None, None, report
        k = np.minimum(slack, -r-inward)
        report.update(tau=tau, inward_fraction=fraction, inward_normalized_offset=inward,
            anchor_coordinate_norm=length, original_anchor_linear_values=cd.tolist(),
            complete_parent_bounds=self.b.tolist(), correction_halfspace_bounds=k.tolist(),
            actual_nonlinear_minus_parent_linear=(r-(cd-self.b)).tolist(),
            correction_rule='C e <= min(b-C d_anchor, -g(x+T d_anchor)/parent_scale-inward) for EVERY row',
            cubic_remainder_theorem_not_claimed_for_observed_fraction=True)
        e, projection = self.base.minimum_norm_halfspaces(self.C, k,
            block_columns=self.block_columns, feasibility_tolerance=tolerance,
            dual_tolerance=max(1.e-14, min(1.e-12, tolerance/16)),
            max_sweeps=20000, refresh_sweeps=64)
        report['projection'] = projection
        if e is None:
            report.update(complete=True, reason='No feasible complete-row correction returned within its numerical budget; no row was removed')
            return None, None, report
        z = d+e
        ce = self.base._dot(self.C, e, self.block_columns)
        cz = self.base._dot(self.C, z, self.block_columns)
        linear_violation = float(np.max(cz-self.b, initial=0.))
        target_violation = float(np.max(r+inward+ce, initial=0.))
        report.update(corrected_linear_violation=linear_violation,
            corrected_target_linear_violation=target_violation,
            correction_norm=float(np.linalg.norm(e)),
            correction_over_anchor_norm=float(np.linalg.norm(e))/length,
            corrected_coordinate_norm=float(np.linalg.norm(z)),
            direct_Cz_minus_Cd_minus_Ce=float(np.max(np.abs(cz-cd-ce), initial=0.)),
            corrected_step_sha256=self.base.array_sha(z),
            original_prefix_sha256_after=prefix_sha(self.path, self.original_bytes),
            complete_QP_prefix_sha256_after=prefix_sha(self.path, self.qp_prefix_bytes))
        if report['original_prefix_sha256_after'] != self.original_prefix_sha256:
            raise ValueError('The original full QP row bytes changed during projection')
        if report['complete_QP_prefix_sha256_after'] != self.qp_prefix_sha256:
            raise ValueError('The complete frozen QP prefix changed during projection')
        if linear_violation > tolerance or target_violation > tolerance:
            report.update(complete=True, reason='Direct readback of the complete original row matrix failed')
            return None, None, report
        candidate = self.x+self.coordinates.lift(z)
        if not np.isfinite(candidate).all():
            report.update(complete=True, reason='The corrected full physical point is nonfinite')
            return None, None, report
        report['corrected_fixed_rows'] = self.read_fixed_values(candidate)
        if not report['corrected_fixed_rows']['complete']:
            report.update(complete=True, reason='The corrected complete fixed-row nonlinear read failed')
            return None, None, report
        report.update(complete=True, proposal_available=True,
            candidate_coordinate_sha256=self.base.array_sha(candidate),
            reason='Proposal only; independently reread A*z, same true Phi, positive domain and full geometry/permanent memory')
        return candidate, z, report

