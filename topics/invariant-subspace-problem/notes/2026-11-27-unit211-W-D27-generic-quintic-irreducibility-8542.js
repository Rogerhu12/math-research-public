// Exact D27 irreducibility certificate at k=1; not a finite-point emptiness test.
const terms=[
 [5,4,16],[4,5,-4],[4,4,32],
 [3,6,2],[3,5,-12],[3,4,-96],[3,3,-384],[3,2,-384],
 [2,6,3],[2,5,8],[2,4,60],[2,3,384],[2,2,1088],[2,1,1024],
 [1,5,-10],[1,4,-28],[1,3,48],[1,2,64],[1,1,-512],[1,0,-768],
 [0,6,-1],[0,5,-18],[0,4,-120],[0,3,-440],[0,2,-1008],[0,1,-1344],[0,0,-768]];
const original=Array(6).fill(0);
for(const [e,k,c] of terms)original[e]+=c;
if(JSON.stringify(original)!==JSON.stringify([-3699,-1206,2567,-874,28,16]))throw Error("whole D27 k=1 specialization");
if(terms.filter(v=>v[0]===5).length!==1||JSON.stringify(terms[0])!=="[5,4,16]")throw Error("original e leading");
if(!terms.some(v=>v[0]===0&&v[1]===0&&v[2]===-768))throw Error("original e-content");

function test(prime){
 const mod=x=>((x%prime)+prime)%prime;
 const trim=a=>{a=a.map(mod);while(a.length&&a[a.length-1]===0)a.pop();return a;};
 const add=(a,b)=>trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||0)+(b[i]||0)));
 const neg=a=>trim(a.map(x=>-x));
 const sub=(a,b)=>add(a,neg(b));
 const scale=(a,c)=>trim(a.map(x=>x*c));
 const mul=(a,b)=>{let r=Array(a.length+b.length-1).fill(0);if(!a.length||!b.length)return [];
  for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)r[i+j]=mod(r[i+j]+a[i]*b[j]);return trim(r);};
 const inv=a=>{for(let j=1;j<prime;j++)if(mod(a*j)===1)return j;throw Error("nonunit");};
 const div=(a,b)=>{a=trim(a);b=trim(b);if(!b.length)throw Error("division zero");let q=Array(Math.max(0,a.length-b.length+1)).fill(0);
  while(a.length>=b.length){let k=a.length-b.length,c=mod(a[a.length-1]*inv(b[b.length-1]));q[k]=mod(q[k]+c);
   a=sub(a,Array(k).fill(0).concat(scale(b,c)));}return [trim(q),a];};
 const eq=(a,b)=>JSON.stringify(trim(a))===JSON.stringify(trim(b));
 const pow=(a,n,f)=>{let r=[1];a=div(a,f)[1];n=BigInt(n);while(n){if(n&1n)r=div(mul(r,a),f)[1];a=div(mul(a,a),f)[1];n>>=1n;}return r;};
 const egcd=(a,b)=>{let s0=[1],s1=[],t0=[],t1=[1],r0=trim(a),r1=trim(b);
  while(r1.length){const[q,r]=div(r0,r1);[r0,r1]=[r1,r];[s0,s1]=[s1,sub(s0,mul(q,s1))];[t0,t1]=[t1,sub(t0,mul(q,t1))];}
  const iv=inv(r0[r0.length-1]);return [scale(r0,iv),scale(s0,iv),scale(t0,iv)];};
 if(mod(original[5])===0)return null;
 const f=scale(original,inv(mod(original[5]))),x=[0,1];let frob=x,sequence=[];
 for(let j=1;j<=5;j++){frob=pow(frob,prime,f);sequence.push(frob);}
 if(!eq(frob,x))return null;
 const xpminusx=sub(sequence[0],x);const[g,s,t]=egcd(f,xpminusx);
 if(!eq(g,[1]))return null;
 if(!eq(add(mul(s,f),mul(t,xpminusx)),[1]))throw Error("reduced Bezout multiplyback");
 const unreduced=Array(prime+1).fill(0);unreduced[1]=-1;unreduced[prime]=1;
 const[quot,rem]=div(unreduced,f);
 if(!eq(rem,xpminusx))throw Error("unreduced Frobenius remainder");
 if(!eq(add(mul(quot,f),rem),unreduced))throw Error("Frobenius division multiplyback");
 const fulls=sub(s,mul(t,quot));
 if(!eq(add(mul(fulls,f),mul(t,unreduced)),[1]))throw Error("full unreduced Bezout multiplyback");
 if(!eq(scale(f,mod(original[5])),trim(original)))throw Error("normalization");
 return {prime,specializationK:1,integerCoefficients:original,degree:5,
  leadingCoefficient:16,monicReduction:f,frobeniusRemainders:sequence,
  rabinPower5ExactlyX:true,rabinOnlyPrimeDegreeDivisor:5,
  gcdWithXPowerPMinusXExactlyOne:true,reducedXPowerPMinusX:xpminusx,bezoutReducedF:s,bezoutReducedSecond:t,
  unreducedDivisionQuotient:quot,bezoutUnreducedF:fulls,bezoutUnreducedSecond:t,
  reducedAndUnreducedBezoutProductsActuallyOne:true,
  fullBezoutProductActuallyOne:true,allSpecializationDegreePreserved:true,fullTwentySevenTermD27SpecializationActuallyVerified:true,originalEContentOneByLeading16k4AndNonzeroConstantAtK0:true,
  conclusion:"D27 is irreducible over QQ(k)[e] by primitive monic-degree-preserving k=1 specialization and this exact mod-p Rabin certificate.",
  finitePointExclusionClaim:false};
}
let result=null;for(const prime of [7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]){
 result=test(prime);if(result)break;
}
if(!result)throw Error("no irreducibility certificate in specified primes");
store("W0_D27_generic_irreducibility_exact_result",result);text(result);
