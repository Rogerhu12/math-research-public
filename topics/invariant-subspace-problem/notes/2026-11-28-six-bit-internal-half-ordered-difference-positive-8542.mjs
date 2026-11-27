// Exact continuation of the unique saved six-site internal characteristic.
// 2026-11-28 Asia/Taipei; no original matrix/inverse replay.
import {readFileSync,writeFileSync} from "node:fs";
const lib=(()=>{

function sha256Stream(){
 const K=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
 const H=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19],buf=new Uint8Array(64),w=new Uint32Array(64);let pos=0,bytes=0,done=false;
 const rr=(x,n)=>(x>>>n)|(x<<(32-n));
 function block(){for(let i=0;i<16;i++)w[i]=((buf[4*i]<<24)|(buf[4*i+1]<<16)|(buf[4*i+2]<<8)|buf[4*i+3])>>>0;
  for(let i=16;i<64;i++){const a=w[i-15],b=w[i-2],s0=rr(a,7)^rr(a,18)^(a>>>3),s1=rr(b,17)^rr(b,19)^(b>>>10);w[i]=(w[i-16]+s0+w[i-7]+s1)>>>0;}
  let[a,b,c,d,e,f,g,h]=H;for(let i=0;i<64;i++){const x=(h+(rr(e,6)^rr(e,11)^rr(e,25))+((e&f)^(~e&g))+K[i]+w[i])>>>0,y=((rr(a,2)^rr(a,13)^rr(a,22))+((a&b)^(a&c)^(b&c)))>>>0;h=g;g=f;f=e;e=(d+x)>>>0;d=c;c=b;b=a;a=(x+y)>>>0;}
  const r=[a,b,c,d,e,f,g,h];for(let i=0;i<8;i++)H[i]=(H[i]+r[i])>>>0;
 }
 function byte(x){buf[pos++]=x;bytes++;if(pos===64){block();pos=0;}}
 function update(s){if(done)throw Error("hash finalized");for(let i=0;i<s.length;i++){const x=s.charCodeAt(i);if(x>255)throw Error("non-byte string");byte(x);}return api;}
 function hex(){if(done)throw Error("hash finalized");const bits=bytes*8,hi=Math.floor(bits/4294967296),lo=bits>>>0;byte(128);while(pos!==56)byte(0);for(let j=3;j>=0;j--)byte((hi>>>(8*j))&255);for(let j=3;j>=0;j--)byte((lo>>>(8*j))&255);done=true;return H.map(x=>x.toString(16).padStart(8,"0")).join("");}
 const api={update,hex};return api;
}

const N=6,BASE=128,ENC=[1,128,16384,2097152,268435456,34359738368],SHIFT=ENC.reduce((a,b)=>a+b,0);
const factorial=[1n];for(let i=1;i<=200;i++)factorial.push(factorial.at(-1)*BigInt(i));
function key(part){return part.reduce((s,x,i)=>s+x*ENC[i],0);}
function unkey(k){return ENC.map(e=>Math.floor(k/e)%BASE);}
function multiplicity(part){let d=1n;for(let i=0;i<N;){let j=i+1;while(j<N&&part[i]===part[j])j++;d*=factorial[j-i];i=j;}return factorial[N]/d;}
function partitions(n,m=N,max=n){if(!m)return n?[]:[[]];let out=[];for(let a=Math.min(n,max);a>=0;a--)for(const p of partitions(n-a,m-1,a))out.push([a,...p]);return out;}
function subsets(k,start=0){if(!k)return[[]];let out=[];for(let j=start;j<=N-k;j++)for(let s of subsets(k-1,j+1))out.push([j,...s]);return out;}
const choices=Array.from({length:7},(_,k)=>subsets(k)),SCache=new Map;
function SPower(n){if(SCache.has(n))return SCache.get(n);const p=new Map;for(let part of partitions(n)){let q=factorial[n];for(const a of part)q/=factorial[a];p.set(key(part),q*multiplicity(part));}SCache.set(n,p);return p;}
function plus(a,b){const c=new Map(a);for(const[k,v]of b){let w=(c.get(k)||0n)+v;if(w)c.set(k,w);else c.delete(k);}return c;}
function times(a,c){if(!c)return new Map;return new Map([...a].map(([k,v])=>[k,v*c]));}
function multiplyElementary(p,k){
 if(k===6)return new Map([...p].map(([q,v])=>[q+SHIFT,v]));
 const out=new Map;
 for(const[q,v]of p){const part=unkey(q);for(const I of choices[k]){let b=part.slice();for(const i of I)b[i]++;b.sort((a,b)=>b-a);const h=key(b),w=(out.get(h)||0n)+v;if(w)out.set(h,w);else out.delete(h);}}
 return out;
}
async function expand(records,progress){
 let nodes=0,last=Date.now();
 async function rec(rows,index){
  nodes++;
  if(index===0){let p=new Map;for(const {powers,coefficient}of rows)p=plus(p,times(SPower(powers[0]),coefficient));return p;}
  const groups=new Map;for(const r of rows){let e=r.powers[index];if(!groups.has(e))groups.set(e,[]);groups.get(e).push(r);}
  const exps=[...groups.keys()].sort((a,b)=>b-a);let power=exps[0],out=await rec(groups.get(power),index-1);
  for(let j=1;j<exps.length;j++){
   const next=exps[j];while(power>next){out=multiplyElementary(out,index+1);power--;}
   out=plus(out,await rec(groups.get(next),index-1));
   if(progress&&Date.now()-last>500){last=Date.now();await progress({nodes,index,power,terms:out.size});}
  }
  while(power>0){out=multiplyElementary(out,index+1);power--;}
  return out;
 }
 const out=await rec(records,5);
 let expected=0n;const binom=[6n,15n,20n,15n,6n,1n];
 for(const r of records){let v=r.coefficient;for(let j=0;j<6;j++)v*=binom[j]**BigInt(r.powers[j]);expected+=v;}
 const actual=[...out.values()].reduce((a,b)=>a+b,0n);if(actual!==expected)throw Error("equal-variable mass mismatch");
 for(const[q,v]of out){const p=unkey(q);if(v%multiplicity(p))throw Error("nonintegral monomial coefficient");}
 return {polynomial:out,nodes,mass:String(actual)};
}




function parseJSONKeepingIntegers(raw){
 let out="",i=0;
 while(i<raw.length){
  const ch=raw[i];
  if(ch==='"'){
   const start=i++;
   while(i<raw.length){if(raw[i]==="\\"){i+=2;continue;}if(raw[i++]==='"')break;}
   out+=raw.slice(start,i);continue;
  }
  if(ch==="-"||(ch>="0"&&ch<="9")){
   const start=i;let integer=true;if(raw[i]==="-")i++;
   while(i<raw.length&&raw[i]>="0"&&raw[i]<="9")i++;
   if(raw[i]==="."){integer=false;i++;while(i<raw.length&&raw[i]>="0"&&raw[i]<="9")i++;}
   if(raw[i]==="e"||raw[i]==="E"){integer=false;i++;if(raw[i]==="+"||raw[i]==="-")i++;while(i<raw.length&&raw[i]>="0"&&raw[i]<="9")i++;}
   const token=raw.slice(start,i);out+=integer?'"'+token+'"':token;continue;
  }
  out+=ch;i++;
 }
 return JSON.parse(out);
}


const ORD_BASE=32,ORD_ENC=[1,32,1024,32768,1048576,33554432];
const ordKey=p=>p.reduce((s,x,i)=>s+x*ORD_ENC[i],0);
function uniqPermutations(p){
 const c=new Map;for(const x of p)c.set(x,(c.get(x)||0)+1);
 const entries=[...c],out=[],q=[];
 function go(){if(q.length===6){out.push(q.slice());return;}for(const e of entries)if(e[1]){e[1]--;q.push(e[0]);go();q.pop();e[1]++;}}
 go();return out;
}
function elementaryOf(z){const e=[1n,0n,0n,0n,0n,0n,0n];for(const x of z)for(let j=6;j>0;j--)e[j]+=x*e[j-1];return e.slice(1);}
function evaluateElementary(rows,x){
 const max=Array(6).fill(0);for(const r of rows)for(let i=0;i<6;i++)max[i]=Math.max(max[i],r.powers[i]);
 const powers=x.map((v,i)=>{const a=[1n];for(let k=1;k<=max[i];k++)a.push(a.at(-1)*v);return a;});
 let sum=0n;for(const r of rows){let a=r.coefficient;for(let i=0;i<6;i++)a*=powers[i][r.powers[i]];sum+=a;}return sum;
}
function orderedSubstitution(data,degree){
 const start=Date.now(),steps=[],choose=Array.from({length:31},(_,i)=>{const a=[1n];for(let k=1;k<=i;k++)a.push(a[k-1]*BigInt(i-k+1)/BigInt(k));return a;});
 let p=new Map,total=0n;
 for(const [v,w0]of data){
  if(v.some(x=>x<0||x>=32)||v.reduce((s,x)=>s+x,0)!==degree)throw Error("monomial encoding or degree");
  const w=BigInt(w0),per=uniqPermutations(v),n=BigInt(per.length);if(w%n)throw Error("nonintegral original coefficient");const c=w/n;
  for(const r of per){const k=ordKey(r);if(p.has(k))throw Error("duplicate original monomial");p.set(k,c);}total+=w;
 }
 if([...p.values()].reduce((a,b)=>a+b,0n)!==total)throw Error("original equal-variable mass");
 const stats=stage=>({stage,terms:p.size,negative:[...p.values()].filter(x=>x<0n).length});
 steps.push(stats("complete_original_monomials"));
 for(let i=0;i<5;i++){
  const q=new Map,delta=ORD_ENC[i+1]-ORD_ENC[i];
  for(const[k,c]of p){const a=Math.floor(k/ORD_ENC[i])%ORD_BASE;for(let j=0;j<=a;j++){const h=k+j*delta,v=(q.get(h)||0n)+c*choose[a][j];if(v)q.set(h,v);else q.delete(h);}}
  p=q;steps.push(stats("z"+(i+1)+"_to_x"+(i+1)+"_plus_z"+(i+2)));
 }
 let min=null,mass=0n;for(const c of p.values()){if(c<=0n)throw Error("nonpositive final coefficient");if(min===null||c<min)min=c;mass+=c;}
 const diagonal=p.get(degree*ORD_ENC[5])||0n;
 if(diagonal!==total||diagonal<=0n)throw Error("strict positive diagonal boundary");
 const digest=sha256Stream();let tableBytes=0;
 for(const[k,c]of [...p].sort((a,b)=>a[0]-b[0])){const line=k+":"+c+"\n";tableBytes+=line.length;digest.update(line);}
 return {degree,complete_coefficients:p.size,negative_coefficients:0,min_positive_coefficient:String(min),
  x6_power_coefficient:String(diagonal),all_x_equal_one_mass:String(mass),sha256:digest.hex(),
  digest_format:"ascending base-32 monomial key, colon, signed integer coefficient, LF",
  encoding:ORD_ENC,unarchived_table_bytes:tableBytes,stages:steps,elapsed_ms:Date.now()-start};
}
async function run(raw){
 const start=Date.now(),hash=sha256Stream().update(raw).hex();
 if(raw.length!==37383||hash!=="694657b7a7c0315d6c4f137122ef84c77f35bae2fe077deee4c31c85ba4cd4be")throw Error("unique original input");
 const input=parseJSONKeepingIntegers(raw);
 if(input.status!=="EXACT_CHARACTERISTIC_READY"||input.cayley_hamilton_return!==true)throw Error("complete original characteristic return");
 const result=[];
 for(const r of input.complete_coefficients.slice(3)){
  const records=r.complete_reduced_elementary_coefficients.map(([p,c])=>({powers:p.map(Number),coefficient:BigInt(c)}));
  const expanded=await expand(records),data=[...expanded.polynomial].map(([k,w])=>[unkey(k),String(w)]),degree=Number(r.reduced_weighted_degree);
  const o=orderedSubstitution(data,degree);
  const expected=evaluateElementary(records,elementaryOf([6n,5n,4n,3n,2n,1n]));
  if(String(expected)!==o.all_x_equal_one_mass)throw Error("exact independent ordered evaluation");
  result.push({index:Number(r.index),elementary_records:records.length,original_orbits:data.length,
   original_positive_integer_content:r.positive_integer_content,original_positive_factor_powers:r.positive_factor_powers,
   reduced_elementary_sha256:r.reduced_sha256,equal_variable_mass:expanded.mass,...o});
 }
 return {schema:"isp-six-internal-half-ordered-difference-positive-v1",status:"BOTH_REMAINING_COEFFICIENTS_STRICTLY_POSITIVE",
  original_input_sha256:hash,original_source_sha256:input.source_sha256,
  original_matrix:input.actual_matrix,complete_original_characteristic_return:true,
  coefficients:result,elapsed_ms:Date.now()-start,
  scope:"Only the two saved reduced coefficients f4 and f5 are transformed. Together with the already proved positive f1,f2,f3 and the original complete real characteristic, this proves the same six-site internal j=2 half inequality. No original matrix or inverse is recomputed."};
}
return {run};

})();
const result=await lib.run(readFileSync(process.argv[2],"utf8"));
const output=JSON.stringify(result,null,2)+"\n";
if(process.argv[3])writeFileSync(process.argv[3],output);process.stdout.write(output);
