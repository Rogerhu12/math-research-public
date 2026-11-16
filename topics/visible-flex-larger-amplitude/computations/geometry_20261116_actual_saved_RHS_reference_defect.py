#!/usr/bin/env python3
"""R596 actual saved RHS words versus the complete accurate finite DFT.

This optional observer uses the actual R575/R553 field, the original complete
checkpoint arrays and the same target return.  It evaluates all N reference
angles and all 3*M+2 coefficient rows with outward arithmetic.  It does not
run the floating FFT again, infer its internal rounding history, change a
solver/metric/DFS predicate, start an independent clock, or delete data.
Author: geometry agent (AI), 2026-11-16.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import comb
import os
from pathlib import Path
import struct
import sys
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
HERE = Path(__file__).resolve().parent
SCHEMA = "R596-actual-saved-RHS-complete-finite-DFT-and-cell-defect-v1"
PROJECTION_NAME = "geometry_20261116_same_evaluation_full_angle_projection_defect.py"
PROJECTION_SHA = "d2cfc1e35509486dd77f5f2ae4aecba3c0527b2e16b910be69540a73f3c2d6b7"
PROJECTION_SCHEMA = "R575-same-evaluation-complete-angle-projection-defect-v1"
CUBIC_NAME = "geometry_20261116_same_call_cubic_quintic_defect.py"
CUBIC_SHA = "6d27df22093e339fe8940bf24c57cff880d247a5f7f4fd478135adf2e4032f66"
CUBIC_SCHEMA = "R569-same-call-literal-cubic-and-accurate-quintic-v1"
CAPTURE_BRIDGE_NAME = "geometry_20261116_current_C_same_call_cubic_bridge.py"
CAPTURE_BRIDGE_SHA = "861a7d7b9125df75cc233627d664419183163080677b5b90c96905ca69490eeb"
CAPTURE_SCHEMA = "R570-actual-same-call-cubic-capture-and-comparison-v1"
FLOW_PINS = {
    "geometry_20261114_r225_free_core_bvp.py":
        "a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08",
    "geometry_20261114_full_dn_augmented.py":
        "f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e",
    "geometry_20261115_continuous_ten_fixed_power_augmented_v3.py":
        "a248e9577bf6f522b86c7c9b32d3fd51cc49dc9468760ef1d3e78e33062f9e0f",
    "geometry_20261114_full_dn_solve.py":
        "c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162",
}
DEADLINE_SCHEMAS = {
    "request193-owned-job-science-deadline-v1",
    "request203-owned-job-science-deadline-v1",
    "request205-owned-job-science-deadline-v1",
}
ORDINARY = (ArithmeticError, ValueError, TypeError, KeyError, IndexError,
            AttributeError, OSError)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
            "All actual reference arithmetic belongs to the named public Actions")


def encode(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(item) for item in value]
    return value


def canonical(value):
    return (json.dumps(encode(value), sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode("utf-8")


def value_identity(value):
    raw = canonical(value)
    return dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def identity(path):
    path = Path(path).resolve(strict=True)
    h, size = hashlib.sha256(), 0
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block); size += len(block)
    return dict(file=str(path), bytes=size, sha256=h.hexdigest())


def same(left, right):
    return (isinstance(left, dict) and isinstance(right, dict)
            and (left.get("bytes"), left.get("sha256"))
            == (right.get("bytes"), right.get("sha256")))


def error_record(error):
    return dict(type=type(error).__name__, message=str(error),
                traceback=traceback.format_exc())


def actual_module(obj, name, sha, class_name, schema):
    module = sys.modules.get(type(obj).__module__)
    require(module is not None and getattr(module, "__file__", None) is not None,
            "The actual defining class module is absent")
    row = identity(module.__file__)
    require(Path(row["file"]).parent == HERE
            and Path(row["file"]).name == name and row["sha256"] == sha
            and module.SCHEMA == schema
            and getattr(module, class_name, None) is type(obj),
            "Bind the actual loaded class and source, not a same-name module")
    return module, row


def load_cubic():
    path = HERE/CUBIC_NAME
    row = identity(path)
    require(row["sha256"] == CUBIC_SHA, "The actual original R569 source differs")
    tag = "_r596_same_call_cubic_"+CUBIC_SHA
    module = sys.modules.get(tag)
    if module is None:
        spec = importlib.util.spec_from_file_location(tag, path)
        require(spec is not None and spec.loader is not None,
                "The original same-call cubic loader is absent")
        module = importlib.util.module_from_spec(spec)
        sys.modules[tag] = module
        try:
            spec.loader.exec_module(module)
        except BaseException:
            sys.modules.pop(tag, None)
            raise
    require(Path(module.__file__).resolve() == path
            and module.SCHEMA == CUBIC_SCHEMA,
            "The actual cubic library source/schema differs")
    return module, row


def read_bound(path, expected):
    row = identity(path)
    require(same(row, expected), "The complete retained file bytes/SHA differ")
    return json.loads(Path(path).read_bytes()), row


def exact_word(raw):
    require(isinstance(raw, bytes) and len(raw) == 8,
            "Use one actual complete little-endian binary64 word")
    word = int.from_bytes(raw, "little")
    require(((word >> 52) & 2047) != 2047, "A saved defining word is nonfinite")
    # Fraction is an exact lift.  The original bytes, including signed zero,
    # remain separately bound; their signs are not encoded in Fraction zero.
    return Q.from_float(struct.unpack("<d", raw)[0])


def row_words(raw, index, width):
    start = index*width*8
    return tuple(raw[start+8*j:start+8*(j+1)] for j in range(width))


def polynomial_at(coefficients, x):
    result = Q(0)
    for value in reversed(coefficients):
        result = result*x+value
    return result


class BoundSavedRHSDefect:
    """Same actual source/target and original cell retirement; no new solver."""
    def __init__(self, reference_projection, *, original_job_deadline):
        actions()
        self.P, projection_source = actual_module(reference_projection,
            PROJECTION_NAME, PROJECTION_SHA, "BoundProjectionDefect", PROJECTION_SCHEMA)
        self.projection = reference_projection
        self.tubes, self.T = reference_projection.tubes, reference_projection.T
        self.current, self.field = reference_projection.current, reference_projection.field
        self.A, self.api = self.current.Active, reference_projection.api
        self.M, self.N = reference_projection.M, reference_projection.N
        self.n = 3*self.M+2
        self.sqrt_bits = reference_projection.sqrt_bits
        self.check = reference_projection.budget_check
        self.P.validate_reference_grid(self.M, self.N)
        self.check()
        self.cp = self.field.saved.checkpoint
        require(self.cp.k == 0 and self.field.M == self.M
                and self.field.saved.N == self.N,
                "Use the actual already loaded fully frozen complete field")
        root = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
        directory = Path(self.cp.directory).resolve(strict=True)
        require(directory != root and directory.is_relative_to(root),
                "Retain the actual checkpoint directory inside the original job")
        # The original profile original_json receipt has basename only.
        # Resolve from cp.directory, never from cwd and never by changing it.
        require(Path(self.cp.receipt["file"]).name == "checkpoint.json",
                "The original checkpoint descriptor must name checkpoint.json")
        path = directory/"checkpoint.json"
        require(path.is_file() and not path.is_symlink(),
                "The original actual checkpoint file is absent")
        manifest, manifest_receipt = read_bound(path, self.cp.receipt)
        require(manifest == self.cp.manifest
                and manifest.get("repository") == REPOSITORY
                and str(manifest.get("run_id")) == os.environ["GITHUB_RUN_ID"]
                and manifest.get("source_commit") == os.environ["GITHUB_SHA"],
                "The loaded field is not the same actual job's complete checkpoint")
        require(manifest["actual_physical_dimension"] == self.n
                and manifest["actual_core_dimension"] == self.M
                and manifest["actual_dimension"] == self.n+self.M
                and manifest["current_target_identity"] == self.cp.target_identity,
                "The complete current frozen dimensions or target differ")
        deadline, deadline_receipt = read_bound(original_job_deadline["file"],
                                                original_job_deadline)
        require(deadline.get("schema") in DEADLINE_SCHEMAS
                and deadline.get("repository") == REPOSITORY
                and str(deadline.get("run_id")) == os.environ["GITHUB_RUN_ID"]
                and deadline.get("source_commit") == os.environ["GITHUB_SHA"],
                "Keep the original current absolute deadline and source")
        self.raw, array_rows = self.bind_arrays()
        flow_rows = {}
        closure = manifest["actual_runtime_source_closure"]
        for name, digest in FLOW_PINS.items():
            self.check()
            row = identity(HERE/name)
            require(row["sha256"] == digest
                    and closure[name]["sha256"] == digest,
                    "The actual physical RHS producer source differs: "+name)
            flow_rows[name] = row
        self.cubic = None
        self.cubic_binding = dict(available=False, error=None,
            resolved_actual_checkpoint=manifest_receipt,
            directory_rule="actual cp.directory / checkpoint.json; never cwd",
            old_R570_comparison_object_or_receipt_not_modified=True)
        self.bind_capture(directory, deadline_receipt)
        self.binding = dict(schema=SCHEMA+"-binding", source=identity(__file__),
            actual_R575_source=projection_source,
            actual_R575_binding=reference_projection.describe(),
            actual_R553_binding=copy.deepcopy(self.tubes.binding),
            actual_checkpoint=manifest_receipt,
            original_checkpoint_descriptor=copy.deepcopy(self.cp.receipt),
            actual_current_driver=copy.deepcopy(manifest["actual_driver_source"]),
            actual_checkpoint_writer=copy.deepcopy(manifest["writer_source"]),
            actual_complete_array_words=array_rows,
            current_target_identity=copy.deepcopy(self.cp.target_identity),
            actual_full_675_expression=self.field.expression_identity(),
            actual_complete_ten_float64le=copy.deepcopy(manifest["complete_ten_float64le"]),
            actual_physical_RHS_sources=flow_rows,
            actual_job_deadline=deadline_receipt,
            actual_same_call_cubic=copy.deepcopy(self.cubic_binding),
            field_modes=self.M, angular_count=self.N,
            physical_size=self.n, augmented_size=self.n+self.M,
            physical_layout="r0..rM,t1..tM,z0..zM",
            finite_reference_sigma=1,
            sigma_reason="BatchedFFTFlow real normal/binormal path uses the positive square root",
            native_DtN_or_worker_root_sigma_not_inferred=True,
            physical_DY="actual final endpoint-control frozen physical RHS words",
            augmented_DU="actual full node-local-control augmented RHS words",
            fully_frozen_active_control_count=0,
            DY_and_DU_words_not_identified_or_overwritten=True,
            actual_scalar_target="A=a_true; mu=Ltrue/Lnumeric; nu=a_s*mu",
            formation_scope="total saved-word minus accurate finite-reference difference; includes numeric-shadow/scalar/chart differences",
            isolated_FFT_library_roundoff_bound_not_claimed=True,
            original_acceptance_or_DFS_predicates_changed=False,
            independent_clock_child_or_cleanup_created=False)
        self.observed = self.committed = self.split = self.terminal = 0
        self.paid_Q = self.paid_C = self.unpaid_count = 0
        self.retirement_errors = 0
        self.check()
        self.reconstruction = self.api.sqrt_bounds(Q(2*(self.M+1)**2+self.M*self.M),self.sqrt_bits)[1]
        self.max_Q = self.max_C = self.max_vector_Q = Q(0)
        self.node_best = {}
        self.unpaid = []
        self.last_observed = None
        self.inflight = None
        self.cache = []
        self.cache_hits = self.complete_reference_calls = 0

    def bind_arrays(self):
        np = self.field.saved._kernel.np
        arrays = self.cp.arrays
        nodes = len(self.field.x)
        self.nodes = nodes
        specs = (
            ("mesh", "mesh", (nodes,)),
            ("physical", "physical_states", (nodes,self.n)),
            ("physical_rhs", "physical_rhs", (nodes,self.n)),
            ("augmented", "augmented_states", (nodes,self.n+self.M)),
            ("augmented_rhs", "augmented_rhs", (nodes,self.n+self.M)),
            ("core", "core", (self.M,)),
        )
        payloads, records = {}, {}
        for key, original, shape in specs:
            self.check()
            value = np.asarray(arrays[key])
            require(value.shape == shape and value.dtype.kind == "f"
                    and value.dtype.itemsize == 8 and np.all(np.isfinite(value)),
                    "Keep every finite actual checkpoint array word: "+key)
            raw = np.asarray(value,dtype="<f8",order="C").tobytes(order="C")
            record = dict(shape=list(shape),dtype="<f8",
                          sha256=hashlib.sha256(raw).hexdigest())
            require(record == arrays["array_identity"][original]
                    and record == self.cp.manifest["complete_arrays"][original],
                    "The full retained defining array differs: "+key)
            payloads[key] = raw
            records[key] = dict(record,bytes=len(raw))
        for index in range(nodes):
            self.check()
            require(exact_word(row_words(payloads["mesh"],index,1)[0])
                    == self.field.x[index], "The exact physical mesh word differs")
            y = row_words(payloads["physical"],index,self.n)
            u = row_words(payloads["augmented"],index,self.n+self.M)
            require(y == u[:self.n], "Physical and augmented state words differ")
        for key, actual in (("physical",self.field.nodal[0]),
                            ("physical_rhs",self.field.nodal[1])):
            raw = np.asarray(actual,dtype="<f8",order="C").tobytes(order="C")
            require(raw == payloads[key], "The accurate Hermite uses different actual Y/DY words")
        return payloads, records

    def bind_capture(self, directory, deadline):
        """Actually bind the already retained same-call capsule from its directory."""
        try:
            self.check()
            bridge_source = identity(HERE/CAPTURE_BRIDGE_NAME)
            require(bridge_source["sha256"] == CAPTURE_BRIDGE_SHA,
                    "The actual capture writer source differs")
            status_path = directory.parent/"same-call-cubic-status.json"
            status_id = identity(status_path)
            status = json.loads(status_path.read_bytes())
            run = {key:os.environ.get(key) for key in
                   ("GITHUB_REPOSITORY","GITHUB_RUN_ID","GITHUB_RUN_ATTEMPT","GITHUB_SHA")}
            require(status.get("schema") == CAPTURE_SCHEMA+"-phase-capture"
                    and status.get("run") == run
                    and status.get("source_capture_available") is True
                    and same(status.get("source"),bridge_source)
                    and same(status.get("original_job_deadline"),deadline),
                    "The actual complete phase capture and original clock are unavailable")
            capture_path = directory.parent/"same-call-cubic"/"result.json"
            capture, capture_id = read_bound(capture_path,status["capture_result"])
            require(same(capture["source_scope"]["actual_clock"],deadline),
                    "The same-call capsule belongs to another original clock")
            module, source = load_cubic()
            actual = module.bind_loaded_cubic_quintic(self.current,
                capture_result=capture_path,capture_sha256=capture_id["sha256"],
                angular_count=self.N,sqrt_bits=self.sqrt_bits,budget_check=self.check)
            require(actual.dimension == self.n+self.M
                    and actual.payloads["recomputed_augmented_rhs"] == self.raw["augmented_rhs"],
                    "The captured complete DU differs from the actual checkpoint DU")
            self.cubic = actual
            self.cubic_binding.update(available=True, actual_status=status_id,
                actual_capture=capture_id, actual_library_source=source,
                actual_capture_writer_source=bridge_source,
                complete_actual_binding=actual.describe())
        except ORDINARY as error:
            self.cubic_binding["error"] = error_record(error)
            self.cubic_binding["unpaid_reason"] = "same_actual_cubic_capsule_binding_unpaid"

    def describe(self):
        return encode(copy.deepcopy(self.binding))

    def pair(self, value):
        return self.T.pair(value)

    def positive_divide(self, numerator, denominator):
        require(denominator[0] > 0, "The actual whole-grid denominator is not separated from zero")
        return self.T.mul(numerator,(1/denominator[1],1/denominator[0]))

    def reference_velocity(self, d, e, scalar):
        T = self.T
        a, nu, mu = scalar["A"], scalar["nu"], scalar["mu"]
        q = T.norm_squared(d)
        cross = T.cross(d,e)
        w = T.norm_squared(cross)
        p = T.sub(T.mul(T.mul(T.square(a),T.square(mu)),w),
                  T.mul(T.square(nu),T.mul(T.square(q),q)))
        domain = dict(d_squared=q,W=w,P=p,A=a,nu=nu,mu=mu)
        if a[0] <= 0 or mu[0] <= 0 or p[0] <= 0:
            return None,domain
        root = (self.api.sqrt_bounds(p[0],self.sqrt_bits)[0],
                self.api.sqrt_bounds(p[1],self.sqrt_bits)[1])
        dot = (Q(0),Q(0))
        for x,y in zip(d,e):
            dot = T.add(dot,T.mul(x,y))
        b = tuple(T.sub(T.mul(q,ek),T.mul(dot,dk)) for dk,ek in zip(d,e))
        den = T.mul(a,w)
        velocity = tuple(self.positive_divide(
            T.sub(T.mul(root,ck),T.mul(T.mul(nu,q),bk)),den)
            for ck,bk in zip(cross,b))
        return velocity,domain

    def finite_reference(self, coefficient_box, scalar, original_cell, role):
        """Outward complete finite DFT; incomplete sums never become a bound.

        The physical N-point reference is evaluated as a definition, not by
        replaying a floating FFT.  Arb accumulation avoids a growing exact
        common denominator while enclosing every exact rational/trigonometric
        term.  Every retained row and both mean rows receive all N terms.
        """
        self.check()
        T, A = self.T,self.A
        boxes = tuple(T.pair(row) for row in coefficient_box)
        scalar = {key:T.pair(scalar[key]) for key in ("A","nu","mu")}
        require(len(boxes) == self.n, "Use every physical coefficient in the complete DFT")
        key = (boxes,tuple((k,scalar[k]) for k in ("A","nu","mu")),
               self.M,self.N,self.sqrt_bits,int(A.ctx.prec))
        for saved_key,saved in self.cache:
            if saved_key == key:
                self.cache_hits += 1
                result = copy.deepcopy(saved)
                result["complete_exact_input_cache_reused"] = True
                result["complete_exact_input_cache_source_role"] = result["reference_role"]
                result["reference_role"] = role
                return result
        m,n = self.M,self.N
        coefficients = tuple(A.interval(*row) for row in boxes)
        sums = [A.arb(0) for _ in range(self.n)]
        min_p = min_w = None
        min_q = None
        argument = dict(coefficient_box=boxes,scalar=scalar,
            field_modes=m,angular_count=n,finite_reference_sigma=1,
            interval_bits=int(A.ctx.prec),sqrt_bits=self.sqrt_bits)
        record = dict(schema=SCHEMA+"-complete-finite-reference",
            argument_identity=value_identity(argument), reference_role=role,
            all_N_points_complete=False, coefficient_rows=None,
            complete_grid_points=0, completed_retained_rows=0,
            domain_minimum=None, unavailable=None, pending=None,
            complete_exact_input_cache_reused=False,
            original_floating_FFT_not_reexecuted=True,
            reference_rows_include_both_means=True)
        for ell in range(n):
            self.inflight = dict(operation="finite_DFT_reference",role=role,
                original_cell=copy.deepcopy(original_cell),
                grid_index=ell,grid_count=n,physical_q=str(Q(ell,n)),
                suboperation="full_physical_synthesis",next_frequency=1,
                completed_grid_prefix=[0,ell],
                unresolved_grid_suffix=[ell,n],
                complete_retained_row_count=self.n,
                partial_sums_not_a_complete_reference=True)
            self.check()
            phi = 2*A.arb.pi()*A.ball(Q(ell,n))
            d = [A.arb(0),coefficients[0],A.arb(0)]
            e = [-coefficients[0],A.arb(0),A.arb(0)]
            cosines,sines = [A.arb(1)],[A.arb(0)]
            for j in range(1,m+1):
                self.inflight["next_frequency"] = j
                self.check()
                frequency = 2*j
                co,si = (frequency*phi).cos(),(frequency*phi).sin()
                cosines.append(co);sines.append(si)
                r,t,z = coefficients[j],coefficients[m+j],coefficients[2*m+1+j]
                d[0] -= (frequency*r+t)*si
                d[1] += (frequency*t+r)*co
                d[2] -= frequency*z*si
                e[0] -= ((frequency*frequency+1)*r+2*frequency*t)*co
                e[1] -= ((frequency*frequency+1)*t+2*frequency*r)*si
                e[2] -= frequency*frequency*z*co
            dbox = tuple(T.pair(A.bounds(value)) for value in d)
            ebox = tuple(T.pair(A.bounds(value)) for value in e)
            self.inflight["suboperation"] = "actual_whole_box_Frenet_domain"
            self.check()
            velocity,domain = self.reference_velocity(dbox,ebox,scalar)
            if velocity is None:
                record["unavailable"] = dict(reason="complete_finite_grid_positive_domain_unpaid",
                    grid_index=ell,physical_q=Q(ell,n),
                    full_d_box=dbox,full_e_box=ebox,complete_domain=domain)
                record["pending"] = copy.deepcopy(self.inflight)
                return record
            min_p = domain["P"][0] if min_p is None else min(min_p,domain["P"][0])
            min_w = domain["W"][0] if min_w is None else min(min_w,domain["W"][0])
            min_q = domain["d_squared"][0] if min_q is None else min(min_q,domain["d_squared"][0])
            v = tuple(A.interval(*row) for row in velocity)
            self.inflight["suboperation"] = "all_retained_DFT_rows"
            for j in range(m+1):
                self.inflight["next_frequency"] = j
                self.check()
                sums[j] += v[0]*cosines[j]
                sums[2*m+1+j] += v[2]*cosines[j]
                if j:
                    sums[m+j] += v[1]*sines[j]
            record["complete_grid_points"] = ell+1
        rows = []
        self.inflight.update(suboperation="all_completed_DFT_row_bounds",
                             unresolved_grid_suffix=[n,n],next_coefficient=0)
        for column,total in enumerate(sums):
            self.inflight["next_coefficient"] = column
            self.check()
            weight = Q(1,n) if column in (0,2*m+1) else Q(2,n)
            rows.append(T.pair(A.bounds(total*A.ball(weight))))
        record.update(all_N_points_complete=True,
            coefficient_rows=tuple(rows),completed_retained_rows=self.n,
            complete_coefficient_rows_identity=value_identity(rows),
            domain_minimum=dict(P_lower=min_p,W_lower=min_w,d_squared_lower=min_q),
            pending=None,
            grid=dict(first=0,last=n-1,count=n,formula="phi_l=2*pi*l/N",
                duplicated_endpoint=False,largest_retained_frequency=2*m,
                both_means_retained=True,retained_Nyquist=False),
            convention="r_j,z_j cosine rows; t_j sine rows; means 1/N, all nonmeans 2/N",
            domain_scope="Every declared coefficient/scalar box member at every one of the N exact physical grid angles",
            continuous_between_grid_positive_domain_not_inferred=True)
        self.complete_reference_calls += 1
        # At most three complete exact-input records.  No digest-only key,
        # partial response or changed context precision is reused.
        self.cache.append((key,copy.deepcopy(record)))
        if len(self.cache)>3:
            del self.cache[0]
        return record

    def polynomial_data(self, cell, cubic_record):
        T = self.T
        self.inflight = dict(operation="bind_complete_actual_polynomials",
            original_cell=copy.deepcopy(cell),all_physical_columns_pending=True)
        self.check()
        piece = self.field.pieces[cell["piece_index"]]
        index = piece["prefix_span"]
        lo,hi = T.pair(cell["radial"])
        left,right = self.field.x[index],self.field.x[index+1]
        h = right-left
        require(left <= lo <= hi <= right and h>0,
                "Keep the actual closed cell inside its original complete polynomial span")
        unit = ((lo-left)/h,(hi-left)/h)
        qrows = tuple(tuple(T.exact(x) for x in row)
                      for row in self.field.prefix_coefficients(index))
        require(len(qrows)==self.n and all(len(row)==6 for row in qrows),
                "Keep all exact actual six-power coefficients")
        crows = None
        if (self.cubic is not None and isinstance(cubic_record,dict)
                and cubic_record.get("schema")==CUBIC_SCHEMA+"-cell"
                and cubic_record.get("original_cell")==cell
                and cubic_record.get("polynomial_comparison_available") is True):
            crows = self.cubic.cubic_coefficients(index)
            require(cubic_record["polynomial_comparison"]["actual_cubic_power_identity"]
                    ==value_identity(crows)
                    and cubic_record["polynomial_comparison"]["actual_quintic_power_identity"]
                    ==value_identity(qrows),
                    "The actual same-call complete polynomial owner differs")
        qbox,qfirst,cbox,cfirst = [],[],[],[]
        self.inflight = dict(operation="complete_actual_polynomial_ranges",
            original_cell=copy.deepcopy(cell),next_column=0,physical_size=self.n)
        for column,qrow in enumerate(qrows):
            self.inflight["next_column"] = column
            self.check()
            qbox.append(T.polynomial_range(qrow,*unit)[0])
            qfirst.append(T.polynomial_range(T.derivative(qrow,h),*unit)[0])
            if crows is not None:
                crow = crows[column]
                cbox.append(T.polynomial_range(crow,*unit)[0])
                cfirst.append(T.polynomial_range(T.derivative(crow,h),*unit)[0])
        pair_box = tuple((min(q[0],c[0]),max(q[1],c[1]))
                         for q,c in zip(qbox,cbox)) if crows is not None else tuple(qbox)
        if crows is not None:
            expected = tuple(T.pair(row) for row in
                cubic_record["polynomial_comparison"]["complete_curve_segment_coefficient_box"])
            require(pair_box==expected,"The actual complete Q/C_lit affine tube differs")
        return dict(span=index,left=left,right=right,length=h,radial=(lo,hi),unit=unit,
            quintic=qrows,cubic=crows,quintic_box=tuple(qbox),
            quintic_prime=tuple(qfirst),cubic_prime=tuple(cfirst),
            reference_box=pair_box,actual_pair=crows is not None)

    def residual_box(self, derivative_box, reference_rows):
        require(len(derivative_box)==len(reference_rows)==self.n,
                "A complete physical residual needs every original row")
        result = []
        self.inflight = dict(operation="all_physical_residual_rows",
            original_cell=copy.deepcopy(self.last_observed),next_column=0,physical_size=self.n)
        for column,(a,b) in enumerate(zip(derivative_box,reference_rows)):
            self.inflight["next_column"] = column
            self.check()
            result.append(self.T.sub(self.pair(a),self.pair(b)))
        result = tuple(result)
        maxima = tuple(self.T.absolute(row) for row in result)
        upper = max(maxima)
        column = maxima.index(upper)
        return dict(coefficient_infinity_upper=upper,
            actual_full_residual_box_identity=value_identity(result),
            complete_physical_size=self.n,maximum_column=column,
            maximum_column_interval=result[column],
            both_means_retained=True,
            complete_residual_boxes=result)

    def node_record(self, index, scalar, cell, polynomials):
        self.check()
        ywords = row_words(self.raw["physical"],index,self.n)
        dywords = row_words(self.raw["physical_rhs"],index,self.n)
        uwords = row_words(self.raw["augmented"],index,self.n+self.M)
        duwords = row_words(self.raw["augmented_rhs"],index,self.n+self.M)
        y = tuple(exact_word(word) for word in ywords)
        dy = tuple(exact_word(word) for word in dywords)
        du = tuple(exact_word(word) for word in duwords[:self.n])
        require(ywords==uwords[:self.n], "The actual original node words differ")
        row = dict(schema=SCHEMA+"-actual-node",node_index=index,
            original_mesh_float64le=row_words(self.raw["mesh"],index,1)[0].hex(),
            numeric_s=self.field.x[index],complete_physical_size=self.n,
            actual_Y_words_identity=dict(bytes=8*self.n,
                sha256=hashlib.sha256(b"".join(ywords)).hexdigest()),
            actual_frozen_DY_words_identity=dict(bytes=8*self.n,
                sha256=hashlib.sha256(b"".join(dywords)).hexdigest()),
            actual_augmented_DU_full_words_identity=dict(bytes=8*(self.n+self.M),
                sha256=hashlib.sha256(b"".join(duwords)).hexdigest()),
            original_active_controls_count=0,
            actual_node_active_control_words=[],
            actual_frozen_active_control_words=[],
            actual_fixed_ten_words=copy.deepcopy(self.cp.manifest["complete_ten_float64le"]),
            all_node_core_words_identity=dict(bytes=8*self.M,
                sha256=hashlib.sha256(b"".join(uwords[self.n:])).hexdigest()),
            full_augmented_constant_RHS_words_identity=dict(bytes=8*self.M,
                sha256=hashlib.sha256(b"".join(duwords[self.n:])).hexdigest()),
            frozen_DY_and_physical_DU_wordwise_equal=dywords==duwords[:self.n],
            exact_physical_DY_minus_DU_infinity=max(abs(a-b) for a,b in zip(dy,du)),
            actual_fixed_control_source="fullDN.frozen_physical_residual uses endpoint controls; full_rhs uses every actual nodal control",
            reference_applies_to_fixed_ten_and_numeric_s=True,
            formation_difference_available=False, literal_cubic_sample=None,
            no_floating_RHS_replay_performed=True)
        reference = self.finite_reference(tuple((value,value) for value in y),
            scalar,cell,"actual_saved_mesh_node_"+str(index))
        row["complete_reference"] = reference
        if reference["all_N_points_complete"] is not True:
            return row
        rows = reference["coefficient_rows"]
        frozen = self.residual_box(tuple((value,value) for value in dy),rows)
        augmented = self.residual_box(tuple((value,value) for value in du),rows)
        row.update(formation_difference_available=True,
            actual_frozen_DY_minus_accurate_finite_reference=frozen,
            actual_physical_DU_minus_same_frozen_reference=augmented,
            formation_scope="total exact saved output-word gap to the accurate finite N reference; includes scalar/chart/numerical-shadow differences",
            numerical_profile_jets_or_FFT_internal_roundoff_not_separately_certified=True)
        upper = frozen["coefficient_infinity_upper"]
        crows = polynomials["cubic"]
        if crows is not None:
            h = polynomials["length"]
            u = (self.field.x[index]-polynomials["left"])/h
            cv,cd = [],[]
            self.inflight = dict(operation="actual_node_literal_cubic_derivatives",
                original_cell=copy.deepcopy(cell),node_index=index,
                next_column=0,physical_size=self.n)
            for column,c in enumerate(crows):
                self.inflight["next_column"] = column
                self.check()
                cv.append(polynomial_at(c,u))
                cd.append(polynomial_at(self.T.derivative(c,h),u))
            cv,cd = tuple(cv),tuple(cd)
            require(all(lo<=value<=hi for value,(lo,hi) in
                        zip(y,polynomials["reference_box"])),
                    "The actual node is not in the declared full comparison tube")
            sample = dict(original_address=dict(original_cell=copy.deepcopy(cell),
                    actual_mesh_node_index=index,
                    actual_mesh_word=row["original_mesh_float64le"]),
                x=self.field.x[index],
                literal_residual_norm_upper=max(abs(a-b) for a,b in zip(cd,dy)),
                formation_error_upper=upper,
                state_gap_upper=max(abs(a-b) for a,b in zip(cv,y)),
                A_gap_upper=Q(0),nu_gap_upper=Q(0),mu_gap_upper=Q(0),
                zero_scalar_gaps_reason="reference and comparison use the identical accurate scalar function at this node, enclosed in the same original scalar box",
                literal_Cprime_minus_DY_evaluated_as_exact_rationals=True,
                complete_actual_cubic_value_identity=value_identity(cv),
                complete_actual_cubic_derivative_identity=value_identity(cd))
            row["literal_cubic_sample"] = sample
        return row

    def whole_pair_majorants(self, polynomials, scalar, reference):
        require(polynomials["actual_pair"]
                and reference["all_N_points_complete"] is True,
                "A complete same-call pair and all N legal grid boxes are required")
        self.inflight = dict(operation="whole_pair_finite_DFT_majorants",
            radial=polynomials["radial"],all_N_domain_points_already_complete=True)
        self.check()
        synthesis = self.api.fourier_synthesis_majorants(
            tuple(self.T.absolute(row) for row in polynomials["reference_box"]),
            self.M,self.N,self.sqrt_bits)
        domain = dict(A_lower=scalar["A"][0],A_upper=scalar["A"][1],
            mu_lower=scalar["mu"][0],mu_upper=scalar["mu"][1],
            nu_abs_upper=self.T.absolute(scalar["nu"]),
            P_lower=reference["domain_minimum"]["P_lower"],
            W_lower=reference["domain_minimum"]["W_lower"])
        self.check()
        result = self.api.finite_rhs_majorants(domain,synthesis,self.sqrt_bits)
        return dict(actual_R521_finite_rhs_majorants=result,
            actual_domain=domain,
            complete_pair_coefficient_box_identity=value_identity(polynomials["reference_box"]),
            domain_scope="entire independent state/scalar comparison tube at all N exact DFT angles",
            full_N_grid_is_all_relevant_angles_for_this_finite_operator=True,
            continuous_angle_positive_P_not_inferred=True)

    def sample_extension(self, polynomials, context, scalar, majorants, nodes):
        lo,hi = polynomials["radial"]
        if not lo<hi or polynomials["cubic"] is None:
            return dict(available=False,eta_C_upper=None,
                unpaid_reason="nonempty_actual_literal_cubic_cell_unavailable")
        h,left = polynomials["length"],polynomials["left"]
        crows = polynomials["cubic"]
        # Translate the actual local power rows to x-lo.  These are exact
        # polynomials of the retained binary64 words, never a refitted cubic.
        powers = []
        self.inflight = dict(operation="actual_literal_cubic_translation",
            radial=(lo,hi),power=0,next_column=0,physical_size=self.n)
        for k in range(4):
            translated = []
            for column,crow in enumerate(crows):
                self.inflight.update(power=k,next_column=column)
                self.check()
                translated.append(sum((crow[j]*Q(comb(j,k))*(lo-left)**(j-k)/h**j
                    for j in range(k,4)),Q(0)))
            powers.append(tuple(translated))
        powers = tuple(powers)
        cell = self.api.cubic_power_bounds(powers,lo,hi,self.M)
        second = self.pair(context["accurate_arc_second_derivative"])
        derivatives = dict(A=self.T.absolute(scalar["nu"]),
            nu=self.T.absolute(self.T.mul(second,self.T.square(scalar["mu"]))),
            mu=Q(0))
        samples = [row["literal_cubic_sample"] for row in nodes
                   if row.get("literal_cubic_sample") is not None]
        self.check()
        result = self.api.closed_cell_residual(
            majorants["actual_R521_finite_rhs_majorants"],cell,derivatives,samples)
        result["actual_literal_cubic_local_power_identity"] = value_identity(powers)
        result["exact_scalar_derivative_bounds"] = derivatives
        result["mu_derivative_zero_reason"] = "Ltrue/Lnumeric is constant in numeric s for each fixed C/root realization"
        result["point_samples_not_elevated_without_this_full_tube_and_fill_distance"] = True
        return result

    def inspect(self, cell, actual_tube_record):
        """Use the same original target return and already bound defining arrays."""
        self.check()
        piece = self.field.pieces[cell["piece_index"]]
        if piece["kind"]!="prefix":
            return None
        self.observed += 1
        self.last_observed = copy.deepcopy(cell)
        record = dict(schema=SCHEMA+"-cell",original_cell=copy.deepcopy(cell),
            actual_R553_return_identity=value_identity(actual_tube_record),
            actual_cubic_record=None,complete_reference=None,
            whole_quintic_finite_residual_available=False,
            whole_literal_cubic_finite_residual_available=False,
            direct_quintic_residual=None,direct_literal_cubic_residual=None,
            whole_pair_majorants=None,actual_R521_sample_extension=None,
            actual_R521_quintic_transfer=None,
            eta_Q_upper=None,eta_C_upper=None,
            actual_node_formation=[],pending=None,error=None,unpaid=[],
            reference_positive_sqrt_is_the_original_finite_physical_branch=True,
            not_a_new_BVP_native_FD_fullDN_metric_or_DFS_gate=True)
        try:
            require(isinstance(actual_tube_record,dict)
                    and actual_tube_record.get("schema")==self.T.SCHEMA+"-cell"
                    and actual_tube_record.get("original_cell")==cell,
                    "The actual same-cell R553 return is absent")
            scalar_record = actual_tube_record.get("scalar_box")
            require(isinstance(scalar_record,dict),
                    "The actual already returned scalar box is unavailable")
            context = scalar_record["actual_same_target_return"]
            require(context["schema"]==self.T.SCHEMA+"-same-target-return"
                    and self.pair(context["original_numeric_s_interval"])==self.pair(cell["radial"]),
                    "The actual accurate scalar return belongs to another radial cell")
            scalar = {key:self.pair(scalar_record[key]) for key in ("A","nu","mu")}
            require(scalar["A"][0]>0 and scalar["mu"][0]>0,
                    "The accurate scalar domain has not separated A and mu from zero")
            record["same_actual_scalar_return"] = copy.deepcopy(context)
            record["actual_scalar_box"] = scalar
            if self.cubic is not None:
                record["actual_cubic_record"] = self.cubic.cell(cell,context)
            else:
                record["unpaid"].append(dict(reason="same_actual_literal_cubic_not_bound",
                    detail=copy.deepcopy(self.cubic_binding)))
            polynomials = self.polynomial_data(cell,record["actual_cubic_record"])
            record["actual_polynomial_input"] = dict(prefix_span=polynomials["span"],
                full_span=(polynomials["left"],polynomials["right"]),
                actual_closed_radial=polynomials["radial"],
                actual_quintic_all_powers_identity=value_identity(polynomials["quintic"]),
                actual_cubic_all_powers_identity=(None if polynomials["cubic"] is None
                    else value_identity(polynomials["cubic"])),
                complete_reference_coefficient_box_identity=value_identity(polynomials["reference_box"]),
                reference_box_includes_actual_Q_and_literal_C=polynomials["actual_pair"],
                actual_Q_prime_box_identity=value_identity(polynomials["quintic_prime"]),
                actual_C_prime_box_identity=(None if polynomials["cubic"] is None
                    else value_identity(polynomials["cubic_prime"])))
            reference = self.finite_reference(polynomials["reference_box"],scalar,cell,
                "complete_actual_Q_C_lit_cell" if polynomials["actual_pair"]
                else "complete_actual_Q_cell_cubic_unavailable")
            record["complete_reference"] = reference
            if reference["all_N_points_complete"] is True:
                qr = self.residual_box(polynomials["quintic_prime"],reference["coefficient_rows"])
                record["direct_quintic_residual"] = qr
                record["eta_Q_upper"] = qr["coefficient_infinity_upper"]
                record["whole_quintic_finite_residual_available"] = True
                if polynomials["actual_pair"]:
                    cr = self.residual_box(polynomials["cubic_prime"],reference["coefficient_rows"])
                    record["direct_literal_cubic_residual"] = cr
                    record["eta_C_upper"] = cr["coefficient_infinity_upper"]
                    record["whole_literal_cubic_finite_residual_available"] = True
                    record["whole_pair_majorants"] = self.whole_pair_majorants(
                        polynomials,scalar,reference)
            else:
                record["unpaid"].append(dict(reason="whole_cell_complete_N_reference_unpaid",
                    actual_failure=copy.deepcopy(reference["unavailable"]),
                    pending=copy.deepcopy(reference["pending"])))
            lo,hi = polynomials["radial"]
            # An original prefix span has exactly these two mesh endpoints.
            # Nodes outside this subcell are not assigned its scalar/P boxes.
            for index in (polynomials["span"],polynomials["span"]+1):
                if lo<=self.field.x[index]<=hi:
                    row = self.node_record(index,scalar,cell,polynomials)
                    record["actual_node_formation"].append(row)
                    if row["formation_difference_available"] is not True:
                        record["unpaid"].append(dict(reason="actual_mesh_node_reference_unpaid",
                            node_index=index,actual_failure=copy.deepcopy(row["complete_reference"]["unavailable"]),
                            pending=copy.deepcopy(row["complete_reference"]["pending"])))
            if record["whole_pair_majorants"] is not None:
                extension = self.sample_extension(polynomials,context,scalar,
                    record["whole_pair_majorants"],record["actual_node_formation"])
                record["actual_R521_sample_extension"] = extension
                if extension.get("available") is True:
                    record["eta_C_upper"] = min(record["eta_C_upper"],
                                                self.T.exact(extension["eta_C_upper"]))
                cubic = record["actual_cubic_record"]["polynomial_comparison"]
                ky = record["whole_pair_majorants"]["actual_R521_finite_rhs_majorants"]["block_lipschitz"]["y"]
                transferred = self.api.quintic_residual_transfer(record["eta_C_upper"],
                    self.T.exact(cubic["E0_upper"]),self.T.exact(cubic["E1_upper"]),ky)
                record["actual_R521_quintic_transfer"] = dict(
                    eta_C_upper=record["eta_C_upper"],
                    actual_E0_upper=self.T.exact(cubic["E0_upper"]),
                    actual_E1_upper=self.T.exact(cubic["E1_upper"]),
                    actual_state_Lipschitz=ky,eta_Q_upper=transferred,
                    common_actual_full_pair_tube_and_same_scalars_used=True)
                record["eta_Q_upper"] = min(record["eta_Q_upper"],transferred)
            record["pending"] = None
            self.inflight = None
            return encode(record)
        except ORDINARY as error:
            record["error"] = error_record(error)
            record["pending"] = copy.deepcopy(self.inflight)
            record["unpaid"].append(dict(reason="actual_saved_RHS_observer_unpaid",
                                           detail=record["error"]))
            self.inflight = None
            return encode(record)

    def commit_original_retirement(self, cell, record, *, split):
        if self.field.pieces[cell["piece_index"]]["kind"]!="prefix":
            return None
        self.committed += 1
        if split:
            self.split += 1
            return dict(original_cell=copy.deepcopy(cell),original_split=True,
                complete_residual_responsibility_passed_to_original_children=True)
        self.terminal += 1
        self.check()
        valid = (isinstance(record,dict) and record.get("schema")==SCHEMA+"-cell"
                 and record.get("original_cell")==cell)
        qpaid = valid and record.get("whole_quintic_finite_residual_available") is True
        cpaid = valid and record.get("whole_literal_cubic_finite_residual_available") is True
        retirement_error = None
        try:
            if qpaid:
                bound = self.T.exact(record["eta_Q_upper"])
                require(bound>=0,"The actual finite Q defect upper bound is negative")
                self.max_Q=max(self.max_Q,bound)
                self.max_vector_Q=max(self.max_vector_Q,self.reconstruction*bound)
                self.paid_Q += 1
            if cpaid:
                bound = self.T.exact(record["eta_C_upper"])
                require(bound>=0,"The actual finite literal-C defect upper bound is negative")
                self.max_C=max(self.max_C,bound)
                self.paid_C += 1
            for row in (record.get("actual_node_formation",[]) if valid else []):
                if row.get("formation_difference_available") is not True:
                    continue
                index=row["node_index"]
                require(type(index) is int and 0<=index<self.nodes,
                        "A returned actual node address is invalid")
                upper=self.T.exact(row["actual_frozen_DY_minus_accurate_finite_reference"]["coefficient_infinity_upper"])
                require(upper>=0,"The actual saved-word defect bound is negative")
                old=self.node_best.get(index)
                if old is None or upper<old["upper"]:
                    self.node_best[index]=dict(upper=upper,original_cell=copy.deepcopy(cell),
                        full_node_record_identity=value_identity(row),
                        source_array="actual complete physical_rhs")
        except ORDINARY as error:
            qpaid=cpaid=False
            retirement_error=error_record(error)
            self.retirement_errors += 1
        unresolved = (not valid or not qpaid or not cpaid
                      or bool(record.get("unpaid")) or record.get("error") is not None)
        if unresolved:
            self.unpaid_count += 1
            row=dict(original_cell=copy.deepcopy(cell),
                quintic_finite_residual_paid=qpaid,literal_cubic_finite_residual_paid=cpaid,
                actual_return_identity=value_identity(record),
                complete_original_unpaid=(None if not valid else copy.deepcopy(record["unpaid"])),
                complete_original_error=(None if not valid else copy.deepcopy(record["error"])),
                actual_inflight_grid_scope=(None if not valid else copy.deepcopy(record["pending"])),
                retirement_error=retirement_error,
                full_completed_reference_rows_retained_in_original_cell_ledger=True)
            self.unpaid.append(row)
        return dict(original_cell=copy.deepcopy(cell),original_split=False,
            quintic_finite_residual_paid=qpaid,literal_cubic_finite_residual_paid=cpaid,
            eta_Q_upper=(record["eta_Q_upper"] if qpaid else None),
            eta_C_upper=(record["eta_C_upper"] if cpaid else None),
            retirement_error=retirement_error,
            no_metric_or_original_refinement_decision_changed=True)

    def summary(self, *, original_coverage, complete_cell_ledger, original_error,
                original_stop, close_errors, actual_projection_summary=None):
        counters=(self.observed==self.committed
            and self.observed==self.tubes.observed_prefix_cells
            and self.committed==self.tubes.committed_prefix_cells
            and self.split==self.tubes.split_prefix_cells
            and self.terminal==self.tubes.terminal_prefix_leaves)
        full=(original_coverage.get("completed_all_DFS_work") is True
            and complete_cell_ledger is not None and self.terminal>0 and counters
            and self.inflight is None and self.retirement_errors==0 and original_error is None
            and original_stop is None and not close_errors)
        qcomplete=full and self.paid_Q==self.terminal
        ccomplete=full and self.paid_C==self.terminal
        nodecomplete=full and set(self.node_best)==set(range(self.nodes))
        best_max=max((row["upper"] for row in self.node_best.values()),default=None)
        reconstruction=self.reconstruction
        projected_vector=(self.max_vector_Q if qcomplete else None)
        composed=None
        projection_error=None
        if actual_projection_summary is not None:
            try:
                row=actual_projection_summary
                require(row["schema"]==PROJECTION_SCHEMA+"-necessary"
                    and row["binding"]==self.projection.describe()
                    and same(row["complete_original_cell_ledger"],complete_cell_ledger),
                    "Use the actual same field/ledger R575 summary")
                if qcomplete and row["complete_prefix_physical_angle_projection_bound"] is True:
                    projection=row["global_prefix_exact_reference_projection_bound"]
                    require((projection["field_modes"],projection["angular_count"])==(self.M,self.N),
                            "The actual projection reference dimensions differ")
                    self.check()
                    gap=self.T.exact(projection["uniform_reconstructed_projection_defect_upper"])
                    require(gap>=0,"The actual complete projection bound is negative")
                    composed=dict(actual_R575_summary_identity=value_identity(row),
                        reconstructed_finite_ODE_residual_upper=projected_vector,
                        complete_continuous_projection_defect_upper=gap,
                        complete_prefix_unprojected_physical_RHS_defect_upper=projected_vector+gap,
                        finite_reference_sigma=1,
                        original_boundary_anchor_and_metric_transfer_still_required=True)
            except ORDINARY as error:
                projection_error=error_record(error)
        return encode(dict(schema=SCHEMA+"-necessary",binding=self.binding,
            observed_prefix_cells=self.observed,committed_prefix_cells=self.committed,
            split_prefix_cells=self.split,terminal_prefix_cells=self.terminal,
            original_R553_retirement_counters_match=counters,
            actual_retirement_error_count=self.retirement_errors,
            complete_original_closed_DFS_responsibility_paid=full,
            complete_terminal_Q_finite_residual_cells=self.paid_Q,
            complete_terminal_literal_C_finite_residual_cells=self.paid_C,
            complete_prefix_finite_quintic_residual=qcomplete,
            complete_prefix_finite_literal_cubic_residual=ccomplete,
            global_prefix_eta_Q_upper=self.max_Q if qcomplete else None,
            global_prefix_eta_C_upper=self.max_C if ccomplete else None,
            actual_mesh_node_count=self.nodes,
            retired_actual_mesh_nodes_with_complete_formation_bound=len(self.node_best),
            all_original_mesh_node_formation_bounds_complete=nodecomplete,
            global_actual_node_formation_upper=best_max if nodecomplete else None,
            actual_node_best_bound_records_identity=value_identity(self.node_best),
            observed_partial_extrema=dict(eta_Q_upper=self.max_Q,eta_C_upper=self.max_C,
                actual_node_formation_upper=best_max,
                not_global_without_the_corresponding_complete_flag=True),
            complete_reference_calls=self.complete_reference_calls,
            complete_exact_input_cache_hits=self.cache_hits,
            cache_scope="at most three complete exact-input records; no partial or digest-only key",
            all_unpaid_terminal_cells=copy.deepcopy(self.unpaid),
            unpaid_terminal_count=self.unpaid_count,
            actual_current_inflight_work=copy.deepcopy(self.inflight),
            last_observed_cell=copy.deepcopy(self.last_observed),
            complete_cell_ledger=copy.deepcopy(complete_cell_ledger),
            original_complete_coverage=copy.deepcopy(original_coverage),
            original_error=copy.deepcopy(original_error),original_stop=copy.deepcopy(original_stop),
            close_errors=copy.deepcopy(close_errors),
            complete_coefficient_to_vector_synthesis_norm_upper=reconstruction,
            global_reconstructed_finite_ODE_residual_upper=projected_vector,
            actual_continuous_projection_composition=composed,
            projection_summary_binding_error=projection_error,
            actual_same_call_cubic_binding=copy.deepcopy(self.cubic_binding),
            all_reference_rows_node_words_and_actual_polynomials_remain_in_original_temporary_sources_and_cell_ledger=True,
            summary_does_not_claim_all_ledger_rows_transported=True,
            current_and_unvisited_DFS_cells_remain_original_coverage=True,
            scope=dict(
                finite_DFT_full_N_positive_domain_is_separate_from_R553_single_angle_leaf=True,
                whole_cell_bounds_use_actual_polynomials_not_only_mesh_samples=True,
                scalar_and_chart_difference_included_in_total_saved_RHS_gap=True,
                isolated_numpy_FFT_roundoff_or_internal_table_error_not_inferred=True,
                source_control_layout_distinguished_even_when_current_k_is_zero=True,
                reflected_sheet_and_exact_phase_use_transported_base_defect=True,
                fixed_N_projection_not_claimed_to_commute_with_arbitrary_phase_shift=True,
                new_independent_full_angle_reference_evaluation_uses_original_budget_callback=True,
                tail_collar_cut_patch_cap_RHS_reference_unpaid=True,
                original_boundary_anchor_and_full_relative_metric_floor_unpaid=True,
                original_native_worker_root_choice_not_identified_by_FFT_positive_sqrt=True,
                original_BVP_native_FD_fullDN_metric_DFS_acceptance_changed=False,
                new_owned_child_clock_cleanup_or_public_run_started=False)))


def bind_loaded_saved_RHS_defect(reference_projection, *, original_job_deadline):
    """Bind the real R575 object and retained source arrays; no invented inputs."""
    return BoundSavedRHSDefect(reference_projection,
                              original_job_deadline=original_job_deadline)
