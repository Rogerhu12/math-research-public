#!/usr/bin/env python3
"""Choose a lower-dimensional floating Codazzi endpoint, with explicit loss.

This produces a diagnostic initial state, not a projection of an exact PDE
solution.  All retained physical modes, including the mean, are preserved;
the Nyquist and higher modes are discarded and the loss is reported.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np
from fourfold_phase_codazzi_evolution_probe import resample
from fourfold_phase_local_correction_probe import sha


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--state-in',type=Path,required=True)
    p.add_argument('--angles',type=int,required=True)
    p.add_argument('--state',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();old=np.load(args.state_in,allow_pickle=False)
    state=old['state'];oldn=len(state);n=args.angles
    if n<8 or n%2 or not n<oldn:raise ValueError('an even, smaller angular grid is required')
    meta=json.loads(str(old['metadata']));freq=np.fft.fftfreq(oldn,1/oldn)
    coeff=np.fft.fft(state,axis=0)/oldn;chosen=resample(state,n)
    delta=state-resample(chosen,oldn)
    doc=dict(kind='floating_finite_Codazzi_endpoint_projection',certified=False,
        source_sha256=sha(__file__),input_state_path=str(args.state_in),input_state_sha256=sha(args.state_in),
        r=float(old['r']),input_angles=oldn,output_angles=n,physical_frequency_factor=4,
        retained_positive_index=[0,n//2-1],Nyquist_omitted=True,mean_retained=True,
        removed_coefficient_l1_by_column=np.sum(abs(coeff[abs(freq)>=n//2]),axis=0).tolist(),
        sampled_projection_difference_by_column=np.max(abs(delta),axis=0).tolist(),
        columns=old['columns'].tolist(),object_sha256=meta['object_sha256'],
        dependency_sha256={'fourfold_phase_codazzi_evolution_probe.py':sha(Path(__file__).with_name('fourfold_phase_codazzi_evolution_probe.py'))},
        limitations=['Finite, floating projection only; the input state has unvalidated PDE errors.',
            'Discarded channels are listed, not treated as zero for the original PDE.'])
    np.savez_compressed(args.state,r=old['r'],state=chosen,columns=old['columns'],
        metadata=np.array(json.dumps(dict(kind=doc['kind'],object_sha256=meta['object_sha256'],
            source_sha256=doc['source_sha256'],parent_state_sha256=doc['input_state_sha256']))))
    doc['output_state_path']=str(args.state);doc['output_state_sha256']=sha(args.state)
    args.out.write_text(json.dumps(doc,indent=2)+'\n')
    print({k:doc[k] for k in ('r','input_angles','output_angles','removed_coefficient_l1_by_column')})


if __name__=='__main__':main()
