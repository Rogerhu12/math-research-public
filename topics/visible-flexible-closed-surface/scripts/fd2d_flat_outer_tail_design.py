#!/usr/bin/env python3
"""New physical tail: replace the outer finite valley by a conical buffer.

The immutable factory already supports this exact C2 log blending. All
finite constants are kept as explicit data; no old cell calibration is
claimed for the new geometry. Its bounded line and full nonlinear DN must
be recomputed.
"""
import argparse,json,hashlib
from pathlib import Path

def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('source',type=Path);p.add_argument('out',type=Path)
    p.add_argument('--through-cell',type=int,default=0)
    p.add_argument('--start-segment',type=int,default=2)
    p.add_argument('--slope',type=float,default=.1)
    a=p.parse_args()
    if a.out.exists():raise RuntimeError('Unused output required')
    if a.through_cell<0 or a.start_segment not in range(9) or not 0<a.slope<1:raise ValueError('Invalid finite buffer')
    d=json.loads(a.source.read_text())
    d['historical_calibration_only']=d.pop('design_calibration',None)
    d.update(flatOuterThroughCell=a.through_cell,flatOuterStartSegment=a.start_segment,flatSlope=a.slope,
        calibration_status='New physical g. Old beta entries are definition constants only; no cell T21 calibration is imposed or inherited.')
    d['flat_buffer_design']=dict(source_file=a.source.name,source_sha256=digest(a.source),
        source_generator=Path(__file__).name,generator_sha256=digest(__file__),
        changed_finite_cells=list(range(a.through_cell+1)),unchanged_infinite_source_from_cell=160,
        rationale='A constant w interval has Hrr=0 in the exact m2 equation; move the sensitive outer valley to a smooth conical buffer.',
        old_linear_port_reusable=False,nonlinear_solution=False,continuous_geometry_certificate=False)
    a.out.write_text(json.dumps(d,indent=2)+'\n')
    print(json.dumps(dict(output=str(a.out),sha256=digest(a.out))))

if __name__=='__main__':main()
