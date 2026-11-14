// Bounded memoization for one fixed closing_weighted_tail factory/config.
// Replaces only entry.point's lifetime Map. Arithmetic and all integrands,
// primitives, source data and physical parameters are unchanged.
// Call after createRecalibrationFactory(cfg), before factory.assemble().
export function boundTailPointCaches(factory,cfg,{pointsPerEntry=8}={}){
 if(!Number.isInteger(pointsPerEntry)||pointsPerEntry<1)throw Error('positive cache capacity required');
 const protectCell=cfg.protectCell??factory.parameters.protectCell;
 const warpSteps=factory.parameters.warpSteps;
 let entries=0;
 for(let n=0;n<protectCell;n++){
  // Use exactly the controls that the caller will pass to assemble. The
  // weighted factory installs the weights before this method returns.
  const row=factory.getEntries(n,cfg.valleyControls?.[n]??0);
  for(const entry of row.entries){
   const cache=new Map();entries++;
   entry.point=x=>{
    if(cache.has(x))return cache.get(x);
    const g=entry.profileSource(x),d=entry.integrand(x),
     i=Math.min(warpSteps-1,Math.max(0,Math.floor(x*warpSteps)));
    let A,B;
    if(x<=0){A=B=0;}
    else if(x>=1){A=entry.total[0];B=entry.total[1];}
    else{
     A=entry.cumA[i];B=entry.cumB[i];
     if(x>i/warpSteps){const z=entry.integrate(i/warpSteps,x);A+=z[0];B+=z[1];}
    }
    const result={g,A,B,dA:d[0],dB:d[1]};
    cache.set(x,result);
    while(cache.size>pointsPerEntry)cache.delete(cache.keys().next().value);
    return result;
   };
  }
 }
 return {schema:'fd2d-fixed-tail-bounded-point-cache-v1',entries,pointsPerEntry,
  maximum_retained_point_values:entries*pointsPerEntry,
  scope:'Memoization only. The configured fixed physical source, point arithmetic, and subsequent nonlinear equations are unchanged.'};
}
