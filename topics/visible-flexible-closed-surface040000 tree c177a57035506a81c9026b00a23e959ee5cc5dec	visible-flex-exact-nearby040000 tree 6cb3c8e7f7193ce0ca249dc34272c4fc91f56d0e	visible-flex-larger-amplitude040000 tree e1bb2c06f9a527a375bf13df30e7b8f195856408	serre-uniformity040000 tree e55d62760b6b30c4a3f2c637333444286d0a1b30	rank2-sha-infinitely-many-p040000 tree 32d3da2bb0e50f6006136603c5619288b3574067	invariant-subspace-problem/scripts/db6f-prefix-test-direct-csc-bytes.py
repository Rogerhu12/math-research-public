#!/usr/bin/env python3
"""Future small synthetic CSC byte comparison.  SAVED, NOT EXECUTED by author.

This test imports NumPy/SciPy only when run explicitly.  It calls the pinned
official construct_global_jac as the oracle and the new functions-only factory.
It never installs, monkeypatches, calls SuperLU, or invokes a BVP/DN/RK solver.
No research checkpoint, geometry or tail data is read.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
from types import CodeType, FunctionType

FOUNDATION_SHA256 = "8e2bb061ef1fee94672601132cedb8ca7565d4006a327474f039f501e5f516cf"
BVP_SHA256 = "59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2"
ORDER = ("h", "df_dy", "df_dy_middle", "df_dp", "df_dp_middle",
         "dbc_dya", "dbc_dyb", "dbc_dp")


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def json_digest(value):
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return sha256(text.encode())


def file_record(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return {"file": str(path), "bytes": len(raw), "sha256": sha256(raw)}


def array_record(array):
    if array is None:
        return None
    return {
        "shape": list(array.shape),
        "strides": list(array.strides),
        "dtype": array.dtype.str,
        "bytes_C_sha256": sha256(array.tobytes(order="C")),
        "nbytes": int(array.nbytes),
    }


def checked_original_function(module, source, name):
    """Verify the actually called original, not merely a disk file hash."""
    compiled = compile(source, str(module.__file__), "exec", dont_inherit=True)
    codes = [item for item in compiled.co_consts
             if isinstance(item, CodeType) and item.co_name == name]
    require(len(codes) == 1, "ambiguous original function " + name)
    function = getattr(module, name)
    require(isinstance(function, FunctionType), "original is not a Python function")
    require(function.__code__ == codes[0] and function.__globals__ is vars(module),
            "original runtime code/namespace differs: " + name)
    require(function.__defaults__ is None and function.__kwdefaults__ is None
            and function.__closure__ is None,
            "original runtime defaults/closure differs: " + name)
    return function


@dataclass(frozen=True)
class View:
    root: str
    shape: tuple
    offset: int
    strides: tuple


def contiguous_strides(shape):
    stride = 1
    answer = []
    for length in reversed(shape):
        answer.append(stride)
        stride *= length
    return tuple(reversed(answer))


def shapes_for(n, m, k):
    return {
        "h": (m - 1,),
        "df_dy": (n, n, m),
        "df_dy_middle": (n, n, m - 1),
        "df_dp": (n, k, m) if k else None,
        "df_dp_middle": (n, k, m - 1) if k else None,
        "dbc_dya": (n + k, n),
        "dbc_dyb": (n + k, n),
        "dbc_dp": (n + k, k) if k else None,
    }


def make_values(np, count, dtype, ordinal, zeros):
    """Deterministic dyadic recipe; no RNG and no stored numerical fixture."""
    dtype = np.dtype(dtype)
    require(dtype.kind in ("f", "c"), "ordinary real/complex floating dtype required")
    array = np.empty(count, dtype=dtype)
    integers = np.arange(count, dtype=np.int64)
    if zeros:
        real = np.copysign(np.zeros(count, dtype=np.float64),
                           np.where((integers + ordinal) % 2 == 0, -1.0, 1.0))
        imaginary = np.copysign(np.zeros(count, dtype=np.float64),
                                np.where((integers + ordinal + 1) % 2 == 0, -1.0, 1.0))
    else:
        real = ((integers + ordinal) % 31 + 1).astype(np.float64) / 64
        imaginary = -((3 * integers + ordinal + 7) % 29 + 1).astype(np.float64) / 128
    if dtype.kind == "c":
        # Assign components separately so that complex signed zeros are not
        # changed while forming a Python complex expression such as a+1j*b.
        array.real[:] = real
        array.imag[:] = imaginary
    else:
        array[:] = real
    require(bool(np.isfinite(array).all()), "nonfinite synthetic seed")
    return array


def addresses(view):
    """Small pure integer bounds/unique-address check for an input view."""
    result = [view.offset]
    for length, stride in zip(view.shape, view.strides):
        result = [base + index * stride for base in result for index in range(length)]
    return result


class Seed:
    def __init__(self, np, spec):
        self.np = np
        self.spec = spec
        self.roots = {}
        self.views = {}
        n, m, k = spec["n"], spec["m"], spec["k"]
        shapes = shapes_for(n, m, k)
        types = spec.get("types", {})
        base_type = spec.get("dtype", "float64")
        zeros = bool(spec.get("zeros", False))
        for ordinal, name in enumerate(ORDER):
            shape = shapes[name]
            if shape is None:
                self.views[name] = None
                continue
            dtype = "float64" if name == "h" else types.get(name, base_type)
            root_name = "separate_" + name
            root = make_values(np, math.prod(shape), dtype, ordinal, zeros and name != "h")
            if name == "h":
                root[:] = (np.arange(m - 1, dtype=np.float64) + 1) / 16
            self.roots[root_name] = root
            self.views[name] = View(root_name, shape, 0, contiguous_strides(shape))

        mode = spec.get("alias")
        if mode:
            require((n, m, k) in ((2, 4, 1), (2, 3, 2)), "unreviewed alias dimensions")
            common_type = types.get("df_dp_middle", base_type)
            require(all(types.get(name, base_type) == common_type
                        for name in ("dbc_dya", "dbc_dyb", "dbc_dp")),
                    "alias views must share one ordinary dtype")
            if mode == "full_boundary":
                require((n, m, k) == (2, 4, 1), "full alias shape")
                size = 6
                aliases = {
                    "df_dp_middle": ((2, 1, 3), 0, (3, 3, 1)),
                    "dbc_dya": ((3, 2), 0, (2, 1)),
                    "dbc_dyb": ((3, 2), 0, (2, 1)),
                }
            elif mode == "partial_boundary_and_F":
                require((n, m, k) == (2, 3, 2), "partial alias shape")
                size = 20
                aliases = {
                    "df_dp_middle": ((2, 2, 2), 4, (4, 2, 1)),
                    "dbc_dya": ((4, 2), 0, (2, 1)),
                    "dbc_dyb": ((4, 2), 8, (2, 1)),
                    "dbc_dp": ((4, 2), 6, (2, 1)),
                }
            elif mode == "negative_and_fortran":
                require((n, m, k) == (2, 4, 1), "strided alias shape")
                size = 12
                aliases = {
                    "df_dp_middle": ((2, 1, 3), 5, (3, 3, -1)),
                    "dbc_dya": ((3, 2), 1, (2, -1)),
                    "dbc_dyb": ((3, 2), 6, (1, 3)),
                    "dbc_dp": ((3, 1), 3, (1, 1)),
                }
            elif mode == "node_and_boundary":
                require((n, m, k) == (2, 4, 1), "node alias shape")
                require(types.get("df_dp", base_type) == common_type, "node alias dtype")
                size = 12
                aliases = {
                    "df_dp": ((2, 1, 4), 0, (4, 4, 1)),
                    "df_dp_middle": ((2, 1, 3), 2, (3, 3, 1)),
                    "dbc_dya": ((3, 2), 2, (2, 1)),
                    "dbc_dyb": ((3, 2), 5, (2, 1)),
                    "dbc_dp": ((3, 1), 9, (1, 1)),
                }
            else:
                raise AssertionError("unknown alias recipe")
            root_name = "shared_parameter_boundary"
            # Monotone small real seed in these ranges ensures the real alias
            # cases have nonzero node differences and a detectable update.
            root = make_values(np, size, common_type, 0, False)
            self.roots[root_name] = root
            for name, (shape, offset, strides) in aliases.items():
                require(shape == shapes[name], "alias view shape differs from callback contract")
                self.views[name] = View(root_name, shape, offset, strides)

        used = {view.root for view in self.views.values() if view is not None}
        self.roots = {name: root for name, root in self.roots.items() if name in used}
        for view in self.views.values():
            if view is None:
                continue
            offsets = addresses(view)
            require(len(offsets) == math.prod(view.shape) and len(set(offsets)) == len(offsets),
                    "self-overlapping view is outside this test contract")
            require(min(offsets) >= 0 and max(offsets) < self.roots[view.root].size,
                    "view outside its seed buffer")
        for root in self.roots.values():
            root.flags.writeable = False
        self.initial_seed_digest = self.digest()

    def digest(self):
        return json_digest({
            "roots": {name: array_record(root) for name, root in sorted(self.roots.items())},
            "views": {name: None if view is None else {
                "root": view.root, "shape": list(view.shape),
                "offset_elements": view.offset, "strides_elements": list(view.strides),
            } for name, view in sorted(self.views.items())},
        })

    def instantiate(self):
        roots = {name: root.copy() for name, root in self.roots.items()}
        arrays = {}
        for name, view in self.views.items():
            if view is None:
                arrays[name] = None
                continue
            root = roots[view.root]
            require(root.flags.writeable, "fresh independent root must be writable")
            array = self.np.ndarray(
                shape=view.shape, dtype=root.dtype, buffer=root,
                offset=view.offset * root.dtype.itemsize,
                strides=tuple(value * root.dtype.itemsize for value in view.strides),
            )
            require(type(array) is self.np.ndarray and array.flags.writeable,
                    "test view must be an ordinary writable ndarray")
            arrays[name] = array
        return {"roots": roots, "arrays": arrays}


def snapshot(np, cohort):
    arrays = cohort["arrays"]
    names = [name for name in ORDER if arrays[name] is not None]
    alias_pairs = []
    for index, left in enumerate(names):
        for right in names[index + 1:]:
            if np.shares_memory(arrays[left], arrays[right]):
                alias_pairs.append([left, right])
    return {
        "roots": {name: array_record(root) for name, root in sorted(cohort["roots"].items())},
        "views": {name: array_record(arrays[name]) for name in ORDER},
        "alias_pairs": alias_pairs,
    }


def independent_cohorts(np, seed, original, direct):
    for left in original["roots"].values():
        for right in direct["roots"].values():
            require(not np.shares_memory(left, right), "the two runs share a mutable buffer")
        for right in seed.roots.values():
            require(not np.shares_memory(left, right), "oracle shares a seed buffer")
    for left in direct["roots"].values():
        for right in seed.roots.values():
            require(not np.shares_memory(left, right), "new run shares a seed buffer")
    before_original = snapshot(np, original)
    before_direct = snapshot(np, direct)
    require(before_original == before_direct, "independent alias layouts/initial bytes differ")
    return before_original


def signed_zero_counts(np, data):
    real = data.real
    answer = {
        "whole_numeric_zero_count": int(np.count_nonzero(data == 0)),
        "negative_real_zero_count": int(np.count_nonzero((real == 0) & np.signbit(real))),
    }
    if data.dtype.kind == "c":
        imaginary = data.imag
        answer["negative_imaginary_zero_count"] = int(
            np.count_nonzero((imaginary == 0) & np.signbit(imaginary)))
    return answer


def compare_csc(np, original, direct, n, m, k):
    size = n * m + k
    stored = (2 * n + k) * size
    require(original.format == direct.format == "csc", "not CSC")
    require(original.shape == direct.shape == (size, size), "matrix shape differs")
    require(original.nnz == direct.nnz == stored, "structural zero/entry count differs")
    require(bool(original.has_sorted_indices) and bool(direct.has_sorted_indices),
            "sorted-index flag failed")
    require(bool(original.has_canonical_format) and bool(direct.has_canonical_format),
            "canonical flag failed")
    buffers = {}
    for name in ("data", "indices", "indptr"):
        left, right = getattr(original, name), getattr(direct, name)
        require(left.dtype == right.dtype and left.dtype.str == right.dtype.str,
                name + " dtype differs")
        require(left.shape == right.shape and left.strides == right.strides,
                name + " array layout differs")
        require(left.tobytes(order="C") == right.tobytes(order="C"),
                name + " raw bytes differ")
        buffers[name] = array_record(left)
    require(bool(np.isfinite(original.data).all()), "oracle produced nonfinite fixture values")
    zero_counts = signed_zero_counts(np, original.data)
    require(zero_counts == signed_zero_counts(np, direct.data), "signed-zero counts differ")
    return {"shape": [size, size], "stored": stored, "buffers": buffers,
            "signed_zero_counts": zero_counts, "canonical": True}


def specs():
    return [
        {"id": "real64_normal", "n": 2, "m": 4, "k": 1, "dtype": "float64",
         "expected_data_dtype": "float64", "require_mid_change": True},
        {"id": "real64_signed_zero", "n": 2, "m": 3, "k": 1, "dtype": "float64",
         "zeros": True, "expected_data_dtype": "float64", "require_negative_real_zero": True},
        {"id": "float32_k0_m2", "n": 3, "m": 2, "k": 0, "dtype": "float32",
         "expected_data_dtype": "float32"},
        {"id": "complex64_k0", "n": 2, "m": 3, "k": 0, "dtype": "complex64",
         "expected_data_dtype": "complex64"},
        {"id": "complex128_signed_zero", "n": 2, "m": 3, "k": 1, "dtype": "complex128",
         "zeros": True, "expected_data_dtype": "complex128",
         "require_negative_real_zero": True, "require_negative_imaginary_zero": True},
        {"id": "float32_parameter_promotes_to_float64", "n": 2, "m": 3, "k": 1,
         "dtype": "float32", "expected_data_dtype": "float64", "require_mid_change": True},
        {"id": "real32_boundary64_parameter_complex128", "n": 2, "m": 4, "k": 1,
         "dtype": "float32", "types": {
             "dbc_dya": "float64", "dbc_dyb": "float64",
             "df_dp": "complex128", "df_dp_middle": "complex128", "dbc_dp": "complex128"},
         "expected_data_dtype": "complex128", "require_mid_change": True},
        {"id": "complex64_mixed_boundary_parameter128", "n": 2, "m": 3, "k": 2,
         "dtype": "complex64", "types": {
             "dbc_dya": "float32", "df_dp": "complex128",
             "df_dp_middle": "complex128", "dbc_dp": "float64"},
         "expected_data_dtype": "complex128", "require_mid_change": True},
        {"id": "mixed_signed_zero", "n": 2, "m": 3, "k": 1, "dtype": "float32",
         "types": {"dbc_dya": "float64", "dbc_dyb": "float64",
                   "df_dp": "complex128", "df_dp_middle": "complex128", "dbc_dp": "complex128"},
         "zeros": True, "expected_data_dtype": "complex128",
         "require_negative_real_zero": True, "require_negative_imaginary_zero": True},
        {"id": "full_boundary_alias_real64", "n": 2, "m": 4, "k": 1,
         "dtype": "float64", "alias": "full_boundary", "require_mid_change": True,
         "expected_data_dtype": "float64"},
        {"id": "partial_boundary_F_alias_real64", "n": 2, "m": 3, "k": 2,
         "dtype": "float64", "alias": "partial_boundary_and_F", "require_mid_change": True,
         "expected_data_dtype": "float64"},
        {"id": "negative_Fortran_alias_real64", "n": 2, "m": 4, "k": 1,
         "dtype": "float64", "alias": "negative_and_fortran", "require_mid_change": True,
         "expected_data_dtype": "float64"},
        {"id": "full_boundary_alias_complex128", "n": 2, "m": 4, "k": 1,
         "dtype": "complex128", "alias": "full_boundary", "require_mid_change": True,
         "expected_data_dtype": "complex128"},
        {"id": "node_and_boundary_alias_real64", "n": 2, "m": 4, "k": 1,
         "dtype": "float64", "alias": "node_and_boundary", "require_mid_change": True,
         "expected_data_dtype": "float64"},
        {"id": "W14_dimensions_two_nodes", "n": 43, "m": 2, "k": 14,
         "dtype": "float64", "expected_data_dtype": "float64", "require_mid_change": True},
    ]


def run_case(np, spec, original_construct, original_indices, direct_construct, counts):
    n, m, k = spec["n"], spec["m"], spec["k"]
    require(n >= 1 and m >= 2 and k >= 0, "invalid reviewed fixture dimensions")
    require(n * m + k <= 128 and (2 * n + k) * (n * m + k) <= 20000,
            "fixture exceeds the deliberately small matrix budget")
    seed = Seed(np, spec)
    original = seed.instantiate()
    direct = seed.instantiate()
    before = independent_cohorts(np, seed, original, direct)
    arrays_original, arrays_direct = original["arrays"], direct["arrays"]
    # Saved before either call; used only to verify that alias fixtures really
    # exercise the original boundary-before-parameter-update contract.
    D_before = arrays_original["dbc_dya"].copy()
    E_before = arrays_original["dbc_dyb"].copy()
    i_jac, j_jac = original_indices(n, m, k)
    counts["original_construct_attempts"] += 1
    oracle = original_construct(n, m, k, i_jac, j_jac,
                                *(arrays_original[name] for name in ORDER))
    counts["original_construct_completed"] += 1
    counts["new_construct_attempts"] += 1
    candidate = direct_construct(n, m, k, *(arrays_direct[name] for name in ORDER))
    counts["new_construct_completed"] += 1
    matrix = compare_csc(np, oracle, candidate, n, m, k)
    require(oracle.data.dtype == np.dtype(spec["expected_data_dtype"]),
            "fixture did not exercise its declared original dtype outcome")
    after_original = snapshot(np, original)
    after_direct = snapshot(np, direct)
    require(after_original == after_direct,
            "input root/view bytes or alias side effects differ after the two calls")
    require(seed.digest() == seed.initial_seed_digest, "immutable seed changed")
    changed = [name for name in ORDER if before["views"][name] != after_original["views"][name]]
    if spec.get("require_mid_change"):
        require("df_dp_middle" in changed, "fixture did not exercise a nonzero midpoint update")
    if spec.get("alias"):
        require("dbc_dya" in changed and "dbc_dyb" in changed,
                "alias fixture did not actually change both caller-visible boundary views")
        start = (m - 1) * n
        oracle_D = oracle[start:, :n].toarray()
        oracle_E = oracle[start:, (m - 1) * n:m * n].toarray()
        # This is a check of the original oracle's boundary snapshot, not a
        # reconstruction of the new canonical enumeration.
        require(oracle_D.tobytes(order="C")
                == D_before.astype(oracle.data.dtype).tobytes(order="C"),
                "original D snapshot contract was not exercised")
        require(oracle_E.tobytes(order="C")
                == E_before.astype(oracle.data.dtype).tobytes(order="C"),
                "original E snapshot contract was not exercised")
    if spec.get("zeros"):
        require(int(np.count_nonzero(oracle.data)) == 2 * n * (m - 1),
                "zero fixture contains unexpected nonzero entries")
    zero_counts = matrix["signed_zero_counts"]
    if spec.get("require_negative_real_zero"):
        require(zero_counts["negative_real_zero_count"] > 0,
                "fixture lost all negative real zeros")
    if spec.get("require_negative_imaginary_zero"):
        require(zero_counts.get("negative_imaginary_zero_count", 0) > 0,
                "fixture lost all negative imaginary zeros")
    return {
        "id": spec["id"], "spec": spec,
        "seed_sha256": seed.initial_seed_digest,
        "initial_cohort_sha256": json_digest(before),
        "post_cohort_sha256": json_digest(after_original),
        "post_cohort_exact_equal": True,
        "all_input_views_compared": list(ORDER),
        "alias_pairs": before["alias_pairs"],
        "changed_input_views": changed,
        "independent_mutable_runs": True,
        "immutable_seed_unchanged": True,
        "matrix": matrix,
    }


def execute(args, report):
    report["stage"] = "load_source_bindings"
    import numpy as np
    import scipy
    from scipy.integrate import _bvp
    from scipy.sparse import coo_matrix, csc_matrix

    original_file = file_record(_bvp.__file__)
    require(original_file["sha256"] == BVP_SHA256, "official BVP source SHA differs")
    original_text = Path(_bvp.__file__).read_text(encoding="utf-8")
    original_construct = checked_original_function(_bvp, original_text, "construct_global_jac")
    original_indices = checked_original_function(_bvp, original_text, "compute_jac_indices")
    require(_bvp.np is np and _bvp.coo_matrix is coo_matrix and _bvp.csc_matrix is csc_matrix,
            "original sparse/NumPy runtime namespace differs")

    foundation_path = args.foundation.resolve()
    foundation = file_record(foundation_path)
    require(foundation["sha256"] == FOUNDATION_SHA256, "foundation v2 SHA differs")
    watched = {name: getattr(_bvp, name) for name in (
        "prepare_sys", "construct_global_jac", "compute_jac_indices", "solve_newton",
        "collocation_fun", "estimate_fun_jac", "estimate_bc_jac", "stacked_matmul",
        "np", "coo_matrix", "csc_matrix")}
    module_name = "_db6f_direct_csc_small_byte_test"
    require(module_name not in sys.modules, "test module name already present")
    previous_bytecode = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        module_spec = importlib.util.spec_from_file_location(module_name, foundation_path)
        require(module_spec is not None and module_spec.loader is not None, "cannot load foundation")
        module = importlib.util.module_from_spec(module_spec)
        sys.modules[module_name] = module
        module_spec.loader.exec_module(module)
        report["stage"] = "factory_identity_gate"
        functions = module.make_functions(_bvp)
        report["factory_provenance"] = functions.provenance
        report["factory_provenance_is_precomparison_snapshot"] = True
        report["original_source"] = original_file
        report["foundation"] = foundation
        report["numpy_version"] = np.__version__
        report["scipy_version"] = scipy.__version__
        report["np_intc_itemsize"] = int(np.dtype(np.intc).itemsize)
        for name, function in watched.items():
            require(getattr(_bvp, name) is function, "factory installed or replaced " + name)
        for spec in specs():
            report["stage"] = "synthetic_case:" + spec["id"]
            result = run_case(np, spec, original_construct, original_indices,
                              functions.construct_global_jac, report["counts"])
            report["cases"].append(result)
            for name, function in watched.items():
                require(getattr(_bvp, name) is function, "case replaced original " + name)
        report["stage"] = "completed"
        report["status"] = "PASS_SMALL_SYNTHETIC_CSC_BYTES_AND_ALIAS_EFFECTS"
        report["original_function_bindings_unchanged"] = True
    finally:
        sys.modules.pop(module_name, None)
        sys.dont_write_bytecode = previous_bytecode


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--foundation", type=Path,
                        default=Path(__file__).with_name("db6f-prefix-direct-csc-foundation-v2.py"))
    parser.add_argument("--out", type=Path, required=True,
                        help="new small report path; existing output is refused before scientific imports")
    args = parser.parse_args()
    if args.out.exists():
        raise SystemExit("refuse existing report: " + str(args.out))
    report = {
        "schema": "db6f-direct-csc-small-byte-test-v1",
        "status": "STARTED_NOT_PASSED",
        "scope": "small synthetic matrices only; no research input, installation, SuperLU or solver",
        "stage": "preflight",
        "script": file_record(__file__),
        "counts": {
            "original_construct_attempts": 0, "original_construct_completed": 0,
            "new_construct_attempts": 0, "new_construct_completed": 0,
            "superlu_calls": 0, "linear_solve_calls": 0, "bvp_dn_rk_calls": 0,
        },
        "cases": [],
        "research_data_read": False,
        "future_complete_entry_approved": False,
    }
    code = 2
    try:
        execute(args, report)
        code = 0
    except Exception as exc:
        report["status"] = "FAILED_SYNTHETIC_OR_SOURCE_CHECK"
        report["error"] = {"type": type(exc).__name__, "message": str(exc)}
    report["script_return_code"] = code
    report["external_tool_exit_observation"] = "must be recorded independently by the actual launcher"
    text = json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n"
    if len(text.encode()) >= 100000:
        raise RuntimeError("report unexpectedly exceeds 100 KB; not writing a truncated report")
    with args.out.open("x", encoding="utf-8") as handle:
        handle.write(text)
    print(json.dumps({
        "status": report["status"], "stage": report["stage"],
        "completed_cases": len(report["cases"]), "script_return_code": code,
        "out": str(args.out),
    }, sort_keys=True))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
