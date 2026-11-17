#!/usr/bin/env python3
"""Complete represented signed upper-prefix height jets at an identity m3 cut.

For the positive-zr actual tail worker use -H, then reflect the full tail z,
including its nonlinear mean. This does not certify a nonlinear tail seam.
"""
from pathlib import Path
import argparse,hashlib,json,math,sys
import numpy as np
from scipy.interpolate import PPoly
p=argparse.ArgumentParser();p.add_argument('--source-topic',type=Path,required=True);p.add_argument('--checkpoint',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
sys.path.insert(0,str(a.source_topic/'repro/source-root/topics/large-amplitude-twist-flex/scripts'))
from curve_stable_prefix_bvp import load_checkpoint
r=load_checkpoint(a.checkpoint);M=r['config']['modes'];base=r['config']['base_mode'];q=r['gauge_amplitude'];end=r['meridian_length'];cut=r['physical_tail_cut'];E=cut['E'];Ep=cut['Ep'];pp=PPoly.construct_fast(np.asarray(r['pp_coefficients']),np.asarray(r['mesh']),extrapolate=True,axis=1)
if base!=3 or not r['solver_success']:raise ValueError('Expected a successful actual m3 prefix')
H=q*pp(end)[-M:];Hs=q*pp(end,1)[-M:];Hss=q*pp(end,2)[-M:];Hr=-math.sqrt(E)*Hs;Hrr=E*Hss+Ep/(2*E)*Hr
d=dict(scope=__doc__,checkpoint=str(a.checkpoint),checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),modes=(base*np.arange(1,M+1)).tolist(),H=H.tolist(),Hs=Hs.tolist(),Hss=Hss.tolist(),Hr=Hr.tolist(),Hrr=Hrr.tolist(),cut=cut,sigma=-1.,actual_primary_amplitude=r['actual_primary_amplitude'],frozen_profile=r['frozen_profile'],physical_tail_parameters=r['physical_tail_parameters'],port_sha256=r['physical_port_sha256'],metric_sample=r.get('summary',{}).get('metric_l1'),H_l1=float(abs(H).sum()))
a.out.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({k:d[k]for k in ['actual_primary_amplitude','metric_sample','H_l1','checkpoint_sha256']}));print(json.dumps({'H_first4':d['H'][:4],'out':str(a.out),'sha256':hashlib.sha256(a.out.read_bytes()).hexdigest()}))
