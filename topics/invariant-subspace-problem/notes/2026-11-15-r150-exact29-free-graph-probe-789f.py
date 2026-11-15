#!/usr/bin/env python3
"""Read the paid exact29 free image and determine its exact top29 graph.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
No original products, old normal forms, p-adic digits, or candidate searches rerun.
"""
import argparse,gzip,hashlib,json,math,os,pathlib,resource,signal,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
INPUT_BYTES=29488
INPUT_SHA="24f4cbd8ca7c39d5c6280159b71cf8fc85fd9811a1dc9bc6f8bdeb50a977f249"
BINDING="10890e55000e9e0554b2488f333b899dbf224421e5bf091adc24d396348cc6a4"
def need(b,s):
 if not b:raise ValueError(s)
def sha(p):
 b=pathlib.Path(p).read_bytes();return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()}
def save(p,x):
 p=pathlib.Path(p);q=p.with_name(p.name+".tmp")
 if p.suffix==".gz":
  with gzip.open(q,"wt",encoding="utf-8",compresslevel=1) as f:json.dump(x,f,separators=(",",":"))
 else:q.write_text(json.dumps(x,separators=(",",":"))+"\n")
 os.replace(q,p);return {"file":p.name,**sha(p),"temporaryOnly":True}
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument("--free-image",required=True,type=pathlib.Path);ap.add_argument("--out",required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=30);ap.add_argument("--memory-mib",type=int,default=512)
 a=ap.parse_args();need(0<a.seconds<=30 and 0<a.memory_mib<=512,"bounded30s/512MiB")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();deadline=start+a.seconds-1
 out=a.out.resolve();need(not out.exists() or not any(out.iterdir()),"fresh output");out.mkdir(parents=True,exist_ok=True)
 r={"format":"isp-paid-exact29-free-top-graph-v1","status":"running","parameters":{},"largeDataUploadedOrCommitted":False,"newDixonDigitsComputed":0,"originalProductsRecomputed":False}
 code=1
 def check():
  if time.monotonic()>=deadline:raise TimeoutError("shared small budget")
 try:
  got=sha(a.free_image);need(got=={"bytes":INPUT_BYTES,"sha256":INPUT_SHA},"paid exact29 free bytes")
  with gzip.open(a.free_image,"rt",encoding="utf-8") as f:d=json.load(f)
  need(d["binding"]==BINDING and d["rows"]==36 and d["columns"]==29 and d["rankOverQ"]==29 and d["unionWithPaid23RankOverQ"]==29,"paid exact29 dimensions/ranks")
  cols=[[int(v) for v in row] for row in d["integerColumns"]];need(len(cols)==29 and all(len(v)==36 for v in cols),"all36x29 entries")
  from flint import fmpq_mat,nmod_mat
  raw=[cols[c][r] for r in range(36) for c in range(29)]
  F=fmpq_mat(36,29,raw);T=fmpq_mat(29,29,raw[:29*29])
  det31=int(nmod_mat(29,29,[x%31 for x in raw[:29*29]],31).det())
  need(det31!=0,"top29 true31-unit block")
  identity=fmpq_mat(29,29,[int(i==j) for i in range(29) for j in range(29)])
  U=T.solve(identity,algorithm="dixon")
  check();normalized=F*U
  need(all(normalized[i,j]==int(i==j) for i in range(29) for j in range(29)),"exact top29 normalized identity")
  tail=fmpq_mat(7,29,[normalized[i,j] for i in range(29,36) for j in range(29)])
  tail_rank=int(tail.rank());nonzero=[(i,j) for i in range(7) for j in range(29) if tail[i,j]!=0]
  upairs=[[[str(int(U[i,j].p)),str(int(U[i,j].q))] for j in range(29)] for i in range(29)]
  lpairs=[[[str(int(tail[i,j].p)),str(int(tail[i,j].q))] for j in range(29)] for i in range(7)]
  def residue(x):
   u=int(x.p);v=int(x.q);need(v%31!=0,"normalizer remains31-integral");return (u%31)*pow(v%31,-1,31)%31
  reduced=[[residue(normalized[i,j]) for j in range(29)] for i in range(36)]
  need(all(reduced[i][j]==0 for i in range(29,36) for j in range(29)),"paid mod31 bottom-zero identity")
  ur=save(out/"top29-exact-source-normalizer.json.gz",{"binding":BINDING,"input":got,"rows":29,"columns":29,"rationalPairsByRows":upairs,"equation":"F_normalized=F_original*U; top29=I"})
  lr=save(out/"exact-bottom-seven-graph.json.gz",{"binding":BINDING,"input":got,"rows":7,"columns":29,"rationalPairsByRows":lpairs,"rankOverQ":tail_rank,"allZero":not nonzero})
  r.update({"status":"completed","top29DeterminantModulo31":det31,
   "top29InvertibleOverQ":True,"top29Determinant31Unit":True,
   "full36NormalizedFreeIdentityVerified":True,"bottomSevenGraphRankOverQ":tail_rank,
   "bottomSevenGraphAllZeroOverQ":not nonzero,"fullExactFreeImageIsFirst29CoordinateSpace":not nonzero,
   "normalizer31Integral":True,"bottomSevenGraphReducesToZeroModulo31":True})
  r["parameters"].update({"sourceSHA256":sha(__file__)["sha256"],"inputFile":got,"binding":BINDING,
   "topSlots":list(range(29)),"bottomSlots":list(range(29,36)),
   "nonzeroTailPositions":nonzero,"temporaryFiles":[ur,lr],
   "noPureAxisKernelClaimUnlessBottomGraphZero":True})
  # The zero matrix is complete small data; nonzero rational data remain temporary.
  if not nonzero:r["parameters"]["completeBottomSevenGraph"]=[[0]*29 for _ in range(7)]
  code=0
 except TimeoutError as e:r.update(status="budget-exhausted",error=str(e));code=75
 except Exception as e:r.update(status="failed",error=str(e),exceptionType=type(e).__name__);(out/"exception.log").write_text(traceback.format_exc());code=1
 finally:
  r["mathematicalElapsedSeconds"]=time.monotonic()-start
  save(out/"exact29-free-graph-receipt.json",r)
 print(json.dumps(r),flush=True);return code
if __name__=="__main__":sys.exit(main())
