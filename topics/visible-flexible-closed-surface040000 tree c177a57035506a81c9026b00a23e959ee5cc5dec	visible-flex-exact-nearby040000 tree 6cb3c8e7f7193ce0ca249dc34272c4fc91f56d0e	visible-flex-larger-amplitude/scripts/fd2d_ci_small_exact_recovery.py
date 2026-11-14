#!/usr/bin/env python3
"""Execute one small exact recovery calculation and publish its actual result.

Only stdlib, selected already committed files, and ordinary terminal Git are
used. Every pull is immediately followed by both README comparisons.
No user credential is embedded. This source has not yet been executed.
"""
from __future__ import annotations
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import time

TOPIC = "topics/visible-flexible-closed-surface/"
H = TOPIC + "HANDOFF.md"
PUBLISHER = TOPIC + "scripts/fd2d_publish_rebase_checkpoint.py"
CHECKER = "scripts/fd2d-metric-delta7-island-removal-threshold.py"
ROWS = "notes/2026-11-12-fd2d-metric-dyadic34-signed-trace-windows-R182-01-rows.json.gz"
CERT = "notes/2026-11-12-fd2d-metric-dyadic34-signed-trace-windows-R182-01-report.json"

def git(args, data=None, check=True):
    r = subprocess.run(["git", *args], input=data, capture_output=True)
    if check and r.returncode:
        raise RuntimeError(r.stdout.decode(errors="replace") + r.stderr.decode(errors="replace"))
    return r

def text(ref, path):
    return git(["show", ref + ":" + path]).stdout.decode()

def write_blob(data):
    return git(["hash-object", "-w", "--stdin"], data).stdout.decode().strip()

def identity(path):
    raw=path.read_bytes()
    return dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--scratch", type=Path, required=True)
    ap.add_argument("--run-id", required=True)
    args=ap.parse_args()
    if not re.fullmatch(r"[0-9]+", args.run_id):
        raise ValueError("Expected an actual workflow run ID")
    args.scratch.mkdir(parents=True, exist_ok=False)
    initial=git(["rev-parse", "origin/main"]).stdout.decode().strip()
    h=text(initial,H)
    old=re.search(r"`([0-9a-f]{40})`",h.split("## 2.",1)[1].split("## 3.",1)[0]).group(1)
    if git(["cat-file","-e",old+"^{commit}"],check=False).returncode:
        git(["fetch","--filter=blob:none","--depth=1","origin",old])
    pulled=git(["pull","--rebase","--no-stat","origin","main"],check=False)
    current=git(["rev-parse","origin/main"]).stdout.decode().strip()
    diff=git(["diff",old,current,"--","README.md",TOPIC+"README.md"]).stdout.decode()
    first=dict(command="git pull --rebase --no-stat origin main",
               exit=pulled.returncode,readme_previous=old,readme_current=current,
               readme_diff_empty=not bool(diff),utc=dt.datetime.now(dt.timezone.utc).isoformat())
    print(json.dumps(first),flush=True)
    if diff:
        print(diff,flush=True)
        return 78
    if pulled.returncode:
        print(pulled.stdout.decode(errors="replace")+pulled.stderr.decode(errors="replace"),flush=True)
        return pulled.returncode
    h=text(current,H)
    work=args.scratch/"topic"
    for relative in (CHECKER,ROWS,CERT):
        p=work/relative;p.parent.mkdir(parents=True,exist_ok=True)
        p.write_bytes(git(["show",current+":"+TOPIC+relative]).stdout)
    out_name="2026-11-12-fd2d-metric-delta7-island-removal-ci-"+args.run_id
    output=work/"notes"/(out_name+"-report.json")
    command=[sys.executable,CHECKER,"--output","notes/"+output.name]
    started=dt.datetime.now(dt.timezone.utc).isoformat();tic=time.monotonic()
    child=subprocess.run(command,cwd=work,capture_output=True,text=True)
    receipt=dict(schema="fd2d-actual-small-recovery-execution-v1",
                 actual_workflow_run_id=args.run_id,source_commit=current,
                 initial_terminal_pull=first,command=command,
                 started_utc=started,ended_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                 seconds=time.monotonic()-tic,actual_child_returncode=child.returncode,
                 stdout=child.stdout,stderr=child.stderr,
                 checker=identity(work/CHECKER),rows=identity(work/ROWS),
                 certificate=identity(work/CERT),
                 full_field_F_J_BVP_or_body_evaluated=False)
    print(json.dumps(receipt),flush=True)
    files={}
    if output.exists():
        raw=output.read_bytes()
        receipt["output"]=dict(path=TOPIC+"notes/"+output.name,
                              bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
        files[TOPIC+"notes/"+output.name]=raw
    receipt_path=TOPIC+"notes/"+out_name+"-actual-execution.json"
    files[receipt_path]=(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n").encode()
    if child.returncode==0:
        report=json.loads(output.read_text())
        threshold=report["sufficient_delta7_lower"]["display"]
        feasible=report["increase_only_and_under_original_cap_feasible"]
        status=(f"δ7全89盒准确充分阈值已在CI实际0：{threshold:.17g}；"
                f"原.08盒内增量可行={feasible}。来源/准确分数/真实退出见notes/{out_name}-report.json及actual-execution；"
                "只属新g设计充分条件，无新F/J/BVP/accepted。")
    else:
        status=(f"δ7阈值CI实际child exit{child.returncode}，真实stdout/stderr见notes/{out_name}-actual-execution.json；"
                "未宣称阈值或几何成功，继续修复。")
    h=re.sub(r"δ7-only消正K孤岛的89盒阈值尚未实算[^\n]*",status,h,count=1)
    # Keep the existing publisher's exact rule-checkpoint syntax.
    h=re.sub(r"下次实际pull不晚于[0-9:]+", "下次pull不晚于22:36 UTC", h,count=1)
    if len(h.encode())>=10000:raise ValueError("HANDOFF exceeds 10KB")
    entries=[["100644",write_blob(raw),path] for path,raw in sorted(files.items())]
    entries.append(["100644",write_blob(h.encode()),H])
    snapshot=args.scratch/"snapshot.json"
    snapshot.write_text(json.dumps(dict(
        message="Compute the exact delta7 island-removal threshold and preserve its actual receipt",
        base_commit=current,handoff=h,entries=entries),ensure_ascii=False,indent=2)+"\n")
    publisher=args.scratch/"publisher.py";publisher.write_text(text(current,PUBLISHER))
    result=subprocess.run([sys.executable,str(publisher),"--snapshot",str(snapshot),
        "--receipt",str(args.scratch/"main-published.json"),
        "--attempt-log",str(args.scratch/"pull-and-push-history.jsonl")])
    if (args.scratch/"main-published.json").exists():
        print((args.scratch/"main-published.json").read_text(),flush=True)
    return result.returncode or child.returncode

if __name__=="__main__":
    sys.exit(main())
