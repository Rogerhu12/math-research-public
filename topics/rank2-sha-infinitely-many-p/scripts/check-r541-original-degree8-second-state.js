#!/usr/bin/env node
// R541: exact characteristic-zero certificate; all arithmetic uses BigInt.
function checkExactPair8(){"use strict";
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


const al=E(1,3),ga=E(3,1),gb=ec(ga),c=E(1,1,2),dd=E(0,1,2);
const add=(p,q)=>Array.from({length:Math.max(p.length,q.length)},(_,i)=>ea(p[i]||E(0),q[i]||E(0))),scale=(p,c)=>p.map(x=>em(x,c));
const mul=(p,q)=>{let v=Array.from({length:p.length+q.length-1},()=>E(0));p.forEach((x,i)=>q.forEach((y,j)=>v[i+j]=ea(v[i+j],em(x,y))));return v;};
const pow=(p,n)=>{let r=[E(1)];while(n--)r=mul(r,p);return r;};
const prod=(p,q,k)=>{if(k===2)return mul(p,q); if(k===8)return scale(add(mul(pow(p,7),q),mul(p,pow(q,7))),E(1,0,210)); if(k===14)return add(scale(add(mul(pow(p,13),q),mul(p,pow(q,13))),E(-1,0,1801800)),scale(mul(pow(p,7),pow(q,7)),E(1,0,44100))); throw Error("k");};
const sigma2sq={2:E(4),8:E(256,0,105),14:ea(E(-32768,0,1801800),E(16384,0,44100))};
const theta2={0:E(1),6:E(-128,0,15),12:E(16384,0,17325)};
let checks=[];
for(const k of [2,8,14]){const actual=prod([en(al),E(1)],[E(-1),en(ec(al))],k),target=scale(prod([ga,E(1)],[E(1),en(gb)],k),E(-1));
for(const [i0,sq]of Object.entries(sigma2sq)){const i=Number(i0),j=k-i;if(j in theta2){actual[j]=es(actual[j],esc(em(c,em(sq,theta2[j])),2));actual[i]=es(actual[i],esc(em(dd,em(sq,theta2[j])),2));}}
const difference=actual.map((a,i)=>es(a,target[i]));ck(difference.every(ez),"full degree "+k+" mismatch");
const ref=prod([en(al),E(1)],[E(-1),en(ec(al))],k),eta=scale(prod([E(2),E(0,2)],[E(2),E(0,-2)],k),E(-1,-1));
const three=add(ref,eta).map((a,i)=>es(a,target[i]));ck(three.every(ez),"three actual pairs "+k+" mismatch");
checks.push({degree:k,difference:difference.map(out),three_pair_difference:three.map(out)});}
return{c:out(c),d:out(dd),checks};
}
function checkPairFrames(){"use strict";
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


const al=E(1,3),ga=E(3,1),gb=ec(ga),ga13=E(4,1),om=E(0,1);
const Aa=[[al,E(1)],[E(1),en(ec(al))]],Ag=[[ga,E(1)],[E(1),en(gb)]],Ae=[[E(2),E(2)],[E(0,2),E(0,-2)]];
const Ai=inverse(Aa).inverse,G=mm(Ai,Ag),H=mm(Ai,Ae),refl=mm(mm(Ai,[[E(-1),E(0)],[E(0),E(1)]]),Aa);
const outm=M=>M.map(r=>r.map(out)),adj=M=>M[0].map((_,j)=>M.map(r=>ec(r[j])));
ck(mm(G,adj(G)).every((r,i)=>r.every((v,j)=>eq(v,E(i===j?1:0)))),"G unitary");
ck(mm(H,adj(H)).every((r,i)=>r.every((v,j)=>eq(v,E(i===j?1:0)))),"H unitary");
const Y=[E(1),E(2)],W=[E(3,6),E(4)];
return{Aalpha:outm(Aa),Agamma:outm(Ag),Aeta:outm(Ae),G:outm(G),H:outm(H),R_L:outm(refl),G_inv:outm(adj(G)),H_inv:outm(adj(H)),det_G:out(inverse(G).det),det_H:out(inverse(H).det),obs_G:[mm([Y],G)[0],mm([W],G)[0]].map(r=>r.map(out)),obs_H:[mm([Y],H)[0],mm([W],H)[0]].map(r=>r.map(out)),obs_R:[mm([Y],refl)[0],mm([W],refl)[0]].map(r=>r.map(out))};}
function checkHalfTrace(){"use strict";
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


const trace=[{name:"Tr((x-e)^4 e^2)",coefficients:{bX:"12",b2:"3"}},{name:"Tr((x-e)(x+2e)^3 e^2)",coefficients:{bX:"-15",b2:"-24"}}];
const binom=(n,k)=>{let v=1n;for(let j=1;j<=k;j++)v=v*BigInt(n-j+1)/BigInt(j);return v;};
function traceTerm(x,e,n){if(e%3)return null;const q=e/3;return {x,b:q,value:n*3n*(q%2?-1n:1n)};}
let t1={};for(let k=0;k<=4;k++){const a=traceTerm(4-k,k+2,binom(4,k)*(k%2?-1n:1n));if(a)t1[a.x+","+a.b]=String(a.value);}
let t2={};for(let k=0;k<=3;k++)for(let j=0;j<=1;j++){const a=traceTerm(4-k-j,k+j+2,binom(3,k)*(2n**BigInt(k))*(j?-1n:1n));if(a){const key=a.x+","+a.b;t2[key]=String(BigInt(t2[key]||0)+a.value);}}
ck(JSON.stringify(t1)===JSON.stringify({"3,1":"12","0,2":"3"}),"first half trace");
ck(t2["3,1"]==="-15"&&t2["0,2"]==="-24","second half trace");
const al=E(1,3),ga=E(3,1),de=E(1,2),r=esc(es(E(2),esc(de,6)),1,7),rb=ec(r);
const c=esc(em(al,es(E(2),rb)),1,12),d=esc(em(en(ec(al)),es(E(2),r)),1,12);
ck(eq(c,E(1,1,2))&&eq(d,E(0,1,2)),"exact two coefficients");
return {traces:trace,trace_polynomials:[t1,t2],c:out(c),d:out(d),P2_sigma8:"sigma(2z)^2/(12b)",P2_sigma8X:"sigma(2z)^2/6"};
}
function sigma13Polynomial(){"use strict";
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


const pow=(x,n)=>{let v=E(1);while(n--)v=em(v,x);return v;};
const g=E(4,1),g6=pow(g,6),g12=em(g6,g6);
const u=esc(ea(g6,E(167)),1,210);
const base=ea(ea(E(201,0,637),E(-13,0,245)),ea(E(-13,0,1801800),E(78,0,44100)));
const v=es(ea(esc(g12,-1,1801800),esc(u,11,30)),base);
return{gamma13:out(g),g6:out(g6),u:out(u),v:out(v),base:out(base)};
}
function certifyR541(){return {half_trace:checkHalfTrace(),full_theta_identity:checkExactPair8(),physical_frames:checkPairFrames(),sigma13:sigma13Polynomial(),jet_bound:{axis_degree:8,required_rectangle:[8,8],simultaneous_mu6_type:2,checked_total_degrees:[2,8,14]},normalization:{gamma:"3+omega",gamma13:"4+omega",alpha:"1+3omega",rho0:"-nu_sigma^tensor6/84",K8:"-R_L(2P2-I)",F1:"-sigma(gamma*l+m)*sigma(l-conj(gamma)*m)"}};}
if(typeof module!=="undefined"){module.exports={certifyR541};if(require.main===module){const report=certifyR541();require("fs").writeFileSync(__filename.replace(/\.js$/,".json"),JSON.stringify(report,null,2)+"\n");console.log("R541 complete half trace, 2/8/14 full identities and physical frames passed.");}}
