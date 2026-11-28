"""R790 complete R763 public geometry with batched original R761 time endpoints.

The released cap designs use the original R763 provider. The tube design
retains every original material row, the original complement and crown, and
the original rim override. Only the active R761 physical trajectory uses the
augmented chart labels. Its temporary transport tables live on the runner.
"""
import atexit
from collections import OrderedDict
from concurrent.futures import ProcessPoolExecutor, wait, FIRST_COMPLETED
import hashlib
import json
import multiprocessing
import os
from pathlib import Path
import tempfile
import time

import numpy as np

import r763_translated_caps_and_shared_rim as original
import r790_augmented_collar_flow as flow
from r742_tilted_disk_two_jets import J, gather


paired, tube, g, delay = original.paired, original.tube, original.g, original.delay
_WORKING_BYTES = 768 * 1024 * 1024
_shared = None


class Transport:
    def __init__(self):
        self.folder = tempfile.TemporaryDirectory(prefix="r790-collar-", dir=os.environ.get("RUNNER_TEMP"))
        self.root = Path(self.folder.name)
        self.executor = None
        self.files = OrderedDict()
        self.total_bytes = 0
        self.phases = np.array([], dtype=float)
        self.amplitudes = ()
        self.progress = None
        self.label = ""
        self.last_message = 0.
        self.stats = dict(chunks_computed=0, chunks_read=0, exact_angle_rows_read=0,
            active_material_rows_computed=0, auxiliary_rhs_calls=0, original_newton_fallbacks=0,
            original_flow_fallback_angles=0, original_flow_fallback_chunks=0,
            original_flow_fallback_reasons={}, predictor_polishes=0, completed_angle_intervals=0,
            maximum_returned_inverse_residual=0., minimum_returned_abs_determinant=None,
            temporary_cache_evictions=0)
        self.workers = max(1, min(4, len(os.sched_getaffinity(0))))

    def close(self):
        if self.executor is not None:
            self.executor.shutdown(wait=True, cancel_futures=True)
            self.executor = None
        self.files.clear()
        self.folder.cleanup()

    def announce(self, required=False):
        if self.progress is None:
            return
        now = time.monotonic()
        if not required and now-self.last_message < 40:
            return
        self.last_message = now
        workers = []
        for file in sorted(self.root.glob("worker-*.json")):
            try:
                workers.append(json.loads(file.read_text(encoding="utf-8")))
            except FileNotFoundError:
                continue
        self.progress(dict(transport_scope=self.label, transport_totals=self.snapshot(),
                           most_recent_worker_states=workers))

    def snapshot(self):
        return dict(self.stats, allocated_workers=self.workers, cache_bytes=self.total_bytes,
                    cache_entries=len(self.files), physical_method="R790 augmented R761/DOP853",
                    numerical_identity_with_single_phase_integration_assumed=False)

    def set_grid(self, phases, amplitudes, label, progress):
        self.phases=np.unique(np.asarray(phases, dtype=float))
        self.amplitudes=tuple(float(x) for x in amplitudes)
        self.label=str(label)
        self.progress=progress

    def angles(self, theta, amplitude):
        # Equality of the actual binary64 integration angles is required.
        # A new caller outside the configured set still receives its own true endpoint.
        if not len(self.phases):
            return np.array([theta])
        values=np.array([float(a)*np.sin(float(t)) for a in
                         dict.fromkeys((*self.amplitudes, float(amplitude))) for t in self.phases])
        return np.unique(np.r_[values[values>0], theta]).astype(float)

    def adopt(self, key, ids, stats, path):
        size=path.stat().st_size if len(ids) else 0
        self.files[key]=(np.asarray(ids, dtype=np.intp),path,size)
        self.total_bytes+=size
        names={"active_material_rows_computed":"active_points","auxiliary_rhs_calls":"rhs_calls",
               "completed_angle_intervals":"angle_intervals"}
        for target, source in names.items():
            self.stats[target]+=stats[source]
        for name in ("original_newton_fallbacks","predictor_polishes","original_flow_fallback_angles"):
            self.stats[name]+=stats[name]
        self.stats["chunks_computed"]+=1
        if stats["original_flow_fallback_reason"] is not None:
            self.stats["original_flow_fallback_chunks"]+=1
            reasons=self.stats["original_flow_fallback_reasons"]
            tag=stats["original_flow_fallback_reason"]
            reasons[tag]=reasons.get(tag,0)+1
        m=stats["minimum_returned_abs_determinant"]
        if m is not None:
            prev=self.stats["minimum_returned_abs_determinant"]
            self.stats["minimum_returned_abs_determinant"]=m if prev is None else min(prev,m)
        self.stats["maximum_returned_inverse_residual"]=max(
            self.stats["maximum_returned_inverse_residual"],stats["maximum_returned_inverse_residual"])

    def trim(self):
        while self.total_bytes>_WORKING_BYTES and self.files:
            _,(_,path,size)=self.files.popitem(last=False)
            if size:
                path.unlink(missing_ok=True)
            self.total_bytes-=size
            self.stats["temporary_cache_evictions"]+=1

    def prepare(self, blocks, angles, nr, order):
        if self.executor is None:
            self.executor=ProcessPoolExecutor(max_workers=self.workers,
                mp_context=multiprocessing.get_context("spawn"))
        keys=[]; pending={}; submitted=set()
        for words in blocks:
            keyhash=hashlib.sha256()
            keyhash.update(np.asarray([nr,order,*words.shape],dtype="<i8").tobytes())
            keyhash.update(np.asarray(angles,dtype="<f8").tobytes())
            keyhash.update(np.ascontiguousarray(words,dtype="<f8").tobytes())
            key=keyhash.hexdigest(); keys.append(key)
            if key in self.files:
                self.files.move_to_end(key)
                continue
            if key in submitted:
                continue
            path=self.root/(key+".npy")
            fut=self.executor.submit(flow.run_chunk,words,angles,nr,order,str(path),str(self.root))
            pending[fut]=(key,path); submitted.add(key)
        while pending:
            ready,_=wait(pending,timeout=20,return_when=FIRST_COMPLETED)
            for fut in ready:
                key,path=pending.pop(fut)
                ids,stats=fut.result()
                self.adopt(key,ids,stats,path)
            self.announce()
        return keys

    def evaluate(self, words, key, index, theta, nr, order):
        ids,path,_=self.files[key]
        self.files.move_to_end(key);self.stats["chunks_read"]+=1
        x,z=flow.from_words(words)
        direct=tube.planar(x,z,theta,nr,order)
        if not len(ids):
            return direct
        state=np.load(path,mmap_mode="r",allow_pickle=False)
        row=np.array(state[index],copy=True)
        del state
        values=flow.from_words(row);self.stats["exact_angle_rows_read"]+=len(ids)
        return tube.replace(direct[0],ids,values[0]),tube.replace(direct[1],ids,values[1])


def state():
    global _shared
    if _shared is None:
        _shared=Transport()
        atexit.register(_shared.close)
    return _shared


def set_phase_grid(phases,amplitudes,label,progress=None):
    state().set_grid(phases,amplitudes,label,progress)


def counters():
    return state().snapshot()


def chart_jet(chart,u,v,phase=0.,design=None,order=32):
    d={} if design is None else design
    t=float(phase)
    if not t or d.get("cap","translated")!="tube" or not chart.startswith("cap"):
        return original.chart_jet(chart,u,v,t,d,order)
    g.disk._public()
    amp=d.get("angle",.78); nr=d.get("ramp_cells",2)
    if not (0<=t<=np.pi/2+2.e-14 and 0<=amp<=.81 and nr in (2,3)):
        raise ValueError("paired phase/amplitude/ramp outside R761")
    if not amp:
        return original.chart_jet(chart,u,v,t,d,order)
    a,b=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float))
    shape=a.shape;aa=a.ravel();bb=b.ravel()
    result=np.empty((len(aa),6,3))
    direct=np.zeros(len(aa),dtype=bool)
    if "cartesian" not in chart:
        depth=bb if "normal" in chart else 1-bb
        direct=depth<=1.e-8
    if np.any(direct):
        result[direct]=original.chart_jet(chart,aa[direct],bb[direct],t,d,order)
    rest=np.flatnonzero(~direct)
    if not len(rest):
        return result.reshape(shape+(6,3))
    ujet=J(aa[rest],s=1.);vjet=J(bb[rest],a=1.)
    X,_,Z=delay.sphere_chart(chart,ujet,vjet,np.zeros(len(rest)),order,"legacy")
    XZ=tube.packed((X,Z))
    blocks=[np.ascontiguousarray(XZ[:,k:k+32]) for k in range(0,len(rest),32)]
    theta=amp*np.sin(t);manager=state();angles=manager.angles(theta,amp)
    j=int(np.searchsorted(angles,theta))
    if j==len(angles) or angles[j]!=theta:raise ArithmeticError("missing requested physical angle")
    keys=manager.prepare(blocks,angles,nr,order)
    sign=1 if chart.endswith("+") else -1
    for k,(words,key) in enumerate(zip(blocks,keys)):
        P=manager.evaluate(words,key,j,theta,nr,order)
        y=sign*(delay.HALF_WIDTH+delay.end_limits(order)[0]+tube.crown(P,theta,nr,order))
        result[rest[32*k:32*k+words.shape[1]]]=gather((P[0],y,P[1]),words.shape[1])
    manager.trim()
    return result.reshape(shape+(6,3))
