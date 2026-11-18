#!/usr/bin/env python3
"""Hash/read/AST-only preparation of the R47 endpoint model and R48 transfer.

No endpoint checkpoint is invented or loaded as a model.  The q060 binding
is read solely for already recorded original source hashes.  No new module,
core, projection, flow, integral, tail, BVP or mathematical probe is executed.
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
NEW_SOURCE_SHA256 = {
    'r47_endpoint_refinement_model.py': 'd533b93dc78b1eed7656527aa8ac689772f9a4903e441cd5f49e51d2ef16b7b6',
    'r48_reference_state_transfer.py': 'fe7decedceb9b20d9fa70715a40494b24670f40dd28a4c88fc80033d7a14610a',
}
ADDITIONAL_DEPENDENCIES = {
    'm3_raw_diagnostic_model.py': '7e61ce828751789262b99803172065ff6eaa61eab00d86c6a6fb7ac8ae9fc14e',
    'synchronous_core_lift.py': '97e65d2cb8bee00f9fb918de5e44a7b486bf318c11ae2765dbc0c1dd6cfdf6c8',
    'round_raw_lib/exact_core_lift.py': '28936553078df9d1a2c6486fab1613c20fd7cfdb9b4134d4c95e1d60fa5623f5',
    'round_raw_lib/analytic_adaptive_core_jac.py': 'da6690d9f11eac38cec0acee31aa07555a8d1ddd81c1b24997db0421ea19e431',
    'round_raw_lib/exact_lift_parameter_jac.py': 'f64b51e434e4050a8c46bc5ea1376c824413679ec6e8bee2be7bc221021d8b89',
    'round_raw_lib/tight_moment_interval_bounds.py': '9e630a109aac1393f34c02912a61ca960da2d4a3c0b4075182467df46f1cc83f',
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def literal(node):
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name) and node.id in ('HERE', 'M3'):
        return {'HERE': HERE, 'M3': M3}[node.id]
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
        return literal(node.left)/literal(node.right)
    if isinstance(node, ast.Dict):
        return {literal(k): literal(v) for k, v in zip(node.keys, node.values)}
    raise ValueError('Only literal source identities and declared path joins are accepted')


def assignment(path, name):
    tree = ast.parse(Path(path).read_text(), filename=str(path))
    matches = [s.value for s in tree.body if isinstance(s, ast.Assign) and
               len(s.targets) == 1 and isinstance(s.targets[0], ast.Name) and s.targets[0].id == name]
    if len(matches) != 1:
        raise ValueError('A unique literal source identity dictionary is required')
    return literal(matches[0])


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
    own = [Path(__file__).resolve(), *(HERE/n for n in NEW_SOURCE_SHA256)]
    for name, expected in NEW_SOURCE_SHA256.items():
        if sha(HERE/name) != expected:
            raise ValueError('An unreviewed new source changed: '+name)
    for path in own:
        ast.parse(path.read_text(), filename=str(path))
    deps = assignment(HERE/'r47_endpoint_refinement_model.py', 'DEPENDENCIES')
    for filename, field in (('r47_fixed_slot_trace_basis.py', 'DEPENDENCY_SHA256'),
                            ('r47_fixed_slot_trace_core.py', 'CORE_DEPENDENCY_SHA256')):
        deps.update({M3/name: digest for name, digest in assignment(HERE/filename, field).items()})
    deps.update({M3/name: digest for name, digest in ADDITIONAL_DEPENDENCIES.items()})
    old_binding = HERE/'q060_cosine_reference_binding.json'
    old = json.loads(old_binding.read_text())
    for field in ('original_execution_source_sha256', 'current_reference_source_sha256'):
        for name, digest in old[field].items():
            path = Path(name).resolve()
            if path in deps and deps[path] != digest:
                raise ValueError('Original source registries disagree: '+name)
            deps[path] = digest
    for path, expected in deps.items():
        if sha(path) != expected:
            raise ValueError('A bound defining/execution source changed: '+str(path))
    proofs = [HERE.parent.parent/'results'/name for name in
              ('R47-fixed-slot-nested-circle-homotopy.md',
               'R48-exact-reference-compensation-for-mode-extension.md')]
    directory = args.directory.resolve()
    directory.mkdir(parents=True, exist_ok=False)
    full = dict(scope=__doc__, prepared_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        command=sys.argv, new_sources=[ref(path) for path in own],
        old_reference_source_registry=ref(old_binding),
        source_sha256={str(path): digest for path, digest in sorted(deps.items(), key=lambda x: str(x[0]))},
        source_registry_scope='Read only the original source identities; the old q060 curve is not a new endpoint or numerical input.',
        proof_definitions=[ref(path) for path in proofs],
        interface=dict(model='EndpointModeEnvironment(real_endpoint.native_prefix()).make(M, angular, linear_port_path)',
            required_anchor='A genuine completed M8 lambda=1 prefix/actual-tail/physical-quintic checkpoint, not yet available for this preparation.',
            new_mode_range='Integer M>=8; every new model uses the unchanged full-lift and original parameter equations.',
            core_initialization='model.initialize_core() is a future explicit original initial(p) call, not part of this preparation.',
            source_old_parameters='Copy old p[1:8] literally; new p[0]=0, append zero controls; assert the first seven pscales and physical c bits.',
            p0_scope='Original fixed=True p0=log(q_actual/qseed) remains free. Frozen profile does not imply frozen q/controls.',
            profile_rebase='Use the actual frozen_profile once, with the old delta p0 already incorporated.',
            new_actual_tail='Require a real M-dimensional original DN/Jac/audit response; no old response or J is embedded.',
            state_transfer='EndpointStateTransfer(model): blockwise physical-PPoly embedding plus a*chi*(I_new-E*I_old).',
            state_order='R0,R1..RM,T1..TM,Z1..ZM',
            physical_jets='Retain the original a, a_s, a_ss and quintic window derivatives, including the 2*a_s*chi_s cross term.',
            normalized_mesh='The old physical PPoly mesh is mapped through the new original inverse_chart. Old variable-profile raw t is not presumed identical.',
            zero_window='Copy embedded state jets without a floating addition when their reference factor is exactly zero.',
            mean_scope='No mean primitive copied or recomputed; no whole physical map identity inferred from planar compensation alone.',
            interpolation_scope='A continuous callable state is prepared; no new quintic is claimed to equal this non-polynomial function.',
            finite_core_scope='Defining-core nesting is mathematical; no cross-M floating inversion/projection identity is assumed.',
            fixed_all_parameters_refinement_claim=False),
        preparation=dict(AST_sources=len(own), source_hashes_checked=len(deps),
            new_module_imports=0, core_instances=0, flow_instances=0, BVP_instances=0,
            original_or_new_endpoint_reconstructed=False, full_inlet_projections=0,
            initial_field_evaluations=0, parameter_derivative_evaluations=0,
            chart_inverse_calls=0, mean_integrals=0, prefix_audits=0, BVP_solves=0,
            actual_tail_requests=0, new_accepted_endpoint_claim=False,
            source_only=True))
    complete_ref = save(directory/'source-preparation.json', full)
    compact = {key: value for key, value in full.items() if key != 'source_sha256'}
    compact['complete_source_manifest'] = complete_ref
    compact['bound_source_count'] = len(deps)
    compact['bound_source_payload_sha256'] = hashlib.sha256(json.dumps(full['source_sha256'],
        sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    output = save(args.record.resolve(), compact)
    print(json.dumps(dict(record=output, complete_manifest=complete_ref,
        bound_sources=len(deps), AST_sources=len(own), source_only=True)), flush=True)


if __name__ == '__main__':
    main()
