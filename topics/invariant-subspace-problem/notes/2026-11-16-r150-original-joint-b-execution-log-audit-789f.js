// Author: Astra-ISP-789f / root. AI-assisted GPT-6 Astra Pro.
// Date: 2026-11-16. Read-only: no mathematical arrays are written.
// Usage: node this-file.js /path/to/complete-actions-job.log
function auditOriginalJointBExecution(log, hashBytes) {
function auditExactExecutionLog(log, hashBytes, restoredFields = {}) {
  const need=(v,m)=>{if(!v)throw Error(m);};
  const utf=s=>Array.from(unescape(encodeURIComponent(s)),c=>c.charCodeAt(0));
  function parse(s){let i=0;const ws=()=>{while(/\s/.test(s[i]||"")&&i<s.length)i++;};
    function get(){ws();let c=s[i];
      if(c==="{"){i++;let v={};ws();if(s[i]==="}"){i++;return {t:"o",v};}
        for(;;){ws();const k=get();need(k.t==="s","object key");ws();need(s[i++]===":","colon");v[k.v]=get();ws();c=s[i++];if(c==="}")break;need(c===",","object comma");}return {t:"o",v};}
      if(c==="["){i++;let v=[];ws();if(s[i]==="]"){i++;return {t:"a",v};}for(;;){v.push(get());ws();c=s[i++];if(c==="]")break;need(c===",","array comma");}return {t:"a",v};}
      if(c==='"'){const start=i++;for(;;){need(i<s.length,"string end");c=s[i++];if(c==="\\"){i++;continue;}if(c==='"')break;}return {t:"s",v:JSON.parse(s.slice(start,i))};}
      const r=s.slice(i).match(/^(?:-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?|true|false|null)/);need(r,"JSON token "+i);i+=r[0].length;return {t:"n",v:r[0]};
    }
    const a=get();ws();need(i===s.length,"trailing JSON");return a;
  }
  const quote=s=>JSON.stringify(s).replace(/[\u0080-\uffff]/g,c=>"\\u"+c.charCodeAt(0).toString(16).padStart(4,"0"));
  function serial(n,pretty=false,depth=0){
    if(n.t==="s")return quote(n.v);if(n.t==="n")return n.v;
    const arr=n.t==="a",keys=arr?n.v.map((v,i)=>i):Object.keys(n.v).sort(),open=arr?"[":"{",close=arr?"]":"}";
    if(!keys.length)return open+close;
    const items=keys.map(k=>(arr?"":quote(k)+(pretty?": ":":"))+serial(n.v[k],pretty,depth+1));
    return pretty?open+"\n"+"  ".repeat(depth+1)+items.join(",\n"+"  ".repeat(depth+1))+"\n"+"  ".repeat(depth)+close:open+items.join(",")+close;
  }
  const steps=[];
  for(const line of log.split("\n")){
    const ix=line.indexOf("ISP_REMOTE_STEP ");if(ix<0)continue;
    const json=line.slice(ix+16),parsed=JSON.parse(json),ast=parse(json),r=ast.v.result;
    need(r?.t==="o","complete result object");
    for(const [key,value] of Object.entries(restoredFields[parsed.stepId]||{})) {need(!r.v[key],"restored field already exists");r.v[key]=parse(JSON.stringify(value));}
    const options=[r];if(r.v.events){const v={...r.v};delete v.events;options.push({t:"o",v});}
    const found=[];
    for(let oi=0;oi<options.length;oi++)for(const pretty of [false,true])for(const newline of [false,true]){
      const raw=serial(options[oi],pretty)+(newline?"\n":"");
      if(utf(raw).length!==parsed.fullTemporaryReceiptBytes)continue;
      const h=hashBytes(utf(raw));if(h===parsed.fullTemporaryReceiptSHA256)found.push({wrapperEventsRemoved:oi===1,pretty,newline,bytes:utf(raw).length,sha256:h});
    }
    need(found.length>0,"raw receipt identity "+parsed.stepId);
    let bindingVerified=null;
    const semantic=r.v.parameters?.v.inputIdentity;
    if(semantic){const h=hashBytes(utf(serial(semantic)+"\n"));need(h===parsed.result.binding,"original semantic binding "+parsed.stepId);bindingVerified=true;}
    steps.push({stepId:parsed.stepId,exitCode:parsed.exitCode,receipt:found[0],bindingVerified,restoredProducerFields:Object.keys(restoredFields[parsed.stepId]||{})});
  }
  need(steps.length>0,"actual step records");
  return {format:"isp-independent-lossless-raw-receipt-audit-v1",allRawBytesAndSHA256Verified:true,steps};
}

  const need=(v,m)=>{if(!v)throw Error(m);};
  const all=log.split("\n").filter(l=>l.includes("ISP_REMOTE_STEP ")).map(l=>JSON.parse(l.slice(l.indexOf("ISP_REMOTE_STEP ")+16)));
  const ids=["rebuild-selected-true16-original-p9-through35","complete-original-joint-b-structure-p9"];
  const selected=ids.map(id=>{const a=all.filter(s=>s.stepId===id);need(a.length===1,"unique actual mathematical step "+id);return a[0];});
  for(const s of selected)need(s.exitCode===0&&s.result.status==="completed","actual complete original execution");
  need(selected[0].scriptSHA256==="e4b2b935882e899a55d7db10d590e5ce8d35f5fedcab6063a14008a5efe4b69e","original selected p9 source");
  need(selected[1].scriptSHA256==="76308b437da77f3aef3c25390a197af2af0f4d485129d8e6ee9d1431d080fee3","original joint B source");
  const actual=log.split("\n").filter(l=>l.includes("ISP_REMOTE_STEP ")&&ids.some(id=>l.includes('"stepId": "'+id+'"'))).join("\n");
  const rawAudit=auditExactExecutionLog(actual,hashBytes);
  need(rawAudit.steps.length===2&&rawAudit.steps.every(x=>x.bindingVerified===true),"both complete original semantic bindings");
  const sel=selected[0].result.parameters,p=selected[1].result.parameters;
  let stages=0,integer=0,unit=0,unlocked=0;
  for(const q of [sel,p])for(const [name,x] of Object.entries(q.stages)){
    need(x.status==="completed"&&x.exitCode===0,"stage "+name);
    need(/^[a-f0-9]{64}$/.test(x.inputBinding),"stage binding "+name);
    for(const[k,v]of Object.entries(x.statistics||{}))
      if(/^(all|fullOriginal|residualIs|sameOriginal)/.test(k)&&typeof v==="boolean"){
        if(k==="allLockedSourceCoefficientsRetained"){
          need(v===(x.statistics.lockedPrefixLength>0),"declared exact lock scope "+name);if(!v)unlocked++;
        }else need(v,"native full-product gate "+name+" "+k);
      }
    if(x.statistics?.allOriginal17CoefficientsDivisible)integer++;
    if(x.statistics?.fullOriginalGIdentityVerified)unit++;
    stages++;
  }
  need(stages===96,"all 30 parent and 66 consumer stages");
  let classes=0;
  for(const[k,x]of Object.entries(p.classes)){
    for(const q of["all104LocalFreeChecks","all315OriginalCoordinateReconstruction","all505GlobalFreeChecks","sameOriginalSAction","rootTwoPrimaryProjectionExplicit"])
      need(x[q]===true,"complete original class "+k+" "+q);
    classes++;
  }
  need(classes===17,"all complete class gates");
  const cc=Object.entries(p.coordinateChecks);need(cc.length===9,"three high and six low complete coordinate stages");
  for(const[k,x]of cc){
    need(x.all315ProductsVerified,"all315 products "+k);
    need(x.basis.sha256===p.actualRootTwoBasis.matrix.sha256,"same actual root-two basis "+k);
  }
  for(let k=0;k<6;k++)need(p.coordinateChecks["low-r"+k].provedOrderUpperBound===k+2,"true low-order support "+k);
  const tt=Object.entries(p.explicitParentTransports);need(tt.length===6,"G V and four original source families");
  for(const[k,x]of tt)need(x.allMathematicalPayloadBytesIdentical,"complete unchanged source payload "+k);
  const f=p.final,K=f.Hp2PlusLow.exponents,H2=f.Hp2.exponents;
  need(JSON.stringify(H2)==="[2,2,2,2]","true high two-torsion");
  // The separately proved actual H direct summand implies
  // K=H[p^2] direct-sum B_low. Subtract these exact types independently.
  const n2=K.filter(x=>x===2).length-H2.length,n1=K.filter(x=>x===1).length;
  need(n1>=0&&n2>=0,"actual low multiplicities");
  need(n2===f.lowExponentTwoMultiplicity&&n1===f.lowExponentOneMultiplicity,"independent low direct-complement calculation");
  const ex=[...Array(n1).fill(1),...Array(n2).fill(2),3,4,4,5].sort((a,b)=>a-b);
  need(JSON.stringify(ex)===JSON.stringify(f.completeDInvariantExponents),"complete D type");
  need(ex.reduce((a,b)=>a+b,0)===f.jointLength&&ex.length===f.minimumDGenerators,"length and D generators");
  need(ex.length-f.xRankOnLowQuotientModuloP===f.minimumDPolynomialGenerators,"local-ring minimum generators");
  for(const key of ["p2B","p3B","Hp2","Hp2PlusLow","xB","pXB"]){
    const a=f[key];need(a.allOriginalSmallProductsVerified&&a.bothTransformationsDUnits,key+" exact finite Smith products");
    need(a.exponents.reduce((x,y)=>x+y,0)===a.length&&a.minimumDGenerators===a.exponents.length,key+" exact sizes");
  }
  need(f.individualOriginalCyclicChecks.length===9,"all original individual modules");
  for(const x of f.individualOriginalCyclicChecks)need(x.length===7&&JSON.stringify(x.exponents)==="[2,5]","individual original target "+x.label);
  for(const key of ["all104LocalFreeAnd315CoordinateAnd505GlobalFreeChecks","allHighRelationsVerifiedModuloTheirFullPowers","allHigherOrderDigitSupportsChecked","allOriginal6188SourceRowsAnd4367OutputRowsRetained","allSixLowDigitsActuallyComputed","bothMinimumGeneratorCountsIndependentlyVerified","completePresentationAndXStabilityVerified","lastRemainderKilledByPaidFullP6T","rootOneAbsenceUsesPaidXSquareBZero","rootTwoCompletionUsedThroughout"])
    need(f[key]===true,"final original source gate "+key);
  return {
    format:"r150-independent-original-joint-b-execution-log-audit-v1",
    runId:selected[1].runId,rawAudit,allNativeStages:stages,integerProductStages:integer,
    fullUnitSourceSolveStages:unit,explicitlyUnlockedSourceSolves:unlocked,
    all104315505Classes:classes,allCompleteCarryCoordinateStages:cc.length,
    completeParentPayloadTransports:tt.length,derivedLowMultiplicities:[n1,n2],
    derivedDExponents:ex,length:f.jointLength,minimumDGenerators:f.minimumDGenerators,
    minimumPolynomialGenerators:f.minimumDPolynomialGenerators,
    matricesIndependentlyRecomputed:false,
    scope:"Exact native matrix products belong to the separately reviewed original driver. This audit reconstructs both complete mathematical receipts and semantic bindings, checks every reported stage, and independently derives the finite-module consequences using the proved H direct-summand lemma."
  };

}

if (typeof module !== "undefined") {
  module.exports = {auditOriginalJointBExecution};
  if (require.main === module) {
    const fs = require("node:fs"), crypto = require("node:crypto");
    if (process.argv.length !== 3) throw Error("Supply exactly one complete Actions job log path");
    const result = auditOriginalJointBExecution(fs.readFileSync(process.argv[2], "utf8"),
      bytes => crypto.createHash("sha256").update(Buffer.from(bytes)).digest("hex"));
    process.stdout.write(JSON.stringify(result, null, 2) + "\n");
  }
}
