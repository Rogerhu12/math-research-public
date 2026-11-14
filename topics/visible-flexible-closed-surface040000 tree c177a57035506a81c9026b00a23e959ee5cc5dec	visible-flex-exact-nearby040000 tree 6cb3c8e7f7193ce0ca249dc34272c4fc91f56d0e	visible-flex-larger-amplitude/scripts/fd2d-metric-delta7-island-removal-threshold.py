"""Exact delta7-only removal threshold from already certified R182 rows.

This source was first saved during an unavailable executor interval.
It has not yet been run. It reads the existing continuous interval packet;
it does not evaluate F/J, a body, an ODE, or even new profile intervals.

On each saved box I, base_a_ss >= b and psi7'' >= B>0, while the
other six second derivatives vanish. Therefore every delta7 >= -b/B
has a_ss >=0 on I. The maximum is a rigorous sufficient threshold.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import time

ROWS_SHA256="d7f990bcef75ec30311e23d3cf92dadf5736f871f141dd3f7fa62071f7793095"
REPORT_SHA256="44d3d9318ffa7b70f7bcc59cebf81df09e72b9c37562c05e1410cdb65b627a68"


def identity(path):
    path=Path(path);raw=path.read_bytes()
    return dict(path=str(path),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def ratio(value):
    return F(int(value[0]),int(value[1]))


def binary(value):
    m,e=int(value[0]),int(value[1])
    return F(m*(1<<e),1) if e>=0 else F(m,1<<(-e))


def record(q):
    return dict(exact=[str(q.numerator),str(q.denominator)],display=float(q))


def read_bound(row,side):
    return binary(row[side+"_binary"])


def run(args):
    started=time.monotonic()
    if args.output.exists():
        raise FileExistsError("Use a new output path; do not replace a previous result")
    rid=identity(args.rows);cid=identity(args.certificate)
    if rid["sha256"]!=ROWS_SHA256 or cid["sha256"]!=REPORT_SHA256:
        raise ValueError("The exact already-certified R182 inputs changed")
    rows_packet=json.loads(gzip.decompress(args.rows.read_bytes()))
    certificate=json.loads(args.certificate.read_text())
    if not certificate["passed"]:
        raise ValueError("The input continuous certificate did not pass")
    if rows_packet["actual_field"]!=certificate["actual_field"]:
        raise ValueError("The rows and certificate bind different actual fields")
    rows=rows_packet["rows"]["late_negative"]
    window=next(w for w in certificate["windows"] if w["name"]=="late_negative")
    if len(rows)!=window["exact_cover_rows"] or len(rows)!=89:
        raise ValueError("The full original 89-box cover is required")
    left=ratio(window["endpoints"][0]["exact"])
    right=ratio(window["endpoints"][3]["exact"])
    previous=left;threshold=F(0);worst=None;reduced=[]
    for row in rows:
        a,b=map(ratio,row["interval"])
        if a!=previous or not a<b:
            raise ValueError("The original continuous cover has a gap, overlap, or wrong order")
        previous=b
        if any(read_bound(v,"lower")!=0 or read_bound(v,"upper")!=0
               for v in row["second_derivative_basis"][:6]):
            raise ValueError("Another profile second derivative acts on this box")
        B=read_bound(row["second_derivative_basis"][6],"lower")
        base=read_bound(row["base_a_ss"],"lower")
        if B<=0:
            raise ValueError("A strictly positive psi7-second lower bound is required")
        t=max(F(0),-base/B)
        reduced.append((row["index"],a,b,base,B,t))
        if t>threshold:
            threshold=t;worst=(row["index"],a,b,base,B)
    if previous!=right:
        raise ValueError("The right endpoint of the continuous support is uncovered")
    current=ratio(certificate["center_delta_exact"][6])
    cap=F.from_float(.08)
    required=max(threshold,current)
    feasible=required<=cap
    candidate=None;minimum_margin=None
    if feasible:
        # One extra millionth above the exact ceiling gives a strict
        # positive margin unless the original cap itself is necessary.
        units=(required.numerator*1000000+required.denominator-1)//required.denominator
        candidate=min(cap,F(units+1,1000000))
        if candidate<required:
            raise AssertionError("The chosen exact witness is below its sufficient threshold")
        minimum_margin=min(base+candidate*B for _,_,_,base,B,_ in reduced)
        if minimum_margin<0:
            raise AssertionError("An exact nonnegative a_ss witness failed")
    support_right=ratio(certificate["bump_supports_exact"][6][1])
    terminal_start=F.from_float(certificate["unchanged_terminal_window"]["start"])
    if support_right!=terminal_start:
        raise ValueError("The changed compact bump must end at the protected terminal start")
    global_radius=ratio(certificate["exact_global_radius_lower"]["exact"])
    if global_radius<=0:
        raise ValueError("The original global radius lower bound was not positive")
    out=dict(schema="fd2d-R182-delta7-only-island-removal-exact-threshold-v1",
        source=identity(__file__),rows=rid,certificate=cid,
        actual_origin=certificate["actual_field"],
        physical_profile_changed_if_witness_selected=True,
        exact_original_target_interval=[record(left),record(right)],
        endpoint_semantics="the saved R182 exact dyadic support, decimal labels 1.423 and 1.445",
        original_box_count=len(rows),
        all_other_second_derivative_bases_identically_zero_on_cover=True,
        psi7_second_continuously_strictly_positive=True,
        minimum_saved_psi7_second_lower=record(min(x[4] for x in reduced)),
        sufficient_delta7_lower=record(threshold),
        old_delta7=record(current),original_binary64_parameter_cap=record(cap),
        increase_only_and_under_original_cap_feasible=feasible,
        selected_exact_witness=None if candidate is None else record(candidate),
        selected_uniform_a_ss_lower=None if minimum_margin is None else record(minimum_margin),
        maximum_threshold_row=None if worst is None else dict(index=worst[0],
            interval=[record(worst[1]),record(worst[2])],base_a_ss_lower=record(worst[3]),
            psi7_second_lower=record(worst[4])),
        old_global_radius_lower=record(global_radius),
        witness_global_radius_lower=None if candidate is None else record(global_radius),
        radius_reason="psi7=1024*t^5*(1-t)^5 on [0,1], zero outside; increasing delta7 increases a pointwise",
        unchanged_protected_terminal_start=record(terminal_start),
        protected_terminal_g_and_K_unchanged=True,
        terminal_reason="the compact C4 bump and its derivatives through order four vanish at and beyond its exact right support endpoint",
        field_F_J_BVP_body_or_new_profile_intervals_evaluated=False,
        whole_new_geometry_or_solver_success_claimed=False,
        sufficient_threshold_not_claimed_optimal=True,
        seconds=time.monotonic()-started)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2,allow_nan=False)+"\n")
    print(json.dumps(dict(output=str(args.output),threshold=float(threshold),
        feasible=feasible,witness=None if candidate is None else float(candidate),
        a_ss_lower=None if minimum_margin is None else float(minimum_margin)),
        allow_nan=False))


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rows",type=Path,default=Path(
        "notes/2026-11-12-fd2d-metric-dyadic34-signed-trace-windows-R182-01-rows.json.gz"))
    parser.add_argument("--certificate",type=Path,default=Path(
        "notes/2026-11-12-fd2d-metric-dyadic34-signed-trace-windows-R182-01-report.json"))
    parser.add_argument("--output",type=Path,required=True)
    run(parser.parse_args())
