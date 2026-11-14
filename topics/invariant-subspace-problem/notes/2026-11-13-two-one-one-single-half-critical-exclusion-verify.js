"use strict";
// Exact polynomial certificate for the conic and single-half 2+1+1 classes.
function polynomialModel(dim){
const names=dim, D=names.length,zeroKey="0".repeat(D),z=()=>new Map(),con=n=>n?new Map([[zeroKey,n]]):z(),v=k=>new Map([[Array.from({length:D},(_,i)=>i===k?"1":"0").join(""),1]]);
function add(...xs){const o=z();for(const a of xs)for(const[k,x]of a){const n=(o.get(k)||0)+x;if(!Number.isSafeInteger(n))throw Error('integer overflow');o.set(k,n)};for(const[k,x]of o)if(!x)o.delete(k);return o}
function checked(n){if(!Number.isSafeInteger(n))throw Error('integer overflow');return n}
function sc(a,n){return new Map([...a].map(([k,x])=>[k,checked(x*n)]).filter(([k,x])=>x))}
function mul(a,b){const o=z();for(const[k,x]of a)for(const[l,y]of b){const ex=[...k].map((x,i)=>parseInt(x,36)+parseInt(l[i],36));if(ex.some(x=>x>35))throw Error("monomial overflow");const t=ex.map(x=>x.toString(36)).join("");const n=(o.get(t)||0)+x*y;if(!Number.isSafeInteger(n))throw Error("integer overflow");o.set(t,n)}for(const[k,x]of o)if(!x)o.delete(k);return o}
const dot=(a,b)=>add(...a.map((x,i)=>mul(x,b[i]))),mm=(A,B)=>A.map(a=>B[0].map((_,j)=>dot(a,B.map(b=>b[j]))));
function calculate(K,Y,B,C,groups){const T=C.map((r,i)=>r.map((r,j)=>r.map((x,k)=>add(mul(mul(Y[i],Y[j]),Y[k]),sc(mul(Y[i],B[j][k]),-1),sc(mul(Y[j],B[i][k]),-1),sc(mul(Y[k],B[i][j]),-1),sc(x,2)))));
const P=K.map(r=>dot(r,Y)),F=dot(Y,P),BP=B.map(r=>dot(r,P)),KB=mm(K,B),KBK=mm(KB,K),BKB=mm(B,KB),BKBp=BKB.map(r=>dot(r,P));
const Q=add(mul(F,F),sc(dot(P,BP),-4),sc(add(...mm(KB,KB).map((r,i)=>r[i])),2)),G=[];
for(let i=0;i<4;i++){let cp=z(),ck=z();for(let j=0;j<4;j++)for(let k=0;k<4;k++){cp=add(cp,mul(mul(P[j],P[k]),C[i][j][k]));ck=add(ck,mul(KBK[j][k],C[i][j][k]));}G.push(add(mul(Q,Y[i]),sc(mul(F,BP[i]),-4),sc(BKBp[i],8),sc(cp,8),sc(ck,-8)));}
const N=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>add(sc(add(...P.map((p,k)=>mul(p,T[i][j][k]))),2),sc(mul(F,add(mul(Y[i],Y[j]),sc(B[i][j],-1))),-1),sc(BKB[i][j],2))));
const QM=mm(mm(K,N),K);
function t3(x,y,w){let o=z();for(let i=0;i<4;i++)for(let j=0;j<4;j++)for(let k=0;k<4;k++)o=add(o,mul(mul(mul(x[i],y[j]),w[k]),T[i][j][k]));return o}
const col=j=>K.map(r=>r[j]),H=[],V=[];
for(const group of groups)for(let n=0;n<group.length;n++){let hh=z(),vv=z();for(let aa=0;aa<group.length;aa++)for(let bb=0;bb<group.length;bb++){if(aa+bb===n)hh=add(hh,QM[group[aa]][group[bb]]);const cc=n-aa-bb;if(cc>=0&&cc<group.length)vv=add(vv,t3(col(group[aa]),col(group[bb]),col(group[cc])));}H.push(hh);V.push(vv);}
return {G,H,V,Q,N,T};}
function fmt(p){return [...p].sort().map(([k,n])=>n+"*"+[...k].map((x,i)=>x==="0"?"":names[i]+(x==="1"?"":"^"+x)).filter(Boolean).join("*")).join(" + ")}
return {z,con,v,add,sc,mul,dot,mm,calculate,fmt};
}

function verify(){
const names=["a","b","c","d","e","h","t"],P=polynomialModel(names),{z,con,v,add,sc,mul,calculate}=P,[a,b,c,d,e,h,t]=names.map((_,i)=>v(i)),eq=(p,q)=>{if(add(p,sc(q,-1)).size)throw Error("polynomial mismatch")},pow=(p,n)=>{let q=con(1);for(let i=0;i<n;i++)q=mul(q,p);return q};
const K=[[z(),z(),a,b],[z(),h,c,d],[a,c,z(),e],[b,d,e,z()]];
function model(m,beta,gamma){const Y=[m,con(2),beta,gamma],H=[[m,con(2),z(),z()],[con(2),z(),z(),z()],[z(),z(),beta,z()],[z(),z(),z(),gamma]];
function tau2(is){if(is.every(i=>i<2)){const s=is.reduce((a,x)=>a+x,0);return s===0?m:s===1?con(2):z();}if(is.every(i=>i===2))return beta;if(is.every(i=>i===3))return gamma;return z()}
const C=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>Array.from({length:4},(_,k)=>tau2([i,j,k]))));return calculate(K,Y,H,C,[[0,1],[2],[3]]);}
function sub(p,im){let o=z();for(const[k,n]of p){let q=con(n);for(let i=0;i<k.length;i++)for(let j=0;j<parseInt(k[i],36);j++)q=mul(q,im[i]);o=add(o,q)}return o}
const CC=model(z(),con(1),con(1)),SS=model(add(con(1),sc(t,-1)),con(1),t);
function evalT(T,x){let q=z();for(let i=0;i<4;i++)for(let j=0;j<4;j++)for(let k=0;k<4;k++)q=add(q,mul(mul(mul(x[i],x[j]),x[k]),T[i][j][k]));return q}
function conicQ(x){return add(sc(mul(add(x[2],sc(x[0],-1)),add(x[3],sc(x[0],-1))),3),sc(mul(x[1],add(x[2],x[3],sc(x[0],-2))),3),sc(pow(x[1],2),2))}
eq(evalT(CC.T,[a,b,c,d]),sc(mul(b,conicQ([a,b,c,d])),4));
const col0=K.map(r=>r[0]),col1=K.map(r=>r[1]);eq(conicQ(col0),sc(mul(a,b),3));eq(add(conicQ(col0.map((x,i)=>add(x,col1[i]))),sc(conicQ(col0),-1),sc(conicQ(col1),-1)),sc(add(mul(a,d),mul(b,c),mul(h,add(a,b))),3));
const ab0=[z(),z(),c,d,e,h,t];
eq(sub(CC.G[2],ab0),sc(mul(h,add(h,sc(d,2))),16));eq(sub(CC.G[3],ab0),sc(mul(h,add(h,sc(c,2))),16));
eq(sub(CC.G[1],ab0),add(sc(pow(h,2),32),sc(mul(e,h),32),sc(mul(add(c,d),h),64),sc(mul(c,d),64)));
eq(sub(CC.V[2],ab0),add(sc(mul(pow(c,2),e),12),sc(pow(c,3),8)));
eq(SS.V[0],mul(mul(t,add(t,con(-1))),mul(pow(b,2),add(sc(a,3),mul(add(t,con(-2)),b)))));
const b0=[a,z(),c,d,e,h,t],g2=add(pow(h,2),sc(mul(mul(t,d),h),2),mul(mul(t,add(t,con(-1))),pow(d,2)));
eq(sub(SS.G[2],b0),sc(g2,16));
eq(sub(SS.H[1],b0),sc(mul(a,add(sc(pow(h,2),2),sc(mul(mul(t,d),h),3),mul(mul(t,add(t,con(-1))),pow(d,2)))),8));
eq(sub(SS.V[3],ab0),sc(mul(pow(d,2),add(sc(e,3),sc(d,2))),4));
const r=t,r2=pow(r,2),imNode=[z(),z(),add(r2,sc(r,-1)),con(3),con(-2),sc(mul(r,add(con(1),sc(r,-1))),3),r2];
eq(sub(SS.G[0],imNode),sc(mul(r2,add(r,con(-1))),96));eq(sub(SS.G[1],imNode),z());eq(sub(SS.G[2],imNode),z());
const base=[add(con(2),sc(t,-1)),con(3),c,d,e,h,t],tm1=add(t,con(-1)),tm2=add(t,con(-2)),tp1=add(t,con(1));
eq(sub(SS.V[1],base),sc(mul(t,add(sc(mul(tp1,h),2),mul(mul(tm1,tm2),d),sc(mul(tm1,c),3))),9));
eq(add(sc(sub(SS.H[0],base),3),sc(sub(SS.V[1],base),-2)),sc(mul(mul(t,tm1),add(sc(mul(tm2,e),3),mul(tm2,d),sc(c,3))),18));
const u=a,rr=r2,q=sc(mul(add(rr,con(-1)),add(rr,con(-2))),3),D2=add(sc(rr,6),sc(u,2)),H2=add(sc(mul(add(r,sc(rr,-1)),u),2),sc(mul(rr,add(con(1),sc(rr,-1))),3));
const big=[
sc(mul(add(con(2),sc(rr,-1)),q),2),sc(q,6),
add(sc(mul(mul(add(rr,con(-1)),pow(add(rr,con(-2)),2)),D2),-1),sc(mul(mul(add(rr,con(1)),add(rr,con(-2))),H2),-2)),
mul(q,D2),sc(mul(add(rr,con(1)),H2),2),mul(q,H2),rr
];
eq(sub(SS.G[2],big),z());
const square=pow(add(sc(u,2),sc(mul(r,add(r,con(1))),3)),2);
const pref=sc(mul(mul(mul(mul(rr,add(rr,con(-1))),add(rr,con(-2))),pow(add(r,con(-1)),2)),add(rr,con(1))),192);
eq(sub(SS.G[3],big),mul(pref,square));
const Dspec=sc(mul(r,add(r,con(-1))),3);
const special=[sc(mul(add(con(2),sc(rr,-1)),q),2),sc(q,6),sc(mul(mul(add(rr,con(-1)),pow(add(rr,con(-2)),2)),Dspec),-1),mul(q,Dspec),z(),z(),rr];
const finalG1=sc(mul(mul(mul(pow(r,3),pow(add(rr,con(-1)),2)),pow(add(rr,con(-2)),2)),add(rr,con(1))),1728);
eq(sub(SS.G[1],special),finalG1);
const exceptional=[con(3),con(3),d,d,z(),h,con(-1)];
eq(sub(SS.G[0],exceptional),sc(pow(h,2),-32));eq(sub(SS.V[2],exceptional),sc(pow(d,3),8));eq(sub(SS.G[2],[con(3),con(3),z(),z(),z(),z(),con(-1)]),con(144));
return {all_pass:true,conic_factor_and_origin_jets:true,conic_complete_gradient_conditions:true,single_half_highest_factor:true,node_at_double_point_elimination:true,linear_elimination_at_nonzero_b:true,cleared_conic_parametrization:true,remaining_square_identity:true,final_nonzero_G1_identity:true,exception_t_minus_one:true,scope:"All full-H-rank outer-mean nonsecant essential-three complete cubic critical points of support 2+1+1 with at least one single support weight 1/2 are excluded. Only the double block of total weight 1/2 remains in this support type."};
}
if(typeof module!=="undefined"&&module.exports){module.exports={verify};if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(verify(),null,2));}
