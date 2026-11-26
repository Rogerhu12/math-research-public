"use strict";
/* Exact reproducible small fixture for recovered v2; this is a NEW check,
 * not a reconstruction of the ephemeral 51-dimensional check lost earlier.
 * No surface provider, geometry value, full normal, or LM attempt is run. */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto"),assert=require("node:assert/strict");
const base=require("./fd2d-R201-R205-band-border-layout.cjs");
const {createR206AppendedGlobalKernel}=require("./fd2d_appended_global_schur_R206.cjs");
const {createSharedBandR206Kernel}=require("./6a65-r206-shared-band-memory-kernel-recovered-v2.cjs");
const oldKernel=createR206AppendedGlobalKernel(base),newKernel=createSharedBandR206Kernel(base);
const sha=x=>crypto.createHash("sha256").update(x).digest("hex");
const fileHash=p=>sha(fs.readFileSync(p));
const vectorHash=a=>{const v=ArrayBuffer.isView(a)?a:Float64Array.from(a);return sha(Buffer.from(v.buffer,v.byteOffset,v.byteLength));};
let scalarComparisons=0;
function bitEqual(a,b,where="root"){
  if(ArrayBuffer.isView(a)||ArrayBuffer.isView(b)||Array.isArray(a)||Array.isArray(b)){
    const sequence=x=>ArrayBuffer.isView(x)||Array.isArray(x);
    assert(sequence(a)&&sequence(b),where+" numeric/ordinary sequence kind");
    assert.equal(a.length,b.length,where+" length");
    for(let i=0;i<a.length;i++)bitEqual(a[i],b[i],where+"["+i+"]");
    return;
  }
  if(a!==null&&typeof a==="object"||b!==null&&typeof b==="object"){
    assert(a!==null&&b!==null&&typeof a==="object"&&typeof b==="object",where+" object kind");
    const ak=Object.keys(a).filter(k=>k!=="memoryPreparation").sort();
    const bk=Object.keys(b).filter(k=>k!=="memoryPreparation").sort();
    assert.deepEqual(ak,bk,where+" key set");
    for(const k of ak)bitEqual(a[k],b[k],where+"."+k);
    return;
  }
  scalarComparisons++;
  assert(Object.is(a,b),where+" bit difference: "+String(a)+" / "+String(b));
}
function fixture(asOrdinaryArray=false){
  const N=51,n=50,J=7,b=7,w=2,cut=17;
  const pool=Array.from({length:n},(_,i)=>i).filter(i=>i!==cut);
  const field=Array.from({length:49},(_,j)=>pool[(23*j)%49]),perm=[...field,cut,50];
  const C=new Float64Array(N*N);
  for(let i=0;i<49;i++){
    C[i*N+i]=4+(i%7)/7;
    for(let j=0;j<i;j++)if(Math.floor(i/b)-Math.floor(j/b)<=w)
      C[i*N+j]=C[j*N+i]=.002*Math.sin((i+1)*(j+2));
    C[i*N+49]=C[49*N+i]=.003*Math.cos(i+1);
    C[i*N+50]=C[50*N+i]=.002*Math.sin(i+3);
  }
  C[49*N+49]=3.2;C[50*N+50]=2.8;C[49*N+50]=C[50*N+49]=.0013;
  const D=Float64Array.from({length:N},(_,i)=>10**(-4+8*i/(N-1)));
  const H=new Float64Array(N*N),g=Float64Array.from({length:N},(_,i)=>.01*Math.cos(i+.3)*D[i]);
  for(let i=0;i<N;i++)for(let j=0;j<N;j++)
    H[perm[i]*N+perm[j]]=(C[i*N+j]*D[perm[i]])*D[perm[j]];
  H[field[8]*N+field[3]]+=1e-13*Math.sqrt(H[field[8]*N+field[8]]*H[field[3]*N+field[3]]);
  H[cut*N+50]+=3e-14*Math.sqrt(H[cut*N+cut]*H[50*N+50]);
  const diagonal=Float64Array.from({length:N},(_,i)=>H[i*N+i]);
  diagonal[field[2]]*=1+1e-5; // A reported supplied-diagonal mismatch, never a new scale.
  const definition={schema:"fd2d-R206-appended-global-parameter-provider-v1",dimension:N,
    globalIndex:n,globalName:"fixture-global",
    baseProvider:{schema:"fd2d-R201-R205-full-half-developed-tail-curvature-provider-v1",dimension:n,angularModes:1,
      radialBlockLayout:{schema:"fd2d-R201-explicit-radial-blocks-v1",
        radialBlocks:Array.from({length:J},(_,j)=>field.slice(j*b,(j+1)*b)),globalBorder:cut}}};
  return {normal:{H:asOrdinaryArray?Array.from(H):H,g,diagonal,squaredNorm:2.75},
    definition,options:{halfBandwidthBlocks:w},field,
    parameters:{dimension:N,baseDimension:n,radialBlocks:J,blockSize:b,halfBandwidthBlocks:w,
      originalCutBorder:cut,appendedGlobal:50,fieldPermutationMultiplier:23,
      diagonalMultiplierRange:[1e-4,1e4],explicitScaledAsymmetries:[1e-13,3e-14],
      deliberatelyMismatchedSuppliedDiagonal:true,inputStorage:asOrdinaryArray?"ordinary-array":"Float64Array"}};
}
function snapshots(normal){return {H:vectorHash(normal.H),g:vectorHash(normal.g),diagonal:vectorHash(normal.diagonal)};}
function main(){
  const output=process.argv[2];
  if(!output||fs.existsSync(output))throw Error("fresh-report.json required");
  const start=Date.now(),cases=[];
  for(const ordinary of [false,true]){
    const f=fixture(ordinary),before=snapshots(f.normal),countBefore=scalarComparisons;
    const p=oldKernel.prepareBandBorderNormal(f.normal,f.definition,f.options);
    const q=newKernel.prepareBandBorderNormal(f.normal,f.definition,f.options);
    bitEqual(p,q,"prepared");
    const preparedComparisons=scalarComparisons-countBefore;
    assert.equal(q.H,f.normal.H,"full H borrowed");
    const sharedKeys=["band","originalLower","originalUpper","border","originalFieldToBorder",
      "originalBorderToField","diagonal","scale","layout"];
    for(const k of sharedKeys)assert.equal(q.base[k],q.aux[k],"actual shared "+k);
    assert.notEqual(q.base.gradient,q.aux.gradient);assert.notEqual(q.base.scaledGradient,q.aux.scaledGradient);
    assert(q.base.info.suppliedDiagonalDifference>0);assert.equal(q.aux.info.suppliedDiagonalDifference,0);
    const solves=[];
    for(const lambda of [1e-6,.001,1,10]){
      const a=oldKernel.solvePreparedBandBorder(p,lambda),b=newKernel.solvePreparedBandBorder(q,lambda);
      assert.equal(a.ok,true);assert.equal(b.ok,true);
      const beforeSolve=scalarComparisons;bitEqual(a,b,"solve("+lambda+")");
      solves.push({lambda,bitwiseScalarComparisons:scalarComparisons-beforeSolve,
        directionSHA256:vectorHash(a.direction),scaledDirectionSHA256:vectorHash(a.scaledDirection),
        scaleSHA256:vectorHash(a.scale),slope:a.slope,quadratic:a.quadratic,
        predictedSquaredNorm:a.predictedSquaredNorm,
        workingScaledEquationResidualMaximum:a.info.workingScaledEquationResidualMaximum,
        originalScaledEquationResidualMaximum:a.info.originalScaledEquationResidualMaximum,
        workingScaledEquationRelativeResidual:a.info.workingScaledEquationRelativeResidual,
        originalScaledEquationRelativeResidual:a.info.originalScaledEquationRelativeResidual,
        hiddenDiagonalShift:a.info.hiddenDiagonalShift});
    }
    assert.deepEqual(snapshots(f.normal),before,"input H/g/diagonal unchanged");
    const rejection=[];
    for(const [name,kernel] of [["old",oldKernel],["new",newKernel]]){
      const bad={...f.normal,H:Float64Array.from(f.normal.H)};
      bad.H[f.field[0]*51+f.field[48]]=1e-300;
      let caught=null;
      try{kernel.prepareBandBorderNormal(bad,f.definition,f.options);}catch(e){caught=e;}
      assert(caught&&caught.code==="NONZERO_OUTSIDE_RADIAL_BAND",name+" strict nonzero rejection");
      rejection.push({kernel:name,code:caught.code,offBandMaximum:caught.details.offBandMaximum,
        offBandCount:caught.details.offBandCount});
    }
    cases.push({parameters:f.parameters,inputArraySHA256:before,preparedComparisons,solves,
      sharedArraysVerified:sharedKeys,independentAuxiliaryGradientVerified:true,
      suppliedDiagonalDiagnosticsPreserved:true,inputArraysUnchanged:true,rejection,
      allocationAccounting:q.info.memoryPreparation});
  }
  const sourceFiles=["6a65-r206-shared-band-memory-kernel-recovered-v2.cjs",
    "fd2d_appended_global_schur_R206.cjs","fd2d-R201-R205-band-border-layout.cjs"];
  const out={schema:"6a65-R206-shared-band-memory-small-fixture-recovered-v2",
    sourceIdentityIsNew:true,earlierLostFixtureNotRecreated:true,node:process.version,
    entrySHA256:fileHash(__filename),sourceFiles:Object.fromEntries(sourceFiles.map(f=>[f,fileHash(path.join(__dirname,f))])),
    cases,allBitwiseComparisonsPassed:true,totalScalarComparisons:scalarComparisons,
    seconds:(Date.now()-start)/1000,maxRSSKiB:process.resourceUsage().maxRSS,
    surfaceProviderEvaluated:false,actualSurfaceNormalEvaluated:false,actualLMSteps:0,
    actualFullMatrixComparisonNotYetRun:true,OSExitCode:null,externalExitReceiptRequired:true,
    continuousCertificate:false,strongTargetComplete:false};
  fs.mkdirSync(path.dirname(output),{recursive:true});fs.writeFileSync(output,JSON.stringify(out,null,2)+"\n");
  process.stdout.write(JSON.stringify({report:output,reportSHA256:fileHash(output),
    allBitwiseComparisonsPassed:true,totalScalarComparisons:scalarComparisons,
    maxRSSKiB:out.maxRSSKiB,seconds:out.seconds})+"\n");
}
if(require.main===module)main();
module.exports={fixture,bitEqual};
