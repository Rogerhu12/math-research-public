#!/usr/bin/env python3
"""Read only a bounded small mathematical report from an existing Actions job.
Large encoded or coefficient payloads stay inside this runner and are not
printed, uploaded, committed, or passed through the connector."""
import os,json,re,hashlib,urllib.request,signal,resource
signal.alarm(60);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
REPO="Rogerhu12/math-research-public"
RUN=46058835795
JOB=140707871945
url=f"https://api.github.com/repos/{REPO}/actions/jobs/{JOB}/logs"
req=urllib.request.Request(url,headers={"Accept":"application/vnd.github+json",
 "Authorization":"Bearer "+os.environ["GH_TOKEN"],"User-Agent":"ISP-8542-small-status"})
events=[];receipt=None;capture=None;raw_sha=hashlib.sha256();raw_bytes=0
def small(value):
 if isinstance(value,int) and abs(value)>9007199254740991:return str(value)
 if isinstance(value,list):return [small(x) for x in value]
 if isinstance(value,dict):
  return {k:small(v) for k,v in value.items() if k not in
   {"data","dataChunk","starting_matrix","continuation",
    "complete_reduced_elementary_coefficients","complete_coefficients",
    "firstCombination","secondCombination","matrix"}}
 return value
with urllib.request.urlopen(req,timeout=40) as response:
 for raw in response:
  raw_sha.update(raw);raw_bytes+=len(raw)
  line=raw.decode("utf-8","replace").rstrip("\r\n")
  line=re.sub(r"^\d{4}-\d\d-\d\dT\S+\s+","",line)
  if line.startswith("ISP_EXECUTION_RECEIPT "):
   receipt=json.loads(line[len("ISP_EXECUTION_RECEIPT "):])
  elif line.startswith("ISP_SIX_MATRIX_HALF_EXACT_OUTPUT "):
   capture=json.loads(line[len("ISP_SIX_MATRIX_HALF_EXACT_OUTPUT "):])
  elif line.startswith("{"):
   try:obj=json.loads(line)
   except json.JSONDecodeError:continue
   if isinstance(obj,dict) and "stage" in obj and "chunk" not in obj["stage"].lower():
    events.append(small(obj))
  elif "Traceback " in line or re.match(r"^(AssertionError|MemoryError|ValueError|TypeError|ZeroDivisionError|OverflowError)",line):
   events.append({"exceptionLine":line[:1000]})
report={"schema":"isp-actual-run-small-report-v1","run":RUN,"job":JOB,
 "execution":receipt,"mathematicalStages":events,"captureMetadata":capture,
 "downloadedJobLogBytes":raw_bytes,"downloadedJobLogSHA256":raw_sha.hexdigest(),
 "largePayloadPrintedOrCommitted":False,"ordinaryISPClaim":False}
data=json.dumps(small(report),separators=(",",":"))
assert len(data.encode())<80000
print(data,flush=True)
signal.alarm(0)
