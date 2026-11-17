#!/usr/bin/env python3
"""Read actual fixed-material chords and the major-meridian curvature gate.

The proposed circle height is conditional reference data.  Sampled chord
maxima are not interval certificates.  The curvature gate assumes the
reflection major meridian remains an outward projected graph and joins a
horizontal circular cuff; it does not exclude other geometric charts.
"""
import argparse,hashlib,json
from pathlib import Path
import numpy as np
from parallel_20261117_frenet_symbol import Frenet


def sha(raw):return hashlib.sha256(raw).hexdigest()


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for k in ['trace','reference-report','out']:p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--angles',type=int,default=16384);p.add_argument('--actual-curvature-limit',type=float,default=6.5)
    a=p.parse_args();raw=a.trace.read_bytes();tr=json.loads(raw);rr=a.reference_report.read_bytes();ref=json.loads(rr)
    if ref['physical_trace_sha256']!=sha(raw):raise ValueError('Reference profile has another cut trace')
    d=ref['diagnostics'][-1];R=ref['parameters']['cuff_radius'];H=d['conditional_cuff_height'];L=d['total_reference_length']
    q=Frenet(tr['M'],a.angles);phi=q.angle;F,_,_=q.jet(np.array(tr['frenet_state']))
    V,_,_=q.jet(np.array(tr['frenet_r_state']));V*=tr['a_prime']
    freq=2*np.arange(1,len(tr['rho_cos_coefficients'])+1)
    theta=phi+np.sin(phi[:,None]*freq)@(np.array(tr['rho_cos_coefficients'])/freq)
    xy=(F[:,0]+1j*F[:,1])*np.exp(1j*phi)
    chord=np.sqrt(abs(R*np.exp(1j*theta)-xy)**2+(H-F[:,2])**2)
    nearest=np.hypot(R-abs(xy),H-F[:,2]);j=int(np.argmax(chord))
    speed=float(np.linalg.norm(V[0]));vertical=float(V[0,2]/speed);Rmin=float(F[0,0]+vertical/a.actual_curvature_limit)
    report=dict(scope=__doc__,source_sha256=sha(Path(__file__).read_bytes()),physical_trace_sha256=sha(raw),
                reference_report_sha256=sha(rr),background_sha256=ref['background_sha256'],angles=a.angles,
                cuff_radius=R,conditional_reference_cuff_height=H,reference_length=L,
                sampled_max_fixed_material_chord=float(chord[j]),sampled_fixed_material_chord_slack=float(L-chord[j]),
                worst_phi=float(phi[j]),worst_material_theta=float(theta[j]),
                sampled_max_nearest_circle_chord=float(np.max(nearest)),
                maximum_pointwise_fixed_label_extra_distance=float(np.max(chord-nearest)),
                major_x=float(F[0,0]),major_tangent=V[0].tolist(),major_speed=speed,major_unit_vertical_tangent=vertical,
                actual_curvature_limit=a.actual_curvature_limit,necessary_cuff_radius_major=Rmin,
                major_curvature_radius_slack=R-Rmin,nonlinear_success=False)
    out=(json.dumps(report)+'\n').encode();a.out.write_bytes(out);print(json.dumps(report));print(json.dumps(dict(output_sha256=sha(out))))
