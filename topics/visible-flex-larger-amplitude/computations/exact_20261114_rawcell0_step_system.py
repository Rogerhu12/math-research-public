#!/usr/bin/env python3
"""Bind actual28 and a complete rawCell0 original-RK-step capture.

The actual original integrationGrid, including its cusp steps, determines
the new depth. The original 577 nodes and the other 504 full stage blocks
are retained. This is an independently identified expanded finite matrix,
not a claim that a restricted direction solves the old rounded long-J A.
No flow, J, native solve, or nonlinear trial is evaluated by this module.
"""
from __future__ import annotations

import hashlib
import gzip
import importlib
import json
import math
from pathlib import Path
import re
import struct

import numpy as np


HERE=Path(__file__).resolve().parent
BAND_NAME='geometry_20261114_native_captured_band_correction.py'
BAND_SHA='b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390'
CAPTURE_SHA='ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7'
PROBE_NAME='geometry_20261114_native_rawcell0_step_capture.py'
PROBE_SHA='c2341018c6293e15ee8e5ba9109b331b29bee2e3e944514e1a0308afe8e6ffd5'
HOOK_NAME='geometry_20261114_native_rawcell0_step_capture_hook.mjs'
HOOK_SHA='2695cd2dc0abc66fe3f8ae8987b6ae3b50b884f692a418198347a61dddf24435'
WINDOW_NAME='geometry_20261114_native_rawcell0_step_windows.mjs'
WINDOW_SHA='07dd6101569097a9524c35457c1467002a250911dd049bcb720b3b8c700efd2b'
FLOW_SHA='717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f'
GRID_SHA='b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f'
STOP='VISIBLE_NATIVE_RAWCELL0_STEP_CAPTURE_COMPLETE_V1'
SELECTED=tuple(range(72))
MATRIX_SCOPE='rawcell0-original-RK-step-expanded-system'


def file_sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for raw in iter(lambda:stream.read(1<<20),b''):h.update(raw)
    return h.hexdigest()


def load_binding():
    source=HERE/BAND_NAME
    if file_sha(source)!=BAND_SHA:raise ValueError('The frozen complete actual28 binder changed')
    module=importlib.import_module(Path(BAND_NAME).stem)
    if Path(module.__file__).resolve()!=source.resolve():raise ValueError('Unexpected actual28 binder import path')
    return module


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def number_bits(value):
    """The native producer uses binary64; its record preserves signed zero."""
    if isinstance(value,dict):
        text=value.get('float64le_hex')
        if not isinstance(text,str) or not re.fullmatch(r'[0-9a-f]{16}',text):
            raise ValueError('A complete native binary64 bit record is required')
        raw=bytes.fromhex(text)
        if not math.isfinite(struct.unpack('<d',raw)[0]):raise ValueError('A finite original schedule value is required')
        return raw
    if type(value) not in (int,float) or not math.isfinite(value):
        raise ValueError('Use an original finite native binary64 value or its full bit record')
    return struct.pack('<d',value)


class StepArrays:
    """Separate source-bound inventory; reuse only frozen raw-byte I/O rules."""
    def __init__(self,directory,manifest,B):
        self.directory=Path(directory).resolve();self.B=B;self.arrays={}
        self.verified_bytes=self.verified_chunks=0;self.chunk_files=set()
        for row in manifest['arrays']:
            name=row['name']
            if not isinstance(name,str) or not name or name in self.arrays:
                raise ValueError('Every actual step array needs one unique nonempty name')
            B.same(row.get('completed'),True,'all actual step array chunks complete')
            B.same(row.get('dtype'),'<f8','actual step binary64 dtype')
            B.same(row.get('order'),'C','actual step C array order')
            self.arrays[name]=row
        for name in self.arrays:
            # This method binds every chunk size/hash, complete row order,
            # full raw hash and file uniqueness to this independent object.
            B.CapturedArrays.verify_array(self,name)

    def chunks(self,name,verify=True):
        yield from self.B.CapturedArrays.chunks(self,name,verify=verify)

    def all(self,name):
        return self.B.CapturedArrays.all(self,name)

    def row(self,name,index):
        entry=self.arrays[name]
        if not 0<=index<entry['shape'][0]:raise ValueError('Actual step row index out of range')
        for descriptor,values in self.chunks(name):
            if descriptor['row_start']<=index<descriptor['row_stop']:
                return np.array(values[index-descriptor['row_start']],copy=True)
        raise ValueError('A complete actual step row is missing')


class RawCell0StepSystem:
    """Source-bound dynamic-depth native shooting arrays, streamed by stage."""
    def __init__(self,capture_directory,step_directory,step_result_sha256,B=None):
        self.B=B or load_binding();B=self.B;B.actions_only()
        if not re.fullmatch(r'[0-9a-f]{64}',step_result_sha256):
            raise ValueError('Supply the actual completed step capture result SHA256; no future result is inferred')
        for name,digest in ((PROBE_NAME,PROBE_SHA),(HOOK_NAME,HOOK_SHA),(WINDOW_NAME,WINDOW_SHA)):
            B.same(file_sha(HERE/name),digest,'frozen original-step producer '+name)
        self.original=B.CapturedArrays(capture_directory,CAPTURE_SHA)
        self.directory=Path(step_directory).resolve();self.step_result_sha256=step_result_sha256
        B.same(file_sha(self.directory/'result.json'),step_result_sha256,'actual completed step result bytes')
        self.result=B.read(self.directory/'result.json');result=self.result
        for key,value in dict(schema='original-native-rawcell0-step-capture-result-v1',
            capture_completed=True,source_sha256=PROBE_SHA,hook_sha256=HOOK_SHA,
            window_module_sha256=WINDOW_SHA,capture_result_sha256=CAPTURE_SHA,
            native_accepted=False,task_completed=False,worker_exit_code=0,
            original_protocol_requests=1,planned_probe_stop_observed=True,
            actual_original_failure_message='Error: '+STOP,
            original_native_solve_called=False,new_whole_tail_J_evaluations=0,
            new_original_long_J_evaluations=0,no_J_evaluations=0,additional_ODE_steps=0,
            endpoint_J_or_audit_computed=False).items():
            B.same(result.get(key),value,'actual complete step result '+key)
        if result.get('unexpected_error') or result.get('unexpected_complete_native_response_returned'):
            raise ValueError('Consume a complete scoped step capture, never an unexpected native result')
        self.small={}
        for row in result['small_output_files']:
            name=row['file']
            if not isinstance(name,str) or Path(name).name!=name or name in self.small:
                raise ValueError('Unique bounded top-level step metadata names are required')
            path=B.safe_file(self.directory,name)
            B.same(path.stat().st_size,row['bytes'],'actual step metadata size '+name)
            B.same(file_sha(path),row['sha256'],'actual step metadata bytes '+name)
            self.small[name]=row
        spec=self.json('rawcell0-step-spec.json');self.step_spec=spec
        summary=self.json('rawcell0-step-summary.json');self.summary=summary
        manifest=self.json('rawcell0-step-array-manifest.json');self.manifest=manifest
        B.same(self.small['rawcell0-step-spec.json']['sha256'],result['spec_sha256'],'actual step specification')
        B.same(self.small['rawcell0-step-summary.json']['sha256'],result['capture_summary_sha256'],'actual step summary')
        B.same(summary['array_manifest'],{key:self.small['rawcell0-step-array-manifest.json'][key]
            for key in ('file','bytes','sha256')},'complete step array manifest')
        for key,value in dict(schema='original-native-rawcell0-step-capture-summary-v1',
            capture_completed=True,source_sha256=PROBE_SHA,hook_sha256=HOOK_SHA,
            window_module_sha256=WINDOW_SHA,completed_original_stages=list(SELECTED),
            original_capture_result_sha256=CAPTURE_SHA,native_accepted=False,task_completed=False).items():
            B.same(summary.get(key),value,'complete step summary '+key)
        B.same(summary['spec_sha256'],result['spec_sha256'],'step summary/spec identity')
        for key,name in (('original_candidate_float64le_sha256','base-states'),
            ('original_height_float64le_sha256','physical-height'),
            ('original_scales_float64le_sha256','original-scales'),
            ('original_far_graph_float64le_sha256','original-far-graph')):
            B.same(summary[key],self.original.arrays[name]['raw_sha256'],'original native bits '+name)
        B.same(spec['references']['capture_binding'],self.original.binding,'complete original576 capture binding')
        B.same(spec['references'],self.json('original-reference-packets.json'),'all original reference packet descriptors')
        B.same(spec['capture']['array_sha256'],self.original.binding['raw_array_sha256'],
            'every original576 source array used by the step capture')
        B.same(spec['fresh_request'],self.original.spec['fresh_request'],'same original full H and request flags')
        B.same(self.json('original-live-identity-before-seed.json'),self.original.live,
            'all original native profiles/layout/graphs/gains identity')
        for key,value in dict(schema='original-native-rawcell0-step-arrays-v1',completed=True,
            source_sha256=PROBE_SHA,hook_sha256=HOOK_SHA,
            window_module_sha256=WINDOW_SHA,spec_sha256=result['spec_sha256']).items():
            B.same(manifest.get(key),value,'complete raw step manifest '+key)
        self.step_arrays=StepArrays(self.directory,manifest,B)
        self.metadata_packets={}
        for packet in manifest['metadata_packets']:
            name=packet['file']
            if name in self.metadata_packets:raise ValueError('A completed actual metadata packet was listed twice')
            path=B.safe_file(self.directory,name)
            B.same(path.stat().st_size,packet['bytes'],'actual streamed field packet size')
            B.same(file_sha(path),packet['sha256'],'actual streamed field packet bytes')
            B.same(packet['encoding'],'json-gzip','actual field packet encoding')
            h=hashlib.sha256();count=0
            with gzip.open(path,'rb') as stream:
                for raw in iter(lambda:stream.read(1<<20),b''):h.update(raw);count+=len(raw)
            B.same(count,packet['raw_bytes'],'complete actual field packet raw size')
            B.same(h.hexdigest(),packet['raw_sha256'],'complete actual field packet raw bytes')
            self.metadata_packets[name]=packet
        # Unlike a grouped manifest, a streaming journal can interleave
        # the four arrays of one step. Bind every actual descriptor and
        # preserve its order within that array, without reordering it.
        ledger_path=B.safe_file(self.directory,'large-array-chunks.jsonl')
        if 'large-array-chunks.jsonl' not in self.small:raise ValueError('The complete actual chunk journal is missing')
        for key in ('file','bytes','sha256'):
            B.same(manifest['chunk_ledger'][key],self.small['large-array-chunks.jsonl'][key],
                'actual manifest/chunk journal binding '+key)
        expected={(name,row['chunk_index']):row for name,entry in self.step_arrays.arrays.items()
            for row in entry['chunks']}
        seen=set();next_index={name:0 for name in self.step_arrays.arrays}
        with ledger_path.open() as stream:
            for line in stream:
                row=json.loads(line);key=(row['array'],row['chunk_index'])
                if key in seen or key not in expected:raise ValueError('Duplicate or unlisted actual step chunk')
                B.same(row,expected[key],'exact actual step journal descriptor')
                B.same(row['chunk_index'],next_index[row['array']],'actual per-array chunk write order')
                next_index[row['array']]+=1;seen.add(key)
        B.same(seen,set(expected),'complete actual step journal coverage')

        self.M,self.K,self.original_depth=112,224,576
        B.same((self.original.M,self.original.K,self.original.depth),(112,224,576),'actual28 full dimensions')
        selected=tuple(n for n,row in enumerate(self.original.live['stages']) if row['rawCell']==0)
        B.same(selected,SELECTED,'exact complete original rawCell0 stages')
        self.selected=frozenset(selected);self.stage_reports={};self.stage_arrays={};self.step_counts={}
        B.same(len(summary['stage_reports']),len(SELECTED),'every complete original rawCell0 report')
        used_names=set()
        for n,descriptor in zip(SELECTED,summary['stage_reports']):
            report=self.json_descriptor(descriptor);B.same(report['stage'],n,'complete original-stage report order')
            for key,value in dict(schema='original-native-rawcell0-original-stage-steps-v1',rawCell=0,
                original_guards_returned=True,all_actual_original_steps_saved=True,
                complete226_state_kept_between_all_steps=True,mean_not_reset_at_new_nodes=True,
                original_profile_grid_and_x_h_retained=True,original_port_applied_only_at_final_step=True,
                no_product_of_short_J_blocks_formed=True,new_J_is_not_claimed_old_long_J=True,
                no_noJ_flow_or_whole_long_J_reference_recomputed=True,native_accepted=False).items():
                B.same(report.get(key),value,'complete actual stage contract '+key)
            B.same(report['rawSegment'],self.original.live['stages'][n]['rawSegment'],'original raw segment')
            window=self.json_descriptor(report['identity'])
            for key,value in dict(stage=n,rawCell=0,steps=12,profiles=len(self.original.live['stages'][n]['profiles']),
                input_shape_dimension=224,full_state_dimension=226,no_profile_reparameterization=True,
                no_mean_state_reset_between_steps=True,original_port_division_only_at_original_exit=True,
                additional_ODE_steps=0,no_changes_to_original_graphs_gains_far_sigma_or_acceptance=True).items():
                B.same(window.get(key),value,'actual original step-window identity '+key)
            B.same(window['source']['original_flow_module_sha256'],FLOW_SHA,'same original withJac flow module')
            B.same(window['source']['exact_source_roundtrip_verified'],True,'original RK body reversible insertion')
            B.same(window['source']['tangent_identity_reset_before_every_original_step'],True,'actual local tangent origins')
            B.same(window['integration_grid']['source_sha256'],GRID_SHA,'same original integrationGrid module')
            B.same(report['field_observations'],self.metadata_packets.get(report['field_observations']['file']),
                'all already evaluated field observations retained')
            count=report['step_count']
            if type(count) is not int or count<1:raise ValueError('An original stage needs its actual positive step count')
            schedule=report['schedule'];B.same(len(schedule),count,'all actual original schedule steps')
            B.same(report['completed_original_field_calls'],4*count,'exactly the original four RK field calls per step')
            profiles=report['profile_schedules']
            B.same(len(profiles),len(self.original.live['stages'][n]['profiles']),'all original profiles retained')
            flattened=[]
            for p,profile in enumerate(profiles):
                B.same(profile['profile_index'],p,'original profile order')
                pc=profile['step_count']
                if type(pc) is not int or pc<1:raise ValueError('Every original profile needs its actual grid step count')
                original_cuts=self.original.live['stages'][n]['profiles'][p]
                expected_branch='integrationGrid' if original_cuts else 'ordinary'
                B.same(profile['grid_branch'],expected_branch,'original cusp/ordinary branch')
                B.same([number_bits(x) for x in profile['cuts']],[number_bits(x) for x in original_cuts],
                       'complete original profile integration breakpoints')
                if expected_branch=='ordinary':
                    B.same(profile['grid'],None,'ordinary profile has no substituted grid')
                    B.same(pc,12,'original ordinary RK12 count')
                    number_bits(profile['ordinary_h'])
                else:
                    B.same(len(profile['grid']),pc+1,'all actual original integrationGrid nodes')
                    for point in profile['grid']:number_bits(point)
                flattened.extend((p,k,profile['grid_branch']) for k in range(pc))
            B.same(len(flattened),count,'sum of actual original integrationGrid/profile lengths')
            old_port=self.original.live['stages'][n]['portRatio']
            for k,(step,(p,gi,branch)) in enumerate(zip(schedule,flattened)):
                B.same((step['global_step'],step['profile_index'],step['grid_index'],step['grid_branch']),
                       (k,p,gi,branch),'every original grid index and branch')
                B.same(step['final_original_step'],k==count-1,'unique original exit step')
                B.same((step['full_state_row'],step['shape_output_row'],step['shape_J_row']),
                       (k+1,k,k),'complete actual per-step array row bindings')
                B.same(step['field_calls'],4,'all four original field evaluations')
                B.same(step['port_applied'],k==count-1,'only original final step applies the port')
                B.same(number_bits(step['port_ratio']),number_bits(old_port if k==count-1 else 1.),
                       'original port only at the one original stage exit')
                # Preserve x/h themselves. In the ordinary branch it is
                # wrong to replace constant h by adjacent rounded x gaps.
                number_bits(step['x']);number_bits(step['h'])
                if branch=='integrationGrid':
                    B.same(number_bits(step['x']),number_bits(profiles[p]['grid'][gi]),'original cusp step start node')
                else:
                    B.same(number_bits(step['h']),number_bits(profiles[p]['ordinary_h']),'original constant ordinary h')
            names=report['arrays']
            for role,shape in (('full_states',[count+1,226]),('shape_outputs',[count,224]),
                ('shape_jacobians',[count,224,224]),('mean_tangent_rows',[count,2,224])):
                name=names[role]
                if name in used_names or name not in self.step_arrays.arrays:
                    raise ValueError('Every role/stage must retain its own complete actual array')
                used_names.add(name)
                B.same(self.step_arrays.arrays[name]['shape'],shape,'actual complete '+role+' shape')
            self.stage_reports[n]=report;self.stage_arrays[n]=dict(names);self.step_counts[n]=count
        total_steps=sum(self.step_counts.values())
        B.same(summary['total_step_count'],total_steps,'actual total original rawCell0 step count')
        B.same(summary['completed_local_J_blocks'],total_steps,'actual complete local J count')
        B.same(summary['completed_local_J_evaluations'],total_steps,'actual original local J evaluations')
        B.same(summary['completed_original_RK_field_calls'],4*total_steps,'all actual original field calls')
        B.same(summary['original_RK_field_entries'],4*total_steps,'all actual original RK field entries')
        for key,value in dict(original_steps=12,original_native_solve_called=False,new_whole_tail_J_evaluations=0,
            new_original_long_J_evaluations=0,no_J_evaluations=0,nonlinear_trials=0,
            endpoint_J_or_audit_computed=False,additional_ODE_steps=0,
            original_live_functions_graphs_gains_far_and_scales_unchanged=True,
            all_original_seed_bytes_unchanged=True,planned_probe_stop=STOP,
            original_native_request_intentionally_stopped_before_solve=True).items():
            B.same(summary.get(key),value,'unchanged complete actual capture contract '+key)
        self.depth=self.original_depth-len(SELECTED)+total_steps
        self.old_to_new=[];self.cells=[]
        for n in range(self.original_depth):
            self.old_to_new.append(len(self.cells))
            if n in self.selected:
                count=self.step_counts[n]
                for k in range(count-1,-1,-1):
                    self.cells.append(dict(newStage=len(self.cells),originalStage=n,rawCell=0,
                        kind='actual-original-RK-step',stepIndex=k,originalStepCount=count,
                        schedule=self.stage_reports[n]['schedule'][k],
                        port='original-exit' if k==count-1 else 'one'))
            else:
                self.cells.append(dict(newStage=len(self.cells),originalStage=n,
                    rawCell=self.original.live['stages'][n]['rawCell'],kind='unchanged-original-stage',
                    stepIndex=None,port='original-exit'))
        self.old_to_new.append(len(self.cells));B.same(len(self.cells),self.depth,'complete dynamic system depth')
        layout=self.json_descriptor(summary['prospective_layout']);self.layout=layout
        for key,value in dict(schema='original-native-rawcell0-step-layout-v1',originalDepth=576,
            newDepth=self.depth,selectedOriginalStages=list(SELECTED),oldToNew=self.old_to_new,
            not_installed_in_original_dn=True,not_a_solved_new_system=True,
            no_old_long_J_defect_acceptance_gate=True).items():
            B.same(layout.get(key),value,'complete actual prospective layout '+key)
        expected_cells=[]
        for cell in self.cells:
            n=cell['originalStage'];k=cell['stepIndex'];selected=n in self.selected
            expected_cells.append(dict(newStage=cell['newStage'],originalStage=n,
                local_flow_step=k,shape_J_source='actual-original-step-capture' if selected else 'unchanged-actual28',
                shape_J_array=self.stage_arrays[n]['shape_jacobians'] if selected else None,
                shape_J_row=k,port='original' if cell['port']=='original-exit' else 'one'))
        B.same(layout['cells'],expected_cells,'every exact prospective local block/row map')
        old_states=self.original.all('base-states');old_out=self.original.all('stage-out')
        old_r=self.original.all('stage-residuals');old_sigma=self.original.all('original-scales').reshape(-1)
        old_guard_mean=self.original.all('stage-guard-mean')
        states=np.empty((self.depth+1,self.K),dtype='<f8')
        outputs=np.empty((self.depth,self.K),dtype='<f8');residuals=np.empty_like(outputs)
        scales=np.empty(self.depth+1,dtype='<f8')
        old_indices=np.asarray(self.old_to_new,dtype=np.int64)
        states[old_indices]=old_states;scales[old_indices]=old_sigma
        for n in SELECTED:
            names=self.stage_arrays[n];count=self.step_counts[n];start=self.old_to_new[n]
            report=self.stage_reports[n];reference=spec['references']['selected_stages'][str(n)]
            B.same(reference['original_live_stage'],self.original.live['stages'][n],'unchanged original stage reference')
            for role,key,value in (('input','original_input_reference',old_states[n+1]),
                ('output','original_output_reference',old_out[n]),
                ('guard-mean','original_guard_mean_reference',old_guard_mean[n])):
                row=report[key];B.same(row,reference[role],'same original stage reference descriptor')
                B.same(row['dtype'],'<f8','original reference binary64 dtype')
                B.same(row['shape'],list(value.shape),'complete original reference dimensions')
                B.same(row['sha256'],hashlib.sha256(B.float_bytes(value)).hexdigest(),'original reference actual bits')
                B.same(row['bytes'],value.nbytes,'complete original reference byte count')
            B.same(number_bits(report['original_sigma']),B.float_bytes(old_sigma[n:n+1]),'original stage sigma bits')
            B.same(number_bits(report['original_port_ratio']),number_bits(self.original.live['stages'][n]['portRatio']),
                'original stage exit port bits')
            full=self.step_arrays.all(names['full_states']);out=self.step_arrays.all(names['shape_outputs'])
            if not np.isfinite(full).all() or not np.isfinite(out).all():
                raise FloatingPointError('An actual expanded base state/output is nonfinite')
            B.same(B.float_bytes(full[0,:self.K]),B.float_bytes(old_states[n+1]),'original input shape bits')
            B.same(B.float_bytes(full[0,self.K:]),bytes(16),'two original positive-zero mean initial values')
            for k in range(1,count):
                node=start+count-k;states[node]=full[k,:self.K];scales[node]=old_sigma[n]
            for k in range(count):
                stage=start+count-1-k;outputs[stage]=out[k]
                if k<count-1:
                    B.same(B.float_bytes(out[k]),B.float_bytes(full[k+1,:self.K]),
                           'complete internal step output/state words')
                else:
                    B.same(B.float_bytes(out[k,:self.M]),B.float_bytes(full[k+1,:self.M]),
                           'the original exit port never changes Q')
                # The rounded subtraction defines and preserves this
                # new finite residual array. At inserted nodes its two
                # operands are identical actual saved state words.
                residuals[stage]=out[k]-states[stage]
        for n in range(self.original_depth):
            if n not in self.selected:
                stage=self.old_to_new[n];outputs[stage]=old_out[n];residuals[stage]=old_r[n]
        B.same(B.float_bytes(states[old_indices]),B.float_bytes(old_states),'all original577 base node words')
        B.same(B.float_bytes(scales[old_indices]),B.float_bytes(old_sigma),'all original577 sigma words')
        explicit_name=layout['explicit_node_sigma_array']
        B.same(self.step_arrays.arrays[explicit_name]['shape'],[1,self.depth+1],'all actual explicit sigma dimensions')
        B.same(B.float_bytes(self.step_arrays.all(explicit_name)),B.float_bytes(scales),'all actual explicit sigma words')
        B.same(layout['old_node_sigma_sha256'],self.original.arrays['original-scales']['raw_sha256'],
            'actual layout retains every original sigma')
        self._values={'base-states':states,'stage-residuals':residuals,'stage-out':outputs,
            'original-scales':scales.reshape(1,-1)}
        for name in ('cut-residual','end-residual','original-far-graph','physical-height','cut-target'):
            self._values[name]=self.original.all(name)
        for name,value in self._values.items():
            if not np.isfinite(value).all():raise FloatingPointError('Nonfinite expanded-system array '+name)
            value.flags.writeable=False
        if not (scales>0).all():raise ValueError('Every explicit expanded-node sigma must remain positive')
        self.arrays={name:dict(shape=list(value.shape),dtype='<f8',order='C',total_bytes=value.nbytes,
            raw_sha256=hashlib.sha256(B.float_bytes(value)).hexdigest()) for name,value in self._values.items()}
        self.live=dict(stages=[dict(self.original.live['stages'][cell['originalStage']],
            originalStage=cell['originalStage'],newStage=cell['newStage'],expanded_step=cell,
            shape_J_source='actual-original-step-capture' if cell['originalStage'] in self.selected else 'unchanged-actual28')
            for cell in self.cells])
        self.spec=dict(numerical_parameters={'spacing':self.original.spec['numerical_parameters']['spacing']},
            original_full_native_spec_sha256=self.original.binding['capture_spec_sha256'])
        self.J_rows=[];full_hash=hashlib.sha256()
        for stage,J in self.stages():
            if not np.isfinite(J).all():raise FloatingPointError('Nonfinite actual expanded J block '+str(stage))
            raw=B.float_bytes(J);full_hash.update(raw);cell=self.cells[stage]
            self.J_rows.append(dict(new_stage=stage,original_stage=cell['originalStage'],step_index=cell['stepIndex'],
                origin='actual-original-step-capture' if cell['originalStage'] in self.selected else 'unchanged-actual28',
                raw_sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw)))
        B.same(len(self.J_rows),self.depth,'complete actual new block manifest')
        self.arrays['stage-jacobians']=dict(shape=[self.depth,self.K,self.K],dtype='<f8',order='C',
            total_bytes=self.depth*self.K*self.K*8,raw_sha256=full_hash.hexdigest(),virtual_stream=True)
        self.binding=dict(schema='native-rawcell0-original-step-system-binding-v1',matrix_scope=MATRIX_SCOPE,
            adapter_source_sha256=file_sha(__file__),original_capture_binding=self.original.binding,
            actual_step_result_sha256=step_result_sha256,actual_step_source_sha256=PROBE_SHA,
            actual_step_hook_sha256=HOOK_SHA,window_source_sha256=WINDOW_SHA,
            actual_step_spec_sha256=result['spec_sha256'],actual_step_summary_sha256=result['capture_summary_sha256'],
            actual_step_small_files=self.small,actual_step_array_manifest_sha256=self.small['rawcell0-step-array-manifest.json']['sha256'],
            actual_step_metadata_packets=self.metadata_packets,
            actual_step_array_raw_sha256={name:row['raw_sha256'] for name,row in self.step_arrays.arrays.items()},
            actual_step_verified_chunks=self.step_arrays.verified_chunks,actual_step_verified_bytes=self.step_arrays.verified_bytes,
            original_depth=self.original_depth,new_depth=self.depth,original_nodes=self.original_depth+1,new_nodes=self.depth+1,
            modes=self.M,shape_dimension=self.K,old_to_new=self.old_to_new,expanded_original_stages=list(SELECTED),
            original_step_counts=[dict(stage=n,step_count=self.step_counts[n]) for n in SELECTED],
            original_cusp_stages=[n for n in SELECTED if any(self.original.live['stages'][n]['profiles'])],
            actual_total_original_steps=total_steps,cells=self.cells,complete_block_manifest=self.J_rows,
            raw_array_sha256={name:row['raw_sha256'] for name,row in self.arrays.items()},
            reused_original_stage_J_blocks=self.original_depth-len(SELECTED),new_local_step_J_blocks=total_steps,
            new_J_computed_here=0,new_ODE_steps=0,original_finite_scalar_profile_and_RK_schedule_unchanged=True,
            original226_state_continued_at_every_actual_step=True,original_mean_tangent_rows_preserved_in_input_artifact=True,
            old_nodes_and_original_cut_far_H_preserved=True,
            inserted_sigma_rule='Exact original parent-stage sigma; all old-node sigma words retained',
            expanded_residual_rule='Actual captured per-step shape output minus its stored new node; original exit uses old outgoing node',
            original_504_r_and_output_reused_byte_for_byte=True,
            new_linear_representation_not_original_576_A=True,not_accumulated_on_previous_578_system=True,
            old_long_J_defect_is_diagnostic_not_acceptance_gate=True,
            final_original_full_nonlinear_readback_still_required=True,
            no_native_solve_or_trial=True,native_accepted=False,task_completed=False)
        self.binding['new_matrix_identity_sha256']=canonical_sha(dict(
            adapter_source_sha256=self.binding['adapter_source_sha256'],
            original_capture_result_sha256=CAPTURE_SHA,step_result_sha256=step_result_sha256,
            old_to_new=self.old_to_new,cells=self.cells,block_manifest=self.J_rows,
            arrays=self.binding['raw_array_sha256']))

    def json(self,name):
        if name not in self.small:raise ValueError('Missing actual complete step metadata: '+name)
        return self.B.read(self.B.safe_file(self.directory,name))

    def json_descriptor(self,row):
        name=row['file']
        if name not in self.small:raise ValueError('Step metadata descriptor is outside the actual inventory')
        for key in ('bytes','sha256'):self.B.same(row[key],self.small[name][key],'actual step metadata '+name+'/'+key)
        return self.json(name)

    def all(self,name):
        if name not in self._values:raise ValueError('Use streamed complete stage blocks for the new J')
        return self._values[name].copy()

    def raw(self,name):return self.B.float_bytes(self._values[name])

    def stages(self):
        expected=0
        for old,J in self.original.stages():
            if old in self.selected:
                names=self.stage_arrays[old]
                count=self.step_counts[old]
                # Native rows run outer-to-inner, whereas the actual
                # original integrationGrid capture runs inner-to-outer.
                # At most one original-stage array is retained here.
                blocks=self.step_arrays.all(names['shape_jacobians'])
                for k in range(count-1,-1,-1):
                    cell=self.cells[expected]
                    self.B.same((cell['originalStage'],cell['stepIndex']),(old,k),'actual reversed step order')
                    yield expected,blocks[k];expected+=1
            else:
                self.B.same(self.cells[expected]['originalStage'],old,'unchanged original block order')
                yield expected,J;expected+=1
        self.B.same(expected,self.depth,'all actual dynamic step-system blocks')

    def stage_bytes(self):
        for stage,J in self.stages():
            raw=self.B.float_bytes(J)
            self.B.same(hashlib.sha256(raw).hexdigest(),self.J_rows[stage]['raw_sha256'],
                        'reread actual complete expanded J block')
            yield stage,raw

    def stage_raw(self,stage):
        if not 0<=stage<self.depth:raise ValueError('Expanded stage outside the complete system')
        cell=self.cells[stage];old=cell['originalStage']
        if old in self.selected:
            value=self.step_arrays.row(self.stage_arrays[old]['shape_jacobians'],cell['stepIndex'])
            raw=self.B.float_bytes(value)
        else:
            raw=None
            for descriptor,block in self.original.chunks('stage-jacobians'):
                if descriptor['row_start']<=old<descriptor['row_stop']:
                    raw=self.B.float_bytes(block[old-descriptor['row_start']]);break
            if raw is None:raise ValueError('Unchanged original J block is missing')
        self.B.same(hashlib.sha256(raw).hexdigest(),self.J_rows[stage]['raw_sha256'],
                    'complete expanded exact witness J block')
        return raw

    def export_inputs(self,output):
        # The actual J chunks remain in their independently verified
        # original/capture directories; do not duplicate hundreds of MB.
        return {name:output.save('step-system-'+name,value,
            'Actual dynamic step-system array; original boundary and original-node bits bound in input-binding')
            for name,value in self._values.items()}


class DynamicExactContext:
    """Only depth-independent integer kernels; every row index is explicit."""
    _PASSTHROUGH={'decode_bits','decoded_array','sigma_denominator','compact_unit','fraction_record',
        'better','public_record','json_bytes','stage_job','boundary_job'}

    def __init__(self,system,kernel):self.system=system;self.kernel=kernel

    def __getattr__(self,name):
        if name in self._PASSTHROUGH:return getattr(self.kernel,name)
        raise AttributeError('No implicit original576 or split578 helper: '+name)

    def read_raw_array(self,capture,name):
        if capture is not self.system:raise ValueError('Use the same bound actual step system')
        return capture.raw(name)

    def stage_bytes(self,capture):
        if capture is not self.system:raise ValueError('Use the same bound actual step system')
        yield from capture.stage_bytes()

    def row_order(self,kind,node,row):
        M,K,D=self.system.M,self.system.K,self.system.depth
        if kind=='cut':return row
        if kind=='stage':return M+node*K+row
        if kind=='far':return M+D*K+row
        raise ValueError('Unknown complete actual step equation block')

    def max_record(self,kind,node,row,value,sigma_word):
        E=self.kernel;M=self.system.M;denominator=E.sigma_denominator(sigma_word)
        result=dict(kind=kind,node=node,row=row,global_equation_row=self.row_order(kind,node,row),
            component=('Q' if row<M else 'Pi') if kind=='stage' else 'Q' if kind=='cut' else 'Pi-minus-original-GQ',
            mode=row%M+1 if kind=='stage' else row+1,
            original_sigma_float64le_hex=struct.pack('<Q',sigma_word).hex(),
            exact_unscaled_dyadic=E.compact_unit(value),exact_signed_scaled_residual=E.fraction_record(value,denominator),
            exact_absolute_scaled_residual=E.fraction_record(abs(value),denominator),
            matrix_scope=MATRIX_SCOPE,new_matrix_identity_sha256=self.system.binding['new_matrix_identity_sha256'],
            _integer=value,_denominator=denominator)
        if kind=='stage':result['source_stage']=self.system.cells[node]
        return result

    def worst_witness(self,capture,record,direction_raw,inputs):
        if capture is not self.system:raise ValueError('The witness must use the same actual step system')
        M,K,D=capture.M,capture.K,capture.depth;kind=record['kind'];row=record['row'];node=record['node']
        def word(raw,index):return raw[index*8:(index+1)*8].hex()
        if len(direction_raw)!=(D+1)*K*8:raise ValueError('Keep every expanded direction word')
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
        raise ValueError('Unknown exact expanded row kind')
