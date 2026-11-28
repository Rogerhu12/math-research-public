#!/usr/bin/env python3
"""Enclose R87's true beta from complete actual binary support coefficients.

Integration by parts changes the normalization to a positive polynomial
average of the normal-angle inverse. Exact polynomial weights and a complete
second-derivative remainder bound enclose that integral. Gaussian samples
never supply a bound. The recorded finite GL12/24-cell beta is compared with
this independent true-integral interval; position/derivative quadrature and
whole-surface geometry remain separate responsibilities.

An explicitly selected historical small record remains a historical parameter
source: lost raw files and original BVP acceptance are not silently rechecked.
The actual-run option instead invokes the unchanged original acceptance gate.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import resource
import sys
import time

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
REPO = SCRIPTS.parents[2]
CORE_SOURCE = SCRIPTS/'resume_transfer/material_flattened_support_core.py'
CORE_SHA = '1d655f2bdad53e1d320c1115a9873abe399a9b7ba930722c415d02dedb9b1f20'
ORIGINAL_CORE_SHA = 'a529904e265ddc95635c6c6601ea173eb0e1383a75e458d3eaee024fe7078ead'
STEP = {5:Q(126),6:Q(-420),7:Q(540),8:Q(-315),9:Q(70)}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path),sha256=sha(path))


def load_module(name,path):
    spec = importlib.util.spec_from_file_location(name,path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def fq(value):
    if type(value) not in (float,int) or not math.isfinite(value):
        raise ValueError('Require actual finite binary numerical inputs')
    return Q.from_float(float(value))


def ivq(value):
    value = Q(value)
    return mp.iv.mpf(value.numerator)/value.denominator


def endpoint(value):
    sign,mantissa,exponent,_ = value
    if not isinstance(mantissa,int):
        raise ArithmeticError('A nonfinite interval endpoint cannot be a certificate')
    return (-1 if sign else 1)*Q(mantissa)*(Q(2)**exponent)


def bounds(value):
    return tuple(endpoint(v) for v in value._mpi_)


def polynomial(value, moment=False):
    if moment:
        return sum((c*p*value**(p+1)/(p+1) for p,c in STEP.items()),Q(0))
    return sum((c*value**p for p,c in STEP.items()),Q(0))


def inverse_boxes(coefficients,S,width,panels):
    """Prove roots by a residual at an arbitrary seed and global rho_min."""
    frequencies = [3*(j+1) for j in range(len(coefficients))]
    rho_coeff = [(1-m*m)*a for m,a in zip(frequencies,coefficients)]
    signed = [b*((-1)**(j+1)) for j,b in enumerate(rho_coeff)]
    A = sum(map(abs,rho_coeff),Q(0))
    rho_min = 1-A
    targets = [S+width*Q(j,panels) for j in range(panels+1)]
    # Floating iterations only choose seeds. No convergence claim below uses
    # their residual, rounding, iteration count or stopping threshold.
    freq = np.asarray(frequencies,dtype=float)[:,None]
    sb = np.asarray(list(map(float,signed)))[:,None]
    target = np.asarray(list(map(float,targets)))
    phase = target.copy()
    amplitude = float(sum((abs(b)/m for b,m in zip(signed,frequencies)),Q(0)))
    low,high = target-amplitude-1e-14,target+amplitude+1e-14
    for _ in range(40):
        angle = freq*phase[None,:]
        residual = phase+np.sum(sb/freq*np.sin(angle),axis=0)-target
        slope = 1+np.sum(sb*np.cos(angle),axis=0)
        proposal = phase-residual/slope
        phase = np.minimum(high,np.maximum(low,proposal))
    result = []
    for target,seed in zip(targets,phase):
        center = fq(float(seed))
        value = ivq(center)-ivq(target)
        for b,m in zip(signed,frequencies):
            value += ivq(b/m)*mp.iv.sin(m*ivq(center))
        lo,hi = bounds(value)
        radius = max(abs(lo),abs(hi))/rho_min
        result.append((center-radius,center+radius))
    return result,rho_coeff


def true_beta(coefficients,S,width,k,panels):
    if panels < 2:
        raise ValueError('Use at least two complete rational transition panels')
    boxes,bcoef = inverse_boxes(coefficients,S,width,panels)
    A = sum(map(abs,bcoef),Q(0))
    B1 = sum((3*(j+1)*abs(b) for j,b in enumerate(bcoef)),Q(0))
    second = width*width*B1/(1-A)**3
    remainder = second/(8*panels*panels)
    lower,upper,total = Q(0),Q(0),Q(0)
    for j in range(panels):
        left,right = Q(j,panels),Q(j+1,panels)
        mass = polynomial(right)-polynomial(left)
        first_moment = polynomial(right,True)-polynomial(left,True)
        wr = (first_moment-left*mass)/(right-left)
        wl = mass-wr
        if min(wl,wr) < 0:
            raise ArithmeticError('A supposedly positive exact integration weight is negative')
        lower += wl*boxes[j][0]+wr*boxes[j+1][0]
        upper += wl*boxes[j][1]+wr*boxes[j+1][1]
        total += mass
    if total != 1:
        raise ArithmeticError('The complete polynomial transition measure lost mass')
    lower,upper = lower-remainder,upper+remainder
    pi_lower,pi_upper = bounds(mp.iv.pi)
    c = S+width/2
    Dlo,Dhi = pi_lower/3-c,pi_upper/3-c
    if Dlo <= 0 or pi_lower/3-S-width <= 0:
        raise ArithmeticError('The literal R87 window or normalization denominator is invalid')
    lo,hi = lower-k*c,upper-k*c
    if lo <= 0:
        raise ArithmeticError('This certificate has not separated positive beta')
    beta = (lo/Dhi,hi/Dlo)
    return dict(beta=beta,A=A,B1=B1,phase_second_bound=second,
        exact_weight_mass=total,weighted_phase_integral=(lower,upper),
        weighted_phase_interpolation_error=remainder,
        beta_interpolation_error_upper=remainder/Dlo,
        maximum_inverse_root_width=max(hi-lo for lo,hi in boxes),
        pi_interval=(pi_lower,pi_upper),denominator=(Dlo,Dhi),
        normal_angle_inverse_boxes=boxes)


def certificate(args):
    started = time.monotonic()
    if sha(CORE_SOURCE) != CORE_SHA or sha(args.original_core_source) != ORIGINAL_CORE_SHA:
        raise ValueError('Use the unchanged actual original support/material sources')
    path = (args.historical_note or args.actual_run).resolve()
    if args.historical_note is not None:
        record = json.loads(path.read_text())
        if (record.get('kind') != 'actual_original_R87_single_gentle_finite_stage'
                or record.get('classification') != 'accepted' or record.get('accepted') is not True
                or record.get('accepted_original_validator_passed') is not True):
            raise ValueError('Require the real published accepted parameter note, with its honest historical role')
        role = 'historical_published_actual_parameter_record_only'
        original_acceptance_revalidated = False
    else:
        sys.path.insert(0,str(SCRIPTS/'resume_20261126'))
        from material_design_secant_predictor import accepted_original
        record,raw = accepted_original(path,REPO)
        del raw
        role = 'current_original_accepted_design_with_all_raw_source_gates_revalidated'
        original_acceptance_revalidated = True
    settings = record['core_settings']
    cs = record['raw_return']['core_summary']
    coefficients = list(map(fq,cs['physical_parameters']))
    S,width,k = (fq(settings[key]) for key in ('halfwidth','transition','target_curvature'))
    if (len(coefficients) != record['modes'] or cs['base_mode'] != 3
            or cs['core_kind'] != 'material-curvature-flattening'
            or settings['curvature_blend'] != 1 or cs['curvature_blend'] != 1
            or not 0 < settings['homotopy'] <= 1 or cs['homotopy'] != settings['homotopy']
            or (S,width,k) != (fq(.675),fq(.3),Q(1,2))
            or any(settings[key] != cs[key] for key in ('halfwidth','transition','target_curvature',
                                                       'quadrature_order','integration_cells','transition_cells'))
            or (settings['quadrature_order'],settings['integration_cells'],settings['transition_cells']) != (12,64,24)
            or coefficients[0] != fq(cs['support_amplitude'])
            or list(map(fq,record['raw_return']['actual_core_corrections'])) != coefficients[1:]):
        raise ValueError('The complete actual finite R87 coefficient/GL/settings identity differs')
    A = sum(((9*(j+1)**2-1)*abs(c) for j,c in enumerate(coefficients)),Q(0))
    if A > Q(8,9):
        raise ValueError('The actual full weighted support coefficients leave the R91/R94 sufficient box')
    mp.iv.dps = 80
    scalar = true_beta(coefficients,S,width,k,args.panels)
    lo,hi = scalar['beta']
    recorded_beta = fq(cs['compensation_beta'])
    beta_error = max(abs(recorded_beta-lo),abs(recorded_beta-hi))
    coarse_ceiling = Q(897,314)
    transferred_ceiling = Q(9)+coarse_ceiling+beta_error
    if transferred_ceiling >= Q(123,10):
        raise ArithmeticError('This finite normalization error has not paid the retained 12.3 curvature budget')
    # Only the small core is reconstructed. This invokes no prefix model,
    # field integration, Jacobian, BVP, native tail or old full certificate.
    original = load_module('_beta_actual_original_core',args.original_core_source)
    material = load_module('_beta_actual_material_core',CORE_SOURCE)
    seed = original.PlanarSupportCore(float(coefficients[0]),
        [float(v) for v in coefficients[1:]],base_mode=3)
    fresh = material.MaterialFlattenedSupportCore(seed,**settings)
    fresh_beta = fq(fresh.beta)
    fresh_error = max(abs(fresh_beta-lo),abs(fresh_beta-hi))
    roots = scalar.pop('normal_angle_inverse_boxes')
    encoded = json.dumps([[str(a),str(b)] for a,b in roots],separators=(',',':')).encode()
    exact = {key:([str(v) for v in value] if isinstance(value,tuple) else str(value))
             for key,value in scalar.items()}
    return dict(schema='R87-complete-actual-support-true-beta-positive-measure-certificate-v1',
        status='complete_actual_scalar_normalization_error_enclosed',source=ref(__file__),
        input=ref(path),input_role=role,
        original_BVP_acceptance_revalidated=original_acceptance_revalidated,
        actual_support_coefficients_exact=list(map(str,coefficients)),modes=len(coefficients),
        original_support_source=ref(args.original_core_source),material_source=ref(CORE_SOURCE),
        source_settings=settings,source_homotopy_exact=str(fq(settings['homotopy'])),
        S_exact=str(S),b_exact=str(width),k_exact=str(k),
        complete_transition_panels=args.panels,exact_scalar_bounds=exact,
        inverse_root_count=len(roots),inverse_boxes_sha256=hashlib.sha256(encoded).hexdigest(),
        inverse_method='Each arbitrary floating seed is enclosed by a directed interval residual divided by the exact positive global rho lower bound; seed convergence is not assumed.',
        integration_method='Exact positive polynomial weights of the piecewise-linear inverse interpolant, plus the full b^2*sum(m*abs(rho_m))/(1-A)^3/(8*N^2) remainder.',
        recorded_finite_Gauss_beta_exact=str(recorded_beta),
        recorded_finite_Gauss_beta_true_error_upper_exact=str(beta_error),
        reconstructed_finite_Gauss_beta_exact=str(fresh_beta),
        reconstructed_finite_Gauss_beta_true_error_upper_exact=str(fresh_error),
        finite_Gauss_beta_reproduced_bitwise=bool(fresh_beta==recorded_beta),
        transferred_scalar_curvature_upper_exact=str(transferred_ceiling),
        retained_12p3_scalar_margin_exact=str(Q(123,10)-transferred_ceiling),
        finite_curvature_formula_only=True,
        finite_phase_derivative_or_position_quadrature_error_paid=False,
        existing_full_true_integral_oracle='resume_20261126/warm_phase_validated_core.py, zero phase specialization; recompute from actual coefficients, not old bounds',
        old_raw_or_BVP_regenerated=False,large_matrix_or_native_called=False,
        actual_lambda_one_field_produced=False,whole_surface_geometry_certified=False,
        readme_completion_claimed=False,seconds=time.monotonic()-started,
        maximum_rss_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        runtime_versions=dict(python=sys.version,numpy=np.__version__,mpmath=mp.__version__))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    inputs = parser.add_mutually_exclusive_group(required=True)
    inputs.add_argument('--historical-note',type=Path)
    inputs.add_argument('--actual-run',type=Path)
    parser.add_argument('--original-core-source',type=Path,required=True)
    parser.add_argument('--panels',type=int,default=64)
    parser.add_argument('--out',type=Path,required=True)
    args = parser.parse_args()
    out = args.out.resolve()
    if out.exists() or out == REPO or REPO in out.parents:
        raise ValueError('Write one fresh small scalar record outside the source repository')
    result = certificate(args)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(status=result['status'],output=ref(out),
        true_beta_interval=result['exact_scalar_bounds']['beta'],
        normalization_error_upper=float(Q(result['recorded_finite_Gauss_beta_true_error_upper_exact'])),
        scalar_curvature_upper=float(Q(result['transferred_scalar_curvature_upper_exact'])),
        finite_Gauss_beta_reproduced_bitwise=result['finite_Gauss_beta_reproduced_bitwise'],
        seconds=result['seconds'],maximum_rss_KiB=result['maximum_rss_KiB'])),flush=True)


if __name__ == '__main__':
    main()
