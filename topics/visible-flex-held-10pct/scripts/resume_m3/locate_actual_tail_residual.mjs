// Replay one actual finite state with the exact source engine and full Jacobian
// path used by the stopping test. This does not perform a Newton correction.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
const [topic,input,out] = process.argv.slice(2);
const source = path.join(topic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT = source;
process.env.CLOSING_TAIL_CACHE = path.join(source,'topics/large-amplitude-twist-flex/scripts');
const record = JSON.parse(gunzipSync(fs.readFileSync(input))), cfg = record.config;
const checkpoint = record.response.checkpoint;
if(!checkpoint?.states || !checkpoint?.cutHeight) throw Error('A complete recorded finite state is required');
const {createRecalibrationFactory} = await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN} = await import(pathToFileURL(path.join(topic,'scripts/950f-tail-stage-split.mjs')));
const physical = createRecalibrationFactory(cfg).assemble();
const dn = createSplitFluxCompactTailDN({...cfg,tail:physical});
const M = cfg.modes, states = checkpoint.states.map(v=>Float64Array.from(v));
if(states.length !== dn.tail.cells.length+1 || states[0].length !== 2*M) throw Error('The original finite grid is required');
const radius = dn.tail.cells[0].profiles.at(-1)(1).r;
const target = Float64Array.from(checkpoint.cutHeight,v=>v/radius**4);
const scales = new Float64Array(states.length);
scales[0] = Math.max(1e-250,...Array.from(target,Math.abs));
for(let n=0;n<scales.length-1;n++) scales[n+1]=scales[n]/Math.abs(dn.tail.gains[n][0]);
const begin = performance.now();
const actual = dn.tail.evaluate(states,target,true,scales);
const bits = new DataView(new ArrayBuffer(8));
function ulp(x) {
 x=Math.abs(x);
 if(x===0)return Number.MIN_VALUE;
 bits.setFloat64(0,x,false);bits.setBigUint64(0,bits.getBigUint64(0,false)+1n,false);
 return bits.getFloat64(0,false)-x;
}
const rows = actual.flows.map((flow,n)=>{
 const cell=dn.tail.cells[n];let component=0;
 for(let j=1;j<2*M;j++) if(Math.abs(actual.residuals[n][j])>Math.abs(actual.residuals[n][component])) component=j;
 const value=states[n][component],spacing=ulp(value),difference=actual.residuals[n][component];
 return {stage:n,rawCell:cell.rawCell,rawSegment:cell.rawSegment,rawLeft:cell.rawLeft,rawRight:cell.rawRight,
   component,physicalMode:cfg.spacing*(component%M+1),componentKind:component<M?'height-variable':'momentum-variable',
   normalizedResidual:Math.abs(difference)/scales[n],signedResidual:difference,
   stateValue:value,flowValue:flow.out[component],normalizationScale:scales[n],
   componentUlp:spacing,ulpDividedByScale:spacing/scales[n],residualInComponentUlps:Math.abs(difference)/spacing,
   minA:flow.minA,minD:flow.minD};
});
const files=[process.argv[1],...['950f-tail-stage-core.mjs','950f-tail-stage-split.mjs','950f-tail-subdivision.mjs','closing_weighted_tail.mjs'].map(n=>path.join(topic,'scripts',n))];
const result={scope:'Read-only replay of one recorded complete finite tail, with the actual full-Jacobian flow path and original residual scaling. Failed inputs remain failed.',
 input, input_sha256:createHash('sha256').update(fs.readFileSync(input)).digest('hex'),
 inputAccepted:record.response.converged===true && record.response.residual<cfg.solveTolerance,
 inputFailure:record.response.failed??null, inputLastIteration:record.response.lastIteration??null,
 source_sha256:Object.fromEntries(files.map(p=>[p,createHash('sha256').update(fs.readFileSync(p)).digest('hex')])),
 modes:M,quadrature:cfg.quadrature,shootingParts:cfg.shootingParts,stages:rows.length,
 replayNormalizedResidual:actual.norm,minA:actual.minA,minD:actual.minD,
 originalGate:cfg.solveTolerance, seconds:(performance.now()-begin)/1000,
 largestResidual:rows.toSorted((a,b)=>b.normalizedResidual-a.normalizedResidual).slice(0,12),
 lowestA:rows.toSorted((a,b)=>a.minA-b.minA).slice(0,8),
 endResidualMax:Math.max(...Array.from(actual.end,v=>Math.abs(v)/scales.at(-1)))};
fs.writeFileSync(out,JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result));
