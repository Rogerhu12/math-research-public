// Original four-scalar completed-log audit. Author: ChatGPT (AI), literature_audit.
// Date: 2026-11-16. Read-only; no mathematical arrays are written.

function parsePreservingNumbers(s){
 let i=0;const ws=()=>{while(/\s/.test(s[i]||"")&&i<s.length)i++};
 function node(){ws();const c=s[i];
  if(c==="{"){i++;const e=[];ws();if(s[i]!=="}"){for(;;){ws();const k=tokenString();ws();if(s[i++]!==":")throw Error("colon");e.push([JSON.parse(k),node()]);ws();if(s[i]==="}")break;if(s[i++]!==",")throw Error("object comma")}}i++;return{kind:"object",entries:e}}
  if(c==="["){i++;const e=[];ws();if(s[i]!=="]"){for(;;){e.push(node());ws();if(s[i]==="]")break;if(s[i++]!==",")throw Error("array comma")}}i++;return{kind:"array",entries:e}}
  if(c==='"')return{kind:"string",value:JSON.parse(tokenString())};
  const m=s.slice(i).match(/^(?:-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?|true|false|null)/);if(!m)throw Error("literal");i+=m[0].length;return{kind:"literal",raw:m[0]};
 }
 function tokenString(){const j=i++;for(;;){if(i>=s.length)throw Error("string eof");const c=s[i++];if(c==="\\"){i++;continue}if(c==='"')break}return s.slice(j,i)}
 const v=node();ws();if(i!==s.length)throw Error("trailing JSON");return v;
}
function serialPreserved(v){
 const str=s=>JSON.stringify(s).replace(/[\u007f-\uffff]/g,c=>"\\u"+c.charCodeAt(0).toString(16).padStart(4,"0"));
 if(v.kind==="literal")return v.raw;
 if(v.kind==="string")return str(v.value);
 if(v.kind==="array")return "["+v.entries.map(serialPreserved).join(",")+"]";
 return "{"+v.entries.slice().sort((a,b)=>a[0]<b[0]?-1:a[0]>b[0]?1:0).map(([k,z])=>str(k)+":"+serialPreserved(z)).join(",")+"}";
}
function member(v,k){const e=v.entries.find(e=>e[0]===k);if(!e)throw Error("missing "+k);return e[1];}

function auditCompletedFourScalarLog(log,sha){
 const check=(v,m)=>{if(!v)throw Error(m)};
 const all=[];
 for(const l of log.split("\n")){
  const at=l.indexOf("ISP_REMOTE_STEP ");if(at<0)continue;
  const text=l.slice(at+16),tree=parsePreservingNumbers(text),outer=JSON.parse(text);
  check(outer.runId==="43830684123","actual run");
  all.push({tree,outer});
 }
 check(all.length===10&&all.every(z=>z.outer.exitCode===0),"ten completed actual steps");
 const expected=[
  ["rebuild-selected-true16-original8-7-3-1",27369,"f2d33c57d04f609e6b5e39a69da9933cfc68f56f7a55b67a4dc0853f4f2dff48",30],
  ["same-basis-original-hstar-first-carry",17203,"273eff195255b544005740b1a382b3a5c3ab2ee6f55593f98599f45c63aa393e",8],
  ["same-basis-original-h0-seven-socle",23917,"cf79d372a7f297422803fcdd6bb0cf12ca2721898814222ee15f7acb0a73247f",16],
  ["same-basis-original-hstar-x2-socle",26336,"a58a0b5c289d09a2eb5a25a6198aa59625929bbffc78bb9d825fe9fc2f4755bd",16],
  ["same-basis-original-hstar-x3-socle",26339,"8881a23a87a5c95161564960bb6c5ad75106057d40357cdc7d522c8fd3f28779",16],
  ["complete-original-hstar-four-scalar-annihilator",12803,"15e8dd4229d99debd70e967d2970be74adac6589b0dfd8bfa7c5f44538a9eeb0",0]
 ];
 const math=[];
 for(const [id,bytes,hash,n] of expected){
  const a=all.find(z=>z.outer.stepId===id);check(a,"step present");const r=member(a.tree,"result");
  r.entries=r.entries.filter(e=>e[0]!=="events");
  if(n===0){
   const f=serialPreserved(member(member(r,"parameters"),"final"))+"\n";
   r.entries.push(["resultFile",parsePreservingNumbers(JSON.stringify({bytes:f.length,sha256:sha(f)}))]);
  }
  const raw=serialPreserved(r)+"\n";
  check(raw.length===bytes&&sha(raw)===hash,"exact raw receipt "+id);
  check(a.outer.fullTemporaryReceiptBytes===bytes&&a.outer.fullTemporaryReceiptSHA256===hash,"published receipt pin "+id);
  const result=a.outer.result,p=result.parameters;
  check(result.status==="completed","complete status");
  check(Object.keys(p.stages||{}).length===n,"stage count");
  for(const z of Object.values(p.stages||{})){
   check(z.status==="completed","actual stage completed");
   const s=z.statistics;
   if("allOriginal17CoefficientsDivisible" in s)check(s.allOriginal17CoefficientsDivisible,"integer divisibility");
   if("fullOriginalGJetIdentityVerified" in s)
    check(s.fullOriginalGJetIdentityVerified&&s.all13FreeConditionsRetained&&s.maximumSmithExponent===5,"whole unit products and free checks");
  }
  math.push(a.outer);
 }
 const parent=math[0].result,pb=parent.binding;
 check(parent.parameters.allOriginalIntegerCarriesVerified&&parent.parameters.full210NotRecomputed,"selected actual reconstruction");
 check(parent.parameters.trueBasisIdentities.true16.sha256==="679132fd4727fd305b77c82beb5d3f2e002df1860045200c3392158ab8eb48b9","full true16");
 check(parent.parameters.trueBasisIdentities.parameterAction16.sha256==="59d09cbeec71ebf7cda6f12ddd21c1b7ffe1c83a3f9de81b776df0a97df687d8","original parameter action");
 for(const z of math.slice(1,5)){
  const p=z.result.parameters,f=p.final;
  check(p.inputIdentity.parentBinding===pb,"one actual parent");
  for(const flag of ["all104LocalFreeChecks","all505GlobalFreeChecks","allComplete315SpanIdentitiesVerified","allOriginal17IntegerProductsVerified","allOriginalSourceCorrectionsRetained"])check(f[flag]===true,flag);
  for(const k of ["G","V"])check(p.explicitParentTransports[k].allMathematicalPayloadBytesIdentical===true,"constant payload transport");
  for(const k of ["L3","L4","L5","L6"])if(k in p.explicitParentTransports)check(p.explicitParentTransports[k].all6188RowHeadersAndSelectedValuesVerified===true,"full true-source transport");
 }
 const cf=math[1].result.parameters.final,vf=math[2].result.parameters.final,
       zf=math[3].result.parameters.final,qf=math[4].result.parameters.final,
       f=math[5].result.parameters.final;
 check(JSON.stringify(cf.exactExponentsWhenClosed)===JSON.stringify(Array(9).fill(5)),"fresh hstar controls");
 check(JSON.stringify(vf.minimum31DenominatorExponents)===JSON.stringify(Array(9).fill(2)),"fresh h0 controls");
 check(zf.targetParameterPower===2&&qf.targetParameterPower===3,"unscaled two parameter targets");
 const C=cf.firstCarryCoordinateRows,V=vf.obstructionRows,Z=zf.socleCoordinateRows,Q=qf.socleCoordinateRows;
 const A=Array.from({length:63},(_,i)=>{const j=Math.floor(i/7),k=i%7;return[k===6?C[15][j]:0,V[k][j],Z[k][j],Q[k][j]]});
 check(JSON.stringify(A)===JSON.stringify(f.jointMatrixRows),"all252 source-to-final coordinates");
 const matrixHash=a=>sha(String.fromCharCode(...a.flat()));
 check(matrixHash(A)===f.jointMatrix.sha256,"original matrix byte hash");
 check(matrixHash(V)===f.V.sha256&&matrixHash(Z)===f.Z.sha256&&matrixHash(Q)===f.XZ.sha256,"three full blocks");
 function rank(B){
  B=B.map(r=>r.slice());let k=0;
  for(let j=0;j<(B[0]?.length||0);j++){
   let t=k;while(t<B.length&&B[t][j]===0)t++;if(t===B.length)continue;
   [B[k],B[t]]=[B[t],B[k]];let inv=1;while(inv*B[k][j]%31!==1)inv++;
   for(let q=j;q<B[k].length;q++)B[k][q]=B[k][q]*inv%31;
   for(let h=k+1;h<B.length;h++){const c=B[h][j];for(let q=j;q<B[h].length;q++)B[h][q]=(B[h][q]-c*B[k][q]%31+31)%31}
   k++;
  }
  return k;
 }
 check(Z.flat().every(x=>x===0)&&Q.flat().every(x=>x===0),"all126 new source reads zero");
 check(rank(A)===2,"independent joint rank");
 for(let j=0;j<9;j++)check(rank(A.slice(7*j,7*j+7))===2,"independent per-target rank");
 check(f.common.kernelDimension===2&&JSON.stringify(f.common.kernelColumns)==="[[0,0,1,0],[0,0,0,1]]","complete actual kernel");
 for(const z of f.individual)check(z.kernelDimension===2&&z.parameterStable&&z.canonicalAB.every(x=>x===0),"nine exact ideals");
 return {runId:43830684123,jobId:133175032397,allTenStepsSucceeded:true,
  sixExactRawReceiptsVerified:true,allSelectedSourceAndFreeGatesVerified:true,
  sameActualParentBinding:pb,all252CoordinatesVerified:true,jointRank:2,
  allNineIndividualRanksTwo:true,all126NewCoordinatesZero:true,
  matrixSHA256:f.jointMatrix.sha256,canonicalIdeal:"(31^5,31^2*(s-2),(s-2)^2)",
  completeNotDegreeTruncation:true};
}
if(typeof module!=="undefined")module.exports={auditCompletedFourScalarLog};
if(typeof require!=="undefined"&&require.main===module){
 const fs=require("fs"),crypto=require("crypto");
 const hash=s=>crypto.createHash("sha256").update(s,"utf8").digest("hex");
 if(process.argv.length!==3)throw Error("usage: node audit.js completed-job-log.txt");
 process.stdout.write(JSON.stringify(auditCompletedFourScalarLog(fs.readFileSync(process.argv[2],"utf8"),hash))+"\n");
}
