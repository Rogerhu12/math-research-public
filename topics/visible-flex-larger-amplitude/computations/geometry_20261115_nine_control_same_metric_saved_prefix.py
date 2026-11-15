#!/usr/bin/env python3
"""Complete physical SavedPrefix for the explicit all-nine-frozen450 v2 field.

The input must be an actually accepted v2 full-DN output. Neither the earlier
453-row design field nor a recipe/failed native packet is a 450 acceptance.
All nine coefficients and both original finite scalar assembly paths remain
identified by the frozen v2 producer. The physical quintic, complete z0,
material inverse, all nine jets and one global SE(2) use the original kernels.
No numerical acceptance, continuous envelope or completed closed field is
created by reading the checkpoint. Scientific evaluation is Actions-only.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
from fractions import Fraction as Q
from pathlib import Path
from types import SimpleNamespace

for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import numpy as np
import geometry_20261114_large_core_saved_prefix as original
import geometry_20261114_material_quintic_readout as physical
from root_20261114_scaled_core import r225_coefficients

HERE = Path(__file__).resolve().parent
SCHEMA = "frozen-nine450-complete-saved-prefix-v1"
FIELD_SCHEMA = "nine-control-all-frozen-same-metric450-complete-physical-DN-v2"
SCALAR_SCHEMA = "frozen-nine-control-complete-same-metric-scalar-v2"
ENTRY_NAME = "geometry_20261115_nine_control_same_metric_full112_v2.py"
PROFILE_NAME = "geometry_20261115_nine_control_same_metric_profile_v2.py"
PARAMETER_ORDER = ["p1", "p2", "p3", "theta1", "theta2", "theta3", "eta1", "eta2", "eta3"]
SOURCE_PINS = {
    "geometry_20261115_nine_control_same_metric_full112_v2.py": "92cfb0701824df770dfcd009a623e84695e72fe9c489d70537d8983415adc7e8",
    "geometry_20261115_nine_control_same_metric_profile_v2.py": "5e95afdb82f83a276003e6a4846e20893b7eb7f2b44b309d56950f11dbfaa0d3",
    "geometry_20261114_large_core_saved_prefix.py": "51eab8cdc878e22ad2c57bab129b1ef31463799596fcc40399fd8b0714ccbea0",
    "geometry_20261114_material_quintic_readout.py": "14e550ed75ad86bd8308966711313b7e0cd8917a2c166c90cf4e6ca1f5f85756",
    "root_20261114_scaled_core.py": "8f9fe56da99c21ef9b1e585f6000b595aec5098b13bdda197634bba9f86a7c7a",
}
# The complete unchanged local Python import/declared-file closure of the
# physical-jet kernel is separate from the accepted450 producer closure.
PHYSICAL_KERNEL_PINS = {
    "alternative-angle-plateau-connector.py": "d9b1a9b9822664fb466942ccab13d2319c9d0f23c7ccacef2aae193b5e7b9ad7",
    "alternative-controlled-profile.py": "0af61a3bfccf093bfe6c255f864c658c37119b890f362d5d2e16429d2969e430",
    "alternative-direct-tail-connector.py": "9a6462c60bc8b3607decca6aab894210011b40903b0406c233090ff7856d4241",
    "alternative-fast-profile.py": "d6e0515c179a1e96ff2507e4fb5c8e3974ca170a0821af7e0441c7564cc0cc76",
    "alternative-neck-excursion.py": "f70571b8356e33cb89eabae2dba4e173e6612dac4d65d5df74f5ec14c34ad53c",
    "alternative-neck-flatturn.py": "c0578ed401a2433c72ec99702c9c32a8412c66264a7fb81a8b8c74ba054fbbdd",
    "alternative-neck-provider.py": "84ed048425c8b0f4deeec8af37828e318150cde5d59995da77f64d923591b9c2",
    "alternative-outward-probe.py": "cf163a5c42cff95137a78eefda058b6a18f5f226b4261b686a42e645f4002fcb",
    "geometry_20261114_block_csc_bvp.py": "af91df83e0bbf255c79ae25d49f107f4967380bfcdaf56c689bdde54b344835e",
    "geometry_20261114_fft_frenet.py": "973898fcea1e8706d0ff9f87bbe72cde3576bc0055149af0a2e2058b144ac401",
    "geometry_20261114_full_dn_readout.py": "f6602baa54d3f599deb7d7c40ac9f4806e5faca2fc305b674b1c1cda02067cb1",
    "geometry_20261114_full_scalar_profile.py": "8ff23e31a58d0f8b087929d69ac8d6f9b6f2777615e50eef5ebe40ed7b6bed6b",
    "geometry_20261114_large_core_saved_prefix.py": "51eab8cdc878e22ad2c57bab129b1ef31463799596fcc40399fd8b0714ccbea0",
    "geometry_20261114_material_quintic_readout.py": "14e550ed75ad86bd8308966711313b7e0cd8917a2c166c90cf4e6ca1f5f85756",
    "geometry_20261114_prefix_controls_profile.py": "f019e6b33c8e1776d5cca87c22efadd0f999766b894be855efb53ad10b4d6a24",
    "geometry_20261114_r225_fixed_profile.py": "478d0bf603ea05a9f20228ff2fd591e2f767e6ab0686a6129b1114aa831b0c6c",
    "geometry_20261114_r225_free_core_bvp.py": "a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08",
    "geometry_20261114_r225_high_core_bvp.py": "e12916dcf30dd2088ad59d2059647c8a03bed446aeee693b88f423730fa5a530",
    "geometry_20261114_r225_outward_probe.py": "64a3fd482f6ee01f4d149971dff1212b2c2ca3bdb00f1b733c7b119b458bab5f",
    "root_20261114_scaled_core.py": "8f9fe56da99c21ef9b1e585f6000b595aec5098b13bdda197634bba9f86a7c7a",
    "root_profile_scan.py": "3d940a78d18f509b98caa4fb8782ea34ad54423a58bf94e0f386f4f20e2994db",
    "strong_20261114_scaled_core_tail_connector.py": "661d5d84dc0dd3da46f4936c2c3ad28f80df3475f421c56d770a2afa6402ac08",
    "strong_angle_boost.py": "ce2117cffe2e55d310eb0be219e7d22e750d97cd22704e75c3dd74a085c020be"
}
read, sha, actions_only = original.read, original.sha, original.actions_only
PhysicalQuintic = original.PhysicalQuintic
complete_material_means = original.complete_material_means


def checked_sources():
    result = {}
    for table in (PHYSICAL_KERNEL_PINS, SOURCE_PINS):
        for name, expected in table.items():
            actual = sha(HERE/name)
            if actual != expected or (name in result and result[name] != expected):
                raise ValueError("A complete scalar/physical source differs: "+name)
            result[name] = actual
    result[Path(__file__).name] = sha(__file__)
    return result


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False).encode("utf-8")).hexdigest()


def validate_checkpoint(data, receipt):
    """Use the real producer closure and complete parent reader, unchanged."""
    actions_only()
    consumer_sources = checked_sources()
    if (data.get("schema") != FIELD_SCHEMA
            or data.get("fixed_scalar_profile", {}).get("geometry", {}).get("schema") != SCALAR_SCHEMA):
        raise ValueError("Use an actually accepted all-nine-frozen450 v2 output; no design or legacy fallback")
    import geometry_20261115_nine_control_same_metric_full112_v2 as producer
    runtime = producer.runtime()
    # Do not add consumer sources to runtime.closure: the accepted producer's
    # own complete source identity is an exact, independently checked object.
    profile, mesh, retained, parent_binding = runtime.frozen.freeze_parent(
        runtime, data, receipt, accepted=None)
    scalar = profile.specification
    metric = data["original_metric_identity"]
    if (data.get("state_dimension") != 450 or data.get("physical_state_dimension") != 338
            or data.get("left_rows") != 338 or data.get("right_rows") != 112
            or data.get("finite_boundary_scheme") != "physical-phi-complete-DN-v1"
            or data.get("canonical_scalar_identity_sha256") != profile.canonical_scalar_identity_sha256
            or metric.get("schema") != "frozen-nine-same-material-metric-v1"
            or metric.get("canonical_scalar_identity_sha256") != profile.canonical_scalar_identity_sha256
            or runtime.frozen.canonical_bytes(metric.get("scalar_specification")) !=
               runtime.frozen.canonical_bytes(scalar)
            or runtime.frozen.words(data.get("complete_nine_scalar_parameters", [])) !=
               scalar["frozen_nine_float64le"]):
        raise ValueError("The actual450 dimensions or complete same-g scalar identity differ")
    identity = dict(
        schema=SCHEMA, scalar_schema=SCALAR_SCHEMA, field_schema=FIELD_SCHEMA,
        canonical_scalar_identity_sha256=profile.canonical_scalar_identity_sha256,
        actual_field_modes=112, actual_tail_modes=112, actual_angular_quadrature=2048,
        physical_state_dimension=338, augmented_state_dimension=450,
        active_scalar_parameters=0, fixed_core_modes=0, separated_left_rows=338,
        right_rows=112, active_parameter_indices=[], frozen_parameter_indices=list(range(9)),
        parameter_order=PARAMETER_ORDER, frozen_design_parameters=scalar["frozen_design_parameters"],
        frozen_nine_float64le=scalar["frozen_nine_float64le"],
        scalar_support_float64le=copy.deepcopy(scalar["scalar_support_float64le"]),
        actual_accepted_source_prefix_modes=96,
        accepted_source_prefix_sha256=scalar["accepted_source_prefix_sha256"],
        original_design_field_modes=112,
        origin_design_field=copy.deepcopy(scalar["origin_design_field"]),
        accepted_field_file=copy.deepcopy(receipt),
        source_prefix_relabelled_as_accepted_new_field=False,
        design453_relabelled_as_accepted450=False,
        prepared_or_failed_state_accepted_by_this_reader=False,
        full_mean_height_included=True, old_mean_added=False,
        parent_amplitude_or_reach_inherited=False,
        analytic_material_circle_lift_present=False)
    binding = dict(schema="frozen-nine450-saved-prefix-source-binding-v1",
        accepted_field=copy.deepcopy(receipt), accepted_field_source_sha256=data["source_sha256"],
        original_reported_acceptance=parent_binding["parent_reported_original_acceptance"],
        complete_parent_binding=parent_binding,
        accepted_producer_source_sha256=copy.deepcopy(runtime.closure),
        consumer_source_sha256=consumer_sources,
        canonical_scalar_identity_sha256=profile.canonical_scalar_identity_sha256,
        complete_scalar_specification_sha256=canonical_sha(scalar),
        finite_assembly=copy.deepcopy(scalar["finite_assembly"]),
        original_source_metric_identity=copy.deepcopy(data["original_source_metric_identity"]),
        same_g_refers_to_origin_nine_design_not_accepted96=True,
        new_BVP_or_native_acceptance_created=False)
    return profile, identity, binding


class NineControlSameMetricSavedPrefix(original.LargeCoreSavedPrefix):
    """Original full physical/nine-jet API with the actual v2 scalar owner."""
    def __init__(self, checkpoint):
        actions_only()
        self.path = Path(checkpoint)
        self.rec = read(self.path)
        d = self.rec
        # The complete payload may move or be renamed; its mathematical
        # definition binds actual whole-file bytes/SHA, not a storage path.
        receipt = dict(bytes=self.path.stat().st_size, sha256=sha(self.path))
        profile, identity, source_binding = validate_checkpoint(d, receipt)
        self.M, self.N, self.mode = int(d["M"]), int(d["N"]), 2
        self.n = 3*self.M+2
        self.core = np.asarray(d["core"]["coefficients"], float)
        self.frequencies = 2*np.arange(1, self.M+1)
        self.density = (1-self.frequencies**2)*self.core
        reference = [Q(6,5)*v for v in r225_coefficients()]
        exact_core = [Q(float(v)) for v in self.core]
        rho_reference_lower = 1+sum((1-4*m*m)*v for m,v in enumerate(reference,1))
        rho_difference = sum((4*m*m-1)*abs(v-(reference[m-1] if m <= len(reference) else 0))
                             for m,v in enumerate(exact_core,1))
        self.rho_lower_exact = rho_reference_lower-rho_difference
        if self.M < len(reference) or self.rho_lower_exact <= 0:
            raise ValueError("The R237 complete-core bound does not certify this global material inverse; a stronger density certificate is required")
        self.profile_model = profile
        x, Y, DY = (np.asarray(d[k], float) for k in ("mesh", "states", "rhs"))
        if Y.shape != (len(x), self.n) or DY.shape != Y.shape or self.core.shape != (self.M,):
            raise ValueError("The saved state is not the complete r0..rM,t1..tM,z0..zM layout")
        if not np.all(np.isfinite(Y)) or not np.all(np.isfinite(DY)):
            raise ValueError("Nonfinite saved physical field")
        law = d["original_source_metric_identity"]["law"]
        q = physical.base.native.outward.FullCoreProbe(self.core, self.M, self.N,
                        law["velocity"], law["length"], law["k0"])
        q.profile = self.profile_model.profile
        physical.base.fixed.fft.enable_fft(q)
        DDY, gap = [], 0.
        for s, y, yp in zip(x, Y, DY):
            fr = q.frame(float(s), y)
            local = q.project(fr["V"])
            gap = max(gap, float(np.max(abs(local-yp))))
            state = q.project(q.frame(float(s), y.astype(complex)+1j*1e-25*yp,
                                      strict=False)["V"]).imag/1e-25
            da = -fr["app"]/(fr["a"]*fr["kap"])+fr["ap"]**2/(fr["a"]**2*fr["kap"])
            db = -fr["al"]*da/fr["be"]
            DDY.append(state+q.project(da[:, None]*fr["N"]+db[:, None]*fr["B"]))
        self.quintic = PhysicalQuintic(x, Y, DY, np.asarray(DDY))
        self.sol = SimpleNamespace(x=x, y=Y.T, p=np.empty(0), sol=self.quintic)
        self.flow = SimpleNamespace(end=float(x[-1]), breaks=np.asarray(self.profile_model.knots, float),
                                    profile=self.profile, bridge=SimpleNamespace(sigma=-1.))
        self.kind = "complete-full-state-material-quintic"
        self.rotation_to_native = np.eye(2)
        self.translation_from_native = np.zeros(2)
        self.registration = None
        self.mode_identity = identity
        self.frozen_nine450_binding = source_binding
        scalar = profile.specification
        self.definition = dict(
            schema=SCHEMA, input_sha256=sha(self.path), source_sha256=sha(__file__),
            original_complete_state_jet_kernel_sha256=SOURCE_PINS["geometry_20261114_large_core_saved_prefix.py"],
            original_material_quintic_source_sha256=SOURCE_PINS["geometry_20261114_material_quintic_readout.py"],
            scalar_profile_source_sha256=SOURCE_PINS[PROFILE_NAME],
            independent_modes_scalar_profile_sha256=SOURCE_PINS[PROFILE_NAME],
            independent_modes_saved_prefix_sha256=sha(__file__),
            actual_accepted_field_producer_sha256=SOURCE_PINS[ENTRY_NAME],
            independent_field_modes=identity, frozen_nine450_binding=source_binding,
            state_layout="r[0:M+1],t[1:M+1],z[0:M+1]; all physical, n=3M+2",
            includes_entire_z0=True, old_mean_added=False,
            polynomial="Unique physical quintic through saved y, saved RHS, original finite-ODE second jet",
            node_saved_vs_local_RHS_max=gap,
            node_RHS_gap_is_readout_not_new_acceptance_gate=True,
            global_rho_lower_exact=str(self.rho_lower_exact),
            material_circle_diffeomorphism_proof="R237 complete-core rational triangle bound relative to the independently recomputed R236 core",
            frozen_scalar_parameters=copy.deepcopy(scalar["frozen_design_parameters"]),
            parameter_order=PARAMETER_ORDER,
            canonical_scalar_identity_sha256=profile.canonical_scalar_identity_sha256,
            complete_scalar_specification_sha256=canonical_sha(scalar),
            finite_scalar_assembly=copy.deepcopy(scalar["finite_assembly"]),
            point_evaluation="Frozen v2 profile -> original00e4 ThreeActiveView.profile; all nine coefficients retained",
            saved_RHS_evaluation="The actual450 saved batch RHS words, not a re-evaluated point-path replacement",
            finite_ODE_second_jet_evaluation="Original complete FullCoreProbe frame/project and point-profile path",
            canonical_material_metric="ds^2+a(s; all nine final coefficients)^2 dtheta_material^2",
            original_law_source="actual450.original_source_metric_identity.law",
            old_accepted96_g_claimed_as_current_g=False,
            physical_field_source="Actually accepted v2 all-nine-frozen450 complete full-DN output",
            material_jet_definition="Inherited complete-state nine_jets, full z0 mean and one recorded global SE(2)",
            nonlinear_solution_created=False, exact_isometry_certified=False,
            continuous_scalar_domain_or_C2_certificate_created=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("Use a fresh temporary readout path")
    saved = NineControlSameMetricSavedPrefix(args.checkpoint)
    result = dict(**saved.definition, M=saved.M, N=saved.N, n=saved.n,
        end=saved.flow.end, nodes=len(saved.sol.x),
        physical_cut_scalar_jet=list(saved.profile(saved.flow.end)),
        cut_material_mean_012=[float(value[0]) for value in saved.mean_jets([saved.flow.end])],
        closed_surface=False, task_completed=False)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("x") as handle:
        json.dump(result, handle, indent=2, allow_nan=False)
        handle.write("\n")


if __name__ == "__main__":
    main()
