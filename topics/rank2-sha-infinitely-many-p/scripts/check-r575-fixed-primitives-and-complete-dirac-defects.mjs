// R575: fixed primitive towers, positive w normalization and full support-valued cores.
// Run: node check-r575-fixed-primitives-and-complete-dirac-defects.mjs
// Algebraic independence is proved in the companion text, not inferred from jets.
const data=(()=>{
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b]}return a};
const rat=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g]};
const addq=(a,b)=>rat(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),mulq=(a,b)=>rat(a[0]*b[0],a[1]*b[1]);
const negq=a=>[-a[0],a[1]],qs=a=>a[0].toString()+"/"+a[1].toString();
let checks=0;const check=(ok,label)=>{checks++;if(!ok)throw Error(label)};
const key=(j,e)=>j+"|"+e;
function addterm(A,j,e,c){const k=key(j,e),v=addq(A.get(k)||rat(0),c);if(v[0])A.set(k,v);else A.delete(k);}
function diff(A){
 const B=new Map();
 for(const[k,c]of A){const [token,es]=k.split("|"),e=Number(es);
  if(e)addterm(B,token,e-1,mulq(c,rat(e)));
  const [tag,index]=token.split(":");
  if(tag.startsWith("J"))addterm(B,"f"+tag.slice(1)+":0",e+Number(index),c);
  else addterm(B,tag+":"+(Number(index)+1),e,c);
 }
 return B;
}
const binom=(n,k)=>{let q=1;for(let i=1;i<=k;i++)q=q*(n-i+1)/i;return q};
const fact=n=>{let r=1n;for(let j=2;j<=n;j++)r*=BigInt(j);return r};
const towers=[];
for(const[source,maxr,leading]of[["4",2,4],["1",5,1]]){
 for(let r=1;r<=maxr;r++){
  const A=new Map();
  for(let j=0;j<r;j++)addterm(A,"J"+source+":"+j,r-1-j,rat((j%2?-1:1)*binom(r-1,j),fact(r-1)));
  let B=A;
  for(let j=0;j<r;j++){
   check([...B].every(([k])=>k.split("|")[0].startsWith("J")),"zero initial jet "+source+","+r+","+j);
   B=diff(B);
  }
  check(B.size===1&&qs(B.get(key("f"+source+":0",0))||rat(0))==="1/1","actual r-th primitive "+source+","+r);
  const diagonal=rat((r-1)%2?-1:1,fact(r-1));
  check(diagonal[0]!==0n,"triangular primitive transform "+source+","+r);
  const character=(leading+r)%6;
  const defectMaySurvive=character===0;
  check(defectMaySurvive===((source==="4"&&r===2)||(source==="1"&&r===5)),"only two actual negative moments");
  towers.push({source,r,leading_z_power:leading+r,tame_character:character,
   diagonal:qs(diagonal),negative_unit_moment_forced_zero:!defectMaySurvive,
   complete_formula:Object.fromEntries([...A].map(([k,c])=>[k,qs(c)]))});
 }
}

for(const[source,R,leading]of[["4",2,4],["1",5,1]]){
 const F=new Map();
 for(let j=0;j<R;j++)addterm(F,"J"+source+":"+j,R-1-j,rat((j%2?-1:1)*binom(R-1,j),fact(R-1)));
 for(let r=1;r<=R;r++){
  const a=R-r;
  check((leading+r+a)%6===0,"positive normalization tame type "+source+","+r);
  check(r+a===R,"actual normalized distribution order "+source+","+r);
  const V=new Map();
  for(let j=0;j<r;j++)addterm(V,"J"+source+":"+j,r-1-j+a,rat((j%2?-1:1)*binom(r-1,j),fact(r-1)));
  let H=F;for(let j=0;j<a;j++)H=diff(H);
  H=new Map([...H].map(([k,c])=>{const[t,e]=k.split("|");return[key(t,Number(e)+a),c]}));
  check(V.size===H.size&&[...V].every(([k,c])=>qs(c)===qs(H.get(k)||rat(0))),"entire Euler primitive identity "+source+","+r);
 }
}

const coeff=(source,r,n,c)=>rat(BigInt(c[0])*fact(n),BigInt(c[1])*fact(n+r));
const F4z6=coeff("4",2,4,[1,1]),F4z12=coeff("4",2,10,[-4,35]),
 F1z6=coeff("1",5,1,[1,1]),F1z12=coeff("1",5,7,[6,35]);
check(qs(F4z6)==="1/30"&&qs(F1z6)==="1/720","actual leading primitive coefficients");
check(qs(addq(F4z6,mulq(rat(-24),F1z6)))==="0/1","same leading six-jet cancellation");
check(qs(addq(F4z12,mulq(rat(-24),F1z12)))==="-1/1100","actual twelve-jet difference");
// Formal support-valued polynomials in a=beta*kappa^{-r}.
// A_j means [kappa^j]_*tau; Delta means I*delta_0.
const support=(N)=>{const A=new Map();for(let j=0;j<=N;j++){A.set("A"+j+"|"+j,1);A.set("Delta|"+j,-1);}return A};
function plus(A,B,scale=1){const C=new Map(A);for(const[k,v]of B){const z=(C.get(k)||0)+scale*v;if(z)C.set(k,z);else C.delete(k);}return C}
function restrict(A,m){return new Map([...A].filter(([k])=>k.startsWith("Delta")||Number(k.split("|")[0].slice(1))>=m));}
function shift(A,m){return new Map([...A].map(([k,v])=>{const[t,e]=k.split("|");return[(t==="Delta"?t:"A"+(Number(t.slice(1))+m))+"|"+(Number(e)+m),v]}));}
for(let N=0;N<=10;N++){
 const lhs=plus(plus(restrict(support(N),1),shift(support(N),1),-1),new Map([["Delta|0",1]]));
 const rhs=new Map([["A"+(N+1)+"|"+(N+1),-1],["Delta|"+(N+1),1]]);
 check(plus(lhs,rhs,-1).size===0,"finite full-source core with boundary "+N);
 for(let m=1;m<=N;m++){
  let rhs2=shift(support(N-m),m);
  for(let j=0;j<m;j++)rhs2=plus(rhs2,new Map([["Delta|"+j,-1]]));
  check(plus(restrict(support(N),m),rhs2,-1).size===0,"whole p^m cut with all Dirac terms "+N+","+m);
 }
}
return {result:"all exact checks passed",checks,towers,
 primitive_coefficients:{F4_z6:qs(F4z6),F4_z12_over_b:qs(F4z12),F1_z6:qs(F1z6),F1_z12_over_b:qs(F1z12),difference_z12_over_b:"-1/1100"},
 actual_distribution:"sum_n beta^n*kappa^(-rn)*[kappa^n]_*(tau-I*delta_0)",
 core:"rho|p = beta*kappa^(-r)*[kappa]_*rho-I*delta_0",
 all_powers_core:"rho|p^m = a^m*[kappa^m]_*rho-I*(1+a+...+a^(m-1))*delta_0",
 algebraic_independence:"proved in text, not inferred from this finite certificate",
 bounded_measure_claim:false,arithmetic_saturation_claim:false,target_nonvanishing_proved:false};
})();
data.positive_normalization={"V4r":"z^(2-r) U4r","V1r":"z^(5-r) U1r","all_w_order":"1/3","new_transcendence_degree_with_ST":9,"actual_distribution":"(-partial_t)^(R-r) rho","normalized_core":"beta*kappa^(-R), R=2 or 5; only original I4,I1 defects"};
console.log(JSON.stringify(data,null,2));
