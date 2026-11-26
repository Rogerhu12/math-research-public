#!/usr/bin/env python3
"""V2 actual m3 native scope -> background, stage0, all shared-R geometry.

Use --phase stage0 first if its continuous cut budget is needed immediately.
Continue the SAME invocation contract with --phase all --resume. Stage0's
actual data and certificate bytes are preserved; only remaining stages are
exported/certified. All complete outputs remain outside the checkout.
"""
import argparse
import copy
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time

from seam_export_tail_geometry_v2 import (
    HERE, TOPIC, HELPER_SHAS, read, sha, ref, checked, bind_height,
    validate_packet_states, select_native, index_shared_nodes,
)
from seam_cut_height_compatibility import load_packet
from seam_restore_true_background import DEFINITION_SHA


SCHEMA = "actual-m3-tail-geometry-pipeline-v2"


def save(path, data):
    path = Path(path)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(data, indent=2, allow_nan=False) + "\n")
    temp.replace(path)


def source_refs():
    names = ("seam_run_tail_geometry_v2.py", "seam_restore_true_background.py",
             "seam_export_tail_geometry_v2.py", "seam_certify_tail_geometry_v2.py",
             "seam_cut_height_compatibility.py", "seam_tail_spectrum_v2.py",
             "seam_export_shared_r_tail_v2.mjs")
    result = {name: ref(HERE / name) for name in names}
    for name, digest in HELPER_SHAS.items():
        path = TOPIC / "scripts/resume_n4" / name
        if sha(path) != digest:
            raise ValueError("The reviewed mean-chain/export helper changed: " + name)
        result["original/" + name] = ref(path)
    return result


def choose_stages_progress(path, kind):
    """Read only a child's manifest/summary; never scan stage arrays for UI."""
    data = read(path)
    if kind == "export":
        rows = data.get("files", [])
        return {"status": data.get("status"), "completed_stages": len(rows),
                "last_stage": rows[-1]["stage"] if rows else None,
                "failed_stage": data.get("failedStage"),
                "child_seconds": data.get("seconds")}
    if kind == "certify":
        rows = data.get("stages", [])
        last = rows[-1] if rows else {}
        return {"status": data.get("status"), "completed_stages": len(rows),
                "last_stage": last.get("stage"),
                "last_metric_upper": last.get("continuous_metric_operator_upper", {}).get("upper"),
                "last_curvature_upper": last.get("principal_curvature_upper", {}).get("upper"),
                "child_seconds": data.get("seconds")}
    return {"status": data.get("status"), "child_seconds": data.get("seconds")}


class Pipeline:
    def __init__(self, args):
        self.args = args
        self.root = args.outdir.resolve()
        repo = TOPIC.parents[1]
        if self.root == repo or repo in self.root.parents:
            raise ValueError("Full geometry data and certificates must stay outside git")
        self.state_path = self.root / "summary.json"
        if args.resume:
            self.state = read(self.state_path)
            if self.state["schema"] != SCHEMA:
                raise ValueError("Not an existing actual geometry pipeline")
        else:
            self.root.mkdir(parents=True, exist_ok=False)
            (self.root / "logs").mkdir()
            (self.root / "steps").mkdir()
            self.state = {"schema": SCHEMA, "status": "preparing", "completed": {},
                          "attempts": {}, "progress": {}, "errors": [],
                          "closed_surface_proved": False, "large_outputs_in_git": False}
        self.start = time.monotonic()
        self.prior_seconds = self.state.get("seconds", 0)

    def save(self):
        self.state["seconds"] = self.prior_seconds + time.monotonic() - self.start
        save(self.state_path, self.state)

    def event(self, event, **fields):
        row = {"event": event, **fields}
        print(json.dumps(row, allow_nan=False), flush=True)

    def directory(self, phase):
        count = self.state["attempts"].get(phase, 0) + 1
        self.state["attempts"][phase] = count
        self.save()
        return self.root / "steps" / (phase + "-" + str(count).zfill(3))

    def run(self, phase, command, output, progress_path=None, kind=None):
        log = self.root / "logs" / (phase + "-" + str(self.state["attempts"][phase]).zfill(3) + ".log")
        self.state.update(status="running", active_phase=phase)
        self.state["progress"][phase] = {"status": "started", "command": command, "log": str(log)}
        self.save()
        self.event("tail_geometry_phase_started", phase=phase, log=str(log))
        last_stamp = None
        last_heartbeat = time.monotonic()
        with log.open("w") as stream:
            env = dict(os.environ, OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1",
                       MKL_NUM_THREADS="1", NUMEXPR_NUM_THREADS="1")
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT, env=env)
            while process.poll() is None:
                if progress_path is not None and Path(progress_path).exists():
                    try:
                        stamp = Path(progress_path).stat().st_mtime_ns
                        if stamp != last_stamp:
                            progress = choose_stages_progress(progress_path, kind)
                            self.state["progress"][phase].update(progress)
                            self.save()
                            self.event("tail_geometry_progress", phase=phase, **progress)
                            last_stamp = stamp
                    except (OSError, ValueError, KeyError):
                        pass  # A child may be in the middle of a non-atomic save.
                if time.monotonic() - last_heartbeat >= 30:
                    current = self.state["progress"][phase]
                    self.save()
                    self.event("tail_geometry_heartbeat", phase=phase,
                               completed_stages=current.get("completed_stages"),
                               last_stage=current.get("last_stage"),
                               seconds=self.state["seconds"])
                    last_heartbeat = time.monotonic()
                time.sleep(1)
            code = process.returncode
        if code:
            tail = log.read_text(errors="replace")[-4000:]
            raise RuntimeError("Actual child failed in " + phase + ", exit " + str(code) +
                               "; preserved log " + str(log) + "\n" + tail)
        result = ref(output)
        self.state["completed"][phase] = result
        self.state["progress"][phase].update(status="completed", result=result, returncode=code)
        if progress_path is not None:
            self.state["progress"][phase].update(choose_stages_progress(progress_path, kind))
        self.save()
        self.event("tail_geometry_phase_completed", phase=phase, result=result)
        return read(output)

    def existing(self, phase):
        reference = self.state["completed"].get(phase)
        return None if reference is None else checked(reference)

    def prepare(self):
        a = self.args
        background = TOPIC / "notes/2026-11-20-m3-m24-warm050-execution.json"
        packet, response, jets, spacing, M, arrays = load_packet(a.tail_response, a.source_port, background)
        spectrum = validate_packet_states(packet, M, spacing, a.degree)
        height = bind_height(packet, a.height_reference, a.height_reference_key,
                             a.warm_factor, a.height_arithmetic)
        old = self.state.get("contract")
        if old is not None:
            native = Path(old["native_record"]["path"])
            checked(old["native_record"])
            if a.native_record and a.native_record.resolve() != native.resolve():
                raise ValueError("Resume selected a different native evaluation")
            if a.native_record_dir and a.native_record_dir.resolve() not in native.resolve().parents:
                raise ValueError("Original selected native record is outside the supplied directory")
            select_native(packet, native, None)
        else:
            native = select_native(packet, a.native_record, a.native_record_dir)
        native_record = read(native)
        native_manifest = checked(native_record["manifest"])
        if Path(native_manifest["source_topic"]).resolve() != a.source_topic.resolve():
            raise ValueError("Explicit source-topic is not the actual accepted native source")
        contract = {
            "accepted_packet": ref(a.tail_response), "source_port": ref(a.source_port),
            "source_topic": str(a.source_topic.resolve()), "native_record": ref(native),
            "node_command": a.node,
            "height_identity": height, "source_files": source_refs(),
            "finite_scope": spectrum["finite_scope"], "spectrum": spectrum,
            "degree": spectrum["degree"], "difference_step": a.difference_step,
            "quadratic_mode_cutoff": a.quadratic_mode_cutoff,
        }
        if old is not None and contract != old:
            raise ValueError("Resume changes the actual packet, source, H role, or numerical representation")
        self.native = native
        self.state["contract"] = contract
        self.state["requested_phase"] = a.phase
        self.save()

    def background(self):
        previous = self.existing("background")
        if previous is not None:
            if (self.args.background_summary and
                    ref(self.args.background_summary) != self.state["completed"]["background"]):
                raise ValueError("Resume supplied a different background proof-reuse record")
            value = previous
        elif self.args.background_summary:
            value = read(self.args.background_summary)
            self.state["completed"]["background"] = ref(self.args.background_summary)
            self.save()
        else:
            out = self.directory("background")
            command = [sys.executable, str(HERE / "seam_restore_true_background.py"),
                       "--source-topic", str(self.args.source_topic.resolve()), "--outdir", str(out),
                       "--node", self.args.node]
            value = self.run("background", command, out / "summary.json",
                             out / "summary.json", "background")
        if (value["status"] != "recorded_R58_definition_reconstructed_and_interval_reuse_checked" or
                value["definition_sha256"] != DEFINITION_SHA):
            raise ValueError("Not a successfully reconstructed identical R58 background")
        checked(value["constants"])
        checked(value["normalization_certificate"])
        if value.get("oracle_complete_integrals_recomputed") is not False:
            raise ValueError("This entry reuses the existing integral proof without rerunning it")
        self.bg = value

    def stage0(self):
        a = self.args
        cut = self.existing("stage0-export")
        if cut is None:
            out = self.directory("stage0-export")
            command = [sys.executable, str(HERE / "seam_export_tail_geometry_v2.py"),
                       "--tail-response", str(a.tail_response.resolve()),
                       "--source-port", str(a.source_port.resolve()),
                       "--native-record", str(self.native),
                       "--height-reference", str(a.height_reference.resolve()),
                       "--height-reference-key", a.height_reference_key,
                       "--warm-factor", str(a.warm_factor),
                       "--height-arithmetic", a.height_arithmetic,
                       "--stages", "0",
                       "--difference-step", str(a.difference_step),
                       "--node", a.node, "--outdir", str(out)]
            if a.degree is not None:
                command.extend(["--degree", str(a.degree)])
            cut = self.run("stage0-export", command, out / "geometry-bundle.json",
                           out / "shared-R-stages/manifest.json", "export")
        if cut["selected_stages"] != [0] or not cut["actual_cut_stage_exported"]:
            raise ValueError("Stage0 phase did not produce the actual cut map")
        if cut["spectrum"] != self.state["contract"]["spectrum"]:
            raise ValueError("The stage0 child changed the declared complete Fourier map")
        cert = self.existing("stage0-certify")
        if cert is None:
            out = self.directory("stage0-certify")
            command = self.cert_command(self.state["completed"]["stage0-export"]["path"], out, "0")
            cert = self.run("stage0-certify", command, out / "summary.json",
                            out / "summary.json", "certify")
        if len(cert["stages"]) != 1 or cert["stages"][0]["stage"] != 0:
            raise ValueError("Stage0 phase did not produce its own continuous certificate")
        self.cut, self.cut_cert = cut, cert
        self.state["stage0_result"] = {
            "finite_scope": cut["finite_scope"], "degree": cut["spectrum"]["degree"],
            "spectrum_contract": cut["spectrum_contract"],
            "geometry_bundle": self.state["completed"]["stage0-export"],
            "tail_certificate_summary": self.state["completed"]["stage0-certify"],
            "certificate": cert["stages"][0]["certificate"],
            "metric_gate_passed": cert["stages"][0]["metric_gate_passed"],
            "curvature_allocation_passed": cert["stages"][0]["curvature_allocation_passed"],
            "metric_upper": cert["stages"][0]["continuous_metric_operator_upper"]["upper"],
            "curvature_upper": cert["stages"][0]["principal_curvature_upper"]["upper"],
        }
        self.save()

    def cert_command(self, bundle, out, stages):
        return [
            sys.executable, str(HERE / "seam_certify_tail_geometry_v2.py"),
            "--geometry-bundle", str(bundle),
            "--constants", self.bg["constants"]["path"],
            "--normalization-certificate", self.bg["normalization_certificate"]["path"],
            "--stages", stages, "--quadratic-mode-cutoff", str(self.args.quadratic_mode_cutoff),
            "--outdir", str(out),
        ]

    def remaining(self):
        cut_manifest = checked(self.cut["shared_R_manifest"])
        chain = checked(self.cut["mean_chain"])
        S = len(chain["mean_chain"]) - 1
        if S < 2:
            raise ValueError("The declared actual depth-8 map has no remaining stages")
        self.S, self.cut_manifest = S, cut_manifest
        completed = self.existing("remaining-export")
        if completed is not None:
            self.remaining_manifest = completed
            return
        prep = self.directory("remaining-input")
        prep.mkdir(parents=True)
        entry = cut_manifest["files"][0]
        data = checked(entry)
        if entry["stage"] != 0 or data["stage"] != 0:
            raise ValueError("Not the previously completed new stage0")
        # The V2 loader checks the original stage's boundInput and spectrum
        # directly. Preserve this stage0 file, all two-jets and its proof bytes.
        anchors = prep / "new-stage0-inner-anchor.json"
        save(anchors, {"reuse_stages": {}, "node_anchors": [
            {"node": 1, "path": entry["path"], "endpoint": "inner"}
        ]})
        self.state["remaining_anchor"] = {
            "original_stage0": entry, "anchors": ref(anchors),
            "map_hash_unchanged": data["sharing"]["mapHash"],
            "original_stage0_bytes_preserved": True,
            "old_other_field_anchor_used": False,
        }
        out = self.directory("remaining-export")
        batch = HERE / "seam_export_shared_r_tail_v2.mjs"
        command = [self.args.node, str(batch), "--input", self.cut["mean_chain"]["path"],
                   "--outdir", str(out), "--stages", ",".join(map(str, range(1, S))),
                   "--anchors", str(anchors),
                   "--spectrum-contract", self.cut["spectrum_contract"]["path"],
                   "--difference-step", str(self.args.difference_step)]
        self.remaining_manifest = self.run("remaining-export", command, out / "manifest.json",
                                           out / "manifest.json", "export")

    def merge_maps(self):
        previous = self.existing("complete-map")
        if previous is not None:
            self.full_bundle = previous
            return
        cut, rest, S = self.cut_manifest, self.remaining_manifest, self.S
        for key in ("geometrySchema", "spectrum", "spectrumContract",
                    "input", "existingCheckpoint", "finiteScope", "degree", "planarModes",
                    "heightModes", "physicalParameters", "physicalStats", "meanContract"):
            if cut[key] != rest[key]:
                raise ValueError("Stage0 and remaining stages changed their field: " + key)
        if rest["status"] != "selected_stages_share_one_literal_R_C2_definition":
            raise ValueError("Remaining stage export did not complete")
        files = {entry["stage"]: entry for entry in [*cut["files"], *rest["files"]]}
        if len(files) != S or set(files) != set(range(S)):
            raise ValueError("The actual exports do not cover every finite stage exactly once")
        left, right = checked(files[0])["nodes"][0], checked(files[1])["nodes"][-1]
        if left["radiusJS"] != right["radiusJS"] or left["coefficients"] != right["coefficients"]:
            raise ValueError("The actual saved stage0 inner jet is not shared with stage1")
        out = self.directory("complete-map")
        out.mkdir(parents=True)
        merged = copy.deepcopy(rest)
        merged.update(
            selectedStages=list(range(S - 1, -1, -1)),
            files=[files[j] for j in range(S - 1, -1, -1)],
            interfaceRepairs=[*cut["interfaceRepairs"], *rest["interfaceRepairs"]],
            exactAdjacentCommonNodeChecks=[{
                "outerStage": 0, "innerStage": 1, "node": 1,
                "exactSharedRadiusAndCartesianTwoJets": True
            }, *rest["exactAdjacentCommonNodeChecks"]],
            stage0Preservation=self.state["remaining_anchor"],
            actualComponentManifests=[self.cut["shared_R_manifest"],
                                      self.state["completed"]["remaining-export"]],
            mergerSource=ref(__file__),
            originalBvpSolvesExecuted=0, shootingIterationsExecuted=0,
            globalContinuousMetricCertified=False,
        )
        if len(merged["exactAdjacentCommonNodeChecks"]) != S - 1:
            raise ValueError("The actual shared adjacency check count is incomplete")
        manifest_path = out / "manifest.json"
        save(manifest_path, merged)
        index_path = out / "canonical-boundary-node-index.json"
        node_index = index_shared_nodes(manifest_path, Path(self.cut["mean_chain"]["path"]), index_path)
        bundle = copy.deepcopy(self.cut)
        bundle.update(
            source=ref(__file__), shared_R_manifest=ref(manifest_path),
            canonical_node_index=ref(index_path), all_stages_exported=True,
            selected_stages=list(range(S)), complete_finite_C2_stage_chain=True,
            actual_deep_anchor_exported=node_index["deep_node"] is not None,
            construction="Preserved this new stage0, then exported only remaining stages using its exact actual inner node as the sole explicit anchor.",
            component_geometry_bundle=self.state["completed"]["stage0-export"],
            component_manifests=merged["actualComponentManifests"],
            stage0_recomputed=False,
        )
        bundle_path = out / "geometry-bundle.json"
        save(bundle_path, bundle)
        self.state["completed"]["complete-map"] = ref(bundle_path)
        self.full_bundle = bundle
        self.save()

    def certify_remaining(self):
        previous = self.existing("remaining-certify")
        if previous is not None:
            self.rest_cert = previous
            return
        out = self.directory("remaining-certify")
        command = self.cert_command(self.state["completed"]["complete-map"]["path"], out,
                                    ",".join(map(str, range(1, self.S))))
        self.rest_cert = self.run("remaining-certify", command, out / "summary.json",
                                  out / "summary.json", "certify")

    def complete(self):
        previous = self.existing("complete-certificates")
        if previous is not None:
            result = previous
        else:
            first, rest, S = self.cut_cert, self.rest_cert, self.S
            for key in ("accepted_packet", "height_identity", "original_mean_chain",
                        "constants", "normalization", "mathematical_sources", "oracle_provenance",
                        "geometry_schema", "spectrum", "spectrum_contract", "representation_sources"):
                if first[key] != rest[key]:
                    raise ValueError("Component certificates do not share the same actual definition: " + key)
            rows = {row["stage"]: row for row in [*first["stages"], *rest["stages"]]}
            if len(rows) != S or set(rows) != set(range(S)):
                raise ValueError("Actual stage certificates do not cover the whole finite tail")
            manifest = checked(self.full_bundle["shared_R_manifest"])
            files = {entry["stage"]: entry for entry in manifest["files"]}
            for stage, row in rows.items():
                proof = checked(row["certificate"])
                if (proof["data"] != files[stage] or proof["map_hash"] != files[stage]["mapHash"] or
                        proof["stage"] != stage):
                    raise ValueError("An existing stage proof is not of the actual merged map")
            deep = rest.get("deep_collar")
            if deep is None:
                raise ValueError("The new whole tail has no actual deep collar certificate")
            checked(deep["certificate"])
            metric = all(row["metric_gate_passed"] for row in rows.values())
            curvature = all(row["curvature_allocation_passed"] for row in rows.values())
            full_metric = metric and deep["metric_gate_passed"]
            full_curvature = curvature and deep["curvature_allocation_passed"]
            injective = (deep["planar_projection_derivative_less_than_one"] and
                         all(row["planar_projection_derivative_less_than_one"] for row in rows.values()))
            result = copy.deepcopy(rest)
            result.update(
                source=ref(__file__), geometry_bundle=self.state["completed"]["complete-map"],
                selected_stages=list(range(S)), stages=[rows[j] for j in range(S)],
                status=("new_whole_tail_disk_metric_curvature_certified" if full_metric and full_curvature
                        else "new_selected_tail_geometry_bounds_recorded"),
                all_finite_stages_audited=True,
                all_finite_stages_certified=metric and curvature,
                all_selected_stage_metric_gates_passed=metric,
                all_selected_stage_curvature_allocations_passed=curvature,
                complete_tail_disk_metric_gate_passed=full_metric,
                complete_tail_disk_curvature_allocation_passed=full_curvature,
                complete_tail_disk_planar_projection_injective=injective,
                finite_tail_to_its_own_deep_disk_C2=True,
                component_certificate_summaries=[self.state["completed"]["stage0-certify"],
                                                self.state["completed"]["remaining-certify"]],
                original_stage0_certificate_reused_unchanged=True,
                stage0_certification_rerun=False,
                seconds=first.get("seconds", 0) + rest.get("seconds", 0),
            )
            out = self.directory("complete-certificates")
            out.mkdir(parents=True)
            path = out / "summary.json"
            save(path, result)
            self.state["completed"]["complete-certificates"] = ref(path)
        failures = [row["stage"] for row in result["stages"]
                    if not row["metric_gate_passed"] or not row["curvature_allocation_passed"]]
        self.state["result"] = {
            "finite_scope": self.full_bundle["finite_scope"],
            "degree": self.full_bundle["spectrum"]["degree"],
            "spectrum_contract": self.full_bundle["spectrum_contract"],
            "geometry_bundle": self.state["completed"]["complete-map"],
            "tail_certificate_summary": self.state["completed"]["complete-certificates"],
            "actual_stages": len(result["stages"]),
            "failed_allocation_stage_count": len(failures),
            "first_failed_allocation_stages": failures[:16],
            "maximum_stage_metric_upper": max(row["continuous_metric_operator_upper"]["upper"] for row in result["stages"]),
            "maximum_stage_curvature_upper": max(row["principal_curvature_upper"]["upper"] for row in result["stages"]),
            "complete_tail_disk_metric_gate_passed": result["complete_tail_disk_metric_gate_passed"],
            "complete_tail_disk_curvature_allocation_passed": result["complete_tail_disk_curvature_allocation_passed"],
            "complete_tail_disk_planar_projection_injective": result["complete_tail_disk_planar_projection_injective"],
            "deep_collar_status": result["deep_collar"]["status"],
            "deep_collar_metric_upper": result["deep_collar"]["metric_relative_operator_upper"]["upper"],
            "deep_collar_curvature_upper": (None if result["deep_collar"]["principal_curvature_upper"] is None
                                            else result["deep_collar"]["principal_curvature_upper"]["upper"]),
            "source_height_role": self.state["contract"]["height_identity"],
            "prefix_Cartesian_seam_proved": False, "closed_surface_proved": False,
        }
        passed = result["complete_tail_disk_metric_gate_passed"] and result["complete_tail_disk_curvature_allocation_passed"]
        self.state.pop("error", None)
        self.state.update(status="actual_whole_tail_geometry_passed" if passed else "actual_whole_tail_geometry_not_within_allocations",
                          active_phase=None)
        self.save()
        self.event("tail_geometry_terminal", status=self.state["status"], result=self.state["result"])
        return 0 if passed else 2

    def execute(self):
        try:
            self.prepare()
            self.background()
            self.stage0()
            if self.args.phase == "stage0":
                passed = (self.state["stage0_result"]["metric_gate_passed"] and
                          self.state["stage0_result"]["curvature_allocation_passed"])
                self.state.pop("error", None)
                self.state.update(status="actual_stage0_geometry_ready" if passed else "actual_stage0_geometry_not_within_allocations",
                                  active_phase=None, result=copy.deepcopy(self.state["stage0_result"]))
                self.save()
                self.event("tail_geometry_stage0_terminal", status=self.state["status"],
                           stage0=self.state["stage0_result"])
                return 0 if passed else 2
            self.remaining()
            self.merge_maps()
            self.certify_remaining()
            return self.complete()
        except Exception as exc:
            self.state["errors"].append({"phase": self.state.get("active_phase"), "error": str(exc)[-6000:]})
            self.state["status"] = "actual_tail_geometry_execution_failed"
            self.state["error"] = str(exc)[-6000:]
            self.save()
            self.event("tail_geometry_failed", error=str(exc)[-2000:], summary=str(self.state_path))
            return 2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("tail-response", "source-port", "source-topic", "height-reference", "outdir"):
        parser.add_argument("--" + name, type=Path, required=True)
    native = parser.add_mutually_exclusive_group(required=True)
    native.add_argument("--native-record", type=Path)
    native.add_argument("--native-record-dir", type=Path)
    parser.add_argument("--height-reference-key", default="raw_return.candidate_H")
    parser.add_argument("--warm-factor", type=float, required=True)
    parser.add_argument("--height-arithmetic", choices=("python", "numpy"), required=True)
    parser.add_argument("--phase", choices=("stage0", "all"), default="all")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--background-summary", type=Path)
    parser.add_argument("--degree", type=int, help="Explicit actual finite map band; default floor((N-4)/2)")
    parser.add_argument("--difference-step", type=float, default=.00005)
    parser.add_argument("--quadratic-mode-cutoff", type=int, default=12)
    parser.add_argument("--node", default="node")
    args = parser.parse_args()
    if ((args.degree is not None and args.degree < 1)
            or not math.isfinite(args.difference_step) or args.difference_step <= 0
            or args.quadratic_mode_cutoff < 0):
        raise ValueError("Require valid declared spectrum and actual derivative audit settings")
    sys.exit(Pipeline(args).execute())


if __name__ == "__main__":
    main()
