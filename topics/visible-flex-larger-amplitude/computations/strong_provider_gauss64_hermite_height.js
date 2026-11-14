#!/usr/bin/env node
// Exact analytic Gauss64 budgets for the frozen initial Hermite height.
// Actual NumPy nodes/weights/evaluations and the nonlinear surface mean are unpaid.
function certificate(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
 const q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(!d)throw Error('zero denominator');if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};};
 const add=(a,b)=>q(a.n*b.d+b.n*a.d,a.d*b.d),neg=a=>q(-a.n,a.d);
 const sub=(a,b)=>add(a,neg(b)),mul=(a,b)=>q(a.n*b.n,a.d*b.d),div=(a,b)=>q(a.n*b.d,a.d*b.n);
 const pw=(a,n)=>{let y=q(1);for(let i=0;i<n;i++)y=mul(y,a);return y;};
 const lt=(a,b)=>a.n*b.d<b.n*a.d,rec=a=>({numerator:a.n.toString(),denominator:a.d.toString()});
 const binary=x=>{const v=new DataView(new ArrayBuffer(8));v.setFloat64(0,x,false);const b=v.getBigUint64(0,false),sg=b>>63n?-1n:1n,e=Number((b>>52n)&2047n),f=b&((1n<<52n)-1n);if(e===2047)throw Error('nonfinite');const n=e?f+(1n<<52n):f,k=e?e-1023-52:-1074;return k>=0?q(sg*n*(1n<<BigInt(k))):q(sg*n,1n<<BigInt(-k));};
 const checks=[];function ck(name,a,b){const ok=lt(a,b);checks.push({name,passed:ok,left:rec(a),right:rec(b)});if(!ok)throw Error(name);}
 const V=binary(0.31980000000000003),k0=binary(0.45),Slo=q(4,5),Shi=q(9,10);
 const vlo=q(319,1000),vhi=q(321,1000),blo=q(359,1000),bhi=q(406,1000);
 ck('exact_binary_V_lower',vlo,V);ck('exact_binary_V_upper',V,vhi);
 ck('b_lower_from_proved_S',blo,mul(k0,Slo));ck('b_upper_from_proved_S',mul(k0,Shi),bhi);
 const A0=add(div(bhi,q(8)),div(vhi,q(2)));
 const A1=sub(mul(q(3,2),vhi),div(blo,q(4)));
 const A2=div(bhi,q(2)),A3=sub(mul(q(2),vhi),blo),R=q(7,8);
 ck('center_linear_coefficient_positive',q(0),sub(mul(q(3,2),vlo),div(bhi,q(4))));
 ck('center_cubic_coefficient_negative',bhi,mul(q(2),vlo));
 const Vcomplex=add(add(A0,mul(A1,R)),add(mul(A2,pw(R,2)),mul(A3,pw(R,3))));
 const V1=add(A1,add(mul(mul(q(2),A2),R),mul(mul(q(3),A3),pw(R,2))));
 const V2=add(mul(q(2),A2),mul(mul(q(6),A3),R));
 ck('complex_speed_below_point9',Vcomplex,q(9,10));
 ck('complex_speed_derivative_below_1point4',V1,q(7,5));
 ck('complex_speed_second_derivative_below_two',V2,q(2));
 ck('positive_branch_modulus_lower_squared',pw(q(2,5),2),sub(q(1),pw(q(9,10),2)));
 ck('positive_branch_modulus_upper_squared',add(q(1),pw(q(9,10),2)),pw(q(3,2),2));
 const F1=div(mul(q(9,10),q(7,5)),q(2,5));
 const F2=add(div(add(pw(q(7,5),2),mul(q(9,10),q(2))),q(2,5)),
                  div(mul(pw(q(9,10),2),pw(q(7,5),2)),pw(q(2,5),3)));
 ck('height_integrand_first_derivative_below_four',F1,q(4));
 ck('height_integrand_second_derivative_below_36',F2,q(36));
 ck('first_width_kernel_below_eight',add(q(3,2),mul(q(3,2),q(4))),q(8));
 ck('second_width_kernel_below_128',add(mul(q(3),q(4)),mul(q(9,4),q(36))),q(128));
 const decay=pw(q(4,7),128);
 ck('height_zeroth_physical_error_below_2powminus100',mul(q(7),decay),q(1,1n<<100n));
 ck('height_first_physical_error_below_2powminus98',mul(q(38),decay),q(1,1n<<98n));
 ck('height_second_physical_error_below_2powminus93',mul(q(747),decay),q(1,1n<<93n));
 return {scope:'Exact analytic Gauss64 truncation only for the frozen Hermite background-height primitive.',
  all_passed:checks.every(x=>x.passed),guard_count:checks.length,checks,
  frozen_binary_inputs:{vu:rec(V),k0:rec(k0)},
  imported_proved_assumption:'The unique initial Hermite length satisfies 4/5<S<9/10 (33-guard analytic-profile certificate).',
  complex_disc:{center:'1/2',radius:'7/8',branch:'analytic sqrt(1-v^2), positive at real u=0'},
  exact_Gauss_physical_bounds:{height:'2^-100',height_s:'2^-98',height_ss:'2^-93'},
  complete_background_combined_with_phase:{height:'2^-99',within_each_piece_height_s:'2^-98',within_each_piece_height_ss:'2^-93'},
  actual_NumPy_table_or_roundoff_paid:false,floating_segment_assembly_or_seams_paid:false,
  nonlinear_surface_mean_paid:false,physical_ODE_or_BVP_execution:false,arithmetic_only:true};
}
if(typeof process!=='undefined'&&process.argv?.[1]?.endsWith('strong_provider_gauss64_hermite_height.js'))
 console.log(JSON.stringify(certificate(),null,2));
