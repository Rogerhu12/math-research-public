#!/usr/bin/env node
"use strict";
/*
 * Exact rational guards for the intended analytic q096 finite neck and bridge.
 * This does not certify NumPy quadrature, floating source evaluation, a stored
 * physical PPoly, its knots, the actual surface curvatures, or its reach.
 *
 * Reconstructed after a transient environment loss. This r2 source is a fresh,
 * explicit recomputation, not a claim to reproduce the lost old source hash.
 * Run: node strong_q096_analytic_profile_bounds_r2.js --out result.json
 */
function certificate() {
  function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;}
  function q(n,d=1n){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};}
  const zero=q(0),one=q(1);
  function add(a,b){const g=gcd(a.d,b.d),ad=a.d/g,bd=b.d/g,n=a.n*bd+b.n*ad,h=gcd(n,g);return {n:n/h,d:ad*(b.d/h)};}
  function neg(a){return {n:-a.n,d:a.d};}
  function sub(a,b){return add(a,neg(b));}
  function mul(a,b){const g=gcd(a.n,b.d),h=gcd(b.n,a.d);return {n:(a.n/g)*(b.n/h),d:(a.d/h)*(b.d/g)};}
  function div(a,b){if(b.n===0n)throw Error("division by zero");return mul(a,q(b.d,b.n));}
  function sq(a){return mul(a,a);}
  function pw(a,k){let r=one;for(;k;k>>=1,a=sq(a))if(k&1)r=mul(r,a);return r;}
  function lt(a,b){return a.n*b.d<b.n*a.d;}
  function le(a,b){return a.n*b.d<=b.n*a.d;}
  function eq(a,b){return a.n*b.d===b.n*a.d;}
  function max(a,b){return lt(a,b)?b:a;}
  function binary(x){if(!Number.isFinite(x))throw Error("nonfinite input");const z=new DataView(new ArrayBuffer(8));z.setFloat64(0,x,false);const bits=z.getBigUint64(0,false),sign=(bits>>63n)?-1n:1n,e=Number((bits>>52n)&2047n),f=bits&((1n<<52n)-1n);if(e===0&&f===0n)return zero;const n=e?((1n<<52n)+f):f,k=e?e-1023-52:-1074;return k>=0?q(sign*n*(1n<<BigInt(k))):q(sign*n,1n<<BigInt(-k));}
  function dec(a,digits=16){const negative=a.n<0n,n=negative?-a.n:a.n,scale=10n**BigInt(digits),v=n*scale/a.d;const s=v.toString().padStart(digits+1,"0");return (negative?"-":"")+s.slice(0,-digits)+"."+s.slice(-digits);}
  function record(a){return {numerator:a.n.toString(),denominator:a.d.toString(),decimal_display:dec(a)};}
  function factorial(k){let z=1n;for(let j=2;j<=k;j++)z*=BigInt(j);return z;}
  function sinBox(x){let s=zero;for(let k=0;k<=15;k++){let t=div(pw(x,2*k+1),q(factorial(2*k+1)));s=add(s,k&1?neg(t):t);}const e=div(pw(x,33),q(factorial(33)));return [sub(s,e),add(s,e)];}
  function cosBox(x){let s=zero;for(let k=0;k<=15;k++){let t=div(pw(x,2*k),q(factorial(2*k)));s=add(s,k&1?neg(t):t);}const e=div(pw(x,32),q(factorial(32)));return [sub(s,e),add(s,e)];}
  function atanBox(x,terms){let s=zero;for(let k=0;k<terms;k++){let t=div(pw(x,2*k+1),q(2*k+1));s=add(s,k&1?neg(t):t);}const next=div(pw(x,2*terms+1),q(2*terms+1));return terms&1?[sub(s,next),s]:[s,add(s,next)];}
  const guards=[];
  function check(name,ok,evidence={}){guards.push({name,passed:!!ok,...evidence});if(!ok)throw Error("Failed exact guard: "+name);}
  const config={"direction":"outward","cycles":1,"ramp":0.4,"ramp_law":"hermite_boost_neck","delta":0.16208341673538396,"vu":0.31980000000000003,"vd":0.98,"start_acceleration":0.45,"boost_speed":0.8634500737670308,"boost_length":0.12481215570536809,"coast_outward":0,"loop_radius":0.35,"loop_ratio":1.1,"loop_speed":0.985,"loop_curvature":7.5,"descending_turn_curvature":6.7475,"descending_sync_curvature":2,"terminal_peak_fraction":0.1,"boost_law":"angle"};
  const port={"radius":0.30000000000000004,"backgroundSlope":0.08000000000000027,"backgroundSecond":-1.866666666666673,"E":1.0064,"Ep":-0.2986666666666687,"_prefix_bridge":{"kind":"finite_neck_terminal_v1","radius":0.35,"speed":0.985,"curvature":8,"peak_fraction":0.1}};
  const source_sha256={"alternative-neck-provider.py":"84ed048425c8b0f4deeec8af37828e318150cde5d59995da77f64d923591b9c2","alternative-neck-flatturn.py":"c0578ed401a2433c72ec99702c9c32a8412c66264a7fb81a8b8c74ba054fbbdd","alternative-neck-excursion.py":"f70571b8356e33cb89eabae2dba4e173e6612dac4d65d5df74f5ec14c34ad53c","strong_angle_boost.py":"ce2117cffe2e55d310eb0be219e7d22e750d97cd22704e75c3dd74a085c020be","root_dual_core_bvp.py":"85c057132c34694558360af857c9686b3ce7be7c31861ae6a3b6e6313184d652","alternative-neck-provider-smallcut30-port32-r2048.json":"7d3f77821453ccd81ca8eaba9634c899127455b76ec1b95ba27fb130503d4100"};
  const V=binary(config.vu),vp=binary(config.boost_speed),vd=binary(config.vd),vl=binary(config.loop_speed),delta=binary(config.delta),k0=binary(config.start_acceleration),LB=binary(config.boost_length),R=binary(config.loop_radius),ratio=binary(config.loop_ratio),K=binary(config.loop_curvature),Ks=binary(config.descending_turn_curvature),Ksync=binary(config.descending_sync_curvature),fraction=binary(config.terminal_peak_fraction),w=binary(port.backgroundSlope),wprime=binary(port.backgroundSecond),cutR=binary(port.radius),eps=binary(.08),om=sub(one,eps);
  check("frozen_profile_shape_and_angle_boost",config.direction==="outward"&&config.cycles===1&&config.ramp_law==="hermite_boost_neck"&&config.boost_law==="angle"&&config.coast_outward===0);
  check("positive_physical_domain",lt(zero,V)&&lt(V,vp)&&lt(vp,one)&&lt(zero,vd)&&lt(vd,vl)&&lt(vl,one)&&lt(zero,delta)&&lt(zero,LB)&&lt(zero,R)&&lt(one,ratio)&&lt(zero,k0));
  check("tagged_bridge_curvature_is_profile_loop_curvature",eq(K,q(15,2)),{original_untagged_port_curvature:port._prefix_bridge.curvature,actual_tagged_curvature:config.loop_curvature,source_fact:"root_dual_core_bvp calls neck.tagged_port(port,cfg), whose bridge curvature is cfg.loop_curvature"});
  check("cut_slope_and_brake_sign",lt(zero,w)&&lt(w,q(81,1000))&&lt(wprime,zero)&&lt(zero,fraction)&&lt(fraction,one)&&lt(q(12,100),cutR));
  const a=atanBox(q(1,5),24),b=atanBox(q(1,239),8);
  const pi=[sub(mul(q(16),a[0]),mul(q(4),b[1])),sub(mul(q(16),a[1]),mul(q(4),b[0]))];
  function tanDouble(t){return div(mul(q(2),t),sub(one,sq(t)));}
  const tan4=tanDouble(tanDouble(q(1,5))),tanMachin=div(sub(tan4,q(1,239)),add(one,div(tan4,q(239))));
  const machinAngleLo=sub(mul(q(4),a[0]),b[1]),machinAngleHi=sub(mul(q(4),a[1]),b[0]);
  check("Machin_exact_tangent_identity",eq(tan4,q(120,119))&&eq(tanMachin,one)&&lt(zero,machinAngleLo)&&lt(machinAngleHi,one),{meaning:"0<4 atan(1/5)-atan(1/239)<1<pi/2; the last inequality follows from atan(1)=integral_0^1 (1+x^2)^(-1) dx>1/2. Exact tangent 1 selects pi/4."});
  check("pi_and_Taylor_argument_domain",lt(q(314,100),pi[0])&&lt(pi[1],q(22,7))&&lt(q(14,10),div(pi[0],q(2))),{pi_lower:record(pi[0]),pi_upper:record(pi[1])});
  const Slo=q(4,5),Shi=q(9,10);
  function H(S){return sub(add(mul(k0,sq(S)),mul(q(6),mul(V,S))),mul(q(12),delta));}
  check("Hermite_length_unique_between_point8_and_point9",lt(H(Slo),zero)&&lt(zero,H(Shi)),{equation:"k0*S^2+6*V*S=12*delta",length_lower:record(Slo),length_upper:record(Shi)});
  check("Hermite_speed_monotone",le(mul(k0,Shi),mul(q(3),V)),{bernstein_derivative:"[k0,3V/S-k0,0]"});
  const hermiteAccel=max(k0,sub(div(mul(q(3),V),Slo),k0));
  check("Hermite_acceleration_below_one",lt(hermiteAccel,one),{upper:record(hermiteAccel)});
  check("angle_boost_lower_inlet_angle",lt(sinBox(q(32,100))[1],V));
  check("angle_boost_upper_outlet_angle",lt(vp,sinBox(q(105,100))[0]));
  const boostK=div(q(73,100),mul(LB,om));
  check("angle_boost_curvature_below_loop_bound",lt(boostK,K),{upper:record(boostK)});
  check("loop_angle_below_1point4",lt(vl,sinBox(q(14,10))[0]));
  check("loop_complement_below_point18",lt(cosBox(q(18,100))[1],vl));
  const firstL=div(pi[1],mul(Ks,om)),firstLower=sub(add(one,delta),firstL),firstUpper=add(add(add(one,delta),LB),firstL);
  check("first_turn_radius_upper_below_1point8",lt(firstUpper,q(18,10)),{upper:record(firstUpper)});
  check("first_turn_radius_lower_above_point12",lt(q(12,100),firstLower),{lower:record(firstLower)});
  check("asin_Lipschitz_six_on_sync_speeds",le(one,mul(q(36),sub(one,sq(vl)))),{meaning:"1/sqrt(1-v^2)<=6 for vd<=v<=vl"});
  const syncUpper=div(mul(q(6),sub(vl,vd)),mul(Ksync,om)),downMargin=sub(firstLower,add(R,syncUpper));
  check("descending_coast_strictly_nonnegative",lt(zero,downMargin),{radius_margin_lower:record(downMargin)});
  const loopUpper=div(pi[1],mul(K,om)),loopLower=sub(R,div(loopUpper,q(2))),loopHigh=add(mul(ratio,R),div(loopUpper,q(2)));
  check("loop_radius_minimum_above_point12",lt(q(12,100),loopLower),{lower:record(loopLower),meaning:"odd sine under u->1-u gives exactly zero net radial integral for each symmetric loop turn; maximum inward loss occurs in its first half"});
  check("loop_radius_maximum_below_1point8",lt(loopHigh,q(18,10)),{upper:record(loopHigh)});
  check("loop_positive_coasts",lt(R,mul(ratio,R)),{meaning:"the symmetric turns have zero ideal radial net increment"});
  const eta0=mul(sub(one,fraction),div(w,add(one,sq(w))));
  check("bridge_positive_angle_gap",lt(zero,eta0)&&lt(eta0,q(81,1000)),{lower:record(eta0),meaning:"atan(w)>=w/(1+w^2), eta=(1-fraction)*atan(w)"});
  const bridgeSpeed=cosBox(eta0)[1];
  check("bridge_speed_below_point998",lt(bridgeSpeed,q(998,1000)),{upper:record(bridgeSpeed),meaning:"|sin(peak)|=cos(eta)<=cos(eta0), not the loop speed .985"});
  const bridgeTurn=div(q(18,100),mul(K,om)),brakeUpper=div(mul(mul(q(2),fraction),mul(w,sq(add(one,sq(w))))),neg(wprime)),bridgeMargin=sub(sub(R,cutR),add(bridgeTurn,brakeUpper));
  check("bridge_coast_strictly_nonnegative",lt(zero,bridgeMargin),{radius_margin_lower:record(bridgeMargin)});
  check("brake_angular_rate_below_loop_bound",lt(neg(wprime),K),{upper:record(neg(wprime)),meaning:"ps=-wprime/(1+w^2)^(3/2), fixed cut wprime; |phi_s|<=ps"});
  check("all_remaining_nonbridge_speeds_below_point998",lt(vl,q(998,1000))&&lt(vp,q(998,1000))&&lt(vd,q(998,1000))&&lt(V,q(998,1000)));
  check("all_turn_acceleration_caps_below_7point5",le(K,q(15,2))&&le(Ks,K)&&le(Ksync,K)&&le(boostK,K)&&le(hermiteAccel,K));
  const minL=q(27,10000);
  const lengthLower={
    angle_boost:LB,
    first_turn:div(add(vp,vd),mul(Ks,om)),
    sync:div(sub(vl,vd),mul(Ksync,om)),
    each_loop_turn:div(mul(q(2),vl),mul(K,om)),
    bridge_turn:div(sub(sub(div(pi[0],q(2)),q(14,10)),w),mul(K,om)),
    brake:div(mul(mul(q(2),fraction),w),mul(add(one,sq(w)),neg(wprime)))
  };
  check("all_nonconstant_phase_segments_longer_than_point0027",Object.values(lengthLower).every(z=>lt(minL,z)),{lower_bounds:Object.fromEntries(Object.entries(lengthLower).map(([k,v])=>[k,record(v)]))});
  const phaseLength=add(add(add(add(add(LB,firstL),syncUpper),mul(q(2),loopUpper)),bridgeTurn),brakeUpper);
  check("total_nonconstant_phase_length_below_four",lt(phaseLength,q(4)),{upper:record(phaseLength)});
  const P1=div(pi[1],om),P2=div(mul(q(3),pi[1]),mul(q(2),mul(eps,om))),P3=div(mul(q(6),pi[1]),mul(sq(eps),om));
  check("all_phase_absolute_values_below_1point6",lt(div(pi[1],q(2)),q(16,10)));
  check("phase_normalized_first_derivative_below_four",lt(P1,q(4)),{upper:record(P1)});
  check("phase_normalized_second_derivative_below_65",lt(P2,q(65)),{upper:record(P2)});
  check("phase_normalized_third_derivative_below_3300",lt(P3,q(3300)),{upper:record(P3)});
  const totalGuards=guards.length;
  return {
    scope:"Exact intended analytic profile only: whole finite neck and tagged terminal bridge, not a proof of the NumPy Gauss realization or of a surface solution.",
    version:"reconstructed-r2-after-transient-loss",
    all_passed:guards.every(z=>z.passed),guard_count:totalGuards,guards,
    frozen_profile:config,original_port_cut:port,source_sha256,
    ideal_profile_global_bounds:{radius_lower:"3/25",radius_upper:"9/5",speed_absolute_upper:"499/500",acceleration_absolute_upper:"15/2",strict_for_radius_and_speed:true},
    phase_bounds:{absolute:"8/5",first_u:"4",second_u:"65",third_u:"3300",minimum_nonconstant_phase_segment_length:"27/10000",sum_nonconstant_phase_lengths_upper:"4",phase_pieces_have_degree_at_most_four:true},
    exact_inputs:Object.fromEntries(Object.entries({V,vp,vd,vl,delta,k0,LB,R,ratio,K,Ks,Ksync,fraction,w,wprime,cutR,eps}).map(([k,v])=>[k,record(v)])),
    no_numeric_BVP_or_Node_worker_run:true,
    remaining_obligations:["actual NumPy leggauss64 node and weight errors","floating trigonometric and arithmetic evaluation","segment lengths and accumulated endpoints including seam consistency","actual tensor field PPoly and complete independent mean","strict whole-domain mean root positivity","continuous actual surface curvature and reach"],
    prior_transient_result:{old_source_sha256:"5e67ba60e438a0a8bc4e0005c05c07a28801ee37fba3b7554233210acd01ac21",original_source_or_output_bytes_not_recovered:true,new_computation_not_old_hash_replay:true}
  };
}
if(typeof module!=="undefined")module.exports={certificate};
if(typeof require!=="undefined"&&require.main===module){const fs=require("fs"),crypto=require("crypto"),at=process.argv.indexOf("--out");if(at<0||!process.argv[at+1])throw Error("--out required");const result=certificate();result.executed_source_sha256=crypto.createHash("sha256").update(fs.readFileSync(__filename)).digest("hex");const data=JSON.stringify(result,null,2)+"\n";fs.writeFileSync(process.argv[at+1],data,{flag:"wx"});process.stdout.write(JSON.stringify({all_passed:result.all_passed,guard_count:result.guard_count,out:process.argv[at+1]})+"\n");}

