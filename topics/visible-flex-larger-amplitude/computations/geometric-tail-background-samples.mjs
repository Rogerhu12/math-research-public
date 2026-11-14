// Same-source numerical background primitives for a finite assembled mesh.
// This does not certify quadrature, calibration roots, or an infinite
// nonaxisymmetric tail. It does not modify the source metric.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
import {parseArgs} from 'node:util';

const {values}=parseArgs({options:Object.fromEntries(
 ['manifest','radii','out','source-topic'].map(k=>[k,{type:'string'}]))});
for(const key of ['manifest','radii','out','source-topic'])if(!values[key])throw Error('Missing --'+key);
if(fs.existsSync(values.out))throw Error('Refusing to overwrite existing background samples');
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const read=p=>JSON.parse(fs.readFileSync(p,'utf8'));
const manifest=read(values.manifest),request=read(values.radii),radii=Array.isArray(request)?request:request.radii;
const sourceTopic=path.resolve(values['source-topic']),sourceRoot=path.join(sourceTopic,'repro/source-root');
const origin=read(path.join(sourceTopic,'source-origin.json'));
if(origin.source_revision!=='869436630c99aa5a68afb55bd8877c826034d117')throw Error('Pinned source revision required');
if(!manifest.finished||!Array.isArray(radii)||!radii.length)throw Error('Finished manifest and nonempty radius list required');
if(request.finite_tail_manifest_sha256&&request.finite_tail_manifest_sha256!==sha(values.manifest))throw Error('Radii belong to another finite tail');
const p=manifest.parameters;
if(p.orientation!==1||p.rejoinR20At!==null)throw Error('This sampler covers the recorded positive original-source tail only');
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;
process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const factoryFile=path.join(sourceTopic,'scripts/closing_weighted_tail.mjs');
const {createRecalibrationFactory}=await import(pathToFileURL(factoryFile));
const started=performance.now(),factory=createRecalibrationFactory(p),physical=factory.assemble();
const alpha=physical.stats.alpha,cut=manifest.radialGeometry.outerAnchor,cuff=p.rCuff;
const actualCut=physical.cells[0].profiles.at(-1)(1).r;
if(Math.abs(actualCut-cut)>1e-13)throw Error('Regenerated source cut differs from the finite tail anchor');
if(radii.some(r=>!Number.isFinite(r)||r<cuff||r>cut))throw Error('Requested radius outside the closed cuff/cut interval');
if(!radii.includes(cuff)||!radii.includes(cut))throw Error('Radii must include exact recorded cuff and cut');
for(const key of ['alpha','heightSpan','meridianLength','cutRadiusError'])
 if(physical.stats[key]!==manifest.physicalStats[key])throw Error('Regenerated physical stat differs: '+key);

function accumulator(){let sum=0,correction=0;return {add(value){const y=value-correction,t=sum+y;correction=(t-sum)-y;sum=t;},value(){return sum;}};}
const radial=accumulator(),height=accumulator(),pieces=[];
for(let n=0;n<p.protectCell;n++){
 const entries=factory.getEntries(n,p.valleyControls[n]??0).entries;
 for(let j=entries.length-1;j>=0;j--){
  const entry=entries[j],width=entry.total[0]+alpha*entry.total[1],gain=entry.total[4]+alpha*entry.total[5];
  if(!(width>=0&&gain>=0&&Number.isFinite(width)&&Number.isFinite(gain)))throw Error('Invalid source integral');
  const outer=cut-radial.value(),heightAtOuter=height.value();radial.add(width);height.add(gain);
  pieces.push({n,j,entry,width,gain,outer,inner:cut-radial.value(),heightAtOuter});
 }
}
const totalHeight=height.value(),finiteInner=cut-radial.value();
if(Math.abs(finiteInner-cuff)>1e-10)throw Error('Finite source radial total misses cuff');
function relative(piece,x){const a=piece.entry.integrate(x,1);return {radial:a[0]+alpha*a[1],height:a[4]+alpha*a[5]};}
function localJets(piece,x){const z=piece.entry.point(x),w=Math.exp(z.g.logw);return {w,wr:w*z.g.dlogwdx/(z.dA+alpha*z.dB)};}
const rows=[];
for(const r of radii){
 if(r===cut){const g=physical.cells[0].profiles.at(-1)(1),w=Math.exp(g.logw);rows.push({r,heightFromRToCut:0,w,wr:w*g.dlogwdx/g.drdx,location:'exact-cut-by-definition',radialResidualApprox:0,splitHeightDifferenceApprox:0});continue;}
 if(r===cuff){rows.push({r,heightFromRToCut:totalHeight,w:0,wr:0,location:'flat-limit-with-finite-sum-height-representative',radialResidualApprox:finiteInner-cuff,splitHeightDifferenceApprox:0});continue;}
 const piece=pieces.find(z=>z.outer>z.inner&&z.inner<=r&&r<=z.outer);
 if(!piece)throw Error('No positive-width numerical source piece covers radius '+r);
 const distance=piece.outer-r;let lo=0,hi=1;
 for(let k=0;k<48;k++){const mid=(lo+hi)/2;if(relative(piece,mid).radial>distance)lo=mid;else hi=mid;}
 const x=(lo+hi)/2,a=relative(piece,x),mid=(x+1)/2,left=piece.entry.integrate(x,mid),right=piece.entry.integrate(mid,1),split=left[4]+right[4]+alpha*(left[5]+right[5]);
 rows.push({r,heightFromRToCut:piece.heightAtOuter+a.height,...localJets(piece,x),location:'same-finite-source-profile',cell:piece.n,segment:piece.j,sourceXApprox:x,sourceInverseBracketWidth:hi-lo,radialResidualApprox:a.radial-distance,splitHeightDifferenceApprox:Math.abs(split-a.height)});
}
const sourcePaths=[factoryFile,path.join(sourceTopic,'scripts/closing_recalibrated_tail.mjs'),
 ...['tailnext_balanced_tail.mjs','general_root_smooth_tail_cells.cjs'].map(n=>path.join(process.env.CLOSING_TAIL_CACHE,n))];
const n=p.protectCell,delta=p.delta0*2**(-n),rmin=cuff,
 W=physical.parameters.epsilonScale*p.R*delta**(7/4)/rmin**7,
 remainingLog=6*p.delta0*2**(-n)+6*p.etaRatioAtN0*p.delta0*2**(-p.etaPower*n)/(1-2**(-p.etaPower)),
 deepWidth=cuff*Math.expm1(remainingLog/Math.sqrt(12));
const report={status:'same-source-numerical-background-samples-not-a-certificate',finished:true,
 scope:'Numerical primitives and slope jets of the identical frozen rotational background. Finite calibration binaries, positive warp parameters and the assembled alpha representative are reproduced; no interval quadrature/calibration certificate is supplied. The omitted infinite ROTATIONAL background has the R28 flat-limit route. This is not an infinite nonaxisymmetric solution or exact nonlinear DN.',
 inputs:Object.fromEntries(['manifest','radii'].map(k=>[k,{file:path.resolve(values[k]),sha256:sha(values[k])}])),
 script_sha256:sha(fileURLToPath(import.meta.url)),source_revision:origin.source_revision,source_sha256:Object.fromEntries(sourcePaths.map(f=>[path.basename(f),sha(f)])),
 parameters:{rCut:p.rCut,representedCut:cut,rCuff:cuff,protectCell:p.protectCell,calibrationSteps:p.calibrationSteps,warpSteps:p.warpSteps,quadratureTolerance:p.quadratureTolerance},
 numericalAlpha:alpha,regeneratedPhysicalStatsIdentical:true,
 finiteCalibrationValues:factory.source.cells.map((cell,n)=>({n,value:cell.cal.alpha})),
 gauge:'heightFromRToCut=integral_r^cut w. Upper tail z=prefix_cut_mean+tail_Vmean_at_cut+heightFromRToCut-Vz(r,theta); both the base and perturbation height are reflected.',
 finiteHeightToCutApprox:totalHeight,finiteRadialWidthApprox:radial.value(),finiteInnerRadiusApprox:finiteInner,radialTotalMinusCuffApprox:finiteInner-cuff,
 maximumInverseRadiusResidualApprox:Math.max(...rows.map(r=>Math.abs(r.radialResidualApprox))),maximumSplitHeightDifferenceApprox:Math.max(...rows.map(r=>r.splitHeightDifferenceApprox)),
 conditionalDeepRotationalOmission:{beginsAtCell:n,formula:'W_n=epsilon*R*delta_n^(7/4)/r_cuff^7; d_n=r_cuff*expm1((6 delta_n+6 eta0 2^(-3n/2)/(1-2^(-3/2)))/sqrt(12)); height <= W_n*d_n, under the unchanged-source R28 bounds.',numericalW:W,numericalWidth:deepWidth,numericalHeightBoundRepresentative:W*deepWidth,intervalCertificate:false},
 heightIntervalCertificate:false,rows,seconds:(performance.now()-started)/1000};
fs.writeFileSync(values.out,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({finished:true,queries:rows.length,numericalAlpha:alpha,finiteHeightToCutApprox:totalHeight,maximumInverseRadiusResidualApprox:report.maximumInverseRadiusResidualApprox,maximumSplitHeightDifferenceApprox:report.maximumSplitHeightDifferenceApprox,seconds:report.seconds}));
