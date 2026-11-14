
function dixonMonomials(n,d,p=[]){if(n===1)return[[...p,d]];const out=[];for(let k=0;k<=d;k++)out.push(...dixonMonomials(n-1,d-k,[...p,k]));return out;}
function dixonPow(a,n,p){let r=1;for(;n;n=Math.floor(n/2),a=a*a%p)if(n%2)r=r*a%p;return r;}
function dixonMulTable(p){const t=new Uint16Array(p*p);for(let a=0;a<p;a++)for(let b=0;b<p;b++)t[a*p+b]=a*b%p;return t;}
function dixonSolve3(LU,inverseDiagonal,rhs,p,table){
const n=LU.length,nm=a=>(a%p+p)%p,y=Array.from({length:n},()=>[0,0,0]),x=Array.from({length:n},()=>[0,0,0]);
for(let i=0;i<n;i++){let a=rhs[i][0],b=rhs[i][1],c=rhs[i][2];const row=LU[i];for(let j=0;j<i;j++)if(row[j]){const t=row[j]*p;a-=table[t+y[j][0]];b-=table[t+y[j][1]];c-=table[t+y[j][2]];}y[i]=[nm(a),nm(b),nm(c)];}
for(let i=n-1;i>=0;i--){let a=y[i][0],b=y[i][1],c=y[i][2];const row=LU[i];for(let j=i+1;j<n;j++)if(row[j]){const t=row[j]*p;a-=table[t+x[j][0]];b-=table[t+x[j][1]];c-=table[t+x[j][2]];}const t=inverseDiagonal[i]*p;x[i]=[table[t+nm(a)],table[t+nm(b)],table[t+nm(c)]];}
return x;
}
function dixonEncode64(bytes){
const c="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",parts=[];let s="";
for(let i=0;i<bytes.length;i+=3){const a=bytes[i],b=i+1<bytes.length?bytes[i+1]:0,d=i+2<bytes.length?bytes[i+2]:0;s+=c[a>>2]+c[((a&3)<<4)|(b>>4)]+(i+1<bytes.length?c[((b&15)<<2)|(d>>6)]:"=")+(i+2<bytes.length?c[d&63]:"=");if(s.length>=8192){parts.push(s);s="";}}if(s)parts.push(s);return parts.join("");
}
function dixonDecode64(s){
const c="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",map=new Int16Array(128);map.fill(-1);for(let i=0;i<64;i++)map[c.charCodeAt(i)]=i;
const n=s.length/4*3-(s.endsWith("==")?2:s.endsWith("=")?1:0),out=new Uint8Array(n);let k=0;
for(let i=0;i<s.length;i+=4){const a=map[s.charCodeAt(i)],b=map[s.charCodeAt(i+1)],c0=s[i+2]==="="?0:map[s.charCodeAt(i+2)],d=s[i+3]==="="?0:map[s.charCodeAt(i+3)];out[k++]=(a<<2)|(b>>4);if(k<n)out[k++]=((b&15)<<4)|(c0>>2);if(k<n)out[k++]=((c0&3)<<6)|d;}return out;
}
async function prepareDixonLU(integerData,certificate,prefix){
const p=certificate.prime,n=certificate.pivotColumns.length,rowsTotal=certificate.rows;
if(p>255)throw Error("Uint8 factor requires p<=255");
const mons=dixonMonomials(6,10),mult=dixonMonomials(6,7),index=new Map(mons.map((e,i)=>[e.join(","),i]));
const rowPosition=new Int32Array(rowsTotal);rowPosition.fill(-1);certificate.pivotOriginalRows.forEach((v,i)=>rowPosition[v]=i);
const LU=Array.from({length:n},()=>new Uint8Array(n)),seedRhs=Array.from({length:n},()=>[0,0,0]);
const termData=integerData.quarticIntegerTerms.map(t=>({e:t.exponents,c:Number((BigInt(t.coefficient)%BigInt(p)+BigInt(p))%BigInt(p))}));
const table=dixonMulTable(p);
for(let j=0;j<n;j++){
const col=certificate.pivotColumns[j],i=Math.floor(col/mult.length),t=col%mult.length,sol=certificate.solutionsAtPivotColumns[j];
for(const term of termData){if(!term.e[i])continue;const e=term.e.map((v,k)=>v+mult[t][k]-Number(k===i)),originalRow=index.get(e.join(",")),r=rowPosition[originalRow];if(r<0)continue;
const a=term.c*term.e[i]%p;LU[r][j]=(LU[r][j]+a)%p;for(let s=0;s<3;s++)seedRhs[r][s]+=table[a*p+sol[s]];
}}
for(const row of seedRhs)for(let t=0;t<3;t++)row[t]%=p;
const inverseDiagonal=[];
for(let k=0;k<n;k++){
const pivot=LU[k][k];if(!pivot)throw Error("zero pivot at "+k);
const inv=dixonPow(pivot,p-2,p);inverseDiagonal.push(inv);
const ids=[],vals=[];for(let j=k+1;j<n;j++)if(LU[k][j]){ids.push(j);vals.push(LU[k][j]);}
for(let i=k+1;i<n;i++){if(!LU[i][k])continue;const factor=table[LU[i][k]*p+inv];LU[i][k]=factor;const c=factor*p,row=LU[i];for(let q=0;q<ids.length;q++){const j=ids[q];let v=row[j]-table[c+vals[q]];if(v<0)v+=p;row[j]=v;}}
if((k+1)%200===0){notify({stage:"integer LU",prime:p,pivots:k+1,n});await yield_control();}
}
const solved=dixonSolve3(LU,inverseDiagonal,seedRhs,p,table);
const verified=solved.every((row,i)=>row.every((v,t)=>v===certificate.solutionsAtPivotColumns[i][t]));
if(!verified)throw Error("three seed solves did not recover known field solutions");
const chunkRows=64,chunkCount=Math.ceil(n/chunkRows);
for(let k=0;k<chunkCount;k++){const start=k*chunkRows,count=Math.min(chunkRows,n-start),bytes=new Uint8Array(count*n);for(let j=0;j<count;j++)bytes.set(LU[start+j],j*n);store(prefix+"_chunk_"+k,dixonEncode64(bytes));}
const meta={prime:p,n,rowsTotal,chunkRows,chunkCount,inverseDiagonal,pivotColumns:certificate.pivotColumns,pivotOriginalRows:certificate.pivotOriginalRows,integerDataSha:"91416b837b7b95b67cce7cc07fca3f250b179877",seedSolutionsVerified:verified,noRowSwaps:true,scope:"LU modulo 103 of the selected integer-gradient square matrix. This is preparation for exact rational reconstruction, not the final certificate."};
store(prefix+"_metadata",meta);
return{prime:p,n,chunkCount,seedSolutionsVerified:verified,metadataKey:prefix+"_metadata"};
}
function loadDixonLU(prefix){
const meta=load(prefix+"_metadata");if(!meta)throw Error("missing LU metadata");const LU=[];
for(let k=0;k<meta.chunkCount;k++){const bytes=dixonDecode64(load(prefix+"_chunk_"+k)),count=Math.min(meta.chunkRows,meta.n-k*meta.chunkRows);if(bytes.length!==count*meta.n)throw Error("invalid chunk size");for(let j=0;j<count;j++)LU.push(bytes.slice(j*meta.n,(j+1)*meta.n));}
return{meta,LU};
}
