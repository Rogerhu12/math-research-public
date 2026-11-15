#!/usr/bin/env python3
"""Public Actions-only generic exact validation of R811's polynomial module.

The field is Q(c,zeta), c^7=2, and is explicitly NOT the original CM field.
The curve is u^2=z with a deliberately cancelling pair
(z-alpha^2)/(z+alpha^2-2*alpha*u), alpha=c+zeta.
True hard exits at atomic IO boundaries test continuation without changing
the mathematical task or adding an activation gate for original producers.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import time

import flint
from flint import fmpq_poly

FIELD_CORE_SHA = "f196cb805d1ca91e8995866032a0a3ec3f96aac06e03b67a7c1f196fff759251"
MODES = ("none", "after_tile", "after_receipt", "after_commit", "during_cleanup")


def sha(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as source:
        for block in iter(lambda: source.read(1024*1024), b""):
            value.update(block)
    return value.hexdigest()


def load_module(name, path):
    location = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(location)
    location.loader.exec_module(module)
    return module


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("All generic validation arithmetic runs in the public repository Actions.")


def worker(args):
    assert flint.__version__ == "0.9.0"
    assert sha(args.field_core) == FIELD_CORE_SHA
    request = json.loads(args.request.read_text())
    assert request["test_script_sha256"] == sha(__file__)
    assert request["module_helper_sha256"] == sha(args.module_helper)
    assert request["field_core_sha256"] == FIELD_CORE_SHA
    M = load_module("R811_generic_test_polynomial_module", args.module_helper)
    old = load_module("R811_generic_test_frozen_field_adapter", args.field_core)
    F = old.QKField(fmpq_poly([-2, 0, 0, 0, 0, 0, 0, 1]))
    assert F.degree == 7
    # Eisenstein at2 proves the c polynomial irreducible, and its degree7
    # implies disjointness from Q(zeta). No original model is asserted.
    A = M.Algebra(F)
    alpha, z = F.gen+F.zeta, A.variable
    inverse_alpha = alpha.inverse()
    tag = {
        "result": "R811-generic-polynomial-module-validation-fixture",
        "test_script_sha256": sha(__file__), "module_helper_sha256": sha(args.module_helper),
        "field_core_sha256": FIELD_CORE_SHA, "python_flint": flint.__version__,
        "generic_field": "Q(c,zeta), c^7=2, zeta^2+zeta+1=0",
        "generic_curve": "u^2=z", "generic_alpha": "c+zeta",
        "generic_normal_basis": ["1", "u"], "generic_second_basis": ["1", "v=1/u"],
        "generic_normal_basis_degrees": [0, 1],
        "fault_mode_and_filesystem_location_excluded_from_mathematical_identity": True,
        "original_CM_model_or_research_result_claimed": False,
    }
    args.output.mkdir(parents=True, exist_ok=True)
    marker = args.output/"fault-fired.json"

    class FaultStore(M.StageStore):
        def fire(self, boundary, name):
            if args.fault == boundary and not marker.exists():
                M.save(marker, {"boundary": boundary, "after_complete_write_or_delete": name,
                               "simulated_process_exit_code": 97,
                               "no_exception_cleanup_or_finally_will_execute": True})
                print("GENERIC_HARD_EXIT "+json.dumps({"boundary": boundary, "file": name}), flush=True)
                os._exit(97)

        def put(self, name, payload, complete=True, replace=False):
            existed = self.path(name).exists()
            entry = super().put(name, payload, complete=complete, replace=replace)
            if payload.get("matrix_label") == "R811-generic-tau-reduced":
                if payload.get("kind") == "exact_polynomial_vector_tile" and \
                   "operation_plan" in payload and not existed:
                    self.fire("after_tile", entry["file"])
                if payload.get("kind") == "completed_unimodular_operation" and not existed:
                    self.fire("after_receipt", entry["file"])
                if payload.get("kind") == "polynomial_matrix_checkpoint" and \
                   payload.get("operation_count", 0) >= 1:
                    self.fire("after_commit", entry["file"])
            return entry

        def remove_if_owned(self, name, prefix):
            existed = self.path(name).exists()
            super().remove_if_owned(name, prefix)
            if existed and prefix == "R811-generic-tau-reduced" and "-r-" in name:
                self.fire("during_cleanup", name)

    S = FaultStore(args.output/"work", tag, lambda: None)

    # An independent coefficientwise product checks the stride13 pack at
    # b-degree12, including both zeta components, before any module test.
    packing_name = "R811-generic-original-field-polynomial-arithmetic"
    if not S.exists(packing_name):
        p = A.poly([F.gen**6+F.zeta, F.gen**5-F.zeta*F.gen**6, F.gen+F.zeta*F.gen**2])
        q = A.poly([F.one-F.gen*F.zeta, F.gen**6+F.zeta*F.gen**4])
        coefficients = [F.zero]*(len(p)+len(q)-1)
        for i, left in enumerate(p.c):
            for j, right in enumerate(q.c):
                coefficients[i+j] = coefficients[i+j]+left*right
        assert p*q == A.poly(coefficients)
        laurent = M.Laurent(A, -3, z*z-A.poly(alpha*alpha))
        answer = laurent.divide_polynomial(z-A.poly(alpha))
        assert answer == M.Laurent(A, -3, z+A.poly(alpha))
        S.put(packing_name, {
            "generic_field_only": True, "b_degree12_stride13_product_matches_direct_convolution": True,
            "nonmonomial_factor_cancels_before_Laurent_denominator_check": True,
            "generic_c_field_not_original_b_field": True})

    completed = {}
    for chart in ("tau", "sigma"):
        p = z-A.poly(alpha*alpha) if chart == "tau" else A.one-z.scale(alpha*alpha)
        if chart == "tau":
            q_constant, q_u = z+A.poly(alpha*alpha), -2*alpha
        else:
            q_constant, q_u = A.one+z.scale(alpha*alpha), -2*alpha
        # Multiplication by a+b*u in basis (1,u) is [[a,b*z],[b,a]].
        columns = [[p, A.zero], [A.zero, p],
                   [-q_constant, -A.poly(q_u)], [-z.scale(q_u), -q_constant]]
        original = M.VectorMatrix(S, A, "R811-generic-"+chart+"-source", 4, 2, "columns", 1)
        if original.state is None:
            for column, values in enumerate(columns):
                for row, value in enumerate(values):
                    if not original.initial_tile_exists(column, row):
                        original.put_initial_tile(column, row, [value],
                            {"generic_curve": "u^2=z", "chart": chart,
                             "pair": "[Mp,-Mq]", "explicit_generic_pair": True})
            original.initialize([original.initial_vector(i) for i in range(4)],
                                {"phase": "generic_source_complete"},
                                {"generic_original_pair": True, "chart": chart})
        if not original.finished:
            original.finish({"generic_source_matrix": True, "immutable_original_P": True})
        reduced = M.VectorMatrix(S, A, "R811-generic-"+chart+"-reduced", 4, 2, "columns", 1)
        if reduced.state is None:
            reduced.initialize(original.state["vectors"], M.reducer_control(2, False),
                               {"immutable_generic_original_pair": S.spec(original.final_name)})
        M.reduce_columns(reduced, 2, False)
        kernel_rows = M.VectorMatrix(S, A, "R811-generic-"+chart+"-kernel-rows", 4, 2, "rows", 1)
        M.reverse_kernel_replay(reduced, kernel_rows, 2)
        joint = M.VectorMatrix(S, A, "R811-generic-"+chart+"-Hermite-joint", 2, 4, "columns", 1)
        M.transpose_kernel_rows(kernel_rows, joint, 2)
        M.reduce_columns(joint, 2, True)
        product = M.verify_full_kernel_product(original, joint, "R811-generic-"+chart)
        if chart == "tau":
            expected = [[A.one, A.poly(-inverse_alpha), -A.one, A.poly(-inverse_alpha)],
                        [A.zero, z-A.poly(alpha*alpha), z.scale(2*alpha), z+A.poly(alpha*alpha)]]
        else:
            expected = [[A.one, A.poly(-alpha), A.one, A.poly(alpha)],
                        [A.zero, z-A.poly(inverse_alpha*inverse_alpha),
                         z.scale(-2*inverse_alpha), -z-A.poly(inverse_alpha*inverse_alpha)]]
        for column in range(2):
            for row in range(4):
                assert joint.entry(joint.state["vectors"][column], row) == expected[column][row]
        assert sum(x["degree"] for x in joint.state["actual_diagonal"]) == 1
        completed[chart] = (original, reduced, kernel_rows, joint, product)
    forward = M.verify_laurent_inclusion(completed["tau"][3], completed["sigma"][3], [0, 1],
                                        "R811-generic-tau-to-sigma", "tau", "sigma")
    backward = M.verify_laurent_inclusion(completed["sigma"][3], completed["tau"][3], [0, 1],
                                         "R811-generic-sigma-to-tau", "sigma", "tau")
    tau_degree = sum(x["degree"] for x in completed["tau"][3].state["actual_diagonal"])
    boundary_degree = sum(x["order_at_zero"] for x in completed["sigma"][3].state["actual_diagonal"])
    assert (tau_degree, boundary_degree, tau_degree+boundary_degree) == (1, 0, 1)
    if args.fault != "none":
        assert marker.exists(), "Requested hard-exit boundary was not exercised"
    mathematical = {
        "generic_only": True, "original_CM_computation": False,
        "genuine_nontrivial_common_factor": "u-alpha",
        "original_fraction": "(u^2-alpha^2)/(u-alpha)^2",
        "exact_polar_ideal": "(u-alpha)",
        "tau_polar_degree": tau_degree, "missing_sigma_boundary_degree": boundary_degree,
        "global_generic_polar_degree": tau_degree+boundary_degree,
        "two_charts": {
            chart: {"original_pair": S.spec(objects[0].final_name),
                    "column_reduction": S.spec(objects[1].final_name),
                    "complete_reverse_kernel": S.spec(objects[2].final_name),
                    "joint_Hermite_H_and_W": S.spec(objects[3].final_name),
                    "full_polynomial_product_check": objects[4]}
            for chart, objects in completed.items()},
        "forward_exact_Laurent_containment": forward,
        "backward_exact_Laurent_containment": backward,
        "closed_form_H_and_W_checked_over_generic_degree14_field": True,
        "all_complete_operation_plans_and_current_vector_hashes_verified": True,
        "generic_field_arithmetic_check": S.spec(packing_name)}
    M.save(args.output/"generic-mathematical-result.json", mathematical)
    print("GENERIC_POLAR_RESULT "+json.dumps({
        "sha256": sha(args.output/"generic-mathematical-result.json"),
        "generic_polar_degree": 1, "original_research_result_claimed": False}), flush=True)
    return 0


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("request", "module-helper", "field-core", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--worker", action="store_true")
    parser.add_argument("--fault", choices=MODES, default="none")
    args = parser.parse_args()
    if args.worker:
        return worker(args)
    request = json.loads(args.request.read_text())
    assert request["result"] == "R811-generic-polynomial-module-validation"
    assert request["mathematics_is_generic_not_original_CM"] is True
    assert request["test_script_sha256"] == sha(__file__)
    assert request["module_helper_sha256"] == sha(args.module_helper)
    assert request["field_core_sha256"] == sha(args.field_core) == FIELD_CORE_SHA
    args.output.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    outcomes = []
    baseline = None
    for mode in MODES:
        directory = args.output/mode
        command = [sys.executable, "-u", str(Path(__file__).resolve()), "--worker",
                   "--request", str(args.request.resolve()),
                   "--module-helper", str(args.module_helper.resolve()),
                   "--field-core", str(args.field_core.resolve()),
                   "--output", str(directory.resolve()), "--fault", mode]
        first = subprocess.run(command, check=False).returncode
        if mode == "none":
            assert first == 0
        else:
            assert first == 97, ("The designated hard exit did not occur", mode, first)
            assert (directory/"fault-fired.json").exists()
            second = subprocess.run(command, check=False).returncode
            assert second == 0, ("Continuation failed", mode, second)
        result_path = directory/"generic-mathematical-result.json"
        digest = sha(result_path)
        if baseline is None:
            baseline = digest
        assert digest == baseline, ("Resumed exact result differs from uninterrupted result", mode)
        fault = json.loads((directory/"fault-fired.json").read_text()) if mode != "none" else None
        outcomes.append({"mode": mode, "initial_exit_code": first,
                         "hard_exit": fault, "final_exact_result_sha256": digest,
                         "byte_identical_completed_mathematical_result": True})
    summary = {
        "result": request["result"], "complete": True, "source_sha256": sha(__file__),
        "module_helper_sha256": sha(args.module_helper), "field_core_sha256": FIELD_CORE_SHA,
        "generic_field": "Q(c,zeta), c^7=2", "generic_curve": "u^2=z",
        "generic_nontrivial_cancelled_polar_degree": 1,
        "cases": outcomes,
        "actual_hard_exit_boundaries": list(MODES[1:]),
        "original_b_model_beta_MA_MB_polar_divisor_eta_or_height_computed": False,
        "not_an_extra_gate_for_original_producer_activation": True,
        "seconds": time.monotonic()-started}
    target = args.output/"R811-generic-polynomial-module-validation-summary.json"
    target.write_text(json.dumps(summary, sort_keys=True, indent=2)+"\n")
    print("R811_GENERIC_MODULE_VALIDATION="+json.dumps(summary, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
