#!/usr/bin/env node
// Exact R659 certificate. Reads the already published R594 JSON; no new right inverse.
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




function mass(input){
const r=input,parse=s=>{const t=s.split("/");return Q(t[0],t[1]||1);},read=x=>x.map(parse);
const B=r.polynomial_right_inverse.B.map(M=>M.map(row=>row.map(read))), baseP=r.matrix.basePlus.map(read),baseZ=r.matrix.baseZero.map(read),target=r.matrix.target.map(read);
ck(baseZ.every(ez),"R594 baseZero is identically zero");
const rhs=target.map((t,i)=>es(t,ea(baseP[i],baseZ[i])));
const res=B[0].map((row,i)=>en(row.reduce((z,c,j)=>ea(z,em(ea(c,B[1][i][j]),rhs[j])),E(0))));
const w=E(0,1),w2=E(-1,-1),delta=E(1,2),zero=E(0),row=a=>a.map(x=>Array.isArray(x)?E(...x):E(x));
const C=vm(row([1,0,-1,1,0,0]),ei(delta));
const A=row([[1,2],[2,4],[3,1],[2,-1],0,0]);
const Qrow=row([0,0,0,0,1,2]);
const D=row([1,[-1,-1],[0,-2],0,1,[2,3]]),F=va(D,C);
const H1=row([-1,2,[0,1],[1,1],0,0]),g=E(3,-2),G=va(vm(H1,E(13)),vm(F,g));
const a=E(-5,-6,29),bf=E(5,6,5),F0=vs(vs(F,vm(A,a)),vm(Qrow,bf)),D0=vs(F0,C),E0=va(F0,vm(C,E(13))),G0=va(vm(H1,E(13)),vm(F0,g));
const nd=he(D0,D0),neF=he(F0,F0);
ck(eq(nd,E(976,0,145))&&eq(neF,E(831,0,145)),"true norms");
const proj=(V,D)=>vs(V,vm(D,em(he(V,D),ei(he(D,D)))));
const Ep=proj(E0,D0),Gp=proj(G0,D0);
const Cp=vm(vs(Ep,D0),E(1,0,14)),Fp=vm(va(Ep,vm(D0,E(13))),E(1,0,14));
const rows=[Cp,Fp,Gp];
function add(P,R){const z={...P};for(const[k,v]of Object.entries(R)){z[k]=ea(z[k]||E(0),v);if(ez(z[k]))delete z[k];}return z;}
function scale(P,c){return Object.fromEntries(Object.entries(P).map(([k,v])=>[k,em(v,c)]).filter(([k,v])=>!ez(v)));}
function mul(P,R){const z={};for(const[k,v]of Object.entries(P))for(const[j,u]of Object.entries(R)){const e=k.split(",").map((a,i)=>+a+ +j.split(",")[i]).join(",");z[e]=ea(z[e]||E(0),em(v,u));}return z;}
function pow(P,n){let z={"0,0,0":E(1)};for(let i=0;i<n;i++)z=mul(z,P);return z;}
const lin=coeff=>Object.fromEntries(coeff.map((c,i)=>[[0,1,2].map(j=>i===j?1:0).join(","),c]).filter(([k,v])=>!ez(v)));
const z=Array.from({length:6},(_,j)=>lin(rows.map(V=>V[j])));
const zz=scale(add(add(z[0],scale(z[2],E(-1))),scale(z[3],E(-2))),E(1,0,6));
const zq=scale(add(z[0],z[2]),E(1,0,2));
const gen=scale(mul(mul(mul(add(mul(zz,pow(zq,2)),scale(pow(zz,3),E(-1))),z[1]),z[4]),z[5]),E(1,0,42));
const fact=n=>{let x=1;for(let i=2;i<=n;i++)x*=i;return x;};
const moments=r.matrix.exps.map(e=>esc(gen[e.join(",")]||E(0),e.reduce((x,n)=>x*fact(n),1)));
const residue=res.reduce((s,c,i)=>ea(s,em(c,moments[i])),E(0));

const constant=B[0].map(row=>en(row.reduce((z,c,j)=>ea(z,em(c,rhs[j])),E(0))));
const fP=r.matrix.polys.map(P=>Object.fromEntries(Object.entries(P).map(([k,v])=>[k,read(v)])));
const Pbase=Object.fromEntries(Object.entries(r.matrix.base).map(([k,v])=>[k,read(v)]));
let Pres={},Pconst=Pbase;
for(let i=0;i<fP.length;i++){Pres=add(Pres,scale(fP[i],res[i]));Pconst=add(Pconst,scale(fP[i],constant[i]));}
const onlyE0=P=>Object.fromEntries(Object.entries(P).filter(([k,v])=>+k.split(",")[1]===0));
const genFor=rr=>{
 const zz=Array.from({length:6},(_,j)=>lin(rr.map(V=>V[j])));
 const zZ=scale(add(add(zz[0],scale(zz[2],E(-1))),scale(zz[3],E(-2))),E(1,0,6));
 const zQ=scale(add(zz[0],zz[2]),E(1,0,2));
 return scale(mul(mul(mul(add(mul(zZ,pow(zQ,2)),scale(pow(zZ,3),E(-1))),zz[1]),zz[4]),zz[5]),E(1,0,42));
};
const genD=genFor([D0,Ep,Gp]);
const momentPoly=P=>Object.entries(P).reduce((s,[key,coeff])=>ea(s,em(coeff,esc(genD[key]||E(0),key.split(",").reduce((x,n)=>x*fact(+n),1)))),E(0));
const aRes=momentPoly(Pres),aConst=momentPoly(Pconst),aRes0=momentPoly(onlyE0(Pres)),aConst0=momentPoly(onlyE0(Pconst));
ck(eq(aRes,residue),"same residue by original C/F/G and transformed D/E/G coordinates");
const aNumerator=[aRes,es(ea(aRes,aConst),aRes0),es(aConst,aConst0)];
return {residue_without_b:out(residue),nonzero:!ez(residue),
 right_inverse_residue:res.map(out),right_inverse_constant:constant.map(out),
 unrestricted_moments:{aRes:out(aRes),aConst:out(aConst),aRes_E0:out(aRes0),aConst_E0:out(aConst0)},
 unrestricted_A_numerator:aNumerator.map(out),
 Pres:Object.fromEntries(Object.entries(Pres).map(([k,v])=>[k,out(v)])),
 Pconst:Object.fromEntries(Object.entries(Pconst).map(([k,v])=>[k,out(v)])),
 six_degree_generator_DEG:Object.fromEntries(Object.entries(genD).map(([k,v])=>[k,out(v)])),
 original_twenty_moments:moments.map(out),
 rows:{D0:D0.map(out),Eperp:Ep.map(out),Gperp:Gp.map(out),Cprime:Cp.map(out),Fprime:Fp.map(out)},
 full_polynomial_definition:"Qtilde=-C^6/8+sum x_i C^i F^j G^(6-i-j); P=Qtilde((E-D)/14,(E+13D)/14,G); HatP_E^j multiplies (1+lambda*kappa^j)^-1",
 full_numerator_coefficients:"alpha0=aRes, alpha1=aRes+aConst-aRes_E0-bRes, alpha2=aConst-aConst_E0-bConst; bRes,bConst are full degree-six moments of J_E mu0 after E=0",
 boundary:"The complete Ehat-deep term is retained via the fixed J_E operator. No W failure branch or global central coefficient is set to zero."};
}
function geometry(){
const row=a=>a.map(x=>Array.isArray(x)?E(...x):E(x)),w=E(0,1),delta=E(1,2);
const C=vm(row([1,0,-1,1,0,0]),ei(delta)),A=row([[1,2],[2,4],[3,1],[2,-1],0,0]),Qrow=row([0,0,0,0,1,2]);
const D=row([1,[-1,-1],[0,-2],0,1,[2,3]]),F=va(D,C),H1=row([-1,2,[0,1],[1,1],0,0]),g=E(3,-2);
const F0=vs(vs(F,vm(A,E(-5,-6,29))),vm(Qrow,E(5,6,5))),D0=vs(F0,C),EH=va(F0,vm(C,E(831,0,145)));
const G0=va(vm(H1,E(13)),vm(F0,g)),E0=va(F0,vm(C,E(13)));
const proj=(V,D)=>vs(V,vm(D,em(he(V,D),ei(he(D,D)))));
const Gp=proj(G0,D0),G00=proj(Gp,EH);
const eH=em(he(E0,EH),ei(he(EH,EH))),gH=em(he(Gp,EH),ei(he(EH,EH)));
let frame=[vm(D0,E(435)),vm(EH,E(435)),A,Qrow];
for(const j of [1,3]){
 let v=Array.from({length:6},(_,i)=>E(i===j?1:0));for(const r of frame)v=proj(v,r);
 let den=1n;for(const x of v)for(const y of x)den=den/gcd(den,y[1])*y[1];v=vm(v,E(den));
 let cont=0n;for(const x of v)for(const y of x)cont=gcd(cont,y[0]);if(cont>1n)v=vm(v,E(1,0,cont));frame.push(v);
}
for(let i=0;i<6;i++)for(let j=0;j<i;j++)ck(ez(he(frame[i],frame[j])),"full orthogonal frame");
const roots=[E(1),w,E(-1,-1),E(-1),E(0,-1),E(1,1)],counts=[];
for(const zeta of roots){
 const fr=frame.map(V=>va(V,vm(C,em(es(zeta,E(1)),he(V,C)))));
 const cs=fr.map(V=>V.filter(x=>{ck(x[0][1]===1n&&x[1][1]===1n,"integral rotated frame");return ((x[0][0]%2n+2n)%2n)!==0n||((x[1][0]%2n+2n)%2n)!==0n;}).length);
 counts.push({zeta:out(zeta),counts:cs,first_two_rows:fr.slice(0,2).map(V=>V.map(out))});
}
const gamma61=E(9,4),gamma277=E(19,7);
ck(eq(em(gamma61,ec(gamma61)),E(61))&&eq(em(gamma277,ec(gamma277)),E(277)),"norm anchors");
return {frame:frame.map(V=>V.map(out)),norms:frame.map(V=>out(he(V,V))),det:out(inverse(frame).det),six_counts:counts,Dnorm:out(he(D0,D0)),EHnorm:out(he(EH,EH)),eH:out(eH),gH:out(gH),G00:G00.map(out),alphaD:out(esc(gamma61,12)),alphaE:out(esc(em(em(delta,gamma61),gamma277),12))};}
function ray(){
const mod=(a,m)=>(a%m+m)%m, mul=(x,y,m)=>[mod(x[0]*y[0]-x[1]*y[1],m),mod(x[0]*y[1]+x[1]*y[0]-x[1]*y[1],m)];
function lift(N){const odd=N/16n;let aa,bb;for(let j=0n;j<32n;j++){if(mod(1n+odd*j,32n)===27n)aa=1n+odd*j;if(mod(odd*j,32n)===8n)bb=odd*j;}const g=[aa,bb],g2=mul(g,g,2n*N),g4=mul(g2,g2,2n*N);ck(g4[0]===N+1n&&g4[1]===0n,"whole central lift");
return {N:String(N),g:g.map(String),g2:g2.map(String),g4:g4.map(String),odd:String(odd)};}
const nd=1273680n,ne=7299504n;
const oldN=2472927397763665199448933946112894490007339710666935242077696606118805073600n;
const M3=644334713221211664683999580832075275137576500154103114298427212462582953667245059276705086480664434315320963745272978796223865508721827968275879027928001n;
const high=1323133171213029144041201350687525528684869767169429257083200n;
const K0=7042039214102991338991431191415932406822351473245123998636336203728636560665n;
ck(M3===1n+37n*oldN*K0,"unchanged original M3");
ck(gcd(61n*277n,37n*oldN*M3)===1n,"exact CRT");
return {D:lift(nd),E:lift(ne),oldN:String(oldN),M3:String(M3),K0:String(K0),high:String(high),new_conditions:"pi0=-1 mod61 and mod277",remainders:[61n,277n].map(m=>({mod:String(m),oldN:String(oldN%m),M3:String(M3%m),high:String(high%m)}))};}
function certificate(input){return {format:"R659 exact frozen-gate mass certificate",dependencies:{r594:"check-r594-two-source-six-carry-compensation.json",fixed_coefficients:"b=17; no change to the R594 polynomial inverse"},mass:mass(input),geometry:geometry(),ray:ray(),
scope:{full_source:"same mu0=P6_C rho0; all six inputs retained",N:"all positive multiples of four, simultaneously",unit_family:"the existing fixed ordinary ray, plus pi0=-1 mod61,277, minus O(sqrt(X) log(X)) primes and fixed denominators",J_E:"fixed canonical full Heisenberg intertwiner normalized on sigma((-948+2100omega)z); not a numerically expanded matrix",unknown_coefficients:"bRes,bConst retain the complete Esharp-deep source; nonzero constant alpha0 cannot be canceled",W:"both genuine W failure branches and all five S5 tensor components retained"}};}

const fs=require('fs'),path=require('path');
const input=JSON.parse(fs.readFileSync(path.join(__dirname,'check-r594-two-source-six-carry-compensation.json'),'utf8'));
const output=JSON.stringify(certificate(input),null,2)+'\n';
if(process.argv[2])fs.writeFileSync(process.argv[2],output);else process.stdout.write(output);
