#!/usr/bin/env node
// Exact complete moving-angle Jacobi band/mean/parameter algebra.
// No floating computation, FFT, radial collocation, or finite inverse is used.
// This verifies explicit algebraic instances; the accompanying proof supplies
// the identities for arbitrary complete finite centre coefficients.
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
class Q{
 constructor(n=0n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
 add(b){return new Q(this.n*b.d+b.n*this.d,this.d*b.d);}
 neg(){return new Q(-this.n,this.d);}
 sub(b){return this.add(b.neg());}
 mul(b){return new Q(this.n*b.n,this.d*b.d);}
 div(b){return new Q(this.n*b.d,this.d*b.n);}
 eq(b){return this.n===b.n&&this.d===b.d;}
 zero(){return this.n===0n;}
 str(){return this.d===1n?String(this.n):String(this.n)+"/"+String(this.d);}
}
const q=(n,d=1)=>new Q(BigInt(n),BigInt(d));
class C{
 constructor(re=q(0),im=q(0)){this.re=re;this.im=im;}
 add(b){return new C(this.re.add(b.re),this.im.add(b.im));}
 neg(){return new C(this.re.neg(),this.im.neg());}
 sub(b){return this.add(b.neg());}
 mul(b){return new C(this.re.mul(b.re).sub(this.im.mul(b.im)),this.re.mul(b.im).add(this.im.mul(b.re)));}
 div(b){const den=b.re.mul(b.re).add(b.im.mul(b.im));return new C(this.re.mul(b.re).add(this.im.mul(b.im)).div(den),this.im.mul(b.re).sub(this.re.mul(b.im)).div(den));}
 eq(b){return this.re.eq(b.re)&&this.im.eq(b.im);}
 zero(){return this.re.zero()&&this.im.zero();}
 str(){return [this.re.str(),this.im.str()];}
}
const c=(n,d=1)=>new C(q(n,d)),cz=c(0),co=c(1);
const ip=(n)=>new C(q(0),q(n));
function put(a,k,v){if(v.zero())a.delete(k);else a.set(k,v);return a;}
function at(a,k){return a.get(k)||cz;}
function constant(z){return z.zero()?new Map():new Map([[0,z]]);}
function add(a,b){const z=new Map(a);for(const[k,v]of b)put(z,k,at(z,k).add(v));return z;}
function neg(a){return scale(a,c(-1));}
function sub(a,b){return add(a,neg(b));}
function scale(a,z){const b=new Map();if(z.zero())return b;for(const[k,v]of a)put(b,k,v.mul(z));return b;}
function mul(a,b){const z=new Map();for(const[k,v]of a)for(const[l,w]of b)put(z,k+l,at(z,k+l).add(v.mul(w)));return z;}
function derivative(a){const z=new Map();for(const[k,v]of a)if(k)put(z,k,v.mul(ip(4*k)));return z;}
function primitive(a){const z=new Map();for(const[k,v]of a)if(k)put(z,k,v.div(ip(4*k)));return z;}
function shift(a,k){return new Map([...a].map(([j,v])=>[j+k,v]));}
function equal(a,b){if(a.size!==b.size)return false;for(const[k,v]of a)if(!v.eq(at(b,k)))return false;return true;}
function support(a){return a.size?Math.max(...[...a.keys()].map(Math.abs)):0;}
function makeModel(u,v,K,gamma,beta){
 const m=at(v,0),uv=mul(u,v),uu=mul(u,u),vv=mul(v,v);
 const S=add(uu,scale(vv,K)),d=scale(primitive(S),beta.neg());
 const L=[
  [scale(add(constant(co),add(scale(uu,c(3)),scale(vv,K))),beta.neg()),scale(uv,beta.mul(K).mul(c(-2)))],
  [scale(uv,beta.mul(c(-2))),scale(sub(constant(co),add(uu,scale(vv,K.mul(c(3))))),beta)]
 ];
 return {u,v,K,gamma,beta,m,uu,uv,vv,S,d,L,Q:[u,v],W:[u,scale(v,K)],Qp:[derivative(u),derivative(v)]};
}
function fullAction(t,h){
 const T=scale(add(mul(t.u,h[0]),scale(mul(t.v,h[1]),t.K)),c(2));
 const dd=scale(primitive(T),t.beta.neg()),z=at(h[1],0);
 return [
  add(add(mul(t.d,derivative(h[0])),scale(derivative(h[1]),t.gamma.mul(t.m).mul(t.K))),
   add(add(mul(t.L[0][0],h[0]),mul(t.L[0][1],h[1])),add(mul(dd,t.Qp[0]),scale(t.Qp[1],t.gamma.mul(t.K).mul(z))))),
  add(sub(mul(t.d,derivative(h[1])),scale(derivative(h[0]),t.gamma.mul(t.m))),
   add(add(mul(t.L[1][0],h[0]),mul(t.L[1][1],h[1])),sub(mul(dd,t.Qp[1]),scale(t.Qp[0],t.gamma.mul(z)))))
 ];
}
function entry(t,a,b,j,n){
 let z=at(t.L[a][b],j-n);
 if(a===b)z=z.add(at(t.d,j-n).mul(ip(4*n)));
 if(j===n&&a===0&&b===1)z=z.add(t.gamma.mul(t.m).mul(t.K).mul(ip(4*n)));
 if(j===n&&a===1&&b===0)z=z.sub(t.gamma.mul(t.m).mul(ip(4*n)));
 // Exact entire intermediate k, excluding only its true zero mode.
 for(const[l,ql]of t.Q[a]){
  const k=j-l;if(!k)continue;
  const wk=at(t.W[b],k-n);if(wk.zero())continue;
  z=z.sub(t.beta.mul(c(2)).mul(c(l,k)).mul(ql).mul(wk));
 }
 if(b===1&&n===0){
  if(a===0)z=z.add(t.gamma.mul(t.K).mul(at(t.Qp[1],j)));
  else z=z.sub(t.gamma.mul(at(t.Qp[0],j)));
 }
 return z;
}
function parameter(t,dK,dGamma){
 const dd=scale(primitive(t.vv),t.beta.mul(dK).neg());
 return [
  add(mul(dd,t.Qp[0]),add(scale(t.Qp[1],t.m.mul(dGamma.mul(t.K).add(t.gamma.mul(dK)))),scale(mul(t.u,t.vv),t.beta.mul(dK).neg()))),
  add(mul(dd,t.Qp[1]),add(scale(t.Qp[0],t.m.mul(dGamma).neg()),scale(mul(t.v,t.vv),t.beta.mul(dK).neg())))
 ];
}
// Independent forward-mode polynomial differentiation of the nonlinear RHS.
// The tangent action above and its matrix entries are not called here.
function dual(a,b=new Map()){return [a,b];}
function da(a,b){return [add(a[0],b[0]),add(a[1],b[1])];}
function dn(a){return [neg(a[0]),neg(a[1])];}
function dm(a,b){return [mul(a[0],b[0]),add(mul(a[1],b[0]),mul(a[0],b[1]))];}
function ds(a,z){return [scale(a[0],z),scale(a[1],z)];}
function dd(a){return [derivative(a[0]),derivative(a[1])];}
function di(a){return [primitive(a[0]),primitive(a[1])];}
function nonlinearDual(u,v,K,gamma,beta){
 const m=dual(constant(at(v[0],0)),constant(at(v[1],0)));
 const S=da(dm(u,u),dm(K,dm(v,v))),drift=ds(di(S),beta.neg());
 const one=dual(constant(co));
 return [
  da(da(dm(drift,dd(u)),dm(dm(dm(gamma,m),K),dd(v))),ds(dm(u,da(one,S)),beta.neg())),
  da(da(dm(drift,dd(v)),dn(dm(dm(gamma,m),dd(u)))),ds(dm(v,da(one,dn(S))),beta))
 ];
}
function sampleCentre(M){
 const u=new Map(),v=new Map([[0,c(-9,8)]]);
 for(let k=1;k<=M;k++){
  // Full exact dyadic odd/even fields, with nonzero top coefficients.
  const A=q((7*k+3)%19+1,2**18),B=q((11*k+1)%23+1,2**18);
  u.set(k,new C(q(0),A.neg()));u.set(-k,new C(q(0),A));
  v.set(k,new C(B));v.set(-k,new C(B));
 }
 return [u,v];
}
function runExactAlgebra(){
 const M=32,N=3*M+1,[u,v]=sampleCentre(M);
 const t=makeModel(u,v,c(-11,7),c(13,8),c(-5,16)),dK=c(7,13),dGamma=c(2,9);
 const gates=[],gate=(name,pass,detail)=>{gates.push({name,passed:!!pass,...(detail?{detail}:{})});if(!pass)throw Error("exact gate failed: "+name);};
 gate("all_32_centre_modes_nonzero",support(u)===M&&support(v)===M);
 gate("local_and_drift_support_at_most_64",support(t.d)<=2*M&&t.L.every(row=>row.every(p=>support(p)<=2*M)));
 const inputs=[-N,-N+1,-2*M,-M,-1,0,1,M,2*M,N-1,N];
 let allEntries=true,band=true,count=0;
 for(const n of inputs)for(let b=0;b<2;b++){
  const h=[new Map(),new Map()];h[b]=new Map([[n,co]]);
  const direct=fullAction(t,h);
  for(let a=0;a<2;a++){
   for(let j=n-2*M-2;j<=n+2*M+2;j++){count++;if(!at(direct[a],j).eq(entry(t,a,b,j,n)))allEntries=false;}
   for(const[j,z]of direct[a])if(!z.zero()&&Math.abs(j-n)>2*M)band=false;
  }
 }
 gate("closed_infinite_band_entries_equal_complete_convolution_action",allEntries,{exact_entry_checks:count});
 gate("all_basis_outputs_obey_complete_64_band",band);
 let mean=true,meanFar=true;
 for(let n=-N-2;n<=N+2;n++)for(let b=0;b<2;b++){
  let expected=t.beta.mul(t.m).mul(c(-2)).mul(at(t.W[b],-n));
  if(b===1&&n===0)expected=expected.add(t.beta.mul(co.sub(at(t.S,0))));
  const actual=entry(t,1,b,0,n);
  if(!actual.eq(expected))mean=false;
  if(Math.abs(n)>M&&!actual.zero())meanFar=false;
 }
 gate("complete_second_mean_row_exact",mean);
 gate("direct_high_to_second_mean_zero_past_32",meanFar);
 const h=[new Map([[0,c(2,7)],[3,new C(q(1,17),q(2,19))],[-35,c(-3,23)]]),
          new Map([[0,c(-4,11)],[34,new C(q(-2,13),q(1,7))],[-2,c(1,29)]])];
 const A=fullAction(t,h);
 const nd=nonlinearDual(dual(u,h[0]),dual(v,h[1]),dual(constant(t.K)),dual(constant(t.gamma)),t.beta);
 gate("full_state_action_matches_independent_dual_derivative",equal(A[0],nd[0][1])&&equal(A[1],nd[1][1]));
 const pn=parameter(t,dK,dGamma);
 const np=nonlinearDual(dual(u),dual(v),dual(constant(t.K),constant(dK)),dual(constant(t.gamma),constant(dGamma)),t.beta);
 gate("complete_physical_parameter_column_matches_dual_derivative",equal(pn[0],np[0][1])&&equal(pn[1],np[1][1]));
 gate("physical_parameter_support_at_most_96",pn.every(p=>support(p)<=3*M));
 gate("parameter_top_96_not_silently_removed",pn.some(p=>support(p)===3*M));
 const expectedNuMean=t.beta.mul(t.m).mul(dK).mul(at(t.vv,0)).neg();
 gate("parameter_mean_is_minus_beta_m_Knu_mean_v_squared",at(pn[1],0).eq(expectedNuMean));
 const alpha=new C(q(6890507429876859n,9007199254740992n)),s=c(-8,7),snu=c(3,31),snur=c(-5,37);
 const constantShift=fullAction(t,[new Map(),constant(snu)]);
 const normalized=[scale(add(pn[0],constantShift[0]),co.div(alpha)),
                   scale(sub(add(pn[1],constantShift[1]),constant(snur)),co.div(alpha))];
 const dualNormalized=nonlinearDual(dual(u),dual(v,constant(snu)),dual(constant(t.K),constant(dK)),dual(constant(t.gamma),constant(dGamma)),t.beta);
 const independent=[scale(dualNormalized[0][1],co.div(alpha)),scale(sub(dualNormalized[1][1],constant(snur)),co.div(alpha))];
 gate("normalized_parameter_keeps_snu_and_snur",equal(normalized[0],independent[0])&&equal(normalized[1],independent[1]));
 const exactNormalizedMean=expectedNuMean.add(snu.mul(t.beta).mul(co.sub(at(t.S,0)).sub(t.K.mul(t.m).mul(t.m).mul(c(2))))).sub(snur).div(alpha);
 gate("normalized_parameter_complete_mean_row",at(normalized[1],0).eq(exactNormalizedMean));
 gate("normalized_parameter_support_at_most_96",normalized.every(p=>support(p)<=3*M));
 const V0=t.m.sub(s).div(alpha),dCr=snu.div(s.mul(s)).neg();
 const directBoundary=snu.div(t.m.mul(t.m)).neg().sub(dCr).div(alpha);
 const codedBoundary=dCr.neg().mul(V0).mul(s.mul(c(2)).add(alpha.mul(V0))).div(t.m.mul(t.m));
 gate("physical_C0_boundary_parameter_identity",directBoundary.eq(codedBoundary));
 gate("physical_C0_state_derivative_exact",co.div(t.m.mul(t.m)).neg().eq(c(-64,81)));
 const insideCore=N-2*M-1,outerFirst=N-2*M;
 gate("all_internal_parameter_source_fits_head_96",3*M===N-1);
 gate("head_tail_shell_starts_at_33",outerFirst===33&&insideCore===M);
 gate("reflection_head_193_and_shell_128",2*(N-1)+1===193&&4*M===128);
 gate("core_65_plus_shell_128_is_full_head_193",2*M+1+4*M===193);
 let fullMeanColumn=true;
 for(let a=0;a<2;a++)for(let b=0;b<2;b++)for(const j of[-2*M-1,2*M+1,-N,N])if(!entry(t,a,b,j,0).zero())fullMeanColumn=false;
 gate("mean_columns_retained_and_zero_only_outside_exact_band",fullMeanColumn);
 // Show why the inner primitive may not be cut back to the centre support.
 const test=[new Map([[M,co]]),new Map()];
 const T=scale(mul(t.u,test[0]),c(2)),IP=primitive(T);
 const cut=new Map([...IP].filter(([k])=>Math.abs(k)<=M));
 const lost=mul(sub(IP,cut),t.Qp[0]);
 gate("truncating_intermediate_primitive_to_32_changes_operator",lost.size>0);
 return {
  kind:"exact_complete_moving_Jacobi_band_mean_parameter_algebra",
  arithmetic:"BigInt normalized rational complex Laurent coefficients; no float or FFT",
  source:"scripts/fourfold_codazzi_moving_full_band_exact.mjs",
  intended_centre_sha256:"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
  actual_candidate_coefficients_loaded:false,
  coefficient_fixture:"explicit complete degree-32 rational odd/even fields in this source",
  scope:"Exact formula checks and structural support counts. The proof establishes universal identities. This is not a numerical inverse or a coefficient bound for the intended centre.",
  angular_centre_degree:M,complete_jacobi_band:2*M,parameter_source_degree:3*M,
  structural_head_max_index:N-1,physical_first_high_frequency:4*N,
  reflection_head_dimension:2*(N-1)+1,with_one_parameter_dimension:2*(N-1)+2,
  coupling_shell_first_index:outerFirst,coupling_shell_last_index:N-1,
  reflection_shell_dimension:4*M,inner_core_dimension:2*M+1,
  complete:true,gates,
  exact_samples:{normalized_nu_mean:at(normalized[1],0).str(),physical_C0_nu:directBoundary.str()},
  unproved:["same-centre high inverse gate","finite radial head BVP inverse","complete physical boundary operator tail and its feedback","nonlinear full BVP"]
 };
}
export {runExactAlgebra,makeModel,entry,fullAction,parameter};
// NODE CLI: the core above also runs unchanged in a pure JavaScript isolate.
if(typeof process!=="undefined"&&process.versions?.node&&process.argv[1]?.endsWith("fourfold_codazzi_moving_full_band_exact.mjs")){
 const result=runExactAlgebra();const str=JSON.stringify(result,null,2)+"\n";
 const out=process.argv.indexOf("--out");
 if(out>=0){
  const fs=await import("node:fs");fs.writeFileSync(process.argv[out+1],str);
  process.stdout.write(JSON.stringify({complete:result.complete,gates:result.gates.length,out:process.argv[out+1]})+"\n");
 }else process.stdout.write(str);
}
