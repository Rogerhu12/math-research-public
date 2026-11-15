#!/usr/bin/env python3
"""Build a distinct fixed-eta source by literal edits; never import science."""
from pathlib import Path
import ast
import difflib
import hashlib
import json

HERE = Path(__file__).resolve().parent
COMP = Path('/workspace/scratch/visible-larger-recovered-20261114-1843/math-research-public/topics/visible-flex-larger-amplitude/computations')
BASELINE = 'geometry_20261115_small_core_inexact_p3_restoration.py'
BASELINE_SHA = 'ce93a364f8423c89e9e696e1e2c96662b61c6daaf225bd51c44fcd572e05654e'
ENTRY = 'geometry_20261115_small_core_inexact_p3_eta_0p01.py'
SCHEMA = 'R278-original-three-equation-inexact-p3-restoration-LM-eta0p01-v1'
ACTUAL = Path('/tmp/visible-larger-recovery-2207/actions-debug/visible-mainline-smallcoreresonance-43676647334-1')
PARENT = ACTUAL/'small-core-inexact-p3-restoration/inexact-p3-restoration-status.json'
PARENT_SHA = 'd55b5338880cabaae44bd7575db9a10bcba22fad4ae1fce0225f1ef38064f331'

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def receipt(path):
    raw = Path(path).read_bytes()
    return dict(file=str(path), bytes=len(raw), sha256=digest(raw))

original = (COMP/BASELINE).read_bytes()
assert len(original) == 45133 and digest(original) == BASELINE_SHA
parent_raw = PARENT.read_bytes()
assert len(parent_raw) == 233256 and digest(parent_raw) == PARENT_SHA
parent = json.loads(parent_raw)
assert parent['source_sha256'] == BASELINE_SHA
assert parent['schema'] == 'R278-original-three-equation-inexact-p3-restoration-LM-v1'

changes = [
    ('"""Actual inexact p3 restoration and full-residual linear Schur elimination.\n',
     '"""Independent fixed-eta=0.01 inexact p3 restoration from actual97.\n\n'
     'The complete mathematical functions are retained byte-for-byte from the\n'
     'frozen ce93 producer. Its fixed-eta=0.1 entry is not executed or modified.\n'
     'This distinct entry fixes eta=0.01 and binds the genuine actual97 parent\n'
     'or a completed output of this exact new producer and its full closure.\n'),
    ("ENTRY_NAME = '"+BASELINE+"'", "ENTRY_NAME = '"+ENTRY+"'"),
    ("SCHEMA = 'R278-original-three-equation-inexact-p3-restoration-LM-v1'",
     "SCHEMA = '"+SCHEMA+"'"),
    ("PREVIOUS_SCHEMA = 'R278-original-three-equation-approximate-p3-inner-root-LM-v1'\n"
     "ACTUAL92_STATUS_SHA256 = 'e822be884ac07e2b2c46ac7aba7f589ba5233e86cdbb33ad9c95108cc8dca01e'\n"
     'ACTUAL92_STATUS_BYTES = 498765\n',
     "BASELINE_NAME = '"+BASELINE+"'\n"
     "BASELINE_SCHEMA = 'R278-original-three-equation-inexact-p3-restoration-LM-v1'\n"
     "BASELINE_SHA256 = '"+BASELINE_SHA+"'\n"
     "ACTUAL97_STATUS_SHA256 = '"+PARENT_SHA+"'\n"
     'ACTUAL97_STATUS_BYTES = 233256\n'),
    ('FROZEN = {\n', 'FROZEN = {\n    BASELINE_NAME: BASELINE_SHA256,\n'),
    ("    if parent.get('schema') == PREVIOUS_SCHEMA:\n"
     '        if len(decoded) != ACTUAL92_STATUS_BYTES or decoded_sha != ACTUAL92_STATUS_SHA256:\n'
     "            raise ValueError('The first parent is the complete genuine actual92 final status')\n"
     '        expected_sources = FROZEN\n'
     '        expected_producer = FROZEN[PREVIOUS_NAME]\n'
     "        origin = 'actual92 completed approximate-p3-root final accepted candidate'\n",
     "    if parent.get('schema') == BASELINE_SCHEMA:\n"
     '        if len(decoded) != ACTUAL97_STATUS_BYTES or decoded_sha != ACTUAL97_STATUS_SHA256:\n'
     "            raise ValueError('The first parent is the complete genuine actual97 ce93 final status')\n"
     '        expected_sources = FROZEN\n'
     '        expected_producer = BASELINE_SHA256\n'
     "        origin = 'actual97 completed ce93 eta0.1 final accepted candidate; new producer fixes eta0.01'\n"
     "        if parent.get('last_accepted_point_semantics') != 'original-three-merit-accepted-candidate-or-fresh-parent':\n"
     "            raise ValueError('The genuine actual97 parent retains its declared final-point semantics')\n"),
    ('    if not math.isfinite(damping) or damping != .1:\n'
     "        raise ValueError('This independent producer declares the single positive outer damping 0.1')\n",
     '    if not math.isfinite(damping) or damping != .01:\n'
     "        raise ValueError('This independent producer declares the single positive outer damping 0.01')\n"),
    ("            immutable_parent_provenance_only=[PREVIOUS_NAME, RESUME_NAME, 'geometry_20261115_small_core_damped_search.py'],\n"
     '            new_algorithm=ENTRY_NAME),\n',
     "            immutable_parent_provenance_only=[BASELINE_NAME, PREVIOUS_NAME, RESUME_NAME, 'geometry_20261115_small_core_damped_search.py'],\n"
     '            new_algorithm=ENTRY_NAME),\n'
     '        algorithm_baseline_source_sha256=BASELINE_SHA256,\n'
     '        mathematical_function_bodies_unchanged_from_baseline=True,\n'
     '        baseline_producer_not_imported_or_executed=True,\n'
     '        independent_fixed_damping_producer_not_an_unchanged_old_entry=True,\n'),
]

text = original.decode()
records = []
for i, (old, new) in enumerate(changes):
    assert text.count(old) == 1, (i, text.count(old))
    text = text.replace(old, new, 1)
    records.append(dict(index=i, old=old, new=new))
raw = text.encode()
target = HERE/ENTRY
target.write_bytes(raw)

# Explicit inverse of every declared edit recovers the entire immutable source.
recovered = text
for old, new in reversed(changes):
    assert recovered.count(new) == 1
    recovered = recovered.replace(new, old, 1)
assert recovered.encode() == original
tree_old = ast.parse(original, filename=BASELINE)
tree_new = ast.parse(raw, filename=ENTRY)
compile(tree_new, ENTRY, 'exec')
old_defs = {n.name:n for n in tree_old.body if isinstance(n,(ast.FunctionDef,ast.ClassDef))}
new_defs = {n.name:n for n in tree_new.body if isinstance(n,(ast.FunctionDef,ast.ClassDef))}
assert old_defs.keys() == new_defs.keys()
checks = []
for name, old_node in old_defs.items():
    new_node = new_defs[name]
    old_segment = ast.get_source_segment(original.decode(), old_node)
    new_segment = ast.get_source_segment(text, new_node)
    same_ast = ast.dump(old_node, include_attributes=False) == ast.dump(new_node, include_attributes=False)
    same_text = old_segment == new_segment
    if name not in ('checked_parent', 'main'):
        assert same_ast and same_text, name
    checks.append(dict(name=name, AST_unchanged=same_ast, complete_body_bytes_unchanged=same_text,
                       declared_identity_or_entry_change=name in ('checked_parent','main')))

# Literal constant resolution only: no import of either producer or numerical code.
def literal(node, known):
    if isinstance(node,ast.Name): return known[node.id]
    if isinstance(node,ast.Dict): return {literal(k,known):literal(v,known) for k,v in zip(node.keys,node.values)}
    return ast.literal_eval(node)
known = {}
for node in tree_new.body:
    if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name):
        try: known[node.targets[0].id] = literal(node.value,known)
        except (ValueError,KeyError,TypeError): pass
assert known['FROZEN'] == parent['consumed_source_sha256']
assert len(known['FROZEN']) == 13
assert known['ORIGINAL_INPUTS'] == parent['input_sha256']
new_closure = {**known['FROZEN'], ENTRY:digest(raw)}
assert len(new_closure) == 14
assert known['SCHEMA'] != parent['schema']
assert 'BASELINE_NAME' not in ast.get_source_segment(text,new_defs['original_module'])
assert 'ACTUAL92_STATUS' not in text and 'PREVIOUS_SCHEMA' not in text

(HERE/'producer-from-ce93.diff').write_text(''.join(difflib.unified_diff(
    original.decode().splitlines(True),text.splitlines(True),
    fromfile='frozen-ce93/'+BASELINE,tofile='request99/'+ENTRY)))
(HERE/'actual97-original').mkdir(exist_ok=True)
(HERE/'actual97-original/inexact-p3-restoration-status.json').write_bytes(parent_raw)
report = dict(schema='request99-fixed-eta-producer-source-only-check-v1',status='PASS-source-only',
    original_source=receipt(COMP/BASELINE),new_source=receipt(target),
    actual97_status=receipt(PARENT),actual97_parent_copy=receipt(HERE/'actual97-original/inexact-p3-restoration-status.json'),
    full_original_source_inverse_recovered=True,declared_literal_edits=records,
    top_level_function_and_class_checks=checks,
    original_parent_source_closure=known['FROZEN'],original_parent_source_count=13,
    new_producer_source_closure=new_closure,new_producer_source_count=14,
    original_four_input_dictionary_unchanged=True,
    first_parent_is_fixed_genuine_actual97=True,own_schema_continuation_branch_retained=True,
    own_schema_uses_new14_closure_not_old13=True,
    fixed_old_damping='0.1',fixed_new_damping='0.01',
    old_producer_preserved_and_not_imported_or_executed=True,
    AST_and_compile_only_passed=True,scientific_module_imported=False,
    mathematical_function_executed=False,local_scientific_computation=False,
    repository_or_Git_modified=False,workflow_dispatched=False)
(HERE/'request99-producer-source-only-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(source=receipt(target),static_check=receipt(HERE/'request99-producer-source-only-check.json'),
    parent_source_count=13,new_source_count=14,unchanged_function_count=sum(x['complete_body_bytes_unchanged'] for x in checks)),indent=2))
