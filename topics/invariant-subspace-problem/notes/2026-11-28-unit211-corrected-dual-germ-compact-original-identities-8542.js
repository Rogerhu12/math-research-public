"use strict";
// NEW definition correction: the dual-number square in the germ coordinate.
// Original immutable compact source is retained separately; no previous identity is silently rewritten.
const began=Date.now(),D=7,ZKEY="0,0,0,0,0,0,0";let products=0;
function C(n=0n){return n===0n?new Map():new Map([[ZKEY,n]])}
function V(i){const a=Array(D).fill(0);a[i]=1;return new Map([[a.join(","),1n]])}
function add(a,b){const c=new Map(a);for(const[k,v]of b){let x=(c.get(k)||0n)+v;if(x)c.set(k,x);else c.delete(k)}return c}
function neg(a){return new Map([...a].map(([k,v])=>[k,-v]))}
function sub(a,b){return add(a,neg(b))}
function mul(a,b){if(Date.now()-began>120000)throw Error("new corrected original identity 120 second budget");products++;const c=new Map();for(const[ka,va]of a){const ea=ka.split(",").map(Number);for(const[kb,vb]of b){const eb=kb.split(",").map(Number),k=ea.map((x,i)=>x+eb[i]).join(","),x=(c.get(k)||0n)+va*vb;if(x)c.set(k,x);else c.delete(k)}}return c}
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
const dvSquare=vm(dv,dv);
function mean(j){const ee=j===1?sc(tau(vm(rows[0],rows[1])),2):tau(vm(rows[j],rows[j]));return sum([ee,sc(Kd[j],-2),sc(dvSquare[j],-2),sc(mul(F2,dv[j]),2)])}
const E0=mean(0),E1=mean(1),EB=mean(2),EC=mean(3),EW=add(mul(b,EB),mul(c,EC));
const W1=add(mul(mul(b,p),X),mul(mul(c,q),Y));
check("raw_original_E0",sub(E0,sum([T0,sc(W1,-2),sc(mul(u,f),4)])));
const vn=mul(Q,vv),z=mul(Q,t),wn2=sum([mul(Q,T0),sc(prod([Q,u,f]),4),sc(vn,-2)]);
const Ainside=sum([sq(add(vn,prod([a,u,Q]))),sc(prod([u,Q,vn]),-2),
 sc(prod([a,sq(u),sq(Q)]),2),sc(prod([a,u,f,sq(Q)]),-4),
 mul(bc,sq(z)),mul(z,sub(sc(prod([bc,u,Q]),4),mul(ell,vn)))]);
const R2bad=add(sc(mul(r,Ainside),2),prod([diff,z,wn2]));
// d0=u and d1=2f-V-(1-ell)u follow from this SAME original Gram.
check("same_original_germ_d0",sub(dv[0],u));
check("same_original_germ_d1",sub(dv[1],sub(sub(sc(f,2),vv),mul(a,u))));
const deltaE=sub(sc(mul(u,dv[1]),4),sc(sq(dv[1]),2));
const E1bad=sum([sc(tau(vm(rows[0],rows[1])),2),sc(Kd[1],-2),
                sc(sq(dv[1]),-2),sc(mul(F2,dv[1]),2)]);
check("old_minus_correct_germ_mean_exact_difference",sub(sub(E1bad,E1),deltaE));
const jn=sub(sub(sc(mul(Q,f),2),vn),prod([a,u,Q]));
check("corrected_germ_scalar_jn_definition",sub(jn,mul(Q,dv[1])));
const correctedInside=sum([
 sc(prod([Q,sub(f,u),sub(vn,mul(Q,f))]),4),
 mul(bc,sq(z)),mul(z,sub(sc(prod([bc,u,Q]),4),mul(ell,vn)))]);
const R2=add(sc(mul(r,correctedInside),2),prod([diff,z,wn2]));
check("corrected_R2_exact_old_formula_difference",
 sub(R2,add(R2bad,prod([r,sq(Q),deltaE]))));
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

const vrow=rows[0],zrow=rows[1],tv=tau(vrow),tz=tau(zrow);
const Nv=sum([
 sc(tau(vm(dv,vm(vrow,zrow))),4),
 sc(mul(F2,tau(vm(vrow,zrow))),-2),
 sc(add(mul(tv,tau(vm(dv,zrow))),mul(tz,tau(vm(dv,vrow)))),-4),
 sc(prod([F2,tv,tz]),4),tau(vm(vrow,DK(zrow))),tau(vm(zrow,DK(vrow)))
]);
const wnActual=sc(mul(Q,sub(W1,vv)),2),wOneActual=sc(W1,2);
const al=sub(mul(ell,sub(one,u)),mul(r,diff));
const be=sub(mul(r,ell),mul(diff,sub(one,u)));
const AV=add(mul(sub(sc(u,2),one),ell),sc(mul(r,diff),3));
const BU=add(mul(sub(sc(u,2),one),diff),sc(mul(r,ell),3));
const Ncompact=sum([
 mul(al,add(sc(prod([sq(r),sq(vn)]),4),sq(wnActual))),
 sc(prod([be,r,vn,wnActual]),4),
 sc(prod([bc,sq(r),Q,vn,wOneActual]),8),
 sc(prod([bc,sq(r),sq(Q),f,wOneActual]),-24),
 sc(prod([a,bc,sq(r),sq(Q),sub(u,one),wOneActual]),16),
 sc(prod([bc,sq(r),sq(Q),u,sq(f)]),64),
 sc(prod([bc,sq(r),Q,u,f,vn]),-32),
 sc(prod([bc,sq(r),sq(Q),add(one,a),T0,f]),16),
 sc(prod([bc,sq(r),Q,sub(mul(a,Q),T0),vn]),16),
 sc(prod([bc,sq(r),AV,z,vn]),4),
 sc(prod([bc,r,BU,z,wnActual]),-2),
 sc(prod([sq(bc),sq(r),Q,z,sum([sc(f,2),T0,neg(mul(a,Q))])]),16),
 sc(prod([u,sq(bc),sq(r),sq(z)]),-8)
]);
check("new_compact_original_N1_polarized_Nv_identity",
 sub(Ncompact,sc(prod([bc,sq(r),sq(Q),Nv]),4)));

const SS=sub(sc(prod([r,ell,vn]),2),mul(diff,wnActual));
const DD=add(sc(prod([r,diff,vn]),-2),mul(ell,wnActual));
const r3=mul(sq(r),r);
const Ocompact=sum([
 sc(prod([sq(bc),a,sq(Q),r3,sub(u,one)]),32),
 sc(prod([bc,Q,sq(r),SS]),4),
 sc(prod([sq(bc),Q,r3,vn]),32),
 sc(prod([sq(bc),sq(Q),r3,f]),-64),
 sc(prod([bc,Q,r,sum([one,neg(u),sc(f,2)]),DD]),4),
 neg(mul(SS,DD)),
 sc(prod([sq(bc),sq(r),diff,sq(z)]),-8),
 sc(prod([sq(bc),Q,sq(r),z,add(mul(diff,sub(u,one)),mul(ell,r))]),-16),
 sc(prod([sq(bc),r,z,wnActual]),8)
]);
check("new_compact_original_EB_minus_EC_identity",
 sub(Ocompact,sc(prod([sq(bc),sq(Q),sq(r),sub(EB,EC)]),8)));
return {schema:"isp-corrected-dual-germ-compact-all-original-means-and-N1-v1",
 variables:["b","c","rho","f","X","Y","t"],elapsed_milliseconds:Date.now()-began,
 integerPolynomialProducts:products,checks,compactR2ExpandedTerms:R2.size,
 compactW4ExpandedTerms:W4.size,compactNvExpandedTerms:Ncompact.size,
 compactEBminusECExpandedTerms:Ocompact.size,
 actualExecution:"pure V8 BigInt exact integer polynomial arithmetic",
 wrongSourceBlob:"94b2be74c729ee76e239491d8e967dc9c41044b0",
 originalGermSquare:"vm(dv,dv)[1]=2*dv[0]*dv[1]",
 oldWrongGermSquare:"sq(dv[1])",
 correctedOnlyMeanIndex:1,oldR2OriginalNecessityRetracted:true,
 W4OcompactNcompactOriginalIdentitiesRetained:true,
 NvNormalization:"polarization of original N4",noPhiOrUnpaidNormAssumption:true,
 noNewExclusionClaim:true};
