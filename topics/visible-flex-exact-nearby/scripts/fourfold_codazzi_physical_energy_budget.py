#!/usr/bin/env python3
"""New R138 actual physical residual/multiplier budget, public Actions only.

Only accepted complete coefficient/residual geometry rows are consumed.
No old producer is imported or called; no original candidate coefficient,
curvature, residual, primitive, or model ODE target is recomputed. The new
target is the scalar physical-frame defect and energy multiplier budget of
R138 X. All whole radial cells and the true-root collar are retained.

Scientific imports occur inside run. Published output contains only new
scalar conclusions, cumulative checkpoints, identities and scope metadata.
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
KIND = 'R138_same_Qrepair_complete_physical_energy_budget_v1'


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

    eps0 = rat(REPAIR_A0)
    eps1, epsm = 128*eps0, eps0
    pprimitive = arb.pi()/8
    sigma = rat(Fraction(2, 5))

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
                dp=upper(b['drift_phi_A0']))
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
                dp=(beta*(u*u+K*v*v)).upper())
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
        q0 = old['u']+old['v']
        kp = maximum(arb(1), old['K'])
        ds = (kp*(2*q0*eps0+eps0**2)).upper()
        b['dp'] = (old['dp']+2*old['beta']*ds).upper()
        return b

    def field_geometry(b):
        u,v,up,vp,mg,vg,mh = [b[k] for k in ('u','v','u1','v1','mlo','vgap','mhi')]
        lam = (mh/vg).upper()
        lamp = (mh*vp/vg**2).upper()
        upp,vpp = 128*up,128*vp
        B,C = (u/vg).upper(),(1/vg).upper()
        Bp,Cp = (up/vg+u*vp/vg**2).upper(),(vp/vg**2).upper()
        Bpp = (upp/vg+2*up*vp/vg**2+u*vpp/vg**2+2*u*vp**2/vg**3).upper()
        Cpp = (vpp/vg**2+2*vp**2/vg**3).upper()
        Bt,Ct = (lam*Bp).upper(),(lam*Cp).upper()
        Btt,Ctt = (lam**2*Bpp+lam*lamp*Bp).upper(),(lam**2*Cpp+lam*lamp*Cp).upper()
        F0,F1,F2 = norm(B,C),norm(Bt,Ct),norm(Btt,Ctt)
        a,e,b0 = b['a'],(b['a']*b['gamma']).upper(),(b['beta']/b['glo']).upper()
        om = norm(b0,a*F0)
        om1 = (a*F1).upper()
        Ap = (b['K']*vp+2*u*up/vg+u*u*vp/vg**2).upper()
        omr1 = (e*norm(lam*Ap,Bt)).upper()
        return dict(lam=lam,lamp=lamp,B=B,C=C,Bp=Bp,Cp=Cp,Bpp=Bpp,Cpp=Cpp,
            Bt=Bt,Ct=Ct,Btt=Btt,Ctt=Ctt,F0=F0,F1=F1,F2=F2,
            Fp=norm(Bp,Cp),Fpp=norm(Bpp,Cpp),a=a,e=e,b0=b0,
            omega=om,omega1=om1,omegar1=omr1,
            slo=(vg/mh).lower(),sp=(vp/mg).upper())

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

    def outer_state():
        old = original_background(len(positive['rows'])-1)
        b = repaired_background(old)
        go = field_geometry(old)
        eanchor,eanchor1 = [upper(angular['original_anchor_defects'][j]) for j in (0,1)]
        dt = eps0/b['mlo']+old['v']*epsm/(old['mlo']*b['mlo'])
        dphi = (pprimitive*dt/go['slo']).upper()
        dlambda = (epsm/b['vgap']+old['mhi']*eps0/(old['vgap']*b['vgap'])
                   +go['lamp']*dphi).upper()
        vg,vc,u,v,up,vp = old['vgap'],b['vgap'],old['u'],old['v'],old['u1'],old['v1']
        dc = eps0/(vg*vc)
        db = eps0/vc+u*eps0/(vg*vc)
        dcp = eps1/vc**2+vp*eps0*(2*v+eps0)/(vg**2*vc**2)
        dbp = (eps1/vc+up*eps0/(vg*vc)+(eps0*vp+(u+eps0)*eps1)/vc**2
                +u*vp*eps0*(2*v+eps0)/(vg**2*vc**2))
        df0 = (norm(db,dc)+go['Fp']*dphi).upper()
        df1 = ((old['mhi']+epsm)/vc*(norm(dbp,dcp)+go['Fpp']*dphi)
                +go['Fp']*dlambda).upper()
        z = (eanchor/go['slo']+b['a']*df0).upper()
        z1 = (eanchor1/go['slo']**2+eanchor*go['sp']/go['slo']**3
               +b['a']*(df0+df1)).upper()
        return dict(Z=z,Z_theta=z1,P=arb(0),P_theta=arb(0)),dict(
            original_anchor_E=eanchor,original_anchor_E_phi=eanchor1,
            same_physical_angle_repair_F0=df0,same_physical_angle_repair_F1=df1)

    max_keys = ('C_E','C_H','A_Theta','C_W','E_0','E_1','k_0','k_minus_one_third',
                'k_minus_one_half','epsilon','epsilon_theta','repair_residual_A0',
                'physical_curvature_defect','physical_curvature_defect_theta')
    sum_keys = ('drift_derivative_integral','epsilon_derivative_integral',
                'Volterra_J0','root_source_Kminus_squared')
    if args.resume:
        doc = json.loads(args.output.read_text())
        if doc['identity'] != identity or doc['complete'] or doc['failure'] is not None:
            raise ValueError('only this exact successful unfinished prefix may resume')
        done = int(doc['completed_closed_cells'])
        if not 0 <= done < len(cells):
            raise ValueError('the saved prefix count is not an unfinished original prefix')
        state = restored_scalars(doc['physical_defect_state'])
        maxima = restored_scalars(doc['new_scalar_suprema'])
        sums = restored_scalars(doc['new_scalar_integrals'])
        if set(maxima) != set(max_keys) or set(sums) != set(sum_keys):
            raise ValueError('the complete scalar accumulator set changed')
    else:
        state,anchor = outer_state()
        done = 0
        maxima = {name:arb(0) for name in max_keys}
        sums = {name:arb(0) for name in sum_keys}
        doc = dict(identity=identity,complete=False,proved=False,failure=None,
            completed_closed_cells=0,outer_initial_physical_defect=serialized_scalars(state),
            same_outer_anchor_comparison=serialized_scalars(anchor),
            old_scientific_target_calls=0,old_primitive_calls=0,old_geometry_ODE_calls=0,
            published_Fourier_or_frame_arrays=0,
            scope=dict(same_fixed_eta_nu_and_Qrepair=True,full_real_angular_circle=True,
                true_root_not_replaced_by_interval_endpoint=True,complete_means_retained=True,
                complete_original_interfaces_retained=True,physical_Qrepair_defects_have_no_interface_atoms=True,
                original_unrepaired_interface_fees_not_deleted=True,
                actual_DF_not_WVC_hybrid=True,root_boundary_form_constant_paid=False,
                full_positive_inverse_proved=False,final_topic_complete=False))

    def checkpoint():
        doc.update(completed_closed_cells=done,physical_defect_state=serialized_scalars(state),
            new_scalar_suprema=serialized_scalars(maxima),new_scalar_integrals=serialized_scalars(sums),
            current_exact_left=str(cells[len(cells)-done][0]) if done else str(RIGHT),
            current_wall_seconds=time.monotonic()-start)
        save(args.output,doc)

    checkpoint()
    try:
        while done < len(cells):
            left,right,index,body_index = cells[len(cells)-1-done]
            old = original_background(body_index)
            b = repaired_background(old)
            g = field_geometry(b)
            res = old_and_repaired_residual(old,b,angular['rows'][index])
            h = rat(right-left)
            a,e,lam,lp = g['a'],g['e'],g['lam'],g['lamp']
            B,C,Bt,Ct,Btt,Ctt = [g[k] for k in ('B','C','Bt','Ct','Btt','Ctt')]
            F0,F1,F2,slo,sp = [g[k] for k in ('F0','F1','F2','slo','sp')]
            R0,R1,T0,T1 = [res[k] for k in ('R0','R1','T0','T1')]
            ep0 = (pprimitive*T0/b['alo']).upper()
            ep1 = (T0/(b['alo']*slo)).upper()
            ep2 = (T1/(b['alo']*slo**2)+T0*sp/(b['alo']*slo**3)).upper()
            d0 = ((R0+F0*T0)/slo+pprimitive*T0*F1).upper()
            d1 = ((R1+F0*T1)/slo**2+(R0+F0*T0)*sp/slo**3
                    +2*T0*F1/slo+pprimitive*T0*F2).upper()

            z,z1,pp,pp1 = [state[k] for k in ('Z','Z_theta','P','P_theta')]
            aa,bb = g['omegar1']+d0,g['omega']*d0+d1
            iz = h*z+h*h*d0/2
            iz1 = h*z1+h*h*(aa*z+bb)/2+h*h*h*aa*d0/6
            state = dict(Z=(z+h*d0).upper(),Z_theta=(z1+aa*iz+h*bb).upper(),
                         P=(pp+e*iz).upper(),P_theta=(pp1+e*iz1).upper())
            z,z1,pp,pp1 = [state[k] for k in ('Z','Z_theta','P','P_theta')]
            o1 = (g['omega']+z).upper()
            o2 = (o1*g['omega']+g['omega1']+z1).upper()
            ru,rv,ru1p,rv1p = [res[k] for k in ('ru','rv','ru1','rv1')]
            ru1,rv1 = (lam*ru1p).upper(),(lam*rv1p).upper()
            ru2 = (lam*lam*384*ru1p+lam*lp*ru1p).upper()
            rv2 = (lam*lam*384*rv1p+lam*lp*rv1p).upper()

            tB,tC = (C*ru+B*C*rv).upper(),(C*C*rv).upper()
            tB1 = (Ct*ru+C*ru1+(Bt*C+B*Ct)*rv+B*C*rv1).upper()
            tC1 = (2*C*Ct*rv+C*C*rv1).upper()
            tB2 = (Ctt*ru+2*Ct*ru1+C*ru2+(Btt*C+2*Bt*Ct+B*Ctt)*rv
                     +2*(Bt*C+B*Ct)*rv1+B*C*rv2).upper()
            tC2 = (2*(Ct*Ct+C*Ctt)*rv+4*C*Ct*rv1+C*C*rv2).upper()
            dp0 = norm(tC,C*tB+B*tC,2*C*tC)
            dp1 = norm(tC1,Ct*tB+C*tB1+Bt*tC+B*tC1,2*Ct*tC+2*C*tC1)
            v,up,vp,u = [b[k] for k in ('v','u1','v1','u')]
            ut,vt = (lam*up).upper(),(lam*vp).upper()
            L0 = norm(v,u*v,v*v)
            L1 = norm(vt,ut*v+u*vt,2*v*vt)
            vf = product((v,vt),(F1,F2))
            mc_pair = ((b['mhi']*C).upper(),(b['mhi']*Ct).upper())
            crv = ((C*rv).upper(),(Ct*rv+C*rv1).upper())
            theta_t = (norm(tB1,tC1),norm(tB2,tC2))
            q0 = (u*u+b['K']*v*v).upper()
            q1 = (2*u*ut+2*b['K']*v*vt).upper()
            zcoef = (1+2*u+q0).upper()
            zs0 = (b['gamma']*z*zcoef).upper()
            zs1 = (b['gamma']*(z1*zcoef+z*(zcoef*o1+2*ut+q1))).upper()
            es0 = (2*ep0*o1).upper()
            es1 = (2*ep1*o1+2*ep0*(o2+o1*o1)).upper()
            kval = {}
            for tau in (Fraction(0),Fraction(1,3),Fraction(1,2)):
                ns = lambda value: nmult(value,tau)
                mq = ns((L0,L1))*(1+ns(vf)*(1+ns(mc_pair))/4)
                jr = (ns((dp0,dp1))+ns(theta_t)*ns((C,Ct))/4
                    +ns((F1,F2))*ns((C,Ct))*(ns(crv)/4+ns((ep0,ep1))))
                kval[tau] = (ns((arb(1),arb(2).sqrt()*o1))**2*jr*mq
                    +ns((zs0,zs1))+ns((es0,es1))+ns((ep1,ep2))).upper()

            M = (1+u*u+b['K']*v*v).upper()
            cw = (M/(b['glo']*sigma*b['vgap']**2)).upper()
            ce = (M/(sigma*b['vgap'])*(b['gamma']*b['mhi']+1/(b['glo']*b['mlo']))).upper()
            ch = (b['gamma']**2*u*u*b['mhi']/b['vgap']+b['K']*v/b['mlo']).upper()
            angle = maximum(v/b['mlo'],b['mhi']/b['vgap'])
            ft0,ft1 = (a+pp).upper(),(a*o1+pp1).upper()
            Lc0 = (b['gamma']*norm(arb(1),q0,2*u)).upper()
            Lc1 = (2*o1*Lc0+b['gamma']*norm(q1,2*ut)).upper()
            pbound = nmult(product((pp,pp1),(Lc0,Lc1)),Fraction(1,2))
            rbound = (2*nmult((rat(Fraction(222,125)),ft0),Fraction(1,2))*kval[Fraction(1,2)]).upper()
            ebound = nmult(product((ep0,ep1),(ft0,ft1)),Fraction(1,2))
            abound = nmult(((e+2*ep0*ft0).upper(),(e*o1+2*ep1*ft0+2*ep0*ft1).upper()),Fraction(1,2))
            values = dict(C_E=ce,C_H=ch,A_Theta=angle,C_W=cw,
                E_0=(pbound+rbound+ebound).upper(),E_1=(abound+pbound+rbound).upper(),
                k_0=kval[Fraction(0)],k_minus_one_third=kval[Fraction(1,3)],
                k_minus_one_half=kval[Fraction(1,2)],epsilon=ep0,epsilon_theta=ep1,
                repair_residual_A0=res['repair_residual'],
                physical_curvature_defect=d0,physical_curvature_defect_theta=d1)
            for key in max_keys:
                maxima[key] = maximum(maxima[key],values[key])
            sums['drift_derivative_integral'] = (sums['drift_derivative_integral']+h*b['dp']).upper()
            sums['epsilon_derivative_integral'] = (sums['epsilon_derivative_integral']+h*ep1).upper()
            sums['Volterra_J0'] = (sums['Volterra_J0']+120*h*cw*kval[Fraction(0)]**2).upper()
            sums['root_source_Kminus_squared'] = (sums['root_source_Kminus_squared']+h*kval[Fraction(1,3)]**2).upper()
            done += 1
            if done % 32 == 0 or done == len(cells):
                checkpoint()
            if done % 256 == 0:
                print(json.dumps(dict(completed_new_closed_cells=done,total_new_closed_cells=len(cells),
                                      old_scientific_targets_recomputed=0)),flush=True)

        # Consume the entire saved scalar balls, not hidden narrower internal
        # values, in every final derived coefficient and sufficient comparison.
        maxima = restored_scalars(doc['new_scalar_suprema'])
        sums = restored_scalars(doc['new_scalar_integrals'])
        state = restored_scalars(doc['physical_defect_state'])
        ee = (sums['epsilon_derivative_integral']/2).exp().upper()
        gg = sums['drift_derivative_integral'].exp().upper()
        Lmax = rat(RIGHT-ROOT_LO)
        he = (ee*sums['Volterra_J0'].sqrt()).upper()
        hb = (ee*Lmax.sqrt()/20000).upper()
        at,ce,ch = [maxima[k] for k in ('A_Theta','C_E','C_H')]
        we = (gg*(418*at).sqrt()*(ce.sqrt()+ch.sqrt()*he)).upper()
        wb = (gg*(418*at*ch).sqrt()*hb+10*at*(78*gg).sqrt()).upper()
        ze = (gg*(838*at).sqrt()*(ce.sqrt()+ch.sqrt()*he)).upper()
        zb = (gg*(838*at*ch).sqrt()*hb+10*at*(156*gg).sqrt()).upper()
        km = sums['root_source_Kminus_squared'].sqrt().upper()
        re = (ee*km*(we+he)).upper()
        rb = (ee*(rat(Fraction(1,20000))+km*(wb+hb))).upper()
        e0,e1 = maxima['E_0'],maxima['E_1']
        aee = (e0*we*we+e1*we*he).upper()
        aeb = (2*e0*we*wb+e1*(we*hb+wb*he)).upper()
        abb = (e0*wb*wb+e1*wb*hb).upper()
        derived = dict(E_epsilon=ee,Gamma=gg,h_E=he,h_B=hb,w_E=we,w_B=wb,
            z_E=ze,z_B=zb,root_Kminus=km,r_E=re,r_B=rb,
            a_EE=aee,a_EB=aeb,a_BB=abb,
            root_density_H_minus_one_third_norm=at.sqrt().upper())
        doc['complete_derived_energy_bounds'] = serialized_scalars(derived)
        saved_derived = restored_scalars(doc['complete_derived_energy_bounds'])
        ae,ab,bb = [saved_derived[k] for k in ('a_EE','a_EB','a_BB')]
        doc['body_only_sufficient_comparison'] = dict(
            root_constant_for_this_diagnostic='0; actual root constant remains independent',
            E_coefficient_less_than_2=bool(ae<2),
            B_coefficient_less_than_1=bool(bb<1),
            cross_discriminant_positive=bool(ae<2 and bb<1 and ab*ab<4*(2-ae)*(1-bb)),
            false_is_not_a_singularity_claim=True)
        doc.update(complete=True,proved=True,stage='complete-new-physical-scalar-budget',
            actual_root_physical_defect=serialized_scalars(state),
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
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--resume',action='store_true')
    run(parser.parse_args())


if __name__ == '__main__':
    main()
