#!/usr/bin/env python3
"""One complete-parent-row SOC, with optional newly rejected point rows.

All original QP rows remain literal inequalities.  Additional rows, if
requested, are evaluated and differentiated at the SAME parent in the SAME
full variables and appended without replacing the original C or its bounds.
The numerical projection is the published R683 all-halfspace solver.  The
true corrected objective and the full grid/permanent geometry acceptance
are the outer driver's responsibility.  No continuous certificate follows.

This module has no objective-specific derivative: the complete moving-mean
or frozen-target A/J/J* and the original mother norm stay in the caller.
Only public repository Actions may execute scientific functions here.
"""
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys

import numpy as np


SCHEMA = 'complete-original-QP-and-separated-amplitude-SOC-v1'
PROJECTION_SHA = 'a2c6d334d40be88ac7edb2dd2e525da5583d9f723e33d5bae9d910c0adfe745e'
AMPLITUDE_SHA = 'd494f92a3d212c40c8b602588c8cfe74f01ff332f116992ffca6469b3978ad8e'
INEQUALITY_SHA = 'e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8'
TAIL_SHA = '2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216'
SIX_KEYS = ('F', 'Fs', 'Fphi', 'Fss', 'Fsphi', 'Fphiphi')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Complete typed-row SOC runs only in public repository Actions')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_projection(path):
    path = Path(path).resolve()
    if sha(path) != PROJECTION_SHA:
        raise ValueError('Use the complete published R683 original-halfspace projection kernel')
    name = 'complete_typed_SOC_published_all_halfspaces'
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def finite(value, name, *, lower=None, strict=False):
    if isinstance(value, bool):
        raise ValueError(name+' must be a numerical scalar')
    value = float(value)
    if not math.isfinite(value) or (lower is not None and
            (value <= lower if strict else value < lower)):
        raise ValueError('Invalid finite SOC scalar: '+name)
    return value


class CompleteRowsSOC:
    """Keep one parent's complete C/b and typed nonlinear row definitions.

    No forged old-schema report or weakened old source binder is used.  This
    constructor binds the actual new combined-row schema independently.  It
    consumes only the R683 projection algebra, not its old row-type binder.
    """
    def __init__(self, problem, parent_x, row_matrix, bounds, metadata, *,
                 geometry_module, point_module, observed_module, inequality_module,
                 amplitude_module, budgets, projection_source,
                 source_sha256_by_role, observation_carrier_sha256,
                 model_definition, parent_bundle_sha256, block_columns=32768,
                 absolute_curvature_cap=None):
        require_actions()
        self.q = problem
        self.x = np.array(parent_x, dtype=float, copy=True)
        self.C = row_matrix
        self.b = np.array(bounds, dtype=float, copy=True)
        self.rows = json.loads(json.dumps(metadata['rows'], allow_nan=False))
        self.geometry, self.point, self.observed = geometry_module, point_module, observed_module
        self.amplitude, self.budgets = amplitude_module, budgets
        self.base = load_projection(projection_source)
        self.sources = dict(source_sha256_by_role)
        self.block_columns = int(block_columns)
        if self.block_columns != block_columns or self.block_columns < 1:
            raise ValueError('A positive exact column block width is required')
        if self.x.shape != (problem.free_size,) or not np.isfinite(self.x).all():
            raise ValueError('The SOC parent must be the full current real free vector')
        if (self.C.ndim != 2 or self.C.dtype != np.dtype('float64')
                or self.C.shape[1] < 1 or self.b.shape != (len(self.C),)
                or not np.isfinite(self.b).all() or len(self.rows) != len(self.C)):
            raise ValueError('Bind the literal same full C, bounds and row records')
        if (not isinstance(self.C, np.memmap)
                or Path(self.C.filename).resolve() != Path(metadata['row_cache']).resolve()):
            raise ValueError('SOC needs the actual combined parent mmap row cache')
        if (sha(amplitude_module.__file__) != AMPLITUDE_SHA
                or self.sources.get('amplitude_rows') != AMPLITUDE_SHA
                or metadata.get('schema') != amplitude_module.SCHEMA):
            raise ValueError('Unknown complete amplitude-row source or semantics')
        amplitude_module.validate_point_source(point_module)
        amplitude_module._validate_budget_problem(problem, budgets)
        if metadata['amplitude']['budgets'] != budgets.metadata():
            raise ValueError('The parent C was made with another fixed D/L/H budget')
        for role, module in (('geometry', geometry_module), ('point', point_module),
                             ('implementation', observed_module), ('inequalities', inequality_module)):
            if self.sources.get(role) != sha(module.__file__):
                raise ValueError('Actual parent component source differs: '+role)
        if self.sources.get('inequalities') != INEQUALITY_SHA:
            raise ValueError('Retain the original v2 curvature-product row definition')
        context = getattr(problem, 'reference_tail_context', None)
        if (context is None or model_definition != context.definition()
                or model_definition.get('source_sha256') != TAIL_SHA
                or self.sources.get('exact_tail') != TAIL_SHA
                or model_definition.get('original_observation_carrier_sha256') != observation_carrier_sha256
                or model_definition.get('M') != problem.M):
            raise ValueError('SOC must read the same actual canonical R671 physical field/carrier')
        if (sha(geometry_module.fields_block.__code__.co_filename) != TAIL_SHA
                or sha(point_module.fields_at.__code__.co_filename) != TAIL_SHA):
            raise ValueError('The physical six-jet adapters differ from the current field')
        self.reach_ratio = finite(metadata['reach_ratio'], 'reach ratio', lower=0, strict=True)
        self.safety = finite(metadata['safety'], 'original numerical safety', lower=0, strict=True)
        if self.safety >= 1:
            raise ValueError('Keep the original reach screen strictly below one')
        self.absolute_cap = (None if absolute_curvature_cap is None else
            finite(absolute_curvature_cap, 'absolute curvature cap', lower=0, strict=True))
        self.original_qp_row_count = len(self.C)
        self.original_curvature_row_count = int(metadata['amplitude']['original_prefix_rows'])
        if (not 0 <= self.original_curvature_row_count <= len(self.C)
                or metadata['amplitude']['appended_rows'] != len(self.C)-self.original_curvature_row_count):
            raise ValueError('Keep the complete old-curvature prefix and every amplitude row')
        self.identity = dict(schema=SCHEMA, parent_bundle_sha256=parent_bundle_sha256,
            parent_coordinate_sha256=self.base.array_sha(self.x),
            parent_rows_metadata_sha256=self.base.canonical_sha(metadata),
            original_parent_row_cache=str(Path(self.C.filename).resolve()),
            original_parent_row_cache_bytes=int(self.C.size*8),
            original_QP_rows=len(self.C), original_curvature_prefix_rows=self.original_curvature_row_count,
            coordinate_size=int(self.C.shape[1]), original_free_size=problem.free_size,
            observation_carrier_sha256=observation_carrier_sha256,
            source_sha256_by_role=self.sources, canonical_model=model_definition,
            budgets=budgets.metadata(), absolute_curvature_cap=self.absolute_cap,
            projection_source_sha256=PROJECTION_SHA, typed_source_sha256=sha(__file__),
            old_binders_not_relaxed=True)
        for i, row in enumerate(self.rows):
            self._validate_row(row, i, self.b[i], original=True)
        kinds = [row.get('constraint_kind') for row in self.rows]
        if kinds.count('cap_diameter') != 1 or kinds.count('height_floor') != 1:
            raise ValueError('The complete parent must retain its mandatory cap and H rows')
        self.attempted = False
        self.extra_rows = []

    def _curvature_location(self, value):
        # This published pure address validator only uses self.q.  No old
        # constructor/schema/source guard is bypassed or invoked here.
        return self.base.ParentRowsSOC._curvature_location(self, value)

    def _radius_location(self, value):
        return self.base.ParentRowsSOC._radius_location(self, value)

    def _validate_row(self, row, index, bound, *, original):
        if row.get('index') != index or float(row['normalized_bound']) != float(bound):
            raise ValueError('SOC literal row order or bound changed')
        kind = row.get('constraint_kind')
        if kind is None or kind == 'separated_curvature_product':
            if original and index >= self.original_curvature_row_count:
                raise ValueError('An appended parent amplitude row lost its type')
            norm = finite(row['gradient_coordinate_norm'], 'physical row norm', lower=0, strict=True)
            value = finite(row['current_product'], 'parent physical product', lower=0)
            if (row['actual_product_margin'] != self.safety-value
                    or (self.safety-value)/norm != float(bound)):
                raise ValueError('The original product margin or its normalization changed')
            self._curvature_location(row['curvature_point'])
            self._radius_location(row['radius_point'])
        elif kind == 'separated_absolute_curvature':
            norm = finite(row['gradient_coordinate_norm'], 'absolute-cap norm', lower=0, strict=True)
            if self.absolute_cap is None or row['upper_bound'] != self.absolute_cap:
                raise ValueError('An absolute curvature row needs this exact declared cap')
            if -float(row['current_inequality_value'])/norm != float(bound):
                raise ValueError('Absolute-cap row has a different normalized margin')
            self._curvature_location(row['curvature_point'])
        elif kind in ('body_diameter', 'witness_distance', 'cap_diameter', 'height_floor'):
            if original and index < self.original_curvature_row_count:
                raise ValueError('A typed row replaced part of the original curvature prefix')
            norm = finite(row['gradient_coordinate_norm'], 'amplitude row norm', lower=0)
            scale = norm if norm > 0 else 1.0
            value = finite(row['current_inequality_value'], 'parent amplitude value')
            if (row['row_normalization_scale'] != scale or row['current_product'] != value
                    or row['actual_inequality_margin'] != -value
                    or -value/scale != float(bound)):
                raise ValueError('The parent amplitude g<=0 or fixed normalization changed')
            if kind in ('body_diameter', 'witness_distance'):
                self.amplitude._location(self.q, row['point_location'])
            if kind == 'witness_distance' and row.get('sign') not in (-1, 1):
                raise ValueError('Keep the explicit phase-witness sign')
        else:
            raise ValueError('Unknown typed nonlinear SOC row')

    def _point_location(self, value):
        """Convert an ACTUAL full-screen maximum back to a literal row address."""
        if 'stage' in value:
            stage = int(value['stage'])
            phi = float(value['phi'])
            matches = np.flatnonzero(np.asarray(self.q.phi) == phi)
            if len(matches) != 1 or not 0 <= stage < self.q.P:
                raise ValueError('A reported maximum is not an exact actual grid angle/stage')
            return ('grid', stage, int(matches[0]))
        return self._curvature_location(('arbitrary', value['cell'], value['u'], value['phi'], 0))[:-1]

    def _fields(self, prepared, location, cache):
        key = tuple(location)
        if key not in cache:
            if key[0] == 'grid':
                fields = self.geometry.single_fields(self.q, prepared, key[1], key[2])
            elif key[0] == 'arbitrary':
                fields = self.point.fields_at(self.q, prepared, *key[1:], self.observed)
            else:
                raise ValueError('A literal point address must have an explicit type')
            if set(fields) != set(SIX_KEYS) or any(np.shape(fields[k]) != (3,) for k in SIX_KEYS):
                raise ValueError('The bound physical reader changed its complete six-jet interface')
            cache[key] = fields
        return cache[key]

    def _pullback(self, prepared, location, cotangent):
        if location[0] == 'grid':
            return self.point.pullback(self.q, prepared, location[1], location[2], cotangent)
        return self.point.pullback_at(self.q, prepared, *location[1:], cotangent, self.observed)

    def read_fixed_values(self, point):
        """Reread every typed row using its ORIGINAL parent normalization."""
        require_actions()
        point = np.asarray(point)
        if point.shape != self.x.shape or np.iscomplexobj(point) or not np.isfinite(point).all():
            raise ValueError('The typed-row trial must be the actual full finite real field vector')
        records = []
        residuals = np.empty(len(self.rows))
        try:
            p = self.q.prepare(point)
            fields, curvature, diameters = {}, {}, {}
            r0 = self.amplitude.current_witness_radius(self.q, p)
            scalar_values = self.amplitude.scalar_values(p.height, self.budgets)
            for i, row in enumerate(self.rows):
                kind = row.get('constraint_kind')
                if kind is None or kind in ('separated_curvature_product', 'separated_absolute_curvature'):
                    loc = self._curvature_location(row['curvature_point'])
                    if loc not in curvature:
                        f = self._fields(p, loc[:-1], fields)
                        if not all(np.isfinite(f[k]).all() for k in SIX_KEYS):
                            return dict(complete=False, failed_row=i, reason='nonfinite_six_jets', rows=records)
                        area = float(np.linalg.norm(np.cross(f['Fs'], f['Fphi'])))
                        if not math.isfinite(area) or area <= 0:
                            return dict(complete=False, failed_row=i, reason='nonpositive_area', rows=records)
                        value, _, principal = self.geometry.curvature_cotangent(f, loc[-1])
                        if not math.isfinite(value) or not math.isfinite(principal['principal_gap']):
                            return dict(complete=False, failed_row=i, reason='nonfinite_principal_value', rows=records)
                        curvature[loc] = (float(value), float(principal['principal_gap']), area)
                    value, gap, area = curvature[loc]
                    norm = float(row['gradient_coordinate_norm'])
                    details = dict(curvature_point=list(loc), signed_curvature=value,
                        principal_gap=gap, area=area,
                        curvature_sign_changed=row['signed_curvature']*value <= 0)
                    if kind == 'separated_absolute_curvature':
                        g = abs(value)-self.absolute_cap
                        details.update(upper_bound=self.absolute_cap, absolute_curvature=abs(value))
                    else:
                        rloc = self._radius_location(row['radius_point'])
                        if rloc not in diameters:
                            if rloc[0] == 'fixed_core':
                                D = 2.0
                            elif rloc[0] == 'cap_height':
                                D = 2*abs(float(p.height))
                            else:
                                key = 'grid' if rloc[0] == 'grid_radius' else 'arbitrary'
                                D = 2*float(np.linalg.norm(self._fields(p, (key, *rloc[1:]), fields)['F']))
                            if not math.isfinite(D) or D <= 0:
                                return dict(complete=False, failed_row=i, reason='nonpositive_partner_D', rows=records)
                            diameters[rloc] = D
                        D = diameters[rloc]
                        product = self.reach_ratio*D*abs(value)
                        g = product-self.safety
                        details.update(radius_point=list(rloc), diameter=D, product=product,
                            upper_bound=self.safety)
                    scale = norm
                else:
                    scale = float(row['row_normalization_scale'])
                    if kind in ('cap_diameter', 'height_floor'):
                        g = scalar_values[kind]
                        details = dict(height=float(p.height))
                    else:
                        loc, _ = self.amplitude._location(self.q, row['point_location'])
                        key = (('grid', loc['stage'], loc['angle']) if loc['kind'] == 'grid'
                               else ('arbitrary', loc['cell'], loc['u'], loc['phi']))
                        F = self._fields(p, key, fields)['F']
                        values = self.amplitude.point_values(F, loc['phi'], r0, self.budgets)
                        field = ('body_diameter' if kind == 'body_diameter'
                                 else 'witness_plus' if row['sign'] == 1 else 'witness_minus')
                        g = float(values[field])
                        details = dict(point_location=loc, sign=row.get('sign'), current_witness_radius=float(r0))
                residuals[i] = g/scale
                if not math.isfinite(float(residuals[i])):
                    return dict(complete=False, failed_row=i, reason='nonfinite_typed_row_value', rows=records)
                records.append(dict(index=i, constraint_kind=kind or 'original_curvature_product',
                    unnormalized_inequality_value=float(g), parent_normalization_scale=scale,
                    normalized_constraint_value=float(residuals[i]), **details))
        except (FloatingPointError, OverflowError, np.linalg.LinAlgError) as error:
            return dict(complete=False, failed_row=len(records), reason='numeric_typed_point_read_failure',
                arithmetic_error=repr(error), rows=records)
        return dict(complete=True, coordinate_sha256=self.base.array_sha(point), rows=records,
            normalized_constraints=residuals.tolist(),
            maximum_normalized_constraint=float(np.max(residuals, initial=-float('inf'))),
            positive_normalized_rows=np.flatnonzero(residuals > 0).tolist(),
            fixed_parent_scales=True, trial_partner_reselected_inside_existing_rows=False,
            all_original_QP_rows_retained=True, current_total_rows=len(self.rows),
            finite_values_are_not_continuous_geometry_certificates=True)

    def _parent_product_row(self, loc, rloc, transpose, *, absolute=False):
        p = self.q.prepare(self.x)
        cache = {}
        f = self._fields(p, loc[:-1], cache)
        value, cotangent, principal = self.geometry.curvature_cotangent(f, loc[-1])
        if not math.isfinite(value) or not math.isfinite(principal['principal_gap']):
            raise FloatingPointError('Nonfinite actual parent curvature at a separated address')
        dk = self._pullback(p, loc[:-1], cotangent)
        if absolute:
            g = abs(value)-self.absolute_cap
            gradient = np.sign(value)*dk
            record = dict(constraint_kind='separated_absolute_curvature',
                current_inequality_value=float(g), current_product=float(g), upper_bound=self.absolute_cap,
                curvature_point=list(loc), signed_curvature=float(value), principal_metadata=principal)
        else:
            if rloc[0] == 'fixed_core':
                D = 2.0; dD = np.zeros(self.q.free_size)
            elif rloc[0] == 'cap_height':
                D = 2*abs(float(p.height)); dD = np.zeros(self.q.free_size)
                dD[-1] = 2*np.sign(p.height)
            else:
                key = 'grid' if rloc[0] == 'grid_radius' else 'arbitrary'
                rf = self._fields(p, (key, *rloc[1:]), cache)
                D = 2*float(np.linalg.norm(rf['F']))
                if not math.isfinite(D) or D <= 0:
                    raise FloatingPointError('Nonpositive actual parent diameter partner')
                cot = {key: np.zeros(3) for key in SIX_KEYS}
                cot['F'] = 4*rf['F']/D
                dD = self._pullback(p, (key, *rloc[1:]), cot)
            product = self.reach_ratio*D*abs(value)
            g = product-self.safety
            gradient = self.reach_ratio*(D*np.sign(value)*dk+abs(value)*dD)
            record = dict(constraint_kind='separated_curvature_product', current_product=float(product),
                actual_product_margin=float(self.safety-product), curvature_point=list(loc),
                radius_point=list(rloc), signed_curvature=float(value), diameter=float(D),
                principal_metadata=principal)
        row = np.asarray(transpose(gradient))
        norm = float(np.linalg.norm(row))
        if row.shape != (self.C.shape[1],) or not np.isfinite(row).all() or not math.isfinite(norm) or norm <= 0:
            raise FloatingPointError('Unavailable finite parent row norm at a separated address')
        record.update(gradient_coordinate_norm=norm, normalized_bound=float(-g/norm),
            derived_at_original_parent=True, protected_inequality=True)
        return row/norm, -g/norm, record

    def extend_from_rejected_extrema(self, trial_geometry, transpose, workdir, *, actual_filter):
        """Append actual rejected K/D and amplitude extrema at the original x.

        This is a finite separation step, not all-point linearization. Every
        earlier C row stays. Both principal branches are appended for the
        current worst curvature, paired with the current true diameter
        partner. Every violated amplitude maximum contributes its explicit
        original sign. A negative new parent margin stops this extension:
        it needs honest restoration or another parent, not a feasible-zero
        claim. The caller still screens ALL nonlinear locations afterward.
        """
        require_actions()
        if self.attempted:
            raise ValueError('Extend only before this direction consumes its one SOC proposal')
        if trial_geometry.get('complete') is not True:
            return dict(complete=False, extension_available=False, reason='Incomplete rejected geometry')
        additions = []
        existing = set()
        for row in self.rows:
            kind = row.get('constraint_kind')
            if kind is None or kind == 'separated_curvature_product':
                existing.add(('product', tuple(row['curvature_point']), tuple(row['radius_point'])))
            elif kind == 'separated_absolute_curvature':
                existing.add(('absolute', tuple(row['curvature_point'])))
            elif kind in ('body_diameter', 'witness_distance'):
                _, loc_key = self.amplitude._location(self.q, row['point_location'])
                existing.add((kind, loc_key, row.get('sign')))
        worst = trial_geometry.get('worst')
        radius = trial_geometry.get('maximum_radius_point')
        if worst is not None and actual_filter.get('passed') is False:
            loc = self._point_location(worst)
            full_filter = actual_filter
            D = float(full_filter['reference_diameter_lower_bound'])
            H = abs(float(full_filter['height']))
            point_D = float(trial_geometry.get('closed_body_diameter_point_lower', 0.0))
            if not math.isfinite(D) or D != max(2.0, 2*H, point_D):
                raise ValueError('Use the actual unchanged trial diameter normalization')
            if point_D >= max(2.0, 2*H) and radius is not None:
                point = self._point_location(radius)
                rloc = ('grid_radius', *point[1:]) if point[0] == 'grid' else ('arbitrary_radius', *point[1:])
            elif 2*H >= 2.0:
                rloc = ('cap_height',)
            else:
                rloc = ('fixed_core',)
            for branch in (0, 1):
                full_loc = (*loc, branch)
                key = ('product', full_loc, rloc)
                if key not in existing:
                    additions.append(self._parent_product_row(full_loc, rloc, transpose))
                    existing.add(key)
                key = ('absolute', full_loc)
                if self.absolute_cap is not None and key not in existing:
                    additions.append(self._parent_product_row(full_loc, rloc, transpose, absolute=True))
                    existing.add(key)
        p = self.q.prepare(self.x)
        screen = trial_geometry.get('amplitude_screen') or {}
        for key, item in (screen.get('maximum_inequality_by_kind') or {}).items():
            if not math.isfinite(float(item['value'])) or item['value'] <= 0:
                continue
            kind = 'body_diameter' if key == 'body_diameter' else 'witness_distance'
            sign = None if kind == 'body_diameter' else 1 if key == 'witness_plus' else -1
            loc, loc_key = self.amplitude._location(self.q, item['location'])
            row_key = (kind, loc_key, sign)
            if row_key in existing:
                continue
            value, gradient, details = self.amplitude.point_value_and_free_gradient(
                self.q, p, self.point, self.observed, item['location'], kind, sign, self.budgets)
            row = np.asarray(transpose(gradient)); norm = float(np.linalg.norm(row))
            if row.shape != (self.C.shape[1],) or not np.isfinite(row).all() or not math.isfinite(norm) or norm <= 0:
                raise FloatingPointError('Unavailable complete separated amplitude row')
            record = dict(constraint_kind=kind, current_inequality_value=value,
                actual_inequality_margin=-value, current_product=value, actual_product_margin=-value,
                row_normalization_scale=norm, gradient_coordinate_norm=norm, normalized_bound=-value/norm,
                point_location=loc, protected_inequality=True, derived_at_original_parent=True,
                **details)
            record['sign'] = sign
            additions.append((row/norm, -value/norm, record)); existing.add(row_key)
        negative = [dict(index=i, normalized_bound=float(bound), row=record)
                    for i, (_, bound, record) in enumerate(additions) if bound < 0]
        if negative:
            return dict(complete=True, extension_available=False,
                reason='A newly separated true address is not feasible at the actual parent; restoration or a qualifying parent is required',
                new_parent_violations=negative, original_rows_removed=False,
                negative_bound_used_as_feasible_zero=False, global_geometric_infeasibility_proved=False)
        if not additions:
            return dict(complete=True, extension_available=True, added_rows=0,
                reason='Every selected rejected extremum already has the same literal row/partner', original_rows_removed=False)
        directory = Path(workdir)
        directory.mkdir(parents=True, exist_ok=False)
        old = self.C; old_count = len(old)
        path = directory/'all-original-and-separated-SOC-rows.f64'
        C = np.memmap(path, dtype=np.float64, mode='w+', shape=(old_count+len(additions), old.shape[1]))
        for first in range(0, old.shape[1], self.block_columns):
            stop = min(old.shape[1], first+self.block_columns)
            C[:old_count, first:stop] = old[:, first:stop]
            C.flush(); self.base._discard(C); self.base._discard(old)
        new_bounds = []
        records = []
        for j, (row, bound, record) in enumerate(additions):
            index = old_count+j
            C[index] = row; record['index'] = index
            self._validate_row(record, index, bound, original=False)
            new_bounds.append(bound); records.append(record)
        C.flush(); self.base._discard(C)
        self.C = C; self.b = np.r_[self.b, new_bounds]; self.rows.extend(records)
        self.extra_rows.extend(records)
        return dict(complete=True, extension_available=True, added_rows=len(additions), rows=records,
            previous_total_rows=old_count, current_total_rows=len(self.C),
            current_cache=str(path), current_cache_bytes=int(self.C.size*8),
            original_QP_rows_retained=self.original_qp_row_count, original_rows_removed=False,
            parent_feasible_at_new_rows=True, scientific_field_J_calls=0,
            scope='New point covectors only, through complete original free pullbacks and T*; full nonlinear acceptance remains required')

    def propose(self, coordinate_step, lift, full_trial_point, full_trial, *,
                tau=0.0, inward_fraction=0.0, feasibility_tolerance=2e-11):
        require_actions()
        report = dict(schema=SCHEMA, source_sha256=sha(__file__), identity=self.identity,
            attempted=False, complete=False, proposal_available=False,
            original_QP_rows=self.original_qp_row_count, current_complete_rows=len(self.rows),
            appended_separation_rows=len(self.extra_rows), all_original_rows_retained=True,
            objective_acceptance_owned_by_outer_driver=True, full_geometry_acceptance_owned_by_outer_driver=True,
            fallback='Unchanged original parent+alpha*T*d ray; preserve every new location',
            continuous_geometry_certified=False, local_MFCQ_and_remainder_constants_established=False)
        geometry = full_trial.get('curvature_points') or {}
        eligible = (full_trial.get('alpha') == 1 and full_trial.get('finite') is True
            and full_trial.get('feasible') is True and full_trial.get('descent') is True
            and geometry.get('complete') is True
            and (geometry.get('amplitude_screen') or {}).get('complete') is True
            and (full_trial.get('curvature_feasible') is False or full_trial.get('amplitude_feasible') is False))
        if not eligible:
            report.update(complete=True, reason='Not a complete full-step true-Phi/domain-passing geometry rejection')
            return None, None, None, report
        if self.attempted:
            raise ValueError('This direction already consumed its one complete-row SOC proposal')
        self.attempted = True; report['attempted'] = True
        tau = finite(tau, 'cubic inward coefficient', lower=0)
        fraction = finite(inward_fraction, 'observed violation inward fraction', lower=0)
        tolerance = finite(feasibility_tolerance, 'direct complete-row feasibility tolerance', lower=0)
        d = np.asarray(coordinate_step)
        if d.shape != (self.C.shape[1],) or np.iscomplexobj(d) or not np.isfinite(d).all():
            raise ValueError('Keep the original complete augmented QP step')
        if not np.array_equal(np.asarray(full_trial_point), self.x+lift(d)):
            raise ValueError('The full rejected point is not the bound parent plus the SAME original T*d')
        cd = self.base._dot(self.C, d, self.block_columns)
        slack = self.b-cd
        original_violation = float(np.max(-slack[:self.original_qp_row_count], initial=0.0))
        report.update(original_QP_maximum_linear_violation=original_violation,
            all_current_linear_violation=float(np.max(-slack, initial=0.0)),
            original_augmented_step_sha256=self.base.array_sha(d))
        if original_violation > tolerance:
            report.update(complete=True, reason='The main QP step violates an ORIGINAL literal QP row')
            return None, None, None, report
        actual = self.read_fixed_values(full_trial_point)
        report['full_trial_fixed_parent_rows'] = actual
        if not actual['complete']:
            report.update(complete=True, reason='Cannot read every fixed-parent typed nonlinear row')
            return None, None, None, report
        r = np.asarray(actual['normalized_constraints'])
        maximum = float(np.max(r, initial=0.0))
        if maximum <= 0:
            report.update(complete=True, reason='No current fixed-parent row has positive nonlinear value; full rejection remains outside this finite linear row family')
            return None, None, None, report
        a = float(np.linalg.norm(d))
        if not math.isfinite(a) or a <= 0:
            report.update(complete=True, reason='No finite nonzero original direction for a correction')
            return None, None, None, report
        try:
            inward = tau*a**3+fraction*maximum
        except OverflowError:
            inward = float('inf')
        if not math.isfinite(inward):
            report.update(complete=True, reason='Nonfinite declared inward target')
            return None, None, None, report
        k = np.minimum(slack, -r-inward)
        report.update(tau=tau, inward_fraction=fraction, inward_normalized_offset=inward,
            inward_policy='tau*||d||^3 + inward_fraction*max_i(max(c_i(d),0)); fixed parent row scales',
            cubic_theorem_not_claimed_for_observed_fraction_policy=True,
            coordinate_norm=a, normalized_bounds=self.b.tolist(),
            original_complete_row_values=cd.tolist(),
            actual_nonlinear_minus_parent_linear=(r-(cd-self.b)).tolist(),
            correction_halfspace_bounds=k.tolist(),
            correction_policy='C*e<=min(b-C*d, -c(d)-inward) for EVERY original and appended row')
        e, projection = self.base.minimum_norm_halfspaces(self.C, k,
            block_columns=self.block_columns, feasibility_tolerance=tolerance,
            dual_tolerance=max(1e-14, min(1e-12, tolerance/16)), max_sweeps=20000, refresh_sweeps=64)
        report['constrained_projection'] = projection
        if e is None:
            report.update(complete=True, reason='No numerically feasible complete-row correction returned; no geometric impossibility claim')
            return None, None, None, report
        z = d+e
        ce = self.base._dot(self.C, e, self.block_columns)
        cz = self.base._dot(self.C, z, self.block_columns)
        violation = float(np.max(cz-self.b, initial=0.0))
        target_violation = float(np.max(r+inward+ce, initial=0.0))
        report.update(correction_norm=float(np.linalg.norm(e)),
            correction_over_original_norm=float(np.linalg.norm(e))/a,
            corrected_coordinate_norm=float(np.linalg.norm(z)),
            corrected_maximum_linear_violation=violation,
            corrected_all_nonlinear_target_linear_violation=target_violation,
            complete_original_row_direct_readback=True,
            direct_Cd_plus_Ce_discrepancy=float(np.max(np.abs(cz-cd-ce), initial=0.0)),
            correction_sha256=self.base.array_sha(e), corrected_step_sha256=self.base.array_sha(z))
        if violation > tolerance or target_violation > tolerance:
            report.update(complete=True, reason='Direct ORIGINAL complete-row correction readback failed')
            return None, None, None, report
        candidate = self.x+lift(z)
        if not np.isfinite(candidate).all():
            report.update(complete=True, reason='Nonfinite corrected physical candidate')
            return None, None, None, report
        report['corrected_fixed_parent_rows'] = self.read_fixed_values(candidate)
        if not report['corrected_fixed_parent_rows']['complete']:
            report.update(complete=True, reason='Corrected typed-row physical read is incomplete; no true acceptance can be claimed')
            return None, None, None, report
        report.update(complete=True, proposal_available=True,
            candidate_coordinate_sha256=self.base.array_sha(candidate),
            reason='Proposal only: outer driver must recompute A*z, same true Phi and full curvature/amplitude/memory',
            same_original_objective_norm_and_QP_retained=True,
            exact_minimum_norm_not_claimed_from_finite_dual_budget=True)
        return candidate, z, e, report
