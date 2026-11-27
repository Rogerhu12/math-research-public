#!/usr/bin/env python3
"""Source-only construction of the complete N4096 analytic pure binding."""
import argparse
import ast
import hashlib
import json
from pathlib import Path

PARENT_SHA='f34fcafc06b50594b7a651a90e38553ea8ae3da5b6ac8b6ca4ea691d2ab9f14f'
READER_SHA='c2a6039633dbb397bdb6f56358153a362ed4e34c8e035a6a739eb23d5a1b785e'
NORMAL_SCHEMA='complete-angular-refined-reference-centred-analytic-J3-fixed-normal-plane-SO3-v1'
SNAPSHOT_SCHEMA='actual-angular-refined-analytic-J3-normal-current-point-snapshot-v1'
NAMES={
    'analytic_J3':'angular_refined_analytic_normal_stage_jacobian.py',
    'frame_C1':'angular_refined_analytic_frame_c1.py',
    'stage_matrices':'angular_refined_analytic_stage_matrices.py',
    'adjacent_matrices':'angular_refined_analytic_adjacent_matrices.py',
    'reference_calibration':'angular_refined_analytic_calibration.py',
    'endpoint':'so3_angular_refined_analytic_normal_lift.py'}


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def body(text,name):
    node=next(n for n in ast.parse(text).body if isinstance(n,ast.FunctionDef) and n.name==name)
    return '\n'.join(text.splitlines()[node.lineno-1:node.end_lineno])+'\n'


def assign(text,name,value):
    node=next(n for n in ast.parse(text).body if isinstance(n,ast.Assign)
        and len(n.targets)==1 and isinstance(n.targets[0],ast.Name) and n.targets[0].id==name)
    lines=text.splitlines(keepends=True)
    return ''.join(lines[:node.lineno-1])+name+' = '+repr(value)+'\n'+''.join(lines[node.end_lineno:])


def once(text,old,new):
    if text.count(old)!=1:
        raise ValueError('Exact complete-source change missing or repeated '+old[:80])
    return text.replace(old,new)


def derive(parent,reader,additions,generated):
    if sha(parent)!=PARENT_SHA or sha(reader)!=READER_SHA:
        raise ValueError('Use both complete actual original binding and pure reader')
    result=once(parent,'import hashlib\n','import hashlib\nimport importlib.util\nimport sys\n')
    result=assign(result,'SCHEMA','complete-angular-refined-analytic-J3-source-model-and-report-binding-v1')
    result=assign(result,'OPERATOR_SCHEMA',NORMAL_SCHEMA)
    result=assign(result,'ROOT_SNAPSHOT_SCHEMA',SNAPSHOT_SCHEMA)
    result=assign(result,'BASE_SOURCE_SHA256','1ba446d9283891cfbb8d3af319a27804b4889f4b7f5f2891dea0b101aa042529')
    bindings={role:(name,sha((generated/name).read_text())) for role,name in NAMES.items()}
    result=assign(result,'SOURCE_BINDINGS',bindings)
    replacement='\n\n'.join(body(additions,n.name).rstrip() for n in ast.parse(additions).body if isinstance(n,ast.FunctionDef))+'\n'
    result=once(result,body(result,'compatible_legacy_model'),replacement)
    result=once(result,'    policies=_policies(directory)\n',
        "    _observer(directory).validate_base_model(model['base_complete_model'])\n    policies=_policies(directory)\n")
    result=once(result,'        latest_actual_diagnostics=actual,\n',
        '        latest_actual_diagnostics=actual,\n'
        '        angular_observation=angular_observation_binding(report,roles=roles,source_directory=source_directory),\n')
    result+='\n\n'+body(reader,'independent_chart_binding')
    ast.parse(result);compile(result,'angular_refined_analytic_source_binding.py','exec')
    if len(result.encode())>=100000:
        raise ValueError('Keep the complete pure source below 100KB')
    return result


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--parent-source',type=Path,required=True)
    p.add_argument('--parent-reader',type=Path,required=True)
    p.add_argument('--additions-source',type=Path,required=True)
    p.add_argument('--generated-directory',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    value=derive(a.parent_source.read_text(),a.parent_reader.read_text(),a.additions_source.read_text(),a.generated_directory)
    a.output.write_text(value)
    print(json.dumps(dict(bytes=len(value.encode()),sha256=sha(value))))


if __name__=='__main__':
    main()
