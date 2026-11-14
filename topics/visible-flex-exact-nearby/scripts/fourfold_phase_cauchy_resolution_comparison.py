#!/usr/bin/env python3
"""Finite floating endpoint comparison of the two-jet Cauchy diagnostics."""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_waist_cauchy_evolution_probe import acceleration
from fourfold_phase_local_correction_probe import sha,scalar_target

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--coarse',type=Path,required=True);p.add_argument('--fine',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    a,b=[np.load(p,allow_pickle=False) for p in (args.coarse,args.fine)]
    if float(a['r'])!=float(b['r']):raise ValueError('different endpoint radii')
    for data in (a,b):
        meta=json.loads(str(data['metadata']))
        if meta['object_sha256']!=sha(args.object):raise ValueError('different initial objects')
    r=float(a['r']);g,_=load_exact_object(args.object,512);t=scalar_target(g,r)
    Ac,Tc,Mc,Qc=acceleration(a['F'],a['F_r'],t);Af,Tf,Mf,Qf=acceleration(b['F'],b['F_r'],t)
    rows={}
    for key,x,y in zip(['F','F_r','F_theta','F_rr','F_rtheta','F_thetatheta'],
                      [a['F'],a['F_r'],Tc,Ac,Mc,Qc],[b['F'],b['F_r'],Tf,Af,Mf,Qf]):
        freq=np.fft.fftfreq(len(x),1/len(x)).astype(int);pad=np.zeros_like(y,dtype=complex)
        pad[freq%len(y)]=np.fft.fft(x,axis=0)/len(x)
        xi=(len(y)*np.fft.ifft(pad,axis=0)).real
        rows[key]=float(np.max(np.linalg.norm(xi-y,axis=-1)))
    out=dict(kind='floating_endpoint_resolution_comparison',certified=False,r=r,
        coarse_angles=len(a['F']),fine_angles=len(b['F']),source_sha256=sha(__file__),
        input_sha256={str(p):sha(p) for p in (args.coarse,args.fine)},
        object_sha256=sha(args.object),maximum_sampled_two_jet_differences=rows,
        comparison='coarse rotating Fourier endpoint and its nonlinear acceleration upsampled onto the fine grid',
        limitations=['This is a finite sampled convergence diagnostic, not an infinite-tail or rounding certificate.'])
    args.out.write_text(json.dumps(out,indent=2)+'\n');print(rows,flush=True)

if __name__=='__main__':main()
