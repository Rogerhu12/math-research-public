#!/usr/bin/env python3
"""Bind every fresh576 snapshot in the independently identified word-first run.

The initial state is actual73 iteration2's complete failed raw base retained
in actual91; it is not a completed anchor. The first correction may be the
new one-word proposal; this adapter's original complete J/r/cut/far/sigma
assembly and all R273 downstream mathematics remain unchanged. All ten
fresh arrays and the independent current producer are bound at each call.
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
SNAPSHOT_LAUNCHER='geometry_20261115_native_word_first_current576_solve.py'
SNAPSHOT_HOOK='geometry_20261115_native_word_first_current576_solve_hook.mjs'
PRIMAL_FLOW='geometry_20261114_noj_matched_variational_engine.mjs'
PRIMAL_FLOW_SHA='f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9'
CORE_SHA='ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3'
MATRIX_SCOPE='fresh-noJ-primal-current-native576-finite-binary64-complete-J-r-sigma-chain'
PARENT_RUN='43657001633'
PARENT_STATE='f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6'
PARENT_HEIGHT='c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f'
ORIGINAL_RAW_NODE=[0,72,144,216,288,360,432,504,576]
PARENT_SOURCE='exact_20261115_native_word_first_parent.py'
PARENT_SOURCE_SHA='8cd7027df2f7039302dbdc1ed15068c6cf48d6645bc236d74e6e5b1e7dd387e8'

ORIGINAL_FLOW_DEPENDENCIES={
    'product_jacobian':'205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25',
    'local_cusp_grid':'b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f'}
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
    if not isinstance(descriptor,dict):raise ValueError('Complete receipt required: '+label)
    name=descriptor.get('file')
    if not isinstance(name,str) or not name or '\\' in name or '\x00' in name:
        raise ValueError('Ordinary relative receipt path required: '+label)
    path=PurePosixPath(name)
    if path.is_absolute() or '..' in path.parts or not path.parts:
        raise ValueError('Receipt path may not escape its source: '+label)
    if type(descriptor.get('bytes')) is not int or descriptor['bytes']<=0:
        raise ValueError('Actual positive receipt byte count required: '+label)
    valid_sha(descriptor.get('sha256'),label)


def failed_parent_identity(B,parent):
    # These are original receipts, not a completed native response. The
    # launching parent binder has already verified and preserved all bytes.
    path=HERE/PARENT_SOURCE
    B.same(file_sha(path),PARENT_SOURCE_SHA,'independent actual91 parent binder source')
    module=importlib.import_module(path.stem)
    B.same(Path(module.__file__).resolve(),path,'pinned parent helper import')
    for key,value in dict(schema='actual73-failed-current-base-via-complete-actual91-v1',
            state_raw_sha256=PARENT_STATE,source_public_run=43657001633,
            source_commit='9515d5aaf7c68f8efd366438d6bd81ce73c3486f',source_native_call=1,
            source_nonlinear_iteration=2,source_snapshot_sequence=2,native_accepted=False,
            initial_guess_only=True,imported_worker_predictor=False,
            original_base_stage_out_not_exported_or_reconstructed=True).items():
        B.same(parent[key],value,'actual failed73 raw initial guess '+key)
    B.same(parent['actual91_pin'],module.PIN91,'complete original91 archive tuple')
    B.same(parent['actual91_source_commit'],module.SOURCE91,'actual91 source commit')
    for key,expected in (('actual91_result',module.RESULT91_SHA),
            ('actual91_binding',module.BIND91_SHA),('original_probe_result',module.PROBE83_SHA),
            ('original_exact_result',module.EXACT83_SHA)):
        receipt_identity(parent[key],key)
        B.same(parent[key]['sha256'],expected,'actual91 preserved original receipt '+key)
    B.same(parent['complete_parent_eight_array_sha256']['base-states'],PARENT_STATE,
           'complete original73 base-state raw hash')
    B.same(parent['complete_parent_eight_array_sha256']['physical-height'],PARENT_HEIGHT,
           'complete original73 H raw hash')
    B.same(parent['original_native_scope']['original_native_accepted'],False,
           'original73 failure not promoted to successful native anchor')


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


class NoJPrimalCurrent576System:
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
        for key,value in dict(schema='word-first-current-native576-withJ-snapshot-result-v1',
                snapshot_completed=True,native_call=1,M=112,K=224,depth=576).items():
            B.same(r[key],value,'current snapshot '+key)
        self.M,self.K,self.depth=112,224,576
        self.original_depth=self.depth;self.old_to_new=list(range(self.depth+1))
        self.native_call=r['native_call']
        self.iteration=r['nonlinear_iteration'];self.sequence=r['snapshot_sequence']
        for name,value in (('nonlinear_iteration',self.iteration),('snapshot_sequence',self.sequence)):
            if type(value) is not int or value<0:raise ValueError('Nonnegative actual current '+name)
        B.same(self.iteration,self.sequence,'this original iteration and snapshot sequence')
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
        for key,value in dict(schema='word-first-current-native576-current-point-context-v1',
                source_sha256=r['source_sha256'],hook_sha256=r['hook_sha256'],
                native_call=self.native_call,nonlinear_iteration=self.iteration,snapshot_sequence=self.sequence,
                fresh_current_evaluate_completed=True,no_cached_baseline=True,
                snapshot_does_not_call_RHS_J_ODE=True,
                original_evaluate_and_flow_source_not_instrumented=False,
                original_evaluate_source_not_instrumented=True,
                same_original_noJ_primal_contract=True).items():
            B.same(c[key],value,'fresh current context '+key)
        B.same(m['schema'],'word-first-current-native576-snapshot-arrays-v1','current array manifest schema')
        for key in ('source_sha256','hook_sha256','native_call','nonlinear_iteration','snapshot_sequence','M','K','depth'):
            B.same(m[key],r[key],'this actual current array manifest '+key)
        self.parent=c['parent_failed73']
        failed_parent_identity(B,self.parent)
        self.primal_flow=c['primal_flow_implementation']
        primal_flow_identity(B,self.primal_flow)
        self.flow_installation=self._json(self.primal_flow['installation_receipt'],
                                         'actual independent variational installation')
        self.producer_sources[PARENT_SOURCE]=dict(file=PARENT_SOURCE,bytes=(HERE/PARENT_SOURCE).stat().st_size,sha256=file_sha(HERE/PARENT_SOURCE))
        self.producer_sources[PRIMAL_FLOW]=dict(file=PRIMAL_FLOW,
            bytes=(HERE/PRIMAL_FLOW).stat().st_size,sha256=file_sha(HERE/PRIMAL_FLOW))
        for name in ('original_sources','numerical_configuration','parameters'):
            if not isinstance(c[name],dict) or not c[name]:raise ValueError('Complete current '+name+' required')
        for key in ('graphs_sha256','gains_sha256','far_graph_sha256'):
            valid_sha(c[key],key)
        # rawNode is the nine physical-cell boundary indices in the full
        #577-node shooting array.  It is not the full list of577 states.
        # Retain the exact original physical-cell map rather than generating
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
        B.same(core['exact_correction_call_roundtrip_verified'],True,'only the declared replacement inside the original core solve source')
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
        B.same(self.arrays['physical-height']['raw_sha256'],PARENT_HEIGHT,'same original full H at every iteration')
        B.same(self.arrays['original-far-graph']['raw_sha256'],c['far_graph_sha256'],'complete original far bits')
        self.current_state_sha256=self.arrays['base-states']['raw_sha256']
        if self.iteration==0:
            B.same(self.current_state_sha256,PARENT_STATE,'first new-flow withJ uses exact failed73 final raw state as initial guess')
        # In later iterations the actual current state replaces that parent
        # state. In all iterations cut/far arrays retain their real errors;
        # there is deliberately no Q0==target or zero-cut/zero-far condition.
        scales=self.all('original-scales')
        if not np.all(scales>0):raise ValueError('Original residual scales must remain strictly positive')
        target_hashes={name:self.arrays[name]['raw_sha256'] for name in INPUT_NAMES}
        definition=dict(schema='word-first-current-native576-finite-matrix-definition-v1',matrix_scope=MATRIX_SCOPE,
            M=112,K=224,depth=576,variable_order='current577 node-major (allQ112, allPi112)',
            native_call=self.native_call,nonlinear_iteration=self.iteration,snapshot_sequence=self.sequence,
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
        self.binding=dict(schema='word-first-current-native576-complete-linear-system-binding-v1',
            matrix_scope=MATRIX_SCOPE,adapter_source_sha256=file_sha(__file__),
            frozen_byte_io_source_sha256=BYTE_IO_SHA,source_producer_files=self.producer_sources,
            snapshot_result=self.snapshot_result,snapshot_result_sha256=expected_result_sha256,
            snapshot_context=r['context'],snapshot_context_sha256=r['context']['sha256'],
            snapshot_manifest=r['manifest'],snapshot_manifest_sha256=r['manifest']['sha256'],
            core_instrumentation=c['core_instrumentation'],native_call=self.native_call,
            nonlinear_iteration=self.iteration,snapshot_sequence=self.sequence,
            modes=112,shape_dimension=224,depth=576,original_depth=576,node_count=577,
            old_to_new=self.old_to_new,current_state_sha256=self.current_state_sha256,
            parent_failed73=self.parent,parent_public_run=PARENT_RUN,
            parent_receipts_not_reloaded_per_iteration=True,
            primal_flow_implementation=self.primal_flow,
            new_variational_implementation_source_sha256=self.primal_flow['source_sha256'],
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
            failed_parent_is_only_a_raw_initial_guess=True,parent_native_success_not_required=True,
            old73_J_residual_and_norm_not_relabelled_as_current=True,
            original_evaluate_source_not_instrumented=True,original_noJ_root_rhs_rk4_unchanged=True,
            flowStateWithJacobian_is_a_new_identified_implementation=True,
            original_evaluate_and_flow_source_not_instrumented=False,
            exact_DF_of_IEEE_map_not_claimed=True,
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
                        raw_sha256=hashlib.sha256(block).hexdigest(),origin='this-fresh-noJ-primal-withJ-evaluate',
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
                'This actual fresh no-J-primal withJ snapshot input, all saved bits retained; not cached73 or28')
            self.B.same(desc['sha256'],self.arrays[name]['raw_sha256'],'current input export byte identity')
            result[name]=desc
        return result


class NoJPrimalCurrent576ExactContext:
    """Frozen original-sized integer kernel with the new flow/current-matrix scope."""

    def __init__(self,system,kernel):
        self.system,self.kernel=system,kernel
        system.B.same((system.M,system.K,system.depth),(kernel.M,kernel.K,kernel.DEPTH),
                      'complete current native576 exact dimensions')

    def max_record(self,kind,node,row,value,sigma_word):
        record=self.kernel.max_record(kind,node,row,value,sigma_word)
        record.update(matrix_scope=MATRIX_SCOPE,
            new_matrix_identity_sha256=self.system.binding['new_matrix_identity_sha256'],
            snapshot_result_sha256=self.system.snapshot_result['sha256'],
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
            current_state_sha256=self.system.current_state_sha256,
            nonlinear_iteration=self.system.iteration,snapshot_sequence=self.system.sequence,
            complete_direction_float64le_sha256=hashlib.sha256(direction_raw).hexdigest(),
            kind=record['kind'],node=record['node'],row=record['row'])
        return result
