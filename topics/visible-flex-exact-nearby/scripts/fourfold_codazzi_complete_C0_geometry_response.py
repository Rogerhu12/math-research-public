#!/usr/bin/env python3
"""Actual full-model C0 state and compact-nu to geometry error constants.

Consume the already completed strict, positive, and genuine intervening
root coefficient certificates. No primitive, candidate solve, geometric
ODE, or completed old numerical gate is rerun. Unknown state variations
retain every angular mode and both means. The conclusions are conditional
on their explicit C0 error and world-anchor errors; PDE existence is not
asserted here.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import time
from flint import arb, ctx
from fourfold_codazzi_moving_geometry_angular_defect import strict_coefficients, positive_coefficients
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record

STRICT = '23a7554aa141b51b4c897f42399eb355d003d5fe5dd37b1c62f68025a4c8542a'
POSITIVE = 'ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d'
ANGULAR = '7a3dd2c1d48b611f5d9a6bd8c2d7ebeeeb4c2f6a7c2bcc4f61f4d012be4e2f90'
CANDIDATE = 'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
CONTROL_LEFT, CONTROL_RIGHT = Fraction(1,20), Fraction(9,50)


def load(path):
    raw = Path(path).read_bytes()
    data = gzip.decompress(raw) if raw[:2] == bytes((31,139)) else raw
    return json.loads(data), hashlib.sha256(raw).hexdigest()


def save(path, data):
    raw = (json.dumps(data, indent=2, allow_nan=False)+'\n').encode()
    if str(path).endswith('.gz'):
        raw = gzip.compress(raw, mtime=0)
    tmp = Path(str(path)+'.partial')
    tmp.write_bytes(raw)
    tmp.replace(path)


def v(record_):
    return box_from_record(record_)


def norm(*xs):
    return sum((x*x for x in xs), arb(0)).sqrt().upper()


def bump_bounds(left, right):
    if right <= CONTROL_LEFT or left >= CONTROL_RIGHT:
        return arb(0), arb(0)
    if left < CONTROL_LEFT or right > CONTROL_RIGHT:
        raise ValueError('a compact-control seam was crossed')
    t = exact_arb((left-CONTROL_LEFT)/(CONTROL_RIGHT-CONTROL_LEFT)).union(
        exact_arb((right-CONTROL_LEFT)/(CONTROL_RIGHT-CONTROL_LEFT)))
    w = (4096*t**6*(1-t)**6).upper()
    w = min(w, arb(1))  # (4t(1-t))^6 <= 1 on the actual real support.
    wp = abs(24576*t**5*(1-t)**5*(1-2*t)/exact_arb(CONTROL_RIGHT-CONTROL_LEFT)).upper()
    return w, wp


def local_gains(c, gap, amin, negative_K, left, right, eps_cap, nu_cap):
    a,beta,g,gl,k,mu,U,V,D = [c[name] for name in (
        'a','beta','gamma','gamma_lower','K','m_lower','u','v','d')]
    mt, bt = (mu-eps_cap).lower(), (gap-eps_cap).lower()
    if not min(a,gl,mt,bt) > 0:
        raise ValueError('a true mean, pointwise v or metric gap is unresolved')
    W, W1 = bump_bounds(left,right)
    if W.is_zero() and W1.is_zero():
        gnu, knu, G, glt, kt = arb(0),arb(0),g,gl,k
    else:
        if amin is None or not amin>0:
            raise ValueError('the active metric control needs the true radius lower bound')
        gnu = (g*W*(nu_cap*W/2).exp()/2).upper()
        knu = ((nu_cap*W).exp()*(k*W+beta*W1/(2*amin*amin*gl*gl))).upper()
        G = (g+gnu*nu_cap).upper()
        glt = (gl*(-nu_cap*W/2).exp()).lower()
        kt = (k+knu*nu_cap).upper()
    # Complete periodic primitive on L-infinity, including a nonzero mean:
    # its normalized sawtooth kernel has norm period/4 = pi/8.
    primitive = arb.pi()/8
    Su = (2*U+eps_cap+kt*(2*V+eps_cap)).upper()
    Sn = (knu*V*V).upper()
    du,dn = (primitive*beta*Su).upper(), (primitive*beta*Sn).upper()
    rv = (1/mt+V/(mu*mt)).upper()
    ru = (1/mt+U/(mu*mt)).upper()
    inverse_mean = (1/(mu*mt)).upper()
    T = (D*V/mu+g*U).upper()
    tauu = (D*rv+(V+eps_cap)*du/mt+G).upper()
    taun = ((V+eps_cap)*dn/mt+gnu*U).upper()
    pu = (beta*tauu/glt).upper()
    pn = (beta*taun/glt+T*beta*gnu/(glt*gl)).upper()
    qu = (a*(G*kt+D*ru+(U+eps_cap)*du/mt)).upper()
    qn = (a*(V*(G*knu+k*gnu)+(U+eps_cap)*dn/mt)).upper()
    tu = (a*(du/mt+D*inverse_mean)).upper()
    tn = (a*dn/mt).upper()
    omega_u,omega_n = norm(pu,qu,tu),norm(pn,qn,tn)
    force_u,force_n = (a*tauu).upper(),(a*norm(gnu,taun)).upper()
    speed = (a*norm(g,T)).upper()
    da = (kt+(2*U+eps_cap)/bt+U*U/(gap*bt)).upper()
    db = (1/bt+U/(gap*bt)).upper()
    dc = (1/(gap*bt)).upper()
    curvature_u = max((da+db).upper(),(db+dc).upper())
    curvature_n = (knu*V).upper()
    # Algebraic comparison shape matrix; it is not the model's geometric
    # shape operator before the exact Codazzi equation has been solved.
    reference_abs = (max((k*V+U*U/gap).upper(),(1/gap).upper())+U/gap).upper()
    if negative_K.is_zero():
        reference_positive = arb(0)
    else:
        au,cu,bu = negative_K*V,-1/V,U/gap
        reference_positive = max(arb(0),((au+cu+((au-cu)**2+4*bu**2).sqrt())/2).upper())
    return dict(reference_speed=speed, connection_state_gain=omega_u,
        connection_nu_gain=omega_n, position_velocity_state_gain=force_u,
        position_velocity_nu_gain=force_n, algebraic_curvature_state_gain=curvature_u,
        algebraic_curvature_nu_gain=curvature_n,
        reference_algebraic_absolute_curvature=reference_abs,
        reference_algebraic_positive_curvature=reference_positive,
        original_mean_gap=mu,original_pointwise_v_gap=gap,
        true_state_ball_mean_gap=mt,true_state_ball_pointwise_v_gap=bt,
        compact_w=W,compact_w_radial_derivative=W1,
        gamma_nu_difference_gain=gnu,K_nu_difference_gain=knu)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--strict',type=Path,required=True)
    ap.add_argument('--positive',type=Path,required=True)
    ap.add_argument('--angular',type=Path,required=True)
    ap.add_argument('--state-radius',type=Fraction,default=Fraction(1,1000))
    ap.add_argument('--nu-radius',type=Fraction,default=Fraction(1,100000))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();start=time.monotonic();ctx.prec=256;ctx.cap=6
    if args.out.exists():raise FileExistsError('preserve every complete response budget')
    if not 0<args.state_radius<=Fraction(1,1000) or not 0<args.nu_radius<=Fraction(1,100000):
        raise ValueError('the explicit same-state parameter neighborhood is required')
    strict,sh=load(args.strict);positive,ph=load(args.positive);angular,ah=load(args.angular)
    if (sh,ph,ah)!=(STRICT,POSITIVE,ANGULAR):
        raise ValueError('only the complete actual original coefficient natives are accepted')
    if not (strict['complete'] and strict['whole_requested_radial_interval'] and
            strict['whole_closed_angular_circle'] and positive['complete'] and
            positive['coefficient_cover_complete'] and angular['complete']):
        raise ValueError('a full original coefficient cover is missing')
    if (angular['candidate_sha256']!=CANDIDATE or angular['common_parameter_half_width']!='0' or
        strict['exact_amplitude']!=angular['exact_amplitude'] or strict['exact_nu']!=angular['exact_nu']):
        raise ValueError('the exact current object or common parameter scope differs')
    cover=[]
    for index,row in enumerate(strict['rows']):
        c=strict_coefficients(row)
        gap=v(row['base']['v_abs_lower']).lower()
        amin=v(row['scalar_mean']['actual_a']).lower()
        neg=max(arb(0),(-v(row['actual_target']['K']).lower()).upper())
        cover.append((tuple(map(Fraction,row['interval'])),c,gap,amin,neg,('strict',index)))
    root=angular['true_new_common_root_box']
    c={key:(v(value).lower() if key in ('gamma_lower','m_lower') else abs(v(value)).upper())
       for key,value in root['coefficients'].items()}
    gap=(2*c['m_lower']-c['v']).lower()
    root_left=cover[-1][0][1];root_right=Fraction(positive['rows'][0]['interval'][0])
    cover.append(((root_left,root_right),c,gap,None,c['K'],('root',0)))
    for index,row in enumerate(positive['rows']):
        c=positive_coefficients(row)
        gap=v(row['bounds']['real_physical_inverse_gap']).lower()
        amin=v(row['intrinsic']['a']).lower()
        neg=max(arb(0),(-v(row['intrinsic']['K']).lower()).upper())
        cover.append((tuple(map(Fraction,row['interval'])),c,gap,amin,neg,('positive',index)))
    if len(cover)!=7722 or cover[0][0][0]!=0 or cover[-1][0][1]!=Fraction(25,8):
        raise ValueError('the full genuine strict-root-positive cover changed')
    for i,item in enumerate(cover):
        left,right=item[0]
        if not left<right or i and left!=cover[i-1][0][1]:
            raise ValueError('the full coefficient cover has a gap or overlap')
    eps_cap,nu_cap=exact_arb(args.state_radius),exact_arb(args.nu_radius)
    rows=[]
    for (left,right),c,gap,amin,neg,source in cover:
        cuts=sorted({left,right}|{x for x in (CONTROL_LEFT,CONTROL_RIGHT) if left<x<right})
        for a,b in zip(cuts,cuts[1:]):
            gains=local_gains(c,gap,amin,neg,a,b,eps_cap,nu_cap)
            if not all(x.is_finite() for x in gains.values()):
                raise ValueError('a complete local response gain is nonfinite')
            rows.append(dict(interval=[str(a),str(b)],coefficient_source=list(source),
                gains={key:record(value) for key,value in gains.items()}))
    Ou,On,Pu,Pn,length=map(arb,(0,0,0,0,0))
    for row in reversed(rows):
        left,right=map(Fraction,row['interval']);h=exact_arb(right-left)
        gains={key:v(value).upper() for key,value in row['gains'].items()}
        speed=gains['reference_speed'];gu=gains['connection_state_gain'];gn=gains['connection_nu_gain']
        Pu=(Pu+h*speed*Ou+h*h*speed*gu/2+h*gains['position_velocity_state_gain']).upper()
        Pn=(Pn+h*speed*On+h*h*speed*gn/2+h*gains['position_velocity_nu_gain']).upper()
        Ou=(Ou+h*gu).upper();On=(On+h*gn).upper();length=(length+h*speed).upper()
        row['outward_anchor_to_inner_integrals']={key:record(value) for key,value in dict(
            state_to_frame=Ou,nu_to_frame=On,state_to_position=Pu,nu_to_position=Pn,frame_anchor_to_position=length).items()}
    maxima={key:max(v(row['gains'][key]).upper() for row in rows) for key in (
        'algebraic_curvature_state_gain','algebraic_curvature_nu_gain',
        'reference_algebraic_absolute_curvature','reference_algebraic_positive_curvature')}
    bounds=dict(state_to_frame=record(Ou),nu_to_frame=record(On),state_to_position=record(Pu),
        nu_to_position=record(Pn),frame_anchor_to_position=record(length),
        **{key:record(value) for key,value in maxima.items()})
    report=dict(kind='complete_actual_C0_state_and_nu_to_model_geometry_response_v1',complete=True,
        candidate_sha256=CANDIDATE,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        input_sha256={str(p):h for p,h in ((args.strict,sh),(args.positive,ph),(args.angular,ah))},
        exact_interval=['0','25/8'],common_parameter_half_width='0',
        actual_affine_center='-7789843107295549/4611686018427387904',
        exact_original_alpha=angular['exact_amplitude'],exact_original_nu=angular['exact_nu'],
        state_C0_radius=str(args.state_radius),nu_radius=str(args.nu_radius),
        state_error_definition='epsilon=max(sup_r_phi abs(u-u0),sup_r_phi abs(v-v0)); complete physical unnormalized moving state, including baseline changes and both means',
        original_coefficient_cells=len(cover),common_control_split_cells=len(rows),rows=rows,bounds=bounds,
        complete_angular_output_and_mean_retained=True,
        primitive_Linfinity_kernel_norm='pi/8 for period pi/2 with normalized measure',
        compact_control='4096 t^6 (1-t)^6; t=(r-1/20)/(13/100); zero outside [1/20,9/50]',
        a_beta_fixed_under_nu=True,affine_parameter_changes_not_granted=True,
        original_model_not_relabelled_as_repaired_centre=True,
        repair_must_be_included_in_state_error=True,
        world_anchor_errors_independent_and_not_zeroed=True,
        radial_numerical_and_angular_mesh_errors_not_counted_again=True,
        actual_error_radius_or_exact_PDE_solution_proved=False,
        real_caps_markers_or_final_surface_criteria_proved=False,
        dependencies={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in (
            'fourfold_codazzi_moving_geometry_angular_defect.py','fourfold_codazzi_rotational_cap_jacobi.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_metric_defect.py')},
        seconds=time.monotonic()-start)
    save(args.out,report)
    print(json.dumps(dict(complete=True,coefficient_cells=len(cover),control_cells=len(rows),
        bounds=bounds,seconds=report['seconds'])))


if __name__=='__main__':main()
