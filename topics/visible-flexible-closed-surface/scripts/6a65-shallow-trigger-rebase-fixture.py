#!/usr/bin/env python3
"""Reproduce a stale exact-trigger shallow checkout, then the history fix.

Only disposable local Git repositories are used. No mathematical source,
public repository, credential, network, baseline or acceptance is touched.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import time

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--directory",type=Path,required=True)
    args=ap.parse_args();out=args.directory.resolve()
    if out.exists():raise FileExistsError("Fresh local Git fixture required")
    out.mkdir(parents=True);started=time.monotonic()
    def git(folder,*args,check=True):
        p=subprocess.run(["git",*args],cwd=folder,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        if check and p.returncode:raise RuntimeError(p.stdout)
        return p
    origin=out/"origin.git";git(out,"init","--bare","--initial-branch=main",str(origin))
    writer=out/"writer";git(out,"clone",str(origin),str(writer))
    for folder in (writer,):
        git(folder,"config","user.name","Local shallow fixture")
        git(folder,"config","user.email","local-fixture@example.invalid")
    def advance(text):
        (writer/"shared.txt").write_text(text+"\n")
        git(writer,"add","shared.txt");git(writer,"commit","-m",text);git(writer,"push","origin","main")
        return git(writer,"rev-parse","HEAD").stdout.strip()
    base=advance("base")
    trigger=advance("trigger-source")
    before_clone=advance("remote-concurrent-before-clone")
    def checkout(name,unshallow):
        clone=out/name
        git(out,"clone","--depth=1","file://"+str(origin),str(clone))
        git(clone,"fetch","--depth=1","origin",trigger)
        git(clone,"checkout","--detach",trigger)
        git(clone,"config","user.name","Local shallow fixture")
        git(clone,"config","user.email","local-fixture@example.invalid")
        if unshallow:
            if git(clone,"rev-parse","--is-shallow-repository").stdout.strip()!="true":raise AssertionError("Fixture must begin shallow")
            git(clone,"fetch","--unshallow","origin","main")
            if git(clone,"rev-parse","--is-shallow-repository").stdout.strip()!="false":raise AssertionError("History remains shallow")
            git(clone,"merge-base","--is-ancestor",trigger,"origin/main")
            if git(clone,"rev-parse","HEAD").stdout.strip()!=trigger:raise AssertionError("Unshallow changed frozen trigger")
        (clone/"scalar.json").write_text('{"actualAttemptCount":0}\n')
        git(clone,"add","scalar.json");git(clone,"commit","-m","local-scalar-only")
        return clone
    bad=checkout("shallow",False)
    after_clone=advance("remote-concurrent-after-clone")
    failure=git(bad,"pull","--rebase","origin","main",check=False)
    (out/"actual-shallow-failure.log").write_text(failure.stdout)
    if failure.returncode==0 or "could not apply" not in failure.stdout or "CONFLICT" not in failure.stdout:
        raise AssertionError("The precise stale-trigger shallow rebase failure was not reproduced")
    good=checkout("unshallowed",True)
    latest=advance("remote-concurrent-after-unshallow")
    success=git(good,"pull","--rebase","origin","main")
    (out/"actual-unshallow-rebase.log").write_text(success.stdout)
    if (good/"shared.txt").read_text()!="remote-concurrent-after-unshallow\n":raise AssertionError("Remote text was overwritten")
    if (good/"scalar.json").read_text()!='{"actualAttemptCount":0}\n':raise AssertionError("Own scalar was lost")
    if git(good,"rev-list","--count","origin/main..HEAD").stdout.strip()!="1":raise AssertionError("Trigger tree was replayed as a local commit")
    git(good,"push","origin","HEAD:main")
    pushed=git(good,"rev-parse","HEAD").stdout.strip()
    if git(out,"--git-dir",str(origin),"rev-parse","main").stdout.strip()!=pushed:raise AssertionError("Actual ordinary local push did not succeed")
    report=dict(schema="6a65-stale-trigger-shallow-history-rebase-fixture-v1",fixtureSHA256=sha(__file__),
        rootCause="depth-one clone at newer main plus depth-one fetch of older trigger leaves disconnected shallow ancestry",
        syntheticCommits=dict(base=base,trigger=trigger,beforeClone=before_clone,afterClone=after_clone,latest=latest,pushed=pushed),
        originalActualRebaseExit=failure.returncode,actualFailureLogSHA256=sha(out/"actual-shallow-failure.log"),
        repairedActualRebaseExit=success.returncode,actualSuccessLogSHA256=sha(out/"actual-unshallow-rebase.log"),
        exactTriggerRetainedDuringHistoryFetch=True,remoteTextPreserved=True,onlyOwnScalarCommitRebased=True,
        ordinaryLocalPushSucceeded=True,publicRepositoryTouched=False,
        numericalStagesExecuted=0,acceptedMathematicalSteps=0,seconds=time.monotonic()-started)
    result=out/"report.json";result.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(dict(report=str(result),reportSHA256=sha(result),**{k:report[k] for k in
        ("originalActualRebaseExit","repairedActualRebaseExit","ordinaryLocalPushSucceeded","seconds")})))
if __name__=="__main__":main()

