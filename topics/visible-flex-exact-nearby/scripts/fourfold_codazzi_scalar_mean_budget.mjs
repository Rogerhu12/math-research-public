#!/usr/bin/env node
// Exact full-mean identities and actual final-centre endpoint prefactors.
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';

function fullMeanBudget(){
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
class Q{constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const z=gcd(n,d);this.n=n/z;this.d=d/z;}
 static of(v){if(v instanceof Q)return v;if(typeof v==="string"){if(v.includes("/")){let[n,d]=v.split("/");return new Q(n,d);}if(/[eE.]/.test(v)){let[s,e="0"]=v.toLowerCase().split("e");let neg=s.startsWith("-");if(neg)s=s.slice(1);let[a,b=""]=s.split(".");let n=BigInt((a||"0")+b),d=10n**BigInt(b.length);let k=Number(e);if(k>=0)n*=10n**BigInt(k);else d*=10n**BigInt(-k);return new Q(neg?-n:n,d);}return new Q(v);}return new Q(v);}
 add(v){v=Q.of(v);return new Q(this.n*v.d+v.n*this.d,this.d*v.d);}
 neg(){return new Q(-this.n,this.d);}
 sub(v){return this.add(Q.of(v).neg());}
 mul(v){v=Q.of(v);return new Q(this.n*v.n,this.d*v.d);}
 div(v){v=Q.of(v);return new Q(this.n*v.d,this.d*v.n);}
 abs(){return this.n<0n?this.neg():this;}
 pow(k){if(k<0)return new Q(this.d,this.n).pow(-k);return new Q(this.n**BigInt(k),this.d**BigInt(k));}
 cmp(v){v=Q.of(v);let x=this.n*v.d-v.n*this.d;return x<0n?-1:x>0n?1:0;}
 str(){return this.d===1n?""+this.n:this.n+"/"+this.d;}
}
function dyadic(x){if(!Number.isFinite(x))throw Error("nonfinite input");const a=new ArrayBuffer(8),v=new DataView(a);v.setFloat64(0,x,false);const z=v.getBigUint64(0,false);const sign=(z>>63n)?-1n:1n;const e=Number((z>>52n)&2047n);let n=z&((1n<<52n)-1n);let p=e?e-1023-52:-1074;if(e)n+=1n<<52n;if(p>=0)return new Q(sign*(n<<BigInt(p)));return new Q(sign*n,1n<<BigInt(-p));}
function dec(v,up=false,digits=18){v=Q.of(v);let scale=10n**BigInt(digits),n=v.n*scale,q=n/v.d,r=n%v.d;if(r && ((up&&n>0n)||(!up&&n<0n)))q+=up?1n:-1n;const sign=q<0n?"-":"";q=q<0n?-q:q;return sign+(q/scale)+"."+(q%scale).toString().padStart(digits,"0");}

const gates=[];
const eq=(name,a,b)=>{a=Q.of(a);b=Q.of(b);if(a.cmp(b)!==0)throw Error(name+" failed");gates.push({name,passed:true});};
const gt=(name,a,b)=>{a=Q.of(a);b=Q.of(b);if(a.cmp(b)<=0)throw Error(name+" failed");gates.push({name,passed:true,strict_margin_lower:dec(a.sub(b),false,40)});};
const a=Q.of("11/10"),beta=Q.of("13/100"),K=Q.of("-7/10"),m=Q.of(-1),mr=Q.of("1/31");
const U2=Q.of("101/5000"),V2=Q.of("101/20000");
const Smean=U2.add(K.mul(m.pow(2).add(V2)));
const Var=U2.add(K.mul(V2)),c=beta.mul(2).mul(Var);
const R0=mr.sub(beta.mul(m).mul(Q.of(1).sub(Smean)));
const n=a.pow(2).div(m.pow(2)),tau=a.pow(2).mul(-2).div(m.pow(3));
const nr=n.mul(beta.mul(2).sub(mr.mul(2).div(m)));
eq("nonlinear transformed mean residual is exactly tau times R0",nr.sub(c.mul(n)).sub(beta.mul(2).mul(K).mul(a.pow(2))),tau.mul(R0));
gt("test mean transformation is positive",tau,0);
gt("test residual is genuinely nonzero",R0.abs(),0);
const z=Q.of("2/7"),zr=Q.of("1/13"),Uh=Q.of("1/30"),Vh=Q.of("1/1800");
const dVar=Uh.add(K.mul(Vh)).mul(2);
const FmDerivative=beta.mul(z).mul(Q.of(1).sub(Smean)).sub(beta.mul(m).mul(2).mul(Uh.add(K.mul(m.mul(z).add(Vh)))));
const f0=zr.sub(FmDerivative);
const y=tau.mul(z),yr=tau.mul(zr).add(tau.mul(beta.mul(2).sub(mr.mul(3).div(m))).mul(z));
const ct=c.sub(R0.mul(3).div(m));
eq("full mean linearization keeps the exact residual-sensitive coefficient",yr.sub(ct.mul(y)).sub(beta.mul(2).mul(n).mul(dVar)),tau.mul(f0));
const cm=beta.mul(Q.of(1).sub(Smean).sub(K.mul(m.pow(2)).mul(2)));
eq("mean Green diagonal identity on every smooth piece",ct.sub(cm),beta.mul(2).sub(mr.mul(3).div(m)));
const s=Q.of("-6/5"),sr=beta.mul(s).mul(Q.of(1).sub(K.mul(s.pow(2))));
const nref=a.pow(2).div(s.pow(2)),nrefp=nref.mul(beta.mul(2).sub(sr.mul(2).div(s)));
eq("true rotational nref derivative",nrefp,beta.mul(2).mul(K).mul(a.pow(2)));
const rho=Q.of(1).sub(nref),ap=a.mul(beta),E=ap.pow(2).div(rho),T=beta.div(E.mul(2));
const w=Q.of("7/9"),wp=Q.of("-4/11"),Kn=K.neg().mul(w).add(T.mul(wp));
eq("compact reference parameter derivative eliminates the entire large radial source",nrefp.neg().mul(w).add(rho.mul(wp)),beta.mul(2).mul(a.pow(2)).mul(Kn));
const meanParam=beta.mul(m).mul(Kn).mul(m.pow(2).add(V2)).neg();
eq("complete transformed nu mean source",tau.mul(meanParam),beta.mul(2).mul(Kn).mul(n.mul(V2).add(a.pow(2))));
const eta=Q.of("2/9"),yw=y.sub(rho.mul(w).mul(eta));
const ywr=yr.add(tau.mul(meanParam).mul(eta)).sub(beta.mul(2).mul(a.pow(2)).mul(Kn).mul(eta));
const remaining=ct.mul(rho).mul(w).add(beta.mul(2).mul(n).mul(V2).mul(Kn));
eq("reference-subtracted nu mean retains nonmean and residual terms",ywr.sub(ct.mul(yw)).sub(beta.mul(2).mul(n).mul(dVar)).sub(tau.mul(f0)),remaining.mul(eta));
const alpha=new Q(6890507429876859n,9007199254740992n),V0=m.sub(s).div(alpha),V0r=mr.sub(sr).div(alpha);
eq("cancelled exact normalized mean residual",R0,alpha.mul(V0r).sub(beta.mul(alpha).mul(V0).mul(Q.of(1).sub(K.mul(m.pow(2).add(m.mul(s)).add(s.pow(2)))))).add(beta.mul(m).mul(Var)));
const Delta=E.sub(ap.pow(2)),sigma=s.neg().mul(ap.pow(2)).div(Delta.mul(2));
eq("normalized n minus nref explicit nu column",tau.mul(sigma).sub(rho),rho.mul(s.div(m).pow(3).sub(1)));
const ml=Q.of(-1),mu=Q.of("-9/10"),zl=Q.of("3/10"),zu=Q.of("2/5");
const tl=a.pow(2).mul(-2).div(ml.pow(3)),tu=a.pow(2).mul(-2).div(mu.pow(3)),rt=tu.div(tl),jump=zu.sub(zl);
eq("exact multiplicative mean interface and additive physical jump",tu.mul(zu),rt.mul(tl.mul(zl)).add(tu.mul(jump)));
const shift=rho.mul(w).mul(eta);
eq("reference-subtracted transformed nu interface is not deleted",tu.mul(zu).sub(shift),rt.mul(tl.mul(zl).sub(shift)).add(rt.sub(1).mul(shift)).add(tu.mul(jump)));
eq("exact nonlinear n jump",a.pow(2).div(mu.pow(2)).sub(a.pow(2).div(ml.pow(2))),a.pow(2).mul(mu.sub(ml)).mul(mu.add(ml)).neg().div(mu.pow(2).mul(ml.pow(2))));
eq("backward Green jump factor is actual mean ratio cubed",tl.div(tu),mu.div(ml).pow(3));
gt("all interface conversion factors are positive",rt,0);
const a0lo=Q.of("1.06873282"),m0hi=Q.of("1.07"),aRhi=Q.of("7e-6"),mRlo=Q.of("5.8");
gt("published whole-waist mean upper is below the chosen bound",m0hi,"1.068733840999993869");
const base=aRhi.pow(2).div(a0lo.pow(2)).mul(m0hi.pow(3));
const zRpref=base.div(mRlo.pow(3)),C0pref=base.div(mRlo);
const L0=Q.of("7.372818e-7"),L0B=Q.of("8.1920198958e-8");
const capZ=C0pref.mul(L0),capB=C0pref.mul(L0B);
gt("actual waist a0 exceeds one",a0lo,1);
gt("actual endpoint mean gap exceeds five",mRlo,5);
gt("raw outer mean to waist prefactor below three e minus thirteen","3e-13",zRpref);
gt("physical outer C mean to waist prefactor below one e minus eleven","1e-11",C0pref);
gt("actual nonlinear cap mean Z-column prefactor below seven e minus eighteen","7e-18",capZ);
gt("independent far-height mean column prefactor below eight e minus nineteen","8e-19",capB);
return {
 kind:"actual_final_scalar_mean_green_and_residual_sensitive_nu_cancellation",
 complete:true,executed:true,arithmetic:"Exact BigInt rational identities and existing actual endpoint constants; no full native body propagation.",
 candidate_sha256:"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
 actual_full_radial_mean_integration_performed:false,
 actual_mean_jump_log_sum_computed:false,
 actual_body_complement_inverse_proved:false,
 actual_nu_scalar_nonzero_certified:false,
 all_even_mean_and_independent_outer_inputs_retained:true,
 artificial_scalar_jet_test:{actual_candidate_native:false,mean_residual:R0.str(),tau:tau.str(),reference_n:nref.str()},
 endpoint_bounds:{waist_radius_lower:a0lo.str(),waist_mean_abs_upper:m0hi.str(),R_radius_upper:aRhi.str(),R_mean_abs_lower:mRlo.str()},
 endpoint_prefactors_must_multiply_exp_of_actual_diagonal_and_jump_budget:{
  raw_outer_z_to_waist_z:dec(zRpref,true,40),
  physical_outer_delta_Cmean_to_waist_z:dec(C0pref,true,40),
  cap_DZ_mean_to_waist_z:dec(capZ,true,40),
  independent_fB_dotH2_mean_to_waist_z:dec(capB,true,40)},
 unknown_remaining_factor:"exp(integral(max(0,-ctilde)) + 3*sum(abs(exact_mean_jump)/actual_two_sided_mean_gap)); full original radial span",
 gate_count:gates.length,gates};

}

const result=fullMeanBudget();
result.producer_sha256=createHash('sha256').update(readFileSync(new URL(import.meta.url))).digest('hex');
process.stdout.write(JSON.stringify(result,null,2)+'\n');
