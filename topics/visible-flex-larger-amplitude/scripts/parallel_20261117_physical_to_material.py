#!/usr/bin/env python3
"""Project one actual finite physical-angle trace with its full rho density."""
import argparse,hashlib,json
from pathlib import Path
import numpy as np


def project(data,modes,angles):
    phi=np.arange(angles)*2*np.pi/angles
    f=2*np.arange(1,len(data['rho_cos_coefficients'])+1)
    co=np.cos(phi[:,None]*f);si=np.sin(phi[:,None]*f)
    rho=1+co@np.array(data['rho_cos_coefficients'])
    theta=phi+si@(np.array(data['rho_cos_coefficients'])/f)
    pt=si@np.array(data['Ptilde_sin_coefficients'])
    kk=data['K_mean']+co@np.array(data['K_cos_coefficients'])
    hh=data['height_mean']+co@np.array(data['height_cos_coefficients'])
    fm=2*np.arange(1,modes+1);cm=np.cos(theta[:,None]*fm);sm=np.sin(theta[:,None]*fm)
    pc=2*np.mean(pt[:,None]*sm,axis=0)
    kc=2*np.mean((rho*kk)[:,None]*cm,axis=0)
    hc=2*np.mean((rho*hh)[:,None]*cm,axis=0)
    return dict(r=data['r'],w=data['w'],w_r=data['w_r'],
                height_mean=float(np.mean(rho*hh)),K_mean=float(np.mean(rho*kk)),
                P_sin_coefficients=pc.tolist(),K_cos_coefficients=kc.tolist(),height_cos_coefficients=hc.tolist(),
                sampled_material_projection_height_identity_max=float(np.max(abs(pc+fm*hc/(data['r']*data['w'])))),
                minimum_rho=float(np.min(rho)),angles=angles)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--trace',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--modes',type=int,default=16);p.add_argument('--angles',type=int,default=8192)
    a=p.parse_args();raw=a.trace.read_bytes();data=json.loads(raw)
    first=project(data,a.modes,a.angles);last=project(data,a.modes,2*a.angles)
    last.update(scope='Explicit material Fourier projection of the actual physical-angle trace; no new prefix BVP.',
                physical_trace_sha256=hashlib.sha256(raw).hexdigest(),parent_input_sha256=data.get('parent_input_sha256'),
                projection_refinement_difference=max(float(np.max(abs(np.array(first[k])-np.array(last[k]))))
                    for k in ['P_sin_coefficients','K_cos_coefficients','height_cos_coefficients']))
    output=(json.dumps(last)+'\n').encode();a.out.write_bytes(output)
    print(json.dumps(dict(output_sha256=hashlib.sha256(output).hexdigest(),height_mean=last['height_mean'],
                         refinement_difference=last['projection_refinement_difference'],
                         source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())))
