#!/usr/bin/env node
/* R531 exact certificate. Pure BigInt Q(omega); no external dependencies. */
function certifyR531(){"use strict";
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


const om=E(0,1),om2=E(-1,-1),del=E(1,2),ga=E(3,1),gb=E(2,-1);
const Y=[del,E(2,4),ga,gb,E(1),E(2)];
const W=[del,E(2,4),ga,gb,E(3,6),E(4)];
const Wp=[E(4,4),E(2,4),E(4,4),E(0),E(4,2),E(4)];
const W2=[ga,E(2,4),E(6,3),E(3,2),E(-1,1),E(4)];
const H0=[E(1),E(0),E(-1),E(1),E(0),E(0)];
const H1=[E(-1),E(2),om,E(1,1),E(0),E(0)];
const D=[E(1),om2,E(0,-2),E(0),E(1),E(2,3)];
const C=vm(H0,ei(del)),F=va(D,C),EA=va(F,vm(C,E(13)));
const G=va(vm(H1,E(13)),vm(F,E(3,-2)));
const rows={Y,W,Wp,W2,H0,H1,C,F,D,E:EA,G};
for(const row of [C,F,D,EA,G])for(const obs of [Y,W,Wp])ck(ez(he(row,obs)),"hidden/observer orthogonality");
for(const pair of [[C,F],[D,EA],[G,C],[G,F],[G,D],[G,EA]])ck(ez(he(pair[0],pair[1])),"hidden orthogonality");
ck(eq(he(C,C),E(1))&&eq(he(F,F),E(13))&&eq(he(D,D),E(14))&&eq(he(EA,EA),E(182))&&eq(he(G,G),E(936)),"degrees");
const FC=[Y,W,Wp,C,F,G],FD=[Y,W,Wp,D,EA,G];
const invC=inverse(FC),invD=inverse(FD);
ck(mm(FC,invC.inverse).every((row,i)=>row.every((x,j)=>eq(x,E(i===j?1:0)))),"frame C inverse");
ck(mm(FD,invD.inverse).every((row,i)=>row.every((x,j)=>eq(x,E(i===j?1:0)))),"frame D inverse");
function binom(n,k){let a=1n;for(let i=1;i<=k;i++)a=a*BigInt(n-i+1)/BigInt(i);return a;}
function pmul(a,b){let r=Array.from({length:a.length+b.length-1},()=>E(0));a.forEach((x,i)=>b.forEach((y,j)=>r[i+j]=ea(r[i+j],em(x,y))));return r;}
function ppow(a,n){let r=[E(1)];for(let i=0;i<n;i++)r=pmul(r,a);return r;}
const first=ppow([E(1),E(-1)],6).map(x=>esc(x,-1,8));
const second=pmul(ppow([E(1),E(-1)],2),ppow([E(1),E(13)],4)).map(x=>esc(x,3,8*11*13**3));
const q=first.map((x,i)=>ea(x,second[i]));
ck(eq(q[5],E(0))&&eq(q[4],E(-483,0,286)),"fifth cancellation and q4");
const inds=[0,1,2,4,5],di=inds.map(i=>D[i]),ei5=inds.map(i=>EA[i]);
function c4(v){let s=E(0);for(let i=0;i<5;i++){let t=v[i];for(let j=0;j<5;j++)if(j!==i)t=em(t,di[j]);s=ea(s,t);}return esc(s,24);}
const e0=EA[3],cE=c4(ei5),mass=esc(em(em(q[4],esc(e0,2)),cE),-1,84*14**6);
const alpha={},c4obs={};
for(const [name,row] of Object.entries({Y,W,W2})){
 c4obs[name]=c4(inds.map(i=>row[i]));
 alpha[name]=esc(em(em(em(q[4],em(e0,e0)),ei(row[3])),c4obs[name]),-1,84*14**6);
}
const deltaWY=es(em(alpha.W,ei(esc(del,6))),alpha.Y);
const deltaW2Y=es(em(alpha.W2,ei(esc(em(del,om2),-6))),alpha.Y);
function fact(n){n=abs(BigInt(n));const a=[];for(let p=2n;p*p<=n;p+=(p===2n?1n:2n)){if(n%p===0n){let e=0;while(n%p===0n){n/=p;e++;}a.push([String(p),e]);}if(p>100000n)break;}if(n>1n)a.push([String(n),1]);return a;}
function nf(x){const n=em(x,ec(x));ck(n[1][0]===0n,"rational norm");return{value:out(n),numerator_factors:fact(n[0][0]),denominator_factors:fact(n[0][1])};}
const PI4=[Y,W,Wp,G];

const ci=vm(C,del),fi=vm(F,E(3)),de=vm(D,E(1)),ee=vm(EA,E(3));
function oddcount(row){let count=0;for(const x of row){ck(x.every(q=>q[1]===1n),"integer halfchar row");if(x.some(q=>q[0]%2n!==0n))count++;}return count;}
function coeffMixed(a,b,k){
 let sum=E(0);
 for(let mask=0;mask<32;mask++){
  let bits=0,t=E(1);
  for(let j=0;j<5;j++){if(mask&(1<<j)){bits++;t=em(t,a[j]);}else t=em(t,b[j]);}
  if(bits===k)sum=ea(sum,t);
 }
 let fac=1n;for(let j=2;j<=k;j++)fac*=BigInt(j);for(let j=2;j<=5-k;j++)fac*=BigInt(j);
 return esc(sum,fac);
}
const completeMass=[];
for(let k=0;k<=4;k++){
 const mix=coeffMixed(di,ei5,k);
 const m=esc(em(em(q[k],e0),mix),-(6-k),84*14**6);
 completeMass.push({k,r:5-k,full_squarefree_coefficient:out(mix),coefficient:out(m),euler_denominator_power:6-k});
}
ck(eq(mass,esc(em(em(q[4],e0),coeffMixed(di,ei5,4)),-2,84*14**6)),"full mass leading coefficient");
ck(eq(alpha.Y,E(-414,-621,38454416)),"displayed alpha Y");
ck(eq(mass,E(345,759,19227208)),"displayed mass");
const normsToExclude=[alpha.Y,alpha.W,alpha.W2,mass,deltaWY,deltaW2Y];
const smallBad=[...new Set(normsToExclude.flatMap(x=>nf(x).numerator_factors.map(a=>a[0])))];
ck(smallBad.every(q=>BigInt(q)%64n!==7n),"all numerator prime exceptions excluded by current p=7 mod64 ray");
const g64=esc(em(E(-1,2),E(-1,2)),1,7);
function modQ(q,m){const p=BigInt(m);let a=q[1],b=p,u=1n,v=0n;while(b){let c=a/b;[a,b]=[b,a-c*b];[u,v]=[v,u-c*v];}ck(a===1n||a===-1n,"mod rational unit");if(a===-1n)u=-u;return Number(((q[0]*u)%p+p)%p);}
ck(g64.map(x=>modQ(x,64)).join(",")==="27,8","original complete ratio mod64");
const levels=[
 {name:"C via H0",degree:3,modulus:6,g:[1,0],anchors:[1,2],anchor_kind:"sigma(delta z)",full_core:"beta=-lambda"},
 {name:"F via [3]",degree:117,modulus:234,g:[1,0],anchors:[12,3],anchor_kind:"sigma(3 gamma13 z)",full_core:"beta=-lambda"},
 {name:"D",degree:14,modulus:28,g:[15,0],anchors:[3,1],anchor_kind:"Theta(gamma7 z)",full_core:"beta=-lambda"},
 {name:"E via [3]",degree:1638,modulus:3276,g:[1639,0],anchors:[33,18],anchor_kind:"Theta(3 gamma7 gamma13 z)",full_core:"beta=-lambda"}
];
for(const L of levels){
 const a=E(...L.anchors),norm=he([a],[a]);
 ck(eq(norm,E(L.anchor_kind.startsWith("Theta")?L.degree/2:L.degree)),"absolute anchor degree "+L.name);
 ck(L.g[0]%2===1&&L.g[1]===0,"dyadic parity");
 if(L.modulus%4===0)ck(L.g[0]%4===3,"complete mod4 centre");
 if(L.modulus%9===0)ck(L.g[0]%9===1,"mod9 ray");
 if(L.modulus%7===0)ck(L.g[0]%7===1,"mod7 ray");
 if(L.modulus%13===0)ck(L.g[0]%13===1,"mod13 ray");
}
const report={format:"exact Q(omega), omega^2+omega+1=0; row order xi1,xi2,xi3,x,c,d0",
 rows:Object.fromEntries(Object.entries(rows).map(([k,v])=>[k,v.map(out)])),
 frames:{CF:{matrix:FC.map(r=>r.map(out)),inverse:invC.inverse.map(r=>r.map(out)),det:out(invC.det),det_norm:nf(invC.det)},
 DE:{matrix:FD.map(r=>r.map(out)),inverse:invD.inverse.map(r=>r.map(out)),det:out(invD.det),det_norm:nf(invD.det)}},
 gram:FD.map(x=>FD.map(y=>out(he(x,y)))),
 actual_integer_axes:{C_delta:ci.map(out),F_three:fi.map(out),D:de.map(out),E_three:ee.map(out)},
 actual_degrees:[ci,fi,de,ee].map(row=>out(he(row,row))),
 actual_halfcharacter_odd_counts:[ci,fi,de,ee].map(oddcount),
 q_in_DE_before_factor14minus6:q.map(out),
 whole_core_levels:levels, original_g_mod64:g64.map(x=>modQ(x,64)), complete_mass_polynomial:completeMass, unit_numerator_primes:smallBad,
 coefficients:{c4E:out(cE),c4obs:Object.fromEntries(Object.entries(c4obs).map(([k,v])=>[k,out(v)])),e0:out(e0),
 mass:out(mass),mass_norm:nf(mass),alpha:Object.fromEntries(Object.entries(alpha).map(([k,v])=>[k,{value:out(v),norm:nf(v)}])),
 deltaWY:{value:out(deltaWY),norm:nf(deltaWY)},deltaW2Y:{value:out(deltaW2Y),norm:nf(deltaW2Y)}}
 };
return report;
}
if(typeof module!=="undefined"){
 module.exports={certifyR531};
 if(require.main===module){
  const report=certifyR531();
  require("fs").writeFileSync(__filename.replace(/\.js$/,".json"),
    JSON.stringify(report,null,2)+"\n");
  console.log("R531 exact certificate passed.");
 }
}
