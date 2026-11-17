#!/usr/bin/env python3
"""Continuous, full-angle metric bound for the actual finite m3 tail.

The true background is R27's normalized real-integral background.  A batch
of numerical inverse proposals is enclosed by true partial integrals; the
proved global |w_R|<11 transfers each proposal to its actual requested R.
Finite Fourier coefficient algebra then encloses the metric at that R and
its full radial derivative on the whole adjacent interval.  Adaptive radial
subdivision is accepted only by the resulting continuous inequality.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse
import bisect
import hashlib
import json
import math
import subprocess
import time
import numpy as np

import interval_tail_metric as tm
from certify_background_sharp import lower,upper,interval,q,bound,mp,iv
from certify_background_queries import TrueBackgroundQueries,integrate_range,saved_interval


def qview(v):
    v=Q(v)
    return dict(numerator=str(v.numerator),denominator=str(v.denominator),display_only=float(v))


def up_rows(values):
    n=values.shape[1]
    gamma=4*n*2.**-53
    return tm.up(np.sum(values,axis=1)/(1-gamma)+n*np.nextafter(0.,1.))


def deep_bound(tail,certificate):
    """Entire raw cells n>=1 by separate planar/height derivative bounds."""
    f=tail.f
    groups={}
    i=0
    for record in f.meta['files']:
        n=record['rawCell']
        groups.setdefault(n,[i,i])
        i+=record['rows']-1
        groups[n][1]=i
    assert i==len(tail.lengths)
    split=tail.rnodes[groups[0][0]]
    r1lo=Q(certificate['cell0_inner_radius']['lower_exact'])
    W=Q(1,49)+11*max(Q(0),split-r1lo)
    assert W<Q(21,1000)
    W=Q(21,1000)
    assert split<tail.cut-tail.width
    L=tm.mul(tm.exact(f.unscaled_lengths[:,None]),tm.rational_interval(f.radial_scale))
    b0=tm.exact(f.first[:-1]);b4=tm.exact(f.first[1:])
    b1=tm.add(b0,tm.scale(tm.mul(L,tm.exact(f.second[:-1])),.25))
    b3=tm.sub(b4,tm.scale(tm.mul(L,tm.exact(f.second[1:])),.25))
    b2=tm.div(tm.sub(tm.sub(tm.sub(tm.sub(tm.scale(tm.exact(f.midpoint),16),b0),tm.scale(b1,4)),tm.scale(b3,4)),b4),tm.exact(6))
    bs=[b0,b1,b2,b3,b4]
    U=np.maximum.reduce([tm.magnitude(v)for v in bs])
    V=(tail.left[0][:-1],tail.left[1][:-1])
    Vm=tm.magnitude(V)
    for b in bs:
        V=tm.add(V,tm.div(tm.mul(L,b),tm.exact(5)))
        Vm=np.maximum(Vm,tm.magnitude(V))
    P=f.P
    upr=up_rows(U[:,:P]);uzr=up_rows(U[:,P:])
    upt=up_rows(tm.up(Vm[:,:P]*abs(f.planar_modes)[None,:]))
    uzt=up_rows(tm.up(Vm[:,P:]*f.height_modes[None,:]))
    reports=[]
    for n,(first,last)in groups.items():
        if n==0:
            continue
        p,z,pt,zt=[Q.from_float(float(v[first:last].max()))for v in [upr,uzr,upt,uzt]]
        rlo,rhi=tail.rnodes[first],tail.rnodes[last]
        A=2*p+p*p+2*W*z+z*z
        B=(pt+rhi*p+p*pt+(W+z)*zt)/rlo
        C=(2*rhi*pt+pt*pt+zt*zt)/(rlo*rlo)
        op=max(A+B,C+B)
        reports.append(dict(raw_cell=n,spans=last-first,relative_operator_upper=qview(op),
                            planar_radial_l1=qview(p),height_radial_l1=qview(z),
                            planar_angular_l1=qview(pt),height_angular_l1=qview(zt)))
    return dict(reports=reports,split_radius=qview(split),background_slope_upper=qview(W),
                maximum=max(Q(v['relative_operator_upper']['numerator'])/Q(v['relative_operator_upper']['denominator'])for v in reports)),groups[0][0]


class BackgroundGrid:
    """Independent true-radius enclosures at a reusable sorted x grid."""
    def __init__(self,constants,certificate,source,checkpoint,piece_width):
        self.true=TrueBackgroundQueries(constants,certificate,piece_width)
        cfg=constants['parameters']
        expected=dict(rCut=.3,wCut=.08,curvatureBound=8,delta0=.006,R=64,a=2.75,
                      etaPower=1.5,etaRatioAtN0=.05,orientation=1,prefixR=2,
                      prefixEnd=15,prefixReturnStart=8,protectCell=160,slopeCap=.02,
                      capTransition=2,capMode='cut-preserving')
        assert all(cfg[k]==value for k,value in expected.items())
        assert cfg['pulseCaps']==[[.4,.02]] and cfg['valleyCaps']==[.1]
        assert cfg['warpWeightLevels']==[[1,.5,3,.05,1]]
        assert cfg['valleyControls'][:6]==[3.125,2.8125,4.0625,5,5.25,4.0625]
        assert all(value==0 for value in cfg['valleyControls'][6:])
        self.tolerance=mp.mpf(piece_width)
        self.nodes={}
        self.responses={}
        self.integrations=[]
        self.rows={}
        server=Path(__file__).with_name('background_metric_query.mjs')
        self.proc=subprocess.Popen(['node',str(server),str(source),str(checkpoint)],
                                    stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True,bufsize=1)
        self.info=json.loads(self.proc.stdout.readline())
        assert self.info.get('ready')
        # R21: |kappa_r|<=8 and 0<=w<=.41 on the full true background.
        assert 64*(1+Q(41,100)**2)**3<121
        self.lipschitz=iv.mpf(11)

    def proposals(self,radii):
        missing=[r for r in sorted(set(radii))if r not in self.responses]
        for first in range(0,len(missing),256):
            batch=missing[first:first+256]
            self.proc.stdin.write(json.dumps(dict(radii=batch))+'\n');self.proc.stdin.flush()
            result=json.loads(self.proc.stdout.readline())
            assert 'error'not in result,result
            for r,row in zip(batch,result['rows']):
                self.responses[r]=row

    def integrate(self,j,left,right):
        values,stats=integrate_range(self.true.piece(0,j),mp.mpf(left),mp.mpf(right),self.tolerance)
        self.integrations.append(dict(segment=j,left=left,right=right,**stats))
        return values[0]+self.true.normalization*values[1]

    def initialize(self,radii):
        self.proposals(radii)
        points={j:{0.,1.}for j in range(9)}
        for r in radii:
            proposal=self.responses[r]
            if proposal.get('cell')==0:
                points[proposal['segment']].add(proposal['x'])
        current=self.true.cell_start(0)
        for j in range(9):
            xs=sorted(points[j]);values=[current]
            for left,right in zip(xs[:-1],xs[1:]):
                current+=self.integrate(j,left,right)
                values.append(current)
            self.nodes[j]=dict(x=xs,radius=values)
            print(json.dumps(dict(event='true_background_piece',segment=j,nodes=len(xs),
                                  endpoint_width=float(upper(current)-lower(current)))),flush=True)
        cut=q(self.true.bg.cfg['rCut'])
        assert lower(current)<=lower(cut)<=upper(cut)<=upper(current)
        self.finish_rows(radii)

    def add(self,radii):
        self.proposals(radii)
        for r in sorted(set(radii)):
            if r in self.rows:
                continue
            proposal=self.responses[r]
            if proposal.get('cell')!=0:
                continue
            j,x=proposal['segment'],proposal['x']
            nodes=self.nodes[j]
            index=bisect.bisect_left(nodes['x'],x)
            if index<len(nodes['x'])and nodes['x'][index]==x:
                continue
            assert 0<index<len(nodes['x'])
            previous=nodes['x'][index-1]
            value=nodes['radius'][index-1]+self.integrate(j,previous,x)
            nodes['x'].insert(index,x);nodes['radius'].insert(index,value)
        self.finish_rows(radii)

    def finish_rows(self,radii):
        for r in sorted(set(radii)):
            if r in self.rows:
                continue
            proposal=self.responses[r]
            if proposal.get('cell')==0:
                j,x=proposal['segment'],proposal['x']
                nodes=self.nodes[j]
                index=bisect.bisect_left(nodes['x'],x)
                assert nodes['x'][index]==x
                true_radius=nodes['radius'][index]
            else:
                # The finite inner cut differs from the true cell0 boundary
                # by only its certified interval.  A proposal on cell1 uses
                # that same boundary plus the global physical Lipschitz bound.
                assert proposal.get('cell')==1
                j,x=0,0.
                true_radius=self.true.cell_start(0)
                assert max(abs(lower(true_radius)-r),abs(upper(true_radius)-r))<mp.mpf('1e-8')
            w0=self.true.piece(0,j).evaluate(iv.mpf(x),0)[0].c[0]
            shift=q(r)-true_radius
            w=w0+interval(-11,11)*shift
            w=interval(max(mp.mpf(0),lower(w)),min(upper(iv.mpf(41)/100),upper(w)))
            self.rows[r]=dict(radius=r,segment=j,x=x,true_radius=bound(true_radius),
                              exact_w_at_x=bound(w0),true_w=bound(w),
                              proposal_radius_error_upper=math.nextafter(float(max(abs(lower(shift)),abs(upper(shift)))),math.inf))

    def value(self,r):
        row=self.rows[r]['true_w']
        return np.asarray(row['lower']),np.asarray(row['upper'])

    def close(self):
        self.proc.stdin.close();self.proc.wait(timeout=30)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ['manifest','tail-reader','constants','background-certificate','source-topic','checkpoint','out']:
        parser.add_argument('--'+key,type=Path,required=True)
    parser.add_argument('--threshold',default='1e-6')
    parser.add_argument('--piece-width',default='1e-18')
    parser.add_argument('--max-depth',type=int,default=16)
    args=parser.parse_args()
    started=time.monotonic()
    certificate=json.loads(args.background_certificate.read_text())
    constants=json.loads(args.constants.read_text())
    sha=lambda path:hashlib.sha256(path.read_bytes()).hexdigest()
    assert certificate['input_sha256']==sha(args.constants)
    threshold=Q(args.threshold)
    tail=tm.IntervalFiniteTail(args.manifest,args.tail_reader)
    deep,first=deep_bound(tail,certificate)
    assert deep['maximum']<threshold,dict(deep_maximum=float(deep['maximum']))
    deep_maximum=deep['maximum']
    deep['maximum']=qview(deep['maximum'])
    print(json.dumps(dict(event='deep_cells_pass',relative_operator_upper=deep['maximum']['display_only'],
                          shallow_spans=len(tail.lengths)-first)),flush=True)
    endpoints=tail.rnodes[first:].copy();endpoints[-1]=tail.cut
    pending=[(lo,hi,0)for lo,hi in zip(endpoints[:-1],endpoints[1:])]
    center=lambda row:float((row[0]+row[1])/2)
    grid=BackgroundGrid(constants,certificate,args.source_topic,args.checkpoint,args.piece_width)
    accepted=[]
    passes=[]
    try:
        grid.initialize([center(row)for row in pending])
        iteration=0
        while pending:
            maximum=0.;failed=[]
            if iteration:
                grid.add([center(row)for row in pending])
            for index,(lo,hi,depth)in enumerate(pending):
                rc=center((lo,hi,depth));R0=Q.from_float(rc)
                assert lo<R0<hi
                distance=max(R0-lo,hi-R0)
                w=grid.value(rc)
                jets=tail.coefficients(R0)
                point=tm.metric_coefficients(*jets,tail.f.planar_modes,tail.f.height_modes,
                                              tm.rational_interval(R0),w,(np.asarray(-11.),np.asarray(11.)))
                jets_interval=tail.coefficients(lo,hi)
                extent=tm.mul(tm.exact(11),tm.rational_interval(distance))
                w_interval=tm.add(w,(-extent[1],extent[1]))
                w_interval=(np.maximum(w_interval[0],0),np.minimum(w_interval[1],float(tm.rational_interval(Q(41,100))[1])))
                derivative=tm.metric_coefficients(*jets_interval,tail.f.planar_modes,tail.f.height_modes,
                    (tm.rational_interval(lo)[0],tm.rational_interval(hi)[1]),w_interval,(np.asarray(-11.),np.asarray(11.)))
                radius_upper=float(tm.rational_interval(distance)[1])
                total=float(tm.up(point['operator_upper']+tm.up(radius_upper*derivative['derivative_operator_upper'])))
                maximum=max(maximum,total)
                if Q.from_float(total)<threshold:
                    accepted.append(dict(left=qview(lo),right=qview(hi),depth=depth,
                        center=rc,point_metric_upper=point['operator_upper'],
                        radial_derivative_upper=derivative['derivative_operator_upper'],
                        continuous_metric_upper=total))
                else:
                    assert depth<args.max_depth,dict(radius=rc,bound=total,depth=depth)
                    mid=(lo+hi)/2
                    failed.extend([(lo,mid,depth+1),(mid,hi,depth+1)])
                if index%256==0:
                    print(json.dumps(dict(event='metric_interval_batch',iteration=iteration,
                        checked=index+1,total=len(pending),accepted=len(accepted),
                        children_pending=len(failed),maximum_attempted_bound=maximum)),flush=True)
            passes.append(dict(iteration=iteration,intervals=len(pending),maximum_attempted_bound=maximum,
                               refined_parent_intervals=len(failed)//2))
            pending=failed;iteration+=1
    finally:
        grid.close()
    accepted.sort(key=lambda row:Q(row['left']['numerator'])/Q(row['left']['denominator']))
    exact_end=lambda row,key:Q(row[key]['numerator'])/Q(row[key]['denominator'])
    assert exact_end(accepted[0],'left')==endpoints[0]
    assert exact_end(accepted[-1],'right')==tail.cut
    assert all(exact_end(a,'right')==exact_end(b,'left')for a,b in zip(accepted[:-1],accepted[1:]))
    final_max=max(max(row['continuous_metric_upper']for row in accepted),float(tm.rational_interval(deep_maximum)[1]))
    grid_path=args.out.with_name(args.out.stem+'-background-grid.json')
    grid_path.write_text(json.dumps(dict(scope='True partial-integral enclosures used by the continuous metric proof.',
        rows=[grid.rows[r]for r in sorted(grid.rows)],integration_calls=grid.integrations),indent=2)+'\n')
    detail_path=args.out.with_name(args.out.stem+'-intervals.json')
    detail_path.write_text(json.dumps(accepted,indent=2)+'\n')
    sources=[Path(__file__),Path(__file__).with_name('interval_tail_metric.py'),
             Path(__file__).with_name('certify_background_queries.py'),Path(__file__).with_name('certify_background_sharp.py')]
    result=dict(scope=__doc__,command=__import__('sys').argv,source_sha256={p.name:sha(p)for p in sources},
        inputs={str(p.resolve()):sha(p)for p in [args.manifest,args.tail_reader,args.constants,args.background_certificate,args.checkpoint]},
        threshold=args.threshold,deep_cells=deep,shallow_original_spans=len(endpoints)-1,
        accepted_continuous_intervals=len(accepted),maximum_subdivision_depth=max(v['depth']for v in accepted),
        continuous_full_angle_metric_upper=final_max,passes=passes,
        true_background_sample_centers=len(grid.rows),
        largest_true_radius_proposal_error_upper=max(v['proposal_radius_error_upper']for v in grid.rows.values()),
        partial_integration_leaf_panels=sum(v['panels']for v in grid.integrations),
        global_background_wR_abs_bound=11,angular_sampling_used=False,
        full_phase_reason='Physical material-angle shifts and ambient rotations preserve the relative metric norm.',
        exact_isometry_claimed=False,entire_closed_prefix_metric_certified=False,
        scratch_details={str(p):sha(p)for p in [grid_path,detail_path]},seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(success=True,continuous_full_angle_metric_upper=final_max,
                         intervals=len(accepted),seconds=result['seconds'])),flush=True)


if __name__=='__main__':
    main()
