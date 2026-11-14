// R579: full divided-difference and falling-factorial certificates.
// Run: node check-r579-nine-coordinate-divided-difference-budget.mjs
// All D,k,p statements and genuine source normalization are proved in the text.
const data=(()=>{
let checks=0;const check=(ok,label)=>{checks++;if(!ok)throw Error(label)};
const binom=(n,k)=>{if(k<0||k>n)return 0n;let r=1n;for(let j=1;j<=k;j++)r=r*BigInt(n-j+1)/BigInt(j);return r};
function h(nodes,d){if(d<0)return 0n;const a=Array(d+1).fill(0n);a[0]=1n;
 for(const v0 of nodes){const v=BigInt(v0);for(let k=1;k<=d;k++)a[k]+=v*a[k-1];}return a[d]}
function paths(r,s){
 const out=[];function rec(i,j,nodes){if(i===r&&j===s){out.push(nodes);return}
 if(i<r)rec(i+1,j,[...nodes,[i+1,j]]);if(j<s)rec(i,j+1,[...nodes,[i,j+1]]);}
 rec(0,0,[[0,0]]);return out;
}
const xnodes=[0,1,3,7],ynodes=[2,4,8,13];
for(let r=0;r<=3;r++)for(let s=0;s<=3;s++)for(let m=0;m<=12;m++){
 const X=xnodes.slice(0,r+1),Y=ynodes.slice(0,s+1);let left=0n;
 for(let a=0;a<=m;a++)left+=binom(m,a)*h(X,a-r)*h(Y,m-a-s);
 const right=paths(r,s).reduce((v,P)=>v+h(P.map(([i,j])=>X[i]+Y[j]),m-r-s),0n);
 check(left===right,"complete mixed divided-difference shuffle "+r+","+s+","+m);
}
for(let j=0;j<=5;j++)for(let m=0;m<=12;m++){
 const nodes=[0,1,1,3,5,8].slice(0,j+1);
 const left=BigInt(m)*h(nodes,m-1-j);
 const right=nodes.reduce((v,x,i)=>v+h([...nodes.slice(0,i),x,...nodes.slice(i)],m-j-1),0n);
 check(left===right,"confluent derivative shuffle "+j+","+m);
}
const add=(a,b)=>Array.from({length:Math.max(a.length,b.length)},(_,j)=>(a[j]||0n)+(b[j]||0n));
function mul(a,b){const c=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=a[i]*b[j];return c}
function choose(n,j){
 const out=[];function rec(next,left,A){if(!left){out.push(A);return}for(let t=next;t<=n-left;t++)rec(t+1,left-1,[...A,t]);}
 rec(0,j,[]);return out;
}
for(let n=1;n<=10;n++){
 let F=[1n];for(let v=0;v<n;v++)F=mul(F,[-BigInt(v),1n]);
 for(let j=0;j<=Math.min(4,n);j++){
  const nodes=[1,3,6,10,15].slice(0,j+1);
  const left=F.reduce((v,c,m)=>v+c*h(nodes,m-j),0n);
  let right=0n;for(const marked of choose(n,j)){
   const A=new Set(marked);let k=0,term=1n;for(let v=0;v<n;v++){if(A.has(v)){k++;continue}term*=BigInt(nodes[k]-v);}right+=term;
  }
  check(left===right,"all consecutive root segments "+n+","+j);
 }
}
const vpFact=(n,p)=>{let v=0;for(let q=p;q<=n;q*=p)v+=Math.floor(n/q);return v};
const loss=(n,j,p)=>{let v=0;for(let q=p;q<=n;q*=p)v+=Math.min(j,Math.floor(n/q));return v};
function comps(total,count){
 const out=[];function rec(t,c,A){if(c===1){out.push([...A,t]);return}for(let v=0;v<=t;v++)rec(t-v,c-1,[...A,v]);}rec(total,count,[]);return out;
}
let valuationCases=0;
for(let n=1;n<=12;n++)for(let j=0;j<=Math.min(4,n);j++){
 for(const ls of comps(n-j,j+1))for(const p of[2,3,5,7,13]){
  const left=ls.reduce((v,l)=>v+vpFact(l,p),0),right=vpFact(n,p)-loss(n,j,p);
  check(left>=right,"uniform factorial valuation "+n+","+j+","+p);valuationCases++;
 }
}
const examples=[];
for(const[n,R]of[[6,5],[18,5],[30,10],[60,20]]){
 const row={n,R,local_losses:{}};
 for(const p of[2,3,5,7,13,19,31,61])row.local_losses[p]=loss(n,R,p);
 examples.push(row);
}
return {result:"all exact checks passed",checks,valuation_cases:valuationCases,
 shuffle:"sum over monotone lattice paths of the full order r+s divided difference",
 factorial_loss:"Lambda_p(n,R)=sum_a min(R,floor(n/p^a))",
 actual_nine_coordinate_bound:"v_p(r_k(P))>=-Lambda_p(6k,5 min(D,k)) on every true saturated prefix",
 examples,uses_measure_derivative_representation:false,requires_I4_I1_zero:false,
 scope:"Finite certificates of exact algebraic identities; general norms and all D,k,p are proved in the text."};
})();
console.log(JSON.stringify(data,null,2));
