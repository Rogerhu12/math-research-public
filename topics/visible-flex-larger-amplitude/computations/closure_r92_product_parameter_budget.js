#!/usr/bin/env node
"use strict";
/* R92: exact positive-budget transfer from R59 and R74.
   This checks the new scalar arithmetic; it does not claim a new run of
   the 641 original rows, an Arb calculation or an exterior PDE solution. */
function abs(a){return a<0n?-a:a;}
function gcd(a,b){a=abs(a);b=abs(b);while(b){const t=a%b;a=b;b=t;}return a;}
function rat(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const d=gcd(a,b);return[a/d,b/d];}
function add(a,b){return rat(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);}
function sub(a,b){return rat(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);}
function mul(a,b){return rat(a[0]*b[0],a[1]*b[1]);}
function div(a,b){if(!b[0])throw Error("divide by zero");return rat(a[0]*b[1],a[1]*b[0]);}
function cmp(a,b){const d=a[0]*b[1]-b[0]*a[1];return d<0n?-1:d>0n?1:0;}
function p2(n){return n>=0?rat(1n<<BigInt(n)):rat(1n,1n<<BigInt(-n));}
function rec(a){return{numerator:a[0].toString(),denominator:a[1].toString(),display_only:Number(a[0])/Number(a[1])};}
function buildLedger(){
 const one=rat(1), zero=rat(0);
 const lambda0=rat(3970,4096), theta=rat(16705,16384), S=rat(257,256);
 const lambda=mul(theta,lambda0), old74=rat(256), s=p2(20), eta=p2(12);
 const newBox=add(old74,s), old59=add(rat(64),p2(21));
 const incrementImage=add(mul(s,lambda),mul(eta,add(one,lambda)));
 const slack=sub(s,incrementImage);
 const K=div(mul(eta,add(one,lambda)),sub(one,lambda));
 const rho=p2(-30), domain59=rat(147,1000000000000n);
 const mean59=rat(642,100000000000000000n), scaledMean=mul(S,mean59);
 const exponents=[-256,-257,-258,-263,-261,-263,-264,-268,-272,-270,-274,-273,-275,-277,-279,-281,-282,-286,-288,-290,-291,-292,-296,-297,-298,-300];
 const axes=exponents.map((e,i)=>({mode:42+2*i,canonical_exponent:e,guaranteed_height_exponent:e-18,axis:rec(p2(e))}));
 const gates={
  original_lambda_strict:cmp(lambda0,one)<0,
  theta_is_positive_majorant:cmp(theta,one)>0,
  complete_new_lambda_strict:cmp(lambda,one)<0,
  added_radius_positive:cmp(s,zero)>0,
  lift_budget_positive:cmp(eta,zero)>0,
  new_map_strict_slack:cmp(slack,zero)>0,
  new_radius_contains_R74:cmp(newBox,old74)>0,
  new_radius_smaller_than_R59_domain:cmp(newBox,old59)<0,
  R59_total_physical_domain_below_rho:cmp(domain59,rho)<0,
  R74_scaled_mean_domain_below_one_over_64:cmp(scaledMean,rat(1,64))<0,
  new_far_radius_smaller_than_R59:cmp(newBox,old59)<0,
  transverse_unknown_lipschitz_below_added_radius:cmp(K,s)<0,
  transverse_unknown_lipschitz_below_700000:cmp(K,rat(700000))<0,
  exactly26_nonzero_transverse_axes:axes.length===26&&axes.every(x=>cmp([BigInt(x.axis.numerator),BigInt(x.axis.denominator)],zero)>0),
  axes_cover_all_even42_through92:axes.every((x,i)=>x.mode===42+2*i)&&axes.at(-1).mode===92
 };
 if(!Object.values(gates).every(Boolean))throw Error("R92 scalar gate failed");
 return{
  schema:"visible-larger-r92-product-parameter-budget-v1",
  status:"Exact scalar arithmetic completed; complete 641-row transfer is the proof's positive-operator argument",
  proved_inputs:{
   R59:{path:"results/R59-actual-strong-full46-parameter-family.md",git_blob:"447344660f4d65835047d9e2503ccd93b2b71b7a",original_actual_job:20835,original_exit_code:0,
    domain_sha256:"30c7afb45e5b7886072ef5d9da1541e6bf825b78c6d13a9766834220e9798663",
    lifts_sha256:"94db6f6e89e623d27b7661ac8c432335063c1dd9f8303d3cdab93d6751c54497"},
   R74:{path:"results/R74-actual-anisotropic-moving-centre-family.md",git_blob:"06eb1adcd6ff056cc8d93a6f71cc1766c7a95abf",original_actual_job:6375,original_exit_code:0,
    primary_sha256:"4306f0641856e85a8390dee4c22271dbefe1c6c3c7934f9c9b9a1ec6195ad866"}
  },
  constants:{lambda_original:rec(lambda0),theta:rec(theta),moving_centre_scale:rec(S),lambda_majorant:rec(lambda),
   old_R74_radius_coefficient:rec(old74),additional_radius_coefficient:rec(s),new_radius_coefficient:rec(newBox),R59_certified_radius_coefficient:rec(old59),
   transverse_lift_budget:rec(eta),increment_image_coefficient:rec(incrementImage),strict_slack_coefficient:rec(slack),
   transverse_unknown_lipschitz:rec(K),R59_full_domain_upper:rec(domain59),rho:rec(rho),R74_mean_domain_upper:rec(scaledMean)},
  transverse_axes:axes,
  gates,all_gates:true,
  parameter_statement:"Original R74 twenty-coordinate complex product box times sum_{m=42,44,...,92}|d_m|/2^{e_m} <= 1.",
  norm_statement:"New V=S*old strong V; A_new=A_old/S<=A_old; far evaluation unchanged; original positive distance weights W retained.",
  excluded_claims:["No new 641-row integration or numerical replay","No revised R78 beta or external Green bounds are claimed on the larger parameter domain","No exterior cut consistency for all46","No closed surface or completion claim"]
 };
}
if(typeof module!=="undefined"&&module.exports)module.exports={buildLedger};
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module){
 const fs=require("node:fs"),path=require("node:path");
 if(process.argv.length!==3)throw Error("Usage: node closure_r92_product_parameter_budget.js OUT.json");
 const target=process.argv[2];
 if(fs.existsSync(target))throw Error("Use a fresh output path");
 const out=JSON.stringify(buildLedger(),null,2)+"\n";
 fs.mkdirSync(path.dirname(target),{recursive:true});
 fs.writeFileSync(target,out,{flag:"wx"});
 process.stdout.write(JSON.stringify({all_gates:true,gates:15,output:target})+"\n");
}
