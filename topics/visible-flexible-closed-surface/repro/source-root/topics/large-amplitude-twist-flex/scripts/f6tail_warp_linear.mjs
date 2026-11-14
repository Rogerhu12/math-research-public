// True linear height transfers on the redistributed physical-radius geometry.
import fs from 'node:fs/promises';
import {createWarpGeometry} from './f6tail_warp_geometry.mjs';
export function physicalLinearTransfer(profiles,{mode=2,mu=1,orientation=1,steps=128,derivative=false}={}){
 const nu=mode*mode*(mode*mode-1)/12,size=derivative?8:4;let state=new Float64Array(size);state[0]=state[3]=1;
 function rhs(y,p,x){const g=p(x),P=Math.exp(7*Math.log(g.r)+g.logw-Math.log(mu)),len=Math.sqrt(12)*Math.abs(g.drdx)/g.r,k=(mode*mode-4)*g.drdx/g.r,u=len/P,v=-nu*len*P,z=new Float64Array(size),B=g.bump??0;for(let j=0;j<2;j++){z[j]=k*y[j]+u*y[j+2];z[j+2]=v*y[j]-k*y[j+2];if(derivative){z[j+4]=k*y[j+4]+u*y[j+6]-B*u*y[j+2];z[j+6]=v*y[j+4]-k*y[j+6]+B*v*y[j];}}return z;}
 for(const p of profiles)for(let i=0;i<steps;i++){const h=1/steps,x=i*h,a=rhs(state,p,x),tmp=new Float64Array(size);for(let j=0;j<size;j++)tmp[j]=state[j]+h*a[j]/2;const b=rhs(tmp,p,x+h/2);for(let j=0;j<size;j++)tmp[j]=state[j]+h*b[j]/2;const c=rhs(tmp,p,x+h/2);for(let j=0;j<size;j++)tmp[j]=state[j]+h*c[j];const d=rhs(tmp,p,x+h);for(let j=0;j<size;j++)state[j]+=h*(a[j]+2*b[j]+2*c[j]+d[j])/6;}
 const matrix=Array.from(state.slice(0,4));return {matrix,derivative:derivative?Array.from(state.slice(4)):null,determinant:matrix[0]*matrix[3]-matrix[1]*matrix[2]};
}
function farGraph(M,R,a,spacing=2){const rho=2**a,end=new Float64Array(M);for(let j=0;j<M;j++){const m=spacing*(j+1),nu=m*m*(m*m-1)/12,alpha=1+1/R,t00=1-alpha*nu*R,t10=(-nu*(1+R)+alpha*nu*nu*R)/rho,t11=(1-alpha*nu)/rho,tr=t00+t11,det=1/rho,lam=.5*(tr-Math.sqrt(tr*tr-4*det));end[j]=m===2?0:t10/(lam-t11);}return end;}
export function buildWarpTailGraphs(geometry,{modes=2,spacing=2,linearFar=32,linearSteps=128}={}){
 if(linearFar>geometry.leftCells.length)throw Error('linearFar exceeds represented redesigned prefix');
 const a=geometry.linearDeepParameters.a,rho=2**a,answer={};
 for(const [side,cells,orientation] of [['left',geometry.leftCells,1],['right',geometry.rightCells,-1]]){
  const matrices=[],graphs=[],gains=[];let maxDeterminantError=0;
  for(let n=0;n<linearFar;n++){const row=[];for(let j=0;j<modes;j++){const t=physicalLinearTransfer(cells[n].profiles,{mode:spacing*(j+1),mu:cells[n].mu,orientation,steps:linearSteps});maxDeterminantError=Math.max(maxDeterminantError,Math.abs(t.determinant-1));const m=t.matrix;row.push([m[0],m[1],m[2]/rho,m[3]/rho]);}matrices.push(row);}
  graphs[linearFar]=Float64Array.from(farGraph(modes,geometry.linearDeepParameters.R,a,spacing),v=>v*(geometry.momentumNormalization??1));
  for(let n=linearFar-1;n>=0;n--){const G=new Float64Array(modes),gain=new Float64Array(modes);for(let j=0;j<modes;j++){const t=matrices[n][j],z=graphs[n+1][j];gain[j]=t[0]+t[1]*z;if(!(Math.abs(gain[j])>1e-14))throw Error('true tail Dirichlet chart vertical');G[j]=(t[2]+t[3]*z)/gain[j];}graphs[n]=G;gains[n]=gain;}
  answer[side]={matrices,graphs,gains,maxDeterminantError};
 }
 return {...answer,parameters:{modes,spacing,linearFar,linearSteps,a,rho,scope:'True changed-profile finite linear graphs, with far ideal graph as a convergence parameter.'}};
}
export function calibrateWarpCore(geometry,graphs,options={}){
 const mode=graphs.parameters.spacing??2,steps=options.coreSteps??256,limit=options.betaLimit??20,gL=graphs.left.graphs[0][0],gR=graphs.right.graphs[0][0],history=[];
 function evaluate(beta,derivative=true){const t=physicalLinearTransfer(geometry.coreProfiles(beta,options.controlMode??'left'),{mode,mu:geometry.epsilon,orientation:1,steps,derivative}),m=t.matrix,Q=m[0]+m[1]*gL,pi=m[2]+m[3]*gL,f=pi+gR*Q,df=derivative?t.derivative[2]+t.derivative[3]*gL+gR*(t.derivative[0]+t.derivative[1]*gL):null;return {beta,f,df,Q,pi,normalizedResidual:Math.abs(f)/Math.max(1,Math.abs(Q),Math.abs(pi)),matrix:m,determinant:t.determinant};}
 let beta=options.betaInitial??0,current;
 for(let it=0;it<(options.maxIterations??20);it++){current=evaluate(beta);history.push(current);options.progress?.(current);if(current.normalizedResidual<(options.tolerance??1e-10))break;if(!(Math.abs(current.df)>1e-15))break;const change=-current.f/current.df;let accepted=false;for(let k=0;k<20;k++){const next=beta+2**(-k)*change;if(Math.abs(next)>limit)continue;const e=evaluate(next,false);if(Math.abs(e.f)<Math.abs(current.f)){beta=next;accepted=true;break;}}if(!accepted)break;}
 current=evaluate(beta);let states=[[1,gL]],y=Float64Array.from(states[0]);for(const p of geometry.coreProfiles(beta,options.controlMode??'left')){const m=physicalLinearTransfer([p],{mode,mu:geometry.epsilon,orientation:1,steps}).matrix;y=Float64Array.from([m[0]*y[0]+m[1]*y[1],m[2]*y[0]+m[3]*y[1]]);states.push(Array.from(y));}
 return {...current,converged:current.normalizedResidual<(options.tolerance??1e-10),states,history,parameters:{steps,betaLimit:limit,gL,gR,controlMode:options.controlMode??'left',scope:'Scalar genuine fundamental linear kernel calibration only; beta changes core background on a fixed radial map.'}};
}
if(process.argv[1]?.endsWith('f6tail_warp_linear.mjs')){
 const args=process.argv.slice(2),arg=k=>{const i=args.indexOf(k);return i<0?null:args[i+1]},cfg=JSON.parse(await fs.readFile(arg('--input'),'utf8')),start=Date.now(),geometry=await createWarpGeometry(cfg.geometry);console.log(JSON.stringify({event:'geometry',stats:geometry.stats,seconds:(Date.now()-start)/1000}));const graphs=buildWarpTailGraphs(geometry,cfg.linear);console.log(JSON.stringify({event:'tails',leftCut:Array.from(graphs.left.graphs[0]),rightCut:Array.from(graphs.right.graphs[0]),leftDetError:graphs.left.maxDeterminantError,rightDetError:graphs.right.maxDeterminantError,seconds:(Date.now()-start)/1000}));const kernel=calibrateWarpCore(geometry,graphs,{...cfg.kernel,progress:e=>console.log(JSON.stringify({event:'kernel',...e}))});
 const serial={scope:'Actual changed-profile linear-tail graphs and core kernel only. Nonlinear continuation and fixed-final-background audit remain separate.',configuration:cfg,geometry:geometry.stats,graphs:{parameters:graphs.parameters,left:{...graphs.left,graphs:graphs.left.graphs.map(x=>Array.from(x)),gains:graphs.left.gains.map(x=>Array.from(x))},right:{...graphs.right,graphs:graphs.right.graphs.map(x=>Array.from(x)),gains:graphs.right.gains.map(x=>Array.from(x))}},kernel,seconds:(Date.now()-start)/1000};await fs.writeFile(arg('--out'),JSON.stringify(serial,null,2)+'\n');console.log(JSON.stringify({event:'final',converged:kernel.converged,beta:kernel.beta,residual:kernel.normalizedResidual,seconds:serial.seconds}));
}
