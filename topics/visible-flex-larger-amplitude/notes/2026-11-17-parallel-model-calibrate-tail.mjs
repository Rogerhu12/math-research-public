// Actual weighted-source valley calibration for the new orientation -1 tail.
// Design experiment only: changes the metric and does not certify a closed flex.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';

const arg=process.argv.slice(2),get=(k,d=null)=>{const i=arg.indexOf(k);return i<0?d:arg[i+1];};
const source=path.resolve(get('--source')),input=path.resolve(get('--input')),output=path.resolve(get('--out'));
const depth=Number(get('--depth','4')),steps=Number(get('--steps','128')),passes=Number(get('--passes','0'));
const far=Number(get('--far',String(depth)));
const frequencies=JSON.parse(get('--modes','[2,4,6,8]'));
process.env.CLOSING_TAIL_CACHE=path.join(source,'repro/source-root/topics/large-amplitude-twist-flex/scripts');
const weighted=await import(pathToFileURL(path.join(source,'scripts/closing_weighted_tail.mjs')).href);
const original=JSON.parse(fs.readFileSync(input,'utf8'));
const cfg={...original.parameters},controls=Array.from(cfg.valleyControls??[]);
if(get('--all-beta')!==null){const b=Number(get('--all-beta'));for(let i=0;i<controls.length;i++)controls[i]=b;}
if(get('--controls')!==null){const c=JSON.parse(get('--controls'));for(let i=0;i<c.length;i++)controls[i]=c[i];}
if(get('--pulse0')!==null)cfg.pulseCaps=[[Number(get('--pulse0')),Number(get('--pulse1','.02'))]];
if(get('--valley0')!==null)cfg.valleyCaps=[Number(get('--valley0'))];
if(get('--prefix-r')!==null)cfg.prefixR=Number(get('--prefix-r'));
if(get('--slope-cap')!==null)cfg.slopeCap=Number(get('--slope-cap'));
if(get('--weights0')!==null)cfg.warpWeightLevels=[JSON.parse(get('--weights0'))];
if(get('--config-patch')!==null)Object.assign(cfg,JSON.parse(get('--config-patch')));
const factory=weighted.createRecalibrationFactory(cfg);
let tail=factory.assemble(controls),history=[];
const started=performance.now();

function bridgeCell(tail){
  const end=tail.cells[0].profiles.at(-1)(1),r0=original.cut.r,w0=original.cut.w,wr0=original.cut.w_r;
  const width=end.r-r0,c0=Math.log(w0),c1=width*wr0/w0,A=end.logw-c0-c1,B=width*end.dlogwdx/end.drdx-c1;
  const c=[c0,c1,3*A-B,B-2*A];
  const profile=x=>{const t=1-x,r=end.r-width*x;return {r,drdx:-width,logw:c[0]+t*(c[1]+t*(c[2]+t*c[3])),dlogwdx:-(c[1]+t*(2*c[2]+3*t*c[3]))};};
  return {mu:tail.cells[0].mu,profiles:[profile],coefficients:c};
}

function diagnose(tail){
  const cellRows=[];
  for(let n=0;n<depth;n++){
    const col=weighted.physicalModeColumn(tail.cells[n],2,steps,[1,0]);
    cellRows.push({cell:n,beta:controls[n],rStart:tail.cells[n].rStart,rEnd:tail.cells[n].rEnd,
      ...col});
  }
  const modes=[];
  for(const mode of frequencies){
    let y=[1,tail.parameters.orientation*weighted.idealModeGraph(mode,tail.parameters.R,tail.parameters.a)];
    let lastMu=tail.cells[far-1].mu;
    for(let n=far-1;n>=depth;n--){
      const cell=tail.cells[n];y[1]*=lastMu/cell.mu;lastMu=cell.mu;
      y=weighted.physicalModeColumn(cell,mode,steps,y).column;
      const scale=Math.hypot(...y);y=y.map(v=>v/scale);
    }
    y[1]*=lastMu/tail.cells[depth-1].mu;lastMu=tail.cells[depth-1].mu;
    const deepColumn=Array.from(y);
    const deepPoint=tail.cells[depth-1].profiles[0](0);
    const beta=Math.sqrt(12)*Math.exp(Math.log(lastMu)-7*Math.log(deepPoint.r)-deepPoint.logw)/mode;
    const kp=y[0],pp=mode*y[0]+beta*y[1],norm=Math.hypot(kp,pp);
    const deepBoundary={r:deepPoint.r,logw:deepPoint.logw,mu:lastMu,p:pp/norm,k:kp/norm};
    const samples=[];
    for(let n=depth-1;n>=0;n--){
      const cell=tail.cells[n];y[1]*=lastMu/cell.mu;lastMu=cell.mu;
      const col=weighted.physicalModeColumn(cell,mode,steps,y,(segment,x,g,v)=>{
        samples.push({cell:n,segment,x,r:g.r,w:Math.exp(g.logw),u:v[0],v:v[1],mu:cell.mu});
      });
      y=col.column;
    }
    const bridge=bridgeCell(tail);
    y=weighted.physicalModeColumn(bridge,mode,steps,y,(segment,x,g,v)=>{
      samples.push({cell:-1,segment,x,r:g.r,w:Math.exp(g.logw),u:v[0],v:v[1],mu:bridge.mu});
    }).column;
    const cut=samples.at(-1),Pcut=-mode*cut.r**3*cut.u/cut.w;
    let maxP=0,maxK=0,maxL=0,maxAngularGradient=0,maxRadialHeightDerivative=0,maxW2K=0,whereP=null,whereK=null;
    for(const z of samples){
      const P=-mode*z.r**3*z.u/z.w/Pcut;
      const K=(mode*mode*z.r**3*z.u/z.w+Math.sqrt(12)*z.mu*z.v/(z.r**4*z.w*z.w))/Pcut;
      if(Math.abs(P)>maxP){maxP=Math.abs(P);whereP={cell:z.cell,segment:z.segment,x:z.x,r:z.r,w:z.w,P,K};}
      if(Math.abs(K)>maxK){maxK=Math.abs(K);whereK={cell:z.cell,segment:z.segment,x:z.x,r:z.r,w:z.w,P,K};}
      maxL=Math.max(maxL,Math.abs(K+mode*P));
      maxAngularGradient=Math.max(maxAngularGradient,Math.abs(z.w*P));
      maxRadialHeightDerivative=Math.max(maxRadialHeightDerivative,Math.abs(z.w*K));
      maxW2K=Math.max(maxW2K,Math.abs(z.w*z.w*K));
    }
    modes.push({mode,deepColumn,deepBoundary,Pcut,maxP,maxK,maxL,maxAngularGradient,maxRadialHeightDerivative,maxW2K,whereP,whereK,cut_K_over_P:(mode*mode*cut.r**3*cut.u/cut.w+Math.sqrt(12)*cut.mu*cut.v/(cut.r**4*cut.w*cut.w))/Pcut});
  }
  return {alpha:tail.stats.alpha,stats:tail.stats,cellRows,modes};
}

let initial=diagnose(tail);
console.log(JSON.stringify({event:'initial',...initial}));
for(let pass=0;pass<passes;pass++){
  const priorAlpha=tail.stats.alpha;
  for(let n=depth-1;n>=0;n--){
    const cell=tail.cells[n];
    try{
      const v=weighted.solvePhysicalCell(factory,n,cell.rStart,tail.stats.alpha,
        {steps,tolerance:1e-7,initialBeta:controls[n],limit:40});
      controls[n]=v.beta;
      history.push({pass,cell:n,beta:v.beta,gain:v.gain,residual:v.zeroResidual,evaluations:v.evaluations,trace:v.trace});
      console.log(JSON.stringify({event:'cell',pass,cell:n,beta:v.beta,gain:v.gain,residual:v.zeroResidual,evaluations:v.evaluations}));
    }catch(e){
      history.push({pass,cell:n,error:String(e)});
      console.log(JSON.stringify({event:'cell-error',pass,cell:n,error:String(e).slice(0,1800)}));
    }
  }
  tail=factory.assemble(controls);
  const d=diagnose(tail);history.push({pass,diagnostic:d});
  console.log(JSON.stringify({event:'pass',pass,priorAlpha,alpha:tail.stats.alpha,modes:d.modes,cellRows:d.cellRows}));
}
const final=diagnose(tail),sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const report={scope:'Numerical new-metric valley design on the recovered actual weighted source; finite linear columns and sampled gains only.',
 input_sha256:sha(fs.readFileSync(input)),script_sha256:sha(fs.readFileSync(new URL(import.meta.url))),
 depth,far,steps,passes,seconds:(performance.now()-started)/1000,config:{...cfg,valleyControls:controls},effective_parameters:tail.parameters,initial,history,final};
fs.writeFileSync(output,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({event:'done',seconds:report.seconds,output,alpha:tail.stats.alpha,modes:final.modes}));
