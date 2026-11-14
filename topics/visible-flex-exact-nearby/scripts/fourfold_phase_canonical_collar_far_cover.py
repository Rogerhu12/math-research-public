#!/usr/bin/env python3
"""Actual continuous continuation of the degree-six chart across spline knots.

Only ordinary coefficient bounds are extracted away from the root.  Exact
span selection is retained even for adjacent binary knots.  No root-germ
analytic continuation is identified with the actual piecewise spline.
"""
from __future__ import annotations
import argparse
from collections import deque,OrderedDict
from fractions import Fraction
import gzip,json,math,time
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_parameter_germ import provenance
from fourfold_phase_canonical_collar_centered import CenteredPhysicalRootGeometry
from fourfold_phase_canonical_collar_far import OrdinarySpanGeometry,ordinary_canonical_operator
from fourfold_phase_canonical_collar_finite import (
    FiniteRootCoordinates,finite_canonical_operator,root_potential_coefficients,
    physical_polynomial_trial,trial_residual_coefficients,sha)


def st(v):return arb(v).str(50)
def interval(v):return {'lower':st(v.lower()),'upper':st(v.upper())}


class Cover:
    def __init__(self,args):
        self.root=CenteredPhysicalRootGeometry(args.object,args.half_width,args.root_certificate,nodes=args.nodes)
        self.model=OrdinarySpanGeometry(args.object,args.half_width,nodes=args.nodes)
        self.root_cache=OrderedDict()
    def root_values(self,left,right):
        key=left,right
        if key not in self.root_cache:
            angle=(exact_arb((left+right)/4)+arb(0,exact_arb((right-left)/4)))*arb.pi()
            principal=self.root.principal(angle,at_root=True)
            self.root_cache[key]=(angle,FiniteRootCoordinates(principal,self.root.scale),
                                  root_potential_coefficients(principal,self.root.scale))
            while len(self.root_cache)>32:self.root_cache.popitem(last=False)
        self.root_cache.move_to_end(key)
        return self.root_cache[key]
    def evaluate(self,left,right,a,b,span):
        angle,coords,root_values=self.root_values(left,right)
        self.model.prepare_cell(a,b,span=span)
        actual=self.model.principal(angle)
        offset=self.model.center-self.root.root
        if not offset>0:raise ValueError('ordinary continuation touches an unresolved root')
        chart=coords.positive(offset,self.model.m-1,self.model.n)
        values=ordinary_canonical_operator(actual,chart,self.model.scale)
        amp=physical_polynomial_trial(root_values,chart,offset,self.model.scale)
        residual=trial_residual_coefficients(values,amp,self.model.scale)
        positive={}
        for name in ('defining_ratio','ys','pt','J','A11','height','physical_source_factor'):
            v=values[name].coefficient(0,0).real
            if not v>0 or not v.is_finite():raise ValueError('ordinary finite chart not positive: '+name)
            positive[name]=interval(v)
        derivatives={}
        for name,v in {**values,**residual}.items():
            if name=='Vy':continue
            if v.n<3:raise ValueError('ordinary full-lag source lacks two true angle derivatives')
            row=[(abs(v.coefficient(0,j).real)*math.factorial(j)).upper() for j in range(3)]
            if not all(z.is_finite() for z in row):raise ValueError('nonfinite ordinary source coefficient')
            derivatives[name]=list(map(st,row))
        return dict(exact_quarter_interval=list(map(str,(left,right))),
                    exact_physical_radial_interval=list(map(str,(a,b))),
                    exact_scalar_span=list(map(str,span)),
                    positive_offset=interval(offset),positive_chart_coefficients=positive,
                    ordinary_physical_theta_derivatives=derivatives)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--root-certificate',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json'))
    ap.add_argument('--half-width',type=Fraction,default=Fraction(1,2500000))
    ap.add_argument('--left',type=Fraction,default=Fraction(5972,25000))
    ap.add_argument('--right',type=Fraction,default=Fraction(243,1000))
    ap.add_argument('--radial-width',type=Fraction,default=Fraction(1,8192))
    ap.add_argument('--angle-cells',type=int,default=256)
    ap.add_argument('--first-cell',type=int,default=0)
    ap.add_argument('--last-cell',type=int,default=128)
    ap.add_argument('--max-depth',type=int,default=12)
    ap.add_argument('--nodes',type=int,default=512)
    ap.add_argument('--bits',type=int,default=256)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if (not args.left<args.right or args.radial_width<=0 or args.angle_cells%2
            or not 0<=args.first_cell<args.last_cell<=args.angle_cells//2
            or args.max_depth<0):
        raise ValueError('invalid actual ordinary domain')
    ctx.prec,ctx.cap=args.bits,32;start=time.monotonic();cover=Cover(args)
    knots=[args.left]+[k for k in cover.model.knots if args.left<k<args.right]+[args.right]
    radial=[]
    for a,b in zip(knots,knots[1:]):
        index=__import__('bisect').bisect_right(cover.model.knots,(a+b)/2)-1
        span=cover.model.knots[index],cover.model.knots[index+1]
        number=math.ceil((b-a)/args.radial_width)
        for j in range(number):radial.append((a+(b-a)*j/number,a+(b-a)*(j+1)/number,span))
    queue=deque((Fraction(j,args.angle_cells),Fraction(j+1,args.angle_cells),a,b,span,0,0)
                for a,b,span in radial for j in range(args.first_cell,args.last_cell))
    report=dict(kind='actual_finite_chart_ordinary_positive_continuous_cover',proved=False,
      source_sha256=sha(__file__),object=provenance(cover.model.target,args.object),
      root_certificate_sha256=sha(args.root_certificate),exact_radial_range=list(map(str,(args.left,args.right))),
      first_cell=args.first_cell,last_cell=args.last_cell,angle_cells=args.angle_cells,
      initial_radial_intervals=[list(map(str,(a,b,*sp))) for a,b,sp in radial],
      dependencies={name:sha(Path(__file__).parent/name) for name in (
       'fourfold_phase_canonical_collar_far.py','fourfold_phase_canonical_collar_finite.py',
       'fourfold_phase_canonical_collar_centered.py','fourfold_phase_root_potential_complex_strip.py',
       'fourfold_phase_beta_parameter_germ.py','fourfold_phase_beta_bulk_interval.py')},
      cells=[],failed_cells=[],attempts=0,
      scope=['Actual ordinary scalar germ is reselected at every exact common knot.',
       'All recorded source coefficient bounds are ordinary bounds away from the root.',
       'Higher one-sided radial jets are used only internally; no global analyticity or high radial continuity is asserted.',
       'Completed coefficient coverage is not a final Airy reflection or cutoff norm.'])
    def save():
        report['seconds']=time.monotonic()-start
        report['pending']=[[str(l),str(r),str(a),str(b),list(map(str,sp)),ad,rd]
                           for l,r,a,b,sp,ad,rd in queue]
        args.out.parent.mkdir(parents=True,exist_ok=True);tmp=args.out.with_suffix(args.out.suffix+'.tmp')
        with gzip.open(tmp,'wt') as f:json.dump(report,f,indent=2);f.write('\n')
        tmp.replace(args.out)
    while queue:
        left,right,a,b,sp,ad,rd=queue.popleft();report['attempts']+=1
        try:
            row=cover.evaluate(left,right,a,b,sp);row.update(angle_depth=ad,radial_depth=rd)
            report['cells'].append(row)
        except (ValueError,ZeroDivisionError) as exc:
            # Alternate geometric widths; both axes are physical exact intervals.
            if ad<args.max_depth and (ad<=rd+2 or rd>=args.max_depth):
                mid=(left+right)/2
                queue.appendleft((mid,right,a,b,sp,ad+1,rd));queue.appendleft((left,mid,a,b,sp,ad+1,rd))
            elif rd<args.max_depth:
                mid=(a+b)/2
                queue.appendleft((left,right,mid,b,sp,ad,rd+1));queue.appendleft((left,right,a,mid,sp,ad,rd+1))
            else:
                report['failed_cells'].append(dict(angle=list(map(str,(left,right))),radial=list(map(str,(a,b))),reason=str(exc)))
                save();print(json.dumps({'unresolved':report['failed_cells'][-1]}),flush=True);return
        if report['attempts']%32==0:
            save();print(json.dumps({'attempts':report['attempts'],'accepted':len(report['cells']),
               'pending':len(queue),'seconds':report['seconds']}),flush=True)
    # Exact rectangular tiling is checked by slicing at every actual radial endpoint.
    endpoints=sorted(set(Fraction(z) for row in report['cells'] for z in row['exact_physical_radial_interval']))
    if endpoints[0]!=args.left or endpoints[-1]!=args.right:raise ValueError('ordinary radial endpoint mismatch')
    for a,b in zip(endpoints,endpoints[1:]):
        cursor=Fraction(args.first_cell,args.angle_cells)
        intervals=sorted(tuple(map(Fraction,row['exact_quarter_interval'])) for row in report['cells']
          if Fraction(row['exact_physical_radial_interval'][0])<=a<b<=Fraction(row['exact_physical_radial_interval'][1]))
        for l,r in intervals:
            if l!=cursor or not r>l:raise ValueError('ordinary rectangular cover has a gap or overlap')
            cursor=r
        if cursor!=Fraction(args.last_cell,args.angle_cells):raise ValueError('ordinary angular endpoint mismatch')
    report['proved']=(args.first_cell==0 and args.last_cell==args.angle_cells//2 and not report['failed_cells'])
    report['covered_specified_range']=True;save()
    print(json.dumps({'proved':report['proved'],'cells':len(report['cells']),'seconds':report['seconds']}),flush=True)


if __name__=='__main__':main()
