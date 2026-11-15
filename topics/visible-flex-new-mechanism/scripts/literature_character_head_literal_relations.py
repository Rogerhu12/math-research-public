#!/usr/bin/env python3
"""New literal Q-relations among the published 40 R and 107 normal columns.

Read the common original right-Volterra DAG, without generating a response,
normal form, profile value, path integral, old RREF, or LP.  The two canonical
modes are separate rows.  Every dependent column receives a fresh sum of the
original stored coefficients; an echelon zero alone is never a certificate.
Literal independence is not functional independence.  Real inputs run only
in this public repository's GitHub Actions; local execution is toy-only.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from fractions import Fraction as F
import gzip
import hashlib
import json
from math import gcd, lcm
import os
from pathlib import Path
import resource
import sys
import time

SCHEMA = "visible-flex-character-head-literal-relations-v1"
REPOSITORY = "Rogerhu12/math-research-public"
LANE = "character_head_literal_relations"
MAIN_NAME = "character-head-literal-relations.json"
CERT_NAME = "character-head-literal-relations-certificate.json.gz"
STATE_NAME = "character-head-literal-relations-state.json.gz"
MODES = (-4, -2)
R_COUNT, NORMAL_COUNT, COLUMN_COUNT = 40, 107, 147
R_ORIGINAL_COLUMNS = tuple(range(24)) + (25,27,28,29,31,32,33,35,36,39,40,41,46,47,48,49)
HEAD = {
    "run":"43665345551", "commit":"0aae9a6a85583a9f87415e586d8db2c9c7fea6a7",
    "lane":"character_head_minus2", "schema":"visible-flex-complete-character-head-minus2-v1",
    "main":{"filename":"character-head-minus2.json","bytes":15967,
        "sha256":"55320985df05f928caf007016777ecb2413f16c969dca4741b0c2e936f00b940"},
    "receipt":{"filename":"receipt.json","bytes":39451,
        "sha256":"88bdcf2dadbba25d816e886705b70e7844f698f07917b696698e86ea2770f675"},
    "artifact":{"filename":"character-head-minus2-original-expressions.json.gz",
        "stored_bytes":1247411,"stored_sha256":"2c1242e13d253ba352c7ff1b025a91cf564ab2a7cfd93c6bcedc19baa5fac45c",
        "raw_bytes":6560138,"raw_sha256":"7a93a53aa7fafa1cff76608aceaeac294911ca4f828746913c1b125ae2fd33af"},
    "metadata_key":"portable_head_export",
    "driver":{"filename":"literature_character_head_minus2.py","bytes":58856,
        "sha256":"fcc41b4d5a640a1ac411e7f6f29622db81c39cb2be37aed7811136418a045f11"},
}
FINITE = {
    "run":"43665971895", "commit":"05bb659b59997906316ddd2873aedbf4840f62a5",
    "lane":"character_minus2_finite_necessary",
    "schema":"visible-flex-character-minus2-finite-rational-necessary-v1",
    "main":{"filename":"character-minus2-finite-necessary.json","bytes":10143,
        "sha256":"1e8d751fca7fb6d8b2c33d1152e8651399824be22ffad5496c8bdb48de7fef6c"},
    "receipt":{"filename":"receipt.json","bytes":40026,
        "sha256":"6fbdf4f3c98bfa14fe6344d988a5df9acad10b4c7e598711aa3f5b57c8515764"},
    "artifact":{"filename":"character-minus2-finite-necessary-certificate.json.gz",
        "stored_bytes":31976,"stored_sha256":"5658e056313fff939356f91c97578a8dfc3e1158661b209c84ba7d2b86aa3634",
        "raw_bytes":143028,"raw_sha256":"dd539b088c354d99c04af46d8d7c63822679f13ebc02b14a673c76767fd745f7"},
    "metadata_key":"complete_necessary_certificate",
    "driver":{"filename":"literature_character_minus2_finite_necessary.py","bytes":45116,
        "sha256":"d4c3751cf58f1ef08c534e61a16d7a40cd368980c0cca0ef48a0bce505ce3545"},
}
PARITY = {
    "run":"43668125602", "commit":"c8a89721ee361074096b202af6aa0841ac1bc445",
    "lane":"character_minus2_static_parity",
    "schema":"visible-flex-character-minus2-static-and-quadratic-parity-cuts-v1",
    "main":{"filename":"character-minus2-static-parity.json","bytes":6971,
        "sha256":"bb2e66e4ddd6e0e826c8aa78cef96462e23290852f512b84ab0d3fceb800f968"},
    "receipt":{"filename":"receipt.json","bytes":40112,
        "sha256":"947bbcd35c08476233568a67c8f6b4c322bf8991284b8c9382fc65fea2ccd6d2"},
    "artifact":{"filename":"character-minus2-static-parity-certificate.json.gz",
        "stored_bytes":9222,"stored_sha256":"2431172cb890ad9d6bc7fa227793fabd9a33e5f254531ff2411b6fbc6870e3af",
        "raw_bytes":34807,"raw_sha256":"f15004c94a2400bf9fed2e9705227ba2cd1ca2dacc38080a25bf703e9f27ef23"},
    "metadata_key":"complete_necessary_certificate",
    "driver":{"filename":"literature_character_minus2_static_and_parity_cuts.py","bytes":18508,
        "sha256":"9e7f7d2b9b70b78a3eec17f8c4c2e4cd64caf8d6304247355aaff55c962f41e1"},
}


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(path):
    path=Path(path);raw=path.read_bytes()
    return {"filename":path.name,"bytes":len(raw),"sha256":sha(raw)}


def source_identity():
    return {"driver":identity(__file__),"external_research_helpers_imported":False,
        "portable_digest_protocol":{
            "atom":"sha256(JSON jet, or [int_r_to_x,power,sorted child hashes])",
            "root":"sha256(JSON sorted [power,sorted atom hashes,numerator,denominator])",
            "published_protocol_source":"literature_pure_bulk_exact_membership.py",
            "published_protocol_source_sha256":"f7f3e3c6c8732ad9da047fb6005d314dc8568c189fe3cc0c9edef8843051eb70"}}


class Limit(RuntimeError):
    pass


class Budget:
    def __init__(self,seconds=240,memory_mib=1024,bits=8192):
        self.started=time.monotonic();self.seconds=seconds;self.memory_mib=memory_mib
        self.bits=bits;self.operations=0;self.maximum_bits=0
    def check(self,values=None):
        self.operations+=1
        if time.monotonic()-self.started>self.seconds:
            raise Limit("declared elapsed-time ceiling")
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024>self.memory_mib:
            raise Limit("polled resident-memory ceiling")
        if values is not None:
            largest=0
            for value in values:
                if isinstance(value,F):
                    largest=max(largest,abs(value.numerator).bit_length(),value.denominator.bit_length())
                else:
                    largest=max(largest,abs(value).bit_length())
            self.maximum_bits=max(self.maximum_bits,largest)
            if largest>self.bits:
                raise Limit("stored exact coefficient bit ceiling")


def read_small(path,spec):
    raw=Path(path).read_bytes()
    if len(raw)>100000 or len(raw)!=spec["bytes"] or sha(raw)!=spec["sha256"]:
        raise ValueError("bound small published input bytes/SHA changed")
    return json.loads(raw),raw


def checked_gzip(path,metadata,raw_cap=40000000):
    packed=Path(path).read_bytes()
    if (len(packed)>4800000 or len(packed)!=metadata["stored_bytes"]
        or sha(packed)!=metadata["stored_sha256"]):
        raise ValueError("bound gzip bytes/SHA changed")
    with gzip.open(path,"rb") as stream:
        raw=stream.read(raw_cap+1)
    if len(raw)>raw_cap or len(raw)!=metadata["raw_bytes"] or sha(raw)!=metadata["raw_sha256"]:
        raise ValueError("bound uncompressed bytes/SHA changed")
    return json.loads(raw)


def publication_outputs(receipt):
    outputs={}
    for row in receipt.get("outputs",[]):
        name=Path(row["path"]).name
        if name in outputs:
            raise ValueError("ambiguous published output basename")
        outputs[name]=row
    return outputs


def verify_publication(receipt,main,main_raw,spec,metadata):
    if (receipt.get("schema")!="visible-new-mechanism-actions-v1"
        or receipt.get("repository")!=REPOSITORY or str(receipt.get("run_id"))!=spec["run"]
        or receipt.get("source_commit")!=spec["commit"] or receipt.get("lane")!=spec["lane"]):
        raise ValueError("published run/source/repository/lane changed")
    if (main.get("schema")!=spec["schema"] or main.get("completion")!="complete"
        or main.get("github_repository")!=REPOSITORY or str(main.get("github_run_id"))!=spec["run"]
        or main.get("github_sha")!=spec["commit"] or main.get("source_hashes",{}).get("driver")!=spec["driver"]):
        raise ValueError("complete published producer main required")
    source=[v for k,v in receipt.get("source_files",{}).items() if Path(k).name==spec["driver"]["filename"]]
    if len(source)!=1 or any(source[0].get(k)!=spec["driver"][k] for k in ("bytes","sha256")):
        raise ValueError("publication does not bind the exact producer")
    if any(metadata.get(k)!=v for k,v in spec["artifact"].items()):
        raise ValueError("published original/certificate metadata changed")
    outputs=publication_outputs(receipt)
    for name,wanted in (
        (spec["main"]["filename"],{"bytes":len(main_raw),"sha256":sha(main_raw),
            "raw_bytes":len(main_raw),"raw_sha256":sha(main_raw)}),
        (metadata["filename"],{"bytes":metadata["stored_bytes"],"sha256":metadata["stored_sha256"],
            "raw_bytes":metadata["raw_bytes"],"raw_sha256":metadata["raw_sha256"]})):
        if any(outputs.get(name,{}).get(k)!=v for k,v in wanted.items()):
            raise ValueError("publication output bytes/SHA changed")


def consume_bound(directory,spec):
    main,raw=read_small(directory/spec["main"]["filename"],spec["main"])
    receipt,_=read_small(directory/"receipt.json",spec["receipt"])
    metadata=main.get(spec["metadata_key"],{})
    verify_publication(receipt,main,raw,spec,metadata)
    data=checked_gzip(directory/metadata["filename"],metadata)
    if data.get("source_hashes")!=main.get("source_hashes"):
        raise ValueError("artifact source identity differs from its published main")
    return main,data,{k:spec[k] for k in ("run","commit","lane","main","receipt","artifact","driver")}


def monomial(raw,atom_count):
    if not isinstance(raw,list) or len(raw)!=2:
        raise ValueError("portable monomial must have two entries")
    power,indices=raw
    if (type(power) is not int or power<0 or not isinstance(indices,list)
        or any(type(i) is not int or not 0<=i<atom_count for i in indices)
        or indices!=sorted(indices)):
        raise ValueError("invalid portable power/atom multiset")
    return power,tuple(indices)


def portable_atom_hashes(atoms):
    answer=[]
    for node in atoms:
        if not isinstance(node,list) or not node:
            raise ValueError("invalid original atom")
        if node[0]=="jet":
            if len(node)!=3 or not isinstance(node[1],str) or type(node[2]) is not int or node[2]<0:
                raise ValueError("invalid original jet")
            payload=node
        elif node[0]=="int_right" and len(node)==2:
            power,factors=monomial(node[1],len(answer))
            if not factors:
                raise ValueError("original profile primitive must have positive profile degree")
            payload=["int_r_to_x",power,sorted(answer[i] for i in factors)]
        else:
            raise ValueError("unsupported original atom kind")
        answer.append(sha(json.dumps(payload,separators=(",",":"),ensure_ascii=True).encode()))
    return answer


def validate_root(rows,atom_hashes,wanted):
    seen=set();digest_rows=[];previous=None
    for raw,n,d in rows:
        key=monomial(raw,len(atom_hashes))
        if (key in seen or (previous is not None and key<=previous)
            or type(n) is not int or type(d) is not int or not n or d<=0 or gcd(abs(n),d)!=1):
            raise ValueError("original coefficient rows are not unique sorted reduced rationals")
        seen.add(key);previous=key
        digest_rows.append([key[0],sorted(atom_hashes[i] for i in key[1]),n,d])
    digest_rows.sort()
    got=sha(json.dumps(digest_rows,separators=(",",":"),ensure_ascii=True).encode())
    if got!=wanted:
        raise ValueError("selected original root content hash mismatch")
    return {"original_sha256":got,"stored_rows_sha256":sha(canonical(rows)),"stored_terms":len(rows)}


class OriginalColumns:
    """Bound existing polynomials, not a symbolic response compiler."""
    def __init__(self,raw_columns,metadata,budget,atom_count=None):
        self.raw=raw_columns;self.metadata=metadata;self.count=len(raw_columns)
        self.row_keys=[];self.row_index={};self.denominator=1;total=0
        keys=set()
        for modes in raw_columns:
            for mode in MODES:
                for raw,n,d in modes[mode]:
                    key=(mode,raw[0],tuple(raw[1]));keys.add(key)
                    self.denominator=lcm(self.denominator,d);total+=1
                budget.check((self.denominator,))
        self.row_keys=sorted(keys);self.row_index={key:i for i,key in enumerate(self.row_keys)}
        self.term_rows=total
        self.row_table_sha256=sha(canonical([[m,p,list(a)] for m,p,a in self.row_keys]))
        self.metadata_sha256=sha(canonical(metadata))
        self.atom_count=atom_count
    def integer_vector(self,index):
        result={}
        for mode in MODES:
            for raw,n,d in self.raw[index][mode]:
                key=(mode,raw[0],tuple(raw[1]))
                result[self.row_index[key]]=n*(self.denominator//d)
        return result
    def combination(self,coefficients,budget):
        """Materialize a saved state vector; no elimination or function evaluation."""
        result={}
        for index,amount in sorted(coefficients.items()):
            for mode in MODES:
                for raw,n,d in self.raw[index][mode]:
                    key=self.row_index[(mode,raw[0],tuple(raw[1]))]
                    value=result.get(key,0)+amount*n*(self.denominator//d)
                    if value:result[key]=value
                    else:result.pop(key,None)
            budget.check(result.values())
        return result


def read_fraction_row(rows,dimension):
    out={}
    for index,value in rows:
        if type(index) is not int or not 0<=index<dimension or index in out:
            raise ValueError("invalid exact coordinate form")
        value=F(value)
        if value:out[index]=value
    return out


def serial_fraction_row(row):
    return [[i,str(c)] for i,c in sorted(row.items())]


def serial_integer_row(row):
    return [[i,str(c)] for i,c in sorted(row.items())]


def read_integer_row(rows,dimension):
    out={}
    for i,c in rows:
        if type(i) is not int or not 0<=i<dimension or i in out:
            raise ValueError("invalid stored integer coordinate")
        c=int(c)
        if c:out[i]=c
    return out


def add_fraction_row(target,source,amount):
    for i,c in source.items():
        value=target.get(i,F(0))+amount*c
        if value:target[i]=value
        else:target.pop(i,None)


def project_normal(row,transform):
    result={}
    for i,c in row.items():add_fraction_row(result,transform[i],F(c))
    return result


def evaluate_form(row,point):
    return sum((c*point[i] for i,c in row.items()),F(0))


def load_inputs(args,report,budget):
    hmain,head,hbinding=consume_bound(args.head_dir,HEAD)
    fmain,finite,fbinding=consume_bound(args.finite_dir,FINITE)
    pmain,parity,pbinding=consume_bound(args.parity_dir,PARITY)
    if (head.get("schema")!=HEAD["schema"]+"-original-expressions"
        or head.get("content_scope")!="complete-fourteen-weight-minus2-families-and-translation-presentation"
        or head.get("all_fourteen_families_complete") is not True
        or head.get("all_planned_contractions_present") is not True
        or head.get("planned_contractions")!=head.get("completed_contractions")
        or hmain.get("head_generation_complete") is not True
        or head.get("target_weight")!=-2 or str(head.get("github_run_id"))!=HEAD["run"]
        or head.get("github_sha")!=HEAD["commit"]):
        raise ValueError("only the complete bound head is an input")
    for data,spec in ((finite,FINITE),(parity,PARITY)):
        if (data.get("schema")!=spec["schema"]+"-certificate" or data.get("target_weight")!=-2
            or data.get("all_true_positive_characters_embed_in_this_outer_system") is not True):
            raise ValueError("wrong inherited exact outer-coordinate system")
    if (finite.get("normal_coordinate_count")!=NORMAL_COUNT
        or finite.get("normal_coordinate_metadata")!=head.get("normal_family_records")
        or len(finite.get("equalities",[]))!=124 or len(finite.get("rref_equalities",[]))!=84
        or len(finite.get("reduced_inequalities",[]))!=63):
        raise ValueError("the inherited 107-coordinate presentation changed")
    for name,spec in (("main",HEAD["main"]),("publication",HEAD["receipt"]),("export",HEAD["artifact"])):
        if any(finite.get("input",{}).get(name,{}).get(k)!=v for k,v in spec.items()):
            raise ValueError("finite coordinates do not use this exact head")
    if (parity.get("input",{}).get("certificate")!=FINITE["artifact"]
        or parity.get("free_normal_coordinates")!=finite.get("free_normal_coordinates")
        or len(parity.get("updated_reduced_inequalities",[]))!=68):
        raise ValueError("newer candidate/parity is not over the archived coordinate map")
    normal=head["normal_family_records"];responses=head["archived_R_basis_records"]
    if ([r["index"] for r in normal]!=list(range(NORMAL_COUNT))
        or tuple(r["original_column"] for r in responses)!=R_ORIGINAL_COLUMNS):
        raise ValueError("complete normal/R column ordering changed")
    atoms=portable_atom_hashes(head["profile_atoms"]);metadata=[];raw_columns=[]
    for kind,records in (("archived_R",responses),("normal",normal)):
        for position,record in enumerate(records):
            if set(record["roots"])!={"-4","-2"}:
                raise ValueError("both canonical original modes are required")
            roots={};proofs={}
            expected=record["label"]["original_mode_sha256"] if kind=="archived_R" else record["original_mode_sha256"]
            for mode in MODES:
                name=record["roots"][str(mode)];wanted=head["original_root_sha256"][name]
                if expected[str(mode)]!=wanted:
                    raise ValueError("selected column label does not bind its original root")
                rows=head["roots"][name];proofs[str(mode)]=validate_root(rows,atoms,wanted)
                roots[mode]=rows
            metadata.append({"column":len(metadata),"kind":kind,"within_kind_index":position,
                "normal_index":position if kind=="normal" else None,
                "archived_original_R_column":record.get("original_column"),
                "original_metadata":record,"bound_mode_roots":proofs})
            raw_columns.append(roots);budget.check()
    columns=OriginalColumns(raw_columns,metadata,budget,len(atoms))
    if columns.count!=COLUMN_COUNT:
        raise ValueError("the new literal comparison must have exactly 147 columns")
    free=finite["free_normal_coordinates"];dimension=len(free)
    transform=[read_fraction_row(row,dimension) for row in finite["normal_coordinates_as_free_linear_forms"]]
    if len(transform)!=NORMAL_COUNT or dimension!=23:
        raise ValueError("inherited x=B*y dimensions changed")
    for j,i in enumerate(free):
        if transform[i]!={j:F(1)}:raise ValueError("inherited coordinate meanings changed")
    inherited_parity=[]
    detail=parity.get("complete_quadratic_parity",{})
    if detail.get("theorem")!="R168" or detail.get("all_stored_degrees_of_all_three_Q2_families_scanned") is not True:
        raise ValueError("the complete published quadratic parity rows are required")
    for row in detail["wrong_parity_coefficient_rows"]:
        original=read_fraction_row(row["normal_coordinate_linear_form"],NORMAL_COUNT)
        reduced=read_fraction_row(row["free_coordinate_equality"],dimension)
        if project_normal(original,transform)!=reduced:
            raise ValueError("stored parity row is not the same inherited linear form")
        inherited_parity.append({"family":row["family"],"degree":row["degree"],
            "normal_coordinate_linear_form":row["normal_coordinate_linear_form"],
            "free_coordinate_equality":row["free_coordinate_equality"]})
    point=list(map(F,parity["decision"]["outer_candidate"]))
    if len(point)!=dimension:raise ValueError("published diagnostic point has wrong dimension")
    diagnostics={"published_static_parity_outer_point":point}
    if args.diagnose_half_static:
        if free[12]!=73:raise ValueError("the named half-static diagnostic uses y12=normal73")
        modified=list(point);modified[12]=F(-1,2)
        diagnostics["explicit_half_static_diagnostic_not_asserted_realizable"]=modified
    core={"head":hbinding,"column_metadata_sha256":columns.metadata_sha256,
        "profile_atoms_sha256":sha(canonical(head["profile_atoms"])),
        "row_table_sha256":columns.row_table_sha256,"common_integer_denominator":str(columns.denominator),
        "column_order":"40 archived R, then normal indices 0 through 106; both modes tagged separately",
        "selected_original_root_count":2*COLUMN_COUNT,"anchor":head["anchor"]}
    view={"finite":fbinding,"parity":pbinding,
        "old_equalities_sha256":sha(canonical(finite["equalities"])),
        "old_rref_sha256":sha(canonical(finite["rref_equalities"])),
        "old_normal_to_free_sha256":sha(canonical(finite["normal_coordinates_as_free_linear_forms"])),
        "old_63_halfspaces_sha256":sha(canonical(finite["reduced_inequalities"])),
        "updated_68_halfspaces_sha256":sha(canonical(parity["updated_reduced_inequalities"])),
        "inherited_66_translation_rows_sha256":sha(canonical(head["head_translation_presentation"])),
        "free_normal_coordinates":free,"inherited_parity":inherited_parity,
        "diagnostic_configuration":{name:[str(v) for v in point] for name,point in diagnostics.items()}}
    report["inputs"]={"head":hbinding,"finite":fbinding,"parity":pbinding}
    report["read_only_original_inventory"]={"columns":columns.count,"original_root_count":2*columns.count,
        "stored_term_rows":columns.term_rows,"literal_row_count":len(columns.row_keys),
        "profile_atoms":len(atoms),"all_selected_original_content_hashes_checked":True,
        "new_response_or_forcing_or_profile_evaluation":False}
    return columns,transform,inherited_parity,diagnostics,core,view


def normalize_integer_pair(vector,combination):
    divisor=0
    for value in vector.values():divisor=gcd(divisor,abs(value))
    for value in combination.values():divisor=gcd(divisor,abs(value))
    if not divisor:raise AssertionError("a column certificate cannot be the zero pair")
    sign=vector[min(vector)] if vector else combination[max(combination)]
    if sign<0:divisor=-divisor
    if divisor!=1:
        vector={i:c//divisor for i,c in vector.items()}
        combination={i:c//divisor for i,c in combination.items()}
    return vector,combination


def integer_sum(first,a,second,b):
    result={i:a*c for i,c in first.items() if a*c}
    for i,c in second.items():
        value=result.get(i,0)+b*c
        if value:result[i]=value
        else:result.pop(i,None)
    return result


def exact_reduce_step(vector,combination,basis,budget):
    pivot=min(vector);item=basis[pivot]
    bp=item["vector"][pivot];vp=vector[pivot];divisor=gcd(abs(bp),abs(vp))
    a,b=bp//divisor,vp//divisor
    new_vector=integer_sum(vector,a,item["vector"],-b)
    new_combination=integer_sum(combination,a,item["combination"],-b)
    if pivot in new_vector:raise AssertionError("exact integer pivot did not cancel")
    new_vector,new_combination=normalize_integer_pair(new_vector,new_combination)
    budget.check(new_vector.values());budget.check(new_combination.values())
    return new_vector,new_combination


def vector_hash(vector):
    return sha(canonical(serial_integer_row(vector)))


def reduce_small(row,basis,budget,insert=None):
    remaining=dict(row);trace=[]
    for pivot,item in sorted(basis.items()):
        amount=remaining.get(pivot,F(0))
        if amount:
            add_fraction_row(remaining,item["row"],-amount)
            trace.append({"basis_label":item["label"],"amount":str(amount)})
            budget.check(remaining.values())
    if remaining and insert is not None:
        pivot=min(remaining);scale=remaining[pivot]
        basis[pivot]={"row":{i:c/scale for i,c in remaining.items()},"label":insert,
            "source_form":serial_fraction_row(row),"prior_reduction":trace,"normalization":str(scale)}
    return remaining,trace


def initial_state(parities,budget):
    small={}
    for i,row in enumerate(parities):
        reduce_small(read_fraction_row(row["free_coordinate_equality"],23),small,budget,
                     insert="inherited_parity_"+str(i))
    return {"cursor":0,"basis":{},"pending":None,"relations":[],"small_basis":small,
        "independent_original_columns":[],"new_free_equality_count":0,
        "reduction_operations":0,"fresh_original_column_sums":0,
        "resumed_elimination_operations_not_repeated":True}


def start_pending(state,columns,budget):
    index=state["cursor"];vector=columns.integer_vector(index);combination={index:1}
    vector,combination=normalize_integer_pair(vector,combination)
    budget.check(vector.values())
    state["pending"]={"column":index,"stage":"reduce","vector":vector,"combination":combination,
        "reduction_operations":0}


def prepare_verification(pending):
    _,coefficients=normalize_integer_pair({},pending["combination"])
    pending.update(stage="verify_original",combination=coefficients,vector={},
        verify_cursor=0,verify_accumulator={},verify_terms={str(m):0 for m in MODES})


def verify_original_step(pending,columns,budget):
    """Fresh original-row keys, independent of the elimination's indexed rows."""
    support=sorted(pending["combination"].items());cursor=pending["verify_cursor"]
    if cursor==len(support):
        if pending["verify_accumulator"]:
            raise AssertionError("echelon zero failed the fresh two-mode original coefficient sum")
        pending["fresh_original_check"]={"all_modes_exact_original_zero":True,
            "common_positive_denominator":str(columns.denominator),
            "verification":"fresh sum from original stored rational rows, with raw monomial keys",
            "mode_checks":{str(mode):{"summed_original_term_rows":pending["verify_terms"][str(mode)],
                "remaining_terms":0,"zero_rows_sha256":sha(canonical([]))} for mode in MODES}}
        pending["stage"]="project_verified_relation"
        return False
    index,amount=support[cursor]
    accumulator=dict(pending["verify_accumulator"]);counts=dict(pending["verify_terms"])
    for mode in MODES:
        for raw,n,d in columns.raw[index][mode]:
            key=(mode,raw[0],tuple(raw[1]))
            value=accumulator.get(key,0)+amount*n*(columns.denominator//d)
            if value:accumulator[key]=value
            else:accumulator.pop(key,None)
            counts[str(mode)]+=1
    budget.check(accumulator.values())
    pending["verify_accumulator"]=accumulator;pending["verify_terms"]=counts
    pending["verify_cursor"]=cursor+1
    return True


def commit_verified_relation(state,columns,transform,diagnostics,budget,r_count=R_COUNT):
    pending=state["pending"];index=pending["column"];coefficients=pending["combination"]
    if index<r_count:
        raise AssertionError("a fresh exact dependence among the previously certified independent R columns")
    if max(coefficients)!=index or coefficients[index]<=0:
        raise AssertionError("new original dependency lacks its nonzero triangular diagonal")
    normal={i-r_count:F(c) for i,c in coefficients.items() if i>=r_count}
    projected=project_normal(normal,transform);budget.check(projected.values())
    # Tiny new equality algebra only.  The archived 124 equations and RREF are never rebuilt.
    next_small=deepcopy(state["small_basis"]);relation_index=len(state["relations"])
    remaining,trace=reduce_small(projected,next_small,budget,insert="literal_relation_"+str(relation_index))
    if not projected:status="already_implied_by_archived_normal_to_free_map"
    elif not remaining:status="already_implied_by_R168_and_earlier_new_literal_relations"
    else:status="new_exact_equality_modulo_archived_map_R168_and_earlier_relations"
    record={"relation_index":relation_index,"dependent_original_column":index,
        "dense_147_original_coefficients":[str(coefficients.get(i,0)) for i in range(columns.count)],
        "original_column_coefficients":serial_integer_row(coefficients),
        "normal_coordinate_equality":serial_fraction_row(normal),
        "old_free_coordinate_equality":serial_fraction_row(projected),
        "new_row_status":status,"residual_after_known_equalities":serial_fraction_row(remaining),
        "exact_known_row_reduction":trace,"fresh_original_check":pending["fresh_original_check"],
        "diagnostic_values":{name:{"exact_value":str(evaluate_form(projected,point)),
            "violates_this_true_equality":bool(evaluate_form(projected,point))}
            for name,point in diagnostics.items()}}
    state["relations"].append(record);state["small_basis"]=next_small
    state["new_free_equality_count"]+=bool(remaining)
    state["cursor"]+=1;state["pending"]=None
    return record


def advance_one_column(state,columns,transform,diagnostics,budget,r_count=R_COUNT):
    if state["pending"] is None:start_pending(state,columns,budget)
    while state["pending"] is not None:
        budget.check();pending=state["pending"]
        if pending["stage"]=="reduce":
            vector=pending["vector"]
            if not vector:
                prepare_verification(pending);continue
            pivot=min(vector)
            if pivot not in state["basis"]:
                state["basis"][pivot]={"vector":vector,"combination":pending["combination"],
                    "source_column":pending["column"]}
                state["independent_original_columns"].append(pending["column"])
                state["cursor"]+=1;state["pending"]=None
                return None
            vector,combination=exact_reduce_step(vector,pending["combination"],state["basis"],budget)
            pending["vector"]=vector;pending["combination"]=combination
            pending["reduction_operations"]+=1;state["reduction_operations"]+=1
        elif pending["stage"]=="verify_original":
            if verify_original_step(pending,columns,budget):state["fresh_original_column_sums"]+=1
        elif pending["stage"]=="project_verified_relation":
            return commit_verified_relation(state,columns,transform,diagnostics,budget,r_count)
        else:
            raise ValueError("unknown exact continuation phase")


def serialized_state(state,columns,core_sha,view_sha,driver,compact=False):
    entries=[]
    for pivot,item in sorted(state["basis"].items()):
        entry={"pivot":pivot,"source_column":item["source_column"],
            "combination":serial_integer_row(item["combination"]),
            "vector_sha256":vector_hash(item["vector"]),"vector_terms":len(item["vector"])}
        if not compact:entry["vector"]=serial_integer_row(item["vector"])
        entries.append(entry)
    pending=None
    if state["pending"] is not None:
        item=state["pending"]
        pending={k:v for k,v in item.items() if k not in ("vector","combination","verify_accumulator")}
        pending["combination"]=serial_integer_row(item["combination"])
        pending["vector_sha256"]=vector_hash(item["vector"])
        pending["vector_terms"]=len(item["vector"])
        if not compact:pending["vector"]=serial_integer_row(item["vector"])
        if "verify_accumulator" in item:
            pending["verify_accumulator"]=[[[m,p,list(a)],str(c)]
                for (m,p,a),c in sorted(item["verify_accumulator"].items())]
    result={k:v for k,v in state.items() if k not in ("basis","pending","small_basis")}
    result.update(schema=SCHEMA+"-continuation-state",source_driver=driver,
        core_input_sha256=core_sha,inherited_view_sha256=view_sha,
        literal_row_table_sha256=columns.row_table_sha256,column_metadata_sha256=columns.metadata_sha256,
        common_integer_denominator=str(columns.denominator),column_count=columns.count,
        basis=entries,pending=pending,
        small_basis=[{"pivot":p,**{k:v for k,v in item.items() if k!="row"},
                      "row":serial_fraction_row(item["row"])} for p,item in sorted(state["small_basis"].items())],
        vector_storage=("exact_original_linear_combinations_with_vector_hashes" if compact else "explicit_exact_vectors"),
        saved_state_is_new_elimination_not_an_unproved_research_result=True)
    return result


def restore_state(data,columns,core_sha,view_sha,driver,budget):
    if (data.get("schema")!=SCHEMA+"-continuation-state" or data.get("source_driver")!=driver
        or data.get("core_input_sha256")!=core_sha or data.get("inherited_view_sha256")!=view_sha
        or data.get("literal_row_table_sha256")!=columns.row_table_sha256
        or data.get("column_metadata_sha256")!=columns.metadata_sha256
        or data.get("common_integer_denominator")!=str(columns.denominator)
        or data.get("column_count")!=columns.count):
        raise ValueError("saved new elimination is not bound to this exact source/input/view")
    cursor=data["cursor"]
    if type(cursor) is not int or not 0<=cursor<=columns.count:
        raise ValueError("invalid continuation column cursor")
    state={k:data[k] for k in ("cursor","relations","independent_original_columns","new_free_equality_count",
        "reduction_operations","fresh_original_column_sums","resumed_elimination_operations_not_repeated")}
    basis={};restored_from_combinations=0
    for entry in data["basis"]:
        coefficients=read_integer_row(entry["combination"],columns.count)
        if not coefficients or max(coefficients)>=cursor:
            raise ValueError("saved basis depends on a future column")
        if "vector" in entry:
            vector=read_integer_row(entry["vector"],len(columns.row_keys))
        else:
            vector=columns.combination(coefficients,budget);restored_from_combinations+=1
        if (not vector or min(vector)!=entry["pivot"] or vector[min(vector)]<=0
            or vector_hash(vector)!=entry["vector_sha256"] or len(vector)!=entry["vector_terms"]
            or entry["pivot"] in basis):
            raise ValueError("saved exact basis vector integrity changed")
        basis[entry["pivot"]]={"vector":vector,"combination":coefficients,"source_column":entry["source_column"]}
        budget.check(vector.values())
    if len(basis)+len(state["relations"])!=cursor:
        raise ValueError("completed basis/dependency counts do not cover the saved prefix")
    state["basis"]=basis;state["small_basis"]={}
    for entry in data["small_basis"]:
        row=read_fraction_row(entry["row"],23);pivot=entry["pivot"]
        if not row or min(row)!=pivot or row[pivot]!=1 or pivot in state["small_basis"]:
            raise ValueError("saved new small equality basis changed")
        state["small_basis"][pivot]={k:v for k,v in entry.items() if k not in ("pivot","row")}
        state["small_basis"][pivot]["row"]=row
    pending=data.get("pending")
    if pending is not None:
        if pending["column"]!=cursor or cursor==columns.count:
            raise ValueError("saved active column does not follow the completed prefix")
        coefficients=read_integer_row(pending["combination"],columns.count)
        if not coefficients or max(coefficients)!=cursor:
            raise ValueError("active column has no triangular original certificate")
        if "vector" in pending:
            vector=read_integer_row(pending["vector"],len(columns.row_keys))
        else:
            vector=columns.combination(coefficients,budget);restored_from_combinations+=1
        if vector_hash(vector)!=pending["vector_sha256"] or len(vector)!=pending["vector_terms"]:
            raise ValueError("saved active exact vector changed")
        state["pending"]={k:v for k,v in pending.items() if k not in ("vector","combination","verify_accumulator")}
        state["pending"].update(vector=vector,combination=coefficients)
        if "verify_accumulator" in pending:
            accumulator={}
            for (mode,power,atoms),coefficient in pending["verify_accumulator"]:
                key=(mode,power,tuple(atoms));coefficient=int(coefficient)
                if key in accumulator or key not in columns.row_index or not coefficient:
                    raise ValueError("saved fresh-verification accumulator changed")
                accumulator[key]=coefficient
            state["pending"]["verify_accumulator"]=accumulator
    else:state["pending"]=None
    return state,{"restored_completed_columns":cursor,
        "restored_active_stage":None if pending is None else pending["stage"],
        "state_vectors_materialized_from_saved_exact_combinations":restored_from_combinations,
        "completed_elimination_steps_replayed":0,"old_functions_or_responses_evaluated":0}


def atomic_write(path,raw):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+".tmp")
    temporary.write_bytes(raw);temporary.replace(path)


def gzip_payload(data,max_packed,max_raw):
    raw=canonical(data)
    if len(raw)>max_raw:raise Limit("raw exact checkpoint/certificate byte ceiling")
    packed=gzip.compress(raw,mtime=0)
    if len(packed)>max_packed:raise Limit("compressed exact checkpoint/certificate byte ceiling")
    return packed,{"stored_bytes":len(packed),"stored_sha256":sha(packed),
        "raw_bytes":len(raw),"raw_sha256":sha(raw)}


def save_state(ctx,args,driver):
    state=ctx["state"];columns=ctx["columns"]
    last_error=None
    for compact in (False,True):
        try:
            data=serialized_state(state,columns,ctx["core_sha"],ctx["view_sha"],driver,compact)
            packed,metadata=gzip_payload(data,args.max_state_bytes,args.max_raw_bytes)
            if len(packed)+ctx.get("certificate_bytes",0)+args.max_main_bytes>args.max_total_bytes:
                raise Limit("combined exact output byte ceiling")
            atomic_write(args.output.parent/STATE_NAME,packed)
            metadata.update(filename=STATE_NAME,completed_columns=state["cursor"],
                active_stage=None if state["pending"] is None else state["pending"]["stage"],
                reduction_operations=state["reduction_operations"],
                fresh_original_column_sums=state["fresh_original_column_sums"],
                vector_storage=data["vector_storage"],resumable=True)
            ctx["state_metadata"]=metadata;return metadata
        except Limit as error:last_error=error
    raise last_error


def certificate_data(ctx,report):
    state=ctx["state"];columns=ctx["columns"]
    new=[r["relation_index"] for r in state["relations"]
         if r["new_row_status"]=="new_exact_equality_modulo_archived_map_R168_and_earlier_relations"]
    return {"schema":SCHEMA+"-certificate","source_hashes":report["source_hashes"],
        "github_repository":report["github_repository"],"github_run_id":report["github_run_id"],
        "github_sha":report["github_sha"],"target_weight":-2,
        "core_input":ctx["core"],"core_input_sha256":ctx["core_sha"],
        "inherited_view":ctx["view"],"inherited_view_sha256":ctx["view_sha"],
        "column_metadata":columns.metadata,"column_order":"R40 first, then normal107",
        "completed_column_prefix":state["cursor"],"all_147_columns_processed":state["cursor"]==columns.count,
        "independent_columns_of_the_literal_matrix":state["independent_original_columns"],
        "literal_matrix_basis_size":len(state["basis"]),"original_dependencies":state["relations"],
        "new_equalities_for_the_inherited_23_coordinates":new,
        "diagnostic_points":{name:[str(v) for v in point] for name,point in ctx["diagnostics"].items()},
        "diagnostics_test_only_new_true_equalities_not_old_68_halfspaces":True,
        "all_dependency_certificates_freshly_checked_in_both_original_modes":True,
        "independence_claim_is_only_for_the_literal_coefficient_matrix":True,
        "true_function_space_rank_computed":False,"positive_character_existence_claimed":False,
        "old_RREF_path_integrals_or_solver_recomputed":False,
        "raw_nonzero_is_never_used_as_functional_nonmembership":True}


def save_certificate(ctx,args,report):
    data=certificate_data(ctx,report)
    packed,metadata=gzip_payload(data,args.max_certificate_bytes,args.max_raw_bytes)
    state_bytes=ctx.get("state_metadata",{}).get("stored_bytes",0)
    if len(packed)+state_bytes+args.max_main_bytes>args.max_total_bytes:
        # An exact circuit checkpoint is smaller; no completed pivot is discarded.
        previous=args.max_state_bytes
        try:
            args.max_state_bytes=min(previous,args.max_total_bytes-len(packed)-args.max_main_bytes)
            if args.max_state_bytes<=0:raise Limit("combined certificate/checkpoint byte ceiling")
            ctx["certificate_bytes"]=len(packed);save_state(ctx,args,report["source_hashes"]["driver"])
        finally:args.max_state_bytes=previous
    atomic_write(args.output.parent/CERT_NAME,packed)
    metadata.update(filename=CERT_NAME,exact_original_dependency_count=len(ctx["state"]["relations"]),
        completed_columns=ctx["state"]["cursor"],contains_explicit_147_column_coefficients=True,
        all_relations_have_fresh_two_mode_original_zero_checks=True)
    ctx["certificate_metadata"]=metadata;ctx["certificate_bytes"]=len(packed)
    return metadata


def load_resume(args,columns,core_sha,view_sha,driver,budget):
    directory=args.resume_dir
    raw=(directory/MAIN_NAME).read_bytes();praw=(directory/"receipt.json").read_bytes()
    if len(raw)>100000 or sha(raw)!=args.resume_main_sha256 or len(praw)>100000 or sha(praw)!=args.resume_publication_sha256:
        raise ValueError("requested published continuation manifest identity changed")
    main=json.loads(raw);publication=json.loads(praw)
    if (main.get("schema")!=SCHEMA or main.get("github_repository")!=REPOSITORY
        or main.get("source_hashes",{}).get("driver")!=driver
        or main.get("completion") not in ("complete","resource_limit")):
        raise ValueError("only a same-source completed or budget-limited published state can resume")
    metadata=main.get("resumable_exact_state",{})
    if (publication.get("schema")!="visible-new-mechanism-actions-v1"
        or publication.get("repository")!=REPOSITORY or publication.get("lane")!=LANE
        or str(publication.get("run_id"))!=str(main.get("github_run_id"))
        or publication.get("source_commit")!=main.get("github_sha") or metadata.get("resumable") is not True):
        raise ValueError("continuation publication run/source/lane mismatch")
    sources=[v for k,v in publication.get("source_files",{}).items() if Path(k).name==driver["filename"]]
    if len(sources)!=1 or any(sources[0].get(k)!=driver[k] for k in ("bytes","sha256")):
        raise ValueError("continuation receipt does not bind this exact driver")
    outputs=publication_outputs(publication)
    for name,wanted in ((MAIN_NAME,{"bytes":len(raw),"sha256":sha(raw)}),
        (metadata.get("filename"),{"bytes":metadata.get("stored_bytes"),"sha256":metadata.get("stored_sha256"),
            "raw_bytes":metadata.get("raw_bytes"),"raw_sha256":metadata.get("raw_sha256")})):
        if any(outputs.get(name,{}).get(k)!=v for k,v in wanted.items()):
            raise ValueError("continuation publication output identity changed")
    if metadata.get("filename")!=STATE_NAME:raise ValueError("unexpected continuation state filename")
    data=checked_gzip(directory/STATE_NAME,metadata,args.max_raw_bytes)
    state,info=restore_state(data,columns,core_sha,view_sha,driver,budget)
    info.update(prior_run=str(main["github_run_id"]),prior_source_commit=main["github_sha"],
        published_main_sha256=sha(raw),published_receipt_sha256=sha(praw),state=metadata)
    return state,info


def actual(args,report,ctx,budget):
    if (os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY
        or not os.environ.get("GITHUB_RUN_ID","").isdigit()
        or len(os.environ.get("GITHUB_SHA",""))!=40):
        raise ValueError("real research inputs are allowed only in this public repository's GitHub Actions")
    report["phase"]="bind_published_original_columns_and_inherited_coordinate_view"
    columns,transform,parities,diagnostics,core,view=load_inputs(args,report,budget)
    ctx.update(columns=columns,transform=transform,parities=parities,diagnostics=diagnostics,
        core=core,view=view,core_sha=sha(canonical(core)),view_sha=sha(canonical(view)))
    if args.resume_dir:
        state,resume=load_resume(args,columns,ctx["core_sha"],ctx["view_sha"],report["source_hashes"]["driver"],budget)
        report["resume"]=resume
    else:state=initial_state(parities,budget)
    ctx["state"]=state
    save_state(ctx,args,report["source_hashes"]["driver"])
    report["phase"]="new_exact_literal_column_relations_R_first"
    while state["cursor"]<columns.count:
        relation=advance_one_column(state,columns,transform,diagnostics,budget)
        if relation is not None:
            violated={name:value["exact_value"] for name,value in relation["diagnostic_values"].items()
                      if value["violates_this_true_equality"]}
            print(json.dumps({"phase":"fresh_original_relation_paid","column":relation["dependent_original_column"],
                "relation":relation["relation_index"],"new_row_status":relation["new_row_status"],
                "violated_diagnostics":violated}),flush=True)
        if state["cursor"]%args.checkpoint_every==0 or relation is not None:
            save_state(ctx,args,report["source_hashes"]["driver"])
    if len(state["basis"])+len(state["relations"])!=columns.count:
        raise AssertionError("literal kernel/basis counts do not cover all original columns")
    report.update(completion="complete",phase="all_147_literal_columns_processed",
        outcome="complete_literal_dependency_kernel_with_fresh_original_two_mode_certificates")


def toy_columns(raw):
    metadata=[{"column":i,"kind":"artificial"} for i in range(len(raw))]
    return OriginalColumns(raw,metadata,Budget(30,512),3)


def artificial_root(*terms):
    return [[[power,list(atoms)],n,d] for power,atoms,n,d in sorted(terms)]


def toy_only():
    checks={};budget=Budget(30,512,2048)
    # One artificial R and three normal columns.  Separate the two modes.
    e0=artificial_root((0,(0,),1,2));e1=artificial_root((0,(1,),1,3))
    raw=[{-4:e0,-2:[]},{-4:e1,-2:[]},
         {-4:artificial_root((0,(0,),3,2),(0,(1,),2,3)),-2:[]},
         {-4:[], -2:artificial_root((0,(1,),1,3))}]
    columns=toy_columns(raw);transform=[{0:F(1)},{1:F(1)},{2:F(1)}]
    state=initial_state([],budget);diagnostics={"invented":[F(1),F(4),F(1)]}
    while state["cursor"]<columns.count:
        advance_one_column(state,columns,transform,diagnostics,budget,r_count=1)
    assert len(state["basis"])==3 and len(state["relations"])==1
    relation=state["relations"][0]
    assert relation["dense_147_original_coefficients"]==["-3","-2","1","0"]
    assert relation["fresh_original_check"]["all_modes_exact_original_zero"] is True
    assert relation["diagnostic_values"]["invented"]["exact_value"]=="2"
    checks["fraction_free_relation_reconstructs_original_rational_columns_and_not_just_echelon_zero"]=True
    assert 3 in state["independent_original_columns"]
    checks["different_canonical_modes_never_cancel_against_each_other"]=True
    # A false certificate must fail a fresh raw-key check even with a forged empty remainder.
    forged={"combination":{0:1,1:-1}};prepare_verification(forged)
    failed=False
    try:
        while forged["stage"]=="verify_original":verify_original_step(forged,columns,budget)
    except AssertionError:failed=True
    assert failed
    checks["forged_echelon_zero_is_rejected_by_independent_original_coefficient_sum"]=True
    # A lexical primitive is not a free physical history: raw nonzero has no nonmember conclusion.
    assert all("functional_nonmember" not in row for row in state["relations"])
    checks["a_new_literal_basis_column_is_not_reported_as_functionally_independent"]=True
    # Existing-coordinate projection, then known parity, then genuinely new equalities.
    bmap=[{0:F(1)},{0:F(2),1:F(1)}]
    assert project_normal({0:F(-2),1:F(1)},bmap)=={1:F(1)}
    small={};reduce_small({1:F(1)},small,budget,insert="invented_parity")
    residual,_=reduce_small({1:F(3)},small,budget)
    assert not residual
    residual,_=reduce_small({0:F(1),1:F(3)},small,budget,insert="new_original_relation")
    assert residual=={0:F(1)}
    checks["inherited_coordinate_projection_and_only_new_small_equalities_are_distinguished"]=True
    # Resume an unfinished reduction and an unfinished original verification, not old pivots.
    for stage in ("reduce","verify_original"):
        partial=initial_state([],budget)
        for _ in range(2):advance_one_column(partial,columns,transform,diagnostics,budget,r_count=1)
        start_pending(partial,columns,budget)
        pending=partial["pending"]
        if stage=="verify_original":
            while pending["vector"]:
                pending["vector"],pending["combination"]=exact_reduce_step(
                    pending["vector"],pending["combination"],partial["basis"],budget)
                partial["reduction_operations"]+=1
            prepare_verification(pending);verify_original_step(pending,columns,budget)
        for compact in (False,True):
            packed=serialized_state(partial,columns,"artificial_core","artificial_view",{"toy":True},compact)
            restored,info=restore_state(json.loads(canonical(packed)),columns,"artificial_core","artificial_view",{"toy":True},budget)
            assert info["completed_elimination_steps_replayed"]==0
            while restored["cursor"]<columns.count:
                advance_one_column(restored,columns,transform,diagnostics,budget,r_count=1)
            assert restored["relations"]==state["relations"]
            assert restored["independent_original_columns"]==state["independent_original_columns"]
    checks["explicit_and_compact_mid_column_and_mid_verification_states_resume_exactly"]=True
    bad=serialized_state(state,columns,"artificial_core","artificial_view",{"toy":True})
    failed=False
    try:restore_state(bad,columns,"changed_core","artificial_view",{"toy":True},budget)
    except ValueError:failed=True
    assert failed
    checks["continuation_is_bound_to_exact_original_inputs_and_inherited_view"]=True
    atoms=[["jet","toy",0],["int_right",[0,[0]]]]
    hashes=portable_atom_hashes(atoms)
    rows=artificial_root((0,(0,1),-2,3))
    payload=[[0,sorted(hashes[i] for i in (0,1)),-2,3]]
    wanted=sha(json.dumps(payload,separators=(",",":"),ensure_ascii=True).encode())
    assert validate_root(rows,hashes,wanted)["stored_terms"]==1
    failed=False
    try:validate_root(rows,hashes,"0"*64)
    except ValueError:failed=True
    assert failed
    checks["portable_topological_atom_hashes_and_selected_root_original_hashes_are_checked"]=True
    try:
        Budget(30,512,2).check((8,))
        raise AssertionError("bit budget did not stop")
    except Limit:pass
    checks["integer_bit_limit_is_an_explicit_partial_stop_not_a_zero_identity"]=True
    assert all(checks.values())
    return {"all_passed":True,"checks":checks,"artificial_only":True,
        "actual_input_files_opened":False,"old_research_or_old_tests_repeated":False}


def summarize_state(ctx,report):
    state=ctx["state"];columns=ctx["columns"]
    violations={name:[] for name in ctx["diagnostics"]}
    for relation in state["relations"]:
        for name,value in relation["diagnostic_values"].items():
            if value["violates_this_true_equality"]:
                violations[name].append({"relation_index":relation["relation_index"],"exact_value":value["exact_value"]})
    report["literal_comparison"]={"expected_columns":columns.count,"completed_columns":state["cursor"],
        "R_columns_inserted_first":True,"literal_coefficient_basis_size":len(state["basis"]),
        "fresh_original_dependencies":len(state["relations"]),
        "new_equalities_after_archived_B_and_R168":state["new_free_equality_count"],
        "new_exact_elimination_operations":state["reduction_operations"],
        "fresh_original_column_sums":state["fresh_original_column_sums"],
        "pending_stage":None if state["pending"] is None else state["pending"]["stage"],
        "literal_kernel_complete":state["cursor"]==columns.count,
        "functional_kernel_complete_claimed":False,"true_head_dimension_claimed":False}
    report["new_equality_diagnostics"]={name:{"point":[str(v) for v in ctx["diagnostics"][name]],
        "violating_relation_count":len(rows),"first_violations":rows[:8],
        "passes_all_completed_new_equalities":not rows,
        "old_68_halfspaces_rechecked":False,"true_character_existence_claimed":False}
        for name,rows in violations.items()}
    if "state_metadata" in ctx:report["resumable_exact_state"]=ctx["state_metadata"]
    if "certificate_metadata" in ctx:report["fresh_original_relation_certificate"]=ctx["certificate_metadata"]
    metadata=ctx.get("state_metadata",{})
    report["latest_new_progress_has_a_saved_exact_state"]=(
        metadata.get("completed_columns")==state["cursor"]
        and metadata.get("reduction_operations")==state["reduction_operations"]
        and metadata.get("fresh_original_column_sums")==state["fresh_original_column_sums"]
        and metadata.get("active_stage")==report["literal_comparison"]["pending_stage"])


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("head-dir","finite-dir","parity-dir","resume-dir"):
        parser.add_argument("--"+name,type=Path)
    parser.add_argument("--resume-main-sha256")
    parser.add_argument("--resume-publication-sha256")
    parser.add_argument("--diagnose-half-static",action="store_true")
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--toy-only",action="store_true")
    parser.add_argument("--max-seconds",type=float,default=240)
    parser.add_argument("--memory-mib",type=int,default=1024)
    parser.add_argument("--integer-bits",type=int,default=8192)
    parser.add_argument("--checkpoint-every",type=int,default=8)
    parser.add_argument("--max-main-bytes",type=int,default=95000)
    parser.add_argument("--max-state-bytes",type=int,default=4400000)
    parser.add_argument("--max-certificate-bytes",type=int,default=4400000)
    parser.add_argument("--max-total-bytes",type=int,default=4800000)
    parser.add_argument("--max-raw-bytes",type=int,default=40000000)
    args=parser.parse_args()
    if min(args.max_seconds,args.memory_mib,args.integer_bits,args.checkpoint_every,args.max_main_bytes,
           args.max_state_bytes,args.max_certificate_bytes,args.max_total_bytes,args.max_raw_bytes)<=0:
        parser.error("positive explicit budgets required")
    if not args.toy_only:
        if any(getattr(args,name) is None for name in ("head_dir","finite_dir","parity_dir")):
            parser.error("all three exact published input directories are required")
        if args.output.name!=MAIN_NAME:parser.error("actual output basename is fixed for continuation")
    if bool(args.resume_dir)!=(bool(args.resume_main_sha256) and bool(args.resume_publication_sha256)):
        parser.error("resume requires directory and exact published main/receipt SHA256")
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    started=time.monotonic();budget=Budget(args.max_seconds,args.memory_mib,args.integer_bits);ctx={}
    report={"schema":SCHEMA,"source_hashes":source_identity(),"target_weight":-2,
        "github_repository":os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"github_sha":os.environ.get("GITHUB_SHA"),
        "completion":"not_started","phase":"initialization","task_complete":False,
        "original_responses_forcing_profiles_or_path_integrals_evaluated":False,
        "old_RREF_or_LP_solver_recomputed":False,"positive_character_existence_claimed":False,
        "period_or_ruling_paid":False,"literal_nonzero_is_not_functional_nonmembership":True,
        "limits":{k:getattr(args,k) for k in ("max_seconds","memory_mib","integer_bits","checkpoint_every",
            "max_main_bytes","max_state_bytes","max_certificate_bytes","max_total_bytes","max_raw_bytes")}}
    try:
        if args.toy_only:
            report["development"]=toy_only();report.update(completion="complete",phase="new_artificial_checks_complete")
        else:actual(args,report,ctx,budget)
    except (Limit,MemoryError) as error:
        report.update(completion="resource_limit",error={"type":type(error).__name__,"message":str(error)})
    except Exception as error:
        report.update(completion="implementation_check_failed",error={"type":type(error).__name__,"message":str(error)})
    if "state" in ctx:
        try:save_state(ctx,args,report["source_hashes"]["driver"])
        except Exception as error:
            report["state_storage_error"]={"type":type(error).__name__,"message":str(error)}
            if report["completion"]=="complete":report["completion"]="resource_limit"
        try:save_certificate(ctx,args,report)
        except Exception as error:
            report["certificate_storage_error"]={"type":type(error).__name__,"message":str(error)}
            if report["completion"]=="complete":report["completion"]="resource_limit"
        summarize_state(ctx,report)
    report.update(elapsed_seconds=time.monotonic()-started,
        peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,
        budget_checks=budget.operations,maximum_exact_coefficient_bits=budget.maximum_bits)
    raw=canonical(report)
    if len(raw)>args.max_main_bytes:
        report={"schema":SCHEMA,"source_hashes":report["source_hashes"],"completion":"resource_limit",
            "phase":"small_main_output_ceiling","github_repository":report["github_repository"],
            "github_run_id":report["github_run_id"],"github_sha":report["github_sha"],
            "resumable_exact_state":ctx.get("state_metadata"),
            "fresh_original_relation_certificate":ctx.get("certificate_metadata"),
            "task_complete":False,"true_character_existence_claimed":False,
            "original_main_bytes":len(raw),"original_main_sha256":sha(raw)}
        raw=canonical(report)
    atomic_write(args.output,raw)
    print(json.dumps({"output":args.output.name,"completion":report["completion"],
        "phase":report["phase"],"bytes":len(raw),"sha256":sha(raw)}),flush=True)
    return 0 if report["completion"] in ("complete","resource_limit") else 2


if __name__=="__main__":
    raise SystemExit(main())
