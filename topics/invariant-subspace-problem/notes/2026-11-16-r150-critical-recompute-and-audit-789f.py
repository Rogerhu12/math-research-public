#!/usr/bin/env python3
"""Run the frozen critical generator, then audit every regenerated phase.

Astra-ISP-789f / literature_audit; AI-assisted GPT-6 Astra Pro,2026-11-16.
The original mathematical generator is unchanged. This wrapper genuinely
invokes it in the current job, then checks complete file and payload hashes.
No historical temporary matrix is downloaded or asserted to remain alive.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import subprocess
import resource

FORMAT="r150-critical-frozen-generator-recompute-and-audit-v1"
SOURCES={"weak":"f211696b5cb789f054e259648a54be7a60f2d8c7c7772d410143bc0025025b1b",
         "high":"de723d530fe0f2b3ab7876b76c8fc605a5156702309482f02a38c7b582a54753"}
PINS={
  "weak": {
    "plus": {
      "bytes": 29268,
      "sha256": "30043fb3e263f861166f439c198af93bc10a69a8c5940acad42fe0429c3d86e6",
      "binding": "fc1dd340764a2c3f419f2f8fa2cb13581585be8af1a680871ddac1d7fa157593",
      "manifest": {
        "bytes": 10739,
        "file": "checkpoints/manifest.json",
        "sha256": "3a6c668298211eb5831ab35876f59ce88be6f164f50077a7dbb2e8f402aa8e98"
      }
    },
    "minus": {
      "bytes": 29275,
      "sha256": "708cc521471fd10e493be27c206420ca34ef89db71a52791e3e0b5e21eb1954f",
      "binding": "108c040d0df21708a57e1bdc8ba64d796ad894d066476efa56871abd2ffa976d",
      "manifest": {
        "bytes": 10740,
        "file": "checkpoints/manifest.json",
        "sha256": "529a47b394c74f08558ef775f9a477c88d8a966ad536e06f85a10268dd6e8098"
      }
    },
    "e8": {
      "bytes": 29037,
      "sha256": "8b17d7ffc4bc63f6a8d8d7be42df1767c8fe1088958e4a8745e394ef4898d211",
      "binding": "6b2bd281d07a3796c302c5ca8a09d00f22433fb9501c62ff0df682733d8ce7f5",
      "manifest": {
        "bytes": 10411,
        "file": "checkpoints/manifest.json",
        "sha256": "555f91cb50825c78aec5bafc8289bc277fd9f8a30e76a775f7aaa33bf49fdcf3"
      }
    }
  },
  "high": {
    "plus": {
      "bytes": 12261,
      "sha256": "34504275623760b13b74ab4746926f5dc89d0bbf8a786b45c3a373adde1b69b7",
      "binding": "49f79a0f8c89b261868e3835ef01f0b173734e68ff8be96cbc1ca38896abf0ea",
      "manifest": {
        "bytes": 3482,
        "file": "checkpoints/manifest.json",
        "sha256": "da2dc0adfb911c71d0190ff516e52d654cd5505f804fd583ca76141e20c9e3a4"
      }
    },
    "minus": {
      "bytes": 12270,
      "sha256": "33a5d87d1f2ba462964be813327f8325577669dfa9b9515da2274d631c6b73d6",
      "binding": "f85f8011f03eaa6186559605b9280f3a854967574d086e4a946ddd8cd9e802f9",
      "manifest": {
        "bytes": 3482,
        "file": "checkpoints/manifest.json",
        "sha256": "3c75abb80733d5d0c1d65ebaa29b60365c0e0f5d2aafb987033985a148734cdf"
      }
    },
    "e8": {
      "bytes": 12248,
      "sha256": "ce2556100ea766678d9f8a84f6113a0f9c8fcb74221bb4b9e14a53f44cf125c2",
      "binding": "89b91030231d050f82cf672b48a8847744fad4c1bc90e2d306bfe84f8eacbcec",
      "manifest": {
        "bytes": 3484,
        "file": "checkpoints/manifest.json",
        "sha256": "9333e2b88ec31fa65e3f323c993eb9ad0bd1d66a3bd752b1bb065b991f4d0008"
      }
    }
  }
}

def require(v,m):
    if not v:raise AssertionError(m)

def canonical(x):
    return json.dumps(x,sort_keys=True,separators=(",",":")).encode()

def sha_file(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(1048576),b""):h.update(b)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--stage",choices=("weak","high"),required=True)
    ap.add_argument("--field",choices=("plus","minus","e8"),required=True)
    ap.add_argument("--generator-source",required=True)
    ap.add_argument("--generated-out",required=True)
    ap.add_argument("--runtime-receipt",required=True)
    ap.add_argument("--paid-outer",required=True)
    ap.add_argument("--out",required=True)
    ap.add_argument("--generator-timeout",type=float,default=330)
    ap.add_argument("--memory-mib",type=int,default=2048)
    ap.add_argument("--generator-arguments",nargs=argparse.REMAINDER,required=True)
    a=ap.parse_args()
    require(0<a.generator_timeout<=1800 and 512<=a.memory_mib<=8192,"Explicit resources")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    start=time.monotonic()
    output=Path(a.out);output.mkdir(parents=True,exist_ok=True)
    receipt=output/"critical-recomputation-identity-receipt.json"
    result={"format":FORMAT,"status":"started","scriptSHA256":sha_file(__file__),
            "parameters":{"stage":a.stage,"field":a.field,"paidAncestryReadOnly":True,
              "mathematicsExecutedOnlyByTheFrozenGenerator":True,
              "newMathematicalAlgorithm":False,
              "currentRunId":os.environ.get("GITHUB_RUN_ID"),
              "largeArraysUploadedOrCommitted":False}}
    code=1
    try:
        pin=PINS[a.stage][a.field]
        pp=Path(a.paid_outer);rp=Path(a.runtime_receipt)
        require(pp.stat().st_size==pin["bytes"] and sha_file(pp)==pin["sha256"],
                "Exact immutable original actual outer")
        old=json.loads(pp.read_text())
        require(old["exitCode"]==0 and old["result"]["status"]=="completed",
                "Only completed paid ancestry")
        require(sha_file(a.generator_source)==SOURCES[a.stage],
                "Exactly the mathematical generator used by the completed predecessor task")
        require(Path(a.generated_out).resolve()!=output.resolve(),"Separate actual generator and audit outputs")
        require(a.generator_arguments and "--out" in a.generator_arguments,
                "Actual explicit frozen-generator arguments")
        oi=a.generator_arguments.index("--out")
        require(oi+1<len(a.generator_arguments) and
                Path(a.generator_arguments[oi+1]).resolve()==Path(a.generated_out).resolve(),
                "Generator writes only the declared current-job output")
        result["parameters"]["canonicalCacheExistedBeforeInvocation"]=(Path(a.generated_out)/"checkpoints"/"manifest.json").exists()
        log=output/"frozen-generator.log"
        with log.open("wb") as f:
            proc=subprocess.run([sys.executable,str(Path(a.generator_source).resolve())]+a.generator_arguments,
                stdout=f,stderr=subprocess.STDOUT,timeout=a.generator_timeout,check=False)
        result["parameters"]["actualGeneratorExitCode"]=proc.returncode
        result["parameters"]["actualGeneratorInvoked"]=True
        result["parameters"]["generatorLog"]={"file":log.name,"bytes":log.stat().st_size,"sha256":sha_file(log)}
        require(proc.returncode==0,"Actual frozen generator did not complete; its phase checkpoints are preserved")
        raw=rp.read_bytes();actual=json.loads(raw)
        require(actual["scriptSHA256"]==SOURCES[a.stage] and
                old["result"]["scriptSHA256"]==SOURCES[a.stage] and
                actual["binding"]==pin["binding"]==old["result"]["binding"] and
                actual["status"]=="completed" and actual["parameters"]["field"]==a.field,
                "New runtime completed with exactly the same mathematical inputs")
        root=Path(a.generated_out)/"checkpoints";mf=root/"manifest.json"
        require(root.is_dir() and mf.stat().st_size==pin["manifest"]["bytes"]
                and sha_file(mf)==pin["manifest"]["sha256"],
                "Every freshly generated phase has the original complete manifest identity")
        manifest=json.loads(mf.read_text())
        require(manifest["binding"]==pin["binding"] and
                actual["parameters"]["checkpointManifest"]==pin["manifest"],
                "Actual new runtime reports the exact original phase identities")
        records=[]
        for name,r in sorted(manifest["stages"].items()):
            require(Path(r["file"]).name==r["file"],"Local immutable generation basename")
            path=root/r["file"]
            require(path.stat().st_size==r["bytes"] and sha_file(path)==r["sha256"],
                    "Every full generated phase file checked")
            with gzip.open(path,"rb") as z:data=z.read()
            require(hashlib.sha256(data).hexdigest()==r["payloadSHA256"],
                    "Every decompressed complete payload checked")
            v=json.loads(data)
            require(v["format"]==manifest["format"] and v["binding"]==pin["binding"]
                    and v["stage"]==name and v["verified"]==r["verified"],
                    "All mathematical phase names, bindings and proof statuses retained")
            records.append({"stage":name,"bytes":r["bytes"],"sha256":r["sha256"],
                            "payloadSHA256":r["payloadSHA256"],"verified":r["verified"]})
        if a.stage=="weak":
            require(actual["parameters"]["allOriginal6188JetProductsZero"] and
                    actual["parameters"]["candidateLeadingRank"]==9 and
                    actual["parameters"]["actualCanonicalLow"]["allEarlierRowsZero"],
                    "New complete original weak135 computation gates")
        else:
            require(actual["parameters"]["completeHighKernelProved"] and
                    actual["parameters"]["trueHighKernelColumns"]==7 and
                    actual["parameters"]["all6018OriginalHighProductsZero"] and
                    actual["parameters"]["independentColumns"],
                    "New actual complete number-field seven-kernel gates")
        identity={"oldOuter":pin,"newRuntimeReceipt":{"file":rp.name,"bytes":len(raw),
            "sha256":hashlib.sha256(raw).hexdigest()},"generatorSourceSHA256":SOURCES[a.stage],
            "manifest":pin["manifest"],"currentRunId":os.environ.get("GITHUB_RUN_ID"),
            "generatorArguments":a.generator_arguments}
        result["binding"]=hashlib.sha256(canonical({"format":FORMAT,
            "scriptSHA256":result["scriptSHA256"],"identity":identity})).hexdigest()
        result["parameters"].update({"identity":identity,"phaseCount":len(records),
           "allFullPhaseFilesAndPayloadsVerified":True,"exactOriginalManifestMatched":True,
           "allOriginalRuntimeMathematicalGatesPassed":True,"phases":records,
           "newRuntimeIsNotAnAssertionThatOldTemporaryFilesSurvived":True,
           "theOriginalMathematicalBindingDoesNotDependOnJobOrOutputDirectory":True})
        result["status"]="completed";code=0
    except Exception as exc:
        interrupted=isinstance(exc,subprocess.TimeoutExpired) or result["parameters"].get("actualGeneratorExitCode") in (75,124)
        result["status"]="budget-checkpoint" if interrupted else "failed"
        code=75 if interrupted else 1
        result["parameters"]["error"]={"type":type(exc).__name__,"message":str(exc)}
    result["elapsedSeconds"]=time.monotonic()-start
    raw=canonical(result);require(len(raw)<90000,"Small exact recomputation audit")
    tmp=receipt.with_name(receipt.name+".tmp");tmp.write_bytes(raw);tmp.replace(receipt)
    print(json.dumps({"status":result["status"],"receipt":str(receipt),
        "bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),
        "elapsedSeconds":result["elapsedSeconds"]},sort_keys=True),flush=True)
    return code

if __name__=="__main__":
    sys.exit(main())
