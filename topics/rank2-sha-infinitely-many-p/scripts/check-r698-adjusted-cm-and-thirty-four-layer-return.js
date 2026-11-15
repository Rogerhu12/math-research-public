#!/usr/bin/env node
"use strict";
/*
 * R698 standalone exact check.
 * Run only in the repository's public Actions:
 *   node topics/rank2-sha-infinitely-many-p/scripts/check-r698-adjusted-cm-and-thirty-four-layer-return.js
 * No data-file inputs or outputs. Stdout is a compact summary and SHA256.
 * This checks the fixed CRT, whole Heisenberg centre and the Pi_0 obstruction.
 * It does not replace the source/measure arguments in the proof.
 */
const assert = require("node:assert/strict");
const crypto = require("node:crypto");
const digest = crypto.createHash("sha256");
const mod = (a,n) => ((a%n)+n)%n;
function inv(a,n) {
  let [r,s,u,v]=[n,mod(a,n),0n,1n];
  while(s) { const q=r/s; [r,s]=[s,r-q*s]; [u,v]=[v,u-q*v]; }
  assert.equal(r,1n);
  return mod(u,n);
}
const cm = (a,b,n) => [mod(a,n),mod(b,n)];
const mul = (x,y,n) => cm(x[0]*y[0]-x[1]*y[1],
  x[0]*y[1]+x[1]*y[0]-x[1]*y[1],n);
const conj = (x,n) => cm(x[0]-x[1],-x[1],n);
const norm = x => x[0]*x[0]-x[0]*x[1]+x[1]*x[1];
function power(x,e,n) {
  let z=[1n,0n];
  while(e) { if(e&1n) z=mul(z,x,n); x=mul(x,x,n); e>>=1n; }
  return z;
}
const ratio = (x,n) => mul(x,x,n).map(v=>mod(v*inv(norm(x),n),n));
function eq(x,y) { assert.deepEqual(x,y); }
function crt(a,m,b,n) { return mod(a+m*mod((b-a)*inv(m,n),n),m*n); }
function witness(name,value) {
  digest.update(name+":"+JSON.stringify(value,(_,v)=>typeof v==="bigint"?v.toString():v)+"\n");
}
const M0=712345233600n, pi0=[1428552127n,2161889730n];
let z=M0,valuation17=0;
while(z%17n===0n) { z/=17n; valuation17++; }
assert.equal(valuation17,2);
const pi289=cm(...pi0,289n);
eq(pi289,[273n,87n]);
assert.equal(mod(2n*pi289[0]-pi289[1],289n),170n);
assert.equal(mod(norm(pi289),289n),258n);
const g289=ratio(pi289,289n);
eq(g289,[152n,17n]);
const g2=power(g289,2n,289n);
eq(g2,[273n,255n]);
for(let j=1n;j<17n;j++) assert.notDeepEqual(power(g2,j,289n),[1n,0n]);
eq(power(g2,17n,289n),[1n,0n]);
witness("old_fixed_17_square",{pi289,g289,g2,order:17});
const g32=ratio(cm(...pi0,32n),32n);
eq(power(g32,2n,32n),[25n,16n]);
eq(power(g32,4n,32n),[17n,0n]);
eq(power(g32,34n,32n),[25n,16n]);

const NA=134096n,NQ=23120n,full=2n*NA;
assert.equal(NA,29n*68n**2n);
assert.equal(NQ,5n*68n**2n);
assert.equal(136n*29n**2n+19720n,NA);
assert.equal(136n*5n**2n+19720n,NQ);
assert.equal(136n*29n*5n-19720n,0n);
const piWith29=[
  crt(pi0[0],M0,2n,29n),
  crt(pi0[1],M0,0n,29n)
];
assert.equal((M0*29n)%full,0n);
const gFull=ratio(cm(...piWith29,full),full);
const g34=power(gFull,34n,full);
const gB=cm(1n+3n*NA/2n,NA,full);
eq(g34,gB);
witness("full_A34_centre",{NA,NQ,modulus:full,g34,gB});

/* Canonical Weyl operator:
 * T_(a+b omega)/N e_j =
 * exp(pi i(2aj+ab)/N) e_(j+b).
 * Store phase as its exponent modulo 2N.
 */
function weyl(a,b,j,N) {
  return {index:mod(j+b,N),phase:mod(2n*a*j+a*b,2n*N)};
}
function B(j,N) {
  return {index:mod((1n+N/2n)*j+N/2n,N),
          phase:(j&1n)*N};
}
function conjugateB(a,b,j,N) {
  const x=B(j,N), y=weyl(a,b,x.index,N), z=B(y.index,N);
  return {index:z.index,phase:mod(x.phase+y.phase+z.phase,2n*N)};
}
for(let j=0n;j<NA;j++) {
  const x=B(j,NA), y=B(x.index,NA);
  assert.equal(y.index,j);
  assert.equal(mod(x.phase+y.phase,2n*NA),0n);
  const diagonal=conjugateB(1n,0n,j,NA);
  const shift=conjugateB(0n,1n,j,NA);
  eq(diagonal,weyl(gB[0],gB[1],j,NA));
  eq(shift,weyl(-gB[1],gB[0]-gB[1],j,NA));
  digest.update(j+":"+x.index+":"+x.phase+":"+
                diagonal.phase+":"+shift.phase+";");
}
witness("whole_basis_checked",NA);

/* Adjusted first-axis CM and every canonical half-period. */
const N=136n,M=272n;
const g13=ratio([4n,1n],M),g19=ratio([5n,2n],M);
eq(g13,[43n,147n]);
eq(g19,[87n,144n]);
const adj13=mul([0n,1n],g13,M);
const adj19=mul([-1n,0n],g19,M);
eq(adj13,[125n,168n]);
eq(adj19,[185n,128n]);
for(const g of [adj13,adj19]) {
  eq(cm(...g,4n),[1n,0n]);
  for(const u of [0n,1n]) for(const v of [0n,1n]) {
    const a=N*u/2n,b=N*v/2n;
    const ga=g[0]*a-g[1]*b, gb=g[1]*a+(g[0]-g[1])*b;
    for(let j=0n;j<N;j++) eq(weyl(ga,gb,j,N),weyl(a,b,j,N));
  }
}
witness("adjusted_CM",{g13,g19,adj13,adj19,halfPeriodChecks:1088});

/* Coupled B2, with first half-character rotated and the second fixed.
 * Characters are indexed by the three nonidentity points of E[2].
 * For N/4 even, the canonical lifts commute; there is no omitted minus
 * sign on the diagonal half-period.
 */
const chars=[[1,-1,-1],[-1,1,-1],[-1,-1,1]];
const fixed=chars[0];
const coupled=chars.map(c=>(1+c.reduce((a,x,i)=>a+x*fixed[i],0))/2-1);
eq(coupled,[1,-1,-1]);
assert.notEqual(coupled[0],coupled[1]);
assert.notEqual(coupled[0],coupled[2]);
witness("Pi0_noncommutation",{
  characterOrbit:chars,coupledEigenvalues:coupled,
  commutatorCoefficients:["0","-2/3","-2/3"]
});
const report={
  result:"PASS",
  oldRayPreserved:true,
  old17Power:valuation17,
  fullALevel:NA.toString(),
  completeBasisVectors:NA.toString(),
  ordinaryDepth:34,
  adjustedCMFixesEveryCanonicalE2Lift:true,
  firstPi0DoesNotCommuteWithCoupledAOperator:true,
  targetPrimeScan:false,
  outputSHA256:digest.digest("hex")
};
process.stdout.write(JSON.stringify(report,null,2)+"\n");
