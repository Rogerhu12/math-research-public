"use strict";
const fs=require("fs"),crypto=require("crypto"),path=require("path");
const {prolongR187State,correctionJets}=require("./fd2d_r187_prolongation.cjs");
const {createR187}=require("./fd2d-direct-position-tangent-lift-baseline-R187.cjs");
const sha=s=>crypto.createHash("sha256").update(s).digest("hex");
const must=(b,s)=>{if(!b)throw Error(s);};
const fixturePath=process.argv[2]||"notes/2026-11-12-fd2d-direct-position-R187-LM-01.json";
const candidatePath=process.argv[3]||"notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json";
const outputPrefix=process.argv[4]||"notes/2026-11-12-fd2d-R189-prolongation-check-01";
const began=new Date().toISOString(),start=process.hrtime.bigint();
const fixtureBytes=fs.readFileSync(fixturePath),candidateBytes=fs.readFileSync(candidatePath);
const fixture=JSON.parse(fixtureBytes),candidate=JSON.parse(candidateBytes);
const providerPath=path.join(__dirname,"fd2d-direct-position-metric-provider-R187.cjs");
const providerBytes=fs.readFileSync(providerPath),providerSource=providerBytes.toString("utf8");
// Read-only exposure of two frozen internal routines. No arithmetic or
// original source is changed. No whole evaluate/JVP/normal is called.
const target="return {dimension:n,initialVector:()=>new Float64Array(n),";
must(providerSource.split(target).length===2,"Frozen provider exposure anchor changed");
const exposed=providerSource.replace(target,"return {_commonPointRows:(s,z)=>sliceValues(makeSlice(s,1),z,false),dimension:n,initialVector:()=>new Float64Array(n),");
const moduleObject={exports:{}};
new Function("module","exports",exposed)(moduleObject,moduleObject.exports);
const {createR187Provider}=moduleObject.exports,engine=createR187();
const old=createR187Provider(engine,candidate,fixture.options);
const original=new Float64Array(fixture.z),originalCopy=Array.from(original);
const prolong=prolongR187State(original,old.definition,{radialRefinements:1,modes:15,angles:128});
const fineSameQ=createR187Provider(engine,candidate,{...fixture.options,...prolong.providerOptions,angles:fixture.options.angles});
const fineQ=createR187Provider(engine,candidate,{...fixture.options,...prolong.providerOptions});
const angularOnly=prolongR187State(original,old.definition,{radialRefinements:0,modes:15});
const reverseOrder=prolongR187State(angularOnly.vector,angularOnly.definition,{radialRefinements:1,modes:15,angles:128});
let commuteDifference=0;
for(let j=0;j<prolong.vector.length;++j)commuteDifference=Math.max(commuteDifference,Math.abs(prolong.vector[j]-reverseOrder.vector[j]));
must(commuteDifference===0,"Radial/angular operations do not commute in this loop order");
must(Array.from(original).every((x,j)=>Object.is(x,originalCopy[j])),"Original vector was modified");
const c=old.base.centralLength,S=old.base.end,L=S-c,h=L/(old.definition.radialBasisCount+3);
const radial=[0,c,c+h/7,c+h,c+2*h,c+.137*L,c+.31*L,c+.53*L,c+.79*L,S-h,S-h/9,S,S+.01];
const angles=[0,.173,Math.PI/7,Math.PI/4,Math.PI/2,2.271];
const maxJet={theta:new Array(6).fill(0),phi:new Array(6).fill(0),height:new Array(3).fill(0)};
const maxScaled={theta:new Array(6).fill(0),phi:new Array(6).fill(0),height:new Array(3).fill(0)};
let endpointMaximum=0;
for(const s of radial)for(const u of angles){
  const a=correctionJets(original,old.definition,s,u,c,S),b=correctionJets(prolong.vector,prolong.definition,s,u,c,S);
  for(const key of Object.keys(maxJet))for(let d=0;d<a[key].length;++d){
    const difference=Math.abs(a[key][d]-b[key][d]);maxJet[key][d]=Math.max(maxJet[key][d],difference);
    maxScaled[key][d]=Math.max(maxScaled[key][d],difference/(1+Math.abs(a[key][d])));
  }
  if(s===c||s===S){
    for(const key of ["theta","phi"])for(let d=0;d<3;++d)endpointMaximum=Math.max(endpointMaximum,Math.abs(a[key][d]),Math.abs(b[key][d]));
    for(let d=1;d<3;++d)endpointMaximum=Math.max(endpointMaximum,Math.abs(a.height[d]),Math.abs(b.height[d]));
  }
}
const selectedS=[c+.13*L,c+.31*L,c+.53*L,c+.79*L,S];
const actualCommon=[];let sameQMaximum=0,changedQMaximum=0;
for(const s of selectedS){
  const a=old._commonPointRows(s,original),b=fineSameQ._commonPointRows(s,prolong.vector),q=fineQ._commonPointRows(s,prolong.vector);
  let same=0,changed=0;
  must(q.length===2*(a.length-1)+1,"Expected doubled angular quadrature");
  for(let j=0;j<a.length;++j)for(const k of ["rE","rF","relativeMetric","immersion"]){
    same=Math.max(same,Math.abs(a[j][k]-b[j][k]));changed=Math.max(changed,Math.abs(a[j][k]-q[2*j][k]));
  }
  sameQMaximum=Math.max(sameQMaximum,same);changedQMaximum=Math.max(changedQMaximum,changed);
  actualCommon.push({s,oldQuarterNodes:a.length,newQuarterNodes:q.length,sameAngularRuleMaximumDifference:same,doubledAngularRuleMaximumDifference:changed});
}
const scaledMaximum=Math.max(...Object.values(maxScaled).flat());
must(scaledMaximum<1e-10,"Common correction two-jets differ beyond arithmetic tolerance");
must(sameQMaximum<1e-10,"Frozen actual common-point metric differs beyond arithmetic tolerance");
const result={schema:"fd2d-R189-actual-common-point-prolongation-check-v1",passed:true,
  startedUTC:began,completedUTC:new Date().toISOString(),seconds:Number(process.hrtime.bigint()-start)/1e9,
  inputs:{fixture:{path:fixturePath,sha256:sha(fixtureBytes),iteration:fixture.iteration},candidate:{path:candidatePath,sha256:sha(candidateBytes)},
    provider:{path:providerPath,sha256:sha(providerBytes)},prolongation:{path:"scripts/fd2d_r187_prolongation.cjs",sha256:sha(fs.readFileSync(path.join(__dirname,"fd2d_r187_prolongation.cjs")))},
    checker:{path:"scripts/fd2d_r187_prolongation_check.cjs",sha256:sha(fs.readFileSync(__filename))}},
  oldDimension:old.dimension,newDimension:prolong.vector.length,provenance:prolong.provenance,
  sampledCorrectionPoints:radial.length*angles.length,correctionJetMaximumDifferences:maxJet,correctionJetMaximumScaledDifferences:maxScaled,
  endpointCorrectionAndDerivativeMaximum:endpointMaximum,radialAngularOrderDifference:commuteDifference,
  originalArraysUnchanged:true,actualCommonPoints:actualCommon,sameAngularRuleMaximumDifference:sameQMaximum,
  changedAngularRuleMaximumDifference:changedQMaximum,
  exposedProvider:{readOnlyInternalExposure:true,onlyAddedMethod:"_commonPointRows(s,z)",arithmeticChanged:false,sourceFileChanged:false},
  wholeNormalEvaluated:false,wholeJvpEvaluated:false,wholeObjectiveEvaluated:false,acceptedNonlinearState:false,
  exactRealIdentityProvedSeparately:"results/R189-cardinal-cubic-and-angular-exact-nesting.md",binary64FieldBitwiseEqualityClaimed:false};
fs.writeFileSync(outputPrefix+"-report.json",JSON.stringify(result,null,2)+"\n");
fs.writeFileSync(outputPrefix+"-injection.json",JSON.stringify({kind:"R189 injection of the explicitly bound old actual state",source:result.inputs.fixture,
  definition:prolong.definition,providerOptions:{...fixture.options,...prolong.providerOptions},z:Array.from(prolong.vector),provenance:prolong.provenance})+"\n");
process.stdout.write(JSON.stringify({passed:result.passed,seconds:result.seconds,oldDimension:result.oldDimension,newDimension:result.newDimension,
  scaledMaximum,sameQMaximum,changedQMaximum,endpointMaximum,report:outputPrefix+"-report.json"})+"\n");
