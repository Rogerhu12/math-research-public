#!/usr/bin/env python3
"""New same-equation channel-block solver, from a real source in this job.

Only the public original Cauchy source is regenerated as input. The new v5
Cartesian solver has no inherited acceptance. Direct-source caches and all
raw states stay in this runner; numerical children receive no Git tokens.
The publication adapter uses the separately verified v5 publisher unchanged.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
import os
from pathlib import Path
import selectors
import subprocess
import sys
import time
from types import SimpleNamespace

HERE=Path(__file__).resolve().parent


def load(name, filename):
    spec=importlib.util.spec_from_file_location(name, filename)
    value=importlib.util.module_from_spec(spec)
    sys.modules[name]=value
    spec.loader.exec_module(value)
    return value


cold=load("actual_channel_block_source_bootstrap",HERE/"6a65-actions-cartesian-cold-recovered-20261126.py")
publication=load("actual_channel_block_scalar_publication",
    HERE/"6a65-actions-cartesian-channel-block-v5-20261126.py")


class Bootstrap(cold.Controller):
    def __init__(self,args):
        super().__init__(args)
        for name in ("CART_CONTINUATION_TOKEN","MR_TOKEN"):
            self.child_env.pop(name,None)
        # This adapter supplies exactly the scalar-publication contract. It
        # does not initialize a Cartesian controller or invent a Cartesian
        # baseline while the original source is still being generated.
        self.target=self.repo/cold.TOPIC/"notes"/(
            f"2026-11-26-6a65-cartesian-block-bootstrap-{self.run_id}-{self.attempt}.json")
        if self.target.exists():
            raise FileExistsError("Fresh bootstrap scalar namespace required")
        self.report=self.target
        self.total_pull_count=0
        self.own_count=0
        self.last_sync=time.monotonic()
        self.record.update(bootstrapSHA256=cold.sha(__file__),
            publicationControllerSHA256=cold.sha(HERE/"6a65-actions-cartesian-channel-block-v5-20261126.py"),
            completeSourceRecomputedInThisRunner=True,
            previouslyObservedPrefixIsInputRegenerationOnly=True,
            newSolverPriorAcceptedSteps=0,
            publicationPhase="actual-original-source-generation-before-any-Cartesian-attempt",
            continuationEntry="6a65-actions-cartesian-channel-block-v5-20261126.py",
            actualOwnAcceptedCount=0,pulls=[],actualTotalPullCount=0)
        expected_files={
            "bootstrapSHA256":HERE/"6a65-actions-cartesian-channel-block-bootstrap-v5.py",
            "continuationControllerSHA256":self.scripts/"6a65-actions-cartesian-channel-block-v5-20261126.py",
            "numericalEntrySHA256":self.scripts/"6a65-cartesian-independent-experiment-v5.py",
            "linearSolverSHA256":self.scripts/"6a65-cartesian-exact-channel-blocks.py"}
        for key,filename in expected_files.items():
            if cold.sha(filename)!=self.request.get(key):
                raise ValueError("Explicit new source hash mismatch: "+key)
        self.last_publication=time.monotonic()

    def save(self,status):
        self.snapshot(status)

    def publish(self,reason):
        # The inherited Git wrapper returns the same result types used by
        # this publisher: CompletedProcess for noncaptured pull/push, str
        # for successful captured reads. Credentials remain on this object.
        publication.Controller.publish(self,reason)
        self.last_publication=time.monotonic()

    def run_stage(self,name,command):
        log=self.out/(name+".log")
        if log.exists():raise FileExistsError("Fresh actual stage log required")
        start,began=time.monotonic(),cold.utc()
        cold.emit("new-batch-source-stage-start",stage=name,sourceEpoch=self.epoch)
        process=subprocess.Popen(command,cwd=self.frozen,env=self.child_env,
            stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        selector=selectors.DefaultSelector()
        selector.register(process.stdout,selectors.EVENT_READ)
        last_heartbeat=start
        try:
            with log.open("xb") as output:
                while selector.get_map():
                    for key,_ in selector.select(timeout=1):
                        chunk=os.read(key.fileobj.fileno(),65536)
                        if not chunk:
                            selector.unregister(key.fileobj)
                            continue
                        output.write(chunk)
                        output.flush()
                    now=time.monotonic()
                    if now-self.last_publication>=45*60:
                        self.snapshot("actual-new-source-process-running-no-new-exit-claimed")
                        self.publish("hourly rules during actual new source generation")
                    if now-last_heartbeat>=30:
                        cold.emit("actual-new-source-running",stage=name,UTC=cold.utc(),
                            elapsedSeconds=now-start,exitNotYetObserved=True)
                        last_heartbeat=now
                code=process.wait()
        except BaseException:
            process.terminate()
            try:process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.kill();process.wait()
            raise
        finally:
            selector.close()
            process.stdout.close()
        row=dict(stage=name,startedUTC=began,finishedUTC=cold.utc(),
            OSExitCode=code,seconds=time.monotonic()-start,
            stdoutSHA256=cold.sha(log),command=command)
        self.record["stages"].append(row)
        cold.write(self.out/"cold-execution-receipt.json",self.record)
        cold.emit("new-batch-source-stage-returned",**row)
        if code:raise RuntimeError("Actual source child failed: "+name+", exit "+str(code))

    def prepare(self):
        self.snapshot("before-actual-new-source-generation")
        self.publish("pre-process actual new source generation")
        node=["node","--expose-gc","--max-old-space-size=512","--max-semi-space-size=4"]
        self.run_stage("new-Cauchy-complete-value",node+[
            str(self.scripts/"6a65-cauchy-global-position.cjs"),"value",
            str(self.candidate),str(self.config),str(self.initial)])
        actual=json.loads(self.initial.read_text())
        if actual.get("cauchyAcceptedSteps")!=0 or actual.get("accepted") is not False or actual.get("interfaceProbeOnly"):
            raise ValueError("Actual complete new source and original zero count required")
        self.run_stage("new-Cauchy-same-field-observer",node+[
            str(self.scripts/"6a65-cauchy-same-field-observer-recovered-v2.cjs"),
            str(self.candidate),str(self.initial),str(self.observer),"4","256"])
        self.snapshot("actual-regenerated-source-and-matching-observer-ready-for-new-continuation")
        self.publish("actual source regeneration and matching observer exit 0")


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--request",type=Path,required=True)
    ap.add_argument("--directory",type=Path,required=True)
    bootstrap=None
    continuation=None
    continuation_module=None
    try:
        bootstrap=Bootstrap(ap.parse_args())
        request=bootstrap.request
        count=request.get("complete_attempts")
        prior=request.get("prior_observed_accepted")
        if type(count) is not int or not 1<=count<=60 or type(prior) is not int or prior!=0:
            raise ValueError("Explicit true attempt budget and zero inherited v5 acceptances required")
        bootstrap.prepare()
        continuation_module=load("actual_channel_block_cached_continuation",
            bootstrap.scripts/"6a65-actions-cartesian-channel-block-v5-20261126.py")
        args=SimpleNamespace(repo=bootstrap.repo,scripts=bootstrap.scripts,
            candidate=bootstrap.candidate,source=bootstrap.initial,
            source_observer=bootstrap.observer,recipe=bootstrap.recipe,
            out_dir=bootstrap.out/"continuation",source_epoch=bootstrap.epoch,
            rules_read_commit=bootstrap.last_rules,attempts=count,
            prior_observed_accepted=prior,cartesian_state=None,cartesian_observer=None,
            source_cache_directory=None,
            followup_relative=request["same_model_followup_path"])
        continuation=continuation_module.Controller(args)
        continuation.run()
    except BaseException as error:
        rules_changed=isinstance(error,(cold.RulesChanged,publication.RulesChanged)) or (
            continuation_module is not None and isinstance(error,continuation_module.RulesChanged))
        if rules_changed:
            cold.emit("actual-rule-difference-requires-root-application",error=str(error))
            raise
        if continuation is not None:
            continuation.record["actualFailure"]=dict(error=str(error),UTC=cold.utc(),newAcceptanceNotInferred=True)
            try:
                continuation.save("actual-process-or-controller-failure")
                continuation.publish("actual batch continuation failure receipt")
            except BaseException as failure:
                cold.emit("actual-continuation-failure-publication-also-failed",error=str(failure))
        elif bootstrap is not None:
            bootstrap.record["actualFailure"]=dict(error=str(error),atUTC=cold.utc(),acceptedStepsNotInferred=True)
            try:
                bootstrap.snapshot("failed-actual-batch-source-or-publication")
                bootstrap.publish("actual new-source failure receipt")
            except BaseException as failure:
                cold.emit("actual-source-failure-publication-also-failed",error=str(failure))
        raise


if __name__=="__main__":main()
