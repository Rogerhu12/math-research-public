#!/usr/bin/env python3
"""R769: exact bounded enumeration in the retained R759 degree lattice.

Only the original public R759 LLL Gram and map vectors are read.
No periods, HNF, LLL, topology, or old field computations are repeated.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import signal
import sys
import time

RESULT = "R769-retained-degree-lattice-bounded-search"
FINAL = "p41-retained-degree-lattice-bounded-search-certificate.json"
CHECKPOINT = "R769-exact-enumeration-checkpoint.json.gz"
LDL_FILE = "R769-retained-Gram-and-exact-LDL.json"
WITNESS_FILE = "R769-original-short-map-witness.json.gz"
AUDIT_FILE = "R769-enumeration-audit-manifest.json.gz"
DIM = 12
FILES = {
    "p41-original-integral-period-lattice-and-degree-certificate.json":
        "7c2c611b9a5f43bc3a2a0007bf2cb5dd2fa8d10f133b663dbca0d054e1515de0",
    "R759-exact-degree-LLL.json.gz":
        "5a1b6d44694389ac3fe48686a00c1745976726fefd8ff5196e2f60d4ef063825",
    "R759-original-integral-maps-and-bounded-recovery-input.json.gz":
        "037b56d016d502408173319d76a3067a65dd50250c31bc2225c0fca598396ecc",
}
R759_SOURCE = "17403f45f74e03e5a138376068e64e54c9bf6b2622a7b91bb178747d407708e0"
STOP = False


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Actual arithmetic runs only in the public repository Actions.")


def canonical(obj):
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"))+"\n").encode()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    if str(path).endswith(".gz"):
        data = gzip.decompress(data)
    return json.loads(data)


def save(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = canonical(obj)
    if path.suffix == ".gz":
        data = gzip.compress(data, mtime=0)
    tmp = path.with_name(path.name+".tmp")
    tmp.write_bytes(data)
    tmp.replace(path)


def enc(q):
    q = F(q)
    return [str(q.numerator), str(q.denominator)]


def dec(pair):
    return F(int(pair[0]), int(pair[1]))


def qmatrix(rows):
    return [[dec(x) for x in row] for row in rows]


def zmatrix(rows):
    return [[int(x) for x in row] for row in rows]


def exact_ldl(G):
    """G = mu diag(norms) mu^t, mu lower unit triangular."""
    mu = [[F(int(i == j)) for j in range(DIM)] for i in range(DIM)]
    norms = [F(0)]*DIM
    for i in range(DIM):
        for j in range(i):
            mu[i][j] = (G[i][j]-sum(
                (mu[i][k]*mu[j][k]*norms[k] for k in range(j)), F(0)))/norms[j]
        norms[i] = G[i][i]-sum(
            (mu[i][k]*mu[i][k]*norms[k] for k in range(i)), F(0))
        assert norms[i] > 0
    for i in range(DIM):
        for j in range(DIM):
            assert sum((mu[i][k]*norms[k]*mu[j][k]
                        for k in range(min(i, j)+1)), F(0)) == G[i][j]
    return mu, norms


def quadratic(G, v):
    return sum(v[i]*G[i][j]*v[j] for i in range(DIM) for j in range(DIM))


def exact_interval(center, radius_squared):
    """All integers x with (x-center)^2 <= radius_squared, without floats."""
    assert radius_squared >= 0
    a, b = center.numerator, center.denominator
    r, s = radius_squared.numerator, radius_squared.denominator
    K = math.isqrt((b*b*r)//s)
    lower = -((-(a-K))//b)
    upper = (a+K)//b
    return lower, upper


def nearest(q):
    return (2*q.numerator+q.denominator)//(2*q.denominator)


def encode_frame(frame):
    return {k: enc(v) if k in ("center", "partial") else v for k, v in frame.items()}


def decode_frame(frame):
    return {k: dec(v) if k in ("center", "partial") else v for k, v in frame.items()}


def next_integer(frame):
    # Enumerate nearest(center), +1, -1, +2, -2, ...; outside values are skipped.
    while frame["cursor"] <= frame["last_cursor"]:
        k = frame["cursor"]
        frame["cursor"] += 1
        offset = 0 if k == 0 else ((k+1)//2 if k % 2 else -(k//2))
        value = frame["nearest"]+offset
        if frame["lo"] <= value <= frame["hi"]:
            return value
    return None


def decode_poly(value):
    denominator = int(value["denominator"])
    assert denominator > 0
    values = [F(int(x), denominator) for x in value["numerator"]]
    assert len(values) <= 7
    return values+[F(0)]*(7-len(values))


def encode_poly(values):
    denominator = 1
    for x in values:
        denominator = math.lcm(denominator, x.denominator)
    numerators = [int(x*denominator) for x in values]
    while numerators and numerators[-1] == 0:
        numerators.pop()
    return {"numerator": [str(x) for x in numerators], "denominator": str(denominator)}


def request_stop(signum, frame):
    global STOP
    STOP = True


class Search:
    def __init__(self, args):
        self.args = args
        self.out = args.output
        self.out.mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        for name, digest in FILES.items():
            assert sha(args.inputs/name) == digest, "Retained source hash mismatch: "+name
        cert = read(args.inputs/"p41-original-integral-period-lattice-and-degree-certificate.json")
        self.lll = read(args.inputs/"R759-exact-degree-LLL.json.gz")
        self.maps = read(args.inputs/"R759-original-integral-maps-and-bounded-recovery-input.json.gz")
        assert cert["complete"] and cert["p"] == 41
        assert cert["full_integral_period_lattice_Z_rank"] == DIM
        assert cert["all_1600_rational_period_rows_used"] and cert["HNF_unimodular_steps_verified"]
        assert cert["exact_LLL_inequalities_verified"] and cert["positive_definite_degree_form_verified"]
        configuration = cert["configuration"]
        assert configuration["source_sha256"] == R759_SOURCE
        for obj in (self.lll, self.maps):
            assert obj["complete"] and obj["configuration"] == configuration
        assert self.lll["all_LLL_inequalities_exact"]
        assert self.maps["Z_basis_rank"] == DIM and self.maps["O_K_rank"] == 6
        assert self.maps["target"] == "original R735 C/L: y^2=x^3+b; omega_C=dx/(2y)"
        assert self.maps["c1_coset"] == 4424
        self.G = zmatrix(self.lll["twice_degree_Gram_matrix"])
        assert self.G == zmatrix(self.maps["twice_degree_Gram_matrix"])
        assert len(self.G) == DIM and all(len(row) == DIM for row in self.G)
        assert all(self.G[i][j] == self.G[j][i] for i in range(DIM) for j in range(DIM))
        assert all(self.G[i][i] % 2 == 0 for i in range(DIM))
        assert [str(self.G[i][i]//2) for i in range(DIM)] == cert["degrees_of_LLL_Z_basis"]
        self.mu, self.norms = exact_ldl(self.G)
        self.bound = 2*args.degree_bound
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__), "p": 41, "dimension": DIM,
            "degree_bound": args.degree_bound, "quadratic_bound": self.bound,
            "R759_source_sha256": R759_SOURCE, "retained_files": FILES,
            "basis": "the ordered twelve retained R759 LLL map vectors",
            "algorithm": "exact-LDL-Fincke-Pohst-center-out-v1",
            "enumerates_all_integer_vectors_no_sign_or_zeta_quotient": True,
            "degree_formula": "w^t G w / 2; G is the retained twice-degree Gram",
        }
        self.initial_digest = hashlib.sha256(canonical(self.tag)).hexdigest()
        self.digest = self.initial_digest
        self.block_start = self.digest
        self.blocks = []
        self.events = []
        self.v = [0]*DIM
        self.stack = []
        self.counts = {
            "frames_entered": [0]*DIM, "frames_finished": [0]*DIM,
            "integer_candidates": [0]*DIM, "empty_intervals": [0]*DIM,
            "leaves": 0, "zero_leaves": 0, "events": 0,
        }
        self.prior_seconds = 0.0
        self.status = "searching"
        self.winner = None
        ldl = {"configuration": self.tag, "complete": True,
               "twice_degree_Gram_matrix": [[str(x) for x in row] for row in self.G],
               "lower_unit_triangular_mu": [[enc(x) for x in row] for row in self.mu],
               "positive_diagonal": [enc(x) for x in self.norms],
               "G_equals_mu_diag_mu_transpose_verified": True,
               "old_period_HNF_or_LLL_computed": False}
        path = self.out/LDL_FILE
        if path.exists():
            assert read(path) == ldl
        else:
            save(path, ldl)

    def event(self, value):
        self.digest = hashlib.sha256(bytes.fromhex(self.digest)+canonical(value)).hexdigest()
        self.events.append(value)
        self.counts["events"] += 1
        if len(self.events) >= 4096:
            self.flush_events()

    def flush_events(self):
        if not self.events:
            return
        name = "R769-enumeration-audit-%06d.json.gz" % len(self.blocks)
        value = {"configuration": self.tag, "block_index": len(self.blocks),
                 "initial_hash": self.block_start, "final_hash": self.digest,
                 "events": self.events}
        target = self.out/name
        if target.exists():
            assert read(target) == value, "A retained audit block would be overwritten"
        else:
            save(target, value)
        self.blocks.append({"file": name, "sha256": sha(target), "events": len(self.events),
                            "initial_hash": self.block_start, "final_hash": self.digest})
        self.events = []
        self.block_start = self.digest

    def frame(self, i, partial):
        assert 0 <= i < DIM and F(0) <= partial <= self.bound
        center = -sum((self.mu[j][i]*self.v[j] for j in range(i+1, DIM)), F(0))
        lo, hi = exact_interval(center, (self.bound-partial)/self.norms[i])
        q = nearest(center)
        last = 2*max(abs(lo-q), abs(hi-q)) if lo <= hi else -1
        fr = {"i": i, "partial": partial, "center": center, "lo": lo, "hi": hi,
              "nearest": q, "cursor": 0, "last_cursor": last, "accepted": 0}
        self.counts["frames_entered"][i] += 1
        self.event(["enter", i, self.v[i+1:], enc(partial), enc(center), lo, hi])
        return fr

    def save_state(self):
        self.flush_events()
        value = {"configuration": self.tag, "complete": self.status != "searching",
                 "status": self.status, "current_vector": [str(x) for x in self.v],
                 "stack": [encode_frame(x) for x in self.stack], "counts": self.counts,
                 "audit_blocks": self.blocks, "audit_chain_initial": self.initial_digest,
                 "audit_chain_final": self.digest, "winner": self.winner,
                 "elapsed_seconds_total": self.prior_seconds+time.monotonic()-self.started,
                 "no_old_period_lattice_or_LLL_recomputation": True}
        save(self.out/CHECKPOINT, value)
        save(self.out/AUDIT_FILE, {"configuration": self.tag,
             "complete": self.status != "searching", "blocks": self.blocks,
             "initial_hash": self.initial_digest, "final_hash": self.digest,
             "total_events": self.counts["events"]})

    def restore(self):
        path = self.out/CHECKPOINT
        if not path.exists():
            self.stack = [self.frame(DIM-1, F(0))]
            self.save_state()
            return
        prior = read(path)
        assert prior["configuration"] == self.tag
        assert prior["audit_chain_initial"] == self.initial_digest
        self.status = prior["status"]
        assert self.status in ("searching", "found", "exhausted")
        self.v = [int(x) for x in prior["current_vector"]]
        assert len(self.v) == DIM
        self.stack = [decode_frame(x) for x in prior["stack"]]
        self.counts = prior["counts"]
        self.blocks = prior["audit_blocks"]
        self.digest = prior["audit_chain_final"]
        self.block_start = self.digest
        self.winner = prior["winner"]
        self.prior_seconds = prior["elapsed_seconds_total"]
        previous, events = self.initial_digest, 0
        # Read/hash completed audit blocks, but do not enumerate their branches again.
        for index, row in enumerate(self.blocks):
            assert row["file"] == "R769-enumeration-audit-%06d.json.gz" % index
            assert sha(self.out/row["file"]) == row["sha256"]
            block = read(self.out/row["file"])
            assert block["configuration"] == self.tag and block["block_index"] == index
            assert block["initial_hash"] == previous == row["initial_hash"]
            assert len(block["events"]) == row["events"]
            for value in block["events"]:
                previous = hashlib.sha256(bytes.fromhex(previous)+canonical(value)).hexdigest()
            assert previous == block["final_hash"] == row["final_hash"]
            events += row["events"]
        assert previous == self.digest and events == self.counts["events"]
        if self.status == "searching":
            assert self.stack and len(self.stack) <= DIM
            assert [x["i"] for x in self.stack] == list(range(DIM-1, DIM-1-len(self.stack), -1))
        else:
            assert self.status != "exhausted" or not self.stack
        for fr in self.stack:
            i = fr["i"]
            center = -sum((self.mu[j][i]*self.v[j] for j in range(i+1, DIM)), F(0))
            partial = sum((self.norms[k]*(self.v[k]+sum(
                (self.mu[j][k]*self.v[j] for j in range(k+1, DIM)), F(0)))**2
                for k in range(i+1, DIM)), F(0))
            assert center == fr["center"] and partial == fr["partial"]
            assert exact_interval(center, (self.bound-partial)/self.norms[i]) == (fr["lo"], fr["hi"])
            assert fr["nearest"] == nearest(center)
            assert 0 <= fr["cursor"] <= fr["last_cursor"]+1
        print(json.dumps({"stage": "resume", "status": self.status,
                          "retained_events": events, "completed_branches_repeated": False}), flush=True)

    def witness(self, raw):
        divisor = math.gcd(*raw)
        assert divisor > 0
        v = [x//divisor for x in raw]
        if next(x for x in reversed(v) if x) < 0:
            v = [-x for x in v]
        q = quadratic(self.G, v)
        assert q > 0 and q % 2 == 0 and q <= self.bound
        assert math.gcd(*v) == 1
        U = zmatrix(self.lll["unimodular_rows"])
        saturated = [sum(U[j][i]*v[j] for j in range(DIM)) for i in range(DIM)]
        basis = qmatrix(self.maps["coefficient_basis_columns_in_original_h_zeta_h_directions"])
        old_directions = [sum((basis[i][j]*v[j] for j in range(DIM)), F(0))
                          for i in range(DIM)]
        maps = self.maps["all_twelve_integral_map_differential_vectors_in_original_omega_basis"]
        assert len(maps) == DIM and all(len(row) == 6 for row in maps)
        differential = []
        for j in range(6):
            components = []
            for k in range(2):
                coefficients = [F(0)]*7
                for i in range(DIM):
                    polynomial = decode_poly(maps[i][j][k])
                    for ell in range(7):
                        coefficients[ell] += v[i]*polynomial[ell]
                components.append(encode_poly(coefficients))
            differential.append(components)
        assert any(part["numerator"] for row in differential for part in row)
        value = {"configuration": self.tag, "complete": True,
                 "integer_vector_in_retained_LLL_basis": [str(x) for x in v],
                 "integer_vector_in_original_saturated_basis": [str(x) for x in saturated],
                 "original_h_zeta_h_coefficients": [enc(x) for x in old_directions],
                 "differential_vector_in_original_omega_basis": differential,
                 "polynomial_basis": "1,b,...,b^6; pair A(b)+zeta*B(b), same R759 field",
                 "degree": str(q//2), "twice_degree": str(q),
                 "primitive_Z_vector": True,
                 "raw_enumerated_vector": [str(x) for x in raw],
                 "raw_vector_gcd": str(divisor), "raw_degree": str(quadratic(self.G, raw)//2),
                 "target": self.maps["target"], "base_point": self.maps["base_point"],
                 "c1_coset": 4424,
                 "degree_checked_directly_in_retained_Gram": True,
                 "integral_periods_by_retained_full_lattice_membership": True,
                 "global_minimum_degree_claimed": False,
                 "new_rational_functions_beta_or_height_computed": False}
        save(self.out/WITNESS_FILE, value)
        return {"file": WITNESS_FILE, "sha256": sha(self.out/WITNESS_FILE),
                "degree": str(q//2), "integer_vector": [str(x) for x in v]}

    def run(self):
        self.restore()
        if self.status != "searching":
            return
        last_checkpoint = time.monotonic()
        while self.stack:
            if STOP or time.monotonic()-self.started >= self.args.max_seconds:
                self.save_state()
                return
            fr = self.stack[-1]
            i = fr["i"]
            value = next_integer(fr)
            if value is None:
                assert fr["accepted"] == max(0, fr["hi"]-fr["lo"]+1)
                self.counts["frames_finished"][i] += 1
                self.event(["finish", i, fr["accepted"]])
                self.stack.pop()
                self.v[i] = 0
                continue
            fr["accepted"] += 1
            self.v[i] = value
            partial = fr["partial"]+self.norms[i]*(value-fr["center"])**2
            assert partial <= self.bound
            self.counts["integer_candidates"][i] += 1
            self.event(["try", i, value, enc(partial)])
            if i == 0:
                self.counts["leaves"] += 1
                direct = quadratic(self.G, self.v)
                assert partial == direct and direct >= 0 and direct % 2 == 0
                self.event(["leaf", [str(x) for x in self.v], str(direct)])
                if any(self.v):
                    self.winner = self.witness(self.v[:])
                    self.status = "found"
                    self.save_state()
                    return
                assert direct == 0
                self.counts["zero_leaves"] += 1
            else:
                child = self.frame(i-1, partial)
                if child["lo"] > child["hi"]:
                    self.counts["empty_intervals"][i-1] += 1
                    self.counts["frames_finished"][i-1] += 1
                    self.event(["finish", i-1, 0])
                else:
                    self.stack.append(child)
            if time.monotonic()-last_checkpoint >= 5:
                self.save_state()
                last_checkpoint = time.monotonic()
                print(json.dumps({"stage": "search", "events": self.counts["events"],
                                  "active_depth": len(self.stack),
                                  "seconds": time.monotonic()-self.started}), flush=True)
        self.status = "exhausted"
        assert self.counts["zero_leaves"] == 1 and self.counts["leaves"] == 1
        assert self.counts["frames_entered"] == self.counts["frames_finished"]
        self.save_state()

    def finalize(self):
        complete = self.status in ("found", "exhausted")
        assert self.status != "found" or self.winner is not None
        assert self.status != "exhausted" or not self.stack
        cert = {"result": RESULT, "configuration": self.tag, "complete": complete,
                "status": self.status, "p": 41, "source_lattice_rank": DIM,
                "degree_bound": self.args.degree_bound,
                "found": self.status == "found", "exhausted": self.status == "exhausted",
                "no_nonzero_map_of_degree_at_most_bound": self.status == "exhausted",
                "global_minimum_degree_claimed": False,
                "full_integer_lattice_enumerated_when_exhausted": self.status == "exhausted",
                "active_stack_frames": len(self.stack), "counts": self.counts,
                "LDL_file": LDL_FILE, "LDL_sha256": sha(self.out/LDL_FILE),
                "checkpoint_file": CHECKPOINT, "checkpoint_sha256": sha(self.out/CHECKPOINT),
                "audit_manifest_file": AUDIT_FILE, "audit_manifest_sha256": sha(self.out/AUDIT_FILE),
                "audit_blocks": len(self.blocks), "audit_chain_final": self.digest,
                "witness": self.winner,
                "no_old_period_HNF_LLL_or_field_computation_repeated": True,
                "actual_rational_functions_beta_or_height_computed": False,
                "seconds_this_attempt": time.monotonic()-self.started,
                "seconds_total": self.prior_seconds+time.monotonic()-self.started}
        save(self.out/FINAL, cert)
        save(self.out/"core-receipt.json", {
            "result": RESULT, "complete": complete, "status": self.status,
            "source_sha256": sha(__file__), "certificate_sha256": sha(self.out/FINAL),
            "found": cert["found"], "exhausted": cert["exhausted"],
            "no_nonzero_map_claimed": cert["no_nonzero_map_of_degree_at_most_bound"]})
        print(json.dumps({"result": RESULT, "complete": complete, "status": self.status,
                          "degree": None if self.winner is None else self.winner["degree"]}), flush=True)
        return 0 if complete else 124


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--degree-bound", type=int, default=693)
    parser.add_argument("--max-seconds", type=int, default=720)
    args = parser.parse_args()
    assert args.degree_bound == 693 and 1 <= args.max_seconds <= 840
    signal.signal(signal.SIGTERM, request_stop)
    signal.signal(signal.SIGINT, request_stop)
    job = None
    try:
        job = Search(args)
        final = args.output/FINAL
        if final.exists():
            prior = read(final)
            assert prior["configuration"] == job.tag
            if prior["complete"]:
                assert prior["status"] in ("found", "exhausted")
                for key in ("LDL", "checkpoint", "audit_manifest"):
                    assert sha(args.output/prior[key+"_file"]) == prior[key+"_sha256"]
                if prior["found"]:
                    assert sha(args.output/prior["witness"]["file"]) == prior["witness"]["sha256"]
                save(args.output/"core-receipt.json", {
                    "result": RESULT, "complete": True, "status": prior["status"],
                    "source_sha256": sha(__file__), "certificate_sha256": sha(final),
                    "found": prior["found"], "exhausted": prior["exhausted"],
                    "no_nonzero_map_claimed": prior["no_nonzero_map_of_degree_at_most_bound"],
                    "reused_complete": True})
                return 0
        job.run()
        return job.finalize()
    except BaseException as error:
        if job is not None and job.stack:
            job.save_state()
        args.output.mkdir(parents=True, exist_ok=True)
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": False, "source_sha256": sha(__file__),
            "error": type(error).__name__+": "+str(error), "no_nonzero_map_claimed": False,
            "completed_audit_blocks_preserved": True})
        raise


if __name__ == "__main__":
    sys.exit(main())
