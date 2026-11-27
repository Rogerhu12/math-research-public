// Numeric source selection for a new actual six-site matrix budget.
// The full original physical inverses and same two source terms are retained.
// This is not an exact positivity certificate.
const api=(()=>{

const zero=(n,m=n)=>Array.from({length:n},()=>Array(m).fill(0));
const ident=n=>zero(n).map((r,i)=>(r[i]=1,r));
const tr=a=>a[0].map((_,j)=>a.map(r=>r[j]));
function mm(a,b){const r=zero(a.length,b[0].length);for(let i=0;i<a.length;i++)for(let k=0;k<b.length;k++)if(a[i][k])for(let j=0;j<b[0].length;j++)r[i][j]+=a[i][k]*b[k][j];return r;}
const add=(a,b)=>a.map((r,i)=>r.map((x,j)=>x+b[i][j]));
const scale=(a,s)=>a.map(r=>r.map(x=>x*s));
const sub=(a,b)=>add(a,scale(b,-1));
const sym=a=>a.map((r,i)=>r.map((x,j)=>(x+a[j][i])/2));
const trace=a=>a.reduce((s,r,i)=>s+r[i],0);
function inv(a){const n=a.length,L=zero(n);for(let i=0;i<n;i++)for(let j=0;j<=i;j++){let s=a[i][j];for(let k=0;k<j;k++)s-=L[i][k]*L[j][k];if(i===j){if(!(s>0))throw Error("Cholesky pivot "+s);L[i][j]=Math.sqrt(s);}else L[i][j]=s/L[j][j];}
 const result=zero(n);for(let j=0;j<n;j++){const y=Array(n).fill(0),x=Array(n).fill(0);for(let i=0;i<n;i++){let s=i===j?1:0;for(let k=0;k<i;k++)s-=L[i][k]*y[k];y[i]=s/L[i][i];}
  for(let i=n-1;i>=0;i--){let s=y[i];for(let k=i+1;k<n;k++)s-=L[k][i]*x[k];x[i]=s/L[i][i];}for(let i=0;i<n;i++)result[i][j]=x[i];}return sym(result);
}
const levels=Array.from({length:7},()=>[]);for(let x=0;x<64;x++){let p=0;for(let y=x;y;y>>=1)p+=y&1;levels[p].push(x);}
function down(b,k,power=1){const r=zero(levels[k-1].length,levels[k].length),index=new Map(levels[k-1].map((x,i)=>[x,i]));for(let j=0;j<levels[k].length;j++){const x=levels[k][j];for(let i=0;i<6;i++)if(x&(1<<i))r[index.get(x^(1<<i))][j]=b[i]**power;}return r;}
function actualCost(b){
 const R=down(b,2),D3=down(b,3),D4=down(b,4),C=down(b,2,3),F1=mm(R,tr(R)),F1i=inv(F1),P=sub(ident(15),mm(mm(tr(R),F1i),R));
 const S=b.reduce((s,x)=>s+x*x,0),Q=b.map(x=>b.map(y=>x*y/S)),Pi=sub(ident(6),Q);
 const J2=scale(mm(R,D3),.5),F2=mm(J2,tr(J2)),J3=scale(mm(J2,D4),1/3),F3=mm(J3,tr(J3));
 const L1=mm(mm(Pi,F1i),Pi),L2=mm(mm(Pi,inv(F2)),Pi);
 const F2b=mm(F2,b.map(x=>[x])),F2den=b.reduce((s,x,i)=>s+x*F2b[i][0],0),C3low=sub(F2,scale(mm(F2b,tr(F2b)),1/F2den));
 const Fb=mm(F3,b.map(x=>[x])),den=b.reduce((s,x,i)=>s+x*Fb[i][0],0),E=sub(F3,scale(mm(Fb,tr(Fb)),1/den));
 const FU=mm(D3,tr(D3)),Gu=mm(mm(P,inv(FU)),P),FR=mm(FU,tr(R)),Cu=sub(FU,mm(mm(FR,inv(mm(R,FR))),tr(FR)));
 const B=mm(mm(Pi,C),P),Bt=tr(B),X=mm(mm(L2,E),L2);
 const A=scale(add(mm(mm(Cu,Bt),L2),mm(Bt,X)),.5),K=sym(mm(mm(tr(A),Gu),A));
 const K2=mm(K,K),K3=mm(K2,K),m1=trace(K),m2=trace(K2),m3=trace(K3);
 return {trace:m1,trace_square:m2,trace_cube:m3,cubic:32*m3-16*m2+2*m1,
 full_S2_trace:trace(add(K,mm(mm(L1,C3low),L1)))};
}
function screen(){
 const start=Date.now(),cases=[[1,1,1,1,1,1],[6,1,1,1,1,1],[100,1,1,1,1,1],[10,10,1,1,1,1],[10,10,10,1,1,1]],fixed=cases.length;let seed=28540317;
 function random(){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed/4294967296;}
 for(let k=0;k<400;k++)cases.push(Array.from({length:6},()=>Math.exp((2*random()-1)*(k<200?1.5:3))));
 const reports=[],top=[];let failed=0;
 for(let i=0;i<cases.length;i++)try{const r={b:cases[i],...actualCost(cases[i])};if(i<fixed)reports.push(r);top.push(r);top.sort((a,b)=>b.cubic-a.cubic);if(top.length>10)top.pop();}catch(e){failed++;}
 return {schema:"isp-six-site-new-shifted-cubic-budget-numeric-screen-v1",seed:28540317,attempted:cases.length,failed,elapsed_ms:Date.now()-start,fixed:reports,largest:top,
 scope:"Floating-point source selection only. Full physical inverses and both source cross terms retained. This does not prove a uniform cubic or S2 inequality."};
}
return {actualCost,screen};

})();
console.log(JSON.stringify(api.screen(),null,2));
