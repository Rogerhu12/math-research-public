"use strict";
/*
Reconstruct the fixed-D original seventeen equations as polynomials in s,
then ask Singular for exact ideal membership over Q(s), or over F_p(s)
for discovery. No finite sample is interpreted as a characteristic-zero
classification. Public repository README rule 13: use this repository's own Actions. The former cross-repository runner remains stopped.
*/
const fs=require("node:fs"),path=require("node:path"),os=require("node:os"),
 crypto=require("node:crypto"),cp=require("node:child_process");
const {buildRankOneCenteredIntegerSystem}=require("./2026-11-14-rank-one-centered-integer-system-generator.js");
const {translateRankOneCenteredSystem}=require("./2026-11-14-rank-one-centered-translation.js");
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a;};
const choose=(n,k)=>{let a=1n;for(let j=1;j<=k;j++)a=a*BigInt(n-j+1)/BigInt(j);return a;};
const trim=a=>{while(a.length>1&&a.at(-1)===0n)a.pop();return a;};
const mul=(a,b)=>{const c=Array(a.length+b.length-1).fill(0n);a.forEach((x,i)=>b.forEach((y,j)=>c[i+j]+=x*y));return trim(c);};
const peval=(a,s)=>a.reduceRight((x,c)=>x*s+c,0n);
function interpolateIntegers(values){
 const n=values.length-1,dd=values.slice(),d=[];let fact=1n;
 for(let k=0;k<=n;k++){d.push(dd[0]);for(let j=0;j<n-k;j++)dd[j]=dd[j+1]-dd[j];}
 for(let k=2;k<=n;k++)fact*=BigInt(k);
 let falling=[1n],kf=1n,out=Array(n+1).fill(0n);
 for(let k=0;k<=n;k++){
  const v=d[k]*(fact/kf);falling.forEach((x,j)=>out[j]+=v*x);
  falling=mul(falling,[-BigInt(k),1n]);kf*=BigInt(k+1);
 }
 return trim(out.map(x=>{if(x%fact)throw Error("nonintegral polynomial coefficient");return x/fact;}));
}
function parameterSystem(coordinates="original",report=()=>{}){
 if(!["original","translated"].includes(coordinates))throw Error("bad coordinates");
 const dataPath=path.join(__dirname,"2026-11-13-six-mode-cubic-bell-third-moment-exact-data.json"),
  raw=fs.readFileSync(dataPath),data=JSON.parse(raw),bound=coordinates==="original"?10:25;
 const sample=s=>{
  const mean=Array.from({length:6},(_,i)=>String(s**BigInt(i)));
  let z=buildRankOneCenteredIntegerSystem(data,mean);
  if(coordinates==="translated")z=translateRankOneCenteredSystem(z,s);
  return z.equations.map(e=>e.linear.concat(e.quadratic).map(x=>BigInt(x)*BigInt(e.scale)));
 };
 const values=[];
 for(let s=0;s<=bound;s++){values.push(sample(BigInt(s)));if(s%5===0)report({phase:"integer-reconstruction",sample:s,bound});}
 const equations=Array.from({length:17},(_,i)=>Array.from({length:77},(_,j)=>
  interpolateIntegers(values.map(v=>v[i][j]))));
 // The degree bound follows from the original formulas. These extra exact
 // specializations guard reconstruction and restoration of all row scales.
 let checks=0;
 for(const s of [-1n,BigInt(bound+1),BigInt(bound+2)]){
  const v=sample(s);
  equations.forEach((row,i)=>row.forEach((p,j)=>{if(peval(p,s)!==v[i][j])throw Error("fixed-D interpolation mismatch");checks++;}));
 }
 const contents=equations.map(row=>row.flat().reduce(gcd,0n));
 contents.forEach((c,i)=>{if(c===0n)throw Error("zero original generator");equations[i]=equations[i].map(p=>p.map(x=>x/c));});
 const quadraticMonomials=[];for(let i=0;i<11;i++)for(let j=i;j<11;j++)quadraticMonomials.push([i,j]);
 const maxDegrees=equations.map(row=>Math.max(...row.filter(p=>p.some(x=>x!==0n)).map(p=>p.length-1)));
 if(coordinates==="original"&&maxDegrees.some((d,i)=>d>(i<11?10:5)))throw Error("original parameter degree bound exceeded");
 return {equations,contents,quadraticMonomials,coordinates,bound,checks,maxDegrees,
  denominator:String(data.detJ3),sourceDataSHA256:crypto.createHash("sha256").update(raw).digest("hex")};
}
function pstring(a){
 const terms=[];a.forEach((v,i)=>{if(!v)return;let t=String(v);if(i)t+="*s"+(i>1?"^"+i:"");terms.push("("+t+")");});
 return terms.length?terms.join("+"):"0";
}
function systemPolynomials(z){
 const names=Array.from({length:11},(_,i)=>(z.coordinates==="original"?"m":"z")+i);
 return z.equations.map(row=>{
  const terms=[];
  row.forEach((p,j)=>{if(p.every(x=>x===0n))return;
   let mon;if(j<11)mon=names[j];else{const [a,b]=z.quadraticMonomials[j-11];mon=a===b?names[a]+"^2":names[a]+"*"+names[b];}
   terms.push("("+pstring(p)+")*"+mon);
  });return terms.join("+");
 });
}
function targets(z){
 return Array.from({length:9},(_,a)=>{
  const i=a+2;if(z.coordinates==="translated")return "z"+i+"^2";
  const t=[];for(let j=0;j<=i;j++){
   const c=choose(i,j)*(BigInt((i-j)%2)?-1n:1n);
   t.push("("+String(c)+")"+(i===j?"":"*s"+(i-j>1?"^"+(i-j):""))+"*m"+j);
  }return "("+t.join("+")+")^2";
 });
}
function singularProgram(z,opts,files){
 const p=opts.characteristic,vars=Array.from({length:11},(_,i)=>(z.coordinates==="original"?"m":"z")+(10-i));
 const I=systemPolynomials(z),T=targets(z),quoted=x=>JSON.stringify(x);
 const method=opts.algorithm==="std"?"std":"slimgb";
 const lines=["// Generated only from the original fixed-D system.",
  `ring R=(${p},s),(${vars.join(",")}),dp;`,"short=0;",`ideal I=${I.join(",\n")};`,
  `ideal T=${T.join(",\n")};`,"option(redSB);",'print("R150_BEGIN_BASIS");',
  `ideal B=${method}(I);`,'print("R150_BASIS_GENERATORS="+string(size(B)));',
  "int i; int j; int bad=0; poly rr;",
  "for(i=1;i<=size(T);i++){rr=reduce(T[i],B);if(rr!=0){bad++;print(\"R150_NONZERO_NORMAL_FORM=\"+string(i)+\":\"+string(rr));}}",
  `write(${quoted(files.basis)},"// Parameter-field standard basis; reconstruct original input with the accompanying runner.");`,
  `for(i=1;i<=size(B);i++){write(${quoted(files.basis)},"B["+string(i)+"]="+string(B[i])+";");}`,
  'print("R150_TARGET_FAILURES="+string(bad));'];
 if(opts.stage==="basis")return lines.concat('print("R150_DONE_BASIS");',"quit;").join("\n")+"\n";
 lines.push('if(bad!=0){print("R150_ABORT_NO_MEMBERSHIP");quit;}','print("R150_BEGIN_LIFT");',
  "matrix U;",`matrix C=lift(I,T,U,"${method}");`,"matrix check=matrix(I)*C-matrix(T);",
  'for(i=1;i<=ncols(check);i++){if(check[1,i]!=0){print("R150_LIFT_IDENTITY_FAILED");quit;}}',
  'print("R150_EXACT_LIFT_IDENTITY_VERIFIED");',
  `write(${quoted(files.certificate)},"// Exact certificate in the same parameter-field ring as the original generators.");`,
  `write(${quoted(files.certificate)},"matrix C["+string(nrows(C))+"]["+string(ncols(C))+"];");`,
  "ideal Den=1; int di=1; number dn; poly cc;",
  "for(i=1;i<=nrows(C);i++){for(j=1;j<=ncols(C);j++){",
  `if(C[i,j]!=0){write(${quoted(files.certificate)},"C["+string(i)+","+string(j)+"]="+string(C[i,j])+";");}`,
  "cc=C[i,j];while(cc!=0){dn=denominator(leadcoef(cc));if(dn!=1){di++;Den[di]=dn;}cc=cc-lead(cc);}","}}",
  "Den=simplify(Den,2+4);",`ring P=${p},s,dp;`,"short=0; ideal DD=imap(R,Den); poly d=1; poly a; int k;",
  "for(k=1;k<=size(DD);k++){a=DD[k];if(a!=0){d=d*(a/gcd(d,a));}}",
  "d=d/leadcoef(d);",
  `write(${quoted(files.denominator)},"// Denominator of an exact original-generator membership certificate.");`,
  `write(${quoted(files.denominator)},"poly denominatorPolynomial="+string(d)+";");`,
  'print("R150_DENOMINATOR_DEGREE="+string(deg(d)));',
  "poly known=s*(s-2)*(s+6)*(5*s^3-25*s^2+32*s-8)*(5*s^3+135*s^2+864*s+864)*(5*s^8+50*s^7+153*s^6-936*s^5-2888*s^4+15936*s^3-3392*s^2-25472*s+9600);",
  "poly residual=d;poly h=gcd(residual,known);",
  "while(deg(h)>0){residual=residual/h;h=gcd(residual,known);}",
  `write(${quoted(files.denominator)},"poly unresolvedDenominator="+string(residual)+";");`,
  'print("R150_UNRESOLVED_DENOMINATOR_DEGREE="+string(deg(residual)));',
  "list factors=factorize(residual);",
  `write(${quoted(files.denominator)},"// Irreducible factorization of unresolvedDenominator follows:");`,
  `write(${quoted(files.denominator)},string(factors));`,
  'print("R150_DONE_EXACT_MEMBERSHIP");',"quit;");
 return lines.join("\n")+"\n";
}
function singularInvocation(args){
 const limitMiB=Number(process.env.ISP_SINGULAR_MEMORY_MIB||0);
 if(!Number.isSafeInteger(limitMiB)||limitMiB<0)throw Error("bad Singular memory limit");
 return limitMiB?{command:"prlimit",args:["--as="+String(limitMiB*1024*1024),"--","Singular",...args],limitMiB}:
  {command:"Singular",args,limitMiB:0};
}
function singularInterfaceCheck(opts){
 const tmp=fs.mkdtempSync(path.join(os.tmpdir(),"r150-interface-")),file=path.join(tmp,"check.sing");
 fs.writeFileSync(file,[`ring R=(${opts.characteristic},s),x,dp;`,"short=0;",
  "ideal I=(s-1)*x;ideal T=x^2;matrix U;",
  `matrix C=lift(I,T,U,"${opts.algorithm}");`,
  "matrix Q=matrix(I)*C-matrix(T);",
  'if(Q[1,1]!=0){print("INTERFACE_IDENTITY_FAILURE");quit;}',
  "ideal Den=denominator(leadcoef(C[1,1]));",`ring P=${opts.characteristic},s,dp;`,
  "ideal DD=imap(R,Den);",
  'if(deg(DD[1])!=1){print("INTERFACE_DENOMINATOR_FAILURE");quit;}',
  'print("R150_INTERFACE_OK");quit;'].join("\n")+"\n");
 const invocation=singularInvocation(["-q",file]);
 const r=cp.spawnSync(invocation.command,invocation.args,{encoding:"utf8",timeout:30000,maxBuffer:1024*1024});
 if(r.error||r.status!==0||!r.stdout.split(/\r?\n/).some(x=>x.trim()==="R150_INTERFACE_OK")||/^\s*\?/m.test(r.stdout))throw Error("Singular interface check failed: "+String(r.error||r.stdout+"\n"+r.stderr));
}
async function main(){
 const args=process.argv.slice(2),o={characteristic:0,coordinates:"original",algorithm:"slimgb",stage:"lift",out:null,generateOnly:false};
 for(let i=0;i<args.length;i++){
  const a=args[i];if(a==="--generate-only"){o.generateOnly=true;continue;}
  const names={"--out":"out","--characteristic":"characteristic","--coordinates":"coordinates","--algorithm":"algorithm","--stage":"stage"};
  if(!names[a]||i+1===args.length)throw Error("bad argument "+a);o[names[a]]=args[++i];
 }
 o.characteristic=Number(o.characteristic);
 if(!Number.isSafeInteger(o.characteristic)||o.characteristic<0||!["std","slimgb"].includes(o.algorithm)||!["basis","lift"].includes(o.stage)||!o.out)throw Error("bad runner options");
 fs.mkdirSync(o.out,{recursive:true});o.out=path.resolve(o.out);
 if(!o.generateOnly)singularInterfaceCheck(o);
 const log=x=>process.stdout.write(JSON.stringify(x)+"\n"),z=parameterSystem(o.coordinates,log);
 if(o.characteristic>0){const pp=BigInt(o.characteristic);if(BigInt(z.denominator)%pp===0n||z.contents.some(c=>c%pp===0n))throw Error("prime divides original denominator or constant row content");}
 const tmp=fs.mkdtempSync(path.join(os.tmpdir(),"r150-parameter-")),files={
  basis:path.join(tmp,"basis.sing"),certificate:path.join(tmp,"certificate.sing"),denominator:path.join(o.out,"denominator.sing")};
 fs.writeFileSync(files.denominator,"");
 const script=singularProgram(z,o,files),scriptPath=path.join(tmp,"task.sing");fs.writeFileSync(scriptPath,script);
 const receipt={format:"R150-parameter-ideal-v1",options:o,workingFiles:files,temporaryWorkingDirectory:tmp,sourceDataSHA256:z.sourceDataSHA256,
  parameterDegreeBounds:z.maxDegrees,coefficientChecks:z.checks,constantRowContents:z.contents.map(String),
  originalCommonDenominator:z.denominator,inputSHA256:crypto.createHash("sha256").update(script).digest("hex"),
  polynomialSystemSHA256:crypto.createHash("sha256").update(JSON.stringify({equations:z.equations,targets:targets(z)},(_,v)=>typeof v==="bigint"?String(v):v)).digest("hex"),
  target:"Nine squared inverse-binomial transverse coordinates; all original 17 equations retained.",
  singularMemoryLimitMiB:singularInvocation([]).limitMiB,
  status:o.generateOnly?"input-generated-only":"running",started:new Date().toISOString()};
 const save=()=>fs.writeFileSync(path.join(o.out,"receipt.json"),JSON.stringify(receipt,null,2)+"\n");save();
 if(o.generateOnly){log({status:receipt.status,inputBytes:Buffer.byteLength(script),coefficientChecks:z.checks,temporaryInput:scriptPath});return;}
 log({phase:"parameter-input",polynomialSystemSHA256:receipt.polynomialSystemSHA256,
  coefficientChecks:z.checks,coordinates:o.coordinates,characteristic:o.characteristic,
  singularMemoryLimitMiB:receipt.singularMemoryLimitMiB});
 let detectedDone=false,exactIdentity=false,singularError=false,outputTail="";
 const invocation=singularInvocation(["-q",scriptPath]);
 const child=cp.spawn(invocation.command,invocation.args,{stdio:["ignore","pipe","pipe"]});
 const heartbeat=setInterval(()=>{
  let memory={};
  try{const stat=fs.readFileSync("/proc/"+child.pid+"/status","utf8");
   for(const key of ["VmSize","VmRSS","VmPeak","VmHWM"]){const m=stat.match(new RegExp("^"+key+":\\s+(\\d+) kB$","m"));if(m)memory[key+"KiB"]=Number(m[1]);}
  }catch{}
  log({phase:"singular-heartbeat",at:new Date().toISOString(),pid:child.pid,memory,
   exactIdentityVerified:exactIdentity,completionMarker:detectedDone});
 },45000);
 child.stdout.on("data",b=>{const s=String(b);process.stdout.write(s);outputTail=(outputTail+s).slice(-4096);const lines=outputTail.split(/\r?\n/).map(x=>x.trim());if(lines.includes("R150_DONE_EXACT_MEMBERSHIP")||lines.includes("R150_DONE_BASIS"))detectedDone=true;if(lines.includes("R150_EXACT_LIFT_IDENTITY_VERIFIED"))exactIdentity=true;if(/^\s*\?/m.test(outputTail)||lines.includes("R150_ABORT_NO_MEMBERSHIP")||lines.includes("R150_LIFT_IDENTITY_FAILED"))singularError=true;});
 child.stderr.on("data",b=>process.stderr.write(b));
 let completion;
 try{completion=await new Promise((resolve,reject)=>{child.on("error",reject);child.on("close",(code,signal)=>resolve({code,signal}));});}
 finally{clearInterval(heartbeat);}
 const code=completion.code;receipt.exitSignal=completion.signal;
 receipt.exitCode=code;receipt.completionMarker=detectedDone;receipt.exactIdentityVerified=exactIdentity;receipt.singularError=singularError;receipt.finished=new Date().toISOString();
 receipt.status=code===0&&detectedDone&&!singularError&&(o.stage==="basis"||exactIdentity)?"completed":"failed-or-incomplete";
 receipt.outputs={};
 const zlib=require("node:zlib");
 for(const [name,file] of Object.entries(files))if(fs.existsSync(file)){
  const data=fs.readFileSync(file);receipt.outputs[name]={bytes:data.length,sha256:crypto.createHash("sha256").update(data).digest("hex")};
  if(name!=="denominator"||data.length>1000000){
   const gz=zlib.gzipSync(data,{level:9});if(gz.length<=5000000){fs.writeFileSync(path.join(o.out,name+".sing.gz"),gz);receipt.outputs[name].savedCompressedBytes=gz.length;}
   else receipt.outputs[name].saved="hash-and-reproducible-command-only: compressed file exceeds repository 5 MB limit";
   if(name==="denominator")fs.unlinkSync(file);
  }
 }
 save();log({status:receipt.status,exactIdentityVerified:exactIdentity,outputs:receipt.outputs});
 if(receipt.status!=="completed")process.exitCode=1;
}
module.exports={interpolateIntegers,parameterSystem,systemPolynomials,targets,singularProgram};
if(require.main===module)main().catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
