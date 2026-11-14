// Inputs: the published exact-data JSON object and the compact recovery-certificate JSON object.
function verifyCandidateCertificate(data,certificate){
 const N=certificate.N,P=certificate.prime;
 const nm=x=>(x%P+P)%P, pw=(a,n)=>{let r=1;for(;n;n=Math.floor(n/2),a=a*a%P)if(n%2)r=r*a%P;return r;};
 const md=x=>{let r=BigInt(x)%BigInt(P);if(r<0n)r+=BigInt(P);return Number(r);},rt=c=>{const denominator=md(c[1]);if(!denominator)throw Error("invalid rational reduction denominator");return md(c[0])*pw(denominator,P-2)%P;};
 const fa=(a,b)=>a.map((v,i)=>nm(v+b[i])),fn=a=>a.map(v=>nm(-v)),fs=(a,s)=>a.map(v=>nm(v*s));
 const cp=[52565262336n,6080833024n,-43931504n].map(v=>md(v)*pw(md(3725n),P-2)%P);
 const fm=(a,b)=>{const c=Array(5).fill(0);for(let i=0;i<3;i++)for(let j=0;j<3;j++)c[i+j]=nm(c[i+j]+a[i]*b[j]);for(let k=4;k>=3;k--)for(let j=0;j<3;j++)c[k-3+j]=nm(c[k-3+j]-c[k]*cp[j]);return c.slice(0,3);};
 const fi=a=>{const A=Array.from({length:3},(_,r)=>[...Array.from({length:3},(_,j)=>fm(a,Array.from({length:3},(_,i)=>Number(i===j)))[r]),Number(r===0)]);for(let k=0;k<3;k++){let p=k;while(p<3&&!A[p][k])p++;if(p===3)throw Error("candidate denominator not a unit");[A[p],A[k]]=[A[k],A[p]];let inv=pw(A[k][k],P-2);A[k]=A[k].map(v=>v*inv%P);for(let i=0;i<3;i++)if(i!==k){let c=A[i][k];A[i]=A[i].map((v,j)=>nm(v-c*A[k][j]));}}return A.map(r=>r[3]);};
 const one=[1,0,0],zero=[0,0,0],d=[0,1,0],d2=[0,0,1];
 const A=fm(fn([271360,-46784,521].map(nm)),fi([-160*704,160*5,0].map(nm)));
 const B=fa(A,d),rr=[A,B,zero,zero,zero,one];
 const f=fa(fa(fa(fa(fa(fs(fm(A,A),-279),fs(fm(A,B),-242)),fs(A,-65856)),fs(fm(B,B),521)),fs(B,-46784)),fs(one,271360));
 const g=fa(fa(fa(fa(fa(fs(fm(A,A),-1769),fs(fm(A,B),2738)),fs(A,-16087680)),fs(fm(B,B),-969)),fs(B,19820160)),fs(one,140341248));
 if(f.some(v=>v)||g.some(v=>v))throw Error("two node candidate equations failed");
 const mons=(n,d,p=[])=>{if(n===1)return[[...p,d]];let a=[];for(let k=0;k<=d;k++)a.push(...mons(n-1,d-k,[...p,k]));return a;};
 const e2=data.quadraticExponents, k2=new Map(e2.map((e,i)=>[e.join(","),i])),qb=e2.map(()=>[0,0,0]);
 for(let i=0;i<6;i++)for(let j=0;j<6;j++){const c=fm(rr[i],rr[j]);if(!c.some(v=>v))continue;const e=Array(6).fill(0);e[i]++;e[j]++;const ind=k2.get(e.join(","));for(let t=0;t<21;t++)qb[t]=fa(qb[t],fs(c,nm((t===ind?1:0)-rt(data.SchurH2coeff[i+j][t]))));}
 let ex=e2,coeff=qb;
 for(let n=2;n<=N;n++){const en=mons(6,2*n),kn=new Map(en.map((e,i)=>[e.join(","),i])),cn=en.map(()=>[0,0,0]);for(let a=0;a<ex.length;a++)for(let b=0;b<21;b++){if(!coeff[a].some(v=>v)||!qb[b].some(v=>v))continue;const key=ex[a].map((v,i)=>v+e2[b][i]).join(","),idx=kn.get(key);cn[idx]=fa(cn[idx],fm(coeff[a],qb[b]));}ex=en;coeff=cn;}

 const mult=mons(6,2*N-3),cols=mult.length*6,rows=ex.length,kex=new Map(ex.map((e,i)=>[e.join(","),i]));
 if(certificate.rows!==rows||certificate.columns!==cols||certificate.multiplierCount!==mult.length)throw Error("dimension mismatch");
 if(certificate.pivotColumns.length!==certificate.solutionsAtPivotColumns.length)throw Error("solution length mismatch");
 const solutions=Array.from({length:cols},()=>[0,0,0]),seen=new Set();
 certificate.pivotColumns.forEach((col,k)=>{if(col<0||col>=cols||seen.has(col))throw Error("invalid or duplicate column");seen.add(col);const v=certificate.solutionsAtPivotColumns[k];if(v.length!==3||v.some(x=>!Number.isInteger(x)||x<0||x>=P))throw Error("invalid field element");solutions[col]=v;});
 const check=Array.from({length:rows},()=>[0,0,0]);
 for(let i=0;i<6;i++)for(let t=0;t<mult.length;t++){
   const col=i*mult.length+t;if(!solutions[col].some(v=>v))continue;
   for(const term of data.Rterms){if(!term.exponents[i])continue;
     const e=term.exponents.map((v,j)=>v+mult[t][j]-Number(i===j)),row=kex.get(e.join(","));
     if(row===undefined)throw Error("monomial missing");
     const a=rt(term.coefficient)*term.exponents[i]%P;
     for(let k=0;k<3;k++)check[row][k]=nm(check[row][k]+a*solutions[col][k]);
   }
 }
 const failures=[];
 check.forEach((r,i)=>r.forEach((v,t)=>{if(v!==coeff[i][t])failures.push({exponents:ex[i],ringCoefficient:t,left:v,right:coeff[i][t]});}));
 return{N,prime:P,rows,gradientMultiplierColumns:cols,coefficientIdentitiesChecked:3*rows,nonzeroMultiplierColumns:solutions.filter(r=>r.some(v=>v)).length,all_pass:failures.length===0,failures:failures.slice(0,5),scope:"Exact polynomial identity over the displayed finite field quotient only. Pivot rank is not needed or reasserted by this verifier."};
}

if (typeof module !== "undefined") module.exports={verifyCandidateCertificate};
if (typeof require !== "undefined" && require.main === module) {
  const fs=require("node:fs"),path=require("node:path");
  const data=JSON.parse(fs.readFileSync(path.join(__dirname,"2026-11-13-six-mode-second-moment-exact-data.json"),"utf8"));
  const certificate=JSON.parse(fs.readFileSync(path.join(__dirname,"2026-11-13-six-mode-fifth-power-mod103-certificate.json"),"utf8"));
  const result=verifyCandidateCertificate(data,certificate);
  console.log(JSON.stringify(result,null,2));
  if (!result.all_pass) process.exitCode=1;
}
