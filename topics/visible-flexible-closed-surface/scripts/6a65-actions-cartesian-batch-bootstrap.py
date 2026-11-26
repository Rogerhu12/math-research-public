#!/usr/bin/env python3
"""Generate a real new source in this job, then retain actual Cartesian steps.

The known zero-Cauchy prefix is regenerated only as input. Its old acceptance
is not counted as new research. Complete direct-source caches stay in this
same runner; the numerical child never receives publication credentials.
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


cold=load("actual_batch_source_bootstrap",HERE/"6a65-actions-cartesian-cold-recovered-20261126.py")


class Bootstrap(cold.Controller):
    def __init__(self,args):
        super().__init__(args)
        self.child_env.pop("CART_CONTINUATION_TOKEN",None)
        self.record.update(bootstrapSHA256=cold.sha(__file__),
            completeSourceRecomputedInThisRunner=True,
            previouslyObservedPrefixIsInputRegenerationOnly=True,
            continuationEntry="6a65-actions-cartesian-same-model-v4-20261126.py")
        self.last_publication=time.monotonic()

    def publish(self,reason):
        super().publish(reason)
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
        if type(count) is not int or not 1<=count<=60 or type(prior) is not int or not 0<=prior<=count:
            raise ValueError("Explicit true attempt budget and observed regeneration prefix required")
        bootstrap.prepare()
        continuation_module=load("actual_batch_cached_continuation",
            bootstrap.scripts/"6a65-actions-cartesian-same-model-v4-20261126.py")
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
        rules_changed=isinstance(error,cold.RulesChanged) or (
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
