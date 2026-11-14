// Locate full Darboux defects on the saved finite-tail RK audit grid, then
// decompose the complete angular defect at the worst physical and normalized
// points.  This chooses a meaningful next refinement; it is not a proof of
// continuous reach, infinite closure, or a stronger coupled prefix.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';

const [sourceTopic, responseFile, outputFile, rawThroughText] = process.argv.slice(2);
if (!sourceTopic || !responseFile || !outputFile)
  throw Error('Usage: node tail_defect_spectrum.mjs SOURCE_TOPIC RESPONSE.json.gz OUTPUT.json [LAST_RAW_CELL]');
const rawThrough = rawThroughText === undefined ? Infinity : Number(rawThroughText);
if (!(rawThrough === Infinity || (Number.isInteger(rawThrough) && rawThrough >= 0)))
  throw Error('LAST_RAW_CELL must be a nonnegative integer');
const started = Date.now(), sourceRoot = path.join(sourceTopic, 'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT = sourceRoot;
process.env.VISIBLE_FLEX_SOURCE_TOPIC = sourceTopic;
process.env.CLOSING_TAIL_CACHE = path.join(sourceRoot, 'topics/large-amplitude-twist-flex/scripts');
const local = name => pathToFileURL(path.join(sourceTopic, 'scripts', name));
const raw = name => pathToFileURL(path.join(sourceRoot, 'topics/large-amplitude-twist-flex/scripts', name));
const {createStoredPhysical} = await import('./tail_stored_geometry.mjs');
const {createStoredFiniteTailDN, storedEngineManifest} = await import('./tail_stored_engine.mjs');
const {createFourierRootSplitFluxEngine} = await import(local('78718-tail-fourier-root-split-engine.mjs'));
const {createMomentumPhysicalJetEvaluator} = await import(raw('f6tail_momentum_physical_jets.mjs'));
const bytes = fs.readFileSync(responseFile), record = JSON.parse(zlib.gunzipSync(bytes));
if (!record.response?.converged || record.response.failed)
  throw Error('A successful actual finite-tail response is required');
const cfg = record.config, M = cfg.modes, steps = cfg.auditSteps ?? cfg.steps;
const storedGeometry = await createStoredPhysical(cfg), physical = storedGeometry.physical;
const dn = createStoredFiniteTailDN({...cfg, tail: physical, retainTangentPredictor: true});
const engines = new Set();
for (const cell of dn.tail.cells) {
  if (engines.has(cell.engine)) continue;
  engines.add(cell.engine);
  Object.assign(cell.engine, createFourierRootSplitFluxEngine({
    modes: M, spacing: cfg.spacing, quadrature: cfg.quadrature, mu: cell.mu,
    orientation: dn.tail.parameters.orientation,
    projectionFloor: dn.tail.parameters.projectionFloor,
    cuspAwareFlow: cfg.cuspAwareFlow === true
  }));
}
const states = record.response.checkpoint.states;
let worstPhysical = null, worstNormalized = null, minA = Infinity, minD = Infinity;
let maximumRootRelativeResidual = 0, maxCurvature = 0, sampleCount = 0;
const stageRows = [];
const seamRows = [];
let previousInner = null, cutFlowVsStoredNode = null;
function endpointJets(stage, cell, g, y, jets) {
  const r4 = g.r ** 4, sqrtE = Math.sqrt(g.E);
  const values = jets.perAngle.map(p => {
    let nonmeanHeight = 0;
    for (let j = 0; j < M; j++)
      nonmeanHeight += r4 * y[j] * Math.cos(cfg.spacing * (j + 1) * p.theta);
    // Orthonormal components of dh and Hess_g h for g=E dr^2+r^2 dtheta^2.
    const rr = (p.urr - g.w2 * g.dlogwdx * p.ur / (g.E * g.drdx)) / g.E;
    const rt = (p.urt - p.ut / g.r) / (g.r * sqrtE);
    const tt = (p.utt + g.r * p.ur / g.E) / (g.r * g.r);
    return {nonmeanHeight, gradR: p.ur / sqrtE, gradTheta: p.ut / g.r,
      hessRR: rr, hessRT: rt, hessTT: tt,
      ur: p.ur, ut: p.ut, urr: p.urr, urt: p.urt, utt: p.utt};
  });
  return {stage, rawCell: cell.rawCell, rawSegment: cell.rawSegment,
    geometry: {r: g.r, E: g.E, w: g.w,
      wr: g.w * g.dlogwdx / g.drdx}, values};
}
function compareEndpoints(outer, inner, kind) {
  const row = {kind, outerStage: outer.stage, innerStage: inner.stage,
    outerRawCell: outer.rawCell, innerRawCell: inner.rawCell,
    maxNonmeanHeightGap: 0, maxGradientGap: 0, maxCovariantHessianGap: 0,
    worstHessianTheta: null, rawJetMaxima: {ur: 0, ut: 0, urr: 0, urt: 0, utt: 0},
    geometryDifference: Object.fromEntries(Object.keys(outer.geometry).map(k =>
      [k, inner.geometry[k] - outer.geometry[k]]))};
  for (let n = 0; n < outer.values.length; n++) {
    const a = outer.values[n], b = inner.values[n];
    row.maxNonmeanHeightGap = Math.max(row.maxNonmeanHeightGap,
      Math.abs(b.nonmeanHeight - a.nonmeanHeight));
    row.maxGradientGap = Math.max(row.maxGradientGap,
      Math.hypot(b.gradR - a.gradR, b.gradTheta - a.gradTheta));
    const rr = b.hessRR - a.hessRR, rt = b.hessRT - a.hessRT,
      tt = b.hessTT - a.hessTT;
    const gap = Math.abs((rr + tt) / 2) + Math.hypot((rr - tt) / 2, rt);
    if (gap > row.maxCovariantHessianGap) {
      row.maxCovariantHessianGap = gap;
      row.worstHessianTheta = 2 * Math.PI * n / outer.values.length;
    }
    for (const k of Object.keys(row.rawJetMaxima))
      row.rawJetMaxima[k] = Math.max(row.rawJetMaxima[k], Math.abs(b[k] - a[k]));
  }
  return row;
}
function snapshot(stage, cell, profile, step, x, g, y, jets, angularIndex) {
  return {stage, rawCell: cell.rawCell ?? null, rawSegment: cell.rawSegment ?? null,
    profile, step, x, theta: jets.perAngle[angularIndex].theta, angularIndex,
    geometry: g, state: Array.from(y), minA: jets.minA, minD: jets.minD,
    rootRelativeResidual: jets.rootRelativeResidual,
    physicalMaximum: jets.maxDarboux,
    originalProfileNormalizedMaximum: jets.maxDarboux *
      Math.abs(g.E * g.E * g.r * g.drdx / g.w2) * cfg.shootingParts,
    angularDarboux: jets.perAngle.map(p => p.darboux)};
}
for (let stage = 0; stage < dn.tail.cells.length; stage++) {
  const cell = dn.tail.cells[stage], engine = cell.engine;
  if ((cell.rawCell ?? 0) > rawThrough) continue;
  const evaluate = createMomentumPhysicalJetEvaluator(engine, {spacing: cfg.spacing});
  let y = new Float64Array(2 * M + 2); y.set(states[stage + 1]);
  let fullD = 0, originalNormalized = 0;
  let innerEndpoint = null, outerEndpoint = null;
  for (let profile = 0; profile < cell.profiles.length; profile++) {
    const p = cell.profiles[profile];
    for (let step = 0; step <= steps; step++) {
      const x = step / steps, g = engine.geometry(p, x), jets = evaluate(y, p, x);
      if (profile === 0 && step === 0)
        innerEndpoint = endpointJets(stage, cell, g, y, jets);
      if (profile === cell.profiles.length - 1 && step === steps) {
        outerEndpoint = endpointJets(stage, cell, g, y, jets);
        if (stage === 0) {
          const node = new Float64Array(2 * M + 2); node.set(states[0]);
          for (let j = 0; j < M; j++) node[M + j] *= cell.portRatio;
          const nodeJets = evaluate(node, p, x);
          const storedEndpoint = endpointJets(stage, cell, g, node, nodeJets);
          cutFlowVsStoredNode = compareEndpoints(storedEndpoint, outerEndpoint,
            'stored cut node versus integrated cut endpoint');
          cutFlowVsStoredNode.storedCutDarboux = nodeJets.maxDarboux;
          cutFlowVsStoredNode.archivedCutDarbouxDifference =
            nodeJets.maxDarboux - record.response.jets.endpointFullD;
        }
      }
      const factor = Math.abs(g.E * g.E * g.r * g.drdx / g.w2) * cfg.shootingParts;
      const normalized = factor * jets.maxDarboux;
      fullD = Math.max(fullD, jets.maxDarboux);
      originalNormalized = Math.max(originalNormalized, normalized);
      minA = Math.min(minA, jets.minA); minD = Math.min(minD, jets.minD);
      maximumRootRelativeResidual = Math.max(maximumRootRelativeResidual, jets.rootRelativeResidual);
      maxCurvature = Math.max(maxCurvature, jets.formalHeightCurvature);
      const physicalRecord = !worstPhysical || jets.maxDarboux > worstPhysical.physicalMaximum;
      const normalizedRecord = !worstNormalized || normalized > worstNormalized.originalProfileNormalizedMaximum;
      if (physicalRecord || normalizedRecord) {
        let index = 0;
        for (let i = 1; i < jets.perAngle.length; i++)
          if (Math.abs(jets.perAngle[i].darboux) > Math.abs(jets.perAngle[index].darboux)) index = i;
        const point = snapshot(stage, cell, profile, step, x, g, y, jets, index);
        if (physicalRecord) worstPhysical = point;
        if (normalizedRecord) worstNormalized = point;
      }
      sampleCount++;
      if (step < steps) y = engine.rk4(y, p, x, 1 / steps);
    }
  }
  stageRows.push({stage, rawCell: cell.rawCell ?? null,
    rawSegment: cell.rawSegment ?? null, fullD, originalProfileNormalizedDefect: originalNormalized});
  if (previousInner && previousInner.stage === stage - 1)
    seamRows.push(compareEndpoints(previousInner, outerEndpoint,
      'adjacent actual finite ODE pieces'));
  previousInner = innerEndpoint;
}

function spectrum(point) {
  const values = point.angularDarboux, N = values.length, band = cfg.spacing * M;
  const coefficients = [], low = new Float64Array(N), high = new Float64Array(N);
  let lowEnergy = 0, highEnergy = 0, allowedLowMax = 0, oddAmplitudeMax = 0;
  for (let k = 0; k <= N / 2; k++) {
    let cosine = 0, sine = 0;
    const multiplier = (k === 0 || k === N / 2) ? 1 / N : 2 / N;
    for (let n = 0; n < N; n++) {
      const t = 2 * Math.PI * k * n / N;
      cosine += multiplier * values[n] * Math.cos(t);
      sine += multiplier * values[n] * Math.sin(t);
    }
    const amplitude = Math.hypot(cosine, sine);
    coefficients.push({frequency: k, cosine, sine, amplitude,
      retainedBand: k <= band, admittedSymmetry: k % cfg.spacing === 0});
    const energy = (k === 0 || k === N / 2) ? amplitude ** 2 : amplitude ** 2 / 2;
    if (k <= band) lowEnergy += energy; else highEnergy += energy;
    if (k <= band && k % cfg.spacing === 0) allowedLowMax = Math.max(allowedLowMax, amplitude);
    if (k % cfg.spacing !== 0) oddAmplitudeMax = Math.max(oddAmplitudeMax, amplitude);
    const target = k <= band ? low : high;
    for (let n = 0; n < N; n++) {
      const t = 2 * Math.PI * k * n / N;
      target[n] += cosine * Math.cos(t) + sine * Math.sin(t);
    }
  }
  let error = 0, lowMax = 0, highMax = 0;
  for (let n = 0; n < N; n++) {
    error = Math.max(error, Math.abs(values[n] - low[n] - high[n]));
    lowMax = Math.max(lowMax, Math.abs(low[n])); highMax = Math.max(highMax, Math.abs(high[n]));
  }
  return {...point, spectrum: {retainedPhysicalBand: band, angularPoints: N,
    lowBandRMS: Math.sqrt(lowEnergy), highBandRMS: Math.sqrt(highEnergy),
    highBandEnergyFraction: highEnergy / (lowEnergy + highEnergy),
    lowBandSupOnGrid: lowMax, highBandSupOnGrid: highMax,
    allowedLowMaximumCoefficient: allowedLowMax, forbiddenSymmetryMaximumCoefficient: oddAmplitudeMax,
    reconstructionMaxError: error,
    topCoefficients: [...coefficients].sort((a, b) => b.amplitude - a.amplitude).slice(0, 24),
    coefficients}};
}
const hash = data => crypto.createHash('sha256').update(data).digest('hex');
const result = {
  scope: 'Darboux defect of the actual projected ODE on the stated saved finite-tail RK audit cells, with Fourier decomposition at the largest physical and original-profile-normalized defects found there. A restricted search only identifies the archived full-audit maximum when the reported scalar maxima agree. This is a refinement diagnostic, not a continuous enclosure or closed-surface result.',
  normalization: 'Original-profile normalized defect equals abs(Darboux E^2 r r_x / w^2) times shootingParts. Frequency here is physical angular frequency, so retained band is spacing times modes.',
  source_revision: JSON.parse(fs.readFileSync(path.join(sourceTopic, 'source-origin.json'))).source_revision,
  response_file: responseFile, response_sha256: hash(bytes), config: cfg,
  physical_height: record.request.height, nonlinear_residual: record.response.residual,
  stored_metric_adapter: storedGeometry.manifest,
  stable_graph_adapter: storedEngineManifest,
  original_audit: record.response.audit, radial_samples: sampleCount,
  searchedLastRawCell: rawThrough === Infinity ? null : rawThrough,
  searchedAllFiniteStages: stageRows.length === dn.tail.cells.length,
  archivedFullMaximumComparison: {
    physicalAbsoluteDifference: record.response.audit ?
      worstPhysical.physicalMaximum - record.response.audit.fullD : null,
    originalNormalizedAbsoluteDifference: record.response.audit ?
      worstNormalized.originalProfileNormalizedMaximum -
        record.response.audit.normalizedFullDefect * cfg.shootingParts : null
  },
  minA, minD, maxCurvature, maximumRootRelativeResidual,
  shootingSeamJets: {
    scope: 'Actual height jets at adjacent integrated ODE pieces on the searched finite stages. The freely adjustable additive height mean is aligned; all nonmean heights and all physical derivatives are compared. Hessian gaps use the operator norm in the common g orthonormal radial/angular frame. These are finite shooting gaps, not a construction of a globally C2 immersion or an infinite collar.',
    comparedInternalSeams: seamRows.length,
    maxNonmeanHeightGap: Math.max(0, ...seamRows.map(x => x.maxNonmeanHeightGap)),
    maxGradientGap: Math.max(0, ...seamRows.map(x => x.maxGradientGap)),
    maxCovariantHessianGap: Math.max(0, ...seamRows.map(x => x.maxCovariantHessianGap)),
    cutFlowVsStoredNode, rows: seamRows
  },
  worstPhysical: spectrum(worstPhysical), worstNormalized: spectrum(worstNormalized),
  stageRows, script_sha256: hash(fs.readFileSync(new URL(import.meta.url))),
  seconds: (Date.now() - started) / 1000
};
const serialized = JSON.stringify(result, null, 2) + '\n';
if (Buffer.byteLength(serialized) >= 1_000_000) throw Error('Unexpectedly large spectrum report');
fs.writeFileSync(outputFile, serialized, {flag: 'wx'});
console.log(JSON.stringify({output: outputFile, fullD: worstPhysical.physicalMaximum,
  originalProfileNormalizedDefect: worstNormalized.originalProfileNormalizedMaximum,
  worstPhysicalFrequency: result.worstPhysical.spectrum.topCoefficients[0],
  worstNormalizedFrequency: result.worstNormalized.spectrum.topCoefficients[0],
  highBandEnergyFraction: result.worstNormalized.spectrum.highBandEnergyFraction,
  minA, seconds: result.seconds}));
