#!/usr/bin/env node
/** Full inverse-Gram error of the actual complete physical waist row. */
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
function calculate(r){
if(r.kind!=='actual_final_complete_96_physical_waist_amplitude_Jacobi_row'||!r.complete||r.rows.length!==96||!r.whole_original_eta)throw Error('complete actual 96+mean row required');
const S=BigInt(r.exact_interval_denominator);
if(S!==2n**384n)throw Error('actual fixed denominator changed');
const widths=r.rows.map((x,i)=>{
 if(x.moving_index!==i+1||x.physical_frequency!==4*(i+1))throw Error('complete row indexing');
 return BigInt(x.exact_interval_numerator_at_scale[1])-BigInt(x.exact_interval_numerator_at_scale[0]);
});
const mw=BigInt(r.exact_mean_interval_numerator_at_scale[1])-BigInt(r.exact_mean_interval_numerator_at_scale[0]);
if(mw<0n||widths.some(x=>x<0n))throw Error('negative row interval width');
function isqrt(n){if(n<0n)throw Error('negative norm');if(n<2n)return n;let x=1n<<BigInt(Math.ceil(n.toString(2).length/2));for(;;){const y=(x+n/x)/2n;if(y>=x)return x;x=y;}}
const energy=mw*mw+2n*widths.reduce((a,x)=>a+x*x,0n);
let sq=isqrt(energy);if(sq*sq<energy)sq++;
const gcd=(a,b)=>{while(b){const t=a%b;a=b;b=t;}return a;};
const q=(n,d)=>{const g=gcd(n,d);return {n:n/g,d:d/g};};
const add=(a,b)=>q(a.n*b.d+b.n*a.d,a.d*b.d);
const rad=q(sq,2n*S),quant=q(14n,2n**52n),tail=q(1n,10n**42n),total=add(add(rad,quant),tail);
if(!(total.n*1000000000n<60n*total.d))throw Error('actual full row proposal error did not close');
const maxabs=(lo,hi)=>{lo=lo<0n?-lo:lo;hi=hi<0n?-hi:hi;return lo>hi?lo:hi;};
const all=[r.exact_mean_interval_numerator_at_scale,...r.rows.map(x=>x.exact_interval_numerator_at_scale)];
if(all.some(x=>maxabs(BigInt(x[0]),BigInt(x[1]))>=2n*S))throw Error('binary64 rounding magnitude hypothesis');
const upper=a=>{const scale=10n**48n,z=(a.n*scale+a.d-1n)/a.d,t=z.toString().padStart(49,'0');return t.slice(0,-48)+'.'+t.slice(-48);};
return {kind:'actual_complete_waist_midpoint_and_binary64_proposal_error',complete:true,executed:true,
 input_sha256:'c99e3f6c7fd4975ee8fd1de26fadad7f4e42c6c379a861830d6fa419046b052e',
 candidate_sha256:r.candidate_sha256,norm:'complete physical moving L2 dual, mean1 and nonmean inverse Gram2',
 complete_midpoint_head_error:upper(rad),per_entry_binary64_error_upper:'1/4503599627370496',
 quantization_norm_upper:upper(quant),unknown_high_tail_upper:'1e-42',
 full_true_physical_waist_row_error:upper(total),strict_final_upper:'0.00000006',
 exact_total_upper:total.n+'/'+total.d,whole_original_eta:true,current_centre_only:true,
 proposal_contract:'convert Fraction(L+U,2*S) once to binary64; verify exact round-trip error<=2^-52 for every entry',
 actual_finite_head_proposal_verified:false,
 gates:[{name:'all head row entries have absolute magnitude below2',passed:true},
 {name:'whole original physical row to any midpoint proposal with the stipulated rounding error',passed:true}]};
}
const args=process.argv.slice(2);
if(args.length!==4||args[0]!=='--row'||args[2]!=='--out')throw Error('usage: node this.mjs --row ACTUAL_ROW.json --out NEW_REPORT.json');
const raw=await readFile(args[1]);
const digest=createHash('sha256').update(raw).digest('hex');
if(digest!=='c99e3f6c7fd4975ee8fd1de26fadad7f4e42c6c379a861830d6fa419046b052e')throw Error('original complete row bytes changed');
const report=calculate(JSON.parse(raw.toString('utf8')));
report.producer_sha256=createHash('sha256').update(await readFile(fileURLToPath(import.meta.url))).digest('hex');
await writeFile(args[3],JSON.stringify(report,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({complete:report.complete,gates:report.gates.length,out:args[3]}));
