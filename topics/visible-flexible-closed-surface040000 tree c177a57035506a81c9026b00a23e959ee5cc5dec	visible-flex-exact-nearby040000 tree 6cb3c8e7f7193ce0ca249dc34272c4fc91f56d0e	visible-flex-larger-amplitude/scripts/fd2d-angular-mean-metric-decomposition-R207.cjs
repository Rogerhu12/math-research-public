"use strict";
/* R207 diagnostic: the actual complete position field is not changed.
 * Means use fixed positive physical-angle weights, which may themselves define
 * the exact target when evaluated on the complete mathematical position field.
 * This binary64 report is not a continuous certificate. Mean nodes must freeze
 * with the design and must not change when the later objective is refined.
 */
function decomposeR207AngularMeans(position,engine,z,options={}) {
 const N=position.definition.fullEquivalentAngles,nq=N/2,S=position.base.end,
  cuts=position.radialCuts,G2=engine.gauss(2),rows=[];
 if(!Number.isInteger(nq)||nq<2||z.length!==position.dimension)throw Error("Explicit full-half layout required");
 const dot=(x,y)=>x.reduce((s,a,i)=>s+a*y[i],0);
 let original=0,centered=0,relative=0,meanEPart=0,meanFPart=0,varianceE=0,varianceF=0,
  arcLength=0,shear=0,minH=Infinity,minE=Infinity,maxE=-Infinity,maxAbsF=0,
  originalMaximum=0,newMaximum=0,originalWorst=null,newWorst=null,identityError=0;
 for(let i=1;i<cuts.length;i++)for(let g=0;g<G2.x.length;g++){
  const lo=cuts[i-1],width=cuts[i]-lo,s=lo+width*G2.x[g],wr=width*G2.w[g]/S,
   sl=position.slice(s,z,false),points=[];
  let e=0,f=0,oldCost=0,minEi=Infinity,maxEi=-Infinity,minTi=Infinity,maxTi=-Infinity,minImm=Infinity;
  for(let j=0;j<=nq;j++){
   const p=sl.node(j),V=p.jets.Xs,T=p.jets.Xu.map(x=>x/p.a),E=dot(V,V),t=dot(V,T),
    aw=(j===0||j===nq?.5:1)/nq;
   points.push({u:j*Math.PI/nq,E,t,aw,a:p.a});
   e+=aw*E;f+=aw*t;oldCost+=aw*((E-1)**2+2*t*t);
   minEi=Math.min(minEi,E);maxEi=Math.max(maxEi,E);minTi=Math.min(minTi,t);maxTi=Math.max(maxTi,t);minImm=Math.min(minImm,E-t*t);
   const oe=(E-1)/2,oldNorm=Math.abs(oe)+Math.hypot(oe,t);
   if(oldNorm>originalMaximum){originalMaximum=oldNorm;originalWorst={s,u:j*Math.PI/nq,E,t};}
  }
  const h=e-f*f;if(!(h>0&&Number.isFinite(h)))throw Error("Finite mean Gram determinant is not positive");
  let ve=0,vf=0,centerCost=0,newCost=0,rowMax=0;
  for(const p of points){
   const de=p.E-e,dt=p.t-f,rE=(de-2*f*dt)/h,rF=dt/Math.sqrt(h);
   ve+=p.aw*de*de;vf+=p.aw*dt*dt;
   centerCost+=p.aw*(de*de+2*dt*dt);newCost+=p.aw*(rE*rE+2*rF*rF);
   const q=rE/2,nn=Math.abs(q)+Math.hypot(q,rF);rowMax=Math.max(rowMax,nn);
   if(nn>newMaximum){newMaximum=nn;newWorst={s,u:p.u,E:p.E,t:p.t,e,f,h,rE,rF};}
  }
  const me=(e-1)**2,mf=2*f*f;
  identityError=Math.max(identityError,Math.abs(oldCost-centerCost-me-mf));
  original+=wr*oldCost;centered+=wr*centerCost;relative+=wr*newCost;
  meanEPart+=wr*me;meanFPart+=wr*mf;varianceE+=wr*ve;varianceF+=wr*2*vf;
  arcLength+=S*wr*Math.sqrt(h);shear+=S*wr*f/points[0].a;
  minH=Math.min(minH,h);minE=Math.min(minE,e);maxE=Math.max(maxE,e);maxAbsF=Math.max(maxAbsF,Math.abs(f));
  rows.push({s,radialWeight:wr,e,f,h,minimumE:minEi,maximumE:maxEi,minimumT:minTi,maximumT:maxTi,minimumImmersion:minImm,
    originalCost:oldCost,meanEContribution:me,meanFContribution:mf,varianceE:ve,twiceVarianceT:2*vf,
    centeredCost:centerCost,newRelativeCost:newCost,newRelativeMaximum:rowMax});
  if(options.onRadial&&rows.length%32===0)options.onRadial({completed:rows.length,s});
 }
 return {schema:"fd2d-R207-angular-mean-metric-decomposition-v1",dimension:position.dimension,N,radialPoints:rows.length,
  sameInputPositionField:true,wholeNormalComputed:false,newAcceptedStep:false,
  originalFiniteMetricSquaredNorm:original,centeredUnnormalizedSquaredNorm:centered,
  radialMeanEContribution:meanEPart,radialMeanFContribution:meanFPart,angularVarianceEContribution:varianceE,angularVarianceFContribution:varianceF,
  algebraicDecompositionAbsoluteError:Math.abs(original-centered-meanEPart-meanFPart),maximumSliceDecompositionError:identityError,
  explainedFraction:(meanEPart+meanFPart)/original,
  newRelativeFiniteMetricSquaredNorm:relative,originalMaximum,newRelativeMaximum:newMaximum,originalWorst,newWorst,
  targetMeans:{minimumE:minE,maximumE:maxE,maximumAbsF:maxAbsF,minimumH:minH},
  proposedCoordinates:{oldParameterLength:S,finiteOrthogonalArcLength:arcLength,finiteIntegratedShear:shear},
  rows,meansScope:"Fixed N/2+1 physical-angle positive trapezoid weights. This may define a new exact target from the complete field; this report only evaluates it numerically. Freeze mean nodes, weights, and reference state before later same-g refinement.",
  continuousCertificate:false,strongTargetComplete:false};
}
if(typeof module!=="undefined"&&module.exports)module.exports={decomposeR207AngularMeans};
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module){
 const fs=require("node:fs"),[candidatePath,statePath,outPath]=process.argv.slice(2);
 if(!candidatePath||!statePath||!outPath)throw Error("Usage: candidate.json state.json fresh-report.json");
 if(fs.existsSync(outPath))throw Error("Fresh output required");
 const state=JSON.parse(fs.readFileSync(statePath)),candidate=JSON.parse(fs.readFileSync(candidatePath)),
  engine=require("./fd2d-direct-position-tangent-lift-baseline-R187.cjs").createR187(),
  splines=require("./fd2d-cubic-spline-refinement-R196.cjs").createR196CubicSplines(),
  metric=require("./fd2d-nonuniform-metric-provider-R196.cjs").createR196MetricProvider(engine,candidate,state.options,splines),
  bent=require("./fd2d-bent-annulus-reference-R205.cjs").createR205BentAnnulusReference,
  algebra=require("./fd2d-position-curvature-chain-R191.cjs").createR191Algebra(),
  position=require("./fd2d-R201-R205-variable-amplitude-provider.cjs").createR201R205AmplitudeProvider(
   engine,metric,A=>bent(engine,metric.base,{amplitude:A,angles:state.options.angles}),state.curvatureOptions,algebra),
  report=decomposeR207AngularMeans(position,engine,state.z);
 fs.writeFileSync(outPath,JSON.stringify(report)+"\n");
}
