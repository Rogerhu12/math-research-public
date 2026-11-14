"""One small synthetic row-partition/transport/sum fixture; no physical solve.

The exact original elimination contains central-to-p, inactive coast l,
terminal n-l gauge and a fixed cut. Frozen local mathematics is not rerun:
only this module's two imported assembly entry points receive deterministic
small synthetic rows while the new public tile/merge API is exercised.
"""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import resource
import sys
import time
from types import SimpleNamespace
from unittest.mock import patch
import numpy as np
from scipy import sparse

import fd2d_gc_partitioned_normal as part
from fd2d_gc_local_normal_system import LocalNormalSystem
import fd2d_gc_local_normal_system as normal_module
import fd2d_gc_normal_checkpoint as transport


def identity(path):
    p=Path(path);raw=p.read_bytes()
    return dict(path=str(p),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def write_json(path,packet):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(packet,ensure_ascii=False,sort_keys=True,indent=2,allow_nan=False)+'\n')


def fixture():
    p=SimpleNamespace(N=6,q=5,parameter_count=4,K=1,e=2,d=3,work=16,
        x=np.arange(6,dtype=float),fixed_central_nodes=np.array([0,1]),
        additional_fixed_field_indices=np.array([18,19,23]),
        trace_gauge_pairs=np.array([[20,23]]),
        core_coefficients=np.array([[.25],[-.75]]),trace_ramp_stop=4.)
    p.size=p.N*p.q+p.parameter_count
    p.window=lambda:np.array([0.,0.,0.,1.,1.,0.])
    z=np.random.default_rng(20261112).normal(scale=.05,size=p.size)
    y=z[:p.N*p.q].reshape(p.N,p.q);parameters=z[p.N*p.q:]
    for node in p.fixed_central_nodes:
        y[node]=0.;y[node,:p.e]=p.core_coefficients@parameters[:p.K]
    y[-1]=0.;z[p.additional_fixed_field_indices]=0.
    for n,l in p.trace_gauge_pairs:z[l]=-z[n]
    return p,z


def unused_cell_consumer(*args,**kwargs):
    raise AssertionError('The synthetic fixture does not evaluate physical Codazzi')


def row(problem,vector,label,nodes,requested_rows):
    nodes=tuple(nodes)
    count=3 if requested_rows is None else requested_rows
    if label=='node_curvature' and nodes[0]==1:count=0
    key=(label+':'+','.join(map(str,nodes))).encode()
    seed=int.from_bytes(hashlib.sha256(key).digest()[:8],'little')
    rng=np.random.default_rng(seed)
    r=rng.normal(scale=.17,size=count)
    J=rng.normal(scale=.23,size=(count,len(nodes)*problem.q+problem.parameter_count))
    q=problem.q;e=problem.e;d=problem.d
    y=vector[:problem.N*q].reshape(problem.N,q);p=vector[problem.N*q:]
    if label=='central_boundary':
        J[:]=0.;J[:,:d]=np.eye(d)
        J[:e,q:q+problem.K]=-problem.core_coefficients
        r=y[0,:d].copy();r[:e]-=problem.core_coefficients@p[:problem.K]
    elif label=='cut_l':
        J[:]=0.;J[:,d:q]=np.eye(e);r=y[-1,d:].copy()
    elif label=='cut_nm':
        J[:]=0.;J[:,:d]=np.eye(d);r=y[-1,:d].copy()
    elif label=='gap':
        J[:]=0.;J[0,0]=1.25;r=np.array([.015])
    return r,J


def synthetic_stream(problem,vector,*,node_indices,cell_indices,include_boundary,
        observer=None,**kwargs):
    descriptor=dict(node_indices=list(node_indices),cell_indices=list(cell_indices),
        include_boundary=include_boundary,interior_cells=[])
    normal=LocalNormalSystem(problem)
    for spec in part._expected_ledger(problem,descriptor):
        r,J=row(problem,vector,spec['label'],spec['nodes'],spec['rows'])
        normal.add(r,J,spec['nodes'],label=spec['label'],observer=observer)
    return normal,dict(synthetic_rows=True,physical_mathematical_consumer_called=False)


def synthetic_interior(problem,vector,*,cells,**kwargs):
    assert len(cells)==1
    cell=int(cells[0]);nodes=(cell,cell+1)
    columns=np.r_[np.arange(cell*problem.q,(cell+2)*problem.q),
                  problem.N*problem.q+np.arange(problem.parameter_count)]
    specs=part._expected_ledger(problem,dict(node_indices=[],cell_indices=[],
        include_boundary=False,interior_cells=[cell]))
    out=dict(info=dict(synthetic_rows=True,selected_cells=[cell]))
    for spec in specs:
        name=spec['label'].removeprefix('interior_')
        r,J=row(problem,vector,spec['label'],nodes,spec['rows'])
        ii,jj=np.nonzero(J)
        out[name+'_residual']=r
        out[name+'_jacobian']=sparse.coo_matrix((J[ii,jj],(ii,columns[jj])),
            shape=(len(r),problem.size)).tocsc()
    return out


def payload(normal):
    return dict(mapping=transport._mapping_definition(normal.mapping),
        diagonal=[transport._array_id(a) for a in normal.diagonal],
        upper=[transport._array_id(a) for a in normal.upper],
        arrays={key:transport._array_id(getattr(normal,key)) for key in part.ARRAYS},
        metadata={key:transport._pack_metadata(getattr(normal,key))
                  for key in ('residual_squared','rows','blocks','row_groups','info')})


def difference(left,right):
    groups={key:[getattr(left,key),getattr(right,key)] for key in part.ARRAYS}
    for j,(a,b) in enumerate(zip(left.diagonal,right.diagonal)):groups['diagonal_'+str(j)]=[a,b]
    for j,(a,b) in enumerate(zip(left.upper,right.upper)):groups['upper_'+str(j)]=[a,b]
    out={}
    for key,(a,b) in groups.items():
        scale=max(float(np.max(abs(a),initial=0.)),float(np.max(abs(b),initial=0.)))
        absolute=float(np.max(abs(a-b),initial=0.))
        out[key]=dict(maximum_absolute=absolute,scale=scale,
            scale_normalized=absolute/max(1.,scale),bit_identity=transport._array_id(a)==transport._array_id(b))
    out['residual_squared']=dict(maximum_absolute=abs(left.residual_squared-right.residual_squared),
        scale=max(left.residual_squared,right.residual_squared),
        scale_normalized=abs(left.residual_squared-right.residual_squared)/max(1.,left.residual_squared,right.residual_squared),
        bit_identity=left.residual_squared.hex()==right.residual_squared.hex())
    return out


def run(prefix):
    start=time.monotonic();problem,z=fixture();prefix=Path(prefix)
    sources={key:identity(path) for key,path in dict(checker=__file__,partition=part.__file__,
        original_normal=normal_module.__file__,transport=transport.__file__).items()}
    plan=part.make_normal_partition(problem,node_block=2,cell_block=2,interior_cells=[1,3])
    plan_path=Path(str(prefix)+'-plan.json');write_json(plan_path,plan)
    common=dict(schema='synthetic-partition-transport-fixture-v1',sources=sources,
        plan_sha256=plan['plan_sha256'],vector_identity=transport._array_id(z))
    reference=LocalNormalSystem(problem);saved=[];transport_checks=[]
    map_checks=dict(central_to_parameter_exact=True,inactive_coast_l_exact=True,
                    terminal_n_minus_l_exact=True,fixed_cut_exact=True)
    for desc in plan['tiles']:
        with patch.object(part,'stream_positive_trace_normal',synthetic_stream),\
             patch.object(part,'interior_gauss_curvature',synthetic_interior):
            normal,info=part.assemble_normal_tile(problem,z,desc,binding=common,
                cell_consumer=unused_cell_consumer,block_cells=2)
        for spec in part._expected_ledger(problem,desc):
            r,J=row(problem,z,spec['label'],spec['nodes'],spec['rows'])
            reference.add(r,J,spec['nodes'],label=spec['label'])
            A,B=normal.mapping.transform(spec['nodes'],J)
            if spec['label']=='central_boundary':
                map_checks['central_to_parameter_exact'] &= bool(np.all(B==0.))
            for i,node in enumerate(spec['nodes']):
                original=normal.mapping.free[normal.mapping.node_free[node]]%problem.q
                wanted=J[:,i*problem.q+original].copy()
                for ni,li in problem.trace_gauge_pairs:
                    if ni//problem.q==node:
                        local=int(np.flatnonzero(original==ni%problem.q)[0])
                        wanted[:,local]-=J[:,i*problem.q+li%problem.q]
                map_checks['terminal_n_minus_l_exact'] &= bool(np.array_equal(A[i],wanted))
                if node==3:
                    map_checks['inactive_coast_l_exact'] &= bool(not np.any(np.isin(original,[3,4])))
                if node==problem.N-1:
                    map_checks['fixed_cut_exact'] &= bool(A[i].shape[1]==0)
        binding=dict(common=common,descriptor=desc)
        checkpoint=transport.save_normal_checkpoint(normal,Path(str(prefix)+'-tiles')/desc['id'],binding=binding)
        expected=payload(normal)
        restored=transport.load_normal_checkpoint(problem,checkpoint,expected_binding=binding)
        exact=payload(restored)==expected
        transport_checks.append(dict(id=desc['id'],all_array_mapping_metadata_bits_identical=exact,
            storage_bytes=normal.storage_bytes(),manifest=identity(checkpoint)))
        if not exact:raise AssertionError('Synthetic tile transport changed a logical byte')
        saved.append((desc,checkpoint,binding))
        del normal,restored,expected
    def loaded():
        for desc,checkpoint,binding in saved:
            normal=transport.load_normal_checkpoint(problem,checkpoint,expected_binding=binding)
            yield desc,normal
            del normal
    # Exercise the production iterator merge, which owns only the current
    # incoming tile and the unscaled accumulator. saved contains no normals.
    merged,merge_info=part.merge_normal_tiles(problem,loaded(),plan)
    diff=difference(reference,merged)
    max_relative=max(row['scale_normalized'] for row in diff.values())
    counters=(reference.rows==merged.rows and reference.blocks==merged.blocks
        and reference.row_groups==merged.row_groups)
    checks=dict(transport_bit_identity=all(r['all_array_mapping_metadata_bits_identical'] for r in transport_checks),
        original_mapping_identical=transport._mapping_definition(reference.mapping)==transport._mapping_definition(merged.mapping),
        exact_row_counters_and_groups=counters,all_elimination_checks=all(map_checks.values()),
        sum_difference_within_32_machine_eps=max_relative<=32*np.finfo(float).eps)
    # Two tiny deliberately incomplete/misordered streams must fail. These
    # are synthetic transport contract checks, not new physical gates.
    rejection={}
    for name,indices in [('missing_final',list(range(len(saved)-1))),('duplicate_first',[0,0])]:
        def bad_stream():
            for index in indices:
                desc,checkpoint,binding=saved[index]
                packet=transport.load_normal_checkpoint(problem,checkpoint,expected_binding=binding)
                yield desc,packet
                del packet
        try:
            part.merge_normal_tiles(problem,bad_stream(),plan)
        except ValueError as exc:
            rejection[name]=dict(rejected=True,error=str(exc))
        else:
            rejection[name]=dict(rejected=False)
    checks['incomplete_or_duplicate_not_reported_complete']=all(r['rejected'] for r in rejection.values())
    sources_unchanged={key:identity(v['path'])==v for key,v in sources.items()}
    checks['sources_unchanged']=all(sources_unchanged.values())
    report=dict(schema='fd2d-synthetic-partition-transport-sum-check-v1',
        scope='One synthetic six-node local row fixture. No physical BVP, whole Jacobian, or actual v25 normal was computed.',
        utc=datetime.now(timezone.utc).isoformat(),passed=all(checks.values()),checks=checks,
        sources=sources,source_unchanged=sources_unchanged,plan=identity(plan_path),
        dimensions=part._dimensions(problem),node_widths=merged.mapping.widths.tolist(),
        number_of_tiles=len(plan['tiles']),rows=merged.rows,blocks=merged.blocks,row_groups=merged.row_groups,
        elimination_checks=map_checks,transport=transport_checks,
        grouped_vs_sequential=difference(reference,merged),maximum_scale_normalized_sum_difference=max_relative,
        floating_bit_identity_of_regrouped_sum_claimed=False,
        complete_matrix_of_actual_current_field_claimed=False,
        rejection=rejection,merge_info=merge_info,
        seconds=time.monotonic()-start,peak_rss_kib=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
    report_path=Path(str(prefix)+'-report.json');write_json(report_path,report)
    print(json.dumps(dict(report=str(report_path),passed=report['passed'],tiles=len(saved),rows=merged.rows,
        maximum_scale_normalized_sum_difference=max_relative,seconds=report['seconds'],
        peak_rss_kib=report['peak_rss_kib']),ensure_ascii=False),flush=True)
    return 0 if report['passed'] else 1


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out-prefix',required=True)
    args=parser.parse_args();sys.exit(run(args.out_prefix))
