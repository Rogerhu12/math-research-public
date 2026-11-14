/* Exact structure of the complete ordinary Bell polynomial of F^3.
   Variables y_i have weight 1; the eleven Hankel entries H_m have weight 2.
   The sixteen third moments are kept as separate quadratic/linear sectors.
   All polynomial coefficients and determinant calculations use BigInt. */
function verifySixModeCubicBellStructure(){
 const K=[
 [0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],
 [0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]
 ].map(r=>r.map(BigInt));
 const pw=Array.from({length:17},(_,i)=>7**i);
 if(pw[16]*7>=2**52)throw Error("unsafe monomial encoding");
 const zero=()=>new Map(),constant=c=>c?new Map([[0,c]]):zero(),variable=i=>new Map([[pw[i],1n]]);
 function add(A,B){const C=new Map(A);for(const[k,v]of B){const t=(C.get(k)||0n)+v;if(t)C.set(k,t);else C.delete(k);}return C;}
 function scale(A,c){if(!c)return zero();return new Map([...A].map(([k,v])=>[k,v*c]));}
 function div(A,d){return new Map([...A].map(([k,v])=>{if(v%d)throw Error("nonexact polynomial division");return[k,v/d];}));}
 function mul(A,B){const C=zero();for(const[a,u]of A)for(const[b,v]of B){const k=a+b,t=(C.get(k)||0n)+u*v;if(t)C.set(k,t);else C.delete(k);}return C;}
 function diff(A,i){const C=zero();for(const[k,v]of A){const e=Math.floor(k/pw[i])%7;if(e){const a=k-pw[i],t=(C.get(a)||0n)+BigInt(e)*v;if(t)C.set(a,t);else C.delete(a);}}return C;}
 function eq(A,B){return add(A,scale(B,-1n)).size===0;}
 const sum=xs=>xs.reduce(add,zero());
 const pc=(A,B)=>{const C=Array.from({length:A.length+B.length-1},zero);for(let i=0;i<A.length;i++)for(let j=0;j<B.length;j++)C[i+j]=add(C[i+j],mul(A[i],B[j]));return C;};
 const y=Array.from({length:6},(_,i)=>variable(i)),H=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j)=>variable(6+i+j)));
 let F=zero();for(let i=0;i<6;i++)for(let j=i;j<6;j++){const c=i===j?K[i][i]/2n:K[i][j];if(i===j&&K[i][i]%2n)throw Error("nonintegral F");F=add(F,scale(mul(y[i],y[j]),c));}
 const p=K.map(r=>sum(r.map((c,j)=>scale(y[j],c)))),F3=mul(mul(F,F),F);
 const anti=Array(11).fill(0n);for(let i=0;i<6;i++)for(let j=0;j<6;j++)anti[i+j]+=K[i][j];
 if(anti.some(Boolean))throw Error("physical-curve quadratic is nonzero");
 function L2(P){let R=zero();for(let i=0;i<6;i++)for(let j=0;j<6;j++)R=add(R,scale(mul(H[i][j],diff(diff(P,i),j)),-1n));return R;}
 function D3(P){const R=Array.from({length:16},zero);for(let i=0;i<6;i++)for(let j=0;j<6;j++)for(let k=0;k<6;k++)R[i+j+k]=add(R[i+j+k],diff(diff(diff(P,i),j),k));return R;}
 const L2one=L2(F3),L2two=L2(L2one),L2three=L2(L2two);
 const gaussianDirect=sum([F3,L2one,div(L2two,2n),div(L2three,6n)]);
 if(L2(L2three).size)throw Error("Gaussian expansion does not terminate");
 const KH=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j)=>sum(Array.from({length:6},(_,k)=>scale(H[k][j],K[i][k])))));
 const KHK=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j)=>sum(Array.from({length:6},(_,k)=>scale(KH[i][k],K[k][j])))));
 const Hp=H.map(row=>sum(row.map((h,j)=>mul(h,p[j]))));
 const b=sum(p.map((pi,i)=>mul(pi,Hp[i])));
 const c=sum(Array.from({length:6},(_,i)=>sum(Array.from({length:6},(_,j)=>scale(mul(Hp[i],Hp[j]),K[i][j])))));
 const tau2=sum(Array.from({length:6},(_,i)=>sum(Array.from({length:6},(_,j)=>mul(KH[i][j],KH[j][i])))));
 const tau3=sum(Array.from({length:6},(_,i)=>sum(Array.from({length:6},(_,j)=>sum(Array.from({length:6},(_,k)=>mul(mul(KH[i][j],KH[j][k]),KH[k][i])))))));
 const gaussianFormula=sum([F3,scale(mul(F,b),-6n),scale(mul(F,tau2),6n),scale(c,12n),scale(tau3,-8n)]);
 if(!eq(gaussianDirect,gaussianFormula))throw Error("complete Gaussian sector mismatch");
 const d=pc(pc(p,p),p),q=Array.from({length:11},zero);
 for(let i=0;i<6;i++)for(let j=0;j<6;j++)q[i+j]=add(q[i+j],KHK[i][j]);
 const e=pc(q,p),ell=d.map((v,i)=>add(v,scale(e[i],-6n))),D3F=D3(F3);
 for(let m=0;m<16;m++){
  if(!eq(D3F[m],scale(d[m],6n)))throw Error("third derivative leading identity "+m);
  const base=div(scale(D3F[m],2n),3n),actual=add(base,L2(base));
  if(L2(L2(base)).size)throw Error("third-linear sector does not terminate");
  if(!eq(actual,scale(ell[m],4n)))throw Error("complete third-linear sector mismatch "+m);
 }
 function conv(A,B){const C=Array.from({length:A.length+B.length-1},()=>Array(A[0].length+B[0].length-1).fill(0n));for(let i=0;i<A.length;i++)for(let j=0;j<A[0].length;j++)if(A[i][j])for(let k=0;k<B.length;k++)for(let l=0;l<B[0].length;l++)if(B[k][l])C[i+k][j+l]+=A[i][j]*B[k][l];return C;}
 const J2=conv(K,K),J3=conv(J2,K);
 for(let m=0;m<16;m++){const twice=D3(D3F[m]);for(let n=0;n<16;n++)if(!eq(twice[n],constant(36n*J3[m][n])))throw Error("all sixth derivative / third-Hessian entry "+m+","+n);}
 function det(M){const A=M.map(r=>r.slice());let prev=1n,sgn=1n;for(let k=0;k<A.length-1;k++){let r=k;while(r<A.length&&!A[r][k])r++;if(r===A.length)return 0n;if(r!==k){[A[r],A[k]]=[A[k],A[r]];sgn=-sgn;}const p=A[k][k];for(let i=k+1;i<A.length;i++){for(let j=k+1;j<A.length;j++){const v=p*A[i][j]-A[i][k]*A[k][j];if(v%prev)throw Error("nonexact Bareiss");A[i][j]=v/prev;}A[i][k]=0n;}prev=p;}return sgn*A.at(-1).at(-1);}
 const detJ2=det(J2),detJ3=det(J3);
 if(detJ2!==-64701092257700249600n||detJ3!==23366320238786911411830138211362846399922176000n)throw Error("determinant mismatch");
 const adj=Array.from({length:16},()=>Array(16).fill(0n));
 for(let i=0;i<16;i++)for(let j=0;j<16;j++){const minor=J3.filter((_,r)=>r!==i).map(r=>r.filter((_,c)=>c!==j));adj[j][i]=((i+j)%2?-1n:1n)*det(minor);}
 for(let i=0;i<16;i++)for(let j=0;j<16;j++){let a=0n,b=0n;for(let k=0;k<16;k++){a+=J3[i][k]*adj[k][j];b+=adj[i][k]*J3[k][j];}const expected=i===j?detJ3:0n;if(a!==expected||b!==expected)throw Error("two-sided exact adjugate");}
 return {all_pass:true,physicalCurveZero:true,gaussianSectorTerms:gaussianFormula.size,thirdLinearSectorTerms:ell.map(a=>a.size),completeThirdLinearIdentities:16,completeThirdHessianEntries:256,
 detJ2:String(detJ2),detJ3:String(detJ3),thirdHessianMultiplier:16,exactTwoSidedAdjugateEntries:512,
 data:{K:K.map(r=>r.map(String)),J3:J3.map(r=>r.map(String)),adjugateJ3:adj.map(r=>r.map(String)),detJ3:String(detJ3)},
 scope:"Complete ordinary Bell F^3 and a finite exact Schur reduction. No Jacobian membership, new cyclicity, or higher-power conclusion is asserted."};
}
