"""Whole metadata admission for the first complete ORIGINAL Theta rows.

Both parents are admitted under their immutable complete contracts and
their own saved result validators. No numerical runtime is imported.
"""
from __future__ import annotations
import ast
import hashlib
import json
import sys
import textwrap
import types

TOPIC = "topics/visible-flex-exact-nearby/"
REPO = "Rogerhu12/math-research-public"
CYA_IDENTITIES = {
    "CYA_actual": (16375, "1f08e281eeff6bd09b0118f71adf17b1e5842ffc1cb71ebc9c8c78e5582bd20d"),
    "CYA_execution": (11170, "3f3947926f2f7ded20d1333fde2d9d197c02f996cd1f9bbf224a73d764e08a71"),
    "CYA_manifest": (8950, "8c40bc7b1619c8fba9ef35e614cb21e0f29e807b5369285f3060f78d2da6b311"),
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def definitions(raw, name):
    ast.parse(raw.decode(), filename=name)
    module = types.ModuleType(name)
    module.__file__ = name
    exec(compile(raw, name, "exec"), module.__dict__)
    return module


def parent_closure(tag, contents, specs, manifest):
    original = parse(contents[tag+"_manifest"])
    mapping = manifest["parent_roles"][tag]
    old_specs = {spec["role"]: spec for spec in original["files"]+original["historical_inputs"]}
    require(set(mapping) == set(old_specs), "whole original "+tag+" role map")
    found_specs, found_contents = {}, {}
    for role, spec in old_specs.items():
        here = mapping[role]
        require(here in specs and dict(specs[here], role=role) == spec,
                "whole unchanged parent input "+tag+"/"+role)
        found_specs[role], found_contents[role] = spec, contents[here]
    owner = definitions(found_contents["science"], "_OT_original_"+tag+"_owner")
    admitted = owner.admit_complete_inputs(found_contents, found_specs)
    return original, owner, admitted, found_specs, found_contents


def complete_actual(tag, original, owner, old_specs, old_contents, contents, specs):
    raw = contents[tag+"_actual"]
    document = parse(raw)
    identity = document["identity"]
    run, attempt = identity["run_id"], identity["run_attempt"]
    require(type(run) is str and run.isdigit() and attempt == "1",
            "one first complete actual "+tag+" identity")
    directory, name = ({"IR": ("inverse_density_rows_ci", "actual-original-inverse-density-rows.json"),
                       "AS": ("original_alpha_carrier_ci", "actual-original-alpha-carrier.json")})[tag]
    base = TOPIC+"notes/"+directory+"/run-"+run+"-"+attempt
    require(specs[tag+"_actual"]["path"] == base+"/"+name
            and specs[tag+"_execution"]["path"] == base+"/execution.json",
            "whole actual and receipt belong to the same original run")
    worker = definitions(old_contents["worker"], "_OT_original_"+tag+"_worker")
    space = dict(require=require, parse=parse, manifest=original, by_role=old_specs,
                 op=original["operation"], args=types.SimpleNamespace(
                     manifest_sha=specs[tag+"_manifest"]["sha256"]), run=run, attempt=attempt)
    exec(compile(textwrap.dedent(worker.VALIDATOR), "_OT_complete_parent_validator", "exec"), space)
    require(space["validate_output"](raw) == document,
            "the full original actual result validator, never a projected substitute")
    require(document["complete"] is document["proved"] is True
            and document["actual_returncode"] == 0 and document["failure"] is None
            and document["parameters"] == owner.PARAMETERS == original["parameters"]
            and document["completed_targets"] == owner.TARGETS == original["target_order"]
            and document["saved_record_count"] == len(owner.TARGETS)
            and document["current_target"] is document["candidate_record"] is None
            and document["old_scientific_target_calls"] == 0,
            "every whole "+tag+" target actually complete before any new Theta work")
    receipt = parse(contents[tag+"_execution"])
    require(receipt["repository"] == REPO and receipt["complete"] is True
            and receipt["failure"] is None and receipt["actual_child_returncode"] == 0
            and receipt["run_id"] == run and receipt["run_attempt"] == attempt
            and receipt["manifest_sha256"] == specs[tag+"_manifest"]["sha256"]
            and receipt["scientific_children"] == 1
            and receipt["old_completed_targets_recomputed"] == 0
            and receipt["original_scientific_complete"] is True
            and receipt["original_scientific_failure"] is None
            and receipt["completed_new_scalar_targets"] == len(owner.TARGETS)
            and receipt["current_input_receipts"] == original["files"]
            and receipt["actual_scientific_checkout"] == identity["actual_checkout_commit"]
            and receipt["new_arrays_published"] == receipt["new_artifacts"] == receipt["new_Releases"] == 0,
            "whole successful public "+tag+" execution")
    saved = next(value for value in receipt["scientific_files"]
                 if value["path"] == specs[tag+"_actual"]["path"])
    require(saved["bytes"] == len(raw) and saved["sha256"] == sha(raw),
            "the whole actual science file is saved by its completed worker")
    if tag == "IR":
        require(receipt["kind"] == "R149_complete_inverse_density_rows_execution_v1"
                and receipt["old_numerical_producers_called"] == 0
                and document["whole_completed_inputs"] == old_specs,
                "same entire original IR input closure")
        history = receipt["historical_restoration"]
        require(history["original_native_files_restored"] == 6
                and history["scientific_targets_recomputed"] == 0
                and history["complete_receipts"] == [dict(item, whole_original_bytes_restored=True,
                    new_numerical_computation=False) for item in original["historical_inputs"]],
                "the entire original IR native restoration, all six whole files")
    else:
        require(receipt["kind"] == "R149_complete_original_alpha_carrier_execution_v1"
                and receipt["old_numerical_producers_called"] == 1
                and document["necessary_original_input_rematerializations"] == 1
                and receipt["necessary_original_SN_endpoint_restoration"] == document["original_endpoint_restoration"]
                and receipt["complete_original_SN_input_restoration"] == document["original_input_restoration"]
                and receipt["completed_original_alpha_modes"] == 2048
                and document["whole_completed_inputs"] == {role: {"bytes": item["bytes"], "sha256": item["sha256"]}
                    for role, item in old_specs.items()},
                "same complete AS carrier and its necessary exact original endpoint")
    return document, receipt


def admit_complete_inputs(contents, specs, manifest):
    require(set(contents) == set(specs) and set(manifest["parent_roles"]) == {"IR", "AS"},
            "the complete declared current/native closure and both parent maps")
    for role, spec in specs.items():
        raw = contents[role]
        require(spec["role"] == role and type(raw) is bytes
                and len(raw) == spec["bytes"] and sha(raw) == spec["sha256"]
                and blob(raw) == spec["git_blob_sha"], "whole immutable Theta input: "+role)
        if spec.get("encoding") != "gzip-json":
            require(0 < len(raw) < 100000, "complete small current text")
            raw.decode()
            if spec["path"].endswith(".py"):
                ast.parse(raw.decode(), filename=spec["path"])
    contexts = {}
    for tag in ("IR", "AS"):
        original, owner, admitted, old_specs, old_contents = parent_closure(tag, contents, specs, manifest)
        actual, receipt = complete_actual(tag, original, owner, old_specs, old_contents, contents, specs)
        contexts[tag] = dict(manifest=original, owner=owner, admitted=admitted,
                             specs=old_specs, contents=old_contents, actual=actual, execution=receipt)
    ir, alpha = contexts["IR"], contexts["AS"]
    prior, IL, states, DC, DB, IR = ir["admitted"]
    original_SN, SN, density, restore, AS = alpha["admitted"]
    for role in ("W_native", "K_native", "H_native"):
        original = ir["specs"][role]
        require(original_SN["files"][original["path"]] == original["sha256"],
                "exact same original selected conjugacy/phase source for IR and AS")
    terminal = SN["complete_first_nonmean_coefficient_H3_conclusion"]
    require(alpha["actual"]["copied_original_records"]["complete_signed_mu"]
                == terminal["complete_scalar_mu_copied"]
            and ir["actual"]["reference_identity"] == prior["family"]
            and ir["actual"]["copied_prior_scalar_records"]["IL"] == IL["new_records"]
            and ir["actual"]["selected_member_identity"] == IL["selected_member_identity"]
            and sha(ir["contents"]["IL_actual"])
                == "9427186020322b43d99d49fc239c2150949f3155cafc66217ac01469bea88b5e"
            and sha(ir["contents"]["IL_execution"])
                == "8abee7df4e00e4296b6147929e10c729f852a011ea4e5e7c50a0f87874dbd499",
            "the same full selected objects, moving mean and all four actual SDI input balls")
    for role, (size, digest) in CYA_IDENTITIES.items():
        require(len(contents[role]) == size and sha(contents[role]) == digest,
                "the whole immutable successful "+role)
    cayley, execution, original = (parse(contents[role]) for role in ("CYA_actual", "CYA_execution", "CYA_manifest"))
    require(cayley["complete"] is cayley["proved"] is cayley["complete_Cayley_scalar_gap_proved"] is True
            and cayley["failure"] is None and cayley["actual_returncode"] == 0
            and str(cayley["run_id"]) == "43757868884" and str(cayley["run_attempt"]) == "1"
            and len(cayley["gates"]) == 18 and all(g["passed"] is True for g in cayley["gates"])
            and cayley["input_sha256"] == dict(original["mathematical_input_sha256"],
                manifest=specs["CYA_manifest"]["sha256"])
            and cayley["source_sha256"] == original["source_sha256"]
            and cayley["mathematical_parameters"] == original["parameters"]
            and execution["complete"] is True and execution["actual_returncode"] == 0
            and execution["actual_failure"] is None
            and execution["scientific_conclusion"]["bytes"] == len(contents["CYA_actual"])
            and execution["scientific_conclusion"]["sha256"] == specs["CYA_actual"]["sha256"],
            "entire original finite Cayley and independent native infinite scope")
    finite, tail = cayley["complete_new_finite_Cayley_conclusion"], cayley["complete_new_analytic_tail_conclusion"]
    require(finite["complete_selected_same_parameter_scalar_gap_proved"] is True
            and finite["inherited_tail_scope"] == "original native interval only; actual selected beta belongs to it"
            and finite["new_complete_signed_pair_count"] == 7416
            and finite["physical_frequency_is_four_times_signed_label"] is True
            and tail["first_abs_label"] == 1024
            and tail["wider_finite_interval_does_not_acquire_old_infinite_proof"] is True
            and tail["new_Cayley_gap_times_abs_label"] == "1/1024"
            and tail["strict_exact_integer_comparison_passed"] is True,
            "low reference is distinct; only original selected full high scope is used")
    proof_tags = {"DT_proof": ("DT.5", "DT.8"), "TM_proof": ("TM.2", "TM.9"),
                  "TP_proof": ("TP.7", "TP.12"), "SDI_proof": ("SDI.4", "SDI.9"),
                  "WFI_proof": ("WFI.7", "WFI.10", "WFI.15"), "WGB_proof": ("Theta",)}
    for role, tags in proof_tags.items():
        text = contents[role].decode()
        require(all(tag in text for tag in tags), "complete original operator theorem: "+role)
    contexts.update(prior=prior, IL=IL, states=states, IR_math=IR, AS_math=AS,
        SN=SN, SN_restore=restore, density=density, CYA=cayley,
        DT=definitions(contents["DT_math"], "_OT_same_sign_original_Astar"),
        TM=definitions(contents["TM_math"], "_OT_original_graph_model_adjoint"),
        TP=definitions(contents["TP_math"], "_OT_complete_alpha_error_products"))
    require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
            "whole prerequisite admission remains metadata only")
    return contexts
