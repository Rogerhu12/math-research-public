#!/usr/bin/env python3
"""Keep physical finite-piece lengths in the compact loop-control LP.

All geometry evaluation and cached directional samples are the original
compact screen. The LP additionally keeps loop_speed-vd at least .0005,
so its first-order continuation does not cross a zero-length sync segment.
It also bounds every original physical chart interval to .7 through 1.5
times its baseline length at first order. The actual combined warm geometry
is still evaluated; linear length rows are not a finite-step certificate.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import sys
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import numpy as np
import strong_20261114_compact_control_screen as screen


def main():
    prior=screen.optimize
    length_record={}
    def optimize(base,slopes,rows,names,core,profile,sampled,size_factors,trust):
        previous_lp=screen.linprog
        scales=np.asarray([screen.CONTROL[name][1] for name in names])
        derivative=np.asarray([rows[name]['row']['physical_profile_derivative'].get('vd',0.)-
            rows[name]['row']['physical_profile_derivative'].get('loop_speed',0.) for name in names])*scales
        bound=profile['loop_speed']-profile['vd']-.0005
        provider=sys.modules['root_dual_neck_provider']
        port=json.loads(Path(sys.argv[sys.argv.index('--port')+1]).read_text())
        def lengths(configuration):
            prefix=provider.NeckPrefix(configuration)
            bridge=provider.NeckTerminalBridge(provider.tagged_port(port,configuration)['cut'])
            breaks=np.unique(np.r_[prefix.breaks(),prefix.end+bridge.breakpoints])
            return np.diff(breaks)
        baseline_lengths=lengths(profile)
        slopes_length=np.empty((len(baseline_lengths),len(names)))
        for j,name in enumerate(names):
            step=1e-4
            changes=rows[name]['row']['physical_profile_derivative']
            values=[]
            for sign in (-1,1):
                changed=dict(profile)
                for key,value in changes.items():changed[key]=changed.get(key,0.)+sign*step*scales[j]*value
                values.append(lengths(changed))
            if any(value.shape!=baseline_lengths.shape for value in values):
                raise ValueError('The physical knot topology changed in a local length derivative')
            slopes_length[:,j]=(values[1]-values[0])/(2*step)
        length_record.update(baseline_lengths=baseline_lengths.tolist(),
            minimum_ratio=.7,maximum_ratio=1.5,
            normalized_control_length_derivatives=slopes_length.tolist(),
            finite_step_domain_guaranteed=False)
        def solve(objective,*args,**kwargs):
            row=np.zeros(len(objective));row[:len(names)]=derivative
            extended=np.zeros((len(baseline_lengths),len(objective)))
            extended[:,:len(names)]=slopes_length
            kwargs['A_ub']=np.vstack((kwargs['A_ub'],row,extended,-extended))
            kwargs['b_ub']=np.r_[kwargs['b_ub'],bound,.5*baseline_lengths,.3*baseline_lengths]
            return previous_lp(objective,*args,**kwargs)
        screen.linprog=solve
        try:return prior(base,slopes,rows,names,core,profile,sampled,size_factors,trust)
        finally:screen.linprog=previous_lp
    screen.optimize=optimize
    try:screen.main()
    finally:screen.optimize=prior
    output=Path(sys.argv[sys.argv.index('--compact-out')+1])
    result=json.loads(output.read_text())
    result['loop_sync_orientation_constraint']=dict(scope=__doc__,minimum_speed_gap=.0005,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        physical_interval_length_constraints=length_record,
        all_original_geometry_samples_and_formulas_retained=True)
    output.write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
