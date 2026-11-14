// Exploratory float64 samples only; no reach lower-bound certificate.
// Root, 2026-11-09. No existing research data, PDE or main solver is used.
function scanEpicycleSeeds(options) {
 "use strict";
 options = options || {};
 const count=options.count||360;
 const etas=options.etas||[0.44,0.45,0.475,0.5,0.55,0.6,Math.SQRT1_2];
 const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
 const sub=(a,b)=>[a[0]-b[0],a[1]-b[1],a[2]-b[2]];
 const cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
 const norm=a=>Math.sqrt(dot(a,a));
 const rows=[];
 for(const eta of etas){
  const sigma=Math.sqrt(1-eta*eta);
  const p2=2*(1-eta*eta)/(1+6*eta-3*eta*eta);
  if(!(p2>0&&p2<1))throw Error("invalid seed");
  const p=Math.sqrt(p2),q=Math.sqrt(1-p2);
  const R=sigma*(eta+(3-1.5*eta)*p2);
  const A=p*q*(1-eta)**2/4;
  const P=p*q*(2+eta-eta*eta)/2;
  const B=sigma*p2*(1-eta)/28;
  const C=sigma*p2*(1+eta)/20;
  const U=sigma*p*q*(3-2*eta)/3,V=sigma*sigma*p2/12;
  const modes=[[1,R],[4,A],[-2,P],[7,B],[-5,C]];
  const dmodes=[[1,sigma*q],[4,p*(eta-1)/2],[-2,p*(eta+1)/2]];
  const pts=[],tans=[];
  let kappaMin=Infinity,kappaMax=-Infinity,identityError=0;
  for(let i=0;i<count;i++){
   const t=2*Math.PI*i/count;
   let c=[0,0,-U*Math.sin(3*t)-V*Math.sin(6*t)];
   let cp=[0,0,-3*U*Math.cos(3*t)-6*V*Math.cos(6*t)];
   let d=[0,0,-eta*q+sigma*p*Math.cos(3*t)];
   let dp=[0,0,-3*sigma*p*Math.sin(3*t)];
   for(const [n,a] of modes){c[0]-=a*Math.sin(n*t);c[1]+=a*Math.cos(n*t);cp[0]-=n*a*Math.cos(n*t);cp[1]-=n*a*Math.sin(n*t);}
   for(const [n,a] of dmodes){d[0]-=a*Math.cos(n*t);d[1]-=a*Math.sin(n*t);dp[0]+=n*a*Math.sin(n*t);dp[1]-=n*a*Math.cos(n*t);}
   identityError=Math.max(identityError,norm(sub(cp,cross(d,dp))));
   const speed=norm(cp);pts.push(c);tans.push(cp.map(x=>x/speed));
   const J=(eta-3)*q-sigma*p*Math.cos(3*t),W=10-6*eta;
   const kap=(J**3-(19-9*eta)*J-3*W*q)/(W-J*J)**1.5;
   kappaMin=Math.min(kappaMin,kap);kappaMax=Math.max(kappaMax,kap);
  }
  let diameter=0,normalChordMin=Infinity,minPair=null;
  for(let i=0;i<count;i++)for(let j=i+1;j<count;j++){
   const v=sub(pts[j],pts[i]),h2=dot(v,v),h=Math.sqrt(h2);diameter=Math.max(diameter,h);
   for(const [at,tangent] of [[i,tans[i]],[j,tans[j]]]){
    const normal=Math.sqrt(Math.max(0,h2-dot(v,tangent)**2));
    if(normal>1e-13){const tau=h2/(2*normal);if(tau<normalChordMin){normalChordMin=tau;minPair=[at===i?i:j,at===i?j:i];}}
   }
  }
  const k=Math.max(Math.abs(kappaMin),Math.abs(kappaMax));
  const surfaceCurvatureRadius=2/(k+Math.sqrt(k*k+4));
  rows.push({eta,p2,kappaMin,kappaMax,diameterSample:diameter,normalChordMinSample:normalChordMin,
   normalChordToDiameterSample:normalChordMin/diameter,surfaceCurvatureRadiusSample:surfaceCurvatureRadius,
   localRadiusToDiameterSample:surfaceCurvatureRadius/diameter,minPair,identityError});
 }
 return {status:"HEURISTIC_FLOAT64_SAMPLES_ONLY",count,rows,
  lowerReachCertified:false,embeddingCertified:false,positiveCurvatureCertified:false,
  fixedMetricFamilyComputed:false,mainSolverCalls:0,noResearchDataLoaded:true};
}
if (typeof module !== "undefined" && module.exports) {
  module.exports = {scanEpicycleSeeds};
  if (typeof require !== "undefined" && require.main === module) {
    const count = process.argv[2] ? Number(process.argv[2]) : 360;
    if (!Number.isInteger(count) || count < 36 || count > 4096) {
      throw new Error("sample count must be an integer from 36 to 4096");
    }
    console.log(JSON.stringify(scanEpicycleSeeds({count}), null, 2));
  }
}
