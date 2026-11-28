"use strict";
// NEW unrestricted original t=0 mean identity and complete h=k value reduction.
// Seven free b,c,p,q,X,Y,eta; no Phi/W/Pf assumption or N/P gate replay.
// Pure value identities use separate formal lambda,h,w coordinates.
const began=Date.now(),D=7,ZKEY="0,0,0,0,0,0,0";let products=0;
function C(n=0n){return n===0n?new Map():new Map([[ZKEY,n]])}
function V(i){const a=Array(D).fill(0);a[i]=1;return new Map([[a.join(","),1n]])}
function add(a,b){const c=new Map(a);for(const[k,v]of b){let x=(c.get(k)||0n)+v;if(x)c.set(k,x);else c.delete(k)}return c}
function neg(a){return new Map([...a].map(([k,v])=>[k,-v]))}
function sub(a,b){return add(a,neg(b))}
function mul(a,b){if(Date.now()-began>120000)throw Error("new original tzero mean and collision value identity 120 second budget");products++;const c=new Map();for(const[ka,va]of a){const ea=ka.split(",").map(Number);for(const[kb,vb]of b){const eb=kb.split(",").map(Number),k=ea.map((x,i)=>x+eb[i]).join(","),x=(c.get(k)||0n)+va*vb;if(x)c.set(k,x);else c.delete(k)}}return c}
function sc(a,n){return mul(a,C(BigInt(n)))}
function sq(a){return mul(a,a)}
function sum(xs){return xs.reduce(add,C())}
function prod(xs){return xs.reduce(mul,C(1n))}

const [b,c,p,q,X,Y,eta]=Array.from({length:D},(_,i)=>V(i));
const t=C();
const one=C(1n),zero=C(),ell=add(b,c),a=sub(one,ell);
const uu=add(mul(b,p),mul(c,q)),scalarV0=add(mul(b,X),mul(c,Y));
const r=sub(sub(X,mul(a,p)),mul(c,t)),s=sub(sub(Y,mul(a,q)),mul(b,t));
const A1=add(sub(sc(add(uu,eta),2),sc(scalarV0,2)),sc(prod([b,c,t]),2));
const rows=[[zero,zero,p,q],[zero,A1,r,s],
            [p,r,zero,t],[q,s,t,zero]];
const unit=[one,zero,one,one];
function vm(v,w){return[mul(v[0],w[0]),add(mul(v[0],w[1]),mul(v[1],w[0])),
                         mul(v[2],w[2]),mul(v[3],w[3])]}
function va(v,w){return v.map((x,i)=>add(x,w[i]))}
function vs(x,v){return v.map(t=>mul(x,t))}
function tau(v){return sum([mul(a,v[0]),v[1],mul(b,v[2]),mul(c,v[3])])}
function DK(v){return rows.map(row=>tau(vm(row,v)))}
const dv=DK(unit),F2=tau(dv),Kd=DK(dv),dd=vm(dv,dv);
const checks=[];
function check(name,P){if(P.size)throw Error(name+": "+P.size+" nonzero terms");
 checks.push({name,fullIntegerPolynomialDifferenceZero:true});}
const u=tau(rows[0]),d1=tau(rows[1]);
const scalarV=add(mul(b,dv[2]),mul(c,dv[3]));
function mean(j){
 const e=j===1?sc(tau(vm(rows[0],rows[1])),2):tau(vm(rows[j],rows[j]));
 return sum([e,sc(Kd[j],-2),sc(dd[j],-2),sc(mul(F2,dv[j]),2)]);
}

const E0=mean(0),E1=mean(1),EB=mean(2),EC=mean(3);
const EW=add(mul(b,EB),mul(c,EC));
check("entire_original_tzero_mean_identity",
 sub(sum([E1,neg(EW),mul(a,E0)]),sc(mul(eta,A1),4)));
const lm=V(0),hv=V(1),wv=V(2);
const kval=sub(sc(lm,2),one);
const mv1=sum([one,sc(wv,2),hv,sc(lm,-2)]);
const mv2=sum([one,sc(wv,4),sq(hv),sc(sq(lm),-4)]);
const av=sum([C(3n),neg(hv),sc(lm,-2)]);
check("half_total_weight_first_two_value_identity",
 sum([mv2,neg(mul(sum([hv,sc(lm,2),neg(one)]),mv1)),
      sc(kval,2),sc(mul(av,wv),-2)]));
const half1=add(sc(wv,2),hv),half2=add(sc(wv,4),sq(hv));
const half3=add(sc(wv,6),mul(sq(hv),hv));
check("lambda_half_collision_three_moments_force_h_zero",
 sub(sum([half3,neg(mul(add(hv,C(2n)),half2)),
          mul(add(sc(hv,2),one),half1)]),hv));
return {schema:"isp-original-tzero-whole-mean-and-collision-value-identities-v1",
 variables:["b","c","p","q","X","Y","eta"],t:0,f:"u+eta",
 elapsedMilliseconds:Date.now()-began,integerPolynomialProducts:products,checks,
 exactOriginalMeanIdentity:"E1-(b*EB+c*EC)+(1-ell)*E0=4*(f-u)*A1",
 trueDualSquare:true,noPhiWOrPfAssumption:true,
 separateFormalValueVariables:["lambda","h","w"],valueIdentity:"m2-(h+2lambda-1)m1+2(2lambda-1)-2(3-h-2lambda)w=0",
 halfLambdaIdentity:"m3-(h+2)m2+(2h+1)m1=h",
 noOldNPOrProjectionGateReexecuted:true,ordinaryISPClaim:false};
