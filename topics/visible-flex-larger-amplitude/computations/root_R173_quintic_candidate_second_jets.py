#!/usr/bin/env python3
"""Define approximate second jets for a new explicit quintic candidate.

No accuracy of these numerical second jets is assumed in a proof. The exact
binary coefficients they define must subsequently pay a complete continuous
mean and original-equation residual. No ODE or BVP is run here.
Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import resource
import sys
import time
import numpy as np
from flint import arb, ctx

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);raw=p.read_bytes();return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--R170-inputs',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();assert not a.out.exists();started=time.monotonic();ctx.prec=256;ctx.threads=1
    ids=read(a.R170_inputs);counts={}
    def gate(k,v):
        counts[k]=counts.get(k,0)+1
        if not v:raise ArithmeticError(k)
    for k in ('jets','jets_resource','jets_source','original_ready','original_source_manifest'):
        gate('identity_'+k,sha(ids['files'][k]['path'])==ids['files'][k]['sha256'])
    jets=read(ids['files']['jets']['path']);owned=read(ids['files']['jets_resource']['path'])
    gate('actual_original_first_jets',owned['exitcode']==0 and jets['all_gates'] and len(jets['pieces'])==216)
    original=read(ids['files']['original_source_manifest']['path'])
    for row in original['source_files']:gate('original_source_identity',sha(row['path'])==row['sha256'])
    sys.path.insert(0,ids['original_sources_directory'])
    from tail_r33_middle_ordered_physical import SourceValues
    from closure_real_linear_head_enclosure import PositiveKernels
    h=SourceValues(read(ids['files']['original_ready']['path']));ker=PositiveKernels(h,12,92);h.cells={n:ker.source_cell(n) for n in (7,8,9)}
    modes=np.arange(2,41,2,dtype=float);N=1024;theta=2*np.pi*np.arange(N)/N
    co=np.cos(np.outer(theta,modes));si=np.sin(np.outer(theta,modes));epsilon=2.0**-18
    rows=[];max_endpoint_defect=max_second=0.;min_angle_denominator=1.
    def background(bg,x,r):
        q=h.source_point(bg,arb(x));w=float(q['w']);ell=float(q['log_w_x']);ro_x=float(q['ro_x']);E=1+w*w
        rx=abs(w*ell)/(8*E**1.5)+float(h.alpha)*ro_x/E
        return w,rx/(8*r),ell/8,rx/8
    def field(bg,x,r,y):
        nonlocal min_angle_denominator
        P,K=y[:20],y[20:];w,s,ell,_=background(bg,x,r);E=1+w*w
        q0=float(np.sum((K*K+E*P*P)/4+modes*K*P/2));disc=1-2*q0
        if not disc>0:raise ArithmeticError('Candidate quadratic mean branch is undefined')
        c=-2*q0/(1+np.sqrt(disc))
        pv=si@P;tv=co@(modes*P);kv=c+co@K;uv=-si@(modes*K)-pv
        den=1+kv+E*tv;min_angle_denominator=min(min_angle_denominator,float(den.min()))
        if not den.min()>0:raise ArithmeticError('Candidate quadrature denominator is not positive')
        rhs=(E*s*uv*uv+ell*((kv+tv)**2+w*w*(2*kv*tv+tv*tv-pv*pv)))/den
        nm=(2./N)*(co.T@rhs)
        return np.r_[-(s+ell)*P-modes*s*K,-modes*ell*P-2*ell*K+nm]
    for original_row in jets['pieces']:
        n,j,k=original_row['raw_cell'],original_row['raw_segment'],original_row['part'];bg=h.cells[n]['segments'][j];seconds=[];diags=[]
        for side in (0,1):
            x=(k+side)/8.;ep=original_row['endpoint_jets'][side];r=float(ep['r'])
            y=np.r_[original_row['P'+str(side)],original_row['K'+str(side)]]
            dy=np.r_[original_row['dP'+str(side)],original_row['dK'+str(side)]]
            _,_,_,rt=background(bg,x,r)
            f0=field(bg,x,r,y);defect=float(np.max(np.abs(f0-dy)));max_endpoint_defect=max(max_endpoint_defect,defect)
            plus=field(bg,x+epsilon/8,r+epsilon*rt,y+epsilon*dy)
            minus=field(bg,x-epsilon/8,r-epsilon*rt,y-epsilon*dy)
            dd=(plus-minus)/(2*epsilon)
            gate('all_explicit_second_jet_coefficients_finite',bool(np.isfinite(dd).all()))
            max_second=max(max_second,float(np.max(np.abs(dd))));seconds.append(dd)
            diags.append(dict(side=side,raw_x=x,original_binary_radius=r,local_radius_first=rt,endpoint_finite_quadrature_field_defect=defect))
        rows.append(dict(stage_index=original_row['stage_index'],cell=n,segment=j,part=k,
            ddP0=seconds[0][:20].tolist(),ddP1=seconds[1][:20].tolist(),ddK0=seconds[0][20:].tolist(),ddK1=seconds[1][20:].tolist(),endpoint_diagnostics=diags))
    gate('all216_explicit_pieces',len(rows)==216 and len({(r['cell'],r['segment'],r['part']) for r in rows})==216)
    result=dict(schema='explicit-quintic-candidate-approximate-second-jets-v1',author='/root (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),
        R170_input_manifest=dict(path=str(a.R170_inputs),sha256=sha(a.R170_inputs)),original_jets_sha256=ids['files']['jets']['sha256'],
        all_gates=True,gate_count=sum(counts.values()),gate_categories=counts,rows=rows,
        finite_angular_nodes=N,local_stage_difference_epsilon=epsilon,local_to_raw_x_scale='1/8',
        candidate_definition='For each endpoint, centered finite difference of the displayed normalized finite-angle field along its original first jet and the linear radius path. The quadratic mean approximation is used only to define binary second-jet coefficients.',
        quintic_Bernstein_definition=['y0','y0+d0/5','y0+2*d0/5+dd0/20','y1-2*d1/5+dd1/20','y1-d1/5','y1'],
        max_endpoint_field_defect_diagnostic=max_endpoint_defect,max_absolute_second_jet=max_second,minimum_sampled_denominator_diagnostic=min_angle_denominator,
        second_jet_accuracy_certified=False,complete_mean_or_infinite_equation_paid_here=False,no_new_ODE_BVP_or_factory=True,
        subsequent_exact_binary_candidate_and_complete_continuous_residual_required=True,elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    raw=(json.dumps(result,separators=(',',':'))+'\n').encode();a.out.write_bytes(gzip.compress(raw,mtime=0) if a.out.suffix=='.gz' else raw)
    print(json.dumps(dict(path=str(a.out),sha256=sha(a.out),gate_count=result['gate_count'],max_endpoint_field_defect=max_endpoint_defect,max_second_jet=max_second,elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)

if __name__=='__main__':main()
