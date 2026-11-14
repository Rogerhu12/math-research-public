function buildOrthogonalSupportEquations() {
 const Z=()=>new Map(),one=new Map([[0,1n]]),v=i=>new Map([[16**i,1n]]),add=(a,b,s=1n)=>{let o=new Map(a);for(let[k,x]of b){let z=(o.get(k)||0n)+s*x;if(z)o.set(k,z);else o.delete(k)}return o},sc=(a,s)=>add(Z(),a,BigInt(s)),mul=(a,b)=>{let o=Z();for(let[k,x]of a)for(let[l,y]of b){let z=(o.get(k+l)||0n)+x*y;if(z)o.set(k+l,z);else o.delete(k+l)}return o},sq=a=>mul(a,a);
 const[f,a,b,c,d,e,r,s]=Array.from({length:8},(_,i)=>v(i)),K=[[f,d,e],[d,a,c],[e,c,b]],tr=add(add(f,a),b),P=[add(b,a,-1n),sc(add(d,mul(r,a)),-2),sc(add(e,mul(s,b),-1n),2)];
 const all=[];
 for(let group=0;group<2;group++){
  let rho=group?s:r,sign=group?-1:1,col=group?2:1;
  const pa=(A,B,k=1n)=>[add(A[0],B[0],k),add(A[1],B[1],k)],ps=(A,k)=>[sc(A[0],k),sc(A[1],k)];
  const pm=(A,B)=>{let bd=mul(A[1],B[1]);return[add(mul(A[0],B[0]),bd,2n),add(add(mul(A[0],B[1]),mul(A[1],B[0])),mul(rho,bd),2n)]},pq=A=>pm(A,A),pc=A=>pm(pm(A,A),A),cp=x=>[x,Z()];
  let Q=P.map((pi,i)=>[add(pi,K[i][0],BigInt(2*sign)),sc(K[i][col],2)]),R=[add(sc(tr,-2),P[0],BigInt(sign)),P[col]];
  const C=pa(pa(ps(pm(Q[0],pa(pq(Q[1]),pq(Q[2]),-1n)),3),ps(pm(cp(r),pc(Q[1])),2)),ps(pm(cp(s),pc(Q[2])),2));
  let pd=Q.reduce((t,qi,i)=>pa(t,pm(cp(P[i]),qi)),cp(Z())),qnorm=Q.reduce((t,qi)=>pa(t,pq(qi)),cp(Z()));
  let cpq=pa(pa(pa(pm(cp(P[0]),pa(pq(Q[1]),pq(Q[2]),-1n)),ps(pm(cp(P[1]),pm(Q[0],Q[1])),2)),ps(pm(cp(P[2]),pm(Q[0],Q[2])),-2)),pa(ps(pm(cp(mul(r,P[1])),pq(Q[1])),2),ps(pm(cp(mul(s,P[2])),pq(Q[2])),2)));
  let qkq=cp(Z());for(let i=0;i<3;i++)for(let j=0;j<3;j++)qkq=pa(qkq,pm(cp(K[i][j]),pm(Q[i],Q[j])));
  let H=pa(pa(pa(pm(R,pd),cpq),pm(cp(tr),qnorm),-1n),qkq);
  all.push({group,C:C.map(p=>[...p].map(([k,c])=>[k,c.toString()])),H:H.map(p=>[...p].map(([k,c])=>[k,c.toString()]))});
 }
 return {variables:["f","a","b","c","d","e","r","s"],data:all};
}
function specializeHZero(data) {
 const radix=32,Z=()=>new Map(),co=n=>new Map(n?[[0,BigInt(n)]]:[]),v=i=>new Map([[radix**i,1n]]),add=(a,b,s=1n)=>{let o=new Map(a);for(let[k,x]of b){let z=(o.get(k)||0n)+s*x;if(z)o.set(k,z);else o.delete(k)}return o},sc=(a,s)=>add(Z(),a,BigInt(s)),mul=(a,b)=>{let o=Z();for(let[k,x]of a)for(let[l,y]of b){let z=(o.get(k+l)||0n)+x*y;if(z)o.set(k+l,z);else o.delete(k+l)}return o},sq=a=>mul(a,a),pow=(a,n)=>{let o=co(1);for(let i=0;i<n;i++)o=mul(o,a);return o};
 const [q,r,s]=Array.from({length:3},(_,i)=>v(i)),q2=add(sq(r),sq(s)),values=[add(add(sq(s),sq(r),-1n),sc(mul(mul(q,r),s),-2)),co(2),co(-2),sc(q,2),mul(q,s),sc(mul(q,r),-1),r,s];
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
 const subst=poly=>{let o=Z();for(let[key,val]of poly){let t=co(BigInt(val));for(let i=0;i<8;i++){let n=Math.floor(key/(16**i))%16;if(n)t=mul(t,pow(values[i],n));}o=add(o,t);}
 let reduced=Z();for(let[k,c]of o){let n=k%radix;if(n<2)reduced=add(reduced,new Map([[k,c]]));else reduced=add(reduced,mul(new Map([[k-n+n%2,c]]),pow(q2,Math.floor(n/2))));}
 let g=0n;for(let c of reduced.values())g=gcd(g,c);if(g)for(let[k,c]of reduced)reduced.set(k,c/g);
 return [...reduced].sort((a,b)=>b[0]-a[0]).map(([k,c])=>({powers:Array.from({length:3},(_,i)=>Math.floor(k/(radix**i))%radix),c:c.toString()}));
 };
 return data.data.map(g=>({group:g.group,C:g.C.map(subst),H:g.H.map(subst)}));
}
function verifyHZeroConsequences(eq) {
 const R=32,Z=()=>new Map(),co=n=>new Map(n?[[0,BigInt(n)]]:[]),v=i=>new Map([[R**i,1n]]),add=(a,b,s=1n)=>{let o=new Map(a);for(let[k,x]of b){let z=(o.get(k)||0n)+s*x;if(z)o.set(k,z);else o.delete(k)}return o},sc=(a,s)=>add(Z(),a,BigInt(s)),mul=(a,b)=>{let o=Z();for(let[k,x]of a)for(let[l,y]of b){let z=(o.get(k+l)||0n)+x*y;if(z)o.set(k+l,z);else o.delete(k+l)}return o},sq=a=>mul(a,a),pow=(a,n)=>{let o=co(1);for(let i=0;i<n;i++)o=mul(o,a);return o};
 const[q,r,s]=Array.from({length:3},(_,i)=>v(i)),z=add(sq(r),sq(s)),pol=a=>new Map(a.map(t=>[t.powers.reduce((n,e,i)=>n+e*R**i,0),BigInt(t.c)]));
 const reduce=p=>{let o=Z();for(let[k,c]of p){let n=k%R;o=add(o,mul(new Map([[k-n+n%2,c]]),pow(z,Math.floor(n/2))));}return o};
 const Dp=add(pol(eq[0].C[0]),pol(eq[0].H[0]),-1n),Dm=add(pol(eq[1].C[0]),pol(eq[1].H[0]),-1n),Ep=add(pol(eq[0].C[1]),pol(eq[0].H[1]),-3n),Em=add(pol(eq[1].C[1]),pol(eq[1].H[1]),-3n);
 const L=add(mul(mul(mul(q,r),s),z),add(sq(r),sq(s),-1n),-1n);
 const checks={
 "Dplus-Dminus=2(z^2+4z-4)":reduce(add(add(Dp,Dm,-1n),sc(add(add(sq(z),z,4n),co(-4)),2),-1n)).size===0,
 "Dplus+Dminus=8(c^3rs-r^2+s^2)":reduce(add(add(Dp,Dm),sc(L,8),-1n)).size===0,
 "rEplus-sEminus=2z(z-2)+4(r^2-s^2)L":reduce(add(add(mul(r,Ep),mul(s,Em),-1n),add(sc(mul(z,add(z,co(-2))),2),sc(mul(add(sq(r),sq(s),-1n),L),4)),-1n)).size===0
 };
 return{checks,all:Object.values(checks).every(Boolean)};
}
const equations=specializeHZero(buildOrthogonalSupportEquations());
const result=verifyHZeroConsequences(equations);
if(!result.all) throw new Error('h=0 support-gradient identity failed');
console.log(JSON.stringify(result,null,2));
