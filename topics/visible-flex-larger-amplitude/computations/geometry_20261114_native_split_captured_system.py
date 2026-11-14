#!/usr/bin/env python3
"""Bind actual28 plus an actual four-short-block probe as a new578-stage system.

The574 unchanged old Jacobians are streamed without regeneration. The two
selected old long matrices are replaced by four independently identified short
matrices. This is a new finite linear representation, never the old576-stage A.
No ODE, native solve, nonlinear trial, or new Jacobian is evaluated here.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import struct
import sys

import numpy as np

HERE=Path(__file__).resolve().parent
BAND_NAME='geometry_20261114_native_captured_band_correction.py'
BAND_SHA='b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390'
CAPTURE_SHA='ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7'
PROBE_NAME='geometry_20261114_native_same_schedule_split_probe.py'
PROBE_SHA='911b8d8a872ec5ba2d1ae45cb83011e4d7b2d1302c1693bded34fc0a8f6c09ae'
HOOK_NAME='geometry_20261114_native_same_schedule_split_probe_hook.mjs'
HOOK_SHA='34d1bb4f31514425e123e978ccffbc5e2d36bf314a98f53505353743a01c8898'
WINDOW_NAME='geometry_20261114_native_same_schedule_windows.mjs'
WINDOW_SHA='2973c14460de920ba2cc873ef9bcc137bdd264b70799ba9734122f3c610b946f'
STOP='VISIBLE_NATIVE_SAME_SCHEDULE_SPLIT_PROBE_COMPLETE_V1'
SELECTED=(43,58)


def load_binding():
    source=HERE/BAND_NAME
    if hashlib.sha256(source.read_bytes()).hexdigest()!=BAND_SHA:
        raise ValueError('The complete original capture binder changed')
    name='_native_split_original_capture_binding'
    spec=importlib.util.spec_from_file_location(name,source)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module)
    return module


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


class SplitCapturedSystem:
    """An explicitly new virtual matrix; raw old and new sources stay read-only."""
    def __init__(self,capture_directory,split_directory,split_result_sha256,B=None):
        self.B=B or load_binding();B=self.B;B.actions_only()
        if not re.fullmatch(r'[0-9a-f]{64}',split_result_sha256):
            raise ValueError('Provide the actual completed split-probe result SHA256')
        for name,digest in ((PROBE_NAME,PROBE_SHA),(HOOK_NAME,HOOK_SHA),(WINDOW_NAME,WINDOW_SHA)):
            B.same(B.sha(HERE/name),digest,'frozen scoped producer '+name)
        self.original=B.CapturedArrays(capture_directory,CAPTURE_SHA)
        self.directory=Path(split_directory).resolve();self.split_result_sha256=split_result_sha256
        B.same(B.sha(self.directory/'result.json'),split_result_sha256,'actual split result bytes')
        result=B.read(self.directory/'result.json');self.result=result
        required=dict(schema='original-native-same-schedule-split-probe-result-v1',probe_completed=True,
            native_accepted=False,task_completed=False,source_sha256=PROBE_SHA,hook_sha256=HOOK_SHA,
            window_module_sha256=WINDOW_SHA,capture_result_sha256=CAPTURE_SHA,
            original_native_solve_called=False,new_whole_tail_J_evaluations=0,
            new_whole_stage_withJac_evaluations=0,endpoint_J_or_audit_computed=False,
            original_protocol_requests=1,worker_exit_code=0,planned_probe_stop_observed=True,
            completed_short_J_blocks=4,completed_no_J_windows=4,completed_original_stages=list(SELECTED),
            actual_original_failure_message='Error: '+STOP)
        for key,value in required.items():B.same(result.get(key),value,'completed scoped result '+key)
        if result.get('unexpected_error') or result.get('unexpected_complete_native_response_returned'):
            raise ValueError('Use a completed scoped probe, not a changed native execution')
        self.small={}
        for row in result['small_output_files']:
            name=row['file']
            if Path(name).name!=name or name in self.small:raise ValueError('Unique bounded split file names required')
            path=B.safe_file(self.directory,name)
            B.same(path.stat().st_size,row['bytes'],'split file size '+name)
            B.same(B.sha(path),row['sha256'],'split file bytes '+name)
            self.small[name]=row
        self.split_spec=self.json('split-probe-spec.json')
        summary=self.json('split-probe-summary.json');self.summary=summary
        manifest=self.json('split-probe-array-manifest.json')
        layout=self.json('prospective-split-layout.json');self.layout=layout
        references=self.json('original-reference-packets.json');self.references=references
        B.same(self.small['split-probe-spec.json']['sha256'],result['spec_sha256'],'actual probe specification')
        B.same(self.small['split-probe-summary.json']['sha256'],result['split_probe_summary_sha256'],'actual summary')
        B.same(summary['array_manifest'],{k:self.small['split-probe-array-manifest.json'][k]
            for k in ('file','sha256','bytes')},'actual complete new-array manifest')
        for key,value in dict(probe_completed=True,completed_original_stages=list(SELECTED),
            completed_short_J_blocks=4,completed_no_J_windows=4,original_steps=12,split=6,
            new_whole_stage_withJac_evaluations=0,new_whole_tail_J_evaluations=0,
            original_native_solve_called=False,nonlinear_trials=0,endpoint_J_or_audit_computed=False,
            native_accepted=False,task_completed=False,original_live_functions_graphs_gains_far_and_scales_unchanged=True,
            all_original_seed_bytes_unchanged=True,planned_probe_stop=STOP).items():
            B.same(summary.get(key),value,'scoped summary '+key)
        B.same(summary['source_sha256'],PROBE_SHA,'scoped source')
        B.same(summary['hook_sha256'],HOOK_SHA,'scoped hook')
        B.same(summary['window_module_sha256'],WINDOW_SHA,'scoped window source')
        B.same(summary['spec_sha256'],result['spec_sha256'],'summary/spec')
        for key,name in (('original_candidate_float64le_sha256','base-states'),
            ('original_height_float64le_sha256','physical-height'),
            ('original_scales_float64le_sha256','original-scales'),
            ('original_far_graph_float64le_sha256','original-far-graph')):
            B.same(summary[key],self.original.arrays[name]['raw_sha256'],'actual short-probe original bits '+name)
        B.same(summary['original_capture_result_sha256'],CAPTURE_SHA,'short-probe original capture')
        B.same(self.split_spec['references'],references,'complete selected source references')
        B.same(references['capture_binding'],self.original.binding,'all original capture bytes and source identities')
        B.same(self.split_spec['capture']['array_sha256'],self.original.binding['raw_array_sha256'],
            'all original arrays consumed by the actual short probe')
        B.same(self.split_spec['fresh_request'],self.original.spec['fresh_request'],'same full H and original flags')
        B.same(self.json('original-live-identity-before-seed.json'),self.original.live,'same original live layout')
        self.new_arrays={}
        for row in manifest['arrays']:
            name=row['file']
            if name in self.new_arrays:raise ValueError('A short-probe array was listed twice')
            self.descriptor(row);self.new_arrays[name]=row
        B.same(manifest['spec_sha256'],result['spec_sha256'],'new arrays/spec')
        B.same(manifest['source_sha256'],PROBE_SHA,'new arrays producer')
        B.same(manifest['hook_sha256'],HOOK_SHA,'new arrays hook')
        B.same(manifest['window_module_sha256'],WINDOW_SHA,'new arrays window')
        B.same(manifest.get('partial'),False,'all short arrays complete')
        self.M,self.K,self.depth=112,224,578
        self.original_depth=576
        B.same((self.original.M,self.original.K,self.original.depth),(112,224,576),'parent full dimensions')
        self.old_to_new=[];self.cells=[]
        for n in range(self.original_depth):
            self.old_to_new.append(len(self.cells))
            if n in SELECTED:
                self.cells.extend([dict(newStage=len(self.cells),originalStage=n,window=[6,12],port='original'),
                    dict(newStage=len(self.cells)+1,originalStage=n,window=[0,6],port='one')])
            else:self.cells.append(dict(newStage=len(self.cells),originalStage=n,window=[0,12],port='original'))
        self.old_to_new.append(len(self.cells))
        B.same(len(self.cells),self.depth,'new complete stage count')
        for key,value in dict(schema='original-native-shooting-same-schedule-split-layout-v1',
            originalDepth=576,newDepth=578,selectedOriginalStages=list(SELECTED),oldToNew=self.old_to_new,cells=self.cells,
            not_installed_in_original_dn=True,not_a_solved_augmented_system=True).items():
            B.same(layout.get(key),value,'explicit source layout '+key)
        self.short={};self.stage_reports={}
        old_states=self.original.all('base-states');old_out=self.original.all('stage-out')
        old_r=self.original.all('stage-residuals');old_sigma=self.original.all('original-scales').reshape(-1)
        states=np.empty((579,224),dtype=np.float64);residuals=np.empty((578,224),dtype=np.float64)
        outputs=np.empty_like(residuals);scales=np.empty(579,dtype=np.float64)
        states[np.asarray(self.old_to_new)]=old_states;scales[np.asarray(self.old_to_new)]=old_sigma
        stage_metadata=[]
        for cell in self.cells:
            n=cell['originalStage'];stage_metadata.append(dict(self.original.live['stages'][n],
                originalStage=n,newStage=cell['newStage'],same_schedule_window=cell['window'],
                shape_J_source='actual-short-probe' if n in SELECTED else 'unchanged-actual28'))
        self.live=dict(stages=stage_metadata)
        self.spec=dict(numerical_parameters={'spacing':self.original.spec['numerical_parameters']['spacing']},
            original_full_native_spec_sha256=self.original.binding['capture_spec_sha256'])
        for n in SELECTED:
            report=self.json('stage-'+str(n)+'-completed-report.json');self.stage_reports[n]=report
            if summary['stage_reports'][list(SELECTED).index(n)]!=report:
                raise ValueError('Actual completed stage report differs from summary')
            B.same(report['stage'],n,'selected stage identity')
            B.same(report['all_new_local_blocks_saved'],True,'all short matrices saved')
            B.same(report['no_product_of_short_J_blocks_formed'],True,'independent short blocks')
            reference=references['selected_stages'][str(n)]
            for kind,expected in (('input',old_states[n+1]),('output',old_out[n]),
                ('guard-mean',self.original.all('stage-guard-mean')[n])):
                actual=self.array(reference[kind],list(expected.shape),from_manifest=False)
                B.same(B.float_bytes(actual),B.float_bytes(expected),'selected original reference '+str(n)+'/'+kind)
            B.same(reference['original_live_stage'],self.original.live['stages'][n],'selected original live stage')
            full_input=self.array(report['input'],[226])
            B.same(B.float_bytes(full_input[:224]),B.float_bytes(old_states[n+1]),'same complete original short input')
            B.same(B.float_bytes(full_input[224:]),bytes(16),'two original positive-zero mean initial values')
            inner=self.json_descriptor(report['inner_window']);outer=self.json_descriptor(report['outer_window'])
            for packet,first,last in ((inner,0,6),(outer,6,12)):
                B.same(packet['stage'],n,'short window parent')
                B.same(packet['kind'],'withJac','new J branch')
                B.same((packet['window']['firstStep'],packet['window']['lastStep']),(first,last),'unchanged half steps')
                B.same(packet['original_guards_returned'],True,'actual original guard return')
                B.same(len(packet['window']['schedule']),6,'six original recorded steps')
                B.same(packet['window']['tangent_restarted_at_identity_for_this_short_block'],True,'local derivative origin')
            inner_state=self.array(inner['full_state'],[226]);outer_state=self.array(outer['full_state'],[226])
            B.same(inner['window']['state_float64le_sha256'],hashlib.sha256(B.float_bytes(inner_state)).hexdigest(),
                'complete inner state bits')
            B.same(outer['window']['state_float64le_sha256'],hashlib.sha256(B.float_bytes(outer_state)).hexdigest(),
                'complete outer state bits')
            inner_j=self.array(report['inner_shape_J'],[224,224]);outer_j=self.array(report['outer_shape_J_with_original_port'],[224,224])
            exit_out=self.array(report['withJac_output'],[224])
            B.same(report['original_port_applied_once'],self.original.live['stages'][n]['portRatio'],'same exit port')
            B.same(report['original_sigma']['float64le_hex'],B.float_bytes(old_sigma[n:n+1]).hex(),'same old stage sigma')
            i=self.old_to_new[n];mid=i+1
            states[mid]=inner_state[:224];scales[mid]=old_sigma[n]
            # Preserve the actual new exit, not the old residual if bits differ.
            outputs[i]=exit_out;outputs[i+1]=inner_state[:224]
            residuals[i]=exit_out-old_states[n]
            residuals[i+1]=inner_state[:224]-states[mid]
            self.short[(n,'outer')]=outer_j;self.short[(n,'inner')]=inner_j
            self.short[(n,'reference')]=reference['J']
        for cell in self.cells:
            if cell['originalStage'] not in SELECTED:
                i,n=cell['newStage'],cell['originalStage'];outputs[i]=old_out[n];residuals[i]=old_r[n]
        explicit=self.array(layout['explicitNewScales'],[579])
        B.same(B.float_bytes(explicit),B.float_bytes(scales),'every explicit new-node sigma word')
        B.same(B.float_bytes(states[np.asarray(self.old_to_new)]),B.float_bytes(old_states),'all old nodes preserved')
        B.same(B.float_bytes(scales[np.asarray(self.old_to_new)]),B.float_bytes(old_sigma),'all old-node sigma preserved')
        self._values={'base-states':states,'stage-residuals':residuals,'stage-out':outputs,
            'original-scales':scales.reshape(1,-1)}
        for name in ('cut-residual','end-residual','original-far-graph','physical-height','cut-target'):
            self._values[name]=self.original.all(name)
        for name,values in self._values.items():
            if not np.isfinite(values).all():raise FloatingPointError('Nonfinite new finite-system array '+name)
            values.flags.writeable=False
        if not (scales>0).all():raise ValueError('All explicit split-node sigma values must remain positive')
        self.arrays={name:dict(shape=list(value.shape),dtype='<f8',order='C',total_bytes=value.nbytes,
            raw_sha256=hashlib.sha256(B.float_bytes(value)).hexdigest()) for name,value in self._values.items()}
        self.J_rows=[];full=hashlib.sha256()
        for stage,J in self.stages():
            raw=B.float_bytes(J);full.update(raw)
            if not np.isfinite(J).all():raise FloatingPointError('Nonfinite complete short/old J at new stage '+str(stage))
            cell=self.cells[stage]
            self.J_rows.append(dict(new_stage=stage,original_stage=cell['originalStage'],window=cell['window'],
                origin='new-short-probe' if cell['originalStage'] in SELECTED else 'unchanged-actual28',
                raw_sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw)))
        B.same(len(self.J_rows),578,'complete new block manifest')
        self.arrays['stage-jacobians']=dict(shape=[578,224,224],dtype='<f8',order='C',total_bytes=578*224*224*8,
            raw_sha256=full.hexdigest(),virtual_stream=True)
        self.binding=dict(schema='native-original-schedule-split-system-binding-v1',
            adapter_source_sha256=B.sha(__file__),original_capture_binding=self.original.binding,
            actual_split_result_sha256=split_result_sha256,actual_split_source_sha256=PROBE_SHA,
            actual_split_hook_sha256=HOOK_SHA,window_source_sha256=WINDOW_SHA,
            actual_split_spec_sha256=result['spec_sha256'],actual_split_summary_sha256=result['split_probe_summary_sha256'],
            actual_split_files=self.small,original_depth=576,new_depth=578,original_nodes=577,new_nodes=579,
            modes=112,shape_dimension=224,old_to_new=self.old_to_new,split_stages=list(SELECTED),
            cells=self.cells,complete_block_manifest=self.J_rows,
            raw_array_sha256={name:row['raw_sha256'] for name,row in self.arrays.items()},
            reused_original_stage_J_blocks=574,new_short_stage_J_blocks=4,new_J_computed_here=0,
            original_finite_scalar_profile_and_RK_schedule_unchanged=True,
            old_nodes_and_original_cut_far_H_preserved=True,
            inserted_sigma_rule='The exact original parent-stage sigma; old-node sigma words retained',
            selected_outer_residual_rule='Actual split withJac original-coordinate exit minus the original outgoing node',
            selected_inner_residual_rule='Actual inner output minus its identical newly stored midpoint',
            new_linear_representation_not_original_576_A=True,
            old_long_J_defect_is_diagnostic_not_acceptance_gate=True,
            final_original_full_nonlinear_readback_still_required=True,
            no_native_solve_or_trial=True,native_accepted=False,task_completed=False)
        self.binding['new_matrix_identity_sha256']=canonical_sha(dict(
            original_capture_result_sha256=CAPTURE_SHA,split_result_sha256=split_result_sha256,
            old_to_new=self.old_to_new,cells=self.cells,block_manifest=self.J_rows,
            arrays=self.binding['raw_array_sha256']))

    def json(self,name):
        if name not in self.small:raise ValueError('Missing complete actual split file: '+name)
        return self.B.read(self.B.safe_file(self.directory,name))

    def descriptor(self,row):
        name=row['file']
        if name not in self.small:raise ValueError('An output descriptor is outside the actual split inventory: '+name)
        for key in ('bytes','sha256'):self.B.same(row[key],self.small[name][key],'actual descriptor '+name+'/'+key)
        return self.B.safe_file(self.directory,name)

    def json_descriptor(self,row):return self.B.read(self.descriptor(row))

    def array(self,row,shape,from_manifest=True):
        path=self.descriptor(row)
        self.B.same(row['shape'],shape,'complete array shape '+row['file'])
        self.B.same(row['dtype'],'<f8','complete array dtype')
        self.B.same(row.get('order','C'),'C','complete array order')
        if from_manifest:self.B.same(row,self.new_arrays.get(row['file']),'same actual short-array descriptor')
        raw=path.read_bytes();self.B.same(len(raw),int(np.prod(shape))*8,'actual complete binary size')
        self.B.same(hashlib.sha256(raw).hexdigest(),row['sha256'],'reread actual short-array bytes')
        values=np.frombuffer(raw,dtype='<f8').reshape(shape)
        if not np.isfinite(values).all():raise FloatingPointError('The split linear system needs finite stored arrays: '+row['file'])
        return values

    def all(self,name):
        if name not in self._values:raise ValueError('Use streamed stages for the new complete J')
        return self._values[name].copy()

    def raw(self,name):return self.B.float_bytes(self._values[name])

    def stages(self):
        expected=0
        for old,J in self.original.stages():
            if old in SELECTED:
                row=self.short[(old,'reference')]
                self.B.same(hashlib.sha256(self.B.float_bytes(J)).hexdigest(),row['sha256'],
                    'same selected old long-J reference '+str(old))
                for kind in ('outer','inner'):
                    self.B.same(self.cells[expected]['originalStage'],old,'new virtual stage order')
                    yield expected,self.short[(old,kind)];expected+=1
            else:
                self.B.same(self.cells[expected]['originalStage'],old,'unchanged old virtual stage order')
                yield expected,J;expected+=1
        self.B.same(expected,self.depth,'all new virtual stage blocks')

    def stage_bytes(self):
        for stage,J in self.stages():
            raw=self.B.float_bytes(J)
            self.B.same(hashlib.sha256(raw).hexdigest(),self.J_rows[stage]['raw_sha256'],'reread new complete J block')
            yield stage,raw

    def stage_raw(self,stage):
        if not 0<=stage<self.depth:raise ValueError('New stage index outside the complete system')
        cell=self.cells[stage];old=cell['originalStage']
        if old in SELECTED:
            raw=self.B.float_bytes(self.short[(old,'outer' if cell['window']==[6,12] else 'inner')])
        else:
            raw=None
            for descriptor,block in self.original.chunks('stage-jacobians'):
                if descriptor['row_start']<=old<descriptor['row_stop']:
                    raw=self.B.float_bytes(block[old-descriptor['row_start']]);break
            if raw is None:raise ValueError('Complete original J block not found')
        self.B.same(hashlib.sha256(raw).hexdigest(),self.J_rows[stage]['raw_sha256'],'exact witness complete block')
        return raw

    def export_inputs(self,output):
        exported={name:output.save('split-system-'+name,value,
            'Explicit new578-stage finite-system array; original boundary and old-node identities are in input-binding')
            for name,value in self._values.items()}
        for n in SELECTED:
            for kind in ('outer','inner'):
                exported[f'stage-{n}-{kind}-J']=output.save(f'split-system-stage-{n}-{kind}-J',self.short[(n,kind)],
                    'Exact original bytes from the completed actual four-short-block probe; no J recomputation')
        return exported


class DynamicExactContext:
    """Reuse only depth-independent exact kernels; all578 indexing is explicit."""
    _PASSTHROUGH={'decode_bits','decoded_array','sigma_denominator','compact_unit','fraction_record',
        'better','public_record','json_bytes','stage_job','boundary_job'}

    def __init__(self,system,kernel):self.system=system;self.kernel=kernel

    def __getattr__(self,name):
        if name in self._PASSTHROUGH:return getattr(self.kernel,name)
        raise AttributeError('No implicit use of original576 helper: '+name)

    def read_raw_array(self,capture,name):
        if capture is not self.system:raise ValueError('Use the same explicitly bound split system')
        return capture.raw(name)

    def stage_bytes(self,capture):
        if capture is not self.system:raise ValueError('Use the same explicitly bound split system')
        yield from capture.stage_bytes()

    def row_order(self,kind,node,row):
        M,K,D=self.system.M,self.system.K,self.system.depth
        if kind=='cut':return row
        if kind=='stage':return M+node*K+row
        if kind=='far':return M+D*K+row
        raise ValueError('Unknown complete split equation block')

    def max_record(self,kind,node,row,value,sigma_word):
        E=self.kernel;M=self.system.M;denominator=E.sigma_denominator(sigma_word)
        result=dict(kind=kind,node=node,row=row,global_equation_row=self.row_order(kind,node,row),
            component=('Q' if row<M else 'Pi') if kind=='stage' else 'Q' if kind=='cut' else 'Pi-minus-original-GQ',
            mode=row%M+1 if kind=='stage' else row+1,
            original_sigma_float64le_hex=struct.pack('<Q',sigma_word).hex(),
            exact_unscaled_dyadic=E.compact_unit(value),exact_signed_scaled_residual=E.fraction_record(value,denominator),
            exact_absolute_scaled_residual=E.fraction_record(abs(value),denominator),
            matrix_scope='explicit-new578-stage-system',
            new_matrix_identity_sha256=self.system.binding['new_matrix_identity_sha256'],
            _integer=value,_denominator=denominator)
        if kind=='stage':result['source_stage']=self.system.cells[node]
        return result

    def worst_witness(self,capture,record,direction_raw,inputs):
        if capture is not self.system:raise ValueError('The exact witness must use the same split system')
        M,K,D=capture.M,capture.K,capture.depth;kind=record['kind'];row=record['row'];node=record['node']
        def word(raw,index):return raw[index*8:(index+1)*8].hex()
        if len(direction_raw)!=(D+1)*K*8:raise ValueError('Keep every complete split direction word')
        common=dict(new_matrix_identity_sha256=capture.binding['new_matrix_identity_sha256'],
            complete_direction_float64le_sha256=hashlib.sha256(direction_raw).hexdigest(),
            node=node,row=row,kind=kind,explicit_node_sigma_float64le_hex=word(inputs['original-scales'],node))
        if kind=='stage':
            raw=capture.stage_raw(node)
            return dict(common,source_stage=capture.cells[node],complete_stage_J_raw_sha256=hashlib.sha256(raw).hexdigest(),
                full_J_row_float64le_hex=raw[row*K*8:(row+1)*K*8].hex(),
                full_next_delta_float64le_hex=direction_raw[(node+1)*K*8:(node+2)*K*8].hex(),
                current_delta_float64le_hex=word(direction_raw,node*K+row),
                residual_float64le_hex=word(inputs['stage-residuals'],node*K+row))
        if kind=='cut':return dict(common,delta_float64le_hex=word(direction_raw,row),
            residual_float64le_hex=word(inputs['cut-residual'],row))
        if kind=='far':return dict(common,delta_Q_float64le_hex=word(direction_raw,D*K+row),
            delta_Pi_float64le_hex=word(direction_raw,D*K+M+row),
            original_G_float64le_hex=word(inputs['original-far-graph'],row),
            residual_float64le_hex=word(inputs['end-residual'],row))
        raise ValueError('Unknown split exact witness row')
