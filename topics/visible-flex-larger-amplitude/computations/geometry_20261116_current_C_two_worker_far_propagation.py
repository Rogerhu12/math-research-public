#!/usr/bin/env python3
"""R556: two actual independent mode propagations under one original budget.

This is an Actions-only caller for the unchanged complete point_column.
Two bounded mode spools are merged in the original frequency order. All
mathematical fields and internal Arb balls survive; only declared ledger
addresses and their prepared-record hashes are relocated. Every public
source/input/precision is bound by the actual caller. No prior run is reused.
Author: OpenAI / ChatGPT exact_refinement (AI), 2026-11-16.
"""
from __future__ import annotations
import copy
import fcntl
import gzip
import hashlib
import io
import json
import multiprocessing
import os
from pathlib import Path
import re
import shutil
import signal
import struct
import sys
import time
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R556-complete112-two-worker-mode-propagation-v1"
ORIGINAL_SAMPLER_SHA = "21032e3c4fef44b022a7d91394ff0269dcfd3f94f8ee1a9cab9a0696b2530eb6"
STREAMS = ("coefficient-boxes", "far-accepted-panels", "far-complete-tubes",
    "far-panel-commits", "far-inverse-leaf-coverage", "complete-unpaid-scope")
SPAN_STREAM = {
    "complete_step_rows":"far-accepted-panels",
    "uncommitted_written_step_span":"far-accepted-panels",
    "complete_far_tube_rows":"far-complete-tubes",
    "committed_far_tube_rows":"far-complete-tubes",
    "uncommitted_written_far_span":"far-complete-tubes",
    "prepared_far_rows":"far-complete-tubes",
    "far_contribution_span":"far-complete-tubes",
    "complete_panel_commit_rows":"far-panel-commits",
    "complete_far_leaf_coverage_rows":"far-inverse-leaf-coverage",
    "complete_original_leaf_coverage_rows":"far-inverse-leaf-coverage"}
ADDRESS_STREAM = {"coefficient_row":"coefficient-boxes",
    "prepared_panel_row":"far-accepted-panels", "panel_commit_row":"far-panel-commits"}
COEFFICIENT_TOKEN = re.compile(rb'("coefficient_row":)(0|[1-9][0-9]*)(?=[,}])')
_TRANSFER_CLASS = None


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(",",":"),
        allow_nan=False)+"\n").encode("utf-8")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def receipt(path,check=None):
    path=Path(path);digest=hashlib.sha256();size=0
    with path.open("rb") as stream:
        for block in iter(lambda:stream.read(1048576),b""):
            if check is not None:
                check()
            digest.update(block);size+=len(block)
    return dict(file=str(path),bytes=size,sha256=digest.hexdigest())


def write_new(path,value):
    raw=canonical(value);path=Path(path)
    with path.open("xb") as stream:
        stream.write(raw);stream.flush();os.fsync(stream.fileno())
    return dict(file=str(path),bytes=len(raw),sha256=sha(raw))


def process_identity(pid):
    raw=Path("/proc/"+str(pid)+"/stat").read_text()
    end=raw.rfind(")")
    require(end>0,"The actual process stat is malformed")
    tail=raw[end+2:].split()
    return dict(pid=int(pid),ppid=int(tail[1]),pgid=int(tail[2]),sid=int(tail[3]),
        startticks=int(tail[19]))


def same_process(original):
    try:
        actual=process_identity(original["pid"])
    except FileNotFoundError:
        return False
    return all(actual[key]==original[key] for key in ("pid","pgid","sid","startticks"))


class SharedBudget:
    """One lock-protected admission counter and one original absolute clock.

    flock file descriptions are opened separately in each process. Kernel
    close-on-exit releases the lock; a killed process cannot retain a shared
    Python semaphore. No process has a private renewed science allowance.
    """
    def __init__(self,S,original,root,context):
        self.S=S;self.root=Path(root);self.started=original.started
        self.seconds=original.seconds;self.limit=original.limit
        self.reserve=original.reserve;self.label=original.label;self.out=original.out
        # work, checks, checks since disk, disk observations, stop, signal,
        # peer cancellation, total bytes, used bytes, free bytes.
        self.ints=context.RawArray("q",10)
        self.times=context.RawArray("d",2)
        self.times[0]=-1.0;self.times[1]=0.0
        self.lock_path=self.root/"shared-admission.lock"
        with self.lock_path.open("xb") as stream:
            stream.flush();os.fsync(stream.fileno())
        self.fd=None;self.fd_pid=None

    def _open(self):
        if self.fd_pid!=os.getpid():
            if self.fd is not None:
                os.close(self.fd)
            self.fd=os.open(self.lock_path,os.O_RDWR)
            self.fd_pid=os.getpid()

    def _lock(self):
        self._open()
        while True:
            try:
                fcntl.flock(self.fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
                return
            except BlockingIOError:
                if time.monotonic()-self.started>=self.seconds+5:
                    raise self.S.F.WorkStop("original-phase-clock-ended-while-awaiting-shared-admission")
                time.sleep(.005)

    def _unlock(self):
        fcntl.flock(self.fd,fcntl.LOCK_UN)

    def _stop_locked(self,kind,now,**facts):
        if not self.ints[4]:
            self.ints[4]=1
            value=dict(kind=kind,phase=self.label,
                actual_elapsed_seconds=now-self.started,
                actual_work_units=int(self.ints[0]),original_absolute_clock=True,**facts)
            write_new(self.root/"first-resource-stop.json",value)
        return kind

    def _tick(self,admit,ignore_peer):
        self._lock()
        failure=None
        try:
            now=time.monotonic()
            self.ints[1]+=1;self.ints[2]+=1
            if self.ints[4]:
                failure="shared-original-phase-resource-stop"
            elif self.ints[5]:
                failure=self._stop_locked("actual-mode-phase-external-interruption",now,
                    signal_number=int(self.ints[5]))
            elif now-self.started>=self.seconds:
                failure=self._stop_locked("declared-phase-wall-budget-reached",now,
                    declared_seconds=self.seconds)
            elif self.ints[6] and not ignore_peer:
                failure="already-started-peer-mode-stopped-with-unpaid-propagation"
            else:
                if self.times[0]<0 or now-self.times[0]>=1 or self.ints[2]>=256:
                    try:
                        disk=shutil.disk_usage(self.out)
                        self.ints[7]=disk.total;self.ints[8]=disk.used;self.ints[9]=disk.free
                        self.ints[3]+=1;self.ints[2]=0
                        self.times[0]=now;self.times[1]=now-self.started
                        if disk.free<self.reserve:
                            failure=self._stop_locked("declared-owned-output-free-reserve-reached",now,
                                actual_storage=dict(total=disk.total,used=disk.used,free=disk.free,
                                    required_free_reserve=self.reserve,
                                    phase_elapsed_seconds=now-self.started))
                    except OSError as error:
                        failure=self._stop_locked("actual-owned-output-capacity-observation-failed",now,
                            original_error=dict(type=type(error).__name__,message=str(error)))
                if failure is None and admit:
                    if self.ints[0]>=self.limit:
                        failure=self._stop_locked("declared-phase-work-unit-limit-reached",now,
                            declared_work_units=self.limit)
                    else:
                        self.ints[0]+=1
        finally:
            self._unlock()
        if failure is not None:
            raise self.S.F.WorkStop(failure)

    def check(self):
        self._tick(False,False)

    def attempt(self):
        self._tick(True,False)

    def transfer_check(self):
        # A peer's mathematical partial scope does not prohibit returning
        # already formed data. The original time/storage limits still apply.
        self._tick(False,True)

    def cancel_peer(self,mode,error):
        self._lock()
        try:
            if not self.ints[6]:
                self.ints[6]=1
                write_new(self.root/"first-peer-mode-stop.json",dict(
                    physical_frequency=mode,original_error=error,
                    elapsed_seconds=time.monotonic()-self.started,
                    cancellation_is_not_an_independent_refutation=True))
        finally:
            self._unlock()

    def sync_original(self,original):
        self._lock()
        try:
            original.attempts=int(self.ints[0]);original.checks=int(self.ints[1])
            original.checks_since_storage=int(self.ints[2])
            original.storage_observations=int(self.ints[3])
            original.last_storage_time=None if self.times[0]<0 else float(self.times[0])
            original.last_storage=(None if self.times[0]<0 else dict(
                total=int(self.ints[7]),used=int(self.ints[8]),free=int(self.ints[9]),
                required_free_reserve=self.reserve,phase_elapsed_seconds=float(self.times[1])))
            stop_path=self.root/"first-resource-stop.json"
            if stop_path.is_file():
                original.stop=json.loads(stop_path.read_bytes())
            elif self.ints[4]:
                original.stop=dict(kind="shared-resource-stop-record-not-returned",
                    actual_work_units=original.attempts,
                    resource_record_missing_is_not_completion=True)
        finally:
            self._unlock()


def output_journal(storage,path,root,canonicalizer):
    """Original storage descriptor and add/finish, plus complete raw transfer."""
    global _TRANSFER_CLASS
    if _TRANSFER_CLASS is None:
        class TransferJournal(storage.GzipJSONLJournal):
            def add_transferred(self,raw):
                require(self._finished is None and not self.stream.closed and self._failure is None,
                    "A failed or finished complete stream cannot receive a transferred row")
                require(isinstance(raw,bytes) and raw.endswith(b"\n") and raw.count(b"\n")==1,
                    "Transfer one complete canonical JSONL row")
                encoded=gzip.compress(raw,compresslevel=self.compression_level,mtime=0)
                offset=0
                try:
                    while offset<len(encoded):
                        number=os.write(self.stream.fileno(),memoryview(encoded)[offset:])
                        if number<=0:
                            raise OSError("Transferred complete gzip member made no progress")
                        self.stored_hash.update(memoryview(encoded)[offset:offset+number])
                        self.stored_bytes+=number;offset+=number
                    self.stream.flush()
                except BaseException as error:
                    self._failure=dict(type=type(error).__name__,message=str(error),
                        original_row_index=self.rows,original_row_bytes=len(raw),
                        original_row_sha256=sha(raw),encoded_member_bytes=len(encoded),
                        encoded_member_sha256=sha(encoded),stored_member_prefix_bytes=offset,
                        all_preceding_members_and_original_rows_retained=True,
                        complete_current_member_not_claimed=True)
                    raise
                self.hash.update(raw);self.bytes+=len(raw);self.rows+=1
                return encoded

            def finish(self):
                result=super().finish()
                result["storage"]["actual_logical_row_scope"]="current global canonical rows after declared mode-address relocation"
                result["storage"]["worker_private_canonical_bytes_and_local_indices_not_asserted_unchanged"]=True
                return result
        _TRANSFER_CLASS=TransferJournal
    return _TRANSFER_CLASS(path,root,canonicalizer=canonicalizer,compression_level=1)


def pack_ball(value):
    require(value.is_finite(),"Transport the actual finite interval object")
    mid=value.mid().man_exp();rad=value.rad().man_exp()
    return dict(mid=[str(mid[0]),int(mid[1])],rad=[str(rad[0]),int(rad[1])])


def unpack_ball(B,value):
    # python-flint0.9.0 arb tuple constructor sets the arf midpoint and
    # original mag radius, without a decimal or lower/upper reboxing step.
    return B.arb((int(value["mid"][0]),int(value["mid"][1])),
        (int(value["rad"][0]),int(value["rad"][1])))


def context_values(B):
    result={"prec":int(B.ctx.prec)}
    for key in ("threads","cap","pretty","unicode"):
        if hasattr(B.ctx,key):
            value=getattr(B.ctx,key)
            if type(value) in (int,bool,str):
                result[key]=value
    return result


def install_context(B,record):
    for key,value in record.items():
        setattr(B.ctx,key,value)
    require(int(B.ctx.prec)==record["prec"],"The worker must use the actual bound precision")


def mode_worker(S,task,shared,data,required,by_panel,head,args,r_far,mu,
        original_journals,context_record,cache_limit,gate,output,unused_connections):
    root=Path(task["directory"]);streams={}
    mode=task["physical_frequency"]
    result=dict(schema=SCHEMA+"-mode-return-v1",mode_index=task["mode_index"],
        physical_frequency=mode,source=receipt(__file__),
        actual_context=copy.deepcopy(context_record),actual_cache_records=cache_limit,
        input_binding_sha256=task["input_binding_sha256"],
        original_mode=None,exact_internal_unit_row_transport=None,
        ledgers={},error=None,completed=False,scientific_entry_reached=False,
        finalization_errors=[],actual_process=None)
    code=2
    try:
        for connection in unused_connections:
            connection.close()
        for journal in original_journals.values():
            if not journal.stream.closed:
                journal.stream.close()
        def interrupted(number,_frame):
            shared.ints[5]=number
        signal.signal(signal.SIGTERM,interrupted);signal.signal(signal.SIGINT,interrupted)
        own=process_identity(os.getpid());result["actual_process"]=own
        require(own["pgid"]==task["parent"]["pgid"] and own["sid"]==task["parent"]["sid"]
            and own["ppid"]==task["parent"]["pid"],"Keep the actual owned sampler process group")
        write_new(root/"child-identity.json",dict(schema=SCHEMA+"-child-identity-v1",
            actual=own,parent=task["parent"],source=result["source"]))
        # An unregistered child never enters science. Polling keeps a failed
        # parent registration subject to the same stop flag and original clock.
        while not gate.poll(.05):
            shared.check()
        permission=gate.recv();gate.close()
        require(permission=="registered-by-actual-parent","The parent must record this actual child first")
        shared.check()
        for key in ("GH_TOKEN","GITHUB_TOKEN","MR_TOKEN"):
            os.environ.pop(key,None)
        install_context(S.B,context_record)
        local_args=copy.copy(args);local_args.max_geometry_cache_records=cache_limit
        storage,_=S.r498_storage_helper()
        for name in STREAMS:
            streams[name]=(storage.GzipJSONLJournal(root/(name+".jsonl.gz"),root,
                canonicalizer=S.B.canonical,compression_level=1)
                if name=="far-accepted-panels" else S.B.Journal(root/(name+".jsonl"),root))
        geometry=S.F.GeometryCache(head,data["panels"],local_args,streams["coefficient-boxes"],shared)
        far=data["far_rows"][task["mode_index"]]
        require(far["physical_frequency"]==mode,"The actual mode index/frequency differs")
        write_new(root/"scientific-entry.json",dict(schema=SCHEMA+"-mode-entry-v1",
            mode_index=task["mode_index"],physical_frequency=mode,
            source=result["source"],actual_context=context_record,
            input_binding_sha256=task["input_binding_sha256"],
            caller_reached_original_point_column_boundary=True,
            numerical_completion_not_claimed=True))
        result["scientific_entry_reached"]=True
        row=S.point_column(far,data,required,by_panel,geometry,local_args,shared,
            streams["far-accepted-panels"],streams["far-complete-tubes"],
            streams["far-panel-commits"],streams["far-inverse-leaf-coverage"],
            streams["complete-unpaid-scope"],r_far,mu)
        result["original_mode"]={key:value for key,value in row.items() if key!="full_interval_objects"}
        balls=row.get("full_interval_objects")
        if balls is not None:
            result["exact_internal_unit_row_transport"]=[pack_ball(value) for value in balls["unit_row"]]
        result["geometry_cache_observations"]=dict(range_calls=geometry.range_calls,
            hits=geometry.hits,retained=len(geometry.cache),actual_limit=cache_limit)
        result["completed"]=True
        code=0 if row["complete_required_far_propagation"] else 2
        if not row["complete_required_far_propagation"]:
            shared.cancel_peer(mode,row["error"])
    except BaseException as error:
        result["error"]=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc())
        try:
            shared.cancel_peer(mode,result["error"])
        except BaseException as extra:
            result["finalization_errors"].append(dict(scope="peer-cancellation",
                type=type(extra).__name__,message=str(extra),traceback=traceback.format_exc()))
    finally:
        for name,journal in streams.items():
            try:
                result["ledgers"][name]=journal.finish()
            except BaseException as error:
                result["finalization_errors"].append(dict(scope=name,
                    type=type(error).__name__,message=str(error),traceback=traceback.format_exc()))
        if result["finalization_errors"]:
            code=2
        result["actual_exit"]=code
        try:
            rid=write_new(root/"mode-result.json",result)
            output.send(dict(result=rid,actual_exit=code))
        except BaseException:
            traceback.print_exc()
        finally:
            output.close()
    raise SystemExit(code)


class DigestReader(io.RawIOBase):
    def __init__(self,stream):
        self.stream=stream;self.hash=hashlib.sha256();self.bytes=0
    def readable(self):
        return True
    def read(self,size=-1):
        block=self.stream.read(size);self.hash.update(block);self.bytes+=len(block)
        return block
    def readinto(self,buffer):
        block=self.read(len(buffer));buffer[:len(block)]=block;return len(block)


def original_rows(root,descriptor,shared):
    path=(Path(root)/descriptor["file"]).resolve()
    require(path.parent==Path(root).resolve() and not path.is_symlink(),
        "Read only the actual worker's complete local stream")
    stamp=path.stat()
    count=size=0;digest=hashlib.sha256()
    with path.open("rb") as stream:
        stored=DigestReader(stream)
        decoded=(gzip.GzipFile(fileobj=stored,mode="rb")
            if descriptor.get("storage") is not None else stored)
        try:
            # io.BufferedReader supplies bounded readline for raw JSONL.
            reader=io.BufferedReader(decoded)
            for raw in reader:
                shared.transfer_check()
                require(raw.endswith(b"\n"),"A local source stream ended inside an original row")
                count+=1;size+=len(raw);digest.update(raw)
                yield raw
            reader.close()
        finally:
            if descriptor.get("storage") is not None:
                decoded.close()
        require(stored.bytes==descriptor["bytes"] and stored.hash.hexdigest()==descriptor["sha256"],
            "The complete stored local stream differs from its actual identity")
    expected=descriptor.get("decoded",descriptor)
    require((size,count,digest.hexdigest())==(expected["bytes"],expected["rows"],expected["sha256"]),
        "The complete decoded local stream differs from its actual identity")
    after=path.stat()
    require((stamp.st_dev,stamp.st_ino,stamp.st_size,stamp.st_mtime_ns)==
        (after.st_dev,after.st_ino,after.st_size,after.st_mtime_ns),
        "The worker stream changed during the original-order transfer")


def relocate(value,offsets):
    if isinstance(value,list):
        return [relocate(item,offsets) for item in value]
    if not isinstance(value,dict):
        return copy.deepcopy(value)
    result={}
    for key,item in value.items():
        if key in ADDRESS_STREAM:
            require(type(item) is int and item>=0,"An original ledger address is not a nonnegative integer")
            result[key]=item+offsets[ADDRESS_STREAM[key]]
        elif key in SPAN_STREAM:
            require(isinstance(item,dict) and type(item.get("first")) is int
                and type(item.get("stop")) is int and 0<=item["first"]<=item["stop"],
                "An original complete ledger span differs")
            result[key]=dict(item,first=item["first"]+offsets[SPAN_STREAM[key]],
                stop=item["stop"]+offsets[SPAN_STREAM[key]])
        else:
            result[key]=relocate(item,offsets)
    return result


def merge_mode(S,task,result,shared,journals,rows,entry,root):
    """Relocate one complete returned mode, preserving its original partial flag."""
    mode_dir=Path(task["directory"])
    require(result.get("schema")==SCHEMA+"-mode-return-v1"
        and result.get("mode_index")==task["mode_index"]
        and result.get("physical_frequency")==task["physical_frequency"]
        and result.get("input_binding_sha256")==task["input_binding_sha256"]
        and result.get("source",{}).get("sha256")==receipt(__file__)["sha256"],
        "Use the same actual worker source/input/mode return")
    require(result.get("original_mode") is not None and set(result.get("ledgers",{}))==set(STREAMS)
        and not result.get("finalization_errors"),
        "An unreturned original mode or stream cannot be promoted to the global prefix")
    original=result["original_mode"]
    require(original["physical_frequency"]==task["physical_frequency"]
        and original["mode_index"]==len(rows),
        "Merge the complete original mode sequence without closing an unreturned gap")
    offsets={name:journals[name].rows for name in STREAMS}
    entry["relocation_offsets"]=dict(offsets)
    entry["global_transfer_started"]=True
    entry["global_stream_spans"]={}
    hashes_path=mode_dir/"prepared-record-relocation-sha256.bin"
    hash_writer=hashes_path.open("xb")
    try:
        for name in STREAMS:
            shared.transfer_check()
            desc=result["ledgers"][name]
            if name=="far-accepted-panels":
                storage=desc.get("storage",{})
                require(storage.get("complete_encoded_stream") is True
                    and storage.get("complete_member_count")==desc["rows"]
                    and storage.get("incomplete_member") is None,
                    "An incomplete private gzip member cannot become a complete original stream")
            journal=journals[name];first=journal.rows
            logical=hashlib.sha256();stored=hashlib.sha256()
            logical_bytes=stored_bytes=count=0
            span=dict(first=first,stop=first,complete=False,
                original_private_descriptor=copy.deepcopy(desc))
            entry["global_stream_spans"][name]=span
            index_reader=hashes_path.open("rb") if name=="far-panel-commits" else None
            try:
                for original_raw in original_rows(mode_dir,desc,shared):
                    if name=="far-accepted-panels":
                        matches=list(COEFFICIENT_TOKEN.finditer(original_raw))
                        require(len(matches)==1,
                            "The frozen prepared-panel row has exactly one declared coefficient address")
                        match=matches[0]
                        value=int(match.group(2))+offsets["coefficient-boxes"]
                        raw=(original_raw[:match.start(2)]+str(value).encode("ascii")
                            +original_raw[match.end(2):])
                        encoded=journal.add_transferred(raw)
                        hash_writer.write(hashlib.sha256(original_raw).digest()+hashlib.sha256(raw).digest())
                    else:
                        item=json.loads(original_raw)
                        moved=relocate(item,offsets)
                        if name=="far-panel-commits":
                            prepared=item["prepared_panel_row"]
                            require(type(prepared) is int and prepared>=0,"An original prepared-panel address differs")
                            index_reader.seek(64*prepared)
                            pair=index_reader.read(64)
                            require(len(pair)==64 and pair[:32].hex()==item["prepared_panel_canonical_sha256"],
                                "The original commit must bind its actual complete local prepared row")
                            moved["prepared_panel_canonical_sha256"]=pair[32:].hex()
                        raw=S.B.canonical(moved)
                        journal.add(moved);encoded=raw
                    logical.update(raw);stored.update(encoded)
                    logical_bytes+=len(raw);stored_bytes+=len(encoded);count+=1
                    span.update(stop=journal.rows,complete_rows=count,
                        complete_logical_bytes=logical_bytes,complete_stored_bytes=stored_bytes)
                require(count==desc["rows"] and journal.rows-first==count,
                    "Transfer every original row without duplication or omission")
                span.update(complete=True,logical_sha256=logical.hexdigest(),
                    stored_sha256=stored.hexdigest(),
                    logical_bytes=logical_bytes,stored_bytes=stored_bytes,rows=count)
                if name=="far-accepted-panels":
                    hash_writer.flush();os.fsync(hash_writer.fileno())
            finally:
                if index_reader is not None:
                    index_reader.close()
        hash_writer.flush();os.fsync(hash_writer.fileno())
    finally:
        hash_writer.close()
    row=relocate(original,offsets)
    balls=result.get("exact_internal_unit_row_transport")
    if row["complete"]:
        require(isinstance(balls,list) and len(balls)==2,
            "Keep both actual complete internal unit-row intervals")
        row["full_interval_objects"]={"unit_row":[unpack_ball(S.B,value) for value in balls]}
    else:
        row["full_interval_objects"]=None
    for name in STREAMS:
        shared.transfer_check()
        journals[name].stream.flush();os.fsync(journals[name].stream.fileno())
    hash_transport=receipt(hashes_path,shared.transfer_check)
    shared.transfer_check()
    mode_record={key:value for key,value in row.items() if key!="full_interval_objects"}
    mode_record["actual_independent_mode_transport"]=dict(
        schema=SCHEMA+"-ordered-mode-transport-v1",
        original_mode_result=entry["actual_mode_result"],
        relocation_offsets=offsets,
        exact_internal_Arb_midpoint_radius_transport=True,
        actual_global_commit_file=str(root/("mode-"+str(task["mode_index"])+"-global-commit.json")),
        complete_mode_transport_commit_required=True)
    mode_row=journals["far-all-mode-rows"].rows
    journals["far-all-mode-rows"].add(mode_record)
    journals["far-all-mode-rows"].stream.flush()
    os.fsync(journals["far-all-mode-rows"].stream.fileno())
    commit=write_new(root/("mode-"+str(task["mode_index"])+"-global-commit.json"),dict(
        schema=SCHEMA+"-global-mode-transfer-commit-v1",
        physical_frequency=task["physical_frequency"],mode_index=task["mode_index"],
        original_mode_result=entry["actual_mode_result"],relocation_offsets=offsets,
        global_stream_spans=entry["global_stream_spans"],global_mode_row=mode_row,
        global_mode_row_canonical_sha256=sha(S.B.canonical(mode_record)),
        prepared_record_hash_transport=hash_transport,
        complete_original_mode_spatial_scope=bool(row["complete_required_far_propagation"]),
        complete_original_unit_row_family=bool(row["complete"]),
        every_original_stream_transferred_and_fsynced_before_this_commit=True))
    rows.append(row)
    entry.update(global_transfer_complete=True,actual_global_commit=commit,
        global_mode_row=mode_row,complete_required_far_propagation=row["complete_required_far_propagation"],
        complete_unit_row_family=row["complete"])
    # Only redundant local payloads retire. Actual mode result, original
    # stored/decoded identities, worker ownership and relocation receipts stay.
    retired=[];retirement_errors=[]
    for name in STREAMS:
        path=mode_dir/result["ledgers"][name]["file"]
        try:
            path.unlink();retired.append(name)
        except OSError as error:
            retirement_errors.append(dict(stream=name,type=type(error).__name__,message=str(error)))
    try:
        hashes_path.unlink()
    except OSError as error:
        retirement_errors.append(dict(stream="prepared-record-relocation-index",
            type=type(error).__name__,message=str(error)))
    entry.update(retired_redundant_local_streams=retired,
        spool_retirement_errors=retirement_errors,
        retained_original_mode_result_and_ownership=True,
        global_payload_not_retired=True)
    return row


def returned_mode(task,message,source_sha):
    path=Path(task["directory"])/"mode-result.json"
    if not path.is_file():
        return None,None
    raw=path.read_bytes();rid=dict(file=str(path),bytes=len(raw),sha256=sha(raw))
    if message is not None:
        declared=message["result"]
        require(all(declared[key]==rid[key] for key in ("file","bytes","sha256")),
            "Use the actual child result bound by its return message")
    result=json.loads(raw)
    require(result.get("source",{}).get("sha256")==source_sha,
        "The actual mode return has another helper source")
    return result,rid


def preserve_unmerged(S,journals,task,entry,result,error,required):
    row=None if result is None else result.get("original_mode")
    scope=(dict(current_original_source_panel_row=required[0]["panel"]["row"] if required else None,
        complete_required_original_panel_suffix=dict(first=0,stop=len(required)),
        required_panel_index_file="required-source-panels.json",
        actual_scientific_return_absent=True) if row is None else dict(
        complete_pending_scope=row.get("complete_pending_scope"),
        last_paid=row.get("last_paid"),complete_current_factorized_state=row.get("complete_current_factorized_state"),
        last_unaccepted_candidate=row.get("last_unaccepted_candidate"),
        uncommitted_transaction=row.get("uncommitted_transaction"),
        uncommitted_written_step_span=row.get("uncommitted_written_step_span"),
        uncommitted_written_far_span=row.get("uncommitted_written_far_span"),
        complete_required_far_propagation=row.get("complete_required_far_propagation"),
        complete_unit_row_family_enclosed=row.get("complete_unit_row_family_enclosed"),
        error=row.get("error"),
        private_indices_are_not_global_committed_indices=True))
    journals["complete-unpaid-scope"].add(dict(kind="actual-parallel-mode-not-globally-committed",
        physical_frequency=task["physical_frequency"],mode_index=task["mode_index"],
        actual_mode_result=entry.get("actual_mode_result"),
        actual_private_directory=task["directory"],original_mode_scope=scope,
        actual_worker_error=None if result is None else result.get("error"),
        actual_finalization_errors=[] if result is None else result.get("finalization_errors"),
        actual_transfer_error=error,actual_partial_global_spans=entry.get("global_stream_spans",{}),
        local_complete_family_not_promoted_to_global_112_input=True,
        original_private_payload_retained=True))
    entry["unpaid_scope_recorded"]=True


def run_modes(S,*,data,required,by_panel,head,geometry,args,budget,journals,
        rows,record,r_far,mu):
    """Called exactly once by the actual sampler in place of its serial loop."""
    require(os.environ.get("GITHUB_ACTIONS")=="true"
        and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,
        "Parallel full-family propagation is public-Actions-only")
    require(os.name=="posix" and "fork" in multiprocessing.get_all_start_methods(),
        "Use the declared original Linux Actions process environment")
    require(S.M==112 and tuple(S.F.MODES)==tuple(range(2,225,2))
        and [row["physical_frequency"] for row in data["far_rows"]]==list(S.F.MODES),
        "Preserve all original112 ordered deep modes")
    require(not rows,"The actual finite-far mode prefix starts empty")
    root=args.out/"parallel-mode-spools";root.mkdir()
    source=receipt(__file__);parent=process_identity(os.getpid())
    ctx=context_values(S.B)
    require(ctx["prec"]==args.precision_bits,"Keep the actual bound scalar Arb precision")
    work=multiprocessing.get_context("fork")
    shared=SharedBudget(S,budget,root,work)
    leaf_journal=journals["sample-inverse-leaves"]
    leaf_journal.stream.flush();os.fsync(leaf_journal.stream.fileno())
    initial_leaf_prefix=dict(file=str(leaf_journal.path),rows=leaf_journal.rows,
        complete_prefix_bytes=leaf_journal.bytes,
        complete_prefix_sha256=leaf_journal.hash.hexdigest(),
        scope="actual original physical-far sampling ledger prefix before any mode worker",
        full_later_sample_ledger_identity_not_claimed=True)
    required_index=receipt(args.out/"required-source-panels.json",shared.transfer_check)
    binding=dict(original_input_binding=data["binding"],
        actual_required_source_panel_index=required_index,
        actual_initial_far_sampling_leaf_prefix=initial_leaf_prefix,
        original_scope_conditions=data["facts"],
        physical_far_word=S.word(r_far),mu_word=S.word(mu),
        all_required_frequencies=list(S.F.MODES),actual_context=ctx,
        precision_bits=args.precision_bits,max_depth=args.max_depth,
        local_defect_bits=args.local_defect_bits,panel_norm_limit=str(args.panel_norm_limit),
        taylor_terms=args.taylor_terms,max_geometry_cache_records=args.max_geometry_cache_records,
        original_phase_started_monotonic=budget.started,
        original_phase_seconds=budget.seconds,original_work_units=budget.limit,
        original_free_bytes_reserve=budget.reserve)
    binding_id=write_new(root/"input-binding.json",binding)
    record.update(schema=SCHEMA,source=source,parent_process=parent,
        actual_input_binding=binding_id,actual_context=ctx,worker_count=2,
        max_simultaneous_mode_spools=2,original_mode_order=list(S.F.MODES),
        actual_started_modes=[],actual_worker_scientific_entry_modes=[],
        actual_globally_committed_modes=[],mode_tasks=[],owned_child_events=[],
        original_phase_clock_restarted=False,private_work_allowances_created=False,
        every_attempt_uses_one_shared_admission_counter=True,
        new_principal_angle_or_root_choice=False,original_sample_and_momentum_stages_unchanged=True,
        all_internal_interval_transport_uses_exact_midpoint_radius_pairs=True,
        worker_entry_list_scope="confirmed by complete returned mode metadata; absent confirmation does not assert unstarted",
        process_quiet=False,all_required_modes_returned=False,error=None)
    # Parent's prior sampling coefficient rows remain in their original
    # ledger. Dropping only this memo avoids retaining three full LRUs.
    record["parent_geometry_cache_records_released"]=len(geometry.cache)
    geometry.cache.clear()
    previous={}
    def interrupted(number,_frame):
        shared.ints[5]=number
    for number in (signal.SIGTERM,signal.SIGINT):
        previous[number]=signal.signal(number,interrupted)
    live=[];stop_launch=False
    try:
        for first in range(0,len(S.F.MODES),2):
            shared.transfer_check()
            if shared.ints[6]:
                break
            wave=[]
            for lane,index in enumerate(range(first,min(first+2,len(S.F.MODES)))):
                mode=S.F.MODES[index];directory=root/("mode-"+str(index));directory.mkdir()
                task=dict(mode_index=index,physical_frequency=mode,directory=str(directory),
                    parent=parent,input_binding_sha256=binding_id["sha256"])
                # The sum of the two retained worker LRUs is the original cap.
                # Zero means immediate eviction in the original GeometryCache.
                cache_limit=(args.max_geometry_cache_records+1)//2 if lane==0 \
                    else args.max_geometry_cache_records//2
                receive_gate,send_gate=work.Pipe(duplex=False)
                receive_result,send_result=work.Pipe(duplex=False)
                entry=dict(mode_index=index,physical_frequency=mode,private_directory=str(directory),
                    actual_process=None,actual_mode_result=None,actual_worker_exit=None,
                    actual_worker_started=False,actual_worker_reaped=False,actual_return_message=None,
                    global_transfer_started=False,global_transfer_complete=False,
                    actual_cache_records=cache_limit,ownership_unknown=None)
                record["mode_tasks"].append(entry)
                unused=[send_gate,receive_result]
                for older in live:
                    unused.extend((older["receive"],older["gate"]))
                child=work.Process(target=mode_worker,args=(S,task,shared,data,required,by_panel,
                    head,args,r_far,mu,journals,ctx,cache_limit,receive_gate,send_result,unused),
                    name="R556-mode-"+str(mode),daemon=False)
                obj=dict(task=task,entry=entry,process=child,receive=receive_result,
                    gate=send_gate,message=None,stop_started=None,signals=[])
                wave.append(obj);live.append(obj)
                child.start()
                entry["actual_worker_started"]=True
                record["actual_started_modes"].append(mode)
                receive_gate.close();send_result.close()
                try:
                    identity=process_identity(child.pid)
                    require(identity["ppid"]==parent["pid"] and identity["pgid"]==parent["pgid"]
                        and identity["sid"]==parent["sid"],"Record the actual same-group child before science")
                    entry["actual_process"]=identity
                except BaseException as error:
                    entry["registration_error"]=dict(type=type(error).__name__,message=str(error))
                    raise
                write_new(directory/"parent-registration.json",dict(schema=SCHEMA+"-owned-child-v1",
                    source=source,parent=parent,child=identity,task=task,
                    inherited_original_owned_group=True,no_new_session_or_group=True))
                send_gate.send("registered-by-actual-parent");send_gate.close()
            while any(obj["process"].is_alive() for obj in wave):
                now=time.monotonic()
                if now-budget.started>=budget.seconds or shared.ints[5]:
                    try:
                        shared.transfer_check()
                    except Exception as error:
                        if record.get("first_parent_resource_observation") is None:
                            record["first_parent_resource_observation"]=dict(
                                type=type(error).__name__,message=str(error),
                                elapsed_seconds=now-budget.started)
                stopping=bool(shared.ints[4] or shared.ints[5] or shared.ints[6])
                for obj in wave:
                    process=obj["process"];entry=obj["entry"]
                    if obj["message"] is None and obj["receive"].poll():
                        try:
                            obj["message"]=obj["receive"].recv()
                            entry["actual_return_message"]=obj["message"]
                        except EOFError:
                            entry["actual_control_pipe_eof"]=True
                    if not stopping or not process.is_alive():
                        continue
                    if obj["stop_started"] is None:
                        obj["stop_started"]=now
                    elapsed=now-obj["stop_started"]
                    number=(signal.SIGKILL if elapsed>=10 else signal.SIGTERM if elapsed>=5 else None)
                    if number is not None and number not in obj["signals"]:
                        try:
                            if same_process(entry["actual_process"]):
                                os.kill(process.pid,number)
                                obj["signals"].append(number)
                                event=dict(mode=entry["physical_frequency"],pid=process.pid,
                                    signal=number,elapsed_seconds=now-budget.started,
                                    original_phase_not_renewed=True)
                                record["owned_child_events"].append(event)
                        except OSError as error:
                            entry["ownership_unknown"]=dict(type=type(error).__name__,message=str(error))
                time.sleep(.01)
            for obj in wave:
                process=obj["process"];entry=obj["entry"]
                process.join()
                entry.update(actual_worker_exit=process.exitcode,actual_worker_reaped=True)
                if obj["message"] is None and obj["receive"].poll():
                    try:
                        obj["message"]=obj["receive"].recv()
                        entry["actual_return_message"]=obj["message"]
                    except EOFError:
                        entry["actual_control_pipe_eof"]=True
                obj["receive"].close()
                write_new(Path(obj["task"]["directory"])/"parent-close.json",dict(
                    schema=SCHEMA+"-owned-child-close-v1",child=entry["actual_process"],
                    actual_exit=process.exitcode,reaped=True,
                    actual_signals=obj["signals"],ownership_unknown=entry["ownership_unknown"]))
                live.remove(obj)
            gap=False
            for obj in wave:
                task,entry=obj["task"],obj["entry"];result=None
                try:
                    result,rid=returned_mode(task,obj["message"],source["sha256"])
                    entry["actual_mode_result"]=rid
                    if result is not None and result.get("scientific_entry_reached"):
                        record["actual_worker_scientific_entry_modes"].append(task["physical_frequency"])
                    if gap:
                        raise S.F.WorkStop("an-earlier-original-mode-has-no-global-transfer-commit")
                    shared.transfer_check()
                    require(result is not None,"The actual worker mode return is absent")
                    row=merge_mode(S,task,result,shared,journals,rows,entry,root)
                    record["actual_globally_committed_modes"].append(task["physical_frequency"])
                    if entry.get("spool_retirement_errors"):
                        stop_launch=True
                        record["spool_retirement_stop"]=dict(
                            physical_frequency=task["physical_frequency"],
                            actual_errors=entry["spool_retirement_errors"],
                            globally_committed_mathematical_result_remains_valid=True,
                            no_next_wave_created_with_unretired_private_payload=True)
                    print(json.dumps(dict(event="current_C_nondividing_far_mode",
                        physical_frequency=task["physical_frequency"],complete=row["complete"],
                        error=row["error"],accepted_panels=row["accepted_panels"],
                        elapsed_seconds=time.monotonic()-budget.started,
                        actual_mode_parallelism=SCHEMA)),flush=True)
                except Exception as error:
                    gap=True;stop_launch=True
                    details=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc())
                    entry["transfer_error"]=details
                    preserve_unmerged(S,journals,task,entry,result,details,required)
                if result is None or (result.get("original_mode") or {}).get("complete_required_far_propagation") is not True:
                    stop_launch=True
            shared.transfer_check()
            shared.sync_original(budget)
            if stop_launch or shared.ints[4] or shared.ints[5] or shared.ints[6]:
                break
        record["all_required_modes_returned"]=len(rows)==len(S.F.MODES)
    except BaseException as error:
        record["error"]=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc())
        try:
            shared.cancel_peer(None,record["error"])
        except BaseException as extra:
            record["cancellation_record_error"]=dict(type=type(extra).__name__,message=str(extra))
    finally:
        # Every process here was created and registered by this caller. Never
        # signal a reused/unreadable identity; uncertainty remains explicit.
        for obj in list(live):
            process=obj["process"];entry=obj["entry"]
            try:
                obj["gate"].close()
                if not entry["actual_worker_started"]:
                    entry["actual_worker_not_created"]=True
                    continue
                # join uses this actual multiprocessing child handle. It is
                # safe even if /proc registration failed; no PID is signalled.
                process.join(timeout=5)
                if process.is_alive():
                    identity=entry.get("actual_process")
                    if identity is None:
                        entry["ownership_unknown"]={"kind":"unregistered-created-worker-remains-live"}
                    elif same_process(identity):
                        os.kill(process.pid,signal.SIGTERM)
                        obj["signals"].append(signal.SIGTERM)
                        process.join(timeout=5)
                        if process.is_alive() and same_process(identity):
                            os.kill(process.pid,signal.SIGKILL)
                            obj["signals"].append(signal.SIGKILL)
                        process.join(timeout=5)
                    else:
                        entry["ownership_unknown"]={"kind":"created-worker-current-identity-differs"}
                if process.is_alive():
                    if entry["ownership_unknown"] is None:
                        entry["ownership_unknown"]={"kind":"registered-worker-remains-live"}
                else:
                    entry.update(actual_worker_reaped=True,actual_worker_exit=process.exitcode)
                write_new(Path(obj["task"]["directory"])/"parent-close.json",dict(
                    schema=SCHEMA+"-owned-child-close-v1",child=entry["actual_process"],
                    actual_exit=process.exitcode,reaped=entry["actual_worker_reaped"],
                    actual_signals=obj["signals"],ownership_unknown=entry["ownership_unknown"],
                    registration_error=entry.get("registration_error")))
            except BaseException as error:
                entry["ownership_unknown"]=dict(type=type(error).__name__,message=str(error))
            finally:
                try:
                    obj["receive"].close();obj["gate"].close()
                except OSError:
                    pass
        record["process_quiet"]=all((entry.get("actual_worker_started") is False
            or entry.get("actual_worker_reaped") is True)
            and entry.get("ownership_unknown") is None for entry in record["mode_tasks"])
        for entry in record["mode_tasks"]:
            if entry.get("global_transfer_complete") or entry.get("unpaid_scope_recorded"):
                continue
            task=dict(mode_index=entry["mode_index"],physical_frequency=entry["physical_frequency"],
                directory=entry["private_directory"],input_binding_sha256=binding_id["sha256"])
            result=None
            if entry.get("actual_worker_reaped"):
                try:
                    result,rid=returned_mode(task,entry.get("actual_return_message"),source["sha256"])
                    entry["actual_mode_result"]=rid
                    if (result is not None and result.get("scientific_entry_reached")
                            and task["physical_frequency"] not in record["actual_worker_scientific_entry_modes"]):
                        record["actual_worker_scientific_entry_modes"].append(task["physical_frequency"])
                except BaseException as error:
                    entry["mode_return_read_error"]=dict(type=type(error).__name__,
                        message=str(error),traceback=traceback.format_exc())
            try:
                preserve_unmerged(S,journals,task,entry,result,
                    entry.get("transfer_error") or record.get("error") or
                    dict(kind="original-worker-return-or-quiescence-unpaid"),required)
            except BaseException as error:
                entry["unpaid_scope_write_error"]=dict(type=type(error).__name__,
                    message=str(error),traceback=traceback.format_exc())
        record["all_required_modes_returned"]=len(rows)==len(S.F.MODES)
        record["all_required_mode_families_complete"]=(len(rows)==len(S.F.MODES) and all(row["complete"] for row in rows))
        record["actual_not_started_modes"]=[m for m in S.F.MODES if m not in record["actual_started_modes"]]
        record["actual_started_but_not_globally_committed_modes"]=[
            m for m in record["actual_started_modes"] if m not in record["actual_globally_committed_modes"]]
        record["all_unvisited_required_modes_retained"]=True
        record["actual_elapsed_seconds"]=time.monotonic()-budget.started
        try:
            shared.sync_original(budget)
        except BaseException as error:
            record["budget_record_error"]=dict(type=type(error).__name__,message=str(error))
        for number,handler in previous.items():
            signal.signal(number,handler)
        write_new(root/"result.json",record)
    if not record["process_quiet"]:
        raise S.F.WorkStop("actual-owned-parallel-worker-quiescence-unpaid")
    if record.get("error") is not None or record.get("budget_record_error") is not None:
        raise S.F.WorkStop("actual-parallel-mode-caller-or-shared-budget-unpaid")
