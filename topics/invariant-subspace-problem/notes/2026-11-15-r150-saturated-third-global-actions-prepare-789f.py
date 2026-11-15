#!/usr/bin/env python3
"""Bind the actual six-slot global restoration and all nine original modp6 identities."""
from __future__ import annotations
import argparse,ast,hashlib,json,os,shutil
from collections import Counter
from pathlib import Path
NOTES=Path('topics/invariant-subspace-problem/notes')
PREFIX='2026-11-15-r150-saturated-third-global-'
RULES={'README.md':'8fec34716cd4464b55ef546022bd4eb06ea8f50b2040f4025b7383d043db99f2','topics/invariant-subspace-problem/README.md':'40a65616e7a2cdcdc9916585c048b3f66547e71f0627b4abf58e5d3487ce1929'}
ARTIFACT_IDS={"t96":14114364261,"old200":14118112895,"all198":14124017685,"seven":14127663630,"ninth":14130842468,"second":14140872540,"current":14130166013,"third":14141428008}
SCOPES=set(ARTIFACT_IDS)|{'notes'}
TARGETS=list(range(2,11))
OUTCOMES=['all-nine-original-p6-complete']
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def save(p,v):
 p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(v,indent=2)+'\n')
def env(k,v):
 with open(os.environ['GITHUB_ENV'],'a') as f:f.write(k+'='+str(v)+'\n')
def bounded_path(name):
 p=Path(name)
 if not str(p).startswith(str(NOTES)+'/') or '..' in p.parts:raise ValueError('Frozen path outside topic notes')
 return p
def request():return json.loads((NOTES/(PREFIX+'ci-request-789f.json')).read_text())
def contract(req):return json.loads(bounded_path(req['contract_file']).read_text())
def source():
 out=Path(os.environ['RUNNER_TEMP'])/'isp-r150-saturated-third-global-output'
 (out/'results').mkdir(parents=True,exist_ok=True);(out/'recovery').mkdir(exist_ok=True)
 env('ISP_SAT_GLOBAL_OUT',out)
 req=request()
 fixed={'format':'r150-saturated-third-global-fixed-request-v1','original_high_kernel_count':7,
  'auxiliary_source_slots':6,'actual_source_cost_upper_bound':1345,'target_labels':TARGETS,
  'integer_modulus':887503681,'original_target':'31^2*h0','shared_mathematical_seconds':1200,
  'per_child_memory_mib':1024,'per_compilation_seconds':30,'native_compilations':5,
  'old_second_page_mathematics_recomputed':False,'old_third_page_mathematics_recomputed':False,
  'characteristic_zero_identity_asserted':False}
 if any(type(req.get(k)) is not type(v) or req.get(k)!=v for k,v in fixed.items()):
  raise ValueError('Fixed complete six-slot global request changed')
 rules={p:sha(p) for p in RULES}
 if rules!=RULES or req['rules_sha256']!=RULES:raise ValueError('README changed; root must read and apply actual diff')
 mp=bounded_path(req['source_manifest_file'])
 if sha(mp)!=req['source_manifest_sha256']:raise ValueError('Frozen source manifest changed')
 manifest=json.loads(mp.read_text())
 for item in manifest['files']:
  p=bounded_path(item['path'])
  if p.stat().st_size!=item['bytes'] or sha(p)!=item['sha256']:raise ValueError('Frozen source differs: '+str(p))
 for name,digest in manifest.get('reusedDependencies',{}).items():
  p=bounded_path(name if name.startswith(str(NOTES)+'/') else str(NOTES/name))
  if sha(p)!=digest:raise ValueError('Reused source differs: '+name)
 expected_entry={'.github/workflows/invariant-subspace-r150-saturated-third-global.yml',
  str(NOTES/(PREFIX+'actions-prepare-789f.py')),str(NOTES/(PREFIX+'actions-publish-789f.py'))}
 if set(req['workflow_source_sha256'])!=expected_entry:raise ValueError('Exact entry hash set required')
 for name,digest in req['workflow_source_sha256'].items():
  if sha(name)!=digest:raise ValueError('Frozen workflow entry differs: '+name)
 parsed=[]
 for name in req['entry_python_files']:
  p=bounded_path(name)
  if not name.endswith('.py'):raise ValueError('Python extension')
  ast.parse(p.read_text(),filename=name);parsed.append(name)
 c=contract(req);counts=dict(Counter(v['scope'] for v in c['inputs'].values()))
 if len(c['inputs'])!=req['frozen_input_count'] or counts!=req['inputs_by_scope'] or set(counts)!=SCOPES:
  raise ValueError('Every real input and complete scope set required')
 if len(c['inputs'])-counts['notes']!=req['artifact_input_count']:raise ValueError('Artifact input count')
 if {x['scope']:x['id'] for x in req['artifact_sources']}!=ARTIFACT_IDS:raise ValueError('Exact eight source artifacts required')
 if c['nativeModulus']!=887503681 or c['sharedMathematicalSeconds']!=1200 or c['nativeCompilations']!=5 or c['perChildMemoryMiB']!=1024:
  raise ValueError('Bounded original arithmetic contract changed')
 if set(c['completedOutcomes'])!=set(OUTCOMES) or len(c['completionRequired'])<5:
  raise ValueError('Complete original global scope and completion facts required')
 if sha(bounded_path(req['contract_file']))!=req['contract_sha256']:raise ValueError('Contract hash changed')
 save(out/'results/actions-source.json',{'source_commit':os.environ['GITHUB_SHA'],
  'run_id':os.environ['GITHUB_RUN_ID'],'run_attempt':os.environ['GITHUB_RUN_ATTEMPT'],
  'rules_sha256':rules,'request':req,'request_sha256':sha(NOTES/(PREFIX+'ci-request-789f.json')),
  'source_manifest_sha256':req['source_manifest_sha256'],'actualPythonSyntaxFilesParsed':parsed,
  'allOriginalSourceHashesVerified':True,'noMathematicalCompletionClaimed':True})
 print(json.dumps(fixed),flush=True)
def restore():
 req=request();c=contract(req);temp=Path(os.environ['RUNNER_TEMP']);records=[]
 for scope in sorted(SCOPES):
  original=NOTES if scope=='notes' else temp/('isp-r150-saturated-third-global-'+scope+'-download')
  selected=NOTES if scope=='notes' else temp/('isp-r150-saturated-third-global-'+scope+'-input')
  selected.mkdir(parents=True,exist_ok=True)
  for label,item in c['inputs'].items():
   if item['scope']!=scope:continue
   candidates=[original/item['relative']] if 'relative' in item else sorted({p for n in item['names'] for p in original.rglob(n)})
   actual=next((p for p in candidates if p.is_file() and sha(p)==item['sha256']),None)
   if actual is None:raise ValueError('Saved input absent or SHA mismatch: '+label)
   if 'bytes' in item and actual.stat().st_size!=item['bytes']:raise ValueError('Saved byte count: '+label)
   relative=Path(item['relative']) if 'relative' in item else Path(actual.name)
   if relative.is_absolute() or '..' in relative.parts:raise ValueError('Input relative path')
   destination=selected/relative
   if scope!='notes':
    destination.parent.mkdir(parents=True,exist_ok=True)
    try:os.link(actual,destination)
    except OSError:shutil.copyfile(actual,destination)
   records.append({'label':label,'scope':scope,'restoredArtifactPath':str(actual.relative_to(original)),
    'selectedPath':str(relative),'bytes':actual.stat().st_size,'sha256':item['sha256']})
  if scope!='notes':env('ISP_SAT_GLOBAL_'+scope.upper(),selected)
 if len(records)!=req['frozen_input_count']:raise ValueError('All frozen inputs required')
 save(Path(os.environ['ISP_SAT_GLOBAL_OUT'])/'results/actual-restored-inputs.json',
  {'format':'r150-saturated-second-selective-recovery-v1','allSelectedHashesVerified':True,
   'artifactInputs':req['artifact_input_count'],
   'repositoryInputs':sum(x['scope']=='notes' for x in c['inputs'].values()),'inputs':records})
 print(json.dumps({'selectedFiles':len(records),'selectedBytes':sum(x['bytes'] for x in records)}),flush=True)
def outcome():
 req=request();c=contract(req);out=Path(os.environ['ISP_SAT_GLOBAL_OUT'])/'results'
 p=out/c['mainReceipt'];r=json.loads(p.read_text()) if p.exists() else {}
 facts=all(type(r.get(k)) is type(v) and r.get(k)==v for k,v in c['completionRequired'].items())
 costs=r.get('actualFinalSourceCostsBySlot',[])
 cost_check=(len(costs)==9 and all(type(x) is int and 0<=x<=1345 for x in costs))
 targets=(r.get('completedOriginalTargetLabels')==TARGETS)
 originals=all(r.get(k) is True for k in
  ('fullOriginalAllNineMod887503681IdentityVerified','allNineOriginalSeventeenIdentitiesVerified',
   'allSixAuxiliaryOriginalIdentitiesVerified','full315FinalReconciliationVerified',
   'finitePositiveSourceBudgetsVerified','finite_budget_verified'))
 scope=(r.get('characteristicZeroIdentityAsserted') is False)
 complete=(os.environ.get('ISP_EXACT_OUTCOME')=='success' and r.get('status')=='completed'
  and r.get('outcome')=='all-nine-original-p6-complete' and facts and cost_check and targets and originals and scope)
 result={'run_id':os.environ['GITHUB_RUN_ID'],'run_attempt':os.environ['GITHUB_RUN_ATTEMPT'],
  'source_commit':os.environ['GITHUB_SHA'],'native_step_outcome':os.environ.get('ISP_EXACT_OUTCOME'),
  'pipeline_status':r.get('status','not-started'),'outcome':r.get('outcome'),'complete':complete,
  'completionFactsMatched':facts,'allNineTargetLabelsVerified':targets,
  'actualSourceCostsWithin1345':cost_check,'allOriginalIdentitiesAndSixAuxiliariesVerified':originals,
  'completed_original_target_labels':r.get('completedOriginalTargetLabels',[]),
  'actual_final_source_costs_by_slot':costs,
  'mathematical_elapsed_seconds':r.get('mathematicalElapsedSeconds'),
  'packaging_elapsed_seconds':r.get('packagingElapsedSeconds'),
  'full_original_all_nine_mod887503681_identity':complete,
  'characteristic_zero_identity_asserted':False,
  'scope':'All nine actual original p2h0 targets modulo p6 with complete17 identities and actual finite source costs at most1345. No characteristic-zero identity is asserted.',
  'partialCheckpointIsNotIdentity':True,'rootOwnsSharedResearchIndices':True}
 save(out/'actions-outcome.json',result);print(json.dumps(result),flush=True)
def main():
 p=argparse.ArgumentParser();p.add_argument('--mode',choices=['source','restore','outcome'],required=True)
 a=p.parse_args();{'source':source,'restore':restore,'outcome':outcome}[a.mode]()
if __name__=='__main__':main()
