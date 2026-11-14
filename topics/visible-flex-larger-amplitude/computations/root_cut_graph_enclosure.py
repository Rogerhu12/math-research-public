#!/usr/bin/env python3
"""Rational graph-Hessian and convex-projection bounds for the R19 cut jet.

Uses the exact complete mean/second-jet correction enclosure already saved by
R19. This is one cut of two explicit arithmetic objects. It does not enclose
source evaluation error, a radial solution, or a full embedded tail graph.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import time


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--cut-enclosure',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();started=time.monotonic()
    source=Path(__file__).with_name('closure_scaled_endpoint_cut_enclosure.py')
    spec=importlib.util.spec_from_file_location('cut_rational_algebra',source)
    algebra=importlib.util.module_from_spec(spec);spec.loader.exec_module(algebra)
    plus,scale,norm,cosine=algebra.plus,algebra.scale,algebra.norm,algebra.cosine
    def bound(value,lower=False):
        # Keep the report compact. Rounding is exact outward rational rounding,
        # performed only after the full rational expression has been evaluated.
        den=1<<96
        num=(value.numerator*den)//value.denominator if lower else -((-value.numerator*den)//value.denominator)
        rounded=F(num,den)
        if (lower and rounded>value) or (not lower and rounded<value):
            raise AssertionError('Outward dyadic rounding failed')
        return dict(exact=str(rounded),decimal=float(rounded),
                    direction='lower' if lower else 'upper',dyadic_bits=96)
    report=json.loads(args.cut_enclosure.read_text())
    if report['input_sha256']!=sha(args.input):
        raise ValueError('The cut enclosure belongs to a different input')
    if report['entrypoint_sha256']!=sha(source):
        raise ValueError('The rational cut algebra differs from the saved computation')
    raw=args.input.read_bytes()
    packet=json.loads(gzip.decompress(raw) if args.input.suffix=='.gz' else raw)
    jets=packet['response']['jets'];spacing=report['spacing'];rows=[]
    for record in report['reports']:
        correction=record['exact_full_angle_cut_correction']
        if not correction['exists'] or not record['holonomy']['complete_real_mean_root_exists']:
            raise ValueError('The full angular cut correction was not established')
        metric={name:F(item['exact']) for name,item in record['input_metric'].items()}
        r,E,Ep=metric['r'],metric['E'],metric['Ep']
        if E<1:raise ValueError('The rational off-diagonal bound here assumes E>=1')
        eta=F(record['holonomy']['mean_slope_root_correction_abs_upper']['exact'])
        mu=F(correction['radial_second_correction_all_angle']['exact'])
        height=cosine(F(0),jets['height'],spacing)
        k=cosine(metric['mean_slope'],jets['slope'],spacing)
        kr=cosine(metric['mean_second'],jets['second'],spacing)
        # p=iP and k_theta-p=iR; the norms are unchanged by i.
        P={m:m*c/r for m,c in height.items()}
        pt={m:-m*c for m,c in P.items()}
        R=plus({m:m*c for m,c in k.items()},scale(P,-1))
        dmin=F(record['all_angle']['Delta_min']['exact'])
        smin=F(record['all_angle']['one_minus_p2_min']['exact'])
        corrected_dmin=dmin-2*eta*norm(k)-eta*eta
        vertical_normal_squared=corrected_dmin/E
        convex_numerator=1-(norm(k)+eta)*norm(pt)/smin
        # The complete corrected kr is generally infinite Fourier; mu already
        # encloses that entire correction, not only its retained projection.
        rr=(norm(plus(kr,scale(k,-Ep/(2*E))))+mu+abs(Ep)*eta/(2*E))/E
        rt=norm(R)/r  # sqrt(E)>=1, proved above, gives a rational upper bound.
        tt=(norm(plus(pt,scale(k,1/E)))+eta/E)/r
        intrinsic_hessian=max(rr+rt,tt+rt)
        if vertical_normal_squared<=0 or convex_numerator<=0:
            raise ValueError('The corrected cut failed a required positive branch')
        graph_hessian=intrinsic_hessian/vertical_normal_squared**2
        rows.append(dict(interpretation=record['interpretation'],
            corrected_complete_mean_shift_abs_upper=bound(eta),
            corrected_complete_radial_second_change_abs_upper=bound(mu),
            all_angle=dict(vertical_normal_squared_lower=bound(vertical_normal_squared,True),
                projected_curve_turning_numerator_lower=bound(convex_numerator,True),
                orthonormal_height_Hessian_component_abs_upper={
                    'rr':bound(rr),'rtheta':bound(rt),'thetatheta':bound(tt)},
                intrinsic_height_Hessian_operator_upper=bound(intrinsic_hessian),
                conditional_horizontal_graph_Hessian_operator_upper=bound(graph_hessian)),
            boundary_projection_strictly_convex=True,
            radial_graph_existence_or_interior_bound=False,
            scope='Full R19 corrected cut only. Graph-Hessian interpretation is conditional on realization by the same C2 isometric immersion.'))
    out=dict(scope=__doc__,status='Exact rational all-angle cut bounds, not a full tail certificate',
        input=str(args.input),input_sha256=sha(args.input),
        cut_enclosure=str(args.cut_enclosure),cut_enclosure_sha256=sha(args.cut_enclosure),
        source_algebra_sha256=sha(source),entrypoint_sha256=sha(Path(__file__)),
        reports=rows,seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),seconds=out['seconds'],peak_RSS_KiB=out['peak_RSS_KiB'],
        reports=[dict(kind=x['interpretation'],nz2=x['all_angle']['vertical_normal_squared_lower']['decimal'],
            turning=x['all_angle']['projected_curve_turning_numerator_lower']['decimal'],
            graph_hessian=x['all_angle']['conditional_horizontal_graph_Hessian_operator_upper']['decimal']) for x in rows])))


if __name__=='__main__':
    main()
