"""Necessary restoration of the SAME completed TC signed96 matrix carriers.

No numerical import or IO at import.  The public consumer first admits the
whole completed TC, original P224 chain, RW and JC inputs.  This restores the
old TC exact dyadic trial_value array, then both whole signed matrix carriers,
requiring their ORIGINAL full hashes.  No old96 source, row-error, waist-norm
or matrix-norm target is called.  Original R133 nodal QR is never called.

The TC floating QR proposal is necessarily rematerialized and counted.  Its
unaltered AST prefix ends after all trial values, before the three unused
derivative arrays; the full original trial_value SHA is checked independently.
"""
from __future__ import annotations
import ast, hashlib, importlib.util, json, math, os
from fractions import Fraction
from pathlib import Path


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'),
                       ensure_ascii=False, allow_nan=False)+'\n').encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            digest.update(block)
    return digest.hexdigest()


def atomic(path, raw):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+'.candidate')
    require(not path.exists() and not temporary.exists(),
            'one fresh necessary private input carrier')
    temporary.write_bytes(raw)
    require(temporary.read_bytes() == raw, 'whole private carrier readback')
    temporary.replace(path)


def load(path, label):
    spec = importlib.util.spec_from_file_location(label, path)
    require(spec is not None and spec.loader is not None, 'whole pinned source')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def exact_value_prefix(proposal_module, whole_source, expected_sha):
    """Use the original complete value-producing AST verbatim, no new trial.

    The only omitted statements allocate/write derivative_1/2/3 and test the
    already imposed root identity.  They do not alter trial_value.  The owner
    binds the source's original exact hash and then the complete array hash.
    """
    require(sha(whole_source) == expected_sha,
            'the unchanged complete original TC floating proposal source')
    tree = ast.parse(whole_source)
    found = [node for node in tree.body if isinstance(node, ast.FunctionDef)
             and node.name == 'choose_all_columns']
    require(len(found) == 1, 'one whole original TC proposal factory')
    function = found[0]
    cuts = [i for i, node in enumerate(function.body)
            if isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == 'derivatives'
                    for target in node.targets)]
    require(len(cuts) == 1, 'the original post-value derivative-only tail')
    cut = cuts[0]
    require(isinstance(function.body[cut].value, ast.ListComp)
            and isinstance(function.body[-1], ast.Return),
            'the unchanged derivative-only allocation and final return')
    prefix = ast.FunctionDef(name='same_TC_value_array_only', args=function.args,
                             body=function.body[:cut]+[ast.Return(ast.Name('value', ast.Load()))],
                             decorator_list=[], returns=None, type_comment=None)
    module = ast.Module(body=[prefix], type_ignores=[])
    ast.fix_missing_locations(module)
    namespace = dict(vars(proposal_module))
    exec(compile(module, '<same-TC-value-producing-prefix>', 'exec'), namespace)
    return namespace['same_TC_value_array_only'], {
        'complete_original_proposal_source_sha256': expected_sha,
        'value_producing_prefix_AST_sha256': sha(ast.dump(module, include_attributes=False).encode()),
        'original_derivative_arrays_recomputed': 0,
        'complete_original_trial_value_hash_required': True,
    }


def restore(api_np, api_flint, input_root, private, admitted_TC,
            completed_TC_state, completed_TC_matrix, progress):
    """Return both exact original private carriers after full old SHA gates.

    admitted_TC is the complete unchanged TC owner's preflight return.  Its
    full old-input checks run before ANY numerical import in the new owner.
    The two completed objects were validated with the original TC metadata
    validators and their original whole execution receipts.
    """
    np, flint = api_np, api_flint
    input_root, private = Path(input_root), Path(private)
    manifest, roles, raws, helper, prior, rows, identity = admitted_TC
    require(completed_TC_state['input_identity'] == identity,
            'the same entire original TC preflight identity')
    old_proposal = completed_TC_state['proposal']
    require(completed_TC_matrix['proposal_identity'] == old_proposal,
            'the matrix uses the entire same original exact dyadic trial')
    require(os.environ.get('OPENBLAS_CORETYPE') == 'Haswell'
            and all(os.environ.get(key) == '1' for key in (
                'OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
                'BLIS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS')),
            'the original TC value-selection CPU branch and thread count')
    require(flint.ctx.prec == manifest['parameters']['arithmetic_bits'] == 320,
            'the original directed TC/RW precision')
    parameters = manifest['parameters']
    module = load(input_root/roles['trial_math']['path'], '_SC_same_TC_directed_math')
    proposal_module = load(input_root/roles['proposal_math']['path'], '_SC_same_TC_float_factory')
    backend, backend_receipts = helper.directed_backend(
        np, flint, raws[roles['box_math']['path']], raws[roles['fft_math']['path']])
    c = module.DirectedContext(np, flint.arb, backend['Box'], backend['CBox'],
                              backend['zeros'], backend['arb_box'],
                              backend['reduce_box'], backend['DirectedFFT']())
    reader, reader_receipt = helper.candidate_reader(np, raws[roles['candidate_reader']['path']])
    iterator, repair_receipt = helper.repair_iterator(raws[roles['repair_source']['path']])
    base = reader(input_root/roles['base_index']['path'])
    direction = reader(input_root/roles['direction_index']['path'])
    arb = flint.arb

    def read_ball(record):
        require(isinstance(record, dict), 'whole saved original ball record')
        if 'lower' in record and 'upper' in record:
            value = arb(record['lower']).lower().union(arb(record['upper']).upper())
        else:
            value = arb(record['ball'])
        require(value.is_finite(), 'the finite original whole ball')
        return value

    arrays = {}

    def allocate(name, shape):
        require(name not in arrays and all(type(n) is int and n > 0 for n in shape),
                'one fresh complete necessary private array')
        size = math.prod(shape)*8
        require(sum(item['bytes'] for item in arrays.values())+size
                <= parameters['maximum_private_live_array_bytes'],
                'the original complete private-array memory/disk bound')
        path = private/(name+'.f64')
        require(not path.exists(), 'no previous private array is overwritten')
        path.parent.mkdir(parents=True, exist_ok=True)
        value = np.memmap(path, dtype='<f8', mode='w+', shape=shape, order='C')
        arrays[name] = {'path': path, 'shape': shape, 'bytes': size, 'array': value}
        return value

    def release(name):
        info = arrays.pop(name)
        info['array'].flush()
        del info['array']
        info['path'].unlink()

    offsets, offset_receipts = helper.materialize_repairs(
        c, base, direction, iterator, prior, allocate, progress)
    definition, proposal_nodes, plan = helper.complete_plan(rows, base['radial_nodes'])
    definition_sha = sha(canonical(definition))
    require(definition_sha == old_proposal['definition_sha256']
            and sha(canonical(plan)) == old_proposal['certificate_plan_sha256']
            and len(proposal_nodes) == old_proposal['complete_trial_nodes']
            and len(plan) == old_proposal['complete_certificate_cells'],
            'the entire original true-root endpoint definition and complete plan')
    reference = proposal_module.FloatingCentreReference(
        np, rows, base, offsets['base']['midpoint'], helper.ALPHA, read_ball)
    value_factory, prefix_receipt = exact_value_prefix(
        proposal_module, raws[roles['proposal_math']['path']], roles['proposal_math']['sha256'])
    progress('necessary_same_TC_trial_value_restoration', {
        'TC_floating_proposal_QR_rematerializations': 1,
        'original_nodal_QR_calls': 0, 'old_completed_scientific_targets': 0,
        'original_derivative_arrays_recomputed': 0,
    })
    value_factory(np, reference, proposal_nodes, definition['root_index'], allocate, release, progress)
    info = arrays['trial_value']
    info['array'].flush()
    value_receipt = {'name': 'trial_value', 'shape': list(info['shape']),
                     'bytes': info['bytes'], 'sha256': file_sha(info['path']),
                     'encoding': 'little-endian binary64 row-major exact dyadics'}
    require(value_receipt == old_proposal['complete_endpoint_arrays'][0]
            and info['path'].stat().st_size == value_receipt['bytes'],
            'the SAME entire original TC trial_value bytes, no new fitted trial')
    values = np.memmap(info['path'], dtype='<f8', mode='r', shape=info['shape'], order='C')
    for start in range(0, len(values), 32):
        require(np.all(np.isfinite(values[start:start+32])), 'every original value is finite')
    require(np.array_equal(values[definition['root_index'], 97:, :], np.eye(96)),
            'the original exact physical root-even96 identity')

    def scalar_inputs(row, left, right):
        scalar = {name: module.scalar_taylor(
            c, row['intrinsic_midpoint_jets'], row['intrinsic_whole_third_jets'],
            name, *row['interval'], left, right, read_ball)
                  for name in ('beta', 'K', 'gamma', 's')}
        active = Fraction(left) < helper.CONTROL[1] and Fraction(right) > helper.CONTROL[0]
        require(not active or helper.CONTROL[0] <= Fraction(left) < Fraction(right) <= helper.CONTROL[1],
                'the unchanged original compact metric seam')
        return module.selected_intrinsic_fees(
            c, scalar, row['intrinsic_whole_third_jets'], helper.DELTA, active, read_ball)

    def scalar_point(field, coordinate):
        require(field.degree == 0, 'whole angular scalar at the actual waist')
        value = module.trial_value(c, field.coefficients, c.box(coordinate))[0, 0]
        error = float(np.max(field.error.hi))
        value = value+c.Box(-error, error)
        return arb(float(value.lo)).union(arb(float(value.hi)))

    row0 = rows[0]
    left, right = map(Fraction, row0['interval'])
    scalar = scalar_inputs(row0, left, right)
    background = helper.selected_background(
        c, base, direction, offsets, row0['pieces']['background'],
        left, right, scalar['s'], module)
    K0 = scalar_point(scalar['K'], -1)
    mean0 = scalar_point(background[1].mean(), -1)
    a0 = read_ball(row0['intrinsic_whole_third_jets']['a'])
    require(K0.upper() < 0 and mean0.upper() < 0 and a0.lower() > 0,
            'the same whole actual selected waist denominator')
    q0, ng0 = (-K0).sqrt(), a0*a0/(mean0*mean0)
    density = module.full_waist_density(c, c.Box(values[0]), q0, ng0)
    old = prior['RW_actual']
    rw_math = load(input_root/prior['RW_specs']['row_math']['path'], '_SC_same_RW_carrier_only')
    pp = prior['RW']
    factory = rw_math.ReflectedRowFactory(
        flint, pp['H_sines'], pp['H_cosines'], pp['K_sines'], pp['K_cosines'],
        H_constant=pp['zero_translation_qualification']['H_constant'],
        K_constant=pp['zero_translation_qualification']['K_constant'])

    def old_carrier(filename, kind, entries, extra, expected):
        entries = list(entries)
        document = {'kind': kind, 'definition_sha256': old['definition_sha256'],
                    **extra, 'all_real_balls': [value.str(parameters['private_RW_digits'])
                                              for value in entries]}
        raw = canonical(document)
        require(len(raw) == expected['bytes'] and sha(raw) == expected['sha256']
                and len(entries) == expected['complete_real_count'],
                'same complete original RW carrier, no old row-error evaluation')
        path = private/filename
        atomic(path, raw)
        restored = [arb(value) for value in json.loads(path.read_bytes())['all_real_balls']]
        require(all(value.contains(original) for value, original in zip(restored, entries)),
                'all original RW carrier balls read back')
        return restored

    grid = old_carrier('same-RW-grid.json', 'R149_complete_exact_compound_cosine_grid_carrier_v1',
                       factory.materialize_whole_compound_grid(), {'grid_points': 4096},
                       old['private_grid_receipt'])
    factory.base_cosines = grid
    factory.previous = [arb(1) for _ in grid]
    factory.current = list(grid)
    matrices = {'physical_primitive96': [], 'declared_incoming_cosine96': []}
    for index in range(1, 97):
        j, coefficients = factory.next_complete_row()
        require(j == index, 'the complete original sequential RW row order')
        coefficients = old_carrier(
            'same-RW-row-%03d.json'%j, 'R149_complete_exact_DFT_real_row_carrier_v1',
            coefficients, {'mode': j, 'nonnegative_modes': [0, 1024],
                           'negative_modes': 'equal by exact evenness, not selected by midpoint'},
            old['new_records']['row_%03d'%j]['carrier'])
        for name, incoming in (('physical_primitive96', False), ('declared_incoming_cosine96', True)):
            value = module.real_signed_density_pairing(c, coefficients, density, incoming=incoming)
            matrices[name].append([arb(float(a)).union(arb(float(b)))
                                   for a, b in zip(value.lo, value.hi)])
        if index % 16 == 0:
            progress('necessary_same_signed_matrix_carriers', {'complete_rows': index, 'rows': 96})
    receipts, restored_matrices = {}, {}
    for name, matrix in matrices.items():
        document = {'kind': 'TC_complete_signed_finite_matrix_carrier_v1',
                    'name': name, 'trial_definition_sha256': definition_sha,
                    'original_RW_definition_sha256': old['definition_sha256'],
                    'rows': 96, 'columns': 96,
                    'all_signed_entry_balls': [
                        [value.str(parameters['new_private_matrix_digits']) for value in row]
                        for row in matrix]}
        raw = canonical(document)
        expected = completed_TC_matrix['matrices'][name]['whole_private_carrier']
        observed = {'file': name+'.json', 'bytes': len(raw), 'sha256': sha(raw)}
        require(observed == expected, 'the whole original9216 signed matrix balls are byte-identical')
        path = private/(name+'.json')
        atomic(path, raw)
        restored = [[arb(value) for value in row]
                    for row in json.loads(path.read_bytes())['all_signed_entry_balls']]
        require(len(restored) == 96 and all(len(row) == 96 for row in restored)
                and all(value.contains(original) for row, originals in zip(restored, matrix)
                        for value, original in zip(row, originals)),
                'all signed matrix balls completely read back')
        receipts[name], restored_matrices[name] = observed, restored
    return restored_matrices, {
        'necessary_input_rematerialization_only': True,
        'original_nodal_QR_calls': 0, 'TC_floating_proposal_QR_rematerializations': 1,
        'old_completed_scientific_targets_recomputed': 0,
        'old96_residual_or_waist_or_matrix_norm_targets_recomputed': 0,
        'original_derivative_arrays_recomputed': 0,
        'complete_original_trial_value_receipt': value_receipt,
        'original_trial_value_prefix': prefix_receipt,
        'whole_original_matrix_receipts': receipts,
        'original_backend_receipts': backend_receipts,
        'original_readers': [reader_receipt, repair_receipt],
        'same_original_signed_repair_chains': offset_receipts,
        'arrays_published_or_uploaded': 0,
    }
