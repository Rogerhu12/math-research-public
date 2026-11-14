#!/usr/bin/env python3
"""Coarse proved background boxes on every exact finite-tail/collar span.

This is a complete-domain valid packet. Its outer boxes are deliberately
wide; it is intended to let the independent backend certify deep spans
while a tighter outer source packet is computed.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np

from db6f_tail_integrated import IntegratedTail
from db6f_tail_interval_elementary import qbounds
from db6f_tail_background_primitive import strong_profile_anchors


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ['manifest','alpha','cell-zero-A','inner-A','outer-B','out-prefix']:
        ap.add_argument('--'+k,type=Path,required=True)
    args=ap.parse_args()
    t=IntegratedTail(args.manifest)
    al=json.loads(args.alpha.read_text());az=json.loads(args.cell_zero_A.read_text())
    ai=json.loads(args.inner_A.read_text());bo=json.loads(args.outer_B.read_text())
    # Every integral is tied to the same exact source checkpoint, while the
    # finite numerical solution may have a different M/RK discretization.
    hashes=[x['checkpointSHA256'] for x in [az,ai,bo]]
    if len(set(hashes))!=1 or hashes[0]!=al['inputs']['checkpoint']['sha256']:
        raise ValueError('mixed source integral bindings')
    cp_path=Path(al['inputs']['checkpoint']['file'])
    if not cp_path.exists():cp_path=args.alpha.parent/cp_path.name
    raw=cp_path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=hashes[0]:raise ValueError('source checkpoint hash mismatch')
    cp=json.loads(gzip.decompress(raw) if cp_path.suffix=='.gz' else raw)
    response=cp.get('response',cp);source=response.get('checkpoint',response)['parameters']
    keys=['rCut','rCuff','wCut','width','curvatureBound','delta0','R','a','etaPower','etaRatioAtN0','orientation',
          'prefixR','prefixEnd','prefixReturnStart','protectCell','slopeCap','capTransition','capMode',
          'valleyControls','pulseCaps','valleyCaps','warpWeightLevels','prefixRByCell']
    if any(t.meta['parameters'].get(k)!=source.get(k) for k in keys):
        raise ValueError('manifest and certified source define different backgrounds')
    anchors=strong_profile_anchors(t.meta['parameters'],al['exactRadialAlpha'],az,ai,bo,1)
    threshold=Q(anchors[(0,0)]['left'][0])
    if t.unscaled_lengths is None:nodes=[Q(float(x)) for x in t.r_display]
    else:
        rg=t.meta['radialGeometry'];nodes=[Q(rg['innerAnchor'])]
        for x in t.unscaled_lengths:nodes.append(nodes[-1]+t.radial_scale*Q(float(x)))
        if nodes[-1]!=Q(rg['outerAnchor']):raise ValueError('exact radial anchor invariant failed')
    if Q(t.meta['parameters']['rCuff'])>=nodes[0] or nodes[0]>threshold:
        raise ValueError('collar is not strictly inside the proved constant-cap region')
    count=len(nodes)
    index=np.arange(-1,count-1,dtype=np.int64)
    upper=np.array([nodes[0]]+nodes[1:],dtype=object)
    inner=np.array([v<=threshold for v in upper])
    wmax=np.where(inner,float(qbounds(Q(1,49)).hi),float(qbounds(Q(16,15)).hi))
    wrmax=np.where(inner,6.01,24.)
    data=Path(str(args.out_prefix)+'.npz')
    np.savez_compressed(data,span_index=index,u_left=np.zeros(count),u_right=np.ones(count),
                        w_lo=np.zeros((count,1)),w_hi=wmax[:,None],w_remainder=np.zeros(count),
                        wr_lo=-wrmax[:,None],wr_hi=wrmax[:,None],wr_remainder=np.zeros(count))
    if data.stat().st_size>=5000000:raise ValueError('packet exceeds per-file bound')
    here=Path(__file__).parent.parent
    proofs=['2026-11-09-db6f-tail-background-collar-proof.md',
            '2026-11-09-db6f-tail-background-height-bound.md',
            '2026-11-09-db6f-audit-entire-background-curvature.md']
    result={'status':'proved-coarse-background-packet-outer-refinement-pending','scope':__doc__,
            'finite_tail_manifest':str(args.manifest),'finite_tail_manifest_sha256':sha(args.manifest),
            'data_file':data.name,'data_sha256':sha(data),'finished':True,
            'background_definition_hashes':al['inputs'],
            'proof_hashes':{name:sha(here/'notes'/name) for name in proofs},
            'script_sha256':sha(__file__),'primitive_module_sha256':sha(Path(__file__).with_name('db6f_tail_background_primitive.py')),
            'inner_constant_cap_valid_through_radius_lower':float(threshold),
            'all_spans':count,'inner_box_spans':int(np.sum(inner)),'outer_box_spans':int(np.sum(~inner)),
            'background_curvature_bound':6,'coefficient_basis':'power in local tau, degree zero',
            'exact_radial_anchor_invariant':True,
            'bounds_reason':'For r below the certified inner boundary of cell zero, finite inner caps are <=1/49 and the reviewed infinite raw background is smaller. Its background meridian curvature <=6 gives |wr|<=6(1+1/49^2)^(3/2)<6.01. The whole background has w<=16/15 and |wr|<24.',
            'not_certified':['complete surface metric','complete surface curvature/reach','README completion']}
    Path(str(args.out_prefix)+'.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['all_spans','inner_box_spans','outer_box_spans','inner_constant_cap_valid_through_radius_lower']}))


if __name__=='__main__':main()
