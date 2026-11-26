#!/usr/bin/env python3
"""Finite orchestration/Markdown check, without Git/network/numerical work.

The controller rendering object is explicitly synthetic. It never creates a
research checkpoint, reports an actual research acceptance, or runs a child.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import textwrap


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ("controller","request","workflow","scripts","output"):
        ap.add_argument("--"+name,type=Path,required=True)
    args=ap.parse_args()
    if args.output.exists():raise FileExistsError("Fresh fixture output required")
    spec=importlib.util.spec_from_file_location("q2_full_normal_controller_fixture",args.controller)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    request=json.loads(args.request.read_text())
    pinned=[]
    for filename,digest in request["sourceSHA256"].items():
        path=args.controller.parent/filename
        if not path.is_file():path=args.scripts/filename
        if sha(path)!=digest:raise ValueError("Actual source pin mismatch: "+filename)
        pinned.append(filename)
    if request["fullNormalEntrySHA256"]!=module.FULL_ENTRY_SHA:
        raise ValueError("Full-normal entry identity mismatch")
    if request["phases"]!={"singleGridAttempts":6,"twoGridAttempts":9,
        "refinedAttempts":3,"areaAttempts":12,"fullNormalAttempts":40}:
        raise ValueError("Declared complete pipeline changed")
    workflow=args.workflow.read_text()
    lines=workflow.splitlines();shell_blocks=0
    for index,line in enumerate(lines):
        found=re.match(r"^(\s*)run:\s*\|\s*$",line)
        if not found:continue
        depth=len(found.group(1));rows=[]
        for row in lines[index+1:]:
            if row.strip() and len(row)-len(row.lstrip())<=depth:break
            rows.append(row)
        body=textwrap.dedent("\n".join(rows))+"\n"
        subprocess.run(["bash","-n"],input=body,text=True,check=True)
        shell_blocks+=1
    required=("--unshallow origin main","merge-base --is-ancestor",
        "timeout-minutes: 350",module.FULL_ENTRY,args.controller.name,args.request.name)
    if any(part not in workflow for part in required):
        raise ValueError("Workflow lost an actual source/ancestry/time binding")
    with tempfile.TemporaryDirectory(prefix="q2-md-fixture-",dir=args.output.parent) as directory:
        base=Path(directory);repo=base/"synthetic-repo";repo.mkdir()
        controller=module.GapCold.__new__(module.GapCold)
        controller.repo=repo;controller.out=base
        controller.report=repo/"fixture-only.md"
        controller.receipt=base/"scratch-ledger.json"
        controller.run_id="fixture-not-an-actual-Actions-run"
        controller.attempt="fixture"
        controller.epoch="fixture-not-a-source-commit"
        controller.own_count=controller.attempt_count=0
        controller.parent_state=None
        controller.record=dict(requestSHA256=sha(args.request),controllerSHA256=sha(args.controller),
            frozenSourceInventorySHA256=sha(args.workflow),phaseProgress={},processReceipts=[],pulls=[],
            syntheticFixtureOnly=True,doNotPublishThisFixtureObject=True,
            omittedRawSentinel=["NOT_A_PUBLIC_OUTPUT_DUMP"])
        controller.save("synthetic-before-any-child")
        first=controller.report.read_text()
        if not first.startswith("# ") or "NOT_A_PUBLIC_OUTPUT_DUMP" in first:
            raise ValueError("The single Markdown page must not serialize the full record")
        if "NOT_A_PUBLIC_OUTPUT_DUMP" not in controller.receipt.read_text():
            raise ValueError("Complete scratch ledger was not retained separately")
        # The code must render a real type of failure honestly; these example
        # values are synthetic and are never emitted as research results.
        controller.record["actualFailure"]=dict(error="synthetic partial-process failure")
        controller.record["actualSavedStateBeforeFailedProcess"]=dict(accepted=False,
            evaluation=dict(squaredNorm=2.,maxRelativeMetric=3.,maxCurvature=4.,
                            minImmersion=.25,minHeldDistance=.6))
        controller.save("synthetic-failure-fixture")
        second=controller.report.read_text()
        if "非零退出" not in second or "不称自然完成" not in second:
            raise ValueError("Partial saved output must not imply natural completion")
        files=list(repo.rglob("*"))
        if files!=[controller.report] or controller.report.suffix!=".md":
            raise ValueError("Only one Markdown output belongs to the synthetic repo")
        md_bytes=controller.report.stat().st_size
    receipt=dict(schema="6a65-q2-full-normal-controller-static-and-Markdown-fixture-v1",
        controllerSHA256=sha(args.controller),requestSHA256=sha(args.request),workflowSHA256=sha(args.workflow),
        fixtureSHA256=sha(__file__),sourcePinsChecked=len(pinned),bashSyntaxBlocks=shell_blocks,
        singleMarkdownOutputOnly=True,completeJSONLedgerKeptOutsideSyntheticRepo=True,
        syntheticFinalMarkdownBytes=md_bytes,partialFailureDoesNotClaimNaturalExit=True,
        existingPublisherImplementationUnchanged=True,mathematicalCalculationsRepeated=False,
        newGitPublicationExecuted=False,actualResearchChildrenExecuted=0,
        actualResearchAcceptedSteps=0,liveActionsExecution=False)
    args.output.write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps(receipt),flush=True)


if __name__=="__main__":main()
