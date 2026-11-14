// Exact Q(delta) frame and moment constants for R560; delta^2=-3.
function certificate(){
const abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b){[a,b]=[b,a%b]}return a}
function q(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b}const g=gcd(a,b);return[a/g,b/g]}
const add=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>[-a[0],a[1]], sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>q(a[0]*b[0],a[1]*b[1]), div=(a,b)=>q(a[0]*b[1],a[1]*b[0]);
function pow(a,n){let r=q(1);for(;n;n>>=1,a=mul(a,a))if(n&1)r=mul(r,a);return r}
const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1], qs=a=>a[1]===1n?String(a[0]):a[0]+"/"+a[1];
const c=(a=0,b=0)=>[Array.isArray(a)?a:q(a),Array.isArray(b)?b:q(b)];
const ca=(a,b)=>[add(a[0],b[0]),add(a[1],b[1])], cn=a=>[neg(a[0]),neg(a[1])], cs=(a,b)=>ca(a,cn(b));
const cm=(a,b)=>[sub(mul(a[0],b[0]),mul(q(3),mul(a[1],b[1]))),add(mul(a[0],b[1]),mul(a[1],b[0]))];
const cc=a=>[a[0],neg(a[1])], norm=a=>add(mul(a[0],a[0]),mul(q(3),mul(a[1],a[1])));
const ci=a=>[div(a[0],norm(a)),neg(div(a[1],norm(a)))], cd=(a,b)=>cm(a,ci(b));
const ce=(a,b)=>eq(a[0],b[0])&&eq(a[1],b[1]), cj=a=>({real:qs(a[0]),delta:qs(a[1])});
function cp(a,n){let r=c(1);for(;n;n>>=1,a=cm(a,a))if(n&1)r=cm(r,a);return r}
function dot(a,b){return a.map((x,i)=>cm(x,cc(b[i]))).reduce(ca,c())}
function mm(A,B){return A.map(row=>B[0].map((_,j)=>row.map((x,k)=>cm(x,B[k][j])).reduce(ca,c())))}


const w=(a=0,b=0)=>c(q(2*a-b,2),q(b,2)), one=c(1), zero=c(), delta=c(0,1);
const va=(a,b)=>a.map((x,i)=>ca(x,b[i])), vs=(a,b)=>a.map((x,i)=>cs(x,b[i])), vm=(a,b)=>a.map(x=>cm(x,b));
const dv=[w(1),w(-1,-1),w(0,-2),w(),w(1),w(2,3)];
const cv=vm([one,zero,c(-1),one,zero,zero],ci(delta));
const fv=va(dv,cv),ev=va(fv,vm(cv,c(13)));
const h1=[w(-1),w(2),w(0,1),w(1,1),w(),w()];
const gv=va(vm(h1,c(13)),vm(fv,w(3,-2)));
const yv=[delta,cm(c(2),delta),w(3,1),w(2,-1),one,c(2)];
const wv=[delta,cm(c(2),delta),w(3,1),w(2,-1),cm(c(3),delta),c(4)];
const wp=[w(4,4),w(2,4),w(4,4),w(),w(4,2),w(4)];
const cx=[zero,zero,zero,zero,one,zero],dz=[zero,zero,zero,zero,zero,one];
const xx=vs(cx,vm(dv,c(q(1,14)))),zz=va(dz,vm(dv,cd(w(1,3),c(14))));
const u=vm(va(vm(cx,w(0,1)),vm(dz,w(1,-1))),c(q(1,2)));
const uc=vm(va(vm(cx,w(0,-1)),vm(dz,w(1,-1))),c(q(1,2)));
const l=va(vm(cx,w(1,3)),dz),lc=va(vm(cx,w(-1,-3)),dz);
const project=r=>vs(r,vm(dv,divToC(dot(r,dv),c(14))));
function divToC(a,b){return cd(a,b)}
const fr=[dv,ev,yv,wv,wp,gv];
function inv(A){let t=A.map((r,i)=>r.concat(r.map((_,j)=>c(i===j?1:0))));for(let j=0;j<A.length;j++){let k=j;while(k<A.length&&ce(t[k][j],zero))k++;if(k===A.length)throw Error("singular");[t[j],t[k]]=[t[k],t[j]];const pivot=t[j][j];t[j]=t[j].map(x=>cd(x,pivot));for(let i=0;i<A.length;i++)if(i!==j){const v=t[i][j];t[i]=t[i].map((x,k)=>cs(x,cm(v,t[j][k])));}}return t.map(r=>r.slice(A.length));}
const fi=inv(fr);
const outrow=r=>mm([r],fi)[0].map(cj);
const checks={normD:cj(dot(dv,dv)),orthogonal:[ev,yv,wv,wp,gv,xx,zz].map(x=>cj(dot(x,dv))),uCoefficient:cj(cd(dot(u,dv),c(14))),ucCoefficient:cj(cd(dot(uc,dv),c(14))),lcCoefficient:cj(cd(dot(lc,dv),c(14))),uNorm:cj(dot(project(u),project(u))),ucNorm:cj(dot(project(uc),project(uc)))};
return {basis:["D","E","Y","W","Wprime","G"],X:outrow(xx),Z:outrow(zz),checks,degree14_sixth_correction:-672};

}
console.log(JSON.stringify(certificate(),null,2));
