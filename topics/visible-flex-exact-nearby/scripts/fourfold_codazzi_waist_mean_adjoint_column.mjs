#!/usr/bin/env node
/** Actual full mean amplitude column; exact complete unknown-tail budget. */
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
function calculateMeanWaist(input){
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
class Q{
 constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error('zero denominator');if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
 static of(v){if(v instanceof Q)return v;if(typeof v==='string'&&v.includes('/')){const[n,d]=v.split('/');return new Q(n,d);}if(typeof v==='string'&&/[.eE]/.test(v)){let[s,e='0']=v.toLowerCase().split('e'),neg=s.startsWith('-');if(neg)s=s.slice(1);let[a,b='']=s.split('.');let n=BigInt((a||'0')+b),d=10n**BigInt(b.length),k=Number(e);if(k>=0)n*=10n**BigInt(k);else d*=10n**BigInt(-k);return new Q(neg?-n:n,d);}return new Q(v);}
 add(v){v=Q.of(v);return new Q(this.n*v.d+v.n*this.d,this.d*v.d);}neg(){return new Q(-this.n,this.d);}sub(v){return this.add(Q.of(v).neg());}mul(v){v=Q.of(v);return new Q(this.n*v.n,this.d*v.d);}div(v){v=Q.of(v);return new Q(this.n*v.d,this.d*v.n);}pow(n){if(n<0)return new Q(this.d,this.n).pow(-n);return new Q(this.n**BigInt(n),this.d**BigInt(n));}cmp(v){v=Q.of(v);const d=this.n*v.d-v.n*this.d;return d<0n?-1:d>0n?1:0;}abs(){return this.n<0n?this.neg():this;}str(){return this.n+'/'+this.d;}
}
const q=v=>Q.of(v),min=(a,b)=>a.cmp(b)<0?a:b,max=(a,b)=>a.cmp(b)>0?a:b;
const iv=(l,h=l)=>({l:q(l),h:q(h)}),ia=(a,b)=>iv(a.l.add(b.l),a.h.add(b.h)),ineg=a=>iv(a.h.neg(),a.l.neg());
function im(a,b){const v=[a.l.mul(b.l),a.l.mul(b.h),a.h.mul(b.l),a.h.mul(b.h)];return iv(v.reduce(min),v.reduce(max));}
const isc=(a,b)=>im(a,iv(b)),zero=()=>iv(0);
const pa=(a,b)=>{const c=new Map(a);for(const[n,v]of b)c.set(n,ia(c.get(n)||zero(),v));return c;};
const ps=(a,b)=>new Map([...a].map(([n,v])=>[n,isc(v,b)]));
const pm=(a,b)=>{const c=new Map();for(const[n,x]of a)for(const[k,y]of b)c.set(n+k,ia(c.get(n+k)||zero(),im(x,y)));return c;};
function dec(v,up=false,d=24){v=q(v);const s=10n**BigInt(d),n=v.n*s;let z=n/v.d,r=n%v.d;if(r&&((up&&n>0n)||(!up&&n<0n)))z+=up?1n:-1n;const sign=z<0n?'-':'';z=z<0n?-z:z;return sign+(z/s)+'.'+(z%s).toString().padStart(d,'0');}
const gates=[];function positive(name,x){x=q(x);if(x.cmp(0)<=0)throw Error(name+' failed');gates.push({name,passed:true,margin_lower:dec(x)});}
if(input.candidate_sha256!=='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'||!input.complete||input.chart_ball.radius!=='1/1000000')throw Error('actual entire waist input identity');
const alpha=q(input.exact_alpha),V=input.exact_full_V_coefficients.map(q),rho=q('1e-6');
const ml=q(input.exact_mean_absolute_lower),mh=q(input.exact_mean_absolute_upper);
const tau=iv(input.primary_phase_interval_outward_decimal[0],input.primary_phase_interval_outward_decimal[1]);
positive('retained complete mean gap',ml.sub(1));
positive('full primary phase below one',q(1).sub(tau.h));
const retained=8,N=4;let epsAmp=q(0),external=rho.div(2),P=new Map();
for(let j=2;j<=32;j++){
 if(j<=retained){const coefficient=isc(iv(mh.pow(-1),ml.pow(-1)),alpha.mul(V[j]).div(j).neg());
   P.set(j,isc(coefficient,q(1).div(2)));P.set(-j,isc(coefficient,q(-1).div(2)));
   epsAmp=epsAmp.add(alpha.mul(V[j].abs()).div(j).div(ml));
 }else external=external.add(alpha.mul(V[j].abs()).div(j));
}
external=external.div(ml);
positive('all remaining known and unknown phase paid',q('1e-6').sub(external));
let E=new Map([[0,iv(1)]]),power=new Map([[0,iv(1)]]);
for(let k=1;k<=N;k++){power=ps(pm(power,P),q(1).div(k));E=pa(E,power);}
const L=pa(P,new Map([[1,isc(tau,q(-1).div(2))],[-1,isc(tau,q(1).div(2))]]));
const H=pm(pa(new Map([[0,iv(1)]]),L),E);
function fact(n){let z=1n;for(let k=2;k<=n;k++)z*=BigInt(k);return z;}
const cache=new Map();let maxTail=q(0);
function bessel(order){
 let sign=1;if(order<0){order=-order;if(order%2)sign=-1;}
 if(!cache.has(order)){
  let ans=zero(),count=16;
  for(let n=0;n<count;n++){
   const p=2*n+order,den=new Q(2n**BigInt(p)*fact(n)*fact(n+order));
   const term=iv(tau.l.pow(p).div(den),tau.h.pow(p).div(den));ans=ia(ans,n%2?ineg(term):term);
  }
  const p=2*count+order,first=tau.h.pow(p).div(new Q(2n**BigInt(p)*fact(count)*fact(count+order)));
  const ratio=tau.h.pow(2).div(4*(count+1)*(count+order+1));
  if(ratio.cmp(1)>=0)throw Error('complete Bessel tail ratio');
  const tail=first.div(q(1).sub(ratio));maxTail=max(maxTail,tail);
  cache.set(order,ia(ans,iv(tail.neg(),tail)));
 }
 const x=cache.get(order);return sign<0?ineg(x):x;
}
let sum=zero();for(const[n,c]of H)sum=ia(sum,im(c,bessel(n+1)));
const tail=epsAmp.pow(N+1).div(new Q(fact(N+1))).mul(q(1).add(tau.h).add(epsAmp));
const outside=external.mul(q(2).add(tau.h).add(epsAmp)).add(external.pow(2).div(2));
const totalFee=tail.add(outside),full=ia(sum,iv(totalFee.neg(),totalFee));
const bm=im(isc(full,-2),iv(mh.pow(-2),ml.pow(-2)));
positive('actual full mean column strictly negative',bm.h.neg());
positive('mean-column lower coarse bound',bm.l.add('1.3'));
positive('mean-column upper coarse bound',q('-1.27').sub(bm.h));
positive('finite higher-phase exponential full remainder',q('1e-12').sub(tail));
positive('whole-ball final mean-column interval width',q('1e-4').sub(bm.h.sub(bm.l)));
return {
 kind:'actual_final_waist_complete_mean_column_for_adjoint_lift',complete:true,executed:true,
 candidate_sha256:input.candidate_sha256,whole_original_eta:true,
 whole_unknown_Wiener_ball:input.chart_ball,arithmetic:'exact BigInt rational intervals; no quadrature or floating Bessel',
 inputs:{waist_report:'notes/2026-11-13-R133-final-waist-amplitude-chart-rational.json',waist_proof_blob:'511c9ca83972003796c4c4fa456236f32095e3e3',retained_higher_phase_indices:'2..8',all_rest_paid:true},
 derivative_definition:'D A(v)[1], actual physical cosine-four amplitude; complete mean direction',
 derivative_interval_outward_decimal:[dec(bm.l,false),dec(bm.h,true)],
 proved_coarse_interval:['-13/10','-127/100'],
 phase_external_full_bound:dec(external,true),higher_phase_exponential_remainder:dec(tail,true,60),
 mean_integrand_total_error:dec(totalFee,true),Bessel_maximum_order:Math.max(...cache.keys()),
 Bessel_terms_per_series:16,complete_Bessel_tail_upper:dec(maxTail,true,70),
 gate_count:gates.length,gates,actual_nu_Schur_nonzero_proved:false,complete_BVP_inverse_proved:false
};
}
const args=process.argv.slice(2);
if(args.length!==4||args[0]!=='--input'||args[2]!=='--out')throw Error('usage: node this.mjs --input ORIGINAL_WAIST_REPORT.json --out NEW.json');
const bytes=await readFile(args[1]);
const inputSHA=createHash('sha256').update(bytes).digest('hex');
if(inputSHA!=='8066f501acc87d42e7d58f30377680aaa317be500471fa71bcceef336fc9357b')throw Error('the complete published waist report changed');
const result=calculateMeanWaist(JSON.parse(bytes.toString('utf8')));
result.original_waist_report_sha256=inputSHA;
result.producer_sha256=createHash('sha256').update(await readFile(fileURLToPath(import.meta.url))).digest('hex');
await writeFile(args[3],JSON.stringify(result,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({complete:result.complete,gate_count:result.gate_count,out:args[3]}));
