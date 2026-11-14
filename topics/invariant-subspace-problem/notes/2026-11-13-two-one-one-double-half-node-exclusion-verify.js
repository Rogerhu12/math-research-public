"use strict";
// Exact author certificate for the double-half node branch.
function polynomialModel(dim){
const names=dim, D=names.length,zeroKey="0".repeat(D),z=()=>new Map(),con=n=>n?new Map([[zeroKey,n]]):z(),v=k=>new Map([[Array.from({length:D},(_,i)=>i===k?"1":"0").join(""),1]]);
function add(...xs){const o=z();for(const a of xs)for(const[k,x]of a){const n=(o.get(k)||0)+x;if(!Number.isSafeInteger(n))throw Error("integer overflow");o.set(k,n)}for(const[k,x]of o)if(!x)o.delete(k);return o}
function sc(a,n){return new Map([...a].map(([k,x])=>{const y=x*n;if(!Number.isSafeInteger(y))throw Error("integer overflow");return [k,y]}).filter(([k,x])=>x))}
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
 const P=polynomialModel(["a","b","c","d","e","h","t"]);
 const {z,con,v,add,sc,mul,calculate}=P;
 const [a,b,c,d,e,h,t]=Array.from({length:7},(_,i)=>v(i)),one=con(1),A=add(one,sc(t,-1)),B=t,T=mul(A,B);
 const K=[[z(),z(),a,b],[z(),h,c,d],[a,c,z(),e],[b,d,e,z()]];
 const Y=[one,con(2),B,A],BB=[[one,con(2),z(),z()],[con(2),z(),z(),z()],[z(),z(),B,z()],[z(),z(),z(),A]];
 const C=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>Array.from({length:4},(_,k)=>{
  if(i<2&&j<2&&k<2)return i+j+k===0?one:i+j+k===1?con(2):z();
  if(i===2&&j===2&&k===2)return B;if(i===3&&j===3&&k===3)return A;return z();
 })));
 const R=calculate(K,Y,BB,C,[[0,1],[2],[3]]);
 let count=0;
 function eq(x,y,name){const q=add(x,sc(y,-1));if(q.size)throw Error(name+": "+P.fmt(q));count++;}
 function sub(p,im){let o=z();for(const[k,n]of p){let q=con(n);for(let i=0;i<k.length;i++)for(let j=0;j<parseInt(k[i],36);j++)q=mul(q,im[i]);o=add(o,q);}return o;}
 const im=[a,a,c,d,e,h,t],S=Object.fromEntries(["G","H","V"].map(k=>[k,R[k].map(p=>sub(p,im))]));
 eq(S.H[0],sc(mul(mul(a,a),mul(e,T)),4),"node H0");
 const e0=p=>sub(p,[a,b,c,d,z(),h,t]),delta=add(c,sc(d,-1));
 eq(e0(add(S.G[2],S.G[3])),sc(add(mul(h,h),mul(T,mul(delta,delta))),16),"G2+G3");
 eq(e0(S.H[1]),sc(mul(a,add(sc(mul(h,h),2),mul(T,mul(delta,delta)))),8),"node H1");
 for(let j=2;j<4;j++)eq(sub(S.V[j],[a,b,c,c,z(),z(),t]),sc(mul(mul(c,c),add(sc(c,2),sc(a,-3))),4),"node V"+j);
 const p=add(sc(mul(mul(c,c),c),8),sc(mul(A,mul(c,c)),12),sc(mul(T,c),-6),mul(T,add(one,B)));
 const pm=add(sc(mul(mul(d,d),d),8),sc(mul(B,mul(d,d)),12),sc(mul(T,d),-6),mul(T,add(one,A)));
 const r1=add(sc(mul(c,c),4),sc(mul(A,c),4),sc(T,-1));
 const r1m=add(sc(mul(d,d),4),sc(mul(B,d),4),sc(T,-1));
 const U=Object.fromEntries(["G","H","V"].map(k=>[k,R[k].map(p=>sub(p,[z(),z(),c,d,one,h,t]))]));
 eq(U.V[2],p,"basepoint P");eq(U.V[3],pm,"basepoint P mirror");
 eq(U.H[2],add(sc(mul(r1,add(h,sc(mul(c,d),-2))),4),mul(add(sc(d,4),sc(B,2)),p)),"basepoint H2");
 eq(sub(U.G[1],[a,b,c,d,e,sc(mul(c,d),2),t]),sc(mul(r1,r1m),8),"basepoint G1");
 const x=add(sc(c,2),A);
 eq(p,add(mul(mul(x,x),x),sc(mul(A,x),-3),sc(A,2)),"depressed P");
 return {status:"exact",identities:count,coefficient_ring:"Z[a,b,c,d,e,h,t]",result:"The double-half 2+1+1 node branch a=b is empty under the stated original full-gradient assumptions."};
}
if(typeof module!=="undefined")module.exports={verify};
if(typeof require!=="undefined"&&require.main===module)process.stdout.write(JSON.stringify(verify(),null,2)+"\n");
