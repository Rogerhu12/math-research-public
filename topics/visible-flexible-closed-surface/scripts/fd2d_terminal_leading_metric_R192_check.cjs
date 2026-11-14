"use strict";
function runR192Check({engine,bundle,providerSource,api,prolongationApi}){
 const start=Date.now(),anchor="return {dimension:n,initialVector:()=>new Float64Array(n),";
 if(providerSource.split(anchor).length!==2)throw Error("Provider exposure anchor mismatch");
 const mod={exports:{}};
 new Function("module","exports",providerSource.replace(anchor,"return {_rows:(s,z)=>sliceValues(makeSlice(s,1),z,false),dimension:n,initialVector:()=>new Float64Array(n),"))(mod,mod.exports);
 const options={radialBasisCount:12,modes:7,angles:64,gap:.05,radiusCoefficientBound:.4};
 const p=mod.exports.createR190Provider(engine,bundle,options),z=p.initialVector(),def=p.definition;
 for(let j=0;j<z.length;j++)z[j]=.002*Math.sin(.3+.7*j);
 z[def.stateLayout.cutHeight]=.017;
 for(let k=0;k<def.angularModes;k++)z[(def.radialBasisCount-1)*def.angularModes+k]=.003*Math.sin(.2+k);
 z[def.stateLayout.radius[1]-1]=-.03;
 const before=Array.from(z),leading=api.terminalLeadingMetric(z,def,p.base),h=leading.definition.step;
 const rows=[],A=Math.PI/2;
 for(const fraction of [.08,.04,.02,.01]){
  const tau=h*fraction,s=p.base.end-tau,actual=p._rows(s,z);
  let errE=0,errF=0,scaleE=0,scaleF=0,meanE=0,meanEnergy=0;
  for(let j=0;j<actual.length;++j){
   const u=A*j/(actual.length-1),pred=leading.evaluate(u),e=actual[j].rE/(tau*tau),f=actual[j].rF/(tau*tau);
   const w=(j===0||j===actual.length-1?.5:1)/(actual.length-1);
   errE+=w*(e-pred.rEOverTauSquared)**2;errF+=w*(f-pred.rFOverTauSquared)**2;
   scaleE+=w*pred.rEOverTauSquared**2;scaleF+=w*pred.rFOverTauSquared**2;
   meanE+=w*e;meanEnergy+=w*(e*e+2*f*f);
  }
  rows.push({tau,stepFraction:fraction,meanEOverTauSquared:meanE,
   predictedMeanE:leading.meanE,relativeEError:Math.sqrt(errE)/(1+Math.sqrt(scaleE)),
   relativeFError:Math.sqrt(errF)/(1+Math.sqrt(scaleF)),weightedEnergyOverTauFourth:meanEnergy,
   predictedLeadingWeightedEnergy:leading.weightedAngularMeanSquaredLeadingCoefficient});
 }
 if(!(rows.at(-1).relativeEError<rows[0].relativeEError&&rows.at(-1).relativeFError<rows[0].relativeFError))throw Error("Leading-term approach not observed");
 const restriction=api.createTerminalRestriction(def),zero=restriction.zeroCopy(z),free=restriction.reduce(zero.vector),back=restriction.expand(free);
 if(back.some((x,i)=>x!==zero.vector[i]))throw Error("Restriction roundtrip changed the explicitly projected field");
 if(z.some((x,i)=>!Object.is(x,before[i])))throw Error("Original input changed");
 let nonzeroReductionRejected=false;try{restriction.reduce(z);}catch(e){nonzeroReductionRejected=true;}
 if(!nonzeroReductionRejected)throw Error("Silently dropped nonzero coefficients");
 const finer=prolongationApi.prolongR190State(zero.vector,def,{radialRefinements:1,modes:15,angles:128});
 const fineRestriction=api.createTerminalRestriction(finer.definition),fineFree=fineRestriction.reduce(finer.vector);
 const n=z.length,H=new Float64Array(n*n),g=new Float64Array(n),d=new Float64Array(free.length);
 let squaredNorm=1;for(let i=0;i<n;i++){H[i*n+i]=1+i/10;g[i]=Math.sin(i+.4);squaredNorm+=g[i]*g[i]/H[i*n+i];}
 const normal=restriction.selectNormal({H,g,squaredNorm,z:zero.vector},zero.vector);
 for(let i=0;i<d.length;i++)d[i]=.01*Math.cos(.7*i);
 const dfull=restriction.expand(d);
 let qFull=0,qFree=0,linearFull=0,linearFree=0;
 for(let i=0;i<n;i++){qFull+=H[i*n+i]*dfull[i]*dfull[i];linearFull+=g[i]*dfull[i];}
 for(let i=0;i<d.length;i++){qFree+=normal.H[i*d.length+i]*d[i]*d[i];linearFree+=normal.g[i]*d[i];}
 const normalDifference=Math.max(Math.abs(qFull-qFree),Math.abs(linearFull-linearFree));
 if(normalDifference>1e-13)throw Error("Principal normal coordinate transformation mismatch");
 return {schema:"fd2d-R192-finite-terminal-leading-check-v1",passed:true,elapsedMilliseconds:Date.now()-start,
  input:"explicit nonzero synthetic field, not a main accepted state",options,
  exactAsymptoticDefinition:leading.definition,meanE:leading.meanE,cosineE:Array.from(leading.cosineE),sineF:Array.from(leading.sineF),
  actualNearCutQueries:rows,restriction:restriction.definition,explicitZeroing:zero.metadata,
  restrictionRoundtripExact:true,rejectedSilentNonzeroReduction:true,sourceArrayUnchanged:true,
  finerRestrictionDimension:fineFree.length,finerRestrictionSatisfied:true,
  syntheticNormalCoordinateQuadraticDifference:normalDifference,
  actualNewBaselineEvaluated:false,wholeObjectiveCalled:false,wholeNormalCalled:false,wholeJvpCalled:false,
  originalProviderModified:false,activeLMModified:false,OSProcessCreated:false,continuousCertificate:false};
}
module.exports={runR192Check};
if(typeof require==="function"&&require.main===module){
 const fs=require("fs"),path=require("path");
 const engine=require("./fd2d-direct-position-tangent-lift-baseline-R187.cjs").createR187();
 const bundle=JSON.parse(fs.readFileSync(process.argv[2]||"notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json","utf8"));
 const providerSource=fs.readFileSync(path.join(__dirname,"fd2d-direct-position-designed-metric-provider-R190.cjs"),"utf8");
 const report=runR192Check({engine,bundle,providerSource,
  api:require("./fd2d_terminal_leading_metric_R192.cjs"),
  prolongationApi:require("./fd2d_r190_prolongation.cjs")});
 report.OSProcessCreated=true;report.runtime="Node CLI";
 process.stdout.write(JSON.stringify(report,null,2)+"\n");
}
