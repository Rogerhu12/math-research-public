#!/usr/bin/env python3
"""Read a genuine fixed-g original-support actual-DN return as its own map.

The unchanged accepted run keeps its own KIND and fixed problem. Its final
saved physical endpoint H, not its raw nodal candidate, supplies the complete
tail binding. The original shared Cartesian representation, full exact core
lift, frozen source mean count and GL6 rule are reused. This is a new finite
representation of this particular return, not a transferred certificate.

Acceptance must precede importing any geometry provider: the original anchor
may live in another preserved frozen repository, and its gate checks that
Python has not already cached a provider from the wrong source tree.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import copy
import hashlib
import json
from pathlib import Path
import sys
from types import SimpleNamespace

import numpy as np
from scipy.interpolate import PPoly

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
REPO = SCRIPTS.parents[2]
sys.path.insert(0, str(HERE))
import qr_fixed_support_actual_model as model
import qr_fixed_support_actual_acceptance as acceptance
from qr_fixed_support_actual_model import sha, load, ref, checked, module

SOURCE_KIND = 'accepted_original_support_qr_anchor_fixed_metric_actual_dn_physical_height'
REVIEWED_GEOMETRY = {
    'resume_20261128/tail/actual_cartesian_prefix.py':
        '6290427a4bafb2d3e8a5d5c7da10bf43e446de45f5851e69bf3d4a00d758248b',
    'resume_20261128/tail/actual_closed_map_v2.py':
        '3742d3041daad388cc26d63fb7e4300732459f076327938a39ef92b7f3603ee5',
    'resume_20261128/tail/universal_threefold_marker.py':
        '06c97cc20934e08b217dfa04891145e61e1f926c35a8a1c88eee05cd1c8c1060',
    'finite_closure/m3_m8_closed_map/shared_jet.py':
        '0201e9037aa3a35b3d58ffaaf2121d02bb2b26b726fa6218da5f2d71bb4f6dc0',
    'finite_closure/m3_m8_closed_map/m3_shared_prefix.py':
        '39426beb80c26b6899c467413470447417bfd114beac8f59a3bc00c0d2c2a491',
    'finite_closure/m3_m8_closed_map/closed_m3_map.py':
        '1444b817abe0d77410f8c9e9b35b0ea14aa5f182767fd2de3d57527a46e51ba1',
    'finite_closure/m3_m8_closed_map/phase_angle_chart.py':
        '4fd6ebab9982cb3b8efaca27784dfa32b3a997a2a4f0132be55b3bb04b2285d3',
}
REVIEWED_PRODUCERS = {
    'seam_export_tail_geometry_v2.py':
        '5b318a169ef74b29d10295bdc0da764e86b437cd447ca83045248c5fb576408a',
    'seam_run_tail_geometry_v2.py':
        'c165678d912761163ef29cfca1eb9c4dfc4bbf3102de6a00b228ca537f727615',
}
REVIEWED_REPRESENTATION = {
    'seam_tail_spectrum_v2.py':
        'b1525fd0adec4ca28dafed371388ae3624bdfd28c6e1781dd60595253d59ab23',
    'seam_export_shared_r_tail_v2.mjs':
        'd1e9bb0d713b96bb4d01c2267ac32d5b4581d51e398ee40198fc6d0ef05cd0c8',
}


def height_bytes(value, modes):
    return acceptance.height_bytes(value, modes)


def reader_sources():
    return {str(path.resolve()):sha(path) for path in
        (Path(__file__), Path(model.__file__), Path(acceptance.__file__))}


def accepted_fixed(source_run):
    """Check the real fixed-return gate without rewriting its run or bindings."""
    source_run = Path(source_run).resolve()
    record = acceptance.accepted_actual_input(source_run, repo=REPO)
    if record['model_kind'] != model.KIND or record['fixed_problem']['parameter_zero_meaning'] != model.PARAMETER_ZERO:
        raise ValueError('Require the genuine fixed original-support actual-DN model')
    physical_ref = ref(source_run.parent/'physical.npz')
    binding_ref = ref(record['result']['height_reference'])
    target = load(checked(binding_ref))
    packet_ref = ref(record['result']['full_height_record'])
    if (physical_ref['sha256'] != record['physical_sha256']
            or binding_ref['sha256'] != record['result']['height_reference_sha256']
            or packet_ref['sha256'] != record['result']['full_height_record_sha256']
            or target['physical'] != physical_ref):
        raise ValueError('The currently checked complete physical field or endpoint binding changed')
    modes = record['modes']
    H = height_bytes(target['candidate_H'], modes)
    raw_equal = H == height_bytes(record['raw_return']['candidate_H'], modes)
    if raw_equal is not record['final_physical_H_bitwise_equal_raw_H']:
        raise ValueError('The distinct raw and physical height roles changed')
    with np.load(physical_ref['path'], allow_pickle=False) as saved:
        physical = SimpleNamespace(x=saved['x'].copy(), p=saved['p'].copy(),
            sol=PPoly.construct_fast(saved['c'].copy(), saved['x'].copy(),
                                    extrapolate=False, axis=1))
    # This is a separately labelled checked view, not a modified height file.
    view = dict(kind='verified_fixed_actual_saved_physical_endpoint_view',
        candidate_H=copy.deepcopy(target['candidate_H']), packet=packet_ref,
        physical=physical_ref, height_reference=binding_ref,
        source_mean_nodes=record['mean_nodes'])
    provenance = dict(source_kind=SOURCE_KIND, model_kind=model.KIND,
        actual_anchor_source_kind=model.ANCHOR_SOURCE_KIND,
        actual_QR_anchor_provenance=copy.deepcopy(record['fixed_problem']['complete_anchor_gate_provenance']),
        source_run=ref(source_run), physical=physical_ref,
        actual_predecessor=copy.deepcopy(record['actual_source']),
        fixed_problem=copy.deepcopy(record['fixed_problem']),
        actual_frozen_metric=copy.deepcopy(record['frozen_profile']),
        parameter_zero_meaning=model.PARAMETER_ZERO,
        source_mean_nodes=record['mean_nodes'], source_mean_gauss_order=6,
        endpoint_binding=binding_ref, full_height_packet=packet_ref,
        full_height_definition='actual_saved_physical_quintic_endpoint.candidate_H',
        full_height_binary_sha256=hashlib.sha256(H).hexdigest(),
        raw_height_bitwise_equal=raw_equal, raw_height_substituted_for_physical=False,
        numerical_repository=record['repository'], reader_repository=str(REPO),
        original_anchor_repository=record['fixed_problem']['original_repository'],
        original_anchor_coupling_summary=copy.deepcopy(record['fixed_problem']['coupling_summary']),
        native_manifest=copy.deepcopy(record['native_manifest']),
        runtime_tail_configuration=ref(record['tail_settings']),
        base_tail_configuration=ref(record['base_tail_settings']),
        actual_source_port=ref(record['linear_port_path']),
        reader_sources=reader_sources(), source_record_relabelled_or_rewritten=False,
        continuous_geometry_inherited=False, C2_limit_proved=False)
    # Only class/function definitions are imported here, after genuine
    # acceptance. No Cartesian field, mean table or tail is constructed.
    _, _, providers = geometry_libraries(record)
    provenance['actual_geometry_provider_sources'] = providers
    return record, physical, view, provenance


def geometry_libraries(record):
    """Import only after the genuine gate has selected the old anchor tree."""
    old_scripts = Path(record['fixed_problem']['original_repository']).resolve()/(
        'topics/visible-flex-held-10pct/scripts')
    prefix = sys.modules.get('actual_cartesian_prefix')
    if prefix is None or Path(prefix.SCRIPTS).resolve() != old_scripts:
        raise ValueError('Validate this fixed source first in a fresh process; its original geometry provider is not installed')
    providers = {}
    for relative, digest in REVIEWED_GEOMETRY.items():
        path = old_scripts/relative
        if sha(path) != digest or sha(SCRIPTS/relative) != digest:
            raise ValueError('The original/current Cartesian algebra needs a new explicit review: '+relative)
        providers[str(path)] = digest
    if Path(prefix.__file__).resolve() != old_scripts/'resume_20261128/tail/actual_cartesian_prefix.py':
        raise ValueError('The verified Cartesian provider path changed')
    closed_path = old_scripts/'resume_20261128/tail/actual_closed_map_v2.py'
    closed = sys.modules.get('_fixed_actual_reviewed_closed_algebra')
    if closed is None:
        closed = module('_fixed_actual_reviewed_closed_algebra', closed_path)
    elif Path(closed.__file__).resolve() != closed_path:
        raise ValueError('One process cannot mix different frozen geometry providers')
    return prefix, closed, providers


def load_fixed_prefix(source_run, *, side_modes=None, center_width=.04):
    record, physical, view, provenance = accepted_fixed(source_run)
    prefix_module, _, providers = geometry_libraries(record)
    obj = model.load_model(dict(source_run=str(Path(source_run).resolve()), repo=str(REPO)))
    obj.initial(physical.p)
    flow = obj.flow(physical.p[0])
    if (not obj.fixed or obj.cfg != record['fixed_problem']['frozen_profile']
            or model.chart_record(obj) != record['fixed_problem']['frozen_literal_radial_chart']
            or float(flow.delta) != record['frozen_profile']['delta']):
        raise ValueError('The reconstructed fixed source changed its complete metric or literal chart')
    prefix = prefix_module.ActualR53CartesianPrefix(obj, flow, physical,
        record['mean_nodes'], side_modes, center_width)
    provenance['actual_geometry_provider_sources'] = providers
    prefix.actual_fixed_provenance = provenance
    prefix.actual_fixed_height_view = view
    return record, prefix, view, provenance


def validate_bundle_binding(bundle, record, view, provenance):
    """Retain the old complete packet/spectrum gates and the new source role."""
    _, old, providers = geometry_libraries(record)
    helpers = module('_fixed_actual_radius_helpers', HERE/'verify_complete_tail_radius_identity.py')
    seam = sys.modules['seam_export_tail_geometry_v2']
    spectrum_api = sys.modules['seam_tail_spectrum_v2']
    packet_api = sys.modules['seam_cut_height_compatibility']
    identity = bundle['height_identity']
    helpers.require_unscaled(identity)
    if (bundle['accepted_packet'] != view['packet']
            or identity['reference'] != view['height_reference']
            or identity['reference_key'] != 'candidate_H'
            or bundle['source_port'] != provenance['actual_source_port']):
        raise ValueError('The complete tail is not bound to this exact final physical H/port')
    background = Path(old.SCRIPTS).parent/'notes/2026-11-20-m3-m24-warm050-execution.json'
    packet, _, _, spacing, modes, _ = packet_api.load_packet(
        Path(view['packet']['path']), Path(bundle['source_port']['path']), background)
    spectrum = seam.checked(bundle['spectrum_contract'])
    spectrum_api.canonical_contract(spectrum)
    if (spectrum != bundle['spectrum'] or spectrum['finite_scope'] != bundle['finite_scope']
            or seam.validate_packet_states(packet, modes, spacing,
                spectrum_api.degree_argument(spectrum)) != spectrum
            or modes != record['modes'] or packet['config'] != load(record['tail_settings'])):
        raise ValueError('The actual fixed return lost its complete finite tail spectrum or runtime')
    if seam.bind_height(packet, Path(identity['reference']['path']), identity['reference_key'],
            identity['factor'], identity['original_arithmetic']) != identity:
        raise ValueError('The final physical endpoint binding changed')
    H = height_bytes(view['candidate_H'], modes)
    target = seam.checked(identity['reference'])['candidate_H']
    for candidate in (target, packet['request']['height'], packet['response']['checkpoint']['cutHeight']):
        if height_bytes(candidate, modes) != H:
            raise ValueError('The full tail substituted a raw or scaled height vector')
    port = seam.checked(bundle['source_port'])
    if port['parameters'] != record['physical_tail_parameters']:
        raise ValueError('The complete tail background differs from the frozen physical metric')
    return packet, modes, dict(background_record=ref(background),
        packet_spectrum_validator=ref(packet_api.__file__),
        complete_spectrum_source=ref(spectrum_api.__file__),
        full_height_helper=ref(helpers.__file__), actual_geometry_provider_sources=providers)


def load_complete_tail(bundle_path, verified_index_path, record, view, provenance):
    """Use the original finite Fourier map with a strict cross-tree producer gate."""
    _, old, _ = geometry_libraries(record)
    bundle_path = Path(bundle_path).resolve()
    bundle = old.read(bundle_path)
    packet, modes, validation = validate_bundle_binding(bundle, record, view, provenance)
    producer = checked(bundle['source'])
    roots = {REPO.resolve(), Path(record['repository']).resolve(),
             Path(record['fixed_problem']['original_repository']).resolve()}
    accepted_producers = {root/'topics/visible-flex-held-10pct/scripts/resume_20261126'/name: digest
                          for root in roots for name,digest in REVIEWED_PRODUCERS.items()}
    if producer not in accepted_producers or sha(producer) != accepted_producers[producer]:
        raise ValueError('The real complete-tail producer is not a reviewed file in a bound source tree')
    representation_sources = {}
    for name, digest in REVIEWED_REPRESENTATION.items():
        path = producer.parent/name
        if (sha(path) != digest or bundle['representation_sources'].get(name) != ref(path)):
            raise ValueError('The actual finite spectrum/representation provider changed: '+name)
        representation_sources[name] = ref(path)

    class FixedActualFiniteTail(old.ActualFiniteTailV2):
        def __init__(self):
            self.bundle_path, self.bundle = bundle_path, bundle
            b = bundle
            if (b.get('status') != 'accepted_new_tail_shared_R_representation_exported'
                    or b.get('geometry_schema') != 'actual-m3-native-tail-geometry-v2'
                    or b.get('all_stages_exported') is not True
                    or b.get('complete_finite_C2_stage_chain') is not True):
                raise ValueError('Use a genuine complete fixed-actual shared-R representation')
            self.manifest = old.checked(b['shared_R_manifest'])
            self.chain = old.checked(b['mean_chain'])
            self.packet = packet
            saved_index = old.checked(b['canonical_node_index'])
            if (self.chain['status'] != 'all_saved_initial_states_matched_single_mean_chain'
                    or self.chain['checkpoint'] != b['accepted_packet']
                    or self.chain['native_record'] != b['native_record']
                    or self.chain['all_stage_input_maximum_difference'] != 0
                    or self.manifest['status'] != 'selected_stages_share_one_literal_R_C2_definition'
                    or self.manifest['existingCheckpoint'] != b['accepted_packet']
                    or self.manifest['input'] != b['mean_chain']
                    or saved_index['manifest'] != b['shared_R_manifest']
                    or self.manifest['spectrumContract'] != b['spectrum_contract']
                    or saved_index['spectrum_contract'] != b['spectrum_contract']):
                raise ValueError('The whole native mean, finite field, spectrum and original packet lost their common identity')
            current = old.index_shared_nodes(Path(b['shared_R_manifest']['path']),
                Path(b['mean_chain']['path']), Path(verified_index_path))
            if current != saved_index:
                raise ValueError('The complete common-node and entire-mean identity changed')
            self.index = current
            self.S = current['finite_stage_count']
            self.entries = {entry['stage']:entry for entry in self.manifest['files']}
            if set(self.entries) != set(range(self.S)):
                raise ValueError('Every original finite stage is required')
            self.spectrum = old.checked(self.manifest['spectrumContract'])
            old.validate_spectrum_container(self.manifest, self.spectrum)
            if self.spectrum != b['spectrum']:
                raise ValueError('The actual map spectrum differs from its complete packet')
            self.pm = np.asarray(self.spectrum['planar_modes'], int)
            self.hm = np.asarray(self.spectrum['height_modes'], int)
            self.P, self.C = len(self.pm), len(self.pm)+len(self.hm)
            self.parameters = self.manifest['physicalParameters']
            if any(self.parameters.get(key) != value for key,value in record['physical_tail_parameters'].items()):
                raise ValueError('The finite map changes the fixed physical tail background')
            self.cuff = np.longdouble(self.parameters['rCuff'])
            ordered = sorted(current['unique_boundary_nodes'], key=lambda item:item['node'])
            self.boundaries = np.asarray([float(old.Fraction(item['R_exact_binary'])) for item in ordered], float)
            if len(self.boundaries) != self.S+1 or np.any(np.diff(self.boundaries) >= 0):
                raise ValueError('Actual shared stage boundaries must decrease inward')
            cut, deep = self._data(0)['nodes'][-1], self._data(self.S-1)['nodes'][0]
            self.c, self.deep = np.longdouble(cut['radiusJS']), np.longdouble(deep['radiusJS'])
            self.inner = (self.deep+self.cuff)/2
            self.width = self.deep-self.inner
            self.cut_jets = np.asarray(cut['coefficients'], float)
            self.deep_jets = np.asarray(deep['coefficients'], np.longdouble)
            if (not 0 < self.cuff < self.inner < self.deep < self.c
                    or deep['meanPerturbation'] != 0 or deep['meanBackground'] != 0
                    or cut['meanPerturbation'] != self.cut_jets[0,self.P]):
                raise ValueError('The exact original collar or retained cut mean changed')
            self.mean = float(self.cut_jets[0,self.P])
            self.actual_fixed_tail_provenance = dict(source_kind=SOURCE_KIND,
                source_run=provenance['source_run'], fixed_problem=provenance['fixed_problem'],
                full_height_binding=view['height_reference'], full_height_packet=view['packet'],
                actual_producer=ref(producer), producer_repository_explicitly_bound=True,
                actual_representation_sources=representation_sources,
                original_finite_tail_methods_source=ref(old.__file__), validation=validation,
                raw_height_substituted=False, numerical_field_arrays_changed=False)

    return FixedActualFiniteTail()
