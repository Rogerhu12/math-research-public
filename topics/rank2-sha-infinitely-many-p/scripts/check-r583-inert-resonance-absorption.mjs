// Exact certificate for R583; run with Node.js.
// No external dependency and no arithmetic-prime nonvanishing scan.
function run(){

let checks=0;
const check=(ok,label)=>{checks++;if(!ok)throw new Error(label)};
const fact=n=>{let a=1;for(let j=2;j<=n;j++)a*=j;return a};
const binom=(n,k)=>fact(n)/(fact(k)*fact(n-k));
const add=(a,b)=>Array.from({length:Math.max(a.length,b.length)},(_,j)=>(a[j]||0)+(b[j]||0));
const scale=(a,c)=>a.map(x=>x*c);
const mul=(a,b)=>{const c=Array(a.length+b.length-1).fill(0);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=a[i]*b[j];return c};
const intervals=[];
for(const R of [2,5])for(let r=1;r<=R;r++){
 let numerator=[0];
 for(let j=0;j<r;j++){
  let term=[1];
  for(let i=0;i<r;i++)if(i!==j)term=mul(term,[-R+1+i,1]);
  numerator=add(numerator,scale(term,(j%2?-1:1)*binom(r-1,j)));
 }
 check(numerator[0]===fact(r-1)&&numerator.slice(1).every(x=>x===0),
       "full rational partial fractions R="+R+",r="+r);
 intervals.push({R,r,offsets:Array.from({length:r},(_,i)=>R-1-i)});
}
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
const Q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0){n=-n;d=-d}const g=gcd(n,d);return[n/g,d/g]};
const qa=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),qm=(a,b)=>Q(a[0]*b[0],a[1]*b[1]);
const qn=a=>[-a[0],a[1]],qi=a=>Q(a[1],a[0]),qs=a=>a[0]+"/"+a[1];
function determinantInverse(matrix){
 const n=matrix.length,A=matrix.map((row,i)=>[...row.map(x=>[...x]),...Array.from({length:n},(_,j)=>Q(i===j?1:0))]);
 let det=Q(1);
 for(let i=0;i<n;i++){
  let r=i;while(r<n&&!A[r][i][0])r++;check(r<n,"Euler basis invertible "+n);
  if(r!==i){[A[i],A[r]]=[A[r],A[i]];det=qn(det)}
  const pivot=A[i][i];det=qm(det,pivot);const inv=qi(pivot);
  A[i]=A[i].map(x=>qm(x,inv));
  for(let j=0;j<n;j++)if(j!==i){const q=A[j][i];A[j]=A[j].map((x,k)=>qa(x,qn(qm(q,A[i][k]))))}
 }
 return {det:qs(det),inverse:A.map(row=>row.slice(n).map(qs))};
}
const blocks=[];
for(const R of [2,5]){
 const matrix=Array.from({length:R},(_,i)=>Array.from({length:R},()=>Q(0)));
 for(let r=1;r<=R;r++)for(let j=0;j<r;j++)matrix[r-1][R-1-j]=Q((j%2?-1:1)*binom(r-1,j),fact(r-1));
 const di=determinantInverse(matrix);
 check(di.det===(R===2?"1/1":"1/288"),"whole Euler determinant "+R);
 check(di.inverse.flat().every(s=>s.endsWith("/1")),"Euler inverse integral "+R);
 blocks.push({R,matrix:matrix.map(row=>row.map(qs)),...di});
}
const floorCp=(n,p)=>Number(BigInt(n)*BigInt(p)/(BigInt(p)*BigInt(p)-1n));
function divisibilityExponent(n,p){let r=0;while(n%p===0){r++;n/=p}return r}
function costs(n,p,interval){
 const exps=interval.offsets.map(h=>divisibilityExponent(n-h,p));
 return {all:exps.reduce((a,b)=>a+b,0),high:exps.reduce((a,b)=>a+Math.max(0,b-1),0),
  first:exps.filter(a=>a>0).length};
}
let localChecks=0,absorptionChecks=0;
for(let p=8;p<=40;p++){
 for(let n=6;n<=2*p*p+6*p;n+=6){
  for(const h of [0,1,2,3,4])if((n-h)%p===0&&n<2*p*p){
   const m=(n-h)/p;
   check(BigInt(n-6)*BigInt(p)===BigInt(m)*BigInt(p*p-1)+BigInt(m+(h-6)*p),"exact residue numerator");
   check(m+(h-6)*p<0&&m+h*p>=0,"whole absorption sign");
   check(floorCp(n-6,p)+1<=floorCp(n,p),"first resonance absorption");absorptionChecks++;
  }
  for(const interval of intervals){
   const c=costs(n,p,interval);
   check(c.first<=1,"actual short interval one first multiple");
   check(floorCp(n-6,p)+c.all<=floorCp(n,p)+(n>=2*p*p?1:0)+c.high,
         "whole interval bound p="+p+",n="+n+",R="+interval.R+",r="+interval.r);localChecks++;
  }
 }
}
function error(n,K,p){let e=Math.floor(n/(2*p*p));for(let q=p*p;q<=n;q*=p)e+=Math.min(K,Math.floor(n/q));return e}
const mixed=[];const maxK=240,maxQ=6;
for(const p of [8,11,23,40]){
 const local=Array(maxK+1).fill(0);
 for(let k=1;k<=maxK;k++){
  const n=6*k;local[k]=floorCp(n-6,p);
  for(const interval of intervals)local[k]=Math.max(local[k],floorCp(n-6,p)+costs(n,p,interval).all);
 }
 let dp=Array(maxK+1).fill(-Infinity);dp[0]=0;let count=0;
 for(let q=1;q<=maxQ;q++){
  const next=Array(maxK+1).fill(-Infinity);
  for(let k=q;k<=maxK;k++){
   for(let j=1;j<=k-q+1;j++)next[k]=Math.max(next[k],dp[k-j]+local[j]);
   check(next[k]<=floorCp(6*k,p)+error(6*k,q,p),"all compositions and all source labels p="+p+",q="+q+",k="+k);
   count++;
  }
  dp=next;
 }
 mixed.push({integer_base:p,maximum_factor_count:maxQ,maximum_w_degree:maxK,all_composition_checks:count});
}
return {
 status:"all exact checks passed",checks,partial_fraction_checks:intervals.length,
 first_resonance_checks:absorptionChecks,short_interval_checks:localChecks,
 euler_blocks:blocks,mixed_compositions:mixed,
 local_bound:"floor(6kp/(p^2-1)) + floor(6k/(2p^2)) + sum_{a>=2} min(min(D,k),floor(6k/p^a))",
 actual_inert_global_bound:"3 k log k + O(k+D), on the same nine-coordinate saturated source lattice",
 scope:"The finite checks verify arithmetic identities and all bounded compositions; the proof retains all p,D,k.",
 elliptic_prime_scan:false,extra_divisibility_claim:false,negative_moment_nonvanishing_claim:false,
 main_target_complete:false
};
}
console.log(JSON.stringify(run(), null, 2));
