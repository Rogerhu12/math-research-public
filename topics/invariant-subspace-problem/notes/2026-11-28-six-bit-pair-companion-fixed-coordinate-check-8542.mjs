// Fixed positive z point only; the general coordinate proof is in the companion source note.
const result=(()=>{

const n=6,z=[1n,2n,3n,4n,5n,6n],pairs=[];for(let a=0;a<n;a++)for(let b=a+1;b<n;b++)pairs.push([a,b]);
const index=new Map(pairs.map((p,i)=>[p.join(","),i])),m=pairs.length;
function zero(r,c){return Array.from({length:r},()=>Array(c).fill(0n));}
function mm(A,B){return A.map(row=>B[0].map((_,j)=>row.reduce((s,v,k)=>s+v*B[k][j],0n)));}
function eq(A,B,label){if(A.some((r,i)=>r.some((x,j)=>x!==B[i][j])))throw Error(label);}
const es=[1n,...Array(n).fill(0n)];for(const x of z)for(let j=n;j>0;j--)es[j]+=x*es[j-1];
const T=zero(n,n);for(let j=0;j<n-1;j++)T[j+1][j]=1n;for(let i=0;i<n;i++)T[i][n-1]=BigInt((-1)**(n-i+1))*es[n-i];
const vp=[Array.from({length:n},(_,i)=>i===0?1n:0n)];
for(let k=1;k<=2*n;k++)vp.push(T.map(row=>row.reduce((s,x,j)=>s+x*vp[k-1][j],0n)));
function wedge(a,b){return pairs.map(([i,j])=>a[i]*b[j]-a[j]*b[i]);}
const ep=Array.from({length:n},(_,j)=>Array.from({length:n},(_,i)=>i===j?1n:0n));
const U=zero(m,m);for(let k=0;k<m;k++){const[a,b]=pairs[k],Ta=T.map(row=>row[a]),Tb=T.map(row=>row[b]),q=wedge(Ta,ep[b]),r=wedge(ep[a],Tb);for(let i=0;i<m;i++)U[i][k]=q[i]+r[i];}
const R=zero(n,m);for(let k=0;k<m;k++){const[a,b]=pairs[k];for(let r=0;r<b-a;r++){const moment=z.reduce((s,x)=>s+x**BigInt(b-r),0n);for(let i=0;i<n;i++)R[i][k]+=moment*vp[a+r][i];}for(let i=0;i<n;i++)R[i][k]-=BigInt(b-a)*vp[a+b][i];}
const Rs=zero(m,n);for(let k=0;k<n;k++){const q=wedge(ep[0],vp[k+1]),r=wedge(ep[1],vp[k]);for(let i=0;i<m;i++)Rs[i][k]=q[i]-r[i];}
const V=z.map(x=>Array.from({length:n},(_,k)=>x**BigInt(k)));
const W=pairs.map(([i,j])=>pairs.map(([a,b])=>(z[i]**BigInt(a)*z[j]**BigInt(b)-z[i]**BigInt(b)*z[j]**BigInt(a))/(z[j]-z[i])));
const realR=zero(n,m),realRs=zero(m,n);
for(let k=0;k<m;k++){const[i,j]=pairs[k];realR[i][k]=z[j];realR[j][k]=z[i];realRs[k][i]=1n;realRs[k][j]=1n;}
eq(mm(V,R),mm(realR,W),"lowering");
eq(mm(W,Rs),mm(realRs,V),"physical adjoint");
eq(mm(W,U),W.map((row,k)=>row.map(v=>v*(z[pairs[k][0]]+z[pairs[k][1]]))),"pair multiplication");
const F1=mm(R,Rs),realF1=mm(realR,realRs);
eq(mm(V,F1),mm(realF1,V),"complete low Gram");
const FU=mm(Rs,R);for(let i=0;i<m;i++)for(let j=0;j<m;j++)FU[i][j]+=(i===j?es[1]:0n)-2n*U[i][j];
const actualFU=mm(realRs,realR);for(let i=0;i<m;i++)actualFU[i][i]+=es[1]-2n*(z[pairs[i][0]]+z[pairs[i][1]]);
eq(mm(W,FU),mm(actualFU,W),"complete upper Gram");
return {status:"exact_single_parameter_coordinate_calibration",z:z.map(String),identities:5,dimension:15,scope:"Only this fixed-point exact calibration; general formulas require their stated algebraic proof."};

})();
console.log(JSON.stringify(result,null,2));
