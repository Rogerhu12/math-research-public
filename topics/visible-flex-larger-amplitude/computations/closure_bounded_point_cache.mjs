// Replaces only a private weighted factory's point memoization policy.
// The expressions and operation order are copied from the pinned weighted
// entry.point implementation.  Profiles, calibration, warp and quadrature
// data remain the same; a caller should fingerprint them before and after.
export function installBoundedPointCache(factory, {count, controls=[], limit=96}={}) {
  if(!Number.isInteger(count)||count<0||!Number.isInteger(limit)||limit<1)
    throw Error('A finite cell count and positive point-cache limit are required');
  const warpSteps=factory.parameters.warpSteps;
  for(let n=0;n<count;n++){
    const row=factory.getEntries(n,controls[n]??0);
    for(const entry of row.entries){
      const cache=new Map();
      entry.point=x=>{
        if(cache.has(x))return cache.get(x);
        const g=entry.profileSource(x),d=entry.integrand(x);
        const i=Math.min(warpSteps-1,Math.max(0,Math.floor(x*warpSteps)));
        let A,B;
        if(x<=0){A=B=0;}else if(x>=1){A=entry.total[0];B=entry.total[1];}
        else{
          A=entry.cumA[i];B=entry.cumB[i];
          if(x>i/warpSteps){const z=entry.integrate(i/warpSteps,x);A+=z[0];B+=z[1];}
        }
        const result={g,A,B,dA:d[0],dB:d[1]};cache.set(x,result);
        while(cache.size>limit)cache.delete(cache.keys().next().value);
        return result;
      };
    }
  }
}
