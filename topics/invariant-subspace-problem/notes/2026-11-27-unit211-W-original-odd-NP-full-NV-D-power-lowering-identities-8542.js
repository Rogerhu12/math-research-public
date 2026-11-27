/* Exact new odd-N/P and full-NV D-power lowering identities.
These are cleared polynomial identities; no D or norm inverse. */
(()=>{
const begin=Date.now(),sha256=function sha256Ascii(s){
for(let i=0;i<s.length;i++)if(s.charCodeAt(i)>127)throw new Error("non-ASCII hash input");
const K=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
const n=Math.ceil((s.length+9)/64)*64,bytes=new Uint8Array(n);for(let i=0;i<s.length;i++)bytes[i]=s.charCodeAt(i);bytes[s.length]=128;let bits=BigInt(s.length)*8n;for(let j=0;j<8;j++){bytes[n-1-j]=Number(bits&255n);bits>>=8n;}
const rr=(x,k)=>(x>>>k)|(x<<(32-k));let h=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];
for(let off=0;off<n;off+=64){const w=new Uint32Array(64);for(let j=0;j<16;j++)w[j]=(bytes[off+4*j]<<24)|(bytes[off+4*j+1]<<16)|(bytes[off+4*j+2]<<8)|bytes[off+4*j+3];for(let j=16;j<64;j++){let x=w[j-15],y=w[j-2];w[j]=(w[j-16]+(rr(x,7)^rr(x,18)^(x>>>3))+w[j-7]+(rr(y,17)^rr(y,19)^(y>>>10)))>>>0;}
let[a,b,c,d,e,f,g,z]=h;for(let j=0;j<64;j++){let t1=(z+(rr(e,6)^rr(e,11)^rr(e,25))+((e&f)^(~e&g))+K[j]+w[j])>>>0;let t2=((rr(a,2)^rr(a,13)^rr(a,22))+((a&b)^(a&c)^(b&c)))>>>0;[z,g,f,e,d,c,b,a]=[g,f,e,(d+t1)>>>0,c,b,a,(t1+t2)>>>0];}h=h.map((x,j)=>(x+[a,b,c,d,e,f,g,z][j])>>>0);}
return h.map(x=>x.toString(16).padStart(8,"0")).join("");
};
const vars=['ell','m','M','d','D','K','lambda','P02','A0','nb','pb','Z0','Z1','Z2'],N=vars.length,zkey=Array(N).fill(0).join(',');
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


const [ell,m,M,d,D,K,lam,P02,A,nb,pb,Z0,Z1,Z2]=vars.map((_,j)=>P.variable(j));
function assert(v,n){if(!v)throw Error(n);}
const R6=M.mul(K.pow(2)).sub(m.pow(2).mul(D.pow(3)).scale(4));
const DNnum=m.mul(ell).mul(D.pow(2)).mul(nb)
 .add(lam.mul(P02).mul(ell).mul(D).mul(K).mul(A).scale(2))
 .add(lam.mul(P02).mul(K.pow(2)));
const NLnum=m.mul(ell).mul(M).mul(D).mul(nb)
 .add(lam.mul(P02).mul(ell.mul(M).mul(K).mul(A).add(m.pow(2).mul(D.pow(2)).scale(2))).scale(2));
assert(M.mul(DNnum).sub(D.mul(NLnum)).eq(lam.mul(P02).mul(R6)),'full odd N lower-D identity');
const H=m.pow(2).scale(3).add(d.mul(ell.pow(2)));
const DPnum=m.pow(3).mul(ell.pow(2)).mul(D.pow(3)).mul(pb).scale(8)
 .add(P02.mul(m.pow(2).mul(ell.pow(2)).mul(D.pow(2)).mul(A.pow(2)).mul(K).scale(12)
 .add(m.pow(2).mul(ell).mul(D).mul(A).mul(K.pow(2)).scale(12)).add(H.mul(K.pow(3)))));
const PLnum=m.mul(ell.pow(2)).mul(M).mul(D).mul(pb).scale(2)
 .add(P02.mul(ell.pow(2).mul(M).mul(K).mul(A.pow(2)).scale(3)
 .add(H.mul(D).mul(K)).add(m.pow(2).mul(ell).mul(A).mul(D.pow(2)).scale(12))));
const Prhs=P02.mul(R6).mul(m.pow(2).mul(ell).mul(D).mul(A).scale(12).add(H.mul(K)));
assert(M.mul(DPnum).sub(m.pow(2).mul(D.pow(2)).mul(PLnum).scale(4)).eq(Prhs),'full odd P lower-D identity');
const NVnum=m.pow(2).mul(D.pow(2)).mul(Z0).scale(4)
 .add(m.mul(D).mul(K).mul(Z1).scale(2)).add(K.pow(2).mul(Z2));
const VLnum=m.mul(M).mul(D).mul(Z0).scale(2)
 .add(M.mul(K).mul(Z1)).add(m.mul(D.pow(2)).mul(Z2).scale(2));
assert(M.mul(NVnum).sub(m.mul(D).mul(VLnum).scale(2)).eq(Z2.mul(R6)),'entire original quadratic NV lower-D identity');
const cert=JSON.stringify({R6:R6.data(),DNnum:DNnum.data(),NLnum:NLnum.data(),DPnum:DPnum.data(),PLnum:PLnum.data(),NVnum:NVnum.data(),VLnum:VLnum.data()});
return {schema:'isp-W-original-odd-N-P-and-entire-NV-D-power-lowering-v1',
 variables:vars,A0Meaning:'(ell+T)/ell',
 fullAllThreeClearedOriginalPolynomialIdentitiesActuallyVerified:true,
 noDOrNormInverse:true,noNumericalSpecialization:true,
 coefficientDenominatorsOnlyPaidEllMAndLittleM:true,
 exactNRelation:'DNodd = D*Nlow + lambda*P02*R6/(m*ell*M)',
 exactPRelation:'DPodd = D^2*Plow + P02*R6/M*(3*D*A0/(2*m*ell)+(3*m^2+d*ell^2)*K/(8*m^3*ell^2))',
 exactNVRelation:'N4(D*Vval)=D*Vlow+Z2*R6/(4*m^2*M)',
 certificate:{bytes:cert.length,sha256:sha256(cert)},
 elapsedMilliseconds:Date.now()-begin,
 noNewOriginalParameterFiberExcluded:true};
})()
