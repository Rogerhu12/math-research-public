
"use strict";
function algebra(n){
const z=()=>new Map(),con=x=>new Map(x?[["0".repeat(n),BigInt(x)]]:[]),v=i=>new Map([[Array.from({length:n},(_,j)=>i===j?"1":"0").join(""),1n]]);
const add=(...ps)=>{const r=z();for(const p of ps)for(const[k,c]of p)r.set(k,(r.get(k)||0n)+c);return new Map([...r].filter(([k,c])=>c))},sc=(p,c)=>new Map([...p].map(([k,a])=>[k,a*BigInt(c)]).filter(([k,a])=>a)),mul=(p,q)=>{const r=z();for(const[k,a]of p)for(const[l,b]of q){const key=[...k].map((x,i)=>(parseInt(x,36)+parseInt(l[i],36)).toString(36)).join("");r.set(key,(r.get(key)||0n)+a*b)}return new Map([...r].filter(([k,c])=>c))};
return{z,con,v,add,sc,mul};
}
function verify(){
const{con,v,add,sc,mul}=algebra(13),[x0,x1,x2,x3,w,z,a,h,vv,c,k,r,kap]=Array.from({length:13},(_,i)=>v(i)),sq=p=>mul(p,p),cube=p=>mul(sq(p),p);let count=0;
function eq(y,H4,V8,rhs,name){const lhs=add(sc(cube(y),8),sc(mul(y,H4),-12),sc(V8,4)),d=add(lhs,sc(rhs,-1));if(d.size)throw Error(name);count++;}
let y=add(mul(a,x0),x1);
let H4=add(mul(add(sc(h,8),sc(mul(a,c),-8)),sq(x0)),mul(add(sc(a,2),sc(c,8)),mul(x0,x1)),sc(mul(x0,x2),2),sq(x1));
let V8=add(sc(mul(vv,cube(x0)),8),sc(mul(mul(h,sq(x0)),x1),24),mul(add(sc(a,3),sc(c,24)),add(mul(sq(x0),x2),mul(x0,sq(x1)))),sc(mul(sq(x0),x3),3),sc(mul(mul(x0,x1),x2),6),cube(x1));
let rhs=mul(sq(x0),add(mul(add(sc(cube(a),8),sc(mul(a,h),-96),sc(mul(sq(a),c),96),sc(vv,32)),x0),mul(add(sc(a,-12),sc(c,96)),x2),sc(x3,12)));
eq(y,H4,V8,rhs,"outside double mean / fourth jet");
y=add(mul(a,x0),w);const cc=add(con(1),sc(c,4)),d=add(w,sc(x1,-1));
H4=add(mul(add(sc(h,8),sc(mul(c,sq(a)),-8)),sq(x0)),sc(mul(mul(a,cc),mul(x0,x1)),2),mul(add(con(1),sc(c,-4)),sq(w)));
V8=add(sc(mul(vv,cube(x0)),8),sc(mul(mul(h,sq(x0)),x1),24),sc(mul(mul(a,cc),add(mul(sq(x0),x2),mul(x0,sq(x1)))),3),mul(add(con(1),sc(c,-12)),cube(w)));
rhs=mul(x0,add(sc(mul(mul(a,cc),sq(d)),12),sc(mul(mul(a,cc),mul(x0,x2)),12),mul(add(sc(mul(sq(a),cc),24),sc(h,-96)),mul(x0,d)),mul(add(sc(mul(cube(a),add(con(1),sc(c,12))),8),sc(mul(a,h),-96),sc(vv,32)),sq(x0))));
eq(y,H4,V8,rhs,"outside reduced mean / third jet / lambda order one");
H4=add(mul(add(sc(mul(k,r),8),sc(sq(a),2)),sq(x0)),sc(sq(w),2));
V8=add(sc(mul(vv,cube(x0)),8),sc(mul(mul(h,sq(x0)),x1),24),sc(mul(k,add(mul(sq(x0),x2),mul(x0,sq(x1)))),24),sc(cube(w),4));
rhs=mul(x0,add(sc(mul(k,sq(x1)),96),sc(mul(mul(k,x0),add(x2,sc(mul(r,w),-1))),96),sc(mul(mul(h,x0),x1),96),mul(add(sc(vv,32),sc(cube(a),-16),sc(mul(mul(a,k),r),-96)),sq(x0))));
eq(y,H4,V8,rhs,"outside reduced mean / third jet / lambda order at least two");
V8=add(sc(mul(vv,cube(x0)),8),sc(mul(mul(k,sq(x0)),x1),24),sc(cube(w),4),sc(mul(kap,cube(z)),8));
rhs=add(mul(sq(x0),add(sc(mul(k,add(x1,sc(mul(r,w),-1))),96),mul(add(sc(vv,32),sc(cube(a),-16),sc(mul(mul(a,k),r),-96)),x0))),sc(mul(kap,cube(z)),32));
eq(y,H4,V8,rhs,"outside reduced mean / double jet plus other point");
return{status:"exact",identities:count,coefficient_ring:"integer polynomial ring, BigInt arithmetic",scope:"The four displayed local normal forms; the geometric exclusions are in the proof."};
}
if(typeof module!=="undefined")module.exports={verify};
if(typeof require!=="undefined"&&require.main===module)process.stdout.write(JSON.stringify(verify(),null,2)+"\n");
