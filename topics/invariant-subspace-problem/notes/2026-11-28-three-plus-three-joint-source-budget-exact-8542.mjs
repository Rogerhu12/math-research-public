// Exact original physical Gram inverses and same-source joint budgets.
// Coefficients are ascending powers of t; all arithmetic is BigInt over Z[t].
// Run: node --input-type=module -e 'import("./this-file.mjs").then(m=>console.log(m.verifyThreePlusThreeJointSources()))'


const trim=a=>{while(a.length>1&&a.at(-1)===0n)a.pop();return a;},Z=[0n],O=[1n],t=[0n,1n];
const add=(a,b)=>trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||0n)+(b[i]||0n)));
const sc=(a,c)=>trim(a.map(x=>x*c));
const mul=(a,b)=>{const r=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)r[i+j]+=a[i]*b[j];return trim(r);};
const pow=(a,n)=>{let r=O;while(n--)r=mul(r,a);return r;};
const neg=a=>sc(a,-1n),sub=(a,b)=>add(a,neg(b)),iszero=a=>a.length===1&&a[0]===0n;
function igcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let r=a%b;a=b;b=r;}return a;}
function content(a){return a.reduce((g,x)=>igcd(g,x),0n);}
function primitive(a){a=trim(a.slice());if(iszero(a))return a;let c=content(a);if(a.at(-1)<0n)c=-c;return a.map(x=>x/c);}
function prem(a,b){a=a.slice();while(!iszero(a)&&a.length>=b.length){const k=a.length-b.length,ca=a.at(-1),cb=b.at(-1);a=sub(sc(a,cb),Array(k).fill(0n).concat(sc(b,ca)));if(!iszero(a))a=primitive(a);}return a;}
function pgcd(a,b){a=primitive(a);b=primitive(b);while(!iszero(b)){const r=prem(a,b);a=b;b=r;}return primitive(a);}
function exact(a,b){a=a.slice();const q=Array(Math.max(1,a.length-b.length+1)).fill(0n);while(!iszero(a)&&a.length>=b.length){const k=a.length-b.length;if(a.at(-1)%b.at(-1))throw Error("nonexact leading division");const c=a.at(-1)/b.at(-1);q[k]=c;a=sub(a,Array(k).fill(0n).concat(sc(b,c)));}if(!iszero(a))throw Error("nonexact remainder");return trim(q);}
function rat(n,d=O){if(iszero(d))throw Error("zero denominator");if(iszero(n))return {n:Z,d:O};const g=pgcd(n,d);n=exact(n,g);d=exact(d,g);let c=igcd(content(n),content(d));if(d.at(-1)<0n)c=-c;return {n:n.map(x=>x/c),d:d.map(x=>x/c)};}
const rm=(a,b)=>rat(mul(a.n,b.n),mul(a.d,b.d)),ri=a=>rat(a.d,a.n),rs=(a,c)=>rat(sc(a.n,c),a.d);
const ra=(a,b)=>rat(add(mul(a.n,b.d),mul(b.n,a.d)),mul(a.d,b.d)),rsub=(a,b)=>ra(a,rs(b,-1n));
const rp=(a,n)=>{let r=rat(O);while(n--)r=rm(r,a);return r;};
function binom(n,k){if(k<0||k>n)return 0n;let a=1n;for(let i=1;i<=k;i++)a=a*BigInt(n-i+1)/BigInt(i);return a;}
const mm=(a,b)=>a.map(row=>b[0].map((_,j)=>row.reduce((s,x,k)=>add(s,mul(x,b[k][j])),Z)));
function det(a){if(a.length===1)return a[0][0];let r=Z;for(let j=0;j<a.length;j++)r=add(r,sc(mul(a[0][j],det(a.slice(1).map(row=>row.filter((_,k)=>k!==j)))),j%2?-1n:1n));return r;}
function adj(a){const n=a.length;if(n===1)return [[O]];return a.map((_,i)=>a.map((_,j)=>sc(det(a.filter((_,r)=>r!==j).map(row=>row.filter((_,c)=>c!==i))),(i+j)%2?-1n:1n)));}
function gram(p,q,ell,j){
 const rows=Array.from({length:Math.min(p,ell)-Math.max(0,ell-q)+1},(_,x)=>x+Math.max(0,ell-q));
 const cols=Array.from({length:Math.min(p,ell+j)-Math.max(0,ell+j-q)+1},(_,x)=>x+Math.max(0,ell+j-q));
 const D=rows.map(r=>cols.map(i=>{const k=i-r;return k<0||k>j?Z:sc(pow(t,k),binom(p-r,k)*binom(q-ell+r,j-k));}));
 const Ds=cols.map(i=>rows.map(r=>[binom(i,r)*binom(ell+j-i,ell-r)]));
 return {F:mm(D,Ds),rows,D,Ds};
}
function gamma(p,q,ell,j,g){
 const {F,rows}=gram(p,q,ell,j),A=adj(F),d=det(F);
 const weight=rows.map(i=>sc(pow(t,i),binom(p,i)*binom(q,ell-i)));
 let norm=Z,num=Z;
 for(let i=0;i<g.length;i++){norm=add(norm,mul(weight[i],mul(g[i],g[i])));for(let k=0;k<g.length;k++)num=add(num,mul(weight[i],mul(g[i],mul(A[i][k],g[k]))));}
 return rat(num,mul(d,norm));
}
function ser(r){return {numerator:r.n.map(String),denominator:r.d.map(String)};}

function same(a,b,label) {
  if (!iszero(sub(mul(a.n,b.d),mul(b.n,a.d)))) throw Error(label);
}
function positive(p,label,allowLeadingZeros=false) {
  if (p.some(x=>x<0n) || !p.some(x=>x>0n)) throw Error(label);
  if (!allowLeadingZeros && p.some(x=>x===0n)) throw Error(label+" zero coefficient");
}
export function verifyThreePlusThreeJointSources() {
  const began=Date.now();
  const low=[t,[-1n]], upper=[sc(pow(t,2),3n),sc(t,-2n),[3n]];
  const L=[null,...[1,2,3].map(j=>gamma(3,3,1,j,low))];
  const G=[null,...[1,2].map(j=>gamma(3,3,2,j,upper))];
  const a=[1n,3n,1n], b=[1n,8n,1n], c=[3n,4n,3n];
  const d=[1n,4n,10n,4n,1n], v=[1n,0n,1n], q=mul([1n,1n],c);
  const h=sub(sc(mul(a,v),3n),mul(t,b)), j=add(sc(mul(a,v),3n),mul(t,b));
  const f=sub(mul(pow(q,2),pow(v,2)),mul(t,pow(d,2)));
  [rat(a,q),rat(b,sc(d,3n)),rat(a,mul(t,q))]
    .forEach((x,k)=>same(x,L[k+1],"full lower inverse "+k));
  same(G[1],rat(d,mul(q,v)),"full upper first inverse");
  same(G[2],rat(O,t),"full upper second inverse");
  const BB=rat(sc(mul(mul(t,[1n,1n]),pow([-1n,1n],2)),12n),c);
  const C1=ri(G[1]),F=rsub(rp(C1,2),ri(G[2]));
  same(F,rat(f,pow(d,2)),"F");
  const Delta=rsub(rm(C1,L[3]),L[2]);
  const S1=rm(rat(O,[4n]),rm(BB,rm(rp(Delta,2),ri(L[3]))));
  const sourceA=ra(rm(C1,L[2]),rm(rp(L[2],2),ri(L[3])));
  const K=rm(rat(O,[4n]),rm(BB,rm(G[1],rp(sourceA,2))));
  const S2=ra(K,rm(rp(L[1],2),ri(L[2])));
  same(S1,rat(mul(pow([-1n,0n,1n],2),pow(h,2)),sc(mul(a,pow(d,2)),3n)),"same S1");
  same(K,rat(mul(mul(mul(t,pow([-1n,0n,1n],2)),pow(b,2)),pow(j,2)),
    sc(mul(mul(v,pow(a,2)),pow(d,3)),27n)),"both S2 crosses");

  // These three checks pay the entire positive-parameter domain.
  const fGap=sub(mul(pow(q,2),pow(v,2)),sc(mul(t,pow(d,2)),4n));
  const fQuotient=exact(fGap,pow([-1n,1n],2));
  positive(fQuotient,"F >= 3 C1^2/4");
  const s1Gap=sub(mul(a,f),mul(pow([-1n,0n,1n],2),pow(h,2)));
  const s1Quotient=exact(s1Gap,t);
  positive(s1Quotient,"S1 < F/3");
  const halfGap=rsub(rat(O,[2n]),S2);
  positive(halfGap.n,"S2 < 1/2 numerator");
  positive(halfGap.d,"S2 < 1/2 denominator");
  // Verify a single explicit unreduced positive denominator, retaining both crosses.
  const fullDen=sc(mul(mul(mul(mul(v,pow(a,2)),pow(d,3)),b),pow(q,2)),54n);
  const fullNum=sub(sub(sc(mul(mul(mul(mul(v,pow(a,2)),pow(d,3)),b),pow(q,2)),27n),
    sc(mul(mul(mul(mul(t,pow([-1n,0n,1n],2)),pow(b,3)),pow(j,2)),pow(q,2)),2n)),
    sc(mul(mul(v,pow(a,4)),pow(d,4)),162n));
  same(halfGap,rat(fullNum,fullDen),"S2 common denominator");
  positive(fullNum,"unreduced S2 positive coefficients");
  // Assertions contain no floating arithmetic or sampled parameter values.
  return {status:"proved",full_gram_sizes:[2,2,2,3,3],
    f_gap_positive_quotient_terms:fQuotient.length,
    s1_gap_positive_quotient_terms:s1Quotient.length,
    s2_gap_positive_terms:fullNum.length,
    s2_gap_degree:fullNum.length-1,elapsed_ms:Date.now()-began};
}
