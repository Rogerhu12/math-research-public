"""Necessary whole OT carrier restoration; no completed norm is executed.

The two exact original finite-carrier blocks are retained verbatim from
its whole admitted owner. Both precede/omit the completed norm targets.
All four complete original private SHA identities are required afterward.
"""
from __future__ import annotations
import ast
import hashlib
import textwrap

FIRST_BLOCK_SHA = "b8477204bcc9678a7660a3d5200af97d3a84d52d0c7a8fb71e54e893dfd8dba0"
SECOND_BLOCK_SHA = "58a8d2914eeb5d9275b0120206a60b16067381875a1d47d317e4f18f4b41510e"
RECEIPTS = ("private_DT_rows_receipt", "private_model_multipliers_receipt",
            "private_model_rows_receipt", "private_Theta_trial_receipt")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def materializer_source(original_owner_raw):
    source = original_owner_raw.decode()
    first = '        raw = (private/"original-IR/complete-original-IR-trial.f64").read_bytes()'
    stop_first = '\n        def emit('
    second = '        # Every coefficient of the original same-sign A*G action is retained.'
    stop_second = '        rounding, row_squares = TM.complete_model_rounding_error('
    require(all(source.count(marker) == 1 for marker in (first, stop_first, second, stop_second)),
            "each complete original carrier block has its unique original boundary")
    start1, start2 = source.index(first), source.index(second)
    block1 = source[start1:source.index(stop_first, start1)]
    block2 = source[start2:source.index(stop_second, start2)]
    require(hashlib.sha256(block1.encode()).hexdigest() == FIRST_BLOCK_SHA
            and hashlib.sha256(block2.encode()).hexdigest() == SECOND_BLOCK_SHA,
            "both exact complete original carrier blocks, before every old norm")
    header = ('def materialize(api, context, private, document, progress):\n'
              '    arb, acb, rational = api.arb, api.acb, api.rational\n'
              '    ir, alpha = context["IR"]["actual"], context["AS"]["actual"]\n'
              '    DT, TM = context["DT"], context["TM"]\n')
    generated = header+textwrap.indent(textwrap.dedent(block1), '    ')+"\n"+textwrap.indent(
        textwrap.dedent(block2), '    ')+"    return formal_rows, exact_rows\n"
    tree = ast.parse(generated)
    forbidden_names = {"emit", "complete_new_finite_carrier_norms", "complete_product_candidates",
        "complete_true_alpha_upper", "complete_original_joint_errors", "complete_model_rounding_error",
        "complete_original_Theta_error"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = node.func.id if isinstance(node.func, ast.Name) else (
                node.func.attr if isinstance(node.func, ast.Attribute) else None)
            require(name not in forbidden_names, "no completed target call in either restoration block")
    return generated


def restore(api, context, original_owner, original_owner_raw, original_actual, private, progress):
    require(original_actual["complete"] is original_actual["proved"] is True,
            "the entire completed original Theta result, before restoring its witnesses")
    for name in ("complete_new_finite_carrier_norms", "complete_product_candidates",
                 "complete_true_alpha_upper", "complete_original_joint_errors"):
        setattr(context["TP"], name, original_owner.forbidden)
    for name in ("complete_model_rounding_error", "complete_original_Theta_error"):
        setattr(context["TM"], name, original_owner.forbidden)
    original_owner.main = original_owner.forbidden
    space = dict(original_owner.__dict__)
    exec(compile(materializer_source(original_owner_raw), "_TQC_original_OT_carrier_only", "exec"), space)
    document = {"private_complete_row_count": 0}

    def one_progress(stage, data):
        progress("necessary_original_OT_carrier_"+stage, data)

    formal_rows, exact_rows = space["materialize"](api, context, private, document, one_progress)
    require(document["private_complete_row_count"] == 96
            and document["actual_model_input_records"] == original_actual["actual_model_input_records"]
            and all(document[name] == original_actual[name] for name in RECEIPTS),
            "every whole original DT/model/ball/dyadic carrier and the same true model/phase records")
    return formal_rows, exact_rows, {
        "kind": "TQC_complete_original_OT_carrier_restoration_v1", "complete": True,
        "complete_signed_rows": 96, "complete_modes_per_row": 2240,
        "whole_original_SHA_required": True,
        "original_carriers": {name: document[name] for name in RECEIPTS},
        "actual_model_input_records": document["actual_model_input_records"],
        "original_finite_carrier_blocks_sha256": [FIRST_BLOCK_SHA, SECOND_BLOCK_SHA],
        "completed_OT_norm_or_error_targets_replayed": 0,
        "all_original_IR_AS_norm_residual_or_cohomology_targets_replayed": 0,
    }
