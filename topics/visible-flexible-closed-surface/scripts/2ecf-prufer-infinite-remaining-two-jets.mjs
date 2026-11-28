#!/usr/bin/env node
/** Exact rational constants for all uncomputed real layers of the R314 input. */
class Rat {
  constructor(n,d=1n) {
    if(n instanceof Rat) {this.n=n.n;this.d=n.d;return;}
    n=BigInt(n);d=BigInt(d);
    if(d===0n)throw Error("zero denominator");
    if(d<0n){n=-n;d=-d;}
    let a=n<0n?-n:n,b=d;
    while(b){const z=a%b;a=b;b=z;}
    this.n=n/a;this.d=d/a;
  }
  add(b){b=rat(b);return new Rat(this.n*b.d+b.n*this.d,this.d*b.d);}
  sub(b){b=rat(b);return new Rat(this.n*b.d-b.n*this.d,this.d*b.d);}
  mul(b){b=rat(b);return new Rat(this.n*b.n,this.d*b.d);}
  div(b){b=rat(b);return new Rat(this.n*b.d,this.d*b.n);}
  pow(n){n=BigInt(n);return n>=0n?new Rat(this.n**n,this.d**n):new Rat(this.d**(-n),this.n**(-n));}
  cmp(b){b=rat(b);const z=this.n*b.d-b.n*this.d;return z<0n?-1:z>0n?1:0;}
  str(){return this.d===1n?String(this.n):this.n+"/"+this.d;}
}
const rat=(n,d)=>n instanceof Rat?n:new Rat(n,d);
function requireTrue(x,why){if(!x)throw Error(why);}
function expUpper(x,m=12){
  let term=rat(1),sum=term;
  for(let k=1;k<=m;k++){term=term.mul(x).div(k);sum=sum.add(term);}
  const next=term.mul(x).div(m+1);
  return sum.add(next.div(rat(1).sub(x.div(m+2))));
}
function expLower(x,m=20){
  let term=rat(1),sum=term;
  for(let k=1;k<=m;k++){term=term.mul(x).div(k);sum=sum.add(term);}
  return sum;
}
function decimalUpper(x,digits=12){
  requireTrue(x.n>=0n,"nonnegative decimal bound required");
  if(x.n===0n)return "0";
  let e=x.n.toString().length-x.d.toString().length;
  const ten=rat(10);
  if(x.cmp(ten.pow(e))<0)e--;
  const y=x.mul(ten.pow(digits-1-e));
  let q=(y.n+y.d-1n)/y.d;
  if(q>=10n**BigInt(digits)){q=(q+9n)/10n;e++;}
  const s=String(q).padStart(digits,"0");
  return s[0]+"."+s.slice(1)+"e"+e;
}
function packetTailBounds(N=37) {
  requireTrue(Number.isSafeInteger(N)&&N>=6,"N must be an integer >=6");
  const one=rat(1),zero=rat(0),rc=rat(371,1000),R=rat(143,250),z0=rat(1431,2500);
  const eps=rat(1,250000),slope=rat(1,125000),d=rat(11,1000),rt=rat(7,2);
  const d6=d.div(16),qcap=rat(24331,100000),logCap=rat(43,10);
  const tangent=d6.div(one.sub(d6.pow(2).div(2)));
  requireTrue(rat(4).add(tangent).div(one.sub(tangent.mul(4))).cmp(logCap)<0,"transition log-amplitude bound");
  const endpointSquare=one.add(d6.mul(4)).pow(2).div(17).add(d6.mul(8).pow(2));
  requireTrue(endpointSquare.cmp(qcap.pow(2))<0,"constant-piece endpoint norm");
  requireTrue(rat(16,17).cmp(rat(97,100).pow(2))>0,"sin(theta)>0.97");
  const transitionExponent=d6.mul(logCap).mul(4);
  const gain=rat(97,100).div(qcap).pow(2).mul(one.sub(transitionExponent));
  requireTrue(gain.cmp(15)>0,"each deep outward gain exceeds 15");
  const partialNorm=rat(33,8);
  requireTrue(rat(17).mul(one.add(d6.pow(2))).cmp(partialNorm.pow(2))<0,"constant-piece partial amplitude");
  const partial=partialNorm.pow(2).div(one.sub(transitionExponent));
  requireTrue(partial.cmp(18)<0,"each layer partial amplitude below 18");
  // Total x length <20*(2d)+48*(2d)=1.496.
  requireTrue(rat(173,50).pow(2).cmp(12)<0,"sqrt12 lower");
  requireTrue(rt.pow(2).cmp(12)>0,"sqrt12 upper");
  const xTotal=d.mul(136);
  const rMax=rc.mul(expUpper(xTotal.div(rat(173,50))));
  requireTrue(rMax.cmp(R)<0,"entire infinite radius below 0.572");
  requireTrue(expLower(rat(23,5)).cmp(rat(1000,11))>0,"log(1000/11)<4.6");
  requireTrue(expLower(rat(7,10),6).cmp(2)>0,"log2<0.7");
  const j=N-2,two=rat(2),delta=d.div(two.pow(j));
  const B=rat(6,5).div(1000000).div(rat(15).pow(N-6));
  const px=rat(15,8).mul(N+4).div(delta.pow(3));
  const cw=slope.mul(R.div(rc).pow(7));
  const w=cw.div(two.pow(3*j));
  const wr=cw.div(rc).mul(rat(7).div(two.pow(3*j)).add(rat(15,8).mul(rt).mul(N+4).div(d.pow(2)).div(two.pow(j))));
  const missingX=delta.mul(96),missingR=R.mul(missingX).div(3);
  const z=w.mul(missingR);
  const f=eps.mul(R.pow(4)).mul(B);
  const fr=eps.mul(R.pow(3)).mul(B).mul(rat(4).add(rt.div(delta)));
  const frr=eps.mul(R.pow(2)).mul(B).mul(rt.mul(7).div(delta).add(px.mul(12)));
  const mu=slope.mul(R.pow(7)).mul(delta).div(two.pow(3*j));
  const U=eps.mul(rat(6,5)).mul(mu).mul(B).div(rc.pow(3));
  const Ur=w.mul(fr),Urr=wr.mul(f).mul(4).div(rc);
  const A0=z.add(f).add(U);
  const Ar=w.add(fr).add(Ur),Au=f.mul(2).add(U.mul(rat(3,2)));
  const Arr=wr.add(frr).add(Urr),Aru=fr.mul(2).add(Ur.mul(rat(3,2))),Auu=f.mul(4).add(U.mul(3));
  const derivative=Ar.add(Au.div(rc));
  requireTrue(derivative.cmp(one)<0,"flat-chart immersion");
  const Hessian=Arr.add(Aru.mul(2).div(rc)).add(Au.mul(2).add(Auu).div(rc.pow(2))).add(Ar.div(rc));
  const curvature=Hessian.div(one.sub(derivative).pow(2));
  const support=z0.sub(A0).sub(R.add(z0).add(A0).mul(derivative).mul(2).div(one.sub(derivative)));
  const finiteAmplitudeMetric=Ur.add(fr).pow(2).add(U.mul(rat(3,2)).add(f.mul(2)).div(rc).pow(2));
  const bounds={omittedX:missingX,omittedPhysicalRadialWidth:missingR,
    QandPi:B,pX:px,backgroundSlope:w,backgroundSlopeDerivative:wr,backgroundHeightFromFlat:z,
    physicalHeightMode:f,physicalHeightModeDerivative:fr,physicalHeightModeSecondDerivative:frr,
    physicalHorizontalMode:U,physicalHorizontalModeDerivative:Ur,physicalHorizontalModeSecondDerivative:Urr,
    flatChartPositionDifference:A0,flatChartFirstDerivativeOperator:derivative,
    flatChartSecondDerivativeOperator:Hessian,principalCurvatureAbsolute:curvature,
    outwardSupportLower:support,metricRelativeToOwnRotationalBackground:finiteAmplitudeMetric};
  const record={};
  for(const [k,v] of Object.entries(bounds)){
    record[k]={exact:v.str(),upperDecimal: k==="outwardSupportLower"?undefined:decimalUpper(v)};
  }
  return {schema:"R314-actual-infinite-prufer-tail-two-jets-rational-v1",fromLayer:N,
    constants:{cuff:rc.str(),height:z0.str(),modeScale:eps.str(),slope:slope.str(),radiusUpper:R.str()},
    proofConstants:{deepGainLower:gain.str(),partialAmplitudeUpper:partial.str(),entireRadiusUpper:rMax.str()},
    bounds:record,
    scope:"Every real layer n>=N, every material angle and phase. This proves local actual tail jets and curvature, not the entire closed surface, not equality of the nonlinear finite-amplitude metric, and not the old p32 target."};
}

export {packetTailBounds};
if(typeof process!=="undefined"&&process.argv[1]&&process.argv[1].endsWith("2ecf-prufer-infinite-remaining-two-jets.mjs")) {
  const n=process.argv[2]===undefined?37:Number(process.argv[2]);
  console.log(JSON.stringify(packetTailBounds(n),null,2));
}
