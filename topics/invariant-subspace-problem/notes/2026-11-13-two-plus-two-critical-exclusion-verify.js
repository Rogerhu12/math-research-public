"use strict";
// Exact original-gradient and original-kernel certificate; no numerical root sampling.
function polynomialModel(dim){
const names=dim, D=names.length,zeroKey="0".repeat(D),z=()=>new Map(),con=n=>n?new Map([[zeroKey,n]]):z(),v=k=>new Map([[Array.from({length:D},(_,i)=>i===k?"1":"0").join(""),1]]);
function add(...xs){const o=z();for(const a of xs)for(const[k,x]of a){const n=(o.get(k)||0)+x;if(!Number.isSafeInteger(n))throw Error('integer overflow');o.set(k,n)};for(const[k,x]of o)if(!x)o.delete(k);return o}
function checked(n){if(!Number.isSafeInteger(n))throw Error('integer overflow');return n}
function sc(a,n){return new Map([...a].map(([k,x])=>[k,checked(x*n)]).filter(([k,x])=>x))}
function mul(a,b){const o=z();for(const[k,x]of a)for(const[l,y]of b){const ex=[...k].map((x,i)=>+x+(+l[i]));if(ex.some(x=>x>9))throw Error("monomial overflow");const t=ex.join("");const n=(o.get(t)||0)+x*y;if(!Number.isSafeInteger(n))throw Error("integer overflow");o.set(t,n)}for(const[k,x]of o)if(!x)o.delete(k);return o}
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
const names=["a","b","c","d","e","f","t"],P=polynomialModel(names),{z,con,v,add,sc,mul,calculate}=P,[a,b,c,d,e,f,t]=names.map((_,i)=>v(i)),eq=(p,q)=>{if(add(p,sc(q,-1)).size)throw Error("polynomial identity");};
const A=add(con(1),t),B=add(con(1),sc(t,-1)),K=[[z(),z(),c,d],[z(),a,e,f],[c,e,z(),z()],[d,f,z(),b]],Y=[A,con(2),B,con(2)],H=[[A,con(2),z(),z()],[con(2),z(),z(),z()],[z(),z(),B,con(2)],[z(),z(),con(2),z()]];
function tau2(is){if(is.every(i=>i<2)){const s=is.reduce((a,x)=>a+x,0);return s===0?A:s===1?con(2):z();}if(is.every(i=>i>=2)){const s=is.reduce((a,x)=>a+x-2,0);return s===0?B:s===1?con(2):z();}return z()}
const C=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>Array.from({length:4},(_,k)=>tau2([i,j,k])))),R=calculate(K,Y,H,C,[[0,1],[2,3]]);
function sub(p,im){let o=z();for(const[k,n]of p){let h=con(n);for(let i=0;i<k.length;i++)for(let j=0;j<+k[i];j++)h=mul(h,im[i]);o=add(o,h)}return o}
function diff(p,i){let o=z();for(const[k,n]of p)if(+k[i]){const a=[...k],e=+a[i];a[i]=String(e-1);o=add(o,new Map([[a.join(""),n*e]]))}return o}
const base=[a,b,con(1),d,e,f,t],V0=sub(R.V[0],base),V1=sub(R.V[1],base),H0=sub(R.H[0],base),PD=diff(V0,3);
const R1=add(sc(mul(d,d),4),sc(mul(d,t),-4),mul(t,t),sc(t,-1)),R2=add(sc(mul(d,d),4),sc(mul(d,add(t,con(2))),-4),mul(add(t,con(1)),add(t,con(2))));
eq(add(sc(H0,3),sc(mul(A,V0),-6),sc(V1,-4)),sc(add(mul(R2,b),sc(mul(R1,a),-1)),12));
eq(V1,add(mul(PD,add(f,sc(mul(d,e),-1))),sc(mul(e,V0),3),sc(mul(R1,a),6)));
eq(mul(d,PD),add(sc(mul(A,R1),3),sc(V0,3)));
const cubic=add(sc(mul(mul(d,d),d),8),sc(mul(A,mul(d,d)),-12),sc(mul(mul(t,A),d),6),t,sc(mul(mul(t,t),t),-1));eq(V0,cubic);
eq(sub(R.V[0],[a,b,z(),d,e,f,t]),sc(mul(mul(d,d),d),8));eq(sub(R.V[2],[a,b,z(),d,e,f,t]),sc(mul(mul(e,e),e),8));
eq(sub(R.V[0],[a,b,con(1),d,e,f,con(-1)]),sc(mul(mul(d,d),d),8));
eq(sub(R.V[1],[a,b,con(1),z(),e,f,con(-1)]),sc(a,12));
const im=[z(),b,con(1),z(),e,f,con(-1)];
eq(sub(R.H[1],im),sc(mul(b,f),-16));eq(sub(R.G[2],im),sc(mul(b,add(sc(f,2),b)),-32));
eq(sub(R.G[3],[z(),z(),con(1),z(),e,f,con(-1)]),sc(mul(f,f),128));
eq(sub(R.G[0],[z(),z(),con(1),z(),e,z(),con(-1)]),sc(mul(e,add(con(1),sc(e,-1))),64));
eq(sub(R.G[1],[z(),z(),con(1),z(),e,z(),con(-1)]),sc(add(con(1),sc(e,-4),sc(mul(e,e),2)),32));
function trim(a){a=a.slice();while(a.length>1&&!a.at(-1))a.pop();return a}
const pa=(a,b)=>trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||0)+(b[i]||0))),ps=(a,n)=>trim(a.map(x=>x*n));
function pm(a,b){const c=Array(a.length+b.length-1).fill(0);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=a[i]*b[j];if(c.some(x=>!Number.isSafeInteger(x)))throw Error("integer overflow");return trim(c)}
const pp=(a,n)=>{let r=[1];for(let i=0;i<n;i++)r=pm(r,a);return r},N=[-4,-6,0,1],L=[0,1,1],r=[0,1];
const Q=pa(pa(pm([2,3],pp(N,2)),ps(pm(N,pp(L,2)),3)),ps(pp(L,3),2));
const J=pa(pa(pa(pp(N,3),ps(pm(N,pp(L,2)),-6)),ps(pp(L,3),-4)),ps(pm(pm(r,pm(N,L)),pa(N,L)),-1));
const expectedQ=[32,144,204,52,-90,-45,10,6],expectedJ=[-64,-288,-424,-148,158,114,-3,-14,-2];
if(JSON.stringify(Q)!==JSON.stringify(expectedQ)||JSON.stringify(J)!==JSON.stringify(expectedJ))throw Error("rational compatibility expansion");
const U=[93,90,11,92,76,4,23,59],W=[32,33,86,69,24,52,74],mod=a=>trim(a.map(x=>((x%103)+103)%103));
const bezout=mod(pa(pm(U,Q),pm(W,J)));if(JSON.stringify(bezout)!=="[1]"||Q.at(-1)%103===0||J.at(-1)%103===0)throw Error("Bezout or full degree");
const K6=[[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],[0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]];
const ip=(x,y)=>x.reduce((s,v,i)=>s+v*K6[i].reduce((a,k,j)=>a+k*y[j],0),0);
function jets(s){if(s==="infty")return [[0,0,0,0,0,1],[0,0,0,0,1,0]];return [Array.from({length:6},(_,i)=>s**i),Array.from({length:6},(_,i)=>i===0?0:i*s**(i-1))]}
const points=[0,2,-6,"infty"],pairs=[];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++){const [u,du]=jets(points[i]),[w,dw]=jets(points[j]);const M=[[ip(u,w),ip(u,dw)],[ip(du,w),ip(du,dw)]];pairs.push({points:[points[i],points[j]],matrix:M,det:M[0][0]*M[1][1]-M[0][1]*M[1][0]});}
if(JSON.stringify(pairs.map(p=>p.det))!==JSON.stringify([2048,25380864,0,536870912,-40,-120]))throw Error("original cross determinants");
const sp=[con(1),t];for(let i=2;i<=4;i++)sp.push(mul(sp.at(-1),t));const tangent=[z(),con(1),sc(t,2),sc(sp[2],3),sc(sp[3],4),sc(sp[4],5)];let diagonal=z();for(let i=0;i<6;i++)for(let j=0;j<6;j++)diagonal=add(diagonal,sc(mul(tangent[i],tangent[j]),K6[i][j]));
eq(diagonal,sc(mul(sp[2],mul(add(t,con(-2)),add(t,con(6)))),-2));
if(JSON.stringify(pa(K6[4],ps(K6[5],5)))!==JSON.stringify([0,0,5]))throw Error("order-two ratio identity");
return {all_pass:true,gradient_reconstruction:true,three_local_identities:true,mu_zero_exclusion_identities:true,rational_compatibility:{N,L,Q,J,prime:103,full_degrees:[7,8],bezout_u:U,bezout_v:W,bezout_sum:bezout},original_special_cross_determinants:pairs,original_polar_coefficients_ascending:{at_zero:K6[0],first_jet_zero:K6[1],at_infinity:K6[5],first_jet_infinity:K6[4]},scope:"All full-H-rank outer-mean nonsecant essential-three complete cubic critical points with two double physical support points are excluded. The 2+1+1 and four-distinct base-free cases remain open."};
}
if(typeof module!=="undefined"&&module.exports){module.exports={verify};if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(verify(),null,2));}
