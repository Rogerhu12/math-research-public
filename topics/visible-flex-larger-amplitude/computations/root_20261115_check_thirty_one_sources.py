#!/usr/bin/env python3
"""Source/byte/JSON and integer-index checks only; never import the models."""
import ast
import copy
import gzip
import hashlib
import json
from pathlib import Path

BASE = Path('/tmp/visible-larger-actual94-dispatch-sources')
OUT = Path('/tmp/visible-larger-thirty-one-source')
PARENT = Path('/tmp/visible-larger-actual94-published')
KINDS = ('domain_operator', 'condensed_warm', 'condensed_response', 'collocation_observer_warm')


def sha(raw): return hashlib.sha256(raw).hexdigest()
def filename(kind, word): return 'geometry_20261114_'+word+'_query_'+kind+'.py'
def dump(n): return ast.dump(n, include_attributes=False)
def node(root, qual):
    for part in qual.split('.'):
        root = next(x for x in root.body if isinstance(x, (ast.FunctionDef, ast.ClassDef)) and x.name == part)
    return root
def const(tree, key):
    row = next(x for x in tree.body if isinstance(x, ast.Assign) and any(
        isinstance(t, ast.Name) and t.id == key for t in x.targets))
    return ast.literal_eval(row.value)
def receipt(path):
    raw = path.read_bytes()
    return dict(file=str(path), bytes=len(raw), sha256=sha(raw))


report = dict(schema='independent31-source-and-actual94-parent-static-check-v1',
    scientific_modules_imported=False, scientific_calculation_executed=False,
    scope='AST/text, original saved JSON and byte identities; finite integer layout bookkeeping only',
    source_files=[], identical_function_AST=[])
trees = {}
for kind in KINDS:
    oldpath, newpath = BASE/filename(kind, 'twenty_eight'), OUT/filename(kind, 'thirty_one')
    old, new = ast.parse(oldpath.read_bytes()), ast.parse(newpath.read_bytes())
    compile(new, str(newpath), 'exec')
    for call in ast.walk(new):
        if isinstance(call, ast.Call):
            keys = [k.arg for k in call.keywords if k.arg is not None]
            assert len(keys) == len(set(keys)), (kind, call.lineno)
    trees[kind] = old, new
    report['source_files'].append(dict(new=receipt(newpath), original_dispatch=receipt(oldpath)))

checks = {
    'domain_operator': ['query_value', 'selected_actual_angles'],
    'condensed_warm': ['equal', 'guard', 'scalar_or_none', 'evidence', 'compact_metadata',
        '_run_engine.ObservedResidual', 'main.CapturedLinearization', 'main.project', 'main.choose'],
    'collocation_observer_warm': ['scalar', 'component', 'main.observer_write',
        'main.LocationObservedResidual', 'main.annotate_current', 'main.write'],
}
for kind, quals in checks.items():
    old, new = trees[kind]
    for qual in quals:
        assert dump(node(old, qual)) == dump(node(new, qual)), (kind, qual)
        report['identical_function_AST'].append(dict(file=kind, function=qual, identical_AST=True))


class ScopeLabels(ast.NodeTransformer):
    def visit_Constant(self, n):
        if isinstance(n.value, str):
            n.value = n.value.replace('thirty-one', 'twenty-eight')
            n.value = n.value.replace('all twenty unique captured cells', 'all eighteen unique captured cells')
            n.value = n.value.replace('twenty original left-RMS and eleven original collocation-midpoint queries',
                'eighteen original left-RMS and ten original collocation-midpoint queries')
        return n


old_domain, new_domain = trees['domain_operator']
for method in ('__init__', 'verify', 'export'):
    a = node(old_domain, 'TwentyEightQueryDomainOperator.'+method)
    b = ScopeLabels().visit(copy.deepcopy(node(new_domain, 'ThirtyOneQueryDomainOperator.'+method)))
    assert dump(a) == dump(b), method
report['complete_LEFT_and_MID_J_P_chain_constructor_AST_unchanged_except_scope_labels'] = True
report['verify_export_AST_unchanged_except_scope_labels'] = True
report['original_C_projection_call_and_returned_tuple_AST_identical'] = True

oldfd = (BASE/filename('condensed_response','twenty_eight')).read_text()
newfd = (OUT/filename('condensed_response','thirty_one')).read_text()
assert newfd.replace('thirty_one','twenty_eight').replace('thirty-one','twenty-eight') == oldfd
report['FD_full_text_reverse_identity'] = True
oldobs = (BASE/filename('collocation_observer_warm','twenty_eight')).read_text()
newobs = (OUT/filename('collocation_observer_warm','thirty_one')).read_text()
newwarmsha = sha((OUT/filename('condensed_warm','thirty_one')).read_bytes())
oldwarmsha = sha((BASE/filename('condensed_warm','twenty_eight')).read_bytes())
assert newobs.replace('thirty_one','twenty_eight').replace('thirty-one','twenty-eight').replace(newwarmsha,oldwarmsha) == oldobs
report['observer_full_text_reverse_identity_after_names_and_entry_pin'] = True

left_old, left = const(old_domain,'LEFT_INTERVALS'), const(new_domain,'LEFT_INTERVALS')
mid_old, mid = const(old_domain,'MID_INTERVALS'), const(new_domain,'MID_INTERVALS')
assert left == tuple(sorted((*left_old,464,486)))
assert mid == tuple(sorted((*mid_old,486)))
assert tuple(j for j in left if j in left_old) == left_old
assert tuple(j for j in mid if j in mid_old) == mid_old
old_queries = [('left-RMS',j) for j in left_old]+[('collocation-midpoint',j) for j in mid_old]
new_queries = [('left-RMS',j) for j in left]+[('collocation-midpoint',j) for j in mid]
assert [q for q in new_queries if q in old_queries] == old_queries
cells = sorted(set(left+mid)); oldcells = sorted(set(left_old+mid_old))
nodes = sorted(set(cells)|{j+1 for j in cells})
oldnodes = sorted(set(oldcells)|{j+1 for j in oldcells})
assert len(left)==20 and len(mid)==11 and len(cells)==20
assert nodes==list(range(464,489)) and oldnodes==list(range(465,489))
assert sorted(set(cells)-set(oldcells))==[464,486] and sorted(set(nodes)-set(oldnodes))==[464]
assert const(new_domain,'ZERO_LAYOUT_NODES')==()
layout = next(x for x in new_domain.body if isinstance(x,ast.Assign) and any(
    isinstance(t,ast.Name) and t.id=='LOCAL_LAYOUT_NODES' for t in x.targets))
assert isinstance(layout.value,ast.Name) and layout.value.id=='QUERY_ENDPOINT_NODES'
support_source = BASE/'geometry_20261114_fixed_support_halfspaces.py'
support_tree = ast.parse(support_source.read_bytes())
support_assignment = next(x for x in support_tree.body if isinstance(x,ast.Assign) and any(
    isinstance(t,ast.Name) and t.id=='FIXED_PHYSICAL_NODES' for t in x.targets))
assert dump(support_assignment.value)==dump(ast.parse('tuple(range(471,483))',mode='eval').body)
support_nodes = list(range(471,483))
oldindices = [k for j in oldnodes for k in range((j-1)*338,j*338)]
newindices = [k for j in nodes for k in range((j-1)*338,j*338)]
added_indices = sorted(set(newindices)-set(oldindices))
assert added_indices == list(range(463*338,464*338))
assert len(newindices)+3==8453 and len(oldindices)+3==8115
rows=[]
for i,(kind,j) in enumerate(new_queries):
    rows.append(dict(query_index=i,kind=kind,interval=j,
        fraction=const(new_domain,'LEFT_FRACTION') if kind=='left-RMS' else .5,
        original_query_index=old_queries.index((kind,j)) if (kind,j) in old_queries else None,
        row_start=i*2048,row_stop=(i+1)*2048,
        endpoint_nodes=[j,j+1],parent_query_retained=(kind,j) in old_queries))
report.update(query_specs_with_original_index_and_row_ranges=rows,
    original28_relative_order_preserved=True,
    only_added_queries=[q for q in rows if q['original_query_index'] is None],
    left_queries=list(left),midpoint_queries=list(mid),
    retained_left_queries=list(left_old),retained_midpoint_queries=list(mid_old),
    unique_capture_intervals=cells,unique_capture_cell_count=len(cells),
    added_capture_intervals=sorted(set(cells)-set(oldcells)),
    query_endpoint_nodes=nodes,query_endpoint_count=len(nodes),added_endpoint_nodes=[464],
    full_B_rows=len(new_queries)*2048,
    complete_B_H_local_dimension_by_literal_index_formula=len(newindices)+3,
    parent_B_H_local_dimension_by_literal_index_formula=len(oldindices)+3,
    new_original_physical_column_range_half_open=[added_indices[0],added_indices[-1]+1],
    original_p_column_range_half_open=[236033,236036],
    existing_B_local_physical_and_p_columns_shift=338,
    C_support_nodes=support_nodes,C_dimension_by_original_formula=338*len(support_nodes)+3,
    complete_B_outside_C_nodes=[j for j in nodes if j not in support_nodes],
    zero_layout_nodes=[],runtime_complete_column_union_check_retained=True,
    H_left_exterior_nodes_by_original_formula=463,H_right_exterior_nodes_by_original_formula=210,
    C_and_H_are_reformed_from_current_model_not_cached=True,
    new_matrix_values_and_domain_outcomes_not_computed=True)

newwarm = trees['condensed_warm'][1]
assert const(newwarm,'THIRTY_ONE_OPERATOR_SHA')==sha((OUT/filename('domain_operator','thirty_one')).read_bytes())
assert const(trees['collocation_observer_warm'][1],'ENTRY_SHA')==newwarmsha
assert const(new_domain,'ORIGIN_TWENTY_EIGHT_OPERATOR_SHA')==sha((BASE/filename('domain_operator','twenty_eight')).read_bytes())
assert const(new_domain,'ORIGIN_TWENTY_EIGHT_OPERATOR_NAME')==filename('domain_operator','twenty_eight')
assert not any(x in (OUT/filename('condensed_warm','thirty_one')).read_text()
    for x in ('complete_B_local_coordinates=8115','baseline_C_support_dimension=4059','ACTUAL89_'))

warm_path=PARENT/'twenty-eight-condensed-warm/warm-001.json.gz'
status_path=PARENT/'twenty-eight-condensed-warm/driver-status.json.gz'
warmraw=warm_path.read_bytes();statusstored=status_path.read_bytes();statusraw=gzip.decompress(statusstored)
assert sha(warmraw)==const(newwarm,'ACTUAL94_WARM_SHA')
assert sha(statusraw)==const(newwarm,'ACTUAL94_STATUS_SHA')
assert sha(statusstored)=='50e9075ade6d3876f229d91431fbde237e73983ab0e424004e9a0f639cafd982'
status=json.loads(statusraw);warm=json.loads(gzip.decompress(warmraw))
assert status['schema']==warm['optimization_warm']['schema']=='exact-constraint-twenty-eight-query-condensed-complete-H-warm-v1'
assert status['latest_warm_sha256']==sha(warmraw) and status['latest_warm_file']==warm_path.name
assert status['accepted_warm_steps']==1 and status['optimization_progress'] is True
assert status['success'] is False and status['new_coupled_finite_acceptance'] is False
producer=warm['optimization_warm'];parent_sources=producer['source_sha256']
for name,digest in parent_sources.items(): assert sha((BASE/name).read_bytes())==digest,name
for k,v in status['identity'].items(): assert producer[k]==v,k
report.update(source_pins_match=True,actual94_parent_pair_file_SHA_matched=True,
    parent_status_gzip_exact_decoded_bytes=True,parent_status_identity_embedded_exactly=True,
    parent_producer_schema=status['schema'],parent_mathematical_source_count=len(parent_sources),
    new_mathematical_source_count_by_preserved_source_names=len(parent_sources)+2,
    parent_warm=receipt(warm_path),parent_status=dict(file=str(status_path),
        stored_bytes=len(statusstored),stored_sha256=sha(statusstored),
        original_bytes=len(statusraw),original_sha256=sha(statusraw)),
    original_fixed_C_source=receipt(support_source),
    original_full_H_condensation_source=receipt(BASE/'root_20261114_complete_local_qp_condensation.py'),
    old_source_files_untouched=True,metadata_does_not_certify_any_new_scientific_result=True)
path=OUT/'thirty-one-source-static-check.json'
path.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(file=str(path),bytes=path.stat().st_size,sha256=sha(path.read_bytes()),
    checks_passed=True,scientific_execution=False,identical_functions=len(report['identical_function_AST']),
    parent_sources=len(parent_sources)),indent=2))
