/* Independent exact verifier for the N=5 six-mode Jacobian certificate.
No LU, modular arithmetic, reconstruction, or solver state is used.
Inputs: integer data 91416b... and the reconstructed certificate JSON.
All operations below are exact BigInt arithmetic in Z[t]/f(t). */
function verifyN5RationalCertificate(integerData,certificate){
 const must=(condition,message)=>{if(!condition)throw Error(message);};
 const f=integerData.field.monicCubicCoefficients.map(BigInt);
 must(f.length===4&&f[3]===1n,"the cubic must be monic");
 const content=BigInt(certificate.rhsContent),den=BigInt(certificate.commonDenominator);
 must(content>0n&&den>0n,"nonzero positive scaling factors required");
 const zero=()=>[0n,0n,0n],nz=a=>a.some(x=>x!==0n);
 function mul(a,b){
  const p=[0n,0n,0n,0n,0n];
  for(let i=0;i<3;i++)for(let j=0;j<3;j++)p[i+j]+=a[i]*b[j];
  for(let d=4;d>=3;d--){const c=p[d];if(c)for(let j=0;j<3;j++)p[d-3+j]-=c*f[j];}
  return p.slice(0,3);
 }
 function monomials(degree){
  let partial=[{e:[],remaining:degree}];
  for(let coordinate=0;coordinate<5;coordinate++){
   const next=[];
   for(const item of partial)for(let x=0;x<=item.remaining;x++)next.push({e:[...item.e,x],remaining:item.remaining-x});
   partial=next;
  }
  return partial.map(item=>[...item.e,item.remaining]);
 }
 const key=e=>e.join(",");
 function add(map,e,a){const k=key(e);let item=map.get(k);if(!item){item={e:[...e],a:zero()};map.set(k,item);}for(let j=0;j<3;j++)item.a[j]+=a[j];}
 const q=new Map();
 must(integerData.quadraticExponents.length===integerData.BellQuadraticIntegerCoefficients.length,"quadratic data lengths");
 for(let i=0;i<integerData.quadraticExponents.length;i++){
  const e=integerData.quadraticExponents[i],a=integerData.BellQuadraticIntegerCoefficients[i].map(BigInt);
  must(e.length===6&&e.every(x=>Number.isInteger(x)&&x>=0)&&e.reduce((u,v)=>u+v,0)===2&&a.length===3,"quadratic entry");
  add(q,e,a);
 }
 let power=new Map([[key([0,0,0,0,0,0]),{e:[0,0,0,0,0,0],a:[1n,0n,0n]}]]);
 for(let k=0;k<5;k++){
  const next=new Map();
  for(const p of power.values())for(const b of q.values())add(next,p.e.map((x,i)=>x+b.e[i]),mul(p.a,b.a));
  for(const [key,item]of next)if(!nz(item.a))next.delete(key);
  power=next;
 }
 const multipliers=monomials(7),allRows=monomials(10);
 must(multipliers.length===792&&allRows.length===3003,"monomial dimensions");
 const gradients=Array.from({length:6},()=>[]);
 for(const term of integerData.quarticIntegerTerms){
  const e=term.exponents,c=BigInt(term.coefficient);
  must(e.length===6&&e.every(x=>Number.isInteger(x)&&x>=0)&&e.reduce((u,v)=>u+v,0)===4,"quartic entry");
  for(let i=0;i<6;i++)if(e[i]){const d=[...e];d[i]--;gradients[i].push({e:d,c:c*BigInt(e[i])});}
 }
 const columns=certificate.pivotColumns,values=certificate.numeratorsAtPivotColumns;
 must(Array.isArray(columns)&&Array.isArray(values)&&columns.length===values.length,"certificate lengths");
 must(new Set(columns).size===columns.length,"duplicate multiplier column");
 const lhs=new Map();let nonzeroMultipliers=0,maxNumeratorDigits=0;
 for(let j=0;j<columns.length;j++){
  const column=columns[j],a=values[j].map(BigInt);
  must(Number.isInteger(column)&&column>=0&&column<6*multipliers.length&&a.length===3,"multiplier entry");
  if(!nz(a))continue;
  nonzeroMultipliers++;
  for(const v of a)maxNumeratorDigits=Math.max(maxNumeratorDigits,(v<0n?-v:v).toString().length);
  const gradient=Math.floor(column/multipliers.length),e=multipliers[column%multipliers.length];
  for(const term of gradients[gradient])add(lhs,e.map((x,i)=>x+term.e[i]),a.map(x=>x*term.c));
 }
 let checked=0;const failures=[];
 for(let i=0;i<allRows.length;i++){
  const k=key(allRows[i]),l=lhs.get(k)?.a||zero(),r=power.get(k)?.a||zero();
  for(let component=0;component<3;component++){
   must(r[component]%content===0n,"the common RHS content does not divide an integer target coefficient");
   const target=(r[component]/content)*den;
   if(l[component]!==target&&failures.length<8)failures.push({row:i,exponents:allRows[i],component});
   checked++;
  }
 }
 return {all_pass:failures.length===0,exactCoefficientIdentities:checked,targetMonomials:power.size,
  nonzeroMultiplierColumns:nonzeroMultipliers,commonDenominatorDigits:den.toString().length,maxNumeratorDigits,
  rhsContent:content.toString(),failures,
  identity:"grad(R_integer) * numeratorMultipliers = commonDenominator * q_integer^5 / rhsContent",
  arithmetic:"exact BigInt in Z[t]/(the supplied monic cubic); no modular calculation"};
}
