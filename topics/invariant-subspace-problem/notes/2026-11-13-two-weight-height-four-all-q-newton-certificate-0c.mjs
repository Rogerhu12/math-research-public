// Exact all-q certificate for the two-weight height-four primitive Gram bounds.
// Run: node 2026-11-13-two-weight-height-four-all-q-newton-certificate-0c.mjs
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
function h4SparseBalanced(C1=[3n,4n],C2=[2n,3n]){
 const W={num:em([[0,0,[1]],[1,0,[-1]]]),den:1},tw=rt(W),t2w=rt(tw),t3w=rt(t2w),t4w=rt(t3w);
 const T=rT(W),U=rdet3(W,tw,t2w,t2w,t3w,t4w);
 const V=rtheta(tw,[0n,1n],-1n);
 const R=rtheta(ra(tw,W),[-1n,1n],-1n);
 let A0=rt(rtheta(W,[-1n],1n));A0=rtheta(A0,[0n,1n],-1n);A0=rtheta(A0,[1n,1n],-1n);
 const TV=rT(V),TR=rT(R);
 const left1=rx(rx(rx(V,V),A0),U),right1=rx(rx(TV,TV),T);
 const left2=rx(rx(rx(T,T),TV),TR),right2=rx(rx(rx(U,U),V),R);
 const delta1=ra(rs(left1,C1[0]),rs(right1,-C1[1]));
 const delta2=ra(rs(left2,C2[0]),rs(right2,-C2[1]));
 return {W,V,R,T,U,A0,TV,TR,left1,right1,left2,right2,delta1,delta2};
}
function h4SparseDiff2(C1=[3n,4n],C2=[2n,3n]){
 const W={num:em([[0,0,[1]],[1,0,[-1]]]),den:1};
 const W1=rtheta(rtheta(W,[1n,1n],-1n),[0n,1n],-1n);
 const W2=rtheta(rtheta(W,[0n,1n],-1n),[1n],1n);
 const W3=rtheta(rtheta(W,[2n],1n),[1n],1n);
 const A0=rt(rtheta(rtheta(rtheta(W,[2n,1n],-1n),[1n,1n],-1n),[0n,1n],-1n));
 const T1=rT(W1),T2=rT(W2),T3=rT(W3);
 const left1=rx(rx(rx(W1,W1),A0),T2),right1=rx(rx(T1,T1),W2);
 const left2=rx(rx(rx(W2,W2),T1),T3),right2=rx(rx(rx(T2,T2),W1),W3);
 return {W1,W2,W3,A0,T1,T2,T3,left1,right1,left2,right2,delta1:ra(rs(left1,C1[0]),rs(right1,-C1[1])),delta2:ra(rs(left2,C2[0]),rs(right2,-C2[1]))};
}

function assert(ok,msg){if(!ok)throw Error(msg);}
function denseScale(a,c){return pt(a.map(x=>x*c));}
function denseAdd(a,b){return pa(a,b);}
function denseMul(a,b){return pm(a,b);}
function denseTheta(a){return a.map((v,i)=>v*BigInt(i));}
function denseVariance(w){const a=Array(2*w.length-1).fill(0n);for(let i=0;i<w.length;i++)for(let j=i+1;j<w.length;j++)a[i+j]+=w[i]*w[j]*BigInt((j-i)**2);return pt(a);}
function denseTriple(w){const a=Array(3*w.length-2).fill(0n);for(let i=0;i<w.length;i++)for(let j=i+1;j<w.length;j++)for(let k=j+1;k<w.length;k++)a[i+j+k]+=w[i]*w[j]*w[k]*BigInt((j-i)**2*(k-i)**2*(k-j)**2);return pt(a);}
function densePower(a,k){let r=[1n];for(let i=0;i<k;i++)r=pm(r,a);return r;}
function denseBalanced(q){
 const Q=BigInt(q+1),W=Array(q+1).fill(1n);
 const V=W.map((_,r)=>BigInt(r)*(Q-BigInt(r))),R=W.map((_,r)=>(Q-1n-BigInt(r))*BigInt(r+1));
 const A0=W.map((_,r)=>BigInt(r)*BigInt(r-1)*(Q-BigInt(r))*(Q+1n-BigInt(r)));
 const T=denseVariance(W),U=denseTriple(W),TV=denseVariance(V),TR=denseVariance(R);
 const d1=pa(ps(pm(pm(pm(V,V),A0),U),3n),ps(pm(pm(TV,TV),T),-4n));
 const d2=pa(ps(pm(pm(pm(T,T),TV),TR),2n),ps(pm(pm(pm(U,U),V),R),-3n));
 return{delta1:d1,delta2:d2};
}
function denseDiff2(q){
 const Q=BigInt(q+1),W=Array(q+1).fill(1n);
 const W1=W.map((_,r)=>(Q-BigInt(r))*(Q+1n-BigInt(r)));
 const W2=W.map((_,r)=>BigInt(r+1)*(Q-BigInt(r)));
 const W3=W.map((_,r)=>BigInt(r+1)*BigInt(r+2));
 const A0=W.map((_,r)=>BigInt(r)*(Q-BigInt(r))*(Q+1n-BigInt(r))*(Q+2n-BigInt(r)));
 const T1=denseVariance(W1),T2=denseVariance(W2),T3=denseVariance(W3);
 return{delta1:pa(ps(pm(pm(pm(W1,W1),A0),T2),3n),ps(pm(pm(T1,T1),W2),-4n)),
 delta2:pa(ps(pm(pm(pm(W2,W2),T1),T3),2n),ps(pm(pm(pm(T2,T2),W1),W3),-3n))};
}
function sparseNumerator(A,Q){let a=[0n];for(const[k,p]of A.num){const[j,s]=k.split(",").map(Number),i=j*Q+s;while(a.length<=i)a.push(0n);a[i]+=pe(p,BigInt(Q));}return pt(a);}
function exactDenseCheck(A,dense,q){
 const x=pt(pm(dense,densePower([1n,-1n],A.den))),y=sparseNumerator(A,q+1);
 assert(x.length===y.length&&x.every((v,i)=>v===y[i]),"independent dense numerator mismatch q="+q);
}
function runCertificate(){
 const expected={
  balanced:{delta1:[55,198,206,205,194,50],delta2:[80,291,297,296,293,286,258,45]},
  diff2:{delta1:[125,189,188,184,50],delta2:[105,252,251,249,241,75]}
 };
 const tables={},rows=[];let positiveTotal=0;
 for(const kind of ["balanced","diff2"]){
  const data=kind==="balanced"?h4SparseBalanced():h4SparseDiff2();tables[kind]=data;
  for(const name of ["delta1","delta2"]){
   const A=data[name],ex=expected[kind][name];
   const maxShift=Math.max(...[...A.num.keys()].map(k=>+k.split(",")[1]));
   const qDegree=Math.max(...[...A.num.values()].map(p=>p.length-1));
   assert(maxShift<=A.den-1,"negative-binomial guard");
   for(let j=0;j<ex.length;j++){
    const b=blockCoeffs(A,j);assert(b.negative.length===0,"negative Newton coefficient");
    assert(b.pos===ex[j],"positive count mismatch");
    const nz=b.coeff.flat().filter(x=>x>0n);let minimum=nz[0];for(const v of nz)if(v<minimum)minimum=v;
    rows.push({kind,name,block:j,priorDegree:b.deg,positive:b.pos,minimum:minimum.toString()});positiveTotal+=b.pos;
   }
   for(const q of (kind==="balanced"?[2,3,4,7]:[1,2,3,7])){
    const dense=kind==="balanced"?denseBalanced(q):denseDiff2(q);exactDenseCheck(A,dense[name],q);
   }
  }
 }
 assert(positiveTotal===4663,"total");
 for(const q of [2,3,4,7]){
  const p=BigInt(q),d=denseBalanced(q);
  assert(d.delta1[7]===8n*p*p*(p-1n)*(p+2n),"balanced strict anchor 1");
  assert(d.delta2[6]===8n*p*p*(p-1n)*(p-1n),"balanced strict anchor 2");
 }
 for(const q of [1,2,3,7]){
  const p=BigInt(q),d=denseDiff2(q);
  assert(d.delta1[2]===2n*p*p*(p+1n)**4n*(p+2n)**2n*(p+4n),"diff2 strict anchor 1");
  assert(d.delta2[2]===24n*p*(p+1n)**3n*(p+2n),"diff2 strict anchor 2");
 }
 return{status:"PASS",positiveTotal,negativeTotal:0,rows};
}

console.log(JSON.stringify(runCertificate(),null,2));
