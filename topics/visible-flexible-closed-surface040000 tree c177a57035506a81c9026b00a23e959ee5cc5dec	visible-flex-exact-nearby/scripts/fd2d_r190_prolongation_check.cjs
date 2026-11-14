"use strict";
function runCheck({engine,bundle,providerSource,api}){
  const start=Date.now(),anchor="return {dimension:n,initialVector:()=>new Float64Array(n),";
  if(providerSource.split(anchor).length!==2)throw Error("Provider exposure anchor mismatch");
  const src=providerSource.replace(anchor,"return {_commonPointRows:(s,z)=>sliceValues(makeSlice(s,1),z,false),dimension:n,initialVector:()=>new Float64Array(n),");
  const mod={exports:{}};new Function("module","exports",src)(mod,mod.exports);
  const options={radialBasisCount:12,modes:7,angles:64,gap:.05,radiusCoefficientBound:.4};
  const old=mod.exports.createR190Provider(engine,bundle,options),z=old.initialVector();
  for(let i=0;i<old.definition.oldDimension-1;++i)z[i]=.002*Math.sin(.31+.7*i);
  z[old.definition.stateLayout.cutHeight]=.017;
  for(let j=0;j<12;++j)z[old.definition.oldDimension+j]=.07*Math.sin(.3+.4*j);
  const before=Array.from(z),out=api.prolongR190State(z,old.definition,{radialRefinements:1,modes:15,angles:128});
  const fineSame=mod.exports.createR190Provider(engine,bundle,{...options,...out.providerOptions,angles:64});
  const fine=mod.exports.createR190Provider(engine,bundle,{...options,...out.providerOptions});
  const c=old.base.centralLength,S=old.base.end,L=S-c,h=L/15;
  const points=[c,c+h/9,c+h,c+.137*L,c+.31*L,c+.53*L,c+.79*L,S-h/7,S];
  const radiusMaximum=[0,0,0],radiusScaledMaximum=[0,0,0];
  for(const s of points){
    const a=api.radiusCorrectionJets(z,old.definition,s,c,S),b=api.radiusCorrectionJets(out.vector,out.definition,s,c,S);
    for(let d=0;d<3;++d){const e=Math.abs(a[d]-b[d]);radiusMaximum[d]=Math.max(radiusMaximum[d],e);radiusScaledMaximum[d]=Math.max(radiusScaledMaximum[d],e/(1+Math.abs(a[d])));}
  }
  const rows=[];let sameRuleMaximum=0,changedRuleMaximum=0;
  for(const s of [c+.13*L,c+.31*L,c+.53*L,c+.79*L,S]){
    const a=old._commonPointRows(s,z),b=fineSame._commonPointRows(s,out.vector),d=fine._commonPointRows(s,out.vector);
    let same=0,changed=0;
    for(let j=0;j<a.length;++j)for(const key of ["rE","rF","relativeMetric","immersion"]){
      same=Math.max(same,Math.abs(a[j][key]-b[j][key]));
      changed=Math.max(changed,Math.abs(a[j][key]-d[2*j][key]));
    }
    sameRuleMaximum=Math.max(sameRuleMaximum,same);changedRuleMaximum=Math.max(changedRuleMaximum,changed);
    rows.push({s,oldQuarterNodes:a.length,newQuarterNodes:d.length,sameRuleMaximum:same,changedRuleMaximum:changed});
  }
  let boundaryCases=0;
  for(const bound of [.4,.1,Number.MIN_VALUE,2**-1022])for(const sign of [1,-1]){
    let controls=new Float64Array(12).fill(sign*bound);
    for(let level=0;level<3;++level){controls=api.refineRadiusCoefficients(controls);if(Math.max(...controls.map(Math.abs))>bound)throw Error("Refined radius coefficient box violation");++boundaryCases;}
  }
  let roundTrips=0;
  for(const x of [0,Number.MIN_VALUE,-Number.MIN_VALUE,2**-1022,.1,.4,-.4,.8,1,-1,Number.MAX_VALUE]){
    const r=api.binaryDyadic(x),y=api.roundDyadic(r.n,r.e);
    if(y!==x)throw Error("Binary dyadic round trip failed");++roundTrips;
  }
  if(z.some((x,i)=>!Object.is(x,before[i])))throw Error("Input modified");
  if(out.definition.oldDimension!==838||out.vector.length!==865)throw Error("Wrong expanded layout");
  if(Math.max(...radiusScaledMaximum)>1e-10||sameRuleMaximum>1e-10)throw Error("Common actual field identity failed");
  return {schema:"fd2d-R189-R190-prolongation-finite-check-v1",passed:true,elapsedMilliseconds:Date.now()-start,
    input:"explicit deterministic nonzero finite fixture, not a main accepted state",options,
    oldDimension:z.length,newDimension:out.vector.length,provenance:out.provenance,
    radiusJetMaximum:radiusMaximum,radiusJetScaledMaximum:radiusScaledMaximum,
    actualCommonPointRows:rows,sameRuleMaximum,changedRuleMaximum,
    constantBoundaryAndSubnormalRefinementCases:boundaryCases,exactBinaryDyadicRoundTrips:roundTrips,
    sourceArrayUnchanged:true,originalProviderSourceChanged:false,
    onlyReadOnlyInternalExposure:true,wholeObjectiveCalled:false,wholeNormalCalled:false,wholeJvpCalled:false,
    actualNonlinearAcceptedState:false,continuousCertificate:false,OSProcessCreated:false};
}
module.exports={runCheck};
if(typeof require==="function"&&require.main===module){
  const fs=require("fs"),path=require("path");
  const engine=require("./fd2d-direct-position-tangent-lift-baseline-R187.cjs").createR187();
  const bundle=JSON.parse(fs.readFileSync(process.argv[2]||"notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json","utf8"));
  const providerSource=fs.readFileSync(path.join(__dirname,"fd2d-direct-position-designed-metric-provider-R190.cjs"),"utf8");
  const result=runCheck({engine,bundle,providerSource,api:require("./fd2d_r190_prolongation.cjs")});
  result.OSProcessCreated=true;result.runtime="Node CLI";
  process.stdout.write(JSON.stringify(result,null,2)+"\n");
}
