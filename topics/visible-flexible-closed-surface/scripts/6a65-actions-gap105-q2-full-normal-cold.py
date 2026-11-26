#!/usr/bin/env python3
"""Cold-regenerate the actual gap branch, then use a new complete-H q=2 solver.

This is a new Actions orchestration identity, not a recovered checkpoint.
Only the verified v5 git/publish/process methods are reused; publication is a
small Markdown conclusion, never a complete Actions output. Its Cartesian
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
MARKER="<!-- 6a65-gap105-q2-full-normal-ci-rules -->"
PUBLISHER="6a65-actions-cartesian-channel-block-v5-20261126.py"
PUBLISHER_SHA="5055b47a891bb106557842976a6f4766121edf893605fd7a551a39c223283d29"
R233_RAMP="0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7"
R233_COAST="f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d"
SCHEMA="6a65-gap105-q2-full-normal-cold-scratch-ledger-v1"
FULL_ENTRY="6a65-geometry-gap-window-area-power-two-full-normal.py"
FULL_ENTRY_SHA="2af9f7fac1a74b327007952e473f7498de6a1a9fee99ca6cd269222e6e5d80c4"
FULL_SCHEMA="6a65-gap105-complete14-q2-full-physical-normal-fixed-g-Cartesian-v1"


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
        if self.request.get("schema")!="6a65-gap105-q2-full-normal-cold-request-v1":
            raise ValueError("An explicit new-gap whole-branch request is required")
        if self.request.get("ruleCheckSeconds")!=2700:
            raise ValueError("This adapter uses the verified 45-minute publisher check")
        followup=Path(self.request["followupRelative"])
        if (followup.parent!=TOPIC/"ci-requests" or ".." in followup.parts
            or not re.fullmatch("6a65-[A-Za-z0-9_-]+[.]json",followup.name)
            or self.request.get("receiverPollSeconds")!=30):
            raise ValueError("A dedicated small same-job packet path and 30-second poll are required")
        self.phases=self.request["phases"]
        expected=dict(singleGridAttempts=6,twoGridAttempts=9,refinedAttempts=3,areaAttempts=12)
        if any(self.phases.get(key)!=count for key,count in expected.items()):
            raise ValueError("The known 6+9+3+12 attempt prefix must be regenerated unchanged")
        count=self.phases.get("fullNormalAttempts")
        if type(count) is not int or not 1<=count<=100:
            raise ValueError("Explicit bounded new q=2 full-normal attempt budget required")
        if (self.request.get("publication")!="small-Markdown-conclusions-with-run-parameters-output-SHA-only"
            or self.request.get("fullNormalEntrySHA256")!=FULL_ENTRY_SHA):
            raise ValueError("New source identity and README15 Markdown-only publication are required")
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
        self.report_stem=f"2026-11-26-6a65-gap105-q2-full-normal-{self.run_id}-{self.attempt}"
        self.receipt=self.out/"current-scalar-receipt.json"
        self.report=self.repo/TOPIC/"notes"/(self.report_stem+".md")
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
            observedPrefixAttemptBudgets=dict(single=6,joint=9,refined=3,area=12),
            reproductionNeverCountedAsNewScientificSteps=True,
            actualNewFullNormalAcceptedSteps=0,fullNormalEntrySHA256=FULL_ENTRY_SHA,
            publication="one-small-Markdown-conclusion; raw complete ledgers remain RUNNER_TEMP",
            legacyCertificateNamedFlagsAreNotProof=True,
            R233InputBytesMatch=None,literalEvaluatorRoundingCertified=False,
            continuousCertificate=False,strongTargetComplete=False)
        self.git("config","--local","user.name","Astra-visible-flex-6a65")
        self.git("config","--local","user.email","41898282+github-actions[bot]@users.noreply.github.com")
        self.git("switch","-c",f"visible-flex-gap105-q2-full-normal-{self.run_id}-{self.attempt}")

    def save(self,status):
        self.record.update(state=status,actualPipelineAcceptedSteps=self.own_count,
            actualPipelineAttempts=self.attempt_count,
            updatedUTC=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),
            currentStateSHA256=sha(self.parent_state) if self.parent_state else None)
        # Full computational ledgers are scratch only, per root README 15.
        write(self.receipt,self.record)
        stage=self.record.get("stageResult") or self.record.get("lastCompletedStageResult") or {}
        partial=self.record.get("actualSavedStateBeforeFailedProcess")
        if self.record.get("actualFailure") and partial:
            stage=partial
        value=stage.get("evaluation") or {}
        baseline=stage.get("actualOwnBaseline") or {}
        area=value.get("areaBarrierStatistics") or {}
        lines=[
            "# 新 gap 支 q=2 全物理法矩阵：实际 run "+self.run_id+"/"+self.attempt,
            "",
            "**可信度：数值证据；课题尚未完成。** 本页只记结论、参数和输出身份；完整可重算报告、状态与缓存仅留本 runner。",
            "",
            "状态："+status+"；记录时间 "+self.record["updatedUTC"]+"。静态本页不是进程存活证明。",
            "实际阶段："+str(self.record.get("stage","source-freeze"))+"。",
            "",
            "## 冻结输入与计算",
            "",
            "- 触发提交："+self.epoch+"；run "+self.run_id+"，attempt "+self.attempt+"。",
            "- 请求 SHA-256："+self.record["requestSHA256"]+"；controller SHA-256："+self.record["controllerSHA256"]+"。",
            "- 完整冻结源码清单 SHA-256："+self.record["frozenSourceInventorySHA256"]+"。",
            "- 使用同 job 的新 prefix、own-zero、完整 source cache，先真实运行旧 6+9+3+12 配方，再运行独立 q=2 全 H 入口；旧段重生不算新科学接受。",
            "- 新入口 SHA-256："+FULL_ENTRY_SHA+"。全部 5292 列、两组原 13 行和倒面积平方行保留；固定物理 g，原 lambda*S 二次型不变，默认 eta=lambda。",
            "",
            "## 实际接受计数",
            "",
            "| 阶段 | 实际尝试 | 实际接受 | 身份 |",
            "|---|---:|---:|---|"]
        for phase,progress in self.record["phaseProgress"].items():
            kind="本次新完整求解" if phase=="full-normal" else "已观察配方的实际重生"
            lines.append("| "+phase+" | "+str(progress["attempts"])+" | "+
                         str(progress["acceptedSteps"])+" | "+kind+" |")
        lines.extend(["",
            "当前总实际接受 "+str(self.own_count)+"；其中新 full-normal 接受 "+
            str(self.record.get("actualNewFullNormalAcceptedSteps",0))+
            "。baseline/value 不算接受，完整自然退出与接受分别记录。",
            "", "## 最新实际结论", ""])
        if value:
            def number(x):
                return "未返回" if x is None else format(float(x),".16g")
            fields=[("全目标 R²",baseline.get("squaredNorm"),value.get("squaredNorm")),
                    ("最大 sampled metric",baseline.get("maxRelativeMetric"),value.get("maxRelativeMetric")),
                    ("最大 sampled 曲率",baseline.get("maxCurvature"),value.get("maxCurvature")),
                    ("最小归一 Gram 行列式",baseline.get("minImmersion"),value.get("minImmersion")),
                    ("最小 held 距离",baseline.get("minHeldDistance"),value.get("minHeldDistance"))]
            lines.extend(["| 指标 | 本步实际 baseline | 本步实际返回 |","|---|---:|---:|"])
            for label,before,after in fields:
                lines.append("| "+label+" | "+number(before)+" | "+number(after)+" |")
            if area:
                lines.append("")
                lines.append("实际最小面积比 sigma="+number(area.get("minAreaRatio"))+
                             "；面积项 R²="+number(area.get("squaredNorm"))+
                             "。minImmersion 是面积比平方，不是面积比。")
            lines.extend(["","本步 accepted="+str(stage.get("accepted"))+
                          "；参与目标的两个网格都实际重评，不称第三独立密观察。"])
        else:
            if "maximumSampledRepairedMetric" in stage:
                lines.append("本次新 prefix sampled metric="+str(stage["maximumSampledRepairedMetric"])+
                             "，sampled curvature="+str(stage["maximumSampledRepairedCurvature"])+
                             "；这是源生成诊断，不是完整曲面的接受步。")
            elif "cacheHashes" in stage:
                lines.append("实际完整 source cache 已生成，oracle 自然 exit 0；径向点数 "+
                             str(stage["nodes"])+"，整周角数 "+str(stage["angles"])+"。缓存生成不算接受。")
            else:
                lines.append("本阶段尚无完整数值评价可列；不推断成功、接受或失败。")
        if stage.get("fullNormalSolves"):
            lines.extend(["","完整物理法矩阵实际求解："])
            for solve in stage["fullNormalSolves"]:
                lines.append("- lambda="+str(solve["damping"])+", eta="+str(solve["eta"])+
                    "；LSMR istop="+str(solve["istop"])+", iterations="+str(solve["iterations"])+
                    "；原物理 normal 相对残差="+str(solve["originalPhysicalNormalRelativeResidual"])+
                    "；组装 "+str(solve["assemblySeconds"])+" s，带因子 "+str(solve["factorSeconds"])+" s。")
        lines.extend(["","## 实际退出与输出 SHA-256",""])
        for child in self.record.get("processReceipts",[]):
            lines.append("- "+child["label"]+": OS exit "+str(child["OSExitCode"])+
                         "，"+str(child["seconds"])+" s；stdout "+child["stdoutSHA256"]+"。")
        for key in ("sameJobStateSHA256","actualOwnBaselineSHA256","actualSolveReportSHA256",
                    "reportSHA256","rampMasterSHA256","coastMasterSHA256","initialSHA256","preparedSHA256"):
            if stage.get(key):lines.append("- "+key+": "+str(stage[key])+"。")
        if self.parent_state:lines.append("- 当前实际 state: "+sha(self.parent_state)+"。")
        lines.append("- 完整 scratch ledger: "+sha(self.receipt)+"。")
        lines.extend(["",
            "prefix 是否逐字匹配 R233 原 master："+str(self.record.get("R233InputBytesMatch"))+
            "。不匹配时不继承 R233；浮点评估连续误差未因此得到认证。",
            "以上 sampled 数值、求解器退出和有限接受均不能代替连续域 metric、reach、全部时间或完成标准的证明。"])
        pulls=self.record.get("pulls",[])
        if pulls:
            last=pulls[-1]
            lines.extend(["","## 规则回执","",
                "最近真实 pull 至 "+last["toCommit"]+"；"+last["UTC"]+
                "；双 README 无差异="+str(last["readmeDiffEmpty"])+"。该 SHA 同步记入 HANDOFF。"])
        if self.record.get("actualFailure"):
            lines.extend(["","实际失败："+str(self.record["actualFailure"]["error"])+
                          "。失败不产生推断的接受步。"])
            if partial:
                lines.append("上列当前态是失败前实际已保存并绑定父态的文件；本进程仍为非零退出，不称自然完成。")
        if self.record.get("unreviewedReadmeDiffSHA256"):
            lines.extend(["","双 README 已变化，差异已打印、数值停止；差异 SHA-256 "+
                          self.record["unreviewedReadmeDiffSHA256"]+"，待 root 应用。"])
        raw=("\n".join(lines)+"\n").encode()
        if len(raw)>=24000:raise ValueError("The Markdown conclusion must remain compact; no output dump fallback")
        self.report.write_bytes(raw)

    def rotate(self,label):
        self.serial+=1
        self.record["stageNumber"]=self.serial
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
        self.record["lastCompletedStageResult"]=result
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
        if phase=="full-normal":
            if sha(self.scripts/entry)!=FULL_ENTRY_SHA:
                raise ValueError("Frozen full-normal entry identity changed")
            command+=["--operator-epoch",self.epoch]
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
                    if phase=="full-normal":
                        if (partial.get("schema")!=FULL_SCHEMA+"-checkpoint"
                            or partial.get("entrySHA256")!=FULL_ENTRY_SHA
                            or partial.get("modelDefinition",{}).get("operatorSourceEpoch")!=self.epoch
                            or partial.get("fullBandAcceptedSteps")!=self.record.get("actualNewFullNormalAcceptedSteps",0)+int(added)):
                            raise ValueError("Partial full-normal checkpoint source/counter mismatch")
                        self.record["actualNewFullNormalAcceptedSteps"]=partial["fullBandAcceptedSteps"]
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
        if phase=="full-normal":
            if (result.get("schema")!=FULL_SCHEMA+"-checkpoint"
                or result.get("entrySHA256")!=FULL_ENTRY_SHA
                or result.get("fullNormalHelperSHA256")!=self.request["sourceSHA256"][
                    "6a65-cartesian-complete-radial-normal-two-grid-area.py"]
                or result.get("sameQ2LMQuadraticAsOriginalQ2Entry") is not True
                or result["fullBandAcceptedSteps"]!=self.record.get("actualNewFullNormalAcceptedSteps",0)+int(added)
                or result["modelDefinition"].get("operatorSourceEpoch")!=self.epoch):
                raise ValueError("Actual q=2 full-normal model/counter/source epoch mismatch")
        output=dict(accepted=added,sameJobStateSHA256=sha(file),
            actualOwnBaselineSHA256=sha(baseline),
            actualOwnBaseline=scalar_value(json.loads(baseline.read_text())["evaluation"]),
            actualSolveReportSHA256=sha(report),
            dimension=len(result["z"]),evaluation=scalar_value(result["evaluation"]),
            actualPipelineAcceptedSteps=total,
            dampingStartForEachProcess=1e-4,
            oneProcessOneAttempt=True,oldNumericalMetricsNotInherited=True)
        if "observed" in result:output["independentObserver"]=scalar_value(result["observed"])
        if "groupValues" in result:
            output["bothActualGroups"]={k:scalar_value(v) for k,v in result["groupValues"].items()}
        if phase=="full-normal":
            solves=[row for row in result.get("trace",[]) if row.get("kind")=="actual_complete14_LSMR"]
            if not solves:raise ValueError("A real complete full-normal solve receipt is required")
            output["fullNormalSolves"]=[]
            for row in solves:
                if (row.get("LSMRDamp")!=0. or row.get("oldLMQuadraticUnchanged") is not True
                    or row.get("completeColumns")!=5292
                    or row.get("originalRegularizerRows")!=5292):
                    raise ValueError("The actual original LM rows/columns/regularizer changed")
                output["fullNormalSolves"].append(dict(
                    **{key:row[key] for key in ("damping","eta","istop","iterations","originalPhysicalNormalRelativeResidual")},
                    assemblySeconds=row["assembly"]["seconds"],
                    factorSeconds=row["assembly"]["timings"]["bandCholeskySeconds"]))
            if not added and json.loads(state.read_text())["z"]!=result["z"]:
                raise ValueError("A stalled full-normal attempt changed the actual saved field")
            self.record["actualNewFullNormalAcceptedSteps"]=result["fullBandAcceptedSteps"]
        self.own_count=total
        self.attempt_count+=1
        self.parent_state=file
        progress=self.record["phaseProgress"].setdefault(phase,dict(attempts=0,acceptedSteps=0))
        progress["attempts"]+=1
        progress["acceptedSteps"]+=int(added)
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
            if packet.get("schema")!="6a65-gap105-q2-full-normal-same-job-followup-v1":
                raise ValueError("Explicit gap105 same-job followup schema required")
            expected=dict(run_id=self.run_id,run_attempt=self.attempt,
                source_epoch=self.epoch,requestSHA256=self.record["requestSHA256"],
                parentStateSHA256=sha(self.parent_state),preparedSHA256=sha(self.prepared))
            for key,value in expected.items():
                if packet.get(key)!=value:raise ValueError("Followup binding mismatch: "+key)
            operation=packet.get("operation")
            if operation not in ("additional_full_normal_attempts","release"):
                raise ValueError("Only unchanged-model q=2 full-normal attempts or release are supported")
            if operation=="additional_full_normal_attempts":
                count=packet.get("additional_full_normal_attempts")
                if type(count) is not int or not 1<=count<=100:
                    raise ValueError("A bounded explicit additional attempt count is required")
                if self.record["phaseProgress"]["full-normal"].get("endedAfterActualRejectedAttempt"):
                    raise ValueError("The unchanged q=2 full-normal model already rejected; only release is accepted")
            elif packet.get("additional_full_normal_attempts",0)!=0:
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
            actual_packet=self.repo/Path(self.request["followupRelative"])
            if not actual_packet.exists() or sha(actual_packet)!=received["packetSHA256"]:
                self.record["lastIgnoredFollowup"]=dict(packetSHA256=received["packetSHA256"],
                    reason="Packet changed between read-only fetch and actual pull; not consumed")
                continue
            if packet["operation"]=="release":
                self.save("explicitly-released-actual-runner-state-topic-still-incomplete")
                self.publish("explicit release of gap runner")
                return
            for unused in range(packet["additional_full_normal_attempts"]):
                number=self.record["phaseProgress"]["full-normal"]["attempts"]+1
                state,accepted=self.actual_step("full-normal",FULL_ENTRY,self.parent_state,number)
                if not accepted:
                    self.record["phaseProgress"]["full-normal"]["endedAfterActualRejectedAttempt"]=True
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
        self.record["actualReproducedPrefixAcceptedSteps"]=self.own_count
        for number in range(1,self.phases["fullNormalAttempts"]+1):
            state,accepted=self.actual_step("full-normal",FULL_ENTRY,state,number)
            if not accepted:
                self.record["phaseProgress"]["full-normal"]["endedAfterActualRejectedAttempt"]=True
                break
        self.save("requested-actual-q2-full-normal-batch-complete-state-retained-topic-still-incomplete")
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
    pub=module(publisher,"gap105_full_normal_private_publication_adapter")
    pub.MARKER=MARKER
    # No Cartesian Controller.__init__, one(), run(), recipe or binder is used.
    Controller=type("GapQ2FullNormalColdController",(GapCold,pub.Controller),{})
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
