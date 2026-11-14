#!/usr/bin/env node
// Exact current-centre full waist projection. This does not execute the
// radial Python trial factory and does not prove a whole BVP inverse.
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
const CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413";
const INPUT_SHA="c99e3f6c7fd4975ee8fd1de26fadad7f4e42c6c379a861830d6fa419046b052e";
const HIGH_SHA="19fc31617d033a4dcdc92153498592290da23ae58b545f3c5f64dc0ca343a3d9";
const input=process.argv[2]??"notes/2026-11-14-R133-final-waist-complete-96-amplitude-row-rational.json";
const high=process.argv[3]??"notes/2026-11-14-R133-final-waist-high-amplitude-tail-rational.json";
function checked(path,sha){const b=readFileSync(path);if(createHash('sha256').update(b).digest('hex')!==sha)throw Error('actual complete input SHA differs: '+path);return JSON.parse(b.toString('utf8'));}
const q=checked(input,INPUT_SHA),tail=checked(high,HIGH_SHA);
const result=(function(q,tail,CANDIDATE,INPUT_SHA,HIGH_SHA){

const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;};
const R=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return [a/g,b/g];};
const add=(x,y)=>R(x[0]*y[1]+y[0]*x[1],x[1]*y[1]);
const mul=(x,y)=>R(x[0]*y[0],x[1]*y[1]);
const div=(x,y)=>R(x[0]*y[1],x[1]*y[0]);
const pow=(x,n)=>R(x[0]**BigInt(n),x[1]**BigInt(n));
const lt=(x,y)=>x[0]*y[1]<y[0]*x[1];
const str=x=>x[1]===1n?String(x[0]):x[0]+"/"+x[1];
const maxabs=z=>z.map(x=>x<0n?-x:x).reduce((a,b)=>a>b?a:b,0n);
const decimal=(x)=>{const z=String(x).split(".");return R(BigInt(z.join("")),z.length===1?1n:10n**BigInt(z[1].length));};
const gates=[];const gate=(name,value)=>{gates.push({name,passed:!!value});if(!value)throw Error(name);};
gate("actual_complete_current_waist", q.kind==="actual_final_complete_96_physical_waist_amplitude_Jacobi_row" && q.complete && q.executed && q.whole_original_eta && q.candidate_sha256===CANDIDATE);
gate("complete_96_columns_and_mean", q.rows.length===96 && q.rows.every((r,i)=>r.moving_index===i+1 && r.physical_frequency===4*(i+1)) && q.complete_odd_u_derivative_columns==="all exactly zero");
gate("upstream_executed_source_identity",q.producer_sha256==="dc8d3d4183cacc36e617620ca28e7e238564a80a3e53010a39577fe31632d4ae");
gate("actual_infinite_dual_tail",q.full_unknown_high_L2_dual_tail_reference.sha256==="19fc31617d033a4dcdc92153498592290da23ae58b545f3c5f64dc0ca343a3d9" && q.full_unknown_high_L2_dual_tail_reference.current_centre_upper==="1e-42");
gate("executed_actual_complete_high_tail", tail.kind==="actual_final_whole_waist_amplitude_high_tail_and_head_compensation" && tail.complete && tail.executed && tail.whole_original_eta && tail.candidate_sha256===CANDIDATE && tail.complete_high_indices==="|j|>=97" && tail.producer_sha256==="1c5c452613dea03487cb896c0574878954c49fdd3127797373257e610812bd96");
gate("actual_high_tail_below_1e_minus42",lt(decimal(tail.all_mode_actual_centre_amplitude_high_L2_dual_upper),R(1n,10n**42n)));
const D=BigInt(q.exact_interval_denominator);
gate("exact_interval_scale",D===(1n<<384n));
const intervals=[q.exact_mean_interval_numerator_at_scale,...q.rows.map(x=>x.exact_interval_numerator_at_scale)].map(x=>x.map(BigInt));
gate("ordered_exact_intervals",intervals.every(x=>x[0]<=x[1]));
const p=-intervals[1][1];gate("uniform_actual_amplitude_pivot",p>0n && p*100000n>61699n*D);
const abs=intervals.map(maxabs),A0=abs[0]*abs[0];
const S=A0+abs.slice(1).reduce((sum,a)=>sum+2n*a*a,0n);
const eps=R(1n,10n**42n);
const dual2=add(R(S,D*D),pow(eps,2));
gate("complete_actual_amplitude_dual_L2_lt_157_over_100",lt(dual2,pow(R(157,100),2)));
gate("cos4_amplitude_coefficient_inverse_lt_1621_over_1000",lt(R(D,p),R(1621,1000)));
const rL2=R(D*D,2n*p*p);
gate("mean_preserving_amplitude_lift_L2_lt_1147_over_1000",lt(rL2,pow(R(1147,1000),2)));
gate("mean_preserving_amplitude_lift_H1sixth_lt_3_over_2",lt(mul(R(17),pow(rL2,6)),pow(R(3,2),12)));
gate("mean_preserving_amplitude_lift_H1third_lt_37_over_20",lt(mul(R(17),pow(rL2,3)),pow(R(37,20),6)));
gate("mean_preserving_amplitude_lift_H1_lt_19_over_4",lt(mul(R(17),rL2),pow(R(19,4),2)));
const projection0=mul(rL2,dual2);
gate("complete_oblique_projection_L2_lt_9_over_5",lt(projection0,pow(R(9,5),2)));
const scales=[["H_one_sixth",R(401,250),R(43,20),6],["H_one_third",R(643,250),R(13,5),3],["H1",R(17),R(31,5),1]];
for(const [name,scale,bound,n] of scales){
 if(n>1)gate("rigorous_fractional_17_power_"+name,lt(R(17),pow(scale,n)));
 const numerator=add(add(mul(scale,R(A0)),R(S-A0)),mul(scale,mul(R(D*D),pow(eps,2))));
 gate("complete_oblique_projection_"+name+"_bound",lt(div(numerator,R(2n*p*p)),pow(bound,2)));
}
const rounding=R(1n,1n<<52n);
let proposal2=R(0);
for(let j=0;j<intervals.length;j++){
 const [lo,hi]=intervals[j];
 const radius=add(R(hi-lo,2n*D),rounding);
 proposal2=add(proposal2,mul(R(j===0?1:2),pow(radius,2)));
}
proposal2=add(proposal2,pow(eps,2));
gate("complete_physical_waist_proposal_fee_lt_6e_minus8",lt(proposal2,pow(R(6n,10n**8n),2)));
return {
 kind:"actual_final_complete_waist_Galerkin_left_projection_budget",
 complete:true,executed:true,arithmetic:"exact BigInt rational comparisons; no floating square or fractional roots",
 candidate_sha256:CANDIDATE,whole_original_eta:true,
 input_waist_row_sha256:INPUT_SHA,input_complete_high_tail_sha256:HIGH_SHA,
 complete_odd_u_columns_zero:true,mean_retained:true,all_96_cosine_columns_and_infinite_tail_retained:true,
 exact_pivot_abs_lower:str(R(p,D)),
 exact_complete_L2_dual_norm_squared_upper:str(dual2),
 exact_midpoint_plus_checked_binary64_proposal_error_squared_upper:str(proposal2),
 bounds:{
   amplitude_functional_L2:"157/100",
   mean_preserving_cos4_lift:{coefficient:"1621/1000",L2:"1147/1000",H_one_sixth:"3/2",H_one_third:"37/20",H1:"19/4"},
   complete_amplitude_kernel_projection:{L2:"9/5",H_one_sixth:"43/20",H_one_third:"13/5",H1:"31/5"},
   complete_actual_row_to_midpoint_and_checked_float_proposal:"3/50000000"
 },
 float_proposal_condition:"each exact midpoint must be converted as float(Fraction(...)); the producer explicitly checks abs(Fraction(float_value)-midpoint)<=2^-52",
 exact_row_proof_independent_of_float_proposal:true,
 finite_radial_QR_or_Python_execution_claimed:false,actual_nu_Schur_nonzero_proved:false,complete_BVP_inverse_proved:false,
 gate_count:gates.length,gates
};

})(q,tail,CANDIDATE,INPUT_SHA,HIGH_SHA);
result.producer_sha256=createHash('sha256').update(readFileSync(new URL(import.meta.url))).digest('hex');
console.log(JSON.stringify(result,null,2));
