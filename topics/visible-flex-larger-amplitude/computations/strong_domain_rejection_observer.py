"""Observe original domain exceptions without changing the numerical path.

The original radial batching code and Flow methods are called in their original
order. Only a failed block is saved, losslessly, before the same exception is
re-raised. Constructor/boundary failures are explicitly distinguished from a
failed radial block. No extra RHS, geometry or derivative evaluation is made.
"""
from __future__ import annotations
import ast
import atexit
import functools
import hashlib
import io
import json
import math
from pathlib import Path
import time


def native(value):
    if isinstance(value, dict):
        return {str(k): native(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [native(v) for v in value]
    if hasattr(value, 'tolist'):
        return native(value.tolist())
    if isinstance(value, float) and not math.isfinite(value):
        return {'nonfinite_repr': repr(value)}
    if isinstance(value, (str, bool, int, float)) or value is None:
        return value
    return repr(value)


class DomainObservation:
    def __init__(self, out, configuration, source_hashes, emit=None):
        import numpy as np
        self.np, self.out = np, Path(out)
        self.configuration, self.source_hashes = dict(configuration), dict(source_hashes)
        self.emit_callback = emit
        self.active = None
        self.sequence = 0
        self.failures = []
        self.radial_originals = None
        self.methods = []
        self.closed = False
        self.started = time.monotonic()
        atexit.register(self.finish)

    def emit(self, event, **data):
        # Failure to log must not replace the original numerical exception.
        try:
            if self.emit_callback is not None:
                self.emit_callback(event, **data)
            else:
                print(json.dumps(dict(event=event, **data), allow_nan=False), flush=True)
        except Exception:
            pass

    def identity(self, obj, p, flow=None):
        result = {}
        if obj is not None:
            for name in ('M', 'nt', 'q', 'cfg', 'ref_coeff', 'ref_frequencies',
                         '_neck_knots', 'chart_breaks', '_special_layout', 'raw_recovery_context'):
                if hasattr(obj, name):
                    result[name] = native(getattr(obj, name))
            cfg = dict(getattr(obj, 'cfg', {}))
            M = getattr(obj, 'M', -100)
            if p is not None and len(p) == M+3:
                for name, offset in zip(('delta', 'boost_length', 'boost_speed'), p[M:]):
                    if name in cfg:
                        cfg[name] = cfg[name]+offset
                result['physical_profile_from_exact_selected_parameters'] = native(cfg)
        if flow is not None:
            result['actually_constructed_Flow_cfg'] = native(getattr(flow, 'cfg', None))
        return result

    def capture(self, error, kind, arrays, flow=None):
        """Best-effort evidence only; logging failure never replaces error."""
        existing = getattr(error, '_strong_domain_observation', None)
        if existing is not None:
            return existing
        self.sequence += 1
        label = '%04d' % self.sequence
        obj, stage = self.active if self.active is not None else (None, None)
        details = dict(index=self.sequence, kind=kind, callback_stage=stage,
            exception_type=type(error).__name__, exception_repr=repr(error),
            physical_radial_block=(kind in ('radial-value', 'radial-state-jacobian')),
            no_new_numerical_evaluation=True, original_exception_rethrown=True,
            solver_success=False, physical_surface=False)
        try:
            values = {name:self.np.asarray(value).copy() for name,value in arrays.items()}
            details['arrays'] = {name:dict(shape=list(v.shape), dtype=v.dtype.str,
                C_order_bytes_sha256=hashlib.sha256(v.tobytes(order='C')).hexdigest())
                for name,v in values.items()}
            if 's' in values:
                details['physical_s'] = native(values['s'])
            details['identity'] = self.identity(obj, values.get('p'), flow)
            details['run_configuration'] = self.configuration
            details['source_sha256_at_start'] = self.source_hashes
            metadata = json.dumps(native(details), separators=(',', ':'), allow_nan=False).encode()
            stream = io.BytesIO()
            self.np.savez_compressed(stream, metadata=self.np.frombuffer(metadata, dtype='u1'), **values)
            data = stream.getvalue()
            if len(data) >= 5_000_000:
                raise ValueError('Domain observation exceeds the original single-file size rule')
            path = self.out.with_name(self.out.name+'-domain-'+label+'.npz')
            if path.exists():
                raise FileExistsError('Domain evidence cannot overwrite another run: '+str(path))
            temporary = path.with_name(path.name+'.tmp')
            temporary.write_bytes(data)
            temporary.replace(path)
            record = dict(index=self.sequence, kind=kind, exception_repr=repr(error),
                path=str(path), bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                physical_radial_block=details['physical_radial_block'])
        except Exception as storage_error:
            record = dict(index=self.sequence, kind=kind, exception_repr=repr(error),
                observation_storage_error=repr(storage_error),
                original_exception_and_original_domain_rejection_preserved=True)
        error._strong_domain_observation = record
        self.failures.append(record)
        self.emit('original_domain_failure_observed', **record)
        return record

    def rejected(self, error, iteration, alpha, p):
        record = getattr(error, '_strong_domain_observation', None)
        if record is None:
            record = self.capture(error, 'Newton-evaluation-or-linear-solve', {'p':p})
        self.emit('original_Newton_domain_rejection_detail', iteration=int(iteration),
            alpha=float(alpha), exception_repr=repr(error), observation=record,
            original_continue_unchanged=True)

    def install_radial(self, radial):
        if self.radial_originals is not None:
            raise ValueError('Domain radial observation is installed only once')
        owner = self
        class FlowProxy:
            def __init__(self, flow):
                self.flow = flow
            def fun(self, s, y, p):
                try:
                    return self.flow.fun(s, y, p)
                except FloatingPointError as error:
                    owner.capture(error, 'radial-value', {'s':s, 'y':y, 'p':p}, self.flow)
                    raise
            def fun_jac(self, s, y, p):
                try:
                    return self.flow.fun_jac(s, y, p)
                except FloatingPointError as error:
                    owner.capture(error, 'radial-state-jacobian', {'s':s, 'y':y, 'p':p}, self.flow)
                    raise
        old_value, old_jac = radial.value, radial.state_jacobian
        def value(flow, s, y, p, batch_size=48):
            return old_value(FlowProxy(flow), s, y, p, batch_size)
        def state_jacobian(flow, s, y, p, batch_size=48):
            return old_jac(FlowProxy(flow), s, y, p, batch_size)
        value.__defaults__, state_jacobian.__defaults__ = old_value.__defaults__, old_jac.__defaults__
        self.radial_originals = radial, old_value, old_jac, value, state_jacobian
        radial.value, radial.state_jacobian = value, state_jacobian

    def install_class(self, cls):
        if cls.__dict__.get('_strong_domain_observation_installed', False):
            raise ValueError('Domain class observation is installed only once')
        owner = self
        def wrap(original, name):
            @functools.wraps(original)
            def observed(obj, *args, **kwargs):
                previous = owner.active
                owner.active = obj, name
                try:
                    return original(obj, *args, **kwargs)
                except FloatingPointError as error:
                    arrays = {}
                    if name in ('bc', 'bc_jac') and len(args) >= 3:
                        arrays = dict(ya=args[0], yb=args[1], p=args[2])
                    elif name in ('fun', 'fun_jac') and len(args) >= 3:
                        # If Flow construction/chart inversion failed before
                        # radial batching, no failed physical block exists.
                        arrays = dict(numerical_t=args[0], p=args[2])
                    elif name == 'initial' and args:
                        arrays = dict(p=args[0])
                    elif hasattr(obj, 'controls'):
                        arrays = dict(p=obj.controls)
                    owner.capture(error, 'callback-before-or-after-radial-block', arrays)
                    raise
                finally:
                    owner.active = previous
            return observed
        for name in ('flow', 'initial', 'fun', 'fun_jac', 'bc', 'bc_jac'):
            original = getattr(cls, name)
            self.methods.append((cls, name, original))
            setattr(cls, name, wrap(original, name))
        cls._strong_domain_observation_installed = True

    def install_newton(self, loaded, path, adapter):
        path = Path(path)
        transform = adapter.TRANSFORMS[path.name]
        source = path.read_text()
        if hashlib.sha256(source.encode()).hexdigest() != transform['original_sha256']:
            raise ValueError('Domain observer received another original Newton source')
        for change in transform['replacements']:
            if source.count(change['old']) != change['count']:
                raise ValueError('Earlier explicit Newton transform does not reproduce')
            source = source.replace(change['old'], change['new'])
        old = '            except FloatingPointError:\n'
        new = ('            except FloatingPointError as _strong_domain_error:\n'
               '                _strong_domain_observation.rejected(_strong_domain_error,iteration,alpha,trial_p)\n')
        if source.count(old) != 1:
            raise ValueError('The original domain exception site is not unique')
        source = source.replace(old, new, 1)
        ast.parse(source)
        transform['replacements'].append(dict(old=old,new=new,count=1))
        transform['domain_observation_only'] = dict(exception_type_unchanged=True,
            original_continue_and_acceptance_unchanged=True,
            failed_radial_blocks_saved_losslessly=True,
            no_new_numerical_evaluation=True)
        loaded._strong_domain_observation = self

    def finish(self):
        if self.closed:
            return
        if self.radial_originals is not None:
            radial, old_value, old_jac, value, jac = self.radial_originals
            old_value.__defaults__, old_jac.__defaults__ = value.__defaults__, jac.__defaults__
            radial.value, radial.state_jacobian = old_value, old_jac
        for cls, name, original in reversed(self.methods):
            setattr(cls, name, original)
            if cls.__dict__.get('_strong_domain_observation_installed', False):
                delattr(cls, '_strong_domain_observation_installed')
        result = dict(scope=__doc__, source_sha256_at_start=self.source_hashes,
            configuration=self.configuration, failures=self.failures,
            count=len(self.failures), seconds=time.monotonic()-self.started,
            original_equations_domain_decisions_and_acceptance_unchanged=True)
        path = self.out.with_name(self.out.name+'-domain-observer.json')
        temporary = path.with_name(path.name+'.tmp')
        temporary.write_text(json.dumps(native(result),indent=2,allow_nan=False)+'\n')
        temporary.replace(path)
        self.closed = True
