#!/usr/bin/env python3
"""Probe the literal nonlinear mode-4 tail at a completed n4 prefix height.
No prefix re-solve or seam closure is inferred from this tail calculation.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,hashlib,importlib.util,json,sys,time,subprocess
from types import SimpleNamespace
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--prefix-loader-dir',type=Path,required=True);p.add_argument('--tail-source',type=Path,required=True);p.add_argument('--sparse-helper',type=Path,required=True);p.add_argument('--quadrature',type=int,default=256);p.add_argument('--steps',type=int,default=16);p.add_argument('--scales',type=float,nargs='+',default=[.1,.2,.4,.6,.8,1.]);p.add_argument('--source-topic',type=Path,required=True);p.add_argument('--checkpoint',type=Path,required=True);p.add_argument('--config',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--parts',type=int,default=8);a=p.parse_args();a.out.parent.mkdir(parents=True,exist_ok=True)
sys.path.insert(0,str(a.prefix_loader_dir.resolve()))
from diagnose_bimodal_chart import load
rec,obj,flow,par,mesh,pp=load(a)
M=obj.M;q=obj.q
if a.quadrature<=4*M*4 or a.quadrature&(a.quadrature-1):raise ValueError('Original engine and audit require power-of-two quadrature strictly greater than 4*M*spacing')
H=obj.bridge.sigma*q*pp(np.array([flow.end]))[obj.iz:,0]
cfg=json.loads(a.config.read_text());cfg.update(modes=M,spacing=4,shootingParts=a.parts,quadrature=a.quadrature,steps=a.steps)
cfg['traceFile']=str(a.out.with_name(a.out.name+'-trace.jsonl'))
for k,v in rec['physical_port']['parameters'].items():
 if cfg.get(k)!=v:raise ValueError('Physical tail mismatch: '+k)
active=a.out.with_name(a.out.name+'-config.json');active.write_text(json.dumps(cfg,indent=2)+'\n')
source=a.tail_source.resolve();file=source/'scripts/950f-tail-client-v3.py'
os.environ['VISIBLE_FLEX_SPARSE_LINEAR_HELPER']=str(a.sparse_helper.resolve())
os.environ['VISIBLE_FLEX_SPARSE_TRACE']=str(a.out.with_name(a.out.name+'-linear-trace.jsonl'))
spec=importlib.util.spec_from_file_location('n4_actual_tail_client',file);client=importlib.util.module_from_spec(spec);spec.loader.exec_module(client)
stderr=a.out.with_name(a.out.name+'-worker-stderr.log').open('w')
original_popen=subprocess.Popen
def logged_popen(*args,**kwargs):
 kwargs['stderr']=stderr
 return original_popen(*args,**kwargs)
client.subprocess=SimpleNamespace(Popen=logged_popen,PIPE=subprocess.PIPE)
rows=[];tail=None;begin=time.monotonic();out=dict(scope=__doc__,q=q,modes=M,spacing=4,parts=a.parts,height=H.tolist(),checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),config_sha256=hashlib.sha256(active.read_bytes()).hexdigest(),rows=rows,command=sys.argv,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),warmup_path='Uniform scaling of the full actual H vector; arbitrary initialization, not an asserted amplitude branch.')
try:
 tail=client.WeightedTailPort(active,source/'repro/source-root',a.out.with_name(a.out.name+'-tail'),node_heap=2048)
 out['linear_dn_difference']=float(abs(tail.linearD-np.asarray(rec['physical_port']['linearSlope'][:M])).max())
 print(json.dumps(dict(event='ready',q=q,modes=M,first_height=float(H[0]),second_height=float(H[1]),linear_difference=out['linear_dn_difference'])),flush=True)
 for scale in a.scales:
  request=H*scale;r=tail.solve(request,jacobian=scale==1.,audit=True)
  row=dict(scale=scale,converged=r['converged'],residual=r['residual'],tail_calls=tail.calls,mean_slope=r['jets']['meanSlope'],first_slope=r['jets']['slope'][0],second_slope=r['jets']['slope'][1],audit=r.get('audit'),seconds=time.monotonic()-begin)
  rows.append(row);print(json.dumps({k:v for k,v in row.items()if k!='audit'}),flush=True)
 out['success']=True
except Exception as exc:
 out.update(success=False,error=repr(exc),tail_calls=tail.calls if tail else 0);print(json.dumps(dict(event='failure',error=repr(exc))),flush=True)
finally:
 if tail:
  out['worker_returncode_before_close']=tail.proc.poll()
  tail.close()
  out['worker_returncode_after_close']=tail.proc.returncode
  out['tail_source_sha256']=tail.sources
 stderr.close()
 out['seconds']=time.monotonic()-begin;out['output_sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in a.out.parent.glob(a.out.name+'-tail_*.json.gz')}
 a.out.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
