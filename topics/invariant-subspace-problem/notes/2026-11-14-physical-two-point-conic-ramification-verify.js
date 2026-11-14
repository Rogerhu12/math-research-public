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



function algebra(n){
const z=()=>new Map(),con=x=>new Map(x?[["0".repeat(n),BigInt(x)]]:[]),v=i=>new Map([[Array.from({length:n},(_,j)=>i===j?"1":"0").join(""),1n]]);
const add=(...ps)=>{const r=z();for(const p of ps)for(const[k,c]of p)r.set(k,(r.get(k)||0n)+c);return new Map([...r].filter(([k,c])=>c))},sc=(p,c)=>new Map([...p].map(([k,a])=>[k,a*BigInt(c)]).filter(([k,a])=>a)),mul=(p,q)=>{const r=z();for(const[k,a]of p)for(const[l,b]of q){const key=[...k].map((x,i)=>(parseInt(x,36)+parseInt(l[i],36)).toString(36)).join("");r.set(key,(r.get(key)||0n)+a*b)}return new Map([...r].filter(([k,c])=>c))};
return{z,con,v,add,sc,mul};
}


function verify(){
 let identities=0;
 {
 const B=algebra(3),{con,v,add:ad,sc:scale,mul:times}=B;
 const [s,r,t]=[v(0),v(1),v(2)],sq=x=>times(x,x),cube=x=>times(sq(x),x);
 const equal=(a,b)=>{if(ad(a,scale(b,-1)).size)throw Error("Kernel/symmetric identity");identities++};
 const K=[[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],
 [0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]];
 const rp=[con(1)],tp=[con(1)];for(let i=1;i<6;i++){rp.push(times(rp[i-1],r));tp.push(times(tp[i-1],t));}
 let kp=con(0);for(let i=0;i<6;i++)for(let j=0;j<6;j++)kp=ad(kp,scale(times(rp[i],tp[j]),K[i][j]));
 const q=(a,b)=>ad(times(ad(a,con(1)),cube(b)),times(ad(scale(sq(a),-3),scale(a,-3),con(-5)),sq(b)),
 times(ad(cube(a),scale(sq(a),-3),scale(a,22)),b),cube(a),scale(sq(a),-5));
 equal(kp,scale(times(sq(ad(t,scale(r,-1))),q(r,t)),-1));
 const x=ad(r,t),y=times(r,t);
 const Ar=ad(r,con(1)),Br=ad(scale(sq(r),-3),scale(r,-3),con(-5)),Cr=ad(cube(r),scale(sq(r),-3),scale(r,22));
 const Jr=ad(scale(Cr,2),times(ad(scale(s,2),x),Br),
 times(ad(scale(sq(s),2),times(s,x),scale(y,2)),Ar));
 const Qx=ad(sq(x),times(ad(con(9),scale(s,5)),x),scale(sq(s),-2),scale(s,6),con(-44));
 const Bx=ad(times(ad(x,con(8),scale(s,6)),y),scale(sq(s),2),scale(s,-10),times(ad(s,con(-5)),x));
 equal(Jr,ad(scale(times(Qx,r),-1),Bx));
 }
 const A=[1n,1n],B=[-5n,-3n,-3n],C=[0n,22n,-3n,1n],D=[0n,0n,-5n,1n];
 const S=[9n,5n],R=[44n,-6n,2n];
 const P=add(C,mul(A,R)),Q=sub(mul(A,S),B);
 const L=add(P,add(mul(Q,[1n,-1n]),mul(A,[-5n,1n])));
 const C0=add(neg(mul(Q,R)),add(mul([8n,6n],P),mul(A,[0n,-10n,2n])));
 const M=neg(add(mul(A,P),mul(Q,Q)));
 const N=add(sub(mul(A,D),mul(B,P)),mul(mul(A,Q),R));
 const E=sub(mul(L,N),mul(M,C0));
 const fourT=sub(sub(mul(C0,C0),mul(mul(S,C0),L)),mul(R,mul(L,L)));
 const EE=[-19052,3740,48306,43596,8939,-2244,1242,72,9].map(BigInt);
 const TT=[18007,-29632,-19492,11840,-744,-336,124,8,1].map(BigInt);
 const equal=(a,b)=>{if(sub(a,b).some(x=>x))throw Error("Univariate identity");identities++};
 equal(E,EE);equal(fourT,sc(TT,4n));
 equal(L,[53n,59n,-15n,-5n]);equal(C0,[-264n,70n,18n,-2n,2n]);
 equal(M,[-240n,-580n,-566n,-268n,-67n]);equal(N,[836n,1712n,1214n,434n,-9n,25n]);
 const U=[73,46,75,98,37,70,33,32].map(BigInt),V=[35,28,17,78,24,76,12,21].map(BigInt);
 const md=x=>(x%103n+103n)%103n,check=trim(add(mul(U,E),mul(V,TT)).map(md));
 equal(check,[1n]);
 if(E.length!==9||TT.length!==9||md(E.at(-1))!==9n||md(TT.at(-1))!==1n)throw Error("Degree loss");
 return {status:"PASS",original_K_reconstructed:true,exact_identities:identities,
 L:L.map(String),C0:C0.map(String),M:M.map(String),N:N.map(String),
 E:E.map(String),T:TT.map(String),prime:103,U:U.map(String),V:V.map(String),
 bezout:check.map(String),retained_degrees:[8,8],retained_leading_coefficients:[9,1]};
}
if(typeof module!=="undefined")module.exports={verify};
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module)
 process.stdout.write(JSON.stringify(verify(),null,2)+"\n");
