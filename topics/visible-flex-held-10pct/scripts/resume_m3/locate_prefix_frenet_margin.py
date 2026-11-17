#!/usr/bin/env python3
"""Locate the complete finite prefix's sampled Frenet margin bottleneck.

This reuses the accepted actual source field and physical profile.  It does
not solve a BVP or infer a continuous lower bound from the sampled minimum.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import numpy as np
from scipy.interpolate import PPoly
from couple_m3_smallcut_secant import accepted_anchor


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic','short-bridge','prefix','port','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--angular',type=int,default=2048)
    p.add_argument('--radial',type=int,default=401)
    a=p.parse_args();r=json.load(gzip.open(a.prefix,'rt'));accepted_anchor(r,a.prefix)
    if r['config']['base_mode']!=3:raise ValueError('Expected m3 actual state')
    if r.get('core_round_settings'):raise ValueError('Integral-core states need their separately recorded loader')
    ad=module('m3_margin_original_adaptive',a.source_topic/'scripts/950f-prefix-adaptive-chart-bvp-v2.py')
    module('m3_margin_original_flat',a.source_topic/'scripts/db6f-prefix-flat-profile.py').install(ad)
    ad.old.install_source(a.source_topic/'repro/source-root')
    module('m3_margin_original_short',a.short_bridge).install()
    from curve_stable_prefix_bvp import load_checkpoint
    r=load_checkpoint(a.prefix)
    port=json.loads(a.port.read_text());port['cut']['_prefix_bridge']=r['frozen_profile']['prefix_bridge']
    if port['parameters']!=r['physical_tail_parameters'] or port['cut']!=r['physical_tail_cut']:
        raise ValueError('Physical port differs')
    _,BVP=ad.build_classes(r['chart'])
    obj=BVP(r['frozen_profile'],port,r['gauge_amplitude'],r['config']['modes'],a.angular,True,r['warp_reference_q'])
    obj.pscale=np.asarray(r['central_correction_scales'])
    par=np.asarray(r['parameters']);par[0]=math.log(r['actual_primary_amplitude']/obj.q)
    obj.initial(par);flow=obj.flow(par[0]);mesh=np.asarray(r['mesh'])
    pp=PPoly.construct_fast(np.asarray(r['pp_coefficients']),mesh,extrapolate=False,axis=1)
    ss=np.unique(np.r_[mesh,(mesh[:-1]+mesh[1:])/2,np.linspace(0,flow.end,a.radial)])
    _,B1,B2=flow.basis(a.angular);rows=[]
    for first in range(0,len(ss),32):
        s=ss[first:first+32];fr=flow.frame(s,obj.q*pp(s),B1,B2)
        for j,physical in enumerate(s):
            k=int(np.argmin(fr['margin'][j]));g=fr['geo']
            rows.append(dict(s=float(physical),normalized_s=float(physical/flow.end),
                psi=float(2*np.pi*k/a.angular),material_theta=float(g['theta'][j,k]),
                margin=float(fr['margin'][j,k]),a=float(fr['a'][j]),ap=float(fr['ap'][j]),
                curvature=float(fr['kap'][j,k]),alpha=float(fr['alpha'][j,k]),
                chart_rho=float(g['rho'][j,k])))
    rows.sort(key=lambda x:x['margin'])
    fields=['end','prefix_end','Tu','Td','ramp','flat','q','warp_e']
    result=dict(scope=__doc__,command=sys.argv,
        input=str(a.prefix.resolve()),input_sha256=hashlib.sha256(a.prefix.read_bytes()).hexdigest(),
        source_sha256={str(f.resolve()):hashlib.sha256(f.read_bytes()).hexdigest() for f in
          [Path(__file__),a.short_bridge,a.source_topic/'scripts/950f-prefix-adaptive-chart-bvp-v2.py',
           a.source_topic/'scripts/db6f-prefix-flat-profile.py']},
        modes=obj.M,angular=a.angular,radial_points=len(ss),actual_primary_amplitude=r['actual_primary_amplitude'],
        frozen_profile=r['frozen_profile'],flow_scales={k:float(getattr(flow,k)) for k in fields
            if isinstance(getattr(flow,k,None),(int,float,np.number))},lowest_radial_rows=rows[:16])
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(points=len(ss),minimum=rows[0],flow_scales=result['flow_scales'])))


if __name__=='__main__':main()
