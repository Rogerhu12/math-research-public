// Exact all-q certificate for height two: two equal-weight groups and one exceptional site.
// Run: node isp-two-groups-one-bit-1949-h2-certificate.mjs
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
const zero=()=>({num:em([]),den:0}),one=()=>({num:em([[0,0,[1]]]),den:0});
function wa(A,B){return Array.from({length:Math.max(A.length,B.length)},(_,i)=>ra(A[i]||zero(),B[i]||zero()));}
function ws(A,c){return A.map(v=>rs(v,c));}
function wx(A,B){let C=Array.from({length:A.length+B.length-1},zero);for(let i=0;i<A.length;i++)for(let j=0;j<B.length;j++)C[i+j]=ra(C[i+j],rx(A[i],B[j]));return C;}
function ma(A,B){return A.map((row,i)=>row.map((v,j)=>wa(v,B[i][j])));}
function mx(A,B){return A.map(row=>B[0].map((_,j)=>row.reduce((c,v,k)=>wa(c,wx(v,B[k][j])),[])));}
function adj(A){return [[A[1][1],ws(A[0][1],-1n)],[ws(A[1][0],-1n),A[0][0]]];}
function make(){
 const W={num:em([[0,0,[1]],[1,0,[-1]]]),den:1};
 const L=rtheta(W,[0n,1n],-1n),R=rtheta(W,[1n],1n);
 const l1=rt(L),l2=rt(l1),r1=rt(R),r2=rt(r1);
 const A=rt(rtheta(rtheta(W,[0n,1n],-1n),[1n,1n],-1n));
 const C=rtheta(rtheta(rtheta(W,[-1n,1n],-1n),[1n],1n),[2n],1n);
 const TL=rT(L),TR=rT(R);
 const M=ra(ra(rx(L,r2),rx(R,l2)),rs(rx(l1,r1),-2n));
 const J=ra(rx(L,r1),rs(rx(R,l1),-1n));
 const V11=ra(ra(r2,rp(r1,[2n,-2n])),rp(R,[1n,-2n,1n]));
 const V12=ra(rp(R,[-1n,1n]),rs(r1,-1n));
 const U=[[[A,l2],[zero(),l1]],[[zero(),l1],[zero(),L]]];
 const V=[[[V11,C],[V12]],[[V12],[R]]];
 const B=[[[TL,M,TR],[zero(),J]],[[zero(),J],[zero(),rx(L,R)]]];
 const T=mx(mx(mx(adj(U),B),adj(V)),B),trace=wa(T[0][0],T[1][1]);
 if(trace[0].num.size)throw Error('trace has nonzero constant');
 const Z=[L,R],detUoverw=[rx(A,L),TL],detV=[TR,rx(C,R)];
 const Vv=[rx(R,TL),rx(L,TR)];
 const red=wa(wa(wx(wx(Z,Z),wx(detUoverw,detV)),[zero(),...wx(Vv,Vv)]),ws(trace.slice(1),-1n));
 if(red.slice(5).some(v=>v.num.size))throw Error('not quartic');
 return{red:red.slice(0,5),L,R,A,C,TL,TR};
}

function assert(ok,msg){if(!ok)throw Error(msg);}
function dpow(a,k){let v=[1n];for(let i=0;i<k;i++)v=pm(v,a);return v;}
function dtheta(a){return pt(a.map((v,i)=>v*BigInt(i)));}
function dwa(A,B){return Array.from({length:Math.max(A.length,B.length)},(_,i)=>pa(A[i]||[0n],B[i]||[0n]));}
function dws(A,c){return A.map(v=>ps(v,c));}
function dwx(A,B){let C=Array.from({length:A.length+B.length-1},()=>[0n]);for(let i=0;i<A.length;i++)for(let j=0;j<B.length;j++)C[i+j]=pa(C[i+j],pm(A[i],B[j]));return C;}
function dmx(A,B){return A.map(row=>B[0].map((_,j)=>row.reduce((c,v,k)=>dwa(c,dwx(v,B[k][j])),[])));}
function dadj(A){return [[A[1][1],dws(A[0][1],-1n)],[dws(A[1][0],-1n),A[0][0]]];}
function direct(q){
 const p=BigInt(q),Q=p+1n;
 const L=Array.from({length:q+1},(_,r)=>Q-BigInt(r)),R=Array.from({length:q+1},(_,r)=>BigInt(r+1));
 const A=L.map((_,r)=>BigInt(r)*(Q-BigInt(r))*(Q+1n-BigInt(r)));
 const C=L.map((_,r)=>(p-BigInt(r))*BigInt((r+1)*(r+2)));
 const l1=dtheta(L),l2=dtheta(l1),r1=dtheta(R),r2=dtheta(r1);
 const TL=pa(pm(L,l2),ps(pm(l1,l1),-1n)),TR=pa(pm(R,r2),ps(pm(r1,r1),-1n));
 const M=pa(pa(pm(L,r2),pm(R,l2)),ps(pm(l1,r1),-2n));
 const J=pa(pm(L,r1),ps(pm(R,l1),-1n));
 const V11=pa(pa(r2,ps(r1,-2n*p)),ps(R,p*p)),V12=pa(ps(R,p),ps(r1,-1n));
 const U=[[[A,l2],[[0n],l1]],[[[0n],l1],[[0n],L]]];
 const V=[[[V11,C],[V12]],[[V12],[R]]];
 const B=[[[TL,M,TR],[[0n],J]],[[[0n],J],[[0n],pm(L,R)]]];
 const T=dmx(dmx(dmx(dadj(U),B),dadj(V)),B),trace=dwa(T[0][0],T[1][1]);
 assert(trace[0].every(v=>v===0n),'dense trace constant');
 const Z=[L,R],du=[pm(A,L),TL],dv=[TR,pm(C,R)],vv=[pm(R,TL),pm(L,TR)];
 return dwa(dwa(dwx(dwx(Z,Z),dwx(du,dv)),[[0n],...dwx(vv,vv)]),dws(trace.slice(1),-1n)).slice(0,5);
}
function sparseNumerator(A,Q){let a=[0n];for(const[k,p]of A.num){const[j,s]=k.split(',').map(Number),i=j*Q+s;assert(i>=0,'negative exponent');while(a.length<=i)a.push(0n);a[i]+=pe(p,BigInt(Q));}return pt(a);}
function anchor(A,k){let C=[0n];for(const[key,p]of A.num){const[j,s]=key.split(',').map(Number);if(j===0&&s<=k)C=pa(C,ps(p,cb(BigInt(k-s+A.den-1),A.den-1)));}return C;}
function check(){
 const expected=[[69,135,135,133,127,34],[84,135,135,133,127,40],[75,135,135,133,127,45],[65,135,135,133,127,49],[54,135,134,132,124,39]];
 const degrees=[23,24,25,24,23],data=make(),rows=[];let total=0;
 for(const q of [1,2,3,7]){
  const dense=direct(q);
  for(let i=0;i<5;i++){
   const p=data.red[i],x=pm(dense[i],dpow([1n,-1n],p.den)),y=sparseNumerator(p,q+1);
   assert(x.length===y.length&&x.every((v,j)=>v===y[j]),'independent dense numerator mismatch q='+q+', i='+i);
   assert(dense[i].length-1<=6*q-1,'dense degree guard');
  }
 }
 for(let i=0;i<5;i++){
  const p=data.red[i],shifts=[...p.num.keys()].map(k=>+k.split(',')[1]);
  assert(p.den===16,'denominator exponent');
  assert(Math.min(...shifts)>=0&&Math.max(...shifts)<=15,'binomial polynomial range guard');
  const degree=p.den-1+Math.max(...[...p.num.values()].map(v=>v.length-1));
  assert(degree===degrees[i],'prior degree');
  for(let j=0;j<6;j++){
   const c=blockCoeffs(p,j);assert(c.negative.length===0,'negative Newton coefficient');
   assert(c.pos===expected[i][j],'positive-count mismatch');
   const positive=c.coeff.flat().filter(v=>v>0n);let minimum=positive[0];for(const v of positive)if(v<minimum)minimum=v;
   rows.push({wPower:i,region:j,priorDegree:c.deg,positive:c.pos,minimum:minimum.toString()});total+=c.pos;
  }
 }
 const a=anchor(data.red[4],1),wanted=[0n,2n,-4n,2n];
 assert(a.length===wanted.length&&a.every((v,i)=>v===wanted[i]),'strict anchor: 2Q(Q-1)^2');
 assert(total===3199,'total positive coefficient count');
 console.log(JSON.stringify({status:'PASS',positiveTotal:total,negativeTotal:0,strictAnchor:'[w^4 z]R=2q^2(q+1)',independentDenseQ:[1,2,3,7],rows},null,2));
}
check();
