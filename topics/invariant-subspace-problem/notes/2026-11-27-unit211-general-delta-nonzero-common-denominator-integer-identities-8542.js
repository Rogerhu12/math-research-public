const start=Date.now();
const N=5;
function c(x){x=BigInt(x);return x?new Map([["0,0,0,0,0",x]]):new Map();}
function variable(i){let a=Array(N).fill(0);a[i]=1;return new Map([[a.join(","),1n]]);}
function add(...ps){let out=new Map();for(let p of ps)for(let[k,v]of p){let x=(out.get(k)||0n)+v;if(x)out.set(k,x);else out.delete(k);}return out;}
function neg(p){return new Map([...p].map(([k,v])=>[k,-v]));}
function sub(a,b){return add(a,neg(b));}
function mul(...ps){let out=c(1);for(let p of ps){let r=new Map();for(let[k,a]of out){let m=k.split(",").map(Number);for(let[l,b]of p){let n=l.split(",").map(Number),key=m.map((v,i)=>v+n[i]).join(",");let v=(r.get(key)||0n)+a*b;if(v)r.set(key,v);else r.delete(key);}}out=r;}return out;}
function pow(p,n){let r=c(1);while(n){if(n%2)r=mul(r,p);n=Math.floor(n/2);if(n)p=mul(p,p);}return r;}
function scale(n,p){return mul(c(n),p);}
function exactIntDivide(p,n){n=BigInt(n);let r=new Map();for(let[k,v]of p){if(v%n)throw Error("nonexact coefficient division");r.set(k,v/n);}return r;}
function check(name,p){if(p.size)throw Error(name+" is not zero; terms "+p.size);checks.push(name);}
function coeffT(p,n){let r=new Map();for(let[k,v]of p){let a=k.split(",").map(Number);if(a[4]===n){a[4]=0;r.set(a.join(","),v);}}return r;}
function profile(p){let deg=Array(N).fill(-1),total=-1;for(let[k]of p){let a=k.split(",").map(Number);a.forEach((v,i)=>{deg[i]=Math.max(deg[i],v);});total=Math.max(total,a.reduce((s,x)=>s+x,0));}return{degrees_u_Q_ell_lambda_T:deg,totalDegree:total,terms:p.size};}
function canonical(p){return [...p].sort((a,b)=>a[0].localeCompare(b[0])).map(([k,v])=>[k,String(v)]);}
const [u,Q,l,L,T]=Array.from({length:N},(_,i)=>variable(i)),one=c(1),checks=[];
const d=sub(one,Q),m=sub(u,l),V2=sub(scale(2,u),mul(l,Q));
const M=sub(mul(l,V2),pow(u,2)),T0=sub(V2,scale(2,pow(u,2)));
const J=add(scale(2,u),scale(-2,pow(u,2)),mul(l,Q));
const Phi=add(T0,scale(4,u),c(-4),Q);
const P02=add(mul(sub(c(2),scale(3,u)),V2),neg(mul(Q,u)),scale(2,pow(u,3)));
const Pf=mul(T0,sub(J,Q));
const A=add(scale(2,pow(L,2)),scale(-2,L),one);
const B=add(scale(4,pow(L,3)),scale(-6,pow(L,2)),scale(3,L),c(-1));
const D=sub(mul(l,A),pow(T,2));
const sn=sub(mul(l,B),mul(A,T)),zn=sub(mul(T,B),pow(A,2));
const K=add(mul(pow(l,2),B),scale(-3,mul(l,T,A)),scale(2,pow(T,3)));
const Z=sub(mul(u,sn),scale(2,mul(T,D)));
const S=add(sn,mul(sub(c(3),scale(2,L)),D));
const G=sub(mul(L,P02),mul(sub(one,u),T0)),w=sub(sub(L,one),T);
const Pc=sub(mul(Q,P02,add(l,T)),mul(G,T0));
const W=exactIntDivide(sub(mul(Phi,sub(J,scale(2,mul(u,Q)))),Pf),2);
const F6=sub(mul(M,pow(K,2)),scale(4,mul(pow(m,2),pow(D,3))));
check("F6_T_leading_paid_identity",sub(coeffT(F6,6),scale(4,mul(pow(l,2),d))));
check("center_v0_rational_identity",sub(add(K,scale(2,mul(T,D))),mul(l,sn)));
check("center_zeta_rational_identity",sub(mul(l,Z),add(scale(2,mul(m,T,D)),mul(u,K))));
check("v1_equals_v0_minus_zeta",add(sub(mul(m,sn),Z),K));
const core=add(mul(sub(c(3),scale(4,L)),Q,pow(D,2)),neg(mul(J,zn,D)),mul(u,Q,S,sn));
const E=add(mul(m,Phi,core),mul(W,S,Z));
const NF4=add(scale(4,mul(m,add(mul(sub(c(3),scale(4,L)),Q,pow(D,2)),neg(mul(J,zn,D))))),scale(2,mul(S,add(scale(-2,mul(u,Q,K)),mul(J,Z)))));
const NC4=add(scale(4,mul(m,G,zn,D)),scale(-2,mul(G,S,Z)),neg(mul(Q,T0,S,K)),scale(4,mul(m,Q,w,u,sub(c(3),scale(2,L)),pow(D,2))),scale(2,mul(m,Q,w,u,sn,D)),scale(-2,mul(Q,w,sub(u,mul(l,Q)),K,D)));
check("exact_original_two_line_determinant_numerator",sub(sub(mul(Phi,NF4),scale(2,mul(S,Z,Pf))),scale(4,E)));
const Fnum=sub(scale(2,mul(S,Z,Pc)),mul(Phi,NC4));
const Tnum=sub(mul(Pf,NC4),mul(Pc,NF4));
check("complete_original_P1_reconstruction",add(mul(Pf,Fnum),mul(Phi,Tnum),scale(4,mul(E,Pc))));
check("complete_second_original_line_reconstruction",add(mul(NF4,Fnum),scale(2,mul(S,Z,Tnum)),scale(4,mul(E,NC4))));
const all={F6,D,K,Z,S,E,NF4,NC4,Fnum,Tnum};
return{schema:"isp-general-delta-nonzero-five-parameter-exact-integer-identities-v1",variables:["u","Q","ell","lambda","T"],arithmetic:"exact BigInt integer sparse polynomials",checks,profiles:Object.fromEntries(Object.entries(all).map(([k,v])=>[k,profile(v)])),canonicalPolynomials:Object.fromEntries(Object.entries(all).map(([k,v])=>[k,canonical(v)])),newLeadingInverted:false,PhiInverted:false,physicalChart:"original two-line determinant nonzero, original D and ell-u nonzero",ordinaryISPClaim:false,elapsedMilliseconds:Date.now()-start};