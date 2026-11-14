#!/usr/bin/env python3
"""Decompose the actual63 fixed complete damped model, only in public Actions.

Fetch is a separately token-scoped operation using the unchanged safe public
artifact kernel. Analyze rebuilds ONE original base evaluation, ONE complete
linearization, and ONE complete square-root factor. It runs no optimization,
native solve, new nonlinear trial, parameter search, or acceptance test.

The saved local root/candidate and original recovery RHS are data. Full
unconstrained center and force responses are newly computed diagnostics, not
objects falsely attributed to the original artifact.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path, PurePosixPath
import resource
import struct
import sys
import time
import traceback

SCHEMA = "actual63-fixed-complete-model-response-decomposition-v1"
REPOSITORY = "Rogerhu12/math-research-public"
SOURCE_COMMIT = "db6d728f30ee2d0c9ea62c96c622d8d85d2354b2"
PIN = dict(run_id=43646179305, artifact_id=14134662698,
    artifact_name="visible-followup-condensedqp-43646179305-1",
    expected_size=494657224,
    expected_sha256="c90869cdcc317eef9b23a8a17755a7679ea5ce6dc41c2c143216524b481c6653")
KERNEL_NAME = "exact_20261114_fetch_pinned_public_artifact.py"
KERNEL_SHA = "51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859"
KERNEL_SCHEMA = "pinned-public-actions-artifact-fetch-v3"
HERE = Path(__file__).resolve().parent
WARM = "eighteen-condensed-warm"
ROW, INTERVAL, COMPONENT = 155819, 461, 1
SIZE, NPHYS, NODES, NLOCAL, BROWS = 236036, 338, 699, 5749, 36864
DAMPING = 270.0
EXPECTED = dict(
    accepted="b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff",
    prepared="0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714",
    tail_anchor="e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51",
    tail_config="01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5")
REQUIRED_SOURCES = {
    "geometry_20261114_constrained_trust_warm.py":
        "5378b7d732dc768f154849a1138ea59a2571f1128cc507932d38d4f8bfb115f2",
    "geometry_20261114_constrained_collocation.py":
        "70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8",
    "exact_20261114_regularized_block_qr.py":
        "596356c06f710869b3bc26931ddaa87d66fe892bcf7920a25b42453b66bfa722",
    "root_20261114_complete_local_qp_condensation.py":
        "84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b",
}
FILE_PINS = {
    "parent62/warm-001.json.gz":
        "dffaa532026e07357d5115089d968c1be4472c44d9a5f5da25ebcb3e2291ac73",
    "parent62/driver-status.json":
        "4f8239522cef511aca6721ddc9c4541cc9d4e65db3e7260d277b090ad226c054",
    "preparation112/prepared.json.gz": EXPECTED["prepared"],
    "T112-config.json": EXPECTED["tail_config"],
    WARM+"/condensed-QP-result.json.gz":
        "ebe1b7340d29c440e47b50de7eccdc36733b6d28d90a09a9050894db1ab3a0f4",
    WARM+"/condensed-QP-summary.json":
        "f5036998a69fb391b5634514bc19d5ff149c238d8bfb6e2b494abcb1164fdb53",
    WARM+"/condensed-live-model-binding.json":
        "eae92727675563991a9da5e9bb7a6aeece945434c1686e558d00b9aeb59d1c65",
    WARM+"/condensed-array-manifest.json":
        "f65df44ab8866f3e4ab7809e9232dd19a719f5f5bc5ad4c24ee9d427e37339fe",
    WARM+"/optimization-intent.json":
        "688c586b83ad9d1c1cc16526b885c594e471ec3d6e2afeb29ea27f0c1c860f94",
    WARM+"/driver-status.json":
        "8785231faf9785c29dffc37bf4415d235d4dbb78d249a06f7cdbe658aef76f46",
    WARM+"/model-000.json":
        "68549fb677c2a255895a3dcef701c4f2e6b25586874e697f63527bb3c65646e0",
    WARM+"/domain-operator/manifest.json":
        "ff034c85815a98bba2cc1745e3e7a1416c309e656c69b572e15f5f0bb3fcb23f",
}
np = None


def require(test, message):
    if not test:
        raise ValueError(message)


def require_actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
        "Run this diagnostic only in the named public repository's Actions")
    require(sys.byteorder == "little", "The original numerical objects are little-endian")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        while block := f.read(1024*1024):
            h.update(block)
    return h.hexdigest()


def safe_path(base, name):
    require(isinstance(name, str) and "\\" not in name and "\0" not in name,
        "A descriptor path must be a plain relative POSIX path")
    p = PurePosixPath(name)
    require(not p.is_absolute() and p.parts and
        all(x not in ("", ".", "..") for x in p.parts), "Unsafe descriptor path")
    base = Path(base).resolve()
    current = base
    for part in p.parts:
        current = current/part
        require(not current.is_symlink(), "Do not follow descriptor symlinks")
    result = current.resolve()
    require(result.is_relative_to(base), "Descriptor escaped its source directory")
    return result


def read(path):
    raw = Path(path).read_bytes()
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    return json.loads(raw)


def receipt(path, base=None):
    p = Path(path)
    return dict(file=str(p.relative_to(base)) if base is not None else p.name,
        bytes=p.stat().st_size, sha256=sha(p))


def json_safe(value):
    if isinstance(value, dict):
        return {str(k): json_safe(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_safe(v) for v in value]
    if np is not None and isinstance(value, np.integer):
        return int(value)
    if isinstance(value, float) or (np is not None and isinstance(value, np.floating)):
        x = float(value)
        return x if math.isfinite(x) else dict(nonfinite_display=repr(x))
    return value


def write_json(path, data, *, small=False):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(json_safe(data), ensure_ascii=False,
        indent=2 if small else None, allow_nan=False)+"\n").encode()
    require(not small or len(raw) < 100000, "Keep this small report under 100 KB")
    if path.suffix == ".gz":
        raw = gzip.compress(raw, mtime=0)
    tmp = path.with_name(path.name+".tmp")
    tmp.write_bytes(raw)
    tmp.replace(path)
    return receipt(path, path.parent)


def number(value):
    x = float(value)
    return dict(value=x if math.isfinite(x) else None,
        float64le_hex=struct.pack("<d", x).hex(),
        negative_zero=bool(x == 0.0 and math.copysign(1., x) < 0),
        classification=("finite" if math.isfinite(x) else repr(x)))


def rational(value):
    q = value if isinstance(value, Fraction) else Fraction.from_float(float(value))
    return dict(numerator=str(q.numerator), denominator=str(q.denominator))


def same_dict_identity(actual, expected, *, raw=False):
    keys = ("shape", "dtype", "bytes", "raw_sha256" if raw else "sha256")
    return all(actual.get(k) == expected.get(k) for k in keys)


def prefixed_identity(array):
    a = np.asarray(array)
    h = hashlib.sha256(str(a.shape).encode()+b"\0"+a.dtype.str.encode()+b"\0")
    for b in array_bytes(a):
        h.update(b)
    return dict(shape=list(a.shape), dtype=a.dtype.str, bytes=int(a.nbytes),
        sha256=h.hexdigest())


def raw_identity(array):
    a = np.asarray(array)
    h = hashlib.sha256()
    for b in array_bytes(a):
        h.update(b)
    return dict(shape=list(a.shape), dtype=a.dtype.str, order="C",
        bytes=int(a.nbytes), raw_sha256=h.hexdigest())


def array_bytes(array):
    a = np.asarray(array)
    if a.flags.c_contiguous:
        b = memoryview(a).cast("B")
        for start in range(0, len(b), 1024*1024):
            yield b[start:start+1024*1024]
    elif a.ndim == 0:
        yield a.tobytes()
    else:
        for row in a:
            yield np.ascontiguousarray(row).tobytes(order="C")


def stats(array):
    a = np.asarray(array)
    if not a.size:
        return dict(L2=0., Linf=0., finite=True, count=0)
    maximum = float(np.max(abs(a)))
    finite = bool(np.all(np.isfinite(a)))
    norm = (0. if maximum == 0 else
        float(maximum*np.sqrt(np.sum((a/maximum)**2))) if finite else None)
    return dict(L2=norm, Linf=maximum, finite=finite, count=int(a.size))


def compare_arrays(a, b):
    aa, bb = np.asarray(a), np.asarray(b)
    require(aa.shape == bb.shape and aa.dtype == bb.dtype, "Compare the same array representation")
    return dict(left=raw_identity(aa), right=raw_identity(bb),
        byte_identical=bool(aa.tobytes(order="C") == bb.tobytes(order="C")),
        numerical_difference=stats(aa-bb))


class Writer:
    def __init__(self, directory):
        self.root = Path(directory)
        self.large = self.root/"large-arrays"
        self.large.mkdir(parents=True, exist_ok=False)
        self.arrays = []

    def array(self, name, value, role):
        require(name and all(ch.isalnum() or ch in "-_" for ch in name), "Safe array name")
        a = np.asarray(value)
        require(a.dtype.kind in "fiub" and a.dtype.itemsize <= 8,
            "Use explicit finite-width numerical arrays")
        path = self.large/(name+".raw")
        with path.open("xb") as f:
            for block in array_bytes(a):
                f.write(block)
        item = dict(name=name, file=str(path.relative_to(self.root)),
            **raw_identity(a), sha256=sha(path), role=role)
        self.arrays.append(item)
        return item

    def data(self, name, value):
        path = self.large/(name+".json.gz")
        write_json(path, value)
        return receipt(path, self.root)

    def manifest(self):
        path = self.root/"array-manifest.json"
        write_json(path, dict(schema=SCHEMA+"-arrays", arrays=self.arrays))
        return receipt(path, self.root)


class OriginalFiles:
    def __init__(self, directory):
        self.root = Path(directory).resolve()
        self.checked = {}
        for name, digest in FILE_PINS.items():
            self.file(name, digest)
        self.warm = self.root/WARM

    def file(self, name, digest, size=None):
        p = safe_path(self.root, name)
        key = str(p.relative_to(self.root))
        if key not in self.checked:
            require(p.is_file(), "Missing original artifact file: "+key)
            self.checked[key] = receipt(p, self.root)
        r = self.checked[key]
        require(r["sha256"] == digest and (size is None or r["bytes"] == size),
            "Original file bytes differ: "+key)
        return p

    def descriptor(self, base, desc):
        name = desc.get("file", desc.get("path"))
        p = safe_path(base, name)
        return self.file(str(p.relative_to(self.root)), desc["sha256"], desc.get("bytes"))

    def npz(self, base, desc, expected_arrays=None):
        p = self.descriptor(base, desc)
        with np.load(p, allow_pickle=False) as z:
            require(len(z.files) == len(set(z.files)), "Duplicate NPZ member")
            if expected_arrays is not None:
                require(set(z.files) == set(expected_arrays), "Original NPZ key set differs")
            result = {}
            for key in z.files:
                a = np.asarray(z[key])
                require(a.dtype.kind in "fiub" and a.dtype.itemsize <= 8,
                    "An original array has an unsupported dtype")
                if expected_arrays is not None:
                    require(same_dict_identity(prefixed_identity(a), expected_arrays[key]),
                        "Original uncompressed array differs: "+str(p.name)+":"+key)
                result[key] = a
        return result

    def archived(self, ref, manifest):
        require(set(("array_identity", "parts")) <= set(ref), "Complete archived-array reference")
        ident = ref["array_identity"]
        parts = ref["parts"]
        require(parts, "An archived array has no parts")
        arrays, cursor = [], 0
        for part in parts:
            require(part == manifest[part["file"]], "Archived part and original manifest differ")
            pz = self.npz(self.warm, part)
            require(len(pz) == 1, "Each original archive part contains exactly one array")
            a = next(iter(pz.values()))
            require(same_dict_identity(prefixed_identity(a), part["array"]), "Original part bytes")
            lo, hi = part["leading_slice"]
            require(lo == cursor and hi >= lo and a.shape[0] == hi-lo,
                "Archived parts must exactly cover the first dimension in order")
            arrays.append(a)
            cursor = hi
        a = arrays[0] if len(arrays) == 1 else np.concatenate(arrays, axis=0)
        require(same_dict_identity(prefixed_identity(a), ident), "Complete archived array identity")
        return a

    def raw(self, base, desc):
        p = safe_path(base, desc["file"])
        self.file(str(p.relative_to(self.root)), desc["raw_sha256"], desc["bytes"])
        dt = np.dtype(desc["dtype"])
        require(dt.kind in "fiub" and dt.itemsize <= 8 and desc.get("order") == "C",
            "Retain an original explicit C-order raw representation")
        a = np.fromfile(p, dtype=dt).reshape(tuple(desc["shape"]))
        require(same_dict_identity(raw_identity(a), desc, raw=True), "Original raw descriptor")
        return a


def fetch_original(args):
    require_actions()
    path = HERE/KERNEL_NAME
    require(sha(path) == KERNEL_SHA, "The safe transport kernel must remain unchanged")
    spec = importlib.util.spec_from_file_location("_actual63_model_transport", path)
    require(spec is not None and spec.loader is not None, "Public transport module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    require(module.REPOSITORY == REPOSITORY and module.SCHEMA == KERNEL_SCHEMA,
        "Public transport source contract")
    old_metadata, old_public = module.read_metadata, module.public_metadata

    def metadata(opener, token):
        value, url = old_metadata(opener, token)
        require(value["workflow_run"].get("head_sha") == SOURCE_COMMIT,
            "The artifact must belong to the actual63 source commit")
        return value, url

    def public(value):
        result = old_public(value)
        result["diagnostic_adapter_not_GitHub_metadata"] = dict(
            schema=SCHEMA, source_file=Path(__file__).name, source_sha256=sha(__file__),
            safe_transport_source_sha256=KERNEL_SHA,
            only_pin_metadata_and_schema_changed_in_memory=True,
            full_original_extraction_unchanged=True, mathematical_computation_performed=False)
        return result

    module.PIN = dict(PIN)
    module.SCHEMA = SCHEMA+"-artifact-fetch"
    module.read_metadata, module.public_metadata = metadata, public
    argv = [str(path)]
    for key, value in PIN.items():
        argv += ["--"+key.replace("_", "-"), str(value)]
    argv += ["--out", str(args.out)]
    old_argv = sys.argv
    try:
        sys.argv = argv
        code = module.main()
    finally:
        sys.argv = old_argv
    require(code == 0, "The original artifact fetch failed")
    item = read(Path(args.out)/module.RECEIPT_NAME)
    require(item["success"] is True and item["pinned_input"] == PIN
        and item["download"]["actual_sha256"] == PIN["expected_sha256"],
        "The complete downloaded archive receipt differs")
    return 0


def exact_embedding_expansion(rhs, g, force, index, writer):
    """Represent the exact dyadic addition error by finite f64 components.

    This is an Actions diagnostic on saved finite operands, not local host
    work. Fractions concern the original saved RHS ADDITION only; neither
    QR nor A/AT arithmetic becomes an exact operation by this accounting.
    """
    errors = [Fraction.from_float(float(rhs[i]))+Fraction.from_float(float(g[i]))
              -Fraction.from_float(float(force[j])) for j, i in enumerate(index)]
    remainder = list(errors)
    components = []
    # A sum of three binary64 operands has a short finite binary expansion.
    # The cap is a bounded diagnostic implementation limit, not a science gate.
    for unused in range(8):
        if not any(remainder):
            break
        a = np.asarray([float(q) for q in remainder], dtype="<f8")
        require(np.all(np.isfinite(a)), "The exact RHS addition error expansion overflowed")
        components.append(a)
        remainder = [q-Fraction.from_float(float(x)) for q, x in zip(remainder, a)]
    records = [dict(local_index=j, global_index=int(i),
        saved_rhs=number(rhs[i]), saved_g=number(g[i]), nominal_force=number(force[j]),
        exact_addition_error=rational(errors[j]),
        rounded_components=[number(a[j]) for a in components],
        unrepresented_remainder=rational(remainder[j])) for j, i in enumerate(index)]
    report = dict(exact_expression="saved_rhs + saved_g - saved_nominal_local_force",
        entry_count=len(index), component_count=len(components),
        exact_all_entries_represented=not any(remainder),
        original_qr_or_operator_rounding_not_certified=True,
        exact_ledger=writer.data("exact-local-rhs-addition-errors", records))
    require(report["exact_all_entries_represented"],
        "Preserved exact RHS addition error exceeded the finite expansion implementation budget")
    return components, report


def audited_source_closure(files, intent, binding, root):
    expected = dict(intent["source_sha256"])
    expected.update(binding["condensed_QP_entry"]["frozen_dependencies"])
    expected.update(binding["read_only_collocation_observer_entry"]["observed_original_sources"])
    expected.update(binding["read_only_collocation_observer_entry"]["observer_source_sha256"])
    for name, digest in REQUIRED_SOURCES.items():
        require(expected.get(name) == digest, "Required original source does not match the stored ledger")
    checked = {}
    for name, digest in expected.items():
        require(PurePosixPath(name).name == name, "Topic source ledger basename")
        p = HERE/name
        require(p.is_file() and sha(p) == digest, "Frozen numerical source changed: "+name)
        checked[name] = dict(bytes=p.stat().st_size, sha256=digest)
    prep = read(root/"public-source-preparation.json")
    require(prep["actual_public_repository"] == REPOSITORY
        and prep["actual_public_commit"] == SOURCE_COMMIT
        and prep["verified_file_count"] == 78, "Actual63 original public restoration receipt")
    topic = Path(os.environ.get("VISIBLE_SOURCE_TOPIC", "")).resolve()
    require(bool(os.environ.get("VISIBLE_SOURCE_TOPIC")) and topic.is_dir(),
        "Restore the same public 78-file source tree and set VISIBLE_SOURCE_TOPIC")
    restored = []
    prefix = PurePosixPath("topics/visible-flexible-closed-surface")
    for rec in prep["restored_files"]:
        rel = PurePosixPath(rec["path"]).relative_to(prefix)
        p = safe_path(topic, str(rel))
        require(p.stat().st_size == rec["bytes"] and sha(p) == rec["sha256"],
            "Original restored source byte identity: "+str(rel))
        restored.append(rec)
    require(len(restored) == 78, "Every original restored numerical file is represented")
    return dict(topic_sources=checked, original_restored_sources=restored,
        current_diagnostic_source=receipt(__file__), original_public_commit=SOURCE_COMMIT)


def deadline_check(deadline, phase):
    if time.monotonic() >= deadline:
        raise TimeoutError("Diagnostic budget reached before "+phase)


def finite_array(array, shape, label):
    a = np.asarray(array)
    require(a.dtype == np.dtype("<f8") and a.shape == tuple(shape),
        "Retain complete binary64 dimensions: "+label)
    require(np.all(np.isfinite(a)), "Nonfinite diagnostic operand: "+label)
    return a


def saved_B_actions(files, manifest, local_indices, directions, c, writer):
    """Read all saved B coefficients; never recapture a query or Jacobian."""
    directory = files.warm/"domain-operator"
    groups = {}
    for desc in manifest["files"]:
        files.descriptor(directory, desc)
        if "-rows-" in desc["path"]:
            q = desc["query"]["query_index"]
            groups.setdefault(q, []).append(desc)
    require(set(groups) == set(range(18)), "Every actual63 typed query must remain present")
    outputs = {name: np.empty(BROWS, dtype="<f8") for name in directions}
    for q in range(18):
        values, covered = [], np.zeros(2048, dtype=np.uint8)
        columns = None
        for desc in groups[q]:
            arrays = files.npz(directory, desc, desc["arrays"])
            angles = arrays["angle_indices"]
            cols = arrays["global_columns"]
            loc = arrays["local_columns"]
            require(angles.dtype == np.dtype("<i8") and cols.dtype == np.dtype("<i8")
                and loc.dtype == np.dtype("<i8"), "Retain original integer B row/column maps")
            require(np.all((angles >= 0) & (angles < 2048)) and len(set(angles.tolist())) == len(angles)
                and not np.any(covered[angles]), "One saved B record per physical angle")
            covered[angles] = 1
            require(np.array_equal(local_indices[loc], cols), "Full/local B column map")
            if columns is None:
                columns = cols.copy()
            else:
                require(np.array_equal(columns, cols), "Consistent columns within a typed B query")
            require(arrays["rows"].shape == (len(angles), len(columns)), "Complete saved B rows")
            values.append((angles, arrays["rows"]))
        require(np.all(covered), "All original N2048 angles are retained")
        rows = np.empty((2048, len(columns)), dtype="<f8")
        for angles, chunk in values:
            rows[angles] = chunk
        for name, direction in directions.items():
            outputs[name][q*2048:(q+1)*2048] = rows@direction[columns]
    records = {}
    for name, action in outputs.items():
        slack = c+action
        records[name] = dict(action=writer.array("B-"+name, action,
                "Original stored complete B coefficients applied to the named scaled-z diagnostic"),
            slack=writer.array("B-slack-"+name, slack,
                "Original c plus the named B action; not a nonlinear-domain certificate"),
            action_stats=stats(action), minimum_slack=float(np.min(slack)),
            negative_slack_count=int(np.count_nonzero(slack < 0)))
    return outputs, records


def row_label(row):
    if row < (NODES-1)*NPHYS:
        j, component = divmod(row, NPHYS)
        return dict(global_row=row, interval=j, physical_component=component,
            family="physical-collocation")
    return dict(global_row=row, right_boundary_index=row-(NODES-1)*NPHYS,
        family="complete-right-boundary")


def analyze(args):
    require_actions()
    require(math.isfinite(args.budget_seconds) and args.budget_seconds > 0
        and args.jac_workers == 2,
        "Use a finite positive diagnostic budget and the original two Jacobian workers")
    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    deadline = started+args.budget_seconds
    report = dict(schema=SCHEMA, classification="Actions numerical diagnostic",
        completed=False, created_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=sha(__file__), original_artifact=PIN,
        original_source_commit=SOURCE_COMMIT, focus=row_label(ROW),
        scope=dict(fixed_original_model=True, one_original_base_evaluation=True,
            one_original_complete_linearization=True, one_factor_reconstruction=True,
            factor_payload_present_in_original_artifact=False,
            no_QP_or_LSMR_or_new_constraint=True, no_new_native_solve=True,
            no_new_nonlinear_trial=True, no_changed_scientific_gate=True,
            no_damping_search=True, original_accepted_alpha_only=True,
            roundoff_reports_are_not_validated_error_enclosures=True,
            unique_cause_not_assumed=True))
    factor = writer = None
    try:
        global np
        for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
            os.environ[key] = "1"
        import numpy as np_module
        import scipy
        np = np_module
        require(np.__version__ == "2.3.5" and scipy.__version__ == "1.17.0",
            "Use the actual63 NumPy2.3.5/SciPy1.17.0 numerical runtime")
        report["runtime"] = dict(Python=sys.version, NumPy=np.__version__,
            SciPy=scipy.__version__, BLAS_threads={key:os.environ[key] for key in
                ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")})
        files = OriginalFiles(args.artifact_directory)
        root, warm = files.root, files.warm
        fetch_receipt = read(root/"_pinned_public_artifact_receipt.json")
        require(fetch_receipt["success"] is True and fetch_receipt["pinned_input"] == PIN
            and fetch_receipt["download"]["actual_sha256"] == PIN["expected_sha256"],
            "Consume the complete byte-pinned actual63 extraction")
        report["artifact_fetch_receipt"] = receipt(root/"_pinned_public_artifact_receipt.json", root)
        data = read(warm/"condensed-QP-result.json.gz")
        binding = read(warm/"condensed-live-model-binding.json")
        intent = read(warm/"optimization-intent.json")
        model = read(warm/"model-000.json")
        status = read(warm/"driver-status.json")
        archive_manifest = read(warm/"condensed-array-manifest.json")
        domain_manifest = read(warm/"domain-operator/manifest.json")
        saved_factor = data["complete_chain_QR_report"]
        require(binding["damping"] == model["damping"] == saved_factor["damping"] == DAMPING
            and binding["original_A_shape"] == [SIZE, SIZE]
            and binding["constructor_calls"] == 1, "One original full lambda270 model")
        require(saved_factor["column_preconditioner_supplied"] is False
            and saved_factor["factor_storage"] == "memory-only"
            and all(v.get("file") is None for v in saved_factor["factor_arrays"].values()),
            "The actual63 full factor was memory-only; do not claim it was exported")
        require(domain_manifest["model_sha256"] == binding["B_model_sha256"]
            == archive_manifest["original_B_model_sha256"], "Original complete B identity")
        require(status["accepted_warm_steps"] == 1 and len(status["iterations"]) == 1
            and status["success"] is False and status["new_coupled_finite_acceptance"] is False,
            "Read one actual unaccepted full-field optimization warm")
        accepted_trials = [trial for trial in model["trials"] if trial.get("accepted") is True]
        require(len(accepted_trials) == 1, "One saved original accepted trial")
        alpha = float(accepted_trials[0]["alpha"])
        require(alpha == 0.0078125, "The selected original actual63 alpha changed")
        require(intent["resume_sha256"] == FILE_PINS["parent62/warm-001.json.gz"]
            == binding["condensed_QP_entry"]["actual_parent_warm_sha256"],
            "The original model base is actual62, not the new actual63 output")
        require(binding["condensed_QP_entry"]["actual_parent_status_sha256"]
            == FILE_PINS["parent62/driver-status.json"], "Original parent status identity")
        writer = Writer(out)
        sources = audited_source_closure(files, intent, binding, root)
        report["source_closure"] = writer.data("original-source-closure", sources)
        report["consumed_metadata"] = writer.data("original-consumed-metadata",
            dict(binding=binding, intent=intent, model=model,
                domain_manifest=domain_manifest, original_qr_report=saved_factor,
                original_condensation_report=data["condensation_report"],
                original_recovery_report=data["last_recovery"]))
        source = read(root/"preparation112/prepared.json.gz")
        current = read(root/"parent62/warm-001.json.gz")
        parent_status = read(root/"parent62/driver-status.json")
        require(parent_status["latest_warm_sha256"] == intent["resume_sha256"]
            and parent_status["accepted_warm_steps"] == 1,
            "Actual62 parent status must bind its exact original warm")
        require(current["optimization_warm"] == intent["resume_producer"],
            "Retain the entire original parent producer subtree")
        for name, path in (("accepted", args.accepted), ("tail_anchor", args.tail_anchor)):
            require(sha(path) == EXPECTED[name], "External original input SHA: "+name)
        require(intent["source_prepared_sha256"] == EXPECTED["prepared"]
            and intent["source_accepted_sha256"] == EXPECTED["accepted"]
            and intent["actual_zero_anchor_sha256"] == EXPECTED["tail_anchor"]
            and intent["actual_tail_config_sha256"] == EXPECTED["tail_config"],
            "Original accepted96/prepared112/true-zero/config tuple")
        accepted, anchor = read(args.accepted), read(args.tail_anchor)
        report["input_binding"] = dict(original_parent_warm_sha256=intent["resume_sha256"],
            original_parent_status_sha256=FILE_PINS["parent62/driver-status.json"],
            accepted=receipt(args.accepted), tail_anchor=receipt(args.tail_anchor),
            prepared=receipt(root/"preparation112/prepared.json.gz", root),
            tail_config=receipt(root/"T112-config.json", root),
            original_B_model_sha256=binding["B_model_sha256"],
            original_fixed_damping=DAMPING, original_complete_dimension=SIZE)
        amap = {x["file"]: x for x in archive_manifest["files"]}
        require(len(amap) == len(archive_manifest["files"]), "Unique original archive part paths")
        files.descriptor(warm, archive_manifest["result"])
        original = {}
        for name in ("original_b", "original_g", "original_c", "original_LSMR_direction",
                     "original_C_direction", "actual_conditional_recovery"):
            original[name] = files.archived(data[name], amap)
        original["saved_recovered_action"] = files.archived(data["recovered_full_model_evidence"]["action"], amap)
        original["saved_selected_direction"] = files.archived(data["final_selected_evidence"]["direction"], amap)
        original["saved_selected_action"] = files.archived(data["final_selected_evidence"]["action"], amap)
        original["saved_recovered_B"] = files.archived(data["recovered_full_model_evidence"]["Bz"], amap)
        original["saved_selected_B"] = files.archived(data["final_selected_evidence"]["Bz"], amap)
        for name, a in original.items():
            finite_array(a, (BROWS,) if name in
                ("original_c", "saved_recovered_B", "saved_selected_B") else (SIZE,), name)
        b, g, c = original["original_b"], original["original_g"], original["original_c"]
        zold, zselected = original["actual_conditional_recovery"], original["saved_selected_direction"]
        for a, key in ((b, "original_b"), (g, "original_g"),
                       (original["original_C_direction"], "original_C_candidate")):
            require(same_dict_identity(prefixed_identity(a), binding[key]), "Saved binding: "+key)
        root_arrays = {}
        for name, desc in data["condensation_report"]["output_arrays"].items():
            root_arrays[name] = files.raw(warm/"condensed-root", desc)
        local_indices = root_arrays["local-indices"]
        require(local_indices.dtype == np.dtype("<i8") and local_indices.shape == (NLOCAL,)
            and len(set(local_indices.tolist())) == NLOCAL and np.all(np.diff(local_indices) > 0)
            and np.all((local_indices >= 0) & (local_indices < SIZE)), "Complete original local support")
        require(same_dict_identity(prefixed_identity(local_indices), binding["local_indices"]),
            "The full 5749-variable B support is unchanged")
        require(raw_identity(root_arrays["original-g"]) == raw_identity(g)
            and raw_identity(root_arrays["recovery-000-actual-full"]) == raw_identity(zold),
            "Original raw and archived full g/recovery bytes agree")
        requested = root_arrays["recovery-000-requested-local"]
        rhs = root_arrays["recovery-000-rhs"]
        finite_array(requested, (NLOCAL,), "requested local candidate")
        finite_array(rhs, (SIZE,), "original recovery RHS")
        qpu = files.archived(data["local_QP_result"]["local_candidate"], amap)
        require(raw_identity(qpu) == raw_identity(requested), "Use the saved final local QP candidate")
        exterior = np.ones(SIZE, dtype=bool)
        exterior[local_indices] = False
        require(np.array_equal(rhs[exterior].view("<u8"), (-g[exterior]).view("<u8")),
            "Saved recovery RHS has no exterior forcing beyond complete -g")
        base_desc = next(x for x in domain_manifest["files"]
            if x["path"] == "base-and-local-layout.npz")
        base = files.npz(warm/"domain-operator", base_desc, base_desc["arrays"])
        require(np.array_equal(base["local_indices"], local_indices),
            "The saved B base and local root use the same full support")
        require(same_dict_identity(prefixed_identity(np.asarray(current["mesh"])),
            base_desc["arrays"]["mesh"]), "The actual parent also retains the same complete mesh")
        print(json.dumps(dict(event="actual63_diagnostic", phase="original-bytes-bound",
            files=len(files.checked), scientific_optimization_started=False)), flush=True)
        deadline_check(deadline, "original fixed base reconstruction")
        # No scientific producer is imported before the Actions guard and source checks.
        import geometry_20261114_constrained_trust_warm as baseline
        from geometry_20261114_constrained_collocation import CompleteResidual, CompleteLinearization
        import exact_20261114_regularized_block_qr as qr
        for name, digest in baseline.original.FROZEN_SOURCES.items():
            require(sha(HERE/name) == digest, "Original imported source closure: "+name)
        tbase = time.monotonic()
        profile, flow, boundary = baseline.setup(accepted, current, anchor, 4096, args.jac_workers)
        problem = CompleteResidual(np.asarray(source["mesh"]), flow, boundary)
        require(problem.chart.size == SIZE and len(problem.x) == NODES and flow.q.N == 2048,
            "The original full field, mesh, and angular representation are unchanged")
        coordinates = problem.chart.pack(np.asarray(current["states"]))
        state = problem.evaluate(coordinates, require_rms=True)
        require(state["finite"], "Original base reconstruction is not finite")
        weights = problem.weights(state)
        re_b = weights*state["vector"]
        for name, value in (("mesh", problem.x), ("y", state["y"]), ("rhs", state["f"]),
                            ("coordinate_scale", problem.chart.scale)):
            require(same_dict_identity(prefixed_identity(value), base_desc["arrays"][name]),
                "Reconstructed original base differs: "+name)
        require(same_dict_identity(prefixed_identity(weights), binding["original_weights"])
            and prefixed_identity(re_b) == prefixed_identity(b),
            "The original fixed Wr and b must agree in every saved byte")
        report["base_reconstruction"] = dict(seconds=time.monotonic()-tbase,
            state=state["report"], complete_base_arrays_match=True,
            original_parent_is_actual62=True, base_evaluation_calls=1,
            original_weights_calls=1, fixed_weight_merit=float(.5*(b@b)))
        deadline_check(deadline, "one original complete linearization")
        tj = time.monotonic()
        linear = CompleteLinearization(problem, state)
        A = linear.operator(weights)
        computed_g = A.rmatvec(b)
        require(prefixed_identity(computed_g) == prefixed_identity(g),
            "The newly reconstructed full A.T b must match the original full g exactly")
        # Original C is diagnostic provenance only; complete QR still uses no column C.
        original_norms = linear.column_norms_squared(weights)
        original_C = np.sqrt(original_norms+DAMPING*DAMPING)
        require(same_dict_identity(prefixed_identity(original_C), binding["original_C"]),
            "Retain the original complete diagonal C provenance")
        report["complete_linearization_reconstruction"] = dict(seconds=time.monotonic()-tj,
            constructor_calls=1, original_complete_g_matches=True,
            original_C_matches=True, complete_C_used_in_QR=False,
            no_random_operator_test_or_FD_or_optimization_run=True)
        deadline_check(deadline, "one complete square-root factor")
        factor = qr.RegularizedBlockQR(linear, weights, DAMPING, deadline=deadline,
            original_operator=A, column_preconditioner=None, storage_directory=None,
            input_identity=dict(schema=SCHEMA, original_source=SOURCE_COMMIT,
                original_live_binding_sha256=FILE_PINS[WARM+"/condensed-live-model-binding.json"],
                original_B_model_sha256=binding["B_model_sha256"]))
        require(factor.input_hashes == saved_factor["input_arrays"],
            "All L/R/P/BY/BC/BP/inlet/S/Wr original model bytes must match")
        factor.factorize()
        factor_comparison = {}
        for name, expected in saved_factor["factor_arrays"].items():
            actual = factor.report["factor_arrays"][name]
            factor_comparison[name] = dict(expected=expected, reconstructed=actual,
                byte_digest_matches=same_dict_identity(actual, expected, raw=True))
        report["factor_reconstruction"] = dict(
            original_payload_was_not_exported=True,
            complete_original_model_arrays_identical=True,
            complete_factor_sha_comparison=factor_comparison,
            all_factor_digests_match=all(v["byte_digest_matches"] for v in factor_comparison.values()),
            no_factor_identity_mismatch_silently_ignored=True,
            finite_factor_precision_read_back_through_original_A_AT=True)
        # A factor mismatch is diagnostic evidence, not a new acceptance gate.
        # The original coefficient identity above is mandatory to name this fixed model.
        # Subsequent inverse residuals always use that same original full A and AT.
        report["reconstructed_factor_report"] = writer.data("reconstructed-complete-factor-report", factor.report)
        local_root = root_arrays["local-root"]
        local_gradient = root_arrays["local-gradient"]
        nominal_force = local_root.T@(local_root@requested)+local_gradient
        require(same_dict_identity(raw_identity(nominal_force),
            data["last_recovery"]["actual_local_force"], raw=True),
            "Replay of the saved nominal local force must match its original SHA")
        rebuilt_rhs = -g.copy()
        rebuilt_rhs[local_indices] += nominal_force
        require(raw_identity(rebuilt_rhs) == raw_identity(rhs),
            "The saved full recovery RHS addition must reproduce its original bytes")
        embedding_components, embedding_report = exact_embedding_expansion(
            rhs, g, nominal_force, local_indices, writer)
        report["local_rhs_construction"] = dict(
            nominal_local_force=writer.array("nominal-local-force", nominal_force,
                "Saved local-root action plus saved local gradient, matching the original force SHA"),
            requested_local=writer.array("requested-local", requested,
                "Actual saved local QP candidate, unchanged"),
            original_full_rhs=writer.array("original-recovery-rhs", rhs,
                "Complete original RHS actually passed to the original recovery solve"),
            exact_addition_error=embedding_report,
            original_float_embedding_error_report=data["last_recovery"]["local_rhs_embedding_error_L2"],
            original_float_embedding_error_not_called_exact=True)
        directions, solve_reports = {}, {}

        def solve(name, value):
            deadline_check(deadline, "complete fixed-H diagnostic "+name)
            solution = factor.solve_H(value, label="actual63-diagnostic-"+name)
            direction = solution["candidate"]
            directions[name] = direction
            solve_reports[name] = dict(
                rhs=writer.array("solve-"+name+"-rhs", value, "Complete original H right-hand side"),
                direction=writer.array("solve-"+name+"-direction", direction,
                    "New complete fixed-H inverse diagnostic, not an original exported center"),
                original_residual=writer.array("solve-"+name+"-original-residual",
                    solution["original_residual"], "Original A.T A plus lambda squared residual"),
                factor_residual=writer.array("solve-"+name+"-factor-residual",
                    solution["factor_normal_residual"], "Factor-normal residual, never substituted for original H"),
                report=solution["report"])
            return direction

        center = solve("unconstrained-center", -g)
        forcing = np.zeros(SIZE, dtype="<f8")
        forcing[local_indices] = nominal_force
        local_response = solve("nominal-local-force", forcing)
        embedding_names = []
        for k, component in enumerate(embedding_components):
            name = "rhs-addition-error-"+str(k)
            embed = np.zeros(SIZE, dtype="<f8")
            embed[local_indices] = component
            solve(name, embed)
            embedding_names.append(name)
        replay = solve("saved-rhs-replay", rhs)
        cumulative = center+local_response
        for name in embedding_names:
            cumulative = cumulative+directions[name]
        directions["inverse-summation-closure"] = replay-cumulative
        directions["saved-recovery-minus-replay"] = zold-replay
        directions["original-selector-change"] = zselected-zold
        directions["saved-recovered"] = zold
        directions["saved-selected"] = zselected
        component_names = ["unconstrained-center", "nominal-local-force", *embedding_names,
            "inverse-summation-closure", "saved-recovery-minus-replay", "original-selector-change"]
        for name in component_names:
            if name not in solve_reports:
                writer.array("component-"+name, directions[name],
                    "Explicit finite-vector subtraction/summation remainder; no unique causal claim")
        report["inverse_diagnostics"] = writer.data("complete-H-inverse-diagnostics", solve_reports)
        report["inverse_summary"] = {name:dict(
            original_H_residual_L2=value["report"]["original_residual_L2"],
            original_H_residual_Linf=value["report"]["original_residual_Linf"],
            original_relative_residual_L2=value["report"]["original_relative_residual_L2"],
            factor_normal_residual_L2=value["report"]["factor_normal_residual_L2"],
            seconds=value["report"]["seconds"]) for name, value in solve_reports.items()}
        report["original_saved_recovery_replay"] = compare_arrays(replay, zold)
        report["original_local_center_vs_complete_center_restriction"] = compare_arrays(
            root_arrays["local-center"], center[local_indices])
        report["complete_center_scope"] = (
            "New full inverse of -original_g; not the saved local center and not original LSMR")
        actions, action_reports = {}, {}
        for name, direction in directions.items():
            action = A.matvec(direction)
            finite_array(action, (SIZE,), "original full A action: "+name)
            actions[name] = action
            action_reports[name] = dict(
                vector=writer.array("A-"+name, action, "Same fixed complete original A applied to named vector"),
                stats=stats(action), direction_stats=stats(direction))
        report["A_action_outputs"] = writer.data("complete-original-A-actions", action_reports)
        report["saved_action_rechecks"] = dict(
            recovered=compare_arrays(actions["saved-recovered"], original["saved_recovered_action"]),
            selected=compare_arrays(actions["saved-selected"], original["saved_selected_action"]))
        # No extra linearization or optimized direction is formed by these B reads.
        Boutputs, Breports = saved_B_actions(files, domain_manifest, local_indices,
            {name:directions[name] for name in
                ("unconstrained-center", "nominal-local-force", "saved-recovered", "saved-selected")},
            c, writer)
        report["original_saved_B_readback"] = dict(
            source_model_sha256=binding["B_model_sha256"], complete_rows=BROWS,
            complete_local_support=NLOCAL, no_new_domain_derivative=True,
            actions=Breports,
            recovered_against_saved=compare_arrays(Boutputs["saved-recovered"], original["saved_recovered_B"]),
            selected_against_saved=compare_arrays(Boutputs["saved-selected"], original["saved_selected_B"]),
            assembled_row_action_order_recorded="All original 2048 rows per typed query before each matvec",
            numerical_B_slacks_not_nonlinear_certificates=True)
        row_records = []
        interval_start = INTERVAL*NPHYS
        for row in range(interval_start, interval_start+NPHYS):
            terms = {name:float(actions[name][row]) for name in component_names}
            exact_sum = sum((Fraction.from_float(value) for value in terms.values()), Fraction())
            saved_target = Fraction.from_float(float(original["saved_selected_action"][row]))
            new_target = Fraction.from_float(float(actions["saved-selected"][row]))
            rec = dict(**row_label(row), original_b=number(b[row]),
                action_terms={name:number(value) for name,value in terms.items()},
                saved_recovered_Az=number(original["saved_recovered_action"][row]),
                saved_selected_Az=number(original["saved_selected_action"][row]),
                rebuilt_selected_Az=number(actions["saved-selected"][row]),
                exact_sum_of_returned_f64_components=rational(exact_sum),
                exact_saved_action_minus_component_sum=rational(saved_target-exact_sum),
                exact_rebuilt_action_minus_component_sum=rational(new_target-exact_sum),
                original_alpha=number(alpha),
                exact_alpha_times_each_returned_component={
                    name:rational(Fraction.from_float(alpha)*Fraction.from_float(value))
                    for name,value in terms.items()},
                exact_linear_prediction_from_saved_values=rational(
                    Fraction.from_float(float(b[row]))+Fraction.from_float(alpha)*saved_target),
                scope="Exact sums of returned binary64 readouts, not an exact A/QR computation")
            row_records.append(rec)
        report["interval461_complete_row_table"] = writer.data("interval461-all338-row-contributions", row_records)
        report["focus_row"] = row_records[COMPONENT]
        # Report the original L/R/P chains for this row using the original
        # einsum contractions, along with their sum and the authoritative A output.
        row_chains = {}
        for name in ("unconstrained-center", "nominal-local-force", "saved-recovered", "saved-selected"):
            direction = directions[name]/problem.chart.scale
            field, core, control = problem.chart.unpack_parts(direction)
            yl = field[INTERVAL-1]
            yr = field[INTERVAL]
            left = np.einsum("mij,mj->mi", linear.L[INTERVAL:INTERVAL+1], yl[None,:])[0]
            right = np.einsum("mij,mj->mi", linear.R[INTERVAL:INTERVAL+1], yr[None,:])[0]
            parameter = np.einsum("mij,j->mi", linear.P[INTERVAL:INTERVAL+1], control)[0]
            row_chains[name] = dict(
                original_row_weight=number(weights[ROW]),
                physical_node_left=INTERVAL, physical_node_right=INTERVAL+1,
                L_physical_unweighted=number(left[COMPONENT]),
                R_physical_unweighted=number(right[COMPONENT]),
                all_three_global_p_unweighted=number(parameter[COMPONENT]),
                weighted_left=number(weights[ROW]*left[COMPONENT]),
                weighted_right=number(weights[ROW]*right[COMPONENT]),
                weighted_all_p=number(weights[ROW]*parameter[COMPONENT]),
                original_full_A_readout=number(actions[name][ROW]),
                separate_products_not_claimed_bitwise_equal_to_original_sum_order=True,
                omitted_explicit_local_core_columns=False,
                explicit_local_core_columns_are_zero_in_original_LRP=True)
        report["focus_L_R_P_contributions"] = row_chains
        # A separately formed binary64 row supplies a diagnostic precision
        # scale, distinct from the operation order of the original A.matvec.
        with np.errstate(over="raise", invalid="raise", divide="raise"):
            aj = np.zeros(SIZE, dtype="<f8")
            left_slice = slice((INTERVAL-1)*NPHYS, INTERVAL*NPHYS)
            right_slice = slice(INTERVAL*NPHYS, (INTERVAL+1)*NPHYS)
            aj[left_slice] = weights[ROW]*linear.L[INTERVAL,COMPONENT]/problem.chart.scale[left_slice]
            aj[right_slice] = weights[ROW]*linear.R[INTERVAL,COMPONENT]/problem.chart.scale[right_slice]
            aj[-3:] = weights[ROW]*linear.P[INTERVAL,COMPONENT]/problem.chart.scale[-3:]
        row_norm = stats(aj)["L2"]
        report["focus_precision_diagnostics"] = dict(
            separately_formed_f64_coefficient_row=writer.array("focus-formed-f64-row", aj,
                "Diagnostic floating Wr*L/R/P/S row; original matvec operation order remains authoritative"),
            row_L2=row_norm,
            inverse_row_error_scales={name:
                row_norm*value["report"]["original_residual_L2"]/(DAMPING*DAMPING)
                for name,value in solve_reports.items()},
            exact_arithmetic_basis="H >= lambda^2 I implies |a_row H^-1 residual| <= ||a_row||2 ||residual||2/lambda^2",
            limitations=[
                "Stored residual norms and this separately formed row use ordinary floating arithmetic",
                "No validated enclosure for operator multiplication or residual readout error is provided",
                "These are precision diagnostics, not new acceptance or attribution thresholds"])
        report["original_trial"] = dict(alpha=alpha,
            original_accepted_record=accepted_trials[0],
            fresh_nonlinear_trial_evaluations_in_this_diagnostic=0,
            actual63_warm_sha256=status["latest_warm_sha256"],
            scientific_full_BVP_or_native_acceptance_claimed=False)
        report["original_model_scalars"] = dict(
            fixed_weight_merit_before=model["fixed_weight_merit_before"],
            original_unconstrained_LSMR=model["unconstrained_LSMR"],
            original_selector=model["actual_direction_selection"],
            original_conditional_recovery_residual_L2=data["last_recovery"]["factor_solve_report"]["original_residual_L2"])
        report["new_computation_accounting"] = dict(
            original_base_evaluations=1, complete_linearization_constructions=1,
            complete_factorizations=1, complete_H_solves=len(solve_reports),
            explicit_A_actions_after_inverse=len(actions),
            initial_AT_b_actions=1,
            inverse_original_A_actions=sum(x["report"]["original_A_calls"] for x in solve_reports.values()),
            inverse_original_AT_actions=sum(x["report"]["original_AT_calls"] for x in solve_reports.values()),
            inverse_additional_reference_A_actions=sum(x["report"]["frozen_reference_extra_A_calls"] for x in solve_reports.values()),
            inverse_additional_reference_AT_actions=sum(x["report"]["frozen_reference_extra_AT_calls"] for x in solve_reports.values()),
            original_column_norm_reconstructions=1, local_root_force_actions=1,
            newly_run_LSMR=0, newly_run_QP=0, newly_run_native=0,
            new_nonlinear_trials=0, new_FD_checks=0,
            no_reconstruction_of_domain_B=True)
        report["reconstructed_factor_report"] = writer.data("reconstructed-complete-factor-report", factor.report)
        report["original_file_byte_ledger"] = writer.data("original-file-byte-ledger", files.checked)
        report["output_arrays"] = writer.manifest()
        report.update(completed=True, elapsed_seconds=time.monotonic()-started,
            maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            continuation_or_new_optimization_requested=False)
        write_json(out/"result.json.gz", report)
        summary = dict(schema=SCHEMA, completed=True, classification=report["classification"],
            source_sha256=report["source_sha256"], original_artifact=PIN,
            original_source_commit=SOURCE_COMMIT, input_binding=report["input_binding"],
            scope=report["scope"], runtime=report["runtime"],
            result=receipt(out/"result.json.gz", out), array_manifest=report["output_arrays"],
            base_reconstruction=report["base_reconstruction"],
            complete_linearization_reconstruction=report["complete_linearization_reconstruction"],
            factor_reconstruction=report["factor_reconstruction"],
            inverse_summary=report["inverse_summary"],
            original_saved_recovery_replay=report["original_saved_recovery_replay"],
            original_local_center_vs_complete_center_restriction=report["original_local_center_vs_complete_center_restriction"],
            saved_action_rechecks=report["saved_action_rechecks"],
            focus_row=report["focus_row"], focus_L_R_P_contributions=row_chains,
            focus_precision_diagnostics=report["focus_precision_diagnostics"],
            original_selected_alpha=alpha,
            original_artifact_warm_sha256=status["latest_warm_sha256"],
            B_center_slack=Breports["unconstrained-center"],
            original_saved_B_readback_comparisons=dict(
                recovered=report["original_saved_B_readback"]["recovered_against_saved"],
                selected=report["original_saved_B_readback"]["selected_against_saved"]),
            local_rhs_construction=report["local_rhs_construction"],
            interval461_complete_row_table=report["interval461_complete_row_table"],
            new_computation_accounting=report["new_computation_accounting"],
            elapsed_seconds=report["elapsed_seconds"], maximum_RSS_kib=report["maximum_RSS_kib"],
            no_unique_damping_or_constraint_cause_predeclared=True,
            complete_result_and_all_arrays_preserved=True)
        write_json(out/"summary.json", summary, small=True)
        print(json.dumps(dict(event="actual63_diagnostic", phase="completed",
            original_row=ROW, summary="summary.json", result_sha256=sha(out/"result.json.gz"),
            elapsed_seconds=report["elapsed_seconds"])), flush=True)
        return 0
    except Exception as error:
        report.update(completed=False, failure=repr(error), traceback=traceback.format_exc(),
            elapsed_seconds=time.monotonic()-started,
            failure_is_not_a_native_or_QP_acceptance_result=True,
            maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        if factor is not None:
            report["partial_factor_report"] = factor.report
        if writer is not None:
            report["partial_array_manifest"] = writer.manifest()
        write_json(out/"result.json.gz", report)
        write_json(out/"summary.json", dict(schema=SCHEMA, completed=False,
            source_sha256=sha(__file__), original_artifact=PIN,
            failure=repr(error), traceback=traceback.format_exc(),
            result=receipt(out/"result.json.gz", out),
            elapsed_seconds=report["elapsed_seconds"]), small=True)
        print(json.dumps(dict(event="actual63_diagnostic", phase="failed",
            failure=repr(error))), flush=True)
        return 1
    finally:
        if factor is not None:
            factor.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    fetch = commands.add_parser("fetch", help="Only stream and verify the original public artifact")
    fetch.add_argument("--out", type=Path, required=True)
    analysis = commands.add_parser("analyze", help="Actions-only fixed original model decomposition")
    analysis.add_argument("--artifact-directory", type=Path, required=True)
    analysis.add_argument("--accepted", type=Path, required=True)
    analysis.add_argument("--tail-anchor", type=Path, required=True)
    analysis.add_argument("--out", type=Path, required=True)
    analysis.add_argument("--budget-seconds", type=float, default=1200.)
    analysis.add_argument("--jac-workers", type=int, default=2)
    args = parser.parse_args()
    return fetch_original(args) if args.command == "fetch" else analyze(args)


if __name__ == "__main__":
    raise SystemExit(main())

