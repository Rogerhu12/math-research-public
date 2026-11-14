"""Lossless, complete-input persistence of actual prefix fun/fun_jac calls.

This does not cache BCs, Newton decisions, RMS tests, or nonlinear tail work.
One immutable entry contains every input and both Jacobian outputs. A hit
restores the original selected parameters and baseline Flow before returning
arrays with the recorded dtype, layout and bytes. Diagnostic evaluation counts
and the warmth of internal memoization tables are deliberately not replayed.
"""
from __future__ import annotations
import atexit
import functools
import gzip
import hashlib
import inspect
import json
import marshal
import math
import os
from pathlib import Path
import platform
import struct
import sys
import time
import types

RUNTIME_CONFIGURATION = None
HERE = Path(__file__).resolve().parent
SELF_SHA = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
MAGIC = b'STRONG-PREFIX-CACHE-1\n'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encode(value):
    """Typed scalar identity; floats (including minus zero) use exact hex."""
    if value is None or isinstance(value, (str, bool)):
        return value
    if isinstance(value, int):
        return {'integer': str(value)}
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError('Nonfinite cache identity')
        return {'float64': struct.pack('<d', value).hex()}
    if isinstance(value, Path):
        return {'path': str(value)}
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in sorted(value.items(), key=lambda x: str(x[0]))}
    if isinstance(value, (list, tuple)):
        return {'tuple' if isinstance(value, tuple) else 'list': [encode(v) for v in value]}
    if hasattr(value, 'dtype') and hasattr(value, 'shape'):
        return {'array': describe(value)}
    if hasattr(value, 'item'):
        return encode(value.item())
    raise TypeError('Unsupported mathematical identity type: '+str(type(value)))


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def describe(value):
    import numpy as np
    a = np.asarray(value)
    if a.dtype.hasobject or not np.isfinite(a).all():
        raise ValueError('Cache arrays must be finite non-object arrays')
    return dict(shape=list(a.shape), dtype=a.dtype.str, strides=list(a.strides),
        C_contiguous=bool(a.flags.c_contiguous), F_contiguous=bool(a.flags.f_contiguous),
        bytes=int(a.nbytes), C_bytes_sha256=sha(a.tobytes(order='C')))


def restore_array(record, data):
    import numpy as np
    if len(data) != record['bytes'] or sha(data) != record['C_bytes_sha256']:
        raise ValueError('Cached array bytes failed their exact digest')
    shape, dtype, strides = tuple(record['shape']), np.dtype(record['dtype']), tuple(record['strides'])
    plain = np.frombuffer(data, dtype=dtype).reshape(shape)
    low = sum(min(0, (size-1)*stride) for size, stride in zip(shape, strides))
    high = sum(max(0, (size-1)*stride) for size, stride in zip(shape, strides))
    buffer = np.empty(max(dtype.itemsize, high-low+dtype.itemsize), dtype='u1')
    result = np.ndarray(shape, dtype=dtype, buffer=buffer, offset=-low, strides=strides)
    result[...] = plain
    if describe(result) != record:
        raise ValueError('Cached output dtype/layout/bytes failed roundtrip')
    return result


def atomic_new(path, data):
    """No replacement of an existing identity or a completed cache item."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name+'.tmp-'+str(os.getpid()))
    try:
        with temp.open('xb') as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        try:
            os.link(temp, path)
        except FileExistsError:
            if path.read_bytes() != data:
                raise ValueError('Immutable cache entry already contains different bytes: '+str(path))
    finally:
        temp.unlink(missing_ok=True)


class InspectionComplete(BaseException):
    pass


class Runtime:
    def __init__(self, out, source_hashes, source_topic, adapter, batch_sizes):
        if RUNTIME_CONFIGURATION is None:
            raise ValueError('Prefix cache must be explicitly configured by its own entry')
        import numpy as np
        self.np = np
        self.configuration = dict(RUNTIME_CONFIGURATION)
        self.out = Path(out)
        self.root = Path(self.configuration['directory']).resolve()
        self.budget = int(self.configuration['budget_bytes'])
        if not 0 < self.budget <= 256*1024**2:
            raise ValueError('Explicit prefix cache budget must be at most 256 MiB')
        self.source_hashes = source_hashes
        self.source_topic = Path(source_topic).resolve()
        self.adapter = adapter
        self.batch_sizes = dict(batch_sizes)
        self.methods = []
        self.identity = None
        self.identity_sha = None
        self.directory = None
        self.bytes = 0
        self.stats = dict(hits=0, misses=0, completed_writes=0, bypassed_size=0,
            bypassed_budget=0, write_errors=0, restored_baseline_Flow=0)
        self.closed = False
        self.started = time.monotonic()
        self.log = self.out.with_name(self.out.name+'-prefix-cache-events.jsonl')
        self.originals = {}
        atexit.register(self.finish)

    def event(self, event, **details):
        row = dict(event=event, seconds=time.monotonic()-self.started, **details)
        with self.log.open('a') as stream:
            stream.write(json.dumps(row, sort_keys=True, allow_nan=False)+'\n')
        count = self.stats['hits']+self.stats['misses']
        if event != 'prefix_cache_call' or count <= 3 or count % 20 == 0:
            print(json.dumps(row, allow_nan=False), flush=True)

    def source_closure(self, obj):
        """Capture actual loaded local modules, including unregistered imports.

        Class methods' global dictionaries lead to provider modules imported
        outside sys.modules. All pinned Python source is additionally bound.
        Function code hashes bind the actually compiled transformations.
        """
        files = dict(self.source_hashes)
        code = {}
        pending = []
        seen = set()
        roots = (HERE.resolve(), self.source_topic)

        def local_path(path):
            try:
                p = Path(path).resolve()
                return p if p.suffix == '.py' and any(p.is_relative_to(root) for root in roots) else None
            except (TypeError, ValueError, OSError):
                return None

        def function(value):
            value = getattr(value, '__func__', value)
            if not isinstance(value, types.FunctionType) or id(value) in seen:
                return
            seen.add(id(value))
            source = local_path(value.__globals__.get('__file__'))
            filename = local_path(value.__code__.co_filename)
            if source is None and filename is None:
                return
            label = str(source or filename)+':'+value.__qualname__
            code[label] = sha(marshal.dumps(value.__code__))
            for p in (source, filename):
                if p is not None:
                    files[str(p)] = sha(p.read_bytes())
            pending.append(value.__globals__)
            if hasattr(value, '__wrapped__'):
                function(value.__wrapped__)

        def cls(value):
            if not inspect.isclass(value) or id(value) in seen:
                return
            seen.add(id(value))
            for parent in value.__mro__:
                for method in vars(parent).values():
                    function(method)

        for module in list(sys.modules.values()):
            path = local_path(getattr(module, '__file__', None))
            if path is not None:
                files[str(path)] = sha(path.read_bytes())
                pending.append(vars(module))
        cls(type(obj))
        cls(obj.Flow)
        dictionaries = set()
        while pending:
            namespace = pending.pop()
            if id(namespace) in dictionaries:
                continue
            dictionaries.add(id(namespace))
            path = local_path(namespace.get('__file__'))
            if path is not None:
                files[str(path)] = sha(path.read_bytes())
            for value in list(namespace.values()):
                if isinstance(value, types.ModuleType):
                    path = local_path(getattr(value, '__file__', None))
                    if path is not None:
                        files[str(path)] = sha(path.read_bytes())
                        pending.append(vars(value))
                elif isinstance(value, types.FunctionType):
                    function(value)
                elif inspect.isclass(value):
                    module = sys.modules.get(getattr(value, '__module__', ''))
                    if local_path(getattr(module, '__file__', None)) is not None:
                        cls(value)
        for path in self.source_topic.rglob('*.py'):
            files[str(path)] = sha(path.read_bytes())
        files[str(HERE/'strong_prefix_evaluation_cache.py')] = SELF_SHA
        return dict(files=dict(sorted(files.items())), compiled_functions=dict(sorted(code.items())),
            adapter_transforms=encode(self.adapter.TRANSFORMS))

    def object_identity(self, obj):
        names = ('M','nt','q','n','base_mode','cfg','port','ref_coeff','ref_frequencies',
            '_neck_knots','chart_breaks','_special_layout','_strong_target',
            '_strong_constraint_weights','pscale','iz')
        result = {name:encode(getattr(obj,name)) for name in names if hasattr(obj,name)}
        # The bridge is derived from full port/cfg; bind its scalar mathematical
        # fields too, while rejecting any unhandled callable/object silently.
        bridge = getattr(obj, 'bridge', None)
        if bridge is not None:
            result['bridge_scalars'] = encode({k:v for k,v in vars(bridge).items()
                if isinstance(v,(str,bool,int,float,type(None)))})
        return result

    def initialize(self, obj):
        if self.identity is not None:
            return
        import scipy
        np = self.np
        runtime = dict(python=sys.version, implementation=platform.python_implementation(),
            numpy=np.__version__, scipy=scipy.__version__, platform=sys.platform,
            machine=platform.machine(), byteorder=sys.byteorder,
            cpu_features=getattr(np._core._multiarray_umath, '__cpu_features__', {}),
            selected_threads={name:os.environ.get(name) for name in
                ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS')})
        self.identity = dict(schema='actual-prefix-complete-call-v1',
            source=self.source_closure(obj), runtime=runtime,
            batch_sizes=self.batch_sizes,
            cached_operations=['fun complete output','fun_jac complete state and parameter outputs'],
            mathematical_side_effect_restore='select(full p); flow() baseline physical controls',
            no_boundary_or_tail_or_acceptance_cache=True,
            diagnostic_counts_and_internal_memoization_warmth_not_replayed=True)
        data = canonical(self.identity)
        self.identity_sha = sha(data)
        self.directory = self.root/self.identity_sha
        atomic_new(self.directory/'identity.json', data+b'\n')
        self.bytes = sum(p.stat().st_size for p in self.root.glob('*/*.bin.gz'))
        self.event('prefix_cache_identity', identity_sha256=self.identity_sha,
            directory=str(self.directory), existing_total_bytes=self.bytes,
            budget_bytes=self.budget, original_all_mathematical_gates_unchanged=True)

    def request(self, obj, kind, t, y, p):
        self.initialize(obj)
        descriptors = {name:describe(value) for name,value in (('t',t),('y',y),('p',p))}
        request = dict(schema='actual-prefix-complete-call-v1', identity_sha256=self.identity_sha,
            operation=kind, object=self.object_identity(obj), inputs=descriptors)
        return sha(canonical(request)), request

    def load(self, path, key, request):
        payload = gzip.decompress(path.read_bytes())
        if not payload.startswith(MAGIC):
            raise ValueError('Prefix cache magic differs')
        offset = len(MAGIC)
        length = struct.unpack('<Q',payload[offset:offset+8])[0]
        offset += 8
        record = json.loads(payload[offset:offset+length]);offset += length
        if record['key'] != key or record['request'] != request:
            raise ValueError('Complete prefix cache request/key mismatch')
        outputs = []
        for collection in ('inputs','outputs'):
            for item in record[collection]:
                size = item['array']['bytes']
                block = payload[offset:offset+size];offset += size
                if len(block) != size or sha(block) != item['array']['C_bytes_sha256']:
                    raise ValueError('Cached input/output block digest differs')
                if collection == 'inputs' and request['inputs'][item['name']] != item['array']:
                    raise ValueError('Stored complete input descriptor differs')
                if collection == 'outputs':
                    outputs.append(restore_array(item['array'], block))
        if offset != len(payload):
            raise ValueError('Unexpected trailing prefix cache bytes')
        return tuple(outputs) if record['tuple_output'] else outputs[0]

    def save(self, path, key, request, inputs, result):
        sequence = result if isinstance(result, tuple) else (result,)
        records = dict(key=key, request=request, tuple_output=isinstance(result,tuple),
            inputs=[dict(name=name,array=describe(value)) for name,value in inputs],
            outputs=[dict(name=str(i),array=describe(value)) for i,value in enumerate(sequence)])
        if any(item['array'] != request['inputs'][item['name']] for item in records['inputs']):
            raise ValueError('Original mathematical callback mutated its input; cache contract rejected')
        sizes = sum(item['array']['bytes'] for group in ('inputs','outputs') for item in records[group])
        if sizes > 16*1024**2:
            self.stats['bypassed_size'] += 1
            return None
        header = canonical(records)
        blocks = [MAGIC,struct.pack('<Q',len(header)),header]
        blocks.extend(self.np.asarray(value).tobytes(order='C') for _,value in inputs)
        blocks.extend(self.np.asarray(value).tobytes(order='C') for value in sequence)
        compressed = gzip.compress(b''.join(blocks),compresslevel=1,mtime=0)
        if len(compressed) >= 5_000_000:
            self.stats['bypassed_size'] += 1
            return None
        if self.bytes+len(compressed) > self.budget:
            self.stats['bypassed_budget'] += 1
            return None
        try:
            atomic_new(path,compressed)
        except OSError as error:
            self.stats['write_errors'] += 1
            self.event('prefix_cache_optional_write_error',key=key,error=repr(error),
                original_computed_result_returned=True)
            return None
        self.bytes += len(compressed)
        self.stats['completed_writes'] += 1
        return dict(bytes=len(compressed),sha256=sha(compressed))

    def call(self, original, obj, kind, t, y, p):
        key,request = self.request(obj,kind,t,y,p)
        path = self.directory/(key+'.bin.gz')
        if path.exists():
            result = self.load(path,key,request)
            obj.select(p)
            obj.flow()
            self.stats['restored_baseline_Flow'] += 1
            self.stats['hits'] += 1
            self.event('prefix_cache_call',kind=kind,key=key,hit=True,points=len(t))
            return result
        self.stats['misses'] += 1
        result = original(obj,t,y,p)
        record = self.save(path,key,request,(('t',t),('y',y),('p',p)),result)
        self.event('prefix_cache_call',kind=kind,key=key,hit=False,points=len(t),written=record)
        return result

    def install_class(self, cls):
        owner = self
        for kind in ('fun','fun_jac'):
            original = getattr(cls,kind)
            self.originals[kind] = original
            self.methods.append((cls,kind,original))
            def make(method, name):
                @functools.wraps(method)
                def wrapped(obj,t,y,p):
                    return owner.call(method,obj,name,t,y,p)
                return wrapped
            setattr(cls,kind,make(original,kind))

    def inspect(self,obj,x,y,p):
        """Three genuine physical points, complete J and PJ, no BVP or worker."""
        np=self.np
        indices=np.array([1,len(x)//2,len(x)-2])
        t=np.asarray(x[indices]).copy();Y=np.asarray(y[:,indices]).copy();P=p.copy()
        checks={};details={}
        for name in ('fun','fun_jac'):
            original=self.originals[name]
            uncached=original(obj,t,Y,P)
            first=getattr(obj,name)(t,Y,P)
            second=getattr(obj,name)(t,Y,P)
            a=uncached if isinstance(uncached,tuple) else (uncached,)
            b=first if isinstance(first,tuple) else (first,)
            c=second if isinstance(second,tuple) else (second,)
            checks[name+'_complete_original_miss_hit_byte_identical']=len(a)==len(b)==len(c) and all(
                describe(u)==describe(v)==describe(w) for u,v,w in zip(a,b,c))
            checks[name+'_selected_parameters_restored']=np.array_equal(obj.controls,P)
            expected=tuple(map(float,P[obj.M:obj.M+3]))
            checks[name+'_baseline_Flow_restored']=obj._flow_key==expected
            details[name]=[describe(v) for v in a]
        baseline_key,_=self.request(obj,'fun',t,Y,P)
        for name in ('t','y','p'):
            ta,ya,pa=t.copy(),Y.copy(),P.copy()
            value={'t':ta,'y':ya,'p':pa}[name]
            value.flat[0]=np.nextafter(value.flat[0],np.inf)
            key,_=self.request(obj,'fun',ta,ya,pa)
            checks[name+'_one_ULP_change_misses']=key!=baseline_key
        changed=P.copy();changed[obj.M]+=1e-7
        before=self.stats['misses']
        changed_original=self.originals['fun'](obj,t,Y,changed)
        changed_cached=obj.fun(t,Y,changed)
        checks['geometry_parameter_change_actual_miss']=self.stats['misses']==before+1
        checks['geometry_parameter_change_complete_RHS_identical']=describe(changed_original)==describe(changed_cached)
        obj.select(P);obj.flow()
        original_knots=obj._neck_knots
        obj._neck_knots=original_knots.copy();obj._neck_knots[1]=np.nextafter(obj._neck_knots[1],np.inf)
        changed_key,_=self.request(obj,'fun',t,Y,P)
        obj._neck_knots=original_knots
        checks['reference_chart_one_ULP_change_misses']=changed_key!=baseline_key
        original_cfg=obj.cfg
        obj.cfg=dict(original_cfg);obj.cfg['vu']=np.nextafter(obj.cfg['vu'],np.inf)
        changed_key,_=self.request(obj,'fun',t,Y,P)
        obj.cfg=original_cfg
        checks['physical_profile_one_ULP_change_misses']=changed_key!=baseline_key
        negative=np.array([-0.,1.],dtype=float)
        checks['negative_zero_binary_roundtrip']=describe(restore_array(describe(negative),negative.tobytes()))==describe(negative)
        record=dict(scope='Actual three-point complete fun/J/PJ cache equivalence; no Newton, RMS acceptance, or Node.',
            finished=True,passed=all(checks.values()),checks=checks,indices=indices.tolist(),
            nodes=len(x),modes=obj.M,parameters=len(P),field_dimension=obj.n,
            identity_sha256=self.identity_sha,identity_file=str(self.directory/'identity.json'),
            outputs=details,cache_statistics=dict(self.stats),source_sha256=SELF_SHA,
            worker_processes_started=0,new_solution=False)
        path=Path(self.configuration['inspect_output'])
        atomic_new(path,json.dumps(record,indent=2,allow_nan=False).encode()+b'\n')
        self.event('prefix_cache_actual_inspection',passed=record['passed'],path=str(path))
        if not record['passed']:
            raise ValueError('Actual prefix complete-call cache check failed')
        raise InspectionComplete()

    def finish(self):
        if self.closed:
            return
        for cls,kind,original in reversed(self.methods):
            setattr(cls,kind,original)
        record=dict(scope=__doc__,configuration=self.configuration,
            identity_sha256=self.identity_sha,cache_directory=str(self.directory),
            statistics=self.stats,observed_cache_bytes=self.bytes,seconds=time.monotonic()-self.started,
            no_boundary_tail_or_final_acceptance_cached=True,source_sha256=SELF_SHA)
        path=self.out.with_name(self.out.name+'-prefix-cache-summary.json')
        path.write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
        self.closed=True
