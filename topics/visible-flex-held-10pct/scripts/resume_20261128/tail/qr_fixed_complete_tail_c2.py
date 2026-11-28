#!/usr/bin/env python3
"""Complete physical-R tail C2 bounds for an actual QR fixed-metric pair.

The right input is a genuine own fixed-QR actual-DN return. The left input is
either another accepted return of that identical complete fixed problem or
its genuinely accepted QR anchor, with the anchor's own coupling summary.
Each endpoint retains its real source schema, complete runtime/baseline,
physical-H packet, full Fourier spectrum and entire native mean chain.

The unchanged old exact polynomial comparison consumes every finite stage,
both actual deep collars and disks on the exact common radius partition.
Absolute height uses each new finite prefix's literal defining cut zero mode;
no height, phase or rigid alignment is performed. This is one finite pair,
not a Cauchy proof or a bound to an unprojected continuous source. Cut repair,
cylinder and marker differences require their own subsequent comparison.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import argparse
import copy
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
ANALYTIC = HERE.parent/'analytic'
SCRIPTS = HERE.parents[1]
REPO = SCRIPTS.parents[2]
SCHEMA = 'genuine-QR-fixed-problem-complete-tail-finite-C2-pair-v1'
FIXED_KIND = 'original_r53_literal_fixed_metric_qr_anchor_actual_dn_v1'
FIXED_SOURCE_KIND = 'accepted_original_support_qr_anchor_fixed_metric_actual_dn_physical_height'
ANCHOR_SOURCE_KIND = 'actual_lambda_one_qr_chord_final_physical_height'
REVIEWED = {
    'resume_20261126/seam_compare_tail_c2_v2.py':
        'efcbcf6694c7327ca7ffe062aa883dd1226b75a884d9a3fb1f7249946ba11d33',
    'resume_20261126/seam_certify_tail_geometry_v2.py':
        'ee381646dc052b8d7c9833aa693a5568982542cc11e26cfcfdf1c35edb0791ef',
    'resume_20261126/seam_export_tail_geometry_v2.py':
        '5b318a169ef74b29d10295bdc0da764e86b437cd447ca83045248c5fb576408a',
    'resume_20261126/seam_run_tail_geometry_v2.py':
        'c165678d912761163ef29cfca1eb9c4dfc4bbf3102de6a00b228ca537f727615',
    'resume_20261128/tail/qr_actual_coupled_prefix.py':
        '17cf2884fa337ef3a72d23064d2d68dc45973e97ff6722e09fa850fd317bc98a',
    'resume_20261128/tail/qr_coupled_prefix_continuous.py':
        'ef56ab160c7ebf2a16a8fe33901dad2da426d1d8ae71853b645300a53aee0b5c',
    'resume_20261128/analytic/qr_fixed_actual_cartesian_prefix.py':
        'e66f8cb57de54f4c62b84f36b6f9983ef7866cd19d959d0ff9eaa13ad856ac77',
    'resume_20261128/analytic/qr_fixed_support_actual_model.py':
        'c85a7affd7e35328bf708510cb2440b6d530f8a259a85f01f8a8f99691db9b88',
    'resume_20261128/analytic/qr_fixed_support_actual_acceptance.py':
        '045960847c115a4d28126bea63b3237a9b429f760c67ead506a59aff1c996c3e',
    'resume_20261128/analytic/qr_fixed_actual_prefix_continuous.py':
        'eb5ceef73221e761bf8de9d80e0e60454c2db19e794909a09f6859bcc157e323',
    'resume_20261128/geometry/cartesian_prefix_metric_tables.py':
        'ab8c9fb208cfa984c80768144545c9e558682eefa23169364eed9cb7986b82ba',
}
FINAL_CERTIFICATE_STATUSES = {
    'new_whole_tail_disk_metric_curvature_certified',
    'new_selected_tail_geometry_bounds_recorded',
}


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024*1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def checked_path(reference):
    path = Path(reference['path']).resolve()
    if ref(path) != reference:
        raise ValueError('A complete actual source/reference changed: '+str(path))
    return path


def read(path):
    return json.loads(Path(path).read_text())


def write(path, value):
    path = Path(path)
    temporary = path.with_name(path.name+'.tmp')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def module(name, path):
    path = Path(path).resolve()
    previous = sys.modules.get(name)
    if previous is not None:
        if Path(previous.__file__).resolve() != path:
            raise ValueError('Use a fresh process for these bound numerical source trees')
        return previous
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def reviewed(scripts, relative):
    path = Path(scripts)/relative
    if sha(path) != REVIEWED[relative]:
        raise ValueError('A reviewed source needs an explicit new version: '+str(path))
    return path


def source_metadata(source):
    return {key:copy.deepcopy(source[key]) for key in (
        'role', 'source_kind', 'source_run', 'raw', 'physical', 'final_height_binding',
        'final_packet', 'runtime', 'baseline', 'port', 'native_manifest',
        'mean_nodes', 'origin_repo', 'accepted_gate_provenance')}


def accepted_pair(args):
    """Gate real sources first; never turn the anchor into an own fixed return."""
    for relative in REVIEWED:
        reviewed(SCRIPTS, relative)
    sys.path.insert(0, str(ANALYTIC))
    reader = module('qr_fixed_actual_cartesian_prefix',
        ANALYTIC/'qr_fixed_actual_cartesian_prefix.py')
    if read(args.right_source_run).get('model_kind') != FIXED_KIND:
        raise ValueError('The right source must be a genuine own QR fixed-g actual return')
    right_record, physical, right_view, right_provenance = reader.accepted_fixed(args.right_source_run)
    del physical
    problem = copy.deepcopy(right_record['fixed_problem'])
    origin_repo = Path(problem['original_repository']).resolve()
    origin_scripts = origin_repo/'topics/visible-flex-held-10pct/scripts'
    for relative in REVIEWED:
        if relative.startswith('resume_20261126/') or '/tail/qr_' in relative:
            reviewed(origin_scripts, relative)
    fixed_context_api = module('_qr_tail_pair_fixed_continuous',
        ANALYTIC/'qr_fixed_actual_prefix_continuous.py')

    def fixed(path, record, view, provenance):
        if (record['model_kind'] != FIXED_KIND or provenance['source_kind'] != FIXED_SOURCE_KIND
                or record['fixed_problem'] != problem):
            raise ValueError('The two actual fixed fields do not have the identical full fixed problem')
        context = fixed_context_api.FixedActualContext('complete-tail-C2-pair')
        context.capture(path, record, view, provenance)
        return dict(role='own_accepted_QR_fixed_metric_return', source_kind=FIXED_SOURCE_KIND,
            source_run=ref(path), record=record, view=view, context=context,
            raw=ref(Path(path).parent/record['raw_return']['file']), physical=view['physical'],
            final_height_binding=view['height_reference'], final_packet=view['packet'],
            runtime=provenance['runtime_tail_configuration'],
            baseline=provenance['base_tail_configuration'], port=provenance['actual_source_port'],
            native_manifest=provenance['native_manifest'], mean_nodes=record['mean_nodes'],
            origin_repo=str(origin_repo), accepted_gate_provenance=provenance)

    right = fixed(args.right_source_run.resolve(), right_record, right_view, right_provenance)
    # Reconstruct the complete literal frozen target with the same actual
    # anchor constructor. This reads the original full state and initializes
    # its exact support core; it performs no BVP, native flow or Jacobian.
    model = reader.model
    anchor_context = model.accepted_input(checked_path(problem['actual_anchor']), repo=REPO,
        origin_repo=origin_repo, coupling_summary=checked_path(problem['coupling_summary']))
    design, anchor, signature = model.bootstrap(anchor_context)
    raw = model.raw_arrays(anchor_context)
    reconstructed = model.first_fixed_problem(anchor_context, design, anchor, signature, raw)
    del raw, design
    if reconstructed != problem:
        raise ValueError('The literal fixed profile/chart/core/mean does not equal its real anchor construction')
    left_path = args.left_source_run.resolve()
    provisional = read(left_path)
    if provisional.get('model_kind') == FIXED_KIND:
        if args.left_coupling_summary is not None:
            raise ValueError('An own fixed left return uses its bound anchor, not a new coupling summary')
        record, physical, view, provenance = reader.accepted_fixed(left_path)
        del physical
        left = fixed(left_path, record, view, provenance)
        pairing = 'two_own_accepted_returns_of_the_identical_complete_fixed_problem'
    else:
        if (provisional.get('model_kind') is not None or args.left_coupling_summary is None
                or ref(left_path) != problem['actual_anchor']
                or ref(args.left_coupling_summary) != problem['coupling_summary']
                or anchor_context['record'] != provisional):
            raise ValueError('The left nonfixed source must be this exact genuine QR anchor and its actual summary')
        expected = {
            'anchor_raw':'raw', 'anchor_physical':'physical',
            'anchor_final_physical_height_binding':'final_height_binding',
            'anchor_final_physical_packet':'final_packet', 'anchor_port':'port',
        }
        if any(problem[key] != anchor_context[value] for key,value in expected.items()):
            raise ValueError('A complete real anchor raw/physical/H/port identity changed')
        view = read(checked_path(anchor_context['final_height_binding']))
        provenance = anchor_context['complete_anchor_gate_provenance']
        api = module('_qr_tail_pair_anchor_continuous', reviewed(origin_scripts,
            'resume_20261128/tail/qr_coupled_prefix_continuous.py'))
        context = api.CoupledContext(args.left_coupling_summary, 'complete-tail-C2-pair')
        context.capture(left_path, provisional, view, provenance)
        summary = read(args.left_coupling_summary)
        left = dict(role='genuine_accepted_QR_anchor_without_relabelling', source_kind=ANCHOR_SOURCE_KIND,
            source_run=ref(left_path), record=provisional, view=view, context=context,
            raw=anchor_context['raw'], physical=anchor_context['physical'],
            final_height_binding=anchor_context['final_height_binding'], final_packet=anchor_context['final_packet'],
            runtime=anchor_context['tail_settings'], baseline=anchor_context['base_tail_settings'],
            port=anchor_context['port'], native_manifest=summary['native']['manifest'],
            mean_nodes=anchor_context['mean_nodes'], origin_repo=str(origin_repo),
            accepted_gate_provenance=provenance)
        pairing = 'genuine_QR_anchor_to_own_fixed_return_of_its_actual_frozen_metric'
    runtime_keys = set(model.RUNTIME_CONFIG_KEYS)
    baselines = []
    for source in (left, right):
        if (source['mean_nodes'] != problem['mean_nodes']
                or source['record']['frozen_profile'] != problem['frozen_profile']
                or source['record']['physical_tail_parameters'] != problem['physical_tail_parameters']):
            raise ValueError('An accepted field changed the actual fixed target or finite mean rule')
        runtime, baseline, port = (read(checked_path(source[key])) for key in ('runtime','baseline','port'))
        if ({key:value for key,value in runtime.items() if key not in runtime_keys} != baseline
                or port['source']['config_sha256'] != source['baseline']['sha256']
                or port['parameters'] != problem['physical_tail_parameters']
                or baseline['modes'] != source['record']['modes']):
            raise ValueError('A field lost its actual baseline/runtime/port or complete mode identity')
        for key in ('raw','physical','final_height_binding','final_packet','native_manifest'):
            checked_path(source[key])
        baselines.append({key:value for key,value in baseline.items()
                          if key not in ('modes','quadrature','steps')})
    if baselines[0] != baselines[1]:
        raise ValueError('The two full tails differ beyond their declared complete numerical resolution')
    agreement = dict(pairing=pairing, fixed_problem=problem,
        original_literal_anchor_problem_reconstructed_and_equal=True,
        own_fixed_records_keep_their_original_kind=True, anchor_keeps_its_original_kind=True,
        source_mean_nodes=problem['mean_nodes'], source_mean_gauss_order=6,
        full_baseline_agreement_excluding=['modes','quadrature','steps'],
        common_baseline_without_numerical_resolution=baselines[0],
        no_solver_or_native_flow_called=True)
    sys.path.insert(0, str(origin_scripts/'resume_20261126'))
    old = module('_qr_tail_pair_original_exact_comparer', reviewed(origin_scripts,
        'resume_20261126/seam_compare_tail_c2_v2.py'))
    roots = {REPO.resolve(), origin_repo,
             Path(right_record['repository']).resolve()}
    if left['role'] == 'own_accepted_QR_fixed_metric_return':
        roots.add(Path(left['record']['repository']).resolve())
    return left, right, agreement, old, roots


def validate_summary_producer(summary, roots):
    """Preserve actual component and aggregate source labels verbatim."""
    path = checked_path(summary['source'])
    accepted = {}
    for root in roots:
        for name in ('seam_certify_tail_geometry_v2.py','seam_run_tail_geometry_v2.py'):
            relative = 'resume_20261126/'+name
            candidate = Path(root)/'topics/visible-flex-held-10pct/scripts'/relative
            accepted[candidate.resolve()] = REVIEWED[relative]
    if path not in accepted or sha(path) != accepted[path]:
        raise ValueError('The actual full tail certificate producer is not in its bound reviewed trees')
    certifier = path.with_name('seam_certify_tail_geometry_v2.py')
    if sha(certifier) != REVIEWED['resume_20261126/seam_certify_tail_geometry_v2.py']:
        raise ValueError('The actual stage/deep proof producer changed')
    if path.name == 'seam_certify_tail_geometry_v2.py':
        if summary.get('component_certificate_summaries'):
            raise ValueError('A direct certifier report unexpectedly claims a pipeline aggregation')
        return ref(certifier), []
    components = summary.get('component_certificate_summaries')
    if (not isinstance(components,list) or len(components) != 2
            or summary.get('original_stage0_certificate_reused_unchanged') is not True
            or summary.get('stage0_certification_rerun') is not False):
        raise ValueError('The original complete pipeline component identity is missing')
    rows, loaded = {}, []
    shared = ('accepted_packet','height_identity','original_mean_chain','constants','normalization',
        'mathematical_sources','oracle_provenance','geometry_schema','spectrum',
        'spectrum_contract','representation_sources')
    for component_ref in components:
        component = read(checked_path(component_ref))
        if (component.get('status') not in FINAL_CERTIFICATE_STATUSES
                or component['source'] != ref(certifier)
                or any(component[key] != summary[key] for key in shared)):
            raise ValueError('The original component report does not certify this same complete definition')
        checked_path(component['geometry_bundle'])
        checked_path(component['shared_R_manifest'])
        for row in component['stages']:
            if row['stage'] in rows:
                raise ValueError('A component duplicates a complete finite stage')
            rows[row['stage']] = row
        loaded.append(component)
    if (loaded[0]['selected_stages'] != [0]
            or loaded[1].get('deep_collar') != summary.get('deep_collar')
            or [rows[key] for key in sorted(rows)] != summary['stages']
            or sorted(rows) != summary['selected_stages']):
        raise ValueError('The original full aggregation changed a stage, its deep collar or exact inventory')
    return ref(certifier), components


def validate_bound_tail(source, bundle, old):
    record, view = source['record'], source['view']
    identity = bundle['height_identity']
    if (bundle['accepted_packet'] != source['final_packet']
            or bundle['source_port'] != source['port']
            or bundle['finite_scope']['M'] != record['modes']
            or identity['factor'] != 1 or identity['original_arithmetic'] != 'numpy'
            or identity['reference_key'] != 'candidate_H'
            or identity['reference'] != source['final_height_binding']):
        raise ValueError('The complete finite tail does not belong to this final actual physical-H field')
    target = old.checked(identity['reference'])
    packet = old.checked(bundle['accepted_packet'])
    M = record['modes']
    def full_height_bytes(value):
        values = np.asarray(value,dtype='<f8')
        if values.shape != (M,) or not np.all(np.isfinite(values)):
            raise ValueError('A complete finite actual height vector changed')
        return values.tobytes()
    H = full_height_bytes(view['candidate_H'])
    for candidate in (target['candidate_H'], packet['request']['height'],
                      packet['response']['checkpoint']['cutHeight']):
        if full_height_bytes(candidate) != H:
            raise ValueError('A raw, partial, scaled or different physical height was substituted')
    if target['physical'] != source['physical'] or packet['config'] != read(checked_path(source['runtime'])):
        raise ValueError('The original actual physical field/runtime differs from its full packet')
    exporter = sys.modules['seam_export_tail_geometry_v2']
    if exporter.bind_height(packet, checked_path(identity['reference']), 'candidate_H', 1, 'numpy') != identity:
        raise ValueError('The complete original height identity was not reproduced')
    native = old.checked(bundle['native_record'])
    if native['manifest'] != source['native_manifest']:
        raise ValueError('The complete saved native states came from a different actual execution provider')
    return packet


# The complete initializer below changes only the real source contracts and
# aggregate producer handling. stage() and spans() are the original methods.

def complete_tail_class(original):
    read, ref, checked = original.read, original.ref, original.checked
    verify_ref, validate_inputs = original.verify_ref, original.validate_inputs
    state_match, fq = original.state_match, original.fq
    GEOMETRY_SCHEMA, DEFINITION_SHA, H = original.GEOMETRY_SCHEMA, original.DEFINITION_SHA, original.H

    class CompleteTail(original.CompleteTail):
        def __init__(self, actual_source, summary_path, roots):
            self.actual_source = actual_source
            source_path, source = actual_source['source_run']['path'], actual_source['record']
            self.source_path, self.source = Path(source_path), source
            self.summary_path = Path(summary_path)
            summary = self.summary = read(summary_path)
            if summary.get("status") not in (
                    "new_whole_tail_disk_metric_curvature_certified",
                    "new_selected_tail_geometry_bounds_recorded"):
                raise ValueError("The full actual tail certificate execution did not finish")
            self.proof_source, self.component_summaries = validate_summary_producer(summary, roots)
            verify_ref(summary["source"])
            for item in summary["mathematical_sources"].values():
                verify_ref(item)
            for key in ("geometry_bundle", "constants", "normalization"):
                verify_ref(summary[key])
            bundle, chain, manifest, index, constants = validate_inputs(
                Path(summary["geometry_bundle"]["path"]),
                Path(summary["constants"]["path"]), Path(summary["normalization"]["path"]))
            self.bundle, self.chain, self.manifest = bundle, chain, manifest
            self.index, self.constants = index, constants
            for summary_key, bundle_key in (
                    ("accepted_packet", "accepted_packet"),
                    ("shared_R_manifest", "shared_R_manifest"),
                    ("original_mean_chain", "mean_chain"),
                    ("height_identity", "height_identity"),
                    ("spectrum", "spectrum"),
                    ("spectrum_contract", "spectrum_contract"),
                    ("representation_sources", "representation_sources")):
                if summary[summary_key] != bundle[bundle_key]:
                    raise ValueError("The certificate chain changed a finite map identity")
            if summary.get("geometry_schema") != GEOMETRY_SCHEMA:
                raise ValueError("The complete map is not the explicit v2 Fourier definition")
            self.S = S = index["finite_stage_count"]
            if (type(S) is not int or S < 1 or len(chain["mean_chain"]) != S + 1
                    or summary.get("all_finite_stages_audited") is not True
                    or summary.get("finite_tail_to_its_own_deep_disk_C2") is not True
                    or index.get("all_stages_exported") is not True
                    or index.get("all_finite_stage_adjacencies_verified") is not True):
                raise ValueError("A selected-stage result is not a complete tail disk")
            self.files = {row["stage"]: row for row in manifest["files"]}
            self.proofs = {row["stage"]: row for row in summary["stages"]}
            self.nodes = {row["node"]: row for row in index["unique_boundary_nodes"]}
            if (len(self.files) != len(manifest["files"]) or set(self.files) != set(range(S))
                    or len(self.proofs) != len(summary["stages"]) or set(self.proofs) != set(range(S))
                    or len(self.nodes) != len(index["unique_boundary_nodes"])
                    or set(self.nodes) != set(range(S + 1))
                    or index["cut_node"] != self.nodes[0] or index["deep_node"] != self.nodes[S]):
                raise ValueError("The complete canonical stage/node/proof chain is missing or duplicated")
            packet_ref = bundle["accepted_packet"]
            packet = validate_bound_tail(actual_source, bundle, original)
            native = checked(bundle["native_record"])
            if not state_match(bundle["native_record"]["path"], packet):
                raise ValueError("The native representation does not use these complete accepted states")
            protocol = bundle["native_protocol_identity"]
            if protocol["status"] != "actual_native_scope_metric_abi_and_payload_cross_checked":
                raise ValueError("The source-bound original native protocol was not checked")
            for key in ("metadata", "manifest", "input", "output"):
                native_key = "static_metadata" if key == "metadata" else key
                if protocol[key] != native[native_key]:
                    raise ValueError("The saved native protocol identity changed")
                verify_ref(native[native_key])
            self.outer = fq(constants["parameters"]["rCut"])
            if self.outer != Q(self.nodes[0]["R_exact_binary"]):
                raise ValueError("The full disk does not end at its actual physical cut")
            self.mu_cut = Q(self.nodes[0]["mean_perturbation_exact_binary"])
            if self.mu_cut != fq(chain["mean_chain"][0][0]):
                raise ValueError("The full nonrotating cut mean changed")
            self.spectrum = bundle["spectrum"]
            self.keys = tuple([("planar", m) for m in self.spectrum["planar_modes"]] +
                              [("height", m) for m in self.spectrum["height_modes"]])
            deep_small = summary.get("deep_collar")
            if not deep_small:
                raise ValueError("The actual deepest-node collar certificate is missing")
            deep = self.deep = checked(deep_small["certificate"])
            if {k: v for k, v in deep_small.items() if k != "certificate"} != deep:
                raise ValueError("The deep certificate projection changed")
            if (deep["source"] != self.proof_source or deep["stage_data"] != self.files[S - 1]
                    or deep["source_stage"] != S - 1 or deep["canonical_deep_node"] != S
                    or deep["canonical_deep_value_sha256"] != self.nodes[S]["value_sha256"]
                    or deep["true_background_definition_sha256"] != DEFINITION_SHA
                    or deep["geometry_schema"] != GEOMETRY_SCHEMA
                    or deep["spectrum_contract"] != bundle["spectrum_contract"]
                    or deep["C2_outer_match_exact"] is not True
                    or deep["C2_inner_zero_two_jet_exact"] is not True
                    or deep["upper_height_sign"] != -1
                    or deep["right_Hermite_basis_exact"] != [[str(v) for v in row] for row in H]):
                raise ValueError("The actual complete collar definition changed")
            self.R0 = Q(deep["outer_R_exact"])
            self.cuff = fq(constants["parameters"]["rCuff"])
            self.Ri, self.L = (self.R0 + self.cuff) / 2, (self.R0 - self.cuff) / 2
            if (self.R0 != Q(self.nodes[S]["R_exact_binary"])
                    or Q(deep["inner_R_exact"]) != self.Ri
                    or Q(deep["collar_width_exact"]) != self.L
                    or Q(deep["cuff_R_exact"]) != self.cuff
                    or not 0 < self.cuff < self.Ri < self.R0 < self.outer):
                raise ValueError("The actual collar radius partition changed")
            self.completed_stages = 0
            self.completed_native_spans = 0


        def identity(self):
            return dict(**source_metadata(self.actual_source),
                source_model_kind=self.source.get('model_kind'),
                tail_certificate_summary=ref(self.summary_path),
                actual_summary_producer=self.summary['source'],
                actual_deep_proof_producer=self.proof_source,
                actual_component_certificate_summaries=self.component_summaries,
                geometry_bundle=self.summary['geometry_bundle'],
                accepted_packet=self.bundle['accepted_packet'],
                shared_R_manifest=self.bundle['shared_R_manifest'],
                original_mean_chain=self.bundle['mean_chain'],
                canonical_node_index=self.bundle['canonical_node_index'],
                spectrum_contract=self.bundle['spectrum_contract'], spectrum=self.spectrum,
                finite_stage_count=self.S, own_collar_R_exact=[str(self.Ri),str(self.R0)],
                original_mu_cut_exact=str(self.mu_cut),
                original_metric_gate_passed=self.summary['complete_tail_disk_metric_gate_passed'],
                original_curvature_allocation_passed=self.summary['complete_tail_disk_curvature_allocation_passed'],
                failed_original_allocations_not_relabelled_as_passed=True)

    return CompleteTail


def literal_cut_height(path, tail):
    """Read the exact zero mode of this finite map, not a sampled Z_cut."""
    report = read(path)
    source = tail.actual_source
    source['context'].require_report(report)
    if (report.get('status') != 'complete_angular_three_jet_interval_tables'
            or Path(report['source_run']).resolve() != Path(source['source_run']['path'])
            or report['source_run_sha256'] != source['source_run']['sha256']
            or report['physical_sha256'] != source['physical']['sha256']
            or report['modes'] != source['record']['modes']
            or report['homotopy'] != 1 or report['mean_nodes'] != source['mean_nodes']
            or report['source_mean_gauss_order'] != 6
            or report.get('source_record_relabelled_or_rewritten') is not False):
        raise ValueError('Use the complete genuine defining tables for this actual finite prefix')
    for file, digest in report['source_hashes'].items():
        checked_path(dict(path=file, sha256=digest))
    defining = checked_path(report['defining_jets'])
    with np.load(defining,allow_pickle=False) as data:
        knots, jets, pm, hm = (data[key] for key in ('knots','jets','planar_modes','height_modes'))
        lift, chart = data['lift_jets'], data['chart_jets']
        zero = np.flatnonzero(hm == 0)
        if (knots.dtype != np.dtype('float64') or knots.ndim != 1 or len(knots) < 2
                or knots[0] != 0 or not np.all(np.diff(knots)>0)
                or jets.dtype != np.dtype('float64')
                or jets.shape != (3,len(pm)+len(hm),len(knots))
                or pm.ndim != 1 or hm.ndim != 1
                or not np.issubdtype(pm.dtype,np.integer) or not np.issubdtype(hm.dtype,np.integer)
                or len(set(pm.tolist())) != len(pm) or len(set(hm.tolist())) != len(hm)
                or len(zero) != 1 or np.any(pm % 3 != 1) or np.any(hm % 3 != 0)
                or not all(np.all(np.isfinite(values)) for values in (knots,jets,lift,chart))
                or lift.shape[0] != 3 or chart.shape[0] != 3
                or lift.shape[-1] != len(knots) or chart.shape[-1] != len(knots)
                or np.any(lift[:,:,-1] != 0) or np.any(chart[:,:,-1] != 0)
                or report['radial_spans'] != len(knots)-1):
            raise ValueError('The finite Cartesian cut lost a full literal Fourier/zero-chart two-jet')
        with np.load(checked_path(source['physical']),allow_pickle=False) as physical:
            if knots[-1] != physical['x'][-1]:
                raise ValueError('The declared finite cut is not at the actual physical prefix endpoint')
        zcut = Q.from_float(float(jets[0,len(pm)+int(zero[0]),-1]))
        definition = dict(physical_prefix_end_exact=str(Q.from_float(float(knots[-1]))),
            literal_zero_mode_index=int(zero[0]), complete_planar_modes=pm.tolist(),
            complete_height_modes=hm.tolist(), center_width_exact=str(Q.from_float(float(data['center_width']))))
    return dict(table_report=ref(path), literal_defining_jets=report['defining_jets'],
        source_run=source['source_run'], physical=source['physical'], source_kind=source['source_kind'],
        mean_nodes=source['mean_nodes'], source_mean_gauss_order=6,
        final_physical_height_binding=source['final_height_binding'],
        exact_finite_prefix_cut_height=str(zcut), exact_entire_tail_cut_mean=str(tail.mu_cut),
        exact_background_cut_height_zb=str(zcut+tail.mu_cut), **definition,
        height_definition='The literal binary64 zeroth Fourier coefficient of the declared complete shared-Hermite prefix at its physical cut.',
        original_true_prefix_height_reinterpreted=False, sampled_height_used_as_exact=False,
        height_alignment_performed=False), zcut


def compare(args):
    started = time.monotonic()
    out = args.outdir.resolve()
    if out == REPO or REPO in out.parents:
        raise ValueError('Keep all full comparison arrays and span receipts outside Git')
    out.mkdir(parents=True,exist_ok=False)
    summary_path, spans_path = out/'summary.json', out/'common-spans.jsonl.gz'
    report = dict(schema=SCHEMA, status='validating_two_genuine_QR_same_metric_tail_maps',
        complete=False, source=ref(__file__), whole_closed_surface=False,
        Cauchy_sequence_proved=False, source_continuous_Fourier_projection_error_assumed_zero=False,
        new_BVP_or_tail_solver_invoked=False, old_other_field_bounds_reused=False,
        rigid_or_height_alignment_performed=False, exact_cut_seam_corrections_included=False,
        cylinder_and_marker_differences_included=False,
        comparison='right minus left in the same physical-R Cartesian disk coordinates')
    write(summary_path,report)
    try:
        left_source, right_source, agreement, old, roots = accepted_pair(args)
        CompleteTail = complete_tail_class(old)
        left = CompleteTail(left_source,args.left_tail_certificate,roots)
        right = CompleteTail(right_source,args.right_tail_certificate,roots)
        if left.outer != right.outer:
            raise ValueError('The two genuine fixed disks have different actual outer cuts')
        background_keys = ('parameters','cells','checkpoint_sha256','factory_sha256')
        if any(left.constants[key] != right.constants[key] for key in background_keys):
            raise ValueError('The actual backgrounds differ; symbolic cancellation is unavailable')
        lh, lz = literal_cut_height(args.left_prefix_tables,left)
        rh, rz = literal_cut_height(args.right_prefix_tables,right)
        if lh['physical_prefix_end_exact'] != rh['physical_prefix_end_exact']:
            raise ValueError('The two literal fixed target domains have different actual prefix ends')
        height_difference = [rz-lz,rz-lz]
        heights = dict(left=lh,right=rh,
            Delta_Z_cut_interval_exact=list(map(str,height_difference)),
            method='Subtract the exact defining finite cut zero modes; neither midpoint nor translation is applied.')
        modes = tuple(sorted(set(left.keys) | set(right.keys)))
        delta_mu_cut = right.mu_cut-left.mu_cut
        report.update(status='bounding_exact_common_radius_spans',
            original_exact_comparison=ref(old.__file__),
            unchanged_original_methods=['CompleteTail.stage','CompleteTail.spans','common_spans','compare_span',
                'hermite','restrict','bernstein_abs','sqrt_upper'],
            same_metric_source_contract=agreement,
            frozen_complete_problem_sha256=old.canonical_sha(agreement['fixed_problem']),
            inputs={'left':left.identity(),'right':right.identity()},
            same_true_background_definition_sha256=old.DEFINITION_SHA,
            identical_background_canceled_symbolically=True,
            domain_R_exact=['0',str(left.outer)],
            exact_mode_union={'planar':[m for kind,m in modes if kind=='planar'],
                              'height':[m for kind,m in modes if kind=='height']},
            Delta_original_mu_cut_exact=str(delta_mu_cut), literal_finite_cut_heights=heights,
            exact_height_difference='Delta Z_cut + Delta mu_cut - Delta mu(R,theta); the identical true h(R)-h(R_cut) cancels.',
            stage_mean_reset_performed=False,
            finite_projection_scope='Each own complete saved N/degree defines its own finite map; every mode and both actual collars are compared. No zero error to the unprojected continuous source is asserted.')
        write(summary_path,report)
        # These exact arithmetic kernels are the frozen original functions.
        MULTI_INDICES = old.MULTI_INDICES
        common_spans, compare_span = old.common_spans, old.compare_span
        sqrt_upper, upper_row = old.sqrt_upper, old.upper_row
        maxima = {key: Q(0) for key in MULTI_INDICES}
        first_squared = second_squared = Q(0)
        count, last_update = 0, time.monotonic()
        with gzip.GzipFile(filename=str(spans_path), mode="wb", mtime=0) as zipped:
            with io.TextIOWrapper(zipped, encoding="utf-8") as stream:
                for ordinal, low, high, ls, rs in common_spans(
                        iter(left.spans()), iter(right.spans()), left.outer):
                    bounds, first, second = compare_span(ls, rs, low, high, modes, delta_mu_cut)
                    for key in maxima:
                        maxima[key] = max(maxima[key], bounds[key])
                    first_squared, second_squared = max(first_squared, first), max(second_squared, second)
                    row = dict(common_span=ordinal, R_exact=[str(low), str(high)],
                        left_piece=ls.provenance, right_piece=rs.provenance,
                        derivative_bounds_exact={str(a)+","+str(b): str(value)
                                                 for (a, b), value in bounds.items()},
                        disk_first_Frobenius_squared_upper_exact=str(first),
                        disk_second_Frobenius_squared_upper_exact=str(second))
                    stream.write(json.dumps(row, separators=(",", ":"), allow_nan=False) + "\n")
                    count += 1
                    if time.monotonic() - last_update >= 30:
                        stream.flush()
                        progress = dict(common_spans=count, last_R_exact=str(high),
                            left_complete_stages=left.completed_stages,
                            right_complete_stages=right.completed_stages,
                            seconds=time.monotonic() - started)
                        report.update(progress=progress)
                        write(summary_path, report)
                        print(json.dumps(progress), flush=True)
                        last_update = time.monotonic()
        if left.completed_stages != left.S or right.completed_stages != right.S:
            raise ValueError("The full common partition did not consume both complete tails")
        first, second = sqrt_upper(first_squared), sqrt_upper(second_squared)
        relative_position = maxima[0, 0]
        absolute_position = relative_position+max(map(abs,height_difference))
        report.update(status='two_genuine_QR_same_metric_complete_tail_finite_C2_difference_enclosed',
            complete=True, exact_radial_spectral_comparison_complete=True,
            comparison_complete_for_declared_two_finite_maps=True,
            common_spans=count, common_span_certificate=ref(spans_path),
            exact_common_R_partition_consumed_both_complete_maps=True,
            consumed_native_spans={'left':left.completed_native_spans,'right':right.completed_native_spans},
            derivative_bounds_exact={str(a)+','+str(b):str(value) for (a,b),value in maxima.items()},
            position_difference_relative_to_Delta_Z_cut=upper_row(relative_position),
            disk_first_derivative_operator_upper=upper_row(first),
            disk_second_derivative_bilinear_upper=upper_row(second),
            Euclidean_disk_C1_C2_norm_convention='Vector Euclidean norm; operator and bilinear second derivative bounded by their full Cartesian Frobenius norms.',
            absolute_Delta_Z_cut_bounded=True,
            absolute_position_difference_upper=upper_row(absolute_position),
            absolute_C2_norm_upper=upper_row(max(absolute_position,first,second)),
            finite_pair_not_Cauchy_proof=True, seconds=time.monotonic()-started)
        write(summary_path,report)
        return report
    except Exception as exc:
        report.update(status='failed',complete=False,error=repr(exc),seconds=time.monotonic()-started)
        if spans_path.exists():
            report['partial_span_certificate'] = ref(spans_path)
        write(summary_path,report)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('left-source-run','right-source-run','left-tail-certificate',
                 'right-tail-certificate','left-prefix-tables','right-prefix-tables','outdir'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--left-coupling-summary',type=Path,
        help='Required only when the left source is the actual QR anchor, rather than an own fixed return.')
    args = parser.parse_args()
    result = compare(args)
    print(json.dumps({key:result[key] for key in ('status','complete','common_spans',
        'absolute_Delta_Z_cut_bounded','absolute_position_difference_upper',
        'disk_first_derivative_operator_upper','disk_second_derivative_bilinear_upper',
        'absolute_C2_norm_upper','Cauchy_sequence_proved','seconds')}),flush=True)


if __name__ == '__main__':
    main()

