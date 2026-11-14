/* Exact all-q certificate for the height-three two-weight primitive Gram theorem.
 * Only standard JavaScript and BigInt. Run: node this-file.mjs
 * No numerical eigenvalues, random probes, external dependencies or sampled-q extrapolation.
 *
 * Q=q+1, theta=z d/dz.
 * WL=(Q-(Q+1)z+z^(Q+1))/(1-z)^2,
 * WR=(1-(Q+1)z^Q+Qz^(Q+1))/(1-z)^2,
 * A=(theta+1)(Q-1-theta)WL,
 * T(W)=W theta^2 W-(theta W)^2,
 * Delta=z A T(WR) WL^2-2 T(WL)^2 WR.
 *
 * Sparse numerator keys (j,s) mean z^(jQ+s); each value is a polynomial in Q.
 * Exact multiplication and differentiation produce denominator (1-z)^14.
 * Coefficients in five integer regions are polynomials of total degree <=20.
 * Their complete Newton expansions on (u,v)>=0 have 377 positive entries.
 */

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
function h3Sparse(){
 const L={num:em([[0,0,[0,1]],[0,1,[-1,-1]],[1,1,[1]]]),den:2};
 const R={num:em([[0,0,[1]],[1,0,[-1,-1]],[1,1,[0,1]]]),den:2};
 const tl=ra(rx(L,rt(rt(L))),rs(rx(rt(L),rt(L)),-1n));
 const tr=ra(rx(R,rt(rt(R))),rs(rx(rt(R),rt(R)),-1n));
 const pre=ra(rp(L,[-1n,1n]),rs(rt(L),-1n));
 const A=ra(rt(pre),pre);
 const delta=ra(rz(rx(rx(A,tr),rx(L,L)),1),rs(rx(rx(tl,tl),R),-2n));
 return{delta,L,R,A,tl,tr};
}
function h3BlockCoeffs(delta,block){
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

function h3Dense(q,cnum=1n,cden=2n){
 const WL=Array.from({length:q+1},(_,r)=>BigInt(q+1-r));
 const WR=Array.from({length:q+1},(_,r)=>BigInt(r+1));
 const A=Array.from({length:q},(_,r)=>BigInt((r+1)*(q-r)*(q+1-r)));
 const TL=Array(2*q).fill(0n),TR=Array(2*q).fill(0n);
 for(let r=0;r<=q;r++)for(let s=r+1;s<=q;s++){
  const d=BigInt((s-r)*(s-r));
  TL[r+s]+=WL[r]*WL[s]*d;TR[r+s]+=WR[r]*WR[s]*d;
 }
 const left=pm([0n,...A],pm(TR,pm(WL,WL)));
 const right=pm(pm(TL,TL),WR);
 return pa(ps(left,cnum),ps(right,-cden));
}
function verifyHeightThree(){
 const assert=(ok,msg)=>{if(!ok)throw Error(msg);};
 const {delta}=h3Sparse();
 assert(delta.den===14,"common denominator 14");
 assert(delta.num.size===37,"37 sparse numerator terms");
 const maxQDegree=Math.max(...[...delta.num.values()].map(p=>p.length-1));
 const maxOffset=Math.max(...[...delta.num.keys()].map(k=>+k.split(",")[1]));
 assert(maxQDegree===7&&maxOffset===9,"independent polynomial degree and offset guards");
 // The true finite polynomial has degree <=5q-1=5Q-6.
 // For k=jQ+u, j=0,...,4, and Q=u+v+1, u,v>=0:
 // only exponents lambda Q+s with lambda<=j can contribute.
 // The excluded negative lags with lambda<=j are >=-9; hence
 // binom(lag+13,13) is the correct polynomial also at those lags.
 const expected=[42,103,103,99,30],mins=["12","8","4","24","12"];
 const summary=[];
 for(let j=0;j<5;j++){
  const z=h3BlockCoeffs(delta,j);
  assert(z.deg===20,"degree bound 7+13, independent of interpolation values");
  assert(z.negative.length===0,"all Newton coefficients nonnegative");
  assert(z.nonzero===expected[j],"support size");
  let minimum=null,maxTotal=0;
  for(let a=0;a<=20;a++)for(let b=0;b<=20;b++){
   const c=z.coeff[a][b];
   if(c>0n){minimum=minimum===null||c<minimum?c:minimum;maxTotal=Math.max(maxTotal,a+b);}
  }
  assert(String(minimum)===mins[j],"minimum positive coefficient");
  assert(maxTotal===13,"observed exact support degree");
  summary.push({block:j,positive:z.nonzero,minimum:String(minimum),degree_bound:20,max_total_degree:maxTotal});
 }
 // Independent dense construction checks the sparse rational arithmetic
 // at small and generic q. These checks are not the all-q proof:
 // the all-q proof is the degree bound plus the full Newton coefficients.
 for(const q of [1,2,3,7]){
  const dense=h3Dense(q);
  let factor=[1n];for(let j=0;j<14;j++)factor=pm(factor,[1n,-1n]);
  const numerator=pm(dense,factor),Q=BigInt(q+1);
  let collapsed=[0n];
  for(const[key,p]of delta.num){
   const[j,s]=key.split(",").map(Number),e=j*(q+1)+s,v=pe(p,Q);
   while(collapsed.length<=e)collapsed.push(0n);collapsed[e]+=v;
  }
  assert(pa(numerator,ps(collapsed,-1n)).every(v=>v===0n),"dense/sparse identity");
  assert(dense[2]===2n*BigInt(q)*BigInt(q+1)**2n,"strict z^2 coefficient");
 }
 // The two small penultimate blocks needed in the final sharp theorem.
 const d2=h3Dense(2,1n,3n);
 const fact2=pm([0n,0n,0n,8n],pm([1n,-2n,1n],[27n,72n,70n,24n,3n]));
 assert(pa(d2,ps(fact2,-1n)).every(v=>v===0n),"q=2 factorization");
 const d3=h3Dense(3,4n,9n);
 assert(d3.every(v=>v>=0n)&&d3[2]===240n,"q=3 coefficient positivity");
 assert(summary.reduce((a,x)=>a+x.positive,0)===377,"total positive certificate entries");
 return {status:"PASS",denominator:14,sparse_terms:37,max_Q_degree:7,max_offset:9,
         Newton_blocks:summary,total_positive:377,strict_coefficient:"2q(q+1)^2",
         small_blocks:{q2:"8 z^3 (z-1)^2 (27+72z+70z^2+24z^3+3z^4)",q3:"all coefficients nonnegative; z^2 coefficient 240"},
         conclusion:"Every common-head q/(q+1) height-three penultimate block has both adjacent ratios <1/2. The q=2 and q=3 refinements support the full sharp two-weight theorem."};
}
console.log(JSON.stringify(verifyHeightThree(),null,2));
