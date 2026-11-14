#!/usr/bin/env python3
"""Tight real radii for PB subpieces inside the fixed R33 source panels.

The original source-panel strip and source integrals are unchanged.  Only
the radius supplied to each smaller gauge-flow enclosure is refined using
the exact positive physical-width formula and both fixed parent endpoints.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from fractions import Fraction as Q
from flint import arb
from closure_real_head_source_enclosure import exact_q
from closure_real_head_green_enclosure import ball, maximum
from closure_weighted_panel_low_green_v3 import core_kernel


def intersection(a,b):
    lo=max(a.lower(),b.lower());hi=min(a.upper(),b.upper())
    if not lo<=hi:raise ArithmeticError('Independent true-radius boxes do not intersect')
    return lo.union(hi)


def prepare_cell(kernels,n,material,threshold):
    h=kernels.head;cell=kernels.source_cell(n);parents=[];count=0;maxproduct=arb(0)
    value_cache={}
    def value(s,x):
        key=(s['j'],str(x))
        if key not in value_cache:value_cache[key]=h.source_point(s,exact_q(x) if isinstance(x,Q) else x)
        return value_cache[key]
    def width(s,left,right):
        if left==right:return arb(0)
        lo=exact_q(left);hi=exact_q(right);points=[left]
        for t in s['critical_points']:
            if lo<t<hi:points.append(t)
            elif not(t<lo or t>hi):raise ArithmeticError('A critical root overlaps a PB endpoint')
        points.append(right);v=[value(s,x) for x in points]
        wlo=min(x['w'].lower() for x in v);whi=max(x['w'].upper() for x in v)
        normals=[x['w']/(1+x['w']**2).sqrt() for x in v]
        curvature=sum((abs(b-a) for a,b in zip(normals,normals[1:])),arb(0))/8
        dro=v[-1]['ro']-v[0]['ro']
        if not dro>0:raise ArithmeticError('A free radial subpiece lost positivity')
        free=(h.alpha*dro.lower()/(1+whi**2)).lower().union((h.alpha*dro.upper()/(1+wlo**2)).upper())
        return curvature+free
    for row in material['panels']:
        left=Q(*row['x_left']);right=Q(*row['x_right']);s=cell['segments'][row['segment']]
        rleft=ball(row['radius_left']);rright=ball(row['radius_right']);parent_r=ball(row['radius'])
        rcache={left:rleft,right:rright}
        def radius_at(x):
            if x not in rcache:
                r=intersection(rleft+width(s,left,x),rright-width(s,x,right))
                rcache[x]=intersection(r,parent_r)
            return rcache[x]
        pieces=[];stack=[(left,right,0)]
        while stack:
            lo,hi,depth=stack.pop()
            r=radius_at(lo).lower().union(radius_at(hi).upper())
            kernel=core_kernel(kernels,n,row['segment'],lo,hi,r)
            A,B=kernels.mode_integrals(kernel,92);product=(A.upper()*B.upper()).upper()
            if product>threshold:
                if depth>=30:raise ArithmeticError('The true PB subdivision limit was reached')
                mid=(lo+hi)/2;stack.append((mid,hi,depth+1));stack.append((lo,mid,depth+1))
            else:
                pieces.append(kernel);maxproduct=maximum(maxproduct,product)
        parents.append(dict(segment=row['segment'],x_left=row['x_left'],x_right=row['x_right'],
            radius=parent_r,w=ball(row['w']),tau=ball(row['tau_range']),
            J=ball(row['canonical_source_integral']).upper(),pieces=pieces))
        count+=len(pieces)
    return parents,count,maxproduct
