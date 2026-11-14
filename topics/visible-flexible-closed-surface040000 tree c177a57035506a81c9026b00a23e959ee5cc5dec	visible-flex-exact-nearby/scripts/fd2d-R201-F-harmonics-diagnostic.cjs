"use strict";
/* Discrete diagnosis only: no Fourier replacement of the physical field. */
function diagnoseR201FSpectrum(position,z,fullAngles,locations){
 const result=[],N=fullAngles/2;
 if(!Number.isInteger(N)||N%2)throw Error("Even full half-period sample count required");
 for(const s of locations){
  const sl=position.slice(s,z,false),values=[];
  for(let j=0;j<N;j++){const p=sl.node(j),V=p.jets.Xs,T=p.jets.Xu.map(x=>x/p.a);values.push(V.reduce((a,v,k)=>a+v*T[k],0));}
  const mean=values.reduce((a,b)=>a+b,0)/N,variance=values.reduce((a,b)=>a+(b-mean)**2,0)/N,modes=[];
  for(let k=1;k<=N/2;k++){
   let cs=0,sn=0;for(let j=0;j<N;j++){cs+=values[j]*Math.cos(2*Math.PI*k*j/N);sn+=values[j]*Math.sin(2*Math.PI*k*j/N);}
   const scale=k===N/2?1/N:2/N;cs*=scale;sn*=scale;
   const energy=k===N/2?cs*cs:(cs*cs+sn*sn)/2;
   modes.push({index:k,physicalWaveNumber:2*k,cosine:cs,sine:sn,energy,varianceFraction:energy/variance});
  }
  result.push({s,values,mean,variance,modes,
   lowK7Fraction:modes.slice(0,7).reduce((a,m)=>a+m.energy,0)/variance,
   parsevalDifference:modes.reduce((a,m)=>a+m.energy,0)-variance});
 }
 return {schema:"fd2d-R201-complete-field-discrete-F-harmonics-v1",fullAngles,halfPeriodSamples:N,rows:result,
  scope:"Values from the actual complete position source. Discrete Fourier diagnosis only; no new geometry, solver, or continuum spectrum claim.",
  continuousCertificate:false};
}
if(typeof module!=="undefined"&&module.exports)module.exports={diagnoseR201FSpectrum};
