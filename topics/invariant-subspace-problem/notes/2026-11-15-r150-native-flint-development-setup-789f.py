#!/usr/bin/env python3
"""Install the missing native exact-arithmetic headers in this temporary job."""
import argparse,json,os,pathlib,subprocess,time
p=argparse.ArgumentParser();p.add_argument("--out",required=True);a=p.parse_args();start=time.monotonic()
r={"format":"isp-native-flint-development-setup-v1","status":"running","parameters":{"package":"libflint-dev","maximumInstallSeconds":180,"temporaryJobEnvironmentOnly":True},"largeDataUploadedOrCommitted":False}
def run(cmd,seconds):
 try:
  q=subprocess.run(cmd,capture_output=True,text=True,timeout=seconds,env={**os.environ,"DEBIAN_FRONTEND":"noninteractive"})
  return {"argv":cmd,"exitCode":q.returncode,"stdout":q.stdout[-12000:],"stderr":q.stderr[-4000:]}
 except subprocess.TimeoutExpired as e:return {"argv":cmd,"exitCode":124,"error":"bounded native dependency setup timed out"}
header=pathlib.Path("/usr/include/flint/flint.h")
r["parameters"]["headerExistedBefore"]=header.is_file()
if not header.is_file():
 prefix=[] if os.geteuid()==0 else ["sudo","-n"]
 r["parameters"]["actualInstallation"]=run(prefix+["apt-get","install","-y","--no-install-recommends","libflint-dev"],180)
r["parameters"]["headerExistsAfter"]=header.is_file()
if header.is_file():
 r["parameters"]["headerVersionLines"]="\n".join(x for x in header.read_text(errors="replace").splitlines() if x.startswith("#define") and "VERSION" in x)
 r["parameters"]["packageVersion"]=run(["dpkg-query","-W","-f=${Version}","libflint-dev"],15)
 r["status"]="completed"
else:r["status"]="failed"
r["elapsedSeconds"]=time.monotonic()-start
out=pathlib.Path(a.out);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(r,sort_keys=True,indent=2)+"\n")
print(json.dumps({"status":r["status"],"elapsedSeconds":r["elapsedSeconds"]}))
raise SystemExit(0 if r["status"]=="completed" else 1)
