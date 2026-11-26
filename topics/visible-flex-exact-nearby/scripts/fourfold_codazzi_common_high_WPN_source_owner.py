"""One actual4 target: true common-high operator unit ball -> original WPN RHS.

Whole completed WOBSA/D and the exact six original small inputs are admitted
before numerical imports.  This is an actual source operator bound, not a
fictitious particular vector and not a successful future physical inverse.
"""
from __future__ import annotations
import argparse, copy, hashlib, importlib.util, json, os, platform, sys, time, traceback
from fractions import Fraction
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
KIND = "complete_actual_common_high_WPN_source_stage_v1"
MANIFEST_KIND = "actual_common_high_WPN_source_inputs_v1"
STAGE = "common_high_WPN_source"
SOURCE_PATH = TOPIC+"/scripts/fourfold_codazzi_common_high_WPN_source_owner.py"
WORKER_PATH = TOPIC+"/scripts/fourfold_codazzi_common_high_WPN_source_public_worker.py"
GENERATOR_PATH = TOPIC+"/scripts/make_common_high_WPN_source_manifest.py"
PARAMETERS = {
    "arithmetic_bits": 320, "decimal_record_digits": 70,
    "maximum_scientific_wall_seconds": 900, "old_completed_target_calls": 0,
    "ordinary_radial_measure": "dr", "normalized_angular_measure": True,
    "source_input": "original_Xfr_Hminus4over3_operator_unit_ball",
    "source_pair": "(V0 Phi x,-(V0_R Phi-B_R^H Upsilon)x)",
    "exact_true_root_interval": ["1191984371497/5000000000000", "2383968743003/10000000000000"],
    "exact_outer_endpoint": "25/8", "original_parent_count": 153,
    "original_uniform_refinement": 160, "original_WPN_projection_cells": 24480,
    "fixed_intrinsic_parameter": "eta_0", "original_common_input_Ni_applied_again": False,
    "generic_Smax_descriptor_used": False, "old_geometry_target_recomputed": False,
    "particular_input_vector_invented": False,
    "positive_inverse_or_actual_224_32_used": False,
}
TARGETS = [
    "actual_source_weighted_body_rhs_upper",
    "actual_source_raw_endpoint193_rhs_upper",
    "actual_source_complete_WPN_pair_rhs_upper",
    "actual_source_original_radial_tail_rhs_upper",
]
SCI_FIELDS = sorted([
    "identity", "complete", "proved", "actual_returncode", "failure", "stage",
    "completed_targets", "current_target", "new_records", "saved_record_count",
    "parameters", "result", "whole_completed_inputs", "reference_identity",
    "selected_member_identity", "source_packet", "copied_prior_scalar_records",
    "old_scientific_target_calls", "new_arrays_published", "new_artifacts",
    "new_Releases", "wall_seconds", "runtime",
])
ORIGINAL_ROLES = ["negative", "PC", "WSP", "WHVA", "NIF", "WMR"]
WOBSA_GRAPHS = [
    "complete_outer_low_and_affine_rows", "complete_positive_head_and_outer_columns",
    "complete_genuine_288_shell", "complete_genuine_and_rough_observations",
    "complete_zero_IVP_rows", "complete_zero_stable_root_receiver_rows",
]
CENTRE = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION = "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"

FIXED_INPUTS = {
    "WOBSA_actual": {
        "role": "WOBSA_actual",
        "path": "topics/visible-flex-exact-nearby/notes/outer_rows_and_rough_positive_observations_ci/run-43844596176-1/actual-scientific-conclusion.json",
        "bytes": 60416,
        "sha256": "ba8e647cc4572333407b8979f98315e94dbab53ff2ff0086fe1d1dcdb0f17b79",
        "git_blob_sha": "b21c6d0717bccd6827eff4792bb12b8b1cd40d05"
    },
    "WOBSA_execution": {
        "role": "WOBSA_execution",
        "path": "topics/visible-flex-exact-nearby/notes/outer_rows_and_rough_positive_observations_ci/run-43844596176-1/execution.json",
        "bytes": 15866,
        "sha256": "b9022fe012e2e0f5db8186dda91a5ec1f2eb3222eb7af4ea02a9dd5ec41fdb57",
        "git_blob_sha": "4010d981fea326115f7888d7afeb9598066e177c"
    },
    "WOBSA_manifest": {
        "role": "WOBSA_manifest",
        "path": "topics/visible-flex-exact-nearby/notes/2026-11-16-R133-outer-rows-and-rough-positive-observations-current-inputs.json",
        "bytes": 15515,
        "sha256": "390a39928b257267c744b890ebfd5e3889c037f613398c1e39499d53864fe5ff",
        "git_blob_sha": "4958b39b7e0eb693b24e040e38180ce050d16653"
    },
    "D_actual": {
        "role": "D_actual",
        "path": "topics/visible-flex-exact-nearby/notes/reference_boundary_lifts_ci/run-44745017016-1/actual-scientific-conclusion.json",
        "bytes": 55295,
        "sha256": "087ebd3a222c6ef7be8b3ad2e427e272b2bb3f5b611c5acdcef4e03dd1fd2fdd",
        "git_blob_sha": "33b5c5b1f1cb9cb1b5012f651bc54698fa9a66fb"
    },
    "D_execution": {
        "role": "D_execution",
        "path": "topics/visible-flex-exact-nearby/notes/reference_boundary_lifts_ci/run-44745017016-1/execution.json",
        "bytes": 58602,
        "sha256": "827fb78a31aceb6313cff5abd1ec1431dede6af06df959b2d43d83b48197e8b6",
        "git_blob_sha": "615bb36d3b7cc1fcbce44b217a7bd1f622742e54"
    },
    "D_manifest": {
        "role": "D_manifest",
        "path": "topics/visible-flex-exact-nearby/notes/2026-11-20-reference-boundary-lifts-thread-recovery-inputs.json",
        "bytes": 72957,
        "sha256": "38ff0e8f5f3ca03a752a5836ec43baa72a31aefcf29a2d3e4421d0d399323f6d",
        "git_blob_sha": "dab54d23b551dd87ec187b665120e5303b1bd0b6"
    },
    "WVC_actual": {
        "bytes": 78627,
        "git_blob_sha": "746ec1e16befe8914c64521ad087c1f1dd23ab73",
        "path": "topics/visible-flex-exact-nearby/notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/actual-scientific-conclusion.json",
        "role": "WVC_actual",
        "sha256": "85fd5bc63c7cb558ef04ff9699f1f9be81dbd7e7b9638a2e0922818dc559cb88"
    },
    "reviewed_rules": {
        "role": "reviewed_rules",
        "path": "topics/visible-flex-exact-nearby/notes/2026-11-20-reviewed-public-CI-rules.json",
        "bytes": 2112,
        "sha256": "26da0165d2a7ec5f968959332c9fd04aae7259059de2b56f41e76b49b61fc051",
        "git_blob_sha": "71787717a9a58933f311091d20261a61a7581252"
    },
    "original_negative": {
        "bytes": 41797,
        "git_blob_sha": "3abd0f6b7291e0f9318dc035a58a4b6e8dfb851c",
        "path": "topics/visible-flex-exact-nearby/notes/full_delta_negative_one_positive_ci/run-43627228225-1-full-real-delta-negative-one-positive-graph/evidence/full-real-delta-negative-one-positive-graph-summary.json",
        "role": "original_negative",
        "sha256": "0a3fb8e1be19b9ad82655099da8d5446ac49d92f073e7f6626d08a0626ec4fef"
    },
    "original_PC": {
        "bytes": 46253,
        "git_blob_sha": "c32b8e3f3aca08d338784504c2cce5054d203bc6",
        "path": "topics/visible-flex-exact-nearby/notes/genuine_positive_Ai_cutoff_strong_correction_ci/run-43740173506-1/execution.json",
        "role": "original_PC",
        "sha256": "75f780f60446bd2a47fe286e72ca24fad929e3486c12d9ecbea42f42b9b1a817"
    },
    "original_WSP": {
        "bytes": 70207,
        "git_blob_sha": "421bf05d3274c6f9852670678275cf9e1a0fb1ee",
        "path": "topics/visible-flex-exact-nearby/notes/positive_cutoff_Schur_Parseval_ci/run-43816689251-1/actual-scientific-conclusion.json",
        "role": "original_WSP",
        "sha256": "5b099f08c18a2b437cb4b78e4a629fae5dc2411a720fd12ad39cf401401d72f2"
    },
    "original_WHVA": {
        "bytes": 12011,
        "git_blob_sha": "ebe7ae42c2482ce9b20e7af1d41e02f89b920010",
        "path": "topics/visible-flex-exact-nearby/notes/zero_volterra_positive_head_ci/run-43838214094-1/actual-scientific-conclusion.json",
        "role": "original_WHVA",
        "sha256": "ff5d6e5231e6be66107217d670133b18727dd5b24b81e7566fa884973b29df72"
    },
    "original_NIF": {
        "bytes": 29829,
        "git_blob_sha": "7142de95e64d5b3c6df7af705c8b0bf08a5c5c5e",
        "path": "topics/visible-flex-exact-nearby/notes/frozen_common_input_uniform_inverse_constants_ci/run-43795909913-1/actual-scientific-conclusion.json",
        "role": "original_NIF",
        "sha256": "43294b0cd0fdcffea58a805ecfb3cf06d60136d5ffbb3c8269b3040ce5ea9883"
    },
    "original_WMR": {
        "bytes": 51030,
        "git_blob_sha": "5fdb01ed62008489bca34a4b6231519af4f60793",
        "path": "topics/visible-flex-exact-nearby/notes/positive_weight_physical_mean_refinement_ci/run-43840219992-1/actual-scientific-conclusion.json",
        "role": "original_WMR",
        "sha256": "39a2d96accdbe1b4a8073674cabeda97878876f11fc24a055b910ed61567b432"
    }
}
FIXED_REFERENCE_IDENTITY = {
    "all_original_parent_definitions_verified": True,
    "complete_original_WVC_file": {
        "bytes": 78627,
        "git_blob_sha": "746ec1e16befe8914c64521ad087c1f1dd23ab73",
        "path": "topics/visible-flex-exact-nearby/notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/actual-scientific-conclusion.json",
        "role": "WVC_actual",
        "sha256": "85fd5bc63c7cb558ef04ff9699f1f9be81dbd7e7b9638a2e0922818dc559cb88"
    },
    "fine_cell_count": 24480,
    "fine_refinement": 160,
    "finite_normalizer_rule": "rho2=1+h^2*(a^2+c^2*q^2)/12",
    "kind": "complete_fixed_WVC_signed_reference_identity_v1",
    "no_completed_bound_target_recomputed": True,
    "original_reference_chain": {
        "count": 153,
        "sha256": "6fd1cc7b7bc2fb449804263962199175763e3c2d7e4816dfa46778a4d26108ac"
    },
    "reference_outer_impedance": "13/80",
    "same_original_D_S_and_true_root": True,
    "scalar_trace_identically_zero": True,
    "selected_diagonal_chain": {
        "count": 153,
        "sha256": "b19d7e319a9ea4e49909e12b1dfe71ddc23adf5a273708288b3fe6b0cc3af8d2"
    }
}

def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                       allow_nan=False)+"\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def atomic(path, raw):
    temporary = path.with_name(path.name+".partial")
    with temporary.open("wb") as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    os.replace(temporary, path)
    require(path.read_bytes() == raw, "whole exact scalar prefix byte readback")


def admit_complete_inputs(contents, specs):
    """Only full bytes, JSON metadata and rational interval identities.

    Called by the metadata generator too.  No old or new numerical module
    is imported, and no old norm, mesh maximum or scientific target runs.
    """
    require(set(contents) == set(specs), "whole current input map")
    for role, expected in FIXED_INPUTS.items():
        require(specs.get(role) == expected, "same complete fixed input: "+role)
    for role, spec in specs.items():
        raw = contents[role]
        require(0 < len(raw) < 100000 and len(raw) == spec["bytes"]
                and sha(raw) == spec["sha256"] and blob(raw) == spec["git_blob_sha"],
                "whole small current input identity: "+role)
        raw.decode("utf-8")

    def data(role):
        return parse(contents[role])

    def completed_pair(prefix, run, kind, gate_count):
        actual, execution, manifest = (data(prefix+"_"+suffix)
                                      for suffix in ("actual", "execution", "manifest"))
        ar, mr = specs[prefix+"_actual"], specs[prefix+"_manifest"]
        require(actual["kind"] == kind and actual["complete"] is True
                and actual["proved"] is True and actual["failure"] is None
                and actual["actual_returncode"] == 0
                and actual["run_id"] == execution["run_id"] == run
                and actual["run_attempt"] == execution["run_attempt"] == "1"
                and execution["scientific_complete"] is True
                and execution["original_scientific_complete_flag"] is True
                and execution["actual_child_returncode"] == 0 and execution["failure"] is None
                and actual["manifest_sha256"] == execution["manifest_sha256"] == mr["sha256"]
                and execution["current_input_receipts"] == manifest["files"]
                and len(actual["gates"]) == gate_count
                and all(g["passed"] is True for g in actual["gates"]),
                "whole completed science/execution/manifest and all gates: "+prefix)
        receipt = [v for v in execution["scientific_files"] if v["path"] == ar["path"]]
        require(receipt == [{key: ar[key] for key in ("path", "bytes", "sha256")}]
                and execution["completed_old_targets_recomputed"] == 0
                and execution["new_arrays_published"] == 0
                and execution["new_artifacts"] == 0 and execution["new_Releases"] == 0,
                "actual complete publication and no old replay: "+prefix)
        return actual, execution, manifest

    wob, we, wm = completed_pair("WOBSA", "43844596176",
        "complete_outer_rows_and_rough_positive_observation_bounds_v1", 18)
    d, de, dm = completed_pair("D", "44745017016",
        "complete_fixed_WVC_reference_boundary_lifts_v1", 25)
    require(wob["stage"] == "complete" and wob["current_target"] is None
            and wob["parameters"] == wm["parameters"]
            and wob["completed_targets"] == WOBSA_GRAPHS
            and set(wob["complete_new_graphs"]) == set(WOBSA_GRAPHS)
            and sum(len(v["complete_new_records"]) for v in wob["complete_new_graphs"].values()) == 37
            and len(wob["copied_original_scalar_records"]) == 42
            and wob["scientific_modules"] == {
                item["role"]: item["sha256"] for item in wm["scientific_modules"]},
            "entire original WOBSA source, six graphs and all37/42 records")
    for flag in (
            "same_selected_member_same_physical_eta0",
            "Ni_and_stable_inverse_in_original_right_order_once",
            "full_low193_rows_and_independent_even_mean_retained",
            "all_six_complete_original_receipts_read_without_old_math",
            "full_source_jump_root_mean_and_cokernel_rows_retained",
            "independent_physical_coordinates_receive_no_Ni",
            "WSP_complete_RH_source_not_received_positive_bound",
            "original_WHVA_4096_strict_sufficient_test_false",
            "original_WHVA_no_resolvent_admitted",
            "old_whole_bounds_not_subtracted"):
        require(wob["retained_scope"][flag] is True, "old complete WOBSA scope: "+flag)
    require(wob["actual_progress"]["old_scientific_calls"] == 0
            and wob["actual_progress"]["old_targets_recomputed"] == 0
            and wob["retained_scope"]["full_incoming_inverse_proved"] is False
            and wob["retained_scope"]["finite_signed_inverse_proved"] is False,
            "unchanged old scientific and unpaid inverse scopes")
    originals = {}
    prior_pins = {item["role"]: item for item in wm["files"]}
    accepted = wob["accepted_old_inputs"]["originals"]
    require(set(accepted) == set(ORIGINAL_ROLES)
            and set(wob["copied_original_scopes"]) == set(ORIGINAL_ROLES),
            "all six complete original small-source qualification objects")
    for role in ORIGINAL_ROLES:
        spec = specs["original_"+role]
        expected = dict(prior_pins[role]); expected["role"] = "original_"+role
        require(spec == expected
                and wob["verified_original_inputs"][role]
                    == {key: spec[key] for key in ("bytes", "sha256")}
                and wob["input_sha256"][role] == spec["sha256"],
                "same full original WOBSA input: "+role)
        admitted = accepted[role]
        require(admitted["identity"] == {
                    "file": spec["path"], "bytes": spec["bytes"],
                    "sha256": spec["sha256"], "git_blob": spec["git_blob_sha"]}
                and admitted["complete"] is True and admitted["failure"] is None
                and admitted["all_complete_gates_passed"] is True,
                "whole accepted old receipt: "+role)
        original = data("original_"+role)
        actual = original
        for key in admitted["science_object_path"]:
            actual = actual[key]
        require(actual["kind"] == admitted["kind"] and actual["complete"] is True
                and actual.get("failure") is None
                and len(actual["gates"]) == admitted["complete_gate_count"]
                and all(g["passed"] is True for g in actual["gates"]),
                "every gate in the entire original scientific input: "+role)
        if "actual_returncode" in actual:
            require(actual["actual_returncode"] == 0, "old child returned zero: "+role)
        if "source_sha256" in actual:
            require(actual["source_sha256"] == admitted["source_identity"],
                    "original source identity: "+role)
        else:
            require(actual["scientific_modules"] == admitted["source_identity"],
                    "entire original source module identity: "+role)
        if admitted["manifest_sha256"] is not None:
            value = actual.get("manifest_sha256", actual.get("input_manifest_sha256"))
            require(value == admitted["manifest_sha256"], "original input manifest identity: "+role)
        if role == "PC":
            require(original["complete"] is True and original["actual_returncode"] == 0
                    and original["actual_failure"] is None
                    and original["run_id"] == actual["run_id"] == "43740173506",
                    "complete PC execution and its full embedded scientific conclusion")
        originals[role] = actual

    negative, nif, whva = (originals[key] for key in ("negative", "NIF", "WHVA"))
    require(negative["derived_definition_sha256"] == CENTRE
            and negative["explicit_direction_definition_sha256"] == DIRECTION
            and negative["exact_real_delta_radius"] == "1/100000000"
            and negative["given_complete_head_positive_high_inverse_and_root_graph_proved"] is True
            and negative["complete_negative_order_physical_outer_graph_proved"] is True
            and negative["independent_even_mean_and_all_head_and_affine_source_ports_retained"] is True,
            "complete same physical family including the true exterior mean")
    ni = nif["complete_operator_identity_conclusion"]
    require(ni == wob["copied_original_scopes"]["NIF"]["complete_operator_identity_conclusion"]
            and nif["parameters"] == wob["copied_original_scopes"]["NIF"]["parameters"]
            and nif["retained_scope"] == wob["copied_original_scopes"]["NIF"]["retained_scope"]
            and ni["frozen_input_space"] ==
                "X_s_fr = S_star D_plus H_nat^s = (Ni_delta_star)^-1 H_nat^s"
            and ni["frozen_norm"] == "inherited physical H^s norm"
            and ni["natural_and_ambient_projectors_not_identified"] is True
            and ni["selected_KAM_conjugacy_only_at_original_delta_star"] is True
            and ni["physical_mean_coordinates"] == 2
            and nif["parameters"]["fixed_intrinsic_parameter"] == "eta_0"
            and nif["parameters"]["exact_root_interval"] == PARAMETERS["exact_true_root_interval"]
            and nif["retained_scope"]["selected_H_and_S_are_frozen_once_not_extended_as_KAM_family"] is True,
            "the entire actual reflected frozen common domain, selected member and both means")
    require(whva["new_records"]["C_R0"] == wob["copied_original_scalar_records"]["C_R0"]
            and whva["strict_mesh_gate"]["passed"] is False
            and whva["resolvent_admitted"] is False,
            "literal old true-length record; no failed WHVA inverse is admitted")

    require(d["reference_identity"] == FIXED_REFERENCE_IDENTITY
            and d["complete_current_file_receipts"] == dm["files"]
            and d["parameters"] == dm["parameters"]
            and d["parameters"]["parent_cells"] == 153
            and d["parameters"]["uniform_refinement"] == 160
            and d["parameters"]["refined_cells"] == 24480
            and d["parameters"]["true_root_is_not_an_enclosure_endpoint"] is True
            and d["saved_record_count"] == 10
            and d["completed_targets"] == ["complete_D_weighted_right97_boundary_lift",
                                            "complete_D_joint193_boundary_lift"]
            and d["actual_progress"]["old_completed_targets_recomputed"] == 0
            and d["actual_progress"]["old_producer_entrypoints_called"] == 0,
            "whole exact D/S/true-root and its two complete10-record targets")
    for flag in ("complete_reference_weighted_right97_lift_proved",
                 "complete_reference_joint193_boundary_lift_proved",
                 "true_reference_independent_mean_retained",
                 "complete_body_root97_outer96_and_atoms193_retained",
                 "same_original_D_S_and_true_root"):
        require(d["boundary_lift"][flag] is True, "the actual reference mean subcolumn: "+flag)
    require(d["boundary_lift"]["actual_low_boundary_lift_proved"] is False
            and d["boundary_lift"]["actual_physical_outer_rows_proved"] is False,
            "reference D is not a successful actual positive inverse")
    v = data("WVC_actual")
    require(v["complete"] is True and v["proved"] is True and v["actual_returncode"] == 0
            and v["failure"] is None and v["run_id"] == "43891414339"
            and v["run_attempt"] == "1"
            and v["reference_chain"] == FIXED_REFERENCE_IDENTITY["original_reference_chain"]
            and v["reference_selection"]["selected_diagonal_chain"]
                == FIXED_REFERENCE_IDENTITY["selected_diagonal_chain"]
            and v["parameters"]["reference_q_floor"] == "1/8"
            and v["parameters"]["parent_cells"] == 153
            and v["parameters"]["uniform_refinement"] == 160
            and v["parameters"]["refined_cells"] == 24480
            and v["retained_scope"]["actual_S_P_Q_A_B_C_R_and_high_space_unchanged"] is True,
            "original exact positive S and the actual153-by160 projection")
    oldmesh = v["copied_original_scope"]["WPTVS_mesh_summary"]
    require(oldmesh["root"] == PARAMETERS["exact_true_root_interval"]
            and oldmesh["right"] == PARAMETERS["exact_outer_endpoint"]
            and oldmesh["parent_cells"] == 153
            and oldmesh["homogeneous_raw_transmission_is_identity"] is True,
            "true original mesh endpoints and homogeneous raw traces")
    lo, hi = map(Fraction, PARAMETERS["exact_true_root_interval"])
    require(0 < lo <= hi < Fraction(PARAMETERS["exact_outer_endpoint"]),
            "strict ordered actual interval, never a midpoint replacement")
    selected = {
        "kind": "same_original_selected_frozen_member_v1",
        "whole_NIF_actual": copy.deepcopy(specs["original_NIF"]),
        "continuous_centre_definition_sha256": CENTRE,
        "continuous_direction_definition_sha256": DIRECTION,
        "physical_eta0": nif["parameters"]["exact_intrinsic_parameter"],
        "absolute_delta_upper": nif["parameters"]["fixed_selected_parameter_absolute_upper"],
        "same_actual_H_and_S_frozen_once": True,
        "selected_parameter_replaced_by_numeric_point": False,
    }
    return {"wobsa": wob, "reference": d, "selected_member_identity": selected,
            "reference_identity": d["reference_identity"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--manifest-sha", required=True)
    parser.add_argument("--input-map", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--checkout", required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1",
            "one new source target in the public own Actions only")
    raw_manifest = args.manifest.read_bytes()
    require(sha(raw_manifest) == args.manifest_sha, "whole new manifest bytes")
    manifest = parse(raw_manifest)
    require(manifest["kind"] == MANIFEST_KIND and manifest["scientific_kind"] == KIND
            and manifest["stage"] == STAGE and manifest["parameters"] == PARAMETERS
            and manifest["target_order"] == TARGETS
            and manifest["complete_record_counts"] == [4]
            and manifest["allowed_scientific_fields"] == SCI_FIELDS,
            "one precise complete common-high four-source target")
    specs = {spec["role"]: spec for spec in manifest["files"]}
    require(len(specs) == len(manifest["files"])
            and specs["science"]["path"] == SOURCE_PATH
            and specs["worker"]["path"] == WORKER_PATH
            and specs["metadata_generator"]["path"] == GENERATOR_PATH,
            "unique whole new source module identities")
    paths = parse(args.input_map.read_bytes())
    contents = {role: Path(path).read_bytes() for role, path in paths.items()}
    require(sha(Path(__file__).read_bytes()) == specs["science"]["sha256"],
            "this executing owner is pinned")
    prior = admit_complete_inputs(contents, specs)
    require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
            "entire old inputs admitted before numerical libraries")
    require(not args.output.exists(), "no overwrite of a prior scientific prefix")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    wob, d = prior["wobsa"], prior["reference"]
    copied = {
        "Phi": copy.deepcopy(wob["complete_new_graphs"]["complete_genuine_and_rough_observations"][
            "complete_new_records"]["complete_Phi_upper"]),
        "B0": copy.deepcopy(wob["complete_new_graphs"]["complete_zero_IVP_rows"][
            "complete_new_records"]["complete_B0_high_body_row_upper"]),
        "D0": copy.deepcopy(wob["complete_new_graphs"]["complete_zero_IVP_rows"][
            "complete_new_records"]["complete_D0_high_endpoint_row_upper"]),
        "t0": copy.deepcopy(wob["copied_original_scalar_records"]["C_R0"]),
        "d_B": copy.deepcopy(d["new_records"]["reference_weighted_right97_body_upper"]),
    }
    document = {
        "identity": {"kind": KIND, "scalar_stage": STAGE,
            "source_sha256": specs["science"]["sha256"], "manifest_sha256": args.manifest_sha,
            "run_id": os.environ["GITHUB_RUN_ID"], "run_attempt": "1",
            "event_commit": os.environ["GITHUB_SHA"], "actual_checkout_commit": args.checkout,
            "arithmetic_bits": PARAMETERS["arithmetic_bits"]},
        "complete": False, "proved": False, "actual_returncode": None, "failure": None,
        "stage": "whole_old_inputs_admitted", "completed_targets": [], "current_target": None,
        "new_records": {}, "saved_record_count": 0, "parameters": copy.deepcopy(PARAMETERS),
        "result": None, "source_packet": None,
        "whole_completed_inputs": {role: {"file": copy.deepcopy(spec), "json_path": []}
                                  for role, spec in specs.items() if not spec["path"].endswith(".py")},
        "reference_identity": copy.deepcopy(prior["reference_identity"]),
        "selected_member_identity": copy.deepcopy(prior["selected_member_identity"]),
        "copied_prior_scalar_records": copied,
        "old_scientific_target_calls": 0, "new_arrays_published": 0, "new_artifacts": 0,
        "new_Releases": 0, "wall_seconds": 0.0, "runtime": {},
    }
    require(sorted(document) == SCI_FIELDS, "exact complete new scientific schema")
    began = time.perf_counter()

    def bounded_bytes(value):
        value["wall_seconds"] = time.perf_counter()-began
        require(value["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                "bounded new scalar execution")
        raw = canonical(value)
        require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"],
                "whole small result budget")
        return raw

    def save():
        atomic(args.output, bounded_bytes(document))

    def load(role):
        spec = importlib.util.spec_from_file_location("_common_high_source_"+role, paths[role])
        require(spec is not None and spec.loader is not None, "explicit pure source")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    save()
    try:
        import flint
        from importlib.metadata import version
        runtime = {"python": platform.python_version(), "packages": {"python-flint": version("python-flint")}}
        require(runtime == manifest["runtime"], "fixed actual directed runtime")
        document["runtime"] = runtime
        flint.ctx.prec = PARAMETERS["arithmetic_bits"]

        class API:
            def __init__(self):
                self.arb = flint.arb; self.zero = self.arb(0); self.one = self.arb(1)
            def rational(self, n, d=1):
                require(type(n) is int and type(d) is int and d > 0, "exact rational")
                return self.arb(n)/self.arb(d)
            def lower(self, value):
                require(value.is_finite(), "finite lower"); return value.lower()
            def sqrt(self, value):
                require(value.is_finite() and value.lower() >= 0, "nonnegative root")
                return value.sqrt()
            def pi(self):
                return self.arb.pi()
            def interval(self, a, b):
                require(a.is_finite() and b.is_finite() and a.lower() <= b.upper(), "whole interval")
                return a.lower().union(b.upper())
            def old_interval(self, record):
                if isinstance(record, dict) and "lower" in record and "upper" in record:
                    return self.interval(self.arb(record["lower"]).lower(), self.arb(record["upper"]).upper())
                value = self.arb(record["ball"] if isinstance(record, dict) else record)
                require(value.is_finite(), "whole old scalar")
                return value

        api = API()
        core, source_interface, math = (load(role) for role in ("scalar_core", "source_interface", "common_math"))
        require(list(math.NEW_RECORD_ORDER) == TARGETS, "same exact four outputs")
        evidence = specs["proof"]["path"]+"@"+specs["proof"]["sha256"]
        packet = math.common_unit_ball_packet(source_interface, prior["selected_member_identity"], evidence)
        document["source_packet"] = packet
        document["stage"] = "complete_common_unit_ball_source_identity"
        save()
        admitted = {
            "private_token": object(),
            "selected_member_identity": prior["selected_member_identity"],
            "reference_identity": prior["reference_identity"],
            "whole_CX_proof_evidence_id": evidence,
            "whole_WOBSA_actual_execution_manifest_and_six_originals_verified": True,
            "all_WOBSA_same_selected_common_scopes_and_records_verified": True,
            "whole_D_actual_execution_manifest_and_reference_identity_verified": True,
            "same_original_S_mean_column_and_true_mesh_definition_verified": True,
            "same_selected_NIF_reflected_Hminus4over3_domain_verified": True,
            "complete_common_unit_ball_zero_identities_verified": True,
        }

        def emit(name, value, bound):
            require(bound == "upper" and name == TARGETS[document["saved_record_count"]]
                    and value.is_finite(), "ordered complete new upper")
            point = value.upper()
            require(point >= api.zero, "nonnegative directed source upper")
            record = {"ball": point.str(PARAMETERS["decimal_record_digits"]), "bound": "upper"}
            candidate = copy.deepcopy(document)
            candidate["new_records"][name] = record
            candidate["saved_record_count"] += 1
            candidate["completed_targets"].append(name)
            candidate["current_target"] = None
            candidate["stage"] = "complete_new_scalar_saved"
            raw = bounded_bytes(candidate)
            temporary = args.output.with_name(args.output.name+".candidate")
            atomic(temporary, raw)
            reread = parse(temporary.read_bytes())
            require(reread == candidate, "entire candidate document readback")
            ball = api.arb(reread["new_records"][name]["ball"])
            require(ball.is_finite() and ball.contains(point), "whole candidate contains original upper")
            atomic(args.output, raw)
            document.clear(); document.update(candidate)
            temporary.unlink()
            return ball.upper()

        result = math.complete_common_input_source_pair(
            api, core, source_interface, admitted, wob, d, packet, emit)
        require(document["completed_targets"] == TARGETS
                and document["saved_record_count"] == 4
                and result["complete_new_record_order"] == TARGETS
                and result["complete_actual_source_pair_upper_bounds_proved"] is True,
                "one complete four-record real common-source target")
        document["result"] = result
        document["complete"] = document["proved"] = True
        document["actual_returncode"] = 0
        document["stage"] = "complete_"+STAGE+"_scalar_branch"
        save()
        return 0
    except BaseException as error:
        document["complete"] = document["proved"] = False
        document["actual_returncode"] = 1
        document["stage"] = "failed_with_complete_scalar_prefix"
        document["failure"] = {"type": type(error).__name__, "message": str(error)[:1800],
                               "traceback": traceback.format_exc()[-7000:]}
        print(traceback.format_exc(), flush=True)
        document["wall_seconds"] = time.perf_counter()-began
        atomic(args.output, canonical(document))
        return 1


if __name__ == "__main__":
    sys.exit(main())
