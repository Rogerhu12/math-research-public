"""Static mathematical-AST comparison and three tiny metadata cases only.

No problem/provider, F/J, normal assembly, BVP or body is constructed.
The diagnostic statements are executed directly from the new frozen source
on invented tiny diagnostic packets; no physical result is inferred.
"""
from __future__ import annotations
import argparse
import ast
import copy
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import sys
import time
import numpy as np


def identity(path):
    p=Path(path);raw=p.read_bytes()
    return dict(path=str(p),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def dump(node):return ast.dump(node,include_attributes=False)


def functions(path):
    return {n.name:n for n in ast.parse(Path(path).read_text()).body if isinstance(n,ast.FunctionDef)}


class Normalize(ast.NodeTransformer):
    def visit_Name(self,node):
        if node.id=='gauss_cell_positive_trace_grouped_coast':
            node.id='gauss_cell_positive_trace_frozen_operator_compatible'
        return node


def named_call(node,name):
    return isinstance(node,ast.Call) and isinstance(node.func,ast.Attribute) and node.func.attr==name


def common_statistics_index(loop):
    for j,node in enumerate(loop.body):
        if isinstance(node,ast.For) and dump(node.target)==dump(ast.parse('key, packet_key',mode='eval').body):
            return j
    raise ValueError('Frozen stream statistics boundary not found')


def delete_packet_index(loop):
    for j,node in enumerate(loop.body):
        if isinstance(node,ast.Delete) and any(isinstance(t,ast.Name) and t.id=='packet' for t in node.targets):
            return j
    raise ValueError('Frozen packet release boundary not found')


def run(prefix):
    start=time.monotonic();directory=Path(__file__).parent
    paths=dict(old_stream=directory/'fd2d_gc_positive_trace_stream_normal_consumer.py',
        new_stream=directory/'fd2d_gc_grouped_coast_stream_normal.py',
        old_partition=directory/'fd2d_gc_partitioned_normal.py',
        new_partition=directory/'fd2d_gc_grouped_coast_partitioned_normal.py',
        R165=directory/'fd2d_gc_grouped_coast_codazzi.py',checker=Path(__file__))
    source={k:identity(p) for k,p in paths.items()}
    expected=dict(old_stream='db7377aee77ad151083f0c0d02a84cc7585f5108b2b28defe596f990cff226c3',
        old_partition='5802e1c2d366ff98b48127e8ca0327bb4027b97135bd2dae3032553c9741554c',
        R165='a0a8b934a600871bc3743c2d85c61b60f21005ef9c782499fa1e0cb064a5b4e2')
    checks={'frozen_dependencies_unchanged':all(source[k]['sha256']==v for k,v in expected.items())}
    old=functions(paths['old_stream']);new=functions(paths['new_stream'])
    checks['radial_view_AST_identical']=dump(old['radial_view'])==dump(new['radial_view'])
    checks['locality_assertion_AST_identical']=dump(old['_assert_local_cells'])==dump(new['_assert_local_cells'])
    a,b=(f['stream_positive_trace_normal'] for f in (old,new))
    adds=lambda function:[dump(n) for n in ast.walk(function) if named_call(n,'add')]
    checks['all_normal_add_calls_AST_identical']=adds(a)==adds(b)
    node_loop=lambda f:next(n for n in f.body if isinstance(n,ast.For) and isinstance(n.target,ast.Name) and n.target.id=='node')
    checks['complete_node_row_loop_AST_identical']=dump(node_loop(a))==dump(node_loop(b))
    boundary=lambda f:next(n for n in f.body if isinstance(n,ast.If) and isinstance(n.test,ast.Name) and n.test.id=='include_boundary')
    checks['complete_boundary_rows_AST_identical']=dump(boundary(a))==dump(boundary(b))
    cell_loop=lambda f:next(n for n in f.body if isinstance(n,ast.While))
    aa,bb=cell_loop(a),cell_loop(b)
    def math_cell_loop(loop):
        v=copy.deepcopy(loop);j=common_statistics_index(v);k=delete_packet_index(v)
        v.body=v.body[:j]+v.body[k:]
        return v
    checks['cell_row_construction_and_release_AST_identical']=dump(math_cell_loop(aa))==dump(math_cell_loop(bb))
    oldp,newp=functions(paths['old_partition']),functions(paths['new_partition'])
    checks['partition_function_names_identical']=set(oldp)==set(newp)
    normalized={name:dump(oldp[name])==dump(Normalize().visit(copy.deepcopy(newp[name]))) for name in oldp}
    checks['every_partition_function_AST_identical_except_consumer_default']=all(normalized.values())
    # Execute ONLY the new diagnostics block: common maxima and grouped
    # metadata aggregation, from the source AST, without importing providers.
    first=common_statistics_index(bb);last=delete_packet_index(bb)
    code=compile(ast.fix_missing_locations(ast.Module(body=copy.deepcopy(bb.body[first:last]),type_ignores=[])),
        str(paths['new_stream'])+':diagnostic-block','exec')
    ns=dict(np=np,maxima=dict(full_codazzi=0.,retained_codazzi=0.,omitted_codazzi=0.,known_lifting_change=None,
        G2_sampled_interior_Gauss=None,fine_sampled_interior_Gauss=None),
        grouped_rules=[],grouped_cells=[],fine_minimum_active_n=None)
    cases=[]
    for tag,start_cell,info,g2 in [
        ('outside_only',10,dict(grouped_coast_local_cells=[]),.3),
        ('one_grouped_cell',20,dict(grouped_coast_local_cells=[0],grouped_coast_rules=[
            dict(local_cell=0,fine_sampled_Gauss_maximum=.8,fine_sampled_minimum_active_n=.25,
                 points=[.1,.2],average_weights=[.5,.5])]),.4),
        ('mixed_chunk',30,dict(grouped_coast_local_cells=[1],grouped_coast_rules=[
            dict(local_cell=1,fine_sampled_Gauss_maximum=.6,fine_sampled_minimum_active_n=.2,
                 points=[.3,.4],average_weights=[.5,.5])]),.7),
    ]:
        packet=dict(info=info,full_codazzi_cells=np.array([.5]),retained_cells=np.array([.2]),
            omitted_codazzi_cells=np.array([.4]),point_gauss=np.array([g2]))
        before=json.dumps(info,sort_keys=True);ns.update(packet=packet,first=start_cell)
        exec(code,ns)
        cases.append(dict(case=tag,known_lifting_change=ns['maxima']['known_lifting_change'],
            G2_maximum=ns['maxima']['G2_sampled_interior_Gauss'],
            fine_maximum=ns['maxima']['fine_sampled_interior_Gauss'],
            fine_minimum_active_n=ns['fine_minimum_active_n'],
            grouped_global_cells=list(ns['grouped_cells']),input_info_unchanged=before==json.dumps(info,sort_keys=True)))
    checks['outside_fine_and_known_diagnostics_are_None']=cases[0]['fine_maximum'] is None and cases[0]['known_lifting_change'] is None
    checks['known_only_never_fabricated']=all(c['known_lifting_change'] is None for c in cases)
    checks['G2_and_fine_maxima_separate']=cases[-1]['G2_maximum']==.7 and cases[-1]['fine_maximum']==.8
    checks['minimum_and_global_cell_mapping']=cases[-1]['fine_minimum_active_n']==.2 and cases[-1]['grouped_global_cells']==[20,31]
    checks['input_packet_metadata_not_mutated']=all(c['input_info_unchanged'] for c in cases)
    checks['source_identity_unchanged_during_check']=all(identity(p)==source[k] for k,p in paths.items())
    report=dict(schema='fd2d-R165-grouped-normal-thin-adapter-check-v1',utc=datetime.now(timezone.utc).isoformat(),
        passed=all(checks.values()),checks=checks,sources=source,
        partition_functions_compared=normalized,diagnostic_only_synthetic_cases=cases,
        no_problem_or_physical_fields_constructed=True,no_F_or_J_evaluated=True,
        no_normal_assembled=True,no_BVP_or_body=True,
        mathematical_row_AST_scope='Complete node loop, cell construction/release excluding only statistics, boundary block, every normal.add, and every partition function',
        finite_equations_selected_by_new_default='R165 grouped actual coast; distinct from old v25 finite equations',
        seconds=time.monotonic()-start)
    target=Path(str(prefix)+'-report.json');target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(target),passed=report['passed'],checks=checks,seconds=report['seconds']),ensure_ascii=False))
    return 0 if report['passed'] else 1


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out-prefix',required=True)
    args=parser.parse_args();sys.exit(run(args.out_prefix))
