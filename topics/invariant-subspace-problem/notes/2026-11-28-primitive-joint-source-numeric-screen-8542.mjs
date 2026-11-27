#!/usr/bin/env node
// Reproducible exploratory binary64 inputs; no positivity certificate.
import {writeFileSync} from "node:fs";
const six=(function(){

function pc(x){let n=0;while(x){x&=x-1;n++;}return n;}
function masks(n,p){const a=[];for(let x=0;x<(1<<n);x++)if(pc(x)===p)a.push(x);return a;}
function deriv(b,p,k){const n=b.length,cols=masks(n,p),rows=masks(n,p-k),fac=Array.from({length:k},(_,i)=>i+1).reduce((a,c)=>a*c,1);return rows.map(j=>cols.map(i=>{if((i&j)!==j)return 0;let d=i^j,v=fac;for(let t=0;t<n;t++)if(d&(1<<t))v*=b[t];return v;}));}
function dot(a,b){let z=0;for(let i=0;i<a.length;i++)z+=a[i]*b[i];return z;}
function basis(rows,initial=[]){const q=initial.map(a=>a.slice()),fresh=[];let rem=rows.map(a=>a.slice());while(rem.length){let best=-1,bn=0,bv;for(let i=0;i<rem.length;i++){let v=rem[i].slice();for(let rep=0;rep<2;rep++)for(const r of q){const a=dot(v,r);for(let j=0;j<v.length;j++)v[j]-=a*r[j];}const nn=dot(v,v);if(nn>bn){bn=nn;best=i;bv=v;}}if(bn<1e-22)break;for(let j=0;j<bv.length;j++)bv[j]/=Math.sqrt(bn);q.push(bv);fresh.push(bv);rem.splice(best,1);}return fresh;}
function uh(b,p,h){const older=basis(deriv(b,p,h));return basis(deriv(b,p,h-1),older);}
function mul(A,x){return A.map(a=>dot(a,x));}
function adjBlock(b,p,h){const old=uh(b,p-1,h-1),cur=uh(b,p,h),D=deriv(b,p,1);return {old,cur,A:old.map(r=>cur.map(c=>dot(r,mul(D,c))))};}
function symEig(A){A=A.map(r=>r.slice());const n=A.length;for(let st=0;st<100*n*n;st++){let p=0,q=1,v=0;for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)if(Math.abs(A[i][j])>v){v=Math.abs(A[i][j]);p=i;q=j;}if(v<1e-13)break;const th=0.5*Math.atan2(2*A[p][q],A[q][q]-A[p][p]),c=Math.cos(th),s=Math.sin(th),app=A[p][p],aqq=A[q][q],apq=A[p][q];A[p][p]=c*c*app-2*s*c*apq+s*s*aqq;A[q][q]=s*s*app+2*s*c*apq+c*c*aqq;A[p][q]=A[q][p]=0;for(let k=0;k<n;k++)if(k!==p&&k!==q){let a=A[k][p],d=A[k][q];A[k][p]=A[p][k]=c*a-s*d;A[k][q]=A[q][k]=s*a+c*d;}}return A.map((r,i)=>r[i]).sort((a,b)=>a-b);}
function test(b,s,h,C){const p=s+h-1,z=adjBlock(b,p,h),w=adjBlock(b,p+1,h+1);const gram=z.cur.map((_,i)=>z.cur.map((_,j)=>z.A.reduce((a,r)=>a+r[i]*r[j],0)));const cross=z.cur.map(c=>w.cur.map(d=>dot(c,mul(deriv(b,p+1,1),d))));const N=cross.map(a=>cross.map(b=>dot(a,b)));const diff=gram.map((r,i)=>r.map((x,j)=>C*x-N[i][j]));return{n:b.length,s,h,dim:z.cur.length,min:symEig(diff)[0],denmin:symEig(gram)[0],weights:b};}
return {test,symEig};
})();
const phase=(function(){

function pc(x){let n=0;while(x){x&=x-1;n++;}return n;}
function masks(n,p){let a=[];for(let m=0;m<1<<n;m++)if(pc(m)===p)a.push(m);return a;}
function dot(a,b){return a.reduce((s,x,i)=>s+x*b[i],0);}
function tr(A){return A[0].map((_,j)=>A.map(r=>r[j]));}
function mm(A,B){let C=tr(B);return A.map(a=>C.map(c=>dot(a,c)));}
function add(A,B,k=1){return A.map((r,i)=>r.map((x,j)=>x+k*B[i][j]));}
function scale(A,k){return A.map(r=>r.map(x=>k*x));}
function eye(n){return Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>i===j?1:0));}
function orth(rows,old=[]){let q=old.map(r=>r.slice()),out=[];for(let row of rows){let v=row.slice();for(let z=0;z<2;z++)for(let u of q){let x=dot(u,v);for(let i=0;i<v.length;i++)v[i]-=x*u[i];}let n=Math.sqrt(dot(v,v));if(n>1e-10){v=v.map(x=>x/n);q.push(v);out.push(v);}}return out;}
function inv(A){let n=A.length,R=A.map((r,i)=>r.concat(eye(n)[i]));for(let j=0;j<n;j++){let k=j;for(let i=j+1;i<n;i++)if(Math.abs(R[i][j])>Math.abs(R[k][j]))k=i;let t=R[k];R[k]=R[j];R[j]=t;let a=R[j][j];if(Math.abs(a)<1e-25)throw Error("singular");R[j]=R[j].map(x=>x/a);for(let i=0;i<n;i++)if(i!==j){let a=R[i][j];for(let h=0;h<2*n;h++)R[i][h]-=a*R[j][h];}}return R.map(r=>r.slice(n));}
function sym(A){return A.map((r,i)=>r.map((x,j)=>(x+A[j][i])/2));}
function eig(A){A=sym(A);let n=A.length;for(let step=0;step<100*n*n;step++){let p=0,q=1,v=0;for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)if(Math.abs(A[i][j])>v){v=Math.abs(A[i][j]);p=i;q=j;}if(v<1e-13)break;let th=.5*Math.atan2(2*A[p][q],A[q][q]-A[p][p]),c=Math.cos(th),s=Math.sin(th),a=A[p][p],b=A[q][q],h=A[p][q];A[p][p]=c*c*a-2*s*c*h+s*s*b;A[q][q]=s*s*a+2*s*c*h+c*c*b;A[p][q]=A[q][p]=0;for(let i=0;i<n;i++)if(i!==p&&i!==q){let a=A[i][p],b=A[i][q];A[i][p]=A[p][i]=c*a-s*b;A[i][q]=A[q][i]=s*a+c*b;}}return A.map((r,i)=>r[i]).sort((a,b)=>a-b);}
function chol(A){let n=A.length,L=Array.from({length:n},()=>Array(n).fill(0));for(let i=0;i<n;i++)for(let j=0;j<=i;j++){let s=A[i][j];for(let k=0;k<j;k++)s-=L[i][k]*L[j][k];L[i][j]=i===j?Math.sqrt(s):s/L[j][j];if(!Number.isFinite(L[i][j]))throw Error("cholesky");}return L;}
function context(N){let s=N/2,mid=masks(N,s),low=masks(N,s-1),lo2=masks(N,s-2);let d=low.map(r=>mid.map(c=>(r&c)===r?1:0)),dm=lo2.map(r=>low.map(c=>(r&c)===r?1:0));let U=orth(eye(mid.length),orth(d)),V=orth(eye(low.length),orth(dm));let E=scale(mm(V,d),1/Math.sqrt(2));return {N,s,mid,low,U,V,E};}
function weighted(A,B,w){return A.map(a=>B.map(b=>a.reduce((s,x,i)=>s+x*b[i]*w[i],0)));}
function phase(z,ctx){let {N,mid,low,U,V,E}=ctx??context(z.length),prod=m=>z.reduce((s,v,i)=>s*((m>>i)&1?v:1),1),pi=z.reduce((s,v)=>s*v,1);let wm=mid.map(m=>1/prod(m)),wl=low.map(m=>1/prod(m)),wu=low.map(m=>prod(m)/pi);let h=weighted(V,V,wl),ell=weighted(V,V,wu),M=weighted(U,U,wm),C=weighted(U,E,wm),Q=weighted(E,E,wm),R=mm(mm(tr(C),inv(M)),C),S=add(Q,R,-1),J=add(scale(mm(mm(h,inv(S)),ell),2),add(Q,R),-1);let D=mm(mm(tr(J),inv(ell)),J),L=chol(h),Li=inv(L),F=mm(mm(Li,D),tr(Li));return {N,z,dim:V.length,phi:eig(F),hmin:eig(h)[0],smin:eig(S)[0]};}
return {phase,context};
})();
const s2=(function(){

function pc(x){let n=0;while(x){x&=x-1;n++;}return n;}
function masks(n,p){let a=[];for(let m=0;m<1<<n;m++)if(pc(m)===p)a.push(m);return a;}
function dot(a,b){return a.reduce((s,x,i)=>s+x*b[i],0);}
function tr(A){return A[0].map((_,j)=>A.map(r=>r[j]));}
function mm(A,B){let C=tr(B);return A.map(a=>C.map(c=>dot(a,c)));}
function add(A,B,k=1){return A.map((r,i)=>r.map((x,j)=>x+k*B[i][j]));}
function scale(A,k){return A.map(r=>r.map(x=>k*x));}
function eye(n){return Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>i===j?1:0));}
function orth(rows,old=[]){let q=old.map(r=>r.slice()),out=[];for(let row of rows){let v=row.slice();for(let z=0;z<2;z++)for(let u of q){let x=dot(u,v);for(let i=0;i<v.length;i++)v[i]-=x*u[i];}let n=Math.sqrt(dot(v,v));if(n>1e-10){v=v.map(x=>x/n);q.push(v);out.push(v);}}return out;}
function inv(A){let n=A.length,R=A.map((r,i)=>r.concat(eye(n)[i]));for(let j=0;j<n;j++){let k=j;for(let i=j+1;i<n;i++)if(Math.abs(R[i][j])>Math.abs(R[k][j]))k=i;let t=R[k];R[k]=R[j];R[j]=t;let a=R[j][j];if(Math.abs(a)<1e-25)throw Error("singular");R[j]=R[j].map(x=>x/a);for(let i=0;i<n;i++)if(i!==j){let a=R[i][j];for(let h=0;h<2*n;h++)R[i][h]-=a*R[j][h];}}return R.map(r=>r.slice(n));}
function sym(A){return A.map((r,i)=>r.map((x,j)=>(x+A[j][i])/2));}
function eig(A){A=sym(A);let n=A.length;for(let step=0;step<100*n*n;step++){let p=0,q=1,v=0;for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)if(Math.abs(A[i][j])>v){v=Math.abs(A[i][j]);p=i;q=j;}if(v<1e-13)break;let th=.5*Math.atan2(2*A[p][q],A[q][q]-A[p][p]),c=Math.cos(th),s=Math.sin(th),a=A[p][p],b=A[q][q],h=A[p][q];A[p][p]=c*c*a-2*s*c*h+s*s*b;A[q][q]=s*s*a+2*s*c*h+c*c*b;A[p][q]=A[q][p]=0;for(let i=0;i<n;i++)if(i!==p&&i!==q){let a=A[i][p],b=A[i][q];A[i][p]=A[p][i]=c*a-s*b;A[i][q]=A[q][i]=s*a+c*b;}}return A.map((r,i)=>r[i]).sort((a,b)=>a-b);}
function chol(A){let n=A.length,L=Array.from({length:n},()=>Array(n).fill(0));for(let i=0;i<n;i++)for(let j=0;j<=i;j++){let s=A[i][j];for(let k=0;k<j;k++)s-=L[i][k]*L[j][k];L[i][j]=i===j?Math.sqrt(s):s/L[j][j];if(!Number.isFinite(L[i][j]))throw Error("cholesky");}return L;}
function context(N){let s=N/2,mid=masks(N,s),low=masks(N,s-1),lo2=masks(N,s-2);let d=low.map(r=>mid.map(c=>(r&c)===r?1:0)),dm=lo2.map(r=>low.map(c=>(r&c)===r?1:0));let U=orth(eye(mid.length),orth(d)),V=orth(eye(low.length),orth(dm));let E=scale(mm(V,d),1/Math.sqrt(2));return {N,s,mid,low,U,V,E};}
function weighted(A,B,w){return A.map(a=>B.map(b=>a.reduce((s,x,i)=>s+x*b[i]*w[i],0)));}
function phase(z,ctx){let {N,mid,low,U,V,E}=ctx??context(z.length),prod=m=>z.reduce((s,v,i)=>s*((m>>i)&1?v:1),1),pi=z.reduce((s,v)=>s*v,1);let wm=mid.map(m=>1/prod(m)),wl=low.map(m=>1/prod(m)),wu=low.map(m=>prod(m)/pi);let h=weighted(V,V,wl),ell=weighted(V,V,wu),M=weighted(U,U,wm),C=weighted(U,E,wm),Q=weighted(E,E,wm),R=mm(mm(tr(C),inv(M)),C),S=add(Q,R,-1),J=add(scale(mm(mm(h,inv(S)),ell),2),add(Q,R),-1);let D=mm(mm(tr(J),inv(ell)),J),L=chol(h),Li=inv(L),F=mm(mm(Li,D),tr(Li));return {N,z,dim:V.length,phi:eig(F),hmin:eig(h)[0],smin:eig(S)[0]};}

function derivative(b,p,k=1){let cols=masks(b.length,p),rows=masks(b.length,p-k);return rows.map(r=>cols.map(c=>{if((r&c)!==r)return 0;let z=1;for(let i=0;i<b.length;i++)if(((c^r)>>i)&1)z*=b[i];return z;}));}
function primitive(b,p){let d=derivative(b,p),m=masks(b.length,p).length;return orth(eye(m),orth(d));}
function gram(b,p,j,U){let D=derivative(b,p+j,j),F=mm(D,tr(D));return mm(mm(U,inv(F)),tr(U));}
function s2(b,s){let U=primitive(b,s),V=primitive(b,s-1),G=gram(b,s,1,U),C=inv(G),L1=gram(b,s-1,1,V),L2=gram(b,s-1,2,V),L3=gram(b,s-1,3,V),D3=derivative(b.map(x=>x*x*x),s),B=mm(mm(V,D3),tr(U)),Q=mm(tr(B),L2),A=scale(add(mm(C,Q),mm(mm(Q,inv(L3)),L2)),.5),budget=add(eye(V.length),mm(mm(L1,inv(L2)),L1),-1),cost=mm(mm(tr(A),G),A),Li=inv(chol(budget)),F=mm(mm(Li,cost),tr(Li)),vals=eig(F);return {b,s,dim:V.length,budget:eig(budget),vals,trace:vals.reduce((a,c)=>a+c,0)};}
return {s2};

})();
const birth=(function(){

function pc(x){let n=0;while(x){x&=x-1;n++;}return n;}
function masks(n,p){let a=[];for(let m=0;m<1<<n;m++)if(pc(m)===p)a.push(m);return a;}
function dot(a,b){return a.reduce((s,x,i)=>s+x*b[i],0);}
function tr(A){return A[0].map((_,j)=>A.map(r=>r[j]));}
function mm(A,B){let C=tr(B);return A.map(a=>C.map(c=>dot(a,c)));}
function add(A,B,k=1){return A.map((r,i)=>r.map((x,j)=>x+k*B[i][j]));}
function scale(A,k){return A.map(r=>r.map(x=>k*x));}
function eye(n){return Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>i===j?1:0));}
function orth(rows,old=[]){let q=old.map(r=>r.slice()),out=[];for(let row of rows){let v=row.slice();for(let z=0;z<2;z++)for(let u of q){let x=dot(u,v);for(let i=0;i<v.length;i++)v[i]-=x*u[i];}let n=Math.sqrt(dot(v,v));if(n>1e-10){v=v.map(x=>x/n);q.push(v);out.push(v);}}return out;}
function inv(A){let n=A.length,R=A.map((r,i)=>r.concat(eye(n)[i]));for(let j=0;j<n;j++){let k=j;for(let i=j+1;i<n;i++)if(Math.abs(R[i][j])>Math.abs(R[k][j]))k=i;let t=R[k];R[k]=R[j];R[j]=t;let a=R[j][j];if(Math.abs(a)<1e-25)throw Error("singular");R[j]=R[j].map(x=>x/a);for(let i=0;i<n;i++)if(i!==j){let a=R[i][j];for(let h=0;h<2*n;h++)R[i][h]-=a*R[j][h];}}return R.map(r=>r.slice(n));}
function sym(A){return A.map((r,i)=>r.map((x,j)=>(x+A[j][i])/2));}
function eig(A){A=sym(A);let n=A.length;for(let step=0;step<100*n*n;step++){let p=0,q=1,v=0;for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)if(Math.abs(A[i][j])>v){v=Math.abs(A[i][j]);p=i;q=j;}if(v<1e-13)break;let th=.5*Math.atan2(2*A[p][q],A[q][q]-A[p][p]),c=Math.cos(th),s=Math.sin(th),a=A[p][p],b=A[q][q],h=A[p][q];A[p][p]=c*c*a-2*s*c*h+s*s*b;A[q][q]=s*s*a+2*s*c*h+c*c*b;A[p][q]=A[q][p]=0;for(let i=0;i<n;i++)if(i!==p&&i!==q){let a=A[i][p],b=A[i][q];A[i][p]=A[p][i]=c*a-s*b;A[i][q]=A[q][i]=s*a+c*b;}}return A.map((r,i)=>r[i]).sort((a,b)=>a-b);}
function chol(A){let n=A.length,L=Array.from({length:n},()=>Array(n).fill(0));for(let i=0;i<n;i++)for(let j=0;j<=i;j++){let s=A[i][j];for(let k=0;k<j;k++)s-=L[i][k]*L[j][k];L[i][j]=i===j?Math.sqrt(s):s/L[j][j];if(!Number.isFinite(L[i][j]))throw Error("cholesky");}return L;}
function context(N){let s=N/2,mid=masks(N,s),low=masks(N,s-1),lo2=masks(N,s-2);let d=low.map(r=>mid.map(c=>(r&c)===r?1:0)),dm=lo2.map(r=>low.map(c=>(r&c)===r?1:0));let U=orth(eye(mid.length),orth(d)),V=orth(eye(low.length),orth(dm));let E=scale(mm(V,d),1/Math.sqrt(2));return {N,s,mid,low,U,V,E};}
function weighted(A,B,w){return A.map(a=>B.map(b=>a.reduce((s,x,i)=>s+x*b[i]*w[i],0)));}
function phase(z,ctx){let {N,mid,low,U,V,E}=ctx??context(z.length),prod=m=>z.reduce((s,v,i)=>s*((m>>i)&1?v:1),1),pi=z.reduce((s,v)=>s*v,1);let wm=mid.map(m=>1/prod(m)),wl=low.map(m=>1/prod(m)),wu=low.map(m=>prod(m)/pi);let h=weighted(V,V,wl),ell=weighted(V,V,wu),M=weighted(U,U,wm),C=weighted(U,E,wm),Q=weighted(E,E,wm),R=mm(mm(tr(C),inv(M)),C),S=add(Q,R,-1),J=add(scale(mm(mm(h,inv(S)),ell),2),add(Q,R),-1);let D=mm(mm(tr(J),inv(ell)),J),L=chol(h),Li=inv(L),F=mm(mm(Li,D),tr(Li));return {N,z,dim:V.length,phi:eig(F),hmin:eig(h)[0],smin:eig(S)[0]};}

function derivative(b,p,k=1){let cols=masks(b.length,p),rows=masks(b.length,p-k);return rows.map(r=>cols.map(c=>{if((r&c)!==r)return 0;let z=1;for(let i=0;i<b.length;i++)if(((c^r)>>i)&1)z*=b[i];return z;}));}
function primitive(b,p){let d=derivative(b,p),m=masks(b.length,p).length;return orth(eye(m),orth(d));}
function gram(b,p,j,U){let D=derivative(b,p+j,j),F=mm(D,tr(D));return mm(mm(U,inv(F)),tr(U));}
function s2(b,s){let U=primitive(b,s),V=primitive(b,s-1),G=gram(b,s,1,U),C=inv(G),L1=gram(b,s-1,1,V),L2=gram(b,s-1,2,V),L3=gram(b,s-1,3,V),D3=derivative(b.map(x=>x*x*x),s),B=mm(mm(V,D3),tr(U)),Q=mm(tr(B),L2),A=scale(add(mm(C,Q),mm(mm(Q,inv(L3)),L2)),.5),budget=add(eye(V.length),mm(mm(L1,inv(L2)),L1),-1),cost=mm(mm(tr(A),G),A),Li=inv(chol(budget)),F=mm(mm(Li,cost),tr(Li)),vals=eig(F);return {b,s,dim:V.length,budget:eig(budget),vals,trace:vals.reduce((a,c)=>a+c,0)};}

function birth1(b){let n=b.length,z=b.map(x=>x*x),S=z.reduce((a,c)=>a+c,0),Z=0,W=0;for(let i=0;i<n;i++)for(let j=i+1;j<n;j++){Z+=z[i]*z[j];for(let k=j+1;k<n;k++)W+=z[i]*z[j]*z[k];}let U=orth(eye(n),orth([b])),u=b.map((x,i)=>(S-z[i])*x),v=b.map((x,i)=>(Z-S*z[i]+z[i]*z[i])*x),C2=Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>(i===j?S-2*z[i]:0)+b[i]*b[j]-u[i]*u[j]/Z)),C3=Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>(i===j?Z-2*S*z[i]+3*z[i]*z[i]:0)+(S-z[i]-z[j])*b[i]*b[j]-v[i]*v[j]/W));let P=mm(mm(U,C2),tr(U)),Q=mm(mm(U,C3),tr(U)),Pi=inv(P);return {b,max:eig(mm(mm(Pi,Q),Pi)).at(-1)};}
return {birth1};

})();

function random(seed){let x=seed>>>0;return()=>{x=(Math.imul(1664525,x)+1013904223)>>>0;return x/4294967296;};}
const out={status:"floating_exploration_only_not_a_certificate"};
let r=random(8612743);out.six_first_edge=Array.from({length:160},()=>six.test(Array.from({length:6},()=>Math.exp(-4*r())),2,2,4));
r=random(3917205);const ctx=phase.context(6);out.six_phase=Array.from({length:80},()=>phase.phase(Array.from({length:6},()=>Math.exp(2*r()-1)),ctx));
r=random(53914077);out.five_s2_random=Array.from({length:80},()=>s2.s2(Array.from({length:5},()=>Math.exp(4*r()-2)),2));
out.five_s2_targeted=[];
for(const t of [1,.3,.1,.03,.01,.003]){
  for(const b of [[1,1,t,t,t],[1,t,t,t,t],[1,1,1,t,t],[1,t,t*t,t**3,t**4]]){
    try{const q=s2.s2(b,2);out.five_s2_targeted.push({b,trace:q.trace,phi:Math.max(...q.vals),budget:Math.min(...q.budget)});}
    catch(e){out.five_s2_targeted.push({b,error:String(e)});}
  }
}
r=random(731918);out.birth_one_random=[];
for(const N of [5,8,12])for(let j=0;j<16;j++){const b=Array.from({length:N},()=>Math.exp(8*r()-4));out.birth_one_random.push(birth.birth1(b));}
out.birth_one_two_groups=[];
for(const N of [4,5,6,8,12])for(const k of [1,2,3])for(const t of [.1,.01]){
  const q=birth.birth1(Array.from({length:N},(_,i)=>i<k?1:t));
  out.birth_one_two_groups.push({N,k,t,max:q.max});
}
writeFileSync(process.argv[2]??"joint-source-numeric-replay.json",JSON.stringify(out,null,2)+"\n");
