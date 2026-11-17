#!/usr/bin/env python3
"""Derive an initialization-only predictor experiment from the direct runner.

Every textual anchor is replaced exactly once and both source hashes are
recorded. The original DN equations, evaluate, solve, local root guards,
line search, final tolerance and geometric audit are still called unchanged.
"""
from pathlib import Path
import argparse,hashlib,json
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--source',type=Path,required=True)
p.add_argument('--output',type=Path,required=True)
a=p.parse_args();original=a.source.read_text();text=original;changes=[]
def replace(before,after,label):
    global text
    if text.count(before)!=1:raise ValueError('Expected one anchor: '+label)
    text=text.replace(before,after);changes.append(label)
replace("import {createHash} from 'node:crypto';", "import {createHash} from 'node:crypto';\nimport {spawnSync} from 'node:child_process';",'predictor linear-solve transport')
replace('const initial=remeshCheckpoint(prior,dn,createFastSplitFluxMomentumTailEngine),height=request.request.height;',
        'let initial=remeshCheckpoint(prior,dn,createFastSplitFluxMomentumTailEngine);const height=request.request.height;',
        'replace only initial-state variable')
replace('from an unscaled accepted initial state.','from a linearized accepted-state predictor.',
        'accurate scope label')
replace("initialization:'unscaled accepted previous states; no linear boundary correction'",
        "initialization:'original all-node Newton linearization used only as an initial predictor; no predictor step is labelled accepted'",
        'accurate initializer label')
block=r''' const M=cfg.modes,K=2*M,depth=dn.tail.cells.length,r=dn.cutJets(new Float64Array(K)).radius;
 const target=Float64Array.from(height,h=>h/r**4),scales=new Float64Array(depth+1);
 scales[0]=Math.max(1e-250,...target.map(Math.abs));
 for(let n=0;n<depth;n++)scales[n+1]=scales[n]/Math.abs(dn.tail.gains[n][0]);
 const ev=dn.tail.evaluate(initial,target,true,scales);
 const payload={mode:'correction',M,depth,Js:ev.flows.map(f=>Array.from(f.J)),scales:Array.from(scales),
  deepGraph:Array.from(dn.tail.graphs[depth]),residuals:ev.residuals.map(v=>Array.from(v)),
  deepEnd:Array.from(ev.end),targetDelta:Array.from(target,(v,j)=>v-initial[0][j])};
 const helper=process.env.VISIBLE_FLEX_SPARSE_LINEAR_HELPER;
 if(!helper)throw Error('Original sparse-linear helper required');
 const processResult=spawnSync(process.env.VISIBLE_FLEX_SPARSE_PYTHON??'python3',[helper],
  {input:JSON.stringify(payload),encoding:'utf8',maxBuffer:128*1024*1024});
 if(processResult.status!==0)throw Error('Predictor linear solve failed: '+processResult.stderr);
 const linear=JSON.parse(processResult.stdout);
 if(!(linear.normwise_backward_error<1e-11))throw Error('Predictor failed original backward-error check');
 record.predictor={previous_state_residual:ev.norm,linear_diagnostics:Object.fromEntries(
  Object.entries(linear).filter(([k])=>k!=='delta')),trials:[]};
 let chosen=false;
 for(const lambda of [1,.5,.25,.125]){
  const candidate=initial.map((row,n)=>Float64Array.from(row,(v,j)=>v+lambda*linear.delta[n][j]));
  try{
   const v=dn.tail.evaluate(candidate,target,true,scales);
   if(!Number.isFinite(v.norm))throw Error('Nonfinite predictor residual');
   const row={lambda,local_roots_valid:true,complete_residual:v.norm,minA:v.minA,minD:v.minD};
   record.predictor.trials.push(row);trace({event:'predictor_probe',...row});
   // Only a choice of initial guess. The unchanged solve below still has to
   // meet the complete original nonlinear boundary/residual acceptance gate.
   initial=candidate;chosen=true;record.predictor.selected_lambda=lambda;break;
  }catch(error){const row={lambda,local_roots_valid:false,error:String(error)};
   record.predictor.trials.push(row);trace({event:'predictor_probe',...row});}
 }
 if(!chosen)throw Error('No tested tangent predictor passed the original local-root guards');
'''
replace('try{\n const sol=dn.solve(height,', 'try{\n'+block+' const sol=dn.solve(height,',
        'original complete linearization as an initial predictor')
a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(text)
sha=lambda data:hashlib.sha256(data).hexdigest()
record=dict(scope=__doc__,source_sha256=sha(original.encode()),generated_sha256=sha(text.encode()),
            changes=changes,replace_counts=[1]*len(changes))
a.output.with_suffix('.generation.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record))
