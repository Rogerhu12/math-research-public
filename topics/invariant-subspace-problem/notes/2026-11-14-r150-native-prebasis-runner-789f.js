"use strict";
// Bounded F31[s] preparation of the exact original constant-N prebasis.
// The large generated basis is temporary input, never a repository artifact.
const fs=require("node:fs"),path=require("node:path"),cp=require("node:child_process"),crypto=require("node:crypto"),zlib=require("node:zlib");
const {parameterSystem}=require("./2026-11-14-rank-one-parameter-ideal-runner-789f.js");
const {monomialData}=require("./2026-11-14-r150-finite-macaulay-module-789f.js");
const hash=x=>crypto.createHash("sha256").update(x).digest("hex");
async function fileHash(file){const h=crypto.createHash("sha256");for await(const b of fs.createReadStream(file))h.update(b);return h.digest("hex");}
function prepare(out,log=()=>{}){
 const z=parameterSystem("original",log),md=monomialData(),mi=new Map(md.multipliers.map((m,i)=>[m,i]));
 const pfile=path.join(__dirname,"2026-11-14-r150-graded-pivot-profile-789f.json"),pb=fs.readFileSync(pfile),profile=JSON.parse(pb),selected=profile.selectedRows.filter(r=>r[0]<11);
 if(selected.length!==3333||BigInt(z.denominator)%31n===0n||z.contents.some(c=>c%31n===0n))throw Error("bad original F31 model");
 const mod=x=>String((x%31n+31n)%31n),lines=[];
 for(let e=0;e<11;e++){
  const q=z.equations[e].slice(11);if(q.some(p=>p.length>1)||z.equations[e].slice(0,11).some(p=>p.length>11))throw Error("original degree structure failed");
  lines.push(q.map(p=>mod(p[0])).join(" "));
  lines.push(z.equations[e].slice(0,11).flatMap(p=>Array.from({length:11},(_,k)=>mod(p[k]||0n))).join(" "));
 }
 lines.push(String(selected.length));for(const [e,m,piv]of selected)lines.push([e,m,piv,17*mi.get(m)+e+1].join(" "));
 const input=lines.join("\n")+"\n",inputFile=path.join(out,"prebasis-input.txt");fs.writeFileSync(inputFile,input);
 return {inputFile,sourceDataSHA256:z.sourceDataSHA256,originalFixedDChecks:z.checks,originalCommonDenominator:z.denominator,constantRowContents:z.contents.map(String),profileSHA256:hash(pb),inputSHA256:hash(input),inputBytes:Buffer.byteLength(input)};
}
async function main(){
 const o={out:null,seconds:60,memoryMiB:512,binary:null};const opts={"--out":"out","--seconds":"seconds","--memory-mib":"memoryMiB","--binary":"binary"};
 const a=process.argv.slice(2);for(let i=0;i<a.length;i++){const k=opts[a[i]];if(!k||i+1===a.length)throw Error("bad option "+a[i]);o[k]=a[++i];}
 o.seconds=Number(o.seconds);o.memoryMiB=Number(o.memoryMiB);if(!o.out||![o.seconds,o.memoryMiB].every(x=>Number.isSafeInteger(x)&&x>0))throw Error("bad limits");
 fs.mkdirSync(o.out,{recursive:true});o.out=path.resolve(o.out);const log=x=>process.stdout.write(JSON.stringify(x)+"\n");
 const model=prepare(o.out,log),source=path.join(__dirname,"2026-11-14-r150-native-constant-prebasis-789f.cpp");
 const receipt={format:"r150-native-constant-prebasis-v1",options:o,...model,cppSHA256:hash(fs.readFileSync(source)),field:31,parameterDegreeAtMost:10,expectedUnitPivots:3333,status:"running",started:new Date().toISOString()};
 const save=()=>fs.writeFileSync(path.join(o.out,"prebasis-receipt.json"),JSON.stringify(receipt,null,2)+"\n");save();
 if(!o.binary){o.binary=path.join(o.out,"build-prebasis");const r=cp.spawnSync("timeout",["--kill-after=10s","30s","g++","-O3","-std=c++17",source,"-o",o.binary],{encoding:"utf8",maxBuffer:1024*1024});if(r.error||r.status!==0){receipt.status="compile-failed";receipt.compileExit=r.status;save();throw Error("native compile failed: "+String(r.error||r.stderr));}}
 const basis=path.join(o.out,"basis.sing"),operations=path.join(o.out,"source-operations.bin"),logFile=fs.createWriteStream(path.join(o.out,"native-execution.log"));
 const child=cp.spawn("timeout",["--kill-after=10s",String(o.seconds)+"s","prlimit","--as="+String(o.memoryMiB*1024*1024),"--core=0","--",o.binary,model.inputFile,basis,operations],{stdio:["ignore","pipe","pipe"]});
 let done=false,pending="",last=null;
 child.stdout.on("data",b=>{logFile.write(b);process.stdout.write(b);pending+=String(b);const parts=pending.split(/\r?\n/);pending=parts.pop();for(const line of parts){try{const v=JSON.parse(line);if(v.status==="native-prebasis-complete"){done=true;last=v;}}catch{}}});
 child.stderr.on("data",b=>{logFile.write(b);process.stderr.write(b);});
 const result=await new Promise((resolve,reject)=>{child.on("error",reject);child.on("close",(code,signal)=>resolve({code,signal}));});logFile.end();
 receipt.status=result.code===0&&done?"completed":"failed-or-incomplete";receipt.exitCode=result.code;receipt.signal=result.signal;receipt.finished=new Date().toISOString();receipt.nativeStatistics=last;
 receipt.outputs={};for(const [name,file]of [["basis",basis],["sourceOperations",operations]])if(fs.existsSync(file))receipt.outputs[name]={file,bytes:fs.statSync(file).size,sha256:await fileHash(file)};
 if(receipt.status==="completed"){
  const b=fs.readFileSync(operations),gz=zlib.gzipSync(b,{level:9});if(gz.length>5000000)throw Error("source operation certificate exceeds repository compressed limit");fs.writeFileSync(operations+".gz",gz);fs.unlinkSync(operations);receipt.outputs.sourceOperations.compressedFile=operations+".gz";receipt.outputs.sourceOperations.compressedBytes=gz.length;
  receipt.operationsFormat="R150PB31 magic (8 bytes), little-endian u32 row count; each row: original source row u32, scale u8, reduction count u32, then pairs(previous basis index u16, subtraction coefficient u8). New basis row equals scale*(original row - sum coefficient*previous basis row).";
  receipt.basisStorage="Temporary runtime input only. The generated basis is much larger than repository artifact limits; retain hash and reproducible command, never commit this file.";
 }
 save();log({status:receipt.status,nativeStatistics:last,outputs:receipt.outputs});if(receipt.status!=="completed")process.exitCode=1;
}
module.exports={prepare,fileHash};
if(require.main===module)main().catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
