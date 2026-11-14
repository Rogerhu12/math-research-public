// Generic cyclic-symmetry adapter of the pinned integrated-Fr finite exporter.
// The resulting C2 polynomial representation is an approximation with measured
// defects, not an exact infinite-tail continuation or an isometric collar.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import crypto from 'node:crypto';

const args=process.argv.slice(2),where=args.indexOf('--source-topic');
if(where<0||!args[where+1])throw Error('Use --source-topic PINNED_TOPIC, then the source export arguments: RESPONSE OUT_PREFIX --depth 8 --steps 16 ...');
const sourceTopic=path.resolve(args[where+1]);args.splice(where,2);
if(args.includes('--source-root'))throw Error('Source root is selected by --source-topic');
args.push('--source-root',path.join(sourceTopic,'repro/source-root'));
process.argv=[process.argv[0],process.argv[1],...args];
const exporter=path.join(sourceTopic,'scripts/db6f-tail-increment-export-v2.mjs');
const original=fs.readFileSync(exporter,'utf8'),adapter=fileURLToPath(import.meta.url);
const sha=data=>crypto.createHash('sha256').update(data).digest('hex');
const origin=JSON.parse(fs.readFileSync(path.join(sourceTopic,'source-origin.json')));
if(origin.source_revision!=='869436630c99aa5a68afb55bd8877c826034d117')throw Error('This adapter requires the recorded pinned source revision');
let code=original;const transformations=[];
function replace(before,after,count=1){
  const found=code.split(before).length-1;
  if(found!==count)throw Error('Pinned source interface changed: expected '+count+' copies, found '+found+' of '+before);
  code=code.split(before).join(after);transformations.push({before,after,count});
}
replace('here=path.dirname(fileURLToPath(import.meta.url))','here='+JSON.stringify(path.join(sourceTopic,'scripts')));
replace('fileURLToPath(import.meta.url)',JSON.stringify(exporter));
replace('if((m-1)%3===0)planar.push(m);','if((m-1)%p.spacing===0)planar.push(m);');
replace('const height=Array.from({length:M+1},(_,j)=>3*j)','const height=Array.from({length:M+1},(_,j)=>p.spacing*j)');
replace("symmetry:'c3'","symmetry:'c'+p.spacing");
replace('assumedBackgroundCurvature:6.001','assumedBackgroundCurvature:null,backgroundCurvatureCertificate:false');
replace('and C3 coefficients.','and the recorded cyclic-symmetry coefficients.');
const importLine="const {withCuspAwareRK}=await import(source('f6tail_cusp_grid.mjs'));";
replace(importLine,importLine+"\nconst {createFourierRootSplitFluxEngine}=await import(pathToFileURL(path.join(here,'78718-tail-fourier-root-split-engine.mjs')));");
replace('engine=withCuspAwareRK(engine);',
  'engine=withCuspAwareRK(engine); Object.assign(engine,createFourierRootSplitFluxEngine({modes:M,spacing:p.spacing,quadrature:N,mu:cell.mu,orientation:p.orientation,projectionFloor:p.projectionFloor,cuspAwareFlow:true}));');
const actualFiles=['78718-tail-fourier-root-split-engine.mjs','78718-tail-fourier-root-momentum.mjs',
 '78718-tail-fourier-product-flow.mjs','78718-tail-fourier-product-jacobian.mjs',
 '78718-tail-tangent-split.mjs','78718-tail-tangent-core.mjs'];
const adapterRecord={file:adapter,sha256:sha(fs.readFileSync(adapter)),sourceFile:exporter,sourceSha256:sha(original),sourceRevision:origin.source_revision,
  actualEngineSourceSHA256:Object.fromEntries(actualFiles.map(f=>[f,sha(fs.readFileSync(path.join(sourceTopic,'scripts',f)))])),
  scope:'Only finite-map representation: recorded cyclic Fourier lattice, the actual Fourier-root split-flux engine, integrated-Fr polynomial source and explicit stage-jet corrections. Infinite continuation, exact finite-depth DN, continuous certificates and G5 remain separate.'};
replace('report.settings.stageHermiteCorrection=true;',
  'report.settings.stageHermiteCorrection=true; report.geometricAdapter='+JSON.stringify(adapterRecord)+'; report.geometricAdapter.transformations='+JSON.stringify(transformations)+'; report.settings.spacing=p.spacing; report.settings.actualEngine="fourier-root-split-flux";');
console.log(JSON.stringify({event:'finite_tail_export_adapter',sourceRevision:origin.source_revision,sourceSha256:sha(original),adapterSha256:adapterRecord.sha256}));
await import('data:text/javascript;base64,'+Buffer.from(code).toString('base64'));
