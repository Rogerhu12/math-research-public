#!/usr/bin/env python3
"""Independent R314 strict fixed-trace field certificate; public Actions only.

All arithmetic here is new scientific arithmetic. It is never a byte-only
reader or a gate on the producing native run. Integer outward intervals
enclose the accurate real extension of a recorded successful finite trace.
No derivative of IEEE rounding, dynamic branch stability, or F-root theorem
is inferred. All raw inputs and large certificates are temporary job data.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time
import traceback

SCHEMA = "literal-root-fixed-trace-field-interval-certificate-v1"
BINDING_SCHEMA = "literal-root-field-evidence-binding-v1"
MARKER = "R314_FIELD_CERTIFICATE "
SOURCE_PINS = {
    "geometry_20261115_native_primal128.cpp": "1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d",
    "geometry_20261115_native_trace_variation128.cpp": "8c40b4c7ed214a16afd06cd0157bf861822cb217a72bd0117bbed7f2c954204d",
    "geometry_20261115_native_shared_trace128.hpp": "bcca73719ffb98d5d0aed5bc4c88c789343be048475aae22a3b495097f345c6b",
    "geometry_20261115_native_operator_trace128.hpp": "950e1810106f2d268dd87da89be9c042ad3d3a014ea25e7c688701d731a3ddb0",
    "geometry_20261115_literal_root_field_tape128.cpp": "2aa2ad6737ca16854350967bddf49846e345ba5195d799d21dcc40a870c925bb"
}
BITS = 0
ONE = 0
DEADLINE = 0.0
CHECKS = 0


class ResourceEnded(RuntimeError):
    pass


class Unresolved(RuntimeError):
    pass


def tick():
    global CHECKS
    CHECKS += 1
    if time.monotonic() >= DEADLINE:
        raise ResourceEnded("explicit-certificate-wall-budget")


def require(value, reason):
    if not value:
        raise ValueError(reason)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode()


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def receipt(path, root=None):
    path = Path(path)
    return dict(file=path.name if root is None else path.relative_to(root).as_posix(),
                bytes=path.stat().st_size, sha256=sha(path))


def relative(root, name):
    p = Path(name)
    require(not p.is_absolute() and ".." not in p.parts and p.parts,
            "relative-evidence-path")
    target = (root / p).resolve(strict=True)
    require(root.resolve() in target.parents and target.is_file(),
            "regular-file-under-evidence-root")
    return target


def checked(root, desc):
    path = relative(root, desc["file"])
    require(receipt(path, root) == desc, "exact-evidence-bytes:" + desc["file"])
    return path


def ceil_div(a, b):
    if b <= 0:
        raise ValueError("positive-integer-denominator")
    return -((-a) // b)


class I:
    """Closed interval [lo,hi]/2**BITS; all primitive endpoints are outward."""
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo, self.hi = int(lo), int(lo if hi is None else hi)
        if self.lo > self.hi:
            raise ValueError("reversed-interval")

    @staticmethod
    def integer(x):
        return I(int(x) * ONE)

    @staticmethod
    def ratio(a, b):
        if b < 0:
            a, b = -a, -b
        if b == 0:
            raise Unresolved("division-by-zero")
        return I((int(a)*ONE)//int(b), ceil_div(int(a)*ONE, int(b)))

    @staticmethod
    def dyadic(m, exponent):
        exponent = int(exponent) + BITS
        if exponent >= 0:
            return I(int(m) << exponent)
        den = 1 << (-exponent)
        return I(int(m)//den, ceil_div(int(m), den))

    @staticmethod
    def word(word, exponent_bits, fraction_bits, bias):
        sign = -1 if word >> (exponent_bits+fraction_bits) else 1
        exp = (word >> fraction_bits) & ((1 << exponent_bits)-1)
        frac = word & ((1 << fraction_bits)-1)
        if exp == (1 << exponent_bits)-1:
            raise ValueError("nonfinite-original-word")
        if exp == 0:
            return I.dyadic(sign*frac, 1-bias-fraction_bits)
        return I.dyadic(sign*((1 << fraction_bits)+frac),
                        exp-bias-fraction_bits)

    def __add__(self, other):
        if isinstance(other, D):
            return NotImplemented
        b = as_i(other)
        return I(self.lo+b.lo, self.hi+b.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        if isinstance(other, D):
            return NotImplemented
        return self + (-as_i(other))

    def __rsub__(self, other):
        return as_i(other) - self

    def __mul__(self, other):
        if isinstance(other, D):
            return NotImplemented
        b = as_i(other)
        products = (self.lo*b.lo, self.lo*b.hi,
                    self.hi*b.lo, self.hi*b.hi)
        return I(min(products)//ONE, ceil_div(max(products), ONE))

    __rmul__ = __mul__

    def reciprocal(self):
        if self.lo <= 0 <= self.hi:
            raise Unresolved("interval-denominator-contains-zero")
        if self.hi < 0:
            return -(-self).reciprocal()
        return I((ONE*ONE)//self.hi, ceil_div(ONE*ONE, self.lo))

    def __truediv__(self, other):
        if isinstance(other, D):
            return NotImplemented
        return self * as_i(other).reciprocal()

    def __rtruediv__(self, other):
        return as_i(other) / self

    def sqrt(self):
        if self.lo < 0:
            raise Unresolved("square-root-box-not-nonnegative")
        lower = math.isqrt(self.lo*ONE)
        upper = math.isqrt(self.hi*ONE)
        if upper*upper < self.hi*ONE:
            upper += 1
        return I(lower, upper)

    def abs_upper(self):
        return max(abs(self.lo), abs(self.hi))

    def widen(self, upper):
        require(upper >= 0, "nonnegative-radius")
        return I(self.lo-upper, self.hi+upper)

    def payload(self):
        return [str(self.lo), str(self.hi)]


def as_i(x):
    return x if isinstance(x, I) else I.integer(x)


ZERO = None


class D:
    """One directed interval directional derivative, not a rounded-word derivative."""
    __slots__ = ("v", "d")

    def __init__(self, value, direction=0):
        self.v, self.d = as_i(value), as_i(direction)

    def __add__(self, other):
        b = as_d(other)
        return D(self.v+b.v, self.d+b.d)

    __radd__ = __add__

    def __neg__(self):
        return D(-self.v, -self.d)

    def __sub__(self, other):
        return self + (-as_d(other))

    def __rsub__(self, other):
        return as_d(other) - self

    def __mul__(self, other):
        b = as_d(other)
        return D(self.v*b.v, self.d*b.v+self.v*b.d)

    __rmul__ = __mul__

    def __truediv__(self, other):
        b = as_d(other)
        return D(self.v/b.v, (self.d*b.v-self.v*b.d)/(b.v*b.v))

    def __rtruediv__(self, other):
        return as_d(other) / self

    def sqrt(self):
        s = self.v.sqrt()
        return D(s, self.d/(2*s))


def as_d(x):
    return x if isinstance(x, D) else D(x)


def dot(a, b):
    require(len(a) == len(b), "dot-dimensions")
    total = I.integer(0)
    for x, y in zip(a, b):
        total = total + x*y
    return total


def matvec(a, x):
    result = []
    for row in a:
        tick()
        result.append(dot(row, x))
    return result


def matrix_product(a, b):
    n, k = len(a), len(b)
    require(n > 0 and k > 0 and len(a[0]) == k, "matrix-dimensions")
    bt = list(zip(*b))
    out = []
    for row in a:
        tick()
        out.append([dot(row, col) for col in bt])
    return out


def transpose(a):
    return [list(row) for row in zip(*a)]


def flat_matrix(values, n):
    require(len(values) == n*n, "square-matrix-words")
    return [values[i*n:(i+1)*n] for i in range(n)]


def maximum_abs(items):
    return max((v.abs_upper() for v in items), default=0)


def scalar_upper(x):
    return {"numerator": str(x), "binary_exponent": -BITS}


def write_intervals(path, items, shape):
    payload = {"schema": "outward-fixed-binary-interval-array-v1",
               "bits": BITS, "shape": shape,
               "endpoints": [x.payload() for x in items]}
    with gzip.open(path, "wb", compresslevel=6) as stream:
        stream.write(canonical(payload))


def read_words(root, manifests, name, count):
    desc = manifests[name]
    path = checked(root, desc)
    data = path.read_bytes()
    require(len(data) == 16*count, "full-binary128-array:" + name)
    return [I.word(int.from_bytes(data[i:i+16], "little"), 15, 112, 16383)
            for i in range(0, len(data), 16)]


def exact_64_to_128(word):
    sign = word >> 63
    e = (word >> 52) & 2047
    f = word & ((1 << 52)-1)
    require(e != 2047, "finite-original-binary64")
    if not e:
        if not f:
            return sign << 127
        shift = f.bit_length()-1
        exponent = shift-1074+16383
        fraction = (f-(1 << shift)) << (112-shift)
    else:
        exponent = e-1023+16383
        fraction = f << 60
    return (sign << 127) | (exponent << 112) | fraction


def verify_literal_tables(packet, root, manifests, angles, tape):
    """Byte identity only: exact lift of every original frequency/cos/sin/Gram word."""
    with packet.open("rb") as stream:
        header = stream.read(24)
        require(header[:8] == b"QPR11301", "original-packet-magic")
        dims = [int.from_bytes(header[i:i+4], "little") for i in range(8, 24, 4)]
        require(dims[:3] == [112, angles, 576] and dims[3] in (1, 2),
                "complete-original-packet-layout")
        constants = stream.read(48)
        require(len(constants) == 48, "all-original-constants")
        formed_constants = checked(root, manifests["large-arrays/constants.f128"]).read_bytes()
        require(len(formed_constants) == 17*16, "complete-exported-constants")
        for k in range(6):
            wanted = exact_64_to_128(int.from_bytes(constants[8*k:8*(k+1)], "little"))
            require(int.from_bytes(formed_constants[16*k:16*(k+1)], "little") == wanted,
                    "unchanged-original-constant-word")
        sign_word = 0x3ff0000000000000 if dims[3] == 1 else 0xbff0000000000000
        require(int.from_bytes(formed_constants[96:112], "little") == exact_64_to_128(sign_word),
                "unchanged-original-orientation")
        for name, count in (("frequency.f128", 112), ("cosine.f128", angles*113),
                            ("sine.f128", angles*112), ("independent-gram225.f128", angles*225)):
            path = checked(root, manifests["large-arrays/"+name])
            with path.open("rb") as actual:
                for index in range(count):
                    if index % 4096 == 0:
                        tick()
                    raw = stream.read(8)
                    require(len(raw) == 8, "full-original-literal-table")
                    wanted = exact_64_to_128(int.from_bytes(raw, "little")).to_bytes(16, "little")
                    require(actual.read(16) == wanted, "unaltered-independent-literal-word:" + name)
                require(actual.read(1) == b"", "literal-output-no-suffix")
        stream.seek(8*(2*577*224+112+577+112), 1)
        selected = None
        for stage in range(576):
            tick()
            cell = stream.read(20)
            require(len(cell) == 20, "complete-original-cell-header")
            count = int.from_bytes(cell[16:20], "little")
            require(1 <= count <= 100000, "actual-cell-step-count")
            for step in range(count):
                raw = stream.read(128)
                require(len(raw) == 128, "complete-original-step")
                if stage == tape["stage"] and step == tape["RK_step"]:
                    gi = 0 if tape["field"] == 0 else 2 if tape["field"] == 3 else 1
                    selected = raw[8+gi*40:8+(gi+1)*40]+cell[:16]+raw[:8]
        require(stream.read(1) == b"" and selected is not None, "selected-actual-geometry-no-suffix")
        for k in range(8):
            wanted = exact_64_to_128(int.from_bytes(selected[8*k:8*(k+1)], "little"))
            require(int.from_bytes(formed_constants[(7+k)*16:(8+k)*16], "little") == wanted,
                    "actual-field-geometry-mu-ratio-step-word")
        if tape["original_policy"] == "original":
            require(formed_constants[15*16:17*16] == formed_constants[4*16:6*16],
                    "unchanged-original-root-policy")
    return {"all_literal_frequency_cosine_sine_gram_words_match_original_packet": True,
            "gram_is_independent_table": True,
            "literal_square_roots_regenerated": False}


class Evidence:
    def __init__(self, root, binding_sha):
        self.root = root.resolve(strict=True)
        binding_path = root/"input-binding.json"
        require(sha(binding_path) == binding_sha, "explicit-binding-SHA")
        self.binding = json.loads(binding_path.read_bytes())
        require(self.binding["schema"] == BINDING_SCHEMA, "evidence-binding-schema")
        for name, digest in SOURCE_PINS.items():
            require(self.binding["sources"].get(name, {}).get("sha256") == digest,
                    "frozen-mathematical-source:" + name)
        require(self.binding["sources"].get(Path(__file__).name, {}).get("sha256") == sha(__file__),
                "actual-interval-consumer-source")
        for descriptor in self.binding["sources"].values():
            require(set(descriptor) == {"file", "bytes", "sha256"}, "source-receipt-shape")
        manifest = json.loads(checked(root, self.binding["file_manifest"]).read_bytes())
        require(manifest["schema"] == "literal-root-field-temporary-files-v1", "manifest-schema")
        self.files = {}
        for item in manifest["files"]:
            require(item["file"] not in self.files, "unique-temporary-file")
            self.files[item["file"]] = item
            checked(root, item)
        self.result = json.loads(checked(root, self.files["export-result.json"]).read_bytes())
        require(self.result["schema"] == "literal-root-field-export-result-v1"
                and self.result["tape_ready"] is True, "actual-root-tape-returned")
        self.tape = json.loads(checked(root, self.files["tape.json"]).read_bytes())
        require(self.tape["schema"] == "literal-root-field-tape-v1", "actual-tape-schema")
        require(self.tape["modes"] == 112 and self.tape["root_dimension"] == 113
                and self.tape["state_dimension"] == 226 and self.tape["shape_dimension"] == 224,
                "all-original-dimensions")
        require(self.tape["columns_requested"] in (224, 230), "explicit-full-column-family")
        self.N = self.tape["angles"]
        require(isinstance(self.N, int) and 896 < self.N <= 65536, "actual-angular-count")
        for label, item in self.binding["inputs"].items():
            path = Path(item["absolute_path"]).resolve(strict=True)
            require(path.stat().st_size == item["bytes"] and sha(path) == item["sha256"],
                    "actual-same-job-input:" + label)
        owner = json.loads(Path(self.binding["inputs"]["owner_summary"]["absolute_path"]).read_bytes())
        for name in ("GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA"):
            require(owner["run"][name] == os.environ.get(name), "same-job-owner:" + name)
        require(owner["final_state128"]["sha256"] == self.binding["inputs"]["state"]["sha256"],
                "actual-owner-final-state-not-deleted-hash")
        packet = Path(self.binding["inputs"]["packet"]["absolute_path"]).resolve(strict=True)
        original = self.binding["inputs"]["packet"]
        require(packet.stat().st_size == original["bytes"] and sha(packet) == original["sha256"],
                "actual-original-packet-still-present")
        self.literal_check = verify_literal_tables(packet, root, self.files, self.N, self.tape)
        self.frequency = self.words("frequency.f128", 112)
        self.cosine = self.words("cosine.f128", self.N*113)
        self.sine = self.words("sine.f128", self.N*112)
        self.gram = self.words("independent-gram225.f128", self.N*225)
        self.constants = self.words("constants.f128", 17)
        self.state = self.words("field-input226.f128", 226)
        self.nominal_rhs = self.words("nominal-RHS226.f128", 226)
        self.nominal_L = self.words("nominal-returned-L113.f128", 113)
        self.sq2, self.sq12, self.floor = self.constants[:3]
        self.g = self.constants[7:13]
        self.orientation = self.constants[6]
        require(self.orientation.lo == self.orientation.hi
                and self.orientation.lo in (-ONE, ONE), "literal-orientation")
        self.updates = []
        for index, item in enumerate(self.tape["updates"]):
            require(item["update"] == index and 0 <= item["backtrack"] < 20,
                    "actual-finite-update-order")
            self.updates.append(dict(item, e=self.words("update-%d/e113.f128" % index, 113),
                F=self.words("update-%d/formed-F113.f128" % index, 113),
                C=flat_matrix(self.words("update-%d/formed-C113x113.f128" % index, 113*113), 113),
                L=flat_matrix(self.words("update-%d/nominal-factor113x113.f128" % index, 113*113), 113),
                forward=self.words("update-%d/nominal-forward113.f128" % index, 113),
                solve=self.words("update-%d/nominal-solve113.f128" % index, 113)))
        require(len(self.updates) <= 29, "successful-root-at-most29-updates")
        require(len(self.updates) == self.result["updates"], "same-returned-update-count")

    def words(self, name, count):
        return read_words(self.root, self.files, "large-arrays/"+name, count)

    def column(self, index):
        prefix = "column-%d/" % index
        complete = self.files.get("large-arrays/"+prefix+"complete.json")
        if complete is None:
            raise Unresolved("nominal-column-not-complete:" + str(index))
        record = json.loads(checked(self.root, complete).read_bytes())
        require(record == {"column": index, "complete": True}, "full-nominal-column-marker")
        seed = self.words(prefix+"input-seed226.f128", 226)
        env = self.words(prefix+"environment-seed6.f128", 6)
        require(all(x.lo == x.hi == (ONE if j == index and index < 224 else 0)
                    for j, x in enumerate(seed)), "actual-full-state-coordinate-basis")
        require(all(x.lo == x.hi == (ONE if 224+j == index else 0)
                    for j, x in enumerate(env)), "actual-independent-environment-basis")
        return dict(seed=seed, env=env,
                    rhs=self.words(prefix+"nominal-RHS-direction226.f128", 226),
                    L=self.words(prefix+"returned-L-direction.f128", 113),
                    solves=[self.words(prefix+"update-%d/nominal-solve-direction.f128" % k, 113)
                            for k in range(len(self.updates))])


def physical_inputs(ev, seed=None, env=None):
    if seed is None:
        seed = [I.integer(0) for _ in range(226)]
    if env is None:
        env = [I.integer(0) for _ in range(6)]
    r, dr, w, w2, E, mu = [D(v, d) for v, d in zip(ev.g, env)]
    state = [D(v, d) for v, d in zip(ev.state, seed)]
    r3, r4 = r*r*r, (r*r)*(r*r)
    fac = ev.orientation*ev.sq12*mu/(ev.sq2*r4*w2)
    target = [D(0)] + [fac*state[112+j] for j in range(112)]
    momentum = [-ev.frequency[j]*r3*state[j]/(ev.sq2*w) for j in range(112)]
    P, Pt = [], []
    for n in range(ev.N):
        if n % 32 == 0:
            tick()
        sn, cs = ev.sine[n*112:(n+1)*112], ev.cosine[n*113:(n+1)*113]
        p, pt = D(0), D(0)
        for j in range(112):
            p = p + momentum[j]*sn[j]
            pt = pt + ev.frequency[j]*momentum[j]*cs[j+1]
        P.append(p);Pt.append(pt)
    return dict(target=target, momentum=momentum, P=P, Pt=Pt, geometry=[r, dr, w, w2, E, mu])


def local_expression(P, Pt, L, U, w2, E):
    K = L-Pt
    T = 2*K+K*K+E*P*P
    u = w2*T
    DD, S, A = 1-u, 1-w2*P*P, 1+L+w2*Pt
    sd = DD.sqrt()
    fc = u*(2+sd)/(2*sd*(1+sd)*(1+sd))
    gc = w2*(P*P+S*T/(1+sd))/(S*sd)
    quad = (K*K+E*P*P)/2+K*Pt+T*fc+(1+K)*Pt*gc
    am = L+w2*Pt
    dm = u*(sd+1/(1+sd))/(DD*sd)
    rho = am+(1+am)*dm
    flux = U*(K+u/(1+sd)+w2*P*P*sd)/(S*sd)
    return quad, rho, flux, DD, S, A


def prepare_formed(ev, ebox, inputs, partials=True):
    """Full accurate F/C and interval angular derivatives; no C=F_e identity."""
    L = [inputs["target"][j].v+ebox[j] for j in range(113)]
    F = [I.integer(0) for _ in range(113)]
    beta = [I.integer(0) for _ in range(225)]
    rows, flux = [], [I.integer(0) for _ in range(112)]
    lower = None
    invN = I.ratio(1, ev.N)
    w2, E = ev.g[3], ev.g[4]
    for n in range(ev.N):
        if n % 16 == 0:
            tick()
        cs = ev.cosine[n*113:(n+1)*113]
        sn = ev.sine[n*112:(n+1)*112]
        gram = ev.gram[n*225:(n+1)*225]
        Lv, U = L[0], I.integer(0)
        for j in range(112):
            m = ev.frequency[j]
            Lv = Lv+L[j+1]*cs[j+1]
            U = U+(-m*L[j+1]+(m*m-1)*inputs["momentum"][j].v)*sn[j]
        vals = [inputs["P"][n].v, inputs["Pt"][n].v, Lv, U, w2, E]
        q, rho, fl, DD, S, A = local_expression(*vals)
        margin = min(DD.lo, S.lo, A.lo)-ev.floor.hi
        if margin <= 0:
            raise Unresolved("D-S-A-box-not-strictly-original-legal angle=" + str(n))
        lower = margin if lower is None else min(lower, margin)
        for j in range(113):
            F[j] = F[j]+q*cs[j]*invN
        for j in range(225):
            beta[j] = beta[j]+rho*gram[j]*invN
        for j in range(112):
            flux[j] = flux[j]+fl*sn[j]*invN
        part = [[], [], []]
        if partials:
            for axis in range(6):
                args = [D(x, 1 if k == axis else 0) for k, x in enumerate(vals)]
                dq, dc, df, _, _, _ = local_expression(*args)
                for target, value in zip(part, (dq, dc, df)):
                    target.append(value.d)
        rows.append(part)
    F = [x+y for x, y in zip(F, ebox)]
    C = []
    for i in range(113):
        row = []
        for j in range(113):
            if i == 0 and j == 0:
                value = beta[0]
            elif min(i, j) == 0:
                value = ev.sq2*beta[max(i, j)]
            else:
                value = beta[abs(i-j)]+beta[i+j]
            row.append(value+(1 if i == j else 0))
        C.append(row)
    return dict(F=F, C=C, rows=rows, flux=flux, L=L,
                legal_margin_lower=lower, gram_beta=beta)


def interval_cholesky(C):
    n = len(C)
    L = [[I.integer(0) for _ in range(n)] for _ in range(n)]
    minimum = None
    for i in range(n):
        tick()
        for j in range(i+1):
            value = C[i][j]
            for k in range(j):
                value = value-L[i][k]*L[j][k]
            if i == j:
                if value.lo <= 0:
                    raise Unresolved("accurate-formed-C-SPD-not-certified pivot=" + str(i))
                minimum = value.lo if minimum is None else min(minimum, value.lo)
                L[i][j] = value.sqrt()
            else:
                L[i][j] = value/L[j][j]
    return L, minimum


def point_inverse_candidate(L):
    """Midpoint of an interval inverse of the nominal LLt, only a candidate."""
    n = len(L)
    Y = [[None for _ in range(n)] for _ in range(n)]
    for col in range(n):
        tick()
        temp, out = [], [I.integer(0) for _ in range(n)]
        for i in range(n):
            v = I.integer(1 if i == col else 0)
            for j in range(i):
                v = v-L[i][j]*temp[j]
            temp.append(v/L[i][i])
        for i in range(n-1, -1, -1):
            v = temp[i]
            for j in range(i+1, n):
                v = v-L[j][i]*out[j]
            out[i] = v/L[i][i]
        for i in range(n):
            Y[i][col] = I((out[i].lo+out[i].hi)//2)
    return Y


class InverseCertificate:
    def __init__(self, C, L):
        self.C = C
        _, self.spd_pivot_lower = interval_cholesky(C)
        self.Y = point_inverse_candidate(L)
        product = matrix_product(self.Y, C)
        self.N = [[((1 if i == j else 0)-product[i][j]).abs_upper()
                   for j in range(len(C))] for i in range(len(C))]
        self.q = max(sum(row) for row in self.N)
        if self.q >= ONE:
            raise Unresolved("formed-C-inverse-comparison-not-contractive")

    def comparison_bound(self, residual):
        v = [x.abs_upper() for x in matvec(self.Y, residual)]
        current, total = list(v), [0 for _ in v]
        # Finite positive Neumann terms plus the rigorous remaining infinity tail.
        for _ in range(12):
            tick()
            total = [a+b for a, b in zip(total, current)]
            current = [sum(ceil_div(n*x, ONE) for n, x in zip(row, current))
                       for row in self.N]
        tail = ceil_div(max(current, default=0)*ONE, ONE-self.q)
        return [value+tail for value in total]

    def solve_enclosure(self, rhs, nominal):
        residual = [a-b for a, b in zip(matvec(self.C, nominal), rhs)]
        bound = self.comparison_bound(residual)
        return [x.widen(e) for x, e in zip(nominal, bound)], bound, residual


def structured_C_action(ev, beta, v):
    answer = []
    for i in range(113):
        tick()
        s = I.integer(0)
        for j in range(113):
            if i == 0 and j == 0:
                entry = beta[0]
            elif min(i, j) == 0:
                entry = ev.sq2*beta[max(i, j)]
            else:
                entry = beta[abs(i-j)]+beta[i+j]
            s = s+entry*v[j]
        answer.append(s)
    return answer


def formed_direction(ev, formed, de, inputs, direction_inputs, env):
    invN = I.ratio(1, ev.N)
    dL = [direction_inputs["target"][j].d+de[j] for j in range(113)]
    dF = [I.integer(0) for _ in range(113)]
    beta = [I.integer(0) for _ in range(225)]
    dflux = [I.integer(0) for _ in range(112)]
    for n in range(ev.N):
        if n % 16 == 0:
            tick()
        cs, sn = ev.cosine[n*113:(n+1)*113], ev.sine[n*112:(n+1)*112]
        gram = ev.gram[n*225:(n+1)*225]
        dl, du = dL[0], I.integer(0)
        for j in range(112):
            m = ev.frequency[j]
            dl = dl+dL[j+1]*cs[j+1]
            du = du+(-m*dL[j+1]+(m*m-1)*direction_inputs["momentum"][j].d)*sn[j]
        x = [direction_inputs["P"][n].d, direction_inputs["Pt"][n].d,
             dl, du, env[3], env[4]]
        dq, dc, df = [dot(row, x) for row in formed["rows"][n]]
        for j in range(113):
            dF[j] = dF[j]+dq*cs[j]*invN
        for j in range(225):
            beta[j] = beta[j]+dc*gram[j]*invN
        for j in range(112):
            dflux[j] = dflux[j]+df*sn[j]*invN
    return dict(F=[x+y for x, y in zip(dF, de)], beta=beta, flux=dflux, L=dL)


def rhs_formed(ev, L, flux, seed=None, env=None, dL=None, dflux=None):
    if seed is None:
        seed = [I.integer(0) for _ in range(226)]
    if env is None:
        env = [I.integer(0) for _ in range(6)]
    if dL is None:
        dL = [I.integer(0) for _ in range(113)]
    if dflux is None:
        dflux = [I.integer(0) for _ in range(112)]
    r, dr, w, w2, E, mu = [D(v, d) for v, d in zip(ev.g, env)]
    r3, sigma = r*r*r, dr/r
    pref = ev.orientation*ev.sq2*r3*dr*w2/(ev.sq12*mu)
    out = [D(0) for _ in range(226)]
    for j in range(112):
        m = ev.frequency[j]
        y, pi = D(ev.state[j], seed[j]), D(ev.state[112+j], seed[112+j])
        ell = D(L[j+1], dL[j+1])
        momentum = -m*r3*y/(ev.sq2*w)
        out[j] = sigma*((m*m-4)*y+ev.sq2*w*ell/r3)
        out[112+j] = 4*sigma*pi+pref*m*(-m*ell+(m*m-1)*momentum+D(flux[j], dflux[j]))
    out[224], out[225] = dr*w*D(L[0], dL[0]), dr*w
    return out


def nominal_defects(formed, u):
    L, oldC, oldF = u["L"], u["C"], u["F"]
    B = matrix_product(L, transpose(L))
    R = [[B[i][j]-oldC[i][j] for j in range(113)] for i in range(113)]
    a = [x-y for x, y in zip(matvec(L, u["forward"]), oldF)]
    b = [x-y for x, y in zip(matvec(transpose(L), u["solve"]), u["forward"])]
    deltaC = [[formed["C"][i][j]-oldC[i][j] for j in range(113)] for i in range(113)]
    deltaF = [x-y for x, y in zip(formed["F"], oldF)]
    direct = [x-y for x, y in zip(matvec(formed["C"], u["solve"]), formed["F"])]
    # The decomposed expression and direct one both enclose the same real
    # residual. They are reported independently; equality of interval endpoints
    # is neither required nor implied.
    Lb, Rs, dCs = matvec(L, b), matvec(R, u["solve"]), matvec(deltaC, u["solve"])
    assembled = [a[i]+Lb[i]-Rs[i]+dCs[i]-deltaF[i] for i in range(113)]
    return {"factor": [x for row in R for x in row],
            "forward": a, "backward": b,
            "C_formation": [x for row in deltaC for x in row],
            "F_formation": deltaF, "complete_direct_step_residual": direct,
            "complete_decomposed_step_residual": assembled}


def run_certificate(ev, args, out, result):
    large = out/"large-arrays";large.mkdir()
    inputs = physical_inputs(ev)
    ebox = [I.integer(0) for _ in range(113)]
    caches = []
    for k, u in enumerate(ev.updates):
        tick()
        formed = prepare_formed(ev, ebox, inputs)
        inverse = InverseCertificate(formed["C"], u["L"])
        solved, bound, residual = inverse.solve_enclosure(formed["F"], u["solve"])
        # Pure formation defects are evaluated at the actual nominal e words.
        # The separate propagated box additionally contains earlier accurate
        # trace error and must never be relabelled as pure formation error.
        point_formed = prepare_formed(ev, u["e"], inputs, partials=False)
        defects = nominal_defects(point_formed, u)
        d = large/("update-"+str(k));d.mkdir()
        for name, array in defects.items():
            shape = [113, 113] if len(array) == 113*113 else [113]
            write_intervals(d/(name+".json.gz"), array, shape)
        write_intervals(d/"incoming-e113.json.gz", ebox, [113])
        write_intervals(d/"accurate-solve113.json.gz", solved, [113])
        write_intervals(d/"inverse-candidate113x113.json.gz",
                        [x for row in inverse.Y for x in row], [113, 113])
        comparison = {"bits": BITS, "N_upper": [[str(x) for x in row] for row in inverse.N],
                      "q_upper": str(inverse.q), "weights": "all-one",
                      "positive_Cholesky_pivot_lower": str(inverse.spd_pivot_lower)}
        with gzip.open(d/"comparison.json.gz", "wb", compresslevel=6) as f:
            f.write(canonical(comparison))
        caches.append((formed, inverse, solved))
        alpha = I.dyadic(1, -u["backtrack"])
        ebox = [e-alpha*s for e, s in zip(ebox, solved)]
        result["primal_updates"].append(dict(update=k, backtrack=u["backtrack"],
            accurate_C_SPD_certified=True, inverse_comparison_certified=True,
            q_upper=scalar_upper(inverse.q), exact_solve_error_upper=scalar_upper(max(bound)),
            full_C_formation_error_upper=scalar_upper(maximum_abs(defects["C_formation"])),
            full_F_formation_error_upper=scalar_upper(maximum_abs(defects["F_formation"])),
            formation_at_actual_nominal_e_words=True,
            propagated_C_box_is_separate_from_point_formation=True,
            all_113_solve_rows_included=True, all_225_gram_terms_included=True))
    final_formed = prepare_formed(ev, ebox, inputs)
    rhs = rhs_formed(ev, final_formed["L"], final_formed["flux"])
    value = [x.v for x in rhs]
    errors = [x-y for x, y in zip(value, ev.nominal_rhs)]
    write_intervals(large/"accurate-returned-L113.json.gz", final_formed["L"], [113])
    write_intervals(large/"accurate-RHS226.json.gz", value, [226])
    write_intervals(large/"RHS226-minus-nominal.json.gz", errors, [226])
    write_intervals(large/"accurate-returned-F113.json.gz", final_formed["F"], [113])
    result["fixed_trace_primal_field_certified"] = True
    result["complete_226_output_error_upper"] = scalar_upper(maximum_abs(errors))
    result["mean_output_error_uppers"] = [scalar_upper(x.abs_upper()) for x in errors[224:]]
    result["recorded_returned_F_is_not_asserted_zero"] = True
    result["returned_accurate_F_upper"] = scalar_upper(maximum_abs(final_formed["F"]))
    for column in range(args.first_column, args.first_column+args.columns):
        tick()
        result["active_column"] = column
        nominal = ev.column(column)
        direction_inputs = physical_inputs(ev, nominal["seed"], nominal["env"])
        de = [I.integer(0) for _ in range(113)]
        summaries = []
        d = large/("column-"+str(column));d.mkdir()
        for k, (formed, inverse, solved) in enumerate(caches):
            tick()
            tangent = formed_direction(ev, formed, de, inputs, direction_inputs, nominal["env"])
            action = structured_C_action(ev, tangent["beta"], solved)
            rhs_direction = [a-b for a, b in zip(tangent["F"], action)]
            ds, bound, residual = inverse.solve_enclosure(rhs_direction, nominal["solves"][k])
            write_intervals(d/("update-%d-accurate-dsolve113.json.gz" % k), ds, [113])
            write_intervals(d/("update-%d-full-beta225.json.gz" % k), tangent["beta"], [225])
            write_intervals(d/("update-%d-direction-residual113.json.gz" % k), residual, [113])
            de = [x-I.dyadic(1, -ev.updates[k]["backtrack"])*y for x, y in zip(de, ds)]
            summaries.append(dict(update=k, error_upper=scalar_upper(max(bound)),
                                  actual_accurate_solve_interval_used_in_DC_action=True))
        tangent = formed_direction(ev, final_formed, de, inputs, direction_inputs, nominal["env"])
        full = rhs_formed(ev, final_formed["L"], final_formed["flux"],
                          nominal["seed"], nominal["env"], tangent["L"], tangent["flux"])
        derivative = [x.d for x in full]
        error = [a-b for a, b in zip(derivative, nominal["rhs"])]
        write_intervals(d/"accurate-RHS-direction226.json.gz", derivative, [226])
        write_intervals(d/"direction226-minus-nominal.json.gz", error, [226])
        row = dict(column=column, complete=True, all_226_rows=True,
                   shape_error_upper=scalar_upper(maximum_abs(error[:224])),
                   mean_error_uppers=[scalar_upper(x.abs_upper()) for x in error[224:]],
                   root_updates=summaries)
        result["columns"].append(row)
        print(MARKER+canonical(dict(event="column_certified", column=column,
                                   all_226_rows=True, native_accepted=False)).decode(), flush=True)
    result["active_column"] = None
    result["requested_columns_certified"] = True
    result["complete_224_shape_columns_certified"] = (
        args.first_column == 0 and args.columns >= 224)
    result["complete_6_independent_environment_columns_certified"] = (
        args.first_column == 0 and args.columns == 230)


def main():
    global BITS, ONE, DEADLINE, ZERO
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--tape-directory", type=Path, required=True)
    p.add_argument("--binding-sha256", required=True)
    p.add_argument("--bits", type=int, default=320)
    p.add_argument("--seconds", type=int, required=True)
    p.add_argument("--first-column", type=int, default=0)
    p.add_argument("--columns", type=int, default=230)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    args.tape_directory = args.tape_directory.resolve(strict=True)
    args.out = args.out.resolve()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public",
            "public-Actions-scientific-consumer-only")
    require(160 <= args.bits <= 4096 and 1 <= args.seconds <= 20000,
            "explicit-precision-and-resource-budget")
    require(args.first_column >= 0 and args.columns > 0
            and args.first_column+args.columns <= 230, "explicit-column-range")
    require(not args.out.exists(), "fresh-certificate-output")
    args.out.mkdir(parents=True)
    BITS, ONE = args.bits, 1 << args.bits
    ZERO = I.integer(0)
    start = time.monotonic();DEADLINE = start+args.seconds
    result = dict(schema=SCHEMA, source_sha256=sha(__file__),
        run_id=os.environ.get("GITHUB_RUN_ID"), run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        source_commit=os.environ.get("GITHUB_SHA"), command=sys.argv,
        bits=BITS, seconds=args.seconds, scientific_arithmetic=True,
        byte_only=False, procedure_completed=False, unresolved=False, budget_exhausted=False,
        first_column=args.first_column, columns_requested=args.columns, active_column=None,
        primal_updates=[], columns=[], fixed_trace_primal_field_certified=False,
        requested_columns_certified=False, complete_224_shape_columns_certified=False,
        complete_6_independent_environment_columns_certified=False,
        accurate_C_cholesky_trace_object=True, C_is_assumed_F_e=False,
        direction_of_IEEE_roundmap_claimed=False, dynamic_branch_stability_proved=False,
        actual_equation_root_enclosure_proved=False,
        complete_RK_stage_certified=False, complete_576_stage_columns_certified=False,
        complete_cut_stage_far_129248_certified=False,
        complete_112_boundary_response_certified=False,
        original_physical_audit_completed=False, native_accepted=False,
        field_input_upstream_RK_error_certified=False,
        conditional_on_exact_saved_field_input_words=True)
    status = 2
    try:
        ev = Evidence(args.tape_directory, args.binding_sha256)
        require(args.first_column+args.columns <= ev.tape["columns_requested"],
                "requested-range-present-in-export-design")
        result["input_binding"] = receipt(args.tape_directory/"input-binding.json")
        result["original_input_identity"] = ev.binding["inputs"]
        result["source_closure"] = ev.binding["sources"]
        result["actual_field"] = ev.tape
        result["literal_table_check"] = ev.literal_check
        run_certificate(ev, args, args.out, result)
        result["procedure_completed"] = True
        status = 0
    except ResourceEnded as error:
        result["budget_exhausted"] = True;result["error"] = str(error);status = 3
    except Unresolved as error:
        result["unresolved"] = True;result["error"] = str(error)
        result["procedure_completed"] = True;status = 4
    except Exception as error:
        result["error"] = repr(error)
        result["traceback"] = traceback.format_exc()
        status = 2
    result["columns_completed"] = len(result["columns"])
    result["unvisited_column_suffix"] = [
        args.first_column+len(result["columns"]), args.first_column+args.columns]
    result["elapsed_seconds"] = time.monotonic()-start
    files = [receipt(path, args.out) for path in sorted(args.out.rglob("*")) if path.is_file()]
    manifest = args.out/"temporary-certificate-files.json"
    manifest.write_bytes(canonical(dict(schema="temporary-strict-certificate-manifest-v1", files=files)))
    result["temporary_file_manifest"] = receipt(manifest)
    full = args.out/"result.json";full.write_bytes(canonical(result))
    compact = {k: v for k, v in result.items() if k not in ("columns", "original_input_identity", "traceback")}
    compact["result"] = receipt(full)
    compact["column_rows"] = [{k: row[k] for k in ("column", "complete", "shape_error_upper", "mean_error_uppers")}
                              for row in result["columns"]]
    compact["summary_complete"] = True
    raw = canonical(compact)
    if len(raw) > 85000:
        compact["column_rows"] = None
        compact["summary_complete"] = False
        compact["transport_failure"] = "bounded-summary-overflow-full-result-temporary-only"
        raw = canonical(compact);status = 70
    if len(raw) > 90000:
        raw = canonical(dict(schema=SCHEMA, summary_complete=False, transport_failure=True,
                             result=receipt(full), native_accepted=False,
                             columns_completed=result["columns_completed"],
                             unvisited_column_suffix=result["unvisited_column_suffix"]))
        status = 70
    (args.out/"summary.json").write_bytes(raw)
    print(MARKER+raw.decode(), flush=True)
    return status


if __name__ == "__main__":
    raise SystemExit(main())
