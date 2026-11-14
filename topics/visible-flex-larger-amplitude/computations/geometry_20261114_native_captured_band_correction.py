#!/usr/bin/env python3
"""Offline full-band correction of an already captured original native model.

Actions only. No native worker, new J, ODE/RK, initializer, trial, H change or
nonlinear acceptance. Read every captured byte; factor exactly the complete
node-major cut/stage/far array system with partial-pivoted band LU. Scaling
must be selected explicitly. Restore all original coordinates and reread the
unmodified captured J/r/scales for both old and new full linear defects.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import re
import resource
import struct
from fractions import Fraction
from decimal import Decimal, localcontext
import sys
import time

for _thread_name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_thread_name] = "1"

import numpy as np
import scipy
from scipy.linalg.lapack import dgbtrf, dgbtrs

CAPTURE_PY_SHA = "0b49f14218e4d62f0b18d77dd3fa8aee1cb6225f84d92bb81dace173cf74dcc0"
CAPTURE_HOOK_SHA = "b20aee4da9b9dd927a2d78c6691739508798c81e73501b31e14a43ad55b64d30"
CORE_SHA = "ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3"
SEED_SHA = "6b01b385de34af22094bc47fd7c8c2c2da9ac6d07bc40b5ce6362fea241218b8"
HEIGHT_SHA = "c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f"
SCALES_SHA = "ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc"
FAR_SHA = "395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54"
STOP = "VISIBLE_NATIVE_CORRECTION_CAPTURE_COMPLETE_V1"
CAPTURE_RESULT_SHA = "ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7"
CAPTURE_MANIFEST_SHA = "3ed8c1bf3458f2f5852c5e74ebaec77292233a6b940b494c73e4289bbdf95ae3"
CAPTURE_SUMMARY_SHA = "48d8c012aa0e266bd9c39d1ce6342a97ef54c7d01a6dcfb37997da6ede4b22c1"
FULL_J_SHA = "394ca2cc7c28ead3ffb963502ad24df86126c32f6e4eef10079495a753320a19"
ORIGINAL_DELTA_SHA = "d3734cf4587acbddbc32c80e49223fc6db4e8077190c8c875c22f218219031f2"


def actions_only():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY", "").lower() != "rogerhu12/math-research-public"):
        raise RuntimeError("Numerical array solves belong only to this public repository Actions")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def write(path, value, compressed=False):
    path = Path(path)
    raw = (json.dumps(value, ensure_ascii=False, indent=None if compressed else 2,
                      allow_nan=False)+"\n").encode()
    if compressed:
        raw = gzip.compress(raw, mtime=0)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(raw)
    return dict(file=path.name, bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def scalar(value):
    value = float(value)
    return dict(value=value if math.isfinite(value) else None,
        float64le_hex=struct.pack("<d", value).hex(),
        classification=("NaN" if math.isnan(value) else "positive-infinity" if value == math.inf
            else "negative-infinity" if value == -math.inf else
            "negative-zero" if value == 0 and math.copysign(1., value) < 0 else "finite"))


def float_bytes(array):
    """Canonical little-endian row-major bytes; the original inputs are <f8."""
    return np.asarray(array, dtype="<f8", order="C").tobytes(order="C")


def safe_file(directory, relative):
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        raise ValueError("One relative captured file path is required")
    candidate = (directory/relative).resolve()
    if not candidate.is_relative_to(directory.resolve()) or not candidate.is_file():
        raise ValueError("Missing or escaping captured artifact file: "+relative)
    return candidate


def same(left, right, label):
    if left != right:
        raise ValueError("Captured native model identity differs: "+label)


class CapturedArrays:
    def __init__(self, directory, expected_result_sha):
        actions_only()
        self.directory = Path(directory).resolve()
        self.expected_result_sha = expected_result_sha
        same(expected_result_sha, CAPTURE_RESULT_SHA, "actual28 retained result identity")
        if not re.fullmatch(r"[0-9a-f]{64}", expected_result_sha):
            raise ValueError("An explicit actual capture result SHA256 is required")
        result_path = self.directory/"result.json"
        same(sha(result_path), expected_result_sha, "complete actual capture result bytes")
        self.result = read(result_path)
        r = self.result
        if (r.get("schema") != "native-first-correction-capture-result-v1"
                or r.get("diagnostic_complete") is not True or r.get("native_accepted") is not False
                or r.get("planned_diagnostic_stop_observed") is not True
                or r.get("trials_executed") != 0 or r.get("original_native_requests") != 1
                or r.get("worker_exit_code") != 0 or r.get("planned_stop") != STOP):
            raise ValueError("Require the completed diagnostic, never a native accepted response")
        same(r["source_sha256"], CAPTURE_PY_SHA, "frozen capture launcher")
        same(r["hook_sha256"], CAPTURE_HOOK_SHA, "frozen capture hook")
        small = {}
        for row in r["small_output_files"]:
            name = row["file"]
            if Path(name).name != name or name in small:
                raise ValueError("Unique bounded captured output names are required")
            path = safe_file(self.directory, name)
            same(path.stat().st_size, row["bytes"], "small-file size "+name)
            same(sha(path), row["sha256"], "small-file bytes "+name)
            small[name] = row
        self.small = small
        for name in ("capture-spec.json", "capture-summary.json", "capture-manifest.json",
                     "capture-begin.json", "core-instrumentation.json", "seed-binding.json",
                     "original-live-identity-before-seed.json", "large-array-chunks.jsonl"):
            if name not in small:
                raise ValueError("A complete capture output is missing: "+name)
        self.spec = read(self.directory/"capture-spec.json")
        self.summary = read(self.directory/"capture-summary.json")
        self.manifest = read(self.directory/"capture-manifest.json")
        self.begin = read(self.directory/"capture-begin.json")
        self.live = read(self.directory/"original-live-identity-before-seed.json")
        core = read(self.directory/"core-instrumentation.json")
        same(self.small["capture-spec.json"]["sha256"], r["spec_sha256"], "capture specification")
        same(self.small["capture-summary.json"]["sha256"], r["capture_summary_sha256"], "capture summary")
        same(self.small["capture-manifest.json"]["sha256"], self.summary["manifest"]["sha256"], "binary manifest")
        same(self.small["capture-manifest.json"]["sha256"],CAPTURE_MANIFEST_SHA,"actual28 full raw manifest")
        same(self.small["capture-summary.json"]["sha256"],CAPTURE_SUMMARY_SHA,"actual28 original full diagnostic")
        same(self.summary.get("capture_completed"), True, "all capture phases completed")
        same(self.manifest.get("completed"), True, "all captured arrays completed")
        same(core["original_core_file_sha256"], CORE_SHA, "original diagonal-far native source")
        same(core["exact_insertion_roundtrip_verified"], True, "original source insertion roundtrip")
        same(self.manifest["dtype"], "<f8", "raw binary dtype")
        same(self.manifest["order"], "C", "raw binary order")
        self.M, self.K, self.depth = (int(self.begin[k]) for k in ("M", "K", "depth"))
        if (self.M, self.K, self.depth) != (112, 224, 576):
            raise ValueError("This first offline consumer is for the complete original actual28 layout")
        same(self.K, 2*self.M, "complete Q/Pi columns")
        same(len(self.live["stages"]), self.depth, "every original stage location")
        same(self.begin["candidate_states_float64le_sha256"], SEED_SHA, "full original seed bytes")
        self.arrays = {}
        for entry in self.manifest["arrays"]:
            name = entry["name"]
            if name in self.arrays or entry.get("completed") is not True:
                raise ValueError("Every captured array must be complete and uniquely named")
            same(entry["dtype"], "<f8", "array dtype "+name)
            same(entry["order"], "C", "array order "+name)
            self.arrays[name] = entry
        expected = {
            "stage-jacobians": [self.depth,self.K,self.K],
            "stage-residuals": [self.depth,self.K],
            "base-states": [self.depth+1,self.K],
            "original-delta": [self.depth+1,self.K],
            "original-scales": [1,self.depth+1],
            "original-far-graph": [1,self.M],
            "physical-height": [1,self.M], "cut-target": [1,self.M],
            "cut-residual": [1,self.M], "end-residual": [1,self.M],
            "linear-stage-defects": [self.depth,self.K],
            "scaled-linear-stage-defects": [self.depth,self.K],
            "linear-cut-defects": [1,self.M], "scaled-linear-cut-defects": [1,self.M],
            "linear-far-defects": [1,self.M], "scaled-linear-far-defects": [1,self.M],
        }
        for name, shape in expected.items():
            same(self.arrays[name]["shape"], shape, "full array dimensions "+name)
        for name, digest in (("base-states",SEED_SHA),("physical-height",HEIGHT_SHA),
                             ("original-scales",SCALES_SHA),("original-far-graph",FAR_SHA),
                             ("stage-jacobians",FULL_J_SHA),("original-delta",ORIGINAL_DELTA_SHA)):
            same(self.arrays[name]["raw_sha256"], digest, "original complete raw bytes "+name)
        self.verified_bytes, self.verified_chunks = 0, 0
        self.chunk_files = set()
        for name in self.arrays:
            self.verify_array(name)
        ledger = [json.loads(line) for line in (self.directory/"large-array-chunks.jsonl").read_text().splitlines()]
        listed = [row for entry in self.manifest["arrays"] for row in entry["chunks"]]
        same(ledger, listed, "complete successful chunk ledger order")
        self.binding = dict(schema="captured-native-full-array-binding-v1",
            capture_result_sha256=expected_result_sha,capture_public_run="43611175099",
            capture_public_source="6bd52b446241be53e8842d4db5a24f9c2069e6e5",capture_spec_sha256=r["spec_sha256"],
            capture_summary_sha256=r["capture_summary_sha256"],
            capture_manifest_sha256=self.small["capture-manifest.json"]["sha256"],
            capture_source_sha256=CAPTURE_PY_SHA,capture_hook_sha256=CAPTURE_HOOK_SHA,
            original_core_sha256=CORE_SHA,complete_arrays=len(self.arrays),
            complete_chunks=self.verified_chunks,complete_raw_bytes=self.verified_bytes,
            full_original_J_reused=True,no_new_J=True,
            raw_array_sha256={name:entry["raw_sha256"] for name,entry in self.arrays.items()},
            original_far_is_diagonal=True,
            diagonal_far_basis="Pinned original core ev.end[j]=Pi_D[j]-graphs[D][j]*Q_D[j], complete M-vector retained",
            all_original_rows_modes_nodes_and_scales_retained=True,
            no_native_solve_or_trial=True,native_accepted=False,task_completed=False)

    def chunks(self, name, verify=True):
        entry = self.arrays[name]
        shape = entry["shape"]
        row_size = math.prod(shape[1:])
        for descriptor in entry["chunks"]:
            path = safe_file(self.directory, descriptor["file"])
            raw = path.read_bytes()
            if verify:
                same(len(raw),descriptor["bytes"],"reread raw chunk bytes "+descriptor["file"])
                same(hashlib.sha256(raw).hexdigest(),descriptor["raw_sha256"],"reread raw chunk hash "+descriptor["file"])
            count = descriptor["row_stop"]-descriptor["row_start"]
            yield descriptor, np.frombuffer(raw,dtype="<f8").reshape((count,*shape[1:]))

    def verify_array(self, name):
        entry = self.arrays[name]
        rows = 0; total = 0; full = hashlib.sha256()
        shape = entry["shape"]
        if not shape or any(type(x) is not int or x <= 0 for x in shape):
            raise ValueError("Positive complete captured array shape required")
        for index, descriptor in enumerate(entry["chunks"]):
            same(descriptor["array"],name,"chunk array")
            same(descriptor["chunk_index"],index,"chunk index")
            same(descriptor["row_start"],rows,"contiguous chunk rows")
            stop=descriptor["row_stop"]
            if type(stop) is not int or not rows < stop <= shape[0]:
                raise ValueError("Invalid complete chunk row range")
            expected=(stop-rows)*math.prod(shape[1:])*8
            same(descriptor["bytes"],expected,"full raw chunk size")
            relative=descriptor["file"]
            if relative in self.chunk_files:
                raise ValueError("A raw chunk file is reused for two arrays")
            self.chunk_files.add(relative)
            path=safe_file(self.directory,relative)
            raw=path.read_bytes()
            same(len(raw),expected,"actual raw chunk size")
            same(hashlib.sha256(raw).hexdigest(),descriptor["raw_sha256"],"actual raw chunk hash")
            full.update(raw);rows=stop;total+=len(raw);self.verified_chunks+=1
        same(rows,shape[0],"all captured rows")
        same(total,math.prod(shape)*8,"all captured array bytes")
        same(total,entry["total_bytes"],"recorded total array bytes")
        same(full.hexdigest(),entry["raw_sha256"],"concatenated full raw array hash")
        self.verified_bytes+=total

    def all(self,name):
        entry=self.arrays[name]
        result=np.empty(entry["shape"],dtype=np.float64)
        for descriptor,values in self.chunks(name):
            result[descriptor["row_start"]:descriptor["row_stop"]]=values
        return result

    def stages(self):
        expected=0
        for descriptor,values in self.chunks("stage-jacobians"):
            for j,J in enumerate(values):
                stage=descriptor["row_start"]+j
                same(stage,expected,"streamed original J stage")
                yield stage,J
                expected+=1
        same(expected,self.depth,"all original stage matrices streamed")


class OutputArrays:
    def __init__(self,directory):
        self.directory=Path(directory)
        self.large=self.directory/"large-arrays"
        self.large.mkdir()
        self.entries=[]

    def save(self,name,array,role):
        values=np.asarray(array,dtype="<f8",order="C")
        raw=values.tobytes(order="C")
        relative="large-arrays/"+name+".f64le"
        with (self.directory/relative).open("xb") as stream:stream.write(raw)
        record=dict(name=name,file=relative,dtype="<f8",order="C",shape=list(values.shape),
            bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),role=role,
            finite=int(np.isfinite(values).sum()),nan=int(np.isnan(values).sum()),
            positive_infinity=int(np.isposinf(values).sum()),negative_infinity=int(np.isneginf(values).sum()),
            negative_zero=int(((values==0)&np.signbit(values)).sum()))
        self.entries.append(record)
        return record


def location(capture,kind,index):
    M=capture.M
    if kind=="stage":
        n,j=index
        return dict(kind=kind,stage=int(n),row=int(j),component="Q" if j<M else "Pi",
            mode=int(j%M+1),frequency=int(capture.spec["numerical_parameters"]["spacing"]*(j%M+1)),
            rawCell=capture.live["stages"][n]["rawCell"],rawSegment=capture.live["stages"][n]["rawSegment"])
    j=int(index[-1])
    return dict(kind=kind,node=0 if kind=="cut" else capture.depth,row=j,mode=j+1,
                component="Q" if kind=="cut" else "Pi-minus-original-GQ")


def norm_record(capture,kind,values):
    values=np.asarray(values,dtype=np.float64)
    nonfinite=~np.isfinite(values)
    nan=bool(np.isnan(values).any())
    absolute=np.abs(values)
    if nan:
        max_value=math.nan
        index=tuple(int(x) for x in np.argwhere(np.isnan(values))[0])
    else:
        flat=int(np.argmax(absolute));index=np.unravel_index(flat,values.shape)
        max_value=float(absolute[index])
    return dict(max_abs=scalar(max_value),location=location(capture,kind,index),
        entry=scalar(values[index]),nonfinite_entries=int(nonfinite.sum()))


def evaluate_directions(capture,directions,residuals,cut,far,scales,far_graph,output,tag):
    """Sequential separate binary64 multiply/add, matching original matvec order.

    This is still a floating diagnostic, not exact real binary-array algebra.
    All directions are evaluated in one streamed pass through the original J.
    """
    actions_only()
    labels=list(directions)
    D,K,M=capture.depth,capture.K,capture.M
    errors={key:np.empty((D,K),dtype=np.float64) for key in labels}
    with np.errstate(over="ignore",under="ignore",invalid="ignore",divide="ignore"):
        for n,J in capture.stages():
            product=np.zeros((K,len(labels)),dtype=np.float64)
            vector=np.stack([directions[key][n+1] for key in labels],axis=1)
            for j in range(K):
                multiplied=J[:,j,None]*vector[j,None,:]
                np.add(product,multiplied,out=product)
            for c,key in enumerate(labels):
                errors[key][n]=(product[:,c]-directions[key][n])+residuals[n]
    reports={}
    for key in labels:
        delta=directions[key]
        with np.errstate(over="ignore",under="ignore",invalid="ignore",divide="ignore"):
            stage=errors[key];scaled=stage/scales[:-1,None]
            ec=delta[0,:M]+cut
            ef=(delta[-1,M:]-far_graph*delta[-1,:M])+far
            sc=ec/scales[0];sf=ef/scales[-1]
        reports[key]=dict(stage=norm_record(capture,"stage",scaled),
            cut=norm_record(capture,"cut",sc),far=norm_record(capture,"far",sf),
            arithmetic="Separate sequential binary64 multiply/add in original column order; original residual and original sigma",
            exact_real_defect_certified=False,no_derivative_of_nonlinear_flow_claimed=True)
        arrays={"stage-raw":stage,"stage-scaled":scaled,"cut-raw":ec,"cut-scaled":sc,"far-raw":ef,"far-scaled":sf}
        reports[key]["arrays"]={label:output.save(tag+"-"+key+"-"+label,values,
            "Full original native "+key+" direction linear defect "+label) for label,values in arrays.items()}
        if key=="original":
            pairs={"stage-raw":"linear-stage-defects","stage-scaled":"scaled-linear-stage-defects",
                "cut-raw":"linear-cut-defects","cut-scaled":"scaled-linear-cut-defects",
                "far-raw":"linear-far-defects","far-scaled":"scaled-linear-far-defects"}
            reports[key]["capture_bitwise_comparison"]={name:
                hashlib.sha256(float_bytes(values)).hexdigest()==capture.arrays[pairs[name]]["raw_sha256"]
                for name,values in arrays.items()}
        nodes=[]
        for n,row in enumerate(delta):
            absolute=np.abs(row)
            bad=np.flatnonzero(~np.isfinite(row))
            j=int(bad[0]) if len(bad) else int(np.argmax(absolute))
            with np.errstate(over="ignore",invalid="ignore",divide="ignore"):
                ratio=float(row[j]/scales[n])
            nodes.append(dict(node=n,row=j,component="Q" if j<M else "Pi",mode=j%M+1,
                value=scalar(row[j]),relative_to_original_node_scale=scalar(ratio),
                nonfinite_entries=int(len(bad))))
        reports[key]["node_direction_maxima"]=nodes
    return reports


def fraction_record(value):
    """Exact numerator/denominator, plus a clearly labelled decimal display."""
    with localcontext() as context:
        context.prec=60
        decimal_display=format(Decimal(value.numerator)/Decimal(value.denominator),".55E")
    try:approximate=float(value)
    except OverflowError:approximate=math.inf if value>0 else -math.inf
    return dict(numerator=str(value.numerator),denominator=str(value.denominator),
        decimal_display_56_significant_digits=decimal_display,
        nearest_binary64_display=scalar(approximate))


def exact_row(capture,delta,residuals,cut,far,scales,far_graph,site,floating_value,output,name):
    """Exact real algebra of the saved finite binary inputs, not exact DR.

    Only one complete selected row is certified. An exact row lower bound
    cannot be promoted to a full-system exact upper bound.
    """
    actions_only()
    def F(value):
        value=float(value)
        if not math.isfinite(value):raise ValueError("Exact finite row requires finite original operands")
        return Fraction.from_float(value)
    kind=site["kind"];M=capture.M
    if kind=="stage":
        n=int(site["stage"]);j=int(site.get("residual_row",site.get("row")))
        if not 0<=n<capture.depth or not 0<=j<capture.K:raise ValueError("Invalid full stage row")
        row=None
        for descriptor,chunk in capture.chunks("stage-jacobians"):
            if descriptor["row_start"]<=n<descriptor["row_stop"]:
                row=np.array(chunk[n-descriptor["row_start"],j],copy=True);break
        if row is None:raise ValueError("Original full J row was not found")
        terms=[F(row[k])*F(delta[n+1,k]) for k in range(capture.K)]
        exact=sum(terms,Fraction(0))-F(delta[n,j])+F(residuals[n,j])
        sigma=F(scales[n])
        witness=dict(stage=n,row=j,full_J_row_float64le_hex=float_bytes(row).hex(),
            full_next_delta_float64le_hex=float_bytes(delta[n+1]).hex(),
            current_delta=scalar(delta[n,j]),original_residual=scalar(residuals[n,j]),original_scale=scalar(scales[n]),
            exact_sum_absolute_products=fraction_record(sum(map(abs,terms),Fraction(0))))
    elif kind=="cut":
        j=int(site["row"])
        if not 0<=j<M:raise ValueError("Invalid complete cut row")
        exact=F(delta[0,j])+F(cut[j]);sigma=F(scales[0])
        witness=dict(node=0,row=j,delta=scalar(delta[0,j]),original_residual=scalar(cut[j]),original_scale=scalar(scales[0]))
    elif kind=="far":
        j=int(site["row"])
        if not 0<=j<M:raise ValueError("Invalid complete far row")
        exact=F(delta[-1,M+j])-F(far_graph[j])*F(delta[-1,j])+F(far[j]);sigma=F(scales[-1])
        witness=dict(node=capture.depth,row=j,delta_Pi=scalar(delta[-1,M+j]),delta_Q=scalar(delta[-1,j]),
            original_far_G=scalar(far_graph[j]),original_residual=scalar(far[j]),original_scale=scalar(scales[-1]))
    else:raise ValueError("Unknown original native boundary/stage kind")
    normalized=exact/sigma
    record=dict(schema="exact-single-row-of-captured-binary-native-model-v1",
        source_sha256=sha(__file__),capture_result_sha256=CAPTURE_RESULT_SHA,
        capture_manifest_sha256=CAPTURE_MANIFEST_SHA,full_J_sha256=FULL_J_SHA,
        full_delta_float64le_sha256=hashlib.sha256(float_bytes(delta)).hexdigest(),
        site=site,witness=witness,exact_unscaled_defect=fraction_record(exact),
        exact_original_scaled_defect=fraction_record(normalized),
        exact_absolute_scaled_lower_bound_on_full_model_defect=fraction_record(abs(normalized)),
        compared_floating_diagnostic=scalar(floating_value),
        all_input_binary_numbers_interpreted_as_exact_reals=True,
        full_exact_upper_bound_claimed=False,exact_derivative_of_original_nonlinear_flow_claimed=False,
        native_accepted=False,task_completed=False)
    if math.isfinite(float(floating_value)):
        difference=F(floating_value)-normalized
        record["exact_difference_floating_report_minus_exact_row"]=fraction_record(difference)
        if normalized:
            record["exact_relative_difference"]=fraction_record(difference/normalized)
    descriptor=write(output.directory/(name+".json"),record)
    return dict(file=descriptor,site=site,exact_original_scaled_defect=record["exact_original_scaled_defect"],
        floating_diagnostic=record["compared_floating_diagnostic"],
        full_exact_upper_bound_claimed=False,exact_derivative_of_nonlinear_flow_claimed=False)


def select_report_worst(report):
    choices=[report[key] for key in ("stage","cut","far")]
    for row in choices:
        if row["max_abs"]["classification"] not in ("finite","negative-zero"):
            return row["location"],row["entry"]
    worst=max(choices,key=lambda x:x["max_abs"]["value"])
    return worst["location"],worst["entry"]


def stored_scalar(record):
    return struct.unpack("<d",bytes.fromhex(record["float64le_hex"]))[0]


def main():
    actions_only()
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capture-directory",type=Path,required=True)
    parser.add_argument("--capture-result-sha256",default=CAPTURE_RESULT_SHA)
    parser.add_argument("--scaling",choices=("none","original-sigma"),default="original-sigma")
    parser.add_argument("--out",type=Path,required=True)
    a=parser.parse_args()
    a.out=a.out.resolve();a.out.mkdir(parents=True,exist_ok=True)
    if any(a.out.iterdir()) or a.out.is_relative_to(a.capture_directory.resolve()):
        raise ValueError("Use an empty independent output directory")
    started=time.monotonic()
    report=dict(schema="original-captured-native-full-band-correction-v1",source_sha256=sha(__file__),
        capture_result_sha256=a.capture_result_sha256,scaling=a.scaling,
        diagnostic_completed=False,linear_direction_computed=False,native_accepted=False,task_completed=False,
        original_native_calls=0,new_J_calls=0,nonlinear_trials=0,
        NumPy=np.__version__,SciPy=scipy.__version__,
        BLAS_threads={key:os.environ.get(key) for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS")})
    output=None
    try:
        capture=CapturedArrays(a.capture_directory,a.capture_result_sha256)
        write(a.out/"input-binding.json",capture.binding)
        M,K,D=capture.M,capture.K,capture.depth
        N=(D+1)*K;kl=M;ku=3*M-1;ldab=2*kl+ku+1;diagonal=kl+ku
        original_delta=capture.all("original-delta")
        residuals=capture.all("stage-residuals")
        cut=capture.all("cut-residual").reshape(-1)
        far=capture.all("end-residual").reshape(-1)
        scales=capture.all("original-scales").reshape(-1)
        far_graph=capture.all("original-far-graph").reshape(-1)
        for name,values in (("original residuals",residuals),("cut residual",cut),("far residual",far),
                            ("original scales",scales),("original diagonal far graph",far_graph)):
            if not np.isfinite(values).all():raise FloatingPointError("Nonfinite captured "+name)
        if np.any(scales<=0):raise ValueError("Original residual scales must be positive")
        coordinate_scale=scales.copy() if a.scaling=="original-sigma" else np.ones(D+1)
        output=OutputArrays(a.out)
        old_worst=capture.summary["linear_defect_summary"]["all_original_rows"]["worst"]
        old_float=stored_scalar(old_worst["value"])
        report["exact_original_captured_worst_row"]=exact_row(capture,original_delta,residuals,cut,far,scales,far_graph,
            old_worst,old_float,output,"exact-original-captured-worst-row")
        # The original exact-row witness survives a later factor/solve failure.
        # Row and column scales agree at each node. The original -I, cut I and
        # diagonal far blocks therefore require no rounded scale products.
        ab=np.zeros((ldab,N),dtype=np.float64,order="F")
        rhs=np.empty((N,1),dtype=np.float64,order="F")
        rhs[:M,0]=-cut/coordinate_scale[0]
        rhs[M:M+D*K,0]=(-residuals/coordinate_scale[:-1,None]).reshape(-1)
        rhs[M+D*K:,0]=-far/coordinate_scale[-1]
        local=np.arange(K)
        row_entry_max=np.zeros(N,dtype=np.float64)
        column_entry_max=np.zeros(N,dtype=np.float64)
        ab[diagonal,np.arange(M)]=1.
        row_entry_max[:M]=1.;column_entry_max[:M]=1.
        formed_zero_from_nonzero=0
        ratios=[]
        for n,J in capture.stages():
            if not np.isfinite(J).all():raise FloatingPointError("Nonfinite original captured J at stage "+str(n))
            row_start=M+n*K;columns=(n+1)*K+local[None,:]
            band_rows=diagonal+row_start+local[:,None]-columns
            if int(band_rows.min())<kl or int(band_rows.max())>=ldab:
                raise ValueError("The true complete stage does not fit the derived band")
            ratio=coordinate_scale[n+1]/coordinate_scale[n]
            with np.errstate(over="ignore",under="ignore",invalid="ignore",divide="ignore"):
                block=J*ratio
            if not math.isfinite(float(ratio)) or not np.isfinite(block).all():
                raise FloatingPointError("Nonfinite explicitly scaled matrix at stage "+str(n))
            formed_zero_from_nonzero+=int(((J!=0)&(block==0)).sum())
            ab[band_rows,columns]=block
            ab[diagonal+M,n*K+local]=-1.
            row_entry_max[row_start:row_start+K]=np.maximum(1.,np.max(np.abs(block),axis=1))
            column_entry_max[n*K:(n+1)*K]=np.maximum(column_entry_max[n*K:(n+1)*K],1.)
            column_entry_max[(n+1)*K:(n+2)*K]=np.maximum(
                column_entry_max[(n+1)*K:(n+2)*K],np.max(np.abs(block),axis=0))
            ratios.append(scalar(ratio))
        far_columns=D*K+np.arange(M)
        ab[diagonal+M,far_columns]=-far_graph
        ab[diagonal,far_columns+M]=1.
        row_entry_max[M+D*K:]=np.maximum(1.,np.abs(far_graph))
        column_entry_max[far_columns]=np.maximum(column_entry_max[far_columns],np.abs(far_graph))
        column_entry_max[far_columns+M]=np.maximum(column_entry_max[far_columns+M],1.)
        output.save("formed-row-max-absolute-entry",row_entry_max,"Actual formed floating band matrix maximum entry in each equation row; not a condition number")
        output.save("formed-column-max-absolute-entry",column_entry_max,"Actual formed floating band matrix maximum entry in each coordinate column; not a condition number")
        report["formed_matrix_entry_scales"]=dict(
            row_maximum_range=[scalar(np.min(row_entry_max)),scalar(np.max(row_entry_max))],
            column_maximum_range=[scalar(np.min(column_entry_max)),scalar(np.max(column_entry_max))],
            zero_rows=int((row_entry_max==0).sum()),zero_columns=int((column_entry_max==0).sum()),
            extra_equilibration_applied=False)
        if not np.isfinite(rhs).all():raise FloatingPointError("Nonfinite scaled complete RHS")
        output.save("complete-scaled-rhs",rhs[:,0],"Negative complete captured residual in cut/stage/far equation order")
        output.save("coordinate-scales",coordinate_scale,"Explicit diagonal row and column scales by node")
        matrix_hash=hashlib.sha256(memoryview(ab.ravel(order="F")).cast("B")).hexdigest()
        report.update(M=M,K=K,depth=D,dimension=N,lower_bandwidth=kl,upper_bandwidth=ku,
            LAPACK_band_rows=ldab,band_bytes=int(ab.nbytes),band_shape=list(ab.shape),
            equation_order="cut M; D complete K-row stages; far M",variable_order="node-major complete (Q,Pi)",
            far_is_original_diagonal=True,unfactored_band_Fortran_byte_sha256=matrix_hash,
            explicit_coordinate_scale_sha256=hashlib.sha256(float_bytes(coordinate_scale)).hexdigest(),
            scale_ratios=ratios,scaled_matrix_nonzero_rounding_to_zero=formed_zero_from_nonzero,
            scaled_matrix_rounding_is_not_an_exact_change_of_real_arrays=True,
            original_capture_linear_defect_summary=capture.summary["linear_defect_summary"],
            original_capture_maximum_chart_summary=capture.summary["maximum_chart_summary"])
        write(a.out/"assembled-model.json",report)
        factor_started=time.monotonic();pointer=ab.__array_interface__["data"][0]
        lu,piv,info=dgbtrf(ab,kl,ku,overwrite_ab=1)
        report.update(lapack_factor_info=int(info),factorization_seconds=time.monotonic()-factor_started,
            LU_shares_input_storage=bool(np.shares_memory(lu,ab)),
            LU_retains_input_pointer=pointer==lu.__array_interface__["data"][0],
            LU_Fortran_byte_sha256=hashlib.sha256(memoryview(lu.ravel(order="F")).cast("B")).hexdigest())
        # The large reproducible LU is not duplicated on disk; the original J
        # and the source/scaling/RHS/pivots define the solve reproducibly.
        pivot_bytes=np.asarray(piv,dtype="<i4").tobytes()
        with (a.out/"large-arrays/lapack-pivots.i32le").open("xb") as stream:stream.write(pivot_bytes)
        report["pivot_array"]=dict(file="large-arrays/lapack-pivots.i32le",dtype="<i4",shape=list(piv.shape),
            bytes=len(pivot_bytes),sha256=hashlib.sha256(pivot_bytes).hexdigest(),
            interpretation="SciPy dgbtrf pivot indices, retained unchanged for dgbtrs")
        output.entries.append(dict(name="lapack-pivots",role="Unchanged LAPACK full pivot vector",**report["pivot_array"]))
        write(a.out/"factorization.json",report)
        if info<0:raise RuntimeError("dgbtrf rejected argument "+str(-info))
        if info>0:raise FloatingPointError("dgbtrf returned a zero pivot at LAPACK index "+str(info))
        solve_started=time.monotonic()
        solution,info=dgbtrs(lu,kl,ku,rhs,piv,overwrite_b=1)
        report.update(lapack_solve_info=int(info),solve_seconds=time.monotonic()-solve_started)
        if info:raise RuntimeError("dgbtrs failed with info="+str(info))
        scaled_direction=np.asarray(solution[:,0]).reshape(D+1,K)
        if not np.isfinite(scaled_direction).all():raise FloatingPointError("The complete band solve returned a nonfinite direction")
        output.save("complete-scaled-coordinate-delta",scaled_direction,"Every full band-solve coordinate before recovery")
        with np.errstate(over="ignore",under="ignore",invalid="ignore",divide="ignore"):
            delta=scaled_direction*coordinate_scale[:,None]
        delta_record=output.save("complete-original-coordinate-delta",delta,
            "Every restored original native coordinate, before all nonlinear trials")
        report["recovery_nonzero_rounding_to_zero"]=int(((scaled_direction!=0)&(delta==0)).sum())
        if not np.isfinite(delta).all():raise FloatingPointError("Restoring the complete original coordinates was nonfinite")
        report["linear_direction_computed"]=True
        report["new_delta"]=delta_record
        report["linear_defects"]=evaluate_directions(capture,{"original":original_delta,"new":delta},
            residuals,cut,far,scales,far_graph,output,"complete")
        new_site,new_entry=select_report_worst(report["linear_defects"]["new"])
        report["exact_new_floating_worst_row"]=exact_row(capture,delta,residuals,cut,far,scales,far_graph,
            new_site,stored_scalar(new_entry),output,"exact-new-floating-worst-row")
        rows=[dict(node=n,state=row.tolist(),negative_zero_columns=np.flatnonzero((row==0)&np.signbit(row)).tolist())
              for n,row in enumerate(delta)]
        report["direction_checkpoint"]=write(a.out/"direction-checkpoint.json.gz",dict(
            schema="complete-original-native-band-direction-v1",source_sha256=report["source_sha256"],
            input_binding=capture.binding,scaling=a.scaling,M=M,K=K,depth=D,
            delta_float64le_sha256=delta_record["sha256"],rows=rows,
            no_nonlinear_trial=True,native_accepted=False,task_completed=False),compressed=True)
        report["diagnostic_completed"]=True
    except Exception as error:
        report["actual_error"]=repr(error)
    finally:
        if output is not None:
            report["array_manifest"]=write(a.out/"output-array-manifest.json",dict(
                schema="captured-native-band-direction-arrays-v1",source_sha256=report["source_sha256"],
                capture_result_sha256=a.capture_result_sha256,arrays=output.entries,
                all_arrays_artifact_only=True,native_accepted=False,task_completed=False))
        report["elapsed_seconds"]=time.monotonic()-started
        report["maximum_RSS_kib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        write(a.out/"result.json",report)
    print(json.dumps(dict(event="captured-native-band-direction-finished",
        diagnostic_completed=report["diagnostic_completed"],linear_direction_computed=report["linear_direction_computed"],
        native_accepted=False,task_completed=False),allow_nan=False),flush=True)
    return 0 if report["diagnostic_completed"] else 2

if __name__=="__main__":raise SystemExit(main())
