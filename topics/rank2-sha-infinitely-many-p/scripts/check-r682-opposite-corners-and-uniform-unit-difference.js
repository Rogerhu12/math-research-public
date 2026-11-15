"use strict";
const ck=(x,m)=>{if(!x)throw Error(m);};
const abs=x=>x<0n?-x:x,gcd=(x,y)=>{x=abs(x);y=abs(y);while(y)[x,y]=[y,x%y];return x;};
const Q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);ck(d!==0n,"zero denominator");if(d<0n){n=-n;d=-d;}let g=gcd(n,d);return[n/g,d/g];};
const qa=(x,y)=>Q(x[0]*y[1]+y[0]*x[1],x[1]*y[1]),qn=x=>[-x[0],x[1]],
qm=(x,y)=>Q(x[0]*y[0],x[1]*y[1]),qi=x=>Q(x[1],x[0]),
qs=x=>x[1]===1n?String(x[0]):String(x[0])+"/"+x[1];
const E=(a,b=0,d=1)=>[Q(a,d),Q(b,d)], ea=(x,y)=>[qa(x[0],y[0]),qa(x[1],y[1])],
en=x=>[qn(x[0]),qn(x[1])],es=(x,y)=>ea(x,en(y)),
em=(x,y)=>[qa(qm(x[0],y[0]),qn(qm(x[1],y[1]))),
qa(qa(qm(x[0],y[1]),qm(x[1],y[0])),qn(qm(x[1],y[1])))],
ec=x=>[qa(x[0],qn(x[1])),qn(x[1])],
eq=(x,y)=>x[0][0]===y[0][0]&&x[0][1]===y[0][1]&&x[1][0]===y[1][0]&&x[1][1]===y[1][1],
esc=(x,a,b=1)=>em(x,E(a,0,b)),ez=x=>eq(x,E(0)),
ei=x=>{let n=em(x,ec(x));ck(n[1][0]===0n,"norm rational");return[ qm(ec(x)[0],qi(n[0])),qm(ec(x)[1],qi(n[0])) ];},
out=x=>x.map(qs);
const he=(x,y)=>x.reduce((a,t,i)=>ea(a,em(t,ec(y[i]))),E(0));
const va=(x,y)=>x.map((t,i)=>ea(t,y[i])),vs=(x,y)=>x.map((t,i)=>es(t,y[i])),
vm=(x,c)=>x.map(t=>em(t,c));
const mm=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((s,t,k)=>ea(s,em(t,B[k][j])),E(0))));
const ident=n=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>E(i===j?1:0)));
function inverse(A){let M=A.map(row=>row.map(x=>x)),B=ident(A.length),det=E(1);
 for(let k=0;k<M.length;k++){let p=k;while(p<M.length&&ez(M[p][k]))p++;ck(p<M.length,"singular");
  if(p!==k){[M[p],M[k]]=[M[k],M[p]];[B[p],B[k]]=[B[k],B[p]];det=en(det);}
  const pivot=M[k][k];det=em(det,pivot);const inv=ei(pivot);M[k]=vm(M[k],inv);B[k]=vm(B[k],inv);
  for(let i=0;i<M.length;i++)if(i!==k&&!ez(M[i][k])){const f=M[i][k];M[i]=vs(M[i],vm(M[k],f));B[i]=vs(B[i],vm(B[k],f));}
 } return {inverse:B,det}; }




function compute(){
 let checks=0;const check=(x,m)=>{ck(x,m);checks++;};
 const ell=E(0,-3,5),bf=E(5,6,5),bq=E(11,6,5),by=E(20,3,17),bl=E(2,12,5);
 const c=em(es(bq,by),ei(by)),h=em(bl,ei(by)),d=em(es(E(1),by),ei(by));
 const ca=ea(em(c,em(ell,ell)),esc(em(h,em(ell,bf)),2));
 const cb=en(ea(esc(em(c,em(ell,bf)),2),em(h,em(bf,bf))));
 check(eq(ca,E(16623,110820,43625)),"C_a exact");
 check(eq(ca,E(3*1847*3,3*1847*20,125*349)),"C_a fixed factor");
 check(eq(cb,E(54796,55860,43625)),"C_b exact");
 const nca=em(ca,ec(ca));
 check(eq(nca,E(9*1847*1847,0,15625*349)),"C_a norm");
 const prime=n=>{for(let j=2;j*j<=n;j++)if(n%j===0)return false;return n>1;};
 check(prime(1847),"1847 prime");check(prime(349),"349 prime");
 check(1847%64===55&&349%64===29,"old ray excludes both C_a primes");
 // Complete enumeration below degree four in the opposite relative logarithm.
 const surviving=[],rejected=[];
 for(let j=0;j<=3;j++)for(let aq=0;aq<=j;aq++)for(let qq=0;qq<=j-aq;qq++){
 const lq=j-aq-qq;
 for(let order=1;order<=3;order++)for(let na=0;na<=order;na++)for(let nq=0;nq<=order-na;nq++){
 const nc=order-na-nq;
 for(let den=0;den<=3;den++){
 const xp=j+aq+order+na+den;if(xp>3)continue;
 const aLog=na+den,firstDegree=6-j+aq+aLog;
 const item={carry_derivative:j,A_in_carry:aq,Q_in_carry:qq,L_in_carry:lq,log_power:order,A_quadratic_numerator:na,Q_over_L:nq,constant_numerator:nc,denominator_A_power:den,x_power:xp,first_four_degree:firstDegree};
 if(firstDegree%6===4){surviving.push(item);check(xp===3&&j===2&&aq===0&&order===1&&aLog===0,"all low survivors exactly P2 times linear log");}
 else rejected.push(item);
 }
 }
 }
 check(surviving.length===6,"six actual cubic monomials");
 // Bivariate Q(omega) polynomials in a,z for the complete surviving pair contraction.
 const mono=(a,z,k)=>{const p=new Map();if(!ez(k))p.set(a+","+z,k);return p;};
 const add=(p,q)=>{const r=new Map(p);for(const[k,c]of q){const t=ea(r.get(k)||E(0),c);if(ez(t))r.delete(k);else r.set(k,t);}return r;};
 const mul=(p,q)=>{let r=new Map();for(const[k,u]of p)for(const[l,v]of q){const a=k.split(",").map(Number),b=l.split(",").map(Number);r=add(r,mono(a[0]+b[0],a[1]+b[1],em(u,v)));}return r;};
 const sc=(p,k)=>new Map([...p].map(([a,c])=>[a,em(c,k)]).filter(([,c])=>!ez(c)));
 const eqp=(p,q)=>add(p,sc(q,E(-1))).size===0;
 const s=mono(0,1,en(ell)),t=mono(1,0,bf);
 const carry=[mul(t,t),sc(mul(s,t),E(2)),mul(s,s)]; // Q exponent 0,1,2
 const log0=mono(1,0,c),log1=mono(0,1,en(h));
 const actual={M20:new Map(),M11:new Map(),R31:new Map()};
 for(let q=0;q<3;q++)for(let extra=0;extra<=1;extra++){
 const power=q+extra,p=mul(carry[q],extra?log1:log0);
 if(power===0)actual.M20=add(actual.M20,sc(p,E(-1)));
 if(power===1)actual.M11=add(actual.M11,p);
 if(power===2)actual.M20=add(actual.M20,p);
 if(power===3)actual.R31=add(actual.R31,p);
 }
 const expected={
 M20:add(mono(1,2,ca),mono(3,0,en(em(c,em(bf,bf))))),
 M11:mono(2,1,cb),
 R31:mono(0,3,en(em(h,em(ell,ell))))
 };
 for(const k of Object.keys(expected))check(eqp(actual[k],expected[k]),"full cubic pair coefficient "+k);
 // Integer-polynomial checks for alternating interpolation moments.
 const trim=p=>{p=p.slice();while(p.length&&p.at(-1)===0n)p.pop();return p;};
 const pa=(p,q)=>trim(Array.from({length:Math.max(p.length,q.length)},(_,i)=>(p[i]||0n)+(q[i]||0n)));
 const pn=p=>p.map(t=>-t);
 const pm=(p,q)=>{let r=Array(Math.max(0,p.length+q.length-1)).fill(0n);for(let i=0;i<p.length;i++)for(let j=0;j<q.length;j++)r[i+j]+=p[i]*q[j];return trim(r);};
 const ps=(p,n)=>Array(n).fill(0n).concat(p);
 const peq=(p,q)=>{p=trim(p);q=trim(q);return p.length===q.length&&p.every((x,i)=>x===q[i]);};
 const den=pm(pm([1n,-1n],[1n,0n,-1n]),[1n,0n,0n,-1n]);
 const nums=[[0n,0n,0n,1n],[0n,-1n,-1n,-1n],[1n,1n,1n],[-1n]];
 const altern=[];
 for(let s0=0;s0<=2;s0++){
 const sum=nums.reduce((r,p,j)=>pa(r,ps(j%2?pn(p):p,s0*j)),[]);
 const desired=s0===0?pm([2n,2n],[1n,0n,1n]):s0===1?ps(pm([2n,2n],[1n,1n]),2):ps(pm([2n,2n],[1n,0n,1n]),3);
 check(peq(sum,desired),"A(-kappa^s) "+s0);altern.push(sum);
 }
 check(peq(pm(pm([1n,0n,0n,-1n],altern[0]),pm([1n,-1n],[1n,-1n])),pm([2n,0n,2n],den)),"exact negative-one cancellation U");
 // The displayed positive-moment simplifications keep their full Euler factors.
 // Cross multiplication of (1-k^2) A(-k)=2 k^2(1+k)^2/((1-k)(1-k^3)).
 check(peq(pm(pm([1n,0n,-1n],altern[1]),pm([1n,-1n],[1n,0n,0n,-1n])),pm(ps([2n,4n,2n],2),den)),"first full Euler coefficient");
 check(peq(pm(pm([1n,-1n],altern[2]),pm([1n,-1n],[1n,0n,0n,-1n])),pm(ps([2n,0n,2n],3),den)),"second full Euler coefficient");
 const ser=p=>[...p].sort(([a],[b])=>a.localeCompare(b)).map(([k,c])=>({a_z:k.split(",").map(Number),coefficient:out(c)}));
 return{
 format:"R682 exact opposite-corner comparison",field:"Q(omega)",
 constants:{ell_0:out(ell),b_F:out(bf),c:out(c),h:out(h),d:out(d),C_a:out(ca),C_b:out(cb),norm_C_a:out(nca)},
 low_order_survivors:surviving,rejected_low_order_count:rejected.length,
 cubic_pair_coefficients:Object.fromEntries(Object.entries(actual).map(([k,p])=>[k,ser(p)])),
 pair_moments:{
 M20:"4 Omega^2(1-beta)(1-beta*kappa^2)",
 M02:"-M20",
 M11:"3 Omega^2(1-beta*kappa)^2",
 R31:"36 b Omega^3(1-beta*kappa^3) I_(Sigma_5,-1)"
 },
 alternating_numerators:altern.map(p=>p.map(String)),interpolation_denominator:den.map(String),
 exact_cancellation:"sigma_M=(-1)^(M+1)(1+kappa^2)/(1-kappa)^2",
 bounded_actual_row:"D= kappa^(3M+3) B_opposite - sigma_M B_first",
 complete_cubic_numerator:"4 C_a(1+kappa)^2(1-beta)(1-beta*kappa^2)+3 C_b kappa^(M+1)(1+kappa^2)(1-beta*kappa)^2",
 prefactor:"(-1)^M lambda^N kappa^(3r+4M+5-2N)/(b(1-kappa)(1-kappa^3))",
 opposite_analytic_scaling:"x=kappa^(N+M+3) X",
 opposite_tail:"p^(4r-4N-4M-12) O",
 combined_tail:"p^(4r-4N-M-9) O",
 sufficient_depth:"r even, r>2N+5M+14, N positive divisible by 4, M>=2",
 exact_valuation:"3r+4M+5-2N",
 opposite_full_arithmetic_coefficient:"c1=(-1)^(M+1)lambda^(-2r)beta^(N-r)(1-beta^(-1))A_kappa(-1)",
 whole_return_coefficient:"cD=kappa^(3M+3)c1-sigma_M*c0, a unit",
 remaining:"All true S/T complementary domains and q0/q1 observation differences remain. The exact cubic cancellation does not assert cancellation of the entire integrals.",
 exact_checks:checks};
}


if(typeof module!=="undefined")module.exports={compute};
if(typeof require!=="undefined"&&require.main===module){
 const fs=require("fs"),out=JSON.stringify(compute(),null,2)+"\n";
 if(process.argv[2])fs.writeFileSync(process.argv[2],out);else process.stdout.write(out);
}
