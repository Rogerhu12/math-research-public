#!/usr/bin/env python3
"""R89: actual physical-angle compressed positive-body energy constants.

All geometric numbers are reaggregated from the same complete R69 cell
reports.  No high/low commutator or boundary source is discarded.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_closed_approximate_exterior import read,standardized,digest,lo,hi,check_cover


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--closed',type=Path,default=Path('notes/2026-11-12-actual-closed-approximate-exterior.json'))
    ap.add_argument('--robin',type=Path,default=Path('notes/2026-11-12-actual-exterior-robin-certificate.json'))
    ap.add_argument('--common',type=Path,default=Path('notes/2026-11-12-common-core-exterior-parameter-interval.json'))
    ap.add_argument('--bits',type=int,default=256)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits
    closed,robin,common=map(read,(args.closed,args.robin,args.common))
    if not closed.get('complete') or not robin.get('complete'):
        raise ValueError('whole actual exterior and true Robin must already be complete')
    if digest(args.closed) not in robin['input_sha256'].values():
        raise ValueError('true tail does not belong to this completed body')
    box=list(map(Fraction,common['chosen_closed_interval']))
    for report in (closed,robin):
        a,b=map(Fraction,report['exact_parameter_interval'])
        if not a<=box[0]<=box[1]<=b:
            raise ValueError('common actual parameter box exceeds a proved exterior')
    roots=list(map(Fraction,closed['actual_moving_root_interval']))
    loaded={}
    for path,expected in closed['input_sha256'].items():
        if digest(path)!=expected:
            raise ValueError('completed body input changed: '+path)
        loaded[path]=read(path)
    rows=[];coverage=[]
    for path,report in loaded.items():
        if 'positive-family-root-collar' in path or 'positive-family-outer-' in path:
            if not report.get('complete'):
                raise ValueError('incomplete actual collar/body cell list')
            for cell in report['cells']:
                row=standardized(cell,roots)
                row['source_path']=path
                rows.append(row)
        elif 'positive-family-natural-graft' in path:
            if not report.get('complete'):
                raise ValueError('incomplete actual graft')
            for cell in report['rows']:
                row=standardized(cell,roots,True)
                row['source_path']=path
                rows.append(row)
    check_cover([{'radial_interval':[str(r['left']),str(r['right'])]} for r in rows],roots[0],Fraction(25,8))
    if len(rows)!=closed['collar_cells']+closed['regular_body_cells']+closed['graft_cells']:
        raise ValueError('the exact positive cell count changed')
    m0=min(min(r['al'],(r['el']*r['klo']).lower()) for r in rows).lower()
    Q=max(r['vr'] for r in rows).upper()
    L=exact_arb(Fraction(25,8)-roots[1]).lower()
    if not m0>0 or not L>0:
        raise ValueError('nonpositive actual physical form input')
    fee=(arb(3)*Q*Q/2).upper()
    def one(N):
        lam=arb(4*(N+1))
        power=(lam.log()*arb(4)/3).exp()
        kappa=(m0*(power-fee)/3).lower()
        length_gate=lam**(-arb(2)/3)<=L/2
        valid=bool(length_gate and kappa>0)
        result=dict(N=N,first_retained_physical_frequency=4*(N+1),
                    finite_interval_length_gate=bool(length_gate),
                    compressed_L2_coercivity=ball_record(kappa),proved_positive=valid)
        if valid:
            result.update(L2_source_to_L2_inverse=ball_record((1/kappa).upper()),
                          L2_source_to_energy_inverse=ball_record((1/kappa.sqrt()).upper()))
        return result
    threshold=0
    while not one(threshold)['proved_positive']:
        threshold+=1
        if threshold>10000000:
            raise ValueError('actual high threshold exceeds the intended finite search')
    tests=sorted(set([0,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,threshold]))
    minrow=min(rows,key=lambda r:min(r['al'],(r['el']*r['klo']).lower()))
    maxrow=max(rows,key=lambda r:r['vr'])
    report=dict(kind='actual_physical_fourier_high_positive_body_coercivity',proved=True,
      source_sha256=digest(__file__),bits=args.bits,
      dependencies={name:digest(Path(__file__).parent/name) for name in (
        'fourfold_phase_closed_approximate_exterior.py','fourfold_phase_beta_bulk_interval.py',
        'fourfold_phase_beta_interval.py')},
      input_sha256={str(p):digest(p) for p in (args.closed,args.robin,args.common)},
      exact_source_cell_hashes=closed['input_sha256'],
      origin_inputs_sha256=closed['origin_inputs_sha256'],direction_sha256=closed['direction_sha256'],
      exact_parameter_interval=list(map(str,box)),actual_cells=len(rows),
      exact_positive_cover=[str(roots[0]),'25/8'],
      physical_density_measure='dr dtheta; x=r-t(delta); no shear/Jacobian normalization',
      physical_normal_coefficient_lower=ball_record(m0),
      physical_drift_theta_upper=ball_record(Q),
      length_lower=ball_record(L),half_density_transport_mass_fee=ball_record(fee),
      first_sufficient_N=threshold,cutoff_table=[one(n) for n in tests],
      extremal_cells={name:dict(path=r['source_path'],exact_radial_interval=[str(r['left']),str(r['right'])])
                     for name,r in [('physical_minimum',minrow),('maximum_drift_theta',maxrow)]},
      formula='kappa_N = m0/3 * ((4*(N+1))^(4/3) - 3*Q^2/2)',
      scope=['Actual physical-angle high subspace at every radial point; P_N need not commute with q.',
             'True nonnegative full-tail Robin is included; the finite interval length condition is checked.',
             'The same coercivity holds with homogeneous root Dirichlet constraint or on the natural form domain.',
             'Both regular mean trace and mean flux remain in the complementary low system.',
             'This is a compressed volume inverse, not a full cap DN or Airy reflection estimate.',
             'Only residuals genuinely represented by L2 volume functions use the displayed inverse fee; boundary residuals require their actual trace fees.'])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('actual_cells','physical_normal_coefficient_lower',
          'physical_drift_theta_upper','first_sufficient_N','cutoff_table')},indent=2),flush=True)


if __name__=='__main__':
    main()
