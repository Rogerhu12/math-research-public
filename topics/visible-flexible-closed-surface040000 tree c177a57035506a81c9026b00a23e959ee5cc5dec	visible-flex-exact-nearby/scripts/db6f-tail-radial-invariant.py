#!/usr/bin/env python3
"""Independently verify the exact increment/anchor invariant of a tail export."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
from db6f_tail_integrated import IntegratedTail


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('manifest',type=Path);ap.add_argument('out',type=Path)
    args=ap.parse_args();t=IntegratedTail(args.manifest)
    if t.unscaled_lengths is None:raise ValueError('requires increment geometry')
    radial=t.meta['radialGeometry'];inner=Q(radial['innerAnchor']);outer=Q(radial['outerAnchor'])
    ell=[Q(float(v)) for v in t.unscaled_lengths]
    if not all(v>0 for v in ell):raise ValueError('nonpositive exact binary increment')
    total=sum(ell,Q(0));saved=radial['unscaledSum'];exponent=saved['binaryExponent']
    advertised=Q(int(saved['numerator']))*(Q(2)**exponent)
    if total!=advertised:raise ValueError('saved unscaled sum differs from actual data')
    if t.radial_scale!=(outer-inner)/total:raise ValueError('normalization does not equal the exact anchor ratio')
    if inner+t.radial_scale*total!=outer:raise ValueError('exact outer anchor equality fails')
    if radial['spanCount']!=len(ell):raise ValueError('wrong span count')
    if any(info['bytes']>=5000000 for info in t.meta['files']):raise ValueError('file exceeds explicit size bound')
    result={'status':'exact-rational-increment-anchor-invariant-pass','scope':__doc__,
            'manifest':str(args.manifest),'manifestSHA256':sha(args.manifest),'scriptSHA256':sha(__file__),
            'readerSHA256':sha(Path(__file__).with_name('db6f_tail_integrated.py')),
            'spans':len(ell),'nodes':len(ell)+1,'dataFiles':len(t.meta['files']),
            'allDataHashesAndSharedRowsVerified':True,'unscaledSumMatchesData':True,
            'normalizationEqualsExactAnchorRatio':True,'exactFinalAnchorEquality':True,
            'innerAnchorExact':str(inner),'outerAnchorExact':str(outer),
            'largestCompressedFileBytes':max(info['bytes'] for info in t.meta['files']),
            'notCertified':['target metric','curvature or reach','source ODE or solver convergence']}
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['manifestSHA256','spans','nodes','dataFiles','exactFinalAnchorEquality','largestCompressedFileBytes']}))


if __name__=='__main__':main()
