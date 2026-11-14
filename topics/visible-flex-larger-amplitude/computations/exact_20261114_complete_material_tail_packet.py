#!/usr/bin/env python3
"""Material-angle packet for an actually accepted complete frozen scalar profile.

This independently named adapter changes only the old packet's scalar-profile
constructor and its physical-identity serialization.  All original material
inversion, physical-quintic jets, spectra, truncation diagnostics and complete
core-coordinate derivatives are retained.  Both the complete v1 formula and
the explicitly serialized three-prefix-control v2 formula are recognized.
There is no candidate generation, tail solve, or acceptance-threshold change.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import inspect
import json
import os
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
PACKET_NAME = 'exact_20261114_material_tail_packet.py'
PACKET_SHA = '48878519297a5868fc91b82c630b0d5e34c1bfcb98fb9ef66f05117665bfd233'
FORMULA_SOURCES = {
    'geometry_20261114_full_scalar_profile.py': '8ff23e31a58d0f8b087929d69ac8d6f9b6f2777615e50eef5ebe40ed7b6bed6b',
    'geometry_20261114_full_dn_readout.py': 'f6602baa54d3f599deb7d7c40ac9f4806e5faca2fc305b674b1c1cda02067cb1',
    'geometry_20261114_prefix_controls_profile.py': 'f019e6b33c8e1776d5cca87c22efadd0f999766b894be855efb53ad10b4d6a24',
    'strong_20261114_scaled_core_tail_connector.py': '661d5d84dc0dd3da46f4936c2c3ad28f80df3475f421c56d770a2afa6402ac08',
    'alternative-neck-provider.py': '84ed048425c8b0f4deeec8af37828e318150cde5d59995da77f64d923591b9c2',
    'geometry_20261114_r225_fixed_profile.py': '478d0bf603ea05a9f20228ff2fd591e2f767e6ab0686a6129b1114aa831b0c6c',
}
SCHEMAS = ('complete-controlled-scalar-profile-v1',
           'complete-prefix-controls-scalar-profile-v2')
OLD_CONSTRUCTOR = '    fixed = helper.base.fixed.FixedProfile(data["fixed_scalar_profile"]["geometry"])'
NEW_CONSTRUCTOR = '    fixed = completed_profile_factory(data["fixed_scalar_profile"]["geometry"])'
OLD_IDENTITY = '''    physical_identity = dict(
        accepted_core_coefficients_rational=[str(Fraction(float(value))) for value in core],
        scalar_initial_law=data["fixed_scalar_profile"]["geometry"]["initial_law"],
        scalar_exact_polynomial_sha256=fixed.exact_coefficient_sha256,
        scalar_knots=data["fixed_scalar_profile"]["geometry"]["knots"])'''
NEW_IDENTITY = '    physical_identity = completed_physical_identity(data, core, fixed)'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    if (os.environ.get('GITHUB_ACTIONS') != 'true' or
            os.environ.get('GITHUB_REPOSITORY', '').lower() != 'rogerhu12/math-research-public'):
        raise RuntimeError('Numerical execution belongs to this public repository Actions')
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args, _ = parser.parse_known_args()
    if digest(HERE/PACKET_NAME) != PACKET_SHA:
        raise ValueError('Original material-packet implementation changed')
    for name, expected in FORMULA_SOURCES.items():
        if digest(HERE/name) != expected:
            raise ValueError('Frozen complete scalar implementation changed: '+name)

    import exact_20261114_material_tail_packet as original
    from geometry_20261114_prefix_controls_profile import reconstruct_profile

    data = original.read_json(args.input)
    geometry = data.get('fixed_scalar_profile', {}).get('geometry', {})
    if data.get('success') is not True or geometry.get('schema') not in SCHEMAS:
        raise ValueError('Use an actual accepted complete v1/v2 field, not a prepared warm seed')
    if data.get('complete_scalar_profile') != geometry:
        raise ValueError('The two saved complete scalar definitions differ')
    if data.get('scalar_parameters') != geometry.get('frozen_design_parameters'):
        raise ValueError('The saved solved controls differ from their frozen scalar definition')
    tail_hash = data.get('actual_tail', {}).get('final_response_sha256')
    if (not isinstance(tail_hash, str) or len(tail_hash) != 64 or
            any(c not in '0123456789abcdef' for c in tail_hash)):
        raise ValueError('The complete accepted input must retain its actual final tail identity')

    def completed_profile_factory(specification):
        if specification != geometry:
            raise ValueError('Do not change the accepted complete scalar specification')
        # v2 reconstruct_profile verifies its serialized support/polynomial/source
        # identity and delegates the explicit v1 schema to its original reader.
        return reconstruct_profile(specification)

    def completed_physical_identity(saved, core, fixed):
        if saved['fixed_scalar_profile']['geometry'] != geometry:
            raise ValueError('The physical identity must bind the same frozen formula')
        if fixed.frozen_parameters.tolist() != geometry['frozen_design_parameters']:
            raise ValueError('Not every original solved scalar control was retained')
        return dict(
            schema='complete-scalar-physical-field-identity-v1',
            accepted_core_coefficients_rational=[str(Fraction(float(value))) for value in core],
            frozen_complete_scalar_definition=geometry,
            frozen_scalar_parameters_rational=[str(Fraction(float(value)))
                                               for value in fixed.frozen_parameters],
            scalar_formula_dependency_sha256=FORMULA_SOURCES,
            scalar_knots=[float(x) for x in fixed.knots],
            scalar_end=float(fixed.end),
            material_metric='ds^2+a(s;the complete frozen scalar definition)^2*dtheta^2',
            identity_scope='Binds both this finite embedding core and the complete scalar formula; core coefficients are not coefficients of the abstract material metric.')

    def extended_source_hashes(helper):
        answer = original.source_hashes(helper)
        answer.update(FORMULA_SOURCES)
        answer[Path(__file__).name] = digest(__file__)
        return dict(sorted(answer.items()))

    source = inspect.getsource(original.main)
    transformed = source
    changes = []
    for old, new, description in [
        (OLD_CONSTRUCTOR, NEW_CONSTRUCTOR, 'Construct the complete accepted frozen v1/v2 scalar formula.'),
        (OLD_IDENTITY, NEW_IDENTITY, 'Bind its full scalar specification and sources without falsely naming it one polynomial.'),
    ]:
        if transformed.count(old) != 1:
            raise ValueError('The sole expected scalar adaptation anchor changed')
        transformed = transformed.replace(old, new, 1)
        changes.append(dict(description=description,
                            old_fragment_sha256=hashlib.sha256(old.encode()).hexdigest(),
                            new_fragment_sha256=hashlib.sha256(new.encode()).hexdigest()))
    namespace = dict(vars(original))
    namespace.update(completed_profile_factory=completed_profile_factory,
                     completed_physical_identity=completed_physical_identity,
                     source_hashes=extended_source_hashes, __doc__=__doc__)
    exec(compile(transformed, '<original-material-packet-complete-scalar-adapter>', 'exec'), namespace)
    namespace['main']()

    out = args.out.resolve()
    record = dict(schema='complete-material-packet-adaptation-v1',
        adapter_sha256=digest(__file__), original_packet_sha256=PACKET_SHA,
        original_main_sha256=hashlib.sha256(source.encode()).hexdigest(),
        adapted_main_sha256=hashlib.sha256(transformed.encode()).hexdigest(),
        exact_changed_fragments=changes, input_sha256=digest(args.input),
        accepted_complete_scalar_schema=geometry['schema'],
        full_frozen_scalar_definition=geometry,
        accepted_input_final_tail_response_sha256=tail_hash,
        numerical_formula_source_sha256=FORMULA_SOURCES,
        all_original_material_and_spectral_algorithms_retained=True,
        actual_new_tail_solve_performed=False, acceptance_thresholds_changed=False,
        accepted_input_unchanged=True, full_closed_surface_certified=False,
        task_completed=False)
    artifact = original.write_json(out/'complete-scalar-adapter.json', record)
    summary_path = out/'summary.json'
    summary = json.loads(summary_path.read_text())
    summary['complete_scalar_adapter'] = artifact
    summary['accepted_input_final_tail_response_sha256'] = tail_hash
    summary['accepted_complete_scalar_schema'] = geometry['schema']
    summary['artifacts'].append(artifact)
    summary_path.write_text(json.dumps(summary, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(event='complete_scalar_material_packet_recorded',out=str(out),
        input_sha256=record['input_sha256'],scalar_schema=geometry['schema'],
        original_algorithms_retained=True,task_completed=False)),flush=True)


if __name__ == '__main__':
    main()
