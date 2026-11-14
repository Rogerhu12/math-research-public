// One actual saved cut state, geometrically prolonged to larger angular spaces.
// This is a local root/ODE diagnostic only: no shooting, BVP or new DN solve.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {subdividePhysical} from './950f-tail-subdivision.mjs';

const sourceRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
if(!sourceRoot)throw Error('VISIBLE_FLEX_SOURCE_ROOT required');
const src=name=>pathToFileURL(path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts',name));
const {createFastSplitFluxMomentumTailEngine}=await import(src('f6tail_fast_split_flux_engine.mjs'));
const {createMomentumPhysicalJetEvaluator}=await import(src('f6tail_momentum_physical_jets.mjs'));
const {actualMetricFromDarbouxJets}=await import(src('f6tail_actual_metric.mjs'));
const opt={};
for(let i=2;i<process.argv.length;i+=2)opt[process.argv[i].replace(/^--/,'')]=process.argv[i+1];
if(!opt.packet||!opt.out||fs.existsSync(opt.out))throw Error('Existing input and fresh --out required');
const started=Date.now(),bytes=fs.readFileSync(opt.packet),packet=JSON.parse(zlib.gunzipSync(bytes)),
 cfg=packet.config,cp=packet.response.checkpoint,oldM=cfg.modes,oldN=cfg.quadrature,
 targetM=Number(opt.modes??22),physical=createRecalibrationFactory(cfg).assemble(),
 stages=subdividePhysical(physical,cfg.depth,cfg.shootingParts),cell=stages.cells[0],
 profile=cell.profiles.at(-1),x=1,ratio=cell.portRatio,spacing=cfg.spacing,sq2=Math.sqrt(2);
if(cp.states.length!==stages.cells.length+1||targetM<oldM||!(ratio>0))throw Error('Invalid saved cut normalization');
const engine=(M,N)=>createFastSplitFluxMomentumTailEngine({modes:M,spacing,quadrature:N,
 mu:cell.mu,orientation:cfg.orientation,projectionFloor:cfg.projectionFloor??.05});
const oldEngine=engine(oldM,oldN),oldState=new Float64Array(2*oldM+2);
oldState.set(cp.states[0]);
for(let j=0;j<oldM;j++)oldState[oldM+j]*=ratio;
const oldRoot=oldEngine.root(oldState,profile,x),oldRaw=oldEngine.toRaw(oldState,profile,x,oldRoot);

function coefficients(en,y){
 const root=en.root(y,profile,x),g=root.g,field=en.rhs(y,profile,x,false,root),
  jets=createMomentumPhysicalJetEvaluator(en,{spacing})(y,profile,x),
  metric=actualMetricFromDarbouxJets(g,jets.perAngle,{returnCoordinates:true}),
  height=[],slope=[],second=[];
 for(let j=0;j<en.M;j++){
  const f=spacing*(j+1);
  height.push(g.r**4*y[j]);
  slope.push(sq2*g.w*root.L[j+1]+f*f*g.r**3*y[j]);
  second.push(sq2*g.w/g.drdx*(g.dlogwdx*root.L[j+1]+jets.Ldot[j+1])+
    f*f*g.r**3/g.drdx*(field[j]+3*g.drdx/g.r*y[j]));
 }
 const meanSlope=g.w*(1+root.L[0]),
  meanSecond=g.w/g.drdx*(g.dlogwdx*(1+root.L[0])+jets.Ldot[0]);
 let reconstructedSecondGap=0;
 for(let a=0;a<en.N;a++){
  const theta=2*Math.PI*a/en.N;
  let value=meanSecond;
  for(let j=0;j<en.M;j++)value+=second[j]*Math.cos(spacing*(j+1)*theta);
  reconstructedSecondGap=Math.max(reconstructedSecondGap,Math.abs(value-jets.perAngle[a].urr));
 }
 return {root,g,jets,metric,height,slope,second,meanSlope,meanSecond,reconstructedSecondGap};
}
const old=coefficients(oldEngine,oldState),l1=a=>a.reduce((s,v)=>s+Math.abs(v),0),
 max=a=>Math.max(0,...a.map(Math.abs));
function scalarSummary(ev,M,N){
 return {modes:M,quadrature:N,r:ev.g.r,w:ev.g.w,E:ev.g.E,
  rootRelativeResidual:ev.root.err/ev.root.scale,minA:ev.root.e.minA,minD:ev.root.e.minD,
  heightL1:l1(ev.height),slopeL1:l1(ev.slope),secondL1:l1(ev.second),
  meanSlope:ev.meanSlope,meanSecond:ev.meanSecond,
  localMetric:ev.metric.actualMetricRelativeOperatorError,rr:ev.metric.actualMetricRelativeRR,
  rt:ev.metric.actualMetricRelativeRT,tt:ev.metric.actualMetricRelativeTT,
  radialCurlCorrection:ev.metric.maximumRadialCurlCorrection,
  secondCoefficientReconstructionGap:ev.reconstructedSecondGap};
}
const rows=[];
for(const N of [oldN,Math.max(1024,oldN)].filter((v,i,a)=>a.indexOf(v)===i)){
 const en=engine(targetM,N),raw=new Float64Array(2*targetM);
 for(let j=0;j<oldM;j++){raw[j]=oldRaw.raw[j];raw[targetM+j]=oldRaw.raw[oldM+j];}
 const initialized=en.initializeFromRaw(raw,profile,x),ev=coefficients(en,initialized.state);
 if(N%oldN)throw Error('Nested quadrature expected');
 let heightGap=0,slopeGap=0,secondGap=0,positionGap=0,radialDerivativeGap=0;
 for(let a=0;a<oldN;a++){
  const b=a*N/oldN;
  heightGap=Math.max(heightGap,Math.abs(ev.jets.perAngle[b].height-old.jets.perAngle[a].height));
  slopeGap=Math.max(slopeGap,Math.abs(ev.jets.perAngle[b].ur-old.jets.perAngle[a].ur));
  secondGap=Math.max(secondGap,Math.abs(ev.jets.perAngle[b].urr-old.jets.perAngle[a].urr));
  positionGap=Math.max(positionGap,Math.hypot(...ev.metric.coordinates[b].map((v,k)=>v-old.metric.coordinates[a][k])));
  radialDerivativeGap=Math.max(radialDerivativeGap,Math.hypot(...ev.metric.radialDerivatives[b].map((v,k)=>v-old.metric.radialDerivatives[a][k])));
 }
 const delta=key=>ev[key].map((v,j)=>v-(j<oldM?old[key][j]:0));
 rows.push({...scalarSummary(ev,targetM,N),
  newHighHeightL1:l1(ev.height.slice(oldM)),newHighSlopeL1:l1(ev.slope.slice(oldM)),
  newHighSecondL1:l1(ev.second.slice(oldM)),newHighSecondMax:max(ev.second.slice(oldM)),
  allHeightChangeL1:l1(delta('height')),allSlopeChangeL1:l1(delta('slope')),
  allSecondChangeL1:l1(delta('second')),meanSlopeChange:ev.meanSlope-old.meanSlope,
  meanSecondChange:ev.meanSecond-old.meanSecond,
  commonAngleHeightGap:heightGap,commonAngleSlopeGap:slopeGap,commonAngleSecondGap:secondGap,
  commonAnglePeriodicDevelopmentPositionGap:positionGap,
  commonAnglePeriodicDevelopmentRadialDerivativeGap:radialDerivativeGap,
  highHeightSecondCoefficients:ev.second.slice(oldM).map((v,j)=>({frequency:spacing*(oldM+j+1),value:v})),
  scope:'Geometric prolongation of the SAME saved cut Q/L, then local high-mode root and ODE second jet. Not a high-mode DN endpoint.'});
}
const identity=p=>({path:path.resolve(p),bytes:fs.statSync(p).size,
 sha256:crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex')});
const report={scope:'Floating one-cut local diagnostic; no shooting, BVP, radial integration or geometric export. XYZ second derivatives and a new full tail endpoint remain unevaluated.',
 packet:identity(opt.packet),program:identity(process.argv[1]),
 port:{node:0,rawCell:cell.rawCell,rawSegment:cell.rawSegment,part:cell.part,x,
  momentumToPhysicalProfileMultiplier:ratio},
 original:scalarSummary(old,oldM,oldN),rows,elapsedSeconds:(Date.now()-started)/1000};
fs.writeFileSync(opt.out,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({out:path.resolve(opt.out),bytes:fs.statSync(opt.out).size,
 oldLocalMetric:report.original.localMetric,
 newHighSecondL1:rows.map(v=>v.newHighSecondL1),
 radialDerivativeGap:rows.map(v=>v.commonAnglePeriodicDevelopmentRadialDerivativeGap),
 elapsedSeconds:report.elapsedSeconds}));
