#!/usr/bin/env python3
"""One new complete-cap5 LP and exact integral-defect judge; no old science."""
import time
ENTRY_STARTED_AT = time.perf_counter()

import argparse
import array
import functools
import hashlib
import json
import math
import os
from pathlib import Path
import resource
import sys
import traceback
from fractions import Fraction as F
from itertools import product

VERSION = "complete-cap5-integral-certificate-v1"
H_LO = F(3, 5)
H_HI = F(67, 36)
ROUND_POWER = 40
ROUND_DENOMINATOR = 1 << ROUND_POWER
FINAL_OUTPUT_RESERVE = 256 * 1024
GATE_IDS = (1, 2, 3, 4, 6)
PARAM_DEGREE = (8, 2)
END_DEGREE = (12, 1)
GENERATOR_NAMES = (
    "one_minus_p", "one_minus_r", "U_minus_C", "H_minus_U",
    "W_C", "S", "V", "G", "p_minus_r3",
)
GENERATOR_T_DEGREE = (0, 0, 0, 0, 0, 1, 1, 2, 0)
GENERATOR_MIN_WEIGHT = (0, 0, 0, 0, 2, 1, 0, 0, 1)


class StopBudget(RuntimeError):
    pass


class StopCap(RuntimeError):
    pass


def canonical_bytes(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")


def rational(value):
    value = F(value)
    return [str(value.numerator), str(value.denominator)]


def finite_float(value):
    value = float(value)
    return math.isfinite(value)


def rss_kib():
    return int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


class Progress:
    def __init__(self):
        self.started_at = ENTRY_STARTED_AT
        self.limit = None
        self.stage = "entry"
        self.stage_started = self.started_at
        self.stage_times = {}
        self.counts = {
            "new_lp_started": 0, "new_lp_returned": 0,
            "exact_judges_started": 0, "exact_judges_finished": 0,
            "assembly_columns_started": 0, "assembly_columns_finished": 0,
            "exact_columns_started": 0, "exact_columns_finished": 0,
            "old_cap_evaluations": 0, "old_mapper_calls": 0,
            "old_rank_calls": 0, "development_tests": 0,
        }
        self.data = {}
        self.output_limit = 40 * 1024 * 1024
        self.output_bytes = 0
        self.seq = 0
        self.chain = "0" * 64
        self.last_record = None
        self.failure = None

    def elapsed(self):
        return time.perf_counter() - self.started_at

    def configure(self, request):
        self.limit = float(request["budget"]["total_seconds"])
        if not (0 < self.limit <= 3600):
            raise ValueError("invalid explicit single-account total_seconds")
        solver_limit = float(request["budget"]["solver_seconds"])
        judge_reserve = float(request["budget"]["minimum_seconds_reserved_after_LP"])
        if not (0 < solver_limit <= self.limit and 0 < judge_reserve < self.limit):
            raise ValueError("invalid fixed LP limit or post-LP judge reserve")
        self.output_limit = int(request["budget"]["stdout_bytes"])
        if not (1024 * 1024 <= self.output_limit <= 128 * 1024 * 1024):
            raise ValueError("invalid stdout cap")
        self.check()

    def check(self):
        if self.limit is not None and self.elapsed() >= self.limit:
            raise StopBudget("the single entry/account deadline is exhausted")

    def remaining(self):
        if self.limit is None:
            return 0.0
        return max(0.0, self.limit - self.elapsed())

    def enter(self, stage):
        now = time.perf_counter()
        self.stage_times[self.stage] = self.stage_times.get(self.stage, 0.0) + (
            now - self.stage_started)
        self.stage = stage
        self.stage_started = now
        self.emit("stage_started", {"stage": stage, "entry_elapsed": self.elapsed()})
        self.check()

    def emit(self, kind, payload):
        body = canonical_bytes(payload)
        identity = hashlib.sha256(body).hexdigest()
        seq = self.seq + 1
        chain = hashlib.sha256(
            bytes.fromhex(self.chain) + str(seq).encode("ascii") +
            kind.encode("utf-8") + bytes.fromhex(identity)
        ).hexdigest()
        record = {
            "seq": seq, "kind": kind, "payload_bytes": len(body),
            "payload_sha256": identity, "previous_chain": self.chain,
            "chain": chain, "payload": payload,
        }
        line = b"CAP5_CERT_RECORD " + canonical_bytes(record) + b"\n"
        if self.output_bytes + len(line) > self.output_limit - FINAL_OUTPUT_RESERVE:
            self.data["output_cap_next"] = {
                "kind": kind, "required_record_bytes": len(line),
                "payload_sha256": identity,
                "already_emitted_bytes": self.output_bytes,
                "reserved_final_report_and_clock_bytes": FINAL_OUTPUT_RESERVE,
            }
            raise StopCap("full next record exceeds the declared stdout cap")
        sys.stdout.buffer.write(line)
        sys.stdout.buffer.flush()
        self.output_bytes += len(line)
        self.seq = seq
        self.chain = chain
        self.last_record = {"seq": seq, "kind": kind, "payload_sha256": identity}

    def snapshot(self):
        now = time.perf_counter()
        times = dict(self.stage_times)
        times[self.stage] = times.get(self.stage, 0.0) + now - self.stage_started
        return {
            "version": VERSION, "stage": self.stage,
            "entry_elapsed_before_final_output": self.elapsed(),
            "single_account_limit": self.limit,
            "stage_times": times, "counts": dict(self.counts),
            "peak_rss_kib": rss_kib(), "records": self.seq,
            "record_chain": self.chain, "record_bytes": self.output_bytes,
            "last_record": self.last_record,
            "failure": self.failure, "data": self.data,
            "final_clock_supersedes_this_pre_output_elapsed": True,
        }


P = Progress()


# Small exact parameter polynomials in (xi, zeta).
def pc(value):
    value = F(value)
    return {} if not value else {(0, 0): value}


def padd(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, F(0)) + value
        if not out[key]:
            del out[key]
    return out


def pscale(a, value):
    value = F(value)
    return {key: coeff * value for key, coeff in a.items() if coeff * value}


def pmul(a, b):
    out = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            key = (i + k, j + l)
            out[key] = out.get(key, F(0)) + x * y
    return {key: value for key, value in out.items() if value}


def ppow(a, degree):
    out = pc(1)
    for _ in range(degree):
        out = pmul(out, a)
    return out


def psig(a):
    return tuple((i, j, c.numerator, c.denominator)
                 for (i, j), c in sorted(a.items()))


def pfromsig(sig):
    return {(i, j): F(n, d) for i, j, n, d in sig}


@functools.lru_cache(maxsize=None)
def bernstein_basis(d, i, variable):
    if not (0 <= i <= d):
        raise ValueError("invalid Bernstein index")
    out = {}
    for k in range(d - i + 1):
        coeff = F(math.comb(d, i) * math.comb(d - i, k) * ((-1) ** k))
        key = (i + k, 0) if variable == 0 else (0, i + k)
        out[key] = coeff
    return psig(out)


def bp(dh, ih, dz, iz):
    return pmul(pfromsig(bernstein_basis(dh, ih, 0)),
                pfromsig(bernstein_basis(dz, iz, 1)))


@functools.lru_cache(maxsize=20000)
def bernstein_vector(sig, dh, dz):
    poly = pfromsig(sig)
    if any(i > dh or j > dz for i, j in poly):
        raise ValueError("parameter polynomial exceeds frozen degree")
    out = []
    for a in range(dh + 1):
        for b in range(dz + 1):
            value = F(0)
            for (i, j), coeff in poly.items():
                if i <= a and j <= b:
                    value += (coeff * F(math.comb(a, i), math.comb(dh, i))
                              * F(math.comb(b, j), math.comb(dz, j)))
            if value:
                out.append((a, b, value))
    return tuple(out)


# A state polynomial maps (T,U,p,r) exponents to a parameter polynomial.
def sadd(a, b):
    out = {key: dict(value) for key, value in a.items()}
    for key, value in b.items():
        merged = padd(out.get(key, {}), value)
        if merged:
            out[key] = merged
        else:
            out.pop(key, None)
    return out


def sparam(a, param):
    return {key: val for key, coeff in a.items()
            if (val := pmul(coeff, param))}


def sscale(a, scale):
    return sparam(a, pc(scale))


def sterm(state, coeff=1):
    coeff = coeff if isinstance(coeff, dict) else pc(coeff)
    return {} if not coeff else {tuple(state): coeff}


def hpoly(coefficients, hpowers):
    out = {}
    for power, value in coefficients.items():
        out = padd(out, pscale(hpowers[power], value))
    return out


def state_add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def make_math():
    H = {(0, 0): H_LO, (1, 0): H_HI - H_LO}
    ZETA = {(0, 1): F(1)}
    C = pmul(padd(H, pc(-H_LO)), ZETA)
    hp = [ppow(H, i) for i in range(13)]

    # The complete original twelve terms, grouped into eight ell_k.
    ell_raw = (
        ((1, 1, 2, 3, 0),),
        ((-1, 1, 1, 4, 0),),
        ((3, 2, 2, 1, 2), (3, 10, 0, 5, 0)),
        ((-1, 2, 2, 0, 3), (-3, 1, 1, 2, 2)),
        ((3, 2, 1, 1, 3), (3, 2, 0, 3, 2)),
        ((-1, 4, 1, 0, 4), (-1, 1, 0, 2, 3)),
        ((5, 16, 0, 1, 4),),
        ((-3, 80, 0, 0, 5),),
    )
    ell = []
    for terms in ell_raw:
        current = {}
        for num, den, u, p, r in terms:
            current = sadd(current, sterm((0, u, p, r), F(num, den)))
        ell.append(current)
    L = []
    for j in range(8):
        current = {}
        for k in range(j, 8):
            for state, param in ell[k].items():
                target = (k - j, state[1], state[2], state[3])
                current = sadd(current, sterm(
                    target, pscale(param, math.comb(k, j) * ((-1) ** (k - j)))))
        L.append(current)

    # Each tuple is (b_nu7, b_nu0, e_nu), as univariate H coefficients.
    table = {
        1: ({5: -1920, 6: 3840}, {2: 480, 3: -480},
            {5: -200, 6: 336}),
        2: ({4: 3840, 5: -6720, 6: -640},
            {1: -720, 2: 720, 3: 80},
            {4: 360, 5: -588, 6: -56}),
        3: ({3: -1920, 5: 4800}, {0: 320, 1: 240, 2: -640},
            {3: -168, 4: 48, 5: 412}),
        4: ({3: 2880, 4: -3200}, {0: -480, 1: 420},
            {3: 204, 4: -316}),
        5: ({3: -1440, 4: 640}, {0: 200, 1: -120},
            {3: -70, 4: 72}),
        6: ({3: 400, 4: 160}, {0: -20, 1: -20},
            {3: 3, 4: 12}),
    }
    rtable = {
        1: {2: 48, 3: -120}, 2: {1: -96, 2: 240, 3: 20},
        3: {0: 48, 1: -72, 2: -168}, 4: {0: -48, 1: 164},
        5: {0: -4, 1: -34}, 6: {0: 8, 1: -5},
    }
    Rs = {nu: hpoly(v, hp) for nu, v in rtable.items()}
    ds, es = {}, {}
    for nu, (b7, b0, e) in table.items():
        ds[nu] = sadd(sadd(sparam(L[nu], pscale(hp[3], 80)),
                          sparam(L[7], hpoly(b7, hp))),
                      sparam(L[0], hpoly(b0, hp)))
        es[nu] = hpoly(e, hp)
    gates, ends = {}, {}
    for nu in GATE_IDS:
        gates[nu] = sadd(sparam(ds[nu], Rs[5]),
                         sscale(sparam(ds[5], Rs[nu]), -1))
        ends[nu] = padd(pmul(Rs[5], es[nu]),
                        pscale(pmul(Rs[nu], es[5]), -1))

    one = sterm((0, 0, 0, 0))
    U = sterm((0, 1, 0, 0))
    pp = sterm((0, 0, 1, 0))
    rr = sterm((0, 0, 0, 1))
    gen = []
    gen.append(sadd(one, sscale(pp, -1)))
    gen.append(sadd(one, sscale(rr, -1)))
    gen.append(sadd(U, sterm((0, 0, 0, 0), pscale(C, -1))))
    gen.append(sadd(sterm((0, 0, 0, 0), H), sscale(U, -1)))
    gen.append(sadd(sadd(sterm((0, 1, 0, 1), 5),
                         sterm((0, 0, 0, 1), pscale(C, -5))),
                     sterm((0, 0, 2, 0), -3)))
    gen.append(sadd(sadd(sterm((0, 0, 1, 0), 3),
                         sterm((1, 0, 0, 1), 2)),
                     sterm((0, 0, 0, 1), -3)))
    gen.append(sadd(sadd(one, sscale(pp, -1)),
                     sterm((1, 0, 0, 1), -1)))
    gen.append(sadd(sadd(sadd(sterm((0, 0, 0, 0), pscale(H, 2)),
                              sterm((0, 1, 0, 0), -2)),
                          sterm((1, 0, 1, 0), -2)),
                      sterm((2, 0, 0, 1), -1)))
    gen.append(sadd(pp, sterm((0, 0, 0, 3), -1)))

    potentials = []
    for r in range(6):
        for p in range(6 - r):
            u = 5 - p - r
            if p + 2 * r >= 2:
                for t in range(p + 2 * r - 1):
                    potentials.append((t, u, p, r))
    potentials.sort()
    if len(potentials) != 85:
        raise ValueError("frozen 85-potential basis does not reconstruct")
    for t, u, p, r in potentials:
        if u + p + r != 5 or p + 2*r - t < 2:
            raise ValueError("invalid potential tail weight")

    identity = {
        "ell_raw": ell_raw, "integer_gate_table": table,
        "R_table": rtable, "height_interval": [rational(H_LO), rational(H_HI)],
        "potential_basis": potentials, "generator_names": GENERATOR_NAMES,
        "generator_T_degree": GENERATOR_T_DEGREE,
        "generator_min_weight": GENERATOR_MIN_WEIGHT,
        "rounding_denominator": str(ROUND_DENOMINATOR),
        "gate_ids": GATE_IDS,
    }
    return {
        "H": H, "C": C, "hp": hp, "L": L, "gates": gates, "ends": ends,
        "gen": gen, "potentials": potentials,
        "identity": identity,
        "identity_sha256": hashlib.sha256(canonical_bytes(identity)).hexdigest(),
    }


def multiplier_states(tag, gi):
    state_limit = 6 if tag == "A" else 4
    needed = 4 if tag == "A" else 0
    tlimit = 8 - GENERATOR_T_DEGREE[gi]
    lower = needed - GENERATOR_MIN_WEIGHT[gi]
    for u in range(state_limit + 1):
        for p in range(state_limit - u + 1):
            for r in range(state_limit - u - p + 1):
                for t in range(tlimit + 1):
                    if p + 2*r - t >= lower:
                        yield (t, u, p, r)


def variables(mathdata):
    for ih, iz in product(range(2), repeat=2):
        for nu in GATE_IDS:
            for sign in (1, -1):
                yield ("n", nu, ih, iz, sign)
    for state in mathdata["potentials"]:
        for ih in range(9):
            for iz in range(2):
                yield ("B", state, ih, iz)
    for tag in ("A", "Q"):
        for gi in range(9):
            for state in multiplier_states(tag, gi):
                for ih in range(3):
                    for iz in range(2):
                        yield ("m", tag, gi, state, ih, iz)
    yield ("epsilon",)


def vector_entries(tag, state, param, degrees=PARAM_DEGREE):
    for ih, iz, value in bernstein_vector(psig(param), *degrees):
        if tag == "E":
            yield ("E", ih, iz), value
        else:
            yield (tag, state, ih, iz), value


def column(meta, mathdata):
    kind = meta[0]
    if kind == "n":
        _, nu, ih, iz, sign = meta
        basis = bp(1, ih, 1, iz)
        for state, param in mathdata["gates"][nu].items():
            target = (state[0], state[1], state[2] + 1, state[3])
            for row, value in vector_entries(
                    "A", target, pscale(pmul(basis, param), 3 * sign)):
                yield row, value
        for row, value in vector_entries(
                "E", None, pscale(pmul(basis, mathdata["ends"][nu]), sign),
                END_DEGREE):
            yield row, value
        yield ("N", ih, iz), F(1)
    elif kind == "B":
        _, state, ih, iz = meta
        t, u, p, r = state
        basis = bp(8, ih, 1, iz)
        pieces = []
        if t:
            pieces.append(((t - 1, u, p + 1, r), 3*t))
        if u:
            pieces.append(((t, u - 1, p + 2, r), -3*u))
        if 3*p + r:
            pieces.append(((t, u, p, r + 1), -(3*p + r)))
        for target, scalar in pieces:
            yield from vector_entries("A", target, pscale(basis, scalar))
        if r:
            yield from vector_entries("Q", (t, u, p, r - 1),
                                      pscale(basis, -r))
        if t == 0:
            yield from vector_entries(
                "E", None, pmul(basis, mathdata["hp"][u]), END_DEGREE)
    elif kind == "m":
        _, tag, gi, state, ih, iz = meta
        basis = bp(2, ih, 1, iz)
        for gstate, param in mathdata["gen"][gi].items():
            yield from vector_entries(
                tag, state_add(state, gstate),
                pscale(pmul(basis, param), -1))
    elif kind == "epsilon":
        for ih in range(END_DEGREE[0] + 1):
            for iz in range(END_DEGREE[1] + 1):
                yield ("E", ih, iz), F(-1)
    else:
        raise ValueError("unknown new certificate column")


def validate_request(request, request_path, source_commit):
    if request.get("version") != VERSION:
        raise ValueError("request version mismatch")
    expected = request["fixed_ansatz"]
    exact = {
        "height_lo": ["3", "5"], "height_hi": ["67", "36"],
        "potential_count": 85, "n_parameter_degree": [1, 1],
        "B_parameter_degree": [8, 1],
        "multiplier_parameter_degree": [2, 1],
        "residual_parameter_degree": [8, 2],
        "endpoint_parameter_degree": [12, 1],
        "A_state_degree_limit": 6, "Q_state_degree_limit": 4,
        "rounding_power_of_two": 40,
        "single_LP_calls": 1, "single_exact_judges": 1,
        "generator_products": False,
    }
    if expected != exact:
        raise ValueError("request changes the frozen one-shot ansatz")
    if (not source_commit or len(source_commit) != 40 or
            any(c not in "0123456789abcdef" for c in source_commit)):
        raise ValueError("a concrete source commit is required")
    closure = []
    seen_paths = set()
    base = Path(request["repository_checkout"]).resolve()
    if not request["source_manifest"] or len(request["source_manifest"]) > 32:
        raise ValueError("empty or over-cap source manifest")
    if len(canonical_bytes(request["published_math"])) > 64 * 1024:
        raise ValueError("published source-reference metadata is over its cap")
    for spec in request["source_manifest"]:
        path = (base / spec["path"]).resolve()
        if base != path and base not in path.parents:
            raise ValueError("source manifest path escapes checkout")
        raw = path.read_bytes()
        seen_paths.add(path)
        item = {"path": spec["path"], "bytes": len(raw),
                "sha256": hashlib.sha256(raw).hexdigest()}
        closure.append(item)
        if item["bytes"] != int(spec["bytes"]) or item["sha256"] != spec["sha256"]:
            raise ValueError("bound source bytes/hash changed: " + spec["path"])
        P.check()
    if Path(__file__).resolve() not in seen_paths:
        raise ValueError("the executing entry is absent from its source manifest")
    if (base / request["design_path"]).resolve() not in seen_paths:
        raise ValueError("the frozen design is absent from its source manifest")
    bounds = {"variables": 100000, "coefficient_rows": 250000,
              "matrix_nonzeros_before_sum": 20000000,
              "exact_nonzero_coefficients": 250000}
    for key, upper in bounds.items():
        if not (0 < int(request["hard_caps"][key]) <= upper):
            raise ValueError("invalid hard cap: " + key)
    request_raw = request_path.read_bytes()
    P.data["request_identity"] = {
        "bytes": len(request_raw),
        "sha256": hashlib.sha256(request_raw).hexdigest(),
        "source_commit": source_commit, "sources": closure,
        "published_math": request["published_math"],
    }
    P.emit("request_identity", P.data["request_identity"])


def assemble(mathdata, request):
    P.enter("assemble_one_frozen_new_LP")
    rows = {}
    rhs = []
    rowkeys = []
    ri, ci, vv = array.array("i"), array.array("i"), array.array("d")
    metas = []
    bounds = []
    type_counts = {}
    caps = request["hard_caps"]

    def getrow(key):
        if key not in rows:
            idx = len(rows)
            if idx >= int(caps["coefficient_rows"]):
                raise StopCap("coefficient-row cap reached during new assembly")
            rows[key] = idx
            rowkeys.append(key)
            rhs.append(1.0 if key[0] == "N" else 0.0)
        return rows[key]

    for meta in variables(mathdata):
        P.counts["assembly_columns_started"] += 1
        idx = len(metas)
        if idx >= int(caps["variables"]):
            raise StopCap("variable cap reached during new assembly")
        metas.append(meta)
        kind = meta[0]
        type_counts[kind] = type_counts.get(kind, 0) + 1
        bounds.append((None, None) if kind == "B" else (0.0, None))
        for key, exact in column(meta, mathdata):
            row = getrow(key)
            # Residual coefficients and endpoint E-epsilon must be >=0.
            value = exact if key[0] == "N" else -exact
            f = float(value)
            if not math.isfinite(f):
                raise ValueError("nonfinite new LP coefficient")
            if len(vv) >= int(caps["matrix_nonzeros_before_sum"]):
                raise StopCap("matrix-entry cap reached during new assembly")
            ri.append(row)
            ci.append(idx)
            vv.append(f)
        P.counts["assembly_columns_finished"] += 1
        if idx % 256 == 0:
            P.data["assembly_progress"] = {
                "variables": len(metas), "rows": len(rows),
                "entries_before_sum": len(vv), "types": dict(type_counts),
            }
            P.check()

    P.data["assembly"] = {
        "variables": len(metas), "rows": len(rows),
        "entries_before_sum": len(vv), "types": type_counts,
        "exact_parameter_cache": str(bernstein_vector.cache_info()),
    }
    P.emit("assembly_complete", P.data["assembly"])
    P.check()
    return ri, ci, vv, rhs, metas, bounds, rowkeys


def emit_raw_candidate(values, metas):
    chunk = []
    nonzero = 0
    invalid = []
    for idx, (value, meta) in enumerate(zip(values, metas)):
        v = float(value)
        if not math.isfinite(v):
            invalid.append({"index": idx, "meta": meta, "float_hex": v.hex()})
        if v != 0.0 or not math.isfinite(v):
            nonzero += 1
            chunk.append({"index": idx, "meta": meta, "float_hex": v.hex()})
        if len(chunk) == 64:
            P.emit("raw_candidate_coefficients", {"entries": chunk})
            chunk = []
    if chunk:
        P.emit("raw_candidate_coefficients", {"entries": chunk})
    P.emit("raw_candidate_complete", {
        "dimension": len(values), "nonzero_entries": nonzero,
        "nonfinite_entries": invalid,
        "all_floats_recorded_as_exact_binary64_hex": True,
    })
    if invalid:
        raise ValueError("LP returned a nonfinite candidate")
    return nonzero


def solve_once(assembly, request):
    P.enter("import_pinned_new_LP_dependencies")
    import numpy as np
    import scipy
    from scipy import sparse
    from scipy.optimize import linprog

    expected = request["runtime"]
    thread_names = ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS",
                    "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS")
    thread_env = {name: os.environ.get(name) for name in thread_names}
    P.data["thread_environment"] = thread_env
    if any(value != "1" for value in thread_env.values()):
        raise ValueError("the frozen scientific environment must be single-threaded")
    actual = {"python": ".".join(str(x) for x in sys.version_info[:3]),
              "numpy": np.__version__, "scipy": scipy.__version__}
    P.data["runtime"] = actual
    P.emit("runtime", actual)
    if actual != expected:
        raise ValueError("pinned runtime version mismatch")
    P.check()

    ri, ci, vv, rhs, metas, bounds, rowkeys = assembly
    P.enter("compile_new_sparse_LP")
    rid = np.frombuffer(ri, dtype=np.int32)
    cid = np.frombuffer(ci, dtype=np.int32)
    vals = np.frombuffer(vv, dtype=np.float64)
    row_max = np.zeros(len(rhs), dtype=np.float64)
    np.maximum.at(row_max, rid, np.abs(vals))
    row_scale = 1.0 / np.maximum(1.0, row_max)
    # A strictly positive row rescaling changes neither the LP nor the exact judge.
    matrix = sparse.coo_matrix(
        (vals * row_scale[rid], (rid, cid)),
        shape=(len(rhs), len(metas))).tocsr()
    matrix.sum_duplicates()
    objective = np.zeros(len(metas), dtype=np.float64)
    if metas[-1] != ("epsilon",):
        raise ValueError("the single epsilon column is not last")
    objective[-1] = -1.0
    b_ub = np.asarray(rhs, dtype=np.float64) * row_scale
    P.data["compiled_matrix_nonzeros"] = int(matrix.nnz)
    P.emit("compiled_new_LP", {
        "shape": list(matrix.shape), "csr_nonzeros": int(matrix.nnz),
        "minimization_objective": "-epsilon",
        "normalization": "one l1 bound at each of the four n-parameter corners",
        "solver_status_is_not_a_mathematical_certificate": True,
        "strictly_positive_row_scale_min": float(np.min(row_scale)),
        "strictly_positive_row_scale_max": float(np.max(row_scale)),
        "exact_judge_uses_unscaled_original_coefficients": True,
    })
    P.check()

    P.enter("single_new_HiGHS_call")
    left = P.remaining()
    keep = float(request["budget"]["minimum_seconds_reserved_after_LP"])
    limit = min(float(request["budget"]["solver_seconds"]), left - keep)
    if limit <= 0:
        raise StopBudget("no declared LP time remains after the reserved judge window")
    P.counts["new_lp_started"] += 1
    t0 = time.perf_counter()
    result = linprog(
        objective, A_ub=matrix, b_ub=b_ub, bounds=bounds, method="highs",
        options={
            "time_limit": limit, "presolve": True,
            "primal_feasibility_tolerance": 1e-8,
            "dual_feasibility_tolerance": 1e-8,
        },
    )
    elapsed = time.perf_counter() - t0
    P.counts["new_lp_returned"] += 1
    x = getattr(result, "x", None)
    info = {
        "status": int(result.status), "success": bool(result.success),
        "message": str(result.message),
        "fun": None if result.fun is None or not finite_float(result.fun)
        else float(result.fun),
        "fun_binary64_hex": None if result.fun is None else float(result.fun).hex(),
        "nit": None if getattr(result, "nit", None) is None else int(result.nit),
        "crossover_nit": None if getattr(result, "crossover_nit", None) is None
        else int(result.crossover_nit),
        "requested_time_limit": limit, "actual_call_seconds": elapsed,
        "candidate_present": x is not None,
        "candidate_dimension": None if x is None else len(x),
        "deadline_after_return": P.limit is not None and P.elapsed() >= P.limit,
    }
    P.data["LP_return"] = info
    # Preserve the actual returned candidate before deciding whether more science fits.
    P.emit("LP_return", info)
    if x is not None:
        if len(x) != len(metas):
            raise ValueError("LP candidate dimension mismatch")
        emit_raw_candidate(x, metas)
    P.check()
    if x is None:
        return None
    return x


def rounded_units(value, nonnegative):
    # Exact binary64 -> fixed rational grid; no tolerance is treated as a proof.
    units = int(round(F.from_float(float(value)) * ROUND_DENOMINATOR))
    return max(0, units) if nonnegative else units


def bound_A(state):
    a, j, k, l = state
    weight = k + 2*l - a
    if min(state) < 0 or weight < 4:
        raise ValueError("an A residual has no declared uniform tail bound")
    if k:
        return (F(2**j) +
                F(2**(j + k - 1 + 2*l), weight - 2)) / 3
    return F(2**(j + a + 1), 2*l - a - 2)


def bound_Q(state):
    a, j, k, l = state
    if min(state) < 0 or k + 2*l - a < 0:
        raise ValueError("a Q residual has no declared uniform q-weight bound")
    return F(2**(j + a))


def exact_judge(candidate, metas, mathdata, request):
    P.enter("one_fixed_rationalization_and_exact_integral_defect_judge")
    P.counts["exact_judges_started"] += 1
    exact_rows = {}
    rounded_nonzero = 0
    coefficient_chunk = []
    n_net = {}
    changed_negative_nonnegative_variables = 0
    caps = request["hard_caps"]
    for idx, (value, meta) in enumerate(zip(candidate, metas)):
        P.counts["exact_columns_started"] += 1
        kind = meta[0]
        if kind == "epsilon":
            units = 0  # Reconstruct E, not the solver's E-epsilon row.
        else:
            is_nonnegative = kind in ("n", "m")
            if is_nonnegative and float(value) < 0:
                changed_negative_nonnegative_variables += 1
            units = rounded_units(value, is_nonnegative)
        if units:
            rounded_nonzero += 1
            exact_value = F(units, ROUND_DENOMINATOR)
            if kind == "n":
                _, nu, ih, iz, sign = meta
                nkey = (nu, ih, iz)
                n_net[nkey] = n_net.get(nkey, F(0)) + sign * exact_value
            coefficient_chunk.append({
                "index": idx, "meta": meta, "numerator_units": str(units),
                "common_denominator": str(ROUND_DENOMINATOR),
            })
            for key, coeff in column(meta, mathdata):
                if key[0] == "N":
                    continue
                exact_rows[key] = exact_rows.get(key, F(0)) + exact_value * coeff
                if not exact_rows[key]:
                    del exact_rows[key]
            if len(exact_rows) > int(caps["exact_nonzero_coefficients"]):
                raise StopCap("exact new certificate coefficient cap exceeded")
        if len(coefficient_chunk) >= 64:
            P.emit("rational_candidate_coefficients", {"entries": coefficient_chunk})
            coefficient_chunk = []
        P.counts["exact_columns_finished"] += 1
        if idx % 128 == 0:
            P.data["exact_progress"] = {
                "columns_finished": P.counts["exact_columns_finished"],
                "rounded_nonzero_variables": rounded_nonzero,
                "nonzero_exact_coefficients": len(exact_rows),
            }
            P.check()
    if coefficient_chunk:
        P.emit("rational_candidate_coefficients", {"entries": coefficient_chunk})
    norm_nonzero = any(n_net.values())
    P.emit("complete_net_gate_multipliers", {
        "parameter_degree": [1, 1],
        "entries": [{"gate": nu, "xi_index": ih, "zeta_index": iz,
                     "coefficient": rational(n_net.get((nu, ih, iz), F(0)))}
                    for nu in GATE_IDS for ih in range(2) for iz in range(2)],
    })
    P.emit("rational_candidate_complete", {
        "rounding_power_of_two": ROUND_POWER,
        "rounded_nonzero_variables": rounded_nonzero,
        "negative_solver_values_on_nonnegative_variables_replaced_by_zero":
            changed_negative_nonnegative_variables,
        "replacement_is_a_new_rational_candidate_not_a_solver_feasibility_claim": True,
        "nonzero_exact_coefficients": len(exact_rows),
    })
    P.check()

    groups = {"A": {}, "Q": {}}
    endpoint = {}
    for key, value in exact_rows.items():
        if key[0] in groups:
            tag, state, ih, iz = key
            groups[tag].setdefault(state, {})[(ih, iz)] = value
        elif key[0] == "E":
            endpoint[(key[1], key[2])] = value
        else:
            raise ValueError("unexpected exact-row family")

    losses = {}
    group_records = {}
    for tag in ("A", "Q"):
        loss = F(0)
        negative_terms = 0
        for state in sorted(groups[tag]):
            vals = groups[tag][state]
            full = [vals.get((ih, iz), F(0))
                    for ih in range(9) for iz in range(3)]
            minimum = min(full)
            bound = bound_A(state) if tag == "A" else bound_Q(state)
            majorant = max(F(0), -minimum)
            term = majorant * bound
            loss += term
            negative_terms += int(majorant > 0)
            P.emit("complete_exact_residual", {
                "family": tag, "state_exponents_T_U_p_r": list(state),
                "parameter_degree_xi_zeta": [8, 2],
                "coefficient_order": "xi-major, zeta-minor; all 27 entries",
                "bernstein_coefficients": [rational(v) for v in full],
                "minimum": rational(minimum),
                "negative_majorant": rational(majorant),
                "original_integral_bound": rational(bound),
                "complete_loss_contribution": rational(term),
                "tail_weight": state[2] + 2*state[3] - state[0],
            })
            P.check()
        losses[tag] = loss
        group_records[tag] = {
            "complete_state_rows": len(groups[tag]),
            "negative_state_rows": negative_terms,
            "total_loss": rational(loss),
        }
        P.emit("exact_residual_family_complete", {
            "family": tag, **group_records[tag],
        })

    end_values = [endpoint.get((ih, iz), F(0))
                  for ih in range(13) for iz in range(2)]
    end_min = min(end_values)
    total_loss = losses["A"] + losses["Q"]
    margin = end_min - total_loss
    P.emit("complete_exact_endpoint", {
        "parameter_degree_xi_zeta": [12, 1],
        "coefficient_order": "xi-major, zeta-minor; all 26 entries",
        "bernstein_coefficients": [rational(v) for v in end_values],
        "exact_minimum": rational(end_min),
        "left_endpoint_potential": "exactly zero also when C>0",
    })
    result = {
        "exact_endpoint_minimum": rational(end_min),
        "exact_A_loss": rational(losses["A"]),
        "exact_Q_loss": rational(losses["Q"]),
        "exact_total_loss": rational(total_loss),
        "exact_margin": rational(margin),
        "strict_comparison": margin > 0,
        "net_gate_multiplier_is_not_identically_zero": norm_nonzero,
        "complete_cap5_common_zero_excluded_on_height_interval":
            bool(margin > 0 and norm_nonzero),
        "height_interval": [rational(H_LO), rational(H_HI)],
        "C_domain": "0 <= C <= H-3/5, including all true tail terms",
        "five_original_gates": [1, 2, 3, 4, 6],
        "group_records": group_records,
        "a_failed_finite_ansatz_is_not_a_global_nonexistence_or_existence_result": True,
    }
    P.counts["exact_judges_finished"] += 1
    P.data["exact_judge"] = result
    P.emit("EXACT_JUDGE", result)
    P.check()
    return result


def science(request, request_path, source_commit):
    P.configure(request)
    P.enter("validate_only_new_source_and_request")
    validate_request(request, request_path, source_commit)
    P.enter("construct_complete_original_five_gate_coefficients")
    mathdata = make_math()
    P.data["mathematical_identity_sha256"] = mathdata["identity_sha256"]
    P.emit("complete_mathematical_input", {
        "identity": mathdata["identity"],
        "sha256": mathdata["identity_sha256"],
        "full_C_tail_and_Af_remainder_preserved": True,
        "no_old_atom_or_profile_inputs_read": True,
    })
    P.check()
    assembly = assemble(mathdata, request)
    candidate = solve_once(assembly, request)
    if candidate is None:
        P.data["outcome"] = "finite_LP_returned_no_candidate_no_mathematical_decision"
        return
    result = exact_judge(candidate, assembly[4], mathdata, request)
    P.data["outcome"] = (
        "strict_rational_integral_certificate"
        if result["complete_cap5_common_zero_excluded_on_height_interval"]
        else "fixed_finite_certificate_ansatz_unresolved"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    code = 0
    try:
        path = Path(args.request)
        raw = path.read_bytes()
        request = json.loads(raw.decode("utf-8-sig"))
        science(request, path, args.source_commit)
    except BaseException as exc:
        code = 1
        P.failure = {
            "type": type(exc).__name__, "message": str(exc),
            "stage": P.stage, "entry_elapsed_at_failure": P.elapsed(),
            "traceback": traceback.format_exc(),
        }
        if P.data.get("exact_judge", {}).get(
                "complete_cap5_common_zero_excluded_on_height_interval", False):
            P.data["outcome"] = "completed_exact_certificate_with_later_account_or_output_failure"
        else:
            P.data.setdefault("outcome", "finite_failure_no_mathematical_decision")
    finally:
        report = P.snapshot()
        report["exit_code_before_final_output"] = code
        try:
            raw = canonical_bytes(report) + b"\n"
            try:
                output_path = Path(args.out)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_bytes(raw)
            except BaseException as exc:
                code = 1
                report["final_file_write_failure"] = {
                    "type": type(exc).__name__, "message": str(exc),
                }
                # An output-file error must not suppress the complete public report.
                raw = canonical_bytes(report) + b"\n"
            report_line = b"CAP5_CERT_FINAL_REPORT " + raw
            if len(report_line) + 16384 > P.output_limit - P.output_bytes:
                # This cannot be repaired by dropping the already paid work.
                # Keep all charges, phase outcomes, and the full report fingerprint.
                fallback = {
                    "version": VERSION, "final_report_over_output_cap": True,
                    "complete_report_bytes": len(raw),
                    "complete_report_sha256": hashlib.sha256(raw).hexdigest(),
                    "stage": P.stage, "counts": P.counts,
                    "stage_times": report["stage_times"],
                    "entry_elapsed_before_final_output": P.elapsed(),
                    "single_account_limit": P.limit,
                    "peak_rss_kib": rss_kib(),
                    "records": P.seq, "record_chain": P.chain,
                    "record_bytes": P.output_bytes, "failure": P.failure,
                    "outcome": P.data.get("outcome"),
                    "LP_return": P.data.get("LP_return"),
                    "exact_judge": P.data.get("exact_judge"),
                    "source_identity_sha256": hashlib.sha256(
                        canonical_bytes(P.data.get("request_identity", {}))).hexdigest(),
                    "mathematical_identity_sha256":
                        P.data.get("mathematical_identity_sha256"),
                    "exit_code_before_final_output": code,
                    "final_clock_supersedes_this_pre_output_elapsed": True,
                }
                report_line = (b"CAP5_CERT_FINAL_REPORT " +
                               canonical_bytes(fallback) + b"\n")
                code = 1
            sys.stdout.buffer.write(report_line)
            sys.stdout.buffer.flush()
        except BaseException as exc:
            code = 1
            sys.stdout.write("CAP5_CERT_FINAL_OUTPUT_FAILURE " +
                             json.dumps({"type": type(exc).__name__,
                                         "message": str(exc),
                                         "stage": P.stage,
                                         "records_already_emitted": P.seq},
                                        sort_keys=True) + "\n")
            sys.stdout.flush()
        # This clock is deliberately after complete report serialization/write/output.
        elapsed = P.elapsed()
        final = {
            "version": VERSION,
            "entry_elapsed_including_inputs_failure_and_all_previous_output": elapsed,
            "single_account_limit": P.limit,
            "overrun_after_nonpreemptible_output":
                P.limit is not None and elapsed > P.limit,
            "scientific_work_after_this_record": False,
            "supersedes_pre_output_elapsed_in_main_report": True,
            "counts": P.counts, "peak_rss_kib": rss_kib(),
            "last_scientific_stage": P.stage,
            "records": P.seq, "record_chain": P.chain,
            "record_bytes": P.output_bytes, "exit_code": code,
        }
        sys.stdout.write("CAP5_CERT_FINAL_CLOCK " +
                         json.dumps(final, sort_keys=True,
                                    separators=(",", ":"), allow_nan=False) + "\n")
        sys.stdout.flush()
    return code


if __name__ == "__main__":
    raise SystemExit(main())
