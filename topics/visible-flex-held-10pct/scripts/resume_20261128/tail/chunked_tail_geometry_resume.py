#!/usr/bin/env python3
"""Retain real exported stages and continue the unchanged exporter in chunks.

Every chunk uses the same original full mean chain, spectrum and accepted
state. Its inner node is copied from the previous real outer endpoint; the
original stage-zero inner node remains the cut anchor. All adjacent literal
Cartesian two-jets are checked before making the complete original bundle.
No partial child is described as a successful full child invocation.
"""
import argparse
import copy
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import re
import resource
import sys
import time

import geometry_disk_guard


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def read(path):
    return json.loads(Path(path).read_text())


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ('stage0-resource-record', 'failed-summary', 'outdir'):
        ap.add_argument('--'+name, type=Path, required=True)
    ap.add_argument('--chunk-stages', type=int, default=16)
    ap.add_argument('--disk-reserve-mib', type=int, default=128)
    ap.add_argument('--node-heap-mib', type=int, default=512)
    a = ap.parse_args()
    if not 1 <= a.chunk_stages <= 16 or a.node_heap_mib < 256:
        raise ValueError('Use small complete-stage chunks with a positive Node heap')
    resource_path, failed_path, out = map(lambda p:p.resolve(),
        (a.stage0_resource_record, a.failed_summary, a.outdir))
    resource, failed = read(resource_path), read(failed_path)
    original, prior = Path(resource['geometry_entry']['path']), Path(resource['actual_geometry_summary']['path'])
    if (resource.get('returncode') != 0 or not resource.get('full_spectrum_preserved')
            or ref(original) != resource['geometry_entry'] or ref(prior) != resource['actual_geometry_summary']
            or read(prior).get('status') != 'actual_stage0_geometry_ready'
            or failed.get('status') != 'actual_tail_geometry_execution_failed'
            or 'exit -9;' not in failed.get('error', '')):
        raise ValueError('Require the genuine stage0 and recorded original engineering exit')
    old_command = failed['progress']['remaining-export']['command']
    old_manifest_path = Path(old_command[old_command.index('--outdir')+1])/'manifest.json'
    old_manifest = read(old_manifest_path)
    if old_manifest.get('status') != 'running' or not old_manifest.get('files'):
        raise ValueError('The genuine killed child has no retained partial stage inventory')
    if out.exists() or out.parent != prior.parent.parent:
        raise ValueError('Use a new sibling continuation root')
    out.mkdir(); (out/'logs').mkdir(); (out/'steps').mkdir()
    os.environ['HELD10_GEOMETRY_DISK_ROOT'] = str(out)
    os.environ['HELD10_GEOMETRY_DISK_FLOOR'] = str(a.disk_reserve_mib*1024**2)
    os.environ['NODE_OPTIONS'] = '--max-old-space-size='+str(a.node_heap_mib)
    guard = geometry_disk_guard.install()
    for name in ('summary.json', 'inherited-stage0-summary.json'):
        (out/name).write_bytes(prior.read_bytes())
    here = Path(__file__).resolve().parent
    py_guard, js_guard = here/'geometry_disk_guard.py', here/'geometry_disk_guard.mjs'
    argv = list(resource['actual_command'][2:])
    for flag, value in (('--outdir', str(out)), ('--phase', 'all')):
        if argv.count(flag) != 1:
            raise ValueError('Ambiguous original command option')
        argv[argv.index(flag)+1] = value
    argv.append('--resume')
    execution = dict(source=ref(__file__), original_pipeline=ref(original),
        stage0_resource_record=ref(resource_path), original_stage0_summary=ref(prior),
        inherited_snapshot=ref(out/'inherited-stage0-summary.json'),
        original_failed_summary=ref(failed_path), actual_partial_manifest=ref(old_manifest_path),
        python_guard=ref(py_guard), node_guard=ref(js_guard), guard=guard,
        chunk_stages=a.chunk_stages, node_heap_mib=a.node_heap_mib,
        complete_original_continuation_argv=[sys.executable, str(original), *argv],
        equations_or_spectrum_changed=False, stage0_or_registered_stages_recomputed=False)
    execution_path=out/'chunk-execution.json'
    execution_path.write_text(json.dumps(execution, indent=2)+'\n')
    sys.path.insert(0, str(original.parent))
    spec=importlib.util.spec_from_file_location('_chunked_original_geometry_pipeline', original)
    pipeline=importlib.util.module_from_spec(spec);sys.modules[spec.name]=pipeline;spec.loader.exec_module(pipeline)
    Original=pipeline.Pipeline
    common=('geometrySchema','spectrum','spectrumContract','input','existingCheckpoint','finiteScope',
            'degree','planarModes','heightModes','physicalParameters','physicalStats','meanContract','sourceSHA256')

    class Chunked(Original):
        def __init__(self, args):
            super().__init__(args)
            self.state['chunk_execution']=ref(execution_path)
        def run(self, phase, command, *args, **kwargs):
            if Path(command[1]).suffix=='.mjs':
                command=[command[0], '--import', str(js_guard), *command[1:]]
            elif Path(command[1]).suffix=='.py':
                command=[command[0], str(py_guard), '--target', *command[1:]]
            else:
                raise ValueError('Unexpected original child command')
            return super().run(phase, command, *args, **kwargs)
        def remaining(self):
            cut=pipeline.checked(self.cut['shared_R_manifest'])
            chain=pipeline.checked(self.cut['mean_chain'])
            self.S=len(chain['mean_chain'])-1;self.cut_manifest=cut
            for name, expected in old_manifest['sourceSHA256'].items():
                if ref(name)['sha256']!=expected:
                    raise ValueError('The original actual geometry producer changed: '+name)
            for key in common:
                if old_manifest[key]!=cut[key]:
                    raise ValueError('Partial and stage0 definitions differ: '+key)
            entries={}; repairs=[]; components=[]; adjacent=[]
            previous=None
            def take(manifest, manifest_path, original_status, error=None):
                nonlocal previous
                for key in common:
                    if manifest[key]!=cut[key]:
                        raise ValueError('A chunk changed its field: '+key)
                component=dict(manifest=ref(manifest_path), actual_original_status=original_status,
                               registered_stage_count=len(manifest['files']))
                if error is not None:
                    component['actual_child_failure']=str(error)
                components.append(component)
                for entry in sorted(manifest['files'], key=lambda r:r['stage'], reverse=True):
                    index=entry['stage']
                    if index in entries or not 1<=index<self.S:
                        raise ValueError('A retained stage was duplicated or lies outside the remaining chain')
                    data=pipeline.checked(entry)
                    from seam_tail_spectrum_v2 import validate_spectrum_container
                    validate_spectrum_container(data, cut['spectrum'], stage=True)
                    if (data['status']!='literal_R_stage_with_exact_common_boundary_two_jets'
                            or data['stage']!=index or data['boundInput']!=cut['input']
                            or data['spectrumContract']!=cut['spectrumContract']
                            or data['sourceSHA256']!=cut['sourceSHA256']
                            or data['sharing']['mapHash']!=entry['mapHash']):
                        raise ValueError('A real stored stage lacks the exact original map identity')
                    for node in data['nodes']:
                        if not math.isfinite(node['radiusJS']) or not all(math.isfinite(v) for row in node['coefficients'] for v in row):
                            raise ValueError('A real stored finite map is not finite')
                    for n,node in ((index+1,data['nodes'][0]),(index,data['nodes'][-1])):
                        if [node['meanPerturbation'],node['meanBackground']]!=chain['mean_chain'][n]:
                            raise ValueError('A stored node changed the complete cumulative mean')
                    if previous is not None:
                        if previous['stage']!=index+1:
                            raise ValueError('A stage gap would change the full finite chain')
                        left,right=data['nodes'][0],previous['nodes'][-1]
                        if left['radiusJS']!=right['radiusJS'] or left['coefficients']!=right['coefficients']:
                            raise ValueError('Actual adjacent Cartesian two-jets are not exactly common')
                        adjacent.append(dict(outerStage=index,innerStage=index+1,node=index+1,
                                             exactSharedRadiusAndCartesianTwoJets=True))
                    entries[index]=entry;previous=data
                repairs.extend(manifest['interfaceRepairs'])
            take(old_manifest,old_manifest_path,'running_before_recorded_child_exit_minus9')
            low=min(entries)
            if set(entries)!=set(range(low,self.S)):
                raise ValueError('The preserved actual inventory is not the complete inner suffix')
            cut_entry=cut['files'][0]
            cut_data=pipeline.checked(cut_entry)
            initial_anchors=out/'preserved-actual-node-anchors.json'
            pipeline.save(initial_anchors,dict(reuse_stages={},node_anchors=[
                dict(node=1,path=cut_entry['path'],endpoint='inner'),
                dict(node=low,path=entries[low]['path'],endpoint='outer')]))
            self.state['remaining_anchor']=dict(original_stage0=cut_entry,anchors=ref(initial_anchors),
                map_hash_unchanged=cut_data['sharing']['mapHash'],
                original_stage0_bytes_preserved=True,old_other_field_anchor_used=False)
            recovery=out/'preserved-partial-stage-inventory.json'
            recovery.write_text(json.dumps(dict(source=ref(__file__),original_manifest=ref(old_manifest_path),
                original_child_returncode=-9,files=[entries[j] for j in sorted(entries,reverse=True)],
                exact_shared_neighbor_checks=adjacent,all_recorded_stage_bytes_preserved=True),indent=2)+'\n')
            self.state['preserved_partial_inventory']=ref(recovery)
            self.state['remaining_chunk_progress']=dict(complete_stored_stages=len(entries),
                next_stage=low-1,recomputed_old_stages=0,chunk_size=a.chunk_stages)
            self.save()
            counter,size=0,a.chunk_stages
            while low>1:
                counter+=1;hi=low-1;lo=max(1,hi-size+1);selected=list(range(hi,lo-1,-1))
                if counter==1:
                    anchors=initial_anchors
                else:
                    prep=self.directory('chunk-input');prep.mkdir()
                    anchors=prep/'actual-common-node-anchors.json'
                    pipeline.save(anchors,dict(reuse_stages={},node_anchors=[
                        dict(node=1,path=cut_entry['path'],endpoint='inner'),
                        dict(node=hi+1,path=entries[hi+1]['path'],endpoint='outer')]))
                phase='remaining-chunk-'+str(counter).zfill(4)
                directory=self.directory(phase)
                command=[self.args.node,str(original.parent/'seam_export_shared_r_tail_v2.mjs'),
                    '--input',self.cut['mean_chain']['path'],'--outdir',str(directory),
                    '--stages',','.join(map(str,selected)),'--anchors',str(anchors),
                    '--spectrum-contract',self.cut['spectrum_contract']['path'],
                    '--difference-step',str(self.args.difference_step)]
                error=None
                try:
                    actual=self.run(phase,command,directory/'manifest.json',directory/'manifest.json','export')
                except RuntimeError as exc:
                    if 'exit -9;' not in str(exc):
                        raise
                    error=exc
                    if not (directory/'manifest.json').exists():
                        raise
                    actual=read(directory/'manifest.json')
                    if actual.get('status')!='running':
                        raise
                observed=[r['stage'] for r in actual['files']]
                if observed!=selected[:len(observed)] or (error is None and observed!=selected):
                    raise ValueError('Actual original chunk did not return the declared contiguous stages')
                if error is None and actual['status']!='selected_stages_share_one_literal_R_C2_definition':
                    raise ValueError('The original complete chunk did not check its own common jets')
                terminal=directory/'actual-chunk-terminal.json'
                pipeline.save(terminal,dict(source=ref(__file__),manifest=ref(directory/'manifest.json'),
                    original_child_returncode=0 if error is None else -9,actual_stages=observed,
                    original_error=None if error is None else str(error),mathematical_failure_claimed=False,
                    observed_cumulative_child_maxrss_KiB=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss))
                take(actual,directory/'manifest.json',actual['status'],error)
                if error is not None:
                    if size==1 and not observed:
                        raise RuntimeError('Even a single original stage was killed; preserved all earlier stages')
                    size=max(1,size//2)
                low=min(entries)
                self.state['remaining_chunk_progress']=dict(complete_stored_stages=len(entries),
                    next_stage=low-1,recomputed_old_stages=0,chunk_size=size,last_terminal=ref(terminal))
                self.save()
            if set(entries)!=set(range(1,self.S)) or len(adjacent)!=self.S-2:
                raise ValueError('The actual complete remaining stage/neighbor set is incomplete')
            merged=copy.deepcopy(old_manifest)
            merged.update(status='selected_stages_share_one_literal_R_C2_definition',
                selectedStages=list(range(self.S-1,0,-1)),files=[entries[j] for j in range(self.S-1,0,-1)],
                interfaceRepairs=repairs,exactAdjacentCommonNodeChecks=adjacent,
                assemblies=len(components),aggregationSource=ref(__file__),
                actualComponentManifests=components,preservedOriginalPartialInventory=ref(recovery),
                originalPartialChildClaimedComplete=False,
                construction='Exact original full-spectrum stage files, retained partial suffix and new bounded chunks; every common node checked literally.')
            target=self.directory('remaining-merged-manifest');target.mkdir()
            path=target/'manifest.json';pipeline.save(path,merged)
            self.state['completed']['remaining-export']=ref(path)
            self.remaining_manifest=merged
            self.save()

    pipeline.Pipeline=Chunked
    sys.argv=[str(original),*argv]
    pipeline.main()


if __name__=='__main__':
    main()
