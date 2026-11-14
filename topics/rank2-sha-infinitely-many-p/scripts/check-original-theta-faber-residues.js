#!/usr/bin/env node
"use strict";

// R208. Two independent exact series constructions of the original two rows.
// The only calibration prime is the already used p=43; this is not a prime scan.
function runRank2FaberResidueCalibration() {
  const p=43n, r=11, max=2*r, size=2*r+17;
  function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;}
  function Q(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}if(!n)return {n:0n,d:1n};const g=gcd(n,d);return {n:n/g,d:d/g};}
  const zero=Q(0),one=Q(1);
  const add=(a,b)=>Q(a.n*b.d+b.n*a.d,a.d*b.d),neg=a=>({n:-a.n,d:a.d});
  const sub=(a,b)=>add(a,neg(b)),mul=(a,b)=>Q(a.n*b.n,a.d*b.d);
  const div=(a,b)=>{if(!b.n)throw Error("divide by zero");return Q(a.n*b.d,a.d*b.n);};
  function ser(v=[]){let a=Array(size).fill(zero);v.forEach((x,i)=>{if(i<size)a[i]=typeof x==="object"?x:Q(x);});return a;}
  const sa=(a,b)=>a.map((x,i)=>add(x,b[i])),sc=(a,c)=>a.map(x=>mul(x,c));
  function sm(a,b){const c=ser();for(let i=0;i<size;i++)if(a[i].n)for(let j=0;i+j<size;j++)if(b[j].n)c[i+j]=add(c[i+j],mul(a[i],b[j]));return c;}
  function si(a){const b=ser();b[0]=div(one,a[0]);for(let n=1;n<size;n++){let s=zero;for(let j=1;j<=n;j++)s=add(s,mul(a[j],b[n-j]));b[n]=neg(div(s,a[0]));}return b;}
  function sp(a,n){if(n<0)return sp(si(a),-n);let b=ser([1]);while(n){if(n%2)b=sm(b,a);n=Math.floor(n/2);if(n)a=sm(a,a);}return b;}
  function compose(a,b){let c=ser();for(let j=size-1;j>=0;j--){c=sm(c,b);c[0]=add(c[0],a[j]);}return c;}
  function exp(a){if(a[0].n)throw Error("nonzero exponential constant");let b=ser([1]);for(let n=1;n<size;n++){let s=zero;for(let j=1;j<=n;j++)s=add(s,mul(Q(j),mul(a[j],b[n-j])));b[n]=div(s,Q(n));}return b;}
  function truncate(a,n){return a.map((x,i)=>i<=n?x:zero);}
  function vpZ(a){if(!a)return 1000000;a=a<0n?-a:a;let n=0;while(a%p===0n){a/=p;n++;}return n;}
  const vp=a=>a.n?vpZ(a.n)-vpZ(a.d):1000000;
  function mod(a,m){a%=m;return a<0n?a+m:a;}
  function inv(a,m){a=mod(a,m);let u=1n,v=0n,b=m;while(b){let q=a/b;[a,b]=[b,a-q*b];[u,v]=[v,u-q*v];}if(a!==1n)throw Error("nonunit");return mod(u,m);}
  const red=(a,m)=>mod(a.n*inv(a.d,m),m);
  const same=(a,b)=>a.n===b.n&&a.d===b.d;
  const s=ser([0,1]),F=ser([1]),L=ser();
  let bin=1n,d=Q(17,3);
  for(let n=1;n<size;n++){
    bin=bin*BigInt(2*n)*BigInt(2*n-1)/(BigInt(n)*BigInt(n));
    F[n]=Q(bin,4n**BigInt(n)*BigInt(4*n+1));
    L[n]=div(d,Q(n));d=mul(d,Q(4*n+1,4*n+3));
  }
  const W=sm(s,sp(F,4));
  // Coefficientwise reversion by fixed-point iteration, independent of Faber.
  let S=s;
  for(let i=0;i<max;i++)S=truncate(sm(s,sp(compose(F,S),-4)),max);
  const check=compose(W,S);
  if(!check.slice(0,max+1).every((x,i)=>same(x,s[i])))throw Error("reversion");
  const h1=ser([1,4,70,4,1]),h2=ser([1,20,-26,20,1]);
  const q8=ser([1,0,364,-1088,1190,-1088,364,0,1]);
  const J=sc(sm(sm(s,ser([1,-2,5])),ser([5,-2,1])),Q(1,5));
  const P=sm(sm(sm(sm(J,sp(ser([1,-1]),2)),ser([1,1])),h1),h2);
  const B=sm(sm(sm(J,ser([1,-1])),sp(ser([1,1]),2)),q8);
  const Lw=compose(L,S),c=Lw[r],gaugew=Lw.slice();gaugew[r]=zero;
  const Ew=exp(gaugew);
  const direct=[P,B].map(f=>sm(Ew,compose(f,S)));
  // Same original gauge transported before exponentiation in the s coordinate.
  const gs=truncate(sa(L,sc(sp(W,r),neg(c))),max-1);
  const G=truncate(exp(gs),max-1);
  if(G.some(a=>vp(a)<0))throw Error("nonintegral transported theta");
  const outputs=[];
  for(const n of [r,2*r]){
    const coeff=sp(F,-4*n).slice(0,n+1);
    if(coeff.some(a=>vp(a)<0))throw Error("nonintegral Faber");
    const pair=[];
    for(let col=0;col<2;col++){
      const f=sm(G,[P,B][col]);
      const eta=new Map();
      for(let k=1;k<size;k++)if(f[k].n)for(let j=0;j<n;j++){
        const exponent=n-j-1-k;
        const term=mul(Q(-(n-j),4*n),mul(coeff[j],f[k]));
        eta.set(exponent,add(eta.get(exponent)||zero,term));
      }
      const residue=eta.get(-1)||zero, row=mul(Q(-4),residue);
      if(!same(row,direct[col][n]))throw Error("original row / Faber mismatch");
      let minimum=1000000,terms=0;
      for(const [j,a]of eta){
        if(j===-1||!a.n)continue;
        const primitive=div(a,Q(j+1));minimum=Math.min(minimum,vp(primitive));terms++;
        if(!same(mul(primitive,Q(j+1)),a))throw Error("primitive derivative");
      }
      if(minimum<0)throw Error("nonintegral global primitive");
      // Cartier on the P1 Laurent differential has only exponent -1 left.
      for(const [j,a]of eta)if(a.n&&mod(BigInt(j+1),p)===0n&&j!==-1)
        throw Error("unexpected Cartier survivor");
      pair.push({source:col===0?"A2":"B",row_mod_p:Number(red(row,p)),row_mod_p_squared:Number(red(row,p*p)),
        primitive_min_valuation:minimum,primitive_terms:terms,cartier_coefficient_dlog_x_mod_p:Number(red(div(neg(row),Q(2)),p)),
        all_exact_rational_identities:true});
    }
    outputs.push({n,weight:4*n,rows:pair});
  }
  return {p:Number(p),r,theta_degree:max-1,original_polynomial_degrees:[16,16],
    maximum_s_degree:2*r+15,maximum_laurent_pole_order:2*r+15,
    only_excluded_Laurent_integration_exponent:-1,gauge_coefficient_valuation:vp(c),
    two_weights:outputs,
    scope:"Exact original theta gauge and Faber / integral Laurent decomposition. No assertion of simultaneous complete central vanishing or infinite-prime nonvanishing."};
}
if(typeof module!=="undefined"&&require.main===module)
  console.log(JSON.stringify(runRank2FaberResidueCalibration(),null,2));

