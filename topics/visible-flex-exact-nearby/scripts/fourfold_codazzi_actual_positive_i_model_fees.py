"""Whole original +i candidate readback and the new signed-model primitive fees."""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

TOPIC="topics/visible-flex-exact-nearby"
NOTES=TOPIC+"/notes/"
SOURCE=TOPIC+"/scripts/fourfold_codazzi_actual_positive_i_model_fees.py"
WF=".github/workflows/visible-exact-original-positive-i-model-fees.yml"
FIRST=97
SPLIT=1024
TAIL=2**34
GROUP_CAP=F(32,25)
NATIVE_PATH=NOTES+"first_symbol_quadratic_gap_ci/run-43598755503-1/consumers/first-symbol-quadratic-gap.json.gz"
NATIVE_COMMIT="d564ebaa49ae933cc1322f1b2f39e4bcacafd1e5"
NATIVE_SHA="db861442f5b895362abe090306c2899b3771282269b7ccc5743d820e79f8bff3"
FILES={
    "rules":(NOTES+"2026-11-28-read-public-model-ultra-rules.json","32fa03fbdb357d7d5a98b7115a24acc10f218705a1ecdef2e756ff73284098ce"),
    "process":(NOTES+"first_symbol_quadratic_gap_ci/run-43598755503-1/consumers/process.json","afa699e3e86fc1d6678c35606b116dd8074a6ce7adfca246d8804532e32e0f0b"),
    "publication":(NOTES+"first_symbol_quadratic_gap_ci/run-43598755503-1/publication.json","497e1bd37fa9f7fada95c9802a6538ff3bfcbc68537b44a51d57a8b10b3b16b7"),
    "CYA":(NOTES+"finite_Cayley_scalar_gap_ci/run-43757868884-1/actual-scientific-conclusion.json","1f08e281eeff6bd09b0118f71adf17b1e5842ffc1cb71ebc9c8c78e5582bd20d"),
    "CYA_execution":(NOTES+"finite_Cayley_scalar_gap_ci/run-43757868884-1/execution.json","3f3947926f2f7ded20d1333fde2d9d197c02f996cd1f9bbf224a73d764e08a71")}


def require(ok,message):
    if not ok:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encode(obj):
    return (json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=False)+"\n").encode()


def lower(text):
    if not text.startswith("["):
        return F(text)
    match=re.fullmatch(r"\[([^ ]+) \+/- ([^ ]+)\]",text)
    require(match is not None,"complete finite decimal ball")
    midpoint,radius=map(F,match.groups())
    require(radius>=0,"outward original whole-record radius")
    return midpoint-radius


def fees(n,g):
    return [g,g/F(4*n),g**3/F(4*n)]


def upper_fees(records):
    return dict(zip(("I_G","I_squared_G","homogeneous_minus_four_thirds_G_cubed"),
                    (str(max(row[k] for row in records)) for k in range(3))))


def arithmetic(inputs, native):
    p,c,e=inputs["process"],inputs["CYA"],inputs["CYA_execution"]
    require(p["complete"] and p["actual_returncode"]==0 and p["mathematical_complete"]
            and p["mathematical_gates"]==11 and p["native_sha256"]==NATIVE_SHA
            and c["complete"] and c["actual_returncode"]==0 and c["proved"]
            and e["complete"] and c["run_id"]=="43757868884" and p["run_id"]=="43598755503",
            "original actual all-integer norm and actual finite Cayley conclusions")
    ndata=json.loads(gzip.decompress(native))
    require(ndata["complete"] and ndata["complete_finite_candidates"]==p["complete_finite_candidates"]==1502
            and len(ndata["candidates"])==1502 and ndata["candidate_counts_by_fourth_root"]==p["candidate_counts_by_fourth_root"]
            and len(ndata["gates"])==11 and all(x["passed"] for x in ndata["gates"]),"whole original 1502-candidate certificate")
    records=c["complete_new_finite_Cayley_conclusion"]["complete_group_minima"]
    group,=[x for x in records if x["sign"]==1 and x["fourth_root_index"]==1]
    require(len(records)==8 and group["count"]==927 and group["complete_witness"]["index"]==190,
            "old complete positive-frequency +i Cayley group")
    low_g=1/(2*lower(group["complete_weighted_distance_lower"]["lower"]))
    require(low_g<F(573,1000),"saved sharp simultaneous original group")
    counts=[0]*4
    candidates={}
    for row in ndata["candidates"]:
        n,r=row["index_n"],row["fourth_root_residue"]
        require(FIRST<=n<TAIL and r==int(row["exact_P"])%4 and int(row["exact_N"])==4*n,
                "whole existing index and fourth-root residue")
        counts[r]+=1
        if r==1 and n>=SPLIT:
            d=lower(row["full_coefficient_distance_lower"]["lower"])
            require(d>0,"full old positive interval separation")
            candidates[n]=min(candidates.get(n,F(1,16)),d)
    require(counts==[int(p["candidate_counts_by_fourth_root"][str(i)]) for i in range(4)]
            and counts[1]==372,"every original quadrant and all 372 relevant candidate pairs")
    def bound(n,d):
        chord=F(157,25)*d-F(19**3,12*n*n)
        require(chord>0,"strict positive complete Cayley chord after original uniform residual")
        return 1/(2*chord)
    tail_g=F(3,5)
    uniform_g=bound(SPLIT,F(1,16))
    require(uniform_g<GROUP_CAP and lower(p["limiting_norm_interval"]["lower"])>105,"unlisted full-frequency chord and old limiting norm lower")
    # Interval upper is a directed-endpoint ball: its negation is bounded by
    # negating its midpoint and subtracting the complete radius.
    text=p["limiting_norm_interval"]["upper"]
    if text.startswith("["):
        centre,radius=re.fullmatch(r"\[([^ ]+) \+/- ([^ ]+)\]",text).groups()
        up=F(centre)+F(radius)
    else:
        up=F(text)
    poly=p["exact_integer_polynomial"]
    a,b,k=(int(poly[key]) for key in ("a","b","c"))
    require(up<106 and a%4==3 and a%5==b%5==0 and k%5==4 and a<2**54
            and 16*a*F(16,5)**2/TAIL**2<F(1,64)
            and F(16*9,4)*F(2,15)+F(1,64)<5 and 2*(F(157,25)*F(2,15)-F(19**3,12*TAIL**2))>F(1,tail_g),
            "the complete +i infinite tail norm congruences and outward chord bound")
    # |b_phase| < 3, so a hypothetical |u-b_phase| <= 2/15 gives |u| < 16/5.
    require(lower(p["phase_coefficient_interval"]["lower"])>0
            and F(p["phase_coefficient_interval"]["upper"])<3,
            "complete old reduced phase interval below 3")
    resolved={n:bound(n,d) for n,d in candidates.items()}
    exceptions={n:g for n,g in resolved.items() if g>GROUP_CAP}
    generic=[fees(FIRST,low_g),fees(SPLIT,uniform_g),fees(TAIL,tail_g)]
    all_fees=generic+[fees(n,g) for n,g in resolved.items()]
    safe=generic+[fees(n,g) for n,g in resolved.items() if n not in exceptions]
    bands=[]
    for lo,hi in [(97,1024),(1024,4096),(4096,65536),(65536,2**20),(2**20,2**34)]:
        common=fees(lo,low_g if lo==97 else bound(lo,F(1,16)))
        bands.append({"original_first_index":lo,"exclusive_stop":hi,
            "whole_input_fees":upper_fees([common]+[fees(n,g) for n,g in resolved.items() if lo<=n<hi]),
            "exceptional_coordinates":[n for n in sorted(exceptions) if lo<=n<hi]})
    return {"old_complete_quadrant_cardinalities":counts,"all_raw_candidate_bytes":len(native),
        "positive_i_actual_original_minimum_witness":190,"exact_nonexceptional_threshold":str(GROUP_CAP),
        "all_integer_primitive_fees":upper_fees(all_fees),"safe_primitive_fees":upper_fees(safe),
        "all_exceptional_positive_coordinates":[{"n":n,"I_G_upper":str(exceptions[n])} for n in sorted(exceptions)],
        "complete_retained_ordinary_dimension_including_original96":96+len(exceptions),"complete_finite_bands":bands,
        "tail_start":TAIL,"tail_primitive_fees":upper_fees([fees(TAIL,tail_g)]),
        "old_candidate_generation_calls":0,"old_Cayley_finite_distance_calls":0,"new_large_arrays_published":0}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--source-sha",required=True)
    args=parser.parse_args()
    root=args.repo.resolve()
    require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ["GITHUB_REPOSITORY"]=="Rogerhu12/math-research-public"
            and os.environ["GITHUB_RUN_ATTEMPT"]=="1" and os.environ["GITHUB_EVENT_NAME"]=="push",
            "one original new public research job")
    def git(*args):
        return subprocess.check_output(["git",*args],cwd=root)
    event=os.environ["GITHUB_SHA"]
    require(git("rev-parse","HEAD").decode().strip()==event and
            git("diff-tree","--no-commit-id","--name-status","-r",event,"--",WF).decode().strip()=="A\t"+WF
            and git("log","--full-history","--diff-filter=A","--format=%H",event,"--",WF).decode().splitlines()==[event],
            "only the first natural additive workflow commit can consume this arithmetic")
    require(sha((root/SOURCE).read_bytes())==args.source_sha==sha(git("show",event+":"+SOURCE)),"whole actual source")
    inputs={}
    for role,(path,digest) in FILES.items():
        raw=(root/path).read_bytes()
        require(sha(raw)==digest and raw==git("show",event+":"+path),"whole current signed input: "+role)
        inputs[role]=json.loads(raw)
    review=inputs["rules"]
    git("fetch","--no-tags","--filter=blob:none","origin","main")
    head=git("rev-parse","origin/main").decode().strip()
    for path,digest in review["readme_sha256"].items():
        require(sha(git("show",head+":"+path))==digest,"current README still matches reviewed rule16: "+path)
    require(not git("diff",review["read_commit"],head,"--",*review["readme_sha256"]),
            "no unread rule change before new science")
    native=git("show",NATIVE_COMMIT+":"+NATIVE_PATH)
    require(len(native)==198079 and sha(native)==NATIVE_SHA and
            any(x["file"]=="consumers/first-symbol-quadratic-gap.json.gz" and x["bytes"]==len(native)
                and x["sha256"]==NATIVE_SHA for x in inputs["publication"]["files"]),
            "single complete original native brought back only as required")
    result=arithmetic(inputs,native)
    result.update(kind="R149_ASQ11_actual_all_frequency_positive_i_primitive_fees_v1",
        run=os.environ["GITHUB_RUN_ID"],attempt="1",actual_event=event,reviewed_head=head,
        source_sha256=args.source_sha,whole_original_native_sha256=NATIVE_SHA,
        whole_current_input_sha256={k:v[1] for k,v in FILES.items()},complete=True)
    raw=encode(result)
    print("ASQ11 COMPLETE SMALL CONCLUSION bytes="+str(len(raw))+" sha256="+sha(raw),flush=True)
    print(raw.decode(),end="",flush=True)


if __name__=="__main__":
    main()
