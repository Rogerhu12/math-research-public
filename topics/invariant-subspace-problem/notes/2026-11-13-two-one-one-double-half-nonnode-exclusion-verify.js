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


function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b]}return a}
function lcm(a,b){return a/gcd(a,b)*b}
function rat(a,b=1n){a=BigInt(a);b=BigInt(b);if(b<0n){a=-a;b=-b}let g=gcd(a,b);return[a/g,b/g]}
function ra(x,y){return rat(x[0]*y[1]+y[0]*x[1],x[1]*y[1])}
function rm(x,y){return rat(x[0]*y[0],x[1]*y[1])}
const rz=rat(0),ro=rat(1);
function quadReduce(p){
 const o=new Map(),powers=[[ro,rz],[rz,ro]];
 let max=Math.max(0,...p.map(([k])=>parseInt(k[0],36)));
 for(let n=2;n<=max;n++)powers[n]=[rm(powers[n-1][1],rat(1,14)),ra(powers[n-1][0],powers[n-1][1])];
 for(const[k,n]of p){const power=powers[parseInt(k[0],36)];for(let j=0;j<2;j++){const key=j+k.slice(1);o.set(key,ra(o.get(key)||rz,rm(rat(n),power[j])))}}
 let den=1n;for(const q of o.values())den=lcm(den,q[1]);
 const pp=[...o].map(([k,q])=>[k,q[0]*(den/q[1])]).filter(([k,n])=>n);
 let g=0n;for(const[k,n]of pp)g=gcd(g,n);return pp.map(([k,n])=>[k,Number(n/g)]);
}


function verify(){
 const S=polynomialModel(["a","b","c","d","e","h","t"]);
 const{z:zs,con:cs,v:vs,add:as,sc:ss,mul:ms}=S;
 const[a,b,c,d,e,h,t]=Array.from({length:7},(_,i)=>vs(i)),one=cs(1),A=as(one,ss(t,-1));
 const K=[[zs(),zs(),a,b],[zs(),h,c,d],[a,c,zs(),e],[b,d,e,zs()]];
 const Y=[one,cs(2),t,A],B=[[one,cs(2),zs(),zs()],[cs(2),zs(),zs(),zs()],[zs(),zs(),t,zs()],[zs(),zs(),zs(),A]];
 const C=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>Array.from({length:4},(_,k)=>{
 if(i<2&&j<2&&k<2)return i+j+k===0?one:i+j+k===1?cs(2):zs();
 if(i===2&&j===2&&k===2)return t;if(i===3&&j===3&&k===3)return A;return zs();
 })));
 const R=S.calculate(K,Y,B,C,[[0,1],[2],[3]]);let count=0;
 function eq(P,x,y,name){const q=P.add(x,P.sc(y,-1));if(q.size)throw Error(name+": "+P.fmt(q));count++;}
 function substitute(P,p,im){let o=P.z();for(const[k,n]of p){let q=P.con(n);for(let i=0;i<k.length;i++)for(let j=0;j<parseInt(k[i],36);j++)q=P.mul(q,im[i]);o=P.add(o,q)}return o;}
 eq(S,R.V[0],ms(ms(t,A),ms(ms(as(a,ss(b,-1)),as(a,ss(b,-1))),as(ms(as(cs(2),ss(t,-1)),a),ms(as(one,t),b)))),"highest branch split");
 const im=[as(t,one),as(t,cs(-2)),c,d,e,h,t],N=Object.fromEntries(["G","H","V"].map(k=>[k,R[k].map(p=>substitute(S,p,im))]));
 const tm1=as(t,cs(-1)),tp1=as(t,one),tm2=as(t,cs(-2));
 eq(S,N.V[1],ss(ms(ms(t,tm1),as(ss(h,6),ss(ms(tp1,d),-1),ms(tm2,c))),9),"nonnode V1");
 eq(S,N.H[0],ss(ms(ms(t,tm1),as(ss(h,18),ss(ms(tp1,d),-6),ss(ms(tm2,c),6),ms(ms(tm2,tp1),e))),2),"nonnode H0");
 const P=polynomialModel(["t","u","e"]),{z,con,v,add,sc,mul}=P,[tt,u,ee]=[v(0),v(1),v(2)],aa=add(tt,con(1)),bb=add(tt,con(-2));
 const ims=[sc(aa,18),sc(bb,18),sc(mul(aa,u),18),add(sc(mul(bb,u),18),sc(mul(bb,ee),6)),sc(ee,18),mul(mul(aa,bb),ee),tt];
 const Q=Object.fromEntries(["G","H","V"].map(k=>[k,R[k].map(p=>substitute(P,p,ims))]));
 const q=add(sc(mul(tt,tt),14),sc(tt,-14),con(-1));
 eq(P,add(sc(mul(aa,Q.G[2]),-1),mul(sc(bb,-1),Q.G[3])),sc(mul(mul(mul(mul(aa,bb),add(sc(tt,2),con(-1))),q),mul(ee,ee)),-64),"e squared syzygy");
 eq(P,substitute(P,Q.G[0],[tt,u,z()]),sc(mul(mul(tt,add(con(1),sc(tt,-1))),mul(u,u)),46656),"e zero gives u zero");
 function primitive(p){let g=0;function gg(a,b){a=Math.abs(a);b=Math.abs(b);while(b){[a,b]=[b,a%b]}return a}for(const n of p.values())g=gg(g,n);return new Map([...p].filter(([k,n])=>n).map(([k,n])=>[k,n/g]));}
 function half(p){const max=Math.max(0,...[...p.keys()].map(k=>parseInt(k[0],36)));let o=z();for(const[k,n]of p)o=add(o,new Map([["0"+k.slice(1),n*2**(max-parseInt(k[0],36))]]));return primitive(o);}
 eq(P,half(Q.H[1]),sc(ee,-1),"half-weight H1");
 const QR=Object.fromEntries(["G","H"].map(k=>[k,Q[k].map(p=>new Map(quadReduce([...p])))]));
 eq(P,QR.H[1],mul(ee,add(con(9),sc(ee,-5),sc(mul(tt,ee),10))),"quadratic exceptional H1");
 function replaceFraction(p,index,numerator,den,degree){let o=z();for(const[k,n]of p){const power=parseInt(k[index],36);let qq=con(n*den**(degree-power));for(let i=0;i<k.length;i++){const base=i===index?numerator:v(i);for(let j=0;j<parseInt(k[i],36);j++)qq=mul(qq,base);}o=add(o,qq);}return o;}
 const Ee=add(con(7),sc(tt,-14));
 const PG=QR.G.map(p=>new Map(quadReduce([...replaceFraction(p,2,Ee,5,2)])));
 const P0=add(con(-37),sc(u,-460),sc(mul(u,u),-150),sc(tt,182),sc(mul(tt,u),140));
 const P1=add(con(-111),sc(u,160),sc(mul(u,u),150),sc(tt,-42),sc(mul(tt,u),-140));
 eq(P,PG[0],P0,"quadratic G0 after H1");eq(P,PG[1],P1,"quadratic G1 after H1");
 eq(P,add(P0,P1),add(con(-148),sc(u,-300),sc(tt,140)),"linear u equation");
 const numerator=replaceFraction(P0,1,add(sc(tt,35),con(-37)),75,2);
 // 75^2 P0 = 876150 + 183750(t^2-t-1/14).
 eq(P,sc(add(numerator,con(-876150)),14),sc(q,183750),"constant residual 3894/25");
 return {status:"exact",identities:count,coefficient_ring:"Z[a,b,c,d,e,h,t] with explicitly cleared rational specializations",exceptional_polynomial:"14t^2-14t-1",constant_residual:"3894/25",result:"The double-half 2+1+1 nonnode branch is empty after the written original-curve immersion argument."};
}
if(typeof module!=="undefined")module.exports={verify};
if(typeof require!=="undefined"&&require.main===module)process.stdout.write(JSON.stringify(verify(),null,2)+"\n");
