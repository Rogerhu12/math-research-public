#!/usr/bin/env python3
"""Exact finite coefficient witnesses for absence of planar activity patches.

The two axial radial traces are polynomials on each original cell and have
strictly positive values at its left endpoint. A nonzero nonconstant-angular
height Hermite datum proves a nonzero polynomial. Together with analytic
angular continuation and half-turn parity this rules out every planar open
parameter patch. No embedding, reach, isometry or metric refinement is claimed.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def affine(coefficient, constant, box):
    values = [coefficient*x+constant for x in box]
    return min(values), max(values)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def mul(a, b):
    values = [x*y for x in a for y in b]
    return min(values), max(values)


def smoothstep(x):
    return 10*x**3-15*x**4+6*x**5


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('bundle','node-report','out'):
        parser.add_argument('--'+name,type=Path,required=True)
    a = parser.parse_args()
    if a.out.exists():
        raise FileExistsError('Keep prior exact coefficient records')
    started = time.monotonic()
    with np.load(a.bundle,allow_pickle=False) as data:
        jets=np.array(data['qjets']); mesh=np.array(data['mesh'])
        width=F(float(data['width'])); radius_carrier=float(data['radius'])
        height=F(float(data['Hcap']))
    n=jets.shape[-1];M=(n-2)//3;J=len(mesh)
    if n!=3*M+2 or jets.shape!=(J,3,n) or not np.all(np.isfinite(jets)):
        raise ValueError('Expected the complete finite rotating-basis field')
    node_report=json.loads(a.node_report.read_text())
    nodes=[(F(v['S_coefficient']),F(v['constant'])) for v in node_report['true_scalar_nodes']]
    S=tuple(F(node_report['scalar']['S'][k])for k in ('lower_exact','upper_exact'))
    R=tuple(F(node_report['scalar']['R'][k])for k in ('lower_exact','upper_exact'))
    if len(nodes)!=J or nodes[0]!=(F(0),F(0)) or nodes[-1]!=(F(1),F(0)):
        raise ValueError('Exact node interface does not match the field')
    if node_report['S_carrier']!=float(mesh[-1]) or node_report['radius_carrier']!=radius_carrier:
        raise ValueError('Use the same original Hold contour and node carrier')
    if width<=0 or R[0]<=0 or not S[0]>width:
        raise ValueError('Positive original radial scales are required')
    breaknode=(F(1),-width)
    break_index=nodes.index(breaknode)
    if nodes.count(breaknode)!=1:
        raise ValueError('This exact piece proof needs the original lift-break node')
    records=[];min_axis=None;min_witness=None
    for cell in range(J-1):
        left,right=nodes[cell],nodes[cell+1]
        h=affine(right[0]-left[0],right[1]-left[1],S)
        if h[0]<=0:
            raise ValueError('Original exact cell widths must be positive')
        relative=affine(left[0]-1,left[1]+width,S)
        if cell<break_index:
            if affine(right[0]-1,right[1]+width,S)[1]>0:
                raise ValueError('An unrepresented lift break lies inside a cell')
            lift=(F(0),F(0))
        else:
            rr=(relative[0]/width,relative[1]/width)
            if rr[0]<0 or rr[1]>1:
                raise ValueError('Active endpoint not enclosed in the exact lift interval')
            chi=(smoothstep(rr[0]),smoothstep(rr[1]))
            radial=add(R,affine(1-left[0],-left[1],S))
            lift=mul(chi,radial)
        radial_coeff=[F(float(v))for v in jets[cell,0,:M+1]]
        axis0=add((sum(radial_coeff),)*2,lift)
        axis90=add((sum(((-1)**j)*v for j,v in enumerate(radial_coeff)),)*2,lift)
        if axis0[0]<=0 or axis90[0]<=0:
            raise ValueError('An axial trace has no positive endpoint witness')
        angular_height=jets[cell:cell+2,:,2*M+2:]
        index=np.unravel_index(int(np.argmax(np.abs(angular_height))),angular_height.shape)
        value=F(float(angular_height[index]))
        if value==0:
            raise ValueError('This cell has no nonzero angular height Hermite datum')
        item=dict(cell=cell,left_node=cell,axis0_lower_exact=str(axis0[0]),
            axis90_lower_exact=str(axis90[0]),
            height_witness=dict(node=cell+int(index[0]),derivative_order=int(index[1]),
                nonzero_mode=1+int(index[2]),exact_value=str(value)),
            full_open_cell_nonplanar=True)
        records.append(item)
        low=min(axis0[0],axis90[0]);min_axis=low if min_axis is None else min(min_axis,low)
        v=abs(value);min_witness=v if min_witness is None else min(min_witness,v)
    if [r['cell']for r in records]!=list(range(J-1)):
        raise ValueError('Missing an original analytic radial piece')
    record=dict(schema='fullclosed-exact-nonplanar-piece-coefficients-v1',
        source_sha256=sha(__file__),bundle_sha256=sha(a.bundle),
        node_report_sha256=sha(a.node_report),J=J,M=M,
        exact_lift_break_node=break_index,
        all_original_cells_nonplanar=True,covered_original_cells=len(records),
        minimum_axis_endpoint_lower_exact=str(min_axis),
        minimum_axis_endpoint_lower_approximate=float(min_axis),
        minimum_selected_height_jet_absolute_exact=str(min_witness),
        minimum_selected_height_jet_absolute_approximate=float(min_witness),
        height_exact=str(height),records=records,
        proof='Analytic continuation in angle; half-turn parity; nonzero axial trace polynomials force horizontal plane normal to vanish; a nonzero nonconstant-angular height polynomial rules out the remaining horizontal plane',
        arithmetic='Exact Fraction inputs and interval operations; no floating nonzero tolerance',
        embedding_certified=False,reach_certified=False,metric_certified=False,
        seconds=time.monotonic()-started)
    a.out.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:v for k,v in record.items()if k!='records'}),flush=True)
    print(json.dumps(dict(report_sha256=sha(a.out))),flush=True)


if __name__=='__main__':
    main()
