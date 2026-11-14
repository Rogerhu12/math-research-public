"use strict";
// Exact coefficient verification; no floating-point sampling.
// The six physical coordinates are checked in both projective charts.
function runRankOneCenteredReductionVerification() {
  const names=["a","s",...Array.from({length:11},(_,i)=>"m"+i),
    ...Array.from({length:16},(_,i)=>"l"+i)];
  const Z=()=>new Map(), C=x=>x?new Map([[0n,BigInt(x)]]):Z();
  const X=i=>new Map([[1n<<(6n*BigInt(i)),1n]]);
  const add=(...ps)=>{const r=Z();for(const p of ps)for(const[k,v]of p){
    const t=(r.get(k)||0n)+v;if(t)r.set(k,t);else r.delete(k);}return r;};
  const sc=(p,c)=>{c=BigInt(c);const r=Z();if(c)for(const[k,v]of p)r.set(k,v*c);return r;};
  const mul=(p,q)=>{const r=Z();for(const[k,v]of p)for(const[l,w]of q){
    const j=k+l,t=(r.get(j)||0n)+v*w;if(t)r.set(j,t);else r.delete(j);}return r;};
  const pow=(p,n)=>{let r=C(1);while(n--)r=mul(r,p);return r;};
  let checks=0;
  const eq=(p,q,label)=>{checks++;if(add(p,sc(q,-1)).size)throw Error(label);};
  const mat=(f)=>Array.from({length:6},(_,i)=>Array.from({length:6},(_,j)=>f(i,j)));
  const mm=(A,B)=>mat((i,j)=>add(...Array.from({length:6},(_,k)=>mul(A[i][k],B[k][j]))));
  const mv=(A,b)=>Array.from({length:6},(_,i)=>add(...b.map((v,j)=>mul(A[i][j],v))));
  const dot=(a,b)=>add(...a.map((v,i)=>mul(v,b[i])));
  const tr=A=>add(...A.map((r,i)=>r[i]));
  const outer=(a,b)=>mat((i,j)=>mul(a[i],b[j]));
  const K0=[[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],
    [0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]];
  const K=K0.map(row=>row.map(C));
  const receipts=[];
  for (const reverse of [false,true]) {
    const start=checks;
    const y=Array.from({length:6},(_,i)=>mul(X(0),pow(X(1),reverse?5-i:i)));
    const p=mv(K,y), M=mat((i,j)=>X(2+i+j));
    const L=(i,j,k)=>X(13+i+j+k);
    eq(dot(y,p),Z(),"physical mean is isotropic");
    const yy=outer(y,y), H2=mat((i,j)=>add(sc(M[i][j],2),yy[i][j]));
    const V2=(i,j,k)=>add(sc(L(i,j,k),3),mul(yy[i][j],y[k]));
    const T=(i,j,k)=>add(mul(yy[i][j],y[k]),
      sc(add(mul(y[i],H2[j][k]),mul(y[j],H2[i][k]),mul(y[k],H2[i][j])),-1),
      sc(V2(i,j,k),2));
    for(let i=0;i<6;i++)for(let j=i;j<6;j++)for(let k=j;k<6;k++)
      eq(T(i,j,k),add(sc(L(i,j,k),6),sc(add(mul(y[i],M[j][k]),
        mul(y[j],M[i][k]),mul(y[k],M[i][j])),-2)),"third tensor "+i+j+k);
    const MKM=mm(mm(M,K),M), H2KH2=mm(mm(H2,K),H2);
    const N=mat((i,j)=>add(...p.map((v,k)=>mul(T(i,j,k),v)),H2KH2[i][j]));
    for(let i=0;i<6;i++)for(let j=i;j<6;j++)
      eq(N[i][j],add(sc(MKM[i][j],4),sc(add(...p.map((v,k)=>mul(L(i,j,k),v))),6)),
        "second-gradient matrix "+i+j);
    const KH2=mm(K,H2), KM=mm(K,M), KMK=mm(KM,K), KH2K=mm(KH2,K);
    const tauH2=tr(mm(KH2,KH2)), tauM2=tr(mm(KM,KM));
    const pH2p=dot(p,mv(H2,p)), H2KH2p=mv(H2KH2,p), MKMp=mv(MKM,p);
    const contract=(tensor,A,i)=>add(...Array.from({length:6},(_,j)=>
      add(...Array.from({length:6},(_,k)=>mul(tensor(i,j,k),A[j][k])))));
    const pp=outer(p,p);
    for(let i=0;i<6;i++){
      const gamma2=add(mul(add(sc(pH2p,-2),tauH2),y[i]),
        sc(H2KH2p[i],4),sc(contract(V2,pp,i),4),sc(contract(V2,KH2K,i),-4));
      const expected=add(sc(mul(tauM2,y[i]),4),sc(MKMp[i],16),
        sc(contract(L,KMK,i),-24));
      eq(gamma2,expected,"full mean gradient "+i);
    }
    const cM=dot(p,MKMp), tauH2_3=tr(mm(mm(KH2,KH2),KH2)),
      tauM3=tr(mm(mm(KM,KM),KM));
    eq(add(sc(cM,12),sc(tauH2_3,-1)),sc(tauM3,-8),"complete low Schur part");
    receipts.push({chart:reverse?"(s^5,s^4,s^3,s^2,s,1)":"(1,s,s^2,s^3,s^4,s^5)",
      coefficient_identities:checks-start,status:"PASS"});
  }
  return {status:"PASS",arithmetic:"exact sparse multivariate BigInt polynomials",
    variables:names.length,identities:checks,charts:receipts,
    execution:"Executed in code mode; no terminal or Python run is claimed."};
}
if(typeof module!=="undefined")module.exports={runRankOneCenteredReductionVerification};
if(typeof require!=="undefined"&&require.main===module)
  console.log(JSON.stringify(runRankOneCenteredReductionVerification(),null,2));
