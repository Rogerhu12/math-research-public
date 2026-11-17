#!/usr/bin/env python3
"""Add an explicitly different-metric initial guess for first-valley design.

An accepted old vector is used as arbitrary normalized coordinates in the new
equations. It is not called a solution or a same-metric remesh. Only beta[0]
may change and all global solves and local guards remain unchanged.
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
    marker = 'const D=[];\n'
    if before.count(marker) != 1 or 'designInitialCheckpoint' in before:
        raise ValueError('Expected original startup marker')
    addition = '''if(cfg.designInitialCheckpoint){
 if(cfg.initialCheckpoint||cfg.secantCheckpoint)throw new Error('Different-metric initializer must be explicit and exclusive');
 const raw=fs.readFileSync(cfg.designInitialCheckpoint),record=JSON.parse((cfg.designInitialCheckpoint.endsWith('.gz')?zlib.gunzipSync(raw):raw).toString());
 if(record.response?.converged!==true||!(record.response.residual<=record.config.solveTolerance))throw new Error('Design input is not an accepted old finite tail');
 const prior=record.response.checkpoint,old=prior.parameters,now=dn.tail.parameters;
 const fixed=['pulseCaps','valleyCaps','flatOuterThroughCell','flatOuterStartSegment','flatSlope','capMode','rCut','wCut','width','curvatureBound','slopeCap','capTransition','calibrationSteps','warpSteps','quadratureTolerance','cuspAwareQuadrature','orientation','prefixR','prefixEnd','prefixReturnStart','protectCell','warpWeightLevels','constructor','delta0','R','a','etaPower','etaRatioAtN0','rejoinR20At','rejoinIndexOffset','spacing','modes','quadrature','shootingParts'];
 for(const key of fixed)if(JSON.stringify(old[key]??null)!==JSON.stringify(now[key]??null))throw new Error('Undeclared design parameter change: '+key);
 if((old.physicalDepth??old.depth)!==(now.physicalDepth??now.depth))throw new Error('Design physical depth changed');
 if(old.valleyControls.length!==now.valleyControls.length||old.valleyControls.slice(1).some((x,i)=>x!==now.valleyControls[i+1]))throw new Error('Only first valley beta may change');
 if(prior.states.length!==dn.tail.cells.length+1||prior.states.some(row=>row.length!==2*M||row.some(x=>!Number.isFinite(x))))throw new Error('Design initial state has wrong dimensions or nonfinite values');
 last={states:prior.states.map(row=>Float64Array.from(row)),jets:{height:Array.from(prior.cutHeight)}};
 trace({event:'different_metric_initial_state',source:cfg.designInitialCheckpoint,oldBeta0:old.valleyControls[0],newBeta0:now.valleyControls[0],
        scope:'Arbitrary old normalized state vector in the new physical equations; no same-metric remesh or accepted new solution is asserted.'});
}
'''
    after = before.replace(marker, addition + marker)
    file.write_text(after)
    print(json.dumps(dict(scope=__doc__, before_sha256=hashlib.sha256(before.encode()).hexdigest(),
                          after_sha256=hashlib.sha256(after.encode()).hexdigest()), indent=2))


if __name__ == '__main__':
    main()
