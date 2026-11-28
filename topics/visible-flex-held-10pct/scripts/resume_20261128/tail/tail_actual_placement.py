#!/usr/bin/env python3
"""Prove absolute placement of the same actual tail, collar and plain disks.

The actual finite prefix cut zero mode, the entire native perturbation mean,
and the identical R58 true height integral fix the vertical origin. Reuse
the old actual geometric derivative bounds; do not rerun their polynomials.
The old broad-height conditional allocation flags remain unchanged.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import time

import numpy as np
import tail_metric_complete_supplement_v2 as supplement
from geometry_disk_guard import install as install_disk_guard

original = supplement.original
ref, write, checked_plain = supplement.ref, supplement.write, supplement.checked_plain
SUPPLEMENT_SHA = 'ad10604269a322d33f26f5e9e926d68d06b6ca8f836437ecf0ed585384abd115'


def actual_height(args, bundle, chain, manifest, index, constants):
    cut = json.loads(args.cut_summary.read_text())
    if (cut.get('prefix_metric_certified') is not True
            or cut.get('prefix_geometry_certified') is not True
            or cut['geometry_bundle_sha256'] != ref(args.geometry_bundle)['sha256']
            or Path(cut['geometry_bundle']).resolve() != args.geometry_bundle.resolve()
            or not cut['cut_definition']['full_height_identity_checked']
            or not cut['cut_definition']['all_original_tail_modes_retained']):
        raise ValueError('The same actual complete cut prefix certificate is required')
    for path, digest in cut['source_hashes'].items():
        if ref(path)['sha256'] != digest:
            raise ValueError('A bound actual cut source changed')
    table_ref = dict(path=cut['table_report'], sha256=cut['table_report_sha256'])
    table = checked_plain(table_ref)
    if table['defining_jets'] != cut['defining_jets']:
        raise ValueError('Cut and prefix use different literal defining jets')
    if ref(table['source_run'])['sha256'] != cut['source_run_sha256']:
        raise ValueError('The actual prefix source run changed')
    source = json.loads(Path(table['source_run']).read_text())
    source_ref = ref(table['source_run'])
    packet = original.checked(bundle['accepted_packet'])
    identity = bundle['height_identity']
    reference = original.checked(identity['reference'])
    referenced = reference
    for key in identity['reference_key'].split('.'):
        referenced = referenced[key]
    H = source['raw_return']['candidate_H']
    if (identity['factor'] != 1 or referenced != H
            or packet['request']['height'] != H
            or packet['response']['checkpoint']['cutHeight'] != H
            or packet['config']['modes'] != source['modes']
            or reference.get('source_run') != source_ref):
        raise ValueError('Actual prefix and entire unscaled tail H must coincide')
    port = original.checked(bundle['source_port'])
    if (port['parameters'] != source['physical_tail_parameters']
            or any(manifest['physicalParameters'].get(k) != v
                   for k,v in port['parameters'].items())):
        raise ValueError('Prefix and full tail physical backgrounds differ')
    if ref(cut['defining_jets']['path']) != cut['defining_jets']:
        raise ValueError('The actual finite prefix defining jets changed')
    with np.load(cut['defining_jets']['path'], allow_pickle=False) as data:
        pm, hm = data['planar_modes'], data['height_modes']
        jets = data['jets']
        zero = np.flatnonzero(hm == 0)
        if (len(zero) != 1 or jets.dtype != np.dtype('float64')
                or jets.shape[0] != 3 or jets.shape[1] != len(pm)+len(hm)
                or not np.all(np.isfinite(jets[:,:,-1]))
                or np.any(data['lift_jets'][:,:,-1] != 0)
                or np.any(data['chart_jets'][:,:,-1] != 0)):
            raise ValueError('A complete literal zero-chart cut two-jet is required')
        zcut = Q.from_float(float(jets[0,len(pm)+int(zero[0]),-1]))
    if zcut != Q(cut['cut_definition']['finite_mean_height_at_cut_exact']):
        raise ValueError('Cut proof and exact finite-prefix mean differ')
    files = {entry['stage']:entry for entry in manifest['files']}
    stage0 = supplement.selected_data(bundle, manifest, constants, files[0])
    node = stage0['nodes'][-1]
    P, hm = len(stage0['planarModes']), stage0['heightModes']
    if hm.count(0) != 1:
        raise ValueError('The complete tail mean mode is absent or duplicated')
    mean = Q.from_float(node['coefficients'][0][P+hm.index(0)])
    if (mean != Q.from_float(node['meanPerturbation'])
            or mean != Q.from_float(chain['mean_chain'][0][0])):
        raise ValueError('Cut mean is not the entire same native mean chain')
    radius = checked_plain(ref(args.radius_identity))
    Rc = Q.from_float(constants['parameters']['rCut'])
    if (not radius['radius_chart_identity_proved']
            or not radius['complete_bundle_validated']
            or not radius['all_stage_spectra_and_shared_means_revalidated']
            or radius['geometry_bundle'] != ref(args.geometry_bundle)
            or radius['source_run'] != source_ref
            or radius['original_canonical_index'] != bundle['canonical_node_index']
            or Q(radius['reparameterization_delta_exact']) != 0
            or Q(radius['saved_cut_radius_exact']) != Rc
            or Q(radius['physical_cut_radius_exact']) != Rc
            or Q.from_float(node['radiusJS']) != Rc):
        raise ValueError('The same complete tail physical-R identity is required')
    for key in ('source', 'constants', 'normalization'):
        if ref(radius[key]['path']) != radius[key]:
            raise ValueError('The true radius/background identity source changed')
    oracle = supplement.v1.Q060TrueBackgroundOracle(args.constants, args.normalization_certificate)
    cut_primitive = oracle.primitives(0, 8, Q(1))
    cut_R = oracle.bounds(cut_primitive['r'])
    cut_drop = oracle.bounds(cut_primitive['height_drop_to_cut'])
    if not (Q(cut_R['lower_exact']) <= Rc <= Q(cut_R['upper_exact'])
            and Q(cut_drop['lower_exact']) == Q(cut_drop['upper_exact']) == 0):
        raise ArithmeticError('The same true primitive cut anchor failed')
    norm = json.loads(args.normalization_certificate.read_text())
    height = norm['exact_height']
    hlo,hhi = Q(height['lower_exact']),Q(height['upper_exact'])
    zb = zcut+mean
    if not 0 < hlo <= hhi or zb <= 0:
        raise ValueError('Positive actual upper cut and true total height required')
    top = [zb+hlo, zb+hhi]
    rho = original.sqrt_upper(Rc*Rc+top[1]*top[1])
    support = zb/original.sqrt_upper(1+Q(41,100)**2)
    return dict(
        status='actual_same_tail_absolute_height_and_background_placement_proved',
        cut_certificate=ref(args.cut_summary), cut_table_report=table_ref,
        literal_prefix_defining_jets=cut['defining_jets'], prefix_source_run=source_ref,
        cut_width_exact=cut['cut_definition']['cut_width_exact'],
        tail_cut_stage=files[0], entire_mean=bundle['mean_chain'],
        complete_height_identity=identity, accepted_packet=bundle['accepted_packet'],
        physical_R_identity=ref(args.radius_identity),
        exact_finite_prefix_cut_height=str(zcut), exact_entire_tail_cut_mean=str(mean),
        exact_background_cut_height_zb=str(zb),
        exact_true_height_integral_interval=list(map(str,(hlo,hhi))),
        exact_upper_plain_disk_height_interval=list(map(str,top)),
        upper_plain_disk_height_display=[original.lower(top[0]),original.upper(top[1])],
        background_radius_upper=original.upper_row(rho),
        background_support_lower=original.lower_row(support),
        background_slope_global_upper_exact='41/100',
        background_slope_nonnegative_and_height_monotone_source='R58 identical true definition',
        oracle_provenance=oracle.provenance, true_cut_primitive_R=cut_R,
        true_cut_primitive_height_drop=cut_drop,
        entire_true_height_integral_recomputed=False,
        same_proved_normalization_and_integral_reused=True,
        cylinder_half_length_exact='0', marker_amplitude_exact='0',
        full_mean_preserved=True, finite_field_or_target_changed=False), rho, support


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('geometry-bundle','constants','normalization-certificate','cut-summary','radius-identity','outdir'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--original-summary',type=Path,action='append',required=True)
    p.add_argument('--disk-reserve-mib',type=int,default=128)
    args=p.parse_args()
    if args.disk_reserve_mib<128 or ref(supplement.__file__)['sha256']!=SUPPLEMENT_SHA:
        raise ValueError('Keep the complete selected-stage validator and disk reserve')
    out=args.outdir.resolve();out.mkdir(parents=True,exist_ok=False)
    guard=install_disk_guard(out,args.disk_reserve_mib*1024**2)
    started=time.monotonic()
    bundle,chain,manifest,index,constants=original.validate_inputs(
        args.geometry_bundle,args.constants,args.normalization_certificate)
    if not bundle.get('complete_finite_C2_stage_chain') or not bundle.get('all_stages_exported'):
        raise ValueError('A true complete common-C2 tail definition is required')
    height,rho0,support0=actual_height(args,bundle,chain,manifest,index,constants)
    height.update(source=ref(__file__),geometry_bundle=ref(args.geometry_bundle),
                  constants=ref(args.constants),normalization=ref(args.normalization_certificate),
                  mathematical_sources=[ref(supplement.__file__),ref(supplement.v1.__file__),ref(original.__file__)],
                  disk_guard=guard)
    hp=out/'absolute-height.json';write(hp,height)
    print(json.dumps(dict(event='true_absolute_tail_height',height=ref(hp),
                          pole_height=height['upper_plain_disk_height_display'],
                          background_radius_upper=height['background_radius_upper']['upper'],
                          background_support_lower=height['background_support_lower']['lower'])),flush=True)
    originals=[]
    for path in args.original_summary:
        while True:
            value=json.loads(path.read_text())
            if value['status']!='running':break
            print(json.dumps(dict(event='waiting_for_original_geometric_bounds',summary=str(path),
                                  actual_stages=len(value['stages']))),flush=True)
            time.sleep(10)
        reference=ref(path);value=checked_plain(reference)
        if (value['status']=='failed' or value['source']!=ref(original.__file__)
                or value['accepted_packet']!=bundle['accepted_packet']
                or value['original_mean_chain']!=bundle['mean_chain']
                or value['constants']!=ref(args.constants)
                or value['normalization']!=ref(args.normalization_certificate)):
            raise ValueError('The unchanged original geometric execution did not finish on this field')
        originals.append((reference,value))
    files={entry['stage']:entry for entry in manifest['files']}
    receipts={};deep=None
    for reference,value in originals:
        for row in value['stages']:
            if row['stage'] in receipts and receipts[row['stage']]['certificate']!=row['certificate']:
                raise ValueError('Conflicting original stage receipts')
            receipts[row['stage']]=row
        if 'deep_collar' in value:
            candidate=value['deep_collar']
            if deep is not None and deep['certificate']!=candidate['certificate']:
                raise ValueError('Conflicting original complete deep collars')
            deep=candidate
    if set(receipts)!=set(files) or deep is None:
        raise ValueError('All actual finite stages and the true deep collar are required')
    rows=[]
    def append(label,proof,eta,pos,K,old_gate):
        normal=original.normal_difference_bound(eta)
        if normal is None or not 0<=eta<1 or pos<0 or K<0:
            raise ArithmeticError('Original differential bounds do not control the normal')
        radius=rho0+pos
        support=support0-rho0*normal-pos
        rows.append(dict(component=label,original_geometric_certificate=proof,
                         original_K_below_10_allocation_passed=old_gate,
                         first_jet_upper_exact=str(eta),position_upper_exact=str(pos),
                         normal_difference_upper=original.upper_row(normal),
                         radius_upper=original.upper_row(radius),support_lower=original.lower_row(support),
                         principal_curvature_upper=original.upper_row(K),
                         radius_below_1_34=radius<Q(67,50),support_above_0_087=support>Q(87,1000),
                         curvature_below_12_3=K<Q(123,10)))
    for stage,entry in sorted(files.items()):
        receipt=receipts[stage];old=checked_plain(receipt['certificate'])
        data=supplement.selected_data(bundle,manifest,constants,entry)
        if (old['data']!=entry or old['stage']!=stage or old['map_hash']!=entry['mapHash']
                or old['spans']!=len(data['nodes'])-1):
            raise ValueError('Original geometric bound belongs to another actual finite stage')
        append(dict(stage=stage),receipt['certificate'],Q(old['normalized_first_jet_upper']['upper_exact']),
               Q(old['position_perturbation_upper']['upper_exact']),
               Q(old['principal_curvature_upper']['upper_exact']),old['curvature_allocation_passed'])
    deep_row=checked_plain(deep['certificate'])
    if (deep_row['stage_data']!=files[index['finite_stage_count']-1]
            or deep_row['canonical_deep_value_sha256']!=index['deep_node']['value_sha256']
            or not deep_row['C2_outer_match_exact'] or not deep_row['C2_inner_zero_two_jet_exact']
            or deep_row['true_background_definition_sha256']!=height['oracle_provenance']['definition_sha256']):
        raise ValueError('Deep collar has different actual common two-jets or true background')
    append('same_actual_zero_jet_deep_collar',deep['certificate'],
           Q(deep_row['normalized_first_jet_upper']['upper_exact']),
           Q(deep_row['position_perturbation_upper']['upper_exact']),
           Q(deep_row['principal_curvature_upper']['upper_exact']),deep_row['curvature_allocation_passed'])
    append('unchanged_rotational_cuff_and_plain_disks',None,Q(0),Q(0),Q(8),True)
    component_path=out/'component-bounds.json';write(component_path,rows)
    rmax=max(Q(row['radius_upper']['upper_exact']) for row in rows)
    smin=min(Q(row['support_lower']['lower_exact']) for row in rows)
    kmax=max(Q(row['principal_curvature_upper']['upper_exact']) for row in rows)
    passed=rmax<Q(67,50) and smin>Q(87,1000) and kmax<Q(123,10)
    result=dict(status='same_actual_tail_absolute_placement_and_global_curvature_certified' if passed else 'same_actual_tail_absolute_bounds_recorded',
                source=ref(__file__),absolute_height=ref(hp),component_bounds=ref(component_path),
                original_geometric_summaries=[reference for reference,value in originals],
                finite_stage_count=len(files),original_literal_span_count=sum(entry['nodes']-1 for entry in files.values()),
                complete_deep_collar_and_plain_disks_included=True,
                radius_upper=original.upper_row(rmax),support_lower=original.lower_row(smin),
                principal_curvature_upper=original.upper_row(kmax),
                radius_below_1_34=rmax<Q(67,50),support_above_0_087=smin>Q(87,1000),
                curvature_below_12_3=kmax<Q(123,10),
                old_K_below_10_allocation_failures=[row['component'] for row in rows if not row['original_K_below_10_allocation_passed']],
                old_conditional_placement_records_modified=False,
                original_geometric_polynomials_recomputed=False,
                source_mean_or_field_or_metric_target_changed=False,
                phase_and_upper_lower_reflection_invariant=True,
                cylinder_half_length_exact='0',marker_amplitude_exact='0',
                whole_tail_metric_claimed=False,whole_closed_surface_claimed=False,
                readme_completion_claimed=False,seconds=time.monotonic()-started)
    write(out/'summary.json',result)
    print(json.dumps(dict(status=result['status'],summary=ref(out/'summary.json'),
                          radius_upper=result['radius_upper']['upper'],
                          support_lower=result['support_lower']['lower'],
                          curvature_upper=result['principal_curvature_upper']['upper'])),flush=True)


if __name__=='__main__':
    main()
