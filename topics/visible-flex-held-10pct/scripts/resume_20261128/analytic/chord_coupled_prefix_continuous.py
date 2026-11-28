#!/usr/bin/env python3
"""Explicit 7a lambda-one source entry for fresh Cartesian geometry/metric certificates.

The original interval algebra, angular tables, radial subdivisions and proof
loops are reused without modifying their files. Actual coupled acceptance is
checked by its own gate, never by replacing accepted_original or relabelling
an original-design record. Every output binds the current physical file and
the final physical-endpoint height. New fields need their own new complete
certificates; no R73/R74 result is transferred to a different field.

Run one phase per fresh process: geometry, tables, metric, cut, or the cheap
source-only preflight. All original phase options follow the phase name;
--coupling-summary is additionally required for every phase.
"""
import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import argparse
import hashlib
import inspect
import json
from pathlib import Path
import resource
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
GEO, TAIL = HERE.parent/"geometry", HERE.parent/"tail"
SCRIPTS = HERE.parents[1]
sys.path[:0] = [str(GEO), str(TAIL), str(SCRIPTS/"resume_20261126"), str(HERE)]
import cartesian_prefix_interval_geometry as geometry_base
import cartesian_prefix_metric_tables as tables_base
import cartesian_prefix_metric as metric_base
import cartesian_prefix_cut_metric as cut_base
from chord_actual_coupled_prefix import accepted_coupled, load_coupled_prefix
from seam_export_tail_geometry_v2 import checked, ref, sha
from verify_complete_tail_radius_identity import require_unscaled, complete_height_bytes

SOURCE_KIND = "actual_lambda_one_chord_final_physical_height"
SCHEMA = "actual-lambda-one-chord-Cartesian-continuous-entry-v1"
# These files already bind earlier actual fields. A changed implementation
# needs an explicit new review, not a silent change of the inherited algebra.
REVIEWED_BASE_SHA256 = {
    "cartesian_prefix_interval_geometry.py": "1e4554834e66dc72a8942bc9a844225704d478a07e248084aa4531ef891990dc",
    "cartesian_prefix_metric_tables.py": "ab8c9fb208cfa984c80768144545c9e558682eefa23169364eed9cb7986b82ba",
    "cartesian_prefix_metric.py": "935dc0ec201161396e11d25ace0de29e456e2c713618b1469cb78d1cea004ab3",
    "cartesian_prefix_cut_metric.py": "a5b8f4f821f6b284cb124d8f2c90d471271b91f16218c8ff6157f93d609892a7",
    "cartesian_prefix_metric_target.py": "a8bb9135d8ad56a0589db3c5d582a91cc85a8c4b1fd5a5632264cccf53d7ca77",
    "cartesian_prefix_curvature_rounding.py": "e094c1440e487fdd72137e7e20519b98c43addd4a6d5ead82e05fda88f3dbed5",
}


def check_reviewed_algebra():
    for name, digest in REVIEWED_BASE_SHA256.items():
        if sha(GEO/name) != digest:
            raise ValueError("The reviewed interval implementation changed: "+name)


def context_sources():
    paths = (Path(__file__).resolve(), HERE/"chord_actual_coupled_prefix.py",
             TAIL/"actual_cartesian_prefix.py", HERE/"verify_complete_tail_radius_identity.py")
    return {str(path):sha(path) for path in paths}


class CoupledContext:
    """Own the coupled source contract without editing any original record."""
    def __init__(self, summary, phase):
        self.summary = Path(summary).resolve()
        self.phase = phase
        self.payload = None
        self.execution = None
        self.adapter_sources = context_sources()

    def capture(self, run, record, binding, provenance):
        run = Path(run).resolve()
        physical = ref(run.parent/"physical.npz")
        if physical != binding["physical"]:
            raise ValueError("The current verified physical file differs from its endpoint binding")
        H = complete_height_bytes(binding["candidate_H"], int(record["modes"]))
        payload = dict(source_kind=SOURCE_KIND, actual_coupled_source_verified=True,
            coupling_summary=provenance["coupling_summary"],
            full_height_binding=provenance["endpoint_binding"],
            full_height_packet=binding["packet"],
            full_height_definition="final_physical_endpoint_binding.candidate_H",
            full_height_binary_sha256=hashlib.sha256(H).hexdigest(),
            raw_candidate_used_as_final_height=False,
            final_height_bitwise_equal_raw_candidate=provenance["raw_height_bitwise_equal"],
            source_run=str(run), source_run_sha256=sha(run),
            physical_file=physical, physical_sha256=physical["sha256"],
            source_mean_nodes=provenance["source_mean_nodes"],
            source_mean_gauss_order=provenance["source_mean_gauss_order"],
            actual_coupled_gate_provenance=provenance)
        if payload["coupling_summary"] != ref(self.summary):
            raise ValueError("The verified source used another actual coupling summary")
        if self.payload is not None and payload != self.payload:
            raise ValueError("One certificate process attempted to mix actual coupled fields")
        self.payload = payload
        return payload

    def accept(self, run):
        record, physical, binding, provenance = accepted_coupled(run, self.summary)
        self.capture(run, record, binding, provenance)
        return record, physical, binding

    def load_prefix(self, run):
        record, prefix, binding = load_coupled_prefix(run, self.summary)
        self.capture(run, record, binding, prefix.actual_coupling_provenance)
        return record, prefix

    def physical_sha(self):
        if self.payload is None:
            raise ValueError("No actual coupled physical file has been validated")
        current = ref(self.payload["physical_file"]["path"])
        if current != self.payload["physical_file"]:
            raise ValueError("The actual physical file changed during its certificate")
        return current["sha256"]

    def require_report(self, report):
        if self.payload is None:
            raise ValueError("Validate the current coupled source before using a bound report")
        if report.get("coupled_adapter_schema") != SCHEMA:
            raise ValueError("An original-design or other field report cannot supply coupled interval data")
        for key in ("source_kind", "actual_coupled_source_verified", "coupling_summary",
                    "full_height_binding", "full_height_packet", "full_height_definition",
                    "full_height_binary_sha256", "raw_candidate_used_as_final_height",
                    "source_run", "source_run_sha256", "physical_file", "physical_sha256",
                    "source_mean_nodes", "source_mean_gauss_order"):
            if report.get(key) != self.payload[key]:
                raise ValueError("The report belongs to another coupled source/definition: "+key)
        bound = report.get("coupled_adapter_sources")
        if not isinstance(bound, dict) or bound != self.adapter_sources:
            raise ValueError("The report does not bind this explicit coupled adapter and source gate")
        for path, digest in bound.items():
            if sha(path) != digest:
                raise ValueError("A coupled adapter source changed: "+path)

    def save(self, path, value):
        # This changes only the new entry's output metadata, never its source
        # run or the old proof loop's in-memory mathematical quantities.
        record = dict(value)
        if "source_sha256" in record:
            record["reused_main_source_sha256"] = record["source_sha256"]
        record["source_sha256"] = sha(__file__)
        record.update(coupled_adapter_schema=SCHEMA, coupled_phase=self.phase,
            requested_source_kind=SOURCE_KIND, source_run_relabelled_or_rewritten=False,
            accepted_original_replaced=False, old_other_field_bounds_reused=False,
            coupled_adapter_sources=dict(self.adapter_sources),
            coupled_execution_adapter=self.execution)
        if self.payload is not None:
            if ref(self.summary) != self.payload["coupling_summary"]:
                raise ValueError("The accepted coupling summary changed during verification")
            self.physical_sha()
            record.update(self.payload)
        else:
            record.update(actual_coupled_source_verified=False, source_kind=None)
        sources = dict(record.get("source_hashes", {}))
        sources.update(self.adapter_sources)
        record["source_hashes"] = sources
        geometry_base.save(path, record)


class CoupledNewMetric(metric_base.NewMetric):
    """New honest source initializer; the original interval methods are unchanged."""
    def __init__(self, report_path, context):
        self.context = context
        self.report_path = Path(report_path).resolve()
        self.record = json.loads(self.report_path.read_text())
        r = self.record
        if (r.get("status") != "complete_angular_three_jet_interval_tables"
                or r.get("right_sector_endpoint_gram_equals_left_exactly") is not True):
            raise ValueError("Require complete fresh angular tables for this coupled field")
        for path, digest in r["source_hashes"].items():
            if sha(path) != digest:
                raise ValueError("A bound angular construction source changed: "+path)
        for name in ("defining_jets", "angular_tables"):
            if sha(r[name]["path"]) != r[name]["sha256"]:
                raise ValueError("Bound exact-map interval data changed: "+name)
        run = Path(r["source_run"])
        if sha(run) != r["source_run_sha256"]:
            raise ValueError("The actual coupled input run changed")
        source, physical, binding = context.accept(run)
        context.require_report(r)
        self.coupled_source_record, self.coupled_height_binding = source, binding
        loader = geometry_base.module("_coupled_continuous_actual_model",
            SCRIPTS/"resume_m3/actual_m3_metric_model.py")
        obj = loader.load_model({"source_run":str(run.resolve())})
        p = physical.p.copy()
        obj.initial(p)
        # This is the genuinely coupled source flow and its full record.
        # No target g, delta or domain is borrowed from the earlier design.
        self.target = metric_base.FrozenTarget(obj.flow(p[0]), source)
        with np.load(r["defining_jets"]["path"], allow_pickle=False) as d:
            self.knots = d["knots"].copy()
            self.P = len(d["planar_modes"])
            self.field = metric_base.HermiteIntervals(self.knots, d["jets"])
            self.lift = metric_base.HermiteIntervals(self.knots, d["lift_jets"])
            self.chart = metric_base.HermiteIntervals(self.knots, d["chart_jets"])
            self.width = metric_base.fq(d["center_width"])
            self.pm, self.hm = d["planar_modes"].copy(), d["height_modes"].copy()
        if (metric_base.fq(self.knots[0]) != 0
                or metric_base.fq(self.knots[-1]) != self.target.end
                or np.any(self.pm % 3 != 1) or np.any(self.hm % 3 != 0)):
            raise ValueError("The actual coupled target and complete map domains differ")
        with np.load(r["angular_tables"]["path"], allow_pickle=False) as d:
            self.tables = {name:metric_base.pair(d[name].copy()) for name in d.files}
        self.N = int(r["angular_boxes_per_sector"])
        if self.tables["point_lift_0"].x[0].shape != (self.N, 3):
            raise ValueError("Missing complete actual angular table columns")
        self.grid = sorted(set(self.field.x+self.target.grid+[self.width]))


class CoupledCutMetric(cut_base.CutMetric, CoupledNewMetric):
    """The same full cut algebra with the actual final physical H binding."""
    def __init__(self, tables, bundle, outdir, context, width=.04):
        CoupledNewMetric.__init__(self, tables, context)
        self.cut_width = metric_base.fq(width)
        self.cut_start = self.target.end-self.cut_width
        if not 0 < self.cut_width or self.cut_start <= self.width:
            raise ValueError("The exact center and cut repairs must have disjoint strips")
        self.cap = cut_base.ActualFiniteTailV2(bundle,
            Path(outdir)/"verified-shared-node-index.json")
        source, binding = self.coupled_source_record, self.coupled_height_binding
        identity = self.cap.bundle["height_identity"]
        require_unscaled(identity)
        if self.cap.bundle["accepted_packet"] != binding["packet"]:
            raise ValueError("The cut requires the coupled source's actual final endpoint packet")
        H = complete_height_bytes(binding["candidate_H"], int(source["modes"]))
        referenced = checked(identity["reference"])
        for part in identity["reference_key"].split("."):
            referenced = referenced[part]
        packet = self.cap.packet
        for value in (referenced, packet["request"]["height"],
                      packet["response"]["checkpoint"]["cutHeight"]):
            if complete_height_bytes(value, int(source["modes"])) != H:
                raise ValueError("The cut substituted raw or scaled H for the final physical endpoint")
        if packet["config"]["modes"] != source["modes"]:
            raise ValueError("The complete coupled prefix and tail mode dimensions differ")
        port = checked(self.cap.bundle["source_port"])
        if (port["parameters"] != source["physical_tail_parameters"]
                or any(self.cap.parameters.get(k) != v for k, v in port["parameters"].items())):
            raise ValueError("The full tail and current coupled prefix physical metrics differ")
        with np.load(self.record["defining_jets"]["path"], allow_pickle=False) as d:
            if np.any(d["lift_jets"][:, :, -1] != 0):
                raise ValueError("A nonzero true-core endpoint requires a complete new cut contract")
            if np.any(d["chart_jets"][:, :, -1] != 0):
                raise ValueError("The complete material phase chart must have zero cut two-jet")
            jets = d["jets"][:, :, -1].copy()
        pm, hm, coeff, self.cut_definition = cut_base.complete_cut_coefficients(
            jets, self.pm, self.hm, self.cap.cut_jets, self.cap.pm, self.cap.hm,
            self.cap.parameters["rCut"], self.cap.parameters["wCut"])
        self.cut_tables = cut_base.cut_angular_tables(pm, hm, coeff, self.N,
            self.tables["psi_boxes"], self.tables["angular_width"])
        self.tables.update(self.cut_tables)
        self.cut_definition.update(cut_width_exact=str(self.cut_width),
            cut_start_exact=str(self.cut_start), prefix_end_exact=str(self.target.end),
            correction="sum_j (-L)^j H_j((end-s)/L) Delta_j(psi)",
            zero_extension="s <= end-L", all_original_tail_modes_retained=True,
            full_height_identity_checked=True, tail_near_cut_reparameterization_certified=False,
            source_kind=SOURCE_KIND, full_height_binding=context.payload["full_height_binding"],
            full_height_packet=context.payload["full_height_packet"],
            full_height_definition=context.payload["full_height_definition"],
            full_height_binary_sha256=context.payload["full_height_binary_sha256"],
            raw_candidate_used_as_final_height=False)
        self.grid = sorted(set(self.grid+[self.cut_start]))
        self.grid = [s for s in self.grid if s >= self.cut_start]
        output = Path(outdir)/"complete-cut-angular-tables.npz"
        np.savez(output, planar_modes=pm, height_modes=hm,
            cut_coefficient_enclosures=np.asarray(coeff.x),
            **{name:np.asarray(value.x) for name, value in self.cut_tables.items()})
        self.cut_data = dict(path=str(output.resolve()), sha256=sha(output))


def inherited_metric(context, verifier, path, target):
    context.require_report(json.loads(Path(path).read_text()))
    return cut_base.inherit_metric(verifier, path, target)


def inherited_geometry(context, verifier, path, rational_path):
    context.require_report(json.loads(Path(path).read_text()))
    return cut_base.inherit_geometry(verifier, path, rational_path)


def adapted_main(phase, context):
    """Copy one original proof loop with explicit source entry substitutions.

    No imported original gate or class is monkey-patched. A fresh namespace
    executes the adapted main; inherited interval methods remain the original
    bound functions. Both original/executed main hashes are recorded.
    """
    base = {"geometry":geometry_base, "tables":tables_base,
            "metric":metric_base, "cut":cut_base}[phase]
    original = inspect.getsource(base.main)
    changed = original
    replacements = {}
    if phase in ("geometry", "tables"):
        replacements["record, prefix = load_actual_prefix(args.source_run)"] = (
            "record, prefix = coupled_load_prefix(args.source_run)")
        replacements["record['physical_sha256']"] = "coupled_current_physical_sha()"
    elif phase == "metric":
        replacements["verifier=NewMetric(a.tables)"] = "verifier=coupled_new_metric(a.tables)"
    else:
        replacements["verifier=CutMetric(args.tables,args.geometry_bundle,out,args.cut_width)"] = (
            "verifier=coupled_cut_metric(args.tables,args.geometry_bundle,out,args.cut_width)")
        replacements["old_metric=inherit_metric(verifier,args.base_metric,target)"] = (
            "old_metric=coupled_inherit_metric(verifier,args.base_metric,target)")
        replacements["old_geometry=inherit_geometry(verifier,args.base_geometry,args.base_curvature)"] = (
            "old_geometry=coupled_inherit_geometry(verifier,args.base_geometry,args.base_curvature)")
    for before, after in replacements.items():
        if changed.count(before) != 1:
            raise ValueError("The declared original proof-loop entry changed: "+before)
        changed = changed.replace(before, after)
    context.execution = dict(adapter=ref(__file__), phase=phase,
        reused_proof_loop_source=ref(base.__file__),
        original_main_sha256=hashlib.sha256(original.encode()).hexdigest(),
        executed_main_sha256=hashlib.sha256(changed.encode()).hexdigest(),
        explicit_entry_replacements=replacements,
        interval_formula_methods_modified=False, accepted_original_replaced=False)
    namespace = dict(base.__dict__)
    namespace.update(save=context.save, coupled_load_prefix=context.load_prefix,
        coupled_current_physical_sha=context.physical_sha,
        coupled_new_metric=lambda path:CoupledNewMetric(path, context),
        coupled_cut_metric=lambda tables,bundle,out,width:
            CoupledCutMetric(tables,bundle,out,context,width),
        coupled_inherit_metric=lambda verifier,path,target:
            inherited_metric(context,verifier,path,target),
        coupled_inherit_geometry=lambda verifier,path,rational:
            inherited_geometry(context,verifier,path,rational))
    exec(compile(changed, str(Path(__file__).resolve())+"::"+phase, "exec"), namespace)
    return namespace["main"]


def preflight(context, arguments):
    parser = argparse.ArgumentParser(description="Check actual coupled acceptance without constructing geometry")
    parser.add_argument("--source-run", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    args = parser.parse_args(arguments)
    out = args.outdir.resolve()
    if SCRIPTS.parents[2] == out or SCRIPTS.parents[2] in out.parents:
        raise ValueError("Actual execution records must remain outside the source repository")
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    report = dict(status="checking_actual_coupled_source", metric_certified=False,
        geometry_certified=False, full_height_binding_verified=False,
        new_prefix_geometry_constructed=False, nonlinear_solves_executed=0,
        source_run=str(args.source_run.resolve()), source_run_sha256=sha(args.source_run),
        requested_coupling_summary=ref(context.summary), complete_surface=False)
    code = 0
    try:
        _, physical, _ = context.accept(args.source_run)
        del physical
        report.update(status="actual_coupled_source_gate_passed_without_geometry",
            full_height_binding_verified=True)
    except Exception as error:
        report.update(status="actual_coupled_source_gate_rejected", error=repr(error))
        code = 1
    finally:
        report.update(seconds=time.monotonic()-started,
            maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        context.save(out/"preflight.json", report)
    print(json.dumps({key:report[key] for key in ("status", "full_height_binding_verified", "seconds")}), flush=True)
    return code


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=("geometry", "tables", "metric", "cut", "preflight"))
    parser.add_argument("--coupling-summary", type=Path, required=True)
    options, rest = parser.parse_known_args()
    check_reviewed_algebra()
    context = CoupledContext(options.coupling_summary, options.phase)
    if options.phase == "preflight":
        raise SystemExit(preflight(context, rest))
    entry = adapted_main(options.phase, context)
    sys.argv = [str(Path(__file__).resolve())+"::"+options.phase, *rest]
    entry()


if __name__ == "__main__":
    main()
