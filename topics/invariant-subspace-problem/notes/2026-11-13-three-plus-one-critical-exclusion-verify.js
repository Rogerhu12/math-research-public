"use strict";
// Exact reconstruction from the original complete-gradient tensor formulas.
// All coefficients are small integers. Every arithmetic result is checked safe.
// Run with Node: node 2026-11-13-three-plus-one-critical-exclusion-verify.js
function verify() {
 const names=["c","d","e","f","g","h"], zero=()=>new Map();
 const safe=n=>{if(!Number.isSafeInteger(n))throw Error("inexact integer");return n};
 const con=n=>n?new Map([["000000",n]]):zero();
 const variable=k=>new Map([[Array.from({length:6},(_,i)=>i===k?"1":"0").join(""),1]]);
 function add(...as){const r=zero();for(const a of as)for(const[k,n]of a)r.set(k,safe((r.get(k)||0)+n));for(const[k,n]of r)if(!n)r.delete(k);return r}
 function sc(a,n){return new Map([...a].map(([k,x])=>[k,safe(x*n)]).filter(([k,x])=>x))}
 function mul(a,b){const r=zero();for(const[k,x]of a)for(const[l,y]of b){const key=[...k].map((s,i)=>Number(s)+Number(l[i])).join("");r.set(key,safe((r.get(key)||0)+safe(x*y)))}for(const[k,n]of r)if(!n)r.delete(k);return r}
 const sq=a=>mul(a,a), dot=(a,b)=>add(...a.map((x,i)=>mul(x,b[i])));
 const mm=(A,B)=>A.map(row=>B[0].map((_,j)=>dot(row,B.map(row=>row[j]))));
 const eq=(a,b)=>{if(add(a,sc(b,-1)).size)throw Error("polynomial mismatch")};
 const atC0=a=>new Map([...a].filter(([k])=>k[0]==="0"));
 function sub(a,images){let r=zero();for(const[k,n]of a){let t=con(n);for(let i=0;i<6;i++)for(let j=0;j<Number(k[i]);j++)t=mul(t,images[i]);r=add(r,t)}return r}
 const [c,d,e,f,g,h]=names.map((_,i)=>variable(i));
 const K=[[zero(),zero(),c,f],[zero(),sc(c,-2),d,g],[c,d,e,h],[f,g,h,zero()]];
 const an=[1,0,2,1],a=an.map(con),bn=[[1,0,2,0],[0,2,0,0],[2,0,0,0],[0,0,0,1]],B=bn.map(row=>row.map(con));
 function tau2(inds){if(inds.every(i=>i<3))return [1,0,2][inds.reduce((s,x)=>s+x,0)]||0;return inds.every(i=>i===3)?1:0}
 const C=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>Array.from({length:4},(_,k)=>tau2([i,j,k]))));
 const T=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>Array.from({length:4},(_,k)=>an[i]*an[j]*an[k]-an[i]*bn[j][k]-an[j]*bn[i][k]-an[k]*bn[i][j]+2*C[i][j][k])));
 const P=K.map(row=>dot(row,a)),F=dot(a,P),BP=B.map(row=>dot(row,P)),KB=mm(K,B),KBK=mm(KB,K),BKB=mm(B,KB),BKBp=BKB.map(row=>dot(row,P));
 const Q=add(sq(F),sc(dot(P,BP),-4),sc(add(...mm(KB,KB).map((row,i)=>row[i])),2));
 const G=[];
 for(let i=0;i<4;i++){let CP=zero(),CK=zero();for(let j=0;j<4;j++)for(let k=0;k<4;k++){CP=add(CP,sc(mul(P[j],P[k]),C[i][j][k]));CK=add(CK,sc(KBK[j][k],C[i][j][k]));}G.push(add(sc(Q,an[i]),sc(mul(F,BP[i]),-4),sc(BKBp[i],8),sc(CP,8),sc(CK,-8)));}
 const N=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>add(sc(add(...P.map((p,k)=>sc(p,T[i][j][k]))),2),sc(F,-(an[i]*an[j]-bn[i][j])),sc(BKB[i][j],2))));
 const QM=mm(mm(K,N),K),H=[QM[0][0],QM[0][1],add(sc(QM[0][2],2),QM[1][1]),QM[3][3]];
 const V=[];
 for(let n=0;n<3;n++){let r=zero();for(let i=0;i<4;i++)for(let j=0;j<4;j++)for(let k=0;k<4;k++)for(let aa=0;aa<3;aa++)for(let bb=0;bb<3;bb++){const cc=n-aa-bb;if(cc<0||cc>=3)continue;r=add(r,sc(mul(mul(K[i][aa],K[j][bb]),K[k][cc]),T[i][j][k]));}V.push(r);}
 let r=zero();for(let i=0;i<4;i++)for(let j=0;j<4;j++)for(let k=0;k<4;k++)r=add(r,sc(mul(mul(K[i][3],K[j][3]),K[k][3]),T[i][j][k]));V.push(r);
 const E3=add(sq(add(e,sc(c,-1))),sc(sq(d),-2));
 const E0=add(sc(mul(e,h),-4),sc(mul(e,f),2),sc(sq(e),-3),sc(mul(d,g),4),sc(sq(d),6),sc(mul(c,f),2),sc(mul(c,e),6),sc(sq(c),-3));
 const E1=add(mul(add(e,c),g),sc(mul(d,add(h,sc(f,-1),e)),2));
 const E2=add(sc(mul(e,h),2),sc(mul(e,f),-2),sq(e),sc(mul(d,g),-2),sc(sq(d),-2),sc(mul(c,h),-2),sc(mul(c,e),-4),sc(sq(c),3));
 const E4=mul(sq(c),add(sc(f,3),sc(c,2)));
 const E5=mul(c,add(sc(mul(d,f),2),mul(c,g),sc(mul(c,d),2)));
 const E6=mul(c,add(sc(mul(e,f),2),sc(mul(c,h),2),sc(mul(c,f),-1),sc(mul(c,e),2),sc(sq(c),-2)));
 const E7=add(sc(mul(sq(e),f),2),sc(mul(mul(d,e),g),2),sc(mul(sq(d),h),2),sc(mul(sq(d),f),-3),sc(mul(sq(d),e),2));
 eq(G[0],sc(E0,16));eq(G[1],sc(E1,-32));eq(G[2],sc(E2,32));eq(G[3],sc(E3,16));
 eq(V[0],sc(E4,4));eq(V[1],sc(E5,12));eq(H[0],sc(E6,8));eq(atC0(H[2]),sc(E7,8));
 const im=[sc(c,3),sc(d,3),sc(e,3),sc(c,-2),sc(d,-2),add(sc(c,2),sc(e,-1))];
 eq(sub(E0,im),add(sc(mul(c,add(e,sc(c,2))),-12),sc(E3,-15)));
 eq(sub(E1,im),sc(mul(d,add(e,sc(c,3))),6));
 eq(add(atC0(E0),sc(atC0(E2),2),atC0(E3)),sc(mul(e,f),-2));
 const im2=[zero(),sc(d,2),sc(e,2),zero(),sc(d,-2),sc(e,-1)];
 eq(sub(E7,im2),sc(mul(sq(d),e),-8));
 const K6=[[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],[0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]];
 const sp=[con(1),c];for(let i=2;i<=5;i++)sp.push(mul(sp[i-1],c));
 const u0=sp,u1=[zero(),con(1),sc(c,2),sc(sp[2],3),sc(sp[3],4),sc(sp[4],5)],u2=[zero(),zero(),con(1),sc(c,3),sc(sp[2],6),sc(sp[3],10)];
 function inner(x,y){let r=zero();for(let i=0;i<6;i++)for(let j=0;j<6;j++)r=add(r,sc(mul(x[i],y[j]),K6[i][j]));return r}
 const originalC=inner(u0,u2),originalD=inner(u1,u2),originalE=inner(u2,u2);
 eq(originalC,mul(sp[2],mul(add(c,con(-2)),add(c,con(6)))));
 eq(originalD,sc(mul(c,add(sp[2],sc(c,3),con(-6))),-2));
 eq(originalE,add(con(54),sc(c,-24),sc(sp[2],-12)));
 function atS(p,s){let r=0;for(const[k,n]of p){if([...k].slice(1).some(t=>t!=="0"))throw Error("nonunivariate");r=safe(r+safe(n*s**Number(k[0])))}return r}
 if(atS(originalC,0)!==0||atS(originalD,0)!==0||atS(originalE,0)!==54||atS(originalD,2)!==-16||atS(originalD,-6)!==144||K6[5][3]!==0||K6[4][3]!==0||K6[3][3]!==-8)throw Error("contact mismatch");
 const serialize=p=>[...p].sort();
 return {all_pass:true,variables:names,monomial_encoding:"six exponent digits in variable order",mean_times_two:an,H_times_eight:bn,V_times_sixteen:C,T3_times_eight:T,G_times_128:G.map(serialize),H_jet_constraints_times_32:H.map(serialize),T3_jet_constraints_times_eight:V.map(serialize),necessary_equations:[E0,E1,E2,E3,E4,E5,E6,E7].map(serialize),case_elimination_identities_pass:true,original_triple_jet_contacts:{finite_c:"s^2*(s-2)*(s+6)",finite_d:"-2*s*(s^2+3*s-6)",at_zero:[0,0,54],at_two_d:-16,at_minus_six_d:144,at_infinity:[0,0,-8]},scope:"All original full-H-rank outer-mean nonsecant essential-three complete cubic critical points with support 3s+t are excluded. No classification of 2+2, 2+1+1, rank-drop or higher-essential-dimension strata is claimed."};
}
if(typeof module!=="undefined"&&module.exports){module.exports={verify};if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(verify(),null,2));}
