#!/usr/bin/env python3
"""Bind four saved197 small files and publish an exact coefficient readout."""
from __future__ import annotations
import argparse,ast,gzip,hashlib,json,os,shutil
from pathlib import Path
NOTES=Path('topics/invariant-subspace-problem/notes')
REQUEST=NOTES/'2026-11-14-r150-unscaled197-selector-ci-request-789f.json'
RULES={'README.md':'8fec34716cd4464b55ef546022bd4eb06ea8f50b2040f4025b7383d043db99f2','topics/invariant-subspace-problem/README.md':'40a65616e7a2cdcdc9916585c048b3f66547e71f0627b4abf58e5d3487ce1929'}
RECEIPT='unscaled197-first-carry-source-space-receipt.json'
def sha(b):return hashlib.sha256(b).hexdigest()
def save(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2)+'\n')
def env(k,v):
 with open(os.environ['GITHUB_ENV'],'a') as f:f.write(k+'='+str(v)+'\n')
def request():return json.loads(REQUEST.read_text())
def source():
 out=Path(os.environ['RUNNER_TEMP'])/'isp-r150-unscaled197-selector-output'
 for d in (out/'results',out/'recovery/inputs',out/'recovery/calculation'):d.mkdir(parents=True,exist_ok=True)
 env('ISP_UNSCALED197_OUT',out)
 req=request()
 if req['format']!='r150-unscaled197-selector-fixed-request-v1' or req['mathematical_seconds']!=10 or req['memory_mib']!=512 or req['source_mathematical_run']!=43653360404:raise ValueError('fixed saved197 readout request')
 actual={p:sha(Path(p).read_bytes()) for p in RULES}
 if actual!=RULES or req['rules_sha256']!=RULES:raise ValueError('README changed; root must read and apply actual diff')
 parsed=[]
 for name,digest in req['source_sha256'].items():
  p=Path(name)
  if sha(p.read_bytes())!=digest:raise ValueError('Frozen source hash: '+name)
  if name.endswith('.py'):ast.parse(p.read_text(),filename=name);parsed.append(name)
 if set(req['inputs'])!={'prepared_receipt','prepared_system','complete_receipt','complete_system'}:raise ValueError('exact four source files')
 restored={}
 for key,item in req['inputs'].items():
  path=Path(item['path'])
  if not str(path).startswith(str(NOTES)+'/r150-197-third-actions-789f/43653360404-1/') or '..' in path.parts:raise ValueError('source result directory')
  raw=path.read_bytes()
  if len(raw)!=item['stored_bytes'] or sha(raw)!=item['stored_sha256']:raise ValueError('actual stored input '+key)
  data=gzip.decompress(raw) if item['decode_outer_gzip'] else raw
  if len(data)!=item['bytes'] or sha(data)!=item['sha256']:raise ValueError('actual decoded input '+key)
  dest=out/'recovery/inputs'/item['local_name'];dest.write_bytes(data)
  restored[key]={'sourcePath':str(path),'storedBytes':len(raw),'storedSHA256':sha(raw),'bytes':len(data),'sha256':sha(data)}
 save(out/'results/actions-source.json',{'source_commit':os.environ['GITHUB_SHA'],'run_id':os.environ['GITHUB_RUN_ID'],'run_attempt':os.environ['GITHUB_RUN_ATTEMPT'],'rules_sha256':actual,'request':req,'request_sha256':sha(REQUEST.read_bytes()),'actualPythonSyntaxFilesParsed':parsed,'allFourActualSavedInputsVerified':True,'restoredInputs':restored,'noMathematicalCompletionClaimed':True})
 print(json.dumps({'actualSavedInputFiles':4,'actualDecodedInputBytes':sum(x['bytes'] for x in restored.values()),'actualPythonSyntaxFilesParsed':parsed}),flush=True)
def outcome():
 out=Path(os.environ['ISP_UNSCALED197_OUT']);p=out/'recovery/calculation'/RECEIPT
 rec=json.loads(p.read_text()) if p.exists() else {}
 flags=['all197ProjectedColumnsExpressedInTrueV10','allActualSourceCoordinateIdentitiesVerified','allQuotientActionsVerified']
 complete=(os.environ.get('ISP_EXACT_OUTCOME')=='success' and rec.get('status')=='completed'
  and all(rec.get(k) is True for k in flags) and rec.get('higherIntegerProductsRecomputed') is False
  and rec.get('fullOriginalS2HigherLiftComputed') is False and rec.get('characteristicZeroIdentityAsserted') is False
  and rec.get('actualSourceRun')==43653360404)
 if p.exists():shutil.copyfile(p,out/'results'/RECEIPT)
 result={'run_id':os.environ['GITHUB_RUN_ID'],'run_attempt':os.environ['GITHUB_RUN_ATTEMPT'],'source_commit':os.environ['GITHUB_SHA'],
  'native_step_outcome':os.environ.get('ISP_EXACT_OUTCOME'),'complete':complete,'status':rec.get('status','not-started'),
  'rankProjected197':rec.get('rankProjected197'),'modU7Dimension':rec.get('quotients',{}).get('U7',{}).get('polynomialImageDimension'),
  'modU8Dimension':rec.get('quotients',{}).get('U8',{}).get('polynomialImageDimension'),'modU9Dimension':rec.get('quotients',{}).get('U9',{}).get('polynomialImageDimension'),
  'combinedB8ModuloU7Dimension':rec.get('combinedImageWithPaidB8ModuloU7',{}).get('polynomialImageDimension'),
  'mathematical_elapsed_seconds':rec.get('elapsedSeconds'),'higherIntegerProductsRecomputed':False,
  'fullOriginalS2HigherLiftComputed':False,'characteristicZeroIdentityAsserted':False,'rootOwnsSharedResearchIndices':True}
 save(out/'results/actions-outcome.json',result);print(json.dumps(result),flush=True)
def main():
 p=argparse.ArgumentParser();p.add_argument('--mode',choices=['source','outcome'],required=True);a=p.parse_args()
 {'source':source,'outcome':outcome}[a.mode]()
if __name__=='__main__':main()
