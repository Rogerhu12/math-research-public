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
function specializeZZero(data) {
 const Z=()=>new Map(),co=n=>new Map(n?[[0,BigInt(n)]]:[]),v=i=>new Map([[16**i,1n]]),add=(a,b,s=1n)=>{let o=new Map(a);for(let[k,x]of b){let z=(o.get(k)||0n)+s*x;if(z)o.set(k,z);else o.delete(k)}return o},sc=(a,s)=>add(Z(),a,BigInt(s)),mul=(a,b)=>{let o=Z();for(let[k,x]of a)for(let[l,y]of b){let z=(o.get(k+l)||0n)+x*y;if(z)o.set(k+l,z);else o.delete(k+l)}return o};
 let[x,y,r,s]=Array.from({length:4},(_,i)=>v(i)),values=[sc(mul(r,x),-2),co(2),co(-2),Z(),add(x,r,-1n),add(y,s,-1n),r,s];
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
 const pow=(a,n)=>{let o=co(1);for(let i=0;i<n;i++)o=mul(o,a);return o};
 function subst(poly){let o=Z();for(let[key,val]of poly){let t=co(BigInt(val));for(let i=0;i<8;i++){let n=Math.floor(key/(16**i))%16;if(n)t=mul(t,pow(values[i],n));}o=add(o,t);}
 let r0=Z();for(let[k,c]of o){let ex=k%16,er=Math.floor(k/256)%16,n=Math.min(ex,er),nk=k-n*(1+256)+n*(16+4096);r0=add(r0,new Map([[nk,n%2?-c:c]]));}
 let g=0n;for(const c of r0.values())g=gcd(g,c);if(g)for(const[k,c]of r0)r0.set(k,c/g);
 return [...r0].sort((a,b)=>b[0]-a[0]).map(([k,c])=>({powers:Array.from({length:4},(_,i)=>Math.floor(k/(16**i))%16),c:c.toString()}));
 }
 return data.data.map(g=>({group:g.group,C:g.C.map(subst),H:g.H.map(subst)}));
}
function verifyZZeroConsequences(equations) {
 const add=(a,b,s=1n)=>{let out=new Map(a);for(const[k,c]of b){let v=(out.get(k)||0n)+s*c;if(v)out.set(k,v);else out.delete(k)}return out},mul=(a,b)=>{let o=new Map();for(let[k,c]of a)for(let[l,d]of b){let v=(o.get(k+l)||0n)+c*d;if(v)o.set(k+l,v);else o.delete(k+l)}return o};
 const v=i=>new Map([[16**i,1n]]),one=new Map([[0,1n]]),sc=(a,k)=>add(new Map(),a,BigInt(k)),sq=a=>mul(a,a);
 const pol=z=>new Map(z.map(t=>[t.powers.reduce((s,e,i)=>s+e*16**i,0),BigInt(t.c)]));
 const x=v(0),y=v(1),r=v(2),s=v(3);
 const C0=pol(equations[0].C[0]),C1=pol(equations[0].C[1]),H0=pol(equations[0].H[0]),H1=pol(equations[0].H[1]),Cm0=pol(equations[1].C[0]),Hm0=pol(equations[1].H[0]);
 const E1=add(add(add(sq(x),sq(y),-2n),sq(r)),one,2n);
 const E2right=add(add(add(sc(sq(x),-2),sq(y)),sq(s)),one,2n);
 const combo=add(mul(r,add(add(sc(sq(y),3),sc(sq(r),-2)),one,-4n)),mul(mul(s,x),y),3n);
 const checks={"plus H0-C0":add(add(H0,C0,-1n),E1,-1n).size===0,"minus C0-H0":add(add(Cm0,Hm0,-1n),E2right,-1n).size===0,"plus C1-3H1":add(add(C1,H1,-3n),combo,-1n).size===0,"Cplus0 at r=y=0":([...C0].filter(([k,c])=>!(Math.floor(k/16)%16)&&!(Math.floor(k/256)%16)).length===1 && C0.get(0)===-6n)};
 return {checks,all:Object.values(checks).every(Boolean)};
}
const equations=specializeZZero(buildOrthogonalSupportEquations());
const result=verifyZZeroConsequences(equations);
if(!result.all) throw new Error('Z=0 support-gradient identity failed');
console.log(JSON.stringify(result,null,2));
