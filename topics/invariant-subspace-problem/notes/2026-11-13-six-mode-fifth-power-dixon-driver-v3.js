function dixonSolve3Direct(LU,inverseDiagonal,rhs,p){
 const n=LU.length;if(p>65535||!Number.isSafeInteger(n*(p-1)*(p-1)+p))throw Error('unsafe exact Number dot product');const y0=new Uint16Array(n),y1=new Uint16Array(n),y2=new Uint16Array(n),x0=new Uint16Array(n),x1=new Uint16Array(n),x2=new Uint16Array(n);
 for(let i=0;i<n;i++){
  let a=rhs[i][0],b=rhs[i][1],c=rhs[i][2];const row=LU[i];
  for(let j=0;j<i;j++){const v=row[j];if(v){a-=v*y0[j];b-=v*y1[j];c-=v*y2[j];}}
  y0[i]=(a%p+p)%p;y1[i]=(b%p+p)%p;y2[i]=(c%p+p)%p;
 }
 for(let i=n-1;i>=0;i--){
  let a=y0[i],b=y1[i],c=y2[i];const row=LU[i];
  for(let j=i+1;j<n;j++){const v=row[j];if(v){a-=v*x0[j];b-=v*x1[j];c-=v*x2[j];}}
  const inv=inverseDiagonal[i];x0[i]=((a%p+p)%p)*inv%p;x1[i]=((b%p+p)%p)*inv%p;x2[i]=((c%p+p)%p)*inv%p;
 }
 return Array.from({length:n},(_,i)=>[x0[i],x1[i],x2[i]]);
}

function buildDixonSparse(integerData,meta){
 const mons=dixonMonomials(6,10),mult=dixonMonomials(6,7),index=new Map(mons.map((e,i)=>[e.join(","),i]));
 const coefficientIds=new Map(),coefficients=[],gradient=Array.from({length:6},()=>[]);
 for(let i=0;i<6;i++)for(const term of integerData.quarticIntegerTerms){if(!term.exponents[i])continue;const c=BigInt(term.coefficient)*BigInt(term.exponents[i]),key=String(c);if(!coefficientIds.has(key)){coefficientIds.set(key,coefficients.length);coefficients.push(c);}const e=[...term.exponents];e[i]--;gradient[i].push({e,cid:coefficientIds.get(key)});}
 const columns=meta.pivotColumns.map(col=>{const i=Math.floor(col/mult.length),m=mult[col%mult.length],rows=[],ids=[];for(const t of gradient[i]){rows.push(index.get(t.e.map((v,j)=>v+m[j]).join(",")));ids.push(t.cid);}return{rows:Uint16Array.from(rows),ids:Uint16Array.from(ids)};});
 const products=coefficients.map(c=>Array.from({length:meta.prime},(_,d)=>c*BigInt(d)));
 return{rows:mons.length,columns,coefficients,products};
}
function dixonIsqrt(n){if(n<0n)throw Error("negative square root");if(n<2n)return n;let x=1n<<BigInt(Math.ceil(n.toString(2).length/2));for(;;){const y=(x+n/x)>>1n;if(y>=x)return x;x=y;}}
function dixonRR(a,M,Nmax,Dmax){
 if(a===0n)return[0n,1n];let r0=M,r1=a,t0=0n,t1=1n;
 while(r1>Nmax){const q=r0/r1;[r0,r1]=[r1,r0-q*r1];[t0,t1]=[t1,t0-q*t1];if((t1<0n?-t1:t1)>Dmax)return null;if(r1===0n)return null;}
 let num=r1,den=t1;if(den<0n){num=-num;den=-den;}
 if(!den||den>Dmax||dixonGcd(num,den)!==1n||dixonGcd(den,M)!==1n||(num-a*den)%M!==0n)return null;
 return[num,den];
}
function verifyDixonRationalNumerators(sparse,numerators,denominator,rhs){
 const acc=Array.from({length:sparse.rows},()=>[0n,0n,0n]);
 for(let j=0;j<sparse.columns.length;j++){const v=numerators[j];if(!v.some(x=>x))continue;const col=sparse.columns[j];for(let k=0;k<col.rows.length;k++){const row=acc[col.rows[k]],a=sparse.coefficients[col.ids[k]];for(let t=0;t<3;t++)if(v[t])row[t]+=a*v[t];}}
 for(let i=0;i<acc.length;i++)for(let t=0;t<3;t++)if(acc[i][t]!==rhs[i][t]*denominator)return{all_pass:false,firstFailureRow:i,firstFailureComponent:t};
 return{all_pass:true,identities:3*acc.length};
}
function tryDixonRationalRecovery(X,M,sparse,rhs,rhsDigits){
 const ratios=[rhsDigits,Math.max(0,rhsDigits-32),rhsDigits+32,0],attempts=[];
 for(const exponent of [...new Set(ratios)]){
   const scale=10n**BigInt(exponent);if(M<4n*scale){attempts.push({ratioExponent:exponent,reason:"insufficient modulus"});continue;}
   const Nmax=dixonIsqrt((M/2n)*scale),Dmax=(M/2n)/Nmax;if(!Dmax)continue;
   const fractions=[];let commonDen=1n,failed=null;
   outer:for(let i=0;i<X.length;i++){const row=[];for(let t=0;t<3;t++){const q=dixonRR(X[i][t],M,Nmax,Dmax);if(!q){failed={row:i,component:t};break outer;}row.push(q);commonDen=commonDen/dixonGcd(commonDen,q[1])*q[1];if(commonDen.toString(2).length>100000){failed={row:i,component:t,reason:"denominator lcm exceeds checkpoint budget"};break outer;}}fractions.push(row);}
   if(failed){attempts.push({ratioExponent:exponent,failed});continue;}
   const numerators=fractions.map(row=>row.map(([a,b])=>a*(commonDen/b))),verified=verifyDixonRationalNumerators(sparse,numerators,commonDen,rhs);
   if(verified.all_pass)return{success:true,ratioExponent:exponent,numerators,denominator:commonDen,verified,attempts};
   attempts.push({ratioExponent:exponent,reason:"reconstructed candidates failed full exact check",firstFailureRow:verified.firstFailureRow});
 }
 return{success:false,attempts};
}
async function runDixonBatch(options){
 const prefix=options.prefix,luPrefix=options.luPrefix||"normal_dixon103_lu",problem=load(options.problemKey||"normal_dixon_integer_problem"),integerData=load(options.integerDataKey||"normal_dixon_integer_input");
 const {meta,LU}=loadDixonLU(luPrefix),P=BigInt(meta.prime),table=dixonMulTable(meta.prime),sparse=buildDixonSparse(integerData,meta),rhs=problem.rhs.map(row=>row.map(BigInt));
 const old=load(prefix+"_state");
 let step=old?.step||0,M=old?BigInt(old.modulus):1n;
 let X=old?old.solutionResidues.map(row=>row.map(BigInt)):Array.from({length:meta.n},()=>[0n,0n,0n]);
 let residual=old?old.residual.map(row=>row.map(BigInt)):rhs.map(row=>[...row]);
 const startStep=step,maximum=startStep+options.steps;
 function save(){store(prefix+"_state",{step,modulus:String(M),solutionResidues:X.map(row=>row.map(String)),residual:residual.map(row=>row.map(String)),rhsContent:problem.rhsContent,integerDataSha:problem.integerDataSha,luMetadataKey:luPrefix+"_metadata",lastFullDivisibilityCheck:true});}
 while(step<maximum){
   const reduced=meta.pivotOriginalRows.map(i=>residual[i].map(v=>Number((v%P+P)%P))),digits=dixonSolve3Direct(LU,meta.inverseDiagonal,reduced,meta.prime,table);
   const acc=Array.from({length:sparse.rows},()=>[0n,0n,0n]);
   for(let j=0;j<meta.n;j++){const v=digits[j];if(!v.some(x=>x))continue;const col=sparse.columns[j];for(let k=0;k<col.rows.length;k++){const row=acc[col.rows[k]],prod=sparse.products[col.ids[k]];if(v[0])row[0]+=prod[v[0]];if(v[1])row[1]+=prod[v[1]];if(v[2])row[2]+=prod[v[2]];}}
   for(let i=0;i<sparse.rows;i++)for(let t=0;t<3;t++){const diff=residual[i][t]-acc[i][t];if(diff%P!==0n){store(prefix+"_failure",{step:step+1,row:i,component:t,remainder:String(diff%P)});throw Error("full rectangular residual not divisible by 103 at step "+(step+1)+", row "+i);}residual[i][t]=diff/P;}
   const shift=Array.from({length:meta.prime},(_,d)=>M*BigInt(d));for(let j=0;j<meta.n;j++)for(let t=0;t<3;t++)X[j][t]+=shift[digits[j][t]];
   M*=P;step++;
   let reconstruction=null;
   if(step%(options.reconstructEvery||8)===0){
      reconstruction=tryDixonRationalRecovery(X,M,sparse,rhs,problem.maxDigitsAfterContent);
      store(prefix+"_last_reconstruction",{step,success:reconstruction.success,attempts:reconstruction.attempts});
      if(reconstruction.success){
        const exact={integerDataSha:problem.integerDataSha,rhsContent:problem.rhsContent,prime:meta.prime,liftSteps:step,modulus:String(M),commonDenominator:String(reconstruction.denominator),pivotColumns:meta.pivotColumns,numeratorsAtPivotColumns:reconstruction.numerators.map(row=>row.map(String)),zeroElsewhere:true,multiplierDegree:7,coefficientIdentities:reconstruction.verified.identities,allExactIdentitiesVerified:true,ratioExponent:reconstruction.ratioExponent,identity:"grad(R_integer) * numeratorMultipliers = (q_integer^5/rhsContent) * commonDenominator"};
        store(prefix+"_exact_certificate",exact);save();
        return{success:true,step,modulusDigits:String(M).length,commonDenominatorDigits:String(reconstruction.denominator).length,identities:reconstruction.verified.identities,certificateKey:prefix+"_exact_certificate"};
      }
   }
   if(step%(options.checkpointEvery||16)===0||step===maximum){save();let maxDigits=0;for(const row of residual)for(const a of row)maxDigits=Math.max(maxDigits,(a<0n?-a:a).toString().length);notify({stage:"Dixon lifting",step,modulusDigits:String(M).length,maxResidualDigits:maxDigits,fullDivisibilityChecked:9009,reconstructionTried:!!reconstruction,firstReconstructionFailure:reconstruction?.attempts?.[0]?.failed||null});await yield_control();}
 }
 return{success:false,startStep,step,modulusDigits:String(M).length,stateKey:prefix+"_state",scope:"Lifting checkpoint only. No rational ideal-membership certificate yet."};
}
