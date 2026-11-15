#!/usr/bin/env node
/* R675: original fixed q, uncut cd endpoint n=N.
   Exact Q(omega) arithmetic. No prime sampling and no alternative q.
   The full coefficient evaluator takes the already fixed R594 HatP.
   The default certificate reconstructs its entire kappa=u=0 residue from
   the published R659 Pres/Pconst and retains B_C's sixth moment. */
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



function generate(u=E(0),kappa=E(0),isFlat=false){
const endpoint=1;
const r670={"flat_rows":{"A":[["-1","1/2"],["2","3/2"],["2","4"]],"D":[["-19/174","19/174"],["31/58","-37/58"],["-43/29","-21/29"]],"Eperp":[["-133/429","133/429"],["217/143","-259/143"],["-602/143","-294/143"]],"Gperp":[["-5843/858","-3715/858"],["-1593/286","-123/22"],["1324/143","-266/143"]],"G00":[["-247/36","-143/36"],["-65/12","-91/12"],["13/2","-13/6"]]}};

const parse=s=>{let a=s.split("/");return Q(a[0],a[1]||1);},read=v=>v.map(parse);
const F=r670.flat_rows,af=F.A.map(read),df=F.D.map(read),ef=F.Eperp.map(read),gf=F.Gperp.map(read);
const N=5,conv=(a,b)=>Array.from({length:N+1},(_,n)=>{let s=Q(0);for(let i=0;i<=n;i++)s=qa(s,qm(a[i]||Q(0),b[n-i]||Q(0)));return s;});
const pw=(a,k)=>{let z=Array.from({length:N+1},(_,i)=>Q(i?0:1));for(let j=0;j<k;j++)z=conv(z,a);return z;};
const xx=[Q(1),Q(-1,7)];for(let n=2;n<=N;n++){let s=Q(0);for(let i=1;i<n;i++)s=qa(s,qm(xx[i],xx[n-i]));xx[n]=qm(s,Q(1,(6*n+1)*(n-1)));}
const logs=[Q(0),...xx.slice(1).map((a,i)=>qm(qn(a),Q(1,6*(i+1)*(6*(i+1)-1))))],sig=[Q(1)];
for(let n=1;n<=N;n++){let s=Q(0);for(let k=1;k<=n;k++)s=qa(s,qm(qm(Q(k),logs[k]),sig[n-k]));sig[n]=qm(s,Q(1,n));}
const minusY=xx.map((a,n)=>n===0?Q(1):qm(Q(-(3*n-1)),a)),as2=pw(sig,2),as6=pw(sig,6),f3=conv(as6,minusY),f1=conv(f3,xx),theta=conv(as2,xx);
const fact=n=>{let s=1;for(let k=2;k<=n;k++)s*=k;return s;},choose=(n,k)=>{let r=1;for(let j=1;j<=k;j++)r=r*(n+1-j)/j;return r;};
const add=(P,R)=>{let T={...P};for(const[k,c]of Object.entries(R)){T[k]=ea(T[k]||E(0),c);if(ez(T[k]))delete T[k];}return T;};
const scale=(P,c)=>Object.fromEntries(Object.entries(P).map(([k,v])=>[k,em(c,v)]).filter(([k,v])=>!ez(v)));
function mul(P,R){
 const T={},PE=Object.entries(P).map(([k,v])=>[k.split(",").map(Number),v]),RE=Object.entries(R).map(([k,v])=>[k.split(",").map(Number),v]);
 for(const[a,c]of PE)for(const[b,d]of RE){let z=a.map((x,i)=>x+b[i]);if(z[0]+z[1]+z[2]>6||z[3]>30)continue;let q=z.join(",");T[q]=ea(T[q]||E(0),em(c,d));}
 return Object.fromEntries(Object.entries(T).filter(([k,v])=>!ez(v)));
}
function linearPower(v,n){let P={"0,0,0,0":E(1)},L={};for(let i=0;i<3;i++){let e=[0,0,0,0];e[i]=1;L[e.join(",")]=v[i];}for(let i=0;i<n;i++)P=mul(P,L);return P;}
function source(i){
 const ei0=i===0?E(-170,-117,9135):E(-170,-291,9135),obs=[...af,E(i===0?1:2),E(i===0?2:-1)];
 let wr=[...df.map((x,j)=>ea(x,esc(em(ei0,af[j]),5))),esc(ei0,-87),esc(ei0,-29)];
 const hh=i===0?E(-5,-9):E(-5,-3);
 if(endpoint)wr=va(wr,vm([...af.map(x=>esc(x,5)),E(i===0?39:-24),E(i===0?-92:97)],esc(hh,endpoint,315)));
 const er0=[...ef,E(0),E(0)],gr0=[...gf,E(0),E(0)],df0=[...df,E(0),E(0)],g00=[...F.G00.map(read),E(0),E(0)];
 const kr=vs(wr,vm(df0,E(406,0,143))),g=E(3,-2);
 const er=va(vm(er0,isFlat?kappa:E(1)),vm(kr,u));
 const gr=va(isFlat?va(g00,vm(vs(gr0,g00),kappa)):gr0,vm(kr,em(g,u)));
 const lp=Array.from({length:5},(_,axis)=>Array.from({length:7},(_,r)=>linearPower([wr[axis],er[axis],gr[axis]],r)));
 const obsp=obs.map(x=>{let P=[E(1)];for(let j=1;j<=36;j++)P.push(em(P.at(-1),x));return P;});
 function factor(base,coeff,axis){
 let P={};for(let h=0;h<=N;h++){let nn=base+6*h;for(let r=0;r<=Math.min(6,nn);r++){let z=nn-r;if(z>30)continue;const c=em([coeff[h],Q(0)],esc(obsp[axis][z],choose(nn,r)));for(const[k,v]of Object.entries(lp[axis][r])){let q=k.split(",").map(Number);q[3]=z;let kk=q.join(",");P[kk]=ea(P[kk]||E(0),em(c,v));}}}return P;
 }
 let flat=add(mul(factor(1,f1,0),factor(2,as2,1)),scale(mul(factor(3,f3,0),factor(0,theta,1)),E(-1)));
 for(let j=2;j<5;j++)flat=mul(flat,factor(1,sig,j));
 flat=scale(flat,E(1,0,42));
 const cscale=isFlat?kappa:E(1),kC=E(263,0,143);
 const lc=[E(-1),ea(em(cscale,E(1596,0,143)),em(u,kC)),
 ea(em(cscale,E(-789,526,143)),em(em(E(3,-2),u),kC))];
 const six=scale(linearPower(lc,6),E(-1,0,90));
 const full=add(flat,mul(flat,six));
 const Gen=Array.from({length:6},(_,r)=>Object.fromEntries(Object.entries(full).filter(([k,v])=>{let x=k.split(",").map(Number);return x[0]+x[1]+x[2]===6&&x[3]===6*r;}).map(([k,v])=>[k.split(",").slice(0,3).join(","),esc(v,i===0?1:-1)])));
 return{e:out(ei0),observation:obs.map(out),linear_rows:[wr,er,gr].map(R=>R.map(out)),C_component:lc.map(out),gen:Gen};
}

return {sources:[source(0),source(1)].map(s=>({...s,gen:s.gen.map(G=>Object.fromEntries(Object.entries(G).map(([k,v])=>[k,out(v)])))})),sigma:sig.map(qs),wp:xx.map(qs)};
}

const parseR=s=>{const x=String(s).split("/");return Q(x[0],x[1]||1);};
const readE=v=>v.map(parseR);
const factorial=n=>{let f=1;for(let j=2;j<=n;j++)f*=j;return f;};
function moment(P,G,e0=false){
 let v=E(0);
 for(const[k,c]of Object.entries(P)){
  const a=k.split(",").map(Number);if(e0&&a[1])continue;
  v=ea(v,esc(em(readE(c),readE(G[k]||["0","0"])),a.reduce((f,n)=>f*factorial(n),1)));
 } return v;
}
function triangular(data){
 const sig=data.sigma.map(parseR),xx=data.wp.map(parseR),N=5;
 const conv=(a,b)=>Array.from({length:6},(_,n)=>{let c=Q(0);for(let i=0;i<=n;i++)c=qa(c,qm(a[i]||Q(0),b[n-i]||Q(0)));return c;});
 const power=(a,n)=>{let r=[Q(1),...Array.from({length:5},()=>Q(0))];for(let i=0;i<n;i++)r=conv(r,a);return r;};
 const h34=power(sig,34),M=Array.from({length:6},()=>Array.from({length:6},()=>Q(0)));
 for(let j=0;j<6;j++){let a=conv(h34,power(xx,17-3*j));for(let r=j;r<6;r++)M[r][j]=a[r-j];}
 const inv=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j)=>Q(i===j?1:0)));
 for(let i=0;i<6;i++)for(let j=0;j<i;j++)for(let k=0;k<6;k++)inv[i][k]=qa(inv[i][k],qn(qm(M[i][j],inv[j][k])));
 return {matrix:M,inverse:inv};
}
function completeCoefficients(P,lambda,kappa,u,eta,b=17){
 const lam=readE(lambda),kap=readE(kappa),uu=readE(u);
 const full=generate(uu,kap,false),flat=generate(uu,kap,true),iv=triangular(full).inverse;
 const a=full.sources[0].gen.map((G,r)=>es(moment(P,G),esc(em(lam,moment(P,flat.sources[0].gen[r])),eta)));
 const coeff=a.map((_,r)=>{
  let c=E(0);for(let j=0;j<=r;j++)c=ea(c,em([iv[r][j],Q(0)],a[j]));
  const scale=r===0?Q(1,b):Q(BigInt(b)**BigInt(r-1));return out(em([scale,Q(0)],c));
 });
 return {normalized_first_theta_coefficients:coeff,
  actual_second_theta_coefficients:coeff.map(c=>out(en(readE(c)))),
  basis:"Xi_j=sigma^34*x^(17-3j), j=0..5",
  complete_parameters:{lambda,kappa,u,eta,b},
  scope:"All coefficients, including Cperp unit complement; P is the original R594 HatP."};
}
function certificate(r659){
 const full=generate(),flat=generate(E(0),E(0),true),tr=triangular(full);
 const Pres=r659.mass.Pres,Pconst=r659.mass.Pconst;
 let count=0;for(let r=0;r<6;r++){
  for(const key of new Set([...Object.keys(full.sources[0].gen[r]),...Object.keys(full.sources[1].gen[r])])){
   ck(JSON.stringify(full.sources[0].gen[r][key]||["0","0"])===JSON.stringify(full.sources[1].gen[r][key]||["0","0"]),"integer quarter normalized source");count++;
  }
 }
 const residues={},reduced={};
 for(const k of new Set([...Object.keys(Pres),...Object.keys(Pconst)]))if(+k.split(",")[1]===0)ck(eq(readE(Pres[k]||["0","0"]),readE(Pconst[k]||["0","0"])),"original E0 parts agree");
 for(const eta of[-1,1]){
  const N=full.sources[0].gen.map((G,r)=>{
   const A=moment(Pres,G),B=moment(Pconst,G),A0=moment(Pres,G,true),B0=moment(Pconst,G,true),
    Af=moment(Pres,flat.sources[0].gen[r]),Bf=moment(Pconst,flat.sources[0].gen[r]);
   return[A,es(es(ea(A,B),A0),esc(Af,eta)),es(es(B,B0),esc(Bf,eta))];
  });
  const T=N.map((row,r)=>row.map((_,h)=>N.slice(0,r+1).reduce((sum,x,j)=>ea(sum,em([tr.inverse[r][j],Q(0)],x[h])),E(0))));
  ck(!ez(T[0][0]),"nonzero constant term of mass numerator");
  for(const R of T)ck(eq(es(R[1],R[0]),R[2]),"exact common (1+lambda) factor");
  residues[eta]={taylor_numerators:N.map(R=>R.map(out)),theta_numerators:T.map(R=>R.map(out))};
  reduced[eta]=T.map(R=>({inverse_lambda:out(R[0]),constant:out(R[2])}));
 }
 return {
  format:"R675 exact original cd endpoint and full six-coefficient return",
  original_dependencies:["R594 actual fixed right inverse","R659 original Pres/Pconst","R665 full Cperp core","R669 complete S34 source","R671 uncut cd domain"],
  endpoint:{u:"kappa^N",t:1,N:"positive multiple of 4",domains:"{c,d in p^N,Y_i in p^N}={A,Q,L in p^N}=Gamma_N intersect {Eall in p^N}"},
  normalization:"c_j=b^(j-1)*(A_j/lambda+B_j_eta) modulo p; the common (1+lambda) factor is exactly cancelled; no coefficient of P_hat is changed",
  full_evaluator:"completeCoefficients(P,lambda,kappa,u,eta,b)",
  theta_basis:"sigma^34*x^(17-3j), j=0..5",
  source_s_vector:[["0","0"],["1","0"],["-53/7","0"],["-12/7","0"],["-80/7","0"],["-128/7","0"]],
  source_s_vector_weight:"entry j>=1 must be multiplied by b^(j-1)",
  triangular:{matrix:tr.matrix.map(R=>R.map(qs)),inverse:tr.inverse.map(R=>R.map(qs))},
  generators:{full,flat},
  residue:residues,
  reduced_residue:reduced,
  original_sixth_C_moment:"-8*b*Omega^6; B_C(s)=1-b*s^6/90+O(s^12)",
  normalized_quarter_equalities:count,
  mass_constant_nonzero:true,
  integral_exception:"fixed denominator set plus zeros of two fixed norm polynomials at the Frobenius trace; O(sqrt(X)*log X)",
  scope:"The actual endpoint source is off the original S line on a relative-density-one subset. Its unit mass is nonzero. No log derivative or complete arithmetic exterior is set to zero."
 };
}
if(typeof module!=="undefined")module.exports={certificate,generate,completeCoefficients};
if(typeof require!=="undefined"&&require.main===module){
 const fs=require("fs"),path=require("path");
 let answer;
 if(process.argv[2]==="--evaluate"){
  const a=JSON.parse(fs.readFileSync(process.argv[3],"utf8"));
  answer=completeCoefficients(a.hat_polynomial,a.lambda,a.kappa,a.u,a.eta,a.b||17);
 }else{
  const r659=JSON.parse(fs.readFileSync(path.join(__dirname,"check-r659-frozen-gate-mass-and-full-compensation.json"),"utf8"));
  answer=certificate(r659);
 }
 const text=JSON.stringify(answer,null,2)+"\n";
 if(process.argv[2]&&process.argv[2]!=="--evaluate")fs.writeFileSync(process.argv[2],text);else process.stdout.write(text);
}
