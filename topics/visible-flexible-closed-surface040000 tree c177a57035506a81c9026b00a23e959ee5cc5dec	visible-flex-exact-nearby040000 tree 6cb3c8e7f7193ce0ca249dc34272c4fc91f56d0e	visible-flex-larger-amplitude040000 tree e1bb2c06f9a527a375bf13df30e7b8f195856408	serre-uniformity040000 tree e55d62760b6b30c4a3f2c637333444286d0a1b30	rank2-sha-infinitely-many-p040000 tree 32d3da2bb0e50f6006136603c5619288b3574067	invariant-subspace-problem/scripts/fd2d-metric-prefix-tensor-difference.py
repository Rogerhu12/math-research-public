#!/usr/bin/env python3
"""Convert a continuous coordinate difference to the OLD induced C2 norm.

The reference area-element lower bound is taken from that same reference
map's existing complete continuous geometry certificate. All reference
coordinate jets are recomputed as continuous polynomial/Fourier bounds on
the difference report's exact subintervals. The old Levi-Civita connection
is controlled through its actual Gauss tangential projection, not replaced
by the target metric's connection.

This still covers a prefix only: whole-surface C2 matching and tails/caps
remain UNVERIFIED_GLOBALLY.
"""
from __future__ import annotations

import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'

import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
spec=importlib.util.spec_from_file_location('fd2d_tensor_difference_coordinates',
    HERE/'fd2d-metric-prefix-c2-difference.py')
diff=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=diff
spec.loader.exec_module(diff)
I,qb=diff.I,diff.qb


def positive_tensor_bound(a,b,c):
    """lambda_max of the nonnegative norm majorant [[a,b],[b,c]]."""
    return (I(a)+I(c)+((I(a)-I(c)).square()+4*I(b).square()).sqrt())/2


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--difference',type=Path,required=True)
    ap.add_argument('--reference-certificate',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--rows',type=Path)
    ap.add_argument('--batch',type=int,default=64)
    args=ap.parse_args()
    if args.out.exists() or (args.rows is not None and args.rows.exists()):
        raise FileExistsError('Select new report names')
    start=time.monotonic()
    data=json.loads(args.difference.read_text())
    if data['schema']!='fd2d-continuous-prefix-coordinate-c2-difference-v1':
        raise ValueError('Unknown coordinate difference schema')
    if diff.identity(HERE/'fd2d-metric-prefix-c2-difference.py')['sha256']!=data['script']['sha256']:
        raise ValueError('Coordinate report was produced by another source revision')
    row_record=data['row_data'];row_path=Path(row_record['file'])
    if not row_path.is_file():row_path=args.difference.parent/row_path.name
    if diff.identity(row_path)['sha256']!=row_record['sha256']:
        raise ValueError('Coordinate row data changed')
    source_rows=json.loads(gzip.decompress(row_path.read_bytes()))
    certificate=json.loads(args.reference_certificate.read_text())
    if not certificate['continuous_bounds_certified'] or not certificate['entire_finite_prefix_covered']:
        raise ValueError('Reference geometry certificate is not complete and continuous')
    if certificate['geometry_sha256']!=data['reference']['sha256']:
        raise ValueError('Reference area bound belongs to another map')
    ref_path=Path(data['reference']['file'])
    if not ref_path.is_file():ref_path=args.difference.parent/ref_path.name
    if diff.identity(ref_path)['sha256']!=data['reference']['sha256']:
        raise ValueError('Reference definition changed')
    ref,bindings=diff.load_geometry(ref_path,'tensor_reference')
    if str(ref.exact_length)!=data['reference_radial_length_exact']:
        raise ValueError('The radial normalization changed')
    area_raw=Q(float(certificate['area_element_lower']))
    area=area_raw*ref.exact_length
    if area<=0:raise ValueError('No positive reference area lower bound')
    previous=None
    for row in source_rows:
        left,right=Q(row['left_exact']),Q(row['right_exact'])
        if not left<right or (previous is not None and left!=previous):
            raise ValueError('Difference cells are not a contiguous exact partition')
        previous=right
    complete=(data['complete_prefix_domain'] and Q(source_rows[0]['left_exact'])==0
              and Q(source_rows[-1]['right_exact'])==1)
    names={(1,0):'x',(0,1):'psi',(2,0):'xx',(1,1):'xpsi',(0,2):'psipsi'}
    maximum=dict(epsilon=0.,eta=0.,beta=0.)
    locations={};rows=[];minimum_gram=float('inf')
    for first in range(0,len(source_rows),args.batch):
        chunk=source_rows[first:first+args.batch]
        intervals=[(Q(r['left_exact']),Q(r['right_exact'])) for r in chunk]
        spans=[r['reference_span'] for r in chunk]
        power=[diff.raw_power_batch(ref,spans,intervals,d) for d in range(3)]
        reference_bounds={name:diff.batch_norm_bounds(power[d],ref.M,angle)
            for (d,angle),name in names.items()}
        for local,source in enumerate(chunk):
            u={k:v['vector'] for k,v in source['jets'].items()}
            old={name:reference_bounds[name][local]['vector'] for name in names.values()}
            trace=I(old['x']).square()+I(old['psi']).square()
            m=float((qb(area*area)/trace).lo)
            if not m>0:raise ValueError('Unresolved positive old Gram lower bound')
            eta=float(((I(u['x']).square()+I(u['psi']).square())/I(m)).sqrt().hi)
            C_u=positive_tensor_bound(u['xx'],u['xpsi'],u['psipsi'])
            C_X=positive_tensor_bound(old['xx'],old['xpsi'],old['psipsi'])
            beta=float(((C_u+I(eta)*C_X)/I(m)).hi)
            result=dict(cell=source['cell'],subdivision=source['subdivision'],
                left_exact=source['left_exact'],right_exact=source['right_exact'],
                epsilon=u['position'],eta=eta,beta=beta,
                reference_gram_eigenvalue_lower=m,
                reference_jet_upper=old,coordinate_u_second_tensor_upper=float(C_u.hi),
                coordinate_X_second_tensor_upper=float(C_X.hi))
            for name in maximum:
                if result[name]>maximum[name]:
                    maximum[name]=result[name]
                    locations[name]={k:result[k] for k in ('cell','subdivision','left_exact','right_exact')}
            minimum_gram=min(minimum_gram,m)
            if args.rows is not None:rows.append(result)
    report=dict(schema='fd2d-prefix-old-induced-tensor-difference-v1',
        status='PREFIX_ONLY__UNVERIFIED_GLOBALLY',scope=__doc__,script=diff.identity(__file__),
        coordinate_source=diff.identity(HERE/'fd2d-metric-prefix-c2-difference.py'),
        difference_report=diff.identity(args.difference),
        reference_certificate=diff.identity(args.reference_certificate),
        reference=data['reference'],candidate=data['candidate'],reference_bindings=bindings,
        area_raw_lower_exact=str(area_raw),normalized_area_lower_exact=str(area),
        area_certificate_coordinate='original saved radial coordinate and psi; normalized area multiplied by S_ref exactly',
        complete_prefix_domain=bool(complete),radial_cells_checked=len(source_rows),
        old_metric='h=X*e for the actual reference geometry',
        formulas=dict(gram_minimum='m=area_lower^2/(|X_x|_upper^2+|X_psi|_upper^2)',
            gradient='eta <= sqrt(U_x^2+U_psi^2)/sqrt(m)',
            second='beta <= (C_u+eta*C_X)/m',
            tensor_majorant='C_V=lambda_max([[|V_xx|,|V_xpsi|],[|V_xpsi|,|V_psipsi|]])',
            old_connection='dX(Gamma(v,v))=projection_to_tangent(D_coordinate^2 X(v,v)); its norm is <= C_X/m for h-unit v'),
        maxima=maximum,maximum_locations=locations,minimum_old_gram_eigenvalue_lower=minimum_gram,
        budgets=dict(epsilon=1e-4,eta=1e-3,beta=.1),
        each_prefix_budget_met=dict(epsilon=maximum['epsilon']<=1e-4,
            eta=maximum['eta']<=1e-3,beta=maximum['beta']<=.1),
        comparison_is_global_C2_verified=False,tail_covered=False,caps_covered=False,
        whole_surface_transfer=False,new_metric_certificate=False,
        ODE_calls=0,solver_calls=0,seconds=time.monotonic()-start)
    if args.rows is not None:
        if args.rows.suffix!='.gz':raise ValueError('Use gzip for row data')
        packed=gzip.compress((json.dumps(rows,separators=(',',':'),allow_nan=False)+'\n').encode(),mtime=0)
        if len(packed)>=5_000_000:raise ValueError('Row data exceed repository file limit')
        args.rows.write_bytes(packed);report['row_data']=diff.identity(args.rows)
    args.out.write_text(json.dumps(report,indent=2,sort_keys=True,allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(args.out),maxima=maximum,
        prefix_budgets_met=report['each_prefix_budget_met'],complete_prefix_domain=complete,
        global_transfer=False,seconds=report['seconds']),sort_keys=True))


if __name__=='__main__':main()
