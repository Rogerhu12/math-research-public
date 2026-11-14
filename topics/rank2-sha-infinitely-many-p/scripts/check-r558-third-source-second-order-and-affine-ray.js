#!/usr/bin/env node
// Exact R558 calculation reuses the published R536 matrix and right inverse.
function computeRowsR558(cert){
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


const w=c(q(-1,2),q(1,2)),cw=(a,b=0)=>ca(c(a),cm(c(b),w));
const pq=s=>{const t=s.split("/");return q(t[0],t[1]||"1");};
const parse=v=>ca(c(pq(v[0])),cm(c(pq(v[1])),w));
const ps=(A,B)=>Array.from({length:Math.max(A.length,B.length)},(_,i)=>ca(A[i]||c(),B[i]||c()));
const pm=(A,B)=>{let C=Array.from({length:A.length+B.length-1},()=>c());for(let i=0;i<A.length;i++)for(let j=0;j<B.length;j++)C[i+j]=ca(C[i+j],cm(A[i],B[j]));return C;};
const sc=(A,b)=>A.map(a=>cm(a,b));

const p3mul=(P,Q)=>{const R={};for(const[k,a]of Object.entries(P))for(const[l,b]of Object.entries(Q)){const u=k.split(",").map(Number),v=l.split(",").map(Number),m=u.map((x,i)=>x+v[i]).join(",");R[m]=ca(R[m]||c(),cm(a,b));}return R;};
const p3pow=(P,n)=>{let R={"0,0,0":c(1)};for(let i=0;i<n;i++)R=p3mul(R,P);return R;};
const cpoly={"1,0,0":c(q(-1,14)),"0,1,0":c(q(1,14))},fpoly={"1,0,0":c(q(13,14)),"0,1,0":c(q(1,14))},gpoly={"0,0,1":c(1)};
const make=(i,j,k)=>p3mul(p3mul(p3pow(cpoly,i),p3pow(fpoly,j)),p3pow(gpoly,k));
const polys={base:Object.fromEntries(Object.entries(make(6,0,0)).map(([k,v])=>[k,cm(v,c(q(-1,8)))])),polys:cert.matrix.exps.map(e=>make(...e))};

const B=cert.polynomial_right_inverse.B.map(M=>M.map(r=>r.map(parse)));
const b0=cert.matrix.b0.map(parse),b1=cert.matrix.b1.map(parse);
const x=Array.from({length:10},(_,i)=>b0.map((_,j)=>pm([B[0][i][j],B[1][i][j]],[b0[j],b1[j]])).reduce(ps,[c()]));
const e0=parse(cert.matrix.e0),g0=parse(cert.matrix.g0);
function row(P,k){let r=[c()];for(const[mon,co]of Object.entries(P)){const [a,j,l]=mon.split(",").map(Number);if(a!==k)continue;const coeff=cm(co,cm(cp(e0,j),cp(g0,l)));r=ps(r,j===0?[c(),coeff]:[coeff]);}return r;}
const polyOutputs=[];
for(let k=0;k<=6;k++){
 let rr=pm([c(-1),c(1)],row(polys.base,k));
 for(let i=0;i<10;i++)rr=ps(rr,pm(row(polys.polys[i],k),x[i]));
 while(rr.length>1&&ce(rr[rr.length-1],c()))rr.pop();
 polyOutputs.push({k,numerator_in_tau_over_tau_minus_1:rr.map(cj)});
}
return {rows:polyOutputs};

}
function unitConstantsR558(row){
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


const pq=s=>{const t=s.split("/");return q(t[0],t[1]||"1");};
const parse=v=>c(pq(v.real),pq(v.delta));
const [A,B]=row.numerator_in_tau_over_tau_minus_1.map(parse);
const a=cn(A),b=ca(A,B);
let C=1n;for(const z of [...a,...b])C=C/gcd(C,z[1])*z[1];
const ai=cm(a,c(C)),bi=cm(b,c(C)),Na=norm(ai),Nb=norm(bi);
const w=c(q(-1,2),q(1,2)),w2=cp(w,2);
const units=[["1",c(1)],["-1",c(-1)],["omega",w],["-omega",cn(w)],["omega^2",w2],["-omega^2",cn(w2)]];
const candidates=units.map(([name,z])=>({name,z,qz:ca(cd(ai,z),cd(bi,cp(z,2)))}));
let best=candidates[0];for(const t of candidates.slice(1)){let d=sub(norm(t.qz),norm(best.qz));if(d[0]>0n)best=t;}
const gap=sub(norm(best.qz),Nb);
const t1=div(mul(q(16),mul(Na,Nb)),mul(gap,gap)),t2=div(mul(q(2),Na),gap);
const f1=t1[0]/t1[1]+1n,f2=t2[0]/t2[1]+1n,budget=q(f1>f2?f1:f2);
const coeffs=[add(ai[0],ai[1]),mul(q(2),ai[1]),add(bi[0],bi[1]),mul(q(2),bi[1])];
if(coeffs.some(x=>x[1]!==1n))throw Error("integral Eisenstein coefficients required");
const modulusMultiplier=q(2n*coeffs.map(x=>abs(x[0])).reduce((a,b)=>a+b,0n)+1n);
const cf=cd(cm(c(2),cm(w2,cs(c(8),cm(c(3),w)))),cm(c(7),cp(cs(c(2),w),2)));
const om=z=>({a:qs(add(z[0],z[1])),b:qs(mul(q(2),z[1]))});
return {row_index:3,A:cj(A),B:cj(B),affine_a:cj(a),affine_b:cj(b),clear_denominator:String(C),integral_a:om(ai),integral_b:om(bi),norm_integral_a:qs(Na),norm_integral_b:qs(Nb),chosen_unit:best.name,norm_q_zeta:qs(norm(best.qz)),positive_norm_gap:qs(sub(norm(best.qz),Nb)),p_strict_lower_bound:qs(budget),new_modulus_multiplier:qs(modulusMultiplier),new_modulus:"1 + 37 * old_full_ray_modulus * new_modulus_multiplier",second_order_unit_factor:om(cf),second_order_factor_norm:qs(norm(cf))};

}

function exactOldRayModulus(){
 const gcd=(a,b)=>{while(b)[a,b]=[b,a%b];return a;};
 return [1323133171213029144041201350687525528684869767169429257083200n,29n,137n,79n,103n,263n,49n,1013n,31n].reduce((a,b)=>a/gcd(a,b)*b,1n);
}
function certifyR558(cert){
 const row=computeRowsR558(cert).rows[3],constants=unitConstantsR558(row);
 const N0=exactOldRayModulus();
 constants.old_full_ray_modulus=String(N0);
 constants.actual_new_modulus=String(1n+37n*N0*BigInt(constants.new_modulus_multiplier));
 return{format:"R558 exact new row from the existing R536 right inverse; no prime samples.",r536_blob:"ab452d507aa20c2326312ab059187e0c920c87ec",row,constants};
}
if(typeof module!=="undefined"){
 module.exports={certifyR558};
 if(require.main===module){
  const fs=require("fs"),path=require("path");
  const cert=JSON.parse(fs.readFileSync(path.join(__dirname,"check-r536-exact-fibre-mass-compensation.json"),"utf8"));
  const result=certifyR558(cert);
  fs.writeFileSync(__filename.replace(/\.js$/,".json"),JSON.stringify(result,null,2)+"\n");
  console.log("R558 exact second-order row and fixed affine-ray constants computed.");
 }
}
