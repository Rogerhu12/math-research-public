#!/usr/bin/env python3
"""Continue one cap5 search after its actual startup failure; reuse its paid prefix."""
import time
ENTRY_STARTED = time.perf_counter()

import argparse
import copy
import io
import hashlib
import json
import math
import os
import pathlib
import platform
import resource
import sys
import traceback

SCHEMA = "cap5-positive-curvature-search-v1"

# This is the same original120-second/400-started-integral allocation.
# The prior failure and its completed prefix are never erased or rerun.
CONTINUATION_POLICY = "cap5-paid-prefix-startup-repair-v1"
CARRIED_SECONDS = 0.5630522320000182
CARRIED_STARTED = 2
CARRIED_COMPLETED = 1
CARRIED_FAILED = 1
CARRIED_RHS_CALLS = 14
CARRIED_PREFIX_CALLS = 63
CARRIED_RECORD_COUNT = 6
CARRIED_RECORD_OUTPUT_BYTES = 8431
FIRST_STEP = 1e-6
REPAIR_DESIGN = "notes/cap-five-startup-repair-paid-prefix-continuation-20261116.md"

CARRIED_SOURCE = {
    "repository": "Rogerhu12/math-research-public",
    "run_id": "43831664308",
    "job_id": "133178210211",
    "source_commit": "03bfffd120026aa5f25187dc0c0ec5c01705e709",
    "workflow": ".github/workflows/visible-cap-five-positive-curvature-search.yml",
    "log_bytes": 106370,
    "log_sha256": "0e78611cfb99dc2e6a9158991d920a3740185919bb25924c5a4865333fce2520",
    "original_request": {
        "path": "topics/visible-flex-new-mechanism/computations/request-cap-five-positive-curvature-search.json",
        "bytes": 6143,
        "sha256": "353d61eae47e5763176eee3dff13edd56b0e000660afe959cbbe44f799d85c8f"
    }
}
CARRIED_RECORDS = [
    {
        "tag": "CAP5_RECORD",
        "kind": "PREFIX_COMPLETE",
        "record": 3,
        "bytes": 655,
        "sha256": "d1bd2dca8e358f526f9fd904fe37e79c6d651c00ac36e502712b8c98c4015c76"
    },
    {
        "tag": "CAP5_RECORD",
        "kind": "INTEGRAL_FAILED",
        "record": 5,
        "bytes": 854,
        "sha256": "37a2d67d6536a04d4cfb87e59cfd03a83c83e5b4e57dc64f75af8addab85a7a3"
    },
    {
        "tag": "CAP5_RECORD",
        "kind": "FINAL_REPORT",
        "record": 6,
        "bytes": 4837,
        "sha256": "858e14bf1727a21e3740e54140158f642339ce4e1b04066cf0218174884ca6b6"
    },
    {
        "tag": "CAP5_FINAL_CLOCK",
        "kind": "FINAL_CLOCK",
        "record": None,
        "bytes": 333,
        "sha256": "a4ec5d0df80d2f929bae363319c95095d744989a4a329d9af06dbf4ae688b4ef"
    }
]
ROOT = pathlib.Path(__file__).resolve().parents[1]
N = 15
A_START = 1.0 / 32.0
TAGS = ("Delta1", "Delta2", "Delta3", "Delta4", "Delta6")
MONOMIALS = (
    (0, 1.0, 2, 3, 0),
    (1, -1.0, 1, 4, 0),
    (2, 1.5, 2, 1, 2),
    (2, 0.3, 0, 5, 0),
    (3, -0.5, 2, 0, 3),
    (3, -3.0, 1, 2, 2),
    (4, 1.5, 1, 1, 3),
    (4, 1.5, 0, 3, 2),
    (5, -0.25, 1, 0, 4),
    (5, -1.0, 0, 2, 3),
    (6, 5.0 / 16.0, 0, 1, 4),
    (7, -3.0 / 80.0, 0, 0, 5),
)
FINE_CENTRES = tuple(3.0 / 64.0 + j / 64.0 for j in range(5))
FINE_RADIUS = 1.0 / 128.0
WIDE_CENTRES = tuple(0.2 + 0.075 * j for j in range(10))
WIDE_RADIUS = 0.1
BINOMIAL = tuple(tuple(math.comb(k, j) if j <= k else 0
                       for k in range(8)) for j in range(8))
np = None
solve_ivp = None
least_squares = None


class SearchStop(RuntimeError):
    pass


class BudgetStop(RuntimeError):
    pass


class CandidateFound(RuntimeError):
    pass


def finite_json(value):
    if isinstance(value, dict):
        return {str(k): finite_json(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [finite_json(v) for v in value]
    if np is not None and isinstance(value, np.ndarray):
        return finite_json(value.tolist())
    if np is not None and isinstance(value, np.generic):
        return finite_json(value.item())
    if isinstance(value, float) and not math.isfinite(value):
        return {"nonfinite_float": repr(value)}
    return value


class Ledger:
    def __init__(self):
        self.stage = "entry"
        self.integrals_started = CARRIED_STARTED
        self.integrals_completed = CARRIED_COMPLETED
        self.integrals_failed = CARRIED_FAILED
        self.rhs_calls = CARRIED_RHS_CALLS
        self.prefix_calls = CARRIED_PREFIX_CALLS
        self.carried_receipt_verified = False
        self.carried_receipt = None
        self.cache_hits = 0
        self.output_bytes = CARRIED_RECORD_OUTPUT_BYTES
        self.record_count = CARRIED_RECORD_COUNT
        self.output_cap = 3000000
        self.output_compacted = 0
        self.output_limit_reached = False
        self.last_completed = None
        self.best = None
        self.last_started = None
        self.last_rhs = None
        self.starts = []
        self.refinements = []
        self.events = []
        self.cache = {}
        self.prefix = None
        self.whitener = None
        self.whitening_singular_values = None

    def elapsed(self):
        return CARRIED_SECONDS + time.perf_counter() - ENTRY_STARTED

    def check(self, phase=None):
        e = self.elapsed()
        if self.output_limit_reached:
            raise BudgetStop("stdout soft cap reached after preserving the complete paid record")
        if e >= 120.0:
            raise BudgetStop("shared 120 second cap reached")
        if phase == "search" and e >= 112.0:
            raise SearchStop("search stopped at 112 seconds; final refinement reserve")

    def charge(self, phase, details):
        self.check(phase)
        if not self.carried_receipt_verified or self.prefix is None:
            raise RuntimeError("authenticate and restore the completed prefix before new science")
        if self.integrals_started >= 400:
            raise BudgetStop("shared 400 started integral cap reached")
        if phase == "search" and self.integrals_started >= 397:
            raise SearchStop("search integral cap leaves three final slots")
        self.integrals_started += 1
        self.last_started = {
            "integral_id": self.integrals_started,
            "phase": phase, "elapsed_at_start": self.elapsed(), **details,
        }
        self.emit("INTEGRAL_STARTED", self.last_started)
        return self.integrals_started

    def emit(self, kind, payload):
        self.record_count += 1
        obj = finite_json({
            "schema": SCHEMA, "record": self.record_count,
            "kind": kind, "elapsed": self.elapsed(), "data": payload,
        })
        line = "CAP5_RECORD " + json.dumps(
            obj, ensure_ascii=False, separators=(",", ":"), allow_nan=False
        )
        raw_bytes = len((line + "\n").encode("utf-8"))
        print(line, flush=True)
        self.output_bytes += raw_bytes
        if self.output_bytes > self.output_cap:
            # Preserve the whole paid record; stop before any next scientific operation.
            self.output_limit_reached = True

    def costs(self):
        return {
            "elapsed_from_before_scientific_imports": self.elapsed(),
            "current_process_elapsed_seconds": time.perf_counter() - ENTRY_STARTED,
            "carried_failed_attempt_seconds": CARRIED_SECONDS,
            "same_original120_second_allocation_not_reset": True,
            "carried_receipt_verified": self.carried_receipt_verified,
            "current_process_integrals_started": self.integrals_started-CARRIED_STARTED,
            "current_process_integrals_completed": self.integrals_completed-CARRIED_COMPLETED,
            "current_process_integrals_failed": self.integrals_failed-CARRIED_FAILED,
            "current_process_rhs_calls": self.rhs_calls-CARRIED_RHS_CALLS,
            "current_process_prefix_quadrature_calls": self.prefix_calls-CARRIED_PREFIX_CALLS,
            "integrals_started": self.integrals_started,
            "integrals_completed": self.integrals_completed,
            "integrals_failed": self.integrals_failed,
            "rhs_calls": self.rhs_calls,
            "prefix_quadrature_calls": self.prefix_calls,
            "cache_hits": self.cache_hits,
            "rss_max_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            "records": self.record_count, "output_bytes": self.output_bytes,
            "output_compacted": self.output_compacted,
            "output_limit_reached": self.output_limit_reached,
            "budget_seconds": 120.0, "budget_started_integrals": 400,
            "old_psi3_E_evaluations": 0,
            "old_self_or_rank_or_forcing_evaluations": 0,
            "independent_development_checks": 0,
        }


def compact_bump(y, centre, radius):
    z = (y - centre) / radius
    if abs(z) >= 1.0:
        return 0.0
    return math.exp(1.0 - 1.0 / (1.0 - z * z))


def basis(y):
    fine = [compact_bump(y, c, FINE_RADIUS) for c in FINE_CENTRES]
    raw = [compact_bump(y, c, WIDE_RADIUS) for c in WIDE_CENTRES]
    denominator = 1.0 + sum(raw)
    return np.asarray(fine + [b / denominator for b in raw], dtype=float)


def smooth_switch(z):
    if z <= 0.0:
        return 0.0
    if z >= 1.0:
        return 1.0
    a = math.exp(-1.0 / z)
    b = math.exp(-1.0 / (1.0 - z))
    return a / (a + b)


def germ_data(y):
    """Exact formulas for U=psi3(y-1), p, r, v=p^(2/3), v', v''."""
    if y <= 0.0:
        return (0.0,) * 6
    d = 2.0 * y - y * y
    a = 1.0 - y
    log_u = -3.0 / d
    kappa = 6.0 * a / (d * d)
    log_kappa_derivative = -1.0 / a - 4.0 * a / d
    kappa_prime = kappa * log_kappa_derivative
    u = math.exp(log_u)
    p = kappa * u
    r = (kappa * kappa + kappa_prime) * u
    log_v = (2.0 / 3.0) * (log_u + math.log(kappa))
    v = math.exp(log_v)
    g = kappa + log_kappa_derivative
    g_prime = (kappa_prime - 1.0 / (a * a)
               + 4.0 / d + 8.0 * a * a / (d * d))
    vp = (2.0 / 3.0) * g * v
    vpp = v * ((4.0 / 9.0) * g * g + (2.0 / 3.0) * g_prime)
    return u, p, r, v, vp, vpp


def rho_base(y):
    if y >= 3.0 / 16.0:
        return 1.0 - y
    rho_g = germ_data(y)[5]
    if y <= 1.0 / 8.0:
        return rho_g
    z = (y - 1.0 / 8.0) / (1.0 / 16.0)
    chi = smooth_switch(z)
    return (1.0 - chi) * rho_g + chi * (1.0 - y)


def density(u, p, r):
    values = np.zeros(8, dtype=float)
    gradient = np.zeros((8, 3), dtype=float)
    variables = (u, p, r)
    for k, coefficient, a, b, c in MONOMIALS:
        powers = (a, b, c)
        monomial = coefficient
        for value, power in zip(variables, powers):
            monomial *= value ** power
        values[k] += monomial
        for variable in range(3):
            power = powers[variable]
            if power == 0:
                continue
            derivative = coefficient * power
            for j, (value, exponent) in enumerate(zip(variables, powers)):
                derivative *= value ** (exponent - (1 if j == variable else 0))
            gradient[k, variable] += derivative
    return values, gradient


def translation_matrix(t):
    powers = [1.0]
    for _ in range(7):
        powers.append(powers[-1] * t)
    matrix = np.zeros((8, 8), dtype=float)
    for j in range(8):
        for k in range(j, 8):
            matrix[j, k] = BINOMIAL[j][k] * powers[k - j]
    return matrix


class Jet:
    def __init__(self, value, derivative=None):
        self.value = float(value)
        self.derivative = (np.zeros(N, dtype=float) if derivative is None
                           else np.asarray(derivative, dtype=float))

    @staticmethod
    def get(other):
        return other if isinstance(other, Jet) else Jet(other)

    def __add__(self, other):
        o = self.get(other)
        return Jet(self.value + o.value, self.derivative + o.derivative)

    __radd__ = __add__

    def __neg__(self):
        return Jet(-self.value, -self.derivative)

    def __sub__(self, other):
        return self + (-self.get(other))

    def __rsub__(self, other):
        return self.get(other) - self

    def __mul__(self, other):
        o = self.get(other)
        return Jet(self.value * o.value,
                   self.derivative * o.value + self.value * o.derivative)

    __rmul__ = __mul__

    def __truediv__(self, other):
        o = self.get(other)
        return Jet(self.value / o.value,
                   (self.derivative * o.value - self.value * o.derivative) /
                   (o.value * o.value))

    def __rtruediv__(self, other):
        return self.get(other) / self

    def __pow__(self, exponent):
        if not isinstance(exponent, int):
            raise TypeError("only integer jet powers")
        if exponent == 0:
            return Jet(1.0)
        return Jet(self.value ** exponent,
                   exponent * self.value ** (exponent - 1) * self.derivative)


def complete_gates(h, a):
    """R471's complete six beta coefficients, s=1; no principal substitution."""
    a0, a1, a2, a3, a4, a5, a6, a7 = a
    b1 = (a1 + 24*h**2*(2*h-1)*a7 + 6*(1/h-1)*a0
          - (5/2)*h**2 + (21/5)*h**3)
    b2 = (a2 + (48*h-84*h**2-8*h**3)*a7
          + (-9/h**2+9/h+1)*a0
          + (9/2)*h - (147/20)*h**2 - (7/10)*h**3)
    b3 = (a3 + (-24+60*h**2)*a7 + (4/h**3+3/h**2-8/h)*a0
          - 21/10 + (3/5)*h + (103/20)*h**2)
    b4 = (a4 + (36-40*h)*a7 + (-6/h**3+21/(4*h**2))*a0
          + 51/20 - (79/20)*h)
    b5 = (a5 + (-18+8*h)*a7 + (10-6*h)/(4*h**3)*a0
          - 7/8 + (9/10)*h)
    b6 = (a6 + (5+2*h)*a7 - (1+h)/(4*h**3)*a0
          + (3/80)*(1+4*h))
    beta = (b1, b2, b3, b4, b5, b6)
    rr = (
        48*h**2-120*h**3,
        -96*h+240*h**2+20*h**3,
        48-72*h-168*h**2,
        -48+164*h,
        -4-34*h,
        8-5*h,
    )
    reduced = tuple(beta[j] - rr[j]*b5/rr[4] for j in (0, 1, 2, 3, 5))
    delta = tuple(rr[4]*x for x in reduced)
    return beta, rr, reduced, delta


def endpoint_pack(state, parameters, integral_id, phase, settings, diagnostics):
    v, w, u = (math.exp(float(state[j, 0])) for j in range(3))
    if min(v, w, u) <= 0.0:
        raise ArithmeticError("nonpositive computed endpoint state")
    p = v ** 1.5
    r = 1.5 * math.sqrt(v) * w
    s = p / r
    h = u * r / (p * p)
    v_d, w_d, u_d = state[0, 1:], state[1, 1:], state[2, 1:]
    # The first three sensitivity rows are derivatives of log(v), log(v'), log(u).
    log_r_d = 0.5*v_d + w_d
    log_s_d = v_d - w_d
    h_d = h*(u_d - 2.5*v_d + w_d)
    aa, aa_d = [], []
    for j in range(8):
        scale = r**(-5) * s**(-(8-j))
        value = scale * state[3+j, 0]
        derivative = scale * (
            state[3+j, 1:] - state[3+j, 0] *
            (5*log_r_d + (8-j)*log_s_d))
        aa.append(value)
        aa_d.append(derivative)
    hh = Jet(h, h_d)
    aj = [Jet(aa[j], aa_d[j]) for j in range(8)]
    beta, rr, reduced, delta = complete_gates(hh, aj)
    f = np.asarray([x.value for x in reduced])
    jac = np.asarray([x.derivative for x in reduced])
    dd = np.asarray([x.value for x in delta])
    delta_jac = np.asarray([x.derivative for x in delta])
    z = complex(1.0, math.sqrt(2*h-1))
    end_primitive = (
        z**3*(1-z)**5/10 + z**4*(1-z)**4/4
        + z**5*(1-z)**3/4 + z**6*(1-z)**2/8
        + z**7*(1-z)/16 + z**8/40
    )
    ee = sum(aa[j]*z**j for j in range(8)) - end_primitive
    arrays = (state, np.asarray(aa), f, jac, dd, delta_jac)
    if not all(np.all(np.isfinite(x)) for x in arrays):
        raise ArithmeticError("nonfinite complete target or sensitivity")
    if not (math.isfinite(ee.real) and math.isfinite(ee.imag)):
        raise ArithmeticError("nonfinite complete E diagnostic")
    q_endpoint = 0.75*w*w/math.sqrt(v)
    return {
        "integral_id": integral_id, "phase": phase,
        "parameters": np.asarray(parameters).tolist(), "settings": settings,
        "raw_endpoint": {"u": u, "p": p, "r": r, "v": v, "v_prime": w,
                         "q": q_endpoint, "A_f_prime_exact_formula": -9*v*v},
        "raw_moment_coefficients": state[3:, 0].tolist(),
        "normalization": {"s_before_normalization": s, "H": h,
                          "positive_width_b": 1/s,
                          "positive_amplitude_a": 1/(s*s*r)},
        "A_normalized": aa,
        "beta_1_to_6": [x.value for x in beta],
        "R_1_to_6": [x.value for x in rr],
        "Delta_labels": TAGS, "Delta": dd.tolist(),
        "Delta_parameter_jacobian": delta_jac.tolist(),
        "reduced_Delta_over_R5": f.tolist(),
        "reduced_parameter_jacobian": jac.tolist(),
        "candidate_proportion_c": (1152*beta[4]/rr[4]).value,
        "complete_E_upper_root": {"real": ee.real, "imag": ee.imag},
        "diagnostics": diagnostics,
        "classification": "floating_integral_and_sensitivity_only",
        "rigorous_zero_or_global_nonexistence": False,
    }


def restore_paid_prefix(request, ledger):
    """One read of the original failed job; no germ or quadrature evaluation."""
    ledger.stage = "read_paid_cap5_prefix_and_failed_account"
    import read_original_actions_log as reader
    if (request.get("continuation_policy") != CONTINUATION_POLICY
            or request.get("carried_source") != CARRIED_SOURCE
            or request.get("carried_records") != CARRIED_RECORDS
            or request.get("startup_control") != {
                "first_step": FIRST_STEP, "no_exponential_clipping": True,
                "same_math_family_targets_and_six_starts": True}):
        raise ValueError("the exact source failure and one startup repair are required")
    ledger.check()
    api = reader.GitHubReader(CARRIED_SOURCE["repository"])
    run_meta = api.api_json("/actions/runs/" + CARRIED_SOURCE["run_id"])
    job_meta = api.api_json("/actions/jobs/" + CARRIED_SOURCE["job_id"])
    if not (str(run_meta["id"]) == str(job_meta["run_id"]) == CARRIED_SOURCE["run_id"]
            and str(job_meta["id"]) == CARRIED_SOURCE["job_id"]
            and run_meta["head_sha"] == job_meta["head_sha"] == CARRIED_SOURCE["source_commit"]
            and run_meta["status"] == job_meta["status"] == "completed"
            and run_meta["conclusion"] == job_meta["conclusion"] == "failure"
            and run_meta["path"] == CARRIED_SOURCE["workflow"]):
        raise ValueError("the original failed cap5 run/job/source differs")
    ledger.check()
    original_request = CARRIED_SOURCE["original_request"]
    original_request_bytes = api.content(
        original_request["path"], CARRIED_SOURCE["source_commit"], 8192)
    if (len(original_request_bytes) != original_request["bytes"]
            or hashlib.sha256(original_request_bytes).hexdigest() != original_request["sha256"]):
        raise ValueError("the original mathematical request changed")
    original = reader.decode_json(original_request_bytes)
    for name in ("schema", "entry_point", "limits", "dependencies", "family",
                 "starts", "mathematical_sources", "classification"):
        if request.get(name) != original.get(name):
            raise ValueError("startup repair changed the original mathematical request: " + name)
    ledger.check()
    raw, redirects = api.job_log(CARRIED_SOURCE["job_id"])
    if (len(raw) != CARRIED_SOURCE["log_bytes"]
            or hashlib.sha256(raw).hexdigest() != CARRIED_SOURCE["log_sha256"]):
        raise ValueError("the original failed cap5 raw stdout changed")
    expected = {(pin["tag"], pin["record"]): pin for pin in CARRIED_RECORDS}
    saved, complete_records, clocks = {}, [], []
    record_output_bytes = 0
    for line in io.StringIO(raw.decode("utf-8-sig")):
        clean = reader.ANSI.sub("", line.rstrip("\r\n")).lstrip("\ufeff")
        match = reader.TIME_PREFIX.match(clean)
        if match is None:
            continue
        body = match.group(2).lstrip("\ufeff")
        tag, sep, payload = body.partition(" ")
        if not sep or tag not in ("CAP5_RECORD", "CAP5_FINAL_CLOCK"):
            continue
        ledger.check()
        literal = payload.encode("utf-8") + b"\n"
        value = reader.decode_json(literal)
        if tag == "CAP5_RECORD":
            complete_records.append(value)
            record_output_bytes += len((tag+" ").encode("utf-8")) + len(literal)
            key = (tag, value.get("record"))
        else:
            clocks.append(value)
            key = (tag, None)
        if key in expected:
            pin = expected[key]
            if (len(literal) != pin["bytes"]
                    or hashlib.sha256(literal).hexdigest() != pin["sha256"]
                    or (tag == "CAP5_RECORD" and value.get("kind") != pin["kind"])):
                raise ValueError("the paid cap5 record bytes/hash changed: " + str(key))
            if key in saved:
                raise ValueError("duplicate paid cap5 record")
            saved[key] = value
    del raw
    if (set(saved) != set(expected) or len(clocks) != 1
            or [x.get("record") for x in complete_records] != list(range(1, 7))
            or record_output_bytes != CARRIED_RECORD_OUTPUT_BYTES):
        raise ValueError("the complete paid failure/prefix record sequence is required")
    prefix = saved[("CAP5_RECORD", 3)]["data"]
    failure = saved[("CAP5_RECORD", 5)]["data"]
    report = saved[("CAP5_RECORD", 6)]["data"]
    clock = saved[("CAP5_FINAL_CLOCK", None)]
    cost = report["costs_before_final_output"]
    if not (clock["entry_elapsed_seconds_including_output"] == CARRIED_SECONDS
            and clock["authoritative_clock_supersedes_pre_output_costs"] is True
            and clock["integrals_started"] == cost["integrals_started"] == CARRIED_STARTED
            and clock["integrals_completed"] == cost["integrals_completed"] == CARRIED_COMPLETED
            and clock["integrals_failed"] == cost["integrals_failed"] == CARRIED_FAILED
            and cost["rhs_calls"] == CARRIED_RHS_CALLS
            and cost["prefix_quadrature_calls"] == CARRIED_PREFIX_CALLS
            and report["status"] == "partial_or_entry_failure"
            and failure["integral_id"] == 2 and failure["rhs_calls_actual"] == CARRIED_RHS_CALLS
            and failure["error"] == "OverflowError('math range error')"
            and report["request_bytes"] == original_request["bytes"]
            and report["request_sha256"] == original_request["sha256"]
            and report["partial_progress"]["best"] is None
            and report["partial_progress"]["starts"] == []
            and report["partial_progress"]["refinements"] == []):
        raise ValueError("the prior failed startup account or unchanged-search state differs")
    restored = copy.deepcopy(report["partial_progress"]["prefix"])
    if not (prefix["integral_id"] == 1
            and prefix["original_interval_not_truncated"] == [0.0, A_START]
            and prefix["coefficients"] == restored["coefficients"]
            and prefix["initial_u_v_vprime"] == [restored["u"], restored["v"], restored["v_prime"]]
            and prefix["estimated_error_not_rigorous"] == restored["estimated_error"]
            and report["partial_progress"]["last_completed"]["prefix"] == restored
            and len(restored["coefficients"]) == 8
            and all(math.isfinite(x) for x in restored["coefficients"])
            and all(math.isfinite(restored[k]) and restored[k] > 0
                    for k in ("u", "v", "v_prime"))):
        raise ValueError("the exact paid prefix payload is incomplete")
    ledger.prefix = restored
    ledger.last_started = copy.deepcopy(report["partial_progress"]["last_started"])
    ledger.last_rhs = copy.deepcopy(report["partial_progress"]["last_rhs"])
    ledger.last_completed = copy.deepcopy(report["partial_progress"]["last_completed"])
    ledger.carried_receipt = {
        "policy": CONTINUATION_POLICY, "source": copy.deepcopy(CARRIED_SOURCE),
        "records": copy.deepcopy(CARRIED_RECORDS), "source_final_clock": copy.deepcopy(clock),
        "carried_counts": {"started": CARRIED_STARTED, "completed": CARRIED_COMPLETED,
                           "failed": CARRIED_FAILED, "rhs": CARRIED_RHS_CALLS,
                           "prefix_callbacks": CARRIED_PREFIX_CALLS},
        "prefix_original_integral_id": 1, "failed_original_integral_id": 2,
        "no_completed_cap_was_available": True, "next_integral_id": 3,
        "original_math_request_compared_field_by_field": True,
        "redirect_count_no_credential_forwarding": redirects,
        "new_prefix_quadrature_calls": 0}
    ledger.carried_receipt_verified = True
    ledger.emit("PREFIX_RESTORED", {
        "prefix": ledger.prefix, "paid_source": ledger.carried_receipt,
        "first_step": FIRST_STEP,
        "no_new_integral_or_prefix_rhs_charged_for_restore": True,
        "all_read_import_and_serialization_seconds_in_same_remaining_budget": True,
        "costs": ledger.costs()})
    ledger.check()

def evaluate(ledger, parameters, phase, rtol, atol, max_step):
    parameters = np.asarray(parameters, dtype=float)
    if parameters.shape != (N,) or not np.all(np.isfinite(parameters)):
        raise ValueError("parameter vector must be finite length 15")
    if np.max(np.abs(parameters)) > 6.000000000001:
        raise ValueError("fixed parameter box exceeded")
    key = (tuple(float(x).hex() for x in parameters),
           float(rtol), float(atol), float(max_step), FIRST_STEP)
    if key in ledger.cache:
        ledger.cache_hits += 1
        ledger.check(phase)
        return ledger.cache[key]
    settings = {"method": "DOP853", "rtol": rtol, "atol": atol,
                "max_step": max_step, "first_step": FIRST_STEP,
                "analytic_sensitivities": N,
                "positive_state_coordinates": "log(v),log(v_prime),log(u)"}
    ledger.stage = "new_cap_integral_" + phase
    iid = ledger.charge(phase, {"parameters": parameters.tolist(),
                               "settings": settings})
    started = time.perf_counter()
    rhs_before = ledger.rhs_calls
    state0 = np.zeros((11, N+1), dtype=float)
    state0[0, 0] = math.log(ledger.prefix["v"])
    state0[1, 0] = math.log(ledger.prefix["v_prime"])
    state0[2, 0] = math.log(ledger.prefix["u"])
    state0[3:, 0] = ledger.prefix["coefficients"]
    try:
        def rhs(y, flat):
            ledger.rhs_calls += 1
            ledger.check(phase)
            state = flat.reshape(11, N+1)
            logs = [float(state[j, 0]) for j in range(3)]
            ledger.last_rhs = {"integral_id": iid, "coordinate": float(y),
                               "log_v_log_vprime_log_u": logs}
            # Preserve the actual failing stage if exp raises; never clip it.
            v, w, u = (math.exp(value) for value in logs)
            ledger.last_rhs.update(v=float(v), v_prime=float(w), u=float(u))
            if v <= 0.0 or w <= 0.0 or u < 0.0:
                raise ArithmeticError("nonpositive floating interior state")
            bb = basis(float(y))
            rho = rho_base(float(y)) * math.exp(float(bb @ parameters))
            if rho < 0.0 or not math.isfinite(rho):
                raise ArithmeticError("invalid floating curvature")
            sv = math.sqrt(v)
            p = v*sv
            r = 1.5*sv*w
            ud = u*state[2, 1:]
            pd = 1.5*p*state[0, 1:]
            rd = r*(0.5*state[0, 1:] + state[1, 1:])
            ll, gradient = density(u, p, r)
            tt = translation_matrix(float(y)-1.0)
            out = np.empty_like(state)
            out[0, 0] = w/v
            out[0, 1:] = (w/v)*(state[1, 1:]-state[0, 1:])
            out[1, 0] = rho/w
            out[1, 1:] = (rho/w)*(bb-state[1, 1:])
            out[2, 0] = p/u
            out[2, 1:] = (p/u)*(1.5*state[0, 1:]-state[2, 1:])
            out[3:, 0] = tt @ ll
            out[3:, 1:] = tt @ (
                gradient @ np.vstack((ud, pd, rd)))
            if not np.all(np.isfinite(out)):
                raise ArithmeticError("nonfinite complete ODE derivative")
            return out.ravel()
        sol = solve_ivp(
            rhs, (A_START, 1.0), state0.ravel(), method="DOP853",
            rtol=rtol, atol=atol, max_step=max_step,
            first_step=FIRST_STEP, dense_output=False)
        if not sol.success or abs(float(sol.t[-1])-1.0) > 1e-14:
            raise ArithmeticError("complete cap integration did not reach endpoint: " +
                                  str(sol.message))
        state = sol.y[:, -1].reshape(11, N+1)
        pack = endpoint_pack(
            state, parameters, iid, phase, settings,
            {"solver_nfev": int(sol.nfev),
             "rhs_calls_actual": ledger.rhs_calls-rhs_before,
             "accepted_solver_steps": int(len(sol.t)-1),
             "elapsed_integral": time.perf_counter()-started,
             "solver_message": str(sol.message)})
        ledger.integrals_completed += 1
        ledger.cache[key] = pack
        ledger.last_completed = pack
        ledger.emit("INTEGRAL_COMPLETE", pack)
        return pack
    except Exception as exc:
        ledger.integrals_failed += 1
        ledger.emit("INTEGRAL_FAILED", {
            "integral_id": iid, "phase": phase, "error": repr(exc),
            "elapsed_integral": time.perf_counter()-started,
            "rhs_calls_actual": ledger.rhs_calls-rhs_before,
            "last_rhs": ledger.last_rhs, "costs": ledger.costs()})
        raise


def update_best(ledger, pack):
    f = np.asarray(pack["reduced_Delta_over_R5"])
    weighted = ledger.whitener @ f
    merit = float(weighted @ weighted)
    if ledger.best is None or merit < ledger.best["merit"]:
        ledger.best = {"merit": merit, "pack": pack,
                       "weighted_residual": weighted.tolist()}
        ledger.emit("BEST_UPDATE", {
            "integral_id": pack["integral_id"], "merit": merit,
            "weighted_residual": weighted.tolist(),
            "reduced_residual_inf": float(np.max(np.abs(f))),
            "parameters": pack["parameters"],
            "H": pack["normalization"]["H"]})
    return weighted


def validate_request(request, ledger):
    if request.get("schema") != SCHEMA:
        raise ValueError("request schema mismatch")
    if request.get("entry_point") != "scripts/literature_cap5_positive_curvature_search.py":
        raise ValueError("entry point mismatch")
    if request.get("limits") != {
        "seconds": 120, "started_integrals": 400, "search_seconds": 112,
        "search_integrals": 397, "per_start_nfev": 64, "parameter_bound": 6,
        "stdout_soft_bytes": 3000000,
    }:
        raise ValueError("request must retain fixed limits")
    expected_paths = {"scripts/literature_cap5_positive_curvature_search.py",
                      "notes/cap-five-positive-curvature-search-design-20261116.md",
                      REPAIR_DESIGN}
    if {x.get("path") for x in request.get("source_manifest", [])} != expected_paths:
        raise ValueError("entry, original design and one repair addendum are required")
    for item in request.get("source_manifest", []):
        path = ROOT / item["path"]
        data = path.read_bytes()
        if len(data) != item["bytes"] or hashlib.sha256(data).hexdigest() != item["sha256"]:
            raise ValueError("bound source bytes/hash changed: " + item["path"])
    if request.get("scientific_inputs") != "same_cap5_family_paid_prefix_only_one_startup_repair":
        raise ValueError("unexpected input scope")
    starts = request["starts"]
    if len(starts) != 6 or any(len(x) != N for x in starts):
        raise ValueError("exactly six fixed fifteen-parameter starts required")
    if any(not math.isfinite(float(y)) or abs(float(y)) > 6 for x in starts for y in x):
        raise ValueError("invalid start")
    if starts[0] != [0]*N:
        raise ValueError("first start is the family origin")
    ledger.check()


def run(request, ledger):
    global np, solve_ivp, least_squares
    # Restore only the paid prefix/account before any new scientific call.
    validate_request(request, ledger)
    restore_paid_prefix(request, ledger)
    ledger.stage = "scientific_imports"
    import numpy
    import scipy
    from scipy.integrate import solve_ivp as sivp
    from scipy.optimize import least_squares as ls
    np, solve_ivp, least_squares = numpy, sivp, ls
    if platform.python_version() != "3.12.14":
        raise ValueError("Python version must be 3.12.14")
    if np.__version__ != "2.3.5" or scipy.__version__ != "1.17.0":
        raise ValueError("scientific dependency pin mismatch")
    for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
                 "NUMEXPR_NUM_THREADS"):
        if os.environ.get(name) != "1":
            raise ValueError("single thread pin missing: " + name)
    ledger.emit("ENTRY", {
        "python": platform.python_version(), "numpy": np.__version__,
        "scipy": scipy.__version__, "family": request["family"],
        "only_paid_prefix_reused_no_old_self_rank_or_psi3E": True,
        "continuation_policy": CONTINUATION_POLICY,
        "startup_first_step": FIRST_STEP, "costs": ledger.costs()})
    base = evaluate(ledger, np.zeros(N), "search", 2e-9, 1e-13, 1/128)
    ledger.check("search")
    jac0 = np.asarray(base["reduced_parameter_jacobian"])
    uu, singular, _ = np.linalg.svd(jac0, full_matrices=False)
    floor = max(1e-10, float(singular[0])*1e-4)
    ledger.whitener = (uu*(1.0/np.maximum(singular, floor))) @ uu.T
    ledger.whitening_singular_values = singular.tolist()
    ledger.emit("FIXED_SEARCH_PRECONDITIONER", {
        "from_integral_id": base["integral_id"],
        "floating_singular_values_not_exact_rank": singular,
        "floor": floor, "matrix": ledger.whitener,
        "fixed_for_all_six_starts": True})
    update_best(ledger, base)
    candidate_stop = False
    search_stopped = None
    for index, start in enumerate(request["starts"]):
        before = ledger.integrals_started
        start_time = ledger.elapsed()
        entry = {"index": index, "parameters": start,
                 "integrals_started_before": before, "elapsed_before": start_time}
        ledger.starts.append(entry)
        ledger.emit("START_BEGIN", entry)
        try:
            def fun(c):
                pack = evaluate(ledger, c, "search", 2e-9, 1e-13, 1/128)
                ledger.check("search")
                weighted = update_best(ledger, pack)
                f = np.asarray(pack["reduced_Delta_over_R5"])
                if np.max(np.abs(f)) <= 1e-8 and np.max(np.abs(weighted)) <= 1e-8:
                    raise CandidateFound("small floating five-residual candidate")
                return weighted

            def jac(c):
                pack = evaluate(ledger, c, "search", 2e-9, 1e-13, 1/128)
                ledger.check("search")
                return ledger.whitener @ np.asarray(pack["reduced_parameter_jacobian"])

            fit = least_squares(
                fun, np.asarray(start, dtype=float), jac=jac,
                bounds=(-6*np.ones(N), 6*np.ones(N)),
                method="trf", tr_solver="exact", x_scale=np.ones(N),
                ftol=1e-11, xtol=1e-11, gtol=1e-11, max_nfev=64)
            entry.update({
                "status": int(fit.status), "message": str(fit.message),
                "nfev": int(fit.nfev), "njev": int(fit.njev),
                "final_parameters": fit.x.tolist(),
                "floating_cost": float(fit.cost),
                "floating_optimality": float(fit.optimality)})
        except CandidateFound as exc:
            entry.update({"status": "candidate_stop", "message": str(exc)})
            candidate_stop = True
        except (SearchStop, BudgetStop) as exc:
            entry.update({"status": "budget_stop", "message": str(exc)})
            search_stopped = str(exc)
        except Exception as exc:
            entry.update({"status": "failed_start", "error": repr(exc),
                          "traceback": traceback.format_exc(limit=8)})
        entry.update({"integrals_started_after": ledger.integrals_started,
                      "elapsed_after": ledger.elapsed()})
        ledger.emit("START_END", entry)
        if candidate_stop or search_stopped:
            break

    if ledger.best is not None:
        parameters = ledger.best["pack"]["parameters"]
        for phase, rtol, atol, step in (
                ("refine_1", 2e-11, 2e-15, 1/192),
                ("refine_2", 2e-13, 2e-16, 1/256)):
            try:
                pack = evaluate(ledger, parameters, phase, rtol, atol, step)
                ledger.refinements.append(pack)
                ledger.emit("CANDIDATE_REFINEMENT", {
                    "phase": phase, "integral_id": pack["integral_id"],
                    "reduced_residual_inf": max(abs(x) for x in pack["reduced_Delta_over_R5"]),
                    "strictly_same_parameters": True,
                    "not_a_rigorous_error_enclosure": True})
            except Exception as exc:
                ledger.events.append({"phase": phase, "error": repr(exc)})
                ledger.emit("REFINEMENT_FAILED", {
                    "phase": phase, "error": repr(exc), "costs": ledger.costs()})
                break

    outcome = "bounded_search_no_certified_zero"
    refinement_comparison = None
    if len(ledger.refinements) == 2:
        first, second = ledger.refinements
        f1 = np.asarray(first["reduced_Delta_over_R5"])
        f2 = np.asarray(second["reduced_Delta_over_R5"])
        refinement_comparison = {
            "same_parameters": True,
            "reduced_residual_inf": float(np.max(np.abs(f2))),
            "fixed_weighted_residual_inf": float(np.max(np.abs(ledger.whitener @ f2))),
            "two_refinements_difference_inf": float(np.max(np.abs(f2-f1))),
            "A_difference_inf": float(np.max(np.abs(
                np.asarray(second["A_normalized"])-np.asarray(first["A_normalized"])))),
            "Jacobian_difference_inf": float(np.max(np.abs(
                np.asarray(second["reduced_parameter_jacobian"])-
                np.asarray(first["reduced_parameter_jacobian"])))),
            "rigorous_enclosure": False,
        }
        if (refinement_comparison["reduced_residual_inf"] <= 1e-8 and
                refinement_comparison["fixed_weighted_residual_inf"] <= 1e-7 and
                refinement_comparison["two_refinements_difference_inf"] <= 1e-9):
            outcome = "floating_small_residual_candidate_no_rigorous_inclusion"
    return {
        "outcome": outcome, "candidate_stop": candidate_stop,
        "search_stopped": search_stopped,
        "full_five_zero_proved": False,
        "global_nonexistence_proved": False,
        "full_library_or_actual_joint_installed": False,
        "fixed_preconditioner": ledger.whitener,
        "whitening_singular_values": ledger.whitening_singular_values,
        "best": ledger.best, "starts": ledger.starts,
        "refinement_integral_ids": [x["integral_id"] for x in ledger.refinements],
        "final_refined_complete_target": ledger.refinements[-1] if ledger.refinements else None,
        "refinement_comparison": refinement_comparison,
        "events": ledger.events,
    }


def main():
    ledger = Ledger()
    report = {"schema": SCHEMA, "status": "entry_started"}
    out_path = None
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--request", required=True)
        parser.add_argument("--out", required=True)
        args = parser.parse_args()
        out_path = pathlib.Path(args.out)
        ledger.stage = "request_read"
        request_bytes = pathlib.Path(args.request).read_bytes()
        request = json.loads(request_bytes.decode("utf-8"))
        report["request_sha256"] = hashlib.sha256(request_bytes).hexdigest()
        report["request_bytes"] = len(request_bytes)
        report["result"] = run(request, ledger)
        report["status"] = "complete_bounded_observation"
    except BaseException as exc:
        report["status"] = "partial_or_entry_failure"
        report["error"] = repr(exc)
        report["traceback"] = traceback.format_exc(limit=12)
    finally:
        report["last_stage"] = ledger.stage
        report["costs_before_final_output"] = ledger.costs()
        report["carried_source_receipt"] = ledger.carried_receipt
        report["continuation_policy"] = CONTINUATION_POLICY
        report["startup_first_step"] = FIRST_STEP
        report["partial_progress"] = {
            "last_started": ledger.last_started,
            "last_rhs": ledger.last_rhs,
            "last_completed": ledger.last_completed,
            "prefix": ledger.prefix,
            "best": ledger.best,
            "starts": ledger.starts,
            "refinements": ledger.refinements,
            "events": ledger.events,
        }
        try:
            encoded = json.dumps(finite_json(report), ensure_ascii=False,
                                 separators=(",", ":"), allow_nan=False) + "\n"
            if out_path is not None:
                out_path.parent.mkdir(parents=True, exist_ok=True)
                out_path.write_text(encoded, encoding="utf-8")
            ledger.emit("FINAL_REPORT", report)
        except BaseException as exc:
            print("CAP5_FINAL_OUTPUT_FAILURE " + json.dumps({
                "error": repr(exc), "costs": ledger.costs(),
                "no_further_science": True}, allow_nan=False), flush=True)
        current_elapsed = time.perf_counter() - ENTRY_STARTED
        final_elapsed = CARRIED_SECONDS + current_elapsed
        print("CAP5_FINAL_CLOCK " + json.dumps({
            "schema": SCHEMA, "entry_elapsed_seconds_including_output": current_elapsed,
            "carried_failed_attempt_seconds": CARRIED_SECONDS,
            "total_same_scope_seconds_including_carried": final_elapsed,
            "same_original120_second_allocation_not_reset": True,
            "carried_receipt_verified": ledger.carried_receipt_verified,
            "current_process_integrals_started": ledger.integrals_started-CARRIED_STARTED,
            "current_process_integrals_completed": ledger.integrals_completed-CARRIED_COMPLETED,
            "current_process_integrals_failed": ledger.integrals_failed-CARRIED_FAILED,
            "rhs_calls": ledger.rhs_calls, "prefix_quadrature_calls": ledger.prefix_calls,
            "authoritative_clock_supersedes_pre_output_costs": True,
            "budget_seconds": 120.0, "overrun": final_elapsed > 120.0,
            "integrals_started": ledger.integrals_started,
            "integrals_completed": ledger.integrals_completed,
            "integrals_failed": ledger.integrals_failed,
            "rss_max_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            "no_further_science": True}, allow_nan=False), flush=True)
    return 0 if report["status"] == "complete_bounded_observation" else 1


if __name__ == "__main__":
    sys.exit(main())
