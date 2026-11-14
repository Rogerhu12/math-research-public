#!/usr/bin/env python3
"""Freeze, restore, and record the unique p2-integral eta8 continuation."""
from __future__ import annotations
import argparse,ast,hashlib,json,os,shutil
from pathlib import Path
from collections import Counter
NOTES=Path('topics/invariant-subspace-problem/notes')
PREFIX='2026-11-14-r150-eighth-second-'
SCOPES={'t96':5,'all198':15,'seven':5,'current':6,'ninth':13,'notes':2}
RULES={'README.md':'8fec34716cd4464b55ef546022bd4eb06ea8f50b2040f4025b7383d043db99f2','topics/invariant-subspace-problem/README.md':'40a65616e7a2cdcdc9916585c048b3f66547e71f0627b4abf58e5d3487ce1929'}
ALLOWED=['all-nine-full-original31squaredh0-mod887503681-certificates','complete-eighth-admissible-second-obstruction-with-positive-original-certificates','complete-eighth-admissible-second-obstruction-no-compatible-current-source']
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for block in iter(lambda:f.read(1048576),b''):h.update(block)
 return h.hexdigest()
def save(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2)+'\n')
def env(k,v):
 with open(os.environ['GITHUB_ENV'],'a') as f:f.write(k+'='+str(v)+'\n')
def source():
 out=Path(os.environ['RUNNER_TEMP'])/'isp-r150-eighth-second-output'
 (out/'results').mkdir(parents=True,exist_ok=True);(out/'recovery').mkdir(exist_ok=True);env('ISP_EIGHTH_OUT',out)
 request_path=NOTES/(PREFIX+'ci-request-789f.json');request=json.loads(request_path.read_text())
 fixed={'format':'r150-eighth-second-fixed-request-v1','new_direction_labels':[9101],'actual_new_rhs_labels':[9101],'target_labels':list(range(2,11)),'integer_modulus':887503681,'new_kernel_divisor':28629151,'target_multiplier':'31^2*h0','shared_mathematical_seconds':300,'per_child_memory_mib':512,'per_compilation_seconds':30,'native_compilations':6,'frozen_input_count':46,'artifact_input_count':44,'old_nine_raw_products_recomputed':False,'complete_lower_initial_freedom_computed':False,'characteristic_zero_identity_asserted':False}
 if any(request.get(k)!=v for k,v in fixed.items()):raise ValueError('Fixed one-direction original p2 request changed')
 rules={p:sha(p) for p in RULES}
 if rules!=RULES or request['rules_sha256']!=RULES:raise ValueError('README changed; root must read and apply actual diff')
 manifest_path=Path(request['source_manifest_file'])
 if str(manifest_path)!=str(NOTES/(PREFIX+'frozen-manifest-789f.json')) or sha(manifest_path)!=request['source_manifest_sha256']:raise ValueError('Exact frozen source manifest changed')
 manifest=json.loads(manifest_path.read_text())
 for item in manifest['files']:
  p=Path(item['path'])
  if not str(p).startswith(str(NOTES)+'/') or '..' in p.parts:raise ValueError('Frozen path outside topic notes')
  if p.stat().st_size!=item['bytes'] or sha(p)!=item['sha256']:raise ValueError('Frozen source differs: '+str(p))
 for name,digest in manifest.get('reusedDependencies',{}).items():
  if sha(NOTES/name)!=digest:raise ValueError('Reused source differs: '+name)
 expected_entry={'.github/workflows/invariant-subspace-r150-eighth-second.yml',str(NOTES/(PREFIX+'actions-prepare-789f.py')),str(NOTES/(PREFIX+'actions-publish-789f.py'))}
 if set(request['workflow_source_sha256'])!=expected_entry:raise ValueError('Exact workflow, prepare, and publisher hashes required')
 for name,digest in request['workflow_source_sha256'].items():
  if sha(name)!=digest:raise ValueError('Frozen entry source changed: '+name)
 parsed=[]
 for name in request['entry_python_files']:
  if not name.startswith(str(NOTES)+'/') or not name.endswith('.py'):raise ValueError('Python entry path')
  ast.parse(Path(name).read_text(),filename=name);parsed.append(name)
 contract=json.loads((NOTES/(PREFIX+'contract-789f.json')).read_text())
 if len(contract['inputs'])!=46 or dict(Counter(v['scope'] for v in contract['inputs'].values()))!=SCOPES:raise ValueError('All46 original inputs and scopes required')
 if contract['nativeModulus']!=887503681 or contract['newDirectionLabels']!=[9101] or contract['sharedMathematicalSeconds']!=300:raise ValueError('Bounded contract changed')
 save(out/'results/actions-source.json',{'source_commit':os.environ['GITHUB_SHA'],'run_id':os.environ['GITHUB_RUN_ID'],'run_attempt':os.environ['GITHUB_RUN_ATTEMPT'],'rules_sha256':rules,'request':request,'request_sha256':sha(request_path),'source_manifest_sha256':request['source_manifest_sha256'],'actualPythonSyntaxFilesParsed':parsed,'allOriginalSourceHashesVerified':True,'noMathematicalCompletionClaimed':True})
 print(json.dumps(fixed))
def restore():
 temp=Path(os.environ['RUNNER_TEMP']);contract=json.loads((NOTES/(PREFIX+'contract-789f.json')).read_text());records=[]
 for scope in SCOPES:
  original=NOTES if scope=='notes' else temp/('isp-r150-eighth-second-'+scope+'-download')
  selected=NOTES if scope=='notes' else temp/('isp-r150-eighth-second-'+scope+'-input')
  selected.mkdir(parents=True,exist_ok=True)
  for label,item in contract['inputs'].items():
   if item['scope']!=scope:continue
   candidates=[original/item['relative']] if 'relative' in item else sorted({p for n in item['names'] for p in original.rglob(n)})
   actual=next((p for p in candidates if p.is_file() and sha(p)==item['sha256']),None)
   if actual is None:raise ValueError('Actual saved input absent or SHA mismatch: '+label)
   relative=Path(item['relative']) if 'relative' in item else Path(actual.name)
   if relative.is_absolute() or '..' in relative.parts:raise ValueError('Input relative path')
   destination=selected/relative
   if scope!='notes':
    destination.parent.mkdir(parents=True,exist_ok=True)
    try:os.link(actual,destination)
    except OSError:shutil.copyfile(actual,destination)
   records.append({'label':label,'scope':scope,'restoredArtifactPath':str(actual.relative_to(original)),'selectedPath':str(relative),'bytes':actual.stat().st_size,'sha256':item['sha256']})
  if scope!='notes':env('ISP_EIGHTH_'+scope.upper(),selected)
 if len(records)!=46:raise ValueError('All46 inputs required')
 save(Path(os.environ['ISP_EIGHTH_OUT'])/'results/actual-restored-inputs.json',{'format':'r150-eighth-second-selective-recovery-v1','downloadsUsedOnlyFiveFrozenArtifacts':True,'allSelectedHashesVerified':True,'artifactInputs':44,'repositoryInputs':2,'inputs':records})
 print(json.dumps({'selectedFiles':len(records),'selectedBytes':sum(x['bytes'] for x in records)}))
def outcome():
 out=Path(os.environ['ISP_EIGHTH_OUT'])/'results';p=out/'eighth-second-pipeline-receipt.json';r=json.loads(p.read_text()) if p.exists() else {}
 flags=['newEighthSecondDirectionComputed','newDirectionOriginalDivisibilityVerified','integerAdmissibleRelatedSecondImageComplete','allCompatibleTargetsOriginalIdentityVerified','finitePositiveSourceBudgetsVerified']
 positive=r.get('completedOriginalTargetLabels',[]);negative=r.get('obstructedTargetLabels',[]);individual=r.get('individualTargetCompatible',[])
 full=r.get('fullOriginalAllNineMod887503681IdentityVerified') is True
 partition=(sorted(positive+negative)==list(range(2,11)) and len(set(positive+negative))==9 and len(individual)==9 and all(type(x) is bool for x in individual) and positive==[j for j,f in zip(range(2,11),individual) if f] and negative==[j for j,f in zip(range(2,11),individual) if not f] and positive==r.get('compatibleTargetLabels'))
 consistency=(full==(r.get('outcome')==ALLOWED[0]) and full==(len(positive)==9) and r.get('finite_budget_verified')==full and ((r.get('outcome')==ALLOWED[1])==(0<len(positive)<9)) and ((r.get('outcome')==ALLOWED[2])==(len(positive)==0)))
 complete=(os.environ.get('ISP_EXACT_OUTCOME')=='success' and r.get('status')=='completed' and r.get('outcome') in ALLOWED and all(r.get(k) is True for k in flags) and partition and consistency and all(r.get(k) is False for k in ['old1834AndOldSevenDirectionsRecomputed','oldNineRawAndSourcesRecomputed','completeLowerInitialFreedomComputed','characteristicZeroIdentityAsserted']))
 result={'run_id':os.environ['GITHUB_RUN_ID'],'run_attempt':os.environ['GITHUB_RUN_ATTEMPT'],'source_commit':os.environ['GITHUB_SHA'],'native_step_outcome':os.environ.get('ISP_EXACT_OUTCOME'),'pipeline_status':r.get('status','not-started'),'outcome':r.get('outcome'),'complete':complete,'completed_original_target_labels':positive,'obstructed_target_labels':negative,'individual_target_compatible':individual,'full_original_all_nine_mod887503681_identity':full,'original_target':'31^2*h0*T modulo887503681; every compatible original target','negative_scope':'F9 corrections preserving the actual source modulo31 and the original p2-integer lattice; other lower initial choices and unrestricted rational sources remain unpaid','actual_final_source_costs_by_slot':r.get('actualFinalSourceCostsBySlot'),'mathematical_elapsed_seconds':r.get('mathematicalElapsedSeconds'),'integer_admissible_related_second_image_complete':r.get('integerAdmissibleRelatedSecondImageComplete') is True,'old_nine_raw_products_recomputed':False,'complete_lower_initial_freedom_computed':False,'characteristic_zero_identity_asserted':False,'partialCheckpointIsNotIdentity':True,'rootOwnsSharedResearchIndices':True}
 save(out/'actions-outcome.json',result);print(json.dumps(result))
def main():
 p=argparse.ArgumentParser();p.add_argument('--mode',choices=['source','restore','outcome'],required=True);a=p.parse_args()
 {'source':source,'restore':restore,'outcome':outcome}[a.mode]()
if __name__=='__main__':main()
