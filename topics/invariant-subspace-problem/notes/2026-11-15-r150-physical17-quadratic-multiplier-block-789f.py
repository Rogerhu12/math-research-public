#!/usr/bin/env python3
"""One physical-infinity quadratic-multiplier block, with the full136 Koszul subspace.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
No finite-parameter986 statement is substituted for the current original17 heads.
"""
import argparse,gzip,hashlib,itertools,json,math,os,pathlib,resource,struct,sys,time,traceback
sys.dont_write_bytecode=True
POINT_SHA="97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074"
def need(b,s):
 if not b:raise ValueError(s)
def sha(p):
 b=pathlib.Path(p).read_bytes();return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()}
def savejson(p,x):
 q=p.with_name(p.name+".tmp");q.write_text(json.dumps(x,separators=(",",":"))+"\n");os.replace(q,p)
 return {"file":p.name,**sha(p),"temporaryOnly":True}
def savebin(p,magic,shape,body):
 q=p.with_name(p.name+".tmp")
 with q.open("wb") as f:f.write(magic);f.write(struct.pack("<"+"I"*len(shape),*shape));f.write(body)
 os.replace(q,p);return {"file":p.name,**sha(p),"temporaryOnly":True}
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--point-model",required=True,type=pathlib.Path);ap.add_argument("--out",required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=30);ap.add_argument("--memory-mib",type=int,default=512);a=ap.parse_args()
 need(math.isfinite(a.seconds) and 0<a.seconds<=30 and 0<a.memory_mib<=512,"one bounded30s/512MiB task")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();deadline=start+a.seconds-1;out=a.out.resolve()
 need(not out.exists() or not any(out.iterdir()),"fresh output");out.mkdir(parents=True,exist_ok=True)
 r={"format":"isp-physical-seventeen-quadratic-multipliers-degree2-v1","status":"running","parameters":{},
    "largeDataUploadedOrCommitted":False,"oldNormalFormsRecomputed":False,"newDixonDigitsComputed":0}
 files=[];code=1
 def check():
  if time.monotonic()>=deadline:raise TimeoutError("actual small-block budget")
 try:
  need(sha(a.point_model)=={"bytes":87459,"sha256":POINT_SHA},"same exact original physical point")
  point=json.loads(a.point_model.read_text());need(point["characteristicZeroSameOriginal17Verified"],"original17 field transport")
  Q=[[int(x) for x in row[11:]] for row in point["primitivePointCoefficients"]]
  need(len(Q)==17 and all(len(row)==66 for row in Q),"full17 quadratic heads")
  v=[8**i for i in range(11)];qkeys=[v[i]+v[j] for i in range(11) for j in range(i,11)]
  okeys=[sum(v[j] for j in z) for z in itertools.combinations_with_replacement(range(11),4)]
  ix={k:i for i,k in enumerate(okeys)};need(len(qkeys)==66 and len(ix)==1001,"all homogeneous monomials")
  body=bytearray(1001*1122)
  for e in range(17):
   for j,mul in enumerate(qkeys):
    col=e*66+j
    for k,c in enumerate(Q[e]):
     if c:
      ii=ix[mul+qkeys[k]]*1122+col;body[ii]=(body[ii]+c)%31
   check()
  files.append(savebin(out/"physical17-degree2-multiplier-matrix-mod31.bin",b"R150Q231",(31,1001,1122),body))
  from flint import nmod_mat
  M=nmod_mat(1001,1122,list(body),31)
  R,rank=M.rref();rank=int(rank);check()
  rr=bytes(int(x) for x in R.entries())
  files.append(savebin(out/"physical17-degree2-multiplier-rref-mod31.bin",b"R150QR31",(31,1001,1122,rank),rr))
  K=bytearray(1122*136);c=0
  for i in range(17):
   for j in range(i+1,17):
    for k in range(66):
     K[(i*66+k)*136+c]=Q[j][k]%31
     K[(j*66+k)*136+c]=(-Q[i][k])%31
    c+=1
  need(c==136,"all constant skew pairs")
  KM=nmod_mat(1122,136,list(K),31)
  need(int(KM.rref()[1])==136,"complete136 constant Koszul independence")
  prod=M*KM
  need(all(int(x)==0 for x in prod.entries()),"all1001x136 original polynomial kernel identities")
  need(rank<=986,"constant136 upper rank bound")
  files.append(savebin(out/"physical17-constant-koszul136-mod31.bin",b"R150QK31",(31,1122,136),K))
  qminor=[0,1,2,3,4,5,6,7,8,9,10,11,15,18,27,35,42]
  det=int(nmod_mat(17,17,[Q[i][j]%31 for i in range(17) for j in qminor],31).det())
  need(det==4,"same paid physical17 head independence")
  r.update({"status":"completed","rankModulo31":rank,"nullityModulo31":1122-rank,
    "constantKoszulSubspaceDimensionOverQ":136,"rankOverQLowerBound":rank,"rankOverQUpperBound":986,
    "rankOverQExactly986Proved":rank==986,"all1001By136ConstantKoszulProductsZeroModulo31":True,
    "quadraticSkewTopCancellationAddsNoSourceBeyondDegreeOneFamilyProved":rank==986,
    "higherSkewCoefficientDegreesExcluded":False,"entireKoszulModuleExcluded":False})
  r["parameters"].update({"codeSHA256":sha(__file__)["sha256"],"inputPointSHA256":POINT_SHA,
     "columnOrder":"equation0..16 then lex homogeneous quadratic monomial",
     "rowOrder":"lex homogeneous degree4 monomial","physical17QuadraticMinorDeterminantModulo31":det,
     "char0UpperBoundUsesExactSymbolicKoszulIdentitiesAndIndependentQ":True,
     "finiteParameter986ResultNotUsed":True})
  code=0
 except TimeoutError as e:r.update(status="budget-exhausted",error=str(e));code=75
 except Exception as e:r.update(status="failed",error=str(e),exceptionType=type(e).__name__);(out/"exception.log").write_text(traceback.format_exc());code=1
 finally:
  r["parameters"]["temporaryFiles"]=files;r["mathematicalElapsedSeconds"]=time.monotonic()-start
  savejson(out/"physical17-degree2-multiplier-receipt.json",r)
 print(json.dumps(r),flush=True);return code
if __name__=="__main__":sys.exit(main())
