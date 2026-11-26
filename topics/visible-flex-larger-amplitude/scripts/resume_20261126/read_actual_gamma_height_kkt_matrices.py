#!/usr/bin/env python3
"""Read already saved same-state gamma-H KKT matrices in public Actions.

No field, closure, Jacobian, Newton trajectory, integral or checkpoint is
recomputed. All numerical work is small linear algebra on a matrix that the
actual b712 operator already saved at its explicitly identified state.
No matrix, state vector, singular vector or raw controls are emitted.
"""
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time

SCHEMA = 'actual-gamma-height-saved-KKT-matrix-scalar-readout-v1'
TOPIC = Path('topics/visible-flex-larger-amplitude')
PINS = {
    'driver': ('scripts/resume_20261126/fullclosed_zero_gamma_kkt_height_so3_qp.py',
        '8f37529deaa8e07d4561e00371b39b82cb641a4e52e0790d41555b2ae9e320a9'),
    'reader': ('scripts/resume_20261126/read_zero_gamma_kkt_height_so3_report.py',
        'c3fdd83c29dabeb00974899bb183360da01c57fcf364704759efcc1ac643b9ec'),
    'endpoint': ('scripts/resume_20261126/so3_zero_gamma_kkt_operator.py',
        'b712a24a0c0223356b4a53e6aa1fa78ba9cea66e4be39c7ee39931be99cb782a'),
    'reference': ('scripts/resume_20261126/so3_axisymmetric_reference.py',
        '4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3'),
    'scalar': ('notes/2026-11-17-parallel-model-full-hold-oracle.py',
        'a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670'),
}
DRIVER_SCHEMA = 'complete-independent-fixed-deep-added-gamma-nine-KKT-explicit-height-SO3-QP-v1'
OPERATOR_SCHEMA = 'complete-direct-R690-SO3-added-gamma-six-control-KKT-zero-layer-v1'
BATCH_SCHEMA = 'actual-added-gamma-nine-KKT-residual-continuation-batch-v1'
MATRIX_SCOPE = ('already evaluated ORIGINAL nine-KKT Jacobian at its explicitly recorded state; '
    'not a matrix at an unlabelled later state')

def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode('utf-8')).hexdigest()

def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1 << 20),b''):
            h.update(block)
    return h.hexdigest()

def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Numerical matrix diagnostics require public repository Actions')

def file_record(path):
    path = Path(path).resolve()
    return dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size)

def digest_word(value,name):
    if (not isinstance(value,str) or len(value)!=64
            or any(c not in '0123456789abcdef' for c in value)):
        raise ValueError('Use the complete recorded SHA256 for '+name)
    return value

def finite_number(value,name):
    if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(float(value)):
        raise ValueError('A finite actual numerical scalar is required: '+name)
    return float(value)

def integer(value,name,minimum=0):
    if isinstance(value,bool) or not isinstance(value,int) or value<minimum:
        raise ValueError('Use the actual integer '+name)
    return value

def output_number(value):
    value = float(value)
    return value if math.isfinite(value) else None

def ratio(numerator,denominator):
    if (not math.isfinite(numerator) or not math.isfinite(denominator)
            or denominator <= 0):
        return None
    return output_number(numerator/denominator)

def literal_array(np,value,shape,name):
    array = np.asarray(value,dtype=np.float64)
    def scalars(item):
        if isinstance(item,list):
            for child in item:
                yield from scalars(child)
        else:
            yield item
    for item in scalars(value):
        finite_number(item,name)
    if array.shape != shape or not np.isfinite(array).all():
        raise ValueError('The complete actual array shape differs: '+name)
    array = np.ascontiguousarray(array)
    array.setflags(write=False)
    return array

def array_sha(array):
    # This is an actual byte identity, not a numerical certificate.
    return hashlib.sha256(array.tobytes(order='C')).hexdigest()

def load_reader(path):
    spec = importlib.util.spec_from_file_location('_actual_gamma_H_pure_reader',path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module

def source_binding(repo):
    paths = {role:repo/TOPIC/relative for role,(relative,_) in PINS.items()}
    for role,path in paths.items():
        if sha(path) != PINS[role][1]:
            raise ValueError('Changed complete bound source '+role)
    return paths

def working_S(report):
    # The exact a1ed carrier is float((lower+upper)/2). The bound 4e context
    # requires this value to equal its stored mesh[-1], used as q.S by 7f/b712.
    # This reads its existing scalar enclosure; no scalar law is reevaluated.
    metadata = report['independent_reference_context']['full_scalar']
    if metadata['source_sha256'] != PINS['scalar'][1]:
        raise ValueError('The reported complete FullHold carrier source changed')
    box = metadata['S']
    lo,hi = Fraction(box['lower_exact']),Fraction(box['upper_exact'])
    if not 0 < lo <= hi:
        raise ValueError('Use the actual positive complete S enclosure')
    value = float((lo+hi)/2)
    if not math.isfinite(value) or value<=0:
        raise ValueError('The recorded complete S has no finite positive carrier')
    return value

def bind_batch(report):
    metadata = report.get('latest_operator_metadata')
    if metadata is None:
        return None,None,'unread_no_actual_operator_metadata'
    model = report['representation']
    if (metadata.get('schema') != OPERATOR_SCHEMA
            or metadata.get('source_sha256') != PINS['endpoint'][1]
            or metadata.get('model') != model
            or metadata.get('model_identity_sha256') != canonical(model)):
        raise ValueError('Only the same actual complete operator metadata may supply a matrix')
    batch = metadata.get('endpoint_continuation_last_batch')
    if batch is None:
        return metadata,None,'unread_no_saved_continuation_batch'
    point = digest_word(metadata.get('current_full_point_sha256'),'actual current full point')
    if (batch.get('schema') != BATCH_SCHEMA
            or batch.get('current_full_point_sha256') != point
            or batch.get('auxiliary_parameter_is_not_physical_t') is not True
            or batch.get('complete_continuous_branch_certified') is not False):
        raise ValueError('The saved batch belongs to a different point or equation')
    angles = batch['material_angles_binary64_hex']
    count = integer(batch['angle_count'],'batch angle count',1)
    if not isinstance(angles,list) or len(angles)!=count:
        raise ValueError('Retain every actual material angle in the stored batch')
    for word in angles:
        if not isinstance(word,str):
            raise ValueError('Keep actual literal material-angle words')
        value = float.fromhex(word)
        if not math.isfinite(value) or value.hex()!=word:
            raise ValueError('Keep canonical finite material-angle words')
    return metadata,batch,None

def matrix_inputs(np,report,metadata,batch):
    """Yield every saved failure matrix once, with its own state association."""
    point = metadata['current_full_point_sha256']
    angle_words = batch['material_angles_binary64_hex']
    stages = batch['stages']
    if not isinstance(stages,list):
        raise ValueError('Retain the complete ordered saved stage list')
    counts = dict(stored_batch_stage_count=len(stages),stored_angle_stage_records=0,
        successful_angle_stages_without_saved_failure_matrix=0,
        failed_angle_stages=0,failed_angle_stages_without_saved_matrix=0,
        saved_failure_matrix_count=0)
    items = []
    for position,stage in enumerate(stages):
        if stage.get('batch_stage') != position or not isinstance(stage.get('angle_records'),list):
            raise ValueError('Use the actual complete ordered batch stages')
        for entry in stage['angle_records']:
            counts['stored_angle_stage_records'] += 1
            index = integer(entry['angle_index'],'local angle index')
            if not 0<=index<len(angle_words) or entry.get('requested') is not True:
                raise ValueError('The saved angle-stage address is not part of this batch')
            successful = entry.get('successful')
            if not isinstance(successful,bool):
                raise ValueError('A saved stage needs its actual success flag')
            saved = entry.get('last_evaluated_KKT_matrix')
            if successful:
                if saved is not None:
                    raise ValueError('This b712 source stores a matrix only for a failed stage')
                counts['successful_angle_stages_without_saved_failure_matrix'] += 1
                continue
            counts['failed_angle_stages'] += 1
            if saved is None:
                counts['failed_angle_stages_without_saved_matrix'] += 1
                continue
            target = finite_number(saved['continuation_parameter_target'],'matrix continuation target')
            if (saved.get('scope') != MATRIX_SCOPE
                    or saved.get('current_full_point_sha256') != point
                    or saved.get('local_angle_index') != index
                    or target.hex() != finite_number(entry['parameter_target'],'stage target').hex()
                    or not 0<=target<=1
                    or saved.get('extra_field_or_J_evaluations') != 0
                    or saved.get('extra_SVD_evaluations') != 0):
                raise ValueError('The saved matrix/state/angle/target binding differs')
            iteration = integer(saved['newton_iteration'],'matrix Newton iteration')
            matrix = literal_array(np,saved['matrix_values'],(9,9),'own-state complete KKT matrix')
            state = literal_array(np,saved['state_values'],(9,),'own-state six controls and three multipliers')
            residual = literal_array(np,saved['shifted_stage_residual_values'],(9,),
                'own-state shifted nine-equation residual')
            returned = literal_array(np,entry['state_values'],(9,),'returned failed-stage state')
            returned_residual = literal_array(np,entry['nine_KKT_values'],(9,),
                'returned failed-stage shifted residual')
            identity = dict(
                stored_batch_stage_index=position,local_angle_index=index,
                material_angle_binary64_hex=angle_words[index],
                continuation_parameter_target=target,
                continuation_parameter_target_hex=target.hex(),
                actual_matrix_newton_iteration=iteration,
                current_full_point_sha256=point,
                matrix_record_sha256=canonical(saved),
                matrix_binary64_sha256=array_sha(matrix),
                matrix_state_binary64_sha256=array_sha(state),
                matrix_shifted_residual_binary64_sha256=array_sha(residual),
                returned_stage_state_binary64_sha256=array_sha(returned),
                returned_stage_residual_binary64_sha256=array_sha(returned_residual),
                actual_stage_reason=str(entry.get('reason')),
                matrix_state_equals_returned_stage_state=state.tobytes()==returned.tobytes(),
                matrix_residual_equals_returned_stage_residual=residual.tobytes()==returned_residual.tobytes(),
                matrix_and_residual_are_from_the_same_recorded_state=True,
                original_endpoint_residual_equals_shifted_residual=(target==1.))
            counts['saved_failure_matrix_count'] += 1
            items.append((identity,matrix,state,residual))
    return counts,items

def analyze_matrix(np,identity,K,state,residual,policy,S):
    """Ordinary binary64 diagnostics only; no certified rank or SOSC claim."""
    row = dict(identity)
    row.update(matrix_diagnostics_complete=True,
        exact_rank_or_invertibility_certified=False,SOSC_verified=False,
        continuous_root_branch_certified=False,
        control_components_or_matrix_values_emitted=False,
        original_equation_physical_residual_available=(identity['continuation_parameter_target']==1.))
    A,L,AT,Zblock = K[6:,:6],K[:6,:6],K[:6,6:],K[6:,6:]
    norm = lambda value: float(np.linalg.norm(value))
    opnorm = lambda value: float(np.linalg.norm(value,ord=2))
    row.update(
        recorded_KKT_asymmetry_norm_F=output_number(norm(K-K.T)),
        recorded_L_asymmetry_norm_F=output_number(norm(L-L.T)),
        recorded_AT_block_defect_norm_F=output_number(norm(AT-A.T)),
        recorded_zero_multiplier_block_norm_F=output_number(norm(Zblock)),
        own_state_dimensionless_control_norm=output_number(norm(state[:6])),
        own_state_multiplier_norm=output_number(norm(state[6:])),
        own_state_shifted_KKT_residual_norm=output_number(norm(residual)),
        own_state_original_stationarity_residual_norm=output_number(norm(residual[:6])),
        own_state_shifted_endpoint_dimensionless_residual_norm=output_number(norm(residual[6:])),
        own_state_shifted_endpoint_physical_residual_norm=output_number(S*norm(residual[6:])),
        own_state_original_endpoint_physical_residual_norm=(
            output_number(S*norm(residual[6:])) if identity['continuation_parameter_target']==1. else None))
    eps = float(np.finfo(np.float64).eps)
    Lsym = (L+L.T)/2
    row['reduced_Hessian_uses_symmetric_part_of_recorded_L'] = True
    row['recorded_L_symmetrization_change_norm_F'] = output_number(norm(Lsym-L))
    try:
        _,sv,Vh = np.linalg.svd(A,full_matrices=True)
        if not np.isfinite(sv).all() or not np.isfinite(Vh).all():
            raise FloatingPointError('Nonfinite numerical A singular decomposition')
        threshold = max(A.shape)*eps*float(sv[0])
        rank = int(np.count_nonzero(sv>threshold))
        row.update(A_singular_max=output_number(sv[0]),
            A_singular_middle=output_number(sv[1]),
            A_singular_min=output_number(sv[2]),
            A_condition_2=ratio(float(sv[0]),float(sv[2])),
            A_numerical_rank=rank,A_rank_threshold=threshold,
            A_numerically_full_row_rank=(rank==3),
            A_min_over_max=ratio(float(sv[2]),float(sv[0])))
        # The cutoff convention is reported, never used to accept/reject a field.
        # If rank<3, retain ALL additional numerical-kernel directions.
        Z = Vh[rank:,:].T
        dimension = Z.shape[1]
        row.update(numerical_kernel_dimension=dimension,
            numerical_kernel_residual_norm_2=output_number(opnorm(A@Z)),
            numerical_kernel_orthogonality_defect_norm_2=output_number(opnorm(Z.T@Z-np.eye(dimension))))
        reduced = Z.T@Lsym@Z
        reduced = (reduced+reduced.T)/2
        eigenvalues = np.linalg.eigvalsh(reduced)
        if not np.isfinite(eigenvalues).all():
            raise FloatingPointError('Nonfinite numerical reduced Hessian eigenvalues')
        eigen_threshold = dimension*eps*float(np.max(np.abs(eigenvalues)))
        nearest = int(np.argmin(np.abs(eigenvalues)))
        row.update(reduced_Hessian_eigen_min=output_number(eigenvalues[0]),
            reduced_Hessian_eigen_max=output_number(eigenvalues[-1]),
            reduced_Hessian_nearest_zero_eigenvalue=output_number(eigenvalues[nearest]),
            reduced_Hessian_min_abs_eigenvalue=output_number(abs(eigenvalues[nearest])),
            reduced_Hessian_eigenvalue_threshold=eigen_threshold,
            reduced_Hessian_numerical_negative_count=int(np.count_nonzero(eigenvalues < -eigen_threshold)),
            reduced_Hessian_numerical_positive_count=int(np.count_nonzero(eigenvalues > eigen_threshold)),
            reduced_Hessian_numerical_near_zero_count=int(np.count_nonzero(abs(eigenvalues)<=eigen_threshold)),
            reduced_Hessian_sample_positive_by_reported_threshold=bool(eigenvalues[0]>eigen_threshold))
    except (np.linalg.LinAlgError,FloatingPointError) as error:
        row.update(matrix_diagnostics_complete=False,A_or_reduced_Hessian_analysis_unavailable=str(error))
    try:
        singular = np.linalg.svd(K,compute_uv=False)
        if not np.isfinite(singular).all():
            raise FloatingPointError('Nonfinite numerical K singular values')
        threshold = 9*eps*float(singular[0])
        row.update(K_singular_max=output_number(singular[0]),
            K_singular_min=output_number(singular[-1]),
            K_condition_2=ratio(float(singular[0]),float(singular[-1])),
            K_numerical_rank=int(np.count_nonzero(singular>threshold)),
            K_rank_threshold=threshold,
            K_min_over_max=ratio(float(singular[-1]),float(singular[0])))
    except (np.linalg.LinAlgError,FloatingPointError) as error:
        row.update(matrix_diagnostics_complete=False,K_singular_analysis_unavailable=str(error))
    try:
        correction = np.linalg.solve(K,residual)
        if not np.isfinite(correction).all():
            raise FloatingPointError('Nonfinite correction from the saved numerical matrix')
        linear_residual = K@correction-residual
        candidate = state-correction
        denominator = opnorm(K)*norm(correction)+norm(residual)
        row.update(saved_matrix_linear_solve_available=True,
            saved_matrix_Newton_correction_norm=output_number(norm(correction)),
            saved_matrix_linear_residual_norm=output_number(norm(linear_residual)),
            saved_matrix_relative_backward_residual=(
                ratio(norm(linear_residual),denominator) if denominator>0 else 0.),
            linear_candidate_control_norm=output_number(norm(candidate[:6])),
            linear_candidate_multiplier_norm=output_number(norm(candidate[6:])),
            linear_candidate_inside_declared_control_domain=bool(norm(candidate[:6])<policy['control_radius']),
            linear_candidate_inside_declared_multiplier_domain=bool(norm(candidate[6:])<policy['multiplier_radius']),
            linear_candidate_field_or_residual_recomputed=False)
    except (np.linalg.LinAlgError,FloatingPointError) as error:
        row.update(saved_matrix_linear_solve_available=False,saved_matrix_linear_solve_error=str(error))
    return row

def summarize(rows,counts):
    summary = dict(counts)
    summary.update(
        matrices_with_complete_available_diagnostics=sum(v['matrix_diagnostics_complete'] for v in rows),
        matrices_numerically_full_row_rank_A=sum(v.get('A_numerically_full_row_rank') is True for v in rows),
        matrices_with_numerical_rank_A_below_three=sum(
            v.get('A_numerical_rank',3)<3 for v in rows),
        matrices_with_numerical_rank_K_below_nine=sum(
            v.get('K_numerical_rank',9)<9 for v in rows),
        matrices_with_fullrank_A_and_numerically_singular_K=sum(
            v.get('A_numerically_full_row_rank') is True and v.get('K_numerical_rank',9)<9 for v in rows),
        matrices_with_negative_reduced_Hessian_direction=sum(
            v.get('reduced_Hessian_numerical_negative_count',0)>0 for v in rows),
        all_saved_matrix_snapshots_processed=len(rows)==counts['saved_failure_matrix_count'],
        all_saved_matrix_diagnostics_available=all(v['matrix_diagnostics_complete'] for v in rows),
        all_compact_scalar_rows_sha256=canonical(rows),
        empty_saved_matrix_set_is_not_a_zero_matrix=True)
    representatives = {}
    specifications = (
        ('least_A_singular_value','A_singular_min',min),
        ('least_K_singular_value','K_singular_min',min),
        ('nearest_reduced_Hessian_zero','reduced_Hessian_min_abs_eigenvalue',min),
        ('least_reduced_Hessian_eigenvalue','reduced_Hessian_eigen_min',min))
    for label,key,choose in specifications:
        available = [r for r in rows if isinstance(r.get(key),(int,float)) and math.isfinite(r[key])]
        if available:
            selected = choose(available,key=lambda item:item[key])
            representatives[label] = selected
            summary[key+'_over_all_saved_matrices'] = selected[key]
        else:
            summary[key+'_over_all_saved_matrices'] = None
    for key in ('A_condition_2','K_condition_2','recorded_KKT_asymmetry_norm_F',
                'recorded_AT_block_defect_norm_F','recorded_zero_multiplier_block_norm_F'):
        values = [r[key] for r in rows if isinstance(r.get(key),(int,float)) and math.isfinite(r[key])]
        summary[key+'_maximum_over_available_diagnostics'] = max(values,default=None)
    if rows:
        representatives['last_saved_failure_matrix_in_record_order'] = rows[-1]
    return summary,representatives

def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--report',type=Path,required=True)
    p.add_argument('--report-sha256')
    p.add_argument('--output',type=Path,required=True)
    a = p.parse_args()
    a.repo,a.report,a.output = a.repo.resolve(),a.report.resolve(),a.output.resolve()
    if a.report_sha256 is not None:
        digest_word(a.report_sha256,'expected actual report')
    if a.output==a.repo or a.repo in a.output.parents or a.output.exists():
        raise ValueError('Use a fresh diagnostic output outside the repository')
    return a

def main():
    args = parse_args()
    require_actions()
    started = time.monotonic()
    paths = source_binding(args.repo)
    result = dict(schema=SCHEMA,source_sha256=sha(__file__),
        source_roles={role:digest for role,(_,digest) in PINS.items()},
        github_run_id=os.environ.get('GITHUB_RUN_ID'),
        github_run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'),
        complete=False,actual_report_validated=False,actual_matrix_analysis_performed=False,
        scientific_field_or_closure_evaluations=0,new_J_or_Hessian_evaluations=0,
        new_endpoint_solves=0,new_integral_evaluations=0,
        existing_matrices_only=True,matrices_controls_or_singular_vectors_emitted=False,
        continuous_root_branch_certified=False,exact_matrix_rank_certified=False,
        SOSC_verified=False,global_minimum_verified=False,
        global_nonexistence_claimed=False,diagnostic_is_a_solver_precondition=False,
        historical_batches_not_present_in_actual_report_reconstructed=False,
        physical_phase_or_reach_or_metric_certificate_produced=False)
    if not args.report.is_file():
        result.update(status='unread_actual_report_absent',reason='No actual scientific report file is present')
    else:
        record = file_record(args.report)
        if args.report_sha256 is not None and record['sha256'] != args.report_sha256:
            raise ValueError('The actual input report differs from its explicit expected SHA')
        report = json.loads(args.report.read_text(encoding='utf-8'))
        if report.get('schema') != DRIVER_SCHEMA or report.get('source_sha256') != PINS['driver'][1]:
            raise ValueError('This diagnostic consumes only the actual complete gamma-H source report')
        # Reuse its full pure source/JSON validator; do not import a physical
        # operator or reconstruct any reference, field, Q or checkpoint.
        reader = load_reader(paths['reader'])
        checked = reader.read_report(args.repo,args.report,verify_final_bundle=False)
        if checked['report_sha256'] != record['sha256'] or sha(args.report) != record['sha256']:
            raise ValueError('The actual report changed during the complete pure validation')
        result.update(actual_report=record,actual_report_validated=True,
            actual_scientific_driver_sha256=report['source_sha256'],
            actual_scientific_source_commit=report['source_commit'],
            actual_scientific_run_id=report.get('github_run_id'),
            actual_model_identity_sha256=report['model_identity_sha256'],
            actual_base_model_identity_sha256=report['representation']['base_model_identity_sha256'],
            actual_fixed_scalar_metric_identity_sha256=report['fixed_scalar_metric']['identity_sha256'],
            actual_reference_bundle_sha256=report['bundle_sha256'],
            actual_frozen_Q_definition_identity_sha256=report['frozen_moment_Q_definition_identity_sha256'],
            actual_initial_full_point_sha256=report['initial_free_point']['full_point_sha256'],
            actual_initial_height_binary64_hex=report['initial_free_point']['height_binary64_hex'],
            actual_scientific_report_complete=report.get('complete') is True,
            actual_initial_read_failed=report.get('actual_initial_read_error') is not None,
            pure_reader_source_sha256=PINS['reader'][1],
            original_true_field_acceptance_inherited=False)
        metadata,batch,unread = bind_batch(report)
        if unread is not None:
            result.update(complete=True,status=unread,
                absence_is_not_a_zero_or_nonsingular_matrix=True)
        else:
            import numpy as np
            counts,items = matrix_inputs(np,report,metadata,batch)
            S = working_S(report) if items else None
            policy = metadata['endpoint_root_policy']
            if policy != report['working_evaluation']['endpoint_root_policy']:
                raise ValueError('The actual matrix domain policy changed')
            rows = [analyze_matrix(np,*item,policy,S) for item in items]
            summary,representatives = summarize(rows,counts)
            result.update(complete=True,
                status=('actual_saved_matrices_analyzed' if rows else 'unread_no_saved_failure_matrix'),
                actual_matrix_analysis_performed=bool(rows),
                numpy_version=np.__version__,working_S_binary64_hex=None if S is None else S.hex(),
                working_S_rule='a1ed exact midpoint carrier; bound 4e requires this same mesh endpoint, no new integral',
                matrix_batch_sha256=canonical(batch),
                matrix_batch_current_full_point_sha256=batch['current_full_point_sha256'],
                matrix_batch_angle_count=batch['angle_count'],
                matrix_scope='every available saved matrix in latest_operator_metadata.endpoint_continuation_last_batch; unavailable or earlier discarded batches are not reconstructed',
                KKT_block_rule='K=[[L,A^T],[A,0]], L=I+sum ell_k Hess(f_k), A=f_u, f=C/S, u=(z/S,v)',
                matrix_state_rule='each matrix uses its own saved state/residual, even when the returned failed-stage state differs',
                numerical_rank_rule='count singular values greater than max(shape)*binary64_epsilon*largest singular value; diagnostic only, not an exact-rank or solver gate',
                numerical_kernel_rule='all right singular vectors below the stated A rank cutoff; basis residual and orthogonality reported',
                reduced_Hessian_rule='Z^T sym(L) Z; recorded L asymmetry is separately reported; nonstationary or auxiliary samples do not prove SOSC',
                residual_rule='saved shifted stage residual; stationarity is unchanged, original physical endpoint residual is emitted only at continuation target one',
                singular_case_rule='failed SVD/eigen/solve is reported unavailable, never replaced with invented data',
                summary=summary,representatives=representatives)
    result['actual_readout_seconds'] = time.monotonic()-started
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True,allow_nan=False)+'\n',encoding='utf-8')
    print(json.dumps(dict(event='actual_gamma_height_saved_KKT_matrix_readout',
        output=str(args.output),sha256=sha(args.output),bytes=args.output.stat().st_size,
        complete=result['complete'],status=result['status'],
        actual_matrix_analysis_performed=result['actual_matrix_analysis_performed'],
        actual_saved_matrix_count=result.get('summary',{}).get('saved_failure_matrix_count'),
        actual_readout_seconds=result['actual_readout_seconds']),sort_keys=True,allow_nan=False))

if __name__ == '__main__':
    main()
