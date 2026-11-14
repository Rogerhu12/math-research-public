"use strict";
// R230: rigorous certificates for the original sixteen negative twists.
// Dependency-free Node.js.  All nonintegral arithmetic uses outward intervals.
// No Math.exp, Math.log, Math.sqrt, database coefficient, or rank oracle is used.
const LIMIT=60000;
const DISCRIMINANTS=[-7,-11,-67,-20,-24,-35,-52,-187,-232,-267,-372,-483,-555,-795,-1435,-532];
const COARSE_INTERVALS=[[4,5],[7,8],[58,59],[3,4],[3,4],[4,5],[10,11],[28,29],[53,54],[67,68],[36,37],[52,53],[54,55],[53,54],[97,98],[42,43]];
function makeCoefficients(M){
 if(!Number.isInteger(M)||M<389||M>60000)throw Error('coefficient range');
 const spf=new Int32Array(M+1);
 for(let i=2;i<=M;i++)if(!spf[i]){spf[i]=i;if(i*i<=M)for(let j=i*i;j<=M;j+=i)if(!spf[j])spf[j]=i;}
 const a=new Int32Array(M+1),b=new Int32Array(M+1);a[1]=b[1]=1;
 for(let n=2;n<=M;n++){
  const p=spf[n],m=n/p;
  if(m===1){
   const counts=new Uint8Array(p);for(let y=0;y<p;y++)counts[(y*y+y)%p]++;
   let s=0;for(let x=0;x<p;x++)s+=counts[(x*x*x+x*x-2*x)%p];
   a[n]=p-s;
   if(p===2)b[n]=-2;else{
    const chi=new Int8Array(p);chi.fill(-1);for(let y=0;y<p;y++)chi[y*y%p]=1;chi[0]=0;
    s=0;for(let x=0;x<p;x++)s+=chi[(4*x*x*x+4*x*x-8*x+1)%p];b[n]=-s;
   }
   if(a[n]!==b[n])throw Error("independent trace mismatch "+p);
   if(p!==389 && a[n]*a[n]>4*p)throw Error("Hasse "+p);
  }else{
   a[n]=a[p]*a[m];b[n]=b[p]*b[m];
   if(m%p===0 && p!==389){a[n]-=p*a[m/p];b[n]-=p*b[m/p];}
  }
  if(a[n]!==b[n])throw Error("coefficient mismatch "+n);
 }
 if(a[389]!==1 || a[137]!==-2)throw Error("fixed trace mismatch");
 return Array.from(a);
}
const buf=new ArrayBuffer(8),f64=new Float64Array(buf),u32=new Uint32Array(buf);
f64[0]=1;if(u32[1]!==0x3ff00000)throw Error("little-endian IEEE754 required");
function up(x){if(x===Infinity)return x;if(x===-Infinity)return -Number.MAX_VALUE;if(Number.isNaN(x))throw Error("NaN");if(x===0)return Number.MIN_VALUE;f64[0]=x;if(x>0){u32[0]=(u32[0]+1)>>>0;if(u32[0]===0)u32[1]++;}else{if(u32[0]===0)u32[1]--;u32[0]=(u32[0]-1)>>>0;}return f64[0];}
function down(x){return -up(-x);}
const exact=x=>[x,x],neg=a=>[-a[1],-a[0]];
const add=(a,b)=>[down(a[0]+b[0]),up(a[1]+b[1])];
const sub=(a,b)=>add(a,neg(b));
function mul(a,b){const v=[a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]];return [down(Math.min(...v)),up(Math.max(...v))];}
function div(a,b){if(b[0]<=0&&b[1]>=0)throw Error("zero denominator");return mul(a,[down(1/b[1]),up(1/b[0])]);}
const scale=(a,n)=>mul(a,exact(n));
function power(a,n){let z=exact(1);for(;n;n=Math.floor(n/2),a=mul(a,a))if(n%2)z=mul(z,a);return z;}
function widen(a,e){return [down(a[0]-e),up(a[1]+e)];}
function atanSmall(q){const x=div(exact(1),exact(q)),xx=mul(x,x);let t=x,s=x;for(let k=1;k<32;k++){t=mul(t,neg(xx));s=add(s,div(t,exact(2*k+1)));}const next=div(mul(t,xx),exact(65));return widen(s,Math.max(Math.abs(next[0]),Math.abs(next[1])));}
const pi=sub(scale(atanSmall(5),16),scale(atanSmall(239),4));
function logAtanh(t){let s=t,term=t;const t2=mul(t,t);for(let k=1;k<40;k++){term=mul(term,t2);s=add(s,div(term,exact(2*k+1)));}const rem=div(scale(mul(term,t2),2),mul(exact(81),sub(exact(1),t2)));return widen(scale(s,2),Math.max(Math.abs(rem[0]),Math.abs(rem[1])));}
const log2=logAtanh(div(exact(1),exact(3)));
function log(x){if(x[0]<=0)throw Error("positive log");let k=0,y=x;while(y[0]<1){y=scale(y,2);k--;}while(y[1]>2){y=scale(y,0.5);k++;}const t=div(sub(y,exact(1)),add(y,exact(1)));return add(logAtanh(t),scale(log2,k));}
let gamma=exact(0);for(let j=1;j<=64;j++)gamma=add(gamma,div(exact(1),exact(j)));
gamma=sub(sub(gamma,scale(log2,6)),exact(1/128));
const bern=[[1,6],[-1,30],[1,42],[-1,30],[5,66]];
for(let k=1;k<=5;k++)gamma=add(gamma,div(exact(bern[k-1][0]),scale(power(exact(64),2*k),2*k*bern[k-1][1])));
const gammaR=div(exact(691),scale(power(exact(64),12),2730*12))[1];gamma=widen(gamma,gammaR);
function isqrt(n){let x=1n<<BigInt(Math.ceil(n.toString(2).length/2));for(;;){const y=(x+n/x)/2n;if(y>=x)return x;x=y;}}
const DEN=10n**14n,rt=isqrt(389n*DEN*DEN);
// rt and rt+1 are below 2^53, so their Number conversions are exact.
const root389=[down(Number(rt)/100000000000000),up(Number(rt+1n)/100000000000000)];
function expSmallMinus(x){if(x[0]<=0||x[1]>=0.1)throw Error("small exp range");let sum=exact(1),term=exact(1);for(let k=1;k<=18;k++){term=div(mul(term,neg(x)),exact(k));sum=add(sum,term);}const err=div(mul(term,x),exact(19));return widen(sum,Math.max(Math.abs(err[0]),Math.abs(err[1])));}
function cf(x,N){let r=exact(0);for(let j=N;j;j--)r=div(exact(Math.ceil(j/2)),add(j%2?exact(1):x,r));return div(exact(1),add(x,r));}
function E1(x,ex){if(x[1]<1){let term=neg(x),s=term;for(let k=2;k<=22;k++){term=div(mul(term,neg(x)),exact(k));s=add(s,div(term,exact(k)));}const rem=div(mul(term,x),exact(23*23));return widen(sub(neg(gamma),add(log(x),s)),Math.max(Math.abs(rem[0]),Math.abs(rem[1])));}const lo=cf(x,65),hi=cf(x,64);return mul(ex,[lo[0],hi[1]]);}
function kronecker(a,n){let s=1;while(n%2===0){if(a%2===0)return 0;const z=((a%8)+8)%8;if(z===3||z===5)s=-s;n/=2;}a=((a%n)+n)%n;while(a){while(a%2===0){a/=2;if(n%8===3||n%8===5)s=-s;}if(a%4===3&&n%4===3)s=-s;[a,n]=[n%a,a];}return n===1?s:0;}
function certify(D,coeff){const c=div(scale(pi,2),scale(root389,-D)),q=expSmallMinus(c),M=Math.min(coeff.length-1,Math.ceil(20/c[0]));const chi=Array.from({length:-D},(_,n)=>n?kronecker(D,n):0);
let ex=exact(1),sum=exact(0),used=0;
for(let n=1;n<=M;n++){ex=mul(ex,q);const an=coeff[n]*chi[n%(-D)];if(!an)continue;const val=E1(scale(c,n),ex);sum=add(sum,mul(div(exact(2*an),exact(n)),val));used++;}
const tail=div(scale(mul(ex,q),4),mul(scale(c,M+1),sub(exact(1),q)))[1],full=widen(sum,tail);
return {D,conductor:389*D*D,M,used,c,q,partial:sum,tail,enclosure:full,rankOneCertified:full[0]>0||full[1]<0};}


function factorParity(n){const v=[];for(let q=2;q*q<=n;q++){let e=0;while(n%q===0){n/=q;e^=1;}if(e)v.push(q);}if(n>1)v.push(n);return v;}
function squarefree(n){for(let q=2;q*q<=n;q++)if(n%(q*q)===0)return false;return true;}
function checkFixedData(Ds,coeff){
 const basis=new Map();
 for(const D of Ds){
 const d=D%4===0?D/4:D,mod4=((d%4)+4)%4;
 if(!squarefree(-d)||(D%4===0?!(mod4===2||mod4===3):mod4!==1))throw Error("not fundamental "+D);
 if(kronecker(D,389)!==1)throw Error("389 does not split "+D);
 let v=new Set([-1,...factorParity(-D)]);
 while(v.size){const lead=Math.max(...v);if(!basis.has(lead)){basis.set(lead,new Set(v));break;}for(const x of basis.get(lead))v.has(x)?v.delete(x):v.add(x);}
 if(!v.size)throw Error("dependent discriminant "+D);
 }
 if(basis.size!==16)throw Error("quadratic rank");
 if(coeff[1]!==1||coeff[2]!==-2||coeff[3]!==-2||coeff[389]!==1)throw Error("fixed coefficients");
 return {fundamental_discriminants:16,split_at_389:16,quadratic_character_rank:basis.size};
}

function report(coeff){
 const checks=checkFixedData(DISCRIMINANTS,coeff);
 const rows=DISCRIMINANTS.map((D,j)=>{
  const v=certify(D,coeff),g=COARSE_INTERVALS[j];
  if(!(v.enclosure[0]>g[0]&&v.enclosure[1]<g[1]))throw Error("certificate failed "+D);
  return {D:v.D,conductor:v.conductor,M:v.M,nonzero_terms:v.used,
          partial_interval:v.partial,tail_upper:v.tail,
          certified_interval:v.enclosure,coarse_open_interval:g};
 });
 return {curve:"y^2+y=x^3+x^2-2*x",coefficient_limit:LIMIT,
         coefficient_generators:"point histograms and quadratic-discriminant sums; every coefficient agrees",
         arithmetic:"IEEE754 outward intervals; exact integers below 2^53; BigInt square root",
         checks,constants:{pi,sqrt389:root389,euler_gamma:gamma,log2},rows,
         all_sixteen_strictly_positive:true};
}
function main(){return report(makeCoefficients(LIMIT));}
if(typeof module!=="undefined"&&require.main===module)
 console.log(JSON.stringify(main(),null,2));
