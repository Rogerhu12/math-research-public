#!/usr/bin/env python3
"""Read-only original H25 identity and complete coefficient-socle height audit.
Author: Astra-ISP-789f / literature_audit with GPT-6 Astra Pro, 2026-11-16.
No original source solve or integer product is repeated.
"""
import argparse,gzip,hashlib,importlib.util,json,resource,time
from pathlib import Path
from flint import nmod_mat
FORMAT="r150-original-hstar-four-parameter-annihilator-audit-v1"
TAIL_SOURCE_SHA="daaf20b42f05718f5ffbcc570963e00fe46eed2f10216291c4f44f514ef7d1ab"
TAIL_RESULT_SHA="71959c05e881c578dfb01578cb995d2f7a422c16aed7e41ab66afc3cfa395a9d"
TAIL_BINDING="e0c921f51077e07288410fc7c2bdc63adb0a3b27127f4f18cdc61fd1ac6af4f1"
J16_SHA="59d09cbeec71ebf7cda6f12ddd21c1b7ffe1c83a3f9de81b776df0a97df687d8"
U16_SHA="679132fd4727fd305b77c82beb5d3f2e002df1860045200c3392158ab8eb48b9"
H25={
"original-product.json":(815,"25203923b41f758f7e7ada1c0d13e9d23adde710bbe5d3594f64a8780309582e"),
"original.recipe":(1468,"ffe0677a0d2cd14b1cae55fb8e8eb4b5074454e6a99b0def430b4b1fff3ae52a"),
"continuation-receipt.json":(11009,"55e7c11e136df8bacfb78db6ed50a575faa1c7f91a7c721d89322ef599935dde"),
"original-integer-h25-mod29791.txt":(22824,"2785c53d015d05db4550e1978c05db7d42009cfa8942e915541599a76d3701cc")
}
def require(b,s):
 if not b:raise AssertionError(s)
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def pinned(path,size,hs):
 b=path.read_bytes();require(len(b)==size and sha(b)==hs,"complete input identity: "+str(path));return b
def module(path,name):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def poly(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def main():
 ap=argparse.ArgumentParser()
 for name in ["work","tail-source","reader","prior-h25","out"]:ap.add_argument("--"+name,type=Path,required=True)
 a=ap.parse_args();start=time.monotonic()
 require(sha(a.tail_source.read_bytes())==TAIL_SOURCE_SHA,"exact previously completed tail audit source")
 old=module(a.tail_source,"paid_hstar_tail")
 raw=pinned(a.work/"original-hstar-annihilator-tail-audit/result.json",3225,TAIL_RESULT_SHA);tail=json.loads(raw)
 require(tail["status"]=="completed" and tail["binding"]==TAIL_BINDING and tail["sourceSHA256"]==TAIL_SOURCE_SHA,"actual completed tail audit")
 for flag in ["sameTrueBasisForCarryAndSevenSocle","all5040OriginalParameterActionProducts","all2835OriginalCarryCoordinateProducts","allNineIndividualTwoSoclePairsIndependent"]:
  require(tail[flag],"paid original tail gate: "+flag)
 require(sha(a.reader.read_bytes())==old.READER_SHA,"same full315 original reader")
 input_ids={};data={}
 for key in ["state","recipe","D5","parentResult"]:
  rel,size,hs=old.PINS[key];b=pinned(a.work/rel,size,hs);input_ids[key]={"path":rel,"bytes":size,"sha256":hs}
  if key!="state":data[key]=json.loads(gzip.decompress(b) if rel.endswith(".gz") else b)
 reader=module(a.reader,"paid_whole315_reader")
 state=reader.load_state(a.work/old.PINS["state"][0]);J=nmod_mat(state["matrices"]["action"],31)
 U13=nmod_mat(data["recipe"]["true13Full315"],31)
 D5=nmod_mat(data["D5"]["matrixRows"],31);D6=nmod_mat(data["parentResult"]["whole315Classes"],31)
 U=old.join(U13,old.sub(D5,range(315),[10,11]),old.sub(D6,range(315),[12]))
 require(U.rank()==16 and old.record(U)["sha256"]==U16_SHA,"same actual independent true16 basis")
 rr,r=U.transpose().rref();I=[next(j for j in range(315) if rr[i,j]) for i in range(r)]
 JU=J*U;J16=old.sub(U,I,range(16)).inv()*old.sub(JU,I,range(16))
 require(U*J16==JU and old.record(J16)["sha256"]==J16_SHA,"complete original parameter action and saved identity")
 require(all(not J16[i,j] for i in range(16) for j in range(16) if old.EXP[i]>old.EXP[j]),"actual source-order filtration")
 blocks=[]
 for e in [4,5,6]:
  ii=[i for i,v in enumerate(old.EXP) if v==e];B=old.sub(J16,ii,ii)
  N=nmod_mat([[int(B[i,j])-(2 if i==j else 0) for j in range(len(ii))] for i in range(len(ii))],31)
  require(old.iszero(N),"whole same-exponent parameter block is two times identity")
  blocks.append({"exponent":e,"dimension":len(ii),"rankOfJMinusTwo":N.rank(),"parameterBlock":old.record(B)})
 hs25={};b25={}
 for name,(size,hs) in H25.items():
  b25[name]=pinned(a.prior_h25/name,size,hs);hs25[name]={"bytes":size,"sha256":hs}
 product=json.loads(b25["original-product.json"]);continuation=json.loads(b25["continuation-receipt.json"])
 require(product==continuation["originalSeventeenConclusion"],"same original complete product in two paid records")
 for key,value in {"format":"r150-full-original-combination-mod29791-v1","status":"completed","prime":31,"modulus":29791,"divisor":29791,"originalEquations":17,"originalRawRows":6188,"originalComponents":4367,"targetMode":1,"targetCount":9,"failedCoefficientCount":0}.items():
  require(product[key]==value,"old original H25 product field "+key)
 for flag in ["allOriginalProductCoefficientsDivisible","fullOriginalSeventeenEquationIdentityMod29791","fullOriginalMacaulayIdentityMod29791","originalRowScaleTransportVerified","allWeightedBoundsVerified"]:
  require(product[flag],"complete original H25 product gate "+flag)
 require(product["actualSourceCosts"]==[87]*9 and product["quotientNonzeroCounts"]==[0]*9,"all nine original H25 products")
 require(continuation["status"]=="completed" and continuation["fullOriginalMod29791IdentityVerified"],"actual successful original continuation")
 recipe=b25["original.recipe"].decode().splitlines()
 require(recipe[0]=="R150_ORIGINAL_COMBINATION_V1" and list(map(int,recipe[1].split()))==[9,87,29791,1,5] and list(map(int,recipe[2].split()))==list(range(2,11)),"original nine targets and targetMode1 recipe")
 model=b25["original-integer-h25-mod29791.txt"].decode().splitlines()
 require(len(model)==20 and model[0]=="R150_ORIGINAL_MOD29791_V1","same original H25 integer model")
 require(len(model[1].split())==18 and all(int(v)%31 for v in model[1].split()),"eighteen fixed original coefficient units")
 require([len(v.split()) for v in model[2:19]]==[187]*11+[396]*6,"full original eleven plus six coefficient frame")
 fp=[-8,32,-25,5];fm=[864,864,135,5];e8=[9600,-25472,-3392,15936,-2888,-936,153,50,5]
 hstar=poly([0,0,0,1],poly(poly(fp,fp),poly(poly(fm,fm),e8)))
 hzero=poly([-2,1],hstar);h25=poly([-2,1],hzero)
 require(len(hstar)==24 and len(hzero)==25 and len(h25)==26 and h25[-1]==3125,"exact original integer multiplier degrees")
 require(list(map(int,model[-1].split()))==[v%29791 for v in h25],"all26 original H25 target coefficients equal (s-2)^2 hstar")
 command=continuation["stages"]["original"]["command"]
 require(any(str(v).endswith("/original-integer-h25-mod29791.txt") for v in command) and any(str(v).endswith("/projector-free-nine-original.recipe") for v in command),"actual original product consumed pinned target model and recipe")
 semantic={"format":FORMAT,"sourceSHA256":sha(Path(__file__).read_bytes()),"tailSourceSHA256":TAIL_SOURCE_SHA,"tailResultSHA256":TAIL_RESULT_SHA,"readerSHA256":old.READER_SHA,"originalInputs":input_ids,"priorH25Inputs":hs25}
 out={"format":FORMAT,"status":"completed","binding":sha(canon(semantic)),"sourceSHA256":semantic["sourceSHA256"],
  "parentTailBinding":TAIL_BINDING,"inputIdentities":semantic,
  "all5040OriginalParameterActionProductsVerified":True,"sameTrue16Basis":old.record(U),"sameParameterAction16":old.record(J16),
  "sameExponentBlocks":blocks,"priorOriginalH25Mod31CubedIdentityVerified":True,"all26IntegerTargetCoefficientsMatched":True,
  "allNineTargetLabelsAndOriginalFramesMatched":True,"newOriginalSourceSolveOrIntegerProductExecuted":False,
  "mathematicalArraysRemainTemporary":True,"elapsedSeconds":time.monotonic()-start,"peakResidentKiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
 a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_bytes(canon(out)+b"\n");print(json.dumps(out,sort_keys=True),flush=True)
if __name__=="__main__":main()
