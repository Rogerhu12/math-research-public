#!/usr/bin/env python3
"""Actual-margin inequalities with current protected-neighborhood representatives.

Every retained row is C_i z <= b_i with
 C_i = .03*(D sign(kappa) d_kappa + abs(kappa) d_D) T / norm_i,
 b_i = (numerical_safety - .03*D*abs(kappa))/norm_i.
No row is silently changed into a homogeneous tangent equality.
The bounded linear working set is separate from permanent nonlinear memory.
"""
from pathlib import Path
import mmap

import numpy as np


# Complete returned numerical pullbacks are optional, point-local values.
# This scope never stores a Torch graph, computes a missing jet, changes the
# selected row list, or evaluates a new geometric point.
import hashlib
import json
import math
from collections import Counter, OrderedDict

_CURVATURE_CACHE_SCHEMA = 'complete-same-point-returned-curvature-pullback-cache-v1'
_CURVATURE_CACHE_LIMIT = 64 * 1024 * 1024
_CURVATURE_CACHE_NORMAL_SHA256 = 'df08d84d5876eac3f7ca62d0be877afc8e0036ab9ef2d67634c100524c2a52ec'
_CURVATURE_CACHE_MERIDIAN_SHA256 = '2af2d12fbfda3baacbf589812df99db1c6a3cec36b6fcb5d2c321f3c6dbe074c'
_CURVATURE_COTANGENT_FIELDS = ('F','Fs','Fphi','Fss','Fsphi','Fphiphi')


def _curvature_cache_sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def _curvature_cache_canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()


def _curvature_cache_array_sha(value):
    value = np.ascontiguousarray(value)
    h = hashlib.sha256(str(value.dtype).encode())
    h.update(json.dumps(list(value.shape)).encode())
    h.update(value.tobytes())
    return h.hexdigest()


def _curvature_cache_words_sha(value):
    h = hashlib.sha256()
    def visit(v):
        if type(v) is bytes:
            h.update(b'bytes:');h.update(str(len(v)).encode());h.update(b':');h.update(v)
        elif type(v) in (tuple,list):
            h.update(type(v).__name__.encode());h.update(str(len(v)).encode());h.update(b':')
            for item in v:visit(item)
        else:
            h.update(json.dumps(v,sort_keys=True,separators=(',',':'),allow_nan=False).encode())
            h.update(b';')
    visit(value)
    return h.hexdigest()


def complete_curvature_pullback_cache_definition():
    return dict(schema=_CURVATURE_CACHE_SCHEMA,source_sha256=_curvature_cache_sha(__file__),
        maximum_retained_numerical_payload_bytes=_CURVATURE_CACHE_LIMIT,
        scope='one original build_inequality_rows call at one complete immutable field point',
        value='the actually returned complete native free-coordinate curvature pullback',
        key='all original literal call words and all six three-component cotangent words; current full point, model, complete source methods, carriers, actual query, reference values, selected roots and angular matrices',
        no_nearby_location_or_cotangent_merging=True,old_source_normal_sha256=_CURVATURE_CACHE_NORMAL_SHA256,
        old_source_meridian_helper_sha256=_CURVATURE_CACHE_MERIDIAN_SHA256,
        active_graph_or_derivative_tape_retained=False,outer_Torch_transforms_bypassed=True,
        original_point_vjp_runs_outside_any_new_no_grad_context=True,
        original_pullback_called_on_every_miss_or_unavailable_optional_key=True,
        original_radius_cache_and_selected_rows_unchanged=True,
        original_row_arithmetic_normalization_transpose_and_order_unchanged=True,
        source_or_capacity_failure_changes_scientific_budget=False,
        nonrepeated_numerical_pullbacks_not_stored=True,
        allocation_key_or_clone_failure_falls_back_to_original=True,
        numerical_payload_limit_excludes_original_output_transients_and_small_key_metadata=True,
        continuous_geometry_or_actual_speedup_claimed=False)


def validate_complete_curvature_pullback_cache(value, *, selected_rows,
                                                current_full_point_sha256,
                                                model_identity_sha256):
    """Pure source/record validation; it never evaluates a physical field."""
    if (not isinstance(value,dict) or value.get('definition')!=complete_curvature_pullback_cache_definition()
            or value.get('schema')!=_CURVATURE_CACHE_SCHEMA
            or value.get('complete_row_loop_returned') is not True
            or value.get('scope_closed') is not True
            or value.get('current_full_point_sha256')!=current_full_point_sha256
            or value.get('model_identity_sha256')!=model_identity_sha256):
        raise ValueError('Keep this complete numerical-cache source and its own actual row scope')
    counts = value.get('counts')
    keys = {'requests','original_pullback_attempts','original_pullback_returns','numerical_hits',
        'entries_stored','entries_evicted','entries_released_after_last_use',
        'unique_use_values_not_stored','oversize_values_not_stored','optional_failures',
        'peak_retained_numerical_payload_bytes','retained_numerical_payload_bytes'}
    if (not isinstance(counts,dict) or set(counts)!=keys
            or any(type(v) is not int or v<0 for v in counts.values())
            or counts['requests']!=selected_rows
            or counts['requests']!=counts['original_pullback_attempts']+counts['numerical_hits']
            or counts['original_pullback_attempts']!=counts['original_pullback_returns']
            or counts['retained_numerical_payload_bytes']!=0
            or counts['peak_retained_numerical_payload_bytes']>_CURVATURE_CACHE_LIMIT):
        raise ValueError('Keep every actual request, original return, numerical hit and payload bound')
    records = value.get('requests')
    if not isinstance(records,list) or len(records)!=selected_rows:
        raise ValueError('Keep every selected row pullback record in original row order')
    for index,item in enumerate(records):
        if (not isinstance(item,dict) or item.get('row_index')!=index
                or item.get('origin') not in ('original_complete_point_vjp','prior_complete_numerical_pullback')
                or item.get('original_returned') is not (item['origin']=='original_complete_point_vjp')):
            raise ValueError('A numerical hit is not another original point_vjp execution')
        if item['origin']=='prior_complete_numerical_pullback':
            prior = item.get('origin_row_index')
            if (type(prior) is not int or not 0<=prior<index
                    or records[prior].get('origin')!='original_complete_point_vjp'
                    or item.get('complete_key_sha256')!=records[prior].get('stored_complete_key_sha256')
                    or item.get('gradient_words_sha256')!=records[prior].get('gradient_words_sha256')):
                raise ValueError('A hit must bind a prior actual complete original result')
    return dict(value)


class _CompleteCurvaturePullbackCache:
    def __init__(self,q,x,prepared,geometry_module,point_module,candidates):
        self.q,self.x,self.prepared = q,x,prepared
        self.geometry,self.point_module = geometry_module,point_module
        self.cache,self.pending = OrderedDict(),None
        self.payload_bytes = 0
        self.enabled,self.closed = False,False
        self.definition = complete_curvature_pullback_cache_definition()
        names = ('requests','original_pullback_attempts','original_pullback_returns','numerical_hits',
            'entries_stored','entries_evicted','entries_released_after_last_use',
            'unique_use_values_not_stored','oversize_values_not_stored','optional_failures',
            'peak_retained_numerical_payload_bytes','retained_numerical_payload_bytes')
        self.counts = {name:0 for name in names}
        self.requests,self.failures = [],[]
        self.point_sha = getattr(q,'_current_point_sha256',None)
        self.model_sha = getattr(q,'identity',None)
        self.remaining = Counter()
        self.methods,self.sources,self.objects,self.links = [],{},[],[]
        try:
            self.helper = q.detached_meridian_values
            self.module = self.helper.module
            self.torch = q.point_vjp.__func__.__globals__['torch']
            if (_curvature_cache_sha(q.point_vjp.__func__.__code__.co_filename)!=_CURVATURE_CACHE_NORMAL_SHA256
                    or q.model.get('source_sha256')!=_CURVATURE_CACHE_NORMAL_SHA256
                    or _curvature_cache_sha(self.helper.fields_torch.__func__.__code__.co_filename)!=_CURVATURE_CACHE_MERIDIAN_SHA256):
                raise ValueError('The optional numerical cache is bound to its declared complete current source family')
            self.point = q._current_x
            self.owner = self.module._immutable_point_owner(self.point,(q.free_size,))
            self.links = [(q,name,getattr(q,name)) for name in (
                'base','analytic_normal_frame','analytic_stage_jacobian','frame_c1',
                'stage_matrices','adjacent_frames','reference_calibration',
                'detached_closure_values','detached_meridian_values')]
            self.links.append((q.base,'parent_jet',q.base.parent_jet))
            self.models = ((q,q.model,q.identity),(q.base,q.base.model,q.base.identity),
                (q.base.parent_jet,q.base.parent_jet.model,q.base.parent_jet.model_identity))
            for label,obj in (
                    ('normal',q),('base',q.base),('seed',q.base.parent_jet),
                    ('frame',q.analytic_normal_frame),('J3',q.analytic_stage_jacobian),
                    ('C1',q.frame_c1),('stage',q.stage_matrices),('adjacent',q.adjacent_frames),
                    ('calibration',q.reference_calibration),
                    ('closure',q.detached_closure_values),('meridian',self.helper),
                    ('geometry',geometry_module),('point_module',point_module)):
                self.objects.append((label,obj,type(obj)))
                for cls in type(obj).__mro__:
                    if cls is object:continue
                    for name,raw in vars(cls).items():
                        function = raw.__func__ if isinstance(raw,(staticmethod,classmethod)) else raw
                        if hasattr(function,'__code__'):
                            bound = getattr(obj,name)
                            actual = getattr(bound,'__func__',bound)
                            if actual is not function:continue
                            self.methods.append((obj,name,function))
                            path = function.__code__.co_filename
                            self.sources[path] = _curvature_cache_sha(path)
            self.sources[__file__] = self.definition['source_sha256']
            for candidate in candidates:
                self.remaining[self._basic_key(candidate)[0]] += 1
            self._scope_guard()
            self.enabled = True
        except Exception as error:
            self._optional('bind optional complete numerical scope',error)
            self._discard()

    def _optional(self,operation,error):
        self.counts['optional_failures'] += 1
        if len(self.failures)<8:
            self.failures.append(dict(operation=operation,
                error=(type(error).__name__+': '+str(error))[:900]))

    def _discard(self):
        self.counts['entries_evicted'] += len(self.cache)
        self.cache.clear()
        self.payload_bytes = 0

    def _mode(self):
        # The original numerical point_vjp deliberately builds an internal
        # reverse graph and returns NumPy. Only this internal reverse mode is
        # permitted; the guard below leaves it enabled for the original call.
        if not self.torch.is_grad_enabled():
            raise ValueError('Preserve the original point_vjp reverse-mode precondition')
        with self.torch.no_grad():
            reason = self.module._environment_reason()
        if reason is not None:
            raise ValueError('Unknown or outer tracked numerical-call environment: '+reason)
        return (str(self.torch.__version__),int(self.torch.get_num_threads()),
            int(self.torch.get_num_interop_threads()),str(self.torch.get_default_dtype()),
            bool(self.torch.are_deterministic_algorithms_enabled()),
            str(self.torch.get_float32_matmul_precision()))

    def _scope_guard(self):
        q = self.q
        mode = self._mode()
        self.helper._source_binding()
        if (q._current_x is not self.point or q._current_point_sha256!=self.point_sha
                or q.identity!=self.model_sha
                or self.module._immutable_point_owner(self.point,(q.free_size,),self.owner) is not self.owner):
            raise ValueError('The complete immutable current point changed')
        for actual in (self.x,self.prepared.x):
            if (type(actual) is not np.ndarray or actual.dtype!=np.dtype('float64')
                    or not actual.dtype.isnative or actual.shape!=(q.free_size,)
                    or not np.array_equal(actual.view(np.uint64),self.point.view(np.uint64))):
                raise ValueError('Keep every caller and prepared-point word, including signed zeros')
        for obj,model,identity in self.models:
            if (obj.model is not model or _curvature_cache_canonical(model)!=identity
                    or getattr(obj,'identity',getattr(obj,'model_identity',None))!=identity):
                raise ValueError('The full physical model changed inside one selected-row scope')
        for obj,name,original in self.links:
            if getattr(obj,name) is not original:
                raise ValueError('An actual physical producer object changed: '+name)
        for label,obj,kind in self.objects:
            if type(obj) is not kind:raise ValueError('A physical producer class changed: '+label)
        for obj,name,function in self.methods:
            bound = getattr(obj,name)
            if getattr(bound,'__func__',bound) is not function:
                raise ValueError('A complete source method changed: '+name)
        for path,source in self.sources.items():
            if _curvature_cache_sha(path)!=source:
                raise ValueError('A complete actual source file changed inside the row scope')
        return mode

    def _basic_key(self,candidate):
        q = self.q
        loc = candidate['location']
        if loc[0]=='grid':
            if len(loc)!=4:raise ValueError('Keep the full original grid/branch tuple')
            stage,angle,branch = (int(v) for v in loc[1:])
            cell,u,phi = (int(q.observation_cells[stage]),float(q.observation_u[stage]),float(q.phi[angle]))
            literal = ('grid',stage,angle,branch,cell,u.hex(),phi.hex())
        elif loc[0]=='arbitrary':
            if len(loc)!=5:raise ValueError('Keep the full original material/branch tuple')
            cell,u,phi,branch = int(loc[1]),float(loc[2]),float(loc[3]),int(loc[4])
            literal = ('arbitrary',cell,u.hex(),phi.hex(),branch)
        else:
            raise ValueError('Unknown original point-pullback path')
        cot = candidate['cot']
        if type(cot) is not dict or set(cot)!=set(_CURVATURE_COTANGENT_FIELDS):
            raise ValueError('Retain every one of the six actual physical covector slots')
        words = []
        for name in _CURVATURE_COTANGENT_FIELDS:
            value = cot[name]
            if (type(value) is not np.ndarray or value.dtype!=np.dtype('float64')
                    or not value.dtype.isnative or value.shape!=(3,) or not np.isfinite(value).all()):
                raise ValueError('Use actual complete finite binary64 covectors')
            words.append((name,str(value.dtype),tuple(value.shape),tuple(value.strides),value.tobytes(order='C')))
        return (literal,tuple(words)),(cell,u,phi)

    def _complete_key(self,basic,address):
        mode = self._scope_guard()
        q = self.q
        cell,u,phi = address
        query = q._point_queries.get((cell,u.hex()))
        root = q._root_cache.get(phi.hex())
        if query is None or root is None or root.get('order')!=2:
            return None
        if (len(root['stages'])!=q.normal_stage_count
                or any(stage.get('jacobian_order')!=2 or stage.get('jacobian') is None
                       for stage in root['stages'])):
            return None
        provider = q.base.parent_jet
        mean = provider._mean_cache.get(phi.hex())
        radial = provider._radial_cache.get((
            _curvature_cache_array_sha(query['cells']),_curvature_cache_array_sha(query['local'])))
        calibration = q.reference_calibration.cache.get((phi.hex(),))
        reference = q.base._cache.get(('integration',(phi.hex(),)))
        if (mean is None or radial is None or calibration is None
                or not isinstance(reference,dict) or 'cache_path' not in reference):
            return None
        reference_path = Path(reference['cache_path'])
        file_identity = (str(reference_path),reference_path.stat().st_size,_curvature_cache_sha(reference_path))
        carriers = dict(mesh=q.mesh,gauss_u=q.gauss_u,gauss_w=q.gauss_w,
            integration_query=q.integration_query,fixed_core=q.fixed_core,parent_core=q.parent_core,
            frequencies=q.freq,core_frequencies=q.qfreq,radial_free=q.radial_free,
            radial_free_tensor=q.base._radial_free_torch,frozen_Q=q._frozen_Q0,
            bubble_nodes=[[str(v) for v in row] for row in q.bubble_nodes],
            gamma_nodes=[str(v) for v in q.gamma_nodes],
            normal_steps=list(q.normal_step_carriers),S=float(q.S),R=float(q.R),
            M=int(q.M),J=int(q.J),n=int(q.n),free_size=int(q.free_size),
            integration_order=int(q.integration_order),root_iterations=int(q.root_iterations),
            root_tolerance=float(q.root_tolerance),actual_query=query,actual_root_and_matrices=root,
            actual_fixed_mean=mean,actual_fixed_radial=radial,actual_calibration=calibration,
            fixed_provider_core=provider.core,fixed_provider_height=float(provider.height))
        return _curvature_cache_words_sha((
            self.definition['source_sha256'],self.point_sha,self.model_sha,
            tuple(sorted(self.sources.items())),mode,basic,file_identity,self.helper._words(carriers)))

    def get(self,candidate,index):
        self.counts['requests'] += 1
        record = dict(row_index=int(index),origin='original_complete_point_vjp',
            original_returned=False,complete_key_sha256=None,
            stored_complete_key_sha256=None,gradient_words_sha256=None,origin_row_index=None)
        self.requests.append(record)
        self.pending = None
        if self.enabled:
            try:
                basic,address = self._basic_key(candidate)
                self.remaining[basic] -= 1
                self.pending = basic,address,record
                if (self.remaining[basic]<=0
                        and not any(old_basic==basic for old_basic,_ in self.cache)):
                    # A first-and-only request cannot hit. Keep the original
                    # call without copying/hashing its large numerical state.
                    self.counts['original_pullback_attempts'] += 1
                    return None
                complete = self._complete_key(basic,address)
                record['complete_key_sha256'] = complete
                entry = None if complete is None else self.cache.get((basic,complete))
                if entry is not None:
                    # The byte owner is immutable, and callers receive a new
                    # full-size copy rather than a mutable alias to the cache.
                    result = np.frombuffer(entry['words'],dtype=np.float64).copy()
                    if result.shape!=(self.q.free_size,) or not np.isfinite(result).all():
                        raise ValueError('Incomplete stored native pullback')
                    self.cache.move_to_end((basic,complete))
                    self.counts['numerical_hits'] += 1
                    record.update(origin='prior_complete_numerical_pullback',original_returned=False,
                        gradient_words_sha256=entry['gradient_sha'],origin_row_index=entry['row_index'])
                    if self.remaining[basic]<=0:
                        self.payload_bytes -= len(entry['words'])
                        del self.cache[(basic,complete)]
                        self.counts['entries_released_after_last_use'] += 1
                    self.pending = None
                    return result
            except Exception as error:
                self._optional('optional exact numerical lookup',error)
                self._discard()
        self.counts['original_pullback_attempts'] += 1
        return None

    def remember(self,value):
        # Called only after the unchanged original pullback has truly returned.
        self.counts['original_pullback_returns'] += 1
        record = self.requests[-1]
        record['original_returned'] = True
        if not self.enabled or self.pending is None:return
        basic,address,_ = self.pending
        self.pending = None
        if self.remaining[basic]<=0:
            self.counts['unique_use_values_not_stored'] += 1
            return
        try:
            if (type(value) is not np.ndarray or value.dtype!=np.dtype('float64')
                    or not value.dtype.isnative or value.shape!=(self.q.free_size,)
                    or not value.flags.c_contiguous or value.strides!=(8,)
                    or not np.isfinite(value).all()):
                raise ValueError('Keep the complete finite native gradient returned by the original producer')
            complete = self._complete_key(basic,address)
            if complete is None:return
            words = value.tobytes(order='C')
            if len(words)>_CURVATURE_CACHE_LIMIT:
                self.counts['oversize_values_not_stored'] += 1
                return
            while self.cache and self.payload_bytes+len(words)>_CURVATURE_CACHE_LIMIT:
                _,old = self.cache.popitem(last=False)
                self.payload_bytes -= len(old['words'])
                self.counts['entries_evicted'] += 1
            key = (basic,complete)
            old = self.cache.pop(key,None)
            if old is not None:self.payload_bytes -= len(old['words'])
            gradient_sha = _curvature_cache_array_sha(value)
            self.cache[key] = dict(words=words,gradient_sha=gradient_sha,row_index=record['row_index'])
            self.payload_bytes += len(words)
            self.counts['entries_stored'] += 1
            self.counts['peak_retained_numerical_payload_bytes'] = max(
                self.counts['peak_retained_numerical_payload_bytes'],self.payload_bytes)
            record.update(stored_complete_key_sha256=complete,gradient_words_sha256=gradient_sha)
        except Exception as error:
            self._optional('retain complete returned numerical pullback',error)
            self._discard()

    def close(self):
        if self.closed:return
        self.cache.clear()
        self.payload_bytes = 0
        self.counts['retained_numerical_payload_bytes'] = 0
        self.closed = True
        self.pending = None

    def metadata(self):
        return dict(schema=_CURVATURE_CACHE_SCHEMA,definition=self.definition,
            current_full_point_sha256=self.point_sha,model_identity_sha256=self.model_sha,
            complete_row_loop_returned=True,scope_closed=self.closed,
            optional_cache_enabled=self.enabled,actual_source_bindings=dict(self.sources),
            counts=dict(self.counts),requests=list(self.requests),optional_failures=list(self.failures),
            actual_full_stage_or_point_vjp_calls_inferred_from_hits=False,
            continuous_certificate_or_measured_speedup_claimed=False)



def build_inequality_rows(problem, x, geometry_module, point_module, transpose,
                         coordinate_size, *, reach_ratio=.03, safety=.992,
                         active_band=.025, max_rows=192, top_curvature=16,
                         top_radius=2, witnesses=(), radius_witnesses=(),
                         observed_module=None, matrix_workdir=None,
                         block_columns=32768, protected_angle_radius=.05,
                         diversity_u=1e-3, diversity_phi=None):
    q = problem
    if diversity_phi is None:
        diversity_phi = 1.0/(32*q.M)
    if not (0 < protected_angle_radius < np.pi/2 and diversity_u > 0 and diversity_phi > 0):
        raise ValueError('Need declared positive working-row neighborhood parameters')
    p = q.prepare(x)
    scan, locations, radial_locations = geometry_module.scan_geometry(
        q, x, top_curvature=top_curvature, top_radius=top_radius)
    if not scan['complete']:
        raise ValueError('A singular current point cannot define curvature inequalities')
    if observed_module is None or matrix_workdir is None:
        raise ValueError('Need literal observation weights and an explicit scratch directory')
    radii = []
    radius_records = []
    # Keep only scalar values and tiny point fields here.  Full-free radius
    # covectors are generated lazily after working rows have been selected;
    # 100 radius witnesses must not allocate 100 million-entry covectors.
    for stage, angle in radial_locations:
        f = geometry_module.single_fields(q, p, stage, angle)
        radius = float(np.linalg.norm(f['F']))
        radii.append((2*radius, ('grid_radius', int(stage), int(angle)), f))
    for witness in radius_witnesses:
        cell, u, phi = (int(witness['cell']), float(witness['u']), float(witness['phi']))
        f = point_module.fields_at(q, p, cell, u, phi, observed_module)
        radius = float(np.linalg.norm(f['F']))
        if not np.isfinite(radius) or radius <= 0:
            raise ValueError('Every actual radius witness needs positive finite radius')
        radii.append((2*radius, ('arbitrary_radius', cell, u, phi), f))
        radius_records.append(dict(cell=cell, u=u, phi=phi, diameter=2*radius))
    radii.append((2., ('fixed_core',), None))
    radii.append((2*abs(float(p.height)), ('cap_height',), None))
    strongest = max(range(len(radii)), key=lambda j: radii[j][0])
    candidates = []
    witnesses_read = []
    seen = {}
    witness_details = []

    def add_candidates(location, value, cot, meta, protected=False):
        for j, (diameter, rloc, _) in enumerate(radii):
            product = reach_ratio*diameter*abs(value)
            required = bool(protected and j == strongest)
            if not required and product < safety-active_band:
                continue
            key = (tuple(location), tuple(rloc))
            if key in seen:
                if required:
                    candidates[seen[key]]['required'] = True
                continue
            seen[key] = len(candidates)
            candidates.append(dict(product=product, location=location,
                value=value, cot=cot, principal=meta, diameter=diameter,
                radius_index=j, required=required, primary=(j == strongest)))

    for stage, angle, branch in locations:
        f = geometry_module.single_fields(q, p, stage, angle)
        value, cot, meta = geometry_module.curvature_cotangent(f, branch)
        add_candidates(('grid', int(stage), int(angle), int(branch)), value, cot, meta)
    for witness in witnesses:
        cell, u, phi = (int(witness['cell']), float(witness['u']), float(witness['phi']))
        f = point_module.fields_at(q, p, cell, u, phi, observed_module)
        values = [geometry_module.curvature_cotangent(f, branch) for branch in (0, 1)]
        largest = int(np.argmax([abs(v[0]) for v in values]))
        protected = bool(witness.get('protected', False))
        for branch, (value, cot, meta) in enumerate(values):
            add_candidates(('arbitrary', cell, u, phi, branch), value, cot, meta,
                           protected=(protected and branch == largest))
        witnesses_read.append(dict(cell=cell, u=u, phi=phi,
            signed_principal_curvatures=[v[0] for v in values], protected=protected))
        witness_details.append((cell, u, phi, values, protected))
    representatives = []
    for seed_cell, seed_u, seed_phi, seed_values, is_protected in witness_details:
        if not is_protected:
            continue
        neighbors = [value for value in witness_details if value[0] == seed_cell
                     and abs(value[2]-seed_phi) <= protected_angle_radius]
        current = max(neighbors, key=lambda value: max(abs(branch[0]) for branch in value[3]))
        cell, u, phi, values, _ = current
        branch = int(np.argmax([abs(value[0]) for value in values]))
        value, cot, meta = values[branch]
        add_candidates(('arbitrary', cell, u, phi, branch), value, cot, meta, protected=True)
        representatives.append(dict(seed=[seed_cell, seed_u, seed_phi],
            current_location=[cell, u, phi], current_branch=branch,
            current_absolute_curvature=abs(value),
            rule='same original cell, phi within declared radius; highest among all permanent points'))
    required_count = sum(c['required'] for c in candidates)
    if required_count > max_rows:
        raise ValueError('Working-row cap would drop a declared protected inequality')
    eligible = len(candidates)
    candidates.sort(key=lambda c: (not c['required'], not c['primary'], -c['product']))
    required = [candidate for candidate in candidates if candidate['required']]
    selected = required.copy()
    def physical_location(candidate):
        loc = candidate['location']
        if loc[0] == 'grid':
            stage, angle, branch = loc[1:]
            return (int(q.observation_cells[stage]), float(q.observation_u[stage]),
                    float(q.phi[angle]), int(branch))
        return (int(loc[1]), float(loc[2]), float(loc[3]), int(loc[4]))
    selected_points = [physical_location(candidate) for candidate in selected]
    diversity_skips = 0
    for candidate in candidates:
        if len(selected) >= max_rows:
            break
        if candidate['required'] or not candidate['primary']:
            continue
        cell, u, phi, branch = physical_location(candidate)
        close = any(cell == c and branch == br and abs(u-v) < diversity_u
                    and abs(phi-angle) < diversity_phi for c, v, angle, br in selected_points)
        if close:
            diversity_skips += 1
            continue
        selected.append(candidate)
        selected_points.append((cell, u, phi, branch))
    # If distinct primary rows do not use the cap, retain alternative actual
    # diameter partners.  Do not refill it with near-duplicate primary points.
    for candidate in candidates:
        if len(selected) >= max_rows:
            break
        if candidate['required'] or candidate['primary']:
            continue
        selected.append(candidate)
    candidates = selected
    directory = Path(matrix_workdir)
    directory.mkdir(parents=True, exist_ok=False)
    path = directory/'normalized-inequality-rows.f64'
    matrix = (np.memmap(path, dtype=np.float64, mode='w+',
                       shape=(len(candidates), coordinate_size))
              if candidates else np.empty((0, coordinate_size)))
    bounds = np.empty(len(candidates))
    row_metadata = []
    radius_covectors = {}

    def discard_pages():
        if (isinstance(matrix, np.memmap) and hasattr(matrix._mmap, 'madvise')
                and hasattr(mmap, 'MADV_DONTNEED')):
            matrix._mmap.madvise(mmap.MADV_DONTNEED)

    def radius_covector(index):
        if index in radius_covectors:
            return radius_covectors[index]
        diameter, loc, fields = radii[index]
        if loc[0] == 'fixed_core':
            result = np.zeros(q.free_size)
        elif loc[0] == 'cap_height':
            result = np.zeros(q.free_size)
            result[-1] = 2*np.sign(p.height)
        else:
            cot = {key: np.zeros(3) for key in fields}
            cot['F'] = 4*fields['F']/diameter
            if loc[0] == 'grid_radius':
                result = point_module.pullback(q, p, loc[1], loc[2], cot)
            else:
                result = point_module.pullback_at(q, p, *loc[1:], cot, observed_module)
        radius_covectors[index] = result
        return result

    curvature_values = _CompleteCurvaturePullbackCache(
        q,x,p,geometry_module,point_module,candidates)
    try:
        for index, c in enumerate(candidates):
            loc = c['location']
            dk = curvature_values.get(c,index)
            if dk is None:
                if loc[0] == 'grid':
                    dk = point_module.pullback(q, p, loc[1], loc[2], c['cot'])
                else:
                    dk = point_module.pullback_at(q, p, *loc[1:4], c['cot'], observed_module)
                curvature_values.remember(dk)
            dD = radius_covector(c['radius_index'])
            gradient = reach_ratio*(c['diameter']*np.sign(c['value'])*dk+abs(c['value'])*dD)
            row = transpose(gradient)
            norm = float(np.linalg.norm(row))
            if not np.isfinite(norm) or norm <= 0:
                raise ValueError('A declared geometric inequality needs positive finite row norm')
            matrix[index] = row/norm
            bounds[index] = (safety-c['product'])/norm
            row_metadata.append(dict(index=index, current_product=c['product'],
                actual_product_margin=safety-c['product'], normalized_bound=bounds[index],
                gradient_coordinate_norm=norm, signed_curvature=c['value'],
                diameter=c['diameter'], curvature_point=loc,
                radius_point=radii[c['radius_index']][1],
                protected_inequality=c['required'], strongest_radius_partner=c['primary'],
                principal_metadata=c['principal']))
            if (index+1) % 8 == 0:
                matrix.flush()
                discard_pages()
    finally:
        curvature_values.close()
    if isinstance(matrix, np.memmap):
        matrix.flush()
        discard_pages()
    metadata = dict(
        schema='complete-actual-margin-neighborhood-diverse-inequalities-v2',
        selected_rows=len(candidates), eligible_rows=eligible,
        protected_inequalities=required_count,
        protected_current_representatives=representatives,
        protected_phi_neighborhood_radius=protected_angle_radius,
        diversity_u=diversity_u,diversity_phi=diversity_phi,
        near_duplicate_primary_rows_deferred=diversity_skips,
        permanently_screened_curvature_locations=len(witnesses),
        permanently_screened_radius_locations=len(radius_witnesses),
        reach_ratio=reach_ratio, safety=safety, active_band=active_band,
        maximum_working_rows=max_rows, top_curvature=top_curvature, top_radius=top_radius,
        row_formula='C=(reach_ratio*(D*sign(kappa)*dkappa+abs(kappa)*dD) T)/norm',
        bound_formula='b=(safety-reach_ratio*D*abs(kappa))/norm; C z <= b',
        homogeneous_equalities_imposed=False, all_original_field_variables_retained=True,
        row_cache=str(path), row_cache_bytes=int(matrix.size*8), block_columns=block_columns,
        lazy_full_free_radius_covectors=len(radius_covectors),
        complete_curvature_pullback_cache=curvature_values.metadata(),
        current_grid_scan=scan, current_arbitrary_curvatures=witnesses_read,
        current_arbitrary_radii=radius_records, rows=row_metadata,
        selection='Original protected points and each protected current same-cell angular-neighborhood maximum first; separated near-active strongest-D rows next; alternative diameter partners only afterward. No nonlinear location merged or dropped',
        nonlinear_memory_policy='No location removed when its linear row is unselected',
        scope='Finite first-order geometric step inequalities only; true full point geometry still decides nonlinear acceptance')
    return matrix, bounds, metadata
