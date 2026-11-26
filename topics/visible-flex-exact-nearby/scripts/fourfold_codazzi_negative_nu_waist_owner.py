"""R147 one new whole selected negative ordinary source-to-waist target.

This owner reads entire completed S0/D/SP/PW inputs and the exact selected
and complete-two-source proofs.  It computes four new scalar combinations,
without invoking any old producer, integral, Green map or inverse target.
R147 itself was an analytic transfer, not an invented earlier actual run.
"""
from __future__ import annotations
import argparse, ast, copy, hashlib, json, os, platform, sys, time, traceback
from fractions import Fraction
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
KIND = "R147_complete_selected_negative_nu_ordinary_to_waist_v1"
STAGE = "selected_negative_nu_ordinary"
MANIFEST_KIND = "R147_selected_negative_nu_ordinary_to_waist_inputs_v1"
SOURCE_PATH = TOPIC+"/scripts/fourfold_codazzi_negative_nu_waist_owner.py"
WORKER_PATH = TOPIC+"/scripts/fourfold_codazzi_negative_nu_waist_public_worker.py"
GENERATOR_PATH = TOPIC+"/scripts/make_negative_nu_waist_manifest.py"
PARAMETERS = {
    "arithmetic_bits": 320,
    "decimal_record_digits": 70,
    "maximum_scientific_wall_seconds": 300,
    "old_completed_target_calls": 0,
    "ordinary_radial_measure": "dr",
    "normalized_angular_measure": True,
    "source": "F_nu(Q_delta,nu_delta)-(partial_r-A_delta)Z",
    "source_norm": "ordinary_L2_dr_L2_phi_complete_moving_pair",
    "continuous_centre_definition_sha256": "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47",
    "continuous_direction_definition_sha256": "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04",
    "fixed_intrinsic_parameter": "eta_0",
    "exact_nu_centre": "-2572625729470897/72057594037927936",
    "exact_alpha": "6890507429876859/9007199254740992",
    "selected_member_run": "43588332723/1",
    "selected_member_loss": "1/250",
    "selected_parameter_absolute_upper": "9368259853002/100000000000000000000000",
    "delta_budget_radius": "1/10000000000",
    "selected_to_budget_ratio_upper": "936826/1000000",
    "exact_original_negative_window": ["0", "2383968743003/10000000000000"],
    "exact_root_interval": ["1191984371497/5000000000000", "2383968743003/10000000000000"],
    "exact_root_Cauchy_radius": "1/200",
    "exact_strict_interval": ["0", "2333968743003/10000000000000"],
    "negative_root_ordinary_extended_window": "L2_dr_Hminus2over3_first_Hminus1_second",
    "negative_root_second_source_is_required_constant": False,
    "complete_output": "original_waist_primitive_pair_and_both_physical_density_means",
    "positive_inverse_or_incoming_used": False
}
TARGETS = ["selected_negative_source_from_original_whole_body_upper", "selected_negative_source_from_same_fixed_window_upper", "complete_negative_ordinary_L2_to_waist_density_gain_upper", "selected_negative_nu_ordinary_to_waist_density_upper"]
SCI_FIELDS = ["actual_returncode", "candidate_record", "complete", "completed_targets", "copied_prior_scalar_records", "current_target", "failure", "identity", "new_Releases", "new_arrays_published", "new_artifacts", "new_records", "old_scientific_target_calls", "parameters", "proved", "reference_identity", "result", "runtime", "saved_record_count", "selected_member_identity", "stage", "wall_seconds", "whole_completed_inputs"]
FIXED_INPUTS = {
    "proof_SC": {
        "role": "proof_SC",
        "path": "topics/visible-flex-exact-nearby/results/R149-supplement-signed-finite-columns-and-full-negative-residual-sources.md",
        "bytes": 21533,
        "sha256": "059c4d0490ab5725aa01bcefa31446101d4464f151bc3801b1b8530aa1ef1ec0",
        "git_blob_sha": "01efc774c206583123cd838ee26b0e745e29af4c"
    },
    "proof_R147": {
        "role": "proof_R147",
        "path": "topics/visible-flex-exact-nearby/results/R147-selected-negative-nu-source-and-complete-mean-row.md",
        "bytes": 13979,
        "sha256": "7b1a1f3906b5d1dff6a1e3b8077adfba650aa8af2e588b1dfa6731e5fc116e66",
        "git_blob_sha": "93720d2f775fdf45e7920bbdfb1d1f76ec52c0f9"
    },
    "proof_D": {
        "role": "proof_D",
        "path": "topics/visible-flex-exact-nearby/results/R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md",
        "bytes": 15214,
        "sha256": "92fd222bbcc4495cce091cedee2628f83d014be23a40328a7292d47616621635",
        "git_blob_sha": "c85b66866103ea021cebbc050ccead214d4cf9d9"
    },
    "proof_NIF": {
        "role": "proof_NIF",
        "path": "topics/visible-flex-exact-nearby/results/R133-supplement-uniform-frozen-selected-input-coordinates-for-the-real-reference-family.md",
        "bytes": 32942,
        "sha256": "8f3784473b98f9b49449b7012e4c5c919670418246fa03a7f28441aaca28b640",
        "git_blob_sha": "d606faa1ffd30c34d3487985a57dbc62a18890bc"
    },
    "proof_W": {
        "role": "proof_W",
        "path": "topics/visible-flex-exact-nearby/results/R133-supplement-actual-physical-Wiener-conjugacy-strip.md",
        "bytes": 6138,
        "sha256": "1e8d001a5878da2894b4c9ab88baf00555ca8364b23f49df8c827c23a7da88c3",
        "git_blob_sha": "a79a7ad7c147076b044389e98a15ab2f341d0d0c"
    },
    "proof_E": {
        "role": "proof_E",
        "path": "topics/visible-flex-exact-nearby/results/R133-supplement-full-real-large-root-Cauchy-two-source-windows.md",
        "bytes": 11952,
        "sha256": "60ceb9c93e80984c67c2e9847e08815f83bc772f7bf2b8f397a57095617ef78b",
        "git_blob_sha": "948ee3ba2207d8770f98ff69ba3efb97bbd979d8"
    },
    "proof_N": {
        "role": "proof_N",
        "path": "topics/visible-flex-exact-nearby/results/R133-supplement-complete-negative-source-to-strict-density-cut-readout.md",
        "bytes": 13892,
        "sha256": "4d44bbe7082d4ee967ebf9d02284b3510624624ab98adb087b8d0499eb030376",
        "git_blob_sha": "da51581b623d4167ae9278af6892bc9a0591fb3f"
    },
    "proof_SP": {
        "role": "proof_SP",
        "path": "topics/visible-flex-exact-nearby/results/R133-supplement-complete-primitive-and-mean-strict-propagation-to-the-waist.md",
        "bytes": 20730,
        "sha256": "ae01c213b63ae618e4657b5966604e7fbec4acb4763ea4b8aae848e1a40a40b4",
        "git_blob_sha": "9fc2e2c565738b1a6d0fc5962703e01f43b483bf"
    },
    "proof_PW": {
        "role": "proof_PW",
        "path": "topics/visible-flex-exact-nearby/results/R133-supplement-seven-positive-ports-and-mixed-root-to-waist-density.md",
        "bytes": 16459,
        "sha256": "246c81ac387392c75a3267faaa934a7f0a4b978fdad8b8ac7cbbd4bd5c413562",
        "git_blob_sha": "d22fc84975785bfdf0e0ba91b100d53c9d4c32a3"
    },
    "proof": {
        "role": "proof",
        "path": "topics/visible-flex-exact-nearby/results/R147-supplement-same-window-selected-nu-source-to-complete-waist.md",
        "bytes": 6854,
        "sha256": "f122a8492662da32aafc7a64f7a5930782a298b9dda0d42b1b80caf7fe98fad5",
        "git_blob_sha": "63b688722028891ed5d8a6dcdca9cc39a74a30a8"
    },
    "S0_summary": {
        "role": "S0_summary",
        "path": "topics/visible-flex-exact-nearby/notes/complete_Z_source_v2_ci/run-43613560173-1-complete-Z-sources-finish/evidence/complete-Z-source-finish-summary.json",
        "bytes": 21085,
        "sha256": "e1ae6bd3ae8b9f04297fb2c9664d249c15ffe9366d15a4504444f06f08b727ac",
        "git_blob_sha": "79fb51921478ac1e8682601980b35dc1cb3cb904"
    },
    "S0_process": {
        "role": "S0_process",
        "path": "topics/visible-flex-exact-nearby/notes/complete_Z_source_v2_ci/run-43613560173-1-complete-Z-sources-finish/process.json",
        "bytes": 16343,
        "sha256": "0cc2e8f876261c0fa86c0547b1400d47ad71759f43c7001b6359049827017f48",
        "git_blob_sha": "df3beb2150d8eeb080a70198d22670472d41867f"
    },
    "S0_manifest": {
        "role": "S0_manifest",
        "path": "topics/visible-flex-exact-nearby/notes/2026-11-14-R133-complete-mixed-Z-source-cover-v2-CI-inputs.json",
        "bytes": 32588,
        "sha256": "05178f530e1fbc9be1016faa52cb9f5773e199915ab7bfcae1ad187609e7e0ac",
        "git_blob_sha": "fdfc5484c05221c1acb3de0c20deadba4b8a00eb"
    },
    "S0_contract": {
        "role": "S0_contract",
        "path": "topics/visible-flex-exact-nearby/notes/2026-11-14-R133-complete-mixed-Z-source-cover-contract.md",
        "bytes": 8736,
        "sha256": "3567bcd86a2ae190117c9e9acb22f588085ad4d144b5da5417fccb0d666a03c4",
        "git_blob_sha": "2e78310c5f10c2344989675b29b32142cce2e654"
    },
    "S0_source": {
        "role": "S0_source",
        "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_complete_mixed_Z_source_cover.py",
        "bytes": 26118,
        "sha256": "90c90fb1b21806e803e61d5f850b1d8057fcadc577452d3454b05348500a697f",
        "git_blob_sha": "c3c07b7b05488c2a389581ab6c07ff0642756af2"
    },
    "D_execution": {
        "role": "D_execution",
        "path": "topics/visible-flex-exact-nearby/notes/selected_parameter_core_scalar_fees_ci/run-43713242980-1/execution.json",
        "bytes": 40659,
        "sha256": "6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071",
        "git_blob_sha": "ce7af74c8b2f8cf7715775f352d2c26afb03413a"
    },
    "D_manifest": {
        "role": "D_manifest",
        "path": "topics/visible-flex-exact-nearby/notes/2026-11-15-R133-selected-parameter-core-scalar-fees-CI-inputs.json",
        "bytes": 23692,
        "sha256": "14271d7d61c70996092f105768ca29cc0dd355665be0becea4386441b38c907f",
        "git_blob_sha": "0ac3321a17279d73ac56711ebcf3906df921c66f"
    },
    "D_source": {
        "role": "D_source",
        "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_selected_parameter_core_scalar_fees.py",
        "bytes": 25571,
        "sha256": "827fcb237a79b48c095872b61c370ff2ceafc143a8dc6a1774021188ff3ea320",
        "git_blob_sha": "704b1e1d4aa74e97c866c725a2524c1b8624039e"
    },
    "SP_execution": {
        "role": "SP_execution",
        "path": "topics/visible-flex-exact-nearby/notes/primitive_mean_strict_propagation_ci/run-43731464771-1/execution.json",
        "bytes": 35259,
        "sha256": "a3a02969178e5e8b3b040fafd51d08b25d75b3f3922f2ae2e9ee0d4a8ab18a12",
        "git_blob_sha": "9998526894560d41523454334a444f062fe371a4"
    },
    "SP_manifest": {
        "role": "SP_manifest",
        "path": "topics/visible-flex-exact-nearby/notes/2026-11-15-R133-primitive-mean-strict-propagation-CI-inputs.json",
        "bytes": 21754,
        "sha256": "c77e969bd02ef95d30f16b53ae0a0d3854f596412151e9242ffa0485bd142210",
        "git_blob_sha": "92a5282f198dfa05ee8ce1e7b4aaec532485a324"
    },
    "SP_source": {
        "role": "SP_source",
        "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_primitive_mean_strict_propagation.py",
        "bytes": 44298,
        "sha256": "9d6ef721338e47e2cae8d179ce84976881df91762050d2a77d83b5399f6ba69a",
        "git_blob_sha": "f12d3a63f01d8b9bc20c329c67a6582b626eae1d"
    },
    "PW_execution": {
        "role": "PW_execution",
        "path": "topics/visible-flex-exact-nearby/notes/positive_ports_to_waist_density_ci/run-43734233535-1/execution.json",
        "bytes": 35295,
        "sha256": "f17516d3083cd2782866c2163635a3a89efe9479ced8f57eefb2bf63e3f92e90",
        "git_blob_sha": "06ace460f1060b1ef39e8d456d3f0f68aa7773e0"
    },
    "PW_manifest": {
        "role": "PW_manifest",
        "path": "topics/visible-flex-exact-nearby/notes/2026-11-15-R133-positive-ports-to-waist-density-CI-inputs.json",
        "bytes": 11522,
        "sha256": "8c3d9c450f571541295754b21667f02b964c26b3ceca918765b3d77b9ec07133",
        "git_blob_sha": "6ec4c65e1cf5d545fe9b33a913985ea46554d1af"
    },
    "PW_source": {
        "role": "PW_source",
        "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_positive_ports_to_waist_density.py",
        "bytes": 37395,
        "sha256": "268e033e3973ba60eb01b6b45842221f5d480cbe584de541731a4e34e5632e3c",
        "git_blob_sha": "036dd32b94d3d0705716ac146e371b27bfc1230b"
    },
    "reviewed_rules": {
        "role": "reviewed_rules",
        "path": "topics/visible-flex-exact-nearby/notes/2026-11-20-reviewed-public-CI-rules.json",
        "bytes": 2112,
        "sha256": "26da0165d2a7ec5f968959332c9fd04aae7259059de2b56f41e76b49b61fc051",
        "git_blob_sha": "71787717a9a58933f311091d20261a61a7581252"
    },
    "S0_pilot_source": {
        "role": "S0_pilot_source",
        "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_exact_bump_continuous_Z_source_pilot.py",
        "bytes": 31302,
        "sha256": "2d45c2f100484f5a25fe50ec2d8ea2dcd601b79f1f151d4be116225d3284fcc8",
        "git_blob_sha": "1fac6da3acf7116b5feef156adc845e072147e83"
    }
}
GAIN_KEYS = (
    "root_or_affine_jump_to_waist_density_gain",
    "ordinary_root_window_source_to_waist_density_gain",
    "strict_L1_Hminus1_source_to_waist_density_gain",
    "strict_L2_Hminus1_source_to_waist_density_gain",
)
S0_NATIVE = "365f0763d8f4c87182507c4372a3be055624607a77d818a084471b368b33d32e"
CENTRE = PARAMETERS["continuous_centre_definition_sha256"]
DIRECTION = PARAMETERS["continuous_direction_definition_sha256"]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode("utf-8")


def parse(raw):
    return json.loads(raw, parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def atomic(path, raw):
    tmp = path.with_name(path.name+".partial")
    with tmp.open("wb") as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    os.replace(tmp, path)
    require(path.read_bytes() == raw, "whole new scientific prefix byte readback")


def original_negative_window_endpoint(source_raw, pilot_raw):
    """Read exact original source-domain metadata, never import old science."""
    pilot_tree = ast.parse(pilot_raw.decode("utf-8"))
    definitions = [item.value for item in pilot_tree.body
                   if isinstance(item, ast.Assign)
                   and any(isinstance(target, ast.Name) and target.id == "PHASE_RIGHT"
                           for target in item.targets)]
    require(len(definitions) == 1, "one original pilot negative-window endpoint")
    value = definitions[0]
    require(isinstance(value, ast.Call) and isinstance(value.func, ast.Name)
            and value.func.id == "Fraction" and len(value.args) == 2
            and not value.keywords
            and all(isinstance(arg, ast.Constant) and type(arg.value) is int
                    for arg in value.args),
            "original pilot endpoint is an exact Fraction constant")
    endpoint = Fraction(value.args[0].value, value.args[1].value)
    source_tree = ast.parse(source_raw.decode("utf-8"))
    imports = [alias for node in source_tree.body if isinstance(node, ast.Import)
               for alias in node.names
               if alias.name == "fourfold_codazzi_exact_bump_continuous_Z_source_pilot"
               and alias.asname == "pilot"]
    uses = [node.value for node in ast.walk(source_tree)
            if isinstance(node, ast.keyword) and node.arg == "fixed_negative_phase_window"]
    require(len(imports) == 1 and len(uses) == 2
            and all(isinstance(call, ast.Call) and isinstance(call.func, ast.Name)
                    and call.func.id == "aggregate" and len(call.args) == 2
                    and not call.keywords
                    and isinstance(call.args[0], ast.Name) and call.args[0].id == "output"
                    and isinstance(call.args[1], ast.Attribute)
                    and call.args[1].attr == "PHASE_RIGHT"
                    and isinstance(call.args[1].value, ast.Name)
                    and call.args[1].value.id == "pilot" for call in uses),
            "both original source finish/summary branches aggregate this exact pilot endpoint")
    return endpoint


def admit_complete_inputs(contents, specs):
    """Metadata and exact-rational checks only; also used by the generator."""
    for role, expected in FIXED_INPUTS.items():
        require(specs.get(role) == expected, "same complete accepted input: "+role)
    require(set(contents) == set(specs), "complete input map, no hidden scalar input")
    for role, spec in specs.items():
        raw = contents[role]
        require(0 < len(raw) < 100000 and len(raw) == spec["bytes"]
                and sha(raw) == spec["sha256"] and blob(raw) == spec["git_blob_sha"],
                "whole current UTF8 input identity: "+role)
        raw.decode("utf-8")

    def data(role):
        return parse(contents[role])

    z, zp, zm = (data(role) for role in ("S0_summary", "S0_process", "S0_manifest"))
    require(z["kind"] == "complete7721_mixed_exact_bump_and_raw_mean_continuous_Z_source_cover_v1"
            and z["complete"] is True and z["failure"] is None
            and z["phase"] == zp["phase"] == "finish"
            and z["complete_valid_source_cover"] is zp["complete_valid_source_cover"] is True
            and z["selected_cells_complete"] is True
            and z["complete_rows"] == z["complete_original_common_cells"] == 7721
            and z["first_original_index"] == 0 and z["last_original_index"] == 7720
            and z["native_sha256"] == zp["complete_native_sha256"] == S0_NATIVE
            and len(z["gates"]) == zp["actual_scientific_gates"] == 6
            and all(g["passed"] is True for g in z["gates"])
            and zp["complete"] is True and zp["run_id"] == "43613560173"
            and str(zp["run_attempt"]) == "1" and len(zp["children"]) == 1
            and zp["children"][0]["actual_returncode"] == 0,
            "whole completed original7721 source, six gates and its actual finish process")
    found = [x for x in zp["native_files"]
             if x["file"] == "evidence/complete-Z-source-finish-summary.json"]
    require(len(found) == 1 and found[0]["bytes"] == specs["S0_summary"]["bytes"]
            and found[0]["sha256"] == specs["S0_summary"]["sha256"]
            and z["complete_source_bounds"] == zp["complete_source_bounds"],
            "execution binds the entire source summary and every original bound")
    require(zp["input_manifest_sha256"] == specs["S0_manifest"]["sha256"]
            and zm["kind"] == "complete_mixed_Z_source_public_inputs_v2"
            and zm["files"][specs["S0_source"]["path"]] == z["source_sha256"]
                == specs["S0_source"]["sha256"]
            and zm["files"][specs["S0_contract"]["path"]] == specs["S0_contract"]["sha256"]
            and zm["files"][specs["S0_pilot_source"]["path"]]
                == z["exact_bump_source_sha256"] == specs["S0_pilot_source"]["sha256"]
            and z["derived_continuous_centre_definition_sha256"]
                == zm["derived_continuous_centre_definition_sha256"] == CENTRE
            and z["exact_continuous_direction_definition_sha256"]
                == zm["complete_continuous_direction_definition_sha256"] == DIRECTION
            and z["whole_complete_source_interval"] == zm["exact_interval"] == ["0", "25/8"]
            and z["exact_affine_parameter_offset"] == zm["exact_affine_parameter_offset"] == "0"
            and zm["complete_low_projection_dimension"] == 193
            and zm["new_source_known_full_angular_support"] == 160,
            "complete source identity, exact original parameter, ordinary full pair and all mean slots")
    require(original_negative_window_endpoint(contents["S0_source"], contents["S0_pilot_source"])
                == Fraction(PARAMETERS["exact_original_negative_window"][1])
            and PARAMETERS["exact_original_negative_window"][0] == "0",
            "whole source actual fixed-negative aggregate uses the declared exact original window")
    require(z["true_independent_even_mean_retained"] is True
            and z["known_high_output_retained"] is True
            and z["unknown_high_input_feedback_still_required"] is True
            and z["actual_full_PDE_response_error_proved"] is False
            and z["complete_infinite_inverse_proved"] is False
            and zm["complete_Z_residual_preserves_raw_mean"] is True
            and zm["complete_original_raw_signed_mean_residuals_preserved"] is True
            and zm["small_norm_minimum_does_not_replace_polynomial_uniform_remainder"] is True
            and z["new_target_provider_calls"] == 0
            and z["old_original_target_mean_or_trial_reconstructions_executed"] == 0,
            "all full source qualifications and original false inverse scopes retained")
    require(set(z["complete_source_bounds"]) ==
                {"full_body", "inner_body", "fixed_negative_phase_window"}
            and all(set(v) == {"full_through160", "low193", "high97_through160"}
                    for v in z["complete_source_bounds"].values()),
            "all original radial windows and all full/low/high columns retained")

    def legacy(role, manifest_role, source_role, run, kind, gates, output_file):
        execution, old_manifest = data(role), data(manifest_role)
        actual = execution["actual_scientific_receipt"]
        require(execution["complete"] is True and execution["actual_returncode"] == 0
                and execution["actual_failure"] is None
                and execution["run_id"] == actual["run_id"] == run
                and execution["run_attempt"] == actual["run_attempt"] == "1"
                and actual["kind"] == kind and actual["complete"] is True
                and actual["proved"] is True and actual["actual_returncode"] == 0
                and actual["failure"] is None and len(actual["gates"]) == gates
                and all(g["passed"] is True for g in actual["gates"])
                and actual["arithmetic_bits"] == 320
                and actual["input_manifest_sha256"] == execution["input_manifest_sha256"]
                    == specs[manifest_role]["sha256"]
                and actual["source_sha256"] == execution["source_budget_source_sha256"]
                    == specs[source_role]["sha256"],
                "whole old science/execution/manifest/source and all gates: "+role)
        raw = canonical(actual)
        receipts = [x for x in execution["output_hashes"] if x["file"] == output_file]
        require(receipts == [{"file": output_file, "bytes": len(raw), "sha256": sha(raw)}],
                "entire embedded science reproduces its original output bytes: "+role)
        require(actual["old_numerical_enclosures_recomputed"] == 0
                and execution["old_numerical_enclosures_recomputed"] == 0
                and actual["public_repository"] == REPO,
                "original no-repeat and public-science identities: "+role)
        return actual, old_manifest

    d, dm = legacy("D_execution", "D_manifest", "D_source", "43713242980",
        "actual_selected_parameter_core_scalar_fees_from_complete_old_cells_v1",
        12, "actual-scalar-conclusion.json")
    require(d["parameters"] == dm["parameters"]
            and d["derived_continuous_centre_definition_sha256"] == CENTRE
            and d["derived_continuous_response_definition_sha256"] == DIRECTION
            and d["parameters"]["delta_half_width"] == PARAMETERS["delta_budget_radius"]
            and d["parameters"]["exact_negative_interval"] == PARAMETERS["exact_original_negative_window"]
            and d["parameters"]["fixed_intrinsic_parameter"] == "eta_0"
            and d["parameters"]["source_norm"] == "ordinary L2_r L2_phi; normalized circle, full mean"
            and d["exact_original_eta_and_nu"] == {
                "eta": "fixed original eta_0",
                "exact_alpha": PARAMETERS["exact_alpha"],
                "exact_nu": PARAMETERS["exact_nu_centre"]}
            and d["complete_original_rows_verified"] == 7721
            and d["actual_last_verified_original_row"] == 7720
            and len(d["original_part_receipts"]) == 40
            and d["complete_nu_response_extra_source_sign"]
                == "Delta F_nu + Delta A times the same complete continuous Z"
            and d["complete_selected_parameter_body_scalar_fees_proved"] is True,
            "same full selected difference source, true cover, sign and parameters")
    require(dm["files"][specs["D_source"]["path"]] == specs["D_source"]["sha256"]
            and dm["files"][specs["proof_D"]["path"]] == specs["proof_D"]["sha256"]
            and d["complete_response_repair_including_mean"] ==
                {"A0": "0.0000000000000002292", "angular_multiplier": 384}
            and d["complete_finite193_transferred_inverse_proved"] is False
            and d["complete_infinite_BVP_inverse_proved"] is False
            and d["true_parameter_Schur_proved"] is False
            and d["old_target_Fourier_cubic_mean_residual_integral_or_Green_calls"] == 0,
            "same paid D formula and full repair, without upgrading an old inverse")
    neg = d["complete_scalar_fee_conclusions"]["fixed_negative_window"]
    require(neg["exact_interval"] == PARAMETERS["exact_original_negative_window"]
            and neg["exact_total_radial_measure"] == PARAMETERS["exact_original_negative_window"][1]
            and neg["original_closed_rows_consumed"] == neg["new_exact_scalar_restrictions"] == 3071
            and "complete_additional_response_source" in neg["ordinary_L2_bounds"],
            "the entire exact fixed negative integral, not a compact or core substitute")

    sp, spm = legacy("SP_execution", "SP_manifest", "SP_source", "43731464771",
                    "actual_complete_primitive_mean_strict_propagation_v1",
                    20, "consumers/process.json")
    pw, pwm = legacy("PW_execution", "PW_manifest", "PW_source", "43734233535",
                    "actual_complete_positive_ports_to_waist_density_v1",
                    21, "consumers/process.json")
    family = sp["exact_family_identity"]
    require(family == pw["exact_family_identity"]
            and family["continuous_centre_definition_sha256"] == CENTRE
            and family["continuous_response_definition_sha256"] == DIRECTION
            and family["fixed_current_eta"] == "eta_0"
            and family["exact_alpha"] == PARAMETERS["exact_alpha"]
            and family["exact_nu_centre"] == PARAMETERS["exact_nu_centre"]
            and family["original_candidate_sha256"] == z["candidate_sha256"]
            and family["original_object_sha256"] == z["common_input_sha256"]["object"]
            and dm["original_body_manifest_sha256"] == zm["original_body_manifest_sha256"]
                == z["common_input_sha256"]["original-manifest"],
            "one full real repaired family across old source and negative receivers")
    require(sp["mathematical_parameters"] == spm["mathematical_parameters"]
            and pw["mathematical_parameters"] == pwm["mathematical_parameters"]
            and spm["scientific_source_sha256"] == specs["SP_source"]["sha256"]
            and pwm["scientific_source_sha256"] == specs["PW_source"]["sha256"],
            "complete unchanged SP/PW manifest parameter and source objects")
    for role, old_manifest, source_role, proof_role in (
            ("SP", spm, "SP_source", "proof_SP"),
            ("PW", pwm, "PW_source", "proof_PW")):
        for current_role in (source_role, proof_role):
            pins = [x for x in old_manifest["files"]
                    if x["path"] == specs[current_role]["path"]]
            require(len(pins) == 1 and pins[0]["sha256"] == specs[current_role]["sha256"]
                    and pins[0]["bytes"] == specs[current_role]["bytes"],
                    "same complete original "+role+" source/proof bytes")
    ps = sp["mathematical_parameters"]
    require(ps["exact_real_delta_radius"] == "1/100000000"
            and ps["exact_root_interval"] == PARAMETERS["exact_root_interval"]
            and ps["exact_root_Cauchy_radius"] == PARAMETERS["exact_root_Cauchy_radius"]
            and ps["exact_strict_interval"] == PARAMETERS["exact_strict_interval"]
            and ps["complete_mean_coordinates"] == 2
            and pw["mathematical_parameters"]["ordinary_radial_measure"] == "dr",
            "same true root, strict cut, full family and both physical means")
    gains = sp["complete_endpoint_readout_conclusion"]
    copied = pw["complete_negative_inputs_conclusion"][
        "original_endpoint_gain_fields_read_verbatim"]
    require(set(copied) == set(GAIN_KEYS)
            and all(copied[name] == gains[name] for name in GAIN_KEYS)
            and gains["exact_cut"] == PARAMETERS["exact_strict_interval"][1]
            and gains["waist_output"] == "L2 old-circle density pair plus both full mean coordinates",
            "every saved original gain copied literally with the original complete waist")
    require(pw["accepted_small_input_conclusions"]["strict"]["execution_sha256"]
                == specs["SP_execution"]["sha256"]
            and pw["accepted_small_input_conclusions"]["strict"]["input_manifest_sha256"]
                == specs["SP_manifest"]["sha256"]
            and pw["accepted_small_input_conclusions"]["strict"]["source_sha256"]
                == specs["SP_source"]["sha256"],
            "PW actually consumed this entire SP input, not an unrelated gain")
    for flag in ("all_Fourier_variations_and_two_means_retained",
                 "actual_radial_measure_used", "full_ordinary_sources_and_affine_impulses_retained",
                 "original_positive_graph_and_root_mixed_ports_retained"):
        require(sp["scope"][flag] is True, "complete old negative scope: "+flag)
    require(sp["full_high_inverse_claimed"] is False
            and sp["full_return_remainder_claimed"] is False
            and pw["scope"]["finite_root_head_and_two_means_independent"] is True
            and pw["full_high_inverse_claimed"] is False
            and pw["full_return_remainder_claimed"] is False,
            "ordinary contribution does not erase roots, incoming inverse, or the rest of the return")

    # Exact rational theorem restrictions only.  This is not scientific
    # recomputation of the old selected pair or an inferred derivative.
    radius = Fraction(PARAMETERS["delta_budget_radius"])
    selected = Fraction(PARAMETERS["selected_parameter_absolute_upper"])
    ratio = Fraction(PARAMETERS["selected_to_budget_ratio_upper"])
    lo, hi = map(Fraction, PARAMETERS["exact_root_interval"])
    cut = Fraction(PARAMETERS["exact_strict_interval"][1])
    RN = Fraction(PARAMETERS["exact_original_negative_window"][1])
    require(0 < selected/radius < ratio < 1
            and Fraction(9, 50) < lo <= hi == RN
            and 0 < cut < lo and hi-cut == Fraction(1, 200)
            and radius < Fraction(ps["exact_real_delta_radius"]),
            "same selected pair restriction and full fixed-window/root/strict containment")
    return {"source": z, "difference": d, "negative_difference": neg,
            "SP": sp, "PW": pw, "family": family, "gains": copied}


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
            "one new scientific child only in the authorized public Actions")
    raw_manifest = args.manifest.read_bytes()
    require(sha(raw_manifest) == args.manifest_sha, "whole new actual-input manifest")
    manifest = parse(raw_manifest)
    require(manifest["kind"] == MANIFEST_KIND and manifest["scientific_kind"] == KIND
            and manifest["stage"] == STAGE and manifest["parameters"] == PARAMETERS
            and manifest["target_order"] == TARGETS
            and manifest["complete_record_counts"] == [4]
            and manifest["allowed_scientific_fields"] == SCI_FIELDS,
            "one declared complete selected-negative-source-and-receiver target")
    specs = {spec["role"]: spec for spec in manifest["files"]}
    require(len(specs) == len(manifest["files"])
            and specs["science"]["path"] == SOURCE_PATH
            and specs["worker"]["path"] == WORKER_PATH
            and specs["generator"]["path"] == GENERATOR_PATH,
            "unique whole owner/worker/metadata source identities")
    paths = parse(args.input_map.read_bytes())
    require(set(paths) == set(specs), "complete materialized old-input closure")
    contents = {role: Path(path).read_bytes() for role, path in paths.items()}
    require(sha(Path(__file__).read_bytes()) == specs["science"]["sha256"],
            "this actual new mathematical source is pinned")
    prior = admit_complete_inputs(contents, specs)
    require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
            "whole metadata admission before numerical imports")
    require(not args.output.exists(), "never overwrite a prior scientific prefix")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    z = prior["source"]
    neg = prior["negative_difference"]
    old_records = {
        "source_zero_global_full": copy.deepcopy(
            z["complete_source_bounds"]["full_body"]["full_through160"]["L2_L2_radial"]),
        "source_zero_same_fixed_negative_full": copy.deepcopy(
            z["complete_source_bounds"]["fixed_negative_phase_window"]["full_through160"]["L2_L2_radial"]),
        "complete_selected_difference_at_radius_d": copy.deepcopy(
            neg["ordinary_L2_bounds"]["complete_additional_response_source"]),
        "original_SP_PW_negative_gains": copy.deepcopy(prior["gains"]),
    }
    document = {
        "identity": {
            "kind": KIND, "scalar_stage": STAGE,
            "source_sha256": specs["science"]["sha256"],
            "manifest_sha256": args.manifest_sha,
            "run_id": os.environ["GITHUB_RUN_ID"], "run_attempt": "1",
            "event_commit": os.environ["GITHUB_SHA"], "actual_checkout_commit": args.checkout,
            "arithmetic_bits": PARAMETERS["arithmetic_bits"],
        },
        "complete": False, "proved": False, "actual_returncode": None, "failure": None,
        "stage": "whole_source_and_negative_receiver_inputs_admitted",
        "completed_targets": [], "current_target": None, "candidate_record": None, "new_records": {},
        "saved_record_count": 0, "parameters": copy.deepcopy(PARAMETERS), "result": None,
        "whole_completed_inputs": {
            role: {"file": copy.deepcopy(spec), "json_path": []}
            for role, spec in specs.items() if not spec["path"].endswith(".py")},
        "reference_identity": copy.deepcopy(prior["family"]),
        "selected_member_identity": {
            "run": PARAMETERS["selected_member_run"], "loss": PARAMETERS["selected_member_loss"],
            "absolute_delta_upper": PARAMETERS["selected_parameter_absolute_upper"],
            "ratio_upper": PARAMETERS["selected_to_budget_ratio_upper"],
            "original_proof_files": [copy.deepcopy(specs[name]) for name in
                                     ("proof_W", "proof_NIF", "proof_R147", "proof")],
            "selected_parameter_replaced_by_a_numeric_point": False,
        },
        "copied_prior_scalar_records": old_records,
        "old_scientific_target_calls": 0, "new_arrays_published": 0,
        "new_artifacts": 0, "new_Releases": 0, "wall_seconds": 0.0, "runtime": {},
    }
    require(sorted(document) == SCI_FIELDS, "exact new complete scientific schema")
    began = time.perf_counter()

    def save():
        document["wall_seconds"] = time.perf_counter()-began
        require(document["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                "bounded new four-record scalar target with a complete prefix")
        raw = canonical(document)
        require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"],
                "complete small scientific result fits its declared budget")
        atomic(args.output, raw)

    save()
    try:
        import flint
        from importlib.metadata import version
        runtime = {"python": platform.python_version(),
                   "packages": {"python-flint": version("python-flint")}}
        require(runtime == manifest["runtime"], "fixed directed scalar runtime")
        document["runtime"] = runtime
        flint.ctx.prec = PARAMETERS["arithmetic_bits"]
        arb = flint.arb

        def old_upper(record):
            require(isinstance(record, dict) and "ball" in record, "whole accepted old Arb record")
            if "lower" in record and "upper" in record:
                value = arb(record["lower"]).lower().union(arb(record["upper"]).upper())
            else:
                value = arb(record["ball"])
            require(value.is_finite() and value.lower() >= 0, "finite nonnegative complete old ball")
            return value.upper()

        def emit(name, value):
            require(name == TARGETS[document["saved_record_count"]] and value.is_finite(),
                    "complete ordered new scalar record")
            point = value.upper()
            require(point >= 0, "nonnegative directed upper")
            record = {"ball": point.str(PARAMETERS["decimal_record_digits"]), "bound": "upper"}
            require(document["candidate_record"] is None,
                    "no unfinished candidate may be silently replaced")
            document["candidate_record"] = {"name": name, "record": record}
            document["current_target"] = name
            document["stage"] = "whole_new_scalar_candidate_saved"
            save()
            candidate = parse(args.output.read_bytes())["candidate_record"]
            ball = arb(candidate["record"]["ball"])
            require(candidate == {"name": name, "record": record}
                    and ball.is_finite() and ball.contains(point),
                    "whole candidate readback contains the original directed upper")
            # Only the successful whole-candidate check advances completion.
            document["new_records"][name] = copy.deepcopy(candidate["record"])
            document["completed_targets"].append(name)
            document["saved_record_count"] += 1
            document["candidate_record"] = None
            document["stage"] = "complete_new_scalar_saved"
            document["current_target"] = None
            save()
            formal = parse(args.output.read_bytes())["new_records"][name]
            final_ball = arb(formal["ball"])
            require(formal == candidate["record"] and final_ball.is_finite()
                    and final_ball.contains(point),
                    "formal completed prefix has the identical whole verified record")
            return final_ball.upper()

        sg = old_upper(old_records["source_zero_global_full"])
        sn = old_upper(old_records["source_zero_same_fixed_negative_full"])
        dn = old_upper(old_records["complete_selected_difference_at_radius_d"])
        ratio = Fraction(PARAMETERS["selected_to_budget_ratio_upper"])
        tau = arb(ratio.numerator)/arb(ratio.denominator)
        fg = emit(TARGETS[0], (sg+tau*dn).upper())
        fn = emit(TARGETS[1], (sn+tau*dn).upper())
        co = old_upper(old_records["original_SP_PW_negative_gains"][
            "ordinary_root_window_source_to_waist_density_gain"])
        c2 = old_upper(old_records["original_SP_PW_negative_gains"][
            "strict_L2_Hminus1_source_to_waist_density_gain"])
        gn = emit(TARGETS[2], (co*co+c2*c2).upper().sqrt().upper())
        contribution = emit(TARGETS[3], (fn*gn).upper())
        require(fn < fg and fg < arb(3720478)/arb(10**12),
                "same-window full source improves the intact R147 strict rational global bound")
        require(contribution.is_finite() and contribution >= 0
                and document["completed_targets"] == TARGETS
                and document["saved_record_count"] == 4,
                "all four complete source/receiver records, with saved-input dependency")
        document["result"] = {
            "kind": KIND, "complete_new_record_count": 4,
            "complete_new_record_order": list(TARGETS),
            "selected_negative_full_source_proved": True,
            "same_fixed_window_source_strictly_tighter_than_global_restriction": True,
            "original_R147_global_strict_bound_preserved": True,
            "complete_negative_ordinary_to_waist_density_contribution_proved": True,
            "complete_second_nonmean_source_admitted_by_SC2": True,
            "both_physical_density_means_in_output": True,
            "same_raw_source_restricted_to_disjoint_true_radial_windows": True,
            "both_dependencies_used_whole_saved_readback_upper": True,
            "old_Cauchy_source_or_strict_computation_repeated": False,
            "root_stable_or_finite_trace_contribution_included": False,
            "positive_source_or_positive_root_return_contribution_included": False,
            "independent_germ_interface_or_impulse_contribution_included": False,
            "physical_height_Robin_mean_or_phase_source_rows_included": False,
            "actual_incoming_or_principal_angle_normalization_applied": False,
            "complete_nu_response_error_proved": False,
            "complete_incoming_inverse_proved": False,
            "true_nu_or_phase_Schur_proved": False,
            "nonlinear_background_or_surface_proved": False,
            "topic_completion_proved": False,
        }
        document["complete"] = document["proved"] = True
        document["actual_returncode"] = 0
        document["stage"] = "complete_"+STAGE+"_scalar_branch"
        save()
        return 0
    except BaseException as error:
        document["complete"] = document["proved"] = False
        document["actual_returncode"] = 1
        document["stage"] = "failed_with_complete_scalar_prefix"
        document["failure"] = {"type": type(error).__name__, "message": str(error)[:2000],
                               "traceback": traceback.format_exc()[-8000:]}
        print(traceback.format_exc(), flush=True)
        document["wall_seconds"] = time.perf_counter()-began
        atomic(args.output, canonical(document))
        return 1


if __name__ == "__main__":
    sys.exit(main())
