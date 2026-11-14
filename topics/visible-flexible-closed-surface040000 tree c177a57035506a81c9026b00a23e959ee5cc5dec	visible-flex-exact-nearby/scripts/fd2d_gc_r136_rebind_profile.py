"""Reuse the proved R171 exact base packet with another actual bump archive.

The analytic base, all Taylor coefficients/remainders and exact endpoint
stay identical.  New actual delta/support/layout/field identities are read
and checked explicitly.  This is the NEW saved metric when delta changes;
no old field, residual, or body bound is transferred.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json,resource,time,traceback
import numpy as np
from flint import ctx

from fd2d_gc_archive_arrays import identity,load_npz
from fd2d_gc_current_native_interval import rational,rational_pair,bound_record
from fd2d_gc_r136_arb_profile import R136ArbProfile,_encode,ends


def base_payload(profile):
    return dict(bundle=profile.bundle,pieces=profile.pieces,a0=profile.a0,end=profile.end,
        central_length=profile.central_length,join_identities=profile.join_identities,
        precision=profile.precision,order=profile.order)


def base_payload_sha256(profile):
    raw=json.dumps(_encode(base_payload(profile)),sort_keys=True,separators=(',',':'),allow_nan=False).encode()
    return hashlib.sha256(raw).hexdigest()


def rebind_profile(parent_packet,field_arrays,*,expected_parent_sha256):
    profile=R136ArbProfile.from_packet(parent_packet,expected_sha256=expected_parent_sha256)
    parent_definition=profile.definition();before=base_payload_sha256(profile)
    actual=load_npz(field_arrays)
    counts=[int(actual[k]) for k in ('central_parameter_count','tail_parameter_count','profile_count')]
    if min(counts)<1 or len(actual['parameters'])!=sum(counts):
        raise ValueError('The new actual independent layout is malformed')
    mesh=np.asarray(actual['mesh'])
    if (mesh.dtype!=np.float64 or mesh.ndim!=1 or len(mesh)<2
            or not np.all(np.isfinite(mesh)) or not np.all(np.diff(mesh)>0) or mesh[0]!=0):
        raise ValueError('The new actual physical P1 mesh must be finite and increasing from zero')
    # The inherited accurate constructor performs these SAME explicit
    # candidate, fixed-T, independent-layout, support and finite-data checks.
    # Its already-proved base _resolve() is deliberately not repeated.
    profile._bind_bumps(field_arrays)
    if any(left<=profile.central_length or right>=ends(profile.end)[0]
           for left,right in profile.supports):
        raise ValueError('New bump supports must avoid the exact central and cut neighborhoods')
    lower=profile.base_lower+sum((min(F(0),v) for v in profile.delta),F(0))
    if lower<=0:
        raise ValueError('The inherited R136 radius bound does not prove this new target positive')
    profile.inputs['reused_accurate_base_packet']=identity(parent_packet)
    profile.paths['reused_accurate_base_packet']=Path(parent_packet)
    profile.inputs['actual_bump_rebind_source']=identity(__file__)
    profile.paths['actual_bump_rebind_source']=Path(__file__)
    profile.input_binding_sha256=profile._content_binding()
    after=base_payload_sha256(profile)
    if after!=before:raise AssertionError('Rebinding changed an accurate analytic base value or Taylor enclosure')
    provenance=dict(schema='fd2d-R171-exact-base-reuse-with-actual-physical-bumps-v1',
        source=identity(__file__),parent_packet=identity(parent_packet),actual_field=identity(field_arrays),
        parent_input_binding=parent_definition['input_binding_sha256'],
        new_input_binding=profile.input_binding_sha256,
        unchanged_exact_base_payload_sha256=after,analytic_base_and_all_Taylor_remainders_unchanged=True,
        base_integrals_recomputed=False,
        new_exact_delta=[rational_pair(v) for v in profile.delta],
        new_exact_supports=[[rational_pair(v) for v in pair] for pair in profile.supports],
        exact_global_radius_lower=rational_pair(lower),
        physical_target_equal_to_parent_claimed=False,
        parent_saved_field_residual_or_body_bounds_transferred=False,
        tail_domain_decoded_by_scalar_profile=False,
        scope='Actual physical target only; complete angular-tail domain is independently bound by its proper archive reader')
    return profile,provenance


def run(args):
    started=time.monotonic();ctx.prec=args.precision
    out={key:args.out_prefix.with_name(args.out_prefix.name+suffix) for key,suffix in
         (('report','-report.json'),('packet','-packet.json.gz'))}
    args.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    if any(p.exists() for p in out.values()):raise FileExistsError('Use new immutable rebind outputs')
    report=dict(schema='fd2d-R171-actual-profile-rebind-run-v1',source=identity(__file__),
        passed=False,whole_F_J_BVP_body_evaluated=False)
    try:
        before=identity(args.field)
        profile,provenance=rebind_profile(args.parent_packet,args.field,
            expected_parent_sha256=args.parent_sha256)
        report['rebind']=provenance
        report['profile_definition']=profile.definition()
        report['new_packet']=profile.save_packet(out['packet'])
        restored=R136ArbProfile.from_packet(out['packet'],expected_sha256=report['new_packet']['sha256'])
        if (restored.input_binding_sha256!=profile.input_binding_sha256
                or base_payload_sha256(restored)!=provenance['unchanged_exact_base_payload_sha256']
                or restored.delta!=profile.delta or restored.supports!=profile.supports):
            raise AssertionError('Saved new profile did not retain the full exact target identity')
        report['packet_reloaded_with_unchanged_exact_base_and_new_bumps']=True
        # One genuine fixed physical point is enough to exercise the new
        # delta slice; no old 61-piece/130-point check is repeated.
        s=F(7,10);q=restored.physical_box(s,s)
        report['one_actual_new_target_query']=dict(s_exact=rational_pair(s),
            jets={k:bound_record(q[k]) for k in ('a','a_s','a_ss','a_sss','K','K_s')})
        if identity(args.field)!=before:raise AssertionError('Actual new field changed')
        report['actual_field_unchanged']=True;report['passed']=True
    except Exception as exc:
        report['error']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc());raise
    finally:
        report['seconds']=time.monotonic()-started
        report['peak_rss_kib']=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        out['report'].write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
        print(json.dumps(dict(passed=report['passed'],report=str(out['report']),seconds=report['seconds'],
            peak_rss_kib=report['peak_rss_kib'],packet=str(out['packet'])),allow_nan=False))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--parent-packet',type=Path,required=True)
    parser.add_argument('--parent-sha256',required=True)
    parser.add_argument('--field',type=Path,required=True)
    parser.add_argument('--out-prefix',type=Path,required=True)
    parser.add_argument('--precision',type=int,default=256)
    run(parser.parse_args())
