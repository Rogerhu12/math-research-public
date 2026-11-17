#!/usr/bin/env python3
"""Extract signed physical cosine height trace H and radial derivative at cut.
Mean position is omitted here; only the full represented nonzero modes are used.
For full Cartesian two-jets use the recovery endpoint method with ShortBridge
installed. These are finite-prefix data, not a nonlinear tail seam certificate.
"""
import argparse,hashlib,json,sys
from pathlib import Path
import numpy as np
from scipy.interpolate import PPoly
p=argparse.ArgumentParser();p.add_argument('checkpoint',type=Path);p.add_argument('--source-topic',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
sys.path.insert(0,str(a.source_topic/'repro/source-root/topics/large-amplitude-twist-flex/scripts'))
from curve_stable_prefix_bvp import load_checkpoint
r=load_checkpoint(a.checkpoint);M=r['config']['modes'];q=r['gauge_amplitude'];s=r['meridian_length'];pp=PPoly.construct_fast(np.array(r['pp_coefficients']),np.array(r['mesh']),extrapolate=True,axis=1)
cut=r['physical_tail_cut'];w=cut['backgroundSlope'];ap=-1/np.sqrt(1+w*w);H=q*pp(s)[-M:];Hs=q*pp(s,1)[-M:];Hr=Hs/ap
out=dict(scope=__doc__,checkpoint=str(a.checkpoint),checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),solver_success=r['solver_success'],actual_primary_amplitude=r['actual_primary_amplitude'],profile=r['frozen_profile'],cut=cut,sigma=-1.,modes=(2*np.arange(1,M+1)).tolist(),H=H.tolist(),Hs=Hs.tolist(),Hr=Hr.tolist(),H_l1=float(np.abs(H).sum()),metric_l1=r.get('summary',{}).get('metric_l1'),sampled_kappa=r.get('summary',{}).get('kappa_sample'),sampled_height=r.get('summary',{}).get('height_max'))
a.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
