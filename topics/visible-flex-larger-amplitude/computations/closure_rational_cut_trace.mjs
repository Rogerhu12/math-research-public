// Linear full-state chart diagnostics for the separately frozen rational tail.
// It never replaces a nonlinear tail response or an old fixed-metric result.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {createRationalDeepTail} from './closure_rational_tail_model.mjs';

const argv=process.argv.slice(2),opt=(name,def=null)=>{
  const i=argv.indexOf('--'+name);return i<0?def:argv[i+1];
};
const entrypointSHA256=crypto.createHash('sha256').update(fs.readFileSync(new URL(import.meta.url))).digest('hex');
const portPath=opt('port'),out=opt('out');
if(!portPath||!out)throw Error('Usage: --port port.json --out report.json [--modes 46 --steps 1024 --far 176,192 --source-topic path]');
const packet=JSON.parse(fs.readFileSync(portPath,'utf8'));
const parameters=packet.parameters??packet;
const modes=Number(opt('modes',46)),steps=Number(opt('steps',1024));
const fars=opt('far','176,192').split(',').map(Number);
const model=await createRationalDeepTail(parameters,{sourceTopic:opt('source-topic')??process.env.VISIBLE_FLEX_SOURCE_TOPIC});
if(fars.some(n=>!Number.isInteger(n)||n<=model.start))throw Error('Each far truncation must lie strictly inside the rational region');
if(!(modes>=1&&modes<=46&&Number.isInteger(modes)))throw Error('Choose 1..46 modes of the R15 chart');
const SQRT12=Math.sqrt(12),cut=model.cell(0).profiles.at(-1)(1),wCut=Math.exp(cut.logw);
const modeRows=Array.from({length:modes},(_,k)=>({mode:2*(k+1),nu:(k+1)**2*(4*(k+1)**2-1)/3}));
function solveAll(far){
  const ys=modeRows.map(z=>[1,model.idealModeGraph(z.mode,64,2.75)]);
  const logScales=new Float64Array(modes),minQ=new Float64Array(modes).fill(1),minWhere=new Int32Array(modes).fill(far);
  let lastMu=model.cell(far-1).mu;
  for(let n=far-1;n>=0;n--){
    const cell=model.cell(n),logMu=Math.log(cell.mu),ratio=lastMu/cell.mu;lastMu=cell.mu;
    for(const y of ys)y[1]*=ratio;
    const geometry=g=>{const lr=Math.log(g.r);return [SQRT12*g.drdx*Math.exp(logMu-8*lr-g.logw),
      -SQRT12*g.drdx*Math.exp(6*lr+g.logw-logMu),g.drdx/g.r];};
    for(const profile of cell.profiles)for(let k=0;k<steps;k++){
      const x=k/steps,h=1/steps,g0=geometry(profile(x)),gm=geometry(profile(x+h/2)),g1=geometry(profile(x+h));
      for(let j=0;j<modes;j++){
        const y=ys[j],z=modeRows[j],l=z.mode*z.mode-4,v=z.nu,u0=y[0],v0=y[1];
        const a0=l*g0[2]*u0+g0[0]*v0,a1=v*g0[1]*u0-l*g0[2]*v0;
        const u1=u0+h*a0/2,v1=v0+h*a1/2,b0=l*gm[2]*u1+gm[0]*v1,b1=v*gm[1]*u1-l*gm[2]*v1;
        const u2=u0+h*b0/2,v2=v0+h*b1/2,c0=l*gm[2]*u2+gm[0]*v2,c1=v*gm[1]*u2-l*gm[2]*v2;
        const u3=u0+h*c0,v3=v0+h*c1,d0=l*g1[2]*u3+g1[0]*v3,d1=v*g1[1]*u3-l*g1[2]*v3;
        y[0]=u0+h*(a0+2*b0+2*c0+d0)/6;y[1]=v0+h*(a1+2*b1+2*c1+d1)/6;
      }
    }
    for(let j=0;j<modes;j++){
      const y=ys[j],norm=Math.hypot(...y);
      if(!(norm>0&&Number.isFinite(norm)))throw Error('Nonfinite trace: mode '+modeRows[j].mode+', cell '+n);
      y[0]/=norm;y[1]/=norm;logScales[j]+=Math.log(norm);
      if(Math.abs(y[0])<minQ[j]){minQ[j]=Math.abs(y[0]);minWhere[j]=n;}
    }
    if(n%32===0)process.stderr.write(JSON.stringify({far,cellReached:n,modes,steps})+'\n');
  }
  return modeRows.map((z,j)=>{
    const {mode,nu}=z,y=ys[j],rawXi=model.cell(0).mu*y[1]/(cut.r**7*wCut);
    const preconditioned=[y[0],rawXi/nu],pnorm=Math.hypot(...preconditioned),projective=preconditioned.map(x=>x/pnorm);
    if(projective.find(x=>x!==0)<0)for(let k=0;k<2;k++)projective[k]*=-1;
    const height=cut.r**4*y[0],heightDerivative=cut.r**3*(mode*mode*y[0]+SQRT12*rawXi);
    return {mode,far,steps,normalizedCanonicalColumn:y,normalizedRawColumn:[y[0],rawXi],preconditionedProjectiveColumn:projective,
      preferredCoordinate:Math.abs(projective[0])>=Math.abs(projective[1])?'height':'raw-momentum/nu',
      cutSlope:height===0?null:heightDerivative/height,
      logAbsoluteHeightGain:logScales[j]+Math.log(Math.abs(height)),
      minimumNormalizedCanonicalHeight:minQ[j],smallestHeightCell:minWhere[j]};
  });
}
const runs=[];
for(const far of fars){
  const rows=solveAll(far);
  runs.push({far,rows});
}
const comparisons=[];
for(let k=1;k<runs.length;k++){
  const old=runs[k-1],cur=runs[k];
  comparisons.push({from:old.far,to:cur.far,rows:cur.rows.map((r,j)=>{
    const q=old.rows[j];
    const a=q.preconditionedProjectiveColumn,b=r.preconditionedProjectiveColumn;
    return {mode:r.mode,projectiveDistance:Math.hypot(a[0]-b[0],a[1]-b[1]),
      absoluteSlopeDifference:r.cutSlope===null||q.cutSlope===null?null:Math.abs(r.cutSlope-q.cutSlope),
      relativeSlopeDifference:r.cutSlope===null||q.cutSlope===null?null:
        Math.abs(r.cutSlope-q.cutSlope)/Math.max(1,Math.abs(r.cutSlope),Math.abs(q.cutSlope))};
  })});
}
const frozen=model.assertFrozenHead();
const report={status:'finite numerical linear trace; new fixed rational-deep metric',
  entrypointSHA256,
  peakRSSKiB:process.resourceUsage().maxRSS,
  sourcePort:path.resolve(portPath),sourcePortSHA256:crypto.createHash('sha256').update(fs.readFileSync(portPath)).digest('hex'),
  modes,steps,fars,cut:{radius:cut.r,slope:wCut},model:model.manifest,shallowHeadPreserved:frozen,
  runs,comparisons,
  limits:['No nonlinear trace has been evaluated.','Depth comparisons do not bound radial integration error.',
    'The deep rational profile and the old all-stored profile are distinct metrics.',
    'The exact R15 nonlinear smallness gates and shallow analytic propagation remain unpaid.']};
fs.mkdirSync(path.dirname(out),{recursive:true});fs.writeFileSync(out,JSON.stringify(report,null,2)+'\n');
process.stdout.write(JSON.stringify({out,modes,steps,fars,shallowHeadPreserved:frozen,
  comparisonMaxima:comparisons.map(c=>({from:c.from,to:c.to,
    projective:Math.max(...c.rows.map(r=>r.projectiveDistance)),
    relativeSlope:Math.max(...c.rows.map(r=>r.relativeSlopeDifference??0))})),
  endpoint:model.manifest.endpointCheck})+'\n');
