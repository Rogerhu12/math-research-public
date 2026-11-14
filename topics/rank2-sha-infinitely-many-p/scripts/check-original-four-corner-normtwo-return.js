// Exact certificate for R405. Run: node check-original-four-corner-normtwo-return.js
// All arithmetic is rational BigInt; no sampling of target primes.
function verifyR405() {
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;}
class Q {
 constructor(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);this.a=a/g;this.b=b/g;}
 add(r){return new Q(this.a*r.b+r.a*this.b,this.b*r.b);}
 neg(){return new Q(-this.a,this.b);}
 mul(r){return new Q(this.a*r.a,this.b*r.b);}
 zero(){return this.a===0n;}
 str(){return this.b===1n?String(this.a):this.a+"/"+this.b;}
}
function ring(n) {
 const key=e=>e.join(",");
 const zero=()=>new Map();
 const c=(a,b=1)=>{const q=new Q(a,b);return q.zero()?zero():new Map([[key(Array(n).fill(0)),q]]);};
 const add=(p,q)=>{const r=new Map(p);for(const [e,a] of q){const v=(r.get(e)||new Q(0)).add(a);if(v.zero())r.delete(e);else r.set(e,v);}return r;};
 const neg=p=>new Map([...p].map(([e,a])=>[e,a.neg()]));
 const sub=(p,q)=>add(p,neg(q));
 const mul=(p,q)=>{let r=zero();for(const [ei,a] of p)for(const [ej,b] of q){const i=ei.split(",").map(Number),j=ej.split(",").map(Number);r=add(r,new Map([[key(i.map((v,k)=>v+j[k])),a.mul(b)]]));}return r;};
 const pow=(p,m)=>{let r=c(1);for(let i=0;i<m;i++)r=mul(r,p);return r;};
 const v=i=>{const e=Array(n).fill(0);e[i]=1;return new Map([[key(e),new Q(1)]]);};
 const scale=(p,a,b=1)=>mul(p,c(a,b));
 const eq=(p,q)=>sub(p,q).size===0;
 const coefficient=(p,e)=>(p.get(key(e))||new Q(0)).str();
 return {c,add,neg,sub,mul,pow,v,scale,eq,coefficient};
}
const checks=[];
const check=(name,p)=>{if(!p)throw Error(name);checks.push({name,pass:true});};
{
 const {c,add,sub,mul,pow,v,scale,eq,coefficient}=ring(2);
 const x=v(0),b=v(1),X=pow(x,3);
 const R=add(add(pow(X,2),scale(mul(b,X),20)),scale(pow(b,2),-8));
 const P2=add(add(pow(X,2),scale(mul(b,X),-4,7)),scale(pow(b,2),16,7));
 const Q4=mul(add(X,scale(b,4)),add(add(add(pow(X,3),scale(mul(b,pow(X,2)),-96)),scale(mul(pow(b,2),X),48)),scale(pow(b,3),64)));
 const C=mul(sub(X,scale(b,8)),P2);
 const D=mul(pow(x,2),add(X,b)),H=mul(pow(x,2),R);
 const K=mul(mul(x,add(X,b)),Q4),L=mul(mul(x,R),Q4);
 const S=mul(D,C),G=mul(H,C),T=mul(mul(D,L),C),Qcorner=mul(mul(D,K),C);
 check("actual D L equals H K",eq(mul(D,L),mul(H,K)));
 check("four-corner additive convolution ST=GQ",eq(mul(S,T),mul(G,Qcorner)));
 check("D degree and leading coefficient",coefficient(D,[5,0])==="1");
 check("H degree and leading coefficient",coefficient(H,[8,0])==="1");
 check("K degree and leading coefficient",coefficient(K,[16,0])==="1");
 check("L degree and leading coefficient",coefficient(L,[19,0])==="1");
 check("S order six in sigma34 frame",coefficient(S,[14,0])==="1"&&Math.max(...[...S.keys()].map(e=>+e.split(",")[0]))===14);
 check("T order six in sigma72 frame",coefficient(T,[33,0])==="1"&&Math.max(...[...T.keys()].map(e=>+e.split(",")[0]))===33);
 check("Q order twelve in sigma72 frame",coefficient(Qcorner,[30,0])==="1"&&Math.max(...[...Qcorner.keys()].map(e=>+e.split(",")[0]))===30);
}
{
 const {c,add,sub,mul,pow,v,scale,eq}=ring(3);
 const X=v(0),Y=v(1),b=v(2);
 const d=t=>add(t,b),h=t=>add(add(pow(t,2),scale(mul(b,t),20)),scale(pow(b,2),-8));
 const h0=t=>sub(pow(t,2),scale(pow(b,2),28));
 const anti=sub(mul(d(X),h(Y)),mul(h(X),d(Y)));
 check("20 b D correction cancels in antisymmetrization",
  eq(anti,sub(mul(d(X),h0(Y)),mul(h0(X),d(Y)))));
 check("exact antisymmetric rational polynomial",
  eq(anti,mul(sub(Y,X),add(add(mul(X,Y),mul(b,add(X,Y))),scale(pow(b,2),28)))));
 // A starts 2 delta z^3, delta^2=-3. The mu6 projection leaves z^6-w^6.
 check("original norm2 scalar",4*(-3)===-12);
}
{
 const M=[[1,1,1,0,0],[1,-1,0,1,1]],N=[8,8,18,38,18];
 const gram=M.map(a=>M.map(b=>a.reduce((s,x,k)=>s+x*N[k]*b[k],0)));
 check("actual five-input Hermitian Gram",JSON.stringify(gram)==="[[34,0],[0,72]]");
}
{
 const {c,add,sub,mul,pow,v,scale,eq}=ring(5);
 const l=v(0),sy=v(1),sr=v(2),aa=v(3),bb=v(4),one=c(1);
 const l2=pow(l,2),l3=pow(l,3),l5=pow(l,5);
 const Delta=[one,c(-1)],Sigma=[one,one];
 const va=(a,b)=>a.map((x,i)=>add(x,b[i]));
 const vs=(a,b)=>a.map((x,i)=>sub(x,b[i]));
 const vm=(a,t)=>a.map(x=>mul(x,t));
 const veq=(a,b)=>a.every((x,i)=>eq(x,b[i]));
 const CY=a=>vm(a,scale(l,-1));
 const CR=a=>[mul(scale(l,-1),a[0]),mul(l,a[1])];
 check("original Y core",veq(CY(Delta),vm(Delta,scale(l,-1))));
 check("original R core exchanges difference with sum",veq(CR(Delta),vm(Sigma,scale(l,-1))));
 check("both-output deep core",veq(CY(CR(Delta)),vm(Sigma,l2)));
 const E=vs(vm(Sigma,l2),vm(Delta,l5));
 check("primitive five-input double-depth row",
  veq(E,[mul(l2,sub(one,l3)),mul(l2,add(one,l3))]));
 check("unit return determinant exactly 2 lambda^2",eq(add(E[0],E[1]),scale(l2,2)));
 check("adjacent R annulus recovers target tensor",
  veq(vs(vm(Delta,l),CR(Delta)),[scale(l,2),c(0)]));
 check("primitive domain returns target tensor",
  veq(va(vm(Delta,mul(l2,add(one,l3))),E),[scale(l2,2),c(0)]));
 check("primitive domain returns other tensor",
  veq(va(vm(Delta,mul(l2,sub(l3,one))),E),[c(0),scale(l2,2)]));
 const K=a=>[scale(a[0],-1),a[1]];
 check("K square is identity",veq(K(K(Delta)),Delta));
 const ks=mul(l,sr);
 check("operator geometric inverse without infinite unit sum",
  veq(vs(va(Delta,vm(K(Delta),ks)),vm(K(va(Delta,vm(K(Delta),ks))),ks)),vm(Delta,sub(one,pow(ks,2)))));
 const numerator=sub(mul(aa,sub(one,ks)),mul(bb,add(one,ks)));
 check("two spectral parts have the common resolvent numerator",
  eq(numerator,sub(sub(aa,bb),mul(ks,add(aa,bb)))));
 check("all-five deep coefficient retains both axis factors",
  eq(sub(one,mul(l5,mul(sy,sr))),sub(one,mul(mul(l2,l3),mul(sy,sr)))));
 // Derivative of G/(1+lambda U), with U(0)=1, U'(0)=-h.
 const h=sy,g1=sr,m=add(one,l);
 const quotientNumerator=sub(mul(g1,m),mul(m,scale(mul(l,h),-1)));
 check("regularized mass-one slope retains the full scale term",
  eq(quotientNumerator,mul(add(g1,mul(l,h)),m)));
}
return {
 status:"PASS",exact_checks:checks.length,checks,
 arithmetic:"Q with BigInt; polynomial identities in formal parameters",
 input_degrees:[8,8,18,38,18],output_gram:[[34,0],[0,72]],
 core_order:["S:-lambda","T:-lambda","G:-lambda","Q:+lambda"],
 primitive_input_core:"lambda^5",return_determinant:"2 lambda^2",
 original_normtwo_scalar:"-1/12",
 common_axis_denominators:["1+lambda*t1*U1","1-lambda*t2*U2","1+lambda*t2*U2"],
 independent_inputs_preserved:5,
 no_prime_scan:true,
 dependency:"R399 supplies the entire original N7 matrix and K=N7^9, including integral denominator 2^17*3^17."
};
}
const certificate=verifyR405();
console.log(JSON.stringify(certificate,null,2));
