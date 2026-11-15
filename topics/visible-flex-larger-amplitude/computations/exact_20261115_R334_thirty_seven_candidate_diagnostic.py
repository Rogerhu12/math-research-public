#!/usr/bin/env python3
"""Request158: exact R334 readout of one already executed original37 candidate.

This is new scientific arithmetic, restricted to public Actions. It consumes
literal returned arrays and the actual final chosen direction. It makes no
RHS/J/QR/FD/optimization call. The dyadic affine reference is explicitly formed
from recorded words; actual nonlinear query returns and Hermite defects are
separate. Nothing here changes the original model, FD or native acceptance.
"""
from __future__ import annotations
import argparse
from collections import OrderedDict
import gzip
import hashlib
import importlib.util
import json
import math
import os
import signal
from pathlib import Path
import struct
import sys
import time
import traceback

REPOSITORY="Rogerhu12/math-research-public"
SCHEMA="R334-original37-complete-candidate-exact-readout-v1"
CAPTURE_SCHEMA="R334-original37-actual-return-capture-v1"
CAPTURE_NAME="geometry_20261115_R334_thirty_seven_return_capture.py"
CAPTURE_SHA="01a2638409893b60711c3af0ab4d14c6f9bc4272058f2e7577dd41b2db33c59d"
FFT_NAME="geometry_20261114_fft_frenet.py"
FFT_SHA="973898fcea1e8706d0ff9f87bbe72cde3576bc0055149af0a2e2058b144ac401"
UNPACK_SOURCE_SHA="cf163a5c42cff95137a78eefda058b6a18f5f226b4261b686a42e645f4002fcb"
PROOF_SHA="2fd386b8410de271142187cd8911ceb073673665faa0baf96bc8d2b7822b6602"
LEFT=(463,464,465,466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485,486,487)
MID=(471,472,473,475,477,479,480,481,482,483,484,485,486,487,489,490)
ANGLES=2048
GROUPS=37
ROWS=GROUPS*ANGLES
ALPHAS=17
ZERO=(0,0)


def require(ok,message):
    if not ok: raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,ensure_ascii=True,
        separators=(",",":"),allow_nan=False)+"\n").encode("ascii")


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith(".gz") else raw)


def receipt(path):
    p=Path(path)
    return dict(file=p.name,bytes=p.stat().st_size,sha256=file_sha(p))


def word(x):
    return struct.pack("<d",float(x)).hex()


def unword(x):
    require(isinstance(x,str) and len(x)==16,"One literal binary64 word required")
    return struct.unpack("<d",bytes.fromhex(x))[0]


def canonical_d(n,e=0):
    n=int(n);e=int(e)
    if n==0: return ZERO
    low=(abs(n)&-abs(n)).bit_length()-1
    return n>>low,e+low


def dyadic(x):
    x=float(x)
    require(math.isfinite(x),"Exact dyadic arithmetic needs a finite recorded word")
    n,d=x.as_integer_ratio()
    return canonical_d(n,-(d.bit_length()-1))


def add(a,b):
    if not a[0]: return b
    if not b[0]: return a
    e=min(a[1],b[1])
    return canonical_d((a[0]<<(a[1]-e))+(b[0]<<(b[1]-e)),e)


def neg(a): return -a[0],a[1]


def sub(a,b): return add(a,neg(b))


def mul(a,b): return canonical_d(a[0]*b[0],a[1]+b[1])


def scale_pow2(a,k): return (a[0],a[1]+k) if a[0] else ZERO


def total(items):
    result=ZERO
    for item in items: result=add(result,item)
    return result


def compare(a,b):
    d=sub(a,b)[0]
    return (d>0)-(d<0)


def absolute(a): return abs(a[0]),a[1]


def packed(a):
    return dict(integer_hex=("-" if a[0]<0 else "")+format(abs(a[0]),"x"),
        exponent2=a[1],encoding="exact-integer-times-power-of-two")


def integer_hex(n):
    return ("-" if n<0 else "")+format(abs(n),"x")


def note_extreme(obj,key,value,index,minimum=False):
    old=obj.get(key)
    if old is None or (compare(value,old[0])<0 if minimum else compare(absolute(value),absolute(old[0]))>0):
        obj[key]=(value,index)


def output_extremes(obj):
    return {key:dict(value=packed(value),index=index) for key,(value,index) in obj.items()}


def ranges_add(ranges,index):
    if ranges and ranges[-1][1]+1==index: ranges[-1][1]=index
    else: ranges.append([index,index])


def convolution(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out


def psum(a,b,sign=1):
    out=list(a)+[0]*max(0,len(b)-len(a))
    for i,x in enumerate(b): out[i]+=sign*x
    return out


def polynomial(values):
    """Nine exact coefficients from 16 finite dyadic input words.

    Inputs a0,a1,nu0,nu1,d0[3],d1[3],e0[3],e1[3]. All use a common
    exponent only for integer formation; it does not discard a low word.
    """
    ds=[dyadic(x) for x in values]
    e=min((q[1] for q in ds if q[0]),default=0)
    v=[q[0]<<(q[1]-e) if q[0] else 0 for q in ds]
    a=v[0:2];nu=v[2:4]
    d=[[v[4+i],v[7+i]] for i in range(3)]
    second=[[v[10+i],v[13+i]] for i in range(3)]
    Q=[0]*3
    for component in d: Q=psum(Q,convolution(component,component))
    cross=[]
    for i,j in ((1,2),(2,0),(0,1)):
        cross.append(psum(convolution(d[i],second[j]),convolution(d[j],second[i]),-1))
    W=[0]*5
    for component in cross: W=psum(W,convolution(component,component))
    positive=convolution(convolution(a,a),W)
    negative=convolution(convolution(nu,nu),convolution(convolution(Q,Q),Q))
    exponent=min(6*e,8*e)
    coefficients=[0]*9
    for i,x in enumerate(positive): coefficients[i]+=x<<(6*e-exponent)
    for i,x in enumerate(negative): coefficients[i]-=x<<(8*e-exponent)
    return coefficients,exponent,a,e


def point_P(a,nu,d,e):
    ds=[dyadic(x) for x in d];es=[dyadic(x) for x in e]
    Q=total(mul(x,x) for x in ds)
    cross=[sub(mul(ds[i],es[j]),mul(ds[j],es[i])) for i,j in ((1,2),(2,0),(0,1))]
    W=total(mul(x,x) for x in cross)
    return sub(mul(mul(dyadic(a),dyadic(a)),W),
        mul(mul(dyadic(nu),dyadic(nu)),mul(mul(Q,Q),Q)))


class ResourceStop(RuntimeError): pass


class Budget:
    def __init__(self,seconds):
        self.started=time.monotonic();self.deadline=self.started+seconds
        self.current=dict(phase="binding",query_index=None,angle_index=None,trial_index=None)

    def check(self,**current):
        if current: self.current.update(current)
        if time.monotonic()>=self.deadline:
            raise ResourceStop("explicit post-model scientific wall budget exhausted")

    def elapsed(self): return time.monotonic()-self.started


class Ledger:
    def __init__(self,path,maximum,bank):
        self.path=path;self.maximum=maximum;self.bank=bank;self.bytes=0;self.rows=0
        self.digest=hashlib.sha256()
        self.compressed_digest=hashlib.sha256();self.compressed_bytes=0
        self.raw_file=path.open("xb")
        owner=self
        class Sink:
            def write(self,raw):
                written=owner.raw_file.write(raw)
                require(written==len(raw),"Whole compressed ledger write")
                owner.compressed_digest.update(raw);owner.compressed_bytes+=written
                return written
            def flush(self):owner.raw_file.flush()
        self.file=gzip.GzipFile(fileobj=Sink(),mode="wb",compresslevel=1,mtime=0)

    def write(self,value):
        raw=canonical(value)
        if self.bank[0]+len(raw)>self.maximum:
            raise ResourceStop("explicit uncompressed temporary-ledger byte cap reached")
        self.file.write(raw);self.digest.update(raw);self.bytes+=len(raw);self.bank[0]+=len(raw);self.rows+=1

    def close(self):
        self.file.close();self.raw_file.flush();self.raw_file.close()
        return dict(file=self.path.name,bytes=self.compressed_bytes,
            sha256=self.compressed_digest.hexdigest(),complete_written_JSONL_records=self.rows,
            uncompressed_bytes=self.bytes,uncompressed_sha256=self.digest.hexdigest(),
            recomputable_temporary_only=True,uploaded=False)


class Packets:
    def __init__(self,root,np):
        self.root=root.resolve(strict=True);self.np=np
        self.cache=OrderedDict();self.cache_bytes=0;self.verified={}

    def path(self,desc):
        rel=Path(desc["file"])
        require(not rel.is_absolute() and ".." not in rel.parts,"Contained original packet path")
        path=self.root/rel
        require(not path.is_symlink() and path.resolve(strict=True).is_relative_to(self.root),
            "Original packet may not escape capture root")
        return path

    def get(self,desc):
        path=self.path(desc);key=desc["file"]
        if key in self.cache:
            self.cache.move_to_end(key);return self.cache[key]
        require(path.stat().st_size==desc["bytes"] and file_sha(path)==desc["sha256"],
            "Complete original packet bytes/SHA changed: "+key)
        with self.np.load(path,allow_pickle=False) as saved:
            require(set(saved.files)==set(desc["arrays"]),"All original array names bound")
            arrays={}
            for name,identity in desc["arrays"].items():
                a=self.np.array(saved[name],copy=True,order="C")
                require(a.dtype.str==identity["dtype"] and list(a.shape)==identity["shape"]
                    and a.nbytes==identity["raw_bytes"] and identity["order"]=="C"
                    and sha(a.tobytes(order="C"))==identity["raw_sha256"],
                    "All original array words bound: "+key+"/"+name)
                require(a.dtype.kind in "fiu" and not a.dtype.hasobject,"Numerical original array")
                arrays[name]=a
        size=sum(a.nbytes for a in arrays.values())
        while self.cache and self.cache_bytes+size>134217728:
            _,old=self.cache.popitem(last=False);self.cache_bytes-=sum(a.nbytes for a in old.values())
        self.cache[key]=arrays;self.cache_bytes+=size
        self.verified[key]=dict(file=key,bytes=desc["bytes"],sha256=desc["sha256"],
            arrays=desc["arrays"])
        return arrays


def np_identity(a):
    return dict(dtype=a.dtype.str,shape=list(a.shape),order="C",
        raw_bytes=a.nbytes,raw_sha256=sha(a.tobytes(order="C")))


def old_array_identity(a):
    raw=str(a.shape).encode("ascii")+b"\0"+a.dtype.str.encode("ascii")+b"\0"+a.tobytes(order="C")
    return dict(shape=list(a.shape),dtype=a.dtype.str,bytes=a.nbytes,sha256=sha(raw))


def compare_old_identity(a,claimed):
    got=old_array_identity(a)
    require(all(claimed.get(k)==got[k] for k in got),"Original A-chunk identity unchanged")


def save_words(path,np,**arrays):
    require(not path.exists(),"New diagnostic word output cannot overwrite a packet")
    out={k:np.ascontiguousarray(v) for k,v in arrays.items()}
    with path.open("xb") as f: np.savez(f,**out)
    return dict(**receipt(path),arrays={k:np_identity(v) for k,v in out.items()},
        new_post_model_formed_words_not_original_producer_outputs=True)


def exact_action(J,P,dy,dp,budget):
    n=J.shape[0]
    yy=[dyadic(x) for x in dy];pp=[dyadic(x) for x in dp]
    result=[]
    for i in range(n):
        if i%8==0: budget.check(phase="exact-original-chunk-JP-action")
        terms=[mul(dyadic(J[i,j]),yy[j]) for j in range(len(yy))]
        terms.extend(mul(dyadic(P[i,j]),pp[j]) for j in range(len(pp)))
        result.append(total(terms))
    return result


def hermite(weights,h,yl,fl,yr,fr):
    return total((mul(weights[0],yl),mul(mul(h,weights[1]),fl),
        mul(weights[2],yr),mul(mul(h,weights[3]),fr)))


def residual_trial_slots(model):
    trials=(model or {}).get("trials",[])
    require(isinstance(trials,list) and len(trials)<=ALPHAS,"Original bounded17 trial list")
    slots=[]
    for j in range(ALPHAS):
        actual=trials[j] if j<len(trials) else None
        if actual is not None:
            require(isinstance(actual,dict) and word(actual["alpha"])==word(2.0**(-j)),
                "Do not relabel an original alpha or trial order")
        slots.append(dict(trial_index=j,alpha_float64le=word(2.0**(-j)),
            original_trial_visited=actual is not None,original_record=actual,
            nonlinear_return_exists=False,selected_query_call_index=None,
            pointwise_query_defects_complete=False))
    return slots


def bind(capture,packets,model,code,np):
    require(capture.get("schema")==CAPTURE_SCHEMA,"Real observation schema")
    require(capture.get("source_sha256")==CAPTURE_SHA and
        file_sha(code/CAPTURE_NAME)==CAPTURE_SHA,"Capture source words")
    expected=[dict(kind="left-RMS",interval=j,fraction=0.17267316464601146) for j in LEFT]
    expected.extend(dict(kind="collocation-midpoint",interval=j,fraction=.5) for j in MID)
    require(capture.get("query_specs")==expected,"Complete typed37 fixed order")
    require(not capture.get("errors"),"Incomplete original observation remains unresolved")
    require(len(capture["domains"])==1 and len(capture["chosen_directions"])==1
        and len(capture["original_direction_documents"])==1,
        "Need the one actual original full model and final direction")
    domain=capture["domains"][0];choice=capture["chosen_directions"][0]
    direction=capture["original_direction_documents"][0]
    require(domain["B_model_sha256"]==choice["B_model_sha256"],"Same actual B model")
    require((domain["dimension"],domain["n"],domain["M"],domain["N"],domain["k"],
        domain["K"],domain["free"],domain["m"],domain["coordinate_size"])==
        (453,338,112,2048,3,3,109,699,236036),"Original complete finite dimensions")
    require(domain["core_slice"]==[338,450] and domain["parameter_slice"]==[450,453],
        "Original constant core and parameter slices")
    require(domain["original_q_jet_source_sha256"]==FFT_SHA and
        domain["original_q_unpack_source_sha256"]==UNPACK_SOURCE_SHA,"Original full FFT/unpack source")
    compact="".join(domain["original_q_unpack_text"].split())
    require(compact=="defunpack(self,y):returny[:self.M+1],y[self.M+1:2*self.M+1],y[2*self.M+1:]",
        "Use exactly the bound original338 Fourier coefficient partition")
    require(direction["original_resume_sha256"]==capture["source_input_warm"]["sha256"]
        and direction["original_damping"]==270,"Actual original parent and damping")
    require(len(domain["queries"])==GROUPS and len(domain["controls"])==GROUPS
        and len(domain["angular_return_indices"])==GROUPS,"All base37 returns")
    base=packets.get(domain["arrays"]);selected=packets.get(choice["packet"])
    words=packets.get(direction["packet"])
    require(words["coefficient_direction"].shape==(236036,) and
        words["scaled_direction"].shape==(236036,) and selected["z"].shape==(236036,),
        "Actual full chosen direction dimensions")
    require(words["scaled_direction"].tobytes()==selected["z"].tobytes(),
        "The written chosen direction is the actual final z")
    require(selected["Bz"].shape==(ROWS,),"All original75776 Bz readout")
    require(base["y"].shape==(699,453) and base["rhs"].shape==(699,453)
        and base["mesh"].shape==(699,) and base["scale"].shape==(236036,),
        "Complete base arrays before endpoint selection")
    require(np.array_equal(base["endpoint_nodes"],np.arange(463,492,dtype=np.int64))
        and base["inlet"].shape==(338,109),"Actual complete declared support")
    for key in ("y","rhs","mesh","scale","inlet"):
        require(np.all(np.isfinite(base[key])),"Finite original base input: "+key)
    require(np.all(np.isfinite(words["coefficient_direction"])),"Finite actual original direction")
    require(len(capture["evaluations"])>=1,"Actual original evaluated base")
    evaluations={row["index"]:row for row in capture["evaluations"]}
    require(len(evaluations)==len(capture["evaluations"]),"Unique original evaluation indices")
    base_eval=evaluations[domain["base_evaluation_index"]]
    be=packets.get(base_eval["returned_array_packet"])
    require(be["y"].tobytes()==base["y"][base["endpoint_nodes"]].tobytes()
        and be["f"].tobytes()==base["rhs"][base["endpoint_nodes"]].tobytes(),
        "Domain base and observed original evaluation are identical")
    angular={row["index"]:row for row in capture["angular_returns"]}
    require(len(angular)==len(capture["angular_returns"]),"Unique original angular returns")
    calls={row["evaluation_index"]:row for row in capture["selected_query_calls"]}
    require(len(calls)==len(capture["selected_query_calls"]),"One selected call per observed trial")
    slots=residual_trial_slots(model)
    for slot in slots:
        original=slot["original_record"]
        if original is None: continue
        report=original.get("domain")
        tag=report.get("R334_read_only_capture") if isinstance(report,dict) else None
        if not isinstance(tag,dict): continue
        idx=tag["evaluation_index"]
        require(idx in evaluations and evaluations[idx]["coordinates"]==tag["coordinates"],
            "Bind actual trial coordinates, not a second RMS or FD evaluation")
        ev=evaluations[idx]
        slot["nonlinear_return_exists"]=True
        slot["evaluation_index"]=idx
        slot["original_require_rms"]=ev["original_require_rms"]
        require(ev["original_require_rms"] is False,"First actual no-RMS line-search evaluation")
        slot["returned_array_packet"]=ev["returned_array_packet"]
        call=calls.get(idx)
        if call is None: continue
        slot["selected_query_call_index"]=call["index"]
        require(len(call["original_reports"])==GROUPS,"All selected original query reports")
        selected_beta=packets.get(call["actual_beta_arrays"])["beta"]
        require(selected_beta.shape==(GROUPS,ANGLES),"All original returned selected beta rows")
        slot["original_selected_beta_array_packet"]=call["actual_beta_arrays"]
        seq=iter(call["angular_return_indices"]);mapping={}
        for q,report in enumerate(call["original_reports"]):
            require(report["query_index"]==q and report["kind"]==expected[q]["kind"]
                and report["interval"]==expected[q]["interval"],"Original selected query order")
            if report["original_query_input_finite"]:
                index=next(seq,None);require(index in angular,"Returned angular packet exists")
                row=angular[index]
                require(row["context"].get("evaluation_index")==idx and
                    row["context"].get("selected_call")==call["index"],
                    "Actual angular packet belongs to this actual trial")
                require(row["station_float64le"]==domain["queries"][q]["station_float64le"],
                    "Same actual physical query station")
                data=packets.get(row["packet"])
                compare_old_identity(data["query"],report["original_query_array"])
                require(data["beta"].tobytes()==selected_beta[q].tobytes(),
                    "Original angular return and selected beta words are the same observation")
                mapping[q]=index
            else: mapping[q]=None
        require(next(seq,None) is None,"No unexplained angular returns")
        slot["angular_by_query"]=mapping
        slot["original_query_reports"]=call["original_reports"]
    return domain,choice,direction,base,selected,words,angular,slots


def new_alpha_stats(j):
    return dict(trial_index=j,alpha_float64le=word(2.0**(-j)),complete_rows=0,
        exact_affine_endpoint_feasible_count=0,
        exact_affine_interval_certified_count=0,
        exact_affine_interval_endpoint_refuted_count=0,
        exact_affine_interval_unresolved_count=0,undefined_count=0,
        endpoint_nonpositive_ranges=[],interval_unresolved_ranges=[],
        interval_endpoint_refuted_ranges=[],undefined_ranges=[],
        minima={})


def affine_row(values,global_row,bernstein_weights):
    c,e,a,ae=polynomial(values)
    row=dict(global_row=global_row,query_index=global_row//ANGLES,
        angle_index=global_row%ANGLES,coefficients_integer_hex=[integer_hex(x) for x in c],
        coefficients_exponent2=e,coefficient_count=9,
        scalar_a_integer_hex=[integer_hex(x) for x in a],scalar_a_exponent2=ae,
        dyadic_trials=[])
    for j in range(ALPHAS):
        shifts=[x<<(j*(8-k)) for k,x in enumerate(c)]
        p=sum(shifts);b=[sum(bernstein_weights[i][k]*shifts[k] for k in range(i+1))
            for i in range(9)]
        aend=(a[0]<<j)+a[1]
        endpoint=aend>0 and p>0
        initial=a[0]>0 and c[0]>0
        certified=initial and aend>0 and min(b)>0
        refuted=not (initial and endpoint)
        row["dyadic_trials"].append(dict(trial_index=j,
            endpoint_P_integer_hex=integer_hex(p),P_exponent2=e-8*j,
            endpoint_a_integer_hex=integer_hex(aend),a_exponent2=ae-j,
            Bernstein_280_integer_hex=[integer_hex(x) for x in b],
            Bernstein_exponent2=e-8*j,Bernstein_positive_denominator=280,
            affine_endpoint_strict=endpoint,affine_closed_interval_certified=certified,
            affine_closed_interval_endpoint_refuted=refuted))
    return row


def commit_affine_row(row,stats):
    # The whole row has already reached the temporary ledger. A byte-cap stop
    # cannot leave its 17 counters ahead of the declared complete-row prefix.
    global_row=row["global_row"]
    for value,s in zip(row["dyadic_trials"],stats):
        s["complete_rows"]+=1
        if value["affine_endpoint_strict"]:s["exact_affine_endpoint_feasible_count"]+=1
        else:ranges_add(s["endpoint_nonpositive_ranges"],global_row)
        if value["affine_closed_interval_certified"]:s["exact_affine_interval_certified_count"]+=1
        elif value["affine_closed_interval_endpoint_refuted"]:
            s["exact_affine_interval_endpoint_refuted_count"]+=1
            ranges_add(s["interval_endpoint_refuted_ranges"],global_row)
        else:
            s["exact_affine_interval_unresolved_count"]+=1
            ranges_add(s["interval_unresolved_ranges"],global_row)
        p=int(value["endpoint_P_integer_hex"],16)
        a=int(value["endpoint_a_integer_hex"],16)
        b=min(int(x,16) for x in value["Bernstein_280_integer_hex"])
        note_extreme(s["minima"],"P_endpoint",canonical_d(p,value["P_exponent2"]),global_row,minimum=True)
        note_extreme(s["minima"],"a_endpoint",canonical_d(a,value["a_exponent2"]),global_row,minimum=True)
        note_extreme(s["minima"],"280_times_minimum_Bernstein_coefficient",
            canonical_d(b,value["Bernstein_exponent2"]),global_row,minimum=True)


def fresh_point_stats(trial_index,query_index):
    return dict(trial_index=trial_index,query_index=query_index,complete_rows=0,
        original_normal_beta_nonpositive_ranges=[],original_normal_beta_nonfinite_ranges=[],
        original_cross_beta_nonpositive_ranges=[],original_cross_beta_nonfinite_ranges=[],
        exact_actual_P_nonpositive_ranges=[],exact_actual_a_nonpositive=False,
        exact_actual_geometry_undefined_ranges=[],exact_actual_point_positive_count=0,
        extrema={})


def point_rows(j,q,actual,base,d1,e1,scalar1,budget,ledger,stats):
    a=float(actual["scalar"][0]);nu=float(actual["scalar"][1])
    stats["exact_actual_a_nonpositive"]=math.isfinite(a) and a<=0
    stats["actual_original_scalar_float64le"]=[word(x) for x in actual["scalar"]]
    stats["original_normal_beta_minimum"]=None
    stats["original_cross_beta_minimum"]=None
    stats["complete"]=False
    for i in range(ANGLES):
        if i%32==0:budget.check(phase="actual-pointwise-query-geometry",query_index=q,
            trial_index=j,angle_index=i)
        raw=dict(trial_index=j,query_index=q,angle_index=i)
        flags=[]
        for label,key in (("normal","beta"),("cross","cross_beta")):
            x=float(actual[key][i])
            raw["original_"+label+"_beta_float64le"]=word(x)
            if not math.isfinite(x):flags.append("original_"+label+"_beta_nonfinite_ranges")
            elif x<=0:flags.append("original_"+label+"_beta_nonpositive_ranges")
        finite=all(math.isfinite(float(x)) for x in [a,nu,*actual["first"][i],*actual["second"][i]])
        differences={};terms_by_name={};p=None
        if not finite:
            flags.append("exact_actual_geometry_undefined_ranges")
            raw["exact_actual_geometry_defined"]=False
        else:
            p=point_P(a,nu,actual["first"][i],actual["second"][i])
            if p[0]<=0:flags.append("exact_actual_P_nonpositive_ranges")
            for name,current,initial,slope in (
                ("first",actual["first"][i],base["first"][i],d1[i]),
                ("second",actual["second"][i],base["second"][i],e1[i]),
                ("scalar",actual["scalar"][:2],base["scalar"][:2],scalar1[:2])):
                terms=[sub(sub(dyadic(x),dyadic(y)),scale_pow2(dyadic(z),-j))
                    for x,y,z in zip(current,initial,slope)]
                differences[name]=[packed(x) for x in terms];terms_by_name[name]=terms
            raw.update(exact_actual_geometry_defined=True,P=packed(p),
                actual_minus_formed_word_affine=differences,
                pointwise_only_not_an_enclosure_between_alphas=True)
        ledger.write(raw)
        for name in flags:ranges_add(stats[name],i)
        for label,key in (("normal","beta"),("cross","cross_beta")):
            x=float(actual[key][i]);record_key="original_"+label+"_beta_minimum"
            old=stats[record_key]
            if math.isfinite(x) and (old is None or x<old["value"]):
                stats[record_key]=dict(value=x,float64le=word(x),angle_index=i,
                    original_returned_scalar_not_recomputed=True)
        if p is not None:
            if a>0 and p[0]>0:stats["exact_actual_point_positive_count"]+=1
            note_extreme(stats["extrema"],"minimum_actual_P",p,i,minimum=True)
            for name,terms in terms_by_name.items():
                for component,x in enumerate(terms):
                    note_extreme(stats["extrema"],name+"_maximum_absolute_actual_minus_affine",x,
                        dict(angle_index=i,component=component))
        stats["complete_rows"]+=1
    stats["complete"]=True
    return stats


def hermite_defect(j,q,query,base_query,trial_query,y0,f0,ya,fa,dy,ELlinear,ERlinear,
        delta_query,budget,ledger,summary):
    h=dyadic(unword(query["h_float64le"]))
    weights=[dyadic(unword(x)) for x in query["hermite_weights_float64le"]]
    dimension=len(base_query);terms_summary=summary["extrema"];nonzero=summary["nonzero_component_ranges"]
    require(dimension==453 and len(delta_query)==453,"Full augmented Hermite identity")
    endpoint_rows=[]
    for side,fs,ft,linear in (("left",f0[0],fa[0],ELlinear),("right",f0[1],fa[1],ERlinear)):
        defects=[sub(sub(dyadic(b),dyadic(a)),scale_pow2(linear[c],-j))
            for c,(a,b) in enumerate(zip(fs,ft))]
        endpoint_rows.append(defects)
    for c in range(dimension):
        if c%32==0:budget.check(phase="complete453-pointwise-Hermite-identity",
            query_index=q,trial_index=j,angle_index=None)
        yl0,yr0=dyadic(y0[0][c]),dyadic(y0[1][c])
        fl0,fr0=dyadic(f0[0][c]),dyadic(f0[1][c])
        yla,yra=dyadic(ya[0][c]),dyadic(ya[1][c])
        fla,fra=dyadic(fa[0][c]),dyadic(fa[1][c])
        dl,dr=dyadic(dy[0][c]),dyadic(dy[1][c])
        dnode_l=sub(sub(yla,yl0),scale_pow2(dl,-j))
        dnode_r=sub(sub(yra,yr0),scale_pow2(dr,-j))
        node_term=add(mul(weights[0],dnode_l),mul(weights[2],dnode_r))
        EL,ER=endpoint_rows[0][c],endpoint_rows[1][c]
        rhs_term=mul(h,add(mul(weights[1],EL),mul(weights[3],ER)))
        k0=sub(dyadic(base_query[c]),hermite(weights,h,yl0,fl0,yr0,fr0))
        ka=sub(dyadic(trial_query[c]),hermite(weights,h,yla,fla,yra,fra))
        kterm=sub(ka,k0)
        exact_reference=hermite(weights,h,dl,ELlinear[c],dr,ERlinear[c])
        formation=scale_pow2(sub(exact_reference,dyadic(delta_query[c])),-j)
        lhs=sub(sub(dyadic(trial_query[c]),dyadic(base_query[c])),
            scale_pow2(dyadic(delta_query[c]),-j))
        rhs=total((node_term,rhs_term,kterm,formation))
        require(compare(lhs,rhs)==0,"Exact453 Hermite decomposition identity must close")
        values=dict(node_formation=node_term,RHS_defect=rhs_term,
            query_program_finite_formation=kterm,direction_word_formation=formation,
            actual_query_minus_affine=lhs,left_RHS_remainder=EL,right_RHS_remainder=ER,
            base_query_program_difference=k0,actual_query_program_difference=ka)
        ledger.write(dict(kind="full453-Hermite-defect",trial_index=j,query_index=q,
            component=c,identity_exactly_equal=True,terms={k:packed(v) for k,v in values.items()},
            exact_original_JP_action_left=packed(ELlinear[c]),
            exact_original_JP_action_right=packed(ERlinear[c])))
        for name,value in values.items():
            note_extreme(terms_summary,name,value,c)
            if value[0]:ranges_add(nonzero.setdefault(name,[]),c)
        summary["exact_identity_equal_count"]+=1
    summary["complete"]=True
    return summary


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capture",type=Path,required=True)
    parser.add_argument("--model-directory",type=Path,required=True)
    parser.add_argument("--code-directory",type=Path,required=True)
    parser.add_argument("--seconds",type=int,default=1800)
    parser.add_argument("--max-ledger-bytes",type=int,default=8589934592)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS")=="true" and
        os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,"Only the public scientific Actions")
    require(args.seconds>0 and args.max_ledger_bytes>0,"Explicit diagnostic resources")
    temporary=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    for p in (args.capture,args.model_directory,args.out):
        require(p.resolve().is_relative_to(temporary) and p.resolve()!=temporary
            and not p.is_symlink(),"All scientific payload stays in this job temporary root")
    require(not args.out.exists(),"New diagnostic output must be fresh")
    args.out.mkdir(parents=True);large=args.out/"large-arrays";large.mkdir()
    code=args.code_directory.resolve(strict=True)
    require(file_sha(code/FFT_NAME)==FFT_SHA,"Original Fourier finite implementation")
    import numpy as np
    spec=importlib.util.spec_from_file_location("_request158_original_fft",code/FFT_NAME)
    fft=importlib.util.module_from_spec(spec);spec.loader.exec_module(fft)
    budget=Budget(args.seconds);packets=Packets(args.capture,np)
    def external_stop(signum,frame):
        raise ResourceStop("external signal "+str(signum)+" interrupted this diagnostic; original science is separate")
    signal.signal(signal.SIGTERM,external_stop)
    signal.signal(signal.SIGINT,external_stop)
    result=dict(schema=SCHEMA,request=158,run_id=os.environ.get("GITHUB_RUN_ID"),
        source_commit=os.environ.get("GITHUB_SHA"),source_sha256=file_sha(__file__),
        proof_sha256=PROOF_SHA,post_model_scientific_arithmetic=True,
        original_model_and_FD_gates_not_changed=True,extra_RHS_J_QR_or_optimization_calls=0,
        all37_queries_required=True,all_N2048_rows_required=True,
        declared_affine_rows=ROWS,declared_dyadic_alpha_count=ALPHAS,
        declared_exact_polynomial_coefficients=9,declared_Hermite_components=453,
        scientific_completed=False,resource_partial=False,phase="binding",
        scientific_exception=None,affine_complete_rows=0,
        affine_undefined_rows=0,affine_undefined_ranges=[],completed_query_indices=[],
        actual_point_query_summaries=[],actual_Hermite_query_summaries=[],
        finite_word_affine_direction_formation_outputs=[],
        exact_chunk_action_variants=[],temporary_ledgers=[],verified_original_packets=[],
        algorithm_scope=dict(formed_FFT_derivative_words_not_an_exact_IEEE_roundmap_derivative=True,
            actual_normal_formula_not_replaced_by_cross_formula=True,
            interval_certificate_applies_to_recorded_dyadic_affine_reference_only=True,
            actual_trial_returns_are_pointwise_not_a_whole_alpha_curve_enclosure=True,
            no_actual_rhs_second_derivative_enclosure=True,
            all2048_angles_are_complete_original_discrete_grid_not_angle_continuum=True,
            full_original_Bz_read_not_inverted_into_inputs=True,
            no_new_native_fullDN_or_metric_certificate=True))
    ledgers=[];ledger_bank=[0];stats=[new_alpha_stats(j) for j in range(ALPHAS)]
    cursor=dict(query_index=0,phase="binding",angle_index=0,trial_index=None)
    slots=[];exit_code=2
    def checkpoint():
        result["phase"]=budget.current["phase"]
        result["active_cursor"]=dict(budget.current)
        result["elapsed_seconds"]=budget.elapsed()
        view=dict(result)
        view["checkpoint_only"]=True
        count=result["affine_complete_rows"]
        view["unvisited_affine_row_ranges"]=[[count,ROWS-1]] if count<ROWS else []
        view["affine_alpha_results"]=[dict(row,minima=output_extremes(row["minima"])) for row in stats]
        view["actual_point_query_summaries"]=[dict(row,extrema=output_extremes(row["extrema"]))
            if "extrema" in row else dict(row) for row in result["actual_point_query_summaries"]]
        view["actual_Hermite_query_summaries"]=[]
        for row in result["actual_Hermite_query_summaries"]:
            copy=dict(row)
            if "extrema" in copy:copy["maximum_absolute_terms"]=output_extremes(copy.pop("extrema"))
            view["actual_Hermite_query_summaries"].append(copy)
        view["checkpoint_uncompleted_scope_is_not_claimed_processed"]=True
        tmp=args.out/"result.json.partial"
        tmp.write_bytes(canonical(view));tmp.replace(args.out/"result.json")
    try:
        capture=read(args.capture/"capture.json")
        model_path=args.model_directory/"model-000.json"
        model=read(model_path) if model_path.is_file() else None
        result["original_capture_manifest"]=receipt(args.capture/"capture.json")
        result["original_model_document"]=receipt(model_path) if model_path.is_file() else None
        result["original_observation_completed"]=capture.get("observation_complete")
        result["original_model_returned"]=capture.get("original_model_returned")
        result["original_model_exit_code"]=capture.get("original_model_exit_code")
        result["original_model_exception"]=capture.get("original_exception")
        result["original_model_accepted"]=(model or {}).get("accepted")
        domain,choice,direction,base,selected,words,angular,slots=bind(capture,packets,model,code,np)
        result["original_source_pair"]=dict(warm=capture["source_input_warm"],
            status=capture["source_parent_status"])
        result["actual_original_direction"]=direction
        result["actual_final_choice"]=choice
        result["actual_B_model_sha256"]=domain["B_model_sha256"]
        result["complete_original_domain_binding"]=domain
        result["original_scientific_source_bindings"]={key:capture[key] for key in
            ("original_producer","original_observer","original_domain","original_FFT","original_engine")}
        result["new_FFT_and_scalar_action_is_explicit_post_model_arithmetic"]=True
        result["formed_reference_not_asserted_bitwise_equal_to_original_sparse_B_matvec"]=True
        result["query_specs"]=capture["query_specs"]
        result["original_complete_selected_query_calls"]=capture["selected_query_calls"]
        result["original_trial_slots"]=slots
        result["exact_Hermite_method"]="q-H(Y,F) retained for base and actual returns; no SciPy/float equality assumed"
        coefficient=words["coefficient_direction"]
        physical_size=domain["physical_size"];free=domain["free"]
        require(physical_size==(699-1)*338,"Complete original coordinate layout")
        physical=coefficient[:physical_size].reshape(698,338)
        core=coefficient[physical_size:physical_size+free]
        dp=coefficient[physical_size+free:]
        dy=np.zeros((699,453),dtype=np.float64)
        dy[1:,:338]=physical;dy[0,:338]=base["inlet"]@core
        dy[:,341:450]=core;dy[:,450:453]=dp
        require(np.all(np.isfinite(dy)),"Finite lifted actual chosen direction")
        class Query:
            M=112;N=2048
            freq=base["q_frequency"]
            def unpack(self,y):
                return y[:self.M+1],y[self.M+1:2*self.M+1],y[2*self.M+1:]
        query_object=Query()
        bweights=[[280*math.comb(i,k)//math.comb(8,k) for k in range(i+1)] for i in range(9)]
        require(all((280*math.comb(i,k))%math.comb(8,k)==0 for i in range(9)
            for k in range(i+1)),"Exact common280 Bernstein denominator")
        polynomial_ledger=Ledger(large/"all-row-polynomials-and-Bernstein.jsonl.gz",args.max_ledger_bytes,ledger_bank)
        point_ledger=Ledger(large/"actual-query-point-geometry.jsonl.gz",args.max_ledger_bytes,ledger_bank)
        defect_ledger=Ledger(large/"all453-pointwise-Hermite-decomposition.jsonl.gz",args.max_ledger_bytes,ledger_bank)
        action_ledger=Ledger(large/"original-chunk-exact-JP-actions.jsonl.gz",args.max_ledger_bytes,ledger_bank)
        ledgers=[polynomial_ledger,point_ledger,defect_ledger,action_ledger]
        action_cache={}
        nodes=base["endpoint_nodes"];node_map={int(v):i for i,v in enumerate(nodes)}
        for q,query in enumerate(domain["queries"]):
            budget.check(phase="query-binding",query_index=q,angle_index=0,trial_index=None)
            require(query["query_index"]==q and query["kind"]==capture["query_specs"][q]["kind"]
                and query["interval"]==capture["query_specs"][q]["interval"],"Actual query identity")
            original=packets.get(query["packet"])
            base_angular=angular[domain["angular_return_indices"][q]]
            require(base_angular["station_float64le"]==query["station_float64le"],
                "Bind original base physical station")
            b=packets.get(base_angular["packet"])
            require(b["query"].tobytes()==original["query"].tobytes(),"Exact same base query words")
            require(b["first"].shape==(ANGLES,3) and b["second"].shape==(ANGLES,3)
                and b["scalar"].shape==(3,),"Complete original angular and scalar returns")
            require(all(np.all(np.isfinite(b[k])) for k in ("query","first","second","scalar")),
                "Finite original domain-build data")
            controls=domain["controls"][q]
            require(controls["station_float64le"]==query["station_float64le"],"Actual scalar controls")
            control=packets.get(controls["packet"])["controls"]
            require(control.shape==(3,3) and np.all(np.isfinite(control)),"All original scalar control columns")
            j=query["interval"];h=unword(query["h_float64le"])
            weights=[unword(x) for x in query["hermite_weights_float64le"]]
            rounded=[];exact=[]
            for side,node in (("left",j),("right",j+1)):
                J,P=original[side+"_J"],original[side+"_P"]
                require(J.shape==(338,338) and P.shape==(338,3)
                    and np.all(np.isfinite(J)) and np.all(np.isfinite(P)),"Whole original endpoint J/P")
                identities=query["endpoint_original_identities"][side]
                compare_old_identity(J,identities["physical"]);compare_old_identity(P,identities["parameter"])
                formed=np.zeros(453,dtype=np.float64)
                formed[:338]=J@dy[node,:338]+P@dp
                require(np.all(np.isfinite(formed)),"Finite formed reference J/P action")
                rounded.append(formed)
                key=(node,identities["physical"]["sha256"],identities["parameter"]["sha256"])
                if key not in action_cache:
                    values=exact_action(J,P,dy[node,:338],dp,budget)+[ZERO]*(453-338)
                    action_cache[key]=values
                    desc=dict(node=node,physical_sha256=key[1],parameter_sha256=key[2],
                        exact_components=453,physical_components=338,constant_components=115,
                        original_call_number=query["endpoint_original_call_number"],
                        identity_used_for_cache_not_node_alone=True)
                    result["exact_chunk_action_variants"].append(desc)
                    action_ledger.write(dict(**desc,exact_action=[packed(v) for v in values]))
                exact.append(action_cache[key])
            if query["kind"]=="collocation-midpoint":
                delta_query=.5*(dy[j]+dy[j+1])-h*(rounded[1]-rounded[0])/8
            else:
                delta_query=(weights[0]*dy[j]+h*weights[1]*rounded[0]+
                    weights[2]*dy[j+1]+h*weights[3]*rounded[1])
            _,d1,e1=fft.fft_jet(query_object,np.asarray(delta_query[:338]))
            scalar1=control@dp
            require(np.all(np.isfinite(delta_query)) and np.all(np.isfinite(d1))
                and np.all(np.isfinite(e1)) and np.all(np.isfinite(scalar1)),
                "Finite explicitly formed affine-reference words")
            result["finite_word_affine_direction_formation_outputs"].append(
                save_words(large/("query-%02d-reference-words.npz"%q),np,
                    coefficient_node_left=dy[j],coefficient_node_right=dy[j+1],
                    scalar_controls=control,parameter_direction=dp,
                    rounded_endpoint_action_left=rounded[0],rounded_endpoint_action_right=rounded[1],
                    query_direction=delta_query,first_direction=d1,second_direction=e1,
                    scalar_direction=scalar1,original_Bz=selected["Bz"][q*ANGLES:(q+1)*ANGLES]))
            for i in range(ANGLES):
                if i%16==0:budget.check(phase="all9-exact-polynomial-and-17-Bernstein",
                    query_index=q,angle_index=i,trial_index=None)
                values=[b["scalar"][0],scalar1[0],b["scalar"][1],scalar1[1],
                    *b["first"][i],*d1[i],*b["second"][i],*e1[i]]
                row=affine_row(values,q*ANGLES+i,bweights)
                polynomial_ledger.write(row)
                commit_affine_row(row,stats)
                result["affine_complete_rows"]+=1
            for slot in slots:
                alpha_index=slot["trial_index"]
                mapping=slot.get("angular_by_query")
                if mapping is None: continue
                actual_index=mapping.get(q)
                if actual_index is None:
                    result["actual_point_query_summaries"].append(dict(
                        trial_index=alpha_index,query_index=q,complete=True,exact_geometry_defined=False,
                        reason="original actual query nonfinite; original angular evaluation was not called",
                        unresolved_angle_ranges=[[0,ANGLES-1]]))
                    continue
                a=packets.get(angular[actual_index]["packet"])
                require(a["query"].shape==(453,) and a["first"].shape==(ANGLES,3)
                    and a["second"].shape==(ANGLES,3) and a["scalar"].shape==(3,)
                    and a["beta"].shape==(ANGLES,) and a["cross_beta"].shape==(ANGLES,),
                    "Complete original actual angular returns")
                point_stat=fresh_point_stats(alpha_index,q)
                result["actual_point_query_summaries"].append(point_stat)
                point_rows(alpha_index,q,a,b,d1,e1,scalar1,budget,point_ledger,point_stat)
                ev=packets.get(slot["returned_array_packet"])
                yl,yr=node_map[j],node_map[j+1]
                endpoint_values=(ev["y"][[yl,yr]],ev["f"][[yl,yr]])
                if all(np.all(np.isfinite(v)) for v in endpoint_values) and np.all(np.isfinite(a["query"])):
                    defect_stat=dict(trial_index=alpha_index,query_index=q,
                        all_augmented_components=453,exact_identity_equal_count=0,
                        complete=False,extrema={},nonzero_component_ranges={},
                        original_chunk_variants_kept_separate=True,
                        captures_state_RHS_query_and_direction_formation_separately=True,
                        pointwise_only=True,whole_trial_segment_RHS_second_derivative_bound=False)
                    result["actual_Hermite_query_summaries"].append(defect_stat)
                    hermite_defect(alpha_index,q,query,b["query"],a["query"],
                        base["y"][[j,j+1]],base["rhs"][[j,j+1]],
                        endpoint_values[0],endpoint_values[1],dy[[j,j+1]],
                        exact[0],exact[1],delta_query,budget,defect_ledger,defect_stat)
                else:
                    result["actual_Hermite_query_summaries"].append(dict(
                        trial_index=alpha_index,query_index=q,exact_identity_equal_count=0,
                        complete=True,exact_identity_defined=False,reason="nonfinite original actual endpoint/query words",
                        unresolved_component_ranges=[[0,452]]))
            result["completed_query_indices"].append(q)
            checkpoint()
        result["scientific_completed"]=True
        result["phase"]="complete-declared-post-model-readout"
        exit_code=0
    except ResourceStop as error:
        result["resource_partial"]=True;result["stop_reason"]=str(error);exit_code=3
    except BaseException as error:
        result["scientific_exception"]=dict(type=type(error).__name__,message=str(error),
            traceback=traceback.format_exc())
        result["stop_reason"]="input-or-post-model-scientific-program-error";exit_code=2
    finally:
        signal.signal(signal.SIGTERM,signal.SIG_IGN)
        signal.signal(signal.SIGINT,signal.SIG_IGN)
        for ledger in ledgers:
            try:result["temporary_ledgers"].append(ledger.close())
            except Exception as error:
                result.setdefault("readout_errors",[]).append(dict(type=type(error).__name__,message=str(error)))
        result["affine_alpha_results"]=[]
        for s in stats:
            out=dict(s);out["minima"]=output_extremes(s["minima"])
            result["affine_alpha_results"].append(out)
        completed=result["affine_complete_rows"]
        result["unvisited_affine_row_ranges"]=([[completed,ROWS-1]] if completed<ROWS else [])
        result["pending_actual_query_pairs"]=[]
        result["unavailable_original_trial_query_scopes"]=[]
        known={(v["trial_index"],v["query_index"]) for v in result["actual_point_query_summaries"]
            if v.get("complete") is True}
        known_h={(v["trial_index"],v["query_index"]) for v in result["actual_Hermite_query_summaries"]
            if v.get("complete") is True}
        for v in result["actual_point_query_summaries"]:
            if "extrema" in v:v["extrema"]=output_extremes(v["extrema"])
            if v.get("complete") is not True:
                v["unvisited_angle_ranges"]=[[v.get("complete_rows",0),ANGLES-1]]
        for v in result["actual_Hermite_query_summaries"]:
            if "extrema" in v:v["maximum_absolute_terms"]=output_extremes(v.pop("extrema"))
            if v.get("complete") is not True:
                v["unvisited_component_ranges"]=[[v["exact_identity_equal_count"],452]]
        result["temporary_ledgers_total_uncompressed_bytes"]=ledger_bank[0]
        result["all_rows_affine_endpoint_results"]=[dict(
            trial_index=s["trial_index"],alpha_float64le=s["alpha_float64le"],
            all75776_rows_processed=s["complete_rows"]==ROWS,
            all75776_affine_endpoints_strict=(s["complete_rows"]==ROWS and
                s["exact_affine_endpoint_feasible_count"]==ROWS),
            all75776_affine_closed_intervals_certified=(s["complete_rows"]==ROWS and
                s["exact_affine_interval_certified_count"]==ROWS),
            actual_nonlinear_line_search_acceptance_not_implied=True) for s in stats]
        for slot in slots:
            j=slot["trial_index"];mapping=slot.get("angular_by_query")
            if mapping is None:
                if not slot["original_trial_visited"]:
                    reason="original backtracking did not visit this alpha"
                elif not slot["nonlinear_return_exists"]:
                    reason="no bound original nonlinear return; original scalar record is retained"
                else:
                    reason="original nonlinear evaluation returned but selected angular calls have no complete observed result"
                result["unavailable_original_trial_query_scopes"].append(dict(
                    trial_index=j,query_index_range=[0,GROUPS-1],angle_index_range=[0,ANGLES-1],
                    original_trial_visited=slot["original_trial_visited"],
                    original_nonlinear_return_exists=slot["nonlinear_return_exists"],
                    reason=reason,no_new_trial_evaluated_to_fill_this_gap=True))
                continue
            for q in range(GROUPS):
                if (j,q) not in known or (mapping.get(q) is not None and (j,q) not in known_h):
                    result["pending_actual_query_pairs"].append(dict(trial_index=j,query_index=q,
                        geometry_pending=(j,q) not in known,
                        full453_Hermite_pending=mapping.get(q) is not None and (j,q) not in known_h,
                        original_return_exists=mapping.get(q) is not None))
            slot["pointwise_query_defects_complete"]=all(
                (j,q) in known and (mapping.get(q) is None or (j,q) in known_h) for q in range(GROUPS))
        result["verified_original_packets"]=list(packets.verified.values())
        result["elapsed_seconds"]=budget.elapsed()
        result["active_cursor"]=dict(budget.current)
        result["post_model_diagnostic_exit_code"]=exit_code
        result["original_scientific_results_reclassified_by_diagnostic"]=False
        result["raw_artifact_uploads"]=0;result["Git_or_Release_raw_publication"]=False
        raw=canonical(result);(args.out/"result.json").write_bytes(raw)
        summary=dict(schema=SCHEMA,request=158,result=receipt(args.out/"result.json"),
            scientific_completed=result["scientific_completed"],resource_partial=result["resource_partial"],
            affine_complete_rows=completed,unvisited_affine_row_ranges=result["unvisited_affine_row_ranges"],
            actual_point_query_count=len(result["actual_point_query_summaries"]),
            complete_Hermite_query_count=len(result["actual_Hermite_query_summaries"]),
            original_model_accepted=result.get("original_model_accepted"),
            original_model_exit_code=result.get("original_model_exit_code"),
            post_model_diagnostic_exit_code=exit_code,stop_reason=result.get("stop_reason"),
            scientific_exception=result["scientific_exception"],active_cursor=result["active_cursor"],
            elapsed_seconds=result["elapsed_seconds"],
            complete_result_requires_same_job_semantic_readback_before_cleanup=True,
            native_or_full_DN_accepted=False)
        (args.out/"summary.json").write_bytes(canonical(summary))
        print(json.dumps(dict(event="request158_post_model_exact_diagnostic_returned",**summary),
            ensure_ascii=True,separators=(",",":")),flush=True)
    return exit_code


if __name__=="__main__":
    raise SystemExit(main())
