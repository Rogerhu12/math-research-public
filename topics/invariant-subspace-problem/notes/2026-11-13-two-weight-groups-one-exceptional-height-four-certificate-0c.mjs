// Exact all-q certificate for height four: two equal-weight groups and one exceptional site.
// Run: node 2026-11-13-two-weight-groups-one-exceptional-height-four-certificate-0c.mjs
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
function ex(A,B){
 const aa=[...A].map(([k,p])=>{const[j,s]=k.split(',').map(Number);return[j,s,p];});
 const bb=[...B].map(([k,p])=>{const[j,s]=k.split(',').map(Number);return[j,s,p];});
 const C=new Map();
 for(const[j,s,p]of aa)for(const[jj,ss,v]of bb){
  const key=(j+jj)+','+(s+ss),sum=pa(C.get(key)||[0n],pm(p,v));
  if(sum.some(x=>x!==0n))C.set(key,sum);else C.delete(key);
 }
 return C;
}
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
 const maxShift=Math.max(...[...delta.num.keys()].map(k=>+k.split(',')[1]));
 if(maxShift>delta.den-1)throw Error('binomial polynomial range guard');
 const K=delta.den-1,Qmax=2*deg+1,Nmax=block*Qmax+deg+K;
 const bin=Array(Nmax+1).fill(0n);if(Nmax>=K)bin[K]=1n;
 for(let n=K+1;n<=Nmax;n++)bin[n]=bin[n-1]*BigInt(n)/BigInt(n-K);
 const terms=[...delta.num].map(([key,p])=>{const[j,s]=key.split(',').map(Number);return{j,s,p};}).filter(x=>x.j<=block).map(x=>({...x,values:Array.from({length:Qmax+1},(_,q)=>pe(x.p,BigInt(q)))}));
 const grid=Array.from({length:deg+1},(_,u)=>Array.from({length:deg+1},(_,v)=>{
  const Q=u+v+1;let sum=0n;for(const x of terms){const n=(block-x.j)*Q+u-x.s+K;if(n<0||n>Nmax)throw Error('cached binomial guard');sum+=x.values[Q]*bin[n];}return sum;
 }));
 const first=grid.map(row=>{let w=[...row],a=[];for(let k=0;k<=deg;k++){a.push(w[0]);w=w.slice(1).map((v,j)=>v-w[j]);}return a;});
 const coeff=Array.from({length:deg+1},()=>Array(deg+1).fill(0n));
 for(let b=0;b<=deg;b++){let w=first.map(row=>row[b]);for(let a=0;a<=deg;a++){coeff[a][b]=w[0];w=w.slice(1).map((v,j)=>v-w[j]);}}
 const neg=[];let nonzero=0,pos=0;for(let a=0;a<=deg;a++)for(let b=0;b<=deg;b++){const c=coeff[a][b];if(c){nonzero++;if(c>0n)pos++;else neg.push({a,b,c:c.toString()});}}
 return{deg,block,nonzero,pos,negative:neg,coeff};
}

function rtheta(A,m,c=1n){return ra(rp(A,m),rs(rt(A),c));}
function rT(A){return ra(rx(A,rt(rt(A))),rs(rx(rt(A),rt(A)),-1n));}
function rdet3(a,b,c,d,e,f){return ra(ra(rx(a,ra(rx(d,f),rs(rx(e,e),-1n))),rs(rx(b,ra(rx(b,f),rs(rx(c,e),-1n))),-1n)),rx(c,ra(rx(b,e),rs(rx(c,d),-1n))));}


const BTERMS=[{"i": 0, "den": "q", "terms": [[[3, 0, 1, 1, 0, 1, 0, 0, 0], 1], [[2, 2, 0, 1, 0, 1, 0, 0, 0], -1], [[1, 1, 1, 0, 2, 0, 0, 0, 0], -1], [[0, 3, 0, 0, 2, 0, 0, 0, 0], 1]]}, {"i": 1, "den": "q*r", "terms": [[[3, 1, 1, 1, 0, 0, 1, 0, 0], 1], [[2, 3, 0, 1, 0, 0, 1, 0, 0], -1], [[2, 1, 2, 1, 0, 1, 0, 0, 0], 1], [[2, 0, 2, 0, 1, 1, 0, 0, 0], -1], [[1, 2, 1, 0, 1, 1, 0, 0, 0], 1], [[1, 0, 1, 0, 0, 1, 0, 2, 0], -1], [[0, 2, 2, 0, 2, 0, 0, 0, 0], -1], [[0, 1, 0, 1, 0, 0, 0, 0, 2], -1], [[0, 0, 1, 0, 1, 0, 0, 1, 1], -2]]}, {"i": 2, "den": "p*q**2*r", "terms": [[[4, 0, 2, 0, 0, 2, 0, 0, 0], -1], [[3, 3, 1, 1, 0, 0, 1, 0, 0], 1], [[3, 2, 1, 0, 1, 0, 1, 0, 0], 1], [[3, 2, 1, 0, 0, 2, 0, 0, 0], 1], [[2, 4, 0, 0, 1, 0, 1, 0, 0], -1], [[2, 3, 2, 1, 0, 1, 0, 0, 0], 1], [[2, 2, 2, 0, 1, 1, 0, 0, 0], -1], [[2, 2, 0, 0, 0, 0, 1, 2, 0], -1], [[2, 0, 2, 0, 0, 1, 0, 2, 0], -1], [[2, 0, 1, 0, 0, 1, 0, 1, 1], -2], [[0, 4, 2, 0, 2, 0, 0, 0, 0], -1], [[0, 2, 1, 0, 1, 0, 0, 1, 1], -2], [[0, 2, 0, 0, 1, 0, 0, 0, 2], -1], [[0, 0, 0, 0, 0, 0, 0, 2, 2], -1]]}, {"i": 3, "den": "q", "terms": [[[2, 0, 1, 0, 0, 2, 0, 0, 0], -1], [[1, 3, 0, 1, 0, 0, 1, 0, 0], 1], [[1, 2, 0, 0, 1, 0, 1, 0, 0], 1], [[1, 0, 0, 0, 0, 0, 1, 2, 0], -1], [[0, 2, 1, 0, 1, 1, 0, 0, 0], -1], [[0, 0, 0, 0, 0, 1, 0, 1, 1], -2]]}, {"i": 4, "den": "1", "terms": [[[1, 0, 1, 0, 0, 2, 0, 0, 0], -1], [[0, 2, 0, 0, 1, 0, 1, 0, 0], 1]]}];
const CTERMS=[{"i": 0, "den": "r", "terms": [[[1, 1, 1, 1, 0, 2, 0, 0, 0, 0], -1], [[1, 0, 3, 0, 0, 2, 0, 0, 0, 0], 1], [[0, 3, 0, 1, 1, 0, 1, 0, 0, 0], 1], [[0, 2, 2, 0, 1, 0, 1, 0, 0, 0], -1]]}, {"i": 1, "den": "p*r*t", "terms": [[[2, 2, 0, 2, 0, 1, 1, 0, 0, 0], -1], [[2, 1, 2, 1, 0, 1, 1, 0, 0, 0], 1], [[2, 0, 2, 2, 0, 2, 0, 0, 0, 0], -1], [[1, 3, 1, 1, 1, 0, 0, 1, 0, 0], 1], [[1, 2, 3, 0, 1, 0, 0, 1, 0, 0], -1], [[1, 2, 1, 2, 1, 0, 1, 0, 0, 0], 1], [[1, 1, 3, 1, 0, 2, 0, 0, 0, 0], 1], [[1, 0, 1, 0, 1, 0, 0, 0, 0, 2], -1], [[1, 0, 0, 1, 0, 1, 0, 0, 1, 1], -2], [[0, 3, 2, 1, 1, 0, 1, 0, 0, 0], -1], [[0, 1, 0, 1, 0, 0, 1, 0, 2, 0], -1]]}, {"i": 2, "den": "p*q*r**2*t", "terms": [[[2, 4, 0, 2, 0, 0, 2, 0, 0, 0], -1], [[2, 3, 2, 1, 0, 1, 0, 1, 0, 0], 1], [[2, 3, 2, 1, 0, 0, 2, 0, 0, 0], 1], [[2, 2, 4, 0, 0, 1, 0, 1, 0, 0], -1], [[2, 2, 2, 2, 0, 1, 1, 0, 0, 0], -1], [[2, 0, 4, 2, 0, 2, 0, 0, 0, 0], -1], [[2, 0, 2, 0, 0, 1, 0, 0, 0, 2], -1], [[1, 3, 3, 1, 1, 0, 0, 1, 0, 0], 1], [[1, 3, 3, 1, 0, 1, 1, 0, 0, 0], 1], [[1, 2, 3, 2, 1, 0, 1, 0, 0, 0], 1], [[1, 2, 3, 2, 0, 2, 0, 0, 0, 0], 1], [[1, 2, 0, 1, 0, 0, 1, 0, 1, 1], -2], [[1, 0, 2, 1, 0, 1, 0, 0, 1, 1], -2], [[0, 4, 4, 0, 1, 0, 0, 1, 0, 0], -1], [[0, 4, 2, 2, 1, 0, 1, 0, 0, 0], -1], [[0, 2, 2, 0, 1, 0, 0, 0, 0, 2], -1], [[0, 2, 2, 0, 0, 0, 0, 1, 2, 0], -1], [[0, 2, 0, 2, 0, 0, 1, 0, 2, 0], -1], [[0, 0, 0, 0, 0, 0, 0, 0, 2, 2], -1]]}, {"i": 3, "den": "p*r*t", "terms": [[[2, 2, 0, 2, 0, 0, 2, 0, 0, 0], -1], [[2, 1, 2, 1, 0, 1, 0, 1, 0, 0], 1], [[2, 0, 2, 2, 0, 1, 1, 0, 0, 0], -1], [[1, 3, 1, 1, 0, 0, 2, 0, 0, 0], 1], [[1, 2, 3, 0, 0, 1, 0, 1, 0, 0], -1], [[1, 2, 1, 2, 0, 1, 1, 0, 0, 0], 1], [[1, 1, 3, 1, 1, 0, 0, 1, 0, 0], 1], [[1, 0, 1, 0, 0, 1, 0, 0, 0, 2], -1], [[1, 0, 0, 1, 0, 0, 1, 0, 1, 1], -2], [[0, 3, 2, 1, 1, 0, 0, 1, 0, 0], -1], [[0, 1, 0, 1, 0, 0, 0, 1, 2, 0], -1]]}, {"i": 4, "den": "r", "terms": [[[1, 1, 1, 1, 0, 0, 2, 0, 0, 0], -1], [[1, 0, 3, 0, 0, 1, 0, 1, 0, 0], 1], [[0, 3, 0, 1, 0, 0, 2, 0, 0, 0], 1], [[0, 2, 2, 0, 0, 1, 0, 1, 0, 0], -1]]}];
function pow(A,k){let B={num:em([[0,0,[1]]]),den:0};for(let i=0;i<k;i++)B=rx(B,A);return B;}
function makeCase0(){
 const W={num:em([[0,0,[1]],[1,0,[-1]]]),den:1};
 const p=rtheta(rtheta(rtheta(W,[0n,1n],-1n),[1n,1n],-1n),[2n,1n],-1n);
 const q=rtheta(rtheta(rtheta(W,[0n,1n],-1n),[1n,1n],-1n),[1n],1n);
 const r=rtheta(rtheta(rtheta(W,[1n],1n),[2n],1n),[0n,1n],-1n);
 const A=rt(rtheta(rtheta(rtheta(rtheta(W,[0n,1n],-1n),[1n,1n],-1n),[2n,1n],-1n),[3n,1n],-1n));
 const T0=rT(p),T1=rT(q),T2=rT(r);
 const X=ra(rx(p,rt(q)),rs(rx(q,rt(p)),-2n));
 const Y=ra(ra(rs(rx(rx(p,r),rt(q)),2n),rs(rx(rx(q,r),rt(p)),-1n)),rs(rx(rx(p,q),rt(r)),-1n));
 const v=[p,q,r,A,T0,T1,T2,X,Y];
 return BTERMS.map(row=>({i:row.i,den:row.den,value:row.terms.reduce((sum,[exps,c])=>ra(sum,rs(exps.reduce((a,e,j)=>e?rx(a,pow(v[j],e)):a,{num:em([[0,0,[1]]]),den:0}),BigInt(c))),{num:em([]),den:0})}));
}

function makeCase1(){
 const W={num:em([[0,0,[1]],[1,0,[-1]]]),den:1};
 const p=rtheta(rtheta(rtheta(W,[0n,1n],-1n),[1n,1n],-1n),[2n,1n],-1n);
 const q=rtheta(rtheta(rtheta(W,[0n,1n],-1n),[1n,1n],-1n),[1n],1n);
 const r=rtheta(rtheta(rtheta(W,[1n],1n),[2n],1n),[0n,1n],-1n);
 const t=rtheta(rtheta(rtheta(W,[1n],1n),[2n],1n),[3n],1n);
 const A=rT(p),B=rT(q),C=rT(r),D=rT(t);
 const X=ra(ra(rx(rx(q,r),rt(p)),rs(rx(rx(p,r),rt(q)),-2n)),rx(rx(p,q),rt(r)));
 const Y=ra(ra(rs(rx(rx(q,t),rt(r)),2n),rs(rx(rx(r,t),rt(q)),-1n)),rs(rx(rx(q,r),rt(t)),-1n));
 const v=[p,q,r,t,A,B,C,D,X,Y];
 return CTERMS.map(row=>({i:row.i,den:row.den,value:row.terms.reduce((sum,[exps,c])=>ra(sum,rs(exps.reduce((a,e,j)=>e?rx(a,pow(v[j],e)):a,{num:em([[0,0,[1]]]),den:0}),BigInt(c))),{num:em([]),den:0})}));
}


function makeCase2(){
 const W={num:em([[0,0,[1]],[1,0,[-1]]]),den:1};
 const F0=rtheta(W,[0n,1n],-1n),F1=rtheta(W,[1n],1n);
 const V=rt(rtheta(rtheta(W,[0n,1n],-1n),[1n,1n],-1n));
 const A=rt(rtheta(rtheta(rtheta(rtheta(W,[-1n],1n),[0n,1n],-1n),[1n,1n],-1n),[2n,1n],-1n));
 const T0=rT(F0),T1=rT(F1),TV=rT(V);
 const hankel3=f=>rdet3(f,rt(f),rt(rt(f)),rt(rt(f)),rt(rt(rt(f))),rt(rt(rt(rt(f)))));
 const U0=hankel3(F0),U1=hankel3(F1);
 const X=ra(ra(rx(V,T0),rs(rx(T0,rt(V)),-2n)),rx(V,rt(T0)));
 const Y=ra(ra(rs(rx(rx(V,T1),rt(T0)),2n),rs(rx(rx(T0,T1),rt(V)),-1n)),rs(rx(rx(V,T0),rt(T1)),-1n));
 const v=[V,T0,T1,A,TV,U0,U1,X,Y],pows0=[3,3,4,3,2],pows1=[2,2,2,1,1];
 return BTERMS.map(row=>({i:row.i,den:row.den,value:row.terms.reduce((sum,[exps,c])=>{
  const e0=pows0[row.i]-exps[1]-exps[5]-exps[7]-exps[8],e1=pows1[row.i]-exps[2]-exps[6]-exps[8];
  if(e0<0||e1<0)throw Error('negative clearing power i='+row.i);
  let term=exps.reduce((a,e,j)=>e?rx(a,pow(v[j],e)):a,rx(pow(F0,e0),pow(F1,e1)));return ra(sum,rs(term,BigInt(c)));
 },{num:em([]),den:0})}));
}

function makeCase3(){
 const W={num:em([[0,0,[1]],[1,0,[-1]]]),den:1};
 const F0=rtheta(W,[0n,1n],-1n),F1=rtheta(W,[1n],1n);
 const V=rt(rtheta(rtheta(W,[0n,1n],-1n),[1n,1n],-1n));
 const R=rtheta(rtheta(rtheta(W,[-1n,1n],-1n),[1n],1n),[2n],1n);
 const T0=rT(F0),T1=rT(F1),TV=rT(V),TR=rT(R);
 const hankel3=f=>rdet3(f,rt(f),rt(rt(f)),rt(rt(f)),rt(rt(rt(f))),rt(rt(rt(rt(f)))));
 const U0=hankel3(F0),U1=hankel3(F1);
 const X=ra(ra(rx(rx(T0,T1),rt(V)),rs(rx(rx(V,T1),rt(T0)),-2n)),rx(rx(V,T0),rt(T1)));
 const Y=ra(ra(ra(rs(rx(rx(T0,R),rt(T1)),2n),rs(rx(rx(T1,R),rt(T0)),-1n)),rs(rx(rx(T0,T1),rt(R)),-1n)),rs(rp(rx(rx(T0,T1),R),[-1n,1n]),-1n));
 const v=[V,T0,T1,R,TV,U0,U1,TR,X,Y],powers=[0,3,4,3,0];
 const powerTable=(f,k)=>{const out=[{num:em([[0,0,[1]]]),den:0}];for(let j=1;j<=k;j++)out.push(rx(out[j-1],f));return out;};
 const active=CTERMS.filter(row=>row.i>=1&&row.i<=3);
 const vp=v.map((f,j)=>powerTable(f,Math.max(...active.flatMap(row=>row.terms.map(([e])=>e[j]))))),fp0=powerTable(F0,4),fp1=powerTable(F1,4);
 return CTERMS.map(row=>{
  if(row.i===0||row.i===4)return {i:row.i,den:row.den,value:{num:em([]),den:0}};
  return {i:row.i,den:row.den,value:row.terms.reduce((sum,[exps,c])=>{
   const e0=powers[row.i]-exps[1]-exps[5]-exps[8]-exps[9],e1=powers[row.i]-exps[2]-exps[6]-exps[8]-exps[9];
   if(e0<0||e1<0)throw Error('negative clearing power');
   let term=exps.reduce((a,e,j)=>e?rx(a,vp[j][e]):a,rx(fp0[e0],fp1[e1]));return ra(sum,rs(term,BigInt(c)));
  },{num:em([]),den:0})};
 });
}


const META=[{"delta": 0, "kind": "boundary", "positive": 16737, "rows": [{"i": 1, "den": 36, "terms": 165, "maxShift": 28, "degree": 57, "regions": 8, "positive": 4660, "expected": [475, 665, 665, 665, 663, 661, 650, 216]}, {"i": 2, "den": 44, "terms": 246, "maxShift": 34, "degree": 69, "regions": 10, "positive": 8908, "expected": [713, 989, 989, 989, 989, 987, 986, 982, 965, 319]}, {"i": 3, "den": 32, "terms": 126, "maxShift": 24, "degree": 49, "regions": 7, "positive": 3169, "expected": [360, 527, 527, 526, 524, 516, 189]}]}, {"delta": 0, "kind": "central", "positive": 32705, "rows": [{"i": 1, "den": 44, "terms": 254, "maxShift": 33, "degree": 70, "regions": 10, "positive": 8835, "expected": [578, 989, 989, 989, 988, 987, 985, 980, 960, 390]}, {"i": 2, "den": 52, "terms": 355, "maxShift": 39, "degree": 83, "regions": 12, "positive": 15053, "expected": [779, 1377, 1377, 1377, 1377, 1376, 1375, 1374, 1371, 1364, 1336, 570]}, {"i": 3, "den": 44, "terms": 254, "maxShift": 33, "degree": 70, "regions": 10, "positive": 8817, "expected": [525, 989, 989, 989, 988, 987, 985, 980, 960, 425]}]}, {"delta": 1, "kind": "boundary", "positive": 43094, "rows": [{"i": 1, "den": 46, "terms": 279, "maxShift": 31, "degree": 69, "regions": 13, "positive": 12402, "expected": [413, 1056, 1073, 1077, 1078, 1078, 1078, 1076, 1074, 1069, 1057, 1009, 264]}, {"i": 2, "den": 56, "terms": 411, "maxShift": 38, "degree": 85, "regions": 16, "positive": 22998, "expected": [612, 1560, 1584, 1590, 1593, 1593, 1593, 1593, 1592, 1590, 1588, 1584, 1576, 1556, 1475, 319]}, {"i": 3, "den": 40, "terms": 200, "maxShift": 27, "degree": 60, "regions": 11, "positive": 7694, "expected": [306, 800, 813, 817, 817, 816, 814, 809, 799, 756, 147]}]}, {"delta": 1, "kind": "central", "positive": 89151, "rows": [{"i": 1, "den": 56, "terms": 410, "maxShift": 35, "degree": 84, "regions": 16, "positive": 23039, "expected": [632, 1576, 1589, 1593, 1593, 1593, 1593, 1593, 1590, 1590, 1586, 1582, 1572, 1548, 1452, 357]}, {"i": 2, "den": 68, "terms": 619, "maxShift": 42, "degree": 103, "regions": 20, "positive": 43103, "expected": [833, 2316, 2336, 2341, 2343, 2343, 2343, 2343, 2343, 2343, 2340, 2340, 2338, 2336, 2331, 2323, 2309, 2271, 2121, 510]}, {"i": 3, "den": 56, "terms": 410, "maxShift": 34, "degree": 84, "regions": 16, "positive": 23009, "expected": [567, 1576, 1589, 1593, 1593, 1593, 1593, 1593, 1590, 1590, 1586, 1582, 1572, 1548, 1452, 392]}]}];

function assert(ok,msg){if(!ok)throw Error(msg);}
function dpow(a,k){let c=[1n];for(let i=0;i<k;i++)c=pm(c,a);return c;}
function dt(a){return pt(a.map((v,i)=>v*BigInt(i)));}
function dv(a){let c=Array(2*a.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=i+1;j<a.length;j++)c[i+j]+=a[i]*a[j]*BigInt((j-i)**2);return pt(c);}
function du(a){let c=Array(3*a.length-2).fill(0n);for(let i=0;i<a.length;i++)for(let j=i+1;j<a.length;j++)for(let k=j+1;k<a.length;k++)c[i+j+k]+=a[i]*a[j]*a[k]*BigInt((j-i)**2*(k-i)**2*(k-j)**2);return pt(c);}
function clearing(index,i,e){
 if(index<2)return [0,0];
 const pc=[0,3,4,3,0];
 if(index===2){const pr=[0,2,2,1,0];return[pc[i]-e[1]-e[5]-e[7]-e[8],pr[i]-e[2]-e[6]-e[8]];}
 return[pc[i]-e[1]-e[5]-e[8]-e[9],pc[i]-e[2]-e[6]-e[8]-e[9]];
}
const DEGREE_INPUTS=[
 [[1,0],[1,0],[1,0],[1,0],[2,1],[2,1],[2,1],[2,0],[3,1]],
 [[1,0],[1,0],[1,0],[1,0],[2,1],[2,1],[2,1],[2,1],[3,1],[3,1]],
 [[1,0],[2,1],[2,1],[1,0],[2,1],[3,3],[3,3],[3,1],[5,2]],
 [[1,0],[2,1],[2,1],[1,1],[2,1],[3,3],[3,3],[2,3],[5,2],[5,3]]
];
function symbolicDegreeCheck(index){
 const terms=index%2===0?BTERMS:CTERMS;
 for(const row of terms.filter(v=>v.i>=1&&v.i<=3))for(const[e]of row.terms){
  const[u,v]=clearing(index,row.i,e);assert(u>=0&&v>=0,'negative clearing power');
  let slope=u+v,loss=0;for(let j=0;j<e.length;j++){slope+=e[j]*DEGREE_INPUTS[index][j][0];loss+=e[j]*DEGREE_INPUTS[index][j][1];}
  const bound=META[index].rows[row.i-1].regions;
  assert(slope<bound||(slope===bound&&loss>=1),'prior z-degree bound');
 }
}
function dense(index,m){
 const Q=BigInt(m+1),mm=BigInt(m),W=Array(m+1).fill(1n);let inputs,F0=[1n],F1=[1n];
 if(index<2){
  const ph=Array.from({length:4},(_,j)=>W.map((_,k)=>{const r=BigInt(k);let c=1n;for(let i=1;i<=j;i++)c*=r+BigInt(i);for(let i=0;i<3-j;i++)c*=Q+BigInt(i)-r;return c;}));
  if(index===0){
   const[p,q,r]=ph,A=W.map((_,k)=>{let c=BigInt(k);for(let j=0;j<4;j++)c*=Q+BigInt(j-k);return c;});
   const X=pa(pm(p,dt(q)),ps(pm(q,dt(p)),-2n));
   const Y=pa(pa(ps(pm(pm(p,r),dt(q)),2n),ps(pm(pm(q,r),dt(p)),-1n)),ps(pm(pm(p,q),dt(r)),-1n));
   inputs=[p,q,r,A,dv(p),dv(q),dv(r),X,Y];
  }else{
   const[p,q,r,t]=ph;
   const X=pa(pa(pm(pm(q,r),dt(p)),ps(pm(pm(p,r),dt(q)),-2n)),pm(pm(p,q),dt(r)));
   const Y=pa(pa(ps(pm(pm(q,t),dt(r)),2n),ps(pm(pm(r,t),dt(q)),-1n)),ps(pm(pm(q,r),dt(t)),-1n));
   inputs=[p,q,r,t,dv(p),dv(q),dv(r),dv(t),X,Y];
  }
 }else{
  F0=W.map((_,k)=>Q-BigInt(k));F1=W.map((_,k)=>BigInt(k+1));
  const V=W.map((_,k)=>BigInt(k)*(Q-BigInt(k))*(Q+1n-BigInt(k)));
  const R=W.map((_,k)=>(mm-BigInt(k))*BigInt((k+1)*(k+2)));
  const A=W.map((_,k)=>BigInt(k*(k-1))*(Q-BigInt(k))*(Q+1n-BigInt(k))*(Q+2n-BigInt(k)));
  const T0=dv(F0),T1=dv(F1),U0=du(F0),U1=du(F1);
  if(index===2){
   const X=pa(pa(pm(V,T0),ps(pm(T0,dt(V)),-2n)),pm(V,dt(T0)));
   const Y=pa(pa(ps(pm(pm(V,T1),dt(T0)),2n),ps(pm(pm(T0,T1),dt(V)),-1n)),ps(pm(pm(V,T0),dt(T1)),-1n));
   inputs=[V,T0,T1,A,dv(V),U0,U1,X,Y];
  }else{
   const X=pa(pa(pm(pm(T0,T1),dt(V)),ps(pm(pm(V,T1),dt(T0)),-2n)),pm(pm(V,T0),dt(T1)));
   const Y=pa(pa(pa(ps(pm(pm(T0,R),dt(T1)),2n),ps(pm(pm(T1,R),dt(T0)),-1n)),ps(pm(pm(T0,T1),dt(R)),-1n)),ps(pm(pm(T0,T1),R),-mm));
   inputs=[V,T0,T1,R,dv(V),U0,U1,dv(R),X,Y];
  }
 }
 const terms=index%2===0?BTERMS:CTERMS;
 return terms.map(row=>row.i===0||row.i===4?[0n]:row.terms.reduce((sum,[exps,c])=>{
  const[e0,e1]=clearing(index,row.i,exps);let term=pm(dpow(F0,e0),dpow(F1,e1));
  for(let j=0;j<exps.length;j++)if(exps[j])term=pm(term,dpow(inputs[j],exps[j]));return pa(sum,ps(term,BigInt(c)));
 },[0n]));
}
function sparseNumerator(A,Q){let a=[0n];for(const[k,p]of A.num){const[j,s]=k.split(',').map(Number),i=j*Q+s;assert(i>=0,'negative exponent');while(a.length<=i)a.push(0n);a[i]+=pe(p,BigInt(Q));}return pt(a);}
const makers=[makeCase0,makeCase1,makeCase2,makeCase3],rows=[];let positiveTotal=0;
for(let index=0;index<4;index++){
 symbolicDegreeCheck(index);const data=makers[index]();
 for(const m of(index<2?[1,3]:[2,3])){
  const dd=dense(index,m);
  for(let i=1;i<=3;i++){
   const A=data[i].value,x=pm(dd[i],dpow([1n,-1n],A.den)),y=sparseNumerator(A,m+1);
   assert(x.length===y.length&&x.every((v,j)=>v===y[j]),'independent dense numerator mismatch case='+index+',m='+m+',i='+i);
  }
 }
 let subtotal=0;
 for(let i=1;i<=3;i++){
  const A=data[i].value,meta=META[index].rows[i-1],shifts=[...A.num.keys()].map(k=>+k.split(',')[1]);
  assert(A.den===meta.den,'denominator exponent');assert(Math.min(...shifts)>=0&&Math.max(...shifts)<=A.den-1,'binomial polynomial guard');
  const prior=A.den-1+Math.max(...[...A.num.values()].map(p=>p.length-1));assert(prior===meta.degree,'prior coefficient degree');
  for(let j=0;j<meta.regions;j++){
   const b=blockCoeffs(A,j);assert(b.negative.length===0,'negative Newton coefficient');assert(b.pos===meta.expected[j],'positive count mismatch');
   rows.push({delta:META[index].delta,kind:META[index].kind,wPower:i,region:j,priorDegree:b.deg,positive:b.pos});subtotal+=b.pos;
  }
 }
 assert(subtotal===META[index].positive,'branch positive total');positiveTotal+=subtotal;
}
assert(positiveTotal===181687,'total positive coefficient count');
console.log(JSON.stringify({status:'PASS',positiveTotal,negativeTotal:0,branchPositive:[16737,32705,43094,89151],independentDenseM:[[1,3],[1,3],[2,3],[2,3]],rows},null,2));
