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

function verify(){
 const K=[[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],
 [0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]].map(r=>r.map(BigInt));
 const aa=Array.from({length:6},(_,j)=>K.map(r=>r[j]));
 const bb=aa.map(p=>trim(p.slice(1).map((x,i)=>x*BigInt(i+1))));
 const B=Array.from({length:5},()=>Array.from({length:5},()=>[0n]));
 for(let i=0;i<6;i++)for(let j=0;j<i;j++){
  const c=sub(mul(aa[i],bb[j]),mul(bb[i],aa[j]));
  for(let h=0;h<i-j;h++)B[i-1-h][j+h]=add(B[i-1-h][j+h],c);
 }
 const det3=A=>add(mul(A[0][0],sub(mul(A[1][1],A[2][2]),mul(A[1][2],A[2][1]))),
 neg(mul(A[0][1],sub(mul(A[1][0],A[2][2]),mul(A[1][2],A[2][0])))),
 mul(A[0][2],sub(mul(A[1][0],A[2][1]),mul(A[1][1],A[2][0]))));
 const A=[394752,-1752544,942832,1279992,-197868,-33712,55644,-19962,-1549,3228,575].map(BigInt);
 const C=[3023808,-2140640,-4659536,-1531992,551256,-266844,-91676,109854,14250,-1915,-476].map(BigInt);
 const m1=det3([2,3,4].map(i=>[2,3,4].map(j=>B[i][j])));
 const m2=det3([2,3,4].map(i=>[1,2,3].map(j=>B[i][j])));
 const eq=(a,b)=>{if(sub(a,b).some(x=>x))throw new Error("Integer identity failed")};
 eq(m1,[0n,0n].concat(A));eq(m2,Array(5).fill(0n).concat(C));
 const U=[13,93,91,97,18,31,99,6,26,98].map(BigInt);
 const V=[75,55,24,47,57,47,54,84,59,79].map(BigInt);
 const mod=x=>(x%103n+103n)%103n;
 const identity=trim(add(mul(U,A),mul(V,C)).map(mod));
 eq(identity,[1n]);
 if(mod(A.at(-1))!==60n||mod(C.at(-1))!==39n)throw new Error("Degree changed");
 eq(pgcd([0n,0n,0n,0n,5n,-1n],[0n,0n,0n,-32n,5n,-1n]),[0n,0n,0n,1n]);
 return {status:"PASS",original_K:true,minor_rows:[2,3,4],
 minor_columns:[[2,3,4],[1,2,3]],source_powers:[2,5],
 A:A.map(String),C:C.map(String),prime:103,
 U:U.map(String),V:V.map(String),bezout:identity.map(String),
 retained_degrees:[10,10],exceptional_sources:["0","infinity"],
 exceptional_gcd_degrees:[3,3]};
}
if(typeof module!=="undefined")module.exports={verify};
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module)
 process.stdout.write(JSON.stringify(verify(),null,2)+"\n");
