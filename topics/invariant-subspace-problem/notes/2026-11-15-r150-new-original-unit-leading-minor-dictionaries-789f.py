#!/usr/bin/env python3
"""Read paid original dictionaries for a new maximal minor; no elimination.
Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro.
The integral Smith/source theorem proves this minor's valuation. This executable
checks exact original indices, weights, all input bytes and the theorem's paid
antecedents; it does not pretend to compute an 4354-square determinant.
"""
import argparse,hashlib,itertools,json,os,pathlib,resource,sys,time,traceback
sys.dont_write_bytecode=True
PIN={
 "native_model":(128145,"291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"),
 "paid_full_receipt":(72072,"d904b1afcd6feb6d07e310e758869aa345342f7d013773aa0c433203291c438e"),
 "mapper_receipt":(25756,"17bc63e12c112de4ec35e443cb6fc4897fab0c6ed5c3711cf9509ddcb634bc52"),
 "left_receipt":(52012,"2057846f5adb75ed84f20a144f4cb2da436f9b1db5674612ac376f9b4b503248"),
 "full66_receipt":(15355,"bd3bd1c9395562b2b34baed09864f2b2a5650f4f3a9da949c35f843e0b2cf0ad")}
EXPECTED_P="94c940a7b5ff4768e7e1b0820033eca3cabf19bb8958c7cab52c1e1eefb09837"
EXPECTED_R="64fa0d3161556aa057e3003e5d0b7998a5aa03373838805dd15b721666254055"
EXPECTED_H="c4a2b6d005c23a2df7ea71ceef3fea9f1f7dd46ad1e361077e85d571c98c0148"
EXPECTED_E="89adaa79918eeb4e9c114f0009f995b6eb72161fba54078f583a47acbffa0fea"
EXPECTED_F="57bc2f0bdbf50d82920d286bd9ab2fdb0e03fd5a68a3d72bf534a297ab4da683"
EXPECTED_J="5d9d416096e2c6d0a8cf10a7a95ad83453d0a8c8e98758b3d7ab19f93720124e"
SPECTRUM=[1,1,1,1,3,4,4,4,5,6,7,8,10,11]
def need(x,s):
 if not x:raise ValueError(s)
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def sha(b):return hashlib.sha256(b).hexdigest()
def digest(b):return {"bytes":len(b),"sha256":sha(b)}
def ah(x):return sha(canon(x))
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in PIN:ap.add_argument("--"+k.replace("_","-"),required=True,type=pathlib.Path)
 ap.add_argument("--out",required=True,type=pathlib.Path)
 a=ap.parse_args()
 resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,)*2)
 start=time.monotonic()
 rec={"format":"r150-new-original-unit-leading-minor-dictionaries-v1",
      "status":"running","parameters":{"author":"Astra-ISP-789f / normal_annihilator",
      "aiAssisted":"GPT-6 Astra Pro","noNewMatrixElimination":True,
      "noLargeDeterminantComputed":True,"largeDataUploadedOrCommitted":False}}
 rc=1
 try:
  data={}
  for k,(n,s) in PIN.items():
   b=getattr(a,k).read_bytes()
   need(len(b)==n and sha(b)==s,"complete original pinned input: "+k)
   data[k]=b
  tok=iter(data["native_model"].decode().split())
  need(next(tok)=="R150_NATIVE_NF_V1","original native schema")
  def take(n):return [next(tok) for _ in range(n)]
  coeff=list(map(int,take(11*(66+121))))
  need(len(coeff)==2057 and all(0<=v<31 for v in coeff),"original finite coefficient prefix")
  need(int(next(tok))==3333,"all original prebasis records")
  pre=[list(map(int,take(4))) for _ in range(3333)]
  gamma=list(map(int,take(6*66*6)))
  need(all(0<=v<31 for v in gamma),"original Gamma finite coefficient tail")
  ns,nt=map(int,take(2));need((ns,nt)==(2195,9),"original model remaining-source counts")
  take(3*ns)
  need(list(map(int,take(nt)))==list(range(2,11)) and next(tok,None) is None,
       "complete original model consumed")
  varkeys=[8**i for i in range(11)]
  mult=[x for d in range(4) for x in itertools.combinations_with_replacement(range(11),d)]
  out=[x for d in range(5,0,-1) for x in itertools.combinations_with_replacement(range(11),d)]
  mk=[sum(varkeys[i] for i in x) for x in mult]
  ok=[sum(varkeys[i] for i in x) for x in out];oi={x:i for i,x in enumerate(ok)}
  need(len(mult)==364 and len(out)==4367 and len(oi)==4367,"complete original monomial dictionaries")
  pp=[];pr=[]
  for e,m,p,r in pre:
   need(1<=r<=6188 and (r-1)%17==e and mk[(r-1)//17]==m and p in oi,
        "every original prebasis row/source/output identity")
   pp.append(r);pr.append(oi[p])
  need(len(set(pp))==len(set(pr))==3333,"distinct original prebasis indices")
  paid=json.loads(data["paid_full_receipt"]);s=paid["summary"]
  need(paid["status"]=="completed" and s["constantRank"]==1007 and s["kernelRows"]==1848,
       "paid complete original constant profile")
  remaining=[r for r in range(1,6189) if r not in set(pp)]
  components=[r for r in range(4367) if r not in set(pr)]
  P=pp[:];R=pr[:]
  need(len(s["constantPivots"])==1007,"all original constant pivots")
  for c,n,r,d in s["constantPivots"]:
   need(1<=c<=1034 and 1<=n<=2855 and remaining[n-1]==r and 0<d<31,
        "all original constant unit profile coordinates")
   P.append(r);R.append(components[c-1])
  P.sort();R.sort();ps=set(P);H=[r for r in range(1,6189) if r not in ps]
  need(len(P)==len(set(P))==len(R)==len(set(R))==4340 and len(H)==1848,
       "original P/R/H cardinalities")
  need((ah(P),ah(R),ah(H))==(EXPECTED_P,EXPECTED_R,EXPECTED_H),
       "all three paid complete original unit dictionaries")
  mapper=json.loads(data["mapper_receipt"]);mp=mapper["result"]["parameters"]
  need(mapper["exitCode"]==0 and mp["allOriginalConstantUnitDictionariesVerified"],
       "paid same-original source mapper")
  E=list(map(int,mp["highComplementOriginalSourceRowsOneBased"]))
  F=list(map(int,mp["highFreeOriginalSourceRowsOneBased"]))
  need(len(E)==len(set(E))==216 and len(F)==len(set(F))==202 and set(F)<=set(E)<=set(H),
       "same E216 and source F202 (not outside F202)")
  need((ah(E),ah(F))==(EXPECTED_E,EXPECTED_F),"complete canonical E/F coordinate identities")
  steps=mp["highSmallUnitSteps"];active=[];spectrum=[]
  for t in steps:
   need(len(t["unitOriginalColumns"])==t["constantRank"],"complete formal source unit step")
   active.extend(t["unitOriginalColumns"]);spectrum += [t["exponent"]]*t["constantRank"]
  need(spectrum==SPECTRUM and len(active)==len(set(active))==14,
       "all fourteen formal positive source directions exit")
  J14=sorted(set(E)-set(F))
  need(J14==sorted(E[i] for i in active),"field formal active columns match original free complement")
  J=sorted(P+J14);C=sorted(set(range(1,6189))-set(J))
  need(len(J)==len(set(J))==4354 and len(C)==1834 and ah(J)==EXPECTED_J,
       "complete new original column set")
  rp=sorted(set(H)-set(E))
  need(len(rp)==1632 and set(C)==set(rp)|set(F) and not set(rp)&set(F),
       "new source complement is exactly R_Phi disjoint union source F202")
  left=json.loads(data["left_receipt"]);lp=left["result"]["parameters"];lr=left["result"]
  need(left["exitCode"]==0 and lr["primitiveFormalKernelProved"]
       and lr["samePaidOriginalFree13IdentityVerified"]
       and lr["all4367OriginalOutputCoordinatesTransported"]
       and lp["coefficientwise31UnitRepresentationVerified"],
       "complete original D-regular free13 left kernel")
  F13=list(map(int,lp["sameOriginalFree13"]))
  need(F13==[3001,3002,4002,4003,4288,4289,4353,4354,4355,4363,4364,4365,4366],
       "same actual original free13 output coordinates")
  I=[r for r in range(4367) if r not in set(F13)]
  need(len(I)==4354 and len(set(F13))==13,"complete new original output row set")
  full=json.loads(data["full66_receipt"]);fp=full["result"]["parameters"]
  need(full["exitCode"]==0 and fp["completeFullCharacteristicZeroSpectrumProved"]
       and fp["completeFullCharacteristicZeroSpectrumEqualsPaidField"]
       and fp["completeFullCharacteristicZeroPositiveSpectrum"]==SPECTRUM
       and fp["allFullNextHeadsCovered"] and fp["fullOriginalVerificationComplete"],
       "actual full rational66 equals original field spectrum")
  def sw(r):return (20 if (r-1)%17<11 else 25)+10*len(mult[(r-1)//17])
  def histogram(rows):
   ans={}
   for r in rows:
    k=("N" if (r-1)%17<11 else "Gamma")+":degree"+str(len(mult[(r-1)//17]))
    ans[k]=ans.get(k,0)+1
   return ans
  sa=sum(map(sw,J));sb=sum(10*len(out[i]) for i in I)
  weight=sa-sb;degree=weight-sum(SPECTRUM)
  need((sa,sb,weight,degree)==(208695,199860,8835,8769),"exact independently paid natural weight sums")
  original_free=[{"indexZeroBased":i,"monomialMomentIndices":list(out[i]),
                  "outputWeight":10*len(out[i])} for i in F13]
  material={"version":"new-original-unit-leading-minor-v1","source":digest(pathlib.Path(__file__).read_bytes()),
    "inputs":{k:digest(v) for k,v in data.items()},"originalRowsSHA256":ah(I),
    "originalColumnsSHA256":ah(J),"coefficientRing":"Z_(31)[[u]]",
    "theorem":"full integral Smith plus same original source free202 graph and original free13 left graph"}
  rec.update(status="completed",outcome="complete-original-minor-dictionaries-and-weight",
             allOriginalIndicesAndWeightsVerified=True)
  rec["parameters"].update({"binding":ah(material),"inputIdentity":material,
   "all3333OriginalPrebasisCoordinateRecordsVerified":True,
   "all1007OriginalConstantPivotCoordinatesVerified":True,
   "samePaid4340SourceAndOutputDictionariesVerified":True,
   "sameE216AndCompleteFormalFree202DictionaryVerified":True,
   "sourceP4340WeightHistogram":histogram(P),"unitSourceWeightSum":sum(map(sw,P)),
   "sourceJ4354WeightHistogram":histogram(J),"sourceWeightSum":sa,
   "additional14OriginalSourceRowsOneBased":J14,"additional14SourceWeightSum":sum(map(sw,J14)),
   "deleted13OriginalOutputMonomials":original_free,"deleted13OutputWeightSum":sum(x["outputWeight"] for x in original_free),
   "all4367OutputWeightSum":sum(10*len(x) for x in out),"retained4354OutputWeightSum":sb,
   "newOriginalRowSetSHA256":ah(I),"newOriginalColumnSetSHA256":ah(J),
   "newComplementSourceSetSHA256":ah(C),"originalP4340SHA256":ah(P),"originalTail1848SHA256":ah(H),
   "naturalHomogeneousDegree":weight,"theoremDeterminantInfinityOrder":66,
   "theoremAffineDeterminantDegree":degree,"theoremLeadingCoefficientIs31Unit":True,
   "leadingCoefficientComputedNumerically":False,"oldOrder243MinorUnchanged":True,
   "fullNew4354SquareMatrixBuilt":False,"newMatrixEliminationPerformed":False})
  rc=0
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__)
  rec["traceback"]=traceback.format_exc()
 finally:
  rec["elapsedSeconds"]=time.monotonic()-start
  a.out.parent.mkdir(parents=True,exist_ok=True)
  b=json.dumps(rec,sort_keys=True,indent=2).encode()+b"\n"
  need(len(b)<100000,"small exact dictionary receipt only")
  tmp=a.out.with_name(a.out.name+".partial");tmp.write_bytes(b);os.replace(tmp,a.out)
 print(json.dumps({"status":rec["status"],"out":str(a.out),"sha256":sha(a.out.read_bytes())}),flush=True)
 return rc
if __name__=="__main__":raise SystemExit(main())
