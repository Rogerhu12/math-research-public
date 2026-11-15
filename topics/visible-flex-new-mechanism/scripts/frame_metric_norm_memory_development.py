#!/usr/bin/env python3
"""Only new semantic fixtures for direction memory and exact reference transfer."""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import math
import os
from types import SimpleNamespace as NS
import numpy as np
from frame_entry_body_subspace import ArrayLP
from frame_metric_norm_direction_memory import (
    N, POLICY, unit_ball_direction, support_row, NormDirectionBank, solve_remembered_primary)
from frame_metric_norm_memory_transfer import recover_reference_heights, REPO

def must_reject(call):
    try:
        call()
    except (ValueError, ArithmeticError):
        return True
    return False

def require(value, text):
    if not value:
        raise AssertionError(text)

def norm_phi(e, f, epsilon, group):
    return .5*((1 if group == 0 else -1)*e+math.hypot(e, 2*f, epsilon))

def fixture_model(e, f, radius, binding="d"*64):
    de, df = np.zeros(N), np.zeros(N)
    de[0], df[1] = .5, -.25
    selected = NS(e=np.array([e]), f=np.array([f]), de=de[None,:], df=df[None,:])
    requests=[]
    def extra(label, flat):
        requests.append((label, flat))
        return {"e":e-.25, "f":f+.5, "de":de.copy(), "df":df.copy()}
    oracle=NS(
        binding={"coordinate_definition_sha256":"a"*64,
                 "height_reference_definition_sha256":"b"*64,
                 "factorization_definition_sha256":"c"*64},
        grid_binding={label:{"rational_grid_definition_sha256":char*64}
                      for label,char in (("coarse","e"),("fine","f"))},
        grids={label:NS(point_count=1024) for label in ("coarse","fine")},
        original_row=extra, wall=lambda:None)
    return NS(oracle=oracle, epsilon=1e-8, target=.26,
              selected_point_lookup={("coarse",0):0}, selected_model=selected,
              primary=NS(step_scale=np.full(N,radius)), binding_sha256=binding,
              requests=requests)

def developer_check():
    require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPO,
            "new fixtures execute only in public repository Actions")
    checks={}
    normals=[]
    for e,f in [(1.,1e-10),(-3.,.7),(0.,0.),(1e-150,2e-150)]:
        n,_=unit_ball_direction(e,f,1e-8)
        require(sum((Q.from_float(x)**2 for x in n),Q())<=1,"normal left exact unit ball")
        normals.append(n)
    checks["rounded_directions_are_inside_exact_binary64_unit_ball"]=True
    checks["outside_unit_normal_rejected"]=must_reject(
        lambda:support_row({"e":0.,"f":0.,"de":np.zeros(N),"df":np.zeros(N)},
                           (1.,2**-30,0.),0,1e-8,.26,np.ones(N)))
    model=fixture_model(2.,0.,.1)
    bank=NormDirectionBank()
    tag={"grid":"coarse","flat_row_id":0,"group":0}
    bank.remember(model,tag,2.,0.)
    oldA,oldb,oldrecord=bank.rebuilt(model)
    new=fixture_model(-1.,.5,.025,"1"*64)
    newA,newb,record=bank.rebuilt(new)
    actual=norm_phi(-1.,.5,1e-8,0)-.26
    require(-oldb[0]>actual+1.,"old numeric intercept trap was not exposed")
    require(-newb[0]<=actual+1e-14,"rebuilt inherited normal is not below new norm")
    require(not np.array_equal(oldA,newA) and not np.array_equal(oldb,newb),
            "new center and trust did not rebuild coefficients")
    checks["old_numeric_plane_trap_and_changed_trust_rebuilding"]=True
    for n in normals:
        row={"e":-.3,"f":.7,"de":np.arange(N)/1000.,"df":-np.arange(N)/700.}
        for group in (0,1):
            A,b=support_row(row,n,group,1e-8,.26,np.full(N,.02))
            for scalar in (-2.,-.1,0.,.2,3.):
                z=np.full(N,scalar);step=.02*z
                e=row["e"]+float(row["de"]@step)
                f=row["f"]+float(row["df"]@step)
                lower=float(A[:N]@z)-b
                upper=norm_phi(e,f,1e-8,group)-.26
                require(lower<=upper+2e-13*max(1.,abs(upper)),"support escaped norm at a new point")
    checks["both_original_branches_bound_after_center_and_scale_change"]=True
    fine={"grid":"fine","flat_row_id":1024,"group":1}
    bank.remember(new,fine,-.4,.8)
    _,_,rec=bank.rebuilt(new)
    require(new.requests==[("fine",1024)] and rec["selected_current_derivatives_reused"]==1,
            "same original point lookup vs new row derivative not preserved")
    checks["original_grid_branch_ID_and_selected_or_new_derivative_paths"]=True
    checks["wrong_original_branch_rejected"]=must_reject(
        lambda:bank.remember(new,dict(tag,group=1),1.,0.))
    other=fixture_model(-1.,.5,.025)
    other.oracle.binding["coordinate_definition_sha256"]="2"*64
    checks["changed_coordinate_reference_context_rejected"]=must_reject(lambda:bank.rebuilt(other))
    cap=NormDirectionBank()
    for i in range(513):
        cap.remember(model,{"grid":"coarse","flat_row_id":i,"group":0},1.,i/1000.)
    require(len(cap.entries)==512 and ("coarse",0) not in cap.entries and cap.evictions==1,
            "declared bounded latest-per-row storage failed")
    cap.remember(model,{"grid":"coarse","flat_row_id":1,"group":0},-1.,.3)
    require(len(cap.entries)==512 and next(reversed(cap.entries))==("coarse",1),
            "latest same-row direction was not deterministic")
    checks["declared512_capacity_and_latest_row_replacement"]=True
    # Seeded LP enters before the first call; use the inherited residual checker.
    objective=np.zeros(N+2);objective[N],objective[N+1]=1.,.001
    lo=np.r_[np.full(N,-1.),0.,0.];hi=np.r_[np.full(N,1.),np.inf,1.]
    primary=ArrayLP(np.zeros((0,N+2)),np.zeros(0),objective,lo,hi,information={})
    primary.step_scale=np.ones(N)
    row={"e":1.,"f":0.,"de":np.r_[.5,np.zeros(N-1)],"df":np.zeros(N)}
    A,b=support_row(row,(1.,0.,0.),0,1e-8,0.,primary.step_scale)
    toy=NS(primary=primary,summary=lambda:{"new_fixture":True},
           initial_cuts=lambda:(A[None,:],np.array([b]),{"rows":1,"schema":"new-seed-fixture"}),
           rho0=norm_phi(1.,0.,1e-8,0),
           slack=lambda p:norm_phi(1.+.5*float(p[0]),0.,1e-8,0))
    old_primary=(primary.A.copy(),primary.b.copy(),copy.deepcopy(primary.information))
    calls=[]
    def solver(lp,cfg):
        require(len(lp.b)==1 and lp is not primary,"seed row absent before first solver call")
        calls.append(len(lp.b))
        p=np.zeros(N);p[0]=-.1
        return p,{"normalized_step_norm":.1,"predicted_metric_slack":toy.slack(p),
                  "success":True,"status":0}
    cfg={"new_affine_array_fixture_only":True,"max_linear_models":1,
         "linear_program_seconds":10.,"metric_row_tolerance":1e-9,
         "linear_model_improvement_floor":1e-10,"linear_model_residual_limit":1e-7}
    ledger={"linear_program_invocation_count":0,"primary_LP_invocation_count":0}
    progress={}
    p,result=solve_remembered_primary(primary,toy,cfg,ledger,progress=progress,
        wall=lambda:None,remaining_seconds=lambda:120.,solve_one=solver)
    require(p is not None and calls==[1] and ledger["linear_program_invocation_count"]==1
            and result["initial_rebuilt_memory_rows"]==1,"new seeded call/budget protocol failed")
    require(np.array_equal(primary.A,old_primary[0]) and np.array_equal(primary.b,old_primary[1])
            and primary.information==old_primary[2],"original primary for SOC was mutated")
    checks["seed_before_first_LP_same_shared_ledger_and_original_SOC_primary_unchanged"]=True
    # A deliberately rational exact dependent-height vector cannot be rounded first.
    H=[[Q(0) for k in range(5)] for j in range(9)]
    for k in range(5):H[k][k]=Q(1,3+k)
    H[8]=[Q(-1,3+k) for k in range(5)]
    q=np.zeros(N);q[0]=.125;q[154:]=[.25,-.125,.0625,0.,-.5]
    reference=[Q(j-3,32) for j in range(9)]
    phys=[Q.from_float(float(x)) for x in q[:154]]
    phys += [reference[j]+sum((H[j][k]*Q.from_float(float(q[154+k]))
                              for k in range(5)),Q()) for j in range(9)]
    qx=[str(Q.from_float(float(x))) for x in q];px=list(map(str,phys))
    recovered= recover_reference_heights(qx,px,H)
    require(recovered[2]==tuple(reference) and np.array_equal(recovered[0],q),
            "exact affine reference did not recover")
    rounded=[str(Q.from_float(float(x))) for x in phys]
    require(rounded!=px,"fixture did not expose dependent-height rounding")
    checks["exact_original_height_reference_recovered_without_rounding_nine_values"]=True
    bad=list(px);bad[0]="1/7"
    checks["incompatible_physical_tangent_vector_rejected"]=must_reject(
        lambda:recover_reference_heights(qx,bad,H))
    bad=list(px);bad[154]=str(phys[154]+Q(1,7))
    checks["nonbinary_reference_height_rejected"]=must_reject(
        lambda:recover_reference_heights(qx,bad,H))
    require(all(checks.values()),"a new semantic development check failed")
    return {"schema":POLICY+"-development","passed":True,"checks":checks,
            "artificial_inputs_only":True,"old_developer_suites_executed":False,
            "old_optimizer_or_geometry_executed":False,
            "labels_are_new_semantic_checks_not_continuous_physical_certificates":True}
