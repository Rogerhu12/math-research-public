#!/usr/bin/env python3
"""Exact whole-piece domain comparison for the saved dominant pieces 2547/2551.

Only original radial-node bytes are decoded.  No target, FFT, cubic evaluation,
interval enclosure, old norm, source row or accepted stage is recomputed.
All inputs live in the public Actions runner's immutable temporary science tree.
"""
from __future__ import annotations
import argparse
import ast
import datetime as dt
from fractions import Fraction as Q
import gzip
import hashlib
import io
import json
import math
import os
from pathlib import Path
import struct
import sys
import time
import traceback
import zipfile

PUBLIC = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
OLD_INPUT_COMMIT = "a3d84d905ce72e3a854874bbe98d119623f3f8de"
ROOTS = (Q(1191984371497,5000000000000),Q(2383968743003,10000000000000))
ROOT_PIECE = (Q(2147184947341121,9007199254740992),Q(4295308144604611,18014398509481984))
GERM = (Q(8556839292003943,36028797018963968),Q(8636031980136455,36028797018963968))
RG, RHO, RC = Q(3,8000),Q(1,6000),Q(1,2000)
TARGETS, CHAIN = (2547,2551),(2547,2548,2549,2550,2551)
PINS = {
    "candidate_index": (6750,"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"),
    "candidate_shard": (2738003,"3aeb38bf0577207cafcad3a59e43ed5a04a4c9cf9a703c4c3c4088c963a09106"),
    "response_index": (11295,"ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6"),
    "response_shard": (2698707,"ce29c19c81e77cb2f2ea9b70edc59af96a869116fa96e2e5375ffa4d61927917"),
}


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def save(path, value):
    raw = (json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2)+"\n").encode("utf-8")
    if len(raw)>60000:
        raise ValueError("the readable domain result exceeds 60000 bytes")
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_bytes(raw)
    return {"file":Path(path).name,"bytes":len(raw),"sha256":digest(raw)}


def header(stream):
    if stream.read(6)!=b"\x93NUMPY":
        raise ValueError("the original NPZ member is not NPY")
    version=stream.read(2)
    if version==b"\x01\x00":
        size=struct.unpack("<H",stream.read(2))[0]
        encoding="latin1"
    elif version in (b"\x02\x00",b"\x03\x00"):
        size=struct.unpack("<I",stream.read(4))[0]
        encoding="utf-8" if version==b"\x03\x00" else "latin1"
    else:
        raise ValueError("unsupported original NPY version")
    if not 1<=size<=65536:
        raise ValueError("unexpected original NPY header size")
    doc=ast.literal_eval(stream.read(size).decode(encoding))
    if not isinstance(doc,dict) or set(doc)!={"descr","fortran_order","shape"}:
        raise ValueError("unexpected original NPY header schema")
    if doc["descr"] not in ("<f8",">f8","=f8") or not isinstance(doc["fortran_order"],bool):
        raise ValueError("original data must be ordinary binary64, never object arrays")
    if not isinstance(doc["shape"],tuple) or any(not isinstance(n,int) or n<0 for n in doc["shape"]):
        raise ValueError("invalid original array shape")
    return doc


def original_nodes(raw, first, end, components):
    # The container and its complete original bytes have already passed SHA256.
    # Read only the node vector and the coefficient header, never cubic values.
    with zipfile.ZipFile(io.BytesIO(gzip.decompress(raw))) as archive:
        if archive.namelist().count("radial_nodes.npy")!=1 or archive.namelist().count("piece_coefficients.npy")!=1:
            raise ValueError("the original two required NPZ members are not unique")
        with archive.open("piece_coefficients.npy") as stream:
            coefficient_header=header(stream)
        if coefficient_header["shape"]!=(4,end-first,components):
            raise ValueError("complete original coefficient dimensions changed")
        with archive.open("radial_nodes.npy") as stream:
            node_header=header(stream)
            if node_header["shape"]!=(end-first+1,):
                raise ValueError("complete original radial-node dimensions changed")
            payload=stream.read()
        if len(payload)!=8*(end-first+1):
            raise ValueError("original radial-node byte length changed")
        prefix=node_header["descr"][0]
        if prefix=="=":
            prefix="<" if sys.byteorder=="little" else ">"
        values=[x[0] for x in struct.iter_unpack(prefix+"d",payload)]
        if not all(math.isfinite(x) for x in values):
            raise ValueError("nonfinite original radial node")
        exact=[Q(*x.as_integer_ratio()) for x in values]
    return exact,{"node_header":node_header,"coefficient_header":coefficient_header,
        "cubic_values_evaluated":False,"original_whole_shard_sha256":digest(raw)}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--repo",required=True,type=Path)
    parser.add_argument("--manifest",required=True,type=Path)
    parser.add_argument("--manifest-sha",required=True)
    parser.add_argument("--out-dir",required=True,type=Path)
    args=parser.parse_args()
    args.out_dir.mkdir(parents=True,exist_ok=True)
    start=time.monotonic()
    source=Path(__file__).resolve()
    process={
        "kind":"actual_exact_whole_dominant_piece_domain_comparison",
        "repository":PUBLIC,"run_id":os.environ.get("GITHUB_RUN_ID"),
        "run_attempt":os.environ.get("GITHUB_RUN_ATTEMPT"),
        "source_path":TOPIC+"/scripts/"+source.name,"source_sha256":digest(source.read_bytes()),
        "input_manifest_sha256":args.manifest_sha,"historical_input_commit":OLD_INPUT_COMMIT,
        "started_utc":now(),"complete":False,"actual_returncode":1,"failure":None,"gates":[],
        "new_exact_domain_comparison_processes":1,
        "old_numerical_enclosures_recomputed":0,"old_mathematical_stages_recomputed":0,
        "new_target_or_FFT_evaluations":0,"original_cubic_values_evaluated":0,
        "new_operator_norms_or_radial_integrals_evaluated":0,
        "reproducible_data_published":False,"Release_or_Actions_artifact_upload":False,
        "pieces":[],
    }
    def gate(name,passed):
        process["gates"].append({"name":name,"passed":bool(passed)})
        return bool(passed)
    try:
        manifest_raw=args.manifest.read_bytes()
        if digest(manifest_raw)!=args.manifest_sha:
            raise ValueError("the immutable input manifest changed")
        manifest=json.loads(manifest_raw)
        if manifest["public_repository"]!=PUBLIC or manifest["historical_input_commit"]!=OLD_INPUT_COMMIT:
            raise ValueError("unexpected repository or historical scientific input commit")
        expected_parameters={
            "target_pieces":list(TARGETS),"complete_physical_piece_chain":list(CHAIN),
            "exact_root_interval":list(map(str,ROOTS)),"exact_original_root_piece":list(map(str,ROOT_PIECE)),
            "exact_original_scalar_germ":list(map(str,GERM)),
            "exact_paid_auxiliary_fold_radius":str(RG),
            "exact_paid_complete_old_product_radius":str(RHO),
            "exact_paid_intrinsic_Cauchy_radius":str(RC),
            "fixed_intrinsic_parameter":"eta_0",
            "same_real_and_complex_delta_radius":"1/100000000",
        }
        if manifest["mathematical_parameters"]!=expected_parameters:
            raise ValueError("a paid domain or target piece was silently changed")
        entries={r["path"]:r for r in manifest["files"]}
        if len(entries)!=len(manifest["files"]):
            raise ValueError("duplicate original manifest input paths")
        paths=manifest["input_paths"]
        if set(paths)!=set(PINS):
            raise ValueError("exactly the four original data inputs are required")
        originals={}
        process["original_inputs"]=[]
        for role,(size,sha) in PINS.items():
            relative=paths[role]
            if not relative.startswith(TOPIC+"/") or ".." in Path(relative).parts:
                raise ValueError("a data input left the authorized topic")
            entry=entries[relative]
            raw=(args.repo/relative).read_bytes()
            if not (len(raw)==entry["bytes"]==size and digest(raw)==entry["sha256"]==sha):
                raise ValueError("an original complete input changed: "+role)
            originals[role]=raw
            process["original_inputs"].append({"role":role,"path":relative,"bytes":size,"sha256":sha})
        gate("all four complete historical inputs retain their original bytes and SHA256",True)
        ci,zi=[json.loads(originals[k]) for k in ("candidate_index","response_index")]
        if not gate("the original full65/full193 identities and the independent mean are retained",
            ci["coefficient_shape"]==[4,6144,65] and zi["coefficient_shape"]==[4,6144,193]
            and ci["metadata"]["exact_float_amplitude"]=="6890507429876859/9007199254740992"
            and zi["metadata"]["finite_head_mean_was_not_removed_from_the_solve"] is True
            and zi["metadata"]["background_candidate_sha256"]==PINS["candidate_index"][1]):
            raise ValueError("the original full candidate/direction identities failed")
        nodes={}
        for kind,index,first,end,components in (
            ("candidate",ci,1346,2692,65),("response",zi,2265,2718,193)):
            part=next(x for x in index["parts"] if x["first_interval"]==first)
            role=kind+"_shard"
            if not (part["last_interval_exclusive"]==end and part["bytes"]==PINS[role][0]
                and part["sha256"]==PINS[role][1] and part["file"]==Path(paths[role]).name):
                raise ValueError("the exact original natural shard manifest changed")
            vector,evidence=original_nodes(originals[role],first,end,components)
            nodes[kind]={piece:(vector[piece-first],vector[piece-first+1]) for piece in CHAIN}
            process[kind+"_original_array_headers"]=evidence
        if not gate("all five whole physical pieces have identical exact dyadic knots in the full65 and full193 arrays",
            nodes["candidate"]==nodes["response"]):
            raise ValueError("the two original grids disagree")
        cells=nodes["candidate"]
        if not gate("the original physical root piece is exactly the previously proved piece2549",
            cells[2549]==ROOT_PIECE and ROOT_PIECE[0]<ROOTS[0]<ROOTS[1]<ROOT_PIECE[1]):
            raise ValueError("the original root piece moved")
        gate("the five genuine consecutive pieces have no gap, overlap, or invented seam",
            all(cells[j][0]<cells[j][1]==cells[j+1][0] for j in CHAIN[:-1])
            and cells[CHAIN[-1]][0]<cells[CHAIN[-1]][1])
        for piece in CHAIN:
            left,right=cells[piece]
            rho_interval=(ROOTS[0]-right,ROOTS[1]-left)
            outer=max(abs(x) for x in rho_interval)
            side="negative" if piece<2549 else "positive" if piece>2549 else "root"
            strict=(right<ROOTS[0] if side=="negative" else left>ROOTS[1] if side=="positive" else True)
            row={
                "piece":piece,"side":side,"target_for_new_source_extension":piece in TARGETS,
                "exact_original_physical_interval":list(map(str,(left,right))),
                "exact_true_root_rho_cover":list(map(str,rho_interval)),
                "exact_maximum_absolute_rho":str(outer),
                "exact_fold_radius_margin":str(RG-outer),
                "exact_old_product_radius_margin":str(RHO-outer),
                "exact_intrinsic_Cauchy_radius_margin":str(RC-outer),
                "inside_original_scalar_germ":GERM[0]<=left<right<=GERM[1],
                "inside_paid_fold_disk":outer<RG,
                "inside_paid_complete_old_product_disk":outer<RHO,
                "inside_paid_intrinsic_Cauchy_disk":outer<RC,
                "on_the_correct_strict_side":strict,
            }
            if piece!=2549:
                row["exact_positive_minimum_root_distance"]=str(min(abs(x) for x in rho_interval))
                row["true_entry_seam"]=str(right if piece<2549 else left)
                row["inner_predecessor_piece"]=piece+1 if piece<2549 else piece-1
            process["pieces"].append(row)
            if piece in TARGETS:
                gate("the entire physical piece"+str(piece)+" lies in the same original scalar germ",row["inside_original_scalar_germ"])
                gate("the entire physical piece"+str(piece)+" is strictly on its actual root side",strict)
                gate("the entire physical piece"+str(piece)+" is inside the paid Rg disk",row["inside_paid_fold_disk"])
                gate("the entire physical piece"+str(piece)+" is inside the paid RHO product disk",row["inside_paid_complete_old_product_disk"])
                gate("the entire physical piece"+str(piece)+" is inside the paid intrinsic Cauchy disk",row["inside_paid_intrinsic_Cauchy_disk"])
        process["domain_extension_permitted_by_this_comparison"]=all(x["passed"] for x in process["gates"])
        process["required_next_source_contract"]={
            "piece2547_inherits_nonzero_entry_from":2548,
            "piece2551_inherits_nonzero_entry_from":2550,
            "phase_difference_entry_reset_to_zero":False,
            "normalized_first_correction_entry_reset_to_zero":False,
            "log_G_ratio_radial_integral_constant_reset_to_zero":False,
            "all_true_physical_seams_and_independent_mean_retained":True,
            "new_characteristic_strip_gaps_still_to_be_paid":True,
            "complete_angular_compositions_and_all_output_sources_still_to_be_paid":True,
            "no_new_forcing_or_complete_source_bound_claimed":True,
            "no_strong_return_cutoff97_inverse_or_final_PDE_claimed":True,
        }
        process["complete"]=True
        process["actual_returncode"]=0 if process["domain_extension_permitted_by_this_comparison"] else 1
        if process["actual_returncode"]:
            process["failure"]={"kind":"actual_domain_gate_failed","message":"The original paid domain cannot be enlarged by relabeling a piece; complete exact margins are retained."}
    except Exception as error:
        process["failure"]={"type":type(error).__name__,"message":str(error),"traceback":traceback.format_exc()}
    process["finished_utc"]=now()
    process["actual_domain_comparison_wall_seconds"]=time.monotonic()-start
    lines=[
        "# Actual whole-piece domain comparison for pieces2547 and2551","",
        "This is an exact comparison of whole original piece intervals with previously paid domains. It does not compute a new target, old interval enclosure, forcing norm, source integral or inverse.","",
        "- Public repository: "+PUBLIC+".",
        "- Actual run: "+str(process["run_id"])+"/"+str(process["run_attempt"])+".",
        "- Script: "+process["source_path"]+".",
        "- Script SHA256: "+process["source_sha256"]+".",
        "- Input manifest SHA256: "+args.manifest_sha+".",
        "- Immutable original input commit: "+OLD_INPUT_COMMIT+".",
        "- Parameters: fixed eta0; original root interval; targets2547 and2551; same full65/full193 arrays; Rg=3/8000, RHO=1/6000, RC=1/2000.",
        "- CLI: --repo <immutable-science> --manifest <the committed input manifest> --manifest-sha "+args.manifest_sha+" --out-dir <temporary-output>.",
        "- Actual exit code: "+str(process["actual_returncode"])+".",
        "- Old mathematical stages or enclosures recomputed:0. New exact whole-domain comparison process:1.","",
        "## Complete original piece intervals","",
        "| piece | side | exact physical interval | maximum absolute rho | RHO margin | in the original scalar germ |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    for row in process["pieces"]:
        lines.append("| "+str(row["piece"])+" | "+row["side"]+" | ["+", ".join(row["exact_original_physical_interval"])+"] | "+row["exact_maximum_absolute_rho"]+" | "+row["exact_old_product_radius_margin"]+" | "+str(row["inside_original_scalar_germ"])+" |")
    lines.extend(["","## Actual gates",""])
    for row in process["gates"]:
        lines.append("- "+row["name"]+": "+("passed" if row["passed"] else "FAILED")+".")
    if process["failure"]:
        lines.extend(["","Actual failure: "+str(process["failure"]), ""])
    lines.extend([
        "","## Scope","",
        "A positive radial-domain result permits the next, separately paid comparison on these exact two pieces. It does not authorize changing any old domain or setting the comparison entry to zero. Piece2547 inherits the true nonzero phase and first-correction entry from piece2548; piece2551 inherits it from piece2550. The constant in log(G/Gbar)-(1/6)log(A/Abar) is also inherited. Every true physical seam, one-sided radial jet, independent even mean, and old-circle projection remains.",
        "",
        "Characteristic strip gates, complete forcing differences, full old-circle terms and radial source integrals are still separate obligations. No new complete source bound, strong return, cutoff97 inverse or exact PDE family is asserted. Input bytes and new temporary data are not uploaded to the repository, Release or an Actions artifact; this small conclusion records only script, parameters, run, hashes and the actual result.",
    ])
    conclusion=("\n".join(lines)+"\n").encode("utf-8")
    if len(conclusion)>60000:
        raise ValueError("conclusion exceeded60000 bytes")
    (args.out_dir/"conclusion.md").write_bytes(conclusion)
    process["output_hashes"]=[{"file":"conclusion.md","bytes":len(conclusion),"sha256":digest(conclusion)}]
    save(args.out_dir/"process.json",process)
    print(json.dumps({"complete":process["complete"],"actual_returncode":process["actual_returncode"],"gates":len(process["gates"]),"all_gates_passed":all(x["passed"] for x in process["gates"]),"old_enclosures_recomputed":0},sort_keys=True))
    return process["actual_returncode"]


if __name__=="__main__":
    raise SystemExit(main())
