#!/usr/bin/env python3
# Source-comparison snippets retain the SciPy license.
# Copyright (c) 2001-2002 Enthought, Inc. 2003, SciPy Developers.
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
# 
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Pure source/integer-layout check; no NumPy/SciPy import, matrix or solver.

Read six frozen SciPy source files as text.  Import only the new foundation's
standard-library definitions, then call dimensions/column_segments only.
make_functions, _assemble_csc and all returned numerical functions are not called.
"""
from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import textwrap

FOUNDATION_SHA256 = "8e2bb061ef1fee94672601132cedb8ca7565d4006a327474f039f501e5f516cf"
BVP_SHA256 = "59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2"
CONSTRUCT_HEADER = (
    "def construct_global_jac(n, m, k, h, df_dy, df_dy_middle, df_dp,\n"
    "                         df_dp_middle, dbc_dya, dbc_dyb, dbc_dp):\n"
    "    \"\"\"Original arithmetic, followed by direct canonical CSC storage.\"\"\"\n"
)
CONSTRUCT_REPLACEMENTS = (
    (
        "    values = np.hstack((dPhi_dy_0.ravel(), dPhi_dy_1.ravel(), dbc_dya.ravel(),\n"
        "                        dbc_dyb.ravel()))\n",
        "    # Preserve the first hstack\'s pre-parameter-update boundary snapshot.\n"
        "    dbc_dya = dbc_dya.copy()\n"
        "    dbc_dyb = dbc_dyb.copy()\n"
        "    dPhi_dp = None\n",
    ),
    ("        values = np.hstack((values, dPhi_dp.ravel(), dbc_dp.ravel()))\n", ""),
    (
        "    J = coo_matrix((values, (i_jac, j_jac)))\n"
        "    return csc_matrix(J)\n",
        "    return _assemble_csc(np, csc_matrix, get_index_dtype, n, m, k,\n"
        "                         dPhi_dy_0, dPhi_dy_1, dPhi_dp,\n"
        "                         dbc_dya, dbc_dyb, dbc_dp)\n",
    ),
)
PREPARE_REPLACEMENTS = (
    ("    i_jac, j_jac = compute_jac_indices(n, m, k)\n", ""),
    (
        "return construct_global_jac(n, m, k, i_jac, j_jac, h, df_dy,",
        "return construct_global_jac(n, m, k, h, df_dy,",
    ),
)


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def no_scientific_imports():
    bad = [name for name in sys.modules
           if name == "numpy" or name.startswith("numpy.")
           or name == "scipy" or name.startswith("scipy.")]
    require(not bad, "scientific module already imported: " + repr(bad[:5]))


def find_function(container, name):
    matches = [node for node in container.body
               if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
               and node.name == name]
    require(len(matches) == 1, "missing/ambiguous function: " + name)
    return matches[0]


def function_text(source, node):
    lines = source.splitlines(keepends=True)
    return textwrap.dedent("".join(lines[node.lineno - 1:node.end_lineno])).rstrip() + "\n"


def replace_once(source, before, after):
    require(source.count(before) == 1, "source replacement is not unique: " + before[:60])
    return source.replace(before, after, 1)


def source_checks(original, foundation):
    old_tree = ast.parse(original)
    new_tree = ast.parse(foundation)
    factory = find_function(new_tree, "make_functions")
    old_construct = function_text(original, find_function(old_tree, "construct_global_jac"))
    old_prepare = function_text(original, find_function(old_tree, "prepare_sys"))
    new_construct = function_text(foundation, find_function(factory, "construct_global_jac"))
    new_prepare = function_text(foundation, find_function(factory, "prepare_sys"))
    marker = "    df_dy = np.transpose(df_dy, (2, 0, 1))\n"
    require(old_construct.count(marker) == 1, "old arithmetic start is not unique")
    expected = old_construct[old_construct.index(marker):]
    for before, after in CONSTRUCT_REPLACEMENTS:
        expected = replace_once(expected, before, after)
    expected = CONSTRUCT_HEADER + expected
    require(expected == new_construct, "complete construct function replay differs")
    expected_prepare = old_prepare
    for before, after in PREPARE_REPLACEMENTS:
        expected_prepare = replace_once(expected_prepare, before, after)
    require(expected_prepare == new_prepare, "complete prepare_sys replay differs")
    require(ast.dump(ast.parse(expected), include_attributes=False)
            == ast.dump(ast.parse(new_construct), include_attributes=False),
            "construct AST differs")
    require(ast.dump(ast.parse(expected_prepare), include_attributes=False)
            == ast.dump(ast.parse(new_prepare), include_attributes=False),
            "prepare_sys AST differs")
    require(new_construct.count("df_dp_middle +=") == 1,
            "parameter midpoint update must occur exactly once")
    require("compute_jac_indices(" not in foundation and "coo_matrix(" not in foundation
            and "np.hstack(" not in foundation,
            "old global COO/hstack construction remains")

    allowed_imports = {"__future__", "hashlib", "operator", "pathlib", "types",
                       "typing", "marshal"}
    for node in new_tree.body:
        if isinstance(node, ast.Import):
            require(all(alias.name in allowed_imports for alias in node.names),
                    "non-standard top-level import")
        elif isinstance(node, ast.ImportFrom):
            require(node.module in allowed_imports, "non-standard top-level import")
        elif isinstance(node, ast.Expr):
            require(isinstance(node.value, ast.Constant) and isinstance(node.value.value, str),
                    "unexpected top-level expression")
        elif isinstance(node, ast.Assign):
            require(all(isinstance(target, ast.Name) for target in node.targets),
                    "top-level attribute mutation")
            require(not any(isinstance(child, ast.Call) for child in ast.walk(node.value)),
                    "top-level call in assignment")
        else:
            require(isinstance(node, (ast.FunctionDef, ast.ClassDef)),
                    "unexpected top-level statement")
    for node in ast.walk(new_tree):
        if isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name):
                    require(target.value.id not in {"backend", "_base", "_coo", "_csc",
                                                    "_compressed", "_sputils", "scipy"},
                            "installation/mutation of original namespace")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            require(node.func.id not in {"setattr", "exec", "eval"},
                    "dynamic installation/evaluation in foundation")
    assembler = function_text(foundation, find_function(new_tree, "_assemble_csc"))
    require("index_dtype = get_index_dtype(maxval=max(size, stored))" in assembler,
            "original dtype selector not used with full bounds")
    require("for column, kind, block, component, first_row, count in column_segments(n, m, k):"
            in assembler, "assembler is not consuming the checked segment generator")
    require("result.has_sorted_indices = True" in assembler
            and "result.has_canonical_format = True" in assembler,
            "canonical storage flags absent")
    return {
        "construct_text_replay": True,
        "prepare_text_replay": True,
        "construct_ast_replay": True,
        "prepare_ast_replay": True,
        "construct_replacements": len(CONSTRUCT_REPLACEMENTS),
        "prepare_replacements": len(PREPARE_REPLACEMENTS),
        "original_construct_sha256": sha256(old_construct.encode()),
        "original_prepare_sha256": sha256(old_prepare.encode()),
        "new_construct_sha256": sha256(new_construct.encode()),
        "new_prepare_sha256": sha256(new_prepare.encode()),
        "parameter_midpoint_update_count": 1,
        "old_global_coo_construction_present": False,
    }


def old_coo_records(n, m, k):
    """Independent row-major block order of the original compute_jac_indices.

    Records are integer coordinates and unique symbolic block-entry names.
    They are not floating data or sparse/dense matrix objects.
    """
    records = []
    for interval in range(m - 1):
        for row in range(n):
            for component in range(n):
                records.append((interval * n + component, interval * n + row,
                                ("A", interval, row, component)))
    for interval in range(m - 1):
        for row in range(n):
            for component in range(n):
                records.append(((interval + 1) * n + component, interval * n + row,
                                ("B", interval, row, component)))
    boundary = (m - 1) * n
    for row in range(n + k):
        for component in range(n):
            records.append((component, boundary + row, ("D", 0, row, component)))
    for row in range(n + k):
        for component in range(n):
            records.append(((m - 1) * n + component, boundary + row,
                            ("E", 0, row, component)))
    for interval in range(m - 1):
        for row in range(n):
            for component in range(k):
                records.append((m * n + component, interval * n + row,
                                ("C", interval, row, component)))
    for row in range(n + k):
        for component in range(k):
            records.append((m * n + component, boundary + row,
                            ("F", 0, row, component)))
    return records


def from_segments(segments):
    records = []
    for column, kind, block, component, first_row, count in segments:
        for row in range(count):
            records.append((column, first_row + row, (kind, block, row, component)))
    return records


def assert_layout(n, m, k, records):
    size = n * m + k
    stored = (2 * n + k) * size
    expected = sorted(old_coo_records(n, m, k), key=lambda row: (row[0], row[1]))
    require(len(expected) == stored and len(records) == stored, "stored count differs")
    require(len({(col, row) for col, row, tag in expected}) == stored,
            "original pattern contains duplicate coordinates")
    require(records == expected, "canonical records differ from independently sorted COO")
    indptr = [0]
    offset = 0
    for column in range(size):
        start = offset
        last_row = -1
        while offset < stored and records[offset][0] == column:
            row = records[offset][1]
            require(0 <= row < size and row > last_row, "row order/range failure")
            last_row = row
            offset += 1
        require(offset > start, "empty column in required pattern")
        indptr.append(offset)
    require(offset == stored and len(indptr) == size + 1, "indptr extent failure")
    require(indptr[0] == 0 and indptr[-1] == stored, "indptr endpoints failure")
    return {"n": n, "m": m, "k": k, "size": size, "stored": stored,
            "indptr_entries": len(indptr), "canonical": True}


def integer_checks(module):
    cases = []
    for n in (1, 2, 5, 43):
        for m in (2, 3, 7):
            for k in (0, 1, 14):
                got = module.dimensions(n, m, k)
                require(got == (n, m, k, n * m + k, (2 * n + k) * (n * m + k)),
                        "dimension formula mismatch")
                cases.append(assert_layout(n, m, k, from_segments(module.column_segments(n, m, k))))
    invalid = ((True, 2, 0), (1, False, 0), (1, 2, True), (0, 2, 0),
               (1, 1, 0), (1, 2, -1), (1.0, 2, 0), (1, "2", 0))
    for args in invalid:
        try:
            module.dimensions(*args)
        except (TypeError, ValueError):
            pass
        else:
            raise AssertionError("invalid integer dimensions accepted: " + repr(args))

    correct = from_segments(module.column_segments(2, 3, 1))
    malformed = []
    malformed.append(correct[1:])
    malformed.append(correct[:-1])
    changed = copy.deepcopy(correct)
    column, row, tag = changed[0]
    changed[0] = (column, row + 1, tag)
    malformed.append(changed)
    changed = copy.deepcopy(correct)
    column, row, tag = changed[-1]
    changed[-1] = (column - 1, row, tag)
    malformed.append(changed)
    changed = copy.deepcopy(correct)
    column, row, tag = changed[0]
    changed[0] = (column, row, ("B",) + tag[1:])
    malformed.append(changed)
    for records in malformed:
        try:
            assert_layout(2, 3, 1, records)
        except AssertionError:
            pass
        else:
            raise AssertionError("malformed symbolic layout accepted")

    large = []
    for m in (5047, 6344, 6500):
        n, m, k, size, stored = module.dimensions(43, m, 14)
        require(stored == 100 * size, "W14 count factor mismatch")
        large.append({
            "n": n, "m": m, "k": k, "size": size, "stored": stored,
            "float64_final_data_bytes": 8 * stored,
            "two_old_int64_coo_index_bytes": 16 * stored,
            "direct_csc_bytes_if_int32": 12 * stored + 4 * (size + 1),
        })
    limit = 2**31 - 1
    before_m = (limit // 100 - 14) // 43
    before = module.dimensions(43, before_m, 14)
    after = module.dimensions(43, before_m + 1, 14)
    require(before[-1] <= limit < after[-1], "32-bit length threshold mismatch")
    return {
        "small_cases": cases,
        "invalid_dimension_cases_rejected": len(invalid),
        "malformed_symbolic_layouts_rejected": len(malformed),
        "large_integer_counts_only": large,
        "index_dtype_boundary": {
            "int32_max": limit,
            "before_m": before_m, "before_stored": before[-1],
            "after_m": before_m + 1, "after_stored": after[-1],
            "actual_numpy_scipy_dtype_call": False,
            "non_four_byte_intc": "pinned original get_index_dtype returns int64",
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--foundation", type=Path,
                        default=Path(__file__).with_name("db6f-prefix-direct-csc-foundation-v2.py"))
    parser.add_argument("--scipy-source-root", type=Path, required=True,
                        help="directory containing integrate/_bvp.py and sparse/*.py; read as text only")
    parser.add_argument("--out", type=Path,
                        help="optional new small JSON report; an existing file is rejected")
    args = parser.parse_args()
    no_scientific_imports()
    if args.out is not None:
        require(not args.out.exists(), "refuse existing output report")
    foundation_path = args.foundation.resolve()
    raw = foundation_path.read_bytes()
    require(sha256(raw) == FOUNDATION_SHA256, "foundation SHA mismatch")
    foundation = raw.decode("utf-8")
    # Parse before importing; do not execute any external scientific source.
    ast.parse(foundation)
    old_bytecode_flag = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    name = "_db6f_checked_direct_csc_definitions"
    require(name not in sys.modules, "checker namespace already in use")
    try:
        spec = importlib.util.spec_from_file_location(name, foundation_path)
        require(spec is not None and spec.loader is not None, "cannot load foundation definitions")
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        no_scientific_imports()
        sources = []
        bvp_text = None
        for module_name, expected in sorted(module.SCIPY_SOURCE_SHA256.items()):
            parts = module_name.split(".")[1:]
            path = args.scipy_source_root.joinpath(*parts).with_suffix(".py").resolve()
            contents = path.read_bytes()
            require(sha256(contents) == expected, "frozen source mismatch: " + module_name)
            sources.append({"module": module_name, "file": str(path),
                            "bytes": len(contents), "sha256": expected})
            if module_name == "scipy.integrate._bvp":
                require(expected == BVP_SHA256, "BVP identity changed")
                bvp_text = contents.decode("utf-8")
        require(bvp_text is not None, "BVP text missing")
        replay = source_checks(bvp_text, foundation)
        integers = integer_checks(module)
        no_scientific_imports()
    finally:
        sys.modules.pop(name, None)
        sys.dont_write_bytecode = old_bytecode_flag
    report = {
        "schema": "db6f-direct-canonical-csc-source-integer-check-v1",
        "status": "PASS_SOURCE_AND_INTEGER_LAYOUT_ONLY",
        "scope": "no scientific import; no factory, matrix, LU, linear solve or BVP",
        "checker": {"file": str(Path(__file__).resolve()),
                    "sha256": sha256(Path(__file__).read_bytes())},
        "foundation": {"file": str(foundation_path), "bytes": len(raw),
                       "sha256": FOUNDATION_SHA256},
        "frozen_sources": sources,
        "source_replay": replay,
        "integer_layout": integers,
        "factory_called": False,
        "matrix_calls": 0,
        "solver_calls": 0,
        "actual_sparse_byte_replay": "not performed",
        "actual_original_splu_trajectory": "not performed",
        "runtime_callback_binding_gate": "not invoked",
        "complete_new_entry_authorized": False,
    }
    text = json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n"
    require(len(text.encode()) < 100000, "report unexpectedly large")
    if args.out is not None:
        with args.out.open("x", encoding="utf-8") as handle:
            handle.write(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
