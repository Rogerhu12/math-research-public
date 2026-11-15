#!/usr/bin/env python3
"""Read-only FLINT native build inventory; no mathematics or installation.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
"""
import argparse,ctypes.util,glob,hashlib,json,os,pathlib,shutil,subprocess,sys,time
sys.dont_write_bytecode=True
def main():
 p=argparse.ArgumentParser();p.add_argument("--out",type=pathlib.Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True);start=time.monotonic()
 data={"format":"isp-native-flint-read-only-build-inventory-v1","status":"completed","newMathematicsRun":False,"packagesInstalled":False,"parameters":{}}
 import flint
 data["parameters"]["pythonFlintVersions"]={k:str(getattr(flint,k)) for k in ("__version__","__FLINT_VERSION__","__FLINT_RELEASE__") if hasattr(flint,k)}
 data["parameters"]["compiler"]=shutil.which("g++")
 commands=[["pkg-config","--modversion","flint"],["pkg-config","--cflags","--libs","flint"],["ldconfig","-p"]]
 results=[]
 for c in commands:
  try:
   r=subprocess.run(c,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=5,check=False)
   s=r.stdout
   if c[0]=="ldconfig":s="\n".join(z for z in s.splitlines() if any(k in z.lower() for k in ("flint","gmp","mpfr")))
   results.append({"argv":c,"exitCode":r.returncode,"stdout":s[:10000]})
  except Exception as e:results.append({"argv":c,"error":str(e)})
 data["parameters"]["commands"]=results
 roots=[pathlib.Path("/usr/include"),pathlib.Path("/usr/local/include"),pathlib.Path(sys.prefix)/"include"]
 data["parameters"]["headers"]=[str(r/"flint/flint.h") for r in roots if (r/"flint/flint.h").is_file()]
 base=pathlib.Path(flint.__file__).resolve().parent
 libs=sorted(set(glob.glob(str(base.parent/"*flint*.libs"/"*flint*"))+glob.glob(str(base.parent/"flint.libs"/"*flint*"))+glob.glob(str(base/"*.so"))))
 data["parameters"]["candidateWheelLibraries"]=libs
 data["parameters"]["systemFlintLibrary"]=ctypes.util.find_library("flint")
 data["elapsedSeconds"]=time.monotonic()-start
 target=a.out/"native-flint-build-inventory-receipt.json";target.write_text(json.dumps(data,separators=(",",":")))
 print(json.dumps(data),flush=True)
if __name__=="__main__":main()
