/* Exact BigInt certificate: failure of the single-quadratic Rayleigh sufficient test.
 * It does not claim failure of the primitive Gram inequality.
 * Run with node; no dependencies, input files, or floating-point sign tests.
 */
function verify() {

"use strict";
function assert(c,m){if(!c)throw new Error(m);}
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r;}return a;}
function det3(M){return M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])-M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]);}
function adj3(M){const A=Array.from({length:3},()=>Array(3).fill(0n));for(let i=0;i<3;i++)for(let j=0;j<3;j++){const rr=[0,1,2].filter(k=>k!==j),cc=[0,1,2].filter(k=>k!==i);A[i][j]=( (i+j)%2?-1n:1n)*(M[rr[0]][cc[0]]*M[rr[1]][cc[1]]-M[rr[0]][cc[1]]*M[rr[1]][cc[0]]);}return A;}
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n);
const mv=(A,x)=>A.map(r=>dot(r,x));
const q=100,half=50,Q=100n;
const fact=[1n];for(let j=1;j<=q;j++)fact[j]=fact[j-1]*BigInt(j);
const choose=Array.from({length:half+1},(_,j)=>fact[half]/(fact[j]*fact[half-j]));
const pow=(a,n)=>Array.from({length:n+1},(_,j)=>a**BigInt(j));
const p4=pow(4n,half),p5=pow(5n,q),p6=pow(6n,half);
const states=[];
for(let p=0;p<=half;p++)for(let s=0;s<=half;s++){
 const r=BigInt(p+s),d=BigInt(p-s);
 const w=choose[p]*choose[s]*p5[p+s]*p4[half-p]*p6[half-s]*fact[p+s]*fact[q-p-s];
 states.push({r,d,w,b:[1n,r,d]});
}
let wg=0n;for(const x of states)wg=gcd(wg,x.w);for(const x of states)x.w/=wg;
const M=Array.from({length:3},()=>Array(3).fill(0n)),c=Array(3).fill(0n);
for(const x of states)for(let i=0;i<3;i++){c[i]+=x.w*x.r*x.r*x.b[i];for(let j=0;j<3;j++)M[i][j]+=x.w*x.b[i]*x.b[j];}
const Z=M[0][0],dM=det3(M),J=adj3(M);assert(Z>0n&&dM>0n,"positive moment matrix");
assert(M[0][0]*M[1][1]-M[0][1]**2n>0n,"positive first minor");
for(let i=0;i<3;i++)for(let j=0;j<3;j++)assert(dot(M[i],J.map(r=>r[j]))===(i===j?dM:0n),"adjugate identity");
let bn=mv(J,c),bd=dM,bg=bd;for(const b of bn)bg=gcd(bg,b);bn=bn.map(b=>b/bg);bd/=bg;
let S=0n,SA=0n;const dv=Array(3).fill(0n),orth=Array(3).fill(0n);
for(const x of states){
 const T=bd*x.r*x.r-dot(bn,x.b);
 S+=x.w*T*T;SA+=x.w*x.r*(Q-x.r)*T*T;
 for(let i=0;i<3;i++){dv[i]+=x.w*x.r*T*x.b[i];orth[i]+=x.w*T*x.b[i];}
}
assert(orth.every(x=>x===0n),"full linear regression orthogonality");
assert(S>0n&&SA>0n,"nonzero quadratic residual");
const SD=dot(dv,mv(J,dv)),A1=SA*dM+(Q+1n)*SD;
assert(SD>0n&&A1>0n,"positive Rayleigh denominator");
const m1=M[0][1],m2=M[1][1];
const Rnum=(Q+2n)*(Z*m2-m1*m1)-(m1+Z)*((Q+1n)*Z-m1);
assert(Rnum>0n,"positive correction threshold");
const tauNum=Q*S*S*dM,tauDen=Z*(Q+1n)*bd*bd*A1;
const reqNum=Rnum,reqDen=Z*Z*(Q+1n)*(Q+2n);
const num=Q*(Q+2n)*Z*S*S*dM-Rnum*bd*bd*A1;
const den=Z*Z*(Q+1n)*(Q+2n)*bd*bd*A1;
assert(num<0n,"single quadratic criterion fails");
assert(40n*num+den>0n,"margin greater than -1/40");
assert(50n*num+den<0n,"margin less than -1/50");
const rat=(n,d)=>{const scale=10n**12n;return Number(n*scale/d)/1e12;};
return {status:"PASS",q,head_groups:[[50,"5/4"],[50,"5/6"]],states:states.length,
tau_quad:rat(tauNum,tauDen),threshold:rat(reqNum,reqDen),margin:rat(num,den),
exact_margin_interval:["-1/40","-1/50"],orthogonality:true,
coefficient_denominator_digits:bd.toString().length,
signed_numerator_digits:(-num).toString().length};

}
console.log(JSON.stringify(verify(), null, 2));
