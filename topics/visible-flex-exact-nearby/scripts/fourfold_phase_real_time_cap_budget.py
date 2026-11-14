#!/usr/bin/env python3
"""Actual cubic germ-cap fees using only real-time reference image/q gates.

First bound (f_plus-f_minus)/(u-u_cross)^3 at fixed physical theta on the
proved common complex-time disk.  Then substitute the reference only on
real time. No complex-time image condition on the reference is used.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path

from flint import arb, ctx
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_germ_cap_budget import leaf_budget
from fourfold_phase_domain_cover_verify import Closure, Time


def document(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw)if path.suffix=='.gz'else raw)


def lower(row):return arb(row['lower']).lower()
def upper(row):return arb(row['upper']).upper()


def continuity_gate(provenance):
    rows={r['name']:r for r in provenance['scalar_continuity']}
    if (any(rows[n]['minimum_interior_continuity']<4 for n in ['base','raw','shift','mean0','mean1','mean2'])
        or any(rows['height'+str(i)+'_primitive']['minimum_interior_continuity']<5 for i in range(4))):
        raise ValueError('actual scalar continuity does not justify C2 field matching')


def pay_ledger(ledger,physical_image_upper,q_modulus_lower,label_strip,reference_witness):
    """Algebra after the caller's matched complete reference gates."""
    image,m=physical_image_upper,q_modulus_lower
    physical=exact_arb(Fraction(ledger['physical_theta_strip']))
    if not m>0 or not 0<=image<physical:
        raise ValueError('reference real-time q/image gates do not fit the actual field')
    raw=upper(ledger['integrated_h_times_physical_field_difference_upper'])
    amplitude=upper(ledger['uniform_h_times_physical_field_difference_upper'])
    clean={k:v for k,v in ledger.items()if k not in
        ['required_reference_domain','true_small_field_error_proved','interpretation']}
    return dict(**clean,initial_label_strip=str(Fraction(label_strip)),
        actual_reference_image_upper=ball_record(image),actual_reference_q_lower=ball_record(m),
        actual_small_field_cap_error_proved=True,
        integrated_density_cap_error_upper=ball_record((raw/m).upper()),
        uniform_density_cap_error_upper=ball_record((amplitude/m).upper()),
        field_angle_image_margin=ball_record((physical-image).lower()),
        reference_witness=reference_witness,
        reference_complex_time_image_not_required=True,
        interpretation='Fee includes |h| and 1/|Y_x|; add to both the R72 integrated error E and the common M/A allowance.',
        limitations=['Only the adjacent genuine nonturn spline caps in this leaf are paid.',
            'This cap fee does not pay f-P, the main-germ density approximation, or any true-flow error.'])


def real_time_reference_cap(field,reference,image_gate,q_gate):
    """Pipeline API: actual Unified field plus its CompleteReferenceSegment."""
    doc=field.domain;ident=reference.identity
    if not(doc.get('complete')and doc.get('complete_common_span_coverage')
           and doc.get('proved_full_physical_angle_and_complex_time_domain')):
        raise ValueError('complete actual domain for every true germ required')
    expected=dict(retarget_descriptor_sha256=doc['retarget_descriptor_sha256'],
        target_object_sha256=doc['target_object_sha256'],target_root_sha256=doc['target_root_sha256'],
        target_exact_delta_fraction=doc['exact_delta_fraction'],leg=doc['leg'],segment=doc['segment'],
        branch_sign=field.sign,normalized_subspan=doc['normalized_subspan'])
    if any(ident.get(k)!=v for k,v in expected.items()):
        raise ValueError('field and exact finite reference definitions/coordinates differ')
    a,b=map(Time.parse,ident['exact_segment_time_rows']);l,r=map(Fraction,ident['normalized_subspan'])
    if list(map(Time.parse,doc['exact_time_endpoints']))!=[a+(b-a).scale(l),a+(b-a).scale(r)]:
        raise ValueError('actual field and reference exact PiTime endpoints differ')
    if not image_gate.get('complete_real_time_image_proved') or not q_gate.get('q_nonzero_on_complete_real_time_label_strip_proved'):
        raise ValueError('complete real-time image and positive q gates required')
    for gate in [image_gate,q_gate]:
        gid=gate['identity']
        if any(gid.get(k)!=v for k,v in ident.items()if k!='normalized_subspan'):
            raise ValueError('reference gate belongs to a different exact finite object')
        if not gate.get('original_whole_segment_controls'):
            gl,gr=map(Fraction,gid['normalized_subspan'])
            if not gl<=l<r<=gr:raise ValueError('reference gate does not cover this subspan')
    S=Fraction(image_gate['initial_label_strip'])
    if Fraction(q_gate['initial_label_strip'])!=S:
        raise ValueError('image and q gates use different complex label strips')
    package=field.root_package
    if (package.object_sha256!=doc['target_object_sha256']or
        package.certificate_sha256!=doc['target_root_sha256']or
        package.exact_delta!=Fraction(doc['exact_delta_fraction'])):
        raise ValueError('true root and actual field identities differ')
    continuity_gate(package.provenance)
    ledger=leaf_budget(doc,package.root)
    if tuple(map(Fraction,ledger['main_germ_common_span']))!=field.cell:
        raise ValueError('this cap ledger is relative to a different main germ')
    return pay_ledger(ledger,upper(image_gate['physical_theta_image_strip']),
        lower(q_gate['full_real_time_q_real_lower']),S,
        dict(kind='same_exact_reference_real_time_image_and_q',identity=ident,
             image_gate_source_sha256=image_gate['source_sha256'],
             q_gate_source_sha256=q_gate['source_sha256'],
             domain_certificate_path=str(field.domain_path),domain_certificate_sha256=sha(field.domain_path)))


def verified_global_q_report(path,descriptor_path,S):
    """Read the independently completed old forward q gate, without recomputing it."""
    report=document(path);descriptor=document(descriptor_path);identity=report['identity'];S=Fraction(S)
    if not(report.get('complete')and report.get('full_branch_nonzero_proved')
        and identity['retarget_descriptor_sha256']==sha(descriptor_path)):
        raise ValueError('complete same-reference global q gate required')
    leg=identity['leg'];gridrow=descriptor['old_'+leg+'_reference'];grid=document(gridrow['path'])
    if sha(gridrow['path'])!=gridrow['sha256']or identity['manifest_sha256']!=gridrow['sha256']:
        raise ValueError('global q and exact reference time-grid identities differ')
    if identity['source_sha256']!=sha(Path(__file__).with_name('fourfold_reference_derivative_gate.py')):
        raise ValueError('global q proof source bytes changed')
    count=grid['segment_count'];rows=report['segments']
    if identity['first_segment']!=0 or identity['stop_segment']!=count or sorted(r['segment']for r in rows)!=list(range(count)):
        raise ValueError('the global q gate has missing or duplicate segments')
    qrow=descriptor['Q_'+leg];qgrid=document(qrow['path'])
    if sha(qrow['path'])!=qrow['sha256']:raise ValueError('retarget Q manifest changed')
    seen={}
    for row in rows:
        i=row['segment'];bound=row['widths'][str(S)]
        if not bound['positive_real_part_gate_proved']or not lower(bound['real_part_lower'])>0:
            raise ValueError('an actual reference segment has no positive q gate')
        if row['exact_times']!=grid['exact_time_endpoints'][i:i+2]:
            raise ValueError('global q segment time identity differs')
        for key,manifest,mfile in [('base_source',grid,gridrow['path']),('Q_source',qgrid,qrow['path'])]:
            item=row[key];shard=next(v for v in manifest['shards']if v['start_segment']<=i<v['start_segment']+v['segment_count'])
            expected=Path(mfile).parent/shard['path']
            if Path(item['path'])!=expected or item['sha256']!=shard['sha256']:
                raise ValueError('global q coefficient shard differs from the exact definition')
            if str(expected)not in seen:
                if sha(expected)!=shard['sha256']:raise ValueError('actual reference shard bytes changed')
                seen[str(expected)]=shard['sha256']
    bounds=report['global_bounds_on_requested_region'][str(S)]
    actual_lower=min(lower(row['widths'][str(S)]['real_part_lower'])for row in rows)
    actual_upper=max(upper(row['widths'][str(S)]['modulus_upper'])for row in rows)
    if not bounds['every_segment_passed']:
        raise ValueError('the complete q summary is false')
    # The actual per-segment interval endpoints are independently aggregated.
    return report,descriptor,grid,actual_lower,actual_upper,seen


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--cover-index',type=Path,required=True)
    p.add_argument('--descriptor',type=Path,default=Path('data/phase_ring_continuation/step5_retargeted_reference/descriptor.json'))
    p.add_argument('--q-report',type=Path,default=Path('notes/2026-11-12-step5-forward-reference-derivative-gate.json.gz'))
    p.add_argument('--label-strip',default='1/512');p.add_argument('--q-lower',default='3/100')
    p.add_argument('--q-upper',default='21/20');p.add_argument('--bits',type=int,default=192)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args();ctx.prec=args.bits
    index=document(args.cover_index);S=Fraction(args.label_strip)
    qr,descriptor,grid,mactual,Qactual,shards=verified_global_q_report(args.q_report,args.descriptor,S)
    m,Q=exact_arb(Fraction(args.q_lower)),exact_arb(Fraction(args.q_upper))
    if not 0<m<mactual or not Qactual<Q:
        raise ValueError('requested rational q bounds are not implied by actual complete report')
    image=(exact_arb(S)*Q).upper()
    package=index['refined_root'];continuity_gate(package)
    if not(package['proved']and package['object_sha256']==descriptor['target_object']['sha256']
        and package['root_certificate_sha256']==descriptor['target_root']['sha256']
        and index['retarget_descriptor_sha256']==sha(args.descriptor)):
        raise ValueError('actual cap/root/reference target identity differs')
    root=arb(package['refined_root']['ball']);closure=Closure(Path.cwd(),package['object_sha256'],package['root_certificate_sha256'])
    witness=dict(kind='complete_reference_q_derivative_and_vertical_integral_image',
        q_report_path=str(args.q_report),q_report_sha256=sha(args.q_report),
        descriptor_sha256=sha(args.descriptor),full_reference_leg=qr['identity']['leg'],
        exact_label_strip=str(S),q_lower=str(Fraction(args.q_lower)),q_upper=str(Fraction(args.q_upper)),
        image_by_reality_and_vertical_integration=True,physical_image_upper=ball_record(image))
    rows=[];total=arb(0);largest=arb(0)
    for case in index['cases']:
        if not case.get('proved')or case['leg']!=qr['identity']['leg']:
            raise ValueError('global q report does not cover this actual domain case')
        i=case['segment'];a,b=map(Time.parse,grid['exact_time_endpoints'][i:i+2])
        for leaf in case['leaves']:
            doc=closure.domain(leaf['path'],leaf['sha256']);l,r=map(Fraction,leaf['normalized_subspan'])
            if (doc['leg']!=case['leg']or doc['segment']!=i
                or doc['retarget_descriptor_sha256']!=sha(args.descriptor)
                or doc['branch_sign']!=grid['trace_identity']['sign']
                or list(map(Time.parse,doc['exact_time_endpoints']))!=[a+(b-a).scale(l),a+(b-a).scale(r)]):
                raise ValueError('cap domain has different reference coordinates')
            ledger=leaf_budget(doc,root);row=pay_ledger(ledger,image,m,S,witness)
            row.update(domain_certificate_path=leaf['path'],domain_certificate_sha256=leaf['sha256'])
            rows.append(row);total=(total+upper(row['integrated_density_cap_error_upper'])).upper()
            largest=max(largest,upper(row['uniform_density_cap_error_upper'])).upper()
    out=dict(kind='actual_reference_cubic_cap_fees_from_real_time_gates',complete=True,
        source_sha256=sha(__file__),cover_index_path=str(args.cover_index),cover_index_sha256=sha(args.cover_index),
        target_object_sha256=index['target_object_sha256'],target_root_sha256=index['target_root_sha256'],
        exact_delta_fraction=index['exact_delta_fraction'],initial_label_strip=str(S),bits=args.bits,
        q_report_path=str(args.q_report),q_report_sha256=sha(args.q_report),reference_witness=witness,
        independently_reaggregated_q_lower=ball_record(mactual),independently_reaggregated_q_upper=ball_record(Qactual),
        actual_reference_shard_hashes=shards,covered_cases=len(index['cases']),covered_leaves=len(rows),
        ordinary_crossing_pairs=sum(len(r['pairs'])for r in rows),
        integrated_actual_density_cap_error_upper=ball_record(total),
        maximum_leaf_uniform_density_cap_error_upper=ball_record(largest),rows=rows,
        whole_reference_leg_caps=False,reference_complex_time_image_not_required=True,
        domain_dependency_files=sorted(closure.files.values(),key=lambda row:row['path']),
        limitations=['Only the listed completed actual domain cases are included.',
            'This is an actual cap term for the small-field error; the main-germ field/density errors are separate.',
            'The same cap allowance must also enter the common R72 M/A; no true-flow or full return conclusion.'])
    data=(json.dumps(out,indent=2)+'\n').encode()
    if len(data)>1_000_000 and args.out.suffix!='.gz':raise ValueError('gzip required above 1MB')
    data=gzip.compress(data,mtime=0)if args.out.suffix=='.gz'else data
    if len(data)>5_000_000:raise ValueError('split large report')
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_bytes(data)
    print(json.dumps(dict(complete=True,covered_cases=len(index['cases']),pairs=out['ordinary_crossing_pairs'],
        actual_cap_E=out['integrated_actual_density_cap_error_upper'],sha256=sha(args.out))),flush=True)


if __name__=='__main__':main()
