#!/usr/bin/env node
/* R536: exact original six-input fibre mass compensation. Pure BigInt arithmetic. */
function buildR536Matrix(){"use strict";
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


const del=E(1,2),gb=E(2,-1),H0=[E(1),E(0),E(-1),E(1),E(0),E(0)],H1=[E(-1),E(2),E(0,1),E(1,1),E(0),E(0)];
const D=[E(1),E(-1,-1),E(0,-2),E(0),E(1),E(2,3)],C=vm(H0,ei(del)),F=va(D,C),EA=va(F,vm(C,E(13))),G=va(vm(H1,E(13)),vm(F,E(3,-2)));
const inds=[0,1,2,4,5],rows=[D,EA,G].map(r=>inds.map(i=>r[i])),e0=EA[3],g0=G[3];
function mulLin(arr,L){const outa=Array.from({length:32},()=>E(0));for(let s=0;s<32;s++)if(!ez(arr[s]))for(let i=0;i<5;i++)if(!(s&(1<<i)))outa[s|(1<<i)]=ea(outa[s|(1<<i)],em(arr[s],L[i]));return outa;}
const sqcache={};
function sf(a,b,c){const key=[a,b,c].join(",");if(sqcache[key])return sqcache[key];if(a<0||b<0||c<0)return E(0);let r=Array.from({length:32},()=>E(0));r[0]=E(1);[a,b,c].forEach((n,i)=>{for(let j=0;j<n;j++)r=mulLin(r,rows[i]);});return sqcache[key]=r[31];}
function p3mul(A,B){const r={};for(const [ka,a] of Object.entries(A))for(const[kb,b]of Object.entries(B)){const ia=ka.split(",").map(Number),ib=kb.split(",").map(Number),k=ia.map((x,i)=>x+ib[i]).join(",");r[k]=ea(r[k]||E(0),em(a,b));}return r;}
function p3pow(P,n){let r={"0,0,0":E(1)};for(let i=0;i<n;i++)r=p3mul(r,P);return r;}
const cp={"1,0,0":E(-1,0,14),"0,1,0":E(1,0,14)},fp={"1,0,0":E(13,0,14),"0,1,0":E(1,0,14)},gp={"0,0,1":E(1)};
function polynomial(i,j,k){return p3mul(p3mul(p3pow(cp,i),p3pow(fp,j)),p3pow(gp,k));}
function epow(x,n){let r=E(1);for(let i=0;i<n;i++)r=em(r,x);return r;}
const exps=[];for(const i of[2,4,5])for(let j=0;j<=6-i;j++)exps.push([i,j,6-i-j]);
const base=Object.fromEntries(Object.entries(polynomial(6,0,0)).map(([k,v])=>[k,esc(v,-1,8)])),polys=exps.map(v=>polynomial(...v));
function rowsFor(P){const a0=Array.from({length:7},()=>E(0)),a1=Array.from({length:7},()=>E(0));for(const[key,coef]of Object.entries(P)){const[k,j,l]=key.split(",").map(Number);let row=j===0?a1:a0;if(k<=5){let f=E(0);if(j>0)f=ea(f,esc(em(e0,sf(k,j-1,l)),j));if(l>0)f=ea(f,esc(em(g0,sf(k,j,l-1)),l));row[k]=ea(row[k],em(coef,f));}if(k===4)row[6]=ea(row[6],em(coef,em(epow(e0,j),epow(g0,l))));}return[a0,a1];}
const BR=rowsFor(base),PR=polys.map(rowsFor),A0=Array.from({length:7},(_,i)=>PR.map(x=>x[0][i])),A1=Array.from({length:7},(_,i)=>PR.map(x=>x[1][i]));
const b0=BR[0].map((v,i)=>es(E(i===6?1:0),v)),b1=BR[1].map(en);
function rowsAtPower(P,power){
 const outa=Array.from({length:7},()=>E(0));
 for(const[key,coef]of Object.entries(P)){
  const[k,j,l]=key.split(",").map(Number);if(j!==power)continue;
  if(k<=5){
   let f=E(0);
   if(j>0)f=ea(f,esc(em(e0,sf(k,j-1,l)),j));
   if(l>0)f=ea(f,esc(em(g0,sf(k,j,l-1)),l));
   outa[k]=ea(outa[k],em(coef,f));
  }
  if(k===4)outa[6]=ea(outa[6],em(coef,em(epow(e0,j),epow(g0,l))));
 }
 return outa;
}
const powerMatrices=Array.from({length:7},(_,j)=>Array.from({length:7},(_,i)=>polys.map(P=>rowsAtPower(P,j)[i])));
const fixedPowerVectors=Array.from({length:7},(_,j)=>rowsAtPower(base,j));
for(let i=0;i<7;i++)for(let k=0;k<10;k++){
 ck(eq(powerMatrices[0][i][k],A1[i][k]),"zeroth E power");
 ck(eq(powerMatrices.slice(1).reduce((s,M)=>ea(s,M[i][k]),E(0)),A0[i][k]),"positive E powers");
}

return{raw:{A0,A1,b0,b1,exps,base,polys,rows,e0,g0,BR,powerMatrices,fixedPowerVectors},display:{exps,powerMatrices:powerMatrices.map(M=>M.map(r=>r.map(out))),fixedPowerVectors:fixedPowerVectors.map(v=>v.map(out)),A0:A0.map(r=>r.map(out)),A1:A1.map(r=>r.map(out)),b0:b0.map(out),b1:b1.map(out),e0:out(e0),g0:out(g0)}};
}
function polynomialRightInverseR536(raw){"use strict";
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



const {A0,A1}=raw;
function solve(degree){
 const nr=7*(degree+2),nc=10*(degree+1);
 let M=Array.from({length:nr},()=>Array.from({length:nc+7},()=>E(0)));
 for(let h=0;h<=degree;h++)for(let i=0;i<7;i++)for(let j=0;j<10;j++){M[7*h+i][10*h+j]=A0[i][j];M[7*(h+1)+i][10*h+j]=A1[i][j];}
 for(let i=0;i<7;i++){M[i][nc+i]=E(-1);M[7+i][nc+i]=E(1);}
 let rank=0,piv=[];
 for(let col=0;col<nc&&rank<nr;col++){
  let p=rank;while(p<nr&&ez(M[p][col]))p++;if(p===nr)continue;
  [M[p],M[rank]]=[M[rank],M[p]];
  const inv=ei(M[rank][col]);for(let j=col;j<nc+7;j++)M[rank][j]=em(M[rank][j],inv);
  for(let i=rank+1;i<nr;i++)if(!ez(M[i][col])){const f=M[i][col];for(let j=col+1;j<nc+7;j++)M[i][j]=es(M[i][j],em(f,M[rank][j]));M[i][col]=E(0);}
  piv.push(col);rank++;
 }
 for(let i=rank;i<nr;i++)if(M[i].slice(nc).some(x=>!ez(x)))return{degree,rank,columns:nc,rows:nr,consistent:false};
 let sol=Array.from({length:nc},()=>Array.from({length:7},()=>E(0)));
 for(let i=rank-1;i>=0;i--){const c=piv[i];for(let j=0;j<7;j++){let v=M[i][nc+j];for(let k=c+1;k<nc;k++)if(!ez(M[i][k]))v=es(v,em(M[i][k],sol[k][j]));sol[c][j]=v;}}
 const B=Array.from({length:degree+1},(_,h)=>sol.slice(10*h,10*(h+1)));
 for(let h=0;h<=degree+1;h++){
  const r0=h<=degree?mm(A0,B[h]):Array.from({length:7},()=>Array.from({length:7},()=>E(0)));
  const r1=h>0?mm(A1,B[h-1]):Array.from({length:7},()=>Array.from({length:7},()=>E(0)));
  ck(r0.every((row,i)=>row.every((x,j)=>eq(ea(x,r1[i][j]),E(i===j?(h===0?-1:h===1?1:0):0)))),"polynomial right inverse coefficient "+h);
 }
 let den=1n,count=0,maxlen=0;for(const mat of B)for(const row of mat)for(const x of row){if(!ez(x))count++;for(const q of x){den=den/gcd(den,q[1])*q[1];maxlen=Math.max(maxlen,abs(q[0]).toString().length,q[1].toString().length);}}
 return{degree,rank,columns:nc,rows:nr,consistent:true,B:B.map(M=>M.map(r=>r.map(out))),fixed_denominator:String(den),nonzero_CM_entries:count,max_fraction_digits:maxlen,pivots:piv};
}
const result=solve(1);ck(result.consistent,"degree-one polynomial right inverse exists");return result;
}
function extraGeometryR536(){"use strict";
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
const H0=[E(1),E(0),E(-1),E(1),E(0),E(0)],H1=[E(-1),E(2),om,E(1,1),E(0),E(0)];
const D=[E(1),om2,E(0,-2),E(0),E(1),E(2,3)],C=vm(H0,ei(del)),F=va(D,C),EA=va(F,vm(C,E(13))),G=va(vm(H1,E(13)),vm(F,E(3,-2)));
const TI=[[en(om),E(1),om2,om],[en(om2),en(om),E(1),en(om2)],[E(-1),en(om2),en(om),E(1)],[en(om),E(1),en(om2),en(om)]].map(r=>r.map(x=>esc(x,1,2)));
const ix=[0,2,3,4],T=ident(6);for(let i=0;i<4;i++)for(let j=0;j<4;j++)T[ix[i]][ix[j]]=TI[i][j];
ck(mm([C],T)[0].every((x,j)=>eq(x,em(om2,C[j]))),"C T=omega2 C");
ck(mm([F],T)[0].every((x,j)=>eq(x,F[j])),"F T=F");
ck(mm([G],T)[0].every((x,j)=>eq(x,G[j])),"G T=G");
const roots=[E(1),om2,om],Ds=roots.map(z=>vs(F,vm(C,z))),Es=roots.map(z=>va(F,vm(C,esc(z,13))));
for(let j=0;j<3;j++){ck(mm([Ds[j]],T)[0].every((x,k)=>eq(x,Ds[(j+1)%3][k])),"D orbit");ck(Ds[j].every(e=>e.every(q=>q[1]===1n)),"integer D orbit");}
const alpha={Y:esc(em(E(216,216),ei(gb)),-1,84),W:esc(em(E(792,216),ei(gb)),-1,84),W2:esc(em(E(288,216),ei(E(3,2))),-1,84)};
const delta1=es(em(alpha.W,ei(esc(del,6))),alpha.Y),delta2=es(em(alpha.W2,ei(esc(em(del,om2),-6))),alpha.Y);
return{T:T.map(r=>r.map(out)),D_orbit:Ds.map(r=>r.map(out)),E_orbit:Es.map(r=>r.map(out)),alpha:Object.fromEntries(Object.entries(alpha).map(([k,v])=>[k,{value:out(v),norm:out(em(v,ec(v)))}])),deltas:[delta1,delta2].map(v=>({value:out(v),norm:out(em(v,ec(v)))}))};
}
function certifyR536(){
 const matrix=buildR536Matrix();
 const inverse=polynomialRightInverseR536(matrix.raw);
 const geometry=extraGeometryR536();
 const expected="4537451588264139836451244660234336276993718104462606281191442193986936120";
 if(inverse.fixed_denominator!==expected)throw Error("fixed denominator changed");
 return {
  format:"R536 exact Q(omega), omega^2+omega+1=0; no samples used in the proof.",
  matrix:matrix.display,
  polynomial_right_inverse:inverse,
  geometry,
  definitions:{
   tau:"tau=1/(1+lambda)",
   euler_weights:"u_j=1/(1+lambda*kappa^j), 0<=j<=6",
   actual_matrix:"A_p=sum_j u_j powerMatrices[j]",
   actual_target:"b_p=e_6-sum_j u_j fixedPowerVectors[j]",
   residue_matrix:"A(tau)=A0+tau*A1",
   residue_right_inverse:"B(tau)=(B[0]+tau*B[1])/(tau-1)",
   exact_identities:["A0*B[0]=-I7","A0*B[1]+A1*B[0]=I7","A1*B[1]=0"],
   actual_right_inverse:"B_p=B(tau)*(A_p*B(tau))^(-1)",
   coefficients:"x_p=B_p*b_p",
   source_polynomial:"Q_p=-C^6/8+sum_j x_p[j] C^exps[j][0] F^exps[j][1] G^exps[j][2]",
   excluded_fixed_integer:"2*3*7*13*17*"+expected
  }
 };
}
if(typeof module!=="undefined"){
 module.exports={certifyR536};
 if(require.main===module){
  const report=certifyR536();
  require("fs").writeFileSync(__filename.replace(/\.js$/,".json"),
    JSON.stringify(report,null,2)+"\n");
  console.log("R536 exact source, seven-row matrix, and polynomial right inverse passed.");
 }
}
