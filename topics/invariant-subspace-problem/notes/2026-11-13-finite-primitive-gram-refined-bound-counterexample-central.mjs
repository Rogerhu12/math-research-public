// Exact finite Boolean counterexample to the refined primitive-Gram bound.
// No floating arithmetic is used for any matrix or inequality.
function verifyCounterexample() {
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;};
  class Q {
    constructor(n,d=1n) { if(!d) throw Error("zero denominator"); if(d<0n){n=-n;d=-d;} const g=gcd(n,d);this.n=n/g;this.d=d/g; }
    add(v){return new Q(this.n*v.d+v.n*this.d,this.d*v.d);}
    sub(v){return this.add(v.neg());}
    neg(){return new Q(-this.n,this.d);}
    mul(v){return new Q(this.n*v.n,this.d*v.d);}
    div(v){return new Q(this.n*v.d,this.d*v.n);}
    str(){return this.d===1n?String(this.n):String(this.n)+"/"+String(this.d);}
  }
  const fail=(condition,message)=>{if(!condition)throw Error(message);};
  const a=[3n,3n,3n,3n,3n,1n,1n],basis=[];
  for(let i=0;i<7;i++)for(let j=i+1;j<7;j++)basis.push([i,j]);
  const type=S=>S.filter(i=>i<5).length;
  const representatives=[0,1,2].map(r=>basis.find(S=>type(S)===r));
  const counts=[1n,10n,10n],f=[90n,-6n,1n];
  fail(12n*f[2]+2n*f[1]===0n,"strong-site deletion");
  fail(15n*f[1]+f[0]===0n,"weak-site deletion");
  const norm=f.reduce((sum,x,i)=>sum+counts[i]*x*x,0n);
  fail(norm===8470n,"norm");
  const expected=[
    [[45n,30n,0n],[3n,74n,12n],[0n,12n,83n]],
    [[810n,1080n,90n],[108n,1602n,498n],[9n,498n,1621n]],
    [[7290n,14580n,2430n],[1458n,14580n,6318n],[243n,6318n,10287n]]
  ];
  const inverseImages=[
    [new Q(514n,243n),new Q(-14n,81n),new Q(1n,27n)],
    [new Q(94n,729n),new Q(-10n,729n),new Q(1n,243n)],
    [new Q(38n,2187n),new Q(-2n,729n),new Q(1n,729n)]
  ];
  const gamma=[];
  for(let k=1;k<=3;k++){
    const M=Array.from({length:3},()=>[0n,0n,0n]);
    for(let i=0;i<3;i++)for(const T of basis){
      const R=representatives[i],union=new Set([...R,...T]),delta=union.size-2;
      if(delta>k)continue;
      let factor=1n;
      for(const j of R)if(!T.includes(j))factor*=a[j];
      for(const j of T)if(!R.includes(j))factor*=a[j];
      const e=Array(k-delta+1).fill(0n);e[0]=1n;
      for(let j=0;j<7;j++)if(!union.has(j))
        for(let t=e.length-1;t>=1;t--)e[t]+=a[j]*a[j]*e[t-1];
      M[i][type(T)]+=factor*e[k-delta];
    }
    fail(M.every((row,i)=>row.every((x,j)=>x===expected[k-1][i][j])),"orbit matrix "+k);
    // The orbit basis has Gram diag(1,10,10); it is not orthonormal.
    fail(M.every((row,i)=>row.every((x,j)=>counts[i]*x===counts[j]*M[j][i])),"weighted symmetry");
    const x=inverseImages[k-1];
    for(let i=0;i<3;i++){
      const value=M[i].reduce((sum,b,j)=>sum.add(new Q(b).mul(x[j])),new Q(0n));
      fail(value.str()===String(f[i]),"full inverse image "+k);
    }
    const quadratic=x.reduce((sum,b,i)=>sum.add(new Q(counts[i]*f[i]).mul(b)),new Q(0n));
    gamma.push(quadratic.div(new Q(norm)));
  }
  fail(gamma.map(x=>x.str()).join(",")==="181/7623,101/68607,127/617463","compressed scalars");
  const ratio=gamma[1].mul(gamma[1]).div(gamma[2]).div(gamma[0]);
  const difference=new Q(2n,5n).mul(gamma[0]).sub(gamma[1].mul(gamma[1]).div(gamma[2]));
  const quadratic=difference.mul(new Q(norm));
  fail(ratio.str()==="10201/22987","ratio");
  fail(ratio.sub(new Q(2n,5n)).n>0n,"strict violation");
  fail(quadratic.str()==="-1118/127","negative quadratic");
  fail(quadratic.div(new Q(8100n)).str()==="-559/514350","scaled LDL witness");
  fail(ratio.n<ratio.d,"this source does not violate constant one");
  return {
    status:"EXACT_COUNTEREXAMPLE_PASS",
    weights:a.map(String),N:7,s:2,n:2,
    orbitOrder:["weak-weak","strong-weak","strong-strong"],
    primitive:f.map(String),norm:String(norm),
    gamma:gamma.map(x=>x.str()),refinedConstant:"2/5",
    exactNormalizedRatio:ratio.str(),
    exactNegativeQuadratic:quadratic.str(),
    scaledLDLQuadratic:"-559/514350",
    scope:"Refutes the proposed refined constant; does not refute constant one."
  };
}
console.log(JSON.stringify(verifyCounterexample(),null,2));
