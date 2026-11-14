#!/usr/bin/env node
import fs from "node:fs";
const read=p=>JSON.parse(fs.readFileSync(new URL(p,import.meta.url),"utf8"));
const D7=read("../notes/2026-11-14-theta-degree136-cm7-exact.json");
const D19=read("../notes/2026-11-14-theta-degree136-cm19-exact.json");
const Snew=read("./check-r470-original-negative-source-new-line.json").Snew;
const probe=(function(D7,D19){
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


function qp(s){const a=String(s).split("/");return q(a[0],a[1]||1);}
const zvec=n=>Array.from({length:n},()=>c());
function pm(A,B){const O=zvec(A.length+B.length-1);for(let i=0;i<A.length;i++)for(let j=0;j<B.length;j++)O[i+j]=ca(O[i+j],cm(A[i],B[j]));return O;}
function pa(A,B){return Array.from({length:Math.max(A.length,B.length)},(_,i)=>ca(A[i]||c(),B[i]||c()));}
const ps=(A,s)=>A.map(x=>cm(x,s));
function pp(A,n){let r=[c(1)];for(;n;n>>=1,A=pm(A,A))if(n&1)r=pm(r,A);return r;}
function pd(A,B){let r=A.slice(),o=zvec(A.length-B.length+1);for(let i=o.length-1;i>=0;i--){o[i]=cd(r[i+B.length-1],B[B.length-1]);for(let j=0;j<B.length;j++)r[i+j]=cs(r[i+j],cm(o[i],B[j]));}if(r.some(x=>!ce(x,c())))throw Error("nonexact polynomial division");return o;}
const om=c(q(-1,2),q(1,2)),ga=c(q(5,2),q(1,2)),g13=c(q(7,2),q(1,2)),r7=c(q(2,7),q(-6,7));
const xp=[c(1),c(1)],xm=[c(-8),c(1)],X=[c(),c(1)];
const AA=pm(X,pp(xm,3)),BB=ps(pp(xp,3),c(64));
const quad=pa(pa(pm(AA,AA),ps(pm(AA,BB),c(q(-4,7)))),ps(pm(BB,BB),c(q(16,7))));
const S2=ps(pm(pm(pm(pm(pp(xp,3),pp(xm,2)),pa(AA,BB)),pa(AA,ps(BB,c(-8)))),quad),c(64));
const Q13=[c(q(40,13),q(24,13)),c(2,6),c(1)],R2=[c(-8),c(20),c(1)];
const ratioNumer=ps(pm([cn(r7),c(1)],Q13),cd(cm(om,cm(ga,g13)),c(8)));
let v=pm(pd(S2,pm(xp,R2)),ratioNumer);while(v.length<23)v.push(c());while(S2.length<23)S2.push(c());
const decode=d=>d.real.map((r,i)=>r.map((s,j)=>c(qp(s),qp(d.delta[i][j]))));
const M=decode(D7.matrix),N=decode(D19.matrix),D=decode(D19.D33);
const mv=(A,v)=>A.map(row=>row.reduce((a,x,j)=>ca(a,cm(x,v[j])),c()));
const ve=(a,b)=>a.every((x,i)=>ce(x,b[i])),va=(a,b)=>a.map((x,i)=>ca(x,b[i])),vs=(a,s)=>a.map(x=>cm(x,s));
const orbit=(A,x,n=18)=>{let r=[x];for(let j=1;j<=n;j++)r.push(mv(A,r[j-1]));return r;};
const O=orbit(M,v);
if(!ve(O[18],v))throw Error("order18");
const dv=mv(D,v),vp=vs(va(v,dv),c(q(1,2))),vm=vs(va(v,vs(dv,c(-1))),c(q(1,2)));
function solve(columns,b){const n=b.length,m=columns.length,T=Array.from({length:n},(_,i)=>[...columns.map(v=>v[i]),b[i]]);let piv=[];for(let j=0,r=0;j<m&&r<n;j++){let k=r;while(k<n&&ce(T[k][j],c()))k++;if(k===n)continue;[T[k],T[r]]=[T[r],T[k]];const di=T[r][j];T[r]=T[r].map(x=>cd(x,di));for(let h=0;h<n;h++)if(h!==r){const f=T[h][j];if(!ce(f,c()))T[h]=T[h].map((x,l)=>cs(x,cm(f,T[r][l])));}piv.push([r,j]);r++;}
for(const row of T)if(row.slice(0,m).every(x=>ce(x,c()))&&!ce(row[m],c()))return null;const sol=zvec(m);for(const[r,j]of piv)sol[j]=T[r][m];return {solution:sol,rank:piv.length};}
function cyclic(x){if(x.every(y=>ce(y,c())))return {dimension:0,minimal:[c(1)]};const os=orbit(M,x);for(let j=1;j<=18;j++){const s=solve(os.slice(0,j),os[j]);if(s)return {dimension:j,minimal:[...s.solution.map(cn),c(1)]};}throw Error("no polynomial");}
function eigen(x,l){const os=orbit(M,x,17);let sum=zvec(23),li=c(1);for(let j=0;j<18;j++){sum=va(sum,vs(os[j],li));li=cm(li,ci(l));}return vs(sum,c(q(1,18)));}
const specs=[];for(const sg of [1,-1])for(let j=0;j<3;j++){const l=cm(c(sg),cp(om,j));const ep=eigen(vp,l),em=eigen(vm,l);specs.push({lambda:cj(l),plusNonzero:!ep.every(x=>ce(x,c())),minusNonzero:!em.every(x=>ce(x,c())),plusMass:cj(ep[22]),minusMass:cj(em[22]),plus:ep.map(cj),minus:em.map(cj)});}
return {field:"Q(delta), delta^2=-3",basis:"sigma^136*x^2*X^j, j=0,...,22; b=1",source:v.map(cj),S2:S2.map(cj),leading:cj(v[21]),mass:cj(v[22]),cyclic:((r)=>({...r,minimal:r.minimal.map(cj)}))(cyclic(v)),plusCyclic:((r)=>({...r,minimal:r.minimal.map(cj)}))(cyclic(vp)),minusCyclic:((r)=>({...r,minimal:r.minimal.map(cj)}))(cyclic(vm)),Dplus:vp.map(cj),Dminus:vm.map(cj),S2_Dplus:ve(mv(D,S2),S2),S2_Dminus:ve(mv(D,S2),vs(S2,c(-1))),S2_N7_minus:ve(mv(M,S2),vs(S2,c(-1))),spectrum:specs};
});
const extra=(function(O,D7,Snew){
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


function qp(s){const a=String(s).split("/");return q(a[0],a[1]||1);}
const cv=o=>c(qp(o.real),qp(o.delta)),vv=v=>v.map(cv),zvec=n=>Array.from({length:n},()=>c());
const M=D7.matrix.real.map((r,i)=>r.map((s,j)=>c(qp(s),qp(D7.matrix.delta[i][j]))));
const mv=v=>M.map(row=>row.reduce((a,x,j)=>ca(a,cm(x,v[j])),c()));
const va=(a,b)=>a.map((x,i)=>ca(x,b[i])),vs=(a,s)=>a.map(x=>cm(x,s)),ve=(a,b)=>a.every((x,i)=>ce(x,b[i]));
const power=(v,n)=>{for(let j=0;j<n;j++)v=mv(v);return v;};
const v=vv(O.source),S2=vv(O.S2),vp=vv(O.Dplus),vm=vv(O.Dminus),om=c(q(-1,2),q(1,2));
if(!ve(power(v,9),va(v,S2)))throw Error("affine core");
const anti=vv(O.spectrum.find(x=>x.lambda.real==="-1").plus);if(!ve(anti,vs(S2,c(q(-1,2)))))throw Error("S projection");
const nvec=Snew.real.map((r,i)=>c(qp(r[0]),qp(Snew.delta[i][0])));
const newp=vv(O.spectrum.find(x=>x.lambda.real==="-1/2"&&x.lambda.delta==="-1/2").minus);
const cnw=c(q(26,3),q(-26,3));if(!ve(newp,vs(nvec,cnw)))throw Error("new line projection");
const blocks=[];
for(const sign of [1,-1]){const x=sign===1?va(vp,vs(S2,c(q(1,2)))):vm,x3=power(x,3),x6=power(x,6);
 for(const tau of [om,cp(om,2)]){const b=vs(va(va(x,vs(x3,ci(tau))),vs(x6,cp(ci(tau),2))),c(q(1,3)));if(b.every(x=>ce(x,c())))throw Error("missing external block");blocks.push({D33:sign,tau:cj(tau),mass:cj(b[22]),first_orbit_masses:[b,mv(b),power(b,2)].map(v=>cj(v[22])),vector:b.map(cj)});}
}
const massRefs=O.spectrum.reduce((a,o)=>ca(a,ca(cv(o.plusMass),cv(o.minusMass))),c());
return {affine_core:"N7^9 F_eta = F_eta + S(2z)",original_projection:"-S(2z)/2",new_coefficient:cj(cnw),reference_mass_sum:cj(massRefs),external_blocks:blocks};
});
const out=probe(D7,D19),report={...out,...extra(out,D7,Snew),status:"exact full fixed theta-source computation; not a prime sample"};
let den=1n;
function gg(a,b){while(b){[a,b]=[b,a%b];}return a<0n?-a:a;}
function visit(x){if(Array.isArray(x)){for(const y of x)visit(y);}else if(x&&typeof x==="object"){for(const [k,v]of Object.entries(x))if((k==="real"||k==="delta")&&typeof v==="string"&&/^-?\d+\/\d+$/.test(v)){const d=BigInt(v.split("/")[1]);den=den/gg(den,d)*d;}else visit(v);}}
visit(report);report.new_coefficient_denominator_lcm=String(den);
if(report.cyclic.dimension!==10||report.plusCyclic.dimension!==10||report.minusCyclic.dimension!==8)throw Error("cyclic dimensions");
fs.writeFileSync(new URL("./check-r542-original-eta-arithmetic-projections.json",import.meta.url),JSON.stringify(report,null,2)+"\n");
console.log(JSON.stringify({cyclic:10,joint_cyclic:18,source_mass:report.mass,affine_core:report.affine_core,new_coefficient:report.new_coefficient,denominator_lcm:String(den)}));
