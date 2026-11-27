"use strict";
const began=Date.now(),D=7,ZKEY="0,0,0,0,0,0,0";let products=0;
function C(n=0n){return n===0n?new Map():new Map([[ZKEY,n]])}
function V(i){const a=Array(D).fill(0);a[i]=1;return new Map([[a.join(","),1n]])}
function add(a,b){const c=new Map(a);for(const[k,v]of b){let x=(c.get(k)||0n)+v;if(x)c.set(k,x);else c.delete(k)}return c}
function neg(a){return new Map([...a].map(([k,v])=>[k,-v]))}
function sub(a,b){return add(a,neg(b))}
function mul(a,b){products++;const c=new Map();for(const[ka,va]of a){const ea=ka.split(",").map(Number);for(const[kb,vb]of b){const eb=kb.split(",").map(Number),k=ea.map((x,i)=>x+eb[i]).join(","),x=(c.get(k)||0n)+va*vb;if(x)c.set(k,x);else c.delete(k)}}return c}
function sc(a,n){return mul(a,C(BigInt(n)))}
function sq(a){return mul(a,a)}
function sum(xs){return xs.reduce(add,C())}
function prod(xs){return xs.reduce(mul,C(1n))}
const [b,c,r,f,X,Y,t]=Array.from({length:D},(_,i)=>V(i));
const one=C(1n),ell=add(b,c),a=sub(one,ell),diff=sub(b,c);
const p=add(one,r),q=sub(one,r),Q=sub(one,sq(r)),bc=mul(b,c);
const u=add(mul(b,p),mul(c,q)),V2=add(mul(b,sq(p)),mul(c,sq(q))),T0=sub(V2,sc(sq(u),2));
const vv=add(mul(b,X),mul(c,Y)),ud=sub(mul(b,X),mul(c,Y));
const AA=sum([sc(f,2),sc(mul(b,X),-2),sc(mul(c,Y),-2),sc(mul(bc,t),2)]);
const rg=sub(sub(X,mul(a,p)),mul(c,t)),sg=sub(sub(Y,mul(a,q)),mul(b,t));
const zero=C();
const rows=[[zero,zero,p,q],[zero,AA,rg,sg],[p,rg,zero,t],[q,sg,t,zero]];
const unit=[one,zero,one,one];
function vm(v,w){return[mul(v[0],w[0]),add(mul(v[0],w[1]),mul(v[1],w[0])),mul(v[2],w[2]),mul(v[3],w[3])]}
function tau(v){return sum([mul(a,v[0]),v[1],mul(b,v[2]),mul(c,v[3])])}
function DK(v){return rows.map(row=>tau(vm(row,v)))}
const dv=DK(unit),F2=tau(dv),Kd=DK(dv);
const checks=[];
function check(name,poly){if(poly.size)throw Error(name+": "+poly.size+" nonzero terms");checks.push({name,fullIntegerPolynomialDifferenceZero:true})}
check("raw_original_F2",sub(F2,sc(f,2)));
function mean(j){const ee=j===1?sc(tau(vm(rows[0],rows[1])),2):tau(vm(rows[j],rows[j]));return sum([ee,sc(Kd[j],-2),sc(sq(dv[j]),-2),sc(mul(F2,dv[j]),2)])}
const E0=mean(0),E1=mean(1),EB=mean(2),EC=mean(3),EW=add(mul(b,EB),mul(c,EC));
const W1=add(mul(mul(b,p),X),mul(mul(c,q),Y));
check("raw_original_E0",sub(E0,sum([T0,sc(W1,-2),sc(mul(u,f),4)])));
const vn=mul(Q,vv),z=mul(Q,t),wn2=sum([mul(Q,T0),sc(prod([Q,u,f]),4),sc(vn,-2)]);
const Ainside=sum([sq(add(vn,prod([a,u,Q]))),sc(prod([u,Q,vn]),-2),
 sc(prod([a,sq(u),sq(Q)]),2),sc(prod([a,u,f,sq(Q)]),-4),
 mul(bc,sq(z)),mul(z,sub(sc(prod([bc,u,Q]),4),mul(ell,vn)))]);
const R2=add(sc(mul(r,Ainside),2),prod([diff,z,wn2]));
const W4=sum([sc(prod([bc,sq(r),sq(Q),ell,T0]),8),
 sc(prod([ell,sq(r),sq(vn)]),-4),neg(mul(ell,sq(wn2))),
 sc(prod([diff,r,vn,wn2]),4),sc(prod([bc,sq(r),Q,f,vn]),32),
 sc(prod([sq(bc),sq(r),sq(z)]),16),
 sc(prod([sq(bc),sq(r),Q,sub(u,one),z]),32),
 sc(prod([bc,ell,sq(r),z,vn]),-8),sc(prod([bc,diff,r,z,wn2]),4)]);
check("new_compact_R2_original_mean_identity",
 sum([R2,prod([r,sq(Q),sub(E1,EW)]),
      neg(prod([sq(Q),sub(mul(diff,t),mul(a,r)),E0]))]));
const correction=sum([sc(mul(bc,sq(r)),2),prod([bc,r,diff,t]),
                       neg(mul(r,sub(mul(ell,ud),mul(diff,vv))))]);
check("new_compact_W4_original_mean_identity",
 sum([W4,sc(prod([bc,sq(r),sq(Q),EW]),-8),
      sc(prod([sq(Q),E0,correction]),-4),
      prod([ell,sq(Q),sq(E0)])]));
return {schema:"isp-new-compact-original-two-means-integer-return-v1",
 variables:["b","c","rho","f","X","Y","t"],elapsed_milliseconds:Date.now()-began,
 integerPolynomialProducts:products,checks,
 compactR2ExpandedTerms:R2.size,compactW4ExpandedTerms:W4.size,
 actualExecution:"pure V8 BigInt exact integer polynomial arithmetic",
 noPhiOrUnpaidNormAssumption:true,noNewExclusionClaim:true};
