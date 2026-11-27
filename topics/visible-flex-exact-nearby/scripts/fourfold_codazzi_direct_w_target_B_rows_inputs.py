"""Whole ASR qualification for direct DWT2 followed by original BR7.

The original BW4/BR7 entries are retained as unexecuted source identities.
No BW actual is fabricated. DWT supplies the same true-w object and both
whole errors before the original seven finite-row formulas can execute.
"""
from __future__ import annotations
import ast
import hashlib
import json
import sys
import types

TOPIC = "topics/visible-flex-exact-nearby/"
SOURCE_PATH = TOPIC+"scripts/fourfold_codazzi_direct_w_target_B_rows_owner.py"
WORKER_PATH = TOPIC+"scripts/fourfold_codazzi_direct_w_target_B_rows_public_worker.py"
GENERATOR_PATH = TOPIC+"scripts/make_direct_w_target_B_rows_manifest.py"
CARRIER_SHA = "acd0ebe5158bf143b7a85a14fdd3413fc2ff32aef13d90f8417ed7ef4e4254f4"
ADMISSION_SHA = "40c9893cf4a17399b0f913962eee68066b09e66f165a3d79e3654d6aa9d3e9fc"
DWT_SHA = "c13018ef74382104b8ded0f6412913ddd15a7716b55c19dfd9772efe21be3da3"
UDR_SHA = "a562056bb8bc1100cf8402717548b1c4b85fa4bea6f0eb3fe456a8cc71381ae8"
BR_SHA = "dd5eb6055329c65c5460a476ba93c98bf4132a9333ed6e204c901fc7018aca38"
PROPOSAL_SHA = "d7b132b92cdb4a90837c2148bbcb3f0d6a0cd080552fe4bb793e38baab2592cf"
ORIGINAL = {
    "original_BW_owner": (23193, "0752011a4d3245f80585ace11dd70ab50118ce8a784b953546144a116b498be8"),
    "original_BW_worker": (12441, "0f5b9a97fe248977e0d74fc995717edab8bd5a5d68001787a9d6cb5cc6819dcc"),
    "original_BW_generator": (9774, "5e5a3954c241eb1c1810c09f1d1ec113f9144800086f7bcf0e0574a0b08cd66f"),
    "original_BW_math": (3653, "a1c8ef0a4dd2d0f595919a2582a484cb91e7aa972349e07e655ec11b922fe371"),
    "original_BR_owner": (25975, "53a96d3eb3c77eb9e29012b5e0475b6ec3293c664d7efe1b3252676f3ebbb463"),
    "original_BR_worker": (12623, "fa876e961d1f8bfe2ca12d9a3b4a3a8ba6c4302a939c26295461ea8231e4d04b"),
    "original_BR_admission": (7864, "47435f118d8447709310c206121a99c358e4acc812c771317a559753cffb4a69"),
    "original_BR_generator": (9014, "f2fab675c8ce232135eba4a2c7fa1071501278afbaf147e4d103afbd1ca83945"),
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def definitions(raw, name):
    ast.parse(raw.decode(), filename=name)
    module = types.ModuleType(name)
    module.__file__ = name
    exec(compile(raw, name, "exec"), module.__dict__)
    return module


def admit_complete_inputs(contents, specs, manifest):
    require(set(contents) == set(specs) and set(manifest["parent_roles"]) == {"AS"}
            and manifest["historical_inputs"] == [], "the entire source192 ASR original closure")
    for role, spec in specs.items():
        raw = contents[role]
        require(spec["role"] == role and type(raw) is bytes and 0 < len(raw) < 100000
                and len(raw) == spec["bytes"] and sha(raw) == spec["sha256"]
                and blob(raw) == spec["git_blob_sha"], "whole direct-w row input: "+role)
        raw.decode()
        if spec["path"].endswith(".py"):
            ast.parse(raw.decode(), filename=spec["path"])
    require(specs["science"]["path"] == SOURCE_PATH and specs["worker"]["path"] == WORKER_PATH
            and specs["generator"]["path"] == GENERATOR_PATH
            and sha(contents["carrier_original_owner"]) == CARRIER_SHA
            and sha(contents["parent_admission"]) == ADMISSION_SHA
            and sha(contents["DWT_math"]) == DWT_SHA and sha(contents["UDR_math"]) == UDR_SHA
            and sha(contents["BR_math"]) == BR_SHA and sha(contents["proposal"]) == PROPOSAL_SHA,
            "all exact original input and complete new direct-w/old BR formula sources")
    require(all((len(contents[role]), sha(contents[role])) == expected for role, expected in ORIGINAL.items()),
            "all original unexecuted BW and BR source identities are retained")
    admission = definitions(contents["parent_admission"], "_DWTB_complete_original_ASR_admission")
    original, owner, admitted, old_specs, old_contents = admission.parent_closure("AS", contents, specs, manifest)
    actual, execution = admission.complete_actual("AS", original, owner, old_specs, old_contents, contents, specs)
    require(original["parameters"]["complete_raw_source_positive_modes"] == 192
            and old_specs["science"]["path"]
                == TOPIC+"scripts/fourfold_codazzi_original_alpha_full_source_owner.py"
            and actual["private_alpha_trial_receipt"]["positive_modes"] == 2048
            and actual["private_grid_receipt"]["complete_count"] == 8192,
            "the entire successful source192 ASR and original mean/phase/tail inputs")
    parent = dict(manifest=original, owner=owner, admitted=admitted, specs=old_specs,
                  contents=old_contents, actual=actual, execution=execution)
    for role, tags in {
        "DWT_proof": ("DWT.2", "DWT.8", "DWT.11", "DWT.12", "DWT.13"),
        "BR_proof": ("BR.2", "BR.6", "BR.8", "BR.12", "BR.13"),
        "implementation_note": ("DWTB.1", "DWTB.3", "DWTB.5"),
    }.items():
        require(all(tag in contents[role].decode() for tag in tags), "the complete original-object theorem: "+role)
    carrier = definitions(contents["carrier_original_owner"], "_DWTB_original_carrier_owner")
    grid_restore = definitions(contents["grid_restore"], "_DWTB_original_whole_grid_prefix")
    ast.parse(grid_restore.materializer_source(contents["carrier_original_owner"]))
    DWT = definitions(contents["DWT_math"], "_DWTB_direct_target_w_formulas")
    UDR = definitions(contents["UDR_math"], "_DWTB_complete_unit_disk_input_only")
    BR = definitions(contents["BR_math"], "_DWTB_unchanged_original_B_row_formulas")
    proposal = definitions(contents["proposal"], "_DWTB_first_B_row_proposal")
    require(DWT.MODES == BR.W_MODES == proposal.W_MODES == 2048 and DWT.GRID == UDR.GRID == 8192
            and UDR.MODES == 2048 and BR.ROWS == proposal.ROWS == 96
            and BR.TRIAL_MODES == proposal.MODES == 192, "all modes and all original full residual outputs")
    require(not any(name in sys.modules for name in ("numpy", "flint", "scipy")),
            "all complete admission functions remain metadata only")
    return dict(AS=parent, AS_math=admitted[4], SN_restore=admitted[3], carrier=carrier,
                grid_restore=grid_restore, DWT_math=DWT, UDR_math=UDR, BR_math=BR, proposal=proposal)
