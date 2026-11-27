/* Exact new whole W monic T^3 leading identity after lambda=3/2 exclusion.
Integer polynomial arithmetic, no geometry or norm inverse. */
(()=>{
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
const vars=['ell','u','m','Q','J','d','lambda','T'],N=vars.length,zkey=Array(N).fill(0).join(',');
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

function assert(v,m){if(!v)throw Error(m);}
const [ell,u,m,Q,J,d,lam,T]=vars.map((_,j)=>P.variable(j));
const M=ell.pow(2).mul(d).sub(m.pow(2));
const Al=lam.pow(2).scale(2).sub(lam.scale(2)).add(1);
const Bl=lam.pow(3).scale(4).sub(lam.pow(2).scale(6)).add(lam.scale(3)).sub(1);
const c=new P(3).sub(lam.scale(2)),astar=u.mul(Q).scale(4).sub(J);
const cstar=astar.mul(m.pow(2)).add(J.mul(d).mul(ell.pow(2)));
const D=ell.mul(Al).sub(T.pow(2));
const K=ell.pow(2).mul(Bl).sub(ell.mul(T).mul(Al).scale(3)).add(T.pow(3).scale(2));
const ad=M.mul(ell.pow(2)).mul(Q).mul(new P(3).sub(lam.scale(4)))
 .add(M.mul(astar).mul(T.pow(2))).add(M.mul(u).mul(Q).mul(c).mul(ell).mul(T).scale(2))
 .add(cstar.mul(D));
const bd=M.mul(m).mul(astar.mul(T).add(u.mul(Q).mul(c).mul(ell))).scale(2);
const R4=M.mul(ad.pow(2)).sub(D.mul(bd.pow(2)));
const C4=m.mul(D).mul(ad).scale(2).add(K.mul(bd));
function coefficient(poly,j){
 const ans=new P();
 for(const [mm,cc] of poly.t){const ex=mm.split(',').map(Number);if(ex[7]!==j)continue;ex[7]=0;const key=ex.join(',');ans.t.set(key,(ans.t.get(key)||0n)+cc);}
 for(const [mm,cc]of ans.t)if(!cc)ans.t.delete(mm);
 return ans;
}
const c4=m.mul(u).mul(Q).mul(ell.pow(2)).mul(d).scale(8);
assert(coefficient(C4,4).eq(c4),'whole original C4 T4 leading');
assert(coefficient(C4,3).eq(0),'whole original C4 T3 exactly zero');
const a2=M.mul(astar).sub(cstar),b1=M.mul(m).mul(astar).scale(2);
const L4=M.mul(a2.pow(2)).add(b1.pow(2));
assert(coefficient(R4,4).eq(L4),'R4 original T4 leading');
const theta=M.pow(2).mul(u).mul(Q).mul(c).mul(ell.pow(3)).mul(d)
 .mul(u.mul(Q).scale(2).sub(J)).scale(8);
const R3num=c4.mul(R4).sub(L4.mul(C4));
assert(R3num.degree([7])===3,'whole original cubic numerator');
assert(coefficient(R3num,3).eq(c4.mul(theta)),'complete cubic leading');
assert(R3num.add(L4.mul(C4)).eq(c4.mul(R4)),'full original two-quartic combination');
const coeff=[0,1,2,3].map(j=>coefficient(R3num,j));
const encoded=JSON.stringify({C4:C4.data(),R4:R4.data(),c4:c4.data(),L4:L4.data(),theta:theta.data(),R3num:R3num.data()});
return {
 schema:'isp-whole-W-original-monic-T-three-exact-leading-v1',
 variables:vars,onlyWeightRelationSubstituted:'M=ell^2*d-m^2',
 allIntegerCoefficientIdentitiesActuallyVerified:true,
 C4T4Leading:'8*m*u*Q*ell^2*d',C4T3Coefficient:0,
 R3Definition:'R4-[T^4]R4*C4/(8*m*u*Q*ell^2*d)',
 R3T3Leading:'8*M^2*u*Q*(3-2*lambda)*ell^3*d*(2*u*Q-J)',
 originalCombinationNumeratorProfile:R3num.profile(),
 numeratorTCoefficientProfiles:coeff.map(x=>x.profile()),
 sameLambdaAndTInBothOriginalQuartics:true,noDOrNormInverse:true,
 newGeometryHeadOnly:'3-2*lambda; paid by complete previous whole-fiber theorem',
 certificate:{bytes:encoded.length,sha256:sha256(encoded)},
 elapsedMilliseconds:Date.now()-begin,
 wholeWExcluded:false
};
})()
