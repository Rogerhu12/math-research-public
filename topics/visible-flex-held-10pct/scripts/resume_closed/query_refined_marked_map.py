#!/usr/bin/env python3
"""Query the actual refined closed map, including nonzero fixed cap interiors.

The same existing ClosedM3Map supplies every chart and the marker.  This
finite query report supplements, and does not replace, the R28 analytic
common-jet, geometry and noncongruence proof.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'finite_closure/m3_m8_closed_map'))
import argparse
import hashlib
import json
import math
import numpy as np
from closed_m3_map import ClosedM3Map

parser=argparse.ArgumentParser(description=__doc__)
for key in ['source-topic','short-bridge','prefix-checkpoint','tail-checkpoint','port',
            'tail-manifest','tail-reader','cap-source','out']:
    parser.add_argument('--'+key,type=Path,required=True)
args=parser.parse_args()
model=ClosedM3Map(args.source_topic,args.short_bridge,args.prefix_checkpoint,args.tail_checkpoint,
                  args.port,args.tail_manifest,args.tail_reader,args.cap_source,marker_strength=.5)
phases=[0.,math.pi/6,math.pi/3]
seam_max=np.zeros(6)
fixed_max=0.
marker_rows=[]
try:
    assert model.record['config']['modes']==16
    assert model.marker_radius==model.a/2 and model.marker_strength==model.marker_eta==.5
    for phase in phases:
        for side in [-1,1]:
            for theta in np.linspace(0,2*math.pi,12,endpoint=False):
                P=model.prefix_jets(side*model.end,theta,phase)
                T=model.tail_jets(model.Rcut,theta,side,phase)
                ap,app=model.target.ap,model.target.app
                common=[T[0],T[1]*side*ap,T[2]*ap*ap+T[1]*app,T[3],T[4],T[5]*side*ap]
                seam_max=np.maximum(seam_max,[np.linalg.norm(p-t)for p,t in zip(P,common)])
            for radius in [0.,model.a/4,model.a/2,model.a]:
                for theta in [0.,math.pi/2]:
                    J=model.tail_jets(radius,theta,side,phase)
                    J0=model.tail_jets(radius,theta,side,0.)
                    fixed_max=max(fixed_max,max(float(np.linalg.norm(p-q))for p,q in zip(J,J0)))
                    assert all(np.all(np.isfinite(p))for p in J)
    for x,y in [(0.,0.),(model.a/4,0.),(0.,model.a/4),(model.a/2,0.)]:
        value,gradient,Hessian=model.marker(x,y)
        X,DX,D2X=model.disk_jets(x,y,1)
        marker_rows.append(dict(x=x,y=y,value=float(value),gradient_norm=float(np.linalg.norm(gradient)),
                                hessian_norm=float(np.linalg.norm(Hessian,2)),point=np.asarray(X,float).tolist()))
    assert marker_rows[1]['value']>0 and marker_rows[2]['value']>0
    assert marker_rows[1]['value']>marker_rows[2]['value']
    assert marker_rows[3]['value']==marker_rows[3]['gradient_norm']==marker_rows[3]['hessian_norm']==0
    assert fixed_max==0
    sha=lambda path:hashlib.sha256(path.read_bytes()).hexdigest()
    record=dict(scope=__doc__,command=sys.argv,source_sha256=sha(Path(__file__)),
                map_source_sha256=sha(Path(sys.modules['closed_m3_map'].__file__)),
                inputs={str(p.resolve()):sha(p)for p in [args.prefix_checkpoint,args.tail_checkpoint,
                    args.port,args.tail_manifest,args.tail_reader,args.cap_source]},
                actual_q=model.record['actual_primary_amplitude'],modes=16,phases=phases,
                shared_cut_six_jet_numeric_max=np.asarray(seam_max,float).tolist(),
                cap_six_jet_phase_difference_numeric_max=fixed_max,
                marker_strength=model.marker_strength,marker_eta=model.marker_eta,
                marker_radius=model.marker_radius,marker_queries=marker_rows,
                numerical_background=model.background.info,
                mathematical_background='The exact integral definition and R27 bounds, not this numerical primitive.',
                continuous_geometry_and_noncongruence='Separate R28 proof and scalar/interval records.',
                exact_isometry_claimed=False)
    args.out.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({key:record[key]for key in ['actual_q','shared_cut_six_jet_numeric_max',
          'cap_six_jet_phase_difference_numeric_max','marker_radius','marker_queries']}))
finally:
    model.close()
