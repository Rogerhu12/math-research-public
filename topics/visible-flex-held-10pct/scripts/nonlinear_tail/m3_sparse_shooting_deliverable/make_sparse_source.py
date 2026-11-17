#!/usr/bin/env python3
"""Copy the 70-source m3 closure and replace only Newton/DN linear algebra.

The nonlinear equations, guards, residual normalization, integrations,
acceptance thresholds and line search stay byte-identical in their source.
The original recovered source directory is never edited.
"""
import argparse,hashlib,json,shutil
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--source-recovery',type=Path,required=True);p.add_argument('--dest',type=Path,required=True);a=p.parse_args();src=a.source_recovery.resolve();dest=a.dest.resolve()
if dest==src or dest in src.parents or src in dest.parents:raise ValueError('Independent destination required')
shutil.copytree(src,dest);f=dest/'bundle/topics/visible-flexible-closed-surface/scripts/950f-tail-stage-core.mjs';old=f.read_text();s=old
expected='53fdd936cf65f0a42929b6ce42c6ea12f183628abc9c9f3a351aac9c31ffbd6d'
if hashlib.sha256(old.encode()).hexdigest()!=expected:raise ValueError('Expected immutable original stage core hash')
anchors=["import path from 'node:path';",'export function createCompactTailShooting(', ' function correction(ev,states,target){',' function solve(target,opts={}){',' function tangentGraphAtCut(sol){',' function heightJetJacobian(sol,']
counts={x:s.count(x)for x in anchors}
if any(v!=1 for v in counts.values()):raise ValueError('Source transformation anchor must occur exactly once: '+str(counts))
s=s.replace("import path from 'node:path';","import path from 'node:path';\nimport {spawnSync} from 'node:child_process';",1)
insert='''function sparseGlobalSolve(payload){
 const helper=process.env.VISIBLE_FLEX_SPARSE_LINEAR_HELPER;
 if(!helper)throw new Error('VISIBLE_FLEX_SPARSE_LINEAR_HELPER required');
 const r=spawnSync(process.env.VISIBLE_FLEX_SPARSE_PYTHON??'python3',[helper],{input:JSON.stringify(payload),encoding:'utf8',maxBuffer:128*1024*1024});
 if(r.status!==0)throw new Error('Sparse original linear system failed: '+(r.stderr??'').slice(-2000));
 const out=JSON.parse(r.stdout);
 if(!(out.normwise_backward_error<1e-11))throw new Error('Sparse linear backward-error verification failed '+out.normwise_backward_error);
 return out;
}
'''
pos=s.index('export function createCompactTailShooting(');s=s[:pos]+insert+s[pos:]
lo=s.index(' function correction(ev,states,target){');hi=s.index(' function solve(target,opts={}){',lo)
s=s[:lo]+''' function correction(ev,states,target){
  const ans=sparseGlobalSolve({mode:'correction',M,depth,Js:ev.flows.map(f=>Array.from(f.J)),scales:Array.from(scaleFor(target)),deepGraph:Array.from(graphs[depth]),residuals:ev.residuals.map(v=>Array.from(v)),deepEnd:Array.from(ev.end),targetDelta:Array.from(target,(v,j)=>v-states[0][j])});
  return {delta:ans.delta.map(v=>Float64Array.from(v)),maxChartCondition:null,sparseLinear:ans};
 }
'''+s[hi:]
lo=s.index(' function tangentGraphAtCut(sol){');hi=s.index(' function heightJetJacobian(sol,',lo)
s=s[:lo]+''' function tangentGraphAtCut(sol){
  if(graphCache.has(sol))return graphCache.get(sol);
  if(sol.states.length!==tail.parameters.depth+1||sol.states[0].length!==K)throw Error('DN tangent checkpoint dimensions disagree');
  const states=sol.states.map(v=>Float64Array.from(v)),target=states[0].slice(0,M),scales=new Float64Array(states.length);
  scales[0]=Math.max(1e-250,...target.map(Math.abs));
  for(let n=0;n<scales.length-1;n++)scales[n+1]=scales[n]/Math.abs(tail.gains[n][0]);
  const Js=sol.linearizedFlowJacobians??tail.evaluate(states,target,true,scales).flows.map(f=>Array.from(f.J));
  const ans=sparseGlobalSolve({mode:'tangent',M,depth:Js.length,Js,scales:Array.from(scales),deepGraph:Array.from(tail.graphs[Js.length])});
  const G=Float64Array.from(ans.graph);graphCache.set(sol,G);return G;
 }
'''+s[hi:]
f.write_text(s);record=dict(scope=__doc__,original_sha256=hashlib.sha256(old.encode()).hexdigest(),patched_sha256=hashlib.sha256(s.encode()).hexdigest(),original_bytes=len(old.encode()),patched_bytes=len(s.encode()),anchor_counts=counts,patches=['import child_process and strict sparse-linear helper','Newton correction: all-node sparse solve of original linear system','cut tangent graph: all-node sparse solve of original tangent system'],helper_sha256=hashlib.sha256(Path(__file__).with_name('sparse_shooting_linear.py').read_bytes()).hexdigest());(dest/'sparse-source-change.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record))
