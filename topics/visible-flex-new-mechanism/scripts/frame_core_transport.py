#!/usr/bin/env python3
"""Build a new elliptic-core design by semantic coefficient transport.

The command line exposes artificial checks only.  A research caller must run
inside Rogerhu12/math-research-public Actions.  Every source report is replayed
in its original model before a new core, seed, natural field and height base
are constructed.  Equal coefficient bits do not mean equal physical fields.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import traceback

import numpy as np

from frame_collar_bvp import (FrameCollarProblem, EllipticCylinderPort,
    NegativeKRadialSeed, atomic_save)
from frame_collar_enriched import EnrichedProblem, make_enriched, rational_knots
from frame_collar_bent_tail import load_enriched_report, artificial_enriched_report
from frame_collar_natural_body_audit import NaturalBodyProblem
from frame_independent_height import IndependentHeightProblem
from frame_fixed_height_primitive_audit import (load_selected_report,
    implementation_hashes as replay_hashes)
from frame_independent_height_solve import (state_record,
    implementation_hashes as selected_source_hashes)
from frame_collar_residual_audit import digest
from polygonal_tail_heat_extension import exact_metric_definition


def implementation_hashes():
    out=replay_hashes()
    out[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return out


def exact_values(values):
    return [str(Q.from_float(float(x))) for x in values]


def same_bits(left,right):
    a=np.asarray(left,dtype=np.float64);b=np.asarray(right,dtype=np.float64)
    return a.shape==b.shape and np.array_equal(a.view(np.uint64),b.view(np.uint64))


def require_public_actions(environment=None):
    env=os.environ if environment is None else environment
    if env.get('GITHUB_ACTIONS')!='true' or env.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        raise PermissionError('research core transport requires this public repository Actions')


def seed_configuration(seed):
    return {'negative_curvature_drop':str(seed.gap_exact),
        'core_fraction':str(seed.core_fraction_exact),'flat_fraction':str(seed.flat_fraction_exact),
        'active_fractions':[str(x) for x in seed.fractions_exact],
        'tail_smoothstep_order':seed.tail_smoothstep_order}


def field_basis_definition(problem):
    """Complete radial basis definition, deliberately independent of the core."""
    return {'degree':5,'radial_free':problem.radial_free,
        'clamped_knots_exact':[str(x) for x in rational_knots(problem.seed,problem.radial_free)],
        'retained_columns':'3 through radial_free+2 inclusive',
        'zero_extension_outside_active_interval':True,'endpoint_weight':None}


def semantic_labels(problem,fields=('u','v','beta')):
    labels=[]
    for name in fields:
        if name not in ('u','v','beta'):raise ValueError('unknown scalar field')
        trig='cos' if name=='beta' else 'sin'
        angular=[('material-'+trig,k) for k in range(0 if name=='beta' else 1,problem.angular_modes+1)]
        angular += [('ellipse-phase-'+trig,k) for k in range(1,problem.phi_modes+1)]
        if name=='u' and problem.core_direction:angular.append(('exact-u-core',None))
        if len(angular)!=problem.angular_counts[name]:raise ValueError('angular labels do not match the frozen layout')
        for radial in range(problem.radial_free):
            labels += [(name,radial,kind,k) for kind,k in angular]
    if len(set(labels))!=len(labels):raise ValueError('duplicate semantic column labels')
    return labels


def copy_semantic_coefficients(source,source_values,target,fields=('u','v','beta')):
    source_labels=semantic_labels(source,fields);target_labels=semantic_labels(target,fields)
    values=np.asarray(source_values,dtype=np.float64)
    if values.shape!=(len(source_labels),) or not np.all(np.isfinite(values)):
        raise ValueError('finite source coefficients matching the semantic labels required')
    if set(source_labels)!=set(target_labels):raise ValueError('semantic spaces differ; implicit fitting or padding is forbidden')
    if field_basis_definition(source)!=field_basis_definition(target):
        raise ValueError('the complete exact radial field bases differ')
    indexes={label:i for i,label in enumerate(source_labels)}
    permutation=np.array([indexes[label] for label in target_labels],dtype=int)
    result=values[permutation].copy()
    if not same_bits(result,values[permutation]):raise ArithmeticError('semantic copying changed binary64 bits')
    mapping=[{'label':list(label),'source_index':int(i),'target_index':j}
             for j,(label,i) in enumerate(zip(target_labels,permutation))]
    return result,{'schema':'exact-semantic-binary64-coefficient-copy-v1',
        'column_map':mapping,'coefficient_count':len(result),
        'source_exact_binary64_rationals':exact_values(values),
        'target_exact_binary64_rationals':exact_values(result),
        'source_binary64_hex':[float(x).hex() for x in values],
        'target_binary64_hex':[float(x).hex() for x in result],
        'same_bits_under_the_explicit_permutation':True,
        'no_clipping_refitting_orthogonalization_or_new_columns':True,
        'same_physical_field_is_not_claimed':True}


def body_basis_without_seed(body_metric):
    """Compare every family field except the intentionally replaced seed."""
    family=copy.deepcopy(body_metric.family_definition)
    seed=family.pop('seed_definition')
    if not isinstance(seed,dict):raise ValueError('an explicit accurate seed definition is required')
    return {'schema':'complete-body-basis-and-radius-rule-excluding-seed-v1',
        'excluded_field':'seed_definition; its source and target identities are separately retained',
        'complete_remaining_family_definition':family}


class TransportedNaturalBodyProblem(NaturalBodyProblem):
    """Natural fields anchored to the new core, never relabeled old geometry."""
    def __init__(self,old,source_state,transport_definition,**kwargs):
        self.transport_definition=copy.deepcopy(transport_definition)
        if (old.port.identity!=self.transport_definition['target_core_identity'] or
            old.space_definition()!=self.transport_definition['target_enriched_space_definition'] or
            exact_values(source_state)!=self.transport_definition['coefficient_transport']['target_exact_binary64_rationals']):
            raise ValueError('transported anchor does not match the target enriched provider')
        super().__init__(old,source_state,**kwargs)
        self.anchor_definition.update(schema='target-core-transported-enriched-c0',
            core_transport_definition=self.transport_definition,
            core_transport_definition_sha256=digest(self.transport_definition),
            immediate_source_is_the_new_target_enriched_model=True,
            old_public_report_is_provenance_not_the_target_physical_anchor=True)
        # Parent grids may have cached the old anchor schema during construction.
        self._rebuild_evaluation_grids()

    def space_definition(self):
        out=super().space_definition()
        out.update(schema='target-core-transported-natural-frame-space-v1',
            base_field_and_entry_cutoff='target-core entry seed and natural-cap correction anchored at transported c0',
            free_parameter_columns='semantic original labels evaluated on the target core; independent target body controls',
            core_transport_definition_sha256=digest(self.transport_definition))
        return out

    def model_definition(self):
        out=super().model_definition()
        out.pop('physical_cap_unchanged_from_saturated_run',None)
        out.pop('base_definition_changed_from_saturated_run',None)
        out.pop('zero_body_controls_reproduce_the_original_seed_function_exactly',None)
        out.update(schema='target-core-transported-natural-connector-family-v1',
            core_transport_definition=self.transport_definition,
            zero_body_controls_reproduce_the_new_target_seed_function_exactly=True,
            cap_uses_the_existing_exact_S9_six_cap_definition=True,
            target_core_and_radial_metric_are_new_designs=True,
            no_old_geometry_height_or_reach_certificate_is_inherited=True)
        return out


class TransportedIndependentHeightProblem(IndependentHeightProblem):
    """Independent center speed using the immutable target transported c0."""
    def __init__(self,source,height_free=9,*,height_angular_nodes=384,frozen_metric_definition=None):
        if not isinstance(source,TransportedNaturalBodyProblem):
            raise TypeError('a transported natural source is required')
        super().__init__(source,height_free,height_angular_nodes=height_angular_nodes,
                         frozen_metric_definition=frozen_metric_definition)
        self.height_base_definition.update(schema='target-core-transported-c0-angular-mean-height-v1',
            source_fields='the immutable target-core natural field at transported original c0, with zero target body controls',
            core_transport_definition_sha256=digest(source.transport_definition),
            old_height_mean_cache_is_not_reused=True,
            selected_initializer_does_not_replace_this_anchor=True)
        self.height_cache={}

    def identity(self,state):
        out=super().identity(state)
        out.update(schema='target-core-transported-independent-center-speed-v1',
            core_transport_definition_sha256=digest(self.source.transport_definition),
            old_metric_refinement_is_not_claimed=True)
        return out

    def evaluation_variant(self,state,*,heat_order=None,height_angular_nodes=None):
        source=self.source if heat_order is None else self.source.evaluation_variant(heat_order,self.anchor_latent)
        frozen=None if self.metric_free else self.metric_model(state)
        result=TransportedIndependentHeightProblem(source,self.height_free,
            height_angular_nodes=self.height_angular_nodes if height_angular_nodes is None else height_angular_nodes,
            frozen_metric_definition=frozen)
        if result.identity(state)!=self.identity(state):
            raise ArithmeticError('GH or height-mean refinement changed the transported physical state')
        return result


def _validate_artificial_carrier(report,target_minor):
    core=report.get('core_physical_identity',{})
    if (core.get('major')!='9/10' or core.get('minor')!='18/25' or
        core.get('half_width')!='1/50' or Q(target_minor)!=Q(2,3)):
        raise PermissionError('artificial bypass is restricted to the declared 9/10,18/25 -> 2/3 carrier')


def build_core_transport(anchor_bytes,*,target_minor='37/100',selected_report_bytes=None,
        height_free=9,metric_free=5,heat_order=32,height_angular_nodes=384,
        radial_nodes=61,angular_nodes=192,quadrature_order=4,
        support_width='1/10',plateau_fraction='1/3',tau0='1/128',
        ball_radius='101/100',strip_half_width='19/50',
        amplitudes=('3/16','1/8','1/8','3/16','1/8','1/8'),
        expected_anchor_sha256=None,expected_selected_sha256=None,
        initializer_bounds=None,artificial=False):
    """Return (new problem, numerical initializer, complete transport receipt).

    Default initialization uses transported u/v and zero height/body controls.
    Optional selected input is first replayed by the original strict loader;
    it changes only numerical initializer values, never the 234-value anchor.
    No geometry, objective, step or optimizer is evaluated by this factory.
    Constructors do tabulate their scalar fields at configured evaluation nodes.
    """
    if not artificial:require_public_actions()
    if not isinstance(anchor_bytes,bytes):raise TypeError('original carrier bytes are required')
    anchor_sha=hashlib.sha256(anchor_bytes).hexdigest()
    if expected_anchor_sha256 is not None and anchor_sha!=expected_anchor_sha256:
        raise ValueError('original anchor byte hash mismatch')
    report=json.loads(anchor_bytes)
    if artificial:_validate_artificial_carrier(report,target_minor)
    old,c0,source_receipt=load_enriched_report(report)
    if len(old.fixed_metric):raise ValueError('only the original seed-metric enriched carrier is supported')
    selected=None;selected_state=None;selected_receipt=None;selected_sha=None
    if selected_report_bytes is not None:
        if not isinstance(selected_report_bytes,bytes):raise TypeError('selected report bytes are required')
        selected_sha=hashlib.sha256(selected_report_bytes).hexdigest()
        if expected_selected_sha256 is not None and selected_sha!=expected_selected_sha256:
            raise ValueError('selected report byte hash mismatch')
        selected,selected_state,selected_receipt=load_selected_report(json.loads(selected_report_bytes),anchor_bytes)
    elif expected_selected_sha256 is not None:
        raise ValueError('an expected selected hash without selected bytes is invalid')

    port=EllipticCylinderPort(old.port.A_exact,Q(target_minor),old.port.width_exact,old.port.side)
    if port.identity==old.port.identity:raise ValueError('this new-core factory requires a changed core identity')
    cfg=seed_configuration(old.seed)
    seed=NegativeKRadialSeed.from_core(port,old.seed.length_exact,old.seed.cut_radius_exact,cfg)
    target=EnrichedProblem(port,seed,radial_free=old.radial_free,angular_modes=old.angular_modes,
        phi_modes=old.phi_modes,core_direction=old.core_direction,envelope_kind=old.envelope_kind,
        strip_half_width=str(old.strip_exact),fixed_metric_coefficients=old.fixed_metric,
        ellipse_envelope=(port.major,port.minor),height_limit=old.height_limit,shape_weight=old.shape_weight,
        radial_nodes=len(old.radial),angular_nodes=len(old.theta),radial_quadrature_order=old.radial_quadrature_order)
    transported,copy_receipt=copy_semantic_coefficients(old,c0,target)
    definition={'schema':'elliptic-core-semantic-coefficient-transport-v1',
        'source_report_bytes_sha256':anchor_sha,'source_replay_receipt':source_receipt,
        'source_core_identity':old.port.identity,'source_port_identity':old.port.port_identity,
        'source_seed_exact_definition':exact_metric_definition(old.seed),
        'source_enriched_space_definition':old.space_definition(),
        'source_metric_model':old.metric_model(c0),
        'target_core_identity':port.identity,'target_port_identity':port.port_identity,
        'target_seed_exact_definition':exact_metric_definition(seed),
        'target_enriched_space_definition':target.space_definition(),
        'target_enriched_shape_definition':target.shape_definition(),
        'radial_seed_configuration_preserved':cfg,
        'complete_field_radial_basis_definition':field_basis_definition(target),
        'coefficient_transport':copy_receipt,
        'new_arc_inverse_entry_jets_seed_mu_nu_and_heat_radius_are_rebuilt':True,
        'source_report_was_not_modified_to_pass_its_loader':True,
        'new_metric_design_not_old_fixed_g_refinement':True,
        'new_height_base_uses_transported_original_c0_not_selected_initializer':True,
        'new_entry_repair_or_single_Q_wrapper_included':False,
        'physical_field_equality_or_geometric_feasibility_is_not_claimed':True}
    natural=TransportedNaturalBodyProblem(target,transported,definition,metric_free=metric_free,
        support_width=support_width,plateau_fraction=plateau_fraction,tau0=tau0,heat_order=heat_order,
        ball_radius=ball_radius,strip_half_width=strip_half_width,amplitudes=amplitudes,
        radial_nodes=radial_nodes,angular_nodes=angular_nodes,quadrature_order=quadrature_order)
    problem=TransportedIndependentHeightProblem(natural,height_free,height_angular_nodes=height_angular_nodes)
    state=problem.initial_state()
    initializer={'kind':'transported-c0-uv-zero-height-zero-body',
        'selected_input':None,'anchor_is_not_replaced':True}
    if selected is not None:
        if selected.height_basis.identity!=problem.height_basis.identity:
            raise ValueError('complete exact height bases differ; numerical copying is not allowed')
        source_body_basis=body_basis_without_seed(selected.body_metric)
        if source_body_basis!=body_basis_without_seed(problem.body_metric):
            raise ValueError('complete body weighted-basis definitions differ outside the deliberately new seed')
        uv=np.r_[selected_state[selected.slices['u']],selected_state[selected.slices['v']]]
        copied,uv_receipt=copy_semantic_coefficients(selected.source,uv,natural,('u','v'))
        state[:problem.tangent_count]=copied
        state[problem.slices['height']]=selected_state[selected.slices['height']]
        state[problem.slices['metric']]=selected.metric_coefficients(selected_state)
        initializer={'kind':'strictly-replayed-selected-values-on-new-core-bases',
            'selected_input':{'bytes_sha256':selected_sha,'replay_receipt':selected_receipt},
            'uv_coefficient_transport':uv_receipt,
            'complete_height_basis_definition':problem.height_basis.identity,
            'complete_body_basis_definition_without_seed':source_body_basis,
            'source_full_body_family_sha256':selected.body_metric.family_sha256,
            'target_full_body_family_sha256':problem.body_metric.family_sha256,
            'height_values_bitwise_copied':same_bits(state[problem.slices['height']],selected_state[selected.slices['height']]),
            'body_values_bitwise_copied':same_bits(state[problem.slices['metric']],selected.metric_coefficients(selected_state)),
            'anchor_is_not_replaced':True,'total_height_and_metric_are_new_functions':True}
    bounds={}
    if initializer_bounds is not None:
        if set(initializer_bounds)!=set(problem.slices):raise ValueError('bounds must explicitly cover u,v,height,metric')
        for name,sl in problem.slices.items():
            lower,upper=map(float,initializer_bounds[name])
            if not np.isfinite(lower+upper) or lower>upper:raise ValueError('finite ordered initializer bounds required')
            values=state[sl];passed=bool(np.all((values>=lower)&(values<=upper)))
            bounds[name]={'lower':lower,'upper':upper,'inside_without_clipping':passed}
            if not passed:raise ValueError('transported initializer exceeds declared '+name+' bounds; no clipping performed')
    receipt={'schema':'elliptic-core-transport-factory-receipt-v1',
        'source_files_sha256':implementation_hashes(),'transport_definition':definition,
        'transport_definition_sha256':digest(definition),'initializer':initializer,
        'initializer_bounds':bounds if initializer_bounds is not None else None,
        'no_optimizer_bounds_are_implicitly_chosen':initializer_bounds is None,
        'target_natural_model_definition':natural.model_definition(),
        'target_height_base_definition':problem.height_base_definition,
        'target_initial_state':state_record(problem,state),
        'new_core_identity_sha256':port.identity_sha256,
        'old_core_identity_sha256':old.port.identity_sha256,
        'old_and_new_seed_identity_differ':exact_metric_definition(old.seed)!=exact_metric_definition(seed),
        'target_tail_physical_identity':problem.tail.identity,
        'original_anchor_coefficients_count':len(c0),'target_parameter_count':problem.nunknown,
        'artificial_inputs_only':bool(artificial),'geometry_or_objective_evaluated_by_factory':False,
        'scalar_constructor_tables_are_evaluated':True,'optimization_performed':False,
        'complete_isometry_embedding_reach_or_containment_proved':False}
    return problem,state,receipt


def artificial_source(side=1):
    """The declared mild carrier, retaining the actual 234-column layout."""
    port=EllipticCylinderPort('9/10','18/25','1/50',side)
    seed=NegativeKRadialSeed.from_core(port,'11/10','11/50')
    baseline=FrameCollarProblem(port,seed,radial_free=4,angular_modes=5,
        ellipse_envelope=(port.major,port.minor),height_limit=.45,
        radial_nodes=9,angular_nodes=24,radial_quadrature_order=3)
    old=make_enriched(baseline,9,3,9,24,3,strip_half_width='2/5')
    c0=.004*np.sin(np.arange(old.nunknown)+.3)
    carrier=artificial_enriched_report(old,c0,baseline,.003*np.cos(np.arange(baseline.nunknown)))
    raw=json.dumps(carrier,sort_keys=True).encode()
    old,c0,replay=load_enriched_report(json.loads(raw))
    cfg={'metric_free':5,'height_free':9,'heat_order':8,'height_angular_nodes':24,
        'radial_nodes':9,'angular_nodes':24,'quadrature_order':3}
    natural=NaturalBodyProblem(old,c0,metric_free=5,heat_order=8,radial_nodes=9,angular_nodes=24,quadrature_order=3)
    source=IndependentHeightProblem(natural,9,height_angular_nodes=24)
    state=source.initial_state();state[:source.tangent_count]+=.001*np.cos(np.arange(source.tangent_count))
    state[source.slices['height']]=.003*np.sin(np.arange(9)+.2)
    state[source.slices['metric']]=.004*np.cos(np.arange(5)+.4)
    frozen,fc=source.frozen_metric_copy(state)
    selected={'schema':'independent-height-bounded-direct-metric-solve-v1','configuration':cfg,
        'source_files_sha256':selected_source_hashes(),'source_record':{
            'sha256':hashlib.sha256(raw).hexdigest(),'identity':replay,'exact_original_c0':exact_values(c0)},
        'initial_exact_state':state_record(source,source.initial_state()),
        'selected_state':state_record(source,state),'final_metric_freeze':{'metric_model':frozen.metric_model(fc)}}
    return raw,json.dumps(selected,sort_keys=True).encode(),old,c0,source,state


def developer_check():
    rows=[];saved=None
    opts={'target_minor':'2/3','height_free':9,'metric_free':5,'heat_order':8,
        'height_angular_nodes':24,'radial_nodes':9,'angular_nodes':24,'quadrature_order':3,'artificial':True}
    for side in (1,-1):
        raw,selected_raw,old,c0,source,selected_state=artificial_source(side)
        zero,z,receipt=build_core_transport(raw,**opts)
        target,state,selected_receipt=build_core_transport(raw,selected_report_bytes=selected_raw,**opts)
        tc=target.height_basis.left;tf=target.height_basis.right;L=target.seed.length
        radial=np.unique(np.r_[np.linspace(0,L,9),tc,tf,target.source.support_start])
        theta=np.arange(96)*2*np.pi/96
        data=target.geometry(state,radial,theta,3)
        frozen,fc=target.frozen_metric_copy(state);replay=frozen.geometry(fc,radial,theta,3)
        freeze={key:float(np.max(abs(data[key]-replay[key]))) for key in ['X','Xs','Xt','Xss','Xst','Xtt']}
        variants=[target.evaluation_variant(state,heat_order=16),
                  target.evaluation_variant(state,height_angular_nodes=48),
                  frozen.evaluation_variant(fc,heat_order=16,height_angular_nodes=48)]
        physical=target.identity(state)
        identity_ok=all(v.identity(state if v.metric_free else fc)==physical for v in variants)
        probe=np.array([0.,tc/2,tc,tf,(tf+L)/2,L]);g=target.source.grid_for(probe,theta)
        fields=g.full_scalar_jets(target.latent_state(state))
        core=target.port.scalar_jets(probe[:3,None],theta[None,:])
        tail=target.tail.scalar_jets((target.seed.cut_radius+L-probe[3:])[:,None],theta[None,:])
        names=('u','v','beta');keys=('value','s','ss','theta','st','ss_theta')
        core_error=max(float(np.max(abs(fields[n][k][:3]-core[n][k]))) for n in names for k in keys)
        tail_error=max(float(np.max(abs(fields[n][k][3:]-tail[n][k]))) for n in names for k in keys)
        metric=target.metric(state,probe);seed=target.seed.evaluate(probe)
        port_metric_error=max(float(np.max(abs(metric[k]-seed[k]))) for k in ('a','a_s','a_ss'))
        # The immutable b0 is reconstructed on the target and never from the
        # optional selected state.  Evaluation variants must retain both schemas.
        hb0=zero.height_baseline(probe);hb1=target.height_baseline(probe)
        height_anchor_equal=(zero.height_base_definition==target.height_base_definition and
            all(same_bits(hb0[k],hb1[k]) for k in hb0))
        prefix=np.array([0.,tc/2,tc]);pd=target.geometry(state,prefix,theta,3)
        exact=target.port.position_jets(prefix[:,None],theta[None,:])
        core_positions={key:float(np.max(abs(pd[key]-exact[ek]))) for key,ek in
            [('X','X'),('Xs','Xs'),('Xt','Xtheta'),('Xss','Xss'),('Xst','Xst'),('Xtt','Xtt')]}
        rows.append({'side':side,'original_234_count':len(c0),
            'target_parameter_count':target.nunknown,'transported_c0_bits_equal':same_bits(c0,target.source.source_state),
            'semantic_label_map_is_complete':len(receipt['transport_definition']['coefficient_transport']['column_map'])==234,
            'source_and_target_core_differ':old.port.identity!=target.port.identity,
            'source_and_target_seed_differ':receipt['old_and_new_seed_identity_differ'],
            'source_and_target_complete_g_differ':source.metric_model(selected_state)['mathematical_definition']!=target.metric_model(state)['mathematical_definition'],
            'source_and_target_heat_identity_differ':source.source.heat_extension.identity!=target.source.heat_extension.identity,
            'same_exact_tail_definition':source.tail.identity==target.tail.identity,
            'zero_initializer_height_and_body_are_exactly_zero':bool(np.all(z[zero.slices['height']]==0) and np.all(z[zero.slices['metric']]==0)),
            'selected_uv_bits_equal':same_bits(state[:target.tangent_count],selected_state[:source.tangent_count]),
            'selected_height_bits_equal':same_bits(state[target.slices['height']],selected_state[source.slices['height']]),
            'selected_body_bits_equal':same_bits(state[target.slices['metric']],selected_state[source.slices['metric']]),
            'immutable_height_anchor_not_replaced_by_selected':height_anchor_equal,
            'GH_Nb_and_freeze_identity_preserved':identity_ok,
            'evaluation_variants_preserve_subclass':all(isinstance(v,TransportedIndependentHeightProblem) for v in variants),
            'frozen_same_field_position_two_jet_errors':freeze,
            'core_scalar_full_two_jet_error':core_error,'tail_scalar_full_two_jet_error':tail_error,
            'core_and_open_tail_metric_two_jet_error':port_metric_error,
            'numerical_core_position_two_jet_errors':core_positions,
            'target_anchor_schema':target.source.anchor_definition['schema'],
            'target_height_base_schema':target.height_base_definition['schema'],
            'transport_receipt_sha256':digest(receipt),'selected_receipt_sha256':digest(selected_receipt)})
        if saved is None:saved=(raw,selected_raw)
    raw,selected_raw=saved;rejects={}
    cases={'wrong_anchor_bytes_sha':lambda:build_core_transport(raw,expected_anchor_sha256='0'*64,**opts),
        'wrong_selected_bytes_sha':lambda:build_core_transport(raw,selected_report_bytes=selected_raw,expected_selected_sha256='0'*64,**opts),
        'different_height_basis':lambda:build_core_transport(raw,selected_report_bytes=selected_raw,**{**opts,'height_free':8}),
        'different_body_basis':lambda:build_core_transport(raw,selected_report_bytes=selected_raw,**{**opts,'metric_free':4}),
        'out_of_box_no_clipping':lambda:build_core_transport(raw,selected_report_bytes=selected_raw,
            initializer_bounds={name:(-1e-8,1e-8) for name in ['u','v','height','metric']},**opts),
        'artificial_bypass_rejects_research_target':lambda:build_core_transport(raw,**{**opts,'target_minor':'37/100'}),
        'non_public_actions_rejected':lambda:require_public_actions({})}
    bad=json.loads(raw);bad['exact_field_coefficients'][0]='1/3'
    cases['tampered_source_exact_coefficient']=lambda:build_core_transport(json.dumps(bad).encode(),**opts)
    for name,call in cases.items():
        try:call();rejects[name]=False
        except (ValueError,PermissionError):rejects[name]=True
    boolean_keys=['transported_c0_bits_equal','semantic_label_map_is_complete','source_and_target_core_differ',
        'source_and_target_seed_differ','source_and_target_complete_g_differ','source_and_target_heat_identity_differ',
        'same_exact_tail_definition','zero_initializer_height_and_body_are_exactly_zero','selected_uv_bits_equal',
        'selected_height_bits_equal','selected_body_bits_equal','immutable_height_anchor_not_replaced_by_selected',
        'GH_Nb_and_freeze_identity_preserved','evaluation_variants_preserve_subclass']
    passed=(all(rejects.values()) and all(all(row[k] for k in boolean_keys) and row['original_234_count']==234
        and max(row['frozen_same_field_position_two_jet_errors'].values())==0
        and row['core_scalar_full_two_jet_error']<1e-10 and row['tail_scalar_full_two_jet_error']<1e-10
        and row['core_and_open_tail_metric_two_jet_error']<1e-10
        and max(row['numerical_core_position_two_jet_errors'].values())<1e-8 for row in rows))
    return {'schema':'elliptic-core-transport-artificial-development-v1','passed':bool(passed),
        'checks':rows,'rejected_inputs':rejects,'artificial_source_core':{'A':'9/10','B':'18/25'},
        'artificial_target_minor':'2/3','research_target_was_not_constructed':True,
        'research_geometry_evaluated':False,'optimizer_calls':0,
        'finite_artificial_comparisons_are_not_continuous_geometric_certificates':True}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check-only',action='store_true',required=True)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    try:answer=developer_check()
    except Exception as exc:
        answer={'schema':'elliptic-core-transport-artificial-development-v1','passed':False,
            'artificial_inputs_only':True,'research_geometry_evaluated':False,
            'error_type':type(exc).__name__,'error':str(exc),'traceback':traceback.format_exc()}
    answer['source_files_sha256']=implementation_hashes();atomic_save(args.out,answer)
    print(json.dumps({'out':str(args.out),'passed':answer['passed']}),flush=True)
    if not answer['passed']:raise SystemExit(1)


if __name__=='__main__':main()
