"use strict";
function createR208Physical(req,candidate,input){
 const e=req("fd2d-direct-position-tangent-lift-baseline-R187.cjs").createR187();
 const b=req("fd2d-cubic-spline-refinement-R196.cjs").createR196CubicSplines();
 const m=req("fd2d-nonuniform-metric-provider-R196.cjs").createR196MetricProvider(e,candidate,input.options,b);
 const ref=A=>req("fd2d-bent-annulus-reference-R205.cjs").createR205BentAnnulusReference(e,m.base,{amplitude:A,angles:input.options.angles});
 const p=req("fd2d-R201-R205-variable-amplitude-slice-reuse.cjs").createR201R205AmplitudeProvider(e,m,ref,input.curvatureOptions,req("fd2d-position-curvature-chain-R191.cjs").createR191Algebra());
 return {metric:m,position:p};
}
function runR208PhysicalCheck(req,candidate,input,knots){
 const start=Date.now(),r=req("fd2d-R201-R205-complete-radial-prolongation.cjs").prolongR201R205State(input,knots);
 const old=createR208Physical(req,candidate,input),now=createR208Physical(req,candidate,{options:r.options,curvatureOptions:input.curvatureOptions});
 const c=old.metric.base.centralLength,S=old.metric.base.end,L=S-c;
 if(c!==now.metric.base.centralLength||S!==now.metric.base.end||old.metric.curve.A!==now.metric.curve.A||old.metric.curve.B!==now.metric.curve.B)
  throw Error("Original physical background/central curve changed");
 const qs=[0,1/60,1/20,.0574800692123,7/30,.362487251824,7/20,.407044162180,5/12,.77,1];
 const ss=[0,c,...qs.filter(q=>q>0&&q<1).map(q=>c+L*q),S],us=[0,.37,Math.PI/2,2.1,Math.PI,4.7];
 const keys=["X","Xs","Xu","Xss","Xsu","Xuu"],max=Object.fromEntries(keys.map(k=>[k,0])),witness={},scalars={a:0,C:0,S:0,R:0};
 let points=0,comparisons=0;
 for(const s of ss){
  const a=old.position.slice(s,input.z,false),b=now.position.slice(s,r.z,false);
  for(const u of us){
   const x=a.point(u),y=b.point(u);points++;
   for(const k of keys)for(let j=0;j<3;j++){
    const d=Math.abs(x.jets[k][j]-y.jets[k][j]);comparisons++;
    if(d>max[k]){max[k]=d;witness[k]={s,u,coordinate:j,before:x.jets[k][j],after:y.jets[k][j]};}
   }
   scalars.a=Math.max(scalars.a,Math.abs(x.a-y.a));
   for(const k of ["C","S","R"])scalars[k]=Math.max(scalars[k],Math.abs(x.phase[k]-y.phase[k]));
  }
 }
 if(Math.max(...Object.values(max))>5e-9||Math.max(...Object.values(scalars))>1e-10)throw Error("Actual complete physical prolongation failed "+JSON.stringify({max,scalars,witness}));
 const globalChecks={cut:Object.is(input.z[input.cutHeightIndex],r.z[r.cutHeightIndex]),A:Object.is(input.z[input.amplitudeIndex],r.z[r.amplitudeIndex])};
 if(!globalChecks.cut||!globalChecks.A)throw Error("Global coordinate changed");
 return {schema:"fd2d-R208-full-half-actual-prolongation-physical-check-v1",
  runtime:"actual pure V8; no OS child or exit",oldDimension:old.position.dimension,newDimension:now.position.dimension,
  actualDefinitionMatchesNewDimension:now.position.dimension===r.newDimension,insertedKnots:r.insertedKnots,
  inputStatePassedWithoutTruncation:true,points,vectorScalarComparisons:comparisons,
  physicalSpan:{c,S,L},angles:us,normalizedRadialValues:qs,maximumAbsoluteJetDifferences:max,maximumScalarDifferences:scalars,witnesses:witness,globalChecks,
  oldStoredMetricDefinition:old.position.definition.parentMetric,newStoredMetricDefinition:now.position.definition.parentMetric,
  prolongation:r,executionSeconds:(Date.now()-start)/1000,
  actualLMNormalOrStepComputed:false,fieldTestIsNotContinuousRoundoffCertificate:true,continuousCertificate:false,strongTargetComplete:false};
}

function runR208DirectionCheck(req,candidate,input,knots){
 const start=Date.now(),prolong=req("fd2d-R201-R205-complete-radial-prolongation.cjs").prolongR201R205State;
 const actual=prolong(input,knots),direction=Array.from(input.z,(_,i)=>.002*Math.cos((i+1)*.37));
 const mapped=prolong({...input,z:direction},knots).z;
 const old=createR208Physical(req,candidate,input),now=createR208Physical(req,candidate,{options:actual.options,curvatureOptions:input.curvatureOptions});
 const c=old.metric.base.centralLength,L=old.metric.base.end-c,keys=["X","Xs","Xu","Xss","Xsu","Xuu"];
 const maximum=Object.fromEntries(keys.map(k=>[k,0]));let scalarComparisons=0;
 for(const q of [.355,.412])for(const u of [.43,2.17]){
  const s=c+L*q,x=old.position.point(s,u,input.z,{jacobian:true}),y=now.position.point(s,u,actual.z,{jacobian:true});
  for(const key of keys)for(let k=0;k<3;k++){
   let a=0,b=0;
   for(let j=0;j<x.indices.length;j++)a+=x.parameterJets[j][key][k]*direction[x.indices[j]];
   for(let j=0;j<y.indices.length;j++)b+=y.parameterJets[j][key][k]*mapped[y.indices[j]];
   maximum[key]=Math.max(maximum[key],Math.abs(a-b));scalarComparisons++;
  }
 }
 if(Math.max(...Object.values(maximum))>1e-9)throw Error("Complete mapped JVP mismatch "+JSON.stringify(maximum));
 return {allOldColumnsIncluded:true,newDirectionUsesCompleteBoehmMap:true,globalCutAndAmplitudeDirectionsIncluded:true,
  actualPoints:4,scalarComparisons,maximumAbsoluteJetJVPDifferences:maximum,seconds:(Date.now()-start)/1000,
  finiteRoundingCompared:true,largeNormalConstructed:false};
}

module.exports={runR208PhysicalCheck,runR208DirectionCheck,createR208Physical};
if(require.main===module){
 const fs=require("node:fs"),[candidatePath,inputPath,knotsJSON,reportPath]=process.argv.slice(2);
 if(!candidatePath||!inputPath||!knotsJSON||!reportPath||fs.existsSync(reportPath))throw Error("candidate input knotsJSON fresh-report required");
 const r=runR208PhysicalCheck(name=>require("./"+name),JSON.parse(fs.readFileSync(candidatePath,"utf8")),JSON.parse(fs.readFileSync(inputPath,"utf8")),JSON.parse(knotsJSON));
 r.mappedDirectionCheck=runR208DirectionCheck(name=>require("./"+name),JSON.parse(fs.readFileSync(candidatePath,"utf8")),JSON.parse(fs.readFileSync(inputPath,"utf8")),JSON.parse(knotsJSON));
 r.runtime="Actual Node invocation; exit belongs to external receipt";
 fs.writeFileSync(reportPath,JSON.stringify(r,null,2)+"\n");process.stdout.write(JSON.stringify({points:r.points,max:r.maximumAbsoluteJetDifferences})+"\n");
}
