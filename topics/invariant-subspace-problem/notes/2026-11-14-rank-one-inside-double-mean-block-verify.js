"use strict";
function polynomialModel(dim){
const names=dim, D=names.length,zeroKey="0".repeat(D),z=()=>new Map(),con=n=>n?new Map([[zeroKey,BigInt(n)]]):z(),v=k=>new Map([[Array.from({length:D},(_,i)=>i===k?"1":"0").join(""),1n]]);
function add(...xs){const o=z();for(const a of xs)for(const[k,x]of a)o.set(k,(o.get(k)||0n)+x);for(const[k,x]of o)if(!x)o.delete(k);return o}
function sc(a,n){return new Map([...a].map(([k,x])=>[k,x*BigInt(n)]).filter(([k,x])=>x))}
function mul(a,b){const o=z();for(const[k,x]of a)for(const[l,y]of b){const ex=[...k].map((x,i)=>parseInt(x,36)+parseInt(l[i],36));if(ex.some(x=>x>35))throw Error("monomial overflow");const t=ex.map(x=>x.toString(36)).join("");const n=(o.get(t)||0n)+x*y;o.set(t,n)}for(const[k,x]of o)if(!x)o.delete(k);return o}
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

const names=["h0","b","v0","h","k","v","w","l1","l2","n1","n2","g0","g"];
const P=polynomialModel(names),{z,con,v,add,sc,mul}=P;
const [a,b,c0,h,k,vv,ww,l1,l2,n1,n2,g0,g]=names.map((_,i)=>v(i));
const K=[[z(),z(),l1,l2],[z(),g0,n1,n2],[l1,n1,z(),g],[l2,n2,g,z()]];
const Y=[con(2),z(),z(),z()];
const B=[[sc(a,8),sc(b,8),z(),z()],[sc(b,8),z(),z(),z()],[z(),z(),sc(h,8),z()],[z(),z(),z(),sc(k,8)]];
const C=Array.from({length:4},()=>Array.from({length:4},()=>Array.from({length:4},()=>z())));
C[0][0][0]=sc(c0,16);C[0][0][1]=sc(b,16);C[0][1][0]=sc(b,16);C[1][0][0]=sc(b,16);C[2][2][2]=sc(vv,16);C[3][3][3]=sc(ww,16);
const out=P.calculate(K,Y,B,C,[]);
const kap=add(con(1),sc(a,-6),sc(c0,4)),d=add(con(1),sc(a,-2));
const bR=add(mul(h,mul(l1,l1)),mul(k,mul(l2,l2)));
const G=[
 add(sc(mul(kap,bR),-2),sc(mul(mul(h,k),mul(g,g)),4)),z(),
 add(sc(mul(mul(mul(h,k),g),l2),8),sc(mul(mul(d,vv),mul(l1,l1)),4),sc(mul(mul(b,vv),mul(l1,n1)),-16),sc(mul(mul(vv,k),mul(g,g)),-8)),
 add(sc(mul(mul(mul(h,k),g),l1),8),sc(mul(mul(d,ww),mul(l2,l2)),4),sc(mul(mul(b,ww),mul(l2,n2)),-16),sc(mul(mul(ww,h),mul(g,g)),-8))
];
const ny1=add(sc(mul(mul(d,h),l1),-2),sc(mul(mul(b,h),n1),4));
const ny2=add(sc(mul(mul(d,k),l2),-2),sc(mul(mul(b,k),n2),4));
const nu1=sc(mul(mul(b,h),l1),4),nu2=sc(mul(mul(b,k),l2),4);
const NN=[
[sc(mul(g0,mul(b,b)),4),z(),ny1,ny2],
[z(),z(),nu1,nu2],
[ny1,nu1,sc(mul(vv,l1),4),sc(mul(mul(h,k),g),4)],
[ny2,nu2,sc(mul(mul(h,k),g),4),sc(mul(ww,l2),4)]
];
let count=0;
for(let i=0;i<4;i++){if(add(out.G[i],sc(G[i],-128)).size)throw Error("Gamma "+i);count++;for(let j=0;j<4;j++){if(add(out.N[i][j],sc(NN[i][j],-32)).size)throw Error("N "+i+","+j);count++}}
const e1=add(mul(kap,mul(l1,l1)),sc(mul(k,mul(g,g)),-6));
const e2=add(mul(kap,mul(l2,l2)),sc(mul(h,mul(g,g)),-6));
if(add(G[0],sc(mul(h,e1),2),sc(mul(k,e2),2),sc(mul(mul(h,k),mul(g,g)),20)).size)throw Error("Twenty identity");count++;
return {status:"PASS",arithmetic:"BigInt",identities:count,G:G.map(P.fmt),N:NN.map(r=>r.map(P.fmt)),mean_block_retained:true};

}
if(typeof module!=="undefined")module.exports={verify};
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module)
process.stdout.write(JSON.stringify(verify(),null,2)+"\n");