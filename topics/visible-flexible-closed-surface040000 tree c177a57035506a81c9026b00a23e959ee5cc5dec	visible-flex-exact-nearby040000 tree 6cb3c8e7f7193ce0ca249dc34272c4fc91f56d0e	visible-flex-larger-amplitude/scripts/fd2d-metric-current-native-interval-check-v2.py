#!/usr/bin/env python3
"""One small actual-input check of the thin current-field interval pieces.

No BVP, F/J, body ODE, global residual enclosure, or whole-domain certificate.
The finite multiprecision comparisons are implementation evidence, not the
proof of the interval formulas. The supplied saved field is never changed.
"""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
from fractions import Fraction as F
from pathlib import Path
import json
import resource
import time
import traceback

import mpmath as mp
import numpy as np
from flint import arb,ctx

from fd2d_gc_archive_arrays import identity
from fd2d_gc_current_native_interval import (
    CurrentNativeIntervalPieces,Jet,ProfileBox,ChartBox,aq,interval,rational,
    rational_pair,bound_record,compose_R153,compose_R155,connection_box,UnresolvedInterval)
from fd2d_gc_current_primitive_interval import ExactZeroEndPrimitive,propagate_piece_budget


def mq(value):
    q=rational(value)
    return mp.mpf(q.numerator)/q.denominator


def mp_point(value):
    # Only an independent finite numerical comparison. A point comparison
    # never establishes a continuous enclosure for an unknown function.
    return arb(mp.nstr(value,110)).mid()


def raw_oracle(parts,cell,s,xi):
    left,right=parts.mesh[cell:cell+2]
    t=mq((s-left)/(right-left));h=mq(right-left)
    answer=[]
    for offset,count,sine in ((0,parts.e,False),(parts.e,parts.K,True),(parts.d,parts.e,False)):
        out=[mp.mpf(0) for unused in range(5)]
        for j in range(count):
            k=j+1 if sine else j;f=2*k
            a,b=(mq(parts.coefficients[row,offset+j]) for row in (cell,cell+1))
            c=(1-t)*a+t*b;cs=(b-a)/h
            sn,co=mp.sin(f*xi),mp.cos(f*xi)
            basis,db=(sn,f*co) if sine else (co,-f*sn)
            out[0]+=c*basis;out[1]+=cs*basis;out[2]+=c*db
            out[3]-=f*f*c*basis;out[4]+=cs*db
        answer.append(out)
    return answer


def tail_oracle(parts,u):
    y=mq(parts.tail_radius)*mp.sin(u)
    q=(abs(y)-mq(parts.tail_flat))/mq(parts.tail_width)
    controls=parts.parameters[parts.reader.tail_parameter_slice]
    degree=len(controls)-1
    if q<=0 or q>=1:k=mp.mpf(0)
    else:
        k=630/mq(parts.tail_width)*sum(mq(c)*mp.binomial(degree,j)*
               q**(j+4)*(1-q)**(degree-j+4) for j,c in enumerate(controls))
    sn,cs=mp.sin(u),mp.cos(u)
    return k*cs*cs,-k*sn*cs,k*sn*sn


def assert_jet_contains(jet,values,scope):
    for name,value in zip(('value','s','xi','xixi','sxi'),values):
        ball=getattr(jet,name)
        if ball is None:
            if value is not None:raise AssertionError('Missing requested test jet '+scope+'/'+name)
        elif value is not None and not ball.contains(mp_point(value)):
            raise AssertionError('Independent point lies outside '+scope+'/'+name+
                                 ': '+str(ball)+' vs '+mp.nstr(value,30))


def run(args):
    started=time.monotonic();ctx.prec=args.precision;mp.mp.dps=125
    stem=args.out_prefix
    paths={name:stem.with_name(stem.name+suffix) for name,suffix in
           (('report','-report.json'),('definition','-definition.json'),('primitive','-primitive.json'))}
    if any(p.exists() for p in paths.values()):
        raise FileExistsError('Closed output names must not be overwritten')
    stem.parent.mkdir(parents=True,exist_ok=True)
    report=dict(schema='fd2d-current-native-interval-small-check-v1',source=identity(__file__),
        input_definition=identity(args.definition),precision_bits=args.precision,
        scope='one immutable saved field, sparse component boxes and exact algebra only',
        whole_F_J_BVP_body_evaluated=False,continuous_global_certificate=False,passed=False)
    try:
        pieces=CurrentNativeIntervalPieces(args.definition)
        report['actual_arrays']=identity(pieces.reader.arrays_path)
        report['layout']=dict(nodes=len(pieces.mesh),modes=pieces.K,
            parameters=len(pieces.parameters),explicit_slices=pieces.layout)
        before={key:identity(path)['sha256'] for key,path in
                (('arrays',pieces.reader.arrays_path),('definition',args.definition))}
        definition=pieces.definition()
        definition['structural_partition']=pieces.structural_partition()
        paths['definition'].write_text(json.dumps(definition,indent=2,allow_nan=False)+'\n')
        rows=[];point_checks=0
        selected=[0,63,73,121]
        for cell in selected:
            left,right=pieces.mesh[cell:cell+2]
            lo=left+(right-left)/4;hi=left+3*(right-left)/4
            al,ah=F(13,100),F(13,100)+F(1,2048)
            packet=pieces.raw_box(cell,lo,hi,al,ah)
            for s in (lo,(lo+hi)/2,hi):
                for a in (al,(al+ah)/2,ah):
                    values=raw_oracle(pieces,cell,s,mp.pi*mq(a))
                    for component,oracle in zip(packet['fields'],values):
                        assert_jet_contains(component,oracle,'actual_raw_cell_'+str(cell))
                        point_checks+=1
            rows.append(dict(cell=cell,radial_exact=[rational_pair(lo),rational_pair(hi)],
                angular_pi_exact=[rational_pair(al),rational_pair(ah)],
                fields=[q.record() for q in packet['fields']]))
        report['actual_raw_P1_boxes']=rows
        report['independent_raw_vector_jet_point_checks']=point_checks
        # Compare exact rational bump polynomials, not a sampled derivative.
        bump_checks=0
        for s in (F(1,5),F(3,5),F(4,5),F(7,5)):
            packet=pieces.bump_increments(s,s,3)
            exact=[F(0) for unused in range(4)]
            from math import comb,factorial
            for delta,(left,right) in zip(pieces.parameters[pieces.reader.profile_parameter_slice],pieces.profile_supports):
                if not left<s<right:continue
                t=(s-left)/(right-left)
                for d in range(4):
                    exact_sum=F(0)
                    for k in range(d+1):
                        factor=comb(d,k)*factorial(5)//factorial(5-k)
                        factor*=((-1)**(d-k))*factorial(5)//factorial(5-(d-k))
                        exact_sum+=factor*t**(5-k)*(1-t)**(5-(d-k))
                    exact[d]+=1024*delta*exact_sum/(right-left)**d
            for ball,q in zip(packet['increments'],exact):
                if not ball.overlaps(aq(q)):raise AssertionError('Exact physical bump rational value not enclosed')
                bump_checks+=1
        report['exact_bump_derivative_checks']=bump_checks
        weights=pieces.scalar_weights(pieces.entry+pieces.rim,pieces.exit-pieces.rim)
        if not weights['coast'].value.is_exact() or weights['coast'].value!=1 or not weights['coast'].s.is_zero():
            raise AssertionError('Actual exact coast plateau weight is not exactly one')
        report['exact_coast_plateau']=dict(value=bound_record(weights['coast'].value),
                                        derivative=bound_record(weights['coast'].s))
        cutrows=[]
        for lo,hi in ((F(-1,100),F(1,100)),(F(1,5),F(1,5)+F(1,4096)),
                      (F(49,100),F(1,2)),(F(-1,2),F(-49,100))):
            packet=pieces.exact_cut_angular_box(lo,hi)
            for q in packet['fields']:
                if q.s is not None or q.sxi is not None:raise AssertionError('Cut radial derivative was invented')
            for ratio in (lo,(lo+hi)/2,hi):
                u=mp.pi*mq(ratio)
                for j,jet in enumerate(packet['fields']):
                    f=lambda v:tail_oracle(pieces,v)[j]
                    assert_jet_contains(jet,(f(u),None,mp.diff(f,u),mp.diff(f,u,2),None),'actual_cut')
            cutrows.append(dict(angular_pi_exact=[rational_pair(lo),rational_pair(hi)],
                                fields=[q.record() for q in packet['fields']]))
        report['actual_cut_angular_boxes']=cutrows
        report['cut_radial_II_derivative_claimed']=False
        # Independent derivatives of two elementary local formulas exercise
        # the interval chain rules, including actual K_s when requested.
        s0,x0=mp.mpf('0.37'),mp.mpf('0.61')
        s=Jet(interval(F(36,100),F(38,100)),arb(1),arb(0),arb(0),arb(0))
        x=Jet(interval(F(60,100),F(62,100)),arb(0),arb(1),arb(0),arb(0))
        n=2+s/10+x.sin()/5;m=x.cos()/10+s/100;l=F(3,10)+(2*x).sin()/50+3*s/100
        K=F(1,5)+s/100
        def base(ss,xx):return 2+ss/10+mp.sin(xx)/5,mp.cos(xx)/10+ss/100,mp.mpf(3)/10+mp.sin(2*xx)/50+3*ss/100
        algebra=[]
        for kind,w,fn in (
            ('R153',F(3,10)+s/100,compose_R153),('R155',F(1,5)+s/50,compose_R155)):
            fields=fn((n,m,l),w,K)
            def oracle(ss,xx):
                nn,mm,ll=base(ss,xx);kk=mp.mpf(1)/5+ss/100
                if kind=='R153':
                    ww=mp.mpf(3)/10+ss/100;return nn,mm,(1-ww)*ll+ww*(kk+mm*mm)/nn
                ww=mp.mpf(1)/5+ss/50;ee=ww*(mp.sqrt((nn-ll)**2+4*mm*mm+4*kk)-nn-ll)/2
                return nn+ee,mm,ll+ee
            for j,jet in enumerate(fields):
                f=lambda ss,xx:oracle(ss,xx)[j]
                exact=(f(s0,x0),mp.diff(lambda ss:f(ss,x0),s0),mp.diff(lambda xx:f(s0,xx),x0),
                       mp.diff(lambda xx:f(s0,xx),x0,2),
                       mp.diff(lambda ss:mp.diff(lambda xx:f(ss,xx),x0),s0))
                assert_jet_contains(jet,exact,'synthetic_'+kind)
            algebra.append(dict(kind=kind,synthetic_only=True,all_five_jet_components_checked=True))
        report['conditional_jet_algebra_checks']=algebra
        # The source's actual dyadics supply a nontrivial rational test
        # polynomial. It is NOT asserted to approximate the actual forcing.
        c=[[[F(0) for unused in range(3)] for unused in range(3)] for unused in range(3)]
        b=[[[F(0) for unused in range(3)] for unused in range(3)] for unused in range(3)]
        for degree in range(3):
            for mode in range(3):
                c[0][degree][mode]=rational(pieces.coefficients[63+degree,mode])
                c[2][degree][mode]=rational(pieces.coefficients[63+degree,pieces.d+mode])
                if mode:b[1][degree][mode]=rational(pieces.coefficients[63+degree,pieces.e+mode-1])
        left,right=pieces.mesh[63:65]
        primitive=ExactZeroEndPrimitive(left,right,c,b,field_binding_sha256=pieces.binding_sha256,
            provenance=dict(actual_coefficient_source_sha256=report['actual_arrays']['sha256'],
                role='nontrivial exact primitive implementation fixture only; no actual H approximation claim'))
        for endpoint in (left,right):
            p=primitive.polynomial_boxes(endpoint,endpoint,0,1)
            if not all(q.is_zero() for q in p['q']+p['q_xi']):raise AssertionError('Exact primitive endpoint was not zero')
        profile=ProfileBox(aq(1),aq(F(1,10)),aq(-F(1,5)),aq(0))
        chart=ChartBox(aq(F(6,5)),aq(F(1,3)),aq(F(1,50)),aq(F(1,70)))
        connection=connection_box((n,m,l),profile,chart)
        packet=primitive.conditional_box(connection,chart,left,right,F(1,8),F(1,7),
                                         field_binding_sha256=pieces.binding_sha256)
        if not all(v.is_finite() for v in packet['E']):raise AssertionError('Finite conditional primitive algebra failed')
        report['exact_primitive']=dict(identities=primitive.exact_identities,
            field_binding_sha256=primitive.field_binding_sha256,packet_sha256=primitive.packet_sha256,
            actual_H_remainder_paid=False,conditional_synthetic_forcing_only=True,
            complete_three_component_forcing=True,physical_Us_term_included=packet['physical_Us_term_included'],
            E_norm_upper=bound_record(packet['E_norm_upper']),Q_e1_norm_upper=bound_record(packet['Q_e1_norm_upper']))
        paths['primitive'].write_text(json.dumps(primitive.definition(),indent=2,allow_nan=False)+'\n')
        missing_s_K=Jet(aq(F(1,5)),None,arb(0),arb(0),None)
        no_s=compose_R155((n,m,l),Jet.constant(1),missing_s_K)
        if no_s[0].s is not None:raise AssertionError('Missing actual K_s silently became zero')
        rejected=False
        try:connection_box(no_s,profile,chart)
        except UnresolvedInterval:rejected=True
        if not rejected:raise AssertionError('A missing physical radial jet was silently accepted')
        report['missing_radial_jet_is_explicitly_unresolved']=True
        budget=propagate_piece_budget(F(1,50),aq(F(1,10)),aq(F(1,100)),aq(F(1,2)),aq(F(1,5)),aq(1))
        expected_d=F(11,100);expected_k=F(161,10000)
        if budget['d_right']<aq(expected_d).lower() or budget['k_right']<aq(expected_k).lower():
            raise AssertionError('Outward recurrence failed the exact rational fixture')
        report['conditional_budget_fixture']={key:bound_record(budget[key]) for key in ('d_right','k_right','relative_metric_upper')}
        after={key:identity(path)['sha256'] for key,path in
               (('arrays',pieces.reader.arrays_path),('definition',args.definition))}
        if before!=after:raise AssertionError('A defining input changed')
        report['actual_inputs_unchanged']=True
        report['unpaid_parts']=definition['unpaid_interval_parts']
        report['output_definition']=identity(paths['definition'])
        report['output_primitive']=identity(paths['primitive'])
        report['modules']=[identity(Path(__file__).parent/name) for name in
                          ('fd2d_gc_current_native_interval.py','fd2d_gc_current_primitive_interval.py')]
        report['passed']=True
    except Exception as exc:
        report['error']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
        raise
    finally:
        report['seconds']=time.monotonic()-started
        report['peak_rss_kib']=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        paths['report'].write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
        print(json.dumps(dict(passed=report['passed'],report=str(paths['report']),seconds=report['seconds'],
                              peak_rss_kib=report['peak_rss_kib'],continuous_global_certificate=False),allow_nan=False))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--definition',type=Path,required=True)
    parser.add_argument('--out-prefix',type=Path,required=True)
    parser.add_argument('--precision',type=int,default=256)
    run(parser.parse_args())
