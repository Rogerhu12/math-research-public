#!/usr/bin/env node
"use strict";
/* R677: same actual R674 adapted family at the R675 cd endpoint.
   A fixed auxiliary field certifies nonzero rational functions only.
   It is not the research prime and its solution never replaces q_N^dagger. */
const p=1009n,omega=374n,mod=x=>(x%p+p)%p;
function pow(x,n){let y=1n;for(x=mod(x);n;n>>=1n,x=mod(x*x))if(n&1n)y=mod(y*x);return y;}
const ck=(v,m)=>{if(!v)throw Error(m);};
function rat(s){const a=String(s).split("/"),d=mod(BigInt(a[1]||1));ck(d!==0n,"auxiliary denominator");return mod(BigInt(a[0])*pow(d,p-2n));}
const cm=c=>mod(rat(c[0])+omega*rat(c[1]));
const mm=(A,B)=>A.map(R=>B[0].map((_,j)=>mod(R.reduce((s,x,k)=>s+x*B[k][j],0n))));
const ident=n=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>i===j?1n:0n));
const fact=n=>{let z=1n;for(let i=2;i<=n;i++)z*=BigInt(i);return z;};
function solve(A,b){
 let M=A.map((R,i)=>R.map(x=>mod(BigInt(x))).concat(mod(BigInt(b[i])))),det=1n;
 for(let k=0;k<b.length;k++){
  let j=k;while(j<M.length&&M[j][k]===0n)j++;ck(j<M.length,"13 matrix invertible");
  if(j!==k){[M[j],M[k]]=[M[k],M[j]];det=mod(-det);}
  const v=M[k][k];det=mod(det*v);M[k]=M[k].map(x=>mod(x*pow(v,p-2n)));
  for(let i=0;i<M.length;i++)if(i!==k){const v=M[i][k];M[i]=M[i].map((x,j)=>mod(x-v*M[k][j]));}
 }return{solution:M.map(R=>R.at(-1)),det};
}
function certificate(all,adapt,endpoint){
 const AP=all.matrix.Aplus.map(R=>R.map(cm)),AZ=all.matrix.Azero.map(R=>R.map(cm));
 const A=AP.map((R,i)=>R.map((x,j)=>mod(x+2n*AZ[i][j])));
 const Bs=all.polynomial_right_inverse.B.map(M=>M.map(R=>R.map(cm)));
 const B=Bs[0].map((R,i)=>R.map((x,j)=>mod(x+2n*Bs[1][i][j])));
 const AB=mm(A,B),BA=mm(B,A),Pi=ident(20).map((R,i)=>R.map((x,j)=>mod(x-BA[i][j])));
 ck(JSON.stringify(AB.map(R=>R.map(String)))===JSON.stringify(ident(9).map(R=>R.map(String))),"original right inverse");
 ck(mm(A,Pi).every(R=>R.every(x=>x===0n)),"original full kernel");
 const full=endpoint.generators.full.sources[0].gen,flat=endpoint.generators.flat.sources[0].gen;
 const cols=all.matrix.polys,pivs=adapt.pivots;
 const moment=(P,G,e0=false)=>mod(Object.entries(P).reduce((sum,[key,c])=>{
  const e=key.split(",").map(Number);if(e0&&e[1])return sum;
  return sum+cm(c)*cm(G[key]||["0","0"])*e.reduce((f,n)=>f*fact(n),1n);
 },0n));
 const inv=endpoint.triangular.inverse.map(R=>R.map(rat)),out={};
 for(const eta of[1,-1]){
  const sign=BigInt(eta),a=adapt.auxiliary.eta[eta],rows=full.map((G,r)=>cols.map(P=>mod(moment(P,G)+moment(P,G,true)+sign*moment(P,flat[r]))));
  const ker=mm(rows,Pi),given=a.solution.map(BigInt),sol=solve(a.matrix,a.rhs);
  ck(sol.det===BigInt(a.det),"same nonzero 13 determinant");
  ck(sol.solution.every((x,j)=>x===given[j]),"same actual-definition auxiliary solution");
  const rr=endpoint.residue[eta].taylor_numerators;
  const old=rr.map(R=>mod(-2n*cm(R[0])+cm(R[2])));
  const jets=old.map((x,r)=>mod(x+pivs.reduce((s,col,j)=>s+ker[r][col]*given[j],0n)));
  const theta=inv.map(R=>mod(R.reduce((s,c,j)=>s+c*jets[j],0n)));
  ck(theta[0]!==0n,"adapted endpoint mass numerator nonzero");
  const direction=solve(a.matrix,Array.from({length:13},(_,j)=>j===12?1n:0n)).solution;
  const sj=old.map((_,r)=>mod(pivs.reduce((s,col,j)=>s+ker[r][col]*direction[j],0n)));
  const slope=inv.map(R=>mod(R.reduce((s,c,j)=>s+c*sj[j],0n)));
  const base=theta.map((x,j)=>mod(x-slope[j]));
  const a0=base[0],b0=slope[0],a2=mod(7n*base[2]+53n*base[1]),b2=mod(7n*slope[2]+53n*slope[1]),det=mod(a0*b2-a2*b0);
  ck(det!==0n,"all J cannot satisfy both endpoint S constraints");
  out[eta]={adapted_endpoint_jets:jets.map(String),adapted_endpoint_theta:theta.map(String),
   endpoint_theta_at_J0:base.map(String),endpoint_theta_J_slope:slope.map(String),
   full_target_J_direction:direction.map(String),
   affine_two_constraint_matrix:[[a0,b0],[a2,b2]].map(R=>R.map(String)),
   affine_obstruction_determinant:String(det),source13_determinant:String(sol.det)};
 }
 return{
  format:"R677 exact same-adapted-source endpoint, all-J obstruction, and complete exterior filters",
  field:{p:String(p),omega:String(omega),tau:"2",lambda:"-1/2"},
  dependencies:["check-r594-two-source-six-carry-compensation.json","check-r674-double-s-arithmetic-adaptation.json","check-r675-original-cd-endpoint-six-source.json"],
  actual_source_definition:"q(J) uses the complete actual R674 13 inverse at lambda,kappa,u=kappa^N; only its rational-function residue is certified here",
  eta:out,
  exact_domains:{V:"Ei intersect CD_N",I:"Gamma_n intersect CD_N = Gamma_n intersect Eall-deep N",O:"V minus I",X:"Ei minus CD_N",endpoint:"n=N gives V=I"},
  exact_filters:{P6:"product a=1..6 (shift-lambda^2*kappa^a)",P7:"(shift-lambda^2)*P6",
   P6_at_lambda:"lambda^6 * product a=1..6 (1-lambda*kappa^a)",
   P6_at_lambda2:"lambda^12 * product a=1..6 (1-kappa^a)",
   P7_at_lambda:"lambda^7*(1-lambda)*product a=1..6 (1-lambda*kappa^a)"},
  complete_O:"P6 O_i=lambda^(n+3N+6)V6 A_i-epsilon_i d_i lambda^(2n+2N+12)U6 JS",
  complete_X:"P6 X_i=epsilon_i lambda^(n+N+6)V6 JS-lambda^(n+3N+6)V6 A_i",
  mass_and_log:"Endpoint unit mass is nonzero on the relative-density-one subray; exact opposite O/X masses and all log-shift terms remain.",
  boundary:"Neither O nor X is separately assigned zero. The R665/R674 mixed T negative-one branch remains a different physical cut."
 };
}
if(typeof module!=="undefined")module.exports={certificate};
if(typeof require!=="undefined"&&require.main===module){
 const fs=require("fs"),path=require("path"),load=n=>JSON.parse(fs.readFileSync(path.join(__dirname,n),"utf8"));
 const answer=certificate(load("check-r594-two-source-six-carry-compensation.json"),load("check-r674-double-s-arithmetic-adaptation.json"),load("check-r675-original-cd-endpoint-six-source.json"));
 const text=JSON.stringify(answer,null,2)+"\n";
 if(process.argv[2])fs.writeFileSync(process.argv[2],text);else process.stdout.write(text);
}
