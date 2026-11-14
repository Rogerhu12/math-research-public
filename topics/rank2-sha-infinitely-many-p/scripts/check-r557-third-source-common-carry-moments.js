#!/usr/bin/env node
// Exact new R557 Q(omega) identities; omega^2+omega+1=0.
function certifyR557(){
const abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b){[a,b]=[b,a%b]}return a}
function q(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b}const g=gcd(a,b);return[a/g,b/g]}
const add=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>[-a[0],a[1]], sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>q(a[0]*b[0],a[1]*b[1]), div=(a,b)=>q(a[0]*b[1],a[1]*b[0]);
function pow(a,n){let r=q(1);for(;n;n>>=1,a=mul(a,a))if(n&1)r=mul(r,a);return r}
const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1], qs=a=>a[1]===1n?String(a[0]):a[0]+"/"+a[1];
const c=(a=0,b=0)=>[Array.isArray(a)?a:q(a),Array.isArray(b)?b:q(b)];
const ca=(a,b)=>[add(a[0],b[0]),add(a[1],b[1])], cn=a=>[neg(a[0]),neg(a[1])], cs=(a,b)=>ca(a,cn(b));
const cm=(a,b)=>[sub(mul(a[0],b[0]),mul(q(3),mul(a[1],b[1]))),add(mul(a[0],b[1]),mul(a[1],b[0]))];
const cc=a=>[a[0],neg(a[1])], norm=a=>add(mul(a[0],a[0]),mul(q(3),mul(a[1],a[1])));
const ci=a=>[div(a[0],norm(a)),neg(div(a[1],norm(a)))], cd=(a,b)=>cm(a,ci(b));
const ce=(a,b)=>eq(a[0],b[0])&&eq(a[1],b[1]), cj=a=>({real:qs(a[0]),delta:qs(a[1])});
function cp(a,n){let r=c(1);for(;n;n>>=1,a=cm(a,a))if(n&1)r=cm(r,a);return r}
function dot(a,b){return a.map((x,i)=>cm(x,cc(b[i]))).reduce(ca,c())}
function mm(A,B){return A.map(row=>B[0].map((_,j)=>row.map((x,k)=>cm(x,B[k][j])).reduce(ca,c())))}


const w=c(q(-1,2),q(1,2)), w2=cp(w,2), de=c(0,1);
const cw=(a,b=0)=>ca(c(a),cm(c(b),w));
const H=[[cm(c(q(1,2)),cw(-1,-1)),cm(c(q(1,2)),cw(-1,-2))],[cm(c(q(1,2)),cw(2,1)),cm(c(q(1,2)),cw(-1,-1))]];
const trans=r=>r.slice(0,3).concat(mm([r.slice(3)],H)[0]);
const D=[c(1),w2,cm(c(-2),w),c(1),cw(2,3)];
const obs=[
{name:"Y",a:cw(2,-1),z:[de,cm(c(2),de),cw(3,1),c(1),c(2)]},
{name:"W",a:cw(2,-1),z:[de,cm(c(2),de),cw(3,1),cm(c(3),de),c(4)]},
{name:"W2",a:cw(3,2),z:[cw(3,1),cm(c(2),de),cw(6,3),cw(-1,1),c(4)]}
];
const mixed=(d,z)=>cm(c(24),z.map((x,i)=>cm(x,d.filter((_,j)=>j!==i).reduce(cm,c(1)))).reduce(ca,c()));
const omegaFormat=a=>({a:qs(add(a[0],a[1])),b:qs(mul(q(2),a[1]))});
const vals=obs.map(o=>{const raw=mixed(D,o.z),etRaw=cm(w2,mixed(trans(D),trans(o.z))), alpha=cd(cn(raw),cm(c(84),o.a)),eta=cd(cn(etRaw),cm(c(84),o.a)),h=ca(eta,cm(c(q(1,2)),alpha));return{...o,raw,etRaw,alpha,eta,h}});
const ratio=cd(cm(w2,cm(trans(D)[3],trans(D)[4])),cm(D[3],D[4]));
const deltas={};
for(const state of ["alpha","eta","h"]){deltas[state]=[cs(cd(vals[1][state],cm(c(6),de)),vals[0][state]),cs(cd(vals[2][state],cm(c(-6),cm(de,w2))),vals[0][state])].map(v=>({value:omegaFormat(v),norm:qs(norm(v))}));}
return {D_H:trans(D).map(omegaFormat), mass_ratio_eta:omegaFormat(ratio),mass_ratio_h:omegaFormat(ca(ratio,c(q(1,2)))), rows:vals.map(v=>({name:v.name,Z_H:trans(v.z).map(omegaFormat),raw:omegaFormat(v.raw),eta_raw:omegaFormat(v.etRaw),alpha_rho:omegaFormat(v.alpha),alpha_eta:omegaFormat(v.eta),alpha_h:omegaFormat(v.h),norm_eta:qs(norm(v.eta)),norm_h:qs(norm(v.h))})),deltas};

}
if(typeof module!=="undefined"){
  module.exports={certifyR557};
  if(require.main===module){const r=certifyR557();require('fs').writeFileSync(__filename.replace(/\.js$/,'.json'),JSON.stringify(r,null,2)+'\n');console.log('R557 exact full source and moment coefficients computed.');}
}
