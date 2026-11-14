"use strict";
// Exact computations in F_103[s]/(F), not tests at sampled source points.
// Integer products in this small field are below 2^53 and are exact in JS.
function verifyRankOneZeroASection(){
 const p=103,norm=x=>(x%p+p)%p;
 const ipow=(a,n)=>{let r=1;for(;n;n>>=1,a=a*a%p)if(n&1)r=r*a%p;return r;};
 const Kbase=[[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],
  [0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]].map(r=>r.map(norm));
 function coefficientPower(K,d){
  let A=[[1]];
  for(let z=0;z<d;z++){
   const B=Array.from({length:A.length+5},()=>Array(A.length+5).fill(0));
   for(let i=0;i<A.length;i++)for(let j=0;j<A.length;j++)
    for(let k=0;k<6;k++)for(let l=0;l<6;l++)
     B[i+k][j+l]=norm(B[i+k][j+l]+A[i][j]*K[k][l]);
   A=B;
  }return A;
 }
 function inverseMatrix(A){
  const n=A.length,R=A.map((row,i)=>row.concat(Array.from({length:n},(_,j)=>+(i===j))));
  let determinant=1;
  for(let c=0;c<n;c++){
   let k=c;while(k<n&&!R[k][c])k++;if(k===n)throw Error("singular original J3");
   if(k!==c){[R[k],R[c]]=[R[c],R[k]];determinant=norm(-determinant);}
   determinant=determinant*R[c][c]%p;const iv=ipow(R[c][c],p-2);
   R[c]=R[c].map(x=>x*iv%p);
   for(let i=0;i<n;i++)if(i!==c){const f=R[i][c];if(f)R[i]=R[i].map((x,j)=>norm(x-f*R[c][j]));}
  }return {inverse:R.map(r=>r.slice(n)),determinant};
 }
 const cases=[
  {name:"Pplus",F:[-8,32,-25,5],delta:[16,18,94],dinv:[74,11,90],
   eta:[102,5,96],einv:[25,36,52],rows:[0,1,2,3],cols:[0,1,2,3]},
  {name:"Pminus",F:[864,864,135,5],delta:[68,78,100],dinv:[61,6,82],
   eta:[53,9,19],einv:[89,53,51],rows:[0,1,2,3],cols:[0,1,2,3]},
  {name:"E8",F:[9600,-25472,-3392,15936,-2888,-936,153,50,5],
   delta:[22,46,91,50,44,25,27,59],dinv:[100,81,40,77,24,86,31,54],
   eta:[14,54,41,37,41,14,5,69],einv:[86,43,55,9,4,83,102,48],
   rows:[0,1,2,3],cols:[0,1,2,3]},
  {name:"zero",F:[0,1],delta:[94],dinv:[80],eta:[84],einv:[65],rows:[0,6,5],cols:[0,1,2]},
  {name:"two",F:[-2,1],delta:[99],dinv:[77],eta:[15],einv:[55],rows:[0,1,2],cols:[0,1,2]},
  {name:"minus_six",F:[6,1],delta:[102],dinv:[102],eta:[63],einv:[18],rows:[0,1,2],cols:[0,1,2]},
  {name:"infinity",F:[0,1],reverse:true,delta:[80],dinv:[94],eta:[75],einv:[11],rows:[0,6,5],cols:[0,1,2]}
 ];
 const records=[];
 for(const cs of cases){
  const trim=a=>{while(a.length&&a.at(-1)===0)a.pop();return a;};
  const ad=(a,b)=>trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>norm((a[i]||0)+(b[i]||0))));
  const sc=(a,c)=>trim(a.map(x=>norm(x*c)));
  const mu=(a,b)=>{if(!a.length||!b.length)return[];const c=Array(a.length+b.length-1).fill(0);
   for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]=norm(c[i+j]+a[i]*b[j]);return trim(c);};
  const dm=(aa,b)=>{const a=aa.slice(),q=Array(Math.max(0,a.length-b.length+1)).fill(0),iv=ipow(b.at(-1),p-2);
   while(a.length>=b.length&&a.length){const k=a.length-b.length,c=a.at(-1)*iv%p;q[k]=c;
    for(let j=0;j<b.length;j++)a[k+j]=norm(a[k+j]-c*b[j]);trim(a);}return[trim(q),a];};
  if(!norm(cs.F.at(-1)))throw Error("source degree loss");
  const F=trim(cs.F.map(norm)),red=a=>dm(a,F)[1],add=(a,b)=>red(ad(a,b)),mul=(a,b)=>red(mu(a,b));
  const invert=a=>{let r0=F,r1=red(a),t0=[],t1=[1];
   while(r1.length){const[q,r]=dm(r0,r1);[r0,r1]=[r1,r];[t0,t1]=[t1,ad(t0,sc(mu(q,t1),-1))];}
   if(r0.length!==1)throw Error("nonunit in quotient ring: "+cs.name);
   return red(sc(t0,ipow(r0[0],p-2)));};
  const eq=(a,b,label)=>{if(add(a,sc(b,-1)).length)throw Error(cs.name+": "+label);};
  const pow=(a,n)=>{let z=[1];while(n--)z=mul(z,a);return z;};
  const mm=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((z,v,k)=>add(z,mul(v,B[k][j])),[])));
  const tp=A=>A[0].map((_,i)=>A.map(r=>r[i]));
  function det(A){
   const R=A.map(row=>row.map(x=>x.slice()));let out=[1];
   for(let c=0;c<R.length;c++){
    let k=c,iv;for(;k<R.length;k++){try{iv=invert(R[k][c]);break;}catch(e){}}
    if(k===R.length)throw Error("no unit determinant pivot");
    if(k!==c){[R[k],R[c]]=[R[c],R[k]];out=sc(out,-1);}
    out=mul(out,R[c][c]);
    for(let i=c+1;i<R.length;i++){const f=mul(R[i][c],iv);
     for(let j=c;j<R.length;j++)R[i][j]=add(R[i][j],sc(mul(f,R[c][j]),-1));}
   }return out;
  }
  const K=cs.reverse?Kbase.map(r=>r.slice().reverse()).reverse():Kbase,
   J2=coefficientPower(K,2),J3=coefficientPower(K,3),ji=inverseMatrix(J3);
  if(ji.determinant!==75)throw Error("original J3 determinant reduction");
  const pv=K.map(row=>red(row)),B=Array.from({length:16},(_,i)=>
   Array.from({length:11},(_,j)=>i-j>=0&&i-j<=5?pv[i-j]:[]));
  const A=mm(mm(mm(tp(B),ji.inverse.map(r=>r.map(x=>[x]))),B),J2.map(r=>r.map(x=>[x])));
  const bin=(n,k)=>{let x=1;for(let j=1;j<=k;j++)x=x*(n-j+1)/j;return x;};
  const T=Array.from({length:11},(_,i)=>Array.from({length:11},(_,j)=>
   j>i?[]:sc(pow([0,1],i-j),bin(i,j))));
  const AT=mm(A,T),R=AT.slice(0,8).map(row=>row.slice(2,10)),
   delta=det(R);
  eq(delta,cs.delta,"cofactor delta");eq(mul(delta,cs.dinv),[1],"delta inverse certificate");
  const aug=R.map((row,i)=>row.concat([sc(AT[i][10],-1)]));
  for(let c=0;c<8;c++){
   let k=c,iv;for(;k<8;k++){try{iv=invert(aug[k][c]);break;}catch(e){}}
   if(k===8)throw Error("kernel solve");[aug[k],aug[c]]=[aug[c],aug[k]];
   aug[c]=aug[c].map(x=>mul(x,iv));
   for(let i=0;i<8;i++)if(i!==c){const f=aug[i][c];
    aug[i]=aug[i].map((x,j)=>add(x,sc(mul(f,aug[c][j]),-1)));}
  }
  const v=[[],[],...aug.map(row=>row[8]),[1]];
  AT.forEach((row,i)=>eq(row.reduce((z,x,j)=>add(z,mul(x,v[j])),[]),[],"full kernel row "+i));
  const seq=mm(T,v.map(x=>[x])).map(row=>row[0]);
  const hm=seq=>Array.from({length:6},(_,i)=>Array.from({length:6},(_,j)=>seq[i+j]));
  const M=hm(seq),M0=hm(T.map(row=>row[0])),M1=hm(T.map(row=>row[1])),Ks=K.map(r=>r.map(x=>[x]));
  const npoly=(H,G)=>{const Q=mm(mm(mm(mm(Ks,H),Ks),G),Ks),out=Array.from({length:11},()=>[]);
   for(let i=0;i<6;i++)for(let j=0;j<6;j++)out[i+j]=add(out[i+j],Q[i][j]);return out;};
  const n00=npoly(M,M),n01=npoly(M0,M),n10=npoly(M,M0),
   n02=npoly(M1,M),n20=npoly(M,M1),n22=npoly(M1,M1);
  const columns=[n00,n00.map((_,i)=>add(n01[i],n10[i])),
   n00.map((_,i)=>add(n02[i],n20[i])),n22];
  if(cs.cols.length===3)n22.forEach(x=>eq(x,[],"zero tangent-square column"));
  const rho=det(cs.rows.map(i=>cs.cols.map(j=>columns[j][i]))),
   eta=mul(pow(delta,4),rho);
  eq(eta,cs.eta,"original cofactor Gaussian minor");
  eq(mul(eta,cs.einv),[1],"Gaussian minor inverse certificate");
  records.push({source:cs.name,sourcePolynomial:cs.F,delta:cs.delta,deltaInverse:cs.dinv,
   gaussianMinor:cs.eta,gaussianMinorInverse:cs.einv,rows:cs.rows,columns:cs.cols,
   fullKernelResidualRows:11,status:"PASS"});
 }
 return {status:"PASS",arithmetic:"exact polynomial arithmetic over F_103, with bounded integer operations",
  originalJ3DeterminantModulo103:75,families:records,
  meaning:"Polynomial unit certificates; no enumeration of finite-field source points.",
  lift:"After clearing powers of det J3, source leading coefficients remain nonzero modulo 103; Gauss lemma gives characteristic-zero coprimality.",
  execution:"Executed in code mode; no terminal or Python run is claimed."};
}
if(typeof module!=="undefined")module.exports={verifyRankOneZeroASection};
if(typeof require!=="undefined"&&require.main===module)
 console.log(JSON.stringify(verifyRankOneZeroASection(),null,2));
