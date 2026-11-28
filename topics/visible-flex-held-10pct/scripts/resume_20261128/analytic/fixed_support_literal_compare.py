#!/usr/bin/env python3
"""Compare complete actual prefix fields with one frozen R53 metric.

This is a narrow adapter to the existing Nov26 complete-C2 comparison. The
left field may be the genuine design anchor, evaluated at its actual delta,
or a genuinely accepted original-support fixed-g return. The right field
must be a genuinely accepted literal-chart fixed-g return. A design anchor
is not relabelled as an independently solved fixed-g run. All six Cartesian
jets, the common mean1168 primitive and literal core coefficients are kept.
The results are sampled finite differences, not a Cauchy or closure proof.
"""
import os
for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "1"

import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import sys
from types import SimpleNamespace
import numpy as np

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
sys.path[:0] = [str(HERE), str(SCRIPTS/"resume_20261126")]
import fixed_support_literal_model as literal
from material_design_secant_predictor import accepted_original


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def main():
    legacy_path = SCRIPTS/"resume_20261126/fixed_m3_compare_c2.py"
    legacy = module("_literal_complete_c2_original", legacy_path)
    if "--help" in sys.argv:
        return legacy.main()
    paths = [Path(sys.argv[sys.argv.index(flag)+1]).resolve()
             for flag in ("--first-run", "--second-run")]
    output = Path(sys.argv[sys.argv.index("--out")+1]).resolve()
    records = [json.loads(path.read_text()) for path in paths]
    left_design = records[0].get("fixed_metric") is not True
    if left_design:
        accepted_original(paths[0], SCRIPTS.parents[2])
        anchor_path = paths[0]
    else:
        anchor_path = Path(records[0]["origin_design_run"]).resolve()
    anchor = json.loads(anchor_path.read_text())
    anchor_signature = literal.original_source_signature(anchor)
    for index, (path, record) in enumerate(zip(paths, records)):
        if index == 0 and left_design:
            continue
        if (record.get("model_kind") != literal.KIND
                or record.get("finite_linear_candidate_pass") is not True
                or record.get("actual_solve_invoked") is not True):
            raise ValueError("A fixed-g comparison field must be a real accepted literal-chart solve")
        if Path(record["origin_design_run"]).resolve() != anchor_path:
            raise ValueError("The two fields do not share the same actual design anchor")
        if (record["frozen_profile"] != anchor["frozen_profile"]
                or record["mean_nodes"] != anchor["prefix_audit"]["samples_psi"]
                or record["frozen_source_signature"] != anchor_signature):
            raise ValueError("The literal physical metric, mean rule or source changed")
        for file, digest in ((path.parent/record["raw_return"]["file"], record["raw_return"]["sha256"]),
                             (path.parent/"physical.npz", record["physical_sha256"])):
            if sha(file) != digest:
                raise ValueError("A complete actual field changed: "+str(file))
    original_require = legacy.require_same_problem
    captured = {}
    memo_stats = {}

    def require_same(left, right):
        if not left_design:
            contract = original_require(left, right)
            if left["frozen_literal_radial_chart"] != right["frozen_literal_radial_chart"]:
                raise ValueError("Literal computational chart changed")
            return contract
        for key in ("frozen_profile", "physical_tail_parameters", "physical_tail_cut",
                    "angular_chart", "core_settings", "gauge_q", "warp_reference"):
            if left[key] != right[key]:
                raise ValueError("The actual design and fixed field differ physically: "+key)
        if right["terminal_kind"] != "original_linear_dn":
            raise ValueError("The actual terminal equation changed")
        if left.get("actual_tail_requested") or left.get("original_actual_nonlinear_tail"):
            raise ValueError("Cannot compare a nonlinear tail to this linear Robin prefix")
        if not right["q_branch"][0] <= left["gauge_q"] <= right["q_branch"][1]:
            raise ValueError("The actual design anchor is outside the declared nonzero branch")
        return {key: right[key] for key in (
            "frozen_profile", "physical_tail_parameters", "physical_tail_cut",
            "angular_chart", "core_settings", "gauge_q", "warp_reference",
            "q_branch", "mean_nodes", "bc_normalization", "terminal_kind",
            "parameter_zero_meaning", "frozen_source_signature")}

    def load_left(config):
        if Path(config["source_run"]).resolve() != paths[0]:
            raise ValueError("Only the declared first source is loaded by the original entry")
        if left_design:
            adapter = module("_literal_c2_actual_anchor", SCRIPTS/"resume_m3/actual_m3_metric_model.py")
            obj = adapter.load_model(config)
        else:
            obj = literal.load_model(config)
        captured.update(literal.chart_record(obj))
        if captured != records[1]["frozen_literal_radial_chart"]:
            raise ValueError("The second field did not preserve the actual source radial chart")
        with np.load(paths[0].parent/records[0]["raw_return"]["file"], allow_pickle=False) as raw:
            obj.initial(raw["p"])
        memo = module("_literal_c2_complete_core_memo", HERE.parent/"design/material_core_evaluate_cache.py")
        # The two angular audits and fixed mean use three literal theta grids.
        # Four entries only reduce eviction; their full-state keys are unchanged.
        memo_stats.update(cache=memo.install(type(obj._core), max_entries=4),
                          source_sha256=sha(HERE.parent/"design/material_core_evaluate_cache.py"))
        return obj

    def second_chart(obj):
        literal.restore_chart(obj, captured)
        return obj

    original_main = inspect.getsource(legacy.main)
    replacements = {
        'loader = module("_c2_common_fixed_branch_loader", HERE/"fixed_m3_branch_model.py")':
            'loader = literal_loader',
        '    objects = [obj0, obj1]':
            '    obj1 = restore_second_literal_chart(obj1)\n    objects = [obj0, obj1]',
    }
    modified = original_main
    for before, after in replacements.items():
        if modified.count(before) != 1:
            raise ValueError("The declared original complete comparison entry changed")
        modified = modified.replace(before, after)
    legacy.require_same_problem = require_same
    legacy.__dict__.update(literal_loader=SimpleNamespace(load_model=load_left),
                           restore_second_literal_chart=second_chart)
    exec(compile(modified, str(Path(__file__).resolve())+"::literal_main", "exec"), legacy.__dict__)
    legacy.main()
    result = json.loads(output.read_text())
    result.update(adapter_scope=__doc__, adapter_source_sha256=sha(__file__),
        literal_model_source_sha256=sha(HERE/"fixed_support_literal_model.py"),
        original_compare_source_sha256=sha(legacy_path),
        original_main_sha256=hashlib.sha256(original_main.encode()).hexdigest(),
        executed_main_sha256=hashlib.sha256(modified.encode()).hexdigest(),
        left_field_kind="actual_design_anchor_at_its_frozen_delta" if left_design else literal.KIND,
        right_field_kind=literal.KIND,
        source_acceptance=["accepted_original_design" if left_design else "accepted_actual_fixed_g_solve",
                           "accepted_actual_fixed_g_solve"],
        design_anchor_relabelled_as_fixed_solver_return=False,
        literal_radial_chart=captured,
        complete_core_evaluate_cache=memo_stats,
        original_equations_changed=False)
    output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")


if __name__ == "__main__":
    main()
