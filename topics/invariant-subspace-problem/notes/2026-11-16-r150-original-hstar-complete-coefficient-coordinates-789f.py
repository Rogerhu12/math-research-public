#!/usr/bin/env python3
"""Exact original hstar target classes in the complete coefficient-31 torsion basis.
Author: ChatGPT (AI), literature_audit. Date: 2026-11-16.
This small consumer reports only the bounds justified by the actual coordinates.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,resource,signal,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
READER="2026-11-14-r150-torsion-characteristic-789f.py"
HELPER="2026-11-14-r150-ninth-first-matrices-789f.py"
PINS={"state":(1470456,"06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf"),
"reader":(5002,"8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2"),
"helper":(15194,"3f0da5d1814dac10b3dcfa31ac07c67dec38cab420eeedb3037bb4575c61b00a"),
"primitive":(65159,"44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe"),
"parentReceipt":(42372,"dd867cfbbefcce2d7a846016807b1da6f56c73fd82ea9a364036348467bdc5b9"),
"parentResult":(141288,"30d9c04e68e337e2ac5019e527e97e211104b1e9276ff7caf24619a804fde8b9"),
"sevenResult":(1028,"ebd9b1bb82ca732e2a0acb6ebf5aed8046eeed9d0cbeab82eac803ee63967f82")}
PARENT_BIND="712f9b426017d3f63c05e755a314e14d79ac03d22bce6a4b3f943efcd80d7093"
SEVEN_BIND="dce92fb5bbd50efc3cf5bd39a5b7fbf27dec7f88e4c3e0b9308cfff47b042b98"
RECIPE_SHA="d4d486d0d1c6a33e091da3e99d58cb604d7b2ef828a84a20ba23edf76d19a63c"
EXP=[1,1,2,2,2,2,2,3,3,4,4,4,4,5,5,6]
def check(ok,msg):
 if not ok:raise ValueError(msg)
def sha(b):return hashlib.sha256(b).hexdigest()
def ident(p):
 b=p.read_bytes();return {"bytes":len(b),"sha256":sha(b)}
def pin(p,k):
 d=ident(p);check(d=={"bytes":PINS[k][0],"sha256":PINS[k][1]},"exact "+k);return d
def module(p,n):
 sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def rows(M):return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
def rec(M):return {"rows":M.nrows(),"columns":M.ncols(),"sha256":sha(bytes(x for row in rows(M) for x in row))}
def multiply(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def main():
 ap=argparse.ArgumentParser()
 for k in ("state","notes-root","primitive","parent-out","seven-out","recipe","out"):ap.add_argument("--"+k,type=Path,required=True)
 ap.add_argument("--seconds",type=int,default=60);ap.add_argument("--memory-mib",type=int,default=1024)
 a=ap.parse_args();check(1<=a.seconds<=60 and 512<=a.memory_mib<=2048,"small bounded job")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
 def timeout(signum,frame):raise TimeoutError("small hstar coordinate budget")
 signal.signal(signal.SIGALRM,timeout);signal.alarm(a.seconds);a.out.mkdir(parents=True,exist_ok=True);start=time.monotonic()
 receipt={"format":"r150-original-hstar-complete-coefficient31-coordinates-v1","status":"started",
 "prime":31,"targetLabels":list(range(2,11)),"noDenominatorExponentPrefilled":True,"computedArraysTemporaryOnly":True}
 try:
  ps={"state":pin(a.state,"state"),"reader":pin(a.notes_root/READER,"reader"),"helper":pin(a.notes_root/HELPER,"helper"),
   "primitive":pin(a.primitive,"primitive"),"parentReceipt":pin(a.parent_out/"root2-fourth-complete210-receipt.json","parentReceipt"),
   "parentResult":pin(a.parent_out/"complete210-exact-result.json","parentResult"),
   "sevenResult":pin(a.seven_out/"complete-seven-socle-result.json","sevenResult")}
  pr=json.loads((a.parent_out/"root2-fourth-complete210-receipt.json").read_text())
  result=json.loads((a.parent_out/"complete210-exact-result.json").read_text())
  seven=json.loads((a.seven_out/"complete-seven-socle-result.json").read_text())
  check(pr["status"]=="completed" and pr["binding"]==PARENT_BIND and result["remainingExponentExact"]==6,"complete exact coefficient spectrum")
  check(seven["binding"]==SEVEN_BIND and seven["minimum31DenominatorExponents"]==[2]*9,"actual original h0 exact two")
  raw=gzip.decompress(a.recipe.read_bytes());check(len(raw)==709918 and sha(raw)==RECIPE_SHA,"full210 exact true generator recipe")
  recipe=json.loads(raw);ps["recipePayload"]={"bytes":len(raw),"sha256":sha(raw)}
  binding=sha((json.dumps({"source":ident(Path(__file__)),"inputs":ps,"exponents":EXP},sort_keys=True,separators=(",",":"))+"\n").encode())
  receipt["binding"]=binding;receipt["inputs"]=ps
  reader=module(a.notes_root/READER,"paid_torsion_reader");h=module(a.notes_root/HELPER,"paid_matrix_helper")
  from flint import nmod_mat
  def parent_class(name):
   d=json.loads((a.parent_out/"stages"/name/"exact-class.json").read_text());M=nmod_mat(d["matrixRows"],31)
   check(d["binding"]==PARENT_BIND and rec(M)==pr["parameters"]["comparisons"][name]["matrix"],"full parent original class "+name)
   return M
  D3=parent_class("L3-all197-paid-class-check");D4=parent_class("L4-all204-paid-class-check");D5=parent_class("L5-all208-paid-class-check")
  D6=nmod_mat(result["whole315Classes"],31);check(rec(D6)==pr["parameters"]["comparisons"]["L6-all210-complete-quotient"]["matrix"],"complete D6 identity")
  U13=nmod_mat(recipe["true13Full315"],31)
  check(h.sub(U13,range(315),[8])==h.sub(D3,range(315),[0])
    and h.sub(U13,range(315),range(9,13))==h.sub(D4,range(315),range(6,10)),"true original source coordinates")
  U=h.join(U13,h.sub(D5,range(315),[10,11]),h.sub(D6,range(315),[12]))
  check(U.rank()==16,"complete sixteen source directions")
  state=reader.load_state(a.state);m=state["matrices"];J=nmod_mat(m["action"],31)
  K=nmod_mat(m["kernelTranspose"],31).transpose();Xi=nmod_mat(m["targetCoordinates"],31).transpose()
  T=nmod_mat(m["targets"],31).transpose();A=nmod_mat(m["A"],31);O=nmod_mat(state["observabilityEchelon"],31)
  check(K*Xi==T and A*K==K*J and h.zero(O*T),"same nine original targets, whole action, all505 free observations")
  check(h.zero(h.solve_span(U,J*U)["residual"]),"complete coefficient-torsion reduction invariant")
  plain=gzip.decompress(a.primitive.read_bytes())
  check(len(plain)==158741 and sha(plain)=="fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3","exact primitive payload")
  exact=json.loads(plain);h0=list(map(int,exact["h0"]))
  Fp=[-8,32,-25,5];Fm=[864,864,135,5];E=[9600,-25472,-3392,15936,-2888,-936,153,50,5]
  hs=multiply([0,0,0,1],multiply(multiply(Fp,Fp),multiply(multiply(Fm,Fm),E)))
  check(len(hs)==24 and hs[-1]==3125 and multiply([-2,1],hs)==h0,"full integer original h0=(s-2)hstar")
  def apply(poly):
   Z=nmod_mat(315,9,31)
   for c in reversed(poly):Z=J*Z+Xi*(c%31)
   return Z
  H=apply(hs);H0=apply(h0);I=nmod_mat([[int(i==j) for j in range(315)] for i in range(315)],31)
  check((J-I*2)*H==H0 and h.zero(H0),"original h0 field image and exact factor action")
  z=h.solve_span(U,H);check(z["indices"]==list(range(16)) and h.zero(z["residual"]),"complete true coefficient16 span of original hstar targets")
  C=z["solution"];check(U*C==H,"all315 original hstar coordinate products")
  # The true generators give a direct sum by all16 independence and length50.
  # Unknown higher p digits can still contribute from a higher-exponent summand.
  low=[];up=[]
  for j in range(9):
   low.append(max([2]+[EXP[i] for i in range(16) if C[i,j]]))
   up.append(max(EXP[i] if C[i,j] else EXP[i]-1 for i in range(16)))
   check(low[-1]<=up[-1],"exact coefficient-order interval")
  exact_orders=[lo if lo==hi else None for lo,hi in zip(low,up)]
  output={"binding":binding,"targetLabels":list(range(2,11)),"originalHStarIntegerCoefficients":hs,
   "trueGeneratorExponents":EXP,"originalHStarClasses315":rows(H),"true16Coordinates":rows(C)}
  ob=(json.dumps(output,sort_keys=True,separators=(",",":"))+"\n").encode();(a.out/"original-hstar-complete-coordinates.json").write_bytes(ob)
  receipt.update(status="completed",all24IntegerHStarCoefficientsVerified=True,all25IntegerHZeroCoefficientsReconstructed=True,
   exactOriginalTargetsVerified=True,all7380OriginalTargetProductsVerified=True,all258300ActionProductsVerified=True,
   all4545TargetFreeObservationsZero=True,all2835HStarCoordinateProductsVerified=True,all2835FactorActionProductsVerified=True,
   hZeroFieldClassZero=True,trueGeneratorBasis=rec(U),hStarClass=rec(H),coordinates=rec(C),hStarClassRank=H.rank(),
   minimum31DenominatorLowerBounds=low,minimum31DenominatorUpperBounds=up,exactExponentsWhenClosed=exact_orders,
   exactConclusionUsesCharacteristicZeroMembershipAndCompleteExponentSix=True,
   hiddenHigherPDigitsNotDiscarded=True,output={"file":"original-hstar-complete-coordinates.json","bytes":len(ob),"sha256":sha(ob)})
  return 0
 except BaseException as exc:
  receipt.update(status="failed",errorType=type(exc).__name__,error=str(exc));return 75 if isinstance(exc,TimeoutError) else 1
 finally:
  signal.alarm(0);receipt["elapsedSeconds"]=time.monotonic()-start
  rb=(json.dumps(receipt,sort_keys=True,separators=(",",":"))+"\n").encode()
  (a.out/"original-hstar-coefficient-coordinates-receipt.json").write_bytes(rb);print(rb.decode().strip(),flush=True)
if __name__=="__main__":raise SystemExit(main())
