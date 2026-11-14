// Numerical relative rotational heights for visual meshes of the frozen g.
// This helper is not a rigorous quadrature or vertex-error certificate.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
import {gunzipSync} from 'node:zlib';
import {parseArgs} from 'node:util';

const {values}=parseArgs({options:Object.fromEntries(
 ['manifest','calibrations','alpha','radii','out','source-root'].map(k=>[k,{type:'string'}]))});
for(const name of ['manifest','calibrations','alpha','radii','out','source-root'])
 if(!values[name])throw Error('missing --'+name);
if(fs.existsSync(values.out))throw Error('refusing to replace an existing height sample');
const here=path.dirname(fileURLToPath(import.meta.url)),topic=path.dirname(here);
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const read=p=>{const b=fs.readFileSync(p);return JSON.parse((b[0]===31&&b[1]===139?gunzipSync(b):b).toString());};
const reference=p=>path.isAbsolute(p)?p:path.resolve(topic,p);
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const manifest=read(values.manifest),cal=read(values.calibrations),alpha=read(values.alpha);
const requested=read(values.radii),radii=Array.isArray(requested)?requested:requested.radii;
const p=manifest.parameters;
if(!manifest.finished||!p||!Array.isArray(radii)||!radii.length)throw Error('missing finished manifest or radii');
if(cal.status!=='frozen-finite-source-geometry-constants'||cal.constants.length!==160||cal.infiniteSourceBeginsAt!==160)
 throw Error('requires the frozen 160-cell calibration table');
if(sha(values.calibrations)!==alpha.inputs.calibrations.sha256)throw Error('alpha calibration hash mismatch');
const checkpointFile=reference(alpha.inputs.checkpoint.file);
if(sha(checkpointFile)!==alpha.inputs.checkpoint.sha256)throw Error('background checkpoint hash mismatch');
const cpObject=read(checkpointFile),response=cpObject.response??cpObject,cp=response.checkpoint??response;
const geometryKeys=['rCut','rCuff','wCut','width','curvatureBound','delta0','R','a','etaPower','etaRatioAtN0',
 'orientation','prefixR','prefixEnd','prefixReturnStart','protectCell','slopeCap','capTransition','capMode',
 'valleyControls','pulseCaps','valleyCaps','warpWeightLevels','prefixRByCell','flatOuterThroughCell',
 'flatOuterStartSegment','flatSlope','rejoinR20At','rejoinIndexOffset'];
for(const key of geometryKeys)if(!same(p[key],cp.parameters[key]))throw Error('different frozen g parameter '+key);
for(const [key,value] of Object.entries(cal.calibrationParameters))
 if(!same(p[key]??null,value??null))throw Error('different calibration parameter '+key);
if(p.calibrationSteps!==512||p.protectCell!==160||p.orientation!==1)
 throw Error('helper is restricted to the reviewed positive 160-cell background');
const representative=alpha.savedNumericalAlpha;
if(representative!==97.64534740777785||!alpha.exactRadialAlpha.every(Number.isFinite)||
 !(alpha.exactRadialAlpha[0]<=representative&&representative<=alpha.exactRadialAlpha[1]))
 throw Error('numerical alpha representative is outside its reviewed interval');
if(radii.some(r=>typeof r!=='number'||!Number.isFinite(r)||r<p.rCuff||r>p.rCut))
 throw Error('every radius must lie in the closed frozen cuff/cut interval');
if(!radii.includes(p.rCuff)||!radii.includes(p.rCut))throw Error('radii must include exact saved cuff and cut');

const sourceRoot=path.resolve(values['source-root']);
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;
process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const sourcePaths=[path.join(here,'closing_recalibrated_tail.mjs'),path.join(here,'closing_weighted_tail.mjs'),
 ...['tailnext_balanced_tail.mjs','general_root_smooth_tail_cells.cjs'].map(n=>path.join(process.env.CLOSING_TAIL_CACHE,n))];
for(const [old,expected] of Object.entries(cal.sourceHashes)){
 const candidate=sourcePaths.find(f=>path.basename(f)===path.basename(old));
 if(!candidate||sha(candidate)!==expected)throw Error('frozen source hash mismatch '+path.basename(old));
}
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(here,'closing_weighted_tail.mjs')));
const started=performance.now(),factory=createRecalibrationFactory(p);
for(let n=0;n<160;n++)if(cal.constants[n].n!==n||factory.source.cells[n].cal.alpha!==cal.constants[n].value)
 throw Error('regenerated calibration differs from the frozen binary constant at cell '+n);

function accumulator(){let sum=0,correction=0;return {add(value){const y=value-correction,t=sum+y;correction=(t-sum)-y;sum=t;return sum;},value(){return sum;}};}
const radial=accumulator(),height=accumulator(),pieces=[];
for(let n=0;n<160;n++){
 const entries=factory.getEntries(n,p.valleyControls[n]??0).entries;
 for(let j=entries.length-1;j>=0;j--){
  const entry=entries[j],width=entry.total[0]+representative*entry.total[1],
   gain=entry.total[4]+representative*entry.total[5];
  if(!(width>=0&&gain>=0&&Number.isFinite(width)&&Number.isFinite(gain)))throw Error('invalid source integral');
  const outer=p.rCut-radial.value(),heightAtOuter=height.value();
  radial.add(width);height.add(gain);
  pieces.push({n,j,entry,width,gain,outer,inner:p.rCut-radial.value(),heightAtOuter});
 }
}
const totalHeight=height.value(),finiteInner=p.rCut-radial.value();
if(Math.abs(finiteInner-p.rCuff)>1e-9)throw Error('numerical finite radial total misses the cuff by more than 1e-9');
function relativeIntegrals(piece,x){
 const integral=piece.entry.integrate(x,1);
 return {radial:integral[0]+representative*integral[1],height:integral[4]+representative*integral[5]};
}
const rows=[];
for(const r of radii){
 if(r===p.rCut){rows.push({r,heightFromRToCut:0,location:'exact-cut-by-definition',radialResidualApprox:0,splitHeightDifferenceApprox:0});continue;}
 if(r===p.rCuff){rows.push({r,heightFromRToCut:totalHeight,location:'cuff-finite-sum-with-tiny-deep-omission',radialResidualApprox:finiteInner-p.rCuff,splitHeightDifferenceApprox:0});continue;}
 const piece=pieces.find(z=>z.outer>z.inner&&z.inner<=r&&r<=z.outer);
 if(!piece){
  if(Math.abs(r-p.rCuff)>1e-9)throw Error('no numerical source profile covers radius '+r);
  rows.push({r,heightFromRToCut:totalHeight,location:'cuff-roundoff-band-finite-sum',radialResidualApprox:finiteInner-r,splitHeightDifferenceApprox:null});
  continue;
 }
 const distance=piece.outer-r;
 let lo=0,hi=1;
 for(let k=0;k<44;k++){
  const mid=(lo+hi)/2;
  if(relativeIntegrals(piece,mid).radial>distance)lo=mid;else hi=mid;
 }
 const x=(lo+hi)/2,integral=relativeIntegrals(piece,x),mid=(x+1)/2,
  a=piece.entry.integrate(x,mid),b=piece.entry.integrate(mid,1),
  split=a[4]+b[4]+representative*(a[5]+b[5]);
 rows.push({r,heightFromRToCut:piece.heightAtOuter+integral.height,location:'finite-source-profile',
  cell:piece.n,segment:piece.j,sourceXApprox:x,sourceInverseBracketWidth:hi-lo,
  radialResidualApprox:integral.radial-distance,splitHeightDifferenceApprox:Math.abs(split-integral.height)});
}
const finiteSplits=rows.map(r=>r.splitHeightDifferenceApprox).filter(Number.isFinite);
const report={status:'numerical-background-height-samples-for-mesh-not-a-certificate',finished:true,
 scope:'Numerical samples of the same frozen source and an enclosed alpha representative. All finite calibration binaries are checked. Adaptive Gauss quadrature, bisection and binary64 arithmetic are not rigorous interval error bounds; mesh positions remain visual approximations to the proved map.',
 inputs:Object.fromEntries(['manifest','calibrations','alpha','radii'].map(k=>[k,{file:path.resolve(values[k]),sha256:sha(values[k])}])),
 backgroundCheckpoint:{file:checkpointFile,sha256:sha(checkpointFile)},
 scriptSHA256:sha(fileURLToPath(import.meta.url)),sourceSHA256:Object.fromEntries(sourcePaths.map(f=>[path.basename(f),sha(f)])),
 exactGeometryKeysMatched:geometryKeys,finiteCalibrationBinaryEqualityCount:160,
 alphaRepresentative:representative,alphaEnclosure:alpha.exactRadialAlpha,
 parameters:{rCut:p.rCut,rCuff:p.rCuff,protectCell:p.protectCell,calibrationSteps:p.calibrationSteps,
  warpSteps:p.warpSteps,quadratureTolerance:p.quadratureTolerance},
 gauge:'heightFromRToCut is positive integral_r^cut w(s) ds. Upper-tail closed z = prefix_cut_mean + tail_Vmean_at_cut - tail_Vz(r,theta) + heightFromRToCut; the lower tail is its full z reflection.',
 finiteHeightToCutApprox:totalHeight,finiteRadialWidthApprox:radial.value(),finiteInnerRadiusApprox:finiteInner,
 radialTotalMinusCuffApprox:finiteInner-p.rCuff,
 maximumInverseRadiusResidualApprox:Math.max(...rows.map(r=>Math.abs(r.radialResidualApprox))),
 maximumSplitHeightDifferenceApprox:Math.max(0,...finiteSplits),
 deepOmission:{beginsAtCell:160,exactHeightUpperExpression:'640 * 2^(-280)',heightUpper:640*2**-280,
  reason:'R15 gives w <= 1280*2^(-7*n/4) on the unchanged source n>=160; its physical width is less than 1/2. This bounds only the omitted exact deep height, not finite quadrature, inverse, alpha or rounding errors.'},
 heightIntervalCertificate:false,rows,seconds:(performance.now()-started)/1000};
fs.writeFileSync(values.out,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({finished:true,queries:rows.length,finiteHeightToCutApprox:totalHeight,
 maximumInverseRadiusResidualApprox:report.maximumInverseRadiusResidualApprox,
 maximumSplitHeightDifferenceApprox:report.maximumSplitHeightDifferenceApprox,seconds:report.seconds}));
