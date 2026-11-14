
function dixonGcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a;}
function buildDixonIntegerProblem(integerData){
const cp=integerData.field.monicCubicCoefficients.slice(0,3).map(BigInt);
function rm(a,b){const c=Array(5).fill(0n);for(let i=0;i<3;i++)for(let j=0;j<3;j++)c[i+j]+=a[i]*b[j];for(let k=4;k>=3;k--)for(let j=0;j<3;j++)c[k-3+j]-=c[k]*cp[j];return c.slice(0,3);}
const e2=integerData.quadraticExponents,q=integerData.BellQuadraticIntegerCoefficients.map(row=>row.map(BigInt));
let ex=e2,coeff=q;
for(let n=2;n<=5;n++){
 const en=dixonMonomials(6,2*n),kn=new Map(en.map((e,i)=>[e.join(","),i])),cn=en.map(()=>[0n,0n,0n]);
 for(let i=0;i<ex.length;i++){if(!coeff[i].some(v=>v))continue;for(let j=0;j<q.length;j++){if(!q[j].some(v=>v))continue;const row=kn.get(ex[i].map((v,k)=>v+e2[j][k]).join(",")),a=rm(coeff[i],q[j]);for(let k=0;k<3;k++)cn[row][k]+=a[k];}}
 ex=en;coeff=cn;
}
let content=0n,maxBefore=0;for(const row of coeff)for(const a of row){content=dixonGcd(content,a);const d=(a<0n?-a:a).toString().length;if(d>maxBefore)maxBefore=d;}
if(!content)throw Error("zero integer target");
const reduced=coeff.map(row=>row.map(a=>a/content));let maxAfter=0;for(const row of reduced)for(const a of row)maxAfter=Math.max(maxAfter,(a<0n?-a:a).toString().length);
return{integerDataSha:"91416b837b7b95b67cce7cc07fca3f250b179877",degree:10,field:integerData.field,rows:ex.length,exponents:ex,rhs:reduced.map(row=>row.map(String)),rhsContent:String(content),maxDigitsBeforeContent:maxBefore,maxDigitsAfterContent:maxAfter,identity:"rhs = coefficient vectors of q_integer^5 divided by the nonzero common integer content"};
}
