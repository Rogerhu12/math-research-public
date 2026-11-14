"""Durable raw Newton result, before physical interpolation or auditing.

The numerical-coordinate cubic is a recovery object, not a C2 surface.
Array pieces are exact float64, compressed, individually below 5 MB. The
manifest is replaced only after every array piece is fully written.
"""
from __future__ import annotations
import gzip
import gc
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import PPoly


def release_memory(stage):
    """Release unreachable objects/free allocator pages, never live arrays."""
    def current_rss():
        try:
            for line in Path('/proc/self/status').read_text().splitlines():
                if line.startswith('VmRSS:'):
                    return int(line.split()[1])
        except OSError:
            pass
        return None
    before = current_rss()
    collected = gc.collect()
    trimmed = None
    try:
        import ctypes
        trim = ctypes.CDLL(None).malloc_trim
        trim.argtypes, trim.restype = [ctypes.c_size_t], ctypes.c_int
        trimmed = int(trim(0))
    except (AttributeError, OSError):
        pass
    result = dict(event='unused_memory_released', stage=stage,
        collected_unreachable=collected, allocator_trim=trimmed,
        rss_before_kib=before, rss_after_kib=current_rss())
    print(json.dumps(result), flush=True)
    return result


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def identity(obj, args):
    flow = obj.flow(float(obj.controls[0]))
    return dict(modes=int(obj.M), angular=int(obj.nt), gauge=float(obj.q),
                fixed=bool(getattr(obj, 'fixed', False)), profile=dict(flow.cfg),
                physical_tail_parameters=obj.port['parameters'], physical_tail_cut=obj.port['cut'],
                reference_coefficients=obj.ref_coeff.tolist(),
                reference_frequencies=list(getattr(obj, 'ref_frequencies', [2, 4])),
                parameter_layout=obj._special_layout, tol=float(args.tol), bc_tol=1e-7,
                coupling_context=getattr(obj, 'raw_recovery_context', None),
                numerical_reference_knots=None if obj._neck_knots is None else obj._neck_knots.tolist())


def write(path, sol, obj, args, provenance):
    path = Path(path)
    obj.select(sol.p)
    record = dict(scope=__doc__, raw_collocation_only=True, physical_surface=False,
                  identity=identity(obj, args), parameter_state=sol.p.tolist(),
                  solver_success=bool(sol.success), status=int(sol.status), message=str(sol.message),
                  niter=int(sol.niter), provenance=provenance, arrays={},
                  writer_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    arrays = dict(x=sol.x, y=sol.y, p=sol.p, cubic=sol.sol.c, rms=sol.rms_residuals)
    stem = path.name.removesuffix('.gz').removesuffix('.json')
    for name, array in arrays.items():
        array = np.asarray(array, dtype=np.float64)
        flat = array.ravel()
        item = dict(shape=list(array.shape), dtype='float64', chunks=[])
        for number, first in enumerate(range(0, flat.size, 500_000)):
            part = path.with_name(f'{stem}-{name}-{number:03d}.npy.gz')
            temporary = part.with_name(part.name + '.tmp')
            with gzip.open(temporary, 'wb', compresslevel=6) as stream:
                np.save(stream, flat[first:first+500_000], allow_pickle=False)
            if temporary.stat().st_size >= 5_000_000:
                raise ValueError('Raw checkpoint piece exceeds file limit')
            temporary.replace(part)
            item['chunks'].append(dict(file=part.name, first=first,
                count=min(500_000, flat.size-first),
                sha256=hashlib.sha256(part.read_bytes()).hexdigest()))
        record['arrays'][name] = item
    temporary = path.with_name(path.name + '.tmp')
    with gzip.open(temporary, 'wt') as stream:
        json.dump(record, stream, indent=2, allow_nan=False)
        stream.write('\n')
    temporary.replace(path)
    return dict(file=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                nodes=len(sol.x), solver_success=bool(sol.success), physical_surface=False)


def read(path, obj, args):
    path = Path(path)
    with gzip.open(path, 'rt') as stream:
        record = json.load(stream)
    if record.get('raw_collocation_only') is not True or record.get('physical_surface') is not False:
        raise ValueError('This is not a raw collocation recovery manifest')
    obj.select(np.asarray(record['parameter_state']))
    if canonical(identity(obj, args)) != canonical(record['identity']):
        raise ValueError('Raw recovery changed physical data, layout, chart or tolerances')
    values = {}
    for name, item in record['arrays'].items():
        flat = np.empty(int(np.prod(item['shape'])), dtype=np.float64)
        end = 0
        for chunk in item['chunks']:
            if chunk['first'] != end or Path(chunk['file']).name != chunk['file']:
                raise ValueError('Unexpected raw array piece layout')
            part = path.parent / chunk['file']
            if hashlib.sha256(part.read_bytes()).hexdigest() != chunk['sha256']:
                raise ValueError('Raw array piece hash mismatch')
            with gzip.open(part, 'rb') as stream:
                block = np.load(stream, allow_pickle=False)
            if block.size != chunk['count']:
                raise ValueError('Raw array piece shape mismatch')
            flat[end:end+block.size] = block
            end += block.size
        if end != flat.size:
            raise ValueError('Incomplete raw array')
        values[name] = flat.reshape(item['shape'])
    if not np.array_equal(values['p'], record['parameter_state']):
        raise ValueError('Raw parameter manifest mismatch')
    solution = SimpleNamespace(x=values['x'], y=values['y'], p=values['p'],
        sol=PPoly.construct_fast(values['cubic'], values['x'], extrapolate=True, axis=1),
        rms_residuals=values['rms'], status=record['status'], success=record['solver_success'],
        message=record['message'], niter=record['niter'])
    return solution, record
