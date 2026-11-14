#!/usr/bin/env node
// Reproduce with: node check-r619-second-pole-block-and-newton-return.mjs
function sourceX(pp,N){
 const p=BigInt(pp);const vp=n=>{let v=0;while(n&&n%p===0n){v++;n/=p;}return v};
 const denV=Array(N+1).fill(0);let total=0;for(let n=2;n<=N;n++){denV[n]=vp(BigInt((6*n+1)*(n-1)));total+=denV[n]}
 const K=N+total+24,pows=[1n];for(let j=1;j<=K;j++)pows[j]=pows[j-1]*p;
 const mod=(x,M)=>(x%M+M)%M;
 function inv(x,M){let a=M,b=mod(x,M),u=0n,v=1n;while(b){let q=a/b;[a,b]=[b,a-q*b];[u,v]=[v,u-q*v];}if(a!==1n)throw Error("nonunit");return mod(u,M)}
 const B=Array(N+1).fill(0n),E=Array(N+1).fill(K);B[0]=p;B[1]=mod(-p*inv(7n,pows[K]),pows[K]);
 for(let n=2;n<=N;n++){let M=pows[E[n-1]],sum=0n;for(let j=1;j<n;j++)sum=(sum+B[j]*B[n-j])%M;const cost=1+denV[n],cut=pows[cost];if(sum%cut)throw Error("bad integrality at "+n);E[n]=E[n-1]-cost;const outM=pows[E[n]],unit=BigInt((6*n+1)*(n-1))/pows[denV[n]];B[n]=sum/cut*inv(unit,outM)%outM;}
 return{p,pp,N,K,B,E,minPrecision:Math.min(...E)};
}

function runCertificate(){
 const mod=(x,M)=>(x%M+M)%M;
 const vp=(x,p)=>{if(!x)return Infinity;let v=0;while(x%p===0n){v++;x/=p;}return v};
 const inv=(x,M)=>{let a=M,b=mod(x,M),u=0n,v=1n;while(b){let q=a/b;[a,b]=[b,a-q*b];[u,v]=[v,u-q*v];}if(a!==1n)throw Error("nonunit inverse");return mod(u,M)};
 const choose=(n,k)=>{let r=1n;for(let j=1;j<=k;j++)r=r*BigInt(n-k+j)/BigInt(j);return r};
 let count=0;
 const check=(ok,label)=>{count++;if(!ok)throw Error(label)};
 const output=[];
 for(const pp of [17,23]){
  const p=BigInt(pp),s=(pp+1)/6,L=(pp*pp-1)/6,N=2*L-1;
  const raw=sourceX(pp,N),B=raw.B;
  const fact=[1n],vfact=[0];
  for(let n=1;n<=N+2*pp;n++){fact[n]=fact[n-1]*BigInt(n);vfact[n]=vp(fact[n],p)}
  const R=vfact[N]+4,P=p**BigInt(R);
  check(raw.minPrecision>R+2,"source precision");
  const bin=Array.from({length:N+1},()=>[]);
  bin[0]=[1n];
  for(let n=1;n<=N;n++){bin[n]=Array(n+1).fill(1n);for(let j=1;j<n;j++)bin[n][j]=(bin[n-1][j-1]+bin[n-1][j])%P}
  const product=(u,v)=>{let r=Array(N+1).fill(0n);for(let n=0;n<=N;n++){let q=0n;for(let j=0;j<=n;j++)q+=bin[n][j]*u[j]*v[n-j];r[n]=mod(q,P)}return r};
  const exponential=(f)=>{let r=Array(N+1).fill(0n);r[0]=1n;for(let n=1;n<=N;n++){let q=0n;for(let j=1;j<=n;j++)q+=bin[n-1][j-1]*f[j]*r[n-j];r[n]=mod(q,P)}return r};
  const coef=(u,n,scale,label)=>{
   const v=vfact[n],div=v-scale;
   let q=u[n];
   if(div>0){const cut=p**BigInt(div);check(q%cut===0n,label+" pole bound "+n);q/=cut}
   else q*=p**BigInt(-div);
   return mod(q*inv(fact[n]/p**BigInt(v),p),p);
  };
  for(let n=0;n<=N;n++){
   const num=(n%2?-1n:1n)*choose(2*n,n),den=4n**BigInt(n)*BigInt(6*n+1);
   const value=vp(num,p)-vp(den,p);
   check(n===L?value===-1:value>=0,"H unique pole "+pp+":"+n);
   if(n===L){
    const rn=mod(num/p**BigInt(vp(num,p)),p),rd=mod(den/p**BigInt(vp(den,p)),p);
    check(mod(rn*inv(rd,p),p)===p-1n,"H residue");
   }
  }
  for(const bb of (pp===17?[1]:[1,17])){
   const b=BigInt(bb),bp=[1n];for(let n=1;n<=N;n++)bp[n]=bp[n-1]*b%P;
   const bL=mod(bp[L],p);
   const Xlow=[];
   for(let n=0;n<L;n++){check(B[n]%p===0n,"X integral "+n);Xlow[n]=mod((B[n]/p)*bp[n],p)}
   const cp=mod(choose(3*s-1,2*s-1)*bp[s],p),pc=mod(-Xlow[s]*inv(BigInt(pp+1),p),p);
   check(Xlow[s]===cp,"Cartier initial row");
   const sparse=[];
   for(let a=1;s+a*pp<L;a++){const n=s+a*pp;check(Xlow[n]===0n,"Cartier sparse "+n);sparse.push(n)}
   for(let r=0;r<L;r++){
    const xres=mod(B[L+r]*bp[L+r],p);
    check(xres===mod(bL*BigInt(6*r-2)*Xlow[r],p),"X whole band "+r);
    const yres=mod(BigInt(1-3*(L+r))*xres,p);
    const yr=mod(BigInt(1-3*r)*Xlow[r],p);
    check(yres===mod(bL*BigInt(6*r-3)*yr,p),"Y whole band "+r);
   }
   for(let n=1;n<=N;n++){
    let residue=0n;
    if(n!==s){
     const den=BigInt(6*n)*BigInt(6*n-1),v=vp(den,p),num=-p*B[n]*bp[n];
     check(num%(p**BigInt(v))===0n,"F denominator "+n);
     residue=mod(num/(p**BigInt(v))*inv(den/p**BigInt(v),p),p);
    }
    check(residue===(n===pp*s?mod(bL*pc,p):0n),"unique F double pole "+n);
   }
   const Ah=Array(N+1).fill(0n),Yh=Array(N+1).fill(0n),Lh=Array(N+1).fill(0n);
   for(let n=0;n<=N;n++){
    const rawA=fact[n]*B[n];check(rawA%p===0n,"A Hurwitz");
    Ah[n]=mod(rawA/p*bp[n],P);Yh[n]=mod(BigInt(1-3*n)*Ah[n],P);
    if(n&&n!==s){
     const den=BigInt(6*n-1),v=vp(den,p),cut=p**BigInt(v+1),num=-fact[n-1]*B[n];
     check(num%cut===0n,"F Hurwitz "+n);
     Lh[n]=mod(num/cut*inv(den/p**BigInt(v),P)*bp[n],P);
    }
   }
   const E=exponential(Lh),F4=product(Ah,E),F1=product(Yh,F4);
   const one=Array(N+1).fill(0n);one[0]=1n;
   const Apow=[one];for(let i=1;i<=33;i++)Apow[i]=product(Apow[i-1],Ah);
   const mulPoly=(a,b)=>{let z=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)z[i+j]+=a[i]*b[j];return z};
   const PS=mulPoly(mulPoly([1n,1n],[1n,-8n]),[7n,-4n,16n]);
   let PT=mulPoly(PS,[1n,4n]);PT=mulPoly(PT,[1n,-96n,48n,64n]);PT=mulPoly(PT,[1n,20n,-8n]);
   const native=(m,top,pol)=>{
    const Um=exponential(Lh.map(x=>mod(x*BigInt(m)*inv(6n,P),P)));
    const rational=Array(N+1).fill(0n);
    for(let n=0;n<=N;n++)for(let j=0;j<pol.length&&j<=n;j++){
     const falling=fact[n]/fact[n-j],term=falling*pol[j]*bp[j]*Apow[top-3*j][n-j];
     rational[n]=mod(rational[n]+term*inv(7n,P),P);
    }
    return product(Um,rational);
   };
   const GS=native(34,14,PS),GT=native(72,33,PT);
   const sources=[["sigma6",6,E],["f4",6,F4],["f1",6,F1],["S34",34,GS],["T72",72,GT]];
   const details=[];
   for(const [name,m,G] of sources){
    const gamma=mod(BigInt(m)*pc,p);
    for(let n=0;n<L;n++)coef(G,n,0,name+" low");
    const residues=[];
    for(let n=0;n<=N;n++){
     const actual=coef(G,n,2,name+" double");
     const expected=n<pp*s?0n:mod(gamma*bL*coef(G,n-pp*s,0,name+" rhs"),p);
     check(actual===expected,name+" full second block "+n);
     if(n>=pp*s)residues.push(Number(actual));
    }
    details.push({name,m,gamma:Number(gamma),second_block:residues});
   }
   const central=[];
   for(const [name,m,G] of [["S34",34,GS],["T72",72,GT]]){
    const gamma=mod(BigInt(m)*pc,p),g1=coef(G,s-1,0,name+" central g1");
    const first=coef(G,pp*s-1,1,name+" pth first residue");
    check(first===mod(bL*g1,p),name+" pth endpoint");
    const rows=[];
    for(let h=1;h<=pp-2;h++){
     const low=coef(G,h*s-1,0,name+" central low");
     const high=coef(G,(pp+h)*s-1,2,name+" central high");
     check(high===mod(gamma*bL*low,p),name+" central second "+h);
     const factratio=fact[pp+h-1]/p;
     check(mod(factratio,p)===mod(-fact[h-1],p),"Wilson factorial "+h);
     if(gamma){
      const left=mod((h%2?-1n:1n)*factratio*high*inv(gamma**BigInt(pp+h),p),p);
      const right=mod((h%2?1n:-1n)*fact[h-1]*low*bL*inv(gamma**BigInt(pp+h-1),p),p);
      check(left===right,name+" Newton leading "+h);
     }
     rows.push({h,low:Number(low),double_residue:Number(high),physical_index:(pp+h)*s-1});
    }
    central.push({name,m,gamma:Number(gamma),g1:Number(g1),pth_residue:Number(first),rows,
      newton_division_checked:gamma!==0n});
   }
   output.push({p:pp,b:bb,s,L,last_index:N,minimum_source_precision:raw.minPrecision,
     hurwitz_modulus_exponent:R,cp:Number(cp),pc:Number(pc),sparse_rows:sparse,
     ps_log_double_residue:Number(mod(bL*pc,p)),sources:details,central});
  }
 }
 return{result:"R619",status:"passed",checks:count,
  method:"Original Weierstrass recurrence with explicit p-adic precision, then complete Hurwitz exponential and original S/T polynomials. No band theorem is used to fill coefficients.",
  scope:"Existing p=17,23 fibres; p>71 general Newton tail is proved in the text. The p=17 S34 charge is zero, so its gamma division is not asserted.",
  fibres:output};
}

console.log(JSON.stringify(runCertificate(),null,2));
