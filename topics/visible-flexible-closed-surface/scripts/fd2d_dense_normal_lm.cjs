"use strict";
/**
 * Dense, column-scaled LM and true-value Armijo for a NEW finite branch.
 *
 * Contract: H = J^T J, g = J^T r, squaredNorm = ||r||^2 at exactly z.
 * H may be row-major flat storage or an array of n rows. No dependencies.
 * A positive H[j,j] gives scale[j] = 1/sqrt(H[j,j]); an exactly zero
 * diagonal uses scale 1 and is reported. Input arrays are never modified.
 *
 * The working symmetric matrix is (H+H^T)/2; its actual adjustment and
 * residual against the original scaled matrix are reported. Failed
 * Cholesky/solve attempts increase the EXPLICIT lambda. There is no hidden
 * pivot floor, Hessian shift, pseudoinverse, or fabricated accepted value.
 *
 * value(z) may be synchronous/asynchronous. It returns squaredNorm, or an
 * object with squaredNorm (and optionally valid:false). Cost is one half
 * squaredNorm. Every acceptance uses a freshly evaluated actual trial.
 * Default alpha choices are exactly [1, .5, .25].
 *
 * A finite least-squares result is not a continuous geometric certificate.
 */

function assert(condition, message) {
  if (!condition) throw new Error(message);
}
function finiteNumber(x, name) {
  assert(typeof x === "number" && Number.isFinite(x), name + " must be finite");
  return x;
}
function vectorCopy(value, n, name) {
  assert(value != null && typeof value.length === "number", name + " must be array-like");
  if (n != null) assert(value.length === n, name + " has the wrong length");
  const out = new Float64Array(value.length);
  for (let i = 0; i < value.length; ++i) out[i] = finiteNumber(Number(value[i]), name + "[" + i + "]");
  return out;
}
function dot(a, b) {
  assert(a.length === b.length, "dot dimension mismatch");
  let sum = 0, correction = 0;
  for (let i = 0; i < a.length; ++i) {
    const term = a[i] * b[i], next = sum + term;
    correction += Math.abs(sum) >= Math.abs(term) ? (sum - next) + term : (term - next) + sum;
    sum = next;
  }
  return sum + correction;
}
function rowDot(matrix, offset, vector) {
  let sum = 0, correction = 0;
  for (let j = 0; j < vector.length; ++j) {
    const term = matrix[offset + j] * vector[j], next = sum + term;
    correction += Math.abs(sum) >= Math.abs(term) ? (sum - next) + term : (term - next) + sum;
    sum = next;
  }
  return sum + correction;
}
function norm2(a) {
  let answer = 0;
  for (let i = 0; i < a.length; ++i) answer = Math.hypot(answer, a[i]);
  return answer;
}
function maxAbs(a) {
  let answer = 0;
  for (let i = 0; i < a.length; ++i) answer = Math.max(answer, Math.abs(a[i]));
  return answer;
}
function sameVector(a, b) {
  if (a.length !== b.length) return false;
  for (let i = 0; i < a.length; ++i) if (a[i] !== b[i]) return false;
  return true;
}
function allFinite(a) {
  for (let i = 0; i < a.length; ++i) if (!Number.isFinite(a[i])) return false;
  return true;
}

function prepareNormal(normal) {
  assert(normal && normal.H != null && normal.g != null, "Require H and g");
  const gradient = vectorCopy(normal.g, null, "g"), n = gradient.length;
  assert(Number.isInteger(n) && n > 0, "Require a nonempty normal");
  const squaredNorm = finiteNumber(Number(normal.squaredNorm), "squaredNorm");
  assert(squaredNorm >= 0, "squaredNorm must be nonnegative");
  const H = new Float64Array(n * n), source = normal.H;
  const rows = source.length === n && source[0] != null && typeof source[0] !== "number"
    && typeof source[0].length === "number";
  if (rows) {
    for (let i = 0; i < n; ++i) {
      assert(source[i].length === n, "H row has the wrong length");
      for (let j = 0; j < n; ++j) H[i*n+j] = finiteNumber(Number(source[i][j]), "H entry");
    }
  } else {
    assert(source.length === n*n, "Flat H must be row-major n by n");
    for (let i = 0; i < H.length; ++i) H[i] = finiteNumber(Number(source[i]), "H entry");
  }
  const diagonal = new Float64Array(n), scale = new Float64Array(n);
  const given = normal.diagonal == null ? null : vectorCopy(normal.diagonal, n, "diagonal");
  const zeroColumns = [];
  let suppliedDiagonalDifference = 0, suppliedDiagonalRelativeDifference = 0;
  for (let i = 0; i < n; ++i) {
    diagonal[i] = H[i*n+i];
    assert(diagonal[i] >= 0, "A J^T J diagonal cannot be negative");
    scale[i] = diagonal[i] > 0 ? 1 / Math.sqrt(diagonal[i]) : 1;
    assert(Number.isFinite(scale[i]), "The requested exact column scale is not finite");
    if (diagonal[i] === 0) zeroColumns.push(i);
    if (given) {
      const difference = Math.abs(given[i] - diagonal[i]);
      suppliedDiagonalDifference = Math.max(suppliedDiagonalDifference, difference);
      suppliedDiagonalRelativeDifference = Math.max(suppliedDiagonalRelativeDifference,
        difference / Math.max(Number.MIN_VALUE, Math.abs(given[i]), diagonal[i]));
    }
  }
  const scaled = new Float64Array(n*n), originalScaled = new Float64Array(n*n);
  let symmetryAdjustment = 0, scaledSymmetryAdjustment = 0;
  for (let i = 0; i < n; ++i) for (let j = 0; j < n; ++j) {
    const original = H[i*n+j];
    const symmetric = i === j ? original : .5*original + .5*H[j*n+i];
    symmetryAdjustment = Math.max(symmetryAdjustment, Math.abs(symmetric-original));
    const raw = (original * scale[i]) * scale[j];
    const averaged = (symmetric * scale[i]) * scale[j];
    assert(Number.isFinite(raw) && Number.isFinite(averaged), "Scaled normal contains a nonfinite entry");
    originalScaled[i*n+j] = raw;
    scaled[i*n+j] = averaged;
    scaledSymmetryAdjustment = Math.max(scaledSymmetryAdjustment, Math.abs(averaged-raw));
  }
  // Copy the upper half to the lower half. Different multiplication order
  // in S_i H_ij S_j can differ by an ulp; this last symmetric adjustment is
  // measured separately and does not overwrite the original normal.
  let scalingOrderSymmetryAdjustment = 0;
  for (let i = 0; i < n; ++i) for (let j = 0; j < i; ++j) {
    scalingOrderSymmetryAdjustment = Math.max(scalingOrderSymmetryAdjustment,
      Math.abs(scaled[i*n+j] - scaled[j*n+i]));
    const average = .5*scaled[i*n+j] + .5*scaled[j*n+i];
    scaled[i*n+j] = average; scaled[j*n+i] = average;
  }
  const scaledGradient = new Float64Array(n);
  for (let i = 0; i < n; ++i) {
    scaledGradient[i] = gradient[i] * scale[i];
    assert(Number.isFinite(scaledGradient[i]), "Scaled gradient is not finite");
  }
  return {n, H, gradient, squaredNorm, diagonal, scale, scaled, originalScaled,
    scaledGradient,
    info: {dimension: n, zeroDiagonalColumns: zeroColumns,
      zeroDiagonalScale: 1, exactPositiveDiagonalScale: "1/sqrt(Hjj)",
      suppliedDiagonalDifference, suppliedDiagonalRelativeDifference,
      suppliedDiagonalUsedInsteadOfHjj: false, symmetryAdjustment,
      scaledSymmetryAdjustment, scalingOrderSymmetryAdjustment,
      scaledGradientInfinity: maxAbs(scaledGradient),
      inputArraysModified: false, continuousCertificate: false}};
}

function cholesky(matrix, n, lambda) {
  const L = new Float64Array(n*n);
  let minimumPivot = Infinity, maximumPivot = 0;
  for (let i = 0; i < n; ++i) for (let j = 0; j <= i; ++j) {
    let sum = 0, correction = 0;
    for (let k = 0; k < j; ++k) {
      const term = L[i*n+k]*L[j*n+k], next = sum+term;
      correction += Math.abs(sum) >= Math.abs(term) ? (sum-next)+term : (term-next)+sum;
      sum = next;
    }
    const entry = matrix[i*n+j] + (i === j ? lambda : 0);
    const residual = entry - (sum+correction);
    if (i === j) {
      if (!(Number.isFinite(residual) && residual > 0))
        return {ok: false, phase: "cholesky", failedPivot: i,
          pivot: Number.isFinite(residual) ? residual : null, lambda};
      minimumPivot = Math.min(minimumPivot, residual);
      maximumPivot = Math.max(maximumPivot, residual);
      L[i*n+j] = Math.sqrt(residual);
    } else {
      L[i*n+j] = residual/L[j*n+j];
      if (!Number.isFinite(L[i*n+j]))
        return {ok: false, phase: "cholesky", failedPivot: j, row: i, pivot: null, lambda};
    }
  }
  return {ok: true, L, minimumPivot, maximumPivot};
}

function solvePrepared(prepared, lambda) {
  finiteNumber(lambda, "lambda");
  assert(lambda > 0, "Use a strictly positive explicit LM damping");
  const {n, scaled, scaledGradient, scale, gradient, squaredNorm} = prepared;
  const factor = cholesky(scaled, n, lambda);
  if (!factor.ok) return {...factor, preparedInfo: prepared.info};
  const work = new Float64Array(n), q = new Float64Array(n);
  for (let i = 0; i < n; ++i) {
    let sum = 0, correction = 0;
    for (let j = 0; j < i; ++j) {
      const term = factor.L[i*n+j]*work[j], next = sum+term;
      correction += Math.abs(sum) >= Math.abs(term) ? (sum-next)+term : (term-next)+sum;
      sum = next;
    }
    work[i] = (-scaledGradient[i] - (sum+correction))/factor.L[i*n+i];
  }
  for (let i = n-1; i >= 0; --i) {
    let sum = 0, correction = 0;
    for (let j = i+1; j < n; ++j) {
      const term = factor.L[j*n+i]*q[j], next = sum+term;
      correction += Math.abs(sum) >= Math.abs(term) ? (sum-next)+term : (term-next)+sum;
      sum = next;
    }
    q[i] = (work[i] - (sum+correction))/factor.L[i*n+i];
  }
  const direction = new Float64Array(n);
  for (let i = 0; i < n; ++i) direction[i] = scale[i]*q[i];
  if (!allFinite(q) || !allFinite(direction))
    return {ok: false, phase: "triangular_solve", lambda, preparedInfo: prepared.info};
  const symmetricResidual = new Float64Array(n), originalResidual = new Float64Array(n);
  const hq = new Float64Array(n), aq = new Float64Array(n);
  for (let i = 0; i < n; ++i) {
    hq[i] = rowDot(scaled, i*n, q);
    aq[i] = hq[i] + lambda*q[i];
    symmetricResidual[i] = aq[i]+scaledGradient[i];
    originalResidual[i] = rowDot(prepared.originalScaled, i*n, q)+lambda*q[i]+scaledGradient[i];
  }
  const slope = dot(gradient, direction), scaledSlope = dot(scaledGradient, q);
  const quadratic = dot(q, hq), predictedSquaredNorm = squaredNorm+2*slope+quadratic;
  if (![slope, scaledSlope, quadratic, predictedSquaredNorm].every(Number.isFinite))
    return {ok: false, phase: "model_diagnostics", lambda, preparedInfo: prepared.info};
  const denominator = norm2(scaledGradient)+norm2(aq);
  return {ok: true, lambda, direction, scaledDirection: q,
    scale: new Float64Array(scale), slope, quadratic, predictedSquaredNorm,
    predictedReduction: -slope-.5*quadratic,
    info: {...prepared.info, minimumPivot: factor.minimumPivot,
      maximumPivot: factor.maximumPivot, scaledSlope,
      physicalAndScaledSlopeDifference: Math.abs(slope-scaledSlope),
      originalScaledEquationResidualMaximum: maxAbs(originalResidual),
      workingScaledEquationResidualMaximum: maxAbs(symmetricResidual),
      workingScaledEquationRelativeResidual: denominator > 0 ? norm2(symmetricResidual)/denominator : 0,
      diagonalDampingInScaledCoordinates: lambda, hiddenDiagonalShift: 0,
      actualTrialEvaluated: false, finiteSpaceLowerBoundClaimed: false}};
}

function solveDampedNormal(normal, options = {}) {
  const lambda = options.lambda === undefined ? 1e-3 : Number(options.lambda);
  return solvePrepared(prepareNormal(normal), lambda);
}

function evaluationNorm(result) {
  if (typeof result === "number") return result;
  if (!result || typeof result !== "object") return NaN;
  if (result.valid === false) return NaN;
  return typeof result.squaredNorm === "number" ? result.squaredNorm : NaN;
}

async function lmStep(options) {
  const {normal, value} = options || {};
  assert(typeof value === "function", "value must evaluate the actual finite objective");
  const prepared = prepareNormal(normal), z = vectorCopy(options.z, prepared.n, "z");
  if (normal.z != null) assert(sameVector(z, vectorCopy(normal.z, prepared.n, "normal.z")),
    "The supplied normal belongs to a different z");
  const lambdaMin = options.lambdaMin === undefined ? 1e-16 : finiteNumber(Number(options.lambdaMin), "lambdaMin");
  const lambdaMax = options.lambdaMax === undefined ? 1e16 : finiteNumber(Number(options.lambdaMax), "lambdaMax");
  const increase = options.increaseFactor === undefined ? 10 : finiteNumber(Number(options.increaseFactor), "increaseFactor");
  const armijo = options.armijo === undefined ? 1e-4 : finiteNumber(Number(options.armijo), "armijo");
  const attempts = options.maxDampingAttempts === undefined ? 8 : Number(options.maxDampingAttempts);
  const alphas = options.alphas === undefined ? [1, .5, .25] : Array.from(options.alphas, Number);
  assert(lambdaMin > 0 && lambdaMax >= lambdaMin && increase > 1, "Invalid explicit damping interval/factor");
  assert(armijo > 0 && armijo < .5, "Use an Armijo constant in (0, .5)");
  assert(Number.isInteger(attempts) && attempts > 0, "Use a positive finite damping-attempt count");
  assert(alphas.length > 0 && alphas.every((a,i) => Number.isFinite(a) && a > 0 && a <= 1
    && (i === 0 || a < alphas[i-1])), "Use decreasing positive alpha values no greater than 1");
  let lambda = options.lambda === undefined ? 1e-3 : finiteNumber(Number(options.lambda), "lambda");
  assert(lambda > 0, "Initial damping must be strictly positive");
  lambda = Math.max(lambdaMin, Math.min(lambdaMax, lambda));
  const cost = .5*prepared.squaredNorm, trace = [];
  let actualValueEvaluations = 0, lastSolve = null;
  if (prepared.info.scaledGradientInfinity === 0)
    return {accepted: false, status: "zero_linear_gradient", z, squaredNorm: prepared.squaredNorm,
      lambda, nextLambda: lambda, trace, actualValueEvaluations, normalInfo: prepared.info,
      finiteResidualZero: prepared.squaredNorm === 0, strongTargetComplete: false};
  for (let attempt = 0; attempt < attempts; ++attempt) {
    const solved = solvePrepared(prepared, lambda); lastSolve = solved;
    if (!solved.ok) {
      const record = {kind: "factorization_rejected", attempt, lambda,
        phase: solved.phase, failedPivot: solved.failedPivot ?? null, pivot: solved.pivot ?? null,
        actualValueEvaluated: false};
      trace.push(record);
      if (options.onTrial) await options.onTrial(record);
    } else if (!(solved.slope < 0)) {
      const record = {kind: "non_descent_direction", attempt, lambda,
        slope: solved.slope, actualValueEvaluated: false};
      trace.push(record);
      if (options.onTrial) await options.onTrial(record);
    } else {
      for (const alpha of alphas) {
        const candidate = new Float64Array(z.length);
        for (let i = 0; i < z.length; ++i) candidate[i] = z[i]+alpha*solved.direction[i];
        const threshold = cost+armijo*alpha*solved.slope;
        let evaluated = null, trialNorm = NaN, error = null;
        if (allFinite(candidate)) {
          const argument = new Float64Array(candidate);
          ++actualValueEvaluations;
          try {
            evaluated = await value(argument);
            assert(sameVector(argument,candidate), "value mutated its trial parameter vector");
            trialNorm = evaluationNorm(evaluated);
          } catch (caught) {
            error = {name: String(caught && caught.name || "Error"),
              message: String(caught && caught.message || caught)};
          }
        } else error = {name: "NonfiniteTrial", message: "The computed candidate is nonfinite"};
        const valid = Number.isFinite(trialNorm) && trialNorm >= 0 && error === null;
        const trialCost = valid ? .5*trialNorm : null;
        const accepted = valid && trialCost < threshold;
        const predictedReduction = -alpha*solved.slope-.5*alpha*alpha*solved.quadratic;
        const actualReduction = valid ? cost-trialCost : null;
        const rho = valid && predictedReduction > 0 ? actualReduction/predictedReduction : null;
        const record = {kind: "actual_trial", attempt, lambda, alpha, valid, accepted,
          baselineSquaredNorm: prepared.squaredNorm, squaredNorm: valid ? trialNorm : null,
          baselineCost: cost, actualCost: trialCost, armijoThreshold: threshold,
          slope: solved.slope, predictedReduction, actualReduction, rho, error,
          actualValueEvaluated: allFinite(candidate)};
        trace.push(record);
        if (options.onTrial) await options.onTrial(record);
        if (accepted) {
          let nextLambda = lambda;
          if (rho !== null && rho > .75 && alpha === 1) nextLambda = Math.max(lambdaMin, lambda/3);
          else if (rho !== null && rho < .25) nextLambda = Math.min(lambdaMax, lambda*increase);
          return {accepted: true, status: "actual_Armijo_accepted", z: candidate,
            squaredNorm: trialNorm, cost: trialCost, alpha, lambda, nextLambda,
            direction: solved.direction, evaluation: evaluated, solveInfo: solved.info,
            predictedReduction, actualReduction, rho, trace, actualValueEvaluations,
            physicalDomainOrContinuousGeometryCertified: false, strongTargetComplete: false};
        }
      }
    }
    if (lambda >= lambdaMax) break;
    const next = Math.min(lambdaMax, lambda*increase);
    if (!(next > lambda)) break;
    lambda = next;
  }
  return {accepted: false, status: "no_actual_Armijo_step", z,
    squaredNorm: prepared.squaredNorm, cost, lambda, nextLambda: lambda,
    trace, actualValueEvaluations, lastSolveInfo: lastSolve && (lastSolve.info || lastSolve.preparedInfo),
    physicalDomainOrContinuousGeometryCertified: false, strongTargetComplete: false};
}

async function runLM(options) {
  assert(options && typeof options.normal === "function", "normal(z) is required");
  assert(typeof options.value === "function", "value(z) is required");
  let z = vectorCopy(options.z, null, "z");
  const maxIterations = options.maxIterations === undefined ? 40 : Number(options.maxIterations);
  const tolerance = options.squaredNormTolerance === undefined ? 0 : Number(options.squaredNormTolerance);
  assert(Number.isInteger(maxIterations) && maxIterations >= 0, "Use a nonnegative iteration count");
  assert(Number.isFinite(tolerance) && tolerance >= 0, "Use a nonnegative finite squared-norm tolerance");
  let lambda = options.lambda === undefined ? 1e-3 : Number(options.lambda);
  const history = [];
  let actualValueEvaluations = 0, normalEvaluations = 0, acceptedSteps = 0;
  let squaredNorm = null, status = "iteration_limit";
  for (let iteration = 0; iteration < maxIterations; ++iteration) {
    const argument = new Float64Array(z);
    const normal = await options.normal(argument);
    ++normalEvaluations;
    assert(sameVector(argument,z), "normal mutated its parameter vector");
    squaredNorm = finiteNumber(Number(normal.squaredNorm), "normal squaredNorm");
    if (squaredNorm <= tolerance) {
      status = "finite_squared_norm_target"; break;
    }
    const step = await lmStep({...options, z, normal, lambda});
    actualValueEvaluations += step.actualValueEvaluations;
    const record = {iteration, accepted: step.accepted, status: step.status,
      baselineSquaredNorm: squaredNorm, squaredNorm: step.squaredNorm,
      lambda: step.lambda, nextLambda: step.nextLambda, alpha: step.alpha ?? null,
      predictedReduction: step.predictedReduction ?? null, actualReduction: step.actualReduction ?? null,
      rho: step.rho ?? null, actualValueEvaluations: step.actualValueEvaluations,
      trace: step.trace, solveInfo: step.solveInfo || step.lastSolveInfo || step.normalInfo};
    history.push(record);
    if (step.accepted) {
      z = new Float64Array(step.z); squaredNorm = step.squaredNorm;
      lambda = step.nextLambda; ++acceptedSteps;
      if (options.onAccept) await options.onAccept({iteration, z: new Float64Array(z), step});
    } else {
      status = step.status;
      if (options.onIteration) await options.onIteration(record);
      break;
    }
    if (options.onIteration) await options.onIteration(record);
    if (squaredNorm <= tolerance) {status = "finite_squared_norm_target"; break;}
  }
  return {z, squaredNorm, lambda, status, history, acceptedSteps,
    actualValueEvaluations, normalEvaluations,
    finiteObjectiveTargetMet: squaredNorm !== null && squaredNorm <= tolerance,
    strongTargetComplete: false};
}

module.exports = {prepareNormal, solveDampedNormal, lmStep, runLM, dot, norm2};
