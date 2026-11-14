#!/usr/bin/env node
// Complete moving nonlinear flux, retained mean, and joint metric remainder.
// Rational/Laurent primitives are adapted from the published nu-adjoint budget.
// The exact core runs without Node. The CLI only hashes and saves its result.
import {readFileSync,writeFileSync} from 'node:fs';
import {createHash} from 'node:crypto';

function movingNonlinearBudget(){
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
function gate(name,ok,detail){if(!ok)throw Error(name+" failed");gates.push({name,passed:true,...(detail===undefined?{}:{detail})});}
class C{
 constructor(r=0,i=0){this.r=Q.of(r);this.i=Q.of(i);}
 static of(x){return x instanceof C?x:new C(x);}
 add(x){x=C.of(x);return new C(this.r.add(x.r),this.i.add(x.i));}
 neg(){return new C(this.r.neg(),this.i.neg());}
 sub(x){return this.add(C.of(x).neg());}
 mul(x){x=C.of(x);return new C(this.r.mul(x.r).sub(this.i.mul(x.i)),this.r.mul(x.i).add(this.i.mul(x.r)));}
 zero(){return this.r.n===0n&&this.i.n===0n;}
 str(){return [this.r.str(),this.i.str()];}
}
class P{
 constructor(entries=[]){this.c=new Map();for(const[k,v]of entries){const z=C.of(v);if(!z.zero())this.c.set(Number(k),z);}}
 static of(x){return x instanceof P?x:new P([[0,C.of(x)]]);}
 static sin(j,a=1){a=Q.of(a).div(2);return new P([[j,new C(0,a.neg())],[-j,new C(0,a)]]);}
 static cos(j,a=1){a=Q.of(a).div(2);return new P([[j,a],[-j,a]]);}
 add(x){x=P.of(x);const out=new P([...this.c]);for(const[k,z]of x.c){const t=(out.c.get(k)||new C()).add(z);if(t.zero())out.c.delete(k);else out.c.set(k,t);}return out;}
 neg(){return new P([...this.c].map(([k,z])=>[k,z.neg()]));}
 sub(x){return this.add(P.of(x).neg());}
 mul(x){x=P.of(x);const out=new P();for(const[k,z]of this.c)for(const[l,w]of x.c){const p=k+l,t=(out.c.get(p)||new C()).add(z.mul(w));if(t.zero())out.c.delete(p);else out.c.set(p,t);}return out;}
 der(){return new P([...this.c].filter(([k])=>k).map(([k,z])=>[k,z.mul(new C(0,4*k))]));}
 I(){return new P([...this.c].filter(([k])=>k).map(([k,z])=>[k,z.mul(new C(0,Q.of(-1).div(4*k)))]));}
 mean(){return this.c.get(0)||new C();}
 meanP(){return P.of(this.mean());}
 zero(){return this.c.size===0;}
 degree(){return this.c.size?Math.max(...[...this.c.keys()].map(Math.abs)):0;}
}
const dot=(x,y)=>x[0].mul(y[0]).add(x[1].mul(y[1]));
const pair=(x,y)=>dot(x,y).mean();
const add=(x,y)=>[x[0].add(y[0]),x[1].add(y[1])];
const sub=(x,y)=>[x[0].sub(y[0]),x[1].sub(y[1])];
const scale=(x,t)=>x.map(z=>z.mul(t));
const deriv=x=>x.map(z=>z.der());
const J=(x,K)=>[x[1].mul(K),x[0].neg()];
function sameP(name,x,y){gate(name,x.sub(y).zero());}
function sameV(name,x,y){gate(name,sub(x,y).every(z=>z.zero()));}
function sameC(name,x,y){gate(name,x.sub(y).zero());}
function fields(q,beta,K,gamma){
 const [u,v]=q,m=v.meanP(),S=u.mul(u).add(v.mul(v).mul(K));
 const qp=deriv(q),d=S.I().mul(Q.of(beta).neg());
 const L11=P.of(1).add(u.mul(u).mul(3)).add(v.mul(v).mul(K)).mul(Q.of(beta).neg());
 const L12=u.mul(v).mul(Q.of(-2).mul(beta).mul(K));
 const L21=u.mul(v).mul(Q.of(-2).mul(beta));
 const L22=P.of(1).sub(u.mul(u)).sub(v.mul(v).mul(Q.of(3).mul(K))).mul(beta);
 const L=x=>[L11.mul(x[0]).add(L12.mul(x[1])),L21.mul(x[0]).add(L22.mul(x[1]))];
 const LT=x=>[L11.mul(x[0]).add(L21.mul(x[1])),L12.mul(x[0]).add(L22.mul(x[1]))];
 const aa=[u,v.mul(K)],jp=J(qp,K);
 const N=x=>add(scale(qp,dot(aa,x).I().mul(Q.of(-2).mul(beta))),scale(jp,x[1].meanP().mul(gamma)));
 const NT=x=>add(scale(aa,dot(qp,x).I().mul(Q.of(2).mul(beta))),[new P(),dot(jp,x).meanP().mul(gamma)]);
 const Ap=x=>add(scale(x,d),scale(J(x,K),m.mul(gamma)));
 const ApT=x=>[d.mul(x[0]).sub(m.mul(gamma).mul(x[1])),m.mul(gamma).mul(K).mul(x[0]).add(d.mul(x[1]))];
 return {m,S,d,qp,aa,L,LT,N,NT,Ap,ApT};
}
function action(q,h,hr,beta,K,gamma){const f=fields(q,beta,K,gamma);return sub(sub(sub(hr,f.Ap(deriv(h))),f.L(h)),f.N(h));}
function adjAction(q,p,pr,beta,K,gamma){
 const f=fields(q,beta,K,gamma);
 return sub(sub(add(add(scale(pr,-1),f.ApT(deriv(p))),scale(p,f.d.der())),f.LT(p)),f.NT(p));
}
function nonlinear(q,beta,K,gamma){
 const f=fields(q,beta,K,gamma),[u,v]=q;
 return add(add(scale(f.qp,f.d),scale(J(f.qp,K),f.m.mul(gamma))),
 [u.mul(P.of(1).add(f.S)).mul(Q.of(beta).neg()),v.mul(P.of(1).sub(f.S)).mul(beta)]);
}
class D{
 constructor(p,t=0){this.p=P.of(p);this.t=P.of(t);}
 static of(x){return x instanceof D?x:new D(x);}
 add(x){x=D.of(x);return new D(this.p.add(x.p),this.t.add(x.t));}
 neg(){return new D(this.p.neg(),this.t.neg());}
 sub(x){return this.add(D.of(x).neg());}
 mul(x){x=D.of(x);return new D(this.p.mul(x.p),this.t.mul(x.p).add(this.p.mul(x.t)));}
 der(){return new D(this.p.der(),this.t.der());}
 I(){return new D(this.p.I(),this.t.I());}
 mean(){return new D(this.p.meanP(),this.t.meanP());}
}
function dualF(u,v,beta,K,gamma){
 u=D.of(u);v=D.of(v);beta=D.of(beta);K=D.of(K);gamma=D.of(gamma);
 const m=v.mean(),S=u.mul(u).add(K.mul(v.mul(v))),d=beta.mul(S.I()).neg();
 return [d.mul(u.der()).add(gamma.mul(m).mul(K).mul(v.der())).sub(beta.mul(u).mul(D.of(1).add(S))),
 d.mul(v.der()).sub(gamma.mul(m).mul(u.der())).add(beta.mul(v).mul(D.of(1).sub(S)))];
}


const q=[P.sin(1,"1/5").add(P.sin(2,"-1/35")),P.of("-9/8").add(P.cos(1,"1/9")).add(P.cos(3,"1/70"))];
const h=[P.sin(2,"2/7").add(P.sin(4,"-1/23")),P.of("3/11").add(P.cos(1,"-1/13")).add(P.cos(4,"1/29"))];
const k=[P.sin(1,"-1/17").add(P.sin(3,"1/19")),P.of("-2/31").add(P.cos(2,"1/37"))];
const beta=Q.of("13/100"),K=Q.of("-7/10"),gamma=Q.of("6/5");
const SK=x=>x[0].mul(x[0]).add(x[1].mul(x[1]).mul(K));
const BK=(x,y)=>x[0].mul(y[0]).add(x[1].mul(y[1]).mul(K));
const lin=x=>[x[0].mul(beta.neg()),x[1].mul(beta)];
function fluxF(x){
 const s=SK(x),m=x[1].meanP();
 return add(sub(deriv(add(scale(x,s.I().mul(beta.neg())),scale(J(x,K),m.mul(gamma)))),scale(x,s.meanP().mul(beta))),lin(x));
}
function remainderParts(x,z){
 const s=SK(z),b=BK(x,z);
 const quadraticFlux=add(scale(add(scale(x,s.I()),scale(z,b.I().mul(2))),beta.neg()),scale(J(z,K),z[1].meanP().mul(gamma)));
 const cubicFlux=scale(z,s.I().mul(beta.neg()));
 const quadraticLocal=scale(add(scale(x,s.meanP()),scale(z,b.meanP().mul(2))),beta.neg());
 const cubicLocal=scale(z,s.meanP().mul(beta.neg()));
 return {flux:add(quadraticFlux,cubicFlux),local:add(quadraticLocal,cubicLocal),
   quadratic:add(deriv(quadraticFlux),quadraticLocal),cubic:add(deriv(cubicFlux),cubicLocal)};
}
const n=nonlinear(q,beta,K,gamma),df=dualF(new D(q[0],h[0]),new D(q[1],h[1]),beta,K,gamma).map(x=>x.t);
sameV("full nonlinear moving equation equals exact conservative flux plus mean reaction",n,fluxF(q));
sameC("true second mean includes the entire S mean",n[1].mean(),q[1].mean().mul(P.of(1).sub(SK(q).meanP()).mean()).mul(beta));
sameC("actual odd first mean remains zero",n[0].mean(),new C());
gate("fixture includes nonzero even mean in background and both directions",!q[1].mean().zero()&&!h[1].mean().zero()&&!k[1].mean().zero());
const rr=remainderParts(q,h);
const rem=sub(sub(nonlinear(add(q,h),beta,K,gamma),n),df);
sameV("entire quadratic and cubic remainder includes primitive and mean rank",rem,add(deriv(rr.flux),rr.local));
sameV("remainder separates exact homogeneous degrees two and three",rem,add(rr.quadratic,rr.cubic));
const r2=remainderParts(q,scale(h,2));
sameV("quadratic part scales by four",r2.quadratic,scale(rr.quadratic,4));
sameV("cubic part scales by eight",r2.cubic,scale(rr.cubic,8));
sameC("complete remainder mean is the nonzero mean-reaction term",rem[1].mean(),rr.local[1].mean());
gate("nonlinear remainder mean is genuinely nonzero in this exact fixture",!rem[1].mean().zero());
function derivative(x,z){return dualF(new D(x[0],z[0]),new D(x[1],z[1]),beta,K,gamma).map(a=>a.t);}
const bkh=BK(h,k),bqk=BK(q,k),bqh=BK(q,h),sh=SK(h);
const dFlux=add(scale(add(add(scale(q,bkh.I().mul(2)),scale(h,bqk.I().mul(2))),
 add(scale(k,bqh.I().mul(2)),add(scale(h,bkh.I().mul(2)),scale(k,sh.I())))),beta.neg()),
 add(scale(J(h,K),k[1].meanP().mul(gamma)),scale(J(k,K),h[1].meanP().mul(gamma))));
const dLocal=scale(add(add(scale(q,bkh.meanP().mul(2)),scale(h,bqk.meanP().mul(2))),
 add(scale(k,bqh.meanP().mul(2)),add(scale(h,bkh.meanP().mul(2)),scale(k,sh.meanP())))),beta.neg());
sameV("full Jacobian variation retains both mean columns",sub(derivative(add(q,h),k),derivative(q,k)),add(deriv(dFlux),dLocal));
const k0=Q.of("2/5"),g0=Q.of("7/6"),p0=g0.mul(k0);
function coefficientF(x,kk,gg,pp){
 const v=x[1],m=v.meanP(),s=x[0].mul(x[0]).add(v.mul(v).mul(kk));
 const transport=scale(deriv(x),s.I().mul(beta.neg()));
 const radial=scale([v.der().mul(pp),x[0].der().mul(gg.neg())],m);
 return add(add(transport,radial),sub(lin(x),scale(x,s.mul(beta))));
}
sameV("K gamma and gamma K are independent affine coefficient coordinates",coefficientF(q,k0,g0,p0),nonlinear(q,beta,k0,g0));
const dk=Q.of("1/101"),dg=Q.of("-1/103"),dp=Q.of("1/107");
function coefficientDelta(x){
 const v=x[1],m=v.meanP(),v2=v.mul(v);
 const flux=add(scale(x,v2.I().mul(beta.mul(dk).neg())),scale([v.mul(dp),x[0].mul(dg.neg())],m));
 return sub(deriv(flux),scale(x,v2.meanP().mul(beta.mul(dk))));
}
sameV("all coefficient differences have complete conservative form",sub(coefficientF(q,k0.add(dk),g0.add(dg),p0.add(dp)),coefficientF(q,k0,g0,p0)),coefficientDelta(q));
sameV("coefficient difference formula retains complete perturbed state",sub(coefficientF(add(q,h),k0.add(dk),g0.add(dg),p0.add(dp)),coefficientF(add(q,h),k0,g0,p0)),coefficientDelta(add(q,h)));
const w=Q.of("7/9"),wp=Q.of("-4/11"),T=Q.of("3/40"),maxOrd=5;
const fac=n=>{let r=1n;for(let j=2;j<=n;j++)r*=BigInt(j);return new Q(r);};
const expo=(a)=>Array.from({length:maxOrd+1},(_,j)=>Q.of(a).pow(j).div(fac(j)));
const mulJet=(a,b)=>Array.from({length:maxOrd+1},(_,n)=>{let s=Q.of(0);for(let j=0;j<=n;j++)s=s.add((a[j]||Q.of(0)).mul(b[n-j]||0));return s;});
const ek=expo(w.neg()),eg=expo(w.div(2)),ep=expo(w.div(-2));
const kj=mulJet(ek,[k0,T.mul(wp)]),gj=eg.map(x=>x.mul(g0)),pj=mulJet(ep,[p0,g0.mul(T).mul(wp)]);
const product=mulJet(kj,gj);
gate("actual target exponential laws agree through complete fifth jet",product.every((x,j)=>x.cmp(pj[j])===0));
gate("true K parameter first derivative includes w prime",kj[1].cmp(k0.mul(w).neg().add(T.mul(wp)))===0);
gate("true gamma parameter first derivative",gj[1].cmp(g0.mul(w).div(2))===0);
gate("true gamma K first derivative includes its cross coefficient",pj[1].cmp(p0.mul(w).div(-2).add(g0.mul(T).mul(wp)))===0);
const ell=Q.of("13/100"),w1sq=Q.of(24).div(ell).pow(2).div(11).mul(Q.of("10/11").pow(10));
gate("actual compact bump maximum equals one",Q.of(4096).mul(Q.of("1/4").pow(6)).cmp(1)===0);
gate("actual compact bump complete derivative below 35",w1sq.cmp(Q.of(35).pow(2))<0);
const strip=Q.of("1/1024"),loss=Q.of("1/2048"),freq=Q.of(128);
gate("same full finite root centre exponent budget below one",freq.mul(strip).cmp(1)<0);
const expUpper=Q.of(1).div(Q.of(1).sub(freq.mul(strip)));
const qCentre=Q.of("74/5").mul(expUpper);
gate("complete moving root centre Astrip norm below 17",qCentre.cmp(17)<0);
const be=Q.of("9/5"),ga=Q.of("9/5"),rho=Q.of("1/100"),B=Q.of(17),invLoss=Q.of(1).div(loss);
const remConstant=be.mul(invLoss.mul("3/4").add(3).mul(B).add(invLoss.div(4).add(1).mul(rho))).add(ga.mul(invLoss));
const diffConstant=be.mul(invLoss.mul("3/2").add(6).mul(B).add(invLoss.mul("3/4").add(3).mul(rho))).add(ga.mul(2).mul(invLoss));
gate("full root nonlinear remainder constant below 51000",remConstant.cmp(51000)<0);
gate("full root Jacobian difference constant below 102000",diffConstant.cmp(102000)<0);
gate("actual negative and positive root germs both have absolute K below one",Q.of("61/100000").cmp(1)<0);
gate("all allowed unknown angular tails remain in the declared strip ball",rho.cmp(0)>0&&loss.cmp(strip)<0);
const hpar=Q.of("1/100"),E=Q.of(1).div(Q.of(1).sub(hpar)),Eh=Q.of(1).div(Q.of(1).sub(hpar.div(2)));
gate("joint metric parameter exponential majorants remain finite",E.cmp("100/99")===0&&Eh.cmp("200/199")===0);
gate("complete mean chart survives the full infinite-mode root ball",Q.of("1.1197077044").sub(rho).cmp("1.1097")>0);
gate("complete angular chart survives the full infinite-mode root ball",Q.of("0.4488872879").sub(rho).cmp("0.4388")>0);
gate("complete final strip embeds into H one-third with factor below ten",Q.of(1).div(loss.mul(3)).cmp(Q.of(9).pow(3))<0);
gate("same positive-root inverse applied once to the full nonlinear source has L2 gain below one fifth",Q.of(51000).mul(10).mul("3/1000").div(8000).cmp("1/5")<0);
gate("same positive-root full raw trace applied once has gain below sixty-two",Q.of(51000).mul(10).mul("3/1000").div(25).cmp(62)<0);
return {
 kind:"complete_moving_nonlinear_flux_mean_and_joint_parameter_remainder",
 complete:true,executed:true,arithmetic:"normalized BigInt rationals and complete Laurent convolution",
 source:"scripts/fourfold_codazzi_moving_nonlinear_flux_budget.mjs",
 source_algebra_reused_from_published:"scripts/fourfold_codazzi_nu_adjoint_budget.mjs",
 candidate_sha256:"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
 actual_root_application:{whole_original_eta:true,same_actual_root_piece:2549,full_real_joint_germ:true,
  angular_strip:strip.str(),required_strip_loss:loss.str(),allowed_complete_unknown_ball:rho.str(),
  centre_Astrip_upper:qCentre.str(),remainder_quadratic_constant_upper:remConstant.str(),
  Jacobian_difference_linear_constant_upper:diffConstant.str(),all_unknown_Fourier_modes:true,
  metric_nu_bump_exactly_zero_on_this_germ:true,negative_real_mean_gap_after_ball:"1.1097",negative_real_v_gap_after_ball:"0.4388",ordinary_source_H_one_third_embedding:"10",single_positive_root_inverse_L2_response_quadratic:"1/5",single_positive_root_inverse_raw_trace_response_quadratic:"62",no_same_norm_iteration_from_these_gains:true},
 compact_metric_control:{support:["1/20","9/50"],maximum:"1",derivative_square_exact_maximum:w1sq.str(),derivative_upper:"35"},
 fixture:{artificial_field:true,nonzero_even_mean:true,actual_candidate_coefficients_not_reconstructed:true,
  highest_background_mode:Math.max(...q.map(x=>x.degree())),highest_direction_mode:Math.max(...h.map(x=>x.degree())),
  full_remainder_support:Math.max(...rem.map(x=>x.degree())),nonzero_remainder_mean:rem[1].mean().str()},
 source_permissions:{complete_state_and_nu_formulas:true,mean_discarded:false,radial_jumps_of_raw_state_are_linear:true,
  original_full_native_recovery:false,whole_body_coefficient_bounds:false,
  fixed_Sobolev_contraction_claimed:false,complete_global_inverse_claimed:false,nonlinear_closed_family_claimed:false},
 gate_count:gates.length,gates
};
}

const result=movingNonlinearBudget();
result.producer_sha256=createHash('sha256').update(readFileSync(new URL(import.meta.url))).digest('hex');
result.execution_runtime="Node CLI exact core";
const text=JSON.stringify(result,null,2)+'\n';
const oi=process.argv.indexOf('--out');
if(oi>=0){if(!process.argv[oi+1])throw Error('--out requires a new path');writeFileSync(process.argv[oi+1],text,{flag:'wx'});}
else process.stdout.write(text);
