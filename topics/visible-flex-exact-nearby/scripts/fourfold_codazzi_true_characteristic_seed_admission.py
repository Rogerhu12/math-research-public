"""Read accepted original signed stages by whole natural-file identities.

Metadata only. No Taylor, Fourier, characteristic or scalar calculation.
"""
import gzip
import hashlib
import json



HISTORY="a3d84d905ce72e3a854874bbe98d119623f3f8de"
TOPIC="topics/visible-flex-exact-nearby"
TAYLOR=TOPIC+"/notes/old_rho_first_Airy_Taylor_extension_ci/run-43664023495-1/"
ADJACENT=TOPIC+"/notes/correlated_adjacent_piece_first_Airy_sources_ci/run-43676926141-1/"
FIXED={
    "native":(TAYLOR+"consumers/complete-old-rho-first-Airy-Taylor-through-twelve.json.gz",88854,"758a2901d194e9d54ec10bb5004014ee34a972c35367589fd5c86afce3f30c9f"),
    "process":(TAYLOR+"consumers/process.json",34792,"42ab23b97ce922b042b8291af46cfe8c44ffd7e90ba1e2a6049caef263b7224e"),
    "publication":(TAYLOR+"publication.json",55427,"dc7d7f0fca329f4e16af276ea762ab9316285e803d0816b6b8ec01fe3896e7d3"),
    "majorants":(ADJACENT+"consumers/stages/complete-original-reference-holomorphic-majorants.json.gz",4501,"29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144"),
    "adjacent_process":(ADJACENT+"consumers/process.json",37783,"9e8f1f92660c1b44aa3c5c389a2c621a14aa65611cb0cf4c3a98daac1613a89b"),
    "adjacent_publication":(ADJACENT+"publication.json",26496,"0cfbfcd3866c4fda4fd31020efa630c8e3b5e7e24fc6fafe1219a2e84a3efe3c"),
}
ALGEBRA="9eb4b99b9a6b569233a3b7c3da80da7d2738c4f0bd18040654ff5b7beace2d4b"
ROOT=("1191984371497/5000000000000","2383968743003/10000000000000")
PIECE=("2147184947341121/9007199254740992","4295308144604611/18014398509481984")
BRANCH={
    "leading_a0_minus":"a0_plus","leading_b0_minus":"-b0_plus",
    "Fb_minus":"Fb_plus","Fa_minus":"-Fa_plus",
    "normalized_A_minus":"-A_plus","normalized_B_minus":"B_plus",
    "first_correction_a1_minus":"-a1_plus","first_correction_b1_minus":"b1_plus",
    "same_complex_delta_without_conjugation":True,
    "both_original_Airy_carrier_branches_retained":True,
}


def check(ok,msg):
    if not ok:
        raise ValueError(msg)


def admit(read_historical,names):
    receipts=[]
    def get(path,size,digest):
        raw=read_historical(HISTORY,path)
        check((size is None or len(raw)==size) and hashlib.sha256(raw).hexdigest()==digest,
              "wrong original whole bytes: "+path)
        receipts.append({"path":path,"bytes":len(raw),"sha256":digest})
        return json.loads(gzip.decompress(raw) if path.endswith(".gz") else raw)
    docs={key:get(*spec) for key,spec in FIXED.items()}
    n,p,u=docs["native"],docs["process"],docs["publication"]
    check(n["complete"] and n["proved"] and n["failure"] is None
          and n["complete_branch_identity"]==BRANCH and n["algebra_sha256"]==ALGEBRA
          and all(g["passed"] for g in n["gates"]) and len(n["original_stages"])==75
          and len(n["stages"])==205 and p["actual_returncode"]==0
          and p["native_sha256"]==FIXED["native"][2] and p["mathematical_complete"]
          and p["mathematical_proved"] and p["original75_stage_bytes_unchanged"]
          and p["mathematical_failure"] is None and u["complete"] and u["actual_returncode"]==0,
          "incomplete original Taylor provenance")
    m=p["scientific_metadata"]
    check(m["exact_complex_delta_radius"]=="1/100000000" and m["actual_intrinsic_parameter"]=="eta_0"
          and tuple(m["exact_root_interval"])==ROOT and tuple(m["exact_original_physical_piece_interval"])==PIECE
          and m["background_definition_sha256"]=="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
          and m["explicit_direction_definition_sha256"]=="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04",
          "changed signed physical family")
    table={r["file"]:r for r in u["files"]}
    stages={}
    for name in names:
        old=name in n["original_stages"]
        e=n["original_stages"][name] if old else n["stages"][name]
        rel="stages/"+name+".json.gz"
        row=table["consumers/"+rel]
        check(e["file"]==rel and row["bytes"]==e["bytes"] and row["sha256"]==e["sha256"],
              "changed natural historical signed stage")
        source=n["original_Taylor_source_sha256"] if old else n["source_sha256"]
        manifest=n["original_Taylor_manifest_sha256"] if old else n["input_manifest_sha256"]
        doc=get(TAYLOR+"consumers/"+rel,e["bytes"],e["sha256"])
        check(doc["stage"]==name and doc["complete"] and doc["runtime"]==n["runtime"]
              and doc["algebra_sha256"]==ALGEBRA and doc["source_sha256"]==source
              and doc["input_manifest_sha256"]==manifest and (old or doc["stage_kind"]=="new_output"),
              "changed signed coefficient header")
        stages[name]=doc["payload"]
    ap,au,major=docs["adjacent_process"],docs["adjacent_publication"],docs["majorants"]
    row=next(r for r in au["files"] if r["file"]=="consumers/stages/"+major["stage"]+".json.gz")
    check(ap["actual_returncode"]==0 and ap["mathematical_complete"] and ap["mathematical_proved"]
          and ap["mathematical_failure"] is None and au["actual_returncode"]==0 and au["complete"]
          and major["complete"] and row["bytes"]==FIXED["majorants"][1]
          and row["sha256"]==FIXED["majorants"][2] and major["runtime"]==n["runtime"],
          "missing original compatible full-product majorants")
    return stages,major["payload"]["majorants"],receipts
