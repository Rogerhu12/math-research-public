#!/usr/bin/env python3
"""Generate separately named M15/N512 continuation entry sources only.

No numerical candidate or solver. All original files are retained bytewise.
Every literal replacement is counted and a full unified diff is published.
Handwritten input/closed-control gates are separately bound by preparation.
"""
import ast
import difflib
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
NOTES = HERE.parent/'notes'
LEDGER = NOTES/'2026-11-10-78718-numerical-m15-linear-generated-sources-v1.json'
DIFF = NOTES/'2026-11-10-78718-numerical-m15-linear-generated-sources-v1.diff'
ROWS = []
DIFFS = []


def identity(path):
    data = path.read_bytes()
    return {'path': str(path.resolve()), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def functions(text):
    result = {}
    def walk(body, prefix=''):
        for node in body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                name = prefix+node.name
                if not isinstance(node, ast.ClassDef):
                    result[name] = ast.dump(node, include_attributes=False)
                walk(node.body, name+('.' if isinstance(node, ast.ClassDef) else '.<locals>.'))
    walk(ast.parse(text).body)
    return result


def emit(old_name, new_name, changes):
    old, new = HERE/old_name, HERE/new_name
    text = original = old.read_text()
    edits = []
    for before, after, count in changes:
        actual = text.count(before)
        if actual != count:
            raise ValueError((new_name, 'replacement_count', before, actual, count))
        text = text.replace(before, after)
        edits.append({'before': before, 'after': after, 'count': count})
    ast.parse(text)
    with new.open('x') as stream:
        stream.write(text)
    a, b = functions(original), functions(text)
    ROWS.append({'ancestor': identity(old), 'derived': identity(new), 'literal_edits': edits,
                 'functions_AST_unchanged': sorted(k for k in a.keys() & b.keys() if a[k] == b[k]),
                 'functions_AST_changed': sorted(k for k in a.keys() & b.keys() if a[k] != b[k]),
                 'functions_added': sorted(b.keys()-a.keys()), 'functions_removed': sorted(a.keys()-b.keys())})
    DIFFS.extend(difflib.unified_diff(original.splitlines(True), text.splitlines(True),
                                     fromfile=old_name, tofile=new_name))


def main():
    if LEDGER.exists() or DIFF.exists():
        raise FileExistsError('Fresh generation ledger required')
    emit('db6f-prefix-tail-linear-continuation-client-v2.py',
         '78718-prefix-tail-linear-m15q512-v1.py', [
        ('Bounded physical-height continuation around the FROZEN original DN client.',
         'New M15/N512 identity for the frozen bounded physical-height DN control.', 1),
        ("'db6f-physical-height-continuation-v2'", "'78718-m15q512-physical-height-continuation-v1'", 1),
        ("'steps': 32, 'quadrature': 256, 'maxIterations': 36,",
         "'steps': 32, 'quadrature': 512, 'maxIterations': 36,", 1),
        ("        require(canonical(without_io(self.seed['config'])) == canonical(without_io(self.cfg)),\n                'Bootstrap config differs beyond the original five I/O keys')",
         "        require(self.seed['config']['quadrature'] == 256 and self.cfg['quadrature'] == 512,\n                'Only the declared old-N256 to new-N512 warm transition is allowed')\n        require(canonical(dict(without_io(self.seed['config']), quadrature=512)) == canonical(without_io(self.cfg)),\n                'Bootstrap differs beyond five I/O keys and declared angular quadrature')", 1),
        ("            require(canonical(without_io(self.parameters)) == canonical(without_io(seed_parameters)),\n                    'New runtime/seed physical and numerical parameter identity changed')",
         "            require(seed_parameters['quadrature'] == 256 and self.parameters['quadrature'] == 512,\n                    'Wrong old/new angular quadrature in actual runtime parameters')\n            require(canonical(without_io(self.parameters)) == canonical(dict(without_io(seed_parameters), quadrature=512)),\n                    'New runtime changed a parameter outside the declared N512 warm transition')", 1),
        ("'db6f-linear-dn-closed-request-pilot-v2'", "'78718-m15q512-linear-dn-closed-request-pilot-v1'", 1),
    ])
    emit('db6f-prefix-flat-linear-continuation-coupled-v2.py',
         '78718-prefix-flat-linear-m15q512-v1.py', [
        ("HERE = Path(__file__).resolve().parent", "HERE = Path(__file__).resolve().parent\nOLD_HERE = Path('/workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface/scripts')", 1),
        ("HERE / 'db6f-prefix-flat-coupled.py'", "OLD_HERE / 'db6f-prefix-flat-coupled.py'", 1),
        ('original_module = runner.module', 'original_module = runner.module\nselected_control_module = None', 1),
        ('    file = Path(file)\n', '    global selected_control_module\n    file = Path(file)\n', 1),
        ("(HERE / 'db6f-prefix-tail-shared-client.py').resolve()", "(OLD_HERE / 'db6f-prefix-tail-shared-client.py').resolve()", 1),
        ("        return original_module(name, HERE / 'db6f-prefix-tail-linear-continuation-client-v2.py')",
         "        selected_control_module = original_module(name, HERE / '78718-prefix-tail-linear-m15q512-v1.py')\n        return selected_control_module", 1),
    ])
    emit('78718-prefix-spectral-restart8000-v1.py',
         '78718-prefix-spectral-m15-linear-v1.py', [
        ('New restart8000 / typed-code identity of the actual-DN M14 W14 runner.',
         'New M15/N512/W15 actual-DN runner with bounded physical-height continuation.', 1),
        ("ORIGINAL = HERE / 'db6f-prefix-flat-coupled.py'", "ORIGINAL = NEW_HERE / '78718-prefix-flat-linear-m15q512-v1.py'", 1),
        ('M = 14', 'M = 15', 1),
        ("SETTINGS = {'modes': 14,", "SETTINGS = {'modes': 15,", 1),
        ("78718-prefix-restart8000-inputs-v1.py", "78718-prefix-m15-linear-inputs-v1.py", 1),
        ("78718-prefix-audit-restart8000-v1.py", "78718-prefix-audit-m15-linear-v1.py", 1),
        ("(HERE/'db6f-prefix-tail-shared-client.py','WeightedTailPort.solve')",
         "(NEW_HERE/'78718-prefix-tail-linear-m15q512-v1.py','WeightedTailPort.solve')", 1),
        ("(HERE/'db6f-prefix-tail-shared-client.py','WeightedTailPort.close')",
         "(NEW_HERE/'78718-prefix-tail-linear-m15q512-v1.py','WeightedTailPort.close')", 1),
        ("runner = module('spectral_true_original_flat_runner', ORIGINAL).m",
         "wrapper = module('spectral_true_m15_controlled_flat_runner', ORIGINAL)\n        runner = wrapper.runner", 1),
        ("            obj, checked = runtime_callbacks(fun, bc, kwargs, context)",
         "            obj, checked = runtime_callbacks(fun, bc, kwargs, context)\n            control_runtime = i.check_actual_control_module(wrapper.selected_control_module, launch)", 1),
        ("'physical_callbacks': checked,", "'physical_callbacks': checked, 'control_runtime_callbacks': control_runtime,", 1),
        ("                first_packet = Path(str(out) + '_tail_0001.json.gz')",
         "                good = read(launch['continuation_policy_fields']['last_good_file'])\n                require(good['policy_sha256'] == launch['continuation_policy']['sha256'], 'Wrong actual control policy')\n                first_packet = Path(good['packet']['path'])\n                verify(good['packet'])", 1),
        ("# Original equations, main, tail client, callback/outer/final gates remain.",
         "# Original equations/main/physical gates remain; the explicit new DN control is recorded.", 1),
        ('RESTART8000_FINITE_M14_COUPLED_PROGRAM', 'M15_LINEAR_FINITE_COUPLED_PROGRAM', 3),
        ('Runtime W14 differs', 'Runtime W15 differs', 1),
        ('Unexpected original fixed M14 callback owner', 'Unexpected original fixed M15 callback owner', 1),
        ('# Explicit W14, release-LU', '# Explicit W15, release-LU', 1),
    ])
    emit('78718-prefix-audit-restart8000-v1.py',
         '78718-prefix-audit-m15-linear-v1.py', [
        ('New read-only close audit for restart8000 and complete typed runtime code.',
         'New read-only M15/N512 close audit, full control replay and typed runtime code.', 1),
        ('78718-prefix-spectral-restart8000-v1.py', '78718-prefix-spectral-m15-linear-v1.py', 2),
        ('M, TOL = 14, 2e-9', 'M, TOL = 15, 2e-9', 1),
        ("context['prior']['source_sha256'], 'Original shared eight-source identity differs'",
         "context['launch']['continuation_policy_fields']['source_sha256'], 'Actual nine-source continuation identity differs'", 1),
        ("len(record['source_sha256']) == 8, 'Expected eight original shared sources'",
         "len(record['source_sha256']) == 9, 'Expected eight original trial sources plus new continuation source'", 1),
        ("c.without_io(context['prior']['response']['checkpoint']['parameters'])",
         "c.without_io(context['expected_tail_parameters'])", 1),
        ("vector(response['heightJetJacobian'], 616)", "vector(response['heightJetJacobian'], 705)", 1),
        ('616-entry Jacobian', '705-entry Jacobian', 1),
        ("'Jacobian_entries': 616", "'Jacobian_entries': 705", 1),
        ('vector(row, 28)', 'vector(row, 30)', 2),
        ('865 by 28', '865 by 30', 1),
        ('[865,28]', '[865,30]', 1),
        ('[13,28]', '[13,30]', 1),
        ('state == 43', 'state == 46', 1),
        ('all 43 states', 'all 46 states', 1),
        ('value.shape == (43,1)', 'value.shape == (46,1)', 1),
        ("('state_components',43)", "('state_components',46)", 1),
        ("('parameters',14)", "('parameters',15)", 1),
        ('dict(modes=14,', 'dict(modes=15,', 1),
        ("vector(cp['parameters'],14) and vector(cp['central_correction_scales'],13)",
         "vector(cp['parameters'],15) and vector(cp['central_correction_scales'],14)", 1),
        ("packet = Path(str(out) + '_tail_0001.json.gz')",
         "packet = Path(first['packet']['path'])\n    require(packet.parent == out.parent and packet.name.startswith(out.name + '_tail_') and\n            packet.name.endswith('.json.gz') and packet.name[len(out.name)+6:-8].isdigit(),\n            'First actual target packet is outside this run')", 1),
        ("equal(seam['angular_samples'], 896", "equal(seam['angular_samples'], 960", 1),
        ("        for key, entry in call['physical_callbacks'].items():",
         "        c.i.check_control_runtime_record(call['control_runtime_callbacks'], context['launch'])\n        for key, entry in call['physical_callbacks'].items():", 1),
        ("    unique = {row['path']: row for row in required_files}",
         "    control_reader = c.module('m15_closed_control_replay', c.NEW_HERE/'78718-audit-m15-linear-control-v1.py')\n    control = control_reader.audit(context, cp['tail_calls'])\n    required_files += control['required_closed_files']\n    unique = {row['path']: row for row in required_files}", 1),
        ("'first_actual_DN':first,'coefficients':polynomial", "'control_replay':control,'first_actual_DN':first,'coefficients':polynomial", 1),
        ('PASS_RESTART8000_FINITE_M14_PROGRAM_OUTPUTS', 'PASS_M15_LINEAR_FINITE_PROGRAM_OUTPUTS', 1),
        ('RESTART8000_FINITE_M14_COUPLED_PROGRAM_SUCCESS', 'M15_LINEAR_FINITE_COUPLED_PROGRAM_SUCCESS', 1),
        ('PASS_ROOT_OBSERVED_RESTART8000_M14_W14_FINITE_COUPLED_CLOSE', 'PASS_ROOT_OBSERVED_M15_N512_W15_LINEAR_DN_FINITE_COUPLED_CLOSE', 1),
        ('PASS_FIRST_ACTUAL_M14_DN_ONLY', 'PASS_FIRST_ACTUAL_M15_TARGET_DN_ONLY', 1),
        ('finite M14', 'finite M15', 1),
        ('M14 cut jets', 'M15 cut jets', 1),
        ('M14 seam', 'M15 seam', 1),
    ])
    emit('78718-prepare-restart8000-guard-v1.py', '78718-prepare-m15-linear-guard-v1.py', [
        ('78718-prefix-spectral-restart8000-v1.py', '78718-prefix-spectral-m15-linear-v1.py', 1),
        ('78718-restart8000-resource-bound-command-v1', '78718-m15-linear-resource-bound-command-v1', 1),
        ('frozen restart8000 launch', 'frozen M15 linear-DN launch', 1),
    ])
    emit('78718-check-restart8000-runtime-v1.py', '78718-check-m15-linear-runtime-v1.py', [
        ('78718-prefix-spectral-restart8000-v1.py', '78718-prefix-spectral-m15-linear-v1.py', 1),
        ('78718-prefix-audit-restart8000-v1.py', '78718-prefix-audit-m15-linear-v1.py', 1),
        ('78718-restart8000-runtime-identity-check-v1', '78718-m15-linear-runtime-identity-check-v1', 1),
    ])
    emit('db6f-prefix-test-linear-dn-protocol-v2.py', '78718-check-m15-linear-protocol-v1.py', [
        ('db6f-prefix-tail-linear-continuation-client-v2.py', '78718-prefix-tail-linear-m15q512-v1.py', 2),
    ])
    DIFF.open('x').write(''.join(DIFFS))
    report = {'schema': '78718-m15-linear-source-derivation-v1',
              'status': 'SOURCES_GENERATED_ONLY_NO_NUMERICAL_RUN', 'builder': identity(Path(__file__)),
              'files': ROWS, 'full_diff': identity(DIFF), 'solver_calls': 0,
              'handwritten_gates': ['78718-prefix-m15-linear-inputs-v1.py',
                  '78718-prefix-prepare-m15-linear-v1.py', '78718-audit-m15-linear-control-v1.py']}
    LEDGER.open('x').write(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'status': report['status'], 'files': len(ROWS),
                      'ledger': identity(LEDGER), 'diff': identity(DIFF), 'solver_calls': 0}))


if __name__ == '__main__':
    main()
