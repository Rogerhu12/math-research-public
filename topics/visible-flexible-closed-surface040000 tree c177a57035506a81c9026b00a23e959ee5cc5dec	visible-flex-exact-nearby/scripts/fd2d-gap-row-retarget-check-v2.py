#!/usr/bin/env python3
"""Small independent row-assembly check; never evaluate a physical field."""
import copy
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from fd2d_gc_local_normal_system import LocalNormalSystem
from fd2d_gc_gap_row_retarget import gap_retarget_binding, replace_gap_row_in_place


def identity(path):
    p=Path(path);a=p.read_bytes()
    return dict(path=str(p),bytes=len(a),sha256=hashlib.sha256(a).hexdigest())


def main():
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    problem=SimpleNamespace(N=4,q=8,e=3,K=2,parameter_count=5,
        core_coefficients=np.array([[1.,.3],[.2,-.4],[.1,.2]]))
    rng=np.random.default_rng(1846)
    rows=[('node',(1,),rng.normal(size=8),rng.normal(size=(8,13))),
          ('cell',(1,2),rng.normal(size=17),rng.normal(size=(17,21))),
          ('node',(2,),rng.normal(size=7),rng.normal(size=(7,13)))]
    current_gap=.9000098655
    gradient=np.array([.317,-.271])
    binding=dict(schema='synthetic-finite-goal-v1',same_input='fixed-small-fixture',
        mathematical_settings=dict(gap=.9,modes=2,curvature_cap=7.2))
    def assemble(target):
        n=LocalNormalSystem(problem)
        for label,nodes,r,J in rows:n.add(r,J,nodes,label=label)
        full=np.zeros(problem.parameter_count);full[:len(gradient)]=gradient
        n.add([(current_gap-target)/target],full[None,:]/target,(),label='gap')
        n.info=dict(full_finite_objective=True,scaling_or_damping_applied=False,
            state_binding=dict(opaque_binding=dict(field_and_finite_objective=copy.deepcopy(binding))))
        return n
    def unchanged(n):
        return [a.tobytes() for a in n.diagonal+n.upper+[n.Hfp,n.gf,n.field_norm_squared]]
    results=[]
    for target in [.8,.75,.9]:
        n=assemble(.9);expected=assemble(target);before=unchanged(n)
        oldp=[n.Hpp.tobytes(),n.gp.tobytes(),n.parameter_norm_squared.tobytes(),n.residual_squared]
        proof=replace_gap_row_in_place(n,actual_gap=current_gap,central_gap_gradient=gradient,
            old_binding=binding,new_binding=gap_retarget_binding(binding,target))
        deltas={}
        for name in ['Hpp','gp','parameter_norm_squared']:
            actual=getattr(n,name);reference=getattr(expected,name)
            deltas[name]=float(np.max(abs(actual-reference)/(1+abs(reference)),initial=0.))
        deltas['residual_squared']=abs(n.residual_squared-expected.residual_squared)/(1+expected.residual_squared)
        assert max(deltas.values())<2e-14,deltas
        assert before==unchanged(n)
        assert n.rows==expected.rows and n.blocks==expected.blocks and n.row_groups==expected.row_groups
        if target==.9:
            assert oldp==[n.Hpp.tobytes(),n.gp.tobytes(),n.parameter_norm_squared.tobytes(),n.residual_squared]
        results.append(dict(target=target,relative_to_independent_original_row_assembly=deltas,
            all_field_buffers_bitwise_unchanged=True,rows=n.rows,proof=proof))
    bad=gap_retarget_binding(binding,.8);bad['mathematical_settings']['modes']=2
    n=assemble(.9);before=n.Hpp.copy()
    try:
        replace_gap_row_in_place(n,actual_gap=current_gap,central_gap_gradient=gradient,
            old_binding=binding,new_binding=bad)
    except ValueError:pass
    else:raise AssertionError('Unrelated finite-goal change was admitted')
    assert np.array_equal(before,n.Hpp)
    here=Path(__file__).resolve().parent
    report=dict(schema='fd2d-gap-row-retarget-small-independent-check-v1',complete=True,
        cases=results,changed_unrelated_goal_rejected_before_mutation=True,
        actual_physical_field_or_large_matrix_computed=False,
        source=identity(here/'fd2d_gc_gap_row_retarget.py'),checker=identity(__file__))
    args.out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(complete=True,cases=len(results),maximum_relative_difference=max(
        max(r['relative_to_independent_original_row_assembly'].values()) for r in results),
        actual_physical_F_or_J=False)))


if __name__=='__main__':main()
