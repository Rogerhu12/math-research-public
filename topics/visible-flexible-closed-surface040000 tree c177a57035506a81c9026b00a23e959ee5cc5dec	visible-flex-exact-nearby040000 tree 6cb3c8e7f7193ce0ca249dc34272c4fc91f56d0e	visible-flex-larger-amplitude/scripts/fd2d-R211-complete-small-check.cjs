"use strict";
/* Replays only the 18 spectral cases and one complete 30-dimensional field; no LM. */
function runR211SpectralCheck(original,amplified){
  const C=9.5,rows=[];
  const cases=[
    {name:"inactive_distinct",eig:[3,-2],angle:.31},
    {name:"inactive_repeated",eig:[2,2],angle:0},
    {name:"positive_active_distinct",eig:[14,11],angle:.47},
    {name:"positive_active_repeated",eig:[12,12],angle:0},
    {name:"negative_active_distinct",eig:[-12,-17],angle:.29},
    {name:"negative_active_repeated",eig:[-13,-13],angle:0},
    {name:"positive_and_inactive",eig:[15,4],angle:.43},
    {name:"negative_and_inactive",eig:[2,-14],angle:.61},
    {name:"opposite_active",eig:[16,-13],angle:.37},
    {name:"positive_threshold_inactive",eig:[C,2],angle:0,threshold:true},
    {name:"negative_threshold_inactive",eig:[2,-C],angle:0,threshold:true},
    {name:"positive_threshold_repeated",eig:[C,C],angle:0,threshold:true},
    {name:"negative_threshold_repeated",eig:[-C,-C],angle:0,threshold:true},
    {name:"opposite_thresholds",eig:[C,-C],angle:0,threshold:true},
    {name:"positive_active_and_threshold",eig:[13,C],angle:0,threshold:true},
    {name:"negative_active_and_threshold",eig:[-C,-13],angle:0,threshold:true},
    {name:"positive_threshold_opposite_active",eig:[C,-13],angle:0,threshold:true},
    {name:"positive_active_opposite_threshold",eig:[13,-C],angle:0,threshold:true}
  ];
  const directions=[[.31,-.27,.19],[-.23,.14,.37],[.13,.29,-.17]];
  const maxAbs=a=>Math.max(...a.map(Math.abs)),scaled=(a,b)=>maxAbs(a.map((x,i)=>x-b[i]))/Math.max(1,maxAbs(a),maxAbs(b));
  for(const x of cases){
    const c=Math.cos(x.angle),s=Math.sin(x.angle),[p,m]=x.eig;
    const S=[p*c*c+m*s*s,(p-m)*c*s,p*s*s+m*c*c];
    const b=original.hinge(S,C),v=amplified.hinge(S,C),q=b.squared,h=Math.sqrt(1+q/4);
    let fdMaximum=0,chainMaximum=0;
    for(const H of directions){
      const db=b.apply(H),target=db.map((w,i)=>h*w+b.residual[i]*b.residual.reduce((a,r,k)=>a+r*db[k],0)/(4*h));
      chainMaximum=Math.max(chainMaximum,scaled(v.apply(H),target));
      if(!x.threshold){
        const eps=1e-6,plus=amplified.hinge(S.map((w,i)=>w+eps*H[i]),C),minus=amplified.hinge(S.map((w,i)=>w-eps*H[i]),C);
        fdMaximum=Math.max(fdMaximum,scaled(v.apply(H),plus.residual.map((w,i)=>(w-minus.residual[i])/(2*eps))));
      }
    }
    const squareFromRows=v.residual.reduce((a,x)=>a+x*x,0),goal=q+q*q/4;
    const sqScaled=Math.abs(v.squared-squareFromRows)/Math.max(1,v.squared,squareFromRows);
    const thresholdPreserved=v.threshold===b.threshold&&v.threshold===!!x.threshold&&v.threshold_derivative_convention===b.threshold_derivative_convention;
    const zeroSet=(v.squared===0)===(b.squared===0);
    const repeatedThreshold=(x.name==="positive_threshold_repeated"||x.name==="negative_threshold_repeated");
    const zeroGeneralized=repeatedThreshold?directions.every(H=>v.apply(H).every(w=>w===0)):null;
    rows.push({name:x.name,S,eigenvalues:v.eigenvalues,originalSquared:q,amplifiedSquared:v.squared,
      scalarObjectiveDifference:v.squared-goal,residualSquareRelativeDifference:sqScaled,
      chainMaximumScaled:chainMaximum,centeredFDMaximumScaled:x.threshold?null:fdMaximum,
      thresholdPreserved,zeroSetPreserved:zeroSet,repeatedThresholdZeroDerivative:zeroGeneralized,
      thresholdFDPolicy:x.threshold?"No false centered smooth derivative test; original inactive slope zero and exact composition checked.":"Centered finite difference away from guide.",
      passed:sqScaled<2e-14&&chainMaximum<64*Number.EPSILON&&(!x.threshold?fdMaximum<1e-7:true)&&thresholdPreserved&&zeroSet&&zeroGeneralized!==false});
  }
  return {schema:"fd2d-R211-spectral-branch-check-v1",guide:C,tau:2,cases:rows,
    unchangedCurvatureFunction:amplified.curvature===original.curvature,
    unchangedVariationFunction:amplified.variation===original.variation,
    passed:rows.every(x=>x.passed)&&amplified.curvature===original.curvature&&amplified.variation===original.variation};
}

function runR211SmallFieldCheck(deps,bundle,observe=()=>{}){
  const engine=deps.createR187(),splines=deps.createR196CubicSplines();
  const settings={radialBasisCount:4,modes:1,angles:16,gap:.8,radiusCoefficientBound:.4,radialKnots:splines.uniformKnots(4)};
  const curvatureOptions={guide:9.5,weight:.01,nodeShare:.5};
  const md=deps.createR196MetricProvider(engine,bundle,settings,splines);
  const baseAlg=deps.createR191Algebra(),ampAlg=deps.createR211AmplifiedCurvatureAlgebra(baseAlg,{tau:2});
  const referenceFactory=A=>deps.createR205BentAnnulusReference(engine,md.base,{amplitude:A,angles:settings.angles});
  const p=deps.createR201R205AmplitudeProvider(engine,md,referenceFactory,curvatureOptions,ampAlg);
  const old=deps.createR201R205AmplitudeProvider(engine,md,referenceFactory,curvatureOptions,baseAlg);
  const n=p.dimension,J=settings.radialBasisCount,K=settings.modes,z=p.initialVector();
  const L=p.definition.stateLayout,cut=L.legacy.cutHeight,ai=p.amplitudeIndex;
  for(let j=0;j<J;j++){
    z[j*K]=.004*Math.sin(.7+j);
    z[J*K+j*K]=.003*Math.cos(.3+1.1*j);
    z[L.legacy.height[0]+j]=.004*Math.sin(.5+.9*j);
    z[L.legacy.radius[0]+j]=.003*Math.cos(.2+1.3*j);
    const e=L.appended.start+j*L.appended.widthPerRadial;
    z[e]=.002*Math.sin(.4+j);z[e+1]=.003*Math.cos(.6+j);z[e+2]=.004*Math.sin(.8+j);
  }
  z[cut]=-.12;z[ai]=.25;
  const d=Float64Array.from({length:n},(_,i)=>Math.sin(.43+.79*i));
  d[cut]=.7;d[ai]=-.9;
  const dn=Math.sqrt(d.reduce((a,x)=>a+x*x,0));for(let i=0;i<n;i++)d[i]/=dn;
  const dA=new Float64Array(n);dA[ai]=1;
  const input={settings,curvatureOptions,dimension:n,z:Array.from(z),mixedDirection:Array.from(d),amplitudeDirection:Array.from(dA),cutHeightIndex:cut,amplitudeIndex:ai,
    providerDefinition:{...p.definition,curvatureResidualDefinition:ampAlg.definition},
    claim:"A newly specified complete small R201+R205 numerical field, not an accepted production state or a solved surface."};
  observe("input",input);
  const normalStart=Date.now(),a=p.evaluate(z,{jacobian:true,residuals:true,direction:d});
  observe("normal",{seconds:(Date.now()-normalStart)/1000,dimension:n,rowCount:a.rowCount,squaredNorm:a.squaredNorm,maxCurvature:a.curvature.maxCurvature,activePoints:a.curvature.activePoints,
    H:Array.from(a.H),g:Array.from(a.g),diagonal:Array.from(a.diagonal)});
  if(!a.curvature.activePoints)throw Error("Fixture must exercise actual nonzero curvature rows");
  const aa=p.evaluate(z,{direction:dA,residuals:true});
  const eps=5e-7,plus=p.evaluate(Float64Array.from(z,(v,i)=>v+eps*d[i]),{residuals:true}),
    minus=p.evaluate(Float64Array.from(z,(v,i)=>v-eps*d[i]),{residuals:true});
  const dot=(a,b)=>{let s=0;for(let i=0;i<a.length;i++)s+=a[i]*b[i];return s;};
  const norm=v=>Math.sqrt(dot(v,v));
  const mv=v=>Float64Array.from({length:n},(_,i)=>{let s=0;for(let j=0;j<n;j++)s+=a.H[i*n+j]*v[j];return s;});
  const hd=mv(d),ha=mv(dA),fd=Float64Array.from(plus.residuals,(x,i)=>(x-minus.residuals[i])/(2*eps));
  const err=Float64Array.from(fd,(x,i)=>x-a.jvp[i]);
  const rel=(x,y)=>Math.abs(x-y)/Math.max(1,Math.abs(x),Math.abs(y));
  const identities={
    residualSquaredRelative:rel(a.squaredNorm,dot(a.residuals,a.residuals)),
    mixedHessianRelative:rel(dot(d,hd),dot(a.jvp,a.jvp)),
    amplitudeHessianRelative:rel(dot(dA,ha),dot(aa.jvp,aa.jvp)),
    mixedAmplitudeCrossRelative:rel(dot(dA,hd),dot(aa.jvp,a.jvp)),
    mixedGradientRelative:rel(dot(d,a.g),dot(a.residuals,a.jvp)),
    amplitudeGradientRelative:rel(a.g[ai],dot(a.residuals,aa.jvp)),
    FDObjectiveGradientRelative:rel((plus.squaredNorm-minus.squaredNorm)/(4*eps),dot(d,a.g)),
    mixedJVPRelativeL2:norm(err)/Math.max(1,norm(fd),norm(a.jvp)),
    mixedJVPMaximumScaled:Math.max(...Array.from(err,Math.abs))/Math.max(1,...Array.from(fd,Math.abs),...Array.from(a.jvp,Math.abs))
  };
  let sym=0,diag=0;for(let i=0;i<n;i++){diag=Math.max(diag,Math.abs(a.H[i*n+i]-a.diagonal[i]));for(let j=0;j<n;j++)sym=Math.max(sym,Math.abs(a.H[i*n+j]-a.H[j*n+i]));}
  identities.HSymmetryMaximum=sym;identities.diagonalMaximum=diag;
  const worst=a.curvature.worst,s=worst.s,u=worst.u,
    pt=p.point(s,u,z,{jacobian:true}),op=old.point(s,u,z,{jacobian:true});
  let jetDiff=0,variationDiff=0,phaseDiff=0;
  for(const key of["X","Xs","Xu","Xss","Xsu","Xuu"])for(let k=0;k<3;k++){
    jetDiff=Math.max(jetDiff,Math.abs(pt.jets[key][k]-op.jets[key][k]));
    for(let j=0;j<pt.parameterJets.length;j++)variationDiff=Math.max(variationDiff,Math.abs(pt.parameterJets[j][key][k]-op.parameterJets[j][key][k]));
  }
  for(const key of["C","S","R"])phaseDiff=Math.max(phaseDiff,Math.abs(pt.phase[key]-op.phase[key]));
  const indexA=pt.indices.indexOf(ai),indexCut=pt.indices.indexOf(cut);
  const jetColumnNorm=i=>i<0?null:Math.sqrt(Object.values(pt.parameterJets[i]).reduce((a,v)=>a+dot(v,v),0));
  const unchanged={actualPositionTwojetMaximum:jetDiff,allParameterTwojetMaximum:variationDiff,meanPhaseMaximum:phaseDiff,
    sameIndices:JSON.stringify(pt.indices)===JSON.stringify(op.indices),
    sameActualEigenvalues:JSON.stringify(pt.principalCurvatures)===JSON.stringify(op.principalCurvatures),
    completeBetaAndAmplitudeChainFromOriginalProvider:true,amplitudeIndexPresent:indexA>=0,cutIndexPresent:indexCut>=0,
    amplitudeColumnJetNorm:jetColumnNorm(indexA),cutColumnJetNorm:jetColumnNorm(indexCut),at:{s,u,phase:pt.phase,actualCurvature:pt.curvature}};
  const exactGlobalChecks=jetDiff===0&&variationDiff===0&&phaseDiff===0&&unchanged.sameIndices&&unchanged.sameActualEigenvalues&&indexA>=0&&indexCut>=0;
  const normalChecks=identities.residualSquaredRelative<2e-12&&identities.mixedHessianRelative<2e-12&&identities.amplitudeHessianRelative<2e-12&&
    identities.mixedAmplitudeCrossRelative<2e-12&&identities.mixedGradientRelative<2e-12&&identities.amplitudeGradientRelative<2e-12&&sym===0&&diag===0;
  const derivativeChecks=identities.mixedJVPRelativeL2<2e-5&&identities.mixedJVPMaximumScaled<2e-5&&identities.FDObjectiveGradientRelative<2e-5;
  return {schema:"fd2d-R211-complete-small-amplitude-field-check-v1",passed:exactGlobalChecks&&normalChecks&&derivativeChecks,input,
    numericalScope:"Complete finite half-period primitive and full actual Gram curvature at every original small-provider row; quadrature remains finite.",
    normal:{dimension:n,rowCount:a.rowCount,squaredNorm:a.squaredNorm,metricSquaredNorm:a.metricSquaredNorm,amplifiedCurvatureSquaredNorm:a.curvaturePenaltySquaredNorm,
      maxCurvature:a.curvature.maxCurvature,activePoints:a.curvature.activePoints,thresholdPoints:a.curvature.thresholdPoints,
      maxRelativeMetric:a.maxRelativeMetric,minImmersion:a.minImmersion,minMeanR:a.minMeanR,H:Array.from(a.H),g:Array.from(a.g),diagonal:Array.from(a.diagonal)},
    identities,unchanged,finiteDifference:{step:eps,scheme:"Centered mixed direction, including all radial channels plus both actual global columns",directionNorm:dn/dn,
      residualRows:a.residuals.length,mixedJVPNorm:norm(a.jvp),amplitudeOnlyJVPNorm:norm(aa.jvp)},
    noOptimizationStep:true,noLargeNormal:true,noContinuousMetricCurvatureReachCertificate:true};
}


function runR211CompleteCheck(deps,bundle,observe){
  const old=deps.createR191Algebra(),fresh=deps.createR211AmplifiedCurvatureAlgebra(old,{tau:2});
  const spectral=runR211SpectralCheck(old,fresh);
  const field=runR211SmallFieldCheck(deps,bundle,observe);
  return {schema:"fd2d-R211-reproducible-complete-small-check-v1",passed:spectral.passed&&field.passed,spectral,field};
}
if(typeof module!=="undefined"&&module.exports){
  module.exports={runR211SpectralCheck,runR211SmallFieldCheck,runR211CompleteCheck};
  if(typeof require==="function"&&require.main===module){
    const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
    const [candidatePath,output]=process.argv.slice(2);
    if(!candidatePath||!output)throw Error("Usage: node fd2d-R211-complete-small-check.cjs candidate.json fresh-report.json");
    if(fs.existsSync(output))throw Error("Output must be a new path");
    const dependencies=[
      ["fd2d-direct-position-tangent-lift-baseline-R187.cjs","createR187"],
      ["fd2d-cubic-spline-refinement-R196.cjs","createR196CubicSplines"],
      ["fd2d-nonuniform-metric-provider-R196.cjs","createR196MetricProvider"],
      ["fd2d-position-curvature-chain-R191.cjs","createR191Algebra"],
      ["fd2d-curvature-quartic-hinge-R211.cjs","createR211AmplifiedCurvatureAlgebra"],
      ["fd2d-bent-annulus-reference-R205.cjs","createR205BentAnnulusReference"],
      ["fd2d-R201-R205-variable-amplitude-provider.cjs","createR201R205AmplitudeProvider"]
    ];
    const deps={},bindings=[];
    for(const [file,key] of dependencies){
      const full=path.join(__dirname,file),bytes=fs.readFileSync(full);
      deps[key]=require(full)[key];bindings.push({file,bytes:bytes.length,sha256:crypto.createHash("sha256").update(bytes).digest("hex")});
    }
    const raw=fs.readFileSync(candidatePath),started=Date.now();
    const result=runR211CompleteCheck(deps,JSON.parse(raw));
    result.execution={runtime:"Node",seconds:(Date.now()-started)/1000,completedUTC:new Date().toISOString()};
    result.dependencies=bindings;result.input={path:candidatePath,bytes:raw.length,sha256:crypto.createHash("sha256").update(raw).digest("hex")};
    fs.mkdirSync(path.dirname(output),{recursive:true});fs.writeFileSync(output,JSON.stringify(result,null,2)+"\n",{flag:"wx"});
    console.log(JSON.stringify({output,passed:result.passed,seconds:result.execution.seconds,dimension:result.field.normal.dimension,rowCount:result.field.normal.rowCount}));
    if(!result.passed)process.exitCode=1;
  }
}
