#!/usr/bin/env node
// Complete actual-R module/Hilbert budget. No native solver is invoked.
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';

function endpointBudget(){
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
class Q{constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const z=gcd(n,d);this.n=n/z;this.d=d/z;}
 static of(v){if(v instanceof Q)return v;if(typeof v==="string"){if(v.includes("/")){let[n,d]=v.split("/");return new Q(n,d);}if(/[eE.]/.test(v)){let[s,e="0"]=v.toLowerCase().split("e");let neg=s.startsWith("-");if(neg)s=s.slice(1);let[a,b=""]=s.split(".");let n=BigInt((a||"0")+b),d=10n**BigInt(b.length);let k=Number(e);if(k>=0)n*=10n**BigInt(k);else d*=10n**BigInt(-k);return new Q(neg?-n:n,d);}return new Q(v);}return new Q(v);}
 add(v){v=Q.of(v);return new Q(this.n*v.d+v.n*this.d,this.d*v.d);}
 neg(){return new Q(-this.n,this.d);}
 sub(v){return this.add(Q.of(v).neg());}
 mul(v){v=Q.of(v);return new Q(this.n*v.n,this.d*v.d);}
 div(v){v=Q.of(v);return new Q(this.n*v.d,this.d*v.n);}
 abs(){return this.n<0n?this.neg():this;}
 pow(k){if(k<0)return new Q(this.d,this.n).pow(-k);return new Q(this.n**BigInt(k),this.d**BigInt(k));}
 cmp(v){v=Q.of(v);let x=this.n*v.d-v.n*this.d;return x<0n?-1:x>0n?1:0;}
 str(){return this.d===1n?""+this.n:this.n+"/"+this.d;}
}
function dyadic(x){if(!Number.isFinite(x))throw Error("nonfinite input");const a=new ArrayBuffer(8),v=new DataView(a);v.setFloat64(0,x,false);const z=v.getBigUint64(0,false);const sign=(z>>63n)?-1n:1n;const e=Number((z>>52n)&2047n);let n=z&((1n<<52n)-1n);let p=e?e-1023-52:-1074;if(e)n+=1n<<52n;if(p>=0)return new Q(sign*(n<<BigInt(p)));return new Q(sign*n,1n<<BigInt(-p));}
function dec(v,up=false,digits=18){v=Q.of(v);let scale=10n**BigInt(digits),n=v.n*scale,q=n/v.d,r=n%v.d;if(r && ((up&&n>0n)||(!up&&n<0n)))q+=up?1n:-1n;const sign=q<0n?"-":"";q=q<0n?-q:q;return sign+(q/scale)+"."+(q%scale).toString().padStart(digits,"0");}
const gates=[];
function gt(name,x,y){x=Q.of(x);y=Q.of(y);const margin=x.sub(y);if(margin.cmp(0)<=0)throw Error(name+" failed");gates.push({name,passed:true,strict_margin_lower:dec(margin)});}
const one=Q.of(1),piUpper=Q.of("22/7"),sigma=Q.of("1/8");
const psi=Q.of("1.480385e-11"),U=Q.of("1.643190e-9"),V=Q.of("9.603792e-9");
const eps1=psi.div(sigma),eps2=psi.mul(2).div(sigma.pow(2)).div(4),eps3=psi.mul(6).div(sigma.pow(3)).div(16);
gt("actual whole-circle first angle derivative below one quarter","1/4",eps1);
const R0=Q.of("5/12").mul(Q.of("64/39").add("512/693"));
const R1=Q.of(1).div(9).mul(Q.of("5696/1521").add(Q.of("71936/53361").mul("2/3")));
const R2=Q.of("5/216").mul(Q.of("888832/59319").add(Q.of(793*65536).div(231**3).mul("5/48")));
gt("complete cot remainder absolute bound",1,R0);
gt("complete cot remainder first derivative bound",1,R1);
gt("complete cot remainder second derivative bound",1,R2);
const jlo=one.sub(eps1),jhi=one.add(eps1);
const k0=eps2.div(jlo).add(one.add(piUpper).mul(eps1));
const k1=eps3.div(jlo.mul(3)).add(eps2.pow(2).div(jlo.pow(2).mul(2)))
 .add(Q.of(2).add(piUpper).mul(eps1)).add(eps1.pow(2));
const ks=k0.add(k1.mul(4));
gt("complete Hilbert conjugacy L2 kernel bound","1e-9",k0);
gt("complete Hilbert conjugacy first physical derivative bound","7e-9",k1.mul(4));
gt("complete same-Hs Hilbert conjugacy for zero through one","1e-8",ks);
const hilbertInverse=one.div(one.sub(ks));
gt("complete Hilbert Robin leading row inverse","1.000000011",hilbertInverse);
const reg=one.div(new Q(1n<<512n));
const qmin=Q.of(".99999999999936").sub(reg);
gt("actual all-mode regular multiplier is positive",qmin,".9999999999993");
gt("actual all-mode regular multiplier upper below one",1,Q.of(".99999999999937").add(reg));
const rb=one.div(new Q(1n<<60n));
const mMin=Q.of("5.8"),vMax=Q.of(7),wMax=Q.of(1).div(800000);
const cRefLower=one.div(Q.of(6).mul(one.add(wMax.pow(2))));
const meanCentreError=Q.of("6.055e-43");
gt("actual centre mean remains below 6.1 in modulus",cRefLower.sub(meanCentreError),one.div("6.1"));
gt("actual centre v bounded in modulus by seven",vMax,Q.of("6.1").add(V));
gt("actual complete v gap exceeds chosen 5.8",Q.of("5.84461145233").sub(V),mMin);
const up=U.div(sigma),vp=V.div(sigma);
const Cchi=one.add(vMax.div(mMin)).div(mMin.mul(4));
const recover=jhi.mul(one.add(vp.mul(Cchi))).div(mMin.pow(2));
gt("full moving h2 to physical nonmean curvature recovery","3/100",recover);
const cases={};
for(const rzText of ["1e-12","1e-10"]){
 const rz=Q.of(rzText),rf=Q.of(10).mul(rz.add(rb)),F=rf.add(rb);
 const kap=Q.of(36*4096).mul(F);
 const Jf=Q.of(9).div(one.sub(kap)),JB=reg.add(kap).div(one.sub(kap));
 const ld=reg.add(Q.of(4*16384).mul(F).mul(Jf));
 const lmean=Q.of(4*2048).mul(F).mul(Jf);
 const ldB=reg.add(Q.of(4*16384).mul(F).mul(one.add(JB)));
 const lmeanB=Q.of(4*2048).mul(F).mul(one.add(JB));
 const graphInv=one.div(qmin.sub(ld));
 const lift=one.div(jlo),fg=lift.mul(one.add(ld)),gg=lift.mul(one.add(lmean));
 const h1=vMax.mul(fg).add(vMax.mul(U.add(up.div(4))).mul(gg));
 const h2=vMax.pow(2).add(vp.mul(vMax).div(4)).mul(gg);
 const pairSquared=h1.pow(2).add(h2.pow(2));
 const meanMov=vMax.pow(2).mul(lmean);
 gt(rzText+" full dual-module long input ball",one.div(new Q(1n<<25n)),F.mul(2));
 gt(rzText+" C-to-height full L2 derivative contraction",1,kap);
 gt(rzText+" true physical nonlinear B/C derivative invertible",qmin,ld);
 gt(rzText+" full moving outer graph L2 lift below fifty squared",2500,pairSquared);
 const local=rzText==="1e-12";
 gt(rzText+" complete nonlinear regular row derivative",local?"6e-6":".0006",ld);
 gt(rzText+" independent true cap mean derivative",local?"8e-7":".00008",lmean);
 gt(rzText+" full physical B-to-nonmean-C inverse",local?"1.000007":"1.000601",graphInv);
 gt(rzText+" complete moving mean output retained",local?".00004":".004",meanMov);
 cases[rzText]={exact_input_radius:rz.str(),exact_independent_fB_bound:rb.str(),
  C_to_height_L2_contraction_upper:dec(kap,true),
  C_to_dotH2_height_derivative_upper:dec(Jf,true),
  independent_fB_to_dotH2_height_derivative_upper:dec(JB,true),
  true_nonmean_regular_graph_L2_derivative_remainder_upper:dec(ld,true),
  true_cap_mean_L2_derivative_upper:dec(lmean,true),
  independent_fB_to_regular_graph_L2_derivative_upper:dec(ldB,true),
  independent_fB_to_cap_mean_L2_derivative_upper:dec(lmeanB,true),
  complete_physical_B_to_nonmean_C_L2_inverse_upper:dec(graphInv,true),
  full_moving_graph_first_component_upper:dec(h1,true),
  full_moving_graph_second_component_upper:dec(h2,true),
  full_moving_graph_pair_norm_squared_upper:dec(pairSquared,true),
  full_moving_graph_pair_norm_coarse_upper:"50",
  moving_mean_output_coefficient_upper:dec(meanMov,true)};
}
return{kind:"actual_final_regular_end_full_L2_module_and_Hilbert_Robin_budget",
 complete:true,executed:true,arithmetic:"Exact JavaScript BigInt rationals; existing complete endpoint and original tail bounds consumed.",
 candidate_sha256:"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
 endpoint:"25/8",whole_original_affine_parameter_interval:true,all_fourier_modes_and_means_retained:true,
 intrinsic_or_candidate_native_recomputed:false,
 actual_psi_strip_A0_upper:psi.str(),actual_strip:sigma.str(),
 actual_u_strip_A0_upper:U.str(),actual_v_nonmean_strip_A0_upper:V.str(),
 angle_derivative_error_upper:dec(eps1,true),
 normalized_angle_second_derivative_upper:dec(eps2,true),
 normalized_angle_third_derivative_upper:dec(eps3,true),
 cot_regular_remainder_bounds:{zero:dec(R0,true),one:dec(R1,true),two:dec(R2,true)},
 Hilbert_conjugacy_L2_error_upper:dec(k0,true),
 Hilbert_conjugacy_same_Hs_zero_to_one_error_upper:dec(ks,true),
 complete_Hilbert_leading_Robin_inverse_upper:dec(hilbertInverse,true),
 full_physical_curvature_recovery_from_moving_h2_upper:dec(recover,true),
 same_space_composition_minus_identity_not_claimed_small:true,
 nonlinear_L2_neighbourhood_existence_not_claimed:true,
 full_body_BVP_inverse_proved:false,nu_scalar_Schur_proved_nonzero:false,
 fixed_fB_not_set_to_zero:true,independent_mean_height_remains:true,far_label_equation_not_solved:true,
 cases,gate_count:gates.length,gates};
}

const result=endpointBudget();
result.producer_sha256=createHash('sha256').update(readFileSync(new URL(import.meta.url))).digest('hex');
process.stdout.write(JSON.stringify(result,null,2)+'\n');
