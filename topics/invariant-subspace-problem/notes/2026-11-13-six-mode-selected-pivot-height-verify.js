function verifySelectedSolutionHeight(data){
 const p=BigInt(data.prime),M=p**BigInt(data.step),W=10n**BigInt(data.weightExponent),threshold=4n*10n**BigInt(2*data.boundExponent),a=data.residues.map(BigInt),B=data.basis.map(row=>row.map(BigInt));
 function det(input){const n=input.length;if(!n)return 1n;const A=input.map(r=>[...r]);let previous=1n,sign=1n;for(let k=0;k<n-1;k++){let j=k;while(j<n&&!A[j][k])j++;if(j===n)return 0n;if(j!==k){[A[j],A[k]]=[A[k],A[j]];sign=-sign;}const z=A[k][k];for(let i=k+1;i<n;i++)for(let j=k+1;j<n;j++){const v=z*A[i][j]-A[i][k]*A[k][j];if(v%previous)throw Error("nonexact determinant");A[i][j]=v/previous;}previous=z;}return sign*A[n-1][n-1];}
 if(B.length!==4||B.some(row=>row.length!==4)||a.length!==3)throw Error("dimension");
 for(const row of B){if(row[3]%W)throw Error("weight coordinate");const d=row[3]/W;for(let j=0;j<3;j++)if((row[j]-a[j]*d)%M)throw Error("congruence lattice");}
 const d=det(B);if((d<0n?-d:d)!==M**3n*W)throw Error("lattice index");
 const G=B.map(u=>B.map(v=>u.reduce((s,x,i)=>s+x*v[i],0n)));let previous=1n;
 for(let k=1;k<=4;k++){const next=det(G.slice(0,k).map(row=>row.slice(0,k)));if(next<threshold*previous)throw Error("Gram-Schmidt height lower bound");previous=next;}
 return {all_pass:true,dimension:4,fullLatticeIndexVerified:true,allFourGramSchmidtBoundsVerified:true,
 weightedInfinityNormLowerBound:"10^"+data.boundExponent,denominatorAlternativeLowerBound:"10^"+(data.boundExponent-data.weightExponent),
 statement:"Every nonzero integer vector (n0,n1,n2,d*10^weightExponent) satisfying the recorded congruences has weighted maximum at least the stated bound."};
}
