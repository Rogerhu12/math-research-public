#!/usr/bin/env python3
"""Closed prerequisite and provenance gates for the future direct-CSC entry.

Standard library only. Import and every function in this file install nothing,
construct no candidate or matrix, and call no numerical callback or solver.
An author plan or static review is never accepted as an executed check report.
"""
import ast
import copy
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FOUNDATION = HERE / 'db6f-prefix-direct-csc-foundation-v2.py'
PURE_CHECKER = HERE / 'db6f-prefix-check-direct-csc-foundation.py'
BYTE_CHECKER = HERE / 'db6f-prefix-test-direct-csc-bytes.py'
FOUNDATION_SHA = '8e2bb061ef1fee94672601132cedb8ca7565d4006a327474f039f501e5f516cf'
PURE_CHECKER_SHA = 'e437630f9718a898b31d16b21a2616034b0984d17a6b05ac5913f6cc7ec509dd'
BYTE_CHECKER_SHA = '197da92ec9ca8768c1b5a876aeed2b5164056fa7e3a3b3d790cd9eb626ee5bbc'
BVP_SHA = '59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2'
SCIPY_SOURCES = {
    'scipy.integrate._bvp': BVP_SHA,
    'scipy.sparse._coo': '95e4bcd796900894acea3256a7b5a4cab654427bb9fcb9f0e57ec9fb40dc6898',
    'scipy.sparse._compressed': 'd8d847ceb10469b91dc2f64e2be7ec3af04e1a099db9fbb91fb32526f860dc0f',
    'scipy.sparse._sputils': 'b1cdc32d7e49fab5add7ec14f0858321275186e083362e6cc2628f6fef5a641f',
    'scipy.sparse._csc': '88c462e71172169295fa8e1f7ff23d4a3c0037e847a7b6037e74c812ee236552',
    'scipy.sparse._base': 'e6d70fd65f0378f198cdf0c83986aa3b477f87da47137037ef6056d42481fd1b',
}
ORIGINAL_CALLBACKS = {
    'stacked_matmul', 'collocation_fun', 'estimate_fun_jac', 'estimate_bc_jac',
    'get_index_dtype', 'csc_init', 'csc_check_format', 'csc_prune',
    'csc_get_index_dtype', 'csc_swap',
}
NEW_FUNCTIONS = {'construct_global_jac', 'prepare_sys'}
RUNTIME_MODULE = 'db6f_direct_csc_selected_foundation_v2'
TEST_MODULE = '_db6f_direct_csc_small_byte_test'
EVIDENCE_KEYS = ('pure_report', 'pure_observed', 'byte_report', 'byte_observed')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def equal(left, right, message):
    require(canonical(left) == canonical(right), message)


def identity(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return {'path': str(path), 'bytes': len(raw),
            'sha256': hashlib.sha256(raw).hexdigest()}


def _pairs(items):
    result = {}
    for key, value in items:
        require(key not in result, 'Duplicate JSON key: ' + key)
        result[key] = value
    return result


def _bad_constant(value):
    raise ValueError('Nonfinite JSON token: ' + value)


def read(path):
    raw = Path(path).read_bytes()
    require(len(raw) < 1_000_000, 'Prerequisite metadata is not a small JSON document')
    return json.loads(raw.decode('utf-8'), object_pairs_hook=_pairs,
                      parse_constant=_bad_constant)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def checked_file(row, key='path', expected_sha=None):
    require(type(row) is dict and type(row.get(key)) is str, 'Missing file identity')
    actual = identity(row[key])
    require(type(row.get('sha256')) is str and row['sha256'] == actual['sha256'],
            'Changed bound file: ' + row[key])
    if 'bytes' in row:
        equal(row['bytes'], actual['bytes'], 'Changed bound file size')
    if expected_sha is not None:
        require(actual['sha256'] == expected_sha, 'Unexpected frozen source identity')
    return actual


def source_definitions():
    """Read/parse only the three pinned source files; no Python source execution."""
    records = {}
    for key, path, expected in (
        ('foundation', FOUNDATION, FOUNDATION_SHA),
        ('pure_checker', PURE_CHECKER, PURE_CHECKER_SHA),
        ('byte_checker', BYTE_CHECKER, BYTE_CHECKER_SHA),
    ):
        row = identity(path)
        require(row['sha256'] == expected, 'Changed source: ' + key)
        ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
        records[key] = row
    text = FOUNDATION.read_text(encoding='utf-8')
    tree = ast.parse(text)
    factories = [node for node in tree.body
                 if isinstance(node, ast.FunctionDef) and node.name == 'make_functions']
    require(len(factories) == 1, 'Ambiguous foundation factory')
    definitions = {}
    for name in sorted(NEW_FUNCTIONS):
        nodes = [node for node in factories[0].body
                 if isinstance(node, ast.FunctionDef) and node.name == name]
        require(len(nodes) == 1 and not nodes[0].decorator_list, 'Ambiguous nested function')
        node = nodes[0]
        definitions[name] = {
            'file': records['foundation'], 'qualname': 'make_functions.<locals>.' + name,
            'first_line': node.lineno,
            'source_sha256_rstrip': hashlib.sha256(
                ast.get_source_segment(text, node).rstrip().encode()).hexdigest(),
        }
    return {'schema': 'db6f-direct-csc-entry-definitions-v1',
            'gates': identity(__file__), **records, 'new_functions': definitions,
            'installed': False, 'numerical_calls': 0}


def source_map(rows):
    require(type(rows) is list and len(rows) == len(SCIPY_SOURCES),
            'Expected exactly the six frozen SciPy modules')
    result = {}
    for row in rows:
        require(type(row) is dict and row.get('module') in SCIPY_SOURCES
                and row['module'] not in result, 'Missing or repeated SciPy module')
        actual = checked_file(row, 'file', SCIPY_SOURCES[row['module']])
        result[row['module']] = actual
    require(set(result) == set(SCIPY_SOURCES), 'Incomplete SciPy source set')
    return result


def runtime_function_record(row):
    require(type(row) is dict and set(row) ==
            {'module','qualname','filename','firstlineno','code_sha256'},
            'Invalid runtime function identity schema')
    require(all(type(row[name]) is str and row[name]
                for name in ('module','qualname','filename','code_sha256'))
            and type(row['firstlineno']) is int and row['firstlineno'] > 0
            and len(row['code_sha256']) == 64
            and all(c in '0123456789abcdef' for c in row['code_sha256']),
            'Invalid runtime function identity values')


def check_provenance(value, module_name):
    require(type(value) is dict and value.get('schema') ==
            'db6f-direct-canonical-csc-functions-v2', 'Wrong factory provenance')
    equal(checked_file(value['foundation'], 'file', FOUNDATION_SHA),
          identity(FOUNDATION), 'Factory used another foundation path')
    sources = source_map(value['sources'])
    require(type(value.get('numpy_version')) is str and value['numpy_version']
            and type(value.get('scipy_version')) is str and value['scipy_version'],
            'Missing actual environment versions')
    require(type(value.get('original_callbacks')) is dict
            and set(value['original_callbacks']) == ORIGINAL_CALLBACKS
            and type(value.get('new_functions')) is dict
            and set(value['new_functions']) == NEW_FUNCTIONS, 'Incomplete factory runtime identities')
    for row in value['original_callbacks'].values():
        runtime_function_record(row)
    definitions = source_definitions()['new_functions']
    for name, row in value['new_functions'].items():
        runtime_function_record(row)
        require(row['module'] == module_name
                and row['qualname'] == definitions[name]['qualname']
                and Path(row['filename']).resolve() == FOUNDATION.resolve()
                and row['firstlineno'] == definitions[name]['first_line'],
                'New function is not the explicitly named foundation closure')
    require(value.get('actual_sparse_byte_replay') == 'pending',
            'Factory snapshot must not be rewritten into a byte-test success')
    return sources


def normalized_provenance(value, module_name):
    """Only a loader module label differs between the test and the real entry."""
    check_provenance(value, module_name)
    result = copy.deepcopy(value)
    result['sources'] = sorted(result['sources'], key=lambda row: row['module'])
    for row in result['new_functions'].values():
        row['module'] = '<explicit-loader-label>'
    return result


def expected_specs():
    """Read the literal specs() return from the pinned test; never import it."""
    tree = ast.parse(BYTE_CHECKER.read_text(encoding='utf-8'))
    functions = [node for node in tree.body if isinstance(node, ast.FunctionDef)
                 and node.name == 'specs']
    require(len(functions) == 1 and len(functions[0].body) == 1
            and isinstance(functions[0].body[0], ast.Return), 'Test spec source changed')
    specs = ast.literal_eval(functions[0].body[0].value)
    require(type(specs) is list and len(specs) == 15, 'Wrong reviewed synthetic suite')
    return specs


def observed_check(path, report_path, script, required, option_paths):
    """Require root's actual tool observation, not a program-requested code."""
    observed = read(path)
    require(observed.get('status') == 'observed-process-completed'
            and observed.get('observer') == '/root'
            and type(observed.get('actual_exit_code')) is int
            and observed['actual_exit_code'] == 0
            and type(observed.get('tool_receipt')) is str and observed['tool_receipt'],
            'NOT_READY: no successful actual root tool observation')
    # Fast checks need not have a long-running session id.
    argv = observed.get('command')
    require(type(argv) is list and all(type(x) is str for x in argv)
            and len(argv) == 2 + 2 * len(option_paths), 'Missing exact observed check command')
    require(Path(argv[1]).resolve() == script.resolve(), 'Observed a different check script')
    # The executable must be explicitly resolved by the observer. This avoids
    # accepting an unverified PATH alias as proof of the current interpreter.
    require(Path(argv[0]).is_absolute()
            and Path(argv[0]).resolve() == Path(sys.executable).resolve(),
            'Observation must name the actual current Python executable')
    options = {}
    for index in range(2, len(argv), 2):
        key, value = argv[index:index+2]
        require(key in option_paths and key not in options, 'Unknown/duplicate check argument')
        options[key] = str(Path(value).resolve())
    equal(options, {key: str(Path(value).resolve()) for key, value in option_paths.items()},
          'Observed check input or output paths differ')
    equal(options['--out'], str(Path(report_path).resolve()), 'Observed output is not this report')
    require(type(observed.get('files')) is list, 'Actual observation must bind closed files')
    rows = {}
    for row in observed['files']:
        actual = checked_file(row)
        equal(row, actual, 'Observation file record is not a complete byte identity')
        require(actual['path'] not in rows, 'Duplicate observed file')
        rows[actual['path']] = actual
    for row in required:
        equal(rows.get(row['path']), row, 'Observation omitted a required closed check/source file')
    return identity(path), rows


def prerequisite_evidence(pure_report, pure_observed, byte_report, byte_observed):
    """Closed metadata gate; it performs no test itself and grants no solver success."""
    definitions = source_definitions()
    paths = {key: Path(value).resolve() for key, value in zip(
        EVIDENCE_KEYS, (pure_report,pure_observed,byte_report,byte_observed))}
    require(len(set(paths.values())) == 4, 'The four prerequisite documents must be distinct')
    pure = read(paths['pure_report'])
    require(pure.get('schema') == 'db6f-direct-canonical-csc-source-integer-check-v1'
            and pure.get('status') == 'PASS_SOURCE_AND_INTEGER_LAYOUT_ONLY',
            'NOT_READY: no completed actual source/integer check')
    equal(checked_file(pure['checker'],'file',PURE_CHECKER_SHA), definitions['pure_checker'],
          'Pure report checker differs')
    equal(checked_file(pure['foundation'],'file',FOUNDATION_SHA), definitions['foundation'],
          'Pure report foundation differs')
    sources = source_map(pure['frozen_sources'])
    replay = pure['source_replay']
    for key in ('construct_text_replay','prepare_text_replay','construct_ast_replay','prepare_ast_replay'):
        require(replay.get(key) is True, 'Source/AST replay did not pass')
    for key, value in (('construct_replacements',3),('prepare_replacements',2),
                       ('parameter_midpoint_update_count',1),('old_global_coo_construction_present',False)):
        equal(replay.get(key),value,'Changed source replay invariant')
    integers = pure['integer_layout']
    expected = [{'n':n,'m':m,'k':k,'size':n*m+k,'stored':(2*n+k)*(n*m+k),
                 'indptr_entries':n*m+k+1,'canonical':True}
                for n in (1,2,5,43) for m in (2,3,7) for k in (0,1,14)]
    equal(integers['small_cases'],expected,'Incomplete 36-case integer replay')
    equal(integers['invalid_dimension_cases_rejected'],8,'Incomplete invalid-dimension checks')
    equal(integers['malformed_symbolic_layouts_rejected'],5,'Incomplete symbolic negative checks')
    equal(pure['factory_called'],False,'Pure checker called the factory')
    equal(pure['matrix_calls'],0,'Pure checker constructed a matrix')
    equal(pure['solver_calls'],0,'Pure checker called a solver')
    require(pure['actual_sparse_byte_replay'] == 'not performed',
            'Pure integer check incorrectly claims array execution')

    byte = read(paths['byte_report'])
    require(byte.get('schema') == 'db6f-direct-csc-small-byte-test-v1'
            and byte.get('status') == 'PASS_SMALL_SYNTHETIC_CSC_BYTES_AND_ALIAS_EFFECTS'
            and byte.get('stage') == 'completed' and 'error' not in byte,
            'NOT_READY: no completed actual small byte/alias replay')
    equal(byte.get('script_return_code'),0,'Byte program did not request successful exit')
    equal(checked_file(byte['script'],'file',BYTE_CHECKER_SHA),definitions['byte_checker'],
          'Byte report script differs')
    equal(checked_file(byte['foundation'],'file',FOUNDATION_SHA),definitions['foundation'],
          'Byte report foundation differs')
    equal(checked_file(byte['original_source'],'file',BVP_SHA),sources['scipy.integrate._bvp'],
          'Byte oracle was not the same frozen source')
    expected_counts = {'original_construct_attempts':15,'original_construct_completed':15,
                       'new_construct_attempts':15,'new_construct_completed':15,
                       'superlu_calls':0,'linear_solve_calls':0,'bvp_dn_rk_calls':0}
    equal(byte['counts'],expected_counts,'Incomplete byte replay or forbidden numerical calls')
    require(byte.get('original_function_bindings_unchanged') is True
            and byte.get('research_data_read') is False
            and byte.get('future_complete_entry_approved') is False
            and byte.get('factory_provenance_is_precomparison_snapshot') is True,
            'Byte report scope or unchanged-bindings gate differs')
    specs = expected_specs()
    require(type(byte['cases']) is list and len(byte['cases']) == len(specs),
            'Incomplete synthetic cases')
    for row, spec in zip(byte['cases'],specs):
        equal(row['id'],spec['id'],'Synthetic case order/identity differs')
        equal(row['spec'],spec,'Synthetic input recipe differs')
        require(row.get('post_cohort_exact_equal') is True
                and row.get('independent_mutable_runs') is True
                and row.get('immutable_seed_unchanged') is True,
                'Alias layout/side effects were not checked')
        n,m,k = spec['n'],spec['m'],spec['k']
        size, stored = n*m+k,(2*n+k)*(n*m+k)
        matrix = row['matrix']
        equal(matrix['shape'],[size,size],'Wrong synthetic matrix shape')
        equal(matrix['stored'],stored,'Explicit structural entries missing')
        require(matrix.get('canonical') is True and set(matrix['buffers']) ==
                {'data','indices','indptr'}, 'Missing canonical three-buffer comparison')
        for name, length in (('data',stored),('indices',stored),('indptr',size+1)):
            buffer = matrix['buffers'][name]
            equal(buffer['shape'],[length],'Wrong compared sparse buffer shape')
            require(type(buffer.get('dtype')) is str
                    and type(buffer.get('nbytes')) is int and buffer['nbytes'] > 0
                    and type(buffer.get('bytes_C_sha256')) is str
                    and len(buffer['bytes_C_sha256']) == 64,
                    'Incomplete actual sparse byte identity')
        if spec.get('require_mid_change'):
            require('df_dp_middle' in row['changed_input_views'],'Midpoint mutation not exercised')
        if spec.get('alias'):
            require('dbc_dya' in row['changed_input_views'] and 'dbc_dyb' in row['changed_input_views'],
                    'Boundary alias effects not exercised')
        zeros = matrix['signed_zero_counts']
        if spec.get('require_negative_real_zero'):
            require(type(zeros.get('negative_real_zero_count')) is int
                    and zeros['negative_real_zero_count'] > 0,'Negative real-zero case missing')
        if spec.get('require_negative_imaginary_zero'):
            require(type(zeros.get('negative_imaginary_zero_count')) is int
                    and zeros['negative_imaginary_zero_count'] > 0,'Negative imaginary-zero case missing')
    tested = byte['factory_provenance']
    equal(check_provenance(tested,TEST_MODULE),sources,'Test runtime source paths differ')
    equal(byte['numpy_version'],tested['numpy_version'],'Byte NumPy version differs')
    equal(byte['scipy_version'],tested['scipy_version'],'Byte SciPy version differs')
    require(type(byte['np_intc_itemsize']) is int and byte['np_intc_itemsize'] > 0,
            'Missing actual index-environment observation')

    scipy_root = Path(sources['scipy.integrate._bvp']['path']).parent.parent
    for module,row in sources.items():
        expected_path = scipy_root.joinpath(*module.split('.')[1:]).with_suffix('.py').resolve()
        require(Path(row['path']) == expected_path,'Six SciPy sources do not share one root')
    required_sources = list(sources.values()) + [definitions['foundation']]
    pure_required = required_sources + [definitions['pure_checker'],identity(paths['pure_report'])]
    byte_required = required_sources + [definitions['byte_checker'],identity(paths['byte_report'])]
    pure_obs, pure_rows = observed_check(paths['pure_observed'],paths['pure_report'],PURE_CHECKER,
        pure_required,{'--foundation':FOUNDATION,'--scipy-source-root':scipy_root,'--out':paths['pure_report']})
    byte_obs, byte_rows = observed_check(paths['byte_observed'],paths['byte_report'],BYTE_CHECKER,
        byte_required,{'--foundation':FOUNDATION,'--out':paths['byte_report']})
    bindings = {row['path']:row for row in required_sources + list(definitions[key] for key in
                ('gates','pure_checker','byte_checker')) + [pure_obs,byte_obs]
                + list(pure_rows.values()) + list(byte_rows.values())}
    for path in paths.values():
        row=identity(path);bindings[row['path']]=row
    return {'schema':'db6f-direct-csc-actual-prerequisites-v1',
            'status':'ACTUAL_CHECK_REPORTS_AND_ROOT_EXITS_VERIFIED',
            'inputs':{key:identity(path) for key,path in paths.items()},
            'definitions':definitions,'source_files':sources,
            'tested_factory_provenance':tested,
            'tested_factory_normalized_sha256':digest(normalized_provenance(tested,TEST_MODULE)),
            'synthetic_cases':15,'pure_integer_cases':36,
            'bindings':sorted(bindings.values(),key=lambda row:row['path']),
            'scope':'Prerequisites only; no new entry installation, BVP or coupled success.'}


def verify_prerequisites(saved):
    require(type(saved) is dict and type(saved.get('inputs')) is dict
            and set(saved['inputs']) == set(EVIDENCE_KEYS),'Missing closed prerequisite identities')
    paths=[]
    for key in EVIDENCE_KEYS:
        row=saved['inputs'][key];actual=checked_file(row)
        equal(row,actual,'Prerequisite input identity changed')
        paths.append(actual['path'])
    current=prerequisite_evidence(*paths)
    equal(saved,current,'Closed prerequisite evidence changed')
    return current
