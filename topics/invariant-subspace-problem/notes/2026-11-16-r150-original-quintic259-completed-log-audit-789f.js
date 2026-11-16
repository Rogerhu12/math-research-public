/* Original quintic259 completed-job log audit.
 * Author: Astra-ISP-789f / normal_annihilator, with /root.
 * AI-assisted: GPT-6 Astra Pro. 2026-11-16.
 * This reader rebuilds dictionaries, semantic binding and exact raw JSON.
 * It checks executed producer product flags; it does not repeat matrix arithmetic.
 * Full-rank and rank-deficient diagnostic completions remain distinct.
 */
"use strict";
function sha256(s) {
  const b=Array.from(unescape(encodeURIComponent(s)),x=>x.charCodeAt(0)), n=b.length;
  b.push(128); while(b.length%64!==56)b.push(0);
  const hi=Math.floor(n/0x20000000),lo=(n*8)>>>0;
  for(let k=3;k>=0;k--)b.push((hi>>>(8*k))&255);
  for(let k=3;k>=0;k--)b.push((lo>>>(8*k))&255);
  const K=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
  const H=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];
  const R=(x,n)=>(x>>>n)|(x<<(32-n));
  for(let off=0;off<b.length;off+=64){
    const w=new Array(64);
    for(let i=0;i<16;i++)w[i]=((b[off+4*i]<<24)|(b[off+4*i+1]<<16)|(b[off+4*i+2]<<8)|b[off+4*i+3])>>>0;
    for(let i=16;i<64;i++){const x=w[i-15],y=w[i-2];w[i]=(w[i-16]+(R(x,7)^R(x,18)^(x>>>3))+w[i-7]+(R(y,17)^R(y,19)^(y>>>10)))>>>0;}
    let [a,c,d,e,f,g,h,j]=H;
    for(let i=0;i<64;i++){const t1=(j+(R(f,6)^R(f,11)^R(f,25))+((f&g)^(~f&h))+K[i]+w[i])>>>0;const t2=((R(a,2)^R(a,13)^R(a,22))+((a&c)^(a&d)^(c&d)))>>>0;j=h;h=g;g=f;f=(e+t1)>>>0;e=d;d=c;c=a;a=(t1+t2)>>>0;}
    const x=[a,c,d,e,f,g,h,j];for(let i=0;i<8;i++)H[i]=(H[i]+x[i])>>>0;
  }
  return H.map(x=>x.toString(16).padStart(8,"0")).join("");
}
const AUDIT_FORMAT="r150-original-quintic259-completed-log-audit-v1";
const STEP_ID="original-quintic-koszul259-unit60";
const MATH_FORMAT="r150-original-quintic-koszul-span259-unit127-v1";
const SOURCE={"path":"2026-11-16-r150-original-quintic-koszul-span259-unit127-789f.py","bytes":17017,"sha256":"5242360ddf86729c271ea55559c5a84870b7fb92ef73cc653f0cf6f64165d48c"};
const HIGH={"format":"r150-original-quartic-syzygy95-small-field-gate127-v1","binding":"9f0ee10f7e4cece784d8140d063f94c210105e7dded9f811710d6ec6f2825fa1","source":{"bytes":15520,"path":"2026-11-16-r150-original-quartic-syzygy95-small-field-gate127-789f.py","sha256":"b6f72e376aa403ff540a01927ea0dd4ac136099cb7be16fe201f91e95968cc4c"},"phases":{"complete-original-quartic95-unit":{"bytes":20816,"logicalBytes":63121,"logicalSha256":"b711688351ce47161d8e898f1322a2e4e0c355bf8d7033d7a6bb2884a95343eb","path":"complete-original-quartic95-unit.json.gz","sha256":"71d679b394ab9c58f542c576690397d8f1cbcba627d74daffd72f9bbb2e3302e"},"whole-original-quartic95-input":{"bytes":16730,"logicalBytes":95934,"logicalSha256":"bf86bf186cd64d3ed78e0bf66b794bca62aa72e71abd3de3335e905c7cea0589","path":"whole-original-quartic95-input.json.gz","sha256":"a2d91336495f29ff2a15958ab26cf2cefcb782eb2e7acac2c88d90fb91a2de07"}},"manifest":{"path":"original-quartic95-manifest.json","bytes":901,"sha256":"11ad47693c39437e3f7d4711a84817e87d96392886802471116da34e1f79dacc"}};
const MIXED={"format":"r150-original-koszul55-mixed95-source-unit127-v1","binding":"b0d3f4b6dfefddccd68f804561d74188c109c151329ac525e2f7b0d2e90a6232","source":{"path":"2026-11-16-r150-original-koszul55-mixed95-source-unit127-789f.py","bytes":16461,"sha256":"fc1dfea5219a773af1140c3c9e8ba52bcb6acfd36ae67bd325c9317e416d0ab5"},"phases":{"complete-original-koszul55-mixed95-unit":{"bytes":24225,"logicalBytes":86134,"logicalSha256":"4214f41007b68fef5ecf152c769030cd1fb850dbd87d350ea49efd5da55885db","path":"complete-original-koszul55-mixed95-unit.json.gz","sha256":"4309a9164324c4e7ccf214d25b97c96845feb0e93a0dd0998e6e0a226c5e0841"}},"manifest":{"path":"original-koszul55-mixed95-manifest.json","bytes":628,"sha256":"d9211fac3cc3ff06abd00b8ff2b2dec4cb9efc685a6f982027f6a998651054e5"}};
const OBSERVER={path:"2026-11-16-r150-exact-low20-observed-execution-789f.py",bytes:5855,sha256:"c5d5f777246dbb99d516855eb007845c9b25673cfe736e74cf56f559111a5618"};
function need(x,msg){if(!x)throw Error(msg);}
function bytes(s){return unescape(encodeURIComponent(s)).length;}
class NumberToken{constructor(raw){this.raw=raw;}}
/* Preserve Python float lexemes (e.g.60.0), rather than silently changing
 * raw canonical JSON into JavaScript's60. Float repr is not a math gate. */
function losslessJSON(text){
 let i=0;
 function ws(){while(i<text.length&&/\s/.test(text[i]))i++;}
 function value(){
  ws();const ch=text[i];
  if(ch==='"'){
   const start=i++;
   while(i<text.length){
    const c=text[i++];
    if(c==="\\"){i++;continue;}
    if(c==='"')return JSON.parse(text.slice(start,i));
   }
   throw Error("unterminated JSON string");
  }
  if(ch==="{"){
   i++;const out=Object.create(null);ws();if(text[i]==="}"){i++;return out;}
   while(true){
    ws();need(text[i]==='"',"object key string");const k=value();
    need(!Object.prototype.hasOwnProperty.call(out,k),"duplicate object key");
    ws();need(text[i++]===":","object colon");out[k]=value();ws();
    const sep=text[i++];if(sep==="}")return out;need(sep===",","object comma");
   }
  }
  if(ch==="["){
   i++;const out=[];ws();if(text[i]==="]"){i++;return out;}
   while(true){
    out.push(value());ws();const sep=text[i++];
    if(sep==="]")return out;need(sep===",","array comma");
   }
  }
  for(const [word,v] of [["true",true],["false",false],["null",null]])
   if(text.slice(i,i+word.length)===word){i+=word.length;return v;}
  const m=text.slice(i).match(/^-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?/);
  need(m,"JSON scalar token");i+=m[0].length;return new NumberToken(m[0]);
 }
 const result=value();ws();need(i===text.length,"whole JSON line consumed");return result;
}
function plain(x){
 if(x instanceof NumberToken){const n=Number(x.raw);need(Number.isFinite(n),"finite numeric token");return n;}
 if(Array.isArray(x))return x.map(plain);
 if(x&&typeof x==="object")return Object.fromEntries(Object.entries(x).map(([k,v])=>[k,plain(v)]));
 return x;
}
function pstring(s){
 return JSON.stringify(s).replace(/[\u007f-\uffff]/g,c=>"\\u"+c.charCodeAt(0).toString(16).padStart(4,"0"));
}
function canon(x){
 if(x instanceof NumberToken)return x.raw;
 if(x===null)return"null";
 if(typeof x==="boolean")return x?"true":"false";
 if(typeof x==="string")return pstring(x);
 if(typeof x==="number"){
  need(Number.isSafeInteger(x),"constructed canonical values must be exact integers");
  return String(x);
 }
 if(Array.isArray(x))return"["+x.map(canon).join(",")+"]";
 need(x&&typeof x==="object","canonical JSON value");
 return"{"+Object.keys(x).sort().map(k=>pstring(k)+":"+canon(x[k])).join(",")+"}";
}
function same(x,y){return canon(x)===canon(y);}
function selectRecord(log,runId,stepId){
 const matches=[];
 for(const line of log.split(/\r?\n/)){
  const j=line.indexOf("ISP_REMOTE_STEP ");if(j<0)continue;
  const suffix=line.slice(j+"ISP_REMOTE_STEP ".length).trim();if(!suffix.startsWith("{"))continue;
  const loss=losslessJSON(suffix),obj=plain(loss);
  if(String(obj.runId)===String(runId)&&obj.stepId===stepId)matches.push({loss,obj,json:suffix});
 }
 need(matches.length===1,"exactly one actual requested completed step record");
 return matches[0];
}
function mons(n,d){
 const out=[];
 function walk(start,left,e){
  if(left===0){out.push(e.slice());return;}
  for(let i=start;i<n;i++){e[i]++;walk(i,left-1,e);e[i]--;}
 }
 walk(0,d,Array(n).fill(0));return out;
}
function sortedUniqueIds(a,n,bound,label){
 need(Array.isArray(a)&&a.length===n&&a.every((x,i)=>Number.isSafeInteger(x)&&0<=x&&x<bound&&(i===0||a[i-1]<x)),label);
}
function descriptor(d,path){
 need(d&&d.path===path&&Number.isSafeInteger(d.bytes)&&d.bytes>0&&
      Number.isSafeInteger(d.logicalBytes)&&d.logicalBytes>0&&
      /^[0-9a-f]{64}$/.test(d.sha256)&&/^[0-9a-f]{64}$/.test(d.logicalSha256),"complete stored/logical phase descriptor");
}
function reconstructedRaw(record,source){
 const r=record.loss.result;
 return canon({format:r.format,source,status:r.status,parameters:r.parameters,binding:r.binding});
}

function auditQuintic259Log(log,expectedRunId){
 need(typeof log==="string"&&/^[0-9]+$/.test(String(expectedRunId)),"whole job text and explicit run ID");
 const record=selectRecord(log,expectedRunId,STEP_ID),o=record.obj,r=o.result,p=r&&r.parameters;
 need(o.format==="isp-temporary-research-step-source-parameters-run-sha256-v1","original manifest-only execution format");
 need(o.exitCode===0&&o.receiptUnchangedFromBeforeStep===false&&o.preexistingReceipt===null,"fresh actual successful mathematical execution");
 need(o.largeDataUploadedOrCommitted===false&&o.summaryExcludesRecomputableArraysOnly===false,"complete small raw, no array upload");
 need(typeof o.python==="string"&&/^3\.12\.14(?:\s|$)/.test(o.python)&&o.pythonFlint==="0.9.0","same exact original runtime");
 need(o.script==="topics/invariant-subspace-problem/notes/"+OBSERVER.path&&o.scriptSHA256===OBSERVER.sha256,"same actual observer");
 const ex=o.observerExecution;
 need(ex&&same(ex.source,SOURCE)&&same(ex.observer,OBSERVER)&&ex.status==="completed"&&ex.childReturnCode===0&&
      ex.shellEquivalentExitCode===0&&ex.terminationRequestedByObserver===false&&
      ex.unobservedTerminationCauseInferred===false&&ex.outerSeconds===120&&ex.heartbeatSeconds===10,
      "actual observer and original child source completed");
 need(/^[0-9a-f]{40}$/.test(o.executionSourceCommit)&&o.lastRulesReadCommit===o.executionSourceCommit,"actual execution/rules-read commit");
 need(Array.isArray(o.pinnedSupportSources)&&[SOURCE,HIGH.source,MIXED.source].every(s=>
      o.pinnedSupportSources.some(x=>x.path.endsWith("/"+s.path)&&x.sha256===s.sha256)),"all mathematics/parent source pins");
 const argv=o.argvTemplate,cut=argv.indexOf("--");
 const cli=["python","{scripts}/"+SOURCE.path,
  "--high95-source","{scripts}/"+HIGH.source.path,"--high95-out","{work}/original-quartic-syzygy95-small-gate127",
  "--mixed95-source","{scripts}/"+MIXED.source.path,"--mixed95-out","{work}/original-koszul55-mixed95-unit127",
  "--out","{work}/original-quintic-koszul259-unit127","--seconds","60","--memory-mib","512"];
 need(cut>=0&&same(argv.slice(cut+1),cli),"same frozen mathematics CLI/resources");
 need(r&&r.format===MATH_FORMAT&&["completed","completed-diagnostic"].includes(r.status)&&p&&p.exitCode===0&&
      p.seconds===60&&p.memoryMiB===512&&p.prime===127&&p.coefficientRoot===100,"actual mathematical completion or bounded-rank diagnosis");
 for(const name of ["rank259Prefilled","parameterMatricesConstructed","exactECoefficientArraysComputed","BellIdentityClaimed"])
  need(p[name]===false,"restricted original scope "+name);
 const M2=mons(5,2),M3=mons(5,3),M5=mons(5,5),low=[];
 for(let i=0;i<4;i++)for(let k=1;k<=5;k++)low.push(10*i+k);
 const src=[],kl=[],hl=[];
 for(let g=0;g<11;g++)for(const m of M3)src.push([g,m]);
 for(let l=0;l<5;l++)for(let a=0;a<11;a++)for(let b=a+1;b<11;b++)kl.push([l,a,b]);
 for(let m=0;m<15;m++)for(let s=0;s<20;s++)hl.push([m,s]);
 need(M2.length===15&&M3.length===35&&M5.length===126&&src.length===385&&kl.length===275&&hl.length===300,"complete independent ordinary dictionaries");
 const dict={quadraticMonomials:M2,cubicMonomials:M3,quinticMonomials:M5,
  original385SourceLabels:src,all275KoszulLabels:kl,all300MultipliedLowLabels:hl,selectedLowSeedIds:low};
 const sem={format:MATH_FORMAT,source:SOURCE,high95:HIGH,mixed95:MIXED,prime:127,root:100,
  dictionarySha256:sha256(canon(dict)),ordinarySourceShape:[385,275],completeTargetShape:[385,300],
  originalOutputShape:[126,385],originalLowSeedIds:low,maximumKernelDimension:259,
  selectionRule:"all275 original linear Koszul multiples in (ell,a,b) order; original-column pivots and original-row unit"};
 need(same(p.semantic,sem)&&sha256(canon(sem))===r.binding,"independently reconstructed whole semantic and binding");
 need(p.originalQuinticRank===126&&Number.isSafeInteger(p.originalKoszulRank)&&0<=p.originalKoszulRank&&p.originalKoszulRank<=259&&
      p.remainingKernelQuotientDimension===259-p.originalKoszulRank,"actual rank, not prefilled");
 need(p.all34650OriginalKoszulKernelProductsVerified===true&&p.all37800CompleteTargetKernelProductsVerified===true,"all original input kernel products");
 const input="whole-original-quintic259-input",final="complete-original-quintic259-unit",ph=p.completePhases;
 need(ph&&ph[input],"whole original input registered");
 descriptor(ph[input],input+".json.gz");
 let full=false,det=null;
 if(r.status==="completed-diagnostic"){
  need(p.originalKoszulRank<259&&p.exactEQuinticKoszulSpanProved===false&&same(Object.keys(ph),[input])&&
       p.lastEvent===input,"rank-deficient diagnosis does not claim an E obstruction or completed span");
 }else{
  full=true;
  need(p.originalKoszulRank===259&&p.rankD5===126&&p.rankKoszul===259&&p.kernelQuotientDimension===0&&
       p.linearKoszulRelationDimension===16&&p.exactEQuinticKoszulSpanProved===true,"actual complete unit and dimensions");
  sortedUniqueIds(p.original259UnitRows,259,385,"all259 original unit rows");
  sortedUniqueIds(p.original259UnitColumns,259,275,"all259 original unit columns");
  need(same(p.original259UnitColumnLabels,p.original259UnitColumns.map(j=>kl[j])),"all original259 column source labels");
  det=p.original259UnitDeterminant127;
  need(Number.isSafeInteger(det)&&det>0&&det<127,"actual nonzero original259 determinant");
  const free=Array.from({length:275},(_,i)=>i).filter(i=>!p.original259UnitColumns.includes(i));
  need(same(free,p.completeSixteenRelationFreeIndices)&&free.length===16,"complete actual free relation labels");
  for(const n of ["all134162OriginalUnitInverseProductsVerified","all105875OriginalKoszulSpanProductsVerified",
    "all115500CompleteTargetSourceProductsVerified","all6160CompleteRelationProductsVerified","all67081SelectedIdentityProductsVerified"])
   need(p[n]===true,"actual producer full original product gate "+n);
  need(p.exactECoordinateArraysComputed===false&&p.newBellIdentityClaimed===false&&
       p.conditionalOriginalGradientGeneratorBound===120&&p.conditionalOriginalBellGeneratorBound===130,
       "no exact-E coordinate array or Bell identity claim");
  need(p.exactEConclusionMethod==="same original E259 unit plus exact original D5K5 and D5H identities; use the original adjugate, never lifted field coefficients",
       "same exact E proof method");
  need(same(Object.keys(ph).sort(),[final,input].sort())&&p.lastEvent===final,"exactly two completed whole phases");
  descriptor(ph[final],final+".json.gz");
 }
 const raw=reconstructedRaw(record,SOURCE);
 need(bytes(raw)===o.fullTemporaryReceiptBytes&&sha256(raw)===o.fullTemporaryReceiptSHA256,"whole raw canonical bytes/SHA with float lexemes preserved");
 const manifest=canon({format:MATH_FORMAT+"-manifest",binding:r.binding,source:SOURCE,phases:ph});
 return {format:AUDIT_FORMAT,status:"completed",mathematicalStatus:r.status,runId:String(expectedRunId),stepId:STEP_ID,
  executionSourceCommit:o.executionSourceCommit,jobLog:{bytes:bytes(log),sha256:sha256(log)},
  raw:{bytes:bytes(raw),sha256:sha256(raw)},source:SOURCE,binding:r.binding,
  originalQuinticRank:p.originalQuinticRank,originalKoszulRank:p.originalKoszulRank,
  remainingKernelQuotientDimension:p.remainingKernelQuotientDimension,completeOriginalUnitVerified:full,
  actualOriginalUnitDeterminant127:det,original259UnitRows:full?p.original259UnitRows:undefined,
  original259UnitColumns:full?p.original259UnitColumns:undefined,
  completePhases:ph,reconstructedManifest:{bytes:bytes(manifest),sha256:sha256(manifest),physicalFileIndependentlyRead:false},
  all385SourceAnd275KoszulAnd300TargetDictionariesReconstructed:true,allRawCanonicalBytesMatched:true,
  producerExecutedProductFlagsChecked:true,matrixProductsRepeatedByThisAudit:false,phasePayloadArraysReadByThisAudit:false,
  inputProductCoordinates:{D5K5:34650,D5H5:37800},
  finalProductCoordinates:full?{inverses:134162,all275:105875,all300:115500,kernel16:6160,selected:67081}:null,
  exactECoefficientArraysClaimed:false,newBellIdentityClaimed:false,
  actualMathematicalSeconds:p.elapsedSeconds,actualObserverSeconds:ex.elapsedSeconds,actualOuterSeconds:o.wallSeconds};
}
if(typeof module!=="undefined")module.exports={auditQuintic259Log,losslessJSON,plain,canon,selectRecord,reconstructedRaw,sha256};
if(typeof require==="function"&&typeof module!=="undefined"&&require.main===module){
 const fs=require("node:fs");
 try{
  need(process.argv.length===4,"usage: node FILE.js COMPLETED_JOB_LOG EXPECTED_RUN_ID");
  process.stdout.write(JSON.stringify(auditQuintic259Log(fs.readFileSync(process.argv[2],"utf8"),process.argv[3]))+"\n");
 }catch(e){process.stdout.write(JSON.stringify({format:AUDIT_FORMAT,status:"failed",error:{type:e.name,message:e.message}})+"\n");process.exitCode=1;}
}
