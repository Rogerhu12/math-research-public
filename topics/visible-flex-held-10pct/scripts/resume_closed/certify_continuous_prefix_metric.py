#!/usr/bin/env python3
"""Continuous full-angle metric of the unchanged actual M16 Cartesian prefix.

Complete polynomial/Laurent multiplication handles the finite Cartesian
part.  Validated true-integral profile enclosures transfer an auxiliary
radius quintic to the one fixed physical metric.  The unchanged analytic
center and full Cartesian cut lifts are then paid by first-jet inequalities.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
from fractions import Fraction as Q
from pathlib import Path
import argparse,gzip,hashlib,json,math,sys,time
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'finite_closure/m3_m8_closed_map'))
from m3_shared_prefix import load_prefix
from interval_prefix_metric import quintic_powers,prefix_numerators,polynomial_l1_range,pderivative
from prefix_true_profile import TruePrefix,float_bound


def qq(x):return Q.from_float(float(x))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def display(x):return dict(numerator=str(x.numerator),denominator=str(x.denominator),display_only=float(x))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('data','checkpoint','source-topic','short-bridge','port','tail-manifest',
              'prefix-audit','cut-bounds','center-certificate','out'):
        p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--threshold',default='1e-6')
    a=p.parse_args();started=time.monotonic()
    x=np.load(a.data);cp=json.load(gzip.open(a.checkpoint,'rt'))
    audit=json.loads(a.prefix_audit.read_text());cut_bounds=json.loads(a.cut_bounds.read_text())
    manifest=json.loads(a.tail_manifest.read_text())
    r,obj,flow,sol,raw=load_prefix(a.source_topic,a.short_bridge,a.checkpoint,a.port,512)
    assert r['frozen_profile']==cp['frozen_profile'] and float(x['knots'][-1])==flow.end
    assert np.array_equal(x['knots'],x['phase_knots'])
    radius_jets=np.stack(flow.profile(x['knots']))[:,None,:]
    true=TruePrefix(cp['frozen_profile'],dict(radius=manifest['parameters']['rCut'],
        backgroundSlope=manifest['parameters']['wCut']),float(x['knots'][-1]),cut_width=audit['cut_width'])
    assert [true.atlas_first,true.atlas_second]==audit['target_cut_jets'][1:]
    lamlo,lamhi=map(qq,float_bound(true.coordinate_scale))
    rcut=qq(manifest['parameters']['rCut']);rho=Q(8399,10000)
    rows=[];max_raw=Q(0);max_aux=0.;max_eprime=0.;max_phase=0.
    max_numerator=[0.,0.,0.];max_frequency=0;max_degree=0
    for i in range(len(x['knots'])-1):
        sl=slice(i,i+2);knots=x['knots'][sl]
        lo,hi=map(float,knots);h=qq(hi)-qq(lo)
        C=quintic_powers(knots,x['jets'][:,:,sl]);E=quintic_powers(knots,x['phase_jets'][:,:,sl])
        R=quintic_powers(knots,radius_jets[:,:,sl])
        C=tuple(v[:,:,0]for v in C);E=tuple(v[:,:,0]for v in E);R=tuple(v[:,:,0]for v in R)
        phase=polynomial_l1_range(E)
        assert qq(phase)<1-rho
        eprime=polynomial_l1_range(pderivative(E,h))
        nums,info=prefix_numerators(C,E,R,h,x['planar_modes'],x['height_modes'])
        n=[polynomial_l1_range(v)for v in nums]
        auxiliary=true.auxiliary_error(lo,hi,radius_jets[:,0,sl])
        epsilon=qq(auxiliary['upper']);rmin=rcut-epsilon
        assert rmin>0 and epsilon<rcut
        A,B,Cc=map(qq,n)
        eta=max(A+B/rmin,Cc/rmin**2+B/rmin)/rho**2
        tmax=max(1/lamlo**2,(1+epsilon/rcut)**2)
        tdev=max(abs(1/lamlo**2-1),abs(1/lamhi**2-1),
            abs((1+epsilon/rcut)**2-1),abs((1-epsilon/rcut)**2-1))
        raw_metric=tmax*eta+tdev
        rows.append(dict(span=i,radial=[lo,hi],numerator_l1_upper=n,
            auxiliary_radius_error=auxiliary,raw_true_metric=display(raw_metric),phase_abs_upper=phase,eprime_abs_upper=eprime))
        max_raw=max(max_raw,raw_metric);max_aux=max(max_aux,auxiliary['upper'])
        max_eprime=max(max_eprime,eprime);max_phase=max(max_phase,phase)
        max_numerator=[max(v,w)for v,w in zip(max_numerator,n)]
        max_frequency=max(max_frequency,info['maximum_angular_frequency'])
        max_degree=max(max_degree,info['maximum_radial_degree'])
        if i%64==0:
            print(json.dumps(dict(event='continuous_prefix_metric',done=i+1,total=len(x['knots'])-1,
                raw_metric_upper=float(max_raw),auxiliary_radius_error=max_aux,seconds=time.monotonic()-started)),flush=True)
    center=json.loads(a.center_certificate.read_text())
    assert center['input_sha256']==sha(a.data) and center['full_circle']
    delta=[[qq(v)for v in row]for row in center['uniform_delta_norm_angular_then_radial']]
    width=qq(audit['center_width'])
    weights0=[Q(1),Q(2,5)*width,Q(1,20)*width**2]
    weights1=[5/width,Q(2),width/4]
    center_s=sum((v*w for v,w in zip(weights1,delta[0])),Q(0))
    center_psi=sum((v*w for v,w in zip(weights0,delta[1])),Q(0))
    cut=cut_bounds['correction_bounds_radial_then_angular_derivative']
    cut_s,cut_psi=qq(cut[1][0]),qq(cut[0][1])
    assert qq(audit['center_width'])+qq(audit['cut_width'])<qq(flow.end)
    theta_s=qq(max_eprime)/3
    def differential_cost(ds,dp):
        return ds/lamlo+(theta_s/(rho*lamlo)+1/(rho*rcut))*dp
    center_cost=differential_cost(center_s,center_psi)
    cut_cost=differential_cost(cut_s,cut_psi)
    lift=max(center_cost,cut_cost)
    # sqrt(1+eta)<=1+eta, hence an entirely rational metric perturbation bound.
    result=max_raw+2*(1+max_raw)*lift+lift*lift
    assert result<Q(a.threshold),(float(result),a.threshold)
    detail=a.out.with_name(a.out.stem+'-intervals.json')
    detail.write_text(json.dumps(rows,indent=2)+'\n')
    references=[a.data,a.checkpoint,a.short_bridge,a.port,a.tail_manifest,a.prefix_audit,a.cut_bounds,a.center_certificate]
    sources=[Path(__file__),Path(__file__).with_name('interval_prefix_metric.py'),Path(__file__).with_name('prefix_true_profile.py'),
        Path(__file__).with_name('interval_tail_metric.py'),Path(__file__).with_name('certify_background_sharp.py'),
        Path(__file__).resolve().parents[1]/'finite_closure/m3_m8_closed_map/m3_shared_prefix.py']
    out=dict(scope=__doc__,command=sys.argv,success=True,threshold=a.threshold,
        inputs={str(p.resolve()):sha(p)for p in references},sources_sha256={p.name:sha(p)for p in sources},
        physical_reference=true.report(),all_radial_spans=len(rows),covered_material_interval=[float(x['knots'][0]),float(x['knots'][-1])],
        full_circle=True,all_phase=True,angular_sampling_used=False,radial_sampling_used=False,
        rho_lower=display(rho),phase_absolute_upper=max_phase,phase_first_absolute_upper=max_eprime,
        auxiliary_radius_error_upper=max_aux,maximum_raw_numerator_l1_upper=max_numerator,
        finite_raw_true_metric_upper=display(max_raw),maximum_angular_frequency=max_frequency,maximum_radial_degree=max_degree,
        center_lift_first_bounds=dict(radial=display(center_s),angular=display(center_psi),normalized_differential=display(center_cost)),
        cut_lift_first_bounds=dict(radial=display(cut_s),angular=display(cut_psi),normalized_differential=display(cut_cost)),
        continuous_prefix_metric_upper=display(result),
        exact_isometry_claimed=False,scratch_details={str(detail.resolve()):sha(detail)},seconds=time.monotonic()-started)
    a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)


if __name__=='__main__':main()
