#!/usr/bin/env python3
"""Optional complete-spectrum harmonic warm predictor; no physical gate change.

The default worker branch remains original. The new switch is explicitly
fullHarmonicWarmPredictor=true and also requires a declared
fullHarmonicPredictorMaxScale. Exact rational arithmetic checks the actual
binary H vectors against a single fundamental ratio with a stated small
formation allowance. An ineligible vector or excessive power scale falls
back to the original predictor. This is an initial-guess algorithm change,
not a proof of improved residual or a reason to omit any original tail gate.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess


HELPER = r'''// Pure eligibility check: no geometry, flow, matrix, or solver is run.
// Values of all supplied binary64 heights are interpreted as exact rationals.
const buffer=new ArrayBuffer(8),view=new DataView(buffer);
const abs=n=>n<0n?-n:n;
function gcd(a,b){a=abs(a);b=abs(b);while(b){const r=a%b;a=b;b=r;}return a;}
function rational(x){
 if(!Number.isFinite(x))throw Error('Nonfinite height in predictor check');
 if(x===0)return {n:0n,d:1n};
 view.setFloat64(0,x,false);const bits=view.getBigUint64(0,false);
 const e=Number((bits>>52n)&2047n),mant=bits&((1n<<52n)-1n);
 let n=e===0?mant:mant+(1n<<52n),shift=e===0?-1074:e-1075;
 if(bits>>63n)n=-n;
 let d=1n;if(shift>=0)n<<=BigInt(shift);else d<<=BigInt(-shift);
 const g=gcd(n,d);return {n:n/g,d:d/g};
}
export function fullHarmonicEligibility(previous,next,ratio,maxScale){
 if(!Number.isFinite(maxScale)||maxScale<1)
  throw Error('fullHarmonicPredictorMaxScale must be an explicit finite number >= 1');
 const M=previous.length;
 const report={eligible:false,scope:'Initial-guess selection only; no shooting or domain gate is relaxed.',
  ratio,maxScale,formationAllowance:'abs(new_j-old_j*r^j) <= (32*j+16)*2^-52*max(abs(new_j),abs(old_j*r^j)); exact binary-input rationals, j=1..M',
  formationAllowanceIsNotLibmAccuracyCertificate:true};
 if(next.length!==M||M<1||!Number.isFinite(ratio)||ratio<=.25||ratio>=4||
    previous.some(v=>!Number.isFinite(v))||next.some(v=>!Number.isFinite(v))||previous[0]===0||next[0]===0)
  return {...report,reason:'invalid-fundamental-or-height-shape'};
 const a=rational(previous[0]),b=rational(next[0]);
 let rn=b.n*a.d,rd=b.d*a.n;if(rd<0n){rn=-rn;rd=-rd;}
 if(rn<=0n)return {...report,reason:'nonpositive-ratio'};
 const g=gcd(rn,rd);rn/=g;rd/=g;
 let exactMatches=0,maximumFormationUnits=0;
 for(let j=0;j<M;j++){
  if(previous[j]===0||next[j]===0){
   if(previous[j]!==0||next[j]!==0)return {...report,reason:'zero-pattern-mismatch',harmonic:j+1};
   exactMatches++;continue;
  }
  const u=rational(previous[j]),v=rational(next[j]),k=BigInt(j+1);
  const pn=u.n*(rn**k),pd=u.d*(rd**k);
  const A=v.n*pd,B=pn*v.d,diff=abs(A-B),scale=abs(A)>abs(B)?abs(A):abs(B);
  const units=BigInt(32*(j+1)+16),scaled=diff*(1n<<52n);
  if(scaled>units*scale)return {...report,reason:'complete-spectrum-not-harmonic',harmonic:j+1};
  if(diff===0n)exactMatches++;
  const upper=diff===0n?0:Number((scaled+scale-1n)/scale);
  maximumFormationUnits=Math.max(maximumFormationUnits,upper);
 }
 const powers=Array.from({length:M},(_,j)=>ratio**(j+1));
 const maximumMultiplier=Math.max(...powers);
 if(powers.some(v=>!Number.isFinite(v)||v<=0)||maximumMultiplier>maxScale)
  return {...report,reason:'explicit-power-scale-cap',maximumMultiplier,exactMatches,maximumFormationUnits};
 return {...report,eligible:true,reason:'all-heights-match-declared-harmonic-relation',
  maximumMultiplier,exactMatches,maximumFormationUnits};
}
'''

OLD = '''  if(last){
   const prev=last.jets.height[0],ratio=req.height[0]/prev;
   if(Number.isFinite(ratio)&&ratio>.25&&ratio<4)initial=last.states.map(row=>row.map((v,j)=>v*(cfg.harmonicAmplitudePredictor===true && req.height.slice(1).every(x=>x===0)?ratio**(j%M+1):ratio)));
  }'''
NEW = '''  if(last){
   const prev=last.jets.height[0],ratio=req.height[0]/prev;
   if(Number.isFinite(ratio)&&ratio>.25&&ratio<4){
    if(cfg.fullHarmonicWarmPredictor!==true){
     initial=last.states.map(row=>row.map((v,j)=>v*(cfg.harmonicAmplitudePredictor===true && req.height.slice(1).every(x=>x===0)?ratio**(j%M+1):ratio)));
    }else{
     const check=fullHarmonicEligibility(last.jets.height,req.height,ratio,cfg.fullHarmonicPredictorMaxScale);
     const legacy=cfg.harmonicAmplitudePredictor===true && req.height.slice(1).every(x=>x===0);
     let powers=legacy||check.eligible;
     initial=last.states.map(row=>row.map((v,j)=>v*(powers?ratio**(j%M+1):ratio)));
     let nonfiniteFallback=false;
     if(!legacy&&powers&&initial.some(row=>row.some(v=>!Number.isFinite(v)))){
      powers=false;nonfiniteFallback=true;
      initial=last.states.map(row=>row.map(v=>v*ratio));
     }
     trace({event:'warm_predictor',kind:powers?'harmonic-powers':'original-uniform-ratio',
            legacyFundamentalOnly:legacy,completeSpectrumCheck:check,nonfiniteFallback,
            originalLinearBoundaryCorrectionRetained:cfg.correctInitialBoundary!==false});
    }
   }
  }'''


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--copy-from',type=Path,required=True)
    p.add_argument('--source-topic',type=Path,required=True)
    p.add_argument('--manifest',type=Path,required=True)
    a=p.parse_args();source=a.copy_from.resolve();dest=a.source_topic.resolve()
    if dest.exists() or source==dest:
        raise ValueError('Use a fresh independent source destination')
    worker=source/'scripts/950f-tail-stage-port-v3.mjs';text=worker.read_text()
    if text.count(OLD)!=1:
        raise ValueError('The original warm predictor source does not match')
    if text.count('if(initial&&cfg.correctInitialBoundary!==false)')!=1:
        raise ValueError('The original linear boundary correction is missing')
    anchor="import {remeshCheckpoint} from './950f-tail-warm-remesh.mjs';"
    if text.count(anchor)!=1:
        raise ValueError('The worker import anchor changed')
    patched=text.replace(anchor,anchor+"\nimport {fullHarmonicEligibility} from './full_harmonic_warm_predictor.mjs';",1).replace(OLD,NEW,1)
    shutil.copytree(source,dest,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    output=dest/'scripts/950f-tail-stage-port-v3.mjs';output.write_text(patched)
    helper=dest/'scripts/full_harmonic_warm_predictor.mjs';helper.write_text(HELPER)
    for path in (output,helper):
        subprocess.run(['node','--check',str(path)],check=True)
    record=dict(status='installed_and_syntax_checked',source_topic=str(source),destination=str(dest),
        installer_sha256=sha(__file__),original_worker_sha256=sha(worker),
        patched_worker_sha256=sha(output),eligibility_helper_sha256=sha(helper),
        explicit_switch='fullHarmonicWarmPredictor=true',
        explicit_power_cap='fullHarmonicPredictorMaxScale, a finite number >=1; no default acceptance',
        default_original_branch_unchanged=True,original_boundary_correction_unchanged=True,
        physical_parameters_or_acceptance_gates_changed=False,
        comparison_or_tail_solve_executed=False,
        scope='Optional initial-guess algorithm preparation only. Complete H consistency does not certify interior higher-mode signal or residual improvement.')
    a.manifest.parent.mkdir(parents=True,exist_ok=True)
    a.manifest.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))


if __name__=='__main__':
    main()
