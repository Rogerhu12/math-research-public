#!/usr/bin/env python3
"""Read/hash/AST-only preparation of the R47 low-level fixed-slot sources.

No new basis or core is imported or instantiated. Literal source substitutions
are reconstructed using a restricted AST reader, then reversed and parsed.
This records an implementable interface and its exact dependencies, not a
numerical nesting comparison, a higher-M BVP, or a continuous certificate.
"""
import argparse
import ast
import datetime
import hashlib
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
M3 = HERE.parent/'resume_m3'


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def restricted_literal(node, known):
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name) and node.id in known:
        return known[node.id]
    if isinstance(node, (ast.List, ast.Tuple)):
        items = [restricted_literal(v, known) for v in node.elts]
        return tuple(items) if isinstance(node, ast.Tuple) else items
    if isinstance(node, ast.Dict):
        return {restricted_literal(k, known): restricted_literal(v, known)
                for k, v in zip(node.keys, node.values)}
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        return restricted_literal(node.left, known)+restricted_literal(node.right, known)
    raise ValueError('Only literal source metadata/string concatenation is allowed')


def read_assignments(path, names):
    text = Path(path).read_text()
    tree = ast.parse(text, filename=str(path))
    values = {}
    for statement in tree.body:
        if not isinstance(statement, ast.Assign) or len(statement.targets) != 1:
            continue
        target = statement.targets[0]
        if isinstance(target, ast.Name) and target.id in names:
            values[target.id] = restricted_literal(statement.value, values)
    if set(values) != set(names):
        raise ValueError('Every requested defining literal must be present')
    return values


def transform(text, substitutions):
    original = text
    for before, after in substitutions:
        if text.count(before) != 1:
            raise ValueError('A source substitution is not unique: '+before)
        text = text.replace(before, after)
    recovered = text
    for before, after in reversed(substitutions):
        if recovered.count(after) != 1:
            raise ValueError('A reverse substitution is not unique: '+after)
        recovered = recovered.replace(after, before)
    if recovered != original:
        raise ValueError('Unlisted source changes remain')
    ast.parse(text)
    return text


def save(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False, allow_nan=False)
        stream.write('\n')
    return ref(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, required=True)
    parser.add_argument('--record', type=Path, required=True)
    args = parser.parse_args()
    basis = HERE/'r47_fixed_slot_trace_basis.py'
    core = HERE/'r47_fixed_slot_trace_core.py'
    for path in (Path(__file__), basis, core):
        ast.parse(path.read_text(), filename=str(path))
    basis_meta = read_assignments(basis, ['DEPENDENCY_SHA256'])
    core_meta = read_assignments(core, ['CORE_DEPENDENCY_SHA256', 'BASIS_IMPORT'])
    dependencies = {**basis_meta['DEPENDENCY_SHA256'], **core_meta['CORE_DEPENDENCY_SHA256']}
    for name, expected in dependencies.items():
        if ref(M3/name)['sha256'] != expected:
            raise ValueError('An actual defining dependency changed: '+name)
    release = read_assignments(M3/'round_raw_lib/fixed_large_radius_core.py', ['TRANSFORMS'])['TRANSFORMS']
    second = read_assignments(M3/'raw_second_order_core.py', ['SECOND', 'ADDITIONS'])['ADDITIONS']
    combined = read_assignments(M3/'circle_trace_replacement_core.py', ['guard_replacements'])['guard_replacements']
    original = (M3/'round_raw_lib/large_radius_local_core.py').read_text()
    released = transform(original, release)
    same_guard = transform(released, second)
    substitutions = [core_meta['BASIS_IMPORT'], *combined]
    derived = transform(same_guard, substitutions)
    directory = args.directory.resolve()
    directory.mkdir(parents=True, exist_ok=False)
    derived_path = directory/'derived-integral-core.py'
    with derived_path.open('x') as stream:
        stream.write(derived)
    full = dict(scope=__doc__, preparation_command=sys.argv,
        prepared_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        source_files=[ref(p) for p in (Path(__file__), basis, core)],
        original_source_files=[ref(M3/name) for name in dependencies],
        proof_definitions=[ref(HERE.parent.parent/'results'/name) for name in
            ('R47-fixed-slot-nested-circle-homotopy.md',
             'R48-exact-reference-compensation-for-mode-extension.md')],
        literal_substitutions=dict(release_original_first_control=release,
            original_second_order_guard=second, fixed_slot_basis_and_existing_combined_bound=substitutions),
        exact_reverse_source_substitutions=True, derived_integral_core=ref(derived_path),
        derived_original_second_order_core_sha256=hashlib.sha256(same_guard.encode()).hexdigest(),
        new_source_files_AST_parsed=3, new_module_imported=False, basis_instances=0,
        core_instances=0, new_integrals=0, BVP_calls=0, tail_calls=0,
        interface=dict(factory='make_core_factory(reference, original_cosine, settings, *, modes=M)',
            physical_controls='Complete M-1 coefficients in fixed-slot order; no pscale conversion in this interface',
            fixed_trace_zero_based_control_indices=[5, 6],
            fixed_trace_zero_based_parameter_indices_if_delta_first=[6, 7],
            endpoint_order='B2,B3,B4,B5,B6,T,U,B7,...,B(M-2)',
            endpoint_fixed_to_canonical='[0,1,2,3,4,M-3,M-2,5,...,M-4]',
            cosine_frequency_for_slot_j='3*j, j=2..M',
            M8_branch='Directly return the frozen original M8 factory and descriptor',
            zero_branch='Return the supplied original cosine class; high-level dimension/floor handling is unchanged',
            positive_branch='Original integral inverse and full parameter jets; exact fixed/canonical permutation and existing combined trace bound',
            primitive_normalization='Unchanged canonical primitive about the reflection axis and inherited u(0)=0',
            new_high_level_model_installed=False,
            physical_state_or_mean_transfer_implemented=False,
            cross_M_binary64_identity_claimed=False,
            continuous_geometry_certificate_claimed=False))
    full_ref = save(directory/'source-preparation.json', full)
    compact = {k: v for k, v in full.items() if k != 'literal_substitutions'}
    compact['full_literal_source_record'] = full_ref
    compact['original_release_transform_count'] = len(release)
    compact['original_second_order_guard_transform_count'] = len(second)
    compact['new_core_transform_count'] = len(substitutions)
    record = save(args.record.resolve(), compact)
    print(json.dumps(dict(record=record, full_record=full_ref,
        original_dependencies=len(dependencies), source_only=True,
        no_model_or_integral_constructed=True)), flush=True)


if __name__ == '__main__':
    main()
