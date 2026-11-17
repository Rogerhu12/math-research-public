// Recover fixed physical background constants; no nonlinear tail flow is run.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
const [sourceArg, checkpointArg, outArg] = process.argv.slice(2);
if (!sourceArg || !checkpointArg || !outArg) throw Error('SOURCE_TOPIC CHECKPOINT OUTPUT');
const source = path.resolve(sourceArg), checkpoint = path.resolve(checkpointArg);
const bytes = fs.readFileSync(checkpoint);
const record = JSON.parse((checkpoint.endsWith('.gz') ? gunzipSync(bytes) : bytes).toString());
const cp = record.response?.checkpoint ?? record.checkpoint ?? record;
process.env.CLOSING_TAIL_CACHE = path.join(source, 'repro/source-root/topics/large-amplitude-twist-flex/scripts');
const factoryPath = path.join(source, 'scripts/closing_weighted_tail.mjs');
const {createRecalibrationFactory} = await import(pathToFileURL(factoryPath));
const factory = createRecalibrationFactory(record.config ?? cp.parameters);
const physical = factory.assemble();
const cells = factory.source.cells.map(c => ({n:c.physicalIndex, delta:c.delta,
  R:c.R, c:c.c, lengthScale:c.lengthScale, calibrationAlpha:c.cal.alpha}));
const sha = x => createHash('sha256').update(x).digest('hex');
const result = {scope:'Fixed physical background constants; not nonlinear state or a continuous integration certificate.',
  checkpoint, checkpoint_sha256:sha(bytes), factory_sha256:sha(fs.readFileSync(factoryPath)),
  parameters:physical.parameters, physicalStats:physical.stats, cells,
  calibrationAlphaMin:Math.min(...cells.map(c=>c.calibrationAlpha)),
  calibrationAlphaMax:Math.max(...cells.map(c=>c.calibrationAlpha))};
fs.writeFileSync(outArg, JSON.stringify(result)+'\n');
console.log(JSON.stringify({alpha:physical.stats.alpha, minimumWarpWidth:physical.stats.minimumWarpWidth,
  height:physical.stats.heightSpan, calibrationAlphaMin:result.calibrationAlphaMin,
  calibrationAlphaMax:result.calibrationAlphaMax, sha256:sha(fs.readFileSync(outArg))}));
