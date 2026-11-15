// R650. Exact original-coordinate certificate; Node.js, no packages.
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



function certificate(){

const del=E(1,2),om=E(0,1),om2=E(-1,-1);
const A=[del,em(E(2),del),E(3,1),E(2,-1),E(0),E(0)];
const Q5=[E(0),E(0),E(0),E(0),E(1),E(2)],L5=[E(0),E(0),E(0),E(0),E(2),E(-1)];
const Y=va(A,Q5),W=va(A,[E(0),E(0),E(0),E(0),em(E(3),del),E(4)]);
const C=vm([E(1),E(0),E(-1),E(1),E(0),E(0)],ei(del));
const Dc=[E(1),om2,E(0,-2),E(0),E(1),E(2,3)];
const F=va(Dc,C),g=E(3,-2);
const H1=[E(-1),E(2),om,E(1,1),E(0),E(0)],G=va(vm(H1,E(13)),vm(F,g));
const a=E(-5,-6,29),bF=E(5,6,5),f0=vs(vs(F,vm(A,a)),vm(Q5,bF)),f1=vs(F,vm(Q5,bF));
const d0=vs(f0,C),d1=vs(f1,C),ehat=va(f1,vm(C,E(34,0,5)));
ck(eq(he(d1,d1),E(39,0,5))&&ez(he(d1,ehat))&&ez(he(d1,Q5)),"d1 Gram");
ck(eq(he(ehat,ehat),E(1326,0,25))&&eq(he(d0,d0),E(976,0,145)),"norms");
const rA=em(he(A,d1),ei(he(d1,d1))),Ap=vs(A,vm(d1,rA));
const rG=em(he(vs(G,vm(Q5,em(g,bF))),d1),ei(he(d1,d1)));
const G1=vs(G,vm(Q5,em(g,bF))),G1p=vs(G1,vm(d1,rG));
ck(ez(he(Ap,d1))&&ez(he(G1p,d1)),"comps");
const zetas=[E(1),om,om2,E(-1),en(om),en(om2)];
const parity=z=>{ck(z[0][1]===1n&&z[1][1]===1n,"integer");return [Number((z[0][0]%2n+2n)%2n),Number((z[1][0]%2n+2n)%2n)];};
const frames=zetas.map(z=>{
 const r=vm(va(d1,vm(C,es(E(1),z))),E(15));
 ck(eq(he(r,r),E(1755)),"covered norm");
 const pm=r.map(parity),odd=pm.reduce((n,[a,b])=>n+(a||b?1:0),0);ck(odd%2===1,"odd half characteristic");
 return {zeta:out(z),row:r.map(out),mod2:pm,odd_factors:odd};
});
const w0=esc(he(d0,W),1,72),w1=esc(he(d1,W),1,72);
ck(eq(w0,E(-6,-1,60))&&eq(w1,E(-61,-36,360)),"W shifts");

const roweq=(x,y,label)=>ck(x.every((v,i)=>eq(v,y[i])),label);
roweq(C,vm(vs(ehat,d1),E(5,0,39)),"C reconstruction");
roweq(va(f1,vm(C,E(13))),va(vm(ehat,E(70,0,39)),vm(d1,E(-31,0,39))),"old E reconstruction");
roweq(G1,va(G1p,vm(d1,en(esc(g,31,39)))),"G reconstruction");
roweq(A,va(Ap,vm(d1,E(5,30,39))),"A reconstruction");
ck(eq(em(E(61,36),ec(E(61,36))),E(2821)),"W gamma numerator norm");
return {d0:d0.map(out),d1:d1.map(out),five_d1:vm(d1,E(5)).map(out),Ehat:ehat.map(out),
norm_d0:out(he(d0,d0)),norm_d1:out(he(d1,d1)),norm_Ehat:out(he(ehat,ehat)),
rA:out(rA),Aperp:Ap.map(out),norm_Aperp:out(he(Ap,Ap)),rG:out(rG),G1perp:G1p.map(out),
C_in_D1_Ehat:{D1:out(E(-5,0,39)),Ehat:out(E(5,0,39))},
Eold_in_D1_Ehat:{D1:out(E(-31,0,39)),Ehat:out(E(70,0,39))},
W_shift_D0:out(w0),W_shift_D1:out(w1),frames};
}
const text=JSON.stringify(certificate(),null,2)+'\n';
if(process.argv[2])require('fs').writeFileSync(process.argv[2],text);else process.stdout.write(text);
