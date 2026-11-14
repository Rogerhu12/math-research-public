#!/usr/bin/env python3
"""Read-only close audit for the explicit direct-CSC/release-LU true M14 entry.

Only source hashes, JSON, saved polynomial arrays and polynomial evaluation
are used. No BVP, DN, original flow or candidate initializer is called.
Final CLI mode additionally requires root's real tool-exit observation.
"""
import argparse
import gzip
import importlib.util
import io
import json
import hashlib
import marshal
from pathlib import Path
from types import CodeType

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('spectral_true_audit_definitions', HERE / 'db6f-prefix-spectral-true-m14-direct-csc.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)  # Definitions only; c.main is never invoked here.
require, equal, read, identity, verify = c.require, c.equal, c.read, c.identity, c.verify
number, vector = c.number, c.vector
M, TOL = 14, 2e-9
JET_ARRAYS = {'height','slope','second'}
JET_SCALARS = {'radius','backgroundSlope','backgroundSecond','E','Ep','meanSlope','meanSecond',
               'meanSlopeCorrection','meanSecondCorrection','minLeading','minD',
               'endpointFullD','endpointPhi','formalCurvature'}
AUDIT_FIELDS = {'fullD','normalizedFullDefect','minLeading','minD','formalCurvature',
                'maxPhysicalPV','actualMetric','holonomy'}
SEAM_NUMBERS = {'mean_first_actual','mean_first_expected','mean_first_mismatch',
                'mean_second_actual','mean_second_expected','mean_second_mismatch',
                'nonmean_first_mismatch','nonmean_second_mismatch',
                'cut_metric_fft_l1','cut_metric_c1_fft_l1'}
FIXED_FIELDS = {'angular_chart','chart','warp_reference_q','frozen_profile','gauge_amplitude',
                'meridian_length','physical_port_sha256','physical_tail_parameters','physical_tail_cut'}


def check_packet(path, height, audit, context):
    require(vector(height, M), 'Expected physical cut height is not finite M14')
    record = read(path)
    require(type(record) is dict and set(record) == {'request','response','config','source_sha256'},
            'Unexpected original shared response envelope')
    equal(record['request'], {'height': height, 'jacobian': True, 'audit': audit}, 'Wrong original request/flags')
    equal(record['config'], context['config'], 'Response config differs from actual new config')
    equal(record['source_sha256'], context['prior']['source_sha256'], 'Original shared eight-source identity differs')
    require(len(record['source_sha256']) == 8, 'Expected eight original shared sources')
    response = record['response']
    require(type(response) is dict and 'failed' not in response, 'Original DN failed; no missing success fields inferred')
    require(set(response) == {'converged','residual','jets','heightJetJacobian','history','audit','checkpoint'},
            'Unexpected normal original DN schema')
    require(response['converged'] is True and number(response['residual'])
            and 0 <= response['residual'] < TOL, 'Original shooting tolerance not met')
    require(vector(response['heightJetJacobian'], 616), 'Missing finite original 616-entry Jacobian')
    jets = response['jets']
    require(type(jets) is dict and set(jets) == JET_SCALARS | JET_ARRAYS
            and all(number(jets[k]) for k in JET_SCALARS)
            and all(vector(jets[k], M) for k in JET_ARRAYS), 'Invalid 17-field M14 cut jets')
    if audit:
        require(type(response['audit']) is dict and set(response['audit']) == AUDIT_FIELDS
                and all(number(x) for x in response['audit'].values()), 'Invalid original eight-field source audit')
    else:
        require(response['audit'] is None, 'Unexpected audit on an unaudited request')
    history = response['history']
    require(type(history) is list and len(history) > 0, 'Missing original shooting history')
    for row in history:
        require(type(row) is dict and type(row.get('iteration')) is int and row['iteration'] >= 0
                and all(number(row.get(k)) for k in ('norm','minA','minD'))
                and all(number(row[k]) for k in ('step','chartCondition') if k in row),
                'Invalid original history row')
    cp = response['checkpoint']
    require(type(cp) is dict and set(cp) == {'parameters','states','rawNode','rawStates','cutHeight','scope'},
            'Unexpected finite-tail checkpoint schema')
    equal(c.without_io(cp['parameters']), c.without_io(context['prior']['response']['checkpoint']['parameters']),
          'Resolved original geometry/discretization differs')
    for key in c.IO_FIELDS:
        equal((key in cp['parameters'], cp['parameters'].get(key)),
              (key in context['config'], context['config'].get(key)), 'Resolved I/O differs: ' + key)
    equal(cp['cutHeight'], height, 'Checkpoint physical cut label differs')
    require(type(cp['states']) is list and len(cp['states']) == 865
            and all(vector(row, 28) for row in cp['states']), 'Expected finite 865 by 28 staged states')
    require(type(cp['rawNode']) is list and all(type(v) is int for v in cp['rawNode']), 'Invalid raw node types')
    equal(cp['rawNode'], list(range(0, 865, 72)), 'Changed original raw-stage layout')
    require(type(cp['rawStates']) is list and len(cp['rawStates']) == 13
            and all(vector(row, 28) for row in cp['rawStates']), 'Invalid finite raw-state shape')
    equal(cp['rawStates'], [cp['states'][i] for i in cp['rawNode']], 'Raw-state mirror mismatch')
    require(type(cp['scope']) is str, 'Missing finite checkpoint scope')
    return {'packet': identity(path), 'residual': response['residual'], 'history_rows': len(history),
            'last_history_norm': history[-1]['norm'], 'Jacobian_entries': 616, 'jets_fields': 17,
            'audit_fields': 8 if audit else 0, 'states': [865,28], 'raw_states': [13,28],
            'scope': 'Original finite DN only; last history base norm need not equal final residual.'}


def first_packet(context):
    out = context['out']; path = Path(str(out) + '-first-request-binding.json')
    first = read(path)
    require(first['status'] == 'ACTUAL_FIRST_DN_CLOSED_BEFORE_INNER_BVP', 'Missing actual first-call evidence')
    equal(first['launch'], identity(context['launch']['launch_path']), 'First call belongs to another launch')
    equal(first['selector'], identity(HERE / 'db6f-prefix-spectral-true-m14-direct-csc.py'), 'First-call selector identity differs')
    packet = Path(str(out) + '_tail_0001.json.gz')
    equal(first['packet'], identity(packet), 'First packet binding differs')
    report = check_packet(packet, first['request_height'], False, context)
    equal(first['packet_checks'], report, 'First-call saved checks differ')
    return {'status': 'PASS_FIRST_ACTUAL_M14_DN_ONLY', 'first_request_binding': identity(path), **report}


def polynomial_endpoint(cp, context):
    import numpy as np
    from scipy.interpolate import PPoly
    out = context['out']; n = cp['nodes']
    require(type(n) is int and 2 <= n <= 6500 and vector(cp['mesh'], n), 'Invalid final physical mesh')
    mesh = np.asarray(cp['mesh'], float)
    require(mesh[0] == 0 and mesh[-1] == cp['meridian_length'] and np.all(np.diff(mesh) > 0),
            'Saved mesh does not span the full physical interval')
    blocks = cp['pp_coefficient_chunks']; arrays = []; files = []; state = 0
    require(type(blocks) is list and len(blocks) > 0, 'Missing saved physical coefficients')
    for index, block in enumerate(blocks):
        require(type(block) is dict and block['file'] == out.name + f'_coeff_{index:02d}.npy.gz',
                'Coefficient file belongs to another run')
        path = out.parent / block['file']; row = identity(path)
        require(row['bytes'] == block['bytes'] and row['sha256'] == block['sha256']
                and row['bytes'] < 5_000_000, 'Coefficient byte/hash/size mismatch')
        array = np.load(io.BytesIO(gzip.decompress(path.read_bytes())), allow_pickle=False)
        require(array.dtype == np.dtype('float64') and array.ndim == 3
                and array.shape[:2] == (6,n-1) and array.shape[2] > 0
                and np.all(np.isfinite(array)), 'Invalid finite quintic coefficient array')
        require(type(block['state_first']) is int and type(block['state_last_exclusive']) is int
                and block['state_first'] == state
                and block['state_last_exclusive'] == state + array.shape[2], 'Noncontiguous coefficient state partition')
        state += array.shape[2]; arrays.append(array); files.append(row)
    require(state == 43, 'Physical prefix does not cover all 43 states')
    coefficients = np.concatenate(arrays, axis=2)
    pp = PPoly.construct_fast(coefficients, mesh, extrapolate=True, axis=1)
    value = pp(np.array([mesh[-1]]))
    require(value.shape == (43,1) and np.all(np.isfinite(value)), 'Invalid saved endpoint value')
    # Same frozen outward bridge has sigma=-1. This is the original seam
    # expression evaluated on the actual saved PPoly, not a new ODE call.
    height = (-cp['gauge_amplitude'] * value[2*M+1:,0]).tolist()
    return height, files, {'shape': list(coefficients.shape), 'all_coefficients_finite': True,
                           'minimum_span': float(np.min(np.diff(mesh)))}


def check_newton_lifetime_record(record, context):
    require(type(record) is dict and set(record) == {
        'schema','original_definition','selected_runtime','selector','scipy_bvp_source',
        'original_STATS_alias','changed_runtime_identity','scope'},
        'Incomplete explicit Newton runtime schema')
    equal(record['schema'], 'db6f-newton-lu-lifetime-runtime-v1', 'Wrong selected Newton schema')
    equal(record['original_definition'], context['launch']['callbacks']['domain_solve_newton'],
          'Original Newton provenance differs')
    equal(record['selector'], identity(c.LIFETIME_SELECTOR), 'Lifetime selector source differs')
    expected = context['launch']['callbacks']['selected_domain_solve_newton']
    require(type(record['selected_runtime']) is dict and
            set(record['selected_runtime']) == set(expected) | {'runtime_module','signature'},
            'Selected function record is incomplete')
    for key, value in expected.items():
        equal(record['selected_runtime'][key], value, 'Selected Newton function identity differs')
    equal(record['selected_runtime']['runtime_module'], 'db6f_lu_lifetime_selected_definition_v1',
          'Unexpected selected Newton runtime module')
    equal(record['selected_runtime']['signature'],
          '(n, m, h, col_fun, bc, jac, y, p, B, bvp_tol, bc_tol)',
          'Selected Newton signature differs')
    scipy_rows = [row for row in context['launch']['bindings']
                  if Path(row['path']).name == '_bvp.py'
                  and row['sha256'] == '59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2']
    require(len(scipy_rows) == 1, 'Ambiguous original SciPy layout binding')
    equal(record['scipy_bvp_source'], scipy_rows[0], 'Selected Newton used a different SciPy layout')
    require(record['original_STATS_alias'] is True and record['changed_runtime_identity'] is True,
            'The selected source or original STATS alias was not honestly recorded')


def _compiled_runtime_record(row, path, qualname, module):
    """Compile pinned text only; never execute a callback or scientific source."""
    gate = c.module('closed_csc_identity_gate', c.CSC_GATES)
    gate.runtime_function_record(row)
    require(Path(row['filename']).resolve() == Path(path).resolve()
            and row['module'] == module and row['qualname'] == qualname,
            'Runtime function source/module/name differs')
    code = compile(Path(path).read_bytes(), row['filename'], 'exec', dont_inherit=True)
    for name in (part for part in qualname.split('.') if part != '<locals>'):
        candidates = [value for value in code.co_consts
                      if isinstance(value, CodeType) and value.co_name == name]
        require(len(candidates) == 1, 'Ambiguous compiled runtime function')
        code = candidates[0]
    equal(row['firstlineno'], code.co_firstlineno, 'Runtime function line differs')
    equal(row['code_sha256'], hashlib.sha256(marshal.dumps(code)).hexdigest(),
          'Runtime function code digest differs from pinned source')


def check_csc_runtime_record(record, context):
    keys = {'schema','definitions','prerequisite_inputs','tested_factory_normalized_sha256',
            'factory_provenance','original_runtime','selected_runtime',
            'foundation_helper_runtime','newton_runtime_unchanged',
            'only_backend_prepare_attribute_changed','old_exported_construct_and_indices_retained',
            'no_old_global_coo_index_closure','scope'}
    require(type(record) is dict and set(record) == keys
            and record['schema'] == 'db6f-explicit-direct-csc-runtime-v1',
            'Missing explicit CSC runtime identity')
    equal(record['definitions'],context['launch']['csc_selection_definitions'],
          'CSC runtime definitions differ')
    prerequisites = context['csc_prerequisites']
    equal(record['prerequisite_inputs'],prerequisites['inputs'],'CSC actual prerequisites differ')
    equal(record['tested_factory_normalized_sha256'],
          prerequisites['tested_factory_normalized_sha256'],'CSC tested factory differs')
    gate = c.module('closed_csc_actual_factory_gate',c.CSC_GATES)
    equal(gate.normalized_provenance(record['factory_provenance'],gate.RUNTIME_MODULE),
          gate.normalized_provenance(prerequisites['tested_factory_provenance'],gate.TEST_MODULE),
          'Runtime CSC factory did not match the actually byte-tested environment')
    equal(record['selected_runtime'],record['factory_provenance']['new_functions'],
          'Selected new function identities differ from factory')
    bvp_path = prerequisites['source_files']['scipy.integrate._bvp']['path']
    require(type(record['original_runtime']) is dict and set(record['original_runtime']) ==
            {'prepare_sys','construct_global_jac','compute_jac_indices','solve_bvp'},
            'Original exported runtime identities incomplete')
    for name,row in record['original_runtime'].items():
        _compiled_runtime_record(row,bvp_path,name,'scipy.integrate._bvp')
    require(type(record['foundation_helper_runtime']) is dict and
            set(record['foundation_helper_runtime']) == {'dimensions','column_segments','_assemble_csc'},
            'Foundation storage helper identities incomplete')
    for name,row in record['foundation_helper_runtime'].items():
        _compiled_runtime_record(row,c.CSC_FOUNDATION,name,gate.RUNTIME_MODULE)
    for name,row in record['selected_runtime'].items():
        _compiled_runtime_record(row,c.CSC_FOUNDATION,'make_functions.<locals>.'+name,gate.RUNTIME_MODULE)
    _compiled_runtime_record(record['newton_runtime_unchanged'],c.LIFETIME_NEWTON,
                             'solve_newton','db6f_lu_lifetime_selected_definition_v1')
    for key in ('only_backend_prepare_attribute_changed','old_exported_construct_and_indices_retained',
                'no_old_global_coo_index_closure'):
        require(record[key] is True,'CSC changed an unreviewed runtime/closure identity')
    require(type(record['scope']) is str,'Missing runtime identity scope')


def check_csc_restoration(record, context):
    require(type(record) is dict and set(record) ==
            {'schema','before_restore','restored_original_prepare','newton_runtime_unchanged',
             'backend_prepare_restored','scope'}
            and record['schema'] == 'db6f-explicit-direct-csc-restoration-v1',
            'Missing explicit original-prepare restoration')
    check_csc_runtime_record(record['before_restore'],context)
    equal(record['restored_original_prepare'],
          record['before_restore']['original_runtime']['prepare_sys'],
          'Restored prepare is not the original function')
    equal(record['newton_runtime_unchanged'],record['before_restore']['newton_runtime_unchanged'],
          'Restoration changed the separately selected Newton')
    require(record['backend_prepare_restored'] is True and type(record['scope']) is str,
            'Original prepare restoration did not pass')


def check_runtime_records(records, calls, context, cp):
    checks = cp['actual_outer_checks']
    require(type(records) is list and type(calls) is list and len(records) == len(calls) == len(checks),
            'Original successful outer checks and spectral calls do not correspond')
    for index, (record, call) in enumerate(zip(records, calls), 1):
        equal(record['call'], index, 'Wrong spectral call numbering')
        require(record['status'] == 'RETURNED_PHYSICAL_COORDINATES'
                and record['weighted_solver_success'] is True and record['success'] is True
                and record['original_physical_residual_gate_passed'] is True
                and record['coordinate_roundtrips_passed'] is True, 'Inner spectral/physical gate did not pass')
        for key, expected in [('original_tol',2e-9),('original_bc_tol',1e-8),
                              ('maximum_nodes',6500),('state_components',43),('parameters',14)]:
            equal(record[key], expected, 'Changed spectral call option: ' + key)
        equal(record['weights'], context['launch']['weights'], 'Changed actual weights')
        require(number(record['weighted_rms_max']) and record['weighted_rms_max'] >= 0
                and type(record['initial_nodes']) is int and 2 <= record['initial_nodes'] <= 6500
                and type(record['final_nodes']) is int and 2 <= record['final_nodes'] <= 6500,
                'Invalid actual finite collocation diagnostics')
        equal(record['ppoly_axis'], 1, 'Unexpected returned physical PPoly axis')
        require(number(record['original_physical_rms_max']) and 0 <= record['original_physical_rms_max'] <= TOL
                and number(record['original_physical_bc_max']) and 0 <= record['original_physical_bc_max'] <= 1e-8,
                'Original physical inner residual not met')
        require(type(call.get('call')) is int and call['call'] == index
                and call.get('returned_success') is True and 'error' not in call,
                'Runtime callback record did not close successfully')
        for key in ('before_newton','after_newton'):
            check_newton_lifetime_record(call[key], context)
        for key in ('before_csc','after_csc'):
            check_csc_runtime_record(call[key], context)
        require(type(call['physical_callbacks']) is dict and set(call['physical_callbacks']) ==
                {'fun','fun_jac','bc','bc_jac','terminal','initial','chart','physical_fun',
                 'physical_fun_jac','physical_c2_interpolant','affine_dn','seam_audit',
                 'flow_selector','save_checkpoint'}, 'Incomplete runtime physical callback identities')
        equal(record['scipy_bvp_sha256'], '59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2',
              'Unreviewed SciPy layout in runtime record')
        for key, entry in call['physical_callbacks'].items():
            for name, value in context['launch']['callbacks'][key].items():
                equal(entry[name], value, 'Runtime physical callback source differs: '+key)
    equal(records[-1]['original_physical_rms_max'], cp['max_rms_collocation_residual'],
          'Saved original physical RMS is not the final weighted-call physical RMS')
    equal(records[-1]['final_nodes'], cp['nodes'], 'Saved node count differs from final physical return')


def check_outputs(context, records, calls):
    out = context['out']; cp_path = out.with_suffix('.json.gz'); summary_path = Path(str(out)+'-summary.json')
    summary, cp = read(summary_path), read(cp_path)
    require(summary.get('error') is None and summary.get('solver_success') is True
            and cp.get('solver_success') is True, 'Original coupled program did not close a successful prefix')
    equal({k:v for k,v in cp.items() if k not in {'mesh','pp_coefficient_chunks','array_format','seconds'}},
          {k:v for k,v in summary.items() if k != 'seconds'}, 'Original final CP and summary disagree')
    equal(cp['config'], dict(modes=14,base_mode=3,core_kind='adaptive_warped_support',angular=512,
        tol=2e-9,bc_tol=1e-8,physical_bc_tol=2e-11,fixed_metric=True,actual_nonlinear_tail=True),
        'Changed original true-prefix options')
    equal(cp['tail_config'], context['config'], 'Final tail config differs')
    for key in FIXED_FIELDS:
        equal(cp[key], context['seed'][key], 'Fixed physical definition changed: ' + key)
    require(vector(cp['parameters'],14) and vector(cp['central_correction_scales'],13)
            and number(cp['actual_primary_amplitude']), 'Invalid final free parameters')
    require(number(cp['max_rms_collocation_residual']) and 0 <= cp['max_rms_collocation_residual'] <= TOL,
            'Original physical collocation tolerance not attained')
    require(cp['dn_solver'] == 'outer_actual_inner_affine', 'Wrong original actual-DN outer algorithm')
    checks = cp['actual_outer_checks']
    require(type(checks) is list and 1 <= len(checks) <= 8, 'Missing original true outer checks')
    for index, row in enumerate(checks):
        require(type(row.get('outer')) is int and row['outer'] == index and row.get('inner_success') is True
                and number(row.get('actual_boundary_residual')) and row['actual_boundary_residual'] >= 0
                and number(row.get('actual_tail_residual')) and 0 <= row['actual_tail_residual'] < TOL
                and type(row.get('tail_calls')) is int and row['tail_calls'] > 0,
                'Invalid original outer-check record')
    last = checks[-1]
    require(last['actual_boundary_residual'] <= 1e-8, 'Original nonlinear outer BC did not pass')
    outer_path = Path(str(out) + f"_tail_{last['tail_calls']:04d}.json.gz")
    outer = read(outer_path)
    outer_report = check_packet(outer_path, outer['request']['height'], False, context)
    equal(outer_report['residual'], last['actual_tail_residual'], 'Outer BC used a different actual response')
    # Outer height belongs to the inner node solution. Do not force bitwise
    # equality with the subsequently constructed quintic endpoint.
    height, chunks, polynomial = polynomial_endpoint(cp, context)
    seam = cp['tail_seam']
    require(type(seam) is dict and set(seam) == SEAM_NUMBERS |
            {'scope','tail_record','tail_converged','tail_shooting_residual','tail_jets','angular_samples'}
            and all(number(seam[k]) for k in SEAM_NUMBERS), 'Missing finite complete original seam')
    equal(seam['angular_samples'], 896, 'Wrong M14 seam sampling count')
    require(type(cp['tail_calls']) is int and cp['tail_calls'] > last['tail_calls'], 'Missing later actual audit call')
    seam_path = Path(str(out) + f"_tail_{cp['tail_calls']:04d}.json.gz")
    require(seam['tail_record'] == seam_path.name, 'Wrong final seam record identity')
    final_report = check_packet(seam_path, height, True, context)
    final_response = read(seam_path)['response']
    for key, actual in [('tail_converged',final_response['converged']),
                        ('tail_shooting_residual',final_response['residual']),('tail_jets',final_response['jets'])]:
        equal(seam[key], actual, 'Original seam metadata differs from actual response')
    sampled = cp['summary']
    for key in ('metric_l1','flow_defect','darboux_l1','kappa_sample','radius_max','height_max',
                'root_min','chart_rho_min','support_amplitude','terminal_height_coeff_max','physical_bc_max'):
        require(number(sampled.get(key)), 'Nonfinite original sampled diagnostic: ' + key)
    equal(sampled['samples_psi'], 1024, 'Wrong original prefix angular audit')
    require(type(sampled['samples_s']) is int and sampled['samples_s'] > 0, 'Missing radial audit samples')
    check_runtime_records(records, calls, context, cp)
    first = first_packet(context)
    required_files = [identity(cp_path),identity(summary_path),identity(outer_path),identity(seam_path),
                      first['first_request_binding'],first['packet']] + chunks
    unique = {row['path']: row for row in required_files}
    return {'status':'PASS_DIRECT_CSC_FINITE_M14_PROGRAM_OUTPUTS','prefix_CP':identity(cp_path),
            'summary':identity(summary_path),'outer':outer_report,'final_audit':final_report,
            'first_actual_DN':first,'coefficients':polynomial,'outer_checks':len(checks),
            'original_physical_rms':cp['max_rms_collocation_residual'],
            'original_actual_BC':last['actual_boundary_residual'],
            'sampled_prefix_metric':sampled['metric_l1'],
            'source_tail_actualMetric':final_response['audit']['actualMetric'],
            'required_closed_files':sorted(unique.values(),key=lambda r:r['path']),
            'scope':'Finite original solver gates only; no continuous XYZ, reach or exact-limit certificate.'}


def final_audit(context, observed):
    require(observed is not None, 'NOT_READY: root actual tool-exit observation is required')
    obs = read(observed); out = context['out']
    require(obs.get('status') == 'observed-process-completed' and obs.get('observer') == '/root'
            and type(obs.get('actual_exit_code')) is int and type(obs.get('session_id')) is int
            and obs['session_id'] > 0 and type(obs.get('tool_receipt')) is str and bool(obs['tool_receipt'])
            and obs.get('stem') in (out.name,str(out)), 'Wrong actual root observation identity')
    require(obs['actual_exit_code'] == 0, 'Root observed a nonzero tool exit')
    repro_path = Path(str(out)+'-reproduction.json'); repro = read(repro_path)
    equal(repro['launch'], identity(context['launch']['launch_path']), 'Reproduction launch differs')
    equal(repro['source_bindings'], context['launch']['bindings'], 'Reproduction source closure differs')
    equal(repro['actual_command'], context['launch']['command'], 'Actual selector argv differs')
    equal(repro['delegated_parser_argv'], context['launch']['delegated_parser_argv'], 'Delegated original argv differs')
    equal(repro['newton_lifetime_definitions'], context['launch']['newton_lifetime_definitions'],
          'Reproduction omitted or changed the explicit new Newton definitions')
    equal(repro['schema'],'db6f-spectral-true-m14-direct-csc-program-record-v1',
          'Wrong explicit CSC reproduction schema')
    equal(repro['csc_prerequisites'],context['csc_prerequisites'],'Reproduction omitted actual prerequisites')
    equal(repro['csc_selection_definitions'],context['launch']['csc_selection_definitions'],
          'Reproduction CSC definition identity differs')
    check_csc_runtime_record(repro['csc_selection'],context)
    check_csc_restoration(repro['csc_restoration'],context)
    require('csc_restore_error' not in repro,'CSC restoration reported an error')
    calls=repro['runtime_call_audits']
    require(type(calls) is list and len(calls)>0,'No actual selected BVP calls')
    equal(repro['csc_selection'],calls[0]['before_csc'],'Initial CSC identity differs from first call')
    equal(repro['csc_restoration']['before_restore'],calls[-1]['after_csc'],
          'Restored CSC identity differs from last closed call')
    selection = repro['newton_selection']
    require(type(selection) is dict and set(selection) == {
        'before_selection_original_runtime','selected','scope'}, 'Missing original-to-new identity transition')
    before = selection['before_selection_original_runtime']
    expected = context['launch']['callbacks']['domain_solve_newton']
    require(type(before) is dict and set(before) == set(expected) | {'runtime_module','signature'},
            'Original runtime transition record incomplete')
    for key, value in expected.items():
        equal(before[key], value, 'Original runtime identity at selection differs')
    equal(before['runtime_module'], 'f6curve_domain_newton', 'Wrong original installed Newton module')
    equal(before['signature'], '(n, m, h, col_fun, bc, jac, y, p, B, bvp_tol, bc_tol)',
          'Original installed Newton signature differs')
    check_newton_lifetime_record(selection['selected'], context)
    require(repro.get('status') == 'DIRECT_CSC_FINITE_M14_COUPLED_PROGRAM_SUCCESS'
            and repro.get('mathematical_success') is True and repro.get('error') is None
            and type(repro.get('requested_process_exit_code')) is int
            and repro['requested_process_exit_code'] == 0, 'Program did not close successfully')
    report = check_outputs(context,repro['spectral_coordinate_calls'],repro['runtime_call_audits'])
    equal(repro['closed_output_checks'], report, 'Program closed-output binding differs from independent reread')
    required = {row['path']: row for row in report['required_closed_files']}
    for path in (repro_path,Path(context['launch']['launch_path'])):
        row=identity(path); required[row['path']]=row
    require(type(obs.get('files')) is list, 'Root observation must bind closed outputs')
    observed_rows = {}
    for row in obs['files']:
        verify(row); require(row['path'] not in observed_rows, 'Duplicate root output binding')
        observed_rows[row['path']] = row
    for path, row in required.items():
        equal(observed_rows.get(path), row, 'Root observation omitted or changed closed file: '+path)
    report.update(status='PASS_ROOT_OBSERVED_TRUE_M14_W14_DIRECT_CSC_FINITE_COUPLED_CLOSE',
                  root_observation=identity(observed),reproduction=identity(repro_path))
    return report


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--launch',type=Path,required=True)
    parser.add_argument('--mode',choices=('first','final'),default='final')
    parser.add_argument('--observed-execution',type=Path)
    parser.add_argument('--out',type=Path)
    parser.add_argument('--check-current-gate',action='store_true')
    args=parser.parse_args()
    require(not args.check_current_gate or args.out is None, 'Negative gate inspection writes no file')
    report={'scope':__doc__,'mode':args.mode,'ready':False,'solver_calls':0,'active_trace_read':False}
    code=2
    try:
        context=c.validate_inputs(read(args.launch))
        require(args.launch.resolve()==Path(context['launch']['launch_path']), 'Wrong launch file')
        if args.mode=='first':
            require(args.observed_execution is None, 'First packet is not a process-exit audit')
            report.update(first_packet(context))
        else:
            report.update(final_audit(context,args.observed_execution))
        report['ready']=True;code=0
    except (ValueError,KeyError,FileNotFoundError) as error:
        report.update(status='NOT_READY_OR_REJECTED',reason=repr(error))
    if args.out is not None:
        c.write_json(args.out.resolve(),report,exclusive=True)
    print(json.dumps({k:report[k] for k in ('status','ready','mode','solver_calls','active_trace_read')}
                     | ({'reason':report['reason']} if 'reason'in report else {})))
    return code


if __name__=='__main__':
    import sys
    sys.exit(main())
