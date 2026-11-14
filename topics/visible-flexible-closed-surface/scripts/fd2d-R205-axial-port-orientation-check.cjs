"use strict";
/* Direction and endpoint check for the R202/R205 D2 meridian consequence.
 * Numerical table only. The separate proof, not this binary64 table, states
 * the exact necessary condition. No full-body, F, J, or solver is run.
 */
function createR205AxialPortReport(candidate,state,modules) {
 const m=modules||{
  createR187:require("./fd2d-direct-position-tangent-lift-baseline-R187.cjs").createR187,
  createR196CubicSplines:require("./fd2d-cubic-spline-refinement-R196.cjs").createR196CubicSplines,
  createR191Algebra:require("./fd2d-position-curvature-chain-R191.cjs").createR191Algebra,
  createR205BentAnnulusReference:require("./fd2d-bent-annulus-reference-R205.cjs").createR205BentAnnulusReference,
  createR205MetricProvider:require("./fd2d-direct-position-bent-annulus-metric-R205.cjs").createR205MetricProvider,
  createR205CurvatureProvider:require("./fd2d-direct-position-bent-annulus-curvature-R205.cjs").createR205CurvatureProvider
 };
 const engine=m.createR187(),core=m.createR205MetricProvider(engine,candidate,state.options,m.createR196CubicSplines(),m.createR205BentAnnulusReference);
 const p=m.createR205CurvatureProvider(engine,core,state.curvatureOptions,m.createR191Algebra());
 const A=core.definition.centralA,B=core.definition.centralB,c=core.base.centralLength,S=core.base.end,
  Z=core.base.height+state.z[core.definition.stateLayout.cutHeight],a=4/5,C=9.5,r=1/C;
 const necessary=(dx,dz,theta)=>r*theta+Math.hypot(dx-r*(1-Math.cos(theta)),dz-r*Math.sin(theta));
 const central=[p.point(0,0,state.z),p.point(0,Math.PI/2,state.z)].map(v=>({u:v.u,X:v.jets.X,Xs:v.jets.Xs,Xu:v.jets.Xu}));
 const rows=[];
 for(const amplitude of [0,.25,1,1.2]){
  const tail=m.createR205BentAnnulusReference(engine,core.base,{amplitude,angles:state.options.angles,cacheLimit:0});
  const major=tail.tailPoint(a,0,Z),minor=tail.tailPoint(a,Math.PI/2,Z);
  const Couter=minor.jets.X[1],Houter=Z-minor.jets.X[2],theta=Math.PI/2-amplitude;
  const majorBound=necessary(A-a,Z-c,Math.PI/2),minorBound=necessary(B-Couter,Z-Houter-c,theta);
  rows.push({amplitude,major:{X:major.jets.X,Xs:major.jets.Xs,bound:majorBound,slack:S-c-majorBound},
   minor:{X:minor.jets.X,Xs:minor.jets.Xs,Couter,Houter,turn:theta,bound:minorBound,slack:S-c-minorBound}});
 }
 return {schema:"fd2d-R202-R205-axial-port-orientation-diagnostic-v1",stateIteration:state.iteration,
  actualFrozenAmplitude:state.options.bentAnnulus.amplitude,parameters:{A,B,c,S,cuffHeight:Z,outerRadius:a,guideCurvature:C},
  central,rows,majorCutDirectionIndependentOfTailAmplitude:true,
  majorBoundForFixed625:necessary(A-a,.625-c,Math.PI/2),
  lengthAvailableFinite:S-c,
  finiteBinary64Only:true,continuousCertificate:false,
  scope:"The D2 major axis is u=0, not pi/2. The exact R202 major-axis necessary bound is unchanged by R205 amplitude. The hypothetical curvature guide is not a bound on this actual accepted field.",
  doesNotApplyToGeneralNonReflectionFullHalfField:true};
}
if(typeof module!=="undefined"&&module.exports)module.exports={createR205AxialPortReport};
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module){
 const fs=require("node:fs"),[candidatePath,statePath,outputPath]=process.argv.slice(2);
 if(!candidatePath||!statePath||!outputPath)throw Error("Usage: candidate.json state.json fresh-report.json");
 if(fs.existsSync(outputPath))throw Error("Fresh output required");
 const report=createR205AxialPortReport(JSON.parse(fs.readFileSync(candidatePath)),JSON.parse(fs.readFileSync(statePath)));
 fs.writeFileSync(outputPath,JSON.stringify(report,null,2)+"\n");
}
