#!/usr/bin/env python3
"""Pure complete derivation/binding of the direct backtracked-SOC successor.

The entire direct 359f body and entire 892f policy body are read by exact SHA.
Only the declared schema, source documentation, explicit norm/self-policy
restart guards, policy metadata and complete original-ray/SOC selection block
change. Every original physical function and local field/geometry read remains
AST-identical. No numerical module, F, J, endpoint root or scientific array is
imported, constructed or evaluated by this source.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path

PARENT_DRIVER_SHA = '359ffc94df1b33485c2cda4de0f5662ef7bc802c588f583a023fcd5723a7872d'
PARENT_LAUNCHER_SHA = 'faf5f67000eb81a0bc6d26126641f10c606a879f935158222b1fce0f50525d02'
POLICY_DRIVER_SHA = '892f349b140f9a77fde37fc490d7cbb078cfdb21f8b31b7743e50ec6cf5712a8'
HELPER_SHA = '02875e4a150644f8addb6073b346e2de3b0f3cf50498e9cf6efe8fe0333d7c97'
PROJECTION_SHA = 'a2c6d334d40be88ac7edb2dd2e525da5583d9f723e33d5bae9d910c0adfe745e'
SCHEMA = 'complete-independent-axisymmetric-fixed-deep-so3-backtracked-separation-SOC-v1'
DERIVED_DRIVER_SHA = '450a4341ba425544ccb641094e242bb332563835c567af4062a62e278a6647a6'
DERIVED_LAUNCHER_SHA = 'b550dcffdaffd993f89ee493c82bcc96b9e680428262230ddb546cf688eb1c20'
OLD_BEGIN = '        # Keep this one parent residual-Hessian alive: a corrected full z\n'
POLICY_BEGIN = '        # Keep this one original-parent residual-Hessian alive. A corrected\n'
REGION_END = "        if soc_helper is not None:\n            record['final_complete_SOC_cache'] = soc_helper.cache_state()\n"
DRIVER_PATCHES = [
  [
    "\"\"\"Complete prior-separation and same-parent SOC for the actual SO3 field.\n\nThis is an independently declared representation.  All rotation modes and\nshared-quintic jets, all formerly free core coefficients, and H are used.\nThe explicit closure lift is inside every Gram and geometric derivative.\nThe exact old 192-row selection is retained through a genuine new-field\nadapter, and its prefix is followed by the complete selected amplitude\nrows.  A common-slack Phase I is a numerical restoration, never a proof\nthat a residual slack is geometrically feasible.\n\"\"\"",
    "\"\"\"Complete direct axisymmetric SO3 QP with a true backtracked SOC anchor.\n\nThe physical 7f field, all original rotation/core/H variables, full H2\ncoordinates, positive metric rows, original geometric selection, amplitude\nrows and complete permanent-memory screens are unchanged. This independent\nsource first finds a truly feasible original ray, then corrects the closest\nlarger eligible rejected ray at the SAME original parent. Candidate choice\nrequires a fresh full-memory reread. The normalized-parent cache/model and\ninterior Phase I of the policy source are not imported.\n\"\"\""
  ],
  [
    "SCHEMA = 'complete-independent-axisymmetric-fixed-deep-so3-prior-separation-and-SOC-v1'",
    "SCHEMA = 'complete-independent-axisymmetric-fixed-deep-so3-backtracked-separation-SOC-v1'"
  ],
  [
    "                or restart.get('observation_carrier_sha256') != sha(args.carrier)):",
    "                or restart.get('observation_carrier_sha256') != sha(args.carrier)\n                or restart.get('coordinate_norm', {}).get('norm_identity_sha256') != coordinates.record['norm_identity_sha256']):"
  ],
  [
    "                raise ValueError('A same-SOC continuation must retain this full body and every true source role')\n",
    "                raise ValueError('A same-SOC continuation must retain this full body and every true source role')\n            prior_soc = restart.get('complete_same_parent_SOC', {})\n            if prior_soc.get('anchor_policy') != 'closest-eligible-larger-ray-after-first-true-feasible-ray':\n                raise ValueError('Keep the declared complete post-ray immutable-anchor correction policy')\n            for key, expected in (('maximum_rounds', args.soc_rounds),\n                    ('tau', args.soc_tau),\n                    ('observed_violation_inward_fraction', args.soc_inward_fraction),\n                    ('numerical_readback_tolerance', args.soc_feasibility_tolerance)):\n                if prior_soc.get(key) != expected:\n                    raise ValueError('Continue the same explicitly bound complete SOC policy: '+key)\n"
  ],
  [
    "            numerical_finite_projection_is_not_a_geometric_certificate=True),",
    "            numerical_finite_projection_is_not_a_geometric_certificate=True,\n            anchor_policy='closest-eligible-larger-ray-after-first-true-feasible-ray',\n            all_original_ray_backtracking_precedes_SOC=True,\n            true_feasible_original_ray_fallback_required_before_SOC=True,\n            fallback_never_accepted_before_final_memory_readback=True,\n            one_immutable_anchor_per_original_parent_direction=True,\n            candidate_choice_policy='ascending previously-read same-Phi, then complete current-memory revalidation',\n            failed_post_SOC_candidates_resume_remaining_original_ray_budget=True),"
  ]
]


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for part in iter(lambda: stream.read(1048576), b''):
            h.update(part)
    return h.hexdigest()


def sha_text(value):
    return hashlib.sha256(value.encode()).hexdigest()


def validate_source(value, filename):
    tree = ast.parse(value, filename=filename)
    compile(tree, filename, 'exec')
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            keys = [key.value for key in node.keys if isinstance(key, ast.Constant)
                and isinstance(key.value, (str, int, float))]
            if len(keys) != len(set(keys)):
                raise ValueError('Repeated literal dictionary key at '+str(node.lineno))
    if any(line.rstrip() != line for line in value.splitlines()):
        raise ValueError('Do not hide trailing source whitespace')
    return tree


def source_pins(value):
    tree = ast.parse(value)
    nodes = [node for node in tree.body if isinstance(node, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == 'SOURCE_PINS'
            for target in node.targets)]
    if len(nodes) != 1:
        raise ValueError('Keep exactly one complete literal source-role registry')
    return ast.literal_eval(nodes[0].value)


def replace_once(value, old, new):
    if value.count(old) != 1:
        raise ValueError('A complete declared source replacement is absent or ambiguous')
    return value.replace(old, new, 1)


def region(value, start):
    if value.count(start) != 1 or value.count(REGION_END) != 1:
        raise ValueError('The complete same-parent ray/SOC block is absent or ambiguous')
    begin = value.index(start)
    end = value.index(REGION_END, begin)
    return begin, end, value[begin:end]


def unchanged_functions(before, after):
    old, new = ast.parse(before), ast.parse(after)
    a = {node.name: node for node in old.body if isinstance(node, (ast.FunctionDef, ast.ClassDef))}
    b = {node.name: node for node in new.body if isinstance(node, (ast.FunctionDef, ast.ClassDef))}
    if set(a) != set(b):
        raise ValueError('The full original direct interface set changed')
    for name in a:
        if name != 'main' and ast.dump(a[name]) != ast.dump(b[name]):
            raise ValueError('An original direct field/norm/history/Phase-I interface changed: '+name)
    nested_a = {node.name: node for node in a['main'].body if isinstance(node, ast.FunctionDef)}
    nested_b = {node.name: node for node in b['main'].body if isinstance(node, ast.FunctionDef)}
    if set(nested_a) != set(nested_b):
        raise ValueError('A local complete field/metric/geometry function was dropped')
    for name in nested_a:
        if ast.dump(nested_a[name]) != ast.dump(nested_b[name]):
            raise ValueError('An original full local scientific read changed: '+name)


def derive_driver(parent, policy, helper):
    if (sha_text(parent) != PARENT_DRIVER_SHA or sha_text(policy) != POLICY_DRIVER_SHA
            or sha_text(helper) != HELPER_SHA):
        raise ValueError('Bind all three complete published source bodies by exact bytes')
    value = parent
    for old, new in DRIVER_PATCHES:
        value = replace_once(value, old, new)
    a, b, old_region = region(value, OLD_BEGIN)
    _, _, complete_policy = region(policy, POLICY_BEGIN)
    value = value[:a]+complete_policy+value[b:]
    validate_source(helper, 'complete_axisymmetric_so3_rows_soc.py')
    validate_source(value, 'fullclosed_axisymmetric_so3_backtracked_soc.py')
    unchanged_functions(parent, value)
    if source_pins(value) != source_pins(parent):
        raise ValueError('A direct physical/norm/QP/geometry source role was changed or relabeled')
    if sha_text(value) != DERIVED_DRIVER_SHA:
        raise ValueError('The complete direct derived body differs from its declared literal bytes')
    return value


def derive_launcher(parent, complete_driver):
    if sha_text(parent) != PARENT_LAUNCHER_SHA or sha_text(complete_driver) != DERIVED_DRIVER_SHA:
        raise ValueError('Bind the entire old direct launcher and entire new body')
    value = replace_once(parent, "DRIVER_SHA = '"+PARENT_DRIVER_SHA+"'",
        "DRIVER_SHA = '"+DERIVED_DRIVER_SHA+"'")
    value = replace_once(value, 'fullclosed_axisymmetric_so3_separation_soc.py',
        'fullclosed_axisymmetric_so3_backtracked_soc.py')
    value = replace_once(value, 'public-actions-complete-independent-axisymmetric-SO3-separation-SOC-command-v1',
        'public-actions-complete-independent-axisymmetric-SO3-backtracked-SOC-command-v1')
    value = replace_once(value, 'Prepare or execute the complete independent axisymmetric-reference SO3 QP, with explicit CPU runtime.',
        'Prepare or execute the complete direct axisymmetric SO3 backtracked-SOC QP.')
    validate_source(value, 'launch_axisymmetric_so3_backtracked_soc.py')
    if sha_text(value) != DERIVED_LAUNCHER_SHA:
        raise ValueError('The full derived launcher differs from its declared bytes')
    return value


def bind_report(repo, report_path):
    topic = Path(repo).resolve()/'topics/visible-flex-larger-amplitude'
    directory = topic/'scripts/resume_20261126'
    parent = directory/'fullclosed_axisymmetric_so3_separation_soc.py'
    policy = directory/'fullclosed_so3_cached_interior_separation_soc.py'
    helper = directory/'complete_axisymmetric_so3_rows_soc.py'
    derived = directory/'fullclosed_axisymmetric_so3_backtracked_soc.py'
    expected = derive_driver(parent.read_text(), policy.read_text(), helper.read_text())
    if derived.read_text() != expected or sha(derived) != DERIVED_DRIVER_SHA:
        raise ValueError('The entire actual direct source differs from its complete declared derivation')
    report_path = Path(report_path).resolve()
    before = sha(report_path)
    report = json.loads(report_path.read_text())
    if report.get('schema') != SCHEMA or report.get('source_sha256') != DERIVED_DRIVER_SHA:
        raise ValueError('This report belongs to another complete source or physical wrapper')
    pins = source_pins(expected)
    if report.get('source_sha256_by_role') != {role: value[1] for role, value in pins.items()}:
        raise ValueError('The exact full source-role set differs from the true direct registry')
    for role, (relative, digest) in pins.items():
        if sha(topic/relative) != digest:
            raise ValueError('Changed actual complete direct report source role '+role)
    if sha(report_path) != before:
        raise ValueError('The actual complete report changed during pure source binding')
    return dict(actual_driver_sha256=DERIVED_DRIVER_SHA,
        actual_driver_schema=SCHEMA, actual_entire_body_match=True,
        complete_direct_parent_driver_sha256=PARENT_DRIVER_SHA,
        copied_complete_backtracked_policy_source_sha256=POLICY_DRIVER_SHA,
        policy_source_normalized_parent_model_or_cache_imported=False,
        unchanged_full_direct_source_registry=True,
        all_original_top_level_and_local_physical_functions_AST_equal=True,
        complete_SOC_helper_sha256=HELPER_SHA, projection_sha256=PROJECTION_SHA,
        explicit_same_coordinate_norm_restart_guard=True,
        actual_source_commit=report.get('source_commit'),
        physical_model_identity_sha256=report.get('model_identity_sha256'),
        raw_scientific_arrays_recomputed=False, field_calls=0, J_calls=0,
        geometric_feasibility_or_convergence_inferred=False)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--original-driver', type=Path, required=True)
    p.add_argument('--policy-driver', type=Path, required=True)
    p.add_argument('--original-launcher', type=Path, required=True)
    p.add_argument('--helper', type=Path, required=True)
    p.add_argument('--outdir', type=Path, required=True)
    p.add_argument('--verify-existing', action='store_true')
    a = p.parse_args()
    complete_driver = derive_driver(a.original_driver.read_text(),
        a.policy_driver.read_text(), a.helper.read_text())
    complete_launcher = derive_launcher(a.original_launcher.read_text(), complete_driver)
    a.outdir.mkdir(parents=True, exist_ok=True)
    for name, value in (
            ('fullclosed_axisymmetric_so3_backtracked_soc.py', complete_driver),
            ('launch_axisymmetric_so3_backtracked_soc.py', complete_launcher)):
        path = a.outdir/name
        if a.verify_existing:
            if path.read_text() != value:
                raise ValueError('Existing complete generated source differs: '+str(path))
        else:
            if path.exists():
                raise FileExistsError('Do not overwrite an existing complete source: '+str(path))
            path.write_text(value)
    print(json.dumps(dict(complete=True, pure_source_derivation=True,
        numerical_sources_imported=False, scientific_execution=False,
        source_sha256=sha(__file__), driver_sha256=DERIVED_DRIVER_SHA,
        launcher_sha256=DERIVED_LAUNCHER_SHA, helper_sha256=HELPER_SHA,
        policy_source_sha256=POLICY_DRIVER_SHA,
        complete_driver_bytes=len(complete_driver.encode()),
        complete_launcher_bytes=len(complete_launcher.encode())),
        sort_keys=True, allow_nan=False))


if __name__ == '__main__':
    main()
