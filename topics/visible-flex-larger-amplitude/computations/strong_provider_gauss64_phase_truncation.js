#!/usr/bin/env node
// Exact coefficient budgets for the analytic Gauss64 truncation lemma.
// No NumPy table, rounded transcendental evaluation, surface or BVP is tested.
function certificate(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
 const q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d===0n)throw Error('zero denominator');if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};};
 const add=(a,b)=>q(a.n*b.d+b.n*a.d,a.d*b.d);
 const mul=(a,b)=>q(a.n*b.n,a.d*b.d);
 const div=(a,b)=>q(a.n*b.d,a.d*b.n);
 const pw=(a,n)=>{let r=q(1);for(let j=0;j<n;j++)r=mul(r,a);return r;};
 const lt=(a,b)=>a.n*b.d<b.n*a.d;
 const rec=a=>({numerator:a.n.toString(),denominator:a.d.toString()});
 const rows=[];
 function check(name,a,b){const passed=lt(a,b);rows.push({name,left:rec(a),right:rec(b),passed});if(!passed)throw Error(name);}
 const C=div(q(16,5),q(919,1000)); // |Delta phi| < 16/5, eps < 81/1000
 check('all_turn_C_below_four',C,q(4));
 const phaseRamp=mul(mul(q(4),q(81,1000)),q(189,32));
 check('ramp_complex_phase_increment_below_two',phaseRamp,q(2));
 const eBound=q(87,32); // sum k=0..3 plus geometric upper tail from k=4
 check('e_power_four_below_64',pw(eBound,4),q(64));
 check('e_power_two_below_eight',pw(eBound,2),q(8));
 check('brake_complex_phase_increment_below_two',mul(q(9,1000),q(9,4)),q(2));
 const D1=q(54),D2=div(q(90),q(79,1000));
 check('phase_second_complex_bound_below_1200',D2,q(1200));
 const H1=mul(q(64),add(q(1),mul(q(3,2),D1)));
 const H2=mul(q(64),add(mul(q(3),D1),mul(q(9,4),add(q(1200),pw(D1,2)))));
 check('first_width_derivative_integrand_below_2pow13',H1,q(8192));
 check('second_width_derivative_integrand_below_2pow20',H2,q(1048576));
 const E0=q(1,1n<<118n),E1=q(1,1n<<113n);
 const E2=div(q(1,1n<<106n),q(27,10000));
 check('physical_second_primitive_error_below_2powminus97',E2,q(1,1n<<97n));
 return {scope:'Exact arithmetic for the analytic, exact-node/weight Gauss64 truncation lemma only.',
  passed:rows.every(r=>r.passed),guards:rows.length,rows,
  assumptions:{turn_ramp_epsilon:['79/1000','81/1000'],absolute_endpoint_angle:'<8/5',
    brake_phase_gap:'<9/1000',minimum_nonconstant_physical_segment_length:'>27/10000',
    total_nonconstant_phase_segment_length:'<4',Gaussian_nodes_weights_and_function_evaluation:'exact real arithmetic',
    fixed_segment_data:true,local_integral_split_at_both_turn_ramps:true},
  proven_bounds:{global_accumulated_radial_primitive_error_less_than:rec(E0),
    within_piece_physical_first_derivative_error_less_than:rec(E1),
    within_piece_physical_second_derivative_error_less_than:rec(q(1,1n<<97n))},
  not_certified:['actual NumPy leggauss64 table','rounded math/NumPy transcendental operations',
    'floating assembly of segment lengths, a0 and knots','seam repair to a single C2 profile',
    'initial Hermite background-height square-root quadrature','surface mean from the nonlinear PDE',
    'physical surface or metric error, convergence, embedding, reach or held amplitude'],
  arithmetic_only:true,physical_ODE_or_BVP_execution:false};
}
if(typeof process!=='undefined'&&process.argv?.[1]?.endsWith('strong_provider_gauss64_phase_truncation.js'))
 console.log(JSON.stringify(certificate(),null,2));
