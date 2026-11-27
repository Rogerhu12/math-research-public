(()=>{
"use strict";
const started=Date.now();
const T=a=>{a=a.map(BigInt);while(a.length&&a[a.length-1]===0n)a.pop();return a;};
const A=(a,b)=>T(Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||0n)+(b[i]||0n)));
const N=a=>a.map(x=>-x),S=(a,b)=>A(a,N(b));
const M=(a,b)=>{if(!a.length||!b.length)return [];const c=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=a[i]*b[j];return T(c);};
const scale=(a,n)=>T(a.map(x=>x*BigInt(n)));
const Pow=(a,n)=>{let b=[1n];while(n){if(n&1)b=M(b,a);n=Math.floor(n/2);if(n)a=M(a,a);}return b;};
const Eq=(a,b)=>S(a,b).length===0;
let exactDivisions=0;
function Div(a,b){if(!b.length)throw Error("zero divisor polynomial");let r=a.slice(),q=Array(Math.max(0,a.length-b.length+1)).fill(0n);while(r.length>=b.length&&r.length){const s=r.length-b.length,aa=r[r.length-1],bb=b[b.length-1];if(aa%bb)throw Error("nonintegral exact quotient");const c=aa/bb;q[s]+=c;const sub=Array(s).fill(0n).concat(scale(b,c));r=S(r,sub);}if(r.length)throw Error("nonexact polynomial quotient");q=T(q);if(!Eq(M(q,b),a))throw Error("division multiply-back");exactDivisions++;return q;}
const gi=[[0,0,"4096"],[0,1,"9216"],[0,2,"7680"],[0,3,"3072"],[0,4,"592"],[0,5,"24"],[0,6,"-10"],[0,7,"-1"],[1,1,"-6144"],[1,2,"-16128"],[1,3,"-14336"],[1,4,"-6048"],[1,5,"-1416"],[1,6,"-186"],[1,7,"-9"],[2,2,"512"],[2,3,"6016"],[2,4,"6560"],[2,5,"2528"],[2,6,"468"],[2,7,"50"],[2,8,"2"],[3,3,"1792"],[3,4,"832"],[3,5,"-832"],[3,6,"-392"],[3,7,"-50"],[3,8,"-2"],[4,4,"-256"],[4,5,"-544"],[4,6,"-24"],[4,7,"24"],[4,8,"4"],[5,5,"-192"],[5,7,"-8"],[6,6,"32"]];
const g=Array.from({length:7},()=>[]);
for(const [i,j,c] of gi){if(j<i)throw Error("bad coordinate");const t=Array(j-i).fill(0n).concat([BigInt(c)]);g[i]=A(g[i],t);}
if(!Eq(g[6],[32n]))throw Error("nonconstant leading");
function det(A0){const n=A0.length;if(!n)return [1n];let a=A0.map(r=>r.map(p=>p.slice())),old=[1n],sign=1n;for(let j=0;j<n-1;j++){if(!a[j][j].length){const sw=a.findIndex((r,i)=>i>j&&r[j].length);if(sw<0)return [];[a[j],a[sw]]=[a[sw],a[j]];sign=-sign;}const piv=a[j][j];for(let i=j+1;i<n;i++){for(let k=j+1;k<n;k++)a[i][k]=Div(S(M(piv,a[i][k]),M(a[i][j],a[j][k])),old);a[i][j]=[];}old=piv;}return scale(a[n-1][n-1],sign);}
function resultant(h){const n=6,m=h.length-1,sz=n+m,A0=Array.from({length:sz},()=>Array.from({length:sz},()=>[]));for(let i=0;i<m;i++)for(let j=0;j<=n;j++)A0[i][i+j]=g[n-j];for(let i=0;i<n;i++)for(let j=0;j<=m;j++)A0[m+i][i+j]=h[m-j];return det(A0);}
const abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b){const r=a%b;a=b;b=r;}return a;}
function primitive(a){if(!a.length)return a;let c=0n;for(const v of a)c=gcd(c,v);if(a[a.length-1]<0n)c=-c;return a.map(v=>v/c);}
function evalAt(a,x){let v=0n;for(let j=a.length-1;j>=0;j--)v=v*x+a[j];return v;}
const known=[["k",[0n,1n]],["k+1",[1n,1n]],["k+2",[2n,1n]],["k+4",[4n,1n]]];
function stripPaid(a){let f=primitive(a),removed=[];for(const [name,p] of known){let m=0;while(f.length>1&&evalAt(f,-p[0])===0n){f=Div(f,p);m++;}if(m)removed.push([name,m]);}let back=f;for(const [name,m] of removed)back=M(back,Pow(known.find(x=>x[0]===name)[1],m));if(!Eq(back,primitive(a)))throw Error("paid product");return {remaining:f,removed};}
const k=[0n,1n],km1=[1n,-1n],kp2=[2n,1n];
const linear=[
 ["e_numerator_Q",[1n],[]],
 ["u_numerator_Q_plus_k",[1n],k],
 ["d_one_minus_Q",[-1n],[1n]],
 ["V_Q_plus_k_plus_two",[1n],kp2],
 ["ell_numerator",[-2n],Pow(kp2,2)],
 ["Q_minus_two",[1n],[-2n]],
 ["P02_extra_P",[2n],[-8n,-5n,-1n]],
 ["u_minus_Q_numerator",km1,k],
 ["H",[4n],[-8n,-4n,-1n]],
 ["two_e_plus_one_numerator",[2n],k]
];
const outputs=[];
for(const [name,alpha,beta] of linear){let res=[];for(let i=0;i<=6;i++)res=A(res,M(g[i],M(Pow(N(beta),i),Pow(alpha,6-i))));const paid=stripPaid(res);outputs.push({name,rawDegree:res.length-1,normDenominatorConstant:"32",remainingDegree:paid.remaining.length-1,paidRemoved:paid.removed,remainingCoefficients:paid.remaining.map(String),rawCoefficients:res.map(String),allPaidProductsMultipliedBack:true});}
const hC9=[
 [16n,24n,10n,1n],
 [-16n,-20n,-9n,-1n],
 [4n]
];
const hM3=[
 [0n,-16n,-20n,-8n,-1n],
 [16n,32n,24n,8n,1n],
 [-16n,-12n,-3n],
 [4n]
];
const hJ19=[
 [0n,-128n,-160n,-104n,-40n,-10n,-1n],
 [-128n,0n,0n,-12n,-14n,-2n],
 [192n,64n,24n,-8n,-1n],
 [-96n,-16n,-8n],
 [16n]
];
for(const [name,h] of [["C9",hC9],["M13_times_k",hM3],["J19_times_k",hJ19]]){
 const res=resultant(h),paid=stripPaid(res);
 outputs.push({name,QDegree:h.length-1,definingCoefficientsInQ:h.map(a=>a.map(String)),
 rawDegree:res.length-1,normDenominatorConstant:String(32n**BigInt(h.length-1)),
 remainingDegree:paid.remaining.length-1,paidRemoved:paid.removed,
 remainingCoefficients:paid.remaining.map(String),rawCoefficients:res.map(String),
 entireFixedSylvesterDeterminantComputed:true,allBareissExactDivisionsMultipliedBack:true,allPaidProductsMultipliedBack:true});
}
return {seconds:(Date.now()-started)/1000,inputG36:gi,QDegree:6,QLeading:32,knownPaidScalarFibersOnly:["k","k+1","k+2","k+4"],norms:outputs,exactDivisions,allNormZeroFibersRetained:true,notAnEmptinessCertificate:true};
})()