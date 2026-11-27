// Exact continuation of the captured scalar input; no matrix construction is repeated.
// Run: node this-file.mjs path/to/exact-scalar-input.json [receipt-output.json]
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
function emul(a,b){const r=new Map;for(const[k,c]of a)for(const[h,d]of b){const v=(r.get(k+h)||0n)+c*d;if(v)r.set(k+h,v);else r.delete(k+h);}return r;}
function epow(a,n){let r=new Map([[0,1n]]);for(let i=0;i<n;i++)r=emul(r,a);return r;}
async function certify(envelope,io){
 const start=Date.now(),raw=io.inflate(envelope.base64);
 must(raw.length===envelope.uncompressed_bytes,"raw byte count");
 must(io.sha256(raw)===envelope.uncompressed_sha256,"raw SHA256");
 const input=parseJSONKeepingIntegers(raw);
 must(input.status==="EXACT_SCALAR_READY","actual checkpoint status");
 must(input.source_sha256===envelope.source.sha256,"actual source SHA256");
 const rows=input.complete_elementary_coefficients.map(r=>({powers:r.powers.map(Number),v:r.coefficients.map(BigInt)}));
 const seen=new Set;for(const r of rows){
  must(r.powers.length===5&&r.powers.every(x=>Number.isSafeInteger(x)&&x>=0&&x<128),"exponent range");
  const k=key(r.powers);must(!seen.has(k),"duplicate exponent");seen.add(k);
  must(r.powers.reduce((s,x,i)=>s+(i+1)*x,0)===98,"weighted degree");
  must(r.v[2]===r.v[1]-4n*r.v[0]&&r.v[3]===3n*r.v[1]-16n*r.v[0],"same numerator gaps");
 }
 const columns=["N","D","gap","three_sixteenths_gap"];
 for(let c=0;c<4;c++){
  const a=rows.filter(r=>r.v[c]).sort((a,b)=>lex(a.powers,b.powers));
  const canon="["+a.map(r=>"["+JSON.stringify(r.powers)+","+r.v[c].toString()+"]").join(",")+"]";
  must(io.sha256(canon)===input[columns[c]].sha256,"column digest "+columns[c]);
 }
 const delta=new Map([[key([2,0,1,0,0]),1n],[key([1,0,0,1,0]),-4n],[key([0,0,0,0,1]),12n]]);
 const epsilon=new Map([[key([0,1,0,2,0]),1n],[key([1,0,0,1,1]),-4n],[key([0,0,0,0,2]),12n]]);
 const denominator=emul(new Map([[key([2,0,0,4,0]),1n]]),emul(epow(delta,4),epow(epsilon,6)));
 const actualD=new Map(rows.filter(r=>r.v[1]).map(r=>[key(r.powers),r.v[1]]));
 must(denominator.size===actualD.size&&[...denominator].every(([k,v])=>actualD.get(k)===v),"exact denominator factorization");
 const expanded=await expand(rows.map(r=>({powers:r.powers,coefficient:r.v[2]})).filter(r=>r.coefficient));
 let monomials=0n,minCoefficient=null,minMeanWeight=null;
 const orbitRows=[...expanded.polynomial].map(([k,w])=>({p:unkey(k),w})).sort((a,b)=>lex(a.p,b.p));
 for(const {p,w}of orbitRows){
  must(p.reduce((a,b)=>a+b,0)===98&&p.every((x,i)=>i===0||x<=p[i-1]),"original partition");
  const mult=multiplicity(p);must(w>0n&&w%mult===0n,"positive integral original coefficients");
  const c=w/mult;monomials+=mult;
  if(minCoefficient===null||c<minCoefficient)minCoefficient=c;
  if(minMeanWeight===null||w<minMeanWeight)minMeanWeight=w;
 }
 must(orbitRows.length===6936,"all orbit count");
 const orbitCanon="["+orbitRows.map(({p,w})=>"["+JSON.stringify(p)+","+w.toString()+"]").join(",")+"]";
 return {
  schema:"isp-five-bit-s2-quarter-positive-integer-certificate-v1",
  status:"CERTIFIED",input_source:envelope.source,
  exact_input_bytes:raw.length,exact_input_sha256:envelope.uncompressed_sha256,
  elementary_records:rows.length,denominator_terms:denominator.size,
  denominator:"e1^2 e4^4 (e1^2 e3-4 e1 e4+12 e5)^4 (e4^2 e2-4 e1 e4 e5+12 e5^2)^6",
  original_degree:98,positive_orbits:orbitRows.length,negative_orbits:0,
  original_monomials:monomials.toString(),
  min_original_coefficient:minCoefficient.toString(),min_mean_weight:minMeanWeight.toString(),
  equal_variable_mass:expanded.mass,horner_nodes:expanded.nodes,orbit_sha256:io.sha256(orbitCanon),
  statement:"D-4N has strictly positive coefficients on its 6936 nonzero symmetric monomial orbits; hence Tr_L((A*Gu A)^2)<1/4 for all five positive weights.",
  scope:"Same full physical source, full upper MP projection, all mixed blocks retained. This proves five-site S2 and the R275 six-site birth-two first edge; it makes no all-birth, infinite joint-source, or ordinary ISP claim.",
  elapsed_ms:Date.now()-start
 };
}
return {certify};

})();
const input=JSON.parse(readFileSync(process.argv[2],"utf8"));
const io={inflate:s=>inflateSync(Buffer.from(s,"base64")).toString("latin1"),
          sha256:s=>createHash("sha256").update(Buffer.from(s,"latin1")).digest("hex")};
const receipt=await library.certify(input,io);
receipt.execution="Node.js exact BigInt; this entry point uses only built-in modules";
const output=JSON.stringify(receipt,null,2)+"\n";
if(process.argv[3])writeFileSync(process.argv[3],output);
process.stdout.write(output);
