#!/usr/bin/env python3
"""Exact-affine working queries of the unchanged complete R711 seed provider.

This adapter adds an address interface. It does not replace the original
provider, its frozen seed definition, its whole mean quadrature or its roots.
Every precise affine location is retained as two Fractions. An original
cell/local fast path is used only after exact rational identity AND binary64
representability have been proved. Otherwise the original full scalar law
is queried at the exact affine point.

All numerical evaluation belongs in the public repository Actions.
The pure definition/validator imports no scientific package.
"""
from __future__ import annotations

from fractions import Fraction
import copy
import hashlib
import inspect
import json
import math
import os
from pathlib import Path
import time

SCHEMA = "complete-fixed-fejer-supported-meridian-exact-affine-query-v1"
PROVIDER_SHA256 = "ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a"
PROVIDER_SCHEMA = "complete-fixed-fejer-supported-smooth-triangle-meridian-seed-reference-v1"
REFERENCE_SHA256 = "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb"
REFERENCE_SCHEMA = "R690-fixed-fejer-axisymmetric-SO3-reference-input-v1"
MEAN_KERNEL_SHA256 = "f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917"
REFERENCE_J = 923
REFERENCE_M = 160
METHODS = ("_compare", "_width", "_carrier", "_region", "_scaled_coordinate",
    "_cutoff_and_profile", "_scalar", "_prepare_plan", "_chart", "_means",
    "evaluate", "metadata")
ARRAY_KEYS = ("T0", "T0_s", "T0_phi", "T0_phiphi")


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Exact-affine reference queries require public repository Actions")


def sha(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            value.update(chunk)
    return value.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
        allow_nan=False).encode()).hexdigest()


def digest(value, name):
    if (not isinstance(value, str) or len(value) != 64
            or any(c not in "0123456789abcdef" for c in value)):
        raise ValueError("Keep the complete SHA256: "+name)
    return value


def exact(value):
    if isinstance(value, bool):
        raise TypeError("A boolean is not an exact affine coefficient")
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    if not isinstance(value, str):
        raise TypeError("Use Fraction, integer or canonical rational strings")
    answer = Fraction(value)
    if str(answer) != value:
        raise ValueError("Use canonical rational coefficient strings")
    return answer


def exact_point(value):
    if not isinstance(value, (tuple, list)) or len(value) != 2:
        raise ValueError("An exact affine point contains both alpha and beta")
    return tuple(exact(v) for v in value)


def point_record(value):
    return [str(v) for v in exact_point(value)]


def definition(seed_model, *, expected_seed_identity_sha256,
               expected_reference_identity_sha256):
    """Complete fixed-seed source binding; it is not a field or error certificate."""
    digest(expected_seed_identity_sha256, "seed identity")
    digest(expected_reference_identity_sha256, "reference identity")
    if not isinstance(seed_model, dict):
        raise ValueError("Retain the complete original seed model")
    reference = seed_model.get("complete_axisymmetric_reference_model")
    if (seed_model.get("schema") != PROVIDER_SCHEMA
            or seed_model.get("source_sha256") != PROVIDER_SHA256
            or seed_model.get("original_reference_source_sha256") != REFERENCE_SHA256
            or seed_model.get("mean_kernel_source_sha256") != MEAN_KERNEL_SHA256
            or canonical(seed_model) != expected_seed_identity_sha256
            or not isinstance(reference, dict)
            or reference.get("schema") != REFERENCE_SCHEMA
            or reference.get("source_sha256") != REFERENCE_SHA256
            or reference.get("J") != REFERENCE_J or reference.get("M") != REFERENCE_M
            or canonical(reference) != expected_reference_identity_sha256
            or seed_model.get("initial_reference_model_identity_sha256")
                != expected_reference_identity_sha256):
        raise ValueError("Bind the whole unchanged provider, seed and reference")
    for key in ("fixed_scalar_metric_identity_sha256",
                "fixed_scalar_profile_definition", "fixed_chart_core_sha256"):
        if seed_model.get(key) != reference.get(key):
            raise ValueError("The original fixed seed/reference differs: "+key)
    return dict(schema=SCHEMA, source_sha256=sha(__file__),
        original_provider_source_sha256=PROVIDER_SHA256,
        original_reference_source_sha256=REFERENCE_SHA256,
        original_mean_kernel_source_sha256=MEAN_KERNEL_SHA256,
        complete_original_seed_model=copy.deepcopy(seed_model),
        original_seed_identity_sha256=expected_seed_identity_sha256,
        original_reference_identity_sha256=expected_reference_identity_sha256,
        fixed_reference_J=REFERENCE_J, fixed_reference_M=REFERENCE_M,
        point_representation="exact ordered Fraction(alpha,beta), s=alpha*S+beta",
        original_cell_local_fast_path_requires_exact_affine_identity=True,
        original_local_fast_path_requires_exact_binary64_representability=True,
        approximate_local_conversion_or_nearest_point_used=False,
        scalar_fallback="original complete context.law.at(exact_affine_point)",
        original_mean_provider_and_full_radial_plan_unchanged=True,
        original_mean_cache_key_and_literal_angle_order_unchanged=True,
        current_outer_free_point_used_to_define_reference=False,
        reference_norm_and_three_angular_radial_jets_complete=True,
        working_scalar_normalization_trig_root_and_query_errors_enclosed=False,
        full_current_field_or_continuous_certificate=False)


def validate_definition(value):
    if not isinstance(value, dict):
        raise ValueError("Keep the complete exact-affine reference query definition")
    expected = definition(value.get("complete_original_seed_model"),
        expected_seed_identity_sha256=value.get("original_seed_identity_sha256"),
        expected_reference_identity_sha256=value.get("original_reference_identity_sha256"))
    if value != expected:
        raise ValueError("The full exact-affine reference query policy changed")
    return canonical(expected)


def binary_address_for_exact_point(point, nodes, original_cell):
    """Return an EXACT old cell/local representation, or None; never round a point."""
    point = exact_point(point)
    if (type(original_cell) is not int or not 0 <= original_cell < len(nodes)-1):
        raise ValueError("Use an actual original integer cell")
    left, right = exact_point(nodes[original_cell]), exact_point(nodes[original_cell+1])
    delta = tuple(b-a for a, b in zip(left, right))
    if delta == (0, 0):
        raise ValueError("Distinct original affine nodes are required")
    channel = 0 if delta[0] else 1
    local = (point[channel]-left[channel])/delta[channel]
    if not 0 <= local <= 1:
        raise ValueError("The supplied original cell does not contain the exact point")
    if tuple(a+local*d for a, d in zip(left, delta)) != point:
        # For the actual dyadic refinement each point has the original-cell
        # affine representation by construction. Other supplied points must
        # use the exact scalar fallback, not an inexact chart conversion.
        return None
    word = float(local)
    if not math.isfinite(word) or Fraction.from_float(word) != local:
        return None
    return original_cell, word


def points_from_cells(nodes, cells, local):
    """Pure exact address conversion; finite float locals are interpreted as words."""
    points = tuple(exact_point(v) for v in nodes)
    if len(points) < 2 or len(cells) != len(local) or not len(cells):
        raise ValueError("Use every exact node and one local word per row")
    result = []
    for cell, value in zip(cells, local):
        if type(cell) is not int or not 0 <= cell < len(points)-1:
            raise ValueError("Current cells are exact integers")
        if isinstance(value, bool):
            raise TypeError("A boolean is not a local coordinate")
        if isinstance(value, float):
            if not math.isfinite(value):
                raise ValueError("Use a finite literal local coordinate")
            u = Fraction.from_float(value)
        else:
            u = exact(value)
        if not 0 <= u <= 1:
            raise ValueError("Use the full closed local interval")
        result.append(tuple((1-u)*a+u*b
            for a, b in zip(points[cell], points[cell+1])))
    return tuple(result)


class ExactAffineReferenceFailure(RuntimeError):
    def __init__(self, reason, record):
        super().__init__(reason)
        self.record = record


class ExactAffineSupportedReference:
    """Four whole working reference jets at precise affine radial addresses."""

    def __init__(self, provider, *, expected_seed_identity_sha256,
                 expected_reference_identity_sha256):
        require_actions()
        self.provider = provider
        self.context = provider.context
        self.definition = definition(provider.model,
            expected_seed_identity_sha256=expected_seed_identity_sha256,
            expected_reference_identity_sha256=expected_reference_identity_sha256)
        self.identity = canonical(self.definition)
        self._initial_seed_model = copy.deepcopy(provider.model)
        self._initial_seed_identity = provider.model_identity
        self._initial_reference_identity = self.context.identity
        self._nodes = tuple(exact_point(v) for v in self.context.nodes)
        if (len(self._nodes) != REFERENCE_J
                or self._nodes[0] != (0, 0) or self._nodes[-1] != (1, 0)):
            raise ValueError("Retain all original exact reference nodes from 0 to S")
        self._node_identity = canonical([point_record(v) for v in self._nodes])
        self._radial_cache = {}
        self.counts = dict(evaluations_started=0, evaluations_completed=0,
            evaluations_failed=0, requested_radial_rows=0, requested_angle_points=0,
            radial_batches_constructed=0, radial_cache_hits=0,
            exact_original_binary_address_queries=0, exact_affine_scalar_queries=0)
        self.last_call = None
        self._check_binding()

    def _check_binding(self):
        p, c = self.provider, self.context
        if (sha(inspect.getfile(type(p))) != PROVIDER_SHA256
                or sha(inspect.getfile(type(c))) != REFERENCE_SHA256
                or sha(inspect.getfile(type(c.law))) != REFERENCE_SHA256
                or p.context is not c or p.model != self._initial_seed_model
                or canonical(p.model) != self._initial_seed_identity
                or p.model_identity != self._initial_seed_identity
                or c.identity != self._initial_reference_identity
                or canonical(c.model) != c.identity
                or tuple(exact_point(v) for v in c.nodes) != self._nodes):
            raise ValueError("The whole original provider/reference/node identity changed")
        for name in METHODS:
            method = getattr(p, name)
            function = getattr(method, "__func__", method)
            if sha(function.__code__.co_filename) != PROVIDER_SHA256:
                raise ValueError("Use the actual complete original provider method: "+name)
        if (sha(c.law.at.__func__.__code__.co_filename) != REFERENCE_SHA256
                or sha(c.reference_at.__func__.__code__.co_filename) != REFERENCE_SHA256
                or sha(p.kernel.__file__) != MEAN_KERNEL_SHA256):
            raise ValueError("Retain the complete original scalar and mean functions")
        validate_definition(self.definition)

    def _fail(self, phase, reason, **details):
        record = dict(schema=SCHEMA, source_sha256=sha(__file__),
            definition_identity_sha256=self.identity,
            complete=False, phase=phase, reason=str(reason),
            original_seed_identity_sha256=self._initial_seed_identity,
            counts=dict(self.counts), continuous_certificate=False, **details)
        self.last_call = record
        raise ExactAffineReferenceFailure(str(reason), record)

    def _radial(self, points, original_cells):
        import numpy as np
        addresses = []
        for point, hint in zip(points, original_cells):
            if (self.provider._compare(point, (Fraction(0), Fraction(0))) < 0
                    or self.provider._compare(point, (Fraction(1), Fraction(0))) > 0):
                self._fail("exact_radial_domain", "An exact affine query leaves the original whole domain",
                    point=point_record(point))
            if hint is None:
                addresses.append(None)
            else:
                addresses.append(binary_address_for_exact_point(point, self._nodes, hint))
        address_words = [None if a is None else dict(cell=a[0],local_hex=a[1].hex())
            for a in addresses]
        descriptor = dict(definition_identity_sha256=self.identity,
            original_nodes_identity_sha256=self._node_identity,
            exact_affine_points=[point_record(v) for v in points],
            original_binary_addresses=address_words)
        key = canonical(descriptor)
        cached = self._radial_cache.get(key)
        if cached is not None:
            if cached["descriptor"] != descriptor:
                raise ValueError("A complete exact radial-query key collision occurred")
            self.counts["radial_cache_hits"] += 1
            return cached["arrays"], descriptor, key
        values, kinds, chi, chis, profile, profiles = [], [], [], [], [], []
        names = {"outside": 0, "left": 1, "right": 1, "central": 2}
        for point, address in zip(points, addresses):
            kind, index = self.provider._region(point)
            # This is precisely the original source's full scalar method.
            # Passing None invokes law.at(point) with both exact Fractions.
            values.append(self.provider._scalar(point, address))
            if address is None:
                self.counts["exact_affine_scalar_queries"] += 1
            else:
                self.counts["exact_original_binary_address_queries"] += 1
            c0, c1, h0, h1 = self.provider._cutoff_and_profile(point, kind, index)
            kinds.append(names[kind])
            chi.append(c0); chis.append(c1); profile.append(h0); profiles.append(h1)
        arrays = dict(values=np.asarray(values,dtype=np.float64),
            kinds=np.asarray(kinds,dtype=np.int64), chi=np.asarray(chi,dtype=np.float64),
            chi_s=np.asarray(chis,dtype=np.float64),
            profile=np.asarray(profile,dtype=np.float64),
            profile_s=np.asarray(profiles,dtype=np.float64))
        if arrays["values"].shape != (len(points),4):
            self._fail("radial_shapes", "Retain all four original normalized scalar jets")
        for value in arrays.values():
            if not np.isfinite(value).all():
                self._fail("radial_carriers", "An actual complete radial carrier is nonfinite")
            value.setflags(write=False)
        self.counts["radial_batches_constructed"] += 1
        self._radial_cache[key] = dict(descriptor=descriptor, arrays=arrays)
        return arrays, descriptor, key

    def evaluate(self, points, phi, *, original_cells=None):
        require_actions()
        import numpy as np
        self._check_binding()
        points = tuple(exact_point(v) for v in points)
        if not points:
            raise ValueError("Do not omit the requested radial rows")
        if original_cells is None:
            original_cells = (None,)*len(points)
        else:
            original_cells = tuple(original_cells)
        if len(original_cells) != len(points) or any(v is not None
                and (type(v) is not int or not 0 <= v < REFERENCE_J-1)
                for v in original_cells):
            raise ValueError("Keep every original-cell hint, or explicitly supply None")
        raw_phi = np.asarray(phi)
        if (raw_phi.ndim != 1 or not len(raw_phi) or np.iscomplexobj(raw_phi)
                or not np.isfinite(raw_phi).all()):
            raise ValueError("Use all finite literal fixed-chart angle words")
        phi = np.asarray(raw_phi,dtype=np.float64)
        phi_words = [float(v).hex() for v in phi]
        self.counts["evaluations_started"] += 1
        self.counts["requested_radial_rows"] += len(points)
        self.counts["requested_angle_points"] += len(points)*len(phi)
        start = time.monotonic()
        try:
            chart = self.provider._chart(phi)
            mean = self.provider._means(phi,chart)
            radial, descriptor, radial_identity = self._radial(points,original_cells)
            B, C, Bs, Cs = radial["values"].T
            ez = np.array((0.,0.,1.))
            T = B[:,None,None]*chart["e0"][None]+C[:,None,None]*ez
            Ts = Bs[:,None,None]*chart["e0"][None]+Cs[:,None,None]*ez
            Tp = B[:,None,None]*chart["e1"][None]
            Tpp = B[:,None,None]*chart["e2"][None]
            d, dp, dpp = (mean[name][None] for name in ("d","d_phi","d_phiphi"))
            w, wp, wpp = (mean[name][None] for name in ("w","w_phi","w_phiphi"))
            boundary = radial["kinds"] == 1
            if np.any(boundary):
                chi = radial["chi"][boundary,None,None]
                chis = radial["chi_s"][boundary,None,None]
                Y = (1.-chi)*T[boundary]+chi*d
                Yp = (1.-chi)*Tp[boundary]+chi*dp
                Ypp = (1.-chi)*Tpp[boundary]+chi*dpp
                Ys = (1.-chi)*Ts[boundary]+chis*(d-T[boundary])
                norm = np.linalg.norm(Y,axis=-1)
                if not np.isfinite(norm).all() or np.any(norm <= 0):
                    self._fail("boundary_normalization",
                        "The complete actual boundary blend is zero or nonfinite",
                        literal_angle_hex=phi_words)
                unit = Y/norm[...,None]
                rp = np.sum(unit*Yp,axis=-1)
                rpp = (np.sum(Yp*Yp+Y*Ypp,axis=-1)-rp*rp)/norm
                up = (Yp-unit*rp[...,None])/norm[...,None]
                upp = (Ypp-unit*rpp[...,None]-2.*up*rp[...,None])/norm[...,None]
                us = (Ys-unit*np.sum(unit*Ys,axis=-1)[...,None])/norm[...,None]
                T[boundary], Tp[boundary], Tpp[boundary], Ts[boundary] = unit,up,upp,us
            central = radial["kinds"] == 2
            if np.any(central):
                h = radial["profile"][central,None]
                hs = radial["profile_s"][central,None]
                alpha = h*mean["lambda"][None]
                ap = h*mean["lambda_phi"][None]
                app = h*mean["lambda_phiphi"][None]
                sn, co = np.sin(alpha)[...,None],np.cos(alpha)[...,None]
                ap, app = ap[...,None],app[...,None]
                unit = co*d+sn*w
                tangent = -sn*d+co*w
                up = co*dp+sn*wp+ap*tangent
                upp = (co*dpp+sn*wpp+2.*ap*(-sn*dp+co*wp)
                    +app*tangent-ap*ap*unit)
                us = (hs*mean["lambda"][None])[...,None]*tangent
                T[central], Tp[central], Tpp[central], Ts[central] = unit,up,upp,us
            result = dict(T0=T,T0_s=Ts,T0_phi=Tp,T0_phiphi=Tpp,
                norm=np.linalg.norm(T,axis=-1),theta_parent=chart["theta"],
                rho_parent=chart["rho"],rho_phi_parent=chart["rhop"])
            for name in ARRAY_KEYS:
                if result[name].shape != (len(points),len(phi),3):
                    self._fail("complete_reference_jets", "A complete four-jet shape changed")
            for value in result.values():
                if not np.isfinite(value).all():
                    self._fail("complete_reference_jets", "A complete reference jet is nonfinite")
                value.setflags(write=False)
            self._check_binding()
            self.counts["evaluations_completed"] += 1
            self.last_call = dict(schema=SCHEMA,source_sha256=sha(__file__),
                definition_identity_sha256=self.identity,complete=True,
                original_provider_source_sha256=PROVIDER_SHA256,
                original_seed_model_identity_sha256=self._initial_seed_identity,
                original_reference_model_identity_sha256=self._initial_reference_identity,
                exact_radial_query_identity_sha256=radial_identity,
                requested_radial_rows=len(points),requested_angle_count=len(phi),
                literal_angle_hex=phi_words,original_provider_mean_plan_reused=True,
                exact_affine_input=True,rounded_original_local_used=False,
                source_bound_original_binary_fast_paths=sum(a is not None
                    for a in descriptor["original_binary_addresses"]),
                exact_scalar_fallback_rows=sum(a is None
                    for a in descriptor["original_binary_addresses"]),
                seconds=time.monotonic()-start,
                ordinary_working_errors_enclosed=False,current_field_certificate=False)
            result["metadata"] = copy.deepcopy(self.last_call)
            return result
        except Exception as exc:
            self.counts["evaluations_failed"] += 1
            if isinstance(exc,ExactAffineReferenceFailure):
                self.last_call["counts"] = dict(self.counts)
            if not isinstance(exc,ExactAffineReferenceFailure):
                self.last_call = dict(schema=SCHEMA,source_sha256=sha(__file__),
                    definition_identity_sha256=self.identity,complete=False,
                    phase="actual_original_reference_or_affine_query",
                    reason=str(exc),exception_type=type(exc).__name__,
                    literal_angle_hex=phi_words,requested_radial_rows=len(points),
                    seconds=time.monotonic()-start,current_field_certificate=False)
            raise

    def evaluate_cells(self, nodes, cells, local, phi, *, original_cells=None):
        """Use precise current-node definitions; do not turn their points into nearby old u."""
        require_actions()
        points = points_from_cells(nodes,cells,local)
        return self.evaluate(points,phi,original_cells=original_cells)

    def metadata(self):
        self._check_binding()
        return dict(schema=SCHEMA,source_sha256=sha(__file__),
            definition=copy.deepcopy(self.definition),
            definition_identity_sha256=self.identity,
            original_reference_node_identity_sha256=self._node_identity,
            counts=dict(self.counts),cached_exact_radial_batches=len(self._radial_cache),
            last_call=copy.deepcopy(self.last_call),
            original_provider_seed_model_unchanged=True,
            original_provider_mean_plan_and_cache_definitions_unchanged=True,
            scalar_normalization_trigonometric_and_query_errors_enclosed=False,
            current_normal_root_and_physical_field_error_paid=False)
