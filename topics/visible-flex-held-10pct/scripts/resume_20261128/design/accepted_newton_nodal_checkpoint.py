"""Save the whole nodal field after an original accepted Newton step.

The field is still an unaccepted BVP initializer: no RMS/metric/physical gate
is inferred. Each full iterate is immutable; an atomic latest pointer identifies
the most recent complete checkpoint, with a scalar hash journal. No RHS or Jacobian is reevaluated.
"""
import ast
import hashlib
import inspect
import json
from pathlib import Path
import time

import numpy as np
from scipy.integrate import _bvp


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def expected_released_source(domain):
    path = Path(domain.__file__).resolve()
    text = path.read_text()
    node, = [n for n in ast.parse(text).body
             if isinstance(n, ast.FunctionDef) and n.name == 'solve_newton']
    original = ''.join(text.splitlines(keepends=True)[node.lineno-1:node.end_lineno])
    marker = '            try:factor=splu(jac(y,p,ym,ff,fm,br))'
    if original.count(marker) != 1:
        raise ValueError('The original full-factor Newton statement changed')
    return original.replace(marker, '            factor=None\n'+marker)


def install(domain, outdir, scales, source_hashes):
    outdir = Path(outdir)
    scales = np.asarray(scales, dtype=float).copy()
    original_newton = domain.solve_newton
    original_installed = _bvp.solve_newton
    if original_installed is not original_newton:
        raise ValueError('The original released Newton function is not installed')
    expected = expected_released_source(domain)
    namespace = {}
    exec(compile(expected, original_newton.__code__.co_filename, 'exec'), namespace)
    expected_code = namespace['solve_newton'].__code__
    if (expected_code != original_newton.__code__ or
            expected_code.co_filename != original_newton.__code__.co_filename):
        raise ValueError('The executing Newton bytecode differs from the exact released original')
    accepted_line = ('        y,p,data,step,cost,alpha=accepted;STATS[\'accepted_steps\']+=1;'
                     'STATS[\'minimum_alpha\']=min(STATS[\'minimum_alpha\'],alpha);refresh=alpha!=1.')
    if expected.count(accepted_line) != 1:
        raise ValueError('The original accepted Newton tuple assignment changed')
    executed = expected.replace(accepted_line, accepted_line+
        '\n        _held10_save_accepted_newton_nodal(y,p,iteration,factors,alpha)')
    original_prepare = _bvp.prepare_sys
    wanted = ['n', 'm', 'k', 'fun', 'bc', 'fun_jac', 'bc_jac', 'x', 'h']
    if list(inspect.signature(original_prepare).parameters) != wanted:
        raise ValueError('The original adaptive-mesh prepare_sys signature changed')
    mesh = {}
    stats = dict(checkpoints=0, seconds=0.,
        original_released_newton_source_sha256=hashlib.sha256(expected.encode()).hexdigest(),
        executed_newton_source_sha256=hashlib.sha256(executed.encode()).hexdigest(),
        original_bytecode_identity_checked=True,
        all_original_arithmetic_statements_retained_in_original_order=True,
        extra_RHS_or_Jacobian_calls=0, whole_BVP_acceptance_claimed=False)

    def prepare(n, m, k, fun, bc, fun_jac, bc_jac, x, h):
        result = original_prepare(n, m, k, fun, bc, fun_jac, bc_jac, x, h)
        if scales.shape != (k-1,) or np.shape(x) != (m,):
            raise ValueError('The original full nodal dimensions/scales changed')
        mesh.update(n=n, m=m, k=k, x=np.array(x, copy=True))
        return result

    def checkpoint(y, p, iteration, factors, alpha):
        started = time.monotonic()
        n, m, k, x = (mesh[key] for key in ('n', 'm', 'k', 'x'))
        if y.shape != (n, m) or p.shape != (k,):
            raise ValueError('An incomplete state reached the original accepted-step checkpoint')
        ordinal = stats['checkpoints']+1
        filename = 'unaccepted-nodal-after-newton-call%04d-step%04d.npz' % (
            int(domain.STATS['calls']), int(iteration))
        destination = outdir/filename
        if destination.exists():
            raise FileExistsError(destination)
        temporary = destination.with_suffix('.npz.tmp')
        with temporary.open('xb') as stream:
            np.savez(stream, x=x, y=y, p=p, pscale=scales)
        temporary.replace(destination)
        row = dict(kind='unaccepted_complete_nodal_restart', file=destination.name,
            sha256=sha(destination), nodes=m, state_components=n, parameters=k,
            checkpoint_ordinal=ordinal, original_Newton_call=int(domain.STATS['calls']),
            local_Newton_iteration=int(iteration), local_factor_count=int(factors),
            original_accepted_steps=int(domain.STATS['accepted_steps']), alpha=float(alpha),
            mesh_min_spacing=float(np.min(np.diff(x))),
            original_source_hashes=source_hashes, original_Newton_step_accepted=True,
            before_full_J_assembly=False, after_original_accepted_tuple_assignment=True,
            raw_RMS_metric_and_physical_BC_still_unpaid=True, accepted_bvp=False,
            immutable_complete_checkpoint_and_atomic_latest_pointer=True,
            checkpoint_statistics=dict(stats))
        with (outdir/'accepted-newton-nodal-checkpoints.jsonl').open('a') as stream:
            stream.write(json.dumps(row, allow_nan=False)+'\n')
        pointer = outdir/'latest-unaccepted-newton-nodal.json'
        pointer_tmp = pointer.with_suffix('.json.tmp')
        pointer_tmp.write_text(json.dumps(row, indent=2, allow_nan=False)+'\n')
        pointer_tmp.replace(pointer)
        stats['checkpoints'] = ordinal
        stats['seconds'] += time.monotonic()-started

    key = '_held10_save_accepted_newton_nodal'
    if key in domain.__dict__:
        raise ValueError('An accepted-step checkpoint is already installed')
    domain.__dict__[key] = checkpoint
    exec(compile(executed, str(Path(__file__).resolve())+'::checkpointed_original_Newton',
                 'exec'), domain.__dict__)
    domain.install()
    _bvp.prepare_sys = prepare

    def restore():
        _bvp.prepare_sys = original_prepare
        domain.solve_newton = original_newton
        _bvp.solve_newton = original_installed
        domain.__dict__.pop(key)

    return stats, restore
