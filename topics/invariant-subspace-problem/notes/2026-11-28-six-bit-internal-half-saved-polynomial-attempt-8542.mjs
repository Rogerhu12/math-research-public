// Only saved complete polynomial data; no original matrix computation.
import {readFileSync,writeFileSync} from "node:fs";
import {createHash} from "node:crypto";
const lib=(()=>{

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



function pars(n,m,max=n){if(!m)return n?[]:[[]];let a=[];for(let x=Math.min(n,max);x>=0;x--)for(const p of pars(n-x,m-1,x))a.push([x,...p]);return a;}
function pk(p){return p.join(",");}
function covers(p){const a=new Map;for(let i=0;i<6;i++)for(let j=i+1;j<6;j++){if(p[i]<p[j]+2)continue;const q=p.slice();q[i]--;q[j]++;q.sort((a,b)=>b-a);a.set(pk(q),q);}return [...a.values()];}
function solve(data){
 const polys=data.map(([p,w])=>({p:p.slice(),w:BigInt(w)})); const degree=polys[0].p.reduce((a,b)=>a+b,0);
 const demand=polys.reduce((s,x)=>s+(x.w<0n?-x.w:0n),0n),states=pars(degree,6,degree),idx=new Map(states.map((p,i)=>[pk(p),i])),n=states.length,src=n,snk=n+1,graph=Array.from({length:n+2},()=>[]);
 function edge(a,b,c,kind){const e={to:b,rev:graph[b].length,cap:c,orig:c,kind};const r={to:a,rev:graph[a].length,cap:0n,orig:0n};graph[a].push(e);graph[b].push(r);}
 for(let i=0;i<n;i++)for(const q of covers(states[i]))edge(i,idx.get(pk(q)),demand,"move");
 for(const {p,w}of polys){const i=idx.get(pk(p));if(w>0n)edge(src,i,w,"supply");else if(w<0n)edge(i,snk,-w,"demand");}
 let flow=0n;
 while(flow<demand){
  const level=Array(n+2).fill(-1);level[src]=0;const queue=[src];for(let h=0;h<queue.length;h++)for(const e of graph[queue[h]])if(e.cap>0n&&level[e.to]<0){level[e.to]=level[queue[h]]+1;queue.push(e.to);}
  if(level[snk]<0)break;
  const it=Array(n+2).fill(0);
  function dfs(u,pushed){if(u===snk)return pushed;for(;it[u]<graph[u].length;it[u]++){const e=graph[u][it[u]];if(e.cap<=0n||level[e.to]!==level[u]+1)continue;const q=dfs(e.to,pushed<e.cap?pushed:e.cap);if(q){e.cap-=q;graph[e.to][e.rev].cap+=q;return q;}}return 0n;}
  while(flow<demand){const q=dfs(src,demand-flow);if(!q)break;flow+=q;}
 }
 const moves=[],balance=new Map,remaining=[];
 for(let i=0;i<n;i++)for(const e of graph[i])if(e.kind==="move"&&e.orig>e.cap){const q=e.orig-e.cap;balance.set(pk(states[i]),(balance.get(pk(states[i]))||0n)+q);balance.set(pk(states[e.to]),(balance.get(pk(states[e.to]))||0n)-q);moves.push({from:states[i],to:states[e.to],weight:q.toString()});}
 for(const e of graph[src])if(e.kind==="supply"&&e.cap){balance.set(pk(states[e.to]),(balance.get(pk(states[e.to]))||0n)+e.cap);remaining.push({partition:states[e.to],weight:e.cap.toString()});}
 if(flow===demand){const target=new Map(polys.map(x=>[pk(x.p),x.w]));for(const [k,w]of balance)if(w!==(target.get(k)||0n))throw Error("balance");for(const [k,w]of target)if(w!==(balance.get(k)||0n))throw Error("missing balance");}
 return {passed:flow===demand,nodes:n,demand:demand.toString(),flow:flow.toString(),moves,remaining};
}



function elementary(z){const e=[1n,0n,0n,0n,0n,0n,0n];for(const x of z)for(let j=6;j>0;j--)e[j]+=x*e[j-1];return e.slice(1);}
function evalp(p,e){const cache=e.map((x,j)=>{const m=Math.max(...p.map(r=>r.p[j]));const q=[1n];for(let i=1;i<=m;i++)q.push(q.at(-1)*x);return q;});let v=0n;for(const r of p){let c=r.c;for(let j=0;j<6;j++)c*=cache[j][r.p[j]];v+=c;}return v;}
function multisets(n,m,min=1){if(!n)return[[]];let out=[];for(let a=min;a<=m;a++)for(const tail of multisets(n-1,m,a))out.push([a,...tail]);return out;}
function search(polys){
 const seen=new Set,checks=[];let seed=680713549;
 function rnd(){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed/4294967296;}
 const candidates=multisets(6,5).concat(Array.from({length:1500},(_,i)=>Array.from({length:6},()=>i<500?1+Math.floor(12*rnd()):2**Math.floor(12*rnd()))));
 for(const b0 of candidates){const b=b0.slice().sort((a,b)=>a-b);if(seen.has(b.join(",")))continue;seen.add(b.join(","));
  const z=b.map(x=>BigInt(x)**2n),e=elementary(z),values=polys.map(p=>evalp(p,e));
  if(values.some(v=>v<0n))return {status:"exact_negative_found",seed_initial:680713549,tested:seen.size,b,z:z.map(String),values:values.map(String)};
 }
 return {status:"no_negative_in_this_finite_screen",seed_initial:680713549,tested:seen.size,scope:"No positive-weight theorem follows from this finite exact screen."};
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
async function run(raw,sha256){
 const start=Date.now();if(raw.length!==37383||sha256(raw)!=="694657b7a7c0315d6c4f137122ef84c77f35bae2fe077deee4c31c85ba4cd4be")throw Error("original input");
 const input=parseJSONKeepingIntegers(raw);if(input.status!=="EXACT_CHARACTERISTIC_READY"||!input.cayley_hamilton_return)throw Error("actual status");
 const rows=[];
 for(const r of input.complete_coefficients){
  const records=r.complete_reduced_elementary_coefficients.map(([p,c])=>({powers:p.map(Number),coefficient:BigInt(c)}));
  const a=await expand(records),data=[...a.polynomial].map(([k,w])=>[unkey(k),String(w)]);
  const negatives=data.filter(x=>BigInt(x[1])<0n),flow=negatives.length?solve(data):null;
  rows.push({index:Number(r.index),degree:Number(r.reduced_weighted_degree),elementary_records:records.length,
    original_orbits:data.length,negative_orbits:negatives.length,equal_variable_mass:a.mass,
    complete_dominance_flow:flow?.passed??true,demand:flow?.demand??"0",paid:flow?.flow??"0",
    moves:flow?.moves.length??0,positive_remaining:flow?.remaining.length??data.length,
    proved_mean_differences:flow?.passed?flow.moves:undefined});
 }
 const polynomials=input.complete_coefficients.slice(3).map(r=>r.complete_reduced_elementary_coefficients.map(([p,c])=>({p:p.map(Number),c:BigInt(c)})));
 const exact_screen=search(polynomials);
 return {schema:"isp-six-internal-half-saved-polynomial-attempt-v1",status:"PARTIAL_POSITIVITY_ONLY",
   original_input_sha256:sha256(raw),original_source_sha256:input.source_sha256,full_original_characteristic_return:true,
   ledger:rows,exact_integer_screen:exact_screen,
   scope:"The first three actual coefficients are positive by complete mean differences. The selected dominance flow does not close coefficients four and five. The finite exact screen is not a positivity theorem or a matrix counterexample. No full matrix is replayed.",
   elapsed_ms:Date.now()-start};
}
return {run};

})();
const raw=readFileSync(process.argv[2],"utf8");
const sha=s=>createHash("sha256").update(Buffer.from(s,"latin1")).digest("hex");
const r=await lib.run(raw,sha);const text=JSON.stringify(r,null,2)+"\n";
if(process.argv[3])writeFileSync(process.argv[3],text);process.stdout.write(text);
