"""Restore a genuine full design checkpoint literally before the original RHS.

The old portable restart may round-trip support scales and apply its inlet
correction again. A current-equation nodal checkpoint has already undergone
that preparation. Only this explicitly requested unaccepted restart bypasses
those repeated representation operations; the full original RHS, domain,
boundary, Newton, RMS, metric audit and acceptance tests still run.
"""
import hashlib
import inspect
import json
import linecache
from pathlib import Path
import numpy as np


def install(loader_module, checkpoint, outdir):
    checkpoint, outdir = Path(checkpoint).resolve(), Path(outdir).resolve()
    sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
    bound_sha = sha(checkpoint)
    original_loader = loader_module.load_module
    portable = Path(__file__).resolve().parents[2]/"resume_m3/portable_prefix_continue.py"

    def load(name, filename):
        module = original_loader(name, filename)
        if Path(filename).resolve() != portable:
            return module
        before = inspect.getsource(module.main)
        marker = '        rhs = o.fun(x,y,par)'
        if before.count(marker) != 1:
            raise ValueError('The original full nodal entry location changed')

        def restore_nodal(obj, x, y, p):
            if sha(checkpoint) != bound_sha:
                raise ValueError('The saved unaccepted full nodal checkpoint changed')
            with np.load(checkpoint, allow_pickle=False) as raw:
                xx, yy, pp, scales = (raw[key].copy() for key in ('x','y','p','pscale'))
            if (obj.fixed or xx.ndim != 1 or len(xx) < 2 or xx[0] != 0 or xx[-1] != 1
                    or np.any(np.diff(xx) <= 0) or yy.shape != (obj.n,len(xx))
                    or pp.shape != (obj.M,) or not np.array_equal(scales,obj.pscale)
                    or not all(np.all(np.isfinite(v)) for v in (xx,yy,pp,scales))):
                raise ValueError('The literal full design checkpoint contract differs')
            # Synchronize the original full physical core with the original
            # additive delta/support parameter vector, without altering yy.
            obj.initial(pp)
            record = dict(scope=__doc__, checkpoint=str(checkpoint),
                checkpoint_sha256=bound_sha, nodes=len(xx), modes=obj.M,
                full_state_shape=list(yy.shape), all_complete_nodal_arrays_restored_bitwise=True,
                previous_portable_repeat_differences={key:float(np.max(np.abs(a-b)))
                    for key,a,b in (('x',x,xx),('y',y,yy),('p',p,pp))},
                original_main_sha256=hashlib.sha256(before.encode()).hexdigest(),
                executed_main_sha256=hashlib.sha256(after.encode()).hexdigest(),
                adapter_sha256=sha(__file__), original_portable_sha256=sha(portable),
                accepted_bvp=False, physical_gates_paid=False, full_J_assembled=False,
                original_equations_and_gates_changed=False)
            (outdir/'literal-full-design-nodal-restart.json').write_text(
                json.dumps(record,indent=2,allow_nan=False)+'\n')
            return xx, yy, pp

        module.__dict__['_held10_literal_design_nodal_restart'] = restore_nodal
        after = before.replace(marker,
            '        x,y,par = _held10_literal_design_nodal_restart(o,x,y,par)\n'+marker)
        virtual_filename = str(Path(__file__).resolve())+'::literal_nodal_entry'
        linecache.cache[virtual_filename] = (len(after), None,
                                             after.splitlines(keepends=True), virtual_filename)
        exec(compile(after, virtual_filename, 'exec'), module.__dict__)
        return module

    loader_module.load_module = load

    def restore():
        loader_module.load_module = original_loader

    return restore
