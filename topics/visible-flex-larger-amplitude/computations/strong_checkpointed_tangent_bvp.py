#!/usr/bin/env python3
"""Persist accepted Newton states of the unchanged tangent-warm BVP.

Every bundle contains numerical x/y/p and the same nodal cubic, with an
explicit unaccepted status. A unique file is written and validated before
atomic rename; the preceding complete bundle is retained. Only the latest
two complete bundles remain. Restoring one is another initial guess for the
same complete BVP and never bypasses residual, domain or physical auditing.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import sys
import types
from types import SimpleNamespace
import numpy as np
from scipy.integrate import _bvp

HERE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def read_bundle(path):
    with np.load(path, allow_pickle=False) as archive:
        metadata = json.loads(archive['metadata'].tobytes().decode())
        arrays = {name: archive[name].copy() for name in ('x', 'y', 'p', 'cubic')}
    if metadata.get('solver_success') is not False or metadata.get('physical_surface') is not False:
        raise ValueError('An iterate bundle must explicitly remain unaccepted')
    if metadata.get('format') != 'strong-newton-iterate-bundle-v1':
        raise ValueError('Wrong iterate checkpoint format')
    for name, array in arrays.items():
        if not np.isfinite(array).all():
            raise ValueError('Nonfinite iterate array '+name)
        if list(array.shape) != metadata['array_shapes'][name]:
            raise ValueError('Iterate array shape differs')
    return metadata, arrays


class Recorder:
    def __init__(self, prefix, source_hashes):
        self.prefix = Path(prefix)
        self.source_hashes = source_hashes
        self.obj = None
        self.serial = 0
        self.retained = []
        self.last_state_hash = None
        self.last_record = None
        self.ledger = self.prefix.with_name(self.prefix.name+'-iterate-ledger.jsonl')
        if self.ledger.exists():
            raise ValueError('Use a fresh output prefix, preserving the previous run')

    def save(self, col_fun, y, p, data, iteration, phase, bvp_tol, bc_tol, stats):
        if self.obj is None:
            raise RuntimeError('No active BVP object for iterate persistence')
        closure = dict(zip(col_fun.__code__.co_freevars,
                           (cell.cell_contents for cell in col_fun.__closure__ or ())))
        if 'x' not in closure:
            raise RuntimeError('Unknown collocation closure; refusing guessed coordinates')
        x = np.asarray(closure['x'], dtype=np.float64)
        y = np.asarray(y, dtype=np.float64)
        p = np.asarray(p, dtype=np.float64)
        h = np.diff(x)
        if y.shape[1] != len(x) or not np.all(h > 0):
            raise ValueError('Invalid numerical mesh in checkpoint callback')
        state_hash = hashlib.sha256(x.tobytes()+y.tobytes()+p.tobytes()).hexdigest()
        if state_hash == self.last_state_hash:
            print(json.dumps(dict(event='newton_checkpoint_reused', phase=phase,
                call=int(stats['calls']), iteration=iteration, **self.last_record)), flush=True)
            return
        import root_raw_collocation
        self.obj.select(p)
        identity = root_raw_collocation.identity(self.obj, SimpleNamespace(tol=bvp_tol))
        if float(bc_tol) != identity['bc_tol']:
            raise ValueError('Unexpected boundary tolerance in checkpoint callback')
        cubic = _bvp.create_spline(y, data[3], x, h).c
        arrays = dict(x=x, y=y, p=p, cubic=np.asarray(cubic, dtype=np.float64))
        metadata = dict(format='strong-newton-iterate-bundle-v1', scope=__doc__,
            solver_success=False, physical_surface=False,
            state_phase=phase, call=int(stats['calls']), iteration=iteration,
            nonlinear_solver_returned=False, final_residual_acceptance_performed=False,
            physical_audit_performed=False, identity=identity, base_profile=dict(self.obj.cfg),
            scaled_collocation_max=float(np.max(abs(data[1])/(h[None, :]*(1+abs(data[4]))))),
            boundary_max=float(np.max(abs(data[5]))),
            array_shapes={name: list(a.shape) for name, a in arrays.items()},
            source_sha256=self.source_hashes,
            written_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
        encoded = canonical(metadata).encode()
        self.serial += 1
        path = self.prefix.with_name(self.prefix.name+f'-iterate-{self.serial:04d}.npz')
        temporary = path.with_name(path.name+'.tmp')
        if path.exists() or temporary.exists():
            raise ValueError('Refusing to overwrite an immutable iterate bundle')
        with temporary.open('wb') as stream:
            np.savez_compressed(stream, metadata=np.frombuffer(encoded, dtype=np.uint8), **arrays)
            stream.flush()
            os.fsync(stream.fileno())
        if temporary.stat().st_size >= 5_000_000:
            raise ValueError('Iterate bundle exceeds 5 MB; use an explicitly reviewed chunked writer')
        checked_metadata, checked_arrays = read_bundle(temporary)
        if canonical(checked_metadata) != canonical(metadata):
            raise ValueError('Iterate metadata round trip differs')
        for name in arrays:
            if not np.array_equal(arrays[name], checked_arrays[name]):
                raise ValueError('Iterate array round trip differs: '+name)
        del checked_arrays
        temporary.replace(path)
        record = dict(file=str(path), sha256=digest(path), bytes=path.stat().st_size,
                      nodes=len(x), solver_success=False, physical_surface=False)
        pointer = self.prefix.with_name(self.prefix.name+'-latest-iterate.json')
        pointer_tmp = pointer.with_name(pointer.name+'.tmp')
        pointer_tmp.write_text(json.dumps(record, indent=2)+'\n')
        pointer_tmp.replace(pointer)
        with self.ledger.open('a') as stream:
            stream.write(json.dumps(dict(event='saved', phase=phase, call=int(stats['calls']),
                iteration=iteration, scaled_collocation_max=metadata['scaled_collocation_max'],
                boundary_max=metadata['boundary_max'], **record))+'\n')
            stream.flush()
            os.fsync(stream.fileno())
        self.retained.append(path)
        while len(self.retained) > 2:
            old = self.retained.pop(0)
            old.unlink()
        self.last_state_hash, self.last_record = state_hash, record
        print(json.dumps(dict(event='newton_checkpoint_saved', phase=phase,
            call=int(stats['calls']), iteration=iteration, **record)), flush=True)


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--resume-iterate', type=Path)
    parser.add_argument('--iterate-check-output', type=Path)
    opts, remaining = parser.parse_known_args()
    sys.argv = [sys.argv[0]]+remaining
    if '--out-prefix' not in remaining:
        raise ValueError('An explicit fresh output prefix is required')
    prefix = Path(remaining[remaining.index('--out-prefix')+1])
    inner = HERE/'strong_tangent_warm_bvp.py'
    source = inner.read_text()
    hashes = {str(path): digest(path) for path in (
        Path(__file__), inner, HERE/'strong_neck_bvp.py', HERE/'root_domain_newton.py',
        HERE/'root_raw_collocation.py', HERE/'root_block_collocation.py')}
    recorder = Recorder(prefix, hashes)
    resume_metadata, resume_arrays = read_bundle(opts.resume_iterate) if opts.resume_iterate else (None, None)

    def resume(obj, t, y, p, record, saved, form_guess):
        if resume_arrays is None:
            return form_guess(obj, t, y, p, record, saved)
        import root_raw_collocation
        obj.select(resume_arrays['p'])
        tol = float(remaining[remaining.index('--tol')+1]) if '--tol' in remaining else 1e-6
        current = root_raw_collocation.identity(obj, SimpleNamespace(tol=tol))
        if canonical(current) != canonical(resume_metadata['identity']):
            raise ValueError('Iterate recovery changes the physical data, chart, layout or tolerances')
        if obj.cfg != resume_metadata['base_profile']:
            raise ValueError('Iterate recovery changes the numerical profile base')
        obj.initial(resume_arrays['p'])
        record['unaccepted_iterate_recovery'] = dict(
            file=str(opts.resume_iterate), sha256=digest(opts.resume_iterate),
            previous_state_phase=resume_metadata['state_phase'],
            previous_solver_success=False, physical_surface=False,
            prior_call=resume_metadata['call'], prior_iteration=resume_metadata['iteration'],
            interpolation='Exact saved numerical x/y/p; stored cubic is retained for review.',
            final_acceptance_skipped=False)
        obj.design_provenance['unaccepted_iterate_recovery'] = record['unaccepted_iterate_recovery']
        return (resume_arrays['x'].copy(), resume_arrays['y'].copy(),
                resume_arrays['p'].copy(), record)

    def wrap_install(inner_install):
        def install(runner):
            inner_install(runner)
            load = runner.module

            def module(name, path):
                loaded = load(name, path)
                path = Path(path)
                if path.name == 'root_domain_newton.py':
                    transformed = path.read_text()
                    transformation = runner.TRANSFORMS[path.name]
                    for change in transformation['replacements']:
                        if transformed.count(change['old']) != change['count']:
                            raise ValueError('Newton transformation changed')
                        transformed = transformed.replace(change['old'], change['new'])
                    function = transformed[transformed.index('def solve_newton('):transformed.index('\n\ndef install(')]
                    changes = [
                        ('    data = evaluate(y, p)\n',
                         '    data = evaluate(y, p)\n    _strong_checkpoint(col_fun,y,p,data,0,"newton-entry",bvp_tol,bc_tol,STATS)\n'),
                        ('        y, p, data, step, cost, alpha = accepted\n',
                         '        y, p, data, step, cost, alpha = accepted\n        _strong_checkpoint(col_fun,y,p,data,iteration+1,"accepted-newton",bvp_tol,bc_tol,STATS)\n'),
                        ('    return y, p, False',
                         '    _strong_checkpoint(col_fun,y,p,data,iteration,"newton-return",bvp_tol,bc_tol,STATS)\n    return y, p, False')]
                    for old, new in changes:
                        if function.count(old) != 1:
                            raise ValueError('Newton checkpoint anchor changed')
                        function = function.replace(old, new)
                    loaded._strong_checkpoint = recorder.save
                    exec(compile(function, str(path), 'exec'), loaded.__dict__)
                    transformation['checkpoint_only_observation'] = dict(
                        source_sha256=hashes, replacements=[dict(old=a, new=b) for a, b in changes],
                        equations_changed=False, acceptance_changed=False)
                if path.name == 'root_dual_core_bvp.py':
                    solve = loaded.solve_bvp

                    def observed_solve(fun, bc, x, y, p, **kwargs):
                        recorder.obj = fun.__self__
                        # The current production M20/max2000 case has less
                        # than 4.9 MB of raw x/y/p/cubic, plus small metadata.
                        raw_bound = ((5*kwargs['max_nodes']-4)*y.shape[0]
                                     +kwargs['max_nodes']+len(p))*8+100_000
                        if raw_bound >= 5_000_000:
                            raise ValueError('This configuration needs the chunked iterate writer before solving')
                        if opts.iterate_check_output:
                            h = np.diff(x)
                            col, unused_jac = _bvp.prepare_sys(y.shape[0], len(x), len(p),
                                fun, bc, kwargs['fun_jac'], kwargs['bc_jac'], x, h)
                            forbidden_calls = []

                            def forbidden_jac(*unused):
                                forbidden_calls.append(True)
                                raise RuntimeError('A Jacobian is forbidden in the persistence-only inspection')

                            returned_y, returned_p, singular = _bvp.solve_newton(
                                y.shape[0], len(x), h, col, bc, forbidden_jac,
                                y.copy(), p.copy(), None, kwargs['tol'], kwargs['bc_tol'])
                            if forbidden_calls or singular or not np.array_equal(returned_y, y) or not np.array_equal(returned_p, p):
                                raise RuntimeError('Persistence-only inspection changed the warm state')
                            metadata, arrays = read_bundle(recorder.retained[-1])
                            import root_raw_collocation
                            recorder.obj.select(p)
                            current = root_raw_collocation.identity(recorder.obj,
                                SimpleNamespace(tol=kwargs['tol']))
                            if canonical(current) != canonical(metadata['identity']):
                                raise RuntimeError('Real checkpoint identity failed its restore comparison')
                            if not np.array_equal(arrays['x'], x) or not np.array_equal(arrays['y'], y) or not np.array_equal(arrays['p'], p):
                                raise RuntimeError('Real checkpoint state round trip differs')
                            report = dict(scope='Actual successful-prefix warm state through the full production loader and observed Newton entry/return, with Jacobian construction forbidden. No BVP or new surface is solved.',
                                inspection_only=True, nonlinear_solution=False, modes=recorder.obj.M,
                                angular=recorder.obj.nt, nodes=len(x), global_jacobian_calls=0,
                                returned_state_bitwise_equal=True, bundle_arrays_bitwise_equal=True,
                                identity_matches=True, resumed_from=str(opts.resume_iterate) if opts.resume_iterate else None,
                                raw_state=recorder.last_record, saved_metadata=metadata,
                                source_sha256=hashes)
                            opts.iterate_check_output.write_text(json.dumps(report, indent=2)+'\n')
                            print(json.dumps(dict(event='real_iterate_persistence_check_passed',
                                nodes=len(x), raw_state=recorder.last_record,
                                resumed_from=report['resumed_from'])), flush=True)
                            raise RuntimeError('Newton persistence inspection complete; no BVP requested')
                        return solve(fun, bc, x, y, p, **kwargs)

                    loaded.solve_bvp = observed_solve
                return loaded

            runner.module = module
        return install

    replacements = [
        ("module.__dict__['_tangent_install'] = install",
         "module.__dict__['_tangent_install'] = _checkpoint_install(install)"),
        ('return form_guess(self, t, y, p, record, saved)',
         'return _checkpoint_resume(self, t, y, p, record, saved, form_guess)')]
    for old, new in replacements:
        if source.count(old) != 1:
            raise ValueError('Tangent checkpoint entry anchor changed')
        source = source.replace(old, new)
    module = types.ModuleType('strong_checkpointed_tangent_entry')
    module.__file__ = str(inner)
    module.__dict__.update(_checkpoint_install=wrap_install, _checkpoint_resume=resume)
    exec(compile(source, str(inner), 'exec'), module.__dict__)
    module.main()


if __name__ == '__main__':
    main()
