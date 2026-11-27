#!/usr/bin/env python3
"""Strict plain-detached reuse of complete meridian integration values.

Only already evaluated numerical integration data and complete corrected
integration values are reusable. Every field request still invokes the
original full implicit-chain interface. Direct query jets and query partial
integrals retain the original formulas. Active or unknown tracking states
always use the complete original path. Numerical execution is Actions only.
"""
from collections import OrderedDict
import hashlib
import json
import math
import os
from pathlib import Path
import time

SCHEMA = 'complete-fixed-fejer-plain-detached-meridian-value-reuse-v1'
ENDPOINT_SCHEMA = 'complete-fixed-fejer-detached-meridian-values-normal-layer-v1'
PARENT_NORMAL_SOURCE_SHA256 = '42b205ee34af4233002cec3d782acd78ed72a38f6013c1b931b3892f55d73e10'
BASE_SOURCE_SHA256 = '552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3'
CLOSURE_VALUE_SOURCE_SHA256 = '2889fef0d09a32c3f609f9a4e100efb1b136070dad77c8104204b552a867c4e0'
SOURCE_ROLE = 'detached_meridian_values'
CACHE_LIMIT_BYTES = 256*1024*1024
COUNTER_KEYS = (
    'calls_started','calls_returned','calls_failed',
    'field_calls_started','field_calls_returned','field_calls_failed',
    'integration_calls_started','integration_calls_returned','integration_calls_failed',
    'eligible_calls','bypassed_calls','caller_point_word_comparisons',
    'caller_point_word_mismatches','point_entries','point_exits',
    'point_entry_full_word_hashes','point_exit_full_word_hashes',
    'complete_carrier_word_reads','carrier_changes','optional_cache_failures',
    'input_requests','input_hits','input_misses','input_original_returns',
    'corrected_requests','corrected_hits','corrected_misses',
    'corrected_original_returns','prefix_original_returns',
    'query_partial_integrals','original_base_integrals',
    'input_entries_stored','corrected_entries_stored','cache_evictions',
    'oversize_entries_not_stored','peak_cache_payload_bytes')
TIME_KEYS = ('point_binding_seconds','carrier_key_seconds','optional_cache_seconds')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific meridian integration values require public repository Actions')


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()


def _copy(value):
    return json.loads(json.dumps(value,allow_nan=False))


def definition():
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        parent_complete_normal_source_sha256=PARENT_NORMAL_SOURCE_SHA256,
        complete_base_source_sha256=BASE_SOURCE_SHA256,
        complete_closure_value_source_sha256=CLOSURE_VALUE_SOURCE_SHA256,
        endpoint_schema=ENDPOINT_SCHEMA,maximum_retained_cache_payload_bytes=CACHE_LIMIT_BYTES,
        cache_scope='one current immutable complete point owner and the same full model, sources and actual carrier words',
        angle_key='all ordered finite binary64 phi words, shape and exact requested angular order; no sorting, periodic identification or subbatch slicing',
        input_key='complete current caller words equal the selected readonly owner, full carrier words, ordered phi and order',
        corrected_key='input key plus every actual returned six-control angular-jet word, full shape/stride/offset; third slots retained even for first order',
        input_values='complete integration meridians, all three endpoint/reference jets, W, angular node jets and rho0',
        corrected_values='complete corrected integration jets and the original cell/cumsum prefix and centred total reductions',
        direct_query_jets_original=True,query_partial_integral_original=True,
        original_implicit_jet_interface_called_for_every_field=True,
        original_stage_equations_roots_angular_solves_retained=True,
        original_forced_stage_and_final_closure_rereads_retained=True,
        active_parameter_J_and_Jtranspose_use_original_complete_path=True,
        no_grad_alone_sufficient=False,inference_mode_bypassed=True,
        forward_dual_functorch_dispatch_autocast_and_unknown_bypassed=True,
        whole_caller_point_words_compared_on_each_eligible_public_call=True,
        selected_point_array_equal_rule_unchanged=True,
        signed_zero_word_mismatch_bypasses_optional_cache=True,
        private_cache_values_never_exposed_without_clone=True,
        point_change_discards_all_cached_values=True,
        allocation_key_clone_or_capacity_failure_uses_original_complete_formulas=True,
        capacity_scope='sum of retained private tensor storage bytes; transient computations, key metadata and caller returned values are outside this optional retained-value limit',
        original_scientific_errors_not_suppressed=True,
        cache_capacity_changes_scientific_budget=False,
        unchanged_original_reduction_shape_and_order=True,
        fresh_cross_batch_bitwise_equality_claimed=False,
        measured_speedup_claimed=False,continuous_error_certificate_claimed=False)


def validate_metadata(value, *, model, source_by_role, current_full_point_sha256):
    """Pure complete-source attribution; no Torch/NumPy import or evaluation."""
    if (not isinstance(value,dict) or value.get('schema')!=SCHEMA
            or value.get('source_sha256')!=sha(__file__)
            or source_by_role.get(SOURCE_ROLE)!=sha(__file__)
            or value.get('definition')!=definition()
            or value.get('definition_identity_sha256')!=canonical(definition())
            or model.get('detached_meridian_value_reuse')!=definition()
            or model.get('schema')!=ENDPOINT_SCHEMA
            or canonical(model)!=value.get('actual_model_identity_sha256')
            or model.get('source_sha256')!=value.get('operator_source_sha256')):
        raise ValueError('Keep the complete meridian value source, actual model and policy')
    counts=value.get('counts')
    if (not isinstance(counts,dict) or set(counts)!=set(COUNTER_KEYS)
            or any(type(v) is not int or v<0 for v in counts.values())):
        raise ValueError('Keep every actual nonnegative integer meridian-cache count')
    for prefix in ('','field_','integration_'):
        if counts[prefix+'calls_started']!=counts[prefix+'calls_returned']+counts[prefix+'calls_failed']:
            raise ValueError('Every completed public call must retain its actual return or failure')
    if (counts['calls_started']!=counts['field_calls_started']+counts['integration_calls_started']
            or counts['eligible_calls']+counts['bypassed_calls']>counts['calls_started']
            or counts['input_hits']+counts['input_misses']!=counts['input_requests']
            or counts['corrected_hits']+counts['corrected_misses']!=counts['corrected_requests']
            or counts['peak_cache_payload_bytes']>CACHE_LIMIT_BYTES):
        raise ValueError('Logical cache requests, actual hits/misses and capacity must reconcile')
    timing=value.get('timing_seconds')
    if (not isinstance(timing,dict) or set(timing)!=set(TIME_KEYS)
            or any(type(v) not in (int,float) or not math.isfinite(v) or v<0
                   for v in timing.values())):
        raise ValueError('Keep the actual finite nonnegative cache bookkeeping times')
    retained=value.get('retained')
    if (not isinstance(retained,dict)
            or any(type(retained.get(k)) is not int or retained[k]<0
                   for k in ('input_entries','corrected_entries','payload_bytes'))
            or retained['payload_bytes']>CACHE_LIMIT_BYTES):
        raise ValueError('Report the actual current retained entries and payload bytes')
    for name in ('last_call','last_point_exit'):
        item=value.get(name)
        if item is not None and (not isinstance(item,dict)
                or not isinstance(item.get('own_full_point_sha256'),(str,type(None)))):
            raise ValueError('Keep each record own point; do not fill it from the current field')
    last=value.get('last_call')
    if last is not None:
        if (type(last.get('ordinal')) is not int or not 1<=last['ordinal']<=counts['calls_started']
                or last.get('kind') not in ('field','integration')
                or type(last.get('completed')) is not bool
                or last.get('status') not in ('returned','failed')):
            raise ValueError('Keep the last actual complete call status')
        for layer in ('input_reuse','corrected_reuse'):
            r=last.get(layer)
            if r is None:
                continue
            if (not isinstance(r,dict) or r.get('origin') not in ('original','cache')
                    or type(r.get('origin_call_ordinal')) is not int
                    or not 1<=r['origin_call_ordinal']<=last['ordinal']
                    or (r['origin']=='cache' and r['origin_call_ordinal']>=last['ordinal'])
                    or not isinstance(r.get('complete_key_sha256'),str)
                    or not isinstance(r.get('value_words_sha256'),str)):
                raise ValueError('A cache return must bind a prior complete original result and its full key')
    result=_copy(value)
    result['last_call_matches_current_full_point']=(last is not None
        and last['own_full_point_sha256'] is not None
        and last['own_full_point_sha256']==current_full_point_sha256)
    result['retained_point_matches_current_full_point']=(
        retained.get('own_full_point_sha256') is not None
        and retained.get('own_full_point_sha256')==current_full_point_sha256)
    return result


class OptionalReuseUnavailable(RuntimeError):
    pass


class DetachedMeridianValues:
    def __init__(self,q,*,closure_value_module):
        require_actions()
        global np,torch
        import numpy as np
        import torch
        self.q=q
        self.module=closure_value_module
        self.definition=definition()
        self.operator_source=sha(q.fields_torch.__func__.__code__.co_filename)
        if (sha(closure_value_module.__file__)!=CLOSURE_VALUE_SOURCE_SHA256
                or q.model.get('schema')!=ENDPOINT_SCHEMA
                or q.model.get('source_sha256')!=self.operator_source
                or q.fields_torch.__func__.__globals__.get('MERIDIAN_VALUE_SOURCE_SHA256')!=sha(__file__)
                or q.model.get('detached_meridian_value_reuse')!=self.definition
                or canonical(q.model)!=q.identity
                or q.model.get('base_source_sha256')!=BASE_SOURCE_SHA256
                or q.base.model.get('source_sha256')!=BASE_SOURCE_SHA256
                or canonical(q.base.model)!=q.base.identity):
            raise ValueError('Bind this entire optional helper to the actual complete normal and base sources')
        self.identity=q.identity
        self.model=q.model
        self.base=q.base
        self.base_model=q.base.model
        self.base_identity=q.base.identity
        self.closure=q.detached_closure_values
        self.provider=q.base.parent_jet
        self.provider_model=self.provider.model
        self.provider_identity=self.provider.model_identity
        self.calibration=q.reference_calibration
        self.methods={}
        for name in ('_unpack_torch','_angular_nodes','_radial','_meridians','_parent',
                     '_parent_tensor','_integrate','make_query'):
            bound=getattr(q.base,name)
            function=getattr(bound,'__func__',bound)
            if sha(function.__code__.co_filename)!=BASE_SOURCE_SHA256:
                raise ValueError('The complete original meridian base method differs: '+name)
            self.methods[name]=function
        self.normal_methods={name:getattr(getattr(q,name),'__func__',getattr(q,name))
            for name in ('_meridian_data','fields_torch','_select_point','_core_and_cap',
                         '_W','_reference_data','_implicit_jet_value','_corrected_jets','_total')}
        self.require_original=q.fields_torch.__func__.__globals__['require_actions']
        self.tensor=q.fields_torch.__func__.__globals__['tensor']
        self.array_sha=q.fields_torch.__func__.__globals__['array_sha']
        self.cache=OrderedDict()
        self.cache_bytes=0
        self.point=None
        self.owner=None
        self.point_sha=None
        self.carrier=None
        self.carrier_generation=0
        self.last_call=None
        self.last_point_exit=None
        self.counts={name:0 for name in COUNTER_KEYS}
        self.times={name:0. for name in TIME_KEYS}

    def _source_binding(self):
        q=self.q
        self.closure._source_binding()
        if (q.base is not self.base or q.model is not self.model or q.identity!=self.identity
                or canonical(q.model)!=self.identity or q.base.model is not self.base_model
                or q.base.identity!=self.base_identity or canonical(q.base.model)!=self.base_identity
                or q.base.parent_jet is not self.provider
                or self.provider.model is not self.provider_model
                or self.provider.model_identity!=self.provider_identity
                or canonical(self.provider.model)!=self.provider_identity
                or q.reference_calibration is not self.calibration
                or any(getattr(getattr(q.base,name),'__func__',getattr(q.base,name)) is not fn
                       for name,fn in self.methods.items())
                or any(getattr(getattr(q,name),'__func__',getattr(q,name)) is not fn
                       for name,fn in self.normal_methods.items())):
            raise ValueError('Never cross complete source methods, current model, base, provider or calibration')

    def _begin(self,kind):
        self.counts['calls_started']+=1
        self.counts[kind+'_calls_started']+=1
        r=dict(ordinal=self.counts['calls_started'],kind=kind,completed=False,status=None,
            own_full_point_sha256=None,ordered_phi_hex=None,requested_order=None,
            bypass_reason=None,input_reuse=None,corrected_reuse=None,
            actual_failure=None,optional_failures=[])
        self.last_call=r
        return r

    def _finish(self,r,success,error=None):
        suffix='calls_returned' if success else 'calls_failed'
        self.counts[suffix]+=1
        self.counts[r['kind']+'_'+suffix]+=1
        r['completed']=bool(success)
        r['status']='returned' if success else 'failed'
        if error is not None:
            r['actual_failure']=(type(error).__name__+': '+str(error))[:1400]

    def _optional(self,r,label,error):
        self.counts['optional_cache_failures']+=1
        if len(r['optional_failures'])<8:
            r['optional_failures'].append(dict(operation=label,
                error=(type(error).__name__+': '+str(error))[:700]))

    def _drop_cache(self):
        self.counts['cache_evictions']+=len(self.cache)
        self.cache.clear()
        self.cache_bytes=0

    def _leave_point(self):
        if self.point is None:
            return
        r=dict(own_full_point_sha256=self.point_sha,complete_word_hash_matches=None,
            original_owner_identity_retained=False,actual_error=None)
        self.last_point_exit=r
        self.counts['point_exits']+=1
        try:
            self.module._immutable_point_owner(self.point,(self.q.free_size,),self.owner)
            r['original_owner_identity_retained']=True
            self.counts['point_exit_full_word_hashes']+=1
            r['complete_word_hash_matches']=self.array_sha(self.point)==self.point_sha
            if not r['complete_word_hash_matches']:
                raise ValueError('The immutable cache point changed its complete words')
        finally:
            self._drop_cache()
            self.point=self.owner=self.point_sha=self.carrier=None

    def close(self):
        require_actions()
        self._source_binding()
        self._leave_point()

    def _plain_any_tensor(self,value):
        if type(value) is not torch.Tensor:
            return False
        try:
            wrapped=getattr(getattr(torch._C,'_functorch',None),'is_functorch_wrapped_tensor',None)
            functional=getattr(torch,'_is_functional_tensor',None)
            if (not callable(wrapped) or not callable(functional) or wrapped(value) or functional(value)
                    or value.requires_grad or value.grad_fn is not None or value.device.type!='cpu'
                    or value.dtype not in (torch.float64,torch.int64) or value.layout!=torch.strided
                    or torch.autograd.forward_ad.unpack_dual(value).tangent is not None):
                return False
            int(value._version)
            return True
        except (AttributeError,MemoryError,RuntimeError,TypeError):
            return False

    def _plain_query_tree(self,value):
        if isinstance(value,torch.Tensor):
            return self._plain_any_tensor(value)
        if type(value) is np.ndarray:
            return value.dtype.isnative and value.dtype.kind in 'biuf'
        if type(value) is dict:
            return all(type(k) is str and self._plain_query_tree(v) for k,v in value.items())
        if type(value) in (tuple,list):
            return all(self._plain_query_tree(v) for v in value)
        return value is None or type(value) in (bool,int,str,float)

    def _words(self,value):
        if isinstance(value,torch.Tensor):
            if not self._plain_any_tensor(value):
                raise OptionalReuseUnavailable('A complete carrier tensor is not plain and detached')
            a=value.detach().contiguous().numpy()
            return ('tensor',str(a.dtype),tuple(a.shape),tuple(value.stride()),
                    int(value.storage_offset()),a.tobytes(order='C'))
        if type(value) is np.ndarray:
            if value.dtype.kind not in 'biuf' or not value.dtype.isnative:
                raise OptionalReuseUnavailable('Unexpected complete carrier array dtype')
            if value.dtype.kind=='f' and not bool(np.isfinite(value).all()):
                raise OptionalReuseUnavailable('Nonfinite optional carrier words')
            return ('array',str(value.dtype),tuple(value.shape),tuple(value.strides),
                    value.tobytes(order='C'))
        if type(value) is dict:
            if any(type(k) is not str for k in value):
                raise OptionalReuseUnavailable('Use original named carrier keys')
            return ('dict',tuple((k,self._words(value[k])) for k in sorted(value)))
        if type(value) in (tuple,list):
            return (type(value).__name__,tuple(self._words(v) for v in value))
        if value is None or type(value) in (bool,int,str):
            return (type(value).__name__,value)
        if type(value) is float and math.isfinite(value):
            return ('float',value.hex())
        raise OptionalReuseUnavailable('Unknown carrier object; the original formula remains available')

    def _carrier_words(self):
        q=self.q
        self.counts['complete_carrier_word_reads']+=1
        return self._words(dict(mesh=q.mesh,gauss_u=q.gauss_u,gauss_w=q.gauss_w,
            integration_query=q.integration_query,fixed_core=q.fixed_core,parent_core=q.parent_core,
            frequencies=q.freq,core_frequencies=q.qfreq,radial_free=q.radial_free,
            radial_free_tensor=q.base._radial_free_torch,frozen_Q=q._frozen_Q0,
            bubble_nodes=[[str(v) for v in row] for row in q.bubble_nodes],
            gamma_nodes=[str(v) for v in q.gamma_nodes],
            normal_steps=list(q.normal_step_carriers),S=float(q.S),R=float(q.R),
            M=int(q.M),J=int(q.J),n=int(q.n),free_size=int(q.free_size),
            integration_order=int(q.integration_order),root_iterations=int(q.root_iterations),
            root_tolerance=float(q.root_tolerance)))

    def _eligible(self,x,phi,order,r):
        reason=self.module._environment_reason()
        if reason is not None:
            return reason,None
        if not self.module._plain_tensor(x) or tuple(x.shape)!=(self.q.free_size,):
            return 'caller_is_not_the_complete_plain_detached_CPU_float64_point',None
        started=time.monotonic()
        try:
            point=self.q._current_x
            try:
                owner=self.module._immutable_point_owner(point,(self.q.free_size,))
            except ValueError:
                return 'selected_point_has_no_exact_immutable_bytes_owner',None
            caller=x.detach().numpy()
            if (caller.dtype!=np.dtype('float64') or not caller.dtype.isnative
                    or caller.ndim!=1 or not caller.flags.c_contiguous):
                return 'caller_complete_point_layout_unavailable',None
            self.counts['caller_point_word_comparisons']+=1
            if not np.array_equal(caller.view(np.uint64),point.view(np.uint64)):
                self.counts['caller_point_word_mismatches']+=1
                return 'caller_and_selected_owner_differ_in_complete_binary64_words',None
            if self.owner is not owner or self.point is not point:
                self._leave_point()
                self.counts['point_entry_full_word_hashes']+=1
                observed=self.array_sha(point)
                if observed!=self.q._current_point_sha256:
                    raise ValueError('The selected complete point digest differs from its actual immutable words')
                self.point,self.owner,self.point_sha=point,owner,observed
                self.counts['point_entries']+=1
            elif self.point_sha!=self.q._current_point_sha256:
                raise ValueError('A retained immutable point cannot change its complete declared digest')
        except (MemoryError,RuntimeError) as error:
            self._optional(r,'complete optional point comparison',error)
            self._drop_cache()
            return 'complete_optional_point_comparison_unavailable',None
        finally:
            self.times['point_binding_seconds']+=time.monotonic()-started
        started=time.monotonic()
        try:
            carrier=self._carrier_words()
            if self.carrier is None or carrier!=self.carrier:
                if self.carrier is not None:
                    self.counts['carrier_changes']+=1
                    self._drop_cache()
                self.carrier=carrier
                self.carrier_generation+=1
            key=(self.carrier_generation,tuple(phi.shape),tuple(phi.strides),phi.tobytes(order='C'),order)
            return None,key
        except (OptionalReuseUnavailable,MemoryError,RuntimeError) as error:
            self._optional(r,'complete optional carrier key',error)
            return 'complete_optional_carrier_key_unavailable',None
        finally:
            self.times['carrier_key_seconds']+=time.monotonic()-started

    def _payload_bytes(self,value,*,actual_storage=False):
        if isinstance(value,torch.Tensor):
            if not self.module._plain_tensor(value):
                raise OptionalReuseUnavailable('Only complete plain detached float64 values may be retained')
            return (int(value.untyped_storage().nbytes()) if actual_storage
                    else int(value.numel())*int(value.element_size()))
        if type(value) is dict:
            return sum(self._payload_bytes(v,actual_storage=actual_storage) for v in value.values())
        if type(value) in (tuple,list):
            return sum(self._payload_bytes(v,actual_storage=actual_storage) for v in value)
        if value is None or type(value) in (bool,int,str,float):
            return 0
        raise OptionalReuseUnavailable('Do not retain unknown value objects')

    def _clone(self,value):
        if isinstance(value,torch.Tensor):
            if not self.module._plain_tensor(value) or not bool(torch.isfinite(value).all()):
                raise OptionalReuseUnavailable('Do not retain nonfinite or tracked numerical values')
            answer=value.clone(memory_format=torch.preserve_format)
            if tuple(answer.stride())!=tuple(value.stride()):
                raise OptionalReuseUnavailable('The optional clone changed the original tensor stride')
            return answer
        if type(value) is dict:
            return {k:self._clone(v) for k,v in value.items()}
        if type(value) is tuple:
            return tuple(self._clone(v) for v in value)
        if type(value) is list:
            return [self._clone(v) for v in value]
        if value is None or type(value) in (bool,int,str,float):
            return value
        raise OptionalReuseUnavailable('Only the full known original value tree is reusable')

    def _key_digest(self,key):
        h=hashlib.sha256()
        def visit(v):
            if type(v) is bytes:
                h.update(b'bytes');h.update(str(len(v)).encode());h.update(b':');h.update(v)
            elif type(v) in (tuple,list):
                h.update(type(v).__name__.encode())
                for w in v:visit(w)
            else:
                h.update(json.dumps(v,sort_keys=True,separators=(',',':'),allow_nan=False).encode())
        visit((self.identity,self.operator_source,self.point_sha,key))
        return h.hexdigest()

    def _lookup(self,kind,key,r):
        self.counts[kind+'_requests']+=1
        try:
            entry=self.cache.get((kind,key))
        except (MemoryError,RuntimeError) as error:
            self._optional(r,'lookup complete optional '+kind,error)
            self.counts[kind+'_misses']+=1
            return None
        if entry is not None:
            try:
                if self.module._data_token(entry['value'])!=entry['token']:
                    raise OptionalReuseUnavailable('A private retained tensor version or object changed')
                value=self._clone(entry['value'])
                self.cache.move_to_end((kind,key))
            except (OptionalReuseUnavailable,self.module.CacheUnavailable,MemoryError,RuntimeError) as error:
                self._optional(r,'clone complete retained '+kind,error)
                old=self.cache.pop((kind,key))
                self.cache_bytes-=old['bytes']
                self.counts['cache_evictions']+=1
            else:
                self.counts[kind+'_hits']+=1
                r[kind+'_reuse']=dict(origin='cache',origin_call_ordinal=entry['ordinal'],
                    complete_key_sha256=entry['key_sha256'],
                    value_words_sha256=entry['value_sha256'])
                return value
        self.counts[kind+'_misses']+=1
        return None

    def _store(self,kind,key,value,r):
        started=time.monotonic()
        try:
            size=self._payload_bytes(value)
            if size>CACHE_LIMIT_BYTES:
                self.counts['oversize_entries_not_stored']+=1
                return
            while self.cache and self.cache_bytes+size>CACHE_LIMIT_BYTES:
                _,old=self.cache.popitem(last=False)
                self.cache_bytes-=old['bytes']
                self.counts['cache_evictions']+=1
            saved=self._clone(value)
            size=self._payload_bytes(saved,actual_storage=True)
            if size>CACHE_LIMIT_BYTES:
                self.counts['oversize_entries_not_stored']+=1
                return
            while self.cache and self.cache_bytes+size>CACHE_LIMIT_BYTES:
                _,old=self.cache.popitem(last=False)
                self.cache_bytes-=old['bytes']
                self.counts['cache_evictions']+=1
            token=self.module._data_token(saved)
            value_sha=self.module._data_words_digest(saved)
            key_sha=self._key_digest(key)
            existing=self.cache.pop((kind,key),None)
            if existing is not None:
                self.cache_bytes-=existing['bytes']
            self.cache[(kind,key)]=dict(value=saved,token=token,bytes=size,
                ordinal=r['ordinal'],key_sha256=key_sha,value_sha256=value_sha)
            self.cache_bytes+=size
            self.counts[kind+'_entries_stored']+=1
            self.counts['peak_cache_payload_bytes']=max(
                self.counts['peak_cache_payload_bytes'],self.cache_bytes)
            r[kind+'_reuse']=dict(origin='original',origin_call_ordinal=r['ordinal'],
                complete_key_sha256=key_sha,value_words_sha256=value_sha)
        except (OptionalReuseUnavailable,self.module.CacheUnavailable,MemoryError,RuntimeError) as error:
            self._drop_cache()
            self._optional(r,'retain complete original '+kind,error)
        finally:
            self.times['optional_cache_seconds']+=time.monotonic()-started

    def _raw_inputs(self,x,phi,curvature,query=None,query_label='arbitrary'):
        q=self.q
        core,jets,height=q.base._unpack_torch(x)
        nodes=q.base._angular_nodes(jets,phi,0)
        nodes_p=q.base._angular_nodes(jets,phi,1)
        nodes_pp=q.base._angular_nodes(jets,phi,2) if curvature else None
        integration=q.base._meridians(nodes,nodes_p,nodes_pp,
            q.integration_query,phi,'integration',curvature)
        direct=(None if query is None else q.base._meridians(
            nodes,nodes_p,nodes_pp,query,phi,query_label,curvature))
        core_jets,cap_jets,rho0=q._core_and_cap(core,height,phi)
        for values in (integration,) if direct is None else (integration,direct):
            if any(not bool(torch.isfinite(value.detach()).all()) for value in values.values()):
                q._fail('Nonfinite actual direct-reference meridian jets')
        order=2 if curvature else 1
        reference,reference_core,reference_cap=q._reference_data(phi)
        data=dict(meridians=integration,core=core_jets,cap=cap_jets,
            reference=reference,reference_core=reference_core,reference_cap=reference_cap,
            W=q._W(q.integration_query,phi),order=order)
        payload=dict(data=data,nodes=(nodes,nodes_p,nodes_pp),rho0=rho0)
        Wdirect=None if query is None else q._W(query,phi)
        self.counts['input_original_returns']+=1
        return payload,direct,Wdirect

    def meridian_data(self,x,query,phi,curvature,query_label):
        # This exact original fallback does not select a point or reuse values.
        self.require_original()
        self._source_binding()
        payload,direct,Wdirect=self._raw_inputs(x,phi,curvature,query,query_label)
        return payload['data'],direct,Wdirect,payload['rho0']

    def _inputs(self,x,phi,curvature,key,r,query=None,query_label='arbitrary'):
        payload=self._lookup('input',key,r) if key is not None else None
        if payload is None:
            payload,direct,Wdirect=self._raw_inputs(x,phi,curvature,query,query_label)
            if key is not None:
                self._store('input',key,payload,r)
            return payload,direct,Wdirect
        if query is None:
            return payload,None,None
        nodes,nodes_p,nodes_pp=payload['nodes']
        direct=self.q.base._meridians(nodes,nodes_p,nodes_pp,query,phi,query_label,curvature)
        if any(not bool(torch.isfinite(v.detach()).all()) for v in direct.values()):
            self.q._fail('Nonfinite actual direct-reference meridian jets')
        return payload,direct,self.q._W(query,phi)

    def _original_integral_prefix(self,value):
        q=self.q
        block=value.reshape(q.J-1,q.integration_order,value.shape[-2],3)
        widths=self.tensor(np.diff(q.mesh))
        cell_total=(block*self.tensor(q.gauss_w)[None,:,None,None]).sum(1)*widths[:,None,None]
        prefix=torch.cat((torch.zeros_like(cell_total[:1]),torch.cumsum(cell_total,0)),0)
        return dict(block=block,prefix=prefix,total=prefix[-1])

    def _corrected(self,data,controls,order,input_key,r):
        key=None
        if input_key is not None:
            try:
                words=self.module._control_words(controls,order,int(controls.shape[0]))
                key=(input_key,words)
            except (self.module.CacheUnavailable,MemoryError,RuntimeError) as error:
                self._optional(r,'complete corrected-control key',error)
        cached=self._lookup('corrected',key,r) if key is not None else None
        if cached is not None:
            return cached,None
        integrated=self.q._corrected_jets(data['meridians'],data['W'],controls,order)
        self.counts['corrected_original_returns']+=1
        if key is None:
            return None,integrated
        try:
            values={}
            for j,name in enumerate(('T','Tp','Tpp')):
                if j>order:break
                item=self._original_integral_prefix(integrated[name])
                self.counts['prefix_original_returns']+=1
                item['centred_total']=self.q._total(integrated[name]-data['reference'][name])
                values[name]=item
        except (MemoryError,RuntimeError) as error:
            self._optional(r,'optional complete prefix construction',error)
            return None,integrated
        self._store('corrected',key,values,r)
        return values,None

    def _original_fields_selected(self,x,query,phi,curvature,query_label):
        q=self.q
        data,direct,Wdirect,rho0=self.meridian_data(x,query,phi,curvature,query_label)
        order=2 if curvature else 1
        controls=q._implicit_jet_value(data,phi,order,x)
        integrated=q._corrected_jets(data['meridians'],data['W'],controls,order)
        self.counts['corrected_original_returns']+=1
        requested=q._corrected_jets(direct,Wdirect,controls,order,need_s=curvature)
        result,defects,centered={},[],[]
        h,hp,hpp=query['h'],query['hp'],query['hpp']
        for j,(name,output) in enumerate(zip(('T','Tp','Tpp'),('F','Fphi','Fphiphi'))):
            if j>order:break
            integral,total=q.base._integrate(integrated[name],query)
            self.counts['original_base_integrals']+=1
            C,P=data['core'][j][None],data['cap'][j][None]
            defect=C-P+total[None]
            result[output]=(1-h)*P+h*C+integral-(1-h)*total[None]
            defects.append(defect)
            centered.append((data['core'][j]-data['reference_core'][j])
                -(data['cap'][j]-data['reference_cap'][j])
                +q._total(integrated[name]-data['reference'][name]))
        result['Fs']=requested['T']+hp*defects[0]
        if curvature:
            result['Fss']=requested['Ts']+hpp*defects[0]
            result['Fsphi']=requested['Tp']+hp*defects[1]
        result['rho0']=rho0
        result['closure_delta']=defects[0][0]
        result['centered_closure_residual']=centered[0]
        if any(not bool(torch.isfinite(v.detach()).all()) for v in result.values()):
            q._fail('Nonfinite complete reference-centred physical field with its full lift')
        q.reference_calibration.observe_field(defects,centered)
        q.counts['evaluated_field_points']+=len(query['cells'])*len(phi)
        return result

    def _prepare_call(self,x,phi,curvature,r,query=None):
        self.require_original()
        self._source_binding()
        self.q._select_point(x)
        if self.point is not None and self.q._current_x is not self.point:
            try:
                self._leave_point()
            except (MemoryError,RuntimeError) as error:
                if self.last_point_exit is not None:
                    self.last_point_exit['actual_error']=(type(error).__name__+': '+str(error))[:700]
                self._optional(r,'discard previous immutable point values',error)
        phi=np.asarray(phi,dtype=float)
        if phi.ndim!=1 or not len(phi) or not np.isfinite(phi).all():
            raise ValueError('Use an actual finite one-dimensional material-chart angle list')
        order=2 if curvature else 1
        r['own_full_point_sha256']=self.q._current_point_sha256
        r['ordered_phi_hex']=[float(v).hex() for v in phi]
        r['requested_order']=order
        reason,key=self._eligible(x,phi,order,r)
        if reason is None and query is not None:
            try:
                if not self._plain_query_tree(query):
                    reason,key='direct_query_contains_tracked_or_unknown_objects',None
            except (MemoryError,RuntimeError) as error:
                self._optional(r,'optional direct-query tracking probe',error)
                reason,key='direct_query_tracking_probe_unavailable',None
        if reason is None:
            self.counts['eligible_calls']+=1
        else:
            self.counts['bypassed_calls']+=1
            r['bypass_reason']=reason
        return phi,order,key

    def integration_data(self,x,phi,*,curvature=True):
        r=self._begin('integration')
        try:
            phi,order,key=self._prepare_call(x,phi,curvature,r)
            payload,_,_=self._inputs(x,phi,curvature,key,r)
            answer=payload['data']
        except BaseException as error:
            self._finish(r,False,error)
            raise
        self._finish(r,True)
        return answer

    def fields_torch(self,x,query,phi,*,curvature=True,query_label='arbitrary'):
        r=self._begin('field')
        try:
            phi,order,key=self._prepare_call(x,phi,curvature,r,query=query)
            if key is None:
                answer=self._original_fields_selected(x,query,phi,curvature,query_label)
            else:
                payload,direct,Wdirect=self._inputs(x,phi,curvature,key,r,query,query_label)
                data,rho0=payload['data'],payload['rho0']
                # Always retain the original whole root/upgrade interface.
                controls=self.q._implicit_jet_value(data,phi,order,x)
                cached,integrated=self._corrected(data,controls,order,key,r)
                requested=self.q._corrected_jets(direct,Wdirect,controls,order,need_s=curvature)
                result,defects,centered={},[],[]
                h,hp,hpp=query['h'],query['hp'],query['hpp']
                for j,(name,output) in enumerate(zip(('T','Tp','Tpp'),('F','Fphi','Fphiphi'))):
                    if j>order:break
                    if cached is None:
                        integral,total=self.q.base._integrate(integrated[name],query)
                        self.counts['original_base_integrals']+=1
                        centred_total=self.q._total(integrated[name]-data['reference'][name])
                    else:
                        item=cached[name]
                        partial=torch.einsum('pq,pqaj->paj',query['partial'],
                            item['block'][query['cells_torch']])
                        integral=item['prefix'][query['cells_torch']]+partial
                        total=item['total']
                        centred_total=item['centred_total']
                        self.counts['query_partial_integrals']+=1
                    C,P=data['core'][j][None],data['cap'][j][None]
                    defect=C-P+total[None]
                    result[output]=(1-h)*P+h*C+integral-(1-h)*total[None]
                    defects.append(defect)
                    centered.append((data['core'][j]-data['reference_core'][j])
                        -(data['cap'][j]-data['reference_cap'][j])+centred_total)
                result['Fs']=requested['T']+hp*defects[0]
                if curvature:
                    result['Fss']=requested['Ts']+hpp*defects[0]
                    result['Fsphi']=requested['Tp']+hp*defects[1]
                result['rho0']=rho0
                result['closure_delta']=defects[0][0]
                result['centered_closure_residual']=centered[0]
                if any(not bool(torch.isfinite(v.detach()).all()) for v in result.values()):
                    self.q._fail('Nonfinite complete reference-centred physical field with its full lift')
                self.q.reference_calibration.observe_field(defects,centered)
                self.q.counts['evaluated_field_points']+=len(query['cells'])*len(phi)
                answer=result
        except BaseException as error:
            self._finish(r,False,error)
            raise
        self._finish(r,True)
        return answer

    def metadata(self):
        entries=list(self.cache)
        return dict(schema=SCHEMA,source_sha256=sha(__file__),definition=self.definition,
            definition_identity_sha256=canonical(self.definition),
            actual_model_identity_sha256=self.identity,operator_source_sha256=self.operator_source,
            counts=dict(self.counts),timing_seconds=dict(self.times),
            retained=dict(own_full_point_sha256=self.point_sha,
                input_entries=sum(k[0]=='input' for k in entries),
                corrected_entries=sum(k[0]=='corrected' for k in entries),
                payload_bytes=self.cache_bytes),
            last_call=_copy(self.last_call),last_point_exit=_copy(self.last_point_exit),
            count_scope='actual optional reuse bookkeeping plus separately counted complete original computations; no inferred performance or scientific success',
            continuous_or_working_error_bound_produced=False)
