"""Save full unaccepted nodal state immediately before original J assembly.

The wrapper is around prepare_sys's full collocation Jacobian, not around the
RHS Jacobian which also receives midpoint batches.  Each immutable checkpoint
contains the current complete adaptive x, y, p and original parameter scales.
It is only a restart initializer.  All numerical returns are unchanged.
"""
import hashlib
import inspect
import json
from pathlib import Path
import time
import numpy as np
from scipy.integrate import _bvp


def install(outdir, pscale, source_hashes):
    outdir = Path(outdir)
    pscale = np.asarray(pscale, dtype=float).copy()
    original = _bvp.prepare_sys
    wanted = ["n", "m", "k", "fun", "bc", "fun_jac", "bc_jac", "x", "h"]
    if list(inspect.signature(original).parameters) != wanted:
        raise ValueError("The original complete collocation assembler signature changed")
    stats = dict(checkpoints=0, seconds=0., midpoint_batches_never_saved=True,
                 original_prepare_sys_sha256=hashlib.sha256(
                     inspect.getsource(original).encode()).hexdigest())

    def prepare(n, m, k, fun, bc, fun_jac, bc_jac, x, h):
        col_fun, sys_jac = original(n, m, k, fun, bc, fun_jac, bc_jac, x, h)
        full_x = np.asarray(x, dtype=float).copy()
        if len(full_x) != m or pscale.shape != (k-1,):
            raise ValueError("Complete nodal checkpoint dimensions differ")

        def checkpointed(y, p, y_middle, f, f_middle, bc0):
            if y.shape != (n, m) or p.shape != (k,):
                raise ValueError("A midpoint batch reached the full nodal checkpoint")
            begin = time.monotonic()
            count = stats["checkpoints"]+1
            name = "unaccepted-nodal-before-jac-%04d.npz" % count
            path = outdir/name
            temporary = path.with_suffix(".npz.tmp")
            if path.exists():
                raise FileExistsError(path)
            with temporary.open("xb") as stream:
                np.savez(stream, x=full_x, y=y, p=p, pscale=pscale)
            temporary.replace(path)
            row = dict(kind="unaccepted_complete_nodal_restart", file=name,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                nodes=m, state_components=n, parameters=k,
                mesh_min_spacing=float(np.min(np.diff(full_x))),
                before_full_J_assembly=True, accepted_bvp=False,
                original_source_hashes=source_hashes,
                checkpoint_ordinal=count)
            with (outdir/"nodal-checkpoints.jsonl").open("a") as stream:
                stream.write(json.dumps(row, allow_nan=False)+"\n")
            pointer = outdir/"latest-unaccepted-nodal-checkpoint.json"
            pointer_tmp = pointer.with_suffix(".tmp")
            pointer_tmp.write_text(json.dumps(row, indent=2, allow_nan=False)+"\n")
            pointer_tmp.replace(pointer)
            stats["checkpoints"] = count
            stats["seconds"] += time.monotonic()-begin
            return sys_jac(y, p, y_middle, f, f_middle, bc0)

        return col_fun, checkpointed

    _bvp.prepare_sys = prepare

    def restore():
        _bvp.prepare_sys = original

    return stats, restore
