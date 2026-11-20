#!/usr/bin/env python3
"""R53 bridge for an actual old core with explicit material jet providers.

No support-Fourier interpretation of a generic core's coefficient labels is made.
This source was saved while execution was unavailable and has NOT been tested.
The original core must have the same unit-speed, rotation and reflection gauges
as R53. Its rho_lower/rho_upper must bound its true material curvature radius.

make_factory(reference, settings, parameter_jets_provider=..., ...)
returns Core(q, corrections, base_mode). At homotopy=0 the exact original
instance is returned. Use factory.parameter_jets for both endpoints.
"""
import importlib.util
from pathlib import Path
import numpy as np

# Load a separate module object and inject only per-instance callbacks.
# No running module's globals or the old reference class are modified.
_spec = importlib.util.spec_from_file_location(
    "_held10_material_flattening_provider_base",
    Path(__file__).with_name("material_flattened_support_core.py"))
_base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_base)


def _three_jets(value, names):
    if isinstance(value, dict):
        return tuple(np.asarray(value[key], float) for key in names)
    if len(value) != 3:
        raise ValueError("Provider must return exactly three material jets")
    return tuple(np.asarray(item, float) for item in value)


def make_factory(reference, settings=None, *, parameter_jets_provider,
                 rho_material_jets_provider=None,
                 curvature_derivative_bounds_provider=None):
    """Bind a genuine old core factory and its true material derivative providers.

    parameter_jets_provider(core, theta) returns (dF/dp, dFt/dp, dFtt/dp),
    each of shape (parameter_count, len(theta), 3), in actual q/c units;
    a dict with keys d0, d1, d2 is also accepted.

    rho_material_jets_provider(core, theta) returns (rho, rho_u, rho_uu),
    each of shape (len(theta),), or a dict with those three keys. If omitted,
    core.rho_material_jets(theta) is used.

    curvature_derivative_bounds_provider(core), if supplied, returns global
    upper bounds (K1, K2) for |kappa_u| and |kappa_uu| in material coordinates.
    Without it, the exact coarse R53 positivity criterion must pass; otherwise
    this adapter rejects the state. It never substitutes support-label bounds.
    """
    if not callable(parameter_jets_provider):
        raise TypeError("An explicit true parameter-jets provider is required")
    options = dict(settings or {})
    homotopy = float(options.pop("homotopy", 0.))
    if not (0. <= homotopy <= 1.):
        raise ValueError("homotopy must lie in [0,1]")
    original_arc_nodes = options.pop("original_arc_nodes", None)

    def original_jets(core, theta):
        theta = np.asarray(theta, float).reshape(-1)
        jets = _three_jets(parameter_jets_provider(core, theta), ("d0", "d1", "d2"))
        if any(jet.ndim != 3 or jet.shape[1:] != (len(theta), 3) for jet in jets):
            raise ValueError("True parameter jets must have shape (p,N,3)")
        if any(jet.shape != jets[0].shape for jet in jets):
            raise ValueError("True parameter-jet dimensions disagree")
        if any(not np.all(np.isfinite(jet)) for jet in jets):
            raise FloatingPointError("Nonfinite original parameter jet")
        return jets

    def fields(core, theta):
        theta = np.asarray(theta, float).reshape(-1)
        g = core.evaluate(theta)
        T = np.asarray(g["Ft"], float)
        Ftt = np.asarray(g["Ftt"], float)
        if T.shape != (len(theta), 3) or Ftt.shape != T.shape:
            raise ValueError("Original geometry must have planar material shape (N,3)")
        if np.max(np.abs(T[:, 2])) > 1.e-8 or np.max(np.abs(Ftt[:, 2])) > 1.e-8:
            raise FloatingPointError("Original provider is not planar in the expected gauge")
        if np.max(np.abs(np.sum(T*T, axis=1)-1.)) > 1.e-8:
            raise FloatingPointError("Original provider is not unit material speed")
        nu = np.column_stack((T[:, 1], -T[:, 0], np.zeros(len(theta))))
        if "phi" in g:
            phi = np.asarray(g["phi"], float).reshape(-1)
        else:
            raw = np.arctan2(nu[:, 1], nu[:, 0])
            # n>=3 and the R53 monotone sector gauge imply |phi-u|<pi.
            phi = raw+2.*np.pi*np.rint((theta-raw)/(2.*np.pi))
        kappa = -np.einsum("ni,ni->n", Ftt, nu)
        d0, d1, d2 = original_jets(core, theta)
        phi_p = -np.einsum("pni,ni->pn", d1, nu)
        kappa_p = -np.einsum("pni,ni->pn", d2, nu)
        if rho_material_jets_provider is None:
            if not hasattr(core, "rho_material_jets"):
                raise TypeError("True material rho jets are required")
            rho_value = core.rho_material_jets(theta)
        else:
            rho_value = rho_material_jets_provider(core, theta)
        rho, rho_u, rho_uu = _three_jets(rho_value, ("rho", "rho_u", "rho_uu"))
        rho, rho_u, rho_uu = (v.reshape(-1) for v in (rho, rho_u, rho_uu))
        if any(v.shape != theta.shape for v in (rho, rho_u, rho_uu)):
            raise ValueError("True rho material jets must have shape (N,)")
        if (not np.all(np.isfinite(rho+rho_u+rho_uu)) or np.min(rho) <= 0. or
                np.min(kappa) <= 0.):
            raise FloatingPointError("Original material curvature is not positive")
        if np.max(np.abs(kappa-1./rho)) > 1.e-7*(1.+np.max(kappa)):
            raise FloatingPointError("Geometry and rho providers describe different cores")
        return dict(phi=phi, kappa=kappa, phi_p=phi_p, kappa_p=kappa_p,
                    kappa_u=-rho_u/rho**2,
                    kappa_uu=2.*rho_u**2/rho**3-rho_uu/rho**2,
                    original_geometry=g)

    def factory(q, corrections=(), base_mode=3):
        corrections = tuple(float(c) for c in corrections)
        original_options = dict(base_mode=base_mode)
        if original_arc_nodes is not None:
            original_options["arc_nodes"] = int(original_arc_nodes)
        original = reference(q, corrections, **original_options)
        if homotopy == 0.:
            return original
        return _base.MaterialFlattenedSupportCore(
            original, homotopy=homotopy,
            _fields_provider=fields,
            _curvature_derivative_bounds_provider=curvature_derivative_bounds_provider,
            _parameter_count=1+len(corrections),
            _parameter_values=np.r_[float(q), np.asarray(corrections, float)],
            **options)

    def parameter_jets(core, theta):
        if isinstance(core, _base.MaterialFlattenedSupportCore):
            return core.jet_parameter_derivatives(theta)
        return original_jets(core, theta)

    factory.parameter_jets = parameter_jets
    factory.flattening_settings = dict(settings or {})
    return factory
