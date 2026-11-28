// Sample the complete successful finite-tail two-jets and locate curvature,
// Darboux-defect and positive-branch extrema, retaining symmetry-axis data.
// This is an actual finite-state audit, not a continuous enclosure/reach proof.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
const [sourceTopic,responseFile,outputFile]=process.argv.slice(2);
if(!sourceTopic || !responseFile || !outputFile)
  throw Error('Usage: node numerical-tail-curvature-locator.mjs SOURCE_TOPIC RESPONSE.json.gz OUTPUT.json');
const started=Date.now(),sourceRoot=path.join(sourceTopic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;
process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const scriptURL=name=>pathToFileURL(path.join(sourceTopic,'scripts',name));
const rawURL=name=>pathToFileURL(path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts',name));
const {createRecalibrationFactory}=await import(scriptURL('closing_weighted_tail.mjs'));
const {createSplitFluxCompactTailDN}=await import(scriptURL('78718-tail-tangent-split.mjs'));
const {createFourierRootSplitFluxEngine}=await import(scriptURL('78718-tail-fourier-root-split-engine.mjs'));
const {createMomentumPhysicalJetEvaluator}=await import(rawURL('f6tail_momentum_physical_jets.mjs'));
const bytes=fs.readFileSync(responseFile),record=JSON.parse(zlib.gunzipSync(bytes));
if(!record.response?.converged || record.response.failed)throw Error('Successful actual tail required');
const cfg=record.config,M=cfg.modes,K=2*M,steps=cfg.auditSteps??cfg.steps;
const physical=createRecalibrationFactory(cfg).assemble(),
  dn=createSplitFluxCompactTailDN({...cfg,tail:physical,retainTangentPredictor:true});
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
const states=record.response.checkpoint.states,stageRows=[];
let maximum=null,minimumA=null,maximumDefect=null,minimumAxisA=null,axisMaximum=null;
let minD=Infinity,minS=Infinity;
const snapshot=(point,y)=>({...point,state:Array.from(y)});
for(let stage=0;stage<dn.tail.cells.length;stage++) {
  const cell=dn.tail.cells[stage],engine=cell.engine,
    evaluate=createMomentumPhysicalJetEvaluator(engine,{spacing:cfg.spacing});
  let y=new Float64Array(K+2);y.set(states[stage+1]);
  let stageMinA=Infinity,stageMaxCurvature=0,stageMaxDefect=0;
  for(let profileIndex=0;profileIndex<cell.profiles.length;profileIndex++) {
    const profile=cell.profiles[profileIndex];
    for(let step=0;step<=steps;step++) {
      const x=step/steps,root=engine.root(y,profile,x),g=root.g,jets=evaluate(y,profile,x),
        wr=g.w*g.dlogwdx/g.drdx,Kg=g.w*wr/(g.r*g.E*g.E);
      minD=Math.min(minD,root.e.minD);minS=Math.min(minS,root.e.minS);
      for(let i=0;i<engine.N;i++) {
        const v=root.e.rows[i],p=jets.perAngle[i],
          angular=g.w*v.A/(g.r*Math.sqrt(g.E)*v.sd),
          mixed=g.w*v.U/(g.r*v.sd),
          radial=(p.urr-g.w2*g.dlogwdx*p.ur/(g.E*g.drdx))/(Math.sqrt(g.E)*v.sd),
          disc=Math.hypot(radial-angular,2*mixed),
          principal=[(radial+angular+disc)/2,(radial+angular-disc)/2],
          curvature=Math.max(...principal.map(Math.abs)),
          normalizedDefect=Math.abs(p.darboux*g.E*g.E*g.r*g.drdx/g.w2),
          axis=i%(engine.N/4)===0;
        stageMinA=Math.min(stageMinA,v.A);
        stageMaxCurvature=Math.max(stageMaxCurvature,curvature);
        stageMaxDefect=Math.max(stageMaxDefect,normalizedDefect);
        const keepMax=!maximum||curvature>maximum.curvature,
          keepMin=!minimumA||v.A<minimumA.A,
          keepDef=!maximumDefect||normalizedDefect>maximumDefect.normalizedDefect,
          keepAxisMin=axis&&(!minimumAxisA||v.A<minimumAxisA.A),
          keepAxisMax=axis&&(!axisMaximum||curvature>axisMaximum.curvature);
        if(keepMax||keepMin||keepDef||keepAxisMin||keepAxisMax) {
          const point={stage,rawCell:cell.rawCell??null,rawSegment:cell.rawSegment??null,
            profile:profileIndex,step,x,angleIndex:i,theta:p.theta,onReflectionAxis:axis,
            A:v.A,D:v.D,S:v.S,U:v.U,P:v.P,Pt:v.Pt,L:v.L,K:v.K,
            geometry:g,wr,intrinsicGauss:Kg,physicalJets:p,
            radial,angular,mixed,principal,curvature,normalizedDefect,
            formalGaussResidual:radial*angular-mixed*mixed-Kg,
            axisGaussFormula:wr*v.sd/(g.E**1.5*v.A)};
          const saved=snapshot(point,y);
          if(keepMax)maximum=saved;
          if(keepMin)minimumA=saved;
          if(keepDef)maximumDefect=saved;
          if(keepAxisMin)minimumAxisA=saved;
          if(keepAxisMax)axisMaximum=saved;
        }
      }
      if(step<steps)y=engine.rk4(y,profile,x,1/steps);
    }
  }
  stageRows.push({stage,rawCell:cell.rawCell??null,rawSegment:cell.rawSegment??null,
    minA:stageMinA,maxCurvature:stageMaxCurvature,maxNormalizedDefect:stageMaxDefect});
}
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const output={
  scope:'Whole saved finite nonlinear tail on its original RK audit grid. Formal height principal curvatures and projected Darboux defects are sampled; no interval enclosure or complete closed-surface reach claim.',
  source_revision:JSON.parse(fs.readFileSync(path.join(sourceTopic,'source-origin.json'))).source_revision,
  response_file:responseFile,response_sha256:hash(bytes),
  source_response_residual:record.response.residual,source_response_audit:record.response.audit??null,
  physical_height:record.request.height,config:cfg,minD,minS,
  maximumCurvature:maximum,minimumA,maximumNormalizedDefect:maximumDefect,
  reflectionAxisMinimumA:minimumAxisA,reflectionAxisMaximumCurvature:axisMaximum,
  stageRows,
  source_sha256:{...record.source_sha256,
    'numerical-tail-curvature-locator.mjs':hash(fs.readFileSync(new URL(import.meta.url)))},
  seconds:(Date.now()-started)/1000
};
const text=JSON.stringify(output,null,2)+'\n';
if(Buffer.byteLength(text)>=1_000_000)throw Error('Unexpected curvature report size');
fs.writeFileSync(outputFile,text,{flag:'wx'});
const brief=p=>({value:p.curvature,A:p.A,r:p.geometry.r,theta:p.theta,stage:p.stage,
  rawCell:p.rawCell,rawSegment:p.rawSegment,onReflectionAxis:p.onReflectionAxis});
console.log(JSON.stringify({output:outputFile,maximumCurvature:brief(maximum),minimumA:brief(minimumA),
  maxNormalizedDefect:maximumDefect.normalizedDefect,minD,minS,seconds:output.seconds}));
