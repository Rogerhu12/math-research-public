// Original constructor/linear-graph metadata only. No nonlinear solve or native
// integration is invoked. The actual complete J is read separately by Python.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import {pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
const [sourceTopic, packetPath, targetPath, outputPath] = process.argv.slice(2);
if(!outputPath)throw Error('source-topic packet target-height-json output-json required');
const source=path.resolve(sourceTopic),scripts=path.join(source,'scripts');
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(source,'repro/source-root');
process.env.CLOSING_TAIL_CACHE=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts');
const manifest=path.join(source,'native-manifest.json');
process.env.VISIBLE_FLEX_NATIVE_MANIFEST=manifest;
process.env.VISIBLE_FLEX_NATIVE_MANIFEST_SHA256=createHash('sha256').update(fs.readFileSync(manifest)).digest('hex');
const packet=JSON.parse(zlib.gunzipSync(fs.readFileSync(packetPath)).toString());
const cfg=packet.config,cp=packet.response.checkpoint,desired=JSON.parse(fs.readFileSync(targetPath));
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(scripts,'closing_weighted_tail.mjs')));
const {createNativeCompactTailDN}=await import(pathToFileURL(path.join(scripts,'native_batch_factory.mjs')));
const physical=createRecalibrationFactory(cfg).assemble();
const dn=createNativeCompactTailDN({...cfg,tail:physical}),M=cfg.modes,K=2*M,L=dn.tail.cells.length;
if(cp.states.length!==L+1||cp.states.some(row=>row.length!==K)||desired.length!==M)
 throw Error('Complete original finite state/target dimensions required');
for(const name of ['modes','spacing','depth','physicalDepth','shootingParts'])
 if(cp.parameters[name]!==dn.tail.parameters[name])throw Error('Original constructor dimension changed: '+name);
const radius=dn.tail.cells[0].profiles.at(-1)(1).r,r4=radius**4;
const target=packet.request.height.map(x=>x/r4),desiredTarget=desired.map(x=>x/r4);
const scales=Array(L+1).fill(0),gains0=dn.tail.gains.map(row=>row[0]);
scales[0]=Math.max(1e-250,...target.map(Math.abs));
for(let n=0;n<L;n++)scales[n+1]=scales[n]/Math.abs(gains0[n]);
if(!scales.every(x=>Number.isFinite(x)&&x>0)||!desiredTarget.every(Number.isFinite))
 throw Error('Nonfinite original scaling or complete target');
const result={scope:'Original frozen constructor and all-node first-mode scales; no nonlinear state/root integration or full J computed',
 M,K,depth:L,radius,r4,scales,gains0,deepGraph:Array.from(dn.tail.graphs[L]),
 originalTarget:target,desiredTarget,rawNode:dn.tail.rawNode,
 portRatios:dn.tail.cells.map(cell=>cell.portRatio),nonlinear_solve_invoked:false,native_evaluate_invoked:false};
fs.writeFileSync(outputPath,JSON.stringify(result)+'\n',{flag:'wx'});
console.log(JSON.stringify({M,K,depth:L,output:outputPath,nonlinear_solve_invoked:false}));
