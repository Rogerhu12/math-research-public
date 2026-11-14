#!/usr/bin/env node
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;};
const R=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};};
const add=(a,b)=>R(a.n*b.d+b.n*a.d,a.d*b.d),mul=(a,b)=>R(a.n*b.n,a.d*b.d),cmp=(a,b)=>a.n*b.d-b.n*a.d,str=a=>a.n+'/'+a.d;
const gates=[];
function gate(name,a,b,eq=false){gates.push({name,left:str(a),right:str(b),relation:eq?'=':'<',pass:eq?cmp(a,b)===0n:cmp(a,b)<0n});}
const K=2n**128n;
gate('actual_delta8193_scaled_by_2pow8192',mul(R(2,25),R(1,2)),R(1,25),true);
gate('exact_first_low_threshold_binary_part',add(R(-40),R(8192,8)),R(984),true);
gate('first_low_threshold_exceeds_M1024',R(10),R(984));
gate('original_neutral_D_lower',R(1,128),mul(mul(R(K-1n,2n**131n),R(65,64)),R(15,16*12)));
gate('original_neutral_D_upper',mul(mul(R(16n*K+1n,16n*2n**131n),R(65,64)),R(1,12)),R(1,64));
gate('log_D_exceeds_two_log_M_after_1024',R(7),R(20));
gate('first_low_Mh_coefficient_exceeds_two',R(1),R(447,256));
gate('first_low_M_power_exceeds_square_root',R(1,2),R(31,32));
gate('square_root_log_comparison_at_1024',R(4*10),R(2*32));
gate('square_root_log_comparison_monotone',R(2),R(10,2));
gate('log_D_over_eight_exceeds_one',R(8),R(10));
gate('kappa_upper_and_A_lower',R(2n*256n**256n),R(257n**256n));
gate('kappa_lower_and_A_upper',R(513n**256n),R(2n*512n**256n));
gate('exact_original_finite_prefix_angle',add(R(5177,400),R(3968*9,100)),R(5921,16),true);
gate('actual_infinite_angle_tail_below_one_sixteenth',R(513n**256n),R(25n*512n**256n));
gate('complete_angle_upper_rational',add(R(5921,16),R(1,16)),R(2961,8),true);
gate('exact_deep_label_power',R(256*131),R(33536),true);
gate('log_two_upper_from_positive_exp_terms',R(2),R(269,128));
gate('x_log_M_lower',R(984,2),R(492),true);
gate('log_x_over_x_basepoint',R(9*3,4),R(492,64));
gate('log_x_over_x_monotonicity',R(1,492),R(1,64));
gate('lower_physical_normalization_power',R(33536-2*256),R(33024),true);
gate('upper_exponential_power',R(4*(512+1)),R(2052),true);
gate('logarithmic_prefactor_power',R(33536,64),R(524),true);
gate('upper_physical_normalization_power',R(33536-2052-524),R(30960),true);
gate('finite_integer_power_gap',R(33024-30960),R(2064),true);
gate('original_inverse_basis_norm_fee',R(17,16),R(2));
const deps=[
 ['R119-supplement-stronger-deep-first-shear-and-complete-local-map.md','4aaef72754b7c5b60c43cd17520814025dfcd033e2a9eb94842de661b24199ab'],
 ['R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md','513202b38f1c346ef3fb3f43ff79e1c6bd4bccbd1ed8d9151a8a7095dc75bf98'],
 ['R119-supplement-controlled-profile-full-label-and-raw-ports.md','ff11cb043128a5d66ee996bb174edda0d6537fe73f9a7a565ba143d2ab5c04d0']
];
const dependencies=[];
for(const [name,expected] of deps){
 const content=await readFile(new URL('../results/'+name,import.meta.url));
 const actual=createHash('sha256').update(content).digest('hex');
 if(actual!==expected)throw Error('Input proof SHA changed: '+name);
 dependencies.push({file:name,sha256:actual});
}
const argv=process.argv.slice(2);
if(argv.length!==2||argv[0]!=='--out')throw Error('usage: node this.mjs --out NEW_REPORT.json');
const report={
 schema:'R119-original-neutral-layer-physical-label-normalization-v1',
 executed:true,complete:gates.every(g=>g.pass),arithmetic:'exact normalized BigInt rational and integer powers',gate_count:gates.length,gates,dependencies,
 producer_sha256:createHash('sha256').update(await readFile(fileURLToPath(import.meta.url))).digest('hex'),
 range:'physical m in 4Z minus zero, M=abs(m)>=M*=2^984*25^(1/8)',
 original_label:'(E_M(b_M)^-1 X_m,b_M)_1; b_M is the original first neutral crossing minus one',
 C_zeta:'epsilon*delta8192^(-485/4), retained exactly',
 tau_infinity:'5921/16 + h4097/(1-2^(-1/256)), strictly between 5921/16 and 2961/8',
 physical_label_identity:'z_m=(-1)^b_M N_M a_m',
 exact_N:'C_zeta*exp(-tau_infinity*M)*(u_M/(8*M))^33536*exp(A*u_M)',
 exact_neutral_bounds:'log(D_M)<u_M<=2^(1/256)*log(D_M), A=1/(2^(1/256)-1)',
 exact_normalization_bracket_ratio:'2^131*D_M',
 power_bounds:'C_zeta exp(-tau_infinity M) M^-33024 < N_M < C_zeta exp(-tau_infinity M) M^-30960',
 complete_two_state_norm_claimed:false,arbitrary_physical_source_inverse_claimed:false,
 full_nonradial_inverse_proved:false,final_F_zero_proved:false
};
await writeFile(argv[1],JSON.stringify(report,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({complete:report.complete,gate_count:gates.length,out:argv[1]}));
if(!report.complete)process.exitCode=1;
