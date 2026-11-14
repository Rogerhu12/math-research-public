#!/usr/bin/env python3
"""Real synthetic storage/reader checks; never a candidate certificate.

The old and new readers receive exactly the same original gzip/NPZ bytes.
This checks source replay, finite arithmetic equivalence and the actual new
terminal's hash-only prefix-storage subroutine. It does not call candidate(),
the complete terminal gate, a source solver, or a curve/surface optimizer.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import copy
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return {'file': str(path), 'bytes': len(raw), 'sha256': sha(raw)}


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def require(ok, message):
    if not ok:
        raise ValueError(message)


def terminal_child(base_path, expanded_path):
    """Fresh stdlib-only call of the actual terminal storage subroutine."""
    require(not any(k.split('.')[0] in ('numpy', 'scipy') for k in sys.modules),
            'Numerical modules were already imported in the child')
    terminal = load('storage_child_actual_terminal',
                    HERE / '78718-prefix-terminal-error-storage-v2.py')
    base = json.loads(base_path.read_text())
    geom = json.loads(expanded_path.read_text())
    files = terminal.Files()
    for name in terminal.PREFIX_SOURCES:
        files.prefix_source(name)
    records = terminal.prefix_storage(files, base_path, base, geom)
    relocated = [{**row, 'file': '/unavailable-prior-fixture/' + Path(row['file']).name}
                 for row in records]
    terminal.prefix_storage_ledger(files, relocated, records, base_path.parent,
                                   'synthetic-relocated-storage-only')
    rejects = []
    for name, action in [
        ('omitted-storage-file', lambda: terminal.prefix_storage_ledger(
            terminal.Files(), relocated[:-1], records, base_path.parent, 'omitted')),
        ('changed-common-logical-hash', lambda: terminal.prefix_storage(
            terminal.Files(), base_path, base, {**geom, 'data_sha256': '0' * 64})),
        ('changed-common-storage-reference', lambda: terminal.prefix_storage(
            terminal.Files(), base_path, base,
            {**geom, 'data_storage': {**geom['data_storage'], 'modes': geom['modes']}})),
    ]:
        try:
            action()
        except (ValueError, KeyError) as exc:
            rejects.append({'case': name, 'reason': str(exc)})
        else:
            raise ValueError('Terminal storage subroutine accepted ' + name)
    require(not any(k.split('.')[0] in ('numpy', 'scipy') for k in sys.modules),
            'The hash-only terminal storage path imported a numerical module')
    print(json.dumps({'status': 'PASS_ACTUAL_TERMINAL_STORAGE_SUBROUTINE_ONLY',
        'base_modes': base['modes'], 'expanded_metadata_modes': geom['modes'],
        'actual_storage_files': len(records), 'bound_prefix_sources': len(terminal.PREFIX_SOURCES),
        'relocated_ledger_matched': True, 'rejections': rejects,
        'numpy_scipy_imported': False, 'complete_candidate_gate_called': False,
        'solver_calls': 0}))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--scratch-dir', type=Path)
    ap.add_argument('--source-ledger', type=Path)
    ap.add_argument('--report', type=Path)
    ap.add_argument('--terminal-child', type=Path)
    ap.add_argument('--expanded-meta', type=Path)
    args = ap.parse_args()
    if args.terminal_child is not None:
        terminal_child(args.terminal_child, args.expanded_meta)
        return 0
    require(args.scratch_dir is not None and args.source_ledger is not None
            and args.report is not None, 'Missing explicit check paths')
    require(not args.scratch_dir.exists() and not args.report.exists(), 'Use unused check paths')
    args.scratch_dir.mkdir(parents=True)
    start = time.monotonic()
    ledger = json.loads(args.source_ledger.read_text())
    builder_path = HERE / '78718-build-storage-adapters-v3.py'
    require(ledger['builder_sha256'] == identity(builder_path)['sha256'], 'Changed source builder')
    builder = load('storage_reader_checked_builder', builder_path)
    generated, rows = builder.build_all()
    require(rows == ledger['transformations'], 'Full unique source replay differs from ledger')
    for name, raw in generated.items():
        require((HERE / name).read_bytes() == raw, 'Changed adapter: ' + name)
    source_ids = [identity(builder_path), identity(args.source_ledger), identity(__file__)]
    source_ids += [identity(HERE / name) for name in builder.ORIGINAL]
    source_ids += [identity(HERE / name) for name in generated]

    # Load every actual adapter to resolve the complete declared local imports.
    modules = {key: load('storage_smoke_' + key, HERE / name)
               for key, name in builder.NEW.items()}
    old_terminal = load('storage_old_terminal_source_only',
                        HERE / 'db6f-prefix-terminal-error-storage-v3.py')
    new_terminal = modules['terminal']
    require(new_terminal.SOURCES == old_terminal.SOURCES, 'Changed original tail/reference source family')
    for name in ('BOUND', 'FACTOR', 'LOWER', 'HEIGHT_SHA', 'POSITIVE_ALPHA_SHA'):
        require(getattr(new_terminal, name) == getattr(old_terminal, name),
                'Changed original terminal constant: ' + name)
    for name, digest in new_terminal.PREFIX_SOURCES.items():
        require(identity(HERE / name)['sha256'] == digest, 'Broken new terminal source pin')
    for name, digest in modules['angular'].SOURCES.items():
        require(identity(HERE / name)['sha256'] == digest, 'Broken new angular source pin')

    import numpy as np
    from fractions import Fraction
    original_float = load('storage_original_shared_reader', HERE / '950f-root-fullxyz-hermite.py')
    original_interval = load('storage_original_exact_reader', HERE / 'db6f-audit-continuous-hermite.py')
    storage = modules['helper']
    cases = []

    def exact_array(a, b, label):
        require(a.dtype == b.dtype and a.shape == b.shape, 'Reader layout differs: ' + label)
        require(np.array_equal(a, b) and np.array_equal(np.signbit(a), np.signbit(b)),
                'Reader arithmetic differs: ' + label)
        # Long double padding bytes are not a semantic floating-point value.
        if a.dtype == np.dtype('<f8'):
            require(a.tobytes(order='C') == b.tobytes(order='C'),
                    'Binary64 reader bytes differ: ' + label)

    for modes, nodes in ((2, 5), (24, 11)):
        directory = args.scratch_dir / ('modes-' + str(modes))
        directory.mkdir()
        rng = np.random.default_rng(78718000 + modes)
        mesh = np.linspace(0, 1, nodes, dtype='<f8')
        jets = rng.integers(-16384, 16384, size=(3, nodes, 3 * modes + 2)).astype('<f8') / 2**20
        jets[0, :, 0] += 2
        jets[0, 0, 2 * modes + 1:] = 0
        jets[1, 0, :2 * modes + 1] = 0
        jets[1, :, -1] = 1
        jets[2, 0, 2 * modes + 1:] = 0
        jets[2, 1, 1] = -0.0
        increments = rng.integers(-1000, 1000, nodes - 1).astype('<f8') / 2**22
        stream = io.BytesIO()
        np.savez(stream, mesh=mesh, jets=jets, mean_increments=increments)
        payload = gzip.compress(stream.getvalue(), mtime=0)
        require(len(payload) < 1_000_000, 'This finite fixture should be small')
        legacy_data = directory / 'legacy-data.npz.gz'
        legacy_data.write_bytes(payload)
        common = {'modes': modes, 'nodes': nodes, 'ell': 0.0,
                  'data_sha256': sha(payload), 'scope': 'synthetic storage test; no geometric certificate'}
        old_meta = directory / 'legacy.json'
        old_meta.write_text(json.dumps({**common, 'data_file': legacy_data.name}) + '\n')
        envelope = storage.write_payload(directory / 'new', payload,
                                          nodes=nodes, modes=modes, chunk_bytes=257)
        new_meta = directory / 'new.json'
        new_meta.write_text(json.dumps({**common, 'data_storage': envelope}) + '\n')
        loaded, recovered, bindings = storage.read_payload(new_meta, verify_arrays=True)
        require(recovered == payload, 'Original gzip/NPZ bytes changed')
        a = original_float.SharedHermite(old_meta)
        b = modules['fullxyz'].SharedHermite(new_meta)
        for name in ('x', 'jets', 'steps', 'h', 'c'):
            exact_array(getattr(a, name), getattr(b, name), name)
        sample = np.unique(np.r_[mesh, (mesh[:-1] + mesh[1:]) / 2, np.linspace(0, 1, 29)])
        for derivative in (0, 1, 2):
            exact_array(a.evaluate(sample, derivative), b.evaluate(sample, derivative),
                        'evaluated derivative ' + str(derivative))
        for aa, bb in zip(a.basis(97), b.basis(97)):
            exact_array(aa, bb, 'Fourier basis')
        ia = original_interval.ExactHermite(old_meta)
        ib = modules['continuous'].ExactHermite(new_meta)
        require(ia.inlet_exact == ib.inlet_exact and ia.inlet_radius_exact == ib.inlet_radius_exact,
                'Exact inlet arithmetic changed')
        exact_array(ia.x, ib.x, 'interval mesh')
        for name in ('h', 'power'):
            for endpoint in ('lo', 'hi'):
                exact_array(getattr(getattr(ia, name), endpoint),
                            getattr(getattr(ib, name), endpoint), name + endpoint)
        for derivative in (0, 1, 2):
            for lo, hi in ((Fraction(0), Fraction(1)), (Fraction(1, 4), Fraction(3, 4))):
                va, vb = ia.ranges(derivative, lo, hi), ib.ranges(derivative, lo, hi)
                exact_array(va.lo, vb.lo, 'range lower')
                exact_array(va.hi, vb.hi, 'range upper')
        require(ib.storage_bindings == bindings == b.storage_bindings, 'Actual storage closure differs')
        expanded = {**loaded, 'modes': 64}
        expanded_path = directory / 'expanded-metadata-storage-sentinel.json'
        expanded_path.write_text(json.dumps(expanded) + '\n')
        try:
            storage.read_payload(expanded_path, verify_arrays=True)
        except ValueError as exc:
            dimension_rejection = str(exc)
        else:
            raise ValueError('Expanded common-cut metadata was accepted as defining base')
        child_command = [sys.executable, str(Path(__file__).resolve()), '--terminal-child',
                         str(new_meta.resolve()), '--expanded-meta', str(expanded_path.resolve())]
        child = subprocess.run(child_command, capture_output=True, text=True, check=False)
        require(child.returncode == 0, 'Actual terminal storage child failed: ' + child.stderr[-1500:])
        child_report = json.loads(child.stdout)
        require(child_report['numpy_scipy_imported'] is False, 'Child numerical import leak')
        cases.append({'modes': modes, 'nodes': nodes, 'logical_bytes': len(payload),
            'logical_sha256': sha(payload), 'physical_files': len(bindings),
            'source_arrays_byte_identity': True,
            'shared_reader_values_and_signed_zeros_equal': True,
            'exact_interval_coefficients_and_ranges_byte_equal': True,
            'expanded_base_dimension_rejected': dimension_rejection,
            'actual_terminal_storage_subroutine': child_report,
            'synthetic_fixture_directory': str(directory.resolve())})
    result = {'schema': '78718-storage-source-and-reader-check-v1',
        'status': 'PASS_STORAGE_READERS_AND_TERMINAL_SUBROUTINE_ONLY',
        'script': identity(__file__), 'source_bindings': source_ids,
        'source_replay_adapters': len(rows), 'imported_new_sources': len(modules),
        'complete_terminal_tail_source_family_unchanged': True,
        'exact_terminal_threshold_preserved': str(new_terminal.BOUND),
        'new_prefix_source_pins_match': True, 'cases': cases,
        'seconds': time.monotonic() - start,
        'source_solver_calls': 0, 'BVP_Newton_DN_calls': 0,
        'full_common_cut_or_candidate_gate_executed': False,
        'full_producer_executed': False,
        'new_candidate_or_geometric_certificate': False,
        'production_ready': False,
        'scope': 'Synthetic byte/reader arithmetic and actual terminal storage subroutine only. Full source review and new candidate certificates remain required.'}
    raw = (json.dumps(result, indent=2, allow_nan=False) + '\n').encode()
    require(len(raw) < 100_000, 'Check report unexpectedly large')
    with args.report.open('xb') as stream:
        stream.write(raw)
    print(json.dumps({'status': result['status'], 'cases': len(cases),
        'source_replay_adapters': len(rows), 'report_bytes': len(raw),
        'report_sha256': sha(raw), 'solver_calls': 0, 'production_ready': False}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
