"use strict";

/* A genuine new physical-metric design, not refinement of the R208 metric.
 * t denotes the old physical meridian coordinate.  The exact definition is
 * sigma=t+Delta*S9((t-c)/(S-c)), a_Delta(sigma)=a_0(t), and
 * Z_Delta(sigma)=c+integral_c^t sqrt(sigma'(v)^2-a_0'(v)^2) dv.
 * S9'=630*x^4*(1-x)^4.  All finite radial and angular factories are rebuilt
 * with the new end S+Delta.  The two endpoint position jets remain admissible
 * for the unchanged central cylinder and R205 flat/developed tail.
 * Floating primitives below are explicit quadrature approximations. They are
 * not continuous certificates. Delta is fixed during each numerical branch.
 */

function createOuterLengthBase(engine, original, extraLength, options={}) {
  if (!(Number.isFinite(extraLength) && extraLength >= 0)) throw Error("Nonnegative finite extraLength required");
  if (extraLength === 0) return original;
  const c=original.centralLength, S=original.end, L=S-c, end=S+extraLength;
  const order=options.quadratureOrder===undefined?32:options.quadratureOrder;
  if (!(L>0) || !Number.isInteger(order) || order<8 || order>128) throw Error("Positive original outer interval and quadrature order 8..128 required");
  const rule=engine.gauss(order), ratio=extraLength/L;
  function smoothstep(x) {
    if(x<=0)return 0;if(x>=1)return 1;
    return x**5*(126+x*(-420+x*(540+x*(-315+70*x))));
  }
  function clockAt(t) {
    if(t<=c)return {sigma:t,v:1,vt:0,excess:0};
    if(t>=S)return {sigma:t+extraLength,v:1,vt:0,excess:0};
    const x=(t-c)/L,excess=ratio*630*x**4*(1-x)**4;
    return {sigma:t+extraLength*smoothstep(x),v:1+excess,
      vt:ratio*2520*x**3*(1-x)**3*(1-2*x)/L,excess};
  }
  function inverse(sigma) {
    if(sigma<=c)return sigma;if(sigma>=end)return S;
    let lo=c,hi=S,t=c+(sigma-c)*L/(end-c);
    for(let k=0;k<60;k++) {
      const q=clockAt(t),f=q.sigma-sigma;
      if(Math.abs(f)<=2e-16*Math.max(1,end))break;
      if(f>0)hi=t;else lo=t;
      const proposal=t-f/q.v;
      t=proposal>lo&&proposal<hi?proposal:(lo+hi)/2;
    }
    return t;
  }
  const oldCuts=[c,S];
  for(const p of original.segments) {
    if(p.s0>=c)oldCuts.push(p.s0);if(p.s1>=c)oldCuts.push(p.s1);
    if(p.kind==="turn")for(const x of [.08,.92])oldCuts.push(p.s0+x*p.L);
  }
  oldCuts.sort((a,b)=>a-b);
  const cuts=oldCuts.filter((x,i)=>x>=c&&x<=S&&(i===0||x-oldCuts[i-1]>2e-14));
  cuts[0]=c;cuts[cuts.length-1]=S;
  function deltaIntegrand(t) {
    const p=original.at(t),q=clockAt(t);
    if(p.zs < -1e-12)throw Error("This wrapper requires the nondecreasing-height B32 branch");
    const positive=Math.sqrt(p.zs*p.zs+q.excess*(2+q.excess));
    // Rationalized difference avoids subtracting two nearly equal values.
    return q.excess===0?0:q.excess*(2+q.excess)/(positive+p.zs);
  }
  const added=[0];
  for(let j=1;j<cuts.length;j++)added.push(added.at(-1)+engine.quad(deltaIntegrand,cuts[j-1],cuts[j],rule));
  function heightAddition(t) {
    if(t<=c)return 0;if(t>=S)return added.at(-1);
    let lo=0,hi=cuts.length-1;
    while(hi-lo>1){const mid=(lo+hi)>>1;if(cuts[mid]<=t)lo=mid;else hi=mid;}
    return added[lo]+engine.quad(deltaIntegrand,cuts[lo],t,rule);
  }
  const height=original.height+added.at(-1),cache=new Map(),cacheLimit=options.baseCacheLimit??1024;
  function at(sigma) {
    if(!(Number.isFinite(sigma)&&sigma>=0&&sigma<=end))throw Error("New physical meridian point outside [0,S+Delta]");
    if(cache.has(sigma))return cache.get(sigma);
    const t=inverse(sigma),p=original.at(t),q=clockAt(t),as=p.as/q.v,
      ass=p.ass/(q.v*q.v)-p.as*q.vt/(q.v*q.v*q.v),
      oldNumerator=Math.sqrt(p.zs*p.zs+q.excess*(2+q.excess)),zs=oldNumerator/q.v;
    const zss=oldNumerator>0?(-p.as*p.ass*q.v+p.as*p.as*q.vt)/(q.v**3*oldNumerator):0;
    const out={a:p.a,as,ass,z:p.z+heightAddition(t),zs,zss,s:sigma};
    if(sigma===end){out.a=.8;out.as=-1;out.ass=0;out.z=height;out.zs=0;out.zss=0;}
    if(cacheLimit>0){if(cache.size>=cacheLimit)cache.delete(cache.keys().next().value);cache.set(sigma,out);}
    return out;
  }
  const allCuts=[0,...cuts.map(t=>clockAt(t).sigma)];
  const segments=allCuts.slice(1).map((s1,i)=>({kind:"outer_length_quadrature_cell",s0:allCuts[i],s1,L:s1-allCuts[i]}));
  const originalCoast=original.segments.find(p=>p.kind==="coast_to");
  return {a0:original.a0,end,height,centralLength:c,segments,at,
    deepCoast:originalCoast?clockAt(originalCoast.s1).sigma-clockAt(originalCoast.s0).sigma:undefined,
    originalEnd:S,originalHeight:original.height,
    oldToNew:t=>clockAt(t).sigma,newToOld:inverse,
    outerLengthDesign:{schema:"6a65-positive-outer-length-design-v1",extraLength,
      originalEnd:S,newEnd:end,centralLength:c,originalHeight:original.height,newHeight:height,
      clock:"sigma=t+Delta*S9((t-c)/(S-c)); S9'=630*x^4*(1-x)^4",
      radius:"a_Delta(sigma(t))=a_0(t)",
      height:"Z_Delta(sigma(t))=c+integral_c^t sqrt(sigma'(v)^2-a_0'(v)^2) dv",
      primitiveEvaluation:{quadratureOrder:order,splitAtAllOriginalSegmentsAndTurnBreaks:true,continuousRemainderCertified:false},
      physicalMetricChanged:true,finalFixedMetricRefinement:false}}
}

function createOuterLengthRunProvider(candidate,input,extraLength,options={}) {
  const oldEngine=require("./fd2d-direct-position-tangent-lift-baseline-R187.cjs").createR187(),oldBase=oldEngine.candidate(candidate);
  const base=createOuterLengthBase(oldEngine,oldBase,extraLength,options),engine={...oldEngine,candidate:()=>base};
  const splines=require("./fd2d-cubic-spline-refinement-R196.cjs").createR196CubicSplines();
  const metric=require("./fd2d-nonuniform-metric-provider-R196.cjs").createR196MetricProvider(engine,candidate,input.options,splines);
  if(extraLength>0)metric.definition={...metric.definition,outerLengthDesign:base.outerLengthDesign,
    radialMetric:"New positive-clock outer-length design plus unchanged complete radius basis; changing Delta or rho changes g"};
  let algebra=require("./fd2d-position-curvature-chain-R191.cjs").createR191Algebra();
  if(options.quartic)algebra=require("./fd2d-curvature-quartic-hinge-R211.cjs").createR211AmplifiedCurvatureAlgebra(algebra,{tau:2});
  const referenceFactory=amplitude=>require("./fd2d-bent-annulus-reference-R205.cjs").createR205BentAnnulusReference(engine,base,
    {amplitude,angles:input.options.angles,cacheLimit:options.referenceCacheLimit??0});
  const positionSource=options.lazyCurvature?"./fd2d-R201-R205-variable-amplitude-lazy-curvature.cjs":"./fd2d-R201-R205-variable-amplitude-provider.cjs";
  const curvatureOptions={...input.curvatureOptions,sliceReuse:{valueLimit:8,derivativeLimit:4}};
  const position=require(positionSource).createR201R205AmplitudeProvider(engine,metric,referenceFactory,curvatureOptions,algebra);
  if(options.quartic)position.definition={...position.definition,curvaturePenaltyModel:algebra.definition,
    completeSquaredPenaltyEqualsSumPrincipalCurvatureHingesSquared:false,
    baseProvider:{...position.definition.baseProvider,curvaturePenaltyModel:algebra.definition,
      completeSquaredPenaltyEqualsSumPrincipalCurvatureHingesSquared:false}};
  const provider=require("./fd2d-R201-R205-variable-amplitude-geometric-guide.cjs").createR201R205AmplitudeGeometryProvider(position,input.geometryOptions);
  const z=Array.from(input.z),cut=metric.definition.stateLayout.cutHeight;
  if(input.outerLengthDesign) {
    if(input.outerLengthDesign.extraLength!==extraLength)throw Error("A saved new-design state must retain its exact extraLength");
  } else z[cut]+=oldBase.height-base.height;
  if(z.length!==provider.dimension)throw Error("Complete inherited parameter layout mismatch");
  return {engine,oldBase,base,metric,position,provider,z,cutHeightIndex:cut,
    design:{...base.outerLengthDesign,extraLength,centralSeedUnchanged:true,
      allBasisAndProfileWeightsRebuiltOnNewPhysicalInterval:true,
      initialCutCorrection:oldBase.height-base.height,
      initialTrueCuffHeight:base.height+z[cut],continuousCertificate:false,strongTargetComplete:false}};
}

module.exports={createOuterLengthBase,createOuterLengthRunProvider};

if(require.main===module) {
  const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
  const [candidateFile,inputFile,outputFile,...deltaStrings]=process.argv.slice(2);
  if(!candidateFile||!inputFile||!outputFile||fs.existsSync(outputFile))throw Error("candidate input fresh-output delta... required");
  const candidate=JSON.parse(fs.readFileSync(candidateFile)),input=JSON.parse(fs.readFileSync(inputFile)),rows=[];
  for(const delta of deltaStrings.length?deltaStrings.map(Number):[0,.02,.05,.1,.2]) {
    const begin=Date.now(),q=createOuterLengthRunProvider(candidate,input,delta),value=q.provider.value(q.z);
    const row={extraLength:delta,design:q.design,value,elapsedSeconds:(Date.now()-begin)/1000};rows.push(row);
    process.stdout.write(JSON.stringify({extraLength:delta,R2:value.squaredNorm,metric:value.maxRelativeMetric,
      curvature:value.curvature?.maxCurvature,geometry:value.geometry,seconds:row.elapsedSeconds})+"\n");
  }
  const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
  fs.mkdirSync(path.dirname(outputFile),{recursive:true});
  fs.writeFileSync(outputFile,JSON.stringify({schema:"6a65-outer-length-actual-value-scan-v1",
    source:{candidate:candidateFile,candidateSHA256:hash(candidateFile),input:inputFile,inputSHA256:hash(inputFile),scriptSHA256:hash(__filename)},
    rows,acceptedSteps:0,continuousCertificate:false,strongTargetComplete:false},null,2)+"\n");
}
