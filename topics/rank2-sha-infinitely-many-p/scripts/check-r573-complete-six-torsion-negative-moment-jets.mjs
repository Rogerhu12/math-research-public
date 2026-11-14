// R573: exact original division and full E[6] jet certificate.
// Run: node check-r573-complete-six-torsion-negative-moment-jets.mjs
// No prime scan or target nonvanishing claim is made.
const data=(()=>{
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
let count=0;const check=(ok,label)=>{count++;if(!ok)throw Error(label)};
const trim=a=>{while(a.length>1&&!a.at(-1))a.pop();return a};
const eq=(R,a,b)=>R.sub(a,b).every(x=>!x);
function divrem(R,a,b){
 let r=a.slice(),q=Array(Math.max(1,a.length-b.length+1)).fill(0),bi=R.iv(b.at(-1));
 while(r.length>=b.length&&r.some(Boolean)){const k=r.length-b.length,c=R.mod(r.at(-1)*bi);q[k]=c;
 for(let j=0;j<b.length;j++)r[k+j]=R.mod(r[k+j]-c*b[j]);trim(r);}
 return {q:trim(q),r:trim(r)};
}
function quotient(R,M){
 const red=a=>divrem(R,a,M).r,mul=(a,b)=>red(R.mul(a,b)),add=(a,b)=>red(R.add(a,b)),
 sub=(a,b)=>red(R.sub(a,b)),sc=(a,c)=>red(R.sc(a,c));
 function inv(a){
  let r0=M,r1=red(a),t0=[0],t1=[1];
  while(r1.some(Boolean)){const d=divrem(R,r0,r1);[r0,r1]=[r1,d.r];[t0,t1]=[t1,R.sub(t0,R.mul(d.q,t1))];}
  if(r0.length!==1)throw Error("nonunit in full E6 quotient");
  return sc(t0,R.iv(r0[0]));
 }
 const pp=(a,n)=>{let v=[1];for(;n;n=Math.floor(n/2),a=mul(a,a))if(n&1)v=mul(v,a);return v};
 const compose=(a,v)=>a.reduceRight((w,c)=>add(mul(w,v),[c]),[0]);
 return {red,mul,add,sub,sc,inv,pp,compose};
}
const evalp=(R,a,t)=>a.reduceRight((v,c)=>R.mod(v*t+c),0);
const extract=(R,f,shift=0)=>{check(f.every((c,j)=>!c||(j-shift)%3===0),"exact mu6 polynomial type");return trim(Array.from({length:Math.floor((f.length-1-shift)/3)+1},(_,j)=>f[3*j+shift]||0));};
function L3(R,P){
 return R.add(R.add(
 R.sc(R.mul([0,0,1,1],R.der(R.der(R.der(P)))),216),
 R.sc(R.mul([0,4,7],R.der(R.der(P))),108)),
 R.sc(R.mul([1,7],R.der(P)),48));
}
const fibres=[];
for(const p of[13,19,31,61]){
 const R=ring(p),Q4=[-512,-320,-1776,220,1].map(R.mod),
 Q5=R.mul([4,1],Q4),D7=R.mul([0,1,1],Q5),D12=R.mul([0,1,1],R.pp(Q5,2)),B=quotient(R,Q5);
 const r=extract(R,R.r),nn=extract(R,R.N,1),mm=extract(R,R.M),P4=extract(R,R.R4),P1=extract(R,R.R1),
 a4=P4[p]||0,a1=P1[p]||0;
 const psi6Expected=R.sc(R.mul(R.xp(1),Array.from({length:16},(_,j)=>j%3===0?(Q5[j/3]||0):0)),3);
 check(eq(R,R.psi(6),psi6Expected),"p"+p+" entire psi6/2y");
 const A=L3(R,P1);
 const actualD3=R.Dn(R.R1,false,3);
 check(actualD3.odd&&eq(R,actualD3.f,Array.from({length:3*(A.length-1)+1},(_,j)=>j%3===0?(A[j/3]||0):0)),"p"+p+" entire L3 operator");
 check(B.red(R.der(P4)).every(x=>!x),"p"+p+" DR4 all generic E6");
 check(B.red(R.add(A,R.sc(R.mul([1,1],R.der(A)),2))).every(x=>!x),"p"+p+" D4R1 all generic E6");
 check(evalp(R,A,-1)===0,"p"+p+" D4R1 all E2");
 check((A[0]||0)===R.mod(-6*a4),"p"+p+" cross jet at delta");
 check((P4[1]||0)===R.mod(R.Ha*R.Ha*R.iv(24)),"p"+p+" unconditional P4 first jet unit");
 check((P1[1]||0)===R.mod(-a4*R.iv(8)),"p"+p+" P1 first jet reads a4");
 check(R.mod(2*(P1[2]||0))===R.mod(3*a4*R.iv(32)-R.Ha*R.Ha*R.iv(11520)),"p"+p+" P1 second jet");
 const X=[0,1],Y=[1,1],g=B.sub(
 B.sc(B.mul([8,17],B.inv(Y)),-R.iv(72)),
 B.sc(B.mul(B.mul(X,R.der(R.der(Q5))),B.inv(R.der(Q5))),R.iv(12)));
 const rv6=B.pp(r,6),xv=B.mul(B.mul(X,B.pp(nn,3)),B.inv(rv6)),yvFactor=B.mul(mm,B.inv(B.pp(r,3))),
 gv=B.compose(g,xv),Yv=B.add(xv,[1]);
 const F11=B.sub(B.add(B.sc(xv,-5),[-2]),B.sc(B.mul(Yv,gv),6));
 const gv2=B.pp(gv,2),gv3=B.mul(gv2,gv),gv4=B.mul(gv3,gv);
 const F44=B.add(B.sub(B.add(B.sc(xv,-5),[-2]),B.sc(B.mul(Yv,gv),24)),
 B.mul(B.mul(B.pp(Yv,2),B.inv(xv)),B.add(B.sc(gv3,72),B.sc(gv4,54))));
 const F41=B.sub(B.sub(B.sub(B.sub(B.add(B.sc(xv,-18),[-6]),
 B.mul(B.add(B.sc(xv,108),[72]),gv)),
 B.sc(B.mul(Yv,gv2),216)),
 B.mul(B.mul(B.mul(B.add(B.sc(xv,180),[72]),Yv),B.inv(xv)),gv3)),
 B.sc(B.mul(B.mul(B.pp(Yv,2),B.inv(xv)),gv4),54));
 check(eq(R,B.red(P4),B.sc(B.mul(rv6,F44),a4)),"p"+p+" full translated f4 values with actual r6 phase");
 check(eq(R,B.red(P1),B.sc(B.mul(rv6,F11),a1)),"p"+p+" full translated f1 values with actual r6 phase");
 check(eq(R,B.red(A),B.sc(B.mul(B.mul(rv6,yvFactor),F41),a4)),"p"+p+" full cross jet with actual r6 phase");
 const d4quot=divrem(R,R.der(P4),Q5);
 check(d4quot.r.every(x=>!x),"p"+p+" actual derivative divisor");
 const conditional=[];
 if(a4===0){
  const q4=divrem(R,P4,D12),qA=divrem(R,A,D12);
  check(q4.r.every(x=>!x)&&qA.r.every(x=>!x),"p"+p+" both full degree78 factors");
  conditional.push("a4=0: both degree78 factors verified");
 }
 if(a1===0){
  check(divrem(R,P1,D7).r.every(x=>!x),"p"+p+" full E6 factor for R1");
  conditional.push("a1=0: complete degree42 factor verified");
 }
 fibres.push({p,a4,a1,P4_first:P4[1]||0,P1_first:P1[1]||0,P1_second_derivative:R.mod(2*(P1[2]||0)),
 actual_r6_mod_Q5:rv6,derivative_quotient_degree:d4quot.q.length-1,conditional});
}
return {result:"all exact checks passed",checks:count,fibres,
 fixed_division_Q4:[-512,-320,-1776,220,1],
 fixed_factors:{D7:"X(X+b)(X+4b)Q4",D8:"X^2(X+b)(X+4b)Q4",D12:"X(X+b)(X+4b)^2 Q4^2"},
 condition_a4_zero_masses:["h^5/1080","h^2/216"],
 target_nonvanishing_proved:false,scope:"Full original fibres only at 13,19,31,61; all-prime assertions use the proof."};
})();
console.log(JSON.stringify(data,null,2));
