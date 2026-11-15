#!/usr/bin/env python3
"""Observe native exact-arithmetic toolchain; no installation or secret output."""
import argparse,json,pathlib,re,shutil,subprocess,time
def run(argv):
 try:
  p=subprocess.run(argv,capture_output=True,text=True,timeout=15)
  return {"argv":argv,"exitCode":p.returncode,"stdout":p.stdout[-6000:],"stderr":p.stderr[-2000:]}
 except Exception as e:return {"argv":argv,"error":type(e).__name__+": "+str(e)}
p=argparse.ArgumentParser();p.add_argument("--out",required=True);a=p.parse_args()
t=time.monotonic();r={"format":"isp-native-exact-toolchain-observation-v1","status":"completed","commands":[],"headers":[]}
for cmd in (["g++","-dumpfullversion"],["pkg-config","--modversion","flint"],["pkg-config","--cflags","--libs","flint"],["apt-cache","policy","libflint-dev"]):
 r["commands"].append(run(cmd))
for name in ("/usr/include/flint/flint.h","/usr/local/include/flint/flint.h"):
 q=pathlib.Path(name);z={"path":name,"exists":q.exists()}
 if q.is_file():z["versionMacros"]=[x for x in q.read_text(errors="replace").splitlines() if x.startswith("#define") and "VERSION" in x][:12]
 r["headers"].append(z)
q=run(["ldconfig","-p"]);r["nativeFlintLibraryLines"]=[x for x in q.get("stdout","").splitlines() if "libflint" in x]
try:
 import flint
 r["pythonFlintVersion"]=flint.__version__
 r["pythonFlintModule"]=flint.__file__
except ImportError:r["pythonFlintVersion"]=None
r["elapsedSeconds"]=time.monotonic()-t
out=pathlib.Path(a.out);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(r,sort_keys=True,indent=2)+"\n")
print(json.dumps({"status":"completed","receipt":str(out),"elapsedSeconds":r["elapsedSeconds"]}))
