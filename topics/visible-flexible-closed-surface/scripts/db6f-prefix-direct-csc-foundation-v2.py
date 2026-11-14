# Portions adapted from scipy/integrate/_bvp.py at pinned source SHA below.
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

"""Direct canonical CSC foundation for the frozen W14 collocation system.

Version 2 additionally snapshots D/E at the original first-hstack position.
Version 1 is preserved as an uninstalled historical source.

This module defines functions only.  Importing it does not import NumPy/SciPy,
install anything, allocate a matrix, or call a solver.  make_functions() is an
explicit later identity-validation/binding step; it also does not install.

The numerical arithmetic in the returned construct_global_jac and all callback
ordering in prepare_sys are copied from the pinned SciPy source.  The separate
storage assembler preserves structural zeros and canonical column/row order.
Actual NumPy/SciPy byte replay and any complete solver-entry review are pending.
"""
from __future__ import annotations

import hashlib
import operator
from pathlib import Path
from types import CodeType, FunctionType
import marshal
from typing import NamedTuple

ORIGINAL_BVP_SHA256 = "59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2"
SCIPY_SOURCE_SHA256 = {
    "scipy.integrate._bvp": ORIGINAL_BVP_SHA256,
    "scipy.sparse._coo": "95e4bcd796900894acea3256a7b5a4cab654427bb9fcb9f0e57ec9fb40dc6898",
    "scipy.sparse._compressed": "d8d847ceb10469b91dc2f64e2be7ec3af04e1a099db9fbb91fb32526f860dc0f",
    "scipy.sparse._sputils": "b1cdc32d7e49fab5add7ec14f0858321275186e083362e6cc2628f6fef5a641f",
    "scipy.sparse._csc": "88c462e71172169295fa8e1f7ff23d4a3c0037e847a7b6037e74c812ee236552",
    "scipy.sparse._base": "e6d70fd65f0378f198cdf0c83986aa3b477f87da47137037ef6056d42481fd1b",
}


class DirectCSCFunctions(NamedTuple):
    construct_global_jac: object
    prepare_sys: object
    provenance: dict


def dimensions(n, m, k):
    """Integer sizes only; no arrays and no numerical callbacks."""
    values = []
    for name, value in (("n", n), ("m", m), ("k", k)):
        if isinstance(value, bool):
            raise TypeError(name + " must be an integer, not bool")
        try:
            value = operator.index(value)
        except TypeError as exc:
            raise TypeError(name + " must be an integer") from exc
        values.append(int(value))
    n, m, k = values
    if n < 1 or m < 2 or k < 0:
        raise ValueError("need n >= 1, m >= 2, k >= 0")
    size = n * m + k
    stored = (2 * n + k) * size
    return n, m, k, size, stored


def column_segments(n, m, k):
    """Yield canonical (column, kind, block, component, first_row, count).

    A/B/C are the collocation blocks; D/E/F are the three boundary blocks.
    This generator retains O(1) integer state.  It never constructs the old
    length-stored COO row/column arrays or a list of all segments.
    """
    n, m, k, size, stored = dimensions(n, m, k)
    del size, stored
    boundary = (m - 1) * n
    for node in range(m):
        for component in range(n):
            column = node * n + component
            if node > 0:
                yield column, "B", node - 1, component, (node - 1) * n, n
            if node < m - 1:
                yield column, "A", node, component, node * n, n
            if node == 0:
                yield column, "D", 0, component, boundary, n + k
            if node == m - 1:
                yield column, "E", 0, component, boundary, n + k
    for component in range(k):
        column = m * n + component
        for interval in range(m - 1):
            yield column, "C", interval, component, interval * n, n
        yield column, "F", 0, component, boundary, n + k


def _assemble_csc(np, csc_matrix, get_index_dtype, n, m, k,
                  A, B, C, D, E, F):
    """Allocate only final sparse buffers and O(n+k) integer row templates.

    The first original hstack promoted A/B/D/E together.  The second, when
    k > 0, promoted that result with C/F.  Casting each base segment through
    base_dtype retains that intermediate conversion without allocating its
    old global values buffer.  In the actual W14 contract all are float64.
    """
    n, m, k, size, stored = dimensions(n, m, k)
    base_dtype = np.result_type(A, B, D, E)
    final_dtype = np.result_type(base_dtype, C, F) if k > 0 else base_dtype
    index_dtype = get_index_dtype(maxval=max(size, stored))
    data = np.empty(stored, dtype=final_dtype)
    indices = np.empty(stored, dtype=index_dtype)
    indptr = np.empty(size + 1, dtype=index_dtype)
    node_rows = np.arange(n, dtype=index_dtype)
    boundary_rows = np.arange(n + k, dtype=index_dtype)
    position = 0
    previous_column = -1
    for column, kind, block, component, first_row, count in column_segments(n, m, k):
        if column != previous_column:
            if column != previous_column + 1:
                raise RuntimeError("internal canonical column order failure")
            indptr[column] = position
            previous_column = column
        if kind == "A":
            piece = A[block, :, component].astype(base_dtype, copy=False)
        elif kind == "B":
            piece = B[block, :, component].astype(base_dtype, copy=False)
        elif kind == "D":
            piece = D[:, component].astype(base_dtype, copy=False)
        elif kind == "E":
            piece = E[:, component].astype(base_dtype, copy=False)
        elif kind == "C":
            piece = C[block, :, component]
        elif kind == "F":
            piece = F[:, component]
        else:
            raise RuntimeError("internal block kind failure")
        stop = position + count
        data[position:stop] = piece
        rows = node_rows if count == n else boundary_rows
        indices[position:stop] = first_row + rows
        position = stop
    if previous_column != size - 1 or position != stored:
        raise RuntimeError("internal CSC size failure")
    indptr[size] = position
    result = csc_matrix((data, indices, indptr), shape=(size, size), copy=False)
    # Each column was emitted in strictly increasing row order with no overlap.
    # No numerical zero was removed and no duplicate summation is required.
    result.has_sorted_indices = True
    result.has_canonical_format = True
    return result


def _same_literal(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, tuple):
        return len(a) == len(b) and all(_same_literal(x, y) for x, y in zip(a, b))
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(_same_literal(a[key], b[key]) for key in a)
    return a == b


def _verified_source(module):
    name = module.__name__
    if name not in SCIPY_SOURCE_SHA256:
        raise RuntimeError("unlisted source module: " + name)
    path = Path(module.__file__).resolve()
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != SCIPY_SOURCE_SHA256[name]:
        raise RuntimeError("source identity mismatch: " + name)
    text = raw.decode("utf-8")
    # Compile source only, never execute it.  Used to compare live callback code.
    code = compile(text, str(module.__file__), "exec", dont_inherit=True)
    return code, {"module": name, "file": str(path), "bytes": len(raw), "sha256": digest}


def _checked_function(module, module_code, names, defaults, kwdefaults=None):
    value = module
    code = module_code
    for name in names:
        value = getattr(value, name)
        matches = [x for x in code.co_consts if isinstance(x, CodeType) and x.co_name == name]
        if len(matches) != 1:
            raise RuntimeError("ambiguous compiled function identity: " + ".".join(names))
        code = matches[0]
    if not isinstance(value, FunctionType):
        raise RuntimeError("expected an original Python function: " + ".".join(names))
    if value.__code__ != code or value.__globals__ is not vars(module):
        raise RuntimeError("runtime function code/namespace mismatch: " + ".".join(names))
    if value.__closure__ is not None or not _same_literal(value.__kwdefaults__, kwdefaults):
        raise RuntimeError("unexpected original callback closure/kwdefaults")
    if not _same_literal(value.__defaults__, defaults):
        raise RuntimeError("runtime function defaults mismatch: " + ".".join(names))
    return value


def make_functions(backend):
    """Validate dependencies and return two new functions, without installation.

    No callback or matrix function is invoked here.  This factory deliberately
    does not read, replace, wrap, or call backend.solve_newton.  A future entry
    must separately bind its chosen original/release-LU Newton and W14 selector.
    """
    import numpy as np
    import scipy
    from scipy.sparse import csc_matrix
    from scipy.sparse import _base, _compressed, _coo, _csc, _sputils

    if backend.__name__ != "scipy.integrate._bvp":
        raise RuntimeError("expected scipy.integrate._bvp")
    modules = (backend, _base, _compressed, _coo, _csc, _sputils)
    compiled = {}
    sources = []
    for module in modules:
        code, record = _verified_source(module)
        compiled[module.__name__] = code
        sources.append(record)
    if backend.np is not np or _sputils.np is not np or _compressed.np is not np:
        raise RuntimeError("NumPy namespace identity mismatch")
    if backend.csc_matrix is not csc_matrix or csc_matrix is not _csc.csc_matrix:
        raise RuntimeError("CSC class identity mismatch")
    if backend.EPS != np.finfo(float).eps:
        raise RuntimeError("original finite-difference EPS mismatch")

    stacked_matmul = _checked_function(
        backend, compiled[backend.__name__], ("stacked_matmul",), None)
    collocation_fun = _checked_function(
        backend, compiled[backend.__name__], ("collocation_fun",), None)
    estimate_fun_jac = _checked_function(
        backend, compiled[backend.__name__], ("estimate_fun_jac",), (None,))
    estimate_bc_jac = _checked_function(
        backend, compiled[backend.__name__], ("estimate_bc_jac",), (None,))
    get_index_dtype = _checked_function(
        _sputils, compiled[_sputils.__name__], ("get_index_dtype",), ((), None, False))
    original_csc_init = _checked_function(
        _compressed, compiled[_compressed.__name__], ("_cs_matrix", "__init__"),
        (None, None, False), {"maxprint": None})
    if csc_matrix.__init__ is not original_csc_init:
        raise RuntimeError("CSC constructor runtime identity mismatch")
    original_check_format = _checked_function(
        _compressed, compiled[_compressed.__name__], ("_cs_matrix", "check_format"), (True,))
    original_prune = _checked_function(
        _compressed, compiled[_compressed.__name__], ("_cs_matrix", "prune"), None)
    original_index_method = _checked_function(
        _base, compiled[_base.__name__], ("_spbase", "_get_index_dtype"), ((), None, False))
    original_swap = _checked_function(
        _csc, compiled[_csc.__name__], ("_csc_base", "_swap"), None)
    if (csc_matrix.check_format is not original_check_format
            or csc_matrix.prune is not original_prune
            or csc_matrix._get_index_dtype is not original_index_method
            or csc_matrix._swap is not original_swap):
        raise RuntimeError("CSC support method runtime identity mismatch")

    def construct_global_jac(n, m, k, h, df_dy, df_dy_middle, df_dp,
                             df_dp_middle, dbc_dya, dbc_dyb, dbc_dp):
        """Original arithmetic, followed by direct canonical CSC storage."""
        df_dy = np.transpose(df_dy, (2, 0, 1))
        df_dy_middle = np.transpose(df_dy_middle, (2, 0, 1))

        h = h[:, np.newaxis, np.newaxis]

        dtype = df_dy.dtype

        # Computing diagonal n x n blocks.
        dPhi_dy_0 = np.empty((m - 1, n, n), dtype=dtype)
        dPhi_dy_0[:] = -np.identity(n)
        dPhi_dy_0 -= h / 6 * (df_dy[:-1] + 2 * df_dy_middle)
        T = stacked_matmul(df_dy_middle, df_dy[:-1])
        dPhi_dy_0 -= h**2 / 12 * T

        # Computing off-diagonal n x n blocks.
        dPhi_dy_1 = np.empty((m - 1, n, n), dtype=dtype)
        dPhi_dy_1[:] = np.identity(n)
        dPhi_dy_1 -= h / 6 * (df_dy[1:] + 2 * df_dy_middle)
        T = stacked_matmul(df_dy_middle, df_dy[1:])
        dPhi_dy_1 += h**2 / 12 * T

        # Preserve the first hstack's pre-parameter-update boundary snapshot.
        dbc_dya = dbc_dya.copy()
        dbc_dyb = dbc_dyb.copy()
        dPhi_dp = None

        if k > 0:
            df_dp = np.transpose(df_dp, (2, 0, 1))
            df_dp_middle = np.transpose(df_dp_middle, (2, 0, 1))
            T = stacked_matmul(df_dy_middle, df_dp[:-1] - df_dp[1:])
            df_dp_middle += 0.125 * h * T
            dPhi_dp = -h/6 * (df_dp[:-1] + df_dp[1:] + 4 * df_dp_middle)

        return _assemble_csc(np, csc_matrix, get_index_dtype, n, m, k,
                             dPhi_dy_0, dPhi_dy_1, dPhi_dp,
                             dbc_dya, dbc_dyb, dbc_dp)

    def prepare_sys(n, m, k, fun, bc, fun_jac, bc_jac, x, h):
        """Create the function and the Jacobian for the collocation system."""
        x_middle = x[:-1] + 0.5 * h

        def col_fun(y, p):
            return collocation_fun(fun, y, p, x, h)

        def sys_jac(y, p, y_middle, f, f_middle, bc0):
            if fun_jac is None:
                df_dy, df_dp = estimate_fun_jac(fun, x, y, p, f)
                df_dy_middle, df_dp_middle = estimate_fun_jac(
                    fun, x_middle, y_middle, p, f_middle)
            else:
                df_dy, df_dp = fun_jac(x, y, p)
                df_dy_middle, df_dp_middle = fun_jac(x_middle, y_middle, p)

            if bc_jac is None:
                dbc_dya, dbc_dyb, dbc_dp = estimate_bc_jac(bc, y[:, 0], y[:, -1],
                                                           p, bc0)
            else:
                dbc_dya, dbc_dyb, dbc_dp = bc_jac(y[:, 0], y[:, -1], p)

            return construct_global_jac(n, m, k, h, df_dy,
                                        df_dy_middle, df_dp, df_dp_middle, dbc_dya,
                                        dbc_dyb, dbc_dp)

        return col_fun, sys_jac


    def runtime_identity(function):
        return {
            "module": function.__module__,
            "qualname": function.__qualname__,
            "filename": function.__code__.co_filename,
            "firstlineno": function.__code__.co_firstlineno,
            "code_sha256": hashlib.sha256(marshal.dumps(function.__code__)).hexdigest(),
        }

    own_path = Path(__file__).resolve()
    own_bytes = own_path.read_bytes()
    provenance = {
        "schema": "db6f-direct-canonical-csc-functions-v2",
        "scope": "functions-only; no installation and no matrix/solver call by factory",
        "foundation": {
            "file": str(own_path), "bytes": len(own_bytes),
            "sha256": hashlib.sha256(own_bytes).hexdigest(),
        },
        "numpy_version": np.__version__,
        "scipy_version": scipy.__version__,
        "sources": sources,
        "original_callbacks": {
            name: runtime_identity(function)
            for name, function in (
                ("stacked_matmul", stacked_matmul),
                ("collocation_fun", collocation_fun),
                ("estimate_fun_jac", estimate_fun_jac),
                ("estimate_bc_jac", estimate_bc_jac),
                ("get_index_dtype", get_index_dtype),
                ("csc_init", original_csc_init),
                ("csc_check_format", original_check_format),
                ("csc_prune", original_prune),
                ("csc_get_index_dtype", original_index_method),
                ("csc_swap", original_swap),
            )
        },
        "new_functions": {
            "construct_global_jac": runtime_identity(construct_global_jac),
            "prepare_sys": runtime_identity(prepare_sys),
        },
        "newton_selection": "not read, installed, or validated by this foundation",
        "actual_sparse_byte_replay": "pending",
    }
    return DirectCSCFunctions(construct_global_jac, prepare_sys, provenance)
