#!/usr/bin/env node
/* R539: whole degree-eight core, original two-sigma pair, and exact mixed S/T word. */
function certifyR539(){"use strict";
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


const om=E(0,1),om2=E(-1,-1),del=E(1,2),ga=E(3,1),gb=E(2,-1),al=E(1,3);
const L=[E(0),E(0),E(0),E(0),al,E(1)],M=[E(0),E(0),E(0),E(0),E(1),en(ec(al))];
const A=[del,E(2,4),ga,gb,E(0),E(0)],Y=va(A,[E(0),E(0),E(0),E(0),E(1),E(2)]),
W=va(A,[E(0),E(0),E(0),E(0),E(3,6),E(4)]);
const a=E(0,-3,8),bb=E(-1,-6,8),aw=ea(a,E(2));
ck(eq(he(L,L),E(8))&&eq(he(M,M),E(8))&&ez(he(L,M)),"complete pair Gram");
ck(va(va(A,vm(L,a)),vm(M,bb)).every((x,i)=>eq(x,Y[i])),"original Y decomposition");
ck(va(Y,vm(L,E(2))).every((x,i)=>eq(x,W[i])),"W-Y=2L");
const frame=[...ident(6).slice(0,4),L,M],fi=inverse(frame);ck(eq(fi.det,E(-8)),"pair determinant");
const H0=[E(1),E(0),E(-1),E(1),E(0),E(0)],H1=[E(-1),E(2),om,E(1,1),E(0),E(0)],
D=[E(1),om2,E(0,-2),E(0),E(1),E(2,3)],C=vm(H0,ei(del)),F=va(D,C),G=va(vm(H1,E(13)),vm(F,E(3,-2)));
for(const h of[C,F,G])ck(ez(he(h,L)),"R536 complete test fixed along L");
const ci=(a,b=0)=>[a,b],ca=(x,y)=>[x[0]+y[0],x[1]+y[1]],cs=(x,y)=>[x[0]-y[0],x[1]-y[1]],cm=(x,y)=>[x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]],
ce=(x,y)=>x[0]===y[0]&&x[1]===y[1],cd=(x,a)=>[x[0]/a,x[1]/a],phase=e=>[ci(1),ci(0,1),ci(-1),ci(0,-1)][((e%4)+4)%4],
zero8=()=>Array.from({length:8},()=>Array.from({length:8},()=>ci(0))),
eye8=()=>Array.from({length:8},(_,i)=>Array.from({length:8},(_,j)=>ci(i===j?1:0)));
const matmul=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((v,x,k)=>ca(v,cm(x,B[k][j])),ci(0))));
const quarter=zero8(),half=zero8(),terms=[];
for(let s=0;s<4;s++)for(let r=0;r<4;r++){
 const cols=[];
 for(let j=0;j<8;j++){
  const target=(j+2*r)%8,exponent=(s*(j+r))%4;
  quarter[target][j]=ca(quarter[target][j],phase(exponent));
  if(s%2===0&&r%2===0)half[target][j]=ca(half[target][j],phase(exponent));
  cols.push({column:j,target,phase_i:exponent});
 }
 terms.push({s,r,columns:cols});
}
const K=quarter.map((row,i)=>row.map((x,j)=>cs(cd(x,4),cd(half[i][j],2))));
const B=zero8(),R=zero8();
for(let j=0;j<8;j++){B[(3*j+4)%8][j]=ci(j%2?-1:1);R[(8-j)%8][j]=ci(1);}
const J=half.map((row,i)=>row.map((x,j)=>cs(cd(x,2),ci(i===j?1:0))));
ck(K.every((row,i)=>row.every((x,j)=>ce(x,cd(B[i][j],-1)))),"full quarter K=-B");
ck(matmul(K,K).every((row,i)=>row.every((x,j)=>ce(x,ci(i===j?1:0)))),"K8 squared identity");
const RJ=matmul(R,J);ck(K.every((row,i)=>row.every((x,j)=>ce(x,cd(RJ[i][j],-1)))),"K=-R J2");
const pullback2=[Array.from({length:8},(_,i)=>ci(i===0||i===4?1:0)),Array.from({length:8},(_,i)=>ci(i===2||i===6?1:0))];
for(const v of pullback2){const w=matmul(B,v.map(x=>[x])).map(r=>r[0]);ck(w.every((x,j)=>ce(x,v[j])),"B fixed E2 subspace");}
for(let j=0;j<8;j++){ck(((4+3*((3*j+4)%8)-j)%8+8)%8===0,"Z intertwiner exponent");ck(((3*(j+1)+4)-(3*j+4)-3)%8===0,"X intertwiner target");}
const g=E(11,8),g2=em(g,g),normg=em(g,ec(g));ck(Number(g2[0][0]%16n)===9&&Number(g2[1][0]%16n)===0&&Number(normg[0][0]%16n)===1,"whole modulus sixteen");
const inds=[0,1,2,4,5],df=inds.map(i=>D[i]),lf=inds.map(i=>L[i]);
function c4(v){let s=E(0);for(let i=0;i<5;i++){let t=v[i];for(let j=0;j<5;j++)if(j!==i)t=em(t,df[j]);s=ea(s,t);}return esc(s,24);}
const cL=c4(lf);ck(eq(cL,E(288)),"actual mixed L coefficient");
const alphaL=esc(em(cL,ei(gb)),-1,84),bY=em(a,alphaL),bW=em(aw,alphaL);
ck(eq(bY,E(-9,18,49))&&eq(bW,E(-153,-30,49)),"fixed amplified coefficients");
const pL=L.map(x=>ec(x)).map(x=>L.map(y=>esc(em(x,y),1,8)));
return{
 format:"Exact Q(omega) geometry and exact Gaussian-integer 8-state Heisenberg matrices",
 row_order:["xi1","xi2","xi3","x","c","d0"],
 alpha:out(al),A:A.map(out),L:L.map(out),M:M.map(out),Y:Y.map(out),W:W.map(out),
 pair_frame:frame.map(r=>r.map(out)),pair_inverse:fi.inverse.map(r=>r.map(out)),pair_det:out(fi.det),
 pair_gram:[L,M].map(r=>[L,M].map(s=>out(he(r,s)))),
 first_observation_coefficients:{Y_L:out(a),Y_M:out(bb),W_L:out(aw),W_M:out(bb)},
 g_mod16:out(g),g_squared_mod16:["9","0"],
 quarter_lifts:terms,K8:K,B8:B,R8:R,J2:J,pullback_degree2_basis:pullback2,
 physical_rank_one_projector:pL.map(r=>r.map(out)),
 amplified_leading:{c4L:out(cL),alphaL:out(alphaL),bY:out(bY),bY_norm:out(em(bY,ec(bY))),bW:out(bW),bW_norm:out(em(bW,ec(bW)))},
 source_checks:["K8=-B8=-R8*J2","K8^2=I","Theta(2z) belongs to the displayed E2-fixed subspace","L,M have integral determinant -8","C,F,G are all orthogonal to L"]
};
}
if(typeof module!=="undefined"){
 module.exports={certifyR539};
 if(require.main===module){
  const report=certifyR539();
  require("fs").writeFileSync(__filename.replace(/\.js$/,".json"),JSON.stringify(report,null,2)+"\n");
  console.log("R539 full sixteen-lift core and original mixed-source certificate passed.");
 }
}
