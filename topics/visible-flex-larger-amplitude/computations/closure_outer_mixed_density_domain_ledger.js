#!/usr/bin/env node
'use strict';
/* Exact scalar domain and high-block bridge for R98. No uncomputed middle
   or mixed Green kernel is replaced by a numerical assertion. */
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r;}return a;}
class Q {
 constructor(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error('zero denominator');if(b<0n){a=-a;b=-b;}const g=gcd(a,b);this.a=a/g;this.b=b/g;}
 add(x){x=q(x);return new Q(this.a*x.b+x.a*this.b,this.b*x.b);}
 neg(){return new Q(-this.a,this.b);}
 sub(x){return this.add(q(x).neg());}
 mul(x){x=q(x);return new Q(this.a*x.a,this.b*x.b);}
 div(x){x=q(x);return new Q(this.a*x.b,this.b*x.a);}
 pow(n){return n<0?new Q(this.b,this.a).pow(-n):new Q(this.a**BigInt(n),this.b**BigInt(n));}
 le(x){x=q(x);return this.a*x.b<=x.a*this.b;}
 lt(x){x=q(x);return this.a*x.b<x.a*this.b;}
 eq(x){x=q(x);return this.a===x.a && this.b===x.b;}
 abs(){return this.a<0n?this.neg():this;}
 record(){return {numerator:String(this.a),denominator:String(this.b)};}
}
function q(a,b){return a instanceof Q?a:new Q(a,b);}
function p2(n){n=Number(n);if(!Number.isSafeInteger(n))throw Error('bad exponent');return n>=0?q(1n<<BigInt(n)):q(1n,1n<<BigInt(-n));}
function dyad(x){return q(x[0]).mul(p2(x[1]));}
function endpoint(x){return q(x.mantissa).mul(p2(x.binary_exponent));}
function upper(x){return endpoint(x.upper);}
function lower(x){return endpoint(x.lower);}
function point(x){const a=lower(x),b=upper(x);if(!a.eq(b))throw Error('expected exact point');return a;}
function addall(xs){return xs.reduce((a,b)=>a.add(b),q(0));}
function maxall(xs){if(!xs.length)throw Error('empty maximum');return xs.reduce((a,b)=>a.lt(b)?b:a);}
function nonzero(x){return upper(x).lt(0)||q(0).lt(lower(x));}
function ceilDecimal(x,digits=28){
 x=q(x);if(x.a<0n)throw Error('positive display only');
 const scale=10n**BigInt(digits),n=(x.a*scale+x.b-1n)/x.b;
 const s=String(n).padStart(digits+1,'0');
 return s.slice(0,-digits)+'.'+s.slice(-digits);
}
function r(x){x=q(x);return {...x.record(),decimal_upward_display:ceilDecimal(x)};}



function runR98Domain(sourceSha,execution){
 const V0=p2(-40),C0=q(10),rT=q(1,8),Astar=p2(-34),B=q(18555);
 const rPhysical=V0.mul(rT),rH=p2(-149).add(p2(-43).div(50));
 const G=q(11798528,45),qH=G.mul(4).mul(257).mul(Astar);
 const full=C0.mul(V0).add(rPhysical).add(B.mul(rH));
 const image=p2(-152).add(p2(-2053)).add(qH.mul(rPhysical.add(rH)));
 const leading=q(4).mul(full.pow(2)).add(q(5,4).mul(full));
 const gates={
  C0_from_R96_strict_total10:C0.eq(10),
  finite_local_radius_is_one_eighth:rT.eq(q(1,8)),
  finite_absolute_radius_equals_old_middle:rPhysical.eq(p2(-43)),
  exact_high_inverse:G.eq(q(11798528,45)),
  exact_high_feedback:qH.eq(q(1480577,94371840)),
  high_feedback_below_one_over60:qH.lt(q(1,60)),
  entire_three_block_domain_below_Astar:full.lt(Astar),
  entire_complete_mean_domain:full.lt(q(1,64)),
  complete_leading_inverse:leading.lt(1),
  given_finite_field_high_selfmap:image.lt(rH)
 };
 if(!Object.values(gates).every(Boolean))throw Error("Unpaid R98 scalar gate");
 return {status:"Executed scalar domain/high bridge only; all finite mixed Green and Schur gates remain explicit inputs",
  source_sha256:sourceSha,execution,gates,all_gates:true,
  V0:r(V0),known_low_local_cap:r(C0),finite_local_radius:r(rT),finite_physical_radius:r(rPhysical),
  balanced_high_radius:r(rH),balanced_to_physical_upper:r(B),
  high_inverse:r(G),high_feedback:r(qH),full_physical_domain:r(full),domain_limit:r(Astar),
  leading_inverse_norm:r(leading),high_image:r(image),
  high_input_from_local_finite_Lipschitz:r(qH.mul(V0)),
  original_R74_domain_only:true,
  uncomputed_inputs:["Gamma_L,p for p=0,1,2","Gamma_M,p for p=0,1,2","all middle true initial traces","all complete middle pure-source responses","three-block selfmaps and Schur inequality"],
  finite_mid_or_full_joint_solution_claimed:false};
}
if(typeof module!=='undefined')module.exports={runR98Domain};
if(typeof require!=='undefined'&&require.main===module){
 const fs=require('node:fs'),crypto=require('node:crypto'),out=process.argv[2];
 if(!out)throw Error("Usage: node closure_outer_mixed_density_domain_ledger.js FRESH_OUTPUT.json");
 const result=runR98Domain(crypto.createHash('sha256').update(fs.readFileSync(__filename)).digest('hex'),
 {engine:"Node.js BigInt",version:process.version});
 fs.writeFileSync(out,JSON.stringify(result,null,2)+'\n',{flag:"wx"});
 process.stdout.write(JSON.stringify({all_gates:result.all_gates,output:out})+'\n');
}
