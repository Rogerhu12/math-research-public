#!/usr/bin/env python3
"""Locate sampled Frenet square-root margins of an actual saved neck map.

The reported margin is 1-(a'/(a*kappa_latitude))^2, computed from the
actual first and second angular derivatives. It is not an embedding or
reach certificate. Negative Newton trial margins do not prove nonexistence.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse,hashlib,importlib.util,json,time
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('alternative_domain_curvature',P/'alternative-neck-curvature-map.py')
mapper=importlib.util.module_from_spec(spec);spec.loader.exec_module(mapper)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--source-topic',type=Path,required=True)
    p.add_argument('--port',type=Path,required=True)
    p.add_argument('--angular',type=int,default=512)
    p.add_argument('--radial',type=int,default=801)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();start=time.time()
    saved,_=mapper.pb.load_saved(a.input,a.source_topic,a.port,a.angular)
    f=saved.flow;pre=f._alternative_neck
    ss=np.unique(np.r_[np.linspace(0,f.end,a.radial),saved.sol.x,f.breaks])
    rows={}
    for first in range(0,len(ss),24):
        s=ss[first:first+24];fr=f.frame(s,saved.q*saved.sol.sol(s))
        aa,v,acc=f.profile(s)
        for i,x in enumerate(s):
            j=int(np.argmin(fr['margin'][i]));value=float(fr['margin'][i,j])
            seg=next((z for z in pre.segments if z['s0']-1e-12<=x<=z['s1']+1e-12),None)
            label=mapper.label(seg,pre.loop_begin) if seg else 'terminal bridge'
            if label not in rows or value<rows[label]['margin']:
                rows[label]=dict(label=label,margin=value,s=float(x),
                    psi=float(2*np.pi*j/f.nt),a=float(aa[i]),ap=float(v[i]),
                    latitude_curve_curvature=float(fr['kap'][i,j]),
                    background_margin=float(1-v[i]**2))
    report=dict(scope=__doc__,input=str(a.input),
        input_sha256=hashlib.sha256(a.input.read_bytes()).hexdigest(),
        source_sha256={name:hashlib.sha256((P/name).read_bytes()).hexdigest()
            for name in ['alternative-neck-domain-map.py','alternative-neck-curvature-map.py','geometric-checkpoint-core-pullback.py','alternative-neck-provider.py']},
        frozen_profile=saved.rec['frozen_profile'],gauge_amplitude=saved.q,
        meridian_length=f.end,angular=f.nt,radial_samples=len(ss),
        rows=sorted(rows.values(),key=lambda row:row['margin']),
        seconds=time.time()-start)
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(seconds=report['seconds'],minimum=report['rows'][0])))

if __name__=='__main__':main()
