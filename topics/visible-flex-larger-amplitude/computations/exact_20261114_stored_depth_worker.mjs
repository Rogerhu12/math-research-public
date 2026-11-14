// Fixed stored metric, fixed complete cut H, and physical-depth refinement.
// The new remesher only constructs an initial guess. The original full
// nonlinear equations, line search, tolerance and requested audit remain.
import fs from 'node:fs';
import crypto from 'node:crypto';

const originalURL = new URL('./tail_frozen_worker.mjs', import.meta.url);
const depthURL = new URL('./closure_depth_warm_remesh.mjs', import.meta.url);
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
let source = fs.readFileSync(originalURL, 'utf8');
const insertion = `
replaceOnce('const embedded=geometricWarmRemesh(prior,dn,createFastSplitFluxMomentumTailEngine);',
  'const embedded=(old.physicalDepth??old.depth)===cfg.depth?geometricWarmRemesh(prior,dn,createFastSplitFluxMomentumTailEngine):depthWarmRemesh(prior,dn,createFastSplitFluxMomentumTailEngine);');
`;
const anchor = 'const importRedirects=[];';
if (source.split(anchor).length !== 2) throw Error('Original stored worker anchor changed');
source = source.replace(anchor, insertion + anchor);
const second = 'source=`import {actualSlopeJacobian,replaceFirstSlopeRows} from';
if (source.split(second).length !== 2) throw Error('Original stored worker imports changed');
source = source.replace(second,
  'source=`import {depthWarmRemesh} from ' + JSON.stringify(depthURL.href) + ';\\n`+\n' +
  '`import {actualSlopeJacobian,replaceFirstSlopeRows} from');
source = source.replaceAll('import.meta.url', JSON.stringify(originalURL.href));
const record = {
  name: 'same-stored-metric-depth-only-initial-guess-v1',
  storedWorkerSha256: sha(fs.readFileSync(originalURL)),
  depthWarmSha256: sha(fs.readFileSync(depthURL)),
  selfSha256: sha(fs.readFileSync(new URL(import.meta.url))),
  transformedSha256: sha(source),
  mathematicalChange: 'Only extend the finite nonlinear physical depth; all fixed metric parameters and cut H retained.',
  unchanged: ['original stored metric factory', 'original complete equations',
    'original solve tolerance', 'original line search', 'requested complete finite audit'],
};
if (process.env.EXACT_DEPTH_ADAPTER_RECORD)
  fs.writeFileSync(process.env.EXACT_DEPTH_ADAPTER_RECORD, JSON.stringify(record,null,2)+'\n', {flag:'wx'});
try {
  await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));
} catch (error) {
  console.error(String(error?.stack??error).replace(
    /data:text\/javascript;base64,[A-Za-z0-9+/=]+/g, '<stored-depth-worker>'));
  process.exitCode=1;
}
