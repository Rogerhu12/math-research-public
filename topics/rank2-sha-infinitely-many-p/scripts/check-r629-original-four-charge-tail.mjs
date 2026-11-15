// Exact fixed-class certificate for R629. No external packages.
// All arithmetic is BigInt rational arithmetic; this does not scan primes.
const R = (()=>{
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a;}
function q(a,b=1n){a=BigInt(a);b=BigInt(b);if(b===0n)throw Error("zero denominator");if(!a)return[0n,1n];if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return[a/g,b/g];}
const add=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>[-a[0],a[1]];
const sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>q(a[0]*b[0],a[1]*b[1]);
const div=(a,b)=>q(a[0]*b[1],a[1]*b[0]);
const sc=(a,n)=>q(a[0]*BigInt(n),a[1]);
function zeros(N){return Array.from({length:N},()=>q(0));}
function conv(a,b,N){let c=zeros(N);for(let i=0;i<a.length&&i<N;i++)for(let j=0;j<b.length&&i+j<N;j++)c[i+j]=add(c[i+j],mul(a[i],b[j]));return c;}
function inv(a,N){let c=zeros(N);c[0]=div(q(1),a[0]);for(let n=1;n<N;n++){let v=q(0);for(let j=1;j<=n&&j<a.length;j++)v=add(v,mul(a[j],c[n-j]));c[n]=neg(div(v,a[0]));}return c;}
function pow(a,n,N){if(n<0)return pow(inv(a,N),-n,N);let c=zeros(N);c[0]=q(1);while(n){if(n&1)c=conv(c,a,N);a=conv(a,a,N);n>>=1;}return c;}
function theta(N){let logs=zeros(N),rr=q(1);for(let n=1;n<N;n++){rr=mul(rr,q(6*n-4,6*n-1));logs[n]=mul(q(17,3*n),rr);}let L=zeros(N);L[0]=q(1);for(let n=1;n<N;n++){let z=q(0);for(let k=1;k<=n;k++)z=add(z,mul(sc(logs[k],k),L[n-k]));L[n]=div(z,q(n));}return L;}
function det(mat){let M=mat.map(r=>r.map(x=>[...x]));const n=M.length;let z=q(1);for(let k=0;k<n;k++){let pivot=k;while(pivot<n&&!M[pivot][k][0])pivot++;if(pivot===n)return q(0);if(pivot!==k){[M[k],M[pivot]]=[M[pivot],M[k]];z=neg(z);}const v=M[k][k];z=mul(z,v);for(let i=k+1;i<n;i++){if(!M[i][k][0])continue;const c=div(M[i][k],v);for(let j=k+1;j<n;j++)M[i][j]=sub(M[i][j],mul(c,M[k][j]));M[i][k]=q(0);}}return z;}
function serial(a){if(typeof a==="bigint")return a.toString();if(Array.isArray(a))return a.map(serial);if(a&&typeof a==="object"){let b={};for(const k in a)b[k]=serial(a[k]);return b;}return a;}
return{gcd,q,add,sub,mul,div,neg,sc,zeros,conv,inv,pow,theta,det,serial};})();

function certificate() {
 const {q,conv,pow,theta,det,gcd,serial}=R;
 const A=n=>Math.floor((n+1)/4),B=n=>Math.floor((n+1)/3),
 C=n=>Math.floor(n/2),
 b=n=>Math.floor(9*n/2)+4-2*A(n)-B(n)+C(n);
 const limit=16, Y=conv([q(1),q(8)],theta(limit),limit),
 hh=[q(1),q(4,7),q(16,7)], dd=[q(1),q(8)], vv=[q(1),q(-1)];
 const primes=[2n,3n,5n,7n,11n,13n,17n,19n,23n,29n,31n,37n,41n,43n,47n,53n,59n,61n,67n,71n,73n,79n,83n];
 function remainder(a) {
   let x=a<0n?-a:a;
   if(x===0n) return 0n;
   for(const p of primes) while(x%p===0n) x/=p;
   return x;
 }
 function F(n,j) {
  let z=pow(Y,j,limit);
  for(const [f,e] of [[hh,A(n+j)-A(n)],[vv,B(n+j)-B(n)],[dd,C(n)-C(n+j)]])
   z=conv(z,pow(f,e,limit),limit);
  return z;
 }
 const expected=[1376n,2074n,1048576n,1n,16n,8192n,128n,1n,65536n,8n,64n,1n];
 const cases=[];
 for(let residue=0;residue<12;residue++){
   const D=residue<3?residue+12:residue,n=D-3,
    d1=b(n+1)-b(n),d2=b(n+2)-b(n+1),d3=b(D)-b(D-1),
    u=residue===1?1:0,L=d1+d2+d3-u,start=d1+d2+1,rows=Math.max(0,L-start);
   const f1=F(n,1),f2=F(n,2),aa=pow(f2,-1,limit),h=conv(f1,aa,limit);
   const M=Array.from({length:rows},(_,i)=>Array.from({length:d1+2},(_,j)=>
      j===0?aa[start+i]:h[start+i-j+1]));
   const sets=rows===0?[[]]:
      [Array.from({length:rows},(_,j)=>j),
       [...Array.from({length:rows-1},(_,j)=>j),rows]];
   const minors=sets.map(columns=>{
      const value=rows===0?q(1):det(M.map(row=>columns.map(j=>row[j])));
      if(value[0]===0n) throw new Error("chosen minor is zero");
      if(remainder(value[1])!==1n) throw new Error("denominator has a prime >83");
      return {columns,value};
   });
   const gg=minors.reduce((g,x)=>gcd(g,x.value[0]),0n);
   if(gg!==expected[residue])throw new Error("wrong gcd in residue "+residue);
   if(remainder(gg)!==1n)throw new Error("gcd retains a prime >83");
   if(residue===1) {
      const k=(D-1)/12;
      if(6*b(D)+77!==300*k+125 || (300*k+125)%5!==0)
        throw new Error("missing impossible-prime class");
   }
   cases.push({D_mod_12:residue,representative_D:D,
     gaps:[d1,d2,d3],tested_u:u,target_length:L,
     reduced_first_row:start,reduced_rows:rows,reduced_columns:d1+2,
     minors,numerator_gcd:gg});
 }
 return serial({
   status:"all 12 exact rational certificates passed",
   model:"Y(t)=(1+8t)*exp(sum ell_n*t^n), ell_n=17/(3n)*(1/3)_n/(5/6)_n",
   scope:"D>=3, p=6s-1>101, ell=1 or 2, b_D-(s-13)>=0; no prime scan",
   common_denominator_prime_bound:83,cases});
}

const report = certificate();
if (typeof process !== "undefined" && process.stdout) process.stdout.write(JSON.stringify(report,null,2)+"\n");
report;
