"""Bound R139 coast reference values and actual first jets, point cached.

The inlet, scalar coast, material chart and all coefficients stay frozen.
The cache stores physical s/u jets at a specific (s, full material-u column).
Computational x/xi jets are formed from the caller's current U_s/U_xi on
every call. No field of an unknown raw solution is divided here.

Saved entries are floating evaluations of the explicit R139 functions, not
new polynomial field definitions or interval certificates. In a nonzero
physical-bump metric this object is a reference function, not an exact GC
solution for that changed metric.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import numpy as np
from fd2d_k0_native_gc import SavedNativeCoast
from fd2d_gc_archive_arrays import identity, load_npz, save_npz

HERE = Path(__file__).resolve().parent
NOTES = HERE.parent/'notes'
SCHEMA = 'fd2d-frozen-R139-coast-physical-jet-cache-v1'
INVERSE_TOLERANCE = 2e-13
PROOF = NOTES/'2026-11-12-fd2d-k0-ruling-angular-certificate-01.json'


def _sha(value):
    return hashlib.sha256(value).hexdigest()


def _canonical_u(value):
    """Canonical round-tripping longdouble text avoids padding-byte keys."""
    u = np.asarray(value, dtype=np.longdouble)
    if u.ndim != 1 or not len(u) or not np.all(np.isfinite(u)):
        raise ValueError('A cache point needs one finite nonempty material-u column')
    text = np.array([np.format_float_scientific(q, unique=True, trim='k') for q in u])
    digest = _sha(('\n'.join(text.tolist())+'\n').encode('ascii'))
    return u, text, digest


def _array_digest(value):
    a = np.ascontiguousarray(value, dtype=np.float64)
    return _sha(a.tobytes())


class FrozenCoastReference:
    def __init__(self, inlet_path, cache_path=None):
        self.inlet_path = Path(inlet_path)
        self._coast = SavedNativeCoast(self.inlet_path)
        self.geometry = self._coast.geometry
        self.entry_s = float(self._coast.entry_s)
        self.length = float(self._coast.length)
        self.exit_s = self.entry_s+self.length
        self.candidate_sha256 = self._coast.candidate_sha256
        self.a_c, self.v = float(self._coast.a), float(self._coast.v)
        self._cache = {}
        self.hits = self.misses = 0
        self.loaded_cache = None
        inlet = identity(self.inlet_path)
        proof = json.loads(PROOF.read_text())
        if (not proof.get('passed') or proof.get('unresolved')
                or proof['inlet_sha256'] != inlet['sha256']
                or proof['candidate_sha256'] != self.candidate_sha256
                or proof['moments_sha256'] != identity(self.geometry.moments_path)['sha256']):
            raise ValueError('The frozen reference must bind the already proved R139 positive inlet/ruling domain')
        self._inputs = dict(inlet=inlet, positivity_packet=identity(PROOF),
            moments=identity(self.geometry.moments_path), means=identity(self.geometry.means_path))
        names = ('fd2d_gc_frozen_coast_reference.py', 'fd2d_k0_native_gc.py',
                 'fd2d_k0_ruling_coast.py', 'fd2d_balanced_curvature_core.py',
                 'fd2d_metric_curvature_core.py', 'fd2d_gc_archive_arrays.py')
        self._sources = {name: identity(HERE/name) for name in names}
        self._binding = dict(schema=SCHEMA, candidate_sha256=self.candidate_sha256,
            inputs={k: row['sha256'] for k, row in self._inputs.items()},
            sources={k: row['sha256'] for k, row in self._sources.items()},
            entry_s_hex=self.entry_s.hex(), length_hex=self.length.hex(),
            a_c_hex=self.a_c.hex(), v_hex=self.v.hex(), inverse_tolerance=INVERSE_TOLERANCE,
            numpy_version=np.__version__, longdouble_itemsize=np.dtype(np.longdouble).itemsize,
            longdouble_mantissa_bits=int(np.finfo(np.longdouble).nmant),
            stored_jets_dtype='binary64', stored_component_order=['n', 'm', 'l'])
        self.binding_sha256 = _sha(json.dumps(self._binding, sort_keys=True, separators=(',', ':')).encode())
        # The defining arrays are frozen; geometry/inverse caches may change
        # operationally without changing the functions they evaluate.
        for array in (self._coast.n, self._coast.m, self._coast.f):
            array.flags.writeable = False
        if cache_path is not None:
            self.load_cache(cache_path)

    def __copy__(self):
        return self

    def __deepcopy__(self, memo):
        memo[id(self)] = self
        return self

    def _physical_point(self, s, u_column):
        s = float(s)
        if not np.isfinite(s) or not self.entry_s <= s <= self.exit_s:
            raise ValueError('An active reference query is outside the frozen coast')
        u, u_text, u_sha = _canonical_u(u_column)
        key = (s.hex(), u_sha)
        if key in self._cache:
            row = self._cache[key]
            # Hash agreement is never used instead of checking the actual
            # coordinate column. U_s/U_xi are deliberately not cached here.
            if row['s'] != s or row['u'].shape != u.shape or not np.array_equal(row['u'], u):
                raise ValueError('A cache key does not match the actual requested material-u column')
            self.hits += 1
            return row
        # Exact stored endpoint labels avoid subtraction rounding outside
        # SavedNativeCoast's closed sigma interval.
        sigma = 0. if s == self.entry_s else self.length if s == self.exit_s else s-self.entry_s
        q = self._coast.evaluate(sigma, u, tolerance=INVERSE_TOLERANCE)
        n, m, ns, ms = (np.asarray(q[k], np.longdouble) for k in ('n', 'm', 'n_s', 'm_s'))
        if np.any(n <= 0) or np.any(np.asarray(q['D']) <= 0):
            raise FloatingPointError('Positive frozen-reference domain failed in numerical evaluation')
        # l=m^2/n belongs to the already positive, immutable reference.
        # n here is never an independent unknown raw field.
        ls = (2*m*ms*n-m*m*ns)/(n*n)
        values = np.asarray(np.stack((n, m, q['l']), axis=-1), dtype=np.float64)
        ds = np.asarray(np.stack((ns, ms, ls), axis=-1), dtype=np.float64)
        du = np.asarray(np.stack((q['n_u'], q['m_u'], q['l_u']), axis=-1), dtype=np.float64)
        if not all(np.all(np.isfinite(a)) for a in (values, ds, du)):
            raise FloatingPointError('Nonfinite numerical frozen coast jets')
        metrics = dict(sigma=float(sigma), material_inverse_residual=float(np.max(abs(q['material_u']-u))),
            inverse_iterations=int(q['inverse_iterations']), sampled_n_minimum=float(np.min(n)),
            sampled_D_minimum=float(np.min(q['D'])),
            evaluated_gauss_residual=float(np.max(abs(q['gauss_residual']))),
            evaluated_codazzi_residual=float(max(np.max(abs(q['codazzi_m'])),np.max(abs(q['codazzi_n'])))))
        row = dict(s=s, u=u.copy(), u_text=u_text, u_sha256=u_sha,
                   values=values, physical_s=ds, physical_u=du, diagnostics=metrics)
        for name in ('u', 'u_text', 'values', 'physical_s', 'physical_u'):
            row[name].flags.writeable = False
        self._cache[key] = row
        self.misses += 1
        return row

    def jet_on_grid(self, x, coords, active_mask=None):
        """Return values/x/xi with shape (work, len(x), 3), order n,m,l.

        x is physical s. coords must contain full columns u,u_s,u_xi.
        The default mask queries the closed reference coast and zeros the
        other slots. A supplied mask is one boolean per radial point; every
        active point must lie on the coast. Inactive slots are allocation
        placeholders, not an asserted extension of the reference function.
        The caller owns the support weight and its derivatives.
        """
        x = np.asarray(x, dtype=float)
        if x.ndim != 1 or not np.all(np.isfinite(x)):
            raise ValueError('Reference radial coordinates must be a finite one-dimensional array')
        u = np.asarray(coords['u'])
        us, uxi = (np.asarray(coords[k], dtype=float) for k in ('u_s', 'u_xi'))
        if (u.ndim != 2 or u.shape[1] != len(x) or us.shape != u.shape or uxi.shape != u.shape
                or not all(np.all(np.isfinite(a)) for a in (u, us, uxi))):
            raise ValueError('Expected finite actual u,u_s,u_xi arrays of shape (work,N)')
        if active_mask is None:
            active = (x >= self.entry_s)&(x <= self.exit_s)
        else:
            active = np.asarray(active_mask)
            if active.dtype != bool or active.shape != x.shape:
                raise ValueError('active_mask must contain one boolean per radial point')
            if np.any(active&((x < self.entry_s)|(x > self.exit_s))):
                raise ValueError('The active support extends outside this frozen reference coast')
        values = np.zeros(u.shape+(3,), dtype=float)
        dx = np.zeros_like(values); dxi = np.zeros_like(values)
        for j in np.flatnonzero(active):
            point = self._physical_point(x[j], u[:, j])
            values[:, j] = point['values']
            dx[:, j] = point['physical_s']+us[:, j, None]*point['physical_u']
            dxi[:, j] = uxi[:, j, None]*point['physical_u']
        return dict(values=values, x=dx, xi=dxi)

    def cache_statistics(self):
        return dict(entries=len(self._cache), hits=self.hits, misses=self.misses,
            loaded_cache=self.loaded_cache,
            maximum_material_inverse_residual=max((q['diagnostics']['material_inverse_residual'] for q in self._cache.values()), default=0.),
            maximum_numerical_native_GC_residual=max((max(q['diagnostics']['evaluated_gauss_residual'],q['diagnostics']['evaluated_codazzi_residual']) for q in self._cache.values()), default=0.))

    def definition(self):
        return dict(schema='fd2d-frozen-R139-coast-reference-v1', binding_sha256=self.binding_sha256,
            inputs=self._inputs, sources=self._sources, candidate_sha256=self.candidate_sha256,
            entry_s=self.entry_s, length=self.length, physical_coast=[self.entry_s, self.exit_s],
            a_c=self.a_c, v=self.v, scalar_constants='SavedNativeCoast stored numeric representatives, bound by the R139 positivity packet',
            native_formula='R139 at sigma=s-entry_s and the actual fixed material u',
            component_order=['n', 'm', 'l'],
            physical_l_s='(2*m*m_s*n-m*m*n_s)/(n*n), on the positive frozen reference',
            computational_x='physical_s + U_s*physical_u', computational_xi='U_xi*physical_u',
            frozen_parameter_derivatives_zero=True, unknown_raw_n_is_never_divided=True,
            reference_parameters_updated_by_current_delta=False,
            exact_GC_metric_scope='Only the frozen K=0 coast with a(s)=a_c+v*(s-entry_s); changed physical-bump g uses this as reference only',
            inverse_tolerance=INVERSE_TOLERANCE, cached_jets_dtype='binary64',
            cache_key='s.hex plus canonical full actual u column; actual column equality checked on every hit',
            chart_derivatives_reapplied_on_every_call=True,
            complete_position_monodromy_inferred=False, continuous_numeric_certificate=False,
            cache_statistics=self.cache_statistics())

    def save_cache(self, path):
        """Write an immutable small cache; return its actual NPZ(.gz) identity."""
        arrays = {}
        entries = []
        for index, key in enumerate(sorted(self._cache)):
            row = self._cache[key]
            stem = str(index).zfill(5)
            arrays['u_'+stem] = row['u_text']
            for name in ('values', 'physical_s', 'physical_u'):
                arrays[name+'_'+stem] = row[name]
            entries.append(dict(stem=stem, s_hex=row['s'].hex(), u_sha256=row['u_sha256'],
                work=len(row['u']), diagnostics=row['diagnostics'],
                array_sha256={name: _array_digest(row[name]) for name in ('values', 'physical_s', 'physical_u')}))
        metadata = dict(schema=SCHEMA, binding=self._binding, binding_sha256=self.binding_sha256,
            entries=entries, definition=self.definition(), mathematical_function_is_not_defined_by_cache=True)
        arrays['metadata'] = np.array(json.dumps(metadata, sort_keys=True, allow_nan=False))
        return save_npz(path, **arrays)

    def load_cache(self, path):
        """Load only entries bound to this identical input/source/precision set."""
        data = load_npz(path)
        meta = json.loads(str(data['metadata']))
        if (meta.get('schema') != SCHEMA or meta.get('binding_sha256') != self.binding_sha256
                or meta.get('binding') != self._binding):
            raise ValueError('Cache belongs to a different frozen inlet, candidate, source, or numeric precision')
        for spec in meta['entries']:
            stem = spec['stem']; s = float.fromhex(spec['s_hex'])
            if not self.entry_s <= s <= self.exit_s:
                raise ValueError('Saved cache radial point is outside its frozen reference domain')
            u, text, digest = _canonical_u(np.asarray(data['u_'+stem], dtype=np.longdouble))
            if digest != spec['u_sha256'] or len(u) != spec['work']:
                raise ValueError('Saved actual material-u column changed')
            row = dict(s=s, u=u.copy(), u_text=text, u_sha256=digest, diagnostics=spec['diagnostics'])
            for name in ('values', 'physical_s', 'physical_u'):
                value = np.asarray(data[name+'_'+stem], dtype=float)
                if (value.shape != (len(u), 3) or not np.all(np.isfinite(value))
                        or _array_digest(value) != spec['array_sha256'][name]):
                    raise ValueError('Saved physical reference jet changed: '+name)
                row[name] = value.copy()
            for name in ('u', 'u_text', 'values', 'physical_s', 'physical_u'):
                row[name].flags.writeable = False
            key = (s.hex(), digest)
            if key in self._cache:
                old = self._cache[key]
                if not np.array_equal(old['u'], row['u']) or any(not np.array_equal(old[k], row[k]) for k in ('values', 'physical_s', 'physical_u')):
                    raise ValueError('Conflicting entries for the same actual frozen-reference query')
            self._cache[key] = row
        self.loaded_cache = identity(path)
        return self.cache_statistics()
