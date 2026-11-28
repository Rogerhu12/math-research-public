#!/usr/bin/env node
// Exact scalar application of existing R53/R54 to the n=3, b=1/2 design.
// No core quadrature, BVP, Jacobian, metric certificate or closed family is run.
function calculate() {
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;};
  const f=(p,q=1n)=>{p=BigInt(p);q=BigInt(q);if(q===0n)throw Error("zero denominator");if(q<0n){p=-p;q=-q;}const g=gcd(p,q);return {p:p/g,q:q/g};};
  const add=(a,b)=>f(a.p*b.q+b.p*a.q,a.q*b.q);
  const sub=(a,b)=>f(a.p*b.q-b.p*a.q,a.q*b.q);
  const mul=(a,b)=>f(a.p*b.p,a.q*b.q);
  const div=(a,b)=>f(a.p*b.q,a.q*b.p);
  const le=(a,b)=>a.p*b.q<=b.p*a.q;
  const show=a=>({numerator:String(a.p),denominator:String(a.q),display:Number(a.p)/Number(a.q)});
  // The 24 scalar physical support parameters printed by the already returned
  // q=.012 / lambda=.002 / M24 run. These are not nodal or physical field arrays.
  const coefficients=[
    .012,1.6865337340788748e-5,8.266205963269208e-6,1.6575311911171487e-6,
    -1.4801205272388585e-6,-6.872958557889615e-7,3.7065365897695084e-7,
    3.2096562378903867e-7,-9.430782018897675e-8,-1.5715728652822352e-7,
    1.4220901033592869e-8,7.699638157662246e-8,7.452783122660688e-9,
    -3.646561507736185e-8,-1.0459723554567974e-8,1.615736403426476e-8,
    8.10050107879746e-9,-6.432032929237208e-9,-5.006443779959792e-9,
    2.177833475070419e-9,2.4606285870533264e-9,-1.6242562325044267e-10,
    1.8573773834714286e-10,1.9339525413376448e-8];
  const view=new DataView(new ArrayBuffer(8));
  function exactBinary(value) {
    view.setFloat64(0,Math.abs(value),false);
    const bits=view.getBigUint64(0,false),E=Number((bits>>52n)&2047n);
    if(E===2047)throw Error("nonfinite coefficient");
    let p=bits&((1n<<52n)-1n),shift=-1074;
    if(E!==0){p|=1n<<52n;shift=E-1023-52;}
    return shift>=0?f(p<<BigInt(shift)):f(p,1n<<BigInt(-shift));
  }
  const actualA=coefficients.reduce((total,a,j)=>add(total,
    mul(f(9*(j+1)**2-1),exactBinary(a))),f(0));
  if(!le(actualA,f(1,10)))throw Error("The recorded anchor left its stated support box");
  const widths=[f(1,5),f(3,10),f(2,5),f(1,2)];
  const boxes=[f(1,10),f(2,3)];
  const table=[];
  for(const A of boxes)for(const b of widths){
    const K0=div(f(1),sub(f(1),A)),k=f(1,5);
    // T=2*pi/3>2, S=1/2, J=1+b. Hence J/(T-J)<(1+b)/(1-b).
    const ratio=div(add(f(1),b),sub(f(1),b));
    const betaUpper=mul(sub(K0,k),ratio);
    const KUpper=add(K0,betaUpper);
    if(!le(add(f(1,2),b),f(1)))throw Error("The stated pi>3 sector argument no longer applies");
    if(!le(KUpper,f(123,10)))throw Error("Declared scalar box exceeds the core curvature budget");
    table.push({A:show(A),transition:show(b),beta_upper_strict:show(betaUpper),
      all_lambda_curvature_lower:show(k),all_lambda_curvature_upper_strict:show(KUpper),
      strict_margin_below_12_point_3:show(sub(f(123,10),KUpper))});
  }
  return {
    status:"exact_scalar_parameter_budget_only",
    source_commit:"6da577d085d4b8a6e22e3523e10752ad6f4ae42a",
    material_core_git_blob:"1c3b5f164be8d4680b8bcbaf5cee9176c90bde3a",
    reused_results:["R53 equations (3),(4)","R54 sections 2-5","R55 wide design box","R67"],
    source_run_sha256:"21d676daa274a14d2fc64af746f42fcafdaa3f85b6d06201e464d7b2a359924a",
    source_raw_sha256:"3bc1c050dd28c8b8e87bd5733bea18e7be70becd8da461b1640abd655e5e785c",
    physical_scalar_count:coefficients.length,
    recorded_binary_support_weighted_A:show(actualA),
    strict_margin_to_one_tenth:show(sub(f(1,10),actualA)),
    target:{base_mode:3,halfwidth:show(f(1,2)),transition:show(f(1,2)),
      target_curvature:show(f(1,5)),curvature_blend:1},
    comparisons:table,
    W_first_derivative_bound_ratio_to_b_point2:show(f(2,5)),
    W_second_derivative_bound_ratio_to_b_point2:show(f(4,25)),
    kernel_is_degree9_C4_smoothstep:true,
    full_curvature_derivatives_do_not_scale_by_window_ratios_alone:true,
    R54_H_sweep_and_held_constants_changed:false,
    new_wide_transition_core_or_BVP_executed:false,
    original_input_exact_binary_scalars_only:true,
    future_Newton_controls_must_be_rechecked:true,
    completed_closed_surface:false
  };
}
console.log(JSON.stringify(calculate(),null,2));
