#!/usr/bin/env python3
"""Evaluate four predeclared circle-trace combinations, without a BVP.

Every combination is formed before taking a maximum.  These finite maxima
are not continuous upper bounds or a production positivity guard.  The two
single-column rows are included only to expose the actual cancellation in
SA-SB and reinforcement in SA+SB, not to replace their combined evaluation.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import hashlib
import json
from pathlib import Path
import sys
import numpy as np
from circle_trace_controls import CircleTraceControls


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--halfwidth',type=float,default=.21)
    parser.add_argument('--transition',type=float,default=.4)
    parser.add_argument('--angular',type=int,default=12288)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    basis=CircleTraceControls(args.halfwidth,args.transition,80)
    phi=2*np.pi*np.arange(args.angular)/args.angular
    arc=basis.center+np.linspace(-basis.a,basis.a,257)
    jets=basis.support_jets(phi,4)
    arcjets=basis.support_jets(arc,4)
    rows=[]
    for name,coefficient in [('SA',[1.,0.]),('SB',[0.,1.]),
                             ('SA-SB',[1.,-1.]),('SA+SB',[1.,1.])]:
        c=np.asarray(coefficient)
        combined=[c@jet for jet in jets]
        rho=[combined[k]+combined[k+2] for k in range(3)]
        combined_arc=[c@jet for jet in arcjets]
        position=basis.position_increment(phi,c)
        center=basis.position_increment(np.array([basis.center]),c)[0]
        rho0=rho[0]
        peak=int(np.argmax(abs(rho0)))
        rows.append(dict(name=name,coefficient=coefficient,
            finite_support_jet_absmax=[float(np.max(abs(v))) for v in combined],
            finite_rho_jet_absmax=[float(np.max(abs(v))) for v in rho],
            finite_rho_range=[float(np.min(rho0)),float(np.max(rho0))],
            finite_rho_peak_normal_angle=float(phi[peak]),
            finite_position_norm_max=float(np.max(np.linalg.norm(position,axis=1))),
            arc_support_value_range=[float(np.min(combined_arc[0])),float(np.max(combined_arc[0]))],
            arc_radius_trace_error=float(np.max(abs(combined_arc[0]+combined_arc[2]-c[0]))),
            arc_center_point_increment=center.tolist(),
            arc_center_point_increment_error=float(np.max(abs(center-(c[0]+c[1])*
                np.array([np.cos(basis.center),np.sin(basis.center)])))),
            exact_trace_parameters=dict(radius_increment=c[0],
                actual_circle_center_along_nu0=c[1],
                project_negative_center_scalar_increment=-c[1],
                midpoint_position_along_nu0=c[0]+c[1])))
    output=dict(scope=__doc__,command=sys.argv,definition=basis.summary(),
        source_sha256={str(Path(__file__).resolve()):sha(__file__),
            str(Path(__file__).with_name('circle_trace_controls.py').resolve()):
                sha(Path(__file__).with_name('circle_trace_controls.py'))},
        full_circle_nodes=args.angular,arc_nodes=len(arc),rows=rows,
        boundary='The controls are combined before evaluating every jet and maximum. '
            'No actual core, profile, g, solver, H, or acceptance gate was modified. '
            'No sampled maximum is used as a whole-interval derivative bound.')
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),sha256=sha(args.out),
        rho_jet_absmax={row['name']:row['finite_rho_jet_absmax'] for row in rows})),flush=True)


if __name__=='__main__':main()
