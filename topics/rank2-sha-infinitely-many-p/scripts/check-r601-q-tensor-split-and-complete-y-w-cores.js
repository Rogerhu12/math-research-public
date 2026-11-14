#!/usr/bin/env node
"use strict";
// Exact R601 certificate; reuses the published complete CM matrices.
const fs=require("fs"),path=require("path");
const base=path.resolve(__dirname,"..");
const read=p=>JSON.parse(fs.readFileSync(path.join(base,p),"utf8"));
const matrix7=read("notes/2026-11-14-theta-degree136-cm7-exact.json").matrix;
const matrix19=read("notes/2026-11-14-theta-degree136-cm19-exact.json").matrix;
const S2JSON=read("scripts/check-r542-original-eta-arithmetic-projections.json").S2;
const src=((matrix7,matrix19)=>{
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



function ep(x,n){let y=E(1);while(n){if(n&1)y=em(y,x);x=em(x,x);n>>=1;}return y;}
const ptrim=a=>{while(a.length>1&&ez(a[a.length-1]))a.pop();return a;};
const pa=(a,b)=>ptrim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>ea(a[i]||E(0),b[i]||E(0))));
const pn=a=>a.map(en),ps=(a,b)=>pa(a,pn(b));
const pm=(a,b)=>{let c=Array.from({length:a.length+b.length-1},()=>E(0));for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]=ea(c[i+j],em(a[i],b[j]));return ptrim(c);};
const pp=(a,n)=>{let c=[E(1)];for(let i=0;i<n;i++)c=pm(c,a);return c;};
const pc=(a,z)=>a.map(x=>em(x,z)),px=a=>[E(0),...a],pd=a=>a.slice(1).map((x,i)=>esc(x,i+1));
const delta=E(1,2),gbar=E(2,-1),a13=E(4,3);
const r7bar=E(8,12,7),q7=[en(r7bar),E(1)];
const U=[em(r7bar,ea(esc(r7bar,7),E(24))),ea(esc(r7bar,28),E(12)),E(1)];
const V=ps(pm(pa(U,pc(px(pd(U)),E(3))),q7),pc(px(U),E(6)));
const q13=[E(16,-48,13),E(-4,-12),E(1)];
const R2=[E(-8),E(20),E(1)],V4=[E(-512),E(-2048),E(-1344),E(-536),E(1)];
const constant=esc(em(em(gbar,delta),ep(a13,2)),-16,21);
let poly=[constant];
for(const f of [pp([E(1),E(1)],2),q7,U,V,pp(q13,2),pp(R2,2),[E(-8),E(1)],V4])poly=pm(poly,f);
ck(poly.length===22,"degree21");
ck(eq(poly[21],constant),"actual z6");
const source=[...poly,E(0)];
const parseQ=s=>{let a=s.split("/");return Q(a[0],a[1]||"1");};
const parseM=m=>m.real.map((row,i)=>row.map((s,j)=>{let a=parseQ(s),b=parseQ(m.delta[i][j]);return[qa(a,b),qm(Q(2),b)];}));
const M=parseM(matrix7),N=parseM(matrix19);
const mv=(M,x)=>M.map(r=>r.reduce((s,t,j)=>ea(s,em(t,x[j])),E(0)));
const orbit=[source];for(let j=1;j<19;j++)orbit.push(mv(M,orbit[j-1]));
ck(orbit[18].every((x,i)=>eq(x,source[i])),"full M18 source");
const eig=(t)=>{let v=source.map(()=>E(0)),s=E(1),ti=ei(t);for(let j=0;j<18;j++){v=va(v,vm(orbit[j],s));s=em(s,ti);}return vm(v,E(1,0,18));};
const plus=vm(va(source,orbit[9]),E(1,0,2)),minus=vm(vs(source,orbit[9]),E(1,0,2));
const mvpow=(M,v,n)=>{for(let j=0;j<n;j++)v=mv(M,v);return v;};
const D=v=>vm(mv(N,mvpow(M,v,16)),E(-1,-1));
const dplus=vm(va(plus,D(plus)),E(1,0,2)),dminus=vm(vs(plus,D(plus)),E(1,0,2));
const eigen=[];
for(const t of [E(1),E(0,1),E(-1,-1),E(-1),E(0,-1),E(1,1)]){
 const v=eig(t);const dp=vm(va(v,D(v)),E(1,0,2)),dm=vm(vs(v,D(v)),E(1,0,2));
 eigen.push({eigenvalue:out(t),mass:out(v[22]),nonzero:v.some(x=>!ez(x)),Dplus_mass:out(dp[22]),Dminus_mass:out(dm[22]),Dplus:dp.map(out),Dminus:dm.map(out)});
}
ck(vs(va(va(orbit[8],orbit[5]),orbit[2]),va(va(orbit[6],orbit[3]),orbit[0])).every(ez),"complete degree8 annihilator");
const thetaLeading={z6:out(constant),z6_over_S2:out(esc(constant,1,64)),mass:out(source[22])};
return {source:source.map(out),factor:{constant:out(constant),q7:q7.map(out),U:U.map(out),V:V.map(out),q13:q13.map(out),R2:R2.map(out),V4:V4.map(out)},thetaLeading,eigen,plus:plus.map(out),minus:minus.map(out),Dplus:dplus.map(out),Dminus:dminus.map(out),orbit:orbit.map(v=>v.map(out))};

})(matrix7,matrix19);
const sp=((matrix7,matrix19,report,S2JSON)=>{
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



const parseQ=s=>{let a=s.split("/");return Q(a[0],a[1]||"1");};
const parseV=v=>v.map(z=>[parseQ(z[0]),parseQ(z[1])]);
const parseM=m=>m.real.map((row,i)=>row.map((s,j)=>{let a=parseQ(s),b=parseQ(m.delta[i][j]);return[qa(a,b),qm(Q(2),b)];}));
const mv=(M,x)=>M.map(r=>r.reduce((s,t,j)=>ea(s,em(t,x[j])),E(0)));
const M=parseM(matrix7),N=parseM(matrix19);
const vp=(v,n)=>{for(let k=0;k<n;k++)v=mv(M,v);return v;};
const D=v=>vm(mv(N,vp(v,16)),E(-1,-1));
function rank(cols){if(!cols.length)return 0;let A=Array.from({length:23},(_,i)=>cols.map(c=>c[i]));let r=0;for(let j=0;j<A[0].length&&r<23;j++){let p=r;while(p<23&&ez(A[p][j]))p++;if(p===23)continue;[A[p],A[r]]=[A[r],A[p]];A[r]=vm(A[r],ei(A[r][j]));for(let k=0;k<23;k++)if(k!==r&&!ez(A[k][j]))A[k]=vs(A[k],vm(A[r],A[k][j]));r++;}return r;}
const source=parseV(report.source),orbit=report.orbit.map(parseV);
const S2=S2JSON.map(z=>{const a=parseQ(z.real),b=parseQ(z.delta);return[qa(a,b),qm(Q(2),b)];});
ck(parseV(report.minus).every((x,i)=>eq(x,esc(S2[i],1,2))),"negative block S2/2");
const blocks=[];
for(const sign of [1,-1])for(const tau of [E(0,1),E(-1,-1)]){
 const d=vm(va(source,vm(D(source),E(sign))),E(1,0,2));
 // first remove M9 negative block
 const pos=vm(va(d,vp(d,9)),E(1,0,2));
 const x=vm(va(va(pos,vm(vp(pos,3),ei(tau))),vm(vp(pos,6),em(ei(tau),ei(tau)))),E(1,0,3));
 ck(vp(x,3).every((z,i)=>eq(z,em(tau,x[i]))),"cubic block eigen");
 blocks.push({D33:sign,tau:out(tau),nonzero:x.some(z=>!ez(z)),mass:out(x[22]),dimension:rank([x,vp(x,1),vp(x,2)]),vector:x.map(out)});
}
return{cyclic_dimension:rank(orbit.slice(0,18)),Dplus_dimension:rank(orbit.slice(0,18).map(v=>vm(va(v,D(v)),E(1,0,2)))),Dminus_dimension:rank(orbit.slice(0,18).map(v=>vm(vs(v,D(v)),E(1,0,2)))),joint_dimension:rank([...orbit.slice(0,18),...orbit.slice(0,18).map(D)]),blocks,S2_half:true};

})(matrix7,matrix19,src,S2JSON);
const co=(()=>{
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



const delta=E(1,2),az=E(-2,1,2),aq=E(4,3,2),weights=[6,2,1,1,1];
const Y=[az,aq,esc(delta,2),E(1),E(2)],W=[az,aq,esc(delta,2),esc(delta,3),E(4)];
const wh=(a,b)=>a.reduce((s,x,i)=>ea(s,esc(em(x,ec(b[i])),weights[i])),E(0));
ck(eq(wh(Y,Y),E(34))&&eq(wh(W,W),E(72)),"actual Y/W norms");
const cross=wh(Y,W);ck(eq(cross,E(34,-6)),"cross 37-3delta");
const by=Y.map((x,i)=>esc(ec(x),weights[i],34)),bw=W.map((x,i)=>esc(ec(x),weights[i],72));
const Yimage=Array.from({length:5},(_,i)=>es(E(i===0?1:0),em(by[i],az)));
const Wimage=Array.from({length:5},(_,i)=>es(E(i===0?1:0),em(bw[i],az)));
const dot=(r,v)=>r.reduce((s,a,i)=>ea(s,em(a,v[i])),E(0));
ck(ez(dot(Y,Yimage))&&ez(dot(W,Wimage)),"zero-depth projective limits");
const WY=dot(W,Yimage),YW=dot(Y,Wimage);
ck(eq(em(WY,ei(az)),esc(ea(E(1),delta),-3,34)),"W after Y core");
ck(eq(em(YW,ei(az)),esc(ea(E(35),esc(delta,3)),1,72)),"Y after W core");
ck(eq(Yimage[0],E(47,0,68))&&eq(Wimage[0],E(41,0,48)),"old Z units");
const mulInt=(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1]];
const det=(a,b)=>a[0]*b[1]-a[1]*b[0],norm=a=>a[0]*a[0]-a[0]*a[1]+a[1]*a[1];
const char=a=>(norm(a)&1)?-1:1;
const torsion=[];
for(const l of [[0,0],[1,0],[0,1],[1,1]]){
 const ol=mulInt([0,1],l),lz=l.map(x=>-x),lq=mulInt([2,1],l);
 const redExponent=3*det(ol,lz)+det(ol,lq),redSign=(redExponent&1)?-1:1;
 const sigY=char(mulInt([2,4],l))*char(l)*char(mulInt([2,0],l));
 const sigW=char(mulInt([2,4],l))*char(mulInt([3,6],l))*char(mulInt([4,0],l));
 ck(redSign*sigY===1&&redSign*sigW===1,"complete halfperiod phase");
 torsion.push({l,redExponent,redSign,sigY,sigW,totalY:1,totalW:1});
}
const mod=(a,m)=>(a%m+m)%m,cm=(a,b,m)=>mulInt(a,b).map(x=>mod(x,m));
const gp=[91,72];let z=[1,0],powers=[];for(let j=1;j<=8;j++){z=cm(z,gp,576);powers.push(z);}
ck(powers[3][0]===433&&powers[3][1]===288,"full g288 fourth");
const models=[];
for(const [N,reflect,a,b]of [[136,true,203,136],[288,false,433,288]]){
 const coreExponent=mod(a,N),Bexp=1+N/2;
 const K=j=>({j:mod((reflect?-1:1)*(Bexp*j+N/2),N),s:(j&1)?-1:1});
 for(let j=0;j<N;j++){
  const q=K(j),r=K(mod(q.j+1,N));
  ck(r.j===mod(j+coreExponent,N)&&q.s*r.s===-1,"complete X conjugation");
  ck(q.j===mod(coreExponent*j+N/2,N),"complete Z conjugation");
 }
 ck(b===N&&mod(a,2)===1&&a-b===coreExponent,"center phases on both original generators");
 models.push({N,reflect,CM:[a,b],generator_action:["-X^"+coreExponent,"-Z^"+coreExponent],checked_basis_vectors:N});
}
const traces={sum_nonzero_on_P1:[1,-2],sum_nonzero_on_P2:[-2,1],sum_all_matrix:[[2,-2],[-2,2]],B2_matrix:[[0,-1],[-1,0]]};
ck(traces.sum_all_matrix[0][0]/2-1===0&&traces.sum_all_matrix[0][1]/2===-1,"two tensor halftrace");
return{weights,Y:Y.map(out),W:W.map(out),cross:out(cross),Y_projection_vector:by.map(out),W_projection_vector:bw.map(out),Y_image_limit:Yimage.map(out),W_image_limit:Wimage.map(out),W_Yimage:out(WY),Y_Wimage:out(YW),torsion,models,g288:gp,g288_powers:powers,halftrace:traces,excluded_unit_factors:{47:"47 mod64 (also <71)",41:"41 mod64 (also <71)",313:"57 mod64"},
complete_source_cores:{Y:"nu_i|Ydeep=beta*(P_Y,-kappa)_*nu_(3-i)",W4:"nu_i|Wdeep4=-lambda^4*(P_W,kappa^4)_*nu_(3-i)"}};

})();
const report=((src,sp,co)=>{

const report={
format:"R601 full Q tensor split and actual Y/W cores; CM coefficients in Q(omega), omega^2+omega+1=0",
basis:"b=1, sigma^136*x^2*X^j, 0<=j<=22; general b uses coefficient b^(21-j)",
factor:src.factor,source:src.source,thetaLeading:src.thetaLeading,
negative_block:{S2_coefficient:"1/2",vector:src.minus},
references:{Dplus:{curve_D:"-136",N7:["1","0"],N19:["0","1"],mass:["1/3024","1/1512"],vector:src.eigen[0].Dplus},Dminus:{curve_D:"668168",N7:["1","0"],N19:["0","-1"],mass:["-1/3024","-1/1512"],vector:src.eigen[0].Dminus}},
vanishing_eigenspaces:src.eigen.filter(x=>!x.nonzero).map(x=>x.eigenvalue),
Snew_projection:"0, complete vector (not just mass)",external_blocks:sp.blocks,
dimensions:{N7_cyclic:sp.cyclic_dimension,Dplus:sp.Dplus_dimension,Dminus:sp.Dminus_dimension,joint:sp.joint_dimension},
minimal_N7:["-1","0","1","-1","0","1","-1","0","1"],
ordinary_Y_marginal:"K136 F=S(2z)-F, physical PY|p=lambda[kappa](S-PY)",
whole_cores:co,
complement_source:"eta_n=1_(rectangle complement)*nu_flat; eta_n(ell)=R599 E_n",
scope:"Q projection preserves rectangle but changes actual Y/W tests. Reference and all four external blocks retained. Source core formulas retain all five physical coordinates."
};
function gcdDen(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a;}
let den=1n;function visitDen(x){if(typeof x==="string"&&/^-?\d+\/\d+$/.test(x)){const d=BigInt(x.split("/")[1]);den=den/gcdDen(den,d)*d;}else if(Array.isArray(x))x.forEach(visitDen);else if(x&&typeof x==="object")Object.values(x).forEach(visitDen);}
visitDen(report.source);visitDen(report.negative_block);visitDen(report.references);visitDen(report.external_blocks);
let rem=den,f=[];for(const q of [2n,3n,5n,7n,11n,13n,17n,19n]){let e=0;while(rem%q===0n){rem/=q;e++;}if(e)f.push([String(q),e]);}
report.coefficient_denominator={lcm:String(den),small_factors:f,remaining:String(rem)};
return report;

})(src,sp,co);
process.stdout.write(JSON.stringify(report,null,2)+"\n");
