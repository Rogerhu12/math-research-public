/* NEW exact original Gram return on W,t=0,V2=0.
Self-contained rational arithmetic over QQ(u), retaining the ENTIRE
z^2=(2ell-1) algebra and rho^2=1-Q, including both z/rho signs.
Correct jet product v1*w0+v0*w1, no compact-R2 source.
No old determinant/Popov/finite gate is repeated. */
const start=Date.now(); let qops=0, pops=0, rchecks=0;
function igcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r;}return a;}
function Q(a=0n,b=1n){if(Array.isArray(a)){b=a[1];a=a[0];}else a=BigInt(a);b=BigInt(b);if(!b)throw Error('zero rational denominator');if(!a)return [0n,1n];if(b<0n){a=-a;b=-b;}const g=igcd(a,b);return[a/g,b/g];}
function qa(a,b){qops++;return Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);}
function qn(a){return[-a[0],a[1]];}function qs(a,b){return qa(a,qn(b));}
function qm(a,b){qops++;return Q(a[0]*b[0],a[1]*b[1]);}
function qi(a){if(!a[0])throw Error('zero rational inverse');return Q(a[1],a[0]);}
function qd(a,b){return qm(a,qi(b));}
function qt(a){return a[1]===1n?String(a[0]):String(a[0])+'/'+String(a[1]);}
function trim(a){while(a.length&&!a[a.length-1][0])a.pop();return a;}
function pp(a){return trim(a.map(x=>Q(x)));}
const P0=[],P1=[Q(1)];
function pa(a,b){pops++;const r=[];for(let i=0;i<Math.max(a.length,b.length);i++)r.push(qa(a[i]||Q(),b[i]||Q()));return trim(r);}
function pn(a){return a.map(qn);}function ps(a,b){return pa(a,pn(b));}
function pm(a,b){pops++;if(!a.length||!b.length)return[];const r=Array.from({length:a.length+b.length-1},()=>Q());for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)r[i+j]=qa(r[i+j],qm(a[i],b[j]));return trim(r);}
function pc(a,c){return trim(a.map(x=>qm(x,c)));}
function pdm(a,b){if(!b.length)throw Error('zero polynomial divisor');let r=a.slice();const out=Array.from({length:Math.max(0,a.length-b.length+1)},()=>Q());while(r.length>=b.length){const d=r.length-b.length,c=qd(r[r.length-1],b[b.length-1]);out[d]=qa(out[d],c);for(let j=0;j<b.length;j++)r[d+j]=qs(r[d+j],qm(c,b[j]));trim(r);}return[trim(out),r];}
function peq(a,b){return !ps(a,b).length;}
function pmonic(a){return a.length?pc(a,qi(a[a.length-1])):[];}
function pgcd(a,b){while(b.length){const r=pdm(a,b)[1];a=b;b=r;}return pmonic(a);}
function pexact(a,b){const[q,r]=pdm(a,b);if(r.length)throw Error('inexact polynomial division');if(!peq(pm(q,b),a))throw Error('division multiplication failed');rchecks++;return q;}
function pxgcd(a,b){const aa=a,bb=b;let s0=P1,s1=[],t0=[],t1=P1;while(b.length){const[q,r]=pdm(a,b);[a,b]=[b,r];[s0,s1]=[s1,ps(s0,pm(q,s1))];[t0,t1]=[t1,ps(t0,pm(q,t1))];}if(!a.length)return[[],[],[]];const c=qi(a[a.length-1]);a=pc(a,c);s0=pc(s0,c);t0=pc(t0,c);if(!peq(pa(pm(s0,aa),pm(t0,bb)),a))throw Error('Bezout multiplication failed');rchecks++;return[a,s0,t0];}
function powp(a,n){let r=P1;while(n){if(n&1)r=pm(r,a);a=pm(a,a);n>>=1;}return r;}
const n0=pp([6,-15,2]),n1=pp([-2,1,-2]);
const s0=pp([-4,12,-11,6,-1]),s1=pp([4,-12,11,-2,1]);
const p0=pp([-8,44,-98,117,-69,12,-1]),p1=pp([-8,44,-74,37,9,-8,1]);
const A=pp([4,-20,23,-4,1]),B=pp([-16,96,-200,160,-35,2,1]),h=pp([-2,3]);
const detA=ps(pm(n0,s1),pm(s0,n1)),detB=ps(pm(n0,p1),pm(p0,n1));
if(!peq(detA,pc(pm(h,A),Q(-2)))||!peq(detB,pc(pm(h,B),Q(-2))))throw Error('original two-column cofactor identity');
const [gg,S,T]=pxgcd(A,B);if(!peq(gg,P1))throw Error('remaining parameter factor');
const alpha=pa(pm(S,s1),pm(T,p1)),beta=pn(pm(S,n1)),gamma=pn(pm(T,n1));
if(!peq(pa(pa(pm(alpha,n0),pm(beta,s0)),pm(gamma,p0)),pc(h,Q(-2))))throw Error('original constant column');
if(!peq(pa(pa(pm(alpha,n1),pm(beta,s1)),pm(gamma,p1)),[]))throw Error('original z column');
const numeratorS=pp([-355796,1592324,-2043739,492974,-39727,-14852]);
const numeratorT=pp([-89087,308304,-49385,14852]);
if(!peq(pa(pm(numeratorS,A),pm(numeratorT,B)),pp([2208])))throw Error('displayed integer Bezout');
return {stage:'new_original_two_column_cofactor_and_complete_QQ_Bezout',
seconds:(Date.now()-start)/1000,entireQuadZRetained:true,
originalTwoCofactorProductsReturned:true,allTwoOriginalCombinationColumnsReturned:true,
displayedIntegerBezoutReturned:true,QQgcdDegree:gg.length-1,
BezoutDenominator:2208,originalTarget:'-2*(3*u-2)',
claimWhole_t0_f_u_V2_zero_Excluded:true};
