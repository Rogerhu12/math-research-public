"""Bounded, view-aware reuse of four frozen angular operator projections.

The mathematical operator is the existing RawBumpDAE operator. Only its
four chart/basis-only matrix products are shared across delta values and
copy.copy radial views. The original per-view, four-entry delta operator
packet cache remains local and unchanged in scope. No new shared cache
contains a physical-profile scalar, field, forcing, parameter derivative,
or residual. The profile is still evaluated by its original provider.

Installing a thin dynamic subclass keeps method self bound to each copy.
The original explicit R155 coast-background view is also wrapped after
its original constructor formula, without altering its field definition.
No source module or process-global base class is monkey-patched.
"""
from __future__ import annotations
from collections import OrderedDict
import hashlib
import json
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity
from fd2d_gc_raw_bump_dae import RawBumpDAE

HERE = Path(__file__).resolve().parent
SCHEMA = 'fd2d-frozen-angular-operator-projection-cache-v1'
_BASIS = ('PE', 'PO', 'Ex', 'Ox')
_COLUMNS = ('u', 'u_s', 'u_xi', 'advection')
_CLASSES = {}


def _canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


class FrozenOperatorProjectionCache:
    """One frozen mathematical chart/basis binding and a byte-bounded LRU.

    The reported limit counts exact basis/key bytes plus ndarray payload,
    not the Python interpreter's object overhead or old local delta cache.
    A separate entry count is bounded as well.
    """
    def __init__(self, problem, *, byte_limit=32*1024*1024, maximum_entries=1024):
        if int(byte_limit) != byte_limit or byte_limit <= 0:
            raise ValueError('A positive integer cache payload limit is required')
        if int(maximum_entries) != maximum_entries or maximum_entries < 1:
            raise ValueError('A positive integer entry limit is required')
        if problem.profile_kind != 'physical_bumps':
            raise ValueError('This cache factors only the original physical-bump operator')
        self.byte_limit = int(byte_limit)
        self.maximum_entries = int(maximum_entries)
        self.chart = problem.chart
        self.chart_definition = _canonical(problem.angular_atlas_definition)
        self.layout = tuple(int(getattr(problem, key)) for key in ('K', 'e', 'd', 'q', 'work'))
        self.basis = {}
        for name in _BASIS:
            array = np.asarray(getattr(problem, name))
            if array.dtype != np.float64 or not np.all(np.isfinite(array)):
                raise ValueError('The actual frozen projection bases must be finite binary64')
            self.basis[name] = (array.shape, array.dtype.str, np.ascontiguousarray(array).tobytes())
        self.theta = np.ascontiguousarray(np.asarray(problem.chart.theta, float)).tobytes()
        self.fixed_bytes = len(self.theta)+sum(len(row[2]) for row in self.basis.values())
        if self.fixed_bytes > self.byte_limit:
            raise ValueError('The byte limit is smaller than the exact frozen basis binding')
        self.binding = dict(schema=SCHEMA, chart=json.loads(self.chart_definition),
            layout=dict(zip(('K','e','d','q','work'), self.layout)),
            bases={name:dict(shape=list(row[0]), dtype=row[1], sha256=hashlib.sha256(row[2]).hexdigest())
                   for name,row in self.basis.items()},
            theta_sha256=hashlib.sha256(self.theta).hexdigest(),
            original_operator_source=identity(HERE/'fd2d_gc_raw_bump_dae.py'),
            adapter_source=identity(__file__),
            formulas=['PE@(adv*Ex)', 'PE@((1/U_xi)*Ox)',
                      'PO@(adv*Ox)', 'PO@((1/U_xi)*Ex)'])
        self.binding_sha256 = hashlib.sha256(_canonical(self.binding).encode()).hexdigest()
        self.entries = OrderedDict()
        self.entry_bytes = 0
        self.hits = self.misses = self.evictions = self.uncached_oversize = 0
        self.operator_calls = self.local_packet_hits = self.background_view_wraps = 0

    def __copy__(self):
        return self

    def __deepcopy__(self, memo):
        memo[id(self)] = self
        return self

    def view_keys(self, problem):
        """Validate frozen definitions and retain exact actual coordinate bytes."""
        if problem.chart is not self.chart or _canonical(problem.angular_atlas_definition) != self.chart_definition:
            raise ValueError('A different mathematical chart cannot share this cache')
        if tuple(int(getattr(problem, key)) for key in ('K','e','d','q','work')) != self.layout:
            raise ValueError('A different actual Fourier layout cannot share this cache')
        if np.ascontiguousarray(np.asarray(problem.chart.theta, float)).tobytes() != self.theta:
            raise ValueError('The frozen computational-angle array changed')
        for name, (shape, dtype, data) in self.basis.items():
            array = np.asarray(getattr(problem, name))
            if array.shape != shape or array.dtype.str != dtype or np.ascontiguousarray(array).tobytes() != data:
                raise ValueError('The actual frozen basis changed: '+name)
        x = np.asarray(problem.x)
        if x.dtype != np.float64 or x.shape != (problem.N,) or not np.all(np.isfinite(x)):
            raise ValueError('A radial view must carry its actual finite binary64 coordinates')
        arrays = {}
        for name in _COLUMNS:
            array = np.asarray(problem.coords[name])
            if (array.dtype != np.float64 or array.shape != (problem.work, problem.N)
                    or not np.all(np.isfinite(array))):
                raise ValueError('Invalid actual angular-coordinate column: '+name)
            arrays[name] = array
        if np.any(arrays['u_xi'] <= 0):
            raise ValueError('The declared angular chart must remain positive')
        return tuple((np.float64(x[j]).tobytes(),)+tuple(
            np.ascontiguousarray(arrays[name][:,j]).tobytes() for name in _COLUMNS)
            for j in range(problem.N))

    def point(self, problem, j, key):
        if key in self.entries:
            value, amount = self.entries.pop(key)
            self.entries[key] = (value, amount)
            self.hits += 1
            return value
        self.misses += 1
        adv = np.asarray(problem.coords['advection'][:,j], float)
        inverse_angle = 1/np.asarray(problem.coords['u_xi'][:,j], float)
        blocks = (
            problem.PE@(adv[:,None]*problem.Ex),
            problem.PE@(inverse_angle[:,None]*problem.Ox),
            problem.PO@(adv[:,None]*problem.Ox),
            problem.PO@(inverse_angle[:,None]*problem.Ex))
        for block in blocks:
            if not np.all(np.isfinite(block)):
                raise FloatingPointError('Nonfinite frozen projection')
            block.flags.writeable = False
        amount = sum(len(part) for part in key)+sum(v.nbytes for v in blocks)
        if self.fixed_bytes+amount > self.byte_limit:
            self.uncached_oversize += 1
            return blocks
        while self.entries and (self.fixed_bytes+self.entry_bytes+amount > self.byte_limit
                                or len(self.entries) >= self.maximum_entries):
            unused, (_, old_amount) = self.entries.popitem(last=False)
            self.entry_bytes -= old_amount
            self.evictions += 1
        self.entries[key] = (blocks, amount)
        self.entry_bytes += amount
        return blocks

    def statistics(self):
        return dict(schema=SCHEMA, binding_sha256=self.binding_sha256,
            entries=len(self.entries), maximum_entries=self.maximum_entries,
            fixed_basis_key_bytes=self.fixed_bytes, entry_payload_bytes=self.entry_bytes,
            total_counted_bytes=self.fixed_bytes+self.entry_bytes, byte_limit=self.byte_limit,
            payload_limit_excludes_Python_object_overhead=True,
            hits=self.hits, misses=self.misses, evictions=self.evictions,
            uncached_oversize=self.uncached_oversize, operator_calls=self.operator_calls,
            original_local_delta_packet_hits=self.local_packet_hits,
            explicit_background_view_wraps=self.background_view_wraps,
            shared_delta_dependent_values_cached=False,
            original_per_view_delta_cache_retained=True,
            no_global_base_class_patch=True)


def frozen_projection_operators(problem, delta):
    """Original exact operator, with the two 1/a scalars moved outside projections."""
    cache = problem._frozen_operator_projection_cache
    cache.operator_calls += 1
    delta = np.asarray(delta, float)
    if delta.shape != (problem.J,):
        raise ValueError('Expected the explicit physical profile vector')
    if not np.array_equal(problem.profile.coefficients, delta):
        problem.profile.set_parameters(delta)
    point_keys = cache.view_keys(problem)
    # Original local packets still use delta.tobytes(). A copied or edited
    # view must not retain a packet for other actual coordinates.
    if getattr(problem, '_frozen_operator_packet_context', None) != point_keys:
        problem._operator_cache = {}
        problem._frozen_operator_packet_context = point_keys
    key = delta.tobytes()
    if key in problem._operator_cache:
        cache.local_packet_hits += 1
        return problem._operator_cache[key]
    jet = problem.profile.jet(problem.x)
    a, c = jet['a'], jet['c']
    inv = 1/(problem.coords['u_xi']*a)
    adv = problem.coords['advection']
    op = np.zeros((problem.N, problem.d, problem.q))
    Ie, Io = np.eye(problem.e), np.eye(problem.K)
    for j, point_key in enumerate(point_keys):
        A, B, C, D = cache.point(problem, j, point_key)
        op[j,:problem.e,:problem.e] = A-c[j]*Ie
        op[j,:problem.e,problem.e:problem.d] = B/a[j]
        op[j,:problem.e,problem.d:] = c[j]*Ie
        op[j,problem.e:,problem.e:problem.d] = C-2*c[j]*Io
        op[j,problem.e:,problem.d:] = D/a[j]
    result = dict(jet=jet, op=op, inv=inv, adv=adv)
    if len(problem._operator_cache) >= 4:
        problem._operator_cache.pop(next(iter(problem._operator_cache)))
    problem._operator_cache[key] = result
    return result


def frozen_projection_operator_direction(problem, delta, direction):
    """Small analytic parameter JVP of this operator alone, not a whole J."""
    ops = frozen_projection_operators(problem, delta)
    direction = np.asarray(direction, float)
    if direction.shape != (problem.J,) or not np.all(np.isfinite(direction)):
        raise ValueError('Expected one finite physical-profile direction')
    jet = ops['jet']; a = jet['a']
    da, dc = jet['a_parameters']@direction, jet['c_parameters']@direction
    out = np.zeros_like(ops['op'])
    Ie, Io = np.eye(problem.e), np.eye(problem.K)
    cache = problem._frozen_operator_projection_cache
    for j, key in enumerate(cache.view_keys(problem)):
        unusedA, B, unusedC, D = cache.point(problem, j, key)
        scale = -da[j]/(a[j]*a[j])
        out[j,:problem.e,:problem.e] = -dc[j]*Ie
        out[j,:problem.e,problem.e:problem.d] = scale*B
        out[j,:problem.e,problem.d:] = dc[j]*Ie
        out[j,problem.e:,problem.e:problem.d] = -2*dc[j]*Io
        out[j,problem.e:,problem.d:] = scale*D
    return dict(op=out, inv=-da[None,:]/(problem.coords['u_xi']*a[None,:]**2),
                a=da, c=dc)


class _FrozenProjectionOperatorsMixin:
    def operators(self, delta):
        return frozen_projection_operators(self, delta)

    def coast_background_view(self):
        # Use the original R155 formula, including its chosen base class.
        # Then install only this arithmetic method on that new view.
        view = super().coast_background_view()
        _attach(view, self._frozen_operator_projection_cache)
        self._frozen_operator_projection_cache.background_view_wraps += 1
        return view

    def affine_view(self):
        view = super().affine_view()
        return _attach(view, self._frozen_operator_projection_cache)


def _attach(problem, cache):
    if not isinstance(problem, _FrozenProjectionOperatorsMixin):
        base = type(problem)
        if base.operators is not RawBumpDAE.operators:
            raise ValueError('Do not replace an unrecognized operator implementation')
        if base not in _CLASSES:
            _CLASSES[base] = type('FrozenAngularProjection_'+base.__name__,
                (_FrozenProjectionOperatorsMixin, base), {'__module__': __name__})
        problem.__class__ = _CLASSES[base]
    old = getattr(problem, '_frozen_operator_projection_cache', None)
    if old is not None and old is not cache:
        raise ValueError('An installed object already belongs to another frozen cache')
    problem._frozen_operator_projection_cache = cache
    return problem


def install_frozen_operator_projection_cache(problem, *, byte_limit=32*1024*1024,
                                             maximum_entries=1024):
    """Install only on a new/idle problem, before its first derived views.

    copy.copy radial/quadrature/affine views inherit the class method and
    shared cache. Explicit R155 base-class views are wrapped by the mixin.
    Existing derived-view caches are dropped, never the defining fields.
    """
    if isinstance(problem, _FrozenProjectionOperatorsMixin):
        return problem._frozen_operator_projection_cache
    cache = FrozenOperatorProjectionCache(problem, byte_limit=byte_limit,
                                          maximum_entries=maximum_entries)
    _attach(problem, cache)
    problem._operator_cache = {}
    for name in ('_cell_gauss_view_cache', '_chunked_gauss_codazzi_views',
                 '_interior_constraint_point_cache', '_positive_known_coast_view'):
        if hasattr(problem, name):
            delattr(problem, name)
    return cache
