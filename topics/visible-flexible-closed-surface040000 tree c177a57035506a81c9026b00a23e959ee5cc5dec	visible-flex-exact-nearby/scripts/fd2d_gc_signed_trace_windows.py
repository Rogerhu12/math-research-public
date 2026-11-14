"""Explicit R182 signed, disjoint Gauss-trace windows.

All old files remain unchanged. A negative branch is -P_plus(-S), with
full value, angular and metric derivatives. Only the declared original
PSD cut has the old exact-tail bypass. Finite guards are not certificates
of a continuous metric domain.
"""
from __future__ import annotations
import numpy as np
from fd2d_gc_positive_trace_branch import positive_trace_delta

PARTIALS=('delta','delta_xi','gn','gm','gl','gK','hn','hm','hl','hK','h','h_xi')

def signed_trace_delta(values, angular, K, weight, sign, *, exact_tail_mask=None):
    if sign not in (-1,1):
        raise ValueError('An explicit constant sign +1 or -1 is required')
    values=np.asarray(values,float);angular=np.asarray(angular,float)
    if sign==1:
        result=positive_trace_delta(values,angular,K,weight,exact_tail_mask=exact_tail_mask)
    else:
        if exact_tail_mask is not None and np.any(exact_tail_mask):
            raise ValueError('The existing exact PSD tail is only the positive branch')
        result=positive_trace_delta(-values,-angular,K,weight)
        # Two value/angle input signs cancel the outer sign in state
        # partials. K has no input sign; its partials retain the outer -.
        for key in ('delta','delta_xi','gK','hK'):
            result[key]=-result[key]
        actual=values.copy();actual_xi=angular.copy()
        actual[...,0]+=result['delta'];actual[...,2]+=result['delta']
        actual_xi[...,0]+=result['delta_xi'];actual_xi[...,2]+=result['delta_xi']
        result.update(actual=actual,actual_angular=actual_xi,
            actual_n=actual[...,0],actual_l=actual[...,2],
            actual_n_xi=actual_xi[...,0],actual_l_xi=actual_xi[...,2])
    result['constant_trace_sign']=int(sign)
    return result

def disjoint_trace_delta(values,angular,K,components,*,exact_tail_mask):
    values=np.asarray(values,float);angular=np.asarray(angular,float)
    shape=values.shape[:-1]
    pieces=[];total=np.zeros(shape);active=np.zeros(shape,bool)
    for part in components:
        weight=np.broadcast_to(np.asarray(part['weight'],float),shape)
        if np.any((weight>0)&active):
            raise ValueError('Signed trace windows must have disjoint active supports')
        tail=exact_tail_mask if part.get('original_terminal',False) else None
        packet=signed_trace_delta(values,angular,K,weight,int(part['sign']),exact_tail_mask=tail)
        pieces.append(packet);total+=weight;active|=weight>0
    if np.any(total>1) or not pieces:
        raise ValueError('Invalid disjoint trace weight family')
    out={key:sum((p[key] for p in pieces),np.zeros(shape)) for key in PARTIALS}
    actual=values.copy();actual_xi=angular.copy()
    actual[...,0]+=out['delta'];actual[...,2]+=out['delta']
    actual_xi[...,0]+=out['delta_xi'];actual_xi[...,2]+=out['delta_xi']
    evaluable=active&~np.broadcast_to(np.asarray(exact_tail_mask,bool),shape)
    out.update(actual=actual,actual_angular=actual_xi,
        actual_n=actual[...,0],actual_l=actual[...,2],
        actual_n_xi=actual_xi[...,0],actual_l_xi=actual_xi[...,2],
        weight=total,active=evaluable,
        exact_tail_mask=np.broadcast_to(np.asarray(exact_tail_mask,bool),shape),
        minimum_active_h=float(out['h'][evaluable].min()) if np.any(evaluable) else None,
        exact_tail_contract_verified=False,
        signed_components=[{'name':p['name'],'sign':int(p['sign'])} for p in components])
    return out
