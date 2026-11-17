// Probe local flow-relaxation initial guesses for an already failed tail.
// This is not the one-ULP retry. All equations, scales, root guards and the
// original full DN solve/audit are unchanged; only free internal states move.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync, gzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';

const [topic, input, provenance, outputRecord, outputSummary, sparseHelper] = process.argv.slice(2);
if (!sparseHelper || !fs.existsSync(sparseHelper)) throw Error('Original sparse helper required');
for (const key of ['OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS']) process.env[key] = '1';
process.env.VISIBLE_FLEX_SPARSE_LINEAR_HELPER = path.resolve(sparseHelper);
const sha = p => createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const record = JSON.parse(gunzipSync(fs.readFileSync(input)));
const prior = JSON.parse(fs.readFileSync(provenance));
if (sha(input) !== prior.output_record_sha256 || prior.originalSolverConverged !== false)
  throw Error('Expected the complete previously recorded failed candidate');
for (const [file, digest] of Object.entries(prior.source_sha256))
  if (sha(file) !== digest) throw Error('Recorded source differs: ' + file);
const source = path.join(topic, 'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT = source;
process.env.CLOSING_TAIL_CACHE = path.join(source, 'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory} = await import(pathToFileURL(path.join(topic, 'scripts/closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN} = await import(pathToFileURL(path.join(topic, 'scripts/950f-tail-stage-split.mjs')));
const cfg = record.config, cp = record.response.checkpoint;
if (!cp?.states || !cp?.cutHeight || !record.response.failed) throw Error('Complete failed state required');
const physical = createRecalibrationFactory(cfg).assemble();
const dn = createSplitFluxCompactTailDN({...cfg, tail: physical});
const M = cfg.modes, K = 2*M, N = dn.tail.cells.length;
const states = cp.states.map(v => Float64Array.from(v));
if (states.length !== N+1 || states.some(v => v.length !== K)) throw Error('Original complete grid required');
const clone = values => values.map(v => Float64Array.from(v));
const radius = dn.tail.cells[0].profiles.at(-1)(1).r;
const target = Float64Array.from(cp.cutHeight, v => v/radius**4);
const scales = new Float64Array(N+1);
scales[0] = Math.max(1e-250, ...Array.from(target, Math.abs));
for (let n = 0; n < N; n++) scales[n+1] = scales[n]/Math.abs(dn.tail.gains[n][0]);
const began = performance.now();
const original = dn.tail.evaluate(states, target, true, scales);
if (original.norm !== prior.last_original_iteration.norm) throw Error('Original full replay no longer matches');
const originalResiduals = original.residuals.map(v => Float64Array.from(v));
const stageNorms = originalResiduals.map((row,n) => Math.max(...Array.from(row, v => Math.abs(v)/scales[n])));
let peak = {stage: -1, component: -1, norm: 0};
for (let n = 2; n < N; n++) for (let j = 0; j < K; j++) {
  const norm = Math.abs(originalResiduals[n][j])/scales[n];
  if (norm > peak.norm) peak = {stage: n, component: j, norm};
}
if (peak.norm !== original.norm || peak.stage < 2) throw Error('The dominant residual must be internal');
const n = peak.stage, j = peak.component;
const endNorm = Math.max(...Array.from(original.end, v => Math.abs(v)/scales[N]));
const untouched = Math.max(endNorm, ...stageNorms.filter((_,i) => i < n-2 || i > n));
const before = {norm: original.norm, minA: original.minA, minD: original.minD,
  peak: {...peak, signedResidual: originalResiduals[n][j], state: states[n][j],
    flow: original.flows[n].out[j], scale: scales[n]}};

function local(index, values) {
  const cell = dn.tail.cells[index], x = new Float64Array(K+2);
  x.set(values[index+1]);
  const flow = cell.engine.flowStateWithJacobian(x, cell.profiles, {stepsPerSegment: cfg.steps});
  const out = Float64Array.from(flow.state.slice(0,K), (v,k) => k < M ? v : v/cell.portRatio);
  let norm = 0, component = -1;
  for (let k = 0; k < K; k++) {
    const r = Math.abs(out[k]-values[index][k])/scales[index];
    if (r > norm) { norm = r; component = k; }
  }
  return {index, out, norm, component, minA: flow.minA, minD: flow.minD};
}
function slim(row) { return {stage: row.index, norm: row.norm, component: row.component,
  minA: row.minA, minD: row.minD}; }
const alphas = [1/8, 1/4, 5/16, 1/3, 3/8, 1/2, 3/4, 1];
const betas = [1/8, 1/4, 1/2, 3/4, 1];
const trials = [];
let best = {norm: before.norm, states: clone(states), changes: [], alpha: 0, beta: 0};
function consider(values, alpha, beta, rows, changes) {
  const norm = Math.max(untouched, ...rows.map(r => r.norm));
  const trial = {alpha, beta, norm, changes, affected: rows.map(slim)};
  trials.push(trial);
  if (norm < best.norm) best = {...trial, states: clone(values)};
}
for (const alpha of alphas) {
  const values = clone(states);
  values[n][j] = states[n][j] + alpha*before.peak.signedResidual;
  if (values[n][j] === states[n][j]) continue;
  const a = local(n-2, values), b = local(n-1, values), c = local(n, values);
  const changes = [{stage:n, component:j, before:states[n][j], after:values[n][j]}];
  consider(values, alpha, 0, [a,b,c], changes);
  // A second backward relaxation is useful only when the downstream row
  // can already pass; it cannot change that row's state or incoming flow.
  if (c.norm > cfg.solveTolerance || b.norm <= cfg.solveTolerance || b.component < 0) continue;
  const k = b.component, residual = b.out[k]-values[n-1][k];
  for (const beta of betas) {
    const pair = clone(values);
    pair[n-1][k] = states[n-1][k] + beta*residual;
    if (pair[n-1][k] === states[n-1][k]) continue;
    const aa = local(n-2, pair), bb = local(n-1, pair);
    consider(pair, alpha, beta, [aa,bb,c], [...changes,
      {stage:n-1, component:k, before:states[n-1][k], after:pair[n-1][k]}]);
  }
}
const summary = {scope: 'Local internal flow-relaxation candidates followed, only if improved, by the unchanged original complete DN solve and audit. This is not a one-ULP retry or a prefix solution.',
  command: process.argv, input_sha256: sha(input), prior_record_sha256: sha(provenance),
  source_sha256: {...prior.source_sha256, [path.resolve(process.argv[1])]:sha(process.argv[1]),
    [path.resolve(sparseHelper)]:sha(sparseHelper)},
  original_gate: cfg.solveTolerance, before, alphas, betas, local_trial_count:trials.length,
  local_trials:trials, selected:{alpha:best.alpha,beta:best.beta,local_predicted_norm:best.norm,changes:best.changes},
  all_physical_and_solver_parameters_unchanged:true};
console.log(JSON.stringify({event:'initial_candidate',before:before.norm,...summary.selected,local_trials:trials.length}));
const whole = dn.tail.evaluate(best.states, target, true, scales);
summary.full_candidate_replay = {norm:whole.norm,minA:whole.minA,minD:whole.minD};
let response = null, progressStates = null, progressRow = null;
if (!(whole.norm < before.norm)) {
  summary.original_solver_invoked = false;
  summary.reason = 'No strict original full-residual improvement; unchanged failed state is not solved again.';
} else {
  summary.original_solver_invoked = true;
  try {
    const sol = dn.solve(cp.cutHeight, {initial:best.states, maxIterations:cfg.maxIterations,
      tolerance:cfg.solveTolerance, jacobian:true, audit:true, auditSteps:cfg.auditSteps??cfg.steps,
      progress:(row,values)=>{ if(values){progressStates=values;progressRow=row;}
        console.log(JSON.stringify({event:'original_solve_iteration',...row})); }});
    const checkpoint = {parameters:sol.parameters,states:sol.states,rawNode:dn.tail.rawNode,
      rawStates:dn.tail.rawNode.map(k=>sol.states[k]),cutHeight:cp.cutHeight,
      scope:'Unchanged original finite DN solver output with its full audit; no prefix or closed surface acceptance.'};
    response = {converged:sol.converged,residual:sol.normalizedResidual,jets:sol.jets,
      heightJetJacobian:sol.heightJetJacobian??null,history:sol.history,audit:sol.audit,checkpoint};
    summary.original_solver_converged = sol.converged; summary.final_residual = sol.normalizedResidual;
    summary.final_minA = sol.minA; summary.final_minD = sol.minD;
    summary.audit = sol.audit; summary.history = sol.history;
  } catch(error) {
    response = {failed:String(error),lastIteration:progressRow,checkpoint:progressStates?{
      parameters:dn.tail.parameters,states:progressStates,rawNode:dn.tail.rawNode,
      rawStates:dn.tail.rawNode.map(k=>progressStates[k]),cutHeight:cp.cutHeight,
      scope:'Failed unchanged original solve from a local-relaxation initial candidate.'}:null};
    summary.original_solver_converged = false; summary.error = String(error);
  }
}
const result = {request:{height:cp.cutHeight,jacobian:true,audit:true}, response,config:cfg,
  source_sha256:record.source_sha256,execution_source_sha256:summary.source_sha256,
  numerical_initialization:summary.selected,
  scope:'Original DN result from an explicitly new local initial-state relaxation; no equations or gates changed.'};
fs.writeFileSync(outputRecord,gzipSync(JSON.stringify(result)+'\n'));
summary.output_record_sha256=sha(outputRecord); summary.seconds=(performance.now()-began)/1000;
fs.writeFileSync(outputSummary,JSON.stringify(summary,null,2)+'\n');
console.log(JSON.stringify({event:'terminal',invoked:summary.original_solver_invoked,
  converged:summary.original_solver_converged,residual:summary.final_residual,
  error:summary.error,seconds:summary.seconds,output_record_sha256:summary.output_record_sha256}));
