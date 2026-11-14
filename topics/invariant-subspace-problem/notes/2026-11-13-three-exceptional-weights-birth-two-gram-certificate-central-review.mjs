// Exact coefficient certificate for the three-head, relative-birth-two primitive Gram.
// This is an executable JavaScript file. It uses only BigInt and standard Map.
// n>=2: coefficient matrices in Z[A,B,C,x,y] are positive semidefinite.
// n=1: leading principal minors in Z[A,B,C,y] have positive nonzero coefficients.
// This proves the S_L-fixed three-dimensional block, not the full K_s on its own.

function q3Data(n0,d0,fixN=false){
 const BASE=32,DIM=5,pow=Array.from({length:DIM},(_,i)=>BASE**i),degreeCache=new WeakMap();
 const zero=()=>new Map(),con=x=>x?new Map([[0,BigInt(x)]]):zero(),one=con(1);
 function degree(P){if(degreeCache.has(P))return degreeCache.get(P);let d=Array(DIM).fill(0);for(let k of P.keys())for(let i=0;i<DIM;i++)d[i]=Math.max(d[i],Math.floor(k/pow[i])%BASE);degreeCache.set(P,d);return d;}
 function add(P,Q,s=1n){let R=new Map(P);for(const[k,c]of Q){let v=(R.get(k)||0n)+s*c;if(v)R.set(k,v);else R.delete(k);}return R;}
 const scale=(P,s)=>{s=BigInt(s);return s?new Map([...P].map(([k,c])=>[k,c*s])):zero();};
 function mul(P,Q){let a=degree(P),b=degree(Q);if(a.some((v,i)=>v+b[i]>=BASE))throw Error("degree packing overflow");let R=zero();for(const[k,c]of P)for(const[l,d]of Q){let j=k+l,v=(R.get(j)||0n)+c*d;if(v)R.set(j,v);else R.delete(j);}return R;}
 const lin=(i,c)=>add(new Map([[pow[i],1n]]),con(c)),xp=c=>fixN?con(c):lin(3,c),yp=c=>lin(4,c);
 const mp=(...f)=>f.reduce(mul,one),mat=()=>Array.from({length:3},()=>Array.from({length:3},zero));
 const mm=(A,B)=>A.map((row,i)=>row.map((_,j)=>{let P=zero();for(let k=0;k<3;k++)P=add(P,mul(A[i][k],B[k][j]));return P;}));
 const sm=(P,A)=>A.map(row=>row.map(Q=>mul(P,Q)));
 const ma=(A,B,s=1n)=>A.map((row,i)=>row.map((P,j)=>add(P,B[i][j],s)));
 function detSmall(A){if(A.length===1)return BigInt(A[0][0]);let v=0n;for(let j=0;j<A.length;j++)v+=BigInt(j%2?-1:1)*BigInt(A[0][j])*detSmall(A.slice(1).map(row=>row.filter((_,k)=>k!==j)));return v;}
 const bits=Array.from({length:8},(_,r)=>Array.from({length:3},(_,i)=>(r>>i)&1));
 const key=r=>bits[r].reduce((s,v,i)=>s+v*pow[i],0);
 function product(indices,no,dd,divide){
  let np=0,up=0,k=0;const factors=[];
  for(let r of indices){k+=key(r);let m=bits[r].reduce((a,b)=>a+b,0);
   if(m===0){up++;factors.push(yp(dd),yp(dd-1));}
   if(m===1){np++;up++;factors.push(yp(dd-1));}
   if(m===2){np++;up++;factors.push(xp(no+1));}
   if(m===3){np++;factors.push(xp(no+1),xp(no+2));}
  }
  if(np<divide||up<divide)throw Error("illegal factor cancellation");
  for(let i=0;i<np-divide;i++)factors.push(xp(no));
  for(let i=0;i<up-divide;i++)factors.push(yp(dd-2));
  return mul(new Map([[k,1n]]),mp(...factors));
 }
 function build(no,dd){
  const R=mat(),Q=mat();let Z=zero(),E=zero();
  for(let r=0;r<8;r++)Z=add(Z,product([r],no,dd,0));
  for(let r=0;r<8;r++)for(let s=r+1;s<8;s++){const v=bits[r].map((b,i)=>b-bits[s][i]),P=product([r,s],no,dd,1);for(let i=0;i<3;i++)for(let j=0;j<3;j++)if(v[i]*v[j])R[i][j]=add(R[i][j],scale(P,v[i]*v[j]));}
  for(let r=0;r<8;r++)for(let s=r+1;s<8;s++)for(let t=s+1;t<8;t++){
   const V=[r,s,t].map(j=>[1,...bits[j]]),cof=Array.from({length:4},(_,i)=>detSmall(V.map(row=>row.filter((_,k)=>k!==i)))*BigInt(i%2?-1:1));
   if(cof.slice(1).every(x=>!x))continue;const P=product([r,s,t],no,dd,2);for(let i=0;i<3;i++)for(let j=0;j<3;j++)if(cof[i+1]*cof[j+1])Q[i][j]=add(Q[i][j],scale(P,cof[i+1]*cof[j+1]));
  }
  for(let r=0;r<8;r++)for(let s=r+1;s<8;s++)for(let t=s+1;t<8;t++)for(let u=t+1;u<8;u++){let det=detSmall([r,s,t,u].map(j=>[1,...bits[j]]));if(det)E=add(E,scale(product([r,s,t,u],no,dd,3),det*det));}
  return{R,Q,E,Z};
 }
 const P=build(n0-1,d0+1),M=build(n0,d0),N=build(n0+1,d0-1);
 const identityChecks=[];
 for(const [label,O] of [["previous",P],["current",M],["next",N]]){
  const lhs=mm(O.R,O.Q),rhs=mul(O.Z,O.E);
  for(let i=0;i<3;i++)for(let j=0;j<3;j++){
   const residual=add(lhs[i][j],i===j?rhs:zero(),-1n);
   if(residual.size)throw Error("RQ=ZEI failed: "+label+" "+i+","+j);
  }
  identityChecks.push(label);
 }
 const aa=mp(xp(n0+1),xp(n0+2),yp(d0-1),M.Z,M.Z,N.E),bb=mp(xp(n0),xp(n0+3),yp(d0-2),P.Z);
 const Delta=ma(sm(aa,P.R),sm(bb,mm(mm(M.R,N.Q),M.R)),-1n);
 return {Delta,degree,identityChecks};
}

function verifyThreeHeadBirthTwo(){
 const assert=(v,msg)=>{if(!v)throw Error(msg);};
 const det3=a=>a[0][0]*a[1][1]*a[2][2]+2n*a[0][1]*a[0][2]*a[1][2]
   -a[0][0]*a[1][2]**2n-a[1][1]*a[0][2]**2n-a[2][2]*a[0][1]**2n;
 const bulk=q3Data(2,3,false),D=bulk.Delta;
 const keys=new Set(D.flat().flatMap(P=>[...P.keys()]));
 const ranks=[0,0,0,0];
 for(const k of keys){
  const a=D.map(row=>row.map(P=>P.get(k)||0n));
  for(let i=0;i<3;i++)for(let j=0;j<3;j++)assert(a[i][j]===a[j][i],"not symmetric");
  const diagonal=[a[0][0],a[1][1],a[2][2]];
  const pairs=[a[0][0]*a[1][1]-a[0][1]**2n,a[0][0]*a[2][2]-a[0][2]**2n,a[1][1]*a[2][2]-a[1][2]**2n];
  const determinant=det3(a);
  assert([...diagonal,...pairs,determinant].every(x=>x>=0n),"indefinite coefficient block at "+k);
  ranks[determinant>0n?3:pairs.some(x=>x>0n)?2:diagonal.some(x=>x>0n)?1:0]++;
 }
 assert(keys.size===32058,"unexpected bulk support");
 const anchorKey=2+2*32+2*32**2;
 const bulkAnchor=D.map(row=>row.map(P=>P.get(anchorKey)||0n));
 for(let i=0;i<3;i++)for(let j=0;j<3;j++)assert(bulkAnchor[i][j]===(i===j?2488320n:1382400n),"bulk strict anchor mismatch");
 assert(det3(bulkAnchor)===6424875937824768000n,"bulk anchor determinant mismatch");

 const edge=q3Data(1,3,true),Delta=edge.Delta;
 let inputMax=0n;
 for(const P of Delta.flat()){
  let s=0n;for(const c of P.values())s+=c<0n?-c:c;
  if(s>inputMax)inputMax=s;
  const deg=edge.degree(P);
  assert(deg[0]<=7&&deg[1]<=7&&deg[2]<=7&&deg[3]===0&&deg[4]<=17,"edge degree bound mismatch");
 }
 assert(inputMax===216000000000n,"edge l1 coefficient bound mismatch");
 // Every coefficient of every determinant intermediate has absolute value <=6*S^3.
 // Base >12*S^3 therefore permits unique signed-balanced digits without carries.
 const cap=12n*inputMax**3n+1n,WIDTH=cap.toString(2).length+1;
 const BASE=1n<<BigInt(WIDTH),HALF=BASE>>1n;
 assert(BASE>12n*inputMax**3n,"insufficient balanced base");
 const encode=P=>{
  const out=new Map();
  for(const[k,c]of P){
   assert(Math.floor(k/32**3)%32===0,"edge n not fixed");
   const y=Math.floor(k/32**4)%32,head=k%32**3;
   out.set(head,(out.get(head)||0n)+(c<<BigInt(WIDTH*y)));
  }
  return out;
 };
 const A=Delta.map(row=>row.map(encode));
 const add=(P,Q,sign=1n)=>{
  const out=new Map(P);
  for(const[k,c]of Q){const v=(out.get(k)||0n)+sign*c;if(v)out.set(k,v);else out.delete(k);}
  return out;
 };
 const mul=(P,Q)=>{
  const out=new Map();
  // Each head exponent is at most 7 per input and at most 21 in triple products.
  // Thus addition of base-32 head keys has no inter-variable carry.
  for(const[k,c]of P)for(const[l,d]of Q){
   const j=k+l,v=(out.get(j)||0n)+c*d;if(v)out.set(j,v);else out.delete(j);
  }
  return out;
 };
 function inspect(P,maxY,expectedCount,strictExponents,strictCoefficient){
  let count=0,strictFound=false;
  for(const[k,v0]of P){
   let v=v0,y=0;
   while(v!==0n){
    let c=v%BASE;if(c>=HALF)c-=BASE;if(c< -HALF)c+=BASE;
    v=(v-c)/BASE;
    assert(c>=0n,"negative edge coefficient");
    if(c){
     count++;
     const e=[k%32,Math.floor(k/32)%32,Math.floor(k/32**2)%32,y];
     if(e.every((x,i)=>x===strictExponents[i])){
      assert(c===strictCoefficient,"edge strict coefficient mismatch");strictFound=true;
     }
    }
    y++;assert(y<=maxY+1,"balanced digit degree overflow");
   }
  }
  assert(count===expectedCount,"unexpected edge support");
  assert(strictFound,"missing edge strict anchor");
  return {coefficients:count,strictExponents,strictCoefficient:String(strictCoefficient)};
 }
 const first=inspect(A[0][0],17,1964,[2,2,2,0],746496n);
 const minor12=add(mul(A[0][0],A[1][1]),mul(A[0][1],A[1][0]),-1n);
 const second=inspect(minor12,34,22852,[5,4,3,0],481579499520n);
 let determinant=new Map();
 for(let j=0;j<3;j++){
  const cols=[0,1,2].filter(k=>k!==j);
  const minor=add(mul(A[1][cols[0]],A[2][cols[1]]),mul(A[1][cols[1]],A[2][cols[0]]),-1n);
  determinant=add(determinant,mul(A[0][j],minor),j%2?-1n:1n);
 }
 const third=inspect(determinant,51,103458,[7,6,5,0],385175539364659200n);
 return{
  status:"PASS: exact polynomial identities, PSD coefficient blocks, and Sylvester edge certificate",
  bulk:{parameters:"n=2+x,d=3+y; A,B,C>0; x,y>=0",blocks:keys.size,ranks,identityChecks:bulk.identityChecks,strictAnchor:bulkAnchor.map(row=>row.map(String))},
  edge:{parameters:"n=1,d=3+y; A,B,C>0; y>=0",identityChecks:edge.identityChecks,inputCoefficientL1Bound:String(inputMax),balancedDigitBits:WIDTH,first,second,third},
  scope:"Three exceptional positive heads, relative birth 2, S_L-fixed three-dimensional primitive block"
 };
}
const certificate=verifyThreeHeadBirthTwo();
if(typeof console!=="undefined")console.log(JSON.stringify(certificate,null,2));
