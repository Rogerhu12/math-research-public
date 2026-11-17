#!/usr/bin/env python3
"""Separate finite angular projection error from sampled aliasing at true nodes.

This evaluates the stored accepted state and its stored derivative without
re-solving or repairing them. It reports a necessary local source of actual
Gram error; it is not a new field, continuum bound, or refinement result.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np
from parallel_20261117_frenet_symbol import Frenet
from parallel_20261117_profile import Profile
from parallel_20261117_inward_profile import InwardProfile


def probe(path,angles):
    raw=path.read_bytes();data=json.loads(gzip.decompress(raw))
    if not data.get('success'):raise ValueError('Only accepted states are compared')
    if data.get('radial_growth_scale',1)!=1:raise ValueError('Unsupported scalar growth')
    geometry=data['fixed_scalar_profile']['geometry'];origin=data['analytic_extension_origin']
    spec=data.get('inward_scalar_profile')
    profile=(InwardProfile(geometry,origin,spec['cut'],spec['curvature'],spec['ramp_in'],
        spec['ramp_out'],spec['quadrature']) if spec else Profile(geometry,origin))
    q=Frenet(data['M'],angles);s=data['mesh'][-1];a,ap,_=profile(s)
    y=np.array(data['states'][-1]);dy=np.array(data['rhs'][-1])
    z=q.local(y,ap/a);V=z['V'];Vp=q.jet(dy)[0];delta=Vp-V;d=z['d']
    frequency=np.arange(q.N//2+1)
    dd=np.fft.irfft(np.fft.rfft(delta,axis=0)*(1j*frequency[:,None]),n=q.N,axis=0)
    dd[:,0]-=delta[:,1];dd[:,1]+=delta[:,0]
    core=np.array(data['core']['coefficients'])
    rho=1+np.cos(q.angle[:,None]*q.freq[None,1:])@((1-q.freq[1:]**2)*core)
    angular_target=(a*rho)**2
    rr=np.sum(Vp*Vp,axis=1)-1;mixed=np.sum(d*Vp,axis=1)/np.sqrt(angular_target)
    angular=z['Q']/angular_target-1
    eigen=(abs(rr+angular)+np.sqrt((rr-angular)**2+4*mixed*mixed))/2
    local_angular_defect=2*np.sum(d*dd,axis=1)/angular_target
    projection_high=q.project(V)
    coeff_delta=projection_high-dy
    projected_high=q.jet(projection_high)[0]
    spectrum=2*np.fft.rfft(V,axis=0)/q.N
    outside=np.arange(q.N//2+1)>2*q.M
    return dict(input_name=path.name,input_sha256=hashlib.sha256(raw).hexdigest(),
        M=q.M,solve_angles=data['N'],evaluation_angles=q.N,s=s,
        angular_gram_max=float(max(abs(angular))),radial_gram_max=float(max(abs(rr))),
        mixed_gram_max=float(max(abs(mixed))),gram_operator_max=float(max(eigen)),
        unprojected_speed_error=float(max(abs(np.sum(V*V,axis=1)-1))),
        unprojected_orthogonality_error=float(max(abs(np.sum(d*V,axis=1)))),
        stored_velocity_projection_error_max=float(max(np.linalg.norm(delta,axis=1))),
        projection_tail_max=float(max(np.linalg.norm(projected_high-V,axis=1))),
        increased_quadrature_coefficient_difference_max=float(max(abs(coeff_delta))),
        increased_quadrature_velocity_difference_max=float(max(np.linalg.norm(projected_high-Vp,axis=1))),
        unresolved_angular_metric_derivative_max=float(max(abs(local_angular_defect))),
        omitted_velocity_spectral_coefficient_max=float(np.max(abs(spectrum[outside]))))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--inputs',nargs='+',type=Path,required=True)
    p.add_argument('--angles',type=int,default=8192);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();result=dict(scope=__doc__,rows=[probe(f,a.angles) for f in a.inputs],
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    raw=(json.dumps(result,indent=2)+'\n').encode();a.out.write_bytes(raw)
    print(json.dumps(result,indent=2));print('report_sha256',hashlib.sha256(raw).hexdigest())
