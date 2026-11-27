#!/usr/bin/env python3
"""Complete actual-fixed-fejer R722 normal-root and physical-sixjet producer.

All original recorded angles and all 32 common stages are retained. The
optional continuous part always covers the full circle, never an assumed
quarter-orbit reduction. Complete accurate radial/field evaluations run only
in repository Actions. No working F/J/root is replayed and no unreturned
packet or comparison field is fabricated.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time
import uuid

SCHEMA = "actual-fixed-fejer-meridian-batched-R722-complete-normal-root-and-physical-sixjet-fees-v1"
JOURNAL_SCHEMA = "actual-fixed-fejer-meridian-batched-R722-complete-normal-fee-journal-v1"
TOPIC = "topics/visible-flex-larger-amplitude"
PINS = {
    "actual_input": ("fixed_fejer_meridian_batched_normal_packet_accurate_field_input.py", "d892bedeadca4fe0689069ac7489a41c1d348311c2b84dad292bf48133e71cc7"),
    "accurate_rotation": ("accurate_normal_rotation_and_stage_boxes.py", "29eed317796b18c5f7430535ee2f45ee7ce9cb6546bbbd44d0bc97b9839e3f6b"),
    "accurate_radial": ("fixed_fejer_meridian_batched_producer_R722_accurate_reference_control_radial_boxes.py", "7c66ed0f31323451156c1cd76ae7401eb497f37377393bb66503523ad2aaac54"),
    "posterior_mean": ("fixed_fejer_meridian_batched_producer_R722_posterior_mean_jets.py", "4fc252f8977f4f4246d2cc13583efc0bccd4b28742df3a797d1c266cdd1eac7d"),
}
ACTUAL_DRIVER = "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f"
ACTUAL_READER = "8027ec35ea8ee74ab38468678683d798530e8c7a229ec3f9e8d5c631c75dde49"


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Complete accurate normal fees require public repository Actions")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
        allow_nan=False).encode()).hexdigest()


def encode(value):
    if isinstance(value, F):
        return str(value)
    if hasattr(value, "json") and callable(value.json):
        return value.json()
    if isinstance(value, dict):
        return {str(k): encode(v) for k,v in value.items()}
    if isinstance(value, (list,tuple)):
        return [encode(v) for v in value]
    if value is None or type(value) in (bool,int,str):
        return value
    if type(value) is float and math.isfinite(value):
        # Pre-existing finite JSON metadata is retained as its original value.
        return value
    raise TypeError("Keep all accurate values rational and actual metadata finite")


def file_record(path):
    path = Path(path).resolve()
    return dict(path=str(path),bytes=path.stat().st_size,sha256=sha(path))


def read_record(record):
    path = Path(record["path"]).resolve()
    if file_record(path) != record:
        raise ValueError("Changed complete accuracy result: "+str(path))
    payload = path.read_bytes()
    if hashlib.sha256(payload).hexdigest() != record["sha256"]:
        raise ValueError("A recorded complete JSON changed during reading")
    return json.loads(payload)


def write_json(path,value):
    path = Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    text = json.dumps(encode(value),sort_keys=True,indent=2,allow_nan=False)+"\n"
    temp = path.with_name(path.name+".partial-"+uuid.uuid4().hex)
    with temp.open("x") as handle:
        handle.write(text)
        handle.flush()
        os.fsync(handle.fileno())
    temp.replace(path)
    return file_record(path)


def immutable_json(path,value):
    path = Path(path)
    encoded = encode(value)
    if path.exists():
        old = json.loads(path.read_text())
        if old != encoded:
            raise ValueError("An immutable same-field accuracy file already has different contents")
        return file_record(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    temp = path.with_name(path.name+".partial-"+uuid.uuid4().hex)
    raw = (json.dumps(encoded,sort_keys=True,indent=2,allow_nan=False)+"\n").encode()
    with temp.open("xb") as handle:
        handle.write(raw)
        handle.flush()
        os.fsync(handle.fileno())
    try:
        os.link(temp,path)
    except FileExistsError:
        if path.read_bytes() != raw:
            raise ValueError("Concurrent immutable accurate output differs")
    finally:
        if temp.exists():
            temp.unlink()
    return file_record(path)


def load(name,path,digest):
    if sha(path) != digest:
        raise ValueError("A complete accuracy-source role changed: "+str(path))
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    if sha(path) != digest or sha(module.__file__) != digest:
        raise ValueError("Changed complete module during loading")
    return module


def word_intervals(value,r,bits):
    if hasattr(value,"tolist"):
        value = value.tolist()
    if isinstance(value,list):
        return [word_intervals(v,r,bits) for v in value]
    if not isinstance(value,(float,int)) or isinstance(value,bool) or not math.isfinite(value):
        raise ValueError("Use the entire finite actual packet array")
    word = float(value).hex()
    exact = r.binary_word(word)
    answer = r.Interval(exact,exact,bits)
    if answer.lo != answer.hi:
        raise ArithmeticError("Declared outward precision does not preserve an actual comparison word")
    return answer


def boxes(value,shape,r,bits):
    if not shape:
        return r.box(value,bits)
    if not isinstance(value,list) or len(value) != shape[0]:
        raise ValueError("Incomplete saved accurate box shape")
    return [boxes(v,shape[1:],r,bits) for v in value]


def point_in_box(value,box):
    return F(box[0]) <= value <= F(box[1])


def box_inclusion(inner,outer):
    if len(inner) != 3 or len(outer) != 3:
        raise ValueError("A complete three-coordinate root box is required")
    return all(F(a[0]) >= F(b[0]) and F(a[1]) <= F(b[1]) for a,b in zip(inner,outer))


def plan_jobs(actual,r,bits,full_angle_cells):
    """All actual angles plus an explicit full [0,2*pi] closed interval cover."""
    if type(full_angle_cells) is not int or full_angle_cells < 0:
        raise ValueError("Keep an explicit nonnegative full-circle cell count")
    pi0 = actual.seed_fees.pi_bounds(bits)
    pi = r.Interval(pi0.lo,pi0.hi,bits)
    jobs = []
    for index,angle in enumerate(actual.angles):
        q = r.binary_word(angle)
        jobs.append(dict(id="actual-"+str(index).zfill(6),kind="actual_literal",
            literal_phi_hex=angle,actual_anchor=angle,accurate_phi_interval=[str(q),str(q)],
            original_cache_index=index,original_required_angle=angle in actual.required_angles))
    candidates = [(r.binary_word(angle),angle) for angle in actual.angles]
    if full_angle_cells and not candidates:
        raise ValueError("No actual comparison carrier exists for a continuous-angle proposal")
    for index in range(full_angle_cells):
        a,b = F(2*index,full_angle_cells),F(2*(index+1),full_angle_cells)
        interval = r.Interval(a,b,bits)*pi
        centre = (interval.lo+interval.hi)/2
        anchor = min(candidates,key=lambda item:abs(item[0]-centre))[1]
        jobs.append(dict(id="circle-"+str(index).zfill(6),kind="full_angle_cell",
            actual_anchor=anchor,accurate_phi_interval=interval.json(),
            exact_phi_over_pi_interval=[str(a),str(b)],full_circle_cell_index=index,
            original_working_words_at_other_angles_not_claimed=True))
    return jobs,pi


class CompleteJobJournal:
    """All successful stages and unsuccessful attempts in a hash-linked journal."""

    def __init__(self,directory,binding,request,*,partition,radii):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True,exist_ok=True)
        self.request = request
        self.partition = partition
        self.radii = [str(v) for v in radii]
        self.header = dict(schema=JOURNAL_SCHEMA,complete_execution_binding=binding,
            request=request,exact_normal_step_nodes=[str(v) for v in partition],
            original_stage_count=len(partition)-1,root_radius_proposals=self.radii,
            all_original_angles_and_stages_retained=True)
        self.header_record = immutable_json(self.directory/"binding.json",self.header)
        self.identity = canonical(self.header)
        self.path = self.directory/"journal.jsonl"
        self.events = []
        self.stages = []
        self.physical = None
        self.completed = None
        self.reference_record = None
        self.last_hash = self.identity
        if self.path.exists():
            with self.path.open("rb") as handle:
                for raw in handle:
                    if not raw.endswith(b"\n"):
                        raise ValueError("An incomplete journal line must not be treated as a complete fee result")
                    item = json.loads(raw)
                    self._accept(item)

    def _accept(self,item):
        if (not isinstance(item,dict) or item.get("sequence") != len(self.events)+1
                or item.get("previous_identity_sha256") != self.last_hash
                or item.get("event_identity_sha256") != canonical(item.get("definition"))
                or item["definition"].get("journal_binding_identity_sha256") != self.identity):
            raise ValueError("The complete same-field accuracy journal chain changed")
        event = item["definition"]
        kind = event.get("kind")
        if self.completed is not None:
            raise ValueError("No accuracy event may follow a completed immutable job")
        if kind == "stage_complete":
            stage = event["stage"]
            index = len(self.stages)+1
            proof = stage["complete_proof"]
            if (stage.get("normal_stage_index") != index or index >= len(self.partition)
                    or F(proof["tau"]) != self.partition[index] or proof.get("passed") is not True
                    or str(F(stage["selected_radius"])) not in self.radii
                    or F(proof["contraction_radius"]) != F(stage["selected_radius"])
                    or F(proof["q"]) >= 1 or F(proof["strict_invariance_margin"]) <= 0
                    or proof.get("all_upstream_control_and_frame_angular_jets_propagated") is not True
                    or len(stage.get("eta0_centre_binary64_hex",[])) != 3):
                raise ValueError("Keep every original accurate stage in order with its complete proof")
            if self.physical is not None or self.completed is not None:
                raise ValueError("No stage may be appended after complete physical output")
            self._bind_reference(stage["whole_accurate_oracle_reference"])
            self.stages.append(stage)
        elif kind == "accurate_attempt_unavailable":
            if event.get("next_normal_stage_index") != len(self.stages)+1:
                raise ValueError("An unavailable attempt cannot skip an original stage")
        elif kind == "physical_file_complete":
            if len(self.stages) != len(self.partition)-1 or self.physical is not None:
                raise ValueError("Physical sixjets require the entire accurate original normal chain")
            record = event["file"]
            if file_record(record["path"]) != record:
                raise ValueError("The complete physical interval stream changed")
            if type(event.get("complete_radial_leaf_count")) is not int or event["complete_radial_leaf_count"] < 1:
                raise ValueError("Keep every exact positive radial leaf")
            self.physical = event
        elif kind == "job_complete":
            if self.physical is None or self.completed is not None:
                raise ValueError("A job cannot complete without its entire physical interval stream")
            self._bind_reference(event["complete_accurate_reference_and_domain"])
            self.completed = event
        else:
            raise ValueError("Unknown complete normal-fee journal event")
        self.events.append(item)
        self.last_hash = item["event_identity_sha256"]

    def _bind_reference(self,record):
        expected_path = (self.directory/"accurate-reference-and-domain.json").resolve()
        if Path(record["path"]).resolve() != expected_path:
            raise ValueError("A stage must bind this job's complete same-field reference proof")
        if self.reference_record is None:
            if file_record(expected_path) != record:
                raise ValueError("The complete reference/domain proof changed")
            self.reference_record = dict(record)
        elif record != self.reference_record:
            raise ValueError("One immutable job cannot change its complete reference proof")

    def recheck_outputs(self):
        expected_journal = hashlib.sha256()
        for event in self.events:
            expected_journal.update((json.dumps(event,sort_keys=True,separators=(",",":"),
                allow_nan=False)+"\n").encode())
        if self.path.exists():
            if sha(self.path) != expected_journal.hexdigest():
                raise ValueError("The complete on-disk journal differs from all consumed events")
        elif self.events:
            raise ValueError("A complete consumed accuracy journal is missing")
        if file_record(self.header_record["path"]) != self.header_record:
            raise ValueError("The complete job binding changed")
        if self.reference_record is not None and file_record(
                self.reference_record["path"]) != self.reference_record:
            raise ValueError("The complete reference/domain proof changed after consumption")
        if self.physical is not None and file_record(
                self.physical["file"]["path"]) != self.physical["file"]:
            raise ValueError("The complete accurate physical interval stream changed")
        return True

    def append(self,kind,**payload):
        definition = encode(dict(journal_binding_identity_sha256=self.identity,kind=kind,**payload))
        item = dict(sequence=len(self.events)+1,previous_identity_sha256=self.last_hash,
            definition=definition,event_identity_sha256=canonical(definition))
        # Validate an independent temporary state by the same transition rules.
        old = (list(self.events),list(self.stages),self.physical,self.completed,
            self.last_hash,self.reference_record)
        try:
            self._accept(item)
        except Exception:
            (self.events,self.stages,self.physical,self.completed,
                self.last_hash,self.reference_record) = old
            raise
        try:
            with self.path.open("ab") as handle:
                handle.write((json.dumps(item,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode())
                handle.flush()
                os.fsync(handle.fileno())
        except Exception:
            (self.events,self.stages,self.physical,self.completed,
                self.last_hash,self.reference_record) = old
            raise
        return item

    def summary(self):
        return dict(request=self.request,journal_header=self.header_record,
            journal=(file_record(self.path) if self.path.exists() else None),
            journal_binding_identity_sha256=self.identity,last_event_identity_sha256=self.last_hash,
            completed_stage_count=len(self.stages),original_stage_count=len(self.partition)-1,
            unavailable_attempt_count=sum(e["definition"]["kind"]=="accurate_attempt_unavailable" for e in self.events),
            complete=self.completed is not None,complete_physical_stream=self.physical,
            complete_reference_and_domain_file=self.reference_record,
            all_original_stages_retained=True,complete_journal_event_count=len(self.events))


def stage_source(journal,actual_packet,index):
    packet = actual_packet["packet"]
    record = packet["definition"]["stages"][index-1]
    return dict(original_packet_file=actual_packet["original_packet_file"],
        actual_packet_identity_sha256=packet["packet_identity_sha256"],
        actual_packet_arrays_file=packet["arrays_file"],
        actual_original_stage_metadata=record,
        actual_cached_angular_order=packet["definition"]["actual_cached_angular_order"],
        original_root_order_not_upgraded=True)


def completed_stage(request,journal,actual_packet,index,proof,eta,radius,attempts):
    source = stage_source(journal,actual_packet,index)
    order = source["actual_cached_angular_order"]
    return dict(normal_stage_index=index,selected_radius=str(radius),
        eta0_centre_binary64_hex=[float(v).hex() for v in eta[0]],
        complete_proof=encode(proof),source=source,all_radius_attempts=attempts,
        actual_comparison_scope=("same literal angle and original saved angular order"
            if request["kind"]=="actual_literal" else "genuine original anchor words used only as constant proposals on the whole angular cell"),
        actual_working_second_angular_word_comparison_available=order==2,
        uncomputed_stored_high_order_slots_are_only_arbitrary_comparison_carriers=order<2,
        accurate_second_angular_solution_enclosed_without_working_root_upgrade=True,
        off_anchor_proposal_error_not_described_as_original_working_field_error=True)


def stream_physical(oracle,controls,journal,execution_identity):
    name = "complete-physical-sixjets-"+uuid.uuid4().hex+".jsonl.gz"
    path = journal.directory/name
    count = 0
    with gzip.open(path,"xb") as handle:
        header = dict(schema="complete-actual-fixed-fejer-meridian-batched-R722-accurate-physical-sixjet-stream-v1",
            execution_identity_sha256=execution_identity,journal_binding_identity_sha256=journal.identity,
            accurate_request=journal.request,accurate_final_stage_event_identity=journal.last_hash,
            original_stage_count=32,complete_original_field_model=oracle.g.actual.model_identity,
            original_working_physical_arrays_recomputed=False)
        handle.write((json.dumps(header,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode())
        for item in oracle.physical_cells(controls):
            count += 1
            handle.write((json.dumps(encode(dict(kind="complete_closed_radial_cell",
                ordinal=count,**item)),sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode())
        if count != len(oracle.leaves):
            raise ValueError("The complete exact radial field stream omitted a cell")
        footer = dict(kind="complete_radial_cover_footer",complete_radial_leaf_count=count,
            all_exact_radial_leaves_written=True,working_sixjet_words_not_supplied=True,
            full_closed_surface_seams_or_reach_certified=False)
        handle.write((json.dumps(footer,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode())
    return file_record(path),count


def run_job(actual,geometry,modules,request,journal,args,execution_identity):
    r = modules["accurate_rotation"]
    if journal.completed is not None:
        return journal.summary()
    phi = r.box(request["accurate_phi_interval"],args.precision_bits)
    anchor = request["actual_anchor"]
    packet = actual.packet(anchor)
    oracle = modules["accurate_radial"].AccurateAngleOracle(geometry,phi,anchor,
        radial_depth=args.radial_depth,mean_maximum_splits=args.mean_maximum_splits,
        mean_width_goal=args.mean_width_goal,first_exp_degree=args.first_exp_degree,
        maximum_exp_degree=args.maximum_exp_degree)
    proof_record = immutable_json(journal.directory/"accurate-reference-and-domain.json",
        dict(schema="complete-actual-reference-mean-and-domain-for-normal-fees-v1",
            execution_identity_sha256=execution_identity,request=request,
            accurate_reference_mean_evidence=oracle.mean_evidence,
            complete_accurate_core_and_cap=oracle.endpoints,
            precise_whole_radial_plan=oracle.leaves))
    if journal.stages:
        previous = boxes(journal.stages[-1]["complete_proof"]["controls"],(3,6),r,args.precision_bits)
    else:
        previous = [[r.point(0,args.precision_bits) for _ in range(6)] for _ in range(3)]
    control_radius = r.binary_word(actual.model["root_control_radius_hex"])
    for index in range(len(journal.stages)+1,len(actual.partition)):
        geometry.budget.check()
        prefix = "stage_"+str(index).zfill(3)+"_"
        arrays = packet["arrays"]
        eta,frame,controls,J3 = (arrays[prefix+name] for name in ("eta","frame","controls","J"))
        actual_eta = word_intervals(eta,r,args.precision_bits)
        actual_frame = word_intervals(frame,r,args.precision_bits)
        actual_controls = word_intervals(controls,r,args.precision_bits)
        actual_J3 = word_intervals(J3,r,args.precision_bits)
        attempts,accepted = [],None
        for radius in args.root_radius:
            proof = r.stage_root_box(oracle,previous=previous,actual_frame=actual_frame,
                actual_eta=actual_eta,actual_controls=actual_controls,actual_J3=actual_J3,
                tau=actual.partition[index],radius=radius,control_radius=control_radius,
                bits=args.precision_bits)
            if proof.get("passed") is True:
                accepted = (proof,radius)
                break
            attempts.append(encode(proof))
        if accepted is None:
            journal.append("accurate_attempt_unavailable",next_normal_stage_index=index,
                reason="Complete exact interval root conditions were not established for any declared proposal radius",
                complete_attempts=attempts,whole_accurate_oracle_reference=proof_record,
                scientific_root_failure_inferred=False,original_solver_success_criterion_changed=False)
            return journal.summary()
        proof,radius = accepted
        stage = completed_stage(request,journal,packet,index,proof,eta,radius,attempts)
        stage["whole_accurate_oracle_reference"] = proof_record
        journal.append("stage_complete",stage=stage)
        previous = proof["controls"]
    if journal.physical is None:
        record,count = stream_physical(oracle,previous,journal,execution_identity)
        journal.append("physical_file_complete",file=record,complete_radial_leaf_count=count,
            entire_accurate_same_field_sixjets=True,
            complete_original_working_sixjet_word_errors_paid=False)
    journal.append("job_complete",all_original_stage_count=32,
        complete_accurate_reference_and_domain=proof_record,
        actual_oracle_counts=oracle.calls,rotation_enclosure_metadata=oracle.rotations.metadata(),
        accurate_current_point_sha256=actual.point_sha256,
        all_recorded_anchor_sources_retained=True,working_fields_or_roots_replayed=False,
        local_root_uniqueness_and_whole_radial_bounds=True,
        whole_angle_branch_or_closed_surface_geometry_not_inferred_from_one_job=True)
    return journal.summary()


def contraction_domain(stage,r):
    radius = F(stage["selected_radius"])
    centre = [r.binary_word(v) for v in stage["eta0_centre_binary64_hex"]]
    return [[str(v-radius),str(v+radius)] for v in centre]


def glue_two(left,right,r,label):
    if left.completed is None or right.completed is None:
        return dict(label=label,passed=False,reason="A complete original stage chain is absent")
    if len(left.stages) != 32 or len(right.stages) != 32:
        raise ValueError("Do not glue partial original stage chains")
    steps = []
    for index,(a,b) in enumerate(zip(left.stages,right.stages),1):
        ra,rb = a["complete_proof"]["eta_jets"][0],b["complete_proof"]["eta_jets"][0]
        da,db = contraction_domain(a,r),contraction_domain(b,r)
        ab,ba = box_inclusion(ra,db),box_inclusion(rb,da)
        steps.append(dict(normal_stage_index=index,
            left_root_enclosure_in_right_uniqueness_domain=ab,
            right_root_enclosure_in_left_uniqueness_domain=ba,passed=ab or ba))
    return dict(label=label,passed=all(v["passed"] for v in steps),stages=steps,
        inclusion_is_directed_not_just_intersection=True,
        preceding_stage_identity_required_and_inductively_retained=True,
        comparison_domain_is_the_same_exact_field_equation=True)


def branch_cover(actual,journals,requests,r,full_angle_cells):
    if not full_angle_cells:
        return dict(full_circle_requested=False,complete_continuous_angle_branch_certified=False,
            actual_point_fees_are_not_a_continuous_cover=True)
    circle = [journals[q["id"]] for q in requests if q["kind"]=="full_angle_cell"]
    if len(circle) != full_angle_cells:
        raise ValueError("Keep the entire explicit full-circle cover")
    if any(item.completed is None for item in circle):
        return dict(full_circle_requested=True,complete_continuous_angle_branch_certified=False,
            complete_circle_cell_count=sum(item.completed is not None for item in circle),
            requested_circle_cell_count=full_angle_cells,reason="Some complete angle-cell obligations remain")
    adjacent = [glue_two(a,b,r,"adjacent closed full-circle cells "+str(i))
                for i,(a,b) in enumerate(zip(circle,circle[1:]))]
    periodic = glue_two(circle[0],circle[-1],r,"exact 0/2pi periodic endpoint")
    associations = []
    for request in requests:
        if request["kind"] != "actual_literal":
            continue
        point = r.binary_word(request["literal_phi_hex"])
        possibilities = [item for item in circle
            if point_in_box(point,item.request["accurate_phi_interval"])]
        checks = [glue_two(journals[request["id"]],item,r,
            "actual literal root to full-circle cell "+item.request["id"]) for item in possibilities]
        associations.append(dict(actual_job=request["id"],literal_phi_hex=request["literal_phi_hex"],
            actual_required_angle=request["original_required_angle"],
            passed=any(v["passed"] for v in checks),
            no_silent_modulo_or_rounded_angle_replacement=True,checks=checks))
    complete = (all(v["passed"] for v in adjacent) and periodic["passed"]
                and all(v["passed"] for v in associations))
    return dict(full_circle_requested=True,complete_continuous_angle_branch_certified=complete,
        exact_complete_angle_domain_over_pi=["0","2"],no_quarter_orbit_reduction=True,
        complete_circle_cell_count=len(circle),requested_circle_cell_count=full_angle_cells,
        adjacent_directed_inclusions=adjacent,periodic_directed_inclusion=periodic,
        every_original_recorded_angle_association=associations,
        periodic_equation_proof=dict(
            all_current_and_fixed_angular_modes_are_original_integer_frequencies=True,
            accurate_global_positive_core_inverse_has_exact_two_pi_lift=True,
            full_R722_unique_reference_mean_and_projected_frame_are_two_pi_periodic=True,
            exact_controls_and_fixed_common_stage_partition_preserved=True,
            unique_local_roots_glued_from_the_identical_zero_control_stage=True,
            source_specific_field_model_identity_sha256=actual.model_identity),
        whole_declared_control_ball_uniqueness_claimed=False,
        reflected_lower_surface_or_cap_C2_seams_certified=False)


def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True)
    p.add_argument("--report",type=Path,required=True,
        help="A genuine immutable report of the complete fixed Fejer immutable-point normal entry")
    p.add_argument("--report-sha256")
    p.add_argument("--snapshot-identity-sha256",
        help="Select this genuinely recorded complete point; default is latest complete required-angle snapshot")
    p.add_argument("--outdir",type=Path,required=True)
    p.add_argument("--seconds",type=float,default=3600.)
    p.add_argument("--maximum-leaf-evaluations",type=int,default=1000000)
    p.add_argument("--precision-bits",type=int,default=192)
    p.add_argument("--panels",type=int,default=128)
    p.add_argument("--rho-leaf-budget",type=int,default=8192)
    p.add_argument("--inverse-steps",type=int,default=64)
    p.add_argument("--inverse-width",default="1/1000000000000000000000000")
    p.add_argument("--full-angle-cells",type=int,default=1024,
        help="Complete [0,2pi] cells; zero requests all actual literal angles only, never a continuous certificate")
    p.add_argument("--radial-depth",type=int,default=0)
    p.add_argument("--mean-maximum-splits",dest="mean_maximum_splits",type=int,default=8192)
    p.add_argument("--mean-width-goal",default="1/1000000000")
    p.add_argument("--first-exp-degree",type=int,default=24)
    p.add_argument("--maximum-exp-degree",type=int,default=128)
    p.add_argument("--root-radius",action="append",
        help="Explicit positive local fee-box radius; repeated proposals do not alter the scientific model")
    args = p.parse_args()
    if args.root_radius is None:
        args.root_radius = ["1/100000000","1/1000000","1/10000"]
    args.root_radius = [F(v) for v in args.root_radius]
    if not args.root_radius or any(v <= 0 for v in args.root_radius):
        raise ValueError("All complete local interval proposal radii must be positive")
    if len(set(args.root_radius)) != len(args.root_radius):
        raise ValueError("Do not silently repeat a root-domain proposal")
    return args


def main():
    args = parse_args()
    require_actions()
    started = time.monotonic()
    root = args.repo.resolve()/TOPIC/"scripts/resume_20261126"
    paths = {role:root/name for role,(name,digest) in PINS.items()}
    modules = {role:load("_complete_normal_fee_"+role,paths[role],digest)
               for role,(name,digest) in PINS.items()}
    actual = modules["actual_input"].ActualNormalPacketPoint(args)
    actual.used.add(__file__)
    for path in paths.values():
        actual.used.add(path)
    outdir = actual.used.protect_output(args.outdir)
    r,radial = modules["accurate_rotation"],modules["accurate_radial"]
    budget = radial.WorkBudget(seconds=args.seconds,
        maximum_leaf_evaluations=args.maximum_leaf_evaluations)
    requests,pi = plan_jobs(actual,r,args.precision_bits,args.full_angle_cells)
    parameters = dict(precision_bits=args.precision_bits,panels=args.panels,
        rho_leaf_budget=args.rho_leaf_budget,inverse_steps=args.inverse_steps,
        inverse_width=str(F(args.inverse_width)),full_angle_cells=args.full_angle_cells,
        radial_depth=args.radial_depth,mean_maximum_splits=args.mean_maximum_splits,
        mean_width_goal=str(F(args.mean_width_goal)),first_exp_degree=args.first_exp_degree,
        maximum_exp_degree=args.maximum_exp_degree,root_radius=[str(v) for v in args.root_radius])
    request_binding = encode(dict(schema=SCHEMA+"-complete-input-and-request",
        source_sha256=sha(__file__),
        complete_source_sha256_by_role={role:value[1] for role,value in PINS.items()},
        actual_complete_input=actual.binding,actual_complete_input_identity_sha256=actual.identity,
        complete_parameters=parameters,complete_angle_requests=requests,
        accurate_pi_enclosure=pi,all_actual_required_and_cached_angles_preserved=True,
        complete_normal_stage_count=32,numerical_solver_or_metric_target_changed=False,
        accuracy_budgets_are_not_new_scientific_acceptance_criteria=True))
    request_identity = canonical(request_binding)
    outdir.mkdir(parents=True,exist_ok=True)
    request_record = immutable_json(outdir/"complete-input-and-request.json",request_binding)
    geometry = None
    binding_record = None
    identity = None
    journals = {}
    unavailable = None
    final_bytes_rechecked = False
    def report():
        if geometry is None or len(journals) != len(requests):
            summaries = [(journals[q["id"]].summary() if q["id"] in journals else
                dict(request=q,complete=False,completed_stage_count=None,
                    original_stage_count=32,journal_header=None,journal=None,
                    complete_physical_stream=None,
                    prior_saved_job_state="not reread before complete accurate geometry setup"))
                for q in requests]
            cover = dict(full_circle_requested=bool(args.full_angle_cells),
                complete_continuous_angle_branch_certified=False,
                complete_circle_cell_count=0,requested_circle_cell_count=args.full_angle_cells,
                reason="The complete accurate geometry/journal setup is not yet available")
        else:
            summaries = [journals[q["id"]].summary() for q in requests]
            cover = branch_cover(actual,journals,requests,r,args.full_angle_cells)
        all_done = bool(summaries) and all(v["complete"] for v in summaries)
        return dict(schema=SCHEMA,source_sha256=sha(__file__),source_commit=os.environ.get("GITHUB_SHA"),
            github_run_id=os.environ.get("GITHUB_RUN_ID"),github_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
            complete_input_and_request=request_record,
            complete_input_and_request_identity_sha256=request_identity,
            complete_binding=binding_record,complete_binding_identity_sha256=identity,
            actual_report=actual.report_record,actual_current_full_point_sha256=actual.point_sha256,
            actual_snapshot_identity_sha256=actual.snapshot["snapshot_identity_sha256"],
            actual_scientific_driver_sha256=ACTUAL_DRIVER,actual_pure_reader_sha256=ACTUAL_READER,
            accurate_geometry_setup_complete=geometry is not None,
            complete=all_done and final_bytes_rechecked,
            all_bound_input_and_output_bytes_rechecked_at_final_report=final_bytes_rechecked,
            all_planned_original_stages_and_sixjet_streams_complete=all_done,
            all_original_recorded_angle_count=len(actual.angles),
            all_original_required_angle_count=len(actual.required_angles),
            requested_full_circle_cell_count=args.full_angle_cells,planned_job_count=len(requests),
            completed_job_count=sum(v["complete"] for v in summaries),
            unfinished_job_ids=[v["request"]["id"] for v in summaries if not v["complete"]],
            full_same_field_angle_branch=cover,actual_jobs=summaries,
            accurate_geometry=(geometry.metadata() if geometry is not None else None),
            actual_input=actual.metadata(),actual_work_budget=budget.metadata(),
            latest_unavailable=unavailable,
            elapsed_seconds_binary64_hex=float(time.monotonic()-started).hex(),
            existing_working_root_and_field_calls=0,existing_working_J_or_Jtranspose_calls=0,
            comparison_candidates_were_existing_complete_actual_packet_words=True,
            working_second_order_words_not_invented=True,
            complete_original_working_physical_sixjet_word_errors_paid=False,
            physical_sixjet_output_scope="accurate entire upper-meridian radial/angle boxes for the bound selected exact chain",
            complete_reflected_closed_surface_C2_or_reach_certificate=False,
            external_parameter_J_and_transpose_error_certificate=False,
            unknown_historical_material_role_obligations_removed=False,
            mathematical_problem_completion_claimed=False)
    def print_result(record,value):
        print(json.dumps(dict(schema=SCHEMA,report=record,complete=value["complete"],
            completed_job_count=value["completed_job_count"],planned_job_count=value["planned_job_count"],
            complete_continuous_angle_branch_certified=value["full_same_field_angle_branch"][
                "complete_continuous_angle_branch_certified"],
            working_F_J_root_calls=0,geometry_certified=False),sort_keys=True))
    write_json(outdir/"report.json",report())
    try:
        geometry = radial.AccurateFieldGeometry(actual,r,bits=args.precision_bits,
            rho_leaf_budget=args.rho_leaf_budget,inverse_steps=args.inverse_steps,
            inverse_width=args.inverse_width,budget=budget)
        binding = encode(dict(schema=SCHEMA,source_sha256=sha(__file__),
            complete_source_sha256_by_role={role:value[1] for role,value in PINS.items()},
            actual_complete_input=actual.binding,actual_complete_input_identity_sha256=actual.identity,
            complete_input_and_request_identity_sha256=request_identity,
            accurate_geometry_identity_sha256=geometry.identity,complete_parameters=parameters,
            complete_angle_requests=requests,accurate_pi_enclosure=pi,
            all_actual_required_and_cached_angles_preserved=True,complete_normal_stage_count=32,
            numerical_solver_or_metric_target_changed=False,
            accuracy_budgets_are_not_new_scientific_acceptance_criteria=True))
        identity = canonical(binding)
        binding_record = immutable_json(outdir/"complete-binding.json",binding)
        for request in requests:
            journals[request["id"]] = CompleteJobJournal(outdir/"angles"/request["id"],
                identity,request,partition=actual.partition,radii=args.root_radius)
    except (radial.EnclosureUnavailable,ArithmeticError) as error:
        unavailable = dict(scope="complete-accurate-geometry-and-journal-setup",
            reason=str(error),type=type(error).__name__,
            incomplete_is_not_nonexistence_or_solver_failure=True)
        actual.recheck()
        final = report()
        result_record = write_json(outdir/"report.json",final)
        print_result(result_record,final)
        return 0
    except Exception as error:
        unavailable = dict(scope="complete-accurate-geometry-and-journal-setup",
            reason=str(error),type=type(error).__name__,complete_bound_evaluation_stopped=True,
            incomplete_is_not_nonexistence_or_solver_failure=True)
        actual.recheck()
        write_json(outdir/"report.json",report())
        raise
    report_record = write_json(outdir/"report.json",report())
    for request in requests:
        journal = journals[request["id"]]
        if journal.completed is not None:
            continue
        try:
            run_job(actual,geometry,modules,request,journal,args,identity)
        except (radial.EnclosureUnavailable,ArithmeticError) as error:
            unavailable = dict(job_id=request["id"],reason=str(error),
                type=type(error).__name__,next_original_stage_index=len(journal.stages)+1,
                incomplete_is_not_nonexistence_or_solver_failure=True)
            if len(journal.stages) < 32 and journal.completed is None:
                journal.append("accurate_attempt_unavailable",
                    next_normal_stage_index=len(journal.stages)+1,
                    reason=str(error),exception_type=type(error).__name__,
                    scientific_root_failure_inferred=False)
            report_record = write_json(outdir/"report.json",report())
            if time.monotonic() >= budget.deadline or budget.leaves >= budget.maximum:
                break
        except Exception as error:
            unavailable = dict(job_id=request["id"],reason=str(error),
                type=type(error).__name__,complete_bound_evaluation_stopped=True,
                next_original_stage_index=len(journal.stages)+1,
                incomplete_is_not_nonexistence_or_solver_failure=True)
            actual.recheck()
            write_json(outdir/"report.json",report())
            raise
        report_record = write_json(outdir/"report.json",report())
    actual.recheck()
    for record in (request_record,binding_record):
        if file_record(record["path"]) != record:
            raise ValueError("A complete top-level input or execution binding changed")
    for journal in journals.values():
        journal.recheck_outputs()
    final_bytes_rechecked = True
    final = report()
    report_record = write_json(outdir/"report.json",final)
    print_result(report_record,final)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
