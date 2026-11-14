"use strict";
// Deterministic exact small number-field projection certificates. No large kernel file is uploaded.
function translateRankOneIntegerSystem(original,s){
 s=BigInt(s);const pow=(a,n)=>{let z=1n;while(n--)z*=a;return z;};
 const bin=(n,k)=>{let z=1n;for(let i=1;i<=k;i++)z=z*BigInt(n-i+1)/BigInt(i);return z;};
 const T=Array.from({length:11},(_,i)=>Array.from({length:11},(_,j)=>j<=i?bin(i,j)*pow(s,i-j):0n));
 const transformed={...original,variableConvention:"m_i=sum_j binomial(i,j) s^(i-j) z_j, s="+s,
  variables:Array.from({length:11},(_,i)=>"z"+i)};
 transformed.equations=original.equations.map(e=>{
  const l=e.linear.map(BigInt),q=e.quadratic.map(BigInt);
  const linear=Array.from({length:11},(_,a)=>l.reduce((z,x,i)=>z+x*T[i][a],0n));
  const quadratic=original.quadraticMonomials.map(([a,b])=>original.quadraticMonomials.reduce((z,[i,j],k)=>
   z+q[k]*(T[i][a]*T[j][b]+(a===b?0n:T[i][b]*T[j][a])),0n));
  return {...e,linear:linear.map(String),quadratic:quadratic.map(String)};
 });
 transformed.LNumerator=original.LNumerator.map(row=>T[0].map((_,j)=>String(row.reduce((a,x,i)=>a+BigInt(x)*T[i][j],0n))));
 return transformed;
}

function reconstructLowProjectionNewton(data,buildSystem){
 const schema=[];for(let e=0;e<17;e++){for(let j=2;j<11;j++)schema.push({e,kind:"linear",j});for(let a=0;a<2;a++)for(let j=2;j<11;j++)schema.push({e,kind:"quadratic",a,j});schema.push({e,kind:"quadratic",a:1,j:1});}
 const vals=[];
 for(let s=0;s<=26;s++){
  const p=BigInt(s),z=translateRankOneIntegerSystem(buildSystem(data,Array.from({length:6},(_,i)=>String(p**BigInt(i)))),p);
  for(const e of z.equations){
   if(BigInt(e.linear[0])||BigInt(e.linear[1]))throw Error("Unexpected tangent linear term");
   for(const [a,b]of [[0,0],[0,1]]){const k=z.quadraticMonomials.findIndex(([i,j])=>a===i&&b===j);if(BigInt(e.quadratic[k]))throw Error("Unexpected pure c^2 or cd term");}
  }
  vals.push(schema.map(t=>{const e=z.equations[t.e];if(t.kind==="linear")return String(BigInt(e.scale)*BigInt(e.linear[t.j]));const j=z.quadraticMonomials.findIndex(([a,b])=>a===t.a&&b===t.j);return String(BigInt(e.scale)*BigInt(e.quadratic[j]));}));
 }
 let extraChecks=0;const newton=[];
 for(let i=0;i<schema.length;i++){
  let d=vals.slice(0,26).map(v=>BigInt(v[i])),factorial=1n,a=[];
  for(let k=0;k<=25;k++){if(k)factorial*=BigInt(k);if(d[0]%factorial)throw Error("Nonintegral falling-factorial coefficient");a.push(d[0]/factorial);d=d.slice(1).map((v,j)=>v-d[j]);}
  let check=0n,fall=1n;for(let k=0;k<=25;k++){check+=a[k]*fall;fall*=BigInt(26-k);}if(check!==BigInt(vals[26][i]))throw Error("Extra integer source check failed");
  extraChecks++;newton.push(a.map(String));
 }
 return {schema,newton,extraChecks,degreeBound:25};
}

"use strict";
function cubicIntegerRing(coefficients){
 const f=coefficients.map(BigInt),zero=()=>[0n,0n,0n],one=()=>[1n,0n,0n],isZero=a=>a.every(x=>x===0n);
 const add=(a,b)=>a.map((x,i)=>x+b[i]),sub=(a,b)=>a.map((x,i)=>x-b[i]),scale=(a,n)=>a.map(x=>x*n);
 function mul(a,b){const c=Array(5).fill(0n);for(let i=0;i<3;i++)for(let j=0;j<3;j++)c[i+j]+=a[i]*b[j];for(let k=4;k>=3;k--)for(let j=0;j<3;j++)c[k-3+j]-=c[k]*f[j];return c.slice(0,3);}
 function invData(a){const c0=a,c1=mul(a,[0n,1n,0n]),c2=mul(a,[0n,0n,1n]),A=Array.from({length:3},(_,i)=>[c0[i],c1[i],c2[i]]);
 const adj=[A[1][1]*A[2][2]-A[1][2]*A[2][1],A[1][2]*A[2][0]-A[1][0]*A[2][2],A[1][0]*A[2][1]-A[1][1]*A[2][0]],den=A[0][0]*adj[0]+A[0][1]*adj[1]+A[0][2]*adj[2];if(!den)throw Error("Nonzero field element expected.");return {adj,den};}
 function divExact(a,inverse){const p=mul(a,inverse.adj);if(p.some(x=>x%inverse.den!==0n))throw Error("Bareiss quotient not integral in the cubic order");return p.map(x=>x/inverse.den);}
 return {f,zero,one,isZero,add,sub,scale,mul,invData,divExact};
}
function lowProjectionInCubicField(newtonData,coefficients){
 const R=cubicIntegerRing(coefficients),basis=[];let fall=R.one();
 for(let k=0;k<=25;k++){basis.push(R.scale(fall,5n**BigInt(25-k)));fall=R.mul(fall,[-5n*BigInt(k),1n,0n]);}
 const values=newtonData.newton.map(row=>row.reduce((a,x,k)=>R.add(a,R.scale(basis[k],BigInt(x))),R.zero()));
 const C=[];for(let n=1;n<=3;n++)for(let b=0;b<=n;b++)C.push({j:null,a:n-b,b});
 for(let j=2;j<11;j++)for(const [a,b]of [[0,0],[1,0],[0,1]])C.push({j,a,b});
 const key=x=>[x.j===null?"p":x.j,x.a,x.b].join(":"),index=new Map(C.map((x,i)=>[key(x),i]));
 const rows=[];
 for(let e=0;e<17;e++)for(const [ma,mb]of [[0,0],[1,0],[0,1]]){
  const row=C.map(()=>R.zero());
  for(let k=0;k<values.length;k++){const t=newtonData.schema[k];if(t.e!==e||R.isZero(values[k]))continue;
   let x;if(t.kind==="linear")x={j:t.j,a:ma,b:mb};else if(t.a===1&&t.j===1)x={j:null,a:ma,b:mb+2};else x={j:t.j,a:ma+(t.a===0?1:0),b:mb+(t.a===1?1:0)};
   const j=index.get(key(x));if(j!==undefined)row[j]=R.add(row[j],values[k]);
  }
  rows.push(row);
 }
 return {coefficients:coefficients.map(String),columns:C,matrix:rows.map(r=>r.map(a=>a.map(String)))};
}
async function bareissCubicField(input,report){
 const R=cubicIntegerRing(input.coefficients),A=input.matrix.map(r=>r.map(a=>a.map(BigInt))),pivots=[];let rank=0,prev=R.one(),last=Date.now();
 for(let c=0;c<A[0].length&&rank<A.length;c++){
  let k=rank;while(k<A.length&&R.isZero(A[k][c]))k++;if(k===A.length)continue;
  [A[k],A[rank]]=[A[rank],A[k]];const pivot=A[rank][c],inv=R.invData(prev);
  for(let i=rank+1;i<A.length;i++){const b=A[i][c];for(let j=c+1;j<A[i].length;j++)A[i][j]=R.divExact(R.sub(R.mul(pivot,A[i][j]),R.mul(b,A[rank][j])),inv);A[i][c]=R.zero();}
  pivots.push(c);rank++;prev=pivot;
  if(report&&Date.now()-last>7000){await report({rank,column:c,maxDigits:Math.max(...pivot.map(x=>String(x).length))});last=Date.now();}
 }
 return {coefficients:input.coefficients,rank,pivots,rows:A.slice(0,rank).map(r=>r.map(a=>a.map(String)))};
}


"use strict";
function cubicFieldFractions(R){
 const gcd=(a,b)=>{if(a<0n)a=-a;if(b<0n)b=-b;while(b)[a,b]=[b,a%b];return a;};
 function make(n,d=1n){if(R.isZero(n))return {n:R.zero(),d:1n};let g=d;for(const x of n)g=gcd(g,x);if(d<0n)g=-g;return {n:n.map(x=>x/g),d:d/g};}
 const zero=()=>make(R.zero()),one=()=>make(R.one()),from=n=>make(n),isZero=x=>R.isZero(x.n),neg=x=>({n:x.n.map(v=>-v),d:x.d});
 const add=(x,y)=>{if(isZero(x))return y;if(isZero(y))return x;const g=gcd(x.d,y.d),a=y.d/g,b=x.d/g;return make(R.add(R.scale(x.n,a),R.scale(y.n,b)),x.d*a);};
 const mul=(x,y)=>{if(isZero(x)||isZero(y))return zero();return make(R.mul(x.n,y.n),x.d*y.d);};
 const inv=x=>{const a=R.invData(x.n);return make(R.scale(a.adj,x.d),a.den);};
 return {gcd,make,zero,one,from,isZero,neg,add,mul,inv};
}
function cubicFieldKernel(echelon,columns){
 const R=cubicIntegerRing(echelon.coefficients),F=cubicFieldFractions(R),rows=echelon.rows.map(r=>r.map(a=>a.map(BigInt))),pivotSet=new Set(echelon.pivots),free=Array.from({length:columns},(_,i)=>i).filter(i=>!pivotSet.has(i)),pivotInverses=rows.map((r,i)=>F.inv(F.from(r[echelon.pivots[i]]))),kernels=[];
 for(const f of free){let v=Array.from({length:columns},F.zero);v[f]=F.one();
  for(let i=echelon.rank-1;i>=0;i--){const p=echelon.pivots[i];let sum=F.zero();for(let j=p+1;j<columns;j++)if(!F.isZero(v[j])&&!R.isZero(rows[i][j]))sum=F.add(sum,F.mul(F.from(rows[i][j]),v[j]));v[p]=F.neg(F.mul(sum,pivotInverses[i]));}
  let den=1n;for(const x of v)den=den/F.gcd(den,x.d)*x.d;let integer=v.map(x=>R.scale(x.n,den/x.d)),g=0n;for(const a of integer)for(const x of a)g=F.gcd(g,x);integer=integer.map(a=>a.map(x=>x/g));kernels.push(integer.map(a=>a.map(String)));
 }
 return {coefficients:echelon.coefficients,free,kernels};
}


"use strict";
function fullProjectionInCubicField(newtonData,coefficients){
 const R=cubicIntegerRing(coefficients),basis=[];let fall=R.one();
 for(let k=0;k<=25;k++){basis.push(R.scale(fall,5n**BigInt(25-k)));fall=R.mul(fall,[-5n*BigInt(k),1n,0n]);}
 const values=newtonData.newton.map(row=>row.reduce((a,x,k)=>R.add(a,R.scale(basis[k],BigInt(x))),R.zero()));
 const C=[],mult=[];for(let n=1;n<=5;n++)for(let b=0;b<=n;b++)C.push({j:null,a:n-b,b});for(let j=2;j<11;j++)for(let n=0;n<=4;n++)for(let b=0;b<=n;b++)C.push({j,a:n-b,b});for(let n=0;n<=3;n++)for(let b=0;b<=n;b++)mult.push([n-b,b]);
 const key=x=>[x.j===null?"p":x.j,x.a,x.b].join(":"),index=new Map(C.map((x,i)=>[key(x),i])),rows=[];
 for(let e=0;e<17;e++)for(const [ma,mb]of mult){
  const row=C.map(()=>R.zero());
  for(let k=0;k<values.length;k++){const t=newtonData.schema[k];if(t.e!==e||R.isZero(values[k]))continue;
   let x;if(t.kind==="linear")x={j:t.j,a:ma,b:mb};else if(t.a===1&&t.j===1)x={j:null,a:ma,b:mb+2};else x={j:t.j,a:ma+(t.a===0?1:0),b:mb+(t.a===1?1:0)};
   const j=index.get(key(x));if(j===undefined)throw Error("Full projection lost a column");row[j]=R.add(row[j],values[k]);
  }rows.push(row);
 }
 for(let j=2;j<11;j++)for(let n=0;n<=2;n++)for(let b=0;b<=n;b++){const row=C.map(()=>R.zero());row[index.get(key({j,a:n-b,b:b+2}))]=R.one();rows.push(row);}
 return {coefficients:coefficients.map(String),columns:C,matrix:rows.map(r=>r.map(a=>a.map(String)))};
}
function verifyAndExtendCubicFieldKernels(full,low,kernelData){
 const R=cubicIntegerRing(full.coefficients),key=x=>[x.j===null?"p":x.j,x.a,x.b].join(":"),index=new Map(full.columns.map((x,i)=>[key(x),i])),map=low.columns.map(x=>index.get(key(x))),free=kernelData.free.map(i=>map[i]);
 const kernels=kernelData.kernels.map(v=>{const out=full.columns.map(()=>R.zero());for(let i=0;i<map.length;i++)out[map[i]]=v[i].map(BigInt);return out;});
 for(const [a,b]of [[4,0],[5,0],[3,1],[4,1]]){const j=index.get(key({j:null,a,b}));free.push(j);const v=full.columns.map(()=>R.zero());v[j]=R.one();kernels.push(v);}
 const rows=full.matrix.map(r=>r.map(a=>a.map(BigInt)));let zeroChecks=0,integerComponentChecks=0,independenceChecks=0;
 for(let k=0;k<kernels.length;k++){const v=kernels[k],support=v.map((a,j)=>R.isZero(a)?-1:j).filter(j=>j>=0);
  for(const row of rows){let sum=R.zero();for(const j of support)if(!R.isZero(row[j]))sum=R.add(sum,R.mul(row[j],v[j]));if(!R.isZero(sum))throw Error("Nonzero full projection kernel product");zeroChecks++;integerComponentChecks+=3;}
  for(let j=0;j<free.length;j++){if(k===j?R.isZero(v[free[j]]):!R.isZero(v[free[j]]))throw Error("Kernel independence diagonal failed");independenceChecks++;}
 }
 return {coefficients:full.coefficients,free,kernels:kernels.map(v=>v.map(a=>a.map(String))),zeroChecks,integerComponentChecks,independenceChecks,rankUpper:155-kernels.length};
}


function sha256ASCII(text){
 const K=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
 const H=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19],N=Math.ceil((text.length+9)/64)*64,B=new Uint8Array(N);
 for(let i=0;i<text.length;i++){const c=text.charCodeAt(i);if(c>127)throw Error("SHA input must be ASCII");B[i]=c;}B[text.length]=128;let bits=BigInt(text.length)*8n;for(let i=0;i<8;i++){B[N-1-i]=Number(bits&255n);bits>>=8n;}
 const R=(x,n)=>(x>>>n)|(x<<(32-n)),W=new Uint32Array(64);
 for(let off=0;off<N;off+=64){
  for(let i=0;i<16;i++)W[i]=(B[off+4*i]<<24)|(B[off+4*i+1]<<16)|(B[off+4*i+2]<<8)|B[off+4*i+3];
  for(let i=16;i<64;i++){const a=W[i-15],b=W[i-2],s0=R(a,7)^R(a,18)^(a>>>3),s1=R(b,17)^R(b,19)^(b>>>10);W[i]=(W[i-16]+s0+W[i-7]+s1)>>>0;}
  let [a,b,c,d,e,f,g,h]=H;
  for(let i=0;i<64;i++){const S1=R(e,6)^R(e,11)^R(e,25),ch=(e&f)^(~e&g),T1=(h+S1+ch+K[i]+W[i])>>>0,S0=R(a,2)^R(a,13)^R(a,22),maj=(a&b)^(a&c)^(b&c),T2=(S0+maj)>>>0;h=g;g=f;f=e;e=(d+T1)>>>0;d=c;c=b;b=a;a=(T1+T2)>>>0;}
  const V=[a,b,c,d,e,f,g,h];for(let i=0;i<8;i++)H[i]=(H[i]+V[i])>>>0;
 }
 return H.map(x=>x.toString(16).padStart(8,"0")).join("");
}

async function verifyRankOneCubicNumberFieldProjections(data,buildSystem,report){
 const newton=reconstructLowProjectionNewton(data,buildSystem),receipt={execution:"Exact BigInt polynomial and cubic-number-field operations; no floating-point decisions.",fixedEquationMultiplier:"det(J3); each sampled primitive equation is multiplied back by its scale before Newton reconstruction.",thetaScaling:"theta=5s; all reconstructed first rows multiplied by 5^25.",newton:{degreeBound:25,coefficientSequences:newton.schema.length,reconstructionSources:Array.from({length:26},(_,i)=>i),extraSource:26,exactExtraSourceChecks:newton.extraChecks},fields:[]};
 for(const [name,f]of [["Pplus",[-200,160,-25]],["Pminus",[21600,4320,135]]]){
  const mod11=Array.from({length:11},(_,t)=>((t**3+f[2]*t*t+f[1]*t+f[0])%11+11)%11);if(mod11.some(x=>!x))throw Error("Irreducibility certificate failed");
  const low=lowProjectionInCubicField(newton,f),echelon=await bareissCubicField(low,report),small=cubicFieldKernel(echelon,36),full=fullProjectionInCubicField(newton,f),certificate=verifyAndExtendCubicFieldKernels(full,low,small);
  if(echelon.rank!==25||small.kernels.length!==11||certificate.rankUpper!==140)throw Error("Unexpected exact rank or kernel count");
  const text=JSON.stringify(certificate);
  receipt.fields.push({name,monicPolynomialAscending:[...f,1],nonzeroValuesModulo11:mod11,lowMatrix:{rows:51,columns:36,exactRank:echelon.rank,pivots:echelon.pivots,free:small.free},fullMatrix:{rows:224,columns:155,independentKernelCount:certificate.kernels.length,rankUpper:certificate.rankUpper,numberFieldZeroChecks:certificate.zeroChecks,integerCoefficientZeroChecks:certificate.integerComponentChecks,freeCoordinateIndependenceChecks:certificate.independenceChecks,free:certificate.free},fullCanonicalKernelJSONBytes:text.length,fullCanonicalKernelSHA256:sha256ASCII(text)});
 }
 return receipt;
}
if(typeof module!=="undefined")module.exports={verifyRankOneCubicNumberFieldProjections,reconstructLowProjectionNewton,cubicIntegerRing,lowProjectionInCubicField,bareissCubicField,cubicFieldKernel,fullProjectionInCubicField,verifyAndExtendCubicFieldKernels,sha256ASCII};
if(typeof require!=="undefined"&&require.main===module){
 const fs=require("fs"),path=require("path"),data=JSON.parse(fs.readFileSync(path.join(__dirname,"2026-11-13-six-mode-cubic-bell-third-moment-exact-data.json"),"utf8"));
 const {buildRankOneCenteredIntegerSystem}=require("./2026-11-14-rank-one-centered-integer-system-generator.js");
 verifyRankOneCubicNumberFieldProjections(data,buildRankOneCenteredIntegerSystem).then(r=>process.stdout.write(JSON.stringify(r,null,2)+"\n")).catch(e=>{console.error(e);process.exitCode=1;});
}
