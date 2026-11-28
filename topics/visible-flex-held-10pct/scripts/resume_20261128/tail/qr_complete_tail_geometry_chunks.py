#!/usr/bin/env python3
"""Export a real final physical-H QR tail in complete, bounded stage chunks.

The genuine QR/native4/chord3/eight-outer source gate runs first. The unchanged
v2 pipeline produces the new stage zero, complete global mean and spectrum.
Remaining original stage exports start in small chunks immediately; no prior
large-process failure is required or invented. Every preserved stage and
cross-chunk boundary is revalidated before the original complete merge/index
and original continuous certificate phases. All earlier scientific bytes
remain unchanged. A failed original numerical allocation remains failed.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
import copy
import fcntl
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
import time
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
ORIGINAL = SCRIPTS/'resume_20261126/seam_run_tail_geometry_v2.py'
ORIGINAL_SHA = 'c165678d912761163ef29cfca1eb9c4dfc4bbf3102de6a00b228ca537f727615'
sys.path[:0] = [str(HERE), str(ORIGINAL.parent)]
import geometry_disk_guard
import geometry_recursive_write_guard as recursive_guard
from qr_actual_coupled_prefix import accepted_coupled
from seam_tail_spectrum_v2 import validate_spectrum_container

COMMON = ('geometrySchema', 'spectrum', 'spectrumContract', 'input',
    'existingCheckpoint', 'finiteScope', 'degree', 'planarModes', 'heightModes',
    'physicalParameters', 'physicalStats', 'meanContract', 'sourceSHA256')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def read(path):
    return json.loads(Path(path).read_text())


def checked(value):
    path = Path(value['path']).resolve()
    if ref(path) != value:
        raise ValueError('Changed actual complete-tail evidence: '+str(path))
    return path


def process_identity(pid):
    try:
        root = Path('/proc')/str(pid)
        stat = (root/'stat').read_text().rsplit(')', 1)[1].split()
        return dict(pid=int(pid), start_ticks=int(stat[19]),
            command_sha256=hashlib.sha256((root/'cmdline').read_bytes()).hexdigest(),
            boot_id=Path('/proc/sys/kernel/random/boot_id').read_text().strip())
    except (OSError, ValueError, IndexError):
        return None


def no_live_child(state):
    for progress in state.get('progress', {}).values():
        identity = progress.get('actual_child_identity')
        if identity is not None and process_identity(identity['pid']) == identity:
            raise RuntimeError('An actual previously launched geometry child is still alive; do not duplicate it')


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def make_pipeline(original, source_contract, options):
    """Only resource dispatch and complete-stage composition are different."""
    Base = original.Pipeline

    class Chunked(Base):
        def __init__(self, args):
            super().__init__(args)
            no_live_child(self.state)
            previous = self.state.get('actual_QR_physical_height_source')
            if previous is not None and previous != source_contract:
                raise ValueError('Resume changed the complete final physical-H/source contract')
            self.state['actual_QR_physical_height_source'] = source_contract

        def run(self, phase, command, output, progress_path=None, kind=None):
            requested = list(map(str, command))
            actual = recursive_guard.wrapped(requested)
            old_popen, child = subprocess.Popen, None

            def popen(argv, *args, **kwargs):
                nonlocal child
                if list(map(str, argv)) != actual:
                    raise ValueError('The original pipeline launched an unexpected concurrent child')
                self.state['progress'][phase].update(
                    original_mathematical_command=requested,
                    actual_wrapped_command=actual, actual_child_identity=None,
                    actual_child_dispatch_observed=False,
                    actual_child_returncode_observed=None)
                self.save()
                child = old_popen(argv, *args, **kwargs)
                identity = process_identity(child.pid)
                if identity is None and child.poll() is None:
                    raise RuntimeError('Cannot bind a live geometry child to its process identity')
                self.state['progress'][phase].update(
                    original_mathematical_command=requested,
                    actual_wrapped_command=actual,
                    actual_child_identity=identity, actual_child_dispatch_observed=True,
                    actual_child_returncode_observed=None,
                    nested_python_write_guard=ref(Path(recursive_guard.__file__)),
                    node_write_guard=ref(HERE/'geometry_disk_guard.mjs'))
                self.save()
                return child

            subprocess.Popen = popen
            try:
                return super().run(phase, actual, output, progress_path, kind)
            finally:
                subprocess.Popen = old_popen
                if child is not None:
                    code = child.poll()
                    self.state['progress'][phase]['actual_child_returncode_observed'] = code
                    self.state['progress'][phase]['child_terminal_status_inferred'] = False
                    self.save()

        def remaining(self):
            cut = original.checked(self.cut['shared_R_manifest'])
            chain = original.checked(self.cut['mean_chain'])
            self.S = len(chain['mean_chain'])-1
            self.cut_manifest = cut
            if self.S < 2:
                raise ValueError('The original complete finite chain has no remaining stages')
            done = self.existing('remaining-export')
            if done is not None:
                self.remaining_manifest = done
                return
            entries, neighbors, repairs, components = {}, [], [], []
            previous = None
            template = None

            def take(path, terminal):
                nonlocal previous, template
                path = Path(path).resolve()
                if self.root not in path.parents:
                    raise ValueError('A chunk manifest is outside this actual field output')
                manifest = read(path)
                for key in COMMON:
                    if manifest[key] != cut[key]:
                        raise ValueError('A chunk changed the original field: '+key)
                status = manifest.get('status')
                code = terminal.get('actual_child_returncode_observed')
                if status not in ('running', 'selected_stages_share_one_literal_R_C2_definition'):
                    raise ValueError('The stored exporter manifest has no reusable complete stage inventory')
                if code == 0 and status != 'selected_stages_share_one_literal_R_C2_definition':
                    raise ValueError('A successful original child lacks its real common-jet completion')
                if not manifest.get('files'):
                    raise ValueError('No actual completed stage exists in this chunk')
                if template is None:
                    template = copy.deepcopy(manifest)
                component = dict(manifest=ref(path), original_manifest_status=status,
                    actual_child_returncode_observed=code,
                    original_child_claimed_complete=(code == 0),
                    terminal_status_inferred_from_absence=False,
                    complete_stage_count=len(manifest['files']))
                components.append(component)
                for entry in sorted(manifest['files'], key=lambda row:row['stage'], reverse=True):
                    stage = entry['stage']
                    expected = self.S-1 if previous is None else previous['stage']-1
                    if stage != expected or stage in entries or not 1 <= stage < self.S:
                        raise ValueError('A preserved chunk has a duplicate, gap or out-of-scope stage')
                    data = original.checked(entry)
                    validate_spectrum_container(data, cut['spectrum'], stage=True)
                    if (data['status'] != 'literal_R_stage_with_exact_common_boundary_two_jets'
                            or data['stage'] != stage or data['boundInput'] != cut['input']
                            or data['spectrumContract'] != cut['spectrumContract']
                            or data['sourceSHA256'] != cut['sourceSHA256']
                            or data['sharing']['mapHash'] != entry['mapHash']
                            or data['physicalParameters'] != cut['physicalParameters']):
                        raise ValueError('An actual stage lost its full original map/source identity')
                    for node in data['nodes']:
                        if (not math.isfinite(node['radiusJS'])
                                or not all(math.isfinite(v) for row in node['coefficients'] for v in row)):
                            raise ValueError('A stored complete finite-map node is not finite')
                    for number,node in ((stage+1,data['nodes'][0]), (stage,data['nodes'][-1])):
                        if [node['meanPerturbation'],node['meanBackground']] != chain['mean_chain'][number]:
                            raise ValueError('The original global mean was reset at a chunk boundary')
                    if previous is not None:
                        left, right = data['nodes'][0], previous['nodes'][-1]
                        if left['radiusJS'] != right['radiusJS'] or left['coefficients'] != right['coefficients']:
                            raise ValueError('The actual neighboring Cartesian two-jets differ')
                        neighbors.append(dict(outerStage=stage, innerStage=stage+1,
                            node=stage+1, exactSharedRadiusAndCartesianTwoJets=True))
                    entries[stage], previous = entry, data
                repairs.extend(manifest['interfaceRepairs'])

            # Durable original successful and interrupted children are distinct.
            # No returncode is guessed for an orphaned stored manifest.
            stored = []
            for phase, progress in self.state.get('progress', {}).items():
                if not phase.startswith('remaining-chunk-'):
                    continue
                command = progress.get('original_mathematical_command')
                if command is None:
                    raise ValueError('A preserved chunk lacks its exact original exporter command')
                if command.count('--outdir') != 1:
                    raise ValueError('A preserved chunk has an ambiguous output directory')
                path = Path(command[command.index('--outdir')+1])/'manifest.json'
                if path.is_file() and read(path).get('files'):
                    stored.append((max(row['stage'] for row in read(path)['files']), path, progress))
            stored.sort(reverse=True, key=lambda row:row[0])
            for _, path, progress in stored:
                take(path, progress)
            cut_entry = cut['files'][0]
            cut_data = original.checked(cut_entry)
            if cut_entry['stage'] != 0 or cut_data['stage'] != 0:
                raise ValueError('The stage-zero anchor is not the actual new cut stage')
            low = min(entries) if entries else self.S
            if set(entries) != set(range(low, self.S)):
                raise ValueError('Preserved complete stages are not the exact inner suffix')
            initial_count, size = len(entries), options.chunk_stages
            ordinal = 0
            while low > 1:
                ordinal += 1
                hi, lo = low-1, max(1,low-size)
                selected = list(range(hi,lo-1,-1))
                prep = self.directory('chunk-input')
                prep.mkdir()
                anchors = [dict(node=1, path=cut_entry['path'], endpoint='inner')]
                if entries:
                    anchors.append(dict(node=hi+1,path=entries[hi+1]['path'],endpoint='outer'))
                anchor_path = prep/'actual-common-node-anchors.json'
                original.save(anchor_path, dict(reuse_stages={}, node_anchors=anchors))
                self.state['remaining_anchor'] = dict(original_stage0=cut_entry,
                    anchors=ref(anchor_path), map_hash_unchanged=cut_data['sharing']['mapHash'],
                    original_stage0_bytes_preserved=True, old_other_field_anchor_used=False,
                    additional_actual_inner_suffix_anchor=bool(entries))
                # Each invocation gets a new phase key, so even an interrupted
                # earlier partial manifest remains visible to the next resume.
                phase = 'remaining-chunk-'+str(len(stored)+ordinal).zfill(4)
                while phase in self.state['progress']:
                    ordinal += 1
                    phase = 'remaining-chunk-'+str(len(stored)+ordinal).zfill(4)
                directory = self.directory(phase)
                command = [self.args.node, str(ORIGINAL.parent/'seam_export_shared_r_tail_v2.mjs'),
                    '--input', self.cut['mean_chain']['path'], '--outdir', str(directory),
                    '--stages', ','.join(map(str,selected)), '--anchors', str(anchor_path),
                    '--spectrum-contract', self.cut['spectrum_contract']['path'],
                    '--difference-step', str(self.args.difference_step)]
                failure = None
                try:
                    actual = self.run(phase, command, directory/'manifest.json',
                                      directory/'manifest.json', 'export')
                except RuntimeError as error:
                    code = self.state['progress'][phase].get('actual_child_returncode_observed')
                    if type(code) is not int or not (code < 0 or code >= 128):
                        raise
                    failure = str(error)
                    if not (directory/'manifest.json').is_file():
                        raise
                    actual = read(directory/'manifest.json')
                observed = [row['stage'] for row in actual.get('files', [])]
                if observed != selected[:len(observed)] or (failure is None and observed != selected):
                    raise ValueError('The original chunk did not return its declared contiguous stage prefix')
                terminal = dict(source=ref(__file__), manifest=ref(directory/'manifest.json'),
                    actual_child_returncode_observed=self.state['progress'][phase].get('actual_child_returncode_observed'),
                    actual_stages=observed, original_error=failure,
                    mathematical_failure_inferred_from_signal=False,
                    cumulative_child_maxrss_KiB=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
                terminal_path = directory/'actual-chunk-terminal.json'
                original.save(terminal_path, terminal)
                if observed:
                    take(directory/'manifest.json', terminal)
                if failure is not None:
                    if size == 1 and not observed:
                        raise RuntimeError('One original stage was resource-interrupted; all earlier stages are preserved')
                    size = max(1,size//2)
                low = min(entries) if entries else self.S
                self.state['remaining_chunk_progress'] = dict(complete_stored_stages=len(entries),
                    next_stage=low-1, inherited_actual_stages=initial_count,
                    recomputed_stored_stages=0, chunk_size=size,
                    last_actual_terminal=ref(terminal_path))
                self.save()
            if set(entries) != set(range(1,self.S)) or len(neighbors) != self.S-2:
                raise ValueError('The actual remaining stage/adjacency coverage is incomplete')
            merged = copy.deepcopy(template)
            merged.update(status='selected_stages_share_one_literal_R_C2_definition',
                selectedStages=list(range(self.S-1,0,-1)),
                files=[entries[j] for j in range(self.S-1,0,-1)],
                interfaceRepairs=repairs, exactAdjacentCommonNodeChecks=neighbors,
                assemblies=len(components), aggregationSource=ref(__file__),
                actualComponentManifests=components,
                original_partial_child_claimed_complete=False,
                construction='Original complete-spectrum stage files in bounded chunks with the same unreset global mean and exact successive real boundary two-jet anchors.')
            directory = self.directory('remaining-merged-manifest')
            directory.mkdir()
            path = directory/'manifest.json'
            original.save(path, merged)
            self.state['completed']['remaining-export'] = ref(path)
            self.remaining_manifest = merged
            self.save()

        def merge_maps(self):
            super().merge_maps()
            # Preserve the original merger's complete bundle bytes and expose
            # the additional genuine chunk anchors through a bound sidecar.
            path = self.root/'complete-bundle-chunk-assembly.json'
            value = dict(source=ref(__file__), original_merger=ref(ORIGINAL),
                complete_bundle=self.state['completed']['complete-map'],
                full_source_contract=source_contract,
                stage0_bundle=self.state['completed']['stage0-export'],
                remaining_manifest=self.state['completed']['remaining-export'],
                actual_chunk_components=self.remaining_manifest['actualComponentManifests'],
                stage0_bytes_and_certificate_unchanged=True,
                all_original_mean_spectrum_and_adjacent_two_jets_retained=True,
                original_bundle_construction_text_is_legacy=True,
                actual_anchor_contract='The actual stage-zero inner node plus each completed inner chunk outer node; every adjacent literal two-jet is checked. No other field is used.',
                old_other_field_certificates_reused=False)
            if path.is_file() and read(path) != value:
                raise ValueError('The complete bundle assembly sidecar changed')
            if not path.is_file():
                original.save(path,value)
            self.state['actual_chunk_assembly'] = ref(path)
            self.save()

    return Chunked


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('source-run', 'coupling-summary', 'outdir'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--background-summary', type=Path)
    parser.add_argument('--phase', choices=('stage0', 'all'), default='all')
    parser.add_argument('--resume', action='store_true')
    parser.add_argument('--chunk-stages', type=int, default=8)
    parser.add_argument('--node-heap-mib', type=int, default=512)
    parser.add_argument('--disk-reserve-mib', type=int, default=128)
    parser.add_argument('--difference-step', type=float, default=.00005)
    parser.add_argument('--quadratic-mode-cutoff', type=int, default=12)
    parser.add_argument('--node', default='node')
    args = parser.parse_args()
    if (not 1 <= args.chunk_stages <= 16 or args.node_heap_mib < 256
            or args.disk_reserve_mib < 128 or args.quadratic_mode_cutoff < 0
            or not math.isfinite(args.difference_step) or args.difference_step <= 0):
        raise ValueError('Retain complete small chunks, at least 128MiB disk reserve and valid original settings')
    if sha(ORIGINAL) != ORIGINAL_SHA:
        raise ValueError('The reviewed original complete-tail pipeline changed')
    run, summary = args.source_run.resolve(), args.coupling_summary.resolve()
    record, physical, binding, provenance = accepted_coupled(run, summary)
    del physical
    if run != Path(read(summary)['result']['run']).resolve():
        raise ValueError('The input is not the actual final physical-height source')
    argv = record['command']
    if argv.count('--port') != 1:
        raise ValueError('The actual complete source has no unique original port')
    port = Path(argv[argv.index('--port')+1]).resolve()
    native_manifest = read(checked(binding['native_manifest']))
    source_topic = Path(native_manifest['source_topic']).resolve()
    native_runs = summary.parent/'native-runs'
    if not native_runs.is_dir():
        raise ValueError('The genuine final QR source native record directory is missing')
    original = module('_qr_actual_original_tail_geometry_pipeline', ORIGINAL)
    source_contract = dict(source=ref(__file__), original_pipeline=ref(ORIGINAL),
        actual_source_kind=provenance['source_kind'], accepted_source_gate=provenance,
        accepted_final_physical_run=ref(run), coupling_summary=ref(summary),
        physical=ref(run.parent/'physical.npz'), final_physical_packet=binding['packet'],
        final_physical_height_binding=read(summary)['result']['full_height_binding'],
        raw_height_used_as_definition=False, source_port=ref(port),
        native_manifest=binding['native_manifest'], native_record_dir=str(native_runs),
        old_1152_stage_map_or_certificate_reused=False,
        original_mathematical_sources=original.source_refs())
    inherited = SimpleNamespace(tail_response=checked(binding['packet']), source_port=port,
        source_topic=source_topic, height_reference=checked(source_contract['final_physical_height_binding']),
        height_reference_key='candidate_H', warm_factor=1., height_arithmetic='numpy',
        native_record=None, native_record_dir=native_runs, outdir=args.outdir.resolve(),
        phase=args.phase, resume=args.resume, background_summary=args.background_summary,
        degree=None, difference_step=args.difference_step,
        quadratic_mode_cutoff=args.quadratic_mode_cutoff, node=args.node)
    Pipeline = make_pipeline(original, source_contract, args)
    pipeline = Pipeline(inherited)
    lock = (pipeline.root/'geometry-owner.lock').open('a+')
    try:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        no_live_child(pipeline.state)
        os.environ['HELD10_GEOMETRY_DISK_ROOT'] = str(pipeline.root)
        os.environ['HELD10_GEOMETRY_DISK_FLOOR'] = str(args.disk_reserve_mib*1024**2)
        js_guard = HERE/'geometry_disk_guard.mjs'
        os.environ['NODE_OPTIONS'] = ('--max-old-space-size='+str(args.node_heap_mib)+
                                     ' --import='+str(js_guard))
        guard = geometry_disk_guard.install()
        invocation = pipeline.directory('bounded-chunk-invocation')
        invocation.mkdir()
        execution = dict(source=ref(__file__), command=[sys.executable,*sys.argv],
            original_pipeline=ref(ORIGINAL), complete_source_contract=source_contract,
            recursive_python_guard=ref(Path(recursive_guard.__file__)),
            original_python_guard=ref(Path(geometry_disk_guard.__file__)),
            original_node_guard=ref(js_guard), disk_guard=guard,
            node_options=os.environ['NODE_OPTIONS'], chunk_stages=args.chunk_stages,
            source_gate_checked_before_any_export=True,
            original_native_or_BVP_solves_executed=False,
            previous_large_export_failure_required=False,
            original_complete_mean_spectrum_and_certification_gates_changed=False)
        original.save(invocation/'execution.json', execution)
        pipeline.state['current_chunk_execution'] = ref(invocation/'execution.json')
        pipeline.save()
        return pipeline.execute()
    finally:
        lock.close()


if __name__ == '__main__':
    sys.exit(main())
