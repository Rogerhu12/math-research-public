#!/usr/bin/env python3
"""Exact symmetry-reduced correction of the actual waist two-jet.

The initial target E(r) dr^2 + a(r)^2 dtheta^2 is kept fixed.  F(0,theta)
is unchanged, F_r is set to sqrt(E) e_z, and F_rr is set to
-a a'' F_thetatheta / |F_thetatheta|^2.  This is an actual smooth local
two-jet, not a solution on an unlisted radial neighborhood.  The report
encloses its complete angular and affine-parameter dependence, including
the original infinite primitive tail.  At the waist the updated metric,
its first jet, and its Gauss curvature agree exactly with the fixed target,
so the true R117 source is exactly zero there.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, ctx

import fourfold_phase_two_jet_newton_source as source
from fourfold_phase_two_jet_newton_source import (
    Box, CBox, zeros, arb_box, square_box, real_interval, common_cells,
    load_definition, save, record, sha, dot, cross, box_abs_upper,
    range_record, sqrt_box_arb,
)
from fourfold_phase_newton_source_centered import CenteredSource, CenteredPolynomial


def euclidean_square(v):
    return sum((square_box(x) for x in v), Box(0.))


def norm_upper(v):
    return arb(float(np.max(euclidean_square(v).hi))).sqrt().upper()


def scalar_range(v):
    return range_record(Box(float(np.min(v.lo)), float(np.max(v.hi))))


def zero_by_symmetry(v, name):
    if not np.all((v.lo <= 0) & (v.hi >= 0)):
        raise ValueError('exact waist symmetry not enclosed: ' + name)
    return Box(np.zeros_like(v.lo))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--half-width',type=Fraction,default=Fraction(1,10**9))
    p.add_argument('--nodes',type=int,default=512)
    p.add_argument('--angles',type=int,default=16384)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=192;ctx.cap=4
    source.Polynomial=CenteredPolynomial
    target=CenteredSource(args.object,args.half_width,args.nodes,args.angles)
    cuts=common_cells(target);i=bisect_right(cuts,Fraction(0))-1
    target.set_cell(cuts[i],cuts[i+1]);start=time.monotonic()
    FF,YY,a,EF,EY,tail=target.first_two_jets(acb(real_interval(Fraction(0),Fraction(0))))
    Fp=[[target.lift(FF[j][:,k],EF[j][0]) for k in range(3)] for j in range(3)]
    Yp=[[target.lift(YY[j][:,k],EY[j]) for k in range(3)] for j in range(2)]
    frequency=np.asarray(target.frequency)
    zz=YY[0]*CBox(0.,Box(frequency[:,None]))
    zz[:,0]=zz[:,0]-YY[0][:,1];zz[:,1]=zz[:,1]+YY[0][:,0]
    ezz=(EF[0][2]+2*EF[0][1]+EF[0][0]).upper()
    Zp=[target.lift(zz[:,k],ezz) for k in range(3)]
    F=[[v.angular_cells(args.angles) for v in row] for row in Fp]
    Y=[[v.angular_cells(args.angles) for v in row] for row in Yp]
    Z=[v.angular_cells(args.angles) for v in Zp]
    a0,a1,a2=[v.to_acb().real for v in a[:3]]
    E=dot(Fp[1],Fp[1]).mean();E1=2*dot(Fp[1],Fp[2]).mean()
    if not a0>0 or not E>0:raise ValueError('positive fixed target unresolved')
    if not a1.contains(0) or not E1.contains(0):raise ValueError('even target first jet unresolved')
    # Every overwritten zero is supplied by the exact R33 waist reflection.
    zero_by_symmetry(F[0][2],'F_z');zero_by_symmetry(F[2][2],'F_rr,z')
    zero_by_symmetry(Y[0][2],'F_theta,z');zero_by_symmetry(Z[2],'F_thetatheta,z')
    for k in (0,1):
        zero_by_symmetry(F[1][k],'F_r,horizontal')
        zero_by_symmetry(Y[1][k],'F_rtheta,horizontal')
    F[0][2]=Box(0.);F[2][2]=Box(0.);Y[0][2]=Box(0.);Z[2]=Box(0.)
    for k in (0,1):F[1][k]=Box(0.);Y[1][k]=Box(0.)
    if not np.all(F[1][2].lo>0):raise ValueError('positive waist radial orientation unresolved')
    Z2=euclidean_square(Z)
    if not np.all(Z2.lo>0):raise ValueError('nonvanishing waist planar curvature unresolved')
    tangent_orthogonality=sum((Y[0][k]*Z[k] for k in range(3)),Box(0.))
    if not np.all((tangent_orthogonality.lo<=0)&(tangent_orthogonality.hi>=0)):
        raise ValueError('exact unit speed orthogonality not enclosed')
    Ebox=arb_box(E);abox=arb_box(a0);aa2=arb_box(a0*a2)
    rootE=arb_box(E.sqrt());F1new=[Box(0.),Box(0.),rootE]
    F2new=[-aa2*zk/Z2 for zk in Z]
    V1=[F1new[k]-F[1][k] for k in range(3)]
    V2=[F2new[k]-F[2][k] for k in range(3)]
    V12=[-Y[1][k] for k in range(3)]
    # All fixed-target Christoffel symbols vanish at the even waist.
    H11=[v/Ebox for v in V2]
    H12=[v/(abox*rootE) for v in V12]
    hsq=euclidean_square(H11)+2*euclidean_square(H12)
    grad=[v/rootE for v in V1]
    oldC=cross(Y[0],F[1]);oldC2=euclidean_square(oldC)
    normalH11=sum((oldC[k]*H11[k] for k in range(3)),Box(0.))/sqrt_box_arb(oldC2)
    # R79/R123 use the ORIGINAL induced metric, not the fixed target g0.
    # At the waist g_F=diag(b(theta)^2,a^2), Gamma^r_{rtheta}=b_theta/b.
    # Its original orthonormal Hessians are E/b^2 times the g0 values.
    b=F[1][2];b2=square_box(b);target_to_original=Ebox/b2
    oldgrad=[v/b for v in V1]
    oldH11=[v/b2 for v in V2]
    oldH12=[-rootE*v/(abox*b2) for v in Y[1]]
    oldhsq=euclidean_square(oldH11)+2*euclidean_square(oldH12)
    oldnormalH11=sum((oldC[k]*oldH11[k] for k in range(3)),Box(0.))/sqrt_box_arb(oldC2)
    # The mixed Hessian is vertical whereas the normal is horizontal, so its
    # normal projection, and the entire theta-theta Hessian, are exactly zero.
    newC=cross(Y[0],F1new);newG=euclidean_square(newC)
    newL=dot(newC,F2new);newN=dot(newC,Z)
    Knew=newL*newN/square_box(newG)
    K0=arb_box(-a2/(a0*E))
    directKdefect=Knew-K0
    # This direct interval check is only a redundant arithmetic enclosure;
    # the exact curvature cancellation is used in the mathematical result.
    if not np.all((directKdefect.lo<=0)&(directKdefect.hi>=0)):
        raise ValueError('exact updated curvature identity not enclosed')
    definition,_,_,center=load_definition(args.object)
    doc=dict(kind='actual_fixed_target_exact_waist_two_jet_correction',complete=True,
        whole_real_angular_circle=True,whole_radial_domain=False,
        exact_radial_interval=['0','0'],exact_scalar_germ=list(map(str,target.cell)),
        exact_center_parameter=str(center),exact_half_width=str(args.half_width),
        object_sha256=sha(args.object),source_sha256=sha(__file__),
        centered_source_sha256=sha(Path(__file__).with_name('fourfold_phase_newton_source_centered.py')),
        origin_sha256=definition['origin_inputs']['sha256'],direction_sha256=definition['direction']['sha256'],
        original_fixed_target=dict(E=record(E),Eprime_exact='0',a=record(a0),aprime_exact='0',asecond=record(a2),K0=record(-a2/(a0*E))),
        positivity=dict(old_F_r_z=scalar_range(F[1][2]),waist_F_thetatheta_squared=scalar_range(Z2)),
        fixed_target_metric_correction=dict(V_C0_exact='0',material_gradient_C0_upper=record(norm_upper(grad)),
            radial_partial_C0_upper=record(norm_upper(V1)),
            material_H_rr_C0_upper=record(norm_upper(H11)),
            material_H_rtheta_C0_upper=record(norm_upper(H12)),
            material_H_thetatheta_C0_exact='0',
            material_Hilbert_Schmidt_Hessian_C0_upper=record(arb(float(np.max(hsq.hi))).sqrt().upper()),
            normal_projected_material_H_rr_C0_upper=record(box_abs_upper(normalH11)),
            normal_projected_material_H_rtheta_C0_exact='0',
            normal_projected_material_H_thetatheta_C0_exact='0',
            radial_second_partial_C0_upper=record(norm_upper(V2)),
            mixed_partial_C0_upper=record(norm_upper(V12))),
        original_induced_metric_correction=dict(V_C0_exact='0',
            target_to_original_Hessian_ratio=scalar_range(target_to_original),
            material_gradient_C0_upper=record(norm_upper(oldgrad)),
            material_H_rr_C0_upper=record(norm_upper(oldH11)),
            material_H_rtheta_C0_upper=record(norm_upper(oldH12)),
            material_H_thetatheta_C0_exact='0',
            material_Hilbert_Schmidt_Hessian_C0_upper=record(arb(float(np.max(oldhsq.hi))).sqrt().upper()),
            normal_projected_material_H_rr_C0_upper=record(box_abs_upper(oldnormalH11)),
            normal_projected_material_H_rtheta_C0_exact='0',
            normal_projected_material_H_thetatheta_C0_exact='0'),
        exact_updated_waist=dict(metric_defect='0',first_metric_jet_defect='0',Gauss_curvature_defect='0',
            R117_Newton_source='0',held_waist_positions_unchanged=True),
        redundant_direct_updated_curvature_defect_C0_upper=record(box_abs_upper(directKdefect)),
        complete_primitive_error=record(tail),angles=args.angles,primitive_nodes=args.nodes,bits=192,
        wall_seconds=time.monotonic()-start,
        limitations=['The specified waist two-jet has a smooth symmetry-preserving local extension; no positive radial extent is certified here.',
            'No global correction, low/mid/tail inverse, regular-mean return condition, or Newton convergence is claimed.',
            'Fixed-target and original-induced material norms are reported separately; R79/R123 use original_induced_metric_correction.',
            'This is an exact local nonlinear jet replacement, not a certified global Newton step.'])
    save(args.out,doc)
    print({'out':str(args.out),'original_induced_metric_correction':doc['original_induced_metric_correction'],'wall_seconds':doc['wall_seconds']},flush=True)


if __name__=='__main__':main()
