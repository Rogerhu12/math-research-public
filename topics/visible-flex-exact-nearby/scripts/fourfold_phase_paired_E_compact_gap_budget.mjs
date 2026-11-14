#!/usr/bin/env node
// R109 supplement: full paired E gap, real cutoff energies, and compact-pair lower bounds.
// The exact BigInt core has run in V8; this Node filesystem entry is separately labelled.
import {readFileSync,writeFileSync,mkdirSync} from "node:fs";
import {createHash} from "node:crypto";
import {resolve,dirname} from "node:path";
import {fileURLToPath,pathToFileURL} from "node:url";
const sha=x=>createHash("sha256").update(x,"utf8").digest("hex");
const INPUTS=[
  {
    "key": "v0",
    "path": "notes/2026-11-12-ci-canonical-v0-scaled-Wiener-summary.json",
    "sha256": "66112956b245389aa38c3d07244685ad31c29f7aae0575b8986bf80b54459ce8"
  },
  {
    "key": "v1",
    "path": "notes/2026-11-12-ci-canonical-v1-scaled-Wiener-summary.json",
    "sha256": "c0050bf6f15666f1b0283d7d232c10a167d08a4bb69e42c6cc5653dc51c94c3b"
  },
  {
    "key": "contact",
    "path": "notes/2026-11-12-ci-direct-canonical-source-summary.json",
    "sha256": "826bda30e5d42bf47efc4fb5daa3bf6da1361bb2f4ee737486f89be9c597ca09"
  },
  {
    "key": "root",
    "path": "notes/2026-11-12-actual-common-root-high-remainder.json",
    "sha256": "e727251cd6c187ded5782aff3a03401301d21b83fd03d419f31f716862be6253"
  },
  {
    "key": "rootChange",
    "path": "notes/2026-11-12-R109-frozen-linear-Airy-root-budget.json",
    "sha256": "d73ccef2d88d1ba22ee7f548a576ebb50b2891f1b2a571fbcb065b6ee104d8df"
  },
  {
    "key": "streamBudget",
    "path": "notes/2026-11-12-R108-canonical-stream-gap-budget.json",
    "sha256": "c1b90d922f0484358397b66c149efeb36e0eeb54412eadc3ae6ad022740d4a7c"
  },
  {
    "key": "fullR96",
    "path": "notes/2026-11-12-actual-direct-canonical-source-budget.json",
    "sha256": "b568783f5270102aac2ed2d9656c6e86cc6acdce734358e53a0ac4a265513d3c"
  }
];
export const pairedBudget=function(inputs,progress=()=>{}){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
 const F=(n,d=1n)=>{if(typeof n==="object"&&n.n!==undefined)return n;n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}if(!d)throw Error("zero divisor");const g=gcd(n,d);return{n:n/g,d:d/g};};
 const add=(a,b)=>{a=F(a);b=F(b);return F(a.n*b.d+b.n*a.d,a.d*b.d);},neg=x=>F(-x.n,x.d),sub=(a,b)=>add(a,neg(F(b)));
 const mul=(a,b)=>{a=F(a);b=F(b);return F(a.n*b.n,a.d*b.d);},div=(a,b)=>{a=F(a);b=F(b);return F(a.n*b.d,a.d*b.n);},pow=(x,k)=>F(x.n**BigInt(k),x.d**BigInt(k));
 const lt=(a,b)=>{a=F(a);b=F(b);return a.n*b.d<b.n*a.d;};
 const dec=x=>{x=String(x);if(x.includes("/")){const[a,b]=x.split("/");return F(a,b);}const m=/^([+-]?)(\d*)(?:\.(\d*))?(?:[eE]([+-]?\d+))?$/.exec(x);if(!m)throw Error(x);let n=BigInt((m[2]||"0")+(m[3]||""));if(m[1]==="-")n=-n;const e=Number(m[4]||0)-(m[3]||"").length;return e>=0?F(n*10n**BigInt(e)):F(n,10n**BigInt(-e));};
 const iv=x=>{if(typeof x==="object")return iv(x.ball||x.upper);const s=String(x).trim();if(!s.startsWith("[")){const q=dec(s);return[q,q];}const m=/^\[\s*(\S+)\s+\+\/-\s+(\S+)\s*\]$/.exec(s);if(!m)throw Error(s);const c=dec(m[1]),r=dec(m[2]);return[sub(c,r),add(c,r)];};
 const upper=x=>iv(x)[1],ceilInt=x=>(x.n+x.d-1n)/x.d;
 const up=(x,k=30)=>{if(x.n<0n)throw Error("negative positive rounding");const s=10n**BigInt(k);return F((x.n*s+x.d-1n)/x.d,s);};
 const plus=(a,b)=>up(add(a,b)),times=(a,b)=>up(mul(a,b)),over=(a,b)=>up(div(a,b));
 const decimal=(a,k=18)=>{const s=10n**BigInt(k),q=(a.n*s+a.d-1n)/a.d,t=q.toString().padStart(k+1,"0");return t.slice(0,-k)+"."+t.slice(-k);};
 const pack=x=>{x=up(x);return{numerator:x.n.toString(),denominator:x.d.toString(),decimal_upper:decimal(x)};};
 const ir=(n,p)=>{if(n<2n)return n;const P=BigInt(p);let x=1n<<BigInt(Math.ceil(n.toString(2).length/p));let count=0;while(true){if(++count>1000)throw Error("root iteration");const y=((P-1n)*x+n/x**(P-1n))/P;if(y>=x){while((x+1n)**P<=n)x++;while(x**P>n)x--;return x;}x=y;}};
 const rootLo=(a,p)=>{const s=10n**24n;return F(ir(a.n*s**BigInt(p)/a.d,p),s);};
 const rootHi=(a,p)=>{const s=10n**24n;return F(ir(a.n*s**BigInt(p)/a.d,p)+1n,s);};

 const checks=[],check=(name,ok)=>{checks.push({name,passed:!!ok});if(!ok)throw Error(name);};
 const sum=xs=>xs.reduce(plus,F(0)),prod=xs=>xs.reduce(times,F(1)),sq=x=>times(x,x);
 const momentAudit=(function(inputs,progress=()=>{}){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
 const F=(n,d=1n)=>{if(typeof n==="object"&&n.n!==undefined)return n;n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}if(!d)throw Error("zero divisor");const g=gcd(n,d);return{n:n/g,d:d/g};};
 const add=(a,b)=>{a=F(a);b=F(b);return F(a.n*b.d+b.n*a.d,a.d*b.d);},neg=x=>F(-x.n,x.d),sub=(a,b)=>add(a,neg(F(b)));
 const mul=(a,b)=>{a=F(a);b=F(b);return F(a.n*b.n,a.d*b.d);},div=(a,b)=>{a=F(a);b=F(b);return F(a.n*b.d,a.d*b.n);},pow=(x,k)=>F(x.n**BigInt(k),x.d**BigInt(k));
 const lt=(a,b)=>{a=F(a);b=F(b);return a.n*b.d<b.n*a.d;};
 const dec=x=>{x=String(x);if(x.includes("/")){const[a,b]=x.split("/");return F(a,b);}const m=/^([+-]?)(\d*)(?:\.(\d*))?(?:[eE]([+-]?\d+))?$/.exec(x);if(!m)throw Error(x);let n=BigInt((m[2]||"0")+(m[3]||""));if(m[1]==="-")n=-n;const e=Number(m[4]||0)-(m[3]||"").length;return e>=0?F(n*10n**BigInt(e)):F(n,10n**BigInt(-e));};
 const iv=x=>{if(typeof x==="object")return iv(x.ball||x.upper);const s=String(x).trim();if(!s.startsWith("[")){const q=dec(s);return[q,q];}const m=/^\[\s*(\S+)\s+\+\/-\s+(\S+)\s*\]$/.exec(s);if(!m)throw Error(s);const c=dec(m[1]),r=dec(m[2]);return[sub(c,r),add(c,r)];};
 const upper=x=>iv(x)[1],ceilInt=x=>(x.n+x.d-1n)/x.d;
 const up=(x,k=30)=>{if(x.n<0n)throw Error("negative positive rounding");const s=10n**BigInt(k);return F((x.n*s+x.d-1n)/x.d,s);};
 const plus=(a,b)=>up(add(a,b)),times=(a,b)=>up(mul(a,b)),over=(a,b)=>up(div(a,b));
 const decimal=(a,k=18)=>{const s=10n**BigInt(k),q=(a.n*s+a.d-1n)/a.d,t=q.toString().padStart(k+1,"0");return t.slice(0,-k)+"."+t.slice(-k);};
 const pack=x=>{x=up(x);return{numerator:x.n.toString(),denominator:x.d.toString(),decimal_upper:decimal(x)};};
 const ir=(n,p)=>{if(n<2n)return n;const P=BigInt(p);let x=1n<<BigInt(Math.ceil(n.toString(2).length/p));let count=0;while(true){if(++count>1000)throw Error("root iteration");const y=((P-1n)*x+n/x**(P-1n))/P;if(y>=x){while((x+1n)**P<=n)x++;while(x**P>n)x--;return x;}x=y;}};
 const rootLo=(a,p)=>{const s=10n**24n;return F(ir(a.n*s**BigInt(p)/a.d,p),s);};
 const rootHi=(a,p)=>{const s=10n**24n;return F(ir(a.n*s**BigInt(p)/a.d,p)+1n,s);};

 const lo=x=>iv(x)[0], max=(a,b)=>lt(a,b)?b:a, min=(a,b)=>lt(a,b)?a:b;
 const {v0,v1}=inputs;
 const get=(v,K,a,m)=>{const r=v.budgets.find(z=>z.high_cutoff===K&&z.weight_order===a&&z.moment===m);if(!r)throw Error("row "+K+"/"+a+"/"+m);return r;};
 const lower=r=>max(F(0),sub(lo(r.finite_reference_sum||r.finite_reference_sum_div3),upper(r.complete_low_coefficient_L2_fee||r.complete_low_coefficient_L2_fee_div3)));
 const calc=(v,factor)=>{
  const Ks=[...new Set(v.budgets.map(r=>r.high_cutoff))];let U=[null,null,null,null],w=[];
  for(const K of Ks){
   const r00=get(v,K,0,0),r01=get(v,K,0,1),r11=get(v,K,1,1),r21=get(v,K,2,1);
   const u=[upper(r00.true_scaled_Wiener_upper),upper(r01.true_scaled_Wiener_upper),
    mul(F(K+1),sub(upper(r11.true_scaled_Wiener_upper),lower(r01))),
    mul(F((K+1)**2),add(sub(upper(r21.true_scaled_Wiener_upper),mul(2,lower(r11))),upper(r01.true_scaled_Wiener_upper)))];
   u.forEach((x,j)=>{if(x.n<0n)throw Error("negative moment");if(U[j]===null||lt(x,U[j]))U[j]=x;});
   w.push({K,ordinary_moment_upper:u.map(x=>pack(mul(factor,x)))});
  }
  return {full_upper:U.map(x=>pack(mul(factor,x))),integer_upper:U.map(x=>ceilInt(mul(factor,x)).toString()),candidates:w};
 };
 return {v0:calc(v0,1),v1:calc(v1,3)};
})(inputs);
 const V=momentAudit.v0.integer_upper.map(x=>F(x)),W=momentAudit.v1.integer_upper.map(x=>F(x));
 const {v0,v1,contact,root,rootChange,scalarTerms,streamBudget}=inputs;
 check("source_reports_proved",[v0,v1,contact,root,rootChange].every(x=>x.proved));
 for(const k of ["exact_parameter_interval","exact_center_parameter","exact_parameter_half_width","origin_inputs_sha256","direction_sha256"])
  check("same_actual_"+k,[v1,root].every(x=>JSON.stringify(x.identity[k])===JSON.stringify(v0.identity[k])));
 check("same_R109_actual",JSON.stringify(rootChange.actual_identity)===JSON.stringify(v0.identity));
 check("R108_same_actual",JSON.stringify(streamBudget.actual_identity)===JSON.stringify(v0.identity));
 check("R108_complete_matrix_factor",lt(F(streamBudget.inverse_density_factor_including_normalized_matrix.numerator,streamBudget.inverse_density_factor_including_normalized_matrix.denominator),F(2257,1000)));
 check("R108_mu_upper",!lt(F(24940215,1000000),F(streamBudget.coefficient_bounds.mu0.numerator,streamBudget.coefficient_bounds.mu0.denominator)));
 check("R108_root_height_upper",!lt(F(1477443,1000000),F(streamBudget.true_root_height_upper.numerator,streamBudget.true_root_height_upper.denominator)));
 check("eta_1e_minus9",v0.identity.exact_parameter_half_width==="1/1000000000");
 check("true_complete_R96_cells",contact.actual_cells===178);
 check("q_range",lt(F(243,25),iv(v0.true_frequency.lower)[0])&&lt(upper(v0.true_frequency.upper),10));
 const H=F(49,102400),eps=F(1552858,10n**12n),G=F(33417980,10n**6n),tmin=F(11568,10000),dens=F(2257,1000),qlo=F(243,25),Q=F(40);
 check("epsilon_upper",lt(upper(contact.constants.epsilon),eps));
 check("height_gradient_upper",lt(upper(contact.constants.G0),G));
 check("height_lower",lt(tmin,iv(contact.constants.actual_height_lower)[0]));
 check("H_inside_y_of_physical_h",lt(F(49,50),iv(contact.constants.actual_defining_ratio_lower)[0]));
 check("physical_h",String(contact.constants.physical_collar_height.ball).startsWith("0.000488281250"));
 const db=scalarTerms.find(x=>x.name==="DB_without_Cphi"),byy=scalarTerms.find(x=>x.name==="LB_normal");
 check("V2_scalar_orders",db.radial_order==="2"&&byy.radial_order==="0");
 const V2=plus(upper(db.complete_multiplier_bound),times(F(5,2),upper(byy.complete_multiplier_bound)));
 const coeffDirect=over(eps,rootLo(sub(1,eps),2));
 const coeffStream=over(prod([rootHi(dens,2),G,eps]),tmin);
 const lambda1=times(4,qlo);
 const fact=n=>{let t=1n;for(let i=2n;i<=BigInt(n);i++)t*=i;return t;};
 const choose=(n,r)=>F(fact(n),fact(r)*fact(n-r));
 const cutNormSquared=p=>{
  let I=F(0);for(let r=0;r<=p;r++)I=add(I,mul(div(choose(p,r),F(2n**BigInt(p))),F(fact(r+4)*fact(4),fact(r+9))));
  return mul(div(F(1800),H),I);
 };
 const cutoffWeights=[0,10,11].map(p=>({p,Lp:pack(cutNormSquared(p)),sqrtLp:pack(rootHi(cutNormSquared(p),2))}));
 check("cutoff_L0_identity",!lt(cutNormSquared(0),div(20,mul(7,H)))&&!lt(div(20,mul(7,H)),cutNormSquared(0)));

 const gammaHead=a=>{let x=F(0);for(let n=0;n<=10;n++){const t=div(1,mul(F(fact(n)),add(n,a)));x=add(x,n%2?neg(t):t);}return x;};
 let eLower=F(0);for(let n=0;n<=10;n++)eLower=add(eLower,F(1,fact(n)));
 const invE=div(1,eLower);
 const gamma23=add(gammaHead(F(2,3)),add(mul(F(4,5),invE),mul(F(1,5),pow(invE,2))));
 const gamma13=add(gammaHead(F(1,3)),add(mul(F(2,3),invE),mul(F(1,3),pow(invE,2))));
 check("Gamma23_secant_endpoint",lt(F(1,2),pow(F(4,5),3)));
 check("Gamma13_secant_endpoint",lt(F(1,4),pow(F(2,3),3)));
 const Ai0lower=div(1,mul(rootHi(F(9),3),gamma23));
 const Ai1lower=div(1,mul(rootHi(F(3),3),gamma13));
 check("Ai0_above_035",lt(F(35,100),Ai0lower));
 check("minus_Ai1_above_025",lt(F(25,100),Ai1lower));
 check("cAi0_below_0432",!lt(pow(F(432,1000),2),div(pow(F(36,100),3),F(25,100))));
 check("cAbsAi1_below_0306",lt(mul(F(36,100),F(26,100)),pow(F(306,1000),2)));
 check("cAi0_above_04",lt(pow(F(4,10),2),div(pow(F(35,100),3),F(26,100))));
 check("cAbsAi1_above_0295",lt(pow(F(295,1000),2),mul(F(35,100),F(25,100))));
 const expLower=F(157,81);
 check("Ai_positive_z_F_bound",lt(div(F(432,1000),expLower),F(224,1000)));
 check("Ai_positive_sqrtz_Fp_bound",lt(div(F(648,1000),expLower),F(335,1000)));
 const negF=div(F(5085,10000),sub(1,F(1,128)));
 check("Ai_negative_F_bound",lt(negF,F(513,1000)));
 check("Ai_negative_Fp_bound",lt(add(F(306,1000),div(negF,32)),F(323,1000)));
 check("Ai_third_negative_bound",lt(add(F(513,1000),mul(F(1,4),F(323,1000))),F(738,1000)));
 check("Ai_third_positive_large_bound",lt(div(F(108,100),expLower),F(738,1000)));
 const M1=F(323,1000),M2=F(224,1000),M3=F(738,1000),aU=F(6,5);
 const rows=[];
 for(const rr of root.budgets){
  const K=rr.canonical_high_cutoff,L=dec(rr.strict_Lambda_lower),cl=dec(rr.strict_cuberoot_Lambda_lower);
  progress("actual paired E K="+K);
  check("frequency_K"+K,lt(L,mul(mul(4,qlo),K+1)));
  check("cuberoot_K"+K,lt(pow(cl,3),L));
  const t=over(W[0],sq(L)),u=rootLo(sub(1,t),3);
  check("t_below_half_K"+K,lt(t,F(1,2)));
  check("a_upper_K"+K,lt(add(1,t),pow(aU,3)));
  const um=n=>over(1,pow(u,n));
  const A=[
   over(times(W[0],um(2)),3),
   over(times(W[1],um(2)),3),
   sum([over(times(W[2],um(2)),3),over(prod([F(2),sq(W[1]),um(5)]),times(9,sq(L)))]),
   sum([over(times(W[3],um(2)),3),over(prod([F(2),W[1],W[2],um(5)]),times(3,sq(L))),over(prod([F(10),pow(W[1],3),um(8)]),times(27,pow(L,4)))])
  ];
  const B=[
   um(2),
   over(prod([F(2),W[1],um(5)]),times(3,sq(L))),
   sum([over(prod([F(2),W[2],um(5)]),times(3,sq(L))),over(prod([F(10),sq(W[1]),um(8)]),times(9,pow(L,4)))]),
   sum([over(prod([F(2),W[3],um(5)]),times(3,sq(L))),over(prod([F(10),W[1],W[2],um(8)]),times(3,pow(L,4))),over(prod([F(80),pow(W[1],3),um(11)]),times(27,pow(L,6)))])
  ];
  const Z=A.map((a,r)=>plus(times(H,a),sum(Array.from({length:r+1},(_,k)=>prod([choose(r,k),V[k],B[r-k]])))));
  const inv=(n,d)=>{if(d!==3)throw Error("fractional exponent");const q=Math.floor(n/3),r=n%3;return over(1,prod([pow(L,q),pow(cl,r)]));};
  const S=prod([V[0],B[0],inv(4,3)]);
  check("all_Airy_arguments_above_minus_quarter_K"+K,lt(S,F(1,4)));
  const Cv0=prod([M1,Z[0],inv(5,3)]);
  const Cv2=sum([prod([M2,sq(Z[1]),inv(9,3)]),prod([M1,Z[2],inv(5,3)])]);
  const Cr0=sum([prod([M1,A[0],inv(5,3)]),prod([M2,Z[0],inv(3,3)])]);
  const Cr2=sum([prod([M1,A[2],inv(5,3)]),prod([F(2),M2,A[1],Z[1],inv(9,3)]),prod([aU,M3,sq(Z[1]),inv(7,3)]),prod([aU,M2,Z[2],inv(3,3)])]);
  const Cp0=prod([M1,Z[0],inv(2,3)]);
  const Cp2=sum([prod([M2,sq(Z[1]),inv(6,3)]),prod([M1,Z[2],inv(2,3)])]);
  const Cx0=prod([M1,Z[1],inv(5,3)]);
  const Cx2=sum([prod([M3,pow(Z[1],3),inv(13,3)]),prod([F(3),M2,Z[1],Z[2],inv(9,3)]),prod([M1,Z[3],inv(5,3)])]);
  const lag=(x,y)=>plus(x,times(F(10,3),y));
  const Cv=lag(Cv0,Cv2),Cr=lag(Cr0,Cr2),Cp=lag(Cp0,Cp2),Cx=lag(Cx0,Cx2);
  const energy=[];
  for(const p of [0,10,11]){
   const sqrtLp=rootHi(cutNormSquared(p),2);
   const free=p===0?F(36,100):rootHi(F(162401,1000000*p),2);
   const freeCut=prod([F(432,1000),inv(1,3),sqrtLp]);
   const radial=times(Cr,rootHi(div(H,p+1),2));
   const angle=over(times(plus(Cp,times(Q,Cx)),H),rootLo(F(p+2),2));
   const deltaCut=times(Cv,sqrtLp);
   const Gp=sum([free,freeCut,radial,angle,deltaCut]);
   energy.push({p,total:pack(Gp),free_gradient:pack(free),free_cutoff:pack(freeCut),delta_radial:pack(radial),delta_angle:pack(angle),delta_cutoff:pack(deltaCut)});
  }
  const E=p=>{const v=energy.find(x=>x.p===p).total;return F(v.numerator,v.denominator);};
  const direct=times(coeffDirect,E(11));
  const streamRadial=times(coeffStream,over(times(H,E(0)),rootLo(F(156),2)));
  const streamAngular=times(coeffStream,over(E(10),times(lambda1,rootLo(H,2))));
  const stream= rootHi(plus(sq(streamRadial),sq(streamAngular)),2);
  const paired=sum([direct,stream]);

  const lowerPack=x=>{const s=10n**30n,t=x.n*s/x.d,y=F(t,s),d=10n**18n,q=y.n*d/y.d,v=q.toString().padStart(19,"0");return {numerator:y.n.toString(),denominator:y.d.toString(),decimal_lower:v.slice(0,-18)+"."+v.slice(-18)};};
  const rootValueLo=sub(F(4,10),mul(M1,S)),rootValueHi=plus(F(432,1000),times(M1,S));
  const rootSlopeLo=sub(F(295,1000),mul(M2,S)),rootSlopeHi=plus(F(306,1000),times(M2,S));
  const upperLambda=F(40*(K+1)),upperCube=rootHi(upperLambda,3),rootTau=F(1477443,1000000),mu=F(24940215,1000000);
  const rootPmin=div(sub(mul(mul(u,cl),rootSlopeLo),div(mul(mu,rootValueHi),cl)),rootTau);
  check("root_value_positive_K"+K,rootValueLo.n>0n);
  check("root_pure_mode_conormal_negative_K"+K,rootPmin.n>0n);
  const primalLower=div(pow(div(mul(tmin,rootValueLo),upperCube),2),mul(dens,H));
  const dualLower=mul(div(mul(2,pow(tmin,2)),mul(add(1,eps),pow(H,2))),pow(div(rootPmin,upperLambda),2));
  const aRatio=rootHi(add(1,t),3);
  const newMeanObject=rootChange.rows.find(x=>x.K===K).new_complete_mean;
  const meanUpper=F(newMeanObject.numerator,newMeanObject.denominator);
  const crossUpper=sum([prod([F(2),aRatio,rootValueHi,rootSlopeHi]),
   over(prod([F(2),mu,sq(rootValueHi)]),sq(cl)),
   over(prod([F(2),rootTau,rootValueHi,meanUpper]),cl)]);
  const gapLowerSquared=sub(add(primalLower,dualLower),crossUpper);
  check("compact_full_gap_lower_positive_K"+K,gapLowerSquared.n>0n);
  const compactLower={test_input_index:K+1,root_value_amplitude_lower:lowerPack(rootValueLo),
   root_value_amplitude_upper:pack(rootValueHi),root_slope_amplitude_lower:lowerPack(rootSlopeLo),
   root_slope_amplitude_upper:pack(rootSlopeHi),root_conormal_modulus_lower:lowerPack(rootPmin),
   primal_energy_lower:lowerPack(primalLower),dual_energy_lower:lowerPack(dualLower),twice_root_cross_absolute_upper:pack(crossUpper),
   full_gap_squared_lower:lowerPack(gapLowerSquared),full_gap_lower:lowerPack(rootLo(gapLowerSquared,2)),
   scope:"Any compact primal with the R109 root value and any compact solenoidal dual with root inward flux Pi p0, both zero beyond H, for this pure input; full cap includes zero regular mismatch."};
  const ENrow=contact.high_root_contact_table.find(z=>z.canonical_output_cutoff_N===K);
  check("complete_contact_row_K"+K,!!ENrow);
  const contactE=times(paired,rootHi(plus(upper(ENrow.root_extension_energy),upper(ENrow.regular_mean_extension_energy)),2));
  rows.push({K,L:pack(L),u_lower:{numerator:u.n.toString(),denominator:u.d.toString()},S_upper:pack(S),A:A.map(pack),B:B.map(pack),Z:Z.map(pack),lag_constants:{Cv:pack(Cv),Cr:pack(Cr),Cp:pack(Cp),Cx:pack(Cx)},weighted_energy:energy,
   compact_lower_bound:compactLower,paired_E:{direct:pack(direct),stream_radial:pack(streamRadial),stream_angle:pack(streamAngular),stream_total:pack(stream),gap:pack(paired),complete_high_root_and_regular_contact:pack(contactE)},contact_row:ENrow});
 }
 return {kind:"actual_paired_E_and_complete_cutoff_energy_budget",proved:true,full_cap_gap_paid:false,actual_identity:v0.identity,
 H:pack(H),epsilon:pack(eps),height_C0_gradient:pack(G),height_lower:{numerator:tmin.n.toString(),denominator:tmin.d.toString()},inverse_density_upper:pack(dens),
 Airy_elementary_lower_bounds:{Gamma23_upper:pack(gamma23),Gamma13_upper:pack(gamma13),cAi0_lower:"2/5",cAbsAi1_lower:"59/200",cAi0_upper:"54/125",cAbsAi1_upper:"153/500"},E_profile_power:"11/2",ordinary_index_moments:momentAudit,V2_Htwo_thirds_multiplier:pack(V2),cutoff_weights:cutoffWeights,rows,checks,
 source_scope:"full operator E contribution, full trial gradient, and a strictly positive lower bound for compact pairs; no small full scalar/cutoff gap is claimed",
 unpaid:["complete P0(chi Ulin) stream","actual exterior matching if cutoff is removed","same actual physical/symplectic inverse and low-column augmentation"],
 rounding:"All displayed upper rationals use exact BigInt operations and upward 30-decimal rounding; square/cube roots are enclosed at 24 decimals. Moment differences use lower bounds only in subtracted terms."};
};

if(process.argv[1]&&pathToFileURL(resolve(process.argv[1])).href===import.meta.url){
 const topic=resolve(dirname(fileURLToPath(import.meta.url)),".."),inputs={};
 for(const spec of INPUTS){
  const raw=readFileSync(resolve(topic,spec.path),"utf8");
  if(sha(raw)!==spec.sha256)throw Error("input SHA mismatch: "+spec.path);
  inputs[spec.key]=JSON.parse(raw);
 }
 if(inputs.fullR96.proved!==true||inputs.fullR96.actual_cells!==178)throw Error("incomplete R96");
 inputs.scalarTerms=inputs.fullR96.scalar_terms;
 const report=pairedBudget(inputs);
 report.input_reports=INPUTS;
 report.source_sha256=sha(readFileSync(fileURLToPath(import.meta.url),"utf8"));
 report.execution={core_executed:true,full_Node_entry_executed:true,runtime:"Node.js exact BigInt rational arithmetic",new_geometric_sampling:false,full_input_SHA_checks:true};
 const out=process.argv[2]||resolve(topic,"notes/2026-11-13-R109-paired-E-and-compact-gap-budget.json");
 mkdirSync(dirname(out),{recursive:true});writeFileSync(out,JSON.stringify(report,null,2)+"\n");
 process.stdout.write(JSON.stringify({checks:report.checks.length,all_passed:report.checks.every(x=>x.passed),source_sha256:report.source_sha256,report_sha256:sha(readFileSync(out,"utf8")),full_cap_gap_paid:false})+"\n");
}
