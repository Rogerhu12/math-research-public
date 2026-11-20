#!/usr/bin/env python3
"""Prepare/run a genuine finer full-Phi solve from one refinement report.

Derives a separately identified driver from the frozen original or R671
driver. The only semantic edits are: exact binary tuple location keys,
and explicit pure-location JSON structure instead of a byte-size cutoff.
No old running source is modified. Numerical solving requires public Actions.
"""
import argparse
import ast
import hashlib
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys


REFINEMENT_SHA = '2e8ae99813c105982b10b896606538c1c42baf0abf089457412b32e265d4411a'
BASES = {
    'original': ('fullclosed_gauss_inequality_qp.py',
        '5ef7e26834b55d97d2c2dfc2d82f0113b2e072b2f46d3d54f04978177ce0629a'),
    'R671': ('fullclosed_gauss_exact_tail_inequality_qp.py',
        'b1b0725acffde7958d9a4ad245057ea243d4319bde15bd9a7778ade3b0f844e8'),
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def same_ast(left, right):
    return ast.dump(left, include_attributes=False) == ast.dump(right, include_attributes=False)


class ExactLocationDriver(ast.NodeTransformer):
    def __init__(self):
        self.function = None
        self.removed_size_checks = 0
        self.exact_key_replacements = 0
        self.position_schema_insertions = 0
        self.size_test = ast.parse('witness_path.stat().st_size > 100000', mode='eval').body

    def visit_FunctionDef(self, node):
        old, self.function = self.function, node.name
        node = self.generic_visit(node)
        if node.name == 'load_witnesses':
            # The payload assignment lives inside the source-file loop.
            for loop in [n for n in ast.walk(node) if isinstance(n, ast.For)]:
                new_body = []
                for statement in loop.body:
                    new_body.append(statement)
                    if (isinstance(statement, ast.Assign)
                            and any(isinstance(t, ast.Name) and t.id == 'payload' for t in statement.targets)):
                        new_body.extend(ast.parse(
                            "if not isinstance(payload, dict) or payload.get('schema') != 'immutable-curvature-history-locations-v1':\n"
                            "    raise ValueError('Fine solver consumes explicit immutable position manifests')\n"
                            "for point_key in ('curvature_points','radius_points','protected_curvature_points'):\n"
                            "    positions = payload.get(point_key, [])\n"
                            "    if not isinstance(positions, list) or any(not isinstance(p, (list,tuple)) or len(p) != 3 for p in positions):\n"
                            "        raise ValueError('Every permanent position must be a cell/u/phi triple')\n"
                        ).body)
                        self.position_schema_insertions += 1
                loop.body = new_body
        self.function = old
        return node

    def visit_If(self, node):
        if self.function == 'load_witnesses' and same_ast(node.test, self.size_test):
            self.removed_size_checks += 1
            return None
        return self.generic_visit(node)

    def visit_Call(self, node):
        node = self.generic_visit(node)
        if self.function not in ('load_witnesses', 'add_actual_location'):
            return node
        if (not isinstance(node.func, ast.Name) or node.func.id != 'round'
                or len(node.args) != 2 or not isinstance(node.args[1], ast.Constant)
                or node.args[1].value != 13):
            return node
        value = node.args[0]
        if (not isinstance(value, ast.Call) or not isinstance(value.func, ast.Name)
                or value.func.id != 'float' or len(value.args) != 1):
            return node
        subscript = value.args[0]
        if (isinstance(subscript, ast.Subscript) and isinstance(subscript.value, ast.Name)
                and subscript.value.id in ('value', 'old') and isinstance(subscript.slice, ast.Constant)
                and subscript.slice.value in ('u', 'phi')):
            self.exact_key_replacements += 1
            return ast.copy_location(value, node)
        return node


def derive_driver(base, destination):
    original = Path(base).read_text()
    tree = ast.parse(original, filename=str(base))
    transform = ExactLocationDriver()
    tree = ast.fix_missing_locations(transform.visit(tree))
    changes = dict(removed_arbitrary_size_checks=transform.removed_size_checks,
        round13_keys_replaced_by_exact_binary_keys=transform.exact_key_replacements,
        pure_position_schema_insertions=transform.position_schema_insertions)
    if changes != dict(removed_arbitrary_size_checks=1,
                       round13_keys_replaced_by_exact_binary_keys=6, pure_position_schema_insertions=1):
        raise ValueError('The bound frozen driver no longer has the declared exact edit sites')
    provenance = dict(frozen_driver_path=str(Path(base).resolve()),
        frozen_driver_sha256=sha(base), derivation_source_sha256=sha(__file__), **changes,
        mathematical_objective_changed=False, numerical_linear_solver_changed=False,
        geometry_and_all_native_residual_rows_retained=True,
        exact_duplicate_locations_may_merge=True, distinct_binary_locations_may_merge=False)
    text = ('#!/usr/bin/env python3\n# Explicit fixed-g refinement driver derivation:\n# '
            +json.dumps(provenance, sort_keys=True)+'\n'+ast.unparse(tree)+'\n')
    destination = Path(destination)
    if destination.exists() and destination.read_text() != text:
        raise FileExistsError('Use a new derived-driver path for different bytes')
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(text)
    return dict(path=str(destination.resolve()), sha256=sha(destination),
                bytes=destination.stat().st_size, derivation=provenance)


def replace(command, flag, value):
    if command.count(flag) != 1:
        raise ValueError('Expected one explicit driver argument: '+flag)
    command[command.index(flag)+1] = str(value)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('repo', 'work', 'refinement-report', 'outdir'):
        p.add_argument('--'+key, type=Path, required=True)
    p.add_argument('--damping', type=float, required=True)
    p.add_argument('--directions', type=int, default=1)
    p.add_argument('--maxiter', type=int, default=256)
    p.add_argument('--active-rows', type=int, default=192)
    p.add_argument('--qp-rtol', type=float, default=1e-6)
    p.add_argument('--qp-atol', type=float, default=1e-12)
    p.add_argument('--stage-block', type=int, default=64)
    p.add_argument('--coarse-centers')
    p.add_argument('--print-command', action='store_true')
    a = p.parse_args()
    repo, work = a.repo.resolve(), a.work.resolve()
    a.outdir = a.outdir.resolve()
    value = json.loads(a.refinement_report.read_text())
    if value.get('source_sha256') != REFINEMENT_SHA:
        raise ValueError('Use the declared exact symbolic/same-g refinement source report')
    outputs = value['outputs']
    inputs = value['inputs']
    for entry in [outputs[key] for key in ('bundle','carrier','node_report','permanent_locations')]+[inputs['scalar_input']]:
        if sha(entry['path']) != entry['sha256']:
            raise ValueError('The actual finer solve input changed: '+entry['path'])
    source = repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261120'
    refinement_source = source/'refine_fixed_g_fullclosed.py'
    if sha(refinement_source) != REFINEMENT_SHA:
        raise ValueError('Use the exact refinement/common-parent-grid reader source')
    is_tail = value['refined_model'].get('schema') == 'R671-exact-reference-tail-lift-v1'
    kind = 'R671' if is_tail else 'original'
    basename, expected = BASES[kind]
    base = source/basename
    if sha(base) != expected:
        raise ValueError('The original/full-R671 solver version differs from its explicit derivation')
    launcher = source/('launch_full_phi_exact_tail_actions.py' if is_tail else 'launch_full_phi_qp_actions.py')
    prepare = [sys.executable, str(launcher), '--repo', str(repo), '--work', str(work),
        '--bundle', outputs['bundle']['path'], '--carrier', outputs['carrier']['path'],
        '--manifest', outputs['permanent_locations']['path'], '--outdir', str(a.outdir),
        '--damping', str(a.damping), '--directions', str(a.directions),
        '--maxiter', str(a.maxiter), '--active-rows', str(a.active_rows),
        '--qp-rtol', str(a.qp_rtol), '--qp-atol', str(a.qp_atol), '--print-command']
    if a.coarse_centers is not None:
        prepare.extend(['--coarse-centers', a.coarse_centers])
    if is_tail:
        definition = value['refined_model']
        prepare.extend(['--node-report', outputs['node_report']['path'],
            '--scalar-input', inputs['scalar_input']['path'],
            '--eta-start-node', str(definition['eta_start_node']),
            '--lambda-value', str(definition['lambda_value']),
            '--source-lambda', str(definition['lambda_value']), '--migration', 'keep-q'])
    prepared = subprocess.run(prepare, check=True, capture_output=True, text=True)
    command = shlex.split(prepared.stdout.strip())
    if len(command) < 3 or Path(command[2]).resolve() != base.resolve():
        raise ValueError('Frozen launcher returned another complete-field driver')
    derived = derive_driver(base, work/'refinement-driver-sources'/(a.outdir.name+'-'+basename))
    command[2] = derived['path']
    replace(command, '--angles', value['angular_refinement']['refined_full_angles'])
    replace(command, '--stage-block', a.stage_block)
    common_command = [sys.executable, str(refinement_source), 'read-common',
        '--repo', str(repo), '--refinement-report', str(a.refinement_report.resolve()),
        '--bundle', str(a.outdir/'final.npz'), '--out', str(a.outdir/'common-parent-grid.json'),
        '--stage-block', str(a.stage_block)]
    plan = dict(schema='same-fixed-g-finer-full-Phi-solve-plan-v1',
        source_sha256=sha(__file__), refinement_report=dict(path=str(a.refinement_report.resolve()),
            sha256=sha(a.refinement_report)), derived_driver=derived,
        frozen_launcher=dict(path=str(launcher), sha256=sha(launcher)), command=command,
        common_parent_grid_command=common_command,
        exact_permanent_location_keys=True, arbitrary_manifest_size_limit_removed=True,
        scalar_and_parameter_range_unchanged=True, radial_frequency_refinement=value['transfer'],
        nonlinear_solve_started=False, convergence_claimed=False,
        comparison='Read the actual solved fine field on parent rows, parent angles, parent positive weights and parent a carriers; changed fine-grid Phi is not subtracted from coarse Phi; transfer/re-read alone is not convergence')
    work.mkdir(parents=True, exist_ok=True)
    plan_path = work/(a.outdir.name+'-fine-command.json')
    if plan_path.exists():
        raise FileExistsError('Use a fresh actual fine-solve command record')
    plan_path.write_text(json.dumps(plan, indent=2, allow_nan=False)+'\n')
    if a.print_command:
        print(shlex.join(command))
        return
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Actual finer scientific solving requires the public repository Actions')
    if a.outdir.exists():
        raise FileExistsError('Do not overwrite an earlier numerical budget')
    plan.update(nonlinear_solve_started=True, execution={key: os.environ.get(key)
        for key in ('GITHUB_REPOSITORY','GITHUB_RUN_ID','GITHUB_RUN_ATTEMPT','GITHUB_SHA')})
    plan_path.write_text(json.dumps(plan, indent=2, allow_nan=False)+'\n')
    env = os.environ.copy()
    env.update(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1',
               PYTHONDONTWRITEBYTECODE='1')
    subprocess.run(command, cwd=repo, env=env, check=True)
    final = a.outdir/'final.npz'
    returned = json.loads((a.outdir/'report.json').read_text())
    if returned.get('final_bundle_sha256') != sha(final):
        raise ValueError('The completed fine solver report does not identify its actual final field')
    plan.update(nonlinear_solve_returned=True,
        final_bundle=dict(path=str(final), sha256=sha(final)),
        solver_report=dict(path=str(a.outdir/'report.json'), sha256=sha(a.outdir/'report.json')),
        convergence_claimed=False)
    plan_path.write_text(json.dumps(plan, indent=2, allow_nan=False)+'\n')
    subprocess.run(common_command, cwd=repo, env=env, check=True)
    common_path = a.outdir/'common-parent-grid.json'
    plan['common_parent_grid_report'] = dict(path=str(common_path), sha256=sha(common_path))
    plan_path.write_text(json.dumps(plan, indent=2, allow_nan=False)+'\n')


if __name__ == '__main__':
    main()

