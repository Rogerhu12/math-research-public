/* R384. Exact rational source computation; no prime sampling. */
function verifyR384(){

function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
class Q{constructor(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denom");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);this.a=a/g;this.b=b/g;}add(x){return new Q(this.a*x.b+x.a*this.b,this.b*x.b);}neg(){return new Q(-this.a,this.b);}sub(x){return this.add(x.neg());}mul(x){return new Q(this.a*x.a,this.b*x.b);}inv(){return new Q(this.b,this.a);}div(x){return this.mul(x.inv());}eq(x){return this.a===x.a&&this.b===x.b;}zero(){return !this.a;}str(){return this.b===1n?String(this.a):this.a+"/"+this.b;}}
const q=x=>new Q(x),zq=q(0),oq=q(1);

const NN=10;
const f=(a,b=1)=>new Q(a,b);
const sa=(a,b)=>Array.from({length:NN+1},(_,i)=>(a[i]||zq).add(b[i]||zq));
const ss=(a,c)=>Array.from({length:NN+1},(_,i)=>(a[i]||zq).mul(c));
const sm=(a,b)=>{const r=Array.from({length:NN+1},()=>zq);for(let i=0;i<=NN;i++)for(let j=0;i+j<=NN;j++)r[i+j]=r[i+j].add((a[i]||zq).mul(b[j]||zq));return r;};
const sp=(a,n)=>{let r=[oq];while(n){if(n%2)r=sm(r,a);n=Math.floor(n/2);a=sm(a,a);}return r;};
const sh=(a,k)=>Array.from({length:NN+1},(_,i)=>i<k?zq:(a[i-k]||zq));
const se=a=>{const r=Array.from({length:NN+1},()=>zq);r[0]=oq;for(let n=1;n<=NN;n++){let v=zq;for(let j=1;j<=n;j++)v=v.add(f(j).mul(a[j]||zq).mul(r[n-j]));r[n]=v.div(f(n));}return r;};
const X=Array.from({length:NN+1},()=>zq),L=X.slice();X[0]=oq;X[1]=f(-1,7);
for(let n=2;n<=NN;n++){let v=zq;for(let j=1;j<n;j++)v=v.add(X[j].mul(X[n-j]));X[n]=v.div(f((6*n+1)*(n-1)));}
for(let n=1;n<=NN;n++)L[n]=X[n].neg().div(f(6*n*(6*n-1)));
const B16=se(ss(L,f(16))),B18=se(ss(L,f(18)));
const DS=sm(B16,sa(sh(sp(X,5),1),sh(sp(X,2),2)));
const CS=sm(B18,sa(sa(sp(X,9),ss(sh(sp(X,6),1),f(-60,7))),sa(ss(sh(sp(X,3),2),f(48,7)),ss(sh([oq],3),f(-128,7)))));
function bi(n,k){if(k<0||k>n)return 0n;let r=1n;for(let j=1;j<=k;j++)r=r*BigInt(n-j+1)/BigInt(j);return r;}
function cross(i,j,l){let v=0n;for(let r=Math.max(0,6*l-6*j);r<=Math.min(6*i,6*l);r++)v+=bi(6*i,r)*bi(6*j,6*l-r)*(9n**BigInt(r))*((-8n)**BigInt(6*l-r));return v;}
const JJ=Array.from({length:6},(_,k)=>Array.from({length:6},(_,l)=>{let v=zq;for(let i=0;i<=k+l;i++)v=v.add(DS[i].mul(CS[k+l-i]).mul(f(cross(i,k+l-i,l))));return v;}));
function determinantQ(A){A=A.map(r=>r.slice());let det=oq;for(let j=0;j<A.length;j++){let i=j;while(i<A.length&&A[i][j].zero())i++;if(i===A.length)return zq;if(i!==j){[A[i],A[j]]=[A[j],A[i]];det=det.neg();}const pivot=A[j][j];det=det.mul(pivot);for(let k=j+1;k<A.length;k++){const c=A[k][j].div(pivot);for(let l=j+1;l<A.length;l++)A[k][l]=A[k][l].sub(c.mul(A[j][l]));A[k][j]=zq;}}return det;}


function solveMatrix(A,B){A=A.map(r=>r.slice());B=B.map(r=>r.slice());for(let j=0;j<A.length;j++){let i=j;while(i<A.length&&A[i][j].zero())i++;if(i===A.length)throw Error("singular");if(i!==j){[A[i],A[j]]=[A[j],A[i]];[B[i],B[j]]=[B[j],B[i]];}const c=A[j][j].inv();A[j]=A[j].map(x=>x.mul(c));B[j]=B[j].map(x=>x.mul(c));for(let r=0;r<A.length;r++)if(r!==j){const d=A[r][j];for(let k=0;k<A.length;k++)A[r][k]=A[r][k].sub(d.mul(A[j][k]));for(let k=0;k<B[r].length;k++)B[r][k]=B[r][k].sub(d.mul(B[j][k]));}}return B;}
const B34=se(ss(L,f(34)));
const BB=Array.from({length:6},()=>Array.from({length:6},()=>zq));
for(let j=0;j<6;j++){const v=sh(sm(B34,sp(X,2+3*j)),5-j);for(let k=0;k<6;k++)BB[k][j]=v[k];}
const GG=solveMatrix(BB,JJ);
const target=[f(-128,7),f(-80,7),f(-12,7),f(-53,7),oq,zq];
if(!determinantQ(BB).eq(f(-1)))throw Error("basis determinant");
if(!GG.every((r,i)=>r[0].eq(target[i])))throw Error("original target");
if(!determinantQ(GG).eq(determinantQ(JJ).neg()))throw Error("coefficient determinant");
const expected="-23318923282365151738616026730130526028494926226150500448150665439776887285725607516802822313558989210799570944/117649";
if(determinantQ(JJ).str()!==expected)throw Error("joint determinant");
return {checks:4,D:DS.map(x=>x.str()),C:CS.map(x=>x.str()),joint_matrix:JJ.map(r=>r.map(x=>x.str())),basis_matrix:BB.map(r=>r.map(x=>x.str())),coefficient_matrix:GG.map(r=>r.map(x=>x.str())),joint_determinant:determinantQ(JJ).str(),target:target.map(x=>x.str()),leading_evaluation_determinant:determinantQ(GG).str()};

}
const certificate=verifyR384();
console.log(JSON.stringify(certificate,null,2));
