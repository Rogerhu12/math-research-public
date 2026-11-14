// Author: Astra-ISP-1cf8c51d; 2026-11-13. Diagnostic only; no universal bound is asserted.
function clusterComparison(trials=300,seed0=910734){
let seed=seed0>>>0;const rnd=()=>{seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return(seed>>>0)/4294967296;};
const dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0),mv=(A,x)=>A.map(r=>dot(r,x)),tr=A=>A[0].map((_,j)=>A.map(r=>r[j])),mm=(A,B)=>{const T=tr(B);return A.map(r=>T.map(c=>dot(r,c)));},norm=x=>Math.sqrt(dot(x,x));
function inv(A){const n=A.length,X=A.map((r,i)=>r.concat(Array.from({length:n},(_,j)=>+(i===j))));let maxPivot=0,minPivot=Infinity;for(let k=0;k<n;k++){let p=k;for(let i=k+1;i<n;i++)if(Math.abs(X[i][k])>Math.abs(X[p][k]))p=i;const val=Math.abs(X[p][k]);maxPivot=Math.max(maxPivot,val);minPivot=Math.min(minPivot,val);if(val<1e-20)return null;[X[p],X[k]]=[X[k],X[p]];let v=X[k][k];for(let j=k;j<2*n;j++)X[k][j]/=v;for(let i=0;i<n;i++)if(i!==k){let t=X[i][k];for(let j=k;j<2*n;j++)X[i][j]-=t*X[k][j];}}const B=X.map(r=>r.slice(n)),check=mm(A,B);let residual=0;for(let i=0;i<n;i++)for(let j=0;j<n;j++)residual=Math.max(residual,Math.abs(check[i][j]-(i===j)));return{A:B,pivotRatio:maxPivot/minPivot,residual};}
function levels(sizes,p){let out=[];function r(a,i,left){if(i===sizes.length){if(left===0)out.push(a);return;}for(let j=0;j<=Math.min(left,sizes[i]);j++)r(a.concat(j),i+1,left-j);}r([],0,p);return out;}
let best={ratio:0},valid=0,rejected=0;
for(let trial=0;trial<trials;trial++){const nc=trial%3?3:4,s=1+trial%5,sizes=Array.from({length:nc},(_,i)=>i===0?s:(s+2+Math.floor(Math.exp(rnd()*7))));let weights=Array.from({length:nc},()=>Math.exp(-rnd()*5));weights[0]=1;const scale=Math.max(...weights.map((w,i)=>w*Math.sqrt(sizes[i])));weights=weights.map(w=>w/scale);
const lev=[-1,0,1,2].map(i=>levels(sizes,s+i)),dim=lev[1].length;
function down(a,b){const idx=new Map(a.map((x,i)=>[x.join(","),i])),D=Array.from({length:a.length},()=>Array(b.length).fill(0));for(let j=0;j<b.length;j++)for(let i=0;i<nc;i++)if(b[j][i]){const v=b[j].slice();v[i]--;D[idx.get(v.join(","))][j]+=weights[i]*Math.sqrt(b[j][i]*(sizes[i]-b[j][i]+1));}return D;}
const D0=down(lev[0],lev[1]),D1=down(lev[1],lev[2]),D2=mm(D1,down(lev[2],lev[3]));const dg=inv(mm(D0,tr(D0)));if(!dg)continue;const dt=tr(D0);
const proj=x=>{const z=mv(dt,mv(dg.A,mv(D0,x)));return x.map((v,i)=>v-z[i]);};
let basis=[];for(let j=0;j<dim;j++){let x=proj(Array.from({length:dim},(_,i)=>+(i===j)));for(let turn=0;turn<2;turn++)for(const q of basis){let t=dot(x,q);x=x.map((v,i)=>v-t*q[i]);}let nn=norm(x);if(nn>1e-7)basis.push(x.map(v=>v/nn));}
if(basis.length!==dim-lev[0].length){rejected++;continue;}const K=tr(basis),g1=inv(mm(D1,tr(D1))),g2=inv(mm(D2,tr(D2)));if(!g1||!g2||g1.residual>1e-5||g2.residual>1e-5){rejected++;continue;}
const H1=mm(basis,mm(g1.A,K)),H2=mm(basis,mm(g2.A,K)),hi=inv(H2);if(!hi||hi.residual>1e-5){rejected++;continue;}const B=mm(H1,mm(hi.A,H1));let asym=0;for(let i=0;i<B.length;i++)for(let j=0;j<B.length;j++)asym=Math.max(asym,Math.abs(B[i][j]-B[j][i]));if(asym>1e-5){rejected++;continue;}
let v=Array.from({length:B.length},()=>rnd()*2-1),vn=norm(v);v=v.map(t=>t/vn);for(let it=0;it<250;it++){let x=mv(B,v),nn=norm(x);v=x.map(t=>t/nn);}const ratio=dot(v,mv(B,v)),g=mv(K,v);valid++;if(ratio>best.ratio)best={ratio,nc,s,sizes,weights,g,primitiveResidual:norm(mv(D0,g)),inverseResiduals:[g1.residual,g2.residual,hi.residual],asym,pivotRatios:[g1.pivotRatio,g2.pivotRatio,hi.pivotRatio]};}
return{trials,valid,rejected,best};}
console.log(JSON.stringify(clusterComparison(350,910734),null,2));
