#!/usr/bin/env python3
"""Request170: R354 complete finite endpoint reference and Hermite bounds.

New interval/dyadic arithmetic runs only in public Actions after one original37
model and its original FD attempt. No original RHS/J/QR/FD/optimization call is
made here. Accurate uniform-DFT references are distinct from recorded IEEE
words; all unproved floating execution errors remain explicitly unproved.
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
SCHEMA="R354-original37-finite-endpoint-and-Hermite-enclosures-v1"
CAPTURE_SCHEMA="R354-original37-endpoint-literal-cache-capture-v1"
CAPTURE_NAME="geometry_20261115_R354_thirty_seven_literal_endpoint_capture.py"
CAPTURE_SHA="74fc383db1b00c564ccab9709b1de5f500674914a5efef83997960c867950c4c"
FFT_NAME="geometry_20261114_fft_frenet.py"
FFT_SHA="973898fcea1e8706d0ff9f87bbe72cde3576bc0055149af0a2e2058b144ac401"
UNPACK_SOURCE_SHA="cf163a5c42cff95137a78eefda058b6a18f5f226b4261b686a42e645f4002fcb"
PROOF_SHA="b6e293c20ffb6584f316b3e38877b7e3d4fb61cbad1f008718ab034f605cb183"
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
        if i%8==0: budget.check(phase="exact-original-chunk-JP-action",matrix_row=i)
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


def match_original_query_controls(domain,packets,np):
    """Match actual B-used words, retaining cache fills and every extra call."""
    calls=domain["controls"]
    require(isinstance(calls,list),"All original control returns remain a list")
    require([x.get("observed_call_index") for x in calls]==list(range(len(calls))),
        "The complete actual control return order is explicit")
    matched=[];readback=[]
    for q,query in enumerate(domain["queries"]):
        require(query["query_index"]==q,"Original37 query order")
        field=("scalar_control_jets" if query["kind"]=="left-RMS"
            else "original_scalar_control_jets")
        require(query.get("explicit_identity_copied_from_original_B_query_report") is True
            and query.get("original_explicit_scalar_control_identity_field")==field,
            "The identity is copied from the original explicit B control use")
        claimed=query["original_explicit_scalar_control_identity"]
        candidates=[];exact=[]
        for call_index,record in enumerate(calls):
            if record["station_float64le"]!=query["station_float64le"]:
                continue
            data=packets.get(record["packet"])["controls"]
            require(data.shape==(3,3) and np.all(np.isfinite(data)),
                "All observed same-station complete scalar control words are finite")
            got=old_array_identity(data)
            same=all(claimed.get(k)==got[k] for k in got)
            candidates.append(dict(observed_call_index=call_index,
                original_array_identity=got,matches_original_explicit_identity=same))
            if same:exact.append(call_index)
        require(exact,"No returned control packet matches the actual B query: "+str(q))
        selected=exact[0]
        # Identical returned words suffice. Do not invent which caller filled
        # the cache, or label the representative as the actual explicit call.
        matched.append(dict(calls[selected],matched_query_index=q,
            actual_explicit_array_identity=claimed,matching_observed_call_indices=exact,
            representative_caller_identity_not_claimed=True))
        readback.append(dict(query_index=q,kind=query["kind"],interval=query["interval"],
            station_float64le=query["station_float64le"],
            original_explicit_scalar_control_identity=claimed,
            original_identity_field=field,all_same_station_observed_returns=candidates,
            selected_observed_call_index=selected,matching_observed_call_indices=exact))
    require(len(matched)==GROUPS,"All37 original query controls are matched")
    result=dict(domain)
    result["matched_query_controls"]=matched
    result["query_control_matching_readback"]=dict(
        raw_original_control_call_count=len(calls),original_query_count=len(domain["queries"]),
        matched_query_count=len(matched),all_original_calls_retained=True,
        no_control_values_recomputed=True,no_observer_call_discarded=True,
        total_calls_not_required_equal_queries=True,queries=readback)
    return result


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
    require(len(domain["queries"])==GROUPS
        and len(domain["angular_return_indices"])==GROUPS,"All base37 query and angular returns")
    domain=match_original_query_controls(domain,packets,np)
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
        tag=report.get("R354_read_only_capture") if isinstance(report,dict) else None
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

BITS=320
SCALE=1 << BITS
PHYSICAL_SOURCE="geometry_20261114_r225_free_core_bvp.py"
PHYSICAL_SHA="a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08"
AUGMENTED_SOURCE="geometry_20261114_full_dn_augmented.py"
AUGMENTED_SHA="f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e"
PROOF_NAME="R354-full-Frenet-velocity-and-closed-step-Hermite-remainders.md"
PREFIX_N=338
FULL_N=453
MEAN_ROWS=(0,225)


def floor_scaled(n,e):
    return n << e if e>=0 else n // (1 << (-e))


def ceil_scaled(n,e):
    return n << e if e>=0 else -((-n) // (1 << (-e)))


class Interval:
    """Closed [lo,hi]*2^-320 with outward integer arithmetic."""
    __slots__=("lo","hi")

    def __init__(self,lo,hi=None):
        self.lo=int(lo);self.hi=self.lo if hi is None else int(hi)
        require(self.lo<=self.hi,"Ordered outward interval")

    @staticmethod
    def integer(n):return Interval(int(n)*SCALE)

    @staticmethod
    def rational(n,d=1):
        n=int(n);d=int(d)
        require(d>0,"Positive exact rational denominator")
        return Interval(n*SCALE//d,-((-n*SCALE)//d))

    @staticmethod
    def dyadic(value):
        n,e=value
        return Interval(floor_scaled(n,e+BITS),ceil_scaled(n,e+BITS))

    @staticmethod
    def floating(value):return Interval.dyadic(dyadic(value))

    def __add__(self,other):
        if isinstance(other,int):other=Interval.integer(other)
        return Interval(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__

    def __neg__(self):return Interval(-self.hi,-self.lo)

    def __sub__(self,other):return self+(-other)
    def __rsub__(self,other):return -self+other

    def __mul__(self,other):
        if isinstance(other,int):
            values=(self.lo*other,self.hi*other)
            return Interval(min(values),max(values))
        values=(self.lo*other.lo,self.lo*other.hi,self.hi*other.lo,self.hi*other.hi)
        return Interval(min(values)//SCALE,-((-max(values))//SCALE))
    __rmul__=__mul__

    def __truediv__(self,other):
        if isinstance(other,int):other=Interval.integer(other)
        if other.lo<=0<=other.hi:raise ArithmeticError("Interval denominator contains zero")
        values=[(x*SCALE,y) for x in (self.lo,self.hi) for y in (other.lo,other.hi)]
        lower=min(n//d for n,d in values)
        upper=max(-((-n)//d) for n,d in values)
        return Interval(lower,upper)

    def square(self):
        a,b=self.lo,self.hi
        low=0 if a<=0<=b else min(a*a,b*b)
        high=max(a*a,b*b)
        return Interval(low//SCALE,-((-high)//SCALE))

    def sqrt(self):
        if self.lo<0:raise ArithmeticError("Square root lower endpoint negative")
        low=math.isqrt(self.lo*SCALE)
        high=math.isqrt(self.hi*SCALE)
        if high*high<self.hi*SCALE:high+=1
        return Interval(low,high)

    def power(self,n):
        require(isinstance(n,int) and n>=0,"Nonnegative integer interval power")
        result=Interval.integer(1)
        for _ in range(n):result=result*self
        return result

    def absolute_upper(self):return max(abs(self.lo),abs(self.hi))
    def hull(self,other):return Interval(min(self.lo,other.lo),max(self.hi,other.hi))

    def intersect(self,other):
        lo=max(self.lo,other.lo);hi=min(self.hi,other.hi)
        require(lo<=hi,"Two sound enclosures of the same exact quantity intersect")
        return Interval(lo,hi)

    def record(self):
        return dict(lower_integer_hex=integer_hex(self.lo),
            upper_integer_hex=integer_hex(self.hi),binary_exponent=-BITS)


IZERO=Interval(0)


def upper_record(value):
    return dict(nonnegative_integer_hex=integer_hex(value),binary_exponent=-BITS)


def p_add(a,b,sign=1):
    out=list(a)+[IZERO]*max(0,len(b)-len(a))
    for i,value in enumerate(b):out[i]=out[i]+value*sign
    return out


def p_mul(a,b):
    out=[IZERO]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
    return out


def p_derivative(a):
    return [a[i]*i for i in range(1,len(a))] or [IZERO]


def p_value(a,x):
    value=IZERO
    for coefficient in reversed(a):value=value*x+coefficient
    return value


def p_bernstein(a,alpha):
    degree=len(a)-1
    powers=[Interval.integer(1)]
    for _ in range(degree):powers.append(powers[-1]*alpha)
    formed=[]
    for i in range(degree+1):
        value=IZERO
        for k in range(i+1):
            value=value+a[k]*powers[k]*Interval.rational(math.comb(i,k),math.comb(degree,k))
        formed.append(value)
    answer=formed[0]
    for value in formed[1:]:answer=answer.hull(value)
    # Both are full-coefficient enclosures; their intersection is sound.
    return answer.intersect(p_value(a,Interval(0,alpha.hi)))


def p_dot(a,b):
    answer=[IZERO]
    for left,right in zip(a,b):answer=p_add(answer,p_mul(left,right))
    return answer


def p_cross(a,b):
    return [p_add(p_mul(a[i],b[j]),p_mul(a[j],b[i]),-1)
        for i,j in ((1,2),(2,0),(0,1))]


def angle_polynomials(d0,d1,e0,e1,scalar0,scalar1):
    d=[[d0[i],d1[i]] for i in range(3)]
    e=[[e0[i],e1[i]] for i in range(3)]
    a=[scalar0[0],scalar1[0]];nu=[scalar0[1],scalar1[1]]
    Q=p_dot(d,d);S=p_dot(d,e);C=p_cross(d,e);W=p_dot(C,C)
    B=[p_add(p_mul(Q,e[i]),p_mul(S,d[i]),-1) for i in range(3)]
    T=[p_mul(p_mul(nu,Q),part) for part in B]
    D=p_mul(a,W)
    P=p_add(p_mul(p_mul(a,a),W),p_mul(p_mul(nu,nu),p_mul(p_mul(Q,Q),Q)),-1)
    P=P+[IZERO]*(9-len(P))
    require(len(P)==9 and len(D)==6 and all(len(part)==7 for part in T),
        "Retain every degree-eight P, degree-five D and degree-six T coefficient")
    return dict(a=a,nu=nu,Q=Q,S=S,C=C,W=W,B=B,T=T,D=D,P=P)


def evaluate_velocity(poly,alpha,derivative=False):
    a=p_value(poly["a"],alpha);nu=p_value(poly["nu"],alpha)
    P=p_value(poly["P"],alpha);D=p_value(poly["D"],alpha)
    if a.lo<=0 or P.lo<=0:
        return None,dict(reason="accurate-reference-positive-square-root-domain-unresolved",
            a=a.record(),nu=nu.record(),P=P.record(),
            accurately_refuted=a.hi<=0 or P.hi<=0)
    # D=aW >= P/a, even if direct interval dependence obscures its sign.
    positive=(Interval(P.lo)/Interval(a.hi)).lo
    D=D.intersect(Interval(max(D.lo,positive),D.hi))
    if D.lo<=0:
        return None,dict(reason="outward-denominator-grid-cannot-isolate-positive-D",
            a=a.record(),P=P.record(),D=D.record(),accurately_refuted=False)
    K=P.sqrt()
    C=[p_value(v,alpha) for v in poly["C"]]
    T=[p_value(v,alpha) for v in poly["T"]]
    U=[K*c-t for c,t in zip(C,T)]
    value=[v/D for v in U]
    result=dict(value=value,scalar_domain=(nu.lo>-SCALE and nu.hi<SCALE),
        a=a,nu=nu,P=P,D=D)
    if derivative:
        P1=p_value(p_derivative(poly["P"]),alpha)
        D1=p_value(p_derivative(poly["D"]),alpha)
        C1=[p_value(p_derivative(v),alpha) for v in poly["C"]]
        T1=[p_value(p_derivative(v),alpha) for v in poly["T"]]
        K1=P1/(2*K)
        U1=[K1*c+K*c1-t1 for c,c1,t1 in zip(C,C1,T1)]
        result["first"]=[u1/D-u*D1/D.square() for u,u1 in zip(U,U1)]
    return result,None


def closed_second_bound(poly,alpha):
    a=p_bernstein(poly["a"],alpha);nu=p_bernstein(poly["nu"],alpha)
    P=p_bernstein(poly["P"],alpha);D=p_bernstein(poly["D"],alpha)
    aend=p_value(poly["a"],alpha);nuend=p_value(poly["nu"],alpha)
    Pend=p_value(poly["P"],alpha)
    refuted=(aend.hi<=0 or Pend.hi<=0 or nuend.lo>=SCALE or nuend.hi<=-SCALE)
    if not (a.lo>0 and P.lo>0 and nu.lo>-SCALE and nu.hi<SCALE):
        return None,dict(reason="closed-accurate-endpoint-domain-not-proved",
            accurate_endpoint_refuted=refuted,a=a.record(),nu=nu.record(),P=P.record(),
            a_endpoint=aend.record(),nu_endpoint=nuend.record(),P_endpoint=Pend.record())
    dmin=max(D.lo,(Interval(P.lo)/Interval(a.hi)).lo)
    if dmin<=0:
        return None,dict(reason="closed-positive-denominator-grid-unresolved",
            accurate_endpoint_refuted=False,D=D.record())
    def derivative_magnitudes(coeffs):
        return [p_bernstein(coeffs,alpha).absolute_upper(),
            p_bernstein(p_derivative(coeffs),alpha).absolute_upper(),
            p_bernstein(p_derivative(p_derivative(coeffs)),alpha).absolute_upper()]
    pc=derivative_magnitudes(poly["P"])
    dc=derivative_magnitudes(poly["D"])
    cc=[derivative_magnitudes(part) for part in poly["C"]]
    tc=[derivative_magnitudes(part) for part in poly["T"]]
    c=[Interval(max(row[i] for row in cc)) for i in range(3)]
    t=[Interval(max(row[i] for row in tc)) for i in range(3)]
    rootmin=Interval(P.lo).sqrt()
    k0=Interval(P.hi).sqrt()
    k1=Interval(pc[1])/(2*rootmin)
    k2=Interval(pc[2])/(2*rootmin)+Interval(pc[1]).square()/(4*rootmin.power(3))
    u0=k0*c[0]+t[0]
    u1=k1*c[0]+k0*c[1]+t[1]
    u2=k2*c[0]+2*k1*c[1]+k0*c[2]+t[2]
    lower=Interval(dmin);d1=Interval(dc[1]);d2=Interval(dc[2])
    bound=u2/lower+(2*u1*d1+u0*d2)/lower.square()+2*u0*d1.square()/lower.power(3)
    require(bound.hi>=0,"Nonnegative outward R354 second derivative bound")
    return bound.hi,dict(a_lower_integer_hex=integer_hex(a.lo),
        P_lower_integer_hex=integer_hex(P.lo),D_lower_integer_hex=integer_hex(dmin),
        binary_exponent=-BITS,complete_P_coefficients=9,
        source_of_bound="R354.14 full polynomial Bernstein and outward interval operations")

class TrigonometricTable:
    """True rational multiples of pi, never np.pi or literal FFT twiddles."""
    def __init__(self,arb,fmpq,ctx,budget):
        ctx.prec=BITS+64
        self.arb=arb;self.fmpq=fmpq;self.cache={};self.budget=budget
        self.digest=hashlib.sha256()

    def pair(self,frequency,angle):
        residue=(2*int(frequency)*int(angle))%(2*ANGLES)
        if residue not in self.cache:
            self.budget.check(phase="outward-accurate-uniform-trigonometric-table")
            sin,cos=self.arb.sin_cos_pi_fmpq(self.fmpq(residue,ANGLES))
            values=[]
            for value in (sin,cos):
                require(value.is_finite(),"Arb trigonometric enclosure must be finite")
                low=value.lower().man_exp();high=value.upper().man_exp()
                values.append(Interval(floor_scaled(int(low[0]),int(low[1])+BITS),
                    ceil_scaled(int(high[0]),int(high[1])+BITS)))
            self.cache[residue]=tuple(values)
            self.digest.update(canonical(dict(numerator=residue,denominator=ANGLES,
                sine=values[0].record(),cosine=values[1].record())))
        return self.cache[residue]

    def row(self,angle):
        return [self.pair(frequency,angle) for frequency in range(2,225,2)]

    def identity(self):
        return dict(accurate_angle_definition="theta_n = 2*pi*n/2048, n=0..2047",
            frequencies=list(range(0,225,2)),real_Arb_bits=BITS+64,
            outward_integer_grid_bits=BITS,distinct_actual_rational_arguments=len(self.cache),
            complete_created_table_records_sha256=self.digest.hexdigest(),
            source="Arb sin_cos_pi_fmpq of exact rational arguments",
            literal_original_FFT_twiddle_identity_claimed=False)


def synthesis_signals(physical):
    """Six exact coefficient rows for the full rotating d/e, no mode dropped."""
    require(len(physical)==338,"Complete physical338 coefficient vector")
    r=[dyadic(x) for x in physical[:113]]
    t=[ZERO]+[dyadic(x) for x in physical[113:225]]
    z=[dyadic(x) for x in physical[225:]]
    coefficients=[[],[],[],[],[],[]]
    for k in range(1,113):
        f=2*k
        coefficients[0].append(add(mul(r[k],(-f,0)),neg(t[k])))
        coefficients[1].append(add(mul(t[k],(f,0)),r[k]))
        coefficients[2].append(mul(z[k],(-f,0)))
        coefficients[3].append(add(mul(r[k],(-(f*f+1),0)),mul(t[k],(-2*f,0))))
        coefficients[4].append(add(mul(t[k],(-(f*f+1),0)),mul(r[k],(-2*f,0))))
        coefficients[5].append(mul(z[k],(-f*f,0)))
    constants=(ZERO,r[0],ZERO,neg(r[0]),ZERO,ZERO)
    rows=[]
    for signal,(constant,coeffs) in enumerate(zip(constants,coefficients)):
        exponent=min((v[1] for v in [constant]+coeffs if v[0]),default=0)
        ints=[(v[0]<<(v[1]-exponent)) if v[0] else 0 for v in coeffs]
        initial=(constant[0]<<(constant[1]-exponent)) if constant[0] else 0
        rows.append((signal in (0,2,4),initial,ints,exponent))
    return rows


def synthesize(signals,trig):
    answer=[]
    for sine,constant,coefficients,exponent in signals:
        lo=hi=constant*SCALE
        for coefficient,pair in zip(coefficients,trig):
            value=pair[0 if sine else 1]
            first=coefficient*value.lo;second=coefficient*value.hi
            lo+=min(first,second);hi+=max(first,second)
        answer.append(Interval(floor_scaled(lo,exponent),ceil_scaled(hi,exponent)))
    return answer[:3],answer[3:]


def product_integer_bounds(a,b):
    values=(a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi)
    return min(values),max(values)


class CompleteProjection:
    """All338 rows and both means; exact sums of outward product endpoints."""
    def __init__(self):
        self.low=[0]*338;self.high=[0]*338;self.angles=0

    def add(self,value,trig):
        for row,component in ((0,0),(225,2)):
            self.low[row]+=value[component].lo*SCALE
            self.high[row]+=value[component].hi*SCALE
        # rfft uses exp(-i*theta); its negative imaginary part is +sin projection.
        for k,(sine,cosine) in enumerate(trig,1):
            for row,component,weight in ((k,0,cosine),(112+k,1,sine),(225+k,2,cosine)):
                low,high=product_integer_bounds(value[component],weight)
                self.low[row]+=low;self.high[row]+=high
        self.angles+=1

    def finish(self):
        require(self.angles==ANGLES,"Do not call a partial angular projection complete")
        result=[]
        for row in range(338):
            factor=1 if row in MEAN_ROWS else 2
            denominator=ANGLES*SCALE
            result.append(Interval(self.low[row]*factor//denominator,
                -((-self.high[row]*factor)//denominator)))
        return result+[IZERO]*115


def interval_vector_summary(values):
    require(len(values)==453,"Keep full453 augmented rows in a vector summary")
    index=max(range(453),key=lambda i:values[i].absolute_upper())
    physical=max(range(338),key=lambda i:values[i].absolute_upper())
    constants=max(range(338,453),key=lambda i:values[i].absolute_upper())
    return dict(complete_rows=453,physical_rows=338,constant_RHS_rows=115,
        maximum_absolute_upper=upper_record(values[index].absolute_upper()),
        maximum_absolute_upper_row=index,interval_at_maximum=values[index].record(),
        physical_maximum_absolute_upper=upper_record(values[physical].absolute_upper()),
        physical_maximum_row=physical,
        constant_row_maximum_absolute_upper=upper_record(values[constants].absolute_upper()),
        constant_maximum_row=constants,
        complete_two_mean_rows={str(i):values[i].record() for i in MEAN_ROWS})


def exact_vector_summary(values):
    require(len(values)==453,"Complete exact dyadic453 rows")
    index=max(range(453),key=lambda i:(abs(values[i][0]).bit_length()+values[i][1]
        if values[i][0] else -100000))
    # The above candidate exponent is not enough for a maximum. Compare exact values.
    for i in range(453):
        if compare(absolute(values[i]),absolute(values[index]))>0:index=i
    nonzero=[]
    for i,v in enumerate(values):
        if v[0]:ranges_add(nonzero,i)
    return dict(complete_rows=453,maximum_absolute=packed(absolute(values[index])),
        maximum_row=index,exact_nonzero_row_ranges=nonzero,
        complete_two_mean_rows={str(i):packed(values[i]) for i in MEAN_ROWS})


def original_direction(base,words,np):
    coefficients=words["coefficient_direction"]
    physical_size=698*338
    physical=coefficients[:physical_size].reshape(698,338)
    core=coefficients[physical_size:physical_size+109]
    parameters=coefficients[physical_size+109:]
    require(core.shape==(109,) and parameters.shape==(3,),"All external core and controls retained")
    direction=np.zeros((699,453),dtype=np.float64)
    direction[1:,:338]=physical
    direction[0,:338]=base["inlet"]@core
    direction[:,341:450]=core
    direction[:,450:453]=parameters
    require(np.all(np.isfinite(direction)),"Finite full physical coefficient-direction lift")
    return direction,parameters


def bind_endpoint_variants(domain,base,direction,packets,np,budget):
    observations=domain.get("endpoint_scalar_cache_observations")
    require(isinstance(observations,list),"Actual captured endpoint scalar caches are required")
    actual_calls=domain["capture_description"]["captured_original_calls"]
    require(len(observations)==len(actual_calls),"Every actually captured A chunk retained")
    by_call={};variants=[];indices={};query_variants=[]
    for observation,call in zip(observations,actual_calls):
        number=call["call_number"]
        require(observation["original_A_call_number"]==number
            and observation["original_station_identity"]==call["stations"]
            and observation["original_station_count"]==call["station_count"]
            and observation["original_selected_intervals"]==call["selected_intervals"]
            and observation["copied_existing_cache_without_any_new_scientific_call"] is True,
            "Each original A chunk's complete scalar-cache identity is explicit")
        saved=packets.get(observation["packet"])
        compare_old_identity(saved["stations"],call["stations"])
        require(saved["stations"].shape==(call["station_count"],)
            and saved["baseline"].shape==(call["station_count"],3)
            and saved["controls"].shape==(call["station_count"],3,3),
            "Full scalar cache dimensions")
        require(all(np.all(np.isfinite(saved[k])) for k in saved),"Finite literal cache input")
        require(number not in by_call,"Unique original A call number")
        require(observation["original_scalar_jets_function_identity"]["source_sha256"]==AUGMENTED_SHA,
            "The literal cache comes from the original complete augmented scalar_jets")
        by_call[number]=(observation,saved)
    for q,query in enumerate(domain["queries"]):
        budget.check(phase="bind-all-original-endpoint-variants",query_index=q)
        number=query["endpoint_original_call_number"]
        require(query["endpoint_scalar_original_call_number"]==number and number in by_call,
            "Do not cross a physical J/P chunk with another scalar coefficient chunk")
        observation,saved=by_call[number]
        pos=observation["endpoint_positions"][str(query["interval"])]
        matrices=packets.get(query["packet"]);used=[]
        for side,node in (("left",query["interval"]),("right",query["interval"]+1)):
            k=pos[side];J=matrices[side+"_J"];P=matrices[side+"_P"]
            require(J.shape==(338,338) and P.shape==(338,3),"All original J/P input columns")
            compare_old_identity(J,query["endpoint_original_identities"][side]["physical"])
            compare_old_identity(P,query["endpoint_original_identities"][side]["parameter"])
            require(word(saved["stations"][k])==word(base["mesh"][node]),
                "Literal chunk station and original endpoint station are the same word")
            baseline=np.ascontiguousarray(saved["baseline"][k])
            control=np.ascontiguousarray(saved["controls"][k])
            identity=dict(node=node,station_float64le=word(base["mesh"][node]),
                original_J=old_array_identity(J),original_P=old_array_identity(P),
                original_base_jets=np_identity(baseline),original_control_jets=np_identity(control))
            key=sha(canonical(identity))
            origin=dict(query_index=q,side=side,original_A_call_number=number,
                original_cache_packet=observation["packet"],position_in_original_chunk=k)
            if key not in indices:
                index=len(variants);indices[key]=index
                scalar0=[];scalar1=[]
                for jet in range(3):
                    scalar0.append(add(dyadic(baseline[jet]),total(
                        mul(dyadic(control[jet,k0]),dyadic(base["y"][node,450+k0]))
                        for k0 in range(3))))
                    scalar1.append(total(mul(dyadic(control[jet,k0]),
                        dyadic(direction[node,450+k0])) for k0 in range(3)))
                variants.append(dict(index=index,identity=identity,
                    identity_sha256=key,origins=[origin],node=node,J=J,P=P,
                    baseline=baseline,controls=control,
                    scalar0_exact=scalar0,scalar1_exact=scalar1,
                    scalar0=[Interval.dyadic(v) for v in scalar0],
                    scalar1=[Interval.dyadic(v) for v in scalar1],
                    signals0=synthesis_signals(base["y"][node,:338]),
                    signals1=synthesis_signals(direction[node,:338]),
                    reference=None,closed=None,partial_phase=None))
            else:
                index=indices[key];variants[index]["origins"].append(origin)
            used.append(index)
        query_variants.append(tuple(used))
    require(len(query_variants)==37,"Both exact chunk-bound endpoints for all37 queries")
    return variants,query_variants


def form_declared_references(domain,base,direction,variants,query_variants,packets,np,
        budget,out,ledger,result):
    for variant in variants:
        budget.check(phase="exact-literal-JP-action",endpoint_variant=variant["index"])
        node=variant["node"];J=variant["J"];P=variant["P"]
        exact=exact_action(J,P,direction[node,:338],direction[node,450:453],budget)+[ZERO]*115
        formed=np.zeros(453,dtype=np.float64)
        formed[:338]=J@direction[node,:338]+P@direction[node,450:453]
        require(np.all(np.isfinite(formed)),"New post-model formed action is finite")
        delta=[sub(dyadic(x),y) for x,y in zip(formed,exact)]
        variant["ell_exact"]=exact;variant["ell_formed"]=formed
        ledger.write(dict(kind="complete-original-JP-word-action",
            endpoint_variant=variant["index"],identity=variant["identity"],
            exact_action=[packed(v) for v in exact],
            post_model_formed_action_words=[word(v) for v in formed],
            formed_minus_exact=[packed(v) for v in delta]))
        result["exact_JP_actions"].append(dict(endpoint_variant=variant["index"],
            complete_physical_columns=338,complete_parameter_columns=3,
            complete_augmented_rows=453,formed_minus_exact=exact_vector_summary(delta),
            formed_action_is_new_post_model_arithmetic_not_original_return=True))
    query_state=[]
    for q,query in enumerate(domain["queries"]):
        budget.check(phase="full453-Hermite-formation-defects",query_index=q)
        left,right=(variants[i] for i in query_variants[q])
        i=query["interval"];packet=packets.get(query["packet"]);q0=packet["query"]
        require(q0.shape==(453,) and np.all(np.isfinite(q0)),"Complete literal original query")
        h=unword(query["h_float64le"])
        weights=[unword(v) for v in query["hermite_weights_float64le"]]
        if query["kind"]=="collocation-midpoint":
            q1=.5*(direction[i]+direction[i+1])-h*(right["ell_formed"]-left["ell_formed"])/8
        else:
            q1=(weights[0]*direction[i]+h*weights[1]*left["ell_formed"]+
                weights[2]*direction[i+1]+h*weights[3]*right["ell_formed"])
        require(q1.shape==(453,) and np.all(np.isfinite(q1)),"All post-model query direction words")
        wd=[dyadic(x) for x in weights];hd=dyadic(h)
        delta0=[];delta1=[]
        for row in range(453):
            delta0.append(sub(hermite(wd,hd,dyadic(base["y"][i,row]),
                dyadic(base["rhs"][i,row]),dyadic(base["y"][i+1,row]),
                dyadic(base["rhs"][i+1,row])),dyadic(q0[row])))
            delta1.append(sub(hermite(wd,hd,dyadic(direction[i,row]),
                left["ell_exact"][row],dyadic(direction[i+1,row]),
                right["ell_exact"][row]),dyadic(q1[row])))
        original=save_words(out/("query-reference-"+str(q).zfill(2)+".npz"),np,
            original_query=q0,post_model_formed_query_direction=q1)
        ledger.write(dict(kind="complete453-Hermite-literal-formation-defects",
            query_index=q,kind_of_query=query["kind"],interval=i,endpoint_variants=list(query_variants[q]),
            weights_float64le=query["hermite_weights_float64le"],h_float64le=query["h_float64le"],
            delta_H0=[packed(v) for v in delta0],delta_H1=[packed(v) for v in delta1],
            declared_affine_words=original))
        query_state.append(dict(q0=q0,q1=q1,delta0=delta0,delta1=delta1,h=hd,weights=wd))
        result["Hermite_formation"].append(dict(query_index=q,kind=query["kind"],
            interval=i,endpoint_variants=list(query_variants[q]),reference_words=original,
            delta_H0=exact_vector_summary(delta0),delta_H1=exact_vector_summary(delta1),
            original_q0=True,q1_new_post_model_formed_words=True,
            exact_literal_JP_reference_not_original_floating_matvec=True,
            full453_rows_complete=True))
    return query_state

def decode_interval(record):
    require(record.get("binary_exponent")==-BITS,"Exact fixed-grid interval record")
    return Interval(int(record["lower_integer_hex"],16),int(record["upper_integer_hex"],16))


def close_ledger(ledger):
    if not hasattr(ledger,"closed_receipt"):ledger.closed_receipt=ledger.close()
    return ledger.closed_receipt


def reference_endpoint(variant,base,trig,budget,angle_ledger,vector_ledger,summary):
    projection=CompleteProjection();derivative=CompleteProjection()
    summary.update(processed_angle_count=0,regular_reference_angle_count=0,
        accurate_scalar_domain_proved=(variant["scalar0"][0].lo>0 and
            variant["scalar0"][1].lo>-SCALE and variant["scalar0"][1].hi<SCALE),
        unresolved_angle_ranges=[],
        accurately_refuted_angle_ranges=[],complete_finite_projection=False)
    for angle in range(ANGLES):
        budget.check(phase="accurate-full338-endpoint-RHS-and-first-direction",
            endpoint_variant=variant["index"],node=variant["node"],angle_index=angle)
        table=trig.row(angle)
        d0,e0=synthesize(variant["signals0"],table)
        d1,e1=synthesize(variant["signals1"],table)
        poly=angle_polynomials(d0,d1,e0,e1,variant["scalar0"],variant["scalar1"])
        value,error=evaluate_velocity(poly,IZERO,derivative=True)
        # This small full-angle input permits later bounds without repeating
        # the original RHS/J, or repeating the accurate Fourier synthesis.
        record=dict(kind="accurate-full-endpoint-angle-input",endpoint_variant=variant["index"],
            node=variant["node"],angle_index=angle,
            d0=[v.record() for v in d0],d1=[v.record() for v in d1],
            e0=[v.record() for v in e0],e1=[v.record() for v in e1],
            point_reference_domain_unresolved=error)
        angle_ledger.write(record)
        if value is None:
            ranges_add(summary["unresolved_angle_ranges"],angle)
            if error.get("accurately_refuted"):ranges_add(summary["accurately_refuted_angle_ranges"],angle)
            vector_ledger.write(dict(kind="accurate-endpoint-base-domain-unresolved",
                endpoint_variant=variant["index"],angle_index=angle,details=error))
        else:
            projection.add(value["value"],table);derivative.add(value["first"],table)
            summary["regular_reference_angle_count"]+=1
            if not value["scalar_domain"]:summary["accurate_scalar_domain_proved"]=False
        summary["processed_angle_count"]+=1
    summary["angle_input_ledger"]=close_ledger(angle_ledger)
    if summary["regular_reference_angle_count"]==ANGLES:
        f0=projection.finish();f1=derivative.finish()
        node=variant["node"]
        e0=[v-Interval.floating(w) for v,w in zip(f0,base["rhs"][node])]
        e1=[v-Interval.dyadic(w) for v,w in zip(f1,variant["ell_exact"])]
        variant["reference"]=dict(f0=f0,f1=f1,e0=e0,e1=e1)
        vector_ledger.write(dict(kind="complete453-accurate-endpoint-reference",
            endpoint_variant=variant["index"],node=node,
            fstar0=[v.record() for v in f0],fstar_first0=[v.record() for v in f1],
            e0=[v.record() for v in e0],e1=[v.record() for v in e1],
            exact_literal_JP_reference=[packed(v) for v in variant["ell_exact"]],
            original_RHS_words=[word(v) for v in base["rhs"][node]]))
        summary.update(complete_finite_projection=True,
            accurate_fstar0=interval_vector_summary(f0),
            accurate_fstar_first0=interval_vector_summary(f1),
            e0_accurate_minus_original_returned_RHS=interval_vector_summary(e0),
            e1_accurate_minus_exact_original_JP_word_action=interval_vector_summary(e1),
            two_means_retained=True,all115_constant_RHS_rows_exact_zero=True)
    else:
        summary["complete_finite_projection_unavailable_reason"]=(
            "At least one accurate positive-root angle was not enclosed; no missing angular contribution is replaced by zero")


def fresh_closed_stats(index):
    return dict(trial_index=index,alpha_float64le=word(2.0**(-index)),
        complete_angle_rows=0,strict_regular_count=0,accurate_endpoint_refuted_count=0,
        unresolved_angle_ranges=[],accurate_endpoint_refuted_angle_ranges=[],_M=0)


def closed_endpoint(variant,summary,budget,ledger,angle_root):
    stats=[fresh_closed_stats(j) for j in range(17)]
    variant["closed"]=stats
    saved=summary.get("angle_input_ledger")
    if summary.get("processed_angle_count")!=ANGLES or saved is None:
        return
    path=angle_root/saved["file"]
    require(path.stat().st_size==saved["bytes"] and file_sha(path)==saved["sha256"],
        "Complete generated angle-input ledger identity before reuse")
    with gzip.open(path,"rt",encoding="ascii") as stream:
        count=0
        for angle,line in enumerate(stream):
            budget.check(phase="R354-all17-closed-endpoint-bounds",
                endpoint_variant=variant["index"],node=variant["node"],angle_index=angle)
            require(angle<ANGLES,"No extra angle-input record")
            row=json.loads(line)
            require(row["endpoint_variant"]==variant["index"] and row["angle_index"]==angle
                and row["node"]==variant["node"],"Complete original endpoint/angle ordering")
            vectors=[[decode_interval(v) for v in row[name]] for name in ("d0","d1","e0","e1")]
            require(all(len(v)==3 for v in vectors),"Full rotating vectors")
            poly=angle_polynomials(*vectors,variant["scalar0"],variant["scalar1"])
            values=[]
            for j in range(17):
                budget.check(trial_index=j)
                alpha=Interval.rational(1,1<<j)
                bound,details=closed_second_bound(poly,alpha)
                values.append(dict(trial_index=j,closed_regular_bound_available=bound is not None,
                    second_derivative_upper=None if bound is None else upper_record(bound),
                    bound_details=details))
            # Atomically retain the whole17-row outcome before advancing counts.
            ledger.write(dict(kind="complete17-closed-endpoint-angle",
                endpoint_variant=variant["index"],node=variant["node"],angle_index=angle,
                all_nine_P_coefficient_enclosures=[v.record() for v in poly["P"]],
                complete_alpha_results=values))
            for state,value in zip(stats,values):
                state["complete_angle_rows"]+=1
                if value["closed_regular_bound_available"]:
                    state["strict_regular_count"]+=1
                    state["_M"]=max(state["_M"],int(
                        value["second_derivative_upper"]["nonnegative_integer_hex"],16))
                else:
                    ranges_add(state["unresolved_angle_ranges"],angle)
                    if value["bound_details"].get("accurate_endpoint_refuted"):
                        state["accurate_endpoint_refuted_count"]+=1
                        ranges_add(state["accurate_endpoint_refuted_angle_ranges"],angle)
            count+=1
        require(count==ANGLES,"Complete generated angle-input ledger has all2048 rows")


def rendered_closed_stats(variant):
    answer=[]
    for row in variant.get("closed") or [fresh_closed_stats(j) for j in range(17)]:
        out={k:v for k,v in row.items() if not k.startswith("_")}
        complete=row["complete_angle_rows"]==ANGLES
        proved=complete and row["strict_regular_count"]==ANGLES
        out.update(all2048_rows_processed=complete,
            full_accurate_endpoint_closed_domain_proved=proved,
            unvisited_angle_ranges=[] if complete else [[row["complete_angle_rows"],ANGLES-1]],
            complete338_RHS_second_bound_available=proved,
            uniform_physical_nonmean_second_upper=upper_record(2*row["_M"]) if proved else None,
            each_of_two_mean_second_upper=upper_record(row["_M"]) if proved else None,
            constant115_second_derivatives_exact_zero=True,
            missing_angles_not_bounded_by_processed_maximum=not proved)
        answer.append(out)
    return answer


def endpoint_E(variant,index):
    # This interval encloses E at alpha_j only; M and its domain cover [0,alpha_j].
    if variant.get("reference") is None or variant.get("closed") is None:return None
    state=variant["closed"][index]
    if state["complete_angle_rows"]!=ANGLES or state["strict_regular_count"]!=ANGLES:return None
    alpha=Interval.rational(1,1<<index);quadratic=alpha.square()/2
    values=[]
    for row in range(453):
        bound=(state["_M"] if row in MEAN_ROWS else 2*state["_M"]) if row<338 else 0
        remainder=quadratic*Interval(-bound,bound)
        values.append(variant["reference"]["e0"][row]+alpha*variant["reference"]["e1"][row]+remainder)
    return values


def transfer_Hermite(domain,query_state,variants,query_variants,angular,slots,packets,
        np,budget,ledger,result):
    for q,query in enumerate(domain["queries"]):
        budget.check(phase="R354-complete453-Hermite-transfer",query_index=q)
        item=query_state[q];left,right=(variants[i] for i in query_variants[q])
        for j in range(17):
            budget.check(trial_index=j)
            alpha=Interval.rational(1,1<<j);El=endpoint_E(left,j);Er=endpoint_E(right,j)
            record=dict(query_index=q,kind=query["kind"],interval=query["interval"],
                trial_index=j,alpha_float64le=word(2.0**(-j)),
                original_trial_visited=slots[j]["original_trial_visited"],
                original_nonlinear_query_return_exists=False,
                accurate_reference_pointwise_Hermite_bound_available=False,
                entire_original_IEEE_query_execution_error_enclosed=False,
                all75776_original_query_domain_rows_certified=False)
            if El is None or Er is None:
                record["unresolved_endpoint_variants"]=[v["index"] for v,E in ((left,El),(right,Er)) if E is None]
                record["reason"]="a full endpoint reference or its all2048 closed bound is not available"
                result["Hermite_transfer"].append(record)
                continue
            h=Interval.dyadic(item["h"]);wl=Interval.dyadic(item["weights"][1])
            wr=Interval.dyadic(item["weights"][3])
            gap=[Interval.dyadic(item["delta0"][row])+alpha*Interval.dyadic(item["delta1"][row])+
                h*(wl*El[row]+wr*Er[row]) for row in range(453)]
            detail=dict(kind="full453-accurate-Hermite-gap-enclosure",query_index=q,
                trial_index=j,endpoint_variants=list(query_variants[q]),
                gap_relative_to_literal_q0_plus_alpha_q1=[v.record() for v in gap])
            record.update(accurate_reference_pointwise_Hermite_bound_available=True,
                full453_gap=interval_vector_summary(gap),
                formula="R354.21 with e0/e1 and exact literal Hermite formation defects",
                original_query_word_direction_is_declared_post_model_reference=True)
            mapping=slots[j].get("angular_by_query",{})
            actual_index=mapping.get(q)
            if actual_index is not None:
                actual=packets.get(angular[actual_index]["packet"])
                aq=actual["query"]
                require(aq.shape==(453,),"Original complete nonlinear query return")
                record["original_nonlinear_query_return_exists"]=True
                if np.all(np.isfinite(aq)):
                    # A pointwise outward eta interval follows by subtracting
                    # the declared accurate-reference enclosure from actual words.
                    # This is not an enclosure of the IEEE program at other alpha.
                    affine=[Interval.floating(item["q0"][row])+alpha*Interval.floating(item["q1"][row])
                        for row in range(453)]
                    eta=[Interval.floating(aq[row])-affine[row]-gap[row] for row in range(453)]
                    detail["original_actual_query_words"]=[word(v) for v in aq]
                    detail["pointwise_eta_from_accurate_Hermite_bound"]=[v.record() for v in eta]
                    record["pointwise_execution_difference_enclosure"]=interval_vector_summary(eta)
                    record["pointwise_eta_enclosure_method"]="actual word minus interval accurate Hermite reference"
                    record["eta_is_not_directly_recomputed_IEEE_error_or_a_whole_alpha_bound"]=True
                else:
                    record["pointwise_eta_unavailable_reason"]="original nonlinear query contains nonfinite words"
            ledger.write(detail)
            result["Hermite_transfer"].append(record)


def safe_write(path,value):
    raw=canonical(value)
    temporary=path.with_suffix(path.suffix+".writing")
    temporary.write_bytes(raw);temporary.replace(path)
    return dict(file=path.name,bytes=len(raw),sha256=sha(raw))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capture",type=Path,required=True)
    parser.add_argument("--model-directory",type=Path,required=True)
    parser.add_argument("--code-directory",type=Path,required=True)
    parser.add_argument("--seconds",type=int,default=5400)
    parser.add_argument("--max-ledger-bytes",type=int,default=8589934592)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS")=="true" and
        os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,"Only public Actions perform scientific arithmetic")
    require(args.seconds>0 and args.max_ledger_bytes>0,"Explicit independent diagnostic resources")
    budget=Budget(args.seconds)
    temporary=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    for p in (args.capture,args.model_directory,args.out):
        require(p.resolve().is_relative_to(temporary) and p.resolve()!=temporary and not p.is_symlink(),
            "All raw output remains in this actual job's temporary tree")
    require(not args.out.exists(),"Fresh independent diagnostic output")
    args.out.mkdir(parents=True);large=args.out/"large-arrays";large.mkdir()
    code=args.code_directory.resolve(strict=True)
    result=dict(schema=SCHEMA,request=170,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),source_commit=os.environ.get("GITHUB_SHA"),
        source_sha256=file_sha(__file__),proof_sha256=PROOF_SHA,post_model_scientific_arithmetic=True,
        scientific_completed=False,resource_partial=False,scientific_exception=None,
        complete_actual_input_binding_paid=False,
        original_model_and_FD_gates_not_changed=True,extra_original_RHS_J_QR_FD_or_trial_calls=0,
        declared_query_count=37,declared_angles_per_query=2048,declared_query_rows=75776,
        declared_augmented_state_dimension=453,declared_physical_rows=338,
        declared_constant_RHS_rows=115,declared_two_mean_rows=list(MEAN_ROWS),
        declared_alpha_count=17,outward_integer_grid_bits=BITS,Arb_trigonometric_bits=BITS+64,
        exact_JP_actions=[],Hermite_formation=[],endpoint_variants=[],
        Hermite_transfer=[],temporary_ledgers=[],original_trial_slots=[],
        scope=dict(
            accurate_uniform_finite_DFT_not_original_FFT_operation_order=True,
            scalar_reference_is_original_A_chunk_literal_b_plus_C_times_complete_parameters=True,
            original_ap_field_not_relabelled_as_derivative_of_another_profile=True,
            all338_plus112_plus3_retained=True,
            exact_original_JP_word_action_distinguished_from_new_floating_action=True,
            original_same_node_distinct_chunk_words_never_silently_merged=True,
            full_interval_original_IEEE_execution_error_enclosure_paid=False,
            complete_true_Hermite_query_angular_domain_transfer_paid=False,
            scalar_and_endpoint_bounds_not_original_trial_acceptance_gates=True,
            Hermite_gap_intervals_are_pointwise_at_declared_alpha=True,
            whole_alpha_uniform_Hermite_gap_enclosure_computed=False,
            no_full699_node698_midpoint_RMS_or_continuous_angle_certificate=True,
            no_native_fullDN_metric_or_user_goal_acceptance=True))
    ledgers=[];bank=[0];variants=[];query_variants=[];endpoint_summaries=[]
    slots=[];packets=None;trig=None;exit_code=2
    def external_stop(signum,frame):
        raise ResourceStop("external signal "+str(signum)+" interrupted the independent diagnostic")
    signal.signal(signal.SIGTERM,external_stop);signal.signal(signal.SIGINT,external_stop)
    try:
        for name,digest in ((CAPTURE_NAME,CAPTURE_SHA),(FFT_NAME,FFT_SHA),
                (PHYSICAL_SOURCE,PHYSICAL_SHA),(AUGMENTED_SOURCE,AUGMENTED_SHA)):
            require(file_sha(code/name)==digest,"Exact scientific source: "+name)
        proof=code.parent/"results"/PROOF_NAME
        require(file_sha(proof)==PROOF_SHA,"The actual published R354 proof bytes")
        import numpy as np
        import flint
        from flint import arb,fmpq,ctx
        result["runtime"]=dict(python=sys.version,numpy=np.__version__,
            python_flint=getattr(flint,"__version__",None),
            finite_reference_implementation="outward320 integer grid with Arb384 trigonometry")
        packets=Packets(args.capture,np)
        capture=read(args.capture/"capture.json")
        require(capture.get("run_id")==os.environ.get("GITHUB_RUN_ID") and
            capture.get("source_commit")==os.environ.get("GITHUB_SHA"),
            "The actual model capture belongs to this same job and fixed source checkout")
        model_path=args.model_directory/"model-000.json"
        model=read(model_path) if model_path.is_file() else None
        result["original_capture_manifest"]=receipt(args.capture/"capture.json")
        result["original_model_document"]=receipt(model_path) if model_path.is_file() else None
        result["original_model_accepted"]=(model or {}).get("accepted")
        result["original_model_exit_code"]=capture.get("original_model_exit_code")
        result["original_model_exception"]=capture.get("original_exception")
        result["original_observation_completed"]=capture.get("observation_complete")
        domain,choice,document,base,selected,words,angular,slots=bind(capture,packets,model,code,np)
        require(np.array_equal(base["q_frequency"],np.arange(0,225,2)),
            "All actual frequencies0,2,...224 retained in their original order")
        require(np.all(base["rhs"][:,338:]==0),"All original constant core/control RHS rows are zero")
        for key,digest in (("original_augmented",AUGMENTED_SHA),("original_physical",PHYSICAL_SHA)):
            require(capture[key]["sha256"]==digest,"Original finite RHS source binding")
        result["original_source_pair"]=dict(warm=capture["source_input_warm"],
            status=capture["source_parent_status"])
        result["actual_B_model_sha256"]=domain["B_model_sha256"]
        result["actual_final_chosen_direction"]=document
        result["original_source_bindings"]={key:capture[key] for key in
            ("original_producer","original_observer","original_domain","original_FFT",
             "original_engine","original_augmented","original_physical")}
        result["query_specs"]=capture["query_specs"]
        result["query_control_matching_readback"]=domain["query_control_matching_readback"]
        result["original_trial_slots"]=slots
        # The complete source/packet binding is temporary and hash identified.
        binding=dict(schema=SCHEMA,original_capture=capture,complete_original_domain=domain,
            final_choice=choice,original_direction=document,original_trial_slots=slots)
        binding_raw=canonical(binding);binding_path=large/"complete-input-binding.json.gz"
        binding_path.write_bytes(gzip.compress(binding_raw,compresslevel=1,mtime=0))
        result["complete_input_binding"]=dict(**receipt(binding_path),
            uncompressed_bytes=len(binding_raw),uncompressed_sha256=sha(binding_raw))
        for q,query in enumerate(domain["queries"]):
            data=packets.get(angular[domain["angular_return_indices"][q]]["packet"])
            qp=packets.get(query["packet"])
            require(data["query"].tobytes()==qp["query"].tobytes()
                and data["first"].shape==(2048,3) and data["second"].shape==(2048,3)
                and data["scalar"].shape==(3,) and data["beta"].shape==(2048,),
                "All actual base query angular words are retained and bound")
        direction,dp=original_direction(base,words,np)
        variants,query_variants=bind_endpoint_variants(domain,base,direction,packets,np,budget)
        for variant in variants:
            metadata=dict(endpoint_variant=variant["index"],node=variant["node"],
                identity=variant["identity"],identity_sha256=variant["identity_sha256"],
                all_identical_word_origins=variant["origins"],
                scalar_reference_intercept_exact=[packed(v) for v in variant["scalar0_exact"]],
                scalar_reference_direction_exact=[packed(v) for v in variant["scalar1_exact"]],
                identical_words_only_reused=True,processed_angle_count=0,
                complete_finite_projection=False)
            endpoint_summaries.append(metadata)
        result["complete_actual_input_binding_paid"]=True
        result["declared_actual_endpoint_variant_count"]=len(variants)
        result["declared_original_unique_endpoint_nodes"]=sorted({v["node"] for v in variants})
        result["endpoint_variants"]=endpoint_summaries
        result["query_endpoint_variant_indices"]=[list(v) for v in query_variants]
        formation=Ledger(large/"complete453-formation-and-JP-actions.jsonl.gz",
            args.max_ledger_bytes,bank);ledgers.append(formation)
        query_state=form_declared_references(domain,base,direction,variants,query_variants,
            packets,np,budget,large,formation,result)
        close_ledger(formation)
        vector_ledger=Ledger(large/"complete453-accurate-endpoint-vectors.jsonl.gz",
            args.max_ledger_bytes,bank);ledgers.append(vector_ledger)
        trig=TrigonometricTable(arb,fmpq,ctx,budget)
        for variant,summary in zip(variants,endpoint_summaries):
            budget.check(phase="accurate-full-endpoint-reference-start",endpoint_variant=variant["index"])
            angles=Ledger(large/("endpoint-"+str(variant["index"]).zfill(3)+"-angle-jets.jsonl.gz"),
                args.max_ledger_bytes,bank);ledgers.append(angles)
            try:
                reference_endpoint(variant,base,trig,budget,angles,vector_ledger,summary)
            finally:
                summary["angle_input_ledger"]=close_ledger(angles)
        close_ledger(vector_ledger)
        bounds=Ledger(large/"all17-closed-endpoint-angle-bounds.jsonl.gz",
            args.max_ledger_bytes,bank);ledgers.append(bounds)
        for variant,summary in zip(variants,endpoint_summaries):
            closed_endpoint(variant,summary,budget,bounds,large)
        close_ledger(bounds)
        transfer=Ledger(large/"all453-Hermite-reference-gap-and-pointwise-eta.jsonl.gz",
            args.max_ledger_bytes,bank);ledgers.append(transfer)
        transfer_Hermite(domain,query_state,variants,query_variants,angular,slots,
            packets,np,budget,transfer,result)
        close_ledger(transfer)
        result["scientific_completed"]=True
        result["stop_reason"]="all-declared-independent-computations-visited"
        exit_code=0 if all(v["accurate_reference_pointwise_Hermite_bound_available"]
            for v in result["Hermite_transfer"]) else 3
    except ResourceStop as error:
        result["resource_partial"]=True;result["stop_reason"]=str(error);exit_code=3
    except BaseException as error:
        result["scientific_exception"]=dict(type=type(error).__name__,message=str(error),
            traceback=traceback.format_exc())
        result["stop_reason"]="input-or-independent-program-error";exit_code=2
    finally:
        signal.signal(signal.SIGTERM,signal.SIG_IGN);signal.signal(signal.SIGINT,signal.SIG_IGN)
        for ledger in ledgers:
            try:result["temporary_ledgers"].append(close_ledger(ledger))
            except Exception as error:
                result.setdefault("readout_errors",[]).append(dict(type=type(error).__name__,message=str(error)))
        result["complete_ledger_values_are_not_all_reprinted_as_large_scientific_tables"]=True
        result["temporary_ledger_uncompressed_bytes"]=bank[0]
        paid_actions={v["endpoint_variant"] for v in result["exact_JP_actions"]}
        result["pending_complete_JP_action_variants"]=[dict(endpoint_variant=v["index"],
            complete_output_row_range=[0,452],physical_input_column_range=[0,337],
            parameter_input_column_range=[0,2]) for v in variants if v["index"] not in paid_actions]
        formed_queries={v["query_index"] for v in result["Hermite_formation"]}
        result["pending_complete_Hermite_formation_queries"]=[dict(query_index=q,
            augmented_component_range=[0,452]) for q in range(37) if q not in formed_queries]
        result["pending_reference_scopes"]=[]
        result["closed_endpoint_results"]=[]
        for variant,summary in zip(variants,endpoint_summaries):
            processed=summary.get("processed_angle_count",0)
            if processed<ANGLES:
                result["pending_reference_scopes"].append(dict(endpoint_variant=variant["index"],
                    node=variant["node"],angle_range=[processed,ANGLES-1],
                    full453_projection_unavailable_until_all_angles_defined=True))
            result["closed_endpoint_results"].append(dict(endpoint_variant=variant["index"],
                node=variant["node"],alpha_results=rendered_closed_stats(variant)))
        completed={(row["query_index"],row["trial_index"]) for row in result["Hermite_transfer"]}
        result["pending_Hermite_transfer_pairs"]=[dict(query_index=q,trial_index=j,
            augmented_component_range=[0,452]) for q in range(37) for j in range(17) if (q,j) not in completed]
        result["unavailable_original_trial_scopes"]=[dict(trial_index=s["trial_index"],
            original_trial_visited=s["original_trial_visited"],
            original_nonlinear_return_exists=s["nonlinear_return_exists"],
            complete_query_range=[0,36],angle_range=[0,2047],
            no_actual_return_is_fabricated=True)
            for s in slots if not s.get("angular_by_query")]
        result["all_declared_accurate_Hermite_bounds_available"]=(
            len(result["Hermite_transfer"])==37*17 and
            all(row["accurate_reference_pointwise_Hermite_bound_available"] for row in result["Hermite_transfer"]))
        result["entire_original_IEEE_execution_error_certified"]=False
        result["complete_true_Hermite_query_angle_domain_certified"]=False
        result["original_model_FD_or_native_gate_changed"]=False
        result["native_or_fullDN_acceptance"]=False
        result["accurate_trigonometric_table"]=trig.identity() if trig is not None else None
        result["verified_original_packets"]=list(packets.verified.values()) if packets is not None else []
        result["elapsed_seconds"]=budget.elapsed();result["active_cursor"]=dict(budget.current)
        result["post_model_diagnostic_exit_code"]=exit_code
        result["Git_Release_or_artifact_raw_uploads"]=0
        result_receipt=safe_write(args.out/"result.json",result)
        summary=dict(schema=SCHEMA,request=170,result=result_receipt,
            scientific_completed=result["scientific_completed"],resource_partial=result["resource_partial"],
            scientific_completed_means_all_requested_computations_visited_not_certificate=True,
            scientific_exception=result["scientific_exception"],stop_reason=result.get("stop_reason"),
            original_model_accepted=result.get("original_model_accepted"),
            original_model_exit_code=result.get("original_model_exit_code"),
            post_model_diagnostic_exit_code=exit_code,
            original_complete_endpoint_variants=len(variants),
            complete_finite_endpoint_projections=sum(v.get("complete_finite_projection") is True for v in endpoint_summaries),
            full453_Hermite_formation_queries=len(result["Hermite_formation"]),
            complete_Hermite_transfer_pairs=len(result["Hermite_transfer"]),
            proved_accurate_Hermite_pairs=sum(v["accurate_reference_pointwise_Hermite_bound_available"]
                for v in result["Hermite_transfer"]),
            all_declared_accurate_Hermite_bounds_available=result["all_declared_accurate_Hermite_bounds_available"],
            pending_reference_scopes=result["pending_reference_scopes"],
            pending_Hermite_transfer_pairs=result["pending_Hermite_transfer_pairs"],
            entire_original_IEEE_execution_error_certified=False,
            complete_true_Hermite_query_angle_domain_certified=False,
            all_raw_numerical_values_not_claimed_printed=True,
            complete_scalar_range_and_failure_metadata_require_same_job_readback=True,
            original_model_and_FD_gates_not_changed=True,
            elapsed_seconds=result["elapsed_seconds"],active_cursor=result["active_cursor"])
        safe_write(args.out/"summary.json",summary)
        print(json.dumps(dict(event="request170_post_model_R354_returned",**summary),
            ensure_ascii=True,separators=(",",":")),flush=True)
    return exit_code


if __name__=="__main__":
    raise SystemExit(main())
