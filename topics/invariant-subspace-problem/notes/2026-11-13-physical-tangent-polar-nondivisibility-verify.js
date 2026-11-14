"use strict";
// Original-form exact author certificate; no numerical root approximation.

const z=[0n],one=[1n],trim=a=>{a=a.slice();while(a.length>1&&!a.at(-1))a.pop();return a};
const add=(a,b)=>trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||0n)+(b[i]||0n)));
const neg=a=>a.map(x=>-x),sub=(a,b)=>add(a,neg(b)),sc=(a,n)=>trim(a.map(x=>x*n));
const mul=(a,b)=>{let o=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)o[i+j]+=a[i]*b[j];return trim(o)};
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b]}return a}
function prim(a){a=trim(a);let g=0n;for(const x of a)g=gcd(g,x);if(!g)return a;if(a.at(-1)<0n)g=-g;return a.map(x=>x/g)}
function prem(a,b){a=trim(a);b=trim(b);while(a.length>=b.length&&a.some(x=>x)){let c=a.at(-1),m=a.length-b.length;a=sub(sc(a,b.at(-1)),Array(m).fill(0n).concat(sc(b,c)));a=prim(a)}return a}
function pgcd(a,b){while(b.some(x=>x)){[a,b]=[b,prem(a,b)]}return prim(a)}
function div(a,b){a=trim(a);b=trim(b);let q=Array(Math.max(1,a.length-b.length+1)).fill(0n);while(a.length>=b.length&&a.some(x=>x)){let n=a.at(-1);if(n%b.at(-1))throw Error("nonintegral division");let c=n/b.at(-1),m=a.length-b.length;q[m]+=c;a=sub(a,Array(m).fill(0n).concat(sc(b,c)))}if(a.some(x=>x))throw Error("nonzero remainder");return trim(q)}

function verify(){
const E=[9600n,-25472n,-3392n,15936n,-2888n,-936n,153n,50n,5n];
const A=[1n,1n],B=[-5n,-3n,-3n],C=[0n,22n,-3n,1n],D=[0n,0n,-5n,1n];
const disc=add(add(sub(mul(mul(B,B),mul(C,C)),sc(mul(A,mul(mul(C,C),C)),4n)),sub(sc(mul(mul(mul(A,B),C),D),18n),sc(mul(mul(B,B),mul(B,D)),4n))),sc(mul(mul(A,A),mul(D,D)),-27n));
if(JSON.stringify(disc.map(String))!==JSON.stringify([0n,0n,...E].map(String)))throw Error("discriminant");
const p=103,md=x=>((x%p)+p)%p,tm=a=>{a=a.slice();while(a.length>1&&!a.at(-1))a.pop();return a};
const ad=(a,b)=>tm(Array.from({length:Math.max(a.length,b.length)},(_,i)=>md((a[i]||0)+(b[i]||0)))),ng=a=>a.map(x=>md(-x)),su=(a,b)=>ad(a,ng(b));
const ml=(a,b)=>{let o=Array(a.length+b.length-1).fill(0);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)o[i+j]=md(o[i+j]+a[i]*b[j]);return tm(o)};
const iv=x=>{let y=1,n=p-2,a=md(x);while(n){if(n%2)y=y*a%p;a=a*a%p;n=Math.floor(n/2)}return y};
function dv(a,b){a=tm(a);let q=Array(Math.max(1,a.length-b.length+1)).fill(0);while(a.length>=b.length&&a.some(x=>x)){let c=md(a.at(-1)*iv(b.at(-1))),m=a.length-b.length;q[m]=md(q[m]+c);a=su(a,Array(m).fill(0).concat(b.map(x=>md(x*c))))}return[q,a]}
let f=E.map(x=>Number((x%103n+103n)%103n)),g=f.slice(1).map((x,i)=>md(x*(i+1))),r0=f,r1=g,s0=[1],s1=[0],t0=[0],t1=[1];
while(r1.some(x=>x)){const[q,r]=dv(r0,r1);[r0,r1]=[r1,r];[s0,s1]=[s1,su(s0,ml(q,s1))];[t0,t1]=[t1,su(t0,ml(q,t1))]}
const unit=iv(r0[0]);s0=s0.map(x=>md(x*unit));t0=t0.map(x=>md(x*unit));const check=ad(ml(s0,f),ml(t0,g));if(check.length!==1||check[0]!==1)throw Error("Bezout");

function equal(a,b,label){if(JSON.stringify(trim(a).map(String))!==JSON.stringify(trim(b).map(String)))throw Error(label);}
equal(sc([-8n,22n,-15n,1n],9n),add(mul([6n,-17n,3n],[-28n,3n]),[96n,-296n]),"s=2 remainder");
equal(sc([168n,166n,33n,1n],5n),add(mul([66n,65n,5n],[20n,1n]),[-480n,-536n]),"s=-6 remainder");
const ev=(p,x)=>p.reduceRight((a,c)=>a*x+c,0n);
if(ev([0n,0n,0n,-32n,5n,-1n],5n)!==-4000n)throw Error("s0");
if(ev([5n,5n,5n],-1n)!==5n)throw Error("infinity");
if(17n**2n-4n*3n*6n!==217n||65n**2n-4n*5n*66n!==2905n)throw Error("quadratic discriminants");
function det(M){if(M.length===1)return M[0][0];return M[0].reduce((o,x,j)=>o+(j%2?-x:x)*det(M.slice(1).map(r=>r.filter((_,k)=>k!==j))),0n)}
if(det([[0n,0n,-5n,1n],[0n,22n,-3n,1n],[-5n,-3n,-3n,0n],[1n,1n,0n,0n]])!==70n)throw Error("q pairing determinant");
return{E8:E.map(String),modulus:p,U:s0,V:t0,bezout:check,E8_minus_one:E.reduce((a,c,i)=>a+c*(i%2?-1n:1n),0n).toString(),
special_remainders:{s2:"(-296z+96)/9",sminus6:"(-536z-480)/5"},s0_p1_at_5:"-4000",sinfty_p1_at_minus1:"5"};
}

if(typeof module!=="undefined")module.exports={verify};
if(typeof require!=="undefined"&&require.main===module)process.stdout.write(JSON.stringify(verify(),null,2)+"\n");
