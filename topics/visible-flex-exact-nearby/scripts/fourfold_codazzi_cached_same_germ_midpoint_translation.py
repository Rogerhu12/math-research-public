#!/usr/bin/env python3
"""Derive missing quarter midpoint jets only from saved same-germ enclosures.

This module makes no target calls. It is intended for a separate actual
consumer after the original cached-Hessian result is complete. Original
quarter rows stay immutable; derived point data have their own receipt.
"""
from __future__ import annotations
import copy,hashlib,json
from fractions import Fraction
from flint import arb
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_codazzi_known_cut_direction_cap_pilot_v3 import exact,rec,rowsha

NAMES=('gamma','beta','K','s')


def midpoint(cell):
    lo,hi=map(Fraction,cell['interval'])
    return (lo+hi)/2


def germ(cell):
    return tuple(map(Fraction,cell['actual_scalar_germ']))


def path_cover(cells,x,y,required_germ):
    """Exact closed path covered by original quarters of one true C3 germ."""
    lo,hi=min(x,y),max(x,y)
    if lo==hi:raise ValueError('a missing midpoint cannot be its own saved anchor')
    edge=lo;pieces=[]
    for cell in cells:
        left,right=map(Fraction,cell['interval'])
        if right<=lo:continue
        if left>=hi:break
        a,b=max(left,lo),min(right,hi)
        if a!=edge or not a<b:return None
        if germ(cell)!=required_germ:return None
        if not required_germ[0]<=a<b<=required_germ[1]:return None
        whole=cell.get('all_original_target_coefficients',{})
        if any(n+'3' not in whole for n in NAMES):return None
        pieces.append((cell,a,b));edge=b
    return pieces if edge==hi else None


def from_anchor(target,anchor,pieces):
    x,y=midpoint(anchor),midpoint(target);delta=y-x;d=exact(delta)
    jets=anchor['intrinsic_midpoint_jets'];whole=target['all_original_target_coefficients']
    values={};hulls={}
    for name in NAMES:
        third=None
        for cell,_,_ in pieces:
            value=box_from_record(cell['all_original_target_coefficients'][name+'3'])
            if not value.is_finite():raise ValueError('a saved full third derivative is nonfinite')
            third=value if third is None else third.union(value)
        if third is None:raise ValueError('the exact nonempty derivative path is missing')
        a0,a1,a2=(box_from_record(jets[name+s]) for s in ('','1','2'))
        derived=(a0+d*a1+d*d*a2/2+d*d*d*third/6,
                 a1+d*a2+d*d*third/2,a2+d*third)
        for order,value in enumerate(derived):
            key=name+('' if order==0 else str(order))
            # The target whole-interval derivative is a second independent
            # enclosure of this same point, so its intersection is legitimate.
            value=value.intersection(box_from_record(whole[key]))
            if not value.is_finite():raise ValueError('saved Taylor and target whole jets have empty intersection')
            values[key]=value
        values[name+'3']=box_from_record(whole[name+'3'])
        hulls[name]=rec(third)
    receipt=dict(anchor_request=anchor['request'],anchor_original_quarter_row_sha256=rowsha(anchor),
        exact_anchor=str(x),exact_target=str(y),exact_signed_displacement=str(delta),
        original_midpoint_jets_sha256=rowsha(jets),
        full_path=[dict(request=c['request'],original_quarter_row_sha256=rowsha(c),
            actual_closed_intersection=[str(a),str(b)],
            original_parameter_enclosure_half_width=c.get('intrinsic_target_enclosure_half_width',
                c.get('new_parameter_half_width','0'))) for c,a,b in pieces],
        same_actual_scalar_germ=list(map(str,germ(target))),
        directed_third_derivative_interval_hulls=hulls,
        exact_Taylor_masses=['1/6','1/2','1'],
        physical_parameter='fixed original physical eta0 only',
        no_new_target_evaluation=True)
    return values,receipt


def fill_missing(table):
    """Keep every original row unchanged and derive at most its missing point.

    Up to two closest original saved anchors, one on each side, are used.
    No derived point is silently reused as an unrecorded original anchor.
    A target with no complete same-germ path keeps the original fallback.
    """
    keys=sorted(table);cells=[table[k] for k in keys];edge=Fraction(9,10)
    for cell in cells:
        left,right=map(Fraction,cell['interval'])
        if left!=edge or not left<right:raise ValueError('the complete original quarter cover changed')
        edge=right
    if edge!=Fraction(25,8):raise ValueError('the exact complete cap endpoint is missing')
    anchors={}
    for cell in cells:
        if cell.get('intrinsic_midpoint_jets'):
            anchors.setdefault(germ(cell),[]).append(cell)
    new_table=dict(table);receipts=[];unavailable=[]
    for key in keys:
        target=table[key]
        if target.get('intrinsic_midpoint_jets'):continue
        y=midpoint(target);choices=anchors.get(germ(target),[])
        left=[c for c in choices if midpoint(c)<y];right=[c for c in choices if midpoint(c)>y]
        selected=([max(left,key=midpoint)] if left else [])+([min(right,key=midpoint)] if right else [])
        candidates=[];sources=[]
        for anchor in selected:
            pieces=path_cover(cells,midpoint(anchor),y,germ(target))
            if pieces is None:continue
            value,receipt=from_anchor(target,anchor,pieces)
            candidates.append(value);sources.append(receipt)
        if not candidates:
            unavailable.append(dict(request=target['request'],original_quarter_row_sha256=rowsha(target),
                reason='no original saved midpoint with a complete same-germ closed derivative path'))
            continue
        result={}
        for name in candidates[0]:
            value=candidates[0][name]
            for other in candidates[1:]:value=value.intersection(other[name])
            if not value.is_finite():raise ValueError('two legitimate saved-anchor point enclosures have empty intersection')
            result[name]=rec(value)
        derived=copy.deepcopy(target);derived['intrinsic_midpoint_jets']=result
        receipt=dict(request=target['request'],original_quarter_row_sha256=rowsha(target),
            exact_midpoint=str(y),same_actual_scalar_germ=target['actual_scalar_germ'],
            original_full_third_jets_unchanged=True,derived_midpoint_not_called_original_saved_data=True,
            original_anchor_receipts=sources,new_target_evaluations=0,
            physical_parameter='fixed original physical eta0 only')
        receipt['derived_midpoint_jets_sha256']=rowsha(result)
        derived['midpoint_derivation_receipt']=receipt
        new_table[key]=derived
        receipts.append(receipt)
    return new_table,receipts,unavailable
