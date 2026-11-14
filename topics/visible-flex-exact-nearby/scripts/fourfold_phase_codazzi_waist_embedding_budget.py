#!/usr/bin/env python3
"""Consume the frozen R127 certificate and check R128's rational embedding gates.

This does not reconstruct or sample an embedding. The exact embedding
theorem uses R126's frame identities, the R127 actual PDE existence and the
original R79/R123 waist support/radius bounds. Every new numerical gate is
checked either by directed Arb inclusion or exact rational arithmetic.
"""
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as Q
from pathlib import Path
from flint import arb,ctx


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def exact(q):
    q=Q(q);return arb(q.numerator)/q.denominator
def bound(record,key):return arb(record[key])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--certificate',type=Path,default=Path('notes/2026-11-13-Codazzi-continuation-r001-v3-native.json'))
    p.add_argument('--out',type=Path,required=True);args=p.parse_args();ctx.prec=192
    if sha(args.certificate)!='0f7aa2f4e9a1df567b209cd873f2af5f6428feafc01a9613fc75a46259fb75eb':
        raise ValueError('the frozen R127 certificate changed')
    data=json.loads(args.certificate.read_bytes())
    identities={
        'source_sha256':'ea61a2d27273352b65951900359301df41e9a29a2a9c2ef62836809de4981acc',
        'coefficient_provider_sha256':'4a37d58640b54b091fab9bfd677b55e3392c30405d08073a2ad90f13205cf9f1',
        'candidate_sha256':'a3e43fc8ee7ab8b6a0e080edccb107ac1e2d92634b0325783f7a99711cf6842f',
        'object_sha256':'91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848'}
    if any(data.get(k)!=v for k,v in identities.items()):raise ValueError('R127 identity mismatch')
    for k in ('complete','continuation_certified','whole_affine_parameter_interval','whole_real_angular_circle'):
        if not data[k]:raise ValueError('missing R127 actual complete gate: '+k)
    if data['exact_requested_interval']!=['0','1/1000'] or data['covered_interval']!=['0','1/1000']:
        raise ValueError('unexpected certified radial domain')
    if data['parameter_half_width']!='1/1000000000':raise ValueError('different parameter family')
    if not data['barrier']['passed'] or not all(data['barrier']['gates'].values()):raise ValueError('R127 barrier failed')
    rows=data['rows'];barrier=data['barrier']
    e0=bound(barrier['C0_final_barrier'],'upper').upper()
    phat=bound(barrier['maxima']['Mhat'],'upper').upper()
    gap=bound(barrier['candidate_gap_lower'],'lower').lower()-2*e0
    kmax=max(bound(r['true_target_coefficients']['k'],'upper').upper() for r in rows)
    Emax=max(bound(r['true_target_coefficients']['E'],'upper').upper() for r in rows)
    Emin=min(bound(r['true_target_coefficients']['E'],'lower').lower() for r in rows)
    amin=min(bound(r['true_target_coefficients']['a'],'lower').lower() for r in rows)
    M=Q(2737,1000);d=Q(41,250);k=Q(463,500);e=Q(111,100);T=Q(1,1000)
    A=Q(85);B=Q(31);C=Q(12);R=Q(13,10);support=Q(1,2)
    Yrate=Q(35);nrate=Q(101);Xrate=Q(95)
    gates=dict(
        actual_Riemann_amplitude=bool(phat+e0<exact(M)),
        actual_Riemann_gap=bool(gap>exact(d)),
        target_k_upper=bool(kmax<exact(k)),
        target_sqrtE_upper=bool(Emax<exact(e*e)),
        target_sqrtE_lower=bool(Emin>1),target_a_lower=bool(amin>1),
        actual_A_bound=bool(2*k*M*M/d<A),
        actual_B_bound=bool(2*k*M/d<B),actual_C_bound=bool(2*k/d<C),
        Y_radial_rate=bool(e*B<Yrate),normal_radial_rate=bool(e*e*(A*A+B*B)<nrate*nrate),
        X_radial_rate=bool(e*A<Xrate),
        initial_radius_from_R123=bool(Q(2553,2000)<R))
    displacement=e*T;radius=R+displacement
    angular=support-displacement-R*Yrate*T
    horizontal_support=support-displacement-R*nrate*T
    horizontal_radius_lower=support-displacement
    Xz=1-Xrate*Xrate*T*T/2
    gates.update(nonzero_horizontal_radius=horizontal_radius_lower>0,
        fixed_r_argument_derivative=angular>radius*radius/4,
        cylindrical_Jacobian=horizontal_support>radius*radius/5,
        positive_height_derivative=Xz>Q(199,200))
    if not all(gates.values()):raise ValueError('an actual R128 embedding budget gate failed: '+str(gates))
    exact_values=dict(
        radial_half_width=T,Riemann_amplitude=M,Riemann_gap_lower=d,target_k_upper=k,
        sqrtE_upper=e,waist_radius_upper=R,waist_support_lower=support,
        A_absolute_upper=A,B_absolute_upper=B,C_absolute_upper=C,
        X_radial_rate_upper=Xrate,Y_radial_rate_upper=Yrate,normal_radial_rate_upper=nrate,
        displacement_from_initial_curve=displacement,horizontal_radius_upper=radius,
        horizontal_radius_lower=horizontal_radius_lower,
        planar_angular_numerator_lower=angular,horizontal_support_lower=horizontal_support,
        Xz_lower=Xz,argument_theta_lower=Q(1,4),cylindrical_Jacobian_lower=Q(1,5))
    doc=dict(kind='R128_actual_R127_waist_annulus_embedding_budget',proved=True,
        embedding_certified=True,closed_surface_complete=False,source_sha256=sha(__file__),
        input_certificate_path=str(args.certificate),input_certificate_sha256=sha(args.certificate),
        original_identities=identities,certified_positive_interval=['0','1/1000'],
        reflected_embedded_annulus=['-1/1000','1/1000'],
        parameter_half_width=data['parameter_half_width'],exact_center_parameter=data['exact_center_parameter'],
        whole_affine_parameter_interval=True,whole_real_angular_circle=True,
        arithmetic='192-bit directed Arb to consume certified endpoints, then Python Fraction exact rational inequalities',
        gates=gates,exact_values={k:str(v) for k,v in exact_values.items()},
        used_geometric_theorems={name:sha(Path('results')/name) for name in
            ('R123-separated-correction-budgets-and-normal-Hessian.md','R126-exact-Codazzi-reconstruction-and-continuation.md')},
        limitations=['This proves embedding only for the actual R127 branch on the stated annulus, using the R128 theorem.',
            'The auxiliary parameter changes the target metric; no common-metric flex family is claimed.',
            'No cap attachment, global closed surface, visible displacement or closed-surface reach is proved here.'])
    args.out.write_text(json.dumps(doc,indent=2)+'\n')
    print(json.dumps(dict(proved=True,gates=gates,exact_values=doc['exact_values']),indent=2))


if __name__=='__main__':main()
