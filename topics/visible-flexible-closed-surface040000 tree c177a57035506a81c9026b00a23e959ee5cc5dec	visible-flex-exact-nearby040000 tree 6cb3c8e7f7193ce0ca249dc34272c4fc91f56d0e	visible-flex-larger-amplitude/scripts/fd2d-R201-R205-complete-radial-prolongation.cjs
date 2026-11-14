"use strict";
/* Complete full-half R201 + developed-tail R205 Boehm radial refinement.
 * All radial channels are prolonged with the same exact rational matrix.
 * Global cut height and tail amplitude are copied unchanged.
 */
function prolongR201R205State(input,insertedKnots,splines){
 if(!splines)splines=require("./fd2d-cubic-spline-refinement-R196.cjs").createR196CubicSplines();
 if(input.schema!=="fd2d-R201-R205-variable-amplitude-actual-checkpoint-v1")
  throw Error("Explicit complete R201/R205 variable-amplitude checkpoint required");
 const o=input.options,J=o?.radialBasisCount,K=o?.modes,width=4*K+3;
 if(!Number.isInteger(J)||J<1||!Number.isInteger(K)||K<1||!Array.isArray(o.radialKnots)||o.radialKnots.length!==J+4)
  throw Error("Explicit original simple radial knots and complete angular layout required");
 const legacy=J*(2*K+2)+1,cut=J*(2*K+1),A=J*width+1,n=A+1;
 if(!Array.isArray(input.z)||input.z.length!==n||input.z.some(x=>!Number.isFinite(x)))throw Error("Complete finite parameter vector required");
 if(input.amplitudeIndex!==undefined&&input.amplitudeIndex!==A)throw Error("Amplitude index disagrees with full layout");
 if(input.cutHeightIndex!==undefined&&input.cutHeightIndex!==cut)throw Error("Cut index disagrees with full layout");
 if(!Array.isArray(insertedKnots)||insertedKnots.length<1)throw Error("At least one new explicit simple rational knot required");
 const rows=Array.from({length:J},(_,j)=>[
  ...input.z.slice(j*K,(j+1)*K),...input.z.slice(J*K+j*K,J*K+(j+1)*K),
  input.z[2*J*K+j],input.z[2*J*K+J+1+j],
  ...input.z.slice(legacy+j*(2*K+1),legacy+(j+1)*(2*K+1))
 ]);
 if(rows.some(r=>r.length!==width))throw Error("Internal complete channel count");
 const p=splines.prolongCoefficients(o.radialKnots,rows,insertedKnots),JJ=p.new_count;
 const newLegacy=JJ*(2*K+2)+1,newCut=JJ*(2*K+1),newA=JJ*width+1,z=new Array(newA+1).fill(0);
 for(let j=0;j<JJ;j++){
  const r=p.coefficients_binary64[j];
  for(let k=0;k<K;k++){z[j*K+k]=r[k];z[JJ*K+j*K+k]=r[K+k];}
  z[2*JJ*K+j]=r[2*K];z[2*JJ*K+JJ+1+j]=r[2*K+1];
  for(let k=0;k<2*K+1;k++)z[newLegacy+j*(2*K+1)+k]=r[2*K+2+k];
 }
 z[newCut]=input.z[cut];z[newA]=input.z[A];
 if(!Object.is(z[newCut],input.z[cut])||!Object.is(z[newA],input.z[A]))throw Error("Global coordinates must be copied exactly");
 return {schema:"fd2d-R201-R205-complete-radial-prolongation-v1",
  options:{...o,radialBasisCount:JJ,radialKnots:p.new_knots},
  z,amplitudeIndex:newA,cutHeightIndex:newCut,
  inherited:{curvatureOptions:input.curvatureOptions,geometryOptions:input.geometryOptions,centralSeed:input.centralSeed,
   lambda:input.nextLambda??input.lambda,candidate:input.candidate},
  channelOrder:["theta sine 2..2K","psi sine 2..2K","height","rho","theta constant","theta cosine 2..2K","psi cosine 2..2K"],
  oldDimension:n,newDimension:z.length,oldRadialCount:J,newRadialCount:JJ,angularModes:K,
  oldKnots:p.old_knots,newKnots:p.new_knots,insertedKnots:p.insertions.map(x=>x.inserted_knot),
  exactRealAllChannelFieldPreserved:true,finiteStoredFieldClaimedBitwiseEqual:false,
  globalCutAndAmplitudeCopiedByObjectIs:true,roundingMode:p.rounding_mode,intermediateRounding:p.intermediate_rounding,
  storedSplineRoundoffBounds:p.stored_spline_roundoff_bounds,
  basisNumericalEvaluationErrorIncluded:false,physicalRoundoffConversion:"For L=S-c, divide first bounds by L and second bounds by L^2; nonlinear X/phase effects need separate propagation",
  definitionRebuildRequired:true,freshCompleteNormalRequired:true,newRadialQuadratureRequiresFreshBaseline:true,
  acceptedOptimizationStep:false,continuousCertificate:false,strongTargetComplete:false};
}
module.exports={prolongR201R205State};
if(require.main===module){
 const fs=require("node:fs"),[inputPath,knotsJSON,outputPath]=process.argv.slice(2);
 if(!inputPath||!knotsJSON||!outputPath||fs.existsSync(outputPath))throw Error("checkpoint.json, explicit JSON rational knot array, fresh output.json required");
 const r=prolongR201R205State(JSON.parse(fs.readFileSync(inputPath,"utf8")),JSON.parse(knotsJSON));
 fs.writeFileSync(outputPath,JSON.stringify(r,null,2)+"\n");
 process.stdout.write(JSON.stringify({oldDimension:r.oldDimension,newDimension:r.newDimension,acceptedOptimizationStep:false})+"\n");
}
