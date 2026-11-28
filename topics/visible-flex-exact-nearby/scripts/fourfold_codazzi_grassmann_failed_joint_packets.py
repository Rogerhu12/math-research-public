"""Admit the actual failed GG and recover exactly its 89 closed packets, before starting new science."""
from hashlib import sha256
import itertools
import json
from pathlib import Path
import queue

ACTUAL=(61622,"183e1b223c015b2c591133bebb5741ca9eec0d02c74b7055192d1c2c59f575cd")
EXECUTION=(68240,"f3de409e81db324211cb2c66f6bbff14811ed3542a3c72099ec20de87915cc15")
MANIFEST=(72126,"e5f106998e4456d951183c05ace1cd2930d67fb7b8ffe207749dba6136799c19")
PACKET_CHAIN="61e66e72eecdf989305547f10bdec90b0f97ec078cc7d7228cec470ce6bda9f4"
OLD_SCALAR_CHAIN="df33217279c5fc9d2717b0a3815e44d8aa507ade1f5186cc63195747f8f73434"
PACKETS_INDEX="a64b34280dc6adad784589085ba6039c7f8cc19077be988aee15a35ad26c8e52"
FRAMES_INDEX="bb0c87191792f278615889be4cfa95413845c60bb031a749bfac817ee5990574"
MATRICES_INDEX="9fd5ef9f1ca8b8b5331b1cff704b0d6af1d7b6b08b1064c1693fba3d629fd292"
MATRIX_JOURNAL="108f895c53394560171651408584a00aa21e370846c64dc69dfcffd843c53aa3"


def require(ok,msg):
    if not ok:
        raise ValueError(msg)


def canonical(v):
    return (json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()


def admit(actual_raw,execution_raw,manifest_raw,qualifier):
    for raw,spec in zip((actual_raw,execution_raw,manifest_raw),(ACTUAL,EXECUTION,MANIFEST)):
        require((len(raw),sha256(raw).hexdigest())==spec,"the entire immutable original failed GG triple")
    a,e,m=map(json.loads,(actual_raw,execution_raw,manifest_raw))
    require(a["kind"]==qualifier.KIND and a["complete"] is False and not a["proved"] and
        a["actual_returncode"]==e["actual_child_returncode"]==1 and not e["scientific_complete"]
        and a["run_id"]==e["run_id"]=="46135063788" and a["run_attempt"]==e["run_attempt"]=="1"
        and a["manifest_sha256"]==e["manifest_sha256"]==MANIFEST[1]
        and a["actual_checkout_commit"]==e["actual_scientific_checkout"]
        and a["workflow_event_commit"]==e["workflow_event_commit"]=="60016291d42e88e9f12d62c3c367fbe6cce4aa22"
        and e["failure"] and a["failure"]["message"]=="strict centred Grassmann denominator"
        and not a["failure"]["actual_operator_singularity_inferred"]
        and a["complete_current_file_receipts"]==e["current_input_receipts"]==m["files"]
        and a["scientific_modules"]==m["operation"]["scientific_module_binding"]
        and len(m["files"])==98 and len(m["historical_inputs"])==e["historical_restoration"]["historical_input_count"]==21
        and not a["completed_targets"] and a["current_target"]==qualifier.TARGETS[0]
        and e["completed_target_names"]==[] and a["actual_progress"]["actual_left_cells_complete"]==81
        and a["actual_progress"]["actual_right_cells_complete"]==a["actual_progress"]["actual_source_cells_complete"]==0,
        "the original first physical graph failure with exactly 81 completed left scalar records")
    c=a["certificate"]
    ledger=qualifier.unpack_powers(c["joint_inclusions"])
    require(len(ledger["left"])==81 and not ledger["right"] and not ledger["nodes"]
        and ledger["left"][-1]==[-1,1] and ledger["whole_ordered_record_chain_sha256"]==OLD_SCALAR_CHAIN
        and c["true_model"] is None
        and c["joint_matrices"]["whole_live_matrix_index_sha256"]==MATRICES_INDEX
        and c["joint_matrices"]["whole_write_journal_sha256"]==MATRIX_JOURNAL
        and c["joint_matrices"]["whole_live_matrices"]==c["joint_matrices"]["all_matrix_writes"]==245
        and c["joint_matrices"]["whole_live_bytes"]==36669520
        and c["packet_carriers"]["whole_cell_carrier_index_sha256"]==PACKETS_INDEX
        and c["packet_carriers"]["whole_frame_index_sha256"]==FRAMES_INDEX
        and c["packet_carriers"]["whole_frame_count"]==82 and c["packet_carriers"]["whole_frame_file_bytes"]==12283518
        and c["packet_carriers"]["whole_cell_indices"]==list(range(89))
        and c["packet_carriers"]["whole_cell_file_bytes"]==185822772
        and c["complete_packet_prefix"]==dict(restored=81,post81=8,maximum_index=88,receipt_chain_sha256=PACKET_CHAIN)
        and c["restored_original81"]["whole_original_actual_sha256"]==qualifier.OLD["whole_original_actual_sha256"],
        "old scalar history plus separately hashed 245 original graph matrices, 82 frames and 89 packets")
    return a


def recover(pool,old,context,provider,balances,flow,budget):
    """Only the original81 + eight actual existing packet bytes can enter the new signed graph.

    Caller has installed exactly TF's original81 from its three authenticated original objects.
    Original public GG recorded an ordered arrival hash for 81..88 but did not publish their
    individual arrival order. Derive it from all eight verified whole files and that actual hash.
    """
    require(set(pool.records)==set(range(81)) and pool.next_panel==81 and not pool.pool_started,
            "the whole original TF data immediately before the eight missing GG packet carriers")
    pool.start_workers(context,provider,balances,flow)
    require(pool.next_panel==89 and pool.pending==set(range(81,89)),"only the actual old eight packets scheduled")
    while pool.pending:
        budget()
        try:
            rec=pool.outgoing.get(timeout=2)
        except queue.Empty:
            require(all(p.is_alive() for p in pool.processes),"original packet recovery workers remain present")
            continue
        i=rec["panel"]
        require(i in pool.pending and "failure" not in rec,"same original complete packet "+str(rec))
        pool.pending.remove(i)
        pool._accept(rec)
    records={}
    for i in range(89):
        r=pool.records[i]
        b=(pool.directory/r["name"]).read_bytes()
        require(len(b)==r["bytes"] and sha256(b).hexdigest()==r["sha256"],"entire ordered original packet file")
        records[i]=canonical({k:r[k] for k in ("panel","bytes","sha256")})
        budget()
    first=sha256(b"GG-received-packets").digest()
    for i in range(81):
        first=sha256(first+records[i]).digest()
    found=[]
    last=old["preparation_prefix"]["detail"]
    require(last==json.loads(records[88]),"the actual terminal received packet and its complete size and digest")
    # The stored preparation prefix identifies the last receipt as 88.
    for perm in itertools.permutations(range(81,88)):
        value=first
        for i in (*perm,88):
            value=sha256(value+records[i]).digest()
        if value.hex()==PACKET_CHAIN:
            found.append([*perm,88])
    require(len(found)==1,"one whole original GG 89-packet byte identity and original receipt order")
    receipt=dict(actual=ACTUAL[1],execution=EXECUTION[1],manifest=MANIFEST[1],restored_packets=89,
        whole_original_packet_bytes=sum(pool.records[i]["bytes"] for i in range(89)),
        original_89_receipt_chain=PACKET_CHAIN,original_8_arrival_order=found[0],
        original_81_graph_scalar_record_chain=OLD_SCALAR_CHAIN,
        old_failed_graph_gate_calls=0)
    return receipt


def restore_graph_carriers(*,e,np,math_module,pool,old,oldstore,budget,progress):
    """Recover the actual partial matrix and frame objects, including the failed transition's defined frame only."""
    api=e.api
    frame=math_module.certify_householder_frame(e,[])
    Z=e.zero(96,97)
    oldstore.put(("frame",0),frame)
    oldstore.put(("Z",0),Z)
    chain=sha256(b"R149-GG-v1").digest()
    def public(x):
        if hasattr(x,"mid_rad_10exp"):
            m,r,p=x.mid_rad_10exp(48)
            return dict(kind="complete_decimal_ball_v1",midpoint_integer=str(int(m)),radius_integer=str(int(r)),
                        decimal_exponent=str(int(p)),semantics="the exact directed scalar lies in (midpoint +/- radius)*10^exponent")
        if isinstance(x,dict):
            return {k:public(v) for k,v in x.items()}
        return x
    for i in range(82):
        f=pool(i,"left")["forward"]
        col=e.product(f,frame,e.vcat(e.eye(97),math_module.MatrixBall(e,Z.c,api.zero,Z.centre_norm()))).c
        vec=pool.freeze_vectors(i+1,math_module.propose_householders(np,e,col))
        next_frame=math_module.certify_householder_frame(e,vec)
        if i==81:
            break
        trans=e.product(e.transpose(next_frame),f,frame)
        Z,U,row=math_module.advance_graph(e,trans,Z)
        oldstore.put(("frame",i+1),next_frame)
        oldstore.put(("Z",i+1),Z)
        oldstore.put(("Uinv",i),U)
        frame,Z=oldstore.get(("frame",i+1)),oldstore.get(("Z",i+1))
        chain=sha256(chain+canonical(["new_joint_left_graph",public(dict(complete_cells=i+1,whole_cells=1424,
            original_TF_accepted_records_reissued=0,index=i,complete_record=row))])).digest()
        progress("restore_original_245_matrix_objects",{"complete_original_left_carrier_cells":i+1})
        budget()
    c=old["certificate"]
    require(chain.hex()==OLD_SCALAR_CHAIN and pool.receipt()==c["packet_carriers"]
        and oldstore.receipt()==c["joint_matrices"],"the entire original scalar journal, 245 live matrices, 82 frame and 89 packet objects")
    for store,directory in ((oldstore.data,oldstore.directory),(pool.frame_records,pool.directory)):
        for key,spec in store.items():
            raw=(directory/spec["name"]).read_bytes()
            require(len(raw)==spec["bytes"] and sha256(raw).hexdigest()==spec["sha256"],"whole recovered native object "+str(key))
        budget()
    return next_frame,dict(whole_packets=PACKETS_INDEX,whole_frames=FRAMES_INDEX,whole_matrices=MATRICES_INDEX,
        whole_write_journal=MATRIX_JOURNAL,whole_graph_scalar_journal=OLD_SCALAR_CHAIN,
        old_failed_denominator_calls=0,old_scientific_targets_reissued=0)
