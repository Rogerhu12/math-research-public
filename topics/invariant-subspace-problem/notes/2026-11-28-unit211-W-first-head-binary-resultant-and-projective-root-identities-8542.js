/* New universal exact original-head identities, V8 BigInt.
   No old W parameter gate or data payload.
   Independent coefficients a,b,c,d,e,f,g,h,i and x,y.
   Return both the fixed 4x4/5x5 identity and complete pseudo-remainder.
*/
(()=>{
const started=Date.now(),N=11,Z=()=>new Map(),key=e=>e.join(",");
function con(v){const p=Z();if(v)p.set(key(Array(N).fill(0)),BigInt(v));return p;}
function v(j){const e=Array(N).fill(0);e[j]=1;return new Map([[key(e),1n]]);}
function add(...ps){const r=Z();for(const p of ps)for(const [m,c]of p){const n=(r.get(m)||0n)+c;if(n)r.set(m,n);else r.delete(m);}return r;}
function neg(p){return new Map([...p].map(([m,c])=>[m,-c]));}
function sub(p,q){return add(p,neg(q));}
function mul(p,q){const r=Z();for(const [m,c]of p){const a=m.split(",").map(Number);for(const[n,d]of q){const b=n.split(",").map(Number),k=key(a.map((x,j)=>x+b[j])),z=(r.get(k)||0n)+c*d;if(z)r.set(k,z);else r.delete(k);}}return r;}
function pow(p,n){let r=con(1);for(let j=0;j<n;j++)r=mul(r,p);return r;}
function eq(p,q,label){if(sub(p,q).size)throw new Error("Exact identity failed: "+label);}
function det(m){if(!m.length)return con(1);if(m.length===1)return m[0][0];let r=Z();for(let j=0;j<m.length;j++){if(!m[0][j].size)continue;const z=mul(m[0][j],det(m.slice(1).map(row=>row.filter((_,k)=>k!==j))));r=add(r,j%2?neg(z):z);}return r;}
const[a,b,c,d,e,f,g,h,i,x,y]=Array.from({length:N},(_,j)=>v(j));
const z=con(0),A=add(mul(a,pow(x,2)),mul(b,mul(x,y)),mul(c,pow(y,2)));
const B=add(mul(d,pow(x,2)),mul(e,mul(x,y)),mul(f,pow(y,2)));
const C=add(mul(g,pow(x,2)),mul(h,mul(x,y)),mul(i,pow(y,2)));
const D=sub(mul(x,C),mul(y,B));
const d0=g,d1=sub(h,d),d2=sub(i,e),d3=neg(f);
const K=add(mul(add(mul(a,x),mul(b,y)),B),mul(mul(c,y),C));
const head=[
 [neg(a),neg(b),neg(c),z],
 [z,neg(a),neg(b),neg(c)],
 [d0,d1,d2,d3],
 [mul(a,d),add(mul(a,e),mul(b,d),mul(c,g)),
  add(mul(a,f),mul(b,e),mul(c,h)),add(mul(b,f),mul(c,i))]
];
const mon=[pow(x,3),mul(pow(x,2),y),mul(x,pow(y,2)),pow(y,3)];
const forms=[neg(mul(x,A)),neg(mul(y,A)),D,K];
for(let j=0;j<4;j++)eq(forms[j],add(...head[j].map((q,k)=>mul(q,mon[k]))),"four full homogeneous original overlap rows "+j);
const delta=det(head);
const sylvester=[
 [a,b,c,z,z],[z,a,b,c,z],[z,z,a,b,c],
 [d0,d1,d2,d3,z],[z,d0,d1,d2,d3]
];
const res=det(sylvester);
eq(delta,res,"fixed four-head determinant equals complete binary resultant");
const R1=add(mul(pow(a,2),d2),neg(mul(mul(a,b),d1)),mul(sub(pow(b,2),mul(a,c)),d0));
const R0=add(mul(pow(a,2),d3),neg(mul(mul(a,c),d1)),mul(mul(b,c),d0));
const q=add(mul(mul(a,d0),x),mul(sub(mul(a,d1),mul(b,d0)),y));
eq(mul(pow(a,2),D),add(mul(q,A),mul(pow(y,2),add(mul(R1,x),mul(R0,y)))),"complete degree-three original pseudo-remainder");
eq(mul(pow(a,2),delta),add(mul(a,pow(R0,2)),neg(mul(mul(b,R0),R1)),mul(c,pow(R1,2))),"complete resultant quadratic identity");
return {
 schema:"isp-universal-original-head-polynomial-identity-v1",
 variables:["a","b","c","d","e","f","g","h","i","x","y"],
 ring:"ZZ[a,b,c,d,e,f,g,h,i,x,y]",
 fourFullHeadRowsReturned:true,fixed4EqualsFixed5ResultantReturned:true,
 entireHomogeneousPseudoRemainderReturned:true,resultantQuadraticIdentityReturned:true,
 actualDeterminantTerms:delta.size,actualR1Terms:R1.size,actualR0Terms:R0.size,
 newParameterOrGeometryInverse:false,numericalSampling:false,
 noOriginalWeightFibreExcluded:true,noOldParameterGateReplayed:true,
 elapsedMilliseconds:Date.now()-started,osExitCode:null,peakRSSKiB:null,
 executionEngine:"functions.exec V8 exact BigInt, no OS process"
};
})()
