#!/usr/bin/env python3
"""Continue a real own Cartesian state in the same runner, with scalar pushes.

An upstream job must really produce the Cauchy source and original observer.
Optional own-state inputs must have been produced in this same run/epoch.
No raw output is fetched from a finished job, and no reported old hash is
substituted for an actual local file.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import re
import selectors
import subprocess
import sys
import time

TOPIC=Path("topics/visible-flexible-closed-surface")
HANDOFF=TOPIC/"HANDOFF.md"
RULES=[Path("README.md"),TOPIC/"README.md"]
MARKER="<!-- 6a65-cartesian-continuation-ci-rules -->"
ENTRY="6a65-cartesian-independent-experiment-v3.py"


def utc():return datetime.now(timezone.utc).isoformat(timespec="seconds")
def sha(path):
    digest=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for data in iter(lambda:stream.read(1048576),b""):digest.update(data)
    return digest.hexdigest()
def emit(event,**values):print(json.dumps(dict(event=event,**values),allow_nan=False),flush=True)
def write(path,value):Path(path).write_text(json.dumps(value,indent=2,allow_nan=False)+"\n")
def small_int(value,maximum=60):
    if type(value) is not int or not 1<=value<=maximum:raise ValueError("Explicit bounded positive attempt count required")
    return value
def concurrent_ref(message):
    return bool(re.search(r"non-fast-forward|fetch first|\[rejected\]|"
        r"cannot lock ref ['\"]refs/heads/main['\"][^\n]*(?:is at [0-9a-f]+ but expected [0-9a-f]+|incorrect old value provided)|"
        r"\[remote rejected\][^\n]*->\s*main\b[^\n]*(?:is at [0-9a-f]+ but expected [0-9a-f]+|incorrect old value provided)",message,re.I))
class RulesChanged(RuntimeError):pass


class Controller:
    def __init__(self,args):
        self.args=args
        self.repo=args.repo.resolve()
        self.out=args.out_dir.resolve()
        if self.out.exists() or self.out==self.repo or self.repo in self.out.parents:
            raise ValueError("A fresh Git-external output directory is required")
        self.out.mkdir(parents=True)
        self.run_id=os.environ.get("GITHUB_RUN_ID","")
        self.attempt=os.environ.get("GITHUB_RUN_ATTEMPT","")
        if (os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public" or
                not self.run_id.isdigit() or not self.attempt.isdigit()):
            raise ValueError("Actual authorized Actions run/attempt required")
        if not os.environ.get("CART_CONTINUATION_TOKEN"):
            raise ValueError("Explicit workflow credential CART_CONTINUATION_TOKEN required")
        self.git_env=os.environ.copy()
        self.git_env.update(GIT_TERMINAL_PROMPT="0",GIT_CONFIG_COUNT="2",
            GIT_CONFIG_KEY_0="credential.helper",GIT_CONFIG_VALUE_0="",
            GIT_CONFIG_KEY_1="credential.helper",
            GIT_CONFIG_VALUE_1='!f() { printf "username=x-access-token\\npassword=%s\\n" "$CART_CONTINUATION_TOKEN"; }; f')
        self.child_env={k:v for k,v in os.environ.items() if k not in
            ("GH_TOKEN","GITHUB_TOKEN","MR_TOKEN","VISIBLE_FLEX_TOKEN","M12_RECOVERY_TOKEN",
             "CART_COLD_TOKEN","CART_CONTINUATION_TOKEN") and not k.startswith("GIT_CONFIG_")}
        self.child_env.update(OPENBLAS_NUM_THREADS="1",OMP_NUM_THREADS="1")
        if self.git("rev-parse","--show-toplevel",capture=True).strip()!=str(self.repo):
            raise ValueError("Explicit actual Git checkout required")
        self.git("config","--local","user.name","Astra-visible-flex-6a65")
        self.git("config","--local","user.email","41898282+github-actions[bot]@users.noreply.github.com")
        self.git("switch","-c",f"visible-flex-Cartesian-{self.run_id}-{self.attempt}")
        self.epoch=args.source_epoch
        self.last_rules=args.rules_read_commit
        for value in (self.epoch,self.last_rules):
            if not re.fullmatch("[0-9a-f]{40}",value):raise ValueError("Full actual source and read-rules commits required")
            if self.git("cat-file","-e",value+"^{commit}",capture=True,check=False).returncode:
                self.git("fetch","--filter=blob:none","origin",value)
        self.scripts=args.scripts.resolve()
        if self.repo==self.scripts or self.repo in self.scripts.parents:
            raise ValueError("Numerical code must be a frozen snapshot outside changing Git")
        self.frozen=self.scripts.parents[2]
        if self.scripts!=self.frozen/TOPIC/"scripts":raise ValueError("Complete frozen topic layout required")
        self.candidate=args.candidate.resolve()
        self.source=args.source.resolve()
        self.original_observer=args.source_observer.resolve()
        self.recipe=args.recipe.resolve()
        for raw in (self.source,self.original_observer):
            if raw==self.repo or self.repo in raw.parents:raise ValueError("Actual raw sources must stay outside Git")
        self.source_hash,self.original_observer_hash=sha(self.source),sha(self.original_observer)
        self.candidate_hash,self.recipe_hash=sha(self.candidate),sha(self.recipe)
        original=json.loads(self.source.read_text())
        if original.get("schema") not in ("6a65-Cauchy-global-position-initial-v1","6a65-Cauchy-global-position-checkpoint-v1") or original.get("interfaceProbeOnly"):
            raise ValueError("Actual original Cauchy source required")
        self.original_count=original["cauchyAcceptedSteps"]
        if type(self.original_count) is not int or self.original_count<0:raise ValueError("Actual original counter required")
        self.parent_state=args.cartesian_state.resolve() if args.cartesian_state else None
        self.parent_observer=args.cartesian_observer.resolve() if args.cartesian_observer else None
        if bool(self.parent_state)!=bool(self.parent_observer):raise ValueError("Both actual own parent files are required")
        self.own_count=self.attempt_count=0
        if self.parent_state:
            for raw in (self.parent_state,self.parent_observer):
                if raw==self.repo or self.repo in raw.parents:raise ValueError("Own raw state must remain outside Git")
            old=json.loads(self.parent_state.read_text())
            if old.get("source",{}).get("runId")!=int(self.run_id) or old.get("source",{}).get("sourceEpoch")!=self.epoch:
                raise ValueError("An ended job's checkpoint cannot initialize this same-run controller")
            self.own_count=old["cartesianAcceptedSteps"]
            self.attempt_count=old["completeAttemptCount"]
            if type(self.own_count) is not int or self.own_count<0 or type(self.attempt_count) is not int or self.attempt_count<self.own_count:
                raise ValueError("Valid own cumulative counters required")
        self.prior_observed=args.prior_observed_accepted
        if type(self.prior_observed) is not int or self.prior_observed<0:raise ValueError("Explicit nonnegative prior scientific count required")
        self.total_attempts=small_int(args.attempts)
        self.followup=Path(args.followup_relative)
        if self.followup.parent!=TOPIC/"ci-requests" or not re.fullmatch("6a65-[A-Za-z0-9_-]+\\.json",self.followup.name):
            raise ValueError("A topic-local small same-job reception path is required")
        self.last_sync=time.monotonic()
        self.total_pull_count=0
        self.report_stem=f"2026-11-26-6a65-Cartesian-continuation-{self.run_id}-{self.attempt}"
        self.report=self.repo/TOPIC/"notes"/(self.report_stem+"-start.json")
        if self.report.exists():raise ValueError("Fresh same-run scalar receipt namespace required")
        self.receipt=self.out/"scalar-continuation-manifest.json"
        self.record=dict(schema="6a65-actual-own-Cartesian-same-model-continuation-scalar-v1",
            run_id=self.run_id,run_attempt=self.attempt,source_epoch=self.epoch,
            controllerSHA256=sha(__file__),entrySHA256=sha(self.scripts/ENTRY),
            originalCauchyStateSHA256=self.source_hash,originalCauchyObserverSHA256=self.original_observer_hash,
            originalCauchyAcceptedSteps=self.original_count,originalCauchyStateAndCounterUnchanged=True,
            candidateSHA256=self.candidate_hash,recipeSHA256=self.recipe_hash,
            initialOwnAcceptedCount=self.own_count,initialOwnAttemptCount=self.attempt_count,
            priorScientificallyObservedAcceptedSteps=self.prior_observed,
            sourceInputsProducedInThisActualRunner=True,oldRunRawFetched=False,
            fixedPhysicalMetricAndSource=True,allThirteenPointRowsRetained=True,
            startedUTC=utc(),state="starting",attempts=[],processReceipts=[],pulls=[],
            usedFollowups=[],rawPublished=False,continuousCertificate=False,strongTargetComplete=False)
        self.code_inventory=self.verify_snapshot()
        self.record["frozenCompleteScriptInventorySHA256"]=self.code_inventory
        self.save("starting")

    def git(self,*args,capture=False,check=True):
        r=subprocess.run(["git",*args],cwd=self.repo,env=self.git_env,text=True,
                         stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        if r.stdout and not capture:print(r.stdout,end="",flush=True)
        if check and r.returncode:raise RuntimeError("Actual Git "+args[0]+" failed")
        if capture and check:return r.stdout
        return r

    def verify_snapshot(self):
        tree=self.git("ls-tree","-r","-z",self.epoch,"--",str(TOPIC/"scripts"),capture=True)
        inventory=[]
        for item in tree.split("\0"):
            if not item:continue
            info,rel=item.split("\t",1);mode,kind,blob=info.split()
            if kind!="blob" or mode not in ("100644","100755"):raise ValueError("Frozen script must be a tracked ordinary file")
            filename=self.frozen/rel
            size=filename.stat().st_size
            git_hash=hashlib.sha1(("blob "+str(size)+"\0").encode())
            file_hash=hashlib.sha256()
            with filename.open("rb") as stream:
                for chunk in iter(lambda:stream.read(1048576),b""):
                    git_hash.update(chunk);file_hash.update(chunk)
            if git_hash.hexdigest()!=blob:raise ValueError("Frozen complete script differs from public epoch: "+rel)
            inventory.append(dict(path=rel,sha256=file_hash.hexdigest(),bytes=size))
        if not inventory or not (self.scripts/ENTRY).is_file():raise ValueError("Complete public numerical snapshot required")
        for filename in (self.candidate,self.recipe):
            rel=filename.relative_to(self.frozen)
            expected=self.git("rev-parse",f"{self.epoch}:{rel.as_posix()}",capture=True).strip()
            actual=self.git("hash-object","--",str(filename),capture=True).strip()
            if actual!=expected:raise ValueError("Frozen candidate/recipe differs from actual public epoch")
        data=json.dumps(inventory,sort_keys=True,separators=(",",":")).encode()
        return hashlib.sha256(data).hexdigest()

    def save(self,status):
        self.record.update(state=status,updatedUTC=utc(),actualOwnAcceptedCount=self.own_count,
            actualOwnAttemptCount=self.attempt_count,
            currentStateSHA256=sha(self.parent_state) if self.parent_state else None,
            currentObserverSHA256=sha(self.parent_observer) if self.parent_observer else None)
        raw=(json.dumps(self.record,indent=2,allow_nan=False)+"\n").encode()
        if len(raw)>=100000:raise ValueError("Small scalar report limit reached; raw fallback is forbidden")
        self.receipt.write_bytes(raw);self.report.write_bytes(raw)

    def publish(self,reason):
        subject=f"visible-flex: own Cartesian {self.run_id}/{self.attempt} {reason}"
        self.git("add","--",str(self.report.relative_to(self.repo)))
        self.git("commit","-m",subject)
        changed_rules=False
        while True:
            pull=self.git("pull","--rebase","origin","main",check=False)
            remote=self.git("rev-parse","origin/main",capture=True).strip()
            difference=self.git("diff",self.last_rules,remote,"--",*(str(x) for x in RULES),capture=True)
            if difference:
                print("UNREVIEWED_README_DIFF\n"+difference,flush=True)
                changed_rules=True
                self.record["state"]="unreviewed-readme-difference-numerical-work-stopped"
                self.record["unreviewedReadmeDiffSHA256"]=hashlib.sha256(difference.encode()).hexdigest()
            if pull.returncode:
                conflicts=self.git("diff","--name-only","--diff-filter=U",capture=True).splitlines()
                if conflicts!=[str(HANDOFF)]:raise RuntimeError("Actual pull/rebase failed outside own HANDOFF marker")
                base=self.git("show",":1:"+str(HANDOFF),capture=True)
                ours=self.git("show",":3:"+str(HANDOFF),capture=True)
                strip=lambda text:"".join(x for x in text.splitlines(keepends=True) if not x.startswith(MARKER))
                if strip(base)!=strip(ours):raise RuntimeError("Local conflict includes nonmarker HANDOFF changes")
                upstream=self.git("show",":2:"+str(HANDOFF),capture=True)
                (self.repo/HANDOFF).write_text(upstream)
                self.git("add","--",str(HANDOFF))
                self.git("-c","core.editor=true","rebase","--continue")
            lines=(self.repo/HANDOFF).read_text().splitlines(keepends=True)
            positions=[i for i,line in enumerate(lines) if line.startswith(MARKER)]
            if len(positions)>1:raise RuntimeError("Duplicate own HANDOFF markers")
            receipt=dict(UTC=utc(),fromCommit=self.last_rules,toCommit=remote,readmeDiffEmpty=not bool(difference),pullCommandExit=pull.returncode)
            self.record["pulls"].append(receipt)
            self.total_pull_count+=1
            self.record["actualTotalPullCount"]=self.total_pull_count
            rule_state="双 README 有差异未审，已打印并停数值步骤" if changed_rules else "双 README 无差异"
            line=f"{MARKER} run {self.run_id}/{self.attempt}；实际 pull 至 {remote}；{receipt['UTC']}；{rule_state}。\n"
            if positions:lines[positions[0]]=line
            else:lines.insert(1,line)
            text="".join(lines)
            if len(text.encode())>=10000:raise RuntimeError("HANDOFF would exceed 10KB; root must compact")
            (self.repo/HANDOFF).write_text(text)
            if not changed_rules:self.last_rules=remote
            self.save(self.record["state"])
            self.git("add","--",str(HANDOFF),str(self.report.relative_to(self.repo)))
            pending=self.git("rev-list","origin/main..HEAD",capture=True).strip()
            if pending:
                if self.git("log","-1","--format=%s",capture=True).strip()!=subject:raise RuntimeError("Refusing to amend an unrelated commit")
                self.git("commit","--amend","--no-edit")
            else:self.git("commit","-m",subject)
            pushed=self.git("push","origin","HEAD:main",check=False)
            if pushed.returncode==0:break
            if not concurrent_ref(pushed.stdout):raise RuntimeError("Actual push failed outside identified concurrent-ref cases")
            emit("non-fast-forward-immediate-pull-rebase-retry")
        self.last_sync=time.monotonic()
        emit("actual-own-Cartesian-scalar-published",commit=self.git("rev-parse","HEAD",capture=True).strip(),
             ownAcceptedCount=self.own_count,state=self.record["state"])
        if changed_rules:
            raise RulesChanged("Actual pull SHA and unreviewed diff receipt published; root must apply rules")

    def execute_child(self,label,command):
        log=self.out/(label+".log")
        if log.exists():raise FileExistsError("Fresh process receipt required")
        start=time.monotonic()
        process=subprocess.Popen(command,cwd=self.frozen,env=self.child_env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        selector=selectors.DefaultSelector();selector.register(process.stdout,selectors.EVENT_READ)
        try:
            with log.open("wb") as output:
                while selector.get_map():
                    for key,_ in selector.select(timeout=1):
                        chunk=os.read(key.fileobj.fileno(),65536)
                        if not chunk:selector.unregister(key.fileobj);continue
                        output.write(chunk);output.flush();sys.stdout.buffer.write(chunk);sys.stdout.buffer.flush()
                    if time.monotonic()-self.last_sync>=45*60:
                        self.save("actual-numerical-process-running-no-new-exit-claimed")
                        self.publish("hourly rules during actual numerical process")
                code=process.wait()
        except BaseException:
            process.terminate()
            try:process.wait(timeout=10)
            except subprocess.TimeoutExpired:process.kill();process.wait()
            raise
        finally:selector.close();process.stdout.close()
        receipt=dict(label=label,OSExitCode=code,seconds=time.monotonic()-start,stdoutSHA256=sha(log))
        self.record["processReceipts"].append(receipt)
        write(self.receipt,self.record)
        if code:raise RuntimeError("Actual numerical child failed with exit "+str(code))
        return receipt

    def one(self):
        number=self.attempt_count+1
        previous=dict(path=str(self.report.relative_to(self.repo)),sha256=sha(self.report))
        self.report=self.repo/TOPIC/"notes"/(self.report_stem+f"-attempt-{number:03d}.json")
        if self.report.exists():raise ValueError("An actual prior scalar attempt cannot be overwritten")
        self.record["previousPublishedScalarPart"]=previous
        self.record["attempts"]=[]
        self.record["processReceipts"]=[]
        self.record["pulls"]=[]
        prefix=self.out/f"Cartesian-{number:03d}"
        parent_sha=sha(self.parent_state) if self.parent_state else None
        observer_sha=sha(self.parent_observer) if self.parent_observer else None
        args=[sys.executable,str(self.scripts/ENTRY),"--scripts",str(self.scripts),
            "--candidate",str(self.candidate),"--source",str(self.source),"--observer",str(self.original_observer),
            "--prefix",str(prefix),"--recipe",str(self.recipe),"--source-epoch",self.epoch,"--run-id",self.run_id]
        if self.parent_state:args+=["--cartesian-state",str(self.parent_state),"--cartesian-observer",str(self.parent_observer)]
        self.save("running-one-real-complete-Cartesian-attempt")
        self.publish("pre-process actual attempt "+str(number))
        process=self.execute_child("Cartesian-attempt-"+str(number),args)
        report_file=Path(str(prefix)+"-report.json")
        report=json.loads(report_file.read_text())
        state_file,observer_file=Path(str(prefix)+"-state.json"),Path(str(prefix)+"-observer.json")
        state=json.loads(state_file.read_text())
        obs=json.loads(observer_file.read_text())
        if (report.get("schema")!="6a65-independent-complete-Cartesian-experiment-scalar-report-v1" or
            report.get("originalCauchyStateSHA256")!=self.source_hash or
            report.get("originalCauchyObserverSHA256")!=self.original_observer_hash or
            report.get("originalCauchyAcceptedSteps")!=self.original_count or
            report.get("originalCauchyStateAndCounterUnchanged") is not True or
            report.get("acceptedCauchyStepsAddedByThisExperiment")!=0 or
            report.get("parentCartesianStateSHA256")!=parent_sha or
            report.get("parentCartesianObserverSHA256")!=observer_sha or
            report.get("entrySHA256")!=sha(self.scripts/ENTRY) or
            report.get("recipeSHA256")!=self.recipe_hash or
            report.get("sourceEpoch")!=self.epoch or report.get("runId")!=int(self.run_id)):
            raise ValueError("Actual own-model report identity mismatch")
        accepted=report.get("accepted") is True
        if (report.get("ownAcceptedSteps")!=self.own_count+int(accepted) or
            report.get("ownAcceptedStepsAddedThisAttempt")!=int(accepted) or
            report.get("ownCompleteAttemptCount")!=number or state.get("cartesianAcceptedSteps")!=report["ownAcceptedSteps"]):
            raise ValueError("Actual cumulative own-model counters did not inherit their parent")
        if report["stateSHA256"]!=sha(state_file) or report["observerSHA256"]!=sha(observer_file) or obs["inputs"]["cartesianStateSHA256"]!=sha(state_file):
            raise ValueError("Actual own observer/checkpoint byte identity mismatch")
        if accepted and not report["evaluation"]["squaredNorm"]<report["baseline"]["squaredNorm"]:
            raise ValueError("Accepted flag lacks actual full objective decrease")
        if not accepted and self.parent_state:
            if state["z"]!=json.loads(self.parent_state.read_text())["z"]:raise ValueError("Stalled own state changed its saved coefficients")
        if sha(self.source)!=self.source_hash or sha(self.original_observer)!=self.original_observer_hash:
            raise ValueError("Original Cauchy source/observer changed")
        if self.verify_snapshot()!=self.code_inventory:raise ValueError("Frozen complete source inventory changed")
        purpose=("previously observed accepted prefix regenerated; not a new result" if
                 accepted and report["ownAcceptedSteps"]<=self.prior_observed else "actual new complete attempt")
        row=dict(number=number,purpose=purpose,accepted=accepted,ownAcceptedSteps=report["ownAcceptedSteps"],
            stateSHA256=sha(state_file),observerSHA256=sha(observer_file),reportSHA256=sha(report_file),
            parentCartesianStateSHA256=parent_sha,parentCartesianObserverSHA256=observer_sha,
            baseline=report["baseline"],evaluation=report["evaluation"],refinedObservation=report["refinedObservation"],
            targetGaussianCurvatureTraining=report["targetGaussianCurvatureTraining"],
            targetGaussianCurvatureRefined=report["targetGaussianCurvatureRefined"],
            dimension=report["dimension"],completeRows=report["completeRows"],
            alpha=report["alpha"],trace=report["trace"],**process)
        self.record["attempts"].append(row)
        self.parent_state,self.parent_observer=state_file,observer_file
        self.own_count,self.attempt_count=report["ownAcceptedSteps"],number
        self.save("actual-complete-attempt-and-dense-observer-returned" if accepted else "actual-stall-valid-own-state-and-observer-retained")
        self.publish("actual attempt "+str(number)+" exit 0 accepted "+str(accepted))
        return accepted

    def wait_followup(self):
        self.save("awaiting-explicit-matched-same-model-followup")
        self.publish("actual state and dense observer retained")
        last_blob=None
        while True:
            self.git("fetch","--filter=blob:none","origin","main")
            found=self.git("rev-parse",f"origin/main:{self.followup}",capture=True,check=False)
            blob=found.stdout.strip() if found.returncode==0 else None
            changed=blob is not None and blob!=last_blob
            if changed or time.monotonic()-self.last_sync>=45*60:
                self.save("awaiting-explicit-matched-same-model-followup")
                self.publish("new reception candidate" if changed else "hourly rules during same-job wait")
                last_blob=blob
            if changed and (self.repo/self.followup).is_file():
                filename=self.repo/self.followup
                if filename.stat().st_size>=100000:raise ValueError("Followup must be a small recipe")
                packet=json.loads(filename.read_text())
                identity=packet.get("followup_id")
                if str(packet.get("run_id"))==self.run_id and str(packet.get("attempt"))==self.attempt and identity not in self.record["usedFollowups"]:
                    try:
                        if (packet.get("schema")!="6a65-own-Cartesian-same-model-followup-v1" or
                            not isinstance(identity,str) or not re.fullmatch("[A-Za-z0-9_-]{1,80}",identity) or
                            packet.get("parent_state_sha256")!=sha(self.parent_state) or
                            packet.get("parent_observer_sha256")!=sha(self.parent_observer) or
                            packet.get("source_epoch")!=self.epoch or packet.get("recipe_sha256")!=self.recipe_hash):
                            raise ValueError("Exact same-run current-state/source/recipe match required")
                        rules=packet.get("rules_read_commit","")
                        if not re.fullmatch("[0-9a-f]{40}",rules):raise ValueError("Root's actual read-rules commit required")
                        if self.git("cat-file","-e",rules+"^{commit}",capture=True,check=False).returncode:
                            self.git("fetch","--filter=blob:none","origin",rules)
                        difference=self.git("diff",rules,"origin/main","--",*(str(p) for p in RULES),capture=True)
                        if difference:raise ValueError("Followup rules commit lacks current README text")
                        action=packet.get("action")
                        if action=="continue_same_model":
                            count=small_int(packet.get("additional_attempts"))
                            self.record["usedFollowups"].append(identity)
                            self.record["lastFollowupSHA256"]=sha(filename)
                            return count
                        if action=="release_runner" and isinstance(packet.get("reason"),str) and packet["reason"].strip():
                            self.record["usedFollowups"].append(identity)
                            self.record["explicitReleaseReason"]=packet["reason"]
                            self.save("released-by-explicit-matched-recipe-not-completion")
                            self.publish("explicit matched release")
                            return 0
                        raise ValueError("Explicit supported continuation or release action required")
                    except ValueError as error:emit("actual-Cartesian-followup-rejected",reason=str(error))
            emit("actual-Cartesian-runner-wait-heartbeat",UTC=utc(),run_id=self.run_id,
                 ownAcceptedCount=self.own_count,stateSHA256=sha(self.parent_state),observerSHA256=sha(self.parent_observer))
            time.sleep(30)

    def run(self):
        self.save("starting-complete-same-model-continuation")
        self.publish("actual start and current rules")
        count=self.total_attempts
        while count:
            for _ in range(count):
                if not self.one():break
            count=self.wait_followup()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ("repo","scripts","candidate","source","source-observer","recipe","out-dir"):
        parser.add_argument("--"+key,type=Path,required=True)
    parser.add_argument("--source-epoch",required=True)
    parser.add_argument("--rules-read-commit",required=True)
    parser.add_argument("--attempts",type=int,required=True)
    parser.add_argument("--prior-observed-accepted",type=int,default=0)
    parser.add_argument("--cartesian-state",type=Path)
    parser.add_argument("--cartesian-observer",type=Path)
    parser.add_argument("--followup-relative",required=True)
    controller=None
    try:
        controller=Controller(parser.parse_args());controller.run()
    except RulesChanged:
        emit("unreviewed-rules-require-root-application")
        raise
    except BaseException as error:
        if controller is not None:
            controller.record["actualFailure"]=dict(error=str(error),UTC=utc(),newAcceptanceNotInferred=True)
            try:
                controller.save("actual-process-or-controller-failure")
                controller.publish("actual failure receipt")
            except BaseException as failure:emit("actual-failure-publication-also-failed",error=str(failure))
        raise

if __name__=="__main__":main()
