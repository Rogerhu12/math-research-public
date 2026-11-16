// R150, complete coefficient-31 characteristic after the paid rational degree 298.
// Author: ChatGPT (AI), literature_audit. 2026-11-16.
// Inputs are the two already-published small actual receipts. No matrix is loaded.
export function auditCoefficientCharacteristic16(omegaOuter, i2Outer) {
  const p = 31;
  const require = (b,s) => { if (!b) throw new Error(s); };
  const norm = x => ((x % p) + p) % p;
  const trim = a => { a=a.map(norm); while(a.length>1&&!a[a.length-1])a.pop(); return a; };
  const equal = (a,b) => { a=trim(a);b=trim(b);return a.length===b.length&&a.every((x,i)=>x===b[i]); };
  const mul = (a,b) => {const c=Array(a.length+b.length-1).fill(0);
    for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]=norm(c[i+j]+a[i]*b[j]);return trim(c);};
  const pow = (a,n) => {let b=[1];for(let i=0;i<n;i++)b=mul(b,a);return b;};
  const product = fs => fs.reduce((a,[b,n])=>mul(a,pow(b,n)),[1]);
  const div = (a,b) => {a=trim(a);b=trim(b);require(b[b.length-1]===1,"monic divisor");
    const q=Array(Math.max(1,a.length-b.length+1)).fill(0);
    while(a.length>=b.length&&!(a.length===1&&!a[0])){const k=a.length-b.length,c=a[a.length-1];
      q[k]=c;for(let j=0;j<b.length;j++)a[k+j]=norm(a[k+j]-c*b[j]);a=trim(a);}
    require(a.length===1&&a[0]===0,"exact polynomial division");return trim(q);};
  require(omegaOuter.exitCode===0&&omegaOuter.result.status==="completed","actual Omega success");
  require(i2Outer.exitCode===0&&i2Outer.result.status==="completed","actual complete I2 success");
  const op=omegaOuter.result.parameters, ip=i2Outer.result.parameters.conclusion;
  require(op.all121OmegaCoefficientDenominatorsAre31Units&&op.fieldSquareIdentityVerified,"paid original Omega coefficients");
  require(ip.completeGlobalI2Dimension===7&&ip.all315CoordinatesRetained&&ip.multiplicationBySClosed,"complete original I2");
  const omega=op.fieldOmega.coefficientsAscending;
  const eta=ip.characteristic.coefficientsAscending;
  const remaining=ip.remaining315Characteristic.coefficientsAscending;
  const factors=ip.remaining315Characteristic.factors;
  const outside=factors.filter(f=>[2,6,7,16,29].includes(f.degree)&&
    !(f.degree===6&&equal(f.coefficientsAscending,[30,15,0,2,18,13,1])));
  require(outside.length===5&&outside.every(f=>f.exponent===2),"all five outside factors");
  require(equal(product(outside.map(f=>[f.coefficientsAscending,f.exponent])),omega),"all121 Omega/outside identity");
  const chi315=mul(eta,remaining);
  const s=[0,1], sm1=[30,1], sm2=[29,1], sp6=[6,1];
  const fp=[17,25,26,1], fm=[24,24,27,1], e6=[30,15,0,2,18,13,1];
  const e8=mul(mul(sm1,sm2),e6);
  const originalE8=[9600,-25472,-3392,15936,-2888,-936,153,50,5].map(x=>norm(25*x));
  require(equal(e8,originalE8),"all9 monic original E8 reduction");
  const k178=product([[s,66],[sm2,12],[sp6,12],[fp,8],[fm,8],[e8,5]]);
  const delta298=mul(k178,omega);
  const coefficient16=product([[sm1,2],[sm2,14]]);
  const cbar=div(chi315,sm2);
  require(chi315.length===316&&k178.length===179&&delta298.length===299,"paid degrees");
  require(equal(mul(delta298,coefficient16),cbar),"all315 coefficient carrier identity");
  require(equal(mul(mul(delta298,coefficient16),sm2),chi315),"all316 full characteristic identity");
  require(equal(div(cbar,delta298),coefficient16),"exact coefficient torsion quotient");
  return {
    format:"r150-original-coefficient31-sixteen-directions-small-audit-v1",
    prime:p,
    interpretation:"Polynomial identity audit; rational Delta=mon(K178)*Omega and J=s-2 are separately proved inputs.",
    omegaCoefficientsCompared:121,
    e8CoefficientsCompared:9,
    carrierCoefficientsCompared:315,
    fullCharacteristicCoefficientsCompared:316,
    rationalAffineDegree:298,
    carrierResidueDimension:314,
    coefficientCyclicSummands:16,
    coefficientTorsionReductionCharacteristic:coefficient16,
    coefficientTorsionPrimaryCounts:{"1":2,"2":14},
    knownExactGlobalPrimeMultiplicities:[2,5,2,4,2],
    higherPrimeCyclicSummands:1,
    higherPrimeExponentLowerBound:6,
    allPolynomialIdentitiesVerified:true,
    noNewSourceOrMatrixCalculation:true
  };
}
