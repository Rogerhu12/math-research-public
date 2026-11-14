"use strict";
function polynomialModel(dim){
const names=dim, D=names.length,zeroKey="0".repeat(D),z=()=>new Map(),con=n=>n?new Map([[zeroKey,n]]):z(),v=k=>new Map([[Array.from({length:D},(_,i)=>i===k?"1":"0").join(""),1]]);
function add(...xs){const o=z();for(const a of xs)for(const[k,x]of a)o.set(k,(o.get(k)||0)+x);for(const[k,x]of o)if(!x)o.delete(k);return o}
function sc(a,n){return new Map([...a].map(([k,x])=>[k,x*n]).filter(([k,x])=>x))}
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

const names=["rho","F","l1","l2","n1","n2","g","h","k","v","w"];
const P=polynomialModel(names),{z,con,v,add,sc,mul}=P;
const [r,F,l,m,n,o,g,h,k,a,b]=names.map((_,i)=>v(i));
const K=[[sc(F,2),z(),l,m],[z(),sc(F,-2),n,o],[l,n,z(),g],[m,o,g,z()]];
const Y=[con(2),z(),z(),z()];
const B=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>i===j?[sc(r,4),sc(r,4),sc(h,8),sc(k,8)][i]:z()));
const C=Array.from({length:4},()=>Array.from({length:4},()=>Array.from({length:4},()=>z())));
C[0][0][0]=sc(r,4);C[0][1][1]=sc(r,4);C[1][0][1]=sc(r,4);C[1][1][0]=sc(r,4);C[2][2][2]=sc(a,16);C[3][3][3]=sc(b,16);
const out=P.calculate(K,Y,B,C,[]);
const kap=add(con(1),sc(r,-2)),oneR=add(con(1),sc(r,-1));
const bform=add(mul(h,mul(l,l)),mul(k,mul(m,m)));
const g0=add(mul(mul(kap,kap),mul(F,F)),sc(mul(kap,bform),-2),sc(mul(mul(h,k),mul(g,g)),4));
const g2=add(sc(mul(mul(mul(kap,F),h),l),-4),sc(mul(mul(mul(h,k),g),m),8),sc(mul(mul(oneR,a),mul(l,l)),4),sc(mul(mul(r,a),mul(n,n)),-4),sc(mul(mul(a,k),mul(g,g)),-8));
const g3=add(sc(mul(mul(mul(kap,F),k),m),-4),sc(mul(mul(mul(h,k),g),l),8),sc(mul(mul(oneR,b),mul(m,m)),4),sc(mul(mul(r,b),mul(o,o)),-4),sc(mul(mul(b,h),mul(g,g)),-8));
const wantG=[g0,z(),g2,g3];
const NN=[
 [mul(mul(oneR,kap),F),z(),sc(mul(mul(oneR,h),l),-2),sc(mul(mul(oneR,k),m),-2)],
 [z(),mul(mul(r,kap),F),sc(mul(mul(r,h),n),2),sc(mul(mul(r,k),o),2)],
 [sc(mul(mul(oneR,h),l),-2),sc(mul(mul(r,h),n),2),add(sc(mul(F,h),-2),sc(mul(a,l),4)),sc(mul(mul(h,k),g),4)],
 [sc(mul(mul(oneR,k),m),-2),sc(mul(mul(r,k),o),2),sc(mul(mul(h,k),g),4),add(sc(mul(F,k),-2),sc(mul(b,m),4))]
];
const bad=[];
for(let i=0;i<4;i++){if(add(out.G[i],sc(wantG[i],-128)).size)bad.push({G:i,actual:P.fmt(out.G[i]),expected:P.fmt(sc(wantG[i],128))});for(let j=0;j<4;j++)if(add(out.N[i][j],sc(NN[i][j],-32)).size)bad.push({N:[i,j],actual:P.fmt(out.N[i][j]),expected:P.fmt(sc(NN[i][j],32))})}
return {status:bad.length?"FAIL":"PASS",bad,G:wantG.map(P.fmt),N:NN.map(r=>r.map(P.fmt)),original_scalings:{Y:2,B:8,C:16,G:128,N:32}};

}
if(typeof module!=="undefined")module.exports={verify};
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module)
process.stdout.write(JSON.stringify(verify(),null,2)+"\n");
