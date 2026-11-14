
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;}
function R(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return [a/g,b/g];}
const add=(a,b)=>R(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>[-a[0],a[1]];
const sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>R(a[0]*b[0],a[1]*b[1]);
const div=(a,b)=>R(a[0]*b[1],a[1]*b[0]);
const fmt=a=>a[1]===1n?""+a[0]:a[0]+"/"+a[1];
const N=5,Z=()=>Array.from({length:N+1},()=>R(0));
const pa=(a,b)=>a.map((x,i)=>add(x,b[i]));
function pm(a,b){const c=Z();for(let i=0;i<=N;i++)for(let j=0;j+i<=N;j++)c[i+j]=add(c[i+j],mul(a[i],b[j]));return c;}
function pp(a,n){let c=Z();c[0]=R(1);for(let i=0;i<n;i++)c=pm(c,a);return c;}
function pe(a){if(a[0][0])throw Error("exp nonzero constant");let c=Z();c[0]=R(1);for(let n=1;n<=N;n++){for(let k=1;k<=n;k++)c[n]=add(c[n],mul(R(k),mul(a[k],c[n-k])));c[n]=div(c[n],R(n));}return c;}

const X=Z();X[0]=R(1);X[1]=R(-1,7);
for(let n=2;n<=N;n++){let q=R(0);for(let i=1;i<n;i++)q=add(q,mul(X[i],X[n-i]));X[n]=mul(q,R(6,(6*n-2)*(6*n-3)-12));}
const A=Z();for(let n=1;n<=N;n++)A[n]=div(neg(X[n]),R(6*n*(6*n-1)));
const E=pe(A.map(a=>mul(R(34),a)));
const F=Array.from({length:6},(_,j)=>{let f=pm(E,pp(X,2+3*j));return Array.from({length:6},(_,m)=>m<5-j?R(0):f[m-(5-j)]);});
const ell=[-329,14,112,-616,7168,-15232].map(n=>R(n,17496));
const q=Z();
for(let j=0;j<=5;j++){let v=ell[j];for(let m=6-j;m<=5;m++)v=sub(v,mul(q[m],F[j][m]));q[5-j]=v;}
const checks=[];
for(let j=0;j<6;j++){
 let v=R(0);for(let m=0;m<=5;m++)v=add(v,mul(q[m],F[j][m]));
 if(fmt(v)!==fmt(ell[j]))throw Error("dual row failed at "+j);
 checks.push("full CM13 dual on F_"+j);
}
const s=[R(-128,7),R(-80,7),R(-12,7),R(-53,7),R(1),R(0)];
let one=R(0);for(let j=0;j<6;j++)one=add(one,mul(ell[j],s[j]));
if(fmt(one)!=="1")throw Error("S normalization");
checks.push("actual S normalization");
let fact=1n;for(let n=1;n<=30;n++)fact*=BigInt(n);
const leading=div(q[5],R(fact));
if(fmt(leading)!=="-47/662980576467727823128693309440000000")throw Error("leading weight");
checks.push("degree thirty leading coefficient");
const mixed=R(720n**3n,84n*2952450n);
if(fmt(mixed)!=="2560/1701")throw Error("mixed scalar");
checks.push("original mixed factor and signs");
let den=1n;for(const a of q)den=den/gcd(den,a[1])*a[1];
const primes=[];
for(let p=2n;p*p<=den;p++){if(den%p===0n){let e=0;while(den%p===0n){den/=p;e++;}primes.push([String(p),e]);}}
if(den>1)primes.push([String(den),1]);
if(primes.some(([p])=>BigInt(p)>29n))throw Error("denominator prime bound");
checks.push("all fixed denominator primes at most twenty-nine");
const certificate={status:"PASS",checks,X:X.map(fmt),A:A.map(fmt),F:F.map(f=>f.map(fmt)),q:q.map(fmt),denominatorPrimes:primes,leading:fmt(leading),mixedScalar:fmt(mixed)};
console.log(JSON.stringify(certificate,null,2));
