"use strict";

const z=[0n],one=[1n],trim=a=>{a=a.slice();while(a.length>1&&!a.at(-1))a.pop();return a};
const add=(a,b)=>trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||0n)+(b[i]||0n)));
const neg=a=>a.map(x=>-x),sub=(a,b)=>add(a,neg(b)),sc=(a,n)=>trim(a.map(x=>x*n));
const mul=(a,b)=>{let o=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)o[i+j]+=a[i]*b[j];return trim(o)};
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b]}return a}
function prim(a){a=trim(a);let g=0n;for(const x of a)g=gcd(g,x);if(!g)return a;if(a.at(-1)<0n)g=-g;return a.map(x=>x/g)}
function prem(a,b){a=trim(a);b=trim(b);while(a.length>=b.length&&a.some(x=>x)){let c=a.at(-1),m=a.length-b.length;a=sub(sc(a,b.at(-1)),Array(m).fill(0n).concat(sc(b,c)));a=prim(a)}return a}
function pgcd(a,b){while(b.some(x=>x)){[a,b]=[b,prem(a,b)]}return prim(a)}
function div(a,b){a=trim(a);b=trim(b);let q=Array(Math.max(1,a.length-b.length+1)).fill(0n);while(a.length>=b.length&&a.some(x=>x)){let n=a.at(-1);if(n%b.at(-1))throw Error("nonintegral division");let c=n/b.at(-1),m=a.length-b.length;q[m]+=c;a=sub(a,Array(m).fill(0n).concat(sc(b,c)))}if(a.some(x=>x))throw Error("nonzero remainder");return trim(q)}


function modularBezout(aa,bb,p=103){
const md=x=>((x%p)+p)%p,trim=a=>{a=a.slice();while(a.length>1&&!a.at(-1))a.pop();return a},add=(a,b)=>trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>md((a[i]||0)+(b[i]||0)))),neg=a=>a.map(x=>md(-x)),sub=(a,b)=>add(a,neg(b)),mul=(a,b)=>{const o=Array(a.length+b.length-1).fill(0);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)o[i+j]=md(o[i+j]+a[i]*b[j]);return trim(o)},inv=x=>{let a=md(x),y=1,n=p-2;while(n){if(n%2)y=y*a%p;a=a*a%p;n=Math.floor(n/2)}return y};
function div(a,b){a=trim(a);b=trim(b);const q=Array(Math.max(1,a.length-b.length+1)).fill(0);while(a.length>=b.length&&a.some(x=>x)){const c=md(a.at(-1)*inv(b.at(-1))),m=a.length-b.length;q[m]=md(q[m]+c);a=sub(a,Array(m).fill(0).concat(b.map(x=>md(x*c))))}return[q,a]}
const red=a=>trim(a.map(x=>Number((BigInt(x)%BigInt(p)+BigInt(p))%BigInt(p)))),a=red(aa),b=red(bb);
let r0=a,r1=b,u0=[1],u1=[0],v0=[0],v1=[1];while(r1.some(x=>x)){const[q,r]=div(r0,r1);[r0,r1]=[r1,r];[u0,u1]=[u1,sub(u0,mul(q,u1))];[v0,v1]=[v1,sub(v0,mul(q,v1))]}
const c=inv(r0.at(-1)),u=u0.map(x=>md(x*c)),v=v0.map(x=>md(x*c)),check=add(mul(u,a),mul(v,b));
return{p,degree_a:a.length-1,degree_b:b.length-1,lead_a:a.at(-1),lead_b:b.at(-1),gcd:r0.map(x=>md(x*c)),u,v,check,remainder_b_mod_a:div(b,a)[1]};
}

function verify(){
const S=[[25n,-25n,0n,100n,80n,-2800n],[-25n,25n,0n,-100n,-80n,-400n],[0n,0n,0n,0n,640n,3200n],[100n,-100n,0n,0n,0n,0n],[80n,-80n,640n,0n,-6912n,-34560n],[-2800n,-400n,3200n,0n,-34560n,-172800n]];
const q=[[0n,0n,-5n,1n],[0n,22n,-3n,1n],[-5n,-3n,-3n],[1n,1n]],qs=q.map(p=>p.slice(1).map((c,i)=>c*BigInt(i+1))),f=[[0n,0n,1n],[0n,-2n],[1n]],p=Array.from({length:6},()=>[0n]);
for(let i=0;i<4;i++)for(let j=0;j<3;j++)p[i+j]=add(p[i+j],mul(qs[i],f[j]));
const Y=S.map(row=>row.reduce((a,c,i)=>add(a,sc(p[i],c)),[0n]));
function det(M){if(M.length===1)return M[0][0];return M[0].reduce((o,x,j)=>add(o,sc(mul(x,det(M.slice(1).map(r=>r.filter((_,k)=>k!==j)))),j%2?-1n:1n)),[0n])}
const cat=Array.from({length:4},(_,i)=>Array.from({length:3},(_,j)=>Y[i+j])),minors=Array.from({length:2},(_,i)=>prim(det(cat.filter((_,j)=>j!==i))));
const zproof=modularBezout(minors[0],minors[1]);
if(zproof.degree_a!==10||zproof.degree_b!==10||String(zproof.check)!=="1"||zproof.lead_a!==4||zproof.lead_b!==2)throw Error("corrected tangent Cat Bezout");
const E=[9600n,-25472n,-3392n,15936n,-2888n,-936n,153n,50n,5n],N=[0n,110n,6n,26n,3n,3n],DD=[25n,-36n,-18n,24n,6n],Q=sc(DD,2n);
let composition=[0n];for(let i=0;i<=8;i++){let term=[E[i]];for(let j=0;j<i;j++)term=mul(term,N);for(let j=i;j<8;j++)term=mul(term,Q);composition=add(composition,term);}
const compproof=modularBezout(E,composition),rproof=modularBezout(E,compproof.remainder_b_mod_a);
if(composition.length!==41||composition.at(-1)!==32805n||String(compproof.check)!=="1"||String(rproof.check)!=="1")throw Error("double-root composition");
if(String(compproof.remainder_b_mod_a)!=="64,14,24,6,66,94,97,13")throw Error("composition remainder");
const ev=(p,x)=>p.reduceRight((a,c)=>a*x+c,0n),special=[];
for(const s of [0n,2n,-6n]){
const gg=pgcd(q.map(p=>ev(p,s)),qs.map(p=>ev(p,s)));special.push({s:String(s),gcd:gg.map(String)});
if(String(gg.map(String))!==(s===0n?"0,1":"1"))throw Error("special source pair");}
return {status:"exact",Y:Y.map(p=>p.map(String)),P0:minors[0].map(String),P1:minors[1].map(String),zproof,composition:composition.map(String),composition_remainder:compproof.remainder_b_mod_a,rproof,special};
}
if(typeof module!=="undefined")module.exports={verify};
if(typeof require!=="undefined"&&require.main===module)process.stdout.write(JSON.stringify(verify(),null,2)+"\n");
