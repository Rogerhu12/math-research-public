#!/usr/bin/env python3
"""Install an optional bounded chord method in a separate original tail source.

Default/absent chordMaxCorrections retains the complete original solve.
Explicit 2 or 3 permits at most that many corrections per fresh stage
Jacobian, including the fresh-Jacobian correction itself.  Every trial still
uses the original field evaluation, domain handling and strict residual
descent.  Accepted shooting states receive a fresh original full Jacobian
before a response is returned.  The original iteration and outer budgets
are not increased.  This is an algorithm change, not the original path.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess


OLD_LOOP = """  const scales=scaleFor(target);let states=opts.initial?opts.initial.map(x=>Float64Array.from(x)):initial(target);
  const history=[];let last;
  for(let it=0;it<(opts.maxIterations??8);it++){
   const ev=evaluate(states,target,true,scales);last=ev;history.push({iteration:it,norm:ev.norm,minA:ev.minA,minD:ev.minD});opts.progress?.(history.at(-1),states.map(v=>Array.from(v)));
   if(ev.norm<(opts.tolerance??1e-10))break;
   const cor=correction(ev,states,target);history.at(-1).chartCondition=cor.maxChartCondition;opts.progress?.({...history.at(-1),phase:'correction'});
   let accepted=false;
   for(let k=0;k<10;k++){
    const lambda=2**(-k),trial=states.map((s,n)=>Float64Array.from(s,(v,j)=>v+lambda*cor.delta[n][j]));
    try{const test=evaluate(trial,target,false,scales);if(test.norm<ev.norm){states=trial;history.at(-1).step=lambda;accepted=true;break;}}catch(_){}
   }
   if(!accepted)throw new Error("multiple-shooting line search failed at "+ev.norm);
  }
  if(!last||last.norm>=(opts.tolerance??1e-10)){last=evaluate(states,target,true,scales);}
"""

NEW_LOOP = """  const scales=scaleFor(target);let states=opts.initial?opts.initial.map(x=>Float64Array.from(x)):initial(target);
  const maximum=Number(opts.chordMaxCorrections),tolerance=opts.tolerance??1e-10;
  if(maximum!==2&&maximum!==3)throw Error('chordMaxCorrections must be 2 or 3');
  const history=[];let last,lastExact=false,cachedJ=null,used=0,pending=null;
  function fresh(){
   const ev=evaluate(states,target,true,scales);
   cachedJ=ev.flows.map(f=>f.J);used=0;pending=null;
   return ev;
  }
  for(let it=0;it<(opts.maxIterations??8);it++){
   let ev,exact,kind;
   if(cachedJ&&used<maximum&&pending){
    ev=pending;pending=null;exact=false;kind='chord-cached-J';
    // A small state-only residual cannot authorize an approximate DN Jacobian.
    if(ev.norm<tolerance){ev=fresh();exact=true;kind='fresh-final-J';}
    else ev={...ev,flows:ev.flows.map((f,n)=>({...f,J:cachedJ[n]}))};
   }else{ev=fresh();exact=true;kind='fresh-J';}
   last=ev;lastExact=exact;
   history.push({iteration:it,norm:ev.norm,minA:ev.minA,minD:ev.minD,
                 jacobianMode:kind,correctionsOnJacobian:used,chordMaxCorrections:maximum});
   opts.progress?.(history.at(-1),states.map(v=>Array.from(v)));
   if(ev.norm<tolerance)break;
   const cor=correction(ev,states,target);used++;
   history.at(-1).chartCondition=cor.maxChartCondition;
   opts.progress?.({...history.at(-1),phase:'correction'});
   let accepted=false;
   for(let k=0;k<10;k++){
    const lambda=2**(-k),trial=states.map((s,n)=>Float64Array.from(s,(v,j)=>v+lambda*cor.delta[n][j]));
    try{const test=evaluate(trial,target,false,scales);if(test.norm<ev.norm){states=trial;pending=test;history.at(-1).step=lambda;accepted=true;break;}}catch(_){}
   }
   if(!accepted){
    // A failed chord search spends this iteration; the next iteration can
    // refresh J within the unchanged maxIterations budget. No trial is accepted.
    if(!exact){history.at(-1).refreshAfterRejectedChord=true;cachedJ=null;pending=null;continue;}
    throw new Error("multiple-shooting line search failed at "+ev.norm);
   }
  }
  // Also cover a last accepted trial at the original iteration ceiling.
  // Never emit cached stage Jacobians as the derivative of the final state.
  if(!last||last.norm>=tolerance||!lastExact){last=fresh();lastExact=true;}
"""

DISPATCH = """ function solve(target,opts={}){
  if(options.chordMaxCorrections===undefined)return solveOriginal(target,opts);
  const maximum=Number(options.chordMaxCorrections);
  if(maximum!==2&&maximum!==3)throw Error('chordMaxCorrections must be 2 or 3');
  return solveChord(target,{...opts,chordMaxCorrections:maximum});
 }
"""


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--copy-from",type=Path,required=True)
    parser.add_argument("--source-topic",type=Path,required=True)
    parser.add_argument("--manifest",type=Path,required=True)
    args=parser.parse_args()
    source=args.copy_from.resolve()
    dest=args.source_topic.resolve()
    if source==dest or dest.exists():
        raise ValueError("A fresh independent destination is required")
    path=source/"scripts/950f-tail-stage-core.mjs"
    text=path.read_text()
    start=text.index(" function solve(target,opts={}){")
    end=text.index("\n return {",start)
    original=text[start:end]
    if original.count(OLD_LOOP)!=1:
        raise ValueError("The original shooting loop does not match this patch")
    if "linearizedFlowJacobians:last.flows.map" not in original:
        raise ValueError("The original final DN derivative contract is missing")
    original_branch=original.replace(" function solve(target,opts={}){",
                                     " function solveOriginal(target,opts={}){",1)
    chord=original.replace(" function solve(target,opts={}){",
                            " function solveChord(target,opts={}){",1)
    chord=chord.replace(OLD_LOOP,NEW_LOOP,1)
    stamp="return {parameters:{...physical.parameters,modes:M,"
    replacement=("return {parameters:{...physical.parameters,"
                 "shootingAlgorithm:'bounded-chord-v1',"
                 "chordMaxCorrections:maximum,finalStageJacobian:'fresh-original',modes:M,")
    if chord.count(stamp)!=1:
        raise ValueError("The original parameter return location changed")
    chord=chord.replace(stamp,replacement,1)
    patched=text[:start]+original_branch+"\n"+chord+"\n"+DISPATCH+text[end:]
    shutil.copytree(source,dest,ignore=shutil.ignore_patterns("__pycache__","*.pyc"))
    output=dest/"scripts/950f-tail-stage-core.mjs"
    output.write_text(patched)
    subprocess.run(["node","--check",str(output)],check=True)
    report=dict(
        scope=__doc__,status="installed_and_syntax_checked",
        source_topic=str(source),destination=str(dest),
        installer_sha256=sha(__file__),
        original_stage_source_sha256=sha(path),
        patched_stage_source_sha256=sha(output),
        explicit_config_option={"chordMaxCorrections":[2,3]},
        default_original_branch_retained=True,
        shooting_trial_equations_changed=False,
        original_line_search_levels=10,original_tolerance_unchanged=True,
        original_iteration_budget_unchanged=True,
        prefix_outer_budget_unchanged=True,
        final_accepted_stage_jacobians="fresh original full evaluation",
        caches_from_accepted_state_trials_only=True,
        real_shooting_comparison_executed=False,
        active_baseline_source_changed=False)
    args.manifest.parent.mkdir(parents=True,exist_ok=True)
    args.manifest.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()

