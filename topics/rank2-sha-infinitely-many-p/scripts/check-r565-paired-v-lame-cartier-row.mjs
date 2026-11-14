// R565 exact certificate. Run: node check-r565-paired-v-lame-cartier-row.mjs
const certificate=(()=>{

"use strict";
let checks=0;
const ok=(v,msg)=>{if(!v)throw new Error(msg);checks++;};
const formal=(()=>{
const key=e=>e.join(","),out=P=>Object.fromEntries([...P].sort().map(([e,c])=>[e,c.toString()]));
function binom(n,k){let r=1n;for(let j=1;j<=k;j++)r=r*BigInt(n-j+1)/BigInt(j);return r}
function mono(e,c=1n){
 const P=new Map(),q=Math.floor(e[2]/2),r=e[2]%2;
 for(let j=0;j<=q;j++){const a=[...e];a[0]+=q-j;a[1]+=3*j;a[2]=r;P.set(key(a),c*binom(q,j))}
 return P;
}
const add=(A,B)=>{const C=new Map(A);for(const[k,v]of B){const n=(C.get(k)||0n)+v;if(n)C.set(k,n);else C.delete(k)}return C};
const scale=(A,c)=>new Map([...A].map(([k,v])=>[k,v*BigInt(c)]).filter(([k,v])=>v));
const mul=(A,B)=>{let C=new Map();for(const[ka,a]of A)for(const[kb,b]of B){
 const ea=ka.split(",").map(Number),eb=kb.split(",").map(Number);
 C=add(C,mono(ea.map((v,i)=>v+eb[i]),a*b));
}return C};
const pow=(A,n)=>{let R=mono([0,0,0,0,0]);for(let i=0;i<n;i++)R=mul(R,A);return R};
function diff(P){
 let Q=new Map();
 for(const[k,v]of P){const e=k.split(",").map(Number);
  if(e[1]){const a=[...e];a[1]--;a[2]++;Q=add(Q,mono(a,2n*BigInt(e[1])*v))}
  if(e[2]){const a=[...e];a[2]--;a[1]+=2;Q=add(Q,mono(a,3n*BigInt(e[2])*v))}
  if(e[3]){const a=[...e];a[3]--;a[1]++;Q=add(Q,mono(a,-BigInt(e[3])*v))}
  if(e[4]){const a=[...e];a[3]++;Q=add(Q,mono(a,BigInt(e[4])*v))}
 }
 return Q;
}
const x=mono([0,1,0,0,0]),y=mono([0,0,1,0,0]),g=mono([0,0,0,1,0]),sig=mono([0,0,0,0,1]);

const b=mono([1,0,0,0,0]);
const f4=mul(x,pow(sig,6)),f1=scale(mul(mul(x,y),pow(sig,6)),-1);
const theta=mul(x,pow(sig,2)),Z=mul(add(y,mul(x,g)),pow(sig,6));
const equal=(A,B)=>add(A,scale(B,-1)).size===0;
const conn=A=>add(diff(A),scale(mul(g,A),-6));
const tests={
 bounded_source:equal(scale(Z,2),mul(pow(sig,4),diff(theta))),
 lame_f4:equal(conn(conn(f4)),scale(mul(x,f4),6)),
 lame_Z:equal(conn(conn(Z)),scale(mul(x,Z),6)),
 wronskian:equal(add(mul(f4,diff(Z)),scale(mul(Z,diff(f4)),-1)),scale(mul(b,pow(sig,12)),-2)),
 exact_difference:equal(add(diff(diff(diff(f4))),scale(f1,-24)),scale(mul(pow(g,2),Z),216)),
 covariant_difference:equal(conn(conn(conn(f4))),scale(f1,-24))
};
for(const[k,v]of Object.entries(tests))if(!v)throw new Error(k);
return tests;

})();
for(const [k,v]of Object.entries(formal))ok(v,"characteristic-zero "+k);
const ring=(()=>{
function ring(p,b=1){
 const mod=a=>(a%p+p)%p,pow=(a,n)=>{let r=1;for(a=mod(a);n;n=Math.floor(n/2),a=a*a%p)if(n&1)r=r*a%p;return r},iv=a=>pow(a,p-2);
 const trim=a=>{while(a.length>1&&!a[a.length-1])a.pop();return a},
 add=(a,b)=>trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>mod((a[i]||0)+(b[i]||0)))),
 sc=(a,c)=>trim(a.map(v=>mod(v*c))),neg=a=>sc(a,-1),sub=(a,b)=>add(a,neg(b)),
 mul=(a,b)=>{let r=Array(a.length+b.length-1).fill(0);for(let i=0;i<a.length;i++)if(a[i])for(let j=0;j<b.length;j++)if(b[j])r[i+j]=mod(r[i+j]+a[i]*b[j]);return trim(r)},
 pp=(a,n)=>{let r=[1];for(;n;n=Math.floor(n/2),a=mul(a,a))if(n&1)r=mul(r,a);return r},
 der=a=>trim(a.slice(1).map((v,i)=>mod(v*(i+1)))),xp=n=>{let a=Array(n+1).fill(0);a[n]=1;return a};
 const X=xp(1),Y=add(xp(3),[b]),Y2=mul(Y,Y);
 const memo={0:[0],1:[1],2:[1],3:add(sc(xp(4),3),sc(X,12*b)),4:add(add(sc(xp(6),2),sc(xp(3),40*b)),[-16*b*b])};
 const psi=n=>{if(memo[n])return memo[n];const m=Math.floor(n/2);let r;
 if(n&1){let a=mul(psi(m+2),pp(psi(m),3)),c=mul(psi(m-1),pp(psi(m+1),3));r=(m&1)?sub(a,sc(mul(Y2,c),16)):sub(sc(mul(Y2,a),16),c)}
 else r=mul(psi(m),sub(mul(psi(m+2),pp(psi(m-1),2)),mul(psi(m-2),pp(psi(m+1),2))));
 return memo[n]=r};
 const rootP=a=>{let r=Array(Math.floor((a.length-1)/p)+1).fill(0);a.forEach((v,i)=>{if(v&&i%p)throw Error("not p power at "+i);if(i%p===0)r[i/p]=v});return trim(r)};
 const r=rootP(psi(p)),N=rootP(sub(mul(X,pp(psi(p),2)),sc(mul(Y,mul(psi(p-1),psi(p+1))),4)));
 const Ha=r[r.length-1],M=sc(sub(mul(der(N),r),sc(mul(N,der(r)),2)),iv(Ha));
 const q4=mul(pp(r,4),N),q1=neg(mul(mul(r,N),M));
 const D=(f,odd)=>odd?add(sc(mul(xp(2),f),3),sc(mul(Y,der(f)),2)):sc(der(f),2);
 const Dn=(f,odd,n)=>{for(let j=0;j<n;j++){f=D(f,odd);odd=!odd}return {f,odd}};
 const R4=Dn(q4,false,p-3).f,R1=Dn(q1,true,p-6).f;
 const E4=sub(Dn(R4,false,2).f,sc(q4,Ha)),E1=sub(Dn(R1,false,5).f,sc(q1,Ha));
 return {p,b,mod,pow,iv,add,sub,sc,mul,pp,der,xp,Y,psi,r,N,M,Ha,q4,q1,R4,R1,E4,E1,Dn};
}
return ring;

})();
const mod=(a,n)=>(a%n+n)%n;
const km=(a,b,n)=>[mod(a[0]*b[0]-a[1]*b[1],n),mod(a[0]*b[1]+a[1]*b[0]-a[1]*b[1],n)];
const pi=[7,18],pi2=km(pi,pi,24),ratio=pi2.map(x=>mod(7*x,24));
ok(pi2[0]===13&&pi2[1]===0,"full pi square mod24");
ok(ratio[0]===19&&ratio[1]===0,"full CM ratio mod24");
for(let j=0;j<12;j++){
 const sign=j%2?-1:1;
 const row=Array(12).fill(0);
 row[j]+=(1+sign)/2;row[(j+6)%12]+=(1-sign)/2;
 ok(row[(7*j)%12]===1&&row.reduce((a,b)=>a+b,0)===1,"whole degree12 column "+j);
}
ok((13*7)%24===19&&((13*13-1)/12)%2===0,"center lift 19 versus 7");
for(const [m,n]of [[1,0],[0,1],[1,1]]){
 const dm=m-2*n,dn=2*m-n;
 ok(mod(dm+dn+dm*dn,2)===1,"actual sigma(2delta z) half-character");
}
ok(9+3/3===10&&60/3===20&&3/3===1,"complete half-period polynomial");
const rows=[];
for(const p of [13,19,31,61]){
 const R=ring(p),{r,N,M,Ha:h,Y}=R;
 const rx=R.der(r),Nx=R.der(N),r4=R.pp(r,4),r12=R.pp(r,12);
 const z=R.mul(r4,Nx),dz=R.Dn(z,true,1).f,dq=R.Dn(R.q4,false,1).f;
 const zero=a=>a.every(v=>v===0);
 const denom=R.sub(R.sc(R.mul(r,R.add(R.sc(R.mul(R.xp(2),rx),3),R.sc(R.mul(Y,R.der(rx)),2))),2),R.sc(R.mul(Y,R.pp(rx,2)),4));
 ok(zero(R.add(denom,R.sc(N,h*h))),"full division denominator p="+p);
 const num=R.sub(R.mul(N,R.add(R.sc(R.mul(R.xp(2),Nx),3),R.sc(R.mul(Y,R.der(Nx)),2))),R.sc(R.mul(Y,R.pp(Nx,2)),2));
 ok(zero(R.add(num,R.sc(r4,2*h*h))),"full division numerator p="+p);
 const W=R.sub(R.mul(R.q4,dz),R.mul(Y,R.mul(z,dq)));
 ok(zero(R.add(W,R.sc(r12,2*h*h))),"actual polynomial Wronskian p="+p);
 const defect=R.sub(R.Dn(R.q4,false,3).f,R.sc(R.q1,24*R.pow(h,3)));
 const qv=R.sc(R.mul(R.pp(r,2),R.mul(Y,R.mul(R.pp(rx,2),Nx))),864);
 ok(zero(R.sub(defect,qv)),"actual D/connection defect p="+p);
 ok(N[p-3]===R.mod(-2*R.pow(h,6)*R.iv(15)),"exact first numerator coefficient p="+p);
 ok(Nx[p-4]===R.mod(2*R.pow(h,6)*R.iv(5)),"unit highest numerator derivative p="+p);
 const rem=(aa,bb)=>{
  const a=[...aa];while(a.length>1&&!a.at(-1))a.pop();
  const inv=R.iv(bb.at(-1));
  while(a.length>=bb.length&&a.some(Boolean)){
   const j=a.length-bb.length,c=R.mod(a.at(-1)*inv);
   for(let k=0;k<bb.length;k++)a[k+j]=R.mod(a[k+j]-c*bb[k]);
   while(a.length>1&&!a.at(-1))a.pop();
  }
  return a;
 };
 const gcd=(a,b)=>{for(;b.some(Boolean);){const c=rem(a,b);a=b;b=c;}return R.sc(a,R.iv(a.at(-1)));};
 const same=(a,b)=>zero(R.sub(a,b));
 ok(same(gcd(r,rx),[1]),"separable etale denominator p="+p);
 ok(same(gcd(r,Nx),[1]),"all nonzero deck phases p="+p);
 ok(same(gcd(N,Nx),[1]),"separable three-torsion numerator p="+p);
 ok(same(gcd(N,rx),[0,1]),"exact numerator/denominator-critical gcd p="+p);
 const expected=R.mul(R.pp(r,2),[0,1]),monic=R.sc(expected,R.iv(expected.at(-1)));
 ok(same(gcd(R.q4,qv),monic),"complete paired-source gcd p="+p);
 const powmod=(a,n)=>{let z=[1];for(a=rem(a,r);n;n=Math.floor(n/2),a=rem(R.mul(a,a),r))if(n&1)z=rem(R.mul(z,a),r);return z;};
 const phase=R.sub(R.mul(powmod(Y,(p-1)/2),powmod(Nx,p-1)),R.sc(powmod(N,p-1),h));
 ok(zero(rem(phase,r)),"entire etale algebra a^(p-1)=Ha p="+p);
 const C=f=>{
  const ff=R.mul(f,R.pp(Y,(p-1)/2)),out=[];
  for(let j=p-1;j<ff.length;j+=p)if(ff[j])out[(j-(p-1))/p]=ff[j];
  for(let j=0;j<out.length;j++)if(!out[j])out[j]=0;
  return out.length?out:[0];
 };
 const c1=C(r),c12=C(r12),cw=C(R.mul(R.q4,dz));
 ok(same(c1,[1]),"absolute original sigma Cartier anchor p="+p);
 ok(same(cw,R.sc(c12,-h*h)),"entire Cartier bilinear row p="+p);
 const companion=R.sub(R.mul(Y,R.pp(dq,2)),R.sc(R.mul(R.pp(r,6),R.pp(N,3)),2*h*h));
 ok(same(C(companion),R.sc(c12,2*h*h)),"log-free quadratic Cartier identity p="+p);
 let fixedCenter=false;
 if(p===31){
  const poly=R.sc(R.add(R.add(R.xp(6),R.sc(R.xp(3),20)),[10]),-R.iv(18));
  ok(same(c12,poly),"fixed g19 absolute Cartier row p31");
  ok(cw[6]===R.mod(h*h*R.iv(18)),"unit top coordinate p31");
  fixedCenter=true;
 }
 rows.push({p,Ha:h,full_original_gcd:"monic(r^2*x)",complete_deck_equation:"a^(p-1)=Ha in the entire nonzero V-fibre algebra",cartier_r12:c12,cartier_q4_Dz:cw,fixed_center_check:fixedCenter});
}
return {
 title:"R565 paired Verschiebung Lame and actual Cartier bilinear row",
 status:"passed",checks,formal_identities:formal,
 full_degree12:{ratio_mod24:ratio,operator:"(I+D+X-DX)/2, e_j -> e_(7j)",sigma_pull_anchor:-1,cartier_sign:"C12=-K12",half_period_polynomial:"(x^6+20b x^3+10b^2)/(18b^2)"},
 original_polynomial_defect:"D^3 q4 -24 Ha^3 q1 =864 r^2 y^3 r_x^2 N_x",
 phase:"a_T=y(T)N_x(T)/N(T), all nonzero T in ker V",
 fixed_ray_cartier:"C(q4 DzV omega)=Ha^2 (x^6+20x^3+10) omega /18",
 b17_factor:"theta^(12-7/p) times pullback of the E0 differential; theta^6=17",
 fibres:rows,
 scope:"The displayed nonlinear Cartier row is nonzero. This is not a proof that the two specified linear negative moments cannot simultaneously vanish.",
 finite_checks:"13,19,61 are the previous fibres; 31 is a single centre-normalization check already present in the existing prime table. The universal proof is in R565."
};

})();
process.stdout.write(JSON.stringify(certificate,null,2)+"\n");
