#!/usr/bin/env python3
"""Complete source-only N refinement of the actual independent fixed-chart consumer."""
import argparse
import ast
import hashlib
import json
from pathlib import Path

PARENT_SHA='4d92ca2387523a76bbea0a3444e0665c306369dd0351c3354c998a09884e043b'


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def once(text,old,new):
    if text.count(old)!=1:
        raise ValueError('Exact source change missing or repeated: '+old[:100])
    return text.replace(old,new)


ADDITIONS='''
def _observation_module():
    path=Path(__file__).with_name('angular_observation_refinement.py')
    if sha(path)!=OBSERVATION_SOURCE_SHA256:
        raise ValueError('The complete dyadic observer source changed')
    name='_full_dyadic_observer_memory_'+OBSERVATION_SOURCE_SHA256
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module


def _walk_at_declared_N(points,payload,history,carrier_path,*,label,default_N=None):
    declared=payload.get('N',payload.get('full_angles',payload.get('full_N',default_N))) if isinstance(payload,dict) else default_N
    indexed=_indexed_grid(payload)
    if declared is None:
        if indexed:
            raise ValueError('An indexed history must declare its original full N')
        declared=4096
    if type(declared) is not int or declared not in (2048,4096):
        raise ValueError('Only the explicitly bound original or refined observer may supply indexed history')
    source=history.Locations(923,7377,declared)
    source.walk(payload,path=(label,'declared_N_'+str(declared)))
    resolved=source.resolve_grid(carrier_path)
    arrays=source.arrays()
    # Arrays contain explicit literal phi; no original tagged index is walked
    # with the new N. Role/protected arrays are copied in their entirety.
    points.walk(arrays,path=(label,'complete_literal_role_arrays'))
    return dict(declared_full_N=declared,resolved_grid_positions=resolved,
        complete_literal_role_fingerprints=_fingerprint(arrays),
        old_indices_reinterpreted=False)

'''


def derive(text,observer):
    if sha(text)!=PARENT_SHA:
        raise ValueError('The entire independent fixed-chart 4d92 consumer is required')
    result=text
    result=result.replace("SCHEMA = 'complete-independent-fixed-chart-material-envelope-memory-and-typed-policy-v1'",
        "SCHEMA = 'complete-angular-refined-independent-fixed-chart-material-envelope-memory-v1'")
    result=result.replace("SCAN_SCHEMA = 'complete-independent-fixed-chart-material-envelope-same-point-scan-v1'",
        "SCAN_SCHEMA = 'complete-angular-refined-independent-fixed-chart-material-envelope-scan-v1'")
    result=result.replace("DEFINITION_SCHEMA = 'literal-old-current-grid-independent-fixed-chart-working-policy-v1'",
        "DEFINITION_SCHEMA = 'literal-old-even-new-full-angular-grid-independent-fixed-chart-policy-v1'\nOBSERVATION_SOURCE_SHA256 = '"+sha(observer)+"'")
    result=once(result,'        original_full_free_space_norm_and_objective_formula_unchanged=True,',
        '        original_full_free_space_norm_unchanged=True,\n'
        '        original_full_free_space_norm_and_objective_formula_unchanged=True,\n'
        '        original_full_free_space_norm_and_objective_unchanged=False,\n'
        '        finite_angular_objective_changed=True,reference_full_N=2048,current_full_N=4096,\n'
        '        original_tagged_angles_resolved_before_union=True,\n'
        '        complete_original_grid_is_even_subset_of_new_grid=True,')
    result=once(result,'def load_memory(args, preparation, q, history, *, restart=None, source_report_path=None):',
        ADDITIONS+'\ndef load_memory(args, preparation, q, history, *, restart=None, source_report_path=None):')
    result=once(result,"or int(preparation['N']) != 2048 or q.full_N != 2048 or q.N != 513",
        "or int(preparation['N']) != 2048 or q.full_N != 4096 or q.N != 1025\n"
        "            or q.base.reference_full_N != 2048")
    start=result.index('    phi = [float(v) for v in q.phi]',result.index('def load_memory('))
    end=result.index('    chart = q.base.context.core',start)
    result=result[:start]+'''    phi = [float(v) for v in q.phi]
    observation=_observation_module().validate_base_model(q.base.model)
    if ([v.hex() for v in phi]!=observation['current_literal_phi_hex']
            or [float(v).hex() for v in q.base.parent.phi]!=observation['reference_literal_phi_hex']):
        raise ValueError('The actual full observer and original reference words must agree with their independent binding')
'''+result[end:]
    result=once(result,"    sources = [file_record(args.preparation_report)]",
        "    sources = [file_record(args.preparation_report)]\n    angle_transfers=[]")
    result=once(result,"or prepared_locations.get('N') != q.full_N", "or prepared_locations.get('N') != 2048")
    result=once(result,"    points.walk(prepared_locations,path=('complete_actual_current_prepared_locations',))",
        "    angle_transfers.append(_walk_at_declared_N(points,prepared_locations,history,args.carrier,\n"
        "        label='complete_actual_current_prepared_locations',default_N=2048))")
    result=once(result,"        points.walk(restart, path=('complete_actual_new_policy_restart',))",
        "        angle_transfers.append(_walk_at_declared_N(points,restart,history,args.carrier,\n"
        "            label='complete_actual_new_policy_restart',default_N=4096))")
    result=once(result,"        if _indexed_grid(payload) and int(payload.get('N',payload.get('full_angles',payload.get('full_N',-1)))) != q.full_N:\n            raise ValueError('Do not reinterpret a tagged historical angle')\n",'')
    result=once(result,"        points.walk(payload, path=('explicit_complete_history',Path(path).name))",
        "        angle_transfers.append(_walk_at_declared_N(points,payload,history,args.carrier,\n"
        "            label='explicit_complete_history.'+Path(path).name))")
    result=once(result,"    record = dict(sources=sources, before=before, resolved_grid_positions=resolved, after=points.summary(),",
        "    record = dict(sources=sources, before=before, resolved_grid_positions=resolved, after=points.summary(),\n"
        "        complete_declared_N_angle_transfers=angle_transfers,reference_full_N=2048,current_full_N=4096,\n"
        "        indexed_history_reinterpreted=False,")
    result=once(result,"            implicit_grid=dict(current_radial_entry_count=len(current['radial_words']),",
        "            implicit_grid=dict(angular_observation=_observation_module().validate_base_model(q.base.model),\n"
        "                current_radial_entry_count=len(current['radial_words']),")
    result=once(result,"                phi_formula='binary64 pi * integer j / 1024, j=0,...,512',",
        "                phi_formula='old N2048 literal words copied to even indices; new odd binary64 pi*j/2048; all 1025',")
    result=once(result,"grid['angular_count'] != 513", "grid['angular_count'] != 1025")
    result=once(result,"grid['full_angular_count'] != 2048", "grid['full_angular_count'] != 4096")
    result=once(result,"grid['union_unique_radial_count']*513", "grid['union_unique_radial_count']*1025")
    result=once(result,"    for key in ('actual_phi_sha256','union_radial_words_sha256','extra_radial_words_sha256'):",
        "    observation=_observation_module().validate_carrier(grid.get('angular_observation'))\n"
        "    if grid.get('actual_phi_sha256')!=observation['current_phi_sha256']:\n"
        "        raise ValueError('Complete refined implicit grid must use its entire actual observer')\n"
        "    for key in ('actual_phi_sha256','union_radial_words_sha256','extra_radial_words_sha256'):")
    ast.parse(result);compile(result,'angular_refined_independent_chart_memory.py','exec')
    tree_before,tree_after=ast.parse(text),ast.parse(result)
    functions_before={n.name:ast.dump(n,include_attributes=False) for n in tree_before.body if isinstance(n,ast.FunctionDef)}
    functions_after={n.name:ast.dump(n,include_attributes=False) for n in tree_after.body if isinstance(n,ast.FunctionDef)}
    for name in ('validate_public_binding','_validate_independent_target_binding','read_carrier','_original_p0'):
        if functions_before[name]!=functions_after[name]:
            raise ValueError('The complete original independent target/address validation changed: '+name)
    classes_before={n.name:n for n in tree_before.body if isinstance(n,ast.ClassDef)}
    classes_after={n.name:n for n in tree_after.body if isinstance(n,ast.ClassDef)}
    for name in classes_before:
        original={n.name:ast.dump(n,include_attributes=False) for n in classes_before[name].body if isinstance(n,ast.FunctionDef)}
        current={n.name:ast.dump(n,include_attributes=False) for n in classes_after[name].body if isinstance(n,ast.FunctionDef)}
        for method in original:
            if method!='__init__' and original[method]!=current[method]:
                raise ValueError('Original material-memory behavior changed: '+name+'.'+method)
    return result


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--parent-source',type=Path,required=True)
    p.add_argument('--observer-source',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    value=derive(a.parent_source.read_text(),a.observer_source.read_text())
    a.output.write_text(value)
    print(json.dumps(dict(bytes=len(value.encode()),sha256=sha(value))))


if __name__=='__main__':
    main()
