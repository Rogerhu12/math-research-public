// Author: Astra-ISP-1cf8c51d; 2026-11-13. Diagnostic only; no universal bound is asserted.
function probeComparison(trials=200,seed0=173071){
let seed=seed0>>>0; const rnd=()=>{seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return(seed>>>0)/4294967296;};
const dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0),mv=(A,x)=>A.map(r=>dot(r,x)),tr=A=>A[0].map((_,j)=>A.map(r=>r[j])),mm=(A,B)=>{const T=tr(B);return A.map(r=>T.map(c=>dot(r,c)));},norm=x=>Math.sqrt(dot(x,x));
function inv(A){const n=A.length,X=A.map((r,i)=>r.concat(Array.from({length:n},(_,j)=>+(i===j))));let maxPivot=0,minPivot=Infinity;for(let k=0;k<n;k++){let p=k;for(let i=k+1;i<n;i++)if(Math.abs(X[i][k])>Math.abs(X[p][k]))p=i;const val=Math.abs(X[p][k]);maxPivot=Math.max(maxPivot,val);minPivot=Math.min(minPivot,val);if(val<1e-22)return null;[X[p],X[k]]=[X[k],X[p]];let v=X[k][k];for(let j=k;j<2*n;j++)X[k][j]/=v;for(let i=0;i<n;i++)if(i!==k){let t=X[i][k];for(let j=k;j<2*n;j++)X[i][j]-=t*X[k][j];}}return{A:X.map(r=>r.slice(n)),pivotRatio:maxPivot/minPivot};}
function sets(n,k){let a=[];function rec(m,i,r){if(!r){a.push(m);return;}for(let j=i;j<=n-r;j++)rec(m|1<<j,j+1,r-1);}rec(0,0,k);return a;}
let best={ratio:0},valid=0;
for(let trial=0;trial<trials;trial++){
const n=6+trial%3,s=trial%4<2?1:2,lev=[sets(n,s-1),sets(n,s),sets(n,s+1),sets(n,s+2)],dim=lev[1].length;
const weights=Array.from({length:n},()=>Math.exp(-rnd()*(1+4*(trial%3))));weights[0]=1;
const down=lev[0].map(I=>lev[1].map(J=>((I&J)===I)?weights[Math.log2(I^J)]:0));
const ig=inv(mm(down,tr(down)));if(!ig)continue;
const proj=x=>{const y=mv(ig.A,mv(down,x)),z=mv(tr(down),y);return x.map((v,i)=>v-z[i]);};
const basis=[];for(let j=0;j<dim;j++){let x=proj(Array.from({length:dim},(_,i)=>+(i===j)));for(let turn=0;turn<2;turn++)for(const q of basis){const t=dot(x,q);x=x.map((v,i)=>v-t*q[i]);}const r=norm(x);if(r>1e-8)basis.push(x.map(v=>v/r));}
if(basis.length!==dim-lev[0].length)continue;const K=tr(basis);
function gram(k){const A=Array.from({length:dim},()=>Array(dim).fill(0));for(const J of lev[k+1]){let v=[];for(let i=0;i<dim;i++){const I=lev[1][i];if((I&J)!==I)continue;let x=k===2?2:1;for(let j=0;j<n;j++)if((I^J)&1<<j)x*=weights[j];v.push([i,x]);}for(const[i,x]of v)for(const[j,y]of v)A[i][j]+=x*y;}return A;}
const g1=gram(1),g2=gram(2),a1=inv(g1),a2=inv(g2);if(!a1||!a2)continue;
const H1=mm(basis,mm(a1.A,K)),H2=mm(basis,mm(a2.A,K)),iH2=inv(H2);if(!iH2)continue;
const B=mm(H1,mm(iH2.A,H1));let v=Array.from({length:basis.length},()=>rnd()*2-1);let vn=norm(v);v=v.map(t=>t/vn);
for(let t=0;t<120;t++){let x=mv(B,v),nx=norm(x);if(!isFinite(nx)||nx===0)break;v=x.map(z=>z/nx);}
const ratio=dot(v,mv(B,v)),g=mv(K,v),res=norm(mv(down,g));
valid++;if(ratio>best.ratio)best={ratio,n,s,weights,g,primitiveResidual:res,pivotRatios:[a1.pivotRatio,a2.pivotRatio,iH2.pivotRatio]};
}return{trials,valid,seed0,best};
}
console.log(JSON.stringify(probeComparison(250,173071),null,2));
