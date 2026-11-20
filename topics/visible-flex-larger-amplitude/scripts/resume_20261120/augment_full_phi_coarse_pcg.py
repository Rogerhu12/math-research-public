#!/usr/bin/env python3
"""Small AST augmentation of an ALREADY AUTHENTICATED complete full driver.

This is a source transform, not a parent binder or launcher.  Its caller must
first rebuild the frozen original/R671 + exact-location + optional SOC body,
then apply this exact transform when binding any resulting parent.  Matching
edit sites alone does not authenticate a supplied scientific implementation.
No driver, numerical module, matrix or field is executed by this module.
"""
import ast
import copy
import hashlib
from pathlib import Path


SCHEMA = 'complete-full-Phi-current-coarse-PCG-augmentation-v1'
FRAME_SHA256 = '324513a115a61800e105f340bd070eb50931bbe16dd66d3a8643bfe11298f2da'
MOMENTS_SHA256 = 'da083ae9b20674a29121c25d5b57ef867fba442559a50791b7fc0b43d4db5719'
PCG_SHA256 = 'dd59510599334843cf79159cafe5d2548818ab8b7fdf6813f164ee811247ad3b'
V3_SHA256 = 'fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4'
EXPECTED_EDITS = dict(arguments=1, helpers=1, source_setup=1,
                      run_report=1, solve=1, direction_report=1)


def _statements(text):
    return ast.parse(text).body


def _same(left, right):
    return ast.dump(left, include_attributes=False) == ast.dump(right, include_attributes=False)


def _assigned(node, name):
    return (isinstance(node, ast.Assign) and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name) and node.targets[0].id == name)


_RUNTIME_HELPERS = '''
def _coarse_preconditioner_sources(args, paths):
    if not args.enable_coarse_preconditioner:
        return None, None, dict(enabled=False,
            status='disabled_original_QP_call_retained', additional_J_calls=0,
            additional_JT_calls=0, no_optional_source_loaded=True)
    if args.objective != 'spectral':
        raise ValueError('The declared coarse data assembler is for the actual full spectral Phi bridge')
    if args.coarse_frame_source is None or args.coarse_moments_source is None:
        raise ValueError('Enabled coarse PCG needs both explicit frozen component sources')
    paths['coarse_frame'] = args.coarse_frame_source.resolve()
    paths['coarse_moments'] = args.coarse_moments_source.resolve()
    paths['coarse_qp_v3'] = paths['qp'].with_name('fullspace_feasible_active_cg_v3.py')
    expected = COARSE_EXPECTED_SOURCES
    records = {}
    for role, digest in expected.items():
        path = paths[role]
        if not path.is_file() or path.stat().st_size > 100000 or sha(path) != digest:
            raise ValueError('Unexpected frozen coarse-PCG source identity: '+role)
        records[role] = dict(path=str(path), sha256=digest, bytes=path.stat().st_size)
    frame_module = load('complete_current_coarse_frame', paths['coarse_frame'])
    moments_module = load('complete_current_coarse_moments', paths['coarse_moments'])
    return frame_module, moments_module, dict(enabled=True,
        sources=records, background_inverse_scale_rule='beta=1/(actual_direction_damping**2)',
        moments_stage_block=8,
        normalized_Phi_factor='k/(spectral_scale**2 * sum(stage_weights) * full_N)',
        original_operator_rows_objective_and_mother_norm_retained=True,
        source_or_layout_errors_propagate=True,
        construction_failure='Only arithmetic/resource unavailability delegates explicitly to frozen v3 before solve',
        application_failure='v4 returns a truthful truncated status; no within-solve replacement or automatic retry')


def _prepare_current_coarse_preconditioner(frame_module, moments_module,
        coordinates, height_map, basis, coarse_diagonal, coarse_chol,
        bridge, damping, provenance, progress):
    started = time.monotonic()
    frame = None
    gram = None
    data_report = None
    detail = dict(enabled=True, status='construction_started',
        actual_direction_damping=float(damping),
        additional_field_or_residual_evaluations=0, additional_J_calls=0,
        additional_JT_calls=0, unit_column_probes=0,
        unchanged_original_QP=True, actual_bridge_reused=True,
        original_coarse_diagonal_and_cholesky_reused=True)
    try:
        mu = float(damping)
        if not np.isfinite(mu) or mu <= 0:
            raise ValueError('Use the actual positive finite direction damping')
        mu_squared = mu*mu
        if not np.isfinite(mu_squared) or mu_squared <= 0:
            raise frame_module.SmallSPDUnavailable('actual damping squared',
                'Not representable as finite positive float')
        beta = 1./mu_squared
        if not np.isfinite(beta) or beta <= 0:
            raise frame_module.SmallSPDUnavailable('fixed background inverse scale',
                'The declared beta=1/mu^2 is not representable as finite positive float')
        detail['background_inverse_scale'] = beta
        frame = frame_module.CoarseFrame(coordinates, height_map, basis,
            coarse_diagonal, coarse_chol, provenance=provenance)
        detail['frame'] = frame.metadata()
        gram, data_report = moments_module.assemble_current_coarse_gram(
            bridge, frame, stage_block=8, provenance=provenance, progress=progress)
        detail['current_coarse_data_Gram'] = data_report
        preconditioner = frame_module.FixedSPDPreconditioner(frame, gram, mu, beta,
            data_provenance=data_report)
        detail.update(status='prepared_fixed_current_coarse_SPD',
            fixed_metadata=preconditioner.metadata(), fallback_to_frozen_v3=False)
        return preconditioner, detail
    except frame_module.SmallSPDUnavailable as error:
        detail.update(status='construction_unavailable_frozen_v3_selected',
            failure=error.record(), fallback_to_frozen_v3=True,
            no_jitter_no_clipping_no_changed_damping=True)
        return None, detail
    except (ArithmeticError, MemoryError) as error:
        # The frozen moment assembler uses ArithmeticError for its declared
        # nonfinite arithmetic.  Source, shape and layout ValueError are not
        # caught.  A process killed by an external memory limit cannot return
        # here and must not be described as a successful fallback.
        detail.update(status='construction_unavailable_frozen_v3_selected',
            failure=dict(kind=type(error).__name__, reason=str(error)),
            fallback_to_frozen_v3=True,
            no_jitter_no_clipping_no_changed_damping=True)
        return None, detail
    finally:
        detail['construction_seconds'] = time.monotonic()-started
        detail['dense_Gram_reference_released_before_solve'] = True
        # The successful object alone retains its frame and small factor.
        # No Gc, dense temporary, traceback or exception object is returned.
        del gram, frame
'''


_BEFORE_SOLVE = '''
coarse_preconditioner = None
coarse_preconditioner_kwargs = {}
coarse_preconditioner_detail = dict(enabled=False,
    status='disabled_original_QP_call_retained',
    additional_field_or_residual_evaluations=0,
    additional_J_calls=0, additional_JT_calls=0)
if args.enable_coarse_preconditioner:
    coarse_counts_before = counts.copy()
    coarse_parent_sha = next((item['accepted_bundle_sha256']
        for item in reversed(report['directions'])
        if item.get('accepted') and item.get('accepted_bundle_sha256')),
        report['bundle_sha256'])
    coarse_provenance = dict(direction=index, parent_bundle_sha256=coarse_parent_sha,
        observation_carrier_sha256=report['observation_carrier_sha256'],
        source_sha256_by_role=report['source_sha256_by_role'],
        derivative_source_sha256=report['source_sha256'],
        augmentation=report['coarse_preconditioner_derivation'])
    coarse_preconditioner, coarse_preconditioner_detail = _prepare_current_coarse_preconditioner(
        coarse_frame_module, coarse_moments_module, coordinates, height_map,
        basis, coarse_diagonal, coarse_chol, bridge, damping,
        coarse_provenance,
        lambda value: event(direction=index, **value))
    coarse_preconditioner_detail['additional_counted_operator_calls'] = {
        key:counts[key]-coarse_counts_before[key] for key in coarse_counts_before}
    coarse_preconditioner_kwargs = dict(preconditioner=coarse_preconditioner,
        preconditioner_metadata=coarse_preconditioner_detail.get(
            'fixed_metadata', coarse_preconditioner_detail),
        v3_source=paths['coarse_qp_v3'])
    event(event='complete_current_coarse_preconditioner_prepared', direction=index,
        status=coarse_preconditioner_detail['status'],
        construction_seconds=coarse_preconditioner_detail['construction_seconds'],
        additional_J_calls=coarse_preconditioner_detail['additional_J_calls'],
        additional_JT_calls=coarse_preconditioner_detail['additional_JT_calls'],
        background_inverse_scale=coarse_preconditioner_detail.get('background_inverse_scale'))
'''


_AFTER_SOLVE = '''
coarse_preconditioner_detail['actual_QP_status'] = qp_report.get('status')
coarse_preconditioner_detail['actual_QP_schema'] = qp_report.get('schema')
coarse_preconditioner_detail['automatic_application_failure_retry'] = False
'''


class _Augment(ast.NodeTransformer):
    def __init__(self, lineage):
        self.lineage = lineage
        self.counts = {key:0 for key in EXPECTED_EDITS}

    def visit_Module(self, node):
        node = self.generic_visit(node)
        indices = [i for i, st in enumerate(node.body)
                   if isinstance(st, ast.FunctionDef) and st.name == 'main']
        if len(indices) != 1:
            raise ValueError('Need the complete authenticated driver main function')
        helpers = _RUNTIME_HELPERS.replace('COARSE_EXPECTED_SOURCES', repr({
            'coarse_frame':FRAME_SHA256, 'coarse_moments':MOMENTS_SHA256,
            'qp':PCG_SHA256, 'coarse_qp_v3':V3_SHA256}))
        node.body[indices[0]:indices[0]] = _statements(helpers)
        self.counts['helpers'] += 1
        return node

    def visit_Expr(self, node):
        node = self.generic_visit(node)
        call = node.value
        if (isinstance(call, ast.Call) and isinstance(call.func, ast.Attribute)
                and isinstance(call.func.value, ast.Name) and call.func.value.id == 'parser'
                and call.func.attr == 'add_argument' and call.args
                and isinstance(call.args[0], ast.Constant)
                and call.args[0].value == '--qp-source'):
            self.counts['arguments'] += 1
            return [node]+_statements("""
parser.add_argument('--enable-coarse-preconditioner', action='store_true')
parser.add_argument('--coarse-frame-source', type=Path)
parser.add_argument('--coarse-moments-source', type=Path)
""")
        return node

    def visit_Assign(self, node):
        node = self.generic_visit(node)
        resolve_paths = _statements('paths = {key:path.resolve() for key,path in paths.items()}')[0]
        if _same(node, resolve_paths):
            self.counts['source_setup'] += 1
            return [node]+_statements('coarse_frame_module, coarse_moments_module, coarse_preconditioner_binding = _coarse_preconditioner_sources(args, paths)')
        if (isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name)
                and node.value.func.id == 'dict'):
            keys = {key.arg for key in node.value.keywords}
            if _assigned(node, 'report') and {'schema','bundle_sha256','directions','source_sha256_by_role'} <= keys:
                node.value.keywords.extend([
                    ast.keyword(arg='coarse_preconditioner_setup', value=ast.Name(id='coarse_preconditioner_binding', ctx=ast.Load())),
                    ast.keyword(arg='coarse_preconditioner_derivation', value=ast.parse(repr(self.lineage), mode='eval').body)])
                self.counts['run_report'] += 1
            if _assigned(node, 'record') and {'index','damping','active_geometry','qp'} <= keys:
                node.value.keywords.append(ast.keyword(arg='coarse_preconditioner',
                    value=ast.Name(id='coarse_preconditioner_detail', ctx=ast.Load())))
                self.counts['direction_report'] += 1
        target = _statements('coordinate_step, qp_report = None')[0].targets[0]
        if len(node.targets) == 1 and _same(node.targets[0], target):
            call = node.value
            expected = ast.parse('qp_module.solve', mode='eval').body
            if (not isinstance(call, ast.Call) or not _same(call.func, expected)
                    or len(call.args) != 4
                    or [ast.unparse(a) for a in call.args] != ['A','model_residual','active_rows','active_bounds']
                    or {k.arg for k in call.keywords} != {'damping','block_columns','parameters','callback'}
                    or not any(k.arg == 'damping' and isinstance(k.value, ast.Name)
                               and k.value.id == 'damping' for k in call.keywords)):
                raise ValueError('The authenticated complete QP call site changed')
            call.keywords.append(ast.keyword(arg=None,
                value=ast.Name(id='coarse_preconditioner_kwargs', ctx=ast.Load())))
            cleanup = _statements("""
coarse_preconditioner_kwargs.clear()
coarse_preconditioner = None
coarse_preconditioner_detail['frame_and_factor_released_after_solve'] = True
""")
            wrapped = ast.Try(body=[node], handlers=[], orelse=[], finalbody=cleanup)
            self.counts['solve'] += 1
            return _statements(_BEFORE_SOLVE)+[wrapped]+_statements(_AFTER_SOLVE)
        return node


def augment_driver_text(validated_text):
    """Return (derived_text, metadata), without executing the driver.

    Required caller contract: validated_text is the complete body rebuilt
    from the caller's already byte-bound frozen driver and declared earlier
    transforms.  Future parent binding must repeat this transform and compare
    the entire final AST, in addition to binding the actual source/report SHA.
    This function deliberately supplies no permissive standalone binder.

    Output is canonical Python text with a constant, path-independent header.
    Runtime lineage binds the canonical input BODY, not comments containing
    a prior launcher's scratch path.  Returned metadata also records the exact
    supplied UTF-8 bytes for this particular source-preparation invocation.
    """
    if not isinstance(validated_text, str):
        raise TypeError('Supply the already authenticated complete Python text')
    tree = ast.parse(validated_text)
    names = {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)}
    functions = {n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    if ('coarse_preconditioner_binding' in names
            or '_coarse_preconditioner_sources' in functions
            or '_prepare_current_coarse_preconditioner' in functions):
        raise ValueError('The optional coarse-PCG augmentation is already present')
    canonical_input = ast.unparse(tree)+'\n'
    own_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    lineage = dict(schema=SCHEMA, augmentation_source_sha256=own_sha,
        authenticated_input_body_sha256=hashlib.sha256(canonical_input.encode()).hexdigest(),
        source_sha256s=dict(frame=FRAME_SHA256, moments=MOMENTS_SHA256,
                           PCG=PCG_SHA256, frozen_v3=V3_SHA256),
        edits=dict(EXPECTED_EDITS),
        source_binding_scope='Caller rebuilds the entire frozen-base and earlier-transform lineage before this exact augmentation',
        background_inverse_scale_rule='beta=1/(actual_direction_damping**2)',
        moments_stage_block=8,
        original_field_target_rows_coordinates_mother_norm_and_damping_rule_unchanged=True,
        additional_J_calls=0, additional_JT_calls=0,
        application_failure_restarted_automatically=False)
    transform = _Augment(lineage)
    output_tree = ast.fix_missing_locations(transform.visit(copy.deepcopy(tree)))
    if transform.counts != EXPECTED_EDITS:
        raise ValueError('The authenticated full-driver edit sites changed: '+repr(transform.counts))
    compile(output_tree, '<authenticated-full-driver-with-current-coarse-PCG>', 'exec')
    output = ('#!/usr/bin/env python3\n'
        '# Authenticated complete-driver optional current-coarse PCG augmentation.\n'
        +ast.unparse(output_tree)+'\n')
    metadata = dict(**lineage,
        input_text_sha256=hashlib.sha256(validated_text.encode()).hexdigest(),
        output_text_sha256=hashlib.sha256(output.encode()).hexdigest(),
        output_bytes=len(output.encode()),
        output_body_sha256=hashlib.sha256((ast.unparse(output_tree)+'\n').encode()).hexdigest(),
        path_dependent_header=False, driver_executed=False,
        numerical_components_imported=False, scientific_computation_performed=False,
        parent_binder_or_launcher_supplied=False)
    return output, metadata
