// Independent cheap finite-tail root audit; no Cartesian second derivatives.
// Angular triangle diagnostics apply to the finite returned polynomial only.
// Radial extrema are sampled; no interval or infinite-tail assertion.
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

const stride=+values['sample-every'],steps=+(values['replay-steps']??p.steps),N=+(values['angular-nodes']??p.quadrature),count=Math.min(depth,+(values['max-cells']??depth));
if(!Number.isInteger(stride)||stride<1||!Number.isInteger(steps)||steps<1||!Number.isInteger(N)||N<4||(N&(N-1)))throw Error('Invalid discretization');
const sourceFiles=[fileURLToPath(import.meta.url),...['closing_recalibrated_tail.mjs','closing_weighted_tail.mjs','closing_tail_sources.mjs'].map(n=>path.join(here,n)),...['f6tail_fast_split_flux_engine.mjs','f6tail_momentum_split_flux.mjs','f6tail_fast_momentum.mjs','general_root_tail_momentum.mjs','f6tail_cusp_grid.mjs'].map(n=>path.join(sourceScripts,n))];
const keys=['maxP','maxK','maxL','maxU','maxPFiniteCoefficientTriangle','maxKFiniteCoefficientTriangle','maxLFiniteCoefficientTriangle','minASampled','minDSampled','minSSampled','minAFiniteCoefficientTriangle','minDFiniteCoefficientTriangle','minSFiniteCoefficientTriangle','maxRootRelativeResidual','maxRelativeNodeReplayError'];
const empty=()=>Object.fromEntries(keys.map(k=>[k,k.startsWith('min')?Infinity:0]));
const report={scope:'Independent sampled raw-cell root sizes for the finite projected tail. Stage geometry and rawNode mapping rebuilt independently. The coefficient-triangle quantities bound the returned finite angular polynomials algebraically, but floating arithmetic and radial interpolation are not interval-enclosed. No nonlinear infinite-tail or Cartesian two-jet certificate.',input:path.resolve(input),inputSHA256:sha(input),parameters:p,audit:{steps,N,stride,representedStages:count},sourceSHA256:Object.fromEntries(sourceFiles.map(f=>[f,sha(f)])),runtime:{node:process.version},rawNodeVerified:rawNode,rawCells:[],totals:empty()};
const sq2=Math.sqrt(2),freq=Array.from({length:M},(_,j)=>p.spacing*(j+1));
for(let n=0;n<count;n++){
 const cell=cells[n],raw=cell.rawCell;
 let row=report.rawCells[raw];if(!row){row={rawCell:raw,representedStages:0,sampledRadialPoints:0,...empty()};report.rawCells[raw]=row;}
 let engine=createFastSplitFluxMomentumTailEngine({modes:M,spacing:p.spacing,quadrature:N,mu:cell.mu,orientation:p.orientation,projectionFloor:p.projectionFloor});
 if(p.cuspAwareFlow===true)engine=withCuspAwareRK(engine);
 let y=new Float64Array(K+2);y.set(checkpoint.states[n+1]);
 for(const profile of cell.profiles)for(let k=0;k<=steps;k++){
  const x=k/steps;
  if(k%stride===0||k===steps){
   const rt=engine.root(y,profile,x),g=rt.g;
   let lp=Math.abs(rt.L[0]),kp=Math.abs(rt.L[0]),pp=0,ap=0;
   for(let j=0;j<M;j++){
    const pc=-freq[j]*g.r**3*y[j]/g.w,pt=freq[j]*pc,lc=sq2*rt.L[j+1];
    pp+=Math.abs(pc);kp+=Math.abs(lc-pt);lp+=Math.abs(lc);ap+=Math.abs(lc+g.w2*pt);
   }
   row.maxPFiniteCoefficientTriangle=Math.max(row.maxPFiniteCoefficientTriangle,pp);
   row.maxKFiniteCoefficientTriangle=Math.max(row.maxKFiniteCoefficientTriangle,kp);
   row.maxLFiniteCoefficientTriangle=Math.max(row.maxLFiniteCoefficientTriangle,lp);
   row.minAFiniteCoefficientTriangle=Math.min(row.minAFiniteCoefficientTriangle,1+rt.L[0]-ap);
   row.minDFiniteCoefficientTriangle=Math.min(row.minDFiniteCoefficientTriangle,1-g.w2*(2*kp+kp*kp+g.E*pp*pp));
   row.minSFiniteCoefficientTriangle=Math.min(row.minSFiniteCoefficientTriangle,1-g.w2*pp*pp);
   row.maxRootRelativeResidual=Math.max(row.maxRootRelativeResidual,rt.err/rt.scale);
   for(const v of rt.e.rows){
    for(const name of ['P','K','L','U'])row['max'+name]=Math.max(row['max'+name],Math.abs(v[name]));
    row.minASampled=Math.min(row.minASampled,v.A);row.minDSampled=Math.min(row.minDSampled,v.D);row.minSSampled=Math.min(row.minSSampled,v.S);
   }
   row.sampledRadialPoints++;
  }
  if(k<steps)y=engine.rk4(y,profile,x,1/steps);
 }
 const scale=Math.max(1e-250,...checkpoint.states[n].slice(0,M).map(Math.abs));
 for(let j=0;j<K;j++)row.maxRelativeNodeReplayError=Math.max(row.maxRelativeNodeReplayError,Math.abs((j<M?y[j]:y[j]/cell.portRatio)-checkpoint.states[n][j])/scale);
 row.representedStages++;
 for(const key of keys)report.totals[key]=key.startsWith('min')?Math.min(report.totals[key],row[key]):Math.max(report.totals[key],row[key]);
 fs.writeFileSync(out,JSON.stringify(report,null,2)+'\n');
 if(n+1===count||n+1===rawNode[raw+1])console.log(JSON.stringify({rawCell:raw,maxP:row.maxP,maxK:row.maxK,maxL:row.maxL,minA:row.minASampled,minD:row.minDSampled}));
}
