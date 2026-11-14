// Exact BigInt and finite-field certificate verifier. No network, cache, numerical reconstruction, or symbolic algebra package is required.
function makeSixModeCurvedJets(terms,reverse=false){
 const exps=[];for(let d=0;d<=3;d++){const rec=(a,i,left)=>{if(i===4){exps.push([...a,left]);return;}for(let x=0;x<=left;x++)rec([...a,x],i+1,left-x);};rec([],0,d);}
 const allIndex=new Map(exps.map((e,i)=>[e.join(","),i])), keep=exps.map((e,i)=>e.slice(1).some(Boolean)?i:-1).filter(i=>i>=0);
 const add=(a,b)=>{let c=Array(Math.max(a.length,b.length)).fill(0n);for(let i=0;i<a.length;i++)c[i]+=a[i];for(let i=0;i<b.length;i++)c[i]+=b[i];while(c.length>1&&!c.at(-1))c.pop();return c;};
 const choose=(n,k)=>{if(k<0||k>n)return 0n;let c=1n;for(let j=1;j<=k;j++)c=c*BigInt(n-j+1)/BigInt(j);return c;};
 function monomialJet(alpha){
  const a=reverse?alpha.slice().reverse():alpha, out=exps.map(()=>[0n]);
  for(let j=0;j<exps.length;j++){const e=exps[j];let c=1n,K=a[1];
   for(let i=2;i<6;i++){c*=choose(a[i],e[i-1]);K+=i*(a[i]-e[i-1]);}
   if(!c||K<e[0])continue;c*=choose(K,e[0]);if(!c)continue;
   out[j]=Array(K-e[0]+1).fill(0n);out[j][K-e[0]]=c;
  }
  return out;
 }
 const grads=[];
 for(let i=0;i<6;i++){
  let row=exps.map(()=>[0n]);
  for(const t of terms){if(!t.exponents[i])continue;let a=t.exponents.slice(),c=BigInt(t.coefficient)*BigInt(a[i]--),j=monomialJet(a);for(let k=0;k<j.length;k++)row[k]=add(row[k],j[k].map(v=>v*c));}
  for(let k=0;k<exps.length;k++)if(!exps[k].slice(1).some(Boolean)&&row[k].some(Boolean))throw Error("gradient does not vanish on curve");
  grads.push(row);
 }
 const mults=exps.filter(e=>e.reduce((a,b)=>a+b,0)<=2), rows=[];
 for(let i=0;i<6;i++)for(const m of mults){let row=exps.map(()=>[0n]);for(let j=0;j<exps.length;j++){const e=exps[j].map((x,k)=>x+m[k]);if(e.reduce((a,b)=>a+b,0)>3)continue;row[allIndex.get(e.join(","))]=grads[i][j];}rows.push(keep.map(k=>row[k]));}
 return {exponents:keep.map(k=>exps[k]),rows,monomialJet:alpha=>{let a=monomialJet(alpha);return keep.map(k=>a[k]);},allExponents:exps};
}
function sixRationalAlgebra(modulus){
 const f=modulus.map(BigInt),d=f.length-1;
 function gcd(a,b){if(a<0n)a=-a;if(b<0n)b=-b;while(b)[a,b]=[b,a%b];return a;}
 function make(n,den=1n){if(!den)throw Error("zero denominator");n=n.slice();while(n.length<d)n.push(0n);n.length=d;if(den<0n){den=-den;n=n.map(x=>-x);}let g=den;for(const x of n){g=gcd(g,x);if(g===1n)break;}if(g!==1n){den/=g;n=n.map(x=>x/g);}return{n,d:den};}
 const zero=()=>make(Array(d).fill(0n)),one=()=>make([1n]),iszero=a=>a.n.every(x=>!x);
 function reduce(n){n=n.slice();for(let k=n.length-1;k>=d;k--)if(n[k]){let x=n[k];for(let j=0;j<d;j++)n[k-d+j]-=x*f[j];}return Array.from({length:d},(_,i)=>n[i]||0n);}
 function add(a,b){const g=gcd(a.d,b.d),u=b.d/g,v=a.d/g;return make(a.n.map((x,i)=>x*u+b.n[i]*v),a.d*u);}
 function neg(a){return{n:a.n.map(x=>-x),d:a.d};}
 function sub(a,b){const g=gcd(a.d,b.d),u=b.d/g,v=a.d/g;return make(a.n.map((x,i)=>x*u-b.n[i]*v),a.d*u);}
 function mul(a,b){if(iszero(a)||iszero(b))return zero();let c=Array(2*d-1).fill(0n);for(let i=0;i<d;i++)if(a.n[i])for(let j=0;j<d;j++)if(b.n[j])c[i+j]+=a.n[i]*b.n[j];return make(reduce(c),a.d*b.d);}
 const scale=(a,c)=>make(a.n.map(x=>x*c),a.d);
 function frac(n,den){if(den<0n){n=-n;den=-den;}let g=gcd(n,den);return[n/g,den/g];}
 function inv(a){
  if(iszero(a))return null;const A=Array.from({length:d},()=>Array(d+1).fill(0n));
  for(let j=0;j<d;j++){const c=reduce([...Array(j).fill(0n),...a.n]);for(let i=0;i<d;i++)A[i][j]=c[i];}A[0][d]=1n;
  let previous=1n;for(let k=0;k<d-1;k++){let r=k;while(r<d&&!A[r][k])r++;if(r===d)return null;if(r!==k)[A[r],A[k]]=[A[k],A[r]];let pivot=A[k][k];
   for(let i=k+1;i<d;i++){for(let j=k+1;j<=d;j++){let v=pivot*A[i][j]-A[i][k]*A[k][j];if(v%previous)throw Error("nonexact inverse Bareiss");A[i][j]=v/previous;}A[i][k]=0n;}previous=pivot;
  }
  if(!A[d-1][d-1])return null;let x=Array(d);
  for(let i=d-1;i>=0;i--){let n=A[i][d],den=1n;for(let j=i+1;j<d;j++){let g=gcd(den,x[j][1]),u=x[j][1]/g,v=den/g;n=n*u-A[i][j]*x[j][0]*v;den*=u;[n,den]=frac(n,den);}x[i]=frac(n,den*A[i][i]);}
  let den=1n;for(const v of x)den=den/gcd(den,v[1])*v[1];let v=make(x.map(t=>t[0]*(den/t[1])*a.d),den);let test=mul(a,v);if(test.d!==1n||test.n[0]!==1n||test.n.slice(1).some(Boolean))throw Error("inverse identity");return v;
 }
 return{d,f,gcd,make,zero,one,iszero,reduce,add,sub,mul,scale,neg,inv,serialize:a=>({n:a.n.map(String),d:String(a.d)})};
}

function sixModAlgebra(p,modulus){
 const m=x=>{x%=p;return x<0?x+p:x;}, d=modulus.length-1, f=modulus.map(m);
 function scalarInv(x){let a=p,b=m(x),u=0,v=1;while(b){let q=Math.floor(a/b);[a,b]=[b,a-q*b];[u,v]=[v,u-q*v];}if(a!==1)throw Error("scalar nonunit");return m(u);}
 const trim=a=>{while(a.length>1&&!a.at(-1))a.pop();return a;};
 function psub(a,b){let c=Array(Math.max(a.length,b.length)).fill(0);for(let i=0;i<c.length;i++)c[i]=m((a[i]||0)-(b[i]||0));return trim(c);}
 function pmul(a,b){let c=Array(a.length+b.length-1).fill(0);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]=m(c[i+j]+a[i]*b[j]);return trim(c);}
 function divrem(a,b){a=a.slice();let q=Array(Math.max(1,a.length-b.length+1)).fill(0),iv=scalarInv(b.at(-1));while(a.length>=b.length&&a.some(Boolean)){const k=a.length-b.length,c=m(a.at(-1)*iv);q[k]=c;for(let i=0;i<b.length;i++)a[k+i]=m(a[k+i]-c*b[i]);trim(a);}return{q:trim(q),r:a};}
 function reduce(a){a=a.slice();for(let k=a.length-1;k>=d;k--)if(a[k]){let x=a[k];for(let j=0;j<d;j++)a[k-d+j]=m(a[k-d+j]-x*f[j]);}return Array.from({length:d},(_,i)=>m(a[i]||0));}
 const zero=()=>Array(d).fill(0),one=()=>[1,...Array(d-1).fill(0)],iszero=a=>!a.some(Boolean);
 const add=(a,b)=>a.map((x,i)=>m(x+b[i])),sub=(a,b)=>a.map((x,i)=>m(x-b[i])),mul=(a,b)=>reduce(pmul(a,b)),scale=(a,c)=>a.map(x=>m(x*c));
 function inv(a){if(iszero(a))return null;let r0=f.slice(),r1=trim(a.slice()),s0=[0],s1=[1];while(r1.some(Boolean)){let {q,r}=divrem(r0,r1);[r0,r1]=[r1,r];[s0,s1]=[s1,psub(s0,pmul(q,s1))];}if(r0.length!==1)return null;return scale(reduce(s0),scalarInv(r0[0]));}
 return{p,d,f,m,scalarInv,zero,one,iszero,add,sub,mul,scale,inv,reduce};
}

function sixMonomials(n,d){const out=[];function rec(a,i,left){if(i===n-1){out.push([...a,left]);return;}for(let x=0;x<=left;x++)rec([...a,x],i+1,left-x);}rec([],0,d);return out;}
function sixModGlobalLeftCertificate(terms,local,engine,jetFactory,p=103){
 const mons=sixMonomials(6,10), rows=Array.from({length:85},()=>new Uint16Array(mons.length));let rowOffset=51;
 for(let col=0;col<mons.length;col++){const a=mons[col];rows[a.reduce((s,x,i)=>s+x*i,0)][col]=1;}
 const details=[];
 for(const [name,reverse]of [["zero",false],["infinity",true],["double",false],["simple",false]]){
  const item=local[name],F=engine.sixModAlgebra(p,item.modulus),J=jetFactory(terms,reverse),z=F.scale(F.reduce([0,1]),F.scalarInv(5));
  const powers=[F.one()];for(let k=1;k<=50;k++)powers.push(F.mul(powers.at(-1),z));
  const lookup=item.basis.map(b=>b.map(c=>powers.map(zp=>F.mul(c,zp))));
  for(let col=0;col<mons.length;col++){const jets=J.monomialJet(mons[col]);for(let bi=0;bi<item.basis.length;bi++){let value=F.zero();for(let j=0;j<jets.length;j++){const poly=jets[j];for(let k=0;k<poly.length;k++)if(poly[k])value=F.add(value,F.scale(lookup[bi][j][k],Number(poly[k]%BigInt(p))));}for(let k=0;k<F.d;k++)rows[rowOffset+bi*F.d+k][col]=value[k];}}
  details.push({name,from:rowOffset,count:item.basis.length*F.d});rowOffset+=item.basis.length*F.d;
 }
 const nodes=[["990895","1153105","2063840","4524760","11260192","30644640"],["143682655","-222517655","664053920","-4306767840","39985265088","-450141192000"]];
 const mod=x=>{x%=p;return x<0?x+p:x;}, inv=x=>{let a=p,b=mod(x),u=0,v=1;while(b){let q=Math.floor(a/b);[a,b]=[b,a-q*b];[u,v]=[v,u-q*v];}if(a!==1)throw Error("nonunit");return mod(u);};
 for(const node of nodes){const ps=node.map(x=>{let a=[1],v=Number((BigInt(x)%BigInt(p)+BigInt(p))%BigInt(p));for(let j=1;j<=10;j++)a.push(mod(a.at(-1)*v));return a;});for(let c=0;c<mons.length;c++)rows[rowOffset][c]=mons[c].reduce((s,x,i)=>mod(s*ps[i][x]),1);rowOffset++;}
 if(rowOffset!==85)throw Error("left-row count");
 const A=rows.map(r=>Array.from(r)),pivotColumns=[];let rank=0,det=1;
 for(let col=0;col<mons.length&&rank<A.length;col++){let k=rank;while(k<A.length&&!A[k][col])k++;if(k===A.length)continue;if(k!==rank){[A[k],A[rank]]=[A[rank],A[k]];det=mod(-det);}let v=A[rank][col];det=mod(det*v);let iv=inv(v);for(let j=col;j<mons.length;j++)A[rank][j]=mod(A[rank][j]*iv);for(let i=rank+1;i<A.length;i++)if(A[i][col]){let x=A[i][col];for(let j=col;j<mons.length;j++)A[i][j]=mod(A[i][j]-x*A[rank][j]);}pivotColumns.push(col);rank++;}
 return{rank,p,pivotColumns,pivotMonomials:pivotColumns.map(i=>mons[i]),minorDeterminant:det,details,rowCount:rows.length,columnCount:mons.length,rows:rows.map(r=>Array.from(r))};
}
async function sixVerifyImageRankMinor(integerData,seed,onProgress){
 const p=103,n=2918,mons=sixMonomials(6,10),mult=sixMonomials(6,7),index=new Map(mons.map((e,i)=>[e.join(","),i]));
 if(seed.prime!==p||seed.pivotColumns.length!==n||seed.pivotOriginalRows.length!==n||new Set(seed.pivotColumns).size!==n||new Set(seed.pivotOriginalRows).size!==n)throw Error("invalid image minor indices");
 const rowPosition=new Int32Array(3003);rowPosition.fill(-1);seed.pivotOriginalRows.forEach((v,i)=>{if(v<0||v>=3003)throw Error("minor row");rowPosition[v]=i;});
 const U=Array.from({length:n},()=>new Uint8Array(n));
 const termData=integerData.quarticIntegerTerms.map(t=>({e:t.exponents,c:Number((BigInt(t.coefficient)%103n+103n)%103n)}));
 for(let j=0;j<n;j++){const col=seed.pivotColumns[j];if(col<0||col>=4752)throw Error("minor column");const i=Math.floor(col/792),alpha=mult[col%792];for(const term of termData){if(!term.e[i])continue;const e=term.e.map((v,k)=>v+alpha[k]-Number(k===i)),r=rowPosition[index.get(e.join(","))];if(r>=0)U[r][j]=(U[r][j]+term.c*term.e[i])%p;}}
 const table=new Uint16Array(p*p);for(let i=0;i<p;i++)for(let j=0;j<p;j++)table[i*p+j]=i*j%p;
 const pow=(a,n)=>{let r=1;for(;n;n=Math.floor(n/2),a=a*a%p)if(n%2)r=r*a%p;return r;};
 let det=1;for(let k=0;k<n;k++){const pivot=U[k][k];if(!pivot)throw Error("image minor zero pivot "+k);det=det*pivot%p;const iv=pow(pivot,p-2),ids=[],vals=[];for(let j=k+1;j<n;j++)if(U[k][j]){ids.push(j);vals.push(U[k][j]);}
 for(let i=k+1;i<n;i++){if(!U[i][k])continue;const factor=table[U[i][k]*p+iv],c=factor*p,row=U[i];row[k]=0;for(let j=0;j<ids.length;j++){let v=row[ids[j]]-table[c+vals[j]];if(v<0)v+=p;row[ids[j]]=v;}}
 if(onProgress&&(k+1)%200===0)await onProgress({stage:"image_rank_minor",pivots:k+1,n});
 }
 if(det!==35)throw Error("image minor determinant mismatch "+det);
 return{rankAtLeast:n,prime:p,determinant:det,rebuiltFromOriginalIntegerGradient:true};
}
async function verifySixModeJacobianJetCertificate(integerData,jetCertificate,modularSeed,options={}){
 const cases=[["zero",false,["0","1"],3],["infinity",true,["0","1"],3],["double",false,["-4320000","2592000","124200","-65000","1105","110","1"],3],["simple",false,["750000000","-398000000","-10600000","9960000","-361000","-23400","765","50","1"],1]];
 const localMod={},localChecks=[];let rationalIdentityCount=0,componentCount=0;
 for(const [name,reverse,modulus,dim]of cases){
  const item=jetCertificate.local[name];if(JSON.stringify(item.modulus)!==JSON.stringify(modulus)||item.basis.length!==dim)throw Error("local certificate shape "+name);
  const F=sixRationalAlgebra(modulus),J=makeSixModeCurvedJets(integerData.quarticIntegerTerms,reverse);
  const z=F.make(F.reduce([0n,1n]),5n),powers=[F.one()];for(let k=1;k<=15;k++)powers.push(F.mul(powers.at(-1),z));
  const cache=new Map(),cv=poly=>{let key=poly.join(",");if(cache.has(key))return cache.get(key);let v=F.zero();for(let k=0;k<poly.length;k++)if(poly[k])v=F.add(v,F.scale(powers[k],BigInt(poly[k])));cache.set(key,v);return v;};
  const A=J.rows.map(r=>r.map(cv)),basis=item.basis.map(b=>{if(b.length!==52)throw Error("jet count");return b.map(a=>{if(a.n.length!==F.d||BigInt(a.d)<=0n)throw Error("rational field coefficient");return F.make(a.n.map(BigInt),BigInt(a.d));});});
  for(const b of basis)for(const row of A){let v=F.zero();for(let j=0;j<52;j++)if(!F.iszero(b[j])&&!F.iszero(row[j]))v=F.add(v,F.mul(b[j],row[j]));if(!F.iszero(v))throw Error("exact local identity "+name);rationalIdentityCount++;componentCount+=F.d;}
  const FM=sixModAlgebra(103,modulus.map(x=>Number(BigInt(x)%103n))),bmod=basis.map(b=>b.map(a=>{const den=Number(a.d%103n);if(!den)throw Error("bad denominator for independence prime");return a.n.map(n=>FM.m(Number(n%103n)*FM.scalarInv(den)));}));
  localMod[name]={basis:bmod,modulus:FM.f,p:103};
  localChecks.push({name,algebraDimension:F.d,extraFunctionals:F.d*dim,allOriginalLocalIdentitiesExact:true});
  if(options.onProgress)await options.onProgress({stage:"exact_local_jets",name});
 }
 const global=sixModGlobalLeftCertificate(integerData.quarticIntegerTerms,localMod,{sixModAlgebra},makeSixModeCurvedJets,103);
 if(global.rank!==85||global.minorDeterminant!==jetCertificate.globalMod103.determinant||JSON.stringify(global.pivotColumns)!==JSON.stringify(jetCertificate.globalMod103.pivotColumns))throw Error("global left-rank minor");
 const exps=integerData.quadraticExponents,Q=integerData.BellQuadraticIntegerCoefficients.map(r=>r.map(BigInt));
 if(exps.length!==21||Q.length!==21||Q.some(r=>r.length!==3))throw Error("Bell shape");
 const curve=Array.from({length:11},()=>[0n,0n,0n]);for(let i=0;i<21;i++){const k=exps[i].reduce((s,x,j)=>s+x*j,0);for(let a=0;a<3;a++)curve[k][a]+=Q[i][a];}
 if(curve.flat().some(Boolean))throw Error("Bell RNC vanishing");
 const expectedNodes=[["990895","1153105","2063840","4524760","11260192","30644640"],["143682655","-222517655","664053920","-4306767840","39985265088","-450141192000"]];
 if(JSON.stringify(jetCertificate.nodes)!==JSON.stringify(expectedNodes))throw Error("nodes");
 for(const ns of expectedNodes){const n=ns.map(BigInt);let value=[0n,0n,0n],grad=Array(6).fill(0n);
 for(let i=0;i<21;i++){const v=exps[i].reduce((s,x,j)=>s*n[j]**BigInt(x),1n);for(let a=0;a<3;a++)value[a]+=Q[i][a]*v;}
 for(let i=0;i<6;i++)for(const term of integerData.quarticIntegerTerms){const e=term.exponents.slice();if(!e[i])continue;let v=BigInt(term.coefficient)*BigInt(e[i]--);for(let j=0;j<6;j++)v*=n[j]**BigInt(e[j]);grad[i]+=v;}
 if(value.some(Boolean)||grad.some(Boolean))throw Error("node exact identities");
 }
 const lower=options.skipImageMinor?{notRerun:true,requiresPreviouslyVerifiedImageRank2918:true}:await sixVerifyImageRankMinor(integerData,modularSeed,options.onProgress);
 return{all_pass:!options.skipImageMinor,localAndTargetAndLeftRankPass:true,rationalIdentityCount,rationalCoefficientIdentities:componentCount,localChecks,leftRank:85,leftRankPrime:103,leftMinorDeterminant:global.minorDeterminant,imageMinor:lower,exactBellCurveAndTwoNodeVanishing:true,
 conclusion:options.skipImageMinor?"Partial check: image-rank lower bound must be independently supplied.":"Over Q, the homogeneous degree-ten Jacobian image is exactly the kernel of the 85 rational functionals. All three coefficients of q_integer^5 belong to that image.",
 scope:"Finite characteristic-zero ideal membership for the stated quartic and Bell quadratic. Operator consequences require the separately proved Schur lift and actual Bell inverse bridge."};
}

