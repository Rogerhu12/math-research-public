#!/usr/bin/env python3
"""Strict continuation of a saved actual far-collar rectangle queue.

The unchanged Cover.evaluate and unchanged subdivision rule are used.
Accepted rectangles plus pending rectangles must exactly tile the original
domain before any new native interval evaluation is started.
"""
from __future__ import annotations
import argparse,ctypes,gc,gzip,json,time
from collections import deque
from fractions import Fraction as F
from pathlib import Path
from flint import ctx
from fourfold_phase_beta_parameter_germ import provenance
from fourfold_phase_canonical_collar_far_cover import Cover,sha


def read(path):
    with gzip.open(path,"rt") as f:return json.load(f)


def verify_cover(report,pending,knots):
    intervals=[]
    bounds=set()
    for row in report["cells"]:
        l,r=map(F,row["exact_quarter_interval"])
        a,b=map(F,row["exact_physical_radial_interval"])
        sp=tuple(map(F,row["exact_scalar_span"]))
        intervals.append((l,r,a,b,sp))
    intervals += [(l,r,a,b,sp) for l,r,a,b,sp,ad,rd in pending]
    left,right=map(F,report["exact_radial_range"])
    lo=F(report["first_cell"],report["angle_cells"])
    hi=F(report["last_cell"],report["angle_cells"])
    actual_spans=set(zip(knots,knots[1:]))
    for l,r,a,b,sp in intervals:
        if not lo<=l<r<=hi or not left<=a<b<=right:
            raise ValueError("saved actual rectangle is outside its domain")
        if sp not in actual_spans or not sp[0]<=a<b<=sp[1]:
            raise ValueError("saved actual scalar selector is not a genuine common span")
        bounds.update((a,b))
    bounds=sorted(bounds)
    if not bounds or bounds[0]!=left or bounds[-1]!=right:
        raise ValueError("saved actual radial endpoints differ")
    for a,b in zip(bounds,bounds[1:]):
        cursor=lo
        for l,r in sorted((l,r) for l,r,c,d,sp in intervals if c<=a<b<=d):
            if l!=cursor:raise ValueError("accepted plus pending cover has a gap/overlap")
            cursor=r
        if cursor!=hi:raise ValueError("saved actual angle slice is incomplete")


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--checkpoint",type=Path,required=True)
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args()
    if args.checkpoint.resolve()==args.out.resolve():
        raise ValueError("preserve the input partial and write a separate continuation")
    report=read(args.checkpoint)
    if report.get("proved") or report.get("failed_cells") or not report.get("pending"):
        raise ValueError("a nonfailed unfinished actual queue is required")
    if report["source_sha256"]!=sha(Path(__file__).with_name("fourfold_phase_canonical_collar_far_cover.py")):
        raise ValueError("original true evaluator source changed")
    for name,value in report["dependencies"].items():
        if sha(Path(__file__).with_name(name))!=value:
            raise ValueError("original true dependency changed: "+name)
    object_path=Path(report["object"]["center_object_path"])
    if sha(object_path)!=report["object"]["center_object_sha256"]:
        raise ValueError("saved exact affine object changed")
    root_path=Path("data/phase_ring_continuation/type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json")
    if sha(root_path)!=report["root_certificate_sha256"]:
        raise ValueError("saved true moving root changed")
    # These were the original command's defaults, preserved in the task
    # checkpoint; no change to arithmetic precision or FFT node count.
    ctx.prec,ctx.cap=256,32
    settings=argparse.Namespace(object=object_path,half_width=F(report["object"]["exact_parameter_half_width"]),
       root_certificate=root_path,nodes=512)
    cover=Cover(settings)
    if provenance(cover.model.target,object_path)!=report["object"]:
        raise ValueError("resumed actual family/dependency provenance differs")
    pending=deque((F(l),F(r),F(a),F(b),tuple(map(F,sp)),int(ad),int(rd))
                  for l,r,a,b,sp,ad,rd in report["pending"])
    if any(not 0<=ad<=12 or not 0<=rd<=12 for l,r,a,b,sp,ad,rd in pending):
        raise ValueError("saved actual subdivision depth exceeds its original limit")
    verify_cover(report,pending,cover.model.knots)
    report.setdefault("continuations",[]).append(dict(
       source_sha256=sha(__file__),input_checkpoint_path=str(args.checkpoint),
       input_checkpoint_sha256=sha(args.checkpoint),
       verified_saved_accepted_cells=len(report["cells"]),verified_pending_rectangles=len(pending),
       exact_accepted_plus_pending_cover_verified=True,bits=256,nodes=512,max_depth=12,
       prior_session_exit_reason="unknown; old execution handle unavailable and saved mtime stopped"))
    previous=float(report.get("seconds",0));start=time.monotonic();libc=ctypes.CDLL(None)
    def save():
        report["seconds"]=previous+time.monotonic()-start
        report["pending"]=[[str(l),str(r),str(a),str(b),list(map(str,sp)),ad,rd]
                          for l,r,a,b,sp,ad,rd in pending]
        args.out.parent.mkdir(parents=True,exist_ok=True)
        tmp=args.out.with_suffix(args.out.suffix+".tmp")
        with gzip.open(tmp,"wt") as f:json.dump(report,f,indent=2);f.write("\n")
        tmp.replace(args.out)
    save()
    print(json.dumps({"resumed_exact_accepted":len(report["cells"]),"remaining":len(pending),
                      "joint_exact_cover_verified":True}),flush=True)
    while pending:
        l,r,a,b,sp,ad,rd=pending.popleft();report["attempts"]+=1
        try:
            row=cover.evaluate(l,r,a,b,sp)
            row.update(angle_depth=ad,radial_depth=rd);report["cells"].append(row)
        except (ValueError,ZeroDivisionError) as exc:
            if ad<12 and (ad<=rd+2 or rd>=12):
                mid=(l+r)/2
                pending.appendleft((mid,r,a,b,sp,ad+1,rd))
                pending.appendleft((l,mid,a,b,sp,ad+1,rd))
            elif rd<12:
                mid=(a+b)/2
                pending.appendleft((l,r,mid,b,sp,ad,rd+1))
                pending.appendleft((l,r,a,mid,sp,ad,rd+1))
            else:
                report["failed_cells"].append(dict(angle=list(map(str,(l,r))),
                    radial=list(map(str,(a,b))),reason=str(exc)))
                save();print(json.dumps({"unresolved":report["failed_cells"][-1]}),flush=True);return
        if report["attempts"]%16==0:
            save();gc.collect()
            if hasattr(libc,"malloc_trim"):libc.malloc_trim(0)
            print(json.dumps({"attempts":report["attempts"],"accepted":len(report["cells"]),
                             "pending":len(pending),"seconds":report["seconds"]}),flush=True)
    verify_cover(report,pending,cover.model.knots)
    report["proved"]=(report["first_cell"]==0 and
                     2*report["last_cell"]==report["angle_cells"] and not report["failed_cells"])
    report["covered_specified_range"]=True
    save()
    print(json.dumps({"proved":report["proved"],"cells":len(report["cells"]),
                      "seconds":report["seconds"],"report_sha256":sha(args.out)}),flush=True)


if __name__=="__main__":main()
