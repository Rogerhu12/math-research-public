// Author: Astra-ISP-789f / root. AI-assisted GPT-6 Astra Pro.
// Date: 2026-11-16. Read-only whole-log provenance and original-gate audit.
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

function auditOriginalJointMExecution(log,hashBytes){
 const need=(v,m)=>{if(!v)throw Error(m);};
 const ids=["rebuild-selected-true16-original-p9-through35","original-joint-m-primitive-free-lattice-qualification"];
 const lines=log.split("\n").filter(l=>l.includes(" ISP_REMOTE_STEP "));
 const all=lines.map(l=>JSON.parse(l.slice(l.indexOf("ISP_REMOTE_STEP ")+16)));
 const selected=ids.map(id=>{const z=all.filter(s=>s.stepId===id);need(z.length===1,"unique actual step "+id);return z[0];});
 need(selected[0].scriptSHA256==="e4b2b935882e899a55d7db10d590e5ce8d35f5fedcab6063a14008a5efe4b69e","original selected source");
 need(selected[1].scriptSHA256==="855614a779dca566478752179e68710934cc2982eef3a4b60452119a0ff3cf01","complete original M source");
 for(const s of selected)need(s.exitCode===0&&s.result.status==="completed","actual completed mathematical step");
 const relevant=lines.filter(l=>ids.some(id=>l.includes('"stepId": "'+id+'"'))).join("\n");
 const raw=auditExactExecutionLog(relevant,hashBytes);
 need(raw.steps.length===2&&raw.steps.every(s=>s.bindingVerified===true),"both complete original semantic bindings");
 let stages=0,fullIntegerProducts=0,fullUnitProducts=0;
 for(const[name,x]of Object.entries(selected[0].result.parameters.stages)){
  need(x.status==="completed"&&x.exitCode===0,"actual completed parent stage "+name);
  need(/^[a-f0-9]{64}$/.test(x.inputBinding),"stage input binding");
  for(const[k,v]of Object.entries(x.statistics||{}))
   if(/^(all|fullOriginal|residualIs|sameOriginal)/.test(k)&&typeof v==="boolean"){
    if(k==="allLockedSourceCoefficientsRetained")need(v===(x.statistics.lockedPrefixLength>0),"declared lock scope");
    else need(v,"full original parent gate "+name+" "+k);
   }
  if(x.statistics?.allOriginal17CoefficientsDivisible)fullIntegerProducts++;
  if(x.statistics?.fullOriginalGIdentityVerified)fullUnitProducts++;
  stages++;
 }
 const p=selected[1].result.parameters.final;
 for(const k of ["actualTrue16OriginalSourceBasisUsed","all225OriginalParameterProductsVerified","all315CoordinatesRetained","all505OriginalFreeChecksVerified","completePrimitiveFreeLatticeQualified","extraWholeFieldDefectDirectionNotIdentifiedWithOriginalFreeCarrier","highPCoordinatesAndCompleteJointMStructureNotClaimed","full210NotRecomputed"])need(p[k]===true,"full original M gate "+k);
 need(p.originalTargetFieldDimension===34&&p.freeTargetDimensionModuloFullTrue16===25&&p.combinedTargetAndTrueTorsionDimension===41&&p.globalTargetTorsionIntersectionResidueDimension===9,"whole original image and true torsion quotient");
 need(p.minimumFieldPolynomialGeneratorsOfTargetImage===6&&JSON.stringify(p.originalJointMMinimumDPolynomialGeneratorInterval)==="[8,9]"&&p.originalJointMHasExactlyNineGenerators===false,"actual generator scope");
 need(p.primary.length===6&&p.primary.every(q=>q.all315OriginalPrimaryProductsVerified===true),"all six original primary products");
 for(const center of [1,2]){
  const q=p.primary.find(q=>q.center===center);
  need(q?.primitiveFreeLineQualified===true&&q.primitiveTargetLabel===2,"actual primitive target");
  need(q.torsionIntersectionResidueDimension===(center===1?0:9)&&q.torsionIntersectionEqualsCompleteComponent===false,"residue intersection scope");
 }
 return {format:"isp-original-joint-m-independent-log-audit-v1",rawAudit:raw,completedParentStages:stages,fullOriginalIntegerProducts:fullIntegerProducts,fullOriginalUnitProducts:fullUnitProducts,
  wholeOriginalTargetDimension:34,primitiveFreeDimension:25,allSixPrimaryProductsVerified:true,fieldImageMinimumGenerators:6,originalGeneratorInterval:[8,9]};
}

if(typeof module!=="undefined"&&require.main===module){
 const fs=require("fs"),crypto=require("crypto");
 const log=fs.readFileSync(process.argv[2],"utf8");
 const hashBytes=b=>crypto.createHash("sha256").update(Buffer.from(b)).digest("hex");
 process.stdout.write(JSON.stringify(auditOriginalJointMExecution(log,hashBytes),null,2)+"\n");
}
