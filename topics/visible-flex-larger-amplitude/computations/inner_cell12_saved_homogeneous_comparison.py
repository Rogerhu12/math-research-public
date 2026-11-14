#!/usr/bin/env python3
"""Compare the two saved cell12 homogeneous upper matrices, without replay.

This records a negative result: the new ordered-panel source kernel is
useful, but its complete homogeneous matrix does not improve the old one.
"""
import argparse
import hashlib
import json
from pathlib import Path
import time
import resource
from flint import arb,ctx
from inner_true_cell13_endpoint_window_kernels import sha,read,ab,pack,lower_pack
from closure_split_joint_io_v2 import metadata_without_array


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('ordered','base','panels','out'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();started=time.monotonic();ctx.prec=256;ctx.threads=1
    if a.out.exists():raise FileExistsError(a.out)
    pins={a.ordered:'4ffa4e25efb846a3f54569b79b79c379db7c09e356c0561217b49f238aa29329',a.base:'5e03915b960e6ebdfa6847d155a82af5e54866e2bd0fde3e177815d7ea821133',a.panels:'d0dc6791001a1668afa2f9442bbefbe7e6644e73b0b753943df5a9bc12258181'}
    if any(sha(k)!=v for k,v in pins.items()):raise ValueError('Frozen actual input changed')
    d,b=read(a.ordered),read(a.base);meta=metadata_without_array(a.panels,'panels')
    if not(d['all_gates'] and b['all_gates']):raise ValueError('Completed actual kernels required')
    dt=ab(meta['tau_inner'],'lower')-ab(meta['tau_outer']);rows=[]
    for row in d['rows']:
        m=row['window'][0];old=next(z for z in b['rows'] if z['window']==[m,m]);entries=[]
        decay=(-m*dt).exp()
        for i in range(2):
            for j in range(2):
                old_upper=(ab(old['whole_cell_positive_matrix_upper'][i][j])*decay).upper()
                new=ab(row['complete_weighted_homogeneous_matrix_upper'][i][j])
                if not(0<old_upper<new):raise ArithmeticError('Claimed strict entrywise no-improvement is false')
                ratio=new/old_upper
                entries.append({'entry':[i,j],'old_weighted_upper':pack(old_upper),'new_weighted_upper':pack(new),'new_over_old_ratio_lower':lower_pack(ratio),'new_over_old_ratio_upper':pack(ratio)})
        rows.append({'mode':m,'entries':entries})
    out={'schema':'inner-cell12-saved-homogeneous-negative-result-v1','author':'geometry_audit (GPT-6 Astra Pro; AI-assisted)',
         'all_gates':True,'strict_entrywise_comparisons':8,'source_sha256':sha(__file__),'input_sha256':{str(k):v for k,v in pins.items()},
         'result':'The complete old A times the exact full moving-strip multiplier is entrywise strictly below the new ordered-panel homogeneous upper matrix. Every identical nonnegative input/output conversion therefore prefers the old bound. This does not weaken the separately proved new inhomogeneous source columns.',
         'new_fixedpoint_or_truecut_claimed':False,'new_ODE_quadrature_or_replay':0,'rows':rows,'elapsed_seconds':time.monotonic()-started,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'all_gates':True,'comparisons':8,'path':str(a.out),'sha256':sha(a.out)}),flush=True)


if __name__=='__main__':main()
