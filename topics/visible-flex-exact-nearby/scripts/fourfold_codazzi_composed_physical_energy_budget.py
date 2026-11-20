#!/usr/bin/env python3
"""New composed physical feedback budget, only in public repository Actions.

Read the whole completed X budget and its execution. Its monotone root
Z/Ztheta/P/Ptheta bounds, Gamma, Eepsilon and geometric energy constants
are reused unchanged. No old frame propagation, old constant target, or
old scientific producer is called. The new calculation composes the exact
coordinate Hessian before taking norms, then consumes every original
closed cell for the new full multiplier and absorption budgets.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import os
from pathlib import Path
import time

POSITIVE_SHA = 'ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d'
ANGULAR_SHA = '7a3dd2c1d48b611f5d9a6bd8c2d7ebeeeb4c2f6a7c2bcc4f61f4d012be4e2f90'
GERM_SHA = '397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864'
CANDIDATE_SHA = 'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
OBJECT_SHA = '91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848'
REPAIR_SHA = '440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
ALPHA = Fraction(6890507429876859, 9007199254740992)
ETA = Fraction(-7789843107295549, 4611686018427387904)
NU = Fraction(-2572625729470897, 72057594037927936)
ROOT_LO = Fraction(1191984371497, 5000000000000)
ROOT_HI = Fraction(2383968743003, 10000000000000)
BODY_LEFT = Fraction(1192029371497, 5000000000000)
RIGHT = Fraction(25, 8)
REPAIR_A0 = Fraction(4, 10**18)
BITS = 320
KIND = 'R138_same_Qrepair_composed_physical_energy_budget_v1'
PRIOR_KIND = 'R138_same_Qrepair_complete_physical_energy_budget_v1'
PRIOR_SHA = '1259c3687cea0af523dd52055e88d5ee9a7b77094c218101835b6c38dfbbc7ec'
PRIOR_EXECUTION_SHA = '999555eafb3c443266f1a8fed98056c9d4f448c0131ef5ffff93941b35040c92'
PRIOR_SOURCE_SHA = '716fde1b56617680898ed61e7ebc0da0177c086e1a0f8865e36a5d7ff9b6a2eb'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path, expected):
    data = Path(path).read_bytes()
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError('accepted original native byte identity differs: '+str(path))
    return json.loads(gzip.decompress(data) if data[:2] == b'\x1f\x8b' else data)


def save(path, document):
    payload = (json.dumps(document, ensure_ascii=False, indent=2, allow_nan=False)+'\n').encode()
    temporary = Path(str(path)+'.partial')
    temporary.write_bytes(payload)
    temporary.replace(path)
    if path.read_bytes() != payload:
        raise OSError('new complete scalar checkpoint failed exact byte readback')


def run(args):
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
        or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('new scientific execution requires the public repository Actions child')
    if args.output.exists() and not args.resume:
        raise FileExistsError('preserve the completed or failed scientific result')
    if args.resume and not args.output.exists():
        raise FileNotFoundError('the requested unfinished prefix is absent')
    from flint import arb, ctx
    ctx.prec = BITS
    start = time.monotonic()
    args.output.parent.mkdir(parents=True, exist_ok=True)

    def rat(x):
        x = Fraction(x)
        return arb(x.numerator)/x.denominator

    def ball(record):
        return arb(record['lower']).lower().union(arb(record['upper']).upper())

    def hi(x):
        return abs(x).upper()

    def upper(record):
        return hi(ball(record))

    def maximum(*values):
        if not values:
            return arb(0)
        total = values[0]
        for value in values[1:]:
            total = total.union(value)
        return total.upper()

    def norm(*values):
        return sum((hi(x)**2 for x in values), arb(0)).sqrt().upper()

    def unpack(record):
        exponent = int(record['decimal_exponent'])
        scale = rat(10**exponent) if exponent >= 0 else rat(Fraction(1, 10**(-exponent)))
        midpoint = rat(int(record['midpoint_integer']))*scale
        radius = rat(int(record['radius_integer']))*scale
        return (midpoint-radius).lower().union((midpoint+radius).upper())

    def recorded(value):
        if not value.is_finite():
            raise ValueError('a new scalar budget is nonfinite')
        midpoint, radius, exponent = value.mid_rad_10exp(75)
        result = dict(kind='complete_decimal_ball_v1',
                      midpoint_integer=str(int(midpoint)), radius_integer=str(int(radius)),
                      decimal_exponent=str(int(exponent)))
        if int(radius) < 0 or not unpack(result).contains(value):
            raise ValueError('saved scalar does not enclose its complete original ball')
        return result

    def serialized_scalars(values):
        return {name: recorded(value.upper()) for name, value in values.items()}

    def restored_scalars(values):
        return {name: unpack(value).upper() for name, value in values.items()}

    def nmult(pair, tau):
        a0, a1 = pair
        if tau == 0:
            return a0.upper()
        if a0 == 0:
            return arb(0)
        if not a0 > 0 or not a1 >= 0:
            raise ValueError('invalid complete multiplier envelope')
        return (a0**rat(1-tau)*(a0+a1)**rat(tau)).upper()

    def product(left, right):
        a, ap = left
        b, bp = right
        return ((a*b).upper(), (ap*b+a*bp).upper())

    positive = read(args.positive, POSITIVE_SHA)
    angular = read(args.angular, ANGULAR_SHA)
    germ = read(args.germ, GERM_SHA)
    ident = positive['identity']
    if (not positive['complete'] or not positive['coefficient_cover_complete']
        or positive['failure'] is not None or len(positive['rows']) != 4650
        or ident['candidate_sha256'] != CANDIDATE_SHA or ident['object_sha256'] != OBJECT_SHA
        or Fraction(ident['actual_alpha']) != ALPHA or Fraction(ident['actual_nu']) != NU
        or Fraction(ident['exact_eta_center']) != ETA or not positive['whole_original_eta']):
        raise ValueError('accepted original positive complete scope differs')
    if (angular['kind'] != 'complete_original_moving_model_continuous_angular_defect_v1'
        or not angular['complete'] or angular['failure'] is not None
        or angular['candidate_sha256'] != CANDIDATE_SHA or angular['object_sha256'] != OBJECT_SHA
        or Fraction(angular['exact_amplitude']) != ALPHA or Fraction(angular['exact_nu']) != NU
        or angular['common_closed_box_count'] != 7722 or len(angular['rows']) != 7722
        or not angular['full_real_angular_circle']
        or not angular['even_source_and_interface_means_retained']
        or not angular['normalized_residual_multiplied_by_exact_physical_alpha']
        or not angular['complete_original_6143_value_jumps_paid']
        or not angular['original_centre_not_relabelled_as_continuous_repair']
        or list(map(Fraction, angular['interval'])) != [Fraction(0), RIGHT]):
        raise ValueError('accepted original complete moving angular scope differs')
    if (not germ['complete'] or not germ['proved'] or germ['failure'] is not None
        or germ['candidate_sha256'] != CANDIDATE_SHA or germ['object_sha256'] != OBJECT_SHA
        or Fraction(germ['exact_amplitude']) != ALPHA or Fraction(germ['actual_fixed_nu']) != NU
        or Fraction(germ['exact_center_parameter']) != ETA
        or list(map(Fraction, germ['root_interval'])) != [ROOT_LO, ROOT_HI]
        or not germ['whole_affine_parameter_interval'] or germ['actual_candidate_piece'] != 2549
        or not germ['compact_bump_identically_zero_on_entire_actual_germ']):
        raise ValueError('accepted true root germ scope differs')
    for interval in (germ['complex_radial_rectangle']['real_interval'], germ['original_scalar_germ']):
        left, right = map(Fraction, interval)
        if not left <= ROOT_LO < ROOT_HI < BODY_LEFT <= right:
            raise ValueError('the complete true-root collar leaves its original germ')

    cursor = BODY_LEFT
    interfaces = []
    for row in positive['rows']:
        left, right = map(Fraction, row['interval'])
        if left != cursor or not left < right:
            raise ValueError('an original positive closed row/interface is missing')
        if not row['physical_inverse_gap_certified']:
            raise ValueError('original whole positive inverse gap was not proved')
        if row['right_interface'] is not None:
            interfaces.append(row['right_interface'])
        cursor = right
    if cursor != RIGHT or len(interfaces) != 3594:
        raise ValueError('the full original positive cover or interface count differs')

    # This is an exact partition/identity operation, not a repeated scientific
    # target. The original angular partition already refines positive rows.
    cells, cursor, angular_interfaces = [], Fraction(0), []
    for index, row in enumerate(angular['rows']):
        left, right = map(Fraction, row['interval'])
        if left != cursor or not left < right:
            raise ValueError('an original angular closed row/interface is missing')
        cursor = right
        if 'left_candidate_join' in row:
            angular_interfaces.append(row['left_candidate_join'])
        if right <= ROOT_LO:
            continue
        left = max(left, ROOT_LO)
        source, source_index = row['coefficient_source']
        if left < BODY_LEFT:
            if source != 'new_true_root_box' or right > BODY_LEFT:
                raise ValueError('the true-root collar is not its original common root source')
            body_index = -1
        else:
            if source != 'positive':
                raise ValueError('a positive cell lost its exact original coefficient source')
            old_left, old_right = map(Fraction, positive['rows'][source_index]['interval'])
            if not old_left <= left < right <= old_right:
                raise ValueError('the common cell crosses its actual source row')
            body_index = source_index
        cells.append((left, right, index, body_index))
    if cursor != RIGHT or len(angular_interfaces) != 6143:
        raise ValueError('the original complete angular partition is not preserved')
    if not cells or cells[0][0] != ROOT_LO or cells[-1][1] != RIGHT:
        raise ValueError('the new scalar target does not cover the whole true positive interval')
    for left_cell, right_cell in zip(cells, cells[1:]):
        if left_cell[1] != right_cell[0]:
            raise ValueError('the new complete scalar integration has a gap')

    def meta_hash(value):
        return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

    identity = dict(kind=KIND, source_sha256=sha(__file__), arithmetic_bits=BITS,
        original_positive_sha256=POSITIVE_SHA, original_angular_sha256=ANGULAR_SHA,
        original_germ_sha256=GERM_SHA, original_candidate_sha256=CANDIDATE_SHA,
        intrinsic_object_sha256=OBJECT_SHA, exact_repair_definition_sha256=REPAIR_SHA,
        exact_alpha=str(ALPHA), exact_eta=str(ETA), exact_nu=str(NU), fixed_point='(0,0,1/2)',
        exact_true_root_interval=[str(ROOT_LO), str(ROOT_HI)],
        conservative_integration_interval=[str(ROOT_LO), str(RIGHT)],
        original_positive_rows=4650, original_angular_rows=7722,
        original_positive_interfaces=3594, original_angular_interfaces=6143,
        original_positive_interface_metadata_sha256=meta_hash(interfaces),
        original_angular_interface_metadata_sha256=meta_hash(angular_interfaces),
        new_complete_closed_cell_count=len(cells),
        new_common_partition_sha256=meta_hash([[str(a),str(b),i,j] for a,b,i,j in cells]),
        full_repair_A0=str(REPAIR_A0), full_repair_angular_bound='128*4/10^18',
        full_repair_mean_bound=str(REPAIR_A0), physical_period='2*pi')


    prior = read(args.prior_budget,PRIOR_SHA)
    prior_execution = read(args.prior_execution,PRIOR_EXECUTION_SHA)
    pi = prior['identity']
    if (not prior['complete'] or not prior['proved'] or prior['failure'] is not None
        or prior['stage'] != 'complete-new-physical-scalar-budget'
        or pi['kind'] != PRIOR_KIND or pi['source_sha256'] != PRIOR_SOURCE_SHA
        or prior['completed_closed_cells'] != len(cells) or len(cells) != 4651
        or prior['old_scientific_target_calls'] != 0 or prior['old_primitive_calls'] != 0
        or prior['old_geometry_ODE_calls'] != 0 or prior['published_Fourier_or_frame_arrays'] != 0
        or prior['scope']['actual_DF_not_WVC_hybrid'] is not True
        or prior['scope']['full_positive_inverse_proved'] is not False
        or prior['scope']['root_boundary_form_constant_paid'] is not False
        or prior['scope']['final_topic_complete'] is not False):
        raise ValueError('the entire completed original X budget or its qualification differs')
    for name in identity:
        if name not in ('kind','source_sha256') and identity[name] != pi[name]:
            raise ValueError('same full original object and closed partition differ: '+name)
    gate_names = ('E_coefficient_less_than_2','B_coefficient_less_than_1','cross_discriminant_positive')
    if not all(prior['body_only_sufficient_comparison'][key] is False for key in gate_names):
        raise ValueError('the original complete false sufficient comparison must remain unchanged')
    if (not prior_execution['complete'] or prior_execution['failure'] is not None
        or prior_execution['repository'] != 'Rogerhu12/math-research-public'
        or str(prior_execution['run_id']) != '44737045152'
        or str(prior_execution['run_attempt']) != '1'
        or prior_execution['actual_child_returncode'] != 0
        or prior_execution['scientific_children'] != 1
        or prior_execution['original_scientific_complete'] is not True
        or prior_execution['original_scientific_failure'] is not None
        or prior_execution['old_completed_targets_recomputed'] != 0
        or prior_execution['old_numerical_producers_called'] != 0
        or prior_execution['completed_closed_cells'] != len(cells)):
        raise ValueError('the original complete public X execution differs')
    matches = [item for item in prior_execution['scientific_files']
               if item['sha256'] == PRIOR_SHA]
    if len(matches) != 1 or matches[0]['bytes'] != len(args.prior_budget.read_bytes()):
        raise ValueError('the original execution does not identify the whole X conclusion')
    identity.update(prior_complete_budget_sha256=PRIOR_SHA,
                    prior_complete_execution_sha256=PRIOR_EXECUTION_SHA,
                    prior_source_sha256=PRIOR_SOURCE_SHA,prior_run='44737045152/1')
    previous_root = restored_scalars(prior['actual_root_physical_defect'])
    previous_sup = restored_scalars(prior['new_scalar_suprema'])
    previous_energy = restored_scalars(prior['complete_derived_energy_bounds'])
    z,z1,pp,pp1 = [previous_root[k] for k in ('Z','Z_theta','P','P_theta')]
    cw,ce,ch,at = [previous_sup[k] for k in ('C_W','C_E','C_H','A_Theta')]
    ee,gg,hb,wb,zb = [previous_energy[k] for k in ('E_epsilon','Gamma','h_B','w_B','z_B')]
    if not all(x >= 0 and x.is_finite() for x in (z,z1,pp,pp1,cw,ce,ch,at,ee,gg,hb,wb,zb)):
        raise ValueError('whole prior scalar upper endpoints are unresolved')
    if not all(x > 0 for x in (cw,ce,ch,at,ee,gg,hb,wb,zb)):
        raise ValueError('a reused geometric positive bound is unresolved')
    eps0 = rat(REPAIR_A0)
    eps1,epsm = 128*eps0,eps0
    pprimitive = arb.pi()/8
    def original_background(body_index):
        if body_index >= 0:
            row = positive['rows'][body_index]
            c, b = row['intrinsic'], row['bounds']
            get = lambda key: ball(c[key])
            mm = ball(b['mean_v'])
            result = dict(a=hi(get('a')), alo=get('a').lower(), beta=hi(get('beta')),
                gamma=hi(get('gamma')), glo=get('gamma').lower(), K=hi(get('K')),
                mlo=(-mm).lower(), mhi=hi(mm), u=upper(b['U_A0']), v=upper(b['V_A0']),
                u1=upper(b['U_phi_A0']), v1=upper(b['V_phi_A0']),
                vgap=ball(b['real_physical_inverse_gap']).lower(),
                nonmean=upper(b['V_nonmean_A0']))
        else:
            ci = germ['complex_intrinsic_coefficients']
            get = lambda key: ball(ci[key]['real'])
            mm = ball(germ['moving_mean_v']['real'])
            u, v = upper(germ['moving_U_derivative_Astrip'][0]), upper(germ['moving_v_derivative_Astrip'][0])
            beta, K = hi(get('beta')), hi(get('K'))
            result = dict(a=hi(get('a')), alo=get('a').lower(), beta=beta,
                gamma=hi(get('gamma')), glo=get('gamma').lower(), K=K,
                mlo=(-mm).lower(), mhi=upper(germ['moving_mean_v']['modulus_upper']),
                u=u, v=v, u1=upper(germ['moving_U_derivative_Astrip'][1]),
                v1=upper(germ['moving_v_derivative_Astrip'][1]),
                vgap=ball(germ['angle_inverse']['bounds']['v_gap']).lower(),
                nonmean=(v-(-mm).lower()).upper())
        if not min(result[k] for k in ('alo','glo','mlo','vgap')) > 0:
            raise ValueError('an original same-object geometric denominator is unresolved')
        return result

    def repaired_background(old):
        b = dict(old)
        b.update(u=(old['u']+eps0).upper(), v=(old['v']+eps0).upper(),
            u1=(old['u1']+eps1).upper(), v1=(old['v1']+eps1).upper(),
            mlo=(old['mlo']-epsm).lower(), mhi=(old['mhi']+epsm).upper(),
            vgap=(old['vgap']-eps0).lower())
        if not min(b[k] for k in ('alo','glo','mlo','vgap')) > 0:
            raise ValueError('actual Qrepair lost a whole-cell denominator')
        b['nonmean'] = (old['nonmean']+eps0).upper()
        return b


    def field_geometry(b):
        u,v,up,vp,mg,vg,mh = [b[k] for k in ('u','v','u1','v1','mlo','vgap','mhi')]
        lam = (mh/vg).upper()
        B,C = (u/vg).upper(),(1/vg).upper()
        Bt = (lam*(up/vg+u*vp/vg**2)).upper()
        Ct = (lam*vp/vg**2).upper()
        F0,F1 = norm(B,C),norm(Bt,Ct)
        a,e,b0 = b['a'],(b['a']*b['gamma']).upper(),(b['beta']/b['glo']).upper()
        om = norm(b0,a*F0)
        om1 = (a*F1).upper()
        return dict(lam=lam,B=B,C=C,Bt=Bt,Ct=Ct,F0=F0,F1=F1,a=a,e=e,
            omega=om,omega1=om1,slo=(vg/mh).lower(),sp=(vp/mg).upper())
    def old_and_repaired_residual(old, b, angular_row):
        mc = angular_row['model_coefficients']
        R0,R1,T0,T1 = [upper(mc[k]) for k in ('curvature','curvature_phi','torsion','torsion_phi')]
        m,a,u,v,up,vp = [old[k] for k in ('mhi','alo','u','v','u1','v1')]
        rm = (m*m*R0/a).upper()
        ru = (m*norm(arb(1),u)*R0/a).upper()
        rv = (m*(T0+v*R0)/a).upper()
        ru1,rv1 = (m*(R1+up*R0)/a).upper(),(m*(T1+vp*R0)/a).upper()
        q0,q1 = u+v,up+vp
        kp = maximum(arb(1),old['K'])
        ss,ds = kp*q0*q0,kp*(2*q0*eps0+eps0*eps0)
        fc = (old['beta']/4*(ds*q1+(ss+ds)*eps1)
            +old['gamma']*kp*(epsm*q1+(m+epsm)*eps1)
            +old['beta']*(eps0+ds*q0+(ss+ds)*eps0)).upper()
        di1 = (epsm/(old['mlo']*b['mlo'])).upper()
        di2 = (epsm*(2*m+epsm)/(old['mlo']**2*b['mlo']**2)).upper()
        def quotient_fee(z,z1,rz,rz1):
            g0 = (fc/b['mlo']+rz*di1
                +(eps0*(rm+fc)+z*fc)/b['mlo']**2+z*rm*di2).upper()
            g1 = (384*fc/b['mlo']+rz1*di1
                +(eps1*(rm+fc)+z1*fc)/b['mlo']**2+z1*rm*di2).upper()
            return g0,g1
        gu,gu1 = quotient_fee(u,up,ru,ru1)
        gv,gv1 = quotient_fee(v,vp,rv,rv1)
        gm = (fc/b['mlo']**2+rm*di2).upper()
        b0,aa = old['beta']/old['glo'],old['a']
        return dict(rm=(rm+fc).upper(),ru=(ru+fc).upper(),rv=(rv+fc).upper(),
            ru1=(ru1+384*fc).upper(),rv1=(rv1+384*fc).upper(),repair_residual=fc,
            R0=(R0+norm(b0*gv,aa*gu,aa*gm)).upper(),
            R1=(R1+norm(b0*gv1,aa*gu1)).upper(),
            T0=(T0+aa*gv).upper(),T1=(T1+aa*gv1).upper())


    max_keys = ('E_0','E_1','k_0','k_minus_one_third','k_minus_one_half')
    sum_keys = ('composed_k0_squared_integral','composed_kminus_squared_integral')
    derived_order = ('Volterra_J0','root_Kminus','h_E','w_E','z_E',
                     'r_E','r_B','a_EE','a_EB','a_BB')
    if args.resume:
        doc = json.loads(args.output.read_text())
        if doc['identity'] != identity or doc['complete'] or doc['failure'] is not None:
            raise ValueError('only this exact successful unfinished prefix may resume')
        done = int(doc['completed_closed_cells'])
        if not 0 <= done <= len(cells):
            raise ValueError('the saved prefix count is outside this original cover')
        maxima = restored_scalars(doc['new_scalar_suprema'])
        sums = restored_scalars(doc['new_scalar_integrals'])
        if set(maxima) != set(max_keys) or set(sums) != set(sum_keys):
            raise ValueError('the new complete scalar accumulator set changed')
        saved_order = tuple(doc['complete_derived_energy_bounds'])
        if saved_order != derived_order[:len(saved_order)]:
            raise ValueError('the saved derived scalar prefix is not the declared order')
    else:
        done = 0
        maxima = {name:arb(0) for name in max_keys}
        sums = {name:arb(0) for name in sum_keys}
        doc = dict(identity=identity,complete=False,proved=False,failure=None,
            completed_closed_cells=0,complete_derived_energy_bounds={},
            prior_complete_budget=dict(sha256=PRIOR_SHA,execution_sha256=PRIOR_EXECUTION_SHA,
                run='44737045152/1',json_path=[],whole_original_scope_and_false_gates_retained=True),
            reused_prior_scalar_paths=dict(
                physical_Z_Ztheta_P_Ptheta=['actual_root_physical_defect'],
                C_E_C_H_ATheta_CW=['new_scalar_suprema'],
                Gamma_Eepsilon_hB_wB_zB=['complete_derived_energy_bounds'],
                root_density_norm=['complete_derived_energy_bounds','root_density_H_minus_one_third_norm']),
            old_scientific_target_calls=0,old_primitive_calls=0,old_geometry_ODE_calls=0,
            old_frame_propagation_steps=0,old_energy_constant_targets_recomputed=0,
            published_Fourier_or_frame_arrays=0,
            scope=dict(same_fixed_eta_nu_and_Qrepair=True,full_real_angular_circle=True,
                true_root_not_replaced_by_interval_endpoint=True,complete_means_retained=True,
                complete_original_interfaces_retained=True,
                actual_DF_not_WVC_hybrid=True,root_boundary_form_constant_paid=False,
                full_positive_inverse_proved=False,final_topic_complete=False,
                primitive_to_L2_smoothing_used=True,exact_physical_C_primitive_used=True,
                complete_prior_X_outcome_preserved=True))

    def checkpoint():
        doc.update(completed_closed_cells=done,new_scalar_suprema=serialized_scalars(maxima),
            new_scalar_integrals=serialized_scalars(sums),
            current_exact_left=str(cells[len(cells)-done][0]) if done else str(RIGHT),
            current_wall_seconds=time.monotonic()-start)
        save(args.output,doc)

    def derived(name,make_value):
        existing = doc['complete_derived_energy_bounds']
        if name in existing:
            return unpack(existing[name]).upper()
        if derived_order[len(existing)] != name:
            raise ValueError('the exact new scalar order changed')
        original = make_value().upper()
        existing[name] = recorded(original)
        doc['stage'] = 'new-composed-energy-scalar-saved'
        save(args.output,doc)
        reread = json.loads(args.output.read_text())['complete_derived_energy_bounds'][name]
        if reread != existing[name] or not unpack(reread).contains(original):
            raise ValueError('the complete new derived ball failed outward readback')
        return unpack(reread).upper()

    checkpoint()
    try:
        while done < len(cells):
            left,right,index,body_index = cells[len(cells)-1-done]
            old = original_background(body_index)
            b = repaired_background(old)
            g = field_geometry(b)
            res = old_and_repaired_residual(old,b,angular['rows'][index])
            h = rat(right-left)
            a,e,lam = g['a'],g['e'],g['lam']
            B,C,Bt,Ct,F1,slo,sp = [g[k] for k in ('B','C','Bt','Ct','F1','slo','sp')]
            R0,R1,T0,T1 = [res[k] for k in ('R0','R1','T0','T1')]
            ep0 = (pprimitive*T0/b['alo']).upper()
            ep1 = (T0/(b['alo']*slo)).upper()
            ep2 = (T1/(b['alo']*slo**2)+T0*sp/(b['alo']*slo**3)).upper()
            o1 = (g['omega']+z).upper()
            o2 = (o1*g['omega']+g['omega1']+z1).upper()

            # Exact composed residual coordinates: s=Ru-B Rv, t=-C Rv.
            # The mean r3 cancels in s and has zero angular derivative in t.
            ma = (b['mhi']/b['alo']).upper()
            s0 = (ma*(R0+B*T0)).upper()
            t0 = (ma*(R0+C*T0)).upper()
            st = (ma*(lam*R1+Bt*T0+B*lam*T1)).upper()
            tt = (ma*(Ct*T0+C*lam*T1)).upper()
            d0 = norm(st,tt)
            local0 = norm(s0,arb(5).sqrt()*t0)
            local1 = (2*o1*local0+norm(st,arb(5).sqrt()*tt)).upper()

            # Exact reflection-class identity:
            # I_theta C = -(I_phi(v-m)) o Phi / m^2.
            # positive rows provide full V_nonmean_A0 directly. The germ
            # V[0] was defined as |m| plus that complete weighted sum;
            # only a true lower bound for |m| was subtracted above.
            if not b['nonmean'] >= 0:
                raise ValueError('the complete nonmean Wiener upper is unresolved')
            ic = min((pprimitive*C).upper(),
                     (b['nonmean']/(4*b['mlo']**2)).upper()).upper()
            mean0 = (b['mhi']*(d0*ic+ep0*F1)).upper()

            u,v,up,vp = [b[k] for k in ('u','v','u1','v1')]
            ut,vt = (lam*up).upper(),(lam*vp).upper()
            q0 = (u*u+b['K']*v*v).upper()
            q1 = (2*u*ut+2*b['K']*v*vt).upper()
            zcoef = (1+2*u+q0).upper()
            zs0 = (b['gamma']*z*zcoef).upper()
            zs1 = (b['gamma']*(z1*zcoef+z*(zcoef*o1+2*ut+q1))).upper()
            es0 = (2*ep0*o1).upper()
            es1 = (2*ep1*o1+2*ep0*(o2+o1*o1)).upper()
            kval = {}
            for tau in (Fraction(0),Fraction(1,3),Fraction(1,2)):
                nx = nmult((arb(1),o1),tau)
                ip = (arb(17)**rat(tau/2)/4).upper()
                kval[tau] = (nmult((local0,local1),tau)
                    +d0*ip*nx+mean0*nx+nmult((zs0,zs1),tau)
                    +nmult((es0,es1),tau)+nmult((ep1,ep2),tau)).upper()

            ft0,ft1 = (a+pp).upper(),(a*o1+pp1).upper()
            lc0 = (b['gamma']*norm(arb(1),q0,2*u)).upper()
            lc1 = (2*o1*lc0+b['gamma']*norm(q1,2*ut)).upper()
            pb = nmult(product((pp,pp1),(lc0,lc1)),Fraction(1,2))
            rb = (2*nmult((rat(Fraction(222,125)),ft0),Fraction(1,2))*kval[Fraction(1,2)]).upper()
            eb = nmult(product((ep0,ep1),(ft0,ft1)),Fraction(1,2))
            ab = nmult(((e+2*ep0*ft0).upper(),(e*o1+2*ep1*ft0+2*ep0*ft1).upper()),Fraction(1,2))
            values = dict(E_0=(pb+rb+eb).upper(),E_1=(ab+pb+rb).upper(),
                k_0=kval[Fraction(0)],k_minus_one_third=kval[Fraction(1,3)],
                k_minus_one_half=kval[Fraction(1,2)])
            for key in max_keys:
                maxima[key] = maximum(maxima[key],values[key])
            sums['composed_k0_squared_integral'] = (
                sums['composed_k0_squared_integral']+h*kval[Fraction(0)]**2).upper()
            sums['composed_kminus_squared_integral'] = (
                sums['composed_kminus_squared_integral']+h*kval[Fraction(1,3)]**2).upper()
            done += 1
            if done % 32 == 0 or done == len(cells):
                checkpoint()
            if done % 256 == 0:
                print(json.dumps(dict(completed_new_closed_cells=done,total_new_closed_cells=len(cells),
                    old_frame_propagation_steps=0,old_scientific_targets_recomputed=0)),flush=True)

        maxima = restored_scalars(doc['new_scalar_suprema'])
        sums = restored_scalars(doc['new_scalar_integrals'])
        j0 = derived('Volterra_J0',lambda: 120*cw*sums['composed_k0_squared_integral'])
        km = derived('root_Kminus',lambda: sums['composed_kminus_squared_integral'].sqrt())
        he = derived('h_E',lambda: ee*j0.sqrt())
        we = derived('w_E',lambda: gg*(418*at).sqrt()*(ce.sqrt()+ch.sqrt()*he))
        ze = derived('z_E',lambda: gg*(838*at).sqrt()*(ce.sqrt()+ch.sqrt()*he))
        re = derived('r_E',lambda: ee*km*(we+he))
        rb = derived('r_B',lambda: ee*(rat(Fraction(1,20000))+km*(wb+hb)))
        e0,e1 = maxima['E_0'],maxima['E_1']
        ae = derived('a_EE',lambda: e0*we*we+e1*we*he)
        cross = derived('a_EB',lambda: 2*e0*we*wb+e1*(we*hb+wb*he))
        bb = derived('a_BB',lambda: e0*wb*wb+e1*wb*hb)
        doc['body_only_sufficient_comparison'] = dict(
            root_constant_for_this_diagnostic='0; actual root constant remains independent',
            E_coefficient_less_than_2=bool(ae<2),B_coefficient_less_than_1=bool(bb<1),
            cross_discriminant_positive=bool(ae<2 and bb<1 and cross*cross<4*(2-ae)*(1-bb)),
            false_is_not_a_singularity_claim=True)
        doc.update(complete=True,proved=True,stage='complete-new-composed-physical-scalar-budget',
                   wall_seconds=time.monotonic()-start)
        save(args.output,doc)
        print(json.dumps(dict(complete=True,new_closed_cells=done,old_scientific_targets_recomputed=0,
            body_only_sufficient_comparison=doc['body_only_sufficient_comparison'],
            seconds=doc['wall_seconds'])),flush=True)
    except Exception as error:
        doc.update(failure=type(error).__name__+': '+str(error),complete=False,proved=False)
        checkpoint()
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--positive',type=Path,required=True)
    parser.add_argument('--angular',type=Path,required=True)
    parser.add_argument('--germ',type=Path,required=True)
    parser.add_argument('--prior-budget',type=Path,required=True)
    parser.add_argument('--prior-execution',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--resume',action='store_true')
    run(parser.parse_args())


if __name__ == '__main__':
    main()
