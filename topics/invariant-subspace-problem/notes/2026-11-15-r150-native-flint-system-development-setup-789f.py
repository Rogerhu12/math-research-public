#!/usr/bin/env python3
"""Install the actual native FLINT development dependency for this ephemeral research job.
Astra-ISP-789f; AI-assisted, GPT-6 Astra Pro. No mathematical solve.
"""
import argparse,hashlib,json,pathlib,shutil,subprocess,time
def run(cmd,limit,out,label):
 start=time.monotonic()
 try:
  p=subprocess.run(cmd,capture_output=True,text=True,timeout=limit,check=False)
  raw=(p.stdout+"\n"+p.stderr).encode()
  (out/(label+".log")).write_bytes(raw)
  return {"argv":cmd,"exitCode":p.returncode,"seconds":time.monotonic()-start,
          "temporaryLogBytes":len(raw),"temporaryLogSHA256":hashlib.sha256(raw).hexdigest(),
          "outputTail":raw[-2500:].decode(errors="replace")}
 except Exception as e:
  return {"argv":cmd,"seconds":time.monotonic()-start,"error":type(e).__name__+": "+str(e)[:500]}
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--out",type=pathlib.Path,required=True);a=ap.parse_args()
 a.out.mkdir(parents=True,exist_ok=True);start=time.monotonic();events=[]
 rec={"format":"isp-native-flint-system-development-setup-v1","status":"running",
      "newMathematicsRun":False,"packagesInstallationAttempted":False,
      "parameters":{"commands":events,"dependency":"libflint-dev","compiler":shutil.which("g++")}}
 if not pathlib.Path("/usr/include/flint/flint.h").is_file():
  rec["packagesInstallationAttempted"]=True
  events.append(run(["sudo","-n","apt-get","update","-qq"],110,a.out,"apt-update"))
  if events[-1].get("exitCode")==0:
   events.append(run(["sudo","-n","apt-get","install","-y","--no-install-recommends","libflint-dev"],110,a.out,"apt-install"))
 headers=pathlib.Path("/usr/include/flint/flint.h").is_file()
 rec["parameters"]["standardHeaderPresent"]=headers
 rec["parameters"]["packageVersion"]=run(["dpkg-query","-W","-f=$"+"{Version}\n","libflint-dev"],5,a.out,"package-version")
 if headers and rec["parameters"]["compiler"]:
  source=a.out/"native-flint-version-probe.cpp";binary=a.out/"native-flint-version-probe"
  source.write_text('#include <gmp.h>\n#include <flint/flint.h>\n#include <flint/fmpz.h>\n#include <iostream>\nint main(){fmpz_t z;fmpz_init(z);fmpz_set_ui(z,31);fmpz_mul(z,z,z);int ok=fmpz_cmp_ui(z,961)==0;std::cout<<"header="<<FLINT_VERSION<<" runtime="<<flint_version<<" exactProbe="<<ok<<"\\n";fmpz_clear(z);return ok?0:2;}\n')
  events.append(run([rec["parameters"]["compiler"],"-std=c++17","-O2",str(source),"-o",str(binary),"-lflint","-lgmp"],25,a.out,"compile-version"))
  if events[-1].get("exitCode")==0:events.append(run([str(binary)],5,a.out,"run-version"))
  rec["status"]="completed" if events[-1].get("exitCode")==0 and events[-1]["argv"]==[str(binary)] else "failed"
 else:rec["status"]="failed"
 rec["elapsedSeconds"]=time.monotonic()-start
 (a.out/"native-flint-system-development-setup-receipt.json").write_text(json.dumps(rec,separators=(",",":")))
 print(json.dumps(rec),flush=True)
 return 0 if rec["status"]=="completed" else 1
if __name__=="__main__":raise SystemExit(main())
