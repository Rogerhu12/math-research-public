/* Whole current W, lambda=3/2: exact same-value ratio and e-quadratic reduction.
   BigInt polynomial identities; no specialization, field root, or unproved inverse. */
(() => {
const begin=Date.now();
const sha256=function sha256Ascii(s){
for(let i=0;i<s.length;i++)if(s.charCodeAt(i)>127)throw new Error("non-ASCII hash input");
const K=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
const n=Math.ceil((s.length+9)/64)*64,bytes=new Uint8Array(n);for(let i=0;i<s.length;i++)bytes[i]=s.charCodeAt(i);bytes[s.length]=128;let bits=BigInt(s.length)*8n;for(let j=0;j<8;j++){bytes[n-1-j]=Number(bits&255n);bits>>=8n;}
const rr=(x,k)=>(x>>>k)|(x<<(32-k));let h=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];
for(let off=0;off<n;off+=64){const w=new Uint32Array(64);for(let j=0;j<16;j++)w[j]=(bytes[off+4*j]<<24)|(bytes[off+4*j+1]<<16)|(bytes[off+4*j+2]<<8)|bytes[off+4*j+3];for(let j=16;j<64;j++){let x=w[j-15],y=w[j-2];w[j]=(w[j-16]+(rr(x,7)^rr(x,18)^(x>>>3))+w[j-7]+(rr(y,17)^rr(y,19)^(y>>>10)))>>>0;}
let[a,b,c,d,e,f,g,z]=h;for(let j=0;j<64;j++){let t1=(z+(rr(e,6)^rr(e,11)^rr(e,25))+((e&f)^(~e&g))+K[j]+w[j])>>>0;let t2=((rr(a,2)^rr(a,13)^rr(a,22))+((a&b)^(a&c)^(b&c)))>>>0;[z,g,f,e,d,c,b,a]=[g,f,e,(d+t1)>>>0,c,b,a,(t1+t2)>>>0];}h=h.map((x,j)=>(x+[a,b,c,d,e,f,g,z][j])>>>0);}
return h.map(x=>x.toString(16).padStart(8,"0")).join("");
};
const vars=['e','k','z'],N=3,zkey='0,0,0';
class P {
 constructor(v=0n){this.t=new Map();if(v instanceof P){this.t=new Map(v.t);return;}v=BigInt(v);if(v)this.t.set(zkey,v);}
 static variable(j){const a=new P(),e=Array(N).fill(0);e[j]=1;a.t.set(e.join(","),1n);return a;}
 add(v){v=new P(v);const r=new P(this);for(const [m,c]of v.t){const w=(r.t.get(m)||0n)+c;if(w)r.t.set(m,w);else r.t.delete(m);}return r;}
 neg(){const r=new P();for(const [m,c]of this.t)r.t.set(m,-c);return r;}
 sub(v){return this.add(new P(v).neg());}
 mul(v){v=new P(v);const r=new P();for(const [ma,ca]of this.t){const a=ma.split(",").map(Number);for(const [mb,cb]of v.t){const b=mb.split(",").map(Number),key=a.map((x,j)=>x+b[j]).join(","),w=(r.t.get(key)||0n)+ca*cb;if(w)r.t.set(key,w);else r.t.delete(key);}}return r;}
 pow(n){let r=new P(1n),a=this;for(;n;n>>=1){if(n&1)r=r.mul(a);if(n>1)a=a.mul(a);}return r;}
 scale(v){return this.mul(v);}
 eq(v){return this.sub(v).t.size===0;}
 degree(ids){let d=-1;for(const [m]of this.t){const a=m.split(",").map(Number);d=Math.max(d,ids.reduce((s,j)=>s+a[j],0));}return d;}
 data(){return [...this.t].sort((a,b)=>a[0].localeCompare(b[0])).map(([m,c])=>[m.split(",").map(Number),c.toString()]);}
 profile(){const s=JSON.stringify(this.data());return {terms:this.t.size,degrees:vars.map((_,j)=>this.degree([j])),bytes:s.length,sha256:sha256(s)};}
}

const [e,k,z]=vars.map((_,j)=>P.variable(j));
const u=e.add(1),Q=e.mul(k),d=new P(1).sub(Q),V=u.mul(k).add(2);
const Lhat=k.add(2).pow(2).sub(e.mul(k).scale(2));
const mhat=k.add(2).mul(Q.sub(2));
const HJ=k.add(2).sub(e.scale(4));
const Ahat=V.scale(4).sub(HJ);
const U=Ahat.add(HJ.mul(d).mul(z.pow(2)));
const P2hat=Lhat.mul(new P(1).add(d.mul(z.pow(2)))).sub(mhat.mul(z).scale(2));
const P3hat=Lhat.mul(new P(1).add(d.mul(z.pow(2)).scale(3)))
 .sub(mhat.mul(z).mul(new P(3).add(d.mul(z.pow(2)))));
const R=P2hat.scale(6).sub(k.mul(U).scale(5));
const Rexpected=d.mul(k.pow(2).add(e.scale(8).add(14).mul(k)).add(24)).mul(z.pow(2))
 .sub(k.add(2).mul(Q.sub(2)).mul(z).scale(12))
 .sub(e.scale(20).add(9).mul(k.pow(2)))
 .sub(e.scale(32).add(6).mul(k)).add(24);
if(!R.eq(Rexpected))throw new Error('whole ratio identity');
const B=k.pow(2).add(k.scale(14)).add(16).mul(z.pow(2))
 .add(k.add(2).mul(z).scale(12)).add(k.scale(20)).add(32);
const C=k.add(2).mul(k.add(12).mul(z.pow(2)).add(z.scale(24)).sub(k.scale(3).sub(4).scale(3)));
const leading=k.pow(2).mul(z.pow(2)).scale(-8);
if(!R.eq(leading.mul(e.pow(2)).sub(k.mul(B).mul(e)).add(C)))throw new Error('all e coefficients');
const H=u.mul(k.pow(2)).mul(U.pow(3)).scale(49).sub(V.mul(P3hat.pow(2)).scale(108));
function ce(p,j){const q=new P();for(const [key,c]of p.t){const a=key.split(',').map(Number);if(a[0]===j){a[0]=0;q.t.set(a.join(','),c);}}return q;}
let rem=H,quot=new P(),scale=new P(1),steps=0;
while(rem.degree([0])>=2){
 const dg=rem.degree([0]),lc=ce(rem,dg),term=lc.mul(e.pow(dg-2));
 rem=leading.mul(rem).sub(term.mul(R));
 quot=leading.mul(quot).add(term);scale=leading.mul(scale);steps++;
 if(steps>20)throw new Error('nonterminating e pseudodivision');
}
if(!scale.mul(H).eq(quot.mul(R).add(rem)))throw new Error('complete original e pseudodivision');
if(!rem.t.size)throw new Error('no new relation');
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r;}return a;}
let cont=0n,mins=[Infinity,Infinity,Infinity];
for(const[key,c]of rem.t){cont=gcd(cont,c);key.split(',').map(Number).forEach((v,j)=>mins[j]=Math.min(mins[j],v));}
if(mins[0]!==0)throw new Error('unexpected e content: do not strip e');
let primitive=new P();
for(const[key,c]of rem.t){const a=key.split(',').map(Number).map((v,j)=>v-mins[j]);primitive.t.set(a.join(','),c/cont);}
const removed=k.pow(mins[1]).mul(z.pow(mins[2])).scale(cont);
if(!removed.mul(primitive).eq(rem))throw new Error('paid monomial content product');
const g0=ce(primitive,0),g1=ce(primitive,1);
if(!primitive.eq(g0.add(g1.mul(e))))throw new Error('same e linear remainder');
const norm=leading.mul(g0.pow(2)).add(k.mul(B).mul(g0).mul(g1)).add(C.mul(g1.pow(2)));
const identity=g1.pow(2).mul(R).sub(norm);
const right=primitive.mul(leading.mul(e).mul(g1).sub(leading.mul(g0)).sub(k.mul(B).mul(g1)));
if(!identity.eq(right))throw new Error('same e original norm combination');
const data={R:R.data(),H:H.data(),scale:scale.data(),quotient:quot.data(),paidMonomialContent:removed.data(),G0:g0.data(),G1:g1.data(),parameterNorm:norm.data()};
const serialized=JSON.stringify(data);
return {receipt:{schema:'isp-W-lambda-three-halves-same-value-ratio-quadratic-v1',
 session:'Astra-ISP-8542378f-20261127',date:'2026-11-27',
 arithmetic:'exact BigInt multivariate polynomial over ZZ; no point or prime specialization',
 lambda:'3/2',sameZDefinition:'z=s/v0; both s and v0 are physical units on the stated original W chart',
 exactWholeRatioAndAllECoefficients:true,eQuadraticLeading:'-8*k^2*z^2',
 fullOriginalHigherMomentPseudodivisionIdentity:true,pseudodivisionSteps:steps,
 removedOnlyNonzeroRationalAndPaidKZMonomial:{integerContent:cont.toString(),kPower:mins[1],zPower:mins[2]},
 lowerMomentRatio:R.profile(),sameValueThirdMoment:H.profile(),
 eLinearG0:g0.profile(),eLinearG1:g1.profile(),necessaryParameterNorm:norm.profile(),
 fullSameELinearNormCombinationActuallyReturned:true,G1ZeroFiberRetained:true,
 AzP3BothZeroFiberPhysicallyExcludedOnlyByOriginalDeltaAndThirdMoment:true,
 noCompleteGramOrIndividualNPExclusion:true,wholeLambdaFiberExcluded:false,
 exactCertificate:{bytes:serialized.length,sha256:sha256(serialized)},
 elapsedMilliseconds:Date.now()-begin,externalProcessExitCode:null,maxRssKiB:null},certificate:data};
})()
