#!/usr/bin/env python3
"""Scan actual assembled cell-momentum zeros while holding other controls fixed.

Every evaluation updates the common physical warp alpha. Brackets and roots
are numerical design evidence only. No nonlinear capacity claim is made.
"""
import argparse,hashlib,json,os,subprocess,time
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
p=argparse.ArgumentParser(description=__doc__)
for key in ('source-topic','factory','config','worker','out'):p.add_argument('--'+key,type=Path,required=True)
p.add_argument('--control-count',type=int,default=7);p.add_argument('--steps',type=int,default=128)
p.add_argument('--lo',type=float,default=-5);p.add_argument('--hi',type=float,default=25)
p.add_argument('--stride',type=float,default=.5);p.add_argument('--cells',nargs='*',type=int)
a=p.parse_args();cfg=json.loads(a.config.read_text());base=cfg['valleyControls'][:a.control_count]
proc=subprocess.Popen(['node',str(a.worker.resolve()),str(a.source_topic.resolve()),str(a.factory.resolve()),str(a.config.resolve()),str(a.steps)],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True,bufsize=1)
rows=[];roots=[];errors=[];begin=time.monotonic();cache={}
def evaluate(n,beta):
 key=(n,float(beta))
 if key not in cache:
  controls=base.copy();controls[n]=float(beta)
  proc.stdin.write(json.dumps(controls)+'\n');proc.stdin.flush();line=proc.stdout.readline()
  if not line:raise RuntimeError('Physical calibration worker closed')
  result=json.loads(line);cache[key]=result
  with a.out.with_suffix('.jsonl').open('a')as stream:stream.write(json.dumps(dict(cell=n,beta=float(beta),result=result))+'\n')
 return cache[key]
def save():
 result=dict(scope=__doc__,configuration=str(a.config),configuration_sha256=hashlib.sha256(a.config.read_bytes()).hexdigest(),worker_sha256=hashlib.sha256(a.worker.read_bytes()).hexdigest(),factory_sha256=hashlib.sha256(a.factory.read_bytes()).hexdigest(),base_controls=base,steps=a.steps,lo=a.lo,hi=a.hi,stride=a.stride,scans=rows,roots=roots,errors=errors,evaluations=len(cache),seconds=time.monotonic()-begin)
 a.out.write_text(json.dumps(result,indent=2)+'\n')
try:
 for n in a.cells or list(range(a.control_count)):
  previous=None;cellrows=[];cellroots=[]
  for beta in np.arange(a.lo,a.hi+a.stride/2,a.stride):
   result=evaluate(n,beta)
   if 'error'in result:
    errors.append(dict(cell=n,beta=float(beta),error=result['error']));previous=None;continue
   v=result['rows'][n];row=dict(beta=float(beta),momentum=v['momentum'],gain=v['gain'],height=result['height'],alpha=result['alpha'])
   cellrows.append(row)
   if previous and previous['momentum']*row['momentum']<0:
    try:
     f=lambda b:evaluate(n,b)['rows'][n]['momentum']
     value=brentq(f,previous['beta'],row['beta'],xtol=2e-11)
     z=evaluate(n,value);v=z['rows'][n]
     found=dict(cell=n,beta=float(value),gain=v['gain'],momentum=v['momentum'],height=z['height'],alpha=z['alpha'],bracket=[previous['beta'],row['beta']])
     roots.append(found);cellroots.append(found)
    except Exception as exc:errors.append(dict(cell=n,bracket=[previous['beta'],row['beta']],error=repr(exc)))
   previous=row
  rows.append(dict(cell=n,values=cellrows));save()
  print(json.dumps(dict(event='cell_completed',cell=n,roots=cellroots,seconds=time.monotonic()-begin)),flush=True)
finally:
 save();proc.stdin.close();proc.wait(timeout=10)
