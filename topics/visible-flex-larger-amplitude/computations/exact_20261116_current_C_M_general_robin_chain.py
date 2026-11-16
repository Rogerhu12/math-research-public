#!/usr/bin/env python3
"""Independent complete-M general-Robin chain direction and undamped sensitivity.

The old R273 source remains immutable. Its pinned Householder front routine is
reused; complete endpoint matrices and multiple RHS columns are new explicit
inputs. Scientific imports and every computation are Actions-only.
Author: exact-refinement agent (AI), 2026-11-16. Fixed112 source remains immutable.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import struct
import sys
import time

SCHEMA = "current-C-complete-M-general-Robin-complete-chain-linear-result-v1"
SNAPSHOT_SCHEMA = "current-C-complete-M-native-linear-snapshot-v1"
MODEL = "R286-original-stored-continuous-model-convention-C-v1"
BASE_NAME = "exact_20261114_native_damped_chain_qr.py"
BASE_SHA = "9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33"
DEPTH = 576


def field_dimensions(value):
    if isinstance(value, bool) or not isinstance(value, int) or value < 112:
        raise ValueError("Explicit field_modes integer at least112 required for complete mode expansion")
    return value, 2*value, DEPTH


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Current-C scientific execution belongs to this public repository Actions")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read_json(path):
    raw = Path(path).read_bytes()
    payload = gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw
    return json.loads(payload), dict(file=Path(path).name, bytes=len(raw), sha256=sha(raw))


def emit(path, value):
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)+"\n").encode()
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(raw)
    return dict(file=path.name, bytes=len(raw), sha256=sha(raw))


def bounded_file(directory, name):
    root = Path(directory).resolve()
    p = (root/name).resolve()
    if p == root or root not in p.parents or p.is_symlink():
        raise ValueError("Array path is not a contained regular original file")
    return p


def word(value):
    x = float(value)
    return dict(value=x if math.isfinite(x) else None, f64le=struct.pack("<d", x).hex(),
                classification=("negative-zero" if x == 0 and math.copysign(1.0,x) < 0 else
                    "finite" if math.isfinite(x) else "NaN" if math.isnan(x) else
                    "positive-infinity" if x > 0 else "negative-infinity"))


def runtime(directory):
    require_actions()
    p = Path(directory)/BASE_NAME
    raw = p.read_bytes()
    if sha(raw) != BASE_SHA:
        raise ValueError("Preserved original R273 front source differs")
    # Importing this module is scientific and occurs only after require_actions.
    spec = importlib.util.spec_from_file_location("_current_C_original_QR_front", p)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module, dict(file=p.name, bytes=len(raw), sha256=sha(raw))


class Arrays:
    def __init__(self, directory, np):
        self.directory, self.np = Path(directory), np
        self.directory.mkdir(parents=True, exist_ok=False)
        self.entries = []

    def save(self, name, value, scope):
        a = self.np.asarray(value, dtype="<f8", order="C")
        raw = a.tobytes(order="C")
        name = name+".f64le"
        p = self.directory/name
        with p.open("xb") as stream:
            stream.write(raw)
        item = dict(name=name[:-6], file="large-arrays/"+name, bytes=len(raw),
                    sha256=sha(raw), dtype="<f8", order="C", shape=list(a.shape),
                    completed=True, scope=scope)
        self.entries.append(item)
        return item

    def load(self, descriptor):
        p = self.directory/Path(descriptor["file"]).name
        raw = p.read_bytes()
        if len(raw) != descriptor["bytes"] or sha(raw) != descriptor["sha256"]:
            raise ValueError("Retained complete factor bytes differ")
        return self.np.frombuffer(raw, dtype="<f8").reshape(descriptor["shape"]).copy()


class CurrentSystem:
    def __init__(self, directory, expected, np, owner_source, field_modes):
        require_actions()
        M, K, D = field_dimensions(field_modes)
        self.M, self.K, self.D = M, K, D
        self.np, self.directory = np, Path(directory)
        doc, receipt = read_json(self.directory/"snapshot.json")
        if receipt["sha256"] != expected or doc.get("schema") != SNAPSHOT_SCHEMA:
            raise ValueError("Actual current snapshot identity differs")
        owner_raw = Path(owner_source).read_bytes()
        if doc["native_owner_source_sha256"] != sha(owner_raw):
            raise ValueError("Snapshot is not from the actual current owner source")
        if doc["kind"] not in ("correction", "sensitivity"):
            raise ValueError("Independent direction or final sensitivity required")
        if (doc["model_schema"] != MODEL or doc["modes"] != M or doc["depth"] != D
                or doc["shape_dimension"] != K or doc["old_graphs_or_gains_used"] is not False):
            raise ValueError("Current complete C dimensions or source scope differs")
        if not doc.get("original_C_input_binding") or not doc.get("numeric_geometry_identity"):
            raise ValueError("Current C geometry provenance must be complete")
        denominator = float(doc["cut_height_denominator"])
        if not math.isfinite(denominator) or denominator <= 0:
            raise ValueError("Actual positive native cut height denominator word required")
        if doc["cut_height_denominator_word"] != word(denominator):
            raise ValueError("Native denominator metadata is not its actual binary64 word")
        entries = doc["arrays"]
        if not isinstance(entries, dict):
            raise ValueError("Exact named current arrays are required")
        expected_shapes = {
            "base-states": (D+1,K), "target": (M,), "scales": (D+1,),
            "stage-jacobians": (D,K,K), "stage-residuals": (D,K),
            "cut-residual": (M,), "far-residual": (M,), "far-matrix": (M,K)}
        self.arrays = {}
        for name, shape in expected_shapes.items():
            d = entries[name]
            if (d["dtype"] != "<f8" or d["order"] != "C" or tuple(d["shape"]) != shape
                    or d["completed"] is not True or d["bytes"] != math.prod(shape)*8):
                raise ValueError("Complete current array differs: "+name)
            p = bounded_file(self.directory, d["file"])
            h = hashlib.sha256(); count = 0
            with p.open("rb") as stream:
                while chunk := stream.read(1024*1024):
                    count += len(chunk); h.update(chunk)
            if count != d["bytes"] or h.hexdigest() != d["sha256"]:
                raise ValueError("Current original array SHA differs: "+name)
            a = np.memmap(p, mode="r", dtype="<f8", shape=shape, order="C")
            if not np.isfinite(a).all():
                raise FloatingPointError("Actual current input is nonfinite: "+name)
            self.arrays[name] = a
        self.scales = self.arrays["scales"]
        if not (self.scales > 0).all():
            raise ValueError("Every declared current scale must be strictly positive")
        if not (np.max(np.abs(self.arrays["far-matrix"]), axis=1) > 0).all():
            raise ValueError("A complete actual far row is zero")
        self.doc, self.receipt = doc, receipt
        self.binding = dict(schema="current-C-complete-M-general-Robin-linear-binding-v1",
            field_modes=M, shape_dimension=K, stage_count=D,
            snapshot=receipt, native_owner_source_sha256=doc["native_owner_source_sha256"],
            call=doc["call"], iteration=doc["iteration"], kind=doc["kind"],
            original_C_input_binding=doc["original_C_input_binding"],
            numeric_geometry_identity=doc["numeric_geometry_identity"],
            all_arrays=entries, physical_cut_radius=doc["cut_radius"],
            actual_cut_height_denominator=word(denominator),
            source_sha256=sha(Path(__file__).read_bytes()),
            no_old_graph_or_gain_used=True, no_interior_height_divisibility_assumed=True)
        self.identity = sha(json.dumps(self.binding, sort_keys=True, separators=(",", ":")).encode())


class GeneralRobinQR:
    def __init__(self, system, engine, eta, output, deadline, maximum_bytes):
        require_actions()
        M, K, D = system.M, system.K, system.D
        self.system, self.engine, self.np, self.output = system, engine, engine.np, output
        self.kind = system.doc["kind"]
        self.eta = float(eta)
        if not math.isfinite(self.eta) or (self.kind == "correction" and self.eta <= 0) or (
                self.kind == "sensitivity" and self.eta != 0):
            raise ValueError("Positive eta for direction; exactly zero for final sensitivity")
        self.RHS = 1 if self.kind == "correction" else M
        self.deadline, self.started = deadline, time.monotonic()
        self.qr_calls = 0; self.workspaces = {}
        self.factors = []; self.formed_stages = []; self.complete = False
        self.constant_rows = 0
        self.maximum_bytes = maximum_bytes
        self.minimum_diagonal = math.inf
        self.expected_bytes = 8*(D*(2*K*K+K*self.RHS)
            +K*K+K*self.RHS+(D+1)*K*self.RHS)
        self.report = dict(schema="current-C-complete-M-general-Robin-complete-square-root-v1",
            kind=self.kind, eta=word(self.eta), columns=(D+1)*K, right_hand_side_columns=self.RHS,
            rows=(D+1)*K, augmented_rows=2*(D+1)*K, source_matrix_identity=system.identity,
            all_cut_stage_far_rows_retained=True, all_penalty_and_constant_rows_retained=True,
            general_far_rows=True, old_graph_used=False, explicit_inverse_used=False,
            interior_Dirichlet_charts_required=False,
            floating_nonzero_pivots_are_not_a_strict_nonresonance_certificate=True,
            exact_saved_matrix_nonresonance_certified=False,
            expected_factor_constant_bytes=self.expected_bytes,
            maximum_factor_constant_bytes=maximum_bytes)

    def check_deadline(self):
        if self.deadline is not None and time.monotonic() >= self.deadline:
            raise TimeoutError("Declared current-chain resource budget reached")

    def finite(self, value, label):
        if not self.np.isfinite(value).all():
            self.report["nonfinite"] = self.output.save("nonfinite-"+str(len(self.output.entries)),
                value, label+"; actual unmodified nonfinite words")
            raise FloatingPointError("Actual current chain array is nonfinite: "+label)

    def qr_prefix(self, matrix, columns):
        # Frozen original complete Householder transformation, including all trailing RHS columns.
        return self.engine.NativeDampedChainQR.qr_prefix(self, matrix, columns)

    def formed(self, stage, remember):
        M, K, D = self.system.M, self.system.K, self.system.D
        np = self.np
        J = self.system.arrays["stage-jacobians"][stage]
        s = self.system.scales
        with np.errstate(over="ignore", under="ignore", invalid="ignore", divide="ignore"):
            V = np.asarray((np.asarray(J, dtype=np.longdouble)*np.longdouble(s[stage+1]))
                          /np.longdouble(s[stage]), dtype="<f8")
            rho = (np.asarray(np.asarray(self.system.arrays["stage-residuals"][stage],
                dtype=np.longdouble)/np.longdouble(s[stage]), dtype="<f8")[:,None]
                if self.kind == "correction" else np.zeros((K,self.RHS),dtype="<f8"))
        self.finite(V, "complete formed V"); self.finite(rho, "complete formed rho")
        h = sha(V.tobytes(order="C")+rho.tobytes(order="C"))
        if remember:
            self.formed_stages.append(dict(stage=stage, sha256=h,
                J_sha256=sha(J.tobytes(order="C")),
                V_sha256=sha(V.tobytes(order="C")),rho_sha256=sha(rho.tobytes(order="C"))))
        elif h != self.formed_stages[stage]["sha256"]:
            raise ValueError("Repeated formed-model bytes differ")
        return V, rho

    def save_factor(self, node, R, S, affine, constant):
        np = self.np
        combined = np.column_stack((R,affine)) if S is None else np.column_stack((R,S,affine))
        factor = self.output.save(f"factor-{node:04d}", combined,
            "Complete upper R, optional next-node S, and every affine RHS")
        pure = self.output.save(f"constant-{node:04d}", constant,
            "Every pure residual row and RHS left by complete orthogonal compression")
        self.factors.append(dict(node=node, factor=factor, constant=pure, final=S is None))
        self.constant_rows += constant.shape[0]
        self.minimum_diagonal = min(self.minimum_diagonal,float(np.min(np.abs(np.diag(R)))))

    def factorize(self):
        require_actions()
        M, K, D = self.system.M, self.system.K, self.system.D
        np = self.np
        if self.factors or self.complete:
            raise RuntimeError("A bound current matrix has only one factorization attempt")
        if self.expected_bytes > self.maximum_bytes:
            raise MemoryError("Complete factors exceed declared storage resource budget")
        I = np.eye(K,dtype="<f8"); penalty = self.eta*I
        if self.kind == "correction":
            cut = np.asarray(np.asarray(self.system.arrays["cut-residual"],dtype=np.longdouble)
                /np.longdouble(self.system.scales[0]),dtype="<f8")[:,None]
            far = np.asarray(np.asarray(self.system.arrays["far-residual"],dtype=np.longdouble)
                /np.longdouble(self.system.scales[-1]),dtype="<f8")[:,None]
        else:
            r = float(self.system.doc["cut_radius"])
            if not math.isfinite(r) or r <= 0:
                raise ValueError("Actual positive current cut radius required")
            with np.errstate(over="ignore",under="ignore",invalid="ignore",divide="ignore"):
                cut = np.asarray(-np.eye(M,dtype=np.longdouble)/
                    (np.longdouble(self.system.doc["cut_height_denominator"])*
                     np.longdouble(self.system.scales[0])),dtype="<f8")
            far = np.zeros((M,M),dtype="<f8")
        self.finite(cut,"complete cut RHS"); self.finite(far,"complete far RHS")
        self.cut_rho,self.far_rho=cut,far
        self.report["formed_cut_rhs"]=self.output.save("formed-cut-rhs",cut,"Actual complete formed cut affine columns")
        self.report["formed_far_rhs"]=self.output.save("formed-far-rhs",far,"Actual complete formed far affine columns")
        carry=np.column_stack((I[:M],cut))
        for n in range(D):
            self.check_deadline()
            V,rho=self.formed(n,True); crows=carry.shape[0]
            front=np.zeros((crows+2*K,2*K+self.RHS),dtype="<f8",order="F")
            front[:crows,:K]=carry[:,:K];front[:crows,2*K:]=carry[:,K:]
            front[crows:crows+K,:K]=penalty
            front[crows+K:,:K]=-I;front[crows+K:,K:2*K]=V;front[crows+K:,2*K:]=rho
            first=self.qr_prefix(front,K)
            second=self.qr_prefix(first[K:,K:],K)
            carry=np.column_stack((np.triu(second[:K,:K]),second[:K,K:]))
            self.save_factor(n,np.triu(first[:K,:K]).copy(),first[:K,K:2*K].copy(),
                first[:K,2*K:].copy(),second[K:,K:].copy())
            if (n+1)%32==0 or n+1==D:
                print(json.dumps(dict(event="current_C_general_chain_factor",kind=self.kind,
                    completed_stages=n+1,expected_stages=D,elapsed=time.monotonic()-self.started)),flush=True)
        self.check_deadline()
        final=np.zeros((2*K+M,K+self.RHS),dtype="<f8",order="F")
        final[:K]=carry;final[K:2*K,:K]=penalty
        final[2*K:,:K]=self.system.arrays["far-matrix"];final[2*K:,K:]=far
        last=self.qr_prefix(final,K)
        self.save_factor(D,np.triu(last[:K,:K]).copy(),None,last[:K,K:].copy(),last[K:,K:].copy())
        if self.constant_rows!=(D+1)*K or len(self.factors)!=D+1:
            raise AssertionError("A complete factor or constant row is missing")
        total=sum(x["factor"]["bytes"]+x["constant"]["bytes"] for x in self.factors)
        if total!=self.expected_bytes:
            raise AssertionError("The complete factor byte account differs")
        self.complete=True
        self.report.update(complete=True,qr_calls=self.qr_calls,complete_factors=D+1,
            constant_rows=self.constant_rows,actual_factor_constant_bytes=total,
            minimum_absolute_triangular_diagonal=word(self.minimum_diagonal),
            no_threshold_rank_truncation=True)
        return self.report

    def load_factor(self,n):
        M, K, D = self.system.M, self.system.K, self.system.D
        row=self.factors[n];a=self.output.load(row["factor"])
        return a[:,:K],None if row["final"] else a[:,K:2*K],a[:,K if row["final"] else 2*K:]

    def solve(self):
        require_actions()
        M, K, D = self.system.M, self.system.K, self.system.D
        np=self.np
        if not self.complete:
            raise RuntimeError("Incomplete factors cannot supply a complete direction or sensitivity")
        z=np.empty((D+1,K,self.RHS),dtype="<f8")
        for n in range(D,-1,-1):
            self.check_deadline()
            R,S,a=self.load_factor(n);rhs=-a.copy()
            if S is not None:rhs-=S@z[n+1]
            self.finite(rhs,"complete backward RHS")
            solved,info=self.engine.dtrtrs(np.asarray(R.T,dtype="<f8",order="F"),
                np.asarray(rhs,dtype="<f8",order="F"),lower=1,trans=1,unitdiag=0,overwrite_b=1)
            if info:
                self.report["triangular_failure"]={"node":n,"info":int(info)}
                raise RuntimeError("Whole current chain final or retained triangular solve failed: "+str(info))
            self.finite(solved,"actual complete backward solution");z[n]=solved
        with np.errstate(over="ignore",under="ignore",invalid="ignore"):
            delta=np.multiply(z,self.system.scales[:,None,None],dtype=np.float64)
        self.finite(delta,"complete sigma recovery")
        self.report["z"]=self.output.save("complete-scaled-solution",z,"Every node, shape coordinate and RHS")
        self.report["delta"]=self.output.save("complete-original-coordinate-solution",delta,
            "Actual binary64 sigma*z, all 577 nodes and all requested RHS")
        self.report["nonzero_recovery_to_zero"]=int(np.count_nonzero((z!=0)&(delta==0)))
        self.report["negative_zero_recovered"]=int(np.count_nonzero((delta==0)&np.signbit(delta)))
        return z,delta

    def numerical_readback(self,z,delta):
        require_actions()
        M, K, D = self.system.M, self.system.K, self.system.D
        np=self.np
        # Sensitivity uses BLAS f64 for all M complete columns. Direction uses
        # longdouble readback. Both are readouts, not exact/rank/acceptance gates.
        dtype=np.longdouble if self.RHS==1 else np.float64
        zz=np.asarray(z,dtype=dtype)
        cut=zz[0,:M]+np.asarray(self.cut_rho,dtype=dtype)
        errors=[cut]
        original_cut=(np.asarray(delta[0,:M],dtype=dtype)
            +(np.asarray(self.system.arrays["cut-residual"],dtype=dtype)[:,None]
              if self.RHS==1 else -np.eye(M,dtype=dtype)/dtype(self.system.doc["cut_height_denominator"])))
        original=[original_cut/ dtype(self.system.scales[0])]
        for n in range(D):
            self.check_deadline()
            V,rho=self.formed(n,False)
            errors.append(-zz[n]+np.asarray(V,dtype=dtype)@zz[n+1]+np.asarray(rho,dtype=dtype))
            residual=-np.asarray(delta[n],dtype=dtype)+np.asarray(
                self.system.arrays["stage-jacobians"][n],dtype=dtype)@np.asarray(delta[n+1],dtype=dtype)
            if self.RHS==1:residual+=np.asarray(self.system.arrays["stage-residuals"][n],dtype=dtype)[:,None]
            original.append(residual/dtype(self.system.scales[n]))
        F=np.asarray(self.system.arrays["far-matrix"],dtype=dtype)
        errors.append(F@zz[-1]+np.asarray(self.far_rho,dtype=dtype))
        original_far=F@np.asarray(delta[-1],dtype=dtype)
        if self.RHS==1:original_far+=np.asarray(self.system.arrays["far-residual"],dtype=dtype)[:,None]
        original.append(original_far/dtype(self.system.scales[-1]))
        model=np.concatenate(errors,axis=0);unscaled=np.concatenate(original,axis=0)
        if model.shape!=((D+1)*K,self.RHS) or unscaled.shape!=model.shape:
            raise AssertionError("Complete original row set changed")
        self.finite(model,"formed-model residual");self.finite(unscaled,"original-coordinate numerical residual")
        return dict(arithmetic=str(np.dtype(dtype)),kind=self.kind,
            complete_rows=(D+1)*K,columns=self.RHS,
            formed_residual=self.output.save("all-formed-residuals",model,"Full numerical formed-model row readback"),
            original_coordinate_weighted_residual=self.output.save("all-original-residuals",unscaled,
                "Full numerical action of original saved J and general far matrix on the recovered arrays"),
            maximum_by_rhs=[word(x) for x in np.max(np.abs(unscaled),axis=0)],
            no_linear_residual_gate=True,no_nonlinear_acceptance_claim=True,
            exact_saved_matrix_nonresonance_certified=False)


def scaled_integer(value):
    bits=struct.unpack("<Q",struct.pack("<d",float(value)))[0]
    sign=-1 if bits>>63 else 1
    exponent=(bits>>52)&2047;fraction=bits&((1<<52)-1)
    if exponent==2047:raise ValueError("Nonfinite exact-row operand")
    return sign*(fraction if exponent==0 else ((1<<52)|fraction)<<(exponent-1))


def compact_integer(value):
    if value==0:return {"significand_hex":"0","power_of_two":0}
    shift=(abs(value)&-abs(value)).bit_length()-1
    reduced=value>>shift
    return {"significand_hex":("-" if reduced<0 else "")+format(abs(reduced),"x"),"power_of_two":shift}


def exact_direction_readback(system,delta,out,deadline):
    """Every original row, including general far rows, in exact dyadic integer arithmetic."""
    require_actions()
    M, K, D = system.M, system.K, system.D
    d=[[scaled_integer(v) for v in row[:,0]] for row in delta]
    scales=[scaled_integer(x) for x in system.scales]
    path=Path(out)/"large-arrays"/"all-original-exact-direction-rows.jsonl.gz"
    ledger_hash=hashlib.sha256();count=0;maximum=None
    with path.open("xb") as raw_stream, gzip.GzipFile(filename="",mode="wb",fileobj=raw_stream,mtime=0) as stream:
        def put(kind,node,index,integer):
            nonlocal count,maximum
            s=scales[node]
            row=dict(global_row=count,kind=kind,node=node,component=index,
                residual_times_2_power_2148=compact_integer(integer),
                sigma_times_2_power_1074=compact_integer(s))
            encoded=(json.dumps(row,sort_keys=True,separators=(",",":"))+"\n").encode()
            stream.write(encoded);ledger_hash.update(encoded)
            candidate=dict(global_row=count,kind=kind,node=node,component=index,
                numerator=abs(integer),denominator=s,signed_numerator=integer)
            if maximum is None or candidate["numerator"]*maximum["denominator"]>maximum["numerator"]*s:
                maximum=candidate
            count+=1
        for i,r in enumerate(system.arrays["cut-residual"]):
            put("cut",0,i,(scaled_integer(r)+d[0][i])<<1074)
        for n in range(D):
            if deadline is not None and time.monotonic()>=deadline:
                raise TimeoutError("Resource deadline during exact direction readback; partial raw ledger retained")
            J=system.arrays["stage-jacobians"][n]
            for i,r in enumerate(system.arrays["stage-residuals"][n]):
                value=(scaled_integer(r)-d[n][i])<<1074
                for a,b in zip(J[i],d[n+1]):
                    if b and a!=0:value+=scaled_integer(a)*b
                put("stage",n,i,value)
        F=system.arrays["far-matrix"]
        for i,r in enumerate(system.arrays["far-residual"]):
            value=scaled_integer(r)<<1074
            for a,b in zip(F[i],d[-1]):
                if b and a!=0:value+=scaled_integer(a)*b
            put("far",D,i,value)
    if count!=(D+1)*K:raise AssertionError("Not every original exact row was retained")
    b=path.read_bytes()
    from decimal import Decimal,localcontext
    with localcontext() as ctx:
        ctx.prec=65
        decimal=str(Decimal(maximum["numerator"])/Decimal(maximum["denominator"])/(Decimal(2)**1074))
    maximum["numerator"]=compact_integer(maximum["numerator"])
    maximum["signed_numerator"]=compact_integer(maximum["signed_numerator"])
    maximum["denominator"]=compact_integer(maximum["denominator"])
    maximum["absolute_original_sigma_residual_decimal"]=decimal
    maximum["decimal_is_a_display_not_a_new_gate"]=True
    return dict(schema="current-C-complete-M-general-Robin-all-original-direction-rows-v1",complete_rows=count,
        ledger=dict(file="large-arrays/"+path.name,bytes=len(b),sha256=sha(b),
                    decoded_sha256=ledger_hash.hexdigest(),rows=count),
        maximum=maximum,formula="(r+A delta)/original_sigma, exact saved f64 operands",
        unit="integer residual * 2^-2148 divided by integer sigma * 2^-1074",
        no_new_nonlinear_gate=True)


def main(argv=None):
    require_actions()
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--field-modes",type=int,required=True)
    p.add_argument("--snapshot-directory",type=Path,required=True)
    p.add_argument("--snapshot-result-sha256",required=True)
    p.add_argument("--native-owner-source",type=Path,required=True)
    p.add_argument("--computations",type=Path,required=True)
    p.add_argument("--eta",required=True,type=float)
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--budget-seconds",type=float,required=True)
    p.add_argument("--max-factor-bytes",type=int,default=2147483648)
    args=p.parse_args(argv)
    M, K, D = field_dimensions(args.field_modes)
    if not math.isfinite(args.budget_seconds) or args.budget_seconds<=0:
        raise ValueError("Positive explicit linear resource budget required")
    if args.out.exists():raise FileExistsError("Fresh owned current-chain output required")
    args.out.mkdir(parents=True)
    started=time.monotonic();report=dict(schema=SCHEMA,source_sha256=sha(Path(__file__).read_bytes()),
        completed=False,failed=False,exact_saved_matrix_nonresonance_certified=False,
        nonlinear_native_accepted=False,new_RHS_calls=0,new_J_calls=0,new_ODE_steps=0)
    exit_code=1; qr=None; arrays=None
    try:
        engine,base_receipt=runtime(args.computations)
        system=CurrentSystem(args.snapshot_directory,args.snapshot_result_sha256,engine.np,args.native_owner_source,M)
        report.update(input_binding=system.binding,input_matrix_identity=system.identity,
            original_front_engine=base_receipt,kind=system.doc["kind"],eta=args.eta)
        binding=emit(args.out/"input-binding.json",system.binding)
        arrays=Arrays(args.out/"large-arrays",engine.np)
        deadline=started+args.budget_seconds
        qr=GeneralRobinQR(system,engine,args.eta,arrays,deadline,args.max_factor_bytes)
        report["factorization"]=qr.report
        qr.factorize()
        z,delta=qr.solve()
        report["readback"]=qr.numerical_readback(z,delta)
        if system.doc["kind"]=="correction":
            report["exact_original_readback"]=exact_direction_readback(system,delta,args.out,deadline)
            report["delta"]=qr.report["delta"]
        else:
            report["cut_sensitivity"]=arrays.save("complete-cut-sensitivity",delta[0],
                "All 2M cut coordinates differentiated with respect to every physical height column")
            report["complete_all_node_sensitivity"]=qr.report["delta"]
        report.update(completed=True,input_binding_file=binding,
            output_array_manifest=emit(args.out/"array-manifest.json",dict(
                schema="current-C-complete-M-general-chain-arrays-v1",arrays=arrays.entries)),
            complete_factors=qr.factors,exact_saved_matrix_nonresonance_certified=False)
        exit_code=0
    except Exception as error:
        report.update(failed=True,error_type=type(error).__name__,error=str(error),
            reason_scope="actual linear computation or resource/binding failure; no native acceptance result inferred")
        if qr is not None:
            report["complete_factors"] = qr.factors
            report["completed_factor_nodes"] = [item["node"] for item in qr.factors]
            report["pending_factor_nodes"] = list(range(len(qr.factors),D+1))
            report["complete_factorization_completed"] = qr.complete
        if arrays is not None and not (args.out/"array-manifest.json").exists():
            report["output_array_manifest"] = emit(args.out/"array-manifest.json",dict(
                schema="current-C-complete-M-general-chain-arrays-v1",arrays=arrays.entries,
                partial=True,all_existing_saved_array_descriptors_retained=True))
    finally:
        report["elapsed_seconds"]=time.monotonic()-started
        result=emit(args.out/"result.json",report)
        print(json.dumps(dict(event="current_C_general_chain_result",result=result,
            completed=report["completed"],failed=report["failed"],kind=report.get("kind"),
            all_rhs=report.get("factorization",{}).get("right_hand_side_columns"))),flush=True)
    return exit_code


if __name__=="__main__":
    raise SystemExit(main())
