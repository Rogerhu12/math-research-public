#!/usr/bin/env python3
"""Optional one-neighbor initial-value retry after the original line search fails.

Only a largest residual that is the difference of adjacent finite binary64
values at an interior free state is eligible. The candidate sets that one
state value to the already computed original flow value. It is accepted only
when a new full original residual/Jacobian evaluation passes the original
tolerance. All root/RHS/RK/linear solve/residual/physical gates are unchanged.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil


HELPER = '''function oneUlpInteriorCandidate(states,ev,scales){
 let largest=0,stage=-1,component=-1;
 for(let n=0;n<ev.residuals.length;n++)for(let j=0;j<ev.residuals[n].length;j++){
  const value=Math.abs(ev.residuals[n][j])/scales[n];
  if(value>largest){largest=value;stage=n;component=j;}
 }
 if(stage<=0||stage>=states.length-1||largest!==ev.norm)return null;
 const before=states[stage][component],after=ev.flows[stage].out[component];
 if(!Number.isFinite(before)||!Number.isFinite(after)||before===after)return null;
 const bits=new DataView(new ArrayBuffer(16));
 bits.setFloat64(0,before,false);bits.setFloat64(8,after,false);
 const a=bits.getBigUint64(0,false),b=bits.getBigUint64(8,false);
 if((a>b?a-b:b-a)!==1n)return null;
 const trial=states.map(row=>Float64Array.from(row));trial[stage][component]=after;
 return {states:trial,metadata:{stage,component,before,after,absoluteChange:after-before,
   binary64NeighborDistance:1,previousNormalizedResidual:ev.norm}};
}

'''

RETRY = '''   if(!accepted&&options.oneUlpInitialRetry===true){
    const candidate=oneUlpInteriorCandidate(states,ev,scales);
    if(candidate){
     try{
      const check=evaluate(candidate.states,target,true,scales);
      opts.progress?.({...history.at(-1),phase:'one_ulp_initial_candidate',
        candidate:candidate.metadata,candidateNormalizedResidual:check.norm});
      if(check.norm<(opts.tolerance??1e-10)){
       states=candidate.states;last=check;
       history.push({iteration:it+1,norm:check.norm,minA:check.minA,minD:check.minD,
         oneUlpInitialCandidate:candidate.metadata});
       opts.progress?.(history.at(-1),states.map(v=>Array.from(v)));
       break;
      }
     }catch(error){opts.progress?.({...history.at(-1),phase:'one_ulp_initial_candidate_error',error:String(error)});}
    }
   }
'''


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('copy-from', 'source-topic', 'manifest', 'export-modules'):
        p.add_argument('--' + key, type=Path, required=True)
    a = p.parse_args()
    source, dest = a.copy_from.resolve(), a.source_topic.resolve()
    if source == dest or dest.exists():
        raise ValueError('A fresh owned source copy is required')
    name = '950f-tail-stage-core.mjs'
    original = (source / 'scripts' / name).read_text()
    marker = 'export function createCompactTailShooting(options={}){\n'
    failure = '   if(!accepted)throw new Error("multiple-shooting line search failed at "+ev.norm);'
    if original.count(marker) != 1 or original.count(failure) != 1 or 'oneUlpInteriorCandidate' in original:
        raise ValueError('Expected the original current sparse shooting flow')
    if 'function sparseGlobalSolve(payload)' not in original:
        raise ValueError('The original sparse linear solve must be present')
    derived = original.replace(marker, HELPER + marker).replace(failure, RETRY + failure)
    if derived.replace(HELPER, '').replace(RETRY, '') != original:
        raise AssertionError('An unrelated original numerical line changed')
    shutil.copytree(source, dest, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    (dest / 'scripts' / name).write_text(derived)
    a.export_modules.mkdir(parents=True, exist_ok=True)
    (a.export_modules / name).write_text(derived)
    if (source / 'scripts' / name).read_text() != original:
        raise AssertionError('The input source must remain unchanged')
    result = dict(scope=__doc__, copy_from=str(source), source_topic=str(dest),
                  configuration_flag='oneUlpInitialRetry', default_enabled=False,
                  original_sha256={name: sha(original)}, derived_sha256={name: sha(derived)},
                  installer_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  original_residual_formula_unchanged=True, original_acceptance_gate_unchanged=True,
                  maximum_candidates_per_failed_solve=1)
    a.manifest.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
