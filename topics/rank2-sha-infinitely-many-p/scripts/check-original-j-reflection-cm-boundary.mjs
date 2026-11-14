#!/usr/bin/env node
import {readFileSync} from "node:fs";
const DATA=JSON.parse(readFileSync(new URL("./check-r464-degree102-cm7-exact.json",import.meta.url),"utf8"));
const cert=(function(DATA){

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

const NMAX=3;
function qp(s){const t=String(s).split("/");return q(t[0],t[1]||1)}
const zvec=n=>Array.from({length:n},()=>c());
function sm(A,B,L=NMAX+1){const out=zvec(L);for(let i=0;i<A.length;i++)for(let j=0;j<B.length&&i+j<L;j++)out[i+j]=ca(out[i+j],cm(A[i],B[j]));return out}
function sp(A,n,L=NMAX+1){let out=zvec(L);out[0]=c(1);for(;n;n>>=1,A=sm(A,A,L))if(n&1)out=sm(out,A,L);return out}
const wp=[q(1),q(-1,7)];
for(let n=2;n<=NMAX;n++){let sum=q(0);for(let i=1;i<n;i++)sum=add(sum,mul(wp[i],wp[n-i]));wp[n]=div(sum,q((6*n+1)*(n-1)))}
const logs=[q(0),...wp.slice(1).map((v,i)=>div(neg(v),q(6*(i+1)*(6*(i+1)-1))))];
const sig=[q(1)];for(let n=1;n<=NMAX;n++){let s=q(0);for(let j=1;j<=n;j++)s=add(s,mul(q(j),mul(logs[j],sig[n-j])));sig[n]=div(s,q(n))}
function sigmaPoly(alpha,N,off){const m=(N-2*off-1)/6;if(!Number.isInteger(m))throw Error("type");const p=zvec(m+1),partial=zvec(m+1),A=sp(sig.map(v=>c(v)),N),B=wp.map(v=>c(v));
 for(let k=0;k<=m;k++){const target=cm(c(sig[k]),cp(alpha,6*k));const coeff=cs(target,partial[k]);p[m-k]=coeff;const basis=sm(A,sp(B,off+3*(m-k)));for(let j=0;j+k<=m;j++)partial[j+k]=ca(partial[j+k],cm(coeff,basis[j]))}
 for(let k=0;k<=m;k++)if(!ce(partial[k],cm(c(sig[k]),cp(alpha,6*k))))throw Error("source reconstruction");
 return p;
}
const om=c(q(-1,2),q(1,2)),delta=c(0,1),barGamma=c(q(5,2),q(-1,2));
const a13=c(1,2),a21=cn(cm(delta,barGamma)),a19=c(-4,-1);
const p13=sigmaPoly(a13,13,0),p21=sigmaPoly(a21,21,1),p19=sigmaPoly(a19,19,0);
const polyMul=(a,b)=>sm(a,b,a.length+b.length-1);
const Gpoly=[[4,1],[1,1],[-8,1],[-8,1],[64,48,228,1]].map(v=>v.map(x=>c(x))).reduce(polyMul,[c(1)]);
let v=polyMul(polyMul(polyMul(Gpoly,p13),p21),p19);
v=[c(),...v].map(x=>cm(x,cm(cd(delta,c(7)),cm(cp(om,2),cm(a13,cm(a21,a19))))));
while(v.length<18)v.push(c());
const M=DATA.matrix.real.map((r,i)=>r.map((s,j)=>c(qp(s),qp(DATA.matrix.delta[i][j]))));
const mv=x=>M.map(r=>r.map((a,j)=>cm(a,x[j])).reduce(ca,c()));
const orbit=[v];for(let j=1;j<=18;j++)orbit.push(mv(orbit[j-1]));
if(orbit[18].some((a,i)=>!ce(a,v[i])))throw Error("N7^18");
const proj=zvec(18);for(let j=0;j<6;j++)for(let i=0;i<18;i++)proj[i]=ca(proj[i],cm(c(q(j%2?-1:1,6)),orbit[3*j][i]));
const ari=Object.entries(DATA.arithmetic_pullback_basis).map(([name,o])=>({name,v:o.real.map((r,i)=>c(qp(r[0]),qp(o.delta[i][0])))}));
function solve(A,b){const n=A.length,m=A[0].length,T=A.map((r,i)=>[...r,b[i]]);let piv=[];for(let j=0,r=0;j<m&&r<n;j++){let k=r;while(k<n&&ce(T[k][j],c()))k++;if(k===n)continue;[T[k],T[r]]=[T[r],T[k]];const d=T[r][j];T[r]=T[r].map(x=>cd(x,d));for(let h=0;h<n;h++)if(h!==r){const f=T[h][j];if(!ce(f,c()))T[h]=T[h].map((x,l)=>cs(x,cm(f,T[r][l])))}piv.push([r,j]);r++}for(const row of T)if(row.slice(0,m).every(x=>ce(x,c()))&&!ce(row[m],c()))return null;const sol=zvec(m);for(const[r,j]of piv)sol[j]=T[r][m];return {solution:sol,rank:piv.length}}
const coeffs=solve(Array.from({length:18},(_,i)=>ari.map(o=>o.v[i])),proj);
if(!coeffs)throw Error("arithmetic projection outside");
if(orbit[3].some((a,i)=>!ce(a,cm(om,v[i]))))throw Error("N7 cubed scalar");
const rank=solve(Array.from({length:18},(_,i)=>orbit.slice(0,18).map(v=>v[i])),zvec(18)).rank;
const outside=v.map((a,i)=>cs(a,proj[i]));
const n9pos=v.map((a,i)=>cm(c(q(1,2)),ca(a,orbit[9][i])));
const n9neg=v.map((a,i)=>cm(c(q(1,2)),cs(a,orbit[9][i])));
return {status:"exact",sigma:sig.map(qs),wp:wp.map(qs),p13:p13.map(cj),p19:p19.map(cj),p21:p21.map(cj),
v:v.map(cj),orbit:orbit.slice(0,18).map(v=>v.map(cj)),rank,arithmetic:ari.map((o,i)=>({name:o.name,coefficient:cj(coeffs.solution[i])})),
N7_cubed_scalar:cj(om),N7_cubed_identity:true,outside_zero:outside.every(a=>ce(a,c())),outside_mass:cj(outside[17]),n9pos_zero:n9pos.every(a=>ce(a,c())),n9neg_zero:n9neg.every(a=>ce(a,c())),leading:cj(v[16])};

})(DATA);
cert.orbit=cert.orbit.slice(0,3);
if(cert.rank!==3||cert.arithmetic.some(x=>x.coefficient.real!=="0"||x.coefficient.delta!=="0"))throw Error("spectral assertions");
process.stdout.write(JSON.stringify(cert,null,2)+"\n");
