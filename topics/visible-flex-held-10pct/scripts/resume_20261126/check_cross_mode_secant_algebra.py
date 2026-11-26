#!/usr/bin/env python3
"""Pure algebra check of the cross-M evaluator; no real field or BVP is used."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace
import sys
import numpy as np
from scipy.interpolate import PPoly


def module(name, path):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec)
    sys.modules[name]=value
    spec.loader.exec_module(value)
    return value


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--predictor',type=Path,required=True)
    parser.add_argument('--original-lift',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    predictor=module('_checked_cross_mode_predictor',args.predictor)
    lift=module('_checked_original_lift',args.original_lift)
    old_m,new_m=2,4
    n0,n1=3*old_m+1,3*new_m+1
    knots=np.array([0.,.2,.6,1.])
    # One actual global quadratic, stored in the PPoly local-power convention.
    c=np.zeros((4,len(knots)-1,n0))
    a=np.arange(1,n0+1)/9.
    b=np.arange(n0,0,-1)/11.
    constant=np.arange(n0)/13.
    for j,left in enumerate(knots[:-1]):
        c[1,j]=a
        c[2,j]=2*a*left+b
        c[3,j]=a*left*left+b*left+constant
    pp=PPoly.construct_fast(c,knots,axis=1,extrapolate=False)
    raw=dict(x=knots,y=pp(knots),cubic_x=knots,cubic_c=c)
    checked_pp,nodal_roundoff=predictor.saved_cubic(raw)
    query=np.unique(np.r_[knots,np.linspace(0,1,29)])
    flow=SimpleNamespace(prefix_end=1.)
    flow.profile=lambda s:(1.+.2*s+.05*s*s,.2+.1*s,np.full_like(s,.1))
    def chart(t,delta):
        return t+delta*t*(1.-t),1.+delta*(1.-2*t)
    old=SimpleNamespace(M=old_m,q=.06,chart=chart,flow=lambda _:flow)
    new=SimpleNamespace(M=new_m,q=.06,chart=chart,flow=lambda _:flow)
    old_p=np.array([.17,-.3])
    new_p=np.array([.17,-.3,0.,0.])
    difference=np.arange(1,n1+1)/17.
    values=predictor.evaluate_lifted_left(
        checked_pp,query,old,new,old_p,new_p,difference,lift)
    physical_s,_=chart(query,old_p[0])
    weight=lift.lift_weights(flow,physical_s)[0]
    expected=np.zeros((n1,len(query)))
    old_values=pp(query)
    # Independent explicit block map, not a second call to embed.
    expected[0]=old_values[0]
    expected[1:3]=old_values[1:3]
    expected[5:7]=old_values[3:5]
    expected[9:11]=old_values[5:7]
    expected+=weight[None,:]*difference[:,None]
    block_gap=float(np.max(abs(values-expected)))
    psi=2*np.pi*np.arange(41)/41
    def basis(M):
        out=np.zeros((3*M+1,len(psi),3))
        out[0,:,0]=1.
        for j in range(1,M+1):
            out[j,:,0]=np.cos(3*j*psi)
            out[M+j,:,1]=np.sin(3*j*psi)
            out[2*M+j,:,2]=np.cos(3*j*psi)
        return out
    B0,B1=basis(old_m),basis(new_m)
    old_field=old.q*np.einsum('nt,nkc->tkc',old_values,B0)
    new_reference=-new.q*weight[:,None,None]*np.einsum('n,nkc->kc',difference,B1)[None,:,:]
    new_field=new_reference+new.q*np.einsum('nt,nkc->tkc',values,B1)
    cancellation=float(np.max(abs(new_field-old_field)))
    wrong_s,_=chart(query,.31)
    wrong_weight=lift.lift_weights(flow,wrong_s)[0]
    wrong_coordinate_gap=float(np.max(abs((wrong_weight-weight)[:,None]*difference[None,:])))
    wrong_new=SimpleNamespace(M=new_m,q=.06,flow=lambda _:flow,
        chart=lambda t,_:chart(t,.31))
    rejected=False
    try:
        predictor.evaluate_lifted_left(
            checked_pp,query,old,wrong_new,old_p,new_p,difference,lift)
    except ValueError as error:
        rejected='literal radial chart' in str(error)
    if not (block_gap==0. and cancellation<2e-15 and wrong_coordinate_gap>1e-3 and rejected):
        raise AssertionError((block_gap,cancellation,wrong_coordinate_gap,rejected))
    record=dict(kind='pure_algebra_mock_check',complete=True,
        actual_source_field_used=False,BVP_invoked=False,DN_invoked=False,
        actual_input_or_predictor_acceptance_claimed=False,
        modes=[old_m,new_m],query_nodes=len(query),angular_nodes=len(psi),
        source_nodal_roundoff=nodal_roundoff,explicit_block_formula_gap=block_gap,
        complete_reference_cancellation_max=cancellation,
        deliberately_wrong_right_coordinate_gap=wrong_coordinate_gap,
        wrong_coordinate_rejected=rejected,
        source_hashes={str(args.predictor.resolve()):sha(args.predictor),
                       str(args.original_lift.resolve()):sha(args.original_lift),
                       str(Path(__file__).resolve()):sha(__file__)})
    args.out.write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    print(json.dumps(record,allow_nan=False))


if __name__=='__main__':
    main()
