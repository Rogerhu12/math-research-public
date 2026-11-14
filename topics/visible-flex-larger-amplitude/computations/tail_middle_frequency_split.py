#!/usr/bin/env python3
"""R50 split of the existing causal kernels, without new integration.

True unknown supports are near=94..184 and rest=186..8190.  The saved
130..192 comparison window is conservatively reused for both restrictions.
The immutable original propagation arithmetic is executed unchanged;
callbacks only retain the two maxima and two positive boundary sums.

No existence or joint contraction is asserted by this derived ledger.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
import types

from flint import arb
from closure_real_head_source_enclosure import ball_record
from closure_real_head_green_enclosure import load_json, ball
from closure_split_joint_io import (
    digest, read, iter_array, metadata_without_array)


BASE_SHA256 = "9b9c5b5fd0c76a853dc07aa6c4f5ceaea54594e445e961320c7debf3bd867346"
CELLS = tuple(range(12, 225))
EXPECTED_BANDS = ((94, 96), (98, 104), (106, 112), (114, 128),
                  (130, 192), (194, 256), (258, 512), (514, 1024),
                  (1026, 2048), (2050, 4096), (4098, 8190))
ACTIVE_MONITOR = None


class ResourceMonitor:
    def __init__(self, args):
        self.path = args.resource_out
        self.trace = self.path.with_suffix(".jsonl")
        if self.path.exists() or self.trace.exists():
            raise FileExistsError("Resource records also require a fresh prefix")
        self.started = time.monotonic()
        self.limit = args.rss_limit_mib*1024
        self.output = args.out
        self.rows = 0
        self.last = None
        self.check("start")

    def check(self, phase, **fields):
        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        self.rows += 1
        self.last = dict(sequence=self.rows, phase=phase, peak_RSS_KiB=peak,
                         seconds=time.monotonic()-self.started, **fields)
        with self.trace.open("a") as f:
            f.write(json.dumps(self.last, separators=(",", ":"))+"\n")
        if peak > self.limit:
            self.finish("stopped_at_RSS_limit", "Observed peak exceeds the authorized bound")
            raise MemoryError(f"Own RSS guard: {peak}KiB exceeds {self.limit}KiB")

    def finish(self, status, error=None):
        value = dict(status=status, error=error, limit_KiB=self.limit,
                     peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                     elapsed_seconds=time.monotonic()-self.started,
                     resource_events=self.rows, last_event=self.last,
                     trace=str(self.trace), output=str(self.output),
                     output_exists=self.output.exists(),
                     source_sha256=digest(Path(__file__)))
        self.path.write_text(json.dumps(value, indent=2)+"\n")


def resource_start(args):
    global ACTIVE_MONITOR
    ACTIVE_MONITOR = ResourceMonitor(args)


def resource_check(phase, **fields):
    if ACTIVE_MONITOR is not None:
        ACTIVE_MONITOR.check(phase, **fields)


def exact_record(record):
    """Drop display text only; retain both exact dyadic endpoints."""
    return dict(lower=record["lower"], upper=record["upper"])


def compact_upper(value, bits=32):
    """Exact dyadic upper, with relative inflation less than 2^(1-bits)."""
    if not value >= 0 or not value.is_finite():
        raise ArithmeticError("Only finite nonnegative comparison bounds are stored")
    mantissa, exponent = value.upper().man_exp()
    mantissa, exponent = int(mantissa), int(exponent)
    shift = max(0, mantissa.bit_length()-bits)
    mantissa = (mantissa+(1 << shift)-1) >> shift
    exponent += shift
    if mantissa.bit_length() > bits:
        mantissa >>= 1
        exponent += 1
    point = dict(mantissa=str(mantissa), binary_exponent=exponent)
    return dict(lower=point, upper=point)


def load_trimmed(path, name):
    """Retain exactly the original arithmetic's inputs, never full JSON rows."""
    resource_check("input-start", input=name)
    if name in ("positive", "subhead", "extra_positive", "local"):
        meta = metadata_without_array(path, "cell_rows")
        rows = []
        for row in iter_array(path, "cell_rows"):
            resource_check("input-cell", input=name, cell=row["cell"])
            if name != "local":
                rows.append(dict(cell=row["cell"], positive_cell_matrices=[
                    [[exact_record(v) for v in line] for line in matrix]
                    for matrix in row["positive_cell_matrices"]]))
            else:
                keys = ("canonical_Q_end", "canonical_Xi_over_nu_end",
                        "local_gamma", "physical_norm_end",
                        "homogeneous_peak_over_V", "homogeneous_physical_end")
                rows.append(dict(cell=row["cell"], bands=[
                    {key: exact_record(band[key]) for key in keys}
                    for band in row["bands"]]))
        return dict(input_hashes=meta["input_hashes"], bands=meta["bands"], cell_rows=rows)
    if name == "hybrid":
        meta = metadata_without_array(path, "bands")
        bands = []
        for b in iter_array(path, "bands"):
            resource_check("input-band", input=name, first_mode=b["first_mode"])
            bands.append(dict(first_mode=b["first_mode"], last_mode=b["last_mode"]))
        return dict(input_hashes=meta["input_hashes"], bands=bands)
    if name == "density":
        doc = read(path)
        keys = ("B", "canonical_total_envelope", "Q_coefficient", "mu_lower",
                "mu_upper", "w_lower", "TV_log_w_upper", "normalized_width_upper",
                "tau_inner", "tau_outer")
        return dict(input_hashes=doc["input_hashes"], gates=doc["gates"],
                    rows=[dict(cell=r["cell"], **{key: exact_record(r[key]) for key in keys})
                          for r in doc["rows"]])
    return read(path)


class SplitCollector:
    def __init__(self, bands):
        actual = tuple((b["first_mode"], b["last_mode"]) for b in bands)
        if actual != EXPECTED_BANDS:
            raise ValueError("The original eleven comparison bands must be unchanged")
        self.gamma = {
            group: {(n, j): arb(0) for n in CELLS for j in range(n, 225)}
            for group in ("near", "rest")}
        self.argmax = {group: {key: None for key in rows}
                       for group, rows in self.gamma.items()}
        self.far = {group: {n: arb(0) for n in CELLS} for group in ("near", "rest")}
        self.witness = {}

    @staticmethod
    def groups(band):
        return ("near",) if band < 4 else ("near", "rest") if band == 4 else ("rest",)

    def record(self, n, j, band, value):
        if (n, j) == (12, 15):
            self.witness[band] = value.upper()
        for group in self.groups(band):
            if value > self.gamma[group][n, j]:
                self.gamma[group][n, j] = value.upper()
                self.argmax[group][n, j] = band

    def record_far(self, n, band, value):
        for group in self.groups(band):
            self.far[group][n] = (self.far[group][n]+value).upper()

    def finish(self, args, hashes, densityhash, original_gamma, original_far,
               started, base_source_hash):
        if args.out.exists():
            raise FileExistsError("Use a fresh output; never overwrite an original package")
        old = metadata_without_array(args.original_middle, "gamma_rows")
        hashes[str(args.original_middle)] = digest(args.original_middle)
        if densityhash not in old["input_hashes"].values():
            raise ValueError("The comparison middle package has another true density")
        if old["source_sha256"] != BASE_SHA256 or not all(old["gates"].values()):
            raise ValueError("The original complete causal package is not the frozen paid one")
        compared, seen = 0, []
        for row in iter_array(args.original_middle, "gamma_rows"):
            n = row["output_cell"]
            resource_check("verify-original-row", cell=n)
            seen.append(n)
            if sorted(s["source_cell"] for s in row["sources"]) != list(range(n, 225)):
                raise ValueError("Original source-cell coverage is incomplete")
            for entry in row["sources"]:
                j = entry["source_cell"]
                if original_gamma[n, j] != ball(entry["gamma"]):
                    raise ArithmeticError(f"The unchanged original kernel did not reproduce at {n},{j}")
                if max(self.gamma["near"][n, j], self.gamma["rest"][n, j]) != original_gamma[n, j]:
                    raise AssertionError("The two covers lost an original comparison band")
                compared += 1
        if seen != list(CELLS):
            raise ValueError("Original output-cell coverage is incomplete")
        old_cells = {r["cell"]: r for r in old["cells"]}
        ratio = arb(2)**(2*(args.z_log2-old["z_log2"]))
        for n in CELLS:
            if original_far[n] != (ball(old_cells[n]["far_boundary"])*ratio).upper():
                raise ArithmeticError(f"The same far lift did not reproduce at cell {n}")
        del old, old_cells

        high = read(args.reference_high)
        hashes[str(args.reference_high)] = digest(args.reference_high)
        if densityhash not in high["input_hashes"].values():
            raise ValueError("Reference high field uses another density/continuous strip")
        if hashes[str(args.original_middle)] not in high["input_hashes"].values():
            raise ValueError("Reference high field does not cite the frozen original middle kernel")
        if high["z_log2"] != args.z_log2 or not all(high["gates"].values()):
            raise ValueError("Use the complete paid high package at this independent far radius")
        if not high["complete_mean_and_pointwise_inverse"] or not high["independent_far_parameter"]:
            raise ValueError("The complete mean and independent far parameter must remain present")
        high_rows = {r["cell"]: r for r in high["rows"]}
        infinity = {key: high[key] for key in (
            "infinite_radius", "deep_high_boundary", "pure_low_infinite_residual")}

        wide = metadata_without_array(args.wide_low, "bands")
        hashes[str(args.wide_low)] = digest(args.wide_low)
        if densityhash not in wide["input_hashes"].values() or not wide.get("wide_low_adapter_sha256"):
            raise ValueError("The pure-low response must retain its paid wider reference strip")
        pure = {group: {n: arb(0) for n in CELLS} for group in ("near", "rest")}
        pure_original = {n: arb(0) for n in CELLS}
        seen_bands = []
        for bi, band in enumerate(iter_array(args.wide_low, "bands")):
            resource_check("wide-pure-band", band=bi)
            seen_bands.append((band["first_mode"], band["last_mode"]))
            rows = band["low_source_residual"]["rows"]
            if sorted(row["cell"] for row in rows) != list(CELLS):
                raise ValueError("A pure-low band lacks a true cell")
            for row in rows:
                n = row["cell"]
                value = 2*ball(row["combined_bound"])
                pure_original[n] = (pure_original[n]+value).upper()
                for group in self.groups(bi):
                    pure[group][n] = (pure[group][n]+value).upper()
        if tuple(seen_bands) != EXPECTED_BANDS:
            raise ValueError("The complete pure-low band cover changed")
        for n in CELLS:
            if pure_original[n] != ball(high_rows[n]["pure_low_residual"]):
                raise ArithmeticError(f"The complete original pure-low residual did not reproduce at {n}")
        del wide, high_rows, high
        rows = [
            dict(cell=n, **{
                f"pure_low_residual_{group}": ball_record(pure[group][n])
                for group in ("near", "rest")},
                **{f"far_boundary_{group}": ball_record(self.far[group][n])
                   for group in ("near", "rest")})
            for n in CELLS]
        result = dict(
            status="Complete two-support causal kernels derived from the unchanged paid propagation; joint gates not evaluated",
            author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
            groups=dict(near=dict(first_mode=94, last_mode=184, saved_band_indices=list(range(5))),
                        rest=dict(first_mode=186, last_mode=8190, saved_band_indices=list(range(4, 11)))),
            shared_comparison_window=dict(index=4, first_mode=130, last_mode=192,
                explanation="Its proved whole-window upper is used for each disjoint true restriction; no new184 endpoint or new integral is claimed"),
            cells=rows, **infinity, z_log2=args.z_log2,
            independent_far_parameter=True, complete_mean_and_pointwise_inverse=True,
            continuous_strip_unchanged=True,
            gamma_semantics="Each group uses the maximum of the original saved band operator uppers, acting on that group's actual source spectral mass",
            pure_and_far_semantics="Sum positive original band uppers within each cover; the shared130..192 upper is conservatively charged to both groups",
            full_head_closed=False, nonlinear_joint_gates_evaluated=False,
            original_kernel_identity_count=compared,
            original_kernel_identity_bitwise=True,
            original_far_and_pure_identity_bitwise=True,
            split_gamma_dyadic_precision_bits=32,
            split_gamma_rounding="Each exported dyadic is rounded upward; relative inflation is less than2^-31. Original kernel identities are checked before this output rounding.",
            edge_12_15_by_saved_band=[
                dict(index=bi, first_mode=EXPECTED_BANDS[bi][0],
                     last_mode=EXPECTED_BANDS[bi][1], gamma=ball_record(self.witness[bi]))
                for bi in range(len(EXPECTED_BANDS))],
            source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            base_source_sha256=base_source_hash, input_hashes=hashes,
            streaming_reader_sha256=digest(Path(__file__).with_name("closure_split_joint_io.py")),
            new_ODE_or_source_integrations=0,
            elapsed_seconds=time.monotonic()-started,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        if args.out.suffix != ".gz":
            raise ValueError("The complete derived ledger must be gzip")
        # Keep at most one output row's JSON objects; never build all45k
        # exported records or an entire uncompressed JSON string together.
        with args.out.open("wb") as raw:
            with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0) as out:
                out.write(json.dumps(result, separators=(",", ":"))[:-1].encode())
                out.write(b',"gamma_rows":[')
                for position, n in enumerate(CELLS):
                    resource_check("output-row", cell=n)
                    if position:
                        out.write(b",")
                    row = dict(output_cell=n, sources=[
                        dict(source_cell=j,
                             near_gamma=compact_upper(self.gamma["near"][n, j]),
                             rest_gamma=compact_upper(self.gamma["rest"][n, j]),
                             near_maximizing_band=self.argmax["near"][n, j],
                             rest_maximizing_band=self.argmax["rest"][n, j])
                        for j in range(n, 225)])
                    out.write(json.dumps(row, separators=(",", ":")).encode())
                out.write(b"]}\n")
        size = args.out.stat().st_size
        if size >= 5_000_000:
            raise ValueError("The complete derived ledger must stay below5MB")
        print(json.dumps(dict(output=str(args.out), bytes=size,
            sha256=digest(args.out),
            original_kernel_identity_count=compared,
            near_edge_12_15=ball_record(self.gamma["near"][12, 15]),
            rest_edge_12_15=ball_record(self.gamma["rest"][12, 15]),
            seconds=result["elapsed_seconds"], RSS_KiB=result["peak_RSS_KiB"])), flush=True)


def main():
    path = Path(__file__).with_name("tail_r33_middle_causal_box.py")
    original = path.read_text()
    if hashlib.sha256(path.read_bytes()).hexdigest() != BASE_SHA256:
        raise ValueError("The frozen causal propagation source has changed")
    source = original
    changes = [
        ('        docs[name],raw=load_json(path);hashes[str(path)]=hashlib.sha256(raw).hexdigest()',
         '        docs[name]=_load_trimmed(path,name);hashes[str(path)]=_digest(path)'),
        ('    args=p.parse_args();ctx.prec=192;started=time.monotonic()',
         '    for name in ("wide-low","original-middle","reference-high","resource-out"):\n'
         '        p.add_argument("--"+name,type=Path,required=True)\n'
         '    p.add_argument("--rss-limit-mib",type=int,default=120)\n'
         '    args=p.parse_args();ctx.prec=192;started=time.monotonic()\n'
         '    if args.out.exists():raise FileExistsError("Use a fresh output")\n'
         '    _resource_start(args)'),
        ('            cfg[n,bi]=dict(B=B,A=A,decay=decay,qweight=qweight,zweight=zweight,',
         '            _resource_check("config-cell",cell=n,band=bi)\n'
         '            cfg[n,bi]=dict(B=B,A=A,decay=decay,qweight=qweight,zweight=zweight,'),
        ('    for bi,b in enumerate(bands):\n        for j in range(224,11,-1):',
         '    _split=_SplitCollector(bands)\n'
         '    for bi,b in enumerate(bands):\n        for j in range(224,11,-1):'),
        ('            peak=2*c["peak"]',
         '            peak=2*c["peak"]\n'
         '            _split.record(j,j,bi,peak)'),
        ('                if 2*peak>gamma[n,j]:gamma[n,j]=(2*peak).upper();argmax[n,j]=bi',
         '                _split.record(n,j,bi,2*peak)\n'
         '                if 2*peak>gamma[n,j]:gamma[n,j]=(2*peak).upper();argmax[n,j]=bi'),
        ('            far[n]=(far[n]+2*peak).upper()',
         '            far[n]=(far[n]+2*peak).upper()\n'
         '            _split.record_far(n,bi,2*peak)'),
        ('        print(json.dumps(dict(event="band",first=lo,last=b["last_mode"],',
         '        _resource_check("band-complete",band=bi)\n'
         '        print(json.dumps(dict(event="band",first=lo,last=b["last_mode"],'),
        ('    residual={n:far[n] for n in far}',
         '    docs.clear();matrices.clear();cfg.clear();ll.clear()\n'
         '    positive.clear();subhead.clear();local.clear();hybrid.clear()\n'
         '    _split.finish(args,hashes,densityhash,gamma,far,started,_base_source_hash)\n'
         '    return\n'
         '    residual={n:far[n] for n in far}'),
    ]
    for before, after in changes:
        if source.count(before) != 1:
            raise ValueError("A frozen source anchor is no longer unique")
        source = source.replace(before, after)
    module = types.ModuleType("tail_middle_frequency_split_replay")
    module.__file__ = str(path)
    module.__dict__.update(_SplitCollector=SplitCollector, _base_source_hash=BASE_SHA256,
                           _load_trimmed=load_trimmed, _digest=digest,
                           _resource_start=resource_start, _resource_check=resource_check)
    exec(compile(source, str(path), "exec"), module.__dict__)
    try:
        module.main()
    except BaseException as error:
        if ACTIVE_MONITOR is not None:
            ACTIVE_MONITOR.finish("failed", repr(error))
        raise
    else:
        if ACTIVE_MONITOR is not None:
            ACTIVE_MONITOR.finish("complete")


if __name__ == "__main__":
    main()
