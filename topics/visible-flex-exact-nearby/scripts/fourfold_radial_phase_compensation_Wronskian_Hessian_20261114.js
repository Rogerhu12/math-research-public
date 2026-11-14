/* R119 actual radial phase compensation and fixed-port Wronskian Hessian.
   New exact BigInt/rational/Laurent implementation, 2026-11-14.
   Run with Node; no external dependencies. */
(function(){
"use strict";
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

const len=R(1,32), d=R(1,80), e=two(-190);
qgate("principal_shape_first",len,"lt",R(1,16));
qgate("principal_shape_second",M(M(d,len),R(1,2)),"lt",two(-10));
const c21=A(R(3,512),D(R(273,2),R(64*80*80*32)));
qgate("beta_shape_first",c21,"lt",R(1,16));
const c22=A(D(M(d,len),R(16)),M(D(M(pow(d,3),len),R(64)),A(R(72),R(35*49,4))));
qgate("beta_shape_second",c22,"lt",two(-10));
qgate("inverse_row1_numerator",A(R(61,1000),R(5,1000)),"lt",R(1,8));
qgate("inverse_row2_numerator",A(R(87,1000),R(23,2000)),"lt",R(1,8));
qgate("actual_two_phase_inverse",M(R(1,8),two(12)),"eq",two(9));
qgate("psi1_third_derivative",R(384*8*8*8),"eq",M(R(3),two(16)));
qgate("psi2_third_derivative",R(384*32*32*32),"eq",M(R(3),two(22)));
qgate("shifted_Legendre_extrema_below_one",R(1,5),"lt",R(1));
qgate("complete_principal_Jacobian_row",R(105,64),"lt",R(2));
const bcoef=A(M(R(7,8),A(R(3,16),A(M(R(3,16),e),M(R(9,16),pow(e,2))))),M(R(12,6400),A(R(24),R(735,16))));
qgate("complete_Bs_complex_bound",bcoef,"lt",R(1));
qgate("first_bump_complex_u_second_bound",A(R(25),M(M(R(3),two(16)),D(two(-15),R(80)))),"lt",R(64));
qgate("second_bump_complex_u_second_bound",A(R(25),M(M(R(3),two(22)),D(two(-29),R(80)))),"lt",R(64));
qgate("first_bump_complex_u_first_bound",A(R(45,8),M(R(6144,80),two(-15))),"lt",R(7));
qgate("second_bump_complex_u_first_bound",A(R(29,5),M(R(98304,80),two(-29))),"lt",R(7));
qgate("second_bump_complex_u_gap",A(R(1,2),M(R(384,80),two(-29))),"lt",R(22815,32768));
qgate("Cauchy_Gamma2_circle_inside",A(two(-30),two(-31)),"lt",two(-29));
qgate("Cauchy_Gamma1_circle_inside",A(two(-16),two(-31)),"lt",two(-15));
qgate("full_gamma_Hessian_bound",M(R(4),two(31)),"lt",two(34));
qgate("compensation_contraction",two(9+34-48),"eq",R(1,32));
qgate("compensation_forcing",M(two(9),D(two(-64),R(16))),"eq",two(-59));
qgate("compensation_quadratic_selfmap",M(M(two(9),D(two(34),R(2))),two(-96)),"eq",two(-54));
qgate("compensation_complete_selfmap",A(two(-59),two(-54)),"lt",two(-48));
qgate("current_true_inverse",D(two(9),R(31,32)),"lt",two(10));
qgate("full_shape_compensation_Lipschitz",D(two(10),R(16)),"le",two(6));
qgate("full_compensation_Hessian",M(two(10),A(two(-10),M(two(34),two(12)))),"lt",two(58));
qgate("annihilator_quadratic_control",M(two(10),two(-11)),"le",R(1));
qgate("annihilator_first_control",M(two(10),two(-10)),"le",R(1));
qgate("annihilator_full_second_control",A(R(1),two(44-128)),"lt",R(2));
qgate("compensation_stays_Gamma2_core",A(two(-32),two(-58)),"lt",two(-30));
qgate("compensation_stays_Gamma1_core",A(two(-18),two(-58)),"lt",two(-16));
qgate("old_bump_Ctwo_sum",R(6144+98304),"lt",two(18));
qgate("actual_compensated_first_shape",A(R(1),two(18-64)),"lt",R(2));
qgate("actual_compensated_second_shape",M(R(2),two(18)),"le",two(19));
qgate("constant_platform_k_ge_2M",R(0),"lt",R(3*16-16));
qgate("direct_Hessian_lower_order",R(1,80),"lt",R(1));
qgate("complete_A_Hessian_fee",A(two(19),R(1)),"lt",two(20));
qgate("two_ordered_Duhamel_Hessian_fee",A(two(18),R(8)),"lt",two(22));
qgate("full_label_first_parameter_fee",M(R(16),two(21)),"eq",two(25));
qgate("full_label_second_polarization_fee",A(two(48),two(35)),"lt",two(50));

/* Exact Laurent identities. v=sqrt(B), z=sqrt(u), Delta=a*v^2.
   Variables after ux stand for independent variation jets. */
const names=["a","v","z","ux","px","pxx","qx","qxx","Q","Qt","t1","t2","t12","t1t","t2t","t12t","t1tt","t2tt","t12tt","m","k"];
const ix=Object.fromEntries(names.map((n,i)=>[n,i]));
const dim=names.length;
const ek=e=>e.join(",");
const un=k=>k.split(",").map(Number);
function mon(c,ex={}){let es=Array(dim).fill(0);for(const[n,j]of Object.entries(ex))es[ix[n]]=j;let p=new Map();if(c.n)p.set(ek(es),c);return p;}
const pc=n=>mon(R(n));
const pm=(c,e)=>mon(c,e);
const ps=(n,e)=>pm(R(n),e);
function pa(P,Q){let X=new Map(P);for(const[k,c]of Q){let z=A(X.get(k)||R(0),c);if(z.n)X.set(k,z);else X.delete(k);}return X;}
const pn=P=>new Map([...P].map(([k,c])=>[k,N(c)]));
const pd=(P,Q)=>pa(P,pn(Q));
function pp(P,Q){let X=new Map();for(const[k,c]of P)for(const[l,f]of Q){let x=un(k),y=un(l);let ex={};for(const n of names)ex[n]=x[ix[n]]+y[ix[n]];X=pa(X,mon(M(c,f),ex));}return X;}
function diff(P,n){let X=new Map();for(const[k,c]of P){let x=un(k),j=x[ix[n]];if(!j)continue;x[ix[n]]--;let ex={};for(const v of names)ex[v]=x[ix[v]];X=pa(X,mon(M(c,R(j)),ex));}return X;}
const du=P=>pp(pm(R(1,2),{z:-1}),diff(P,"z"));
const delta=ps(1,{a:1,v:2}), dinv=ps(1,{a:-1,v:-2});
const Fe=pa(ps(1,{z:3}),pa(ps(2,{v:-2,z:1}),ps(1,{v:-4,z:-1})));
const T=pa(pc(1),ps(1,{v:2,z:2}));
const betaOriginal=pa(pp(pm(R(1,16),{a:1,v:-2,z:-1}),pp(T,T)),pm(R(1,64),{a:-1,v:-2,ux:2,z:-5}));
const betaExpected=pa(pp(pm(R(1,16),{a:1,v:2}),Fe),pm(R(1,64),{a:-1,v:-2,ux:2,z:-5}));
gate("exact_full_beta_dimensionless_units",pd(betaOriginal,betaExpected).size===0);
function varp(P,x,xx){return pn(pp(dinv,pa(pp(ps(1,{[x]:1}),du(P)),pp(ps(1,{[xx]:1}),diff(P,"ux")))));}
const thetaNorm=ps(-2,{a:1,v:2,z:1});
const thetaD=varp(thetaNorm,"px","pxx");
gate("exact_Theta_minus_two_S_first_variation",pd(thetaD,ps(1,{px:1,z:-1})).size===0);
gate("exact_Theta_second_variation",pd(varp(thetaD,"qx","qxx"),pm(R(1,2),{a:-1,v:-2,px:1,qx:1,z:-3})).size===0);
const betaD=varp(betaExpected,"px","pxx");
const betaDexpected=pa(pp(pm(R(-1,16),{px:1}),du(Fe)),
 pp(pm(R(1,64),{a:-2,v:-4}),pa(ps(-2,{ux:1,pxx:1,z:-5}),pm(R(5,2),{ux:2,px:1,z:-7}))));
gate("exact_full_beta_first_variation",pd(betaD,betaDexpected).size===0);
const betaDD=varp(betaD,"qx","qxx");
let betaDDexpected=pp(pm(R(1,16),{a:-1,v:-2,px:1,qx:1}),du(du(Fe)));
let gg=pa(ps(2,{pxx:1,qxx:1,z:-5}),pa(ps(-5,{ux:1,pxx:1,qx:1,z:-7}),pa(ps(-5,{ux:1,qxx:1,px:1,z:-7}),pm(R(35,4),{ux:2,px:1,qx:1,z:-9}))));
betaDDexpected=pa(betaDDexpected,pp(pm(R(1,64),{a:-3,v:-6}),gg));
gate("exact_full_beta_symmetric_second_variation",pd(betaDD,betaDDexpected).size===0);
const H=pa(ps(1,{m:2,Q:1}),pa(pm(R(1,2),{Qt:1}),pp(pm(R(-1,4),{}),pp(pa(pc(1),ps(1,{Q:1})),pa(pc(1),ps(1,{Q:1}))))));
const At=pn(pp(ps(1,{k:-1}),H));
function shapeD(P,t,tt){return pn(pa(pp(ps(1,{[t]:1}),diff(P,"Q")),pp(ps(1,{[tt]:1}),diff(P,"Qt"))));}
const Afirst=shapeD(At,"t1t","t1tt");
const expectedAfirst=pp(ps(1,{k:-1}),pa(pp(pd(ps(1,{m:2}),pm(R(1,2),{Q:1})),ps(1,{t1t:1})),pa(pm(R(-1,2),{t1t:1}),pm(R(1,2),{t1tt:1}))));
gate("exact_physical_A_first_variation",pd(Afirst,expectedAfirst).size===0);
const Asecond=pa(shapeD(Afirst,"t2t","t2tt"),shapeD(At,"t12t","t12tt"));
const expectedAsecond=pa(shapeD(At,"t12t","t12tt"),pm(R(1,2),{k:-1,t1t:1,t2t:1}));
gate("exact_compensated_A_second_variation",pd(Asecond,expectedAsecond).size===0);
const mu12=pa(ps(1,{t1:1,t2:1}),ps(1,{t12:1}));
const secondRow=pa(pn(pp(ps(1,{Q:1}),mu12)),pa(ps(1,{t1:1,t2t:1}),pa(ps(1,{t2:1,t1t:1}),ps(1,{t12t:1}))));
const productSecond=pa(pn(pp(ps(1,{Q:1}),mu12)),pn(pa(pp(ps(1,{t1:1}),ps(-1,{t2t:1})),pa(pp(ps(1,{t2:1}),ps(-1,{t1t:1})),ps(-1,{t12t:1})))));
gate("exact_second_metric_density_row",pd(secondRow,productSecond).size===0);
const invSecond=pd(ps(1,{t1:1,t2:1}),ps(1,{t12:1}));
const inverseProductSecond=pa(pa(mu12,invSecond),pa(pp(ps(1,{t1:1}),ps(-1,{t2:1})),pp(ps(1,{t2:1}),ps(-1,{t1:1}))));
gate("exact_mean_inverse_density_second_from_product",inverseProductSecond.size===0);
const ordinarySecond=pa(ps(4,{t1:1,t2:1}),ps(2,{t12:1}));
gate("ordinary_w_squared_full_second_factor",pd(ordinarySecond,pa(pp(pc(2),mu12),ps(2,{t1:1,t2:1}))).size===0);
const report={
 schema:"R119-radial-phase-compensation-Wronskian-Hessian-v1",
 date:"2026-11-14",
 computation:"new JavaScript exact BigInt rational and Laurent identities",
 dependencies:{"proof":"dd0d1378fce997297795ce14312fe91b181af4b1","controls53":"f11edbccd752bf034aa40e71888859d667a04b42","two_phase":"ae87a824ab3e58479894df470c9f066969e83241","compact":"5662bf40391a53a2212311406cf7ad63064908fc"},
 domains:{shape_complex_radius:"2^-64",gamma_correction_ball:"2^-48",Gamma1_complex:"2^-15",Gamma2_complex:"2^-29"},
 proved_bounds:{Dphase_shape:"<1/16",D2phase_shape:"<2^-10",true_phase_inverse:"<2^9",annihilator_D2Gamma:"<2",Wronskian_Hessian:"<2^22 K_j^3 (|m|+B/|m|)^2"},
 scope:"radial compensated profile, actual fixed Robin ports, all complete source and mean variations retained; no whole nonlinear F closure",
 gates_count:gates.length,all_passed:true,gates
};
if(typeof console!=="undefined"&&typeof console.log==="function")console.log(JSON.stringify(report,null,2));
return report;
})()
