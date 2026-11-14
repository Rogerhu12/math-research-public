#!/usr/bin/env python3
"""Stream R42/R50 strong scaling of the two actual frequency supports.

The existing prepared strong-density construction is reused unchanged
through its output point.  There is no full causal matrix load, fixed-low
nonlinear box recomputation, ODE, source integral or new Node process.
The complete strong joint gate remains a separate R51 verification.

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
from closure_real_head_green_enclosure import ball
from closure_split_joint_io import digest, read, iter_array, metadata_without_array
from tail_middle_frequency_split import compact_upper, ResourceMonitor


BASE_SHA256 = "52c82cb1462f44c397dfee17cb94cd2f8b0b888d1b0c7490543bb569f91ac284"
ACTIVE_MONITOR = None
CELLS = list(range(12, 225))


class StrongResourceMonitor(ResourceMonitor):
    def finish(self, status, error=None):
        super().finish(status, error)
        document = json.loads(self.path.read_text())
        document["monitor_source_sha256"] = document.pop("source_sha256")
        document["source_sha256"] = digest(Path(__file__))
        document["output_prefix"] = str(self.output)
        document["output_exists"] = any(
            Path(str(self.output)+"-"+suffix).exists()
            for suffix in ("density.json.gz", "split.json.gz", "summary.json"))
        self.path.write_text(json.dumps(document, indent=2)+"\n")


def resource_start(args):
    global ACTIVE_MONITOR
    # The inherited monitor records a path; here it is explicitly a prefix.
    args.out = args.out_prefix
    ACTIVE_MONITOR = StrongResourceMonitor(args)


def check(phase, **fields):
    if ACTIVE_MONITOR is not None:
        ACTIVE_MONITOR.check(phase, **fields)


def load_identity_doc(path, name):
    check("input-start", input=name)
    result = (metadata_without_array(path, "gamma_rows")
              if name in ("q_middle", "q_split") else read(path))
    check("input-complete", input=name)
    return result


def validate_q_split(args, documents, hashes):
    split = documents["q_split"]
    dh = hashes[str(args.q_density)]
    if dh not in split["input_hashes"].values():
        raise ValueError("The split comparison package belongs to another q density")
    for path in (args.q_middle, args.q_high):
        if hashes[str(path)] not in split["input_hashes"].values():
            raise ValueError("The split package does not retain the same paid q high response")
    if not (split["original_kernel_identity_bitwise"]
            and split["original_far_and_pure_identity_bitwise"]
            and split["original_kernel_identity_count"] == 213*214//2):
        raise ValueError("The q split must have genuinely reproduced the entire original package")
    if not (split["continuous_strip_unchanged"] and split["independent_far_parameter"]
            and split["complete_mean_and_pointwise_inverse"]):
        raise ValueError("The q strip/full source/far input must be unchanged")
    if split["z_log2"] != -2200:
        raise ValueError("This scaling retains the same independent R18 ball")
    for name, first, last in (("near", 94, 184), ("rest", 186, 8190)):
        group = split["groups"][name]
        if (group["first_mode"], group["last_mode"]) != (first, last):
            raise ValueError("The actual disjoint frequency supports changed")


def finish_split(args, documents, hashes, density, density_record, sigma,
                 sminus, splus, infinite_scale, source_hashes, started, paths):
    split = documents["q_split"]
    original_rows = {r["cell"]: r for r in split["cells"]}
    if sorted(original_rows) != CELLS:
        raise ValueError("Every strong source and target cell is required")
    source_hashes = dict(source_hashes)
    source_hashes[Path(__file__).name] = digest(Path(__file__))
    source_hashes["closure_split_joint_io.py"] = digest(
        Path(__file__).with_name("closure_split_joint_io.py"))
    source_hashes["tail_middle_frequency_split.py"] = digest(
        Path(__file__).with_name("tail_middle_frequency_split.py"))
    new_hashes = dict(hashes)
    new_hashes[str(paths["density"])] = density_record["sha256"]
    rows = []
    for n in CELLS:
        check("scale-fixed-response", cell=n)
        row = dict(cell=n)
        for group in ("near", "rest"):
            row["pure_low_residual_"+group] = ball_record(
                (splus*splus/sigma[n]*ball(original_rows[n]["pure_low_residual_"+group])).upper())
            row["far_boundary_"+group] = ball_record(
                (ball(original_rows[n]["far_boundary_"+group])/sigma[n]).upper())
        rows.append(row)
    meta = dict(
        status="Strong M20 same-q-strip two-support kernels; actual joint gates remain to be evaluated",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        theorem="R42 same-strip rescaling and R50 exact frequency supports",
        groups=split["groups"], shared_comparison_window=split["shared_comparison_window"],
        cells=rows, z_log2=-2200, independent_far_parameter=True,
        complete_mean_and_pointwise_inverse=True, all46_low_parameters_retained=True,
        continuous_strip_unchanged=True,
        continuous_strip_origin=density["continuous_strip_origin"],
        q_split_origin=dict(path=str(args.q_split), sha256=hashes[str(args.q_split)]),
        q_original_kernel_identity_bitwise=split["original_kernel_identity_bitwise"],
        q_original_far_and_pure_identity_bitwise=split["original_far_and_pure_identity_bitwise"],
        q_original_kernel_identity_count=split["original_kernel_identity_count"],
        original_kernel_identity_bitwise=False,
        original_far_and_pure_identity_bitwise=False,
        original_kernel_identity_count=0,
        identity_scope="Only the q-origin package reproduced original q values bitwise. Strong values are new rigorous rescaled uppers and are not asserted equal to q.",
        rescaled_causal_entry_count=213*214//2,
        strong_scale_semantics=dict(
            sigma="sigma_n=Xbar_strong,n/Xbar_q,n using their defined exact dyadic envelopes",
            gamma="Both groups: Gamma_s[k,n]=(sigma_n^2/sigma_k)*Gamma_q[k,n], rounded upward",
            pure="Each group: pure_s[k]<=sigma_plus^2/sigma_k*pure_q[k]; original universal complete-source envelope, not a proportional Fourier-state assumption",
            far="Each group: far_s[k]<=far_q[k]/sigma_k on unchanged independentZ=2^-2200",
            infinite_gamma_and_pure="sigma_plus^2/sigma_minus times the original upper",
            infinite_deep_boundary="original bound/sigma_minus"),
        sigma_lower=ball_record(sminus), sigma_upper=ball_record(splus),
        infinite_radius=split["infinite_radius"],
        deep_high_boundary=ball_record((ball(split["deep_high_boundary"])/sminus).upper()),
        pure_low_infinite_residual=ball_record(
            (infinite_scale*ball(split["pure_low_infinite_residual"])).upper()),
        split_gamma_dyadic_precision_bits=32,
        split_gamma_rounding="Each rescaled upper is rounded upward again; this added relative inflation is less than2^-31",
        gamma_semantics="Exactly the same true near94..184/rest186..8190 supports, with new strong physical normalization",
        pure_and_far_semantics=split["pure_and_far_semantics"],
        input_hashes=new_hashes, source_hashes=source_hashes,
        source_sha256=digest(Path(__file__)), base_source_sha256=BASE_SHA256,
        nonlinear_joint_gates_evaluated=False, full_head_closed=False,
        source_gates=density["gates"],
        new_ODE_or_source_integrations=0)
    target = paths["split"]
    count = 0
    seen = []
    with target.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0) as out:
            out.write(json.dumps(meta, separators=(",", ":"))[:-1].encode())
            out.write(b',"gamma_rows":[')
            for position, old in enumerate(iter_array(args.q_split, "gamma_rows")):
                k = old["output_cell"]
                seen.append(k)
                check("scale-causal-row", cell=k)
                if [r["source_cell"] for r in old["sources"]] != list(range(k, 225)):
                    raise ValueError("A q causal source row is incomplete")
                sources = []
                for item in old["sources"]:
                    n = item["source_cell"]
                    factor = sigma[n]**2/sigma[k]
                    row = dict(source_cell=n)
                    for group in ("near", "rest"):
                        row[group+"_gamma"] = compact_upper(
                            (factor*ball(item[group+"_gamma"])).upper())
                        row[group+"_maximizing_band"] = item[group+"_maximizing_band"]
                    sources.append(row)
                    count += 1
                if position:
                    out.write(b",")
                out.write(json.dumps(dict(output_cell=k, sources=sources),
                                     separators=(",", ":")).encode())
            out.write(b"]}\n")
    if seen != CELLS or count != 213*214//2:
        raise ValueError("The full strong triangle was not covered")
    if target.stat().st_size >= 5_000_000:
        raise ValueError("The compressed strong ledger exceeds the file limit")
    record = dict(path=str(target), bytes=target.stat().st_size, sha256=digest(target))
    summary = dict(
        status="Complete strong M20 same-q-strip density and split rescaling, not a joint existence certificate",
        author=meta["author"], files=[density_record, record],
        gates=density["gates"], rescaled_causal_entry_count=count,
        q_split_origin=meta["q_split_origin"],
        strong_scale_semantics=meta["strong_scale_semantics"],
        sigma_lower=meta["sigma_lower"], sigma_upper=meta["sigma_upper"],
        original_strong_native_strip_not_reused=True,
        continuous_strip_origin=density["continuous_strip_origin"],
        input_hashes=new_hashes, source_hashes=source_hashes,
        no_new_radial_integrations=True, new_Node=False,
        full641_joint_gates_paid=False,
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    paths["summary"].write_text(json.dumps(summary, indent=2)+"\n")
    print(json.dumps(dict(output=str(paths["summary"]), files=summary["files"],
        gates=summary["gates"], seconds=summary["elapsed_seconds"],
        RSS_KiB=summary["peak_RSS_KiB"])), flush=True)


def main():
    path = Path(__file__).with_name("tail_r42_same_strip_strong_high.py")
    original = path.read_text()
    if digest(path) != BASE_SHA256:
        raise ValueError("The complete prepared same-strip density source changed")
    source = original
    changes = [
        ('    args = parser.parse_args()',
         '    parser.add_argument("--q-split", type=Path, required=True)\n'
         '    parser.add_argument("--resource-out", type=Path, required=True)\n'
         '    parser.add_argument("--rss-limit-mib", type=int, default=120)\n'
         '    args = parser.parse_args()\n'
         '    _resource_start(args)'),
        ('    names = ("density.json.gz", "middle.json.gz", "high.json.gz", "summary.json")',
         '    names = ("density.json.gz", "split.json.gz", "summary.json")'),
        ('    for name in ("q_density", "strong_density", "q_high", "q_middle"):',
         '    for name in ("q_density", "strong_density", "q_high", "q_middle", "q_split"):'),
        ('        docs[name], raw = load_json(path)\n        hashes[str(path)] = sha(raw)',
         '        docs[name] = _load_identity_doc(path, name)\n'
         '        hashes[str(path)] = _digest(path)'),
        ('    cells = list(range(12, 225))',
         '    _validate_q_split(args, docs, hashes)\n'
         '    cells = list(range(12, 225))'),
        ('    density = dict(',
         '    source_hashes.update(_extra_source_hashes)\n'
         '    density = dict('),
        ('    new_hashes = dict(hashes)',
         '    _finish_split(args, docs, hashes, density, density_record, sigma,\n'
         '                  sminus, splus, infinite_scale, source_hashes, started, paths)\n'
         '    return\n'
         '    new_hashes = dict(hashes)'),
    ]
    for before, after in changes:
        if source.count(before) != 1:
            raise ValueError("A frozen strong-density source anchor is no longer unique")
        source = source.replace(before, after)
    module = types.ModuleType("tail_strong_split_density_replay")
    module.__file__ = str(path)
    module.__dict__.update(
        _resource_start=resource_start, _load_identity_doc=load_identity_doc,
        _digest=digest, _validate_q_split=validate_q_split,
        _finish_split=finish_split,
        _extra_source_hashes={
            Path(__file__).name: digest(Path(__file__)),
            "closure_split_joint_io.py": digest(Path(__file__).with_name("closure_split_joint_io.py")),
            "tail_middle_frequency_split.py": digest(Path(__file__).with_name("tail_middle_frequency_split.py"))})
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
