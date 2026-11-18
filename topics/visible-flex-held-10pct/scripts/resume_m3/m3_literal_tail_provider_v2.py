#!/usr/bin/env python3
"""Bind a native tail provider, including its two literal provenance markers.

This module reads identities only. It does not construct a core or evaluate a
flow. The historical V8 response remains a historical response; the new native
provider gets its own source map, manifest, executable/library fingerprints and
run directory. Physical/numerical configuration and the strict original gate
are retained. A provider binding is not a convergence or error certificate.
"""
import copy
import hashlib
import json
from pathlib import Path


NATIVE_NAMES = (
    '950f-tail-client-v3.py', '950f-tail-stage-port-v3.mjs',
    '950f-tail-stage-core.mjs', '950f-tail-stage-split.mjs',
    '950f-tail-subdivision.mjs', '950f-tail-warm-remesh.mjs',
    'closing_weighted_tail.mjs', 'closing_recalibrated_tail.mjs')
FIXED_SCOPE = dict(M=8, spacing=3, quadrature=128, steps=16,
                   projectionFloor=.05, orientation=1, cuspAwareFlow=True,
                   stageCount=1152)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def file_refs(value):
    if isinstance(value, dict):
        if isinstance(value.get('path'), str) and isinstance(value.get('sha256'), str):
            yield value
        for item in value.values():
            yield from file_refs(item)
    elif isinstance(value, list):
        for item in value:
            yield from file_refs(item)


def bind_provider(manifest_path, manifest_sha256, historical_native_sources, config):
    """Pin the announced M8/gcd-one native provider, without running it."""
    path = Path(manifest_path).resolve()
    if sha(path) != manifest_sha256:
        raise ValueError('The explicit native-provider manifest changed')
    manifest = json.loads(path.read_text())
    scope = manifest['fixed_scope']
    if any(scope.get(k) != v for k, v in FIXED_SCOPE.items()):
        raise ValueError('Only the declared M8/n3/N128/1152-stage native provider is supported')
    required = dict(modes=8, spacing=3, quadrature=128, steps=16,
                    shootingParts=16, solveTolerance=2e-9,
                    orientation=1, cuspAwareFlow=True)
    if (any(config.get(k) != v for k, v in required.items()) or
            config.get('projectionFloor', .05) != .05 or config.get('sharedEngines')):
        raise ValueError('The original finite configuration and all stopping/domain gates are required')
    if set(historical_native_sources) != set(NATIVE_NAMES):
        raise ValueError('The complete historical eight-file native map is required')
    topic = Path(manifest['source_topic']).resolve()
    source_root = topic/'repro/source-root'
    if not source_root.is_dir():
        raise ValueError('The explicit provider source root is unavailable')
    native = {name: sha(topic/'scripts'/name) for name in NATIVE_NAMES}
    changed = {name for name in NATIVE_NAMES if native[name] != historical_native_sources[name]}
    if changed != {'950f-tail-stage-core.mjs', '950f-tail-stage-port-v3.mjs'}:
        raise ValueError('Only the announced whole-evaluate core hook and worker factory import may replace the old native map')
    files = {str(path): manifest_sha256}
    for item in file_refs(manifest):
        p = Path(item['path']).resolve()
        if sha(p) != item['sha256']:
            raise ValueError('A native manifest input/source/executable/library changed: '+str(p))
        if str(p) in files and files[str(p)] != item['sha256']:
            raise ValueError('Conflicting provider fingerprints')
        files[str(p)] = item['sha256']
    for name in ('cpp', 'header', 'executable', 'build'):
        item = manifest['native_files'][name]
        if files.get(str(Path(item['path']).resolve())) != item['sha256']:
            raise ValueError('The full native build binding is required')
    if not manifest['runtime_libraries']:
        raise ValueError('The native runtime-library identities are required')
    for name in ('native_batch_adapter.mjs', 'native_batch_factory.mjs'):
        p = topic/'scripts'/name
        if files.get(str(p)) != sha(p):
            raise ValueError('The native adapter/factory must be covered by the manifest')
    files.update({str(topic/'scripts'/name): digest for name, digest in native.items()})
    return dict(schema='m3-explicit-literal-native-tail-provider-v1',
        manifest=ref(path), source_topic=str(topic), source_root=str(source_root),
        client=ref(topic/'scripts/950f-tail-client-v3.py'),
        historical_native_source_sha256=copy.deepcopy(historical_native_sources),
        native_tail_source_sha256=native, changed_native_map_entries=sorted(changed),
        source_sha256=files, fixed_scope=copy.deepcopy(scope),
        mathematics_scope='Same finite tail configuration, residual/normalization/line-search/stop/cut/audit gates. Shooting state and its literal implicit Jacobian use the explicitly bound native arithmetic provider; no byte equality to V8 is claimed.',
        historical_response_scope='Old V8 actual responses are retained only as historical inner-affine evidence. They are not inserted into the new provider actual-response cache.',
        binding_operation_scope='This descriptor is produced by metadata-only identity validation. It makes no claim about whether a later consumer has executed the bound provider.')


def runtime_environment(provider, directory):
    return dict(VISIBLE_FLEX_NATIVE_MANIFEST=provider['manifest']['path'],
                VISIBLE_FLEX_NATIVE_MANIFEST_SHA256=provider['manifest']['sha256'],
                VISIBLE_FLEX_NATIVE_RUN_DIR=str(Path(directory).resolve()/'native-provider-runs'))


def install_client(context, module_loader):
    """Change only the active tail client; keep prefix imports/source-root literal."""
    provider = context.plan['active_tail_provider']
    for path, digest in provider['source_sha256'].items():
        if sha(path) != digest:
            raise ValueError('The active native provider changed before client installation: '+path)
    client = module_loader('explicit_m3_literal_native_client', Path(provider['client']['path']))
    original = client.WeightedTailPort

    class ProviderWeightedTailPort(original):
        def __init__(self, config, source_root, record_prefix, node_heap=1536):
            # The original main still supplies the original prefix source root.
            # Only this worker's environment is redirected to the new provider.
            super().__init__(config, Path(provider['source_root']), record_prefix, node_heap=node_heap)
            if self.sources != provider['native_tail_source_sha256']:
                self.close()
                raise ValueError('The new worker did not report the bound native map')

    from types import SimpleNamespace
    context.coupler.client = SimpleNamespace(WeightedTailPort=ProviderWeightedTailPort)
    context.event('explicit_tail_arithmetic_provider_installed',
        provider_manifest=provider['manifest'], provider_client=provider['client'],
        provider_source_root=provider['source_root'],
        original_prefix_source_root_unchanged=True,
        native_tail_source_sha256=provider['native_tail_source_sha256'])


def provider_parameter_io_mapping(before, after, old_config, new_config, provider):
    """Remove only two exact provider annotations, then apply the old checker.

    The annotations are not configuration options or physical parameters.
    Ready carries shootingEvaluation; a successfully returned native checkpoint
    additionally carries its actual manifest SHA. Their before/after presence
    is recorded explicitly. Every remaining key follows the original checker.
    """
    from recovering_tail_client_v2 import validate_parameter_io_mapping
    expected = dict(shootingEvaluation='native-literal-LD-batch-v1',
                    nativeBatchManifestSHA256=provider['manifest']['sha256'])
    if any(key in old_config or key in new_config for key in expected):
        raise ValueError('Provider annotations must not become new configuration options')
    left, right = copy.deepcopy(before), copy.deepcopy(after)
    annotations = {}
    for key, value in expected.items():
        for label, source in (('before', before), ('after', after)):
            if key in source and source[key] != value:
                raise ValueError('A provider annotation has another value: '+label+':'+key)
        annotations[key] = dict(before_present=key in before, before=before.get(key),
                                after_present=key in after, after=after.get(key))
        left.pop(key, None)
        right.pop(key, None)
    if after.get('shootingEvaluation') != expected['shootingEvaluation']:
        raise ValueError('The readied worker does not identify the native arithmetic provider')
    original = validate_parameter_io_mapping(left, right, old_config, new_config)
    return dict(original_parameter_IO_transition=original, provider_annotations=annotations,
                physical_or_numerical_keys_relaxed=False)


def check_native_response_metadata(record, provider):
    parameters = record['response']['checkpoint']['parameters']
    if (parameters.get('shootingEvaluation') != 'native-literal-LD-batch-v1' or
            parameters.get('nativeBatchManifestSHA256') != provider['manifest']['sha256'] or
            parameters.get('projectionFloor') != .05):
        raise ValueError('The complete actual response does not bind this native manifest/.05 gate')
