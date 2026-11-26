"use strict";
/* Use the already proved R208 all-channel Boehm injection on a recovered
 * R211/quartic state. The checkpoint schema transition below is explicit:
 * only its physical representation is projected to the older R208 API.
 * Loss history is never relabelled; changed quadrature starts a fresh branch.
 */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const {createMemoryBoundR211RunProvider}=require("./6a65-low-memory-r211-provider-recovered-20261126.cjs");
const {createQuarticMetricProvider}=require("./6a65-quartic-metric-recovered-20261126.cjs");
const {createR201R205AmplitudeGeometryProvider}=require("./fd2d-R201-R205-variable-amplitude-geometric-guide.cjs");
const {prolongR201R205State}=require("./fd2d-R201-R205-complete-radial-prolongation.cjs");
const {createR196CubicSplines}=require("./fd2d-cubic-spline-refinement-R196.cjs");
const acceptedSchemas=new Set([
 "6a65-R211-original-metric-checkpoint-v1",
 "6a65-R211-quartic-metric-checkpoint-v1",
 "6a65-R211-radial-refinement-initial-v1"
]);
const dot=(x,y)=>x[0]*y[0]+x[1]*y[1]+x[2]*y[2];
const hash=f=>crypto.createHash("sha256").update(fs.readFileSync(f)).digest("hex");
function build(candidate,input){
 const base=createMemoryBoundR211RunProvider(candidate,input);
 const tau=input.metricTau??.05;
 if(!(Number.isFinite(tau)&&tau>0))throw Error("Explicit positive quartic metric tau required");
 const quartic=createQuarticMetricProvider(base.position,base.engine,tau);
 const provider=createR201R205AmplitudeGeometryProvider(quartic,input.geometryOptions);
 return {...base,quartic,provider};
}
function radialBlocks(J,K){
 const legacy=J*(2*K+2)+1;
 return Array.from({length:J},(_,j)=>[
  ...Array.from({length:K},(_,k)=>j*K+k),
  ...Array.from({length:K},(_,k)=>J*K+j*K+k),
  2*J*K+j,2*J*K+J+1+j,
  ...Array.from({length:2*K+1},(_,k)=>legacy+j*(2*K+1)+k)
 ]);
}
function inject(candidate,input,knots){
 if(!acceptedSchemas.has(input.schema))throw Error("Known recovered complete checkpoint required");
 if(input.outerLengthDesign)throw Error("This adapter is for the unextended background; rebuild length-design providers explicitly");
 const o=input.options,J=o?.radialBasisCount,K=o?.modes,n=J*(4*K+3)+2;
 if(!Number.isInteger(J)||!Number.isInteger(K)||!Array.isArray(input.z)||input.z.length!==n)
  throw Error("Complete physical layout required");
 const old=createMemoryBoundR211RunProvider(candidate,input);
 const cut=old.metric.definition.stateLayout.cutHeight,A=old.position.amplitudeIndex;
 if(cut!==J*(2*K+1)||A!==n-1||old.position.dimension!==n)
  throw Error("Physical factory and all-channel R208 layout disagree");
 const physicalView={
  schema:"fd2d-R201-R205-variable-amplitude-actual-checkpoint-v1",
  options:o,z:input.z,curvatureOptions:input.curvatureOptions,
  geometryOptions:input.geometryOptions,centralSeed:input.centralSeed,
  nextLambda:input.nextLambda??input.lambda,cutHeightIndex:cut,amplitudeIndex:A
 };
 const mapped=prolongR201R205State(physicalView,knots);
 const next={
  schema:"6a65-R211-radial-refinement-initial-v1",candidate:input.candidate??null,
  options:mapped.options,z:mapped.z,
  curvatureOptions:input.curvatureOptions,geometryOptions:input.geometryOptions,
  centralSeed:input.centralSeed??null,metricTau:input.metricTau??.05,
  nextLambda:input.nextLambda??input.lambda??1e-3,
  amplitudeIndex:mapped.amplitudeIndex,cutHeightIndex:mapped.cutHeightIndex,
  metricBranchAcceptedSteps:0,acceptedSteps:0,accepted:false,
  parent:{schema:input.schema,metricBranchAcceptedSteps:input.metricBranchAcceptedSteps??null},
  refinement:{
   method:"Existing R208 all-channel exact rational Boehm insertion, one final binary64 rounding",
   insertedKnots:mapped.insertedKnots,oldDimension:mapped.oldDimension,newDimension:mapped.newDimension,
   oldRadialCount:mapped.oldRadialCount,newRadialCount:mapped.newRadialCount,
   physicalViewSchemaConversionExplicit:true,lossHistoryRelabelled:false,
   originalSchema:input.schema,
   exactRealAllChannelFieldPreserved:true,finiteStoredFieldClaimedBitwiseEqual:false,
   storedSplineRoundoffBounds:mapped.storedSplineRoundoffBounds,
   newRadialQuadratureRequiresFreshBaseline:true,acceptedOptimizationStep:false
  },continuousCertificate:false,strongTargetComplete:false
 };
 const now=createMemoryBoundR211RunProvider(candidate,next);
 if(old.metric.base.end!==now.metric.base.end||old.metric.base.centralLength!==now.metric.base.centralLength||
    old.metric.curve.A!==now.metric.curve.A||old.metric.curve.B!==now.metric.curve.B)
  throw Error("Physical background/central curve changed during same-field insertion");
 return {old,now,next,mapped};
}
/* One insertion adds a single radial quotient direction. Its Euclidean
 * coefficient-orthogonal representative is used only as a diagnostic.
 * No pre-existing column is deleted or assumed to be solved. */
function newRadialDetail(oldKnots,knot){
 const spline=createR196CubicSplines(),M=spline.insertionMatrix(oldKnots,knot);
 const rows=M.rows.length,cols=M.old_count;
 const P=Array.from({length:cols},()=>new Float64Array(rows));
 for(let i=0;i<rows;i++)for(let k=0;k<M.rows[i].old_indices.length;k++){
  const w=M.rows[i].weights[k];P[M.rows[i].old_indices[k]][i]=Number(w[0])/Number(w[1]);
 }
 const inner=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0),Q=[];
 for(const column of P){
  const q=Float64Array.from(column);
  for(let pass=0;pass<2;pass++)for(const old of Q){
   const a=inner(q,old);for(let i=0;i<rows;i++)q[i]-=a*old[i];
  }
  const norm=Math.sqrt(inner(q,q));if(!(norm>1e-10))throw Error("Unexpected deficient Boehm column rank");
  for(let i=0;i<rows;i++)q[i]/=norm;Q.push(q);
 }
 let best=null,bestNorm=0;
 for(let k=0;k<rows;k++){
  const q=new Float64Array(rows);q[k]=1;
  for(let pass=0;pass<2;pass++)for(const old of Q){
   const a=inner(q,old);for(let i=0;i<rows;i++)q[i]-=a*old[i];
  }
  const norm=Math.sqrt(inner(q,q));if(norm>bestNorm){best=q;bestNorm=norm;}
 }
 if(!(bestNorm>1e-10))throw Error("Expected one new radial quotient direction");
 for(let i=0;i<rows;i++)best[i]/=bestNorm;
 return {vector:best,maxOldColumnContraction:Math.max(...P.map(p=>Math.abs(inner(p,best)))),
  normalization:"unit Euclidean coefficient norm; not a geometric norm",old_count:cols,new_count:rows};
}
function detailAtPoint(position,z,detail,s,u){
 const p=position.slice(s,z,true).point(u),md=position.definition.parentMetric;
 const J=md.radialBasisCount,K=md.angularModes,blocks=radialBlocks(J,K),width=4*K+3;
 const indexToBlock=new Map();for(let j=0;j<J;j++)for(let h=0;h<width;h++)indexToBlock.set(blocks[j][h],[j,h]);
 const e=dot(p.jets.Xs,p.jets.Xs)-1,T=p.jets.Xu.map(x=>x/p.a),f=dot(p.jets.Xs,T);
 const de=new Float64Array(width),df=new Float64Array(width),rho=md.stateLayout.radius;
 for(let k=0;k<p.indices.length;k++){
  const idx=p.indices[k],loc=indexToBlock.get(idx);if(!loc)continue;
  const [j,h]=loc,d=p.parameterJets[k],da=idx>=rho[0]&&idx<rho[1]?dot(d.Xu,T):0;
  const dT=d.Xu.map((x,l)=>(x-da*T[l])/p.a),v=detail.vector[j];
  de[h]+=v*2*dot(p.jets.Xs,d.Xs);df[h]+=v*(dot(d.Xs,T)+dot(p.jets.Xs,dT));
 }
 const labels=[...Array.from({length:K},(_,k)=>"theta_sin_"+(2*k+2)),
  ...Array.from({length:K},(_,k)=>"psi_sin_"+(2*k+2)),"height","rho","theta_constant",
  ...Array.from({length:K},(_,k)=>"theta_cos_"+(2*k+2)),
  ...Array.from({length:K},(_,k)=>"psi_cos_"+(2*k+2))];
 const channels=Array.from(de,(value,h)=>({channel:labels[h],de:value,df:df[h]})).sort((a,b)=>Math.abs(b.de)-Math.abs(a.de));
 return {s,u,e,f,largestNewDetailEColumns:channels.slice(0,8),allNewDetailEGradientNorm:Math.hypot(...de),
  maxOldColumnContraction:detail.maxOldColumnContraction,
  meaning:"Local derivative in the newly added radial quotient space only; no global descent or optimum claim"};
}
function diagnostics(candidate,input,knots,{fullBaseline=true}={}){
 const start=Date.now(),r=inject(candidate,input,knots),keys=["X","Xs","Xu","Xss","Xsu","Xuu"];
 const c=r.old.metric.base.centralLength,S=r.old.metric.base.end,L=S-c;
 const sites=[{s:0,u:0},{s:c,u:Math.PI/2},{s:.1359375,u:Math.PI},{s:c+L*.9,u:Math.PI*37/64},{s:S,u:0}];
 const max=Object.fromEntries(keys.map(k=>[k,0]));
 for(const {s,u}of sites){
  const a=r.old.position.slice(s,input.z,false).point(u),b=r.now.position.slice(s,r.next.z,false).point(u);
  for(const key of keys)for(let k=0;k<3;k++)max[key]=Math.max(max[key],Math.abs(a.jets[key][k]-b.jets[key][k]));
  r.old.position.clearSliceReuse();r.now.position.clearSliceReuse();
 }
 let detail=null;
 if(knots.length===1){
  detail=detailAtPoint(r.now.position,r.next.z,newRadialDetail(input.options.radialKnots,knots[0]),.1359375,Math.PI);
 }
 let baseline=null;
 if(fullBaseline){
  const built=build(candidate,r.next);baseline=built.provider.value(r.next.z);
  r.next.providerDefinition=built.provider.definition;r.next.baseline=baseline;
 }
 return {initial:r.next,report:{
  schema:"6a65-R208-recovered-quartic-refinement-diagnostic-v1",
  parentSchema:input.schema,parentAcceptedSteps:input.metricBranchAcceptedSteps,
  oldDimension:input.z.length,newDimension:r.next.z.length,insertedKnots:r.mapped.insertedKnots,
  physicalSpan:{c,S,L},sameStoredFieldProbeMaximumJetDifferences:max,
  probesAreNotContinuousRoundoffCertificate:true,novelRadialDetailAtOldObservedPeak:detail,
  freshCompleteBaseline:baseline,baselineIsNotAnAcceptedStep:true,
  elapsedSeconds:(Date.now()-start)/1000,continuousCertificate:false,strongTargetComplete:false
 }};
}
module.exports={inject,diagnostics,newRadialDetail};
if(require.main===module){
 const [candidatePath,inputPath,knotsText,prefix]=process.argv.slice(2);
 if(!candidatePath||!inputPath||!knotsText||!prefix)throw Error("candidate checkpoint inserted-knots-JSON fresh-prefix");
 const initialPath=prefix+"-initial.json",reportPath=prefix+"-report.json";
 if(fs.existsSync(initialPath)||fs.existsSync(reportPath))throw Error("Fresh outputs required");
 const r=diagnostics(JSON.parse(fs.readFileSync(candidatePath)),JSON.parse(fs.readFileSync(inputPath)),JSON.parse(knotsText));
 r.initial.parent={...r.initial.parent,inputPath,inputSHA256:hash(inputPath)};
 r.report.source={candidateSHA256:hash(candidatePath),inputSHA256:hash(inputPath),scriptSHA256:hash(__filename)};
 fs.mkdirSync(path.dirname(prefix),{recursive:true});fs.writeFileSync(initialPath,JSON.stringify(r.initial)+"\n");
 r.report.initialSHA256=hash(initialPath);fs.writeFileSync(reportPath,JSON.stringify(r.report,null,2)+"\n");
 process.stdout.write(JSON.stringify({event:"refined_initial",dimension:r.initial.z.length,
  metric:r.report.freshCompleteBaseline?.maxRelativeMetric,R2:r.report.freshCompleteBaseline?.squaredNorm,
  curvature:r.report.freshCompleteBaseline?.curvature?.maxCurvature,
  seconds:r.report.elapsedSeconds,initialSHA256:r.report.initialSHA256,
  reportSHA256:hash(reportPath),acceptedOptimizationStep:false})+"\n");
}

