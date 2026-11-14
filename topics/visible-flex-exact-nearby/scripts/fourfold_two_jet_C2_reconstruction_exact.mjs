#!/usr/bin/env node
// R117 universal C0 -> C1 compatibility projection and C1 -> C2
// compatible strain reconstruction. These gates certify the proved constants,
// not a numerical geometric candidate or a nonlinear inverse.
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r;}return a;}
function F(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g];}
const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const sub=(a,b)=>F(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);
const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]);
const div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
function pow(a,n){let b=F(1);for(let k=0;k<n;k++)b=mul(b,a);return b;}
const cmp=(a,b)=>a[0]*b[1]-b[0]*a[1];
const str=a=>a[1]===1n?String(a[0]):a[0]+"/"+a[1];

export function certifyTwoJetReconstruction(){
 const gates=[];
 function gate(name,a,b,strict=true){
  const ok=strict?cmp(a,b)<0n:cmp(a,b)<=0n;
  gates.push({name,left:str(a),relation:strict?"<":"<=",right:str(b),passed:ok});
  if(!ok)throw Error("unpaid R117 gate: "+name);
 }
 let sum=F(0),term=F(1);
 for(let n=0;n<8;n++){if(n)term=mul(term,F(2,n));sum=add(sum,term);}
 const term8=mul(term,F(2,8));
 const exp2Upper=add(sum,div(term8,sub(F(1),F(2,9))));
 gate("complete positive Taylor envelope for exp(2)",exp2Upper,F(8));
 gate("exp(1) exceeds two already at order two",F(2),F(5,2));
 gate("sqrt(2) below 3/2",F(2),F(9,4));
 gate("sqrt(3) below 7/4",F(3),F(49,16));
 gate("1/sqrt(2) below 3/4",F(1,2),F(9,16));
 gate("(3/2)^(3/2) below 15/8",F(27,8),F(225,64));
 const q=F(1,64),gap=sub(F(1),q);
 const spectral=add(div(F(5),gap),div(mul(F(2),q),pow(gap,2)));
 gate("all l>=2 heat-kernel spectral tail",spectral,F(9));
 const small=[F(8),F(8),F(16),F(60)];
 const large=[F(3,2),F(3,2),F(3),F(63,8)];
 const psi=[F(10),F(10),F(19),F(68)];
 for(let j=0;j<=3;j++)gate("integrated "+j+" rotation derivatives",
  add(small[j],large[j]),psi[j],j!==2);
 const grad=mul(F(7,4),psi[1]);
 const Hess=add(mul(F(3),psi[2]),grad);
 const third=add(add(mul(F(21,4),psi[3]),mul(F(5,2),grad)),mul(F(3),Hess));
 gate("scalar gradient",grad,F(35,2),false);
 gate("covariant Hessian from rotation derivatives",Hess,F(149,2),false);
 gate("covariant third derivative with all frame terms",third,F(2497,4),false);
 const T0=add(add(mul(F(3),Hess),mul(F(3,2),psi[0])),F(3,4));
 const T1=add(mul(F(3),third),mul(F(3,2),grad));
 gate("projection tensor C0 including retained constant mode",T0,F(256));
 gate("projection tensor first derivative",T1,F(2048));
 // pi < 22/7 follows from the elementary Machin enclosure in R104/R110.
 // All remaining upper bounds use only this exact rational and sqrt(3)/2<7/8.
 gate("sqrt(3)/2 below 7/8",F(3,4),F(49,64));
 const omega=mul(F(22,7),F(7,8));
 gate("global geodesic primitive",omega,F(11,4),false);
 const p1=add(F(1,2),mul(F(3,2),omega));
 const p2=add(F(3,2),mul(F(3,2),omega));
 gate("compatible primitive first derivative",p1,F(37,8),false);
 gate("compatible primitive second derivative",p2,F(45,8),false);
 gate("complete C1 to C2 primitive norm",p2,F(6));
 // Etilde = rho^2 f - 2 rho w sigma + sym(dw tensor d rho).
 gate("rho squared times strain C1 coefficient",add(F(1),F(2)),F(3),false);
 gate("minus 2 rho w sigma C1 coefficient",mul(F(4),F(3,2)),F(6),false);
 gate("complete w part C1 coefficient",add(F(6),F(4)),F(10),false);
 const primitiveProjection=mul(F(6),F(2048));
 const capProjection=mul(F(1024),F(2048));
 gate("whole-cap projection correction",capProjection,F(2n**21n),false);
 gate("global plus whole-cap compatible source fee",add(primitiveProjection,capProjection),F(2n**22n));
 gate("physical scalar times tangent field C2 coefficient",
   add(add(F(9,2),F(4)),F(1)),F(10));
 gate("complete ambient C2 of w times sphere position",add(F(1),mul(F(3),F(3,2))),F(6));
 return {kind:"R117_two_jet_source_and_C2_reconstruction_universal_constants",
  complete:true,arithmetic:"exact reduced BigInt rational inequalities, complete exponential series tail",
  norms:"scalar/tensor intrinsic derivatives use spherical Hilbert-Schmidt point norms; physical vector derivatives use the sphere connection on inputs and ambient output",
  heat_psi_rotation_derivative_bounds:psi.map(str),
  scalar_gradient_bound:str(grad),scalar_Hessian_bound:str(Hess),scalar_third_derivative_bound:str(third),
  compatibility_projection_C0_bound:str(T0),compatibility_projection_C1_bound:str(T1),
  rounded_C0_to_C1_projection_constant:"2048",
  compatible_strain_C1_to_tangent_C2_constant:"6",
  with_whole_cap_tangent_C2_bound:"18 A^2 F + 60 A W + 2^22 H",
  physical_C2_bound:"10 B (18 A^2 F + 60 A W + 2^22 H) + 6 W",
  notation:{A:"||rho||C2",B:"||1/rho||C2",F:"||desired strain||C1",W:"||radial correction||C2",H:"||complete compatibility residual||C0"},
  retains_scalar_mean:true,degree_one_source:"required orthogonality is automatic for an actual complete compatibility residual",
  third_geometry_derivatives_required:false,
  high_Sobolev_or_material_analytic_norms_paid:false,
  actual_candidate_inverse_paid:false,nonlinear_convergence_paid:false,
  gates,passed_gates:gates.length};
}

if(typeof process!=="undefined" &&
 process.argv[1]?.endsWith("fourfold_two_jet_C2_reconstruction_exact.mjs")){
 Promise.all([import("node:fs"),import("node:crypto")]).then(([fs,crypto])=>{
  const report=certifyTwoJetReconstruction();
  report.source_sha256=crypto.createHash("sha256").update(fs.readFileSync(process.argv[1])).digest("hex");
  report.execution="Node CLI exact universal kernel";
  const i=process.argv.indexOf("--out"),out=JSON.stringify(report,null,2)+"\n";
  if(i<0)process.stdout.write(out);
  else {if(!process.argv[i+1])throw Error("--out path required");fs.writeFileSync(process.argv[i+1],out);}
 }).catch(e=>{process.stderr.write(String(e)+"\n");process.exitCode=1;});
}
