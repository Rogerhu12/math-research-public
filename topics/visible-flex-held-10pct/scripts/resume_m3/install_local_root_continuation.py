#!/usr/bin/env python3
"""Retry a failed local momentum root using its original solver and guards.

The original direct solver is tried first. A retry starts from the zero state,
continues the actual state lambda*y, and feeds only the previous accepted L as
the next initial guess. Every accepted root meets the original residual and
D/S/A requirements. The global DN problem and acceptance gate are unchanged.
Run only on a task-local source copy.
"""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--source-topic', type=Path, required=True)
    a = p.parse_args()
    original = a.source_topic / 'repro/source-root/topics/large-amplitude-twist-flex/scripts'
    file = original / 'general_root_tail_momentum.mjs'
    before = file.read_text()
    if hashlib.sha256(before.encode()).hexdigest() != '182847f2ff1b27ff211364729c2969e4b417973efe0bba5977b2ef26e500528c':
        raise ValueError('Expected the original recorded momentum engine')
    old = ' function root(state,profile,x,guess){\n'
    marker = ' function initializeFromRaw(raw,profile,x=0){\n'
    if before.count(old) != 1 or before.count(marker) != 1 or 'directRoot' in before:
        raise ValueError('Expected the unmodified local root and raw initializer')
    addition = ''' function root(state,profile,x,guess){
  try{return directRoot(state,profile,x,guess);}
  catch(originalError){
   if(!/momentum branch D\\/S\\/A rejected|momentum Newton/.test(String(originalError)))throw originalError;
   localRootContinuationStatistics.attempted++;
   let lambda=0,step=.1,L=new Float64Array(J),last=null,tries=0;
   while(lambda<1&&tries<200){
    tries++;const next=Math.min(1,lambda+step),trial=Float64Array.from(state,v=>next*v);
    try{
     last=directRoot(trial,profile,x,L);L=last.L;lambda=next;step=Math.min(.1,1.5*step);
    }catch(error){step/=2;if(step<1e-6)break;}
   }
   localRootContinuationStatistics.maximumTries=Math.max(localRootContinuationStatistics.maximumTries,tries);
   if(lambda!==1){localRootContinuationStatistics.failed++;throw originalError;}
   localRootContinuationStatistics.accepted++;
   localRootContinuationStatistics.maximumAcceptedRelativeResidual=Math.max(localRootContinuationStatistics.maximumAcceptedRelativeResidual,last.err/last.scale);
   return {...last,continuationRetry:true,continuationTries:tries};
  }
 }
'''
    stats = '''export const localRootContinuationStatistics={attempted:0,accepted:0,failed:0,maximumTries:0,maximumAcceptedRelativeResidual:0};
'''
    after = stats + before.replace(old, ' function directRoot(state,profile,x,guess){\n').replace(marker, addition + marker)
    derived = a.source_topic / 'scripts/local-root-continuation'
    derived.mkdir(parents=True, exist_ok=True)
    legacy = '../../repro/source-root/topics/large-amplitude-twist-flex/scripts/'
    after = after.replace('"./general_exact_tail_cauchy_raw.mjs"', '"' + legacy + 'general_exact_tail_cauchy_raw.mjs"')
    (derived / file.name).write_text(after)
    records = {file.name: dict(original_sha256=hashlib.sha256(before.encode()).hexdigest(),
                              derived_sha256=hashlib.sha256(after.encode()).hexdigest())}
    for name in ['f6tail_fast_momentum.mjs', 'f6tail_momentum_split_flux.mjs', 'f6tail_fast_split_flux_engine.mjs']:
        text = (original / name).read_text()
        updated = text.replace("'./f6tail_cusp_grid.mjs'", "'" + legacy + "f6tail_cusp_grid.mjs'")
        (derived / name).write_text(updated)
        records[name] = dict(original_sha256=hashlib.sha256(text.encode()).hexdigest(),
                             derived_sha256=hashlib.sha256(updated.encode()).hexdigest())
    stage = a.source_topic / 'scripts/950f-tail-stage-split.mjs'
    text = stage.read_text()
    needle = "await import(sourceURL('f6tail_fast_split_flux_engine.mjs'))"
    if text.count(needle) != 1:
        raise ValueError('Expected original optional split factory import')
    updated = text.replace(needle, "await import('./local-root-continuation/f6tail_fast_split_flux_engine.mjs')")
    stage.write_text(updated)
    records[stage.name] = dict(original_sha256=hashlib.sha256(text.encode()).hexdigest(),
                              derived_sha256=hashlib.sha256(updated.encode()).hexdigest())
    print(json.dumps(dict(source_topic=str(a.source_topic), original_dependencies_unchanged=True,
                          modules=records, scope=__doc__), indent=2))


if __name__ == '__main__':
    main()
