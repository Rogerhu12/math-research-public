/* Original mixed95 completed-job log audit.
 * Author: Astra-ISP-789f / normal_annihilator, with /root.
 * AI-assisted: GPT-6 Astra Pro. 2026-11-16.
 * No matrix arithmetic is repeated. Producer product flags are checked as
 * executed evidence; original mathematical products are not relabelled as ours.
 * Usage: node FILE.js COMPLETED_JOB_LOG EXPECTED_RUN_ID
 * Pure V8: Function(source+";return auditMixed95Log;")()(log,runId).
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
const AUDIT_FORMAT="r150-original-koszul55-mixed95-completed-log-audit-v1";
const STEP_ID="original-koszul55-mixed95-unit60";
const MATH_FORMAT="r150-original-koszul55-mixed95-source-unit127-v1";
const SOURCE={"path":"2026-11-16-r150-original-koszul55-mixed95-source-unit127-789f.py","bytes":16461,"sha256":"fc1dfea5219a773af1140c3c9e8ba52bcb6acfd36ae67bd325c9317e416d0ab5"};
const PARENT={"format":"r150-original-quartic-syzygy95-small-field-gate127-v1","binding":"9f0ee10f7e4cece784d8140d063f94c210105e7dded9f811710d6ec6f2825fa1","source":{"bytes":15520,"path":"2026-11-16-r150-original-quartic-syzygy95-small-field-gate127-789f.py","sha256":"b6f72e376aa403ff540a01927ea0dd4ac136099cb7be16fe201f91e95968cc4c"},"phases":{"complete-original-quartic95-unit":{"bytes":20816,"logicalBytes":63121,"logicalSha256":"b711688351ce47161d8e898f1322a2e4e0c355bf8d7033d7a6bb2884a95343eb","path":"complete-original-quartic95-unit.json.gz","sha256":"71d679b394ab9c58f542c576690397d8f1cbcba627d74daffd72f9bbb2e3302e"},"whole-original-quartic95-input":{"bytes":16730,"logicalBytes":95934,"logicalSha256":"bf86bf186cd64d3ed78e0bf66b794bca62aa72e71abd3de3335e905c7cea0589","path":"whole-original-quartic95-input.json.gz","sha256":"a2d91336495f29ff2a15958ab26cf2cefcb782eb2e7acac2c88d90fb91a2de07"}},"manifest":{"path":"original-quartic95-manifest.json","bytes":901,"sha256":"11ad47693c39437e3f7d4711a84817e87d96392886802471116da34e1f79dacc"}};
const OBSERVER={path:"2026-11-16-r150-exact-low20-observed-execution-789f.py",bytes:5855,
 sha256:"c5d5f777246dbb99d516855eb007845c9b25673cfe736e74cf56f559111a5618"};
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
function auditMixed95Log(log,expectedRunId){
 need(typeof log==="string"&&/^[0-9]+$/.test(String(expectedRunId)),"complete job text and explicit run id");
 const record=selectRecord(log,expectedRunId,STEP_ID),o=record.obj,r=o.result,p=r&&r.parameters;
 need(o.format==="isp-temporary-research-step-source-parameters-run-sha256-v1","original manifest-only execution format");
 need(o.exitCode===0&&o.receiptUnchangedFromBeforeStep===false&&o.preexistingReceipt===null,"fresh actual successful execution");
 need(o.largeDataUploadedOrCommitted===false&&o.summaryExcludesRecomputableArraysOnly===false,"complete small actual receipt, no array uploads");
 need(typeof o.python==="string"&&/^3\.12\.14(?:\s|$)/.test(o.python)&&o.pythonFlint==="0.9.0","exact original runtime");
 need(o.script==="topics/invariant-subspace-problem/notes/"+OBSERVER.path&&o.scriptSHA256===OBSERVER.sha256,"original observer source");
 const ex=o.observerExecution;
 need(ex&&same(ex.source,SOURCE)&&same(ex.observer,OBSERVER)&&ex.status==="completed"&&
      ex.childReturnCode===0&&ex.shellEquivalentExitCode===0&&ex.terminationRequestedByObserver===false&&
      ex.unobservedTerminationCauseInferred===false&&ex.outerSeconds===120&&ex.heartbeatSeconds===10,
      "actual original observer, child source and clean completion");
 need(/^[0-9a-f]{40}$/.test(o.executionSourceCommit)&&o.lastRulesReadCommit===o.executionSourceCommit,
      "actual execution commit and last real rules read");
 need(Array.isArray(o.pinnedSupportSources)&&o.pinnedSupportSources.some(x=>x.path.endsWith("/"+SOURCE.path)&&x.sha256===SOURCE.sha256)&&
      o.pinnedSupportSources.some(x=>x.path.endsWith("/"+PARENT.source.path)&&x.sha256===PARENT.source.sha256),
      "complete mathematics and parent source pins");
 const argv=o.argvTemplate,cut=argv.indexOf("--");
 need(cut>=0,"observer separator");
 const expected=["python","{scripts}/"+SOURCE.path,"--parent-source","{scripts}/"+PARENT.source.path,
  "--parent-out","{work}/original-quartic-syzygy95-small-gate127",
  "--out","{work}/original-koszul55-mixed95-unit127","--seconds","60","--memory-mib","512"];
 need(same(argv.slice(cut+1),expected),"exact mathematics CLI and resource scope");
 need(r&&r.format===MATH_FORMAT&&r.status==="completed"&&p&&p.exitCode===0&&p.seconds===60&&p.memoryMiB===512,
      "actual completed mathematical receipt");
 const lowIds=[];for(let j=0;j<4;j++)for(let k=1;k<=5;k++)lowIds.push(10*j+k);
 const m2=mons(5,2),labels=[];
 for(let g=0;g<11;g++)for(const e of m2)labels.push([g,e]);
 const klabels=[];for(let a=0;a<11;a++)for(let b=a+1;b<11;b++)klabels.push([a,b]);
 const tlabels=[];for(let ell=0;ell<5;ell++)for(let s=0;s<20;s++)tlabels.push([ell,s]);
 const sem=p.semantic;
 need(sem&&same(sem.source,SOURCE)&&same(sem.parent,PARENT)&&sem.prime===127&&sem.root===100,"same original parent and coefficient place");
 sortedUniqueIds(sem.actualOriginalUnitRows,95,165,"all actual original95 row labels");
 const expectedSem={format:MATH_FORMAT,source:SOURCE,parent:PARENT,prime:127,root:100,
  originalQuarticSourceLabels:labels,actualOriginalUnitRows:sem.actualOriginalUnitRows,
  koszulSourceLabels:klabels,allOriginalMultipliedLabels:tlabels,selectedLowSeedIds:lowIds,
  selectionRule:"original55 Koszul columns first, then original100 multiplied-low columns in their paid order"};
 need(same(sem,expectedSem)&&sha256(canon(expectedSem))===r.binding,"independent complete original dictionaries and semantic binding");
 need(same(p.original55KoszulLabels,klabels)&&same(p.actualOriginalUnitRows,sem.actualOriginalUnitRows),"duplicated result original dictionaries");
 const chosen=p.selectedOriginalMultipliedColumnIds;
 sortedUniqueIds(chosen,40,100,"actual forty original multiplied-low columns");
 need(same(p.selectedOriginalMultipliedLabels,chosen.map(j=>tlabels[j]))&&
      same(p.selectedOriginalLowSeedLabels,chosen.map(j=>{const [ell,s]=tlabels[j];return[ell,lowIds[s]];})),
      "all forty literal source labels without relabeling");
 const pc=Array.from({length:55},(_,i)=>i).concat(chosen.map(j=>55+j));
 need(same(pc,p.originalMixedPivotColumns),"all55 initial Koszul pivots and40 actual original T pivots");
 need(p.koszulRank===55&&p.mixedRank===95&&p.koszulQuotientDimension===40&&
      Number.isSafeInteger(p.mixedOriginal95UnitDeterminant127)&&0<p.mixedOriginal95UnitDeterminant127&&p.mixedOriginal95UnitDeterminant127<127,
      "actual mixed unit and exact dimension scope");
 const gates=["all11550OriginalQuarticCoordinatesReconstructed","all16500OriginalMultipliedCoordinatesReconstructed",
  "all3850OriginalKoszulProductsVerified","all18050MixedInverseProductsVerified",
  "all25575OriginalFullSourceCoordinatesVerified","all9025SelectedMixedIdentityCoordinatesVerified",
  "all3800SelectedFortyIdentityCoordinatesVerified"];
 for(const k of gates)need(p[k]===true,"actual producer complete product gate "+k);
 for(const k of ["parentRank95Repeated","parameterMatricesConstructed","exactECoordinateArraysComputed",
                 "BellMembershipClaimed","originalParameterMatricesConstructed","newBellMembershipConclusion",
                 "interruptedExactConstantsStageClaimedComplete"])
  need(p[k]===false,"actual restricted scope "+k);
 need(p.conditionalOriginalEGradientGeneratorBound===200&&p.conditionalOriginalEBellGeneratorBound===210,
      "same original theorem consequence, no new materialized parameter presentation");
 const name="complete-original-koszul55-mixed95-unit",ph=p.completePhases;
 need(ph&&same(Object.keys(ph),[name]),"one complete transactional phase");
 descriptor(ph[name],name+".json.gz");
 need(same(p.completePhase,ph[name])&&p.lastEvent===name,"whole final phase referenced consistently");
 const raw=reconstructedRaw(record,SOURCE);
 need(bytes(raw)===o.fullTemporaryReceiptBytes&&sha256(raw)===o.fullTemporaryReceiptSHA256,
      "whole original raw canonical bytes and SHA, preserving Python numeric lexemes");
 const manifest=canon({format:MATH_FORMAT+"-manifest",binding:r.binding,source:SOURCE,phases:ph});
 return{format:AUDIT_FORMAT,status:"completed",runId:String(expectedRunId),stepId:STEP_ID,
  executionSourceCommit:o.executionSourceCommit,jobLog:{bytes:bytes(log),sha256:sha256(log)},
  raw:{bytes:bytes(raw),sha256:sha256(raw)},binding:r.binding,source:SOURCE,
  actualOriginalUnitRows:sem.actualOriginalUnitRows,actualSelectedOriginalMultipliedColumnIds:chosen,
  actualSelectedOriginalLowSeedLabels:p.selectedOriginalLowSeedLabels,
  mixedUnitDeterminant127:p.mixedOriginal95UnitDeterminant127,
  completePhases:ph,reconstructedManifest:{bytes:bytes(manifest),sha256:sha256(manifest),physicalFileIndependentlyRead:false},
  allOriginalDictionaryLabelsReconstructed:true,allLiteralSourceLabelsChecked:true,
  allRawCanonicalBytesMatched:true,allActualProducerProductFlagsTrue:true,
  matrixProductsRepeatedByThisAudit:false,phasePayloadArraysReadByThisAudit:false,
  producerProductCoordinates:{D:11550,T:16500,K:3850,inverses:18050,all155:25575,selected95:9025,selected40:3800},
  exactECoordinateArraysClaimed:false,newBellIdentityClaimed:false,
  actualMathematicalSeconds:p.elapsedSeconds,actualObserverSeconds:ex.elapsedSeconds,actualOuterSeconds:o.wallSeconds};
}
if(typeof module!=="undefined")module.exports={auditMixed95Log,losslessJSON,plain,canon,selectRecord,reconstructedRaw,sha256};
if(typeof require==="function"&&typeof module!=="undefined"&&require.main===module){
 const fs=require("node:fs");
 try{
  need(process.argv.length===4,"usage: node FILE.js COMPLETED_JOB_LOG EXPECTED_RUN_ID");
  const result=auditMixed95Log(fs.readFileSync(process.argv[2],"utf8"),process.argv[3]);
  process.stdout.write(JSON.stringify(result)+"\n");
 }catch(e){process.stdout.write(JSON.stringify({format:AUDIT_FORMAT,status:"failed",error:{type:e.name,message:e.message}})+"\n");process.exitCode=1;}
}
