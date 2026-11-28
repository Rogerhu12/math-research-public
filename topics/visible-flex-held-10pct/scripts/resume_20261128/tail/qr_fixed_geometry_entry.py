#!/usr/bin/env python3
"""Original whole-tail/closed geometry for a genuine own fixed-QR return.

The four phases bind the already accepted fixed source without relabelling it
as its QR anchor.  Radius uses the reviewed exact radius formula and the own
complete-tail reader.  Placement executes the unchanged original main and
all of its scalar mathematics, replacing only its raw-source height gate.
Definition constructs the existing own fixed atlas without sampled queries.
Geometry executes the exact scalar transfer block of the reviewed QR proof.
The existing closed_map_complete_metric.py then consumes the resulting same
field geometry and its genuinely complete finite-tail metric certificate.

No native solve, old field certificate, new cap design or convergence claim is
introduced here.  Acceptance precedes importing geometry from a frozen tree.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import inspect
import json
from pathlib import Path
import resource
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
ANALYTIC = HERE.parent/'analytic'
sys.path.insert(0, str(ANALYTIC))
import qr_fixed_actual_cartesian_prefix as reader
from qr_fixed_actual_prefix_continuous import FixedActualContext

SCHEMA = 'own-fixed-QR-actual-complete-geometry-entry-v1'
SOURCE_KIND = reader.SOURCE_KIND
REF = reader.ref
REVIEWED = {
    'qr_complete_tail_radius_identity.py':
        '65513a57f2dcbfaed42c40c6c7a91cb87540f1b53a1fc7b89917f6becb8fb53b',
    'tail_actual_placement.py':
        'bb0af087d1649b4067c52096f2a17f41ed2ea7c7d48f8b89ec16ca5290cb2bbc',
    'qr_closed_map_marker_cylinder_geometry.py':
        '6ae95abb2341a7edf80c340c47fb53f29ae2097cb0813a46951b121c1b10ed5d',
    'closed_map_complete_metric.py':
        '4a2a799b49f01d8eb70925b4cf406d7ef39192f1faf80448fbf73cf3216d6fad',
}
FIXED_MAP_SHA = 'ea1bd53b8a5ff8c23f68d1c08e49f47f688345050556ccd04277d31afd2afbc5'
SUPPLEMENT_SHA = 'ad10604269a322d33f26f5e9e926d68d06b6ca8f836437ecf0ed585384abd115'
ORIGINAL_VALIDATOR_SHA = 'ee381646dc052b8d7c9833aa693a5568982542cc11e26cfcfdf1c35edb0791ef'
ORIGINAL_PIPELINE_SHA = 'c165678d912761163ef29cfca1eb9c4dfc4bbf3102de6a00b228ca537f727615'


def checked(item):
    return json.loads(reader.checked(item).read_text())


def write(path, value):
    path = Path(path)
    temporary = path.with_name(path.name+'.tmp')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def setup(source_run, phase):
    context = FixedActualContext('own-complete-'+phase)
    record, physical, view, provenance = context.accept(source_run)
    del physical
    prefix, atlas, providers = reader.geometry_libraries(record)
    scripts = Path(record['fixed_problem']['original_repository']).resolve()/(
        'topics/visible-flex-held-10pct/scripts')
    if Path(atlas.SCRIPTS).resolve() != scripts or Path(prefix.SCRIPTS).resolve() != scripts:
        raise ValueError('The genuine fixed gate selected a different geometry tree')
    return dict(context=context, record=record, view=view, provenance=provenance,
                scripts=scripts, atlas=atlas, providers=providers,
                source_run=Path(source_run).resolve(), phase=phase)


def scratch_out(state, path):
    path = Path(path).resolve()
    repositories = {reader.REPO.resolve(),
        Path(state['record']['repository']).resolve(),
        Path(state['record']['fixed_problem']['original_repository']).resolve()}
    if any(path == root or root in path.parents for root in repositories):
        raise ValueError('Actual complete geometry and certificate data stay outside git')
    return path


def math_module(state, name):
    """Load the reviewed numerical algebra only after the true fixed gate."""
    digest = REVIEWED[name]
    path = state['scripts']/'resume_20261128/tail'/name
    if reader.sha(path) != digest or reader.sha(HERE/name) != digest:
        raise ValueError('The original/current proof source needs explicit review: '+name)
    sys.path[:0] = [str(path.parent), str(state['scripts']/'resume_20261126')]
    value = reader.module('_own_fixed_geometry_'+name.replace('.', '_'), path)
    supplement = sys.modules.get('tail_metric_complete_supplement_v2')
    if supplement is not None:
        if (Path(supplement.__file__).resolve() != path.parent/'tail_metric_complete_supplement_v2.py'
                or reader.sha(supplement.__file__) != SUPPLEMENT_SHA
                or Path(supplement.original.__file__).resolve() != state['scripts']/(
                    'resume_20261126/seam_certify_tail_geometry_v2.py')
                or reader.sha(supplement.original.__file__) != ORIGINAL_VALIDATOR_SHA):
            raise ValueError('Use a fresh process: a complete-tail proof provider belongs to another tree')
    return value


def metadata(state, phase):
    return dict(own_fixed_geometry_adapter_schema=SCHEMA,
        own_fixed_geometry_phase=phase, source=REF(__file__),
        actual_source_kind=SOURCE_KIND, actual_fixed_source_verified=True,
        own_fixed_source_contract=copy.deepcopy(state['context'].payload),
        actual_fixed_gate_provenance=copy.deepcopy(state['provenance']),
        final_physical_height_binding=state['view']['height_reference'],
        full_height_packet=state['view']['packet'],
        final_physical_height_is_definition=True,
        raw_candidate_used_as_final_height=False,
        source_record_relabelled_or_rewritten=False,
        old_other_field_bounds_reused=False)


def require_own(state, value, phase):
    for key, wanted in metadata(state, phase).items():
        if value.get(key) != wanted:
            raise ValueError('The same own fixed geometry source is required: '+key)


def radius(args):
    state = setup(args.source_run, 'radius')
    helper = math_module(state, 'qr_complete_tail_radius_identity.py')
    out = scratch_out(state, args.outdir)
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    result = dict(schema='actual-complete-tail-radius-identity-v1', status='checking',
        geometry_bundle=REF(args.geometry_bundle), source_run=REF(args.source_run),
        constants=REF(args.constants), normalization=REF(args.normalization_certificate),
        radius_chart_identity_proved=False, complete_bundle_validated=False,
        metric_certificate_executed=False, original_tail_metric_reused=False,
        immersion_or_embedding_proved=False, prefix_C2_seam_proved=False,
        complete_surface=False, large_prefix_geometry_constructed=False,
        nonlinear_solves_executed=0, reviewed_radius_helper=REF(helper.__file__))
    result.update(metadata(state, 'radius'))
    try:
        bundle, chain, manifest, index, constants = helper.validate_inputs(
            args.geometry_bundle, args.constants, args.normalization_certificate)
        helper.require_unscaled(bundle['height_identity'])
        if (bundle.get('all_stages_exported') is not True
                or bundle.get('complete_finite_C2_stage_chain') is not True
                or index.get('all_stages_exported') is not True
                or index.get('all_finite_stage_adjacencies_verified') is not True):
            raise ValueError('The entire actual fixed finite stage chain is required')
        record, view, provenance = state['record'], state['view'], state['provenance']
        cap = reader.load_complete_tail(args.geometry_bundle, out/'verified-node-index.json',
            record, view, provenance)
        port = checked(bundle['source_port'])
        if (cap.S != index['finite_stage_count'] or set(cap.entries) != set(range(cap.S))
                or any(cap.parameters.get(k) != v for k,v in port['parameters'].items())
                or any(cap.parameters.get(k) != v for k,v in constants['parameters'].items())):
            raise ValueError('The complete fixed map, true background and actual port differ')
        method_hashes = helper.verify_reviewed_radius_source(Path(state['atlas'].__file__))
        stage_entry = cap.entries[0]
        stage = checked(stage_entry)
        helper.validate_spectrum_container(stage, bundle['spectrum'], stage=True)
        node = stage['nodes'][-1]
        if (stage['rawCell'] != 0 or stage['rawSegment'] != 8 or stage['rawRight'] != 1
                or node['canonicalNode'] != 0 or node['xi'] != 1 or node['sourceX'] != 1):
            raise ValueError('The selected endpoint is not the actual outer stage-0 cut')
        exact = helper.exact_binary
        c, Rc = exact(node['radiusJS']), exact(cap.parameters['rCut'])
        if (exact(cap.c) != c or Q(index['cut_node']['R_exact_binary']) != c
                or exact(constants['parameters']['rCut']) != Rc
                or exact(port['parameters']['rCut']) != Rc):
            raise ValueError('The actual map and background use different literal radii')
        delta = c-Rc
        result.update(complete_bundle_validated=True, source_kind=SOURCE_KIND,
            prefix_source_gate=dict(source_kind=SOURCE_KIND, source_run=REF(args.source_run),
                endpoint_binding=view['height_reference'], bound_endpoint_packet=view['packet'],
                complete_fixed_gate_provenance=provenance,
                raw_candidate_is_height_definition=False),
            height_identity=bundle['height_identity'],
            expected_complete_height_sha256=hashlib.sha256(
                reader.height_bytes(view['candidate_H'], record['modes'])).hexdigest(),
            accepted_packet=bundle['accepted_packet'], spectrum_contract=bundle['spectrum_contract'],
            finite_scope=bundle['finite_scope'], planar_modes=bundle['spectrum']['planar_modes'],
            height_modes=bundle['spectrum']['height_modes'], full_stage_count=cap.S,
            all_stage_spectra_and_shared_means_revalidated=True,
            original_canonical_index=bundle['canonical_node_index'],
            independently_recomputed_index=REF(out/'verified-node-index.json'),
            actual_stage0=stage_entry, saved_cut_radius_exact=str(c),
            physical_cut_radius_exact=str(Rc), reparameterization_delta_exact=str(delta),
            closed_map_source=REF(state['atlas'].__file__), reviewed_radius_methods=method_hashes,
            actual_complete_tail_reader=REF(reader.__file__),
            actual_complete_tail_provenance=cap.actual_fixed_tail_provenance,
            actual_closed_cap_c_exactly_saved_stage0_radius=True,
            current_radius_method_default_width_exact=str(exact(.02)))
        if delta:
            result.update(status='validated_complete_bundle_has_nonidentity_radius_chart',
                separate_inverse_chart_transfer_required=True,
                R75_outer_radius_domain_c_le_Rc=bool(c <= Rc))
            return result, 2
        # Only two real input radii are used by this exact identity.  This is
        # not a fabricated accepted prefix or a substitute full geometry map.
        from types import SimpleNamespace
        point = SimpleNamespace(c=cap.c, R=float(cap.parameters['rCut']))
        if exact(cap.c-np.longdouble(point.R)) != 0:
            raise ArithmeticError('The live radius evaluator lost the exact zero difference')
        diagnostic = []
        for R in (np.longdouble(0), np.longdouble(point.R)/2,
                  np.longdouble(point.R)-np.longdouble(.02), np.longdouble(point.R)):
            r, first, second = state['atlas'].ActualCutTarget.perturbation_radius(point, R)
            if exact(r) != exact(R) or exact(first) != 1 or exact(second) != 0:
                raise ArithmeticError('The reviewed zero-delta evaluator changed')
            diagnostic.append(dict(R_exact=str(exact(R)), r_exact=str(exact(r)),
                first_exact=str(exact(first)), second_exact=str(exact(second))))
        result.update(status='complete_unscaled_tail_radius_chart_identity_proved',
            radius_chart_identity_proved=True, live_evaluator_delta_exact='0',
            identity_domain_exact=['0', str(Rc)],
            mathematical_identity="r(R)=R, r'(R)=1, r''(R)=0; the defining real difference c-Rc is exactly zero",
            proof_basis='Exact rational endpoint equality and the bound original radius formula; not a sampled inference',
            numerical_radius_function_diagnostics=diagnostic,
            separate_inverse_chart_transfer_required=False)
        return result, 0
    except Exception as error:
        result.update(status='complete_tail_radius_identity_not_verified', error=repr(error))
        return result, 1
    finally:
        result.update(seconds=time.monotonic()-started,
            maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        write(out/'radius-identity.json', result)


def make_placement_height(core, source_gate):
    """Replace one source-only section; retain the original exact height math."""
    text = inspect.getsource(core.actual_height)
    start = "    source = json.loads(Path(table['source_run']).read_text())\n"
    finish = "    if ref(cut['defining_jets']['path']) != cut['defining_jets']:\n"
    if text.count(start) != 1 or text.count(finish) != 1:
        raise ValueError('The reviewed raw-source placement gate changed')
    before, body = text.split(start)
    replaced, after = body.split(finish)
    replacement = '    source_ref, identity = _own_fixed_source_gate(args, cut, table, bundle, manifest)\n'
    generated = before+replacement+finish+after
    scope = dict(vars(core), _own_fixed_source_gate=source_gate)
    exec(compile(generated, str(Path(__file__).resolve())+'::original_actual_height', 'exec'), scope)
    evidence = dict(original_actual_height_source_sha256=hashlib.sha256(text.encode()).hexdigest(),
        original_source_only_section_sha256=hashlib.sha256((start+replaced).encode()).hexdigest(),
        generated_height_function_sha256=hashlib.sha256(generated.encode()).hexdigest(),
        unchanged_height_math_suffix_sha256=hashlib.sha256((finish+after).encode()).hexdigest(),
        original_main_reused_without_edit=True,
        original_main_source_sha256=hashlib.sha256(inspect.getsource(core.main).encode()).hexdigest())
    return scope['actual_height'], evidence


def placement(args):
    state = setup(args.source_run, 'placement')
    core = math_module(state, 'tail_actual_placement.py')
    scratch_out(state, args.outdir)

    def source_gate(original_args, cut, table, bundle, manifest):
        context, record, view = state['context'], state['record'], state['view']
        if (Path(table['source_run']).resolve() != state['source_run']
                or REF(table['source_run']) != REF(state['source_run'])):
            raise ValueError('The literal cut tables belong to another fixed return')
        context.require_report(table)
        context.require_report(cut)
        reader.validate_bundle_binding(bundle, record, view, state['provenance'])
        if (any(manifest['physicalParameters'].get(k) != v
                for k,v in record['physical_tail_parameters'].items())):
            raise ValueError('The finite tail changes the fixed physical background')
        proof = checked(REF(original_args.radius_identity))
        require_own(state, proof, 'radius')
        if (proof['source_run'] != REF(state['source_run'])
                or proof['accepted_packet'] != view['packet']
                or proof['height_identity'] != bundle['height_identity']
                or proof['prefix_source_gate']['complete_fixed_gate_provenance'] != state['provenance']):
            raise ValueError('The radius proof uses another actual final physical height')
        return REF(state['source_run']), bundle['height_identity']

    adapted, evidence = make_placement_height(core, source_gate)
    core.actual_height = adapted
    original_writer = core.write

    def own_writer(path, value):
        if isinstance(value, dict) and 'source' in value:
            value = dict(value)
            value.update(metadata(state, 'placement'))
            value.update(reused_original_scalar_placement_source=REF(core.__file__),
                source_gate_adaptation=evidence,
                all_original_placement_scalar_formulas_and_main_reused=True)
        original_writer(path, value)

    core.write = own_writer
    argv = [str(core.__file__)]
    for name in ('geometry_bundle', 'constants', 'normalization_certificate',
                 'cut_summary', 'radius_identity', 'outdir', 'disk_reserve_mib'):
        argv.extend(['--'+name.replace('_','-'), str(getattr(args, name))])
    for path in args.original_summary:
        argv.extend(['--original-summary', str(path)])
    previous = sys.argv
    try:
        sys.argv = argv
        core.main()
    finally:
        sys.argv = previous
    return checked(REF(args.outdir/'summary.json')), 0


def definition(args):
    state = setup(args.source_run, 'definition')
    path = ANALYTIC/'qr_fixed_actual_closed_map.py'
    if reader.sha(path) != FIXED_MAP_SHA:
        raise ValueError('The own fixed complete atlas source changed')
    api = reader.module('_own_fixed_geometry_atlas_entry', path)
    out = scratch_out(state, args.outdir)
    out.mkdir(parents=True, exist_ok=False)
    node_path = out/'verified-node-index.json'
    value = api.load_closed_map(args.source_run, args.geometry_bundle, node_path,
        cut_width=args.cut_width, cylinder_half_length=args.cylinder_half_length,
        canonical_r67_marker=True)
    try:
        if value.actual_fixed_provenance != state['provenance']:
            raise ValueError('The constructed atlas belongs to another fixed return')
        chart = value.phase_chart.report()
        # The original chart report includes a numerical interpolation
        # diagnostic which may have long-double dtype. Only that diagnostic
        # is rounded for JSON display; all exact chart bounds stay rational.
        display = []
        for item in chart['numerical_source_chart_difference_orders_0_1_2']:
            number = float(item)
            if not np.isfinite(item) or not np.isfinite(number) or (item != 0 and number == 0):
                raise ValueError('A sampled chart diagnostic is not representable in JSON')
            display.append(number)
        chart['numerical_source_chart_difference_orders_0_1_2'] = display
        report = dict(status='own_fixed_actual_complete_closed_map_defined',
            source_run=REF(args.source_run), geometry_bundle=REF(args.geometry_bundle),
            full_node_check=REF(node_path), own_fixed_atlas_source=REF(path),
            complete_atlas_definition=value.definition_provenance,
            full_source_height_identity_checked=True,
            source_tail_is_own_fixed_actual=True,
            actual_new_finite_closed_map_constructed=True,
            complete_finite_stage_count=value.cap.S, modes=value.prefix.M,
            cut_width=args.cut_width, cylinder_half_length=value.cylinder_half_length,
            marker_strength=value.marker_strength, canonical_r67_marker=True,
            canonical_marker_metadata=value.r67_marker.metadata(),
            canonical_marker_source=value.definition_provenance['canonical_R67_marker_source'],
            phase_chart=chart,
            source_chart_difference_display_is_not_an_outward_or_continuous_bound=True,
            full_saved_spectrum_and_entire_mean_retained=True,
            numerical_point_queries_executed=0, continuous_metric_certificate=False,
            reach_certificate=False, C2_limit_proved=False, readme_completion_claimed=False)
        report.update(metadata(state, 'definition'))
        write(out/'definition.json', report)
        return report, 0
    finally:
        value.close()


def scalar_transfer(core):
    """Execute the reviewed scalar block verbatim, including all its gates."""
    text = inspect.getsource(core.main)
    start = "    width = Q.from_float(query['cut_width'])\n"
    end = '    scripts = Path(__file__).resolve().parents[2]\n'
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError('The reviewed complete geometry scalar block changed')
    block = start+text.split(start)[1].split(end)[0]
    generated = ('def unchanged_scalar_transfer(query, cut, height, placement, constants):\n'
                 +block+'    return locals()\n')
    scope = dict(vars(core))
    exec(compile(generated, str(Path(core.__file__).resolve())+'::unchanged_scalar_transfer', 'exec'), scope)
    return scope['unchanged_scalar_transfer'], hashlib.sha256(block.encode()).hexdigest()


def geometry(args):
    state = setup(args.source_run, 'geometry')
    core = math_module(state, 'qr_closed_map_marker_cylinder_geometry.py')
    if args.phase_end <= 0:
        raise ValueError('Specify the positive exact phase interval of this same family')
    refs = [REF(path) for path in (args.cut_prefix_report, args.placement_report,
            args.complete_original_certificate, args.complete_map_definition)]
    cut_ref, placement_ref, complete_ref, definition_ref = refs
    cut, place, complete, query = map(checked, refs)
    height = checked(place['absolute_height'])
    state['context'].require_report(cut)
    require_own(state, place, 'placement')
    require_own(state, height, 'placement')
    require_own(state, query, 'definition')
    bundle_ref = height['geometry_bundle']
    bundle = checked(bundle_ref)
    radius_proof = checked(height['physical_R_identity'])
    require_own(state, radius_proof, 'radius')
    constants = checked(height['constants'])
    reader.validate_bundle_binding(bundle, state['record'], state['view'], state['provenance'])
    if (cut['status'] != 'continuous_full_cut_prefix_metric_geometry_certified'
            or not cut['prefix_geometry_certified'] or not cut['all_phase_prefix_bounds']
            or place['status'] != 'same_actual_tail_absolute_placement_and_global_curvature_certified'
            or not place['complete_deep_collar_and_plain_disks_included']
            or not place['phase_and_upper_lower_reflection_invariant']
            or Q(place['cylinder_half_length_exact']) != 0
            or Q(place['marker_amplitude_exact']) != 0):
        raise ValueError('Complete same-map unshifted prefix and tail bounds are required')
    for path, digest in cut['source_hashes'].items():
        if reader.sha(path) != digest:
            raise ValueError('A genuine fixed cut proof source changed: '+path)
    for item in (place['source'], complete['source'], height['source'], height['prefix_source_run'],
                 height['constants'], height['normalization'], height['entire_mean'],
                 height['accepted_packet'], cut['defining_jets'], query['full_node_check'],
                 query['canonical_marker_source'], query['own_fixed_atlas_source']):
        if REF(item['path']) != item:
            raise ValueError('An actual complete same-field definition changed: '+item['path'])
    if (query['status'] != 'own_fixed_actual_complete_closed_map_defined'
            or query['own_fixed_atlas_source'] != REF(ANALYTIC/'qr_fixed_actual_closed_map.py')
            or query['own_fixed_atlas_source']['sha256'] != FIXED_MAP_SHA
            or query['source_run'] != REF(args.source_run)
            or height['prefix_source_run'] != REF(args.source_run)
            or query['geometry_bundle'] != bundle_ref
            or cut['geometry_bundle'] != bundle_ref['path']
            or cut['geometry_bundle_sha256'] != bundle_ref['sha256']
            or cut['source_run_sha256'] != REF(args.source_run)['sha256']
            or height['cut_certificate'] != cut_ref
            or not query['actual_new_finite_closed_map_constructed']
            or not query['full_source_height_identity_checked']
            or query['source_tail_is_own_fixed_actual'] is not True
            or not query['canonical_r67_marker'] or query['marker_strength'] != 0
            or query['complete_atlas_definition']['actual_fixed_source'] != state['provenance']):
        raise ValueError('Use this own fixed physical-H atlas, exact cut and unchanged canonical cap')
    pipeline = state['scripts']/'resume_20261126/seam_run_tail_geometry_v2.py'
    if (reader.sha(pipeline) != ORIGINAL_PIPELINE_SHA or complete['source'] != REF(pipeline)
            or complete['geometry_bundle'] != bundle_ref
            or complete['component_certificate_summaries'] != place['original_geometric_summaries']
            or complete['constants'] != height['constants']
            or complete['normalization'] != height['normalization']
            or complete['original_mean_chain'] != height['entire_mean']
            or complete['accepted_packet'] != height['accepted_packet']
            or not complete['all_finite_stages_audited']
            or not complete['finite_tail_to_its_own_deep_disk_C2']
            or not bundle['all_stages_exported'] or not bundle['complete_finite_C2_stage_chain']
            or bundle['height_identity']['factor'] != 1
            or query['full_node_check']['sha256'] != bundle['canonical_node_index']['sha256']):
        raise ValueError('The unchanged complete finite/deep C2 certificates belong to another field')
    if (not radius_proof['radius_chart_identity_proved']
            or not radius_proof['complete_bundle_validated']
            or radius_proof['geometry_bundle'] != bundle_ref
            or Q(radius_proof['reparameterization_delta_exact']) != 0):
        raise ValueError('The actual same-field physical-R identity remains required')
    transfer, block_sha = scalar_transfer(core)
    numbers = transfer(query, cut, height, place, constants)
    original = core.original
    n = numbers
    dependencies = {str(Path(__file__).resolve()), str(ANALYTIC/'qr_fixed_actual_closed_map.py'),
                    str(Path(core.__file__).resolve()), str(pipeline)}
    dependencies.update(state['context'].adapter_sources)
    dependencies.update(state['providers'])
    dependencies.update(str(state['scripts']/'resume_20261128/tail'/name) for name in REVIEWED)
    topic = state['scripts'].parent
    report = dict(status='actual_complete_marked_column_closed_C2_geometry_certified',
        source_dependencies=[REF(path) for path in sorted(dependencies)],
        actual_complete_map_definition=definition_ref,
        sampled_query_required_or_used_as_continuous_bound=False,
        unchanged_scalar_transfer_source=REF(core.__file__),
        unchanged_scalar_transfer_block_sha256=block_sha,
        phase_interval_exact=['0', str(args.phase_end)],
        phase_time_definition='alpha(t)=('+str(args.phase_end)+')*t, 0<=t<=1',
        whole_geometry_invariant_under_held_rigid_frame=True,
        cut_prefix=cut_ref, absolute_tail_placement=placement_ref,
        complete_original_tail_certificate=complete_ref,
        absolute_height=place['absolute_height'], geometry_bundle=bundle_ref,
        source_run=REF(args.source_run), entire_mean=height['entire_mean'],
        accepted_packet=height['accepted_packet'], physical_R_identity=height['physical_R_identity'],
        finite_stage_count=place['finite_stage_count'],
        literal_span_count=place['original_literal_span_count'],
        cut_width_exact=str(n['width']), cylinder_half_length_exact_binary=str(n['half_length']),
        cylinder_total_length_exact_binary=str(n['ell']),
        cylinder_total_length_equals_rational_one_over_200=(n['ell'] == Q(1,200)),
        canonical_marker=n['metadata'], marker_source=query['canonical_marker_source'],
        phase_chart_exact_rho_lower=str(n['rho_min']),
        cap_height_after_column_exact_interval=[str(n['cap_height_low']), str(n['cap_height_high'])],
        cap_support_lower=original.lower_row(n['cap_support']),
        cap_curvature_upper=original.upper_row(n['cap_curvature']),
        whole_radius_upper=original.upper_row(n['whole_radius']),
        whole_diameter_upper=original.upper_row(n['diameter']),
        whole_support_lower=original.lower_row(n['support']),
        whole_principal_curvature_upper=original.upper_row(n['curvature']),
        whole_reach_lower=original.lower_row(n['reach']),
        reach_over_initial_diameter_lower=original.lower_row(n['ratio']),
        reach_ratio_above_three_percent=n['ratio'] > Q(3,100),
        center_full_Cartesian_two_jet='Gamma, e_z, 0, Gamma_u, Gamma_uu, 0 in the exact material-angle chart',
        center_identity='The complete center target has Xss=b*Gamma_u, theta_ss=b and theta_s=0; the same inverse angle chart cancels Xss exactly.',
        core_column_geometric_bounds_inherited_from_same_prefix_center=True,
        prefix_tail_real_arclength_two_jets_shared=True,
        all_finite_tail_common_two_jets_and_deep_collar_retained=True,
        regular_Cartesian_disks_and_cap_boundary_two_jets_retained=True,
        all_phase_continuous_C2_immersion_sphere=True,
        all_phase_embedding_and_reach_by_existing_positive_support_theorem=True,
        prior_polynomials_integrals_or_continuous_boxes_recomputed=False,
        mathematical_results=[REF(topic/'results'/name) for name in (
            'R23-shared-jets-closed-c2-geometry.md',
            'R54-transverse-held-arc-and-short-cylinder-window.md',
            'R67-universal-threefold-marker-and-euclidean-noncongruence.md')],
        full_metric_certificate_claimed=False, euclidean_noncongruence_claimed=False,
        exact_lambda_one_held_arc_claimed=False, exact_isometric_limit_claimed=False,
        source_is_accepted_fixed_metric_refinement_return=True,
        fixed_problem_refinement_limit_claimed=False, readme_completion_claimed=False)
    report.update(metadata(state, 'geometry'))
    out = scratch_out(state, args.outdir)
    out.mkdir(parents=True, exist_ok=False)
    write(out/'summary.json', report)
    return report, 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='phase', required=True)
    p = commands.add_parser('radius')
    for name in ('source-run', 'geometry-bundle', 'constants', 'normalization-certificate', 'outdir'):
        p.add_argument('--'+name, type=Path, required=True)
    p = commands.add_parser('placement')
    for name in ('source-run', 'geometry-bundle', 'constants', 'normalization-certificate',
                 'cut-summary', 'radius-identity', 'outdir'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--original-summary', type=Path, action='append', required=True)
    p.add_argument('--disk-reserve-mib', type=int, default=128)
    p = commands.add_parser('definition')
    for name in ('source-run', 'geometry-bundle', 'outdir'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--cut-width', type=float, required=True)
    p.add_argument('--cylinder-half-length', type=float, required=True)
    p = commands.add_parser('geometry')
    for name in ('source-run', 'cut-prefix-report', 'placement-report',
                 'complete-original-certificate', 'complete-map-definition', 'outdir'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--phase-end', type=Q, required=True)
    args = parser.parse_args()
    result, code = globals()[args.phase](args)
    print(json.dumps(dict(status=result['status'], phase=args.phase,
                         actual_source_kind=SOURCE_KIND, output=str(args.outdir.resolve()))), flush=True)
    raise SystemExit(code)


if __name__ == '__main__':
    main()
