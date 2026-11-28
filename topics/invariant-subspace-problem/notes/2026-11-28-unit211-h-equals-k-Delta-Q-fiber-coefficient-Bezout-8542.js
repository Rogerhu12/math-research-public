"use strict";
// NEW corrected h=k Delta: rule out identically-zero Q fibers.
// Pure lambda Bezout for the exact coefficient compatibility F and E*(B^2-A^3).
// No old resultant, coefficient cache, or frozen target is used.
const began=Date.now();let products=0,divisions=0;
const abs=a=>a<0n?-a:a;
function gcd(a,b){a=abs(a);b=abs(b);while(b){const t=a%b;a=b;b=t}return a}
function q(n=0n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d}const g=gcd(n,d);return[n/g,d/g]}
const qa=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const qn=a=>[-a[0],a[1]];
const qm=(a,b)=>q(a[0]*b[0],a[1]*b[1]);
const qi=a=>q(a[1],a[0]);
const zero=q(),one=q(1);
function trim(p){while(p.length&&!p[p.length-1][0])p.pop();return p}
const C=n=>n===0?[]:[q(n)];
const P=a=>trim(a.map(x=>q(x)));
function add(a,b){const z=[];for(let i=0;i<Math.max(a.length,b.length);i++)z.push(qa(a[i]||zero,b[i]||zero));return trim(z)}
const neg=a=>a.map(qn),sub=(a,b)=>add(a,neg(b));
function mul(a,b){if(Date.now()-began>120000)throw Error("absolute new identity budget");products++;const z=Array.from({length:Math.max(0,a.length+b.length-1)},()=>zero);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)z[i+j]=qa(z[i+j],qm(a[i],b[j]));return trim(z)}
const scale=(a,c)=>trim(a.map(x=>qm(x,c)));
function pow(a,n){let z=C(1);while(n--){z=mul(z,a)}return z}
function dm(a,b){if(!b.length)throw Error("zero polynomial divisor");let r=a.slice(),z=[];while(r.length>=b.length){const k=r.length-b.length,c=qm(r[r.length-1],qi(b[b.length-1]));z[k]=qa(z[k]||zero,c);const t=Array.from({length:k},()=>zero).concat(scale(b,c));r=sub(r,t)}z=trim(Array.from({length:z.length},(_,i)=>z[i]||zero));if(sub(a,add(mul(z,b),r)).length)throw Error("division product");divisions++;return[z,r]}
function egcd(a,b){let r=a,s=b,x=C(1),y=[],v=[],w=C(1);while(s.length){const [d,z]=dm(r,s);[r,s]=[s,z];[x,v]=[v,sub(x,mul(d,v))];[y,w]=[w,sub(y,mul(d,w))]}const c=qi(r[r.length-1]);return[scale(r,c),scale(x,c),scale(y,c)]}
const lam=P([0,1]),A=P([1,-2,2]),B=P([-1,3,-6,4]);
const c=P([3,-2]),d=P([3,-4]),E=P([-1,1,1]);
const H=add(B,mul(c,A)),I=add(H,B);
const Pell=sub(pow(B,2),pow(A,3));
const F=add(add(mul(mul(pow(A,2),I),d),mul(pow(A,3),H)),mul(mul(B,H),add(H,I)));
const G=mul(Pell,E);
const [g,x,y]=egcd(F,G);
if(sub(add(mul(x,F),mul(y,G)),g).length)throw Error("full Bezout identity");
const paid=mul(mul(mul(A,B),lam),I);let rest=g,rounds=0;
while(rest.length>1){const [z]=egcd(rest,paid);if(z.length<=1)break;const [r,t]=dm(rest,z);if(t.length)throw Error("paid division");rest=r;rounds++}
const show=p=>p.map(x=>x[1]===1n?x[0].toString():x[0]+"/"+x[1]);
return {schema:"isp-corrected-hk-Delta-Q-fiber-coefficient-Bezout-v1",
elapsed_milliseconds:Date.now()-began,integerRationalPolynomialProducts:products,
exactPolynomialDivisionProducts:divisions,
definitions:"H=B+(3-2lambda)A, I=H+B, F=A^2 I(3-4lambda)+A^3 H+B H(H+I), G=(B^2-A^3)(lambda^2+lambda-1)",
degrees:{F:F.length-1,G:G.length-1,gcd:g.length-1},
fullBezoutPolynomialProductReturned:true,gcdLowToHigh:show(g),
paidSupport:"A*B*lambda*(2B+(3-2lambda)A)",paidStripRounds:rounds,
remainingLowToHigh:show(rest),
noIdenticallyZeroQFiberInPaidChart:rest.length===1,
sourceScope:"Only new pure-lambda coefficient compatibility; original Delta coefficient derivation is in the proof",
noOldResultantOrProjectionRepeated:true,ordinaryISPClaim:false};
