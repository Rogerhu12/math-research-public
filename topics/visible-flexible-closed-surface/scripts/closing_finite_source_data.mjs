// Preserve the actual finite source valley values as explicit decimal parameters.
// Choosing these finitely many values does not constrain the unchanged exact deep root sequence.
import fs from 'node:fs/promises';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
const input=process.argv[2],output=process.argv[3];
if(!input||!output)throw Error('Usage: config.json output.json');
const config=JSON.parse(await fs.readFile(input,'utf8')),f=createRecalibrationFactory(config);
const finiteCalibrations=f.source.cells.map(c=>({n:c.n,alpha:String(c.cal.alpha),R:String(c.R),delta:String(c.delta),c:String(c.c)}));
await fs.writeFile(output,JSON.stringify({scope:'The displayed finite alpha decimals may be taken as exact parameters. All n>=protectCell exact roots remain as in the deep-source theorem; finite alpha choices do not alter port jets.',config,finiteCalibrations},null,2)+'\n');
console.log(JSON.stringify({output,finiteCells:finiteCalibrations.length}));
