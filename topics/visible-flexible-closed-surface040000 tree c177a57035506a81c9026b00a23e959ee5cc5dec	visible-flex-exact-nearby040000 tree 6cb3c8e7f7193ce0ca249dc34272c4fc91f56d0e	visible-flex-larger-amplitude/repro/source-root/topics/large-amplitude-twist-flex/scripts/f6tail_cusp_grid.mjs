// Numerical grids for one unchanged analytic compact profile. They split at
// zeros of the raw logarithmic slope before |w_x| enters the radial warp.
export function rawLogSlopeCriticalPoints(raw){
  const d0=raw(0).dlogwdx,delta=(raw(.5).dlogwdx-d0)/(15/8);
  if(delta===0)return[];
  const q=-d0/(30*delta);
  if(!(q>0&&q<1/16))return[];
  const z=Math.sqrt(q),lo=2*z/(1+Math.sqrt(1-4*z));
  return [lo,1-lo];
}

export function installCompactCriticalPoints(tail){
  const smooth=x=>x*x*x*(10+x*(-15+6*x)),derivative=x=>30*x*x*(1-x)*(1-x);
  for(let n=0;n<tail.cells.length;n++)for(let j=0;j<tail.cells[n].profiles.length;j++){
    const base=tail.source.cells[n].profiles[j],beta=tail.parameters.valleyControls?.[n]??0,
      raw=x=>{const g=base(x);return {...g,dlogwdx:g.dlogwdx+beta*(j===3?derivative(x):j===5?-derivative(x):0),
        logw:g.logw+beta*(j===3?smooth(x):j===4?1:j===5?1-smooth(x):0)};};
    tail.cells[n].profiles[j].integrationBreakpoints=rawLogSlopeCriticalPoints(raw);
  }
  return tail;
}

export function splitIntegrationInterval(a,b,breakpoints=[]){
  const lo=Math.min(a,b),hi=Math.max(a,b),middle=breakpoints.filter(x=>x>lo&&x<hi).sort((x,y)=>x-y);
  if(b<a)middle.reverse();return [a,...middle,b];
}

export function integrationGrid(steps,breakpoints=[]){
  const grid=[...Array.from({length:steps+1},(_,k)=>k/steps),...breakpoints].sort((x,y)=>x-y);
  return grid.filter((x,k)=>k===0||x!==grid[k-1]);
}

export function withCuspAwareRK(engine){
  const original=engine.rk4;
  return {...engine,rk4(state,profile,x,h){
    const grid=splitIntegrationInterval(x,x+h,profile.integrationBreakpoints);let y=state;
    if(grid.length===2)return original(state,profile,x,h);
    for(let k=0;k<grid.length-1;k++)y=original(y,profile,grid[k],grid[k+1]-grid[k]);return y;
  }};
}
