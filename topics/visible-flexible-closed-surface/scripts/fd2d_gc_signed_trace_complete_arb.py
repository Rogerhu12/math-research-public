"""Complete accurate R182 signed field, its true jets and R119 forcing.

The explicit new native schema is decoded once. Closed R173 full-affine,
atlas and raw polynomial formulas are reused, followed by the actual signed
maps. The final cell uses the unchanged R172 mathematical formula under a
new explicit constructor: all additional windows vanish there identically.
"""
from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import json

import numpy as np
from flint import arb,ctx

from fd2d_gc_archive_arrays import identity
from fd2d_gc_current_native_interval import (
    Jet,aq,rational,rational_pair,compose_R153,compose_R155,connection_box,
    step5_jet,reflected_step5_jet,UnresolvedInterval)
from fd2d_gc_current_complete_field_arb import CompleteCurrentFieldArb
from fd2d_gc_current_accurate_domain_arb import AccurateDomainCurrentFieldArb,digest,ExactNormalizedCellPrimitive
from fd2d_gc_current_frozen_atlas_arb import FrozenAtlasArb
from fd2d_gc_dyadic_tail_complete_arb import DyadicTailIntervalPieces,checked_sources
from fd2d_gc_r136_arb_profile import R136ArbProfile
from fd2d_gc_r136_bernstein_bumps import BernsteinBumpProfile
from fd2d_gc_dyadic_tail_accurate_last_cell import DyadicTailAccurateLastCell
from fd2d_gc_accurate_last_cell import AccurateLastCell
from fd2d_gc_signed_trace_archive_native import SignedTraceArchiveNativeField

HERE=Path(__file__).resolve().parent
PARTS_SCHEMA='fd2d-R182-signed-raw-interval-pieces-v1'
INTERIOR_SCHEMA='fd2d-R182-signed-complete-interior-Arb-v1'
TERMINAL_SCHEMA='fd2d-R182-signed-accurate-last-cell-Arb-v1'
SCHEMA='fd2d-R182-signed-complete-accurate-domain-Arb-v1'


def compose_signed(fields,weight,K,sign):
    if weight.value.is_zero() and weight.s is not None and weight.s.is_zero():
        return tuple(fields)
    if sign not in (-1,1):
        raise ValueError('An explicit constant trace sign is required')
    if not K.value>0:
        raise UnresolvedInterval('The new active signed support has no strictly positive continuous K enclosure')
    n,m,l=fields
    h=((n-l).squared()+4*m.squared()+4*K).sqrt()
    increment=weight*(sign*h-n-l)/2
    return n+increment,m,l+increment


class SignedTraceIntervalPieces(DyadicTailIntervalPieces):
    def __init__(self,definition_path):
        sources=checked_sources()
        self.definition_path=Path(definition_path)
        self.original_definition=json.loads(self.definition_path.read_text())
        self.reader=SignedTraceArchiveNativeField.from_definition(self.definition_path)
        r=self.reader
        self.mesh=tuple(rational(v) for v in r.nodes)
        self.K,self.e,self.d=r.K,r.e,r.d
        self.coefficients=r.values
        self.parameters=tuple(rational(v) for v in r.parameters)
        self.profile_supports=tuple(tuple(rational(v) for v in row) for row in r.profile.supports)
        self.layout=r.explicit_parameter_layout
        self.entry,self.exit=map(rational,r.gauss_l_definition['support'])
        self.length=rational(r.coast_reference.length)
        self.rim=rational(float(r.coast_reference.length*r.reference_rim_fraction))
        self.trace_start,self.trace_stop,self.cut=(rational(r.original_positive_trace_definition[k])
            for k in ('start','ramp_stop','cut'))
        self.signed_windows=tuple(dict(name=p['name'],sign=int(p['sign']),
            breaks=tuple(rational(v) for v in p['breaks'])) for p in r.signed_windows)
        self.tail_radius,self.tail_flat,self.tail_width=F(4,5),F(17,50),F(23,50)
        self._cell_cache={}
        self.binding=dict(schema=PARTS_SCHEMA,source=identity(__file__),inherited_sources=sources,
            native_definition_identity=identity(self.definition_path),arrays_identity=identity(r.arrays_path),
            parameter_layout=self.layout,mesh_exact=[rational_pair(v) for v in self.mesh],
            signed_trace_definition=r.signed_trace_definition,
            tail_search_domain_definition=r.tail_search_domain_definition,
            tail_search_domain_certificate=r.tail.control_certificate,
            signed_archive_decoded_by_old_positive_constructor=False)
        self.binding_sha256=digest(self.binding)

    def definition(self):
        result=super().definition()
        result.update(schema=PARTS_SCHEMA,binding=self.binding,binding_sha256=self.binding_sha256,
            signed_windows=self.reader.signed_trace_definition,
            complete_saved_raw_coefficients_enclosed=True)
        return result

    def structural_partition(self):
        result=super().structural_partition()
        records={F(int(p['exact'][0]),int(p['exact'][1])):list(p['labels']) for p in result['points']}
        for window in self.signed_windows:
            for letter,q in zip(('A','B','C','D'),window['breaks']):
                records.setdefault(q,[]).append('signed_'+window['name']+'_'+letter)
        result['points']=[dict(exact=rational_pair(q),labels=records[q]) for q in sorted(records)]
        result['all_explicit_signed_weight_breakpoints_included']=True
        return result


class SignedTraceCompleteInteriorArb(CompleteCurrentFieldArb):
    def __init__(self,native_definition,profile_packet,*,profile_packet_sha256,
                 precision=256,profile_backend='bernstein_bumps',atlas_options=None):
        ctx.prec=max(int(ctx.prec),int(precision))
        self.parts=SignedTraceIntervalPieces(native_definition)
        self.reader=self.parts.reader
        profile_class={'bernstein_bumps':BernsteinBumpProfile,'original':R136ArbProfile}.get(profile_backend)
        if profile_class is None:
            raise ValueError('Unknown declared accurate profile backend')
        self.profile=profile_class.from_packet(profile_packet,expected_sha256=profile_packet_sha256)
        if (self.profile.inputs['field_arrays']['sha256']!=identity(self.reader.arrays_path)['sha256'] or
                self.profile.inputs['candidate']['sha256']!=identity(self.reader.candidate_path)['sha256'] or
                tuple(self.profile.delta)!=tuple(self.parts.parameters[self.reader.profile_parameter_slice])):
            raise ValueError('The signed archive and accurate actual profile differ')
        self.atlas=FrozenAtlasArb(self.parts,precision=precision,
            **({} if atlas_options is None else atlas_options))
        self.tail_controls=tuple(self.parts.parameters[self.reader.tail_parameter_slice])
        self.saved_end=self.parts.mesh[-1]
        self.tail_start=rational(float(.42*float(self.saved_end)))
        self.tail_old_independent_width=rational(float(.58*float(self.saved_end)))
        self.tail_accurate_width=self.saved_end-self.tail_start
        self._binding=dict(schema=INTERIOR_SCHEMA,source=identity(__file__),
            inherited_sources=checked_sources(),native_definition=identity(native_definition),
            actual_arrays=identity(self.reader.arrays_path),raw_parts_binding_sha256=self.parts.binding_sha256,
            accurate_profile_packet=identity(profile_packet),profile_definition=self.profile.definition(),
            full_atlas_binding_sha256=self.atlas.binding_sha256,
            signed_trace_definition=self.reader.signed_trace_definition,
            exact_saved_mesh=[rational_pair(v) for v in self.parts.mesh],
            actual_tail_controls=[rational_pair(v) for v in self.tail_controls],
            accurate_tail_constants=['4/5','17/50','23/50'],
            exact_tail_weight_endpoints=[rational_pair(self.tail_start),rational_pair(self.saved_end)],
            full_function_semantics='Actual raw+complete affine+R153, explicit disjoint signed windows, then original R155 terminal; true physical profile and full material chart',
            continuous_global_surface_certificate=False)
        self.binding_sha256=digest(self._binding)

    def box(self,cell,lo,hi,angular_lo,angular_hi,*,angle_unit='pi',side='both',connection=True):
        raw=self.parts.raw_box(cell,lo,hi,angular_lo,angular_hi,angle_unit=angle_unit)
        q=self.affine_box(lo,hi,angular_lo,angular_hi,angle_unit=angle_unit,side=side)
        background=tuple(r+a for r,a in zip(raw['fields'],q['affine']))
        K=q['profile'].curvature_jet()
        coast=compose_R153(background,q['weights']['coast'].native(),K)
        fields=coast;signed=[]
        for window in self.parts.signed_windows:
            A,B,C,D=window['breaks']
            weight=step5_jet(lo,hi,A,B)*reflected_step5_jet(lo,hi,D,D-C)
            fields=compose_signed(fields,weight,K,window['sign'])
            signed.append(dict(name=window['name'],sign=window['sign'],weight=weight))
        fields=compose_R155(fields,q['weights']['terminal'].native(),K)
        out=dict(q,raw_fields=raw['fields'],affine_background_fields=background,
            coast_background_fields=coast,fields=fields,signed_components=signed,
            field_order=['n','m','l'],cell=int(cell),
            all_defining_functions_enclosed_on_requested_box=True,
            conditional_unknown_denominators_resolved_on_this_box=True,
            radial_derivative_side='Explicit saved P1 cell and declared atlas side',
            accurate_target_and_saved_interior_only=True,
            continuous_global_surface_certificate=False)
        if connection:
            out['connection']=connection_box(fields,q['profile'],q['chart'])
        return out


class SignedTraceAccurateLastCell(DyadicTailAccurateLastCell):
    """New explicit constructor, with unchanged old terminal formulas."""
    def __init__(self,reader,profile,profile_packet):
        if not isinstance(reader,SignedTraceArchiveNativeField):
            raise TypeError('Require the explicitly decoded actual signed field')
        self.parent_formula_source=identity(HERE/'fd2d_gc_accurate_last_cell.py')
        self.field_path,self.packet_path=reader.arrays_path,Path(profile_packet)
        self.profile=profile
        if profile.inputs['field_arrays']['sha256']!=identity(self.field_path)['sha256']:
            raise ValueError('The accurate final cell and actual signed profile differ')
        self.K,self.e,self.d=reader.K,reader.e,reader.d
        self.mesh=tuple(rational(v) for v in reader.nodes)
        self.raw=reader.values
        self.parameters=tuple(rational(v) for v in reader.parameters)
        self.central=reader.central_parameter_count
        self.tail=self.parameters[reader.tail_parameter_slice]
        self.tail_control_certificate=reader.tail.control_certificate
        self.tail_search_domain_definition=reader.tail_search_domain_definition
        self.b,self.E=self.mesh[-2:]
        self.S=profile.end;self.length=self.S-aq(self.b)
        if not self.length>0 or not np.all(self.raw[-1]==0):
            raise ValueError('Positive accurate width and exact zero final raw row are required')
        terminal=reader.original_positive_trace_definition
        protected=[reader.seed_weight_definition['end'],reader.angular_atlas_definition['exit_transition'][1],
            reader.gauss_l_definition['support'][1],terminal['ramp_stop'],
            float(np.max(reader.profile.supports)),reader.blend_interval[-1]]
        protected.extend(p['breaks'][-1] for p in reader.signed_windows)
        if any(rational(v)>=self.b for v in protected) or rational(terminal['cut'])!=self.E:
            raise ValueError('All additional windows must vanish throughout the accurate terminal completion')
        self.weight_start=rational(float(.42*float(self.E)))
        self.weight_length=rational(float(.58*float(self.E)))
        if self.weight_start+self.weight_length!=self.E or self.weight_start>=self.b:
            raise ValueError('The full original tail weight endpoints differ')
        last=profile.pieces[-1]
        if not aq(self.b)>last['s0']:
            raise ValueError('The completed final cell is outside the accurate last phase piece')
        self.last_piece=last['index']
        self.c0=tuple(rational(v) for v in self.raw[-2])
        self.signed_trace_definition=reader.signed_trace_definition
        self.inputs=dict(field_arrays=identity(self.field_path),profile_packet=identity(profile_packet),
            source=identity(__file__))

    def definition(self):
        result=super().definition()
        result.pop('binding_sha256')
        result.update(schema=TERMINAL_SCHEMA,source=identity(__file__),
            signed_trace_definition=self.signed_trace_definition,
            additional_signed_weights_identically_zero_on_entire_completed_cell=True,
            old_terminal_interval_formula_unchanged=True,
            signed_archive_sent_to_legacy_constructor=False)
        result['binding_sha256']=digest(result)
        return result


class SignedTraceAccurateDomainFieldArb(AccurateDomainCurrentFieldArb):
    def __init__(self,native_definition,profile_packet,*,profile_packet_sha256,
                 precision=256,profile_backend='bernstein_bumps',atlas_options=None):
        self.interior=SignedTraceCompleteInteriorArb(native_definition,profile_packet,
            profile_packet_sha256=profile_packet_sha256,precision=precision,
            profile_backend=profile_backend,atlas_options=atlas_options)
        self.parts,self.reader,self.atlas=(self.interior.parts,self.interior.reader,self.interior.atlas)
        self.profile=self.interior.profile
        self.saved_mesh=self.parts.mesh
        self.last_cell=len(self.saved_mesh)-2
        self.terminal=SignedTraceAccurateLastCell(self.reader,self.profile,profile_packet)
        self.accurate_end=self.terminal.S
        self._binding=dict(schema=SCHEMA,source=identity(__file__),
            native_source=identity(HERE/'fd2d_gc_signed_trace_archive_native.py'),
            inherited_sources=checked_sources(),interior_binding_sha256=self.interior.binding_sha256,
            accurate_profile_definition=self.profile.definition(),terminal_definition=self.terminal.definition(),
            exact_saved_mesh=[rational_pair(v) for v in self.saved_mesh],final_cell=self.last_cell,
            signed_trace_definition=self.reader.signed_trace_definition,
            complete_field_semantics='Actual full signed interior, followed by R172 exact last-cell completion where all additional weights are identically zero',
            native_derivatives='physical s at fixed xi; material s/u derivatives use complete U_s/U_xi chain rule',
            accurate_rational_tail_constants=['4/5','17/50','23/50'],
            cut_scope='Exact tail value/u/uu only; no invented radial or mixed II derivative',
            explicit_new_mathematical_field=True,whole_surface_certificate=False)
        self.binding_sha256=digest(self._binding)


__all__=['SignedTraceIntervalPieces','SignedTraceCompleteInteriorArb',
         'SignedTraceAccurateLastCell','SignedTraceAccurateDomainFieldArb',
         'ExactNormalizedCellPrimitive','compose_signed']
