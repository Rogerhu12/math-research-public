"""Exact whole-angle initial compatibility for the actual saved current field.

The initial curve is the declared exact same-g central curvature family,
with exact material-weighted means.  Saved raw coefficients stay unchanged.
Only the finite coefficient discrepancy is enclosed; no curve/body ODE or
sampled angular maximum is used.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import argparse,gzip,json,resource,time,traceback
from flint import arb,ctx

from fd2d_gc_archive_arrays import identity
from fd2d_gc_current_native_interval import aq,rational,rational_pair,bound_record
from fd2d_gc_r136_arb_profile import _moment
from fd2d_gc_current_primitive_interval_v2 import norm_upper


def initial_compatibility(field):
    """Return R119 d0/k0 and an optional true whole-angle D0,u bound."""
    parts,reader,atlas=field.parts,field.reader,field.atlas
    if parts.mesh[0]!=0 or reader.central_parameter_count!=parts.K:
        raise ValueError('This exact central family requires its declared physical origin/layout')
    if (rational(reader.seed_weight_definition['start'])<0
            or atlas.entry_start<=0 or min(atlas.blend)<=0
            or field.interior.tail_start<=0 or parts.trace_start<=0):
        raise ValueError('The complete initial affine/atlas functions have a different central contract')
    origin=field.profile.physical_box(F(0),F(0),side='right')
    if not origin['a_s'].is_zero():
        raise ValueError('The declared exact central cylinder must have a_s(0)=0')
    mean_path=atlas.paths['means'];packed=Path(mean_path).read_bytes()
    data=json.loads(gzip.decompress(packed) if Path(mean_path).suffix=='.gz' else packed)
    if (data['exact_moment_report']['sha256']!=atlas.inputs['moments']['sha256']
            or not data['source_moment_intervals_remain_valid']):
        raise ValueError('Exact central means refer to another seed')
    rows=data['rows'][:parts.K]
    if len(rows)!=parts.K or [r['angular_mode'] for r in rows]!=list(range(2,2*parts.K+1,2)):
        raise ValueError('Missing exact material-weighted central means')
    mu=[_moment(r['material_weighted_mean']) for r in rows]
    central=parts.parameters[reader.central_slice]
    raw=tuple(rational(v) for v in reader.values[0])
    cosine_difference=tuple(raw[j]-central[j-1] for j in range(1,parts.K+1))
    sine=raw[parts.e:parts.d]
    constant=aq(raw[0])+sum((aq(c)*m for c,m in zip(central,mu)),arb(0))
    n_upper=(abs(constant).upper()+aq(sum(map(abs,cosine_difference),F(0)))).upper()
    m_upper=aq(sum(map(abs,sine),F(0))).upper()
    a0=atlas.a0
    d0=norm_upper((a0*n_upper,a0*m_upper,origin['a_s']))
    # Curve tangent derivative is a0*kappa*N.  The rotation-invariant
    # matrix derivative includes F0,u, even when the coefficient error is
    # constant; it is not silently reported as zero.
    nxi=aq(sum((2*j*abs(v) for j,v in enumerate(cosine_difference,1)),F(0)))
    mxi=aq(sum((2*j*abs(v) for j,v in enumerate(sine,1)),F(0)))
    derivative_error=norm_upper((a0*nxi/atlas.h_lower,a0*mxi/atlas.h_lower,arb(0)))
    if reader.base_kind=='balanced_seed':base_max=1/atlas.rho_lower
    elif reader.base_kind=='circle':base_max=1/a0.lower()
    else:raise ValueError('Undeclared exact central base')
    curvature_max=(base_max+sum((aq(abs(c))*(1+abs(m).upper()) for c,m in zip(central,mu)),arb(0))).upper()
    d0u=(a0.upper()*curvature_max*d0+derivative_error).upper()
    return dict(schema='fd2d-current-exact-central-compatibility-v1',source=identity(__file__),
        full_field_binding_sha256=field.binding_sha256,
        actual_field=identity(reader.arrays_path),exact_means=identity(mean_path),
        exact_moments=atlas.inputs['moments'],accurate_profile_binding=field.profile.input_binding_sha256,
        base_kind=reader.base_kind,central_count=parts.K,
        exact_initial_curve='Declared central family kappa=base+sum c_j(cos(2j*xi)-mu_j_true), gamma_u=a0*T',
        exact_initial_frame='F0=(fixed unit transverse direction,T,N), right handed, T_u=a0*kappa*N',
        exact_raw_n_mean=rational_pair(raw[0]),
        raw_cosine_minus_central_exact=[rational_pair(v) for v in cosine_difference],
        raw_initial_m_exact=[rational_pair(v) for v in sine],
        raw_initial_l_exact=[rational_pair(v) for v in raw[parts.d:]],
        n_field_minus_exact_curve_constant=bound_record(constant),
        n_error_uniform_upper=bound_record(n_upper),m_uniform_upper=bound_record(m_upper),
        exact_cosine_match=all(v==0 for v in cosine_difference),
        initial_m_exact_zero=all(v==0 for v in sine),
        initial_l_exact_zero=all(v==0 for v in raw[parts.d:]),
        initial_D_operator_upper=bound_record(d0),initial_C_norm_upper=bound_record(arb(0)),
        initial_Du_operator_upper=bound_record(d0u),initial_Cu_norm_upper=bound_record(arb(0)),
        auxiliary_exact_curve_abs_curvature_upper=bound_record(curvature_max),
        formulas=dict(d0='a0*sup sqrt((n_field-n_curve)^2+m_field^2); a_s(0)=0',
            k0='0 exactly for the declared accurate arclength initial curve/frame',
            d0u='a0*sup|kappa_curve|*d0 + a0*sup sqrt((Delta_n)_u^2+(m_field)_u^2)'),
        whole_angle_bound=True,angular_sampling_used=False,
        actual_initial_curve_numeric_quadrature_error_transferred=False,
        frame_body_BVP_or_full_F_J_computed=False,global_embedding_or_surface_certificate=False)


def run(args):
    start=time.monotonic();ctx.prec=args.precision
    out=args.out_prefix.with_name(args.out_prefix.name+'-report.json')
    if out.exists():raise FileExistsError('Do not overwrite an actual compatibility report')
    out.parent.mkdir(parents=True,exist_ok=True)
    report=dict(schema='fd2d-current-central-compatibility-actual-run-v1',passed=False,source=identity(__file__),
        native_definition=identity(args.native_definition),profile_packet=identity(args.profile_packet))
    try:
        from fd2d_gc_current_accurate_domain_arb import AccurateDomainCurrentFieldArb
        field=AccurateDomainCurrentFieldArb(args.native_definition,args.profile_packet,
            profile_packet_sha256=report['profile_packet']['sha256'],precision=args.precision)
        before=identity(field.reader.arrays_path)
        report['bound']=initial_compatibility(field)
        if identity(field.reader.arrays_path)!=before:raise AssertionError('Actual field changed')
        report['actual_field_unchanged']=True;report['passed']=True
    except Exception as exc:
        report['error']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc());raise
    finally:
        report['seconds']=time.monotonic()-start
        report['peak_rss_kib']=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
        print(json.dumps(dict(passed=report['passed'],report=str(out),seconds=report['seconds'],
                             peak_rss_kib=report['peak_rss_kib']),allow_nan=False))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);root=Path(__file__).resolve().parent.parent
    p.add_argument('--native-definition',type=Path,required=True)
    p.add_argument('--profile-packet',type=Path,default=root/'notes/2026-11-12-fd2d-metric-r136-arb-profile-01-packet.json.gz')
    p.add_argument('--out-prefix',type=Path,required=True);p.add_argument('--precision',type=int,default=256)
    run(p.parse_args())
