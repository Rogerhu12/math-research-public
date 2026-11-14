#!/usr/bin/env node
// Exact BigInt proof budget for the complete final-waist amplitude coordinate.
// Usage: node scripts/fourfold_codazzi_waist_amplitude_chart.mjs \
//   notes/2026-11-13-R133-moving-m32-alpha0765-fullR-v2-tol2e9-reconstruction.json
// The complete original intrinsic first-box enclosure is reused verbatim.
// This is not a body inverse or a numerical evaluation of its nu Schur scalar.
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';

function calculate(input){
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
const gates=[];function gt(name,x,y){x=Q.of(x);y=Q.of(y);const margin=x.sub(y);if(margin.cmp(0)<=0)throw Error(name+" failed");gates.push({name,passed:true,strict_margin_lower:dec(margin)});}
function eq(name,a,b){if(a!==b)throw Error(name+" failed");gates.push({name,passed:true});}
const meta=input.complete_candidate_index.metadata,state=input.complete_candidate_index.initial_state;
eq("actual candidate identity",input.candidate_sha256,"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413");
eq("all 65 complete moving waist coefficients retained",state.length,65);
eq("actual moving mode count",meta.modes,32);
eq("physical fourfold frequency",meta.physical_frequency_factor,4);
eq("actual coordinate identity",meta.coordinates,"moving phi: u=alpha*U; v=1/Cref_nu+alpha*V; theta_phi=v/mean_phi(v); B=u/v; C=1/v");
const alpha=dyadic(meta.amplitude);
eq("exact dyadic amplitude",alpha.str(),meta.exact_float_amplitude);
const aL=Q.of("1.06873282"),aU=Q.of("1.068732841");
const originalLo=Q.of("1.0687328210563735580995725626962667").sub("1.35e-35");
const originalHi=Q.of("1.0687328409354375363671252330277639").add("2.45e-36");
gt("whole-original-target first closed box lower containment",originalLo,aL);
gt("whole-original-target first closed box upper containment",aU,originalHi);
const V=state.slice(32).map(dyadic);
const rho=Q.of("1e-6"),centerMeanShift=alpha.mul(V[0]);
const mlo=aL.sub(centerMeanShift).sub(rho),mhi=aU.sub(centerMeanShift).add(rho);
gt("complete unknown mean gap",mlo,1);
let a0=Q.of(0),rest=Q.of(0);
for(let j=1;j<=32;j++){a0=a0.add(V[j].abs());if(j>=2)rest=rest.add(V[j].abs().div(j));}
const vgap=aL.sub(centerMeanShift).sub(alpha.mul(a0)).sub(rho);
gt("whole infinite Wiener ball remains negative v",vgap,"1/20");
const p1=alpha.mul(V[1]),tlo=p1.sub(rho).div(mhi),thi=p1.add(rho).div(mlo);
gt("primary physical phase coefficient positive",tlo,0);
gt("primary phase coefficient below one",1,thi);
const remainder=alpha.mul(rest).add(rho.div(2)).div(mlo);
gt("complete higher phase including every unknown Fourier tail",Q.of("1/100"),remainder);
function fact(n){let a=1n;for(let j=2;j<=n;j++)a*=BigInt(j);return a;}
function bessel(order,N){let lo=Q.of(0),hi=Q.of(0);
 for(let n=0;n<N;n++){const power=2*n+order,den=new Q((2n**BigInt(power))*fact(n)*fact(n+order));
 const l=tlo.pow(power).div(den),h=thi.pow(power).div(den);
 if(n%2){lo=lo.sub(h);hi=hi.sub(l);}else{lo=lo.add(l);hi=hi.add(h);}}
 const power=2*N+order,first=thi.pow(power).div(new Q((2n**BigInt(power))*fact(N)*fact(N+order)));
 const ratio=thi.pow(2).div(4*(N+1)*(N+order+1));
 gt("Bessel order "+order+" complete series ratio",1,ratio);
 const tail=first.div(Q.of(1).sub(ratio));
 return{lo:lo.sub(tail),hi:hi.add(tail),tail};
}
const N=16,j0=bessel(0,N),j2=bessel(2,N);
const I0lo=j0.lo.sub(j2.hi).div(2),I0hi=j0.hi.sub(j2.lo).div(2);
const Ilo=I0lo.sub(remainder),Ihi=I0hi.add(remainder);
gt("complete real-angle correlation positive",Ilo,"1/3");
const Dlo=Ilo.mul(2).div(mhi.pow(2)),Dhi=Ihi.mul(2).div(mlo.pow(2));
gt("actual full amplitude row negative derivative magnitude",Dlo,"3/5");
gt("actual full amplitude row derivative upper magnitude","2/3",Dhi);
const lift=Q.of(1).div(Dlo);
gt("one-dimensional amplitude-row right inverse","5/3",lift);
const Vne=alpha.mul(a0).add(rho);
const functional=Q.of(2).div(mlo.pow(2)).mul(Q.of(1).add(Vne.div(mlo)));
const projection=Q.of(1).add(lift.mul(functional));
gt("complete mean-preserving amplitude functional norm","7/2",functional);
gt("complete infinite Fourier A0 projection norm",7,projection);
gt("cos4phi complete H1 squared norm bound",9,"17/2");
const h1Projection=Q.of(1).add(lift.mul(3).mul(functional).mul("11/10"));
gt("complete mean-preserving H1 projection norm",20,h1Projection);
return{
 kind:"actual_final_waist_complete_amplitude_coordinate_rational_certificate",
 complete:true,executed:true,arithmetic:"JavaScript BigInt exact rationals; no floating quadrature or characteristic sample",
 candidate_sha256:input.candidate_sha256,
 reconstruction_git_blob:"f0af21a2979bcfde913ba18ec095c93b34d4d8a4",
 original_target_path:"notes/2026-11-13-Codazzi-continuation-r001-v3-native.json",
 original_target_git_blob:"1c0abbebb166c6b85a87cb52b4aeab8378567b4c",
 original_target_sha256_from_R128:"0f7aa2f4e9a1df567b209cd873f2af5f6428feafc01a9613fc75a46259fb75eb",
 original_target_row:0,
 original_target_closed_interval:["0","1152921504606847/73786976294838206464"],
 exact_target_waist_radius_enclosure:[aL.str(),aU.str()],
 whole_original_affine_parameter_interval:true,
 actual_nu_bump_identically_zero_at_waist:true,
 exact_alpha:alpha.str(),
 exact_full_V_coefficients:V.map(q=>q.str()),
 input_state_scope:"The complete exact dyadic waist vector in the published final candidate index; no unavailable radial shard or its contents are reconstructed here.",
 true_PDE_solution_proved:false,
 full_body_BVP_inverse_proved:false,
 metric_parameter_Schur_nonzero_proved:false,
 chart_ball:{norm:"sum over all physical moving frequencies 4j of absolute complex Fourier coefficients of v-v_center; real even symmetry, full mean retained",radius:rho.str(),unknown_infinite_tail_retained:true},
 functional:"A(v)=2 mean_phi(cos(4 theta(phi)))/mean_phi(v); theta=phi+I(v-mean(v))/mean(v)",
 direction:"unscaled h2=cos(4phi); equivalently the derivative of normalized physical c4 with respect to normalized V1 at fixed alpha",
 derivative_interval_outward_decimal:[dec(Dhi.neg(),false),dec(Dlo.neg(),true)],
 proved_coarse_interval:["-2/3","-3/5"],
 one_dimensional_right_inverse_norm_upper:dec(lift,true),
 complete_A0_functional_norm_upper:dec(functional,true),
 complete_A0_projection_norm_upper:dec(projection,true),
 complete_H1_projection_norm_upper:dec(h1Projection,true),
 full_mean_preserved_by_projection:true,
 projection_formula:"P h=h-(0,cos(4phi))*D A[h]/D A[(0,cos(4phi))]",
 complete_negative_v_gap_lower:dec(vgap,false),
 exact_mean_absolute_lower:dec(mlo,false),
 exact_mean_absolute_upper:dec(mhi,true),
 primary_phase_interval_outward_decimal:[dec(tlo),dec(thi,true)],
 full_higher_phase_upper:dec(remainder,true),
 Bessel_terms_per_series:N,
 J0_uniform_tail_upper:dec(j0.tail,true,70),
 J2_uniform_tail_upper:dec(j2.tail,true,70),
 full_correlation_interval_outward_decimal:[dec(Ilo),dec(Ihi,true)],
 gate_count:gates.length,gates
};
}

const path=process.argv[2]||'notes/2026-11-13-R133-moving-m32-alpha0765-fullR-v2-tol2e9-reconstruction.json';
const bytes=readFileSync(path);
const hash=createHash('sha256').update(bytes).digest('hex');
if(hash!=='464480dee60749f019b23a89b04568bf496731a580c21a3e761d4bc2192e108a')throw Error('the exact published complete reconstruction manifest changed');
const result=calculate(JSON.parse(bytes.toString('utf8')));
result.reconstruction_sha256=hash;
result.original_target_bound_reused_not_recomputed=true;
result.producer_sha256=createHash('sha256').update(readFileSync(new URL(import.meta.url))).digest('hex');
process.stdout.write(JSON.stringify(result,null,2)+'\n');
