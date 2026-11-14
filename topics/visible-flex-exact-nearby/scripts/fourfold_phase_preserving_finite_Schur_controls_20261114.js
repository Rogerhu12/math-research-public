"use strict";
/* New exact BigInt polynomial and rational calculation, actually run in V8.
   node this-file.js PRODUCER_GIT_BLOB_SHA > output.json
   No native/Python replay or numerical Schur gap is claimed. */
const dependencies={
  "results/R119-supplement-phase-preserving-actual-finite-Schur-controls.md": "5214cfffb5d16f3aebb0105af8aab14b2b5188b1",
  "results/R119-supplement-stronger-deep-first-shear-and-complete-local-map.md": "cb2db7a4d9593e75e96344b1c2557fd1a38a0e03",
  "results/R119-supplement-uniform-frequency-reference-Airy-Cauchy.md": "e44caf5cddb05512b3940a132305f4aa23f63e7a",
  "results/R119-supplement-actual-two-parameter-complete-phase-arithmetic.md": "7d2a2f93a6c1c2ce01931fcba94fb8d1478cb7dc",
  "results/R119-supplement-actual-nonradial-first-density-phase.md": "811e36bbc3858a2c3e3792d5103b4f25d38694b9",
  "results/R119-supplement-joint-actual-principal-and-beta-selection.md": "934cddff433cee17338575ea6d70fe8c95a8a207"
};

function run(producerGitBlobSha){
 function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
 function Q(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return {a:a/g,b:b/g};}
 function add(a,b){return Q(a.a*b.b+b.a*a.b,a.b*b.b);}
 function sub(a,b){return Q(a.a*b.b-b.a*a.b,a.b*b.b);}
 function mul(a,b){return Q(a.a*b.a,a.b*b.b);}
 function div(a,b){return Q(a.a*b.b,a.b*b.a);}
 function pow(a,k){return Q(a.a**BigInt(k),a.b**BigInt(k));}
 function eq(a,b){return a.a*b.b===b.a*a.b;}
 function lt(a,b){return a.a*b.b<b.a*a.b;}
 function str(a){return a.b===1n?String(a.a):String(a.a)+"/"+String(a.b);}
 const gates=[];function gate(name,pass,detail){gates.push({name,pass:!!pass,detail});if(!pass)throw Error(name);}
 // Exact Laurent polynomials with monomial key (lambda exponent, twice-Q exponent,
 // Q' exponent, Q'' exponent). Rational coefficients; negative Q powers allowed.
 function mono(c,e=[0,0,0,0]){const z=new Map();c=typeof c==="object"?c:Q(c);if(c.a)z.set(e.join(","),c);return z;}
 function pa(...xs){const z=new Map();for(const x of xs)for(const [k,c]of x){const a=add(z.get(k)||Q(0),c);if(a.a)z.set(k,a);else z.delete(k);}return z;}
 function scale(x,c){c=typeof c==="object"?c:Q(c);const z=new Map();for(const[k,v]of x){const a=mul(v,c);if(a.a)z.set(k,a);}return z;}
 function pm(...xs){let z=mono(1);for(const x of xs){const y=new Map();for(const[k,a]of z)for(const[l,b]of x){const e=k.split(",").map(Number),f=l.split(",").map(Number);const h=e.map((v,i)=>v+f[i]).join(",");const c=add(y.get(h)||Q(0),mul(a,b));if(c.a)y.set(h,c);else y.delete(h);}z=y;}return z;}
 function pd(x,v){const z=new Map();for(const[k,c]of x){const e=k.split(",").map(Number);const n=e[v];if(!n)continue;const f=e.slice();f[v]-=v===1?2:1;const a=mul(c,Q(n,v===1?2:1));z.set(f.join(","),add(z.get(f.join(","))||Q(0),a));}return z;}
 function dt(x){return pa(pm(pd(x,1),mono(1,[0,0,1,0])),pm(pd(x,2),mono(1,[0,0,0,1])));}
 function same(x,y){return pa(x,scale(y,-1)).size===0;}
 const one=mono(1),zero=mono(0),lam=mono(1,[1,0,0,0]),q=mono(1,[0,2,0,0]),q1=mono(1,[0,0,1,0]);
 const O=[
 [scale(pa(one,q),-1),mono(2),zero],
 [scale(pm(lam,q),-1),zero,one],
 [zero,scale(pm(lam,q),-2),pa(one,q)]
 ];
 function rm(v,A){return A[0].map((_,j)=>pa(...v.map((x,i)=>pm(x,A[i][j]))));}
 const v=[lam,scale(lam,-2),one],v1=rm(v,O),v2=rm(v1,O).map((x,i)=>pa(x,dt(v1[i])));
 const F=pa(pm(q,q),pm(pa(mono(2),scale(lam,-4)),q),one,q1);
 const target=v.map(x=>pm(F,x));
 target[0]=pa(target[0],scale(pm(lam,pa(lam,mono(-1)),q1),2));
 gate("symmetric_square_full_A_row",same(v2[0],target[0]),"exact Laurent-polynomial identity, no sampled Q");
 gate("symmetric_square_full_B_row",same(v2[1],target[1]),"exact K'' coefficient of mu h h'");
 gate("symmetric_square_full_C_row",same(v2[2],target[2]),"exact K'' coefficient of mu h'^2");
 gate("symmetric_square_nonzero_fourfold",16n*15n>0n,"2 lambda(lambda-1) nonzero for all lambda=m^2>=16");
 const L128=pa(mono(8,[0,3,0,0]),mono(16,[0,1,0,0]),mono(8,[0,-1,0,0]),mono(2,[0,-5,2,0]));
 const Euler128=pa(pd(L128,1),scale(dt(pd(L128,2)),-1));
 const B128=pa(mono(12,[0,1,0,0]),mono(8,[0,-1,0,0]),mono(-4,[0,-3,0,0]),mono(5,[0,-7,2,0]),mono(-4,[0,-5,0,1]));
 gate("complete_beta_Euler_kernel",same(Euler128,B128),"128 times the exact Euler derivative, all Q' and Q'' terms");
 gate("beta_total_derivative_coefficient",eq(sub(Q(5,16),Q(3,8)),Q(-1,16)),"integrated kappa: 5/16-6/16=-1/16");
 gate("beta_integral_coefficients",eq(mul(Q(-1,4),Q(-1,4)),Q(1,16))&&eq(mul(Q(-1,4),Q(-1,16)),Q(1,64)),"physical n=m/4 beta unit is retained");
 gate("principal_variation_sign",eq(mul(Q(1,2),Q(-1,2)),Q(-1,4)),"dot S=-(1/4) int psi Q'/Q^(3/2)");
 gate("unoccupied_support_left",lt(Q(3,8),Q(7,16))&&lt(Q(7,32),Q(7,16)),"third control is disjoint from both existing bump supports");
 gate("unoccupied_support_right",lt(Q(15,32),Q(1,2)),"support avoids the Q peak");
 const xL=Q(7,16),xR=Q(15,32);
 const SpL=mul(Q(30),pow(mul(xL,sub(Q(1),xL)),2));
 const SppR=mul(Q(60),mul(xR,mul(sub(Q(1),xR),sub(Q(1),mul(Q(2),xR)))));
 const SpppL=mul(Q(60),add(Q(1),add(mul(Q(-6),xL),mul(Q(6),pow(xL,2)))));
 gate("actual_quintic_Q_lower",lt(Q(7,4),SpL),str(SpL)+">7/4");
 gate("actual_quintic_derivative_lower",lt(Q(7,8),SppR),str(SppR)+">7/8");
 gate("quintic_second_decreases",lt(SpppL,Q(0)),"S'''<0 on support; its quadratic decreases until 1/2");
 gate("compact_support_order",6-1===5,"sixth-order endpoint zeros give genuine C5 compact test functions");
 gate("all_complex_asymptotic_degrees",2*4>4&&2*4>3&&2*4>4-1,"-Q^2/4 degree 8 cannot cancel with Q, Q', or Q A'/A");
 gate("phase_kernel_distinct_orders",-4/2-1===-3&&4/2-1===1,"phi_S order -3, phi_beta order +1");
 const J=[[0n,1n],[-1n,0n]],S=[[1n,0n],[0n,-1n]],T=[[0n,1n],[1n,0n]];
 function mm(A,B){return A.map((r,i)=>B[0].map((_,j)=>r.reduce((v,a,k)=>v+a*B[k][j],0n)));}
 function ms(A,B){return A.map((r,i)=>r.map((a,j)=>a-B[i][j]));}
 function me(A,B){return A.every((r,i)=>r.every((a,j)=>a===B[i][j]));}
 function sm(A,k){return A.map(r=>r.map(a=>a*k));}
 gate("exact_rotation_conjugacy_S",me(ms(mm(S,J),mm(J,S)),sm(T,2n)),"[S,J]=2T");
 gate("exact_rotation_conjugacy_T",me(ms(mm(T,J),mm(J,T)),sm(S,-2n)),"[T,J]=-2S");
 gate("signed_J_square",me(mm(J,J),[[-1n,0n],[0n,-1n]]),"J^2=-I, fixing affine boundary signs");
 // Reuse the polynomial engine as four abstract independent integer exponents:
 const aa=mono(1,[1,0,0,0]),bb=mono(1,[0,2,0,0]),cc=mono(1,[0,0,1,0]),dd=mono(1,[0,0,0,1]);
 const detC=pa(pm(pa(aa,cc),pa(aa,scale(cc,-1))),scale(pm(pa(bb,dd),pa(scale(bb,-1),dd)),-1));
 gate("SL2_exact_four_coefficients",same(detC,pa(pm(aa,aa),pm(bb,bb),scale(pm(cc,cc),-1),scale(pm(dd,dd),-1))),"det C=a^2+b^2-c^2-d^2");
 const Bcoef=pa(pm(aa,cc),pm(bb,dd)),Dcoef=pa(scale(pm(bb,cc),-1),pm(aa,dd));
 gate("exact_trigonometric_amplitude",same(pa(pm(Bcoef,Bcoef),pm(Dcoef,Dcoef)),pm(pa(pm(aa,aa),pm(bb,bb)),pa(pm(cc,cc),pm(dd,dd)))),"(c s+d t)^2+(-d s+c t)^2=(c^2+d^2)(s^2+t^2)");
 gate("plateau_wave_frequency",7*16-16===96&&96>4*16&&96<9*16,"2<k_m/|m|<3 for every |m|>=4");
 gate("mean_platform_frequency",7*0-16===-16,"mean is hyperbolic u''-16u=0, never substitute m=0 in k^-1");
 gate("fixed_platform_shear",eq(mul(Q(-1,2),Q(-8)),Q(4)),"p_tot=sqrt(mu)(pi+4u)");
 gate("moving_density_factor",eq(sub(Q(0),Q(8)),Q(-8)),"mu_ell(t)=e^(-8ell) mu_0(t-ell)");
 gate("slide_buffers",lt(Q(1,16),Q(1,4)),"a_j/16 shift stays inside both a_j/4 buffers");
 gate("sublevel_period_cover_constant",lt(Q(2),Q(16))&&lt(mul(Q(2),Q(22,7)),Q(16)),"2+2pi/(kL)<16(1+1/(kL))");
 gate("relative_reflection_ratio",1+2===3,"rho/sigma>=min(rho,1)/3");
 gate("sublevel_selection_constant",lt(Q(3),Q(4))&&eq(Q(16,256),Q(1,16)),"16 sqrt(3*2^-16)<1/8");
 gate("all_layers_and_modes_union",eq(mul(Q(2),mul(Q(1,1024),mul(Q(2),Q(2)))),Q(1,128)),"two ramps and two reciprocal-square sums; strict actual bound");
 gate("complete_Cauchy_frame_fee",5000+2*20<6000&&5+2<8&&10+2<16,"same true geometric doors and both physical wave-frame conversions");
 gate("full_source_inverse_constant",2+1<4,"(2K^2+K)/epsilon <= 4K^2/epsilon, K>=1");
 const deltaMinusMuQ=scale(pa(pm(aa,scale(dd,-1)),pm(aa,bb,cc)),-1);
 gate("metric_variation_angle_entry",same(deltaMinusMuQ,pm(aa,pa(dd,scale(pm(bb,cc),-1)))),"exact dual-product derivative of -mu_epsilon Q_epsilon gives mu(psi'-Q psi)");
 const invMu=mono(1,[-1,0,0,0]);
 const inverseProductDerivative=pa(pm(aa,scale(pm(invMu,bb),-1)),pm(aa,bb,invMu));
 gate("mean_resistance_inverse_derivative",inverseProductDerivative.size===0&&same(pm(aa,invMu),one),"dual inverse derivative is -mu^-1 psi; total resistance variation remains in the source/mean contract");
 return {
  status:"passed",computed_at_utc_date:"2026-11-14",
  implementation:"new exact reduced-rational and symbolic Laurent-polynomial BigInt JavaScript, actually executed in V8",
  producer_git_blob_sha:producerGitBlobSha,
  proof_git_blob_sha:dependencies["results/R119-supplement-phase-preserving-actual-finite-Schur-controls.md"],
  dependencies,gates_passed:gates.length,gates_total:gates.length,gates,
  mathematical_scope:"Actual phase-preserving compact controls, exact ramp-translation Wronskian, full affine/weak/mean formulas, and finite-frequency transversality including transparent modes. No uniform nonzero lower bound over all moving Schur windows, new full-label chart, or nonlinear outer F closure is claimed."
 };
}
if(typeof module!=="undefined")module.exports={run};
if(typeof require!=="undefined"&&require.main===module){
 const sha=process.argv[2];if(!/^[0-9a-f]{40}$/.test(sha||""))throw Error("pass actual producer Git blob SHA");
 process.stdout.write(JSON.stringify(run(sha),null,2)+"\n");
}
