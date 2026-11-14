#!/usr/bin/env python3
"""Sample the accepted actual C2 polynomial with its original complete mean.

The saved nonmean polynomial and all original curvature/metric formulas are
retained. Geometry angles remain independent from the original postprocessor
mean rule max(512,16*(3*M+1)); the latter supplies both mean first and second
jets. All values remain finite spatial samples, not continuous certificates.
No field, profile, metric, nonlinear solve or acceptance gate is changed.
"""
from __future__ import annotations
import ast
import hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXPECTED = '1b7f45785fffc41595eda9aae844c3081d2954d3ea08ac0da6e5a90c935294fa'


def main():
    original = (HERE/'strong_interior_jet_audit.py').read_text()
    if hashlib.sha256(original.encode()).hexdigest() != EXPECTED:
        raise ValueError('Original actual-polynomial audit source differs')
    edits = [
        ('    f=saved.flow;N=a.angular;B,B1,B2=f.basis(N);x=saved.sol.x',
         '    f=saved.flow;N=a.angular;B,B1,B2=f.basis(N);x=saved.sol.x\n'
         '    meanN=max(512,16*(3*f.M+1));_,meanB1,meanB2=f.basis(meanN)'),
        ("        aa,ap,app=f.profile(s);fr,Fsp,dW=f.velocity_s(s,Y,Yp,B1,B2);g=fr['geo'];rho=g['rho'];v=g['v']",
         "        aa,ap,app=f.profile(s);fr,Fsp,dW=f.velocity_s(s,Y,Yp,B1,B2);g=fr['geo'];rho=g['rho'];v=g['v']\n"
         '        if meanN==N:meanFrame,meanDW=fr,dW\n'
         '        else:meanFrame,_,meanDW=f.velocity_s(s,Y,Yp,meanB1,meanB2)'),
        ("np.mean(fr['V'][:,:,2],axis=1)", "np.mean(meanFrame['V'][:,:,2],axis=1)"),
        ('np.mean(dW[:,:,2],axis=1)', 'np.mean(meanDW[:,:,2],axis=1)'),
        ('config=dict(angular=N,radial=a.radial,batch=a.batch,interior_fractions=xi.tolist())',
         'config=dict(angular=N,radial=a.radial,batch=a.batch,interior_fractions=xi.tolist(),'
         'mean_angular=meanN,mean_rule="original physical postprocessor",'
         'original_audit_source_sha256=ORIGINAL_INTERIOR_AUDIT_SHA)'),
    ]
    source = original
    for before, after in edits:
        if source.count(before) != 1:
            raise ValueError('Original complete-mean jet anchor is not unique: '+repr(before))
        source = source.replace(before, after, 1)
    first = source.index('"""')
    last = source.index('"""', first+3)+3
    source = source[:first]+repr(__doc__)+source[last:]
    ast.parse(source, filename='<actual-interior-complete-mean>')
    namespace = dict(__file__=__file__, __name__='strong_original_interior_with_complete_mean',
                     ORIGINAL_INTERIOR_AUDIT_SHA=EXPECTED)
    exec(compile(source, '<actual-interior-complete-mean>', 'exec'), namespace)
    namespace['main']()


if __name__ == '__main__':
    main()
