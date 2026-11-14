function verifyOrthogonalMeanReduction() {
 const Z=()=>new Map(),v=i=>new Map([[16**i,1n]]),add=(a,b,s=1n)=>{let o=new Map(a);for(let[k,x]of b){let z=(o.get(k)||0n)+s*x;if(z)o.set(k,z);else o.delete(k)}return o},sc=(a,s)=>add(Z(),a,BigInt(s)),mul=(a,b)=>{let o=Z();for(let[k,x]of a)for(let[l,y]of b){let z=(o.get(k+l)||0n)+x*y;if(z)o.set(k+l,z);else o.delete(k+l)}return o},sq=a=>mul(a,a);
 const[f,A,B,c,d,e,r,s]=Array.from({length:8},(_,i)=>v(i)),tr=add(add(f,A),B),K=[[f,d,e],[d,A,c],[e,c,B]];
 const P=[add(B,A,-1n),sc(add(d,mul(r,A)),-2),sc(add(e,mul(s,B),-1n),2)];
 const KK=K.map(row=>K.map((_,j)=>row.reduce((a,x,k)=>add(a,mul(x,K[k][j])),Z())));
 const Q4=add(P.reduce((a,x)=>add(a,sq(x)),Z()),sc(add(add(add(add(add(mul(f,A),mul(f,B)),mul(A,B)),sq(d),-1n),sq(e),-1n),sq(c),-1n),4));
 const g08=add(add(add(sq(P[1]),sq(P[2]),-1n),sc(add(KK[1][1],KK[2][2],-1n),-4)),sc(mul(tr,P[0]),-4));
 const g14=add(add(add(mul(P[0],P[1]),KK[0][1],-4n),mul(r,add(sq(P[1]),KK[1][1],-4n))),mul(tr,P[1]),-2n);
 const g24=add(add(add(sc(mul(P[0],P[2]),-1),KK[0][2],4n),mul(s,add(sq(P[2]),KK[2][2],-4n))),mul(tr,P[2]),-2n);
 const Z8=add(sc(sq(c),4),sq(add(A,B)),-1n);
 const R18=add(add(add(sc(mul(A,f),8),sc(mul(sq(r),sq(A)),8)),sc(mul(mul(r,A),d),16)),Z8,-1n);
 const R28=add(add(add(sc(mul(B,f),8),sc(mul(sq(s),sq(B)),8)),sc(mul(mul(s,B),e),-16)),Z8,-1n);
 const L18=add(add(add(sc(mul(add(A,B),d),4),sc(mul(c,e),-8)),mul(r,Z8),-1n),sc(mul(r,add(sq(A),sq(B),-1n)),2));
 const L28=add(add(add(sc(mul(c,d),8),sc(mul(add(A,B),e),-4)),mul(s,Z8),-1n),sc(mul(s,add(sq(A),sq(B),-1n)),-2));
 const checks={
 "8R1=4Q+8g0":add(R18,add(Q4,g08),-1n).size===0,
 "8R2=4Q-8g0":add(R28,add(Q4,g08,-1n),-1n).size===0,
 "8g1=r(8R1)+8L1":add(sc(g14,2),add(mul(r,R18),L18),-1n).size===0,
 "8g2=s(8R2)+8L2":add(sc(g24,2),add(mul(s,R28),L28),-1n).size===0};
 return {checks,all:Object.values(checks).every(Boolean)};
}
const result=verifyOrthogonalMeanReduction();
if(!result.all) throw new Error('Exact orthogonal mean reduction failed');
console.log(JSON.stringify(result,null,2));
