#!/usr/bin/env python3
"""Install an optional complete-state secant initial guess in a copied worker.

This changes no physical equation, Newton step, local guard or acceptance gate.
The supplied source topic must be an isolated copy; do not patch old snapshots.
"""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--source-topic', type=Path, required=True)
    a = p.parse_args()
    file = a.source_topic / 'scripts/950f-tail-stage-port-v3.mjs'
    before = file.read_text()
    if hashlib.sha256(before.encode()).hexdigest() != '41a3fc113a8565dc2382966ed0dd299532a0510bee279552fb191aca3cb99f45':
        raise ValueError('Expected the recorded original M8/M16 continuation worker')
    marker = 'const D=[];\n'
    addition = '''let secantLow=null;
if(cfg.secantCheckpoint){
 const raw=fs.readFileSync(cfg.secantCheckpoint),record=JSON.parse((cfg.secantCheckpoint.endsWith('.gz')?zlib.gunzipSync(raw):raw).toString());
 if(record.response?.converged!==true || !(record.response.residual<=cfg.solveTolerance))throw new Error('Secant lower anchor is not an accepted actual tail');
 const prior=record.response.checkpoint;
 if(!prior?.parameters||!prior?.states||!prior?.cutHeight)throw new Error('Secant lower checkpoint is incomplete');
 const old=prior.parameters,now=dn.tail.parameters;
 for(const key of ['pulseCaps','valleyCaps','flatOuterThroughCell','flatOuterStartSegment','flatSlope','capMode','rCut','wCut','width','curvatureBound','slopeCap','capTransition','calibrationSteps','warpSteps','quadratureTolerance','cuspAwareQuadrature','orientation','prefixR','prefixEnd','prefixReturnStart','protectCell','warpWeightLevels','constructor','valleyControls','delta0','R','a','etaPower','etaRatioAtN0','rejoinR20At','rejoinIndexOffset','spacing']){
  if(JSON.stringify(old[key]??null)!==JSON.stringify(now[key]??null))throw new Error('Secant tail geometry mismatch: '+key);
 }
 if((old.physicalDepth??old.depth)>cfg.depth)throw new Error('Secant remesh cannot shorten physical depth');
 const states=remeshCheckpoint(prior,dn,createFastSplitFluxMomentumTailEngine);
 const height=Array(M).fill(0);for(let j=0;j<Math.min(old.modes,M);j++)height[j]=prior.cutHeight[j];
 secantLow={states,jets:{height}};
 trace({event:'secant_lower_state',source:cfg.secantCheckpoint,sourceModes:old.modes,targetModes:M});
}
'''
    old = '''  // Warm starts must satisfy the NEW Dirichlet height, including higher modes.
'''
    new = '''  if(last&&secantLow){
   const delta=last.jets.height[0]-secantLow.jets.height[0];
   if(Number.isFinite(delta)&&Math.abs(delta)>1e-20){
    const weight=(req.height[0]-last.jets.height[0])/delta;
    if(!Number.isFinite(weight))throw new Error('Nonfinite full-state secant weight');
    initial=last.states.map((row,n)=>row.map((v,j)=>v+weight*(v-secantLow.states[n][j])));
    trace({event:'full_state_secant_initial',call,weight,highHeight:last.jets.height[0],lowHeight:secantLow.jets.height[0]});
   }
  }
  // Warm starts must satisfy the NEW Dirichlet height, including higher modes.
'''
    if before.count(marker) != 1 or before.count(old) != 1 or 'secantLow' in before:
        raise ValueError('Source does not match the unique original warm-start blocks')
    after = before.replace(marker, addition + marker).replace(old, new)
    file.write_text(after)
    print(json.dumps(dict(file=str(file), before_sha256=hashlib.sha256(before.encode()).hexdigest(),
                          after_sha256=hashlib.sha256(after.encode()).hexdigest(),
                          replacements=2, scope=__doc__), indent=2))


if __name__ == '__main__':
    main()
