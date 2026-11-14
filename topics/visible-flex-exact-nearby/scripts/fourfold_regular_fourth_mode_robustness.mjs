import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';

function compute() {
  const gcd=(a,b)=>{while(b!==0n){const c=a%b;a=b;b=c;}return a<0n?-a:a;};
  const rat=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b===0n)throw Error('zero denominator');if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return [a/g,b/g];};
  const add=(a,b)=>rat(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const sub=(a,b)=>rat(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);
  const mul=(a,b)=>rat(a[0]*b[0],a[1]*b[1]);
  const div=(a,b)=>rat(a[0]*b[1],a[1]*b[0]);
  const lt=(a,b)=>a[0]*b[1]<b[0]*a[1];
  const R=(n,d=1n)=>rat(n,d);
  const scalar=(n,a)=>mul(R(n),a);
  const power10=n=>10n**BigInt(n);
  const rec=a=>({numerator:String(a[0]),denominator:String(a[1])});
  const zero=R(0),one=R(1);
  const epsilon=R(1,2n**512n);
  const Lmin=mul(R(7,5),sub(R(2n**24n),R(25,8)));
  const Z=R(2532986,power10(19));
  const previousTrueRobin=R(1256750,power10(21));
  const meanCandidate=R(6055,power10(46));
  const modelFee=R(915,power10(20));
  const qstarLow=R(99999999999936n,power10(14));
  const qstarHigh=R(99999999999937n,power10(14));
  const rZ=R(1,power10(12)),rB=R(1,2n**60n);
  const rf=scalar(10,add(rZ,rB));
  const F=add(rf,rB),H=scalar(6,F),F2=mul(F,F);
  const image=add(add(scalar(9,rZ),mul(epsilon,rB)),scalar(9n*4096n,F2));
  const lip=scalar(36n*4096n,F);
  const inverseDerivative=div(R(9),sub(one,lip));
  const fullQProposalFee=add(modelFee,epsilon);
  const longD=add(add(mul(epsilon,rZ),mul(epsilon,rB)),scalar(16384,F2));
  const longMean=scalar(2048,F2);
  const completeRobin=add(add(previousTrueRobin,mul(scalar(2,epsilon),Z)),longD);
  const completeMean=add(meanCandidate,longMean);
  const derivativeD=add(epsilon,scalar(4n*16384n,mul(F,inverseDerivative)));
  const derivativeMean=scalar(4n*2048n,mul(F,inverseDerivative));
  const gates={
    genuine_long_length_lower:lt(R(2n**24n),Lmin),
    all_mode_regular_fee_below_epsilon:lt(R(554),scalar(8,Lmin)),
    regular_plus_finite_long_fee_below_epsilon:lt(R(555),scalar(8,Lmin)),
    far_reflection_fee_below_epsilon:lt(R(513),scalar(6,Lmin)),
    actual_complete_Z_in_original_ball:lt(Z,R(1,power10(10))),
    actual_complete_Z_in_stated_smaller_ball:lt(Z,rZ),
    broadened_true_q_strictly_positive:lt(zero,sub(qstarLow,epsilon)),
    broadened_true_q_strictly_below_one:lt(add(qstarHigh,epsilon),one),
    broadened_nominal_q_error_below_1e17:lt(fullQProposalFee,R(1,power10(17))),
    complete_long_small_input_gate:lt(scalar(2,F),R(1,2n**25n)),
    complete_long_Y_gate:lt(H,R(1,2n**20n)),
    actual_C_inverse_strict_image:lt(image,rf),
    actual_C_inverse_strict_contraction:lt(lip,one),
    actual_C_inverse_derivative_below_ten:lt(inverseDerivative,R(10)),
    complete_nonlinear_long_d_below_1p638404e18:lt(longD,R(1638404,power10(24))),
    complete_nonlinear_Robin_below_1p258389e15:lt(completeRobin,R(1258389,power10(21))),
    complete_mean_C_below_2p048004e19:lt(completeMean,R(2048004,power10(25))),
    complete_d_derivative_below_6e6:lt(derivativeD,R(6,power10(6))),
    complete_mean_derivative_below_8e7:lt(derivativeMean,R(8,power10(7)))
  };
  if(!Object.values(gates).every(Boolean))throw Error('an exact rational robustness gate failed');
  return {
    kind:'exact_rational_true_regular_fourth_mode_robustness_budget',
    complete:true,arithmetic:'normalized BigInt rational operations and strict integer comparisons only',
    candidate_sha256:'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413',
    consumed_endpoint_proof:'results/R133-supplement-final-moving-centre-actual-regular-boundary.md',
    consumed_endpoint_proof_git_blob:'479d98118588ffc7b4edcec172df21b8aae7723b',
    consumed_executed_endpoint_source_sha256:'aa98cdd2289b13ac125a0bdb193faa9ae389b566d9a561c0b0e93208d29937f1',
    original_binary_native_hash_not_invented:true,
    assumptions:[
      'same actual a_R, omega, B, periodic long interval, and reflection class',
      'all physical m in 4N including m=4 satisfy |lambda_m+m*omega|<2^41*m*omega*exp(-2*m*L)',
      'actual complete endpoint C/B/previous true Robin bounds are those of the consumed proof',
      'independent far Dirichlet dot A2 norm <=2^-60; mean height remains independent'
    ],
    transcendental_comparisons_paid_symbolically:[
      'omega>7/5 implies L>(7/5)*(2^24-25/8)>2^24',
      'e>2 implies 2^42*exp(-8L)<2^(42-8L)<2^-512',
      '(2^42+8)*exp(-8L)<2^(43-8L)<2^-512',
      '2*exp(-6L)<2^(1-6L)<2^-512'
    ],
    exact_bounds:Object.fromEntries(Object.entries({
      Lmin,epsilon,actual_Z_A0_upper:Z,previous_complete_true_Robin_upper:previousTrueRobin,
      actual_mean_C_upper:meanCandidate,model_q_error_upper:modelFee,
      qstar_lower:qstarLow,qstar_upper:qstarHigh,rZ,rB,rf,F,H,
      C_inverse_image:image,C_inverse_image_margin:sub(rf,image),
      C_inverse_contraction:lip,C_inverse_derivative:inverseDerivative,
      full_q_proposal_error:fullQProposalFee,
      complete_true_regular_to_long_difference:epsilon,
      complete_nonlinear_long_d:longD,complete_nonlinear_long_mean:longMean,
      complete_true_Robin_residual:completeRobin,complete_C_mean_residual:completeMean,
      complete_d_derivative:derivativeD,complete_mean_derivative:derivativeMean
    }).map(([name,value])=>[name,rec(value)])),
    gates,number_of_strict_rational_gates:Object.keys(gates).length,
    fourth_regular_fee_not_assumed_zero:true,
    all_physical_modes_and_mean_retained:true,
    independent_far_Dirichlet_and_mean_height_retained:true,
    actual_far_regular_label_equation_solved:false,
    new_tail_profile_existence_claimed:false,
    full_body_inverse_or_nonlinear_solution_claimed:false
  };
}

const report=compute();
report.source_sha256=createHash('sha256').update(readFileSync(new URL(import.meta.url))).digest('hex');
console.log(JSON.stringify(report,null,2));
