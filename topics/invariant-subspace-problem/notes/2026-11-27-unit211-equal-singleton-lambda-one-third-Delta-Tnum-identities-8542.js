/* Exact parent-requested hU=kU lambda=1/3 Delta/Tnum factor identities. */
(()=>{
const begin=Date.now();const sha256=function sha256Ascii(s){
for(let i=0;i<s.length;i++)if(s.charCodeAt(i)>127)throw new Error("non-ASCII hash input");
const K=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
const n=Math.ceil((s.length+9)/64)*64,bytes=new Uint8Array(n);for(let i=0;i<s.length;i++)bytes[i]=s.charCodeAt(i);bytes[s.length]=128;let bits=BigInt(s.length)*8n;for(let j=0;j<8;j++){bytes[n-1-j]=Number(bits&255n);bits>>=8n;}
const rr=(x,k)=>(x>>>k)|(x<<(32-k));let h=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];
for(let off=0;off<n;off+=64){const w=new Uint32Array(64);for(let j=0;j<16;j++)w[j]=(bytes[off+4*j]<<24)|(bytes[off+4*j+1]<<16)|(bytes[off+4*j+2]<<8)|bytes[off+4*j+3];for(let j=16;j<64;j++){let x=w[j-15],y=w[j-2];w[j]=(w[j-16]+(rr(x,7)^rr(x,18)^(x>>>3))+w[j-7]+(rr(y,17)^rr(y,19)^(y>>>10)))>>>0;}
let[a,b,c,d,e,f,g,z]=h;for(let j=0;j<64;j++){let t1=(z+(rr(e,6)^rr(e,11)^rr(e,25))+((e&f)^(~e&g))+K[j]+w[j])>>>0;let t2=((rr(a,2)^rr(a,13)^rr(a,22))+((a&b)^(a&c)^(b&c)))>>>0;[z,g,f,e,d,c,b,a]=[g,f,e,(d+t1)>>>0,c,b,a,(t1+t2)>>>0];}h=h.map((x,j)=>(x+[a,b,c,d,e,f,g,z][j])>>>0);}
return h.map(x=>x.toString(16).padStart(8,"0")).join("");
};
const vars=['u','Q'],N=2,zkey='0,0';
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


const u=P.variable(0),Q=P.variable(1),one=new P(1);
function assert(v,m){if(!v)throw Error(m);}
const t0=u.pow(2).scale(-392).add(u.scale(392)).sub(Q.scale(125));
const j=u.pow(2).scale(-392).add(u.scale(392)).add(Q.scale(125));
const phi=u.pow(2).scale(-392).add(u.scale(1176)).sub(784).add(Q.scale(71));
const p02=u.pow(3).scale(392).sub(u.pow(2).scale(1176)).add(u.scale(784)).add(u.mul(Q).scale(179)).sub(Q.scale(250));
const g=p02.add(u.sub(1).mul(t0).scale(3));
const dl=u.sub(1).mul(u.sub(3)).scale(196).sub(Q.scale(71));
const tl=u.mul(u.sub(1)).mul(u.scale(19).sub(2)).scale(-392).add(new P(250).sub(u.scale(1457)).mul(Q));
assert(j.sub(Q.scale(196)).sub(phi.scale(3)).eq(dl.scale(4)),'Delta original factor');
const np=j.sub(Q.scale(196)).mul(g.sub(u.mul(Q).scale(45))).add(Q.mul(p02).scale(25)).sub(g.mul(t0));
assert(np.eq(Q.mul(tl).scale(2)),'Tnum original factor');
const f=new P(250).sub(u.scale(1457));
assert(tl.scale(71).add(f.mul(dl)).eq(u.sub(1).pow(2).mul(u.scale(277).sub(50)).scale(-2940)),'complete Q elimination');
return {
 schema:'isp-parent-h-equals-k-lambda-one-third-original-Delta-Tnum-factor-v1',
 constants:{ell:'125/196',T:'-25/42',xi:'-14/15',w:'-1/14',S:'7/15',eta:'7/5'},
 NF:'-98*T0/75',
 Delta:'(2*T0/225)*(196*(u-1)*(u-3)-71*Q)',
 Tnum:'(Q*T0/44100)*(-392*u*(u-1)*(19*u-2)+(250-1457*u)*Q)',
 exactElimination:'71*Tlin+(250-1457*u)*Dlin=-2940*(u-1)^2*(277*u-50)',
 candidateAfterPaidUminusOneQT0:{u:'50/277',Q:'489412/76729'},
 allThreeFullIntegerPolynomialProductsActuallyVerified:true,
 elapsedMilliseconds:Date.now()-begin,
 originalGramNotReturnedHere:true
};
})()
