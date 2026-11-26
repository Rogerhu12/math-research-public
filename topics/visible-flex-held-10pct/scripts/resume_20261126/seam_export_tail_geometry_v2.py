#!/usr/bin/env python3
"""Bind one actual m3 native scope to its own complete shared-R Fourier map.

No solve is performed. Large native records, stage arrays, and unique-node
indices remain on the runner. An unscaled reference H is not a coupled prefix
certificate or a claim of exact/full surface closure.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
import math
from pathlib import Path
import re
import struct
import subprocess
import sys
import time

from seam_cut_height_compatibility import load_packet
from seam_tail_spectrum_v2 import (
    GEOMETRY_SCHEMA, spectrum_contract, validate_spectrum_container,
)


HERE = Path(__file__).resolve().parent
TOPIC = HERE.parents[1]
PARAMETER_SEMANTIC_SOURCE_SHAS = {
    "950f-tail-stage-core.mjs": "53fdd936cf65f0a42929b6ce42c6ea12f183628abc9c9f3a351aac9c31ffbd6d",
    "950f-tail-subdivision.mjs": "e44317579d483147aa7fe73b086aba059695aa0f675b831c178902a2c0cb62e6",
    "closing_recalibrated_tail.mjs": "4a109f26b0e6c9741dfff678c0fe42da4935bfda9c605e55688e97848aef0dd6",
    "closing_weighted_tail.mjs": "740e672edee58cff7a15f89d75e181577dd439c1c62777c57d0d0ab1af32141e",
}
STAGE_PARAMETER_TAIL = (
    "modes:M,spacing,depth,physicalDepth,shootingParts:stages.parts,steps,"
    "quadrature,linearFar,linearSteps,linearMethod:'stable-momentum-cusp-subdivision',"
    "projectionFloor,farPadding,nodeIndex"
)
CHORD_PARAMETER_PREFIX = (
    "shootingAlgorithm:'bounded-chord-v1',chordMaxCorrections:maximum,"
    "finalStageJacobian:'fresh-original',"
)
HELPER_SHAS = {
    "extract_q060_native_mean_chain.py":
        "51edadb5ca1e2a6c36369c7965788065ff79ab44ce21a219c6d36e3aae896945",
    "extract_q060_stage_from_native_record.py":
        "4eecd166b16aa66cd91a520baafb1530950a0462617c126db1ee507c92cb5f8c",
    "../resume_n4_tail/native_extended/probe_native_frozen_flow.py":
        "42893f210b6d31c59abd04cdfec415a2408a543f726f87d808fc99cf8fad45db",
}


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith(".gz") else raw)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    return {"path": str(Path(path).resolve()), "sha256": sha(path)}


def checked(reference):
    if sha(reference["path"]) != reference["sha256"]:
        raise ValueError("Bound runtime input changed: " + reference["path"])
    return read(reference["path"])


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     allow_nan=False).encode()).hexdigest()


def write(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def fresh_dir(path):
    path = Path(path).resolve()
    repo = TOPIC.parents[1]
    if path == repo or repo in path.parents:
        raise ValueError("Native/stage arrays must remain outside git")
    path.mkdir(parents=True, exist_ok=False)
    return path


def bind_height(packet, reference_path, key, factor, arithmetic):
    source, value = read(reference_path), None
    value = source
    for part in key.split("."):
        value = value[part]
    M = packet["config"]["modes"]
    if (not isinstance(value, list) or len(value) != M or
            not all(isinstance(x, (float, int)) and math.isfinite(x) for x in value)):
        raise ValueError("The bound reference does not contain a complete finite H")
    if not math.isfinite(factor) or not 0 < factor <= 1:
        raise ValueError("Warm factor must be explicit and lie in (0,1]")
    if arithmetic == "python":
        requested = [float(x) * factor ** (j + 1) for j, x in enumerate(value)]
    elif arithmetic == "numpy":
        import numpy as np
        requested = (np.asarray(value, dtype=float) *
                     factor ** np.arange(1, M + 1)).tolist()
    else:
        raise ValueError("Unknown original warm arithmetic")
    actual = packet["request"]["height"]
    cp = packet["response"]["checkpoint"]
    if requested != actual or cp["cutHeight"] != actual:
        raise ValueError("Accepted height is not the declared original request")
    return {
        "reference": ref(reference_path), "reference_key": key,
        "reference_height_sha256": canonical_sha(value),
        "requested_height_sha256": canonical_sha(actual),
        "factor": factor, "factor_exact_binary": str(Q.from_float(factor)),
        "original_arithmetic": arithmetic,
        "role": ("unscaled_reference_height_candidate" if factor == 1
                 else "warm_scaled_reference_height"),
        "unscaled_reference_request_verified": factor == 1,
        "prefix_coupling_verified": False, "exact_full_H_solution_proved": False,
    }


def state_match(record_path, packet):
    """Check exact accepted states with small seeks; hashing follows extraction."""
    record = read(record_path)
    if record.get("status") != "complete" or record.get("returncode") != 0:
        return False
    if not record.get("input") or not record.get("static_metadata"):
        return False
    meta = checked(record["static_metadata"])
    cp, M = packet["response"]["checkpoint"], packet["config"]["modes"]
    if len(meta["stages"]) + 1 != len(cp["states"]):
        return False
    with open(record["input"]["path"], "rb") as stream:
        stream.seek(44)
        if stream.read(64).decode("ascii") != record["payload_token"]:
            return False
        for row in meta["stages"]:
            stream.seek(row["initialOffset"])
            data = stream.read(8 * (2 * M + 2))
            if len(data) != 8 * (2 * M + 2):
                return False
            initial = struct.unpack("<" + "d" * (2 * M + 2), data)
            if (list(initial[:2 * M]) != cp["states"][row["stage"] + 1] or
                    initial[-2:] != (0.0, 0.0)):
                return False
    return True


def select_native(packet, explicit=None, directory=None):
    if bool(explicit) == bool(directory):
        raise ValueError("Give one native record or its containing native-runs directory")
    if explicit:
        if not state_match(explicit, packet):
            raise ValueError("Explicit native evaluation is not of these accepted states")
        return Path(explicit).resolve()
    candidates = sorted(Path(directory).rglob("*-record.json"),
                        key=lambda p: p.stat().st_mtime_ns, reverse=True)
    for candidate in candidates:
        if state_match(candidate, packet):
            return candidate.resolve()
    raise ValueError("No completed native evaluation exactly matches the accepted states")


def validate_packet_states(packet, M, spacing, degree=None):
    cp, cfg = packet["response"]["checkpoint"], packet["config"]
    spectrum = spectrum_contract(cfg["modes"], cfg["quadrature"], cfg["spacing"], degree)
    if M != cfg["modes"] or spacing != cfg["spacing"] or cfg["depth"] != 8:
        raise ValueError("Retain the actual m3 dimensions and the declared finite physical depth 8")
    if cp["parameters"]["modes"] != M or cp["parameters"]["spacing"] != spacing:
        raise ValueError("Checkpoint finite dimensions differ")
    if len(cp["states"]) != cp["parameters"]["depth"] + 1:
        raise ValueError("Incomplete finite checkpoint")
    if any(len(row) != 2 * M or not all(math.isfinite(x) for x in row)
           for row in cp["states"]):
        raise ValueError("Incomplete or nonfinite finite state")
    return spectrum


def validate_factory_parameters(physical, cfg, parameters, stage_count):
    """The source spreads factory parameters, then overwrites these exact keys."""
    defaults = dict(modes=2, spacing=6, depth=8, steps=64, quadrature=128,
                    linearFar=48, linearSteps=512, projectionFloor=.05,
                    linearMethod="matrix", shootingParts=1)
    physical_depth = cfg.get("depth", defaults["depth"])
    parts = cfg.get("shootingParts")
    parts = 1 if parts is None else parts  # Original nullish default.
    if type(parts) is not int or parts <= 0:
        raise ValueError("The original shooting subdivision requires positive integral parts")
    overrides = {key: cfg.get(key, defaults[key]) for key in
                 ("modes", "spacing", "steps", "quadrature", "linearFar",
                  "linearSteps", "projectionFloor")}
    overrides.update(depth=stage_count, physicalDepth=physical_depth,
                     shootingParts=parts, linearMethod="stable-momentum-cusp-subdivision",
                     farPadding=overrides["linearFar"] - physical_depth, nodeIndex=0)
    if any(parameters.get(key) != value for key, value in overrides.items()):
        raise ValueError("A source-defined checkpoint parameter override changed")
    for key, value in physical.items():
        if key in overrides:
            # The factory preserves the original input here. E.g. its depth=8
            # and linearMethod='matrix' are NOT the derived checkpoint values.
            if key not in cfg and key not in defaults:
                raise ValueError("Unexpected prederived factory parameter: " + key)
            if value != cfg.get(key, defaults.get(key)):
                raise ValueError("The original factory input differs from its actual config: " + key)
        elif key not in parameters or parameters[key] != value:
            raise ValueError("A complete non-overridden factory parameter changed: " + key)
    return overrides


def validate_stage_parameter_text(text):
    """Check the actual installed parameter regions, including the chord clone.

    The recovered sparse/shared/periodic/chord/native installers change the
    whole stage-core file. Its historical SHA is therefore provenance only.
    These constructor and return expressions are the parameter semantics used
    by validate_factory_parameters; the runtime bytes are separately bound.
    """
    anchors = (
        "const {modes=2,spacing=6,depth:physicalDepth=8,steps=64,quadrature=128,"
        "linearFar=48,linearSteps=512,projectionFloor=.05,linearMethod='matrix',"
        "fastJacobian=false}=options;",
        "const physical=options.tail??createCompactControlledTail(options),"
        "cuspAwareFlow=options.cuspAwareFlow===true;",
        "const nodeIndex=0,farPadding=linearFar-physicalDepth,M=modes,K=2*M,portRatio=2**a;",
        "const stages=subdividePhysical(physical,physicalDepth,options.shootingParts??1),"
        "depth=stages.cells.length;",
    )
    if any(text.count(anchor) != 1 for anchor in anchors):
        raise ValueError("An installed stage-core parameter constructor expression changed")
    objects = re.findall(r"parameters:\{\.\.\.physical\.parameters,([^{}]*)\}", text)
    expected = [STAGE_PARAMETER_TAIL, STAGE_PARAMETER_TAIL]
    if len(objects) == 3:
        expected.append(CHORD_PARAMETER_PREFIX + STAGE_PARAMETER_TAIL)
    if sorted(objects) != sorted(expected):
        raise ValueError("An installed stage-core parameter return expression changed")
    return {
        "constructor_regions_checked": len(anchors),
        "parameter_return_regions_checked": len(objects),
        "bounded_chord_metadata_region_present": len(objects) == 3,
        "source_defined_override_count": 13,
        "parameter_tail_sha256": hashlib.sha256(STAGE_PARAMETER_TAIL.encode()).hexdigest(),
    }


def validate_parameter_sources(packet, native_manifest):
    """Bind actual packet sources to the actual installed native manifest."""
    source_topic = Path(native_manifest["source_topic"]).resolve()
    sources = {}
    for name, historical_sha in PARAMETER_SEMANTIC_SOURCE_SHAS.items():
        path = source_topic / "scripts" / name
        matches = [item for item in native_manifest["owned_sources"]
                   if Path(item["path"]).resolve() == path]
        if len(matches) != 1:
            raise ValueError("Actual parameter source is absent or duplicated in native manifest: " + name)
        source = matches[0]
        actual_sha = sha(path)
        if (actual_sha != source["sha256"] or
                actual_sha != packet["source_sha256"].get(name)):
            raise ValueError("Actual packet/native/installed parameter source differs: " + name)
        # These three files are not patched by the recovered installer chain.
        # The stage core is patched; check its parameter expressions below.
        if name != "950f-tail-stage-core.mjs" and actual_sha != historical_sha:
            raise ValueError("An unchanged reviewed factory/subdivision source differs: " + name)
        sources[name] = dict(path=str(path), sha256=actual_sha)
    regions = validate_stage_parameter_text(
        (source_topic / "scripts/950f-tail-stage-core.mjs").read_text())
    return {
        "actual_installed_sources": sources,
        "reviewed_semantic_source_sha256": PARAMETER_SEMANTIC_SOURCE_SHAS,
        "historical_stage_core_whole_sha_used_as_runtime_gate": False,
        "installed_stage_parameter_regions": regions,
    }


def validate_native_identity(record, native_manifest, packet, source_port):
    """Cross-bind actual config, physical metric, ABI and frozen native bytes."""
    meta, port = checked(record["static_metadata"]), read(source_port)
    cfg, cp = packet["config"], packet["response"]["checkpoint"]
    S, M = len(cp["states"]) - 1, cfg["modes"]
    if native_manifest["schema"] != "n4-native-batch-adapter-v1":
        raise ValueError("Unexpected original native manifest schema")
    if meta["manifest"] != record["manifest"]:
        raise ValueError("Native metadata and actual evaluation bind different manifests")
    if [row["stage"] for row in meta["stages"]] != list(range(S)):
        raise ValueError("Native static stage order/count differs from the accepted checkpoint")
    # These are the reviewed original createCompactTailShooting defaults.
    # In particular cuspAwareFlow is true ONLY for an explicit boolean true;
    # absence does not silently enable the current native cusp-aware branch.
    expected = {
        "spacing": cfg.get("spacing", 6), "quadrature": cfg.get("quadrature", 128),
        "steps": cfg.get("steps", 64), "projectionFloor": cfg.get("projectionFloor", .05),
        "orientation": port["parameters"]["orientation"],
        "cuspAwareFlow": cfg.get("cuspAwareFlow") is True,
    }
    expected.update(M=M, stageCount=S)
    if any(meta["scope"].get(k) != v for k, v in expected.items()):
        raise ValueError("Native static scope differs from the actual accepted config")
    if any(meta["scope"].get(k) != v for k, v in native_manifest["fixed_scope"].items()):
        raise ValueError("Original native manifest scope differs from its static metadata")
    # The physical factory keeps its complete input/default dictionary; the
    # stage core then overwrites depth and its other documented derived keys.
    # Validate both meanings explicitly rather than conflating depth 8 with
    # the actual shooting-stage count. All untouched physical keys remain bound.
    parameter_sources = validate_parameter_sources(packet, native_manifest)
    physical = meta["physicalParameters"]
    parameter_overrides = validate_factory_parameters(physical, cfg, cp["parameters"], S)
    if any(k not in physical or physical[k] != v for k, v in port["parameters"].items()):
        raise ValueError("Native mean chain differs from an explicit original port parameter")
    if meta["original_scalar_and_variational_grid_bytes_equal"] is not True:
        raise ValueError("Original scalar/variational grid identity is not established")
    if type(record["withJac"]) is not bool:
        raise ValueError("Native Jacobian flag is not an explicit original boolean")
    data = Path(record["input"]["path"]).read_bytes()
    if hashlib.sha256(data).hexdigest() != record["input"]["sha256"]:
        raise ValueError("Actual native input bytes changed")
    N, spacing = cfg["quadrature"], cfg["spacing"]
    nq = N // math.gcd(N, spacing)
    if (data[:8] != b"VFN4LD01" or len(data) != meta["counts"]["inputBytes"] or
            struct.unpack_from("<9i", data, 8) !=
            (1, M, N, spacing, nq, 30, 20, S, int(record["withJac"]))):
        raise ValueError("Original native input ABI or finite scope differs")
    token = hashlib.sha256(data[:44] + data[108:]).hexdigest()
    if data[44:108].decode("ascii") != token or token != record["payload_token"]:
        raise ValueError("Original input payload token does not hash its actual bytes")
    if struct.unpack_from("<4d", data, 108) != (expected["projectionFloor"], 8e-14, 5e-12, 1e-300):
        raise ValueError("Original native root floor/tolerances changed")
    if sha(record["output"]["path"]) != record["output"]["sha256"]:
        raise ValueError("Actual native output bytes changed")
    source_refs = [*native_manifest["owned_sources"],
                   *native_manifest["native_files"].values(),
                   *native_manifest.get("runtime_libraries", [])]
    for reference in source_refs:
        if sha(reference["path"]) != reference["sha256"]:
            raise ValueError("Bound native source/binary/runtime changed: " + reference["path"])
    return {
        "status": "actual_native_scope_metric_abi_and_payload_cross_checked",
        "metadata": record["static_metadata"], "manifest": record["manifest"],
        "input": record["input"], "output": record["output"],
        "accepted_state_vectors_checked": S, "native_source_runtime_files_checked": len(source_refs),
        "complete_checkpoint_physical_parameters_checked": len(physical),
        "source_defined_checkpoint_overrides": parameter_overrides,
        "factory_checkpoint_parameter_sources": parameter_sources,
        "explicit_port_parameters_checked": len(port["parameters"]),
        "original_scalar_variational_grid_identity": True,
        "original_root_gates_changed": False,
    }


def index_shared_nodes(manifest_path, mean_chain_path, outpath):
    manifest, chain = read(manifest_path), read(mean_chain_path)
    spectrum = checked(manifest["spectrumContract"])
    validate_spectrum_container(manifest, spectrum)
    if any(chain["finite_scope"].get(k) != v for k, v in spectrum["finite_scope"].items()):
        raise ValueError("The full shared map and original native chain have different dimensions")
    if manifest["status"] != "selected_stages_share_one_literal_R_C2_definition":
        raise ValueError("Shared-R construction did not finish")
    if manifest["input"] != ref(mean_chain_path):
        raise ValueError("Shared-R export used another original mean chain")
    S = len(chain["mean_chain"]) - 1
    files = {row["stage"]: row for row in manifest["files"]}
    if len(files) != len(manifest["files"]):
        raise ValueError("Duplicate exported stage")
    nodes = {}
    cut = deep = None
    for stage in sorted(files):
        entry, data = files[stage], checked(files[stage])
        validate_spectrum_container(data, spectrum, stage=True)
        if data["spectrumContract"] != manifest["spectrumContract"]:
            raise ValueError("A stage binds another exact spectrum contract file")
        if (data["stage"] != stage or
                data["status"] != "literal_R_stage_with_exact_common_boundary_two_jets" or
                data["sharing"]["mapHash"] != entry["mapHash"] or
                data["boundInput"] != manifest["input"]):
            raise ValueError("Stage identity or shared map hash changed")
        for index, local in ((stage + 1, 0), (stage, len(data["nodes"]) - 1)):
            node = data["nodes"][local]
            value = {"radius": node["radiusJS"], "coefficients": node["coefficients"]}
            digest = canonical_sha(value)
            if index in nodes and nodes[index]["value_sha256"] != digest:
                raise ValueError("Adjacent stages have different literal full two-jets")
            if [node["meanPerturbation"], node["meanBackground"]] != chain["mean_chain"][index]:
                raise ValueError("A shared node changed the original cumulative mean")
            nodes[index] = {
                "node": index, "R_exact_binary": str(Q.from_float(node["radiusJS"])),
                "value_sha256": digest, "stage_file": entry,
                "local_node_index": local, "canonical_definition": node["canonicalDefinition"],
                "mean_perturbation_exact_binary": str(Q.from_float(node["meanPerturbation"])),
                "mean_background_exact_binary": str(Q.from_float(node["meanBackground"])),
            }
            if index == 0:
                cut = nodes[index]
            if index == S:
                deep = nodes[index]
    all_stages = set(files) == set(range(S))
    if all_stages and len(nodes) != S + 1:
        raise ValueError("Complete stage selection lost a canonical boundary node")
    index = {
        "status": "exact_common_boundary_nodes_indexed",
        "geometry_schema": GEOMETRY_SCHEMA, "spectrum_contract": manifest["spectrumContract"],
        "manifest": ref(manifest_path), "mean_chain": ref(mean_chain_path),
        "finite_stage_count": S, "selected_stages": sorted(files),
        "all_stages_exported": all_stages, "unique_boundary_nodes": list(nodes.values()),
        "cut_node": cut, "deep_node": deep,
        "all_finite_stage_adjacencies_verified": all_stages,
        "internal_stage_knots": "Exact binary radius and two-jet arrays in each bound stage file.",
        "arrays_are_new_field_data": True,
    }
    write(outpath, index)
    return index


def export(args):
    start = time.monotonic()
    outdir = fresh_dir(args.outdir)
    background_record = TOPIC / "notes/2026-11-20-m3-m24-warm050-execution.json"
    packet, response, jets, spacing, M, arrays = load_packet(
        args.tail_response, args.source_port, background_record
    )
    spectrum = validate_packet_states(packet, M, spacing, args.degree)
    spectrum_path = outdir / "spectrum-contract.json"
    write(spectrum_path, spectrum)
    height = bind_height(packet, args.height_reference, args.height_reference_key,
                         args.warm_factor, args.height_arithmetic)
    native = select_native(packet, args.native_record, args.native_record_dir)
    native_data = read(native)
    native_manifest = checked(native_data["manifest"])
    protocol = validate_native_identity(native_data, native_manifest, packet, args.source_port)
    source_topic = Path(native_manifest["source_topic"])
    for name, digest in packet["source_sha256"].items():
        if sha(source_topic / "scripts" / name) != digest:
            raise ValueError("Accepted packet source changed: " + name)
    for name, digest in HELPER_SHAS.items():
        if sha(TOPIC / "scripts/resume_n4" / name) != digest:
            raise ValueError("Analysed exporter/mean-chain source changed: " + name)
    summary_path = outdir / "geometry-bundle.json"
    summary = {
        "status": "running", "source": ref(__file__),
        "geometry_schema": GEOMETRY_SCHEMA, "spectrum": spectrum,
        "spectrum_contract": ref(spectrum_path),
        "representation_sources": {name: ref(HERE / name) for name in
            ("seam_tail_spectrum_v2.py", "seam_export_shared_r_tail_v2.mjs")},
        "accepted_packet": ref(args.tail_response), "source_port": ref(args.source_port),
        "native_record": ref(native), "height_identity": height,
        "native_protocol_identity": protocol,
        "original_accepted_gate": {"converged": True, "residual": response["residual"],
                                   "solveTolerance": packet["config"]["solveTolerance"]},
        "source_files": packet["source_sha256"], "finite_scope": spectrum["finite_scope"],
        "original_BVP_solves": 0, "original_tail_solves": 0,
        "continuous_metric_certified": False, "closed_surface_proved": False,
    }
    write(summary_path, summary)
    chain_path = outdir / "original-native-mean-chain.json"
    extract = TOPIC / "scripts/resume_n4/extract_q060_native_mean_chain.py"
    batch = HERE / "seam_export_shared_r_tail_v2.mjs"
    stage_dir = outdir / "shared-R-stages"
    commands = [
        [sys.executable, str(extract), "--checkpoint", str(args.tail_response.resolve()),
         "--native-record", str(native), "--out", str(chain_path)],
        [args.node, str(batch), "--input", str(chain_path), "--outdir", str(stage_dir),
         "--stages", args.stages, "--spectrum-contract", str(spectrum_path),
         "--difference-step", str(args.difference_step)],
    ]
    try:
        for number, command in enumerate(commands):
            with (outdir / ("step-" + str(number) + ".log")).open("w") as stream:
                subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT, check=True)
        node_index_path = outdir / "canonical-boundary-node-index.json"
        index = index_shared_nodes(stage_dir / "manifest.json", chain_path, node_index_path)
        summary.update(
            status="accepted_new_tail_shared_R_representation_exported",
            mean_chain=ref(chain_path), shared_R_manifest=ref(stage_dir / "manifest.json"),
            canonical_node_index=ref(node_index_path),
            all_stages_exported=index["all_stages_exported"],
            selected_stages=index["selected_stages"],
            complete_finite_C2_stage_chain=index["all_stages_exported"],
            actual_cut_stage_exported=index["cut_node"] is not None,
            actual_deep_anchor_exported=index["deep_node"] is not None,
            deep_collar_attached=False, commands=commands, seconds=time.monotonic() - start,
        )
    except Exception as exc:
        summary.update(status="failed", error=repr(exc), commands=commands,
                       seconds=time.monotonic() - start)
        write(summary_path, summary)
        raise
    write(summary_path, summary)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("tail-response", "source-port", "height-reference", "outdir"):
        parser.add_argument("--" + name, type=Path, required=True)
    native = parser.add_mutually_exclusive_group(required=True)
    native.add_argument("--native-record", type=Path)
    native.add_argument("--native-record-dir", type=Path)
    parser.add_argument("--height-reference-key", default="raw_return.candidate_H")
    parser.add_argument("--warm-factor", type=float, required=True)
    parser.add_argument("--height-arithmetic", choices=("python", "numpy"), required=True)
    parser.add_argument("--stages", default="all")
    parser.add_argument("--degree", type=int, help="Explicit finite map band; default is floor((actual N-4)/2)")
    parser.add_argument("--difference-step", type=float, default=.00005)
    parser.add_argument("--node", default="node")
    args = parser.parse_args()
    result = export(args)
    print(json.dumps({key: result[key] for key in (
        "status", "accepted_packet", "height_identity", "selected_stages",
        "all_stages_exported", "seconds"
    )}), flush=True)


if __name__ == "__main__":
    main()
