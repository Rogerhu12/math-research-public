"use strict";
// Identify the two small exact eta-quotient parameters from their compact formulas; no original Gram gate runs.
// Eight free variables b,c,p,q,X,Y,t,eta with f=u+eta. True dual product.
// Compact two scalar consequences below are used only after p+q=2 and original value equalities.
const began=Date.now(),D=8,ZKEY="0,0,0,0,0,0,0,0";let products=0;
function C(n=0n){return n===0n?new Map():new Map([[ZKEY,n]])}
function V(i){const a=Array(D).fill(0);a[i]=1;return new Map([[a.join(","),1n]])}
function add(a,b){const c=new Map(a);for(const[k,v]of b){let x=(c.get(k)||0n)+v;if(x)c.set(k,x);else c.delete(k)}return c}
function neg(a){return new Map([...a].map(([k,v])=>[k,-v]))}
function sub(a,b){return add(a,neg(b))}
function mul(a,b){if(Date.now()-began>120000)throw Error("new original bipartite jet identity 120 second budget");products++;const c=new Map();for(const[ka,va]of a){const ea=ka.split(",").map(Number);for(const[kb,vb]of b){const eb=kb.split(",").map(Number),k=ea.map((x,i)=>x+eb[i]).join(","),x=(c.get(k)||0n)+va*vb;if(x)c.set(k,x);else c.delete(k)}}return c}
function sc(a,n){return mul(a,C(BigInt(n)))}
function sq(a){return mul(a,a)}
function sum(xs){return xs.reduce(add,C())}
function prod(xs){return xs.reduce(mul,C(1n))}

const [b,c,p,q,X,Y,t,eta]=Array.from({length:D},(_,i)=>V(i));
const one=C(1n),zero=C(),ell=add(b,c),a=sub(one,ell);
const uu=add(mul(b,p),mul(c,q)),scalarV0=add(mul(b,X),mul(c,Y));

const u=uu,f=add(u,eta),Vmean=scalarV0,sigma=add(p,q);
const V2=add(mul(b,sq(p)),mul(c,sq(q)));
const W1=add(prod([b,p,X]),prod([c,q,Y]));
const E0=sum([V2,sc(W1,-2),sc(sq(u),-2),sc(mul(f,u),4)]);
const A1=sum([sc(f,2),sc(Vmean,-2),sc(prod([b,c,t]),2)]);
const Rw=add(sc(E0,-2),sc(prod([b,c,t,sub(sigma,t)]),4));
const Rl=sum([Rw,sc(mul(u,A1),-4),sc(prod([b,c,sigma,t]),4)]);
function canonical(P){return [...P].map(([key,c])=>[key.split(",").map(Number),String(c)])
 .sort((a,b)=>{for(let i=0;i<D;i++)if(a[0][i]!==b[0][i])return a[0][i]-b[0][i];return 0;});}

const sha256=(function sha256(str){const s=unescape(encodeURIComponent(str)),a=Array.from(s,c=>c.charCodeAt(0)),n=a.length*8; a.push(128);while(a.length%64!==56)a.push(0);for(let k=7;k>=0;k--)a.push(k>=4?0:(n>>>8*k)&255);const K=[],H=[];for(let p=2;K.length<64;p++){let prime=true;for(let d=2;d*d<=p;d++)if(p%d===0){prime=false;break;}if(prime){if(H.length<8)H.push((Math.sqrt(p)%1*4294967296)|0);K.push((Math.cbrt(p)%1*4294967296)|0);}}const r=(x,n)=>(x>>>n)|(x<<(32-n));for(let at=0;at<a.length;at+=64){const w=[];for(let i=0;i<16;i++)w[i]=(a[at+4*i]<<24)|(a[at+4*i+1]<<16)|(a[at+4*i+2]<<8)|a[at+4*i+3];for(let i=16;i<64;i++){let s0=r(w[i-15],7)^r(w[i-15],18)^(w[i-15]>>>3),s1=r(w[i-2],17)^r(w[i-2],19)^(w[i-2]>>>10);w[i]=(w[i-16]+s0+w[i-7]+s1)|0;}let [a0,b,c,d,e,f,g,h]=H;for(let i=0;i<64;i++){let S1=r(e,6)^r(e,11)^r(e,25),ch=(e&f)^(~e&g),t1=(h+S1+ch+K[i]+w[i])|0,S0=r(a0,2)^r(a0,13)^r(a0,22),maj=(a0&b)^(a0&c)^(b&c),t2=(S0+maj)|0;h=g;g=f;f=e;e=(d+t1)|0;d=c;c=b;b=a0;a0=(t1+t2)|0;}for(const [i,x]of [a0,b,c,d,e,f,g,h].entries())H[i]=(H[i]+x)|0;}return H.map(x=>(x>>>0).toString(16).padStart(8,"0")).join("");});
const actualRw=sha256(JSON.stringify(canonical(Rw))),actualRl=sha256(JSON.stringify(canonical(Rl)));
if(actualRw!=="3dd5ab30079285cc5e065fe6ced6802d23690e1d94a7103a8869f735bb0d559f"||actualRl!=="05b1367603f039ea2507b992a00d49acc7d6149fbca6b0020b5426f6320176f9")throw Error("Compact parameter identity does not match actual original quotient");
return {schema:"isp-free-f-compact-eta-quotients-identification-v1",elapsedMilliseconds:Date.now()-began,
 integerPolynomialProducts:products,RwSHA256:actualRw,RlSHA256:actualRl,
 RwTerms:Rw.size,RlTerms:Rl.size,bothOriginalParametersIdentified:true,
 originalGramGateNotReplayed:true,ordinaryISPClaim:false};
