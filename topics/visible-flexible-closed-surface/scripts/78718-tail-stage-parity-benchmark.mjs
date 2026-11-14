// Small serial/pool comparison harness. Importing this module performs no flow.
// The caller supplies the actual production cellFlow and the pool implementation;
// this file does not copy an engine, profile, RK loop, or shooting residual.
import crypto from 'node:crypto';
import {performance} from 'node:perf_hooks';

const digest = value => crypto.createHash('sha256').update(value).digest('hex');

function doubles(value, label) {
  if (!(Array.isArray(value) || ArrayBuffer.isView(value))) {
    throw new Error(`${label} must be a numeric vector`);
  }
  const result = Float64Array.from(value);
  for (let i = 0; i < result.length; i++) {
    if (!Number.isFinite(result[i])) throw new Error(`${label}[${i}] is not finite`);
  }
  return result;
}

function bytes(value) {
  return Buffer.from(value.buffer, value.byteOffset, value.byteLength);
}

function inputStatus(input, originalLength, originalDigest) {
  // A pool is allowed to transfer the disposable input copy to a worker.
  if (input.byteLength === 0 && originalLength > 0) return 'transferred';
  return digest(bytes(input)) === originalDigest ? 'unchanged' : 'modified';
}

function vectorComparison(left, right, label) {
  const a = doubles(left, `${label}.serial`), b = doubles(right, `${label}.parallel`);
  if (a.length !== b.length) throw new Error(`${label} dimension mismatch`);
  let maximumAbsoluteDifference = 0, largestDifferenceIndex = null;
  let maximumMagnitude = 0, unequalNumericalComponents = 0;
  for (let i = 0; i < a.length; i++) {
    const difference = Math.abs(a[i] - b[i]);
    maximumMagnitude = Math.max(maximumMagnitude, Math.abs(a[i]), Math.abs(b[i]));
    if (!Object.is(a[i], b[i])) unequalNumericalComponents++;
    if (difference > maximumAbsoluteDifference) {
      maximumAbsoluteDifference = difference;
      largestDifferenceIndex = i;
    }
  }
  return {
    components: a.length,
    bitwiseEqual: bytes(a).equals(bytes(b)),
    unequalNumericalComponents,
    maximumAbsoluteDifference,
    largestDifferenceIndex,
    maximumMagnitude,
    maximumDifferenceRelativeToLargestEntry:
      maximumMagnitude > 0 ? maximumAbsoluteDifference / maximumMagnitude : 0,
    serialSHA256: digest(bytes(a)),
    parallelSHA256: digest(bytes(b)),
  };
}

function checkFlow(flow, stateDimension, withJac, label) {
  if (!flow || typeof flow !== 'object') throw new Error(`${label} is not a flow result`);
  const out = doubles(flow.out, `${label}.out`);
  if (out.length !== stateDimension) throw new Error(`${label}.out dimension mismatch`);
  if (!Number.isFinite(flow.meanHeight)) throw new Error(`${label}.meanHeight is not finite`);
  if (withJac) {
    const jacobian = doubles(flow.J, `${label}.J`);
    if (jacobian.length !== stateDimension * stateDimension) {
      throw new Error(`${label}.J dimension mismatch`);
    }
    if (!Number.isFinite(flow.minA) || !Number.isFinite(flow.minD)) {
      throw new Error(`${label} does not have finite variational minima`);
    }
  }
}

/**
 * Run two to four already selected actual stages, never a shooting solve.
 *
 * stages: [{stage, input, target?, scale?, metadata?}]
 *   input is the actual checkpoint node stage+1 in the production normalization.
 *   target, if supplied, is the actual checkpoint node stage (used only for a
 *   scalar residual summary). metadata must contain only scalar provenance.
 * serialFlow(stage, inputCopy, withJac): the actual core cellFlow callback.
 * parallelFlows([{stage,input:inputCopy}, ...], withJac): matching ordered flows.
 *   It must return the same {out,J,meanHeight,minA,minD} convention as cellFlow,
 *   including the actual stage portRatio. The harness never rescales the state.
 *
 * Await pool startup before calling this function. Timings below then compare
 * the selected-stage blocks. Their speed ratio is not a whole-DN speed claim.
 * Source, config and snapshot identities belong in the caller's report.
 */
export async function runStageParityBenchmark({
  stages,
  serialFlow,
  parallelFlows,
  withJacValues = [false, true],
}) {
  if (!Array.isArray(stages) || stages.length < 2 || stages.length > 4) {
    throw new Error('This local benchmark accepts two to four stages');
  }
  if (typeof serialFlow !== 'function' || typeof parallelFlows !== 'function') {
    throw new Error('Actual serialFlow and parallelFlows callbacks are required');
  }
  if (!Array.isArray(withJacValues) || !withJacValues.length ||
      withJacValues.some(v => typeof v !== 'boolean') ||
      new Set(withJacValues).size !== withJacValues.length) {
    throw new Error('withJacValues must contain distinct booleans');
  }
  const selected = stages.map((item, index) => {
    if (!Number.isInteger(item.stage) || item.stage < 0) throw new Error('Invalid stage index');
    const input = doubles(item.input, `stages[${index}].input`);
    const target = item.target === undefined ? null : doubles(item.target, `stages[${index}].target`);
    if (!input.length || (target && target.length !== input.length)) throw new Error('Invalid stage dimensions');
    if (item.scale !== undefined && !(Number.isFinite(item.scale) && item.scale > 0)) {
      throw new Error('A supplied stage scale must be finite and positive');
    }
    return {...item, input, target, inputSHA256: digest(bytes(input))};
  });
  if (new Set(selected.map(item => item.stage)).size !== selected.length) {
    throw new Error('Selected stages must be distinct');
  }
  const blocks = [];
  for (const withJac of withJacValues) {
    const serialInputs = selected.map(item => Float64Array.from(item.input));
    const serial = [];
    const serialBegin = performance.now();
    for (let i = 0; i < selected.length; i++) {
      serial.push(await serialFlow(selected[i].stage, serialInputs[i], withJac));
    }
    const serialMilliseconds = performance.now() - serialBegin;
    const poolTasks = selected.map(item => ({stage: item.stage, input: Float64Array.from(item.input)}));
    const parallelBegin = performance.now();
    const parallel = await parallelFlows(poolTasks, withJac);
    const parallelMilliseconds = performance.now() - parallelBegin;
    if (!Array.isArray(parallel) || parallel.length !== selected.length) {
      throw new Error('The pool must return one ordered result per selected stage');
    }
    const comparisons = selected.map((item, i) => {
      checkFlow(serial[i], item.input.length, withJac, `serial stage ${item.stage}`);
      checkFlow(parallel[i], item.input.length, withJac, `parallel stage ${item.stage}`);
      const state = vectorComparison(serial[i].out, parallel[i].out, `stage ${item.stage} out`);
      const J = withJac ? vectorComparison(serial[i].J, parallel[i].J, `stage ${item.stage} J`) : null;
      const meanHeightDifference = serial[i].meanHeight - parallel[i].meanHeight;
      const meanHeightBitwiseEqual = bytes(Float64Array.of(serial[i].meanHeight))
        .equals(bytes(Float64Array.of(parallel[i].meanHeight)));
      let maximumSerialResidual = null;
      if (item.target) {
        maximumSerialResidual = 0;
        for (let j = 0; j < item.target.length; j++) {
          maximumSerialResidual = Math.max(maximumSerialResidual, Math.abs(serial[i].out[j] - item.target[j]));
        }
      }
      return {
        stage: item.stage,
        metadata: item.metadata ?? null,
        inputSHA256: item.inputSHA256,
        state,
        J,
        meanHeightDifference,
        meanHeightBitwiseEqual,
        serialMinimumA: serial[i].minA ?? null,
        parallelMinimumA: parallel[i].minA ?? null,
        serialMinimumD: serial[i].minD ?? null,
        parallelMinimumD: parallel[i].minD ?? null,
        maximumSerialResidual,
        maximumSerialNormalizedResidual: item.scale !== undefined && maximumSerialResidual !== null
          ? maximumSerialResidual / item.scale : null,
        normalizedStateDifference: item.scale !== undefined ? state.maximumAbsoluteDifference / item.scale : null,
        serialInputStatus: inputStatus(serialInputs[i], item.input.length, item.inputSHA256),
        poolInputStatus: inputStatus(poolTasks[i].input, item.input.length, item.inputSHA256),
      };
    });
    blocks.push({
      withJac,
      serialMilliseconds,
      parallelMilliseconds,
      selectedBlockSpeedRatio: parallelMilliseconds > 0 ? serialMilliseconds / parallelMilliseconds : null,
      comparisons,
      allFlowsBitwiseEqual: comparisons.every(row => row.state.bitwiseEqual &&
        (!withJac || row.J.bitwiseEqual) && row.meanHeightBitwiseEqual &&
        Object.is(row.serialMinimumA, row.parallelMinimumA) &&
        Object.is(row.serialMinimumD, row.parallelMinimumD)),
    });
  }
  return {
    scope: 'Only the supplied two-to-four actual stages and selected flow branches; no whole-tail timing or whole-shooting claim.',
    selectedStageCount: selected.length,
    serialStageFlows: selected.length * withJacValues.length,
    parallelStageFlows: selected.length * withJacValues.length,
    blocks,
  };
}
