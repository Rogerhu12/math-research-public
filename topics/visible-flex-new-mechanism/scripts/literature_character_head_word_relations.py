#!/usr/bin/env python3
"""New functional relations on R174's 77 literal basis columns.

Use a shared fixed-color right-word map on stored originals.  Reuse the
published pure R40/J/D0 representatives.  The resulting Psi is the linear
extension of bound per-column identities, not an asserted copy of Phi.
Every proposed kernel relation is checked independently by (i) freshly
assembling its two original polynomial differences, and (ii) summing its
source-bound column-conversion identities in the two faithful projections.
No old seventy literal identities, pure40/31, forcing, response, profile
query, old RREF, LP, or path integral is recomputed.

Genuine work is restricted to this public repository's GitHub Actions.
Local --toy-only uses only small invented inputs.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from fractions import Fraction as F
import gzip
import json
from math import lcm
import os
from pathlib import Path
import resource
import sys
import time

import literature_character_head_literal_relations as raw
import literature_color_priority_words as priority

exact, colored, words = priority.exact, priority.colored, priority.words
SCHEMA = "visible-flex-character-head-fixed-color-word-relations-v1"
REPOSITORY = raw.REPOSITORY
LANE = "character_head_word_relations"
MAIN_NAME = "character-head-word-relations.json"
CERT_NAME = "character-head-word-relations-certificate.json.gz"
STATE_NAME = "character-head-word-relations-state.json.gz"
PROJECTIONS = (-4, -2)
EXPECTED_BASIS = tuple(range(40)) + (40,41,42,44,45,47,48,50,60,63,65,68,70,71,
    78,80,83,85,86,88,93,98,103,109,111,112,113,115,117,130,131,132,137,138,140,141,143)
OLD_NEW_EQUALITIES = (0,4,35,55,62,64,65,66,67)
PURE_POSITIONS = (0,1,2,3,8,9,10,12,19)
FROZEN = {
    "raw": {"filename":"literature_character_head_literal_relations.py","bytes":58885,
        "sha256":"80ab553a2dbb35fd4547beaf1b7ad094e831a2cb7f02e4968b867c4654cd9995"},
    "priority": {"filename":"literature_color_priority_words.py","bytes":21642,
        "sha256":"ec2022d8f9ba764dad05350b6fd2084d0c8fdc4bb9a26550f65f1f95f504a9b9"},
    "exact": {"filename":"literature_pure_bulk_exact_membership.py","bytes":33718,
        "sha256":"f7f3e3c6c8732ad9da047fb6005d314dc8568c189fe3cc0c9edef8843051eb70"},
    "colored": {"filename":"literature_colored_profile_algebra.py","bytes":15738,
        "sha256":"c0d87a214f27a03fb29cd07cc5e9740249580da7f854ed4ff02d6eaf69b1f66f"},
    "words": {"filename":"literature_pure_bulk_word_normal_form.py","bytes":32310,
        "sha256":"d39482c9e33e7358f1afa51b073daf5f65e84b4858f9a18f446206e8f9d9ea65"},
    "profile_storage": {"filename":"literature_range_profile_algebra.py","bytes":33169,
        "sha256":"a7f1771a33a8e73934f9549b3407a9e351fed59a9eec163c5b11c965c7f1dc52"},
}
LITERAL = {
    "run":"43670254711","commit":"952cf7927d809150ac2579f1a390225c2cf23f52",
    "lane":"character_head_literal_relations","schema":"visible-flex-character-head-literal-relations-v1",
    "main":{"filename":"character-head-literal-relations.json","bytes":7103,
        "sha256":"0d3351e00b434292b7b8fce62ac74096ea0fbb96cdf78998bb096d29ab336055"},
    "receipt":{"filename":"receipt.json","bytes":41254,
        "sha256":"043a234f7cf4c8962d50edc69a441794f562041e2fbf334c8ad570335ae42d73"},
    "artifact":{"filename":"character-head-literal-relations-certificate.json.gz",
        "stored_bytes":41109,"stored_sha256":"5d929f4f45265ee4eec949eace228bf4b639753cd0a4b24a8a3d32d0857dc62e",
        "raw_bytes":269605,"raw_sha256":"ed3bedb70a0f49a058daf578ff9403a7ff89407c55f0954f876bfedaeaeac775"},
    "metadata_key":"fresh_original_relation_certificate","driver":FROZEN["raw"],
}
PURE = {
    "run":"43657785023","commit":"c606688a842bd811106ff2844e1161a4f34c159e",
    "lane":"general_pure_J_membership","schema":"visible-flex-general-pure-J-complete-response-membership-v1",
    "main":{"filename":"general-pure-J-membership.json","bytes":45019,
        "sha256":"98442251ed15b708a70e3fcbbdb2ae6cf76c8c1873aa21345354a5a320a9cfac"},
    "receipt":{"filename":"receipt.json","bytes":35841,
        "sha256":"31d6380160437b0098d33d35e4b722c79cd780d351f614a4e48901100a9d0fa4"},
    "artifact":{"filename":"general-pure-J-membership-certificate.json.gz",
        "stored_bytes":84283,"stored_sha256":"af46437f676716a20051bf3bad5a96235398dcf8a45c179d1395bc1f9d84712e",
        "raw_bytes":456216,"raw_sha256":"9859368ec20e0923cc168199a7ecb82eff0beac5fa191f1b6388e67cfd1aa550"},
    "metadata_key":"portable_original_certificate",
    "driver":{"filename":"literature_general_pure_J_membership.py","bytes":37092,
        "sha256":"1a84590f8b6f0c35a1df5f251a8ffa0e9f4da65ea2cc3bd777e752482ef05bcc"},
}
D0 = {
    "run":"43659795254","commit":"ce6c80bfbde6158e38c0e74e26fba3f352201658",
    "lane":"general_pure_D0_membership","schema":"visible-flex-general-pure-D0-archived-basis-membership-v1",
    "main":{"filename":"general-pure-D0-membership.json","bytes":39342,
        "sha256":"e78475ec38bed8057dc40d18979167ae2c4d5b5909f73fa3142a28cc38231c3d"},
    "receipt":{"filename":"receipt.json","bytes":36637,
        "sha256":"d773b41d6deebf782fc386fb4b0198c42f242ef05b7ea62fccc5d679f4d76fe2"},
    "artifact":{"filename":"general-pure-D0-membership-certificate.json.gz",
        "stored_bytes":15463,"stored_sha256":"f5355a03cbdb076c9d33900930f0cad5e5c86abf4713f6b59b3acbd9b875037e",
        "raw_bytes":88545,"raw_sha256":"117a4bf88cedd3a85ccfc26e6c80324bd67f3ce07aaf19b1837e434b0c7173cc"},
    "metadata_key":"portable_original_certificate",
    "driver":{"filename":"literature_general_pure_D0_membership.py","bytes":25604,
        "sha256":"c296f72becff4366297e3b9f00db97425b1aa5b15c10ba7625932966ae7c8f1f"},
}
POINT = {
    "run":"43672582314","commit":"14f33da3731f543bdafeee98f5f83ec5390f0b5e",
    "lane":"character_minus2_raw_positive_candidate",
    "schema":"visible-flex-character-minus2-raw-positive-candidate-v1",
    "main":{"filename":"character-minus2-raw-positive-candidate.json","bytes":7063,
        "sha256":"25b16d6cd538bb7affbc2d532ef1f1a688546f1f4777b355a632af8a0e421067"},
    "receipt":{"filename":"receipt.json","bytes":41821,
        "sha256":"61712e89f0f14b1ad6f4dab3a5423b3c3a925d30e8ad628d62fe42af3421d655"},
    "artifact":{"filename":"character-minus2-raw-positive-candidate-certificate.json.gz",
        "stored_bytes":12864,"stored_sha256":"b7b7cf0fc4bf476c918f9302462e3dc2071b5bff799bdf6131e8b6d7c22e2778",
        "raw_bytes":60197,"raw_sha256":"e37ce83e392bdc743614451126cbb64c7444788fd6ae253ead154d3d1a8f7d26"},
    "metadata_key":"complete_candidate_certificate",
    "driver":{"filename":"literature_character_minus2_raw_positive_candidate.py","bytes":29045,
        "sha256":"415e1b67f5c52ac60bf4b0fc152e1cf1c21f05b327536920517c46cc1a397d09"},
}


def source_identity():
    modules = {"raw":raw,"priority":priority,"exact":exact,"colored":colored,"words":words,
               "profile_storage":exact.formal}
    actual = {key:raw.identity(module.__file__) for key,module in modules.items()}
    if actual != FROZEN:
        raise ValueError("a frozen helper changed; explicitly rebind it before new work")
    return {"driver":raw.identity(__file__),"frozen_reused_dependencies":actual,
            "profile_atom_storage":raw.identity(exact.formal.__file__),
            "old_research_entry_points_called":False}


def check_export_identity(data,spec,suffix,identity_in_bound_manifest=False):
    if data.get("schema") != spec["schema"]+suffix:
        raise ValueError("bound export schema changed: "+spec["lane"])
    keys=("github_repository","github_run_id","github_sha")
    if identity_in_bound_manifest:
        # Exactly this old completed finite certificate omitted the three
        # duplicate fields. consume_bound already checked its exact main,
        # receipt, producer, packed/raw hashes, and identical source_hashes.
        if spec!=raw.FINITE or any(key in data for key in keys):
            raise ValueError("only the exact original finite certificate has manifest-only run identity")
        return "exact_published_main_receipt_and_artifact_hashes"
    if (data.get(keys[0]) != REPOSITORY or str(data.get(keys[1])) != spec["run"]
        or data.get(keys[2]) != spec["commit"]):
        raise ValueError("bound export embedded run/source identity changed: "+spec["lane"])
    return "embedded_identity_plus_exact_published_main_and_receipt"


def bound_data(directory, spec, suffix,identity_in_bound_manifest=False):
    main, data, binding = raw.consume_bound(directory, spec)
    check_export_identity(data,spec,suffix,identity_in_bound_manifest)
    return main, data, binding


def pure_summary(payload):
    value = raw.sha(json.dumps(payload,separators=(",",":")).encode())
    return {"terms":len(payload),"sha256":value,
        "max_word_length":max((len(row[1]) for row in payload),default=0),
        "max_local_jet_order":max((jet for row in payload
            for local in (row[0],)+tuple(row[1]) for jet in local[1]),default=0)}


def archived_pure_records(data, ddata):
    """Only read published successful conversion records; no old normalization."""
    if (data.get("pure_response_upper_bound",{}).get("input_true_full_basis_columns") != 40
        or data["pure_response_upper_bound"].get("proved_true_pure_dimension_upper_bound") != 9
        or data["pure_response_upper_bound"].get("new_original_pure_dependencies_verified") != 31
        or data.get("one_J_proposal",{}).get("original_identity_proved") is not True
        or ddata.get("one_D0_proposal",{}).get("original_identity_proved") is not True):
        raise ValueError("only the completed R151/R157 positive certificates may be reused")
    labels = data["input_basis"]["retained_original_labels"]
    records = data["pure_column_representatives"]
    if len(records) != 40 or [row["original_position"] for row in records] != list(range(40)):
        raise ValueError("the complete archived pure40 representative order changed")
    output = {}

    def append(row, name, source, original_data, extra=None):
        wanted = original_data["original_root_sha256"][name]
        expected = row.get("original_sha256",wanted)
        if expected != wanted or pure_summary(row["word_rows"]) != row["word_summary"]:
            raise ValueError("archived pure representative/root or stored word summary changed")
        hashes = raw.portable_atom_hashes(original_data["profile_atoms"])
        proof = raw.validate_root(original_data["roots"][name],hashes,wanted)
        record = {"original_sha256":wanted,"archived_original_root":name,
            "word_rows":row["word_rows"],"source":source,"word_summary":row["word_summary"],
            "original_binding":proof,"transport_theorem":"published sound right-IBP and word conversion",
            "new_normalization_of_this_old_pure_root":False}
        if extra:record.update(extra)
        output.setdefault(wanted,record)

    for i,row in enumerate(records):
        if (row["original_root"] != "original_pure_column_%02d"%i
            or labels[i]["position"] != i
            or labels[i]["weight_block_original_column"] != raw.R_ORIGINAL_COLUMNS[i]
            or labels[i]["original_pure_sha256"] != row["original_sha256"]):
            raise ValueError("pure40/source weight-block ordering changed")
        append(row,row["original_root"],"R151",data,{"R_position":i})
    append(data["target_pure_representative"],"original_J_minus4","R151_J",data)
    proposal = ddata["one_D0_proposal"]
    dname = "original_D0_minus4"
    if dname not in ddata["roots"]:
        possible = [name for name,wanted in ddata["original_root_sha256"].items()
                    if wanted == "1236f94a788454870d655dda499714eacccfee730cba582e22fb2c0b4d892f7f"]
        if len(possible) != 1:
            raise ValueError("the archived complete D0 pure root is absent or ambiguous")
        dname = possible[0]
    append({"word_rows":proposal["target_word_rows"],
            "word_summary":proposal["target_word_summary"]},dname,"R157_D0",ddata)
    return output


class OriginalInputs:
    """A read-only portable original DAG and its two faithful projections."""
    def __init__(self, head, literal, ring, budget):
        self.head = head
        self.ring = ring
        self.profile_atoms = head["profile_atoms"]
        self.hashes = raw.portable_atom_hashes(self.profile_atoms)
        self.atom_keys = []
        self.atom_degrees = []
        self.atom_weights = []
        for index,node in enumerate(self.profile_atoms):
            if node[0] == "jet":
                if node[1] not in priority.ORDER:
                    raise ValueError("the canonical head contains an undeclared input color")
                key = ring.p.jet(node[1],node[2])
                degree = (int(node[1]=="q"),int(node[1]=="qbar"))
                weight = -node[2]
            else:
                power,atoms = raw.monomial(node[1],index)
                key = ring.p.primitive(self.to_ring_monomial((power,atoms)))
                degree = tuple(sum(self.atom_degrees[a][c] for a in atoms) for c in (0,1))
                weight = power+sum(self.atom_weights[a] for a in atoms)+1
            if key[0] != 0 or len(key[1]) != 1:
                raise ValueError("portable atom reconstruction did not yield one original atom")
            self.atom_keys.append(key[1][0])
            self.atom_degrees.append(degree)
            self.atom_weights.append(weight)
        self.columns = []
        metadata = literal["column_metadata"]
        for local_index,index in enumerate(EXPECTED_BASIS):
            record = metadata[index]
            original = record["original_metadata"]
            if record["column"] != index:
                raise ValueError("published literal basis metadata changed")
            bound, projection = {}, {}
            for mode in PROJECTIONS:
                name = original["roots"][str(mode)]
                wanted = head["original_root_sha256"][name]
                rows = head["roots"][name]
                proof = raw.validate_root(rows,self.hashes,wanted)
                if proof != record["bound_mode_roots"][str(mode)]:
                    raise ValueError("selected original no longer matches R174")
                selected = []
                for monomial,n,d in rows:
                    key = raw.monomial(monomial,len(self.atom_keys))
                    degree = tuple(sum(self.atom_degrees[a][c] for a in key[1]) for c in (0,1))
                    weight = key[0]+sum(self.atom_weights[a] for a in key[1])
                    if weight != -2 or sum(degree) != 4:
                        raise ValueError("a complete canonical source column changed true weight or degree")
                    if mode == -4 and degree != (4,0):
                        raise ValueError("the source pure root is not pure q degree four")
                    if mode == -4 or degree == (2,2):
                        selected.append([monomial,n,d])
                projection[mode] = selected
                bound[str(mode)] = {"original_root":name,**proof,
                    "projection":"pure_q4" if mode==-4 else "balanced_q2_qbar2",
                    "projected_rows_sha256":raw.sha(raw.canonical(selected)),
                    "projected_terms":len(selected)}
            self.columns.append({"index":local_index,"original147_index":index,
                "normal_index":None if index<40 else index-40,
                "kind":"R" if index<40 else "normal","roots":projection,
                "source_metadata":record,"binding":bound})
            budget.check()

    def to_ring_monomial(self, key):
        return key[0],tuple(sorted(self.atom_keys[a] for a in key[1]))

    def expression(self, rows):
        return exact.Expr(self.ring,{self.to_ring_monomial(raw.monomial(key,len(self.atom_keys))):F(n,d)
                                    for key,n,d in rows})

    def root_hash(self, rows):
        payload = [[key[0],sorted(self.hashes[a] for a in key[1]),n,d] for key,n,d in rows]
        payload.sort()
        return raw.sha(json.dumps(payload,separators=(",",":")).encode())

    def bind_conversion(self, column, mode, rows, method, source):
        original = self.columns[column]
        grammar=all(priority.is_remainder_letter(letter) for row in rows for letter in row[1])
        if not grammar:
            raise ValueError("a reused or new word letter is outside the proved R178 remainder dictionary")
        return {"column":column,"original147_index":original["original147_index"],"mode":mode,
            "original_mode_sha256":original["binding"][str(mode)]["original_sha256"],
            "projected_original_sha256":self.root_hash(original["roots"][mode]),
            "word_rows_sha256":raw.sha(raw.canonical(rows)),"word_terms":len(rows),
            "conversion_method":method,"conversion_source":source,
            "every_word_letter_is_an_R178_fixed_color_remainder":True,
            "same_common_physical_right_anchor":True,
            "representative_is_an_original_function_identity":True}


def load_inputs(args, report, budget, ring):
    hmain,head,hbinding = bound_data(args.head_dir,raw.HEAD,"-original-expressions")
    lmain,literal,lbinding = bound_data(args.literal_dir,LITERAL,"-certificate")
    fmain,finite,fbinding = bound_data(args.finite_dir,raw.FINITE,"-certificate",
                                     identity_in_bound_manifest=True)
    pmain,pure,pbinding = bound_data(args.pure_dir,PURE,"-original-expressions")
    dmain,ddata,dbinding = bound_data(args.D0_dir,D0,"-original-expressions")
    cmain,point,cbinding = bound_data(args.point_dir,POINT,"-certificate")
    if (head.get("all_fourteen_families_complete") is not True
        or head.get("all_planned_contractions_present") is not True
        or head.get("target_weight") != -2 or len(head.get("normal_family_records",[])) != 107
        or len(head.get("archived_R_basis_records",[])) != 40
        or head.get("content_scope") != "complete-fourteen-weight-minus2-families-and-translation-presentation"):
        raise ValueError("only the bound complete fourteen-family head may be consumed")
    if (literal.get("all_147_columns_processed") is not True
        or literal.get("all_dependency_certificates_freshly_checked_in_both_original_modes") is not True
        or tuple(literal.get("independent_columns_of_the_literal_matrix",[])) != EXPECTED_BASIS
        or literal.get("literal_matrix_basis_size") != 77
        or len(literal.get("original_dependencies",[])) != 70
        or tuple(literal.get("new_equalities_for_the_inherited_23_coordinates",[])) != OLD_NEW_EQUALITIES):
        raise ValueError("only R174's completed 77-column literal basis is used")
    if (literal["core_input"]["head"] != hbinding
        or finite.get("normal_coordinate_metadata") != head["normal_family_records"]
        or literal["inherited_view"]["finite"] != fbinding
        or point.get("input",{}).get("original_complete_system_certificate") != raw.FINITE["artifact"]
        or cmain.get("prescribed_outer_point_verified") is not True
        or cmain.get("inequality_verification",{}).get("all_rows_satisfied_exactly") is not True):
        raise ValueError("the exact head, inherited coordinates, or completed prescribed point changed")
    transform = [raw.read_fraction_row(row,23) for row in finite["normal_coordinates_as_free_linear_forms"]]
    free = finite["free_normal_coordinates"]
    if len(transform)!=107 or len(free)!=23 or free != literal["inherited_view"]["free_normal_coordinates"]:
        raise ValueError("the inherited 107/23 coordinate map changed")
    for i,normal in enumerate(free):
        if transform[normal] != {i:F(1)}:
            raise ValueError("the old free coordinate meanings changed")
    interpreted = point["interpretation"]
    point_y = list(map(F,interpreted["free_coordinate_values"]))
    point_nu = list(map(F,interpreted["normal_coordinate_values"]))
    if (len(point_y)!=23 or len(point_nu)!=107
        or list(map(str,point_y)) != cmain["prescribed_23_coordinates"]
        or point.get("prescribed_point") != cmain["prescribed_23_coordinates"]):
        raise ValueError("the completed single point identity changed")
    # Values are consumed, not the old 86 inequalities or fourteen integrals re-evaluated.
    original = OriginalInputs(head,literal,ring,budget)
    archives = archived_pure_records(pure,ddata)
    for column in original.columns[:40]:
        wanted = column["binding"]["-4"]["original_sha256"]
        if wanted not in archives or archives[wanted]["source"] != "R151":
            raise ValueError("a pure R40 original lacks its already published representative")
    for normal,label in ((90,"R151_J"),(103,"R157_D0")):
        column = next(row for row in original.columns if row["normal_index"]==normal)
        if archives.get(column["binding"]["-4"]["original_sha256"],{}).get("source") != label:
            raise ValueError("the same original J/D0 pure target must be reused, not recomputed")
    known = []
    for index,row in enumerate(literal["inherited_view"]["inherited_parity"]):
        known.append(("R168_%d"%index,raw.read_fraction_row(row["free_coordinate_equality"],23)))
    for index in OLD_NEW_EQUALITIES:
        relation = literal["original_dependencies"][index]
        if not relation["fresh_original_check"]["all_modes_exact_original_zero"]:
            raise ValueError("a consumed old exact equality is not certified")
        known.append(("R174_%d"%index,raw.read_fraction_row(relation["old_free_coordinate_equality"],23)))
    binding = {"head":hbinding,"literal77":lbinding,"finite_B":fbinding,
        "pure_R40_and_J":pbinding,"D0_pure":dbinding,"prescribed_point":cbinding,
        "original147_basis_indices":list(EXPECTED_BASIS),
        "anchor":head["anchor"],"profile_atoms_sha256":raw.sha(raw.canonical(head["profile_atoms"])),
        "old_B_sha256":raw.sha(raw.canonical(finite["normal_coordinates_as_free_linear_forms"])),
        "point_107_sha256":raw.sha(raw.canonical(list(map(str,point_nu)))),
        "point_23_sha256":raw.sha(raw.canonical(list(map(str,point_y))))}
    report["inputs"] = binding
    report["archived_finite_identity_location"]={
        "run":raw.FINITE["run"],
        "certificate_has_no_duplicate_repository_run_source_fields":True,
        "identity_bound_by_exact_main_receipt_producer_and_packed_raw_hashes":True,
        "source_hashes_in_certificate_equal_the_bound_main":True}
    report["scope_inventory"] = {"literal_original_basis_columns":77,"archived_R_columns":40,
        "new_normal_basis_columns":37,"old_pure_R40_recomputed":0,"old_31_pure_dependencies_recomputed":0,
        "old_70_literal_dependencies_recomputed":0,"old_J_and_D0_pure_targets_recomputed":0,
        "old_86_necessary_rows_rechecked":False,"old_RREF_or_solver_recomputed":False,
        "original_response_or_forcing_recompiled":False,"single_named_candidate":POINT["run"]}
    return original,archives,transform,point_y,point_nu,known,binding


def word_rows(terms):
    return [[local,word,value.numerator,value.denominator]
            for (local,word),value in sorted(terms.items())]


def original_rows(terms):
    return [[[power,list(atoms)],value.numerator,value.denominator]
            for (power,atoms),value in sorted(terms.items())]


def original_terms(payload, count):
    result = {}
    for key,n,d in payload:
        key = raw.monomial(key,count)
        if key in result or not n or d<=0 or F(n,d).numerator!=n or F(n,d).denominator!=d:
            raise ValueError("invalid stored original difference")
        result[key] = F(n,d)
    return result


def add_scaled(target, source, amount):
    result = dict(target)
    for key,value in source.items():
        answer = result.get(key,F(0))+amount*value
        if answer:result[key]=answer
        else:result.pop(key,None)
    return result


def fresh_state(known, budget):
    small = {}
    for label,row in known:
        raw.reduce_small(row,small,budget,insert=label)
    return {"cursor":0,"pending":None,"columns":[],"row_keys":[],"row_index":{},
        "basis":{},"independent_columns":[],"relations":[],"small_basis":small,
        "new_small_equalities":0,"elimination_steps":0,"fresh_original_column_sums":0,
        "fresh_transport_column_sums":0,"mapping_term_steps":0,
        "archived_pure_representatives_consumed":0,"new_original_projections_mapped":0}


def new_mapper(ring,args):
    return priority.PriorityWords(ring,max_calls=args.max_IBP_calls,max_terms=args.max_terms,
        max_shuffle_entries=args.max_shuffle_entries,max_cache_entries=args.max_cache_entries)


def start_column(state):
    state["pending"] = {"column":state["cursor"],"stage":"map","mode_index":0,
        "term_cursor":0,"accumulator":{},"projections":{},"conversions":{}}


def finish_projection(ctx,mode,payload,method,source):
    state,inputs = ctx["state"],ctx["original"]
    pending = state["pending"];index=pending["column"]
    conversion = inputs.bind_conversion(index,mode,payload,method,source)
    pending["projections"][mode] = payload
    pending["conversions"][mode] = conversion
    pending["mode_index"] += 1
    pending["term_cursor"] = 0
    pending["accumulator"] = {}
    if method == "published_pure_transport":state["archived_pure_representatives_consumed"] += 1
    else:state["new_original_projections_mapped"] += 1


def map_one_step(ctx,args,budget):
    state,inputs,mapper = ctx["state"],ctx["original"],ctx["mapper"]
    pending = state["pending"];index=pending["column"]
    if pending["mode_index"]==len(PROJECTIONS):
        joint = {}
        for mode in PROJECTIONS:
            value = priority.decode_rows(mapper,pending["projections"][mode])
            for (local,word),coefficient in value.terms.items():
                key = (mode,local,word)
                if key not in state["row_index"]:
                    if len(state["row_keys"])>=args.max_terms:
                        raise raw.Limit("shared exact word-row dictionary ceiling")
                    state["row_index"][key]=len(state["row_keys"])
                    state["row_keys"].append(key)
                joint[state["row_index"][key]]=coefficient
        denominator=1
        for value in joint.values():denominator=lcm(denominator,value.denominator)
        vector={row:int(value*denominator) for row,value in joint.items()}
        vector,combination=raw.normalize_integer_pair(vector,{index:denominator})
        budget.check(vector.values());budget.check(combination.values())
        record={"column":index,"original147_index":inputs.columns[index]["original147_index"],
            "projections":pending["projections"],"conversions":pending["conversions"]}
        if len(state["columns"])!=index:
            raise AssertionError("a fully mapped original column must be stored once")
        state["columns"].append(record)
        pending.update(stage="eliminate",vector=vector,combination=combination)
        for key in ("projections","conversions","accumulator","mode_index","term_cursor"):
            pending.pop(key,None)
        return
    mode=PROJECTIONS[pending["mode_index"]]
    column=inputs.columns[index]
    wanted=column["binding"][str(mode)]["original_sha256"]
    if mode==-4 and wanted in ctx["archives"]:
        archive=ctx["archives"][wanted]
        value=priority.embed_pure_rows(mapper,archive["word_rows"])
        source={k:archive[k] for k in ("source","archived_original_root","original_sha256",
                                     "word_summary","original_binding")}
        source["published_certificate"]=PURE["artifact"] if archive["source"]!="R157_D0" else D0["artifact"]
        finish_projection(ctx,mode,priority.rows(value),"published_pure_transport",source)
        return
    source_rows=column["roots"][mode]
    cursor=pending["term_cursor"]
    if cursor==len(source_rows):
        finish_projection(ctx,mode,word_rows(pending["accumulator"]),
            "new_R178_fixed_color_map",{"map":FROZEN["priority"],"color_order":list(priority.ORDER),
            "theorem":"R178","cycle_fallbacks":0})
        return
    key,n,d=source_rows[cursor]
    local=inputs.to_ring_monomial(raw.monomial(key,len(inputs.atom_keys)))
    value=mapper.monomial(local)
    accumulated=add_scaled(pending["accumulator"],value.terms,F(n,d))
    if len(accumulated)>args.max_terms:
        raise raw.Limit("current new original projection word term ceiling")
    budget.check(accumulated.values())
    pending["accumulator"]=accumulated
    pending["term_cursor"]=cursor+1
    state["mapping_term_steps"]+=1


def begin_transport_verification(pending):
    _,combination=raw.normalize_integer_pair({},pending["combination"])
    pending.update(stage="verify_transports",combination=combination,vector={},
        verify_cursor=0,original_accumulator={mode:{} for mode in PROJECTIONS},
        representative_accumulator={mode:{} for mode in PROJECTIONS},
        conversion_support=[],summed_original_terms={mode:0 for mode in PROJECTIONS})


def verify_conversion(ctx,index,mode):
    """Reload a stored conversion independently of the elimination row IDs."""
    state,inputs,mapper=ctx["state"],ctx["original"],ctx["mapper"]
    record=state["columns"][index]
    binding=record["conversions"][mode]
    payload=record["projections"][mode]
    if (record["column"]!=index
        or record["original147_index"]!=inputs.columns[index]["original147_index"]
        or binding!=inputs.bind_conversion(index,mode,payload,binding["conversion_method"],
                                           binding["conversion_source"])):
        raise AssertionError("column transport does not bind this actual original and word payload")
    value=priority.decode_rows(mapper,payload)
    if binding["conversion_method"]=="published_pure_transport":
        if mode!=-4:raise AssertionError("no mixed representative is silently treated as archived pure")
        archive=ctx["archives"].get(binding["original_mode_sha256"])
        if archive is None:
            raise AssertionError("original pure transport is not in the bound published archive")
        expected=priority.embed_pure_rows(mapper,archive["word_rows"])
        if value.terms!=expected.terms:
            raise AssertionError("stored reused pure words differ from the source-bound old conversion")
    elif binding["conversion_method"]=="new_R178_fixed_color_map":
        if (binding["conversion_source"].get("map")!=FROZEN["priority"]
            or binding["conversion_source"].get("color_order")!=list(priority.ORDER)
            or binding["conversion_source"].get("cycle_fallbacks")!=0):
            raise AssertionError("new original conversion uses another rule or a cycle fallback")
    else:
        raise AssertionError("unknown original-to-word transport")
    return value,binding


def verify_one_step(ctx,budget):
    state,inputs=ctx["state"],ctx["original"]
    pending=state["pending"]
    support=sorted(pending["combination"].items());cursor=pending["verify_cursor"]
    if cursor==len(support):
        if any(pending["representative_accumulator"][mode] for mode in PROJECTIONS):
            raise AssertionError("a proposed Psi kernel failed independent original-transport summation")
        pending["stage"]="commit_relation"
        return
    index,amount=support[cursor]
    originals={mode:dict(pending["original_accumulator"][mode]) for mode in PROJECTIONS}
    representatives={mode:dict(pending["representative_accumulator"][mode]) for mode in PROJECTIONS}
    counts=dict(pending["summed_original_terms"])
    conversions=[]
    for mode in PROJECTIONS:
        value,binding=verify_conversion(ctx,index,mode)
        # Preserve the complete original mode -2 polynomial, not only its
        # balanced selection.  The certified zero transport is (pure,balanced).
        name=inputs.columns[index]["binding"][str(mode)]["original_root"]
        original=inputs.head["roots"][name]
        for key,n,d in original:
            key=raw.monomial(key,len(inputs.atom_keys))
            updated=originals[mode].get(key,F(0))+amount*F(n,d)
            if updated:originals[mode][key]=updated
            else:originals[mode].pop(key,None)
        counts[mode]+=len(original)
        representatives[mode]=add_scaled(representatives[mode],value.terms,F(amount))
        if len(representatives[mode])>ctx["args"].max_terms:
            raise raw.Limit("fresh two-root transport-sum term ceiling")
        budget.check(originals[mode].values());budget.check(representatives[mode].values())
        conversions.append({"column":index,"mode":mode,
            "conversion_sha256":raw.sha(raw.canonical(binding)),
            "word_payload_sha256":raw.sha(raw.canonical(state["columns"][index]["projections"][mode]))})
    pending["original_accumulator"]=originals
    pending["representative_accumulator"]=representatives
    pending["summed_original_terms"]=counts
    pending["conversion_support"].extend(conversions)
    pending["verify_cursor"]=cursor+1
    state["fresh_original_column_sums"]+=1
    state["fresh_transport_column_sums"]+=1


def commit_relation(ctx,budget):
    state,inputs=ctx["state"],ctx["original"];pending=state["pending"]
    index=pending["column"];coefficients=pending["combination"]
    if max(coefficients)!=index or coefficients[index]<=0:
        raise AssertionError("a new relation lacks its triangular original-column diagonal")
    if index<40 and len(inputs.columns)==77:
        raise AssertionError("a certified original relation contradicts the old true R40 independence")
    lifted={inputs.columns[i]["original147_index"]:F(c) for i,c in coefficients.items()}
    normal={i-40:c for i,c in lifted.items() if i>=40}
    form=raw.project_normal(normal,ctx["transform"])
    normal_value=sum((value*ctx["point_nu"][i] for i,value in normal.items()),F(0))
    free_value=raw.evaluate_form(form,ctx["point_y"])
    if normal_value!=free_value:
        raise AssertionError("new original equality evaluates differently in the same published 107/23 point")
    next_small=deepcopy(state["small_basis"])
    relation_index=len(state["relations"])
    remainder,trace=raw.reduce_small(form,next_small,budget,
                                     insert="R178_original_relation_%d"%relation_index)
    original_differences={}
    for mode in PROJECTIONS:
        payload=original_rows(pending["original_accumulator"][mode])
        selected=[]
        for key,n,d in payload:
            degree=tuple(sum(inputs.atom_degrees[a][c] for a in key[1]) for c in (0,1))
            if mode==-4 or degree==(2,2):selected.append([key,n,d])
        original_differences[str(mode)]={
            "original_rows":payload,"original_sha256":inputs.root_hash(payload),
            "original_terms":len(payload),"faithful_projection_rows":selected,
            "faithful_projection_original_sha256":inputs.root_hash(selected),
            "summed_original_term_rows":pending["summed_original_terms"][mode],
            "independently_summed_word_rows":[],
            "word_sum_sha256":raw.sha(raw.canonical([])),
            "original_function_zero_proved_by_bound_transport_sum":True}
    record={"relation_index":relation_index,"dependent_basis_column":index,
        "dependent_original147_column":inputs.columns[index]["original147_index"],
        "basis77_coefficients":raw.serial_integer_row(coefficients),
        "dense77_coefficients":[str(coefficients.get(i,0)) for i in range(len(inputs.columns))],
        "original147_coefficients":raw.serial_fraction_row(lifted),
        "dense147_coefficients":[str(lifted.get(i,0)) for i in range(147)],
        "normal_coordinate_equality":raw.serial_fraction_row(normal),
        "old_free_coordinate_equality":raw.serial_fraction_row(form),
        "residual_after_R168_R174_and_prior_new_relations":raw.serial_fraction_row(remainder),
        "known_row_reduction":trace,"new_equality_modulo_known_rows":bool(remainder),
        "prescribed_point_exact_value":str(free_value),
        "prescribed_point_violates_this_true_original_equality":bool(free_value),
        "original_differences":original_differences,
        "conversion_support":pending["conversion_support"],
        "proof_method":"fresh complete original differences + bound per-column transport identities + independent two-root word sum",
        "all_two_faithful_root_sums_exactly_zero":True,
        "complete_canonical_original_identity_proved":True,
        "complete_canonical_faithfulness_theorem":"R159",
        "Psi_is_not_assumed_equal_to_new_Phi_on_raw_inputs":True,
        "fresh_Phi_reduction_of_original_difference_required_or_performed":False,
        "old_pure_targets_or_literal_dependencies_recomputed":False}
    state["relations"].append(record);state["small_basis"]=next_small
    state["new_small_equalities"]+=bool(remainder)
    state["cursor"]+=1;state["pending"]=None
    return record


def advance(ctx,args,budget):
    state=ctx["state"]
    if state["pending"] is None:start_column(state)
    pending=state["pending"]
    if pending["stage"]=="map":
        map_one_step(ctx,args,budget);return None
    if pending["stage"]=="eliminate":
        if not pending["vector"]:
            begin_transport_verification(pending);return None
        pivot=min(pending["vector"])
        if pivot not in state["basis"]:
            state["basis"][pivot]={"vector":pending["vector"],
                "combination":pending["combination"],"source_column":pending["column"]}
            state["independent_columns"].append(pending["column"])
            state["cursor"]+=1;state["pending"]=None
            return None
        vector,combination=raw.exact_reduce_step(pending["vector"],pending["combination"],
                                               state["basis"],budget)
        pending["vector"]=vector;pending["combination"]=combination
        state["elimination_steps"]+=1
        return None
    if pending["stage"]=="verify_transports":
        verify_one_step(ctx,budget);return None
    if pending["stage"]=="commit_relation":
        return commit_relation(ctx,budget)
    raise AssertionError("unknown new shared-map phase")


def compact_cache(mapper,max_bytes):
    temporary=priority.PriorityWords(mapper.ring,max_calls=mapper.max_calls,
        max_terms=mapper.max_terms,max_shuffle_entries=mapper.max_shuffle_entries,
        max_cache_entries=mapper.max_cache_entries,color_order=mapper.color_order)
    temporary.atom_cache=mapper.atom_cache
    temporary.stats=dict(mapper.stats)
    temporary.run_primitive_calls=mapper.run_primitive_calls
    payload=temporary.snapshot(max_bytes=max_bytes)
    payload["compact_omitted_derived_monomial_primitive_shuffle_caches"]=True
    payload["all_completed_original_atom_values_preserved"]=True
    payload["unfinished_atomic_call_may_be_replayed"]=True
    return payload


def serialize_pending(pending):
    if pending is None:return None
    result={k:v for k,v in pending.items() if k not in (
        "vector","combination","accumulator","original_accumulator","representative_accumulator")}
    if "vector" in pending:
        result["vector"]=raw.serial_integer_row(pending["vector"])
        result["vector_sha256"]=raw.vector_hash(pending["vector"])
    if "combination" in pending:result["combination"]=raw.serial_integer_row(pending["combination"])
    if "accumulator" in pending:result["accumulator"]=word_rows(pending["accumulator"])
    if "original_accumulator" in pending:
        result["original_accumulator"]={str(mode):original_rows(value)
                                       for mode,value in pending["original_accumulator"].items()}
    if "representative_accumulator" in pending:
        result["representative_accumulator"]={str(mode):word_rows(value)
                                             for mode,value in pending["representative_accumulator"].items()}
    return result


def serialized_state(ctx,report,compact=False):
    state=ctx["state"]
    basis=[]
    for pivot,item in sorted(state["basis"].items()):
        row={"pivot":pivot,"combination":raw.serial_integer_row(item["combination"]),
            "source_column":item["source_column"],"vector_sha256":raw.vector_hash(item["vector"]),
            "vector_terms":len(item["vector"])}
        if not compact:row["vector"]=raw.serial_integer_row(item["vector"])
        basis.append(row)
    pending=serialize_pending(state["pending"])
    if compact and pending is not None and "vector" in pending:pending.pop("vector")
    return {"schema":SCHEMA+"-state","source_hashes":report["source_hashes"],
        "input_binding_sha256":ctx["binding_sha"],"color_order":list(priority.ORDER),
        "github_repository":REPOSITORY,"github_run_id":report.get("github_run_id"),
        "github_sha":report.get("github_sha"),
        "original147_basis_indices":[row["original147_index"] for row in ctx["original"].columns],
        "cursor":state["cursor"],"columns":state["columns"],"relations":state["relations"],
        "row_keys":state["row_keys"],"basis":basis,"pending":pending,
        "independent_columns":state["independent_columns"],
        "small_basis":[{"pivot":pivot,**{k:(raw.serial_fraction_row(v) if k=="row" else v)
                       for k,v in item.items()}} for pivot,item in sorted(state["small_basis"].items())],
        "counters":{key:state[key] for key in ("new_small_equalities","elimination_steps",
            "fresh_original_column_sums","fresh_transport_column_sums","mapping_term_steps",
            "archived_pure_representatives_consumed","new_original_projections_mapped")},
        "word_map_cache":compact_cache(ctx["mapper"],ctx["args"].max_raw_bytes) if compact
            else ctx["mapper"].snapshot(max_bytes=ctx["args"].max_raw_bytes),
        "compact_completed_vectors_restored_by_exact_saved_combination":compact,
        "completed_original_column_normalizations_or_pivots_replayed":False,
        "an_unfinished_atomic_call_is_not_claimed_as_a_completed_conversion":True}


def read_joint_key(raw_key):
    mode,local,word=raw_key
    if mode not in PROJECTIONS:raise ValueError("unknown faithful projection tag")
    return mode,priority.local_key(local),priority.word_key(word)


def rehydrate_column(row):
    result=dict(row)
    result["projections"]={int(mode):value for mode,value in row["projections"].items()}
    result["conversions"]={int(mode):value for mode,value in row["conversions"].items()}
    if set(result["projections"])!=set(PROJECTIONS) or set(result["conversions"])!=set(PROJECTIONS):
        raise ValueError("saved completed column needs both faithful projections")
    return result


def saved_combination_vector(state,combination,mapper,budget):
    result={}
    for index,amount in sorted(combination.items()):
        if not 0<=index<len(state["columns"]):raise ValueError("saved vector uses an unmapped original")
        for mode,payload in state["columns"][index]["projections"].items():
            value=priority.decode_rows(mapper,payload)
            for (local,word),coefficient in value.terms.items():
                row=state["row_index"][(mode,local,word)]
                new=result.get(row,F(0))+amount*coefficient
                if new:result[row]=new
                else:result.pop(row,None)
        budget.check(result.values())
    if any(value.denominator!=1 for value in result.values()):
        raise ValueError("saved integer reduction state did not reconstruct integrally")
    return {key:int(value) for key,value in result.items()}


def restore_state(data,ctx,args,report,budget):
    if (data.get("schema")!=SCHEMA+"-state"
        or data.get("source_hashes")!=report["source_hashes"]
        or data.get("input_binding_sha256")!=ctx["binding_sha"]
        or data.get("color_order")!=list(priority.ORDER)
        or data.get("original147_basis_indices")!=[row["original147_index"] for row in ctx["original"].columns]):
        raise ValueError("the exact source, shared map, original inputs, or prescribed point changed")
    mapper=ctx["mapper"]
    mapper.restore(data["word_map_cache"])
    # restore resets only the separate per-run counter.  Cumulative statistics
    # stay unchanged, and the declared per-run cap is not silently enlarged.
    cursor=data["cursor"]
    count=len(ctx["original"].columns)
    if type(cursor) is not int or not 0<=cursor<=count:raise ValueError("invalid saved column cursor")
    state={"cursor":cursor,"pending":None,"columns":[rehydrate_column(row) for row in data["columns"]],
        "relations":data["relations"],"row_keys":[read_joint_key(row) for row in data["row_keys"]],
        "basis":{},"small_basis":{},"independent_columns":data["independent_columns"],**data["counters"]}
    state["row_index"]={key:i for i,key in enumerate(state["row_keys"])}
    if len(state["row_index"])!=len(state["row_keys"]):raise ValueError("duplicate saved word rows")
    if [row["column"] for row in state["columns"]]!=list(range(len(state["columns"]))):
        raise ValueError("completed conversion prefix is not ordered")
    ctx["state"]=state
    for column in state["columns"]:
        for mode in PROJECTIONS:verify_conversion(ctx,column["column"],mode)
    restored_from_combinations=0
    for item in data["basis"]:
        combination=raw.read_integer_row(item["combination"],count)
        if not combination or max(combination)>=cursor:
            raise ValueError("a completed pivot depends on a future column")
        if "vector" in item:vector=raw.read_integer_row(item["vector"],len(state["row_keys"]))
        else:
            vector=saved_combination_vector(state,combination,mapper,budget)
            restored_from_combinations+=1
        pivot=item["pivot"]
        if (not vector or min(vector)!=pivot or vector[pivot]<=0 or pivot in state["basis"]
            or len(vector)!=item["vector_terms"] or raw.vector_hash(vector)!=item["vector_sha256"]):
            raise ValueError("saved exact pivot integrity changed")
        state["basis"][pivot]={"vector":vector,"combination":combination,
                               "source_column":item["source_column"]}
    if len(state["basis"])+len(state["relations"])!=cursor:
        raise ValueError("saved completed basis/kernel counts do not cover the prefix")
    for item in data["small_basis"]:
        row=raw.read_fraction_row(item["row"],23);pivot=item["pivot"]
        if not row or min(row)!=pivot or row[pivot]!=1 or pivot in state["small_basis"]:
            raise ValueError("invalid saved small equality basis")
        state["small_basis"][pivot]={k:v for k,v in item.items() if k not in ("pivot","row")}
        state["small_basis"][pivot]["row"]=row
    pending=data.get("pending")
    if pending is not None:
        pending=dict(pending)
        if pending["column"]!=cursor or cursor==count:
            raise ValueError("saved active column does not follow the completed prefix")
        if "combination" in pending:
            pending["combination"]=raw.read_integer_row(pending["combination"],count)
            if not pending["combination"] or max(pending["combination"])!=cursor:
                raise ValueError("saved active column lacks its triangular certificate")
            if "vector" in pending:
                pending["vector"]=raw.read_integer_row(pending["vector"],len(state["row_keys"]))
            else:
                pending["vector"]=saved_combination_vector(state,pending["combination"],mapper,budget)
                restored_from_combinations+=1
            if raw.vector_hash(pending["vector"])!=pending.pop("vector_sha256"):
                raise ValueError("saved pending exact vector changed")
        if "accumulator" in pending:
            pending["accumulator"]=priority.decode_rows(mapper,pending["accumulator"]).terms
        for key in ("projections","conversions","summed_original_terms"):
            if key in pending:pending[key]={int(mode):value for mode,value in pending[key].items()}
        if "original_accumulator" in pending:
            pending["original_accumulator"]={int(mode):original_terms(value,len(ctx["original"].atom_keys))
                for mode,value in pending["original_accumulator"].items()}
        if "representative_accumulator" in pending:
            pending["representative_accumulator"]={int(mode):priority.decode_rows(mapper,value).terms
                for mode,value in pending["representative_accumulator"].items()}
        state["pending"]=pending
    mapped=cursor+int(pending is not None and pending["stage"]!="map")
    if len(state["columns"])!=mapped:
        raise ValueError("mapped-column prefix does not match the active stage")
    return {"restored_completed_columns":cursor,"restored_mapped_columns":len(state["columns"]),
        "restored_active_stage":None if pending is None else pending["stage"],
        "restored_completed_original_atom_values":len(mapper.atom_cache),
        "vectors_materialized_from_saved_exact_combinations":restored_from_combinations,
        "completed_original_column_normalizations_replayed":0,"completed_elimination_pivots_replayed":0,
        "derived_cache_compaction":bool(data["word_map_cache"].get(
            "compact_omitted_derived_monomial_primitive_shuffle_caches")),
        "an_unfinished_atomic_call_may_be_replayed":True}


def save_state(ctx,args,report,available=None):
    available=min(args.max_state_bytes,available if available is not None
                  else args.max_total_bytes-args.max_main_bytes)
    if available<=0:raise raw.Limit("no bytes reserved for a complete resumable state")
    last=None
    for compact in (False,True):
        try:
            payload=serialized_state(ctx,report,compact)
            packed,metadata=raw.gzip_payload(payload,available,args.max_raw_bytes)
            raw.atomic_write(args.output.with_name(STATE_NAME),packed)
            pending=ctx["state"]["pending"]
            metadata.update(filename=STATE_NAME,completed_columns=ctx["state"]["cursor"],
                mapped_columns=len(ctx["state"]["columns"]),
                active_stage=None if pending is None else pending["stage"],
                completed_elimination_steps=ctx["state"]["elimination_steps"],
                exact_progress_sha256=progress_digest(ctx),
                compact=compact,all_completed_original_atom_values_preserved=True,
                completed_original_columns_and_pivots_need_not_be_repeated=True)
            ctx["state_metadata"]=metadata
            return metadata
        except (raw.Limit,exact.formal.CompilationBudgetExceeded) as error:last=error
    raise last


def progress_digest(ctx):
    state=ctx["state"];pending=state["pending"];mapper=ctx["mapper"]
    progress={"cursor":state["cursor"],"columns":len(state["columns"]),
        "relations":len(state["relations"]),"basis":len(state["basis"]),
        "word_rows":len(state["row_keys"]),
        "counters":{key:state[key] for key in ("elimination_steps","mapping_term_steps",
            "fresh_original_column_sums","fresh_transport_column_sums")},
        "active":None if pending is None else {key:pending.get(key) for key in
            ("column","stage","mode_index","term_cursor","verify_cursor")},
        "map_statistics":mapper.stats,
        "completed_cache_counts":[len(mapper.atom_cache),len(mapper.monomial_cache),
                                  len(mapper.primitive_cache),len(mapper.shuffle_cache)]}
    return raw.sha(raw.canonical(progress))


def certificate_data(ctx,report):
    state=ctx["state"]
    return {"schema":SCHEMA+"-certificate","source_hashes":report["source_hashes"],
        "github_repository":REPOSITORY,"github_run_id":report.get("github_run_id"),
        "github_sha":report.get("github_sha"),"target_weight":-2,"inputs":ctx["binding"],
        "input_binding_sha256":ctx["binding_sha"],"anchor":ctx["original"].head["anchor"],
        "profile_atoms":ctx["original"].profile_atoms,
        "original147_basis_indices":list(EXPECTED_BASIS),
        "completed_column_prefix":state["cursor"],
        "completed_original_to_word_conversions":state["columns"],
        "original_conversion_metadata":[{k:v for k,v in row.items() if k!="roots"}
                                        for row in ctx["original"].columns],
        "exact_original_relations":state["relations"],
        "shared_representative_matrix_basis_columns":state["independent_columns"],
        "shared_representative_matrix_rank_on_completed_prefix":len(state["basis"]),
        "new_equalities_for_old_free_coordinates":[row["relation_index"] for row in state["relations"]
                                                   if row["new_equality_modulo_known_rows"]],
        "prescribed_point_107_values":list(map(str,ctx["point_nu"])),
        "prescribed_point_23_values":list(map(str,ctx["point_y"])),
        "all_77_columns_processed":state["cursor"]==77,
        "Phi_and_Psi_identified":False,
        "nonzero_word_independence_or_true_head_dimension_claimed":False,
        "complete_true_functional_kernel_claimed":False,
        "all_certified_relations_have_full_original_differences_and_two_zero_transport_sums":True,
        "old_pure40_31_literal70_or_profile_evaluation_repeated":False}


def save_outputs(ctx,args,report):
    cert=certificate_data(ctx,report)
    packed,metadata=raw.gzip_payload(cert,args.max_certificate_bytes,args.max_raw_bytes)
    metadata.update(filename=CERT_NAME,
        content_scope="new bound column conversions and complete original two-projection relation certificates",
        completed_columns=ctx["state"]["cursor"],certified_relations=len(ctx["state"]["relations"]))
    available=args.max_total_bytes-len(packed)-args.max_main_bytes
    if available<=0:raise raw.Limit("combined publication byte ceiling")
    save_state(ctx,args,report,available)
    raw.atomic_write(args.output.with_name(CERT_NAME),packed)
    ctx["certificate_metadata"]=metadata


def load_resume(args,ctx,report,budget):
    directory=args.resume_dir
    main_path=directory/MAIN_NAME;receipt_path=directory/"receipt.json"
    mraw=main_path.read_bytes();rraw=receipt_path.read_bytes()
    if (len(mraw)>=100000 or len(rraw)>=100000
        or raw.sha(mraw)!=args.resume_main_sha256
        or raw.sha(rraw)!=args.resume_publication_sha256):
        raise ValueError("resume main/receipt exact hashes changed")
    previous=json.loads(mraw);publication=json.loads(rraw)
    metadata=previous.get("resumable_shared_word_state",{})
    if (previous.get("schema")!=SCHEMA or previous.get("source_hashes")!=report["source_hashes"]
        or previous.get("input_binding_sha256")!=ctx["binding_sha"]
        or metadata.get("filename")!=STATE_NAME
        or publication.get("schema")!="visible-new-mechanism-actions-v1"
        or publication.get("repository")!=REPOSITORY or publication.get("lane")!=LANE
        or str(publication.get("run_id"))!=str(previous.get("github_run_id"))
        or publication.get("source_commit")!=previous.get("github_sha")):
        raise ValueError("resume publication is not this same new exact computation")
    outputs=raw.publication_outputs(publication)
    for name,expected in ((MAIN_NAME,{"bytes":len(mraw),"sha256":raw.sha(mraw),
                                     "raw_bytes":len(mraw),"raw_sha256":raw.sha(mraw)}),
                          (STATE_NAME,{"bytes":metadata["stored_bytes"],"sha256":metadata["stored_sha256"],
                            "raw_bytes":metadata["raw_bytes"],"raw_sha256":metadata["raw_sha256"]})):
        if any(outputs.get(name,{}).get(k)!=v for k,v in expected.items()):
            raise ValueError("resume published bytes or raw/stored hashes changed")
    for info in (report["source_hashes"]["driver"],*FROZEN.values()):
        matches=[value for key,value in publication.get("source_files",{}).items()
                 if Path(key).name==info["filename"]]
        if len(matches)!=1 or any(matches[0].get(k)!=info[k] for k in ("bytes","sha256")):
            raise ValueError("resume publication does not bind every frozen implementation source")
    data=raw.checked_gzip(directory/STATE_NAME,metadata,args.max_raw_bytes)
    return restore_state(data,ctx,args,report,budget)


def summarize(ctx,report):
    state=ctx["state"];pending=state["pending"]
    violations=[{"relation_index":row["relation_index"],
                 "exact_value":row["prescribed_point_exact_value"]}
                for row in state["relations"]
                if row["prescribed_point_violates_this_true_original_equality"]]
    report["shared_word_progress"]={
        "expected_literal_basis_columns":77,"completed_columns":state["cursor"],
        "completed_column_conversions":len(state["columns"]),
        "active_stage":None if pending is None else pending["stage"],
        "active_raw_term_cursor":None if pending is None else pending.get("term_cursor"),
        "representative_rank_on_completed_prefix":len(state["basis"]),
        "certified_new_original_relations":len(state["relations"]),
        "new_equalities_modulo_old_B_R168_R174":state["new_small_equalities"],
        "all_77_columns_processed":state["cursor"]==77,
        "complete_true_function_kernel_or_true_rank_claimed":False,
        "elimination_steps":state["elimination_steps"],"mapping_term_steps":state["mapping_term_steps"],
        "fresh_original_column_sums":state["fresh_original_column_sums"],
        "fresh_transport_column_sums":state["fresh_transport_column_sums"],
        "archived_pure_representatives_consumed":state["archived_pure_representatives_consumed"],
        "new_original_projections_mapped":state["new_original_projections_mapped"]}
    report["prescribed_point_diagnostic"]={
        "source_run":POINT["run"],"cut_by_a_certified_complete_original_identity":bool(violations),
        "violations":violations,"passes_all_certified_new_relations":not violations,
        "passing_does_not_prove_functional_well_definedness":True,
        "old_86_rows_or_scalar_path_certificates_retested":False}
    report["fixed_color_map_statistics"]=dict(ctx["mapper"].stats)
    report["fixed_color_current_run_call_budget"]={
        "started_primitive_calls":ctx["mapper"].run_primitive_calls,
        "declared_additional_call_ceiling":ctx["mapper"].max_calls,
        "cumulative_calls_are_separate_from_this_ceiling":True,
        "cache_entries_terms_and_bytes_remain_global_hard_limits":True}
    report["new_original_relation_certificate"]=ctx.get("certificate_metadata")
    report["resumable_shared_word_state"]=ctx.get("state_metadata")
    report["latest_exact_progress_has_a_saved_state"]=(
        ctx.get("state_metadata",{}).get("exact_progress_sha256")==progress_digest(ctx))


def actual(args,report,ctx,budget):
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise RuntimeError("real original/profile computation is only authorized in this public repository Actions")
    remaining=max(0.001,args.max_seconds-(time.monotonic()-budget.started))
    limits=exact.Limits(seconds=remaining,nodes=args.max_nodes,atoms=args.max_atoms,
        terms=args.max_terms,rewrites=args.max_IBP_calls,memory_mib=args.memory_mib,
        rational_bits=args.integer_bits)
    ring=colored.ColoredRing(limits)
    original,archives,transform,point_y,point_nu,known,binding=load_inputs(args,report,budget,ring)
    ctx.update(original=original,archives=archives,transform=transform,point_y=point_y,
        point_nu=point_nu,binding=binding,binding_sha=raw.sha(raw.canonical(binding)),
        mapper=new_mapper(ring,args),args=args)
    report["input_binding_sha256"]=ctx["binding_sha"]
    if args.resume_dir:report["resume"]=load_resume(args,ctx,report,budget)
    else:ctx["state"]=fresh_state(known,budget)
    state=ctx["state"]
    save_state(ctx,args,report)
    report["phase"]="new_shared_fixed_color_original_transports_and_relations"
    checkpoint_cursor=state["cursor"]
    while state["cursor"]<77:
        if (not args.finish_all_77 and any(row["prescribed_point_violates_this_true_original_equality"]
                                         for row in state["relations"])):
            break
        budget.check()
        relation=advance(ctx,args,budget)
        if relation is not None:
            print(json.dumps({"phase":"new_complete_original_relation_certified",
                "relation":relation["relation_index"],"completed_columns":state["cursor"],
                "new_equality":relation["new_equality_modulo_known_rows"],
                "prescribed_point_value":relation["prescribed_point_exact_value"]}),flush=True)
        if relation is not None or state["cursor"]>=checkpoint_cursor+args.checkpoint_every:
            save_state(ctx,args,report);checkpoint_cursor=state["cursor"]
    cut=any(row["prescribed_point_violates_this_true_original_equality"] for row in state["relations"])
    report.update(completion="complete",
        phase="prescribed_point_cut_by_complete_original_identity" if cut else "all_77_shared_representatives_processed",
        outcome="one_true_functional_relation_cuts_the_prescribed_point" if cut else
                "no_cut_in_the_complete_sound_shared_representative_kernel",
        all_77_columns_processed=state["cursor"]==77,
        prescribed_point_functional_well_definedness_proved=False,
        original_function_kernel_complete_proved=False)


def artificial_input(ring,expressions):
    """Small invented originals, with the same portable-projection interface."""
    profile_atoms=json.loads(json.dumps(ring.p.atoms))
    item=object.__new__(OriginalInputs)
    item.ring=ring;item.profile_atoms=profile_atoms
    item.hashes=raw.portable_atom_hashes(profile_atoms)
    item.atom_keys=list(range(len(profile_atoms)))
    item.atom_degrees=[];item.atom_weights=[]
    for node in profile_atoms:
        if node[0]=="jet":
            item.atom_degrees.append((int(node[1]=="q"),int(node[1]=="qbar")))
            item.atom_weights.append(-node[2])
        else:
            power,atoms=node[1]
            item.atom_degrees.append(tuple(sum(item.atom_degrees[a][c] for a in atoms) for c in (0,1)))
            item.atom_weights.append(power+sum(item.atom_weights[a] for a in atoms)+1)
    item.head={"profile_atoms":profile_atoms,"roots":{},"anchor":"artificial common right collar"}
    item.columns=[]
    for index,expression in enumerate(expressions):
        projection={};binding={}
        for mode,value in ((-4,ring.number(0)),(-2,expression)):
            name="artificial_%d_%d"%(index,mode);payload=original_rows(value.terms)
            item.head["roots"][name]=payload
            projection[mode]=payload
            binding[str(mode)]={"original_root":name,"original_sha256":ring.digest(value),
                "stored_rows_sha256":raw.sha(raw.canonical(payload)),"stored_terms":len(payload)}
        item.columns.append({"index":index,"original147_index":0 if index==0 else 39+index,
            "normal_index":None if index==0 else index-1,
            "kind":"R" if index==0 else "normal","roots":projection,
            "source_metadata":{"artificial_only":True},"binding":binding})
    return item


def artificial_context(args):
    limits=exact.Limits(seconds=30,memory_mib=512,terms=4000,rewrites=20000)
    ring=colored.ColoredRing(limits)
    q,qb=ring.color("q"),ring.color("qbar")
    first=(q*q.D()*qb*qb.D()).I()
    second=q*q.D()*qb*qb/2-((q.D()*q.D()+q*q.D().D())*qb*qb).I()/2
    original=artificial_input(ring,[first,second])
    transform=[{} for _ in range(107)];transform[0]={0:F(1)}
    point_y=[F(1)]+[F(0)]*22;point_nu=[F(1)]+[F(0)]*106
    return {"original":original,"archives":{},"transform":transform,
        "point_y":point_y,"point_nu":point_nu,"binding":{"artificial":True},
        "binding_sha":"artificial_no_research_input","mapper":new_mapper(ring,args),
        "state":fresh_state([],raw.Budget(30,512)),"args":args}


def artificial_checks(include_map_resume=True):
    args=argparse.Namespace(max_IBP_calls=20000,max_terms=4000,max_shuffle_entries=4000,
        max_cache_entries=20000,max_raw_bytes=4000000)
    budget=raw.Budget(30,512,2048)
    ctx=artificial_context(args);checks={}
    while ctx["state"]["cursor"]<2:advance(ctx,args,budget)
    relation=ctx["state"]["relations"][0]
    assert relation["basis77_coefficients"]==[[0,"-1"],[1,"1"]]
    assert relation["complete_canonical_original_identity_proved"]
    assert relation["original_differences"]["-2"]["original_terms"]>0
    assert relation["original_differences"]["-2"]["independently_summed_word_rows"]==[]
    assert relation["prescribed_point_exact_value"]=="1"
    checks["new_original_function_relation_has_nonzero_raw_difference_and_two_exact_zero_transport_sums"]=True
    assert relation["normal_coordinate_equality"]==[[0,"1"]]
    assert relation["old_free_coordinate_equality"]==[[0,"1"]]
    checks["same_original_relation_is_projected_through_archived_B_and_evaluated_at_one_named_point"]=True
    record=ctx["state"]["columns"][1]
    original=record["conversions"][-2]["word_rows_sha256"]
    record["conversions"][-2]["word_rows_sha256"]="0"*64
    failed=False
    try:verify_conversion(ctx,1,-2)
    except AssertionError:failed=True
    assert failed
    record["conversions"][-2]["word_rows_sha256"]=original
    checks["forged_word_transport_is_rejected_independently_of_the_elimination_vector"]=True
    # Save an unfinished source-monomial sum and an unfinished original proof.
    report={"source_hashes":{"driver":{"artificial":True}},"github_run_id":"artificial","github_sha":"artificial"}
    for wanted in ("map","verify_transports"):
        partial=artificial_context(args)
        if wanted=="map":
            start_column(partial["state"])
            advance(partial,args,budget)
            advance(partial,args,budget)
        else:
            while not (partial["state"]["pending"] is not None
                       and partial["state"]["pending"]["stage"]=="verify_transports"):
                advance(partial,args,budget)
            verify_one_step(partial,budget)
        for compact in (False,True):
            snapshot=json.loads(raw.canonical(serialized_state(partial,report,compact)))
            resumed=artificial_context(args)
            info=restore_state(snapshot,resumed,args,report,budget)
            assert info["completed_original_column_normalizations_replayed"]==0
            assert info["completed_elimination_pivots_replayed"]==0
            while resumed["state"]["cursor"]<2:advance(resumed,args,budget)
            assert resumed["state"]["relations"]==ctx["state"]["relations"]
    checks["full_and_compact_states_resume_mid_original_map_and_mid_transport_proof"]=True
    wrong=json.loads(raw.canonical(serialized_state(ctx,report)))
    failed=False
    changed=artificial_context(args);changed["binding_sha"]="different_original_or_candidate"
    try:restore_state(wrong,changed,args,report,budget)
    except ValueError:failed=True
    assert failed
    checks["resume_rejects_a_different_exact_original_input_or_prescribed_point"]=True
    assert priority.is_remainder_letter((0,(("q",2),("qbar",0))))
    assert not priority.is_remainder_letter((0,(("q",1),("qbar",1))))
    assert priority.is_remainder_letter((0,(("q",1),("q",1))))
    assert not priority.is_remainder_letter((0,(("q",1),)))
    checks["new_and_archived_dictionary_grammar_uses_the_same_fixed_color_remainder_test"]=True
    result={"all_passed":True,"artificial_only":True,"real_input_files_opened":False,
        "old_pure40_31_or_literal70_repeated":False,"checks":checks}
    if include_map_resume:result["new_mapper_continuation_checks"]=priority.artificial_resume_checks()
    return result


def binding_only_checks():
    """Only the newly observed old-manifest metadata contract, not old toys."""
    old={"schema":raw.FINITE["schema"]+"-certificate"}
    assert check_export_identity(old,raw.FINITE,"-certificate",True)==(
        "exact_published_main_receipt_and_artifact_hashes")
    for data,spec,allow in (
        (old,raw.FINITE,False),
        ({**old,"github_run_id":"different"},raw.FINITE,True),
        ({"schema":PURE["schema"]+"-original-expressions"},PURE,True)):
        failed=False
        try:check_export_identity(data,spec,"-certificate" if spec==raw.FINITE else "-original-expressions",allow)
        except ValueError:failed=True
        assert failed
    return {"all_passed":True,"artificial_only":True,"real_input_files_opened":False,
        "old_nine_or_ten_development_checks_repeated":False,
        "checks":{
            "exact_old_finite_export_identity_is_taken_from_its_already_strictly_bound_manifest":True,
            "missing_other_or_conflicting_embedded_identities_are_not_silently_relaxed":True}}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("head-dir","literal-dir","finite-dir","pure-dir","point-dir","resume-dir"):
        parser.add_argument("--"+name,type=Path)
    parser.add_argument("--d0-dir",dest="D0_dir",type=Path)
    parser.add_argument("--resume-main-sha256")
    parser.add_argument("--resume-publication-sha256")
    parser.add_argument("--finish-all-77",action="store_true")
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--toy-only",action="store_true")
    parser.add_argument("--binding-toy-only",action="store_true")
    parser.add_argument("--max-seconds",type=float,default=240)
    parser.add_argument("--memory-mib",type=int,default=1024)
    parser.add_argument("--integer-bits",type=int,default=8192)
    parser.add_argument("--max-nodes",type=int,default=500000)
    parser.add_argument("--max-atoms",type=int,default=60000)
    parser.add_argument("--max-terms",type=int,default=80000)
    parser.add_argument("--max-IBP-calls",type=int,default=250000)
    parser.add_argument("--max-cache-entries",type=int,default=250000)
    parser.add_argument("--max-shuffle-entries",type=int,default=100000)
    parser.add_argument("--checkpoint-every",type=int,default=4)
    parser.add_argument("--max-main-bytes",type=int,default=95000)
    parser.add_argument("--max-state-bytes",type=int,default=3200000)
    parser.add_argument("--max-certificate-bytes",type=int,default=3200000)
    parser.add_argument("--max-total-bytes",type=int,default=4800000)
    parser.add_argument("--max-raw-bytes",type=int,default=40000000)
    args=parser.parse_args()
    numerical=("max_seconds","memory_mib","integer_bits","max_nodes","max_atoms","max_terms",
        "max_IBP_calls","max_cache_entries","max_shuffle_entries","checkpoint_every","max_main_bytes",
        "max_state_bytes","max_certificate_bytes","max_total_bytes","max_raw_bytes")
    if any(getattr(args,key)<=0 for key in numerical):parser.error("all explicit budgets must be positive")
    if not 12000<=args.max_main_bytes<100000 or args.max_total_bytes>4800000:
        parser.error("main budget at least12000 and below100KB; complete publication at most4.8MB")
    if args.max_total_bytes<=args.max_main_bytes:
        parser.error("reserve publication bytes beyond the small main for an exact state")
    if args.toy_only and args.binding_toy_only:parser.error("choose one artificial entry point")
    if not (args.toy_only or args.binding_toy_only):
        if any(getattr(args,key) is None for key in (
            "head_dir","literal_dir","finite_dir","pure_dir","D0_dir","point_dir")):
            parser.error("all six exact published input directories are required")
        if args.output.name!=MAIN_NAME:parser.error("the actual output basename is fixed for continuation")
    if bool(args.resume_dir)!=(bool(args.resume_main_sha256) and bool(args.resume_publication_sha256)):
        parser.error("resume needs directory plus exact published main and receipt hashes")
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    started=time.monotonic();budget=raw.Budget(args.max_seconds,args.memory_mib,args.integer_bits);ctx={}
    report={"schema":SCHEMA,"source_hashes":source_identity(),"target_weight":-2,
        "github_repository":os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"github_sha":os.environ.get("GITHUB_SHA"),
        "completion":"not_started","phase":"binding_existing_originals","task_complete":False,
        "original_kernel_question":"one source-bound complete-positive scalar point must kill every real original function relation",
        "word_map_sound_but_not_asserted_complete":True,"Phi_is_not_identified_with_reused_Psi":True,
        "old_response_forcing_profile_evaluation_RREF_LP_or_path_integral_performed":False,
        "true_character_or_period_or_ruling_constructed":False,
        "limits":{key:getattr(args,key) for key in numerical}}
    try:
        if args.binding_toy_only:
            report["development"]=binding_only_checks()
            report.update(completion="complete",phase="only_new_archived_manifest_metadata_checks_complete")
        elif args.toy_only:
            report["development"]=artificial_checks()
            report.update(completion="complete",phase="only_new_artificial_interface_checks_complete")
        else:actual(args,report,ctx,budget)
    except (raw.Limit,exact.formal.CompilationBudgetExceeded,MemoryError) as error:
        report.update(completion="resource_limit",error={"type":type(error).__name__,"message":str(error)},
            global_term_cache_byte_or_coefficient_caps_are_not_silently_increased=True)
    except Exception as error:
        report.update(completion="implementation_check_failed",
                      error={"type":type(error).__name__,"message":str(error)})
    if "state" in ctx:
        try:save_outputs(ctx,args,report)
        except Exception as error:
            report["storage_error"]={"type":type(error).__name__,"message":str(error)}
            if report["completion"]=="complete":report["completion"]="resource_limit"
            try:save_state(ctx,args,report)
            except Exception as checkpoint_error:
                report["latest_state_storage_error"]={"type":type(checkpoint_error).__name__,
                                                       "message":str(checkpoint_error)}
        summarize(ctx,report)
    report.update(elapsed_seconds=time.monotonic()-started,
        peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,
        exact_budget_checks=budget.operations,maximum_exact_coefficient_bits=budget.maximum_bits)
    payload=raw.canonical(report)
    if len(payload)>args.max_main_bytes:
        report={key:report.get(key) for key in ("schema","source_hashes","github_repository",
            "github_run_id","github_sha","input_binding_sha256","shared_word_progress",
            "prescribed_point_diagnostic","new_original_relation_certificate","resumable_shared_word_state")}
        report.update(completion="resource_limit",phase="small_main_byte_ceiling",
            full_unwritten_main_bytes=len(payload),full_unwritten_main_sha256=raw.sha(payload),
            task_complete=False)
        payload=raw.canonical(report)
    if len(payload)>args.max_main_bytes:
        raise raw.Limit("even the source-bound minimal main exceeds its explicitly declared byte ceiling")
    raw.atomic_write(args.output,payload)
    print(json.dumps({"output":args.output.name,"completion":report["completion"],
        "phase":report["phase"],"bytes":len(payload),"sha256":raw.sha(payload)}),flush=True)
    return 0 if report["completion"] in ("complete","resource_limit") else 2


if __name__=="__main__":
    raise SystemExit(main())
