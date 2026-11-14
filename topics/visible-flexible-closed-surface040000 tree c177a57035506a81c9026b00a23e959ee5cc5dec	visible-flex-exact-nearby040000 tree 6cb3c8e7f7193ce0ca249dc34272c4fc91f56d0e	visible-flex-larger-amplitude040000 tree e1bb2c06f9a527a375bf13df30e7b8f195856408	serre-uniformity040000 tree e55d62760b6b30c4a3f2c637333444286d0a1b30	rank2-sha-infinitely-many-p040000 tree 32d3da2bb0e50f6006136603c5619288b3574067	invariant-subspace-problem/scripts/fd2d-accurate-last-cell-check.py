#!/usr/bin/env python3
"""One bounded current-input check of the R172 exact endpoint completion."""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import resource
import time

import mpmath as mp
from flint import arb

from fd2d_gc_accurate_last_cell import AccurateLastCell
from fd2d_gc_current_native_interval import bound_record, aq, rational
from fd2d_gc_r136_arb_profile import ends
from fd2d_gc_archive_arrays import identity


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--field',type=Path,required=True)
    ap.add_argument('--profile',type=Path,required=True)
    ap.add_argument('--profile-sha256',required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    a=ap.parse_args();start=time.monotonic();mp.mp.dps=80
    z=AccurateLastCell(a.field,a.profile,profile_sha256=a.profile_sha256)
    frac=lambda x:mp.mpf(x.numerator)/x.denominator
    mid=lambda x:frac(sum(ends(x),F(0))/2)
    S=mid(z.S);b=frac(z.b);E=frac(z.E);L=mid(z.profile.pieces[-1]['L'])
    p=z.profile.pieces[-1];p0=mid(p['p0']);p1=-mp.pi/2
    q0=L*mid(p['ps0']);q1=L*mid(p['ps1'])
    c2=3*(p1-p0)-2*q0-q1;c3=-2*(p1-p0)+q0+q1
    phase=lambda v:p0+q0*v+c2*v*v+c3*v*v*v
    last_start=S-L
    def field(s,u,cut=False):
        t=(s-b)/(S-b);sigma=b+(E-b)*t
        v=(s-last_start)/L
        radius=(mp.mpf(4)/5 if cut else mp.mpf(4)/5-L*mp.quad(lambda x:mp.sin(phase(x)),[v,1]))
        ps=(q0+2*c2*v+3*c3*v*v)/L
        K=mp.mpf(0) if cut else -mp.cos(phase(v))*ps/radius
        sn,cs=mp.sin(u),mp.cos(u);y=radius*sn
        q=(abs(y)-mp.mpf(17)/50)/(mp.mpf(23)/50)
        k=mp.mpf(0)
        if 0<q<1:
            poly=sum(frac(c)*mp.binomial(15,j)*q**j*(1-q)**(15-j) for j,c in enumerate(z.tail))
            k=630*q**4*(1-q)**4*poly/(mp.mpf(23)/50)
        tail=(k*cs*cs,-k*sn*cs,k*sn*sn)
        if cut:return tail
        eta_x=(sigma-frac(z.weight_start))/frac(z.weight_length)
        eta=eta_x**3*(10-15*eta_x+6*eta_x**2)
        raw=(sum(frac(z.c0[j])*mp.cos(2*j*u) for j in range(z.e)),
             sum(frac(z.c0[z.e+j])*mp.sin(2*(j+1)*u) for j in range(z.K)),
             sum(frac(z.c0[z.d+j])*mp.cos(2*j*u) for j in range(z.e)))
        n,m,l=tuple((1-t)*r+eta*f for r,f in zip(raw,tail))
        d=n-l;h=mp.sqrt(d*d+4*m*m+4*K)
        return ((h+d)/2,m,(h-d)/2)
    comparisons=[]
    for t,angle in [(F(0),F(0)),(F(1,3),F(1,9)),(F(2,3),F(1,4)),(F(3,4),F(1,2))]:
        s=b+(S-b)*frac(t);u=mp.pi*frac(angle)
        box=z.box(t,t,angle,angle)
        for component,jet in enumerate(box['fields']):
            f=lambda x,y:field(x,y)[component]
            exact=[f(s,u),mp.diff(lambda x:f(x,u),s),mp.diff(lambda y:f(s,y),u),
                   mp.diff(lambda y:f(s,y),u,2),
                   mp.diff(lambda x:mp.diff(lambda y:f(x,y),u),s)]
            for key,value in zip(('value','s','xi','xixi','sxi'),exact):
                enclosure=getattr(jet,key)
                low,high=ends(enclosure);vv=mp.re(value)
                # The independent 80-digit scalar quadrature is a finite
                # check, not the proof of the Arb interval enclosure.
                included=frac(low)<=vv<=frac(high)
                if not included:raise AssertionError((str(t),str(angle),component,key,str(vv),str(enclosure)))
                comparisons.append(dict(t=str(t),u_over_pi=str(angle),component=component,jet=key,
                                        independent_scalar_in_interval=True))
    for angle in (F(0),F(1,9),F(1,4),F(1,2)):
        box=z.box(1,1,angle,angle)
        assert all(q.s is None and q.sxi is None for q in box['fields'])
        for component,jet in enumerate(box['fields']):
            u=mp.pi*frac(angle)
            f=lambda y:field(S,y,True)[component]
            for key,order in (('value',0),('xi',1),('xixi',2)):
                value=f(u) if order==0 else mp.diff(f,u,order)
                low,high=ends(getattr(jet,key))
                if not frac(low)<=mp.re(value)<=frac(high):raise AssertionError(('cut',angle,component,key))
                comparisons.append(dict(t='cut',u_over_pi=str(angle),component=component,jet=key,
                                        independent_scalar_in_interval=True))
    raw_cut=z.raw_box(1,1,0,1)
    assert all(q.value.is_zero() and q.xi.is_zero() and q.xixi.is_zero() for q in raw_cut)
    assert z.weight_box(1,1).value == 1
    bounds=z.raw_coordinate_change_bounds()
    encoded={key:([ [bound_record(v) for v in row] for row in value]
                   if key=='value_u_uu_by_n_m_l' else bound_record(value) if isinstance(value,arb) else value)
             for key,value in bounds.items()}
    definition=z.definition();out=a.out_prefix
    paths={'definition':Path(str(out)+'-definition.json'),'report':Path(str(out)+'-report.json')}
    for path in paths.values():
        if path.exists():raise FileExistsError(path)
    paths['definition'].write_text(json.dumps(definition,ensure_ascii=False,indent=2)+'\n')
    report=dict(schema='fd2d-R172-actual-last-cell-check-v1',source=identity(__file__),
        definition=identity(paths['definition']),input=identity(a.field),passed=True,
        actual_scalar_checks=comparisons,check_count=len(comparisons),
        exact_endpoint_identities=['raw=0','eta=1','a=4/5','K=0','no radial II assigned'],
        uniform_change_bounds=encoded,seconds=time.monotonic()-start,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        whole_F_J_BVP_or_body_run=False,whole_surface_certificate=False)
    paths['report'].write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(passed=True,checks=len(comparisons),seconds=report['seconds'],
        peak_rss_kib=report['peak_rss_kib'],definition=identity(paths['definition']),
        report=identity(paths['report']),complete_II_value_bound=encoded['complete_positive_trace_II_value_frobenius_bound'])))


if __name__=='__main__':main()
