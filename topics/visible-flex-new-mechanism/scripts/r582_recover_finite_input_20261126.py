#!/usr/bin/env python3
"""Read one completed original Actions log and recover its next-input parameters.

This is stdlib evidence recovery after transient workspace loss. It performs
no numerical model evaluation, fitting, old optimization or seed transfer.
Raw logs and old large FIELD/endpoint arrays are neither saved nor printed.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import struct
import time
import urllib.request
from urllib.parse import urlsplit

RUNNER_HASH = "7fde98e3337eb537b18b18789b125fcac57e7382e8f22c755947e907c0ea7785"
if hashlib.sha256(Path(__file__).with_name("run_inverse_state_stdin_20261126.py").read_bytes()).hexdigest() != RUNNER_HASH:
    raise RuntimeError("original stdlib pull entry binding differs")
import run_inverse_state_stdin_20261126 as rules

OLD_SOURCE = "d4a5b41506139a2bd7ad6d53a473e1766f536377"
OLD_RUN, OLD_JOB = 45827253372, 139934478969
OLD_RAW_SHA = "0f8c0ea00bf770412d0b532dc8d28dd1d7ff0c8c2c51a874e11023e9a2432feb"
OLD_FINAL_SHA = "397a1a6fb7999c36f4849956ef6b820ba615118ce9733ebf0e6356a6ecbfb169"
OLD_INPUT_SHA = "187a463fdd777d2884310ac0793ed96583d5216d47407795b53daae633c46ac4"
LOST_PRE_RECEIPT_INPUT_SHA = "470a67d1b19249bdd08fc8b63cd129c12a4bf71b8e30c5b24a51c0ef496d0e3b"
RECEIPT_PATH = "topics/visible-flex-new-mechanism/notes/2026-11-26-r582-finite-radius-only-original-receipt.md"
RECEIPT_SHA = "e8781d68fca91b48896369af506b1ddc3ba904f81cc3d7d4eb15937c73537a4f"


def emit(tag, value):
    text = json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)
    text = text.replace("::","\\u003a\\u003a").replace("##[","\\u0023\\u0023[")
    print("FINITE_INPUT_RECOVERY_"+tag+" "+text,flush=True)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(values):
    return {"entries":len(values),
            "binary64_sha256":digest(b"".join(struct.pack("<d",x) for x in values))}


class CleanRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        follow = super().redirect_request(req,fp,code,msg,headers,newurl)
        if follow is not None and urlsplit(newurl).hostname != "api.github.com":
            follow.remove_header("Authorization")
        return follow


def recover(final, final_text, old_string):
    source = json.loads(old_string)
    source["schema"] = "identified-radius-only-terminal-for-local-tail-columns-v1"
    source["resume_origin"] = {
        "run_id":OLD_RUN,"job_id":OLD_JOB,"source_commit":OLD_SOURCE,
        "source_wrapper_sha256":"445e3ac5098cbaaa08f080e1be5d8172e576f72a00b825b2cb000adad83725d2",
        "original_log_raw_bytes":12912168,"original_log_raw_sha256":OLD_RAW_SHA,
        "raw_log_hash_includes_UTF8_BOM":True,
        "FINAL_JSON_bytes":len(final_text.encode()),"FINAL_JSON_sha256":digest(final_text.encode()),
        "original_request_sha256":"d2dfbc420b74f7b5de9b84d7ea84b802ffeb0e9b5cafaa6857d7f370a8aad708",
        "original_input_sha256":digest(old_string.encode())}
    retained = final["actual_retained_state"]
    state = {
        "p":final["actual_retained_p"],"retained_q_81":retained["q"],
        "retained_q_identity":retained["q_identity"],
        "qualified_on_old_fine_grid":retained["qualified_on_this_fine_grid"],
        "retained_state_label":retained["accepted_as"],
        "actual_constraint_radial_nodes":final["actual_constraint_radial_nodes"],
        "actual_constraint_radial_identity":identity(final["actual_constraint_radial_nodes"]),
        "actual_constraint_theta_nodes":final["actual_constraint_theta_nodes"],
        "actual_fine_theta_nodes":final["actual_fine_theta_nodes"],
        "actual_fine_radial_identity":identity(final["actual_fine_radial_nodes"]),
        "old_material_observation_nodes":final["material_observation"]["finite_material_observation_nodes"],
        "old_material_observation_identity":identity(final["material_observation"]["finite_material_observation_nodes"]),
        "pending_radial_nodes":final["pending_radial_nodes"],
        "pending_angular_upgrade":final["pending_angular_upgrade"],
        "actual_backend_trust":final["actual_backend_trust"],
        "proposed_next_trust":final["proposed_next_trust"],
        "retained_fine_scan":retained["scan"],
        "last_natural_backend_q_is_not_the_retained_input":True,
        "new_initial_trust_explicitly_resets_for_a_new_operator":1.0,
        "new_extra_columns_embed_at_zero":16,
        "old_4811_plus_old_material_plus_actual_and_actual_midpoints_reconstruct_all_10835":True}
    nodes=state["actual_constraint_radial_nodes"]
    reconstructed=sorted(set(source["paid_fine_radial_nodes"]+
        state["old_material_observation_nodes"]+nodes+
        [(a+b)/2 for a,b in zip(nodes[:-1],nodes[1:])]))
    rules.require(reconstructed==final["actual_fine_radial_nodes"],
                  "all original physical fine positions must be recovered literally")
    rules.require(identity(state["retained_q_81"])==state["retained_q_identity"],
                  "retained q binary64 identity changed")
    source["resume_state"] = state
    source["prior_cost_ledger"]["identified_radius_only_finite_failure"] = {
        "run_id":OLD_RUN,"job_id":OLD_JOB,
        "exact_reported_scientific_seconds":final["elapsed_seconds"],
        "child_wall_seconds":215.382499,"child_wall_is_not_scientific_seconds":True,
        "termination":final["termination"],"counts":final["counts"],
        "field_counts":final["final_resonant_field_counts"],
        "model_counts":final["new_model_counts"],
        "original_model_new_counts":final["original_model_new_counts"],
        "completed_Jacobian_seconds_sum":39.55630442399956,
        "material_mesh_binary64_sha256":final["field_receipt"]["material_mesh_binary64_sha256"],
        "original_15_outers_and_43_callbacks_not_replayed":True,
        "old_cost_not_subtracted_from_new_reconstruction":True,
        "large_dense_and_material_arrays_not_persisted_so_new_reconstruction_is_charged":True}
    encoded=json.dumps(source,sort_keys=True,separators=(",",":"),allow_nan=False)
    rules.require(len(encoded.encode())==218542 and digest(encoded.encode())==LOST_PRE_RECEIPT_INPUT_SHA,
                  "recovered necessary input differs from the completed pre-outage input identity")
    source["resume_origin"].update(
        published_receipt_commit="f28e377f69168b22537e82f49a4993349c1fa919",
        published_receipt_path=RECEIPT_PATH,published_receipt_sha256=RECEIPT_SHA)
    return json.dumps(source,sort_keys=True,separators=(",",":"),allow_nan=False)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request",required=True)
    args=parser.parse_args()
    started=time.monotonic()
    source=os.environ["GITHUB_SHA"]
    rules.require(re.fullmatch(r"[0-9a-f]{40}",source) is not None,"invalid recovery Actions source")
    root=Path.cwd()
    raw_request=Path(args.request).read_bytes()
    request=json.loads(raw_request)
    token=os.environ.get("MR_TOKEN","")
    rules.require(bool(token),"MR_TOKEN is required for authorized original job-log retrieval")
    public_after=rules.public_pull(root,request,source)
    private_after=rules.private_pull(request)
    for name in ("MR_TOKEN","GITHUB_TOKEN","GH_TOKEN"):
        os.environ.pop(name,None)
    rules.git(root,"checkout","--detach",source)
    rules.require(Path(args.request).read_bytes()==raw_request,"recovery request changed at pinned source")
    for path,expected in request["source_sha256"].items():
        rules.require(digest(Path(path).read_bytes())==expected,"recovery source binding differs: "+path)
    rules.require(digest(Path(RECEIPT_PATH).read_bytes())==RECEIPT_SHA,"published receipt binding differs")
    old_request=rules.git(root,"show",OLD_SOURCE+":topics/visible-flex-new-mechanism/computations/request-r582-finite-radius-only-20261126.json").stdout
    rules.require(digest(old_request)=="d2dfbc420b74f7b5de9b84d7ea84b802ffeb0e9b5cafaa6857d7f370a8aad708",
                  "original request identity changed")
    old_string=json.loads(old_request)["lanes"]["actual-resonant-radius-only"]["source_state_json"]
    rules.require(digest(old_string.encode())==OLD_INPUT_SHA,"original paid input identity changed")
    opener=urllib.request.build_opener(CleanRedirect())
    headers={"Authorization":"Bearer "+token,"Accept":"application/vnd.github+json",
             "X-GitHub-Api-Version":"2022-11-28","User-Agent":"math-research-original-input-recovery"}
    api="https://api.github.com/repos/Rogerhu12/math-research-public/actions/jobs/"+str(OLD_JOB)
    with opener.open(urllib.request.Request(api,headers=headers),timeout=90) as response:
        metadata=json.load(response)
    rules.require(metadata["status"]=="completed" and metadata["run_id"]==OLD_RUN,
                  "only the identified naturally completed original job may be read")
    with opener.open(urllib.request.Request(api+"/logs",headers=headers),timeout=120) as response:
        raw=response.read(30000000)
    token=None;headers=None
    rules.require(len(raw)==12912168 and digest(raw)==OLD_RAW_SHA,"official original raw log identity differs")
    matched=[]
    for line in raw.decode("utf-8-sig").splitlines():
        found=re.search(r"FINITE_RESONANT_FINAL (\{.*\})$",line)
        if found:matched.append(found.group(1))
    rules.require(len(matched)==1 and len(matched[0].encode())==447283
                  and digest(matched[0].encode())==OLD_FINAL_SHA,"original FINAL identity differs")
    final=json.loads(matched[0])
    encoded=recover(final,matched[0],old_string)
    emit("SOURCE",{"source_commit":source,"public_actual_pull_commit":public_after,
        "private_actual_pull_commit":private_after,"request_sha256":digest(raw_request),
        "old_run_id":OLD_RUN,"old_job_id":OLD_JOB,"official_original_status":metadata["status"],
        "old_raw_bytes":len(raw),"old_raw_sha256":digest(raw),
        "old_FINAL_bytes":len(matched[0].encode()),"old_FINAL_sha256":digest(matched[0].encode()),
        "raw_log_and_FIELD_arrays_saved_or_printed":False,
        "mathematical_model_evaluations":0,"old_optimization_replays":0,
        "recovered_pre_outage_input_sha256":LOST_PRE_RECEIPT_INPUT_SHA})
    emit("NEXT_INPUT",{"source_state_json":encoded,"source_state_bytes":len(encoded.encode()),
        "source_state_sha256":digest(encoded.encode()),
        "only_necessary_next_input_coordinates_and_existing_cost_ledger":True})
    emit("FINISHED",{"wall_seconds":time.monotonic()-started,
        "science_seconds_or_new_mathematical_evaluations":0,
        "stdout_only":True,"README_completion_claim":False})


if __name__=="__main__":
    try:
        main()
    except Exception as error:
        emit("ERROR",{"type":type(error).__name__,"message":"original-input recovery failed; credential-bearing transport details withheld"})
        raise SystemExit(2) from None
