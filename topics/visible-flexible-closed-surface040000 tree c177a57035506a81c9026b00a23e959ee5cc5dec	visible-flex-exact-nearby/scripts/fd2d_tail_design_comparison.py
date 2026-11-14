#!/usr/bin/env python3
"""Compare closed actual full-tail trajectories in physical height units."""
import argparse,gzip,hashlib,json
from pathlib import Path

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def read_report(path):
    r=json.loads(path.read_text())
    if not r['completed']:raise ValueError('Closed actual report required')
    trajectory=path.parent/r['trajectory']['file']
    if sha(trajectory)!=r['trajectory']['sha256']:raise ValueError('Trajectory binding mismatch')
    peaks={};cells={};count=0
    for line in gzip.open(trajectory,'rt'):
        q=json.loads(line);q['Gamma']=q['L']-4*q['H']*q['w']/q['r']
        for key in ('Gamma','L','linear_shape_operator_row_bound','H','Hr'):
            if key not in peaks or abs(q[key])>abs(peaks[key][key]):peaks[key]=q.copy()
        if q['cell']<8:
            n=str(q['cell'])
            if n not in cells or q['linear_shape_operator_row_bound']>cells[n]['linear_shape_operator_row_bound']:cells[n]=q.copy()
        count+=1
    return dict(report_file=path.name,report_sha256=sha(path),config_file=r['config_file'],config_sha256=r['config_sha256'],
        far=r['far'],steps=r['steps'],samples=count,stats={k:v for k,v in r['stats'].items() if k!='positiveWarpWeights'},
        actual_D2=r['linear_slopes']['2'],ideal_D2=4/r['stats']['rCut'],D2_minus_ideal=r['linear_slopes']['2']-4/r['stats']['rCut'],
        maximum_background_curvature=r['maximum_sampled_background_curvature'],maxima=peaks,
        first_eight_cell_physical_peaks=cells,trajectory_sha256=r['trajectory']['sha256'],
        scope='Full saved finite trajectories. Physical II and Gamma use real Hcut=1. This is not a continuous or nonlinear certificate.')

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('out',type=Path);p.add_argument('reports',nargs='+',type=Path);a=p.parse_args()
    if a.out.exists():raise RuntimeError('Unused comparison output required')
    rows=[read_report(q) for q in a.reports]
    d=dict(schema='fd2d-actual-tail-design-physical-comparison-v1',source_sha256=sha(__file__),rows=rows)
    a.out.write_text(json.dumps(d,indent=2)+'\n')
    print(json.dumps([dict(config=r['config_file'],rcut=r['stats']['rCut'],D2=r['actual_D2'],
        row_bound=r['maxima']['linear_shape_operator_row_bound']['linear_shape_operator_row_bound'],
        Gamma=abs(r['maxima']['Gamma']['Gamma'])) for r in rows]))

if __name__=='__main__':main()
