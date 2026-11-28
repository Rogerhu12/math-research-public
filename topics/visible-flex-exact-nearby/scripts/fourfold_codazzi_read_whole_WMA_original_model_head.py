"""Read the 14 actual WMA conclusions and their whole inventory; no original arithmetic."""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re

TOPIC="topics/visible-flex-exact-nearby"
NOTES=TOPIC+"/notes/"
DIR=NOTES+"weighted_model_Theta_receiver_ci/run-46122573619-1/"
FILES={
    "manifest":(NOTES+"2026-11-28-weighted-model-Theta-receiver-inputs.json",45728,"4913fe4ce57cd579741b65090cd5e6dae22392956545196c888c3061b8974ffb"),
    "actual":(DIR+"actual-weighted-model-Theta-receiver.json",12593,"587ec4c28e521c8b04a85d42fad02bd5a53b4468ac9fdf217206ef40f231e3ae"),
    "execution":(DIR+"execution.json",8924,"1b022e585f9fc30968a3aaaa8167229891ba02e15e8ece1ea010fe317c856cdc")}
HEAD_KEY="complete_original_model_D1_head_weight_upper"


def require(ok,message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read(root):
    docs={}
    for role,(path,length,digest) in FILES.items():
        raw=(root/path).read_bytes()
        require(len(raw)==length and sha(raw)==digest,"whole completed WMA "+role)
        docs[role]=json.loads(raw)
    m,a,e=(docs[k] for k in ("manifest","actual","execution"))
    records=m["files"]
    encoded=(json.dumps(records,sort_keys=True,separators=(",",":"),ensure_ascii=False)+"\n").encode()
    require(len(records)==m["expected_current_input_count"]==139 and e["current_input_receipts"]=={
        "complete_count":139,"complete_descriptors_sha256":sha(encoded),"manifest_sha256":FILES["manifest"][2],
        "reconstruct_from":"whole manifest.files"},"all 139 complete original current descriptors")
    roles={}
    for spec in records:
        raw=(root/spec["path"]).read_bytes()
        require(len(raw)==spec["bytes"] and sha(raw)==spec["sha256"] and
                hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()==spec["git_blob_sha"],
                "complete original current file: "+spec["role"])
        roles[spec["role"]]=spec
    restoration=e["historical_restoration"]
    require(len(m["historical_inputs"])==restoration["original_native_files_restored"]==6
            and restoration["complete_receipts"]==[{**s,"whole_original_bytes_restored":True,"new_numerical_computation":False} for s in m["historical_inputs"]]
            and restoration["scientific_targets_recomputed"]==0,"all six original historical receipts, without rematerialization")
    ident=a["identity"]
    require(a["complete"] is a["proved"] is e["complete"] is True and a["actual_returncode"]==e["actual_child_returncode"]==0
            and a["failure"] is e["failure"] is a["current_target"] is None
            and e["child_timeout"] is False and e["scientific_children"]==1
            and ident["run_id"]==e["run_id"]=="46122573619" and ident["run_attempt"]==e["run_attempt"]=="1"
            and ident["source_sha256"]==roles["science"]["sha256"]=="4c2fd770110f67972061f2892e0e3d4770c26b36d08cda4171c24ac129f3f2e6"
            and roles["WMT_math"]["sha256"]=="15c74f7158e7e516fde6215590ff5d6fc9f996982c9c52a868c70b7d9bc2c114"
            and e["manifest_sha256"]==ident["manifest_sha256"]==FILES["manifest"][2]
            and e["scientific_files"]==[dict(zip(("path","bytes","sha256"),FILES["actual"]))]
            and a["completed_targets"]==m["target_order"] and len(m["target_order"])==a["saved_record_count"]==14
            and set(a["new_records"])==set(m["target_order"]) and m["target_order"][11]==HEAD_KEY
            and a["result"]["all_model_head_and_infinite_tail_terms_paid"] is True and a["old_scientific_target_calls"]==0,
            "actual complete 14-target result from the same original owner and run")
    old=a["original_model_carrier_receipt"]
    fresh=a["new_carrier_receipts"]["complete-new-model-weighted-head.jsonl.gz"]
    phases=a["copied_complete_input_records"]["original_model_input_records"]
    require(old=={"bytes":440380,"complete_modes":2240,"low_reference_modes":96,
                 "sha256":"037354a0b051a4a251e0d4be858e49e897c1b924d2e92b8c7e67c4fad05f4ae1"}
            and fresh=={"all_original2240_modes_also_in_whole_maximum":True,"bytes":76096772,"first_new_mode":2241,
                "last_new_mode":1048576,"new_complete_records":1046336,
                "sha256":"950ce3eada70b3ff079847fd9d43150d34d7b863395afedc238a1772afb48f13"}
            and a["complete_model_head_count"]==a["parameters"]["complete_new_model_head"]==1048576
            and a["parameters"]["physical_frequency"]==4 and phases["low_reference_multiplier"]=="1"
            and phases["same_full_beta_minus_mu_over4_inside_original_native"] is True
            and phases["true_target_basis_phase_a_retained"] is True,"the exact same selected model, full frequency span and whole private chain")
    saved=a["new_records"][HEAD_KEY]
    match=re.fullmatch(r"\[([^ ]+) \+/- ([^ ]+)\]",saved["ball"])
    require(saved["bound"]=="upper" and match is not None and
            Fraction(match[1])+Fraction(match[2])<Fraction(573,1000),"entire saved upper ball below 573/1000")
    return {"original_complete_run":"46122573619/1","whole_current_inputs":len(records),
            "whole_historical_receipts":6,"original_completed_targets":14,"original_modes_covered":[1,1048576],
            "saved_complete_head_record":saved,"original_private_model_files_restored":0,"new_scientific_targets":0}


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    print(json.dumps(read(parser.parse_args().repo.resolve()),sort_keys=True))
