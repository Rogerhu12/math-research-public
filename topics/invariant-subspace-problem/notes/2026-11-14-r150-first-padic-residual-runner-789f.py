#!/usr/bin/env python3
"""Prepare exactly one original mod-31^2 residual in the fixed B=85 source space."""
import argparse,gzip,hashlib,json,subprocess,time
from pathlib import Path
FIXED={
 "normal-form-input.txt":"291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6",
 "nf-forward.bin":"66ab292e67681fa17d286fee516d830fa25017138e354f82dbb9c33e7f50976e",
 "nf-backward.bin":"cb396444652183924167e9cacaae888125c0e758e639af92b9784f7d1534132f",
 "nf-reduction.bin":"e977b75f618f30d00fd4edca3bdcadba1e5553a956bf4d781ee45df0d15c1e8b"}
def sha(p):
 h=hashlib.sha256()
 with Path(p).open("rb") as f:
  while b:=f.read(1048576):h.update(b)
 return h.hexdigest()
def main():
 p=argparse.ArgumentParser()
 for name in ("coefficients","coefficient-receipt","nf-dir","integer-model","integer-receipt","out"):p.add_argument("--"+name,type=Path,required=True)
 p.add_argument("--binary",type=Path);p.add_argument("--seconds",type=int,default=60);p.add_argument("--memory-mib",type=int,default=512);a=p.parse_args()
 if a.seconds<1 or a.memory_mib<1:raise ValueError("positive explicit bounds")
 a.out.mkdir(parents=True,exist_ok=True);root=Path(__file__).resolve().parent;source=root/"2026-11-14-r150-first-padic-residual-789f.cpp"
 c=json.loads(a.coefficient_receipt.read_text());m=json.loads(a.integer_receipt.read_text())
 if c.get("status")!="completed" or c["nativeStatistics"].get("standardKernelNormalForm") is not True or c["nativeStatistics"].get("fullNormalFormSourceIdentity") is not True:raise ValueError("complete canonical original source required")
 record=c["outputs"]["canonical-coefficients.bin"];payload=a.coefficients.read_bytes()
 if a.coefficients.suffix==".gz":
  if hashlib.sha256(payload).hexdigest()!=record["gzipSHA256"]:raise ValueError("canonical compressed hash")
  payload=gzip.decompress(payload)
 if hashlib.sha256(payload).hexdigest()!="9b324992d72d4bdf41e007e1ffe2474b494dc87b4d1c04ddf89a95094c54aec6" or hashlib.sha256(payload).hexdigest()!=record["sha256"]:raise ValueError("fixed canonical source hash")
 plain=a.out/"canonical-input.bin";plain.write_bytes(payload)
 for name,expected in FIXED.items():
  if sha(a.nf_dir/name)!=expected:raise ValueError("original provenance changed: "+name)
 if m.get("status")!="exact-integer-model-generated" or m.get("modulus")!=961 or m.get("h0Mod31Scale")!=25 or m["model"]["sha256"]!=sha(a.integer_model):raise ValueError("exact original integer model required")
 receipt={"format":"r150-first-original-padic-residual-run-v1","status":"preparing","prime":31,"modulus":961,"fixedSourceBudget":85,"inputSHA256":record["sha256"],"canonicalReceiptSHA256":sha(a.coefficient_receipt),"integerModelSHA256":sha(a.integer_model),"integerModelReceiptSHA256":sha(a.integer_receipt),"originalProvenanceSHA256":FIXED,"cppSHA256":sha(source),"runnerSHA256":sha(__file__),"secondsLimit":a.seconds,"memoryMiBLimit":a.memory_mib,"outputs":{}}
 rp=a.out/"first-padic-residual-receipt.json"
 def save():rp.write_text(json.dumps(receipt,indent=2)+"\n")
 save();binary=a.binary or a.out/"first-padic-residual"
 if not a.binary:
  r=subprocess.run(["timeout","--kill-after=10s","30s","prlimit","--as=536870912","--core=0","--","g++","-O2","-std=c++17",str(source),"-o",str(binary)],capture_output=True,text=True)
  if r.returncode:receipt.update(status="compile-failed",compileOutput=r.stdout+r.stderr);save();raise SystemExit(1)
 receipt.update(status="running",binarySHA256=sha(binary));save();prefix=a.out/"lift";started=time.monotonic()
 child=subprocess.Popen(["timeout","--kill-after=10s",f"{a.seconds}s","prlimit",f"--as={a.memory_mib*1048576}","--core=0","--",str(binary),str(plain),str(a.nf_dir/"normal-form-input.txt"),str(a.nf_dir/"nf-reduction.bin"),str(a.nf_dir/"nf-forward.bin"),str(a.nf_dir/"nf-backward.bin"),str(a.integer_model),str(prefix)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1);events=[]
 with (a.out/"first-padic-residual.log").open("w") as log:
  for line in child.stdout:
   log.write(line);log.flush();print(line,end="",flush=True)
   try:event=json.loads(line);events.append(event);receipt["lastProgress"]=event;save()
   except ValueError:pass
 code=child.wait();last=events[-1] if events else {}
 complete=code==0 and last.get("status")=="first-original-padic-residual-complete" and last.get("initialOriginalPrimitiveIdentityMod31") is True and last.get("allWeightedBoundsVerified") is True
 receipt.update(status="completed" if complete else "failed-or-incomplete",exitCode=code,elapsedSeconds=time.monotonic()-started,nativeStatistics=last,correctionComputed=False)
 if complete:
  for suffix in ("initial-standard-source.bin","first-residual.bin"):
   f=Path(str(prefix)+"-"+suffix);g=a.out/(suffix+".gz");g.write_bytes(gzip.compress(f.read_bytes(),mtime=0))
   if g.stat().st_size>5000000:raise ValueError("bounded first-lift artifact exceeds file limit")
   receipt["outputs"][suffix]={"bytes":f.stat().st_size,"sha256":sha(f),"gzipFile":str(g),"gzipBytes":g.stat().st_size,"gzipSHA256":sha(g)}
  f=Path(str(prefix)+"-first-residual.json");receipt["outputs"]["metadata"]={"file":str(f),"bytes":f.stat().st_size,"sha256":sha(f)}
 save();print(json.dumps(receipt))
 if not complete:raise SystemExit(1)
if __name__=="__main__":main()
