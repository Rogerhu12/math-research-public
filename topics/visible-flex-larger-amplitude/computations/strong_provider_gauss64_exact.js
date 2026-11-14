#!/usr/bin/env node
"use strict";
/* Exact Legendre64 reference rule and conditional neck primitive jet bounds.
   This does not certify an unprovided NumPy node/weight table or an actual neck. */
const ENGINE_SHA="ac4a3e419e064c23a2eb42a1cb626507866d5e74e0ef608313fb887f8dbfcb80";
function buildGauss(Q,hash){
 function assert(ok,message){if(!ok)throw Error(message);}
 const Z=Q(0),O=Q(1);
 const min=(a,b)=>a.cmp(b)<0?a:b,max=(a,b)=>a.cmp(b)>0?a:b;
 const I=(a,b=a)=>{a=Q(a);b=Q(b);assert(a.cmp(b)<=0,"reversed interval");return [a,b];};
 const sub=(a,b)=>I(a[0].sub(b[1]),a[1].sub(b[0]));
 const mul=(a,b)=>{const p=[a[0].mul(b[0]),a[0].mul(b[1]),a[1].mul(b[0]),a[1].mul(b[1])];return I(p.reduce(min),p.reduce(max));};
 const square=a=>{const x=a[0].mul(a[0]),y=a[1].mul(a[1]);return I(a[0].cmp(Z)<=0&&a[1].cmp(Z)>=0?Z:min(x,y),max(x,y));};
 const inv=a=>{assert(a[0].cmp(Z)>0||a[1].cmp(Z)<0,"zero reciprocal");return I(O.div(a[1]),O.div(a[0]));};
 const absmax=a=>max(a[0].abs(),a[1].abs());
 function binom(n,k){if(k<0||k>n)return 0n;k=Math.min(k,n-k);let r=1n;for(let j=1;j<=k;j++)r=r*BigInt(n-k+j)/BigInt(j);return r;}
 function coefficients(n){const p=Array(n+1).fill(0n);for(let k=0;k<=Math.floor(n/2);k++)p[n-2*k]=(k%2?-1n:1n)*binom(n,k)*binom(2*n-2*k,n);return p;}
 function derivative(p){return p.slice(1).map((x,k)=>x*BigInt(k+1));}
 function evalNumerator(p,x){
  let a=p.at(-1),power=x.d;
  for(let k=p.length-2;k>=0;k--){a=a*x.n+p[k]*power;power*=x.d;}
  return {n:a,d:power/x.d};
 }
 function evalRat(p,x,scale){const v=evalNumerator(p,x);return Q(v.n).div(Q(v.d*scale));}
 function signAt(p,x){const n=evalNumerator(p,x).n;return n<0n?-1:n>0n?1:0;}
 function exactFloat(x){
  assert(Number.isFinite(x),"nonfinite seed");if(x===0)return Z;
  const view=new DataView(new ArrayBuffer(8));view.setFloat64(0,x,false);
  const a=view.getUint32(0,false),b=view.getUint32(4,false),negative=(a>>>31)!==0;
  const exp=(a>>>20)&2047,mant=(BigInt(a&1048575)<<32n)|BigInt(b);
  const n=exp===0?mant:mant+(1n<<52n),e=(exp===0?-1022:exp-1023)-52;
  let q=e>=0?Q(n<<BigInt(e)):Q(n).div(Q(1n<<BigInt(-e)));return negative?q.neg():q;
 }
 function cap(q,bits=112){
  assert(q.cmp(Z)>=0,"negative cap");const scale=1n<<BigInt(bits),u=Q((q.n*scale+q.d-1n)/q.d).div(Q(scale));
  assert(u.cmp(q)>=0,"cap did not round outward");
  return {exact_upper:u.toString(),exact_unrounded_sha256:hash(q.toString()),decimal_display:Number(u.n)/Number(u.d),outward_rounding_verified:true};
 }
 function packedInterval(interval,bits=128){
  const scale=1n<<BigInt(bits);
  function floor(q){const n=q.n*scale;return n>=0n?n/q.d:-((-n+q.d-1n)/q.d);}
  const lo=Q(floor(interval[0])).div(Q(scale)),hi=Q(-floor(interval[1].neg())).div(Q(scale));
  assert(lo.cmp(interval[0])<=0&&hi.cmp(interval[1])>=0,"packing not outward");
  return {endpoints:[lo.toString(),hi.toString()],exact_sha256:hash(interval.map(String).join("\n")+"\n")};
 }
 function pow(q,n){let x=O;for(let k=0;k<n;k++)x=x.mul(q);return x;}
 function factorial(n){let x=1n;for(let k=2;k<=n;k++)x*=BigInt(k);return Q(x);}
 function profileConstants(){
  const phi=Q("8/5"),p1=Q(4),p2=Q(65),p3=Q(3300);
  const T0=pow(phi,33).div(factorial(33)),T1=p1.mul(pow(phi,32)).div(factorial(32));
  const T2=p1.mul(p1).mul(pow(phi,31)).div(factorial(31)).add(p2.mul(pow(phi,32)).div(factorial(32)));
  const F2=p1.mul(p1).add(p2),F3=pow(p1,3).add(p1.mul(p2).mul(3)).add(p3);
  return {
   conditional_on_phase_bounds:{abs_phase:phi.toString(),abs_phase_u:p1.toString(),abs_phase_uu:p2.toString(),abs_phase_uuu:p3.toString(),polynomial_degree_on_each_panel:4},
   sin_truncation_degree:31,resulting_u_polynomial_degree:124,gauss_exact_degree:127,
   exact_gauss_primitive_errors:{radius_per_segment_length:cap(T0.mul(2)),physical_first:cap(T0.mul(2).add(T1)),physical_second_times_segment_length:cap(T1.mul(3).add(T2))},
   finite_table_perturbation_errors:{
    definitions:"eta=max normalized-node error; omega=sum absolute normalized-weight errors; approximate nodes must remain in [0,1]. Whole-piece radius sums its ramp subpanels.",
    radius_per_segment_length:{omega:"1/1",eta:p1.toString()},
    physical_first:{omega:O.add(p1).toString(),eta:p1.mul(2).add(F2).toString()},
    physical_second_times_segment_length:{omega:p1.mul(2).add(F2).toString(),eta:p1.mul(2).add(F2.mul(4)).add(F3).toString()}},
   actual_phase_bounds_verified:false,actual_numpy_rule_verified:false,
   actual_floating_evaluation_error_paid:false,actual_seam_or_endpoint_error_paid:false};
 }
 function run(bits=112){
  assert(Number.isInteger(bits)&&bits>=64&&bits<=192,"bisections outside 64..192");
  const n=64,scale=1n<<64n,P=coefficients(n),D=derivative(P),DD=derivative(D);
  const Dmax=Q(n*(n+1)/2),DDmax=Q((n-1)*n*(n+1)*(n+2)/8);
  assert(evalRat(D,O,scale).eq(Dmax)&&evalRat(DD,O,scale).eq(DDmax),"endpoint derivative constant disagrees");
  const expansion=Array(63).fill(0n);
  for(let k=n-1;k>=0;k-=2)for(let j=k-1;j>=0;j-=2){
   const c=BigInt((2*k+1)*(2*j+1)),pj=coefficients(j),factor=1n<<BigInt(n-j);
   for(let r=0;r<pj.length;r++)expansion[r]+=c*pj[r]*factor;
  }
  assert(expansion.length===DD.length&&expansion.every((x,k)=>x===DD[k]),"positive Legendre second-derivative expansion failed");
  const positive=[],initialRadius=Q("1/2048");
  for(let k=1;k<=32;k++){
   const center=exactFloat(Math.cos(Math.PI*(k-0.25)/(64.5)));
   let lo=center.sub(initialRadius),hi=center.add(initialRadius);
   assert(lo.cmp(Z)>0&&hi.cmp(O)<0,"initial root bracket outside (0,1)");
   let sl=signAt(P,lo),sh=signAt(P,hi);assert(sl*sh===-1,"uncertified root seed bracket");
   for(let j=0;j<bits;j++){
    const mid=lo.add(hi).div(2),sm=signAt(P,mid);assert(sm!==0,"unexpected exact rational Legendre root");
    if(sm===sl){lo=mid;sl=sm;}else{hi=mid;sh=sm;}
   }
   assert(signAt(P,lo)*signAt(P,hi)===-1,"final root bracket failed");positive.push(I(lo,hi));
  }
  positive.sort((a,b)=>a[0].cmp(b[0]));
  const roots=[...positive.slice().reverse().map(x=>I(x[1].neg(),x[0].neg())),...positive];
  for(let i=0;i<roots.length;i++){
   assert(roots[i][0].cmp(-1)>0&&roots[i][1].cmp(1)<0,"root outside (-1,1)");
   if(i)assert(roots[i-1][1].cmp(roots[i][0])<0,"root boxes overlap");
   assert(signAt(P,roots[i][0])*signAt(P,roots[i][1])===-1,"root sign check failed");
  }
  const rows=roots.map((x,index)=>{
   const mid=x[0].add(x[1]).div(2),rad=x[1].sub(x[0]).div(2),dp=evalRat(D,mid,scale),eps=DDmax.mul(rad);
   const di=I(dp.sub(eps),dp.add(eps)),oneMinusX2=sub(I(O),square(x));
   assert(di[0].cmp(Z)>0||di[1].cmp(Z)<0,"P' interval crosses zero");
   const weight=inv(mul(oneMinusX2,square(di))),u=I(x[0].add(1).div(2),x[1].add(1).div(2));
   const wp=packedInterval(weight),pd=packedInterval(di);
   return {index,x:x.map(String),normalized_node:u.map(String),normalized_weight:wp.endpoints,
    P64_endpoint_signs:[signAt(P,x[0]),signAt(P,x[1])],P64_prime:pd.endpoints,
    exact_unrounded_sha256:{normalized_weight:wp.exact_sha256,P64_prime:pd.exact_sha256},outward_quantization_bits:128};
  });
  const momentChecks=[],moments=[];
  for(const degree of [0,2,64,126]){
   let total=I(Z);
   for(const row of rows){
    const x=I(Q(row.x[0]),Q(row.x[1])),w=I(Q(row.normalized_weight[0]),Q(row.normalized_weight[1]));
    const x2=square(x);const power=I(pow(x2[0],degree/2),pow(x2[1],degree/2));
    const term=mul(w,power);total=I(total[0].add(term[0]),total[1].add(term[1]));
   }
   const target=O.div(Q(degree+1)),ok=total[0].cmp(target)<=0&&total[1].cmp(target)>=0;
   momentChecks.push(ok);moments.push({canonical_x_degree:degree,exact_normalized_integral:target.toString(),interval:packedInterval(total).endpoints,verified:ok});
  }
  const checks={
   P64_normalization_at_one:evalRat(P,O,scale).eq(O),
   four_normalized_gauss_moments:momentChecks.every(Boolean),
   legendre_integer_polynomial_degree_64:P.length===65&&P.at(-1)!==0n,
   derivative_endpoint_constants_exact:true,positive_second_derivative_legendre_expansion:true,
   all_64_disjoint_sign_change_boxes:rows.length===64,all_weight_and_derivative_packing_outward:true,
   all_nodes_strictly_inside_unit_interval:rows.every(x=>Q(x.normalized_node[0]).cmp(Z)>0&&Q(x.normalized_node[1]).cmp(O)<0),
   all_normalized_weight_intervals_positive:rows.every(x=>Q(x.normalized_weight[0]).cmp(Z)>0),
   exact_reflection_symmetry:roots.every((x,k)=>x[0].eq(roots[63-k][1].neg())&&x[1].eq(roots[63-k][0].neg())),
   original_numpy_table_not_claimed:true};
  assert(Object.values(checks).every(Boolean),"exact Gauss certificate check failed");
  return {
   schema:"strong-legendre64-phase-primitive-v1",scope:"Exact reference Gauss rule and conditional phase-primitive jet error constants, not a certified original numerical neck.",
   checks,all_checks_passed:Object.values(checks).every(Boolean),bisections_per_positive_root:bits,
   root_completeness:"64 disjoint sign-change boxes for a degree-64 polynomial give exactly one root per box and no other roots.",
   seed_status:"Math.cos produced only proposals; every bracket sign, disjointness and completeness decision is exact rational.",
   integer_polynomial_scale:scale.toString(),integer_polynomial_coefficients_ascending:P.map(String),
   derivative_maximum:Dmax.toString(),second_derivative_maximum:DDmax.toString(),
   exact_rule:rows,verified_polynomial_moments:moments,phase_primitive:profileConstants(),
   actual_numpy_table_loaded:false,actual_accepted_prefix_loaded:false,actual_neck_profile_certificate:false,
   physical_RHS_calls:0,tail_workers:0,newton_solves:0,
   remaining:["Compare actual NumPy gu and gw/2 binary64 table with these boxes.","Bind all original phase panels and verify their derivative bounds.","Pay floating evaluations, stored segment endpoints and intended exact seam/profile identity separately."]};
 }
 function compareTable(certificate,table){
  assert(certificate.schema==="strong-legendre64-phase-primitive-v1"&&certificate.all_checks_passed,"wrong exact rule certificate");
  assert(table.schema==="strong-provider-gauss64-binary-table-v1","wrong binary table schema");
  assert(table.normalized_nodes.length===64&&table.normalized_weights.length===64,"need all 64 nodes/weights");
  let eta=Z,omega=Z;const rows=[];
  for(let i=0;i<64;i++){
   const node=Q(table.normalized_nodes[i]),weight=Q(table.normalized_weights[i]),r=certificate.exact_rule[i];
   assert(node.cmp(Z)>0&&node.cmp(O)<0&&weight.cmp(Z)>0,"invalid positive original rule");
   if(i)assert(Q(table.normalized_nodes[i-1]).cmp(node)<0,"original nodes must increase");
   const en=absmax(sub(I(node),I(Q(r.normalized_node[0]),Q(r.normalized_node[1]))));
   const ew=absmax(sub(I(weight),I(Q(r.normalized_weight[0]),Q(r.normalized_weight[1]))));
   eta=max(eta,en);omega=omega.add(ew);rows.push({index:i,node_error_upper:cap(en),weight_error_upper:cap(ew)});
  }
  return {schema:"strong-provider-gauss64-table-comparison-v1",all_64_entries_consumed:true,table_identity:table.identity,
   eta:cap(eta),omega:cap(omega),rows,raw_table_sha256:hash(JSON.stringify(table)),actual_profile_certificate:false,
   actual_numpy_evaluation_roundoff_paid:false,physical_RHS_calls:0,tail_workers:0,newton_solves:0};
 }
 return {run,compareTable,profileConstants};
}
if(typeof module!=="undefined")module.exports={buildGauss};
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module){
 const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto"),args=process.argv.slice(2);
 const option=n=>{const i=args.indexOf(n);return i<0?null:args[i+1];},out=option("--out");
 if(!out||fs.existsSync(out))throw Error("fresh --out required");
 const hash=x=>crypto.createHash("sha256").update(x).digest("hex"),helper=path.join(__dirname,"strong_exact_rational_fast.js");
 if(hash(fs.readFileSync(helper))!==ENGINE_SHA)throw Error("rational arithmetic helper differs");
 const {Q}=require(helper),api=buildGauss(Q,hash);let result;
 if(option("--table")){
  if(!option("--certificate"))throw Error("--certificate required with --table");
  const cb=fs.readFileSync(option("--certificate")),tb=fs.readFileSync(option("--table"));
  result=api.compareTable(JSON.parse(cb),JSON.parse(tb));result.input_certificate_sha256=hash(cb);result.input_table_sha256=hash(tb);
 }else result=api.run();
 result.source_sha256=hash(fs.readFileSync(__filename));result.arithmetic_source_sha256=ENGINE_SHA;
 const text=JSON.stringify(result,null,2)+"\n";if(Buffer.byteLength(text)>=5000000)throw Error("repository file size exceeded");
 fs.writeFileSync(out,text,{flag:"wx"});process.stdout.write(JSON.stringify({event:"provider_gauss64_complete",out,actual_neck_profile_certificate:false})+"\n");
}
