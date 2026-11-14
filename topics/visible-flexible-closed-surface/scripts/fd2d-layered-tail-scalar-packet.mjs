// Read-only scalar definition packet for the finitely modified physical tail.
// The finite source calibration constants are frozen binary64 data; this
// does not impose their finite T21 residual as an exact infinite-tail root.
import fs from 'node:fs';
import crypto from 'node:crypto';
import path from 'node:path';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
const [input,output]=process.argv.slice(2);
if(!input||!output||fs.existsSync(output))throw Error('config unused-output required');
const hash=f=>crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex'),cfg=JSON.parse(fs.readFileSync(input,'utf8'));
const factory=createRecalibrationFactory(cfg),alpha=factory.source.cells.map(c=>c.cal.alpha);
if(alpha.some(x=>!(x>=.5&&x<=2)))throw Error('finite alpha bracket failed');
const packet={schema:'fd2d-layered-tail-frozen-scalar-definition-v1',
 config_file:path.basename(input),config_sha256:hash(input),config:cfg,
 generator_sha256:hash(new URL(import.meta.url)),base_constructor_sha256:hash(new URL('./closing_recalibrated_tail.mjs',import.meta.url)),
 weighted_constructor_sha256:hash(new URL('./closing_weighted_tail.mjs',import.meta.url)),
 finite_source_alphas:alpha,finite_alpha_minimum:Math.min(...alpha),finite_alpha_maximum:Math.max(...alpha),
 semantics:'Finite n<160 alpha and beta entries are exact binary64 constants for their continuous real formulas. Radii/lengths follow the original exact geometric source formulas and cap interpolation follows the declared levels. n>=160 remains the original exactly calibrated infinite source; no rounded finite source alpha is substituted there.',
 parameters:{delta0:.006,R:64,a:2.75,etaPower:1.5,etaRatioAtN0:.05,rCuff:.32,rCut:cfg.rCut,wCut:cfg.wCut,
  curvatureBound:7,capTransition:2,slopeCap:.004,protectCell:cfg.protectCell},
 scope:'Definition/export only. Positive warp and all actual nonlinear/metric/reach claims require their own certificates.'};
fs.writeFileSync(output,JSON.stringify(packet,null,2)+'\n');console.log(JSON.stringify({output,sha256:hash(output),alphaMin:packet.finite_alpha_minimum,alphaMax:packet.finite_alpha_maximum}));
