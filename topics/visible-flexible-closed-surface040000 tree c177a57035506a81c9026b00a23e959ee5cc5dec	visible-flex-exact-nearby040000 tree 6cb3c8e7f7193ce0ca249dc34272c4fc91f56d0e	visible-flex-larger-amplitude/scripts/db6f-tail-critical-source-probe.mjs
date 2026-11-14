// Numerical localization of the native64/native128 C2 interpolation defect.
// This is a source diagnostic, never a continuous or exact ODE certificate.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL,fileURLToPath} from 'node:url';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
import {parseArgs} from 'node:util';
const {positionals,values}=parseArgs({allowPositionals:true,options:{
  'source-root':{type:'string'},'radius':{type:'string',default:'0.5209378646005576'},
  'angular-nodes':{type:'string',default:'512'},
  'difference-steps':{type:'string',default:'0.0001,0.00005,0.000025,0.0000125,0.00000625'}
}});
if(positionals.length<2||!values['source-root'])throw Error('checkpoint(s) output.json --source-root ROOT required');
const output=positionals.at(-1),inputs=positionals.slice(0,-1),r=+values.radius,N=+values['angular-nodes'];
const sourceRoot=path.resolve(values['source-root']),here=path.dirname(fileURLToPath(import.meta.url));
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;
process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const src=name=>pathToFileURL(path.join(process.env.CLOSING_TAIL_CACHE,name));
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(here,'closing_weighted_tail.mjs')));
const {subdividePhysical}=await import(pathToFileURL(path.join(here,'950f-tail-subdivision.mjs')));
const {createFastSplitFluxMomentumTailEngine}=await import(src('f6tail_fast_split_flux_engine.mjs'));
const {withCuspAwareRK}=await import(src('f6tail_cusp_grid.mjs'));
const {createRelativeSpatialJetEvaluator}=await import(src('f6tail_relative_spatial_jets.mjs'));
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const records=inputs.map(input=>{const b=fs.readFileSync(input),rec=JSON.parse((input.endsWith('.gz')?gunzipSync(b):b).toString());const response=rec.response??rec;return {input,rec,cp:response.checkpoint??response};});
const factory=createRecalibrationFactory(records[0].rec.config??records[0].cp.parameters),physical=factory.assemble();
const gkeys=['rCut','wCut','width','curvatureBound','delta0','R','a','etaPower','etaRatioAtN0','orientation','prefixR','prefixEnd','prefixReturnStart','protectCell','slopeCap','capTransition','capMode','valleyControls','pulseCaps','valleyCaps','warpWeightLevels','rCuff'];
const report={status:'numerical-source-jet-probe-not-a-certificate',radius:r,angularNodes:N,
  scriptSHA256:sha(fileURLToPath(import.meta.url)),backgroundStats:physical.stats,rows:[]};
for(const {input,rec,cp} of records){
  const p=cp.parameters,M=p.modes,K=2*M;
  for(const key of gkeys)if(JSON.stringify(p[key])!==JSON.stringify(physical.parameters[key]))throw Error('background differs: '+key);
  const staged=subdividePhysical(physical,8,p.shootingParts??1);
  const index=staged.cells.findIndex(c=>c.profiles[0](0).r<=r&&r<=c.profiles[0](1).r);
  if(index<0)throw Error('radius outside stages');
  const cell=staged.cells[index],profile=cell.profiles[0];
  let lo=0,hi=1;
  for(let k=0;k<56;k++){const mid=(lo+hi)/2;if(profile(mid).r<r)lo=mid;else hi=mid;}
  const x=(lo+hi)/2;
  let engine=createFastSplitFluxMomentumTailEngine({modes:M,spacing:p.spacing,quadrature:N,mu:cell.mu,orientation:p.orientation,projectionFloor:p.projectionFloor});
  engine=withCuspAwareRK(engine);
  let state=new Float64Array(K+2);state.set(cp.states[index+1]);
  const count=Math.floor(x*p.steps);
  for(let k=0;k<count;k++)state=engine.rk4(state,profile,k/p.steps,1/p.steps);
  const remaining=x-count/p.steps;
  if(remaining>0)state=engine.rk4(state,profile,count/p.steps,remaining);
  const row={input,inputSHA256:sha(input),nativeSteps:p.steps,shootingParts:p.shootingParts,stage:index,
    rawCell:cell.rawCell,rawSegment:cell.rawSegment,rawLeft:cell.rawLeft,rawRight:cell.rawRight,
    sourceXApprox:x,sourceRadiusError:profile(x).r-r,probes:[]};
  const breaks=profile.integrationBreakpoints??[];
  row.nearestSourceBreakpointDistance=breaks.length?Math.min(...breaks.map(y=>Math.abs(y-x))):null;
  for(const h of values['difference-steps'].split(',').map(Number)){
    const evaluator=createRelativeSpatialJetEvaluator(engine,{spacing:p.spacing,radialDifferenceStep:h});
    const v=evaluator.evaluate(state,profile,x),rr=v.perAngle[0].Vrr,wr=v.g.w*v.g.dlogwdx/v.g.drdx;
    row.probes.push({differenceStep:h,perturbationRRAtThetaZero:rr,backgroundWr:wr,
      fullRRAtThetaZero:[rr[0],rr[1],wr+rr[2]],sourceMetric:v.development.actualMetricRelativeOperatorError,
      formalHeightDarboux:v.heightJets.maxDarboux});
  }
  report.rows.push(row);
}
fs.writeFileSync(output,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({radius:r,rows:report.rows.map(row=>({nativeSteps:row.nativeSteps,rawCell:row.rawCell,rawSegment:row.rawSegment,sourceX:row.sourceXApprox,nearestBreakpoint:row.nearestSourceBreakpointDistance,probes:row.probes}))}));
