"""Unique chunked recovery points for accepted affine-inner Newton iterates.

Each raw manifest has unique array filenames and is published only after
every piece is written and read back.  The latest pointer changes atomically;
the preceding complete point is kept.  These states are explicitly not
accepted nonlinear-tail solutions, even when an inner Newton step was
accepted.  A fresh true-tail check remains mandatory on every restart.
"""
from __future__ import annotations
import datetime
import gzip
import hashlib
import json
import os
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.integrate import _bvp
import root_raw_collocation as raw


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class Recorder:
    def __init__(self, prefix, source_hashes):
        self.prefix = Path(prefix)
        self.hashes = dict(source_hashes)
        self.obj = None
        self.serial = 0
        self.retained = []
        self.last_digest = None
        self.last_record = None
        self.ledger = self.prefix.with_name(self.prefix.name+'-iterate-ledger.jsonl')
        if self.ledger.exists():
            raise FileExistsError('Use a fresh actual-continuation output prefix')

    def save(self, col_fun, y, p, data, iteration, phase, bvp_tol, bc_tol, stats):
        if self.obj is None:
            raise RuntimeError('Actual Newton observer has no active object')
        closure = dict(zip(col_fun.__code__.co_freevars,
            (cell.cell_contents for cell in col_fun.__closure__ or ())))
        if 'x' not in closure:
            raise RuntimeError('The actual collocation closure no longer exposes its exact mesh')
        x = np.asarray(closure['x'], np.float64)
        y, p = np.asarray(y, np.float64), np.asarray(p, np.float64)
        h = np.diff(x)
        if y.shape != (self.obj.n, len(x)) or len(p) != self.obj.M+3 or not np.all(h > 0):
            raise ValueError('Actual iterate dimensions or mesh differ')
        digest = hashlib.sha256(x.tobytes()+y.tobytes()+p.tobytes()).hexdigest()
        if digest == self.last_digest:
            print(json.dumps(dict(event='actual_iterate_checkpoint_reused', phase=phase,
                call=int(stats['calls']), iteration=int(iteration), **self.last_record)), flush=True)
            return
        self.obj.select(p)
        if bc_tol != 1e-7:
            raise ValueError('The original boundary tolerance changed')
        cubic = _bvp.create_spline(y, data[3], x, h)
        # RMS is deliberately not re-evaluated inside this observation. Its
        # empty array and false success prevent postprocess-only acceptance.
        sol = SimpleNamespace(x=x, y=y, p=p, sol=cubic,
            rms_residuals=np.empty(0), success=False, status=1,
            niter=int(iteration), message='Unaccepted affine-inner Newton recovery point; true full-H nonlinear tail recheck and original final gates still required')
        self.serial += 1
        path = self.prefix.with_name(self.prefix.name+f'-iterate-{self.serial:04d}.json.gz')
        if path.exists() or any(path.parent.glob(path.name.removesuffix('.json.gz')+'-*.npy.gz')):
            raise FileExistsError('Immutable actual iterate filenames already exist')
        provenance = dict(scope=__doc__, phase=phase, call=int(stats['calls']),
            iteration=int(iteration), rms_not_evaluated=True, actual_coupled_acceptance_pending=True,
            physical_surface=False, source_sha256=self.hashes,
            scaled_collocation_max=float(np.max(abs(data[1])/(h[None, :]*(1+abs(data[4]))))),
            boundary_max=float(np.max(abs(data[5]))),
            written_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
        record = raw.write(path, sol, self.obj, SimpleNamespace(tol=bvp_tol), provenance)
        checked, checked_record = raw.read(path, self.obj, SimpleNamespace(tol=bvp_tol))
        for name in ('x', 'y', 'p'):
            if not np.array_equal(getattr(checked, name), getattr(sol, name)):
                raise ValueError('Actual iterate readback differs: '+name)
        if not np.array_equal(checked.sol.c, cubic.c) or checked.success or checked.rms_residuals.size:
            raise ValueError('Actual iterate cubic or unaccepted status differs')
        del checked
        record.update(unique_immutable_manifest=True,
            complete_piece_readback_passed=True, actual_coupled_acceptance_pending=True)
        pointer = self.prefix.with_name(self.prefix.name+'-latest-iterate.json')
        temporary = pointer.with_name(pointer.name+'.tmp')
        with temporary.open('w') as stream:
            stream.write(json.dumps(record, indent=2)+'\n')
            stream.flush()
            os.fsync(stream.fileno())
        temporary.replace(pointer)
        with self.ledger.open('a') as stream:
            stream.write(json.dumps(dict(event='saved', phase=phase, call=int(stats['calls']),
                iteration=int(iteration), scaled_collocation_max=provenance['scaled_collocation_max'],
                boundary_max=provenance['boundary_max'], **record))+'\n')
            stream.flush()
            os.fsync(stream.fileno())
        self.retained.append((path, checked_record))
        while len(self.retained) > 2:
            old_path, old_record = self.retained.pop(0)
            for item in old_record['arrays'].values():
                for chunk in item['chunks']:
                    piece = old_path.parent/chunk['file']
                    if (Path(chunk['file']).name != chunk['file'] or
                            not piece.name.startswith(old_path.name.removesuffix('.json.gz')+'-')):
                        raise ValueError('Refusing to remove a non-owned iterate piece')
                    piece.unlink()
            old_path.unlink()
        self.last_digest, self.last_record = digest, record
        print(json.dumps(dict(event='actual_iterate_checkpoint_saved', phase=phase,
            call=int(stats['calls']), iteration=int(iteration), **record)), flush=True)


def install_observer(loaded, path, adapter, recorder):
    """Add observations to the already selected, unchanged owned Newton."""
    path = Path(path)
    source = path.read_text()
    transform = adapter.TRANSFORMS[path.name]
    if sha(path) != transform['original_sha256']:
        raise ValueError('Newton source changed after its reviewed loading')
    for change in transform['replacements']:
        if source.count(change['old']) != change['count']:
            raise ValueError('The existing Newton source transform changed')
        source = source.replace(change['old'], change['new'])
    function = source[source.index('def solve_newton('):source.index('\n\ndef install(')]
    changes = [
        ('    data = evaluate(y, p)\n',
         '    data = evaluate(y, p)\n    _strong_actual_checkpoint(col_fun,y,p,data,0,"newton-entry",bvp_tol,bc_tol,STATS)\n'),
        ('        y, p, data, step, cost, alpha = accepted\n',
         '        y, p, data, step, cost, alpha = accepted\n        _strong_actual_checkpoint(col_fun,y,p,data,iteration+1,"accepted-newton",bvp_tol,bc_tol,STATS)\n'),
        ('    return y, p, False',
         '    _strong_actual_checkpoint(col_fun,y,p,data,iteration,"newton-return",bvp_tol,bc_tol,STATS)\n    return y, p, False')]
    for before, after in changes:
        if function.count(before) != 1:
            raise ValueError('The actual Newton observation anchor changed')
        function = function.replace(before, after)
    loaded._strong_actual_checkpoint = recorder.save
    exec(compile(function, str(path), 'exec'), loaded.__dict__)
    transform['actual_checkpoint_only_observation'] = dict(
        replacements=[dict(old=a, new=b, count=1) for a, b in changes],
        equations_changed=False, acceptance_changed=False,
        unique_immutable_pieces=True, keep_latest_complete=2)
