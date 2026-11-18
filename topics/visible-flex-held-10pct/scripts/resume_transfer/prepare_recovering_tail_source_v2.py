#!/usr/bin/env python3
"""Prepare an owned coupler overlay; do not run a prefix or a tail solve.

The original client, worker and mathematical sources stay read-only.  The
owned coupler gains the already published raw-inner serialization hook and
one separate actual-DN provenance sidecar.  A thin owned client delegates
all actual acceptance to the original WeightedTailPort and its worker.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-topic', type=Path, required=True)
    parser.add_argument('--owned-topic', type=Path, required=True)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--candidate-helper', type=Path,
        default=Path(__file__).with_name('propose_tail_internal_candidate_v3.mjs'))
    parser.add_argument('--inner-dump-installer', type=Path,
        default=Path(__file__).parents[1]/'resume_m3/install_inner_prefix_debug_record.py')
    args = parser.parse_args()
    source, dest = args.source_topic.resolve(), args.owned_topic.resolve()
    manifest = args.manifest.resolve()
    if dest.exists() or manifest.exists():
        raise FileExistsError('Use a fresh owned topic and manifest')
    if dest == source or source in dest.parents:
        raise ValueError('Owned overlay must be outside the original source tree')
    source_scripts = source/'scripts'
    original_coupler = source_scripts/'db6f-prefix-coupled.py'
    original_client = source_scripts/'950f-tail-client-v3.py'
    original_text = original_coupler.read_text()
    original_hashes = {str(p): sha(p) for p in (original_coupler, original_client)}
    runtime_root = source/'repro/source-root'
    runtime_hashes = {str(file.resolve()): sha(file) for file in sorted(runtime_root.rglob('*'))
        if file.is_file() and file.suffix in ('.py', '.mjs', '.js')}
    installer = args.inner_dump_installer.resolve()
    adapter = Path(__file__).with_name('recovering_tail_client_v2.py').resolve()
    helper = args.candidate_helper.resolve()
    if not source_scripts.is_dir() or not (source/'repro/source-root').is_dir():
        raise ValueError('A complete explicit original topic and source root are required')
    for file in (installer, adapter, helper):
        if not file.is_file():
            raise FileNotFoundError(file)
    dest.mkdir(parents=True)
    scripts = dest/'scripts'
    scripts.mkdir()
    for item in source.iterdir():
        if item.name != 'scripts':
            (dest/item.name).symlink_to(item.resolve(), target_is_directory=item.is_dir())
    replaced = {'db6f-prefix-coupled.py', '950f-tail-client-v3.py',
                'recovering_tail_client_v2.py', helper.name}
    for item in source_scripts.iterdir():
        if item.name not in replaced:
            (scripts/item.name).symlink_to(item.resolve(), target_is_directory=item.is_dir())
    owned_coupler = scripts/original_coupler.name
    shutil.copyfile(original_coupler, owned_coupler)
    shutil.copyfile(adapter, scripts/adapter.name)
    shutil.copyfile(helper, scripts/helper.name)
    installer_record = dest/'inner-dump-installation.json'
    subprocess.run([sys.executable, str(installer), '--source-topic', str(dest),
                    '--manifest', str(installer_record)], check=True)
    dumped_text = owned_coupler.read_text()
    before = ('        record_inner_prefix_debug(o,sol,a,outer,candidate)\n'
              '        actual=tail.solve(candidate,jacobian=True,audit=False)')
    after = ('        record_inner_prefix_debug(o,sol,a,outer,candidate)\n'
             '        client.record_inner_dn_anchor(a,outer,tail,height,response,candidate)\n'
             '        actual=tail.solve(candidate,jacobian=True,audit=False)')
    if dumped_text.count(before) != 1:
        raise ValueError('The published raw-inner hook must occur exactly once')
    final_text = dumped_text.replace(before, after)
    spec = importlib.util.spec_from_file_location('existing_inner_dump_installer', installer)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    original_call = ('        candidate=o.bridge.sigma*o.q*sol.y[o.iz:,-1]\n'
                     '        actual=tail.solve(candidate,jacobian=True,audit=False)')
    dumped_call = ('        candidate=o.bridge.sigma*o.q*sol.y[o.iz:,-1]\n'
                   '        record_inner_prefix_debug(o,sol,a,outer,candidate)\n'
                   '        actual=tail.solve(candidate,jacobian=True,audit=False)')
    reversed_text = final_text.replace(after, before).replace(module.HELPER, '').replace(dumped_call, original_call)
    if reversed_text != original_text:
        raise AssertionError('The owned coupler contains an unapproved equation or solver change')
    compile(final_text, str(owned_coupler), 'exec')
    owned_coupler.write_text(final_text)
    stub = '''"""Owned recovery adapter; the original worker remains the only DN solver."""
import importlib.util
from pathlib import Path

def module(name, path):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value

ORIGINAL_TOPIC=Path(ORIGINAL_TOPIC_LITERAL)
OWNED_SCRIPTS=Path(__file__).resolve().parent
base=module('unchanged_original_tail_client',ORIGINAL_TOPIC/'scripts/950f-tail-client-v3.py')
protocol=module('owned_tail_recovery_protocol',OWNED_SCRIPTS/'recovering_tail_client_v2.py')
WeightedTailPort=protocol.make_recovering_class(
    base.WeightedTailPort,ORIGINAL_TOPIC,OWNED_SCRIPTS/HELPER_LITERAL)
record_inner_dn_anchor=protocol.record_inner_dn_anchor
'''.replace('ORIGINAL_TOPIC_LITERAL', repr(str(source))).replace('HELPER_LITERAL', repr(helper.name))
    owned_client = scripts/original_client.name
    compile(stub, str(owned_client), 'exec')
    owned_client.write_text(stub)
    for file, digest in original_hashes.items():
        if sha(file) != digest:
            raise AssertionError('An original source changed during preparation')
    for file, digest in runtime_hashes.items():
        if sha(file) != digest:
            raise AssertionError('An original runtime source changed during preparation')
    if (dest/'repro/source-root').resolve() != (source/'repro/source-root').resolve():
        raise AssertionError('Owned overlay changed the original runtime source root')
    record = dict(scope=__doc__, command=[sys.executable, *sys.argv],
        original_topic=str(source), owned_topic=str(dest),
        original_source_sha256=original_hashes,
        original_runtime_source_sha256=runtime_hashes,
        preparation_source_sha256={str(file): sha(file) for file in
            (Path(__file__).resolve(), installer, adapter, helper)},
        owned_source_sha256={str(file): sha(file) for file in
            (owned_coupler, owned_client, scripts/adapter.name, scripts/helper.name)},
        existing_raw_dump_installer=dict(path=str(installer_record), sha256=sha(installer_record)),
        coupler_reverse_patch_restores_original_bytes=True,
        original_sources_unchanged=True, source_root_identity=True,
        actual_solver_invoked=False, production_wrapper_executed=False,
        candidate_budget_per_failed_request=dict(external_calls=1, original_worker_retries=1),
        physical_solver_configuration_changes=[],
        allowed_restart_metadata_changes=['initialCheckpoint', 'designInitialCheckpoint',
                                          'secantCheckpoint', 'traceFile'])
    with manifest.open('x') as stream:
        json.dump(record, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(event='owned_recovery_source_prepared', manifest=str(manifest),
                         sha256=sha(manifest), solver_invoked=False)))


if __name__ == '__main__':
    main()
