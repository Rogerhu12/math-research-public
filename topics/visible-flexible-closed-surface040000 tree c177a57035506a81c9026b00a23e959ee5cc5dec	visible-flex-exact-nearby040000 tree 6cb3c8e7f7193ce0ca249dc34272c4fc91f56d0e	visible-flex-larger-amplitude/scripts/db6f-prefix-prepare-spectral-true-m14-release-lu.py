#!/usr/bin/env python3
"""Pure preparation of the explicit LU-lifetime true M14/N512 W14 variant.

No candidate class, saved-mesh restart, flow, RHS, Newton installation,
weighted solver factory, BVP or DN is constructed/called by this script.
"""
import argparse
import ast
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC / 'notes'
RUNNER = HERE / 'db6f-prefix-spectral-true-m14-release-lu.py'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out-prefix', type=Path, required=True)
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location('spectral_true_prepare_definitions', RUNNER)
    c = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(c)  # Definitions/NumPy only; never c.main().
    out = args.out_prefix.resolve()
    c.require(out.parent == NOTES.resolve() and not list(out.parent.glob(out.name+'*')),
              'Use a completely unused topic notes stem')
    reference = c.read(c.REFERENCE)
    c.require(c.identity(c.REFERENCE)['sha256'] == c.REFERENCE_SHA, 'Changed frozen original source bundle')
    seed, prior, port = c.h.validate_inputs(reference)
    auditor = c.module('spectral_true_prepare_closed_seed_schema', HERE/'db6f-prefix-audit-spectral-true-m14-release-lu.py')
    original_tail_check = auditor.check_packet(reference['frozen_tail']['path'], prior['request']['height'],
                                               True, {'config': prior['config'], 'prior': prior})
    bindings = {row['path']: row for row in reference['bindings']}
    for p in (c.REFERENCE, RUNNER, Path(__file__).resolve(),
              HERE / 'db6f-prefix-audit-spectral-true-m14-release-lu.py',
              NOTES / '2026-11-09-db6f-prefix-spectral-true-m14-interface.md',
              NOTES / '2026-11-09-db6f-prefix-spectral-true-m14-interface-sources.json',
              NOTES / '2026-11-09-db6f-tail-review-spectral-true-m14-interface.md',
              NOTES / '2026-11-09-db6f-prefix-spectral-true-m14-implementation.md',
              c.ORIGINAL_ENTRY, HERE/'db6f-prefix-prepare-spectral-true-m14.py',
              HERE/'db6f-prefix-audit-spectral-true-m14.py',
              c.LIFETIME_SELECTOR, c.LIFETIME_NEWTON,
              HERE/'db6f-prefix-check-domain-newton-release-lu.py',
              NOTES/'2026-11-09-db6f-prefix-newton-release-lu-method.md',
              NOTES/'2026-11-09-db6f-prefix-newton-release-lu-sources.json',
              NOTES/'2026-11-09-db6f-prefix-newton-release-lu-protocol.json',
              NOTES/'2026-11-09-db6f-prefix-newton-release-lu-observed-validation.json',
              NOTES/'2026-11-09-db6f-prefix-spectral-true-m14-release-lu-implementation.md'):
        row = c.identity(p); bindings[row['path']] = row

    source_scripts = Path(reference['source_root'])/'topics/large-amplitude-twist-flex/scripts'
    search_roots = [source_scripts, NOTES, HERE]
    included_main = {RUNNER.resolve(), (HERE/'db6f-prefix-coupled.py').resolve()}
    pending = [Path(row['path']) for row in bindings.values() if Path(row['path']).suffix == '.py']
    visited, unresolved = set(), set()
    skipped = []
    while pending:
        path = pending.pop().resolve()
        if path in visited:
            continue
        visited.add(path)
        row = c.identity(path); bindings[row['path']] = row
        names = set()
        def imports(node):
            if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)) and node.name == 'main' and path not in included_main:
                skipped.append({'path':str(path),'function':'main','line':node.lineno,
                                'scope':'Unused dependency CLI entry in the actual true-selector call graph; whole source remains bound.'})
                return
            if isinstance(node,ast.Import):
                names.update(v.name.split('.')[0] for v in node.names)
            elif isinstance(node,ast.ImportFrom) and node.module and not node.level:
                names.add(node.module.split('.')[0])
            for child in ast.iter_child_nodes(node):
                imports(child)
        imports(ast.parse(path.read_text(),filename=str(path)))
        for name in names:
            found = next((root/(name+'.py') for root in search_roots if (root/(name+'.py')).is_file()),None)
            if found is not None:
                pending.append(found)
            elif name.startswith(('f6','curve_','construct_','fixed_metric_','repo_scan_')):
                unresolved.add(name)
    c.require(not unresolved,'Unbound local Python dependency: '+', '.join(sorted(unresolved)))
    # Unlike the affine preparation, this call graph includes the original
    # coupled main(), which constructs the actual shared tail client.
    c.require((HERE/'db6f-prefix-coupled.py').resolve() in visited, 'Original actual coupled main is not bound')
    callbacks = dict(reference['callbacks'])
    for key,(path,qualname) in c.EXTRA_CALLBACK_DEFINITIONS.items():
        callbacks[key] = c.h.source_function(path,qualname)
    for row in callbacks.values():
        c.equal(bindings.get(row['file']['path']),row['file'],'Callback file is not in the source closure')

    cfg = c.expected_config(reference,out)
    cfg_path = Path(str(out)+'-tail-config.json')
    cfg_bytes = (json.dumps(cfg,indent=2,ensure_ascii=False,allow_nan=False)+'\n').encode()
    cfg_binding = {'path':str(cfg_path),'bytes':len(cfg_bytes),'sha256':hashlib.sha256(cfg_bytes).hexdigest()}
    bindings[str(cfg_path)] = cfg_binding
    launch_path = Path(str(out)+'-launch.json')
    prep_path = Path(str(out)+'-preparation.json')
    launch = {'schema':'db6f-spectral-true-m14q512-release-lu-v1','status':'PREPARED_NOT_STARTED',
              'scope':c.SCOPE,'settings':c.SETTINGS,'reference_preparation':c.identity(c.REFERENCE),
              'launch_path':str(launch_path),'out_prefix':str(out),'tail_config':cfg_binding,
              'source_checkpoint':reference['checkpoint'],'own_actual_tail_warm':reference['frozen_tail'],
              'frozen_physical_fields':reference['frozen_physical_fields'],
              'source_root':reference['source_root'],'callbacks':callbacks,
              'weights':[1.]+[float(1<<(9*j*j).bit_length()) for _ in range(3) for j in range(1,15)],
              'command':[sys.executable,str(RUNNER),'--launch',str(launch_path)],'cwd':str(c.REPO),
              'delegated_parser_argv':c.expected_parser_argv(reference,cfg_path,out),
              'stdout_log':str(out)+'-run.log','reproduction_file':str(out)+'-reproduction.json',
              'original_summary_file':str(out)+'-summary.json','checkpoint_output':str(out)+'.json.gz',
              'first_request_binding':str(out)+'-first-request-binding.json',
              'coefficient_output_pattern':str(out)+'_coeff_*.npy.gz',
              'newton_lifetime_definitions':c.module('pure_lu_lifetime_metadata',c.LIFETIME_SELECTOR).definitions(
                  Path(reference['callbacks']['domain_solve_newton']['file']['path'])),
              'runtime_newton_gate':'Before first BVP, require original installed f6 Newton, explicitly select the separately bound one-statement LU-lifetime variant and preserve the exact original STATS object; every BVP records/checks the selected identity before and after. Pure preparation installs nothing.',
              'physical_BC_scope':'The weighted callable checks inner affine-DN physical-coordinate BC; the unchanged actual outer checks pay the nonlinear BC.',
              'included_runtime_cli_main_sources':sorted(str(p) for p in included_main),
              'excluded_unused_dependency_cli_entries':sorted(skipped,key=lambda r:r['path']),
              'bindings':sorted(bindings.values(),key=lambda r:r['path'])}
    c.validate_inputs(launch,planned_config=cfg)
    # All input/source validation precedes writing these three small metadata
    # files. There is no new CP, PPoly, DN response or positive future fixture.
    c.write_json(cfg_path,cfg,exclusive=True)
    c.write_json(launch_path,launch,exclusive=True)
    report = {'status':'PREPARED_ONLY_NO_CANDIDATE_INITIALIZATION_NO_SOLVER','scope':__doc__,
              'launch':c.identity(launch_path),'tail_config':c.identity(cfg_path),
              'source_checkpoint':reference['checkpoint'],'own_actual_tail_warm':reference['frozen_tail'],
              'original_warm_residual':prior['response']['residual'],'bindings':len(bindings),
              'old_actual_tail_metadata_check':original_tail_check,
              'original_reference_bindings':len(reference['bindings']),'callback_definitions':len(callbacks),
              'visited_python_sources':len(visited),'included_actual_coupled_main':True,
              'new_state_components':43,'new_free_parameters':14,'new_central_scales':13,
              'new_tail_Jacobian_entries':616,'original_settings':c.SETTINGS,
              'operations':{'candidate_objects':0,'restart_calls':0,'flow_calls':0,'RHS_calls':0,
                            'Newton_install_calls':0,'weighted_solver_factory_calls':0,'BVP_calls':0,'DN_calls':0},
              'runtime_identity_status':'NOT_RUN; remains a gate in the future actual selector',
              'future_tool_exit_status':'NOT_STARTED; only root may provide an actual tool observation'}
    c.write_json(prep_path,report,exclusive=True)
    print(json.dumps({'status':report['status'],'bindings':len(bindings),'callbacks':len(callbacks),
                      'launch':c.identity(launch_path),'preparation':c.identity(prep_path),
                      'config':c.identity(cfg_path),'new_solver_calls':0},indent=2))


if __name__=='__main__':
    main()
