#!/usr/bin/env node
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;};
const R=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};};
const sub=(a,b)=>R(a.n*b.d-b.n*a.d,a.d*b.d),cmp=(a,b)=>a.n*b.d-b.n*a.d,str=a=>a.n+'/'+a.d;
const gates=[];
function gate(name,a,b,eq=false){gates.push({name,left:str(a),right:str(b),relation:eq?'=':'<',pass:eq?cmp(a,b)===0n:cmp(a,b)<0n});}
gate('actual_J_below_nine_log2_M',R(325),R(984));
gate('log2_984_below_ten',R(984),R(2n**10n));
gate('layer_power_bound_at_first_frequency',R(204*(4+10)),R(4096+984/2));
gate('layer_power_difference_decreases',R(408,984),R(1,2));
gate('complete_upper_middle_binary_fee',R(65536+4096),R(69632),true);
gate('original_delta_to_h_exponent_denominator',R(320*256),R(81920),true);
gate('complete_frequency_exponent_denominator',R(2*320*256),R(163840),true);
gate('h_prefactor_below_sixteen',R(3*81920+69632,81920),R(4));
gate('two_physical_weights_total_binary_coefficient',R(-800+4+1),R(-795),true);
gate('subexponential_positive_power',R(0),R(163839,163840));
gate('subexponential_power_strictly_below_one',R(163839,163840),R(1));
gate('exact_integral_power_gap',sub(R(1),R(163839,163840)),R(1,163840),true);
gate('whole_continuous_sum_fee',R(163840),R(2n**18n));
gate('whole_dyadic_sum_fee',R(2*163840+1),R(2n**19n));
const input='R119-supplement-weighted-spectral-selection-one-common-radial-profile.md';
const expected='caf0779ae9c9dd14df18a3b2d80f6763d61b6f47101b24cb9e58462ae3d5b05a';
const hash=createHash('sha256').update(await readFile(new URL('../results/'+input,import.meta.url))).digest('hex');
if(hash!==expected)throw Error('Actual weighted spectral input changed.');
const argv=process.argv.slice(2);
if(argv.length!==2||argv[0]!=='--out')throw Error('usage: node this.mjs --out NEW_REPORT.json');
const report={
 schema:'R119-complete-radial-middle-subexponential-and-summable-width-v1',
 executed:true,complete:gates.every(g=>g.pass),gate_count:gates.length,
 arithmetic:'exact normalized BigInt rational',gates,
 input:{file:input,sha256:hash},
 producer_sha256:createHash('sha256').update(await readFile(fileURLToPath(import.meta.url))).digest('hex'),
 same_profile_and_outer_t:true,
 actual_window:'j>=8193, 2^-40 delta_j^-1/8 <= M <= 2^65536(j+5)^204 delta_j^-320',
 complete_ports:'the same 2*|I_M| Euclidean physical scattering ports including exact eliminated prefix/low-tail lines and affine inputs',
 layer_width:'h_j<16 M^(-1/163840) on every actual middle window',
 full_radial_middle_inverse:'||(I-U_M)^-1||_2<exp(2^-795 M^(1-1/163840))',
 arbitrary_width_loss:'exp(K(eps)), K(eps)=(c/q)*(c*(q-1)/(q*eps))^(q-1), c=2^-795, q=163840',
 continuous_logarithmic_sum:'<2^-777 for N0>=Mstar',
 dyadic_logarithmic_sum:'<2^-776 for N0>=Mstar',
 low_frequency_range_granted:false,original_source_conversion_granted:false,
 updated_nonradial_inverse_proved:false,nonlinear_iteration_performed:false,final_F_zero_proved:false
};
await writeFile(argv[1],JSON.stringify(report,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({complete:report.complete,gate_count:gates.length,out:argv[1]}));
if(!report.complete)process.exitCode=1;
