
"use strict";
function algebra(n){
const z=()=>new Map(),con=x=>new Map(x?[["0".repeat(n),BigInt(x)]]:[]),v=i=>new Map([[Array.from({length:n},(_,j)=>i===j?"1":"0").join(""),1n]]);
const add=(...ps)=>{const r=z();for(const p of ps)for(const[k,c]of p)r.set(k,(r.get(k)||0n)+c);return new Map([...r].filter(([k,c])=>c))},sc=(p,c)=>new Map([...p].map(([k,a])=>[k,a*BigInt(c)]).filter(([k,a])=>a)),mul=(p,q)=>{const r=z();for(const[k,a]of p)for(const[l,b]of q){const key=[...k].map((x,i)=>(parseInt(x,36)+parseInt(l[i],36)).toString(36)).join("");r.set(key,(r.get(key)||0n)+a*b)}return new Map([...r].filter(([k,c])=>c))};
return{z,con,v,add,sc,mul};
}

function verify(){
const{con,v,add,sc,mul}=algebra(15),[x0,x1,x2,x3,z0,z1,a,b,h0,h1,c,e0,e1,k0,t0]=Array.from({length:15},(_,i)=>v(i)),sq=p=>mul(p,p),cube=p=>mul(sq(p),p);let count=0;
function equal(x,y,name){if(add(x,sc(y,-1)).size)throw Error(name);count++;}
let yy=add(mul(a,x0),mul(b,x1)),H=add(mul(h0,sq(x0)),sc(mul(mul(h1,x0),x1),2),mul(c,add(sc(mul(x0,x2),2),sq(x1))));
let V2=add(sc(mul(e0,cube(x0)),2),sc(mul(mul(e1,sq(x0)),x1),6),sc(mul(mul(c,a),add(mul(sq(x0),x2),mul(x0,sq(x1)))),6),mul(mul(c,b),add(sc(mul(sq(x0),x3),3),sc(mul(mul(x0,x1),x2),6),cube(x1))));
let lhs=add(sc(cube(yy),2),sc(mul(yy,H),-12),sc(V2,4));
const A=add(cube(a),sc(mul(a,h0),-6),sc(e0,4)),B=add(sc(mul(sq(a),b),3),sc(mul(b,h0),-6),sc(mul(a,h1),-12),sc(e1,12)),C=add(sc(mul(a,sq(b)),3),sc(mul(b,h1),-12),sc(mul(a,c),6)),D=mul(b,add(sq(b),sc(c,-4)));
let rhs=sc(add(sc(mul(mul(mul(c,b),sq(x0)),x3),6),mul(D,cube(x1)),mul(C,mul(x0,sq(x1))),mul(B,mul(sq(x0),x1)),mul(A,cube(x0))),2);
equal(lhs,rhs,"inside doubled tangent mean fourth jet");
yy=add(mul(a,x0),mul(b,z0));
H=add(mul(h0,sq(x0)),sc(mul(mul(mul(c,a),x0),x1),2),mul(k0,sq(z0)),sc(mul(mul(mul(c,b),z0),z1),-2));
const V=add(mul(e0,cube(x0)),sc(mul(mul(mul(c,sq(a)),sq(x0)),x1),3),mul(t0,cube(z0)),sc(mul(mul(mul(c,sq(b)),sq(z0)),z1),-3));
lhs=add(cube(yy),sc(mul(yy,H),-6),sc(V,4));
rhs=add(sc(mul(mul(mul(mul(c,a),b),mul(x0,z0)),add(z1,sc(x1,-1))),12),
mul(add(cube(a),sc(mul(a,h0),-6),sc(e0,4)),cube(x0)),
mul(add(sc(mul(sq(a),b),3),sc(mul(b,h0),-6)),mul(sq(x0),z0)),
mul(add(sc(mul(a,sq(b)),3),sc(mul(a,k0),-6)),mul(x0,sq(z0))),
mul(add(cube(b),sc(mul(b,k0),-6),sc(t0,4)),cube(z0)));
equal(lhs,rhs,"inside doubled reduced mean two double jets");
return{status:"exact",identities:count,coefficient_ring:"integer polynomial ring; BigInt arithmetic",scope:"The full fourth-jet and two-double-jet third tensor identities."};
}
if(typeof module!=="undefined")module.exports={verify};
if(typeof require!=="undefined"&&require.main===module)process.stdout.write(JSON.stringify(verify(),null,2)+"\n");
