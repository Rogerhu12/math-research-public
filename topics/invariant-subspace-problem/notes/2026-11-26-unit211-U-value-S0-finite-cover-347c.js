// Exact BigInt proof of the S=0 rank-drop finite parameter cover.
function trim(p){p=p.slice();while(p.length&&p[p.length-1]===0n)p.pop();return p;}
function pa(a,b){let c=Array(Math.max(a.length,b.length)).fill(0n);for(let i=0;i<c.length;i++)c[i]=(a[i]||0n)+(b[i]||0n);return trim(c);}
function pn(a){return a.map(x=>-x);}
function ps(a,b){return pa(a,pn(b));}
function pm(a,b){let c=Array(Math.max(0,a.length+b.length-1)).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=a[i]*b[j];return trim(c);}
function pc(a,k){return trim(a.map(x=>x*BigInt(k)));}
function pp(a,n){let c=[1n];while(n){if(n&1)c=pm(c,a);a=pm(a,a);n>>=1;}return c;}
function ztrim(a){a=a.slice();while(a.length&&!a[a.length-1].length)a.pop();return a;}
function za(a,b){let c=[];for(let i=0;i<Math.max(a.length,b.length);i++)c.push(pa(a[i]||[],b[i]||[]));return ztrim(c);}
function zn(a){return a.map(pn);}
function zs(a,b){return za(a,zn(b));}
function zm(a,b){let c=Array.from({length:Math.max(0,a.length+b.length-1)},()=>[]);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]=pa(c[i+j],pm(a[i],b[j]));return ztrim(c);}
function zc(a,k){return ztrim(a.map(x=>pc(x,k)));}
function det(a){let n=a.length;if(!n)return [1n];if(n===1)return a[0][0];let c=[];for(let j=0;j<n;j++){if(!a[0][j].length)continue;let b=a.slice(1).map(row=>row.filter((_,k)=>k!==j));let t=pm(a[0][j],det(b));c=pa(c,j%2?pn(t):t);}return trim(c);}
function resultant(a,b){let n=a.length-1,m=b.length-1;const mat=[];for(let i=0;i<m;i++){let row=Array.from({length:n+m},()=>[]);for(let j=0;j<=n;j++)row[i+j]=a[n-j];mat.push(row);}for(let i=0;i<n;i++){let row=Array.from({length:n+m},()=>[]);for(let j=0;j<=m;j++)row[i+j]=b[m-j];mat.push(row);}return det(mat);}
function igcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let c=a%b;a=b;b=c;}return a;}
function primitive(p){p=trim(p);if(!p.length)return p;let g=p.reduce((a,b)=>igcd(a,b),0n);if(p.at(-1)<0n)g=-g;return p.map(x=>x/g);}
function divexact(a,b){a=trim(a);b=trim(b);if(!b.length)throw Error("zero div");if(!a.length)return [];if(a.length<b.length)return null;let q=Array(a.length-b.length+1).fill(0n);while(a.length>=b.length){let sh=a.length-b.length,al=a.at(-1),bl=b.at(-1);if(al%bl!==0n)return null;let cc=al/bl;q[sh]+=cc;for(let j=0;j<b.length;j++)a[sh+j]-=cc*b[j];a=trim(a);}return a.length?null:trim(q);}

function prem(a,b){a=trim(a);b=trim(b);while(a.length>=b.length&&a.length){let sh=a.length-b.length,al=a.at(-1),bl=b.at(-1);a=pc(a,bl);for(let j=0;j<b.length;j++)a[sh+j]-=al*b[j];a=primitive(a);}return a;}
function pgcd(a,b){a=primitive(a);b=primitive(b);while(b.length){let r=prem(a,b);a=b;b=r;}return primitive(a);}
function evrat(p,n,d){let r=0n;for(let j=p.length-1;j>=0;j--)r=r*n+p[j]*d**BigInt(p.length-1-j);return r;}


const assert=(v,m)=>{if(!v)throw Error(m||"exact check failed");};
const eq=(a,b)=>JSON.stringify(a.map(String))===JSON.stringify(b.map(String));
const a=[0n,1n],o=[1n],z=[[],o];
const A=[1n,-2n,2n],C=[-2n,5n,-4n],s=[-3n,2n],R=[3n,-4n],j=[-1n,2n];
const Dl=[pm(s,C),pn(A)];
const I=za(za(zc(zm([pm(ps(pc(a,4),o),C)],Dl),2),zm(z,zs([pc(pm(pm(C,ps(o,a)),R),2)],zc(zm([[2n,-7n,4n]],Dl),2)))),zm(zm(z,z),[pa(pc(pm(a,C),-2),pm(pm(s,j),R))]));
const H=za(za(zm(Dl,zs(zs(zm(z,za([[0n,4n,-4n]],zc(zm([a],z),2))),zc(zm([j],Dl),4)),[pc(pm(s,C),2)])),zc(zm(zm(z,z),[pm(ps(a,o),C)]),-2)),za(zc(zm(z,[pm(C,C)]),2),za(zc(zm(zm(z,z),zm(z,[pm(j,R)])),-2),zc(zm(zm(z,z),zm([j],Dl)),4))));
const M=[-693n,5810n,-17150n,21020n,-8496n,-1344n,1280n];
const expected=pm(pm(pm(pp(j,3),[-1n,4n]),s),pm(pm(pp(C,4),[-1n,0n,2n]),M));
const res=primitive(resultant(I,H));
assert(eq(res,primitive(expected)),"QQ Sylvester identity");
const special=[];
for(const [n,d,want]of [[1n,4n,[0n,1n]],[3n,2n,[0n,1n]],[1n,2n,[-1n,1n]]]){
 const max=Math.max(...I.concat(H).map(p=>p.length-1));
 const ip=I.map(c=>evrat(c,n,d)*d**BigInt(max-(c.length-1)));
 const hp=H.map(c=>evrat(c,n,d)*d**BigInt(max-(c.length-1)));
 const gg=pgcd(ip,hp);assert(eq(gg,want),"rational lambda fiber");
 special.push({lambda:n.toString()+"/"+d.toString(),zGcd:gg.map(String)});
}
assert(eq(pgcd(C,I[2]),[1n]),"C=0 has only forbidden z=0");
function zprem(aa,bb){aa=ztrim(aa);bb=ztrim(bb);while(aa.length>=bb.length&&aa.length){const sh=aa.length-bb.length,al=aa.at(-1),bl=bb.at(-1);aa=aa.map(x=>pm(x,bl));for(let i=0;i<bb.length;i++)aa[sh+i]=ps(aa[sh+i],pm(al,bb[i]));aa=ztrim(aa);}return aa;}
const pr=zprem(H,I),ct=pr.reduce((x,y)=>pgcd(x,y),[]);
const [r0,r1]=pr.map(p=>divexact(p,ct));
assert(eq(pgcd(M,r1),[1n]),"z graph denominator");
assert(eq(pgcd(M,r0),[1n]),"z nonzero");
assert(eq(pgcd(M,I[2]),[1n]),"quadratic degree preserved");
const lminusone=ps(pa(pm(pm(s,C),pp(r1,2)),pm(pm(A,r0),r1)),pp(r0,2));
assert(eq(pgcd(M,lminusone),[1n]),"l is not one; original q equation is never identically zero");
assert(eq(pgcd(M,pa(pm(pp(s,2),r1),pc(r0,4))),[1n]),"distinct values");
assert(eq(pgcd(M,pa(pm(pp(A,2),r0),pm(ps(pm(pm(A,C),s),pp(C,2)),r1))),[1n]),"two weights nonzero");
assert(eq(pgcd(M,M.slice(1).map((c,i)=>c*BigInt(i+1))),[1n]),"sextic squarefree");
// Exact QQ(sqrt(2)) arithmetic verifies the other algebraic lambda fiber.
function qn(aa,bb,dd){if(dd<0n){aa=-aa;bb=-bb;dd=-dd;}const g=igcd(igcd(aa,bb),dd);assert(g!==0n);return [aa/g,bb/g,dd/g];}
const qzero=[0n,0n,1n],lambda=[0n,1n,2n];
function qa(x,y){return qn(x[0]*y[2]+y[0]*x[2],x[1]*y[2]+y[1]*x[2],x[2]*y[2]);}
function qneg(x){return [-x[0],-x[1],x[2]];}
function qm(x,y){return qn(x[0]*y[0]+2n*x[1]*y[1],x[0]*y[1]+x[1]*y[0],x[2]*y[2]);}
function qi(x){assert(x[0]*x[0]-2n*x[1]*x[1]!==0n);return qn(x[2]*x[0],-x[2]*x[1],x[0]*x[0]-2n*x[1]*x[1]);}
function qz(x){return x[0]===0n&&x[1]===0n;}
function qe(p){let v=qzero;for(let i=p.length-1;i>=0;i--)v=qa(qm(v,lambda),[p[i],0n,1n]);return v;}
function qt(p){p=p.slice();while(p.length&&qz(p.at(-1)))p.pop();return p;}
function qr(aa,bb){aa=qt(aa);bb=qt(bb);while(aa.length>=bb.length&&aa.length){const sh=aa.length-bb.length,v=qm(aa.at(-1),qi(bb.at(-1)));for(let i=0;i<bb.length;i++)aa[sh+i]=qa(aa[sh+i],qneg(qm(v,bb[i])));aa=qt(aa);}return aa;}
function qgcd(aa,bb){aa=qt(aa);bb=qt(bb);while(bb.length){const cc=qr(aa,bb);aa=bb;bb=cc;}const iv=qi(aa.at(-1));return aa.map(x=>qm(x,iv));}
const qg=qgcd(I.map(qe),H.map(qe));
assert(qg.length===2&&eq(qg[0],[-11n,6n,4n])&&eq(qg[1],[1n,0n,1n]),"sqrt2 collision-only gcd");
// Rabin's degree-6 irreducibility test modulo 41. All Number arithmetic
// uses products below 41^2 and reduction after each addition.
function mt(p){p=p.map(x=>(x%41+41)%41);while(p.length&&!p.at(-1))p.pop();return p;}
function mpow(v,n){let r=1;for(;n;n=Math.floor(n/2),v=v*v%41)if(n%2)r=r*v%41;return r;}
function mr(aa,bb){aa=mt(aa);const iv=mpow(bb.at(-1),39);while(aa.length>=bb.length&&aa.length){const sh=aa.length-bb.length,cc=aa.at(-1)*iv%41;for(let i=0;i<bb.length;i++)aa[sh+i]=(aa[sh+i]-cc*bb[i]%41+41)%41;aa=mt(aa);}return aa;}
function mm(aa,bb){const cc=Array(Math.max(0,aa.length+bb.length-1)).fill(0);for(let i=0;i<aa.length;i++)for(let j=0;j<bb.length;j++)cc[i+j]=(cc[i+j]+aa[i]*bb[j])%41;return mt(cc);}
function mg(aa,bb){aa=mt(aa);bb=mt(bb);while(bb.length){const cc=mr(aa,bb);aa=bb;bb=cc;}return aa;}
let mod=M.map(x=>Number((x%41n+41n)%41n));assert(mod.length===7&&mod.at(-1)!==0,"mod41 preserves degree");
mod=mod.map(x=>x*mpow(mod.at(-1),39)%41);
function mf(aa,n){let rr=[1];for(;n;n=Math.floor(n/2),aa=mr(mm(aa,aa),mod))if(n%2)rr=mr(mm(rr,aa),mod);return rr;}
let xp=[0,1];const frobenius=[];
for(let i=1;i<=6;i++){xp=mf(xp,41);const df=xp.slice();while(df.length<2)df.push(0);df[1]=(df[1]-1+41)%41;const dd=mt(df);if(i===2||i===3){const gd=mg(mod,dd).length-1;assert(gd===0,"Rabin gcd");frobenius.push({power:i,gcdDegree:gd});}if(i===6)assert(!dd.length,"Rabin final identity");}
const report={schema:"r150-unit211-S0-finite-rankdrop-exact-bigint-v1",status:"all_exact_cover_identities_pass",resultantDegree:res.length-1,sexticCoefficientsAscending:M.map(String),rationalFibers:special,sqrt2FiberGcd:qg.map(p=>p.map(String)),sexticIrreducibleModPrime:41,rabinChecks:frobenius,zGraphGcdsAllOne:true,lMinusOneGcdOne:true,maximumParameterFibers:24,claimExcluded:false,claimLambdaLayerEmpty:false,ordinaryISPClaim:false};
if(typeof text==="function")text(report);else console.log(JSON.stringify(report));
