// Exact continuation from one saved original scalar input; no matrix calculation is repeated.
// Run: node this-file.mjs exact-scalar-input.json mean-differences.json [receipt.json]
import {readFileSync,writeFileSync} from "node:fs";
import {inflateSync} from "node:zlib";
import {createHash} from "node:crypto";
const library=(()=>{

const N=5,BASE=128,ENC=[1,128,16384,2097152,268435456],SHIFT=ENC.reduce((a,b)=>a+b,0);
const factorial=[1n];for(let i=1;i<=200;i++)factorial.push(factorial.at(-1)*BigInt(i));
function key(part){return part.reduce((s,x,i)=>s+x*ENC[i],0);}
function unkey(k){return ENC.map(e=>Math.floor(k/e)%BASE);}
function multiplicity(part){let d=1n;for(let i=0;i<N;){let j=i+1;while(j<N&&part[i]===part[j])j++;d*=factorial[j-i];i=j;}return factorial[N]/d;}
function partitions(n,m=N,max=n){if(!m)return n?[]:[[]];let out=[];for(let a=Math.min(n,max);a>=0;a--)for(const p of partitions(n-a,m-1,a))out.push([a,...p]);return out;}
function subsets(k,start=0){if(!k)return[[]];let out=[];for(let j=start;j<=N-k;j++)for(let s of subsets(k-1,j+1))out.push([j,...s]);return out;}
const choices=Array.from({length:6},(_,k)=>subsets(k)),SCache=new Map;
function SPower(n){if(SCache.has(n))return SCache.get(n);const p=new Map;for(let part of partitions(n)){let q=factorial[n];for(const a of part)q/=factorial[a];p.set(key(part),q*multiplicity(part));}SCache.set(n,p);return p;}
function plus(a,b){const c=new Map(a);for(const[k,v]of b){let w=(c.get(k)||0n)+v;if(w)c.set(k,w);else c.delete(k);}return c;}
function times(a,c){if(!c)return new Map;return new Map([...a].map(([k,v])=>[k,v*c]));}
function multiplyElementary(p,k){
 if(k===5)return new Map([...p].map(([q,v])=>[q+SHIFT,v]));
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
 const out=await rec(records,4);
 let expected=0n;const binom=[5n,10n,10n,5n,1n];
 for(const r of records){let v=r.coefficient;for(let j=0;j<5;j++)v*=binom[j]**BigInt(r.powers[j]);expected+=v;}
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
function must(p,m){if(!p)throw Error(m);}
function lex(a,b){for(let i=0;i<5;i++)if(a[i]!==b[i])return a[i]-b[i];return 0;}
function covers(p){const out=new Set;for(let i=1;i<5;i++)for(let j=i+1;j<5;j++){if(p[i]<p[j]+2)continue;let q=p.slice();q[i]--;q[j]++;q.sort((a,b)=>b-a);out.add(key(q));}return out;}
async function certify(envelope,flow,io){
 const start=Date.now(),raw=io.inflate(envelope.base64);
 must(raw.length===envelope.uncompressed_bytes&&io.sha256(raw)===envelope.uncompressed_sha256,"original exact input");
 const input=parseJSONKeepingIntegers(raw);
 must(input.source_sha256===envelope.source.sha256&&input.status==="EXACT_SCALAR_READY","same original source");
 const rows=input.complete_elementary_coefficients.map(r=>({powers:r.powers.map(Number),v:r.coefficients.map(BigInt)}));
 for(const r of rows)must(r.v[3]===3n*r.v[1]-16n*r.v[0],"same stronger gap");
 const col=rows.filter(r=>r.v[3]).sort((a,b)=>lex(a.powers,b.powers));
 const canon="["+col.map(r=>"["+JSON.stringify(r.powers)+","+r.v[3].toString()+"]").join(",")+"]";
 must(io.sha256(canon)===input.three_sixteenths_gap.sha256,"exact stronger gap digest");
 const expanded=await expand(rows.map(r=>({powers:r.powers,coefficient:r.v[3]})).filter(r=>r.coefficient));
 const head=new Map,tail=new Map;
 for(const[k,w]of expanded.polynomial){const p=unkey(k);must(p.reduce((a,b)=>a+b,0)===98,"degree");if(p[0]===36)head.set(k,w);else{must(w>0n,"strictly positive remainder");tail.set(k,w);}}
 must(head.size===458&&tail.size===6478,"all source orbits");
 must([...head.values()].reduce((a,b)=>a+b,0n)===0n,"zero leading mass");
 const balance=new Map;for(const move of flow.moves){
  const a=move.from,b=move.to,w=BigInt(move.weight);
  must(a.length===5&&b.length===5&&a[0]===36&&b[0]===36&&w>0n,"positive mean difference");
  must(a.every((x,i)=>Number.isInteger(x)&&x>=0&&(i===0||x<=a[i-1]))&&b.every((x,i)=>Number.isInteger(x)&&x>=0&&(i===0||x<=b[i-1])),"partitions");
  must(covers(a).has(key(b)),"single Robin-Hood transfer among the four tail exponents");
  balance.set(key(a),(balance.get(key(a))||0n)+w);balance.set(key(b),(balance.get(key(b))||0n)-w);
 }
 const keys=new Set([...head.keys(),...balance.keys()]);
 for(const k of keys)must((head.get(k)||0n)===(balance.get(k)||0n),"complete coefficient conservation");
 let minCoefficient=null,monomials=0n;
 for(const[k,w]of tail){const m=multiplicity(unkey(k));must(w%m===0n,"integral positive remainder");const c=w/m;if(minCoefficient===null||c<minCoefficient)minCoefficient=c;monomials+=m;}
 const all=[...expanded.polynomial].map(([k,w])=>({p:unkey(k),w})).sort((a,b)=>lex(a.p,b.p));
 const orbitCanon="["+all.map(({p,w})=>"["+JSON.stringify(p)+","+w.toString()+"]").join(",")+"]";
 return {
  schema:"isp-five-bit-s2-three-sixteenths-mean-certificate-v1",status:"CERTIFIED",
  input_source:envelope.source,exact_input_sha256:envelope.uncompressed_sha256,
  elementary_records:rows.length,original_degree:98,total_orbits:all.length,
  leading_orbits:head.size,leading_negative_orbits:[...head.values()].filter(x=>x<0n).length,
  leading_total_mean_weight:"0",positive_mean_differences:flow.moves.length,
  negative_mean_demand:[...head.values()].filter(x=>x<0n).reduce((s,x)=>s-x,0n).toString(),
  strictly_positive_remainder_orbits:tail.size,remainder_monomials:monomials.toString(),
  minimum_positive_remainder_coefficient:minCoefficient.toString(),
  equal_variable_mass:expanded.mass,orbit_sha256:io.sha256(orbitCanon),
  statement:"3D-16N is a sum of 472 positive multiples of single-transfer symmetric mean differences and 6478 strictly positive monomial orbits. Hence Tr_L((A*Gu A)^2)<3/16 and full five-site S2 has uniform budget (2+sqrt(3))/4.",
  scope:"Same original five-site full primitive source. No optimality, arbitrary-birth, infinite source, or ordinary ISP assertion.",
  elapsed_ms:Date.now()-start
 };
}
return {certify};

})();
const input=JSON.parse(readFileSync(process.argv[2],"utf8"));
const flow=JSON.parse(readFileSync(process.argv[3],"utf8"));
const io={inflate:s=>inflateSync(Buffer.from(s,"base64")).toString("latin1"),
          sha256:s=>createHash("sha256").update(Buffer.from(s,"latin1")).digest("hex")};
const receipt=await library.certify(input,flow,io);
receipt.execution="Node.js exact BigInt; built-in modules only";
const output=JSON.stringify(receipt,null,2)+"\n";
if(process.argv[4])writeFileSync(process.argv[4],output);
process.stdout.write(output);
