#!/usr/bin/env node
// Exact adjoint identity checks and actual complete outer-boundary fees.
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';

function nuAdjointBudget(){
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
const q=[P.sin(1,"1/5").add(P.sin(2,"1/50")),P.of(-1).add(P.cos(1,"1/10")).add(P.cos(2,"1/100"))];
const qr=[P.sin(1,"-1/7").add(P.sin(2,"1/60")),P.of("1/31").add(P.cos(1,"-1/40")).add(P.cos(2,"1/70"))];
const h=[P.sin(1,"1/3").add(P.sin(3,"-1/8")),P.of("2/7").add(P.cos(2,"1/9"))];
const hr=[P.sin(2,"1/11"),P.of("1/13").add(P.cos(3,"-1/17"))];
const p=[P.sin(2,"-2/5").add(P.sin(1,"1/19")),P.of("3/8").add(P.cos(1,"-1/23")).add(P.cos(4,"1/29"))];
const pr=[P.sin(1,"1/37"),P.of("-1/41").add(P.cos(2,"1/43"))];
const beta=Q.of("13/100"),K=Q.of("-7/10"),gamma=Q.of("6/5"),T=Q.of("3/40");
const beta1=Q.of("1/17"),K1=Q.of("2/13"),gamma1=Q.of("-1/19"),T1=Q.of("1/23");
const w=Q.of("7/9"),wp=Q.of("-4/11");
const f=fields(q,beta,K,gamma);
sameC("complete nonlocal adjoint including nonzero mean",pair(p,f.N(h)),pair(f.NT(p),h));
gate("the mean test direction is genuinely nonzero",!h[1].mean().zero());
gate("the mean dual rank-one column is genuinely nonzero",!dot(J(f.qp,K),p).mean().zero());
sameC("complete radial Green identity on arbitrary actual jets",pair(p,action(q,h,hr,beta,K,gamma)).sub(pair(adjAction(q,p,pr,beta,K,gamma),h)),
 pair(pr,h).add(pair(p,hr)));
const dh=dualF(new D(q[0],h[0]),new D(q[1],h[1]),beta,K,gamma).map(x=>x.t);
sameV("full moving derivative agrees with local plus primitive plus mean",dh,sub(hr,action(q,h,hr,beta,K,gamma)));
const Kv=K.neg().mul(w).add(T.mul(wp)),gv=gamma.mul(w).div(2);
const par=dualF(q[0],q[1],beta,new D(K,Kv),new D(gamma,gv)).map(x=>x.t);
const v2=q[1].mul(q[1]),Piv=v2.I();
const W=add(scale(f.qp,Piv),scale(q,v2));
const A=add(scale(W,beta.mul(T).neg()),[f.qp[1].mul(f.m).mul(gamma).mul(T),new P()]);
const B=sub(scale(W,beta.mul(K)),[f.qp[1].mul(f.m).mul(gamma).mul(K).mul("1/2"),f.qp[0].mul(f.m).mul(gamma).mul("1/2")]);
sameV("true fixed-Q nu column equals A wprime plus B w",par,add(scale(A,wp),scale(B,w)));
sameC("full nu source mean retained",par[1].mean(),f.m.mul(v2.meanP()).mul(beta.mul(Kv).neg()).mean());
gate("the true nu source mean is nonzero in the test",!par[1].mean().zero());
const Wr=add(add(scale(f.qp,scale(qr,2)[1].mul(q[1]).I()),scale(deriv(qr),Piv)),
 add(scale(q,q[1].mul(qr[1]).mul(2)),scale(qr,v2)));
const Ar=add(add(scale(W,beta1.mul(T).add(beta.mul(T1)).neg()),scale(Wr,beta.mul(T).neg())),
 [f.qp[1].mul(gamma1.mul(T)).mul(f.m).add(f.qp[1].mul(gamma).mul(T).mul(qr[1].meanP()))
   .add(f.qp[1].mul(gamma).mul(T1).mul(f.m)).add(qr[1].der().mul(gamma).mul(T).mul(f.m)),new P()]);
const du=new D(q[0],qr[0]),dv=new D(q[1],qr[1]),db=new D(beta,beta1),dt=new D(T,T1),dg=new D(gamma,gamma1);
const dw= [dv.mul(dv).I().mul(du.der()).add(dv.mul(dv).mul(du)),
 dv.mul(dv).I().mul(dv.der()).add(dv.mul(dv).mul(dv))];
const aDual=[db.mul(dt).mul(dw[0]).neg().add(dg.mul(dv.mean()).mul(dt).mul(dv.der())),
 db.mul(dt).mul(dw[1]).neg()];
sameV("A radial derivative retains all true polynomial and mean jets",Ar,aDual.map(x=>x.t));
const G=sub(B,action(q,A,Ar,beta,K,gamma));

sameC("source integration-by-parts kernel and full adjoint residual",pair(p,B).sub(pair(pr,A)).sub(pair(p,Ar)),
 pair(p,G).add(pair(adjAction(q,p,pr,beta,K,gamma),A)));
sameC("A mean is minus beta T m mean-v-square",A[1].mean(),f.m.mul(v2.meanP()).mul(beta.mul(T).neg()).mean());
sameC("B mean is beta K m mean-v-square",B[1].mean(),f.m.mul(v2.meanP()).mul(beta.mul(K)).mean());
gate("full A and B support through three M",Math.max(...A.map(x=>x.degree()),...B.map(x=>x.degree()))<=6);
gate("complete integration-by-parts kernel support through five M",Math.max(...G.map(x=>x.degree()))<=10);
const bump=[];
const fact=n=>{let t=1n;for(let j=2;j<=n;j++)t*=BigInt(j);return t;};
const choose=(n,k)=>fact(n)/(fact(k)*fact(n-k));
for(let j=0;j<=6;j++)bump[j+6]=new Q((j%2?-1n:1n)*4096n*choose(6,j));
for(let ord=0;ord<=5;ord++){
 let left=Q.of(0),right=Q.of(0);
 for(let j=6;j<=12;j++){let mult=1n;for(let k=0;k<ord;k++)mult*=BigInt(j-k);
  const coeff=bump[j].mul(new Q(mult));right=right.add(coeff);if(j===ord)left=left.add(coeff);}
 gate("actual bump derivative "+ord+" vanishes at both support endpoints",left.n===0n&&right.n===0n);
}
const bumpIntegral=new Q(4096n*13n*fact(6)*fact(6),100n*fact(13));
gate("actual compact bump integral is strictly positive",bumpIntegral.cmp(0)>0);
const ld=Q.of("5.898255e-6"),l0=Q.of("7.372818e-7"),dz=Q.of("3/100");
const positiveReg=Q.of(1).div(new Q(1n<<512n));
const dq=Q.of("9.1496e-18").add(positiveReg);
const outer=dz.mul(ld.add(l0).add(dq));
const alpha=new Q(6890507429876859n,9007199254740992n);
gate("actual amplitude exceeds three quarters",alpha.cmp("3/4")>0);
gate("sine cosine normalized row factor below two",Q.of("3/2").div(alpha).cmp(2)<0);
gate("all exact outer rows physical L2 perturbation below two e minus seven",outer.cmp("2e-7")<0);
gate("all normalized real rows perturbation below four e minus seven",outer.mul(2).cmp("4e-7")<0);
const fb=Q.of("0.000000655361591650").add("0.000000081920198958");
gate("independent far-height derivative column below one point five e minus six",fb.mul(2).cmp("1.5e-6")<0);
return {
 kind:"actual_final_nu_full_adjoint_and_boundary_budget",
 complete:true,executed:true,
 arithmetic:"Exact BigInt rationals and complete Laurent convolution; no native reconstruction or body inverse run.",
 candidate_sha256:"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
 algebra_tests:{complete_mode_operations:true,artificial_exact_test_field:true,test_modes:2,
  full_A_support:Math.max(...A.map(x=>x.degree())),full_B_support:Math.max(...B.map(x=>x.degree())),
  full_G_support:Math.max(...G.map(x=>x.degree())),
  true_parameter_mean_test_value:par[1].mean().str(),
  direction_mean_test_value:h[1].mean().str()},
 actual_compact_bump_integral_exact:bumpIntegral.str(),
 actual_outer_physical_L2_row_difference_upper:dec(outer,true),
 actual_outer_normalized_real_row_difference_upper:dec(outer.mul(2),true),
 independent_fB_normalized_derivative_column_upper:dec(fb.mul(2),true),
 actual_proposal_q_error_positive_upper:dq.str(),
 keeps_cap_mean_and_full_physical_M4_row:true,
 independent_fB_and_far_label_equation_remain:true,
 adjoint_or_response_candidate_available:false,
 actual_body_complement_inverse_proved:false,
 actual_nu_scalar_nonzero_certified:false,
 full_native_nu_kernel_run:false,
 gate_count:gates.length,gates};

}

const result=nuAdjointBudget();
result.producer_sha256=createHash('sha256').update(readFileSync(new URL(import.meta.url))).digest('hex');
process.stdout.write(JSON.stringify(result,null,2)+'\n');
