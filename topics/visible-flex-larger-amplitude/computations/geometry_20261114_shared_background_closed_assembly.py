#!/usr/bin/env python3
"""Render one actual full v3/v4 closed field on its explicit shared background.

Only the geometric scalar background and the resulting complete angular cut
correction change.  Position and both radial derivatives come from the SAME
exact real Hermite B.  The original height/w/wr table remains the reference
metric input; it is never replaced by B'.  The original accepted full prefix,
R249 choice, native FFT nodes, one recorded SE2, cap height and markers remain
bound to the actual source bundle.  No fit, BVP, tail solve or primitive is run.

The exported prefix-definition guard deliberately makes the frozen legacy
loader reject these new meshes.  Subsequent cover/held consumers MUST use
load_shared_bundle, or an explicitly equivalent checked adapter.  The guard
is an identity annotation only: original prefix coefficients are unchanged.

All actual evaluation/rendering belongs to this public repository's Actions.
This entry cannot manufacture the genuinely accepted parent required by the
frozen full-bundle loader.  It also does not certify floating evaluation error,
operator/curvature/reach/held envelopes, or final topic completion.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
import math
import os
from pathlib import Path
from types import SimpleNamespace

for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import numpy as np

import geometry_20261114_large_core_closed_assembly as large
import geometry_20261114_shared_background_normal_form as background_form
from exact_20261114_refined_tail_adapter import synth
from geometry_20261114_large_core_saved_prefix import actions_only, read, sha


HERE = Path(__file__).resolve().parent
SCHEMA = "complete-shared-background-closed-geometry-v1"
GUARD_KEY = "closed_geometry_wrapper"
EXPECTED_SOURCES = {
    "geometry_20261114_shared_background_normal_form.py":
        "da4a0b5004ef8466119025d8e39e23ffb0366a5367e6761c8321299aeb19c3f9",
    "geometry_20261114_full_state_continuous_cover.py":
        "c39012655f36f652bacdbc39087c6934f03e6fde721830785fb0636930ceabe6",
    "geometry_20261114_large_core_closed_assembly.py":
        "e70d27a92bf153e49e50016706db854b339d96d3414d7f4c00a5993e1f7609c0",
    "geometry_20261114_lifted_modes_closed_assembly.py":
        "e5cf3eadb093fb741a8a610a09042a15f1869c79b2b4fc30f02c3de0635d2179",
    "exact_20261114_refined_closed_assembly.py":
        "1fec55a9d9f6c2a9211e64036226496bb4e4ae42c641c842e863e8c4f34fcccc",
    "exact_20261114_refined_tail_adapter.py":
        "6b06db6c7c96078b9fabe403a0b3ade14f8b30b07a78b565ed299c77f840d937",
    "geometry_20261114_inlet_parity_normal_form.py":
        "ce5f287c1de870b6bf71d1650d6942e23fd2bdd23a25af72ec5b637599a97410",
    "geometry_20261114_large_core_saved_prefix.py":
        "51eab8cdc878e22ad2c57bab129b1ef31463799596fcc40399fd8b0714ccbea0",
}
def check_sources():
    for name, digest in EXPECTED_SOURCES.items():
        if sha(HERE/name) != digest:
            raise ValueError("A frozen geometry/input source changed: "+name)


def canonical_sha(value):
    return background_form.canonical_sha(value)


def write_new(path, value):
    with Path(path).open("x") as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write("\n")


def source_arguments(args):
    value = copy.copy(args)
    value.directory = Path(args.source_directory)
    value.basename = getattr(args, "source_basename", "surface")
    return value


def checked_source_bundle(args):
    actions_only()
    check_sources()
    from geometry_20261114_full_state_continuous_cover import load_full_bundle
    bundle = load_full_bundle(source_arguments(args))
    if (GUARD_KEY in bundle[1]["large_core_prefix"] or
            "shared_background_geometry" in bundle[2]):
        raise ValueError("Use the actual original complete bundle, not recursive postprocessing")
    return bundle


def checked_background(bundle, descriptor_path):
    paths, plan, assembly, table, saved, original, binding = bundle
    record = background_form.read(descriptor_path)
    if record.get("source_sha256") != EXPECTED_SOURCES[
            "geometry_20261114_shared_background_normal_form.py"]:
        raise ValueError("The descriptor was not made by the frozen actual-background preparer")
    if record.get("complete_field_binding") != binding:
        raise ValueError("The descriptor belongs to another complete field or closed source bundle")
    B = background_form.SharedBackground.from_record(record)
    exact = background_form.exact
    rows = table["rows"]
    source_radii = tuple(exact(row["r"]) for row in rows)
    if (B.radii != source_radii or
            source_radii != tuple(map(exact, plan["background_radii"]))):
        raise ValueError("The descriptor dropped, changed or reordered source background nodes")
    height, w, wr = (np.array([row[key] for row in rows])
                     for key in ("heightFromRToCut", "w", "wr"))
    selected = (original.offset-original.sigma*height,
                original.sigma*w, original.sigma*wr)
    expected = tuple(tuple(exact(column[i]) for column in selected)
                     for i in range(len(rows)))
    if expected != B.nodal:
        raise ValueError("The exact nodal jets differ from the actual table output values")
    if (B.radii[0] != exact(original.cuff) or B.radii[-1] != exact(original.cut) or
            B.nodal[0] != (exact(original.cap_height), Q(0), Q(0)) or
            B.nodal[-1][0] != exact(original.offset)):
        raise ValueError("The original absolute cut/cuff/cap anchors changed")
    fft = np.asarray(original.outer_coeff)
    packed = np.asarray(fft, dtype="<c16", order="C")
    if not np.array_equal(packed.astype(np.clongdouble), fft):
        raise ValueError("Do not replace an actual higher-precision FFT by a binary64 shadow")
    fft_sha = hashlib.sha256(str(packed.shape).encode()+b"\0"+packed.tobytes()).hexdigest()
    if fft_sha != record["complete_cut"]["complete_outer_FFT_coefficients_sha256"]:
        raise ValueError("The descriptor's actual complete outer FFT node changed")
    if record["cuff"]["all_original_markers_unchanged"] is not True:
        raise ValueError("Retain the explicitly bound original caps and all markers")
    geometry = dict(schema=SCHEMA, wrapper_sha256=sha(__file__),
        descriptor_sha256=sha(descriptor_path),
        exact_background_payload_sha256=record["exact_background_payload_sha256"],
        descriptor_producer_sha256=record["source_sha256"],
        original_closed_bundle_sha256=copy.deepcopy(binding["closed_bundle_sha256"]),
        original_complete_prefix_definition_sha256=canonical_sha(saved.definition),
        original_target_metric_background_sha256=sha(paths["background"]),
        actual_outer_FFT_coefficients_sha256=fft_sha,
        original_cap_height=original.cap_height,
        fixed_cap_definition_sha256=canonical_sha(plan["fixed_cap"]),
        recorded_single_global_planar_registration_sha256=canonical_sha(saved.registration),
        original_inlet_normalization_sha256=canonical_sha(binding["inlet_normalization"]),
        frozen_geometry_sources=copy.deepcopy(EXPECTED_SOURCES),
        prefix_numerical_coefficients_and_original_definition_unchanged=True,
        original_target_metric_table_unchanged=True,
        target_metric_not_replaced_by_one_plus_Bprime_squared=True,
        complete_cut_difference_reformed_against_own_B=True,
        one_recorded_SE2_retained_without_new_fit=True,
        source_background_primitive_recomputed=False,
        actual_tail_or_BVP_resolved=False,
        geometry_background_definition="One exact shared-node real Hermite B, with B' and B'' its derivatives",
        new_native_background_formula="r*e_r(theta)+B(r)*e_z+diag(1,1,-1)*U(r,theta)",
        numerical_scalar_evaluation="Exact rational evaluation at each supplied binary query, then Python Fraction-to-binary64 rounding",
        complete_tail_FFT_Hermite_rounding_and_trigonometric_errors_certified=False,
        all_continuous_geometry_envelopes_inherited=False,
        geometric_acceptance_created=False, task_completed=False)
    return record, B, geometry


def guard_for(geometry):
    return dict(schema=SCHEMA, wrapper_sha256=geometry["wrapper_sha256"],
        descriptor_sha256=geometry["descriptor_sha256"],
        exact_background_payload_sha256=geometry["exact_background_payload_sha256"],
        original_complete_prefix_definition_sha256=geometry[
            "original_complete_prefix_definition_sha256"],
        prefix_numerical_coefficients_unchanged=True,
        identity_annotation_only=True,
        required_geometry_loader="geometry_20261114_shared_background_closed_assembly.load_shared_bundle",
        legacy_background_reconstruction_authorized=False)


def guarded_definition(original, geometry):
    result = copy.deepcopy(original)
    if GUARD_KEY in result:
        raise ValueError("Do not stack a second closed-geometry wrapper annotation")
    if canonical_sha(original) != geometry["original_complete_prefix_definition_sha256"]:
        raise ValueError("The original prefix definition changed before export")
    result[GUARD_KEY] = guard_for(geometry)
    return result


def binary64_queries(values, label):
    """The frozen tail API uses f64 queries; reject hidden extended narrowing."""
    supplied = np.asarray(values)
    if supplied.ndim != 1:
        raise ValueError(label+" must be one-dimensional")
    converted = np.asarray(supplied,dtype=float)
    if not np.all(np.isfinite(converted)):
        raise ValueError(label+" contains a nonfinite query")
    for old,new in zip(supplied,converted):
        old_exact = Q(int(old)) if isinstance(old,(int,np.integer)) else background_form.exact(old)
        if old_exact != background_form.exact(new):
            raise ValueError(label+" would silently narrow the original query precision")
    return converted


class SharedBackgroundAssembly(large.LargeCoreAssembly):
    """Geometry-only wrapper around an already registered, actual full bundle."""

    @classmethod
    def from_original(cls, original, B, geometry):
        actions_only()
        obj = cls.__new__(cls)
        obj.__dict__ = original.__dict__.copy()
        obj.original_assembly = original
        obj.shared_background = B
        obj.shared_background_geometry = copy.deepcopy(geometry)
        obj._scalar_cache = {}
        obj._scalar_rounding_max = [Q(0), Q(0), Q(0)]
        obj._original_reference_table = original.height
        obj._original_reference_table_sha = canonical_sha(original.height)
        obj._original_registration = copy.deepcopy(original.saved.registration)
        obj._original_definition = copy.deepcopy(original.saved.definition)
        obj.original_source_unpatched_cut = copy.deepcopy(original.unpatched_cut)
        # Do not reuse even a single old cut-difference cache entry: its native
        # slope/second background came from a different source expression.
        obj.delta_cache = {}
        obj.unpatched_cut = []
        for count in (obj.tail.N, 2*obj.tail.N):
            theta = 2*np.pi*np.arange(count)/count
            delta = obj.cut_difference(theta)
            obj.unpatched_cut.append(dict(angular=count,
                radial_angular_jet_norms={f"r{i}_theta{j}":large.maxnorm(delta[(i,j)])
                                         for i in range(3) for j in range(3)}))
        theta = 2*np.pi*np.arange(obj.tail.N)/obj.tail.N
        diagnostic = obj.cut_difference(theta)
        obj.cut_difference_coeff = np.stack([diagnostic[(i,0)] for i in range(3)])
        obj.assert_unchanged()
        return obj

    def assert_unchanged(self):
        if (self.height is not self._original_reference_table or
                canonical_sha(self.height) != self._original_reference_table_sha):
            raise AssertionError("The original metric table must not become B' or B''")
        if (self.saved.registration != self._original_registration or
                self.saved.definition != self._original_definition):
            raise AssertionError("The original complete prefix or recorded SE2 changed")
        if (self.cap_height != self.original_assembly.cap_height or
                self.offset != self.original_assembly.offset or
                self.plan["fixed_cap"] != self.original_assembly.plan["fixed_cap"]):
            raise AssertionError("The cap, marker or absolute cut/cuff gauge changed")

    def scalar_jets(self, radii):
        """One B and its genuine derivatives; retain the original query bits."""
        exact = background_form.exact
        values = np.asarray(radii)
        if values.ndim != 1:
            raise ValueError("Background queries must be one-dimensional radii")
        rows = []
        for radius in values:
            key = exact(radius)
            if key not in self._scalar_cache:
                true = tuple(self.shared_background.evaluate_exact(key, j) for j in range(3))
                rounded = tuple(float(value) for value in true)
                if not all(math.isfinite(value) for value in rounded):
                    raise ValueError("A represented background jet is not finite in the renderer")
                for j in range(3):
                    self._scalar_rounding_max[j] = max(self._scalar_rounding_max[j],
                                                       abs(exact(rounded[j])-true[j]))
                self._scalar_cache[key] = rounded
            rows.append(self._scalar_cache[key])
        return np.asarray(rows, dtype=float).reshape(len(values), 3)

    def native_cut_nine(self, theta):
        theta = binary64_queries(theta,"Native cut angles")
        scalar = self.scalar_jets(np.array([self.cut]))[0]
        co, si = np.cos(theta), np.sin(theta)
        circle = (np.column_stack([co,si]), np.column_stack([-si,co]),
                  np.column_stack([-co,-si]))
        out = {}
        for i in range(3):
            radius = (self.cut, 1., 0.)[i]
            for j in range(3):
                value = synth(self.outer_coeff[i], theta, j)*self.reflection
                value[:,:2] += radius*circle[j]
                if j == 0:
                    value[:,2] += scalar[i]
                out[(i,j)] = value
        return out

    def tail_jets(self, radii, theta):
        r = binary64_queries(radii,"Tail radii")
        theta = binary64_queries(theta,"Tail angles")
        scalar = self.scalar_jets(r)
        # The complete angular outer correction is inherited, but its virtual
        # native_cut_nine now reads B and the old delta cache was discarded.
        out = self.perturbation(r, theta)
        for value in out.values():
            value[:,:,2] *= self.sigma
        co, si = np.cos(theta)[None,:], np.sin(theta)[None,:]
        zero = np.zeros((len(r),len(theta)))
        out["pos"] += np.stack(np.broadcast_arrays(r[:,None]*co,r[:,None]*si,
                                                     scalar[:,0,None]),axis=-1)
        out["s1"] += np.stack(np.broadcast_arrays(co,si,scalar[:,1,None]),axis=-1)
        out["s2"][:,:,2] += scalar[:,2,None]
        out["p1"] += np.stack(np.broadcast_arrays(-r[:,None]*si,r[:,None]*co,zero),axis=-1)
        out["p2"] += np.stack(np.broadcast_arrays(-r[:,None]*co,-r[:,None]*si,zero),axis=-1)
        out["sp"] += np.stack(np.broadcast_arrays(-si,co,zero),axis=-1)
        return out

    def evaluation_diagnostics(self):
        self.assert_unchanged()
        return dict(queried_distinct_background_radii=len(self._scalar_cache),
            exact_scalar_to_binary64_max_errors=[background_form.qrecord(x)
                                                 for x in self._scalar_rounding_max],
            exact_errors_only_at_actual_queries=True,
            errors_exclude_other_renderer_arithmetic=True,
            continuous_evaluation_error_envelope_certified=False,
            old_cut_difference_cache_reused=False,
            original_source_unpatched_cut=self.original_source_unpatched_cut,
            own_background_unpatched_cut=self.unpatched_cut)


def new_plan(source, geometry, descriptor_path):
    result = copy.deepcopy(source)
    result["schema"] = "shared-background-complete-material-finite-closed-plan-v1"
    result["original_plan_schema"] = source["schema"]
    result["shared_background_geometry"] = copy.deepcopy(geometry)
    result["original_complete_prefix_definition"] = copy.deepcopy(source["large_core_prefix"])
    result["large_core_prefix"] = guarded_definition(source["large_core_prefix"],geometry)
    result["inputs"]["shared_background"] = dict(file=str(Path(descriptor_path).resolve()),
                                                  sha256=sha(descriptor_path))
    return result


def new_heights(source, geometry, plan_path):
    """Rebind identical reference rows; do not replace them by geometric B jets."""
    result = copy.deepcopy(source)
    result["inputs"]["plan"] = dict(file=str(Path(plan_path).resolve()),sha256=sha(plan_path))
    result["shared_background_geometry"] = copy.deepcopy(geometry)
    result["source_table_reused_without_primitive_recomputation"] = True
    result["rows_role"] = "Unchanged original reference metric table; geometric position/0/1/2 jets use the separately bound B"
    return result


def annotate_output(data, source_assembly, geometry, A):
    """Called after the frozen writer has installed all its original metadata."""
    data["shared_background_geometry"] = copy.deepcopy(geometry)
    data["original_complete_prefix_definition"] = copy.deepcopy(A.saved.definition)
    data["large_core_prefix"] = guarded_definition(A.saved.definition,geometry)
    # Retain the actual reader identity, including v4 and the R249 definition,
    # rather than inventing a v3 reader identity for an unchanged v4 source.
    for key in ("large_core_binding", "inlet_normalization", "inlet_normal_form_wrapper_sha256",
                "actual_saved_prefix_constructor_sha256", "independent_modes_saved_prefix_sha256",
                "independent_modes_scalar_profile_sha256", "field_representation",
                "independent_field_modes"):
        if key in source_assembly:
            data[key] = copy.deepcopy(source_assembly[key])
    data["postprocessed_finite_field"] = True
    data["original_BVP_reaccepted_after_postprocessing"] = False
    if "shared_cut" in data:
        data["schema"] = "shared-background-complete-material-finite-closed-assembly-v1"
        data["shared_cut"]["native_background"] = "The same exact shared B and its first two derivatives"
        data["shared_cut"]["full_angular_correction_reformed"] = True
        data["shared_cut"]["literal_floating_C2_identity_certified"] = False
        data["inner_collar"]["definition"] = (
            "Original full native FFT endpoint collar on the new explicit shared B; "
            "original reference metric retained, no exact nonlinear extension claimed")
        data["shared_background_evaluation"] = A.evaluation_diagnostics()
        if data["mean_gauge"] != source_assembly["mean_gauge"]:
            raise AssertionError("The complete original mean/cap gauge changed during rendering")
        if data["single_global_planar_registration"] != source_assembly["single_global_planar_registration"]:
            raise AssertionError("A new planar fit was introduced during rendering")
        if data["fixed_markers"]["centers"] != source_assembly["fixed_markers"]["centers"]:
            raise AssertionError("The original fixed marker centers changed")
        data["limitations"] = [row for row in data["limitations"]
            if not row.startswith("The explicit full-angular outer correction gives a finite C2 map")]
        data["limitations"].extend([
            "Only the scalar background is newly defined as one exact real shared-node C2 Hermite function; its floating evaluations and the other finite-field normal-form representations retain their stated error obligations.",
            "The complete angular cut difference was recomputed using that same B, without changing the one recorded SE2, source prefix, FFT nodes, cap height or markers.",
            "All metric samples still use the original height-table w and E=1+w^2; B' is not substituted into the target metric.",
            "Continuous operator, curvature, reach and held-image bounds must be paid for this new bound geometry; old finite samples or conditional envelopes are not inherited.",
            "Cover and held consumers must use load_shared_bundle. The prefix-definition wrapper annotation intentionally makes the legacy loader reject this new geometry."])


def render(args):
    bundle = checked_source_bundle(args)
    paths, source_plan, source_assembly, source_table, saved, original, source_binding = bundle
    _, B, geometry = checked_background(bundle,args.descriptor)
    A = SharedBackgroundAssembly.from_original(original,B,geometry)
    prefix = Path(args.out_prefix)
    if not prefix.name or prefix.name in (".",".."):
        raise ValueError("Use a new ordinary output basename")
    outputs = [Path(str(prefix)+suffix) for suffix in (
        "-plan.json","-heights.json","-assembly.json","-normal-samples.npz",
        "-all-phase-finite-pairs.json")]
    outputs.extend(Path(str(prefix)+f"-phase{i}.ply.gz") for i in source_plan["mesh_phase_indices"])
    if any(path.exists() for path in outputs):
        raise FileExistsError("Preserve all prior results; use a fresh output prefix")
    prefix.parent.mkdir(parents=True,exist_ok=True)
    plan_path, heights_path = outputs[:2]
    plan = new_plan(source_plan,geometry,args.descriptor)
    write_new(plan_path,plan)
    heights = new_heights(source_table,geometry,plan_path)
    write_new(heights_path,heights)
    A.plan = plan
    A.assert_unchanged()
    display = source_assembly.get("display_sampling",{})
    render_args = SimpleNamespace(**vars(args))
    render_args.action = "render"
    render_args.plan,render_args.heights = plan_path,heights_path
    render_args.angular,render_args.phase_samples = plan["angular"],plan["phase_samples"]
    render_args.marker_k = plan["fixed_cap"]["marker_k"]
    render_args.cut_correction_width = plan["cut_correction_width"]
    for key, default in (("prefix_intervals",48),("tail_intervals",64),
                         ("collar_intervals",16),("cap_intervals",24)):
        setattr(render_args,key,display.get(key,default))
    import geometry_20261114_lifted_modes_closed_assembly as lifted
    old_bundle,old_last = large._bundle,large._last_assembly
    large._bundle = (saved,original.tail,read(args.config),copy.deepcopy(source_assembly["large_core_binding"]))
    large._last_assembly = A
    try:
        consumer = lifted.install_consumer(render_args)
        render_args.source_hash = sha(__file__)
        consumer.load = lambda parsed: large._bundle[:3]
        def use_own_assembly(s,t,p,h,mean):
            if s is not saved or t is not original.tail or p != plan or h != heights:
                raise ValueError("The frozen renderer requested another full field or plan")
            A.assert_unchanged()
            return A
        consumer.RefinedAssembly = use_own_assembly
        previous_write = consumer.write
        def write(path,data):
            previous_write(path,data)
            if isinstance(data,dict):
                annotate_output(data,source_assembly,geometry,A)
                # As in the existing R249 wrapper, amend only the file just
                # created exclusively by the original writer, never old data.
                Path(path).write_text(json.dumps(data,indent=2,allow_nan=False)+"\n")
        consumer.write = write
        consumer.render(render_args)
    finally:
        large._bundle,large._last_assembly = old_bundle,old_last
    A.assert_unchanged()
    print(json.dumps(dict(event="actual-shared-background-closed-render",
        plan=str(plan_path),assembly=str(prefix)+"-assembly.json",
        descriptor_sha256=geometry["descriptor_sha256"],
        original_target_metric_preserved=True,new_geometric_acceptance=False)),flush=True)


def load_shared_bundle(args):
    """The full-cover tuple API for these new meshes, never the old loader.

    args.directory/basename identify the NEW render.  args.source_directory/
    source_basename identify its actual ORIGINAL complete bundle; descriptor,
    checkpoint, port, config, tail_response, complete and source_topic are the
    same original inputs.  Paths may move; every scientific payload is hashed.
    """
    bundle = checked_source_bundle(args)
    old_paths,old_plan,old_assembly,old_table,saved,original,old_binding = bundle
    _,B,geometry = checked_background(bundle,args.descriptor)
    if not args.basename or Path(args.basename).name != args.basename:
        raise ValueError("--basename must be one file-name component")
    paths = {key:Path(args.directory)/(args.basename+suffix) for key,suffix in (
        ("plan","-plan.json"),("assembly","-assembly.json"),
        ("mesh","-phase0.ply.gz"),("background","-heights.json"),
        ("normals","-normal-samples.npz"))}
    plan,assembly,table = map(read,(paths["plan"],paths["assembly"],paths["background"]))
    for name,item in (("plan",plan),("assembly",assembly),("background",table)):
        if item.get("finished") is not True or item.get("shared_background_geometry") != geometry:
            raise ValueError("The new "+name+" has another descriptor/wrapper/source identity")
    expected_definition = guarded_definition(saved.definition,geometry)
    for item in (plan,assembly):
        if (item.get("large_core_prefix") != expected_definition or
                item.get("original_complete_prefix_definition") != saved.definition):
            raise ValueError("The original prefix or required geometry wrapper guard changed")
    restored_plan = copy.deepcopy(plan)
    restored_plan["schema"] = restored_plan.pop("original_plan_schema")
    restored_plan["large_core_prefix"] = restored_plan.pop("original_complete_prefix_definition")
    restored_plan.pop("shared_background_geometry")
    descriptor_input = restored_plan["inputs"].pop("shared_background")
    if descriptor_input["sha256"] != sha(args.descriptor) or restored_plan != old_plan:
        raise ValueError("The new plan changed an original ring, phase, marker, node or field input")
    restored_table = copy.deepcopy(table)
    if restored_table.pop("source_table_reused_without_primitive_recomputation") is not True:
        raise ValueError("The reference table provenance changed")
    restored_table.pop("rows_role")
    restored_table.pop("shared_background_geometry")
    if restored_table["inputs"]["plan"]["sha256"] != sha(paths["plan"]):
        raise ValueError("The reference rows were not rebound to this exact new plan")
    restored_table["inputs"]["plan"] = copy.deepcopy(old_table["inputs"]["plan"])
    if restored_table != old_table:
        raise ValueError("The original reference metric table or its provenance changed")
    for key,path in (("plan",paths["plan"]),("heights",paths["background"])):
        if assembly["inputs"][key]["sha256"] != sha(path):
            raise ValueError("The new assembly references another "+key)
    phase0 = [row for row in assembly["files"] if row.get("t") == 0]
    if len(phase0) != 1 or phase0[0]["sha256"] != sha(paths["mesh"]):
        raise ValueError("The new phase-zero mesh hash differs")
    if assembly["normal_samples"]["sha256"] != sha(paths["normals"]):
        raise ValueError("The new normal packet hash differs")
    for key in ("large_core_binding","single_global_planar_registration", "mean_gauge",
                "core_and_hold_gauge"):
        if assembly[key] != old_assembly[key]:
            raise ValueError("The new geometry changed original prefix/tail/gauge identity at "+key)
    A = SharedBackgroundAssembly.from_original(original,B,geometry)
    A.plan = plan
    A.assert_unchanged()
    bindings = copy.deepcopy(old_binding)
    bindings.update(closed_bundle_sha256={key:sha(path) for key,path in paths.items()},
        original_closed_bundle_sha256=copy.deepcopy(old_binding["closed_bundle_sha256"]),
        original_complete_prefix_definition=copy.deepcopy(saved.definition),
        complete_prefix_definition=expected_definition,
        shared_background_geometry=geometry,
        actual_native_tail_and_full_cut_correction_retained=False,
        actual_native_tail_retained_and_complete_cut_correction_reformed=True,
        original_target_metric_table_unchanged=True,
        same_shared_background_loader_required_for_cover_and_held=True,
        all_source_envelopes_inherited=False,continuous_envelopes_certified=False,
        geometric_acceptance_created=False)
    return paths,plan,assembly,table,saved,A,bindings


def main():
    actions_only()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action",choices=("render",))
    for name in ("source-directory","descriptor","checkpoint","port","config",
                 "tail-response","complete","source-topic","out-prefix"):
        parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--source-basename",default="surface")
    parser.add_argument("--mean-batch",type=int,default=8)
    parser.add_argument("--reach-ring-stride",type=int,default=2)
    parser.add_argument("--reach-angle-stride",type=int,default=4)
    args = parser.parse_args()
    if min(args.mean_batch,args.reach_ring_stride,args.reach_angle_stride)<1:
        parser.error("Batches and sampling strides must be positive")
    render(args)


if __name__ == "__main__":
    main()
