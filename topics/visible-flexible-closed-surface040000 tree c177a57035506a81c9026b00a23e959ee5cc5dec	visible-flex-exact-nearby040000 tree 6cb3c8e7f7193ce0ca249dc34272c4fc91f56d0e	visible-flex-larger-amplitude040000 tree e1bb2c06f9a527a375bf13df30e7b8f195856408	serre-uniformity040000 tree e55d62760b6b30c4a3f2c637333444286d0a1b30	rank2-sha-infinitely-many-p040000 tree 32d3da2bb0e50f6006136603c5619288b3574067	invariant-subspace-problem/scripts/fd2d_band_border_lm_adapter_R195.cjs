"use strict";
/* R195 alternate backend. Frozen dense LM value/Armijo/trace/lambda policy copied unchanged.
 * No physical provider, domain or objective changes. Pure V8 callers supply kernel explicitly.
 */
function createBandBorderLM(kernel, definition){
  if(!kernel||typeof kernel.prepareBandBorderNormal!=="function"||typeof kernel.solvePreparedBandBorder!=="function")throw Error("Explicit R195 kernel required");
  if(!definition)throw Error("Explicit actual provider definition required");
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

function prepareNormal(normal){const p=kernel.prepareBandBorderNormal(normal,definition);return {...p,n:p.layout.n};}
function solvePrepared(prepared,lambda){return kernel.solvePreparedBandBorder(prepared,lambda);}
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

  return {lmStep,runLM,backendDefinition:{schema:"R195-band-border-LM-backend-v1",densePolicySHA256:"1e74ee24bd59b3f7a0b41fedf17e338f7ea42f113de72986396fde484de38ea4",kernelSHA256:"0ae8ae6d6cd58b8bbc6435189a9850861dc5948c4ba322028dc6fc3886d98013",actualValuePolicyChanged:false,domainChanged:false,normalRowsChanged:false}};
}
module.exports={createBandBorderLM};
