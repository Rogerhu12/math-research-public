#!/usr/bin/env python3
"""Complete whole-angle/time domain documents from saved true coefficient balls.

No ``inherited`` claim is used for a larger disk. Every selected actual germ
gets a fresh outer modulus, complete angular/time complements, denominator
gate and curvature branch. Failed germs leave the expanded document unusable;
the caller may then keep its original proved R3 domain.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path
import time
from flint import arb, ctx

from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_unified_scalar_time_circle import UnifiedScalarTimeCircleField, exact_time
from fourfold_saved_invariant_time_extension import extension
from fourfold_forward_density_pipeline import read, save


DEFAULT_DESCRIPTOR=Path('data/phase_ring_continuation/step5_retargeted_reference/descriptor.json')


def _passed(doc):
    return bool(doc.get('complete') and doc.get('complete_common_span_coverage')
                and doc.get('proved_full_physical_angle_and_complex_time_domain'))


def _center_scale(doc):
    a,b=map(exact_time,doc['exact_time_endpoints'])
    return (a+b)/2,(b-a)/2


def resolve_retained_norms(path,doc,index):
    """Only exact +/- time reflection is allowed; shifted disks are rejected."""
    original=doc
    current_path,current,index=Path(path),doc,int(index)
    links=[];time_sign=1;radial_sign=1;seen=set()
    while True:
        digest=sha(current_path)
        if digest in seen:raise ValueError('cyclic inherited domain source')
        seen.add(digest)
        if not _passed(current):raise ValueError('retained norms come from an incomplete domain')
        for key in ('target_object_sha256','target_root_sha256','retarget_descriptor_sha256','exact_delta_fraction'):
            if current[key]!=original[key]:raise ValueError('retained coefficient exact object differs')
        row=current['germs'][index]
        if not row.get('passed'):raise ValueError('retained coefficient germ failed')
        if 'invariant_bounds' in row:
            if any('retained_DFT_coefficient_norms' not in row['invariant_bounds'][name]
                   for name in ('D','M','W')):
                raise ValueError('saved domain lacks the actual retained coefficient balls')
            source=dict(path=str(current_path),sha256=digest,germ_index=index,
                angle_nodes=int(row.get('retained_angle_nodes',current['angles'])),
                cutoff=int(row.get('retained_cutoff',current['cutoff'])),
                norm_physical_strip=row.get('retained_norm_physical_strip',current['physical_theta_strip']),
                exact_source_time_endpoints=current['exact_time_endpoints'],
                source_common_span=row['common_span'],
                source_u_equals_signed_current_u=time_sign,
                source_radius_equals_signed_current_radius=radial_sign,links=links)
            return row,source
        inherit=row.get('inherited')
        if not inherit:raise ValueError('no retained coefficient source is available')
        parent_path=Path(inherit['path'])
        if sha(parent_path)!=inherit['sha256']:raise ValueError('inherited domain source hash changed')
        parent=read(parent_path);parent_index=int(inherit['germ_index'])
        child_c,child_h=_center_scale(current)
        parent_c,parent_h=_center_scale(parent)
        reflect=-1 if inherit.get('reflected_time_and_germ') else 1
        if reflect*child_c!=parent_c:
            raise ValueError('shifted inherited time centers need a separately paid coefficient translation')
        if reflect*child_h==parent_h:flip=1
        elif reflect*child_h==-parent_h:flip=-1
        else:raise ValueError('scaled inherited time germs are not reused without a paid transform')
        child_cell=tuple(map(Fraction,row['common_span']))
        parent_cell=tuple(map(Fraction,parent['germs'][parent_index]['common_span']))
        expected=child_cell if reflect==1 else (-child_cell[1],-child_cell[0])
        if parent_cell!=expected:raise ValueError('inherited radial reflection does not match the actual germ')
        links.append(dict(child_path=str(current_path),child_sha256=digest,
            parent_path=str(parent_path),parent_sha256=inherit['sha256'],
            exact_center_and_scale_checked=True,time_coordinate_sign=flip,radial_reflection_sign=reflect))
        time_sign*=flip;radial_sign*=reflect
        current_path,current,index=parent_path,parent,parent_index


def expand_domain(path,out,R=6,S=8,*,descriptor=DEFAULT_DESCRIPTOR,nodes=512,bits=192,
                  radial_degree=64,models=None):
    """Return and save a complete new domain doc; no false fallback promotion.

    ``models`` may map germ indices to already initialized original-domain
    scalar samplers. Their original shared budgets are restored after each
    fresh outer calculation, so original-radius point sampling stays unchanged.
    """
    path,out,descriptor=map(Path,(path,out,descriptor))
    R,S=Fraction(R),Fraction(S)
    if not 1<R<S:raise ValueError('strictly nested enlarged time radii required')
    ctx.prec=bits;start,cpu=time.monotonic(),time.process_time()
    original=read(path)
    if not _passed(original):raise ValueError('an original fully proved domain is required')
    if sha(descriptor)!=original['retarget_descriptor_sha256']:
        raise ValueError('actual reference descriptor differs')
    narrow=Fraction(original['physical_theta_strip'])
    wide=Fraction(original.get('wider_physical_theta_strip','1/32'))
    required=[tuple(map(Fraction,c)) for c in original['required_common_spans']]
    observed=[tuple(map(Fraction,row['common_span'])) for row in original['germs']]
    if observed!=required or len(set(observed))!=len(observed):
        raise ValueError('all actual required germs must be retained once and in order')
    keys=('target_object_sha256','target_root_sha256','retarget_descriptor_sha256','R59_sha256',
          'time_grid_manifest_sha256','exact_delta_fraction','leg','segment','branch_sign',
          'exact_time_endpoints','normalized_subspan','sharp_real_germ_cover','required_common_spans',
          'angles','cutoff','time_order','independent_root_nodes','depth')
    result={key:original[key] for key in keys if key in original}
    result.update(kind='new_complete_true_time_domain_from_saved_retained_coefficient_norms',
        complete=False,proved_full_physical_angle_and_complex_time_domain=False,
        complete_common_span_coverage=False,source_sha256=sha(__file__),
        original_domain_path=str(path),original_domain_sha256=sha(path),
        time_radius=str(R),larger_time_radius=str(S),physical_theta_strip=str(narrow),
        wider_physical_theta_strip=str(wide),bits=bits,primitive_nodes=nodes,
        radial_degree=radial_degree,germs=[],
        coefficient_reuse_contract='identical exact time center and scale up to signed reflection only',
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_saved_invariant_time_extension.py','fourfold_phase_unified_scalar_time_circle.py',
            'fourfold_phase_sine_time_geometry.py','fourfold_phase_full_angle_time_domain.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_beta_affine.py')})
    save(out,result)
    for index,cell in enumerate(required):
        try:
            saved,provenance=resolve_retained_norms(path,original,index)
            if Fraction(provenance['norm_physical_strip'])<narrow:
                raise ValueError('saved retained norms do not cover the requested angle strip')
            model=(models[index] if models is not None and index in models else
                UnifiedScalarTimeCircleField(descriptor,path,germ=index,nodes=nodes,
                    root_nodes=nodes,radial_degree=radial_degree))
            if model.identity()['domain_sha256']!=sha(path) or model.cell!=cell:
                raise ValueError('provided sampler belongs to a different original domain/germ')
            row=extension(model,saved,provenance['angle_nodes'],provenance['cutoff'],R,S,narrow,wide)
            anchor=dict(saved['anchor'])
            anchor['u_anchor']=ball_record(provenance['source_u_equals_signed_current_u']
                                           *arb(saved['anchor']['u_anchor']['ball']))
            anchor['actual_germ_span']=list(map(str,cell))
            anchor['source_anchor_provenance']=provenance
            row.update(common_span=list(map(str,cell)),anchor=anchor,
                retained_coefficient_provenance=provenance,
                retained_angle_nodes=provenance['angle_nodes'],retained_cutoff=provenance['cutoff'],
                retained_norm_physical_strip=str(narrow),
                complete_new_angular_and_time_complements_paid=True)
        except Exception as exc:
            row=dict(common_span=list(map(str,cell)),passed=False,
                failure=type(exc).__name__+': '+str(exc))
        result['germs'].append(row);save(out,result)
    passed=all(row['passed'] for row in result['germs'])
    result.update(complete=True,complete_common_span_coverage=passed,
        proved_full_physical_angle_and_complex_time_domain=passed,
        wall_seconds=time.monotonic()-start,cpu_seconds=time.process_time()-cpu,
        limitations=['Every new larger disk is proved afresh; no inherited shrinking-domain label is used.',
            'Only the stated exact affine object, reference time scale, branches and actual germ union.',
            'This supplies actual field domains, not a trajectory residual or a full return certificate.',
            'If any germ fails, keep the original proved domain; this expanded document grants no whole-leaf field.'])
    save(out,result)
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--domain',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--R',type=Fraction,default=Fraction(6));p.add_argument('--S',type=Fraction,default=Fraction(8))
    p.add_argument('--descriptor',type=Path,default=DEFAULT_DESCRIPTOR)
    p.add_argument('--nodes',type=int,default=512);p.add_argument('--bits',type=int,default=192)
    p.add_argument('--radial-degree',type=int,default=64)
    a=p.parse_args();d=expand_domain(a.domain,a.out,a.R,a.S,descriptor=a.descriptor,
        nodes=a.nodes,bits=a.bits,radial_degree=a.radial_degree)
    print({'complete':d['complete'],'proved':d['proved_full_physical_angle_and_complex_time_domain'],
           'germs':[{'passed':r['passed'],'D_lower':r.get('D_lower'),
                     'f':r.get('true_field_moduli',{}).get('f'),'failure':r.get('failure')}
                    for r in d['germs']],
           'cpu_seconds':d['cpu_seconds'],'wall_seconds':d['wall_seconds']},flush=True)


if __name__=='__main__':main()
