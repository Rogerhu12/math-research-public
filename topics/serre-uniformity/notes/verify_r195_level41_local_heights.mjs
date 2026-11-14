#!/usr/bin/env node
// Exact recovery after the 2026-11-12 runtime outages.
import fs from 'node:fs';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
const sourceSHA = crypto.createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex');
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const args = process.argv.slice(2);
function option(k) { const i=args.indexOf(k); if(i<0||i+1===args.length) throw Error('Missing '+k); return args[i+1]; }
function readJSON(p) { const b=fs.readFileSync(p); return {raw:b,value:JSON.parse((p.endsWith('.gz')?zlib.gunzipSync(b):b).toString('utf8'))}; }
function bigmod(a,m){return ((a%m)+m)%m;}
function bigpow(a,n,m){let r=1n;for(a=bigmod(a,m);n>0n;n>>=1n,a=a*a%m)if(n&1n)r=r*a%m;return r;}
function invmod(a,m){let b=m,x=1n,y=0n;for(a=bigmod(a,m);b!==0n;){const q=a/b;[a,b]=[b,a-q*b];[x,y]=[y,x-q*y];}if(a!==1n)throw Error('nonunit');return bigmod(x,m);}
function log47(a){const q=47n**4n,z=bigmod(bigpow(BigInt(a),46n,q)-1n,q);return Number(bigmod((z-z*z*invmod(2n,q)+z*z*z*invmod(3n,q))*invmod(46n,q),q));}
function chebyshevShifted(n){
 let a=[2n],b=[2n,1n];if(n===0)return a;if(n===1)return b;
 for(let k=2;k<=n;k++){const c=new Array(b.length+1).fill(0n);for(let j=0;j<b.length;j++){c[j]+=2n*b[j];c[j+1]+=b[j];}for(let j=0;j<a.length;j++)c[j]-=a[j];[a,b]=[b,c];}return b;
}
function computeR195(odd,two){
 const Q=47**4,mod=(n,p=Q)=>((n%p)+p)%p,assert=(b,m)=>{if(!b)throw Error(m);};
 assert(odd.rows.length===54&&two.rows.length===54,'54 common rows');
 const c=chebyshevShifted(41);assert(c[0]===2n&&c[1]===1681n&&c[41]===1n,'exact ST quotient polynomial');
 const nonsquares=Array.from({length:40},(_,i)=>i+1).filter(x=>Number(bigpow(BigInt(x),20n,41n))===40);
 const rows=odd.rows.map((r,i)=>{
  assert(JSON.stringify(r.correspondence)===JSON.stringify(two.rows[i].correspondence),'ordered labels');
  assert(r.CM_return_multiplicity===two.rows[i].CM_return_multiplicity,'CM return match');
  const rho=r.CM_return_multiplicity,I41=-40*rho,I2=two.rows[i].I2;
  const coeff=new Map(r.odd_non41_non47_coefficients);assert(!coeff.has(2)&&!coeff.has(41)&&!coeff.has(47),'old support exclusion');
  if(I2)coeff.set(2,I2);if(I41)coeff.set(41,I41);
  const full=[...coeff].sort((a,b)=>a[0]-b[0]),known=mod(r.known_odd_correction_mod47four+I2*log47(2)+I41*log47(41));
  assert(mod(full.reduce((s,[p,v])=>s+v*log47(p),0))===known,'combined local sum');
  let gaussian=0;const n=r.correspondence.index,R=Math.floor(Math.sqrt(n)),maps=[];
  for(let a=-R;a<=R;a++)for(let b=-R;b<=R;b++)if(a*a+b*b===n){
    gaussian++;const A=mod(a+9*b,41),D=mod(a-9*b,41);assert(A&&D,'prime-to41 Gaussian matrix');
    const factor=Number(bigpow(BigInt(A)*invmod(BigInt(D),41n),2n,41n)),image=nonsquares.map(t=>mod(factor*t,41));
    assert(new Set(image).size===20&&image.every(t=>nonsquares.includes(t)),'Gaussian necklace permutation');
    maps.push({a,b,necklace_factor:factor});
  }
  assert(gaussian/4-(r.correspondence.kind==='cyclic4'?1:0)===rho,'Gaussian return count');
  return {correspondence:r.correspondence,CM_return_multiplicity:rho,I2,I41,
   known_odd_correction_mod47four:r.known_odd_correction_mod47four,non47_coefficients:full,
   non47_correction_mod47four:known,gaussian_transport_checks:maps};
 });
 assert(rows[0].non47_correction_mod47four===4226475,'T1');
 assert(rows[1].non47_correction_mod47four===1840520,'T2');
 assert(rows[2].non47_correction_mod47four===3638646,'T3');
 assert(rows.find(r=>r.correspondence.kind==='cyclic4').non47_correction_mod47four===3837879,'C4');
 return {result:'R195',level:41,auxiliary_prime:47,precision:4,modulus:Q,
  tangent_parameters:{Z_minus4:'j-1728',cusps:'q41'},
  formula:'I41(T_n)=-40*rho(n); C4=T4-T1 has I41=0',
  geometric_inputs:{semistable_base_ramification_index:840,ordinary_components:2,CM_degree_per_component:10,cusp_degree_per_component:10,vertical_correction_for_B:0,
   Serre_Tate_fine_map:'q_ST=w^41',coarse_parameter:'z=w+w^-1-2',j_tangent_valuation_per_CM_point:2,trace_self:-40},
  exact_polynomial:{meaning:'C41(z+2)-2, where C_m(w+w^-1)=w^m+w^-m',coefficients:c.map((x,j)=>(j===0?x-2n:x).toString()),linear_coefficient:1681},
  logarithms:{two:log47(2),forty_one:log47(41)},rows,
  height_equation:'h(B,S_iB)=lambda47(e_i)-non47_correction_i',
  scope:'non47 local coefficients only; geometric identifications are proved separately; enumeration does not prove the global theorem'};
}
const old=readJSON(option('--odd')),two=readJSON(option('--two'));
if(sha(old.raw)!=='b2bdf1471fefc76dd6d05523af8929b66ef770b479534378c414b657d8420b54')throw Error('R190 input SHA');
const result=computeR195(old.value,two.value);
result.generating_source_sha256=sourceSHA;
result.input_sha256={R190_odd_certificate:sha(old.raw),R193_two_certificate:sha(two.raw)};
const raw=Buffer.from(JSON.stringify(result,null,2)+'\n','utf8');
fs.writeFileSync(option('--output'),raw);
console.log(JSON.stringify({status:'PASS',rows:54,source_sha256:sourceSHA,certificate_sha256:sha(raw),first_three_K:result.rows.slice(0,3).map(x=>x.non47_correction_mod47four)}));
