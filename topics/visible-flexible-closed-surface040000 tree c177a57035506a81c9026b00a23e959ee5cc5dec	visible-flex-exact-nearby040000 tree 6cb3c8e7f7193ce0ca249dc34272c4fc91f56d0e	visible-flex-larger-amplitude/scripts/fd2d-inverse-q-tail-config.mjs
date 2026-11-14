// Close one inverse-Q physical input and evaluate the actual complete tail.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {createRecalibrationFactory} from './fd2d-inverse-q-tail.mjs';
import {appendUnchangedDeepSource} from './fd2d-gc-tail-deep-extension.mjs';
const [baseFile,candidateFile,out]=process.argv.slice(2);
if(!baseFile||!candidateFile||!out)throw Error('base-config candidate-json output-prefix');
const hash=x=>crypto.createHash('sha256').update(x).digest('hex'),read=f=>JSON.parse(fs.readFileSync(f,'utf8')),
  base=read(baseFile),candidate=read(candidateFile),exact=candidate.exact_definition,
  rational=s=>{const [a,b='1']=s.split('/');return Number(a)/Number(b);},
  rCut=rational(exact.right_rational),wCut=rational(exact.outer_w_rational),
  rCuff=base.rCut-base.orientation*base.width;
const output=out+'-config.json',reportFile=out+'-provider-report.json';
if(fs.existsSync(output)||fs.existsSync(reportFile))throw Error('Unused output prefix required');
if(exact.inner_reference_config_sha256!==hash(fs.readFileSync(baseFile)))
  throw Error('Candidate is bound to a different original physical tail');
const cfg={...base,schema:'fd2d-inverse-q-full-tail-v1',rCut,wCut,width:rCut-rCuff,
  baseConfig:base,inverseQCandidate:candidate,inverseQQuadratureGrid:1024,inverseQPiecesPerCell:9,
  definitionFileBindings:{base:{file:path.basename(baseFile),sha256:hash(fs.readFileSync(baseFile))},
    candidate:{file:path.basename(candidateFile),sha256:hash(fs.readFileSync(candidateFile))}},
  design_label:'New inverse-Q outer buffer with unchanged original finite interior and deep source',
  calibration_status:'Integral-defined inverse-Q buffer; its actual complete m2 response and nonlinear DN must be recomputed'};
fs.writeFileSync(output,JSON.stringify(cfg,null,2)+'\n');
const started=Date.now(),factory=createRecalibrationFactory(cfg),tail=factory.assemble(),
  extended=appendUnchangedDeepSource(tail,196),N=exact.replace_outer_cells,
  pointJet=g=>({r:g.r,w:Math.exp(g.logw),wr:Math.exp(g.logw)*g.dlogwdx/g.drdx}),
  join=pointJet(tail.cells[N-1].profiles[0](0)),inner=pointJet(tail.cells[N].profiles.at(-1)(1)),
  cut=pointJet(tail.cells[0].profiles.at(-1)(1));
const report={schema:'fd2d-inverse-q-tail-provider-report-v1',
  scope:'Actual floating constructor and exact-source identity check. This is not a nonlinear solution or a continuous metric/reach certificate.',
  generator_sha256:hash(fs.readFileSync(new URL(import.meta.url))),config_file:path.basename(output),
  config_sha256:hash(fs.readFileSync(output)),
  physical_definition_sha256:tail.parameters.inverseQDefinitionSHA256,
  source_files:tail.parameters.inverseQDefinition.sources,
  original_source_object_preserved:tail.source===factory.source,
  cells:tail.cells.length,replace_outer_cells:N,source_cells:tail.source.cells.length,
  old_inner_port:inner,new_inner_port:join,cut,stats:tail.stats,
  actual_deep_extension:extended.deepExtension,
  physical_identity_embedded_in_parameters:true,
  caveat:'w and w_r agree at the physical join; w_rr is not constrained and is a third derivative of the meridian immersion.',
  seconds:(Date.now()-started)/1000};
fs.writeFileSync(reportFile,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({config:output,config_sha256:report.config_sha256,
  definition_sha256:report.physical_definition_sha256,stats:tail.stats,
  deep_source_identity_preserved:true,seconds:report.seconds}));
