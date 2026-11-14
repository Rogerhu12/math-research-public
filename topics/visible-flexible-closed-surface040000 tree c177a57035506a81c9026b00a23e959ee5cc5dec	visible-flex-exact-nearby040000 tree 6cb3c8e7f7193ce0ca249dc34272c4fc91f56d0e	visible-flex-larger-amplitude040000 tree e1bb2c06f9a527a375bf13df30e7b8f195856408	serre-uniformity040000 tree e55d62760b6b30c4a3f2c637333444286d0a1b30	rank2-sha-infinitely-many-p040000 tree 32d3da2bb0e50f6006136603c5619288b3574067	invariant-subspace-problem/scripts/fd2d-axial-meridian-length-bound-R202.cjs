"use strict";
/* R202: exact rational necessary domain test for a planar D2 axial meridian.
 * The exact certificate uses no floating square root or Math.PI.
 */
function createR202AxialLengthBound(){
 function need(c,m){if(!c)throw Error(m);}
 function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
 function R(a,b=1n){a=BigInt(a);b=BigInt(b);need(b!==0n,"Zero denominator");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return[a/g,b/g];}
 function input(x,name){need(Array.isArray(x)&&x.length===2,name+" requires an explicit [integer numerator, integer denominator]");return R(x[0],x[1]);}
 const add=(a,b)=>R(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
 const neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b));
 const mul=(a,b)=>R(a[0]*b[0],a[1]*b[1]);
 const div=(a,b)=>{need(b[0]!==0n,"Division by zero");return R(a[0]*b[1],a[1]*b[0]);};
 const sq=a=>mul(a,a),cmp=(a,b)=>{const v=a[0]*b[1]-b[0]*a[1];return v<0n?-1:v>0n?1:0;};
 const out=a=>a.map(String),zero=R(0),one=R(1),two=R(2),four=R(4);
 function atanBounds(q,N){
   need(Number.isInteger(q)&&q>1&&Number.isInteger(N)&&N>0,"Alternating-series parameters");
   let sum=zero,p=BigInt(q),q2=BigInt(q)*BigInt(q);
   for(let k=0;k<N;k++){const t=R(k%2?-1:1,BigInt(2*k+1)*p);sum=add(sum,t);p*=q2;}
   const next=R(N%2?-1:1,BigInt(2*N+1)*p),edge=add(sum,next);
   return cmp(sum,edge)<0?[sum,edge]:[edge,sum];
 }
 function piBounds(N=16){
   const a=atanBounds(5,N),b=atanBounds(239,N);
   return [sub(mul(R(16),a[0]),mul(four,b[1])),sub(mul(R(16),a[1]),mul(four,b[0]))];
 }
 function diagnoseDomain(p){
   const A=input(p.centralMajorAxisLower,"centralMajorAxisLower"),ac=input(p.cutRadius,"cutRadius"),
     c=input(p.centralCylinderLength,"centralCylinderLength"),S=input(p.materialEndUpper,"materialEndUpper"),
     Z=input(p.cutHeightLower,"cutHeightLower"),C=input(p.principalCurvatureUpper,"principalCurvatureUpper"),
     eps=input(p.relativeMetricErrorUpper,"relativeMetricErrorUpper");
   need(cmp(C,zero)>0&&cmp(eps,zero)>=0&&cmp(S,c)>0,"Positive curvature cap, nonnegative tolerance, and nonempty interval required");
   const r=div(one,C),dx=sub(A,ac),dz=sub(Z,c);
   need(cmp(dx,r)>=0&&cmp(dz,r)>=0,"This theorem is only used when both axial displacements are at least 1/C");
   const pi=piBounds(16),u=div(mul(r,pi[0]),two),v=add(sq(sub(dx,r)),sq(sub(dz,r))),
     lengthUpperSquared=mul(sq(sub(S,c)),add(one,eps)),
     M=sub(sub(lengthUpperSquared,sq(u)),v),disc=sub(mul(mul(four,sq(u)),v),sq(M));
   const rejected=cmp(M,zero)<0||(cmp(M,zero)>=0&&cmp(disc,zero)>0);
   return {schema:"R202-exact-rational-axial-domain-test-v1",
     input:p,conditionalDomainExcluded:rejected,currentSavedSurfaceExcluded:false,
     scope:"Only a D2 planar fixed-axis meridian with the stated endpoint positions/tangents, principal curvature cap, and full axial metric upper bound.",
     exact:{radius:out(r),horizontalDisplacementLower:out(dx),verticalDisplacementLower:out(dz),
       piLower:out(pi[0]),piUpper:out(pi[1]),arcLengthTermLower:out(u),straightLengthTermSquaredLower:out(v),
       materialLengthSquaredUpper:out(lengthUpperSquared),M:out(M),discriminant:out(disc)},
     test:cmp(M,zero)<0?"M<0":rejected?"M>=0 and 4*u^2*v-M^2>0":"No exclusion by this lower bound",
     allRationalArithmetic:true,usesFloatingSquareRoot:false,usesMathPiForCertificate:false,
     passingThisNecessaryTestDoesNotProveExistence:true};
 }
 function finiteScreen(p){
   for(const k of ["A","ac","c","S","Z","C","eps"])need(Number.isFinite(p[k]),"Finite screen input "+k);
   need(p.C>0&&p.eps>=0,"Positive finite C and nonnegative eps");
   const r=1/p.C,dx=p.A-p.ac,dz=p.Z-p.c,L=(p.S-p.c)*Math.sqrt(1+p.eps);
   need(dx>=r&&dz>=r,"Outside stated displacement domain");
   const bound=r*Math.PI/2+Math.hypot(dx-r,dz-r),q=L-r*Math.PI/2;
   return {input:p,radius:r,availableLengthUpper:L,necessaryLengthLower:bound,excess:bound-L,
     maximumHeightByThisNecessaryBound:q>=dx-r?p.c+r+Math.sqrt(q*q-(dx-r)*(dx-r)):null,
     isFloatingDiagnostic:true,isCertificate:false};
 }
 return {diagnoseDomain,finiteScreen,piBounds:N=>piBounds(N).map(out),compareRationals:(a,b)=>cmp(input(a,"a"),input(b,"b"))};
}
if(typeof module!=="undefined"&&module.exports)module.exports={createR202AxialLengthBound};
