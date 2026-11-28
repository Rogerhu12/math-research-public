"""Construct the full physical Cartesian two-jet input at the large-radius port."""
import argparse
import importlib.util
import json
from pathlib import Path
import numpy as np


def load_certificate():
    name=Path(__file__).with_name('2ecf-prufer-macro-harmonic-certificate.py')
    spec=importlib.util.spec_from_file_location('packet_certificate',name)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def physical_port(data,coeff,scale,axis_height):
    cert=load_certificate().bound(data,coeff,1.35)
    meta=json.loads(Path(data).read_text());row=meta['rows'][-1];m=meta.get('fundamental',2)
    z=np.load(coeff)
    # Add all nonlinear radial Fourier PVA to the analytic mean and second mode.
    # The full corrected mean height at this mouth defines the vertical translation.
    jet=np.stack([z['delta'][-1],z['derivative'][-1],z['second'][-1]]).copy()
    jet[:,0,0]+=[row[3]+row[12],1+row[13],row[14]]
    jet[0,2,0]=axis_height/scale
    jet[1:,2,0]+=[row[4]+row[15],row[5]+row[16]]
    jet[:,0,1]+=[row[9],row[10],row[11]]
    jet[:,1,1]-=np.array([row[9],row[10],row[11]])/m
    jet[:,2,1]+=[row[6],row[7],row[8]]
    for d in range(3):
        jet[d]*=scale**(1-d)
    return dict(fundamental=m,normalizedOuterRadius=row[3],physicalRadius=scale*row[3],physicalScale=scale,
                correctedAxisHeight=axis_height,cylindricalRadialPVA=jet.tolist(),certificate=cert,
                physicalTarget=[1+row[4]**2,(scale*row[3])**2],physicalSlope=row[4])


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('data');ap.add_argument('coeff');ap.add_argument('out')
    ap.add_argument('--scale',type=float,default=.5);ap.add_argument('--height',type=float,default=.85)
    a=ap.parse_args();d=physical_port(a.data,a.coeff,a.scale,a.height)
    Path(a.out).write_text(json.dumps(d,separators=(',',':'))+'\n')
    print(json.dumps({k:v for k,v in d.items() if k!='cylindricalRadialPVA'},indent=2))
