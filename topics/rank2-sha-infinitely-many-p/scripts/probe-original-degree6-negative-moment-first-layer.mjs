// Exact ordinary first-layer coefficients of the original degree-six negative moments.
// node probe-original-degree6-negative-moment-first-layer.mjs [exclusive-limit<=20000]
import fs from "node:fs";
function calc(p){
 const mod=x=>(x%p+p)%p,pow=(a,n)=>{let r=1;for(a=mod(a);n;n=Math.floor(n/2),a=a*a%p)if(n%2)r=r*a%p;return r;},iv=a=>{if(mod(a)===0)throw Error("zero denominator");return pow(a,p-2);};
 const n=(p-1)/6-1,A=Array(n+1).fill(0),S=Array(n+1).fill(0),L=Array(n+1).fill(0),B=Array(n+1).fill(0);
 A[0]=S[0]=B[0]=1;if(n>=1)A[1]=mod(-iv(7));
 for(let k=2;k<=n;k++){let t=0;for(let j=1;j<k;j++)t=mod(t+A[j]*A[k-j]);A[k]=mod(t*iv((6*k+1)*(k-1)));}
 for(let k=1;k<=n;k++){L[k]=mod(-A[k]*iv(k*(6*k-1)));B[k]=mod(-(3*k-1)*A[k]);let t=0;for(let j=1;j<=k;j++)t=mod(t+j*L[j]*S[k-j]);S[k]=mod(t*iv(k));}
 const mul=(x,y)=>{const o=Array(n+1).fill(0);for(let i=0;i<=n;i++)for(let j=0;j<=n-i;j++)o[i+j]=mod(o[i+j]+x[i]*y[j]);return o;};
 const F4=mul(A,S),F1=mul(F4,B);
 return {p,n,c4:F4[n],c1:F1[n],ratio:F4[n]?mod(F1[n]*iv(F4[n])):null};
}
const limit=Number(process.argv[2]??2000);
if(!Number.isInteger(limit)||limit<14||limit>20000)throw Error("limit must be an integer in [14,20000]");
const rows=[];
for(let p=13;p<limit;p+=6){
 let prime=true;
 for(let q=2;q*q<=p;q++)if(p%q===0){prime=false;break;}
 if(prime)rows.push(calc(p));
}
const output={status:"finite exact evidence only",curve_b:17,limit_exclusive:limit,
 normalization:"c4=[u^((p-7)/6)]AS; c1=[u^((p-7)/6)]ABS; u=17z^6",
 count:rows.length,zeros_c4:rows.filter(r=>r.c4===0).map(r=>r.p),
 zeros_c1:rows.filter(r=>r.c1===0).map(r=>r.p),
 simultaneous_zeros:rows.filter(r=>r.c4===0&&r.c1===0).map(r=>r.p),rows};
fs.writeFileSync(new URL("./probe-original-degree6-negative-moment-first-layer.json",import.meta.url),JSON.stringify(output,null,2)+"\n");
console.log(JSON.stringify({count:output.count,zeros_c4:output.zeros_c4,zeros_c1:output.zeros_c1,simultaneous_zeros:output.simultaneous_zeros}));
