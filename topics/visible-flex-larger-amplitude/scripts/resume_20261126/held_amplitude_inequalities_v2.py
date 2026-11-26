#!/usr/bin/env python3
"""Complete original-free-coordinate rows for fixed held-amplitude budgets.

This module only supplies finite point inequalities and their full transpose.
It does not replace the original objective, variables, mother norm, QP, ray
search, squared SOC, permanent-location memory, or continuous certificates.
The caller must screen EVERY declared grid/permanent point, with BOTH signs
of the phase witness at each quarter-domain point, on every nonlinear trial.

For marked-diameter budget D, marker height h=1/1000, body budget B<=D-2h,
and held-witness lower budget L>=D/5, the dimensionless inequalities are

    4 F.F/B^2 - 1 <= 0,
    1 - (F - sign*r0*u).(F - sign*r0*u)/L^2 <= 0,
    4 (R^2 + H^2)/B^2 - 1 <= 0,
    (max(L+h, H_min) - H)/L <= 0,

where u=(sin(phi),cos(phi),0), r0=1+sum(ALL current core coefficients),
R is the fixed terminal radius of the unchanged FullHold, and H_min>1.
The point pullback already pays the dependence of F on every free core
coefficient.  The moving witness adds ONE further constant to each entry
of the original free-core prefix BEFORE applying the unchanged T*.

Scientific execution is restricted to the public repository's Actions.
Importing/compiling this source alone is not a numerical validation.
"""
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import math
import mmap
import os
from pathlib import Path

import numpy as np


SCHEMA = 'complete-held-amplitude-budget-rows-v1'
POINT_SOURCE_SHA256 = 'fe8e926c3239d707d6af48efbc48c1755bbac84c3d5722bdbf40f7be7bb53cad'
TAIL_POINT_ADAPTER_SHA256 = '2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216'
SIX_KEYS = ('F', 'Fs', 'Fphi', 'Fss', 'Fsphi', 'Fphiphi')
MARKER_HEIGHT_EXACT = Fraction(1, 1000)


def _require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific amplitude-row evaluations run only in the public repository Actions')


def _sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _round_fraction(value, upward):
    rounded = float(value)
    if not math.isfinite(rounded):
        raise ValueError('A finite declared scalar budget is required')
    exact_rounded = Fraction.from_float(rounded)
    if (upward and exact_rounded < value) or (not upward and exact_rounded > value):
        rounded = math.nextafter(rounded, math.inf if upward else -math.inf)
    return rounded


@dataclass(frozen=True)
class Budgets:
    """Fixed design budgets, not estimates recomputed from a trial candidate.

    Inputs are interpreted as their exact binary64 values.  The body budget
    is rounded DOWN from D-2/1000, and the amplitude height floor is rounded
    UP from L+1/1000.  These scalar precautions do not make point evaluations
    or finite scans into outward continuous certificates.
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
                raise ValueError('Every fixed amplitude budget must be finite')
            object.__setattr__(self, name, value)
        D = Fraction.from_float(self.marked_diameter_budget)
        L = Fraction.from_float(self.witness_lower_budget)
        R = Fraction.from_float(self.cap_radius)
        H = Fraction.from_float(self.height_floor)
        if not 2*MARKER_HEIGHT_EXACT < D <= Fraction(9, 2):
            raise ValueError('Need 2h < marked diameter budget <= 4.5 for the fixed 0.9 grip diameter')
        if L <= 0 or 5*L < D:
            raise ValueError('The fixed held-witness budget must be at least one fifth of marked D')
        if R <= Fraction(9, 20):
            raise ValueError('The unchanged FullHold cap radius must contain the fixed radius-0.45 grip')
        if H <= 1:
            raise ValueError('An explicit fixed height floor strictly greater than 1 is required')

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
            cap_radius=self.cap_radius, height_floor=self.height_floor,
            cap_radius_carrier_hex=self.cap_radius.hex(),
            amplitude_height_floor=self.amplitude_height_floor,
            effective_height_floor=self.effective_height_floor,
            marker_height_exact='1/1000', fixed_grip_diameter=0.9,
            body_budget_rounding='downward from exact binary64 marked budget minus 2/1000',
            amplitude_height_rounding='upward from exact binary64 witness budget plus 1/1000',
            fixed_during_direction_and_all_trial_reads=True,
            cap_radius_scope='fixed terminal radius of the SAME unchanged FullHold; not a free variable',
            scope='Numerical design budgets; final continuous certification must use the actual same field and exact FullHold')


def _layout(problem, prepared=None, x=None):
    M, K, J, n = (int(problem.M), int(problem.K), int(problem.J), int(problem.n))
    if M < 1 or not 0 <= K <= M or J < 2 or n != 3*M+2:
        raise ValueError('This helper requires the original complete Fourier/three-jet layout')
    expected = (M-K)+(2*M+1)+3*(J-2)*n+1
    if int(problem.free_size) != expected:
        raise ValueError('Original free-core prefix / interior jets / final H layout mismatch')
    if prepared is not None:
        core = np.asarray(prepared.core)
        if core.shape != (M,):
            raise ValueError('The phase witness uses ALL current core coefficients')
        if x is not None:
            point = np.asarray(x)
            if point.shape != (expected,):
                raise ValueError('Wrong original full-free point shape')
            if not np.array_equal(core[K:], point[:M-K]):
                raise ValueError('Prepared core does not match this actual original free-core prefix')
            if prepared.height != point[-1]:
                raise ValueError('Prepared height does not match this actual original last coordinate')
    return M-K


def validate_point_source(point_module):
    source = Path(point_module.__file__).resolve()
    if _sha(source) != POINT_SOURCE_SHA256:
        raise ValueError('Use the byte-bound complete six-jet point pullback; do not omit a core/lift branch')
    adapter = getattr(point_module, 'reference_tail_adapter_source_sha256', None)
    if adapter != TAIL_POINT_ADAPTER_SHA256:
        raise ValueError('Use the SAME canonical R671 exact-tail adapter, including its fixed k position offset')
    adapter_sources = {}
    for name in ('fields_at', 'pullback_at'):
        function = getattr(point_module, name)
        path = Path(function.__code__.co_filename).resolve()
        if _sha(path) != TAIL_POINT_ADAPTER_SHA256:
            raise ValueError('The actual exact-tail point entry differs from its recorded source: '+name)
        adapter_sources[name] = dict(path=str(path), sha256=TAIL_POINT_ADAPTER_SHA256)
    return dict(path=str(source), sha256=POINT_SOURCE_SHA256,
        canonical_exact_tail_adapter=adapter_sources)


def _validate_budget_problem(problem, budgets):
    if not isinstance(budgets, Budgets):
        raise TypeError('Use one explicit immutable Budgets instance for the whole step and ray')
    if float(problem.R).hex() != budgets.cap_radius.hex():
        raise ValueError('The cap budget must use this SAME unchanged FullHold R carrier')


def current_witness_radius(problem, prepared):
    """r0 from this candidate, including the fixed and free core entries."""
    _require_actions()
    _layout(problem, prepared)
    core = np.asarray(prepared.core)
    if not np.isfinite(core).all():
        raise ValueError('Nonfinite current core in the actual phase witness')
    return 1.0+np.sum(core)


def _point_values(F, phi, r0, budgets):
    """Bilinear analytic formulas, also used by the new complex-step check."""
    F = np.asarray(F)
    angle = np.asarray(phi)
    u = np.stack((np.sin(angle), np.cos(angle), np.zeros_like(angle)), axis=-1)
    B = budgets.body_diameter_budget
    L = budgets.witness_lower_budget
    plus = F-r0*u
    minus = F+r0*u
    return dict(body_diameter=4*np.sum(F*F, axis=-1)/(B*B)-1,
        witness_plus=1-np.sum(plus*plus, axis=-1)/(L*L),
        witness_minus=1-np.sum(minus*minus, axis=-1)/(L*L))


def point_values(F, phi, r0, budgets):
    """Vectorized TRUE values for grid/permanent screening, both signs.

    No orbit multiplicity or mean is taken: every individual point and both
    witness branches are separate inequalities.  F is in the existing
    rotated-phi orthonormal frame.  An input failure must reject the trial.
    """
    _require_actions()
    F = np.asarray(F)
    angle = np.asarray(phi)
    if (F.ndim < 1 or F.shape[-1] != 3 or np.ndim(r0) != 0
            or np.iscomplexobj(F) or np.iscomplexobj(angle) or np.iscomplexobj(r0)):
        raise ValueError('A true point screen requires real physical positions and current r0')
    if not (np.isfinite(F).all() and np.isfinite(angle).all() and np.isfinite(r0)):
        raise ValueError('Nonfinite physical value in held-amplitude point screen')
    return _point_values(F, angle, r0, budgets)


def _scalar_values(height, budgets):
    B = budgets.body_diameter_budget
    L = budgets.witness_lower_budget
    return dict(cap_diameter=4*(budgets.cap_radius**2+height*height)/(B*B)-1,
        height_floor=(budgets.effective_height_floor-height)/L)


def scalar_values(height, budgets):
    """Two mandatory true scalar screens, including the H>1 marker floor."""
    _require_actions()
    if np.iscomplexobj(height) or not np.isfinite(height):
        raise ValueError('A true scalar screen requires finite real current H')
    return _scalar_values(float(height), budgets)


def _location(problem, location):
    if 'stage' in location or 'angle' in location:
        if 'stage' not in location or 'angle' not in location:
            raise ValueError('A grid location needs both its current stage and angle indices')
        stage, angle = int(location['stage']), int(location['angle'])
        if not 0 <= stage < problem.P or not 0 <= angle < problem.N:
            raise ValueError('Grid amplitude location outside the actual current observation carrier')
        phi = float(problem.phi[angle])
        result = dict(kind='grid', stage=stage, angle=angle, phi=phi)
        if hasattr(problem, 'observation_cells'):
            result.update(cell=int(problem.observation_cells[stage]),
                u=float(problem.observation_u[stage]))
        return result, ('grid', stage, angle)
    if not all(key in location for key in ('cell', 'u', 'phi')):
        raise ValueError('An arbitrary point needs exact current-carrier cell/u/phi')
    cell, u, phi = int(location['cell']), float(location['u']), float(location['phi'])
    if not 0 <= cell < problem.J-1 or not 0 <= u <= 1 or not math.isfinite(phi):
        raise ValueError('Arbitrary amplitude witness outside an actual original closed cell')
    return dict(kind='arbitrary', cell=cell, u=u, phi=phi), ('arbitrary', cell, u.hex(), phi.hex())


def _fields(problem, prepared, point_module, observed_module, location):
    if location['kind'] == 'grid':
        jets = problem.six_jets(prepared, location['stage'])
        return {key: np.asarray(jets[key][location['angle']]) for key in SIX_KEYS}
    if observed_module is None:
        raise ValueError('Arbitrary amplitude locations require the actual original Hermite source')
    return point_module.fields_at(problem, prepared, location['cell'], location['u'],
                                  location['phi'], observed_module)


def _point_covector(problem, prepared, point_module, observed_module,
                     location, kind, sign, budgets, fields=None):
    if kind not in ('body_diameter', 'witness_distance'):
        raise ValueError('Unsupported amplitude point row kind')
    free_core_count = _layout(problem, prepared)
    fields = (_fields(problem, prepared, point_module, observed_module, location)
              if fields is None else fields)
    F = np.asarray(fields['F'])
    if F.shape != (3,) or np.iscomplexobj(F) or not np.isfinite(F).all():
        raise ValueError('A selected point covector needs the actual finite real three-position')
    cot = {key: np.zeros(3) for key in SIX_KEYS}
    extra_core = 0.0
    B, L = budgets.body_diameter_budget, budgets.witness_lower_budget
    if kind == 'body_diameter':
        value = 4*float(F@F)/(B*B)-1
        cot['F'] = 8*F/(B*B)
        details = dict(radius_squared=float(F@F))
    else:
        if sign not in (-1, 1):
            raise ValueError('A witness-distance row needs the explicit sign +1 or -1')
        r0 = current_witness_radius(problem, prepared)
        if np.iscomplexobj(r0):
            raise ValueError('A selected real point row cannot use a complex current core')
        u = np.array([np.sin(location['phi']), np.cos(location['phi']), 0.0])
        w = F-sign*r0*u
        value = 1-float(w@w)/(L*L)
        cot['F'] = -2*w/(L*L)
        # F(core) is ALREADY fully paid by point_module.pullback below.
        # Only dp_current = sign*u*sum(delta_free_core) is added here.
        extra_core = 2*sign*float(w@u)/(L*L)
        details = dict(sign=int(sign), current_witness_radius=float(r0),
            distance_squared=float(w@w), extra_each_original_free_core_entry=extra_core,
            extra_free_core_entries=free_core_count,
            p_current_differentiated=True, F_core_chain_paid_by_original_point_source=True)
    if location['kind'] == 'grid':
        gradient = point_module.pullback(problem, prepared, location['stage'],
                                         location['angle'], cot)
    else:
        gradient = point_module.pullback_at(problem, prepared, location['cell'],
            location['u'], location['phi'], cot, observed_module)
    gradient = np.asarray(gradient)
    if gradient.shape != (problem.free_size,) or np.iscomplexobj(gradient):
        raise ValueError('The physical point source did not return the full original real free covector')
    if kind == 'witness_distance':
        gradient[:free_core_count] += extra_core
    if not math.isfinite(value) or not np.isfinite(gradient).all():
        raise ValueError('Nonfinite complete amplitude value or original-free gradient')
    return float(value), gradient, details


def point_value_and_free_gradient(problem, prepared, point_module, observed_module,
                                  location, kind, sign, budgets):
    """One complete covector in ORIGINAL variables, before the caller's T*."""
    _require_actions()
    validate_point_source(point_module)
    _validate_budget_problem(problem, budgets)
    loc, _ = _location(problem, location)
    return _point_covector(problem, prepared, point_module, observed_module,
                           loc, kind, sign, budgets)


def _scalar_covector(problem, prepared, kind, budgets):
    gradient = np.zeros(problem.free_size)
    values = scalar_values(prepared.height, budgets)
    if kind == 'cap_diameter':
        gradient[-1] = 8*prepared.height/(budgets.body_diameter_budget**2)
    elif kind == 'height_floor':
        gradient[-1] = -1/budgets.witness_lower_budget
    else:
        raise ValueError('Unknown scalar amplitude row')
    return float(values[kind]), gradient, dict(only_original_last_H_entry=True,
        cap_radius_has_no_free_derivative=True)


def build_selected_rows(problem, x, point_module, observed_module, transpose,
                        coordinate_size, *, budgets, selections,
                        matrix_workdir, block_columns=32768, prefix=None):
    """Append selected amplitude rows and mandatory cap/H rows in one mmap.

    Each selection is {kind: 'body_diameter' or 'witness_distance',
    location: {stage,angle} or {cell,u,phi}, sign: +/-1, protected: bool}.
    For witness_distance, omitting sign explicitly requests BOTH signs.
    Exact duplicate selected rows are combined only by exact binary location
    identity plus kind/sign; no decimal rounding or neighborhood merging.
    Grid and arbitrary observation identities remain distinct.

    prefix, if supplied, is the actual original (C,b,metadata).  Its rows and
    metadata are copied unchanged, with bounded column blocks, before new
    rows.  This helper never recomputes or replaces the original constraints.
    The caller owns selection and complete nonlinear permanent-point memory.
    """
    _require_actions()
    point_identity = validate_point_source(point_module)
    _validate_budget_problem(problem, budgets)
    if int(coordinate_size) != coordinate_size or coordinate_size < 1 or block_columns < 1:
        raise ValueError('Need positive actual coordinate size and row-cache block width')
    coordinate_size = int(coordinate_size)
    p = problem.prepare(x)
    _layout(problem, p, x)
    selected = []
    seen = {}
    requested = 0
    for item in selections:
        kind = item['kind']
        if kind not in ('body_diameter', 'witness_distance'):
            raise ValueError('Only physical point row kinds belong in selections')
        loc, loc_key = _location(problem, item['location'])
        signs = ((None,) if kind == 'body_diameter'
                 else (item['sign'],) if 'sign' in item else (1, -1))
        for sign in signs:
            if kind == 'witness_distance' and sign not in (-1, 1):
                raise ValueError('Distance sign must be exactly +/-1')
            requested += 1
            key = (kind, loc_key, sign)
            if key in seen:
                selected[seen[key]]['protected'] |= bool(item.get('protected', False))
                continue
            seen[key] = len(selected)
            selected.append(dict(kind=kind, location=loc, sign=sign,
                protected=bool(item.get('protected', False))))
    selected.extend(dict(kind=kind, protected=True)
                    for kind in ('cap_diameter', 'height_floor'))
    if prefix is None:
        old_rows = np.empty((0, coordinate_size))
        old_bounds = np.empty(0)
        old_metadata = {}
    else:
        old_rows, old_bounds, old_metadata = prefix
        if old_rows.ndim != 2 or old_rows.shape[1] != coordinate_size:
            raise ValueError('Prefix rows must use the SAME unchanged full coordinates')
        old_bounds = np.asarray(old_bounds)
        if old_bounds.shape != (len(old_rows),) or not np.isfinite(old_bounds).all():
            raise ValueError('Invalid actual prefix inequality bounds')
        if len(old_metadata.get('rows', ())) != len(old_rows):
            raise ValueError('Keep one original metadata record for every prefix row')
    old_count = len(old_rows)
    count = old_count+len(selected)
    directory = Path(matrix_workdir)
    directory.mkdir(parents=True, exist_ok=False)
    cache = directory/'normalized-complete-geometry-and-amplitude-rows.f64'
    matrix = np.memmap(cache, dtype=np.float64, mode='w+', shape=(count, coordinate_size))
    bounds = np.empty(count)
    bounds[:old_count] = old_bounds

    def discard_pages():
        if hasattr(matrix._mmap, 'madvise') and hasattr(mmap, 'MADV_DONTNEED'):
            matrix._mmap.madvise(mmap.MADV_DONTNEED)

    def discard_prefix_pages():
        if (isinstance(old_rows, np.memmap) and hasattr(old_rows._mmap, 'madvise')
                and hasattr(mmap, 'MADV_DONTNEED')):
            old_rows._mmap.madvise(mmap.MADV_DONTNEED)

    for first in range(0, coordinate_size, block_columns):
        last = min(coordinate_size, first+block_columns)
        matrix[:old_count, first:last] = old_rows[:, first:last]
        matrix.flush()
        discard_pages()
        discard_prefix_pages()
    new_metadata = []
    for offset, item in enumerate(selected):
        row_index = old_count+offset
        if item['kind'] in ('cap_diameter', 'height_floor'):
            value, gradient, details = _scalar_covector(problem, p, item['kind'], budgets)
        else:
            value, gradient, details = _point_covector(problem, p, point_module,
                observed_module, item['location'], item['kind'], item['sign'], budgets)
        row = np.asarray(transpose(gradient))
        if row.shape != (coordinate_size,) or np.iscomplexobj(row) or not np.isfinite(row).all():
            raise ValueError('The unchanged complete T* returned an invalid amplitude covector')
        norm = float(np.linalg.norm(row))
        if not math.isfinite(norm) or (norm == 0 and np.any(row != 0)):
            raise ValueError('A numerical row norm failed; no mathematical infeasibility follows')
        # An exactly zero derivative is retained as 0*z <= -g.  It is not
        # silently removed, regularized, or declared globally infeasible.
        scale = norm if norm > 0 else 1.0
        matrix[row_index] = row/scale
        bounds[row_index] = -value/scale
        if not math.isfinite(float(bounds[row_index])):
            raise ValueError('A normalized bound overflowed; no mathematical infeasibility follows')
        record = dict(index=row_index, constraint_kind=item['kind'],
            current_inequality_value=value, actual_inequality_margin=-value,
            current_product=value, actual_product_margin=-value,
            product_alias_scope='Compatibility alias for g<=0; this value is NOT a reach product',
            normalized_bound=float(bounds[row_index]),
            gradient_coordinate_norm=norm, row_normalization_scale=scale,
            protected_inequality=item['protected'],
            point_location=item.get('location'),
            zero_original_coordinate_derivative=bool(norm == 0),
            row_formula='C=T*grad(g)/scale; b=-g/scale; original C*z<=b',
            **details)
        # Witness details already contain sign: avoid duplicate keyword arguments.
        record['sign'] = item.get('sign')
        new_metadata.append(record)
        del gradient, row
        if (offset+1) % 8 == 0:
            matrix.flush()
            discard_pages()
    matrix.flush()
    discard_pages()
    metadata = dict(old_metadata)
    metadata.update(schema=SCHEMA, selected_rows=count,
        eligible_rows=int(old_metadata.get('eligible_rows', old_count))+len(selected),
        protected_inequalities=int(old_metadata.get('protected_inequalities', 0))
            +sum(int(item['protected']) for item in selected),
        rows=list(old_metadata.get('rows', ()))+new_metadata,
        row_cache=str(cache), row_cache_bytes=int(matrix.size*8),
        block_columns=int(block_columns), all_original_field_variables_retained=True,
        homogeneous_equalities_imposed=False)
    metadata['amplitude'] = dict(schema=SCHEMA,
        source=dict(path=str(Path(__file__).resolve()), sha256=_sha(__file__)),
        point_source=point_identity, budgets=budgets.metadata(),
        original_prefix_rows=old_count, appended_rows=len(selected),
        requested_point_rows_with_explicit_signs=requested,
        unique_point_rows=len(selected)-2,
        eligible_input_scope='Only the caller-selected point rows are enumerated here; the caller retains its full scan counts',
        current_witness_radius=float(current_witness_radius(problem, p)),
        permanent_nonlinear_locations_owned_by_caller=True,
        every_nonlinear_point_requires_both_witness_signs=True,
        orbit_multiplicity_does_not_relax_any_inequality=True,
        original_free_core_prefix=[0, int(problem.M-problem.K)],
        original_height_entry=int(problem.free_size-1),
        moving_witness_derivative_added_before_Tstar=True,
        fixed_mother_norm_and_complete_original_Tstar=True,
        scope='Selected finite first-order step inequalities only; true all-point screening and same-field continuous proofs remain required')
    return matrix, bounds, metadata


def directional_checks(problem, x, point_module, observed_module, transpose,
                       lift, coordinate_size, *, budgets, location,
                       seed=2026112603, tolerance=2e-9):
    """New-row checks on ONE actual candidate/location, only in Actions.

    The dedicated free-core direction recomputes p_current from the COMPLEX
    trial core; freezing p in the check would miss precisely the new branch.
    The squared distances use bilinear sum(z*z), never conjugation or norms.
    A second arbitrary actual coordinate direction checks the complete T*.
    The H-only row formulas are checked with a dedicated H direction.
    This is a diagnostic, never a continuous geometric certificate.
    """
    _require_actions()
    point_identity = validate_point_source(point_module)
    _validate_budget_problem(problem, budgets)
    p = problem.prepare(x)
    free_core_count = _layout(problem, p, x)
    if free_core_count < 1:
        raise ValueError('The dedicated new p_current check requires an actual free-core entry')
    loc, _ = _location(problem, location)
    records = []
    epsilon = 1e-30
    gradients = {}
    for kind, sign in (('body_diameter', None), ('witness_distance', 1), ('witness_distance', -1)):
        value, gradient, details = _point_covector(problem, p, point_module,
            observed_module, loc, kind, sign, budgets)
        gradients[(kind, sign)] = gradient
    core_direction = np.zeros(problem.free_size)
    core_direction[:free_core_count] = 1/math.sqrt(free_core_count)
    rng = np.random.default_rng(seed)
    z = rng.standard_normal(coordinate_size)
    z /= np.linalg.norm(z)
    coordinate_direction = np.asarray(lift(z))
    if coordinate_direction.shape != (problem.free_size,):
        raise ValueError('Diagnostic lift must be the actual unchanged complete original map')
    for name, direction in (('all_free_core_witness_branch', core_direction),
                            ('complete_coordinate_map', coordinate_direction)):
        trial = problem.prepare(np.asarray(x)+1j*epsilon*direction)
        F = _fields(problem, trial, point_module, observed_module, loc)['F']
        r0 = current_witness_radius(problem, trial)
        values = _point_values(F, loc['phi'], r0, budgets)
        for kind, sign, key in (('body_diameter', None, 'body_diameter'),
                                ('witness_distance', 1, 'witness_plus'),
                                ('witness_distance', -1, 'witness_minus')):
            gradient = gradients[(kind, sign)]
            predicted = (float(z@transpose(gradient)) if name == 'complete_coordinate_map'
                         else float(gradient@direction))
            actual = float(np.imag(values[key])/epsilon)
            relative = abs(actual-predicted)/max(1.0, abs(actual), abs(predicted))
            records.append(dict(direction=name, constraint_kind=kind, sign=sign,
                predicted=predicted, complex_step=actual, scaled_difference=relative,
                complex_trial_witness_recomputed=True))
    for kind in ('cap_diameter', 'height_floor'):
        _, gradient, _ = _scalar_covector(problem, p, kind, budgets)
        actual = float(np.imag(_scalar_values(p.height+1j*epsilon, budgets)[kind])/epsilon)
        predicted = float(gradient[-1])
        relative = abs(actual-predicted)/max(1.0, abs(actual), abs(predicted))
        records.append(dict(direction='original_H_only', constraint_kind=kind,
            predicted=predicted, complex_step=actual, scaled_difference=relative))
    differences = [record['scaled_difference'] for record in records]
    maximum = max(differences)
    if not all(math.isfinite(value) for value in differences) or maximum > tolerance:
        raise ValueError('The new complete amplitude rows failed their actual-field directional check: '
                         +repr(records))
    return dict(schema=SCHEMA, point_source=point_identity, location=loc,
        seed=seed, epsilon=epsilon, tolerance=tolerance,
        maximum_scaled_difference=maximum, records=records,
        scope='New amplitude rows and moving-witness free-core derivative on the ACTUAL candidate only; no continuous metric, diameter, held-distance, embedding, or reach certificate')
