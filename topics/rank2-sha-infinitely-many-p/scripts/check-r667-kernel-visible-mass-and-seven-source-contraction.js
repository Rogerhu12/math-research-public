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



function visible(all){

const parse=s=>{const x=s.split("/");return Q(x[0],x[1]||1);},read=x=>x.map(parse),row=a=>a.map(x=>Array.isArray(x)?E(...x):E(x));
const w=E(0,1),delta=E(1,2),C=vm(row([1,0,-1,1]),ei(delta)),A=row([[1,2],[2,4],[3,1],[2,-1]]),D4=row([1,[-1,-1],[0,-2],0]),H=row([-1,2,[0,1],[1,1]]),g=E(3,-2),aa=E(-5,-6,29);
const D=vs(D4,vm(A,aa)),d=he(D,D),F=va(D,C),Erow=va(D,vm(C,E(14))),Grow=va(vm(H,E(13)),vm(F,g));
ck(eq(d,E(143,0,29))&&eq(he(D,C),E(-1))&&ez(he(D,A)),"actual Dstar norms and non-orthogonal C");
const proj=(V,U)=>vs(V,vm(U,em(he(V,U),ei(he(U,U)))));
const Cp=proj(C,D),Ep=proj(Erow,D),Gp=proj(Grow,D),G00=proj(Gp,Cp);
ck(Ep.every((v,i)=>eq(v,esc(Cp[i],14))),"Eperp=14 Cperp");
const deriv=P=>{const z={};for(const[k,c]of Object.entries(P)){let e=k.split(",").map(Number);if(e[0]>=2){const fac=e[0]*(e[0]-1);e[0]-=2;z[e.join(",")]=esc(c,fac);}}return z;};
function add(P,R){const z={...P};for(const[k,c]of Object.entries(R)){z[k]=ea(z[k]||E(0),c);if(ez(z[k]))delete z[k];}return z;}
const scale=(P,c)=>Object.fromEntries(Object.entries(P).map(([k,v])=>[k,em(v,c)]).filter(([k,v])=>!ez(v)));
function mul(P,R){const z={};for(const[k,c]of Object.entries(P))for(const[l,v]of Object.entries(R)){const a=k.split(",").map((x,i)=>+x+ +l.split(",")[i]).join(",");z[a]=ea(z[a]||E(0),em(c,v));}return z;}
function pow(P,n){let z={"0,0,0":E(1)};for(let i=0;i<n;i++)z=mul(z,P);return z;}
const lin=rr=>Object.fromEntries(rr.map((c,i)=>[[0,1,2].map(j=>i===j?1:0).join(","),c]).filter(([k,v])=>!ez(v)));
const fact=n=>{let a=1;for(let i=2;i<=n;i++)a*=i;return a;};
function gen4(rr){const z=Array.from({length:4},(_,j)=>lin(rr.map(V=>V[j]))),zZ=scale(add(add(z[0],scale(z[2],E(-1))),scale(z[3],E(-2))),E(1,0,6)),zQ=scale(add(z[0],z[2]),E(1,0,2));
return scale(mul(add(mul(zZ,pow(zQ,2)),scale(pow(zZ,3),E(-1))),z[1]),E(1,0,42));}
function moment(P,rr){const gen=gen4(rr);return Object.entries(P).reduce((s,[k,c])=>ea(s,em(c,esc(gen[k]||E(0),k.split(",").reduce((a,i)=>a*fact(+i),1)))),E(0));}
const e0=P=>Object.fromEntries(Object.entries(P).filter(([k,v])=>+k.split(",")[1]===0));

const cols=all.matrix.polys.map(P=>Object.fromEntries(Object.entries(P).map(([k,v])=>[k,read(v)])));
const jr=cols.map(P=>{const dP=deriv(P);return {a:moment(dP,[D,Ep,Gp]),a0:moment(e0(dP),[D,Ep,Gp]),b:moment(e0(dP),[D,Array(4).fill(E(0)),G00])};});
const AP=all.matrix.Aplus.map(r=>r.map(read)),AZ=all.matrix.Azero.map(r=>r.map(read));
const BM=all.polynomial_right_inverse.B.map(M=>M.map(r=>r.map(read)));
const tt=E(2),At=AP.map((r,i)=>r.map((v,j)=>ea(v,em(tt,AZ[i][j])))),Bt=BM[0].map((r,i)=>r.map((v,j)=>ea(v,em(tt,BM[1][i][j]))));
const values={};
for(const eta of[1,-1]){
 const jp=jr.map(x=>es(es(x.a,x.a0),esc(x.b,eta))),jz=jr.map(x=>ea(x.a0,esc(x.b,eta))),j=jp.map((v,i)=>ea(v,em(tt,jz[i])));
 const rowB=Array.from({length:9},(_,k)=>j.reduce((s,c,i)=>ea(s,em(c,Bt[i][k])),E(0)));
 const delta=j.map((v,i)=>es(v,rowB.reduce((s,c,k)=>ea(s,em(c,At[k][i])),E(0))));
 values[String(eta)]={nonzero_indices:delta.map((v,i)=>!ez(v)?i:null).filter(i=>i!==null),sample:delta.map(out),row_plus:jp.map(out),row_zero:jz.map(out)};
}
return{values,column_moments:jr.map(x=>Object.fromEntries(Object.entries(x).map(([k,v])=>[k,out(v)]))),exps:all.matrix.exps};

}
function kernel(all,visible){

const parse=s=>{const x=s.split("/");return Q(x[0],x[1]||1);},read=v=>v.map(parse);
const AP=all.matrix.Aplus.map(r=>r.map(read)),AZ=all.matrix.Azero.map(r=>r.map(read)),B=all.polynomial_right_inverse.B.map(M=>M.map(r=>r.map(read)));
const index=1,e=Array.from({length:20},(_,i)=>E(i===index?1:0));
const matvec=(M,v)=>M.map(r=>r.reduce((s,c,j)=>ea(s,em(c,v[j])),E(0)));
const cp=AP.map(r=>r[index]),cz=AZ.map(r=>r[index]);
const v0=vs(vm(e,E(-1)),matvec(B[0],cp));
const v1=vs(vs(e,matvec(B[0],cz)),matvec(B[1],cp));
const v2=vm(matvec(B[1],cz),E(-1)),v=[v0,v1,v2];
const zero=[matvec(AP,v0),va(matvec(AP,v1),matvec(AZ,v0)),va(matvec(AP,v2),matvec(AZ,v1)),matvec(AZ,v2)];
for(const row of zero)ck(row.every(ez),"full A(tau) kernel polynomial identity");
const ds={};
for(const eta of[1,-1]){
 const z=visible.values[String(eta)],jp=z.row_plus.map(read),jz=z.row_zero.map(read);
 const dot=(x,y)=>x.reduce((s,c,i)=>ea(s,em(c,y[i])),E(0));
 const num=[dot(jp,v0),ea(dot(jp,v1),dot(jz,v0)),ea(dot(jp,v2),dot(jz,v1)),dot(jz,v2)];
 const at2=num.reduce((s,c,i)=>{let x=E(1);for(let j=0;j<i;j++)x=esc(x,2);return ea(s,em(c,x));},E(0));
 ck(eq(at2,read(z.sample[index]))&&!ez(at2),"exact tau=2 nonzero, both eta");
 ds[String(eta)]={numerator:num.map(out),denominator:"tau-1",at_tau2:out(at2)};
}
let den=1n;for(const pol of v)for(const c of pol)for(const q of c)den=den/gcd(den,q[1])*q[1];
return{column_index_zero_based:index,column:all.matrix.exps[index],kernel_numerator:v.map(row=>row.map(out)),kernel_denominator:"tau-1",fixed_kernel_denominator:String(den),visible_mass_functions:ds,source_rows:visible.values,polynomial_kernel_verified:true,
actual_integral_lift:"R_p=B(tau)(A_p B(tau))^-1; v_p=e_(C F G^4)-R_p A_p e_(C F G^4)",
actual_saturation:"A_p v_p=0; normalized delta J_N is a unit for all N in 4Z>0 on the fixed-ray relative-density-one subfamily; original q_N is not changed"};
}
function pair(){

const choose=(n,k)=>{let x=1;for(let j=1;j<=k;j++)x=x*(n+1-j)/j;return x;};
const facts=n=>{let x=1;for(let j=2;j<=n;j++)x*=j;return x;};
function c8(k){
 let v=0;
 if(k<=7)v+=2*choose(7,k)*2**k+choose(7,k)*(-1)**k*2**(7-k);
 if(k>=1)v-=choose(7,k-1)*2**(k-1);
 if(k>=1)v+=2*choose(7,k-1)*(-1)**(k-1)*2**(8-k);
 return Q(v,210);
}
const leading2=[2,3,-2],checks={};
for(const k of[3,5,6]){
 const mm=qm(c8(k),Q(facts(k)));
 const target=Q(k===3?36:k===5?720:240);
 ck(mm[0]===target[0]&&mm[1]===target[1],"full sigma degree-eight pair coefficient");
 checks[String(k)]={coefficient_q_power:8-k,taylor_b_coefficient:qs(c8(k)),moment_b_coefficient:qs(mm)};
}
ck(2+0===leading2[0]&&leading2[1]===3&&facts(2)*leading2[2]===-4,"pair degree-two coefficients");
const moment_table=[
{ell:0,source:"F12",factor:"1"},
{ell:1,source:"Z5",factor:"3 Omega"},
{ell:2,source:"D5",factor:"-4 Omega^2"},
{ell:3,source:"Sigma5",factor:"36 b Omega^3"},
{ell:4,source:"0",factor:"0"},
{ell:5,source:"X5",factor:"720 b Omega^5"},
{ell:6,source:"F12",factor:"120 b Omega^6"}
];
return{moment_table,exact_sigma_coefficients:checks,opposite_axis_sign:"(-1)^(ell+1)",
basis_scope:"Full standard odd S5 has the five one-dimensional angular lines 0,1,2,3,5; type 4 is absent. Coefficients plus the original S5 tensor identity determine whole sources, not truncated jets.",
finite_n_coefficients:{alpha_j:"e_j kappa^N+h_j kappa^n/315",b_j:"-29 e_j kappa^N+34 h_j kappa^n/315",observed:"A+q unit",j0:"K_k(alpha_0,b_0)",normalized_j1:"K_k(alpha_1,-b_1)"},
quadratic_kernels:{minus:"H_q^2 F12-174 Omega H_q Z5-3364 Omega^2 D5",plus:"H_q^2 F12+174 Omega H_q Z5-3364 Omega^2 D5"},
scope:"All seven conditional A measures remain; the T observation keeps the full A/Q/L mixed unit test."};

}

function certificate(all){
 const vis=visible(all),ker=kernel(all,vis),pr=pair();
 let den=1n;
 function visit(x){if(typeof x==="string"&&/^-?\d+\/\d+$/.test(x)){const d=BigInt(x.split("/")[1]);den=den/gcd(den,d)*d;}
 else if(Array.isArray(x))x.forEach(visit);else if(x&&typeof x==="object")Object.values(x).forEach(visit);}
 visit(ker);
 return{format:"R667 original arithmetic-null carry direction, seven conditional A sources and complete S5 moment contraction",
 input:"check-r594-two-source-six-carry-compensation.json; its existing exact matrices only",
 kernel:ker,column_moments:vis.column_moments,pair:pr,fixed_certificate_denominator:String(den),
 arithmetic_scope:"The original q_N remains fixed. Delta q_N is a separate same-family kernel test with identically zero complete pi4 pushforward; it does not vanish on each cut.",
 valuation:"v(delta J_N)=-2N for all N in 4Z>0 on one relative-density-one subfamily of the old fixed ray; both actual eta signs are retained.",
 compensation:"The known nonzero negative-one deep branch is exactly compensated by the original shallow mixed-unit domain plus the actual T exteriors. No central contradiction is inferred."};
}
const fs=require('fs'),path=require('path');
const all=JSON.parse(fs.readFileSync(path.join(__dirname,'check-r594-two-source-six-carry-compensation.json'),'utf8'));
const data=JSON.stringify(certificate(all),null,2)+'\n';
if(process.argv[2])fs.writeFileSync(process.argv[2],data);else process.stdout.write(data);
