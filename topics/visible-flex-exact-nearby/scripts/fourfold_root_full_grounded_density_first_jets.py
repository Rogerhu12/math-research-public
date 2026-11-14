#!/usr/bin/env python3
"""Complete actual grounded log-density and its two physical first derivatives.

Both real sides and the full complex rho disk are enclosed. Native finite
primitive evaluation retains all angular/radial errors, the moving root and
the whole real affine parameter box. No finite positive canonical chart is
used. This supplies the height-gradient input for a later full-cap consumer.
"""
from __future__ import annotations
import argparse,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_interval import ball_record,vector_dot,vector_cross
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_parameter_germ import provenance
from fourfold_phase_root_fourier_fit import save,sha
from fourfold_subprincipal_root_fields import RootPhaseModel
from fourfold_subprincipal_root_bidisk_domain import true_target_root_disk_jet
from fourfold_subprincipal_root_bidisk_boundary_v2 import complex_boundary_fields


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--root-certificate',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json'))
    p.add_argument('--half-width',type=Fraction,default=Fraction(1,10**9))
    p.add_argument('--radial-radius',type=Fraction,default=Fraction(279,1000000))
    p.add_argument('--physical-strip',type=Fraction,default=Fraction(11,5000))
    p.add_argument('--nodes',type=int,default=512)
    p.add_argument('--angles',type=int,default=1024)
    p.add_argument('--precision',type=int,default=48)
    p.add_argument('--bits',type=int,default=256)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists() or a.out.suffix!='.gz':raise ValueError('a new gzip report is required')
    if not 0<a.half_width<=Fraction(1,10**9):raise ValueError('outside the actual parameter family')
    if a.angles<a.nodes or a.angles&(a.angles-1) or a.precision<12:
        raise ValueError('complete finite layout is required')
    if sha(a.object)!='91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848':
        raise ValueError('the original actual object changed')
    ctx.prec,ctx.cap=a.bits,10;tick=time.monotonic()
    model=RootPhaseModel(a.object,a.half_width,a.root_certificate,a.physical_strip,nodes=a.nodes,refine_steps=3)
    target=model.target;target.angles=a.angles;ctx.cap=a.precision
    R,S=exact_arb(a.radial_radius),exact_arb(a.physical_strip)
    if not 0<R<model.budget['E_radius']<model.budget['radial_radius']:
        raise ValueError('true analytic radial domains are not nested')
    cf,radius,Efinite,_,_=target.target(model.root,model.scale,None)
    Q,Qrho,kreport=true_target_root_disk_jet(target,radius,Efinite,model.budget,model.scale,R)
    geom,fees=complex_boundary_fields(target,cf,model.budget,model.scale,R,S)
    report=dict(kind='actual_full_root_grounded_log_density_first_jets',complete=False,proved=False,
        source_sha256=sha(__file__),identity=provenance(target,a.object),
        object_path=str(a.object),object_sha256=sha(a.object),
        root_certificate_path=str(a.root_certificate),root_certificate_sha256=sha(a.root_certificate),
        root=ball_record(model.root),rho_radius=str(a.radial_radius),physical_angle_strip=str(a.physical_strip),
        nodes=a.nodes,angles=a.angles,precision=a.precision,bits=a.bits,
        curvature_disk=kreport,complete_geometry_fees=fees,cells=[],
        grounded_density='Ucal=Q*Fz^4*area2^2/support^4',
        physical_radial_convention='rho=t(p)-r; X=F_r and Cr=(F_theta cross F_r)_r',
        exact_first_derivatives={
            'rho':'Qrho/Q - 4*Xz/Fz - 4*(C dot Cr)/area2 + 4*(Cr dot F)/support',
            'theta':'4*Ftheta_z/Fz + 4*(C dot Ctheta)/area2 - 4*(Ctheta dot F)/support'},
        dependencies={n:sha(Path(__file__).with_name(n)) for n in (
            'fourfold_subprincipal_root_fields.py','fourfold_subprincipal_root_bidisk_domain.py',
            'fourfold_subprincipal_root_bidisk_boundary_v2.py','fourfold_phase_beta_interval.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_beta_parameter_germ.py',
            'fourfold_phase_root_cauchy_frame_ci_v1.py','fourfold_phase_root_potential_complex_strip.py',
            'fourfold_native_series_fft.py')})
    bounds={k:[] for k in ('log_Ucal','log_Ucal_rho','log_Ucal_theta')}
    mins={k:[] for k in ('Q','Fz','area2','support')}
    for j in range(a.angles):
        F,X,Frr,Y,Frt,Ftt=[g[j] for g in geom]
        C=vector_cross(Y,X)
        Cr1,Cr2=vector_cross(Frt,X),vector_cross(Y,Frr)
        Ct1,Ct2=vector_cross(Ftt,X),vector_cross(Y,Frt)
        Cr=[Cr1[i]+Cr2[i] for i in range(3)]
        Ct=[Ct1[i]+Ct2[i] for i in range(3)]
        area,support=vector_dot(C,C),vector_dot(C,F)
        den={'Q':Q,'Fz':F[2],'area2':area,'support':support}
        if any(not z.real>0 for z in den.values()):
            raise ValueError('true complete logarithm denominator is not in the right half-plane')
        L=Q.log()+4*F[2].log()+2*area.log()-4*support.log()
        Lrho=Qrho/Q-4*X[2]/F[2]-4*vector_dot(C,Cr)/area+4*vector_dot(Cr,F)/support
        Ltheta=4*Y[2]/F[2]+4*vector_dot(C,Ct)/area-4*vector_dot(Ct,F)/support
        vals={'log_Ucal':abs(L).upper(),'log_Ucal_rho':abs(Lrho).upper(),
              'log_Ucal_theta':abs(Ltheta).upper()}
        if any(not v.is_finite() for v in vals.values()):raise ValueError('nonfinite complete density derivative')
        for k,v in vals.items():bounds[k].append(v)
        for k,v in den.items():mins[k].append(v.real.lower())
        report['cells'].append(dict(index=j,complete_moduli={k:ball_record(v) for k,v in vals.items()},
            positive_real_denominator_lower={k:ball_record(v.real.lower()) for k,v in den.items()}))
        if (j+1)%128==0:
            report['seconds']=time.monotonic()-tick;save(a.out,report)
            print(dict(cells=j+1,total=a.angles,seconds=report['seconds']),flush=True)
    report.update(complete=True,proved=True,
        complete_moduli={k:ball_record(max(v)) for k,v in bounds.items()},
        positive_real_denominator_lower={k:ball_record(min(v)) for k,v in mins.items()},
        coverage='Every closed upper angular boundary cell and the entire complex rho disk; Schwarz reflection supplies the lower boundary, then successive positive-real and maximum principles give the full bidisk. The same real moving root and entire affine parameter box are retained.',
        full_canonical_height_gradient_bound_proved=False,full_positive_cap_source_contact_proved=False,
        scope='Actual first jets of the grounded physical log-density on the complete complex root bidisk. Canonical inverse/Delta derivatives and full-cap/contact are separate consumers.',
        seconds=time.monotonic()-tick)
    save(a.out,report)
    if a.out.stat().st_size>5_000_000:raise ValueError('complete report exceeds the repository single-file limit')
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),moduli=report['complete_moduli'],seconds=report['seconds']),flush=True)


if __name__=='__main__':main()
