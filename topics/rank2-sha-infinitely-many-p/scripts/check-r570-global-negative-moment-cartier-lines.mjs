// R570. Exact fixed-fibre certificate, not a prime scan.
// Run: node check-r570-global-negative-moment-cartier-lines.mjs
// This reproduces the companion JSON. The all-prime proof is in R570.
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
const atg0=A=>new Map([...A].filter(([k])=>Number(k.split(",")[3])===0));
const target=scale(mul(add(scale(pow(x,3),5),scale(b,2)),pow(sig,6)),-1);
const d1=atg0(diff(f1)),d4=atg0(diff(diff(diff(diff(f4)))));
if(add(d1,scale(target,-1)).size)throw Error("f1 full torsion diagonal");
if(add(d4,scale(target,-24)).size)throw Error("f4 full torsion diagonal");
return {checks:2,diagonal:out(target),f4_factor:24,
 torsion_values:{delta:"-2b",two:"3b"},ring:"Z[b,x,y,g,sigma]/(y^2-x^3-b)",
 derivation:["Dx=2y","Dy=3x^2","Dg=-x","Dsigma=g sigma"]};
})();
const finite=(()=>{
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
let count=0;
const check=(ok,label)=>{count++;if(!ok)throw Error(label)};
const eq=(R,a,b)=>R.sub(a,b).every(x=>x===0);
const trim=a=>{while(a.length>1&&!a.at(-1))a.pop();return a};
function divrem(R,a,b){
 let r=a.slice(),q=Array(Math.max(1,a.length-b.length+1)).fill(0);
 const bi=R.iv(b.at(-1));
 while(r.length>=b.length && r.some(Boolean)){
  const k=r.length-b.length,c=R.mod(r.at(-1)*bi);q[k]=c;
  for(let j=0;j<b.length;j++)r[j+k]=R.mod(r[j+k]-c*b[j]);
  trim(r);
 }
 return {q:trim(q),r:trim(r)};
}
const evalp=(R,a,t)=>a.reduceRight((v,c)=>R.mod(v*t+c),0);
function rationalRow(R,P,label){
 const {p,b}=R,a=P[p]||0,B=P[0]||0,E=evalp(R,P,-b);
 check(B===R.mod(-2*b*a),label+" X=0");
 check(E===R.mod(3*b*a),label+" X=-b");
 const d0=divrem(R,R.sub(P,[B]),[0,1]);
 const d1=divrem(R,R.sub(P,[E]),[b,1]);
 check(d0.r.every(x=>!x)&&d1.r.every(x=>!x),label+" partial fractions exact");
 const S=R.sub(R.sc(d0.q,R.iv(3)),R.sc(d1.q,R.iv(2)));
 check(S.length<=p,label+" polynomial pole cap");
 check((S[p-1]||0)===R.mod(-a*R.iv(6)),label+" polynomial Cartier coefficient");
 const output=[S[p-1]||0,R.mod(B*R.iv(3)),R.mod(-E*R.iv(2))];
 check(eq(R,output,[R.mod(-a*R.iv(6)),R.mod(-2*b*a*R.iv(3)),R.mod(-3*b*a*R.iv(2))]),label+" entire Cartier line");
 const Hp=R.add(R.sub(R.xp(p),R.sc(R.xp(1),6)),[-2*b]);
 const Q=R.sub(P,R.sc(Hp,a));
 check(Q.length<=p,label+" highest Frobenius subtraction");
 const dq=divrem(R,Q,[0,b,1]);
 check(dq.r.every(x=>!x),label+" polynomial primitive divisor");
 const SQ=R.sc(R.mul([2*b,-1],dq.q),R.iv(6));
 check(SQ.length<=p-1,label+" no resonance in primitive");
 const F=[0,...SQ.map((c,j)=>R.mod(c*R.iv(j+1)))];
 check(eq(R,R.der(F),SQ),label+" displayed primitive derivative");
 const checkS=R.add(SQ,R.sc(R.sub(
   R.sc(divrem(R,R.sub(Hp,[-2*b]),[0,1]).q,R.iv(3)),
   R.sc(divrem(R,R.sub(Hp,[3*b]),[b,1]).q,R.iv(2))),a));
 check(eq(R,S,checkS),label+" full representative plus primitive");
 return {top:a,at_zero:B,at_minus_b:E,
   cartier_basis:["dX","dlog X","dlog(X+b)"],cartier:output,
   residue_O:R.mod(13*b*a),primitive_degree:trim(F).length-1,
   full_differential_exact:a===0};
}
const fibres=[];
for(const p of [13,19,31,61]){
 const R=ring(p),s=(p-1)/6;
 check(R.pow(R.r[0],6)===1,"p"+p+" delta torsion phase");
 check(eq(R,divrem(R,R.pp(R.r,6),R.Y).r,[1]),"p"+p+" entire E2 phase");
 const rows={};
 for(const name of ["R4","R1"]){
  const f=R[name];
  check(f.every((c,j)=>!c||j%3===0),"p"+p+" "+name+" exact mu6 type");
  const P=Array.from({length:Math.floor((f.length-1)/3)+1},(_,j)=>f[3*j]||0);
  check(P.length<=p+1,"p"+p+" "+name+" actual pole cap");
  const fyp=R.mul(f,R.pp(R.Y,(p-1)/2));
  check(fyp.every((c,j)=>!c||(j%p!==p-1)),"p"+p+" "+name+" canonical Cartier zero");
  rows[name]=rationalRow(R,P,"p"+p+" "+name);
 }
 fibres.push({p,b:1,hasse:R.Ha,degree_r:R.r.length-1,rows});
}
const R0=ring(31),Rb=ring(31,17),p=31,b=17,s=5;
const scalePoly=(poly,shift)=>poly.map((c,j)=>{
 if(!c)return 0;
 if((j-shift)%3)throw Error("bad homothety type");
 return Rb.mod(c*Rb.pow(b,((shift===0?s:2*s)-(j-shift)/3)%(p-1)+(p-1)));
});
const rb=scalePoly(R0.r,0),nb=scalePoly(R0.N,1);
const mb=Rb.sc(Rb.sub(Rb.mul(Rb.der(nb),rb),Rb.sc(Rb.mul(nb,Rb.der(rb)),2)),Rb.iv(R0.Ha));
const q4b=Rb.mul(Rb.pp(rb,4),nb),q1b=Rb.sc(Rb.mul(Rb.mul(rb,nb),mb),-1);
const scaleRows=[];
for(const [name,f,odd,n]of [["R4",q4b,false,p-3],["R1",q1b,true,p-6]]){
 const actual=Rb.Dn(f,odd,n).f;
 const predicted=R0[name].map((c,j)=>Rb.mod(c*Rb.pow(b,7*s-j/3)));
 check(eq(Rb,actual,predicted),"b17 "+name+" full transported V polynomial");
 const P=Array.from({length:p+1},(_,j)=>actual[3*j]||0);
 const expectedTop=Rb.mod((R0[name][3*p]||0)*Rb.pow(b,s-1));
 check((P[p]||0)===expectedTop,"b17 "+name+" highest scale");
 scaleRows.push({name,...rationalRow(Rb,P,"b17 "+name)});
}
return {result:"all exact checks passed",checks:count,
  scope:"Only existing fibres 13,19,31,61; not a prime scan or proof of nonvanishing",
  fibres,homothety:{p:31,b:17,base_hasse:R0.Ha,
    transported_V_hasse:R0.Ha,rows:scaleRows},
  cartier_line:"-(top)*(dX/6+2b*dlog(X)/3+3b*dlog(X+b)/2)",
  primitive:"P dlog(-x/y)=top*(X^p-6X-2b)dlog(-x/y)+dF, deg F<=p-1",
  nonvanishing_claim:false};
})();
const data={...finite,checks:finite.checks+formal.checks,formal};
console.log(JSON.stringify(data,null,2));
