#!/usr/bin/env python3
"""Build the one-time-H SLSQP extension inside the declared public Actions.

No mathematical probe or optimizer is run by this builder.  Its source fetch,
native compilation, import, and every failed attempt are charged to the same
scientific clock as the consuming optimization.  Temporary original sources
and binaries are not scientific output artifacts and are never committed.
"""
from __future__ import annotations

import ctypes
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys
import sysconfig
import time
import urllib.request


MODULE_NAME = "_r566_slsqp_seeded_20261127"
PATCH_NAME = "r566_seeded_slsqp_native_20261127.patch"
PATCH_SHA256 = "53926005cd188c164ed3cf243e91929f20060e6462edb03930a0d0c8c9c17d1c"
SOURCES = {
    "__slsqp.c": (33406, "bc6516a9c65eb4b43d823c13c44c8fa02bc9486af87c17e7ffe1ec21b9dbd25b"),
    "__slsqp.h": (17294, "4888eb0a72734e36d09f7bbae3290f3c68451c2b14258da56fc360b0f9b9a3b9"),
    "__nnls.c": (9982, "bf9228b49a696cae15b26c24275508580d7965726df08efbcd91cf04d8e548a2"),
    "__nnls.h": (654, "a68f214a640c08fe382cb69e829afe79767f91f6744f043d1da9d08e0d957857"),
}
PATCHED = {
    "__slsqp.c": (33889, "6c51bc16553050db0c392ed3cd07e1dbf647d0da3252aac20327507e00aad1cf"),
    "__slsqp.h": (18918, "cbbcbea90fe3aed039c3bd68fee68e7d39b08d0c0164ab2462b3be121751d1f5"),
}
PY_WRAPPER_SHA256 = "c8362e8d36440f3de97b58562aadb86661271ea7f66160505f51a601aff71609"
LICENSE_SHA256 = "221e59f5e910fd7f94e44f0dac77436a11338c285c6346232e4a850a50da0e94"
BLAS_NAMES = ["daxpy", "ddot", "dgelsy", "dgemv", "dgeqr2", "dgerq2",
              "dlarf", "dlarfgp", "dlartgp", "dnrm2", "dorm2r", "dormr2",
              "dscal", "dtpmv", "dtpsv", "dtrsm", "dtrsv"]


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def require_public_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("This native build belongs only to the declared public Actions scope.")


def verify(path, expected):
    data = Path(path).read_bytes()
    actual = len(data), sha256_bytes(data)
    if actual != expected:
        raise ValueError("Bound source bytes differ: " + str(path.name))
    return {"bytes": actual[0], "sha256": actual[1]}


def build(directory, deadline, receipt, emit):
    """Return a newly built module; mutate receipt even on an interrupted build.

    directory is a caller-owned ephemeral directory.  deadline is the same
    monotonic deadline used by the actual scientific driver, never a fresh one.
    emit accepts the usual (event_name, small_json_receipt) pair.
    """
    require_public_actions()
    started = time.monotonic()
    receipt.update({"started": True, "completed": False, "source_fetch_attempts": 0,
                    "source_fetch_completed": 0, "source_fetch_seconds": 0.0,
                    "native_compile_attempts": 0, "native_compile_seconds": 0.0,
                    "scientific_probe_or_old_qualification_replayed": False,
                    "module_name": MODULE_NAME})

    def remaining(stage, cap=120.0):
        value = deadline-time.monotonic()
        if value <= 0:
            raise TimeoutError("Native build reached original scientific deadline: " + stage)
        receipt["stage"] = stage
        return min(cap, value)

    try:
        import numpy as np
        import scipy
        import scipy.optimize._slsqp_py as original_python

        remaining("version_and_actual_bound_python_wrapper")
        if scipy.__version__ != "1.17.0":
            raise ValueError("The one-time-H patch is bound to SciPy 1.17.0.")
        wrapper = Path(original_python.__file__).resolve()
        if sha256_bytes(wrapper.read_bytes()) != PY_WRAPPER_SHA256:
            raise ValueError("The actual Python SLSQP control flow differs from the bound source.")
        receipt["runtime"] = {"python": sys.version, "numpy": np.__version__,
                              "scipy": scipy.__version__,
                              "python_wrapper_sha256": PY_WRAPPER_SHA256}
        directory = Path(directory).resolve()
        directory.mkdir(parents=True, exist_ok=True)
        script_directory = Path(__file__).resolve().parent
        patch = script_directory/PATCH_NAME
        if sha256_bytes(patch.read_bytes()) != PATCH_SHA256:
            raise ValueError("The native initialization patch differs from its declaration.")
        license_path = script_directory/"r566_seeded_slsqp_SCIPY_LICENSE.txt"
        if sha256_bytes(license_path.read_bytes()) != LICENSE_SHA256:
            raise ValueError("The redistributed SciPy license differs from the official source.")
        (directory/"SCIPY_LICENSE.txt").write_bytes(license_path.read_bytes())
        receipt["official_original_sources"] = {}
        for name, expected in SOURCES.items():
            timeout = remaining("fetch_official_"+name, 30.0)
            receipt["source_fetch_attempts"] += 1
            one_started = time.monotonic()
            url = "https://raw.githubusercontent.com/scipy/scipy/v1.17.0/scipy/optimize/"+name
            try:
                request = urllib.request.Request(url, headers={"User-Agent": "public-math-r566-source"})
                with urllib.request.urlopen(request, timeout=timeout) as response:
                    data = response.read()
                if (len(data), sha256_bytes(data)) != expected:
                    raise ValueError("Official source byte identity differs: "+name)
                (directory/name).write_bytes(data)
                receipt["official_original_sources"][name] = {
                    "url": url, "bytes": expected[0], "sha256": expected[1]}
                receipt["source_fetch_completed"] += 1
            finally:
                receipt["source_fetch_seconds"] += time.monotonic()-one_started
        remaining("apply_exact_original_source_patch")
        applied = subprocess.run(["patch", "--batch", "--fuzz=0", "-p1", "-i", str(patch)],
                                 cwd=directory, capture_output=True, text=True,
                                 timeout=remaining("apply_exact_original_source_patch"))
        if applied.returncode:
            raise RuntimeError("Exact source patch failed: "+applied.stdout+applied.stderr)
        receipt["patched_sources"] = {name: verify(directory/name, expected)
                                       for name, expected in PATCHED.items()}

        # The pinned wheel's own LP64 OpenBLAS library supplies every original
        # BLAS/LAPACK call.  No unrelated system BLAS is selected silently.
        libraries = sorted((Path(scipy.__file__).resolve().parent.parent/"scipy.libs")
                           .glob("libscipy_openblas*.so"))
        if len(libraries) != 1:
            raise RuntimeError("The pinned SciPy wheel must identify one LP64 OpenBLAS library.")
        library = libraries[0]
        linked = ctypes.CDLL(str(library))
        for name in BLAS_NAMES:
            getattr(linked, "scipy_"+name+"_")
        receipt["same_scipy_blas_lapack"] = {
            "filename": library.name, "bytes": library.stat().st_size,
            "sha256": sha256_bytes(library.read_bytes()),
            "required_symbols": ["scipy_"+name+"_" for name in BLAS_NAMES],
            "numeric_probe_calls": 0}
        compiler = shlex.split(sysconfig.get_config_var("CC") or "cc")
        version = subprocess.run(compiler+["--version"], capture_output=True, text=True,
                                 timeout=remaining("compiler_version", 15.0), check=True)
        receipt["compiler"] = version.stdout.splitlines()[0]
        suffix = sysconfig.get_config_var("EXT_SUFFIX")
        output = directory/(MODULE_NAME+suffix)
        command = compiler+["-O2", "-std=c11", "-shared", "-fPIC", "-fvisibility=hidden", "-fno-fast-math",
            "-ffp-contract=off", "-I"+sysconfig.get_paths()["include"],
            "-I"+np.get_include()]
        command += ["-D"+name+"_=scipy_"+name+"_" for name in BLAS_NAMES]
        command += [str(directory/"__slsqp.c"), str(directory/"__nnls.c"), str(library),
                    "-Wl,-rpath,"+str(library.parent), "-lm", "-o", str(output)]
        receipt["compile_argv"] = command
        receipt["native_compile_attempts"] += 1
        compile_started = time.monotonic()
        try:
            compiled = subprocess.run(command, capture_output=True, text=True,
                                      timeout=remaining("compile_original_plus_initial_H"))
            receipt["compiler_returncode"] = compiled.returncode
            receipt["compiler_stdout_sha256"] = sha256_bytes(compiled.stdout.encode())
            receipt["compiler_stderr_sha256"] = sha256_bytes(compiled.stderr.encode())
            if compiled.returncode:
                receipt["compiler_failure_text"] = (compiled.stdout+compiled.stderr)[-12000:]
                raise RuntimeError("The declared native initialization extension did not compile.")
        finally:
            receipt["native_compile_seconds"] += time.monotonic()-compile_started
        remaining("import_actual_new_native_extension")
        spec = importlib.util.spec_from_file_location(MODULE_NAME, output)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        receipt["binary"] = {"bytes": output.stat().st_size,
                             "sha256": sha256_bytes(output.read_bytes())}
        receipt["completed"] = True
        receipt["stage"] = "native_initial_H_extension_ready"
        return module
    except Exception as error:
        receipt["error"] = type(error).__name__+": "+str(error)
        raise
    finally:
        receipt["seconds"] = time.monotonic()-started
        emit("R566_INITIAL_H_NATIVE_BUILD", json.loads(json.dumps(receipt, allow_nan=False)))
