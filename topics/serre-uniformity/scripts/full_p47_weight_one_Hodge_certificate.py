#!/usr/bin/env python3
"""Original full-p47 weight-one source and finite integral Hodge certificate.

The first request runs only 168-jet rank95 and ALL23 cusp residues/kernel73.
The uncalled hecke_bridge API is for a separately reviewed, budgeted request.
Every mathematical entry point requires this public repository's Actions.
"""
import hashlib
import json
import os
from pathlib import Path
import signal
import sys
import time
import traceback

ROOT = Path(__file__).resolve().parents[3]
REQUEST = ROOT / "topics/serre-uniformity/notes/full-p47-weight-one-Hodge-request.json"
START = time.monotonic()
STAGE = "preflight"
SOURCE = None
REQUEST_HASH = None
PROGRESS = {"last_complete_rank": 0, "rho_batches_completed": 0,
            "logarithmic_basis_certified": False, "Hodge_kernel_certified": False}


def digest(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True,
                          separators=(",", ":")).encode()).hexdigest()


def emit(kind, **data):
    print(json.dumps(dict(kind=kind, elapsed_seconds=time.monotonic()-START, **data),
                     sort_keys=True, ensure_ascii=False), flush=True)


def stop(signum, frame):
    raise TimeoutError("Mathematical budget; unfinished Hodge stages remain unresolved.")


def ci_only():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get(
            "GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("Mathematics is restricted to this public repository's Actions.")


def source_head():
    gd = ROOT / ".git"
    source = (gd / "HEAD").read_text().strip()
    if source.startswith("ref: "):
        ref = source[5:]
        if not ref.startswith("refs/") or ".." in ref.split("/"):
            raise RuntimeError("Unexpected ref.")
        path = gd / ref
        if path.exists():
            source = path.read_text().strip()
        else:
            rows = [s.split(" ", 1)[0] for s in (gd/"packed-refs").read_text().splitlines()
                    if s.endswith(" "+ref)]
            if len(rows) != 1:
                raise RuntimeError("Ambiguous actual checkout.")
            source = rows[0]
    if len(source) != 40 or source != os.environ.get("GITHUB_SHA"):
        raise RuntimeError("Actual checkout/GITHUB_SHA mismatch.")
    return source


class Original47Source:
    """Fixed actual source, not a transported X0 basis.

    Descriptor (a,c,d) means rho=d+c*i, and the FULL Reynolds form
    sum_x zeta^(a*Nx)*e_x*e_(rho*x)
          + zeta^(-a*Nx)*e_x*e_(bar(rho)*x).
    """

    def __init__(self, root=2, callback=None):
        ci_only()
        from sage.all import GF, PolynomialRing, ZZ, proof
        from sage.env import SAGE_VERSION
        if SAGE_VERSION != "10.6":
            raise RuntimeError("The source is pinned to Sage 10.6.")
        proof.all(True)
        self.p, self.q, self.root = 47, 4513, int(root)
        if not ZZ(self.p).is_prime(proof=True) or not ZZ(self.q).is_prime(proof=True):
            raise ArithmeticError("Fixed prime input failed.")
        if pow(self.root, 47, 4513) != 1 or self.root == 1:
            raise ArithmeticError("The actual root is not primitive.")
        self.K = GF(self.q)
        self.PR = PolynomialRing(self.K, "t")
        self.inv2 = pow(2, -1, self.q)
        self.inv47 = pow(47, -1, self.q)
        self.callback = callback
        self.labels = [(c,d) for c in range(47) for d in range(47) if c or d]
        self.half = [x for x in self.labels if x < self.neg(x)]
        counts = {n: 0 for n in range(1,47)}
        for x in self.half:
            counts[self.norm(x)] += 1
        if len(self.half) != 1104 or any(v != 24 for v in counts.values()):
            raise ArithmeticError("Incomplete full-norm half-vector fibers.")
        self._series_key = None
        self._series_value = None
        self.half_series_sha256 = None

    @staticmethod
    def neg(x):
        return ((-x[0]) % 47, (-x[1]) % 47)

    @staticmethod
    def multiply(rho, x):
        c,d = rho
        a,b = x
        return ((c*b+d*a) % 47, (d*b-c*a) % 47)

    @staticmethod
    def norm(x):
        n = (x[0]*x[0]+x[1]*x[1]) % 47
        if n == 0:
            raise ArithmeticError("A nonzero nonsplit vector had norm zero.")
        return n

    def constants(self, root):
        powers = [pow(int(root),d,self.q) for d in range(47)]
        ans = {}
        for c,d in self.labels:
            if c:
                ans[c,d] = (c*self.inv47-self.inv2) % self.q
            else:
                u = powers[d]
                ans[c,d] = ((u+1)*self.inv2*pow((u-1) % self.q,-1,self.q)) % self.q
        return ans

    def series(self, length, root):
        """Actual e_(c,d) coefficients 0,...,length-1; one cache at a time."""
        length, root = int(length), int(root)
        if length < 1 or length > 836:
            raise ValueError("This source API is restricted to the proved finite jet range.")
        if pow(root,47,self.q) != 1 or root == 1:
            raise ArithmeticError("Invalid Galois conjugate root.")
        key = (length,root)
        if self._series_key == key:
            return self._series_value
        cc = self.constants(root)
        coeff = {x:[cc[x]]+[0]*(length-1) for x in self.labels}
        powers = [pow(root,d,self.q) for d in range(47)]
        for n in range(1,length):
            for r in range(1,n+1):
                if n % r:
                    continue
                k, c = n//r, r % 47
                cm = (-c) % 47
                for d in range(47):
                    if c or d:
                        coeff[c,d][n] = (coeff[c,d][n]-powers[(d*k) % 47]) % self.q
                    if cm or d:
                        coeff[cm,d][n] = (coeff[cm,d][n]+powers[(-d*k) % 47]) % self.q
        for x in self.half:
            if any((a+b) % self.q for a,b in zip(coeff[x],coeff[self.neg(x)])):
                raise ArithmeticError("The original odd weight-one identity failed.")
        if length == 168 and root == self.root:
            self.half_series_sha256 = digest([coeff[x] for x in self.half])
        self._series_value = {x:self.PR(coeff[x]) for x in self.labels}
        self._series_key = key
        return self._series_value

    def jets(self, descriptors, length=168, root=None):
        """Return row jets in the exact requested descriptor order."""
        from sage.all import matrix
        root = self.root if root is None else int(root)
        descriptors = [tuple(map(int,v)) for v in descriptors]
        for a,c,d in descriptors:
            if not (1 <= a <= 46 and 0 <= c <= 23 and 0 <= d <= 23 and (c or d)):
                raise ValueError("A descriptor is outside the declared complete orbit range.")
        e = self.series(length,root)
        powers = [self.K(pow(root,j,self.q)) for j in range(47)]
        requested = {}
        for a,c,d in descriptors:
            requested.setdefault((c,d), []).append(a)
        answer = {}
        for rho, alist in requested.items():
            c,d = rho
            bar_rho = ((-c) % 47,d)
            first = {n:self.PR.zero() for n in range(1,47)}
            second = {n:self.PR.zero() for n in range(1,47)}
            for x in self.half:
                n = self.norm(x)
                first[n] += 2*(e[x]*e[self.multiply(rho,x)]).truncate(length)
                second[n] += 2*(e[x]*e[self.multiply(bar_rho,x)]).truncate(length)
            for a in dict.fromkeys(alist):
                F = self.PR.zero()
                for n in range(1,47):
                    F += powers[(a*n) % 47]*first[n]
                    F += powers[(-a*n) % 47]*second[n]
                answer[a,c,d] = [int(F[j]) for j in range(length)]
        return matrix(self.K, [answer[v] for v in descriptors])

    def residues(self, descriptors):
        """ALL23 actual residues, including width47, rows indexed by b=1,...,23."""
        from sage.all import matrix
        descriptors = [tuple(map(int,v)) for v in descriptors]
        rhos = list(dict.fromkeys((c,d) for a,c,d in descriptors))
        rows = []
        for b in range(1,24):
            root = pow(self.root,b,self.q)
            cc = self.constants(root)
            powers = [pow(root,j,self.q) for j in range(47)]
            grouped = {}
            for rho in rhos:
                c,d = rho
                bar_rho = ((-c) % 47,d)
                first = {n:0 for n in range(1,47)}
                second = {n:0 for n in range(1,47)}
                for x in self.half:
                    n = self.norm(x)
                    first[n] = (first[n]+2*cc[x]*cc[self.multiply(rho,x)]) % self.q
                    second[n] = (second[n]+2*cc[x]*cc[self.multiply(bar_rho,x)]) % self.q
                grouped[rho] = first,second
            row = []
            for a,c,d in descriptors:
                first,second = grouped[c,d]
                c0 = sum(powers[(a*n) % 47]*first[n]+powers[(-a*n) % 47]*second[n]
                         for n in range(1,47)) % self.q
                row.append((47*c0) % self.q)
            rows.append(row)
        return matrix(self.K,rows)


def integral_rows(M):
    return [[int(x) for x in row] for row in M.rows()]


def build_source(descriptors=None, max_rho_batches=64, callback=None,
                 expected_certificate=None):
    """Build or rebuild the actual source, entirely within a public CI run.

    New certificate: descriptors=None searches exactly the prescribed prefix.
    Later consumer: pass the certified 95 descriptors and expected hash fields;
    no candidate search or previously certified rank computation is repeated.
    Returns K, engine, descriptors, logarithmic_jets, residues, kernel,
    hodge_jets and certificate. Raw matrices stay only in the running process.
    """
    ci_only()
    from sage.all import matrix
    engine = Original47Source(root=2,callback=callback)
    K = engine.K

    def note(kind, **payload):
        if callback is not None:
            callback(kind,**payload)

    fresh = descriptors is None
    used_rho = []
    if fresh:
        rhos = sorted([(c,d) for c in range(24) for d in range(24) if c or d],
                      key=lambda z:(z[0]+z[1],z[0],z[1]))[:int(max_rho_batches)]
        rows, labels = [], []
        for rho in rhos:
            c,d = rho
            batch_labels = [[a,c,d] for a in range(1,47)]
            batch = engine.jets(batch_labels,length=168)
            combined_rows = rows+integral_rows(batch)
            combined_labels = labels+batch_labels
            pivots = list(matrix(K,combined_rows).transpose().pivots())
            rows = [combined_rows[i] for i in pivots]
            labels = [combined_labels[i] for i in pivots]
            if len(rows) > 95:
                raise ArithmeticError("Actual jets exceed the original line-bundle dimension.")
            used_rho.append([c,d])
            note("rank_progress",rho=[c,d],rho_batches_completed=len(used_rho),
                 forms_considered=46*len(used_rho),exact_rank=len(rows),
                 selected_basis_labels_sha256=digest(labels))
            if len(rows) == 95:
                break
        if len(rows) != 95:
            return {"complete":False,"last_complete_rank":len(rows),
                    "used_rho":used_rho,"descriptors":labels,
                    "selected_jets_sha256":digest(rows)}
        descriptors = labels
        J = matrix(K,rows)
        note("logarithmic_basis_certificate",dimension=95,jet_length=168,
             selected_forms=descriptors,used_rho=used_rho,
             basis_labels_sha256=digest(descriptors),
             basis_jets_sha256=digest(rows),
             original_half_series_sha256=engine.half_series_sha256)
    else:
        descriptors = [list(map(int,v)) for v in descriptors]
        if len(descriptors) != 95 or len({tuple(v) for v in descriptors}) != 95:
            raise ValueError("A rebuild requires exactly the certified 95 actual descriptors.")
        if expected_certificate is None:
            raise ValueError("A rebuild must pin the previous source certificate hashes.")
        J = engine.jets(descriptors,length=168)

    residues = engine.residues(descriptors)
    residue_rows = integral_rows(residues)
    if any(sum(row[j] for row in residue_rows) % 4513 for j in range(95)):
        raise ArithmeticError("ALL23 original cusp residues do not sum to zero.")
    if fresh and int(residues.rank()) != 22:
        raise ArithmeticError("Unexpected full residue rank.")
    kernel = residues.right_kernel().basis_matrix()
    if kernel.nrows() != 73 or kernel.ncols() != 95 or not (
            residues*kernel.transpose()).is_zero():
        raise ArithmeticError("Incorrect full integral Hodge-kernel reduction.")
    hodge_jets = kernel*J
    if fresh and int(hodge_jets.rank()) != 73:
        raise ArithmeticError("Original Hodge jets lost rank.")
    if any(hodge_jets[i,0] != 0 for i in range(73)):
        raise ArithmeticError("The all-cusp kernel is not holomorphic at the standard cusp.")
    cert = {
        "prime":47,"coefficient_prime":4513,"primitive_root":2,
        "source_family":"full_Reynolds_separate_phases",
        "logarithmic_dimension":95,"all_cusp_count":23,"residue_rank":22,
        "Hodge_dimension":73,"injective_jet_length":168,
        "basis_labels_sha256":digest(descriptors),
        "basis_jets_sha256":digest(integral_rows(J)),
        "all_23_residues_sha256":digest(residue_rows),
        "kernel_coordinates_sha256":digest(integral_rows(kernel)),
        "original_Hodge_jets_sha256":digest(integral_rows(hodge_jets)),
        "all_residues_include_width47":True,
        "integral_Hodge_lift":"Exact Z_4513 residue kernel using a unit22 minor; arbitrary integer representatives need not be holomorphic.",
    }
    if not fresh:
        for key in ("basis_labels_sha256","basis_jets_sha256","all_23_residues_sha256",
                    "kernel_coordinates_sha256","original_Hodge_jets_sha256"):
            if cert[key] != expected_certificate.get(key):
                raise ArithmeticError("Rebuilt original-source hash mismatch: "+key)
    note("Hodge_kernel_certificate",**cert)
    return {
        "complete":True,"K":K,"engine":engine,"descriptors":descriptors,
        "logarithmic_jets":J,"residues":residues,"kernel":kernel,
        "hodge_jets":hodge_jets,"certificate":cert,"used_rho":used_rho,
    }


def hecke_bridge(source, primes=(2,3,5), callback=None):
    """UNCALLED by the first request. For a separately reviewed public request.

    Return row-action matrices: T_n(omega_i)=sum_j M_n[i,j]*omega_j.
    The CM evaluation column transforms by M_n, with the same original basis.
    """
    ci_only()
    if not source.get("complete"):
        raise ValueError("A certified source is required.")
    if tuple(primes) != (2,3,5):
        raise ValueError("Only the explicitly proved finite bridge is implemented.")
    from sage.all import matrix
    engine, labels = source["engine"],source["descriptors"]
    kernel,H = source["kernel"],source["hodge_jets"]
    K, zeta = source["K"],2
    operators = {}
    for n in primes:
        # r=0,...,167; highest requested coefficient is n*167, at most835.
        high_root = pow(zeta,pow(n,-1,47),4513)
        low_root = pow(zeta,n,4513)
        high = kernel*engine.jets(labels,length=n*167+1,root=high_root)
        low = kernel*engine.jets(labels,length=168,root=low_root)
        images = matrix(K,73,168,
            lambda i,r: high[i,n*r]+(n*low[i,r//n] if r % n == 0 else 0))
        if any(images[i,0] != 0 for i in range(73)):
            raise ArithmeticError("The actual Hecke image has a nonzero cusp residue.")
        M = H.transpose().solve_right(images.transpose()).transpose()
        if M*H != images:
            raise ArithmeticError("Original finite-jet Hecke coordinate reconstruction failed.")
        operators[n] = M
        if callback is not None:
            callback("Hecke_bridge_prime",prime=n,
                     matrix_sha256=digest(integral_rows(M)))
    for a in primes:
        for b in primes:
            if operators[a]*operators[b] != operators[b]*operators[a]:
                raise ArithmeticError("Original Hecke operators do not commute.")
    H2 = operators[2]+2*operators[3]+4*operators[5]
    return {"operators":operators,"H2":H2,"convention":"row_action_on_differentials",
            "H2_sha256":digest(integral_rows(H2))}


def main():
    global STAGE,SOURCE,REQUEST_HASH
    ci_only()
    raw = REQUEST.read_bytes()
    REQUEST_HASH = hashlib.sha256(raw).hexdigest()
    if REQUEST_HASH != os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("Request pin mismatch.")
    req = json.loads(raw)
    for name,wanted in req["source_sha256"].items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest() != wanted:
            raise RuntimeError("Source pin mismatch: "+name)
    SOURCE = source_head()
    if (req["prime"] != 47 or req["coefficient_prime"] != 4513
            or req["root_of_unity"] != 2 or req["jet_length"] != 168
            or req["max_rho_batches"] != 64 or req["enable_Hecke_bridge"] is not False
            or req["total_seconds"] != 600 or req["reserve_seconds"] != 30
            or req["sage_version"] != "10.6"
            or req["execution_id"] != "full-p47-weight-one-Hodge-v1"):
        raise RuntimeError("Unexpected request.")
    signal.signal(signal.SIGALRM,stop)
    signal.setitimer(signal.ITIMER_REAL,max(0.1,570-(time.monotonic()-START)))
    emit("preflight",source=SOURCE,run=os.environ.get("GITHUB_RUN_ID"),
         attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),request_sha256=REQUEST_HASH,
         source_sha256=req["source_sha256"])

    def progress(kind,**data):
        global STAGE
        STAGE=kind
        if kind == "rank_progress":
            PROGRESS["last_complete_rank"]=data["exact_rank"]
            PROGRESS["rho_batches_completed"]=data["rho_batches_completed"]
        elif kind == "logarithmic_basis_certificate":
            PROGRESS["logarithmic_basis_certified"]=True
        elif kind == "Hodge_kernel_certificate":
            PROGRESS["Hodge_kernel_certified"]=True
        emit(kind,**data)

    source=build_source(max_rho_batches=64,callback=progress)
    signal.setitimer(signal.ITIMER_REAL,0)
    if not source["complete"]:
        STAGE="finite_prefix_exhausted"
        emit("receipt",status="complete_search_unresolved",source=SOURCE,
             run=os.environ.get("GITHUB_RUN_ID"),request_sha256=REQUEST_HASH,
             progress=PROGRESS,used_rho=source["used_rho"],
             scope="Only the prescribed finite prefix was tested; the whole-source method is not declared impossible.")
        return
    STAGE="completed"
    cert=source["certificate"]
    emit("receipt",status="complete",source=SOURCE,
         run=os.environ.get("GITHUB_RUN_ID"),request_sha256=REQUEST_HASH,
         progress=PROGRESS,certificate=cert,certificate_sha256=digest(cert),
         scope="Original rank95 logarithmic basis and ALL23-residue kernel73 only; no Hecke bridge, CM moment, MW saturation or rational-point uniqueness.")

if __name__ == "__main__":
    try:
        main()
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL,0)
        emit("receipt",status="incomplete",stage=STAGE,source=SOURCE,
             run=os.environ.get("GITHUB_RUN_ID"),request_sha256=REQUEST_HASH,
             exception_type=type(exc).__name__,message=str(exc),progress=PROGRESS,
             scope="Only explicitly completed stages survive; unfinished targets remain unresolved.")
        traceback.print_exc()
        sys.exit(1)
