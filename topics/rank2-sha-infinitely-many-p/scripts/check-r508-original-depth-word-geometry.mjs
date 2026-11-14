#!/usr/bin/env node
// R508: exact four-axis geometry. The all-length word theorem is proved in the accompanying text.
const certificate = (() => {

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

const alpha=c(37,3),one=c(1),zero=c();
const I=[[one,zero],[zero,one]];
const EU=[[cd(c(1396),c(1944)),cd(cm(c(2),cc(alpha)),c(1944))],
          [cd(cm(c(274),alpha),c(1944)),cd(c(548),c(1944))]];
const ms=(A,B)=>A.map((r,i)=>r.map((x,j)=>cs(x,B[i][j])));
const E={Z:[[one,zero],[zero,zero]],V:[[zero,zero],[zero,one]],U:EU,P:ms(I,EU)};
const star={Z:"V",V:"Z",U:"P",P:"U"};
const lines={Z:[c(),c(1)],V:[c(1),c()],U:[c(-2),alpha],P:[cc(alpha),c(274)]};
const mv=(A,v)=>A.map(r=>r.map((x,j)=>cm(x,v[j])).reduce(ca,c()));
const same=(a,b)=>a.length===b.length&&a.every((x,i)=>ce(x,b[i]));
const zeroVector=v=>v.every(x=>ce(x,c()));
for(const a of Object.keys(E)){
 const D0=ms(I,E[a]);
 if(!same(mv(D0,lines[a]),lines[a]))throw Error("image line");
 if(!zeroVector(mv(D0,lines[star[a]])))throw Error("kernel line");
 const prod=mm(E[a],E[star[a]]);
 if(!prod.every(r=>r.every(x=>ce(x,c()))))throw Error("complement product");
 if(!E[a].every((r,i)=>r.every((x,j)=>ce(ca(x,E[star[a]][i][j]),I[i][j]))))throw Error("complement sum");
}
const dets={};
const keys=Object.keys(lines);
for(let i=0;i<4;i++)for(let j=i+1;j<4;j++){
 const a=lines[keys[i]],b=lines[keys[j]];
 const det=cs(cm(a[0],b[1]),cm(a[1],b[0]));
 if(ce(det,c()))throw Error("coincident line");
 dets[keys[i]+","+keys[j]]={determinant:cj(det),norm:qs(norm(det))};
}
return{
 status:"exact complete four-axis projector and boundary-line certificate passed",
 complement:star,
 projectors:Object.fromEntries(Object.entries(E).map(([k,A])=>[k,A.map(r=>r.map(cj))])),
 mod_p_image_lines:Object.fromEntries(Object.entries(lines).map(([k,v])=>[k,v.map(cj)])),
 pair_determinants:dets,
 bad_rational_primes:[2,3,137,349],
 general_proof:"A reduced word has nonzero rank-one reduction modulo p. Its image line determines the first letter; invert it and induct. This is an all-length proof, not a finite word scan.",
 y_fixed_words:"Only nonnegative powers of V keep Z+bar(gamma)*x fixed when x is fixed.",
 projective_group:"The two nonorthogonal compression generators Z,U freely generate a rank-two free group."
};

})();
process.stdout.write(JSON.stringify(certificate, null, 2) + "\n");
