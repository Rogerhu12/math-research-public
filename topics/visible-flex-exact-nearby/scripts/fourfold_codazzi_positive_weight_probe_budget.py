#!/usr/bin/env python3
"""Floating feasibility check of the exact finite comparison weights.

This reads every saved coefficient but samples the radial/angular domain.
Its output is explicitly not a proof, even when its trial barrier passes.
The residual majorants are copied from the actual complete native report;
the weight inequalities still require an independent directed enclosure.
"""
from __future__ import annotations
import argparse,bisect,gzip,io,json,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_local_correction_probe import sha,scalar_target
from fourfold_phase_codazzi_dense_candidate import full_coefficients
from fourfold_codazzi_sharded_candidate import ShardedDenseCandidate


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--weights',type=Path,required=True)
    ap.add_argument('--native',type=Path,default=Path('notes/2026-11-13-Codazzi-cubic-cleared-r02-n1024-v1-native.json.gz'))
    ap.add_argument('--candidate',type=Path,default=Path('notes/2026-11-13-codazzi-dense-r02-n1024-candidate-shards.json'))
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--grid',type=int,default=2048)
    ap.add_argument('--tubes',type=float,nargs='+',default=[.002,.005,.01,.02,.0625])
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();start=time.monotonic()
    if a.out.exists():raise FileExistsError('new diagnostic report required')
    d=json.loads(gzip.decompress(a.native.read_bytes()))
    if not d['complete'] or d['failure'] is not None:raise ValueError('complete true residual input required')
    with np.load(io.BytesIO(gzip.decompress(a.weights.read_bytes())),allow_pickle=False) as z:
        nodes=z['time_nodes'];ends=z['positive_endpoint_coefficients'];meta=json.loads(str(z['metadata']))
    if meta['kind']!='exact_finite_piecewise_linear_Fourier_positive_weight_candidate':raise ValueError('wrong finite weight object')
    if meta['object_sha256']!=sha(a.object):raise ValueError('weight actual target differs')
    candidate=ShardedDenseCandidate(a.candidate);geometry,_=load_exact_object(a.object,512)
    if a.grid<2*candidate.grid:raise ValueError('complete finite candidate required')
    native_nodes=[float(Fraction(row['interval'][0])) for row in d['rows']]
    right=float(Fraction(d['covered_interval'][1]))
    cuts=sorted({0.,right}|{float(x) for x in nodes if 0<x<right}|{x for x in native_nodes if 0<x<right})
    samples=lambda c:(a.grid*np.fft.ifft(full_coefficients(c,a.grid),axis=0)).real
    records=[];barriers={T:2*d['actual_initial_error']['epsilon0']['mid_float']+1e-30 for T in a.tubes}
    maxerrors={T:0. for T in a.tubes};firstfailure={T:None for T in a.tubes}
    for index,(left,end) in enumerate(zip(cuts,cuts[1:])):
        wpiece=min(len(nodes)-2,bisect.bisect_right(nodes,(left+end)/2)-1)
        L,R=ends[wpiece:wpiece+2];dh=nodes[wpiece+1]-nodes[wpiece]
        Wr=samples((R-L)/dh)
        nrow=min(len(native_nodes)-1,bisect.bisect_right(native_nodes,(left+end)/2)-1)
        rho=d['rows'][nrow]['bounds']['rho0']['mid_float']
        lower=np.inf;upper=0.;rates={T:-np.inf for T in a.tubes}
        for r in np.linspace(left,end,5):
            v=L+(R-L)*((r-nodes[wpiece])/dh)
            W=samples(v);Wt=samples(1j*(4*np.arange(len(v)))[:,None]*v)
            # Positive Fourier differentiation keeps the conjugacy of each
            # derivative; the full function is reconstructed by samples().
            t=scalar_target(geometry,float(r));K=t['K'];k=np.sqrt(-K)
            gamma=np.sqrt(t['E'])/t['a'];beta=t['a_x']/t['a'];kappa=t['minus_K_x']/(-4*K)
            raw=candidate.evaluate(float(r),a.grid);B,C=raw['BC'].T;Bt,Ct=raw['BC_theta'].T
            P=(B+k)/C;Q=(B-k)/C
            Pt=Bt/C-(B+k)*Ct/C**2;Qt=Bt/C-(B-k)*Ct/C**2
            nominal=-2*beta*P*Q+kappa
            b=gamma*Pt-beta*(1+P*P)-kappa;c=gamma*Qt-beta*(1+Q*Q)-kappa
            n0=nominal*W[:,0]+abs(b)*W[:,1]+gamma*Q*Wt[:,0]-Wr[:,0]
            n1=nominal*W[:,1]+abs(c)*W[:,0]+gamma*P*Wt[:,1]-Wr[:,1]
            lower=min(lower,float(W.min()));upper=max(upper,float(W.max()))
            if np.min(W)<=0:
                raise ValueError(f'sampled weight positivity fails on piece {wpiece}')
            d0=abs(gamma*Wt[:,0]-2*beta*P*W[:,0])/W[:,0]
            d1=abs(gamma*Wt[:,1]-2*beta*Q*W[:,1])/W[:,1]
            for T in a.tubes:
                rate=max(np.max(n0/W[:,0]+T*d0+abs(beta)*T*(abs(Q)+T)),
                         np.max(n1/W[:,1]+T*d1+abs(beta)*T*(abs(P)+T)))
                rates[T]=max(rates[T],float(rate))
        h=end-left;outputs={}
        for T in a.tubes:
            rate=max(0.,rates[T]);forcing=rho/lower
            old=barriers[T]
            new=old*np.exp(h*rate)+forcing*(np.expm1(h*rate)/rate if rate else h)
            barriers[T]=new;error=upper*new;maxerrors[T]=max(maxerrors[T],error)
            if error>=T and firstfailure[T] is None:firstfailure[T]=index
            outputs[str(T)]=dict(L=rates[T],z=new,unweighted_error=error)
        records.append(dict(index=index,interval=[left,end],weight_piece=wpiece,native_row=nrow,
                            sampled_weight_min=lower,sampled_weight_max=upper,rho0=rho,trial=outputs))
        if index%50==0:print(dict(index=index,r=end,minW=lower,maxW=upper,trial=outputs),flush=True)
    out=dict(kind='floating_full_finite_positive_weight_comparison_diagnostic',complete=True,
        certified=False,continuation_certified=False,source_sha256=sha(__file__),
        inputs={str(p):sha(p) for p in (a.weights,a.native,a.candidate,a.object)},
        five_radial_samples_per_piece=True,angular_samples=a.grid,full_coefficients_retained=True,
        first_sampled_failure={str(k):v for k,v in firstfailure.items()},
        maximum_sampled_error={str(k):v for k,v in maxerrors.items()},rows=records,
        wall_seconds=time.monotonic()-start,
        scope='Feasibility diagnostic only. Sampled inequalities and floating barriers are not native enclosures.')
    a.out.write_text(json.dumps(out,indent=2)+'\n')
    print(dict(complete=True,maxerrors=maxerrors,firstfailure=firstfailure,seconds=out['wall_seconds']),flush=True)


if __name__=='__main__':main()
