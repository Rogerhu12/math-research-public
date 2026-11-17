#!/usr/bin/env python3
"""Compare sparse and original linear algebra on a real accepted M8 checkpoint.

Use the fixed-M8 checkpoint/config reproduced by the separate m3 seed bundle.
All generated source copies and numerical arrays stay in the new work folder.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,gzip,hashlib,importlib.util,json,subprocess,sys
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser(description=__doc__)
for k in ('source-recovery','seed-checkpoint','base-config','work'):p.add_argument('--'+k,type=Path,required=True)
a=p.parse_args();here=Path(__file__).resolve().parent;out=a.work.resolve();out.mkdir(exist_ok=False);origin=a.source_recovery.resolve()
subprocess.run([sys.executable,str(here/'make_sparse_source.py'),'--source-recovery',str(origin),'--dest',str(out/'patched')],check=True)
os.environ['VISIBLE_FLEX_SPARSE_LINEAR_HELPER']=str(here/'sparse_shooting_linear.py');os.environ['VISIBLE_FLEX_SPARSE_TRACE']=str(out/'linear-trace.jsonl');os.environ['VISIBLE_FLEX_SPARSE_PYTHON']=sys.executable
record=json.loads(gzip.decompress(a.seed_checkpoint.read_bytes()));height=np.asarray(record['request']['height'])*1.000001
if len(height)!=8 or record['config']['spacing']!=3:raise ValueError('Accepted M8, spacing3 seed required')
base=json.loads(a.base_config.read_text());summary=dict(scope=__doc__,original_checkpoint_sha256=hashlib.sha256(a.seed_checkpoint.read_bytes()).hexdigest(),height_multiplier=1.000001,source_change=json.loads((out/'patched/sparse-source-change.json').read_text()));answers=[];prior=a.seed_checkpoint.resolve()
for name,root in [('sparse',out/'patched'),('original',origin)]:
 source=root/'bundle/topics/visible-flexible-closed-surface';cfg={**base,'initialCheckpoint':str(prior),'traceFile':str(out/(name+'-worker-trace.jsonl'))};cfile=out/(name+'-config.json');cfile.write_text(json.dumps(cfg,indent=2)+'\n')
 spec=importlib.util.spec_from_file_location('tail_compare_'+name,source/'scripts/950f-tail-client-v3.py');c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c);port=c.WeightedTailPort(cfile,source/'repro/source-root',out/name,node_heap=2304)
 try:r=port.solve(height,jacobian=True,audit=True)
 finally:port.close()
 answers.append(r);prior=out/(name+'_0001.json.gz');summary[name]={k:r[k]for k in ['converged','residual','audit','history']};summary[name]['checkpoint_sha256']=hashlib.sha256(prior.read_bytes()).hexdigest();summary[name]['jacobian_linf']=float(np.max(np.abs(r['heightJetJacobian'])));(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
x,y=answers;summary['jet_max_difference']=max(float(np.max(abs(np.asarray(x['jets'][k])-np.asarray(y['jets'][k]))))for k in ['height','slope','second','meanSlope','meanSecond']);J,K=np.asarray(x['heightJetJacobian']),np.asarray(y['heightJetJacobian']);summary['jacobian_absolute_max_difference']=float(abs(J-K).max());summary['jacobian_relative_max_difference']=float(abs(J-K).max()/max(1.,abs(J).max(),abs(K).max()));(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary))
