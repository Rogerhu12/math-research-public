#!/usr/bin/env node
"use strict";
/*
Uniform exact mode weights for the convective contribution to the mean
height in the fixed actual-q096 chart. Pure algebra, no physical worker.
The normal-velocity mean is NOT bounded by this file.
*/
const MEAN_ENGINE_SHA="e3529092246444db572868f0dc747480b06becbdcecc907f3aff2dcc137b5d1e";
const CHART_CERTIFICATE_SHA="da4709e9bfdc6330e440c8a69a556ddd760ffd364bb05fa45a4caf28eff4e618";
function buildConvection(Q,hash){
 function assert(ok,message){if(!ok)throw Error(message);}
 const Z=Q(0),O=Q(1);
 const add=(a,b)=>a.add(b),mul=(a,b)=>a.mul(b);
 const absMax=a=>a.reduce((x,y)=>x.cmp(y.abs())>=0?x:y.abs(),Z);
 const pow=(a,n)=>{let v=O;for(let j=0;j<n;j++)v=v.mul(a);return v;};
 function binom(n,k){if(k<0||k>n)return 0n;k=Math.min(k,n-k);let r=1n;for(let j=1;j<=k;j++)r=r*BigInt(n-k+j)/BigInt(j);return r;}
 function qratio(a,b){return Q(a).div(Q(b));}
 function cap(q,bits=96){
  assert(q.cmp(Z)>=0,"negative upper bound");const scale=1n<<BigInt(bits);
  const u=Q((q.n*scale+q.d-1n)/q.d).div(Q(scale));
  assert(q.cmp(u)<=0,"outward cap failed");
  return {dyadic_upper:u.toString(),exact_bound_sha256:hash(q.toString()),rounding_bits:bits,
          rounding_verified:true,decimal_display:Number(u.n)/Number(u.d)};
 }
 function polynomialMul(a,b){const r=Array.from({length:a.length+b.length-1},()=>Z);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)r[i+j]=r[i+j].add(a[i].mul(b[j]));return r;}
 function polynomialAdd(a,b){const r=Array.from({length:Math.max(a.length,b.length)},()=>Z);for(let i=0;i<r.length;i++)r[i]=(a[i]||Z).add(b[i]||Z);return r;}
 function scale(a,k){return a.map(x=>x.mul(k));}
 function chebU(n){if(n===0)return [O];let p=[O],q=[Z,Q(2)];for(let j=1;j<n;j++){const xq=[Z,...scale(q,Q(2))];const next=polynomialAdd(xq,scale(p,Q(-1)));p=q;q=next;}return q;}
 function arcsineMean(p){let v=Z;for(let k=0;k<p.length;k+=2)v=v.add(p[k].mul(qratio(binom(k,k/2),4n**BigInt(k/2))));return v;}
 function bernstein(power){
  const n=power.length-1,r=[];
  for(let i=0;i<=n;i++){let x=Z;for(let k=0;k<=i;k++)x=x.add(power[k].mul(qratio(binom(i,k),binom(n,k))));r.push(x);}
  return r;
 }
 const coefficients=[Q("3242591731706757/36028797018963968"),Q("-7337147526749689/1152921504606846976")];
 const L=Q("7092420367637499/2251799813685248"),gauge=coefficients[0];
 const d2=coefficients[0].mul(-3),d4=coefficients[1].mul(-15);
 const r=d2.abs().add(d4.abs()),Aabs=d2.abs().div(2).add(d4.abs().div(4));
 const bp=Q(15).div(L.mul(8)),bpp=Q(6).div(L.mul(L));
 function run(K=32,M=28){
  assert(Number.isInteger(K)&&K>=4&&K<=64,"K outside 4..64");
  assert(Number.isInteger(M)&&M>=2&&M<=48,"M outside 2..48");
  assert(r.cmp(O)<0&&r.cmp(Z)>0,"geometric series radius invalid");
  const table=Array.from({length:M},()=>[]);
  let fourier=[O],powerAtPlus=O,powerAtMinus=O;
  const endpointChecks=[],entryChecks=[];
  const Bpoly=[d4.neg(),d2,d4.mul(2)];
  let Bpower=[O];let independentChecks=0;
  for(let k=0;k<=K;k++){
   const get=n=>fourier[Math.abs(n)]||Z;
   let plus=fourier[0],minus=fourier[0];
   for(let n=1;n<fourier.length;n++){plus=plus.add(fourier[n].mul(2));minus=minus.add(fourier[n].mul(n%2?-2:2));}
   endpointChecks.push(plus.eq(powerAtPlus)&&minus.eq(powerAtMinus));
   for(let j=1;j<=M;j++){
    const ak=d2.div(4).mul(get(j-1).sub(get(j+1))).add(d4.div(8).mul(get(j-2).sub(get(j+2))));
    table[j-1].push(ak);
    entryChecks.push(ak.abs().cmp(Aabs.mul(pow(r,k)))<=0);
    if(k<=4&&j<=4){
     const Asin=scale(polynomialMul(polynomialMul([O,Z,Q(-1)],[d2,d4]),chebU(j-1)),Q("1/2"));
     const direct=arcsineMean(polynomialMul(Asin,Bpower));
     assert(direct.eq(ak),"independent arcsine moment disagrees");independentChecks++;
    }
   }
   const next=Array.from({length:fourier.length+2},(_,n)=>
    d2.div(2).mul(get(n-1).add(get(n+1))).add(d4.div(2).mul(get(n-2).add(get(n+2)))));
   fourier=next;
   powerAtPlus=powerAtPlus.mul(d2.add(d4));powerAtMinus=powerAtMinus.mul(d2.neg().add(d4));
   if(k<4)Bpower=polynomialMul(Bpower,Bpoly);
  }
  const oneMinus=O.sub(r);
  const R0=Aabs.mul(pow(r,K+1)).div(oneMinus);
  const R1=Aabs.mul(pow(r,K+1)).mul(Q(K+1).div(oneMinus).add(r.div(oneMinus.mul(oneMinus))));
  const records=[];
  for(let j=1;j<=M;j++){
   const poly=table[j-1].map((x,k)=>k%2?x.neg():x);
   const derivative=poly.slice(1).map((x,k)=>x.mul(k+1));
   const valueHull=absMax(bernstein(poly)),derivativeHull=absMax(bernstein(derivative));
   const C=valueHull.add(R0),Cp=derivativeHull.add(R1),m=Q(2*j);
   const first=gauge.abs().mul(m).mul(bp).mul(C);
   const second=gauge.abs().mul(m).mul(bpp.mul(C).add(bp.mul(bp).mul(Cp)));
   records.push({
    vertical_cosine_index:j,physical_frequency:2*j,
    C_value_abs:cap(C),C_derivative_abs:cap(Cp),
    delta_mean_prime_coefficient_weight:cap(first),
    delta_mean_second_coefficient_weight:cap(second),
    delta_mean_second_coefficient_derivative_weight:cap(first),
    exact_moment_row_sha256:hash(table[j-1].map(x=>x.toString()).join("\n")+"\n")
   });
  }
  const checks={
   fixed_chart_radius_below_one:r.cmp(O)<0,
   both_fourier_endpoints_at_every_power:endpointChecks.every(Boolean),
   every_exact_moment_within_uniform_integrand_bound:entryChecks.every(Boolean),
   independent_arcsine_moments_20:independentChecks===20,
   zero_order_j1:table[0][0].eq(d2.div(4)),
   zero_order_j2:table[1][0].eq(d4.div(8)),
   zero_order_higher_modes_vanish:table.slice(2).every(row=>row[0].eq(Z)),
   geometric_value_tail_positive:R0.cmp(Z)>0,
   geometric_derivative_tail_positive:R1.cmp(Z)>0,
   all_reported_dyadic_caps_outward:records.every(x=>[x.C_value_abs,x.C_derivative_abs,x.delta_mean_prime_coefficient_weight,x.delta_mean_second_coefficient_weight,x.delta_mean_second_coefficient_derivative_weight].every(q=>q.rounding_verified))
  };
  assert(Object.values(checks).every(Boolean),"convection certificate check failed");
  return {
   schema:"strong-q096-chart-convection-weights-v1",
   scope:"Uniform all-b mode weights for only the convective v*d_z part of the exact height mean; no actual M28 field evaluated.",
   source_summary_sha256:"c3291bbc2de37008f5a9272e762c628a3f4e95106b3382d6253bf4a5b14c3c2a",
   source_chart_sha256:"7678b2b43984b74c94b948efb21ea014f75a25841ed40527e0b76c569190e0cb",
   prior_chart_certificate_sha256:CHART_CERTIFICATE_SHA,mean_engine_sha256:MEAN_ENGINE_SHA,
   input:{reference_coefficients:coefficients.map(String),reference_frequencies:[2,4],length:L.toString(),gauge:gauge.toString(),transition:[0,1]},
   definitions:{A:"d2 sin(2 psi)/2+d4 sin(4 psi)/4",B:"d2 cos(2 psi)+d4 cos(4 psi)",Cj:"mean_psi A sin(2 j psi)/(1+b B)",transport:"-q b_s sum_j (2j) DeltaY_height,j Cj(b)"},
   truncation_degree:K,vertical_modes:M,uniform_parameter_b:["0","1"],
   geometric_ratio_exact:r.toString(),arc_offset_triangle_bound:Aabs.toString(),
   blend_first_abs:bp.toString(),blend_second_abs:bpp.toString(),
   C_uniform_tail:cap(R0),C_derivative_uniform_tail:cap(R1),
   exact_moment_table_sha256:hash(table.map(row=>row.map(String).join(",")).join("\n")+"\n"),
   checks,all_checks_passed:true,mode_weights:records,
   normal_velocity_mean_paid:false,actual_finite_field_data_loaded:false,
   complete_height_mean_bound:false,actual_prefix_C2_certificate:false,
   physical_RHS_calls:0,tail_workers:0,newton_solves:0,
   limitations:["Only the fixed reference chart is paid. Actual DeltaY and DeltaY_s bounds are required.",
    "The normal part of the Frenet mean remains a separate full-domain obligation.",
    "This is not an angular quadrature alias certificate or a numerical Gauss-height error.",
    "No exact-solution, closed-family, diameter, curvature or reach conclusion is made."]
  };
 }
 return {run};
}
if(typeof module!=="undefined")module.exports={buildConvection};
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module){
 const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto"),args=process.argv.slice(2);
 const i=args.indexOf("--out");if(i<0||!args[i+1])throw Error("--out is required");const out=args[i+1];
 if(fs.existsSync(out))throw Error("fresh output required");
 const hash=s=>crypto.createHash("sha256").update(s).digest("hex");
 const helper=path.join(__dirname,"strong_mean_homotopy_exact.js");
 if(hash(fs.readFileSync(helper))!==MEAN_ENGINE_SHA)throw Error("exact mean helper source differs");
 const {Q}=require(helper),result=buildConvection(Q,hash).run();
 result.source_sha256=hash(fs.readFileSync(__filename));
 const text=JSON.stringify(result,null,2)+"\n";if(Buffer.byteLength(text)>=5000000)throw Error("repository file size exceeded");
 fs.writeFileSync(out,text,{flag:"wx"});
 process.stdout.write(JSON.stringify({event:"chart_convection_weights_complete",out,checks:result.checks,actual_prefix_C2_certificate:false})+"\n");
}
