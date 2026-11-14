#!/usr/bin/env node
// Exact rational gates for R114. No geometric numerical input is inferred.
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r;}return a;}
function F(n,d=1n){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g];}
const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>F(-a[0],a[1]);
const sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]);
const div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
function pow(a,n){let b=F(1);for(let j=0;j<n;j++)b=mul(b,a);return b;}
const cmp=(a,b)=>a[0]*b[1]-b[0]*a[1];
const str=a=>a[1]===1n?String(a[0]):a[0]+"/"+a[1];

export function certifyCapRepair(){
 const gates=[];
 function gate(name,left,right,strict=false){
  const pass=strict?cmp(left,right)<0n:cmp(left,right)<=0n;
  gates.push({name,left:str(left),relation:strict?"<":"<=",right:str(right),passed:pass});
  if(!pass)throw Error("unpaid cap repair gate: "+name);
 }
 const r=F(1,8),R=F(1,4),one=F(1),two=F(2);
 // arcsin(r) <= r/sqrt(1-r^2) < 1/7; norm D Omega <= sqrt(3)/2 B < 7/8 B.
 gate("geodesic radius below 1/7, squared",div(pow(r,2),sub(one,pow(r,2))),F(1,49),true);
 gate("D Omega sqrt(3)/2 below 7/8, squared",F(3,4),F(49,64),true);
 gate("sqrt(2) below 3/2, squared",F(2),F(9,4),true);
 const q0=F(1,8),q1=F(11,16),q2=F(27,16);
 const L=F(65,64),M=F(33,32);
 gate("inner chart first derivative",div(one,sub(one,pow(r,2))),pow(L,2));
 gate("inner chart second derivative",div(one,pow(sub(one,pow(r,2)),3)),pow(M,2));
 const Q2=add(add(add(mul(pow(L,2),q2),mul(mul(r,M),q1)),
                       mul(mul(mul(two,r),pow(L,2)),q1)),
                add(mul(mul(pow(r,2),M),q0),mul(L,q0)));
 gate("horizontal coordinate Hessian",Q2,F(9,4));
 const weights=[3,-3,1],nodes=[0,-1,-2];
 for(let m=0;m<=2;m++){
  let total=0;for(let j=0;j<3;j++)total+=weights[j]*nodes[j]**m;
  if(total!==1)throw Error("boundary jet identity failed");
  gates.push({name:"boundary normal jet "+m,left:String(total),relation:"=",right:"1",passed:true});
 }
 // D^2(x/|x|) has bilinear norm 2/sqrt(3)/s^2, proved in R114.
 gate("radial projection Hessian rational majorant, squared",F(4,3),F(49,36));
 gate("quintic cutoff radial Hessian rational majorant, squared",F(1600,3),F(4900,9));
 const E0=F(7,2),E1=F(8),E2=F(24),chi1=F(15,4),chi2=F(70,3);
 const extSecond=add(add(E2,mul(mul(two,chi1),E1)),mul(chi2,E0));
 gate("reflection remainder C2 coefficient",extSecond,F(166));
 const taylorDerivative=F(1,2),coordinateHessian=F(9,4);
 const Qext0=add(mul(R,taylorDerivative),mul(mul(E0,pow(r,2)),coordinateHessian));
 const Qext1=add(mul(F(19,4),taylorDerivative),
                  mul(mul(add(E1,mul(chi1,E0)),r),coordinateHessian));
 const Qext2=add(mul(div(F(185,6),R),taylorDerivative),
                  mul(F(166),coordinateHessian));
 gate("full coordinate extension C0",Qext0,F(1,4));
 gate("full coordinate extension C1",Qext1,F(17,2));
 gate("full coordinate extension C2",Qext2,F(436));
 const LR=F(17,16),MR=F(9,8);
 gate("outer chart first derivative",div(one,sub(one,pow(R,2))),pow(LR,2));
 gate("outer chart second derivative",div(one,pow(sub(one,pow(R,2)),3)),pow(MR,2));
 gate("outer chart third derivative below 1, squared",
      div(mul(F(9),pow(R,2)),pow(sub(one,pow(R,2)),5)),one,true);
 const b0=mul(LR,F(1,4));
 const b1=add(mul(LR,F(17,2)),mul(MR,F(1,4)));
 const b2=add(add(mul(LR,F(436)),mul(mul(two,MR),F(17,2))),F(1,4));
 gate("ambient b C0",b0,F(17,64));
 gate("ambient b C1",b1,F(149,16));
 gate("ambient b C2",b2,F(3861,8));
 const intrinsic2=mul(two,add(add(b2,mul(R,b1)),b0));
 gate("intrinsic Hessian HS coefficient",intrinsic2,F(15527,16));
 gate("intrinsic C0 below 1024",b0,F(1024),true);
 gate("intrinsic C1 HS below 1024",mul(F(3,2),b1),F(1024),true);
 gate("intrinsic C2 HS below 1024",intrinsic2,F(1024),true);
 return {
  kind:"R114_exact_whole_cap_C2_repair_from_C1_strain_constants",
  complete:true,arithmetic:"signed BigInt reduced rationals; square comparisons only for positive quantities",
  normalized_input:"B=max(||T||_infty,||nabla T||_infty) in spherical Hilbert-Schmidt point norms",
  cap_graph_radius_maximum:"1/8",fixed_support_graph_radius:"1/4",
  reflection_weights:weights,reflection_nodes:nodes,reflection_outer_radius:"3r/2",
  local_coordinate_hessian_coefficient:str(Q2),
  remainder_C2_coefficient:str(extSecond),
  extension_coordinate_C012:[Qext0,Qext1,Qext2].map(str),
  extension_ambient_C012:[b0,b1,b2].map(str),
  extension_intrinsic_Hessian_HS_coefficient:str(intrinsic2),
  uniform_C2_repair_constant:"1024",
  repaired_strain_C1_additional_constant:"2048",
  gates,passed_gates:gates.length,
  mathematical_scope:"Assumes exactly the compatible tensor and normalized local reconstruction in the proved R114 theorem. It certifies its explicit constants, not an actual nonlinear solution.",
  full_strong_tail_proved:false,full_PDE_inverse_proved:false,nonlinear_convergence_proved:false
 };
}

if(typeof process!=="undefined" && process.argv[1]?.endsWith("fourfold_whole_cap_C1_repair_exact.mjs")){
 Promise.all([import("node:fs"),import("node:crypto")]).then(([fs,crypto])=>{
  const report=certifyCapRepair();
  report.source_sha256=crypto.createHash("sha256").update(fs.readFileSync(process.argv[1])).digest("hex");
  const text=JSON.stringify(report,null,2)+"\n";
  const i=process.argv.indexOf("--out");
  if(i>=0){if(!process.argv[i+1])throw Error("--out path required");fs.writeFileSync(process.argv[i+1],text);}
  else process.stdout.write(text);
 }).catch(error=>{process.stderr.write(String(error)+"\n");process.exitCode=1;});
}
