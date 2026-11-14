"use strict";
// Bounded, source-faithful F31[s] normal forms. The original 17 equations,
// constant prebasis source profile and the exact 2195-source theorem are used.
const fs=require("node:fs"),path=require("node:path"),cp=require("node:child_process"),crypto=require("node:crypto");
const {parameterSystem}=require("./2026-11-14-rank-one-parameter-ideal-runner-789f.js");
const {monomialData}=require("./2026-11-14-r150-finite-macaulay-module-789f.js");
const hash=b=>crypto.createHash("sha256").update(b).digest("hex");
async function fileHash(f){const h=crypto.createHash("sha256");for await(const b of fs.createReadStream(f))h.update(b);return h.digest("hex");}
function prepare(out,o,log=()=>{}){
 const z=parameterSystem("original",log),md=monomialData(),mi=new Map(md.multipliers.map((m,i)=>[m,i]));
 const profileBytes=fs.readFileSync(path.join(__dirname,"2026-11-14-r150-graded-pivot-profile-789f.json")),profile=JSON.parse(profileBytes),selected=profile.selectedRows.filter(r=>r[0]<11);
 const extraBytes=fs.readFileSync(path.join(__dirname,"2026-11-14-r150-eleven-n-source-profile-789f.json")),extra=JSON.parse(extraBytes);
 if(selected.length!==3333||BigInt(z.denominator)%31n===0n||z.contents.some(c=>c%31n===0n))throw Error("bad original F31 model");
 // These are actual original row numbers proved sufficient in the published
 // polynomial-module compression, not rows of the homogeneous truncation.
 const extraRaw=[5842,5978,5995,6012,6080,6097,6114,6131,6148,6165,6182];
 if(extra.field!==31||extra.homogeneousProfileSHA256!==hash(profileBytes)||JSON.stringify(extra.extraRows.map(r=>r.originalRow))!==JSON.stringify(extraRaw))throw Error("extra source theorem profile mismatch");
 const allSources=extraRaw.map(raw=>({e:(raw-1)%17,multiplier:md.multipliers[Math.floor((raw-1)/17)],raw}));
 for(let u=0;u<364;u++)for(let e=11;e<17;e++)allSources.push({e,multiplier:md.multipliers[u],raw:17*u+e+1});
 if(allSources.length!==2195||new Set(allSources.map(s=>s.raw)).size!==2195)throw Error("compressed source count");
 // Include both endpoints in each homogeneous degree, plus two actual extra N
 // rows. This is a throughput probe, not a substitute for the full 2195 rows.
 const sample=[11,16,17,82,83,478,479,2194,0,10];
 const indices=o.all?allSources.map((_,i)=>i):o.indices?o.indices.split(",").map(Number):sample;
 if(new Set(indices).size!==indices.length||indices.some(i=>!Number.isSafeInteger(i)||i<0||i>=2195))throw Error("invalid source index");
 const sources=indices.map(i=>allSources[i]),targets=o.targets?Array.from({length:9},(_,i)=>i+2):[];
 const mod=x=>String((x%31n+31n)%31n),lines=["R150_NATIVE_NF_V1"];
 for(let e=0;e<11;e++){
  const q=z.equations[e].slice(11);if(q.some(p=>p.length>1)||z.equations[e].slice(0,11).some(p=>p.length>11))throw Error("original N degree structure");
  lines.push(q.map(p=>mod(p[0])).join(" "));lines.push(z.equations[e].slice(0,11).flatMap(p=>Array.from({length:11},(_,k)=>mod(p[k]||0n))).join(" "));
 }
 lines.push(String(selected.length));for(const [e,m,p]of selected)lines.push([e,m,p,17*mi.get(m)+e+1].join(" "));
 for(let e=11;e<17;e++){
  if(z.equations[e].slice(0,11).some(p=>p.some(a=>a!==0n))||z.equations[e].slice(11).some(p=>p.length>6))throw Error("original full Gamma degree structure");
  lines.push(z.equations[e].slice(11).flatMap(p=>Array.from({length:6},(_,k)=>mod(p[k]||0n))).join(" "));
 }
 lines.push([sources.length,targets.length].join(" "));for(const s of sources)lines.push([s.e,s.multiplier,s.raw].join(" "));lines.push(targets.join(" "));
 const input=lines.join("\n")+"\n",inputFile=path.join(out,"normal-form-input.txt");fs.writeFileSync(inputFile,input);
 const pivots=new Set(selected.map(r=>r[2])),components=md.columns.filter(k=>!pivots.has(k));if(components.length!==1034)throw Error("component projection");
 const mapping={format:"r150-native-normal-form-mapping-v1",field:31,components,originalComponentIndices:components.map(k=>md.index.get(k)),sourceIndices:indices,sources,targets,
  allCompressedSourceRows:allSources.map(s=>s.raw),prebasisRows:selected.map(([e,m,p])=>({generator:e,multiplier:m,pivot:p,raw:17*mi.get(m)+e+1})),
  originalRows:"17*u+i: multiplier u=0..363, original generator i=1..17",componentKeys:"sum exponent_i * 8^i in the original m coordinates"};
 fs.writeFileSync(path.join(out,"normal-form-mapping.json"),JSON.stringify(mapping)+"\n");
 return {inputFile,sourceDataSHA256:z.sourceDataSHA256,originalFixedDChecks:z.checks,originalCommonDenominator:z.denominator,constantRowContents:z.contents.map(String),profileSHA256:hash(profileBytes),extraSourceProfileSHA256:hash(extraBytes),inputSHA256:hash(input),inputBytes:Buffer.byteLength(input),sourceCount:sources.length,targetCount:targets.length,allSources:!!o.all};
}
async function main(){
 const o={out:null,seconds:60,memoryMiB:512,binary:null,all:false,indices:null,targets:true,basisMode:"rref",generateOnly:false};
 const opts={"--out":"out","--seconds":"seconds","--memory-mib":"memoryMiB","--binary":"binary","--indices":"indices","--basis-mode":"basisMode"};
 const a=process.argv.slice(2);for(let i=0;i<a.length;i++){
  if(a[i]==="--all"){o.all=true;continue;}if(a[i]==="--no-targets"){o.targets=false;continue;}if(a[i]==="--generate-only"){o.generateOnly=true;continue;}
  const k=opts[a[i]];if(!k||i+1===a.length)throw Error("bad option "+a[i]);o[k]=a[++i];
 }
 o.seconds=Number(o.seconds);o.memoryMiB=Number(o.memoryMiB);if(!o.out||![o.seconds,o.memoryMiB].every(x=>Number.isSafeInteger(x)&&x>0)||!["forward","rref"].includes(o.basisMode)||o.all&&o.indices)throw Error("bad options");
 fs.mkdirSync(o.out,{recursive:true});o.out=path.resolve(o.out);const log=x=>process.stdout.write(JSON.stringify(x)+"\n");
 const model=prepare(o.out,o,log),source=path.join(__dirname,"2026-11-14-r150-native-normal-form-789f.cpp");
 const receipt={format:"r150-native-normal-forms-v1",options:o,...model,cppSHA256:hash(fs.readFileSync(source)),runnerSHA256:hash(fs.readFileSync(__filename)),field:31,components:1034,status:o.generateOnly?"input-generated-only":"running",started:new Date().toISOString()};
 const save=()=>fs.writeFileSync(path.join(o.out,"normal-form-receipt.json"),JSON.stringify(receipt,null,2)+"\n");save();if(o.generateOnly){log(receipt);return;}
 if(!o.binary){o.binary=path.join(o.out,"native-normal-form");const r=cp.spawnSync("timeout",["--kill-after=10s","30s","prlimit","--as=536870912","--core=0","--","g++","-O3","-std=c++17",source,"-o",o.binary],{encoding:"utf8",maxBuffer:1024*1024});if(r.error||r.status!==0){receipt.status="compile-failed";receipt.compileExit=r.status;save();throw Error("compile failed: "+String(r.error||r.stderr));}}
 receipt.binarySHA256=await fileHash(o.binary);save();
 const prefix=path.join(o.out,"nf"),lf=fs.createWriteStream(path.join(o.out,"native-normal-form.log"));
 const child=cp.spawn("timeout",["--kill-after=10s",String(o.seconds)+"s","prlimit","--as="+String(o.memoryMiB*1024*1024),"--core=0","--",o.binary,model.inputFile,prefix,o.basisMode],{stdio:["ignore","pipe","pipe"]});
 let pending="",done=false,last=null;child.stdout.on("data",b=>{lf.write(b);process.stdout.write(b);pending+=String(b);const ls=pending.split(/\r?\n/);pending=ls.pop();for(const l of ls){try{const v=JSON.parse(l);if(v.status==="native-normal-forms-complete"){done=true;last=v;}}catch{}}});
 child.stderr.on("data",b=>{lf.write(b);process.stderr.write(b);});const heartbeat=setInterval(()=>log({phase:"native-normal-form-heartbeat",at:new Date().toISOString()}),30000);
 let result;try{result=await new Promise((resolve,reject)=>{child.on("error",reject);child.on("close",(code,signal)=>resolve({code,signal}));});}finally{clearInterval(heartbeat);lf.end();}
 Object.assign(receipt,{status:result.code===0&&done?"completed":"failed-or-incomplete",exitCode:result.code,signal:result.signal,finished:new Date().toISOString(),nativeStatistics:last,outputs:{}});
 for(const name of ["forward.bin","backward.bin","reduction.bin","normal-forms.bin","normal-forms.sing"]){const file=prefix+"-"+name;if(fs.existsSync(file))receipt.outputs[name]={file,bytes:fs.statSync(file).size,sha256:await fileHash(file)};}
 receipt.sourceIdentity="For each source or target, NF=raw-sum coefficient*s^exponent*RREFBasis[basis]. RREFBasis is obtained from the original unit prebasis by the recorded backward operations. The original unit prebasis has the unchanged R150PB31 source DAG.";
 receipt.storage="Large generated matrices and traces are temporary runtime outputs. Publish only bounded compressed certificates or hashes with reproducible inputs.";
 save();log({status:receipt.status,nativeStatistics:last,outputs:receipt.outputs});if(receipt.status!=="completed")process.exitCode=1;
}
module.exports={prepare,fileHash};if(require.main===module)main().catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
