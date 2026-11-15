#!/usr/bin/env python3
"""One new pure-image calculation: archived R151 nine plus R186 twelve.

Only standard-library exact row arithmetic is used.  Actual execution requires
public Actions.  No original expression, normalizer, profile, or forcing code
is imported.  The complete new certificate stays in memory and is SHA-bound;
the repository's metadata-only publication rule applies to all output files.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
import os
from pathlib import Path
import resource
import sys
import tempfile
import time

SCHEMA = "visible-flex-pure-minus2-archived-projection-v1"
REPO = "Rogerhu12/math-research-public"
ANCHOR = "I(F)=integral_r^xi F; all input colors zero on the same right collar"
R_POS = [0, 1, 2, 3, 8, 9, 10, 12, 19]
R_GLOBAL = [0, 48, 88, 112, 41, 73, 81, 193, 170]
U_POS = [40, 41, 42, 43, 44, 45, 46, 49, 51, 52, 54, 58]
U_NORMAL = [0, 1, 2, 4, 5, 7, 8, 23, 28, 30, 38, 46]
JOINT_BASIS = list(range(40)) + U_POS
ORIGINAL147 = list(range(40)) + [40,41,42,44,45,47,48,50,60,63,65,68,70,71,78,80,83,85,86,88,93,98,103,109,111,112,113,115,117,130,131,132,137,138,140,141,143]
WORD = {
    "run":"43676765171", "commit":"ca4e52869123fa97df4560232a03f9529cf05332",
    "lane":"character_head_word_relations",
    "schema":"visible-flex-character-head-fixed-color-word-relations-v1",
    "main":("character-head-word-relations-certificate.json.gz",773910,"fec2d558a1241a4e0beaedcd80fd03395f7c87bce028cb65357cb804bf434685"),
    "raw":(3936105,"88baa9dd0ff0ed3d992d67846cbcb2553b68b455ed99b24cfca926ca382d7647"),
    "report":("character-head-word-relations.json",12724,"68bf26fc88ffea61f5be2e17e11324540f58ff0a4c71f59b87428caef38c1341"),
    "receipt":("receipt.json",43019,"1e4faea0f993c36021fc769c9e66c313f6e131f8d2d2add418143d14ed724dfa"),
    "driver":("literature_character_head_word_relations.py",79108,"1ec5fab96ec173c3e1583b40a124c5c98b3249cec9a87be39db3b3066e31b300"),
    "suffix":"-certificate", "export_key":"new_original_relation_certificate"}
PURE = {
    "run":"43657785023", "commit":"c606688a842bd811106ff2844e1161a4f34c159e",
    "lane":"general_pure_J_membership",
    "schema":"visible-flex-general-pure-J-complete-response-membership-v1",
    "main":("general-pure-J-membership-certificate.json.gz",84283,"af46437f676716a20051bf3bad5a96235398dcf8a45c179d1395bc1f9d84712e"),
    "raw":(456216,"9859368ec20e0923cc168199a7ecb82eff0beac5fa191f1b6388e67cfd1aa550"),
    "report":("general-pure-J-membership.json",45019,"98442251ed15b708a70e3fcbbdb2ae6cf76c8c1873aa21345354a5a320a9cfac"),
    "receipt":("receipt.json",35841,"31d6380160437b0098d33d35e4b722c79cd780d351f614a4e48901100a9d0fa4"),
    "driver":("literature_general_pure_J_membership.py",37092,"1a84590f8b6f0c35a1df5f251a8ffa0e9f4da65ea2cc3bd777e752482ef05bcc"),
    "suffix":"-original-expressions", "export_key":"portable_original_certificate"}


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()


def sha(payload):
    return hashlib.sha256(payload).hexdigest()


class BudgetExit(RuntimeError):
    pass


class Limits:
    def __init__(self,seconds=120,memory_mib=512,bits=16384,operations=2000000):
        self.start=time.monotonic();self.seconds=seconds;self.memory=memory_mib
        self.bits=bits;self.maximum_bits=0;self.operations=0;self.max_operations=operations
    def check(self):
        if time.monotonic()-self.start>self.seconds:raise BudgetExit("elapsed_seconds")
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024>self.memory:raise BudgetExit("rss_mib")
        if self.operations>self.max_operations:raise BudgetExit("sparse_arithmetic_operations")
    def rational(self,x):
        self.operations+=1
        n=max(x.numerator.bit_length(),x.denominator.bit_length())
        self.maximum_bits=max(self.maximum_bits,n)
        if n>self.bits:raise BudgetExit("rational_bit_length")
        if self.operations%256==0:self.check()
        return x


def read_exact(path,entry):
    name,size,digest=entry
    p=Path(path)/name
    if p.stat().st_size!=size:raise ValueError("bound byte count: "+name)
    payload=p.read_bytes()
    if sha(payload)!=digest:raise ValueError("bound SHA256: "+name)
    return payload


def verify_receipt(pub,spec,report,certificate):
    if (pub.get("schema")!="visible-new-mechanism-actions-v1" or pub.get("repository")!=REPO
        or str(pub.get("run_id"))!=spec["run"] or pub.get("source_commit")!=spec["commit"]
        or pub.get("lane")!=spec["lane"]):raise ValueError("publication identity mismatch")
    for data,suffix in ((report,""),(certificate,spec["suffix"])):
        if (data.get("schema")!=spec["schema"]+suffix or data.get("github_repository")!=REPO
            or str(data.get("github_run_id"))!=spec["run"] or data.get("github_sha")!=spec["commit"]):
            raise ValueError("embedded identity mismatch")
    if report.get("completion")!="complete":raise ValueError("source calculation incomplete")
    if certificate.get("source_hashes")!=report.get("source_hashes"):raise ValueError("source table mismatch")
    name,size,digest=spec["driver"]
    driver=report["source_hashes"]["driver"]
    if driver!={"filename":name,"bytes":size,"sha256":digest}:raise ValueError("producer changed")
    source=pub["source_files"].get("topics/visible-flex-new-mechanism/scripts/"+name)
    if not source or source.get("bytes")!=size or source.get("sha256")!=digest:raise ValueError("receipt source mismatch")
    output={Path(row["path"]).name:row for row in pub["outputs"]}
    for entry in (spec["report"],spec["main"]):
        name,size,digest=entry;rec=output.get(name,{})
        if rec.get("bytes")!=size or rec.get("sha256")!=digest:raise ValueError("receipt output mismatch")
    rec=output[spec["main"][0]]
    if (rec.get("raw_bytes"),rec.get("raw_sha256"))!=spec["raw"]:raise ValueError("receipt raw identity mismatch")
    rec=report[spec["export_key"]]
    expected={"filename":spec["main"][0],"stored_bytes":spec["main"][1],"stored_sha256":spec["main"][2],
        "raw_bytes":spec["raw"][0],"raw_sha256":spec["raw"][1]}
    if any(rec.get(k)!=v for k,v in expected.items()):raise ValueError("report export identity mismatch")


def load_bound(directory,spec,limits):
    report=json.loads(read_exact(directory,spec["report"]))
    pub=json.loads(read_exact(directory,spec["receipt"]))
    packed=read_exact(directory,spec["main"])
    payload=gzip.decompress(packed)
    if (len(payload),sha(payload))!=spec["raw"]:raise ValueError("decompressed identity mismatch")
    data=json.loads(payload);verify_receipt(pub,spec,report,data);limits.check()
    return report,data


def local_key(raw,colors=("q",)):
    if not isinstance(raw,list) or len(raw)!=2 or type(raw[0]) is not int or raw[0]<0:
        raise ValueError("invalid local polynomial monomial")
    jets=[]
    for pair in raw[1]:
        if (not isinstance(pair,list) or len(pair)!=2 or pair[0] not in colors
            or type(pair[1]) is not int or pair[1]<0):raise ValueError("invalid color/jet")
        jets.append(tuple(pair))
    if jets!=sorted(jets):raise ValueError("unsorted local jet multiset")
    return raw[0],tuple(jets)


def remainder_letter(key):
    if not key[1]:return False
    color=max(c for c,j in key[1]);order=max(j for c,j in key[1] if c==color)
    return order==0 or key[1].count((color,order))>=2


def decode_rows(payload,limits,weight=-2):
    if len(payload)>100000:raise BudgetExit("stored_rows")
    out={};previous=None
    for local,word,n,d in payload:
        key=(local_key(local),tuple(local_key(letter) for letter in word))
        if any(not remainder_letter(letter) for letter in key[1]):raise ValueError("outside R178 remainder grammar")
        if (type(n) is not int or type(d) is not int or not n or d<=0
            or (previous is not None and key<=previous)):raise ValueError("invalid word coefficient/order")
        coeff=F(n,d)
        if (coeff.numerator,coeff.denominator)!=(n,d):raise ValueError("noncanonical Fraction")
        pieces=(key[0],)+key[1]
        if sum(len(a[1]) for a in pieces)!=4:raise ValueError("not pure quartic")
        degree=sum(a[0]-sum(j for c,j in a[1]) for a in pieces)+len(key[1])
        if degree!=weight:raise ValueError("wrong actual affine weight")
        out[key]=limits.rational(coeff);previous=key
    return out


def rows(terms):
    return [[key[0],key[1],v.numerator,v.denominator] for key,v in sorted(terms.items())]


def sparse_coefficients(terms):
    return [[i,str(v)] for i,v in sorted(terms.items())]


def add_scaled(target,source,factor,limits):
    if not factor:return dict(target)
    out=dict(target)
    for key,value in source.items():
        new=limits.rational(out.get(key,F(0))+factor*value)
        if new:out[key]=new
        else:out.pop(key,None)
    return out


def scaled(source,factor,limits):
    return {key:limits.rational(value*factor) for key,value in source.items() if value*factor}


def reduce_pair(value,combination,basis,limits):
    value=dict(value);combination=dict(combination)
    for item in basis:
        amount=value.get(item["pivot"],F(0))
        if amount:
            value=add_scaled(value,item["value"],-amount,limits)
            combination=add_scaled(combination,item["combination"],-amount,limits)
    return value,combination


def install(value,combination):
    if not value:raise ValueError("inherited independent basis became dependent")
    pivot=min(value);factor=value[pivot]
    return pivot,factor


def verify_combination(expected,combination,original,limits):
    total={}
    for label,coef in combination.items():total=add_scaled(total,original[label],coef,limits)
    if total!=expected:raise ArithmeticError("new row identity does not sum from the archived original representatives")
    return {"exact_sum_checked":True,"remainder_terms":0,"original_representative_sum_sha256":sha(canonical(rows(total)))}


def prepare_known_basis(original,labels,limits):
    basis=[]
    for label in labels:
        value,combination=reduce_pair(original[label],{label:F(1)},basis,limits)
        pivot,factor=install(value,combination)
        basis.append({"pivot":pivot,"value":scaled(value,1/factor,limits),
            "combination":scaled(combination,1/factor,limits),"original_column":label})
    return basis


def new_projection(original,known_labels,new_labels,limits,progress):
    # The first nine are a known true basis, prepared only as a solving interface.
    old=prepare_known_basis(original,known_labels,limits);extra=[];records=[]
    for label in new_labels:
        old_residue,old_comb=reduce_pair(original[label],{label:F(1)},old,limits)
        member=not old_residue
        remainder,comb=reduce_pair(old_residue,old_comb,extra,limits)
        row={"original_77_column":label,"member_of_inherited_R_pure_image":member,
            "old_nine_residual_terms":len(old_residue),
            "old_nine_residual_sha256":sha(canonical(rows(old_residue))),
            "new_pure_quotient_basis_column":bool(remainder)}
        if member:
            row["coefficients_in_original_R40_positions"] = sparse_coefficients({i:-v for i,v in old_comb.items() if i!=label})
        if remainder:
            pivot,factor=install(remainder,comb)
            value=scaled(remainder,1/factor,limits);comb=scaled(comb,1/factor,limits)
            row["pivot_word"]=pivot;row["pivot_before_normalization"]=str(factor)
            row["normalized_residual_original_combination"]=sparse_coefficients(comb)
            row["fresh_stored_word_sum"]=verify_combination(value,comb,original,limits)
            extra.append({"pivot":pivot,"value":value,"combination":comb,"original_column":label})
        else:
            row["exact_original_column_relation"]=sparse_coefficients(comb)
            row["fresh_stored_word_sum"]=verify_combination({},comb,original,limits)
        if old_residue:
            row["nonmembership_in_old_pure_image_is_true_by_R179"]=True
        records.append(row);progress["new_columns_completed"]=len(records)
        progress["new_quotient_rank_lower_bound"]=len(extra);limits.check()
    return old,extra,records


def check_inherited(word_report,word,pure_report,pure,limits):
    if (word.get("anchor")!=ANCHOR or word.get("target_weight")!=-2
        or word.get("completed_column_prefix")!=77 or word.get("all_77_columns_processed") is not True
        or word_report.get("all_77_columns_processed") is not True):raise ValueError("complete R186 source required")
    if word["original147_basis_indices"]!=ORIGINAL147:raise ValueError("R174 basis mapping changed")
    if word["shared_representative_matrix_basis_columns"]!=JOINT_BASIS:raise ValueError("R186 genuine basis changed")
    if word["shared_representative_matrix_rank_on_completed_prefix"]!=52:raise ValueError("R186 rank binding")
    deps=word["exact_original_relations"]
    if len(deps)!=25 or sorted(a["dependent_basis_column"] for a in deps)!=[i for i in range(77) if i not in JOINT_BASIS]:
        raise ValueError("R186 inherited coverage changed")
    if not all(a.get("complete_canonical_original_identity_proved") is True and a.get("all_two_faithful_root_sums_exactly_zero") is True for a in deps):
        raise ValueError("an inherited joint identity was not completed")
    upper=pure["pure_response_upper_bound"]
    if (upper!=pure_report["pure_response_upper_bound"] or upper["retained_original_positions"]!=R_POS
        or upper["retained_global_R116_columns"]!=R_GLOBAL
        or upper["new_original_pure_dependencies_verified"]!=31
        or upper["proved_true_pure_dimension_upper_bound"]!=9):raise ValueError("R151 nine-basis binding")
    pdeps=pure["new_pure_dependency_proofs"]
    if (len(pdeps)!=31 or sorted(a["dependent_original_position"] for a in pdeps)!=[i for i in range(40) if i not in R_POS]
        or not all(a.get("original_identity_proved") is True and a["fresh_original_normal_form"]["terms"]==0 for a in pdeps)):
        raise ValueError("R151 inherited pure coverage changed")
    if word["inputs"]["pure_R40_and_J"]["artifact"]["raw_sha256"]!=PURE["raw"][1]:raise ValueError("cross-source R151 binding")
    columns=word["completed_original_to_word_conversions"];metadata=word["original_conversion_metadata"]
    if len(columns)!=77 or len(metadata)!=77:raise ValueError("R186 column inventory")
    archive={a["original_position"]:a for a in pure["pure_column_representatives"]}
    if set(archive)!=set(range(40)):raise ValueError("R151 stored inventory")
    original={};binding=[]
    for j,(column,meta) in enumerate(zip(columns,metadata)):
        if (column["column"]!=j or column["original147_index"]!=ORIGINAL147[j]
            or meta["index"]!=j or meta["original147_index"]!=ORIGINAL147[j]):raise ValueError("column identity changed")
        for mode in ("-4","-2"):
            payload=column["projections"][mode];conversion=column["conversions"][mode]
            if (conversion["column"]!=j or conversion["original147_index"]!=ORIGINAL147[j]
                or conversion["mode"]!=int(mode) or conversion["word_terms"]!=len(payload)
                or conversion["word_rows_sha256"]!=sha(canonical(payload))
                or conversion["original_mode_sha256"]!=meta["binding"][mode]["original_sha256"]):
                raise ValueError("stored conversion identity mismatch")
            for flag in ("same_common_physical_right_anchor","every_word_letter_is_an_R178_fixed_color_remainder","representative_is_an_original_function_identity"):
                if conversion.get(flag) is not True:raise ValueError("missing source theorem precondition")
        conv=column["conversions"]["-4"]
        if conv["projected_original_sha256"]!=conv["original_mode_sha256"]:raise ValueError("pure root projection changed")
        if j<40 and conv["original_mode_sha256"]!=archive[j]["original_sha256"]:raise ValueError("R151-to-R186 original pure root mismatch")
        if j in R_POS+U_POS:
            if j in U_POS and meta["normal_index"]!=U_NORMAL[U_POS.index(j)]:raise ValueError("new quotient basis label changed")
            original[j]=decode_rows(column["projections"]["-4"],limits)
            binding.append({"original_77_column":j,"normal_index":meta["normal_index"],
                "original147_index":ORIGINAL147[j],"original_pure_sha256":conv["original_mode_sha256"],
                "stored_word_sha256":conv["word_rows_sha256"],"stored_word_terms":conv["word_terms"]})
        limits.check()
    return original,binding


def actual(args,report,limits):
    if (os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPO
        or not os.environ.get("GITHUB_RUN_ID") or not os.environ.get("GITHUB_SHA")):
        raise ValueError("actual archived target is public-Actions-only")
    report["phase"]="read_bound_archived_sources"
    wm,w=load_bound(args.word_dir,WORD,limits);pm,p=load_bound(args.pure_dir,PURE,limits)
    original,binding=check_inherited(wm,w,pm,p,limits)
    report["input_original_columns"]=binding
    report["inheritance"]={"R186_joint_basis_dimension":52,"R186_joint_relations_consumed_without_recomputation":25,
        "R151_pure_R_dimension":9,"R151_pure_relations_consumed_without_recomputation":31,
        "R186_all_77_stored_bindings_checked":True,"new_originals_decoded":False}
    del wm,w,pm,p
    report["phase"]="twelve_new_pure_membership_and_quotient_columns"
    old,extra,records=new_projection(original,R_POS,U_POS,limits,report["progress"])
    r=len(extra)
    report["new_column_results"]=records
    report["mathematical_result"]={"complete_new_target":True,"inherited_pure_R_dimension":9,
        "true_pure_U_minus2_dimension":9+r,"true_pure_quotient_dimension":r,
        "all_pure_U_minus2_is_pure_R_minus2":r==0,"true_kernel_of_pure_on_U_minus2_dimension":43-r,
        "true_kernel_of_pure_on_R_minus2_dimension":31,
        "true_kernel_dimension_of_induced_U_over_R_to_pure_quotient":12-r,
        "new_independent_quotient_original77_columns":[a["original_column"] for a in extra],
        "source_of_true_function_independence":"R179, with R178 sound same-anchor identities",
        "full_period_or_ruling_paid":False,"finite_geometric_control_constructed":False,
        "fixed_profile_nonmembership_claimed":False}
    cert={"schema":SCHEMA+"-in-memory-certificate","inputs":report["inputs"],
        "source":report["source_hashes"],"input_original_columns":binding,"anchor":ANCHOR,
        "inherited_known_basis":[{"column":a["original_column"],"pivot":a["pivot"],
            "normalized_rows":rows(a["value"]),"original_combination":sparse_coefficients(a["combination"])} for a in old],
        "new_quotient_basis":[{"column":a["original_column"],"pivot":a["pivot"],
            "normalized_rows":rows(a["value"]),"original_combination":sparse_coefficients(a["combination"])} for a in extra],
        "new_column_results":records,"result":report["mathematical_result"]}
    payload=canonical(cert)
    if len(payload)>5000000:raise BudgetExit("in_memory_certificate_bytes")
    report["in_memory_certificate"]={"bytes":len(payload),"sha256":sha(payload),"saved":False,
        "reproduce_from_this_script_and_frozen_parameters":True}
    report["phase"]="complete";report["completion"]="complete"
    report["outcome"]="pure_images_equal" if r==0 else "new_true_pure_quotient_found"


def artificial():
    limits=Limits(30,512,16384);checks=[]
    def good(name,condition):
        if not condition:raise AssertionError(name)
        checks.append(name)
    def rejects(name,fn):
        try:fn()
        except (ValueError,ArithmeticError):checks.append(name);return
        raise AssertionError(name)
    key=lambda i:((i,()),())
    o={0:{key(0):F(2),key(1):F(1)},1:{key(1):F(3),key(2):F(1)}}
    o[2]=add_scaled(scaled(o[0],F(3,7),limits),o[1],F(-2,5),limits)
    o[3]={key(3):F(5)};o[4]=add_scaled(o[3],o[0],F(11,3),limits);o[5]={key(4):F(-7)}
    progress={};old,new,rec=new_projection(o,[0,1],[2,3,4,5],limits,progress)
    good("exact_fraction_member",rec[0]["coefficients_in_original_R40_positions"]==[[0,"3/7"],[1,"-2/5"]])
    good("new_quotient_rank_two",[a["original_column"] for a in new]==[3,5])
    good("nonmember_dependent_on_prior_new",not rec[2]["member_of_inherited_R_pure_image"] and not rec[2]["new_pure_quotient_basis_column"])
    good("all_new_relations_freshly_sum",all(a["fresh_stored_word_sum"]["exact_sum_checked"] for a in rec))
    good("input_vectors_not_mutated",o[0]=={key(0):F(2),key(1):F(1)} and o[3]=={key(3):F(5)})
    e0=[0,[["q",0],["q",0],["q",1],["q",1]]]
    payload=[[e0,[],1,3]];decoded=decode_rows(payload,limits)
    good("pure_quartic_weight_and_roundtrip",canonical(rows(decoded))==canonical(payload))
    rejects("unreduced_fraction_rejected",lambda:decode_rows([[e0,[],2,6]],limits))
    rejects("foreign_pure_color_rejected",lambda:decode_rows([[[0,[["qbar",0]]],[],1,1]],limits))
    rejects("nonremainder_letter_rejected",lambda:decode_rows([[[0,[["q",0],["q",0]]],[[0,[["q",1],["q",2]]]],1,1]],limits))
    rejects("wrong_weight_rejected",lambda:decode_rows([[[1,e0[1]],[],1,1]],limits))
    rejects("incorrect_new_identity_rejected",lambda:verify_combination({}, {0:F(1)},o,limits))
    rejects("dependent_inherited_basis_rejected",lambda:prepare_known_basis({0:{0:F(1)},1:{0:F(2)}},[0,1],limits))
    with tempfile.TemporaryDirectory() as d:
        data=b'{"artificial":true}\n';p=Path(d)/"toy.json";p.write_bytes(data)
        good("exact_input_byte_binding",read_exact(d,(p.name,len(data),sha(data)))==data)
        rejects("bad_bound_sha_rejected",lambda:read_exact(d,(p.name,len(data),"0"*64)))
    spec={"run":"7","commit":"toy-commit","lane":"toy-lane","schema":"toy-schema",
        "driver":("toy.py",3,"driver-digest"),"report":("toy.json",4,"report-digest"),
        "main":("toy.gz",5,"packed-digest"),"raw":(6,"raw-digest"),
        "suffix":"-certificate","export_key":"export"}
    driver={"filename":"toy.py","bytes":3,"sha256":"driver-digest"}
    embedded={"github_repository":REPO,"github_run_id":"7","github_sha":"toy-commit",
        "source_hashes":{"driver":driver}}
    report={**embedded,"schema":"toy-schema","completion":"complete","export":{
        "filename":"toy.gz","stored_bytes":5,"stored_sha256":"packed-digest",
        "raw_bytes":6,"raw_sha256":"raw-digest"}}
    certificate={**embedded,"schema":"toy-schema-certificate"}
    pub={"schema":"visible-new-mechanism-actions-v1","repository":REPO,"run_id":"7",
        "source_commit":"toy-commit","lane":"toy-lane",
        "source_files":{"topics/visible-flex-new-mechanism/scripts/toy.py":driver},
        "outputs":[{"path":"toy.json","bytes":4,"sha256":"report-digest"},
            {"path":"toy.gz","bytes":5,"sha256":"packed-digest","raw_bytes":6,"raw_sha256":"raw-digest"}]}
    verify_receipt(pub,spec,report,certificate)
    good("synthetic_publication_binding",True)
    rejects("wrong_publication_run_rejected",lambda:verify_receipt({**pub,"run_id":"8"},spec,report,certificate))
    good("no_research_input_access",True)
    return {"all_passed":True,"checks":checks,"research_inputs_read":0,
        "real_rank_or_profile_calculations":0,"synthetic_only":True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy",action="store_true")
    parser.add_argument("--word-dir",type=Path)
    parser.add_argument("--pure-dir",type=Path)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--seconds",type=float,default=120)
    parser.add_argument("--memory-mib",type=int,default=512)
    parser.add_argument("--rational-bits",type=int,default=16384)
    args=parser.parse_args()
    if args.seconds<=0 or args.memory_mib<128 or args.rational_bits<256:parser.error("invalid budget")
    if not args.toy and (args.word_dir is None or args.pure_dir is None):parser.error("actual needs both frozen source directories")
    self_path=Path(__file__);source=self_path.read_bytes();limits=Limits(args.seconds,args.memory_mib,args.rational_bits)
    report={"schema":SCHEMA,"github_repository":os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"github_sha":os.environ.get("GITHUB_SHA"),
        "source_hashes":{"driver":{"filename":self_path.name,"bytes":len(source),"sha256":sha(source)}},
        "inputs":{"R186":WORD,"R151":PURE},"phase":"start","completion":"not_started","progress":{},
        "limits":{"seconds":args.seconds,"memory_mib":args.memory_mib,"rational_bits":args.rational_bits,
            "memory_limit_is_polled":True,"in_memory_certificate_bytes":5000000},
        "work_scope":{"new_projection_columns":12,"inherited_pure_basis_columns":9,
            "old_40_or_77_column_elimination_repeated":False,"old_31_or_25_identities_recomputed":False,
            "normal_form_or_original_DAG_restored":False,"new_profile_or_geometry_evaluated":False,
            "response_or_forcing_recompiled":False,"machine_data_published":False}}
    exit_code=0
    try:
        if args.toy:
            report["artificial_development"]=artificial();report["completion"]="toy_passed";report["phase"]="toy_complete"
        else:actual(args,report,limits)
    except BudgetExit as exc:
        report.update(completion="budget_exhausted",failure=str(exc));exit_code=2
    except Exception as exc:
        report.update(completion="implementation_check_failed",failure=type(exc).__name__+": "+str(exc));exit_code=1
    report["elapsed_seconds"]=time.monotonic()-limits.start
    report["peak_rss_mib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    report["maximum_rational_bits"]=limits.maximum_bits;report["sparse_arithmetic_operations"]=limits.operations
    payload=canonical(report)+b"\n"
    if len(payload)>95000:
        report["detailed_report_bytes"]=len(payload);report["detailed_report_sha256"]=sha(payload)
        report["details_omitted_from_small_report"]=["new_column_results","input_original_columns"]
        report.pop("new_column_results",None);report.pop("input_original_columns",None)
        payload=canonical(report)+b"\n"
    if len(payload)>95000:raise RuntimeError("small report exceeds the explicit output bound")
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_bytes(payload)
    if report.get("mathematical_result",{}).get("complete_new_target"):
        print("MATHEMATICAL_RESULT "+json.dumps(report["mathematical_result"],sort_keys=True,separators=(",",":")),flush=True)
        for row in report.get("new_column_results",[]):print("MATHEMATICAL_COLUMN "+json.dumps(row,sort_keys=True,separators=(",",":")),flush=True)
    print("REPORT_SHA256 "+sha(payload)+" BYTES "+str(len(payload))+" COMPLETION "+report["completion"],flush=True)
    if "in_memory_certificate" in report:print("CERTIFICATE_METADATA "+json.dumps(report["in_memory_certificate"],sort_keys=True),flush=True)
    return exit_code


if __name__=="__main__":
    sys.exit(main())
