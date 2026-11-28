"""Finite-phase R732 disk continuation. Public Actions entry. Every paid array is resumable."""
import argparse
import hashlib
import json
import os
import platform
import tempfile
import time
import traceback
from collections import Counter
from pathlib import Path

import numpy as np
import scipy
from scipy.interpolate import RectBivariateSpline

from r688_actual_r664_window_collars import require_public
from r732_closed_ring import Line, Ring
from r732_compensated_pulses import Pulse
from r732_disk_fields import Frame
from r732_physical_disk import Build, Profile


PHASES = (0., .02, .08, .20, .40, .65, .85, 1.)
DEGREES = (3, 5)
HERE = Path(__file__).resolve().parent
TYPES = {cls.__name__: cls for cls in (Pulse, Line, Ring, Frame, Profile, Build, RectBivariateSpline)}
FILES = ("r732_disk_solver.py", "r732_disk_qualification.py", "r732_disk_fields.py",
         "r732_physical_disk.py", "r732_closed_ring.py", "r732_compensated_pulses.py",
         "r688_actual_r664_window_collars.py", "r688_true_caps_and_reference_sections.py")
OPTIONS = dict(baseline=.100, modes=8192, steps=12, order=48)
FIT_TOL = 1.e-7


def plain(data):
    return json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(b):
    return hashlib.sha256(b).hexdigest()


def array_id(a):
    a = np.ascontiguousarray(a)
    return dict(shape=list(a.shape), dtype=a.dtype.str, sha256=digest(a.tobytes()))


def write_json(path, obj):
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(plain(obj) + "\n", encoding="utf-8")
    os.replace(tmp, path)


class ClockStop(Exception):
    pass


class Pack:
    """Numerical arrays plus whitelisted data-only objects. Loading never unpickles."""
    def __init__(self):
        self.arrays = {}

    def encode(self, v):
        if isinstance(v, np.ndarray):
            if v.dtype.hasobject:
                raise TypeError("object array in paid state")
            key = f"a{len(self.arrays)}"
            self.arrays[key] = v
            return ["array", key]
        if isinstance(v, np.generic):
            return self.encode(v.item())
        if isinstance(v, float) and not np.isfinite(v):
            return ["nonfinite", v.hex()]
        if isinstance(v, (type(None), bool, str, int, float)):
            return ["scalar", v]
        if isinstance(v, (list, tuple)):
            return ["tuple" if isinstance(v, tuple) else "list", [self.encode(x) for x in v]]
        if isinstance(v, dict):
            return ["dict", [[self.encode(k), self.encode(x)] for k, x in v.items()]]
        if type(v).__name__ in TYPES and type(v) is TYPES[type(v).__name__]:
            return ["instance", type(v).__name__, self.encode(vars(v))]
        raise TypeError("unsupported paid state type " + str(type(v)))

    @staticmethod
    def decode(item, arrays):
        tag, arg = item[:2]
        if tag == "nonfinite":
            return float.fromhex(arg)
        if tag == "scalar":
            return arg
        if tag == "array":
            return arrays[arg]
        if tag in ("tuple", "list"):
            seq = [Pack.decode(z, arrays) for z in arg]
            return tuple(seq) if tag == "tuple" else seq
        if tag == "dict":
            return {Pack.decode(k, arrays): Pack.decode(v, arrays) for k, v in arg}
        if tag == "instance" and arg in TYPES:
            obj = TYPES[arg].__new__(TYPES[arg])
            vars(obj).update(Pack.decode(item[2], arrays))
            return obj
        raise ValueError("invalid paid state node")


class Paid:
    def __init__(self, directory, seconds, settings):
        self.start = time.monotonic()
        self.end = self.start + seconds
        self.deadline = self.end - min(.12*seconds,240.)
        self.root = Path(directory)
        self.root.mkdir(parents=True, exist_ok=True)
        self.data = self.root / "paid"
        self.data.mkdir(exist_ok=True)
        self.run = os.environ["GITHUB_RUN_ID"] + "-" + os.environ.get("GITHUB_RUN_ATTEMPT", "1")
        hashes = {p: digest((HERE/p).read_bytes()) for p in FILES}
        identity = dict(sha256=hashes, build=OPTIONS, settings=settings, phases=PHASES, degrees=DEGREES,
                        python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__)
        path = self.root/"input-identity.json"
        if path.exists() and plain(json.loads(path.read_text())) != plain(identity):
            raise ValueError("paid archive has another physical input, solver, library version or schedule")
        write_json(path, identity)
        self.identity = digest(plain(identity).encode())
        self.now = Counter()
        self.io = 0.
        self.current = None

    def guard(self):
        if time.monotonic() >= self.deadline:
            raise ClockStop("next unpaid scientific operation deferred at the requested wall clock")

    def append(self, filename, value):
        with (self.root/filename).open("a", encoding="utf-8") as f:
            f.write(plain(value) + "\n")

    def filename(self, kind, key):
        semantic = [self.identity, kind, key]
        return self.data/(kind + "-" + digest(plain(semantic).encode()) + ".npz")

    def get(self, kind, key, compute):
        semantic = [self.identity, kind, key]
        path = self.filename(kind,key)
        if path.exists():
            t = time.monotonic()
            with np.load(path, allow_pickle=False) as d:
                header = json.loads(d["meta"].tobytes())
                if header["semantic"] != json.loads(plain(semantic)):
                    raise ValueError("paid record label mismatch")
                value = Pack.decode(header["tree"], d)
            self.io += time.monotonic() - t
            self.now["reused_" + kind] += 1
            return value
        self.current = dict(kind=kind, key=key, run=self.run)
        self.guard()
        self.now["started_" + kind] += 1
        self.append("cost.jsonl", {**self.current, "event": "start"})
        t = time.monotonic()
        try:
            value = compute()
        except Exception as exc:
            self.append("cost.jsonl", {**self.current, "event": "failed",
                        "error": repr(exc), "scientific_seconds": time.monotonic()-t})
            raise
        elapsed = time.monotonic() - t
        t = time.monotonic()
        pack = Pack()
        tree = pack.encode(value)
        meta = plain(dict(semantic=semantic, tree=tree)).encode()
        with tempfile.NamedTemporaryFile(dir=self.data, delete=False, suffix=".npz") as f:
            name = f.name
            try:
                np.savez_compressed(f, meta=np.frombuffer(meta, dtype=np.uint8), **pack.arrays)
            except BaseException:
                f.close()
                os.unlink(name)
                raise
        os.replace(name, path)
        io = time.monotonic()-t
        self.io += io
        self.now["finished_" + kind] += 1
        self.append("cost.jsonl", {**self.current, "event": "saved", "file": path.name,
                                   "bytes": path.stat().st_size, "scientific_seconds": elapsed,
                                   "archive_seconds": io})
        self.current = None
        return value


def uplift(q, old, new):
    terms = [(i,j) for i in range(old+1) for j in range(old+1-i)]
    by_term = dict(zip(terms, np.asarray(q).reshape(-1,3), strict=True))
    return np.array([by_term.get((i,j), np.zeros(3))
                     for i in range(new+1) for j in range(new+1-i)]).reshape(-1)


def metrics(curl, frame):
    a = np.asarray(curl)
    if a.shape != frame.shape + (3,) or not np.isfinite(a).all() or not frame.source_min > 0:
        raise ValueError("incomplete curl or singular source chart on actual nodes")
    a = a.reshape(-1,3)
    row = np.einsum("ij,ij->i", a, a)
    i = int(np.argmax(row))
    norm = float(np.sqrt(row[i]))
    return dict(max=norm, rms=float(np.sqrt(np.mean(row))), by_axis=np.abs(a).max(axis=0).tolist(),
                max_r=float(frame.r[i]), max_s=float(frame.s[i]), at_peak=a[i].tolist(),
                source_min=frame.source_min, relative_peak=norm/frame.source_min, rows=len(a),
                array=array_id(curl))


def summarize(x):
    if isinstance(x, np.ndarray):
        return array_id(x)
    if isinstance(x, np.generic):
        return summarize(x.item())
    if isinstance(x, dict):
        return {str(k): summarize(v) for k,v in x.items()}
    if isinstance(x, (list,tuple)):
        if len(x)>16:
            return dict(count=len(x), json_sha256=digest(plain([summarize(v) for v in x]).encode()))
        return [summarize(v) for v in x]
    if isinstance(x, float) and not np.isfinite(x):
        return str(x)
    return x


class Continuation:
    def __init__(self, paid, level, iterations):
        self.p = paid
        self.level = level
        self.iterations = iterations
        self.build = paid.get("source_build", [], lambda: Build(**OPTIONS))
        self.frames = {}
        self.source_id = self.build.seed_identity
        self.path = paid.root/"continuation.json"
        self.s = json.loads(self.path.read_text()) if self.path.exists() else dict(
            phase_index=0, degree=DEGREES[0], iteration=0, damping=.02, accepted=0,
            q=[0.]*(3*(DEGREES[0]+1)*(DEGREES[0]+2)//2), line=0, records=[],
            last_fit_phase=None)
        write_json(paid.root/"source-identity.json", self.source_id)

    def put(self):
        write_json(self.path, self.s)

    def setup(self, phase, degree):
        if phase not in self.build.rings:
            self.build.rings[phase] = self.p.get("phase_ring", [phase], lambda: self.build.target(phase))
        if phase not in self.build.pulse_cache:
            self.build.pulse_cache[phase] = self.p.get(
                "phase_pulses", [phase], lambda: self.build.pulses(phase))
        if self.frames.get("id") == (phase,degree):
            return self.frames
        self.frames = {"id": (phase,degree)}
        for purpose, level in (("train",self.level),("validation",self.level+1)):
            r,s = self.p.get("native_nodes", [purpose,level], lambda: self.build.nodes(level,purpose))
            key = [phase,degree,purpose,level,array_id(r),array_id(s)]
            self.frames[purpose] = self.p.get(
                "native_frame", key, lambda: Frame(self.build, phase, r[:,None], s[None,:], degree))
        return self.frames

    def field(self, phase, degree, purpose, q, frame):
        key = [phase,degree,purpose,self.level,array_id(q)]
        return self.p.get("curl", key, lambda: frame.curl(q))

    def operator(self, phase, degree, q, frame, residual):
        basekey = [phase,degree,self.level,array_id(q)]
        if self.p.filename("factor",basekey).is_file():
            return self.p.get("factor",basekey,None)
        n = frame.ncols
        chunks = []
        for first in range(0,n,4):
            last = min(n,first+4)
            def evaluate():
                # The exact complex-step evaluation and ordering in Frame.jac.
                ans = np.empty((residual.size,last-first))
                for j in range(first,last):
                    z = np.array(q, dtype=complex)
                    z[j] += 1.e-24j
                    ans[:,j-first] = frame.curl(z).imag.ravel()/1.e-24
                if not np.isfinite(ans).all():
                    raise ArithmeticError("nonfinite physical derivative")
                return ans
            chunks.append(self.p.get("jac_columns", basekey+[first,last], evaluate))
        def factor():
            J = np.column_stack(chunks)
            flat = residual.ravel()
            U,s,Vt = np.linalg.svd(J/np.sqrt(len(flat)//3), full_matrices=False)
            return dict(s=s, Vt=Vt, projected=(U.T@flat)/np.sqrt(len(flat)//3), raw=array_id(J))
        return self.p.get("factor", basekey, factor)

    def qualify(self, phase, degree, q):
        from r732_disk_qualification import qualify
        key = [phase,degree,array_id(q)]
        result = self.p.get("qualification", key, lambda: qualify(
            self.build,phase,q,degree,level=self.level,outdir=self.p.root/"physical"))
        local = self.p.root/"physical"/Path(result["physical_archive"]).name
        if not local.is_file() or digest(local.read_bytes()) != result["archive_sha256"]:
            raise ValueError("physical qualification points to missing or mismatched paid jet archive")
        return result

    def run(self):
        s = self.s
        while s["phase_index"] < len(PHASES):
            phase = PHASES[s["phase_index"]]
            degree = s["degree"]
            q = np.asarray(s["q"], dtype=float)
            frames = self.setup(phase,degree)
            work = self.field(phase,degree,"train",q,frames["train"])
            fine = self.field(phase,degree,"validation",q,frames["validation"])
            m, v = metrics(work,frames["train"]), metrics(fine,frames["validation"])
            fitted = max(m["relative_peak"],v["relative_peak"]) <= FIT_TOL
            # Preserve the true source and the most recent best state's independent
            # field even when this clock cannot afford its next numerical operation.
            s["current"] = dict(phase=phase,degree=degree,q=array_id(q),train=m,validation=v,
                                finite_fit=fitted,iteration=s["iteration"])
            s["current_q"] = q.tolist()
            self.put()
            exhausted = s["iteration"] >= self.iterations
            # At least one complete 3-axis operator at each attained phase/degree,
            # including the actual source. Blocks are restartable at the next column.
            op = self.operator(phase,degree,q,frames["train"],work)
            singular = op["s"]
            s["current"]["operator"] = dict(raw=op["raw"],singular=singular.tolist(),
                                             spectral_rank=int(np.sum(singular>singular[0]*1.e-12)))
            self.put()
            if fitted or exhausted:
                if exhausted and not fitted and degree < DEGREES[-1]:
                    s.update(q=uplift(q,degree,DEGREES[-1]).tolist(),degree=DEGREES[-1],
                             iteration=0,damping=.02,line=0)
                    self.put()
                    continue
                full = self.qualify(phase,degree,q)
                record = {**s["current"], "q_values": q.tolist(),
                          "physical_qualification": summarize(full)}
                s["records"].append(record)
                if fitted:
                    s["last_fit_phase"] = phase
                s.update(phase_index=s["phase_index"]+1,iteration=0,line=0,damping=.02)
                self.put()
                print("R732_PHASE", plain({k:record[k] for k in
                      ("phase","degree","q","train","validation","finite_fit")}),flush=True)
                continue
            ref = max(float(singular[0]), 1.e-14)
            mu = (s["damping"]*ref)**2
            dx = -(op["Vt"].T @ ((singular/(singular**2+mu))*op["projected"]))
            size = float(np.linalg.norm(dx))
            dx *= min(1., .7/max(size,1.e-300))
            accepted = False
            for backtrack in range(s["line"],8):
                test = q + (2.**(-backtrack))*dx
                trial = self.field(phase,degree,"train",test,frames["train"])
                mt = metrics(trial,frames["train"])
                checked = None
                if mt["rms"] < m["rms"] and not np.array_equal(test,q):
                    checked = metrics(self.field(phase,degree,"validation",test,frames["validation"]),
                                      frames["validation"])
                    accepted = checked["rms"] <= v["rms"] and checked["max"] <= v["max"]*(1+1.e-8)
                self.p.append("trials.jsonl", dict(run=self.p.run,phase=phase,degree=degree,
                              iteration=s["iteration"],q=array_id(q),trial=test.tolist(),
                              damping=s["damping"],backtrack=backtrack,accepted=accepted,
                              train=mt,validation=checked))
                s["line"] = backtrack+1
                if accepted:
                    s["current"] = dict(phase=phase,degree=degree,q=array_id(test),train=mt,
                                        validation=checked,finite_fit=max(mt["relative_peak"],
                                        checked["relative_peak"]) <= FIT_TOL, iteration=s["iteration"]+1)
                    s["current_q"] = test.tolist()
                    s.update(q=test.tolist(),accepted=s["accepted"]+1,line=0,
                             iteration=s["iteration"]+1,damping=max(1.e-6,.65*s["damping"]))
                    self.put()
                    break
                self.put()
            if not accepted:
                s.update(iteration=s["iteration"]+1,line=0,damping=min(100.,4*s["damping"]))
                self.put()
        return "finished_finite_pose_schedule"


def cost_summary(root):
    out = {}
    path = root/"cost.jsonl"
    if not path.exists():
        return out
    operators = {}
    for line in path.read_text().splitlines():
        z = json.loads(line)
        t = out.setdefault(z["kind"],dict(started=0,saved=0,failed=0,science_seconds=0.,
                                          archive_seconds=0.,bytes=0))
        event = z["event"]
        t[{"start":"started","saved":"saved","failed":"failed"}[event]] += 1
        t["science_seconds"] += z.get("scientific_seconds",0.)
        t["archive_seconds"] += z.get("archive_seconds",0.)
        t["bytes"] += z.get("bytes",0)
        if event == "saved" and z["kind"] == "jac_columns":
            phase,degree,level,q,first,last = z["key"]
            op = operators.setdefault((phase,degree,level,q["sha256"]),
                                      dict(ncols=3*(degree+1)*(degree+2)//2,columns=set()))
            op["columns"].update(range(first,last))
    out["actual_original_cartesian_jacobians"] = dict(
        complete=sum(len(z["columns"]) == z["ncols"] for z in operators.values()),
        partial=sum(len(z["columns"]) != z["ncols"] for z in operators.values()),
        paid_complex_step_columns=sum(len(z["columns"]) for z in operators.values()))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--state", default="r732-paid-state")
    ap.add_argument("--seconds", type=float, default=2400.)
    ap.add_argument("--level", type=int, default=1)
    ap.add_argument("--iterations", type=int, default=5)
    args = ap.parse_args()
    require_public()
    if not 0 < args.seconds <= 3200 or not 1 <= args.level <= 6 or not 1 <= args.iterations <= 30:
        raise ValueError("invalid per-allocation clock, native grid level or iteration count")
    paid = Paid(args.state,args.seconds,dict(level=args.level,iterations=args.iterations))
    state, error, trace = None, None, None
    try:
        state = Continuation(paid,args.level,args.iterations)
        reason = state.run()
    except ClockStop as exc:
        reason = str(exc)
    except Exception as exc:
        reason,error,trace = "scientific_or_io_failure",repr(exc),traceback.format_exc()
    s = state.s if state is not None else {}
    deferred = paid.current
    terminal_physical, terminal_error = None, None
    if state is not None and reason.startswith("next unpaid") and "current" in s:
        now = s["current"]
        q = np.asarray(s["q"], dtype=float)
        # A newly requested pose or larger degree may still have no independent
        # fields. Select the actual q of the latest paid two-grid point.
        if now["q"] != array_id(q):
            q = np.asarray(s["current_q"], dtype=float)
        if now["q"] == array_id(q):
            paid.deadline = paid.end
            try:
                terminal_physical = summarize(state.qualify(now["phase"],now["degree"],q))
            except Exception as exc:
                terminal_error = repr(exc)
    cost = cost_summary(paid.root)
    out = dict(reason=reason,error=error,trace=trace,run=paid.run,input_identity=paid.identity,
               seed_identity=None if state is None else state.source_id,
               schedule=list(PHASES),latest_individually_fitted_phase=s.get("last_fit_phase"),
               finished_phase_records=len(s.get("records",[])),phase_index=s.get("phase_index"),
               retained_paired_field=s.get("current"),retained_q_values=s.get("current_q"),
               warm_q_for_next_operation=s.get("q"),accepted=s.get("accepted",0),
               completed_pose_index=[
                   dict(phase=a["phase"],degree=a["degree"],q=a["q"],fitted=a["finite_fit"],
                        training_peak=a["train"]["max"],validation_peak=a["validation"]["max"],
                        physical={k:a["physical_qualification"].get(k) for k in
                                  ("disk_metric_max","disk_curvature_max","disk_cartesian_curl_max",
                                   "given_far_seat_z","max_source_to_phase_union_diameter_sample",
                                   "archive_sha256","full_shell_qualification")})
                   for a in s.get("records",[])],
               next_iteration=s.get("iteration"),next_backtrack=s.get("line"),
               active_operation=deferred,all_archived_cost=cost,
               terminal_physical=terminal_physical,terminal_physical_error=terminal_error,
               this_allocation_counts=dict(paid.now),this_allocation_archive_seconds=paid.io,
               this_allocation_wall_seconds=time.monotonic()-paid.start,
               certified_all_phase_or_global_reach=False)
    write_json(paid.root/"terminal.json",out)
    print("R732_DISK_FINAL",plain(out),flush=True)
    if error:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
