/* R196 real nonuniform radial branch, unchanged R195 Armijo policy.
 * Pure V8 and Node can supply the same explicit factories. No hidden restart,
 * parameter projection, trial reuse, discarded off-band entry or new gate.
 */
"use strict";
function createR196RefinedBranchRuntime(engine,bundle,factories){
  const sp=factories.splines;
  function providers(checkpoint){
    const metric=factories.metric(engine,bundle,checkpoint.options,sp);
    const curvature=factories.curvature(engine,metric,checkpoint.curvatureOptions,factories.algebra);
    const lm=factories.bandLM(factories.bandKernel,curvature.definition,{
      halfBandwidthBlocks:4,kernelSourceSHA256:"3484c99bfe0a5602c16eb5ccd70288326be04eeadc2804df4c7fd16639ece02c"});
    return{metric,curvature,lm};
  }
  function initialize(parent,insertedKnots,bindings){
    const J=parent.options.radialBasisCount,K=parent.options.modes,z=parent.z,cut=2*J*K+J;
    if(z.length!==2*J*K+2*J+1)throw Error("Explicit full radius-design layout required");
    const oldKnots=parent.options.radialKnots||sp.uniformKnots(J);
    const rows=Array.from({length:J},(_,j)=>[...z.slice(j*K,(j+1)*K),...z.slice(J*K+j*K,J*K+(j+1)*K),z[2*J*K+j],z[cut+1+j]]);
    const p=sp.prolongCoefficients(oldKnots,rows,insertedKnots),nj=p.new_count,r=p.coefficients_binary64,nz=[];
    for(let j=0;j<nj;j++)nz.push(...r[j].slice(0,K));
    for(let j=0;j<nj;j++)nz.push(...r[j].slice(K,2*K));
    for(let j=0;j<nj;j++)nz.push(r[j][2*K]);
    nz.push(z[cut]);for(let j=0;j<nj;j++)nz.push(r[j][2*K+1]);
    const curvatureOptions={...(parent.curvatureOptions||parent.guide)};
    if(curvatureOptions.guide!==9.5||curvatureOptions.weight!==.01||curvatureOptions.nodeShare!==.5)
      throw Error("This assigned branch retains guide9.5/weight.01/nodeShare.5");
    const c={schema:"fd2d-R196-actual-nonuniform-radial-branch-checkpoint-v1",bindings,
      options:{...parent.options,radialBasisCount:nj,radialKnots:p.new_knots},curvatureOptions,
      z:nz,lambda:parent.lambda,parentAcceptedIteration:parent.iteration,localAcceptedSteps:0,
      centralSeed:parent.centralSeed,history:[],parentLastFiniteEvaluation:parent.history?.slice(-1)[0]?.evaluation||null,
      injection:{oldCount:J,newCount:nj,insertedKnots,oldKnots,newKnots:p.new_knots,
        coefficientRounding:p.stored_spline_roundoff_bounds,cutHeightCopiedIdentically:nz[2*nj*K+nj]===z[cut],
        exactRealFieldPreservedBeforeRounding:true,binary64FieldBitwiseEqual:false,
        newQuadratureBaselineRequired:true},
      completePhysicalMetricFixedDuringDesign:false,continuousCertificate:false,strongTargetComplete:false,
      execution:{runtime:"pure JavaScript/V8",OS_subprocess_started:false,OS_exit_code:null}};
    const runtime=providers(c),t=Date.now(),v=runtime.curvature.value(c.z);
    c.newQuadratureBaseline=v;c.lastEvaluation=v;c.baselineMilliseconds=Date.now()-t;
    c.providerDefinition=runtime.curvature.definition;c.backendDefinition=runtime.lm.backendDefinition;
    c.status="injected_actual_fresh_quadrature_baseline";
    return c;
  }
  async function runBatch(checkpoint,requestedAcceptedSteps,onCheckpoint){
    if(!Number.isInteger(requestedAcceptedSteps)||requestedAcceptedSteps<1)throw Error("positive finite batch size required");
    let c=JSON.parse(JSON.stringify(checkpoint));const runtime=providers(c);
    for(let k=0;k<requestedAcceptedSteps;k++){
      const start=Date.now(),z=Float64Array.from(c.z),normalStart=Date.now();
      const normal=runtime.curvature.normal(z),normalMs=Date.now()-normalStart;
      normal.z=Float64Array.from(z);
      const step=await runtime.lm.lmStep({normal,z,lambda:c.lambda,value:q=>runtime.curvature.value(q)});
      const record={localIteration:c.localAcceptedSteps+1,accepted:step.accepted,status:step.status,
        baselineSquaredNorm:normal.squaredNorm,previousSavedValueSquaredNorm:c.lastEvaluation.squaredNorm,
        savedValueVersusFreshNormalDifference:normal.squaredNorm-c.lastEvaluation.squaredNorm,
        lambda:step.lambda,nextLambda:step.nextLambda,alpha:step.alpha??null,squaredNorm:step.squaredNorm,
        predictedReduction:step.predictedReduction??null,actualReduction:step.actualReduction??null,rho:step.rho??null,
        evaluation:step.evaluation||null,trace:step.trace,solveInfo:step.solveInfo||step.lastSolveInfo||step.normalInfo,
        actualValueEvaluations:step.actualValueEvaluations,normalMs,elapsedMs:Date.now()-start,
        backend:"R195 v2 explicit width4; original actual-value Armijo policy"};
      c.history.push(record);c.lambda=step.nextLambda;
      if(step.accepted){c.z=Array.from(step.z);c.localAcceptedSteps++;c.lastEvaluation=step.evaluation;c.status="actual_Armijo_accepted";}
      else c.status=step.status;
      c.execution.completed=true;
      if(onCheckpoint)await onCheckpoint(c,record);
      if(!step.accepted)break;
    }
    return c;
  }
  return{initialize,runBatch,providers};
}
if(typeof module!=="undefined"&&module.exports)module.exports={createR196RefinedBranchRuntime};
