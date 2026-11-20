#!/usr/bin/env python3
"""Pure-report attribution of one actual R676 radial refinement batch.

Reads JSON and hashes bytes only. No field modules, arrays, oracle calls,
scientific experiments or solver calls. Distinguishes the common-parent
functional from the changed fine rule and leaves unreported new-only maxima
unpaid. One fine direction never certifies sustained refinement convergence.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path


CHAIN_SHA = '4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'
REFINEMENT_SHA = '2e8ae99813c105982b10b896606538c1c42baf0abf089457412b32e265d4411a'
FINE_SHA = '100e57c66e1f5b592fe22570c6c7894a6ab75e082b714edfff42514098d5c622'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def get(value, *keys, default=None):
    for key in keys:
        if not isinstance(value, dict) or key not in value:
            return default
        value = value[key]
    return value


def arg(command, flag):
    if not isinstance(command, list) or command.count(flag) != 1:
        return None
    index = command.index(flag)
    return command[index+1] if index+1 < len(command) else None


def read(path):
    if path is None:
        return {}, dict(state='no_declared_path', path=None)
    path = Path(path).resolve()
    try:
        raw = path.read_bytes()
    except FileNotFoundError:
        return {}, dict(state='not_returned', path=str(path))
    record = dict(path=str(path), bytes=len(raw), sha256=digest(raw))
    try:
        value = json.loads(raw)
        if not isinstance(value, dict):
            raise ValueError('Expected a JSON object')
    except (ValueError, UnicodeDecodeError) as exc:
        return {}, dict(**record, state='unreadable_snapshot', error=str(exc))
    return value, dict(**record, state='readable')


def finite(value):
    return (not isinstance(value, bool) and isinstance(value, (int, float))
            and math.isfinite(value))


def clean(value):
    if isinstance(value, float) and not math.isfinite(value):
        return dict(nonfinite_report_value=repr(value))
    if isinstance(value, dict):
        return {key:clean(item) for key,item in value.items()}
    if isinstance(value, (list,tuple)):
        return [clean(item) for item in value]
    return value


def binding(record, conditions):
    failures = [reason for passed,reason in conditions if not passed]
    if record.get('state') != 'readable':
        failures.insert(0, record.get('state','not_returned'))
    return dict(bound=not failures, reasons=failures)


def same_parameters(value):
    return all(get(value,key) == number for key,number in dict(p=8,epsilon=.001,scale=.05).items())


def comparison(left, right, left_name, right_name):
    if not (left.get('comparable') and right.get('comparable')):
        return dict(scope='identical parent finite functional', paid=False,
                    reason='Both actual identity-bound common-grid reports have not returned')
    a, b = left.get('mean_Phi'), right.get('mean_Phi')
    if not finite(a) or not finite(b):
        return dict(scope='identical parent finite functional', paid=False,
                    reason='A reported common Phi is absent or nonfinite')
    return dict(scope='identical parent finite functional', paid=True,
        before=left_name, after=right_name, before_mean_Phi=a, after_mean_Phi=b,
        difference_after_minus_before=b-a, decreased=b<a,
        ratio_after_over_before=b/a if a else None,
        arithmetic='Ordinary arithmetic on reported finite summaries, not an outward certificate',
        changed_fine_rule_Phi_used=False, convergence_claimed=False)


def common_entry(common, bound, parent, parent_record, field_sha, label):
    spectral=get(parent,'current','spectral') or get(parent,'initial','spectral',default={})
    parent_N=get(parent,'N')
    parent_rows=(get(parent,'all_full_rows')//(3*parent_N)
                 if isinstance(parent_N,int) and parent_N>0
                 and isinstance(get(parent,'all_full_rows'),int) else None)
    reasons=[]
    for condition, reason in (
        (bound, 'The field/report identity is not bound'),
        (get(common,'complete_parent_row_scope') is True,'The complete parent row scope is not returned'),
        (get(common,'parent_rows') == parent_rows,'The parent radial row count differs'),
        (get(common,'full_angles') == parent_N,'The parent full angular grid differs'),
        (get(common,'exact_parent_scalar_carriers_used') is True,'The literal parent a carriers are not confirmed'),
        (get(common,'exact_parent_angle_carriers_used') is True,'The literal parent angle carriers are not confirmed'),
        (get(common,'legacy_fraction') == .5,'The parent mixture differs'),
        (same_parameters(get(common,'positive_spectral_parameters',default={})), 'The fixed p/epsilon/scale differ'),
        (get(common,'normalization_denominator') == get(spectral,'normalization'), 'The parent normalization differs')):
        if not condition:reasons.append(reason)
    return dict(stage=label,field_sha256=field_sha,parent_report_sha256=parent_record.get('sha256'),
        comparable=not reasons,reasons=reasons,mean_Phi=get(common,'mean_Phi'),
        maximum_relative_Gram=get(common,'maximum_relative_Gram'),worst_Gram=get(common,'worst_Gram'),
        weighted_frobenius_sse=get(common,'weighted_frobenius_sse'),
        normalization_denominator=get(common,'normalization_denominator'),
        rows_read=get(common,'rows_read'),parent_rows=get(common,'parent_rows'),
        full_angles=get(common,'full_angles'),
        evaluation='Actual current field on the same parent rows/angles/weights/literal a; ordinary binary evaluation')


def position_counts(value, *, manifest):
    if not value:
        return dict(paid=False,reason='Position JSON has not returned')
    keys=('curvature_points','radius_points') if manifest else ('final_curvature_memory','final_radius_memory')
    if any(key not in value for key in keys):
        return dict(paid=False,reason='The complete two position lists are not present')
    protected=set()
    def points(items):
        out=set()
        for item in items:
            if isinstance(item,dict):
                if not all(k in item for k in ('cell','u','phi')):
                    raise ValueError('A final memory position has no complete cell/u/phi')
                key=(int(item['cell']),float(item['u']),float(item['phi']))
                if item.get('protected'):protected.add(key)
            else:
                if not isinstance(item,list) or len(item)!=3:
                    raise ValueError('A manifest position is not a numeric triple')
                key=(int(item[0]),float(item[1]),float(item[2]))
            if not finite(key[1]) or not finite(key[2]):
                raise ValueError('A position is nonfinite')
            out.add(key)
        return out
    curvature, radius = (points(value[key]) for key in keys)
    if manifest:protected.update(points(value.get('protected_curvature_points',[])))
    return dict(paid=True,curvature_numeric_tuples=len(curvature),radius_numeric_tuples=len(radius),
        union_numeric_tuples=len(curvature|radius),protected_curvature_numeric_tuples=len(protected),
        protected_subset_of_curvature=protected<=curvature,
        scope='Distinct literal numeric tuples; no rounding or geometric-symmetry quotient; no values inherited')


def new_only(refinement, ref_bound, after_fine=False, fine_stats=None):
    if after_fine:
        maximum=get(fine_stats,'max_relative_gram')
        return dict(paid=False,maximum=None,worst=None,naturally_complete_bound_fine=ref_bound,
            finite_same_evaluation_upper=maximum if ref_bound and finite(maximum) else None,
            reason='The full-QP report has no new-only row maximum or worst point; its common read uses a separate arithmetic path, so all-minus-common inference is not used',
            continuous_maximum_certified=False,additional_field_read_performed=False)
    value=get(refinement,'readout',default={})
    common=get(value,'common_parent_grid',default={})
    all_max=get(value,'maximum_relative_Gram');old_max=get(common,'maximum_relative_Gram')
    conditions=dict(identity_bound=ref_bound,
        finite_readout_returned=get(refinement,'finite_readout_performed') is True,
        all_old_rows_mapped=get(refinement,'observations','inherited_row_mapping_complete') is True,
        inherited_literal_a_identical=get(refinement,'observations','inherited_scalar_carriers_bitwise_equal') is True,
        parent_row_scope_complete=get(common,'complete_parent_row_scope') is True,
        literal_parent_angles_identical=get(common,'exact_parent_angle_carriers_used') is True,
        full_N_unchanged=get(refinement,'angular_refinement','source_full_angles')
                        ==get(refinement,'angular_refinement','refined_full_angles'),
        same_shared_array_formula_source=get(refinement,'source_sha256')==REFINEMENT_SHA,
        finite_reported_maxima=finite(all_max) and finite(old_max))
    if all(conditions.values()) and all_max>old_max:
        return dict(paid=True,maximum=all_max,worst=get(value,'worst_Gram'),
            reason='In this same streaming evaluation, all-grid max exceeds the complete inherited-row max; hence an all-grid maximizer lies among genuinely new observation rows',
            conditions=conditions,
            scope='Finite binary evaluation only: shared E/F/G arrays, identical literal a and angles, identical residual/norm formula, unchanged N',
            continuous_maximum_certified=False,additional_field_read_performed=False)
    return dict(paid=False,maximum=None,worst=None,finite_same_evaluation_lower=0.,
        finite_same_evaluation_upper=all_max if ref_bound and finite(all_max) else None,
        conditions=conditions,
        reason='New-only maxima were not separately recorded; the available summaries do not identify them',
        continuous_maximum_certified=False,additional_field_read_performed=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--chain-plan',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    for key in ('parent-report','refinement-report','fine-report','common-report','fine-plan','refined-manifest'):
        p.add_argument('--'+key,type=Path)
    a=p.parse_args()
    chain,chain_file=read(a.chain_plan)
    ref_command=get(chain,'commands','refinement');fine_command=get(chain,'commands','fine_solve')
    ref_dir=arg(ref_command,'--outdir');fine_dir=arg(fine_command,'--outdir');fine_work=arg(fine_command,'--work')
    parent,parent_file=read(a.parent_report or get(chain,'inputs','parent_report','path'))
    refinement,ref_file=read(a.refinement_report or (Path(ref_dir)/'refinement-report.json' if ref_dir else None))
    fine,fine_file=read(a.fine_report or (Path(fine_dir)/'report.json' if fine_dir else None))
    common,common_file=read(a.common_report or (Path(fine_dir)/'common-parent-grid.json' if fine_dir else None))
    fine_plan,fine_plan_file=read(a.fine_plan or (Path(fine_work)/(Path(fine_dir).name+'-fine-command.json')
                                                if fine_work and fine_dir else None))
    manifest,manifest_file=read(a.refined_manifest or get(refinement,'outputs','permanent_locations','path'))
    chain_binding=binding(chain_file,[(get(chain,'source_sha256')==CHAIN_SHA,'Unknown chain producer source')])
    parent_binding=binding(parent_file,[
        (chain_binding['bound'],'Unbound chain identity'),
        (parent_file.get('sha256')==get(chain,'inputs','parent_report','sha256'),'Parent report SHA mismatch'),
        (get(parent,'complete') is True,'Parent has no natural complete state'),
        (get(parent,'final_bundle_sha256')==get(chain,'inputs','bundle','sha256'),'Parent final bundle mismatch'),
        (get(parent,'source_sha256')==get(chain,'parent_driver','sha256'),'Parent driver identity mismatch'),
        (get(parent,'observation_carrier_sha256')==get(chain,'inputs','carrier','sha256'),'Parent carrier mismatch')])
    ref_binding=binding(ref_file,[
        (parent_binding['bound'],'Unbound actual parent'),
        (get(refinement,'source_sha256')==REFINEMENT_SHA,'Unknown refinement producer'),
        (get(refinement,'inputs','bundle','sha256')==get(parent,'final_bundle_sha256'),'Refinement starts from another field'),
        (get(refinement,'inputs','carrier','sha256')==get(parent,'observation_carrier_sha256'),'Refinement parent carrier mismatch'),
        (get(refinement,'inputs','node_report','sha256')==get(chain,'inputs','node_report','sha256'),'Parent symbolic node report mismatch'),
        (get(refinement,'inputs','scalar_input','sha256')==get(chain,'inputs','scalar_input','sha256'),'Original scalar input mismatch'),
        (get(refinement,'transfer','radial_factor')==2,'This chain declares one radial bisection'),
        (get(refinement,'transfer','parent_J')==get(parent,'J'),'Parent radial shape mismatch'),
        (get(refinement,'transfer','parent_M')==get(parent,'M')
         and get(refinement,'transfer','refined_M')==get(parent,'M'),'The declared radial-only batch changed M'),
        (get(refinement,'angular_refinement','source_full_angles')==get(parent,'N')
         and get(refinement,'angular_refinement','refined_full_angles')==get(parent,'N'),'The declared radial-only batch changed N')])
    fine_plan_binding=binding(fine_plan_file,[
        (get(fine_plan,'source_sha256')==FINE_SHA,'Unknown fine launcher'),
        (get(fine_plan,'refinement_report','sha256')==ref_file.get('sha256'),'Fine launcher uses another refinement report')])
    fine_binding=binding(fine_file,[
        (ref_binding['bound'] and fine_plan_binding['bound'],'Unbound refinement/fine command'),
        (get(fine,'source_sha256')==get(fine_plan,'derived_driver','sha256'),'Actual fine driver mismatch'),
        (get(fine,'bundle_sha256')==get(refinement,'outputs','bundle','sha256'),'Fine starts from another transferred seed'),
        (get(fine,'observation_carrier_sha256')==get(refinement,'outputs','carrier','sha256'),'Fine uses another observation carrier'),
        (get(fine,'M')==get(refinement,'transfer','refined_M'),'Fine M mismatch'),
        (get(fine,'J')==get(refinement,'transfer','refined_J'),'Fine J mismatch'),
        (get(fine,'N')==get(refinement,'angular_refinement','refined_full_angles'),'Fine N mismatch')])
    fine_complete=fine_binding['bound'] and get(fine,'complete') is True and isinstance(get(fine,'final_bundle_sha256'),str)
    common_binding=binding(common_file,[
        (fine_complete,'Fine has no bound natural final state'),
        (get(common,'source_sha256')==REFINEMENT_SHA,'Unknown common-grid reader'),
        (get(common,'refinement_report','sha256')==ref_file.get('sha256'),'Common grid belongs to another refinement'),
        (get(common,'bundle','sha256')==get(fine,'final_bundle_sha256'),'Common grid evaluates another fine field')])
    manifest_binding=binding(manifest_file,[
        (ref_binding['bound'],'Unbound refinement'),
        (manifest_file.get('sha256')==get(refinement,'outputs','permanent_locations','sha256'),'Refined manifest SHA mismatch'),
        (get(manifest,'carrier_sha256')==get(refinement,'outputs','carrier','sha256'),'Refined manifest carrier mismatch'),
        (get(manifest,'bundle_sha256')==get(refinement,'outputs','bundle','sha256'),'Refined manifest seed mismatch')])
    parent_stats=get(parent,'current') or get(parent,'initial',default={})
    parent_spectral=get(parent_stats,'spectral',default={})
    before=dict(stage='actual_parent_final',field_sha256=get(parent,'final_bundle_sha256'),
        comparable=parent_binding['bound'] and same_parameters(parent_spectral)
                   and get(parent,'radial_weights','legacy_fraction')==.5,
        mean_Phi=get(parent_spectral,'phi_normalized'),maximum_relative_Gram=get(parent_stats,'max_relative_gram'),
        weighted_frobenius_sse=get(parent_spectral,'original_weighted_sse'),
        normalization_denominator=get(parent_spectral,'normalization'),
        scope='Actual complete parent report on its own original complete finite functional')
    transferred=common_entry(get(refinement,'readout','common_parent_grid',default={}),
        ref_binding['bound'] and get(refinement,'finite_readout_performed') is True,
        parent,parent_file,get(refinement,'outputs','bundle','sha256'),'after_transfer_before_fine_solve')
    solved=common_entry(get(common,'common_parent_grid',default={}),common_binding['bound'],
        parent,parent_file,get(fine,'final_bundle_sha256'),'actual_fine_final')
    fine_stats=get(fine,'current') or get(fine,'initial',default={})
    try:manifest_counts=position_counts(manifest,manifest=True)
    except (ValueError,TypeError,KeyError) as exc:manifest_counts=dict(paid=False,reason=str(exc))
    if not manifest_binding['bound']:manifest_counts.update(paid=False,identity_reasons=manifest_binding['reasons'])
    try:final_counts=position_counts(fine,manifest=False)
    except (ValueError,TypeError,KeyError) as exc:final_counts=dict(paid=False,reason=str(exc))
    if not fine_complete:final_counts.update(paid=False,reason='The bound fine final memory has not naturally returned')
    directions=get(fine,'directions',default=[])
    scalar_bounds=get(refinement,'transfer','continuous_sixjet_rounding_difference')
    result=dict(schema='same-fixed-g-radial-refinement-pure-report-attribution-v1',
        source_sha256=digest(Path(__file__).read_bytes()),
        execution_provenance=dict(chain=get(chain,'execution'),refinement=get(refinement,'execution'),
            scope='Only execution fields explicitly returned by these bound producers; no parent run is invented'),
        reports=dict(chain=chain_file,parent=parent_file,refinement=ref_file,fine_command=fine_plan_file,
                     fine=fine_file,common_parent_grid=common_file,refined_manifest=manifest_file),
        identity=dict(chain=chain_binding,parent=parent_binding,refinement=ref_binding,
                      fine_command=fine_plan_binding,fine=fine_binding,common=common_binding,manifest=manifest_binding),
        stages=dict(
            chain=dict(scientific_execution_started=get(chain,'scientific_execution_started'),
                scientific_execution_complete=get(chain,'scientific_execution_complete'),
                active_stage=get(chain,'active_stage'),failed_stage=get(chain,'failed_stage'),
                subprocess_returncode=get(chain,'subprocess_returncode'),
                process_liveness_observed=False),
            parent=dict(naturally_complete=parent_binding['bound']),
            transfer=dict(coordinate_report_returned=ref_binding['bound'],
                finite_readout_returned=ref_binding['bound'] and get(refinement,'finite_readout_performed') is True,
                nonlinear_solve_performed=get(refinement,'nonlinear_solve_performed')),
            fine=dict(report_returned=fine_binding['bound'],naturally_complete=fine_complete,
                recorded_directions=len(directions),accepted_directions=sum(d.get('accepted') is True for d in directions),
                stopped_before_linear_iteration=get(fine,'stopped_before_linear_iteration'),
                initial_curvature_filter=get(fine,'initial_curvature_filter'),final_curvature_filter=get(fine,'final_curvature_filter')),
            common_read=dict(returned=common_binding['bound'],complete_parent_scope=solved['comparable'])),
        common_parent_functional=dict(before_transfer=before,after_transfer=transferred,after_fine=solved,
            transfer_change=comparison(before,transferred,'parent','transferred_seed'),
            fine_solve_change=comparison(transferred,solved,'transferred_seed','fine_final'),
            total_change=comparison(before,solved,'parent','fine_final')),
        native_fine_rule=dict(after_transfer=dict(mean_Phi=get(refinement,'readout','mean_Phi'),
            maximum_relative_Gram=get(refinement,'readout','maximum_relative_Gram'),
            worst_Gram=get(refinement,'readout','worst_Gram')),
            after_fine=dict(natural_final_returned=fine_complete,
                mean_Phi=get(fine_stats,'spectral','phi_normalized') if fine_complete else None,
                maximum_relative_Gram=get(fine_stats,'max_relative_gram') if fine_complete else None),
            latest_reported_fine_state=dict(identity_bound=fine_binding['bound'],
                natural_final_returned=fine_complete,
                mean_Phi=get(fine_stats,'spectral','phi_normalized'),
                maximum_relative_Gram=get(fine_stats,'max_relative_gram')),
            parent_coarse_Phi_subtraction_performed=False,
            scope='Different rule from the parent; these numbers are retained without cross-layer subtraction'),
        genuinely_new_observations=dict(after_transfer=new_only(refinement,ref_binding['bound']),
            after_fine=new_only(refinement,fine_complete,after_fine=True,
                               fine_stats=fine_stats if fine_complete else None)),
        transfer_rounding=dict(paid_from_bound_report=ref_binding['bound'] and isinstance(scalar_bounds,dict),
            continuous_sixjet_difference=scalar_bounds,
            inserted_jet_error_upper_per_derivative=get(refinement,'transfer','inserted_jet_error_upper_per_derivative'),
            ideal_restriction_equals_parent=get(refinement,'transfer','ideal_restricted_field_equals_parent'),
            literal_field_equality_certified=get(refinement,'transfer','literal_stored_field_equality_certified'),
            field_or_interval_recomputed=False),
        positions=dict(parent_report_union=get(chain,'complete_parent_location_union'),
            caller_manifest_count=len(get(chain,'caller_manifests',default=[])),
            refined_complete_manifest=manifest_counts,
            actual_transfer_locations_read=get(refinement,'readout','permanent_locations_read'),
            transfer_invalid_point_count=get(refinement,'readout','invalid_point_count'),
            fine_final_memory=final_counts,geometric_values_inherited=False),
        next_frequency_layer=dict(
            actual_parent='Bind the next layer to this actual fine final bundle/report and complete final location union',
            unchanged=['original scalar input and accurate S/R/a','exact current symbolic radial nodes',
                'material metric and parameter range','fixed lambda and symbolic eta endpoints',
                'caps/markers and original affine core/cap interfaces','all inherited physical observation locations',
                'p/epsilon/scale and an explicitly common comparison functional'],
            pure_M_change='Zero-pad R/T/Z and core modes, retain original q and analytic lift; update M-dependent canonical model identity',
            quadrature_constraint='For a genuinely M-only comparison preserve the current observation plan and every weight. Published R676 radial-factor=1 still remixes quadrature; disclose that change and use its common-parent functional if used unchanged.',
            angles='Retain N if N>4*Mnew; any necessary N increase is a separately recorded angular change retaining old angles',
            new_larger_space_solve_not_yet_performed=True),
        time_parameter=dict(theorem='R248 equations (248.8)-(248.10)',
            exact_family='F_alpha=R_alpha*F_0 composed with psi_-alpha on the active body; fixed cap graphs stay fixed',
            full_metric_error='sup_M epsilon_alpha = sup_M epsilon_0 for every exact phase',
            no_independent_time_grid_convergence_task=True,
            preserve=['the same exact phase formula and time interval','the same material circle action',
                      'rotationally invariant active reference metric','fixed cap/marker maps and compatible C2 traces'],
            caveat='Linear interpolation between exported time meshes is another map and is not covered; continuous spatial metric/embedding/reach hypotheses still require the same candidate evidence',
            requested_multiple_time_mesh_exports_still_required=True,
            additional_time_samples_evaluated=False),
        scope=dict(report_only=True,scientific_arrays_read=False,field_values_computed=False,
            continuous_metric_certified=False,continuous_geometry_certified=False,
            sustained_fixed_metric_refinement_convergence_certified=False,topic_completion_certified=False))
    a.out.parent.mkdir(parents=True,exist_ok=True)
    temporary=a.out.with_name(a.out.name+'.partial')
    temporary.write_text(json.dumps(clean(result),indent=2,allow_nan=False)+'\n')
    temporary.replace(a.out)
    print(json.dumps(dict(event='fixed_g_refinement_report_attribution_returned',
        output=str(a.out.resolve()),sha256=digest(a.out.read_bytes()),
        parent_bound=parent_binding['bound'],transfer_bound=ref_binding['bound'],
        fine_naturally_complete=fine_complete,common_final_comparable=solved['comparable'],
        scientific_arrays_read=False,sustained_refinement_convergence_certified=False),allow_nan=False))


if __name__=='__main__':
    main()
