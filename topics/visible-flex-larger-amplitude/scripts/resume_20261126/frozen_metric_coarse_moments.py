#!/usr/bin/env python3
"""Complete coarse Gram for one FROZEN target: keep every residual mean.

FrozenMetricOperator has J_fixed=D(s) J_original with the fixed positive
diagonal D. This module assembles exactly that coarse Gram using the old
R681 angular/radial algebra and the current R664 blocks. It never subtracts
the R684 moving-target mean derivatives and never changes the fixed g.

The optional SPD preparation can feed R685 v5. Failure before PCG selects
the original complete fixed-target v3 QP; no spectrum clipping or silent
jitter is supplied. Numerical calls require public repository Actions.
"""
from functools import lru_cache
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

import numpy as np


SCHEMA='fixed-target-complete-coarse-Gram-with-all-means-v1'
FROZEN_TRANSFORM_SHA256='9d6440ab9f86cfe5312b78643e704a3ec861f2c5b6fd45047461af92eca81d28'
ORIGINAL_MOMENTS_SHA256='da083ae9b20674a29121c25d5b57ef867fba442559a50791b7fc0b43d4db5719'


class CoarseLayoutUnavailable(ValueError):
    """The known zero-core coarse shortcut is unavailable; retain full J."""


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS','').lower()!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific frozen-target coarse construction belongs in public Actions')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


@lru_cache(maxsize=None)
def _helpers(path=None):
    path=(Path(path).resolve() if path is not None else
        Path(__file__).resolve().parent.parent/'resume_20261120/full_phi_coarse_moments.py')
    if not path.is_file() or sha(path)!=ORIGINAL_MOMENTS_SHA256:
        raise ValueError('Use the complete frozen R681 angular/radial helper source')
    name='fixed_target_complete_original_moment_helpers'
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module


def _frozen_source(function,role):
    function=getattr(function,'__func__',function)
    code=getattr(function,'__code__',None)
    if code is None:
        raise ValueError('The fixed target needs its actual published wrapper: '+role)
    path=Path(code.co_filename).resolve()
    if not path.is_file() or sha(path)!=FROZEN_TRANSFORM_SHA256:
        raise ValueError('The fixed-target wrapper source differs: '+role)
    return dict(path=str(path),sha256=FROZEN_TRANSFORM_SHA256,
        bytes=path.stat().st_size,symbol=function.__qualname__)


def _zero_core_contract(helpers,basis):
    try:
        return dict(literal_B=helpers._source(basis.free_direction,'basis'),
            literal_BT=helpers._source(basis.transpose_free,'basis'),
            literal_B_candidate=helpers._source(basis.candidate,'basis_base'))
    except ValueError as error:
        raise CoarseLayoutUnavailable(
            'The full published B source with an identically zero leading core block is unavailable: '+str(error)) from error


def assemble_current_coarse_gram(bridge,frame,*,stage_block=8,provenance=None,
        progress=None,original_moments_source=None):
    """Return fixed-g Gc=A_fixed,coarse^T A_fixed,coarse and its scope.

    Consume an already frozen target materialization and current field
    cache. No target evaluator, field reader, J or J* is called here.
    Actual call counts are owned by prepare_current_frozen_preconditioner.
    """
    require_actions()
    started=time.monotonic()
    helpers=_helpers(original_moments_source)
    frozen,b,parameters=bridge.original,frame.basis,bridge.parameters
    frozen_sources=dict(frozen_wrapper=_frozen_source(type(frozen).__init__,'constructor'),
        fixed_J=_frozen_source(type(frozen).jvp,'J'),
        fixed_Jstar=_frozen_source(type(frozen).vjp,'Jstar'))
    o=frozen.original_operator
    if frame.coordinates.problem is not frozen or frame.coarse_size!=b.dimension:
        raise ValueError('Use this actual fixed-target bridge and original coordinate frame')
    if (frozen._base_x is None or frozen._base_state is None
            or not np.array_equal(frozen._base_x,bridge.x)):
        raise ValueError('Use the existing fixed-target residual state at the actual bridge x')
    if (o._base_x is None or o._base_p is None or o._base_first is None
            or not np.array_equal(o._base_x,bridge.x)):
        raise ValueError('Use the existing complete physical first-jet cache at the same x')
    literal_sources=_zero_core_contract(helpers,b)
    sources=dict(**frozen_sources,**literal_sources,
        frame=helpers._source(type(frame).__init__,'frame'),
        bridge=helpers._source(type(bridge).__init__,'hessian'),
        R664_blocks=helpers._source(type(bridge.blocks).whiten_columns,'hessian'),
        cached_first_jet_access=helpers._source(o._first_batch,'batch'),
        actual_cache_builder=helpers._source(o.set_base,'batch'),
        observation_pair=helpers._source(o._stage_pair,'observed'),
        unpack=helpers._source(o.unpack,'dense'))
    tail=getattr(o,'reference_tail_context',None)
    if tail is not getattr(b.o,'reference_tail_context',None):
        raise ValueError('Retain the same actual h/f/k context for the complete field and coarse B')
    if tail is None:
        sources['first_jet_builder']=helpers._source(o._first_batch_uncached,'batch')
        model=dict(representation='original analytic lift',reference_tail_lambda=0.)
    else:
        sources['first_jet_builder']=helpers._source(o._first_batch_uncached,'reference_tail')
        sources['reference_definition']=helpers._source(tail.definition,'reference_tail')
        definition=tail.definition()
        model=dict(representation='R671 exact reference tail lift',
            reference_tail_lambda=float(tail.lambda_value),model_definition=definition,
            model_identity_sha256=hashlib.sha256(json.dumps(definition,sort_keys=True,
                separators=(',',':'),allow_nan=False).encode()).hexdigest())
    if any(getattr(b.o,key)!=getattr(o,key) for key in ('J','n','M','K','free_size')):
        raise ValueError('Retain the complete native and observed free layouts')
    if (not np.array_equal(b.o.mesh,o.mesh) or not np.array_equal(b.o.phi,o.phi)
            or not np.array_equal(b.o.freq,o.freq)):
        raise ValueError('Retain all actual nodes, angle rows and modes')
    P,N,dimension=int(o.P),int(o.N),int(b.dimension)
    stage_block=int(stage_block)
    if stage_block<1:
        raise ValueError('A positive radial assembly block is required')
    first=o._base_first
    if first.shape!=(2,P,N,3) or np.iscomplexobj(first):
        raise ValueError('Need all complete cached moving-frame first jets')
    real=helpers._real
    rho=np.array(real(o._base_p.rho,(N,),'current physical rho'),copy=True)
    a=np.array(real(o.a,(P,),'original intermediate target a'),copy=True)
    radial=np.array(real(bridge.radial,(P,),'all radial weights',positive=True),copy=True)
    orbit=np.array(real(o.multiplicity,(N,),'all orbit weights',positive=True),copy=True)
    phi=np.array(real(o.phi,(N,),'all actual angles'),copy=True)
    fixed_scale=real(frozen.fixed_scale,(P,3),'fixed target normalization',positive=True)
    fixed_E=real(frozen.fixed_radial,(P,),'fixed radial target',positive=True)
    fixed_C=real(frozen.fixed_angular,(P,),'fixed angular target over a squared',positive=True)
    if any(value.flags.writeable for value in (fixed_scale,fixed_E,fixed_C)):
        raise ValueError('The target materialization must remain immutable during the QP')
    target_identity=frozen.target.identity
    if (not isinstance(target_identity,str) or len(target_identity)!=64
            or frozen.target_materialization.get('target_identity_sha256')!=target_identity):
        raise ValueError('The current fixed scale has no matching frozen-target identity')
    if float(orbit.sum())!=int(o.full_N):
        raise ValueError('Keep the exact complete angular orbit multiplicities')
    if bridge.blocks.parameters is not parameters:
        raise ValueError('Use the same current fixed-target R664 block parameters')
    for key in ('axis','offaxis','root_plus','root_off','root_minus'):
        if np.shape(getattr(bridge.blocks,key))!=(P,N):
            raise ValueError('The current R664 blocks must cover every original observation')
    cells=np.asarray(o.observation_cells)
    real(o.observation_weights,(P,3,6),'complete observation weights')
    if (cells.shape!=(P,) or not np.issubdtype(cells.dtype,np.integer)
            or np.any(cells<0) or np.any(cells>=o.J-1) or o.lift_scalar.shape!=(P,6)):
        raise ValueError('Use the complete current observation plan and physical six-scalar lift')
    pairs=np.asarray(b.pairs)
    if pairs.shape!=(dimension,2):
        raise ValueError('The literal coarse pair layout changed')
    ri,cj=pairs.T
    nodes=np.array(real(b.node_jets,(b.nb,o.J,3),'literal nodal coarse three jets'),copy=True)
    nodes[:,0,:2]=0.
    nodes[:,-1,:]=0.
    for radial_index,channel_index in pairs:
        if b.channels[channel_index][0]=='Z' and nodes[radial_index,0,2]!=0:
            raise CoarseLayoutUnavailable('This shortcut retains the published fixed A0_Z coarse slots only')
    if tuple(pairs[-1])!=(b.height_radial,1):
        raise CoarseLayoutUnavailable('The physical-height column changed')
    nodal=nodes.transpose(1,2,0)
    angular=helpers._AngularMoments(b.channels,phi,orbit)
    normalizer=float(radial.sum())*int(o.full_N)
    gamma=float(parameters.k)/(float(parameters.scale)**2*normalizer)
    if not np.isfinite(gamma) or gamma<=0:
        raise ValueError('The actual fixed-target normalized Phi factor must be positive')
    normal=np.zeros((dimension,dimension))
    maximum_active=zero_column_stages=assembled_stages=0
    for start in range(0,P,stage_block):
        stop=min(start+stage_block,P)
        V,d=first[0,start:stop],first[1,start:stop]
        ar=a[start:stop,None]*rho[None]
        if (not np.isfinite(V).all() or not np.isfinite(d).all()
                or not np.isfinite(ar).all() or np.any(ar==0)):
            raise ArithmeticError('Invalid current physical cache or original Gram denominator')
        derivative=np.zeros((stop-start,N,3,6))
        derivative[:,:,0,:3]=2*V
        derivative[:,:,1,:3]=d/ar[:,:,None]
        derivative[:,:,1,3:]=V/ar[:,:,None]
        derivative[:,:,2,3:]=2*d/(ar*ar)[:,:,None]
        # Fixed target: THIS is the whole derivative. No material mean,
        # density weight, moving-target normalization or zero-mode removal.
        derivative*=fixed_scale[start:stop,None,:,None]
        block=helpers._block_view(bridge.blocks,start,stop)
        weighted=block.whiten_columns(derivative)
        tensor=weighted.transpose(0,1,3,2)@weighted
        kernels=angular.contract(tensor)
        y,u=helpers._radial_pair(o,nodal,b.height_radial,start,stop)
        c=angular.nc
        for local,stage in enumerate(range(start,stop)):
            by,bu=y[local,ri],u[local,ri]
            active=np.flatnonzero((by!=0)|(bu!=0))
            maximum_active=max(maximum_active,len(active))
            if not len(active):
                zero_column_stages+=1
                continue
            channel=cj[active]
            ix=np.ix_(channel,channel)
            ku=kernels[local,:c,:c][ix]
            kuy=kernels[local,:c,c:][ix]
            ky=kernels[local,c:,c:][ix]
            v,z=bu[active],by[active]
            increment=(np.outer(v,v)*ku+np.outer(v,z)*kuy
                +np.outer(z,v)*kuy.T+np.outer(z,z)*ky)
            normal[np.ix_(active,active)]+=radial[stage]*increment
        assembled_stages=stop
        if progress is not None:
            progress(dict(event='fixed_target_coarse_moments_block',stages_done=stop,
                total_stages=P,maximum_active_coarse_columns=maximum_active,
                elapsed_seconds=time.monotonic()-started))
    normal*=gamma
    if not np.isfinite(normal).all():
        raise ArithmeticError('The current fixed-target coarse Gram is not finite')
    skew=float(np.max(np.abs(normal-normal.T),initial=0.))
    raw_diagonal=np.diag(normal)
    diagonal_min=float(np.min(raw_diagonal))
    negative_diagonal_count=int(np.count_nonzero(raw_diagonal<0))
    maximum_entry=float(np.max(np.abs(normal),initial=0.))
    normal=.5*normal+.5*normal.T
    result,whitening=helpers._apply_original_whitening(normal,frame,cj)
    report=dict(schema=SCHEMA,status='assembled_current_fixed_target_complete_coarse_Gram',
        assembly_source=dict(path=str(Path(__file__).resolve()),sha256=sha(__file__),
            bytes=Path(__file__).stat().st_size),sources=sources,
        original_moment_helper_source_sha256=ORIGINAL_MOMENTS_SHA256,
        caller_provenance=dict(provenance or {}),model=model,
        fixed_target_identity_sha256=target_identity,
        target_materialization=frozen.target_materialization,
        fixed_target_full_angles=int(frozen.target.full_angles),current_full_angles=int(o.full_N),
        fixed_target_unchanged=True,moving_mean_projection_used=False,
        every_original_mean_constraint_retained=True,low_rank_mean_correction_used=False,
        coarse_derivative='J_fixed,coarse = fixed_scale(s) * J_original,coarse; complete K00 only',
        actual_x_sha256=helpers._array_sha(bridge.x),
        actual_fixed_scale_sha256=helpers._array_sha(fixed_scale),
        actual_fixed_radial_sha256=helpers._array_sha(fixed_E),
        actual_fixed_angular_over_a2_sha256=helpers._array_sha(fixed_C),
        actual_original_a_sha256=helpers._array_sha(a),actual_rho_sha256=helpers._array_sha(rho),
        actual_radial_weight_sha256=helpers._array_sha(radial),actual_orbit_weight_sha256=helpers._array_sha(orbit),
        actual_scale_sha256=helpers._array_sha(frame.scale),
        actual_coarse_diagonal_sha256=helpers._array_sha(frame.diagonal),
        actual_coarse_cholesky_sha256=helpers._array_sha(frame.chol),
        literal_nodal_basis_sha256=helpers._array_sha(b.node_jets),
        actual_mesh_sha256=helpers._array_sha(o.mesh),actual_angles_sha256=helpers._array_sha(phi),
        p=int(parameters.p),epsilon=float(parameters.epsilon),spectral_scale=float(parameters.scale),
        normalization=normalizer,outer_half_hessian_factor=gamma,
        actual_bridge_true_gradient_factor=float(bridge.true_gradient_factor),
        stages=P,evaluated_angles=N,full_angles=int(o.full_N),rows=P*N*3,
        full_rows=P*int(o.full_N)*3,full_field_M=int(o.M),
        coarse_variables=dimension,coarse_maximum_mode=angular.max_mode,
        angular_channels=angular.nc,angular_moment_orders=angular.span,
        symmetric_six_tensor_components=21,stage_block=stage_block,
        assembled_stages=assembled_stages,maximum_active_coarse_columns=maximum_active,
        zero_column_stages=zero_column_stages,
        all_current_field_modes_and_observation_rows_retained=True,
        original_coarse_core_variation=False,
        full_free_core_derivatives_retained_by_original_J=True,
        reference_fixed_kprime_in_current_cache=tail is not None,
        raw_coarse_float_skew=skew,raw_coarse_diagonal_minimum=diagonal_min,
        raw_negative_diagonal_count=negative_diagonal_count,
        raw_maximum_absolute_entry=maximum_entry,whitening=whitening,
        eigenvalue_clipping=False,jitter_added=False,
        actual_operator_counts_owned_by_caller=True,
        expected_extra_J_calls_by_formula=0,expected_extra_Jstar_calls_by_formula=0,
        target_recomputed_from_current_candidate=False,
        output_bytes=int(result.nbytes),elapsed_seconds=time.monotonic()-started,
        mathematical_objective_or_regularization_changed=False,
        fixed_g_refinement_convergence_claimed=False,continuous_geometry_certified=False,
        floating_outward_certificate=False)
    return result,report


class _ActualOperatorCounts:
    """Temporary instance-entry counters; report nested wrapper/base roles."""
    def __init__(self,frozen):
        self.counts={};self.saved=[]
        self.objects=[('wrapper',frozen),('physical_base',frozen.original_operator)]

    def __enter__(self):
        try:
            for role,obj in self.objects:
                for name in ('jvp','vjp','residual','raw_residual'):
                    method=getattr(obj,name);key=role+'.'+name
                    self.counts[key]=0
                    present=name in vars(obj);old=vars(obj).get(name)
                    def counted(*args,_method=method,_key=key,**kwargs):
                        self.counts[_key]+=1
                        return _method(*args,**kwargs)
                    self.saved.append((obj,name,present,old));setattr(obj,name,counted)
        except BaseException:
            self.__exit__(None,None,None)
            raise
        return self

    def __exit__(self,exc_type,exc,traceback):
        for obj,name,present,old in reversed(self.saved):
            if present:setattr(obj,name,old)
            else:delattr(obj,name)
        self.saved.clear()
        return False


def prepare_current_frozen_preconditioner(frame_module,coordinates,height_map,
        basis,diagonal,chol,bridge,damping,*,stage_block=8,provenance=None,
        progress=None,original_moments_source=None):
    """Return (optional SPD map, detail) for unchanged fixed-g v5 / v3.

    On None, use the original complete fixed-target v3 QP. Do not transfer
    the R688 moving-mean projection or a Gram from another target/parent.
    """
    require_actions()
    started=time.monotonic();frame=gram=None
    detail=dict(enabled=True,status='construction_started',
        actual_direction_damping=float(damping),fixed_target_identity_sha256=bridge.original.target.identity,
        current_fixed_target_and_full_J_unchanged=True,moving_mean_projection_used=False,
        all_original_mean_constraints_retained=True,
        original_mother_norm_and_coarse_whitening_retained=True)
    counter=_ActualOperatorCounts(bridge.original)
    try:
        with counter:
            helpers=_helpers(original_moments_source)
            _zero_core_contract(helpers,basis)
            _frozen_source(type(bridge.original).__init__,'constructor')
            mu=float(damping);mu2=mu*mu
            if not np.isfinite(mu) or mu<=0:
                raise ValueError('Use the current actual positive fixed-g damping')
            if not np.isfinite(mu2) or mu2<=0:
                raise frame_module.SmallSPDUnavailable('actual damping squared','Not finite positive')
            beta=1./mu2
            if not np.isfinite(beta) or beta<=0:
                raise frame_module.SmallSPDUnavailable('background inverse scale','1/mu^2 is not finite positive')
            detail['background_inverse_scale']=beta
            frame=frame_module.CoarseFrame(coordinates,height_map,basis,diagonal,chol,provenance=provenance)
            detail['frame']=frame.metadata()
            gram,data_report=assemble_current_coarse_gram(bridge,frame,
                stage_block=stage_block,provenance=provenance,progress=progress,
                original_moments_source=original_moments_source)
            detail['current_fixed_target_coarse_Gram']=data_report
            preconditioner=frame_module.FixedSPDPreconditioner(frame,gram,mu,beta,data_provenance=data_report)
            metadata=preconditioner.metadata()
            metadata['original_source_active_face_note']=metadata.get('active_face_usage')
            metadata['active_face_usage']='R685 constrained inverse B-BQ^T(QBQ^T)^-1QB; actual v5 cache diagnostics govern'
            detail.update(status='prepared_current_fixed_target_SPD',fixed_metadata=metadata,
                fallback_to_frozen_v3=False)
            return preconditioner,detail
    except CoarseLayoutUnavailable as error:
        detail.update(status='zero_core_shortcut_unavailable_original_fixed_target_v3_selected',
            failure=dict(kind=type(error).__name__,reason=str(error)),fallback_to_frozen_v3=True,
            full_fixed_target_J_retained=True)
        return None,detail
    except frame_module.SmallSPDUnavailable as error:
        detail.update(status='small_SPD_unavailable_original_fixed_target_v3_selected',
            failure=error.record(),fallback_to_frozen_v3=True,
            numerical_failure_is_not_physical_infeasibility=True,
            no_jitter_no_clipping_no_changed_damping=True)
        return None,detail
    except (ArithmeticError,MemoryError) as error:
        detail.update(status='arithmetic_or_resource_unavailable_original_fixed_target_v3_selected',
            failure=dict(kind=type(error).__name__,reason=str(error)),fallback_to_frozen_v3=True,
            numerical_failure_is_not_physical_infeasibility=True,
            no_jitter_no_clipping_no_changed_damping=True)
        return None,detail
    finally:
        observed=dict(counter.counts)
        detail.update(construction_seconds=time.monotonic()-started,
            actual_operator_entry_calls=observed,operator_instrumentation_complete=len(observed)==8,
            actual_additional_J_calls=observed.get('physical_base.jvp'),
            actual_additional_Jstar_calls=observed.get('physical_base.vjp'),
            all_observed_J_and_Jstar_entries_zero=bool(len(observed)==8 and all(
                value==0 for key,value in observed.items() if key.endswith('.jvp') or key.endswith('.vjp'))),
            all_observed_residual_entries_zero=bool(len(observed)==8 and all(
                value==0 for key,value in observed.items() if key.endswith('.residual') or key.endswith('.raw_residual'))),
            operator_count_scope='Separate actual wrapper/base entries, not an independent-product sum',
            temporary_method_wrappers_restored=not counter.saved,
            dense_Gram_reference_released_before_solve=True,
            no_full_J_unit_column_probes_or_fixture=True)
        del gram,frame
