#!/usr/bin/env python3
"""Reviewed public continuation of all remaining one-column cap cells and same-Z ports."""
from __future__ import annotations
import argparse,json,shutil,signal,sys
from pathlib import Path
from fourfold_codazzi_reviewed_CI_resume import ReviewedBodyWorker
from fourfold_codazzi_known_cut_direction_cap_CI_v3 import KnownCutDirectionWorker
from fourfold_codazzi_cap128_CI_worker import digest,read
from fourfold_codazzi_phase_high7_CI_worker import TOPIC
from fourfold_native_lossless_parts import restore

REL='topics/visible-flex-exact-nearby/'
PRODUCER=REL+'scripts/fourfold_codazzi_complete_cut_direction_Z_sources.py'
CAP='69f55939742b26988690e54b7f5636eb591a351063b93187feeb38c1f6611ebe'
CAP_CUT='36f498e3b0addbb46290c12fae6b63af7673db20ba230e22dd83809d18427104'
BOUNDARY='b1adeea522b31efa2fc83a6436bc3fe52dbd04630c17d5436927b5872b05e263'
PILOT='f36831b1f5cc354548686c7d3e5f3fdfb10a456899d25f57d1be1b4cefccbe5c'
PILOT_WORKER='ccf1b8d76eb68ce2731538b87e6f90f627d2633d1dc469272176743ba422d4d0'
PILOT_MANIFEST='fb0971a3d5e471c7c8d13d009c7dd23b109e3c88e6875f3236373cd79e329f5a'
RANGES=((0,512),(512,1024),(1024,1536),(1536,1977))


def small(path,doc):
    raw=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
    if len(raw)>60000:raise ValueError('a new plaintext summary exceeded60000 bytes; preserve the complete native')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)


def actual(process,run):
    return (process.get('repository')=='Rogerhu12/math-research-public'
        and str(process.get('run_id'))==str(run) and process.get('complete')
        and not process.get('failure') and process.get('children')
        and all(c.get('actual_returncode')==0 for c in process['children']))


class CompleteCutZWorker(ReviewedBodyWorker):
    def __init__(self,a):
        super().__init__(a)
        suffix=a.phase if a.phase!='range' else f'range-{a.first:04d}-{a.end:04d}'
        self.name=f'run-{self.run_label}-complete-cut-Z-{suffix}'
        self.dest=TOPIC/'notes/complete_cut_Z_source_ci'/self.name
        self.native_name=('complete-cut-direction-Z-plan.json.gz' if a.phase=='plan' else
            f'new-cut-direction-Z-cells-{a.first:04d}-{a.end:04d}.json.gz' if a.phase=='range' else
            'complete1977-cut-direction-and-same-Z-sources.json.gz')
        self.state.update(kind='actual_public_complete_cut_direction_and_same_Z_process_v1',
            worker_source_sha256=digest(__file__),phase=a.phase,
            source_range=[a.first,a.end] if a.phase=='range' else None,
            original_successful_v3_run=43610982446,original_successful_v3_native_sha256=PILOT,
            original_sixteen_completed_one_column_cells_reused=True,
            old_complete_matrix_residual_cells_recomputed=0,
            original_large_matrix_reconstructions_executed=0,
            original_true_endpoint_sources_recomputed=0,
            complete_finite193_response_error_proved=False,complete_infinite_inverse_proved=False)

    def check_inputs(self):
        super().check_inputs()
        if self.manifest.get('kind')!='complete_cut_direction_and_same_Z_sources_public_inputs_v1':
            raise ValueError('the independent complete same-Z cut source manifest is required')
        if self.args.phase=='range' and (self.args.first,self.args.end) not in RANGES:
            raise ValueError('the requested one-column range was not assigned')

    def execute(self,label,command):
        try:return super().execute(label,command)
        finally:
            path=self.cache/self.native_name
            if path.exists():
                native=read(path);rows=native.get('new_one_column_rows',[])
                outcome=dict(native_sha256=digest(path),complete=native.get('complete'),
                    failure=native.get('failure'),gates=native.get('gates',[]),
                    completed_new_range_cells=len(rows),
                    actual_new_cells_in_this_child=native.get('new_one_column_cells_executed_in_this_child'),
                    completed_indices=[r['index'] for r in rows] if len(rows)<=100 else None,
                    first_completed_index=rows[0]['index'] if rows else None,
                    last_completed_index=rows[-1]['index'] if rows else None)
                small(self.evidence/'actual-latest-child-outcome.json',outcome)
                print(json.dumps(outcome),flush=True)
                if native.get('failure') and self.log.exists():print(self.log.read_text()[-16000:],flush=True)

    def exact_native(self,root,name,process,expected=None):
        path=root/'native'/name
        if not path.exists():
            matches=[x for x in process.get('native_files',[]) if x.get('logical_file')=='native/'+name]
            if len(matches)!=1 or 'lossless_manifest' not in matches[0]:
                raise ValueError('the complete original native bytes are absent')
            path=self.work/('restored-'+matches[0]['sha256']+'.json.gz')
            if not path.exists():restore(root/matches[0]['lossless_manifest'],path)
        if digest(path)!=(expected or process.get('complete_native_sha256')):
            raise ValueError('the original actual native identity changed')
        return path

    def original_inputs(self):
        if self.args.phase=='range':
            candidate,proposal=KnownCutDirectionWorker.restore_exact_prepared_arrays(self)
        else:
            candidate=self.science/self.manifest['published_candidate']
            proposal=self.science/self.manifest['precomposed_descriptor']
        inputs=dict(candidate=candidate,proposal=proposal)
        for name,key in (('object','object_input'),('repair-report','repair_input'),('inlet','inlet_input'),
            ('q-vector','q_vector_input'),('q-native','q_native_input'),('hessian','hessian_input'),('cut','cut_input'),
            ('direction','complete_continuous_direction_native')):
            inputs[name]=self.science/self.manifest[key]
        specs={
            'cap':(self.args.cap_artifact,'complete-cap-native.json.gz',CAP,43583838015),
            'cap-cut':(self.args.cap_cut_artifact,'complete-cap-and-true-moving-cut-native.json.gz',CAP_CUT,43587619797),
            'boundary':(self.args.boundary_artifact,'known-waist-and-true-cap-sources.json.gz',BOUNDARY,43599771405),
            'pilot':(self.args.pilot_artifact,'known-cut-direction-complete-cap-mixed-source-pilot.json.gz',PILOT,43610982446)}
        for label,(root,name,expected,run) in specs.items():
            root=root.resolve();pp=root/'process.json';process=read(pp)
            if not actual(process,run) or process.get('complete_native_sha256')!=expected:
                raise ValueError('the true successful original '+label+' outcome is required')
            if label=='pilot' and (process.get('worker_source_sha256')!=PILOT_WORKER
                or process.get('input_manifest_sha256')!=PILOT_MANIFEST):
                raise ValueError('the original successful v3 one-column pilot identity changed')
            native=self.exact_native(root,name,process,expected)
            inputs[label]=native;inputs[label+'-process']=pp
            shutil.copyfile(pp,self.evidence/('original-'+label+'-artifact-process.json'))
        # The old pilot binds the three old process snapshots by their exact SHA.
        original=read(inputs['pilot'])
        for key,value in original['input_sha256'].items():
            if key not in inputs or digest(inputs[key])!=value:
                raise ValueError('an original cap artifact snapshot or exact source byte differs from v3')
        return inputs

    def completed_plan(self,inputs):
        root=TOPIC/'notes/complete_cut_Z_source_ci'
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!='Rogerhu12/math-research-public' or p.get('phase')!='plan'
                or not any(c.get('actual_returncode')==0 for c in p.get('children',[]))
                or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or p.get('actual_common_input_sha256')!=inputs):continue
            matches=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/complete-cut-direction-Z-plan.json.gz']
            if len(matches)!=1 or not isinstance(matches[0].get('sha256'),str) or len(matches[0]['sha256'])!=64:continue
            native=self.exact_native(pp.parent,'complete-cut-direction-Z-plan.json.gz',p,matches[0]['sha256']);old=read(native)
            if (old.get('complete') and not old.get('failure') and old.get('source_sha256')==self.manifest['files'][PRODUCER]
                and old.get('common_input_sha256')==inputs and old.get('gates') and all(x['passed'] for x in old['gates'])):
                self.state.update(original_completed_plan_process_complete=bool(p.get('complete')),
                    original_completed_plan_publication_failure=p.get('failure'))
                return pp,native
        return None

    def best_prefix(self,inputs,plan_sha):
        root=TOPIC/'notes/complete_cut_Z_source_ci';candidates=[]
        if not root.exists():return None
        for pp in sorted(root.glob('*/process.json')):
            p=read(pp)
            if (p.get('repository')!='Rogerhu12/math-research-public' or p.get('phase')!='range'
                or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or p.get('source_range')!=[self.args.first,self.args.end]
                or p.get('actual_common_input_sha256')!=inputs
                or p.get('actual_plan_native_sha256')!=plan_sha):continue
            matches=[x for x in p.get('native_files',[]) if x.get('logical_file')=='native/'+self.native_name]
            if len(matches)!=1:continue
            native=self.exact_native(pp.parent,self.native_name,p,matches[0]['sha256']);old=read(native)
            rows=old.get('new_one_column_rows',[])
            if (old.get('source_sha256')!=self.manifest['files'][PRODUCER]
                or old.get('common_input_sha256')!=inputs or old.get('plan_native_sha256')!=plan_sha
                or not rows or not all(x.get('actual_complete_one_column_cell') for x in rows)):continue
            candidates.append((len(rows),pp,native,old))
        return max(candidates,key=lambda x:x[0]) if candidates else None

    def actual_plan(self):
        root=self.args.plan_artifact.resolve();pp=root/'process.json';p=read(pp)
        if (not actual(p,self.args.workflow_run) or p.get('phase')!='plan'
            or p.get('worker_source_sha256')!=digest(__file__)
            or p.get('input_manifest_sha256')!=self.args.manifest_sha):
            raise ValueError('the same-run actual successful continuation plan is required')
        native=self.exact_native(root,'complete-cut-direction-Z-plan.json.gz',p)
        shutil.copyfile(pp,self.evidence/'actual-same-run-plan-process.json')
        return native

    def range_inputs(self,plan_sha):
        found={}
        for root in sorted(self.args.range_artifacts.iterdir()):
            if not root.is_dir() or not (root/'process.json').exists():continue
            pp=root/'process.json';p=read(pp);pair=tuple(p.get('source_range',[]))
            if (pair not in RANGES or pair in found or not actual(p,self.args.workflow_run)
                or p.get('phase')!='range' or p.get('worker_source_sha256')!=digest(__file__)
                or p.get('input_manifest_sha256')!=self.args.manifest_sha
                or p.get('actual_plan_native_sha256')!=plan_sha):
                raise ValueError('a complete source range artifact failed or changed identity')
            native=self.exact_native(root,f'new-cut-direction-Z-cells-{pair[0]:04d}-{pair[1]:04d}.json.gz',p)
            found[pair]=(native,pp)
        if set(found)!=set(RANGES):raise ValueError('all four actual source ranges are required')
        natives=[];processes=[]
        for pair in RANGES:
            native,pp=found[pair];natives.append(native);processes.append(pp)
            shutil.copyfile(pp,self.evidence/f'actual-range-{pair[0]:04d}-{pair[1]:04d}-process.json')
        return natives,processes

    def prepare(self):
        native=self.cache/self.native_name;inputs=self.original_inputs()
        expected={k:digest(v) for k,v in inputs.items()}
        self.state['actual_common_input_sha256']=expected
        command=[sys.executable,'-u',str(self.science/PRODUCER),'--phase',self.args.phase,
            '--workflow-run',str(self.args.workflow_run),'--out',str(native)]
        for k,v in inputs.items():command+=['--'+k,str(v)]
        if self.args.phase=='plan':
            previous=self.completed_plan(expected)
            if previous:
                pp,old=previous;command+=['--resume',str(old)]
                shutil.copyfile(pp,self.evidence/'original-completed-plan-process.json')
                self.state.update(original_complete_plan_native_sha256=digest(old),
                    original_plan_bytes_reused_without_recomputation=True)
        else:
            plan=self.actual_plan()
            if read(plan).get('common_input_sha256')!=expected:
                raise ValueError('all phases must use the same exact original artifact bytes')
            self.state['actual_plan_native_sha256']=digest(plan);command+=['--plan',str(plan)]
            if self.args.phase=='range':
                command+=['--first',str(self.args.first),'--end',str(self.args.end)]
                prefix=self.best_prefix(expected,digest(plan))
                if prefix:
                    count,pp,old,prior=prefix;command+=['--resume',str(old)]
                    shutil.copyfile(pp,self.evidence/'original-completed-range-prefix-process.json')
                    self.state.update(original_completed_range_cells_reused=count,
                        original_range_prefix_sha256=digest(old),original_range_prefix_failure=prior.get('failure'))
            else:
                natives,processes=self.range_inputs(digest(plan))
                command+=['--range-natives',*[str(p) for p in natives],'--range-processes',*[str(p) for p in processes]]
        self.publish();self.execute('actual_complete_cut_direction_same_Z_'+self.args.phase,command)
        result=read(native)
        if (not result.get('complete') or result.get('failure') or not result.get('selected_cells_complete')
            or result.get('source_sha256')!=self.manifest['files'][PRODUCER]
            or result.get('common_input_sha256')!=expected
            or not result.get('gates') or not all(x['passed'] for x in result['gates'])
            or result.get('complete_finite193_response_error_proved') or result.get('complete_infinite_inverse_proved')):
            raise ValueError('the actual complete same-Z cap result failed or exceeded its scope')
        summary=dict(phase=self.args.phase,native_sha256=digest(native),complete=True,gates=result['gates'],
            seconds=result.get('seconds'),common_input_sha256=expected,
            exact_continuous_direction_definition_sha256=result['exact_continuous_direction_definition_sha256'],
            reused_original_one_column_indices=result['reused_original_one_column_indices'],
            new_one_column_cells_executed_in_this_child=result.get('new_one_column_cells_executed_in_this_child',0),
            completed_new_range_cells=len(result.get('new_one_column_rows',[])),
            complete_all_one_column_cells_computed=result.get('complete_all_one_column_cells_computed',False),
            full_original_native_retained=True,complete_finite193_response_error_proved=False,
            complete_infinite_inverse_proved=False,unknown_high_input_feedback_still_required=True)
        if 'range' in result:summary['range']=result['range']
        if 'assignments' in result:
            summary['assignments']=[dict(first=r['first'],end=r['end'],requested_new_cells=len(r['actual_new_cells']))
                for r in result['assignments']]
        for key in ('complete_w0_physical_cap_error','complete_w0_moving_cap_error',
            'retained_endpoint_and_bridge_budget_without_body_terms'):
            if key in result:summary[key]=result[key]['upper']
        for key in ('original_actual_fourteen_physical_error_contributions','complete_fourteen_physical_error_contributions'):
            if key in result:summary[key]={k:v['upper'] for k,v in result[key].items()}
        boundary=result.get('same_Z_boundary',result.get('same_Z_boundary_from_completed_v3'))
        if boundary:
            summary['same_Z_source_bounds']={k:v['upper'] for k,v in boundary['source_bounds'].items()}
            for key in ('whole_body_Z_minus_raw_pair_A0','nominal_odd_map_Frobenius_gain',
                'nominal_mean_map_exact_row_gain','complete_Z_even_input_L2','complete_Z_even_minus_w0_L2',
                'original_complete_moving_error_operator_norm','complete_w0_moving_cap_error',
                'complete_Z_moving_cap_error','nominal_Z_odd_L2','nominal_Z_mean_absolute'):
                summary[key]=boundary[key]['upper']
            summary['boundary_source_convention']=boundary['boundary_source_convention']
            summary['original_high_output_norm_contract']=boundary['original_high_output_norm_contract']
        small(self.evidence/('complete-cut-Z-'+self.args.phase+'-summary.json'),summary)
        self.state.update(complete=True,complete_native_sha256=digest(native),
            actual_scientific_gates=len(result['gates']),
            actual_new_one_column_cells_in_this_child=result.get('new_one_column_cells_executed_in_this_child',0),
            complete_all_one_column_cells_computed=result.get('complete_all_one_column_cells_computed',False),
            actual_new_summary_bytes=(self.evidence/('complete-cut-Z-'+self.args.phase+'-summary.json')).stat().st_size)
        if boundary:self.state['complete_same_Z_source_bounds']=boundary['source_bounds']


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('manifest','rules','work','artifact-dir','cap-artifact','cap-cut-artifact','boundary-artifact','pilot-artifact'):
        p.add_argument('--'+name,type=Path,required=True)
    for name in ('prepared','plan-artifact','range-artifacts'):p.add_argument('--'+name,type=Path)
    for name in ('manifest-sha','rules-sha','driver-sha'):p.add_argument('--'+name,required=True)
    p.add_argument('--phase',choices=('plan','range','finish'),required=True)
    p.add_argument('--first',type=int,default=0);p.add_argument('--end',type=int,default=0)
    p.add_argument('--workflow-run',type=int,required=True)
    p.add_argument('--compute-minutes',type=int,default=100);p.add_argument('--checkpoint-minutes',type=int,default=10)
    a=p.parse_args();a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    a.kind='complete-cut-direction-same-Z';a.mode='prepare';a.recovery_manifest=None;a.recovery_sha=None
    worker=CompleteCutZWorker(a)
    for sig in (signal.SIGTERM,signal.SIGINT):signal.signal(sig,lambda *_:setattr(worker,'interrupted',True))
    worker.run_cap()


if __name__=='__main__':main()
