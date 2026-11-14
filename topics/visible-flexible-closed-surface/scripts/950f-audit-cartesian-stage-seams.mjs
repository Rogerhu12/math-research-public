// Independent replay of a supplied finite tail.  No nonlinear optimization.
// All extrema remain sampled; this is not an interval or infinite-tail proof.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL, fileURLToPath} from 'node:url';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
import {parseArgs} from 'node:util';

const {values,positionals}=parseArgs({allowPositionals:true,options:{
  'source-root':{type:'string'},'sample-every':{type:'string',default:'4'},
  'difference-step':{type:'string',default:'0.00005'},'max-cells':{type:'string'},
  'replay-steps':{type:'string'},'angular-nodes':{type:'string'},
  'height-sign':{type:'string',default:'-1'},'cut-z':{type:'string',default:'0'}}});
if(positionals.length!==2||!values['source-root'])throw Error('Usage: node 950f-audit-cartesian-tail.mjs checkpoint out.json --source-root ROOT [--max-cells N]');
const [input,out]=positionals,sourceRoot=path.resolve(values['source-root']);
if(fs.existsSync(out))throw Error('Refusing to overwrite an earlier audit record');
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;
const here=path.dirname(fileURLToPath(import.meta.url)),sourceScripts=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
process.env.CLOSING_TAIL_CACHE=sourceScripts;
const readJson=file=>{const raw=fs.readFileSync(file);return JSON.parse((file.endsWith('.gz')?gunzipSync(raw):raw).toString());};
const sha=file=>createHash('sha256').update(fs.readFileSync(file)).digest('hex');
const record=readJson(input),container=record.response??record;
const checkpoint=container.checkpoint??container.tail_checkpoint??container.seam?.tail_checkpoint??container;
if(!checkpoint.parameters||!Array.isArray(checkpoint.states))throw Error('Missing finite tail checkpoint');
const p=checkpoint.parameters,cfg=record.config??p,M=p.modes,K=2*M,depth=p.depth,rawDepth=p.physicalDepth??depth,parts=p.shootingParts??1;
if(checkpoint.states.length!==depth+1||checkpoint.states.some(v=>v.length!==K))throw Error('Bad checkpoint dimensions');
const factoryName=p.constructor==='closing_weighted_tail_v1'?'closing_weighted_tail.mjs':'closing_recalibrated_tail.mjs';
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(here,factoryName)));
const {createFastSplitFluxMomentumTailEngine}=await import(pathToFileURL(path.join(sourceScripts,'f6tail_fast_split_flux_engine.mjs')));
const {withCuspAwareRK,installCompactCriticalPoints}=await import(pathToFileURL(path.join(sourceScripts,'f6tail_cusp_grid.mjs')));
const {createRelativeSpatialJetEvaluator}=await import(pathToFileURL(path.join(sourceScripts,'f6tail_relative_spatial_jets.mjs')));
const {relativeSurfaceGeometry}=await import(pathToFileURL(path.join(sourceScripts,'f6tail_relative_development.mjs')));
const physical=createRecalibrationFactory(cfg).assemble();
const geometryKeys=['rCut','wCut','width','curvatureBound','delta0','R','a','etaPower',
  'etaRatioAtN0','orientation','prefixR','prefixEnd','prefixReturnStart','protectCell',
  'calibrationSteps','warpSteps','quadratureTolerance','slopeCap','capTransition',
  'capMode','cuspAwareQuadrature','valleyControls','rejoinR20At','rejoinIndexOffset',
  'pulseCaps','valleyCaps','flatOuterThroughCell','flatOuterStartSegment','flatSlope',
  'warpWeightLevels','constructor','rCuff','oldCut','epsilonScale','prefixRByCell'];
for(const key of geometryKeys){
  if(JSON.stringify(p[key]??null)!==JSON.stringify(physical.parameters[key]??null))throw Error('Frozen physical geometry mismatch: '+key);
}
for(const name of ['closing_recalibrated_tail.mjs','closing_weighted_tail.mjs']){
  if(record.source_hashes?.[name]&&record.source_hashes[name]!==sha(path.join(here,name)))throw Error('Recorded physical source hash mismatch: '+name);
}
if(!p.shootingParts&&p.cuspAwareFlow===true)installCompactCriticalPoints(physical);
// Match the solver's actual-cusp search only on the represented finite cells;
// scanning the unchanged n>=depth source is irrelevant to this finite audit.
if(!p.shootingParts&&p.actualCuspGrid===true)for(const cell of physical.cells.slice(0,depth))for(const profile of cell.profiles){
  const roots=[...(profile.integrationBreakpoints??[])];let a=0,fa=profile(a).dlogwdx;
  for(let k=1;k<=128;k++){
    const b=k/128,fb=profile(b).dlogwdx;
    if(fa*fb<0){let lo=a,hi=b,flo=fa;for(let j=0;j<48;j++){const mid=(lo+hi)/2,fm=profile(mid).dlogwdx;if(flo*fm<=0)hi=mid;else{lo=mid;flo=fm;}}roots.push((lo+hi)/2);}
    a=b;fa=fb;
  }
  profile.integrationBreakpoints=[...new Set(roots)].sort((a,b)=>a-b);
}
// Independently construct the subdivision; do not import the submitted
// subdividePhysical or trust its rawNode/rawStates arrays.
const cells=[],rawNode=[];
if(p.shootingParts){
  if(p.orientation!==1||!Number.isInteger(parts)||parts<1)throw Error('Unsupported recorded subdivision');
  for(let rawCell=0;rawCell<rawDepth;rawCell++){
    rawNode.push(cells.length);const source=physical.cells[rawCell];
    for(let segment=source.profiles.length-1;segment>=0;segment--)for(let part=parts-1;part>=0;part--){
      const lo=part/parts,hi=(part+1)/parts,scale=hi-lo,original=source.profiles[segment];
      const profile=u=>{const g=original(lo+scale*u);return {...g,drdx:scale*g.drdx,dlogwdx:scale*g.dlogwdx};};
      profile.integrationBreakpoints=(original.integrationBreakpoints??[]).filter(t=>t>lo&&t<hi).map(t=>(t-lo)/scale);
      cells.push({...source,profiles:[profile],portRatio:segment===source.profiles.length-1&&part===parts-1?2**p.a:1,rawCell,rawSegment:segment,rawLeft:lo,rawRight:hi});
    }
  }
  rawNode.push(cells.length);
  if(cells.length!==depth||JSON.stringify(rawNode)!==JSON.stringify(checkpoint.rawNode))throw Error('Independent stage index map disagrees');
  for(let n=0;n<rawNode.length;n++)if(JSON.stringify(checkpoint.states[rawNode[n]])!==JSON.stringify(checkpoint.rawStates[n]))throw Error('Recorded rawStates mismatch at '+n);
}else{
  for(let n=0;n<depth;n++)cells.push({...physical.cells[n],portRatio:2**p.a,rawCell:n,rawSegment:null,rawLeft:0,rawRight:1});
}
const stride=+values['sample-every'],h=+values['difference-step'],steps=+(values['replay-steps']??p.steps),N=+(values['angular-nodes']??p.quadrature),count=Math.min(depth,+(values['max-cells']??depth)),heightSign=+values['height-sign'],cutZ=+values['cut-z'];
if(![1,-1].includes(heightSign)||!Number.isInteger(stride)||stride<1||!Number.isInteger(steps)||steps<1||!Number.isInteger(N)||N<4||(N&(N-1))||!(h>0&&h<.01))throw Error('Invalid audit discretization');
const sourceFiles=[fileURLToPath(import.meta.url),...['closing_recalibrated_tail.mjs','closing_weighted_tail.mjs','closing_tail_sources.mjs','950f-tail-subdivision.mjs','950f-tail-stage-core.mjs'].map(n=>path.join(here,n)),...['f6tail_fast_split_flux_engine.mjs','f6tail_momentum_split_flux.mjs','f6tail_fast_momentum.mjs','general_root_tail_momentum.mjs','f6tail_cusp_grid.mjs','f6tail_relative_spatial_jets.mjs','f6tail_relative_development.mjs','f6tail_momentum_physical_jets.mjs','f6tail_actual_metric.mjs'].map(n=>path.join(sourceScripts,n))];
const report={scope:'Independent finite Cartesian replay with independently rebuilt shooting subdivisions and checked rawNode/rawStates. The physical metric is unchanged. Extrema are sampled; planar rr derivative uses finite differences. No infinite extension, all-time reach, or completed closed-surface assertion.',checkpointPath:path.resolve(input),checkpointSHA256:sha(input),checkpointConverged:container.converged??null,checkpointShootingResidual:container.residual??null,parameters:p,sourceSHA256:Object.fromEntries(sourceFiles.map(f=>[f,sha(f)])),runtime:{node:process.version},auditSettings:{stride,differenceStep:h,steps,N,representedStages:count,physicalDepth:rawDepth,checkpointDepth:depth,heightSign,cutZ},rawNodeVerified:rawNode,rows:[],totals:{metric:0,fullTensor:0,actualCurvature:0,formalCurvature:0,fullDarboux:0,normalizedFullDefect:0,normalizedFullDefectRawProfile:0,translationPeriod:0,angularHolonomy:0,radialGaugeMean:0,relativeNodeReplayError:0,minArea:Infinity,minProjectionD:Infinity,minLeading:Infinity,minNormalZ:Infinity,minSupportAtCutZ:Infinity,minSupportAffineConstant:Infinity},meanOffsets:{atCut:0,finiteDeepMean:0,finiteDeepBackground:0}};
Object.assign(report.totals,{seamPosition:0,seamR:0,seamThetaNormalized:0,seamRR:0,seamRThetaNormalized:0,seamThetaThetaNormalized:0});
report.seamScope='Sampled Cartesian jets in the common physical (r,theta) chart. Common vertical mean is aligned by the recorded integrated mean increments, not fitted. Planar rr jets still have finite-difference error; small discrepancies are not exact C2 matching.';
function cartesianSnapshot(a,mean){
  const result=new Float64Array(18*a.perAngle.length),g=a.g,wr=g.w*g.dlogwdx/g.drdx;
  for(let j=0;j<a.perAngle.length;j++){
    const v=a.perAngle[j],c=Math.cos(v.theta),s=Math.sin(v.theta),jet=[g.r*c+v.V[0],g.r*s+v.V[1],v.V[2]-mean,c+v.Vr[0],s+v.Vr[1],g.w+v.Vr[2],-g.r*s+v.Vt[0],g.r*c+v.Vt[1],v.Vt[2],v.Vrr[0],v.Vrr[1],wr+v.Vrr[2],-s+v.Vrt[0],c+v.Vrt[1],v.Vrt[2],-g.r*c+v.Vtt[0],-g.r*s+v.Vtt[1],v.Vtt[2]];
    result.set(jet,18*j);
  }
  return {r:g.r,values:result};
}
let meanCumulative=0,backgroundCumulative=0,previousDeep=null;
for(let n=0;n<count;n++){
  const cell=cells[n];
  let engine=createFastSplitFluxMomentumTailEngine({modes:M,spacing:p.spacing,quadrature:N,mu:cell.mu,orientation:p.orientation,projectionFloor:p.projectionFloor});
  if(p.cuspAwareFlow===true)engine=withCuspAwareRK(engine);
  const ev=createRelativeSpatialJetEvaluator(engine,{spacing:p.spacing,radialDifferenceStep:h});
  const row={n,rawCell:cell.rawCell,rawSegment:cell.rawSegment,rawLeft:cell.rawLeft,rawRight:cell.rawRight,portRatio:cell.portRatio,...Object.fromEntries(Object.keys(report.totals).map(k=>[k,k.startsWith('min')?Infinity:0])),sampledPoints:0};
  let y=new Float64Array(K+2);y.set(checkpoint.states[n+1]);
  const supportPairs=[],start=Date.now();let deepSnapshot=null,outerSnapshot=null;
  for(let segment=0;segment<cell.profiles.length;segment++){
    const profile=cell.profiles[segment];
    for(let k=0;k<=steps;k++){
      const x=k/steps;
      if(k%stride===0||k===steps){
        const a=ev.evaluate(y,profile,x),g=a.g,j=a.heightJets,d=a.development;
        if(segment===0&&k===0)deepSnapshot=cartesianSnapshot(a,y[K]);
        if(segment===cell.profiles.length-1&&k===steps)outerSnapshot=cartesianSnapshot(a,y[K]);
        row.formalCurvature=Math.max(row.formalCurvature,j.formalHeightCurvature);
        row.fullDarboux=Math.max(row.fullDarboux,j.maxDarboux);
        row.minProjectionD=Math.min(row.minProjectionD,j.minD);row.minLeading=Math.min(row.minLeading,j.minA);
        row.translationPeriod=Math.max(row.translationPeriod,d.translationPeriod);row.angularHolonomy=Math.max(row.angularHolonomy,d.angularHolonomyResidual);row.radialGaugeMean=Math.max(row.radialGaugeMean,Math.abs(d.angularPhaseMeanDerivative));
        for(const q of j.perAngle){const defect=Math.abs(q.darboux*g.E*g.E*g.r*g.drdx/g.w2);row.normalizedFullDefect=Math.max(row.normalizedFullDefect,defect);row.normalizedFullDefectRawProfile=Math.max(row.normalizedFullDefectRawProfile,defect/(cell.rawRight-cell.rawLeft));}
        for(const v of a.perAngle){
          const z=relativeSurfaceGeometry(g,v.theta,v.Vr,v.Vt,v.Vrr,v.Vrt,v.Vtt),c=Math.cos(v.theta),s=Math.sin(v.theta);
          row.metric=Math.max(row.metric,z.metric);row.fullTensor=Math.max(row.fullTensor,z.fullTensorFrobeniusBound);row.actualCurvature=Math.max(row.actualCurvature,z.actualCurvature);row.minArea=Math.min(row.minArea,z.areaNormalized);
          const xr=[c+v.Vr[0],s+v.Vr[1],heightSign*(g.w+v.Vr[2])],xt=[-g.r*s+v.Vt[0],g.r*c+v.Vt[1],heightSign*v.Vt[2]],cross=[xr[1]*xt[2]-xr[2]*xt[1],xr[2]*xt[0]-xr[0]*xt[2],xr[0]*xt[1]-xr[1]*xt[0]],area=Math.hypot(...cross),normal=cross.map(q=>q/area),xx=g.r*c+v.V[0],yy=g.r*s+v.V[1];
          const base=xx*normal[0]+yy*normal[1]+heightSign*(y[K+1]+v.V[2])*normal[2];
          supportPairs.push([base,normal[2]]);row.minNormalZ=Math.min(row.minNormalZ,normal[2]);row.sampledPoints++;
        }
      }
      if(k<steps)y=engine.rk4(y,profile,x,1/steps);
    }
  }
  if(previousDeep){
    if(Math.abs(previousDeep.r-outerSnapshot.r)>1e-12)throw Error('Adjacent physical radii do not agree');
    const labels=['seamPosition','seamR','seamThetaNormalized','seamRR','seamRThetaNormalized','seamThetaThetaNormalized'],rr=(previousDeep.r+outerSnapshot.r)/2,scales=[1,1,1/rr,1,1/rr,1/(rr*rr)];
    for(let j=0;j<N;j++)for(let k=0;k<6;k++){
      const offset=18*j+3*k,err=Math.hypot(...[0,1,2].map(l=>previousDeep.values[offset+l]-outerSnapshot.values[offset+l]))*scales[k];
      row[labels[k]]=Math.max(row[labels[k]],err);
    }
  }
  previousDeep=deepSnapshot;
  row.cellMeanChange=y[K];row.cellBackgroundChange=y[K+1];
  const offset=meanCumulative+backgroundCumulative+y[K]+y[K+1];
  for(const [base,nz] of supportPairs){const affineConstant=base-heightSign*offset*nz;row.minSupportAffineConstant=Math.min(row.minSupportAffineConstant,affineConstant);row.minSupportAtCutZ=Math.min(row.minSupportAtCutZ,affineConstant+cutZ*nz);}
  const scale=Math.max(1e-250,...checkpoint.states[n].slice(0,M).map(Math.abs));
  for(let k=0;k<K;k++)row.relativeNodeReplayError=Math.max(row.relativeNodeReplayError,Math.abs((k<M?y[k]:y[k]/cell.portRatio)-checkpoint.states[n][k])/scale);
  meanCumulative+=y[K];backgroundCumulative+=y[K+1];row.seconds=(Date.now()-start)/1000;
  for(const key of Object.keys(report.totals))report.totals[key]=key.startsWith('min')?Math.min(report.totals[key],row[key]):Math.max(report.totals[key],row[key]);
  report.rows.push(row);report.meanOffsets={atCut:0,finiteDeepMean:-meanCumulative,finiteDeepBackground:-backgroundCumulative};
  fs.writeFileSync(out,JSON.stringify(report,null,2)+'\n');
  if(n===count-1||n%18===0)console.log(JSON.stringify({stage:n,rawCell:cell.rawCell,metricSoFar:report.totals.metric,actualCurvatureSoFar:report.totals.actualCurvature,rawNormalizedFullDefectSoFar:report.totals.normalizedFullDefectRawProfile,nodeReplaySoFar:report.totals.relativeNodeReplayError}));
}
