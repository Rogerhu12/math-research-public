#!/usr/bin/env python3
"""One new complete short-root integral screening radial-weight budgets.

Scientific execution is public Actions only.  Original positive/germ rows,
candidate definitions and all completed high/two-mode/X/GB conclusions are
read unchanged.  No old target, geometry ODE or capacity ODE is called.
The only new numerical target is the positive integral T in RS.15, with
length 1/100 and 32 fixed subdivisions per original intersected cell.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import time

KIND = 'R138_radial_weight_independent_root_budget_screen_v1'
BITS = 320
LENGTH = Fraction(1, 100)
SUBDIVISIONS = 32
DEFINITION_SHA = 'd152f31cef53c1d58099cf3d1f994d2dad9d31d6a75cb42a7d9e54a35c17ae79'
HIGH_SHA = 'f3f97be683009e9c8ae461c25dfd17d782a61ea6feaf9b8b7967b3e28a9e835d'
HIGH_EXECUTION_SHA = 'e753dd0ea848302ccbe41dc90a3cd8ab1a1a211985d7a7d3691d7ab6384a7687'
TWO_MODE_SHA = '95c80fdeeb3cf75327f028b1020db5aeda0fa3502aa6c0b3546c17ac6d2258c2'
TWO_MODE_EXECUTION_SHA = 'f66a976a0433204c9c043ab977d58439f091d2304b6cd9ef1df13eac0ae2c0f2'
X_SHA = '1259c3687cea0af523dd52055e88d5ee9a7b77094c218101835b6c38dfbbc7ec'
X_EXECUTION_SHA = '999555eafb3c443266f1a8fed98056c9d4f448c0131ef5ffff93941b35040c92'
GB_SHA = '5b5f374fb68e66ce25725195a9d574940e5ee7e9b273b6b55da90ada261ec492'
GB_EXECUTION_SHA = '9bc00f39ab9656ef3e3afbc64f3df20d8340bbe85b92be4bc17141a80f28a18f'
AXIS_SHA = 'b300ea209acb2239a93a87aa3f14d6d9c5f0ed3b5b88ea44b415e5078ea0cd92'
MEAN_SHA = 'de3a14606aa432fbd1f7707c277a33110f81ce6ca23fdfc6bfdf7e9d497623b4'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path, expected):
    raw = Path(path).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == expected,
            'whole original input identity: ' + Path(path).name)
    return json.loads(raw)


def save(path, document):
    raw = (json.dumps(document, ensure_ascii=False, indent=2, allow_nan=False)+'\n').encode()
    temporary = Path(str(path)+'.partial')
    temporary.write_bytes(raw)
    temporary.replace(path)
    require(path.read_bytes() == raw, 'whole new scalar result exact byte readback')


def execution_admission(document, run_id, scientific_sha):
    require(document.get('complete') is True
        and str(document.get('run_id')) == run_id
        and str(document.get('run_attempt')) == '1'
        and document.get('actual_child_returncode') == 0
        and document.get('original_scientific_complete') is True
        and document.get('original_scientific_failure') is None
        and document.get('old_completed_targets_recomputed') == 0
        and document.get('old_numerical_producers_called') == 0
        and document.get('scientific_children') == 1,
        'complete original execution and original no-recomputation scope')
    require(any(row.get('sha256') == scientific_sha
                for row in document.get('scientific_files', [])),
            'original execution binds its complete scientific result')


def run(args):
    require(os.environ.get('GITHUB_ACTIONS') == 'true'
        and os.environ.get('GITHUB_REPOSITORY') == 'Rogerhu12/math-research-public',
        'new science runs only in this repository public Actions')
    require(not args.output.exists(), 'preserve every previous result or failed prefix')
    require(digest(args.definition_source) == DEFINITION_SHA, 'pure original definition helper')
    spec = importlib.util.spec_from_file_location('root_input_definitions_only',
                                                args.definition_source)
    definition = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(definition)
    from flint import arb, ctx
    ctx.prec = BITS
    began = time.monotonic()
    args.output.parent.mkdir(parents=True, exist_ok=True)

    def rat(value):
        value = Fraction(value)
        return arb(value.numerator)/value.denominator

    def old_ball(record):
        require('lower' in record and 'upper' in record, 'complete original signed endpoints')
        return arb(record['lower']).lower().union(arb(record['upper']).upper())

    def unpack(record):
        if 'ball' in record:
            return arb(record['ball'])
        require(record.get('kind') == 'complete_decimal_ball_v1', 'complete saved scalar kind')
        exponent = int(record['decimal_exponent'])
        scale = rat(10**exponent) if exponent >= 0 else rat(Fraction(1, 10**(-exponent)))
        mid = rat(int(record['midpoint_integer']))*scale
        radius = rat(int(record['radius_integer']))*scale
        require(radius >= 0, 'nonnegative whole scalar radius')
        return (mid-radius).lower().union((mid+radius).upper())

    def recorded(value):
        require(value.is_finite(), 'finite complete new positive integral upper')
        m, r, e = value.mid_rad_10exp(75)
        result = dict(kind='complete_decimal_ball_v1', mathematical_direction='upper',
                      midpoint_integer=str(int(m)), radius_integer=str(int(r)),
                      decimal_exponent=str(int(e)))
        require(int(r) >= 0 and unpack(result).contains(value),
                'saved whole scalar contains its complete directed value')
        return result

    high = read(args.high, HIGH_SHA)
    two = read(args.two_mode, TWO_MODE_SHA)
    old_x = read(args.physical, X_SHA)
    gb = read(args.body_budget, GB_SHA)
    priors = ((high, read(args.high_execution, HIGH_EXECUTION_SHA), '44750653724', HIGH_SHA),
              (two, read(args.two_mode_execution, TWO_MODE_EXECUTION_SHA), '44745192261', TWO_MODE_SHA),
              (old_x, read(args.physical_execution, X_EXECUTION_SHA), '44737045152', X_SHA),
              (gb, read(args.body_execution, GB_EXECUTION_SHA), '44745355257', GB_SHA))
    for result, execution, run_id, native in priors:
        require(result.get('complete') is True and result.get('proved') is True
            and result.get('failure') is None, 'whole successful prior conclusion')
        execution_admission(execution, run_id, native)
    require(high['completed_cells'] == 32768
        and high['high_lower_bound_positive'] is True and high['receiver_neumann_gate'] is True
        and high['strict_gates_use_complete_saved_decimal_balls'] is True
        and high['whole_original_references']['two_mode'] == two,
        'same complete original high inverse and exact whole signed two-mode input')
    require(sum(len(high[key]) for key in (
        'complete_new_scalar_bounds', 'complete_receiver_coefficients',
        'complete_high_lower_bound_terms', 'complete_nonhomogeneous_source_coefficients'))+1 == 41,
        'all41 completed original high scalar records retained')
    for key in ('old_axis_targets_called', 'old_mean_targets_called', 'old_X_targets_called',
                'old_two_mode_matrix_entries_recomputed', 'old_ZP_propagations_called',
                'old_geometry_targets_called', 'published_arrays'):
        require(high[key] == 0, 'original high no-recomputation qualification')
    require(high['scope']['same_Qrepair_true_root'] is True
        and high['scope']['original_root_low96_and_all_high_rows_preserved'] is True
        and high['scope']['actual_positive_boundary_problem_singular'] is False
        and high['scope']['positive_inverse_proved'] is False,
        'same original root operator, no old false scope changed')
    require(two['completed_cells'] == two['nonlocal_completed_cells'] == 32768
        and two['scope']['negative_two_mode_direction_proved'] is True
        and two['scope']['actual_positive_boundary_problem_singular'] is False
        and two['strict_sign_uses_complete_saved_decimal_balls'] is True
        and two['whole_original_references']['physical_budget'] == old_x,
        'complete signed root form and same whole X budget')
    axis = two['whole_original_references']['axis']
    mean = two['whole_original_references']['mean']
    require(two['identity']['prior_axis_sha256'] == AXIS_SHA
        and two['identity']['prior_mean_sha256'] == MEAN_SHA
        and axis['complete'] is True and axis['proved'] is True
        and axis['completed_original_rows'] == 4650
        and mean['complete'] is True and mean['proved'] is True
        and mean['completed_cells'] == 8192
        and unpack(mean['actual_mean_denominator']).lower() > rat(Fraction(17,20)),
        'whole original axis and independent mean are read only and retained')
    coefficient = high['complete_new_scalar_bounds']
    for key, upper in (('b_0_upper',1), ('b_1_upper',2), ('b_2_upper',2), ('g_m_0_upper',3)):
        require(unpack(coefficient[key]).upper() < rat(upper),
                'original whole high record proves the analytic RS norm premise')
    matrix = two['complete_actual_signed_two_mode_matrix']
    require(len(matrix) == 3 and unpack(matrix[0]).upper() < rat(Fraction(457,1000))
        and unpack(matrix[1]).lower() > rat(Fraction(189,10))
        and unpack(matrix[2]).upper() < rat(Fraction(601,250)),
        'original whole signed matrix endpoints, never reevaluate the three entries')
    require(old_x['scope']['actual_DF_not_WVC_hybrid'] is True
        and old_x['scope']['complete_means_retained'] is True
        and unpack(old_x['complete_derived_energy_bounds']['Gamma']).lower() > rat(Fraction(59,50))
        and gb['saved_record_count'] == 6 and gb['actual_returncode'] == 0
        and gb['scope']['new_body_Hhalf_bounds_proved'] is True
        and gb['scope']['root_Htwo_thirds_path_changed'] is False
        and unpack(gb['new_records']['aEE_upper']).lower() > rat(Fraction(11,10)),
        'the exact previously selected scalar Gamma and GB budget, not optimal error lower bounds')

    positive = definition.read(args.positive, definition.POSITIVE_SHA)
    germ = definition.read(args.germ, definition.GERM_SHA)
    candidate, nodes, cc = definition.load_candidate(args.candidate)
    alpha = Fraction(candidate['metadata']['exact_float_amplitude'])
    require(positive['complete'] is True and positive['coefficient_cover_complete'] is True
        and positive['failure'] is None and len(positive['rows']) == 4650
        and positive['identity']['candidate_sha256'] == definition.CANDIDATE_SHA
        and positive['identity']['object_sha256'] == definition.OBJECT_SHA
        and Fraction(positive['identity']['actual_alpha']) == alpha
        and Fraction(positive['identity']['actual_nu']) == definition.NU
        and Fraction(positive['identity']['exact_eta_center']) == definition.ETA
        and positive['whole_original_eta'] is True,
        'complete original positive coefficient cover and fixed centre')
    require(germ['complete'] is True and germ['proved'] is True and germ['failure'] is None
        and germ['candidate_sha256'] == definition.CANDIDATE_SHA
        and germ['object_sha256'] == definition.OBJECT_SHA
        and Fraction(germ['exact_amplitude']) == alpha
        and Fraction(germ['actual_fixed_nu']) == definition.NU
        and Fraction(germ['exact_center_parameter']) == definition.ETA
        and germ['whole_affine_parameter_interval'] is True
        and tuple(map(Fraction,germ['root_interval'])) == (definition.ROOT_LO,definition.ROOT_HI)
        and germ['actual_candidate_piece'] == 2549
        and germ['compact_bump_identically_zero_on_entire_actual_germ'] is True,
        'same whole true-root germ and original complete candidate definition')
    radial = tuple(map(Fraction,germ['complex_radial_rectangle']['real_interval']))
    scalar = tuple(map(Fraction,germ['original_scalar_germ']))
    require(nodes[2549] <= definition.ROOT_LO < definition.ROOT_HI
        < definition.BODY_LEFT <= nodes[2550]
        and radial[0] <= definition.ROOT_LO < definition.BODY_LEFT <= radial[1]
        and scalar[0] <= definition.ROOT_LO < definition.BODY_LEFT <= scalar[1],
        'the entire uncertain-root collar is inside the original signed germ')
    require(high['identity']['candidate_sha256'] == definition.CANDIDATE_SHA
        and high['identity']['germ_sha256'] == definition.GERM_SHA
        and high['identity']['object_sha256'] == definition.OBJECT_SHA
        and high['identity']['repair_definition_sha256'] == definition.REPAIR_DEFINITION_SHA
        and high['identity']['exact_root_interval'] == [str(definition.ROOT_LO),str(definition.ROOT_HI)]
        and high['identity']['fixed_point'] == '(0,0,1/2)',
        'original high, geometry and new scalar use the identical Qrepair root')

    cutoff = definition.ROOT_HI+LENGTH
    require(cutoff < definition.RIGHT, 'fixed whole test interval is inside the positive cap')
    endpoint = definition.BODY_LEFT
    pieces = [(definition.ROOT_LO, definition.BODY_LEFT, -1, 2549)]
    original_interfaces = []
    for index,row in enumerate(positive['rows']):
        left,right = map(Fraction,row['interval'])
        piece = row['candidate_piece']
        require(left == endpoint and nodes[piece] <= left < right <= nodes[piece+1],
                'every original row and candidate interface is preserved')
        endpoint = right
        if row['right_interface'] is not None:
            original_interfaces.append(row['right_interface'])
        if left < cutoff:
            pieces.append((left,min(right,cutoff),index,piece))
    require(endpoint == definition.RIGHT and pieces[0][0] == definition.ROOT_LO
        and pieces[-1][1] == cutoff
        and all(pieces[j][1] == pieces[j+1][0] for j in range(len(pieces)-1)),
        'complete original full cover and complete new fixed short interval')
    partition = [[str(l),str(r),row,piece] for l,r,row,piece in pieces]
    partition_sha = hashlib.sha256(json.dumps(partition,separators=(',',':')).encode()).hexdigest()
    interface_sha = hashlib.sha256(json.dumps(original_interfaces,sort_keys=True,
                                            separators=(',',':')).encode()).hexdigest()
    identity = dict(kind=KIND, source_sha256=digest(__file__), arithmetic_bits=BITS,
        definition_source_sha256=DEFINITION_SHA,
        original_positive_sha256=definition.POSITIVE_SHA,
        original_germ_sha256=definition.GERM_SHA,
        original_candidate_sha256=definition.CANDIDATE_SHA,
        original_intrinsic_object_sha256=definition.OBJECT_SHA,
        exact_repair_definition_sha256=definition.REPAIR_DEFINITION_SHA,
        exact_eta=str(definition.ETA), exact_nu=str(definition.NU), exact_alpha=str(alpha),
        exact_true_root_interval=[str(definition.ROOT_LO),str(definition.ROOT_HI)],
        actual_test_interval='[r_star,r_star+1/100]',
        conservative_integration_interval=[str(definition.ROOT_LO),str(cutoff)],
        fixed_test_length=str(LENGTH), fixed_subdivisions_per_original_cell=SUBDIVISIONS,
        original_positive_rows=4650, original_positive_interfaces=len(original_interfaces),
        original_positive_interface_metadata_sha256=interface_sha,
        complete_new_partition_sha256=partition_sha,
        reflection_axis_moving_angles=['0','pi/4'],
        physical_angles_equal_moving_angles_on_both_axes=True,
        full_repair_A0=str(definition.REPAIR), support_vector_norm_upper='222/125',
        analytic_test_root_L2_upper='26/25', analytic_test_root_derivative_L2_upper='385',
        old_high_sha256=HIGH_SHA,old_high_execution_sha256=HIGH_EXECUTION_SHA,
        old_two_mode_sha256=TWO_MODE_SHA,old_two_mode_execution_sha256=TWO_MODE_EXECUTION_SHA,
        old_X_sha256=X_SHA,old_X_execution_sha256=X_EXECUTION_SHA,
        old_GB_sha256=GB_SHA,old_GB_execution_sha256=GB_EXECUTION_SHA,
        original_low_modes=[1,96],original_high_modes='j>=97')
    references = {}
    for name,(result,execution,run_id,native),exec_sha in zip(
        ('high','two_mode','physical_budget','body_budget'),priors,
        (HIGH_EXECUTION_SHA,TWO_MODE_EXECUTION_SHA,X_EXECUTION_SHA,GB_EXECUTION_SHA)):
        references[name] = dict(complete_result_sha256=native,complete_execution_sha256=exec_sha,
            run_id=run_id,whole_result_admitted=True,whole_execution_admitted=True,
            original_identity=result['identity'],original_scope=result['scope'])
    references['nested_axis_mean'] = dict(complete_axis_sha256=AXIS_SHA,
        complete_mean_sha256=MEAN_SHA,contained_unchanged_in_complete_two_mode=True,
        old_axis_target_called=False,old_mean_target_called=False)
    doc = dict(identity=identity,complete=False,proved=False,failure=None,stage='prepared-complete-new-integral',
        expected_common_cells=len(pieces),completed_common_cells=0,
        expected_subcells=SUBDIVISIONS*len(pieces),completed_subcells=0,
        completed_positive_rows=0,integral_prefix=recorded(arb(0)),complete_test_integral=None,
        current_exact_right=str(definition.ROOT_LO),old_scientific_targets_called=0,
        old_axis_targets_called=0,old_mean_targets_called=0,old_high_41_targets_recomputed=0,
        old_signed_matrix_entries_recomputed=0,old_GB_X_targets_recomputed=0,
        old_geometry_ODE_calls=0,new_capacity_ODE_calls=0,published_arrays=0,
        whole_original_references=references,
        scope=dict(same_actual_Qrepair_and_original_full_high=True,
            exact_independent_mean_and_original_all_interfaces_retained=True,
            true_root_not_replaced_by_midpoint=True,
            arbitrary_radial_weights_and_free_outer_cuts_compared=True,
            complete_integral_target_proved=False,
            original_Gamma_LC_receiver_budget_excluded=False,
            all_scalar_Jacobian_LC_receiver_budgets_excluded=False,
            exclusion_keeps_original_selected_GB_body_budget=True,
            optimized_body_error_lower_bound_proved=False,
            actual_positive_boundary_problem_singular=False,
            localized_receiver_budget_proved=False,
            positive_inverse_proved=False,final_topic_complete=False),
        strict_gates=None,seconds=time.monotonic()-began)
    save(args.output,doc)
    total = unpack(json.loads(args.output.read_text())['integral_prefix']).upper()
    repair_ball = arb(0,rat(definition.REPAIR))
    derivative_cost = rat(Fraction(26,25))**2/(rat(LENGTH)**2)
    angular_cost = rat(385)**2
    geometric = rat(Fraction(222,125))
    cache_piece = None
    axis_polynomials = None

    for cell_index,(left,right,row_index,piece) in enumerate(pieces):
        if piece != cache_piece:
            # Exact old cubic definitions only, for this new integral target.
            # The former support propagation and its axis outputs are not called.
            axis_polynomials = []
            for axis_sign in (1,-1):
                axis_polynomials.append([
                    alpha*sum((Fraction.from_float(float(cc[degree,piece,32+j]))
                               *axis_sign**j for j in range(1,33)),Fraction(0))
                    for degree in range(4)])
            cache_piece = piece
        if row_index < 0:
            intrinsic = germ['complex_intrinsic_coefficients']
            gamma = old_ball(intrinsic['gamma']['real'])
            curvature_original = old_ball(intrinsic['K']['real'])
            mean_original = old_ball(germ['moving_mean_v']['real'])
        else:
            row = positive['rows'][row_index]
            gamma = old_ball(row['intrinsic']['gamma'])
            curvature_original = old_ball(row['intrinsic']['K'])
            mean_original = old_ball(row['bounds']['mean_v'])
            require(curvature_original > 0, 'original positive closed row has its strict K sign')
        require(gamma > 0 and mean_original+repair_ball < 0,
                'whole ordinary eta denominator with the independent repaired mean')
        eta = -gamma*(mean_original+repair_ball)
        require(eta > 0 and curvature_original.upper() > 0,
                'positive eta and a nonempty nonnegative physical curvature intersection')
        # Only the actual positive part r>=r_star contributes.  The germ
        # interval extends below that unknown root; K>=0 there is the paid
        # positive-side fact, not an assertion about the extra lower padding.
        curvature_lower = max(arb(0),curvature_original.lower())
        curvature = curvature_lower.union(curvature_original.upper())
        width = (right-left)/SUBDIVISIONS
        for sub in range(SUBDIVISIONS):
            l,r = left+sub*width,left+(sub+1)*width
            dx = rat(l-nodes[piece]).union(rat(r-nodes[piece]))
            quotients = []
            for polynomial in axis_polynomials:
                nonmean = arb(0)
                for coefficient_value in polynomial:
                    nonmean = nonmean*dx+rat(coefficient_value)
                axis_v = mean_original+nonmean+repair_ball
                require(axis_v < 0, 'complete repaired reflection-axis v sign')
                denominator = 1+curvature*axis_v**2
                require(denominator > 0, 'whole true positive-axis denominator')
                quotients.append((-axis_v/denominator).upper())
            h_upper = (geometric*min(quotients)).upper()
            # The actual portion has 0<=r-r_star<=ell.  Enlarging its radial
            # cover to [ROOT_LO,ROOT_HI+ell] is safe because all fees are positive.
            x_lower = max(Fraction(0),l-definition.ROOT_HI)
            f_upper = max(Fraction(0),Fraction(1)-x_lower/LENGTH)
            integrand = h_upper*(derivative_cost/eta
                         +angular_cost*eta*curvature*rat(f_upper)**2)
            require(integrand.is_finite() and integrand >= 0,
                    'complete new positive integrand on the original whole subcell')
            contribution = (rat(width)*integrand.upper()).upper()
            total = (total+contribution).upper()
            doc['completed_subcells'] += 1
            doc['current_exact_right'] = str(r)
            if sub+1 == SUBDIVISIONS:
                doc['completed_common_cells'] = cell_index+1
                doc['completed_positive_rows'] += int(row_index >= 0)
            if doc['completed_subcells'] % 32 == 0:
                doc['integral_prefix'] = recorded(total)
                doc['stage'] = 'complete-original-cell-prefix'
                doc['seconds'] = time.monotonic()-began
                save(args.output,doc)
                total = unpack(json.loads(args.output.read_text())['integral_prefix']).upper()
                print(json.dumps(dict(completed_common_cells=doc['completed_common_cells'],
                    completed_subcells=doc['completed_subcells'],current_exact_right=str(r))),flush=True)

    require(doc['completed_common_cells'] == doc['expected_common_cells']
        and doc['completed_subcells'] == doc['expected_subcells']
        and Fraction(doc['current_exact_right']) == cutoff,
        'whole fixed new short interval, no prefix promoted to a conclusion')
    doc['complete_test_integral'] = doc['integral_prefix']
    doc['stage'] = 'complete-integral-saved-before-comparisons'
    save(args.output,doc)
    whole_saved = unpack(json.loads(args.output.read_text())['complete_test_integral'])
    gate_original = bool(whole_saved.upper() <= rat(225))
    gate_all_scalar = bool(whole_saved.upper() <= rat(160))
    doc['strict_gates'] = dict(
        original_Gamma_and_selected_GB_budget_excluded=gate_original,
        all_scalar_Jacobian_factors_at_least_one_and_selected_GB_budget_excluded=gate_all_scalar,
        thresholds={'original_Gamma':'225','all_scalar_Jacobian':'160'},
        complete_saved_upper_used=True,
        false_gate_means_only_this_screen_did_not_exclude=True,
        negative_true_BVP_or_inverse_claimed=False)
    doc['scope']['complete_integral_target_proved'] = True
    doc['scope']['original_Gamma_LC_receiver_budget_excluded'] = gate_original
    doc['scope']['all_scalar_Jacobian_LC_receiver_budgets_excluded'] = gate_all_scalar
    doc.update(complete=True,proved=True,stage='complete-radial-weight-independent-root-screen',
               seconds=time.monotonic()-began)
    save(args.output,doc)
    print(json.dumps(dict(complete=True,proved=True,completed_subcells=doc['completed_subcells'],
        original_Gamma_excluded=gate_original,all_scalar_Jacobian_excluded=gate_all_scalar,
        output=str(args.output))),flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for flag in ('definition_source','positive','candidate','germ','high','high_execution',
                 'two_mode','two_mode_execution','physical','physical_execution',
                 'body_budget','body_execution','output'):
        parser.add_argument('--'+flag.replace('_','-'),type=Path,required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError('preserve the existing completed result or unfinished prefix')
    try:
        run(args)
    except Exception as exc:
        if args.output.exists():
            doc = json.loads(args.output.read_text())
            if not doc.get('complete'):
                doc['failure'] = dict(type=type(exc).__name__,message=str(exc))
                doc['stage'] = 'unfinished-new-integral-prefix'
                save(args.output,doc)
        raise


if __name__ == '__main__':
    main()
