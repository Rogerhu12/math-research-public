#!/usr/bin/env python3
"""Rebase the complete native-prefix Gram enclosure to the original manifest cuff."""
from fractions import Fraction as F
import argparse
import hashlib
import json
from pathlib import Path


def transfer(prefix,correction,manifest):
    if not (prefix['complete_original_prefix'] and prefix['complete_elements']==158
            and correction['continuous_all_knots_and_all_angles']
            and prefix['field_sha256']==correction['field_sha256']
            =='5778bee4c19c6f878e2039876a9b250e940b7b4d0d9f949b1982bf6cebf5a5b8'):
        raise ValueError('Incompatible complete original prefix and derivative envelope')
    s0,s1=map(F,prefix['common_q_endpoint_interval'])
    cut,cuff=[F.from_float(manifest['parameters'][k]) for k in ('rCut','rCuff')]
    h0=F(.6)-F(.15)
    h1=cut-cuff
    if not (cut==F(manifest['radialGeometry']['outerAnchor'])==F(.6)
            and h1-h0==F(1,2**55)
            and list(map(F,prefix['common_z_endpoint_interval']))==[s0/(s0+h0),s1/(s1+h0)]):
        raise ValueError('Unexpected chart source lengths')
    # q is the same original physical prefix meridian coordinate for both fields.
    T0=s0+h0;T1=s0+h1
    dinv=abs(h1-h0)/(T0*T1);dz=s1*dinv
    M=correction['raw_unit_chart_bounds']
    raw=lambda i,j:F(M[str((i,j))]['upper_exact'])
    u1=F(correction['central_source_constants']['U1']['upper_exact'])
    # The R226 globally valid f>=rCuff also holds on this whole prefix.
    ds=raw(2,0)*dz/T1+raw(1,0)*dinv
    du=raw(1,1)*dz*u1/cuff
    d=ds+du
    old=F(prefix['maximum_relative_metric_upper_exact'])
    gram=2*(1+old)*d+d*d
    new=old+gram
    if new>=F(prefix['requested_B_exact']):raise ArithmeticError('Original tolerance missed')
    vals=dict(commonPhysicalSInterval=[str(s0),str(s1)],proxyCuff=str(F(.15)),actualCuff=str(cuff),
              proxyWidth=str(h0),actualWidth=str(h1),widthChange=str(h1-h0),
              actualCommonCutUnitInterval=[str(s0/(s0+h1)),str(s1/(s1+h1))],
              positionParameterShiftUpper=str(dz),differentialRadialUpper=str(ds),
              differentialAngularOrthonormalUpper=str(du),differentialOperatorUpper=str(d),
              relativeGramPerturbationUpper=str(gram),actualEntirePrefixGramUpper=str(new))
    return vals


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ('prefix','correction','manifest','out'):ap.add_argument('--'+k,type=Path,required=True)
    a=ap.parse_args()
    def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
    p,c,m=[json.loads(x.read_bytes()) for x in (a.prefix,a.correction,a.manifest)]
    if p['correction_bounds_sha256']!=digest(a.correction) or c['tail_manifest_sha256']!=digest(a.manifest):
        raise ValueError('Original proof inputs differ')
    record=dict(schema='2ecf-M12-original-actual-cuff-prefix-one-ulp-transfer-v1',
                entrySHA256=digest(Path(__file__)),prefixSHA256=digest(a.prefix),
                correctionSHA256=digest(a.correction),manifestSHA256=digest(a.manifest),
                **transfer(p,c,m))
    with a.out.open('x') as f:json.dump(record,f,indent=2);f.write('\n')
    for name in ('positionParameterShiftUpper','relativeGramPerturbationUpper','actualEntirePrefixGramUpper'):
        print(name,float(F(record[name])))


if __name__=='__main__':main()
