function certificate(){
const abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b)[a,b]=[b,a%b];return a}
function q(a,b=1n){a=BigInt(a);b=BigInt(b);if(b<0n){a=-a;b=-b}const d=gcd(a,b);return[a/d,b/d]}
const add=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),mul=(a,b)=>q(a[0]*b[0],a[1]*b[1]),sc=(a,n,d=1)=>mul(a,q(n,d));
const p=17,s=3;
function binom(n,k){if(k<0||k>n)return 0n;let a=1n;for(let j=1;j<=k;j++)a=a*BigInt(n-j+1)/BigInt(j);return a}
const mod=x=>Number((BigInt(x)%BigInt(p)+BigInt(p))%BigInt(p));
function pow(a,n){a=mod(a);let r=1;for(;n;n>>=1,a=a*a%p)if(n&1)r=r*a%p;return r}
function red(a){if(a[1]%BigInt(p)===0n)throw Error("nonintegral row");return mod(a[0])*pow(mod(a[1]),p-2)%p}
function exp(a){const r=Array.from({length:s+1},()=>q(0));r[0]=q(1);for(let n=1;n<=s;n++){let z=q(0);for(let j=1;j<=n;j++)z=add(z,sc(mul(a[j],r[n-j]),j));r[n]=sc(z,1,n)}return r}
function conv(a,b){return a.map((_,n)=>{let z=q(0);for(let j=0;j<=n;j++)z=add(z,mul(a[j],b[n-j]));return z})}
function mixed(A,B){let m=0n;for(let j=0;j<=6;j++)m+=binom(A,j)*binom(B,6-j)*((B-6+j)%2? -1n:1n);return m}
let checks=0;function check(x,y,msg){checks++;if(x!==y)throw Error(msg+": "+x+" != "+y)}
const frames=[];
for(const b of [1,2]){
 const A=Array.from({length:s+1},()=>q(0));A[0]=q(1);A[1]=q(-b,7);
 for(let n=2;n<=s;n++){let z=q(0);for(let j=1;j<n;j++)z=add(z,mul(A[j],A[n-j]));A[n]=sc(z,1,(6*n+1)*(n-1))}
 const log6=A.map((x,n)=>n?sc(x,-1,n*(6*n-1)):q(0));
 const sigma=exp(log6.map(x=>sc(x,1,6))),sigma3=exp(log6.map(x=>sc(x,1,2)));
 const yy=A.map((x,n)=>sc(x,1-3*n)),B3=conv(yy,sigma3);
 const AS=conv(A,exp(log6)),ABS=conv(yy,AS);
 const c4=red(AS[s-1]),c1=red(ABS[s-1]);
 const cp=mod(binom(3*s-1,2*s-1)*BigInt(b)**BigInt(s));
 const results={};
 for(const [name,source,offset,target] of [["P",sigma3,3,AS[s-1]],["B",B3,0,ABS[s-1]]]){
  let total=q(0),interior=q(0),ends=q(0);
  const terms=[];
  for(let i=0;i<=s;i++){
   const j=s-i,term=sc(mul(source[i],sigma[j]),(-27n)**BigInt(j)*mixed(6*i+offset,6*j+1));
   total=add(total,term);
   if(i===0||i===s)ends=add(ends,term);else interior=add(interior,term);
   terms.push(term.map(String));
  }
  const rhs=sc(target,12*b,5);
  check(total[0]*rhs[1]===rhs[0]*total[1],true,"complete original addition identity "+name);
  const expectedEnds=name==="P"?mod(-14*cp*pow(5,p-2)):mod(cp*pow(5,p-2));
  check(red(ends),expectedEnds,"two complete Gaussian endpoint contribution "+name);
  check((red(interior)+red(ends))%p,red(rhs),"all integral convolution retained "+name);
  results[name]={whole:total.map(String),whole_mod_p:red(total),regular:interior.map(String),regular_mod_p:red(interior),endpoints:ends.map(String),endpoints_mod_p:red(ends),terms};
 }
 check((results.P.regular_mod_p+14*results.B.regular_mod_p)%p,mod(12*b*pow(5,p-2)*(c4+14*c1)),"true zero-constant combination");
 frames.push({p,b,c4,c1,cp,original_addition_rows:results});
}
return {status:"all exact checks passed",checks,frames,
 actual_normalization:"F_P/a and F_B/a; a=2+omega, a^6=-27",
 complete_regular_convolutions_retained:true,
 target_nonvanishing_claim:false,main_target_complete:false};
}
console.log(JSON.stringify(certificate(),null,2));
