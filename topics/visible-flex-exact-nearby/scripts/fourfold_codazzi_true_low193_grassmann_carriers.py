"""Private whole carriers and four deterministic single-thread TF packet workers.

No numerical work at import. The original 81 cells enter only after the
three whole restoration hashes pass. New cells81..1423 each compute all
four source roles and all five raw193 moments exactly once. Private files
are complete binary objects; no arrays enter git, Release or artifacts.
"""
from __future__ import annotations
import hashlib
import json
import math
import multiprocessing
import os
import queue
import struct
import sys
import traceback
from array import array
from collections import OrderedDict
from pathlib import Path

N, P, Q = 193, 97, 96
ROLES = ("ordinary_raw_low_source", "transformed_low_source",
         "low_second_kind_correction", "centre_high0_return_source")
MATRIX_NAMES = ("forward", "backward", "output")+ROLES
MAGIC = b"R149-GG-whole-packet-v1\0"
FRAME_MAGIC = b"R149-GG-whole-frame-v1\0"
MATRIX_MAGIC = b"R149-GG-whole-joint-matrix-v1\0"
PRIVATE_BUDGET = {
    "complete_new_cells": 1343, "restored_cells": 81, "whole_cells": 1424,
    "worker_processes": 4, "threads_per_process": 1,
    "maximum_submitted_unreceived_cells": 8,
    "new_order": 16, "initial_new_subboxes_per_cell": 4, "maximum_dyadic_denominator": 64,
    "full_joint_matrix_payload_bytes": 298008,
    "seven_joint_matrices_per_cell_payload_bytes": 2086056,
    "all1424_seven_matrix_payload_bytes": 2970543744,
    "all1424_full_frame_vector_payload_bytes": 213269632,
    "maximum_private_packet_file_bytes": 2100000,
    "maximum_private_joint_store_bytes": 2147483648,
    "maximum_private_directory_bytes": 8589934592,
    "maximum_aggregate_parent_and_worker_rss_bytes": 15032385536,
    "maximum_parent_matrix_decode_entries": 200000,
    "maximum_private_packet_decode_cache": 1,
    "maximum_outstanding_queue_record_bytes": 65536,
    "parent_receives_graph_cells_in_original_order": True,
    "all_four_roles_and_five_moments_per_cell": True,
    "only_small_file_receipts_cross_process_queues": True,
    "large_raw_packet_arrays_kept_on_private_disk": True,
    "old_prefix_release_requires_all_three_hashes": True,
}
_WORK = None


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value,sort_keys=True,ensure_ascii=False,allow_nan=False,
                       separators=(",", ":"))+"\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def atomic(path, raw):
    path = Path(path)
    temporary = path.with_name(path.name+".tmp-"+str(os.getpid()))
    temporary.write_bytes(raw)
    temporary.replace(path)
    require(path.read_bytes() == raw, "whole private carrier write/read equality")


def scalar(value):
    require(value.is_finite(), "finite complete statistic")
    mid,rad,exponent = value.mid_rad_10exp(48)
    return {"kind":"complete_decimal_ball_v1", "midpoint_integer":str(int(mid)),
        "radius_integer":str(int(rad)), "decimal_exponent":str(int(exponent)),
        "semantics":"the exact directed scalar lies in (midpoint +/- radius)*10^exponent"}


def decimal_ball(api, value):
    require(value["kind"] == "complete_decimal_ball_v1", "one full decimal enclosure")
    mid,rad,power = (int(value[key]) for key in
                    ("midpoint_integer","radius_integer","decimal_exponent"))
    require(rad >= 0, "nonnegative full decimal radius")
    scale = api.rational(10)**power
    return api.interval(api.rational(mid-rad)*scale,api.rational(mid+rad)*scale)


def packed_ball(engine, value):
    """Exact dyadic centre; only two norm uppers are rounded outward."""
    value = engine.as_ball(value)
    payload = array("d")
    for row in value.c.values:
        for entry in row:
            number = float(entry)
            require(engine.exact_float(number) == entry, "whole unchanged dyadic centre")
            payload.append(number)
    def outward(bound):
        bound = engine.upper(bound)
        number = float(bound)
        require(math.isfinite(number) and number >= 0, "finite directed private bound")
        for unused in range(8):
            if bool(engine.exact_float(number) >= bound):
                return number
            number = math.nextafter(number,math.inf)
        raise ValueError("outward whole-matrix radius packing")
    payload.extend((outward(value.r),outward(value.norm())))
    if sys.byteorder != "little":
        payload.byteswap()
    return payload.tobytes()


def unpacked_ball(engine, math_module, rows, cols, raw):
    require(len(raw) == (rows*cols+2)*8, "complete whole-matrix payload")
    values = array("d"); values.frombytes(raw)
    if sys.byteorder != "little":
        values.byteswap()
    require(all(math.isfinite(x) for x in values) and values[-2] >= 0 and values[-1] >= 0,
            "finite full joint matrix and its two nonnegative bounds")
    centre = engine.km.Matrix(rows,cols,[[engine.exact_float(values[i*cols+j])
                          for j in range(cols)] for i in range(rows)])
    return math_module.MatrixBall(engine,centre,engine.exact_float(values[-2]),
                                  engine.exact_float(values[-1]))


def encode_packet(engine, packet, origin, order):
    require(packet["all193_coordinates_retained"] is True and packet["actual_S_changed"] is False
        and set(packet["true_moments"]["inputs"]) == set(ROLES),
        "all original193 coordinates, physical S and every source role")
    matrices = {"forward":packet["forward"], "backward":packet["backward"],
        "output":packet["true_moments"]["output"], **packet["true_moments"]["inputs"]}
    require(all(v.shape == (N,N) for v in matrices.values()), "all seven whole193 matrices")
    parts = [packed_ball(engine,matrices[name]) for name in MATRIX_NAMES]
    require(all(len(part) == PRIVATE_BUDGET["full_joint_matrix_payload_bytes"] for part in parts),
            "complete exact private packet dimension")
    header = {"kind":"complete_private_R149_joint_cell_packet_v1", "panel":packet["panel"],
        "origin":origin,"Peano_order":order,"subboxes":packet["subboxes"],
        "cut_numerators_over_64":packet["cut_numerators_over_64"],
        "all193_coordinates_retained":True,"actual_S_changed":False,
        "matrix_names":list(MATRIX_NAMES),"matrix_shape":[N,N],
        "source_roles":list(ROLES),"source_columns":[193,193,193,128],
        "payload_layout":"little-endian binary64 exact centres, then joint radius and norm upper",
        "matrix_payload_bytes":len(parts[0]),"whole_payload_bytes":sum(map(len,parts)),
        "statistics":{key:scalar(packet[key]) for key in
            ("beta_sum_upper","beta2_sum_upper","complete_raw_prefix_and_inverse_upper",
             "largest_local_tail_upper")}}
    encoded = canonical(header)
    raw = MAGIC+struct.pack("<Q",len(encoded))+encoded+b"".join(parts)
    require(len(raw) <= PRIVATE_BUDGET["maximum_private_packet_file_bytes"],
            "whole local private packet byte cap")
    return raw,header


def read_packet_header(raw):
    require(raw.startswith(MAGIC), "whole private packet magic")
    offset = len(MAGIC)
    size = struct.unpack("<Q",raw[offset:offset+8])[0]
    require(0 < size < 10000, "whole private packet header cap")
    start = offset+8
    header = json.loads(raw[start:start+size])
    require(raw[start:start+size] == canonical(header)
        and header["kind"] == "complete_private_R149_joint_cell_packet_v1"
        and header["matrix_names"] == list(MATRIX_NAMES) and header["matrix_shape"] == [N,N]
        and header["source_roles"] == list(ROLES) and header["source_columns"] == [193,193,193,128]
        and header["all193_coordinates_retained"] is True and header["actual_S_changed"] is False
        and header["matrix_payload_bytes"] == PRIVATE_BUDGET["full_joint_matrix_payload_bytes"]
        and header["whole_payload_bytes"] == PRIVATE_BUDGET["seven_joint_matrices_per_cell_payload_bytes"]
        and start+size+header["whole_payload_bytes"] == len(raw), "whole packet schema and bytes")
    cuts = header["cut_numerators_over_64"]
    require(type(cuts) is list and cuts == sorted(set(cuts))
            and all(type(n) is int and 0 <= n <= 64 for n in cuts)
            and {0,16,32,48,64} <= set(cuts) and len(cuts)-1 == header["subboxes"]
            and all(b-a in (1,2,4,8,16) and a%(b-a) == 0 for a,b in zip(cuts,cuts[1:])),
            "complete ordered partition with original quarters and only dyadic descendant leaves")
    if header["origin"] == "restored_original81_flow_and_moments":
        require(cuts == [0,16,32,48,64], "unchanged original accepted four-subbox partition")
    return header,start+size


class DiskJointStore:
    """Complete new frame/graph/node matrices on private disk, with bounded decoded cache."""
    def __init__(self, engine, math_module, directory):
        self.e,self.math,self.directory = engine,math_module,Path(directory)
        self.directory.mkdir(parents=True,exist_ok=False)
        self.data,self.cache = {},OrderedDict()
        self.live_bytes,self.peak_bytes,self.decoded_entries,self.counter = 0,0,0,0
        self.writes_chain = sha(b"complete_R149_joint_matrix_write_journal_v1")

    def put(self, key, value):
        require(key not in self.data, "one complete matrix per new private key")
        payload = packed_ball(self.e,value)
        header = canonical({"key":list(key),"rows":value.rows,"cols":value.cols,
                            "payload_bytes":len(payload)})
        raw = MATRIX_MAGIC+struct.pack("<Q",len(header))+header+payload
        require(self.live_bytes+len(raw) <= PRIVATE_BUDGET["maximum_private_joint_store_bytes"],
                "complete private joint-store byte cap")
        path = self.directory/(str(self.counter)+".joint")
        self.counter += 1
        atomic(path,raw)
        record = {"key":list(key),"rows":value.rows,"cols":value.cols,
                  "bytes":len(raw),"sha256":sha(raw),"name":path.name}
        self.data[key] = record
        self.writes_chain = sha(bytes.fromhex(self.writes_chain)+canonical(record))
        self.live_bytes += len(raw); self.peak_bytes = max(self.peak_bytes,self.live_bytes)

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        record = self.data[key]
        raw = (self.directory/record["name"]).read_bytes()
        require(len(raw) == record["bytes"] and sha(raw) == record["sha256"]
                and raw.startswith(MATRIX_MAGIC), "whole private joint matrix identity")
        prefix = len(MATRIX_MAGIC)
        size = struct.unpack("<Q",raw[prefix:prefix+8])[0]
        header = json.loads(raw[prefix+8:prefix+8+size])
        require(header == {"key":list(key),"rows":record["rows"],"cols":record["cols"],
                            "payload_bytes":(record["rows"]*record["cols"]+2)*8},
                "whole private joint matrix header")
        out = unpacked_ball(self.e,self.math,record["rows"],record["cols"],raw[prefix+8+size:])
        self.cache[key] = out; self.decoded_entries += out.rows*out.cols
        while self.decoded_entries > PRIVATE_BUDGET["maximum_parent_matrix_decode_entries"] and len(self.cache)>1:
            unused,old = self.cache.popitem(last=False)
            self.decoded_entries -= old.rows*old.cols
        return out

    def remove(self, key):
        record = self.data.pop(key)
        (self.directory/record["name"]).unlink()
        self.live_bytes -= record["bytes"]
        if key in self.cache:
            old = self.cache.pop(key); self.decoded_entries -= old.rows*old.cols

    def receipt(self):
        chain = hashlib.sha256(b"complete_R149_joint_live_private_matrices_v1")
        for key in sorted(self.data):
            chain.update(canonical(self.data[key]))
        return {"whole_live_matrices":len(self.data),"whole_live_bytes":self.live_bytes,
            "maximum_live_bytes":self.peak_bytes,"all_matrix_writes":self.counter,
            "whole_write_journal_sha256":self.writes_chain,
            "whole_live_matrix_index_sha256":chain.hexdigest(),
            "each_whole_matrix_readback_hash_checked":True,
            "arrays_published_to_git_Release_or_artifact":False}


class WholePacketCarriers:
    def __init__(self, engine, math_module, directory, budget, accepted=None):
        self.e,self.math,self.directory = engine,math_module,Path(directory)
        self.directory.mkdir(parents=True,exist_ok=False)
        self.budget,self.accepted = budget,accepted
        self.records,self.frame_records,self.processes,self.pending = {},{},[],set()
        self.incoming,self.outgoing,self.next_panel = None,None,81
        self.pool_started,self.pool_closed = False,False
        self.maximum_submitted = 0

    def _accept(self, record):
        panel = record["panel"]
        require(type(panel) is int and 0 <= panel < 1424 and panel not in self.records,
                "one complete whole-cell carrier acceptance")
        path = self.directory/record["name"]
        require(path.parent == self.directory and path.name == str(panel)+".packet",
                "one original panel file")
        raw = path.read_bytes()
        require(len(raw) == record["bytes"] and sha(raw) == record["sha256"],
                "complete whole private cell carrier identity")
        header,unused_offset = read_packet_header(raw)
        require(header["panel"] == panel and header["origin"] ==
                ("restored_original81_flow_and_moments" if panel < 81 else "new_post81_order16_whole_cell")
                and header["Peano_order"] == (24 if panel < 81 else 16)
                and (4 <= header["subboxes"] <= 64 if panel >= 81 else header["subboxes"] == 4),
                "strict separation of restored prefix and genuinely new packet")
        self.records[panel] = dict(record)
        if self.accepted is not None:
            self.accepted(dict(record))

    def install_restored_prefix(self, restored):
        require(restored["first_uncompleted_cell"] == 81 and len(restored["local_statistics"]) == 81,
                "the complete admitted original81 carrier first")
        source,flows = restored["private_store"],restored["passively_saved_raw_flows"]
        for i,statistics in enumerate(restored["local_statistics"]):
            self.budget()
            packet = {**statistics,"forward":flows.get(("restored_raw_forward",i)),
                "backward":flows.get(("restored_raw_backward",i)),
                "all193_coordinates_retained":True,"actual_S_changed":False,
                "true_moments":{"output":source.get(("true_moment","output",i)),
                    "inputs":{role:source.get(("true_moment",role,i)) for role in ROLES}}}
            packet["cut_numerators_over_64"] = [0,16,32,48,64]
            raw,unused_header = encode_packet(self.e,packet,"restored_original81_flow_and_moments",24)
            path = self.directory/(str(i)+".packet")
            atomic(path,raw)
            self._accept({"panel":i,"name":path.name,"bytes":len(raw),"sha256":sha(raw)})
        require(set(self.records) == set(range(81)), "all original81 converted only after whole verification")

    def start_workers(self, context, provider, balances, flow):
        global _WORK
        require(not self.pool_started and set(self.records) == set(range(81))
                and sys.platform.startswith("linux"), "fork only after complete restored81 carrier conversion")
        require(all(os.environ.get(key) == "1" for key in
                    ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS")),
                "all four packet workers and parent use one native thread")
        _WORK = {"engine":self.e,"context":context,"provider":provider,
                 "balances":balances,"flow":flow,"directory":self.directory}
        mp = multiprocessing.get_context("fork")
        self.incoming,self.outgoing = mp.Queue(maxsize=8),mp.Queue(maxsize=8)
        for unused in range(4):
            process = mp.Process(target=_packet_worker,args=(self.incoming,self.outgoing))
            process.start(); self.processes.append(process)
        self.pool_started = True
        self._fill()

    def _fill(self):
        while self.next_panel < 1424 and len(self.pending) < 8:
            self.incoming.put(self.next_panel)
            self.pending.add(self.next_panel); self.next_panel += 1
        self.maximum_submitted = max(self.maximum_submitted,len(self.pending))
        require(self.maximum_submitted <= 8, "whole submitted/computing/queued bound")

    def _receive_until(self, panel):
        require(self.pool_started and not self.pool_closed, "new whole packet pool is live")
        while panel not in self.records:
            self.budget()
            try:
                record = self.outgoing.get(timeout=1)
            except queue.Empty:
                require(all(process.is_alive() for process in self.processes),
                        "a complete packet worker stopped without a whole outcome")
                continue
            require(len(canonical(record)) <= 65536 and record["panel"] in self.pending,
                    "small receipt for one outstanding whole cell")
            if "failure" in record:
                raise ValueError("new whole cell "+str(record["panel"])+": "+record["failure"])
            self.pending.remove(record["panel"])
            self._accept(record)
            self._fill()

    def __call__(self, panel, phase):
        require(phase in ("left","right","maps"), "whole defined packet consumer phase")
        if panel not in self.records:
            self._receive_until(panel)
        record = self.records[panel]
        raw = (self.directory/record["name"]).read_bytes()
        require(len(raw) == record["bytes"] and sha(raw) == record["sha256"],
                "whole packet identity on every later consumer phase")
        header,offset = read_packet_header(raw)
        needed = {"forward"} if phase == "left" else ({"backward"} if phase == "right" else set(MATRIX_NAMES[2:]))
        decoded = {}
        width = header["matrix_payload_bytes"]
        for j,name in enumerate(MATRIX_NAMES):
            if name in needed:
                decoded[name] = unpacked_ball(self.e,self.math,N,N,raw[offset+j*width:offset+(j+1)*width])
        return {"panel":panel,"subboxes":header["subboxes"],"all193_coordinates_retained":True,
            "actual_S_changed":False,"forward":decoded.get("forward"),"backward":decoded.get("backward"),
            **{key:decimal_ball(self.e.api,value) for key,value in header["statistics"].items()},
            "true_moments":{"output":decoded.get("output"),
                "inputs":{role:decoded.get(role) for role in ROLES}}}

    def freeze_vectors(self, node, vectors):
        require(type(node) is int and 1 <= node <= 1424 and node not in self.frame_records
                and len(vectors) == P and all(len(v) == N for v in vectors),
                "one complete ordered proposed rational orthogonal frame")
        values = array("d",(x for row in vectors for x in row))
        if sys.byteorder != "little": values.byteswap()
        raw = FRAME_MAGIC+struct.pack("<Q",node)+values.tobytes()
        path = self.directory/("frame-"+str(node)+".vectors")
        atomic(path,raw)
        restored = array("d"); restored.frombytes(path.read_bytes()[len(FRAME_MAGIC)+8:])
        if sys.byteorder != "little": restored.byteswap()
        self.frame_records[node] = {"node":node,"name":path.name,"bytes":len(raw),"sha256":sha(raw)}
        return [[restored[i*N+j] for j in range(N)] for i in range(P)]

    def close(self):
        if self.pool_started and not self.pool_closed:
            # On failure a partial current cell is not a result. Complete
            # atomic packet/done pairs below are still fully recovered.
            for process in self.processes:
                if process.is_alive(): process.terminate()
            for process in self.processes: process.join(timeout=5)
            self.pool_closed = True
            self.incoming.close(); self.outgoing.close()
        for done in sorted(self.directory.glob("*.done"),key=lambda p:int(p.stem)):
            record = json.loads(done.read_bytes())
            if record["panel"] not in self.records:
                self._accept(record)

    def receipt(self):
        chain = hashlib.sha256(b"complete_R149_whole_cell_carrier_index_v1")
        for index in sorted(self.records): chain.update(canonical(self.records[index]))
        frames = hashlib.sha256(b"complete_R149_exact_rational_frame_vectors_index_v1")
        for index in sorted(self.frame_records): frames.update(canonical(self.frame_records[index]))
        return {"whole_cell_indices":sorted(self.records),"whole_cell_count":len(self.records),
            "whole_cell_carrier_index_sha256":chain.hexdigest(),
            "whole_cell_file_bytes":sum(record["bytes"] for record in self.records.values()),
            "whole_frame_count":len(self.frame_records),"whole_frame_index_sha256":frames.hexdigest(),
            "whole_frame_file_bytes":sum(record["bytes"] for record in self.frame_records.values()),
            "old_scientific_targets_reissued":0,"maximum_submitted_unreceived_cells":self.maximum_submitted,
            "four_roles_and_five_moments_present_in_every_whole_packet":True,
            "complete_private_payload_durable_after_runner_exit":False,
            "all_private_objects_have_complete_fixed_source_restoration_recipe":True,
            "restoration_is_not_authorized_without_matching_all_whole_hashes":True,
            "arrays_published_to_git_Release_or_artifact":False}


def positive_tail_cuts(e, context, provider, flow, panel, balance):
    """Split only an unintegrated local box whose directed order16 tail gap fails."""
    diagonal = [e.api.one]*96+[balance]*97
    domain = context.domain
    pending = [(48,64),(32,48),(16,32),(0,16)]
    ends = [0]
    while pending:
        a,b = pending.pop()
        lo,hi = domain.fone*a/64,domain.fone*b/64
        coefficient = provider.centre_matrix(flow.HEAD,flow.HEAD,(panel,lo,hi))
        balanced = flow.diagonal_similarity(e.km,coefficient,diagonal)
        h = domain.full_length(panel)*domain.exact(hi-lo)
        beta = flow.infinity_upper(e.api,e.km.scale(e.api,h,balanced))
        gap = (e.api.one-beta/18).lower()
        if e.api.lower(gap) > 0:
            require(ends[-1] == a, "each accepted positive-tail leaf in original order")
            ends.append(b)
        elif b-a > 1:
            mid = (a+b)//2
            pending.extend(((mid,b),(a,mid)))
        else:
            raise ValueError("uncertified order16 tail on panel %d, normalized [%d/64,%d/64], beta=%s"
                             % (panel,a,b,beta.str(44)))
    return ends


def _packet_worker(incoming,outgoing):
    require(_WORK is not None, "whole fixed inherited worker context")
    work = _WORK
    e,context = work["engine"],work["context"]
    while True:
        panel = incoming.get()
        if panel is None: return
        try:
            require(type(panel) is int and 81 <= panel < 1424, "only genuinely new whole cells")
            cell = context.domain.cells[panel]
            balance = work["balances"][cell["parent_panel"]]
            cut_numbers = positive_tail_cuts(e,context,work["provider"],work["flow"],panel,balance)
            cuts = [context.domain.fone*j/64 for j in cut_numbers]
            packet = work["flow"].true_cell_packet(e.api,e.km,context,work["provider"],panel,cuts,
                balance,order=16,source_provider=None,source_roles=ROLES)
            packet["cut_numerators_over_64"] = cut_numbers
            raw,unused_header = encode_packet(e,packet,"new_post81_order16_whole_cell",16)
            path = work["directory"]/(str(panel)+".packet")
            atomic(path,raw)
            record = {"panel":panel,"name":path.name,"bytes":len(raw),"sha256":sha(raw)}
            atomic(work["directory"]/(str(panel)+".done"),canonical(record))
            outgoing.put(record)
        except BaseException as error:
            traceback.print_exc()
            outgoing.put({"panel":panel,"failure":type(error).__name__+": "+str(error)})
            return


def aggregate_rss_bytes(processes):
    """Sum current RSS, deliberately counting shared COW pages in every process."""
    pids = [os.getpid()]+[process.pid for process in processes if process.pid and process.is_alive()]
    pages = 0
    for pid in pids:
        try:
            values = Path("/proc/"+str(pid)+"/statm").read_text().split()
            pages += int(values[1])
        except FileNotFoundError:
            require(pid != os.getpid(), "the parent resident measurement exists")
    return pages*int(os.sysconf("SC_PAGE_SIZE"))
