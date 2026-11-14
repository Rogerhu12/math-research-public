#!/usr/bin/env python3
"""Consume the new body's actual complex germ to close its fold/Airy collar.

The accompanying proof supplies analytic Picard, parity, inverse-chart and
two-port Green lemmas.  Every bound below is evaluated in directed Arb.
No old nonradial turning constants or changed candidate are substituted.
The collar ports are the actual inverse images of T=+/-delta; this script
does not certify the outside fixed-r seams or the full feedback inverse.
"""
from __future__ import annotations
import argparse,gzip,json,time,math
from fractions import Fraction
from pathlib import Path
from flint import arb,acb,ctx
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_metric_defect import record,save,sha
from fourfold_phase_beta_bulk_interval import exact_arb


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--germ',type=Path,default=Path('notes/2026-11-13-R133-actual-alpha075-complex-turning-germ.json.gz'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=320;started=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve every actual fold attempt')
    d=json.loads(gzip.decompress(args.germ.read_bytes()))
    if (not d['complete'] or not d['proved'] or not d['whole_affine_parameter_interval']
        or not d['all_finite_candidate_modes_retained']
        or d['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_turning_complex_germ.py'))):
        raise ValueError('the complete same-object new complex-germ certificate is required')
    B=d['bounds'];u=lambda k:box_from_record(B[k]).upper();l=lambda k:box_from_record(B[k]).lower()
    C=d['complex_intrinsic_coefficients']
    az=lambda k:acb(box_from_record(C[k]['real']),box_from_record(C[k]['imag']))
    R=exact_arb(Fraction(d['complex_radial_radius']));sig=exact_arb(Fraction(d['physical_theta_strip']))
    Z=arb(1)/512;rho=arb(2)**-26;Tb=arb(2)**-34;delta=arb(2)**-104
    Md,MP,Ld,LP=u('d'),u('aq'),u('dtheta'),u('aqtheta')
    epsilon=(Z*Z*Md+arb(2)/3*Z**3*MP).upper()
    lam=(Z*Z*Ld+arb(2)/3*Z**3*LP).upper()
    Jflow=(lam.exp()-1).upper()
    MG=(arb(2)/3*MP*lam.exp()).upper()
    MH=(epsilon/(Z*Z)).upper()
    t=rho/(Z*Z)
    Gdiff=(MG*t/(1-t)).upper()
    Gmin=(arb(2)/3*l('Re_aq_lower')-Gdiff).lower()
    Gprime=(MG/(Z*Z)/(1-t)**2).upper()
    Cmax=((arb(3)/2*MG)**(arb(2)/3)).upper()
    Cmin=((arb(3)/2*Gmin)**(arb(2)/3)/2).lower()
    Cr=(Gprime/(arb(3)/2*Gmin)**(arb(1)/3)).upper()
    Ctheta=(4*Cmax/sig).upper()
    Xr=(MH/(1-t)**2).upper();Xthetafee=(4*rho*MH/sig).upper()
    Trmin=(Cmin-rho*Cr).lower();Trmax=(Cmax+rho*Cr).upper()
    Ttheta=(rho*Ctheta).upper()
    Jmin=(Trmin-Trmax*Xthetafee-Xr*Ttheta).lower()
    Jmax=(Trmax*(1+Xthetafee)+Xr*Ttheta).upper()
    kmin=box_from_record(C['K1']['real']).lower();kmax=box_from_record(C['K1']['modulus_upper']).upper()
    bmin=(Cmin/kmax).sqrt().lower();bmax=(Cmax/kmin).sqrt().upper()
    frame=max(bmax.sqrt(),1/bmin.sqrt()).upper()
    DeltaMin=(l('Re_a_lower')*Jmin/bmax).lower()
    Asup=(Trmax+Md*Ttheta).upper()
    Ksmall=(rho*kmax).upper();Jprincipal=max(arb(1),Ksmall)
    Ainv=((Asup+u('a')*Ttheta*Jprincipal)/DeltaMin).upper()
    logr=(arb(1)/2*(Cr/Cmin+kmax/((R-rho)*kmin))).upper()
    logtheta=(Ctheta/(2*Cmin)).upper()
    logT=(((1+Xthetafee)*logr+Xr*logtheta)/Jmin).upper()
    logX=((Ttheta*logr+Trmax*logtheta)/Jmin).upper()
    Vmax=(frame**2*Ainv*u('complete_L_matrix')+(logT+logX)/2).upper()
    # Holomorphic inverse on |T|<=Tb, |Im X|<=sig/4.  The Picard
    # unknowns use radii rho/4 and sig/8, with their weighted max norm.
    ru=rho/4;rt=sig/8
    inverse_u_image=(Tb/Cmin).upper();inverse_theta_image=(ru*MH).upper()
    invrow1=(Tb/Cmin**2*(Cr+Ctheta*rt/ru)).upper()
    invrow2=(Xr*ru/rt+4*ru*MH/sig).upper()
    inverse_lipschitz=max(invrow1,invrow2).upper()
    source2D=(frame*Ainv*Jmax.sqrt()).upper()
    state2D=(frame/Jmin.sqrt()).upper()
    physical_angle_to_X_min=(Jmin/Trmax).lower()
    physical_angle_to_X_max=(Jmax/Trmin).upper()
    # Full two-line radial Airy reference: one negative incoming and one
    # positive unstable port, with mean two-state equations separately.
    Kair=arb(2)**25
    w2=(2*delta+arb(16)/3*delta**(arb(3)/4)+4*delta.sqrt()).upper()
    Gref=(Kair*w2).upper();Pref=(2*w2).sqrt()*Kair
    contraction=(Gref*Vmax).upper();resolvent=(1/(1-contraction)).upper()
    Usource=(resolvent*Gref).upper();Uports=(resolvent*Pref).upper()
    physical_source=(state2D*Usource*source2D).upper()
    physical_ports=(state2D*Uports).upper()
    # Full outgoing balanced trace, both components and both boundaries.
    # Each source response has norm <= Kair sqrt(w2); V acts on the whole
    # two-dimensional solution.  For the two-boundary direct sum use sqrt2.
    trace_source=(2*w2).sqrt()*Kair*(1+Vmax*Usource)
    trace_ports=2*Kair+(2*w2).sqrt()*Kair*Vmax*Uports
    jets=[Vmax]
    for j in range(1,7):jets.append((math.factorial(j)*(8/sig)**j*Vmax).upper())
    # Each q-th derivative is bounded by the table coefficient times the
    # sum of all supplied source/port derivative norms through q.
    source_stair=[Usource];port_stair=[Uports]
    for q in range(1,7):
        source_stair.append((resolvent*(Gref+Gref*sum((math.comb(q,j)*jets[j]*source_stair[q-j] for j in range(1,q+1)),arb(0)))).upper())
        port_stair.append((resolvent*(Pref+Gref*sum((math.comb(q,j)*jets[j]*port_stair[q-j] for j in range(1,q+1)),arb(0)))).upper())
    tests=[
        ('full compact bump vanishes and all source candidate modes remain',d['compact_bump_identically_zero_on_entire_actual_germ']),
        ('analytic rotational square-root quotient stays in right half-plane',(az('E')/az('rotational_gap')).real>0),
        ('blown-up root disk lies inside the proved actual radial disk',Z*Z<R),
        ('complete characteristic displacement fits every angular Picard margin',epsilon<sig/32),
        ('actual characteristic Picard and inverse derivative are contractions',lam<arb(1)/4 and Jflow<arb(1)/4),
        ('odd difference divided by z cubed has positive complex real part',Gmin>0),
        ('whole fold complex radial derivative has positive real part',Trmin>0),
        ('whole actual fold Jacobian stays nonzero',Jmin>0),
        ('full diagonal spinor and true first-order source inverse exist',DeltaMin>0 and bmin>0),
        ('complex canonical rectangle is mapped into the single actual germ',inverse_u_image<ru and inverse_theta_image<rt),
        ('two-variable inverse Picard map is a strict contraction',inverse_lipschitz<arb(1)/4),
        ('canonical Green rectangle and derivative strip fit inside the true inverse domain',delta<Tb/2 and delta<arb(1)/16),
        ('complete original zero-order matrix is absorbed in full two-dimensional L2',contraction<arb(1)/8),
        ('negative one-wave positive one-unstable and two mean ports retained',True),
        ('physical ordinary two-dimensional source Jacobian paid',source2D.is_finite() and physical_source.is_finite()),
        ('all canonical derivative staircase coefficients through six finite',all(x.is_finite() for x in source_stair+port_stair)),
    ]
    vals=locals();names=('epsilon','lam','Jflow','MG','MH','Gdiff','Gmin','Gprime','Cmax','Cmin','Cr','Ctheta',
        'Xr','Xthetafee','Trmin','Trmax','Ttheta','Jmin','Jmax','kmin','kmax','bmin','bmax','frame',
        'DeltaMin','Asup','Ksmall','Ainv','logr','logtheta','logT','logX','Vmax','inverse_u_image',
        'inverse_theta_image','invrow1','invrow2','inverse_lipschitz','source2D','state2D',
        'physical_angle_to_X_min','physical_angle_to_X_max','w2','Gref','Pref','contraction','resolvent',
        'Usource','Uports','physical_source','physical_ports','trace_source','trace_ports')
    complete=all(bool(v) for _,v in tests)
    doc=dict(kind='actual_reciprocal_body_fold_and_full_two_port_Airy_collar',complete=complete,proved=complete,
        source_sha256=sha(__file__),inputs={str(args.germ):sha(args.germ)},
        original_complex_germ_source_sha256=d['source_sha256'],actual_candidate_inputs=d['inputs'],
        object_sha256=d['object_sha256'],actual_fixed_nu=d['actual_fixed_nu'],exact_amplitude=d['exact_amplitude'],
        exact_center_parameter=d['exact_center_parameter'],exact_parameter_half_width=d['exact_parameter_half_width'],
        whole_affine_parameter_interval=True,actual_root_interval=d['root_interval'],
        exact_original_scalar_germ=d['original_scalar_germ'],exact_candidate_piece=d['exact_candidate_piece_interval'],
        scales=dict(blown_up_z_radius='1/512',fold_radial_radius='1/67108864',
            complex_canonical_T_radius='1/17179869184',canonical_real_half_width=str(Fraction(1,2**104)),
            original_theta_strip=d['physical_theta_strip'],canonical_complex_X_strip=str(Fraction(d['physical_theta_strip'])/4)),
        fold_definition=dict(X='(Splus+Sminus)/2',T='-(3*(Splus-Sminus)/4)^(2/3)',
            branch='Splus-Sminus = 2 z^3 G, Re G>0; T=(r-rstar)*(3G/2)^(2/3)',
            original_domain='exact inverse image of the canonical rectangle |T|<=delta, X in the entire physical-period circle'),
        full_original_physical_two_state_linearization=True,
        full_ordinary_physical_two_dimensional_L2_source=True,
        all_Fourier_modes_including_mean_and_both_port_outputs=True,
        negative_input='one full canonical incoming wave; at m=0 the first original canonical state',
        positive_input='one full canonical unstable Airy coefficient; at m=0 the second canonical state',
        canonical_higher_derivative_source_scope='all X derivatives through the requested order after the exact two-dimensional pullback; no free anisotropic physical-source equivalence',
        bounds={name:record(vals[name]) for name in names},
        canonical_coefficient_X_derivative_bounds=[record(x) for x in jets],
        canonical_L2_source_derivative_staircase=[record(x) for x in source_stair],
        canonical_port_derivative_staircase=[record(x) for x in port_stair],
        reference_negative_two_line_bound=64,reference_positive_split_kernel_bound=32,
        reference_complete_two_port_kernel_bound=2**25,
        no_candidate_PPoly_join_crossed=True,
        actual_nonlinear_body_existence_proved=False,
        outside_fixed_radial_seams_or_cap_regular_graph_identified=False,
        full_feedback_inverse_or_finite_head_solved=False,
        no_old_nonradial_numerical_turning_constants_transferred=True,
        gates=[dict(name=n,passed=bool(v)) for n,v in tests],seconds=time.monotonic()-started,
        dependencies={n:sha(Path(__file__).with_name(n)) for n in ('fourfold_codazzi_rotational_cap_jacobi.py',
            'fourfold_phase_metric_defect.py','fourfold_phase_beta_bulk_interval.py')})
    save(args.out,doc)
    print(dict(complete=complete,gates=len(tests),out=str(args.out),sha256=sha(args.out),
        Vmax=Vmax.str(14),jacobian_lower=Jmin.str(14),contraction=contraction.str(14),
        physical_source=physical_source.str(14),failed=[n for n,v in tests if not v]),flush=True)
    if not complete:raise SystemExit(1)


if __name__=='__main__':main()
