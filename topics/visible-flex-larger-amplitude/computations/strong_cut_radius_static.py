#!/usr/bin/env python3
"""Static metric/provider geometry for larger cuts and loop radii.

No tail is recalibrated, no DN entry is reused, and no resonance or nonlinear
BVP is solved. The cut slope and second derivative use the prescribed tail
cut identities wCut and -7*wCut/rCut. Reported curvature and dimensions are
background surface-of-revolution samples; they are not the flexible image.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse,gzip,hashlib,importlib.util,json,math
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkpoint',type=Path,required=True)
    parser.add_argument('--source-topic',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    raw=args.checkpoint.read_bytes();record=json.loads(gzip.decompress(raw) if args.checkpoint.suffix=='.gz' else raw)
    if not record.get('solver_success'):raise ValueError('Use a successful original physical profile')
    cfg=record['frozen_profile'];parameters=record['physical_tail_parameters']
    source=args.source_topic/'scripts/closing_recalibrated_tail.mjs'
    hashes={str(args.checkpoint):hashlib.sha256(raw).hexdigest(),str(source):hashlib.sha256(source.read_bytes()).hexdigest()}
    for name in ('strong_cut_radius_static.py','alternative-neck-provider.py','strong_angle_boost.py','alternative-neck-flatturn.py'):
        hashes[name]=hashlib.sha256((P/name).read_bytes()).hexdigest()
    spec=importlib.util.spec_from_file_location('strong_cut_static_provider',P/'alternative-neck-provider.py')
    provider=importlib.util.module_from_spec(spec);spec.loader.exec_module(provider)
    outer=cfg['loop_ratio']*cfg['loop_radius'];loop_span=outer-cfg['loop_radius'];rows=[]
    def inspect_parts(parts):
        summaries=[]
        for seg in parts:
            u=np.linspace(0.,1.,2049);a,v,acc=provider.piece_jet(seg,u);b=np.sqrt(1-v*v)
            principal=np.maximum(abs(acc)/b,b/a)
            summaries.append(dict(kind=seg['kind'],length=seg['length'],height=seg['dh'],
                radius_min_sample=float(a.min()),radius_max_sample=float(a.max()),
                meridian_curvature_max_sample=float(np.max(abs(acc)/b)),
                angular_curvature_max_sample=float(np.max(b/a)),
                principal_curvature_max_sample=float(principal.max()),
                absolute_gaussian_max_sample=float(np.max(abs(acc/a)))))
        return summaries
    def spherical_envelope(parts):
        z0=0.;s0=0.;best=dict(norm=0.);largest_gap=0.;endpoint_disagreement=0.
        for index,seg in enumerate(parts):
            u=np.linspace(0.,1.,2049);a,_,_=provider.piece_jet(seg,u)
            if seg['kind']=='hermite' or (seg['kind']=='boost' and not seg.get('strong_angle_boost')):
                v=provider.velocity(seg,u[:,None]*provider.base.gu[None,:])
                height=seg['length']*u/2*(np.sqrt(1-v*v)@provider.base.gw)
            else:height=seg['length']*provider.fl.integral(seg,u,'cos')
            z=z0+height;norm=np.hypot(a,z);j=int(np.argmax(norm))
            if norm[j]>best['norm']:best=dict(norm=float(norm[j]),radius=float(a[j]),height=float(z[j]),
                meridian=float(s0+u[j]*seg['length']),segment=index,kind=seg['kind'],u=float(u[j]))
            largest_gap=max(largest_gap,seg['length']/2048)
            endpoint_disagreement+=abs(float(height[-1])-seg['dh'])
            z0+=float(height[-1]);s0+=seg['length']
        return dict(twice_max_sampled_norm=2*best['norm'],maximizer=best,
            lipschitz_diameter_pad=largest_gap,provider_endpoint_height_disagreement=endpoint_disagreement,
            D_upper_prefix_bridge_estimate=2*best['norm']+largest_gap+2*endpoint_disagreement,
            integrated_height=z0,
            scope='The meridian is unit speed, so the norm is 1-Lipschitz and the sample-to-continuum diameter pad is max(ds). Numerical provider integration is not interval enclosed. Tail and cap are still separate.')
    for strategy in ('fixed_loop_ratio','fixed_loop_coast_radial_span'):
        for radius in (float(parameters['rCut']),.45,.55,.65,.75):
            loop=radius+(cfg['loop_radius']-parameters['rCut'])
            profile={**cfg,'loop_radius':loop,'loop_ratio':cfg['loop_ratio'] if strategy=='fixed_loop_ratio' else 1+loop_span/loop}
            w=float(parameters['wCut']);second=-7*w/radius
            cut=dict(radius=radius,backgroundSlope=w,backgroundSecond=second,E=1+w*w,Ep=2*w*second)
            cut=provider.tagged_port(dict(cut=cut),profile)['cut']
            prefix=provider.NeckPrefix(profile);bridge=provider.NeckTerminalBridge(cut)
            segments=inspect_parts(prefix.segments+bridge.segments)
            maximum=max(z['radius_max_sample'] for z in segments);minimum=min(z['radius_min_sample'] for z in segments)
            height=prefix.height+bridge.height
            envelope=spherical_envelope(prefix.segments+bridge.segments)
            rows.append(dict(strategy=strategy,cut_radius=radius,cut_slope=w,cut_second=second,
                prescribed_width=parameters['width'],prescribed_cuff_radius=radius-parameters['width'],
                profile=profile,outer_loop_coast_radius=profile['loop_ratio']*loop,
                prefix_height=prefix.height,bridge_height=bridge.height,total_background_height=height,
                total_meridian_length=prefix.end+bridge.end,background_radius_min_sample=minimum,
                background_radius_max_sample=maximum,
                background_principal_curvature_max_sample=max(z['principal_curvature_max_sample'] for z in segments),
                metric_required_principal_curvature_lower_sample=math.sqrt(max(z['absolute_gaussian_max_sample'] for z in segments)),
                reflected_background_diameter_lower_from_extent=max(2*maximum,2*height),
                reflected_background_enclosing_cylinder_diagonal=2*math.hypot(maximum,height),
                spherical_envelope=envelope,
                flat_cap_at_cut_height_spherical_diameter=2*math.hypot(radius-parameters['width'],height),
                remaining_envelope_budget=dict(tail_and_cap_height_above_cut='B >= 0, to be recomputed for the new tail and cap',
                    tail_cylinder_diameter_formula='2*sqrt(rCut^2+(heightCut+B)^2)',
                    cap_disk_diameter_formula='2*sqrt(rCuff^2+(heightCut+B)^2)',
                    rCut=radius,rCuff=radius-parameters['width'],heightCut=height),segments=segments))
    bd=math.sqrt(1-cfg['vd']**2)/cfg['vd'];bl=math.sqrt(1-cfg['loop_speed']**2)/cfg['loop_speed']
    result=dict(scope=__doc__,nonlinear_solution=False,tail_recalibrated=False,dn_reused=False,
        derivative_identity=dict(fixed_ratio='-sqrt(1-vd^2)/vd + 2*(ratio-1)*sqrt(1-vl^2)/vl',
            fixed_ratio_value=-bd+2*(cfg['loop_ratio']-1)*bl,
            fixed_coast_span='-sqrt(1-vd^2)/vd',fixed_coast_span_value=-bd,
            fixed_outer_formal='-sqrt(1-vd^2)/vd - 2*sqrt(1-vl^2)/vl',fixed_outer_formal_value=-bd-2*bl,
            fixed_outer_domain=f'Requires loop_radius < {outer}; not admissible for the requested .50/.60 inner radii.',
            scope='Exact prefix background height derivative with all other profile controls fixed. Terminal bridge varies separately.'),
        source_sha256=hashes,rows=rows,
        missing=['new tail calibration and linear DN','new nonlinear prefix and actual tail coupling','flexible-image diameter and reach','nonaxisymmetric cap construction'])
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(derivative_identity=result['derivative_identity'],rows=[{k:z[k] for k in
        ('strategy','cut_radius','prescribed_cuff_radius','outer_loop_coast_radius','total_background_height','background_radius_max_sample','background_principal_curvature_max_sample','metric_required_principal_curvature_lower_sample','spherical_envelope')}for z in rows])),flush=True)

if __name__=='__main__':main()
