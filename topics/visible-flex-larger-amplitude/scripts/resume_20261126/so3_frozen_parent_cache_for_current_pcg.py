#!/usr/bin/env python3
"""Explicit original/cached/SOC/current-PCG producers for the same immutable T0 cache.

The complete 234ac operator and d3f25 parent provider are not modified.  This
module validates a completed producer, installs only identified cache entries
in its existing plain dictionary, and records a new runner-only manifest.
Legacy reports did NOT commit cache checksums.  Their first adoption is a new
explicit numerical input binding, never a retroactive checksum assertion.
Missing or unidentified entries are left to the original actual provider.
"""
import ast
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import shutil
import sys
import time

import numpy as np


SCHEMA = 'same-actual-frozen-parent-numerical-meridian-cache-v1'
CONSUMER_SCHEMA = 'complete-normalized-parent-cached-current-eight-column-PCG-SOC-v1'
CONSUMER_BASENAME = 'fullclosed_so3_cached_current_pcg_soc.py'
OPERATOR_SHA = '234ac8db3ebc34fc1c146c56bec810f1c777cf6e2689858c7234124eece7ea42'
PROVIDER_SHA = 'd3f25bb74e179865b20f7759bc1ee8dcdf2c2771f062ac096ee4d5398a8be4b9'
BINDER_SHA = '9ca39afd9f840ba89fbb75d7365220c2d85d26ddb26b2d66b6c55e611313fd55'
MANIFEST_BASENAME = 'reference-meridian-cache-manifest.json'
CACHE_BASENAME = 'frozen-parent-meridian-cache'
KEYS = ('T0', 'T0_s', 'T0_phi', 'T0_phiphi')
LEGACY_PRODUCERS = {
    'complete-normalized-parent-cached-interior-separated-SOC-v1':
        ('fullclosed_so3_cached_interior_separation_soc.py', '892f349b140f9a77fde37fc490d7cbb078cfdb21f8b31b7743e50ec6cf5712a8'),
    'complete-actual-fixed-deep-parent-cached-interior-restore-QP-v1':
        ('fullclosed_so3_cached_interior_restore_qp.py', '174b79f4b2393a719e7ddee70f59fe5c500e89d41e8d181497f1b4329f8b015f'),
    'complete-actual-fixed-deep-parent-closed-so3-meridian-QP-v1':
        ('fullclosed_so3_actual_profile_qp.py', '7e9095b3a765f064baae9a36e9593667d5c469686232b6095065e0c3cf22c55b'),
    'complete-actual-fixed-deep-parent-closed-so3-interior-restore-QP-v1':
        ('fullclosed_so3_actual_profile_interior_restore_qp.py', '0f542de9ab1f91f5ca27a0efe315b0ee96beddd3e3972ba12fbc5140221623a6'),
}


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Read or adopt numerical parent caches only in public repository Actions')


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def array_sha(value):
    value = np.ascontiguousarray(value)
    h = hashlib.sha256(str(value.dtype).encode())
    h.update(json.dumps(list(value.shape)).encode())
    h.update(value.tobytes())
    return h.hexdigest()


def record(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)


def literal(path, name):
    matches = [node.value for node in ast.parse(Path(path).read_text()).body
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name)
        and t.id == name for t in node.targets)]
    if len(matches) != 1:
        raise ValueError('Need one complete literal source declaration '+name)
    return ast.literal_eval(matches[0])


def portable(value):
    """Discard location strings only; preserve every exact mathematical/data key."""
    if isinstance(value, dict):
        return {key: portable(item) for key, item in value.items()
            if key not in ('path', 'repo_relative_path')}
    if isinstance(value, list):
        return [portable(item) for item in value]
    return value


def producer_report(repo, path, consumer_source):
    """Pure byte/source attribution shared by restart and cache adoption."""
    repo, path, consumer_source = Path(repo).resolve(), Path(path).resolve(), Path(consumer_source).resolve()
    topic = repo/'topics/visible-flex-larger-amplitude'
    source_dir = topic/'scripts/resume_20261126'
    report = json.loads(path.read_text())
    if report.get('complete') is not True:
        raise ValueError('A cache or restart donor must be an actually completed budget')
    schema, source_sha = report.get('schema'), report.get('source_sha256')
    if schema in LEGACY_PRODUCERS:
        basename, expected = LEGACY_PRODUCERS[schema]
        source = source_dir/basename
    elif schema == CONSUMER_SCHEMA:
        if consumer_source.name != CONSUMER_BASENAME or consumer_source.parent != source_dir:
            raise ValueError('The new cache-aware producer must be its explicit complete source')
        source, expected = consumer_source, sha(consumer_source)
    else:
        raise ValueError('Unknown complete producer schema; no label substitution')
    if source_sha != expected or sha(source) != expected or literal(source, 'SCHEMA') != schema:
        raise ValueError('The actual full producer source/schema pair changed')
    pins = literal(source, 'SOURCE_PINS')
    if report.get('source_sha256_by_role') != {role: value[1] for role, value in pins.items()}:
        raise ValueError('Retain the producer complete exact source registry')
    for role, (relative, expected_sha) in pins.items():
        if sha(topic/relative) != expected_sha:
            raise ValueError('Changed actual producer dependency '+role)
    if (pins['meridian'][1] != OPERATOR_SHA or pins['parent_jet'][1] != PROVIDER_SHA
            or pins['actual_parent_binding'][1] != BINDER_SHA):
        raise ValueError('This cache belongs only to the unchanged 234ac/d3f25 representation')
    binder_path = topic/pins['actual_parent_binding'][0]
    name = '_frozen_meridian_cache_actual_parent_binding'
    spec = importlib.util.spec_from_file_location(name, binder_path)
    binder = importlib.util.module_from_spec(spec)
    sys.modules[name] = binder
    spec.loader.exec_module(binder)
    fixed_profile = binder.verify_saved_binding(report, expected_binding_source_sha256=BINDER_SHA)
    model = report.get('representation')
    if (not isinstance(model, dict) or canonical(model) != report.get('model_identity_sha256')
            or model.get('source_sha256') != OPERATOR_SHA
            or model.get('parent_meridian_kernel_sha256') != PROVIDER_SHA
            or model.get('fixed_scalar_metric_identity_sha256') != fixed_profile
            or model.get('frozen_parent_bundle_sha256') != report.get('bundle_sha256')):
        raise ValueError('The producer complete frozen field model differs from its input binding')
    return report, dict(report=record(path), producer=record(source),
        schema=schema, fixed_scalar_metric_identity_sha256=fixed_profile,
        complete_source_registry_verified=True)


def _query_record(cells, local):
    cells, local = np.asarray(cells), np.asarray(local)
    return dict(rows=len(cells), cells_sha256=array_sha(cells), local_sha256=array_sha(local),
        cells_dtype=str(cells.dtype), local_dtype=str(local.dtype),
        addresses='complete cell integer and literal binary64 u arrays, in original order')


def _key(label, phi_hex):
    if label not in ('integration', 'grid') or not isinstance(phi_hex, (tuple, list)) or not phi_hex:
        raise ValueError('Only complete original integration/grid cache entries are reusable')
    values = [float.fromhex(value) for value in phi_hex]
    if any(not math.isfinite(value) or value.hex() != word for value, word in zip(values, phi_hex)):
        raise ValueError('A cache angle needs its complete canonical literal binary64 identity')
    return label, tuple(phi_hex)


def _filename(key):
    label, phi_hex = key
    return canonical(dict(label=label, phi=list(phi_hex)))+'.npz'


def _state(path):
    st = Path(path).stat()
    # A later hardlink/unlink changes ctime without modifying any data word.
    return (st.st_dev, st.st_ino, st.st_size, st.st_mtime_ns)


class FrozenParentCache:
    """Fill the original plain q._cache; never replace any operator method.

    The current field x, its derivative, objective, norm, constraints and true
    geometry remain the original complete source operations. A cache miss
    still calls the actual frozen parent evaluator. Full raw file inventories
    and literal queries are written only to this runner's new manifest.
    """

    def __init__(self, q, args, consumer_source, *, witnesses=(), radius_witnesses=()):
        require_actions()
        started = time.monotonic()
        self.q, self.args = q, args
        self.repo = Path(args.repo).resolve()
        self.consumer_source = Path(consumer_source).resolve()
        self.directory = Path(q.cache_directory).resolve()
        self.manifest_path = Path(args.outdir).resolve()/MANIFEST_BASENAME
        if (self.directory != Path(args.outdir).resolve()/CACHE_BASENAME
                or self.repo == self.directory or self.repo in self.directory.parents
                or self.manifest_path.exists() or type(q._cache) is not dict or q._cache):
            raise ValueError('Install into the untouched fresh original cache outside the repository')
        for name in ('_parent', '_parent_tensor', 'make_query', '_meridians', '_integrate',
                     'fields_torch', 'residual', 'jvp', 'vjp', 'grid_fields', 'point_fields', 'point_vjp'):
            if sha(getattr(q, name).__code__.co_filename) != OPERATOR_SHA:
                raise ValueError('Do not replace any original physical/cache method: '+name)
        if sha(q.parent_jet.evaluate.__code__.co_filename) != PROVIDER_SHA:
            raise ValueError('The real complete parent provider changed')
        if canonical(q.model) != q.identity or q.model.get('source_sha256') != OPERATOR_SHA:
            raise ValueError('Keep the exact original complete frozen field model')
        self.queries = {
            'integration': _query_record(q.integration_query['cells'], q.integration_query['local']),
            'grid': _query_record(q.grid_query['cells'], q.grid_query['local']),
        }
        self.binding = dict(schema='complete-frozen-parent-cache-query-binding-v1',
            operator_source_sha256=OPERATOR_SHA, parent_provider_source_sha256=PROVIDER_SHA,
            complete_field_model=q.model, model_identity_sha256=q.identity,
            complete_portable_parent_binding=portable(q.parent_jet.binding),
            original_parent_report_sha256=sha(args.parent_report),
            complete_input_sha256s=dict(parent_bundle=sha(args.parent_bundle),
                observation_carrier=sha(args.carrier), node_report=sha(args.node_report),
                scalar_input=sha(args.scalar_input)),
            full_N=q.full_N, quarter_N=q.N, P=q.P, J=q.J, M=q.M,
            mesh_sha256=array_sha(q.mesh), full_quarter_phi_sha256=array_sha(q.phi),
            integration_order=q.integration_order, gauss_u_sha256=array_sha(q.gauss_u),
            gauss_w_sha256=array_sha(q.gauss_w), queries=self.queries,
            returned_jets=list(KEYS), frame='world Cartesian', dtype='float64',
            current_free_state_not_part_of_T0_identity=True)
        self.binding_identity = canonical(self.binding)
        self.entries, self.states = {}, {}
        self.donor = None
        self.adopted_files = self.adopted_points = self.adopted_bytes = 0
        self.hardlinked_files = self.copied_files = 0
        self.missing_planned_files = self.unidentified_legacy_files = 0
        self.fresh_files = self.fresh_points = 0
        self.fresh_file_validation_seconds = self.final_audit_seconds = 0.
        self.legacy_adoption = False
        self.donor_norm_deviation = None
        if bool(args.reference_cache) != bool(args.reference_cache_report):
            raise ValueError('Cache adoption needs both the actual directory and its completed report')
        if args.reference_cache is not None:
            self._adopt(Path(args.reference_cache).resolve(),
                Path(args.reference_cache_report).resolve(), witnesses, radius_witnesses)
        self.setup_seconds = time.monotonic()-started

    def _validate_report(self, path):
        q, args = self.q, self.args
        report, provenance = producer_report(self.repo, path, self.consumer_source)
        metadata = report.get('latest_operator_metadata', {})
        if (report['representation'] != q.model or report['model_identity_sha256'] != q.identity
                or metadata.get('model') != q.model or metadata.get('model_identity_sha256') != q.identity
                or portable(metadata.get('frozen_parent_binding')) != portable(q.parent_jet.binding)
                or report.get('bundle_sha256') != self.binding['complete_input_sha256s']['parent_bundle']
                or report.get('original_parent_report', {}).get('sha256') != sha(args.parent_report)
                or report.get('observation_carrier_sha256') != sha(args.carrier)
                or report.get('exact_tail_node_report_sha256') != sha(args.node_report)
                or report.get('exact_tail_scalar_input_sha256') != sha(args.scalar_input)
                or report.get('N') != q.full_N or report.get('J') != q.J or report.get('M') != q.M
                or report.get('all_full_rows') != 3*q.P*q.full_N
                or report.get('working_evaluation', {}).get('integration_order') != q.integration_order):
            raise ValueError('Cache donor must retain the full same actual frozen parent, model and radial queries')
        if str(report.get('github_run_id')) != str(os.environ.get('GITHUB_RUN_ID')):
            raise ValueError('This first cache entry only reuses actual raw files retained on the same public run')
        final = Path(report['final_bundle']).resolve()
        if final != path.parent/'final.npz' or sha(final) != report['final_bundle_sha256']:
            raise ValueError('Bind the completed donor to its actual final bundle and original output directory')
        self.donor_norm_deviation = metadata.get('maximum_requested_parent_norm_deviation')
        if (self.donor_norm_deviation is not None and
                (not math.isfinite(float(self.donor_norm_deviation)) or self.donor_norm_deviation < 0)):
            raise ValueError('Malformed historical parent-normalization diagnostic')
        return report, provenance

    def _validate_file(self, path, key, *, expected=None):
        label, phi_hex = _key(*key)
        path = Path(path)
        if path.name != _filename(key) or path.is_symlink():
            raise ValueError('Use the complete original cache filename protocol, without symlinks')
        before = _state(path)
        file_sha = sha(path)
        shape = (self.queries[label]['rows'], len(phi_hex), 3)
        arrays = {}
        with np.load(path, allow_pickle=False) as data:
            if set(data.files) != set(KEYS) or len(data.files) != len(KEYS):
                raise ValueError('Keep all four complete original normalized parent jets')
            for name in KEYS:
                value = np.asarray(data[name])
                if value.shape != shape or value.dtype != np.dtype('float64') or not np.isfinite(value).all():
                    raise ValueError('Invalid complete original cache array '+name)
                arrays[name] = dict(shape=list(shape), dtype=str(value.dtype), sha256=array_sha(value))
        if _state(path) != before:
            raise ValueError('A donor cache changed while its complete bytes were being bound')
        answer = dict(label=label, phi_hex=list(phi_hex), filename=path.name,
            bytes=before[2], sha256=file_sha, query=self.queries[label],
            arrays=arrays, point_count=shape[0]*shape[1])
        if expected is not None:
            # Provenance fields may differ; every numerical/query/byte item must match.
            for name in answer:
                if expected.get(name) != answer[name]:
                    raise ValueError('Committed numerical cache entry differs: '+name)
        return answer

    def _install_file(self, source, key, *, expected=None, origin):
        source = Path(source)
        if not source.is_file():
            self.missing_planned_files += 1
            return
        entry = self._validate_file(source, key, expected=expected)
        target = self.directory/entry['filename']
        if target.exists() or key in self.q._cache:
            raise ValueError('Never replace an existing cache entry or ambiguous duplicate')
        try:
            os.link(source, target)
            transfer = 'hardlink of verified immutable retained bytes'
            self.hardlinked_files += 1
        except OSError:
            if target.exists():
                raise
            shutil.copyfile(source, target)
            transfer = 'complete byte copy after hardlink was unavailable'
            self.copied_files += 1
        if sha(target) != entry['sha256'] or sha(source) != entry['sha256']:
            raise ValueError('A cache changed during its explicit same-run adoption')
        entry['origin'] = origin
        entry['adoption_transfer'] = transfer
        self.entries[key] = entry
        self.states[key] = _state(target)
        # This is the ORIGINAL dictionary/value protocol used by 234ac.
        self.q._cache[key] = dict(cache_path=target)
        self.adopted_files += 1
        self.adopted_points += entry['point_count']
        self.adopted_bytes += entry['bytes']

    def _adopt(self, directory, report_path, witnesses, radius_witnesses):
        if directory != report_path.parent/CACHE_BASENAME or directory == self.directory:
            raise ValueError('Use the actual producer output cache directory, not an unrelated folder')
        if directory == self.repo or self.repo in directory.parents or not directory.is_dir():
            raise ValueError('The retained scientific cache must be outside Git on this runner')
        report, provenance = self._validate_report(report_path)
        self.donor = dict(provenance, cache_directory=str(directory),
            same_actual_public_run_verified=True)
        saved = report.get('reference_meridian_cache')
        if saved is not None:
            manifest_record = saved['manifest']
            manifest_path = Path(manifest_record['path']).resolve()
            if (manifest_path != report_path.parent/MANIFEST_BASENAME
                    or sha(manifest_path) != manifest_record['sha256']
                    or manifest_path.stat().st_size != manifest_record['bytes']):
                raise ValueError('Use the final complete producer committed cache manifest')
            manifest = json.loads(manifest_path.read_text())
            payload = {key: value for key, value in manifest.items() if key != 'manifest_identity_sha256'}
            expected_cache_source = report['source_sha256_by_role'].get('reference_cache')
            allowed_cache_sources = {'4e9ed6949bf42f8ef103b06d0e15dbfa1a8f7d21317a9492f71dca33195824cd',
                '50a9a4802fb23d01659de4a5ff2e1429f52837c59d6b4c563ae72f54836a4abe', sha(__file__)}
            if (manifest.get('schema') != SCHEMA or expected_cache_source not in allowed_cache_sources
                    or manifest.get('source_sha256') != expected_cache_source
                    or canonical(payload) != manifest.get('manifest_identity_sha256')
                    or manifest.get('binding') != self.binding
                    or manifest.get('binding_identity_sha256') != self.binding_identity
                    or manifest.get('producer_source_sha256') != report['source_sha256']
                    or manifest.get('completed_run_snapshot') is not True
                    or saved.get('binding_identity_sha256') != self.binding_identity):
                raise ValueError('A prior committed cache manifest belongs to different actual queries or sources')
            seen = set()
            for entry in manifest['entries']:
                key = _key(entry['label'], entry['phi_hex'])
                if key in seen:
                    raise ValueError('The complete saved cache manifest repeats an address')
                seen.add(key)
                self._install_file(directory/_filename(key), key, expected=entry,
                    origin='previous complete source-bound cache manifest')
            self.donor['manifest'] = dict(manifest_record)
            self.donor['cache_checksums_previously_committed_by_producer'] = True
        else:
            self.legacy_adoption = True
            working = report['working_evaluation']
            current_metadata = self.q.metadata()
            if (working.get('numpy_version') != np.__version__
                    or working.get('torch_version') != current_metadata['torch_version']
                    or working.get('torch_threads') != self.args.torch_threads
                    or working.get('angle_block') != self.q.angle_block):
                raise ValueError('First legacy adoption requires the unchanged same-run numerical query setup')
            planned = set()
            for begin in range(0, self.q.N, self.q.angle_block):
                phi = tuple(float(v).hex() for v in self.q.phi[begin:begin+self.q.angle_block])
                planned.add(('integration', phi))
                planned.add(('grid', phi))
            for location in (*witnesses, *radius_witnesses):
                value = float(location['phi'])
                if not math.isfinite(value):
                    raise ValueError('Use complete actual finite permanent angular addresses')
                planned.add(('integration', (value.hex(),)))
            for key in sorted(planned):
                self._install_file(directory/_filename(key), key,
                    origin='legacy raw words first bound by this explicit adoption')
            identified = {_filename(key) for key in planned}
            self.unidentified_legacy_files = sum(1 for path in directory.glob('*.npz')
                if path.name not in identified)
            self.donor.update(cache_checksums_previously_committed_by_producer=False,
                first_explicit_byte_binding_is_this_adoption=True,
                old_radial_query_hash_was_recorded=False,
                radial_query_attribution='unchanged 234ac/d3f25 complete model and four inputs; same live run, NumPy, Q and angle blocks; current literal arrays newly committed here',
                shape_alone_used_as_parent_identity=False)

    def snapshot(self, *, completed_run=False):
        """Capture only cache words already produced; this never calls F or J."""
        require_actions()
        started = time.monotonic()
        for raw_key, item in self.q._cache.items():
            key = _key(*raw_key)
            if set(item) != {'cache_path'}:
                raise ValueError('The original unchanged cache record protocol changed')
            path = Path(item['cache_path']).resolve()
            if path != self.directory/_filename(key):
                raise ValueError('Every current cache entry must remain inside its own output directory')
            if key in self.entries:
                if _state(path) != self.states[key]:
                    raise ValueError('An already frozen numerical cache entry was modified')
            else:
                entry = self._validate_file(path, key)
                entry['origin'] = 'fresh actual 234ac call to unchanged d3f25 parent provider'
                self.entries[key] = entry
                self.states[key] = _state(path)
                self.fresh_files += 1
                self.fresh_points += entry['point_count']
        self.fresh_file_validation_seconds += time.monotonic()-started
        if completed_run:
            audit = time.monotonic()
            for key, entry in self.entries.items():
                if sha(self.directory/entry['filename']) != entry['sha256']:
                    raise ValueError('An actual cache byte changed before the completed report')
            self.final_audit_seconds += time.monotonic()-audit
        payload = dict(schema=SCHEMA, source_sha256=sha(__file__),
            producer_source_sha256=sha(self.consumer_source),
            binding=self.binding, binding_identity_sha256=self.binding_identity,
            completed_run_snapshot=bool(completed_run), donor=self.donor,
            entries=[self.entries[key] for key in sorted(self.entries)],
            original_operator_methods_replaced=False, original_cache_protocol_unchanged=True,
            only_four_frozen_parent_jets_reused=True, current_field_or_derivatives_cached_as_T0=False,
            quadrature_normalization_or_rounding_errors_certified=False,
            cache_identity_is_a_numerical_input_binding_not_an_exact_T0_certificate=True)
        payload['manifest_identity_sha256'] = canonical(payload)
        temporary = self.manifest_path.with_suffix('.json.tmp')
        temporary.write_text(json.dumps(payload, indent=2, allow_nan=False)+'\n')
        os.replace(temporary, self.manifest_path)
        return dict(schema=SCHEMA, source_sha256=sha(__file__),
            binding_identity_sha256=self.binding_identity, manifest=record(self.manifest_path),
            manifest_identity_sha256=payload['manifest_identity_sha256'],
            completed_run_snapshot=bool(completed_run), cache_directory=str(self.directory),
            adoption_requested=self.args.reference_cache is not None,
            donor_report=None if self.donor is None else self.donor['report'],
            legacy_adoption_without_historical_checksums=self.legacy_adoption,
            adopted_files=self.adopted_files, adopted_points=self.adopted_points,
            adopted_bytes=self.adopted_bytes, hardlinked_files=self.hardlinked_files,
            copied_files=self.copied_files, missing_planned_files=self.missing_planned_files,
            unidentified_legacy_files_not_used=self.unidentified_legacy_files,
            fresh_files=self.fresh_files, fresh_points=self.fresh_points,
            complete_manifest_entries=len(self.entries), setup_seconds=self.setup_seconds,
            fresh_file_validation_seconds=self.fresh_file_validation_seconds,
            final_byte_audit_seconds=self.final_audit_seconds,
            original_parent_evaluation_counts_are_only_fresh_calls=True,
            cache_hit_count_instrumented=False,
            current_maximum_parent_norm_deviation_scope='fresh provider evaluations in this run only',
            donor_maximum_parent_norm_deviation=self.donor_norm_deviation,
            donor_norm_diagnostic_is_not_a_fresh_cache_array_read=True,
            operator_methods_replaced=False, unknown_entries_call_original_provider=True,
            no_metric_geometry_or_convergence_certificate_inherited=True)
