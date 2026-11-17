#!/usr/bin/env python3
"""Compare exact-circle primary designs with different flattening widths.

Only the primary core is sampled, with all complementary controls zero.
The underlying integral core is retained. This is neither an actual BVP nor
a continuous spectral bound, and changing width defines a new design.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
import numpy as np

LIB=Path(__file__).resolve().parent.parent/'resume_m3/round_raw_lib'
sys.path.insert(0,str(LIB))
from plateau_core import PlateauSupportCore
from fixed_large_radius_core import make_core_class
from tight_moment_interval_bounds import install
install()
Core=make_core_class(PlateauSupportCore)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--widths',type=float,nargs='+',default=[.08,.12,.16,.24,.32])
    p.add_argument('--q',type=float,default=.085)
    p.add_argument('--halfwidth',type=float,default=.21)
    p.add_argument('--samples',type=int,default=12288)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();N=a.samples
    if N%3 or N<4096:raise ValueError('Use a fine grid compatible with C3')
    u=2*np.pi*np.arange(N)/N;freq=abs(np.rint(np.fft.fftfreq(N)*N).astype(int))
    rows=[]
    for width in a.widths:
        core=Core(a.q,(),3,halfwidth=a.halfwidth,transition=width,homotopy=1.,center=np.pi/3,
                  control_transition=.4,lock_fundamental=True,bimodal_eta=0.,arc_nodes=2048,
                  coefficient_precision=80,positivity_grid_max=32768)
        g=core.evaluate(u);c=np.fft.fft(g['Ftt'],axis=0)/N
        magnitude=np.linalg.norm(c,axis=1)
        k=np.abs(np.fft.fft(g['kappa'])/N)
        center=core.normal_geometry(np.array([np.pi/3]))['F'][0]
        R=1+8*a.q;circle_center=center-R*np.array([.5,math.sqrt(3)/2,0.])
        center_distance=float(np.linalg.norm(circle_center))
        phi=np.linspace(np.pi/3-a.halfwidth,np.pi/3+a.halfwidth,65)
        arc=core.normal_geometry(phi)
        rows.append(dict(flatten_transition=width,flatten_beta=core.local_flatten_beta,
            source_rho_guard_lower=core.rho_lower,sampled_rho_min=core.rho_min_sample,
            sampled_radius_max=core.radius_max_sample,circle_radius=R,
            sampled_circle_center_distance=center_distance,
            sampled_circle_arc_rho_defect=float(abs(arc['rho']-R).max()),
            circle_center_constant_sample=center_distance/a.q,
            conditional_c3_witness_sample=math.sqrt(3)*center_distance*math.sin(.7046/(2*R)),
            retained_state_cutoffs={str(M):dict(
                Fuu_vector_fft_l1_above_3Mplus1=float(magnitude[freq>3*M+1].sum()),
                kappa_fft_l1_above_3M=float(k[freq>3*M].sum()))for M in (8,16,24,32)},
            far_frequency_Fuu_vector_l1=float(magnitude[freq>N//4].sum())))
        print(json.dumps(rows[-1]),flush=True)
    result=dict(scope=__doc__,arguments={k:str(v)if isinstance(v,Path)else v for k,v in vars(a).items()},
        physical_definition=dict(base_mode=3,bimodal_eta=0,homotopy=1,all_complementary_controls_zero=True,
                                 protected_halfwidth=a.halfwidth,phase_for_conditional_witness=.7046),
        source_sha256={str(x.resolve()):hashlib.sha256(x.read_bytes()).hexdigest()for x in [Path(__file__),*sorted(LIB.glob('*.py'))]},
        rows=rows,interpretation='Normal-angle flattening width changes the mathematical primary curve. Frequency summaries use the physical material angle u, and finite FFT l1 is not a certified infinite tail. The R32 whole-surface budgets and any fixed-g convergence are not inherited.')
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')


if __name__=='__main__':main()
