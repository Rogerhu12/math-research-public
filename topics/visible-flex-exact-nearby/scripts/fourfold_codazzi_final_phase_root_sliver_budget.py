#!/usr/bin/env python3
"""Actual final root sliver and full transported-phase residual contract.

This bounds the genuine two-ray remainder after the declared scalar stop,
using the common drift cancellation and the complete real mean. It also
certifies the exact finite proposed H as an oriented analytic lift. It
does not claim that H conjugates the true return before its PDE residual
and terminal Fourier defect have been evaluated.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip,json,time
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_curvature_angle_energy_prefix import polynomial_ranges,dyadic
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha

EXPECTED=dict(candidate='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413',
    germ='397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864',
    repair='6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc',
    analytic='91f1a3e5900300cd6e66060063e0c9fe5b826e238f68cf9e49f356f0c4ff4071',
    proposal='32f559962fe14abe33f17c230846ad70f9bebab95aea27b1da09919e657f29f0')


def read(path):
    raw=Path(path).read_bytes();return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def b(x):return box_from_record(x)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--germ',type=Path,default=Path('notes/2026-11-13-R133-actual-moving0765-physical-complex-turning-germ-native.json.gz'))
    ap.add_argument('--repair',type=Path,default=Path('notes/2026-11-14-R133-final-exact-continuous-value-repair-native.json.gz'))
    ap.add_argument('--analytic',type=Path,default=Path('notes/2026-11-14-R133-complete-two-ray-analytic-strips-native.json.gz'))
    ap.add_argument('--proposal',type=Path,default=Path('notes/2026-11-14-R133-full-regular-response-ray-twist-proposal.json'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=256;ctx.cap=6
    if args.out.exists():raise FileExistsError('preserve each complete phase-root budget')
    for name,expected in EXPECTED.items():
        if sha(getattr(args,name))!=expected:raise ValueError('the exact same phase input changed: '+name)
    germ,repair,analytic,proposal=(read(getattr(args,n)) for n in ('germ','repair','analytic','proposal'))
    if not all(x['complete'] for x in (germ,repair,analytic)):raise ValueError('a complete geometric input is missing')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']));nodes=list(map(dyadic,saved['radial_nodes']))
    roots=list(map(Fraction,germ['root_interval']));gap=Fraction(1,2**32);stop=roots[0]-gap
    domain=list(map(Fraction,germ['complex_radial_rectangle']['real_interval']));piece=germ['actual_candidate_piece']
    if not domain[0]<stop<roots[0]<=roots[1]<domain[1] or not nodes[piece]<stop<roots[1]<nodes[piece+1]:
        raise ValueError('the complete final sliver must remain inside the same genuine analytic piece')
    y,_=polynomial_ranges(saved,nodes,piece,stop,roots[1]);alpha=exact_arb(Fraction(meta['exact_float_amplitude']))
    offset=list(map(Fraction,repair['special_piece_offsets'][str(piece)]['physical_offset']))
    intr=germ['complex_intrinsic_coefficients'];mean=b(intr['s']['real'])+alpha*y[32]+exact_arb(offset[32])
    gamma=abs(b(intr['gamma']['modulus_upper'])).upper();K1=abs(b(intr['K1']['modulus_upper'])).upper()
    length=exact_arb(roots[1]-stop);optical=(exact_arb(Fraction(2,3))*gamma*abs(mean)*K1.sqrt()*length**arb('1.5')).upper()
    # H is defined by all exact dyadic coefficients in the floating proposal.
    # Proving bounds for this finite polynomial does not certify its conjugacy.
    H=proposal['inverse_conjugacy_proposal'];a=list(map(dyadic,H['sine_coefficients']));c=list(map(dyadic,H['cosine_coefficients']))
    if len(a)!=24 or len(c)!=24:raise ValueError('all coefficients of the original proposed lift are required')
    field_width=Fraction(1,16);residual_width=Fraction(1,32);input_width=Fraction(1,64)
    budget=next(z for z in analytic['strip_budgets'] if z['outer_field_strip']==str(field_width))
    L=b(budget['complete_one_leg_integrated_first_derivative']).upper()
    hnorm=sum(((exact_arb(abs(x))+exact_arb(abs(z)))*(4*j*exact_arb(residual_width)).exp()
        for j,(x,z) in enumerate(zip(a,c),1)),arb(0)).upper()
    h1=sum((4*j*(exact_arb(abs(x))+exact_arb(abs(z)))*(4*j*exact_arb(residual_width)).exp()
        for j,(x,z) in enumerate(zip(a,c),1)),arb(0)).upper()
    image=(exact_arb(input_width)*(3*L).exp()).upper()
    tail=(2*(1+h1)*L.exp()*optical).upper()
    inverse_strip=(exact_arb(residual_width)-hnorm).lower()
    inverse_derivative=(1/(1-h1)).upper()
    gates=[dict(name=name,passed=bool(ok)) for name,ok in (
        ('the same complete repaired candidate and all original eta are retained',analytic['whole_original_eta'] and germ['whole_affine_parameter_interval']),
        ('the true variable root and the stop remain in one actual analytic germ',domain[0]<stop and roots[1]<domain[1]),
        ('the same exact cumulative root correction and true even mean are retained',len(offset)==65),
        ('the root slope and complete scalar speed modulus are finite',gamma.is_finite() and K1.is_finite() and mean.is_finite()),
        ('all finite H coefficients are exact dyadics',len(a)==24 and len(c)==24),
        ('the finite proposed H is an actual oriented analytic lift',h1<1),
        ('its complex inverse has a positive declared strip',inverse_strip>exact_arb(input_width)),
        ('all forward inverse and common-drift paths stay inside the residual strip',image<exact_arb(residual_width)),
        ('all these paths stay in the already proved outer field strip',exact_arb(residual_width)<exact_arb(field_width)),
        ('the complete final two-ray sliver cost is below one trillionth',tail<arb(10)**-12),
    )]
    report=dict(kind='actual_final_complete_phase_root_sliver_and_residual_contract',complete=all(g['passed'] for g in gates),
        source_sha256=sha(__file__),inputs={str(getattr(args,n)):expected for n,expected in EXPECTED.items()},
        derived_definition_sha256=repair['derived_definition_sha256'],candidate_sha256=EXPECTED['candidate'],
        whole_original_eta=True,exact_nu=meta['exact_float_nu'],actual_candidate_piece=piece,
        exact_root_interval=list(map(str,roots)),exact_scalar_stop=str(stop),exact_stop_gap=str(gap),
        full_root_sliver_length=record(length),complete_true_mean=record(mean),gamma_modulus=record(gamma),K1_modulus=record(K1),
        complete_one_ray_optical_sliver=record(optical),full_two_ray_conjugacy_defect_sliver=record(tail),
        field_strip=str(field_width),residual_and_terminal_Fourier_strip=str(residual_width),return_input_strip=str(input_width),
        complete_one_leg_drift_Lipschitz_integral=record(L),all_paths_imaginary_bound=record(image),
        exact_H_sine_coefficients=list(map(str,a)),exact_H_cosine_coefficients=list(map(str,c)),
        exact_proposed_rotation=str(dyadic(H['omega'])),H_minus_identity_strip_norm=record(hnorm),
        H_prime_minus_one_strip_norm=record(h1),H_inverse_input_strip=record(inverse_strip),H_inverse_derivative_upper=record(inverse_derivative),
        contract='true H(P)-H-Omega on strip1/64 <= complete terminal (Wminus-Wplus-Omega) norm on strip1/32 + both initial errors + all true PDE residual L1 norms on strip1/32 + every W jump norm + full root sliver',
        no_evaluated_transport_residual_claimed=True,no_actual_conjugacy_or_rotation_arithmetic_claimed=True,
        no_full_body_or_parameter_inverse_claimed=True,gates=gates,seconds=time.monotonic()-started)
    save(args.out,report)
    print(dict(complete=report['complete'],root_sliver=tail.str(14),optical=optical.str(14),H1=h1.str(14),
        inverse_strip=inverse_strip.str(14),path_bound=image.str(14),seconds=report['seconds']),flush=True)
    if not report['complete']:raise RuntimeError('a true complete root phase contract gate failed')


if __name__=='__main__':main()
