#!/usr/bin/env python3
"""Small semantic check of the new true-bridge adapter; no BVP field is used."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import types
import numpy as np
import mpmath as mp


def mod(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    result=importlib.util.module_from_spec(spec);sys.modules[name]=result
    spec.loader.exec_module(result);return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--driver',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    driver=mod('_true_bridge_adapter_check',args.driver)
    scripts,helper=driver.setup(args.repo)
    b,v=helper.jets,helper.prefix_mean
    I=b.I
    primitive=mod('_synthetic_bridge_primitive',scripts/'resume_20261126/seam_bridge_endpoint_primitive.py')
    base=helper.MeanMap.__new__(helper.MeanMap)
    base.M,base.n,base.N=2,7,1168
    base.entry=Q(0)
    base.peak,base.eps=Q(3,2),Q(1,50)
    base.L1,base.L2,base.L3=Q(9,16),Q(1,10),Q(1,50)
    base.end=base.L1+base.L2+base.L3
    base.cutoff=3*base.end/4
    base.xx=base.spx=[Q(0),base.end]
    base.pc={0:[I(np.zeros(base.n)) for _ in range(6)]}
    base.ec={(0,late):([I(0)]*6,[I(0)]*5) for late in (False,True)}
    base.q=I(.06)
    base.f=types.SimpleNamespace(even=np.array([3,6]))
    base.first=primitive.sin_polynomial([Q(0),Q(0),3*base.peak,-2*base.peak],40)
    base.last=primitive.sin_polynomial([base.peak,Q(0),-base.eps],40)
    base.first_integral=[I(0)]+[I.rational(x/(j+1)) for j,x in enumerate(base.first)]
    base.last_integral=[I(0)]+[I.rational(x/(j+1)) for j,x in enumerate(base.last)]
    base.drop1=I.rational(base.L1)*helper.ipoly(base.first_integral,I(1))
    base.plateau=I.rational(primitive.sin_polynomial([base.peak],40)[0])
    base.bridge_remainder=base.peak**41/math.factorial(41)
    base.grid=sorted(set([Q(0),base.L1,base.L1+base.L2,base.end,base.cutoff]))
    psi=2*np.pi*np.arange(1168)/1168
    table=v.AngleTable(psi,psi,base.f.even)
    base.co,base.sn,base.co3,base.sn3=table.co,table.sn,table.co3,table.sn3
    obj=driver.TrueBridgeJets(base,helper)
    gram=b.GramVerifier(obj,12)
    mp.mp.dps=90
    def real(q):
        return mp.mpf(q.numerator)/q.denominator
    def contained(interval,truth):
        return mp.mpf(float(interval.x[0]))<=truth<=mp.mpf(float(interval.x[1]))
    def phase(s):
        if s<=base.L1:
            u=s/base.L1
            return base.peak*(3*u*u-2*u*u*u),6*base.peak*u*(1-u)/base.L1,6*base.peak*(1-2*u)/base.L1**2
        if s<=base.L1+base.L2:
            return base.peak,Q(0),Q(0)
        u=(s-base.L1-base.L2)/base.L3
        return base.peak-base.eps*u*u,-2*base.eps*u/base.L3,-2*base.eps/base.L3**2
    def integral(s):
        first=lambda x: mp.sin(real(base.peak)*(3*x*x-2*x*x*x))
        last=lambda x: mp.sin(real(base.peak)-real(base.eps)*x*x)
        value=real(base.L1)*mp.quad(first,[0,min(real(s/base.L1),mp.mpf(1))])
        if s>base.L1:
            value+=real(min(s-base.L1,base.L2))*mp.sin(real(base.peak))
        if s>base.L1+base.L2:
            value+=real(base.L3)*mp.quad(last,[0,real((s-base.L1-base.L2)/base.L3)])
        return 1-value
    angle_table=driver.angular_boxes(v,base.f.even,256)
    geometric_model=v.PrefixMetric(driver.BridgePieces(obj),None,None,angle_table,0.)
    point_height=types.SimpleNamespace(enclose=lambda left,right,interval: interval.rational(Q(2,5)))
    rows=[]
    for s in (base.L1/5,base.L1*4/5,base.L1+base.L2/2,
              base.L1+base.L2+base.L3/3,base.end):
        a,ap,co=obj.profile(I.rational(s),s,s)
        ph,dph,ddph=map(real,phase(s))
        truth_a=[integral(s),-mp.sin(ph),-mp.cos(ph)*dph]
        truth_ap=[truth_a[1],truth_a[2],mp.sin(ph)*dph*dph-mp.cos(ph)*ddph]
        truth_mean=[mp.cos(ph),-mp.sin(ph)*dph,-mp.cos(ph)*dph*dph-mp.sin(ph)*ddph]
        diff,mean,root=obj.evaluate(s,s)
        for name,actual,truth in (('a',a,truth_a),('ap',ap,truth_ap),('mean',mean,truth_mean)):
            for index,component in enumerate(('v','d','d2')):
                if not contained(getattr(actual,component),truth[index]):
                    raise AssertionError((str(s),name,component,'independent high-precision value not enclosed'))
        bound,meta,_=gram.enclose(s,s)
        if not 0<=bound<1e-8:
            raise AssertionError(('rotation has unresolved isometric Gram bound',bound))
        geometric=driver.geometry(v,geometric_model,angle_table,obj,point_height,s,s,bound)
        actual_curvature=max(abs(dph),mp.cos(ph)/truth_a[0])
        actual_radius=mp.sqrt(truth_a[0]**2+mp.mpf(4)/25)
        actual_support=truth_a[0]*mp.cos(ph)+mp.mpf(2)/5*mp.sin(ph)
        if (mp.mpf(geometric['curvature_upper'])<actual_curvature or
                mp.mpf(geometric['radius_upper'])<actual_radius or
                mp.mpf(geometric['support_lower'])>actual_support):
            raise AssertionError('The complete-angle geometry misses the exact rotational value')
        rows.append(dict(s_exact=str(s),point_metric_bound=bound,root_lower=meta['root_min'],
            geometry=geometric,
            mean_width=max(float(mean.v.x[1]-mean.v.x[0]),float(mean.d.x[1]-mean.d.x[0]),
                           float(mean.d2.x[1]-mean.d2.x[0]))))
    # A negative lower mean and positive upper mean require the full product
    # enclosure, not an assumed monotone mean-height primitive.
    height=driver.HeightPrimitive.__new__(driver.HeightPrimitive)
    height.starts=[Q(0)]
    height.rows=[(Q(0),Q(2),Q(-1,4),Q(3,4),Q(2,5),Q(1,2))]
    enclosure=height.enclose(Q(1,2),Q(3,2),I)
    if not (contained(enclosure,real(Q(1,40))) and contained(enclosure,real(Q(13,8)))):
        raise AssertionError('Signed Darboux primitive product is not enclosed')
    args.out.parent.mkdir(parents=True,exist_ok=True)
    report=dict(status='synthetic_true_bridge_adapter_check_passed',
        actual_BVP_field=False,complete_actual_bridge_certificate=False,
        literal_mean_nodes=1168,modes=2,radial_points=len(rows),
        independently_checked_derivatives=['a through order 2','a_s through order 2','M through order 2'],
        rotation_metric_max=max(row['point_metric_bound'] for row in rows),
        signed_height_product_checked=True,all_angle_rotation_geometry_checked=True,
        geometry_angular_boxes=256,rows=rows,
        driver_sha256=driver.sha(args.driver),checker_sha256=driver.sha(__file__),
        reviewed_sources={key:driver.sha(scripts/key) for key in driver.REVIEWED})
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(report,allow_nan=False))
    return 0


if __name__=='__main__':
    raise SystemExit(main())

