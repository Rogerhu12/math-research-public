/** Finite floating design check, not a continuous certificate. */
import fs from 'node:fs';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {createInverseQBuffer} from './fd2d-metric-inverse-q-buffer.mjs';

const args=process.argv.slice(2),opts={};
for(let j=0;j<args.length;j+=2)opts[args[j].replace(/^--/,'')]=args[j+1];
if(!opts.candidate||!opts.output)throw new Error('Require --candidate PATH --output PATH');
const grid=Number(opts.grid??1024),checkGrid=Number(opts['check-grid']??512),N=Number(opts.nodes??4096);
const sha=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const d=JSON.parse(fs.readFileSync(opts.candidate)),began=performance.now();
const f=createInverseQBuffer(d,{grid}),g=createInverseQBuffer(d,{grid:checkGrid});
let bg=0,bgCircular=0,Gamma=0,II=0,defect=0,diff=0,wmax=0,height=0,meridian=0;
const where={};let previous;
for(let j=0;j<=N;j++) {
  const t=j/N,z=f.evaluate(t),q=g.evaluate(t);
  if(Math.abs(z.backgroundMeridionalCurvature)>bg){bg=Math.abs(z.backgroundMeridionalCurvature);where.bg=t;}
  bgCircular=Math.max(bgCircular,Math.abs(z.backgroundCircularCurvature));
  if(Math.abs(z.referenceGamma)>Gamma){Gamma=Math.abs(z.referenceGamma);where.Gamma=t;}
  if(z.referenceIIRow>II){II=z.referenceIIRow;where.II=t;}
  defect=Math.max(defect,Math.abs(z.referenceLinearEquationDefect));
  diff=Math.max(diff,Math.abs(z.logw-q.logw));wmax=Math.max(wmax,z.w);
  if(previous){const dr=z.r-previous.r;height+=dr*(z.w+previous.w)/2;meridian+=dr*(Math.sqrt(z.E)+Math.sqrt(previous.E))/2;}
  previous=z;
}
const provider=fileURLToPath(new URL('./fd2d-metric-inverse-q-buffer.mjs',import.meta.url));
const out={scope:'Floating local provider check; no continuous/global nonlinear certificate',
  candidate:{path:opts.candidate,sha256:sha(opts.candidate)},
  checker:{path:fileURLToPath(import.meta.url),sha256:sha(fileURLToPath(import.meta.url))},
  provider:{path:provider,sha256:sha(provider)},metadata:f.metadata,
  ports:[f.evaluate(0),f.evaluate(1)],sampled:{nodes:N+1,
    maxBackgroundMeridionalCurvature:bg,maxBackgroundCircularCurvature:bgCircular,
    maxReferenceGamma:Gamma,maxReferenceIIRow:II,maxReferenceEquationDefect:defect,
    maxLogwDifferenceBetweenQuadratureGrids:diff,wmax,heightTrapezoid:height,meridianTrapezoid:meridian,
    sampledBackgroundBelow7:Math.max(bg,bgCircular)<7,where},seconds:(performance.now()-began)/1000};
if(d.solver?.deep_coefficients){
  out.sampled.unchangedDeepGammaProxy=d.solver.deep_coefficients.CG*f.metadata.gamma;
  out.sampled.unchangedDeepIIProxy=d.solver.deep_coefficients.CII*f.metadata.gamma;
}
fs.writeFileSync(opts.output,JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({path:opts.output,sha256:sha(opts.output),metadata:out.metadata,sampled:out.sampled,seconds:out.seconds}));
