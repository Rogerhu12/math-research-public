#!/usr/bin/env python3
"""Finite actual-control m3 endpoint spectra in the unchanged inlet chart.

Every lambda-one row is a new unsolved design. All physical controls come
from a completed actual coupled checkpoint; no zero-control substitution,
infinite Fourier-tail bound, full metric test or new BVP is performed.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time
import numpy as np
from diagnose_primary_flatten_width import Core, LIB

M3 = Path(__file__).resolve().parent.parent/'resume_m3'
sys.path.insert(0, str(M3))
from couple_m3_smallcut_secant import accepted_anchor


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--checkpoint',type=Path,required=True)
    p.add_argument('--widths',type=float,nargs='+',default=[.08,.16,.24,.32])
    p.add_argument('--control-transition',type=float,default=.4)
    p.add_argument('--samples',type=int,default=12288)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();start=time.monotonic()
    r=json.load(gzip.open(a.checkpoint,'rt'));accepted_anchor(r,a.checkpoint)
    assert r['config']['base_mode']==3 and r['core_control_path']=='raw-mean-primary-compact-v1'
    settings=r['core_round_settings']
    assert settings['bimodal_eta']==0 and settings['lock_fundamental']
    q=r['actual_primary_amplitude']; c=np.asarray(r['parameters'][1:])*np.asarray(r['central_correction_scales'])
    M=r['config']['modes']; assert len(c)==M-1
    # This is the existing m3 inlet chart, frozen by warp_reference_q rather
    # than rescaled to the slightly different solved primary amplitude.
    e=8*r['warp_reference_q'];assert 0<=e<1
    N=a.samples;assert N>=4096 and N%3==0
    psi=2*np.pi*np.arange(N)/N;freq=abs(np.rint(np.fft.fftfreq(N)*N).astype(int))
    u=psi-e*np.sin(3*psi)/3;du=1-e*np.cos(3*psi);ddu=3*e*np.sin(3*psi)
    z=np.exp(1j*u)
    circle=[z,1j*du*z,(1j*ddu-du*du)*z]
    background=[np.stack((w.real,w.imag,np.zeros_like(w.real)),axis=-1)for w in circle]
    designs=[dict(label='accepted_core',settings=dict(settings))]
    for width in a.widths:
        designs.append(dict(label='new_lambda_one_design',settings=dict(settings,homotopy=1.,
                            transition=width,control_transition=a.control_transition)))
    rows=[]
    for design in designs:
        s=design['settings'];core=Core(q,c,3,arc_nodes=2048,**s)
        g=core.evaluate(u)
        jets=[g['F'],g['Ft']*du[:,None],g['Ftt']*du[:,None]**2+g['Ft']*ddu[:,None]]
        spectra={}
        for j,name in enumerate(('F','F_psi','F_psipsi')):
            co=np.fft.fft(jets[j]-background[j],axis=0)/N
            mag=np.linalg.norm(co,axis=1)
            spectra[name]={str(m):float(mag[freq>3*m+1].sum())for m in (8,16,24,32)}
            spectra[name]['above_N_over_4']=float(mag[freq>N//4].sum())
        row=dict(label=design['label'],settings=s,original_rho_guard_lower=core.rho_lower,
                 rho_sample_min=core.rho_min_sample,arc_inverse_residual=float(abs(g['arc_residual']).max()),
                 perturbation_vector_fft_l1=spectra)
        rows.append(row)
        print(json.dumps(dict(label=row['label'],primary=s['transition'],control=s['control_transition'],
                              homotopy=s['homotopy'],F_psipsi=spectra['F_psipsi'])),flush=True)
    files=[Path(__file__),Path(__file__).with_name('diagnose_primary_flatten_width.py'),
           M3/'couple_m3_smallcut_secant.py',*sorted(LIB.glob('*.py'))]
    result=dict(scope=__doc__,command=sys.argv,input_checkpoint=str(a.checkpoint.resolve()),
        input_checkpoint_sha256=sha(a.checkpoint),source_sha256={str(f.resolve()):sha(f)for f in files},
        actual_q=q,all_actual_controls=len(c),physical_controls_sha256=hashlib.sha256(c.astype('<f8').tobytes()).hexdigest(),
        source_modes=M,warp_reference_q=r['warp_reference_q'],inlet_warp_e=e,samples=N,
        chart_definition='u=psi-e*sin(3*psi)/3; e=8*input.warp_reference_q, unchanged for every row',
        derivative_definition='F_psipsi=F_uu*(du/dpsi)^2+F_u*d2u/dpsi2',
        perturbation_definition='Subtract exact analytic derivatives of exp(i*u(psi)) before FFT',
        cutoff_definition='absolute Cartesian frequency greater than 3*M+1; finite sampled FFT l1 only',
        rows=rows,seconds=time.monotonic()-start,
        limitations='Changing width or lambda changes the complete physical core. These scalar spectra only help choose a new design; they are not the original solver projection, an infinite-tail certificate, a full metric residual, or evidence of a solved endpoint.')
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
