// Same linear ODE, RK4 order and cusp splits as pinned 950f-tail-subdivision.
// Evaluate common physical coefficients once per grid point, then advance all
// angular modes. This avoids retaining a full deep grid for every scalar run.
const SQRT12=Math.sqrt(12);

function ideal(mode,R,a){
  if(mode===2)return 0;
  const nu=mode*mode*(mode*mode-1)/12,rho=2**a,alpha=1+1/R;
  const t00=1-alpha*nu*R,t10=(-nu*(1+R)+alpha*nu*nu*R)/rho,t11=(1-alpha*nu)/rho;
  const tr=t00+t11,det=1/rho,lambda=.5*(tr-Math.sqrt(tr*tr-4*det));
  return t10/(lambda-t11);
}

export function advanceLinearColumns(ys,profiles,mu,rows,steps){
  const logMu=Math.log(mu);
  // Keep the source multiplication order, including its mode-dependent b,d.
  // Cache only common expensive profile/log/exp values, not reassociations.
  const geometry=g=>{const lr=Math.log(g.r);return [SQRT12*g.drdx*Math.exp(logMu-8*lr-g.logw),
    g.drdx,Math.exp(6*lr+g.logw-logMu),g.r];};
  for(const profile of profiles)for(let k=0;k<steps;k++){
    const lo=k/steps,hi=(k+1)/steps;
    const xs=[lo,...(profile.integrationBreakpoints??[]).filter(x=>x>lo&&x<hi).sort((a,b)=>a-b),hi];
    for(let s=0;s<xs.length-1;s++){
      const x=xs[s],h=xs[s+1]-x,g0=geometry(profile(x)),gm=geometry(profile(x+h/2)),g1=geometry(profile(x+h));
      for(let j=0;j<rows.length;j++){
        const y=ys[j],z=rows[j],l=z.mode*z.mode-4,v=z.nu,u0=y[0],v0=y[1];
        const B0=-v*SQRT12*g0[1]*g0[2],D0=l*g0[1]/g0[3],
          Bm=-v*SQRT12*gm[1]*gm[2],Dm=l*gm[1]/gm[3],
          B1=-v*SQRT12*g1[1]*g1[2],D1=l*g1[1]/g1[3];
        const a0=D0*u0+g0[0]*v0,a1=B0*u0-D0*v0;
        const u1=u0+h*a0/2,v1=v0+h*a1/2,b0=Dm*u1+gm[0]*v1,b1=Bm*u1-Dm*v1;
        const u2=u0+h*b0/2,v2=v0+h*b1/2,c0=Dm*u2+gm[0]*v2,c1=Bm*u2-Dm*v2;
        const u3=u0+h*c0,v3=v0+h*c1,d0=D1*u3+g1[0]*v3,d1=B1*u3-D1*v3;
        y[0]=u0+h*(a0+2*b0+2*c0+d0)/6;y[1]=v0+h*(a1+2*b1+2*c1+d1)/6;
        if(!Number.isFinite(y[0])||!Number.isFinite(y[1]))throw Error('Nonfinite batched linear column, mode '+z.mode);
      }
    }
  }
  return ys;
}

export function buildRationalStableStageGraphs(physical,stages,{modes,spacing,linearFar,linearSteps}){
  if(!(linearFar>stages.rawDepth))throw Error('linearFar must exceed the nonlinear physical depth');
  const rho=2**physical.parameters.a;
  const rows=Array.from({length:modes},(_,j)=>{const mode=spacing*(j+1);return {mode,nu:mode*mode*(mode*mode-1)/12};});
  const graphs=Array.from({length:stages.cells.length+1},()=>new Float64Array(modes));
  const gains=Array.from({length:stages.cells.length},()=>new Float64Array(modes));
  const ys=rows.map(z=>[1,ideal(z.mode,physical.parameters.R,physical.parameters.a)]);
  let lastMu=physical.cells[linearFar-1].mu;
  for(let n=linearFar-1;n>=stages.rawDepth;n--){
    const c=physical.cells[n],ratio=lastMu/c.mu;lastMu=c.mu;
    for(const y of ys)y[1]*=ratio;
    advanceLinearColumns(ys,c.profiles,c.mu,rows,linearSteps);
    for(const y of ys){const a=Math.hypot(...y);if(!(a>0))throw Error('Zero linear column');y[0]/=a;y[1]/=a;}
  }
  for(let j=0;j<modes;j++)graphs.at(-1)[j]=ys[j][1]/(rho*ys[j][0]);
  for(let n=stages.cells.length-1;n>=0;n--){
    const c=stages.cells[n],cols=rows.map((_,j)=>[1,graphs[n+1][j]]);
    advanceLinearColumns(cols,c.profiles,c.mu,rows,Math.max(8,Math.ceil(linearSteps/stages.parts)));
    for(let j=0;j<modes;j++){
      gains[n][j]=cols[j][0];graphs[n][j]=cols[j][1]/(c.portRatio*cols[j][0]);
      if(!Number.isFinite(graphs[n][j])||!Number.isFinite(gains[n][j])||Math.abs(gains[n][j])<=1e-250)
        throw Error('Stage Dirichlet chart vertical at '+n+', mode '+rows[j].mode);
    }
  }
  return {graphs,gains};
}
