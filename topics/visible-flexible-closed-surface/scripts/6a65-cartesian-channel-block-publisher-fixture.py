#!/usr/bin/env python3
"""Local bare-Git fixture for the new same-model scalar publisher.

No repository network, numerical source, Actions identity, or scientific
acceptance is asserted. A competing local clone creates a real nonfastforward
and HANDOFF conflict between the actual pull and push.
"""
import argparse,hashlib,importlib.util,json,os
from pathlib import Path
import subprocess,sys,time

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("cartesian_local_publisher_fixture",HERE/"6a65-actions-cartesian-channel-block-v5-20261126.py")
module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module)
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def git(folder,*args):
    r=subprocess.run(["git",*args],cwd=folder,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    if r.returncode:raise RuntimeError(r.stdout)
    return r.stdout.strip()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory",type=Path,required=True)
    args=parser.parse_args();root=args.directory.resolve()
    if root.exists():raise FileExistsError("Fresh local-only Git fixture directory required")
    root.mkdir(parents=True);start=time.monotonic()
    bare=root/"remote.git";git(root,"init","--bare","--initial-branch=main",str(bare))
    seed=root/"seed";git(root,"clone",str(bare),str(seed))
    for repo in [seed]:
        git(repo,"config","user.name","Explicit local fixture")
        git(repo,"config","user.email","local-fixture@example.invalid")
    topic=module.TOPIC
    (seed/topic/"notes").mkdir(parents=True)
    (seed/"README.md").write_text("Local fixture root rules\n")
    (seed/topic/"README.md").write_text("Local fixture topic rules\n")
    (seed/module.HANDOFF).write_text("# Local fixture HANDOFF\nRoot-owned text.\n")
    (seed/topic/"notes"/"seed.txt").write_text("Only a local test.\n")
    git(seed,"add",".");git(seed,"commit","-m","local fixture seed");git(seed,"push","origin","main")
    worker=root/"worker";competitor=root/"competitor"
    for folder in (worker,competitor):
        git(root,"clone",str(bare),str(folder))
        git(folder,"config","user.name","Explicit local fixture")
        git(folder,"config","user.email","local-fixture@example.invalid")
    obj=module.Controller.__new__(module.Controller)
    obj.repo=worker;obj.out=root/"raw";obj.out.mkdir()
    obj.git_env=os.environ.copy();obj.run_id="local-fixture";obj.attempt="1"
    obj.last_rules=git(worker,"rev-parse","HEAD");obj.last_sync=time.monotonic()
    obj.total_pull_count=0;obj.own_count=obj.attempt_count=0
    obj.parent_state=obj.parent_observer=None
    obj.report=worker/topic/"notes"/"local-publisher-fixture.json"
    obj.receipt=obj.out/"local-scalar.json"
    obj.record=dict(schema="explicit-local-bare-Git-publisher-interface-fixture",
        state="local-only-publication-test",pulls=[],actualCauchySourceConsumed=False,
        completeLMAcceptances=0,notAnActionsRun=True)
    real_git=obj.git;injected=[]
    def wrapped(*args,**kwargs):
        if args and args[0]=="push" and not injected:
            p=competitor/module.HANDOFF
            p.write_text("# Local fixture HANDOFF\nCompeting root-owned replacement.\n")
            git(competitor,"add",str(module.HANDOFF))
            git(competitor,"commit","-m","local competing root edit")
            git(competitor,"push","origin","main")
            injected.append(git(competitor,"rev-parse","HEAD"))
        return real_git(*args,**kwargs)
    obj.git=wrapped
    obj.save("local-only-publication-test")
    obj.publish("actual local conflict fixture")
    remote=git(bare,"rev-parse","refs/heads/main")
    local=git(worker,"rev-parse","HEAD")
    content=(worker/module.HANDOFF).read_text()
    preserved="Competing root-owned replacement." in content
    own=content.count(module.MARKER)==1
    clean=git(worker,"status","--porcelain")==""
    permission_rejected=not module.concurrent_ref("remote: permission denied; [remote rejected] main -> main (protected branch)")
    network_rejected=not module.concurrent_ref("fatal: unable to access origin: Could not resolve host")
    foreign_lock_rejected=not module.concurrent_ref("remote: cannot lock ref 'refs/heads/main': Permission denied")
    first_pull_count=len(obj.record["pulls"])
    git(competitor,"pull","--rebase","origin","main")
    duplicated=(competitor/module.HANDOFF).read_text()
    own_lines=[line for line in duplicated.splitlines(keepends=True) if line.startswith(module.MARKER)]
    if len(own_lines)!=1:raise AssertionError("Exactly one prior receipt required before real duplicate injection")
    (competitor/module.HANDOFF).write_text(duplicated+own_lines[0])
    git(competitor,"add",str(module.HANDOFF))
    git(competitor,"commit","-m","local actual identical own marker duplication")
    git(competitor,"push","origin","main")
    duplicate_commit=git(competitor,"rev-parse","HEAD")
    obj.save("local-only-real-identical-marker-repair")
    obj.publish("actual local identical marker repair fixture")
    repaired=(worker/module.HANDOFF).read_text()
    duplicate_repaired=(repaired.count(module.MARKER)==1 and duplicate_commit in repaired and
        "Competing root-owned replacement." in repaired and
        obj.record["identicalOwnMarkerRepairs"][-1]["removedCount"]==1 and
        git(bare,"rev-parse","refs/heads/main")==git(worker,"rev-parse","HEAD"))
    git(competitor,"pull","--rebase","origin","main")
    (competitor/"README.md").write_text("Local fixture root rules\nA new explicit fixture rule.\n")
    git(competitor,"add","README.md");git(competitor,"commit","-m","local README rule change")
    git(competitor,"push","origin","main")
    changed_commit=git(competitor,"rev-parse","HEAD")
    obj.save("local-only-changed-rules-fixture")
    raised=False
    try:obj.publish("actual local changed-rule fixture")
    except module.RulesChanged:raised=True
    changed_handoff=(worker/module.HANDOFF).read_text()
    changed_recorded=(raised and changed_commit in changed_handoff and "未审" in changed_handoff and
        obj.record["pulls"][-1]["readmeDiffEmpty"] is False and
        git(bare,"rev-parse","refs/heads/main")==git(worker,"rev-parse","HEAD"))
    verified=remote==local and preserved and own and clean and first_pull_count==2 and permission_rejected and network_rejected and foreign_lock_rejected and changed_recorded and duplicate_repaired
    report=dict(schema="6a65-channel-block-local-bare-Git-identical-marker-repair-fixture-v1",
        controllerSHA256=sha(HERE/"6a65-actions-cartesian-channel-block-v5-20261126.py"),
        fixtureSHA256=sha(__file__),actualPullCount=len(obj.record["pulls"]),nonfastforwardCaseActualPullCount=first_pull_count,
        changedREADMEPullRecordedInHANDOFFAndPublishedBeforeStop=bool(changed_recorded),
        actualIdenticalMarkerDuplicateInjected=True,
        identicalDuplicateRemovedAndNewPullReceiptPublished=bool(duplicate_repaired),
        duplicateUpstreamCommit=duplicate_commit,
        identicalOwnMarkerRepairs=obj.record["identicalOwnMarkerRepairs"],
        realConcurrentLocalPushInjected=True,remoteEqualsActualWorkerHEAD=remote==local,
        unrelatedRootHANDOFFTextPreserved=preserved,exactlyOneOwnMarker=own,worktreeClean=clean,
        permissionNotRetriedAsNFF=permission_rejected,networkNotRetriedAsNFF=network_rejected,
        permissionLockNotRetriedAsNFF=foreign_lock_rejected,localBareOnly=True,
        actualCauchySourceConsumed=False,completeLMAcceptances=0,verified=bool(verified),
        seconds=time.monotonic()-start)
    output=root/"report.json";output.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report),flush=True)
    if not verified:raise AssertionError("Actual local publication fixture failed")
if __name__=="__main__":main()
