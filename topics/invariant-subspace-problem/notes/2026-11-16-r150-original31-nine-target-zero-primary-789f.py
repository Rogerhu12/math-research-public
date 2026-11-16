#!/usr/bin/env python3
"""Original F31 nine-target zero-primary module; no old elimination is repeated.
Author: ChatGPT (AI), literature_audit. Date: 2026-11-16.
All computed arrays and receipts are temporary.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,resource,signal,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
STATE_BYTES=1470456
STATE_SHA="06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf"
READER_NAME="2026-11-14-r150-torsion-characteristic-789f.py"
READER_SHA="8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2"
HELPER_NAME="2026-11-14-r150-ninth-first-matrices-789f.py"
HELPER_SHA="3f0da5d1814dac10b3dcfa31ac07c67dec38cab420eeedb3037bb4575c61b00a"
def check(ok,message):
 if not ok:raise ValueError(message)
def sha(raw):return hashlib.sha256(raw).hexdigest()
def identity(p):
 b=p.read_bytes();return {"bytes":len(b),"sha256":sha(b)}
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def data(M):return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
def record(M):
 return {"rows":M.nrows(),"columns":M.ncols(),"sha256":sha(bytes(x for row in data(M) for x in row))}
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--state",type=Path,required=True);ap.add_argument("--notes-root",type=Path,required=True)
 ap.add_argument("--out",type=Path,required=True);ap.add_argument("--seconds",type=int,default=60);ap.add_argument("--memory-mib",type=int,default=1024)
 a=ap.parse_args();check(1<=a.seconds<=60 and 512<=a.memory_mib<=2048,"small explicit budget")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
 def timeout(signum,frame):raise TimeoutError("zero-primary small-consumer budget")
 signal.signal(signal.SIGALRM,timeout);signal.alarm(a.seconds)
 a.out.mkdir(parents=True,exist_ok=True);start=time.monotonic()
 r={"format":"r150-original31-nine-target-zero-primary-v1","status":"started","prime":31,"targetLabels":list(range(2,11)),
    "computedArraysTemporaryOnly":True,"rationalPartitionNotAssumed":True}
 try:
  si=identity(a.state);check(si=={"bytes":STATE_BYTES,"sha256":STATE_SHA},"exact paid complete315 state")
  ri=identity(a.notes_root/READER_NAME);hi=identity(a.notes_root/HELPER_NAME)
  check(ri["sha256"]==READER_SHA and hi["sha256"]==HELPER_SHA,"exact paid readers")
  semantics={"source":identity(Path(__file__)),"state":si,"reader":ri,"helper":hi,"originalTargetLabels":list(range(2,11)),
   "method":"minimum-polynomial cofactor followed by complete original-target Krylov and all315 products"}
  binding=sha((json.dumps(semantics,sort_keys=True,separators=(",",":"))+"\n").encode());r["binding"]=binding;r["inputIdentity"]=semantics
  reader=load(a.notes_root/READER_NAME,"original_paid315_reader");h=load(a.notes_root/HELPER_NAME,"original_paid315_helper")
  from flint import nmod_mat
  state=reader.load_state(a.state);m=state["matrices"]
  check(state["torsionDimension"]==315 and state["observabilityRank"]==505,"complete original state dimensions")
  J=nmod_mat(m["action"],31);K=nmod_mat(m["kernelTranspose"],31).transpose()
  T=nmod_mat(m["targetCoordinates"],31).transpose();targets=nmod_mat(m["targets"],31).transpose()
  A=nmod_mat(m["A"],31);C=nmod_mat(m["C"],31);O=nmod_mat(state["observabilityEchelon"],31)
  check(K*T==targets,"all original nine target products")
  check(A*K==K*J and h.zero(C*K),"complete original parameter action")
  check(h.zero(O*targets),"all505 original target free observations")
  mu=J.minpoly();coef=[int(mu[i]) for i in range(mu.degree()+1)]
  e=next(i for i,v in enumerate(coef) if v);q=coef[e:]
  check(e==11 and q[0]!=0,"paid complete zero maximum11 and nonzero cofactor constant")
  # q is a unit on the zero primary, and kills every other primary of J.
  X=nmod_mat(315,9,31)
  for c in reversed(q):X=J*X+T*c
  blocks=[];Y=X
  for k in range(e):
   blocks.append(Y);Y=J*Y
  check(h.zero(Y),"complete J^11 q(J)T zero")
  Krylov=h.join(*blocks);sol=h.solve_span(Krylov,J*Krylov)
  check(h.zero(sol["residual"]),"all315 complete Krylov closure")
  B=sol["basis"];d=B.ncols();jb=h.solve_span(B,J*B);xt=h.solve_span(B,X)
  check(jb["indices"]==list(range(d)) and xt["indices"]==list(range(d))
    and h.zero(jb["residual"]) and h.zero(xt["residual"]),"full original restriction and seed identities")
  JM=jb["solution"];TM=xt["solution"]
  check(J*B==B*JM and X==B*TM,"all315 original basis action and seed products")
  powers=[nmod_mat([[int(i==j) for j in range(d)] for i in range(d)],31)]
  ranks=[d]
  for k in range(1,e+1):powers.append(powers[-1]*JM);ranks.append(powers[-1].rank())
  check(ranks[-1]==0 and all(ranks[i+1]<=ranks[i] for i in range(e)),"nilpotent ranks")
  counts=[ranks[i]-ranks[i+1] for i in range(e)]
  multiplicities=[counts[i]-(counts[i+1] if i+1<e else 0) for i in range(e)]
  check(all(x>=0 for x in multiplicities),"complete nilpotent invariant factors")
  partition=[i+1 for i,v in enumerate(multiplicities) for _ in range(v)]
  check(sum(partition)==d,"complete partition dimension")
  result={"binding":binding,"zeroTargetBasisOriginalKrylovIndices":sol["indices"],
   "zeroTargetBasis315":data(B),"zeroTargetAction":data(JM),"zeroTargetSeeds":data(TM),
   "zeroCofactorCoefficients":q,"wholeMinimumPolynomial":coef}
  raw=(json.dumps(result,sort_keys=True,separators=(",",":"))+"\n").encode();path=a.out/"complete-zero-target-module.json";path.write_bytes(raw)
  r.update(status="completed",dimension=d,zeroInvariantFactors=partition,actionPowerRanks=ranks,
   sameOriginalNineTargets=True,all7380OriginalTargetProductsVerified=True,
   all258300OriginalActionProductsVerified=True,all4095LeakageProductsZero=True,
   all4545OriginalTargetFreeObservationsZero=True,completeByMutualContainment=True,
   completeKrylovColumns=99,basisOriginalKrylovIndices=sol["indices"],
   basis=record(B),action=record(JM),zeroSeeds=record(TM),
   originalRestrictionCoordinates=315*d,originalSeedCoordinates=315*9,
   originalMinimumPolynomialDegree=mu.degree(),zeroPrimaryMaximum=e,
   cofactorConstant=q[0],zeroCofactorDegree=len(q)-1,
   output={"file":path.name,"bytes":len(raw),"sha256":sha(raw)},
   rationalTransferConditionalOnOriginalIntegralCarrier=True)
  return 0
 except BaseException as exc:
  r.update(status="failed",errorType=type(exc).__name__,error=str(exc));return 75 if isinstance(exc,TimeoutError) else 1
 finally:
  signal.alarm(0);r["elapsedSeconds"]=time.monotonic()-start
  raw=(json.dumps(r,sort_keys=True,separators=(",",":"))+"\n").encode()
  (a.out/"original31-zero-target-module-receipt.json").write_bytes(raw);print(raw.decode().strip(),flush=True)
if __name__=="__main__":raise SystemExit(main())
