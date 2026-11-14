// Locate the smallest actual positive-branch A on a successful finite tail.
// The scan uses the saved full mixed-mode shooting state and the same RK grid.
// It records the angular and radial geometry instead of treating the guard as
// a theorem of nonexistence. No source file is modified.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';

const [sourceTopic,responseFile,outputFile]=process.argv.slice(2);
if(!sourceTopic || !responseFile || !outputFile)
  throw Error('Usage: node numerical-tail-branch-locator.mjs SOURCE_TOPIC RESPONSE.json.gz OUTPUT.json');
const started=Date.now(),sourceRoot=path.join(sourceTopic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;
process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const sourceURL=name=>pathToFileURL(path.join(sourceTopic,'scripts',name));
const {createRecalibrationFactory}=await import(sourceURL('closing_weighted_tail.mjs'));
const {createSplitFluxCompactTailDN}=await import(sourceURL('78718-tail-tangent-split.mjs'));
const {createFourierRootSplitFluxEngine}=await import(sourceURL('78718-tail-fourier-root-split-engine.mjs'));
const {createMomentumPhysicalJetEvaluator}=await import(pathToFileURL(path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts/f6tail_momentum_physical_jets.mjs')));
const bytes=fs.readFileSync(responseFile),record=JSON.parse(zlib.gunzipSync(bytes));
if(!record.response?.converged || record.response.failed)throw Error('Successful actual tail required');
const cfg=record.config,M=cfg.modes,K=2*M,steps=cfg.auditSteps??cfg.steps;
const physical=createRecalibrationFactory(cfg).assemble();
const dn=createSplitFluxCompactTailDN({...cfg,tail:physical,retainTangentPredictor:true});
const transformed=new Set();
for(const cell of dn.tail.cells) {
  if(transformed.has(cell.engine))continue;
  transformed.add(cell.engine);
  Object.assign(cell.engine,createFourierRootSplitFluxEngine({
    modes:M,spacing:cfg.spacing,quadrature:cfg.quadrature,mu:cell.mu,
    orientation:dn.tail.parameters.orientation,projectionFloor:dn.tail.parameters.projectionFloor,
    cuspAwareFlow:cfg.cuspAwareFlow===true
  }));
}
const states=record.response.checkpoint.states,rows=[];
let minimum=null,minD=Infinity,minS=Infinity;
for(let n=0;n<dn.tail.cells.length;n++) {
  const cell=dn.tail.cells[n];let y=new Float64Array(K+2);y.set(states[n+1]);
  let stageMin=Infinity;
  for(let j=0;j<cell.profiles.length;j++) {
    const profile=cell.profiles[j];
    for(let k=0;k<=steps;k++) {
      const x=k/steps,rt=cell.engine.root(y,profile,x);
      minD=Math.min(minD,rt.e.minD);minS=Math.min(minS,rt.e.minS);
      stageMin=Math.min(stageMin,rt.e.minA);
      if(!minimum || rt.e.minA<minimum.A) {
        const angle=rt.e.rows.reduce((best,v,i)=>v.A<rt.e.rows[best].A?i:best,0);
        minimum={stage:n,profile:j,step:k,x,angleIndex:angle,theta:2*Math.PI*angle/cell.engine.N,
          rawCell:cell.rawCell??null,rawSegment:cell.rawSegment??null,
          ...rt.e.rows[angle],geometry:rt.g,state:Array.from(y)};
      }
      if(k<steps)y=cell.engine.rk4(y,profile,x,1/steps);
    }
  }
  rows.push({stage:n,rawCell:cell.rawCell??null,rawSegment:cell.rawSegment??null,minA:stageMin});
}
const cell=dn.tail.cells[minimum.stage],profile=cell.profiles[minimum.profile];
const evaluator=createMomentumPhysicalJetEvaluator(cell.engine,{spacing:cfg.spacing});
const jet=evaluator(Float64Array.from(minimum.state),profile,minimum.x);
const p=jet.perAngle[minimum.angleIndex],g=minimum.geometry,v=minimum;
const wr=g.w*g.dlogwdx/g.drdx,Kg=g.w*wr/(g.r*g.E*g.E),
  angular=g.w*v.A/(g.r*Math.sqrt(g.E)*v.sd),
  mixed=g.w*v.U/(g.r*v.sd),
  radial=(p.urr-g.w2*g.dlogwdx*p.ur/(g.E*g.drdx))/(Math.sqrt(g.E)*v.sd),
  disc=Math.hypot(radial-angular,2*mixed),
  principal=[(radial+angular+disc)/2,(radial+angular-disc)/2];
const angleToAxis=Math.min(...[0,Math.PI/2,Math.PI,3*Math.PI/2,2*Math.PI].map(a=>Math.abs(minimum.theta-a)));
const hash=x=>crypto.createHash('sha256').update(x).digest('hex');
const result={
  scope:'Sampled location of the true finite nonlinear tail minimum A. This is a successful-state diagnostic, not an existence boundary or a continuous-angle certificate.',
  source_revision:JSON.parse(fs.readFileSync(path.join(sourceTopic,'source-origin.json'))).source_revision,
  response_file:responseFile,response_sha256:hash(bytes),
  source_response_residual:record.response.residual,source_response_audit:record.response.audit??null,
  physical_height:record.request.height,config:cfg,
  sampled_minD:minD,sampled_minS:minS,
  minimum:{...minimum,angleToReflectionAxis:angleToAxis,
    physicalJets:p,radialSlopeDerivative:wr,intrinsicGauss:Kg,
    formalSecondForm:{radial,angular,mixed,principal},
    formalGaussResidual:radial*angular-mixed*mixed-Kg,
    exactGaussRequiredRadial:(Kg+mixed*mixed)/angular,
    axisGaussFormula:wr*v.sd/(g.E**1.5*v.A),
    axisFormulaApplicable:angleToAxis<1e-13,
    formalCurvatureAtSameRadialSample:jet.formalHeightCurvature,
    fullDarbouxAtSameRadialSample:jet.maxDarboux},
  stage_minima:rows,
  source_sha256:{...record.source_sha256,
    'numerical-tail-branch-locator.mjs':hash(fs.readFileSync(new URL(import.meta.url)))},
  seconds:(Date.now()-started)/1000
};
const output=JSON.stringify(result,null,2)+'\n';
if(Buffer.byteLength(output)>=1_000_000)throw Error('Unexpected branch report size');
fs.writeFileSync(outputFile,output,{flag:'wx'});
console.log(JSON.stringify({output:outputFile,minA:minimum.A,minD,minS,stage:minimum.stage,
  rawCell:minimum.rawCell,rawSegment:minimum.rawSegment,r:g.r,w:g.w,theta:minimum.theta,
  angleToAxis,wr,Kg,angular,mixed,radial,principal,seconds:result.seconds}));
