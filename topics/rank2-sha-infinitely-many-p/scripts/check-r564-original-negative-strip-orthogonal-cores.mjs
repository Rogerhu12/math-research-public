// R564 exact original Q(delta) frame, projections and half-character data.
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


const w=(a=0,b=0)=>c(q(2*a-b,2),q(b,2)), zero=c(),one=c(1),delta=c(0,1);
const va=(a,b)=>a.map((x,i)=>ca(x,b[i])),vs=(a,b)=>a.map((x,i)=>cs(x,b[i])),vm=(a,b)=>a.map(x=>cm(x,b));
const D=[w(1),w(-1,-1),w(0,-2),w(),w(1),w(2,3)], C=vm([one,zero,c(-1),one,zero,zero],ci(delta));
const F=va(D,C),E=va(F,vm(C,c(13))),G=va(vm([w(-1),w(2),w(0,1),w(1,1),w(),w()],c(13)),vm(F,w(3,-2)));
const Y=[delta,cm(c(2),delta),w(3,1),w(2,-1),one,c(2)],W=[delta,cm(c(2),delta),w(3,1),w(2,-1),cm(c(3),delta),c(4)];
const Wp=[w(4,4),w(2,4),w(4,4),w(),w(4,2),w(4)];
const cr=[zero,zero,zero,zero,one,zero],dr=[zero,zero,zero,zero,zero,one];
const X=vs(cr,vm(D,c(q(1,14)))),Z=va(dr,vm(D,cd(w(1,3),c(14))));
const V=[w(1,1),w(0,-1),w(2),zero,w(0,-2),w(0,-2)];
const uc=vm(va(vm(cr,w(0,-1)),vm(dr,w(1,-1))),c(q(1,2)));
const gamma=w(3,1),gammabar=w(2,-1);
const identity=vs(vm(va(uc,vm(D,cd(w(2,3),c(14)))),c(14)),vm(V,gamma));
const Id=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j)=>c(i===j?1:0)));
const H=Id.map(r=>r.slice());H[4][4]=cd(w(-1,-1),c(2));H[4][5]=cd(w(-1,-2),c(2));H[5][4]=cd(w(2,1),c(2));H[5][5]=cd(w(-1,-1),c(2));
const Rc=Id.map(r=>r.slice());Rc[4][4]=c(-1);
const Sc=Id.map((r,i)=>r.map((x,j)=>ca(x,cm(w(-1,1),cm(cc(C[i]),C[j])))));
const proj=(r,v)=>vs(r,vm(v,cd(dot(r,v),dot(v,v))));
const coeff=r=>cd(dot(r,V),c(14));
const axisRows={D,E,G,Y,W,Wprime:Wp,X,Z,L:va(vm(cr,w(1,3)),dr),C};
const coeffs=Object.fromEntries(Object.entries(axisRows).map(([k,r])=>[k,cj(coeff(r))]));
function parityNonzero(z){const aw=sub(z[0],z[1]),bw=mul(q(2),z[1]);if(aw[1]!==1n||bw[1]!==1n)throw Error("nonintegral axis");return (aw[0]%2n!==0n||bw[0]%2n!==0n)?1:0;}
let Vs=V,conjugates=[];
for(let j=0;j<3;j++){const VH=mm([Vs],H)[0];conjugates.push({j,V:Vs.map(cj),VH:VH.map(cj),norm:cj(dot(Vs,Vs)),odd:Vs.reduce((s,z)=>s+parityNonzero(z),0),oddH:VH.reduce((s,z)=>s+parityNonzero(z),0)});Vs=mm([Vs],Sc)[0];}
const up=vm(va(vm(cr,w(0,1)),vm(dr,w(1,-1))),c(q(1,2))),U=vs(vm(up,c(7)),vm(D,w(-1,-1)));
const base={basis:"a+b delta",V:V.map(cj),normV:cj(dot(V,V)),orthogonalDV:cj(dot(D,V)),axisIdentityZero:identity.every(x=>ce(x,zero)),coefficients:coeffs,conjugates,U35:U.map(cj),normU:cj(dot(U,U)),twiceU:vm(U,c(2)).map(cj),UH:mm([U],H)[0].map(cj)};

const KK=[w(1,1),w(0,-1),w(2),zero,w(-3,3),w(3)];
const zp=proj(Z,V);
const zidentity=vs(vm(zp,c(14)),KK);
let Ks=KK,Kconjugates=[];
for(let j=0;j<3;j++){const KH=mm([Ks],H)[0];Kconjugates.push({j,K:Ks.map(cj),KH:KH.map(cj),norm:cj(dot(Ks,Ks)),odd:Ks.reduce((a,z)=>a+parityNonzero(z),0),oddH:KH.reduce((a,z)=>a+parityNonzero(z),0)});Ks=mm([Ks],Sc)[0];}
const gram= [D,V,KK].map(a=>[D,V,KK].map(b=>cj(dot(a,b))));
const coreData={D:{degree:14,g_mod_28:[15,0],anchor:"Theta(gamma z)",anchor_norm:7},V:{degree:14,g_mod_28:[15,0],anchor:"Theta(gamma z)",anchor_norm:7},K:{degree:42,g_mod_84:[43,0],anchor:"Theta(delta gamma z)",anchor_norm:21}};
return {...base,K42:KK.map(cj),gramDVK:gram,ZprojectedEqualsKover14:zidentity.every(x=>ce(x,zero)),Kconjugates,coreData};

}
console.log(JSON.stringify(certificate(),null,2));
