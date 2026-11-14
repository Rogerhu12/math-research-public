#!/usr/bin/env python3
"""Bind every original197 input and retain actual outcomes without broadening their scope."""
from __future__ import annotations
import argparse,ast,hashlib,json,os,shutil
from pathlib import Path
from collections import Counter
NOTES=Path('topics/invariant-subspace-problem/notes')
PREFIX='2026-11-14-r150-197-third-'
RULES={'README.md':'8fec34716cd4464b55ef546022bd4eb06ea8f50b2040f4025b7383d043db99f2','topics/invariant-subspace-problem/README.md':'40a65616e7a2cdcdc9916585c048b3f66547e71f0627b4abf58e5d3487ce1929'}
SCOPES={'t96','old200','all198','seven','current','ninth','five','notes'}
ARTIFACT_IDS={'t96':14114364261,'old200':14118112895,'all198':14124017685,'seven':14127663630,'current':14130166013,'ninth':14130842468,'five':14134247079}
TARGETS=list(range(2,11))
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for block in iter(lambda:f.read(1048576),b''):h.update(block)
 return h.hexdigest()
def save(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2)+'\n')
def env(k,v):
 with open(os.environ['GITHUB_ENV'],'a') as f:f.write(k+'='+str(v)+'\n')
def request():
 return json.loads((NOTES/(PREFIX+'ci-request-789f.json')).read_text())
def bounded_path(name):
 p=Path(name)
 if not str(p).startswith(str(NOTES)+'/') or '..' in p.parts:raise ValueError('Frozen path outside topic notes')
 return p
def contract(req):
 return json.loads(bounded_path(req['contract_file']).read_text())
def source():
 out=Path(os.environ['RUNNER_TEMP'])/'isp-r150-197-third-output'
 (out/'results').mkdir(parents=True,exist_ok=True);(out/'recovery').mkdir(exist_ok=True);env('ISP_197_THIRD_OUT',out)
 req=request()
 fixed={'format':'r150-197-third-fixed-request-v1','remaining_original_high_kernel_count':197,
  'target_labels':TARGETS,'integer_modulus':887503681,'target_multiplier':'31^2*h0',
  'shared_mathematical_seconds':300,'per_child_memory_mib':512,'per_compilation_seconds':30,
  'local_taylor_center':2,'local_input_precision':10,'local_output_precision':5,
  'relevant_quotient_dimension':24,'old_five_native_mathematics_recomputed':False,
  'old_nine_raw_products_recomputed':False,'characteristic_zero_identity_asserted':False}
 if any(req.get(k)!=v for k,v in fixed.items()):raise ValueError('Fixed original197 request changed')
 rules={p:sha(p) for p in RULES}
 if rules!=RULES or req['rules_sha256']!=RULES:raise ValueError('README changed; root must read and apply actual diff')
 mp=bounded_path(req['source_manifest_file'])
 if sha(mp)!=req['source_manifest_sha256']:raise ValueError('Exact frozen source manifest changed')
 manifest=json.loads(mp.read_text())
 for item in manifest['files']:
  p=bounded_path(item['path'])
  if p.stat().st_size!=item['bytes'] or sha(p)!=item['sha256']:raise ValueError('Frozen source differs: '+str(p))
 for name,digest in manifest.get('reusedDependencies',{}).items():
  p=bounded_path(name if name.startswith(str(NOTES)+'/') else str(NOTES/name))
  if sha(p)!=digest:raise ValueError('Reused source differs: '+name)
 expected_entry={'.github/workflows/invariant-subspace-r150-197-third.yml',str(NOTES/(PREFIX+'actions-prepare-789f.py')),str(NOTES/(PREFIX+'actions-publish-789f.py'))}
 if set(req['workflow_source_sha256'])!=expected_entry:raise ValueError('Exact workflow, prepare, and publisher hashes required')
 for name,digest in req['workflow_source_sha256'].items():
  if sha(name)!=digest:raise ValueError('Frozen entry source changed: '+name)
 parsed=[]
 for name in req['entry_python_files']:
  p=bounded_path(name)
  if not name.endswith('.py'):raise ValueError('Python entry extension')
  ast.parse(p.read_text(),filename=name);parsed.append(name)
 c=contract(req)
 counts=dict(Counter(v['scope'] for v in c['inputs'].values()))
 if len(c['inputs'])!=req['frozen_input_count'] or counts!=req['inputs_by_scope'] or set(counts)!=SCOPES:raise ValueError('All original inputs and scopes required')
 if len(c['inputs'])-counts['notes']!=req['artifact_input_count']:raise ValueError('Artifact input count mismatch')
 if {x['scope']:x['id'] for x in req['artifact_sources']}!=ARTIFACT_IDS:raise ValueError('Exact seven artifact scopes required')
 if c['nativeModulus']!=887503681 or c['sharedMathematicalSeconds']!=300 or c['nativeCompilations']!=req['native_compilations']:raise ValueError('Bounded original197 contract changed')
 if c['mainReceipt']!='197-third-local-jet-pipeline-receipt.json' or len(c['completionRequired'])<5:raise ValueError('Exact main receipt and completion facts required')
 if sha(bounded_path(req['contract_file']))!=req['contract_sha256']:raise ValueError('Contract hash changed')
 save(out/'results/actions-source.json',{'source_commit':os.environ['GITHUB_SHA'],'run_id':os.environ['GITHUB_RUN_ID'],
  'run_attempt':os.environ['GITHUB_RUN_ATTEMPT'],'rules_sha256':rules,'request':req,
  'request_sha256':sha(NOTES/(PREFIX+'ci-request-789f.json')),'source_manifest_sha256':req['source_manifest_sha256'],
  'actualPythonSyntaxFilesParsed':parsed,'allOriginalSourceHashesVerified':True,'noMathematicalCompletionClaimed':True})
 print(json.dumps(fixed),flush=True)
def restore():
 req=request();c=contract(req);temp=Path(os.environ['RUNNER_TEMP']);records=[]
 for scope in sorted(SCOPES):
  original=NOTES if scope=='notes' else temp/('isp-r150-197-third-'+scope+'-download')
  selected=NOTES if scope=='notes' else temp/('isp-r150-197-third-'+scope+'-input')
  selected.mkdir(parents=True,exist_ok=True)
  for label,item in c['inputs'].items():
   if item['scope']!=scope:continue
   candidates=[original/item['relative']] if 'relative' in item else sorted({p for name in item['names'] for p in original.rglob(name)})
   actual=next((p for p in candidates if p.is_file() and sha(p)==item['sha256']),None)
   if actual is None:raise ValueError('Actual saved input absent or SHA mismatch: '+label)
   if 'bytes' in item and actual.stat().st_size!=item['bytes']:raise ValueError('Actual saved byte count mismatch: '+label)
   relative=Path(item['relative']) if 'relative' in item else Path(actual.name)
   if relative.is_absolute() or '..' in relative.parts:raise ValueError('Input relative path')
   destination=selected/relative
   if scope!='notes':
    destination.parent.mkdir(parents=True,exist_ok=True)
    try:os.link(actual,destination)
    except OSError:shutil.copyfile(actual,destination)
   records.append({'label':label,'scope':scope,'restoredArtifactPath':str(actual.relative_to(original)),
    'selectedPath':str(relative),'bytes':actual.stat().st_size,'sha256':item['sha256']})
  if scope!='notes':env('ISP_197_THIRD_'+scope.upper(),selected)
 if len(records)!=req['frozen_input_count']:raise ValueError('Every frozen input required')
 save(Path(os.environ['ISP_197_THIRD_OUT'])/'results/actual-restored-inputs.json',
  {'format':'r150-197-third-selective-recovery-v1','downloadsUsedOnlySevenFrozenArtifacts':True,
   'allSelectedHashesVerified':True,'artifactInputs':req['artifact_input_count'],
   'repositoryInputs':req['inputs_by_scope']['notes'],'inputs':records})
 print(json.dumps({'selectedFiles':len(records),'selectedBytes':sum(x['bytes'] for x in records)}),flush=True)
def outcome():
 req=request();c=contract(req);out=Path(os.environ['ISP_197_THIRD_OUT'])/'results'
 p=out/c['mainReceipt'];r=json.loads(p.read_text()) if p.exists() else {}
 positive=r.get('completedOriginalTargetLabels',[]);negative=r.get('insufficientTargetLabels',[])
 individual=r.get('individualTargetCompatible',[])
 partition=(sorted(positive+negative)==TARGETS and len(set(positive+negative))==9 and len(individual)==9
  and all(type(x) is bool for x in individual) and positive==[j for j,f in zip(TARGETS,individual) if f]
  and negative==[j for j,f in zip(TARGETS,individual) if not f] and positive==r.get('compatibleTargetLabels'))
 full=r.get('fullOriginalAllNineMod887503681IdentityVerified') is True
 count=len(positive)
 allowed=['complete-relevant-low-initial-third-obstruction','partial-original-p6-complete','all-nine-original-p6-complete']
 expected_outcome=allowed[0 if count==0 else 2 if count==9 else 1]
 actual_positive_verified=r.get('allCompatibleTargetsOriginalIdentityVerified') is True
 positive_budget_verified=r.get('finitePositiveSourceBudgetsVerified') is True
 consistency=(full==(count==9) and r.get('finite_budget_verified')==full
  and r.get('characteristicZeroIdentityAsserted') is False and r.get('outcome')==expected_outcome
  and set(c['completedOutcomes'])==set(allowed) and actual_positive_verified==(count>0)
  and (count==0 or positive_budget_verified))
 flag_names=['fullOriginalAllNineMod887503681IdentityVerified','finite_budget_verified',
  'allCompatibleTargetsOriginalIdentityVerified','finitePositiveSourceBudgetsVerified']
 costs=r.get('actualFinalSourceCostsBySlot',[])
 cost_slots=(len(costs)==9 and len(individual)==9 and all(type(x) is int for x in costs)
  and all((0<=cost<=765) if active else cost==-1 for cost,active in zip(costs,individual)))
 consistency=(consistency and all(type(r.get(k)) is bool for k in flag_names)
  and positive_budget_verified==(count>0) and cost_slots)
 facts=all(r.get(k)==v and type(r.get(k)) is type(v) for k,v in c['completionRequired'].items())
 complete=(os.environ.get('ISP_EXACT_OUTCOME')=='success' and r.get('status')=='completed'
  and r.get('outcome') in allowed and facts and partition and consistency)
 result={'run_id':os.environ['GITHUB_RUN_ID'],'run_attempt':os.environ['GITHUB_RUN_ATTEMPT'],
  'source_commit':os.environ['GITHUB_SHA'],'native_step_outcome':os.environ.get('ISP_EXACT_OUTCOME'),
  'pipeline_status':r.get('status','not-started'),'outcome':r.get('outcome'),'complete':complete,
  'completionFactsMatched':facts,'targetPartitionVerified':partition,
  'completed_original_target_labels':positive,'insufficient_target_labels':negative,
  'individual_target_compatible':individual,'full_original_all_nine_mod887503681_identity':full,
  'original_target':'31^2*h0*T modulo887503681; every compatible original target',
  'negative_scope':req['negative_scope'],'actual_final_source_costs_by_slot':r.get('actualFinalSourceCostsBySlot'),
  'mathematical_elapsed_seconds':r.get('mathematicalElapsedSeconds'),
  'characteristic_zero_identity_asserted':False,'partialCheckpointIsNotIdentity':True,'rootOwnsSharedResearchIndices':True}
 save(out/'actions-outcome.json',result);print(json.dumps(result),flush=True)
def main():
 p=argparse.ArgumentParser();p.add_argument('--mode',choices=['source','restore','outcome'],required=True);a=p.parse_args()
 {'source':source,'restore':restore,'outcome':outcome}[a.mode]()
if __name__=='__main__':main()
