#!/usr/bin/env node
"use strict";
/*
 * Exact reference Gauss6 operator constant and the variable-endpoint mean
 * primitive interface. No actual prefix field or NumPy table is loaded.
 */
const ENGINE_SHA="ac4a3e419e064c23a2eb42a1cb626507866d5e74e0ef608313fb887f8dbfcb80";
function buildMeanGauss(Q,hash){
 const Z=Q(0),O=Q(1);
 function requireTrue(ok,message){if(!ok)throw Error(message);}
 const min=(a,b)=>a.cmp(b)<0?a:b,max=(a,b)=>a.cmp(b)>0?a:b;
 function I(a,b=a){a=Q(a);b=Q(b);requireTrue(a.cmp(b)<=0,"reversed interval");return [a,b];}
 const add=(a,b)=>I(a[0].add(b[0]),a[1].add(b[1]));
 const sub=(a,b)=>I(a[0].sub(b[1]),a[1].sub(b[0]));
 const neg=a=>I(a[1].neg(),a[0].neg());
 function mul(a,b){const z=[a[0].mul(b[0]),a[0].mul(b[1]),a[1].mul(b[0]),a[1].mul(b[1])];return I(z.reduce(min),z.reduce(max));}
 function sq(a){const x=a[0].mul(a[0]),y=a[1].mul(a[1]);return I(a[0].cmp(Z)<=0&&a[1].cmp(Z)>=0?Z:min(x,y),max(x,y));}
 function inv(a){requireTrue(a[0].cmp(Z)>0||a[1].cmp(Z)<0,"zero in reciprocal");return I(O.div(a[1]),O.div(a[0]));}
 function pow(a,n){let z=I(O);for(let i=0;i<n;i++)z=mul(z,a);return z;}
 function packed(a,bits=128){
  const scale=1n<<BigInt(bits);
  function floor(q){const n=q.n*scale;return n>=0n?n/q.d:-((-n+q.d-1n)/q.d);}
  const lo=Q(floor(a[0])).div(Q(scale)),hi=Q(-floor(a[1].neg())).div(Q(scale));
  requireTrue(lo.cmp(a[0])<=0&&hi.cmp(a[1])>=0,"rounding was not outward");
  return {interval:[lo.toString(),hi.toString()],decimal_display:[Number(lo.n)/Number(lo.d),Number(hi.n)/Number(hi.d)],unpacked_exact_sha256:hash(a.map(String).join("\n")+"\n")};
 }
 const polynomial=[-5n,0n,105n,0n,-315n,0n,231n],scale=Q(16);
 const derivative=polynomial.slice(1).map((c,k)=>c*BigInt(k+1));
 const second=derivative.slice(1).map((c,k)=>c*BigInt(k+1));
 function at(p,x){let z=Q(p.at(-1));for(let k=p.length-2;k>=0;k--)z=z.mul(x).add(Q(p[k]));return z.div(scale);}
 function sign(p,x){return at(p,x).cmp(Z);}
 function run(){
  const checks={},detail=[];
  function check(name,ok,evidence){checks[name]=!!ok;requireTrue(ok,name);if(evidence!==undefined)detail.push({name,evidence});}
  check("exact_degree_six_and_normalization",polynomial.length===7&&at(polynomial,O).eq(O));
  check("exact_derivative_constants",at(derivative,O).eq(Q(21))&&at(second,O).eq(Q(210)));
  const orthogonal=[];
  for(let k=0;k<6;k++){
   let integral=Z;
   for(let j=0;j<polynomial.length;j++)if((j+k)%2===0)
    integral=integral.add(Q(polynomial[j]).mul(2).div(j+k+1).div(scale));
   orthogonal.push(integral.eq(Z));
  }
  check("six_exact_Legendre_orthogonality_integrals",orthogonal.every(Boolean));
  let norm=Z;
  for(let i=0;i<polynomial.length;i++)for(let j=0;j<polynomial.length;j++)if((i+j)%2===0)
   norm=norm.add(Q(polynomial[i]*polynomial[j]).mul(2).div(i+j+1).div(scale.mul(scale)));
  check("exact_Legendre_square_norm",norm.eq(Q("2/13")));
  const brackets=[["119/500","239/1000"],["661/1000","331/500"],["233/250","933/1000"]];
  const positive=[];
  for(const b of brackets){
   let lo=Q(b[0]),hi=Q(b[1]),sl=sign(polynomial,lo),sh=sign(polynomial,hi);
   requireTrue(sl*sh===-1,"initial rational sign bracket failed");
   for(let j=0;j<112;j++){
    const mid=lo.add(hi).div(2),sm=sign(polynomial,mid);
    requireTrue(sm!==0,"unexpected exact rational Legendre root");
    if(sm===sl){lo=mid;sl=sm;}else{hi=mid;sh=sm;}
   }
   requireTrue(sign(polynomial,lo)*sign(polynomial,hi)===-1,"final root signs failed");positive.push(I(lo,hi));
  }
  const roots=[...positive.slice().reverse().map(neg),...positive];
  check("six_disjoint_strict_sign_change_boxes",roots.length===6&&roots.every((r,i)=>
   r[0].cmp(-1)>0&&r[1].cmp(1)<0&&sign(polynomial,r[0])*sign(polynomial,r[1])===-1&&(!i||roots[i-1][1].cmp(r[0])<0)));
  check("exact_reflection_symmetry",roots.every((r,i)=>r[0].eq(roots[5-i][1].neg())&&r[1].eq(roots[5-i][0].neg())));
  const rows=roots.map((x,index)=>{
   const mid=x[0].add(x[1]).div(2),rad=x[1].sub(x[0]).div(2),dp=at(derivative,mid),epsilon=rad.mul(210);
   const dpi=I(dp.sub(epsilon),dp.add(epsilon));
   requireTrue(dpi[0].cmp(Z)>0||dpi[1].cmp(Z)<0,"uncertain derivative sign");
   const weight=inv(mul(sub(I(O),sq(x)),sq(dpi)));
   const u=I(x[0].add(1).div(2),x[1].add(1).div(2));
   return {index,x,u,weight,derivative:dpi};
  });
  check("all_six_positive_interior_nodes_and_weights",rows.every(r=>r.u[0].cmp(Z)>0&&r.u[1].cmp(O)<0&&r.weight[0].cmp(Z)>0));
  const moments=[];
  for(let k=0;k<=12;k++){
   let value=I(Z);for(const r of rows)value=add(value,mul(r.weight,pow(r.u,k)));
   const target=O.div(k+1),contains=value[0].cmp(target)<=0&&value[1].cmp(target)>=0;
   if(k<=11)requireTrue(contains,"certified Gauss moment misses its exact value");
   moments.push({degree:k,...packed(value),exact_integral:target.toString(),contains_exact_integral:contains});
  }
  check("all_twelve_degree_zero_through_eleven_moment_enclosures",moments.slice(0,12).every(x=>x.contains_exact_integral));
  let cumulative=I(Z),C=I(Z);const gaps=[];
  for(let i=0;i<=6;i++){
   const left=i?rows[i-1].u:I(Z),right=i<6?rows[i].u:I(O);
   if(i===6)cumulative=I(O); // exact Gauss normalization, not an approximate renormalization
   const A=sub(cumulative,left),B=sub(right,cumulative);
   requireTrue(A[0].cmp(Z)>=0&&B[0].cmp(Z)>=0,"cumulative weight outside adjacent-node gap");
   const term=mul(I("1/2"),add(sq(A),sq(B)));C=add(C,term);
   gaps.push({index:i,left_node:left.map(String),right_node:right.map(String),cumulative_weight:packed(cumulative),W1_contribution:packed(term)});
   if(i<6)cumulative=add(cumulative,rows[i].weight);
  }
  check("cumulative_weights_between_adjacent_nodes",gaps.length===7);
  check("sharp_C1_operator_constant_below_one_twentieth",C[1].cmp(Q("1/20"))<0,{C6:packed(C),safe_upper:"1/20"});
  check("constant_is_nonzero_and_above_47_over_1000",C[0].cmp(Q("47/1000"))>0);
  check("derivative_range_bound_coefficient_below_one_fortieth",C[1].div(2).cmp(Q("1/40"))<0);
  const leading=Q(924),monicNorm=O.div(leading.mul(leading).mul(13));
  const degree12=I(Q(moments[12].interval[0]),Q(moments[12].interval[1]));
  const error=sub(I("1/13"),degree12);
  check("degree12_error_encloses_exact_monic_legendre_norm",error[0].cmp(monicNorm)<=0&&error[1].cmp(monicNorm)>=0);
  check("degree12_error_strictly_positive",error[0].cmp(Z)>0);
  const jump=monicNorm.mul(13);
  check("variable_endpoint_join_counterexample_is_exact",monicNorm.eq(Q("1/11099088"))&&jump.eq(Q("1/853776")));
  check("all_computations_exact_rational",Object.values(checks).every(Boolean));
  return {
   schema:"strong-gauss6-mean-primitive-exact-v1",
   scope:"Exact reference rule and certified operator constants, not an actual prefix or a NumPy table certificate.",
   all_checks_passed:Object.values(checks).every(Boolean),check_count:Object.keys(checks).length,checks,detail,
   reference_rule:{polynomial_scale:"16",integer_coefficients_ascending:polynomial.map(String),positive_root_bisections:112,
    root_completeness:"Six disjoint sign-change boxes for degree six give one root each and no omissions.",
    derivative_bound:"21",second_derivative_bound:"210",
    derivative_bound_proof:"P'_6=sum_{k=1,3,5}(2k+1)P_k; differentiating gives a nonnegative Legendre expansion with sum 210, and |P_k|<=1 on [-1,1].",
    exact_degree:11,rows:rows.map(r=>({index:r.index,x:r.x.map(String),normalized_node:r.u.map(String),normalized_weight:packed(r.weight),P6_prime:packed(r.derivative)})),
    moments},
   C1_operator_constant:{definition:"C6=integral_0^1 |t-sum_{u_i<=t}w_i|dt",...packed(C),certified_simple_upper:"1/20",
    exact_gap_formula:"1/2 sum_{i=0}^6 ((S_i-u_i)^2+(u_{i+1}-S_i)^2); u_0=0,u_7=1,S_0=0,S_6=1",gaps},
   certified_mean_interface:{
    exact_C2_primitive:"H(s)=H(a)+integral_a^s m(t)dt for m continuously differentiable",
    single_interval_position_error:"|integral_a^b m - (b-a)sum_i w_i m(a+(b-a)u_i)| <= C6*(b-a)^2*osc_[a,b](m')/2",
    simple_position_error:"< (b-a)^2*osc_[a,b](m')/40 when the oscillation is positive; equality zero for affine m",
    variable_endpoint_first_derivative_error:"|d/ds [(s-a)sum_i w_i m(a+(s-a)u_i)]-m(s)| <= (s-a)*osc_[a,s](m')/2",
    internal_knot_first_jet_jump:"At b, the right derivative of the next partial primitive is m(b); absolute jump <= (b-a)*osc_[a,b](m')/2.",
    sum_rule:"Sum the position bounds over every completed original interval and the final partial interval; do not replace different old/fine quadrature meshes by a common difference rule without paying that change.",
    complete_mean:"m may be the exact continuous angular average or one specified finite equal-weight angular functional. They are different choices; their conversion and finite evaluation roundoff are separate inputs.",
    finite_rule_perturbation:"For h=b-a, max normalized node error eta, total absolute weight error omega, |m|<=M, |m'|<=L, sample errors epsilon_i: |h Q6(m)-h Qhat(mhat)| <= h*omega*M+h^2*eta*L+h*sum_i |what_i| epsilon_i. All actual normalized nodes must lie in [0,1]; endpoint mapping and cumulative-sum rounding remain separate."
   },
   exact_counterexample:{function:"m(s)=s^12, original intervals [0,1] and [1,2]",
    exact_integral_minus_Q6:"1/11099088",variable_endpoint_left_derivative_at_one:"1-1/853776",
    next_interval_right_derivative_at_one:"1",first_jet_jump:"1/853776",
    consequence:"The position produced by the exact reference Gauss algorithm need not even be C1 across original knots. Independently reported m,m' are not automatically its derivatives."},
   original_source_binding:{commit:"869436630c99aa5a68afb55bd8877c826034d117",
    path:"topics/large-amplitude-twist-flex/scripts/curve_stable_prefix_bvp.py",sha256:"e621ee2e9e8a706332b3839122a8ec57e1c5c2cfe82a48a759dcdad0548c54b2",function:"Prefix.height_integral",original_Gauss_order:6},
   physical_RHS_calls:0,tail_workers:0,newton_solves:0,actual_field_boxes_loaded:false,actual_NumPy_table_loaded:false,
   actual_evaluation_roundoff_paid:false,actual_accepted_prefix_C2_certificate:false,
   remaining:["Actual m' interval enclosures from the same fixed profile/chart/field and complete mean.",
    "Actual Gauss6 table, sample evaluations, endpoint mapping and accumulation errors.",
    "Any continuous-angular versus discrete-angular mean conversion.",
    "Nonmean PPoly and background knot consistency remain independent, as in R28 and the fixed-chart mean interface."]
  };
 }
 return {run};
}
if(typeof module!=="undefined")module.exports={buildMeanGauss};
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module){
 const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
 const a=process.argv.indexOf("--out");if(a<0||!process.argv[a+1])throw Error("--out required");
 const out=process.argv[a+1];if(fs.existsSync(out))throw Error("fresh --out required");
 const helper=path.join(__dirname,"strong_exact_rational_fast.js"),hash=x=>crypto.createHash("sha256").update(x).digest("hex");
 if(hash(fs.readFileSync(helper))!==ENGINE_SHA)throw Error("rational helper SHA differs");
 const {Q}=require(helper),result=buildMeanGauss(Q,hash).run();
 result.executed_source_sha256=hash(fs.readFileSync(__filename));result.rational_helper_sha256=ENGINE_SHA;
 fs.writeFileSync(out,JSON.stringify(result,null,2)+"\n",{flag:"wx"});
 process.stdout.write(JSON.stringify({all_checks_passed:result.all_checks_passed,checks:result.check_count,C6:result.C1_operator_constant.decimal_display})+"\n");
}
