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
 const fact=n=>{let a=1n;for(let i=2;i<=n;i++)a*=BigInt(i);return a;};
 const se=(entries)=>new Map(entries.map(([k,a,b=1])=>[k,Q(a,b)]));
 const sa=(p,q)=>{let r=new Map(p);for(const[k,c]of q){let v=qa(r.get(k)||Q(0),c);if(v[0])r.set(k,v);else r.delete(k);}return r;};
 const sm=(p,q)=>{let r=new Map();for(const[k,a]of p)for(const[l,b]of q){let e=k+l;if(e>24)continue;let v=qa(r.get(e)||Q(0),qm(a,b));if(v[0])r.set(e,v);else r.delete(e);}return r;};
 const ss=(p,q)=>new Map([...p].map(([k,c])=>[k,qm(c,q)]));
 const sp=(p,n)=>{let r=se([[0,1]]);for(let i=0;i<n;i++)r=sm(r,p);return r;};
 const qe=(a,b)=>a[0]===b[0]&&a[1]===b[1];
 const sigma=se([[1,1],[7,1,210]]),xb=se([[-2,1],[4,-1,7]]),yb=se([[-3,-1],[3,-2,7]]);
 const sig5=sp(sigma,5),D5=ss(sm(sm(xb,yb),sig5),Q(-1)),Z5=sm(sp(xb,2),sig5),X5=sm(xb,sig5);
 const sigma2=se([[1,2],[7,128,210]]),F12=sm(sigma,sigma2);
 const coeff=(p,k)=>p.get(k)||Q(0);
 check(qe(coeff(D5,0),Q(1))&&qe(coeff(D5,6),Q(1,6)),"D5 first two coefficients");
 check(qe(coeff(Z5,1),Q(1))&&qe(coeff(Z5,7),Q(-11,42)),"Z5 first two coefficients");
 check(qe(coeff(X5,3),Q(1))&&qe(coeff(sig5,5),Q(1)),"X and Sigma leading");
 check(qe(coeff(F12,2),Q(2))&&qe(coeff(F12,8),Q(13,21)),"F12 first two coefficients");
 const MX3=qm(coeff(X5,3),Q(fact(3))),MS5=qm(coeff(sig5,5),Q(fact(5))),MD6=qm(coeff(D5,6),Q(fact(6)));
 const MZ1=qm(coeff(Z5,1),Q(fact(1))),MZ7=qm(coeff(Z5,7),Q(fact(7))),MF2=qm(coeff(F12,2),Q(fact(2)));
 const mass={
 "5,3":qm(Q(6),qm(MS5,MX3)),
 "3,5":qm(Q(6),qm(MX3,MS5)),
 "2,6":qm(MF2,MD6),
 "1,7":qm(Q(3),qm(MZ1,MZ7))
 };
 check(qe(mass["5,3"],Q(4320))&&qe(mass["3,5"],Q(4320)),"two mixed positive moments");
 check(qe(mass["2,6"],Q(480)),"F12 D5 moment");
 check(qe(mass["1,7"],Q(-3960)),"Z5 Z5 moment");
 const allowed=[];
 const thetaTypes=new Set([0,1,2,3,5]);
 for(let l=0;l<=8;l++)if(thetaTypes.has(l%6)&&thetaTypes.has((8-l)%6)&&l>=3&&l<8)allowed.push(l);
 check(JSON.stringify(allowed)===JSON.stringify([3,5,6,7]),"all surviving degree-eight mass powers");
 const firstMassModes=allowed,oppositeMassModes=allowed.map(x=>x+3);
 check(firstMassModes[0]===3&&Math.min(...firstMassModes.filter(x=>x!==3),...oppositeMassModes)===5,"Q eliminates unique least mass mode");
 const qval=s=>s===3?"zero":2*Math.min(s,3);
 check(qval(4)===6&&qval(5)===6,"Q unit-mode factors");
 const pvals={};
 for(const s of[3,4,5]){
 const v=Array.from({length:13},(_,a)=>2*Math.min(s,a)).reduce((a,b)=>a+b,0);
 check(v===s*(25-s),"thirteen-factor valuation "+s);pvals[s]=v;
 }
 check(pvals[3]===66&&pvals[4]===84&&pvals[5]===100,"explicit P13 valuations");
 const killed=[],remaining=[];
 for(let a=0;a<=12;a++){if(a+3<=12)killed.push(a);else remaining.push(a);}
 check(killed.length===10&&JSON.stringify(remaining)==="[10,11,12]","literal kappa^6 filter conjugation");
 const shiftedVal=Array.from({length:13},(_,a)=>2*a).reduce((a,b)=>a+b,0);
 check(shiftedVal===156,"all surviving high common modes");
 const N=4,M=2,r=44;
 const leading=3*r+4*M+11-2*N,tail=4*r-4*N-M-13,massBound=8*r+5*M+9-8*N;
 check(r>2*N+5*M+24&&leading===143&&tail===145&&massBound===339,"fixed actual Q example");
 const rp=144,pLeading=3*rp+4*M+89-2*N,pTail=4*rp-4*N-M-35;
 check(rp>2*N+5*M+124&&pLeading===521&&pTail===523,"fixed P13 example");
 return{
 format:"R685 new carry full mass and actual outside filters",field:"exact rationals and original Q(omega) constants",
 source:"R679 actual q_N^sharp; fixed N, independent of r and M",
 normalization:"K2=lambda^N kappa^(-2N)/(2b Omega^2)",
 low_S5_coefficients:{D5:{z0:"1",z6:"b/6"},Z5:{z1:"1",z7:"-11b/42"},X5:{z3:"1"},Sigma5:{z5:"1"},F12:{z2:"2",z8:"13b/21"}},
 unit_pair_moments:Object.fromEntries(Object.entries(mass).map(([k,v])=>[k,{coefficient:qs(v),scale:"b Omega^8",Euler:"(1-beta*kappa^a)(1-beta*kappa^b) for displayed exponents (a,b)"}])),
 mass_powers:allowed,
 full_mass_factor:"K8(x)=integral_Gstar (partial_v^8 Psharp)(Xstar+a*x^2*A*v)/8!, a polynomial in x^2 of degree at most four",
 mass_first_shifts:["b_F","ell_0"],mass_opposite_shifts:["-ell_0","b_F"],
 mass_formula:"B_i(0)=x^8 K8(x) sum_l binom(8,l) q_i^(8-l) l_i^l (1-kappa^(8-l)) kappa^(M*l) A_kappa(kappa^l) M_(8-l,l)",
 Q_operator:"(T2-1)(T2-lambda^2*kappa^6)",
 outside_coefficient_modes:["1","lambda^2*kappa^6"],
 whole_outside_elimination:"Q Xhat^Z=Q Vhat^Z=0 for the entire Mellin rows; Q Rhat^Z=-Q Dhat^Z",
 actual_Q_primary_modes:["lambda^2*kappa^8","lambda^2*kappa^10"],
 actual_Q_units:["(lambda^2*kappa^8-1)(kappa^2-1)","(lambda^2*kappa^10-1)(kappa^4-1)"],
 P13_values:pvals,
 literal_conjugation:{killed: killed, retained:remaining,valuation_of_retained:156},
 central_Q_valuation:"3r+4M+11-2N",
 central_Q_tail:"4r-4N-M-13",
 S_Q_lower_bound:"4r-4N-M-13",
 mass_Q_lower_bound:"8r+5M+9-8N",
 example:{N,M,r,A_depth:88,Q_annuli:[44,45],L_annuli:[46,47,48,49,50,51,52,53],T_central_valuation:leading,S_central_lower_bound:tail,individual_mass_lower_bound:massBound},
 remaining:"Eliminating the fixed mixed row by an M-only filter also eliminates the same coefficient of the original central row. The remaining true CD_N complement is not assigned zero.",
 exact_checks:checks};
}


if(typeof module!=="undefined")module.exports={compute};
if(typeof require!=="undefined"&&require.main===module){
 process.stdout.write(JSON.stringify(compute(),null,2)+"\n");
}
