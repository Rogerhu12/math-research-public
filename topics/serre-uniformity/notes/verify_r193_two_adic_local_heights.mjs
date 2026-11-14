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
const Q = 47 ** 4;
function assert(ok, message) { if (!ok) throw new Error(message || 'assertion'); }
function mod(a,p=41) { return ((a % p) + p) % p; }
function powmod(a,n,p=41) { let r=1; for(a=mod(a,p);n>0;n=Math.floor(n/2),a=mod(a*a,p))if(n%2)r=mod(r*a,p);return r; }
function val2(n) { assert(n>0,'positive valuation input');let v=0;while(n%2===0){v++;n/=2;}return v; }
const NONSQUARES=Array.from({length:40},(_,i)=>i+1).filter(t=>powmod(t,20)===40);
assert(NONSQUARES.length===20,'20 necklaces');
function weight(beta) {
 const [a,b,c,d]=beta;
 if(a===0&&b===0)return 20;
 if(c===0&&d===0)return 20;
 return powmod(-(a*a+b*b)*(c*c+d*d),20)===40?1:0;
}
function matrixMatch(beta,n) {
 const [a,b,c,d]=beta;
 const A=mod((a+9*b)*21),B=mod((c+9*d)*21),C=mod((-c+9*d)*21),D=mod((a-9*b)*21);
 assert(mod(A*D-B*C)===mod(n),'quaternion matrix determinant');
 return NONSQUARES.filter(t=>mod(B*D-A*C*t)===0);
}
function hurwitz(n) {
 const M=4*n,r=Math.floor(Math.sqrt(M)), pairs=[new Map(),new Map()];
 for(let a=-r;a<=r;a++)for(let b=-r;b<=r;b++){
  if(mod(a,2)!==mod(b,2)||a*a+b*b>M)continue;
  const k=a*a+b*b,p=mod(a,2);if(!pairs[p].has(k))pairs[p].set(k,[]);pairs[p].get(k).push([a,b]);
 }
 const out=[];
 for(let p=0;p<2;p++)for(const [k,ab] of pairs[p])for(const [a,b] of ab)for(const [c,d] of pairs[p].get(M-k)||[])out.push([a,b,c,d]);
 out.sort((x,y)=>{for(let i=0;i<4;i++)if(x[i]!==y[i])return x[i]-y[i];return 0;});
 let oddSum=0;for(let d=1;d<=n;d+=2)if(n%d===0)oddSum+=d;
 assert(out.length===24*oddSum,'Hurwitz norm mass');
 assert(new Set(out.map(b=>b.join(','))).size===out.length,'unique enumeration');
 return out;
}
function rawRecord(n) {
 let gaussian=0, weightedMass=0, weightedLength=0, noncm=0;
 const histogram={},all=hurwitz(n);
 for(const beta of all){
  const w=weight(beta),matches=matrixMatch(beta,n);assert(w===matches.length,'necklace match');
  weightedMass+=w;
  if(beta[2]===0&&beta[3]===0){gaussian++;continue;}
  noncm++;const L=val2(beta[2]*beta[2]+beta[3]*beta[3]);weightedLength+=L*w;
  const key=L+','+w;histogram[key]=(histogram[key]||0)+1;
 }
 assert(gaussian%4===0&&weightedMass%4===0&&weightedLength%4===0,'marking mass divisibility');
 const rho=gaussian/4,k=val2(n),I2=weightedLength/4+20*rho*k-120*rho;
 return {n,quaternions:all.length,non_gaussian:noncm,gaussian_markings:gaussian,rho,
  depth_weight_histogram:Object.entries(histogram).map(([key,count])=>({depth:Number(key.split(',')[0]),weight:Number(key.split(',')[1]),count})).sort((a,b)=>a.depth-b.depth||a.weight-b.weight),
  weighted_non_gaussian_length:weightedLength,weighted_all_mass:weightedMass,layer_mass:weightedMass/4,valuation_of_degree:k,
  raw_proper_coefficient:weightedLength/4,ramified_degree_correction:20*rho*k,j_tangent_diagonal_correction:-120*rho,I2};
}
function verifyDoubling(n,records) {
 const from=hurwitz(n),to=hurwitz(2*n),target=new Set(to.map(b=>b.join(',')));
 assert(from.length===to.length,'ramified norm counts');
 const images=new Set();
 for(const beta of from){
  const [a,b,c,d]=beta,image=[a-b,a+b,c-d,c+d],key=image.join(',');
  assert(target.has(key),'1+i maps into Hurwitz target');assert(!images.has(key),'injective 1+i');images.add(key);
  assert(weight(beta)===weight(image),'doubling preserves necklace weight');
  if(c||d)assert(val2(image[2]**2+image[3]**2)===val2(c*c+d*d)+1,'doubling length increment');
 }
 assert(images.size===target.size,'surjective 1+i');
 const r=records.get(n)||rawRecord(n),s=records.get(2*n)||rawRecord(2*n);
 assert(s.rho===r.rho&&s.layer_mass===r.layer_mass,'CM/mass doubling');
 assert(s.I2-r.I2===r.layer_mass,'coefficient doubling recurrence');
 return {n,twice:2*n,bijection_size:from.length,weighted_layer:r.layer_mass,intersection_increment:s.I2-r.I2};
}
function computeR193(oddCertificate) {
 assert(oddCertificate.rows.length===54,'54 original rows');
 const labels=oddCertificate.rows.map(r=>r.correspondence),closure=new Set();
 for(const l of labels){let n=l.index;closure.add(n);while(n%2===0){n/=2;closure.add(n);}}
 const records=new Map([...closure].sort((a,b)=>a-b).map(n=>[n,rawRecord(n)])),doubling=[];
 for(const n of [...closure].sort((a,b)=>a-b))if(closure.has(2*n))doubling.push(verifyDoubling(n,records));
 const rows=labels.map((correspondence,i)=>{
  const r=records.get(correspondence.index),cyclic=correspondence.kind==='cyclic4';
  const I2=r.I2-(cyclic?records.get(1).I2:0),rho=r.rho-(cyclic?1:0);
  assert(rho===oddCertificate.rows[i].CM_return_multiplicity,'independent CM return count');
  return {correspondence,CM_return_multiplicity:rho,I2,formula_terms:{norm_degree:r.n,ordinary_Hecke_coefficient:r.I2,subtract_diagonal:cyclic?records.get(1).I2:0}};
 });
 assert(rows[0].I2===-80&&rows[1].I2===-40&&rows[2].I2===0,'T1/T2/T3');
 assert(rows.find(r=>r.correspondence.kind==='cyclic4').I2===80,'C4');
 const pairs=[],seen=new Set();
 for(const t of NONSQUARES)if(!seen.has(t)){const u=powmod(t,39);assert(u!==t&&NONSQUARES.includes(u),'wild pair distinct');seen.add(t);seen.add(u);pairs.push([t,u].sort((a,b)=>a-b));}
 assert(pairs.length===10,'ten coarse pairs');
 const total=labels.reduce((s,l)=>s+records.get(l.index).quaternions,0),noncm=labels.reduce((s,l)=>s+records.get(l.index).non_gaussian,0);
 assert(total===56616&&noncm===56460,'original 54-row norm counts');
 return {result:'R193',level:41,auxiliary_prime:47,precision:4,modulus:Q,
  tangent_parameters:{Z_minus4:'j-1728',cusps:'q41'},
  formula:'I2(T_n)=sum_nonGaussian(v2(c^2+d^2)*w)/4+20*rho(n)*v2(n)-120*rho(n)',
  formula_status:'geometric normalization is proved separately; enumeration alone is not a proof',
  normalization:{full_CM_marking_units:4,effective_wild_stabilizer:2,normalized_fine_length:'L/2',coarse_length:'L',
   canonical_self_per_point:-6,number_of_canonical_points:20,coarse_pairs:pairs,ordered_pair_contact_total:40,canonical_trace_self:-80},
  audit:{basis_rows:54,distinct_norm_degrees:records.size,total_quaternions_in_54_rows:total,non_gaussian_quaternions_in_54_rows:noncm,matrix_weight_checks:'every quaternion',doubling},
  norm_records:[...records.values()],rows};
}
const old=readJSON(option('--odd'));
if(sha(old.raw)!=='b2bdf1471fefc76dd6d05523af8929b66ef770b479534378c414b657d8420b54')throw Error('R190 input SHA');
const result=computeR193(old.value);
result.generating_source_sha256=sourceSHA;
result.input_sha256={R190_odd_certificate:sha(old.raw)};
const raw=Buffer.from(JSON.stringify(result,null,2)+'\n','utf8');
fs.writeFileSync(option('--output'),raw);
console.log(JSON.stringify({status:'PASS',rows:54,norm_degrees:result.audit.distinct_norm_degrees,quaternions:result.audit.total_quaternions_in_54_rows,non_gaussian:result.audit.non_gaussian_quaternions_in_54_rows,source_sha256:sourceSHA,certificate_sha256:sha(raw)}));
