// Exact continuation of the one saved full-companion characteristic input.
// Run: node this-file.mjs characteristic-input.json mean-differences.json [receipt.json]
import {readFileSync,writeFileSync} from "node:fs";
import {createHash} from "node:crypto";
const library=(()=>{

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
function must(p,m){if(!p)throw Error(m);}
function lex(a,b){for(let i=0;i<6;i++)if(a[i]!==b[i])return a[i]-b[i];return 0;}
function covers(p){const out=new Set;for(let i=0;i<6;i++)for(let j=i+1;j<6;j++){if(p[i]<p[j]+2)continue;const q=p.slice();q[i]--;q[j]++;q.sort((a,b)=>b-a);out.add(key(q));}return out;}
async function certify(raw,flow,io){
 const start=Date.now();
 must(raw.length===9168&&io.sha256(raw)==="3528a1b7b56167987e4c1c7c35048330a76cd2179ea263f49bf6cb29c4022bdf","unique original data");
 const input=parseJSONKeepingIntegers(raw);
 must(input.status==="EXACT_CHARACTERISTIC_READY"&&input.cayley_hamilton_return===true,"actual complete return");
 must(input.source_sha256==="bc8fd33a164d957fd07cfd02200985aa25dd511d902623ed5ed3591d1706a886","original source");
 must(input.complete_coefficients.length===5,"all five coefficients");
 const certificates=[];
 for(let k=1;k<=5;k++){
  const c=input.complete_coefficients[k-1];must(Number(c.index)===k,"source order");
  const shift=c.elementary_monomial_factor.map(Number),content=BigInt(c.positive_integer_content);
  must(content>0n&&shift.length===6&&shift.every(x=>Number.isInteger(x)&&x>=0),"positive removed factor");
  const rows=c.complete_reduced_elementary_coefficients.map(([p,v])=>({powers:p.map(Number),coefficient:BigInt(v)})).sort((a,b)=>lex(a.powers,b.powers));
  const reduced="["+rows.map(r=>"["+JSON.stringify(r.powers)+","+r.coefficient.toString()+"]").join(",")+"]";
  const original="["+rows.map(r=>"["+JSON.stringify(r.powers.map((e,i)=>e+shift[i]))+","+(content*r.coefficient).toString()+"]").join(",")+"]";
  must(io.sha256(reduced)===c.reduced_sha256&&io.sha256(original)===c.original_sha256,"complete original and reduced hashes");
  const degree=Number(c.reduced_weighted_degree);
  must(degree+shift.reduce((s,x,i)=>s+(i+1)*x,0)===9*k,"degree and positive factor");
  for(const r of rows)must(r.powers.length===6&&r.powers.every(x=>Number.isInteger(x)&&x>=0&&x<128)&&r.powers.reduce((s,x,i)=>s+(i+1)*x,0)===degree,"full reduced degree");
  const expanded=await expand(rows);
  const actual=new Map(expanded.polynomial),residual=new Map(actual);
  const moves=flow.records.find(x=>x.index===k)?.moves||[];
  for(const move of moves){
   const a=move.from,b=move.to,w=BigInt(move.weight);
   must(w>0n&&a.length===6&&b.length===6&&a.every((x,i)=>Number.isInteger(x)&&x>=0&&(i===0||x<=a[i-1]))&&b.every((x,i)=>Number.isInteger(x)&&x>=0&&(i===0||x<=b[i-1])),"positive mean difference");
   must(a.reduce((s,x)=>s+x,0)===degree&&covers(a).has(key(b)),"one legal transfer");
   residual.set(key(a),(residual.get(key(a))||0n)-w);
   residual.set(key(b),(residual.get(key(b))||0n)+w);
  }
  for(const[k,w]of residual){must(w>=0n,"no unpaid coefficient");if(!w)residual.delete(k);}
  must(residual.size>0,"strict positive remainder");
  const orbits=[...actual].map(([a,w])=>({p:unkey(a),w})).sort((a,b)=>lex(a.p,b.p));
  const canon="["+orbits.map(({p,w})=>"["+JSON.stringify(p)+","+w.toString()+"]").join(",")+"]";
  let minResidual=null;for(const w of residual.values())if(minResidual===null||w<minResidual)minResidual=w;
  certificates.push({index:k,reduced_weighted_degree:degree,elementary_records:rows.length,
    positive_integer_content:content.toString(),elementary_monomial_factor:shift,
    original_variable_orbits:actual.size,original_negative_orbits:[...actual.values()].filter(x=>x<0n).length,
    positive_mean_differences:moves.length,positive_remainder_orbits:residual.size,
    minimum_remainder_mean_weight:minResidual.toString(),equal_variable_mass:expanded.mass,
    original_mean_orbit_sha256:io.sha256(canon)});
 }
 return {schema:"isp-six-site-full-half-positive-characteristic-certificate-v1",status:"CERTIFIED",
   original_input_sha256:io.sha256(raw),original_source_sha256:input.source_sha256,
   complete_characteristic_coefficients:5,cayley_hamilton_return:true,certificates,
   statement:"All five full physical nonzero characteristic coefficients are strictly positive for every six positive weights. Hence C2^2-2C3 is positive on the entire physical primitive K1 and the first adjacent Gram constant is strictly 1/2.",
   scope:"Full six-site source, not a separate support block. Reciprocal-weight duality gives the same last edge. No general birth, infinite joint source, or ordinary ISP conclusion.",
   elapsed_ms:Date.now()-start};
}
return {certify};

})();
const raw=readFileSync(process.argv[2],"utf8"),flow=JSON.parse(readFileSync(process.argv[3],"utf8"));
const io={sha256:s=>createHash("sha256").update(Buffer.from(s,"latin1")).digest("hex")};
const receipt=await library.certify(raw,flow,io);
receipt.execution="Node.js exact BigInt, built-in modules only";
const output=JSON.stringify(receipt,null,2)+"\n";
if(process.argv[4])writeFileSync(process.argv[4],output);
process.stdout.write(output);
