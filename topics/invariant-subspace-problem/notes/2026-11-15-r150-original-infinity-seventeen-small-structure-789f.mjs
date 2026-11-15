#!/usr/bin/env node
// Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
// Small exact structure only. No old normal form, selected Gaussian, or Dixon digit.
import fs from "node:fs";
import crypto from "node:crypto";
function analyze(point, selected) {
  const need=(ok,msg)=>{if(!ok)throw new Error(msg)};
  const mod=x=>{x%=31n;return x<0n?x+31n:x};
  const inv=x=>{for(let i=1n;i<31n;i++)if(mod(x*i)===1n)return i;throw new Error("nonunit")};
  function determinant31(matrix) {
    const A=matrix.map(r=>r.map(x=>mod(BigInt(x))));
    const n=A.length; need(A.every(r=>r.length===n),"square minor");
    let d=1n;
    for(let i=0;i<n;i++){
      let p=i;while(p<n&&A[p][i]===0n)p++;
      if(p===n)return 0;
      if(p!==i){[A[p],A[i]]=[A[i],A[p]];d=mod(-d);}
      const z=A[i][i];d=mod(d*z);const zi=inv(z);
      for(let r=i+1;r<n;r++){
        const t=mod(A[r][i]*zi);
        for(let c=i+1;c<n;c++)A[r][c]=mod(A[r][c]-t*A[i][c]);
        A[r][i]=0n;
      }
    }
    return Number(d);
  }
  const R=point.primitivePointCoefficients.map(r=>r.map(BigInt));
  need(point.characteristicZeroSameOriginal17Verified===true,"paid original model");
  need(R.length===17&&R.every(r=>r.length===77),"17x77");
  const pairs=[];for(let i=0;i<11;i++)for(let j=i;j<11;j++)pairs.push([i,j]);
  const profile=R.map((r,e)=>{
    const uses=Array(11).fill(false);
    pairs.forEach(([i,j],k)=>{if(r[11+k]!==0n){uses[i]=true;uses[j]=true;}});
    const square=r.reduce((a,x)=>a+x*x,0n);
    return {
      equation:e,name:point.rowProportionalities[e].name,
      linearNonzero:r.slice(0,11).filter(x=>x!==0n).length,
      quadraticNonzero:r.slice(11).filter(x=>x!==0n).length,
      quadraticVariables:uses.flatMap((x,i)=>x?[i]:[]),
      constantCoefficientEliminationVariables:r.slice(0,11).flatMap((x,i)=>x!==0n&&!uses[i]?[i]:[]),
      squaredColumnNorm:String(square),squaredColumnNormBits:square.toString(2).length,
    };
  });
  const v=[-667173150n,916517025n,-1165860900n,1165860900n,-65750400n,
    -4102287600n,10453284000n,24721136800n,740643383296n,0n,0n];
  need(R.every(r=>r.slice(0,11).reduce((a,x,i)=>a+x*v[i],0n)===0n),"all17 exact linear annihilations");
  need(R.every(r=>r[9]===0n&&r[10]===0n),"two linear zero columns");
  const ld=determinant31(R.slice(0,8).map(r=>r.slice(0,8)));
  need(ld===5,"linear minor31");
  const qc=[0,1,2,3,4,5,6,7,8,9,10,11,15,18,27,35,42];
  const qd=determinant31(R.map(r=>qc.map(c=>r[11+c])));
  need(qd===4,"quadratic17 minor31");
  const [a,b,c,d]=[R[0][0],R[0][1],R[1][0],R[1][1]];
  const delta=a*d-b*c;
  need(delta!==0n&&mod(delta)===5n,"two-variable constant unit");
  for(const e of[0,1])pairs.forEach(([i,j],k)=>{
    if(i<2||j<2)need(R[e][11+k]===0n,"two-variable quadratic independence");
  });
  const pureTangent=pairs.map(([i,j],k)=>i>=9&&j>=9?k:-1).filter(k=>k>=0);
  need(R.every(r=>pureTangent.every(k=>r[11+k]===0n)),"all pure tangent quadratics zero");
  const free=selected.selectedConstantKernelFreeOriginalRows.map(Number);
  need(free.length===36&&new Set(free).size===36,"paid free36 dictionary");
  const paid=[0,1,2,4,10,11,12,13,14,16,20,22,24,3,5,6,7,21,23,25,8,9,15];
  const paidSet=new Set(paid);
  const degree=raw=>raw<=17?0:raw<=204?1:raw<=1326?2:3;
  const remaining=free.flatMap((raw,slot)=>paidSet.has(slot)?[]:[{
    slot,originalSource:raw,equation:(raw-1)%17,
    equationName:point.rowProportionalities[(raw-1)%17].name,
    multiplierDegree:degree(raw)}]);
  need(remaining.length===13&&remaining.every(x=>x.multiplierDegree===3),"remaining13 degrees");
  const observed=[10,11,12,18,19,20,21,22,23,24,25,27,28];
  return {
    status:"completed",format:"isp-original-infinity-seventeen-small-structure-v1",
    original17PolynomialSpanRankOverQ:17,quadraticSpanRankOverQ:17,
    nonzeroPureLinearConstantRowCombinationExists:false,
    linearPartRankOverQ:8,linearMinorRowsZeroBased:[0,1,2,3,4,5,6,7],
    linearMinorColumnsZeroBased:[0,1,2,3,4,5,6,7],linearMinorDeterminantModulo31:ld,
    exactLinearRightKernel:v.map(String),all17ExactLinearKernelIdentitiesVerified:true,
    linearZeroColumns:[9,10],quadraticMinorColumnsZeroBased:qc,
    quadraticMinorDeterminantModulo31:qd,
    twoVariableElimination:{variables:[0,1],equations:[0,1],
      a:String(a),b:String(b),c:String(c),d:String(d),delta:String(delta),
      deltaModulo31:Number(mod(delta)),
      exactConstantUnitEliminationValid:true,tailPolynomialDegreeAtMost:2,
      other15SubstitutedPolynomialDegreeAtMost:4,
      multiplierDegreeThreeTransportsToAtMost:6,
      selected4354SourceSpaceNotDiscarded:true,
      fixedSourceCapPreservedWithoutTransport:false},
    allPureTangentQuadraticCoefficientsZero:true,
    sourcePolynomialProfiles:profile,remainingFreeSources:remaining,
    priorObservationSources:observed.map(raw=>({originalSource:raw,multiplierDegree:degree(raw)})),
    oldFullNormalFormsRecomputed:false,oldDixonDigitsRecomputed:false,
    selectedCharacteristicZeroRankComputed:false,
  };
}
const argv=process.argv.slice(2),opts={};
for(let i=0;i<argv.length;i+=2){if(!argv[i]?.startsWith("--")||argv[i+1]===undefined)throw new Error("CLI --point-model FILE --selected-receipt FILE --out FILE");opts[argv[i]]=argv[i+1];}
const pins={
  "--point-model":"97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074",
  "--selected-receipt":"5cd9543de68bdb562bbe21189d5b0712248e6943c5572fe38ff27ec4fc1f5f68"
};
const loaded={},inputs={};
for(const [key,sha]of Object.entries(pins)){
  const b=fs.readFileSync(opts[key]),actual=crypto.createHash("sha256").update(b).digest("hex");
  if(actual!==sha)throw new Error(key+" SHA mismatch");
  loaded[key]=JSON.parse(b.toString("utf8"));inputs[key]={bytes:b.length,sha256:actual};
}
const start=process.hrtime.bigint(),result=analyze(loaded["--point-model"],loaded["--selected-receipt"]);
result.elapsedSeconds=Number(process.hrtime.bigint()-start)/1e9;
result.executionEnvironment={kind:"node",version:process.version};
result.inputs=inputs;result.sourceSHA256=crypto.createHash("sha256").update(fs.readFileSync(new URL(import.meta.url))).digest("hex");
const s=JSON.stringify(result,null,2)+"\n";if(Buffer.byteLength(s)>=100000)throw new Error("small receipt cap");
fs.writeFileSync(opts["--out"],s);
console.log(JSON.stringify({status:result.status,linearRankQ:result.linearPartRankOverQ,quadraticRankQ:result.quadraticSpanRankOverQ,twoVariableElimination:true,elapsedSeconds:result.elapsedSeconds}));
