"use strict";
/* Explicit finite nonreflection seeds. No old state or mathematical provider is
 * modified. Each sine/cosine pair is rotated, not clipped or silently dropped.
 */
function phaseRotateR201Seed(input,options={}){
 const J=input.options.radialBasisCount,K=input.options.modes,legacy=2*J*K+2*J+1,
  width=2*K+1,amplitudeIndex=legacy+J*width;
 if(input.z.length!==amplitudeIndex+1||input.amplitudeIndex!==amplitudeIndex)throw Error("Explicit R201/R205 two-global layout required");
 const knots=input.options.radialKnots;if(!Array.isArray(knots)||knots.length!==J+4)throw Error("Saved R196 simple knots required");
 const angle=options.angle===undefined?1/8:options.angle,families=options.families||["theta","psi"];
 if(!Number.isFinite(angle)||Math.abs(angle)>1/2||families.some(x=>x!=="theta"&&x!=="psi"))throw Error("Explicit bounded phase and known channel families required");
 const z=Array.from(input.z),changes=[],phaseByBlock=[],toNumber=x=>Number(x[0])/Number(x[1]);
 let pairEnergyError=0;
 for(let j=0;j<J;j++){
  const q=(toNumber(knots[j+1])+toNumber(knots[j+2])+toNumber(knots[j+3]))/3,
   beta=angle*64*q*q*q*(1-q)*(1-q)*(1-q);
  phaseByBlock.push({j,q,beta});
  for(let k=1;k<=K;k++)for(const family of families){
   const si=(family==="theta"?0:J*K)+j*K+k-1,
    ci=legacy+j*width+(family==="theta"?k:K+k),
    phase=2*k*beta,cs=Math.cos(phase),sn=Math.sin(phase),a=input.z[si],b=input.z[ci];
   z[si]=a*cs+b*sn;z[ci]=b*cs-a*sn;
   pairEnergyError=Math.max(pairEnergyError,Math.abs(z[si]*z[si]+z[ci]*z[ci]-a*a-b*b));
   if(z[si]!==a)changes.push(si);if(z[ci]!==b)changes.push(ci);
  }
 }
 const changed=new Set(changes),unchanged=Array.from({length:z.length},(_,i)=>i).filter(i=>!changed.has(i));
 const cut=2*J*K+J,radius=[cut+1,legacy],protectedIndices=[cut,amplitudeIndex,...Array.from({length:J},(_,j)=>2*J*K+j),...Array.from({length:J},(_,j)=>radius[0]+j),...Array.from({length:J},(_,j)=>legacy+j*width)];
 for(const i of protectedIndices)if(!Object.is(z[i],input.z[i]))throw Error("Protected height/radius/amplitude/theta-constant coefficient changed");
 return {z,definition:{schema:"fd2d-R201-compact-mode-phase-seed-v1",angle,families,phaseByBlock,
  formula:"beta_j=angle*64*q_j^3*(1-q_j)^3; q_j is the saved-knot Greville mean; [sin,cos] -> [sin*cos(2k beta)+cos*sin(2k beta),cos*cos(2k beta)-sin*sin(2k beta)]",
  meaning:"Finite new initial field; not claimed an accepted LM step or exact pointwise material reparameterization.",
  samePhysicalTargetMetric:true,allHeightRadiusAmplitudeAndThetaConstantCoefficientsIdentical:true,
  exactCentralAndCutTwojetsRetainedByTheExistingZeroTwojetBasis:true,
  changedIndices:Array.from(changed).sort((a,b)=>a-b),unchangedCount:unchanged.length,
  maximumBinary64PairEnergyError:pairEnergyError,
  oldMaximumAppendedCoefficient:Math.max(...input.z.slice(legacy,amplitudeIndex).map(Math.abs)),
  newMaximumAppendedCoefficient:Math.max(...z.slice(legacy,amplitudeIndex).map(Math.abs))}};
}
if(typeof module!=="undefined"&&module.exports)module.exports={phaseRotateR201Seed};
