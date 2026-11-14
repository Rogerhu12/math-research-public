#!/usr/bin/env node
// R116: exact angular-coordinate and tame-density constants from the
// already completed, continuous R106 true-ray certificate.
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r;}return a;}
function F(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g];}
function rat(s){const a=String(s).split("/");return F(a[0],a[1]??1);}
const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const sub=(a,b)=>F(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);
const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]);
const div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
function pow(a,n){let b=F(1);while(n-->0)b=mul(b,a);return b;}
const cmp=(a,b)=>a[0]*b[1]-b[0]*a[1];
const str=a=>a[1]===1n?String(a[0]):a[0]+"/"+a[1];
const INPUT="notes/2026-11-12-R106-actual-all-time-ray-tube.json";
const INPUT_SHA="6463e62641b9187045016c63ee633816676a75baf941ea01375a6ae36f1a1863";

export function certifyAngularMaps(input,inputSha){
 const g=[];
 function identity(name,ok){g.push({name,passed:!!ok});if(!ok)throw Error("unpaid identity: "+name);}
 function gate(name,a,b,strict=true){
  const ok=strict?cmp(a,b)<0n:cmp(a,b)<=0n;
  g.push({name,left:str(a),relation:strict?"<":"<=",right:str(b),passed:ok});
  if(!ok)throw Error("unpaid rational gate: "+name);
 }
 identity("complete paid input bytes",inputSha===INPUT_SHA && input.complete===true);
 identity("same full forward leg and 550 segments",
  input.proved_region.leg==="forward" && input.proved_region.segments===550 &&
  JSON.stringify(input.proved_region.time_endpoints)===JSON.stringify(["-pi/2","pi/2"]));
 identity("whole actual parameter interval",
  input.proved_region.parameter_center==="-7789843107295549/4611686018427387904" &&
  input.proved_region.parameter_half_width==="1/1000000000");
 identity("physical angle and label periods are not conflated",
  input.proved_region.label_period==="2*pi" &&
  input.proved_region.physical_angle==="theta; reference Y(x+2*pi)=Y(x)+pi/2");
 identity("same actual affine geometry",
  input.provenance.actual_object_sha256==="91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848");
 identity("all upstream gates passed",input.gates.length===24 && input.gates.every(x=>x.passed));
 const jp=rat(input.bounds.true_label_J_real_lower.exact);
 const Jp=rat(input.bounds.true_label_J_modulus.exact);
 const second=rat(input.bounds.true_second_label_derivative.exact);
 identity("exact actual Jacobian fractions",
  str(jp)==="213831/7812500" && str(Jp)==="8223669/7812500");
 gate("positive physical label derivative",F(0),jp);
 gate("paid physical second derivative below 1100",second,F(1100));
 // psi=4 Theta is the degree-one self-map of the 2pi circle.
 const m=mul(F(4),jp),M=mul(F(4),Jp),L=F(4400),R=div(M,m);
 gate("normalized derivative lower bound below one",m,F(1));
 gate("normalized derivative upper bound above one",F(1),M);
 gate("m times M below one",mul(m,M),F(1));
 const A=F(3023,1000),C=F(2052,1000),H=F(2491,1000),B=F(3101,500);
 gate("one-leg L2 and H1 forward bound, squared",div(F(1),m),pow(A,2));
 gate("one-leg L2 inverse bound, squared",M,pow(C,2));
 gate("one-leg Hhalf inverse bound, fourth power",R,pow(H,4));
 gate("relative full Hs, zero<=s<=1, both directions, squared",R,pow(B,2));
 gate("relative derivative upper bound",R,F(38459,1000));
 // The H2 chain rule uses the exact discrete derivative norm
 // sup_{k != 0} kappa^2 |k|/(1+kappa^2 k^2)=kappa^2/(1+kappa^2).
 gate("one-leg principal H2 bound",mul(M,C),F(9));
 gate("one-leg forward zeroth term below principal H2 budget",A,F(9));
 gate("inverse principal H2 bound",div(A,m),F(28));
 gate("inverse zeroth term below principal H2 budget",C,F(28));
 const Linv=div(L,pow(m,3));
 const rows=[];
 for(const [k,forwardH2,inverseH2,forwardH54,inverseH54] of [
  [1,6660,3441000,21,99],[4,12528,6477000,25,116]]){
  const q=F(k*k,1+k*k);
  const D=add(F(9),mul(mul(q,L),A));
  const Di=add(F(28),mul(mul(q,Linv),C));
  gate("kappa="+k+" complete forward H2",D,F(forwardH2));
  gate("kappa="+k+" complete inverse H2",Di,F(inverseH2));
  gate("kappa="+k+" forward H5/4, fourth power",
       mul(pow(A,3),F(forwardH2)),pow(F(forwardH54),4));
  gate("kappa="+k+" inverse H5/4, fourth power",
       mul(pow(A,3),F(inverseH2)),pow(F(inverseH54),4));
  rows.push({kappa:String(k),forward_H2:String(forwardH2),
    inverse_H2:String(inverseH2),forward_H5over4:String(forwardH54),
    inverse_H5over4:String(inverseH54)});
 }
 // ln(2)=2 atanh(1/3); the remainder after k=0,1,2 is
 // <= 2/(7*3^7)*(1-1/9)^-1 = 2/13608.
 const log2=mul(F(2),add(add(add(F(1,3),F(1,81)),F(1,1215)),F(1,13608)));
 gate("complete log2 geometric-tail envelope",log2,F(7,10));
 gate("sqrt(2 log2) below 6/5, squared",mul(F(2),log2),F(36,25));
 const relativeL=div(mul(L,add(M,m)),pow(m,3));
 const tame=[];
 for(const [k,rootK,fee,invFee,relFee] of [
  [1,1,15962,8256400,107803000],
  [4,2,31924,16512800,215606000]]){
  const c=F(6*rootK,5);
  gate("kappa="+k+" forward density lower-to-higher fee",mul(mul(c,L),A),F(fee));
  gate("kappa="+k+" inverse density lower-to-higher fee",mul(mul(c,Linv),C),F(invFee));
  gate("kappa="+k+" relative density lower-to-higher fee",mul(mul(c,relativeL),B),F(relFee));
  tame.push({kappa:String(k),forward_base:str(C),forward_high:str(M),
    forward_lower_to_higher:String(fee),inverse_base:str(A),inverse_high:str(div(F(1),m)),
    inverse_lower_to_higher:String(invFee),relative_base:str(B),
    relative_high:str(R),relative_lower_to_higher:String(relFee)});
 }
 return {kind:"R116_actual_true_ray_angular_Sobolev_and_density_constants",
  complete:true,arithmetic:"exact reduced BigInt fractions; positive powers remove all square/fourth roots",
  input:{path:INPUT,sha256:INPUT_SHA},actual_object_sha256:input.provenance.actual_object_sha256,
  parameter:input.proved_region,normalized_self_map:"psi=4 Theta; period 2pi on both sides",
  normalized_m:str(m),normalized_M:str(M),normalized_second_derivative:str(L),
  relative_derivative_ratio:str(R),relative_second_derivative:str(relativeL),
  one_leg:{height_Hhalf_forward:str(A),height_Hhalf_inverse:str(H),
    density_Hminus_half_forward:str(H),density_Hminus_half_inverse:str(A),
    common_scale_symplectic_port_both_directions:str(A),
    homogeneous_Hhalf_both_directions:str(H)},
  relative:{height_Hs_both_directions_for_0_le_s_le_1:str(B),
    density_Hminus_s_both_directions_for_0_le_s_le_1:str(B),
    common_scale_symplectic_port_both_directions:str(B)},
  strong_height:rows,tame_density_Hplus_half:tame,
  tame_norm:"mean^2 + kappa sum_{k!=0}|k| |f_k|^2; mean retained exactly",
  coordinate_change_only:true,full_strong_propagator_proved:false,
  final_KAM_frame_paid:false,full_PDE_inverse_proved:false,nonlinear_family_proved:false,
  gates:g,passed_gates:g.length};
}

if(typeof process!=="undefined" &&
 process.argv[1]?.endsWith("fourfold_true_ray_Sobolev_coordinates_exact.mjs")){
 Promise.all([import("node:fs"),import("node:crypto"),import("node:path")]).then(([fs,crypto,path])=>{
  const sha=s=>crypto.createHash("sha256").update(s).digest("hex");
  const rootIndex=process.argv.indexOf("--root");
  const root=rootIndex<0?process.cwd():process.argv[rootIndex+1];
  const bytes=fs.readFileSync(path.join(root,INPUT));
  const report=certifyAngularMaps(JSON.parse(bytes.toString("utf8")),sha(bytes));
  report.source_sha256=sha(fs.readFileSync(process.argv[1]));
  report.execution="Node CLI; byte-checked original continuous R106 input";
  const outIndex=process.argv.indexOf("--out"),out=JSON.stringify(report,null,2)+"\n";
  if(outIndex<0)process.stdout.write(out);
  else {if(!process.argv[outIndex+1])throw Error("--out path required");fs.writeFileSync(process.argv[outIndex+1],out);}
 }).catch(e=>{process.stderr.write(String(e)+"\n");process.exitCode=1;});
}
