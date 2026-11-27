#!/usr/bin/env python3
"""Complete detached normal-stage J6/J9 from adjacent total-angular frames.

This is an independent working matrix producer.  It never changes selected
roots, stage equations, Newton/J3 evaluations, angular solves, or the active
implicit residual graph.  Original complete AD is the fallback.  Its block
products have a new rounding order and are NOT asserted bitwise equal to AD.
Every scientific operation requires this repository's public Actions.
"""
import ast
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import time

import numpy as np
import torch


SCHEMA = 'complete-closure-value-compatible-adjacent-total-angular-frame-normal-stage-matrices-v1'
ANALYTIC_STAGE_SOURCE_SHA256 = '223afb992e0e9904c30ab20387a92569dc2979dbfde84f75f04e3402b9c5e811'
TORCH_VERSION = '2.5.1'
FRAME_C1_SOURCE_SHA256 = 'c97749c8fae14981a1f86e45845d152134a62039d88b7cfaccfb69fb0665e246'
STAGE_MATRIX_SOURCE_SHA256 = 'f98bf270265f9d41c9c297dd23c2db7da9ea91a039663c1785966e9135795791'
PARENT_OPERATOR_SOURCE_SHA256 = 'd461f660063bfa2aeecc724050d71c6ef98143b9129f7cfe34f22e4043488a7f'
BASE_SOURCE_SHA256 = '552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3'
PROVENANCE_SCHEMA = 'actual-normal-frame-complete-previous-control-provenance-v1'
CONTEXT_SCHEMA = 'actual-normal-frame-point-angle-and-required-data-words-v1'
COUNTER_KEYS = ('frame_contexts', 'frame_provenance_angle_records',
    'matrix_calls_started', 'matrix_calls_completed', 'matrix_calls_failed',
    'requested_stage_angle_blocks', 'adjacent_stage_angle_blocks_assembled',
    'adjacent_stage_angle_blocks_published', 'original_AD_stage_angle_blocks_published',
    'complete_AD_fallback_calls', 'required_data_mismatch_calls',
    'optional_assembly_failure_calls', 'final_frame_angle_attempts',
    'final_frame_angle_returns', 'actual_final_frame_reverse_angle_products',
    'published_six_by_six_angle_blocks', 'published_nine_by_nine_angle_blocks')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific adjacent normal frames require public repository Actions')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()


def definition():
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        parent_complete_operator_source_sha256=PARENT_OPERATOR_SOURCE_SHA256,
        complete_frame_C1_source_sha256=FRAME_C1_SOURCE_SHA256,
        complete_detached_matrix_source_sha256=STAGE_MATRIX_SOURCE_SHA256,
        complete_base_source_sha256=BASE_SOURCE_SHA256,
        complete_analytic_stage_source_sha256=ANALYTIC_STAGE_SOURCE_SHA256,
        local_scalar_matrix_policy='selected analytic working Rodrigues J3; angular assembly does not replace it',
        angular_orders=[1,2],
        matrix_formula='M0=A0 B0^T; M1=A1 B0^T+A0 B1^T; M2=A2 B0^T+2 A1 B1^T+A0 B2^T',
        block_formula='J6=[[M0,0],[M1,M0]]; J9=[[M0,0,0],[M1,M0,0],[M2,2M1,M0]]',
        A='total angular jets of f_u at the SAME selected current-stage controls',
        B='actual stored total angular jets of f_u at the preceding selected controls',
        interior_A_origin='next actual stage frame with complete input-control provenance',
        last_A_origin='one complete current no-grad analytic frame or its full AD fallback at actual final controls',
        complete_three_control_and_frame_jets_preserved=True,
        requested_first_order_may_use_actual_second_order_root=True,
        lower_jet_upgrade_origins_retained=True,
        required_data_words_checked_for_every_used_frame_component=True,
        actual_batch_origins_retained_without_claiming_identical_batches=True,
        complete_original_AD_fallback_on_required_data_word_mismatch=True,
        complete_original_AD_fallback_on_optional_assembly_failure=True,
        all_selected_stage_equations_roots_Newton_J3_and_angular_solves_retained=True,
        original_active_residual_and_all_upstream_parameter_edges_retained=True,
        original_fixed_common_partition_retained=True,
        cached_root_values_or_zero_targets_modified=False,
        jacobian_fields_are_the_only_deliberately_replaced_root_fields=True,
        matrices_are_detached_and_not_active_graph_caches=True,
        old_source_root_cache_imported=False,
        block_products_have_independent_working_rounding_definition=True,
        bitwise_equality_to_unexecuted_AD_claimed=False,
        derivative_or_inverse_rounding_error_enclosed=False,
        speedup_or_success_claimed=False)


def _new_counts():
    return {name:0 for name in COUNTER_KEYS}


def _copy(value):
    return json.loads(json.dumps(value,allow_nan=False))


def _digest(value):
    return (isinstance(value,str) and len(value)==64
        and all(c in '0123456789abcdef' for c in value))


def validate_metadata(value, *, model_identity, operator_source_sha256,
                      expected_definition=None):
    """Pure validation of actual counters and own-point provenance, not science."""
    if not isinstance(value,dict):
        raise ValueError('Require actual adjacent-frame producer metadata')
    expected = definition() if expected_definition is None else expected_definition
    if (expected != definition() or value.get('schema') != SCHEMA
            or value.get('source_sha256') != sha(__file__)
            or value.get('definition') != expected
            or value.get('definition_identity_sha256') != canonical(expected)
            or value.get('actual_model_identity_sha256') != model_identity
            or value.get('actual_operator_source_sha256') != operator_source_sha256
            or not _digest(model_identity) or not _digest(operator_source_sha256)):
        raise ValueError('Bind the complete actual adjacent-frame source and model')
    counts = value.get('actual_counts')
    if (not isinstance(counts,dict) or set(counts) != set(COUNTER_KEYS)
            or any(type(counts[name]) is not int or counts[name]<0 for name in COUNTER_KEYS)
            or counts['matrix_calls_started'] != counts['matrix_calls_completed']+counts['matrix_calls_failed']
            or counts['adjacent_stage_angle_blocks_published'] > counts['adjacent_stage_angle_blocks_assembled']
            or counts['adjacent_stage_angle_blocks_published']+counts['original_AD_stage_angle_blocks_published']
                != counts['published_six_by_six_angle_blocks']+counts['published_nine_by_nine_angle_blocks']
            or counts['final_frame_angle_returns'] > counts['final_frame_angle_attempts']
            or counts['complete_AD_fallback_calls'] > counts['matrix_calls_started']):
        raise ValueError('Adjacent-frame actual counters are not complete or consistent')
    seconds = value.get('matrix_call_seconds')
    if (isinstance(seconds,bool) or not isinstance(seconds,(int,float))
            or not math.isfinite(seconds) or seconds<0):
        raise ValueError('Keep actual nonnegative producer time without an acceleration claim')
    if any(value.get(key) is not flag for key,flag in (
            ('selected_Newton_and_J3_unchanged_by_angular_assembly',True),
            ('original_active_implicit_chain_unchanged',True),
            ('root_success_inferred_from_matrix_production',False),
            ('measured_acceleration_claimed',False),
            ('matrix_arithmetic_errors_enclosed',False),
            ('matrix_or_data_arrays_retained_in_kernel',False))):
        raise ValueError('Keep the exact independent working-producer scope')
    last = value.get('last_call')
    if last is not None:
        if (not isinstance(last,dict) or last.get('schema') != 'actual-adjacent-normal-matrix-call-v1'
                or not _digest(last.get('current_full_point_sha256'))
                or last.get('model_identity_sha256') != model_identity
                or last.get('operator_source_sha256') != operator_source_sha256
                or last.get('requested_angular_order') not in (1,2)
                or type(last.get('angle_count')) is not int or last['angle_count']<=0
                or type(last.get('normal_stage_count')) is not int or last['normal_stage_count']<1
                or type(last.get('completed')) is not bool
                or type(last.get('protected_root_fields_unchanged')) is not bool):
            raise ValueError('The last call must retain its own real point and complete scope')
        orders = last.get('actual_root_orders')
        if (not isinstance(orders,list) or len(orders)!=last['angle_count']
                or any(type(v) is not int or v not in (1,2)
                    or v<last['requested_angular_order'] for v in orders)):
            raise ValueError('Keep actual higher-order roots independently of the request order')
        records = last.get('stage_records')
        if not isinstance(records,list) or len(records)>last['normal_stage_count']:
            raise ValueError('The actual matrix-stage record list is invalid')
        for index,record in enumerate(records):
            size=3*(last['requested_angular_order']+1)
            if (not isinstance(record,dict) or record.get('normal_stage_index')!=index+1
                    or record.get('matrix_shape')!=[last['angle_count'],size,size]
                    or not _digest(record.get('matrix_words_sha256'))
                    or record.get('origin') not in ('adjacent_total_frames','complete_original_AD')):
                raise ValueError('Keep every produced matrix stage and its actual numerical origin')
        if last['completed'] and (len(records)!=last['normal_stage_count']
                or not last['protected_root_fields_unchanged']
                or last.get('published_origin') not in ('adjacent_total_frames','complete_original_AD')):
            raise ValueError('A completed matrix call requires every stage and the root protection check')
    elif counts['matrix_calls_started']:
        raise ValueError('Do not omit the last actual matrix-call record')
    return _copy(value)


def _array(value, shape):
    if isinstance(value,torch.Tensor):
        if (value.dtype!=torch.float64 or value.device.type!='cpu' or value.requires_grad
                or value.grad_fn is not None):
            raise ValueError('Use detached CPU binary64 values only')
        result=value.detach().cpu().numpy()
    else:
        result=np.asarray(value)
    if (result.dtype!=np.dtype(np.float64) or tuple(result.shape)!=tuple(shape)
            or not bool(np.isfinite(result).all())):
        raise ValueError('Require every finite binary64 value in the declared complete shape')
    return result


def _words_sha(value, shape):
    value=_array(value,shape)
    h=hashlib.sha256(str(value.dtype).encode())
    h.update(json.dumps(list(value.shape)).encode())
    h.update(np.ascontiguousarray(value).tobytes())
    return h.hexdigest()


def _raw_words_sha(value):
    return _words_sha(value,tuple(value.shape))


class AdjacentNormalFrameMatrices:
    """One source-bound numerical producer, without a cross-call value cache."""
    def __init__(self,q,*,frame_c1_module,stage_matrix_module):
        require_actions()
        if torch.__version__.split('+')[0]!=TORCH_VERSION:
            raise ValueError('Use the declared CPU Torch version')
        if (sha(frame_c1_module.__file__)!=FRAME_C1_SOURCE_SHA256
                or sha(stage_matrix_module.__file__)!=STAGE_MATRIX_SOURCE_SHA256
                or q.frame_c1.q is not q or q.stage_matrices.q is not q
                or q.frame_c1.definition!=frame_c1_module.definition()
                or q.stage_matrices.definition!=stage_matrix_module.definition()):
            raise ValueError('Bind both entire unchanged frame/J3 helpers')
        self.q,self.frame_module,self.stage_module=q,frame_c1_module,stage_matrix_module
        self.definition=definition()
        self.model_identity=q.identity
        self.model_object=q.model
        self.base_model_object=q.base.model
        self.operator_source=q.model.get('source_sha256')
        if (q.model.get('adjacent_normal_frame_matrices')!=self.definition
                or canonical(q.model)!=q.identity
                or q.model.get('normal_frame_C1_reuse')!=frame_c1_module.definition()
                or q.model.get('detached_stage_matrix_reuse')!=stage_matrix_module.definition()
                or q.model.get('base_source_sha256')!=BASE_SOURCE_SHA256
                or q.model.get('base_complete_model')!=q.base.model
                or canonical(q.base.model)!=q.base.identity
                or q.model.get('complete_first_angular_implicit_dimension')!=6*q.normal_stage_count
                or q.model.get('complete_second_angular_implicit_dimension')!=9*q.normal_stage_count):
            raise ValueError('The complete source, model, free space and finite chain differ')
        path=Path(q._normal_frame_jets.__func__.__code__.co_filename).resolve()
        if sha(path)!=self.operator_source:
            raise ValueError('The actual complete normal operator source differs')
        tree=ast.parse(path.read_bytes())
        classes=[n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='ZeroClosureOperator']
        if len(classes)!=1:
            raise ValueError('Read one complete actual normal operator class')
        nodes={n.name:n for n in classes[0].body if isinstance(n,ast.FunctionDef)}
        self.methods={}
        for name,expected in frame_c1_module.complete_method_ast().items():
            bound=getattr(q,name);function=bound.__func__
            if (bound.__self__ is not q or name not in nodes
                    or Path(function.__code__.co_filename).resolve()!=path
                    or canonical(frame_c1_module._ast_value(nodes[name]))!=expected
                    or function is not q.stage_matrices.methods[name]
                    or function.__globals__.get('SCHEMA')!=q.model.get('schema')
                    or function.__globals__.get('ADJACENT_FRAME_SOURCE_SHA256')!=sha(__file__)
                    or function.__globals__.get('STAGE_MATRIX_SOURCE_SHA256')!=STAGE_MATRIX_SOURCE_SHA256
                    or function.__globals__.get('ANALYTIC_STAGE_SOURCE_SHA256')!=ANALYTIC_STAGE_SOURCE_SHA256):
                raise ValueError('An original full method or explicit source pin changed: '+name)
            self.methods[name]=function
        self.tensor=q._normal_frame_jets.__func__.__globals__['tensor']
        self.partition=tuple(str(v) for v in q.normal_step_nodes)
        self.carriers=tuple(float(v).hex() for v in q.normal_step_carriers)
        if (len(self.partition)!=q.normal_stage_count+1
                or self.partition[0]!='0' or self.partition[-1]!='1'
                or tuple(float(Fraction(v)).hex() for v in self.partition)!=self.carriers
                or q.model.get('exact_normal_step_nodes')!=list(self.partition)):
            raise ValueError('Keep the complete common exact finite partition')
        self.counts=_new_counts()
        self.matrix_call_seconds=0.
        self.last_call=None

    def _binding(self,data,keys,order):
        require_actions()
        q=self.q
        if (type(order) is not int or order not in (1,2)
                or q.model is not self.model_object or q.base.model is not self.base_model_object
                or canonical(q.model)!=self.model_identity or q.identity!=self.model_identity
                or q.model.get('source_sha256')!=self.operator_source
                or q.model.get('adjacent_normal_frame_matrices')!=self.definition
                or tuple(str(v) for v in q.normal_step_nodes)!=self.partition
                or tuple(float(v).hex() for v in q.normal_step_carriers)!=self.carriers
                or any(getattr(q,n).__func__ is not f for n,f in self.methods.items())
                or not self.frame_module._all_data_detached(data)
                or data.get('order') not in (1,2) or data['order']<order
                or len(keys)!=len(data['core'][0]) or not keys
                or any(not isinstance(v,str) or not math.isfinite(float.fromhex(v))
                    or float.fromhex(v).hex()!=v for v in keys)):
            raise ValueError('Keep the complete same-model point, detached data and ordered literal angles')
        point=_words_sha(q._current_x,(q.free_size,))
        if point!=q._current_point_sha256:
            raise ValueError('The actual complete current free point differs')
        carrier=canonical(dict(mesh=_raw_words_sha(q.mesh),gauss_u=_raw_words_sha(q.gauss_u),
            gauss_w=_raw_words_sha(q.gauss_w),S=float(q.S).hex(),J=int(q.J),
            integration_order=int(q.integration_order),partition=list(self.partition),
            carrier_nodes=list(self.carriers)))
        return dict(model_identity_sha256=self.model_identity,
            operator_source_sha256=self.operator_source,current_full_point_sha256=point,
            complete_integral_carriers_sha256=carrier,
            ordered_literal_angles_sha256=canonical(list(keys)),
            actual_data_angular_order=int(data['order']))

    def frame_context(self,data,keys,order):
        """Hash actual per-angle required input words once for this root batch."""
        binding=self._binding(data,keys,order)
        names=('T','Tp','Tpp');wnames=('W','Wp','Wpp')
        context=[]
        for i,key in enumerate(keys):
            prefixes=[]
            for j in range(order+1):
                terms={}
                for name in names[:j+1]:
                    for role in ('meridians','reference'):
                        value=data[role][name][:,i:i+1]
                        terms[role+'.'+name]=_raw_words_sha(value)
                for name in wnames[:j+1]:
                    terms['W.'+name]=_raw_words_sha(data['W'][name][:,i:i+1])
                for role in ('core','cap','reference_core','reference_cap'):
                    for k in range(j+1):
                        terms[role+'.'+str(k)]=_raw_words_sha(data[role][k][i:i+1])
                prefixes.append(canonical(terms))
            value=dict(schema=CONTEXT_SCHEMA,**binding,literal_angle_hex=key,
                source_requested_angular_order=order,required_data_prefix_sha256=prefixes)
            context.append(value)
        self.counts['frame_contexts']+=1
        return dict(binding=binding,angle_contexts=context,
            data_object=data,data_object_identity=self.frame_module._data_identity(data),
            keys=tuple(keys),order=order)

    def capture_frame_inputs(self,context,previous,frame,stage_index,old_stages=None):
        """Record actual inputs AFTER old lower frame values have been restored."""
        q=self.q;keys=context['keys'];count=len(keys);order=context['order']
        if (type(stage_index) is not int or not 0<=stage_index<q.normal_stage_count
                or context['binding']!=self._binding(context['data_object'],keys,order)
                or self.frame_module._data_identity(context['data_object'])!=context['data_object_identity']
                or (old_stages is not None and (order!=2 or len(old_stages)!=count))):
            raise ValueError('The actual frame input provenance left its current complete root call')
        p=_array(previous,(count,3,6));b=_array(frame,(count,3,3,6))
        answer=[]
        for angle in range(count):
            sources=[]
            for j in range(order+1):
                if old_stages is not None and j<2:
                    old=old_stages[angle].get('frame_provenance')
                    self._check_record_integrity(old,old_stages[angle]['frame'],keys[angle],stage_index)
                    origin=_copy(old['jet_sources'][j])
                    if (origin['required_previous_prefix_sha256']!=_words_sha(p[angle,:j+1],(j+1,6))
                            or origin['actual_frame_component_sha256']!=_words_sha(b[angle,j],(3,6))):
                        raise ValueError('An upgrade changed a prior lower frame input or output word')
                else:
                    origin=dict(context=_copy(context['angle_contexts'][angle]),
                        actual_previous_all_three_jets_sha256=_words_sha(p[angle],(3,6)),
                        required_previous_prefix_sha256=_words_sha(p[angle,:j+1],(j+1,6)),
                        actual_frame_component_sha256=_words_sha(b[angle,j],(3,6)),
                        component_angular_order=j)
                sources.append(origin)
            value=dict(schema=PROVENANCE_SCHEMA,source_sha256=sha(__file__),
                model_identity_sha256=self.model_identity,operator_source_sha256=self.operator_source,
                current_full_point_sha256=context['binding']['current_full_point_sha256'],
                literal_angle_hex=keys[angle],normal_stage_index=stage_index+1,
                actual_root_angular_order=order,
                current_previous_all_three_jets_sha256=_words_sha(p[angle],(3,6)),
                actual_frame_all_three_jets_sha256=_words_sha(b[angle],(3,3,6)),
                lower_jet_origins_preserved_on_upgrade=old_stages is not None,
                jet_sources=sources)
            value['provenance_identity_sha256']=canonical(value)
            answer.append(value)
        self.counts['frame_provenance_angle_records']+=count
        return answer

    def _check_record_integrity(self,value,frame,key,index):
        if not isinstance(value,dict):
            raise ValueError('Do not import an old root without actual frame-input provenance')
        payload={k:v for k,v in value.items() if k!='provenance_identity_sha256'}
        order=value.get('actual_root_angular_order')
        if (value.get('schema')!=PROVENANCE_SCHEMA or value.get('source_sha256')!=sha(__file__)
                or value.get('model_identity_sha256')!=self.model_identity
                or value.get('operator_source_sha256')!=self.operator_source
                or value.get('current_full_point_sha256')!=self.q._current_point_sha256
                or value.get('literal_angle_hex')!=key or value.get('normal_stage_index')!=index+1
                or order not in (1,2) or type(order) is not int
                or value.get('actual_frame_all_three_jets_sha256')!=_words_sha(frame,(3,3,6))
                or value.get('provenance_identity_sha256')!=canonical(payload)
                or not isinstance(value.get('jet_sources'),list) or len(value['jet_sources'])!=order+1):
            raise ValueError('Actual stored frame provenance, identity, or complete words differ')
        for j,origin in enumerate(value['jet_sources']):
            context=origin.get('context',{})
            if (origin.get('component_angular_order')!=j
                    or origin.get('actual_frame_component_sha256')!=_words_sha(frame[j],(3,6))
                    or not _digest(origin.get('actual_previous_all_three_jets_sha256'))
                    or not _digest(origin.get('required_previous_prefix_sha256'))
                    or context.get('schema')!=CONTEXT_SCHEMA
                    or context.get('model_identity_sha256')!=self.model_identity
                    or context.get('operator_source_sha256')!=self.operator_source
                    or context.get('current_full_point_sha256')!=self.q._current_point_sha256
                    or context.get('literal_angle_hex')!=key
                    or context.get('source_requested_angular_order') not in (1,2)
                    or context['source_requested_angular_order']<j
                    or not isinstance(context.get('required_data_prefix_sha256'),list)
                    or len(context['required_data_prefix_sha256'])!=context['source_requested_angular_order']+1
                    or any(not _digest(v) for v in context['required_data_prefix_sha256'])):
                raise ValueError('A frame component lost its actual lower-jet/data origin')

    def _root_protection(self,selected,keys,order):
        records=[]
        for angle,(item,key) in enumerate(zip(selected,keys)):
            if (set(item)!=set(('Z','zero','stages','order','record'))
                    or type(item['order']) is not int or item['order'] not in (1,2)
                    or item['order']<order or len(item['stages'])!=self.q.normal_stage_count):
                raise ValueError('Retain every actual root and its possibly higher angular order')
            stages=[]
            previous=np.zeros((3,6),dtype=np.float64)
            for index,stage in enumerate(item['stages']):
                required={'eta','frame','controls','J','record','frame_provenance','jacobian','jacobian_order'}
                if set(stage)!=required:
                    raise ValueError('The complete original stage plus explicit provenance is required')
                values={name:_words_sha(stage[name],shape) for name,shape in (
                    ('eta',(3,3)),('frame',(3,3,6)),('controls',(3,6)),('J',(3,3)))}
                prov=stage['frame_provenance']
                self._check_record_integrity(prov,stage['frame'],key,index)
                if (prov['actual_root_angular_order']!=item['order']
                        or prov['current_previous_all_three_jets_sha256']!=_words_sha(previous,(3,6))):
                    raise ValueError('Each next frame must retain the entire preceding selected control input')
                for j,origin in enumerate(prov['jet_sources']):
                    if origin['required_previous_prefix_sha256']!=_words_sha(previous[:j+1],(j+1,6)):
                        raise ValueError('A component input is not the corresponding complete selected lower jets')
                stages.append(dict(values=values,record=stage['record'],frame_provenance=prov))
                previous=stage['controls']
            if _words_sha(item['Z'],(3,6))!=_words_sha(previous,(3,6)):
                raise ValueError('The final selected control must remain the actual final stage words')
            records.append(dict(literal_angle_hex=key,actual_root_order=item['order'],
                Z=_words_sha(item['Z'],(3,6)),zero=_words_sha(item['zero'],(3,3)),
                record=item['record'],stages=stages))
        # jacobian/jacobian_order alone are intentionally excluded: this producer writes them.
        return canonical(records)

    def _eligible(self,selected,context,order):
        mismatches=[]
        for angle,item in enumerate(selected):
            current=context['angle_contexts'][angle]
            for index,stage in enumerate(item['stages']):
                for j in range(order+1):
                    prior=stage['frame_provenance']['jet_sources'][j]['context']
                    if (prior['complete_integral_carriers_sha256']!=current['complete_integral_carriers_sha256']
                            or prior['required_data_prefix_sha256'][j]!=current['required_data_prefix_sha256'][j]):
                        mismatches.append(dict(local_angle_index=angle,normal_stage_index=index+1,
                            component_angular_order=j,old_data_angular_order=prior['actual_data_angular_order'],
                            current_data_angular_order=current['actual_data_angular_order']))
        return mismatches

    @staticmethod
    def _assemble(A,B,order):
        count=len(A);size=3*(order+1)
        A=_array(A,(count,order+1,3,6));B=_array(B,(count,order+1,3,6))
        # Use detached CPU double tensors and declare this independent product order.
        a=torch.as_tensor(np.array(A,copy=True),dtype=torch.float64)
        b=torch.as_tensor(np.array(B,copy=True),dtype=torch.float64)
        product=lambda i,j:a[:,i]@b[:,j].transpose(-1,-2)
        m0=product(0,0)
        m1=product(1,0)+product(0,1)
        result=torch.zeros((count,size,size),dtype=torch.float64)
        result[:,:3,:3]=m0;result[:,3:6,:3]=m1;result[:,3:6,3:6]=m0
        if order==2:
            m2=product(2,0)+2*product(1,1)+product(0,2)
            result[:,6:9,:3]=m2;result[:,6:9,3:6]=2*m1;result[:,6:9,6:9]=m0
        if not bool(torch.isfinite(result).all()):
            raise RuntimeError('Nonfinite adjacent total-frame complete block products')
        return result.detach()

    def _original_all(self,data,keys,selected,order,record):
        count=len(keys);q=self.q
        zero=self.tensor(np.stack([item['zero'] for item in selected]))
        previous=torch.zeros((count,3,6),dtype=torch.float64)
        answer=[]
        self.counts['complete_AD_fallback_calls']+=1
        with q.stage_matrices.scope(data,keys,order,'complete_angular_J6_J9') as scope:
            for index in range(q.normal_stage_count):
                stages=[item['stages'][index] for item in selected]
                frame=self.tensor(np.stack([item['frame'] for item in stages]))
                eta=self.tensor(np.stack([item['eta'] for item in stages]))
                value=scope.angular(eta,previous,frame,zero,q.normal_step_carriers[index+1],index,order)
                answer.append(value)
                previous=self.tensor(np.stack([item['controls'] for item in stages]))
        record['fallback_actual_matrix_scope']=_copy(q.stage_matrices.last_scope)
        return answer

    def populate(self,data,keys,selected,order):
        """Replace only complete angular matrices after validating selected roots."""
        binding=self._binding(data,keys,order)
        if len(selected)!=len(keys):
            raise ValueError('Keep all selected actual angles in their original order')
        protected=self._root_protection(selected,keys,order)
        count=len(keys);q=self.q;size=3*(order+1);start=time.monotonic()
        self.counts['matrix_calls_started']+=1
        self.counts['requested_stage_angle_blocks']+=count*q.normal_stage_count
        record=dict(schema='actual-adjacent-normal-matrix-call-v1',**binding,
            requested_angular_order=order,actual_root_orders=[item['order'] for item in selected],
            angle_count=count,normal_stage_count=q.normal_stage_count,
            exact_normal_step_nodes=list(self.partition),
            original_selected_root_fields_sha256=protected,
            protected_root_fields_unchanged=False,completed=False,
            published_origin=None,stage_records=[],failure=None,
            field_or_root_success_inferred=False)
        self.last_call=record
        completed=False
        try:
            context=self.frame_context(data,keys,order)
            mismatch=self._eligible(selected,context,order)
            record['required_data_word_mismatch_count']=len(mismatch)
            record['required_data_word_mismatches']=mismatch
            if mismatch:
                self.counts['required_data_mismatch_calls']+=1
                matrices=self._original_all(data,keys,selected,order,record)
                origin='complete_original_AD'
            else:
                try:
                    final=self.tensor(np.stack([item['stages'][-1]['controls'] for item in selected]))
                    self.counts['final_frame_angle_attempts']+=count
                    before=q.normal_counts['frame_reverse_angle_products']
                    try:
                        with torch.no_grad():
                            last=self.methods['_normal_frame_jets'](q,final,data,order)
                    finally:
                        self.counts['actual_final_frame_reverse_angle_products']+=(
                            q.normal_counts['frame_reverse_angle_products']-before)
                    _array(last,(count,order+1,3,6))
                    self.counts['final_frame_angle_returns']+=count
                    record['last_frame_complete_selected_controls_sha256']=_raw_words_sha(final)
                    record['last_frame_words_sha256']=_raw_words_sha(last)
                    matrices=[]
                    for index in range(q.normal_stage_count):
                        B=np.stack([item['stages'][index]['frame'][:order+1] for item in selected])
                        A=(last if index==q.normal_stage_count-1 else
                            np.stack([item['stages'][index+1]['frame'][:order+1] for item in selected]))
                        matrices.append(self._assemble(A,B,order))
                        self.counts['adjacent_stage_angle_blocks_assembled']+=count
                    origin='adjacent_total_frames'
                except (MemoryError,RuntimeError) as error:
                    self.counts['optional_assembly_failure_calls']+=1
                    record['optional_assembly_failure']=dict(type=type(error).__name__,message=str(error),
                        partial_products_not_published=True)
                    matrices=self._original_all(data,keys,selected,order,record)
                    origin='complete_original_AD'
            if (binding!=self._binding(data,keys,order)
                    or protected!=self._root_protection(selected,keys,order)):
                raise ValueError('Matrix production changed selected root, frame, control, J3, zero, or point words')
            # Prepare ALL immutable replacement arrays before changing any root field.
            replacements=[]
            for index,matrix in enumerate(matrices):
                value=_array(matrix,(count,size,size))
                arrays=[np.array(value[j],dtype=np.float64,copy=True) for j in range(count)]
                for array in arrays:array.setflags(write=False)
                replacements.append(arrays)
                record['stage_records'].append(dict(normal_stage_index=index+1,
                    exact_auxiliary_node=self.partition[index+1],actual_auxiliary_node_hex=self.carriers[index+1],
                    matrix_shape=[count,size,size],matrix_words_sha256=_raw_words_sha(matrix),origin=origin,
                    current_frame_origin=('fresh_final_complete_frame' if index==q.normal_stage_count-1
                        else 'next_actual_stage_frame') if origin=='adjacent_total_frames' else 'complete_original_AD',
                    current_selected_controls_sha256=canonical([
                        _words_sha(item['stages'][index]['controls'],(3,6)) for item in selected])))
            if len(replacements)!=q.normal_stage_count:
                raise AssertionError('A complete matrix producer must retain every original normal stage')
            for index,arrays in enumerate(replacements):
                for j,item in enumerate(selected):
                    item['stages'][index]['jacobian']=arrays[j]
                    item['stages'][index]['jacobian_order']=order
            record['protected_root_fields_unchanged']=(protected==self._root_protection(selected,keys,order))
            if not record['protected_root_fields_unchanged']:
                raise AssertionError('Only the explicit angular-matrix output fields may change')
            blocks=count*q.normal_stage_count
            published=('adjacent_stage_angle_blocks_published' if origin=='adjacent_total_frames'
                       else 'original_AD_stage_angle_blocks_published')
            self.counts[published]+=blocks
            self.counts['published_six_by_six_angle_blocks' if order==1
                        else 'published_nine_by_nine_angle_blocks']+=blocks
            record.update(completed=True,published_origin=origin,
                jacobian_fields_deliberately_replaced=True,original_root_values_recomputed=False)
            completed=True
        except BaseException as error:
            record['failure']=dict(type=type(error).__name__,message=str(error))
            raise
        finally:
            self.counts['matrix_calls_completed' if completed else 'matrix_calls_failed']+=1
            self.matrix_call_seconds+=time.monotonic()-start

    def metadata(self):
        value=dict(schema=SCHEMA,source_sha256=sha(__file__),definition=_copy(self.definition),
            definition_identity_sha256=canonical(self.definition),
            actual_model_identity_sha256=self.model_identity,
            actual_operator_source_sha256=self.operator_source,
            actual_counts=dict(self.counts),matrix_call_seconds=self.matrix_call_seconds,
            last_call=_copy(self.last_call),selected_Newton_and_J3_unchanged_by_angular_assembly=True,
            original_active_implicit_chain_unchanged=True,
            root_success_inferred_from_matrix_production=False,measured_acceleration_claimed=False,
            matrix_arithmetic_errors_enclosed=False,matrix_or_data_arrays_retained_in_kernel=False)
        return validate_metadata(value,model_identity=self.model_identity,
            operator_source_sha256=self.operator_source,expected_definition=self.definition)
