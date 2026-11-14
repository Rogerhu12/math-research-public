"""Actual R153 Gauss-l window jets on a saved R149 affine background.

The angular jets use K only. The separately exposed radial and mixed jets
consume the real one-sided K_s of the explicit physical profile, only where
the fixed window is active. No global C3 assumption or unknown n division
outside the declared positive domain is introduced.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import load_npz
from fd2d_gc_raw_native_field import identity, locate_bound
from fd2d_gc_bump_coast_native_field import decoded_definition, window
from fd2d_gc_ruling_atlas_native_field import RulingAtlasRawBumpNativeField
from fd2d_frozen_ellipse_candidate import phase
from fd2d_balanced_curvature_core import FixedBalancedGeometry

HERE = Path(__file__).resolve().parent
SCHEMA = 'fd2d-actual-positive-Gauss-l-ruling-atlas-native-v1'


def physical_profile_third(profile, physical_s, *, side='right'):
    """The actual explicit profile's one-sided a''' on requested pieces.

    This numerical jet is queried only on the active Gauss-l support. It
    neither modifies the profile nor assumes traces of a''' match globally.
    """
    if side not in ('left', 'right'):
        raise ValueError('Select a real radial side for the profile third jet')
    s = np.atleast_1d(np.asarray(physical_s, float))
    if not np.all(np.isfinite(s)) or np.any(s < 0) or np.any(s > profile.end):
        raise ValueError('Profile third jet requested outside the physical domain')
    base = profile.base
    ids = np.clip(np.searchsorted(base.breaks, s, side=side)-1, 0, len(base.segments)-1)
    out = np.empty_like(s)
    for index in np.unique(ids):
        mask = ids == index; piece = base.segments[int(index)]
        L = float(piece['L']); t = np.clip((s[mask]-piece['s0'])/L, 0., 1.)
        kind = piece['kind']
        if kind == 'hermite':
            coefficients = np.asarray(piece['coefficients'], float)
            out[mask] = np.polynomial.polynomial.polyval(t,
                np.polynomial.polynomial.polyder(coefficients, 3))/L**3
            continue
        phi, ps = phase(piece, t)
        difference = float(piece['p1']-piece['p0'])
        if kind == 'turn':
            z = np.clip(np.minimum(t, 1-t)/.08, 0., 1.)
            zt = np.where(t < .08, 1/.08, np.where(t > .92, -1/.08, 0.))
            pss = difference*(6*z-6*z*z)*zt/(.92*L*L)
        elif kind == 'brake':
            pss = np.full_like(t, 2*difference/(L*L))
        elif kind == 'phase_bridge':
            q0, q1 = L*piece['ps0'], L*piece['ps1']
            c2, c3 = 3*difference-2*q0-q1, -2*difference+q0+q1
            pss = (2*c2+6*t*c3)/(L*L)
        elif kind in ('coast', 'coast_to'):
            pss = np.zeros_like(t)
        else:
            raise ValueError('Unsupported actual phase piece: '+str(kind))
        out[mask] = np.cos(phi)*pss-np.sin(phi)*ps*ps
    out += profile.basis(s, 3)@np.asarray(profile.coefficients, float)
    if not np.all(np.isfinite(out)):
        raise FloatingPointError('Nonfinite actual profile third jet')
    return out


def gauss_l_native_jets(raw, weight, weight_s, K_s=None, *, minimum_active_n,
                        include_radial=True):
    """Apply the exact quotient/product rules to five actual native jets.

    K_s is consumed only on w>0, where x is physical s. The native x jet
    already includes all U_s material-angle drift in n_x and m_x.
    """
    out = dict(raw)
    n, m, old = (np.asarray(raw[key], float) for key in ('n', 'm', 'l'))
    if include_radial and K_s is None:
        raise ValueError('The requested radial jets need the actual K_s')
    w, ws, unused = np.broadcast_arrays(np.asarray(weight, float), np.asarray(weight_s, float), n)
    ks = None if not include_radial else np.broadcast_to(np.asarray(K_s, float), n.shape)
    if not np.isfinite(minimum_active_n) or minimum_active_n < 0:
        raise ValueError('The explicit positive-n search margin must be finite and nonnegative')
    if not np.all(np.isfinite(w)) or np.any(w < 0) or np.any(w > 1):
        raise ValueError('The actual fixed window must lie in [0,1]')
    active = w > 0
    if np.any((w == 0)&(ws != 0)):
        raise ValueError('The declared quintic zero window must also have zero first jet')
    if np.any(n[active] <= minimum_active_n):
        raise FloatingPointError('Actual field is outside its declared active positive-n domain')
    derivatives = ('', '_xi', '_xixi') if not include_radial else ('', '_x', '_xi', '_xixi', '_x_xi')
    if not include_radial:
        # A partial angular query must not carry stale raw l radial jets.
        out.pop('l_x', None); out.pop('l_x_xi', None)
    for suffix in derivatives:
        out['l'+suffix] = np.array(raw['l'+suffix], copy=True)
    if not np.any(active):
        return out
    ni, mi = n[active], m[active]
    K = -np.asarray(raw['a_ss'], float)/np.asarray(raw['a'], float)
    nu, mu = (np.asarray(raw[key], float)[active] for key in ('n_xi', 'm_xi'))
    nuu, muu = (np.asarray(raw[key], float)[active] for key in ('n_xixi', 'm_xixi'))
    H = (K[active]+mi*mi)/ni
    Hu = (2*mi*mu-H*nu)/ni
    Huu = (2*(mu*mu+mi*muu)-H*nuu-2*Hu*nu)/ni
    wi, wsi = w[active], ws[active]
    Hjets = {'': H, '_xi': Hu, '_xixi': Huu}
    if include_radial:
        nx, mx = (np.asarray(raw[key], float)[active] for key in ('n_x', 'm_x'))
        nxu, mxu = (np.asarray(raw[key], float)[active] for key in ('n_x_xi', 'm_x_xi'))
        Hx = (ks[active]+2*mi*mx-H*nx)/ni
        Hxu = (2*(mx*mu+mi*mxu)-Hx*nu-Hu*nx-H*nxu)/ni
        Hjets.update(_x=Hx, _x_xi=Hxu)
    for suffix in derivatives:
        before = np.asarray(raw['l'+suffix], float)[active]
        value = (1-wi)*before+wi*Hjets[suffix]
        if suffix == '_x':
            value += wsi*(H-old[active])
        elif suffix == '_x_xi':
            value += wsi*(Hu-np.asarray(raw['l_xi'], float)[active])
        out['l'+suffix][active] = value
        if not np.all(np.isfinite(out['l'+suffix])):
            raise FloatingPointError('Nonfinite actual Gauss-l jet '+suffix)
    return out


class PositiveGaussLNativeField(RulingAtlasRawBumpNativeField):
    """The explicitly saved nonlinear field, with original raw n and m."""
    def __init__(self, arrays, candidate, *, gauss_l_definition=None, **kwargs):
        saved = load_npz(arrays)
        declared = saved.get('gauss_l_definition')
        if declared is None and gauss_l_definition is None:
            raise ValueError('The actual nonlinear field must explicitly declare gauss_l_definition')
        meta = decoded_definition(declared if gauss_l_definition is None else gauss_l_definition)
        if declared is not None and decoded_definition(declared) != meta:
            raise ValueError('Caller Gauss-l definition differs from the actual saved field')
        super().__init__(arrays, candidate, **kwargs)
        if self.representation_kind != 'global_ruling_atlas_positive_n_local_Gauss_l_v1':
            raise ValueError('The saved representation is not this explicit nonlinear field')
        if meta.get('schema') != 'fd2d-positive-n-local-Gauss-l-field-v1':
            raise ValueError('Unsupported explicit nonlinear Gauss-l field schema')
        sources = dict(provider_source_sha256='fd2d_gc_raw_bump_positive_gauss.py',
                       algebra_source_sha256='fd2d_gc_positive_gauss_l.py')
        for key, name in sources.items():
            if meta.get(key) != identity(HERE/name)['sha256']:
                raise ValueError('Actual Gauss-l source binding differs: '+key)
        ref = self.coast_reference
        rim = ref.length*self.reference_rim_fraction
        expected = dict(support=[ref.entry_s, ref.exit_s],
            rim_fraction=self.reference_rim_fraction,
            weight='same S5 coast-window function as the declared frozen reference',
            l='(1-w)*l_raw+w*(K+m^2)/n; evaluate quotient only where w>0',
            n_and_m='unchanged complete affine P1 correction plus exact declared lifting',
            true_gauss_identity='G_actual=(1-w)*G_raw',
            gauss_plateau=[ref.entry_s+rim, ref.exit_s-rim],
            known_lifting_unchanged=True, physical_metric_changed_by_representation=False)
        for key, value in expected.items():
            if meta.get(key) != value:
                raise ValueError('Changed or unsupported actual Gauss-l definition: '+key)
        margin = float(meta['selected_finite_evaluation_floor'])
        if not np.isfinite(margin) or margin <= 0:
            raise ValueError('Bind the actual positive finite search margin explicitly')
        plateau = expected['gauss_plateau']
        inactive = [j for j in range(1, len(self.nodes)-1)
            if self.nodes[j-1] >= plateau[0] and self.nodes[j+1] <= plateau[1]]
        if meta.get('inactive_l_raw_nodes') != inactive:
            raise ValueError('Declared inactive P1 hats differ from the actual defining mesh')
        if 'inactive_l_raw_nodes' in saved and not np.array_equal(saved['inactive_l_raw_nodes'], inactive):
            raise ValueError('Saved inactive l index array differs from its full definition')
        self.gauss_l_definition = meta
        self.minimum_active_n = margin
        self._minimum_sampled_active_n = None
        self._maximum_consumed_abs_K_s = 0.

    def evaluate_raw_native(self, x, xi, *, side='right'):
        """Explicit affine background, useful for comparisons only."""
        return RulingAtlasRawBumpNativeField.evaluate_native(self, x, xi, side=side)

    def evaluate_angular_native(self, x, xi, *, side='right'):
        """Values and first/second angular jets, with no profile third query.

        The omitted l_x/l_x_xi keys cannot be confused with unchanged raw
        derivatives. Angular chains to physical u need only these jets.
        """
        raw = self.evaluate_raw_native(x, xi, side=side)
        xx, unused = np.broadcast_arrays(np.asarray(x, float), np.asarray(xi, float))
        w, ws = window(xx, self.coast_reference.entry_s, self.coast_reference.length,
                       self.reference_rim_fraction)
        return gauss_l_native_jets(raw, w, ws, minimum_active_n=self.minimum_active_n,
                                   include_radial=False)

    def evaluate_native(self, x, xi, *, side='right'):
        raw = self.evaluate_raw_native(x, xi, side=side)
        xx, pp = np.broadcast_arrays(np.asarray(x, float), np.asarray(xi, float))
        shape = xx.shape
        w, ws = window(xx, self.coast_reference.entry_s, self.coast_reference.length,
                       self.reference_rim_fraction)
        active = w > 0
        ks = np.zeros(shape, float)
        if np.any(active):
            ss = xx[active]
            unique, inverse = np.unique(ss, return_inverse=True)
            third = physical_profile_third(self.profile, unique, side=side)[inverse]
            a, av, acc = (np.asarray(raw[key], float)[active] for key in ('a', 'a_s', 'a_ss'))
            ks[active] = -third/a+acc*av/(a*a)
            self._maximum_consumed_abs_K_s = max(self._maximum_consumed_abs_K_s,
                                                 float(np.max(abs(ks[active]))))
            minimum = float(np.min(np.asarray(raw['n'])[active]))
            self._minimum_sampled_active_n = (minimum if self._minimum_sampled_active_n is None
                else min(minimum, self._minimum_sampled_active_n))
        return gauss_l_native_jets(raw, w, ws, ks, minimum_active_n=self.minimum_active_n)

    @classmethod
    def from_definition(cls, path):
        path = Path(path); meta = json.loads(path.read_text())
        if meta['schema'] != SCHEMA:
            raise ValueError('Wrong explicit positive-Gauss-l native schema')
        for row in meta['sources']:
            locate_bound(path, row)
        geometry = FixedBalancedGeometry(moments=locate_bound(path, meta['moments']),
                                         means=locate_bound(path, meta['means']))
        cache = meta.get('reference_cache_input')
        return cls(locate_bound(path, meta['arrays']), locate_bound(path, meta['candidate_input']),
            reference_inlet=locate_bound(path, meta['reference_inlet_input']),
            reference_cache=None if cache is None else locate_bound(path, cache),
            angular_atlas_definition=meta['angular_atlas_definition'],
            coast_reference_definition=meta['coast_reference_definition'],
            gauss_l_definition=meta['gauss_l_definition'],
            seed_weight_definition=meta['seed_weight_definition'], representation_kind=meta['representation_kind'],
            blend_interval=meta['blend_interval'], profile_supports=meta['profile_supports'],
            fixed_base_T=meta['fixed_base_T'], base_kind=meta['base_kind'], tail_kind=meta['tail_kind'],
            candidate_sha256=meta['candidate_input']['sha256'], collar_guard=meta['collar_guard'], geometry=geometry)

    def definition(self):
        meta = super().definition()
        meta['schema'] = SCHEMA
        extra = ('fd2d_gc_positive_gauss_l_native_field.py', 'fd2d_gc_positive_gauss_l.py',
                 'fd2d_gc_raw_bump_positive_gauss.py', 'fd2d_frozen_ellipse_candidate.py')
        meta['sources'] = [identity(HERE/name) for name in extra]+meta['sources']
        meta['gauss_l_definition'] = self.gauss_l_definition
        meta['no_shape_denominator'] = False
        meta['actual_shape_denominator'] = 'n only where w>0, after the explicitly bound positive finite-domain check'
        meta['independent_l_saved'] = True
        meta['independent_l_is_actual_everywhere'] = False
        meta['actual_complete_field'] = ('Original complete R149 affine n,m and independent l_raw; '
            'actual l=(1-w)*l_raw+w*(K+m^2)/n only on the explicitly positive active window')
        meta['new_field_equal_to_affine_background'] = False
        meta['jet_requirements'] = dict(
            values_and_angular_first_second='Actual K and full native n/m angular jets; no K_s',
            radial_and_mixed='Actual one-sided K_s=-a_sss/a+a_ss*a_s/a^2 on w>0 only',
            base_a_sss='Actual Hermite polynomial third derivative, or cos(phase)*phase_ss-sin(phase)*phase_s^2',
            bump_a_sss='Sum of actual saved delta_j times compact basis third derivative',
            outside_window='Original affine jets copied; no division by n and no profile third derivative query',
            global_C3_requirement_added=False)
        meta['finite_evaluation_statistics'] = dict(
            minimum_sampled_active_n=self._minimum_sampled_active_n,
            maximum_consumed_abs_K_s=self._maximum_consumed_abs_K_s,
            continuous_positive_domain_proved=False, continuous_residual_certificate=False)
        meta['actual_body_consumer'] = ('Inherited fixed-material 24-component ODE dynamically calls these actual l, '
            'l_u,l_uu jets; no body integration is claimed by this definition')
        return meta
