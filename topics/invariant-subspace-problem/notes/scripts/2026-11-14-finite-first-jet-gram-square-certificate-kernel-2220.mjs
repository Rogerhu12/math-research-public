
const ZERO=[0n,1n],ONE=[1n,1n];
function gcd(a,b){if(a<0n)a=-a;if(b<0n)b=-b;while(b){let r=a%b;a=b;b=r;}return a;}
function F(a,b=1n){a=BigInt(a);b=BigInt(b);if(!a)return ZERO;if(b<0n){a=-a;b=-b;}let g=gcd(a,b);return[a/g,b/g];}
function add(a,b){if(!a[0])return b;if(!b[0])return a;let g=gcd(a[1],b[1]),ad=a[1]/g,bd=b[1]/g;return F(a[0]*bd+b[0]*ad,ad*b[1]);}
function neg(a){return[-a[0],a[1]];}function sub(a,b){return add(a,neg(b));}
function mul(a,b){if(!a[0]||!b[0])return ZERO;let x=gcd(a[0],b[1]),y=gcd(b[0],a[1]);return[(a[0]/x)*(b[0]/y),(a[1]/y)*(b[1]/x)];}
function div(a,b){if(!b[0])throw Error("div0");return mul(a,F(b[1],b[0]));}
function ps(a,k){let z=ONE;for(let i=0;i<k;i++)z=mul(z,a);return z;}
function s(a){return a[0].toString()+"/"+a[1].toString();}
function zz(n,m){return Array.from({length:n},()=>Array(m).fill(ZERO));}
function pop(x){let c=0;while(x){c+=x&1;x>>=1;}return c;}
function fac(n){let p=1n;for(let i=2;i<=n;i++)p*=BigInt(i);return p;}
function mv(A,x){return A.map(r=>r.reduce((v,a,i)=>add(v,mul(a,x[i])),ZERO));}
function inner(x,y,w){return x.reduce((v,a,i)=>add(v,mul(mul(a,y[i]),w[i])),ZERO);}
function linear(A,b){A=A.map((r,i)=>r.concat([b[i]]));let n=A.length;
 for(let j=0;j<n;j++){let k=j;while(k<n&&!A[k][j][0])k++;if(k===n)throw Error("singular");[A[j],A[k]]=[A[k],A[j]];let pivot=A[j][j];for(let k=j;k<=n;k++)A[j][k]=div(A[j][k],pivot);
 for(let i=0;i<n;i++)if(i!==j&&A[i][j][0]){let v=A[i][j];for(let k=j;k<=n;k++)A[i][k]=sub(A[i][k],mul(v,A[j][k]));}}
 return A.map(r=>r[n]);}
function Nhead(etas){let A=[[ZERO]];for(let p=0;p<=etas.length;p++){let h=A.length,N=zz(2*h,2*h);for(let i=0;i<h;i++)for(let j=0;j<h;j++){N[i][j]=A[i][j];N[h+i][h+j]=A[i][j];}for(let i=0;i<h;i++)N[i][h+i]=F(1,(p+1)**2);for(let j=0;j<p;j++){let prod=ONE;for(let nu=j;nu<p;nu++)prod=mul(prod,etas[nu]);let mask=(1<<p)-(1<<j);for(let x=0;x<h;x++)if(!(x&mask))N[x|mask][h+x]=add(N[x|mask][h+x],mul(prod,F(1,(j+1)**2)));}A=N;}return A;}
function calc(){
 const A=Nhead([F(1,5),F(1,50)]),d=8,a=ONE,b=F(1,2),beta=F(1,10);
 const B=zz(4*d,4*d);
 for(let i=0;i<d;i++)for(let j=0;j<d;j++)for(let h=0;h<4;h++)B[4*i+h][4*j+h]=add(B[4*i+h][4*j+h],A[i][j]);
 for(let i=0;i<d;i++)for(let h=0;h<4;h++){if(h&1)B[4*i+(h^1)][4*i+h]=add(B[4*i+(h^1)][4*i+h],a);if(h&2)B[4*i+(h^2)][4*i+h]=add(B[4*i+(h^2)][4*i+h],b);}
 const labels=[];for(let p=1;p<=d;p++)for(let i=0;i<=d-p;i++)for(let h=0;h<4;h++)if(pop(h)<=p)labels.push([p,i,h]);
 const w=labels.map(([p,i,h])=>F(1,fac(p-pop(h))));
 function col(i,h){let v=Array(4*d).fill(ZERO);v[4*i+h]=ONE;const pow=[v];for(let j=1;j<=d;j++)pow.push(mv(B,pow.at(-1)));return labels.map(([p,i,st])=>mul(F((-1)**(p-pop(st))*10**(p-pop(st))),pow[p-pop(st)][4*i+st]));}
 function low(x){let out=x.slice();for(let p=2;p<=d;p++)for(let i=0;i<=d-p;i++){let g=Array(labels.length).fill(ZERO);for(let k=0;k<labels.length;k++)if(labels[k][0]===p&&labels[k][1]===i){let h=labels[k][2];g[k]=F(h===0?50*p*(p-1):h===1?-5*(p-1):h===2?-10*(p-1):1);}let c=div(inner(g,out,w),inner(g,g,w));out=out.map((x,k)=>sub(x,mul(c,g[k])));}return out;}
 const vs=[];for(let h=1;h<=2;h++)for(let i=0;i<d;i++)vs.push(col(i,h));const ws=[];for(let i=0;i<d-1;i++)ws.push(col(i,3));
 for(const x of ws)if(low(x).some(t=>t[0]))throw Error("high basis not high");
 const vlo=vs.map(low),sig=labels.map(([p,i,h])=>F(p===1&&i===5?(h===0?25:h===1?-2:-1):0));
 const M=vlo.map(x=>vlo.map(y=>inner(x,y,w))),rhs=vlo.map(x=>neg(inner(x,sig,w))),c=linear(M,rhs);
 const lift=labels.map((_,i)=>vs.reduce((t,x,j)=>add(t,mul(c[j],x[i])),ZERO)),lo=low(lift),hi=lift.map((x,i)=>sub(x,lo[i]));
 const G=ws.map(x=>ws.map(y=>inner(x,y,w))),rh=ws.map(x=>neg(inner(x,hi,w))),cc=linear(G,rh);
 const pure=hi.map((x,i)=>ws.reduce((t,y,j)=>add(t,mul(cc[j],y[i])),x));
 if(ws.some(x=>inner(x,pure,w)[0]))throw Error("pure not orthogonal");
 if(vlo.some(x=>inner(x,sig.map((v,i)=>add(v,lo[i])),w)[0]))throw Error("bare not orthogonal");
 const sig2=inner(sig,sig,w),energy=inner(pure,pure,w),ratio=div(energy,sig2),gap=sub(energy,sig2);
 return{labels:labels.length,A:A.map(row=>row.map(s)),sigma2:s(sig2),energy:s(energy),ratio:s(ratio),gapPositive:gap[0]>0n,gap:s(gap),c:c.map(s),highCorrection:cc.map(s),bareResidualNorm:s(inner(sig.map((v,i)=>add(v,lo[i])),sig.map((v,i)=>add(v,lo[i])),w))};
}

const certificate=calc();
const [numerator,denominator]=certificate.ratio.split("/").map(BigInt);
if(!(13n*denominator<numerator && numerator<14n*denominator))
  throw new Error("The claimed exact interval failed.");
certificate.exact_interval="13 < pure_energy / sigma_squared < 14";
console.log(JSON.stringify(certificate,null,2));
