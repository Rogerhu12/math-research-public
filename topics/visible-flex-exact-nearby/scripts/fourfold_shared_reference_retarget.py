#!/usr/bin/env python3
"""Define a new target reference by exact symbolic initial-value correction.

Old U/L coefficients remain untouched. A degree-seven Bernstein/Fourier
polynomial Q is selected from exp(old dense L) values; no approximation-to-J
claim is made. Exact dyadic a=Hnew/4-Uold,start corrects the initial value.
Products Q*a are kept symbolic. All new-target ODE residuals remain unpaid.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import io
import json
from pathlib import Path

import numpy as np

from fourfold_shared_dense_reference import load


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def document(path):
    return json.loads(Path(path).read_text())


def reference_endpoints(path):
    doc=document(path)
    if (not doc.get("complete") or doc["time_basis"]!="bernstein"
        or doc["fields"]!=["U","L"] or doc["time_degree"]!=7):
        raise ValueError("complete U/L Bernstein reference required")
    previous=first=None;count=0
    for row in doc["shards"]:
        source=path.parent/row["path"]
        if sha(source)!=row["sha256"]:raise ValueError("base reference shard changed")
        data=load(source)
        values=data["coefficient_real"]+1j*data["coefficient_imag"]
        if row["start_segment"]!=count or values.shape!=(row["segment_count"],8,2,doc["Fourier_degree"]+1):
            raise ValueError("base reference shards do not tile correctly")
        for c in values:
            if previous is not None and not np.array_equal(previous,c[0]):
                raise ValueError("base reference is not exactly continuous")
            if first is None:first=c[0].copy()
            previous=c[-1].copy();count+=1
    if count!=doc["segment_count"]:raise ValueError("base reference is incomplete")
    return doc,first,previous


def dense_L(yold,F,z):
    value=np.zeros_like(yold)
    for j,coefficient in enumerate(F[::-1]):
        value=(value+coefficient)*(z if j%2==0 else 1-z)
    return value+yold


def construct_Q(reference,output,degree,per_file,source_hash):
    output.mkdir(parents=True)
    N=reference["total_initial_grid_nodes"]
    if not 0<=degree<N//2:raise ValueError("Q Fourier degree must be below Nyquist")
    index=0;previous=None;buffer=[];shards=[];start=0
    first_value=None;input_hashes=[]
    def save():
        nonlocal buffer,start
        if not buffer:return
        values=np.asarray(buffer,dtype=np.complex128)
        stream=io.BytesIO()
        metadata=dict(start_segment=start,segment_count=len(buffer),
                      exact_times=reference["exact_time_endpoints"][start:start+len(buffer)+1])
        np.savez(stream,coefficient_real=values.real,coefficient_imag=values.imag,
                 metadata=np.array(json.dumps(metadata,sort_keys=True)))
        payload=gzip.compress(stream.getvalue(),mtime=0)
        if len(payload)>5_000_000:raise ValueError("reduce Q shard length")
        path=output/f"segments_{start:05d}.npz.gz";path.write_bytes(payload)
        shards.append(dict(path=path.name,sha256=sha(path),bytes=len(payload),
                           start_segment=start,segment_count=len(buffer)))
        start+=len(buffer);buffer=[]
    for row in reference["input_traces"]:
        path=Path(row["path"])
        if sha(path)!=row["sha256"]:raise ValueError("old dense source changed")
        data=load(path);metadata=json.loads(str(data["metadata"]))
        if metadata["identity"]!=reference["trace_identity"]:
            raise ValueError("Q source is another old branch")
        if row["first_accepted_segment"]!=index:raise ValueError("old chunks are out of order")
        input_hashes.append(dict(path=str(path),sha256=row["sha256"]))
        for j in range(len(data["dense_h"])):
            left,right=data["accepted_tau"][j:j+2]
            controls=[]
            for ell in range(8):
                if ell in (0,7):
                    L=data["accepted_state"][j+(ell==7),1]
                else:
                    tau=left+(right-left)*(ell/7)
                    z=(tau-data["dense_t_old"][j])/data["dense_h"][j]
                    L=dense_L(data["dense_y_old"][j,1],data["dense_F"][j,:,1],z)
                q=np.exp(L)
                if not np.all(np.isfinite(q)):raise ValueError("nonfinite Q selection")
                coefficient=(np.fft.rfft(q)/N)[:degree+1]
                coefficient[0]=complex(coefficient[0].real,0.)
                controls.append(coefficient)
            controls=np.asarray(controls)
            if previous is None:
                controls[0]=0.;controls[0,0]=1.
                first_value=controls[0].copy()
            else:controls[0]=previous
            previous=controls[-1].copy();buffer.append(controls);index+=1
            if len(buffer)>=per_file:save()
    save()
    if index!=reference["segment_count"]:raise ValueError("Q branch is incomplete")
    # Re-read every final dyadic array; this checks the definition actually
    # written to disk, independently of the in-memory construction state.
    endpoint=None;checked=0
    for row in shards:
        data=load(output/row["path"])
        values=data["coefficient_real"]+1j*data["coefficient_imag"]
        for c in values:
            if endpoint is not None and not np.array_equal(c[0],endpoint):
                raise ValueError("saved Q lost an endpoint equality")
            endpoint=c[-1].copy();checked+=1
    if not (first_value[0]==1 and np.all(first_value[1:]==0) and checked==index):
        raise ValueError("Q initial constant/coverage gate failed")
    report=dict(kind="defined_dyadic_Fourier_Bernstein_Qtilde",complete=True,
        source_sha256=source_hash,leg=reference["leg"],Fourier_degree=degree,
        time_degree=7,time_basis="bernstein",fields=["Qtilde"],segment_count=index,
        total_initial_grid_nodes=N,exact_time_endpoints=reference["exact_time_endpoints"],
        coefficient_convention="positive Fourier coefficients; negative conjugates; exact binary64 dyadics",
        construction="eight exp(old dense L) selections form Bernstein controls; not interpolation claims; shared endpoint controls; first control polynomial exactly 1",
        initial_constant_one_proved=True,continuous_by_shared_endpoint_coefficients=True,
        input_traces=input_hashes,shards=shards,bytes_total=sum(x["bytes"] for x in shards),
        limitations=["Qtilde is a chosen correction propagator, not a certified Jacobian or exp(L) approximation."])
    path=output/"manifest.json";path.write_text(json.dumps(report,indent=2)+"\n")
    return path,report,first_value,previous


def exact_initial_correction(H,U,path):
    degree=max(int(H["H_degree"]),len(U)-1)
    scale=1<<int(H["denominator_power_of_two"])
    pairs=[]
    for k in range(degree+1):
        h=H["h_nonnegative_integer_coefficients"][k] if k<=H["H_degree"] else (0,0)
        u=U[k] if k<len(U) else 0j
        pairs.append([Fraction(int(h[0]),4*scale)-Fraction.from_float(float(u.real)),
                      Fraction(int(h[1]),4*scale)-Fraction.from_float(float(u.imag))])
    bits=max(v.denominator.bit_length()-1 for pair in pairs for v in pair)
    denominator=1<<bits
    integers=[]
    for pair in pairs:
        row=[]
        for v in pair:
            value=v*denominator
            if value.denominator!=1:raise ValueError("non-dyadic initial correction")
            row.append(str(value.numerator))
        integers.append(row)
    if int(integers[0][1]):raise ValueError("nonreal correction mean")
    for k,row in enumerate(integers):
        h=H["h_nonnegative_integer_coefficients"][k] if k<=H["H_degree"] else (0,0)
        u=U[k] if k<len(U) else 0j
        for j,value in enumerate((u.real,u.imag)):
            if Fraction.from_float(float(value))+Fraction(int(row[j]),denominator)!=Fraction(int(h[j]),4*scale):
                raise ValueError("exact initial Fourier identity failed")
    result=dict(kind="exact_dyadic_initial_angle_correction",degree=degree,
        denominator_power_of_two=bits,nonnegative_integer_coefficients=integers,
        definition="a(x)=h_target(x)/4-U_old_forward_start(x)",
        exact_coefficient_identity_proved=True)
    path.write_text(json.dumps(result,indent=2)+"\n")
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--forward-reference",type=Path,required=True)
    p.add_argument("--backward-reference",type=Path,required=True)
    p.add_argument("--target-object",type=Path,required=True)
    p.add_argument("--target-root",type=Path,required=True)
    p.add_argument("--target-H",type=Path,required=True)
    p.add_argument("--Q-degree",type=int,default=128)
    p.add_argument("--segments-per-file",type=int,default=48)
    p.add_argument("--out-dir",type=Path,required=True)
    args=p.parse_args()
    if args.out_dir.exists():raise ValueError("choose a fresh retarget definition directory")
    args.out_dir.mkdir(parents=True)
    source_hash=sha(__file__)
    forward,fs,fe=reference_endpoints(args.forward_reference)
    backward,bs,be=reference_endpoints(args.backward_reference)
    if not np.array_equal(fe[0],bs[0]):raise ValueError("old Y legs do not share the exact endpoint")
    for key in ("source_sha256","dyadic_conjugacy_sha256","root_certificate_sha256","exact_delta_fraction"):
        if forward["trace_identity"][key]!=backward["trace_identity"][key]:
            raise ValueError("mixed old objects")
    if forward["exact_time_endpoints"][-1]!=backward["exact_time_endpoints"][0]:
        raise ValueError("old turn times do not agree exactly")
    obj,root,H=map(document,(args.target_object,args.target_root,args.target_H))
    delta=Fraction(int(obj["delta_fraction"]["numerator"]),int(obj["delta_fraction"]["denominator"]))
    if (not root.get("proved") or Fraction(root["exact_delta_fraction"])!=delta
        or root["origin_inputs_sha256"]!=obj["origin_inputs"]["sha256"]
        or root["frozen_direction_sha256"]!=obj["direction"]["sha256"]
        or Fraction(H["source_metadata"]["exact_delta_fraction"])!=delta):
        raise ValueError("target object/root/H identity mismatch")
    if (forward["trace_identity"]["origin_inputs_sha256"]!=obj["origin_inputs"]["sha256"]
        or forward["trace_identity"]["curve_direction_sha256"]!=obj["direction"]["sha256"]):
        raise ValueError("old and new objects are different affine families")
    qf,qfm,qfs,qfe=construct_Q(forward,args.out_dir/"Q_forward",args.Q_degree,args.segments_per_file,source_hash)
    qb,qbm,qbs,qbe=construct_Q(backward,args.out_dir/"Q_backward",args.Q_degree,args.segments_per_file,source_hash)
    a_path=args.out_dir/"initial_correction.json"
    a=exact_initial_correction(H,fs[0],a_path)
    ref=lambda path:dict(path=str(path),sha256=sha(path))
    descriptor=dict(kind="symbolic_continuous_reference_retarget_definition",complete=True,
        source_sha256=source_hash,definition_only_not_true_flow=True,
        old_exact_delta_fraction=forward["trace_identity"]["exact_delta_fraction"],
        target_exact_delta_fraction=str(delta),exact_parameter_step=str(delta-Fraction(forward["trace_identity"]["exact_delta_fraction"])),
        old_forward_reference=ref(args.forward_reference),old_backward_reference=ref(args.backward_reference),
        target_object=ref(args.target_object),target_root=ref(args.target_root),target_H=ref(args.target_H),
        Q_forward=ref(qf),Q_backward=ref(qb),initial_correction=ref(a_path),
        formulas=dict(forward="Y5f=x/4+U4f+Qf*a; L5f=L4f",
                      backward="Y5b=x/4+U4b+Qb*(Qf,end*a); L5b=L4b",
                      time_coordinate="each segment uses its saved exact rational/pi endpoints",
                      parameter_correction="no Z correction; the actual change of target field must be paid by fresh residual verification"),
        proof_gates=dict(exact_initial_H_over_four=True,old_intra_leg_U_L_continuity=True,
            Q_intra_leg_continuity=True,Q_leg_initial_values_exactly_one=True,
            exact_forward_backward_Y_junction=True),
        symbolic_product_only=True,
        limitations=["The original delta4 traces and the target delta5 graph remain distinct immutable inputs.",
            "No Q approximation accuracy or positivity is asserted; q for flow bounds is still exp(old L).",
            "Fresh true target e0/e1, denominators, complex image, all target spline germs, parameter sources and full time/angle coverage remain unpaid.",
            "The old numerical knot mesh is a reference choice; it does not change or certify target radial knot locations."])
    out=args.out_dir/"descriptor.json";out.write_text(json.dumps(descriptor,indent=2)+"\n")
    print(json.dumps(dict(descriptor=str(out),sha256=sha(out),proof_gates=descriptor["proof_gates"],
        Q_bytes=qfm["bytes_total"]+qbm["bytes_total"],initial_correction_degree=a["degree"],
        initial_correction_denominator_bits=a["denominator_power_of_two"])),flush=True)


if __name__=="__main__":main()
