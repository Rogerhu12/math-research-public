"""Complete current raw/affine/R153/R155 interval jets on the old interior.

This joins the saved independent layout, accurate R136 physical profile,
complete R149 fixed atlas, and complete R132 rational flat-tail definition.
The original numeric evaluators remain untouched and are not definitions of
the analytic derivatives. The accurate terminal-domain wrapper of R172 is
separate; no old saved endpoint is silently promoted to the true S.
"""
from __future__ import annotations
from dataclasses import replace
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib,json
from flint import arb,ctx

from fd2d_gc_archive_arrays import identity
from fd2d_gc_current_native_interval import (
    CurrentNativeIntervalPieces,Jet,ProfileBox,ChartBox,aq,rational,rational_pair,
    angle_interval,interval,UnresolvedInterval,compose_R153,compose_R155,
    physical_jet,connection_box,bound_record)
from fd2d_gc_r136_arb_profile import R136ArbProfile
from fd2d_gc_current_frozen_atlas_arb import (
    TwoJet,union_jets,step_jet,FrozenAtlasArb)

SCHEMA='fd2d-current-complete-accurate-field-Arb-v1'
TAIL_CUT=F(4,5)
TAIL_FLAT=F(17,50)
TAIL_WIDTH=F(23,50)


def jpow(value,count):
    out=TwoJet.constant(1)
    for unused in range(int(count)):out=out*value
    return out


def reflected_step(lo,hi,point,width):
    q=step_jet(-rational(hi),-rational(lo),-rational(point),-rational(point)+rational(width))
    return replace(q,s=-q.s,sxi=-q.sxi)


class CompleteCurrentFieldArb:
    """All defining functions are bound before any interval evaluation.

    A returned complete box is a continuous local enclosure, not a global
    certification of this not-yet-solved candidate. Nonpositive denominators
    are explicit unresolved boxes. No sample floor replaces a proof.
    """
    def __init__(self,native_definition,profile_packet,*,profile_packet_sha256,precision=256,atlas_options=None):
        ctx.prec=max(int(ctx.prec),int(precision))
        self.parts=CurrentNativeIntervalPieces(native_definition)
        self.profile=R136ArbProfile.from_packet(profile_packet,expected_sha256=profile_packet_sha256)
        if self.profile.inputs['field_arrays']['sha256']!=identity(self.parts.reader.arrays_path)['sha256']:
            raise ValueError('Full field and accurate radial packet do not bind the same immutable actual input')
        if self.profile.inputs['candidate']['sha256']!=identity(self.parts.reader.candidate_path)['sha256']:
            raise ValueError('The complete field and radial target candidates differ')
        if tuple(self.profile.delta)!=tuple(self.parts.parameters[self.parts.reader.profile_parameter_slice]):
            raise ValueError('Actual physical delta data differ')
        self.atlas=FrozenAtlasArb(self.parts,precision=precision,**({} if atlas_options is None else atlas_options))
        self.reader=self.parts.reader
        if self.reader.tail_kind!='positive_bernstein':raise ValueError('Only the explicitly declared complete R132 tail is supported')
        self.tail_controls=tuple(self.parts.parameters[self.reader.tail_parameter_slice])
        self.saved_end=self.parts.mesh[-1]
        self.tail_start=rational(float(.42*float(self.saved_end)))
        self.tail_old_independent_width=rational(float(.58*float(self.saved_end)))
        self.tail_accurate_width=self.saved_end-self.tail_start
        self._binding=dict(schema=SCHEMA,source=identity(__file__),native_definition=identity(native_definition),
            immutable_actual_arrays=identity(self.reader.arrays_path),
            accurate_profile_packet=identity(profile_packet),profile_binding_sha256=self.profile.input_binding_sha256,
            full_atlas_binding_sha256=self.atlas.binding_sha256,
            complete_independent_layout=self.parts.layout,
            actual_mesh_exact=[rational_pair(q) for q in self.parts.mesh],
            accurate_tail_constants=dict(cut='4/5',flat='17/50',width='23/50'),
            actual_tail_controls=[rational_pair(q) for q in self.tail_controls],
            exact_tail_weight_endpoints=[rational_pair(self.tail_start),rational_pair(self.saved_end)],
            exact_tail_weight_width=rational_pair(self.tail_accurate_width),
            old_independent_float_tail_width=rational_pair(self.tail_old_independent_width),
            width_difference=rational_pair(self.tail_accurate_width-self.tail_old_independent_width),
            target_definition='R136 accurate phase-integral physical g and original saved physical bump parameters',
            field_semantics='Original complete mathematical raw/affine/R153/R155 functions on the saved interior; accurate radial/tail/atlas evaluation is not the old floating program',
            accurate_endpoint_extension_included=False,
            old_field_arrays_changed=False,old_numeric_sources_changed=False,
            old_numerical_samples_transferred_as_certificates=False)
        content={k:v for k,v in self._binding.items()}
        for k in ('source','native_definition','immutable_actual_arrays','accurate_profile_packet'):
            content[k]={key:content[k][key] for key in ('bytes','sha256')}
        self.binding_sha256=hashlib.sha256(json.dumps(content,sort_keys=True,separators=(',',':')).encode()).hexdigest()

    def weights(self,lo,hi):
        p=self.parts;seed=self.reader.seed_weight_definition
        return dict(seed=1-step_jet(lo,hi,seed['start'],seed['end']),
            tail=step_jet(lo,hi,self.tail_start,self.saved_end),
            coast=step_jet(lo,hi,p.entry,p.entry+p.rim)*reflected_step(lo,hi,p.exit,p.rim),
            terminal=step_jet(lo,hi,p.trace_start,p.trace_stop))

    def kappa(self,y):
        """Full rational R132 curvature on |y| in (17/50,4/5), zero outside.

        Each sign/support branch restricts only the interval value; all
        valid derivative boxes are retained. Fourfold endpoint zeros allow
        the same complete C2 jet to be enclosed across the branch edges.
        """
        cut,flat,width=map(aq,(TAIL_CUT,TAIL_FLAT,TAIL_WIDTH))
        pieces=[]
        yl,yh=y.value.lower(),y.value.upper()
        if not (yl>flat or yh<-flat):pieces.append(TwoJet.constant(0))
        if yl<=-cut or yh>=cut:pieces.append(TwoJet.constant(0))
        for sign in (-1,1):
            absolute=sign*y.value
            left=max(absolute.lower(),flat.lower())
            right=min(absolute.upper(),cut.upper())
            if left>right:continue
            q=(sign*y-flat)/width
            low=max(arb(0),q.value.lower());high=min(arb(1),q.value.upper())
            if low>high:continue
            q=replace(q,value=low.union(high))
            # de Casteljau retains every original Bernstein control.
            work=[TwoJet.constant(aq(v)) for v in self.tail_controls]
            while len(work)>1:work=[(1-q)*a+q*b for a,b in zip(work,work[1:])]
            value=(630/width)*jpow(q,4)*jpow(1-q,4)*work[0]
            pieces.append(value)
        if not pieces:raise ArithmeticError('Complete rational tail support branches did not cover the input')
        return union_jets(pieces)

    def tail_fields(self,a,U):
        sn,cs=U.sin(),U.cos();kappa=self.kappa(a*sn)
        return (kappa*cs.squared(),-kappa*sn*cs,kappa*sn.squared())

    def affine_box(self,lo,hi,angular_lo,angular_hi,*,angle_unit='pi',side='both'):
        lo,hi=map(rational,(lo,hi))
        if not self.parts.mesh[0]<=lo<=hi<self.saved_end:
            raise ValueError('The old interior ends strictly before its numerical endpoint label; use R172 to cover the true terminal domain')
        q=self.profile.physical_box(lo,hi,side=('both' if side=='coast' else side))
        profile=ProfileBox(q['a'],q['a_s'],q['a_ss'],q['a_sss'])
        a=TwoJet(q['a'],q['a_s'],arb(0),q['a_ss'],arb(0),arb(0))
        chart=self.atlas.box(lo,hi,angular_lo,angular_hi,angle_unit=angle_unit,side=side)
        U=chart['U'];weights=self.weights(lo,hi);zero=TwoJet.constant(0)
        if self.reader.base_kind=='balanced_seed':seed=1/chart['angular']['rho']
        elif self.reader.base_kind=='circle':seed=TwoJet.constant(1/self.atlas.a0)
        else:raise ValueError('Unknown saved central baseline')
        tail=self.tail_fields(a,U)
        plain=[weights['tail']*v for v in tail]
        plain[0]+=weights['seed']*seed
        w=weights['coast']
        if w.value.is_zero() and w.s.is_zero():
            affine=tuple(plain);reference=None
        else:
            left,right=max(lo,self.parts.entry),min(hi,self.parts.exit)
            if left>right:raise ArithmeticError('Active coast weight outside its declared reference domain')
            reference=self.atlas.ruling(left,right,chart['angular'])
            affine=tuple((1-w)*plain[j]+w*reference['fields'][j] for j in range(3))
        return dict(affine=tuple(v.native() for v in affine),affine_full_twojet=affine,
            weights=weights,profile=profile,profile_box=q,chart=chart['chart'],atlas_box=chart,
            reference_evaluated_only_on_its_support=True,
            full_known_functions_retained=True,all_original_tail_controls_included=True,
            no_material_angle_inverse_used=True,binding_sha256=self.binding_sha256)

    def box(self,cell,lo,hi,angular_lo,angular_hi,*,angle_unit='pi',side='both',connection=True):
        raw=self.parts.raw_box(cell,lo,hi,angular_lo,angular_hi,angle_unit=angle_unit)
        q=self.affine_box(lo,hi,angular_lo,angular_hi,angle_unit=angle_unit,side=side)
        background=tuple(r+a for r,a in zip(raw['fields'],q['affine']))
        K=q['profile'].curvature_jet()
        fields=compose_R153(background,q['weights']['coast'].native(),K)
        fields=compose_R155(fields,q['weights']['terminal'].native(),K)
        out=dict(q,raw_fields=raw['fields'],affine_background_fields=background,fields=fields,
            field_order=['n','m','l'],cell=int(cell),
            all_defining_functions_enclosed_on_requested_box=True,
            conditional_unknown_denominators_resolved_on_this_box=True,
            radial_derivative_side='explicit saved P1 cell and selected actual atlas side',
            accurate_target_and_saved_interior_only=True,continuous_global_surface_certificate=False)
        if connection:out['connection']=connection_box(fields,q['profile'],q['chart'])
        return out

    def accurate_cut_angular(self,lo,hi,*,angle_unit='pi'):
        if any(v!=0 for v in self.reader.values[-1]):
            raise ValueError('Saved terminal correction is not exactly zero')
        angle=angle_interval(lo,hi,angle_unit)
        U=TwoJet(angle,arb(0),arb(1),arb(0),arb(0),arb(0))
        values=self.tail_fields(TwoJet.constant(TAIL_CUT),U)
        fields=tuple(Jet(v.value,None,v.xi,v.xixi,None) for v in values)
        return dict(fields=fields,field_order=['n','m','l'],
            exact_tail_constants=dict(cut='4/5',flat='17/50',width='23/50'),
            physical_endpoint=self.profile.end,
            scope='accurate R132 cut angular trace; R172 interior/endpoint field coverage is separate',
            radial_II_jets_assigned=False,interior_cut_limit_proved_here=False,
            binding_sha256=self.binding_sha256)

    def primitive_box(self,primitive,cell,lo,hi,angular_lo,angular_hi,*,angle_unit='pi',side='both'):
        """Complete actual H-P followed by the unchanged zero-end identity.

        The polynomial is independently an exact finite object. Its input
        identity must bind this full field, not the earlier conditional
        partial-field packet or the unrelated old NativeLogField consumer.
        No fit residual or point samples substitute for the H-P enclosure.
        """
        if primitive.field_binding_sha256!=self.binding_sha256:
            raise ValueError('The R125 polynomial is not bound to this complete accurate field')
        q=self.box(cell,lo,hi,angular_lo,angular_hi,angle_unit=angle_unit,side=side,connection=True)
        out=primitive.conditional_box(q['connection'],q['chart'],lo,hi,angular_lo,angular_hi,
            field_binding_sha256=self.binding_sha256,angle_unit=angle_unit)
        out.update(complete_actual_field_inputs_supplied=True,
            complete_field_source_binding_sha256=self.binding_sha256,
            H_minus_P_method='direct interval subtraction of this complete field forcing and the exact supplied polynomial',
            source_cell=int(cell),angular_box_only=True,
            initial_compatibility_supplied=False,whole_surface_certificate=False)
        return out

    def definition(self):
        return dict(self._binding,binding_sha256=self.binding_sha256,
            complete_frozen_atlas=self.atlas.definition(),accurate_profile=self.profile.definition(),
            actual_saved_native_definition=self.parts.original_definition,
            computed_interval_blocks=['full raw P1/Fourier','all full affine lifting functions and true native five jets',
                'fixed R149 atlas six jets','actual conditional R153/R155 fields','all R119 Gauss/Codazzi forcing components',
                'R132 rational cut angular value/two jets'],
            unpaid=['whole-domain unknown n positivity for this new accepted input',
                'accurate R172 terminal extension/degenerate one-sided bounds',
                'initial compatibility','actual R125 forcing polynomial/primitive remainder accumulation',
                'actual surface and geometry posterior'],
            no_new_solution_inferred=True,whole_surface_certificate=False)
