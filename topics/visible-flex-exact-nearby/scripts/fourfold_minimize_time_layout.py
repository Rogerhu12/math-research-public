#!/usr/bin/env python3
"""Reduce an already passed time DFT layout using its full original budget.

This changes neither the error target nor the analytic hypotheses.  Only
zero-node-error trial layouts are selected here; the caller must retain its
usual actual node/DFT/coefficient-choice checks after sampling.
"""
from __future__ import annotations
from flint import arb


def bound(value):
    value=arb(value['upper']) if isinstance(value,dict) else arb(value)
    if not value.is_finite() or not value>=0:
        raise ValueError('finite nonnegative complete error budget required')
    return value.upper()


def minimize_time_layout(budget_function, layout, *, target):
    """Return (new_layout, trials); layout is (N,K,Nt,m), target as adaptive_layout.

    budget_function(N,K,Nt,m,[0]*m) is the SAME complete field or density
    budget already used by the caller.  Its total must be <= target/4,
    preserving the original room for true node errors and finite choices.
    Starting after the first passed adaptive layout, try m=Nt and decrease
    the even Nt by two.  Stop at the first failure.  No claim is made that
    this restricted search finds a global optimum among all possible m.
    """
    N,K,Nt,m=map(int,layout)
    if not (N>1 and 0<=K<N//2 and Nt>=2 and Nt%2==0 and 0<m<=Nt):
        raise ValueError('invalid already selected layout')
    target=arb(target['lower']) if isinstance(target,dict) else arb(target)
    if not target.is_finite() or not target>0:
        raise ValueError('finite positive directed target required')
    threshold=(target/4).lower()
    original=budget_function(N,K,Nt,m,[arb(0)]*m)
    if not bound(original['total'])<=threshold:
        raise ValueError('input layout has not passed the original complete threshold')
    best=(N,K,Nt,m)
    trials=[dict(nodes=N,degree=K,time_nodes=Nt,terms=m,passed=True,
        complete_total_upper=str(bound(original['total'])),kind='original_passed_layout')]
    for trial_Nt in range(Nt-2,1,-2):
        candidate=budget_function(N,K,trial_Nt,trial_Nt,[arb(0)]*trial_Nt)
        total=bound(candidate['total'])
        passed=bool(total<=threshold)
        trials.append(dict(nodes=N,degree=K,time_nodes=trial_Nt,terms=trial_Nt,
            passed=passed,complete_total_upper=str(total),kind='full_budget_even_time_trial'))
        if not passed:break
        best=(N,K,trial_Nt,trial_Nt)
    return best,trials
