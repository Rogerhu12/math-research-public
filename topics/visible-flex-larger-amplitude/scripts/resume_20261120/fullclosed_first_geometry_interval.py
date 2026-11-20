#!/usr/bin/env python3
"""Complete first-jet immersion and positive-flow support cover using R656.

All original cells, full angles, both flat caps and the mirror are covered.
Positive A_beta support on a closed C2 sphere immersion implies embedding
by the flow projection argument of R650. This source does not bound curvature
and never asserts reach or an isometric solution.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    spec=importlib.util.spec_from_file_location('fullclosed_first_geometry_kernel',path)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    return module


def first_controls(reader,cell,piece):
    I=reader.I
    left,right,u0,u1,active=piece
    h=reader.width_box(reader.nodes[cell],reader.nodes[cell+1])
    if float(h[0])<=0:
        raise ValueError('The original exact cell width must be positive')
    b=reader.hermite(I.at(reader.jets,cell),I.at(reader.jets,cell+1),h)
    db=reader.derivative(b,h)
    b,db=[reader.elevate(reader.restrict(v,u0,u1))for v in (b,db)]
    fields={}
    for name,controls,order in [('X',b,0),('V',db,0),('T',b,1)]:
        fields[name]=[reader.angle_boxes(c,parity)for c,parity in reader.channels(controls,order)]
    lift=reader.lift_controls(left,right,active)
    lift={key:(value[0][:,None],value[1][:,None])for key,value in lift.items()}
    for name,scalar,zscalar in [('X','f','chi'),('V','fp','cp')]:
        fields[name]=[I.add(fields[name][k],I.mul(lift[scalar],reader.er[k]))for k in range(3)]
        fields[name][2]=I.add(fields[name][2],I.mul(lift[zscalar],reader.Hbox))
    fields['T']=[I.add(fields['T'][k],I.mul(lift['f'],I.mul(reader.rho,reader.et[k])))for k in range(3)]
    return fields


def cover_cell(reader,cell):
    I=reader.I
    record=dict(cell=cell,minimum_normal_squared_lower=float('inf'),
        minimum_E_lower=float('inf'),support_lower=float('inf'),
        maximum_radius_squared_upper=0.,unpaid_immersion_boxes=0,
        worst_support=None,worst_normal=None,worst_radius=None)
    pieces=reader._cell_pieces(cell)
    for part,piece in enumerate(pieces):
        controls=first_controls(reader,cell,piece)
        values={name:[reader.radial_parts(component)for component in vector]for name,vector in controls.items()}
        for sub in range(reader.subdivisions):
            fields={name:[(c[sub][0].min(axis=0),c[sub][1].max(axis=0))for c in vector]for name,vector in values.items()}
            X,V,T=[fields[name]for name in ('X','V','T')]
            at=lambda idx:dict(piece=part,radial_subcell=sub,angle_grid_index=int(idx))
            radius2=reader.norm2(X)[1];idx=int(np.argmax(radius2))
            if float(radius2[idx])>record['maximum_radius_squared_upper']:
                record['maximum_radius_squared_upper']=float(radius2[idx]);record['worst_radius']=at(idx)
            N=reader.cross(T,V);E=reader.norm2(V)
            W2a=reader.norm2(N)
            W2b=I.sub(I.mul(E,reader.norm2(T)),I.square(reader.dot(V,T)))
            W2=np.maximum(W2a[0],W2b[0]),np.minimum(W2a[1],W2b[1])
            idx=int(np.argmin(W2[0]))
            if float(W2[0][idx])<record['minimum_normal_squared_lower']:
                record['minimum_normal_squared_lower']=float(W2[0][idx]);record['worst_normal']=at(idx)
            record['minimum_E_lower']=min(record['minimum_E_lower'],float(E[0].min()))
            bad=(W2[0]<=0)|(E[0]<=0)
            record['unpaid_immersion_boxes']+=int(np.count_nonzero(bad))
            if np.any(bad):
                continue
            weightedX=[X[0],X[1],I.mul(reader.fraction(reader.beta),X[2])]
            support=I.div(reader.dot(weightedX,N),I.sqrt(W2))[0];idx=int(np.argmin(support))
            if float(support[idx])<record['support_lower']:
                record['support_lower']=float(support[idx]);record['worst_support']=at(idx)
    record.update(exact_pieces=len(pieces),all_continuous_immersion_boxes_paid=record['unpaid_immersion_boxes']==0)
    if record['unpaid_immersion_boxes']:
        record['support_lower']=None
    return record


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('bundle','node-report','interval-source','geometry-source','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--angles',type=int,default=2048)
    p.add_argument('--radial-subdivisions',type=int,default=1)
    p.add_argument('--beta',default='1/4')
    a=p.parse_args()
    if a.out.exists():raise FileExistsError('Retain earlier complete geometry reports')
    np.seterr(over='raise',invalid='raise',divide='raise',under='ignore')
    started=time.monotonic();module=load(a.geometry_source)
    reader=module.Reader(a.bundle,a.node_report,a.interval_source,
        angles=a.angles,radial_subdivisions=a.radial_subdivisions,beta=a.beta,witness=False)
    records=[];caps=reader.cap_bounds()
    report=dict(schema='fullclosed-complete-first-geometry-interval-v1',source_sha256=sha(__file__),
        geometry_source_sha256=sha(a.geometry_source),metadata=reader.metadata(),
        cap_bounds=caps,records=records,complete_scope=False,
        embedding_certified=False,curvature_certified=False,reach_certified=False,metric_certified=False)
    for cell in range(reader.J-1):
        records.append(cover_cell(reader,cell))
        if len(records)%64==0:
            report['seconds']=time.monotonic()-started
            a.out.write_text(json.dumps(report,indent=2)+'\n')
            print(json.dumps(dict(event='first_geometry_progress',completed=len(records),total=reader.J-1,
                unpaid_boxes=sum(r['unpaid_immersion_boxes']for r in records),
                smallest_paid_support=min((r['support_lower']for r in records if r['support_lower']is not None),default=None),
                seconds=report['seconds'])),flush=True)
    if [r['cell']for r in records]!=list(range(reader.J-1)):
        raise ValueError('Incomplete original cell coverage')
    unpaid=sum(r['unpaid_immersion_boxes']for r in records)
    support=min(caps['support_lower'],*(r['support_lower']for r in records)) if unpaid==0 else None
    radius2=max(caps['maximum_radius_squared_upper'],*(r['maximum_radius_squared_upper']for r in records))
    diameter=float(reader.I.scale(reader.I.sqrt(reader.I.exact(radius2)),2.)[1])
    rho=report['metadata']['core_rho_continuous_lower']
    embedded=bool(unpaid==0 and support is not None and support>0 and rho>0)
    report.update(complete_scope=True,covered_original_cells=len(records),unpaid_immersion_boxes=unpaid,
        all_body_support_lower=support,maximum_radius_squared_upper=radius2,diameter_upper=diameter,
        minimum_normal_squared_lower=min(r['minimum_normal_squared_lower']for r in records),
        minimum_E_lower=min(r['minimum_E_lower']for r in records),embedding_certified=embedded,
        embedding_proof='R650 positive-definite flow projection on the original closed C2 sphere immersion, with both flat disks; this does not use a curvature bound',
        minimum_support_cells=sorted(records,key=lambda r:float('-inf')if r['support_lower']is None else r['support_lower'])[:10],
        seconds=time.monotonic()-started)
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items()if k not in ('records','metadata')}),flush=True)
    print(json.dumps(dict(event='first_geometry_complete',report_sha256=sha(a.out))),flush=True)


if __name__=='__main__':main()
