// Exact universal coefficient certificate for the two-head primitive Gram inequality.
// Variables are a,b,x=n-1,y=M-n-1. All coefficients are BigInt.
// This checks identities in Z[a,b,x,y], not numerical samples.
function verifyTwoHeadPrimitiveGram() {
  const BASE = 64;
  const strides = [1, BASE, BASE**2, BASE**3];
  const constant = c => ({terms: new Map(c ? [[0, BigInt(c)]] : []), degree: [0,0,0,0]});
  const variable = j => ({terms: new Map([[strides[j], 1n]]), degree: strides.map((_,i)=>+(i===j))});
  function add(p,q) {
    const terms = new Map(p.terms);
    for (const [k,v] of q.terms) {
      const c=(terms.get(k)||0n)+v;
      if(c) terms.set(k,c); else terms.delete(k);
    }
    return {terms,degree:p.degree.map((v,i)=>Math.max(v,q.degree[i]))};
  }
  function scale(p,c) {
    c=BigInt(c);
    return {terms:new Map([...p.terms].map(([k,v])=>[k,v*c]).filter(([,v])=>v)),
      degree:p.degree.slice()};
  }
  const sub=(p,q)=>add(p,scale(q,-1n));
  function mul(p,q) {
    const degree=p.degree.map((v,i)=>v+q.degree[i]);
    if(degree.some(v=>v>=BASE)) throw Error("monomial encoding overflow");
    const terms=new Map();
    for(const [k,v] of p.terms) for(const [l,w] of q.terms) {
      const key=k+l,c=(terms.get(key)||0n)+v*w;
      if(c) terms.set(key,c); else terms.delete(key);
    }
    return {terms,degree};
  }
  const square=p=>mul(p,p);
  const one=constant(1n),zero=constant(0n);
  const a=variable(0),b=variable(1),x=variable(2),y=variable(3);
  const aa=square(a),bb=square(b),ab=mul(a,b),P=mul(aa,bb),S=add(aa,bb);
  const n=add(one,x),d=add(one,y);
  function data(k,l) {
    const kp=add(k,one),lp=add(l,one),base=mul(l,lp);
    const diag=t=>mul(add(l,mul(kp,t)),add(lp,mul(k,t)));
    const off=mul(ab,add(add(k,l),one));
    const N=[[diag(aa),off],[off,diag(bb)]];
    const D=add(add(base,mul(mul(k,l),S)),mul(mul(k,kp),P));
    const E=add(add(base,mul(mul(kp,lp),S)),mul(mul(k,kp),P));
    return {N,D,E};
  }
  function matrixMul(A,B) {
    return A.map((row,i)=>B[0].map((_,j)=>
      row.reduce((v,_,k)=>add(v,mul(A[i][k],B[k][j])),zero)));
  }
  const matrixScale=(A,p)=>A.map(row=>row.map(v=>mul(v,p)));
  const matrixSub=(A,B)=>A.map((row,i)=>row.map((v,j)=>sub(v,B[i][j])));
  const adj=A=>[[A[1][1],scale(A[0][1],-1n)],[scale(A[1][0],-1n),A[0][0]]];
  const det=A=>sub(mul(A[0][0],A[1][1]),mul(A[0][1],A[1][0]));
  function zeroIdentity(p,label) {
    if(p.terms.size!==0) throw Error("nonzero identity: "+label);
  }
  const previous=data(sub(n,one),add(d,one));
  const current=data(n,d);
  const next=data(add(n,one),sub(d,one));
  for(const [name,z] of [["previous",previous],["current",current],["next",next]])
    zeroIdentity(sub(det(z.N),mul(z.D,z.E)),name+" det N = D E");
  const Knum=mul(square(add(n,one)),add(d,one));
  const Kden=mul(mul(n,add(n,constant(2n))),d);
  const leftScalar=mul(mul(Knum,next.E),square(current.D));
  const rightScalar=mul(Kden,previous.D);
  const sandwich=matrixMul(matrixMul(current.N,adj(next.N)),current.N);
  const Delta=matrixSub(matrixScale(previous.N,leftScalar),matrixScale(sandwich,rightScalar));
  zeroIdentity(sub(Delta[0][1],Delta[1][0]),"Delta symmetric");
  const determinant=det(Delta);
  function positiveCoefficients(p,label) {
    for(const [,v] of p.terms) if(v<=0n) throw Error("nonpositive coefficient: "+label);
    return p.terms.size;
  }
  const counts={
    firstDiagonal:positiveCoefficients(Delta[0][0],"Delta11"),
    secondDiagonal:positiveCoefficients(Delta[1][1],"Delta22"),
    determinant:positiveCoefficients(determinant,"det Delta")
  };
  function coefficient(p,exponents) {
    const key=exponents.reduce((sum,e,i)=>sum+e*strides[i],0);
    return p.terms.get(key)||0n;
  }
  const strict=[
    [Delta[0][0],[2,0,0,0],576n],
    [Delta[0][0],[0,2,0,0],360n],
    [determinant,[4,0,0,0],207360n],
    [determinant,[2,2,0,0],414720n],
    [determinant,[0,4,0,0],207360n]
  ];
  for(const [p,e,v] of strict)
    if(coefficient(p,e)!==v) throw Error("wrong strict coefficient "+e);
  if(counts.firstDiagonal!==831 || counts.secondDiagonal!==831 ||
      counts.determinant!==9826) throw Error("unexpected support size");
  return {
    status:"PASS: exact polynomial identities and coefficient positivity",
    ring:"Z[a,b,x,y], x=n-1>=0, y=M-n-1>=0",
    counts,
    strictFirstDiagonal:"576 a^2 + 360 b^2",
    strictDeterminant:"207360 (a^2+b^2)^2",
    scope:"S_M-fixed two-dimensional primitive subspace only"
  };
}
const certificate=verifyTwoHeadPrimitiveGram();
if(typeof console!=="undefined") console.log(JSON.stringify(certificate,null,2));
