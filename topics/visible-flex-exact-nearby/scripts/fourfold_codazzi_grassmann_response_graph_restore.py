"""Restore only the certified graph carriers needed by a new signed response.

The old positive source maps and all 1,343 post-prefix covariance packets
are deliberately absent. Output is released only on the original full graph
journal, ordered frame definition index and live matrix index identities.
"""
import gc
import hashlib
import json
import multiprocessing as mp
import os
from pathlib import Path
import platform
import queue
import sys
import time


def require(test,message):
    if not test:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,
                       allow_nan=False)+"\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def unchanged_source(module,role,plan):
    spec = next(s for s in plan["files"] if s["role"] == role)
    raw = Path(module.__file__).read_bytes()
    require(len(raw) == spec["bytes"] and sha(raw) == spec["sha256"],"whole original "+role)


def restore_graph(*, np,flint,engine,math_module,carriers,runner,restore,green,refined,flow,
                  context,provider,charts,balances,tf_admission,gg_validator,gg_inputs,
                  private_directory,native_directory,progress,wall_deadline):
    """Return private model after the same real, wholly verified graph exists.

    gg_inputs gives (actual_bytes,execution_bytes,manifest_bytes,kwargs) for
    the original whole-file validator. Run metadata admission before any
    numerical import in the calling owner, and reconfirm original bytes here.
    """
    require(os.environ.get("GITHUB_ACTIONS") == "true" and
            os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public" and
            platform.python_version() == "3.12.14" and flint.__version__ == "0.9.0" and
            np.__version__ == "2.3.5" and flint.ctx.prec == 384 and sys.byteorder == "little"
            and platform.machine() == "x86_64" and all(os.environ.get(k) == "1" for k in
                    ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS")),
            "original full graph replay runtime")
    actual_raw,execution_raw,plan_raw,kw = gg_inputs
    gg_validator.admit_success(actual_raw,execution_raw,plan_raw,**kw)
    actual,plan = json.loads(actual_raw),json.loads(plan_raw)
    cert = actual["certificate"]
    for module,role in ((math_module,"grassmann_math"),(carriers,"grassmann_carriers"),
            (runner,"grassmann_runner"),(gg_validator,"grassmann_validator"),
            (restore,"original81_restore"),(flow,"true_low193_direct_flow_math"),
            (green,"low_centre_verified_green_math"),(refined,"low_centre_refined_green_math")):
        unchanged_source(module,role,plan)
    require(engine.green is green and engine.flow is flow and provider.context is context
            and context.reference_identity == actual["reference_identity"]
            and len(context.domain.cells) == 1424 and len(balances) == 155,
            "the original hybrid, complete data and true-root domain")
    root = Path(private_directory)
    root.mkdir(parents=True,exist_ok=False)
    flows,frames = root/"flows",root/"frames"
    flows.mkdir()
    frames.mkdir()
    e,api,km = engine,engine.api,engine.km
    n_cells = len(context.domain.cells)
    workers = []
    limits = carriers.PRIVATE_BUDGET
    state = {"peak_rss":0,"peak_disk":0,"last_disk":0.}
    def budget(force=False):
        now = time.monotonic()
        rss = carriers.aggregate_rss_bytes(workers)
        state["peak_rss"] = max(state["peak_rss"],rss)
        require(rss <= limits["maximum_aggregate_parent_and_worker_rss_bytes"],"whole process memory")
        if force or now-state["last_disk"] >= 5:
            used = runner.private_bytes((root,native_directory))
            state["peak_disk"] = max(state["peak_disk"],used)
            state["last_disk"] = now
            require(used <= limits["maximum_private_directory_bytes"],"whole live private and native bytes")
        require(now < wall_deadline,"whole response graph recovery wall time")

    # Only two actual homogeneous directions, in the same joint binary64
    # representation as the two corresponding fields of the private GG packet.
    width = limits["full_joint_matrix_payload_bytes"]
    def write_pair(i,a,b):
        payload = carriers.packed_ball(e,a)+carriers.packed_ball(e,b)
        require(len(payload) == 2*width,"both full 193-square homogeneous balls")
        carriers.atomic(flows/(str(i)+".pair"),payload)
        return sha(payload)

    hashes = {}
    budget(True)
    old = restore.restore_whole_prefix(api,flint,km,green,refined,flow,context,provider,
        charts,balances,tf_admission,root/"original",lambda stage,detail:budget())
    require(old["receipt"] == cert["restored_original81"] and old["first_uncompleted_cell"] == 81,
            "all original accepted carrier bytes including passive forward/backward identity")
    for i in range(81):
        bank = old["passively_saved_raw_flows"]
        hashes[i] = write_pair(i,bank.get(("restored_raw_forward",i)),bank.get(("restored_raw_backward",i)))
        budget()
    del old,bank
    provider.clear_cache()
    gc.collect()
    store = carriers.DiskJointStore(e,math_module,root/"graphs")
    # Reuse the original exact proposed-vector file format without pretending
    # to have a complete seven-matrix packet object.
    class Frames:
        def __init__(self):
            self.directory,self.frame_records = frames,{}
    defs = Frames()
    def freeze(i,vectors):
        return carriers.WholePacketCarriers.freeze_vectors(defs,i,vectors)

    ctx = mp.get_context("fork")
    jobs,finished = ctx.Queue(maxsize=8),ctx.Queue(maxsize=8)
    expected_counts = cert["true_model"]["accepted_subbox_counts"]
    def worker():
        while True:
            i = jobs.get()
            if i is None:
                return
            try:
                factor = balances[context.domain.cells[i]["parent_panel"]]
                nums = carriers.positive_tail_cuts(e,context,provider,flow,i,factor)
                require(len(nums)-1 == expected_counts[i],"same count of genuine directed Peano leaves")
                cuts = [context.domain.fone*n/64 for n in nums]
                pair = flow.true_cell_packet(api,km,context,provider,i,cuts,factor,
                                             order=16,source_provider=None,source_roles=())
                require(pair["true_moments"] is None and pair["forward_increment"] is None
                        and pair["all193_coordinates_retained"] and not pair["actual_S_changed"],
                        "homogeneous carrier recovery without old covariance roles")
                digest = write_pair(i,pair["forward"],pair["backward"])
                finished.put((i,digest,None))
            except BaseException as exc:
                finished.put((i,None,type(exc).__name__+": "+str(exc)))
                return

    pending,next_index = set(),81
    def fill():
        nonlocal next_index
        while len(pending)<8 and next_index<1424:
            jobs.put(next_index)
            pending.add(next_index)
            next_index += 1
    def matrix(i,direction):
        while i not in hashes:
            budget()
            try:
                j,digest,failure = finished.get(timeout=3)
            except queue.Empty:
                require(all(p.is_alive() for p in workers),"loss of a graph recovery worker")
                continue
            require(j in pending and digest is not None and failure is None,
                    "whole homogeneous transition: "+str((j,failure)))
            hashes[j] = digest
            pending.remove(j)
            fill()
        payload = (flows/(str(i)+".pair")).read_bytes()
        require(sha(payload) == hashes[i] and len(payload) == 2*width and direction in (0,1),
                "whole physical homogeneous pair at every use")
        return carriers.unpacked_ball(e,math_module,193,193,payload[direction*width:(direction+1)*width])

    # A graph record includes the *whole* denominator, residual, radius and
    # inverse enclosures, in addition to the privately stored exact matrices.
    ledger = sha(b"R149-GG-v1")
    def public(value):
        if hasattr(value,"mid_rad_10exp"):
            return carriers.scalar(value)
        if isinstance(value,dict):
            return {k:public(v) for k,v in value.items() if k != "private_model_token"}
        if isinstance(value,(tuple,list)):
            return [public(v) for v in value]
        require(value is None or isinstance(value,(int,float,bool,str)),"whole original public record")
        return value
    def record(stage,data):
        nonlocal ledger
        ledger = sha(bytes.fromhex(ledger)+canonical([stage,public(data)]))
    def stop_workers():
        for p in workers:
            if p.is_alive():
                p.terminate()
        for p in workers:
            p.join(timeout=5)
        require(all(not p.is_alive() for p in workers),"whole recovery worker teardown")
    try:
        for unused in range(4):
            worker_process = ctx.Process(target=worker)
            worker_process.start()
            workers.append(worker_process)
        fill()
        P,Q,N = 97,96,193
        frame = math_module.certify_householder_frame(e,[])
        Z = e.zero(Q,P)
        store.put(("frame",0),frame)
        store.put(("Z",0),Z)
        for i in range(n_cells):
            forward = matrix(i,0)
            cols = e.product(forward,frame,e.vcat(e.eye(P),
                math_module.MatrixBall(e,Z.c,api.zero,Z.centre_norm()))).c
            vectors = freeze(i+1,math_module.propose_householders(np,e,cols))
            next_frame = math_module.certify_householder_frame(e,vectors)
            trans = e.product(e.transpose(next_frame),forward,frame)
            Z,C,row = math_module.advance_graph(e,trans,Z)
            store.put(("frame",i+1),next_frame)
            store.put(("Z",i+1),Z)
            store.put(("Uinv",i),C)
            frame,Z = store.get(("frame",i+1)),store.get(("Z",i+1))
            record("new_joint_left_graph",dict(complete_cells=i+1,whole_cells=n_cells,
                original_TF_accepted_records_reissued=0,index=i,complete_record=row))
            progress("restore_complete_left_graph",{"cells":i+1})
            budget()
        stop_workers()
        require(len(hashes) == n_cells and not pending,"complete homogeneous input to graphs")
        outer = math_module.original_outer_boundary(e,frame)
        Y = e.scale(-api.one,e.multiply(e.inverse(e.columns(outer,range(P))),e.columns(outer,range(P,N))))
        ni = math_module.store_complete_node(e,store,n_cells,frame,Z,Y)
        record("new_joint_outer_node",dict(index=n_cells,transversality_inverse_upper=ni))
        store.remove(("Z",n_cells))
        swap = tuple(range(P,N))+tuple(range(P))
        for i in range(n_cells-1,-1,-1):
            last = store.get(("frame",i))
            trans = e.product(e.transpose(last),matrix(i,1),frame)
            Y,D,row = math_module.advance_graph(e,e.submatrix(trans,swap,swap),Y)
            store.put(("Vinv",i),D)
            Z = store.get(("Z",i))
            ni = math_module.store_complete_node(e,store,i,last,Z,Y)
            store.remove(("Z",i))
            frame = last
            record("new_joint_right_graph_and_transversality",dict(complete_cells=n_cells-i,
                whole_cells=n_cells,complete_nodes=n_cells-i+1,index=i,complete_record=row,
                transversality_inverse_upper=ni))
            progress("restore_complete_right_nodes",{"cells":n_cells-i})
            budget()
    finally:
        stop_workers()
        jobs.cancel_join_thread()
        jobs.close()
        finished.close()

    # The published journal continued past the last graph record with a
    # fixed metadata-only word per *previously admitted* map cell. Complete
    # the prior record's serialization. No covariance execution is reported.
    graph_prefix = ledger
    for i in range(n_cells):
        record("new_joint_four_complete_source_covariances",{
            "complete_cells":i+1,"whole_cells":n_cells,"roles":list(math_module.ROLES)})
    require(ledger == cert["joint_inclusions"]["whole_ordered_record_chain_sha256"],
            "whole original directed graph/node journal with literal admitted suffix")
    expected = cert["packet_carriers"]
    frame_index = hashlib.sha256(b"complete_R149_exact_rational_frame_vectors_index_v1")
    require(set(defs.frame_records) == set(range(1,1425)),"every exact Householder definition")
    for i in sorted(defs.frame_records):
        r = defs.frame_records[i]
        raw = (frames/r["name"]).read_bytes()
        require(len(raw) == r["bytes"] and sha(raw) == r["sha256"],"entire saved exact frame")
        frame_index.update(canonical(r))
        budget()
    require(frame_index.hexdigest() == expected["whole_frame_index_sha256"]
            and sum(r["bytes"] for r in defs.frame_records.values()) == expected["whole_frame_file_bytes"],
            "whole original 1424-frame file index")
    mat_receipt = store.receipt()
    require(mat_receipt == cert["joint_matrices"],"whole live matrix index and every original graph write")
    for key in sorted(store.data):
        data = store.data[key]
        raw = (store.directory/data["name"]).read_bytes()
        require(len(raw) == data["bytes"] and sha(raw) == data["sha256"],"all actual live matrix bytes")
        budget()
    budget(True)
    model = {"kind":"R149_actual_low193_joint_Grassmann_inverse_v1","context":context,"joint_store":store,
             "complete_refined_cells":n_cells,"true_hybrid_BVP_verified":True,"private_model_token":object()}
    return model,{"same_original_gg_run":actual["run_id"]+"/1","frame_index":frame_index.hexdigest(),
        "live_graph_matrix_index":mat_receipt["whole_live_matrix_index_sha256"],
        "graph_write_journal":mat_receipt["whole_write_journal_sha256"],
        "actual_graph_record_prefix":graph_prefix,"whole_original_record_journal":ledger,
        "peak_graph_recovery_rss":state["peak_rss"],"peak_recovery_disk":state["peak_disk"],
        "post81_old_covariance_packets_or_maps_recomputed":0,"original_source_norm_targets_reissued":0}
