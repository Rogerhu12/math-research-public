#!/usr/bin/env python3
"""Tiny independent original-product and interrupted-transaction check.
Use the exact while-AST of the frozen H5 elimination implementation.
No research matrix or prior large computation is executed here.
"""
import argparse,ast,copy,hashlib,json,math,pathlib,runpy,time
from fractions import Fraction
from types import SimpleNamespace
SOURCE_SHA="8c671b279161dad3dce4e0caeed3ed49f9911ac6844dba705bf040e2ebcf1a3d"
SOURCE_BYTES=20716
def canonical(state):
 return json.dumps(state,sort_keys=True,separators=(",",":"))
def snapshot(rows,active,dag,nnz):
 return {"rows":[[i,sorted(r.items())] for i,r in sorted(rows.items())],
 "active":sorted(active),"dag":copy.deepcopy(dag),"nnz":nnz}
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--source",type=pathlib.Path,required=True);ap.add_argument("--out",type=pathlib.Path,required=True)
 a=ap.parse_args();start=time.monotonic();data=a.source.read_bytes();sha=hashlib.sha256(data).hexdigest()
 assert len(data)==SOURCE_BYTES and sha==SOURCE_SHA
 tree=ast.parse(data);mainfn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=="main")
 loops=[n for n in ast.walk(mainfn) if isinstance(n,ast.While) and isinstance(n.test,ast.Name) and n.test.id=="active"]
 assert len(loops)==1
 module=runpy.run_path(str(a.source),run_name="exact_h5_test_import")
 setup=ast.parse("""
def actual_loop_exercise(interrupt):
 rows={0:{0:2,1:1,2:3,3:1},1:{0:1,1:3,3:2},2:{0:1,1:1,2:1,3:1}}
 active={0,1};dag=[];rowlabels={0:101,1:102,2:103};nnz=sum(map(len,rows.values()))
 incidence={j:{i for i,row in rows.items() if j in row} for j in active}
 revision={i:0 for i in rows}
 heap=[(len(row),i,0) for i,row in rows.items()];heapq.heapify(heap)
 a=SimpleNamespace(candidate_rows=64,max_pivot_work=150000,max_integer_bits=8192,max_nnz=500000)
 newpivots=0;updates=0;pending_started=False;maxbits=2;last_save=time.monotonic();start=time.monotonic()
 rec={"events":[]};calls=0;before_pending=None;expected_committed=None
 def checkpoint(reason):raise AssertionError("toy should not enter periodic serialization")
 def finish_receipt():raise AssertionError("toy should not publish intermediate receipt")
 def check():
  nonlocal calls,before_pending,expected_committed
  calls+=1
  if interrupt and calls==4:
   before_pending=snapshot(rows,active,dag,nnz);expected_committed=len(dag)
  if interrupt and calls==5:
   raise BudgetExpired("deliberate mid-pending toy interruption")
 caught=None
 try:
  pass
 except BudgetExpired as exc:
  caught=str(exc)
 return {"state":snapshot(rows,active,dag,nnz),"caught":caught,"before":before_pending,
 "expectedCommitted":expected_committed,"newPivots":newpivots,"partialPivotDiscarded":pending_started,
 "calls":calls,"elapsed":time.monotonic()-start}
""")
 function=setup.body[0]
 trynode=next(n for n in function.body if isinstance(n,ast.Try))
 trynode.body=[copy.deepcopy(loops[0])]
 ast.fix_missing_locations(setup)
 module.update(SimpleNamespace=SimpleNamespace,snapshot=snapshot,copy=copy)
 exec(compile(setup,"<frozen-H5-while-AST>","exec"),module)
 full=module["actual_loop_exercise"](False)
 assert full["caught"] is None and full["newPivots"]==2 and not full["state"]["active"]
 assert len(full["state"]["rows"])==1
 schur=dict(full["state"]["rows"][0][1]);assert set(schur)<={2,3} and any(schur.values())
 assert schur.get(2,0)+schur.get(3,0)==0
 x={2:Fraction(1),3:Fraction(1)}
 for pivot in reversed(full["state"]["dag"]):
  j=int(pivot["normalFiveColumn"]);aa=int(pivot["pivotCoefficient"])
  x[j]=-sum(Fraction(int(v))*x[int(k)] for k,v in pivot["otherTerms"])/aa
 vector=[x[j] for j in range(4)]
 original=[[2,1,3,1],[1,3,0,2],[1,1,1,1]]
 products=[sum(Fraction(v)*z for v,z in zip(row,vector)) for row in original]
 # An independent original 3x3 minor is -1, so this nonzero vector spans the whole kernel.
 determinant=2*(3*1-0*1)-1*(1*1-0*1)+3*(1*1-3*1)
 assert determinant==-1 and all(v==0 for v in products) and vector==[Fraction(-2),Fraction(0),Fraction(1),Fraction(1)]
 stopped=module["actual_loop_exercise"](True)
 assert stopped["caught"]=="deliberate mid-pending toy interruption" and stopped["expectedCommitted"]==1
 assert stopped["newPivots"]==1 and stopped["partialPivotDiscarded"]
 assert canonical(stopped["state"])==canonical(stopped["before"])
 result={"format":"isp-normal-five-high-elimination-small-validation-v1","status":"completed",
 "executionEnvironment":"local Python in independent /tmp; not GitHub Actions",
 "frozenSourceBytes":len(data),"frozenSourceSHA256":sha,
 "actualFrozenWhileASTExecuted":True,"newResearchMatrixComputed":False,
 "originalRectangularMatrix":original,"H5Columns":2,"H4AttachedColumns":2,
 "independentOriginalMinorDeterminant":determinant,"exactReverseSubstitutedKernel":[str(v) for v in vector],
 "allOriginalMatrixKernelProducts":[str(v) for v in products],
 "completeKernelDimension":1,"H4CompensationNonzero":True,
 "completeRunPivots":full["newPivots"],"completeSchurRows":full["state"]["rows"],
 "interruptedCommittedPivots":stopped["newPivots"],"interruptedUncommittedPivotDiscarded":True,
 "entireCommittedMathematicalStateAndDAGUnchanged":True,
 "committedStateSHA256":hashlib.sha256(canonical(stopped["state"]).encode()).hexdigest(),
 "mathematicalElapsedSeconds":time.monotonic()-start}
 a.out.mkdir(parents=True,exist_ok=True)
 (a.out/"normal-five-high-small-validation-receipt.json").write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
 print(json.dumps(result))
if __name__=="__main__":main()

