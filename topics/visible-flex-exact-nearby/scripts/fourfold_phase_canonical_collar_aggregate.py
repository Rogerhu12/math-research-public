#!/usr/bin/env python3
"""Reaggregate the complete actual finite-collar coefficient cover."""
from __future__ import annotations
import argparse,gzip,hashlib,json
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_interval import ball_record


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def low(s):return arb(s).lower()
def high(s):return arb(s).upper()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input',type=Path,default=Path('notes/2026-11-12-actual-finite-canonical-collar-centered-cover.json.gz'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=256
    with gzip.open(args.input,'rt') as f:d=json.load(f)
    if not d.get('proved') or d['failed_cells'] or d['pending']:
        raise ValueError('whole actual finite collar has not completed')
    config=d['configuration'];here=Path(__file__).parent
    for key,name in [('source_sha256','fourfold_phase_canonical_collar_centered_cover.py'),
       ('engine_source_sha256','fourfold_phase_canonical_collar_finite.py'),
       ('phase_centered_engine_source_sha256','fourfold_phase_canonical_collar_centered.py'),
       ('phase_taylor_source_sha256','fourfold_phase_root_potential_complex_strip.py')]:
        if config[key]!=sha(here/name):raise ValueError('actual engine source changed: '+name)
    for name,value in config['dependencies'].items():
        if sha(here/name)!=value:raise ValueError('coefficient dependency changed: '+name)
    if config['first_cell']!=0 or config['last_cell']*2!=config['initial_angle_cells']:
        raise ValueError('specified angular cover is not a half quarter')
    height=Fraction(config['exact_collar_height']);R=config['radial_cells']
    for k in range(R):
        interval=[str(height*k/R),str(height*(k+1)/R)]
        rows=sorted([r for r in d['cells'] if r['exact_positive_radial_interval']==interval],
                    key=lambda r:Fraction(r['exact_quarter_interval'][0]))
        cursor=Fraction(0)
        for row in rows:
            a,b=map(Fraction,row['exact_quarter_interval'])
            if a!=cursor or not b>a:raise ValueError('angular coverage gap or overlap')
            cursor=b
        if cursor!=Fraction(1,2):raise ValueError('incomplete half quarter')
    positive={}
    for name in d['cells'][0]['positive_chart_coefficients']:
        lo=min(low(r['positive_chart_coefficients'][name]['lower']) for r in d['cells'])
        hi=max(high(r['positive_chart_coefficients'][name]['upper']) for r in d['cells'])
        if not 0<lo<=hi or not hi.is_finite():raise ValueError('nonfinite/nonpositive chart bound')
        positive[name]={'lower':ball_record(lo),'upper':ball_record(hi)}
    aggregates={}
    for category in ['derivative_sup_for_root_division','ordinary_physical_theta_derivatives',
                     'root_potential_physical_theta_derivatives']:
        result={}
        for name,columns in d['cells'][0][category].items():
            values=[]
            for j in range(len(columns)):
                v=max(high(r[category][name][j]) for r in d['cells'])
                if not v.is_finite() or not v>=0:raise ValueError('nonfinite actual derivative bound')
                values.append(ball_record(v))
            result[name]=values
        aggregates[category]=result
    report=dict(kind='actual_complete_finite_collar_aggregate',proved=True,source_sha256=sha(__file__),
      input_sha256={str(args.input):sha(args.input)},configuration=config,
      actual_cells=len(d['cells']),attempts=d['attempts'],exact_collar_height=str(height),
      exact_half_quarter_cover=['0','1/2'],root_division_orders=d['root_division_orders'],
      positive_chart_coefficients=positive,**aggregates,
      scope=['Every recorded derivative bound was checked finite and nonnegative.',
             'The actual radial and angular intervals tile exactly; D4/root reflection supplies the stated full domain.',
             'These complete coefficient bounds are not yet an Airy source operator norm or full feedback cutoff.'])
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'proved':True,'actual_cells':len(d['cells']),'attempts':d['attempts'],
                      'report_sha256':sha(args.out)},indent=2))


if __name__=='__main__':main()
