"use strict";
/*
Finite Macaulay module over K[s], not the original multivariate ideal GB.
Every module generator is one original F_i times a monomial of degree <=3.
The 4367 components encode all nonconstant original m monomials of degree <=5.
Hence an exact module lift is an exact original-generator certificate with
multiplier degree <=3. Finite characteristic is discovery only.
*/
const fs=require("node:fs"),path=require("node:path"),cp=require("node:child_process"),crypto=require("node:crypto");
const {parameterSystem}=require("./2026-11-14-rank-one-parameter-ideal-runner-789f.js");
const hash=x=>crypto.createHash("sha256").update(x).digest("hex");
async function fileHash(file){const h=crypto.createHash("sha256");for await(const b of fs.createReadStream(file))h.update(b);return h.digest("hex");}
const choose=(n,k)=>{let x=1n;for(let j=1;j<=k;j++)x=x*BigInt(n-j+1)/BigInt(j);return x;};
function monomialData(){
 const powers=Array.from({length:11},(_,i)=>8**i),degrees=[];
 for(let d=0;d<=5;d++){const a=[];const rec=(left,lo,key)=>{if(!left){a.push(key);return;}for(let i=lo;i<11;i++)rec(left-1,i,key+powers[i]);};rec(d,0,0);degrees.push(a);}
 const columns=degrees.slice(1).reverse().flat(),index=new Map(columns.map((x,i)=>[x,i+1]));
 const multipliers=degrees.slice(0,4).flat();
 const terms=powers.slice();for(let i=0;i<11;i++)for(let j=i;j<11;j++)terms.push(powers[i]+powers[j]);
 const positions=multipliers.map(k=>terms.map(t=>index.get(k+t)));
 if(columns.length!==4367||multipliers.length!==364||terms.length!==77||positions.flat().some(x=>!x))throw Error("Macaulay indexing mismatch");
 return {powers,columns,index,multipliers,terms,positions};
}
const peval=(p,s)=>p.reduceRight((a,c)=>a*s+c,0n);
function pstring(p,characteristic,source){
 if(source!==null)p=[peval(p,BigInt(source))];
 const pp=BigInt(characteristic),out=[];
 p.forEach((v,i)=>{if(pp)v=(v%pp+pp)%pp;if(v)out.push("("+String(v)+")"+(i?"*s"+(i>1?"^"+i:""):""));});
 return out.length?out.join("+"):"0";
}
function targetVectors(md,o){
 return Array.from({length:9},(_,i)=>{
  const n=i+2,terms=[];
  for(let a=0;a<=n;a++)for(let b=a;b<=n;b++){
   const degree=2*n-a-b,c=choose(n,a)*choose(n,b)*BigInt((a===b?1:2)*(degree%2?-1:1));
   const p=Array(degree+1).fill(0n);p[degree]=c;
   const coefficient=pstring(p,o.characteristic,o.source);
   if(coefficient!=="0")terms.push("("+coefficient+")*gen("+md.index.get(md.powers[a]+md.powers[b])+")");
  }return terms.join("+");
 });
}
function generate(z,o,out){
 const md=monomialData(),strings=z.equations.map(r=>r.map(p=>pstring(p,o.characteristic,o.source)));
 const profileFile=path.join(__dirname,"2026-11-14-r150-graded-pivot-profile-789f.json"),profileBytes=fs.readFileSync(profileFile),profile=JSON.parse(profileBytes);
 const multIndex=new Map(md.multipliers.map((m,i)=>[m,i]));
 const preRows=profile.selectedRows.filter(r=>r[0]<11).map(([e,m])=>17*multIndex.get(m)+e+1);
 if(preRows.length!==3333||new Set(preRows).size!==3333)throw Error("bad constant pivot profile");
 const basisFile=path.join(out,"basis.sing"),certificateFile=path.join(out,"module-certificate.sing"),denFile=path.join(out,"denominator.sing");
 const lines=["// Exact fixed degree-five original Macaulay module.",
  `ring R=${o.characteristic},s,(c,dp);`,"short=0;",`matrix Coeff[17][77]=${strings.flat().join(",\n")};`,
  `intmat CI[364][77]=${md.positions.flat().join(",")};`,
  "module M; vector vr; int i; int j; int k;",
  'print("R150_MODULE_BEGIN_BUILD");',
  "for(j=1;j<=364;j++){for(i=1;i<=17;i++){vr=0;for(k=1;k<=77;k++){if(Coeff[i,k]!=0){vr=vr+Coeff[i,k]*gen(CI[j,k]);}}M[(j-1)*17+i]=vr;}}",
  `module T=${targetVectors(md,o).join(",\n")};`,
  'print("R150_MODULE_ROWS="+string(size(M)));',
  'print("R150_MODULE_COMPONENTS="+string(nrows(matrix(M))));',
  "option(redSB);","module Reduced;module Target;int nred;",
  ...(o.normalFormsFile?[
   'print("R150_MODULE_BEGIN_NATIVE_NORMAL_FORMS");',
   "kill Reduced;kill Target;",
   `< ${JSON.stringify(o.normalFormsFile)};`,
   'if(nrows(matrix(Reduced))>1034||ncols(matrix(Reduced))>2195||ncols(matrix(Target))!=9||nrows(matrix(Target))>1034){print("R150_MODULE_NATIVE_NORMAL_FORM_SHAPE_FAILED");quit;}',
   "nred=1034;",
   'print("R150_MODULE_NATIVE_SOURCE_ROWS=2195");',
   'print("R150_MODULE_REDUCED_COMPONENTS=1034");'
  ]:o.precondition==="constant"?[
   `intvec preRows=${preRows.join(",")};`,"module Pre;for(i=1;i<=size(preRows);i++){Pre[i]=M[preRows[i]];}",
   'print("R150_MODULE_BEGIN_CONSTANT_PRECONDITIONER");',
   ...(o.prebasisFile?[`< ${JSON.stringify(o.prebasisFile)};`]:["module B0=std(Pre);"]),
   'if(size(B0)!=3333){print("R150_MODULE_CONSTANT_RANK_FAILED");quit;}',
   "intvec reindex=0;reindex[4367]=0;intvec le;",
   'for(i=1;i<=size(B0);i++){le=leadexp(B0[i]);if(le[1]!=0||leadcoef(B0[i])!=1||reindex[le[2]]!=0){print("R150_MODULE_CONSTANT_PIVOT_FAILED");quit;}reindex[le[2]]=-1;}',
   "nred=0;for(i=1;i<=4367;i++){if(reindex[i]==0){nred++;reindex[i]=nred;}}",
   'if(nred!=1034){print("R150_MODULE_CONSTANT_COMPONENTS_FAILED");quit;}',
   'print("R150_MODULE_CONSTANT_PRECONDITIONER_READY");',
   "module Rem=reduce(M,B0);module RemT=reduce(T,B0);matrix AR=matrix(Rem);matrix AT=matrix(RemT);",
   'if(ncols(AR)!=6188||ncols(AT)!=9){print("R150_MODULE_SOURCE_COLUMN_ALIGNMENT_FAILED");quit;}',
   "matrix RR[1034][6188];matrix TT[1034][9];",
   "for(i=1;i<=4367;i++){if(reindex[i]>0){if(i<=nrows(AR)){RR[reindex[i],1..6188]=AR[i,1..6188];}if(i<=nrows(AT)){TT[reindex[i],1..9]=AT[i,1..9];}}}",
   "Reduced=module(RR);Target=module(TT);kill AR;kill AT;kill RR;kill TT;kill Rem;kill RemT;",
   'print("R150_MODULE_REDUCED_COMPONENTS=1034");'
  ]:["Reduced=M;Target=T;nred=4367;"]),
  'print("R150_MODULE_BEGIN_BASIS");',"module B=std(Reduced);",
  'print("R150_MODULE_BASIS_SIZE="+string(size(B)));',
  `write(${JSON.stringify(basisFile)},"module B="+string(B)+";");`,
  'print("R150_MODULE_BEGIN_ANNIHILATOR");',"ideal Ann=std(quotient(B,Target));",
  'if(size(Ann)!=1||Ann[1]==0){print("R150_MODULE_ANNIHILATOR_NOT_NONZERO_PRINCIPAL");quit;}',
  "poly h=Ann[1]/leadcoef(Ann[1]);",
  `write(${JSON.stringify(denFile)},"poly denominatorPolynomial="+string(h)+";");`,
  "poly known=s*(s-2)*(s+6)*(5*s^3-25*s^2+32*s-8)*(5*s^3+135*s^2+864*s+864)*(5*s^8+50*s^7+153*s^6-936*s^5-2888*s^4+15936*s^3-3392*s^2-25472*s+9600);",
  "poly residual=h;poly gg=gcd(residual,known);while(deg(gg)>0){residual=residual/gg;gg=gcd(residual,known);}",
  `write(${JSON.stringify(denFile)},"poly unresolvedDenominator="+string(residual)+";");`,
  `write(${JSON.stringify(denFile)},string(factorize(residual)));`,
  'print("R150_MODULE_DENOMINATOR_DEGREE="+string(deg(h)));',
  'print("R150_MODULE_UNRESOLVED_DEGREE="+string(deg(residual)));',
  "module HT=h*T;module ReducedHT=h*Target;module rem=reduce(ReducedHT,B);",
  'if(size(rem)!=0){print("R150_MODULE_ANNIHILATOR_MEMBERSHIP_FAILED");quit;}'];
 if(o.stage==="lift")lines.push('print("R150_MODULE_BEGIN_LIFT");',
  'matrix U;matrix C=lift(Reduced,ReducedHT,U,"std");',
  ...(o.precondition==="constant"?[
   "matrix remainder=matrix(HT)-matrix(M)*C;module V=module(remainder);",
   'print("R150_MODULE_BEGIN_CONSTANT_BACK_LIFT");',
   'matrix C0=lift(Pre,V,U,"std");',
   "for(i=1;i<=size(preRows);i++){for(j=1;j<=9;j++){C[preRows[i],j]=C[preRows[i],j]+C0[i,j];}}"
  ]:[]),
  "matrix check=matrix(M)*C-matrix(HT);int bad=0;",
  "for(i=1;i<=nrows(check);i++){for(j=1;j<=ncols(check);j++){if(check[i,j]!=0){bad++;}}}",
  'if(bad){print("R150_MODULE_EXACT_IDENTITY_FAILED");quit;}',
  `write(${JSON.stringify(certificateFile)},"matrix C["+string(nrows(C))+"]["+string(ncols(C))+"];");`,
  `for(i=1;i<=nrows(C);i++){for(j=1;j<=ncols(C);j++){if(C[i,j]!=0){write(${JSON.stringify(certificateFile)},"C["+string(i)+","+string(j)+"]="+string(C[i,j])+";");}}}`,
  'print("R150_MODULE_EXACT_IDENTITY_VERIFIED");');
 lines.push('print("R150_MODULE_DONE");',"quit;");
 return {script:lines.join("\n")+"\n",mapping:{columns:md.columns,multipliers:md.multipliers,constantPreconditionerRows:preRows,gradedProfileSHA256:hash(profileBytes),rows:"row 17*u+i corresponds to multiplier index u=0..363 and generator i=1..17",keyEncoding:"sum exponent_i*8^i, original m coordinates"},files:{basis:basisFile,certificate:certificateFile,denominator:denFile}};
}
async function main(){
 const o={characteristic:31,source:null,stage:"annihilator",precondition:"constant",prebasisFile:null,normalFormsFile:null,out:null,singular:"Singular",seconds:60,memoryMiB:512,generateOnly:false};
 const options={"--characteristic":"characteristic","--source":"source","--stage":"stage","--precondition":"precondition","--prebasis-file":"prebasisFile","--normal-forms-file":"normalFormsFile","--out":"out","--singular":"singular","--seconds":"seconds","--memory-mib":"memoryMiB"};
 const args=process.argv.slice(2);for(let i=0;i<args.length;i++){if(args[i]==="--generate-only"){o.generateOnly=true;continue;}const n=options[args[i]];if(!n||i+1===args.length)throw Error("bad argument "+args[i]);o[n]=args[++i];}
 for(const k of ["characteristic","seconds","memoryMiB"])o[k]=Number(o[k]);if(o.source!==null)o.source=Number(o.source);
 if(!o.out||!["annihilator","lift"].includes(o.stage)||!["none","constant"].includes(o.precondition)||![o.characteristic,o.seconds,o.memoryMiB].every(Number.isSafeInteger)||o.characteristic<0||o.seconds<=0||o.memoryMiB<=0||o.source!==null&&!Number.isSafeInteger(o.source))throw Error("bad options");
 fs.mkdirSync(o.out,{recursive:true});o.out=path.resolve(o.out);
 if(o.prebasisFile){if(o.characteristic!==31||o.source!==null||o.precondition!=="constant")throw Error("native prebasis requires original F31[s] constant preconditioning");o.prebasisFile=fs.realpathSync(o.prebasisFile);if(o.prebasisFile===path.join(o.out,"basis.sing"))throw Error("prebasis must be separate from the output basis");}
 if(o.normalFormsFile){
  if(o.prebasisFile||o.characteristic!==31||o.source!==null||o.precondition!=="constant"||o.stage!=="annihilator")throw Error("native normal forms require original F31[s], constant preconditioning, annihilator stage, and no separate prebasis");
  o.normalFormsFile=fs.realpathSync(o.normalFormsFile);
  if(path.dirname(o.normalFormsFile)===o.out)throw Error("large native normal forms must stay in a separate runtime directory");
 }
 const log=x=>process.stdout.write(JSON.stringify(x)+"\n");
 const z=parameterSystem("original",log),p=BigInt(o.characteristic);
 if(p&&(BigInt(z.denominator)%p===0n||z.contents.some(c=>c%p===0n)))throw Error("bad original prime");
 const g=generate(z,o,o.out),input=path.join(o.out,"input.sing");fs.writeFileSync(input,g.script);
 fs.writeFileSync(path.join(o.out,"macaulay-mapping.json"),JSON.stringify(g.mapping)+"\n");
 const receipt={format:"r150-finite-macaulay-module-v1",options:o,sourceDataSHA256:z.sourceDataSHA256,
  fixedDReconstructionChecks:z.checks,constantRowContents:z.contents.map(String),inputSHA256:hash(g.script),inputBytes:Buffer.byteLength(g.script),
  originalCommonDenominator:z.denominator,sourceGeneratorCount:17,multiplierCount:364,components:4367,rows:6188,
  status:o.generateOnly?"input-generated-only":"running",started:new Date().toISOString()};
 if(o.prebasisFile){
  const pr=JSON.parse(fs.readFileSync(path.join(path.dirname(o.prebasisFile),"prebasis-receipt.json"),"utf8"));
  const sha=await fileHash(o.prebasisFile);
  if(pr.status!=="completed"||pr.field!==31||pr.expectedUnitPivots!==3333||pr.sourceDataSHA256!==z.sourceDataSHA256||pr.profileSHA256!==g.mapping.gradedProfileSHA256||pr.outputs?.basis?.sha256!==sha)throw Error("native prebasis provenance mismatch");
  receipt.prebasis={file:o.prebasisFile,bytes:fs.statSync(o.prebasisFile).size,sha256:sha,sourceOperationsSHA256:pr.outputs.sourceOperations.sha256};
 }
 if(o.normalFormsFile){
  const dir=path.dirname(o.normalFormsFile),nf=JSON.parse(fs.readFileSync(path.join(dir,"normal-form-receipt.json"),"utf8"));
  const nmBytes=fs.readFileSync(path.join(dir,"normal-form-mapping.json")),nm=JSON.parse(nmBytes),sha=await fileHash(o.normalFormsFile);
  const extraBytes=fs.readFileSync(path.join(__dirname,"2026-11-14-r150-eleven-n-source-profile-789f.json")),extra=JSON.parse(extraBytes);
  const prior=JSON.parse(fs.readFileSync(path.join(__dirname,"2026-11-14-r150-native-prebasis-receipt-789f.json"),"utf8"));
  const expectedRows=extra.extraRows.map(r=>r.originalRow);
  for(let u=0;u<364;u++)for(let i=12;i<=17;i++)expectedRows.push(17*u+i);
  const profile=JSON.parse(fs.readFileSync(path.join(__dirname,"2026-11-14-r150-graded-pivot-profile-789f.json"),"utf8"));
  const pivots=new Set(profile.selectedRows.filter(r=>r[0]<11).map(r=>r[2]));
  const components=g.mapping.columns.filter(c=>!pivots.has(c)),same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
  if(nf.status!=="completed"||nf.exitCode!==0||nf.field!==31||nf.components!==1034||nf.allSources!==true||nf.sourceCount!==2195||nf.targetCount!==9||nf.sourceDataSHA256!==z.sourceDataSHA256||nf.profileSHA256!==g.mapping.gradedProfileSHA256||nf.extraSourceProfileSHA256!==hash(extraBytes)||nf.outputs?.["normal-forms.sing"]?.sha256!==sha||nf.outputs?.["forward.bin"]?.sha256!==prior.outputs.sourceOperations.sha256)throw Error("native normal form provenance mismatch");
  if(nm.field!==31||!same(nm.components,components)||!same(nm.originalComponentIndices,components.map(c=>g.mapping.columns.indexOf(c)+1))||!same(nm.sources.map(s=>s.raw),expectedRows)||!same(nm.allCompressedSourceRows,expectedRows)||!same(nm.sourceIndices,expectedRows.map((_,i)=>i))||!same(nm.targets,[2,3,4,5,6,7,8,9,10])||!same(nm.prebasisRows.map(s=>s.raw),g.mapping.constantPreconditionerRows))throw Error("native normal form original-row mapping mismatch");
  receipt.normalForms={file:o.normalFormsFile,bytes:fs.statSync(o.normalFormsFile).size,sha256:sha,mappingSHA256:hash(nmBytes),sourceCount:2195,components:1034,sourceOperationsSHA256:nf.outputs["forward.bin"].sha256,backwardOperationsSHA256:nf.outputs["backward.bin"].sha256,reductionOperationsSHA256:nf.outputs["reduction.bin"].sha256,scope:"Exact F31[s] quotient by the constant unit prebasis; source identities are recorded by native operations. No characteristic-zero or lifted original-row certificate is claimed."};
  fs.copyFileSync(path.join(dir,"normal-form-mapping.json"),path.join(o.out,"native-normal-form-mapping.json"));
 }
 const save=()=>fs.writeFileSync(path.join(o.out,"receipt.json"),JSON.stringify(receipt,null,2)+"\n");save();
 if(o.generateOnly){log(receipt);return;}
 const child=cp.spawn("timeout",["--kill-after=10s",String(o.seconds)+"s","prlimit","--as="+String(o.memoryMiB*1024*1024),"--core=0","--",o.singular,"-q",input],{stdio:["ignore","pipe","pipe"]});
 const logfile=fs.createWriteStream(path.join(o.out,"execution.log"));let tail="",done=false,exact=false,error=false;
 child.stdout.on("data",b=>{logfile.write(b);process.stdout.write(b);tail=(tail+String(b)).slice(-8192);const lines=tail.split(/\r?\n/).map(s=>s.trim());if(lines.includes("R150_MODULE_DONE"))done=true;if(lines.includes("R150_MODULE_EXACT_IDENTITY_VERIFIED"))exact=true;if(/^\s*\?/m.test(tail)||lines.some(s=>s.endsWith("_FAILED")||s==="R150_MODULE_ANNIHILATOR_NOT_NONZERO_PRINCIPAL"))error=true;});
 child.stderr.on("data",b=>{logfile.write(b);process.stderr.write(b);});
 const heartbeat=setInterval(()=>log({phase:"finite-module-heartbeat",at:new Date().toISOString(),pid:child.pid,done,exact}),45000);
 let result;try{result=await new Promise((resolve,reject)=>{child.on("error",reject);child.on("close",(code,signal)=>resolve({code,signal}));});}finally{clearInterval(heartbeat);logfile.end();}
 Object.assign(receipt,{finished:new Date().toISOString(),exitCode:result.code,signal:result.signal,completionMarker:done,exactIdentityVerified:exact,singularError:error});
 receipt.status=result.code===0&&done&&!error&&(o.stage!=="lift"||exact)?"completed":"failed-or-incomplete";
 receipt.outputs={};const zlib=require("node:zlib");
 for(const [name,file] of Object.entries(g.files))if(fs.existsSync(file)){const b=fs.readFileSync(file);receipt.outputs[name]={bytes:b.length,sha256:hash(b)};if(b.length>1000000){const gz=zlib.gzipSync(b,{level:9});if(gz.length<=5000000){fs.writeFileSync(file+".gz",gz);receipt.outputs[name].compressedBytes=gz.length;}else receipt.outputs[name].saved="hash-and-reproducible-input-only; compressed file exceeds 5MB";fs.unlinkSync(file);}}
 save();log({status:receipt.status,exitCode:result.code,exactIdentityVerified:exact,outputs:receipt.outputs});if(receipt.status!=="completed")process.exitCode=1;
}
module.exports={monomialData,targetVectors,generate};
if(require.main===module)main().catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
