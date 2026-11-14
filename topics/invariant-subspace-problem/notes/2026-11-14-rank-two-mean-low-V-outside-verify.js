function verifyRankTwoLowVOutsideIdentities() {
 const Z=()=>new Map(),co=n=>new Map(n?[[0,BigInt(n)]]:[]),v=i=>new Map([[16**i,1n]]),add=(a,b,s=1n)=>{let o=new Map(a);for(let[k,c]of b){let z=(o.get(k)||0n)+s*c;if(z)o.set(k,z);else o.delete(k)}return o},sc=(a,s)=>add(Z(),a,BigInt(s)),mul=(a,b)=>{let o=Z();for(let[k,c]of a)for(let[l,d]of b){let z=(o.get(k+l)||0n)+c*d;if(z)o.set(k+l,z);else o.delete(k+l)}return o},sq=a=>mul(a,a),cu=a=>mul(sq(a),a);
 let x=v(0),z=v(1),k=v(2),D=add(co(3),k,-2n),w=add(mul(k,x),mul(add(co(1),k,-1n),z),-1n);
 let reduced=add(add(mul(mul(D,sq(k)),cu(add(x,z))),sc(mul(mul(k,add(x,z)),add(mul(k,sq(x)),mul(add(co(2),k,-1n),sq(z)))),-3)),cu(z),2n);
 const reducedCube=add(reduced,cu(w),2n).size===0;
 let yy=v(0),ell=v(1);const doubleCube=add(add(add(cu(yy),sc(mul(yy,add(mul(yy,ell),sq(ell),-1n)),-3)),cu(ell),-1n),cu(add(yy,ell,-1n)),-1n).size===0;
 let [xx,u0,u1,u2,b,eta0,eta1]=Array.from({length:7},(_,i)=>v(i)),mean=add(xx,mul(b,u0));
 let sixH=add(add(sq(xx),mul(add(sc(eta1,12),sq(b),-1n),sq(u0))),sc(mul(mul(b,u0),u1),4));
 let fourV=add(add(sc(mul(eta0,cu(u0)),4),sc(mul(mul(eta1,sq(u0)),u1),12)),sc(mul(b,add(mul(sq(u0),u2),mul(u0,sq(u1)))),2));
 let actual=add(add(cu(mean),mul(mean,sixH),-1n),fourV);
 let tail=add(add(sc(mul(b,u2),2),mul(add(sc(eta1,12),sq(b),-4n),add(u1,xx,-1n))),mul(add(add(sc(cu(b),2),sc(mul(b,eta1),-12)),sc(eta0,4)),u0));
 let expect=mul(u0,add(sc(mul(b,sq(add(u1,xx,-1n))),2),mul(u0,tail)));
 const tripleConic=add(actual,expect,-1n).size===0;
 return{checks:{"reduced mean block cube after clearing k^2(3-2k)":reducedCube,"double mean block cube":doubleCube,"triple V at shared reduced-mean point conic factor":tripleConic},all:reducedCube&&doubleCube&&tripleConic};
}
const result=verifyRankTwoLowVOutsideIdentities();
if(!result.all) throw new Error('Exact rank-two low-V outside identities failed');
console.log(JSON.stringify(result,null,2));
