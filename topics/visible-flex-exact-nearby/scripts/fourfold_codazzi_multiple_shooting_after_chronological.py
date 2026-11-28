"""Qualify an actual terminal GDC failure and recover only its required whole physical packets."""
from collections import deque
import gc
from hashlib import sha1,sha256
import json
from pathlib import Path
import queue
import time


def require(ok,msg):
    if not ok:
        raise ValueError(msg)


def verify(raw,s):
    require(len(raw)==s["bytes"] and sha256(raw).hexdigest()==s["sha256"]
        and sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()==s["git_blob_sha"],"whole "+s["path"])


def admit(raw,exraw,mraw,specs,gdc,gg,old):
    for b,s in zip((raw,exraw,mraw),specs):
        verify(b,s)
    a,e,m=map(json.loads,(raw,exraw,mraw))
    require(m["operation"]["scientific_entry_role"]=="signed_grassmann_defect_owner" and a["kind"]==gdc.KIND
        and a["scientific_modules"]==m["operation"]["scientific_module_binding"]
        and a["parameters"]==m["parameters"] and a["certificate_parameters"]==m["operation"]["certificate_parameters"]
        and a["run_id"]==e["run_id"]=="46144819361" and a["run_attempt"]==e["run_attempt"]=="1"
        and a["workflow_event_commit"]==e["workflow_event_commit"]=="1a91ec19410f9a31a60f56fd201da69f652a5925"
        and a["actual_checkout_commit"]==e["actual_scientific_checkout"]
        and a["manifest_sha256"]==e["manifest_sha256"]==specs[2]["sha256"]
        and a["complete_current_file_receipts"]==e["current_input_receipts"]==m["files"]
        and e["historical_restoration"]["historical_input_count"]==21 and e["finished_utc"]
        and e["scientific_finished_utc"] and e["scientific_children"]==1 and e["failure"]
        and e["actual_child_returncode"] not in (0,None) and not e["scientific_complete"]
        and e["completed_old_targets_recomputed"]==0 and not a["complete"]
        and a["completed_targets"]==e["completed_target_names"] in ([],gdc.TARGETS[:1])
        and a["current_target"] in (None,*gdc.TARGETS[:2])
        and e["scientific_files"]==[{k:specs[0][k] for k in ("path","bytes","sha256")}],
        "actual terminal GDC result without any already certified complete low BVP")
    def identity(value):
        raw=(json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
        return dict(bytes=len(raw),sha256=sha256(raw).hexdigest())
    native=e["historical_restoration"]
    require(a["complete_restoration_receipts"]==dict(kind="whole_same_outcome_execution_object_reference_v1",
        path=specs[1]["path"],json_path=["historical_restoration"],complete_original_object_identity=identity(native),
        historical_input_count=21,original_WVC_restoration_identity=identity(native["original_WVC_restoration"]),
        whole_original_object_must_be_published_in_same_outcome=True) and len(m["files"])==109
        and len(m["historical_inputs"])==21,"complete original same-outcome native WVC and 21 identities")
    if a["completed_targets"]==gdc.TARGETS[:1]:
        first=a["certificate"]["first_new_cell82"]
        gdc.positive_lower(first["complete_new_denominator_lower"])
        require(not first["old_Grassmann_scalar_gate_recomputed"] and not first["used_original_denominator_witness"],
                "preserve the independently paid previous GDC first cell without rerunning its proof")
    c=a["certificate"]
    require(c["true_model"] is None and not c["actual_low_hybrid_inverse_proved"]
        and not c["sources"] and all(c["restored_original81"].get(k)==v for k,v in gg.OLD.items())
        and c["original_failed_GG"]["old_graphs"]["whole_packets"]==old.PACKETS_INDEX
        and c["original_failed_GG"]["old_graphs"]["whole_matrices"]==old.MATRICES_INDEX
        and c["original_failed_GG"]["old_graphs"]["whole_frames"]==old.FRAMES_INDEX,
        "the original restored physical GDC input scope is genuine")
    rec=c.get("packet_carriers")
    require(isinstance(rec,dict) and rec["whole_cell_indices"]==sorted(set(rec["whole_cell_indices"]))
        and rec["whole_cell_indices"][:89]==list(range(89)) and rec["whole_cell_indices"][-1]<1424
        and rec["whole_cell_count"]==len(rec["whole_cell_indices"]) and rec["whole_cell_file_bytes"]>=185822772
        and len(rec["whole_cell_carrier_index_sha256"])==64,"whole private packet index of actual terminal GDC")
    return a


def restore_and_run(*,e,np,flint,km,green,refined,flow,context,provider,charts,balances,original,restore,gg_failed,
                    old_reader,gdc_actual,carriers,math_module,method,env,model_module,private_bytes,
                    directory,native_directory,started,wall,progress,finish_blocks,finish_model,finish_maps,save_final):
    root=Path(directory)
    root.mkdir(parents=True,exist_ok=False)
    lim=carriers.PRIVATE_BUDGET
    pool=store=None
    peak_rss=peak_disk=0
    last_disk=0.
    def budget(force=False):
        nonlocal peak_rss,peak_disk,last_disk
        rss=carriers.aggregate_rss_bytes(pool.processes if pool else ())
        peak_rss=max(peak_rss,rss)
        require(rss<=lim["maximum_aggregate_parent_and_worker_rss_bytes"],"whole private process fleet")
        now=time.monotonic()
        if force or now-last_disk>=5.:
            peak_disk=max(peak_disk,private_bytes((root,native_directory)))
            last_disk=now
            require(peak_disk<=lim["maximum_private_directory_bytes"],"whole native data and private files")
        require(now-started<wall,"complete original scientific wall bound")
    class PacketPool(carriers.WholePacketCarriers):
        new_missing=None
        def _fill(self):
            if self.new_missing is None:
                return super()._fill()
            while self.new_missing and len(self.pending)<8:
                j=self.new_missing.popleft()
                require(j not in self.records and j not in self.pending,"one truly missing new whole packet")
                self.incoming.put(j)
                self.pending.add(j)
            self.maximum_submitted=max(self.maximum_submitted,len(self.pending))
    try:
        full=restore.restore_whole_prefix(e.api,flint,km,green,refined,flow,context,provider,charts,balances,
            original,root/"TF81",lambda k,v:(progress(k,v),budget()))
        require(full["receipt"]==gg_failed["certificate"]["restored_original81"],"same three complete TF81 native carriers")
        progress("whole_original81_matched",full["receipt"])
        def accept(record):
            progress("multiple_shooting_whole_packet", {k:record[k] for k in ("panel","bytes","sha256")})
        pool=PacketPool(e,math_module,root/"packets",budget,accepted=accept)
        pool.install_restored_prefix(full)
        del full
        provider.clear_cache()
        gc.collect()
        first=old_reader.recover(pool,gg_failed,context,provider,balances,flow,budget)
        old_packets=gg_failed["certificate"]["packet_carriers"]
        def whole_cell_match(want):
            got=pool.receipt()
            for k in ("whole_cell_indices","whole_cell_count","whole_cell_file_bytes","whole_cell_carrier_index_sha256"):
                require(got[k]==want[k],"complete original packet data "+k)
        whole_cell_match(old_packets)
        original_packets=gdc_actual["certificate"]["packet_carriers"]
        pending=deque(j for j in original_packets["whole_cell_indices"] if j not in pool.records)
        while pending or pool.pending:
            while pending and len(pool.pending)<8:
                j=pending.popleft()
                pool.incoming.put(j)
                pool.pending.add(j)
            budget()
            try:
                rec=pool.outgoing.get(timeout=2)
            except queue.Empty:
                require(all(p.is_alive() for p in pool.processes),"original packet recovery fleet")
                continue
            require(rec["panel"] in pool.pending and "failure" not in rec,"one previously completed whole packet")
            pool.pending.remove(rec["panel"])
            pool._accept(rec)
        whole_cell_match(original_packets)
        for j in original_packets["whole_cell_indices"]:
            r=pool.records[j]
            b=(pool.directory/r["name"]).read_bytes()
            require(len(b)==r["bytes"] and sha256(b).hexdigest()==r["sha256"],"every required packet read back whole")
        progress("whole_original_GDC_packets_matched",dict(original_GG89=first,original_GDC_run=gdc_actual["run_id"],
            original_GDC_count=original_packets["whole_cell_count"],original_GDC_bytes=original_packets["whole_cell_file_bytes"],
            original_GDC_index=original_packets["whole_cell_carrier_index_sha256"],GDC_graph_or_source_targets_recomputed=0))
        pool.new_missing=deque(i for i in range(1424) if i not in pool.records)
        pool._fill()
        store=carriers.DiskJointStore(e,math_module,root/"multiple-shooting")
        m=model_module.Model(e=e,np=np,method=method,env=env,math_module=math_module,pool=pool,store=store,
                             context=context,progress=progress,budget=budget)
        receipt=m.certify(root,finish_blocks)
        finish_model(receipt)
        maps=m.hs_source_maps()
        finish_maps(maps)
    finally:
        try:
            if pool:
                pool.close()
        finally:
            save_final(pool.receipt() if pool else None,store.receipt() if store else None,
                       dict(peak_whole_worker_rss=peak_rss,peak_whole_native_and_private_disk=peak_disk))
