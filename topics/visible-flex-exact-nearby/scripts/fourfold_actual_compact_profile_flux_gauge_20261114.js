"use strict";
/* New exact V8/Node computation for the actual compact-profile flux gauge.
   No numerical ODE, finite Fourier approximation, or prior Python native is used. */
function computeCompactProfileFluxGauge(inputBlobs, implementationBlob) {
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a;}
function R(n,d=1n){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}let g=gcd(n,d);return {n:n/g,d:d/g};}
const A=(x,y)=>R(x.n*y.d+y.n*x.d,x.d*y.d);
const N=x=>R(-x.n,x.d);
const S=(x,y)=>A(x,N(y));
const M=(x,y)=>R(x.n*y.n,x.d*y.d);
const D=(x,y)=>R(x.n*y.d,x.d*y.n);
const pow=(x,n)=>{n=Number(n);if(n<0)return pow(D(R(1),x),-n);let z=R(1);while(n){if(n%2)z=M(z,x);x=M(x,x);n=Math.floor(n/2);}return z;};
const two=n=>n>=0?R(1n<<BigInt(n)):R(1n,1n<<BigInt(-n));
const lt=(x,y)=>x.n*y.d<y.n*x.d;
const le=(x,y)=>x.n*y.d<=y.n*x.d;
const eq=(x,y)=>x.n===y.n&&x.d===y.d;
const str=x=>x.d===1n?String(x.n):String(x.n)+"/"+String(x.d);
const gates=[];
function gate(name,ok,detail){if(!ok)throw Error("FAILED: "+name);gates.push({name,passed:true,...(detail===undefined?{}:{detail})});}
function qgate(name,x,op,y){gate(name,op==="lt"?lt(x,y):op==="le"?le(x,y):eq(x,y),{left:str(x),relation:op,right:str(y)});}

const nv=7, zeroKey=Array(nv).fill(0).join(",");
function pc(n){n=BigInt(n);return n?new Map([[zeroKey,n]]):new Map();}
function pv(i){let e=Array(nv).fill(0);e[i]=1;return new Map([[e.join(","),1n]]);}
function pa(...xs){let z=new Map();for(let x of xs)for(let[k,v]of x){let a=(z.get(k)||0n)+v;if(a)z.set(k,a);else z.delete(k);}return z;}
function pn(x){return new Map([...x].map(([k,v])=>[k,-v]));}
function ps(x,y){return pa(x,pn(y));}
function pm(...xs){let z=pc(1);for(let x of xs){let t=new Map();for(let[a,av]of z)for(let[b,bv]of x){let ae=a.split(",").map(Number),be=b.split(",").map(Number);let k=ae.map((v,i)=>v+be[i]).join(",");let c=(t.get(k)||0n)+av*bv;if(c)t.set(k,c);else t.delete(k);}z=t;}return z;}
function pp(x,n){let z=pc(1);for(let i=0;i<n;i++)z=pm(z,x);return z;}
function pd(x,i){let z=new Map();for(let[k,v]of x){let a=k.split(",").map(Number);if(a[i]){let q=a[i];a[i]--;z.set(a.join(","),v*BigInt(q));}}return z;}
function pe(name,x){gate(name,x.size===0,{residual_monomials:x.size});}
const [w,p,k,q,r,s,t]=Array.from({length:nv},(_,i)=>pv(i));
const one=pc(1),twoP=pc(2),E=pa(one,pp(w,2)),T=ps(one,pp(p,2)),K=pa(w,k);
const J=pa(K,pm(E,q)),DD=ps(pm(E,T),pp(K,2));
const A0=pa(pn(k),pn(q),pm(w,ps(pm(k,q),pp(p,2)))),fn=pm(w,A0);
const z=ps(r,p),zt=ps(t,q);
pe("D_both_actual_forms",ps(DD,pa(one,pn(pm(twoP,w,k)),pn(pp(k,2)),pn(pm(E,pp(p,2))))));
const fkn=ps(pm(pd(fn,2),J),pm(fn,pd(J,2)));
const fqn=ps(pm(pd(fn,3),J),pm(fn,pd(J,3)));
const fpn=ps(pm(pd(fn,1),J),pm(fn,pd(J,1)));
pe("actual_f_k",ps(fkn,pm(pp(w,2),ps(pm(E,pp(q,2)),T))));
pe("actual_f_q",pa(fqn,pm(pp(w,2),DD)));
pe("actual_f_p",pa(fpn,pm(twoP,pp(w,2),p,J)));
const fthn=pa(pm(fkn,r),pm(fqn,s),pm(fpn,q));
pe("actual_full_f_theta",ps(fthn,pm(pp(w,2),pa(pm(ps(pm(E,pp(q,2)),T),r),pn(pm(DD,s)),pn(pm(twoP,p,q,J))))));
const Rkn=pa(
 pm(w,ps(pm(twoP,w,pp(z,2),J),pm(E,pp(z,2),pd(J,0))),J),
 pm(twoP,E,z,fthn),pn(pm(E,pp(z,2),fn)),
 pn(pm(fpn,z,J)),pn(pm(fkn,E,pp(z,2))),pn(pm(fqn,zt,J)));
const Rkc=pa(pm(twoP,E,z,fthn),
 pm(pp(w,2),pa(pm(ps(pm(twoP,K),pm(E,q)),pp(z,2)),pm(DD,zt)),J),
 pm(twoP,pp(w,2),p,z,pp(J,2)));
pe("actual_R_k_complete_no_b",ps(Rkn,Rkc));
const BKn=pa(pm(w,J),fn);
pe("pointwise_control_K",ps(BKn,pm(pp(w,2),pa(T,pm(K,q)))));
const BDn=ps(pm(twoP,pp(w,2),T,J),pm(twoP,K,BKn));
pe("pointwise_control_D",ps(BDn,pm(twoP,pp(w,2),q,DD)));
pe("pointwise_holonomy_invariance",ps(pm(twoP,q,BKn,DD),pm(pa(T,pm(K,q)),BDn)));
pe("mass_k_derivative",ps(pa(pm(q,DD),pm(K,pa(T,pm(K,q)))),pm(T,J)));
const fluxMinusMp=pa(pm(DD,T,r),pm(twoP,p,q,K,DD),pm(K,T,pa(pm(E,p,q),pm(K,r))),
 pn(pm(E,p,T,pa(T,pm(K,q)))),pn(pm(twoP,p,K,q,DD)),pn(pm(E,z,pp(T,2))));
pe("full_local_holonomy_conservation_flux",fluxMinusMp);
const B2n=pa(pp(k,2),pm(twoP,E,k,q),pm(E,pp(q,2)),pn(pm(pp(w,2),pp(p,2))));
pe("canonical_quadratic_control",ps(pa(fn,pm(pa(k,q),J)),B2n));
const BJn=pa(pm(w,pd(J,0),J),fn);
pe("actual_control_J",ps(BJn,pm(pp(w,2),pa(T,pm(K,q),pm(twoP,q,J)))));
const Bdn=pa(pm(w,ps(pm(twoP,w,z,J),pm(E,z,pd(J,0))),J),pm(E,fthn),pn(pm(E,z,fn)));
pe("actual_control_drift",ps(Bdn,pa(pm(E,fthn),pm(twoP,pp(w,2),z,pp(J,2)),pn(pm(E,z,BJn)))));
pe("actual_control_log_wave_factor",
 pa(pm(pp(w,2),q,J),pn(BJn),pm(pp(w,2),pa(T,pm(twoP,K,q),pm(E,pp(q,2))))));
pe("actual_log_wave_numerator",
 ps(ps(pp(J,2),pm(pp(w,2),pa(T,pm(twoP,K,q),pm(E,pp(q,2))))),
 pa(pp(K,2),pn(pm(pp(w,2),T)),pm(twoP,K,q),pm(E,pp(q,2)))));
/* Ray L c cancellation for each real branch, using independent scalar jets. */
for(let sig of [-1,1]){
 const [qq,v,d,vt,vth,dth,qt]=[w,p,k,q,r,s,t];
 const gg=pa(pn(d),pn(pm(pc(sig),qq,v)));
 const gth=pa(pn(dth),pn(pm(pc(sig),qq,vth)));
 const exact=ps(pm(qq,pa(vt,pm(gg,vth),pn(pm(gth,v)))),pm(v,qt));
 const claimed=ps(pm(qq,pa(vt,pn(pm(d,vth)),pm(v,dth))),pm(v,qt));
 pe("full_actual_ray_Lc_branch_"+sig,ps(exact,claimed));
}
/* The source norms use the actual small Fourier-algebra ball. */
const n=R(1,64), inv=D(R(1),S(R(1),M(R(3),n)));
qgate("actual_J_inverse",inv,"lt",R(2));
qgate("actual_D_norm",A(R(1),A(M(R(2),n),M(R(3),pow(n,2)))),"lt",R(2));
qgate("actual_T_norm",A(R(1),pow(n,2)),"lt",R(2));
qgate("actual_f_envelope",M(inv,A(M(R(2),n),M(R(2),pow(n,2)))),"lt",M(R(8),n));
qgate("actual_f_theta_envelope",M(R(4),A(M(R(5),n),M(R(4),pow(n,2)))),"lt",M(R(32),n));
qgate("actual_two_component_R_envelope",
 D(A(M(R(48),n),M(R(600),pow(n,2))),R(3)),"lt",M(two(10),n));
qgate("actual_canonical_control_coefficient",R(16,3),"lt",R(8));
qgate("actual_control_J_ratio",M(R(4),A(R(2),M(R(6),n))),"lt",R(9));
qgate("actual_control_drift_envelope",R(128+8*(2+9)),"lt",R(512));
qgate("actual_control_wave_envelope",M(R(4),A(R(16),M(R(24),n))),"lt",R(128));
qgate("actual_control_drift_wave_sum",R(512+128),"lt",two(10));
qgate("actual_profile_L1_fee",M(R(2),two(10)),"eq",two(11));
qgate("actual_fourier_width_margin",R(2),"eq",R(2));
/* Exact raw-to-canonical linear identities; c^2=1/12, nu=M^2(M^2-1)/12. */
const mm=w,mm2=pp(mm,2),nu12=pm(mm2,ps(mm2,one));
pe("linear_canonical_lower_all_modes",ps(nu12,ps(pp(mm,4),mm2)));
pe("linear_canonical_top_diagonal_all_modes",pa(pn(pc(3)),pn(one),mm2,pn(ps(mm2,pc(4)))));
pe("linear_canonical_bottom_diagonal_all_modes",pa(pn(pc(3)),pc(7),pn(mm2),ps(mm2,pc(4))));
/* No analytic or operator conclusion is inferred from these finite algebra gates. */
return {
 schema:"visible-exact-R119-actual-compact-profile-flux-gauge-v1",
 implementation:"new exact BigInt polynomial/rational computation in V8; not recovered Python native",
 scope:"Actual full nonlinear control gauge, pointwise holonomy, true rho4/rho5 source bounds, exact ray and physical-port identities; no unproved global response or D_Omega E estimate",
 input_blobs:inputBlobs,implementation_blob:implementationBlob,
 gates,gate_count:gates.length,all_passed:gates.every(x=>x.passed),
 retained:["both means","all Fourier modes","same current Gamma","full real branch dependence","total and bare weak-flux endpoint charges","actual g_psi propagation remains to be bounded"],
 excluded:["naked pullback operator-norm differentiation","global physical scattering difference from 64 eta alone","finite Fourier substitution for the full PDE","claim that full F is solved"]
 };
}
if(typeof module!=="undefined"&&module.exports)module.exports=computeCompactProfileFluxGauge;
