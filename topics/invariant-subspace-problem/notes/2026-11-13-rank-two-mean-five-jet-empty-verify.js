
"use strict";
function verify(){
 const n=9,zero="0".repeat(n),mon=(i)=>new Map([[Array.from({length:n},(_,j)=>i===j?"1":"0").join(""),1n]]),con=x=>new Map(x?[[zero,BigInt(x)]]:[]),add=(...ps)=>{const q=new Map();for(const p of ps)for(const[k,c]of p)q.set(k,(q.get(k)||0n)+c);return new Map([...q].filter(([k,c])=>c))},sc=(p,a)=>new Map([...p].map(([k,c])=>[k,c*BigInt(a)])),mul=(p,q)=>{let r=new Map();for(const[k,a]of p)for(const[l,b]of q){const key=[...k].map((c,i)=>String(Number(c)+Number(l[i]))).join("");r.set(key,(r.get(key)||0n)+a*b)}return new Map([...r].filter(([k,c])=>c))};
 const[x0,x1,x2,x3,w,a,h,c,k]=Array.from({length:n},(_,i)=>mon(i)),sq=p=>mul(p,p),cube=p=>mul(sq(p),p),y=add(mul(a,x0),x1);
 const H4=add(sc(mul(h,sq(x0)),8),sc(mul(mul(a,x0),x1),2),sc(mul(x0,x2),2),sq(x1));
 const V8=add(sc(mul(c,cube(x0)),8),sc(mul(mul(h,sq(x0)),x1),24),sc(mul(a,add(mul(sq(x0),x2),mul(x0,sq(x1)))),3),sc(mul(sq(x0),x3),3),sc(mul(mul(x0,x1),x2),6),cube(x1),sc(mul(k,cube(w)),8));
 const lhs=add(sc(cube(y),8),sc(mul(y,H4),-12),sc(V8,4));
 const rhs=add(mul(sq(x0),add(mul(add(sc(cube(a),8),sc(mul(a,h),-96),sc(c,32)),x0),sc(mul(a,x2),-12),sc(x3,12))),sc(mul(k,cube(w)),32));
 const diff=add(lhs,sc(rhs,-1));if(diff.size)throw Error("four-jet cubic identity");
 return {status:"exact",coefficient_ring:"Z[x0,x1,x2,x3,w,a,h,c,k]",checked:"8T3=x0^2[(8a^3-96ah+32c)x0-12ax2+12x3]+32kw^3",residual_terms:diff.size};
}
if(typeof module!=="undefined")module.exports={verify};
if(typeof require!=="undefined"&&require.main===module)process.stdout.write(JSON.stringify(verify(),null,2)+"\n");
