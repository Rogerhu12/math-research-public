// Exact all-q certificate for height three: two equal-weight groups and one exceptional site.
// Run: node isp-two-groups-one-bit-height-three-allq-1856-certificate.mjs
// All arithmetic in the certificate is BigInt. Finite q checks are only independent formula checks;
// the all-q proof is the bounded-degree Newton expansion in u,v for each coefficient region.

function pt(a){while(a.length>1&&a.at(-1)===0n)a.pop();return a;}
function pa(a,b){return pt(Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||0n)+(b[i]||0n)));}
function pm(a,b){const c=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=a[i]*b[j];return pt(c);}
function ps(a,x){return pt(a.map(v=>v*x));}
function pe(a,x){let v=0n;for(let i=a.length-1;i>=0;i--)v=v*x+a[i];return v;}
function em(items){const m=new Map();for(const [j,s,p]of items)m.set(j+","+s,p.map(BigInt));return m;}
function ea(A,B){const C=new Map(A);for(const [k,v]of B){const c=pa(C.get(k)||[0n],v);if(c.some(x=>x!==0n))C.set(k,c);else C.delete(k);}return C;}
function esc(A,c){return new Map([...A].map(([k,v])=>[k,ps(v,c)]).filter(x=>x[1].some(v=>v!==0n)));}
function es(A,shift){return new Map([...A].map(([k,v])=>{const [j,s]=k.split(",").map(Number);return[j+","+(s+shift),v];}));}
function ep(A,p){return new Map([...A].map(([k,v])=>[k,pm(v,p)]).filter(x=>x[1].some(v=>v!==0n)));}
function et(A){return new Map([...A].map(([k,v])=>{const[j,s]=k.split(",").map(Number);return[k,pm(v,[BigInt(s),BigInt(j)])];}).filter(x=>x[1].some(v=>v!==0n)));}
function ex(A,B){let C=new Map();for(const[k,p]of A)for(const[l,v]of B){const[j,s]=k.split(",").map(Number),[jj,ss]=l.split(",").map(Number);C=ea(C,new Map([[j+jj+","+(s+ss),pm(p,v)]]));}return C;}
const O=em([[0,0,[1]],[0,1,[-1]]]);
function ra(A,B){let x=A.num,y=B.num;for(let k=A.den;k<B.den;k++)x=ex(x,O);for(let k=B.den;k<A.den;k++)y=ex(y,O);return{num:ea(x,y),den:Math.max(A.den,B.den)};}
function rs(A,c){return{num:esc(A.num,c),den:A.den};}
function rp(A,p){return{num:ep(A.num,p),den:A.den};}
function rx(A,B){return{num:ex(A.num,B.num),den:A.den+B.den};}
function rz(A,s){return{num:es(A.num,s),den:A.den};}
function rt(A){return{num:ea(ex(et(A.num),O),esc(es(A.num,1),BigInt(A.den))),den:A.den+1};}
function cb(n,k){if(n<0n)throw Error("negative upper binomial");if(n<BigInt(k))return 0n;let v=1n;for(let j=1;j<=k;j++)v=v*(n-BigInt(j)+1n)/BigInt(j);return v;}
function blockCoeffs(delta,block){
 const deg=delta.den-1+Math.max(...[...delta.num.values()].map(x=>x.length-1));
 const maxShift=Math.max(...[...delta.num.keys()].map(k=>+k.split(",")[1]));
 if(maxShift>delta.den-1)throw Error("binomial polynomial range guard");
 const terms=[...delta.num].map(([k,p])=>{const[j,s]=k.split(",").map(Number);return{j,s,p};}).filter(x=>x.j<=block);
 const value=(u,v)=>{const Q=BigInt(u+v+1),K=BigInt(block)*Q+BigInt(u);return terms.reduce((a,x)=>a+pe(x.p,Q)*cb(K-BigInt(x.j)*Q-BigInt(x.s)+BigInt(delta.den-1),delta.den-1),0n);};
 const grid=Array.from({length:deg+1},(_,u)=>Array.from({length:deg+1},(_,v)=>value(u,v)));
 const first=grid.map(row=>{let w=[...row],a=[];for(let k=0;k<=deg;k++){a.push(w[0]);w=w.slice(1).map((v,j)=>v-w[j]);}return a;});
 const coeff=Array.from({length:deg+1},()=>Array(deg+1).fill(0n));
 for(let b=0;b<=deg;b++){let w=first.map(row=>row[b]);for(let a=0;a<=deg;a++){coeff[a][b]=w[0];w=w.slice(1).map((v,j)=>v-w[j]);}}
 const neg=[];let nonzero=0,pos=0;for(let a=0;a<=deg;a++)for(let b=0;b<=deg;b++){const c=coeff[a][b];if(c){nonzero++;if(c>0n)pos++;else neg.push({a,b,c:c.toString()});}}
 return{deg,block,nonzero,pos,negative:neg,coeff};
}

function rtheta(A,m,c=1n){return ra(rp(A,m),rs(rt(A),c));}
function rT(A){return ra(rx(A,rt(rt(A))),rs(rx(rt(A),rt(A)),-1n));}
function rdet3(a,b,c,d,e,f){return ra(ra(rx(a,ra(rx(d,f),rs(rx(e,e),-1n))),rs(rx(b,ra(rx(b,f),rs(rx(c,e),-1n))),-1n)),rx(c,ra(rx(b,e),rs(rx(c,d),-1n))));}

const TERMS=[{"i": 0, "den": "q", "terms": [[[3, 0, 1, 1, 0, 1, 0, 0, 0], 1], [[2, 2, 0, 1, 0, 1, 0, 0, 0], -1], [[1, 1, 1, 0, 2, 0, 0, 0, 0], -1], [[0, 3, 0, 0, 2, 0, 0, 0, 0], 1]]}, {"i": 1, "den": "q*r", "terms": [[[3, 1, 1, 1, 0, 0, 1, 0, 0], 1], [[2, 3, 0, 1, 0, 0, 1, 0, 0], -1], [[2, 1, 2, 1, 0, 1, 0, 0, 0], 1], [[2, 0, 2, 0, 1, 1, 0, 0, 0], -1], [[1, 2, 1, 0, 1, 1, 0, 0, 0], 1], [[1, 0, 1, 0, 0, 1, 0, 2, 0], -1], [[0, 2, 2, 0, 2, 0, 0, 0, 0], -1], [[0, 1, 0, 1, 0, 0, 0, 0, 2], -1], [[0, 0, 1, 0, 1, 0, 0, 1, 1], -2]]}, {"i": 2, "den": "p*q**2*r", "terms": [[[4, 0, 2, 0, 0, 2, 0, 0, 0], -1], [[3, 3, 1, 1, 0, 0, 1, 0, 0], 1], [[3, 2, 1, 0, 1, 0, 1, 0, 0], 1], [[3, 2, 1, 0, 0, 2, 0, 0, 0], 1], [[2, 4, 0, 0, 1, 0, 1, 0, 0], -1], [[2, 3, 2, 1, 0, 1, 0, 0, 0], 1], [[2, 2, 2, 0, 1, 1, 0, 0, 0], -1], [[2, 2, 0, 0, 0, 0, 1, 2, 0], -1], [[2, 0, 2, 0, 0, 1, 0, 2, 0], -1], [[2, 0, 1, 0, 0, 1, 0, 1, 1], -2], [[0, 4, 2, 0, 2, 0, 0, 0, 0], -1], [[0, 2, 1, 0, 1, 0, 0, 1, 1], -2], [[0, 2, 0, 0, 1, 0, 0, 0, 2], -1], [[0, 0, 0, 0, 0, 0, 0, 2, 2], -1]]}, {"i": 3, "den": "q", "terms": [[[2, 0, 1, 0, 0, 2, 0, 0, 0], -1], [[1, 3, 0, 1, 0, 0, 1, 0, 0], 1], [[1, 2, 0, 0, 1, 0, 1, 0, 0], 1], [[1, 0, 0, 0, 0, 0, 1, 2, 0], -1], [[0, 2, 1, 0, 1, 1, 0, 0, 0], -1], [[0, 0, 0, 0, 0, 1, 0, 1, 1], -2]]}, {"i": 4, "den": "1", "terms": [[[1, 0, 1, 0, 0, 2, 0, 0, 0], -1], [[0, 2, 0, 0, 1, 0, 1, 0, 0], 1]]}];

function pow(A,k){let B={num:em([[0,0,[1]]]),den:0};for(let i=0;i<k;i++)B=rx(B,A);return B;}
function makeDelta0(){
 const W={num:em([[0,0,[1]],[1,0,[-1]]]),den:1};
 const p=rtheta(rtheta(W,[0n,1n],-1n),[1n,1n],-1n);
 const q=rtheta(rtheta(W,[0n,1n],-1n),[1n],1n);
 const r=rtheta(rtheta(W,[1n],1n),[2n],1n);
 const A=rt(rtheta(rtheta(rtheta(W,[0n,1n],-1n),[1n,1n],-1n),[2n,1n],-1n));
 const T0=rT(p),T1=rT(q),T2=rT(r);
 const X=ra(rx(p,rt(q)),rs(rx(q,rt(p)),-2n));
 const Y=ra(ra(rs(rx(rx(p,r),rt(q)),2n),rs(rx(rx(q,r),rt(p)),-1n)),rs(rx(rx(p,q),rt(r)),-1n));
 const v=[p,q,r,A,T0,T1,T2,X,Y];
 return TERMS.map(row=>({i:row.i,den:row.den,value:row.terms.reduce((sum,[exps,c])=>ra(sum,rs(exps.reduce((a,e,j)=>e?rx(a,pow(v[j],e)):a,{num:em([[0,0,[1]]]),den:0}),BigInt(c))),{num:em([]),den:0})}));
}
function makeDelta1(){
 const W={num:em([[0,0,[1]],[1,0,[-1]]]),den:1};
 const V=rt(rtheta(W,[0n,1n],-1n));
 const R=rtheta(rtheta(W,[-1n,1n],-1n),[1n],1n);
 const A=rt(rtheta(rtheta(rtheta(W,[-1n],1n),[0n,1n],-1n),[1n,1n],-1n));
 const T=rT(W),U=rdet3(W,rt(W),rt(rt(W)),rt(rt(W)),rt(rt(rt(W))),rt(rt(rt(rt(W)))));
 const TV=rT(V),TR=rT(R);
 const X=ra(ra(rx(V,T),rs(rx(T,rt(V)),-2n)),rx(V,rt(T)));
 const Y=ra(ra(ra(rs(rx(rx(V,R),rt(T)),2n),rs(rx(rx(T,R),rt(V)),-1n)),rs(rx(rx(V,T),rt(R)),-1n)),rs(rp(rx(rx(V,T),R),[-1n,1n]),-1n));
 const v=[V,T,R,A,TV,U,TR,X,Y],powers=[3,3,4,3,2];
 return TERMS.map(row=>({i:row.i,den:row.den,value:row.terms.reduce((sum,[exps,c])=>{
  const wp=powers[row.i]-exps[1]-exps[5]-exps[7]-exps[8];if(wp<0)throw Error('negative W clearing power');
  let term=exps.reduce((a,e,j)=>e?rx(a,pow(v[j],e)):a,pow(W,wp));return ra(sum,rs(term,BigInt(c)));
 },{num:em([]),den:0})}));
}

const EXPECTED=[[[231, 405, 405, 405, 403, 401, 390, 144], [338, 594, 594, 594, 594, 592, 591, 587, 570, 209], [171, 324, 324, 323, 321, 313, 126]], [[180, 484, 492, 493, 493, 493, 490, 487, 477, 440, 108], [225, 721, 734, 738, 738, 738, 738, 736, 735, 731, 724, 708, 641, 126], [111, 394, 402, 403, 403, 400, 397, 387, 350, 63]]];

function assert(ok,msg){if(!ok)throw Error(msg);}
function dpow(a,k){let c=[1n];for(let i=0;i<k;i++)c=pm(c,a);return c;}
function dt(a){return pt(a.map((v,i)=>v*BigInt(i)));}
function dv(a){let c=Array(2*a.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=i+1;j<a.length;j++)c[i+j]+=a[i]*a[j]*BigInt((j-i)**2);return pt(c);}
function du(a){let c=Array(3*a.length-2).fill(0n);for(let i=0;i<a.length;i++)for(let j=i+1;j<a.length;j++)for(let k=j+1;k<a.length;k++)c[i+j+k]+=a[i]*a[j]*a[k]*BigInt((j-i)**2*(k-i)**2*(k-j)**2);return pt(c);}
function dense(kind,m){
 const Q=BigInt(m+1),q=BigInt(m),W=Array(m+1).fill(1n);let p,v,r,A,T0,T1,T2,X,Y;
 if(kind===0){
  p=W.map((_,k)=>(Q-BigInt(k))*(Q+1n-BigInt(k)));
  v=W.map((_,k)=>BigInt(k+1)*(Q-BigInt(k)));
  r=W.map((_,k)=>BigInt((k+1)*(k+2)));
  A=W.map((_,k)=>BigInt(k)*(Q-BigInt(k))*(Q+1n-BigInt(k))*(Q+2n-BigInt(k)));
  T0=dv(p);T1=dv(v);T2=dv(r);
  X=pa(pm(p,dt(v)),ps(pm(v,dt(p)),-2n));
  Y=pa(pa(ps(pm(pm(p,r),dt(v)),2n),ps(pm(pm(v,r),dt(p)),-1n)),ps(pm(pm(p,v),dt(r)),-1n));
 }else{
  p=W.map((_,k)=>BigInt(k)*(Q-BigInt(k)));
  r=W.map((_,k)=>(q-BigInt(k))*BigInt(k+1));v=dv(W);
  A=W.map((_,k)=>BigInt(k*(k-1))*(Q-BigInt(k))*(Q+1n-BigInt(k)));
  T0=dv(p);T1=du(W);T2=dv(r);
  X=pa(pa(pm(p,v),ps(pm(v,dt(p)),-2n)),pm(p,dt(v)));
  Y=pa(pa(pa(ps(pm(pm(p,r),dt(v)),2n),ps(pm(pm(v,r),dt(p)),-1n)),ps(pm(pm(p,v),dt(r)),-1n)),ps(pm(pm(p,v),r),-q));
 }
 const inputs=[p,v,r,A,T0,T1,T2,X,Y],powers=[3,3,4,3,2];
 return TERMS.map(row=>row.terms.reduce((sum,[exps,c])=>{
  const wp=kind?powers[row.i]-exps[1]-exps[5]-exps[7]-exps[8]:0;
  let term=exps.reduce((a,e,j)=>e?pm(a,dpow(inputs[j],e)):a,dpow(W,wp));return pa(sum,ps(term,BigInt(c)));
 },[0n]));
}
function sparseNumerator(A,Q){let a=[0n];for(const[k,p]of A.num){const[j,s]=k.split(',').map(Number),i=j*Q+s;assert(i>=0,'negative exponent');while(a.length<=i)a.push(0n);a[i]+=pe(p,BigInt(Q));}return pt(a);}
const data=[makeDelta0(),makeDelta1()],denExpected=[[28,34,25],[31,38,28]],degrees=[[43,53,38],[44,55,40]],blocks=[[8,10,7],[11,14,10]];
const rows=[];let positiveTotal=0;
for(let kind=0;kind<2;kind++){
 for(const m of (kind?[2,3,5]:[1,2,5])){
  const dd=dense(kind,m);
  for(let i=1;i<=3;i++){
   const A=data[kind][i].value,x=pm(dd[i],dpow([1n,-1n],A.den)),y=sparseNumerator(A,m+1);
   assert(x.length===y.length&&x.every((v,j)=>v===y[j]),'independent dense numerator mismatch kind='+kind+',m='+m+',i='+i);
   assert(dd[i].length-1<=blocks[kind][i-1]*m-1,'degree bound');
  }
 }
 for(let i=1;i<=3;i++){
  const A=data[kind][i].value,shifts=[...A.num.keys()].map(k=>+k.split(',')[1]);
  assert(A.den===denExpected[kind][i-1],'denominator exponent');
  assert(Math.min(...shifts)>=0&&Math.max(...shifts)<=A.den-1,'binomial polynomial guard');
  const degree=A.den-1+Math.max(...[...A.num.values()].map(p=>p.length-1));assert(degree===degrees[kind][i-1],'prior degree');
  for(let j=0;j<blocks[kind][i-1];j++){
   const b=blockCoeffs(A,j);assert(b.negative.length===0,'negative Newton coefficient');assert(b.pos===EXPECTED[kind][i-1][j],'count mismatch');
   rows.push({delta:kind,wPower:i,region:j,priorDegree:b.deg,positive:b.pos});positiveTotal+=b.pos;
  }
 }
}
assert(positiveTotal===26929,'total positive coefficient count');
console.log(JSON.stringify({status:'PASS',positiveTotal,negativeTotal:0,delta0Positive:9949,delta1Positive:16980,independentDenseM:[[1,2,5],[2,3,5]],rows},null,2));
