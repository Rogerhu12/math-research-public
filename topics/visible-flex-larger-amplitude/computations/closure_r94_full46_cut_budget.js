#!/usr/bin/env node
"use strict";
/* Complete R92-domain DN transfer and conditional outer low/high response.
   Exact fractions only. The proved input bounds remain separately identified;
   this program performs no Arb, ODE, new quadrature or nonlinear PDE solve. */
function sha256(text){
 const bytes=[];for(const ch of text){const cp=ch.codePointAt(0);if(cp<128)bytes.push(cp);else if(cp<2048)bytes.push(192|(cp>>6),128|(cp&63));else if(cp<65536)bytes.push(224|(cp>>12),128|((cp>>6)&63),128|(cp&63));else bytes.push(240|(cp>>18),128|((cp>>12)&63),128|((cp>>6)&63),128|(cp&63));}
 const n=bytes.length, bit=BigInt(n)*8n;bytes.push(128);while(bytes.length%64!==56)bytes.push(0);for(let j=7;j>=0;j--)bytes.push(Number((bit>>BigInt(8*j))&255n));
 const K=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
 const H=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];const rr=(v,n)=>(v>>>n)|(v<<(32-n));const W=new Array(64);
 for(let q=0;q<bytes.length;q+=64){for(let j=0;j<16;j++)W[j]=((bytes[q+4*j]<<24)|(bytes[q+4*j+1]<<16)|(bytes[q+4*j+2]<<8)|bytes[q+4*j+3])>>>0;
 for(let j=16;j<64;j++){const x=W[j-15],y=W[j-2];W[j]=(W[j-16]+(rr(x,7)^rr(x,18)^(x>>>3))+W[j-7]+(rr(y,17)^rr(y,19)^(y>>>10)))>>>0;}
 let[a,b,c,d,e,f,g,h]=H;for(let j=0;j<64;j++){const t1=(h+(rr(e,6)^rr(e,11)^rr(e,25))+((e&f)^(~e&g))+K[j]+W[j])>>>0;const t2=((rr(a,2)^rr(a,13)^rr(a,22))+((a&b)^(a&c)^(b&c)))>>>0;h=g;g=f;f=e;e=(d+t1)>>>0;d=c;c=b;b=a;a=(t1+t2)>>>0;}
 const v=[a,b,c,d,e,f,g,h];for(let j=0;j<8;j++)H[j]=(H[j]+v[j])>>>0;}
 return H.map(v=>v.toString(16).padStart(8,"0")).join("");
}
function lossless(t){let out="",i=0,inString=false;while(i<t.length){const c=t[i];if(c==='"'){let j=i+1;for(;j<t.length;j++){if(t[j]==="\\"){j++;continue;}if(t[j]==='"'){j++;break;}}out+=t.slice(i,j);i=j;continue;}if(c==="-"||(c>="0"&&c<="9")){const m=t.slice(i).match(/^-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?/);if(!m)throw Error("number");out+='"'+m[0]+'"';i+=m[0].length;continue;}out+=c;i++;}return JSON.parse(out);}

function abs(a){return a<0n?-a:a;}
function gcd(a,b){a=abs(a);b=abs(b);while(b){const t=a%b;a=b;b=t;}return a;}
function rat(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return[a/g,b/g];}
function add(a,b){return rat(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);}
function sub(a,b){return rat(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);}
function mul(a,b){return rat(a[0]*b[0],a[1]*b[1]);}
function div(a,b){if(!b[0])throw Error("division by zero");return rat(a[0]*b[1],a[1]*b[0]);}
function cmp(a,b){const d=a[0]*b[1]-b[0]*a[1];return d<0n?-1:d>0n?1:0;}
function p2(e){e=BigInt(e);return e>=0n?rat(1n<<e):rat(1n,1n<<(-e));}
function p10(e){return 10n**BigInt(e);}
function decimal(s){s=String(s);const m=s.match(/^(-?)(\d+)(?:\.(\d*))?(?:[eE]([+-]?\d+))?$/);if(!m)throw Error("bad exact decimal");const tail=m[3]||"",n=BigInt(m[2]+tail)*(m[1]?-1n:1n),e=Number(m[4]||0)-tail.length;return e>=0?rat(n*p10(e)):rat(n,p10(-e));}
function dyad(v){v=v.upper||v;return mul(rat(v.mantissa),p2(v.binary_exponent));}
function frac(v){return rat(v.numerator,v.denominator);}
function sciUp(a,digits=19){if(a[0]<0n)throw Error("display only nonnegative");if(!a[0])return "0";let e=a[0].toString().length-a[1].toString().length;if(e>=0?a[0]<a[1]*p10(e):a[0]*p10(-e)<a[1])e--;const shift=digits-1-e;let n=a[0],d=a[1];if(shift>=0)n*=p10(shift);else d*=p10(-shift);let q=(n+d-1n)/d;let t=q.toString();if(t.length>digits){q=(q+9n)/10n;e++;t=q.toString();}t=t.padStart(digits,"0");return t[0]+"."+t.slice(1)+"e"+(e>=0?"+":"")+e;}
function rec(a){return{numerator:a[0].toString(),denominator:a[1].toString(),decimal_upward_display:sciUp(a)};}

const INPUTS=[
  {
    "key": "r59",
    "path": "notes/2026-11-12-closure-strong-parameter-domain-r1-summary.json",
    "git_blob": "20f071d10dfd7ccd9529f5d8a85781d83f1440de",
    "sha256": "4642dd6fa011d587f46e86671aa1a0c1df762b0502e33d8073020e5c128cc227"
  },
  {
    "key": "r78",
    "path": "notes/2026-11-12-root-r78-true-cut-cauchy-r1.json",
    "git_blob": "0d35efd94411457faf73c129d73af16eb7e003de",
    "sha256": "9e891098dd625f7418c48d91ee92db900bd7b0d1c44b2b69c1cdebbd8d03c930"
  },
  {
    "key": "r91",
    "path": "notes/2026-11-12-closure-r91-split-jump-high-exact-ledger.json",
    "git_blob": "ad94de7b118c251d0298e9d22d0d5161cc010c51",
    "sha256": "badc734ef590c747d62fc75bd57ce2571bd89e8c522604b691406f469d47392f"
  },
  {
    "key": "r92",
    "path": "notes/2026-11-12-root-r92-product-parameter-exact-ledger.json",
    "git_blob": "00eb0b20a97f82c0885b9e0f383f25fa67429469",
    "sha256": "9ef88cdeef25ed0dd688082e53b25b5f8aacda2bd67c9dada61c250cefa4052a"
  },
  {
    "key": "r93",
    "path": "notes/2026-11-12-closure-r93-positive-prefix-high-exact-ledger.json",
    "git_blob": "c8f939de37107739be41890b7007cdb1e62fb996",
    "sha256": "c55f52b53182ee6a9c5fe8f4a61ac209f785cd233b443c14e7109fea2b7a8277"
  }
];

function buildLedger(I){
 const R59=I.r59,R78=I.r78,R91=I.r91,R92=I.r92,R93=I.r93;
 const one=rat(1),zero=rat(0),S=rat(257,256),eta=rat(4096),lambda0=rat(3970,4096),lambda=rat(33159425,33554432);
 const K0=div(mul(eta,add(one,lambda0)),sub(one,lambda0)),Ksaved=dyad(R59.fixed_point_parameter_Lipschitz_in_W);
 const KT=div(mul(eta,add(one,lambda)),sub(one,lambda));
 const coeff59=decimal("2.532e-20"),epsilon=decimal("1.866468114819e-26"),epsilonNew=mul(S,epsilon);
 const coeffNew=mul(div(KT,K0),coeff59),D=mul(epsilonNew,coeffNew);
 const oldBeta=dyad(R78.complete_coarse_trace_rows.head.all46_low_nonlinear_K.uniform_value_upper);
 const oldImproved=decimal("1.169846811e-48"),newBeta=add(oldImproved,D);
 const baseMean=decimal("3.187952530e-30"),newMeanInput=add(baseMean,D),newMean=mul(rat(40),mul(newMeanInput,newMeanInput));
 const meanDelta=mul(rat(16),mul(newMeanInput,D));
 const oldHeight=dyad(R78.cuff_normalized_complete_mean_height.uniform_value_upper);
 const oldFar=dyad(R59.expanded_far_normalized_radius),WzUpper=div(oldFar,add(rat(64),p2(21)));
 const finiteHeightDelta=mul(oldHeight,div(add(eta,KT),rat(256))),farHeightDelta=mul(p2(-4973),mul(KT,WzUpper));
 const heightDelta=add(finiteHeightDelta,farHeightDelta),newHeight=add(oldHeight,heightDelta);
 const V0=p2(-40),headOperator=div(frac(R91.actual_low_true_head_wide),mul(V0,oldBeta));
 const newLocalHead=mul(headOperator,newBeta),newWideHead=mul(V0,newLocalHead);
 const localLinearUpper=decimal("7.027"),oldSourceCapUpper=rat(1,20000);
 const lowRadius=rat(9),newLocalImage=add(add(localLinearUpper,mul(rat(108),oldSourceCapUpper)),newLocalHead);
 const lowContraction=frac(R91.absolute_low_field_contraction);
 const newCentre=add(add(frac(R91.actual_low_linear_wide),frac(R91.actual_low_source_wide)),newWideHead);
 const bands=R78.complete_coarse_trace_rows.head.high_bands_value_upper;
 const oldRest=dyad(bands[1]),oldInfinite=dyad(bands[2]),oldAllHigh=dyad(R78.complete_coarse_trace_rows.head.complete_high_balanced_P_K.uniform_value_upper);
 const newAllHigh=add(oldAllHigh,D),newHighTrace=add(add(oldRest,oldInfinite),D),newHighLift=mul(rat(256),newHighTrace);
 const M=rat(5760),rM=p2(-43),rH=add(p2(-139),div(rM,rat(50))),q=frac(R93.full_mean_feedback),pureHigh=frac(R93.pure_high_field);
 const domain=add(add(newCentre,rM),mul(rat(18555),rH)),Astar=p2(-34);
 const highImage=add(add(newHighLift,pureHigh),mul(q,add(rM,rH)));
 const simpleImage=add(add(newHighLift,pureHigh),div(add(rM,rH),rat(60)));
 const selected=R78.selected_true_DN_minus_exact_linear_DN.map(row=>{
   const mode=String(row.mode);
   const previous=dyad(row.uniform_value_upper || row.value_uniform_upper || row.nonlinear_value_upper || row.value_upper);
   const value=add(previous,D);
   return {mode,original_narrow_value:rec(previous),expanded_value:rec(value),first_derivative:rec(mul(rat(4),value)),second_derivative:rec(mul(rat(64),value))};
 });
 const feedback=R78.actual_selected_boundary_feedback_rows.map(row=>{
   const sel=selected.find(x=>x.mode===String(row.mode));if(!sel)throw Error("selected mode missing");
   const op=div(dyad(row.transfer_from_Wsigma1_K_to_canonical_Q_upper),dyad(row.output_axis));
   const val=mul(op,frac(sel.expanded_value));
   return{node:String(row.endpoint_physical_node),mode:String(row.mode),normalized_value:rec(val),first_derivative:rec(mul(rat(4),val)),second_derivative:rec(mul(rat(64),val)),full_cut_selfmap_claimed:false};
 });
 const gates={
  all_original_R59_gates:R59.all_gates===true,
  all_original_R78_gates:R78.all_gates===true,
  all_original_R91_gates:R91.all_gates===true,
  all_original_R92_gates:R92.all_gates===true,
  all_original_R93_gates:R93.all_gates===true,
  exact_R59_lambda:cmp(dyad(R59.lambda_upper),lambda0)===0,
  original_saved_K_is_an_upper_bound:cmp(Ksaved,K0)>=0,
  new_K_is_the_R92_complete_lipschitz:cmp(KT,frac(R92.constants.transverse_unknown_lipschitz))===0,
  ratio_comparison_positive:cmp(KT,K0)>0,
  old_cut_coefficient_positive:cmp(coeff59,zero)>0,
  new_trace_difference_below_126e47:cmp(D,decimal("1.26e-45"))<0,
  full_new_beta_below_127e47:cmp(newBeta,decimal("1.27e-45"))<0,
  new_beta_smaller_than_R78_wide_bound:cmp(newBeta,oldBeta)<0,
  new_mean_input_below_one64:cmp(newMeanInput,rat(1,64))<0,
  expanded_R59_far_has_half_ball_margin:cmp(add(p2(-24),oldFar),rat(1,2))<0,
  positive_single_cuff_height_budget:cmp(heightDelta,zero)>0,
  real_both_selected_modes_retained:selected.length===2&&selected[0].mode==="2"&&selected[1].mode==="4",
  real_both_selected_nodes_retained:feedback.length===4,
  all_low_modes_retained:R91.low_mode_rows.length===46,
  low_local_head_positive:cmp(newLocalHead,zero)>0,
  new_low_absolute_selfmap:cmp(newLocalImage,lowRadius)<0,
  new_low_absolute_image_below_7033_over1000:cmp(newLocalImage,rat(7033,1000))<0,
  same_full_low_contraction:cmp(lowContraction,one)<0,
  new_low_constant_strip_below_Astar:cmp(newCentre,Astar)<0,
  same_high_threshold:String(R93.source_interval_minimum_high_mode)==="5760",
  same_rest_actual_input:cmp(oldRest,frac(R93.actual_head_rest_input))===0,
  same_infinite_actual_input:cmp(oldInfinite,frac(R93.actual_head_infinite_input))===0,
  new_balanced_high_lift_below_2minus141:cmp(newHighLift,p2(-141))<0,
  same_high_finite_source_order:String(R93.finite_centre_first_possible_high_term)==="61",
  same_middle_radius:cmp(rM,frac(R93.middle_radius))===0,
  complete_low_middle_high_domain:cmp(domain,Astar)<0,
  complete_high_feedback_below_one60:cmp(q,rat(1,60))<0,
  exact_expanded_high_ball_selfmap:cmp(highImage,rH)<0,
  simple_expanded_high_ball_selfmap:cmp(simpleImage,rH)<0,
  low_Q_P_nonlinear_difference_identically_zero:R78.complete_coarse_trace_rows.head.low_Q_and_P_nonlinear_remainder_identically_zero===true
 };
 const out={
  schema:"visible-larger-r94-full46-cut-and-conditional-exterior-v1",
  status:"Complete exact scalar transfer on R92 product parameter domain",
  author:"/root (GPT-6 Astra Pro, AI-assisted)",
  execution:{engine:"functions.exec V8 BigInt",new_Arb_ODE_source_integral_or_terminal_worker:false},
  all_gates:Object.values(gates).every(Boolean),gates,
  parameter_domain:"R74 original complex l-infinity twenty-box times R59 original transverse26 weighted l1 ball; product norm=max",
  theorem_defined_inputs:{R59_cut_coefficient_59_22:rec(coeff59),R61_cut_conversion_61_22:rec(epsilon),R83_whole_low_wide_value:rec(oldImproved),R83_complete_cut_nonmean_value:rec(baseMean),R90_linear_local_conservative:rec(localLinearUpper),R90_old_source_local_conservative:rec(oldSourceCapUpper)},
  lambda_original:rec(lambda0),lambda_new:rec(lambda),original_K_exact:rec(K0),original_K_saved_upper:rec(Ksaved),new_K:rec(KT),
  moving_centre_scale:rec(S),new_cut_conversion:rec(epsilonNew),new_strong_trace_coefficient:rec(coeffNew),
  transverse_complete_nonmean_cut_difference:rec(D),
  low_nonlinear_K_value:rec(newBeta),low_nonlinear_K_first:rec(mul(rat(4),newBeta)),low_nonlinear_K_second:rec(mul(rat(64),newBeta)),
  whole_high_balanced_value:rec(newAllHigh),whole_high_balanced_first:rec(mul(rat(4),newAllHigh)),whole_high_balanced_second:rec(mul(rat(64),newAllHigh)),
  complete_mean_input:rec(newMeanInput),complete_mean_value:rec(newMean),complete_mean_first:rec(mul(rat(4),newMean)),complete_mean_second:rec(mul(rat(64),newMean)),transverse_mean_difference:rec(meanDelta),
  original_single_cuff_height_value:rec(oldHeight),finite_transverse_height_difference:rec(finiteHeightDelta),far_transverse_height_difference:rec(farHeightDelta),single_cuff_height_value:rec(newHeight),single_cuff_height_first:rec(mul(rat(4),newHeight)),single_cuff_height_second:rec(mul(rat(64),newHeight)),
  selected_DN:selected,selected_boundary_feedback:feedback,
  original_wide_head_value:rec(oldBeta),same_head_operator_local:rec(headOperator),new_low_head_local:rec(newLocalHead),new_low_absolute_image:rec(newLocalImage),new_low_absolute_radius:rec(lowRadius),same_low_contraction:rec(lowContraction),
  same_linear_wide:R91.actual_low_linear_wide,same_source_wide:R91.actual_low_source_wide,new_head_wide:rec(newWideHead),new_low_centre_wide:rec(newCentre),
  high_threshold:5760,new_actual_high_trace:rec(newHighTrace),new_balanced_high_initial_lift:rec(newHighLift),same_high_source_inverse:R93.source_inverse,same_high_feedback:rec(q),same_pure_high_field:R93.pure_high_field,
  middle_radius:rec(rM),balanced_high_radius:rec(rH),complete_physical_domain:rec(domain),work_domain:rec(Astar),expanded_high_image:rec(highImage),simple_expanded_high_image:rec(simpleImage),strict_high_slack:rec(sub(rH,highImage)),
  scope:{R92_parameter_domain_paid:true,all46_true_inner_DN_and_single_cuff_mean:true,absolute_low_projection_equation:true,high_response_for_given_middle:true,middle_self_equation:false,low_high_backreaction:false,all46_cut_consistency:false,outer0_to9:false,closed_family_or_README_completion:false}
 };
 if(!out.all_gates)throw Error("R94 gate failure: "+Object.entries(gates).filter(x=>!x[1]).map(x=>x[0]).join(","));
 return out;
}

function runWithRaw(raw,engine){
 const input={};
 for(const spec of INPUTS){
  if(typeof raw[spec.key]!=="string")throw Error("missing raw input "+spec.key);
  if(sha256(raw[spec.key])!==spec.sha256)throw Error("input SHA256 mismatch "+spec.path);
  input[spec.key]=lossless(raw[spec.key]);
 }
 const ledger=buildLedger(input);
 ledger.execution.engine=engine;
 ledger.input_hashes=Object.fromEntries(INPUTS.map(x=>[x.path,x.sha256]));
 ledger.input_git_blobs=Object.fromEntries(INPUTS.map(x=>[x.path,x.git_blob]));
 ledger.input_sha256_checks=INPUTS.length;
 return ledger;
}
if(typeof require!=="undefined" && typeof module!=="undefined" && require.main===module){
 const fs=require("fs"),path=require("path");
 const topic=process.argv[2]||path.resolve(__dirname,"..");
 const output=process.argv[3];
 if(!output)throw Error("Usage: node closure_r94_full46_cut_budget.js TOPIC_ROOT OUTPUT_JSON");
 const raw=Object.fromEntries(INPUTS.map(x=>[x.key,fs.readFileSync(path.join(topic,x.path),"utf8")]));
 const started=Date.now(),ledger=runWithRaw(raw,"Node BigInt");
 ledger.source_sha256=sha256(fs.readFileSync(__filename,"utf8"));
 ledger.execution.elapsed_milliseconds=Date.now()-started;
 fs.writeFileSync(output,JSON.stringify(ledger,null,2)+"\n");
 process.stdout.write(JSON.stringify({all_gates:ledger.all_gates,gate_count:Object.keys(ledger.gates).length,input_sha256_checks:ledger.input_sha256_checks,output})+"\n");
}
