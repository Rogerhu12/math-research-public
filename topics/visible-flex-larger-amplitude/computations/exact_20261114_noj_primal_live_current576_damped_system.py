#!/usr/bin/env python3
"""Bind a fresh noJ-primal native576 with-J snapshot in a persistent client.

The snapshot belongs to one actual correction point in the unchanged
native iteration.  There is no actual28 cache, no1372 map and no assumed
zero cut residual. Each positive protocol call binds its actual full H,
target, original scales and current states. Only the first bootstrap uses
the literal JSON-decoded completed73 checkpoint as an initial guess; no
unseen pre-JSON signed zero or live predictor is reconstructed. The
constructor verifies saved source/metadata/raw
identities, shapes and finite words; it never evaluates RHS/J/ODE or QR.
The identified new flow follows the original no-J primal path and uses
captured original local fields for its variational propagation. The
original evaluate body is retained; the with-J flow is not labelled as
the unchanged old implementation.
Scientific consumers are restricted to this public repository Actions.
"""
from __future__ import annotations

import hashlib
import importlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import struct

import numpy as np


HERE=Path(__file__).resolve().parent
BYTE_IO='geometry_20261114_native_captured_band_correction.py'
BYTE_IO_SHA='b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390'
SNAPSHOT_LAUNCHER='geometry_20261114_noj_primal_live_tail_client.py'
SNAPSHOT_HOOK='geometry_20261114_noj_primal_live_tail_client_hook.mjs'
PRIMAL_FLOW='geometry_20261114_noj_matched_variational_engine.mjs'
PRIMAL_FLOW_SHA='f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9'
ORIGINAL_FLOW_DEPENDENCIES={
    'product_jacobian':'205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25',
    'local_cusp_grid':'b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f'}
CORE_SHA='ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3'
MATRIX_SCOPE='noj-primal-live-fresh-current-native576-finite-binary64-complete-J-r-sigma-chain'
ANCHOR_PRODUCER_SHA='938fbec22f0733fff6ceb22e6e9b7a9e12942c12d1eae31c608d8f517702df8c'
ANCHOR_HOOK_SHA='099798e9c57f09b82f7532ea184d124446aeeb2cdbafe452390cb794b8db405d'
ORIGINAL_RAW_NODE=[0,72,144,216,288,360,432,504,576]
INPUT_NAMES=('base-states','stage-residuals','stage-out','original-scales',
             'cut-residual','end-residual','original-far-graph','physical-height','cut-target')
EXPECTED_SHAPES={
    'base-states':[577,224],'stage-residuals':[576,224],'stage-out':[576,224],
    'original-scales':[1,577],'cut-residual':[1,112],'end-residual':[1,112],
    'original-far-graph':[1,112],'physical-height':[1,112],'cut-target':[1,112],
    'stage-jacobians':[576,224,224]}


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS')!='true' or
            os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'):
        raise RuntimeError('Current native576 work belongs only to this public repository Actions')


def file_sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for raw in iter(lambda:f.read(1<<20),b''):h.update(raw)
    return h.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
                                    allow_nan=False).encode()).hexdigest()


def load_binding():
    path=HERE/BYTE_IO
    if file_sha(path)!=BYTE_IO_SHA:raise ValueError('Frozen byte/output helper changed')
    module=importlib.import_module(path.stem)
    if Path(module.__file__).resolve()!=path:raise ValueError('Unexpected helper import path')
    return module


def valid_sha(value,label):
    if not isinstance(value,str) or re.fullmatch(r'[0-9a-f]{64}',value) is None:
        raise ValueError('An explicit complete SHA256 is required: '+label)
    return value


def receipt_identity(descriptor,label):
    """A complete declared parent receipt, not a claim of per-call reload."""
    if not isinstance(descriptor,dict):raise ValueError('Complete receipt required: '+label)
    name=descriptor.get('file')
    if not isinstance(name,str) or not name or '\\' in name or '\x00' in name:
        raise ValueError('An ordinary relative receipt path is required: '+label)
    path=PurePosixPath(name)
    if path.is_absolute() or '..' in path.parts or not path.parts:
        raise ValueError('A parent receipt may not escape its source directory: '+label)
    if type(descriptor.get('bytes')) is not int or descriptor['bytes']<=0:
        raise ValueError('An actual positive receipt byte count is required: '+label)
    valid_sha(descriptor.get('sha256'),label)


def anchor_identity(B,parent):
    for key,value in dict(schema='completed-native73-noj-primal-literal-JSON-anchor-v1',
            producer_source_sha256=ANCHOR_PRODUCER_SHA,producer_hook_sha256=ANCHOR_HOOK_SHA,
            primal_flow_source_sha256=PRIMAL_FLOW_SHA,
            original_primal_dependencies=ORIGINAL_FLOW_DEPENDENCIES,
            native_accepted=True,full_J_returned=True,full_audit_returned=True,
            source_state_encoding='original-response-JSON-decoded-binary64-v1',
            pre_JSON_negative_zero_preservation_claimed=False,rawNode=ORIGINAL_RAW_NODE).items():
        B.same(parent[key],value,'actual completed73 literal anchor '+key)
    for key in ('producer_result','original_response','parent_primal_flow_installation',
                'literal_seed_checkpoint','literal_seed_raw'):
        receipt_identity(parent[key],'actual completed73 '+key)
    valid_sha(parent['literal_seed_state_float64le_sha256'],'literal completed JSON state')
    valid_sha(parent['height_float64le_sha256'],'literal completed request height')
    B.same(parent['literal_seed_raw']['sha256'],parent['literal_seed_state_float64le_sha256'],
           'declared literal seed raw identity')
    B.same(parent['literal_seed_raw']['bytes'],577*224*8,'complete literal seed raw shape')


def primal_flow_identity(B,implementation):
    for key,value in dict(schema='original-noJ-matched-primal-captured-variational-v1',
            source_file=PRIMAL_FLOW,only_flowStateWithJacobian_replaced=True,
            original_root_rhs_rk4_unchanged=True,complete_state_dimension=226,
            shape_dimension=224,captured_root_feed_only=True).items():
        B.same(implementation[key],value,'new variational implementation '+key)
    B.same(implementation['source_sha256'],PRIMAL_FLOW_SHA,'frozen new variational source identity')
    B.same(implementation['source_sha256'],file_sha(HERE/PRIMAL_FLOW),
           'actual independent no-J-primal variational source')
    for key,value in ORIGINAL_FLOW_DEPENDENCIES.items():
        B.same(implementation['original_dependencies'][key],value,
               'original variational dependency '+key)
    receipt_identity(implementation['installation_receipt'],'actual new-flow installation')


def request_height_bytes(B,current,call):
    """Recover request JSON words with its actual negative-zero sidecar."""
    B.same(current['schema'],'noj-primal-live-current576-native-request-context-v1','actual live request schema')
    B.same(current['native_call'],call,'actual live protocol call')
    B.same(current['primal_flow_source_sha256'],PRIMAL_FLOW_SHA,
           'this actual request retains the installed identified variational flow')
    for name,value in (('bootstrap_request',call==1),('seed_assigned',call==1)):
        if type(current[name]) is not bool:raise ValueError('Actual request boolean required: '+name)
        B.same(current[name],value,'first seed only: '+name)
    B.same(current['original_worker_predictor_and_fallback_unmodified'],call>1,
           'later actual calls retain the original live predictor and fallback')
    B.same(current['original_request_flags_retained'],True,'original request flags retained')
    B.same(current['original_final_sensitivity_not_redirected'],True,'original final sensitivity retained')
    request=current['request']
    B.same(set(request),{'height','jacobian','audit'},'all original request members')
    for name in ('jacobian','audit'):
        if type(request[name]) is not bool:raise ValueError('Original request flag must be a boolean: '+name)
    height=request['height']
    if not isinstance(height,list) or len(height)!=112 or any(type(x) not in (int,float) for x in height):
        raise ValueError('Every actual current height mode is required')
    raw=bytearray(struct.pack('<112d',*height))
    negative=current['height_negative_zero_columns']
    if not isinstance(negative,list) or any(type(j) is not int or not 0<=j<112 for j in negative):
        raise ValueError('Actual request signed-zero column sidecar required')
    B.same(negative,sorted(set(negative)),'complete ordered request negative-zero columns')
    for j in negative:
        word=int.from_bytes(raw[8*j:8*(j+1)],'little')
        if word&((1<<63)-1):raise ValueError('A negative-zero annotation must identify a zero height mode')
        raw[8*j:8*(j+1)]=(1<<63).to_bytes(8,'little')
    words=[x[0] for x in struct.iter_unpack('<Q',raw)]
    if any(((w>>52)&2047)==2047 for w in words):raise ValueError('The actual request height must be finite')
    B.same([j for j,w in enumerate(words) if w==(1<<63)],negative,'all actual request negative zero words')
    B.same(hashlib.sha256(raw).hexdigest(),valid_sha(current['request_height_float64le_sha256'],
           'actual current request height'),'all actual request height bits')
    return bytes(raw)


def number_record(B,record,label,require_finite=False):
    """Check the saved IEEE record without adding a guard bound.

    Original with-J minA/minD records are metadata here.  In particular
    their actual infinity/NaN words are not converted into a new QR gate.
    The completed original residual norm and all mathematical arrays have
    their separate finite-input contract.
    """
    encoded=record['float64le_hex']
    if not isinstance(encoded,str) or re.fullmatch(r'[0-9a-f]{16}',encoded) is None:
        raise ValueError('One complete original binary64 number record required: '+label)
    word=int.from_bytes(bytes.fromhex(encoded),'little')
    exponent=(word>>52)&0x7ff;fraction=word&((1<<52)-1)
    if exponent==0x7ff:
        expected='NaN' if fraction else ('negative-infinity' if word>>63 else 'positive-infinity')
        B.same(record['classification'],expected,label+' saved IEEE classification')
        B.same(record['value'],None,label+' nonfinite JSON value')
        if require_finite:raise ValueError('A finite original residual norm is required: '+label)
    else:
        expected='negative-zero' if word==(1<<63) else 'finite'
        B.same(record['classification'],expected,label+' saved IEEE classification')
        value=record['value']
        if type(value) not in (int,float):raise ValueError('Original finite number value required: '+label)
        if expected=='negative-zero':B.same(value,0,label+' signed-zero JSON magnitude')
        else:B.same(struct.pack('<d',float(value)).hex(),encoded,label+' original finite number bits')


class NoJPrimalLiveCurrent576System:
    """The exact saved finite arrays at one actual fresh correction point."""

    def __init__(self,snapshot_directory,expected_result_sha256,B=None):
        require_actions()
        self.B=load_binding() if B is None else B;B=self.B
        B.same(file_sha(B.__file__),BYTE_IO_SHA,'frozen byte/output helper identity')
        self.directory=Path(snapshot_directory).resolve()
        result_path=B.safe_file(self.directory,'result.json')
        B.same(file_sha(result_path),valid_sha(expected_result_sha256,'current snapshot result'),
               'actual complete current snapshot result bytes')
        self.result=B.read(result_path);r=self.result
        for key,value in dict(schema='noj-primal-live-current-native576-withJ-snapshot-result-v1',
                snapshot_completed=True,M=112,K=224,depth=576).items():
            B.same(r[key],value,'current snapshot '+key)
        self.M,self.K,self.depth=112,224,576
        self.original_depth=self.depth;self.old_to_new=list(range(self.depth+1))
        self.native_call=r['native_call']
        if type(self.native_call) is not int or self.native_call<=0:
            raise ValueError('A positive actual original protocol call is required')
        self.iteration=r['nonlinear_iteration'];self.sequence=r['snapshot_sequence']
        for name,value in (('nonlinear_iteration',self.iteration),('snapshot_sequence',self.sequence)):
            if type(value) is not int or value<0:raise ValueError('Nonnegative actual current '+name)
        B.same(self.iteration,self.sequence,'original per-call iteration and snapshot sequence')
        # The launching workflow pins all sources.  In this two-sided bridge
        # the snapshot producer pins this module; here the reciprocal check
        # is against the actual fixed-basename files, avoiding circular SHA
        # constants while still retaining both exact source identities.
        self.producer_sources={}
        for key,name in (('source_sha256',SNAPSHOT_LAUNCHER),('hook_sha256',SNAPSHOT_HOOK)):
            path=HERE/name;actual=file_sha(path)
            B.same(r[key],actual,'actual current snapshot producer '+name)
            self.producer_sources[name]=dict(file=name,bytes=path.stat().st_size,sha256=actual)
        self.snapshot_result=dict(file='result.json',bytes=result_path.stat().st_size,
                                  sha256=expected_result_sha256)
        self.context=self._json(r['context'],'current snapshot context')
        self.manifest=self._json(r['manifest'],'current snapshot arrays')
        c=self.context;m=self.manifest
        for key,value in dict(schema='noj-primal-live-current-native576-withJ-snapshot-context-v1',
                source_sha256=r['source_sha256'],hook_sha256=r['hook_sha256'],
                native_call=self.native_call,nonlinear_iteration=self.iteration,snapshot_sequence=self.sequence,
                fresh_current_evaluate_completed=True,no_cached_baseline=True,
                snapshot_does_not_call_RHS_J_ODE=True,
                original_evaluate_and_flow_source_not_instrumented=False,
                original_evaluate_source_not_instrumented=True,
                same_original_noJ_primal_contract=True).items():
            B.same(c[key],value,'fresh current context '+key)
        B.same(m['schema'],'noj-primal-live-current-native576-withJ-snapshot-arrays-v1','current array manifest schema')
        for key in ('source_sha256','hook_sha256','native_call','nonlinear_iteration','snapshot_sequence','M','K','depth'):
            B.same(m[key],r[key],'this actual call array manifest '+key)
        self.parent=c['parent_anchor']
        anchor_identity(B,self.parent)
        self.primal_flow=c['primal_flow_implementation']
        primal_flow_identity(B,self.primal_flow)
        self.flow_installation=self._json(self.primal_flow['installation_receipt'],
                                         'actual independent live variational installation')
        for key,value in dict(schema='noj-primal-live-current576-live-flow-installation-v1',
                source_sha256=r['source_sha256'],hook_sha256=r['hook_sha256'],
                stage_count=576,original_noJ_functions_not_wrapped=True,
                Function_toString_not_modified=True,new_flow_does_not_reuse_saved_J=True,
                installation_does_not_execute_root_RHS_ODE=True,
                original_ready_manifest_is_only_original_constructor_provenance=True,
                no_fresh_withJ_has_been_run_by_installation=True).items():
            B.same(self.flow_installation[key],value,'actual live flow installation '+key)
        B.same(self.flow_installation['implementation'],
               {key:value for key,value in self.primal_flow.items() if key!='installation_receipt'},
               'this snapshot binds the same complete installed variational implementation')
        self.producer_sources[PRIMAL_FLOW]=dict(file=PRIMAL_FLOW,
            bytes=(HERE/PRIMAL_FLOW).stat().st_size,sha256=file_sha(HERE/PRIMAL_FLOW))
        self.current_request=c['current_request']
        request_descriptor=self.current_request['request_file']
        receipt_identity(request_descriptor,'actual local protocol request')
        B.same(request_descriptor['file'],'request.json','local complete request filename')
        request=self._json(request_descriptor,'complete actual current protocol request')
        B.same(request,{key:value for key,value in self.current_request.items() if key!='request_file'},
               'actual call request copied into the snapshot unchanged')
        self.request_height_raw=request_height_bytes(B,self.current_request,self.native_call)
        self.request_height_sha256=self.current_request['request_height_float64le_sha256']
        if self.native_call==1:
            B.same(self.request_height_sha256,self.parent['height_float64le_sha256'],
                   'first bootstrap uses its actual completed anchor height')
        for name in ('original_sources','numerical_configuration','parameters'):
            if not isinstance(c[name],dict) or not c[name]:raise ValueError('Complete current '+name+' required')
        for key in ('graphs_sha256','gains_sha256','far_graph_sha256'):
            valid_sha(c[key],key)
        # rawNode is the nine physical-cell boundary indices in the full
        #577-node shooting array.  It is not the full list of577 states.
        # Retain the exact original physical map rather than generating
        # a different map from the state count.
        if not isinstance(c['rawNode'],list) or any(type(n) is not int for n in c['rawNode']):
            raise ValueError('The original raw-node map must retain integer indices')
        B.same(c['rawNode'],ORIGINAL_RAW_NODE,'unchanged original physical-cell rawNode map')
        if not isinstance(c['cells'],list) or len(c['cells'])!=576:
            raise ValueError('Every current native stage must be retained')
        for n,cell in enumerate(c['cells']):
            if not isinstance(cell,dict) or any(key not in cell for key in
                    ('rawCell','rawSegment','portRatio','mu','profiles')):
                raise ValueError('Complete native cell identity missing at '+str(n))
        self.cells=c['cells'];self.live={'stages':self.cells}
        core=self._json(c['core_instrumentation'],'current core instrumentation')
        B.same(core['original_core_file_sha256'],CORE_SHA,'original native core bytes')
        B.same(core['exact_correction_call_roundtrip_verified'],True,'only declared correction call replacement')
        self.current_records={}
        for name in ('norm','minA','minD'):
            a=c['current_original_'+name]
            B.same(a,r['actual_current_original_'+name],'same original current '+name+' record')
            number_record(B,a,'actual original '+name,require_finite=(name=='norm'))
            self.current_records[name]=a
        self.arrays={}
        for entry in m['arrays']:
            name=entry['name']
            if name in self.arrays:raise ValueError('Duplicate current snapshot array '+name)
            B.same(entry['dtype'],'<f8','current raw dtype')
            B.same(entry['order'],'C','current raw order')
            B.same(entry['completed'],True,'complete current raw array')
            self.arrays[name]=entry
        B.same(set(self.arrays),set(EXPECTED_SHAPES),'all ten and only declared current native arrays')
        for name,shape in EXPECTED_SHAPES.items():B.same(self.arrays[name]['shape'],shape,'full current '+name)
        B.same({name:entry['raw_sha256'] for name,entry in self.arrays.items()},c['raw_array_sha256'],
               'context binds every complete current array')
        self._raw_cache={};self.J_rows=[];self.verified_bytes=0;self.verified_chunks=0
        self.used_files=set()
        for name in self.arrays:self._verify_array(name)
        B.same(len(self.J_rows),576,'all current native J blocks')
        B.same(self.arrays['physical-height']['raw_sha256'],self.request_height_sha256,
               'all height modes belong to this actual protocol request')
        B.same(self.raw('physical-height'),self.request_height_raw,
               'actual request JSON plus signed-zero sidecar equals the complete original height array')
        B.same(self.arrays['original-far-graph']['raw_sha256'],c['far_graph_sha256'],'complete original far bits')
        self.current_state_sha256=self.arrays['base-states']['raw_sha256']
        if self.native_call==1 and self.iteration==0:
            B.same(self.current_state_sha256,self.parent['literal_seed_state_float64le_sha256'],
                   'first bootstrap withJ uses exactly the decoded completed-response literal seed')
        # Later calls use the original live predictor/fallback and their own
        # request H/target/sigma. There is no anchor-height equality outside
        # bootstrap, no state reset, and no Q0==target or zero-cut/far condition.
        scales=self.all('original-scales')
        if not np.all(scales>0):raise ValueError('Original residual scales must remain strictly positive')
        target_hashes={name:self.arrays[name]['raw_sha256'] for name in INPUT_NAMES}
        definition=dict(schema='noj-primal-live-current-native576-finite-matrix-definition-v1',matrix_scope=MATRIX_SCOPE,
            M=112,K=224,depth=576,variable_order='current577 node-major (allQ112, allPi112)',
            native_call=self.native_call,nonlinear_iteration=self.iteration,snapshot_sequence=self.sequence,
            current_request=self.current_request,
            row_order='cut112, all576 stage224 rows, far112',
            full_current_J_raw_sha256=self.arrays['stage-jacobians']['raw_sha256'],
            block_manifest=[{key:row[key] for key in ('stage','bytes','raw_sha256')} for row in self.J_rows],
            current_input_raw_sha256=target_hashes,original_sources=c['original_sources'],
            primal_flow_implementation=self.primal_flow,
            numerical_configuration=c['numerical_configuration'],parameters=c['parameters'],
            rawNode=c['rawNode'],cells=self.cells,graphs_sha256=c['graphs_sha256'],gains_sha256=c['gains_sha256'],
            cut_formula='delta[0,Q]+this_fresh_current_cut_residual',
            stage_formula='this_current_J[n]*delta[n+1]-delta[n]+this_current_r[n]',
            far_formula='delta[576,Pi]-original_diagonal_G*delta[576,Q]+this_current_far_residual',
            row_sigma_rule='cut:sigma0; stage n:sigma_n; far:sigma576')
        self.binding=dict(schema='noj-primal-live-current-native576-complete-linear-system-binding-v1',
            matrix_scope=MATRIX_SCOPE,adapter_source_sha256=file_sha(__file__),
            frozen_byte_io_source_sha256=BYTE_IO_SHA,source_producer_files=self.producer_sources,
            snapshot_result=self.snapshot_result,snapshot_result_sha256=expected_result_sha256,
            snapshot_context=r['context'],snapshot_context_sha256=r['context']['sha256'],
            snapshot_manifest=r['manifest'],snapshot_manifest_sha256=r['manifest']['sha256'],
            core_instrumentation=c['core_instrumentation'],native_call=self.native_call,
            nonlinear_iteration=self.iteration,snapshot_sequence=self.sequence,
            modes=112,shape_dimension=224,depth=576,original_depth=576,node_count=577,
            old_to_new=self.old_to_new,current_state_sha256=self.current_state_sha256,
            parent_anchor=self.parent,current_request=self.current_request,
            primal_flow_implementation=self.primal_flow,
            new_variational_implementation_source_sha256=self.primal_flow['source_sha256'],
            parent_receipts_not_reloaded_per_iteration=True,
            request_height_float64le_sha256=self.request_height_sha256,
            original_sources=c['original_sources'],numerical_configuration=c['numerical_configuration'],
            parameters=c['parameters'],rawNode=c['rawNode'],cells=self.cells,
            graphs_sha256=c['graphs_sha256'],gains_sha256=c['gains_sha256'],far_graph_sha256=c['far_graph_sha256'],
            actual_current_original_records=self.current_records,
            raw_array_sha256={name:entry['raw_sha256'] for name,entry in self.arrays.items()},
            complete_block_manifest=self.J_rows,complete_chunks=self.verified_chunks,
            complete_raw_bytes=self.verified_bytes,full_current_J_raw_sha256=self.arrays['stage-jacobians']['raw_sha256'],
            matrix_identity_definition=definition,new_matrix_identity_sha256=canonical_sha(definition),
            fresh_current_evaluate_completed=True,no_cached_baseline=True,
            not_an_actual28_snapshot_or_a1372_target=True,
            complete_current_J_r_base_boundaries_sigma_H_reused_byte_for_byte=True,
            no_zero_cut_or_far_assumption=True,current_cut_far_errors_not_projected_or_zeroed=True,
            each_protocol_request_full_height_and_signed_zero_bound=True,
            later_protocol_requests_not_forced_to_parent_height_or_seed=True,
            original_completed_anchor_is_only_a_literal_JSON_initial_guess=True,
            pre_JSON_anchor_signed_zero_preservation_claimed=False,
            original_evaluate_source_not_instrumented=True,original_noJ_root_rhs_rk4_unchanged=True,
            flowStateWithJacobian_is_a_new_identified_implementation=True,
            original_evaluate_and_flow_source_not_instrumented=False,
            same_original_noJ_primal_contract=True,exact_DF_of_IEEE_map_not_claimed=True,
            new_RHS_calls_in_this_adapter=0,new_J_calls_in_this_adapter=0,new_ODE_steps_in_this_adapter=0,
            no_QR_or_native_solve_in_this_adapter=True,native_accepted=False,task_completed=False)

    def _json(self,descriptor,label):
        path=self.B.safe_file(self.directory,descriptor['file'])
        if path.is_symlink():raise ValueError('A regular current snapshot file is required: '+label)
        self.B.same(path.stat().st_size,descriptor['bytes'],label+' file bytes')
        self.B.same(file_sha(path),descriptor['sha256'],label+' SHA')
        return self.B.read(path)

    def _verify_array(self,name):
        B=self.B;entry=self.arrays[name];shape=entry['shape']
        width=int(np.prod(shape[1:]))*8;position=0;total=0;full=hashlib.sha256();pieces=[]
        for index,desc in enumerate(entry['chunks']):
            B.same(desc['array'],name,'current chunk array')
            B.same(desc['chunk_index'],index,'current chunk index')
            B.same(desc['row_start'],position,'current complete chunk order')
            stop=desc['row_stop']
            if type(stop) is not int or not position<stop<=shape[0]:raise ValueError('Current chunk range')
            B.same(desc['bytes'],(stop-position)*width,'current complete chunk shape bytes')
            if desc['file'] in self.used_files:raise ValueError('Current raw chunks may not alias')
            self.used_files.add(desc['file'])
            path=B.safe_file(self.directory,desc['file'])
            if path.is_symlink():raise ValueError('Current raw chunk must be a regular file')
            raw=path.read_bytes();B.same(len(raw),desc['bytes'],'current raw file bytes')
            B.same(hashlib.sha256(raw).hexdigest(),desc['raw_sha256'],'current raw file SHA')
            if 'sha256' in desc:B.same(desc['sha256'],desc['raw_sha256'],'raw current chunk SHA alias')
            if not np.isfinite(np.frombuffer(raw,dtype='<f8')).all():
                raise ValueError('Current snapshot contains a nonfinite mathematical input: '+name)
            full.update(raw);total+=len(raw);self.verified_chunks+=1
            if name=='stage-jacobians':
                for offset in range(stop-position):
                    n=position+offset;block=raw[offset*width:(offset+1)*width]
                    self.J_rows.append(dict(stage=n,original_stage=n,bytes=len(block),
                        raw_sha256=hashlib.sha256(block).hexdigest(),origin='this-fresh-noJ-primal-live-withJ-evaluate',
                        current_native_stage_location=self.cells[n]))
            else:pieces.append(raw)
            position=stop
        B.same(position,shape[0],'all current array rows')
        B.same(total,int(np.prod(shape))*8,'all current array words')
        B.same(total,entry['total_bytes'],'current total bytes')
        B.same(full.hexdigest(),entry['raw_sha256'],'complete current array SHA')
        self.verified_bytes+=total
        if name!='stage-jacobians':self._raw_cache[name]=b''.join(pieces)

    def raw(self,name):
        if name not in INPUT_NAMES:raise ValueError('Use staged access for the current full J')
        return self._raw_cache[name]

    def all(self,name):
        return np.frombuffer(self.raw(name),dtype='<f8').reshape(self.arrays[name]['shape'])

    def stages(self):
        width=224*224*8;expected=0
        for desc in self.arrays['stage-jacobians']['chunks']:
            raw=self.B.safe_file(self.directory,desc['file']).read_bytes()
            self.B.same(hashlib.sha256(raw).hexdigest(),desc['raw_sha256'],'immutable current J chunk')
            for n in range(desc['row_start'],desc['row_stop']):
                self.B.same(n,expected,'all current J stages ordered')
                offset=(n-desc['row_start'])*width;block=raw[offset:offset+width]
                self.B.same(hashlib.sha256(block).hexdigest(),self.J_rows[n]['raw_sha256'],'immutable current J block')
                yield n,np.frombuffer(block,dtype='<f8').reshape(224,224)
                expected+=1
        self.B.same(expected,576,'complete current stage stream')

    def stage_bytes(self):
        for n,J in self.stages():yield n,self.B.float_bytes(J)

    def stage_raw(self,n):
        if type(n) is not int or not 0<=n<576:raise ValueError('Current stage range')
        width=224*224*8
        for desc in self.arrays['stage-jacobians']['chunks']:
            if desc['row_start']<=n<desc['row_stop']:
                raw=self.B.safe_file(self.directory,desc['file']).read_bytes()
                self.B.same(hashlib.sha256(raw).hexdigest(),desc['raw_sha256'],'current witness J chunk')
                start=(n-desc['row_start'])*width;block=raw[start:start+width]
                self.B.same(hashlib.sha256(block).hexdigest(),self.J_rows[n]['raw_sha256'],'current witness J block')
                return block
        raise ValueError('Current J witness stage missing')

    def export_inputs(self,output):
        result={}
        for name in INPUT_NAMES:
            desc=output.save('current576-system-'+name,self.all(name),
                'This actual request fresh noJ-primal withJ input, all saved bits retained; not cached61 or28')
            self.B.same(desc['sha256'],self.arrays[name]['raw_sha256'],'current input export byte identity')
            result[name]=desc
        return result


class NoJPrimalLiveCurrent576ExactContext:
    """Frozen row kernel with this request and new variational-flow scope."""

    def __init__(self,system,kernel):
        self.system,self.kernel=system,kernel
        system.B.same((system.M,system.K,system.depth),(kernel.M,kernel.K,kernel.DEPTH),
                      'complete current native576 exact dimensions')

    def max_record(self,kind,node,row,value,sigma_word):
        record=self.kernel.max_record(kind,node,row,value,sigma_word)
        record.update(matrix_scope=MATRIX_SCOPE,
            new_matrix_identity_sha256=self.system.binding['new_matrix_identity_sha256'],
            snapshot_result_sha256=self.system.snapshot_result['sha256'],
            native_call=self.system.native_call,
            request_height_float64le_sha256=self.system.request_height_sha256,
            primal_flow_source_sha256=self.system.primal_flow['source_sha256'],
            nonlinear_iteration=self.system.iteration,snapshot_sequence=self.system.sequence)
        if kind=='stage':record['source_stage']=self.system.cells[node]
        return record

    def row_order(self,kind,node,row):return self.kernel.row_order(kind,node,row)

    def worst_witness(self,record,direction_raw,inputs):
        # The frozen helper only selects raw operands using .directory,
        # .arrays and .live. Here those are the current snapshot, never an
        # actual28 CapturedArrays object or another iteration's data.
        result=self.kernel.worst_witness(self.system,record,direction_raw,inputs)
        result.update(matrix_scope=MATRIX_SCOPE,
            new_matrix_identity_sha256=self.system.binding['new_matrix_identity_sha256'],
            snapshot_result_sha256=self.system.snapshot_result['sha256'],
            native_call=self.system.native_call,
            request_height_float64le_sha256=self.system.request_height_sha256,
            primal_flow_source_sha256=self.system.primal_flow['source_sha256'],
            current_state_sha256=self.system.current_state_sha256,
            nonlinear_iteration=self.system.iteration,snapshot_sequence=self.system.sequence,
            complete_direction_float64le_sha256=hashlib.sha256(direction_raw).hexdigest(),
            kind=record['kind'],node=record['node'],row=record['row'])
        return result
