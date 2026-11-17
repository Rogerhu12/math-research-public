#!/usr/bin/env python3
"""Read an accepted m3 integral-core state and retain its reference lift once.

This reader never solves a BVP.  The exported representative is a finite
shared-two-jet Cartesian part plus one separable integral-core reference
term.  An additional, explicitly subtracted center correction imposes the
true integral core's entire two-jet.  Numerical evaluation of that integral
core is not an interval certificate, nor are its nominal coefficients used
as Fourier coefficients.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'

import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
from types import SimpleNamespace

import numpy as np
from scipy.interpolate import PPoly

HERE = Path(__file__).resolve().parent
CLOSED = HERE.parent / 'finite_closure/m3_m8_closed_map'
ROUND = HERE.parent / 'resume_m3/round_core_lib'
sys.path.insert(0, str(CLOSED))
from m3_shared_prefix import M3SharedPrefix, M3CartesianPrefix, circle
from shared_jet import SharedJetQuintic, build_mean

PAIRS = ((0, 0), (1, 0), (2, 0), (0, 1), (0, 2), (1, 1))
_loaded = False


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def _same_recorded_sources(record, paths):
    """A changed source requires a new explicit interface review, not fallback."""
    recorded = record['core_round_sources']
    for path in paths:
        path = Path(path).resolve()
        candidates = [value for key, value in recorded.items()
                      if Path(key).name == path.name]
        if not candidates or len(set(candidates)) != 1:
            raise ValueError('Missing or ambiguous checkpoint source: ' + str(path))
        if sha(path) != candidates[0]:
            raise ValueError('Checkpoint source changed: ' + str(path))


def round_core_type(library=ROUND):
    """Use the exact owned core implementation, with every control retained."""
    library = Path(library).resolve()
    for name in (path.stem for path in library.glob('*.py')):
        previous = sys.modules.get(name)
        if previous is not None and Path(previous.__file__).resolve().parent != library:
            raise RuntimeError('A different core library is already imported: ' + name)
    sys.path.insert(0, str(library))
    from plateau_core import PlateauSupportCore
    from fixed_large_radius_core import make_core_class
    from tight_moment_interval_bounds import install
    install()
    GeneralCore = make_core_class(PlateauSupportCore)

    class Core(GeneralCore):
        def summary(self):
            value = super().summary()
            value.update(control_family='C4 complementary controls, all support harmonics free',
                         first_free_support_frequency=2*self.base_mode,
                         primary_support_moment_locked=True)
            return value
    return Core


def load_integral_prefix(source_topic, short_bridge, checkpoint, port_path,
                         angular=512, library=ROUND):
    """Reconstruct source evaluation only; reject unaccepted or changed inputs.

    The physical profile and parameter scales are read literally from the
    accepted record.  Using a fixed BVP object here only holds those inputs
    during evaluation; no fixed-g convergence result is thereby asserted.
    """
    global _loaded
    if _loaded:
        raise RuntimeError('Use a fresh process for each source checkpoint')
    source, library = Path(source_topic).resolve(), Path(library).resolve()
    short_bridge, checkpoint = Path(short_bridge).resolve(), Path(checkpoint).resolve()
    record = json.load(gzip.open(checkpoint, 'rt'))
    sys.path.insert(0, str(HERE.parent / 'resume_m3'))
    from couple_m3_smallcut_secant import accepted_anchor
    accepted_anchor(record, checkpoint)
    if record['config']['base_mode'] != 3:
        raise ValueError('An accepted m3 state is required')
    if (record['config'].get('core_kind') != 'exact_m3_local_circle_integral_lift'
            or not record['config'].get('exact_core_lift')):
        raise ValueError('The checkpoint does not contain the actual integral lift')
    settings = dict(record['core_round_settings'])
    if not 0 <= settings['homotopy'] <= 1:
        raise ValueError('Invalid recorded homotopy')
    if bool(record['config'].get('exact_circle_core')) != (settings['homotopy'] == 1):
        raise ValueError('The exact-circle label disagrees with the recorded core')
    required = [source/'scripts/950f-prefix-adaptive-chart-bvp-v2.py',
                source/'scripts/db6f-prefix-flat-profile.py', short_bridge,
                *sorted(library.glob('*.py'))]
    _same_recorded_sources(record, required)
    Core = round_core_type(library)
    adaptive = module('closed_m3_integral_adaptive', required[0])
    module('closed_m3_integral_flat', required[1]).install(adaptive)
    adaptive.old.install_source(source/'repro/source-root')
    module('closed_m3_integral_short', short_bridge).install()
    core_module = __import__('fixed_metric_mode3_core')
    core_module.PlanarSupportCore = lambda q, corrections=(), base_mode=3: Core(
        q, corrections, base_mode, arc_nodes=1024, **settings)
    Flow, BaseBVP = adaptive.build_classes(record['chart'])
    unlifted_geo = Flow.geo
    from exact_core_lift import install_core_lift
    BVP = install_core_lift(Flow, BaseBVP, window=(.5, .9))
    port = json.loads(Path(port_path).read_text())
    if ('_prefix_bridge' in port['cut'] and
            port['cut']['_prefix_bridge'] != record['frozen_profile']['prefix_bridge']):
        raise ValueError('The supplied port changes the prefix bridge')
    port['cut']['_prefix_bridge'] = record['frozen_profile']['prefix_bridge']
    if (port['parameters'] != record['physical_tail_parameters']
            or port['cut'] != record['physical_tail_cut']):
        raise ValueError('The reader port changes the physical metric')
    obj = BVP(record['frozen_profile'], port, record['gauge_amplitude'],
              record['config']['modes'], angular, True, record['warp_reference_q'])
    obj.pscale = np.asarray(record['central_correction_scales'], float).copy()
    par = np.asarray(record['parameters'], float).copy()
    if len(obj.pscale) != obj.M-1 or len(par) != obj.M:
        raise ValueError('Recorded control dimensions are inconsistent')
    par[0] = math.log(record['actual_primary_amplitude']/obj.q)
    obj.initial(par)
    flow = obj.flow(par[0])
    obj.integral_unlifted_geo = unlifted_geo
    actual_controls = np.asarray(record['parameters'][1:])*obj.pscale
    if not np.array_equal(np.asarray(obj._core.corrections), actual_controls):
        raise ValueError('The reader changed a physical complementary control')
    if flow.exact_lift_core is not obj._core:
        raise ValueError('The actual reference lift is absent')
    # Actual accepted checkpoints may keep the regenerable coefficients in
    # hashed external chunks.  Use their original decoder after the source
    # modules are installed, instead of treating the metadata JSON as a field.
    from curve_stable_prefix_bvp import load_checkpoint
    decoded = load_checkpoint(checkpoint)
    raw = PPoly.construct_fast(np.asarray(decoded['pp_coefficients']),
                               np.asarray(decoded['mesh']), extrapolate=False, axis=1)
    rep = SharedJetQuintic.from_ppoly(raw)
    if rep.x[0] != 0 or rep.x[-1] != flow.end:
        raise ValueError('The accepted mesh and frozen physical domain differ')
    sol = SimpleNamespace(x=rep.x, y=rep(rep.x), p=par, sol=rep)
    sol.mean_spline = build_mean(flow, sol, angular, 8)
    used = {str(path): sha(path) for path in [
        *required, Path(__file__).resolve(), CLOSED/'m3_shared_prefix.py',
        CLOSED/'shared_jet.py',
        HERE.parent/'resume_m3/couple_m3_smallcut_secant.py']}
    for imported in tuple(sys.modules.values()):
        path = getattr(imported, '__file__', None)
        if path is None:
            continue
        path = Path(path).resolve()
        if path.is_file() and (source in path.parents or library in path.parents):
            used[str(path)] = sha(path)
    obj.integral_reader_provenance = dict(
        checkpoint_sha256=sha(checkpoint), port_sha256=sha(port_path),
        core_round_settings=settings, physical_controls=actual_controls.tolist(),
        reference_lift_window=[.5, .9], source_sha256=used,
        actual_tail_acceptance_reused=True, bvp_solves=0)
    _loaded = True
    return record, obj, flow, sol, raw


class M3IntegralCartesianPrefix(M3CartesianPrefix):
    """The actual integral reference term occurs exactly once in this map.

    X = Cartesian shared quintics + shared(a chi) H + center repair + cut repair.
    H is the same unprojected angular function as the actual solver.  The
    scalar a chi is replaced by shared endpoint jets, so regularity is literal
    Hermite algebra even when the source profile is evaluated numerically.
    """
    def __init__(self, obj, flow, sol, center_width=.04, side_modes=32):
        if not hasattr(flow, 'exact_lift_core') or flow.exact_lift_core is not obj._core:
            raise ValueError('Expected the actual installed integral lift')
        self.lift_span = (.9-.5)*flow.prefix_end
        # Keep the solver's multiplication order.  The right shared knot is
        # one upward ulp beyond its computed cutoff, where clip is exactly 1.
        # This avoids interpreting two differently rounded products as one
        # literal endpoint; the source-vs-shared radial change is audited.
        self.lift_window = (.5*flow.prefix_end,
                            np.nextafter(.5*flow.prefix_end+self.lift_span, np.inf))
        if not 0 < self.lift_window[0] < self.lift_window[1] < flow.end:
            raise ValueError('The source lift window is invalid')
        nodes = np.unique(np.r_[sol.x, self.lift_window])
        expanded = SimpleNamespace(x=nodes, y=sol.sol(nodes), p=sol.p,
                                   sol=sol.sol, mean_spline=sol.mean_spline)
        old = M3SharedPrefix(obj, flow, expanded, center_width)
        super().__init__(old, side_modes)
        self.reference_initial = np.asarray(flow.exact_lift_initial, float).copy()
        self.reference_inlet_e = float(flow.warp_e)
        self._H_argument = self._H_value = None
        self.lift_rep = SharedJetQuintic(
            self.rep.x, self.source_lift_radial_jets(self.rep.x)[:, None, :])
        if np.any(self.lift_rep.jets[:, 0, self.rep.x >= self.lift_window[1]] != 0):
            raise ValueError('The source lift does not vanish with its two-jet')

    def source_lift_radial_jets(self, s):
        s = np.atleast_1d(np.asarray(s, float))
        lo, hi = self.lift_window
        span = self.lift_span
        t = np.clip((s-lo)/span, 0, 1)
        chi = 1-t**3*(10-15*t+6*t*t)
        chip = -30*t*t*(1-t)**2/span
        chipp = -60*t*(1-t)*(1-2*t)/span**2
        a, ap, app = self.flow.profile(s)
        result = np.stack((a*chi, ap*chi+a*chip,
                           app*chi+2*ap*chip+a*chipp))
        return result

    def reference_angular_jets(self, psi):
        psi = np.atleast_1d(np.asarray(psi, float))
        if self._H_argument is not None and np.array_equal(psi, self._H_argument):
            return self._H_value
        e = self.reference_inlet_e
        theta = psi-e*np.sin(3*psi)/3
        rho, rhop = 1-e*np.cos(3*psi), 3*e*np.sin(3*psi)
        target = self.core.evaluate(theta)
        er, et = circle(theta), circle(theta, 1)
        background = (er, rho[:, None]*et,
                      rhop[:, None]*et-rho[:, None]**2*er)
        core = (target['F'], rho[:, None]*target['Ft'],
                rho[:, None]**2*target['Ftt']+rhop[:, None]*target['Ft'])
        value = tuple(core[j]-background[j]-self.q*self.coefficient_value(
            self.reference_initial, psi, j) for j in range(3))
        self._H_argument, self._H_value = psi.copy(), value
        return value

    def reference_correction(self, s, psi, source_radial=False):
        s = np.atleast_1d(np.asarray(s, float))
        radial = (self.source_lift_radial_jets(s) if source_radial else
                  np.stack([self.lift_rep(s, j)[0] for j in range(3)]))
        angular = self.reference_angular_jets(psi)
        return [radial[i, :, None, None]*angular[j][None, :, :]
                for i, j in PAIRS]

    def raw_evaluate(self, s, psi):
        """The uncorrected finite representative, with one reference lift."""
        s = np.atleast_1d(np.asarray(s, float))
        coefficients = [self.rep(s, j) for j in range(3)]
        correction = self.reference_correction(s, psi)
        return [self.tensor_values(coefficients[i], psi, j)+term
                for (i, j), term in zip(PAIRS, correction)]

    def center_delta(self, psi):
        psi = np.atleast_1d(np.asarray(psi, float))
        theta = psi-self.E0*np.sin(3*psi)/3
        rho, rhop = 1-self.E0*np.cos(3*psi), 3*self.E0*np.sin(3*psi)
        b, bp, bpp = (-self.Epp*np.sin(3*psi)/3,
                      -self.Epp*np.cos(3*psi), 3*self.Epp*np.sin(3*psi))
        cg = self.core.rho_material_jets(theta)
        gt, gtt, rc = cg['Ft'], cg['Ftt'], cg['rho']
        gttt = (-gt/rc[:, None]**2
                +cg['normal']*cg['rho_phi'][:, None]/rc[:, None]**3)
        coefficients = self.rep.jets[:, :, 0]
        radial = self.lift_rep.jets[:, 0, 0]
        H = self.reference_angular_jets(psi)
        result = []
        for j in range(3):
            before = self.tensor_values(coefficients.T, psi, j)
            before += radial[:, None, None]*H[j][None, :, :]
            target = np.zeros_like(before)
            if j == 0:
                target[0] = cg['F']
                target[1, :, 2] = 1
                target[2] = b[:, None]*gt
            elif j == 1:
                target[0] = rho[:, None]*gt
                target[2] = bp[:, None]*gt+(b*rho)[:, None]*gtt
            else:
                target[0] = rho[:, None]**2*gtt+rhop[:, None]*gt
                target[2] = (bpp[:, None]*gt+(2*bp*rho+b*rhop)[:, None]*gtt
                             +(b*rho*rho)[:, None]*gttt)
            result.append(target-before)
        return result

    def evaluate(self, s, psi):
        s = np.atleast_1d(np.asarray(s, float))
        jets = self.raw_evaluate(s, psi)
        if np.any(s <= self.center_width):
            delta = self.center_delta(psi)
            weights = [self.center_weights(s, j) for j in range(3)]
            for X, (i, j) in zip(jets, PAIRS):
                X += np.einsum('sj,juk->suk', weights[i], delta[j])
        if self.end_lift is not None:
            for X, term in zip(jets, self.end_lift.correction(s, psi)):
                X += term
        return jets

    def definition_record(self):
        return dict(
            formula='Cartesian shared quintics + shared(a chi) H + center repair + cut repair',
            reference_lift_multiplicity=1,
            H='Integral Core(theta0) - circle(theta0) - q*initial Fourier projection',
            theta0_e=self.reference_inlet_e,
            center_theta_e=self.E0,
            radial_lift_window=list(self.lift_window),
            source_lift_span=self.lift_span,
            radial_lift_knots=len(self.lift_rep.x),
            center_angular_third_jet='-T/rho^2 + normal*rho_phi/rho^3',
            nominal_core_coefficients_interpreted_as_fourier=False,
            mathematical_core='Exact integral/moment-defined core with recorded parameters; numerical evaluation errors remain separate',
            core_integrals_and_inverse='Source numerical evaluator; rigorous error remains to be bounded',
            exact_c2_reason='Shared radial two-jets, actual smooth angular core, and whole-function endpoint Hermite identities',
            source_numerical_checks_are_continuous_certificates=False)
