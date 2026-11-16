// Exact completed-job audit; source and identities only, no raw fixtures.
// Astra-ISP-789f, 2026-11-16. Inputs remain temporary completed-job logs.
function utf8(s){const a=[];for(const c of s){const v=c.codePointAt(0);if(v<128)a.push(v);else if(v<2048)a.push(192|(v>>6),128|(v&63));else if(v<65536)a.push(224|(v>>12),128|((v>>6)&63),128|(v&63));else a.push(240|(v>>18),128|((v>>12)&63),128|((v>>6)&63),128|(v&63));}return Uint8Array.from(a);}
function sha256(s){const a=typeof s==="string"?utf8(s):s;const n=a.length,b=new Uint8Array(Math.ceil((n+9)/64)*64);b.set(a);b[n]=128;const hi=Math.floor(n/536870912),lo=(n*8)>>>0;for(let i=0;i<4;i++){b[b.length-8+i]=(hi>>>(24-8*i))&255;b[b.length-4+i]=(lo>>>(24-8*i))&255;}
const K=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
const H=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19],w=new Int32Array(64),ro=(x,k)=>(x>>>k)|(x<<(32-k));
for(let off=0;off<b.length;off+=64){for(let i=0;i<16;i++)w[i]=(b[off+4*i]<<24)|(b[off+4*i+1]<<16)|(b[off+4*i+2]<<8)|b[off+4*i+3];for(let i=16;i<64;i++){const x=w[i-15],y=w[i-2];w[i]=(w[i-16]+(ro(x,7)^ro(x,18)^(x>>>3))+w[i-7]+(ro(y,17)^ro(y,19)^(y>>>10)))|0;}let[a0,b0,c,d,e,f,g,h]=H;for(let i=0;i<64;i++){const t1=(h+(ro(e,6)^ro(e,11)^ro(e,25))+((e&f)^((~e)&g))+K[i]+w[i])|0,t2=((ro(a0,2)^ro(a0,13)^ro(a0,22))+((a0&b0)^(a0&c)^(b0&c)))|0;h=g;g=f;f=e;e=(d+t1)|0;d=c;c=b0;b0=a0;a0=(t1+t2)|0;}const v=[a0,b0,c,d,e,f,g,h];for(let i=0;i<8;i++)H[i]=(H[i]+v[i])>>>0;}
return H.map(x=>x.toString(16).padStart(8,"0")).join("");}
class JsonNumber{constructor(text){this.text=text;}}
function parseLossless(s){let p=0;const ws=()=>{while(/\s/.test(s[p]||"")&&p<s.length)p++;};function str(){const st=p++;while(p<s.length){const c=s[p++];if(c==="\\"){p++;continue;}if(c==='"')return JSON.parse(s.slice(st,p));}throw Error("unterminated string");}function val(){ws();const c=s[p];if(c==='"')return str();if(c==="{"){p++;const o=Object.create(null);ws();if(s[p]==="}"){p++;return o;}for(;;){ws();if(s[p]!=='"')throw Error("object key");const k=str();if(Object.hasOwn(o,k))throw Error("duplicate key");ws();if(s[p++]!==":")throw Error("colon");o[k]=val();ws();const e=s[p++];if(e==="}")return o;if(e!==",")throw Error("object comma");}}if(c==="["){p++;const a=[];ws();if(s[p]==="]"){p++;return a;}for(;;){a.push(val());ws();const e=s[p++];if(e==="]")return a;if(e!==",")throw Error("array comma");}}for(const [lit,x]of[["true",true],["false",false],["null",null]])if(s.startsWith(lit,p)){p+=lit.length;return x;}const m=s.slice(p).match(/^-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?/);if(!m)throw Error("JSON token at "+p);p+=m[0].length;return new JsonNumber(m[0]);}const out=val();ws();if(p!==s.length)throw Error("trailing JSON");return out;}
function canonicalLossless(x){if(x instanceof JsonNumber)return x.text;if(x===null)return"null";if(typeof x==="string")return JSON.stringify(x).replace(/[\u007f-\uffff]/g,c=>"\\u"+c.charCodeAt(0).toString(16).padStart(4,"0"));if(typeof x==="boolean"||typeof x==="number")return JSON.stringify(x);if(Array.isArray(x))return"["+x.map(canonicalLossless).join(",")+"]";return"{"+Object.keys(x).sort().map(k=>canonicalLossless(k)+":"+canonicalLossless(x[k])).join(",")+"}";}
function ordinaryLossless(x){if(x instanceof JsonNumber)return Number(x.text);if(Array.isArray(x))return x.map(ordinaryLossless);if(x&&typeof x==="object")return Object.fromEntries(Object.entries(x).map(([k,v])=>[k,ordinaryLossless(v)]));return x;}

function auditWeightTenJob(log,src){
 const need=(v,s)=>{if(!v)throw Error(s);},eq=(a,b)=>canonicalLossless(a)===canonicalLossless(b);
 const logID={bytes:utf8(log).length,sha256:sha256(log)};
 need(logID.bytes===241308&&logID.sha256==="89b03db9de9caee0a5739e7393fc459acb5a656aa3fa4fb9be73b32e0b4fcee1","whole decoded completed log");
 const own={path:"2026-11-16-r150-original-delta-weight10-runtime-parent127-789f.py",bytes:40746,sha256:"433e8942e30cde475bd6e7f13df43b4a6765a876dac495553de5fe6a53fd001f"};
 need(utf8(src).length===own.bytes&&sha256(src)===own.sha256,"whole frozen runtime-parent source");
 const get=k=>{const m=src.match(new RegExp("^"+k+"=(.+)$","m"));need(m,"source constant "+k);return JSON.parse(m[1]);};
 const ids=["original-ten-parameter-model116-180","original-parameter-seed-compression50-180","original-mean-first30-final180","original-weight8-complete-prepare180","original-weight8-complete-final180","original-complete210-all-sources900","original-delta-weight10-prepare600","original-delta-weight10-candidate600"];
 const hashes=[get("MODEL_SHA"),"b1d3dbedd597a8019bab2dca6ff59bfa915aaa457a8ac0c14833266f449a1ee9","810904a2c797b08493ed377c069abd75018e0a0df8035cb700baad80616bea1e","bf5fa8e6ea1a70ed9441cf28918c9bd46946661afd932c7888f713dc2eadc936","bf5fa8e6ea1a70ed9441cf28918c9bd46946661afd932c7888f713dc2eadc936",get("PRODUCER_SHA"),own.sha256,own.sha256];
 const bindings=[get("MODEL_BINDING"),"baaa8ec3f9459c0d2f88ebb452c941ce241f2727d5becab1ca78511a55a589ca","9502b11bf94390e8833cdc236a1ad85746d9823f9f4fe1e62de60f1932434bfd","1fdb39f00f53e51f33cbecef6c25c503c43e85575ad79abbd189ade9fdc7d069","1fdb39f00f53e51f33cbecef6c25c503c43e85575ad79abbd189ade9fdc7d069",get("PARENT_BINDING"),"74fe3018557e728ba1124dce22c134e1b7a43c9bc1cba732df47d6d7c83c2fbc","74fe3018557e728ba1124dce22c134e1b7a43c9bc1cba732df47d6d7c83c2fbc"];
 const texts=log.split("\n").flatMap(l=>{const k=l.indexOf("ISP_REMOTE_STEP ");return k<0?[]:[l.slice(k+16).trim()];}),steps=texts.map(JSON.parse);
 need(steps.length===8,"exactly eight actual attempts");
 for(let i=0;i<8;i++){const a=steps[i];need(a.runId==="43906283833"&&a.stepId===ids[i]&&a.exitCode===(i===7?75:0)&&a.scriptSHA256===hashes[i]&&a.result.binding===bindings[i],"actual ordered source/exit/binding "+i);need(a.python.startsWith("3.12.14 ")&&a.pythonFlint==="0.9.0","exact Python/flint");need(a.largeDataUploadedOrCommitted===false,"no large upload");need(a.summaryExcludesRecomputableArraysOnly===(i===4),"precise known log compaction scope");}
 const omitted=steps[4].result.serializedArrayIdentities;
 need(omitted.length===1&&omitted[0].field==="parameters.completePhases"&&omitted[0].logicalJsonBytes===51711&&omitted[0].logicalJsonSHA256==="3f24f051b3b617dbc21bfec0f6c1582bf4f6a448933528c2694bcc32e0241b06"&&omitted[0].itemCount===201,"only weight8 phase-description list omitted, retained as identity");
 const gates=[
 ["all116OriginalSeedsVerified","all11OriginalGeneratorsInBorderSubmodule","all17GradientTransportProducts","all34CoordinateInverseProducts","all50OriginalBorderProducts","all578JacobianProducts","allSixMeanProducts","sameOriginal17GradientsRetained"],
 ["all1160ModuleCoordinatesVerified","allDeletedOriginal18ProductsVerified","sameCompleteOriginalFiniteFieldParameterSubmodule"],
 ["all30CompleteParameterRelationsVerified","all30Original18ProductsVerified","all30Original18RelationProductsVerified","all50OriginalMultiplicationProductsVerified"],
 ["all100Original18ProductsVerified","all30ParentMeanOriginal18ProductsVerified","all40ParentOriginal18ProductsVerified","all50OriginalMultiplicationProductsVerified"],
 ["all100CompleteParameterRelationsVerified","all100Original18ProductsVerified","all100Original18RelationProductsVerified","all30ParentMeanOriginal18ProductsVerified","all40ParentOriginal18ProductsVerified","all50OriginalMultiplicationProductsVerified"],
 ["all104NewOriginal18ProductsVerified","all104TenVectorsVerified","all106OriginalParentColumnsVerified","all210OriginalSourcesVerified"]];
 for(let i=0;i<6;i++)for(const k of gates[i])need(steps[i].result.parameters[k]===true,"reported complete original gate "+i+"/"+k);
 const w8=steps[4].result.parameters;
 need(steps[2].result.parameters.actualRank===312&&steps[2].result.parameters.keptNewCount===30,"whole mean frontier");
 need(w8.actualRank===1312&&w8.oldRank===1106&&w8.prefixRank===1286&&w8.keptNewCount===26&&w8.deletedNewCount===74,"whole weight8 frontier");
 const pp=steps[5].result.parameters;
 need(pp.all106OriginalProductsThisRun===106&&pp.newOriginal18ProductsThisRun===104,"all original210 products");
 need(pp.manifest.bytes===get("PARENT_MANIFEST").bytes&&pp.manifest.sha256===get("PARENT_MANIFEST").sha256&&eq(pp.completeModel,get("PARENT_FINAL")),"exact paid complete210 mathematical manifest and stored/logical phase");
 const reconstructed=[];
 for(let i=6;i<8;i++){
  const a=steps[i],r=parseLossless(texts[i]).result;delete r.events;r.source=own;
  // Python's original Counter has integer keys. sort_keys orders these
  // numerically before encoding them as JSON strings; a JSON reload loses that.
  const w=r.parameters.inputWeightCounts,ow="{"+Object.keys(w).sort((a,b)=>+a-+b).map(k=>canonicalLossless(k)+":"+canonicalLossless(w[k])).join(",")+"}";
  const raw=canonicalLossless(r).replace('"inputWeightCounts":'+canonicalLossless(w),'"inputWeightCounts":'+ow),rid={stepId:a.stepId,bytes:utf8(raw).length,sha256:sha256(raw)};
  need(rid.bytes===a.fullTemporaryReceiptBytes&&rid.sha256===a.fullTemporaryReceiptSHA256,"all reconstructed original temporary receipt bytes "+i);reconstructed.push(rid);
  const p=a.result.parameters;
  for(const k of ["all17OriginalTransportsRechecked","all200OriginalSourceProductsInheritedFromCompleteParent","all200OriginalSourceWeightsVerified","all24MeanCoordinatesRechecked","allCompletedOriginalParentHashesVerified","bothLiteralAdjugatesRechecked"])need(p[k]===true,"complete child source gate "+k);
  need(p.originalInputColumns===200&&p.completePreparedColumns===200&&p.originalInputTerms===8037189&&p.originalASCIITotalBytes===151071880&&p.targetTerms===2604,"complete original input");
  need(eq(p.inputWeightCounts,{"5":6,"6":20,"7":30,"8":40,"9":24,"10":80}),"all source weights");
  need(p.actualParentReceipt.bytes===steps[5].fullTemporaryReceiptBytes&&p.actualParentReceipt.sha256===steps[5].fullTemporaryReceiptSHA256&&p.paidHistoricalParentReceiptByteMatch===false,"new actual parent metadata bound separately");
  need(p.characteristicZeroConclusion===false&&p.originalIdealNonmembershipClaimed===false&&p.positiveOriginalSourceClaimed===false,"no mathematical target conclusion");
  need(Object.values(p.independentTinyControls).every(x=>x===true),"all independent tiny controls");
 }
 const p=steps[7].result.parameters;
 const sem={format:get("FORMAT"),source:own,prime:127,coefficientRoot:100,modelSourceSHA256:get("MODEL_SHA"),chartSourceSHA256:get("CHART_SHA"),producerSourceSHA256:get("PRODUCER_SHA"),verifierSourceSHA256:get("VERIFIER_SHA"),parentFormat:get("PARENT_FORMAT"),parentBinding:get("PARENT_BINDING"),parentManifest:get("PARENT_MANIFEST"),parentReceipt:p.actualParentReceipt,paidHistoricalParentReceipt:get("PARENT_RECEIPT"),parentFinalPhase:get("PARENT_FINAL"),literalTarget:"delta14*b^2*e0",deltaSHA256:get("DELTA_SHA"),originalMeanRows:[2,3,4,5],originalNonBellColumns:200,targetWeight:10,rowShifts:[0,2,2,2,2,2,4,4,4,4],variableWeights:[1,1,1,1,1,1,2,2,2,2,2,2,1],ordering:"wp(1,1,1,1,1,1,2,2,2,2,2,2,1),C",candidateEngine:"std, degBound=10",negativeGate:src.match(/"negativeGate":"([^"]*)"/)[1],positiveGate:src.match(/"positiveGate":"([^"]*)"/)[1],characteristicZeroConclusion:false,maxCandidateColumns:65536,maxSSIBytes:1073741824};
 need(sha256(canonicalLossless(sem))===steps[7].result.binding,"whole actual semantic binding");
 need(log.includes("Singular for x86_64-Linux version 4.4.1 (44105, 64 bit)"),"actual installed Singular version");
 need(p.stages.length===3,"exact actual engine-stage count");
 for(let i=0;i<2;i++)need(p.stages[i].exitCode===0&&!p.stages[i].budget,"actual completed engine control or materialization");
 need(eq(p.stages[0].markers,["@@SHIFTED-ENGINE-CONTROL-COMPLETE"])&&eq(p.stages[1].markers,["@@ALL-ORIGINAL2000-SSI-COORDINATES"]),"all real engine controls and original2000 coordinates");
 const c=p.stages[2];need(c.name==="bounded-homogeneous-candidate"&&c.budget===true&&c.status==="budget"&&eq(c.markers,["@@WEIGHT10-CANDIDATE-START"]),"only candidate START returned");
 need(steps[7].result.status==="budget-checkpoint"&&p.error.type==="Budget"&&p.candidateAbsentNoEmptyRetry&&p.continuationEligible===false&&p.completeParsedCandidateColumns===0,"honest empty-candidate budget stop");
 need(!log.includes("ISP_WHOLE_PREFIX_RESUME "),"no empty replay");
 need(log.includes("missing=['original-delta-weight10-complete-check600'] failed=['original-delta-weight10-candidate600']"),"final validation not run");
 return {format:"r150-weight10-completed-job-log-audit-v1",runId:43906283833,jobId:133435910806,logIdentity:logID,sourceIdentity:own,actualStages:8,allFrozenSourceAndParentBindingsVerified:true,allReportedParentArithmeticGatesRead:true,omittedWeight8PhaseListRetainedOnlyAsIdentity:omitted[0],original200InputsVerified:true,reconstructedReceipts:reconstructed,semanticBytes:utf8(canonicalLossless(sem)).length,actualBinding:steps[7].result.binding,actualEngineControlsAnd2000SSIProductsVerified:true,candidateCompleted:false,independentSPairOrTargetVerificationRun:false,emptyRetryPerformed:false,mathematicalMembershipConclusion:false,rawArraysOrLogPersistedInGit:false};
}
if(typeof module!=="undefined"&&module.exports){module.exports={auditWeightTenJob};if(require.main===module){const fs=require("fs");if(process.argv.length!==4)throw Error("usage: node audit.js completed-job.log frozen-runtime-parent.py");process.stdout.write(JSON.stringify(auditWeightTenJob(fs.readFileSync(process.argv[2],"utf8"),fs.readFileSync(process.argv[3],"utf8")),null,2)+"\n");}}
