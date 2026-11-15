// R653. Exact original theta-pair certificate; Node.js, no packages.
"use strict";
const ck=(x,m)=>{if(!x)throw Error(m);};
const abs=x=>x<0n?-x:x,gcd=(x,y)=>{x=abs(x);y=abs(y);while(y)[x,y]=[y,x%y];return x;};
const Q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);ck(d!==0n,"zero denominator");if(d<0n){n=-n;d=-d;}let g=gcd(n,d);return[n/g,d/g];};
const qa=(x,y)=>Q(x[0]*y[1]+y[0]*x[1],x[1]*y[1]),qn=x=>[-x[0],x[1]],
qm=(x,y)=>Q(x[0]*y[0],x[1]*y[1]),qi=x=>Q(x[1],x[0]),
qs=x=>x[1]===1n?String(x[0]):String(x[0])+"/"+x[1];
const E=(a,b=0,d=1)=>[Q(a,d),Q(b,d)], ea=(x,y)=>[qa(x[0],y[0]),qa(x[1],y[1])],
en=x=>[qn(x[0]),qn(x[1])],es=(x,y)=>ea(x,en(y)),
em=(x,y)=>[qa(qm(x[0],y[0]),qn(qm(x[1],y[1]))),
qa(qa(qm(x[0],y[1]),qm(x[1],y[0])),qn(qm(x[1],y[1])))],
ec=x=>[qa(x[0],qn(x[1])),qn(x[1])],
eq=(x,y)=>x[0][0]===y[0][0]&&x[0][1]===y[0][1]&&x[1][0]===y[1][0]&&x[1][1]===y[1][1],
esc=(x,a,b=1)=>em(x,E(a,0,b)),ez=x=>eq(x,E(0)),
ei=x=>{let n=em(x,ec(x));ck(n[1][0]===0n,"norm rational");return[ qm(ec(x)[0],qi(n[0])),qm(ec(x)[1],qi(n[0])) ];},
out=x=>x.map(qs);
const he=(x,y)=>x.reduce((a,t,i)=>ea(a,em(t,ec(y[i]))),E(0));
const va=(x,y)=>x.map((t,i)=>ea(t,y[i])),vs=(x,y)=>x.map((t,i)=>es(t,y[i])),
vm=(x,c)=>x.map(t=>em(t,c));
const mm=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((s,t,k)=>ea(s,em(t,B[k][j])),E(0))));
const ident=n=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>E(i===j?1:0)));
function inverse(A){let M=A.map(row=>row.map(x=>x)),B=ident(A.length),det=E(1);
 for(let k=0;k<M.length;k++){let p=k;while(p<M.length&&ez(M[p][k]))p++;ck(p<M.length,"singular");
  if(p!==k){[M[p],M[k]]=[M[k],M[p]];[B[p],B[k]]=[B[k],B[p]];det=en(det);}
  const pivot=M[k][k];det=em(det,pivot);const inv=ei(pivot);M[k]=vm(M[k],inv);B[k]=vm(B[k],inv);
  for(let i=0;i<M.length;i++)if(i!==k&&!ez(M[i][k])){const f=M[i][k];M[i]=vs(M[i],vm(M[k],f));B[i]=vs(B[i],vm(B[k],f));}
 } return {inverse:B,det}; }



function certificate(){

const del=E(1,2),om=E(0,1),om2=E(-1,-1);
const Qrow=[E(1),E(2)],Lrow=[E(2),E(-1)];
ck(eq(he(Qrow,Qrow),E(5))&&eq(he(Lrow,Lrow),E(5))&&ez(he(Qrow,Lrow)),"whole pair Gram");
ck(eq(inverse([Qrow,Lrow]).det,E(-5)),"pair determinant");
const types=[{name:"D5",k:0,order:0,leading:"1"},
{name:"Z5",k:1,order:1,leading:"1"},
{name:"F12",k:2,order:2,leading:"2"},
{name:"X5",k:3,order:3,leading:"1"},
{name:"Sigma5",k:5,order:5,leading:"1"}];
const pairs=[];for(const x of types)for(const y of types)if((x.k+y.k)%6===2)pairs.push([x.name,y.name]);
ck(pairs.length===5,"all tensor types");
const binom=(n,k)=>{let r=1n;for(let j=1;j<=k;j++)r=r*BigInt(n+1-j)/BigInt(j);return r;};
const power=(a,n)=>BigInt(a)**BigInt(n);
function degree8(qexp){
 let sum=0n;
 // (q+2l)^7(2q-l)
 if(qexp>=1&&qexp-1<=7)sum+=2n*binom(7,qexp-1)*power(2,8-qexp);
 if(qexp<=7)sum-=binom(7,qexp)*power(2,7-qexp);
 // (q+2l)(2q-l)^7
 if(qexp>=1&&qexp-1<=7)sum+=binom(7,qexp-1)*power(2,qexp-1)*power(-1,8-qexp);
 if(qexp<=7)sum+=2n*binom(7,qexp)*power(2,qexp)*power(-1,7-qexp);
 return sum;
}
ck(degree8(3)===1260n&&degree8(5)===1260n,"complete degree8 coefficients");
const A=[del,em(E(2),del),E(3,1),E(2,-1),E(0),E(0)];
const Q5=[E(0),E(0),E(0),E(0),E(1),E(2)],L5=[E(0),E(0),E(0),E(0),E(2),E(-1)];
const C=vm([E(1),E(0),E(-1),E(1),E(0),E(0)],ei(del));
const D4=[E(1),om2,E(0,-2),E(0),E(0),E(0)],H1=[E(-1),E(2),om,E(1,1),E(0),E(0)];
const F=va(va(D4,C),[E(0),E(0),E(0),E(0),E(1),E(2,3)]);
const g=E(3,-2),a=E(-5,-6,29),bF=E(5,6,5),G=va(vm(H1,E(13)),vm(F,g));
const Fi=[vs(vs(F,vm(A,a)),vm(Q5,bF)),vs(F,vm(Q5,bF))],Gi=Fi.map(r=>va(vm(H1,E(13)),vm(r,g)));
const equality=(x,y,m)=>ck(x.every((z,j)=>eq(z,y[j])),m);
equality(Fi[1],va(va(D4,C),vm(L5,E(0,-3,5))),"frozen L coefficient");
for(const r of [A,C,...Fi,...Gi])ck(ez(he(r,Q5)),"Q independence");
for(const r of [A,Q5,L5,...Fi,...Gi])ck(ez(he(r,C)),"C independence");
const bq=E(11,6,5),gammas=[E(-6,-1,60),E(-61,-36,360)];
const failureQ=gammas.map(v=>em(v,bq));
ck(failureQ.every(x=>!ez(x)),"moving cuts are not angularly invariant");
return {
curve_b:17,period:"original Omega_p; no physical dilation",
pair_matrix:[[["1","0"],["2","0"]],[["2","0"],["-1","0"]]],determinant:["-5","0"],Gram:["5","5"],
basis:types,simultaneous_type_pairs:pairs,
degree8_integer_coefficients:{q3l5:String(degree8(3)),q5l3:String(degree8(5))},
whole_tensor_coefficients:{"F12*D5":"1","D5*F12":"-1","Z5*Z5":"3","X5*Sigma5":"6b","Sigma5*X5":"6b"},
whole_Q_moment0:"-nu_F12(L)",whole_Q_moment1:"3 Omega nu_Z5(L)",
scalar_rows:["log-principal D5","unit negative-one Sigma5","unit positive-one-log Z5"],
fixed_rows:{F0:Fi[0].map(out),F1:Fi[1].map(out),G0:Gi[0].map(out),G1:Gi[1].map(out)},
Q_free_and_C_free_checks:true,W_failure_Q_coefficients_divided_by_z_minus_one:failureQ.map(out),
native_four_rows:["-M0 ellD","6b Hminus I_Sigma,-1 +3 bF Hplus ellZ,1","-A0","3 Omega A1"],
annular_reference_difference:"-m M0 (1-chi lambda) log<lambda^2>",
unhatted_baseline:"all four full coefficients zero; restricted pieces remain",
boundary_scope:"five whole tensor summands and every moved Q cut retained"
};
}
const text=JSON.stringify(certificate(),null,2)+'\n';
if(process.argv[2])require('fs').writeFileSync(process.argv[2],text);else process.stdout.write(text);
