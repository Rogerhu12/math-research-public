#!/usr/bin/env node
/** Actual complete waist high-mode row, full mean and arbitrary unknown tails. */
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
function calculate(){
const input={"candidate_sha256":"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413","exact_alpha":"6890507429876859/9007199254740992","actual_target_radius_enclosure":["53436641/50000000","1068732841/1000000000"],"exact_full_V_coefficients":["1270129564654771/158456325028528675187087900672","2864496691872449/2251799813685248","1624098663981119/144115188075855872","-5192475905313877/1152921504606846976","3207928299402237/18446744073709551616","8478816635014769/147573952589676412928","-2368231246518113/1180591620717411303424","-241215380024263/295147905179352825856","-7488681247664523/302231454903657293676544","1680147733147791/302231454903657293676544","2508528725620295/9671406556917033397649408","-3887138776749025/77371252455336267181195264","-1066351861434367/309485009821345068724781056","8296177205370157/19807040628566084398385987584","5629761606212273/158456325028528675187087900672","-4861405037374475/633825300114114700748351602688","-6979762178234097/10141204801825835211973625643008","1843513710930941/20282409603651670423947251286016","5718599097241473/649037107316853453566312041152512","-40196755016835/324518553658426726783156020576256","-15433068265181/5192296858534827628530496329220096","1656983633614179/10384593717069655257060992658440192","-265068066504897/649037107316853453566312041152512","185919756031151/2596148429267413814265248164610048","7413412059233215/20769187434139310514121985316880384","-286349145547645/324518553658426726783156020576256","-8537671162694723/10384593717069655257060992658440192","-4276107853106963/10384593717069655257060992658440192","88795069357391/1298074214633706907132624082305024","-41329815694417/2596148429267413814265248164610048","-2699806148147159/1298074214633706907132624082305024","-147053166086193/162259276829213363391578010288128","53994010478195/1298074214633706907132624082305024"],"source_waist_report_sha256":"8066f501acc87d42e7d58f30377680aaa317be500471fa71bcceef336fc9357b"};
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
const q=(n,d=1n)=>{if(typeof n==='string'&&n.includes('/')){const z=n.split('/');n=z[0];d=z[1];}n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}if(!d)throw Error('zero denominator');const g=gcd(n,d);return {n:n/g,d:d/g};};
const add=(a,b)=>q(a.n*b.d+b.n*a.d,a.d*b.d),neg=a=>q(-a.n,a.d),sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>q(a.n*b.n,a.d*b.d),div=(a,b)=>q(a.n*b.d,a.d*b.n),pow=(a,n)=>q(a.n**BigInt(n),a.d**BigInt(n));
const abs=a=>a.n<0n?neg(a):a,lt=(a,b)=>a.n*b.d<b.n*a.d;
const scale=10n**90n;
const ceil=a=>{if(a.n<0n)throw Error('this directed ceiling requires a nonnegative input');return q((a.n*scale+a.d-1n)/a.d,scale);};
const floor=a=>{if(a.n<0n)throw Error('this directed floor requires a nonnegative input');return q((a.n*scale)/a.d,scale);};
const str=a=>a.n+'/'+a.d;
const decimal=(a,d=48)=>{if(a.n<0n)throw Error('nonnegative displayed upper required');const S=10n**BigInt(d),n=(a.n*S+a.d-1n)/a.d,t=n.toString().padStart(d+1,'0');return t.slice(0,-d)+'.'+t.slice(-d);};
const expRecords=[];
function expBounds(x,label){
 if(x.n<0n||!lt(x,q(100)))throw Error('certified positive exponential range');
 let lo=q(1),hi=q(1),tl=q(1),th=q(1);
 const tol=q(1,2n**260n);
 for(let n=1;n<=2000;n++){
  tl=floor(div(mul(tl,x),q(n)));th=ceil(div(mul(th,x),q(n)));
  lo=floor(add(lo,tl));hi=ceil(add(hi,th));
  const ratio=div(x,q(n+2));
  if(lt(ratio,q(1,2))){
   const first=ceil(div(mul(th,x),q(n+1)));
   const tail=ceil(div(first,sub(q(1),ratio)));
   if(lt(tail,tol)){
    const upper=ceil(add(hi,tail));
    expRecords.push({label,terms:n,argument:str(x),lower:str(lo),upper:str(upper),complete_tail_upper:str(tail)});
    return {lower:lo,upper};
   }
  }
 }
 throw Error('complete exponential tail did not close');
}
const alpha=q(input.exact_alpha),V=input.exact_full_V_coefficients.map(x=>q(x));
if(V.length!==33)throw Error('the actual whole 32-mode waist vector is required');
const al=q(input.actual_target_radius_enclosure[0]),au=q(input.actual_target_radius_enclosure[1]);
const minMean=sub(al,mul(alpha,V[0])),maxMean=sub(au,mul(alpha,V[0]));
const rho=q(1,1000000),gap=sub(minMean,rho),N=97;
const E=expBounds(q(1),'exp(4 sigma), sigma=1/4');
let ePow=q(1),P0=q(0),Psigma=q(0);
for(let j=1;j<=32;j++){
 ePow=ceil(mul(ePow,E.upper));
 const phase=div(mul(alpha,abs(V[j])),mul(q(4*j),minMean));
 P0=add(P0,phase);Psigma=add(Psigma,mul(phase,ePow));
}
const growth=expBounds(mul(q(4),Psigma),'whole finite analytic phase');
let decDen=q(1);
for(let j=0;j<N-1;j++)decDen=floor(mul(decDen,E.lower));
const analyticTail=ceil(div(growth.upper,decDen));
const centre=ceil(mul(div(q(2),mul(q(N),pow(minMean,2))),analyticTail));
const delta=div(rho,mul(q(4),gap));
const variationGrowth=expBounds(mul(q(4),add(P0,delta)),'complete arbitrary Wiener perturbation');
const sineDifference=ceil(mul(mul(q(4),delta),variationGrowth.upper));
const whole=ceil(mul(div(q(2),mul(q(N),pow(gap,2))),add(analyticTail,sineDifference)));
const compensation=ceil(mul(q(5,3),whole));
const meanKept=div(rho,gap);
const meanWaist=mul(mul(q(13,10),q(2693551,10n**19n)),q(271,250000000));
const meanCorrection=mul(q(5,3),meanWaist);
const gates=[];
function gate(name,x,bound){if(!lt(x,bound))throw Error(name+' failed: '+decimal(x));gates.push({name,passed:true,computed_upper:str(x),strict_upper:str(bound)});}
gate('entire original target interval positive mean',q(1),gap);
gate('complete finite phase Wiener norm below one quarter',P0,q(1,4));
gate('complete finite phase width-one-quarter bound',Psigma,q(13,20));
gate('actual centre full j>=97 amplitude dual tail',centre,q(1,10n**42n));
gate('unknown mean is included in actual phase difference',meanKept,q(1,1000000));
gate('complete arbitrary unknown tail phase difference',delta,q(1,4000000));
gate('full unknown Wiener ball high amplitude row',whole,q(45,1000000000n));
gate('true cos4 head correction for all high directions',compensation,q(75,1000000000n));
gate('current exact scalar mean high exterior to waist amplitude, Gamma retained',meanWaist,q(3796,10n**22n));
gate('current exact scalar mean high exterior to cos4 correction, Gamma retained',meanCorrection,q(6327,10n**22n));
return {
 kind:'actual_final_whole_waist_amplitude_high_tail_and_head_compensation',
 complete:true,executed:true,arithmetic:'BigInt exact rationals; every positive elementary step directed at 90 decimal places',
 candidate_sha256:input.candidate_sha256,whole_original_eta:true,
 actual_source_input:input,
 input_actual_finite_modes:32,complete_head_indices:'0<=|j|<=96',complete_high_indices:'|j|>=97',
 physical_frequency_factor:4,analytic_strip:'1/4',
 complete_infinite_unknown_Wiener_ball:{radius:'1/1000000',mean_retained:true,unknown_tail_not_assumed_analytic:true},
 actual_mean_abs_lower:str(minMean),actual_mean_abs_upper:str(maxMean),
 actual_mean_gap_after_unknown_ball:str(gap),
 full_real_phase_A0_upper:decimal(P0),full_finite_phase_A_quarter_upper:decimal(Psigma),
 all_mode_actual_centre_amplitude_high_L2_dual_upper:decimal(centre,70),
 all_mode_unknown_ball_amplitude_high_L2_dual_upper:decimal(whole),
 unknown_mean_and_tail_phase_difference_upper:decimal(delta),
 exact_cos4_amplitude_elimination_high_to_head_coefficient_upper:decimal(compensation),
 cosine_four_direction_inverse_upper:'5/3',
 current_centre_mean_eliminated_high_exterior_column:{waist_amplitude_upper:decimal(meanWaist),cos4_coefficient_correction_upper:decimal(meanCorrection),multiply_by_actual_full_radial_Gamma:true,Gamma_numerically_certified:false,updated_infinite_centre_body_band_not_claimed:true},
 interpretation:'Complete waist amplitude row and its high-to-head boundary correction only; body and exterior true rows remain separate.',
 all_mean_rows_preserved:true,gate_count:gates.length,gates,complete_exponential_bounds:expRecords,
 actual_nu_Schur_nonzero_proved:false,complete_body_BVP_inverse_proved:false
};}
const args=process.argv.slice(2);
if(args.length!==2||args[0]!=='--out')throw Error('usage: node this.mjs --out NEW_REPORT.json');
const report=calculate();
report.producer_sha256=createHash('sha256').update(await readFile(fileURLToPath(import.meta.url))).digest('hex');
await writeFile(args[1],JSON.stringify(report,null,2)+'\n',{flag:'wx'});
if(!report.complete)process.exitCode=1;
console.log(JSON.stringify({complete:report.complete,gate_count:report.gate_count,out:args[1]}));
