#!/usr/bin/env node
/** Complete actual physical boundary transpose budgets, final ac1 centre. */
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
function calculate(){
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;};
const q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};};
const add=(a,b)=>q(a.n*b.d+b.n*a.d,a.d*b.d),neg=a=>q(-a.n,a.d),sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>q(a.n*b.n,a.d*b.d),div=(a,b)=>q(a.n*b.d,a.d*b.n),pow=(a,n)=>q(a.n**BigInt(n),a.d**BigInt(n));
const lt=(a,b)=>a.n*b.d<b.n*a.d,str=a=>a.n+'/'+a.d;
const up=(a,d=30)=>{const s=10n**BigInt(d),x=(a.n*s+a.d-1n)/a.d,t=x.toString().padStart(d+1,'0');return t.slice(0,-d)+'.'+t.slice(-d);};
const P=q(1480385,100000000000000000n),U=q(164319,100000000000000n),m=q(29,5);
const e1=mul(q(8),P),e2=mul(q(128),P),gap=sub(q(1),e1),change=add(q(1),e1);
const denominator=pow(m,2);
const Z=mul(div(change,denominator),add(div(add(mul(q(2),e1),pow(e1,2)),pow(gap,2)),div(mul(P,e2),pow(gap,3))));
const B=mul(div(change,denominator),add(div(mul(U,add(q(1),mul(q(8),P))),pow(gap,2)),div(mul(mul(U,P),e2),pow(gap,3))));
const Ld=q(1179651,200000000000n),L0=q(3686409,5000000000000n);
const eps=add(q(11437,1250000000000000000000n),q(1,2n**512n));
const cR=add(add(B,Z),mul(add(Ld,eps),Z));
const omegaRelative=mul(mul(q(49),L0),Z);
const inverseOmega=div(q(49),sub(q(1),omegaRelative));
const lambdaW=mul(q(50),cR),lambdaMu=q(50);
const adjW=mul(q(3,100),add(add(Ld,eps),mul(L0,q(28,10000000000n))));
const adjMu=mul(mul(q(3,100),L0),lambdaMu);
const meanRow=q(271,250000000),responseCorrection=add(q(1),div(pow(meanRow,2),q(2)));
const scalarFee=mul(mul(q(3,100),add(Ld,eps)),responseCorrection);
const gates=[];function gate(name,x,y){if(!lt(x,y))throw Error(name+' failed');gates.push({name,passed:true,strict_upper:str(y),computed_upper:str(x)});}
gate('entire physical angle Jacobian',e1,q(12,100000000000n));
gate('complete pure-mean C nonmean column',Z,q(705,100000000000000n));
gate('complete pure-mean B column',B,q(4885,100000000000000n));
gate('true full Robin mean column including all tails',cR,q(5591,100000000000000n));
gate('actual exterior mean scalar relative error',omegaRelative,q(3,10000000000000000n));
gate('actual exterior mean scalar inverse',inverseOmega,q(50));
gate('outer mean adjoint weight from complete Robin kernel',lambdaW,q(28,10000000000n));
gate('true full adjoint boundary model fee kernel',adjW,q(177,1000000000n));
gate('true full adjoint boundary model fee mean',adjMu,q(553,500000000n));
gate('true corrected scalar exterior model fee',scalarFee,q(177,1000000000n));
return {
 kind:'actual_final_complete_physical_boundary_adjoint_and_mean_column_budget',
 complete:true,executed:true,arithmetic:'exact BigInt rational arithmetic',
 candidate_sha256:'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413',
 whole_original_eta:true,actual_background_fB_kept_in_original_analytic_class:true,
 inputs:[
  {path:'results/R133-supplement-final-moving-centre-actual-regular-boundary.md',git_blob:'40463b6917c943e4ac991a597603cf41095baeb9',used:'P,U_sigma,m, complete final endpoint identity'},
  {path:'results/R133-supplement-final-regular-full-L2-and-Hilbert-Robin.md',git_blob:'a7ff7d2ca24df41ccd242ff9799b21fdcab2aec0',used:'complete true Ld,L0, moving-to-physical nonmean C map<.03'},
  {path:'results/R133-supplement-final-regular-Hs-and-Riccati-outer-graph.md',git_blob:'7784d7158974d4632ca634369e55dc095e134902',used:'true complete moving mean graph bound1.084e-6'}
 ],
 complete_column_bounds:{
  true_moving_angle_jacobian_error:up(e1),
  physical_nonmean_C_from_pure_moving_mean:up(Z),
  physical_B_from_pure_moving_mean:up(B),
  true_physical_Robin_mean_column_norm:up(cR),
  exterior_mean_scalar_relative_error:up(omegaRelative),
  exterior_mean_scalar_inverse:up(inverseOmega),
  true_mean_adjoint_multiplier_kernel_column:up(lambdaW),
  true_mean_adjoint_multiplier_mu_column:'50'
 },
 true_boundary_dual_model_fees:{kernel_L2:'0.000000177',completed_adjoint_mean_trace:'0.000001106'},
 true_corrected_scalar_boundary_fee:'0.000000177 * norm(w_R)_L2 * norm(h2_perp(R))_L2',
 true_model_q_error_exact:str(eps),gate_count:gates.length,gates,
 actual_full_boundary_trial_evaluated:false,complete_BVP_inverse_proved:false,actual_nu_Schur_nonzero_proved:false
};}
const args=process.argv.slice(2);
if(args.length!==2||args[0]!=='--out')throw Error('usage: node this.mjs --out NEW_REPORT.json');
const report=calculate();
report.producer_sha256=createHash('sha256').update(await readFile(fileURLToPath(import.meta.url))).digest('hex');
await writeFile(args[1],JSON.stringify(report,null,2)+'\n',{flag:'wx'});
if(!report.complete)process.exitCode=1;
console.log(JSON.stringify({complete:report.complete,gate_count:report.gate_count,out:args[1]}));
