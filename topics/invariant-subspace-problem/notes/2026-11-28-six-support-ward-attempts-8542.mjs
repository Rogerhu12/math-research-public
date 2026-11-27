#!/usr/bin/env node
// Attempt replay only. Neither six-site positivity nor S2 is certified here.
import {readFileSync,writeFileSync} from "node:fs";
const flow=(function(){

function factorial(n){let v=1n;for(let j=2;j<=n;j++)v*=BigInt(j);return v;}
function multiplicity(p){let d=1n;for(let i=0;i<p.length;){let j=i+1;while(j<p.length&&p[j]===p[i])j++;d*=factorial(j-i);i=j;}return factorial(p.length)/d;}
function pars(n,m,max=n){if(!m)return n?[]:[[]];let out=[];for(let a=Math.min(n,max);a>=0;a--)for(const p of pars(n-a,m-1,a))out.push([a,...p]);return out;}
function key(gs){return gs.map(p=>p.join(",")).join("|");}
function covers(gs){let out=new Map;for(let g=0;g<gs.length;g++)for(let i=0;i<gs[g].length;i++)for(let j=i+1;j<gs[g].length;j++){if(gs[g][i]<gs[g][j]+2)continue;let v=gs.map(p=>p.slice());v[g][i]--;v[g][j]++;v[g].sort((a,b)=>b-a);out.set(key(v),v);}return [...out.values()];}
function permutations(arr){const out=[];function rec(rest,pre){if(!rest.length){out.push(pre);return;}for(let i=0;i<rest.length;i++){if(i&&rest[i]===rest[i-1])continue;rec(rest.slice(0,i).concat(rest.slice(i+1)),pre.concat(rest[i]));}}rec(arr,[]);return out;}
function certify(poly,m,groups){
 const orbit=new Map;
 for(const[k,c]of poly){
  let ex=Array.from({length:m},(_,i)=>Math.floor(k/(32**i))%32),pos=0,gs=groups.map(n=>{const p=ex.slice(pos,pos+n).sort((a,b)=>b-a);pos+=n;return p;});
  let ky=key(gs),old=orbit.get(ky);
  if(old&&old.c!==c)throw Error("stabilizer symmetry mismatch");
  orbit.set(ky,{gs,c});
 }
 // Check every permutation, including potential zero coefficients.
 for(const {gs,c}of orbit.values()){
  let es=[[]];for(const g of gs){const ps=permutations(g);es=es.flatMap(a=>ps.map(b=>a.concat(b)));}
  for(const e of es){let k=e.reduce((s,x,i)=>s+x*32**i,0);if((poly.get(k)||0n)!==c)throw Error("incomplete symmetry orbit");}
 }
 const bins=new Map;
 for(const o of orbit.values()){
  const ds=o.gs.map(p=>p.reduce((s,x)=>s+x,0)).join(",");
  if(!bins.has(ds))bins.set(ds,[]);
  bins.get(ds).push(o);
 }
 let failures=[],certs=[];
 for(const [ds,os]of bins){
  let demand=0n,total=0n;for(const o of os){o.w=o.c*o.gs.reduce((s,p)=>s*multiplicity(p),1n);total+=o.w;if(o.w<0n)demand-=o.w;}
  if(!demand){certs.push({degrees:ds,demand:"0",leftover:String(total)});continue;}
  if(total<0n){failures.push({degrees:ds,reason:"negative grouped equal-variable value",total:String(total),demand:String(demand)});continue;}
  const degrees=ds.split(",").map(Number);
  let states=[[]];for(let i=0;i<groups.length;i++)states=states.flatMap(a=>pars(degrees[i],groups[i]).map(p=>a.concat([p])));
  const idx=new Map(states.map((s,i)=>[key(s),i])),N=states.length,src=N,snk=N+1,graph=Array.from({length:N+2},()=>[]);
  function edge(a,b,c,kind){const e={to:b,rev:graph[b].length,cap:c,orig:c,kind};const r={to:a,rev:graph[a].length,cap:0n,orig:0n};graph[a].push(e);graph[b].push(r);}
  for(let i=0;i<N;i++)for(const next of covers(states[i]))edge(i,idx.get(key(next)),demand,"move");
  for(const o of os){let i=idx.get(key(o.gs));if(o.w>0n)edge(src,i,o.w,"supply");else if(o.w<0n)edge(i,snk,-o.w,"demand");}
  let flow=0n;
  while(true){
   const level=Array(N+2).fill(-1);level[src]=0;let queue=[src];for(let h=0;h<queue.length;h++){let u=queue[h];for(const e of graph[u])if(e.cap>0n&&level[e.to]<0){level[e.to]=level[u]+1;queue.push(e.to);}}
   if(level[snk]<0)break;
   const it=Array(N+2).fill(0);
   function dfs(u,pushed){if(u===snk)return pushed;for(;it[u]<graph[u].length;it[u]++){const e=graph[u][it[u]];if(e.cap<=0n||level[e.to]!==level[u]+1)continue;let x=dfs(e.to,pushed<e.cap?pushed:e.cap);if(x){e.cap-=x;graph[e.to][e.rev].cap+=x;return x;}}return 0n;}
   while(flow<demand){const f=dfs(src,demand-flow);if(!f)break;flow+=f;}
   if(flow===demand)break;
  }
  if(flow!==demand){failures.push({degrees:ds,reason:"incomplete dominance flow",demand:String(demand),flow:String(flow)});continue;}
  // Reconstruct and verify exact coefficient conservation for the certificate.
  const balance=new Map(states.map((s)=>[key(s),0n])),moves=[],left=[];
  for(let i=0;i<N;i++)for(const e of graph[i])if(e.kind==="move"&&e.orig>e.cap){const q=e.orig-e.cap;balance.set(key(states[i]),balance.get(key(states[i]))+q);balance.set(key(states[e.to]),balance.get(key(states[e.to]))-q);moves.push({from:states[i],to:states[e.to],weight:String(q)});}
  for(const e of graph[src])if(e.kind==="supply"&&e.cap){balance.set(key(states[e.to]),balance.get(key(states[e.to]))+e.cap);left.push({state:states[e.to],weight:String(e.cap)});}
  const target=new Map(os.map(o=>[key(o.gs),o.w]));for(const [k,w]of balance)if(w!==(target.get(k)||0n))throw Error("flow coefficient conservation failed");
  certs.push({degrees:ds,demand:String(demand),leftover:String(total),nodes:N,moves,left});
 }
 return {groups,orbits:orbit.size,passed:failures.length===0,failures,certs};
}
return {certify};

})();
const numerical=(function(){

function pc(x){let n=0;while(x){x&=x-1;n++;}return n;}
function masks(n,p){let a=[];for(let m=0;m<1<<n;m++)if(pc(m)===p)a.push(m);return a;}
function dot(a,b){return a.reduce((s,x,i)=>s+x*b[i],0);}
function tr(A){return A[0].map((_,j)=>A.map(r=>r[j]));}
function mm(A,B){let C=tr(B);return A.map(a=>C.map(c=>dot(a,c)));}
function add(A,B,k=1){return A.map((r,i)=>r.map((x,j)=>x+k*B[i][j]));}
function scale(A,k){return A.map(r=>r.map(x=>k*x));}
function eye(n){return Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>i===j?1:0));}
function orth(rows,old=[]){let q=old.map(r=>r.slice()),out=[];for(let row of rows){let v=row.slice();for(let z=0;z<2;z++)for(let u of q){let x=dot(u,v);for(let i=0;i<v.length;i++)v[i]-=x*u[i];}let n=Math.sqrt(dot(v,v));if(n>1e-10){v=v.map(x=>x/n);q.push(v);out.push(v);}}return out;}
function inv(A){let n=A.length,R=A.map((r,i)=>r.concat(eye(n)[i]));for(let j=0;j<n;j++){let k=j;for(let i=j+1;i<n;i++)if(Math.abs(R[i][j])>Math.abs(R[k][j]))k=i;let t=R[k];R[k]=R[j];R[j]=t;let a=R[j][j];if(Math.abs(a)<1e-25)throw Error("singular");R[j]=R[j].map(x=>x/a);for(let i=0;i<n;i++)if(i!==j){let a=R[i][j];for(let h=0;h<2*n;h++)R[i][h]-=a*R[j][h];}}return R.map(r=>r.slice(n));}
function sym(A){return A.map((r,i)=>r.map((x,j)=>(x+A[j][i])/2));}
function eig(A){A=sym(A);let n=A.length;for(let step=0;step<100*n*n;step++){let p=0,q=1,v=0;for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)if(Math.abs(A[i][j])>v){v=Math.abs(A[i][j]);p=i;q=j;}if(v<1e-13)break;let th=.5*Math.atan2(2*A[p][q],A[q][q]-A[p][p]),c=Math.cos(th),s=Math.sin(th),a=A[p][p],b=A[q][q],h=A[p][q];A[p][p]=c*c*a-2*s*c*h+s*s*b;A[q][q]=s*s*a+2*s*c*h+c*c*b;A[p][q]=A[q][p]=0;for(let i=0;i<n;i++)if(i!==p&&i!==q){let a=A[i][p],b=A[i][q];A[i][p]=A[p][i]=c*a-s*b;A[i][q]=A[q][i]=s*a+c*b;}}return A.map((r,i)=>r[i]).sort((a,b)=>a-b);}
function chol(A){let n=A.length,L=Array.from({length:n},()=>Array(n).fill(0));for(let i=0;i<n;i++)for(let j=0;j<=i;j++){let s=A[i][j];for(let k=0;k<j;k++)s-=L[i][k]*L[j][k];L[i][j]=i===j?Math.sqrt(s):s/L[j][j];if(!Number.isFinite(L[i][j]))throw Error("cholesky");}return L;}
function context(N){let s=N/2,mid=masks(N,s),low=masks(N,s-1),lo2=masks(N,s-2);let d=low.map(r=>mid.map(c=>(r&c)===r?1:0)),dm=lo2.map(r=>low.map(c=>(r&c)===r?1:0));let U=orth(eye(mid.length),orth(d)),V=orth(eye(low.length),orth(dm));let E=scale(mm(V,d),1/Math.sqrt(2));return {N,s,mid,low,U,V,E};}
function weighted(A,B,w){return A.map(a=>B.map(b=>a.reduce((s,x,i)=>s+x*b[i]*w[i],0)));}
function phase(z,ctx){let {N,mid,low,U,V,E}=ctx??context(z.length),prod=m=>z.reduce((s,v,i)=>s*((m>>i)&1?v:1),1),pi=z.reduce((s,v)=>s*v,1);let wm=mid.map(m=>1/prod(m)),wl=low.map(m=>1/prod(m)),wu=low.map(m=>prod(m)/pi);let h=weighted(V,V,wl),ell=weighted(V,V,wu),M=weighted(U,U,wm),C=weighted(U,E,wm),Q=weighted(E,E,wm),R=mm(mm(tr(C),inv(M)),C),S=add(Q,R,-1),J=add(scale(mm(mm(h,inv(S)),ell),2),add(Q,R),-1);let D=mm(mm(tr(J),inv(ell)),J),L=chol(h),Li=inv(L),F=mm(mm(Li,D),tr(Li));return {N,z,dim:V.length,phi:eig(F),hmin:eig(h)[0],smin:eig(S)[0]};}

function derivative(b,p,k=1){let cols=masks(b.length,p),rows=masks(b.length,p-k);return rows.map(r=>cols.map(c=>{if((r&c)!==r)return 0;let z=1;for(let i=0;i<b.length;i++)if(((c^r)>>i)&1)z*=b[i];return z;}));}
function primitive(b,p){let d=derivative(b,p),m=masks(b.length,p).length;return orth(eye(m),orth(d));}
function gram(b,p,j,U){let D=derivative(b,p+j,j),F=mm(D,tr(D));return mm(mm(U,inv(F)),tr(U));}
function s2(b,s){let U=primitive(b,s),V=primitive(b,s-1),G=gram(b,s,1,U),C=inv(G),L1=gram(b,s-1,1,V),L2=gram(b,s-1,2,V),L3=gram(b,s-1,3,V),D3=derivative(b.map(x=>x*x*x),s),B=mm(mm(V,D3),tr(U)),Q=mm(tr(B),L2),A=scale(add(mm(C,Q),mm(mm(Q,inv(L3)),L2)),.5),budget=add(eye(V.length),mm(mm(L1,inv(L2)),L1),-1),cost=mm(mm(tr(A),G),A),Li=inv(chol(budget)),F=mm(mm(Li,cost),tr(Li)),vals=eig(F);return {b,s,dim:V.length,budget:eig(budget),vals,trace:vals.reduce((a,c)=>a+c,0),costSquared:cost.reduce((s,r,i)=>s+r.reduce((t,x,j)=>t+x*cost[j][i],0),0)};}

function wardCheck(b){
 const U=primitive(b,2),V=primitive(b,1),Gu=gram(b,2,1,U),Cu=inv(Gu),L1=gram(b,1,1,V),L2=gram(b,1,2,V),L3=gram(b,1,3,V);
 const C=derivative(b.map(x=>x**3),2),B=mm(mm(V,C),tr(U)),Q=mm(tr(B),L2),A=scale(add(mm(Cu,Q),mm(mm(Q,inv(L3)),L2)),.5),old=mm(mm(tr(A),Gu),A);
 const e=tr(derivative(b.map(x=>1/x),2)),F=add(mm(tr(C),tr(V)),mm(mm(mm(e,tr(V)),L1),inv(L3)));
 const R2=derivative(b,3,2),P=add(eye(R2[0].length),mm(mm(tr(R2),inv(mm(R2,tr(R2)))),R2),-1);
 const X=mm(mm(tr(derivative(b,3)),F),L2),nw=mm(mm(tr(X),P),X);
 return {b,maxDifference:Math.max(...old.flatMap((r,i)=>r.map((x,j)=>Math.abs(x-nw[i][j])))),costSquared:old.reduce((s,r,i)=>s+r.reduce((t,x,j)=>t+x*old[j][i],0),0)};
}
return {wardCheck,s2};


})();

const output={status:"attempt_record_only"};
if(!process.argv.includes("--ward-only")){
 const f=new URL("./2026-11-28-birth-one-half-four-five-certificate-8542.mjs",import.meta.url);
 const prefix=readFileSync(f,"utf8").split("async function verifyBirthOneHalfUpToFive")[0];
 const g=Function(prefix+"\nreturn {supportMatrix,directSupport,equivalent,leadingPolynomials,elementaryMatrixCoefficient};")();
 const t=Date.now(),M=g.supportMatrix(6),D=g.directSupport(6);
 for(let i=0;i<6;i++)for(let j=0;j<6;j++)g.equivalent(M[i][j],D[i][j]);
 const ps=g.leadingPolynomials(M);output.six_support=[];
 for(let k=1;k<=5;k++){
  const p=g.elementaryMatrixCoefficient(ps[k-1],6,k),c=flow.certify(p,6,[6]);
  output.six_support.push({order:k,terms:p.size,negative:[...p.values()].filter(x=>x<0n).length,
     passed:c.passed,failures:c.failures,moves:c.certs.reduce((s,q)=>s+(q.moves?.length??0),0)});
 }
 output.six_runtime_ms=Date.now()-t;
}
if(!process.argv.includes("--six-only")){
 const f=new URL("./2026-11-28-primitive-joint-source-numeric-screen-8542-primitive.json",import.meta.url);
 const inputs=JSON.parse(readFileSync(f,"utf8")).five_s2_random.map(r=>r.b);
 inputs.push([1,.01,.01,.01,.01],[1,1,.01,.01,.01],[1,1,1,.01,.01],[1,.5,.25,.125,.0625]);
 output.ward_cost_square=inputs.map((b,index)=>({index,b,costSquared:numerical.s2(b,2).costSquared}));
 output.one_ward_identity_sanity=numerical.wardCheck([1,2,3,4,5]);
}
writeFileSync(process.argv.find(x=>x.endsWith(".json"))??"six-support-ward-attempts.json",JSON.stringify(output,null,2)+"\n");
