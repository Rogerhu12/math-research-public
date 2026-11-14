/* R225: explicit rational 32-mode convex core, no numerical ODE/BVP.
   Pure JavaScript with native BigInt. No dependencies, filesystem or network.
   Run: node r225_rational_32_core.js > r225_rational_32_core.json
   In a V8 isolate: evaluate this source, then R225_generate().
   All proof comparisons use reduced BigInt fractions. Decimal strings are
   enclosing rational displays only. Timing is deliberately not in the data.
*/
(function (root) {
"use strict";
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;}
class Q {
  constructor(n,d=1n){
    n=BigInt(n);d=BigInt(d);
    if(d===0n)throw Error("zero denominator");
    if(d<0n){n=-n;d=-d;}
    const g=gcd(n,d);this.n=n/g;this.d=d/g;
  }
  add(b){const g=gcd(this.d,b.d);return new Q(this.n*(b.d/g)+b.n*(this.d/g),this.d*(b.d/g));}
  sub(b){return this.add(new Q(-b.n,b.d));}
  mul(b){const g=gcd(this.n,b.d),h=gcd(b.n,this.d);return new Q((this.n/g)*(b.n/h),(this.d/h)*(b.d/g));}
  div(b){if(b.n===0n)throw Error("division by zero");return this.mul(new Q(b.d,b.n));}
  neg(){return new Q(-this.n,this.d);}
  abs(){return this.n<0n?this.neg():this;}
  cmp(b){const z=this.n*b.d-b.n*this.d;return z<0n?-1:z>0n?1:0;}
  pow(k){if(!Number.isSafeInteger(k)||k<0)throw Error("bad integer power");let a=this,r=new Q(1n);while(k){if(k%2)r=r.mul(a);k=Math.floor(k/2);if(k)a=a.mul(a);}return r;}
  fraction(){return this.n.toString()+"/"+this.d.toString();}
}
function fixedInteger(v,digits){
  const sign=v<0n?"-":"";if(v<0n)v=-v;
  let s=v.toString().padStart(digits+1,"0");
  return sign+s.slice(0,-digits)+"."+s.slice(-digits);
}
function encode(q){
  const digits=24,scale=10n**BigInt(digits),num=q.n*scale;
  let lo=num/q.d;if(num<0n&&num%q.d!==0n)lo-=1n;
  const hi=num===lo*q.d?lo:lo+1n;
  if(new Q(lo,scale).cmp(q)>0||new Q(hi,scale).cmp(q)<0)throw Error("decimal enclosure");
  return {numerator:q.n.toString(),denominator:q.d.toString(),
    decimal_closed_interval:[fixedInteger(lo,digits),fixedInteger(hi,digits)]};
}
function generate(){
  const one=new Q(1n),two=new Q(2n),t=new Q(7n,13n);
  const A=new Q(8n,7n),epsilon=new Q(3n,10n),alpha=new Q(52n,35n);
  const modes=32,innerLast=64,N=33,checks=[];
  function gate(name,left,relation,right){
    const c=left.cmp(right);
    const ok=relation==="<"?c<0:relation===">"?c>0:relation==="<="?c<=0:relation===">="?c>=0:c===0;
    checks.push({name,relation,holds:ok});
    if(!ok)throw Error(name+": "+left.fraction()+" "+relation+" "+right.fraction());
  }
  gate("Laurent cosine normalization",two.mul(A).mul(new Q(13n,20n)),"=",alpha);
  const b=[one];
  for(let k=0;k<96;k++)b.push(b[k].mul(new Q(1n-2n*BigInt(k),2n*BigInt(k+1))));
  for(let k=1;k<b.length;k++)gate("binomial bound "+k,b[k].abs(),"<=",new Q(1n,2n*BigInt(k)));
  const powers=[one];for(let k=1;k<=162;k++)powers.push(powers[k-1].mul(t));
  const c=[];
  for(let n=1;n<=modes;n++){
    let sum=new Q(0n);
    for(let k=0;k<=innerLast;k++)sum=sum.add(b[k+n].mul(b[k]).mul(powers[n+2*k]));
    c.push(alpha.mul(sum));
  }
  const r=one.sub(t),r2=r.pow(2),r3=r.pow(3),r4=r.pow(4);
  const T0=alpha.mul(powers[N]).div(new Q(BigInt(N)).mul(r));
  const Trho=new Q(208n,35n).mul(powers[N]).mul(new Q(BigInt(N)).sub(new Q(BigInt(N-1)).mul(t))).div(r2);
  const sum3=powers[N].mul(
    new Q(BigInt(N)**3n).div(r)
      .add(new Q(3n*BigInt(N)**2n).mul(t).div(r2))
      .add(new Q(3n*BigInt(N)).mul(t).mul(one.add(t)).div(r3))
      .add(t.mul(one.add(new Q(4n).mul(t)).add(t.pow(2))).div(r4)));
  const TrhoDerivative=new Q(416n,35n).mul(sum3);
  const denominator=one.sub(t.pow(2));
  let E0=new Q(0n),Erho=new Q(0n),ErhoDerivative=new Q(0n),weightSum=0n;
  const innerErrorBounds=[];
  for(let n=1;n<=modes;n++){
    const j=BigInt(n),w=4n*j*j-1n;
    const e=alpha.mul(powers[n+130]).div(denominator);
    innerErrorBounds.push(e);
    E0=E0.add(e);Erho=Erho.add(new Q(w).mul(e));
    ErhoDerivative=ErhoDerivative.add(new Q(2n*j*j*w).mul(e));
    weightSum+=w;
  }
  const complete0=T0.add(E0),completeRho=Trho.add(Erho);
  const completeRhoDerivative=TrhoDerivative.add(ErhoDerivative);
  gate("integer power comparison",new Q(7n**12n*1600n),"<",new Q(13n**12n));
  gate("t33 rational upper bound",powers[33],"<",new Q(2197n,1404928000000n));
  gate("T0 closed form",T0,"=",new Q(338n,3465n).mul(powers[33]));
  gate("Trho closed form",Trho,"=",new Q(27716n,63n).mul(powers[33]));
  gate("finite curvature weights",new Q(weightSum),"=",new Q(45728n));
  gate("t131 coarse bound",powers[131],"<",new Q(1n,10n**32n));
  gate("kept coefficient C0 error",E0,"<",new Q(7n,10n**31n));
  gate("kept coefficient rho error",Erho,"<",new Q(1n,10n**27n));
  gate("complete C0 error",complete0,"<",new Q(2n,10n**10n));
  gate("complete rho error",completeRho,"<",new Q(1n,1000000n));
  gate("complete rho derivative factor error",completeRhoDerivative,"<",new Q(1n,500n));
  const supportDerivativeFloor=A.mul(one.sub(epsilon.pow(2))).div(two);
  const rhoDerivativeFloor=new Q(3n).mul(A).mul(epsilon.pow(2)).mul(one.sub(epsilon.pow(2))).div(two);
  gate("support derivative comparison constant",supportDerivativeFloor,"=",new Q(13n,25n));
  gate("rho derivative comparison constant",rhoDerivativeFloor,"=",new Q(351n,2500n));
  const supportMonotonicMargin=supportDerivativeFloor.sub(completeRho);
  const rhoMonotonicMargin=rhoDerivativeFloor.sub(completeRhoDerivative);
  gate("strict full-angle support monotonicity",supportMonotonicMargin,">",new Q(0n));
  gate("strict full-angle rho monotonicity",rhoMonotonicMargin,">",new Q(0n));
  let hMajor=one,hMinor=one,rhoMin=one,rhoMax=one,gap=new Q(0n);
  for(let n=1;n<=modes;n++){
    const j=BigInt(n),sign=new Q(n%2?-1n:1n),w=new Q(1n-4n*j*j);
    hMajor=hMajor.add(c[n-1]);hMinor=hMinor.add(sign.mul(c[n-1]));
    rhoMin=rhoMin.add(w.mul(c[n-1]));rhoMax=rhoMax.add(sign.mul(w).mul(c[n-1]));
    if(n%2)gap=gap.add(two.mul(c[n-1]));
  }
  const gapError=two.mul(complete0),diameter=two.mul(hMajor);
  const rhoEnvelopeLow=new Q(43n,175n).sub(completeRho);
  const rhoEnvelopeHigh=new Q(943n,231n).add(completeRho);
  gate("axis gap identity",gap,"=",hMajor.sub(hMinor));
  gate("positive support at minimum",hMinor,">",new Q(0n));
  gate("positive global rho minimum",rhoMin,">",new Q(0n));
  gate("strict rho lower envelope",rhoMin,">",rhoEnvelopeLow);
  gate("strict rho upper envelope",rhoMax,"<",rhoEnvelopeHigh);
  gate("whole axis gap error",gap.sub(new Q(4n,5n)).abs(),"<",gapError);
  gate("gap displayed strict error",gapError,"<",new Q(4n,10n**10n));
  gate("global core diameter envelope",diameter,"<",new Q(218n,77n).add(two.mul(complete0)));
  const k0=new Q(3n,10n),entryProduct=k0.mul(gap).mul(rhoMax);
  const radialCurvature=k0.mul(rhoMax),angularCurvature=one.div(rhoMin);
  const coreCurvatureMax=radialCurvature.cmp(angularCurvature)>0?radialCurvature:angularCurvature;
  gate("entry rho simple envelope",rhoMax,"<",new Q(4083n,1000n));
  gate("entry gap simple envelope",gap,"<",new Q(800001n,1000000n));
  gate("entry product exact",entryProduct,"<",new Q(49n,50n));
  gate("radial principal core curvature",radialCurvature,"<",new Q(41n,10n));
  gate("angular principal core curvature",angularCurvature,"<",new Q(41n,10n));
  const diameterBudget=new Q(5n).mul(gap);
  gate("core fits amplitude diameter budget",diameter,"<",diameterBudget);
  const result={
    schema:"r225-exact-rational-32-core-v1",
    method:"BigInt fractions; analytic Laurent tails; strict full-angle derivative-factor comparison",
    author:"strong_recovery (AI assisted)",
    scope:{
      complete_finite_core:true,
      numerical_ODE_Node_Jacobian_QR_BVP_calls:0,
      owned_terminal_scientific_run:false,
      finite_32_coefficients_are_all_prescribed_in_this_static_definition:true,
      current_35_parameter_BVP_only_fixes_three_low_core_modes:true,
      static_core_not_an_accepted_surface:true,
      closed_surface_existence:false,
      closed_Hausdorff_or_rigid_quotient_certificate:false,
      global_surface_reach_certificate:false
    },
    parameters:{modes,base_mode:2,inner_sum_last:innerLast,inner_terms_per_mode:65,
      total_exact_summands:2080,t:t.fraction(),ellipse_epsilon:epsilon.fraction(),
      A:A.fraction(),cosine_prefactor:alpha.fraction(),constant_support_coefficient:"1/1",
      comparison_core_constant:"1-A*mean(f); not numerically evaluated"},
    formula:{
      binomial:"b[0]=1; b[k+1]=((1/2-k)/(k+1))*b[k]",
      support:"h_hat(theta)=1+sum(n=1..32,c[n]*cos(2*n*theta))",
      coefficient:"c[n]=(52/35)*sum(k=0..64,b[k+n]*b[k]*(7/13)^(n+2*k))",
      material_angle:"theta+sum(n=1..32,(1-4*n^2)*c[n]*sin(2*n*theta)/(2*n))",
      material_angle_derivative:"rho_hat(theta)>0; exact increasing material chart",
      kept_coefficient_error:"eta[n]=(52/35)*t^(n+130)/(1-t^2)",
      omitted_rho_derivative_factor_bound:"(416/35)*sum(n=33..infinity,n^3*t^n)"
    },
    coefficients:c.map((v,i)=>({index:i+1,frequency:2*(i+1),value:encode(v)})),
    exact_bounds:{
      omitted_C0:T0,omitted_rho:Trho,omitted_rho_derivative_factor:TrhoDerivative,
      kept_coefficient_C0:E0,kept_coefficient_rho:Erho,
      kept_coefficient_rho_derivative_factor:ErhoDerivative,
      total_C0:complete0,total_rho:completeRho,
      total_rho_derivative_factor:completeRhoDerivative,
      axis_gap_error:gapError,
      support_monotonicity_margin:supportMonotonicMargin,
      rho_monotonicity_margin:rhoMonotonicMargin,
      rho_comparison_lower:rhoEnvelopeLow,rho_comparison_upper:rhoEnvelopeHigh
    },
    exact_extrema:{
      h_max_at_normal_angle_zero:hMajor,h_min_at_normal_angle_pi_over_2:hMinor,
      rho_min_at_normal_angle_zero:rhoMin,rho_max_at_normal_angle_pi_over_2:rhoMax,
      planar_curvature_max:angularCurvature,
      core_diameter:diameter,
      quarter_turn_boundary_Hausdorff:gap
    },
    exact_entry_budget:{
      k0_max:k0,R7_product_at_k0_max:entryProduct,
      R7_margin_to_one:one.sub(entryProduct),
      radial_principal_curvature_max:radialCurvature,
      angular_principal_curvature_max:angularCurvature,
      whole_core_principal_curvature_max:coreCurvatureMax,
      future_full_diameter_bound_for_one_fifth:diameterBudget,
      statement:"A future whole-surface witness needs D<=5*exact_G and full-surface ball exclusion; D<=4 and a rounded G are insufficient."
    },
    continuous_extrema_proof:{
      h_prime_factor:"-h_hat'/sin(2theta) >= 13/25-total_rho_error > 0",
      rho_prime_factor:"rho_hat'/sin(2theta) >= 351/2500-total_rho_derivative_factor_error > 0",
      domain:"all 0<theta<pi/2, then both axis symmetries",
      phase_distance:"exact support-difference supremum at the two axes; R1 boundary Hausdorff identity",
      entry_scope:"R7 only: exact metric and vertical inlet assumed; protects a sufficiently short inlet"
    },
    checks,all_checks:true,check_count:checks.length,
    no_floating_point_proof_comparisons:true
  };
  for(const section of ["exact_bounds","exact_extrema","exact_entry_budget"])
    for(const key of Object.keys(result[section]))
      if(result[section][key] instanceof Q)result[section][key]=encode(result[section][key]);
  return result;
}
root.R225_generate=generate;
if(typeof module!=="undefined"&&module.exports)module.exports={generate};
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module)
  process.stdout.write(JSON.stringify(generate(),null,2)+"\n");
})(globalThis);
