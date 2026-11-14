"""Exact base-packet transport for the actual new R171 physical bumps.

Unlike a decode/re-encode cycle, this version copies the original encoded
analytic base verbatim.  It changes only the explicit field/delta/support
binding.  The original v1 source and its overly strong transport check are
retained as the real first failure, not overwritten.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import argparse,gzip,hashlib,json,resource,time,traceback
from flint import ctx

from fd2d_gc_archive_arrays import identity
from fd2d_gc_current_native_interval import rational_pair,bound_record
from fd2d_gc_r136_arb_profile import R136ArbProfile,_encode
from fd2d_gc_r136_rebind_profile import rebind_profile,base_payload_sha256

BASE_KEYS=('bundle','pieces','a0','end','central_length','join_identities','precision','order')


def encoded_packet(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw)


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def save_rebound_packet(profile,parent_packet,path):
    path=Path(path)
    if path.exists():raise FileExistsError(path)
    old=encoded_packet(parent_packet)
    original_base=canonical_sha({key:old[key] for key in BASE_KEYS})
    profile.inputs['exact_base_transport_source']=identity(__file__)
    profile.paths['exact_base_transport_source']=Path(__file__)
    profile.input_binding_sha256=profile._content_binding()
    data=dict(old)
    for key in ('inputs','delta','supports','field_binding','input_binding_sha256'):
        data[key]=_encode(getattr(profile,key))
    data['definition']=_encode(profile.definition())
    new_base=canonical_sha({key:data[key] for key in BASE_KEYS})
    if new_base!=original_base:raise AssertionError('Encoded analytic base changed')
    raw=(json.dumps(data,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode()
    if path.suffix=='.gz':
        with path.open('wb') as stream:
            with gzip.GzipFile(filename='',fileobj=stream,mode='wb',mtime=0) as out:out.write(raw)
    else:path.write_bytes(raw)
    return dict(**identity(path),uncompressed_bytes=len(raw),uncompressed_sha256=hashlib.sha256(raw).hexdigest(),
        unchanged_encoded_base_sha256=new_base,encoded_analytic_base_identical=True)


def run(args):
    started=time.monotonic();ctx.prec=args.precision
    paths={key:args.out_prefix.with_name(args.out_prefix.name+suffix) for key,suffix in
           (('report','-report.json'),('packet','-packet.json.gz'))}
    args.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    if any(p.exists() for p in paths.values()):raise FileExistsError('Use new immutable output names')
    report=dict(schema='fd2d-R171-actual-profile-exact-base-transport-v2',source=identity(__file__),
        rebind_source=identity(Path(__file__).with_name('fd2d_gc_r136_rebind_profile.py')),
        passed=False,whole_F_J_BVP_body_evaluated=False)
    try:
        before=identity(args.field)
        profile,provenance=rebind_profile(args.parent_packet,args.field,
            expected_parent_sha256=args.parent_sha256)
        report['new_packet']=save_rebound_packet(profile,args.parent_packet,paths['packet'])
        provenance['new_input_binding']=profile.input_binding_sha256
        provenance['exact_base_transport_source']=identity(__file__)
        report['rebind']=provenance
        report['profile_definition']=profile.definition()
        restored=R136ArbProfile.from_packet(paths['packet'],expected_sha256=report['new_packet']['sha256'])
        equal=dict(binding=restored.input_binding_sha256==profile.input_binding_sha256,
            decoded_base=base_payload_sha256(restored)==provenance['unchanged_exact_base_payload_sha256'],
            exact_delta_values=_encode(restored.delta)==_encode(profile.delta),
            exact_support_values=_encode(restored.supports)==_encode(profile.supports))
        if not all(equal.values()):raise AssertionError('A mathematical new profile component changed during exact transport: '+str(equal))
        report['exact_target_transport']=equal
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
        paths['report'].write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
        print(json.dumps(dict(passed=report['passed'],report=str(paths['report']),seconds=report['seconds'],
            peak_rss_kib=report['peak_rss_kib'],packet=str(paths['packet'])),allow_nan=False))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--parent-packet',type=Path,required=True)
    parser.add_argument('--parent-sha256',required=True)
    parser.add_argument('--field',type=Path,required=True)
    parser.add_argument('--out-prefix',type=Path,required=True)
    parser.add_argument('--precision',type=int,default=256)
    run(parser.parse_args())
