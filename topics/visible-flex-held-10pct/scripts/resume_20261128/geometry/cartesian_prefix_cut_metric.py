#!/usr/bin/env python3
"""Enclose the complete cut repair of one actual shared Cartesian prefix.

The new correction uses all declared tail and prefix Fourier modes. Its exact
coefficients use the real R58 arclength expressions of the literal R,w; binary
ap/app caches are not promoted to exact constants. Existing prefix leaves can
be inherited only on the exact unchanged complement of the cut strip. The
near-cut tail radius reparameterization is a separate obligation.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
from fractions import Fraction as Q
import json
from pathlib import Path
import sys
import time
import traceback

import mpmath as mp
import numpy as np

from cartesian_prefix_metric import (NewMetric, constant, stack, operator_upper,
                                     K, SCRIPTS, I, b, fq, HERMITE, save, sha)
from actual_closed_map_v2 import ActualFiniteTailV2
from seam_export_tail_geometry_v2 import checked


def intervals(values, axis=0):
    return I.raw(K.stack([v.x for v in values],axis))


def exact_sincos(x):
    """Outward quadrant reduction followed by the existing Taylor enclosure."""
    x=I(x)
    mp.iv.dps=75
    pi2=mp.iv.pi/2
    pi2=I(K.dn(float(pi2.a)),K.up(float(pi2.b)))
    quadrant=np.rint(((x.x[0]+x.x[1])/2)/(np.pi/2)).astype(np.int64)
    y=x-I(quadrant)*pi2
    sine,cosine=b.m.sincos_i(y)
    q=quadrant%4
    return (I(np.choose(q,[sine.x[0],cosine.x[0],-sine.x[1],-cosine.x[1]]),
              np.choose(q,[sine.x[1],cosine.x[1],-sine.x[0],-cosine.x[0]])),
            I(np.choose(q,[cosine.x[0],-sine.x[1],-cosine.x[1],sine.x[0]]),
              np.choose(q,[cosine.x[1],-sine.x[0],-cosine.x[0],sine.x[1]])))


def complete_cut_coefficients(prefix_jets, prefix_pm, prefix_hm,
                              tail_jets, tail_pm, tail_hm, radius, slope):
    """Return outward coefficient ranges of T_j minus the raw endpoint.

    The arguments are literal finite-map data. This pure algebra does not
    claim that arbitrary input arrays came from any accepted tail.
    """
    pp,ph,tp,th=map(lambda x:np.asarray(x,int),(prefix_pm,prefix_hm,tail_pm,tail_hm))
    P,T=len(pp),len(tp)
    if (prefix_jets.shape!=(3,P+len(ph)) or tail_jets.shape!=(3,T+len(th))
            or not np.all(np.isfinite(prefix_jets)) or not np.all(np.isfinite(tail_jets))
            or len(set(pp))!=len(pp) or len(set(tp))!=len(tp)
            or len(set(ph))!=len(ph) or len(set(th))!=len(th)
            or 0 not in ph or 0 not in th or 1 not in pp or 1 not in tp
            or np.any(pp%3!=1) or np.any(tp%3!=1)
            or np.any(ph%3) or np.any(th%3)):
        raise ValueError('Complete finite threefold Cartesian two-jets are required')
    pm=np.asarray(sorted(set(map(int,pp))|set(map(int,tp))),int)
    hm=np.asarray(sorted(set(map(int,ph))|set(map(int,th))),int)
    pold={int(m):j for j,m in enumerate(pp)}
    hold={int(m):P+j for j,m in enumerate(ph)}
    pnew={int(m):j for j,m in enumerate(tp)}
    hnew={int(m):T+j for j,m in enumerate(th)}
    R,w=I(radius),I(slope)
    if float(R.x[0])<=0:
        raise ValueError('The literal physical cut radius must be positive')
    wr=-7*w/R
    E=1+w.sq()
    ap=-1/E.sqrt()
    app=-w*wr/E.sq()
    def read(data,index,mode,order):
        return I(data[order,index[mode]]) if mode in index else I(0)
    rows=[[] for _ in range(3)]
    for m in pm:
        circle=I(1 if m==1 else 0)
        A=[read(tail_jets,pnew,int(m),j) for j in range(3)]
        target=[R*circle+A[0],ap*(circle+A[1]),ap.sq()*A[2]+app*(circle+A[1])]
        for j in range(3):rows[j].append(target[j]-read(prefix_jets,pold,int(m),j))
    Z=I(prefix_jets[0,hold[0]])
    for m in hm:
        zero=I(1 if m==0 else 0)
        A=[read(tail_jets,hnew,int(m),j) for j in range(3)]
        # At m=0 the identical tail mean cancels algebraically, not by
        # subtracting independent interval copies. Its derivatives do not.
        value=Z if m==0 else -A[0]
        first=-w*zero-A[1]
        second=-wr*zero-A[2]
        target=[value,ap*first,ap.sq()*second+app*first]
        for j in range(3):
            difference=(I(0) if m==0 and j==0 else
                        target[j]-read(prefix_jets,hold,int(m),j))
            rows[j].append(difference)
    return pm,hm,intervals([intervals(row) for row in rows]),dict(
        R_exact=str(fq(radius)),w_exact=str(fq(slope)),wR_exact=str(-7*fq(slope)/fq(radius)),
        ap_definition='-(1+w*w)^(-1/2)',app_definition='-w*wR/(1+w*w)^2',
        finite_mean_height_at_cut_exact=str(fq(prefix_jets[0,hold[0]])),
        tail_mean_value_cancelled_exactly=True,tail_mean_derivatives_retained=True,
        ap_interval=list(map(float,ap.x)),app_interval=list(map(float,app.x)),
        prefix_planar_modes=len(pp),tail_planar_modes=len(tp),union_planar_modes=len(pm),
        prefix_height_modes=len(ph),tail_height_modes=len(th),union_height_modes=len(hm))


def cut_angular_tables(pm,hm,coeff,N,psi_boxes,angular_width):
    """Four complete angular derivatives; no order-three call to old reader."""
    P=len(pm)
    mp.iv.dps=75
    left=[2*mp.iv.pi*j/(3*N) for j in range(N)]
    points=I(np.asarray([K.dn(float(x.a)) for x in left]),
             np.asarray([K.up(float(x.b)) for x in left]))
    result={}
    for tag,angles in [('point',points),('box',psi_boxes)]:
        ps,pc=exact_sincos(I(pm[:,None])*I(angles.x[0][None,:],angles.x[1][None,:]))
        hs,hc=exact_sincos(I(hm[:,None])*I(angles.x[0][None,:],angles.x[1][None,:]))
        for order in range(4):
            bx=[pc,-ps,-pc,ps][order]*I(pm[:,None]**order)
            by=[ps,pc,-ps,-pc][order]*I(pm[:,None]**order)
            bz=[hc,-hs,-hc,hs][order]*I(hm[:,None]**order)
            vectors=[]
            for radial in range(3):
                c=coeff.item(radial)
                x=(c.item(slice(0,P)).expand()*bx).sum(axis=0)
                y=(c.item(slice(0,P)).expand()*by).sum(axis=0)
                z=(c.item(slice(P,None)).expand()*bz).sum(axis=0)
                vectors.append(intervals([x,y,z],axis=-1))
            result[f'{tag}_cut_{order}']=intervals(vectors)
    t=I(0,float(angular_width.x[1]))
    result['box_cut_0']=(result['point_cut_0']+t*result['point_cut_1']+
                         t.sq()*result['box_cut_2']/2)
    result['box_cut_1']=result['point_cut_1']+t*result['box_cut_2']
    if not all(v.finite() for v in result.values()):
        raise ArithmeticError('Nonfinite complete cut angular enclosure')
    return result


class CutMetric(NewMetric):
    def __init__(self,tables,bundle,outdir,width=.04):
        super().__init__(tables)
        self.cut_width=fq(width)
        self.cut_start=self.target.end-self.cut_width
        if not 0<self.cut_width or self.cut_start<=self.width:
            raise ValueError('The exact center and cut repairs must have disjoint strips')
        self.cap=ActualFiniteTailV2(bundle,Path(outdir)/'verified-shared-node-index.json')
        source=json.loads(Path(self.record['source_run']).read_text())
        packet=self.cap.packet
        H=source['raw_return']['candidate_H']
        identity=self.cap.bundle['height_identity']
        reference=checked(identity['reference'])
        referenced=reference
        for part in identity['reference_key'].split('.'):
            referenced=referenced[part]
        if (identity['factor']!=1 or referenced!=H or packet['request']['height']!=H
                or packet['response']['checkpoint']['cutHeight']!=H
                or packet['config']['modes']!=source['modes']):
            raise ValueError('The tail must have the entire actual source height and mode count')
        port=checked(self.cap.bundle['source_port'])
        if (port['parameters']!=source['physical_tail_parameters'] or
                any(self.cap.parameters.get(k)!=v for k,v in port['parameters'].items())):
            raise ValueError('The full tail and prefix physical metrics differ')
        with np.load(self.record['defining_jets']['path'],allow_pickle=False) as d:
            if np.any(d['lift_jets'][:,:,-1]!=0):
                raise ValueError('A nonzero true-core endpoint needs an explicit complete cut contract')
            if np.any(d['chart_jets'][:,:,-1]!=0):
                raise ValueError('The full material phase chart must have zero cut two-jet')
            jets=d['jets'][:,:,-1].copy()
        pm,hm,coeff,self.cut_definition=complete_cut_coefficients(
            jets,self.pm,self.hm,self.cap.cut_jets,self.cap.pm,self.cap.hm,
            self.cap.parameters['rCut'],self.cap.parameters['wCut'])
        self.cut_tables=cut_angular_tables(pm,hm,coeff,self.N,
            self.tables['psi_boxes'],self.tables['angular_width'])
        self.tables.update(self.cut_tables)
        self.cut_definition.update(cut_width_exact=str(self.cut_width),
            cut_start_exact=str(self.cut_start),prefix_end_exact=str(self.target.end),
            correction='sum_j (-L)^j H_j((end-s)/L) Delta_j(psi)',
            zero_extension='s <= end-L',all_original_tail_modes_retained=True,
            full_height_identity_checked=True,tail_near_cut_reparameterization_certified=False)
        self.grid=sorted(set(self.grid+[self.cut_start]))
        self.grid=[s for s in self.grid if s>=self.cut_start]
        out=Path(outdir)/'complete-cut-angular-tables.npz'
        np.savez(out,planar_modes=pm,height_modes=hm,cut_coefficient_enclosures=np.asarray(coeff.x),
                 **{name:np.asarray(value.x) for name,value in self.cut_tables.items()})
        self.cut_data=dict(path=str(out.resolve()),sha256=sha(out))

    def cut_weights(self,s,left,right):
        if right<=self.cut_start:
            return [[I(0) for _ in range(3)] for _ in range(4)]
        if not self.cut_start<=left<=right<=self.target.end:
            raise ValueError('Split at the exact cut repair join')
        t=(I.rational(self.target.end)-s)/I.rational(self.cut_width)
        result=[[] for _ in range(4)]
        for j,poly in enumerate(HERMITE):
            c=list(poly)
            for order in range(4):
                value=I(0)
                for a in c[::-1]:value=value*t+I.rational(a)
                result[order].append(value*I.rational(
                    (-1)**(j+order)*self.cut_width**(j-order)))
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
        cw=self.cut_weights(s,left,right)
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
            cut=angular_value('cut',angular_order)
            for j in range(3):
                weight=radial_value([row[j] for row in cw],radial_order)
                value+=weight*cut.item(j)
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

    def geometry(self,left,right):
        s=I(I.rational(left).x[0],I.rational(right).x[1])
        coefficients=self.field.values(s,left,right)
        radial_lift=[v.item(0) for v in self.lift.values(s,left,right)]
        center_weights=self.weights(s,left,right)
        cut_weights=self.cut_weights(s,left,right)
        fields=[]
        for radial,angular in ((0,0),(1,0),(2,0),(0,1),(0,2),(1,1)):
            c=coefficients[radial]
            parts=[]
            for coordinate in range(3):
                section=slice(0,self.P) if coordinate<2 else slice(self.P,None)
                basis=self.tables[f'box_basis_{angular}_{coordinate}']
                parts.append((c.item(section).expand()*basis).sum(axis=0))
            value=intervals(parts,axis=-1)
            value+=radial_lift[radial]*self.tables[f'box_lift_{angular}']
            for j in range(3):
                value+=center_weights[radial][j]*self.tables[f'box_center_{angular}'].item(j)
                value+=cut_weights[radial][j]*self.tables[f'box_cut_{angular}'].item(j)
            fields.append(value.x)
        X,Xs,Xss,Xp,Xpp,Xsp=fields
        normal=K.cross(Xp,Xs)
        area=K.sqrt(K.norm2(normal))
        if np.any(area[0]<=0):
            return None
        support=K.div(K.dot(X,normal),area)
        radius=K.sqrt(K.norm2(X))
        E,F,G=K.norm2(Xs),K.dot(Xs,Xp),K.norm2(Xp)
        L,M,N=[K.div(K.dot(v,normal),area) for v in (Xss,Xsp,Xpp)]
        curvature=I.rational(Q(123,10)).x
        diagonal=np.full(area[0].shape,np.inf)
        determinant=np.full_like(diagonal,np.inf)
        for sign in (-1,1):
            aa=K.add(K.mul(E,curvature),K.scale(L,sign))
            bb=K.add(K.mul(F,curvature),K.scale(M,sign))
            cc=K.add(K.mul(G,curvature),K.scale(N,sign))
            diagonal=np.minimum(diagonal,np.minimum(aa[0],cc[0]))
            determinant=np.minimum(determinant,K.sub(K.mul(aa,cc),K.square(bb))[0])
        return dict(support_lower=float(np.min(support[0])),
            radius_upper=float(np.max(radius[1])),area_lower=float(np.min(area[0])),
            curvature_psd_diagonal_lower=float(np.min(diagonal)),
            curvature_psd_determinant_lower=float(np.min(determinant)))


def check_sources(record):
    for path,digest in record['source_hashes'].items():
        if sha(path)!=digest:
            raise ValueError('An inherited certificate source changed: '+path)


def inherit_metric(verifier,path,target):
    path=Path(path).resolve()
    record=json.loads(path.read_text())
    if (record.get('status')!='continuous_new_cartesian_prefix_metric_certified'
            or record.get('metric_certified') is not True
            or record['table_report_sha256']!=sha(verifier.report_path)
            or record['source_run_sha256']!=verifier.record['source_run_sha256']
            or record['defining_jets']!=verifier.record['defining_jets']
            or record['exact_target_definition']!=verifier.target.definition
            or record['full_radial_range']!=['0',str(verifier.target.end)]):
        raise ValueError('The inherited metric proof is not for this exact uncut map and target')
    check_sources(record)
    leaves=path.parent/'complete-leaves.jsonl'
    if sha(leaves)!=record['complete_leaves_sha256']:
        raise ValueError('The inherited complete metric leaf data changed')
    cursor,count,used,peak=Q(0),0,0,Q(0)
    for line in leaves.read_text().splitlines():
        row=json.loads(line)
        left,right=Q(row['left']),Q(row['right'])
        bound=fq(row['bound'])
        if left!=cursor or not left<right or not 0<=bound<=target:
            raise ValueError('The old leaves do not form an exact admissible full cover')
        cursor=right;count+=1
        if left<verifier.cut_start:
            used+=1;peak=max(peak,bound)
    if cursor!=verifier.target.end or count!=record['accepted']:
        raise ValueError('The old full metric cover is incomplete')
    return dict(source=str(path),source_sha256=sha(path),
        full_leaf_data_sha256=sha(leaves),full_old_cover_checked_exactly=True,
        inherited_radial_range=['0',str(verifier.cut_start)],
        overlapping_old_leaf_count=used,metric_upper_exact=str(peak),
        correction_identically_zero_on_this_closed_complement=True)


def inherit_geometry(verifier,path,rational_path):
    path,rational_path=Path(path).resolve(),Path(rational_path).resolve()
    record=json.loads(path.read_text())
    rational=json.loads(rational_path.read_text())
    if (record.get('status')!='continuous_new_prefix_geometry_certified'
            or record.get('complete') is not True or record.get('failed_boxes')!=0
            or record['source_run_sha256']!=verifier.record['source_run_sha256']
            or list(map(fq,record['covered_radial']))!=[Q(0),verifier.target.end]
            or record['full_angular_range']!='[0,2*pi]'
            or rational.get('status')!='same_new_prefix_exact_rational_curvature_budget_certified'
            or rational['source_certificate_sha256']!=sha(path)
            or rational['exact_target_curvature']!='123/10'
            or rational['continuous_prefix_absolute_curvature_at_most_12p3'] is not True
            or Q(rational['exact_remaining_psd_lower'])<=0):
        raise ValueError('Require the complete same-map rational-curvature geometry certificate')
    check_sources(record)
    source=Path(__file__).with_name('cartesian_prefix_curvature_rounding.py')
    if sha(source)!=rational['source_sha256']:
        raise ValueError('The rational-curvature postprocessor changed')
    for file,digest in rational['data_sha256'].items():
        if sha(file)!=digest:
            raise ValueError('Inherited rational-curvature input changed: '+file)
    old=path.parent/'actual-prefix-exact-defining-jets.npz'
    if sha(old)!=record['defining_jets_sha256']:
        raise ValueError('The old geometry map definition changed')
    with np.load(old,allow_pickle=False) as old_data, np.load(
            verifier.record['defining_jets']['path'],allow_pickle=False) as new_data:
        keys=list(old_data.files)
        if not all(k in new_data and np.array_equal(old_data[k],new_data[k]) for k in keys):
            raise ValueError('The old geometry and current map defining real values differ')
    return dict(source=str(path),source_sha256=sha(path),
        rational_curvature_source=str(rational_path),rational_curvature_sha256=sha(rational_path),
        all_original_defining_arrays_checked=keys,curvature_exact='123/10',
        inherited_radial_range=['0',str(verifier.cut_start)],
        bounds={k:record['bounds'][k] for k in ('support_lower','radius_upper','area_lower')},
        exact_curvature_comes_from_rational_postprocessor=True,
        correction_identically_zero_on_this_closed_complement=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('tables','geometry-bundle','base-metric','base-geometry','base-curvature','outdir'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--cut-width',type=float,default=.04)
    parser.add_argument('--target',type=float,default=9.9e-7)
    parser.add_argument('--max-cells',type=int,default=100000)
    args=parser.parse_args()
    repo,out=SCRIPTS.parents[2],args.outdir.resolve()
    target=fq(args.target)
    if out==repo or repo in out.parents or not 0<target<=Q(1,1000000):
        raise ValueError('Original metric budget and all generated arrays outside Git are required')
    out.mkdir(parents=True,exist_ok=False)
    begin=time.monotonic()
    report=dict(status='loading_full_height_cut_definition',scope=__doc__,
        prefix_metric_certified=False,prefix_geometry_certified=False,whole_surface=False,
        target_exact_binary=str(target),accepted=0,splits=0,attempts=0,
        source_sha256=sha(__file__),table_report=str(args.tables.resolve()),
        table_report_sha256=sha(args.tables),geometry_bundle=str(args.geometry_bundle.resolve()),
        geometry_bundle_sha256=sha(args.geometry_bundle),tail_reparameterization_certified=False)
    save(out/'summary.json',report)
    try:
        verifier=CutMetric(args.tables,args.geometry_bundle,out,args.cut_width)
        old_metric=inherit_metric(verifier,args.base_metric,target)
        old_geometry=inherit_geometry(verifier,args.base_geometry,args.base_curvature)
        sources=[Path(__file__),Path(__file__).with_name('cartesian_prefix_metric.py'),
            Path(__file__).with_name('cartesian_prefix_metric_target.py'),
            Path(__file__).parents[1]/'tail/actual_closed_map_v2.py',
            SCRIPTS/'resume_20261126/seam_export_tail_geometry_v2.py',
            SCRIPTS/'resume_20261126/seam_tail_spectrum_v2.py']
        bounds=dict(old_geometry['bounds'])
        cut_psd={}
        peak=float(Q(old_metric['metric_upper_exact']))
        report.update(status='continuous_full_cut_prefix_running',
            inherited_metric=old_metric,inherited_geometry=old_geometry,
            cut_definition=verifier.cut_definition,cut_data=verifier.cut_data,
            actual_complete_tail_stages=verifier.cap.S,
            complete_tail_spectrum=verifier.cap.spectrum,
            exact_target_definition=verifier.target.definition,
            source_hashes={str(p.resolve()):sha(p) for p in sources},
            source_run_sha256=verifier.record['source_run_sha256'],
            defining_jets=verifier.record['defining_jets'],peak=peak,bounds=bounds,
            initial_cut_radial_cells=len(verifier.grid)-1,
            angular_boxes_per_sector=verifier.N,curvature_exact='123/10')
        pending=[(l,r,0) for l,r in zip(verifier.grid[:-1],verifier.grid[1:])][::-1]
        with (out/'complete-cut-leaves.jsonl').open('x') as leaves:
            while pending:
                left,right,depth=pending.pop();report['attempts']+=1
                upper,details=verifier.enclose(left,right)
                geo=verifier.geometry(left,right)
                geometry_ok=(geo is not None and fq(geo['support_lower'])>=Q(87,1000)
                    and fq(geo['radius_upper'])<=Q(67,50) and geo['area_lower']>0
                    and geo['curvature_psd_diagonal_lower']>0
                    and geo['curvature_psd_determinant_lower']>0)
                if fq(upper)<=target and geometry_ok:
                    report['accepted']+=1;peak=max(peak,upper)
                    for key,value in geo.items():
                        if key in bounds:
                            bounds[key]=(max if key=='radius_upper' else min)(bounds[key],value)
                        elif key.startswith('curvature_psd_'):
                            cut_psd[key]=min(cut_psd.get(key,value),value)
                    leaves.write(json.dumps(dict(left=str(left),right=str(right),metric_bound=upper,
                        metric_details=details,geometry=geo),allow_nan=False)+'\n')
                else:
                    if depth>=28 or report['accepted']+len(pending)>=args.max_cells:
                        report.update(status='continuous_cut_prefix_unresolved',
                            unresolved_interval=[str(left),str(right)],
                            unresolved_metric_bound=upper,unresolved_metric_details=details,
                            unresolved_geometry=geo,remaining=len(pending)+1)
                        break
                    middle=(left+right)/2
                    pending.extend([(middle,right,depth+1),(left,middle,depth+1)])
                    report['splits']+=1
                report.update(peak=peak,bounds=bounds,new_cut_curvature_psd_minima=cut_psd,
                    seconds=time.monotonic()-begin)
                if report['attempts']%10==0:
                    save(out/'summary.json',report)
                    print(json.dumps(dict(stage='full_cut_prefix',accepted=report['accepted'],
                        attempts=report['attempts'],splits=report['splits'],remaining=len(pending),
                        s=float(right),peak=peak,seconds=report['seconds'])),flush=True)
            else:
                report.update(status='continuous_full_cut_prefix_metric_geometry_certified',
                    prefix_metric_certified=True,prefix_geometry_certified=True,
                    full_radial_range=['0',str(verifier.target.end)],
                    new_cut_radial_range=[str(verifier.cut_start),str(verifier.target.end)],
                    full_angular_range='[0,2*pi], exact threefold covariance',
                    all_phase_prefix_bounds=True,metric_target_unchanged=True,
                    full_tail_near_cut_reparameterization_still_requires_separate_certificate=True)
        report.update(seconds=time.monotonic()-begin,
            complete_cut_leaves_sha256=sha(out/'complete-cut-leaves.jsonl'))
        save(out/'summary.json',report)
        print(json.dumps({k:report[k] for k in ['status','accepted','splits','peak','seconds']}),flush=True)
    except Exception as error:
        (out/'exception.txt').write_text(traceback.format_exc())
        report.update(status='continuous_cut_prefix_execution_failed',error=repr(error),
            seconds=time.monotonic()-begin)
        save(out/'summary.json',report)
        raise


if __name__=='__main__':
    main()
