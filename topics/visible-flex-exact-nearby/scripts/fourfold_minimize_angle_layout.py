#!/usr/bin/env python3
"""Reduce angular DFT nodes using the unchanged complete analytic budget.

The retained degree, time nodes and time terms are fixed.  This is only an
analytic-layout selection; the actual sampled-node RMS and finite choices
must still pass the caller's complete reconstruction check.
"""
from __future__ import annotations
from flint import arb
from fourfold_minimize_time_layout import bound


def minimize_angle_layout(budget_function, layout, *, target, step=128):
    N,K,Nt,m=map(int,layout)
    if not (N>1 and N%2==0 and 0<=K<N//2 and Nt>=2 and Nt%2==0 and 0<m<=Nt):
        raise ValueError('invalid already selected angular layout')
    if step<2 or step%2:
        raise ValueError('the angular decrement must be a positive even integer')
    target=arb(target['lower']) if isinstance(target,dict) else arb(target)
    if not target.is_finite() or not target>0:
        raise ValueError('finite positive directed target required')
    threshold=(target/4).lower()
    original=budget_function(N,K,Nt,m,[arb(0)]*m)
    if not bound(original['total'])<=threshold:
        raise ValueError('the original full analytic threshold has not passed')
    trials=[dict(nodes=N,degree=K,time_nodes=Nt,terms=m,passed=True,
                 complete_total_upper=str(bound(original['total'])),
                 kind='original_passed_angular_layout')]
    best=(N,K,Nt,m)
    for trial_N in range(((N-1)//step)*step,2*K+1,-step):
        candidate=budget_function(trial_N,K,Nt,m,[arb(0)]*m)
        total=bound(candidate['total']);passed=bool(total<=threshold)
        trials.append(dict(nodes=trial_N,degree=K,time_nodes=Nt,terms=m,
                           passed=passed,complete_total_upper=str(total),
                           kind='full_budget_angular_node_trial'))
        if not passed:
            break
        best=(trial_N,K,Nt,m)
    return best,trials
