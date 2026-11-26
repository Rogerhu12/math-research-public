#!/usr/bin/env python3
"""Pure source derivation: freeze the actual verified parent profile for SO3.

No scientific input, field, derivative, or fixture is evaluated.  The
complete original driver/launcher/reader are required by their byte SHA.
All full SO3 field, J/J*, QP, geometry, amplitude and Phase-I bodies remain.
"""
import argparse
import ast
import hashlib
from pathlib import Path
import re

ORIGINAL = {
    'fullclosed_so3_meridian_qp.py': '9cf5c8259426cc6130651d60728e96a9c26820baaa10e5c23f22440c5a0a7b4b',
    'launch_so3_closed_meridian_actions.py': '9b770c78813ca081beb903d81dad0426110003ac4ec2ee89e1e5d5f4a8816f26',
    'read_so3_closed_meridian_report.py': '32bdbb6e60f60ed169bfccae64bd90d20dc17cd9ee3f38fd03a62e1c907a6361',
}
NEW_DRIVER = 'fullclosed_so3_actual_profile_qp.py'
NEW_LAUNCHER = 'launch_so3_actual_profile_actions.py'
NEW_READER = 'read_so3_actual_profile_report.py'
BINDER = 'so3_same_parent_fixed_scalar_binding.py'
NEW_SCHEMA = 'complete-actual-fixed-deep-parent-closed-so3-meridian-QP-v1'


def sha_text(text):
    return hashlib.sha256(text.encode()).hexdigest()


def replace_once(text, before, after):
    if text.count(before) != 1:
        raise ValueError('Source derivation anchor changed: '+repr(before[:90]))
    return text.replace(before, after, 1)


def replace_function(text, name, replacement):
    node = next(node for node in ast.parse(text).body
        if isinstance(node, ast.FunctionDef) and node.name == name)
    lines = text.splitlines(keepends=True)
    return ''.join(lines[:node.lineno-1])+replacement.rstrip()+'\n'+''.join(lines[node.end_lineno:])


def derive(repo, binder_path, output):
    source = Path(repo)/'topics/visible-flex-larger-amplitude/scripts/resume_20261126'
    old = {}
    for name, wanted in ORIGINAL.items():
        text = (source/name).read_text()
        if sha_text(text) != wanted:
            raise ValueError('Need the exact original complete source '+name)
        old[name] = text
    binder_hash = hashlib.sha256(Path(binder_path).read_bytes()).hexdigest()
    driver = old['fullclosed_so3_meridian_qp.py']
    driver = replace_once(driver,
        "SCHEMA = 'complete-fixed-deep-closed-so3-meridian-QP-v1'",
        "SCHEMA = '"+NEW_SCHEMA+"'")
    driver = replace_once(driver,
        "FIXED_PROFILE = '383168fbd269d52a16586fca626632c28243bf230df62a5882e7ed2048625d7d'\n", '')
    driver = replace_once(driver, "SOURCE_PINS = {\n", "SOURCE_PINS = {\n"
        +"    'actual_parent_binding': ('scripts/resume_20261126/"+BINDER+"', '"+binder_hash+"'),\n")
    driver = replace_function(driver, 'actual_parent', """def actual_parent(args, paths):
    binder = load('_so3_actual_same_parent_input_binding', paths['actual_parent_binding'])
    return binder.bind_actual_parent(args, paths)
""")
    driver = replace_once(driver,
        "    parent_report, parent_binding = actual_parent(args, paths)\n",
        "    parent_report, parent_binding = actual_parent(args, paths)\n"
        "    # Freeze the actual canonical target once, before constructing any new field.\n"
        "    fixed_profile = parent_binding['fixed_scalar_target']['identity_sha256']\n"
        "    actual_binding = load('_so3_actual_rebuilt_context_binding', paths['actual_parent_binding'])\n")
    driver = driver.replace('FIXED_PROFILE', 'fixed_profile')
    driver = replace_once(driver,
        "    if (context.deep.model_identity_sha256 != fixed_profile\n",
        "    rebuilt_parent_binding = actual_binding.bind_rebuilt_context(context, parent_report, parent_binding)\n"
        "    if (context.deep.model_identity_sha256 != fixed_profile\n")
    driver = replace_once(driver,
        "        frozen_parent_binding=parent_binding, frozen_parent_affine=affine,\n",
        "        frozen_parent_binding=parent_binding, rebuilt_parent_context_binding=rebuilt_parent_binding,\n"
        "        frozen_parent_affine=affine,\n")
    driver = replace_once(driver,
        '"""Full closed SO(3) meridian optimization of one fixed deep scalar g.',
        '"""Full closed SO(3) meridian optimization of the ACTUAL fixed deep parent g.')
    driver_hash = sha_text(driver)

    launcher = old['launch_so3_closed_meridian_actions.py']
    launcher = replace_once(launcher, "DRIVER_SHA = '"+ORIGINAL['fullclosed_so3_meridian_qp.py']+"'",
        "DRIVER_SHA = '"+driver_hash+"'")
    launcher = replace_once(launcher, "driver = source/'fullclosed_so3_meridian_qp.py'",
        "driver = source/'"+NEW_DRIVER+"'")
    launcher = launcher.replace("public-actions-complete-closed-SO3-command-v1",
        "public-actions-actual-fixed-parent-closed-SO3-command-v1")
    # Emit the genuine child traceback in the parent log rather than allowing
    # a final CalledProcessError wrapper to hide the already printed exception.
    launcher = replace_once(launcher,
        "    subprocess.run(command, env=env, cwd=args.repo, check=True)\n",
        "    actual = subprocess.run(command, env=env, cwd=args.repo, check=False)\n"
        "    if actual.returncode:\n"
        "        raise SystemExit(actual.returncode)\n")

    reader = old['read_so3_closed_meridian_report.py']
    reader = replace_once(reader, "DRIVER_SHA = '"+ORIGINAL['fullclosed_so3_meridian_qp.py']+"'",
        "DRIVER_SHA = '"+driver_hash+"'")
    reader = replace_once(reader, "REPORT_SCHEMA = 'complete-fixed-deep-closed-so3-meridian-QP-v1'",
        "REPORT_SCHEMA = '"+NEW_SCHEMA+"'")
    reader = replace_once(reader,
        "PROFILE_SHA = '383168fbd269d52a16586fca626632c28243bf230df62a5882e7ed2048625d7d'\n", '')
    reader = replace_once(reader, 'import hashlib\n', 'import hashlib\nimport importlib.util\nimport sys\n')
    reader = replace_once(reader, "driver = topic/'scripts/resume_20261126/fullclosed_so3_meridian_qp.py'",
        "driver = topic/'scripts/resume_20261126/"+NEW_DRIVER+"'")
    reader = replace_once(reader, 'def statistic(value):', 'def statistic(value, fixed_profile):')
    reader = replace_once(reader, 'def direction(value):', 'def direction(value, fixed_profile):')
    reader = reader.replace('PROFILE_SHA', 'fixed_profile')
    reader = replace_once(reader, '    model = report[\'representation\']\n',
        "    binding_relative, binding_sha = load_pins(driver)['actual_parent_binding']\n"
        "    binding_path = topic/binding_relative\n"
        "    spec = importlib.util.spec_from_file_location('_SO3_pure_actual_profile_binding', binding_path)\n"
        "    binder = importlib.util.module_from_spec(spec)\n"
        "    sys.modules[spec.name] = binder\n"
        "    spec.loader.exec_module(binder)\n"
        "    fixed_profile = binder.verify_saved_binding(report, expected_binding_source_sha256=binding_sha)\n"
        "    model = report['representation']\n")
    reader = replace_once(reader,
        "        starting_statistics=statistic(value['starting_statistics']),",
        "        starting_statistics=statistic(value['starting_statistics'], fixed_profile),")
    reader = replace_once(reader,
        "        accepted_statistics=statistic(value.get('accepted_statistics')),",
        "        accepted_statistics=statistic(value.get('accepted_statistics'), fixed_profile),")
    reader = replace_once(reader,
        "    initial, final = statistic(report.get('initial')), statistic(report.get('final_statistics'))",
        "    initial, final = statistic(report.get('initial'), fixed_profile), statistic(report.get('final_statistics'), fixed_profile)")
    reader = reader.replace('[direction(value) for value in report.get(', '[direction(value, fixed_profile) for value in report.get(')
    reader = replace_once(reader,
        "    for trial in value['trials']:\n",
        "    for trial in value['trials']:\n"
        "        if trial.get('statistics') is not None:\n"
        "            statistic(trial['statistics'], fixed_profile)\n")
    reader = reader.replace('actual-complete-fixed-deep-SO3-scalar-readout-v1',
        'actual-complete-actual-fixed-parent-SO3-scalar-readout-v1')
    result = {NEW_DRIVER: driver, NEW_LAUNCHER: launcher, NEW_READER: reader}
    for name, text in result.items():
        tree = ast.parse(text)
        compile(text, name, 'exec')
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                names = [key.arg for key in node.keywords if key.arg is not None]
                if len(names) != len(set(names)):
                    raise ValueError('Duplicate actual keyword in '+name)
        if '383168fbd269d52a16586fca626632c28243bf230df62a5882e7ed2048625d7d' in text:
            raise ValueError('Do not leave the old unrelated actual profile digest in the new entry')
    # All original driver functions except the input binder/main retain
    # precisely their original ASTs, including full C/slack and full history.
    old_tree, new_tree = ast.parse(old['fullclosed_so3_meridian_qp.py']), ast.parse(driver)
    old_functions = {n.name: ast.dump(n, include_attributes=False) for n in old_tree.body
        if isinstance(n, (ast.FunctionDef, ast.ClassDef))}
    for node in new_tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name not in ('main', 'actual_parent'):
            if ast.dump(node, include_attributes=False) != old_functions[node.name]:
                raise ValueError('Unintended full scientific helper change '+node.name)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    for name, text in result.items():
        path = output/name
        path.write_text(text)
        print(name, len(text.encode()), sha_text(text))
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, required=True)
    p.add_argument('--binder-source', type=Path, required=True)
    p.add_argument('--output-directory', type=Path, required=True)
    args = p.parse_args()
    derive(args.repo, args.binder_source, args.output_directory)


if __name__ == '__main__':
    main()
