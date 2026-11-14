#!/usr/bin/env node
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a;};
const Q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};};
const add=(a,b)=>Q(a.n*b.d+b.n*a.d,a.d*b.d);
const neg=a=>Q(-a.n,a.d),sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>Q(a.n*b.n,a.d*b.d),div=(a,b)=>Q(a.n*b.d,a.d*b.n);
const pow=(a,n)=>Q(a.n**BigInt(n),a.d**BigInt(n)),str=a=>a.n+'/'+a.d;
const one=Q(1),two=Q(2),eps=Q(1,2n**11n),r=Q(1,2n**16n),gamma=Q(1,2n**9n);
const den=sub(one,mul(eps,add(one,gamma))),gates=[];
function gate(name,a,b,eq=false){
 const c=a.n*b.d-b.n*a.d;
 gates.push({name,left:str(a),right:str(b),relation:eq?'=':'<',pass:eq?c===0n:c<0n});
}
gate('whole_basis_product_below_two',pow(Q(17,16),2),two);
gate('relative_error_exponent',sub(Q(273),Q(124)),Q(149),true);
gate('first_low_relative_error_exponent',sub(Q(149),Q(320,2)),Q(-11),true);
gate('lambda_ratio_exponent_at_M4',add(Q(4),mul(two,add(Q(124),Q(8)))),Q(268),true);
gate('lambda_ratio_safety_margin',Q(16),Q(268));
gate('actual_sqrt_decay_below_three_quarters',one,mul(two,pow(Q(3,4),2)));
gate('entire_epsilon_sum',mul(Q(4),eps),Q(1,512),true);
gate('complete_disk_denominator_positive',Q(0),den);
gate('complete_Mobius_disk_invariance',div(add(eps,mul(add(r,eps),gamma)),den),gamma);
gate('full_determinant_Mobius_contraction',div(add(mul(add(one,eps),add(r,eps)),pow(eps,2)),pow(den,2)),Q(1,4));
gate('narrow_varying_cone_induction',div(add(one,mul(two,add(r,eps))),den),two);
gate('narrow_cone_inside_original_disk',mul(two,eps),gamma);
gate('complete_z_relative_bound',add(one,gamma),two);
gate('all_factor_error_sum',mul(two,Q(1,512)),Q(1,256),true);
const S=Q(1,256);
gate('finite_product_difference',div(S,sub(one,S)),Q(1,255),true);
gate('finite_product_lower',sub(one,S),Q(255,256),true);
gate('finite_product_upper',div(one,sub(one,S)),Q(256,255),true);
gate('inverse_product_difference',div(Q(1,255),Q(255,256)),Q(256,65025),true);
gate('unified_product_and_inverse_relative_error',Q(256,65025),Q(1,254));
gate('complete_physical_lower',mul(Q(16,17),Q(255,256)),Q(255,272),true);
gate('complete_physical_upper',mul(Q(17,16),Q(256,255)),Q(272,255),true);
gate('complete_physical_lower_above_half',Q(1,2),Q(255,272));
gate('complete_physical_upper_below_two',Q(272,255),two);
gate('original_deep_ratio_exact',div(Q(2n**131n),Q(2n**131n)),one,true);
gate('original_D_at_smallest_physical_mode_exceeds_one',one,Q(4**4,128));
gate('all_real_high_prefix_contracts',Q(1,4),one);
const inputs=[
 ['R119-supplement-controlled-profile-full-label-and-raw-ports.md','ff11cb043128a5d66ee996bb174edda0d6537fe73f9a7a565ba143d2ab5c04d0'],
 ['R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md','513202b38f1c346ef3fb3f43ff79e1c6bd4bccbd1ed8d9151a8a7095dc75bf98'],
 ['R119-supplement-original-neutral-label-common-analytic-normalization.md','5bc9d551c8e7b1329709d9513891d15536494d9f55163a2d5c40877877c09fc8']
];
const hash=b=>createHash('sha256').update(b).digest('hex'),dependencies=[];
for(const [file,expected] of inputs){
 const actual=hash(await readFile(new URL('../results/'+file,import.meta.url)));
 if(actual!==expected)throw Error('Dependency changed: '+file);
 dependencies.push({file,sha256:actual});
}
const args=process.argv.slice(2);
if(args.length!==2||args[0]!=='--out')throw Error('usage: node producer.mjs --out NEW.json');
const report={
 schema:'R119-original-label-complete-actual-low-tail-v1',executed:true,
 arithmetic:'exact normalized BigInt rational',complete:gates.every(g=>g.pass),
 gate_count:gates.length,gates,dependencies,
 producer_sha256:hash(await readFile(fileURLToPath(import.meta.url))),
 proof_sha256:hash(await readFile(new URL('../results/R119-supplement-original-label-complete-physical-low-tail.md',import.meta.url))),
 object:'actual radial zero-background Jacobi derivative for the complete original controlled profile box',
 range:'m in 4Z minus zero, abs(m)>=2^984*25^(1/8), all radial layers j>=128',
 original_label_and_C_zeta_retained:true,full_actual_high_prefix_retained:true,
 complete_infinite_low_tail_two_rows_retained:true,
 relative_first_row_error:'strictly below 1/254 relative to N_M a_m Lambda^(b_M-j)',
 physical_two_row_factors:['255/272','272/255'],
 all_layer_original_normalized_majorant:'(272/255)*abs(original label), with all true high prefix contractions',
 arbitrary_physical_source_Green_proved:false,nonzero_nonradial_inverse_proved:false,
 low_finite_frequency_range_proved:false,mean_or_independent_height_removed:false,
 final_F_zero_proved:false
};
await writeFile(args[1],JSON.stringify(report,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({complete:report.complete,gate_count:gates.length,out:args[1]}));
if(!report.complete)process.exitCode=1;
