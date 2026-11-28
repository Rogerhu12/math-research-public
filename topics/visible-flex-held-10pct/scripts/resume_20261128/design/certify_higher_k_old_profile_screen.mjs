// Three higher-k planning budgets and old two-ramp profile exclusions.
// Exact BigInt comparisons. R57's k=.45 integral is cited, not recomputed.
function certificate() {
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;};
  const Q=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const d=gcd(a,b);return[a/d,b/d];};
  const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const sub=(a,b)=>Q(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);
  const mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]);
  const div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]);
  const square=a=>mul(a,a);
  const lt=(a,b)=>a[0]*b[1]<b[0]*a[1];
  const eq=(a,b)=>a[0]*b[1]===b[0]*a[1];
  const repr=a=>a[0]+"/"+a[1];
  const positive=(a,label)=>{if(a[0]<=0n)throw Error(label);return repr(a);};
  const sineLower=x=>sub(x,div(mul(square(x),x),Q(6)));
  const D=Q(67251,25000),rhi=Q(11,10),v0=Q(13,100),L0=Q(104,1425),L1=Q(128,2025);
  const cases=[
    {id:"k040",k:Q(2,5),S:Q(29,50),b:Q(9,20),alpha:Q(61,100),v:Q(7,25),t:Q(301,640),c0:Q(271,1000),c1:Q(123,500)},
    {id:"k045",k:Q(9,20),S:Q(31,50),b:Q(2,5),alpha:Q(69,100)},
    {id:"k050",k:Q(1,2),S:Q(27,40),b:Q(3,10),alpha:Q(4,5),v:Q(41,100),t:Q(137,160),c0:Q(53,250),c1:Q(113,250)}
  ];
  return {
    status:"exact_scalar_screen_completed",
    hypotheses:"Old R55 two-up-ramp profile, r in [21/20,11/10], exact metric, complete accurate circular Cauchy data, R5/R57 C3 classical uniqueness. No arbitrary C2 impossibility claimed.",
    full_BVP_or_interval_field_solver_run:false,
    sources:{read_commit:"6da577d085d4b8a6e22e3523e10752ad6f4ae42a",R55_git_blob:"4f5cd600faa9f7ba2b80aac7ccaa2af7301152d7",R57_git_blob:"3c7022188f2556af4a0099a87b61cd82d8d7eea1"},
    common_budget:{D_upper:repr(D),H_width:"27/50",each_sweep_margin:"1/200",weighted_support_radius_upper:"2/3",old_core_curvature_upper:"3/1",pi_lower:"333/106",pi_upper:"22/7",sqrt3_lower:"433/250"},
    rows:cases.map(c=>{
      const J=add(mul(Q(2),c.S),c.b);
      const core=add(Q(3),mul(sub(Q(3),c.k),div(J,sub(Q(111,53),J))));
      const held=mul(sub(div(Q(433,250),c.k),Q(44,21)),sineLower(div(mul(c.k,c.alpha),Q(2))));
      const H=mul(div(Q(2),c.k),sineLower(mul(c.k,Q(27,100))));
      if(!eq(mul(Q(2),c.S),add(add(Q(27,50),c.alpha),Q(1,100))))throw Error("sweep identity");
      const row={
        id:c.id,parameters:Object.fromEntries(["k","S","b","alpha"].map(key=>[key,repr(c[key])])),
        compensated_window_integral:repr(J),
        material_domain_margin_using_pi_lower:positive(sub(Q(111,106),add(c.S,c.b)),"material domain"),
        core_curvature_upper:repr(core),core_curvature_margin:positive(sub(Q(123,10),core),"core curvature"),
        held_lower:repr(held),held_absolute_margin:positive(sub(held,div(D,Q(10))),"held gate"),
        H_diameter_lower:repr(H),H_absolute_margin:positive(sub(H,div(D,Q(5))),"H gate"),
        planning_scalar_gates_passed:true,
        current_profile_classical_reach_excluded:true
      };
      if(c.id==="k045"){
        const K2=Q(64072265625n,226005494);
        row.obstruction={
          kind:"direct_application_of_registered_R57_not_new_integral_execution",
          second_ramp_t:"533/800",velocity:"173/500",
          registered_chi_upper:"49427/100000",
          protected_margin:positive(sub(c.S,Q(49427,100000)),"R57 protected margin"),
          curvature_squared_lower:repr(K2),
          curvature_squared_excess:positive(sub(K2,Q(2500,9)),"R57 necessary reach obstruction")
        };
      }else{
        const loss0sq=div(mul(mul(rhi,L0),v0),sub(square(c.k),square(v0)));
        const loss1sq=div(mul(mul(mul(rhi,L1),c.t),sub(c.v,v0)),sub(square(c.k),square(c.v)));
        const F=div(sub(c.t,Q(1,40)),Q(19,20));
        if(!eq(c.v,add(v0,mul(Q(8,25),F))))throw Error("plateau velocity");
        if(!lt(Q(1,20),c.t)||!lt(c.t,Q(19,20)))throw Error("not on the linear plateau");
        const K2=div(square(div(Q(405,76),rhi)),sub(square(c.k),square(c.v)));
        row.obstruction={
          kind:"new_exact_Cauchy_Schwarz_instance_of_R55_R57",
          second_ramp_t:repr(c.t),velocity:repr(c.v),root_margin:repr(sub(square(c.k),square(c.v))),
          chi0_squared_upper:repr(loss0sq),chi1_squared_upper:repr(loss1sq),
          chi0_upper:repr(c.c0),chi1_upper:repr(c.c1),
          chi0_bound_square_margin:positive(sub(square(c.c0),loss0sq),"first loss bound"),
          chi1_bound_square_margin:positive(sub(square(c.c1),loss1sq),"second loss bound"),
          protected_margin:positive(sub(c.S,add(c.c0,c.c1)),"remaining protected arc"),
          curvature_squared_lower:repr(K2),
          curvature_squared_excess:positive(sub(K2,Q(2500,9)),"necessary reach obstruction")
        };
      }
      return row;
    })
  };
}
console.log(JSON.stringify(certificate(),null,2));
