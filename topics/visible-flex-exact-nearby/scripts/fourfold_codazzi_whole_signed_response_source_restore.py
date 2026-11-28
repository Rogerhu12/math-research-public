"""Recover the one original WSS source carrier needed by a new inhomogeneous solve."""
from hashlib import sha1, sha256
import json
import multiprocessing as mp
import os
from pathlib import Path
import platform
import queue
import signal
import sys
import time


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return sha256(raw).hexdigest()


def canonical(obj):
    return (json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()


def verify_object(raw,spec):
    require(len(raw) == spec["bytes"] and sha(raw) == spec["sha256"]
            and sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest() == spec["git_blob_sha"],
            "entire original WSS file, SHA256 and Git blob")


def admit(owner, inputs, specs):
    for role in ("actual","execution","manifest"):
        verify_object(inputs[role],specs[role])
    document,execution,manifest = (json.loads(inputs[k]) for k in ("actual","execution","manifest"))
    require(manifest["kind"] == owner.MANIFEST_KIND and manifest["scientific_kind"] == owner.KIND
            and manifest["target_order"] == owner.TARGETS and manifest["parameters"] == owner.PARAMETERS,
            "original two targets and full source domain")
    roles = {row["role"]:row for row in manifest["files"]}
    require(len(roles) == len(manifest["files"]) == 19
            and sha(Path(owner.__file__).read_bytes()) == roles["science"]["sha256"],
            "the actual owner and the entire original pinned logic")
    owner.validate(document,manifest)
    ident = document["identity"]
    source = document["new_records"].get(owner.TARGETS[0])
    require(source and len(document["completed_targets"]) >= 1 and not document["unfinished_chunk"]
            and not document["complete_disjoint_cells"] and document["chunks"][-1]["stop"] == source["whole_private_piece_count"]
            and ident["manifest_sha256"] == execution["manifest_sha256"] == specs["manifest"]["sha256"]
            and ident["source_sha256"] == roles["science"]["sha256"]
            and ident["run_id"] == str(execution["run_id"]) and str(execution["run_attempt"]) == ident["run_attempt"] == "1"
            and manifest["repository"] == execution["repository"] == owner.REPOSITORY
            and execution["kind"] == "R149_whole_selected_body_signed_source_execution_v1"
            and execution["actual_scientific_checkout"] == ident["actual_scientific_checkout"]
            and execution["scientific_children"] == 1 and execution["finished_utc"]
            and execution["actual_child_returncode"] == document["actual_returncode"]
            and execution["original_scientific_complete"] == document["complete"]
            and execution["original_scientific_failure"] == document["failure"]
            and execution["completed_natural_targets"] == document["completed_targets"]
            and execution["new_target_order"] == manifest["target_order"]
            and execution["actual_complete_new_cells"] == document["new_complete_signed_cells"]
            and execution["actual_runtime"] == manifest["runtime"]
            and execution["scientific_started_utc"] and execution["scientific_ended_utc"]
            and execution["whole_new_current_input_count"] == len(roles)
            and execution["original_TC_scientific_target_calls"] == execution["old_completed_targets_recomputed"] == 0
            and execution["whole_original_input_admission"] == document["original_input_identity"],
            "terminal execution of the actual whole source; a missing source cannot be restored")
    if document["complete"]:
        require(execution["complete"] and execution["failure"] is None and execution["actual_child_returncode"] == 0
                and len(document["completed_targets"]) == 2 and not execution["timed_out"], "original successful whole run")
    else:
        require(document["completed_targets"] == owner.TARGETS[:1] and not execution["complete"]
                and execution["failure"] is not None and document["failure"] is not None
                and execution["actual_child_returncode"] != 0, "actual terminal failure after the complete carrier only")
    target = manifest["operation"]["output_base"]+"/run-"+ident["run_id"]+"-1/whole-selected-signed-source.json"
    require(execution["scientific_files"] == [{"path":target,"bytes":len(inputs["actual"]),"sha256":sha(inputs["actual"])}],
            "exact previous scientific object published by that same terminal execution")
    return document,manifest,roles


def preflight(*, owner, inputs, specs, root, old_rows_index):
    """Call before NumPy or Flint is imported, inside the original TCXV raw-input staging."""
    document,manifest,roles=admit(owner,inputs,specs)
    original_manifest,original_roles,original=owner.admit(Path(root),inputs["manifest"],
        specs["manifest"]["sha256"],old_rows_index)
    require(original_manifest == manifest and original_roles == roles
            and original[-1] == document["original_input_identity"]
            and not any(k in sys.modules for k in ("numpy","flint","scipy")),
            "complete original 19 + original 184/32 closure before numerical import")
    return original


def restore(*, owner, inputs, specs, root, old_rows_index, directory, np, flint, admitted,
            budget, progress, wall_deadline):
    """Original data were preflighted BEFORE numerical imports by owner.admit.

    Recreate complete 320-bit source pieces and verify each original chunk +
    the whole original signed index. Polarizations are never evaluated.
    """
    doc,manifest,roles = admit(owner,inputs,specs)
    root,directory = Path(root),Path(directory)
    require(os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_REPOSITORY") == owner.REPOSITORY
            and platform.python_version() == "3.12.14" and flint.__version__ == "0.9.0" and np.__version__ == "2.3.5"
            and all(os.environ.get(k) == "1" for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"))
            and platform.machine() == "x86_64" and sys.byteorder == "little" and flint.ctx.prec == 320,
            "whole original signed-source runtime in a fresh job-private phase")
    original,old_roles,raws,helper,prior,rows,identity = admitted
    require(identity == doc["original_input_identity"] and Path(old_rows_index).is_file(),
            "entire original WSS raw admission shared by the current owner")
    directory.mkdir(parents=True,exist_ok=False)
    def check(processes):
        budget(processes)
        require(time.monotonic() < wall_deadline,"whole joint job wall budget")
    def raw_progress(name,detail):
        check([])
        progress(name,detail)
    check([])
    def load(role):
        spec=roles[role]
        raw=(root/spec["path"]).read_bytes()
        require(sha(raw) == spec["sha256"] and len(raw) == spec["bytes"],"whole source module "+role)
        return owner.load(root/spec["path"],"_new_WSS_recovery_"+role)
    core,positive,field = (load(k) for k in ("raw_input_helper","positive_signed_source","carrier"))
    tc_spec=old_roles["trial_math"]
    tc_raw=(root/tc_spec["path"]).read_bytes()
    require(len(tc_raw) == tc_spec["bytes"] and sha(tc_raw) == tc_spec["sha256"],"original complete radial backend")
    tc=owner.load(root/tc_spec["path"],"_new_WSS_recovery_original_radial_backend")
    base,direction,offsets,rows,receipt=core.raw_inputs(np,flint,admitted,root,directory,raw_progress)
    check([])
    require(receipt == doc["source_restoration"],"actual complete old signed offsets, cubics and all original scalar rows")
    backend,br=helper.directed_backend(np,flint,raws[old_roles["box_math"]["path"]],raws[old_roles["fft_math"]["path"]])
    require(br == receipt["directed_backend"],"same complete interval vector arithmetic and directed runtime")
    c=tc.DirectedContext(np,flint.arb,backend["Box"],backend["CBox"],backend["zeros"],
                         backend["arb_box"],backend["reduce_box"],backend["DirectedFFT"]())
    plan=field.partition(helper,rows,base,direction)
    encoded=canonical([[j,k,str(a),str(b)] for j,k,a,b in plan])
    require(doc["plan"] == {"pieces":len(plan),"bytes":len(encoded),"canonical_sha256":sha(encoded),
          "true_compact_signed_derivatives":True,"both_sides_of_true_uncertain_root":True},"original entire physical partition")
    storage=field.SignedSourceStore(directory/"signed",plan)
    def read(r):
        return field.historical_ball(flint,r)
    ctx=mp.get_context("fork")
    jobs,done=ctx.Queue(8),ctx.Queue(8)
    workers=[]
    def worker():
        signal.signal(signal.SIGTERM,signal.SIG_DFL)
        while True:
            i=jobs.get()
            if i is None:
                return
            try:
                j,k,lo,hi=plan[i]
                pair=field.signed_pair(c,tc,positive,helper,base,direction,offsets,rows[j],k,lo,hi,read)
                storage.put(i,field.packed_pairs(c,positive,pair),field.endpoint_pair(c,positive,pair))
                done.put((i,storage.records.pop(i),None))
            except BaseException as error:
                done.put((i,None,type(error).__name__+": "+str(error)))
                return
    nxt=0
    submitted=set()
    completed={}
    verified=[]
    chunk=None
    try:
        for _ in range(4):
            process=ctx.Process(target=worker)
            process.start()
            workers.append(process)
        for i in range(len(plan)):
            while nxt < min(len(plan),i+8):
                jobs.put(nxt)
                submitted.add(nxt)
                nxt+=1
            while i not in completed:
                check(workers)
                try:
                    j,spec,error=done.get(timeout=2)
                except queue.Empty:
                    require(all(x.is_alive() for x in workers),"no silent child loss during whole carrier recovery")
                    continue
                require(j in submitted and error is None and spec is not None,"actual source recovery "+str((j,error)))
                submitted.remove(j)
                completed[j]=spec
            spec=completed.pop(i)
            storage.records[i]=spec
            storage.get(i)
            if chunk is None:
                chunk=dict(first=i,stop=i,whole_file_bytes=0,sha256=sha(b"WSS-complete-piece-chunk"))
            chunk.update(stop=i+1,whole_file_bytes=chunk["whole_file_bytes"]+spec["bytes"],
                         sha256=sha(bytes.fromhex(chunk["sha256"])+canonical([i,spec])))
            expected=doc["chunks"][len(verified)]
            if i+1 == expected["stop"]:
                require(chunk == expected,"complete original source chunk "+str(len(verified)))
                verified.append(chunk)
                chunk=None
                progress("restore_whole_original_WSS_chunk",dict(verified=len(verified),physical_pieces=i+1))
            check(workers)
    finally:
        for x in workers:
            if x.is_alive():
                x.terminate()
        for x in workers:
            x.join(timeout=5)
        jobs.cancel_join_thread()
        jobs.close()
        done.close()
    check([])
    packet=storage.receipt()
    check([])
    require(chunk is None and verified == doc["chunks"] and packet == doc["new_records"][owner.TARGETS[0]],
            "every old signed source byte covered by its original index")
    return storage,rows,dict(kind="whole_original_WSS_source_recovered_for_new_physical_response_v1",
        actual=specs["actual"]["sha256"],execution=specs["execution"]["sha256"],manifest=specs["manifest"]["sha256"],
        original_run=doc["identity"]["run_id"]+"/1",complete_chunks=len(verified),
        original_whole_packet=packet,old_polarization_and_norm_target_calls=0)
