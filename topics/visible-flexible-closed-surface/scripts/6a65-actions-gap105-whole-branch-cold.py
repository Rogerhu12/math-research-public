#!/usr/bin/env python3
"""Cold-regenerate the explicit gap-1.05 source and continue its full model.

This is a new Actions orchestration identity, not a recovered checkpoint.
Only the verified v5 git/publish/process methods are reused. Its Cartesian
source schema, coefficient representation, recipes, and counters are not.
All numerical sources are copied once outside the changing Git checkout.
The numerical entrypoints remain byte-identical to their published versions.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import importlib.util
import importlib.metadata
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time

TOPIC=Path("topics/visible-flexible-closed-surface")
MARKER="<!-- 6a65-gap105-whole-branch-cold-ci-rules -->"
PUBLISHER="6a65-actions-cartesian-channel-block-v5-20261126.py"
PUBLISHER_SHA="5055b47a891bb106557842976a6f4766121edf893605fd7a551a39c223283d29"
R233_RAMP="0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7"
R233_COAST="f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d"
SCHEMA="6a65-gap105-whole-branch-cold-scalar-v1"


def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda:f.read(1048576),b""):h.update(block)
    return h.hexdigest()


def write(path,value):
    Path(path).write_text(json.dumps(value,indent=2,allow_nan=False)+"\n")


def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m
    spec.loader.exec_module(m)
    return m


def scalar_value(value):
    """Only scalar summaries, never coefficient, mesh, normal or cache arrays."""
    if value is None:return None
    scalar=lambda x:x is None or type(x) in (str,int,float,bool)
    result={k:v for k,v in value.items() if scalar(v)}
    for key in ("curvature","geometry","groupSquaredNorm",
                "originalThirteenRowStatistics","areaBarrierStatistics"):
        part=value.get(key)
        if isinstance(part,dict):
            result[key]={k:v for k,v in part.items() if scalar(v)}
    result["completeValueObjectCanonicalSHA256"]=hashlib.sha256(
        json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
    return result


class GapCold:
    """Numerical commands and own scalar state; the publisher is mixed in."""

    def __init__(self,args):
        self.repo=args.repo.resolve()
        self.out=args.out_dir.resolve()
        if self.out.exists() or self.out==self.repo or self.repo in self.out.parents:
            raise ValueError("A fresh Git-external RUNNER_TEMP directory is required")
        self.run_id=os.environ.get("GITHUB_RUN_ID","")
        self.attempt=os.environ.get("GITHUB_RUN_ATTEMPT","")
        self.epoch=os.environ.get("GITHUB_SHA","")
        if (os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"
            or not self.run_id.isdigit() or not self.attempt.isdigit()
            or not re.fullmatch("[0-9a-f]{40}",self.epoch)):
            raise ValueError("An actual public-repository Actions run/epoch is required")
        if not os.environ.get("CART_CONTINUATION_TOKEN"):
            raise ValueError("The workflow must supply its existing publication credential")
        self.git_env=os.environ.copy()
        self.git_env.update(GIT_TERMINAL_PROMPT="0",GIT_CONFIG_COUNT="2",
            GIT_CONFIG_KEY_0="credential.helper",GIT_CONFIG_VALUE_0="",
            GIT_CONFIG_KEY_1="credential.helper",
            GIT_CONFIG_VALUE_1='!f() { printf "username=x-access-token\\npassword=%s\\n" "$CART_CONTINUATION_TOKEN"; }; f')
        self.child_env={k:v for k,v in os.environ.items() if k not in
            ("GH_TOKEN","GITHUB_TOKEN","MR_TOKEN","VISIBLE_FLEX_TOKEN",
             "M12_RECOVERY_TOKEN","CART_COLD_TOKEN","CART_CONTINUATION_TOKEN")
            and not k.startswith("GIT_CONFIG_")}
        self.child_env.update(OPENBLAS_NUM_THREADS="1",OMP_NUM_THREADS="1",MKL_NUM_THREADS="1")
        if self.git("rev-parse","--show-toplevel",capture=True).strip()!=str(self.repo):
            raise ValueError("Explicit actual Git checkout required")
        if self.git("rev-parse","HEAD",capture=True).strip()!=self.epoch:
            raise ValueError("Trigger checkout must be frozen before the first live pull")
        relative=args.request.relative_to(self.repo) if args.request.is_absolute() else args.request
        if relative.parent!=TOPIC/"ci-requests" or ".." in relative.parts:
            raise ValueError("The small request must be a topic ci-request")
        self.request=json.loads((self.repo/relative).read_text())
        if self.request.get("schema")!="6a65-gap105-window-whole-branch-cold-request-v1":
            raise ValueError("An explicit new-gap whole-branch request is required")
        if self.request.get("ruleCheckSeconds")!=2700:
            raise ValueError("This adapter uses the verified 45-minute publisher check")
        followup=Path(self.request["followupRelative"])
        if (followup.parent!=TOPIC/"ci-requests" or ".." in followup.parts
            or not re.fullmatch("6a65-[A-Za-z0-9_-]+[.]json",followup.name)
            or self.request.get("receiverPollSeconds")!=30):
            raise ValueError("A dedicated small same-job packet path and 30-second poll are required")
        self.phases=self.request["phases"]
        for key in ("singleGridAttempts","twoGridAttempts","refinedAttempts","areaAttempts"):
            if type(self.phases[key]) is not int or not 1<=self.phases[key]<=100:
                raise ValueError("Explicit bounded actual attempt budgets required")
        self.out.mkdir(parents=True)
        self.frozen=self.out/"frozen"
        self.frozen.mkdir()
        candidate_rel=TOPIC/self.request["candidate"]
        recipe_rel=TOPIC/self.request["cauchyRecipe"]
        for rel in (candidate_rel,recipe_rel):
            if ".." in rel.parts or rel.parts[:2]!=TOPIC.parts:
                raise ValueError("Frozen inputs must stay in this topic")
        paths=subprocess.check_output(
            ["git","ls-files","-z","--",str(TOPIC/"scripts"),str(candidate_rel),
             str(recipe_rel),str(relative),"README.md",str(TOPIC/"README.md")],
            cwd=self.repo,env=self.git_env).split(b"\0")
        inventory=[]
        for encoded in paths:
            if not encoded:continue
            rel=Path(encoded.decode())
            target=self.frozen/rel
            target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(self.repo/rel,target)
            inventory.append(dict(path=str(rel),sha256=sha(target),bytes=target.stat().st_size))
        self.inventory=self.out/"frozen-source-inventory.json"
        write(self.inventory,inventory)
        self.scripts=self.frozen/TOPIC/"scripts"
        self.candidate=self.frozen/candidate_rel
        self.recipe=self.frozen/recipe_rel
        if sha(self.candidate)!=self.request["candidateSHA256"]:
            raise ValueError("Public candidate bytes changed")
        if sha(self.recipe)!=self.request["cauchyRecipeSHA256"]:
            raise ValueError("Public Cauchy physical recipe bytes changed")
        for name,digest in self.request["sourceSHA256"].items():
            if Path(name).name!=name or sha(self.scripts/name)!=digest:
                raise ValueError("Frozen numerical source hash mismatch: "+name)
        if sha(self.scripts/PUBLISHER)!=PUBLISHER_SHA:
            raise ValueError("The verified publication implementation changed")
        self.last_rules=self.epoch
        self.last_sync=time.monotonic()
        self.total_pull_count=0
        self.own_count=self.attempt_count=0
        self.parent_state=None
        self.serial=0
        self.report_stem=f"2026-11-26-6a65-gap105-cold-{self.run_id}-{self.attempt}"
        self.receipt=self.out/"current-scalar-receipt.json"
        self.report=self.repo/TOPIC/"notes"/(self.report_stem+"-start.json")
        if self.report.exists():raise FileExistsError("A new actual run report namespace is required")
        self.record=dict(schema=SCHEMA,run_id=self.run_id,run_attempt=self.attempt,
            source_epoch=self.epoch,controllerSHA256=sha(__file__),
            requestSHA256=sha(self.repo/relative),publisherSHA256=PUBLISHER_SHA,
            publicationAdapterMarker=MARKER,sourceSHA256=self.request["sourceSHA256"],
            candidateSHA256=sha(self.candidate),cauchyRecipeSHA256=sha(self.recipe),
            frozenSourceInventorySHA256=sha(self.inventory),frozenSourceFiles=len(inventory),
            requestedAttemptBudgets=self.phases,phaseProgress={},
            runtime=dict(python=sys.version,numpy=importlib.metadata.version("numpy"),
                scipy=importlib.metadata.version("scipy"),
                node=subprocess.check_output(["node","--version"],text=True,env=self.child_env).strip()),
            inheritedAcceptedSteps=0,sameJobNewActualInputs=True,
            rawRetention="RUNNER_TEMP only; no raw artifact, Git or Release publication.",
            numericalSourceFrozenBeforeLivePull=True,ruleCheckIntervalSeconds=2700,
            processReceipts=[],pulls=[],state="new-cold-source-not-yet-evaluated",
            originalCauchyFactoryAcceptedSteps=0,actualPipelineAcceptedSteps=0,
            legacyCertificateNamedFlagsAreNotProof=True,
            R233InputBytesMatch=None,literalEvaluatorRoundingCertified=False,
            continuousCertificate=False,strongTargetComplete=False)
        self.git("config","--local","user.name","Astra-visible-flex-6a65")
        self.git("config","--local","user.email","41898282+github-actions[bot]@users.noreply.github.com")
        self.git("switch","-c",f"visible-flex-gap105-cold-{self.run_id}-{self.attempt}")

    def save(self,status):
        self.record.update(state=status,actualPipelineAcceptedSteps=self.own_count,
            actualPipelineAttempts=self.attempt_count,
            currentStateSHA256=sha(self.parent_state) if self.parent_state else None)
        raw=(json.dumps(self.record,indent=2,allow_nan=False)+"\n").encode()
        if len(raw)>=100000:raise ValueError("Only small scalar reports can be published")
        self.receipt.write_bytes(raw)
        self.report.write_bytes(raw)

    def rotate(self,label):
        prior=dict(path=str(self.report.relative_to(self.repo)),sha256=sha(self.report))
        self.serial+=1
        self.report=self.repo/TOPIC/"notes"/(self.report_stem+f"-{self.serial:03d}-{label}.json")
        if self.report.exists():raise FileExistsError("A real prior scalar result must not be overwritten")
        self.record["previousScalarPart"]=prior
        self.record["processReceipts"]=[]
        self.record["pulls"]=[]
        self.record["stage"]=label
        self.record.pop("stageResult",None)

    def stage(self,label,command):
        self.rotate(label)
        self.save("actual-stage-starting")
        return self.execute_child(label,[str(x) for x in command])

    def publish_stage(self,result):
        self.record["stageResult"]=result
        self.save("actual-stage-exited-zero")
        self.publish(self.record["stage"])

    def actual_step(self,phase,entry,state,number):
        label=f"{phase}-{number:03d}"
        prefix=self.out/label
        command=[sys.executable,self.scripts/entry]
        if phase=="single":command+=["solve"]
        command+=["--scripts",self.scripts,"--prepared",self.prepared,
                  "--prefix",prefix,"--steps","1"]
        if state is not None:command+=["--state",state]
        try:
            self.stage(label,command)
        except BaseException:
            # A subprocess can save a genuine accepted state before a later
            # external failure. Preserve its measured bytes, never invent one.
            available={}
            for suffix in ("-initial.json","-step01-state.json","-report.json"):
                part=Path(str(prefix)+suffix)
                if part.exists():available[suffix]=dict(SHA256=sha(part),bytes=part.stat().st_size)
            self.record["partialStepOutputs"]=available
            part=Path(str(prefix)+"-step01-state.json")
            if part.exists():
                try:
                    partial=json.loads(part.read_text())
                    added=partial["accepted"]
                    total=partial["ownAcceptedSteps"] if phase=="single" else partial["actualTotalCartesianAcceptedSteps"]
                    parent=sha(state) if state is not None else None
                    if (type(added) is not bool or total!=self.own_count+int(added)
                        or partial.get("parentStateSHA256")!=parent
                        or partial.get("preparedSHA256")!=sha(self.prepared)
                        or partial.get("sourceIdentity")!=self.prepared_identity):
                        raise ValueError("Partial saved checkpoint binding failed")
                    self.own_count=total
                    self.attempt_count+=1
                    self.parent_state=part
                    progress=self.record["phaseProgress"].setdefault(phase,dict(attempts=0,acceptedSteps=0))
                    progress["attempts"]+=1
                    progress["acceptedSteps"]+=int(added)
                    self.record["actualSavedStateBeforeFailedProcess"]=dict(
                        SHA256=sha(part),accepted=added,totalAcceptedSteps=total,
                        evaluation=scalar_value(partial["evaluation"]),
                        processExitStillNonzero=True,noNaturalExitClaimed=True)
                except (KeyError,ValueError,TypeError) as validation:
                    self.record["partialSavedStateNotConsumed"]=str(validation)
            raise
        file=Path(str(prefix)+"-step01-state.json")
        report=Path(str(prefix)+"-report.json")
        baseline=Path(str(prefix)+"-initial.json")
        if not file.exists() or not report.exists() or not baseline.exists():
            raise RuntimeError("An exit-zero solve must return its actual state, baseline and report")
        result=json.loads(file.read_text())
        added=result["accepted"]
        if type(added) is not bool:raise ValueError("The actual acceptance flag must be Boolean")
        total=result["ownAcceptedSteps"] if phase=="single" else result["actualTotalCartesianAcceptedSteps"]
        if total!=self.own_count+int(added):
            raise ValueError("An actual checkpoint counter disagrees with same-job accepted steps")
        if result.get("parentStateSHA256")!=(sha(state) if state is not None else None):
            raise ValueError("The actual child does not bind its same-job parent checkpoint")
        if result.get("preparedSHA256")!=sha(self.prepared):
            raise ValueError("The actual checkpoint changed the prepared same-job source")
        if result.get("sourceIdentity")!=self.prepared_identity:
            raise ValueError("The actual checkpoint changed the frozen gap source or metric")
        self.own_count=total
        self.attempt_count+=1
        self.parent_state=file
        progress=self.record["phaseProgress"].setdefault(phase,dict(attempts=0,acceptedSteps=0))
        progress["attempts"]+=1
        progress["acceptedSteps"]+=int(added)
        output=dict(accepted=added,sameJobStateSHA256=sha(file),
            actualOwnBaselineSHA256=sha(baseline),
            actualOwnBaseline=scalar_value(json.loads(baseline.read_text())["evaluation"]),
            actualSolveReportSHA256=sha(report),
            dimension=len(result["z"]),evaluation=scalar_value(result["evaluation"]),
            actualPipelineAcceptedSteps=self.own_count,
            dampingStartForEachProcess=1e-4,
            oneProcessOneAttempt=True,oldNumericalMetricsNotInherited=True)
        if "observed" in result:output["independentObserver"]=scalar_value(result["observed"])
        if "groupValues" in result:
            output["bothActualGroups"]={k:scalar_value(v) for k,v in result["groupValues"].items()}
        self.publish_stage(output)
        return file,added

    def receive_followup(self):
        """Read one small public packet; no raw state or new model is accepted."""
        fetched=self.git("fetch","--filter=blob:none","origin","main",check=False)
        if fetched.returncode:
            print(json.dumps(dict(event="gap105-followup-fetch-failed-no-new-work",
                exitCode=fetched.returncode)),flush=True)
            return None
        rel=Path(self.request["followupRelative"])
        reply=self.git("show","origin/main:"+str(rel),capture=True,check=False)
        if reply.returncode:return None
        raw=reply.stdout.encode()
        digest=hashlib.sha256(raw).hexdigest()
        if digest in self.seen_packets:return None
        self.seen_packets.add(digest)
        try:
            if len(raw)>8192:raise ValueError("Followup must be a small scalar packet")
            packet=json.loads(raw)
            if not isinstance(packet,dict):raise ValueError("Followup must be a JSON object")
            if packet.get("schema")!="6a65-gap105-area-same-job-followup-v1":
                raise ValueError("Explicit gap105 same-job followup schema required")
            expected=dict(run_id=self.run_id,run_attempt=self.attempt,
                source_epoch=self.epoch,requestSHA256=self.record["requestSHA256"],
                parentStateSHA256=sha(self.parent_state),preparedSHA256=sha(self.prepared))
            for key,value in expected.items():
                if packet.get(key)!=value:raise ValueError("Followup binding mismatch: "+key)
            operation=packet.get("operation")
            if operation not in ("additional_area_attempts","release"):
                raise ValueError("Only unchanged-model extra area attempts or release are supported")
            if operation=="additional_area_attempts":
                count=packet.get("additional_area_attempts")
                if type(count) is not int or not 1<=count<=100:
                    raise ValueError("A bounded explicit additional attempt count is required")
                if self.record["phaseProgress"]["area"].get("endedAfterActualRejectedAttempt"):
                    raise ValueError("The unchanged area model already rejected; only release is accepted")
            elif packet.get("additional_area_attempts",0)!=0:
                raise ValueError("Release cannot request a numerical attempt")
            return dict(packet=packet,packetSHA256=digest,
                        actualFetchedCommit=self.git("rev-parse","origin/main",capture=True).strip())
        except (ValueError,TypeError) as error:
            self.record["lastIgnoredFollowup"]=dict(packetSHA256=digest,reason=str(error))
            print(json.dumps(dict(event="gap105-followup-ignored",
                packetSHA256=digest,reason=str(error))),flush=True)
            return None

    def wait_followup(self):
        """Keep the actual same-job files; each numerical child remains one step."""
        self.seen_packets=set()
        while True:
            if time.monotonic()-self.last_sync>=2700:
                self.save("same-job-actual-gap-state-retained-awaiting-bound-packet")
                self.publish("45-minute rules while retaining actual gap state")
            received=self.receive_followup()
            if received is None:
                time.sleep(30)
                continue
            packet=received["packet"]
            self.record["actualFollowup"]=received
            # The extra work starts only after a real pull and new-rule check.
            self.save("explicit-bound-same-job-followup-received")
            self.publish("bound gap same-job followup received")
            if packet["operation"]=="release":
                self.save("explicitly-released-actual-runner-state-topic-still-incomplete")
                self.publish("explicit release of gap runner")
                return
            for unused in range(packet["additional_area_attempts"]):
                number=self.record["phaseProgress"]["area"]["attempts"]+1
                state,accepted=self.actual_step("area",
                    "6a65-geometry-gap-window-area-cartesian.py",self.parent_state,number)
                if not accepted:
                    self.record["phaseProgress"]["area"]["endedAfterActualRejectedAttempt"]=True
                    break
            self.save("same-job-actual-gap-state-retained-after-explicit-additional-attempts")
            self.publish("additional gap batch retained for bound followup")

    def execute(self):
        self.save("new-cold-source-frozen-before-first-numerical-step")
        self.publish("source frozen and initial rules check")
        prefix=self.out/"coupled-prefix"
        self.stage("prefix",[sys.executable,self.scripts/"6a65-geometry-coupled-gap-prefix.py",
            "--scripts-dir",self.scripts,"--output-prefix",prefix])
        ramp=Path(str(prefix)+"-ramp-master.npz")
        coast=Path(str(prefix)+"-coast-master.npz")
        prefix_report=Path(str(prefix)+"-report.json")
        raw=json.loads(prefix_report.read_text())
        match=sha(ramp)==R233_RAMP and sha(coast)==R233_COAST
        self.record["R233InputBytesMatch"]=match
        self.record["actualPrefixInputHashes"]=dict(ramp=sha(ramp),coast=sha(coast))
        self.record["prefixCertificateScope"]=(
            "Published R233 applies to its exact formal source only; literal floating evaluation remains unproved."
            if match else
            "Fresh numerical prefix identity. No R233 metric/curvature/C2 certificate is inherited.")
        self.publish_stage(dict(reportSHA256=sha(prefix_report),rampMasterSHA256=sha(ramp),
            coastMasterSHA256=sha(coast),R233InputBytesMatch=match,
            maximumSampledRepairedMetric=raw["repairedC2Prefix"]["maximumMetric"],
            maximumSampledRepairedCurvature=raw["repairedC2Prefix"]["maximumOwnCurvature"]))
        config=copy.deepcopy(json.loads(self.recipe.read_text())["config"])
        if any(k in config for k in ("z","schema","source","baseline","evaluation","interfaceProbeOnly")):
            raise ValueError("A real new no-z configuration is required")
        config["independentGapColdNewInput"]=dict(sourceEpoch=self.epoch,
            publicRecipeSHA256=sha(self.recipe),historicalAcceptedStepsInherited=0,
            originalFactoryGap=1,newWindowPrefixGap=1.05)
        config_file=self.out/"own-zero-config.json"
        write(config_file,config)
        initial=self.out/"own-zero-initial.json"
        self.stage("own-zero",["node","--expose-gc","--max-old-space-size=128",
            "--max-semi-space-size=4",self.scripts/"6a65-cauchy-global-position.cjs",
            "value",self.candidate,config_file,initial])
        raw=json.loads(initial.read_text())
        if (raw.get("schema")!="6a65-Cauchy-global-position-initial-v1"
            or raw.get("cauchyAcceptedSteps")!=0 or raw.get("accepted") is not False
            or raw.get("execution",{}).get("actualValueBaseline") is not True):
            raise ValueError("The factory did not actually create its own INITIAL/value")
        self.record["actualOwnCauchyInitialSHA256"]=sha(initial)
        self.publish_stage(dict(inputSHA256=sha(config_file),initialSHA256=sha(initial),
            dimension=len(raw["z"]),acceptedSteps=0,evaluation=scalar_value(raw["evaluation"])))
        cache_prefix=self.out/"direct-source-cache"
        self.stage("prepare",[sys.executable,self.scripts/"6a65-geometry-gap-window-cartesian.py",
            "prepare","--scripts",self.scripts,"--candidate",self.candidate,
            "--checkpoint",initial,"--ramp-master",ramp,"--coast-master",coast,
            "--run-id",self.run_id,"--prefix",cache_prefix])
        self.prepared=Path(str(cache_prefix)+"-prepared.json")
        raw=json.loads(self.prepared.read_text())
        identity=raw["definition"]["runIdentity"]
        if identity["actualRunId"]!=int(self.run_id) or identity["scope"]!="actual-same-job-new-source":
            raise ValueError("Direct caches must belong to this actual run")
        child=raw["actualNaturalChildExit"]["originalOracle"]
        if child.get("actualOSExitCode")!=0 or child.get("naturalExit") is not True:
            raise ValueError("The complete source oracle did not naturally exit zero")
        self.prepared_identity=raw["definition"]["sourceIdentity"]
        self.record["actualPreparedSHA256"]=sha(self.prepared)
        self.record["actualGapSourceIdentitySHA256"]=self.prepared_identity["identitySHA256"]
        self.publish_stage(dict(preparedSHA256=sha(self.prepared),
            definitionSHA256=raw["definitionSHA256"],ownAcceptedSteps=0,
            sourceDefinitionSHA256=raw["sourceMetadata"]["sourceDefinitionSHA256"],
            cacheHashes={k:v["SHA256"] for k,v in raw["caches"].items()},
            nodes={k:len(v["nodes"]) for k,v in raw["caches"].items()},
            angles={k:len(v["angles"]) for k,v in raw["caches"].items()},
            originalOracleNaturalExitCode=0))
        state=None
        for phase,key,entry in [
            ("single","singleGridAttempts","6a65-geometry-gap-window-cartesian.py"),
            ("joint","twoGridAttempts","6a65-geometry-gap-window-two-grid-cartesian.py"),
            ("refined","refinedAttempts","6a65-geometry-gap-window-refined-cartesian.py"),
            ("area","areaAttempts","6a65-geometry-gap-window-area-cartesian.py")]:
            for number in range(1,self.phases[key]+1):
                state,accepted=self.actual_step(phase,entry,state,number)
                if not accepted:
                    self.record["phaseProgress"][phase]["endedAfterActualRejectedAttempt"]=True
                    break
        self.save("requested-actual-cold-batch-complete-state-retained-topic-still-incomplete")
        self.publish("actual cold batch retained for own same-job followup")
        self.wait_followup()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--out-dir",type=Path,required=True)
    parser.add_argument("--request",type=Path,required=True)
    args=parser.parse_args()
    publisher=args.repo.resolve()/TOPIC/"scripts"/PUBLISHER
    if sha(publisher)!=PUBLISHER_SHA:raise ValueError("Verified publisher source hash mismatch")
    pub=module(publisher,"gap105_private_publication_adapter")
    pub.MARKER=MARKER
    # No Cartesian Controller.__init__, one(), run(), recipe or binder is used.
    Controller=type("GapColdController",(GapCold,pub.Controller),{})
    controller=Controller(args)
    try:controller.execute()
    except pub.RulesChanged:
        raise SystemExit(42)
    except BaseException as error:
        controller.record["actualFailure"]=dict(error=str(error),newAcceptanceNotInferred=True)
        try:
            controller.save("actual-cold-stage-failed")
            controller.publish("actual failure receipt")
        except BaseException as publication_error:
            print(json.dumps(dict(event="gap105-failure-publication-failed",
                error=str(publication_error))),flush=True)
        raise


if __name__=="__main__":main()
