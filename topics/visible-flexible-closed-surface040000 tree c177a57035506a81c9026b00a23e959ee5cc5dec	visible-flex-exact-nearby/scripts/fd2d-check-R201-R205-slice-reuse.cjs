"use strict";
async function runSliceReuseCheck(req,candidate,onProgress=()=>{}){
 const spl=req("fd2d-cubic-spline-refinement-R196.cjs").createR196CubicSplines();
 const options={radialBasisCount:3,radialKnots:spl.uniformKnots(3),modes:2,angles:32,gap:.8,radiusCoefficientBound:.4};
 const curvatureOptions={guide:9.5,weight:.01,nodeShare:.5};
 const geometryOptions={radius:1.59,width:.84,held:.65,weight:10,nodeShare:.5,cutWindow:[.41,.62]};
 function create(name,extra={}){
   const engine=req("fd2d-direct-position-tangent-lift-baseline-R187.cjs").createR187();
   const metric=req("fd2d-nonuniform-metric-provider-R196.cjs").createR196MetricProvider(engine,candidate,options,spl);
   const algebra=req("fd2d-position-curvature-chain-R191.cjs").createR191Algebra();
   const referenceFactory=A=>req("fd2d-bent-annulus-reference-R205.cjs").createR205BentAnnulusReference(engine,metric.base,{amplitude:A,angles:options.angles});
   const position=req(name).createR201R205AmplitudeProvider(engine,metric,referenceFactory,{...curvatureOptions,...extra},algebra);
   const provider=req("fd2d-R201-R205-variable-amplitude-geometric-guide.cjs").createR201R205AmplitudeGeometryProvider(position,geometryOptions);
   return {metric,position,provider};
 }
 const old=create("fd2d-R201-R205-variable-amplitude-provider.cjs");
 const now=create("fd2d-R201-R205-variable-amplitude-slice-reuse.cjs");
 const n=old.provider.dimension,z=Float64Array.from({length:n},(_,i)=>.0003*Math.sin((i+1)*.71));
 z[old.metric.definition.stateLayout.cutHeight]=.56-old.metric.base.height;z[old.position.amplitudeIndex]=.25;
 const direction=Float64Array.from({length:n},(_,i)=>.1*Math.cos((i+1)*.37));
 const config={jacobian:true,residuals:true,direction},start=Date.now();
 let comparedScalars=0;
 function identical(a,b,path){
   if(typeof a==="number"||typeof b==="number"){comparedScalars++;if(!Object.is(a,b))throw Error("Numerical mismatch "+path+": "+a+" / "+b);return;}
   if(a===null||b===null||typeof a!=="object"||typeof b!=="object"){if(a!==b)throw Error("Metadata mismatch "+path);return;}
   const ka=Object.keys(a),kb=Object.keys(b);if(ka.join("\0")!==kb.join("\0"))throw Error("Key mismatch "+path);
   for(const k of ka)identical(a[k],b[k],path+"."+k);
 }
 const a0=Date.now(),a=old.provider.evaluate(z,config),uncachedSeconds=(Date.now()-a0)/1000;
 await onProgress({stage:"uncached_complete_normal",seconds:uncachedSeconds,dimension:n,rows:a.rowCount});
 const b0=Date.now(),b=now.provider.evaluate(z,config),cachedSeconds=(Date.now()-b0)/1000;
 identical(a,b,"completeNormal");
 const normalStats=now.position.sliceReuseStats();
 if(!(normalStats.hits>0&&normalStats.builds===normalStats.calls-normalStats.hits))throw Error("No actual reuse");
 await onProgress({stage:"exact_complete_normal_compared",scalars:comparedScalars,stats:normalStats,seconds:cachedSeconds});
 const s=old.metric.base.centralLength+.59*(old.metric.base.end-old.metric.base.centralLength),u=.847;
 const baseline=Array.from(z),changes=[
   ["legacy_theta",0,1e-6],
   ["new_theta_constant",old.metric.dimension,1e-6],
   ["radius",old.metric.definition.stateLayout.rho?.[0]??(2*options.radialBasisCount*options.modes+options.radialBasisCount+1),1e-6],
   ["cut_height",old.metric.definition.stateLayout.cutHeight,1e-6],
   ["amplitude",old.position.amplitudeIndex,1e-6]
 ];
 const invalidations=[];
 for(const [name,index,increment] of changes){
   const q=Array.from(baseline);q[index]+=increment;
   const before=now.position.sliceReuseStats();
   identical(old.position.point(s,u,q,{jacobian:true}),now.position.point(s,u,q,{jacobian:true}),"changed."+name);
   const after=now.position.sliceReuseStats();
   if(after.invalidations!==before.invalidations+1)throw Error("Changed full parameter was not invalidated: "+name);
   invalidations.push({name,index,increment,before:before.invalidations,after:after.invalidations});
 }
 const shared=now.position.slice(s,z,true);shared.node=()=>{throw Error("External wrapper mutation");};
 identical(old.position.point(s,u,z,{jacobian:true}),now.position.point(s,u,z,{jacobian:true}),"fresh_public_wrapper");
 const p=now.position.point(s,u,z,{jacobian:true});p.jets.X[0]=1e99;p.parameterJets[0].X[0]=-1e99;
 identical(old.position.point(s,u,z,{jacobian:true}),now.position.point(s,u,z,{jacobian:true}),"fresh_node_packet");
 const limited=create("fd2d-R201-R205-variable-amplitude-slice-reuse.cjs",{sliceReuse:{valueLimit:2,derivativeLimit:1}});
 for(const t of [.21,.42,.63])for(const d of [false,true]){
   const ss=old.metric.base.centralLength+t*(old.metric.base.end-old.metric.base.centralLength);
   identical(old.position.slice(ss,z,d).point(u),limited.position.slice(ss,z,d).point(u),"limited."+t+"."+d);
 }
 const limitedStats=limited.position.sliceReuseStats();if(limitedStats.valueEntries!==2||limitedStats.derivativeEntries!==1)throw Error("Entry limit failed");
 return {schema:"fd2d-complete-amplitude-exact-slice-reuse-check-v1",runtime:"actual pure V8; no OS subprocess or exit code",
  options,curvatureOptions,geometryOptions,dimension:n,z:Array.from(z),direction:Array.from(direction),
  sourceParentSHA256:"eccfb354b52ef49a65e9b4ff74a6d9c3023bbf4fde839184845c2b5dab91ad3b",
  rowCount:a.rowCount,squaredNorm:a.squaredNorm,
  scalarComparisons:comparedScalars,allNumbersComparedByObjectIs:true,fullHGradientDiagonalResidualAndJVPCompared:true,
  normalStats,invalidations,limitedStats,publicWrapperAndPacketMutationDoesNotPoisonReuse:true,
  actualTiming:{uncachedSeconds,cachedSeconds,totalSeconds:(Date.now()-start)/1000,causalSpeedupClaimed:false},
  physicalDefinitionChanged:false,approximationIntroduced:false,continuousCertificate:false,strongTargetComplete:false};
}
module.exports={runSliceReuseCheck};
if(require.main===module){
 const fs=require("node:fs"),[candidatePath,reportPath]=process.argv.slice(2);
 if(!candidatePath||!reportPath||fs.existsSync(reportPath))throw Error("Existing candidate and fresh report required");
 runSliceReuseCheck(name=>require("./"+name),JSON.parse(fs.readFileSync(candidatePath,"utf8")))
 .then(report=>{report.runtime="Actual Node invocation; exit belongs to external receipt";fs.writeFileSync(reportPath,JSON.stringify(report,null,2)+"\n");process.stdout.write(JSON.stringify(report.actualTiming)+"\n");})
 .catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
}
