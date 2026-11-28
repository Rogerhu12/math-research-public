#!/usr/bin/env python3
"""Continuous relative metric of the SAME final shared-Cartesian R53 map.

The finite mean is read from the final defining jets. Complete true-core and
center corrections are included. Radial Taylor bounds and angular linear
interpolation use genuine complete three-jets on closed pieces. This pays no
tail, full-surface embedding/reach, lambda-one held set, or refinement claim.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
from bisect import bisect_right
from fractions import Fraction as Q
import json
import math
from pathlib import Path
import sys
import time
import traceback

import numpy as np

from cartesian_prefix_interval_geometry import K, SCRIPTS, module, save, sha
from cartesian_prefix_metric_target import FrozenTarget, HERMITE, I, b, fq
b.m.K = K


def pair(array):
    return I.raw((array[0],array[1]))


def constant(value):
    zero=I(np.zeros_like(value.x[0]))
    return b.D2(value,zero,zero)


def stack(values, axis=-1):
    return b.D2(*(I.raw(K.stack([getattr(v,attr).x for v in values],axis))
                  for attr in ('v','d','d2')))


class HermiteIntervals:
    """Outward exact-endpoint Hermite coefficients, never rounded PPoly data."""
    def __init__(self, knots, jets):
        self.x = [fq(x) for x in knots]
        if (jets.ndim != 3 or jets.shape[0] != 3 or jets.shape[2] != len(knots)
                or not np.all(np.isfinite(jets)) or np.any(np.diff(knots) <= 0)):
            raise ValueError('Complete finite common two-jets are required')
        h = I(knots[1:])-I(knots[:-1])
        h = I(h.x[0][None,:],h.x[1][None,:])
        y,d,q = [I(jets[j]) for j in range(3)]
        left=lambda a:a.item((slice(None),slice(None,-1)))
        right=lambda a:a.item((slice(None),slice(1,None)))
        e0=right(y)-left(y)-h*left(d)-h.sq()*left(q)/2
        e1=right(d)-left(d)-h*left(q)
        e2=right(q)-left(q)
        c=[left(y),h*left(d),h.sq()*left(q)/2,
           10*e0-4*h*e1+h.sq()*e2/2,
           -15*e0+7*h*e1-h.sq()*e2,
           6*e0-3*h*e1+h.sq()*e2/2]
        self.c=[]
        for order in range(4):
            self.c.append([c[j]*(math.factorial(j)//math.factorial(j-order))/(h**order)
                           for j in range(order,6)])

    def values(self,s,left,right):
        index=min(len(self.x)-2,max(0,bisect_right(self.x,(left+right)/2)-1))
        if not self.x[index] <= left <= right <= self.x[index+1]:
            raise ValueError('Split at every actual common Cartesian/chart knot')
        u=(s-I.rational(self.x[index]))/I.rational(self.x[index+1]-self.x[index])
        result=[]
        for row in self.c:
            value=I(0)
            for c in row[::-1]:
                value=value*u+c.item((slice(None),index))
            result.append(value)
        return result


def operator_upper(components):
    aa,bb,cc=components
    def absolute(v):
        return I(np.maximum(np.abs(v.x[0]),np.abs(v.x[1])))
    value=absolute(aa+cc)/2+((absolute(aa-cc)/2).sq()+absolute(bb).sq()).sqrt()
    return float(np.max(value.x[1]))


class NewMetric:
    def __init__(self, report_path):
        self.report_path=Path(report_path).resolve()
        self.record=json.loads(self.report_path.read_text())
        r=self.record
        if (r.get('status')!='complete_angular_three_jet_interval_tables'
                or r.get('right_sector_endpoint_gram_equals_left_exactly') is not True):
            raise ValueError('Require the complete actual angular enclosure table')
        for path,digest in r['source_hashes'].items():
            if sha(path)!=digest:
                raise ValueError('A bound angular construction source changed: '+path)
        for name in ('defining_jets','angular_tables'):
            if sha(r[name]['path'])!=r[name]['sha256']:
                raise ValueError('Bound exact-map interval data changed: '+name)
        run=Path(r['source_run'])
        if sha(run)!=r['source_run_sha256']:
            raise ValueError('The actual input run changed')
        gate=module('_new_metric_accepted_source',SCRIPTS/'resume_20261126/material_design_secant_predictor.py')
        source,raw=gate.accepted_original(run,SCRIPTS.parents[2])
        del raw
        loader=module('_new_metric_actual_model',SCRIPTS/'resume_m3/actual_m3_metric_model.py')
        obj=loader.load_model({'source_run':str(run)})
        with np.load(run.parent/'physical.npz',allow_pickle=False) as physical:
            p=physical['p'].copy()
        obj.initial(p)
        self.target=FrozenTarget(obj.flow(p[0]),source)
        with np.load(r['defining_jets']['path'],allow_pickle=False) as d:
            self.knots=d['knots'].copy()
            self.P=len(d['planar_modes'])
            self.field=HermiteIntervals(self.knots,d['jets'])
            self.lift=HermiteIntervals(self.knots,d['lift_jets'])
            self.chart=HermiteIntervals(self.knots,d['chart_jets'])
            self.width=fq(d['center_width'])
            self.pm=d['planar_modes'].copy()
            self.hm=d['height_modes'].copy()
        if (fq(self.knots[0])!=0 or fq(self.knots[-1])!=self.target.end
                or np.any(self.pm%3!=1) or np.any(self.hm%3!=0)):
            raise ValueError('The actual target and complete threefold map domains differ')
        with np.load(r['angular_tables']['path'],allow_pickle=False) as d:
            self.tables={name:pair(d[name].copy()) for name in d.files}
        self.N=int(r['angular_boxes_per_sector'])
        if self.tables['point_lift_0'].x[0].shape!=(self.N,3):
            raise ValueError('Missing complete angular table columns')
        self.grid=sorted(set(self.field.x+self.target.grid+[self.width]))

    def weights(self,s,left,right):
        if left>=self.width:
            return [[I(0) for _ in range(3)] for _ in range(4)]
        if right>self.width:
            raise ValueError('Split the exact center repair width')
        t=s/I.rational(self.width)
        result=[[] for _ in range(4)]
        for j,polynomial in enumerate(HERMITE):
            c=list(polynomial)
            for order in range(4):
                value=I(0)
                for coefficient in c[::-1]:
                    value=value*t+I.rational(coefficient)
                result[order].append(value*I.rational(self.width**(j-order)))
                c=[(k+1)*c[k+1] for k in range(len(c)-1)]
        return result

    def evaluate(self,left,right,tag,axis):
        if axis not in ('radial','angular') or tag not in ('point','box'):
            raise ValueError('Explicit derivative and angular coverage modes required')
        s=I(I.rational(left).x[0],I.rational(right).x[1])
        c=self.field.values(s,left,right)
        h=[v.item(0) for v in self.lift.values(s,left,right)]
        e=[v.item(0) for v in self.chart.values(s,left,right)]
        a=self.target.jets(s,left,right)
        w=self.weights(s,left,right)
        radial=axis=='radial'
        def radial_value(values,order):
            return b.D2(*values[order:order+3]) if radial else constant(values[order])
        def angular_value(name,order):
            values=[self.tables[f'{tag}_{name}_{j}'] for j in range(order,order+3 if not radial else order+1)]
            return constant(values[0]) if radial else b.D2(*values)
        def basis(derivative,coordinate):
            values=[self.tables[f'{tag}_basis_{j}_{coordinate}']
                    for j in range(derivative,derivative+3 if not radial else derivative+1)]
            return constant(values[0]) if radial else b.D2(*values)
        def field(radial_order,angular_order):
            coefficient=radial_value(c,radial_order)
            components=[]
            for coordinate in range(3):
                sl=slice(0,self.P) if coordinate<2 else slice(self.P,None)
                components.append((coefficient.item(sl).expand()*basis(angular_order,coordinate)).sum())
            value=stack(components)
            value+=radial_value(h,radial_order)*angular_value('lift',angular_order)
            center=angular_value('center',angular_order)
            for j in range(3):
                weight=radial_value([row[j] for row in w],radial_order)
                value+=weight*center.item(j)
            return value
        Xs,Xp=field(1,0),field(0,1)
        sine=self.tables[f'{tag}_trig_0']
        cosine=self.tables[f'{tag}_trig_1']
        sn=constant(sine) if radial else b.D2(sine,3*cosine,-9*sine)
        co=constant(cosine) if radial else b.D2(cosine,-3*sine,-9*cosine)
        ev,ep=radial_value(e,0),radial_value(e,1)
        av=radial_value(a,0)
        rho=1-ev*co
        theta_s=-ep*sn/3
        if np.min(rho.v.x[0])<=0 or np.min(av.v.x[0])<=0:
            raise ValueError('The target orthonormal material frame is not bounded positive')
        U=Xs-(theta_s/rho).expand()*Xp
        V=Xp/(av*rho).expand()
        values=[U.sq().sum(axis=1)-1,(U*V).sum(axis=1),V.sq().sum(axis=1)-1]
        if not all(getattr(v,key).finite() for v in values for key in ('v','d','d2')):
            raise ArithmeticError('Nonfinite complete normalized Gram derivative')
        return values,dict(radius_lower=float(np.min(av.v.x[0])),rho_lower=float(np.min(rho.v.x[0])))

    def enclose(self,left,right):
        middle=(left+right)/2
        point,pmeta=self.evaluate(middle,middle,'point','radial')
        whole,meta=self.evaluate(left,right,'point','radial')
        angular,_=self.evaluate(left,right,'box','angular')
        p=operator_upper([v.v for v in point])
        d=operator_upper([v.d for v in point])
        d2=operator_upper([v.d2 for v in whole])
        angular_d2=operator_upper([v.d2 for v in angular])
        h=I.rational((right-left)/2)
        radial_bound=I(p)+h*d+h.sq()*d2/2
        interpolation=self.tables['angular_width'].sq()*angular_d2/8
        bound=radial_bound+interpolation
        return float(bound.x[1]),dict(**meta,point_operator=p,radial_first=d,
            radial_second=d2,angular_second=angular_d2,
            radial_taylor_upper=float(radial_bound.x[1]),
            angular_interpolation_upper=float(interpolation.x[1]))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tables',type=Path,required=True)
    parser.add_argument('--outdir',type=Path,required=True)
    parser.add_argument('--target',type=float,default=9.9e-7)
    parser.add_argument('--max-cells',type=int,default=150000)
    parser.add_argument('--probe-only',action='store_true')
    a=parser.parse_args()
    out=a.outdir.resolve()
    repo=SCRIPTS.parents[2]
    if out==repo or repo in out.parents or not 0<a.target<=1e-6:
        raise ValueError('Use the original metric budget; complete certificate arrays stay outside Git')
    out.mkdir(parents=True,exist_ok=False)
    started=time.monotonic()
    report=dict(scope=__doc__,status='loading_bound_tables',metric_certified=False,
        whole_surface=False,table_report=str(a.tables.resolve()),table_report_sha256=sha(a.tables),
        target=a.target,accepted=0,splits=0,attempts=0,peak=0.)
    save(out/'summary.json',report)
    try:
        verifier=NewMetric(a.tables)
        sources=[Path(__file__),HERE/'cartesian_prefix_metric_target.py',
                 SCRIPTS/'resume_m3/certify_bridge_metric_fourier_taylor.py',
                 SCRIPTS/'resume_m3/certify_r59_fixed_mean_ranges.py',
                 SCRIPTS/'resume_20261126/seam_m3_prefix_pieces.py',
                 SCRIPTS/'resume_20261126/seam_certify_true_cut_height.py',
                 SCRIPTS/'resume_20261126/seam_bridge_endpoint_primitive.py',
                 SCRIPTS/'resume_20261126/seam_bridge_cut_trace.py',
                 SCRIPTS/'resume_20261126/warm_certify_bridge_geometry.py',
                 SCRIPTS/'finite_closure/m3_m8_closed_map/interval_geometry_kernel.py']
        report.update(status='continuous_metric_running',exact_target_definition=verifier.target.definition,
            initial_radial_cells=len(verifier.grid)-1,
            angular_boxes_per_sector=verifier.N,source_hashes={str(p):sha(p) for p in sources},
            source_run_sha256=verifier.record['source_run_sha256'],
            defining_jets=verifier.record['defining_jets'],full_core_and_center_repair=True,
            final_Cartesian_mean_used=True,source_mean_primitive_substituted=False,
            radius_lower=None,rho_lower=None)
        rows=[]
        if a.probe_only:
            for index in np.linspace(0,len(verifier.grid)-2,9).astype(int):
                left,right=verifier.grid[index:index+2]
                bound,meta=verifier.enclose(left,right)
                row=dict(radial=[float(left),float(right)],bound=bound,**meta)
                rows.append(row)
                print(json.dumps(dict(stage='unaccepted_interval_probe',**row)),flush=True)
            report.update(status='interval_probes_only',rows=rows,seconds=time.monotonic()-started)
            save(out/'summary.json',report)
            return
        pending=[(l,r,0) for l,r in zip(verifier.grid[:-1],verifier.grid[1:])][::-1]
        leaves=(out/'complete-leaves.jsonl').open('x')
        while pending:
            left,right,depth=pending.pop()
            report['attempts']+=1
            upper,meta=verifier.enclose(left,right)
            if upper<=a.target:
                report['accepted']+=1
                if upper>report['peak']:
                    report.update(peak=upper,peak_interval=[float(left),float(right)],peak_details=meta)
                for key in ('radius_lower','rho_lower'):
                    report[key]=meta[key] if report[key] is None else min(report[key],meta[key])
                leaves.write(json.dumps(dict(left=str(left),right=str(right),bound=upper,**meta))+'\n')
            else:
                if depth>=28 or report['accepted']+len(pending)>=a.max_cells:
                    report.update(status='continuous_metric_unresolved',remaining=len(pending)+1,
                        unresolved_interval=[float(left),float(right)],unresolved_details=meta,last_bound=upper)
                    break
                middle=(left+right)/2
                pending.extend([(middle,right,depth+1),(left,middle,depth+1)])
                report['splits']+=1
            if report['attempts']%50==0:
                report.update(seconds=time.monotonic()-started)
                save(out/'summary.json',report)
                print(json.dumps(dict(stage='continuous_new_map_metric',accepted=report['accepted'],
                    attempts=report['attempts'],splits=report['splits'],remaining=len(pending),
                    s=float(right),peak=report['peak'],seconds=report['seconds'])),flush=True)
        else:
            report.update(status='continuous_new_cartesian_prefix_metric_certified',metric_certified=True,
                full_radial_range=[str(verifier.grid[0]),str(verifier.grid[-1])],
                full_angular_range='[0,2*pi], by exact threefold covariance',
                all_phase_prefix_metric=True,
                phase_reason='Rotation and material-angle translation preserve the frozen radial target metric')
        leaves.close()
        report.update(seconds=time.monotonic()-started,
            complete_leaves_sha256=sha(out/'complete-leaves.jsonl'))
        save(out/'summary.json',report)
        print(json.dumps({k:report[k] for k in ('status','accepted','splits','peak','seconds')}),flush=True)
    except Exception as error:
        (out/'exception.txt').write_text(traceback.format_exc())
        report.update(status='continuous_metric_execution_failed',error=repr(error),
            seconds=time.monotonic()-started)
        save(out/'summary.json',report)
        raise


HERE=Path(__file__).resolve().parent
if __name__=='__main__':
    main()
