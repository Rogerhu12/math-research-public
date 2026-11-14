"""Bounded exact-key memoization of the already frozen R149 geometry.

Install only on a new problem. Original sources and mathematical metadata
are unchanged. Shared chart/reference instances make these caches visible
to the ordinary copy views. No target/profile, tail, raw field, lifting or
forcing depending on the current parameter vector is cached here.
"""
from __future__ import annotations
from collections import OrderedDict
import hashlib
import json
from pathlib import Path
import sys
from types import MethodType
import numpy as np


def _deep_size(value, seen=None):
    """Conservative per-entry accounting; this is not process RSS."""
    seen=set() if seen is None else seen
    if id(value) in seen:return 0
    seen.add(id(value));total=sys.getsizeof(value)
    if isinstance(value,dict):
        total+=sum(_deep_size(k,seen)+_deep_size(v,seen) for k,v in value.items())
    elif isinstance(value,(tuple,list)):
        total+=sum(_deep_size(v,seen) for v in value)
    # Frozen arrays always own their buffers, included by getsizeof.
    return total


def _freeze(value):
    if isinstance(value,np.ndarray):
        out=np.array(value,copy=True,order='C');out.flags.writeable=False;return out
    if isinstance(value,dict):return {k:_freeze(v) for k,v in value.items()}
    if isinstance(value,tuple):return tuple(_freeze(v) for v in value)
    if isinstance(value,list):return [_freeze(v) for v in value]
    return value


def _public(value):
    """Copy mapping containers; immutable array payloads are shared."""
    if isinstance(value,dict):return {k:_public(v) for k,v in value.items()}
    if isinstance(value,tuple):return tuple(_public(v) for v in value)
    if isinstance(value,list):return [_public(v) for v in value]
    return value


def _array_payload(value):
    if isinstance(value,np.ndarray):return value.nbytes
    if isinstance(value,dict):return sum(_array_payload(v) for v in value.values())
    if isinstance(value,(tuple,list)):return sum(_array_payload(v) for v in value)
    return 0


class PreparedGeometryCache:
    def __init__(self,problem,byte_limit):
        if int(byte_limit)!=byte_limit or byte_limit<4096:
            raise ValueError('Use an explicit byte budget of at least 4096')
        self.byte_limit=int(byte_limit)
        self.chart=problem.chart;self.reference=problem.coast_reference
        if (type(self.chart).__name__!='FrozenRulingAtlas'
            or type(self.reference).__name__!='DirectLabelCoastReference'
            or self.reference.atlas is not self.chart
            or problem.profile_kind!='physical_bumps'
            or self.chart.chart_definition().get('parameters_frozen') is not True):
            raise ValueError('Bind the original explicit parameter-frozen R149 chart/reference')
        self.original_coordinates=self.chart.coordinates
        self.original_ruling_jet=self.chart.ruling_jet
        self.original_reference_point=self.reference._point
        self.seed_reference=self.chart.original.reference
        self.original_seed_coordinate=self.seed_reference.reference_coordinate
        self.original_reference_capacity=int(self.reference.maximum_points)
        self._entries=OrderedDict();self._labels=OrderedDict()
        self._entry_bytes=0;self._label_bytes=0;self._serial=0;self._coordinate_depth=0
        self._counts={kind:dict(hits=0,misses=0,stores=0,evictions=0,uncached=0)
            for kind in ('coordinates','ruling_jet','reference_point','seed_coordinate')}
        self.label_hits=self.label_misses=self.label_evictions=0
        self.peak_accounted_bytes=0;self.maximum_composition_residual=0.
        self._binding=dict(chart=self.chart.chart_definition(),
            reference_binding_sha256=self.reference.binding_sha256,
            reference_evaluation=self.reference.evaluation_definition(),
            numpy_version=np.__version__,longdouble_itemsize=np.dtype(np.longdouble).itemsize,
            longdouble_mantissa_bits=int(np.finfo(np.longdouble).nmant))
        self.binding_sha256=hashlib.sha256(json.dumps(self._binding,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        self._source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

    def _used(self):
        return (self._entry_bytes+self._label_bytes
            +sys.getsizeof(self._entries)+sys.getsizeof(self._labels))

    def _drop(self,key):
        packet,lid,kind,cost=self._entries.pop(key)
        self._entry_bytes-=cost;self._counts[kind]['evictions']+=1

    def _drop_label(self,lid):
        for key,entry in list(self._entries.items()):
            if entry[1]==lid:self._drop(key)
        _,cost=self._labels.pop(lid);self._label_bytes-=cost;self.label_evictions+=1

    def _trim(self):
        while self._used()>self.byte_limit and self._entries:
            self._drop(next(iter(self._entries)))
        while self._used()>self.byte_limit and self._labels:
            self._drop_label(next(iter(self._labels)))
        self.peak_accounted_bytes=max(self.peak_accounted_bytes,self._used())

    def _label(self,coordinate):
        xi=np.atleast_1d(np.asarray(self.chart.theta if coordinate is None else coordinate,np.longdouble))
        if xi.ndim!=1 or not np.all(np.isfinite(xi)):
            raise ValueError('A frozen cache label must be one finite actual column')
        for lid,(old,_) in self._labels.items():
            if old.shape==xi.shape and np.array_equal(old,xi):
                self._labels.move_to_end(lid);self.label_hits+=1;return lid,xi
        self.label_misses+=1;self._serial+=1;lid=self._serial
        frozen=_freeze(xi);cost=_deep_size((lid,frozen,0))
        self._labels[lid]=(frozen,cost);self._label_bytes+=cost
        while len(self._labels)>8:self._drop_label(next(iter(self._labels)))
        self._trim()
        return lid,xi

    def _memo(self,kind,lid,tail,compute):
        key=(kind,lid,tail)
        if key in self._entries:
            self._entries.move_to_end(key);self._counts[kind]['hits']+=1
            return _public(self._entries[key][0])
        self._counts[kind]['misses']+=1
        raw=compute()
        packet=_freeze(raw)
        cost=_deep_size(key)+_deep_size((packet,lid,kind,0))
        # Retain the requested label while evicting older result entries.
        if lid not in self._labels or cost+self._label_bytes+512>self.byte_limit:
            self._counts[kind]['uncached']+=1
            return _public(packet)
        self._entries[key]=(packet,lid,kind,cost);self._entry_bytes+=cost
        self._counts[kind]['stores']+=1;self._trim()
        if self._used()>self.byte_limit:raise ArithmeticError('Frozen cache budget accounting failed')
        return _public(packet)

    def coordinates(self,s,coordinate=None,*,side='coast'):
        if side not in ('coast','left','right'):raise ValueError('Use the original declared radial side')
        x=np.atleast_1d(np.asarray(s,float))
        if x.ndim!=1 or not np.all(np.isfinite(x)):raise ValueError('Finite one-dimensional radial coordinates required')
        lid,xi=self._label(coordinate)
        key=(x.shape,np.ascontiguousarray(x).tobytes(),side)
        def evaluate():
            self._coordinate_depth+=1
            try:return self.original_coordinates(x,coordinate=xi,side=side)
            finally:self._coordinate_depth-=1
        return self._memo('coordinates',lid,key,evaluate)

    def ruling_jet(self,s,coordinate=None,*,include_native=False):
        # Whole coordinates already retain their complete scalar-ruling
        # results. Avoid retaining duplicate subpackets, and never retain
        # the large native diagnostic packet here. DirectLabel caches only
        # the nine physical value/first-jet components below.
        if self._coordinate_depth or include_native:
            return self.original_ruling_jet(s,coordinate,include_native=include_native)
        lid,xi=self._label(coordinate);ss=float(s)
        return self._memo('ruling_jet',lid,(ss.hex(),False),
            lambda:self.original_ruling_jet(ss,xi,include_native=False))

    def reference_point(self,s,label,material):
        lid,xi=self._label(label);ss=float(s);u=np.asarray(material,np.longdouble)
        if u.shape!=xi.shape or not np.all(np.isfinite(u)):
            raise ValueError('Expected the paired finite actual material column')
        point=self._memo('reference_point',lid,ss.hex(),
            lambda:self.original_reference_point(ss,xi,u))
        # A matching label never excuses a different material composition.
        error=float(np.max(abs(np.asarray(point['material_u'],np.longdouble)-u),initial=0.))
        self.maximum_composition_residual=max(self.maximum_composition_residual,error)
        if error>2e-13:raise ValueError('Cached label does not match requested actual material coordinate')
        return point

    def seed_coordinate(self,coordinate):
        a=np.asarray(coordinate,np.longdouble)
        if a.ndim!=1:
            return self.original_seed_coordinate(coordinate)
        lid,xi=self._label(a)
        return self._memo('seed_coordinate',lid,(),lambda:self.original_seed_coordinate(xi))

    def definition(self):
        return dict(schema='fd2d-shared-prepared-frozen-geometry-cache-v1',
            source_sha256=self._source_sha256,binding_sha256=self.binding_sha256,
            frozen_binding=self._binding,byte_limit=self.byte_limit,
            budget_scope='Conservatively accounted cache payloads, keys and container headers; not total process RSS or temporary evaluations',
            keys='Registered actual longdouble label column checked by array_equal; exact binary64 radial bytes or scalar hex; full ordered chart side; static frozen binding',
            longdouble_padding_bytes_are_not_keys=True,nearest_point_or_rounded_coordinate_hits=False,
            label_registry_maximum=8,all_cached_arrays_readonly=True,
            mapping_containers_copied_on_return=True,
            original_reference_staging_capacity=self.original_reference_capacity,
            installed_reference_staging_capacity=1,
            reference_staging_outside_budget='One original DirectLabel row plus its original label; measured separately in statistics',
            large_native_packets_cached=False,
            cached=['frozen atlas coordinates','standalone frozen ruling chart jets without native packet',
                'frozen reference physical values/physical_s/physical_u with material check',
                'fixed original seed-coordinate jets'],
            not_cached=['current a_delta/c_delta/K_delta or their parameter jets','raw correction',
                'current tail angle jets at a_delta*sin(U)','full lifting','current Codazzi forcing or Jacobians',
                'nonlinear R153/R155 actual field','core geometry depending on central c'],
            original_mathematical_definitions_changed=False,old_source_files_modified=False,
            source_functions_used_on_every_miss=True)

    def statistics(self):
        payload=sum(_array_payload(entry[0]) for entry in self._entries.values())
        staging=getattr(self.reference,'_points',[])
        by_kind={kind:dict(counts,entries=sum(e[2]==kind for e in self._entries.values()))
                 for kind,counts in self._counts.items()}
        return dict(schema='fd2d-prepared-frozen-geometry-cache-statistics-v1',
            entries=len(self._entries),label_entries=len(self._labels),by_kind=by_kind,
            label_hits=self.label_hits,label_misses=self.label_misses,label_evictions=self.label_evictions,
            cached_array_payload_bytes=payload,accounted_bytes=self._used(),
            peak_post_eviction_accounted_bytes=self.peak_accounted_bytes,byte_limit=self.byte_limit,
            within_byte_limit=self._used()<=self.byte_limit,
            original_reference_staging_entries=len(staging),
            original_reference_staging_accounted_bytes=_deep_size(staging),
            original_reference_statistics=self.reference.cache_statistics(),
            maximum_material_composition_residual=self.maximum_composition_residual,
            no_runtime_speedup_claim=True)

    diagnostics=statistics


def install_prepared_geometry_cache(problem,byte_limit=16*1024*1024):
    """Install exact-key caches on this new problem's shared frozen objects.

    Reinstallation returns the same handle only for the same byte budget.
    No class method or original source is changed. copy.copy(problem) views
    share the explicitly frozen chart and reference exactly as before.
    """
    existing=getattr(problem.chart,'_fd2d_prepared_geometry_cache_v1',None)
    if existing is not None:
        if existing.reference is not problem.coast_reference or existing.byte_limit!=int(byte_limit):
            raise ValueError('Do not silently replace a live frozen cache definition')
        return existing
    handle=PreparedGeometryCache(problem,byte_limit)
    chart=problem.chart;ref=problem.coast_reference;seed=handle.seed_reference
    def coordinates(self,s,coordinate=None,*,side='coast'):
        return handle.coordinates(s,coordinate,side=side)
    def ruling_jet(self,s,coordinate=None,*,include_native=False):
        return handle.ruling_jet(s,coordinate,include_native=include_native)
    def point(self,s,label,material):return handle.reference_point(s,label,material)
    def seed_coordinate(self,coordinate):return handle.seed_coordinate(coordinate)
    chart.coordinates=MethodType(coordinates,chart)
    chart.ruling_jet=MethodType(ruling_jet,chart)
    ref._point=MethodType(point,ref)
    seed.reference_coordinate=MethodType(seed_coordinate,seed)
    # The unified byte-bounded store owns prepared reference values. The
    # old point implementation remains the miss evaluator with one bounded
    # staging row, instead of a second unaccounted 64/256-point cache.
    ref.maximum_points=1;del ref._points[1:]
    chart._fd2d_prepared_geometry_cache_v1=handle
    problem._fd2d_prepared_geometry_cache_v1=handle
    return handle
