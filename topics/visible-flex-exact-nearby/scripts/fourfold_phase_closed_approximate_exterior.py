#!/usr/bin/env python3
"""Combine completed true positive-domain cells and the actual R72 closure.

This program never promotes partial cells to a whole-domain certificate.  Its
finite inputs concern the same exact affine family, the natural graft, and the
already proved real core.  The infinite exterior is defined by the explicit
R11/R22 connector and true R72 profile, not by a finite radial cutoff.
It certifies an approximate closed embedded background and full finite-positive
source/DN constants; it does not certify a nonlinear isometric family.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path

from flint import arb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    with (gzip.open(path,'rt') if Path(path).suffix=='.gz' else open(path)) as f:
        return json.load(f)


def rational(x):
    return Fraction.from_float(x) if isinstance(x,float) else Fraction(x)


def lo(x):
    return arb(x['lower']).lower() if isinstance(x,dict) else arb(x).lower()


def hi(x):
    return arb(x['upper']).upper() if isinstance(x,dict) else arb(x).upper()


def minlo(values):return min(arb(x).lower() for x in values)


def maxhi(values):return max(arb(x).upper() for x in values)


def check_cover(rows,left,right,key='radial_interval'):
    intervals=sorted(tuple(map(rational,row[key])) for row in rows)
    cursor=Fraction(left)
    for a,b in intervals:
        if a!=cursor or not b>a:raise ValueError('radial cover gap, overlap, or empty interval')
        cursor=b
    if cursor!=Fraction(right):raise ValueError('radial cover has a wrong last endpoint')


def check_sources(report,source_name):
    here=Path(__file__).parent
    if report['source_sha256']!=digest(here/source_name):
        raise ValueError('certificate source changed: '+source_name)
    for name,sha in report['dependency_sha256'].items():
        if digest(here/name)!=sha:raise ValueError('certificate dependency changed: '+name)


def standardized(row,roots,graft=False):
    if graft:
        left,right=map(Fraction,row['physical_radial_interval'])
        Klo,Khi=lo(row['target_curvature']),hi(row['target_curvature'])
    else:
        left,right=map(Fraction,row['radial_interval'])
        Klo,Khi=map(arb,row['K'])
    rg,cg=row['real_geometry'],row['complex_geometry']
    if 'K_over_distance_input' in row:
        klo,khi=map(arb,row['K_over_distance_input'])
    else:
        if not left>roots[1] or not Klo>0:
            raise ValueError('a regular cell is not strictly beyond every root')
        klo=(Klo/exact_arb(right-roots[0])).lower()
        khi=(Khi/exact_arb(left-roots[1])).upper()
    al,au=lo(rg['alpha'][0]),hi(rg['alpha'][1])
    el,eu=lo(rg['eta'][0]),hi(rg['eta'][1])
    if not minlo((al,el,klo))>0:raise ValueError('positive matrix gate failed')
    v=maxhi((abs(lo(rg['drift_theta'][0])),abs(hi(rg['drift_theta'][1]))))
    return dict(left=left,right=right,klo=klo,khi=khi,al=al,au=au,el=el,eu=eu,
        vr=v,vc=hi(cg['drift_theta_modulus']),
        ac=hi(cg['alpha_modulus']),ec=hi(cg['eta_modulus']),
        Ylo=lo(rg['Yz'][0]),Yhi=hi(rg['Yz'][1]))


def complete_positive(rows,roots,cut,physical_strip):
    Llo=exact_arb(cut-roots[1]);Lhi=exact_arb(cut-roots[0])
    Ir=sum((exact_arb(row['right']-row['left'])*row['vr'] for row in rows),arb(0))
    Ic=sum((exact_arb(row['right']-row['left'])*row['vc'] for row in rows),arb(0))
    Jr,Jc=Ir.exp(),Ic.exp()
    m=minlo(minlo((row['al'],row['el']*row['klo'])) for row in rows)/Jr
    M=maxhi(maxhi((row['au'],row['eu']*row['khi'])) for row in rows)*Jr
    Mc=maxhi(maxhi((row['ac'],row['ec']*row['khi'])) for row in rows)*Jc
    rho=exact_arb(physical_strip)/(2*Jc)
    elllo,ellhi=Llo/4,Lhi/4
    Ctr=maxhi((2*ellhi+4/elllo+16/elllo**2,
               2*ellhi+4/elllo+32/(3*Llo*elllo)))
    CE=maxhi((1/elllo+ellhi/3+ellhi**2/12,
              1/elllo+ellhi/3+Lhi*ellhi/3))
    g=(1+Lhi**2/arb.pi()**2)/m
    poisson=CE.sqrt()*(1+M*g);DN=M*CE
    gain=(1+maxhi((arb(3),4/Llo**2))).sqrt()
    Nc=2*Mc*(-rho/2).exp()/(-(-rho/2).expm1())**2
    CL=CE*(1+2*g*(M+1))**2
    weight=minlo((rho/2,1/Nc,1/(2*g*Nc),1/(2*CL*Nc)))
    values=dict(length_lower=Llo,length_upper=Lhi,integrated_real_drift=Ir,
        integrated_complex_drift=Ic,real_J_and_inverse=Jr,complex_J_and_inverse=Jc,
        matrix_lower=m,matrix_upper=M,coefficient_strip=rho,complex_matrix_modulus=Mc,
        trace_squared=Ctr,extension_squared=CE,zero_Dirichlet_inverse=g,
        full_Poisson_and_Vdual_contact=poisson,full_DN=DN,
        interior_two_thirds_gain=gain,ordinary_source_to_full_contact=gain*poisson,
        coefficient_first_Fourier_moment=Nc,DN_commutator=CL,
        signed_analytic_weight=weight,Yz_lower=minlo(r['Ylo'] for r in rows),
        Yz_upper=maxhi(r['Yhi'] for r in rows),
        physical_L2_source_to_sheared_L2=Jr.sqrt()*maxhi(r['Yhi'] for r in rows))
    if not all(v.is_finite() for v in values.values()) or not m>0 or not weight>0:
        raise ValueError('nonfinite full-positive constant')
    return {k:ball_record(v) for k,v in values.items()}


def analytic_closed_tail(core,collar,bodies,graft,T):
    entry=graft['exact_radial_entrance']
    a=hi(entry['radius']);Zlo=lo(entry['height']);Zhi=hi(entry['height'])
    omega_lo=lo(entry['normalized_omega']);omega_hi=hi(entry['normalized_omega'])
    if not (omega_lo>arb(7)/5 and omega_hi<arb(3)/2 and a<arb(7)/10**6):
        raise ValueError('true constant radial entrance is outside the proved connector box')
    if T<Fraction(2**24):raise ValueError('the specified long barrier is too short')
    # For u in [0,T], a(u)=a*exp(-omega*u), z_u=a(u)^2/4.
    aT=a*(-omega_lo*exact_arb(T)).exp()
    radial_height=a*a/(8*omega_lo)
    # The R11 prepared q-profile has omega>9/10; the R72 profile after the
    # actual k=4 scaling has W/r and |W_r|<1/8 at Omega=2^360.
    connector_height=arb(5)/36*aT*aT
    tail_height=aT*aT/16
    Zfinal_upper=Zhi+radial_height+connector_height+tail_height
    tail_norm=(a*a+Zfinal_upper**2).sqrt()
    # The R33 primitive is centered in Cartesian coordinates. A closed curve
    # with |F_theta|=a lies within pi*a/2 of its angular mean.
    a3=hi(graft['entry']['radius'][0])
    graft_norm=Zhi+arb.pi()*a3/2
    body_norm=maxhi(arb(row['real_geometry']['norm2'][1]).sqrt()
                      for report in (collar,*bodies) for row in report['cells'])
    full_norm=maxhi((arb(core['F_norm_upper']),body_norm,graft_norm,tail_norm))
    D=2*full_norm
    hold_diameter=2*Zlo
    hold_ratio=hold_diameter/D
    # The exact reference profile constants, independent of the input graph.
    delta=arb(2)/25*arb(2)**(-128);Omega=arb(2)**360
    # b_tail<2, 1+|log(delta)|<96 and delta^(-5/2)<625*2^320.
    infinite_curvature=arb(5)*arb(2)**10*arb(2)**8*96*625*arb(2)**320/Omega
    if not infinite_curvature<arb(1)/8:
        raise ValueError('the complete true infinite-tail curvature fee exceeds 1/8')
    # epsilon_tail < 2^259 / h(T), since k=4 and W_b>2^-799.
    epsilon_upper=arb(2)**259*aT
    if not epsilon_upper<1 or not hold_ratio>arb(1)/5:
        raise ValueError('R72 epsilon or actual held-set diameter gate failed')
    values=dict(radial_height_increase=radial_height,
        connector_height_increase=connector_height,tail_height_increase=tail_height,
        final_height_lower=Zlo,final_height_upper=Zfinal_upper,
        final_exterior_radius_upper=a,radial_barrier_endpoint_radius_upper=aT,
        constant_radial_curvature_upper=hi(entry['principal_curvature_bound']),
        connector_curvature_upper=arb(5)/6,
        infinite_tail_curvature_upper=infinite_curvature,
        true_R72_epsilon_upper=epsilon_upper,core_norm_upper=arb(core['F_norm_upper']),
        body_norm_upper=body_norm,graft_norm_upper=graft_norm,tail_norm_upper=tail_norm,
        entire_closed_norm_upper=full_norm,entire_closed_diameter_upper=D,
        two_flat_subdisks_diameter_lower=hold_diameter,
        two_flat_subdisks_diameter_over_D_lower=hold_ratio)
    if not all(v.is_finite() for v in values.values()):raise ValueError('nonfinite closure value')
    return {k:ball_record(v) for k,v in values.items()}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--core',type=Path,required=True)
    ap.add_argument('--collar',type=Path,required=True)
    ap.add_argument('--body',type=Path,nargs='+',required=True)
    ap.add_argument('--graft',type=Path,required=True)
    ap.add_argument('--barrier-length',type=Fraction,default=Fraction(2**24))
    ap.add_argument('--bits',type=int,default=256)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits
    core,collar,graft=map(read,(args.core,args.collar,args.graft))
    bodies=[read(p) for p in args.body]
    if not core['complete'] or not core['proved_continuous_real_N_support_zeta']:
        raise ValueError('the actual whole core is not proved')
    if core['pending'] or core['failed_cells'] or not all(row['passed'] for row in core['cells']):
        raise ValueError('the actual core still has an unfinished cell')
    core_config=core['configuration'];here=Path(__file__).parent
    if core_config['source_sha256']!=digest(here/'fourfold_phase_affine_core_interval.py'):
        raise ValueError('actual core source changed')
    for name,sha in core_config['dependency_sha256'].items():
        if digest(here/name)!=sha:raise ValueError('actual core dependency changed: '+name)
    if not core['support_numerator_lower']>0:raise ValueError('core support is not positive')
    family=(collar['origin_inputs_sha256'],collar['direction_sha256'])
    parameter=tuple(map(Fraction,collar['exact_parameter_interval']))
    outer=tuple(map(Fraction,core['exact_parameter_fractions']))
    if not outer[0]<=parameter[0]<=parameter[1]<=outer[1]:
        raise ValueError('the finite-positive parameter box escapes the true core family')
    if family!=(core['configuration']['origin_inputs_sha256'],core['configuration']['frozen_direction_sha256']):
        raise ValueError('the core and positive body use different actual families')
    for report,source in [(collar,'fourfold_phase_positive_family_collar.py'),
             *[(r,'fourfold_phase_positive_family_outer.py') for r in bodies],
             (graft,'fourfold_phase_natural_exterior_graft.py')]:
        if not report['complete']:raise ValueError('a radial report is partial')
        if report.get('pending') or report.get('failed_cells') or report.get('failed'):
            raise ValueError('a radial report retains an unfinished or failed cell')
        if (report['origin_inputs_sha256'],report['direction_sha256'])!=family:
            raise ValueError('a radial report concerns a different actual family')
        if tuple(map(Fraction,report['exact_parameter_interval']))!=parameter:
            raise ValueError('the actual parameter intervals are not identical')
        check_sources(report,source)
    roots=tuple(map(Fraction,collar['root_interval']))
    if not roots[1]<rational(core['radial_core'][1]):
        raise ValueError('the true core does not overlap the positive collar')
    check_cover(core['cells'],0,rational(core['radial_core'][1]))
    check_cover(collar['cells'],roots[0],Fraction(1,4))
    flat=[row for report in bodies for row in report['cells']]
    check_cover(flat,Fraction(1,4),3)
    cut=Fraction(graft['exact_radial_entrance']['physical_cut'])
    check_cover(graft['rows'],3,cut,'physical_radial_interval')
    for row in [*collar['cells'],*flat]:
        if not row['real_geometry']['support'][0]>0:
            raise ValueError('a finite body cell lost strict radial support')
    for row in graft['rows']:
        if not minlo(lo(row['real_geometry'][key][0]) for key in ['support_factor','D','radius'])>0:
            raise ValueError('a graft cell lost actual strict radial support or immersion')
    normalized=[standardized(row,roots) for row in [*collar['cells'],*flat]]
    normalized.extend(standardized(row,roots,True) for row in graft['rows'])
    sigma=min([Fraction(collar['normalized_angle_strip'])/4,
               *[Fraction(r['normalized_angle_strip'])/4 for r in bodies],
               Fraction(graft['physical_angle_strip'])])
    positive=complete_positive(normalized,roots,cut,sigma)
    closed=analytic_closed_tail(core,collar,bodies,graft,args.barrier_length)
    files=[args.core,args.collar,*args.body,args.graft]
    report=dict(kind='actual_family_complete_positive_domain_and_closed_approximate_exterior',
        complete=True,exact_parameter_interval=list(map(str,parameter)),
        origin_inputs_sha256=family[0],direction_sha256=family[1],
        source_sha256=digest(__file__),bits=args.bits,
        input_sha256={str(p):digest(p) for p in files},
        mathematical_inputs={name:digest(Path(__file__).parents[1]/'results'/name) for name in [
            'R11-matched-mode-four-physical-tail-connector.md',
            'R14-mode-four-full-tail-geometric-bounds.md',
            'R15-full-tail-lines-label-weights-and-ordinary-sources.md',
            'R22-mu4-true-tail-and-source-conversion.md',
            'R23-mu4-full-graft-and-marker-geometry.md',
            'R66-actual-family-positive-collar-and-natural-exterior-graft.md']},
        exact_positive_cover=[str(roots[0]),str(cut)],
        collar_cells=len(collar['cells']),regular_body_cells=len(flat),graft_cells=len(graft['rows']),
        actual_moving_root_interval=list(map(str,roots)),physical_angular_strip=str(sigma),
        barrier_length=str(args.barrier_length),Omega='2^360',
        complete_finite_positive_operator=positive,closed_approximate_geometry=closed,
        scope=['Every parameter has its own true root; the short interval below it only supplies common bounds.',
               'The infinite tail is the actual R72 profile via the exact R11/R22 construction and k=4 scaling.',
               'The constructed closed background is approximate on the nonradial body and natural graft.',
               'The two flat subdisks have the required diameter, but their simultaneous fixation in a nonlinear family is not proved here.',
               'No full mixed-type nonlinear inverse, common-metric isometric family, reach bound, or visible-amplitude conclusion is asserted.'])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v['ball'] for k,v in closed.items() if k in [
        'entire_closed_diameter_upper','two_flat_subdisks_diameter_over_D_lower',
        'final_height_upper','infinite_tail_curvature_upper']},indent=2))


if __name__=='__main__':main()
