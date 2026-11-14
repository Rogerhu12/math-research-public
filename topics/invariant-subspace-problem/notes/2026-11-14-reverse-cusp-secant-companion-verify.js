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
const K=[[0n,0n,0n,0n,5n,-1n],[0n,0n,0n,-32n,5n,-1n],[0n,0n,54n,-4n,5n,0n],[0n,-32n,-4n,-8n,0n,0n],[5n,5n,5n,0n,0n,0n],[-1n,-1n,0n,0n,0n,0n]];
const S=[[25n,-25n,0n,100n,80n,-2800n],[-25n,25n,0n,-100n,-80n,-400n],[0n,0n,0n,0n,640n,3200n],[100n,-100n,0n,0n,0n,0n],[80n,-80n,640n,0n,-6912n,-34560n],[-2800n,-400n,3200n,0n,-34560n,-172800n]];
const mv=(A,x)=>A.map(r=>r.reduce((a,c,i)=>a+c*x[i],0n));
for(let i=0;i<6;i++)for(let j=0;j<6;j++){let n=0n;for(let k=0;k<6;k++)n+=S[i][k]*K[k][j];if(n!==(i===j?3200n:0n))throw Error("inverse matrix");}
function det(M){if(M.length===1)return M[0][0];return M[0].reduce((o,x,j)=>o+(j%2?-x:x)*det(M.slice(1).map(r=>r.filter((_,k)=>k!==j))),0n)}
const out=[],ss=[0n,2n,-6n],expected=[5910036480n,21064110080n,-169705152000000n];
for(let j=0;j<ss.length;j++){
const s=ss[j],vs=Array.from({length:6},(_,i)=>s**BigInt(i)),p=mv(K,vs),r=div(p,[-s,1n]),co=Array.from({length:6},(_,i)=>r[i]||0n),Y=mv(S,co),Z=Array.from({length:5},(_,i)=>Y[i+1]-s*Y[i]),dd=det(Array.from({length:3},(_,i)=>Array.from({length:3},(_,k)=>Z[i+k])));
if(dd!==expected[j])throw Error("finite determinant");
out.push({s:String(s),companion_polar:co.map(String),Y:Y.map(String),difference_Z:Z.map(String),det:dd.toString()});
}
const pinf=mv(K,[0n,0n,0n,0n,0n,1n]),co=[0n,...pinf.slice(0,5)],Y=mv(S,co),dd=det(Array.from({length:3},(_,i)=>Array.from({length:3},(_,j)=>Y[i+j])));
if(dd!==100000n)throw Error("infinite determinant");
out.push({s:"infinity",companion_polar:co.map(String),Y:Y.map(String),det:dd.toString()});
return{status:"exact",original_inverse_product:"S K=3200 I",cases:out};
}
if(typeof module!=="undefined")module.exports={verify};
if(typeof require!=="undefined"&&require.main===module)process.stdout.write(JSON.stringify(verify(),null,2)+"\n");
