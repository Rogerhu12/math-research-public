#!/usr/bin/env python3
"""Complete actual active x fixed-cap R281 responsibility component.

No truncated worst-pair list is consumed. Every closed active cell is paired
with every closed cap cell. A stopped run records an exact rank suffix, not
a fictitious complete cover. This is a supplementary component of the same
field: the frozen static-base/R24 route, its local-path/curvature/metric gates,
and its original reach target are preserved as independent responsibilities.

R281 is applied to the actual active image rotation against genuinely fixed
marked caps. It is never obtained by rotating one end of an old static-base
point pair. Cuff diagonal/local cells cannot be silently paid by strict phase
gates. No native acceptance or complete reach/held/isometry conclusion is made.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import time

HERE = Path(__file__).resolve().parent
REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "same-shared-field-complete-mixed-phase-responsibility-component-v1"
ACTIVE_SCHEMA = "same-shared-field-complete-active-interval-balls-v1"
ACTIVE_SOURCE = "geometry_20261115_shared_active_interval_balls.py"
ACTIVE_SHA = "675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b"
CAP_SCHEMA = "same-shared-field-two-fixed-cap-rational-balls-v1"
CAP_SOURCE = "geometry_20261115_fixed_cap_rational_balls.py"
CAP_SHA = "a3ada50b5389a075f1da2d2237269a1a1ccc83c29aa35bc889d721eac0e2552e"
OLD_SCHEMA = "R37-R241-complete-shared-background-spatial-cover-budget-v1"
SOURCE_PINS = {
    "geometry_20261115_rational_phase_cover.py": "f6214d1dc66f9890e99f5d9bbbc93fa0e6524acd6ac879f0058ea023ebc17537",
    "geometry_20261115_joint_phase_normal_balls.py": "c5548f28bfe56a283403a7d16e1879c1c1243d0a0bc80761586fe50e1aec1466",
    "root_mixed_phase_normal_balls.py": "ecea0ef58aa5755270807596da5512552ac52fab27e90492fcf85fab095716c6",
    "geometry_20261114_shared_background_continuous_cover.py": "fc5bbb6762cf589a8ab6096c066bdd1bbad17c516954a43c4a40496445e9a5fb",
    "geometry_20261114_full_state_continuous_cover.py": "c39012655f36f652bacdbc39087c6934f03e6fde721830785fb0636930ceabe6",
    "geometry_20261114_continuous_cover_budget_v3.py": "3362fc35c09b98a8feb10706f2b126c9bc45e7d45a4294c928b4b72e59d2c7a1",
}


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Run the exact certificate arithmetic only in the named public Actions repository")


def sha_bytes(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode()


def unique_object(pairs):
    value = {}
    for key,item in pairs:
        if key in value:
            raise ValueError("Duplicate JSON key: "+key)
        value[key] = item
    return value


def decode(raw):
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    return json.loads(raw,object_pairs_hook=unique_object,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def read_bound(path, expected):
    raw = Path(path).read_bytes()
    if sha_bytes(raw) != expected:
        raise ValueError("An actual input changed: "+str(path))
    return decode(raw),dict(file=Path(path).name,bytes=len(raw),sha256=expected)


def child(parent, descriptor):
    path = verify_child(parent,descriptor)
    return path,path.read_bytes()


def verify_child(parent, descriptor):
    name = descriptor["file"]
    if Path(name).name != name or name in (".",".."):
        raise ValueError("Component descriptors use one local file name")
    path = Path(parent)/name
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        for raw in iter(lambda:stream.read(1048576),b""):
            size += len(raw)
            digest.update(raw)
    if size != descriptor["bytes"] or digest.hexdigest() != descriptor["sha256"]:
        raise ValueError("A complete component payload changed: "+name)
    return path


def finite_rational(value):
    if isinstance(value,bool):
        raise ValueError("A Boolean is not a radius or target")
    if isinstance(value,float):
        return F(*value.as_integer_ratio())
    return F(value)


def receipt(path):
    digest = hashlib.sha256()
    size = 0
    with Path(path).open("rb") as stream:
        for raw in iter(lambda:stream.read(1048576),b""):
            size += len(raw)
            digest.update(raw)
    return dict(file=Path(path).name,bytes=size,sha256=digest.hexdigest())


def load_phase(code_directory):
    directory = Path(code_directory)
    for name,expected in {**SOURCE_PINS,ACTIVE_SOURCE:ACTIVE_SHA,CAP_SOURCE:CAP_SHA}.items():
        if sha_bytes((directory/name).read_bytes()) != expected:
            raise ValueError("A frozen defining or phase kernel source changed: "+name)
    path = directory/"geometry_20261115_rational_phase_cover.py"
    spec = importlib.util.spec_from_file_location("_complete_mixed_R281",path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    previous,kernel = module.load_sources()
    return module,previous,kernel


def bind_inputs(args):
    active,active_receipt = read_bound(args.active_result,args.active_result_sha256)
    fixed,fixed_receipt = read_bound(args.fixed_caps,args.fixed_caps_sha256)
    old,old_receipt = read_bound(args.original_cover,args.original_cover_sha256)
    if active.get("schema") != ACTIVE_SCHEMA or active.get("source_sha256") != ACTIVE_SHA:
        raise ValueError("Use the actual complete-expression active ball producer")
    if (fixed.get("schema") != CAP_SCHEMA or fixed.get("source_sha256") != CAP_SHA
            or fixed.get("completed") is not True
            or fixed.get("complete_two_fixed_cap_position_and_unit_normal_balls") is not True):
        raise ValueError("Use the complete same-source two-cap component")
    if (old.get("schema") != OLD_SCHEMA or old.get("finished") is not True
            or old.get("source_sha256") != SOURCE_PINS["geometry_20261114_shared_background_continuous_cover.py"]):
        raise ValueError("Retain the actual original shared-field cover record")
    _,binding_raw = child(args.active_result.parent,active["input_binding"])
    _,expression_raw = child(args.active_result.parent,active["expression"])
    cells_path = verify_child(args.active_result.parent,active["active_cells"])
    binding,expression = decode(binding_raw),decode(expression_raw)
    if (binding["source_sha256"] != ACTIVE_SHA
            or binding["expression_schema"] != expression["schema"]
            or expression["derivatives_are_of_this_exact_expression"] is not True):
        raise ValueError("The active expression/ball identities differ")
    cap_binding = fixed["input_binding"]
    same_geometry = binding["shared_background_geometry"]
    if (cap_binding["shared_background_geometry"] != same_geometry
            or old["complete_field_binding"]["shared_background_geometry"] != same_geometry):
        raise ValueError("Do not mix another geometry, registration, cap gauge or background")
    for key,descriptor in (("plan",binding["shared_plan"]),("assembly",binding["shared_assembly"])):
        if (cap_binding[key]["sha256"] != descriptor["sha256"]
                or cap_binding[key]["bytes"] != descriptor["bytes"]):
            raise ValueError("The complete two-cap and active inputs have different original "+key)
    old_binding = old["complete_field_binding"]
    current_binding = binding["complete_field_binding"]
    for key in ("complete_checkpoint_sha256","config_sha256","actual_tail_response_sha256",
                "complete_readout_sha256","original_port_sha256","closed_bundle_sha256",
                "complete_prefix_definition","inlet_normalization",
                "recorded_single_global_planar_registration","complete_mean_gauge",
                "shared_background_geometry"):
        if old_binding[key] != current_binding[key]:
            raise ValueError("The original cover belongs to another actual field at "+key)
    if binding["common_rotation_axis_xy"] != ["0","0"] or cap_binding["common_rotation_axis_xy"] != ["0","0"]:
        raise ValueError("The moving and fixed components have different native axes")
    if (binding.get("no_rigid_rotation_of_one_end_of_an_old_static_base_pair") is not True
            or binding["global_family_definition"] != "R248: R_alpha F_active(s,theta-alpha), with both marked graph caps pointwise fixed"):
        raise ValueError("The actual mixed-family responsibility differs")
    tau = finite_rational(old["marker_budget"]["target_reach"])
    if tau <= 0:
        raise ValueError("The original marked reach target must be positive")
    cap_cells = fixed["cap_cells"]
    if len(cap_cells) != fixed["fixed_cap_cells"] or not cap_cells:
        raise ValueError("The complete cap list is inconsistent")
    identifiers = set()
    for row in cap_cells:
        if row["cell_id"] in identifiers or row["phase_motion"] != "fixed":
            raise ValueError("A cap cell was duplicated or incorrectly rotated")
        identifiers.add(row["cell_id"])
        check_ball(row,"fixed")
    # Complete gzip bytes are hashed above. Iteration itself remains streamed;
    # no list of all active-pair products or a retained worst subset is built.
    index = dict(active_result=active_receipt,fixed_caps=fixed_receipt,original_cover=old_receipt,
        original_target_reach_binary64=old["marker_budget"]["target_reach"],
        original_target_reach_exact=str(tau),
        original_required_unmarked_reach=old["marker_budget"]["required_unmarked_reach"],
        complete_field_binding=current_binding,shared_background_geometry=same_geometry,
        active_expression_sha256=active["expression"]["sha256"],
        active_cell_stream_sha256=active["active_cells"]["sha256"],
        active_R279_K=active["parameters"]["curvature_upper"],
        active_R279_K_matches_original_cover=(active["parameters"]["curvature_upper"] is not None
            and F(active["parameters"]["curvature_upper"]) == finite_rational(old["supplied_envelopes"]["curvature"])),
        active_R279_result_substituted_for_whole_surface_curvature_gate=False,
        original_static_cover_summary={key:old[key] for key in
            ("supplied_envelopes","supplied_envelopes_contain_saved_samples","marker_budget",
             "numerical_cover_budget_passed","entire_phase_circle_reduced_to_static_base",
             "continuous_reach_interval_certificate")},
        old_all_pair_or_worst_lists_not_used_as_this_mixed_pair_universe=True,
        old_static_base_R24_proof_route_and_all_old_gates_unchanged=True,
        old_numerical_pass_not_promoted_to_interval_certificate=True)
    return active,fixed,expression,cap_cells,cells_path,tau,index


def check_ball(row, prefix):
    for suffix in ("position","normal_centre"):
        values = row[prefix+"_"+suffix]
        if len(values) != 3:
            raise ValueError("A complete 3-dimensional ball center is required")
        tuple(map(F,values))
    for suffix in ("position_radius","normal_radius"):
        if F(row[prefix+"_"+suffix]) < 0:
            raise ValueError("Negative continuous-ball radius")


def active_rows(path, active, expression):
    depth = active["parameters"]["depth"]
    division = 2**depth
    pieces = expression["radial_pieces"]
    per_sheet = len(pieces)*division*division
    expected_count = 2*per_sheet
    if expected_count != active["planned_closed_cells"]:
        raise ValueError("The claimed full closed parameter partition changed")
    count = 0
    with gzip.open(path,"rt",encoding="utf-8") as stream:
        for line in stream:
            row = json.loads(line,object_pairs_hook=unique_object)
            sheet_index,local = divmod(count,per_sheet)
            piece_index,local = divmod(local,division*division)
            ri,qi = divmod(local,division)
            sheet = "upper" if sheet_index == 0 else "lower"
            if sheet_index > 1:
                raise ValueError("Extra active cells beyond the declared complete surface pieces")
            piece = pieces[piece_index]
            a,b = F(piece["left"]),F(piece["right"])
            radial = [str(a+(b-a)*F(ri,division)),str(a+(b-a)*F(ri+1,division))]
            angular = [str(F(qi,division)),str(F(qi+1,division))]
            if (row.get("schema") != "same-shared-field-closed-active-cell-six-jets-v1"
                    or row["ordinal"] != count or row["cell_id"] != f"{sheet}/{piece_index}/{ri}/{qi}"
                    or row["sheet"] != sheet or row["piece_index"] != piece_index
                    or row["piece_kind"] != piece["kind"]
                    or row["closed_radial_interval"] != radial
                    or row["closed_normalized_physical_angle_interval"] != angular
                    or row["phase_motion"] != "active_R248_image_rotation"):
                raise ValueError("An actual full active-cell identity/range was lost or changed")
            if row["normal_ball_certified"] is True:
                check_ball(row,"moving")
                if F(row["squared_cross_lower"]) <= 0:
                    raise ValueError("A normalized normal needs the recorded positive cross lower bound")
            count += 1
            yield row
    if count != active["exported_closed_cells"]:
        raise ValueError("An active-cell record is missing")


def known_cuff_local_responsibility(active, fixed, cuff):
    if (active["piece_kind"] != "collar" or F(active["closed_radial_interval"][0]) != cuff
            or active["sheet"] != fixed["cap"]):
        return False
    box = tuple(tuple(map(F,entry)) for entry in fixed["parameter_box_xy"])
    minimum = sum((F(0) if lo <= 0 <= hi else min(lo*lo,hi*hi) for lo,hi in box),F(0))
    maximum = sum((max(lo*lo,hi*hi) for lo,hi in box),F(0))
    # A closed box is connected; if its squared-radius range straddles cuff²,
    # it contains a boundary point. Over all phases the active cuff arc meets
    # that identical material point. A strict separated/non-normal pair gate
    # cannot pay the whole product, and no local-chart proof is fabricated.
    return minimum <= cuff*cuff <= maximum


def evaluate_mixed_pair(active, fixed, tau, phase, previous, kernel, args):
    row = dict(name=active["cell_id"]+" :: "+fixed["cell_id"],tau=str(tau))
    for prefix,source in (("moving",active),("fixed",fixed)):
        for suffix in ("position","position_radius","normal_centre","normal_radius"):
            row[prefix+"_"+suffix] = source[prefix+"_"+suffix]
    return phase.evaluate_case(row,args.sqrt_bits,args.phase_max_depth,args.phase_max_cells,previous,kernel)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("active-result","fixed-caps","original-cover"):
        parser.add_argument("--"+name,type=Path,required=True)
        parser.add_argument("--"+name+"-sha256",required=True)
    parser.add_argument("--code-directory",type=Path,default=HERE)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--max-pairs",type=int,default=1000000)
    parser.add_argument("--budget-seconds",type=int,default=3600)
    parser.add_argument("--sqrt-bits",type=int,default=128)
    parser.add_argument("--phase-max-depth",type=int,default=16)
    parser.add_argument("--phase-max-cells",type=int,default=131070)
    args = parser.parse_args()
    require_actions()
    if args.out.exists():
        raise FileExistsError("Preserve all original and earlier output packets")
    if not (args.max_pairs > 0 and args.budget_seconds > 0 and 16 <= args.sqrt_bits <= 4096
            and 0 <= args.phase_max_depth <= 40 and args.phase_max_cells >= 2):
        raise ValueError("Invalid explicit resource parameters")
    phase,previous,kernel = load_phase(args.code_directory)
    active,fixed,expression,cap_cells,cells_path,tau,binding = bind_inputs(args)
    args.out.mkdir(parents=True)
    (args.out/"input-binding.json").write_bytes(canonical(binding))
    planned = active["planned_closed_cells"]*len(cap_cells)
    cuff = F(fixed["input_binding"]["cuff"]["exact"])
    started = time.monotonic()
    count = passed = local = unavailable = unresolved_phase = 0
    stop_reason = None
    stream_path = args.out/"complete-mixed-pairs.jsonl.gz"
    with stream_path.open("xb") as raw_stream:
        with gzip.GzipFile(filename="",mode="wb",fileobj=raw_stream,mtime=0) as stream:
            for a in active_rows(cells_path,active,expression):
                for cap_index,c in enumerate(cap_cells):
                    if count >= args.max_pairs or time.monotonic()-started >= args.budget_seconds:
                        stop_reason = "resource_budget_before_next_pair"
                        break
                    rank = a["ordinal"]*len(cap_cells)+cap_index
                    if rank != count:
                        raise AssertionError("The full Cartesian product has a gap")
                    row = dict(rank=rank,active_ordinal=a["ordinal"],cap_index=cap_index,
                        active_cell_id=a["cell_id"],fixed_cell_id=c["cell_id"],
                        complete_phase_component_paid=False)
                    if not a["normal_ball_certified"]:
                        unavailable += 1
                        row.update(reason="active_normal_ball_unresolved",local_responsibility_paid=False)
                    elif known_cuff_local_responsibility(a,c,cuff):
                        local += 1
                        row.update(reason="common_cuff_closed_cells_require_original_local_chart_responsibility",
                            actual_strict_phase_test_skipped_because_zero_chord_in_product=True,
                            original_local_path_gate_reused_or_paid=False,
                            local_responsibility_paid=False)
                    else:
                        value = evaluate_mixed_pair(a,c,tau,phase,previous,kernel,args)
                        ok = value["all_phase_distance_or_no_double_normal_pass"]
                        passed += int(ok)
                        unresolved_phase += int(not ok)
                        row.update(reason="R281_full_phase_component_pass" if ok else "R281_phase_component_unresolved",
                            complete_phase_component_paid=ok,R281=value)
                    stream.write(canonical(row))
                    count += 1
                if stop_reason:
                    break
    enumeration_complete = count == planned
    if not enumeration_complete and stop_reason is None:
        stop_reason = "the_bound_active_component_did_not_export_its_whole_partition"
    component_complete = enumeration_complete and passed == planned
    result = dict(schema=SCHEMA,completed=True,source_sha256=sha_bytes(Path(__file__).read_bytes()),
        input_binding=receipt(args.out/"input-binding.json"),complete_mixed_pairs=receipt(stream_path),
        planned_cartesian_pairs=planned,processed_pairs=count,phase_component_paid_pairs=passed,
        explicit_original_local_chart_responsibilities=local,unavailable_active_ball_pairs=unavailable,
        unresolved_phase_pairs=unresolved_phase,
        unvisited_pair_rank_suffix=None if enumeration_complete else [count,planned],
        rank_rule="rank=active_ordinal*fixed_cap_cell_count+cap_index; exact half-open unvisited suffix",
        complete_cartesian_pair_enumeration=enumeration_complete,
        complete_mixed_phase_component=component_complete,
        every_mixed_pair_R281_paid_or_explicit_original_local_responsibility=(
            enumeration_complete and unavailable == 0 and unresolved_phase == 0),
        explicit_local_responsibilities_actually_discharged=False,
        no_worst_list_or_four_child_truncation=True,
        exact_original_marked_tau=str(tau),new_tau_chosen=False,
        old_static_base_R24_and_local_curvature_and_metric_gates_changed=False,
        all_original_native_same_g_and_whole_image_responsibilities_remain_required=True,
        old_static_base_rotated_at_one_endpoint=False,
        original_pair_gates_combined_into_new_global_acceptance=False,
        full_surface_embedding_or_reach_certified=False,
        same_g_or_held_or_delta_E_certified=False,task_completed=False,
        resource_stop=stop_reason,elapsed_seconds=time.monotonic()-started,
        parameters=dict(max_pairs=args.max_pairs,budget_seconds=args.budget_seconds,
            sqrt_bits=args.sqrt_bits,phase_max_depth=args.phase_max_depth,phase_max_cells=args.phase_max_cells),
        scope=[
            "Actual complete active cells against actual complete fixed marked cap cells, both sheets, all phases.",
            "The untouched original cover is retained as a separate conditional static-base/R24 route; its worst list is not a universe.",
            "Cuff/near-diagonal cell products require the original complete local-chart/path responsibility and are not silently dropped.",
            "Active-active, fixed-fixed, global C2/immersion, the original curvature and metric budgets, and whole-image held bounds remain their original owners.",
            "A budget exhaustion or inconclusive phase polynomial is unresolved, not a geometric counterexample."])
    raw = canonical(result)
    (args.out/"result.json").write_bytes(raw)
    print(json.dumps(dict(event="complete_actual_mixed_phase_component",
        planned_pairs=planned,processed_pairs=count,phase_component_paid_pairs=passed,
        local_responsibility_pairs=local,complete_mixed_phase_component=component_complete,
        result_sha256=sha_bytes(raw),result_bytes=len(raw),
        full_surface_embedding_or_reach_certified=False),sort_keys=True,separators=(",",":")),flush=True)


if __name__ == "__main__":
    main()
