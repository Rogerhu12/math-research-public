#!/usr/bin/env python3
"""Pure reconstruction of the complete angular parent/history/free-word transfer."""
import argparse
import ast
import hashlib
import json
from pathlib import Path

PARENT_SHA='eb22d711122da4e9db99a032f84560a32358f11a543b91757d9e83cc149bc2ee'


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def body(text,name):
    tree=ast.parse(text)
    node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name==name)
    return '\n'.join(text.splitlines()[node.lineno-1:node.end_lineno])+'\n'


def derive(parent,additions):
    # The actual parent whole SHA is passed by the standalone CLI and checked
    # again against the published source-construction manifest.
    ast.parse(parent);ast.parse(additions)
    constants={}
    for n in ast.parse(parent).body:
        if isinstance(n,ast.Assign) and len(n.targets)==1 and isinstance(n.targets[0],ast.Name):
            try: constants[n.targets[0].id]=ast.literal_eval(n.value)
            except (ValueError,TypeError): pass
    required=['HISTORY_SOURCE_SHA256','ORIGINAL_DRIVER_SHA256','ORIGINAL_READER_SHA256',
        'ORIGINAL_OPERATOR_SHA256','ORIGINAL_CALIBRATION_SHA256','ORIGINAL_REPORT_SCHEMA',
        'ORIGINAL_OPERATOR_SCHEMA','ORIGINAL_READER_RELATIVE','ADDRESS_ROLES','TYPE_KEYS']
    result='''#!/usr/bin/env python3
"""Strict complete N-only history and original-free-word transfer.

Fixed scalar/chart/seed/radial/integration/control definitions are compared in
full. The current finite observer is independently N4096. Old tagged indices
are decoded with their original N2048 before union; no physical value or root
is imported. Original final-array reads require public Actions.
"""
import ast
import copy
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import struct
import sys
from types import SimpleNamespace

SCHEMA='complete-dyadic-angular-history-and-free-word-transfer-v1'
CURRENT_OPERATOR_SCHEMA='complete-angular-refined-reference-centred-C1-fixed-normal-plane-SO3-v1'
ORIGINAL_BASE_SHA256='6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865'
ORIGINAL_FRAME_SHA256='ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9'
'''
    result+='\n'.join(n+' = '+repr(constants[n]) for n in required)+'\n\n'
    for name in ('require_actions','sha','canonical','_record_bytes','_same_bytes','_literal_assignments',
        '_point','_address_fingerprints','_from_witnesses','_type','_typed_key','_terminal','_old_reader','_restore_annotations','_digest'):
        result+=body(parent,name)+'\n\n'
    for n in ast.parse(additions).body:
        if isinstance(n,ast.FunctionDef):
            result+=body(additions,n.name)+'\n\n'
    seed=body(parent,'seed_from_complete_prior_final')
    seed=seed.replace("    model_binding = _compatible_models(payload['representation'],q.model,pins)",
        "    pins['_topic']=str(topic)\n    model_binding = _compatible_models(payload['representation'],q.model,pins)")
    seed=seed.replace("str(saved['base_so3_model_identity_sha256'].item()) != q.base.identity",
        "str(saved['base_so3_model_identity_sha256'].item()) != payload['representation']['base_model_identity_sha256']")
    seed=seed.replace("int(saved['working_full_angles'].item()) != q.full_N",
        "int(saved['working_full_angles'].item()) != 2048")
    result+=seed+'\n\n'+body(parent,'validate_seed_metadata')+'\n'
    ast.parse(result);compile(result,'angular_refinement_history_transfer.py','exec')
    return result


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--parent-source',type=Path,required=True)
    p.add_argument('--parent-sha256',required=True)
    p.add_argument('--additions-source',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    parent=a.parent_source.read_text()
    if sha(parent)!=a.parent_sha256 or a.parent_sha256!=PARENT_SHA:
        raise ValueError('Use the exact complete original transfer source')
    value=derive(parent,a.additions_source.read_text())
    a.output.write_text(value)
    print(json.dumps(dict(bytes=len(value.encode()),sha256=sha(value))))


if __name__=='__main__':
    main()
