#!/usr/bin/env python3
"""Complete fixed-g body extension: original independent159 plus nine columns.

Import-only mathematical adapter.  No CLI, solver, check suite, research
candidate, or automatic ledger is installed here.  The calling public task
owns all input restoration, ordinary values, derivatives, and output costs.

R490 defines four P5*sin(2*j*theta) u columns, four P8*sin(2*j*theta)
v columns, and the complete height primitive ell*P8.  Every original scalar,
reference coefficient, fixed metric, and old height primitive is retained.
"""
from __future__ import annotations

import copy
from fractions import Fraction
import hashlib
from pathlib import Path

import numpy as np

from frame_collar_bvp import periodic_operator, target_frame
from frame_direct_reference_geometry159 import DirectReferenceFiveHeightField
from frame_height_null_coordinates import digest


POLICY = "same-fixed-g-complete-body-extension168-v1"
INDEPENDENT_COUNT = 168
ORIGINAL_INDEPENDENT_COUNT = 159
PHYSICAL_COUNT = 172
EXTRA_COUNT = 9
LEFT_EXACT = "9/250"
RIGHT_EXACT = "423/500"
LENGTH_EXACT = "81/100"
LEFT = float(Fraction(LEFT_EXACT))
RIGHT = float(Fraction(RIGHT_EXACT))
LENGTH = float(Fraction(LENGTH_EXACT))
POSITION_KEYS = ("X", "Xs", "Xt", "Xss", "Xst", "Xtt", "T")
FRAME_KEYS = ("T", "Ts", "Tss", "Ttheta")
SCALAR_KINDS = ("value", "s", "ss", "theta")


def definition():
    return {
        "schema": POLICY,
        "original_independent_columns": 159,
        "original_physical_columns": 163,
        "new_independent_columns": 168,
        "new_physical_columns": 172,
        "added_column_count": 9,
        "state_order": [
            "original159", "alpha_sin2_sin4_sin6_sin8",
            "beta_sin2_sin4_sin6_sin8", "gamma_height"],
        "left": LEFT_EXACT,
        "right": RIGHT_EXACT,
        "length": LENGTH_EXACT,
        "xi": "(s-left)/length",
        "P_m": "xi^m*exp(-xi/(1-xi)) on 0<xi<1; zero elsewhere",
        "delta_u": "P5*sum_{j=1}^4 alpha_j*sin(2*j*theta)",
        "delta_v": "P8*sum_{j=1}^4 beta_j*sin(2*j*theta)",
        "delta_center": "length*gamma*P8",
        "delta_b": "gamma*dP8/dxi",
        "delta_b_s": "gamma*d2P8/dxi2/length",
        "delta_b_ss": "gamma*d3P8/dxi3/length^2",
        "regularity": {
            "P5_left_zero_extension": "C4",
            "P8_left_zero_extension": "C7",
            "delta_b_left_zero_extension": "C6",
            "right_zero_extension": "flat",
            "all_position_two_jets_match_at_both_true_interfaces": True},
        "all_old_columns_and_permanent_reference_retained": True,
        "fixed_metric_and_b0_unchanged": True,
        "new_family_not_the_original163_family": True,
        "zero_extra_physical_field_is_original159": True,
        "complete_body_not_a_leading_or_collar_only_substitution": True,
        "one_exact_zero_total_height_primitive": True,
        "ordinary_geometry_uses_original_complete_circle_periodic_operator": True,
        "old159_J_not_recomputed_by_this_module": True,
        "nonzero_extra_requires_current_geometry_and_current_derivatives": True,
        "source": "results/R490-fixed-metric-intrinsic-curvature-bound-and-a-nested-complete-body-extension.md",
    }


def implementation_hashes():
    paths = [Path(__file__)]
    for name in (
        "frame_direct_reference_geometry159.py", "frame_collar_bvp.py",
        "frame_entry_single_q.py", "frame_height_null_coordinates.py"):
        paths.append(Path(__file__).with_name(name))
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}


def _finite(value, shape, label):
    answer = np.asarray(value, dtype=float)
    if answer.shape != shape or not np.all(np.isfinite(answer)):
        raise ValueError("finite original-layout input required: " + label)
    return answer


def _same_bytes(left, right):
    a, b = np.asarray(left), np.asarray(right)
    return a.shape == b.shape and a.dtype == b.dtype and a.tobytes() == b.tobytes()


def array_binding(value):
    a = np.ascontiguousarray(value)
    return {
        "dtype": a.dtype.str,
        "shape": list(a.shape),
        "bytes": int(a.nbytes),
        "sha256": hashlib.sha256(a.tobytes()).hexdigest(),
    }


def _validate_grid(radial, theta):
    r, th = np.asarray(radial, dtype=float), np.asarray(theta, dtype=float)
    if (r.ndim != 1 or len(r) < 2 or r[0] != 0.
            or not np.all(np.isfinite(r)) or np.any(np.diff(r) <= 0)):
        raise ValueError("the zero-anchored strictly increasing original radial grid is required")
    if (th.ndim != 1 or len(th) < 4 or len(th) % 4
            or not np.all(np.isfinite(th))):
        raise ValueError("a finite complete angular grid of multiple-of-four size is required")
    expected = th[0] + np.arange(len(th))*2*np.pi/len(th)
    tolerance = 128*np.finfo(float).eps*max(1., float(np.max(abs(th))))
    if not np.allclose(th, expected, rtol=0., atol=tolerance):
        raise ValueError("the complete original uniform angular grid is required")
    # Keep the supplied association and bytes.  This does not replace a fine
    # grid by an algebraically equal expression with different rounding.
    return r, th


def _profile_xi_jets(radial, power):
    """P_m and xi derivatives 0..3, including the actual zero extensions."""
    r = np.asarray(radial, dtype=float)
    if r.ndim != 1 or not np.all(np.isfinite(r)) or power not in (5, 8):
        raise ValueError("finite radial vector and m in {5,8} required")
    out = [np.zeros_like(r) for _ in range(4)]
    active = (r > LEFT) & (r < RIGHT)
    if not np.any(active):
        return tuple(out)
    x = (r[active]-LEFT)/LENGTH
    # A final binary64 division can round an interior x to 1.  Its distance
    # from the endpoint is then far below the exponential underflow range;
    # these complete derivatives round to zero.  Do not form 0*infinity.
    inside = (x > 0.) & (x < 1.)
    if not np.any(inside):
        return tuple(out)
    indices = np.flatnonzero(active)[inside]
    x = x[inside]
    d = 1.-x
    chi = np.exp(-x/d)
    q = d**-2
    r3 = d**-3
    base = x**power
    first = power*x**(power-1)-q*base
    second = (power*(power-1)*x**(power-2)
              - 2*power*q*x**(power-1)+(q*q-2*r3)*base)
    third = (power*(power-1)*(power-2)*x**(power-3)
             - 3*power*(power-1)*q*x**(power-2)
             + 3*power*(q*q-2*r3)*x**(power-1)
             + (-d**-6+6*d**-5-6*d**-4)*base)
    for target, local in zip(out, (base, first, second, third)):
        target[indices] = chi*local
    if any(not np.all(np.isfinite(v)) for v in out):
        raise FloatingPointError("nonfinite complete body profile derivative")
    return tuple(out)


def radial_columns(radial):
    """Small radial arrays only; no field, geometry, or Jacobian is evaluated."""
    u = _profile_xi_jets(radial, 5)
    v = _profile_xi_jets(radial, 8)
    return {
        "u": tuple(u[k]/LENGTH**k for k in range(4)),
        "v": tuple(v[k]/LENGTH**k for k in range(4)),
        "height": {
            "center": LENGTH*v[0], "b": v[1],
            "b_s": v[2]/LENGTH, "b_ss": v[3]/LENGTH**2},
    }


def angular_columns(theta):
    th = np.asarray(theta, dtype=float)
    if th.ndim != 1 or not np.all(np.isfinite(th)):
        raise ValueError("finite original angular grid required")
    frequencies = np.arange(1, 5, dtype=float)*2.
    phase = th[:, None]*frequencies[None, :]
    return np.sin(phase), np.cos(phase)*frequencies[None, :]


class _Body168Grid:
    """Current scalar fields with the old scalar-grid cache shared verbatim."""
    def __init__(self, field, radial, theta):
        self.field = field
        self.radial = np.asarray(radial, dtype=float)
        self.theta = np.asarray(theta, dtype=float)
        self.original_grid = field.original_field._direct_single.source.grid_for(
            self.radial, self.theta)
        self.radial_body = radial_columns(self.radial)
        self.angular_body, self.angular_body_first = angular_columns(self.theta)

    def fields(self, state):
        q = self.field.validate_state(state)
        reference = self.field.original_field.coordinates.reference_evaluation_state(q[:159])
        original = self.original_grid.fields(reference)
        if not np.any(q[159:167] != 0.):
            return original
        out = dict(original)
        active = (self.radial > LEFT) & (self.radial < RIGHT)
        for name, coefficients in (("u", q[159:163]), ("v", q[163:167])):
            if not np.any(coefficients != 0.):
                continue
            angular = self.angular_body @ coefficients
            first = self.angular_body_first @ coefficients
            rr = self.radial_body[name]
            out[name] = dict(original[name])
            for kind, value in (
                ("value", rr[0][:, None]*angular[None, :]),
                ("s", rr[1][:, None]*angular[None, :]),
                ("ss", rr[2][:, None]*angular[None, :]),
                ("theta", rr[0][:, None]*first[None, :])):
                if kind not in original[name]:
                    raise ValueError("original scalar field is missing " + name + "/" + kind)
                changed = np.asarray(original[name][kind], dtype=float).copy()
                changed[active] += value[active]
                out[name][kind] = changed
        return out


class _Body168Source:
    """New source identity; never advertises the old163 layout for new input."""
    def __init__(self, field):
        self.field = field
        self.nunknown = INDEPENDENT_COUNT
        self.slices = dict(field.slices)
        self._grids = {}

    def grid_for(self, radial, theta):
        r, th = np.asarray(radial, dtype=float), np.asarray(theta, dtype=float)
        key = (r.tobytes(), th.tobytes())
        if key not in self._grids:
            self._grids[key] = _Body168Grid(self.field, r, th)
        return self._grids[key]

    def frame(self, state, grid):
        fields = grid.fields(state)
        fields["_theta"] = grid.theta[None, :]
        return target_frame(fields)

    def model_definition(self):
        return {
            "schema": POLICY+"-scalar-source",
            "old_source": self.field.original_field.source.model_definition(),
            "extension": definition(),
            "parameter_input": "168 independent coordinates, not original163",
        }


class CompleteBody168Field:
    """New family using one unchanged original DirectReferenceFiveHeightField.

    This class intentionally is not a FiveHeightField subclass: the old
    selected159 factory must not silently accept the new layout.  Only
    ordinary geometry and the separately provided new-nine derivatives are
    exposed here.  No old159 factorization is requested by this adapter.
    """
    def __init__(self, original_field):
        if not isinstance(original_field, DirectReferenceFiveHeightField):
            raise ValueError("one original DirectReferenceFiveHeightField is required")
        if original_field.nunknown != 159 or original_field.metric_free != 0:
            raise ValueError("the complete fixed-g original159 field is required")
        self.original_field = original_field
        self.original_problem = original_field.original_problem
        self.nunknown = INDEPENDENT_COUNT
        self.physical_parameter_count = PHYSICAL_COUNT
        self.metric_free = 0
        self.port = original_field.port
        self.seed = original_field.seed
        self.tail = original_field.tail
        self.slices = dict(original_field.slices)
        self.slices.update(body_u=slice(159, 163), body_v=slice(163, 167),
                           body_height=slice(167, 168))
        self.height_base_definition = copy.deepcopy(original_field.height_base_definition)
        self._old_coordinate_sha256 = original_field.coordinate_definition_sha256
        self._old_evaluation_sha256 = digest(original_field.evaluation_definition())
        self.coordinate_definition = {
            "schema": POLICY+"-coordinates",
            "old159_definition": copy.deepcopy(original_field.coordinate_definition),
            "new9_linear_identity": definition(),
            "physical_map": "old exact affine 159-to-163 map direct-sum identity9",
            "physical_count": PHYSICAL_COUNT,
            "independent_count": INDEPENDENT_COUNT,
        }
        self.coordinate_definition_sha256 = digest(self.coordinate_definition)
        self.definition_sha256 = digest(self.evaluation_definition())
        self.source = _Body168Source(self)

    def _assert_context(self):
        if (self.original_field.coordinate_definition_sha256 != self._old_coordinate_sha256
                or digest(self.original_field.evaluation_definition()) != self._old_evaluation_sha256):
            raise ValueError("the original reference, coordinate map, or evaluation identity changed")

    def validate_state(self, state):
        q = _finite(state, (INDEPENDENT_COUNT,), "body168-state")
        self.original_field.coordinates.validate(q[:159])
        return q

    def embed_state(self, original159):
        q = self.original_field.coordinates.validate(original159)
        return np.concatenate((q, np.zeros(EXTRA_COUNT)))

    def initial_state(self):
        return self.embed_state(self.original_field.initial_state())

    def evaluation_definition(self):
        return {
            "schema": POLICY+"-ordinary-evaluation",
            "original_evaluation_definition": self.original_field.evaluation_definition(),
            "coordinate_definition_sha256": self.coordinate_definition_sha256,
            "extension": definition(),
            "old_reference_primitive_cache_owners_are_shared": True,
            "zero_extra_supplied_ordinary_returns_original_object": True,
            "new_ordinary_all_six_position_jets": True,
            "generic_old159_parameter_Jacobian_request_rejected": True,
        }

    def identity(self, state):
        q = self.validate_state(state)
        return {
            "schema": POLICY+"-physical",
            "original_physical163": self.original_field.identity(q[:159]),
            "new9_coefficients_exact": [str(Fraction.from_float(float(v))) for v in q[159:]],
            "new9_definition": definition(),
            "physical_count": PHYSICAL_COUNT,
            "independent_count": INDEPENDENT_COUNT,
        }

    def full_coefficients(self, state, *, exact=True):
        """Original163 exact physical coefficients followed by the new9.

        exact=True is the canonical tuple for physical172 box decisions.
        exact=False is a rounded diagnostic/evaluation array only; it never
        replaces the old exact null-height map or evaluates the field.
        """
        q = self.validate_state(state)
        values = (
            tuple(Fraction.from_float(float(v)) for v in q[:154])
            + tuple(self.original_field.coordinates.exact_heights(q[:159]))
            + tuple(Fraction.from_float(float(v)) for v in q[159:]))
        return values if exact else np.asarray([float(v) for v in values], dtype=float)

    def exact_original_box_decision(self, state, lower163, upper163):
        """Only the old163 coefficient box; the new9 box is a separate gate."""
        q = self.validate_state(state)
        return self.original_field.exact_original_box_decision(
            q[:159], lower163, upper163)

    def exact_full_box_decision(self, state, lower172, upper172):
        """Exact full172 coefficient box, including the actual new9 values."""
        lo = _finite(lower172, (PHYSICAL_COUNT,), "physical172-lower")
        hi = _finite(upper172, (PHYSICAL_COUNT,), "physical172-upper")
        if np.any(lo > hi):
            raise ValueError("ordered physical172 box required")
        values = self.full_coefficients(state, exact=True)
        lower = tuple(Fraction.from_float(float(v)) for v in lo)
        upper = tuple(Fraction.from_float(float(v)) for v in hi)
        bad = [j for j in range(PHYSICAL_COUNT)
               if values[j] < lower[j] or values[j] > upper[j]]
        return {
            "schema": POLICY+"-exact-physical172-box",
            "exact_full_box_pass": not bad,
            "physical_parameter_count": PHYSICAL_COUNT,
            "violating_indices": bad,
            "zero_extra_is_not_an_omission_of_the_new9_gate": True,
            "comparison_uses_exact_rational_physical_coefficients": True,
        }

    def state_record(self, state):
        q = self.validate_state(state)
        identity = self.identity(q)
        return {
            "schema": POLICY+"-state",
            "complete_physical_definition": identity,
            "physical_identity_sha256": digest(identity),
            "coordinate_definition_sha256": self.coordinate_definition_sha256,
            "independent168_exact": [str(Fraction.from_float(float(v))) for v in q],
            "original_physical163_exact": (
                [str(Fraction.from_float(float(v))) for v in q[:154]]
                + [str(v) for v in self.original_field.coordinates.exact_heights(q[:159])]),
            "new9_exact": [str(Fraction.from_float(float(v))) for v in q[159:]],
            "zero_extra": bool(not np.any(q[159:] != 0.)),
            "same_original_physical_at_zero_extra_only": True,
        }

    def metric_model(self, state):
        q = self.validate_state(state)
        return self.original_field.metric_model(q[:159])

    def metric(self, state, radial, jacobian=False):
        q = self.validate_state(state)
        return self.original_field.metric(q[:159], radial, jacobian=jacobian)

    def height_jets(self, state, radial):
        q = self.validate_state(state)
        raw = self.original_field.height_jets(q[:159], radial)
        if q[167] == 0.:
            return raw
        r = np.asarray(radial, dtype=float)
        hh = radial_columns(r)["height"]
        active = (r > LEFT) & (r < RIGHT)
        out = {key: np.asarray(value).copy() for key, value in raw.items()}
        for key in ("b", "b_s", "b_ss"):
            out[key][active] += q[167]*hh[key][active]
        return out

    def scalar_frame(self, state, radial, theta):
        self._assert_context()
        q = self.validate_state(state)
        grid = self.source.grid_for(radial, theta)
        fields = grid.fields(q)
        fields["_theta"] = np.asarray(theta, dtype=float)[None, :]
        return grid, fields, target_frame(fields)

    def bind_ordinary(self, state, radial, theta, data, source_receipt):
        """Bind existing complete ordinary arrays; no geometry is evaluated.

        The task must say whether these arrays were already paid or restored
        as a necessary new derivative input.  The receipt is not a cost waiver.
        Ordinary arrays are referenced, not copied, serialized, or recomputed.
        """
        self._assert_context()
        q = self.validate_state(state)
        r, th = _validate_grid(radial, theta)
        if not isinstance(data, dict) or not isinstance(source_receipt, dict):
            raise ValueError("ordinary data and its explicit source receipt are required")
        for key in POSITION_KEYS:
            _finite(data.get(key), (len(r), len(th), 3), "ordinary/"+key)
        metric = data.get("metric")
        if not isinstance(metric, dict):
            raise ValueError("the original metric array dictionary is required")
        for key in ("a", "a_s", "a_ss"):
            _finite(metric.get(key), (len(r),), "ordinary/metric/"+key)
        for key, expected in (("radial", r), ("theta", th)):
            if key in data and not _same_bytes(np.asarray(data[key], dtype=float), expected):
                raise ValueError("ordinary "+key+" binding mismatch")
        record = {
            "schema": POLICY+"-bound-ordinary",
            "field_definition_sha256": self.definition_sha256,
            "coordinate_definition_sha256": self.coordinate_definition_sha256,
            "physical_identity_sha256": digest(self.identity(q)),
            "state": q.copy(), "radial": r.copy(), "theta": th.copy(),
            "data": data,
            "source_receipt": copy.deepcopy(source_receipt),
            "complete_six_position_jets_required": True,
            "no_ordinary_evaluation_in_binding": True,
        }
        for key in ("state", "radial", "theta"):
            record[key].setflags(write=False)
        record["binding_sha256"] = digest({
            "schema": record["schema"],
            "field_definition_sha256": self.definition_sha256,
            "coordinate_definition_sha256": self.coordinate_definition_sha256,
            "physical_identity_sha256": record["physical_identity_sha256"],
            "state": array_binding(record["state"]),
            "radial": array_binding(record["radial"]),
            "theta": array_binding(record["theta"]),
            "source_receipt": record["source_receipt"],
        })
        return record

    def validate_bound(self, state, radial, theta, bound):
        self._assert_context()
        q = self.validate_state(state)
        r, th = _validate_grid(radial, theta)
        if (not isinstance(bound, dict)
                or bound.get("schema") != POLICY+"-bound-ordinary"
                or bound.get("field_definition_sha256") != self.definition_sha256
                or bound.get("coordinate_definition_sha256") != self.coordinate_definition_sha256
                or bound.get("physical_identity_sha256") != digest(self.identity(q))
                or not _same_bytes(bound.get("state"), q)
                or not _same_bytes(bound.get("radial"), r)
                or not _same_bytes(bound.get("theta"), th)):
            raise ValueError("ordinary input is not bound to this exact168 state/grid/reference")
        return q, r, th, bound["data"]

    def geometry(self, state, radial, theta, quadrature_order=4, *,
                 jacobian=False, full_two_jet_jacobian=False,
                 supplied_zero_geometry=None):
        """Current ordinary six jets.  Old159 Jacobians are never requested.

        With zero extras, an explicitly supplied bound returns the same old
        data object.  With no supplied data, a necessary ordinary call is made
        and must be charged by the caller.  At nonzero extras only current
        reference inputs and current full scalar fields are assembled.
        """
        self._assert_context()
        q = self.validate_state(state)
        r, th = _validate_grid(radial, theta)
        if jacobian or full_two_jet_jacobian:
            raise ValueError("use the new-nine derivative API; no implicit old159 Jacobian")
        if int(quadrature_order) < 1:
            raise ValueError("positive original query quadrature order required")
        zero = not np.any(q[159:] != 0.)
        if supplied_zero_geometry is not None:
            if not zero:
                raise ValueError("an old ordinary cache is usable only at exact zero extras")
            return self.validate_bound(q, r, th, supplied_zero_geometry)[3]
        if zero:
            return self.original_field.geometry(q[:159], r, th, quadrature_order,
                                                jacobian=False, full_two_jet_jacobian=False)

        original = self.original_field
        reference163 = original.coordinates.reference_evaluation_state(q[:159])
        old = original._direct_single.to_old(reference163)
        reference = original._reference_data(old, r)
        grid, fields, frame = self.scalar_frame(q, r, th)
        metric = reference["metric"]
        a, ap, app = (np.asarray(metric[key], dtype=float) for key in ("a", "a_s", "a_ss"))
        P, Ps, Pss = (periodic_operator(frame[key], -1) for key in ("T", "Ts", "Tss"))
        height, center = reference["height"], reference["center"]

        X = a[:, None, None]*P
        X[..., 2] += center[:, None]
        Xs = ap[:, None, None]*P + a[:, None, None]*Ps
        Xs[..., 2] += height["b"][:, None]
        Xss = app[:, None, None]*P + 2*ap[:, None, None]*Ps + a[:, None, None]*Pss
        Xss[..., 2] += height["b_s"][:, None]
        data = {
            "X": X, "Xs": Xs, "Xt": a[:, None, None]*frame["T"],
            "Xss": Xss, "Xst": ap[:, None, None]*frame["T"]+a[:, None, None]*frame["Ts"],
            "Xtt": a[:, None, None]*frame["Ttheta"],
            "T": frame["T"], "Ts": frame["Ts"], "Tss": frame["Tss"],
            "Ttheta": frame["Ttheta"],
            "metric": metric, "height": height, "center": center,
            "primitive": P, "radial": r, "theta": th,
            "auxiliary_R_not_used_as_metric_residual": True,
        }
        data = original._null_height_update(
            data, q[:159], r, jacobian=False, full_two_jet_jacobian=False)
        if q[167] != 0.:
            hh = grid.radial_body["height"]
            active = (r > LEFT) & (r < RIGHT)
            data["center"] = np.asarray(data["center"]).copy()
            data["center"][active] += q[167]*hh["center"][active]
            for key, change in (("X", "center"), ("Xs", "b"), ("Xss", "b_s")):
                value = np.asarray(data[key]).copy()
                value[active, :, 2] += q[167]*hh[change][active, None]
                data[key] = value
            data["height"] = {key: np.asarray(value).copy()
                              for key, value in data["height"].items()}
            for key in ("b", "b_s", "b_ss"):
                data["height"][key][active] += q[167]*hh[key][active]
        data.update(
            complete_body_extension_definition_sha256=self.definition_sha256,
            coordinate_definition_sha256=self.coordinate_definition_sha256,
            independent_geometry_parameter_count=INDEPENDENT_COUNT,
            physical_geometry_parameter_count=PHYSICAL_COUNT,
            complete_original_reference_retained=True,
            old159_geometry_Jacobian_recomputed=False)
        if any(not np.all(np.isfinite(data[key])) for key in POSITION_KEYS):
            raise FloatingPointError("nonfinite current body168 ordinary position jets")
        return data

    def frozen_metric_copy(self, state):
        return self, self.validate_state(state).copy()
