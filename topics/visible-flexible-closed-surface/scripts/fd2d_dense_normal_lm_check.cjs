"use strict";
function check(ok, message) { if (!ok) throw new Error(message); }
function maxDifference(a,b) { let x=0; for(let i=0;i<a.length;++i)x=Math.max(x,Math.abs(a[i]-b[i]));return x; }
function leastSquares(J,residual,z) {
  const n=J[0].length,H=new Float64Array(n*n),g=new Float64Array(n),diagonal=new Float64Array(n);
  let squaredNorm=0;
  for(let k=0;k<J.length;++k) { squaredNorm+=residual[k]*residual[k];for(let i=0;i<n;++i) {g[i]+=J[k][i]*residual[k];for(let j=0;j<n;++j)H[i*n+j]+=J[k][i]*J[k][j];}}
  for(let i=0;i<n;++i)diagonal[i]=H[i*n+i];
  return {H,g,diagonal,squaredNorm,z:new Float64Array(z)};
}
async function runChecks(api) {
  const start=Date.now(), rows=[];
  const J=[[1,2],[3,-1],[.1,4]],b=[1,-2,.5],z=new Float64Array([.4,-.2]);
  const value=x=>({squaredNorm:J.reduce((sum,row,k)=>sum+(row[0]*x[0]+row[1]*x[1]-b[k])**2,0)});
  const r=J.map((row,k)=>row[0]*z[0]+row[1]*z[1]-b[k]);
  const normal=leastSquares(J,r,z), original=JSON.stringify([Array.from(normal.H),Array.from(normal.g),Array.from(z)]);
  const lambda=.01,sol=api.solveDampedNormal(normal,{lambda});
  check(sol.ok,"full rank solve failed");
  const a=normal.H[0]*(1+lambda),c=normal.H[1],d=normal.H[3]*(1+lambda),det=a*d-c*c;
  const exact=[(-d*normal.g[0]+c*normal.g[1])/det,(c*normal.g[0]-a*normal.g[1])/det];
  const err=maxDifference(sol.direction,exact);
  check(err<1e-13,"two by two inverse comparison");
  let calls=0;
  const step=await api.lmStep({z,normal,lambda,value:async x=>{++calls;return value(x);}});
  check(step.accepted&&step.alpha===1&&calls===1,"actual full rank full step");
  check(JSON.stringify([Array.from(normal.H),Array.from(normal.g),Array.from(z)])===original,"input arrays changed");
  rows.push({name:"full_rank_2d_linear_least_squares",actualValueCalls:calls,actualAccepted:true,
    analyticDirectionMaximumError:err,baselineSquaredNorm:normal.squaredNorm,actualSquaredNorm:step.squaredNorm,
    originalScaledEquationResidualMaximum:sol.info.originalScaledEquationResidualMaximum,inputArraysUnchanged:true});

  const rosenNormal=x=>leastSquares([[-20*x[0],10],[-1,0]],[10*(x[1]-x[0]*x[0]),1-x[0]],x);
  let rosenCalls=0;
  const rosenValue=x=>{++rosenCalls;return {squaredNorm:100*(x[1]-x[0]*x[0])**2+(1-x[0])**2};};
  const rosen=await api.runLM({z:[-1.2,1],normal:rosenNormal,value:rosenValue,
    lambda:1e-4,maxIterations:80,squaredNormTolerance:1e-18,maxDampingAttempts:12});
  const accepted=rosen.history.filter(x=>x.accepted);
  let previous=24.2;
  for(const record of accepted) {
    check(record.squaredNorm<previous,"nonmonotone actual Rosenbrock acceptance");
    const trial=record.trace.find(x=>x.accepted);
    check(trial&&trial.actualValueEvaluated&&trial.actualCost<trial.armijoThreshold,"missing actual Armijo");
    previous=record.squaredNorm;
  }
  const actualTrials=rosen.history.flatMap(x=>x.trace).filter(x=>x.kind==="actual_trial");
  check(rosen.actualValueEvaluations===rosenCalls,"actual nonlinear call count mismatch");
  check(rosen.squaredNorm<1e-18&&maxDifference(rosen.z,[1,1])<2e-9,"Rosenbrock did not attain finite target");
  check(actualTrials.some(x=>!x.accepted),"fixture did not exercise an actual rejection");
  rows.push({name:"2d_Rosenbrock_nonlinear_least_squares",status:rosen.status,
    initialSquaredNorm:24.2,finalSquaredNorm:rosen.squaredNorm,finalZ:Array.from(rosen.z),
    acceptedSteps:rosen.acceptedSteps,actualValueCalls:rosenCalls,
    normalEvaluations:rosen.normalEvaluations,rejectedActualTrials:actualTrials.filter(x=>!x.accepted).length,
    acceptedAlphas:accepted.map(x=>x.alpha),acceptedSquaredNorms:accepted.map(x=>x.squaredNorm),
    everyAcceptedStepHasActualStrictArmijo:true});

  const zeroNormal={H:new Float64Array([1,0,0,0]),g:new Float64Array([1,0]),diagonal:[1,0],squaredNorm:1};
  const zero=await api.lmStep({z:[1,7],normal:zeroNormal,lambda:1e-3,value:x=>({squaredNorm:x[0]*x[0]})});
  check(zero.accepted&&zero.z[1]===7&&zero.solveInfo.zeroDiagonalColumns[0]===1,"exact unobserved coordinate handling");
  rows.push({name:"2d_one_exact_zero_column",actualSquaredNorm:zero.squaredNorm,unobservedCoordinate:zero.z[1],
    zeroDiagonalColumns:zero.solveInfo.zeroDiagonalColumns,hiddenShift:zero.solveInfo.hiddenDiagonalShift});

  const rankNormal={H:[[1,1],[1,1]],g:[2,2],diagonal:[1,1],squaredNorm:4};
  const rank=await api.lmStep({z:[1,1],normal:rankNormal,lambda:1e-6,value:x=>({squaredNorm:(x[0]+x[1])**2})});
  check(rank.accepted&&rank.squaredNorm<1e-10,"rank deficient actual LS did not decrease");
  rows.push({name:"2d_exact_rank_one_normal",actualSquaredNorm:rank.squaredNorm,
    lambda:rank.lambda,scaledEquationResidual:rank.solveInfo.originalScaledEquationResidualMaximum,
    hiddenShift:rank.solveInfo.hiddenDiagonalShift});

  // This deliberate roundoff-size indefiniteness is a factorization stress
  // diagnostic, not an assertion that the perturbed matrix is exactly J^T J.
  const e=4*Number.EPSILON;
  const perturbed={H:[[1,1+e],[1+e,1]],g:[2,2],diagonal:[1,1],squaredNorm:4};
  const pert=await api.lmStep({z:[1,1],normal:perturbed,lambda:1e-18,lambdaMin:1e-18,
    maxDampingAttempts:12,value:x=>({squaredNorm:(x[0]+x[1])**2})});
  check(pert.accepted&&pert.trace.some(x=>x.kind==="factorization_rejected"),"explicit damping recovery was not exercised");
  rows.push({name:"2d_roundoff_perturbed_rank_one_factorization_stress",notExactJtJ:true,
    offDiagonalPerturbation:e,actualSquaredNorm:pert.squaredNorm,initialLambda:1e-18,acceptedLambda:pert.lambda,
    rejectedFactors:pert.trace.filter(x=>x.kind==="factorization_rejected").map(x=>({lambda:x.lambda,pivot:x.pivot})),
    hiddenShift:pert.solveInfo.hiddenDiagonalShift,actualAcceptance:true});

  const invalid=await api.lmStep({z:[1,0],normal:{H:[[1,0],[0,1]],g:[1,0],squaredNorm:1},
    lambda:1e-3,maxDampingAttempts:1,value:()=>({squaredNorm:0,valid:false})});
  check(!invalid.accepted&&invalid.actualValueEvaluations===3,"explicit invalid trials must not be accepted");
  rows.push({name:"invalid_actual_values_rejected",accepted:invalid.accepted,actualValueCalls:invalid.actualValueEvaluations,
    triedAlphas:invalid.trace.filter(x=>x.kind==="actual_trial").map(x=>x.alpha)});
  return {schema:"fd2d-dense-normal-lm-finite-v8-fixture-v1",passed:true,
    execution:"actual JavaScript execution",elapsedMilliseconds:Date.now()-start,
    maximumDimension:2,fixtures:rows,continuousGeometryCertificate:false,OSProcessCreated:false};
}
module.exports={runChecks,leastSquares};
if(typeof require==="function"&&require.main===module) {
  runChecks(require("./fd2d_dense_normal_lm.cjs")).then(x=>process.stdout.write(JSON.stringify(x,null,2)+"\n"))
    .catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
}
